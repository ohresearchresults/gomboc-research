"""Full physical support motion, preserving one stable root by exact-form guards.
Numerical SLSQP nominations; strict exact certification is separate.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_persistence import ROOT,complex_for,points,edge_graphs,barcode
from geometry import angular_scores

@jax.jit
def values_jac(Y,ds,tr,tm,bpu,bwu,xm,ym,root,tau):
    def allvals(H):
        X=jnp.linalg.solve(H[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)*tm
        cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six));Z=X-cent;Q=H/(1-H@cent)[:,None]
        r,a,b=Z[bpu[:,0]],Z[bpu[:,1]],Z[bpu[:,2]];d=b-a;ll=jnp.sum(d*d,axis=1)
        t=jnp.clip(-jnp.sum(a*d,axis=1)/jnp.maximum(ll,1e-30),0,1);foot=a+t[:,None]*d
        bars=jnp.maximum(jnp.sum(r*r,axis=1)-jnp.sum(foot*foot,axis=1),0)*bwu
        scale=jnp.max(jnp.sum(Z*Z,axis=1))-1/jnp.max(jnp.sum(Q*Q,axis=1));loss=jnp.sum(bars*bars)/(scale*scale)
        delta=Q[None,:,:]-Q[:,None,:];score=jnp.sum(Q[:,None,:]*delta,axis=2)/(jnp.linalg.norm(Q,axis=1)[:,None]*jnp.sqrt(jnp.sum(delta*delta,axis=2)+1e-24))
        score=jnp.where(jnp.eye(len(Q),dtype=bool),-1e6,score)
        best=jnp.max(score,axis=1)-tau;best=best.at[root].set(1.)
        return jnp.r_[loss,best]
    return allvals(Y),jax.jacrev(allvals)(Y)

class StableSearch:
    def __init__(self,Y,out,root=15,tau=1e-6):
        self.Y=Y;self.out=out;out.mkdir(parents=True,exist_ok=True);self.root=root;self.tau=tau;self.calls=0;self.best=np.inf;self.history=[];self.cache=None;self.target=False;self.started=time.time()
    def data(self,x):
        if self.cache is not None and np.array_equal(x,self.cache[0]):return self.cache[1:]
        Y=x.reshape(self.Y.shape)
        try:
            ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm);bp,bw,p=barcode(Z,xm,eu)
            vals,jac=values_jac(Y,ds,tr,tm,bp,bw,xm,ym,self.root,self.tau);vals=np.array(vals);jac=np.array(jac).reshape(len(vals),-1)
        except (ValueError,np.linalg.LinAlgError,AssertionError):
            vals=np.r_[1e4,np.full(len(Y),-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        if not np.isfinite(vals).all() or not np.isfinite(jac).all():
            vals=np.r_[1e4,np.full(len(Y),-1.)];jac=np.zeros((len(vals),len(x)));self.cache=(x.copy(),vals,jac);return vals,jac
        self.calls+=1
        margin=float(vals[1:].min()+self.tau)
        if margin>1e-9 and vals[0]<self.best:
            u=angular_scores(Z);u[:,xm==0]=-np.inf;ue=u.max(axis=1);s=angular_scores(Q);s[:,ym==0]=-np.inf;se=s.max(axis=1)
            U=int(np.sum((ue<0)&(xm>0)));S=int(np.sum((se<0)&(ym>0)));V=int(xm.sum());F=int(ym.sum());E=V+F-2
            info={'V':V,'E':E,'F':F,'C':2*E,'S':S,'U':U,'loss':float(vals[0]),'polar_min_escape':margin,'primal_bars_top':sorted(p.tolist(),reverse=True)[:5],'calls':self.calls,'seconds':time.time()-self.started}
            self.best=float(vals[0]);self.history.append(info);np.save(self.out/'best.npy',Y);(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            if len(self.history)<5 or len(self.history)%20==0 or U==1:print(self.out.name,info,flush=True)
            if S==U==1:
                self.target=True;np.save(self.out/'numerical_target.npy',Y);(self.out/'numerical_target.json').write_text(json.dumps(info,indent=2)+'\n');print('NUMERICAL_TARGET',self.out,flush=True)
        self.cache=(x.copy(),vals,jac);return vals,jac
    def fun(self,x):v,j=self.data(x);return v[0],j[0]
    def con(self,x):return self.data(x)[0][1:]
    def cj(self,x):return self.data(x)[1][1:]
    def run(self,rounds=15,iters=300):
        Y=self.Y.copy();last_best=np.inf
        for k in range(rounds):
            span=.08*np.mean(np.linalg.norm(Y,axis=1));bounds=list(zip((Y-span).ravel(),(Y+span).ravel()))
            opt=minimize(self.fun,Y.ravel(),jac=True,method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':self.con,'jac':self.cj}],options={'maxiter':iters,'ftol':1e-13,'disp':False})
            vals,jac=self.data(opt.x);np.save(self.out/f'round{k}.npy',opt.x.reshape(Y.shape))
            print(self.out.name,'ROUND',k,'loss',opt.fun,'constraint',vals[1:].min(),'nit',opt.nit,'msg',opt.message,'best',self.best,flush=True)
            if self.target:return
            if np.isfinite(last_best) and self.best>=last_best*(1-1e-9):
                print(self.out.name,'STAGNATION: ending this local chart',flush=True);break
            last_best=self.best
            if (self.out/'best.npy').exists():Y=np.load(self.out/'best.npy')
            else:Y=opt.x.reshape(Y.shape)
        self.Y=Y

if __name__=='__main__':
    tag=sys.argv[1] if len(sys.argv)>1 else 'base';Y=np.load(ROOT/'artifacts/kf27d/supports.npy')
    if len(sys.argv)>2:Y=np.load(sys.argv[2])
    obj=StableSearch(Y,ROOT/'artifacts/stable_constrained'/tag);obj.run(rounds=20,iters=350)
