"""S1 with a finite allowed star for U turnover, and concave basin penalty.
The two exempt physical vertices are identified by their supporting-plane triples;
all other active physical vertices must have a strict outward escape. An exempt
vertex may disappear or lose U without violating the constraints.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from stable_constrained import StableSearch
from support_persistence import ROOT,complex_for,points,edge_graphs,barcode
from geometry import angular_scores

@jax.jit
def vals_jac(Y,ds,tr,tm,bpu,bwu,xm,ym,exempt,root,tau):
    def f(H):
        X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
        vol=jnp.sum(six)/6;cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(24*vol);Z=X-cent;Q=H/(1-H@cent)[:,None]
        r,a,b=Z[bpu[:,0]],Z[bpu[:,1]],Z[bpu[:,2]];d=b-a;ll=jnp.sum(d*d,axis=1);t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(ll,1e-30),0,1);foot=a+t[:,None]*d
        bars=jnp.maximum(jnp.sum(r*r,axis=1)-jnp.sum(foot*foot,axis=1),0)*bwu
        birth=jnp.sum(r*r,axis=1)
        loss=jnp.sum(jnp.log1p((bars/jnp.maximum(birth,1e-30))/1e-3))
        def guards(P,mask):
            delta=P[None,:,:]-P[:,None,:]
            score=jnp.sum(P[:,None,:]*delta,axis=2)/(jnp.linalg.norm(P,axis=1)[:,None]*jnp.sqrt(jnp.sum(delta*delta,axis=2)+1e-24))
            score=jnp.where(jnp.eye(len(P),dtype=bool)|(mask==0)[None,:],-1e6,score)
            return jnp.max(score,axis=1)-tau
        u=guards(Z,xm);u=jnp.where((xm==0)|(exempt>0),1.,u)
        s=guards(Q,ym);s=jnp.where(ym==0,1.,s);s=s.at[root].set(1.)
        return jnp.r_[loss,s,u]
    return f(Y),jax.jacrev(f)(Y)

class StarSearch(StableSearch):
    def __init__(self,Y,out,roots=((12,46,47),(15,31,47)),**kwargs):
        super().__init__(Y,out,**kwargs);self.roots={tuple(sorted(r)) for r in roots}
    def data(self,x):
        if self.cache is not None and np.array_equal(x,self.cache[0]):return self.cache[1:]
        Y=x.reshape(self.Y.shape);N=len(Y);P=2*N-4
        try:
            ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm);bp,bw,p=barcode(Z,xm,eu)
            exempt=np.array([tuple(sorted(r)) in self.roots for r in ds],float)
            vals,jac=vals_jac(Y,ds,tr,tm,bp,bw,xm,ym,exempt,self.root,self.tau);vals=np.array(vals);jac=np.array(jac).reshape(len(vals),-1)
        except (ValueError,np.linalg.LinAlgError,AssertionError):
            vals=np.r_[1e4,np.full(N+P,-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        if not np.isfinite(vals).all() or not np.isfinite(jac).all():
            vals=np.r_[1e4,np.full(N+P,-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        self.calls+=1;margin=float(vals[1:].min()+self.tau)
        if margin>1e-9 and vals[0]<self.best:
            u=angular_scores(Z);u[:,xm==0]=-np.inf;ue=u.max(axis=1);s=angular_scores(Q);s[:,ym==0]=-np.inf;se=s.max(axis=1)
            U=int(np.sum((ue<0)&(xm>0)));S=int(np.sum((se<0)&(ym>0)));V=int(xm.sum());F=int(ym.sum());E=V+F-2
            info={'V':V,'E':E,'F':F,'C':2*E,'S':S,'U':U,'loss':float(vals[0]),'min_required_escape':margin,'primal_bars_top':sorted(p.tolist(),reverse=True)[:5],'calls':self.calls,'seconds':time.time()-self.started,'unstable_triples':[ds[i].tolist() for i in np.flatnonzero((ue<0)&(xm>0))]}
            self.best=float(vals[0]);self.history.append(info);np.save(self.out/'best.npy',Y);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            if len(self.history)<5 or len(self.history)%20==0 or U==1:print(self.out.name,info,flush=True)
            if S==U==1:
                self.target=True;np.save(self.out/'numerical_target.npy',Y);(self.out/'numerical_target.json').write_text(json.dumps(info,indent=2)+'\n');print('NUMERICAL_TARGET',self.out,flush=True)
        self.cache=(x.copy(),vals,jac);return vals,jac

if __name__=='__main__':
    tag=sys.argv[1] if len(sys.argv)>1 else 'base';Y=np.load(ROOT/'artifacts/kf27d/supports.npy')
    if len(sys.argv)>2:Y=np.load(sys.argv[2])
    obj=StarSearch(Y,ROOT/'artifacts/rootstar_constrained'/tag,tau=1e-7);obj.run(rounds=20,iters=400)
