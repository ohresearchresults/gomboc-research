"""Own-centroid persistence minimization for freely moving physical supports.
Zero-dimensional superlevel persistence on genuine primal and polar edge graphs
records complete unstable basins, rather than the small local escape of a vertex.
The desired essential maximum in each landscape is omitted; all finite bars count.
"""
from pathlib import Path
from collections import defaultdict
import sys,json,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_search import SupportSearch,complex_for,ROOT
from support_forest import points
from geometry import angular_scores

def edge_graphs(ds,xm):
    tri=ds[xm>0];pairs=defaultdict(list)
    for i,t in enumerate(tri):
        for a,b in [(t[0],t[1]),(t[1],t[2]),(t[2],t[0])]:pairs[tuple(sorted((int(a),int(b))))].append(i)
    assert all(len(v)==2 for v in pairs.values())
    return np.array(list(pairs.values())),np.array(list(pairs))

def barcode(P,mask,edges):
    a=P[edges[:,0]];d=P[edges[:,1]]-a;ll=np.sum(d*d,axis=1)
    t=np.clip(-np.sum(a*d,axis=1)/ll,0,1)
    deaths=np.sum((a+t[:,None]*d)**2,axis=1);rr=np.sum(P*P,axis=1)
    parent=np.arange(len(P));heir=np.arange(len(P));triples=[];vals=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for k in np.argsort(-deaths):
        i,j=map(int,edges[k]);a,b=find(i),find(j)
        if a==b:continue
        if rr[heir[a]]<rr[heir[b]]:a,b=b,a
        loser=heir[b];parent[b]=a
        triples.append([int(loser),i,j]);vals.append(float(max(rr[loser]-deaths[k],0)))
    assert len(triples)==int(mask.sum())-1
    M=len(P)-1;n=len(triples)
    triples.extend([[0,0,1]]*(M-n));weights=np.r_[np.ones(n),np.zeros(M-n)]
    return np.array(triples),weights,np.array(vals)

@jax.jit
def persist_core(Y,ds,tr,tm,bpu,bwu,bps,bws,xm,ym):
    def f(H):
        X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
        six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
        cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six))
        Z=X-cent;Q=H/(1-H@cent)[:,None]
        def loss(P,pairs,weights,mask,opposite,opposite_mask):
            root,a,b=P[pairs[:,0]],P[pairs[:,1]],P[pairs[:,2]];d=b-a
            ll=jnp.sum(d*d,axis=1);t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(ll,1e-30),0,1)
            foot=a+t[:,None]*d
            bars=jnp.maximum(jnp.sum(root*root,axis=1)-jnp.sum(foot*foot,axis=1),0)*weights
            scale=jnp.max(jnp.where(mask>0,jnp.sum(P*P,axis=1),0))-1/jnp.max(jnp.where(opposite_mask>0,jnp.sum(opposite*opposite,axis=1),0))
            return jnp.sum((bars/jnp.maximum(jnp.sum(root*root,axis=1),1e-30))**2)
        return loss(Z,bpu,bwu,xm,Q,ym)+loss(Q,bps,bws,ym,Z,xm),(cent,jnp.sum(six)/6)
    return jax.value_and_grad(f,has_aux=True)(Y)

class PersistenceSearch(SupportSearch):
    def eval(self,flat):
        Y=flat.reshape(self.Y.shape)
        try:
            ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm)
            bpu,bwu,pv=barcode(Z,xm,eu);bps,bws,qv=barcode(Q,ym,es)
        except (ValueError,np.linalg.LinAlgError,AssertionError):return 1e4,np.zeros_like(flat)
        (cost,(cent,vol)),grad=persist_core(Y,ds,tr,tm,bpu,bwu,bps,bws,xm,ym)
        cost=float(cost);grad=np.array(grad)
        if not np.isfinite(cost) or not np.isfinite(grad).all():return 1e4,np.zeros_like(flat)
        self.calls+=1
        scores=angular_scores(Z);scores[:,xm==0]=-np.inf;u=scores.max(axis=1)
        scores=angular_scores(Q);scores[:,ym==0]=-np.inf;s=scores.max(axis=1)
        U=int(np.sum((u<0)&(xm>0)));S=int(np.sum((s<0)&(ym>0)))
        floor=float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]));V=int(xm.sum());F=int(ym.sum());E=V+F-2
        info={'S':S,'U':U,'V':V,'E':E,'F':F,'C':2*E,'cost':cost,'floor':floor,'primal_bars_top':sorted(pv.tolist(),reverse=True)[:6],'polar_bars_top':sorted(qv.tolist(),reverse=True)[:6],'calls':self.calls,'seconds':time.time()-self.started,'volume':float(vol),'centroid':np.array(cent).tolist()}
        if cost<self.bestcost:
            self.bestcost=cost;np.save(self.out/'lowest_loss.npy',Y);(self.out/'lowest_loss.json').write_text(json.dumps(info,indent=2)+'\n')
            if cost<1e-10:np.save(self.out/f'low_{self.calls}.npy',Y)
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
    if len(sys.argv)>2:Y=np.load(sys.argv[2])
    elif seed>1:Y+=rng.normal(size=Y.shape)*.003*min(seed-1,5)
    obj=PersistenceSearch(Y,ROOT/'artifacts/support_persistence'/f'kf27d_peaknorm_seed{seed}')
    obj.run(rounds=30,iters=600,rng=rng)
