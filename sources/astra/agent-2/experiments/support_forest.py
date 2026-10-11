"""Continuous shortest-path equilibrium exclusion loss.
For each centered primal/polar point, edge cost is squared angular guard deficit.
Sum of shortest distances to the farthest root is continuous while that root and
hull stay fixed. Its derivative weights tree edges by descendant count. This
avoids the discontinuous unweighted Dijkstra-tree objective and collapse traps.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_search import SupportSearch,complex_for,ROOT
from geometry import angular_scores

def points(Y,ds,tr,tm):
    X=np.linalg.solve(Y[ds],np.ones((len(ds),3,1))).squeeze(-1)
    a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
    six=np.einsum('ij,ij->i',a,np.cross(b,c))*tm
    cen=np.sum(six[:,None]*(a+b+c),axis=0)/(4*six.sum())
    return X-cen,Y/(1-Y@cen)[:,None]

def paths(P,mask,margin):
    valid=mask>0;r=np.sum(P*P,axis=1)
    score=angular_scores(P);score[:,~valid]=-1e6
    root=int(np.argmax(np.where(valid,r,-np.inf)))
    costs=np.maximum(margin-score,0)**2+1e-14
    distance=np.full(len(P),np.inf);distance[root]=0;parent=np.full(len(P),root);seen=~valid;order=[]
    for _ in range(int(valid.sum())):
        j=int(np.argmin(np.where(seen,np.inf,distance)));seen[j]=True;order.append(j)
        proposal=distance[j]+costs[:,j];take=(proposal<distance)&~seen
        parent[take]=j;distance[take]=proposal[take]
    weights=valid.astype(float)
    for i in order[::-1]:
        if i!=root:weights[parent[i]]+=weights[i]
    weights[root]=0;weights/=valid.sum()
    parent[~valid]=root
    return parent,weights,score.max(axis=1),root,float(np.sum(distance[valid])/valid.sum())

@jax.jit
def forestcore(Y,ds,tr,tm,pu,wu,ps,ws,margin):
    def f(H):
        X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
        six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
        cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six))
        Z=X-cent;Q=H/(1-H@cent)[:,None]
        def loss(P,pa,w):
            d=P[pa]-P
            score=jnp.sum(P*d,axis=1)/(jnp.sqrt(jnp.sum(P*P,axis=1))*jnp.sqrt(jnp.sum(d*d,axis=1)+1e-24))
            return jnp.sum(w*jnp.maximum(margin-score,0)**2)
        return loss(Z,pu,wu)+loss(Q,ps,ws),(cent,jnp.sum(six)/6)
    return jax.value_and_grad(f,has_aux=True)(Y)

class ForestSearch(SupportSearch):
    def eval(self,flat):
        Y=flat.reshape(self.Y.shape)
        try:
            ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm)
        except (ValueError,np.linalg.LinAlgError):return 1e4,np.zeros_like(flat)
        pu,wu,u,ru,du=paths(Z,xm,self.margin);ps,ws,s,rs,dsum=paths(Q,ym,self.margin)
        (cost,(cent,vol)),grad=forestcore(Y,ds,tr,tm,pu,wu,ps,ws,self.margin)
        cost=float(cost);grad=np.array(grad)
        if not np.isfinite(cost) or not np.isfinite(grad).all():return 1e4,np.zeros_like(flat)
        self.calls+=1;U=int(np.sum((u<0)&(xm>0)));S=int(np.sum((s<0)&(ym>0)))
        floor=float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]));V=int(xm.sum());F=int(ym.sum());E=V+F-2
        # Root-persistence proxy includes full paths; report costs by landscape.
        info={'S':S,'U':U,'V':V,'E':E,'F':F,'C':2*E,'cost':cost,'floor':floor,'primal_path_loss':du,'polar_path_loss':dsum,'calls':self.calls,'seconds':time.time()-self.started,'volume':float(vol),'centroid':np.array(cent).tolist()}
        if cost<self.bestcost:
            self.bestcost=cost;np.save(self.out/'lowest_loss.npy',Y);(self.out/'lowest_loss.json').write_text(json.dumps(info,indent=2)+'\n')
        key=(S+U,cost)
        if key<self.best:
            self.best=key;self.history.append(info);np.save(self.out/'best.npy',Y);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            if len(self.history)<6 or self.calls%100<5 or S==U==1:print(self.out.name,info,flush=True)
        if S==U==1 and floor>1e-10:
            self.target=True;np.save(self.out/'numerical_target.npy',Y);(self.out/'numerical_target.json').write_text(json.dumps(info,indent=2)+'\n');print('NUMERICAL_TARGET',self.out,flush=True)
        return cost,grad.ravel()

if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 1;rng=np.random.default_rng(seed)
    Y=np.load(ROOT/'artifacts/kf27d/supports.npy')
    if seed>1:Y+=rng.normal(size=Y.shape)*.003*min(seed-1,5)
    obj=ForestSearch(Y,ROOT/'artifacts/support_forest'/f'kf27d_seed{seed}',margin=1e-4)
    obj.run(rounds=30,iters=500,rng=rng)
