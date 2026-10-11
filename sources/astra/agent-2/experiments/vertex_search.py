"""Own-centroid convex-hull searches, bounded to <=85 input points.
These are numerical searches, not exact acceptance proofs.
"""
import os
os.environ.setdefault('JAX_ENABLE_X64','true')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import sys,json,time,heapq
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from geometry import escape,mass
ROOT=Path(__file__).resolve().parents[1]

def live_hull(X):
    h=ConvexHull(X)
    if len(h.vertices)<12:raise ValueError('Outside research domain: fewer than12 hull vertices')
    tri=h.simplices.copy()
    a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]]
    sign=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    tri[sign]=tri[sign][:,[0,2,1]]
    # Padding allows one JIT compilation for each N.
    pad=np.tile(tri[0],(2*len(X)-4-len(tri),1));mask=np.r_[np.ones(len(tri)),np.zeros(len(pad))]
    return np.r_[tri,pad],mask,h.vertices

def physical(X,tri,mask):
    a,b,c=X[tri[:,0]],X[tri[:,1]],X[tri[:,2]]
    weights=np.einsum('ij,ij->i',a,np.cross(b,c))*mask
    volume=weights.sum()/6
    centroid=np.sum(weights[:,None]*(a+b+c),axis=0)/(24*volume)
    Z=X-centroid;n=np.cross(b-a,c-a);h=np.einsum('ij,ij->i',n,a-centroid)
    Y=n/h[:,None]
    return Z,Y,centroid,volume

def matrix_score(X):
    from geometry import angular_scores
    return angular_scores(X)

def rooted_parents(X,valid,mode):
    score=matrix_score(X);score[:,~valid]=-np.inf;root=int(np.argmax(np.where(valid,np.sum(X*X,axis=1),-np.inf)))
    if mode=='greedy':
        parent=np.argmax(score,axis=1);parent[root]=root
        return parent,root
    costs=np.maximum(-score+1e-5,0)**2+1e-12
    # Reverse complete-graph Dijkstra. Positive outward witnesses cost ~zero.
    distance=np.full(len(X),np.inf);distance[root]=0;parent=np.full(len(X),root);seen=np.zeros(len(X),bool)
    for _ in range(int(valid.sum())):
        j=int(np.argmin(np.where(seen|~valid,np.inf,distance)))
        if not np.isfinite(distance[j]):break
        seen[j]=True
        cand=distance[j]+costs[:,j];sel=(cand<distance)&~seen&valid
        distance[sel]=cand[sel];parent[sel]=j
    parent[~valid]=root;parent[root]=root
    return parent,root

@jax.jit
def value_grad_core(X,tri,mask,pu,ps,umask,smask,margin):
    def fun(P):
        a,b,c=P[tri[:,0]],P[tri[:,1]],P[tri[:,2]]
        six=jnp.sum(a*jnp.cross(b,c),axis=1)*mask
        centroid=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six))
        Z=P-centroid;n=jnp.cross(b-a,c-a);h=jnp.sum(n*(a-centroid),axis=1)
        Y=n/h[:,None]
        def score(Q,parent):
            delta=Q[parent]-Q
            return jnp.sum(Q*delta,axis=1)/(jnp.sqrt(jnp.sum(Q*Q,axis=1))*jnp.sqrt(jnp.sum(delta*delta,axis=1)+1e-24))
        u=score(Z,pu);s=score(Y,ps)
        ur=jnp.maximum(margin-u,0)*umask;sr=jnp.maximum(margin-s,0)*smask
        return jnp.sum(ur*ur)+jnp.sum(sr*sr)
    return jax.value_and_grad(fun)(X)

class Search:
    def __init__(self,X,out,mode='forest',margin=1e-5):
        self.X=X;self.out=out;self.out.mkdir(parents=True,exist_ok=True);self.mode=mode;self.margin=margin
        self.best=(np.inf,np.inf);self.calls=0;self.history=[];self.started=time.time();self.target=False
    def eval(self,flat):
        X=flat.reshape(self.X.shape)
        try:tri,mask,vertices=live_hull(X)
        except ValueError:return 1e4,np.zeros_like(flat)
        Z,Y,c,vol=physical(X,tri,mask)
        validu=np.zeros(len(X),bool);validu[vertices]=True;valids=mask.astype(bool)
        pu,ru=rooted_parents(Z,validu,self.mode);ps,rs=rooted_parents(Y,valids,self.mode)
        um=validu.astype(float);um[ru]=0;sm=mask.copy();sm[rs]=0
        cost,grad=value_grad_core(X,tri,mask,pu,ps,um,sm,self.margin)
        cost=float(cost);grad=np.array(grad);self.calls+=1
        ue=matrix_score(Z);ue[:,~validu]=-np.inf;us=ue.max(axis=1)
        se=matrix_score(Y);se[:,~valids]=-np.inf;ss=se.max(axis=1)
        U=int(np.sum((us<0)&validu));S=int(np.sum((ss<0)&valids));V=len(vertices);F=int(mask.sum());E=V+F-2
        floor=min(np.sort(us[validu])[1],np.sort(ss[valids])[1])
        key=(S+U,cost)
        if key<self.best:
            self.best=key
            info={'S':S,'U':U,'V':V,'E':E,'F_tri':F,'cost':cost,'floor':float(floor),'calls':self.calls,'seconds':time.time()-self.started,'mode':self.mode,'centroid':c.tolist(),'volume':float(vol)}
            self.history.append(info)
            np.savez(self.out/'best.npz',X=X,tri=tri[mask>0],Y=Y[mask>0])
            (self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            if S+U<=4 or self.calls<3:print(str(self.out.name),info,flush=True)
        if S==U==1 and floor>1e-10:
            self.target=True;np.savez(self.out/'numerical_target.npz',X=X,tri=tri[mask>0],Y=Y[mask>0]);print('NUMERICAL_TARGET',str(self.out),float(floor),flush=True)
        return cost,grad.ravel()
    def run(self,rounds=10,iterations=200):
        X=self.X.copy()
        for k in range(rounds):
            self.mode='forest' if k%3!=2 else 'greedy'
            opt=minimize(self.eval,X.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':iterations,'maxls':30,'ftol':1e-15,'gtol':1e-10,'maxcor':20})
            X=opt.x.reshape(X.shape)
            np.savez(self.out/f'round_{k}.npz',X=X)
            print(self.out.name,'round',k,'loss',opt.fun,'nit',opt.nit,'msg',opt.message,'best',self.best,flush=True)
            if self.target:return
            # Actual hull centroid, invariant scale and location reset.
            tri,m,v=live_hull(X);Z,Y,c,vol=physical(X,tri,m);X=Z/(vol**(1/3))
        self.X=X

def starting_subset(X,n,seed):
    rng=np.random.default_rng(seed);directions=X/np.linalg.norm(X,axis=1)[:,None]
    # Spatial coverage with a different first point for each start.
    ids=[int(rng.integers(len(X)))];dist=np.full(len(X),np.inf)
    while len(ids)<n:
        dist=np.minimum(dist,1-directions@directions[ids[-1]])
        dist[ids]=-np.inf;ids.append(int(np.argmax(dist)))
    P=X[ids].copy();P+=rng.normal(size=P.shape)*1e-7
    return P

if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 1
    n=int(sys.argv[2]) if len(sys.argv)>2 else 85
    base=np.load(ROOT/'artifacts/baseline/numerical.npz',allow_pickle=True)['X']
    X=starting_subset(base,n,seed)
    out=ROOT/'artifacts/vertex_search'/f'n{n}_seed{seed}'
    Search(X,out).run(rounds=12,iterations=200)
