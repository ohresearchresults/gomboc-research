"""S1 plus at most two designated U, with free physical support geometry.
The two exempt physical vertices are identified by their supporting-plane triples;
all other active physical vertices must have a strict outward escape. An exempt
vertex may disappear or lose U without violating the constraints.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import jax
from functools import partial
import jax.numpy as jnp
from stable_constrained import StableSearch
from support_persistence import ROOT,complex_for,points,edge_graphs,barcode
from geometry import angular_scores

@partial(jax.jit, static_argnames=["polar"])
def vals_jac(Y,ds,tr,tm,bpu,bwu,xm,ym,exempt,root,tau,ti,tj,polar):
    def f(H):
        X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
        vol=jnp.sum(six)/6;cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(24*vol);Z=X-cent;Q=H/(1-H@cent)[:,None]
        r,a,b=Z[bpu[:,0]],Z[bpu[:,1]],Z[bpu[:,2]];d=b-a;ll=jnp.sum(d*d,axis=1);t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(ll,1e-30),0,1);foot=a+t[:,None]*d
        bars=jnp.maximum(jnp.sum(r*r,axis=1)-jnp.sum(foot*foot,axis=1),0)*bwu
        birth=jnp.sum(r*r,axis=1)
        P=Q if polar else Z
        delta=P[tj]-P[ti]
        loss=-jnp.dot(P[ti],delta)/(jnp.linalg.norm(P[ti])*jnp.linalg.norm(delta))
        def guards(P,mask):
            delta=P[None,:,:]-P[:,None,:]
            score=jnp.sum(P[:,None,:]*delta,axis=2)/(jnp.linalg.norm(P,axis=1)[:,None]*jnp.sqrt(jnp.sum(delta*delta,axis=2)+1e-24))
            score=jnp.where(jnp.eye(len(P),dtype=bool)|(mask==0)[None,:],-1e6,score)
            return jnp.max(score,axis=1)-tau
        u=guards(Z,xm);u=jnp.where((xm==0)|(exempt>0),1.,u)
        s=guards(Q,ym);s=jnp.where(ym==0,1.,s);s=s.at[root].set(1.)
        return jnp.r_[loss,s,u]
    return f(Y),jax.jacrev(f)(Y)

class GuideSearch(StableSearch):
    def __init__(self,Y,out,roots=((12,46,47),(15,31,47)),guide=None,**kwargs):
        super().__init__(Y,out,**kwargs);self.roots={tuple(sorted(r)) for r in roots};self.guide=guide;self.guide_reached=False
    def data(self,x):
        if self.cache is not None and np.array_equal(x,self.cache[0]):return self.cache[1:]
        Y=x.reshape(self.Y.shape);N=len(Y);P=2*N-4
        try:
            ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm);bp,bw,p=barcode(Z,xm,eu)
            exempt=np.array([tuple(sorted(r)) in self.roots for r in ds],float)
            if self.guide['polar']:
                ti,tj=self.guide['i'],self.guide['j']
                if not (ym[ti] and ym[tj]):raise ValueError('Guide facet retired')
            else:
                keys={tuple(sorted(r)):i for i,r in enumerate(ds) if xm[i]}
                ti=keys.get(tuple(self.guide['i']));tj=keys.get(tuple(self.guide['j']))
                if ti is None or tj is None:raise ValueError('Guide vertex retired')
            vals,jac=vals_jac(Y,ds,tr,tm,bp,bw,xm,ym,exempt,self.root,self.tau,ti,tj,self.guide['polar']);vals=np.array(vals);jac=np.array(jac).reshape(len(vals),-1)
        except (ValueError,np.linalg.LinAlgError,AssertionError):
            vals=np.r_[1e4,np.full(N+P,-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        if not np.isfinite(vals).all() or not np.isfinite(jac).all():
            vals=np.r_[1e4,np.full(N+P,-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        self.calls+=1;margin=float(vals[1:].min()+self.tau)
        if margin>1e-12 and vals[0]<self.best:
            u=angular_scores(Z);u[:,xm==0]=-np.inf;ue=u.max(axis=1);s=angular_scores(Q);s[:,ym==0]=-np.inf;se=s.max(axis=1)
            U=int(np.sum((ue<0)&(xm>0)));S=int(np.sum((se<0)&(ym>0)));V=int(xm.sum());F=int(ym.sum());E=V+F-2
            info={'V':V,'E':E,'F':F,'C':2*E,'S':S,'U':U,'loss':float(vals[0]),'min_required_escape':margin,'primal_bars_top':sorted(p.tolist(),reverse=True)[:5],'calls':self.calls,'seconds':time.time()-self.started,'unstable_triples':[ds[i].tolist() for i in np.flatnonzero((ue<0)&(xm>0))]}
            self.guide_reached=float(vals[0]) < -1e-4
            self.best=float(vals[0]);self.history.append(info);np.save(self.out/'best.npy',Y);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            if len(self.history)<5 or len(self.history)%20==0 or U==1:print(self.out.name,info,flush=True)
            if S==U==1:
                self.target=True;np.save(self.out/'numerical_target.npy',Y);(self.out/'numerical_target.json').write_text(json.dumps(info,indent=2)+'\n');print('NUMERICAL_TARGET',self.out,flush=True)
        self.cache=(x.copy(),vals,jac);return vals,jac

