"""Numerical free-support research with the actual uniform-volume centroid."""
import os
os.environ.setdefault('JAX_ENABLE_X64','true')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import json,sys,time
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import jax
jax.config.update('jax_enable_x64',True)
import jax.numpy as jnp
from geometry import mass,escape
ROOT=Path(__file__).resolve().parents[1]

def complex_for(Y):
    dual=ConvexHull(Y)
    if np.max(dual.equations[:,3])>=-1e-9:raise ValueError('Unbounded physical halfspace intersection')
    ds=dual.simplices.copy();N=len(Y);P=2*N-4
    active=np.zeros(N);active[dual.vertices]=1
    if len(dual.vertices)<12:raise ValueError('Outside research domain: fewer than12 active facets')
    X=np.linalg.solve(Y[ds],np.ones((len(ds),3,1))).squeeze(-1)
    h=ConvexHull(X);tr=h.simplices.copy()
    a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    tr[flip]=tr[flip][:,[0,2,1]]
    # Integration triangulation is never used as a combinatorial facet count.
    xmask=np.r_[np.ones(len(X)),np.zeros(P-len(X))]
    ds=np.r_[ds,np.tile(ds[0],(P-len(ds),1))]
    M=2*P-4;tmask=np.r_[np.ones(len(tr)),np.zeros(M-len(tr))]
    tr=np.r_[tr,np.tile(tr[0],(M-len(tr),1))]
    return ds,xmask,tr,tmask,active

@jax.jit
def core(Y,ds,xmask,tr,tmask,ymask,margin):
    def f(Q0):
        X=jnp.linalg.solve(Q0[ds],jnp.ones((len(ds),3,1))).squeeze(-1)
        a,b,c=X[tr[:,0]],X[tr[:,1]],X[tr[:,2]]
        six=jnp.sum(a*jnp.cross(b,c),axis=1)*tmask
        cent=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six))
        Z=X-cent;Q=Q0/(1-Q0@cent)[:,None]
        def scor(V,mask):
            delta=V[None,:,:]-V[:,None,:]
            dot=jnp.sum(V[:,None,:]*delta,axis=2)
            dist=jnp.sqrt(jnp.sum(delta*delta,axis=2)+1e-24)
            score=dot/(dist*jnp.linalg.norm(V,axis=1)[:,None])
            score=jnp.where(jnp.eye(len(V),dtype=bool)|(~mask.astype(bool))[None,:],-1e6,score)
            best=jnp.max(score,axis=1)
            neg=jnp.maximum(margin-best,0)*mask
            # Omit exactly one root, chosen to minimize this hinge objective.
            root=jnp.argmax(neg);neg=neg.at[root].set(0)
            return jnp.sum(neg**2),best
        ul,u=scor(Z,xmask);sl,s=scor(Q,ymask)
        return ul+sl,(u,s,cent,jnp.sum(six)/6)
    return jax.value_and_grad(f,has_aux=True)(Y)

class SupportSearch:
    def __init__(self,Y,out,margin=1e-5):
        self.Y=Y;self.out=out;out.mkdir(parents=True,exist_ok=True);self.margin=margin
        self.calls=0;self.started=time.time();self.best=(np.inf,np.inf);self.bestcost=np.inf;self.target=False;self.history=[]
    def eval(self,flat):
        Y=flat.reshape(self.Y.shape)
        try:ds,xm,tr,tm,ym=complex_for(Y)
        except (QhullError,ValueError,np.linalg.LinAlgError):
            # Reject unbounded or undefined physical bodies; no substitute geometry.
            return 1e4,np.zeros_like(flat)
        (cost,(u,s,c,vol)),grad=core(Y,ds,xm,tr,tm,ym,self.margin)
        cost=float(cost);u=np.array(u);s=np.array(s);grad=np.array(grad)
        if not np.isfinite(cost) or not np.isfinite(grad).all():return 1e4,np.zeros_like(flat)
        self.calls+=1;U=int(np.sum((u<0)&(xm>0)));S=int(np.sum((s<0)&(ym>0)))
        floor=float(min(np.sort(u[xm>0])[1],np.sort(s[ym>0])[1]))
        V=int(xm.sum());F=int(ym.sum());E=V+F-2;key=(S+U,cost)
        info={'S':S,'U':U,'V':V,'E':E,'F':F,'C':2*E,'cost':cost,'floor':floor,'calls':self.calls,'seconds':time.time()-self.started,'volume':float(vol),'centroid':np.array(c).tolist()}
        if cost<self.bestcost:
            self.bestcost=cost;np.save(self.out/'lowest_loss.npy',Y);(self.out/'lowest_loss.json').write_text(json.dumps(info,indent=2)+'\n')
        if key<self.best:
            self.best=key;self.history.append(info);np.save(self.out/'best.npy',Y)
            (self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n')
            print(self.out.name,info,flush=True)
        if S==U==1 and floor>1e-10:
            self.target=True;np.save(self.out/'numerical_target.npy',Y);(self.out/'numerical_target.json').write_text(json.dumps(info,indent=2)+'\n');print('NUMERICAL_TARGET',self.out,flush=True)
        return cost,grad.ravel()
    def run(self,rounds=12,iters=250,rng=None):
        if rng is None:rng=np.random.default_rng(123)
        Y=self.Y.copy()
        for k in range(rounds):
            # A coordinate box keeps each inner search local while allowing every normal and offset to move.
            span=.2*np.mean(np.linalg.norm(Y,axis=1))
            bounds=list(zip((Y-span).ravel(),(Y+span).ravel()))
            opt=minimize(self.eval,Y.ravel(),jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':iters,'maxls':40,'ftol':1e-15,'gtol':1e-11,'maxcor':30})
            Y=opt.x.reshape(Y.shape);np.save(self.out/f'round{k}.npy',Y)
            print(self.out.name,'ROUND',k,'loss',opt.fun,'nit',opt.nit,'msg',opt.message,'best',self.best,flush=True)
            if self.target:return
            if opt.nit<5:
                Y=Y+rng.normal(size=Y.shape)*(.0005 if k%2==0 else .003)
        self.Y=Y

if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 1
    Y=np.load(ROOT/'artifacts/kf27d/supports.npy');rng=np.random.default_rng(seed)
    if seed>1:Y+=rng.normal(size=Y.shape)*.0001*10**(seed%3)
    ss=SupportSearch(Y,ROOT/'artifacts/support_search'/f'kf27d_seed{seed}')
    ss.run(rounds=20,iters=400,rng=rng)
