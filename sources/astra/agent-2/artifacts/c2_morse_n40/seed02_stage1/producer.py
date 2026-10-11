"""A new C2-symmetric physical family, independent of inherited Figure seeds.

A diamond base and axial apex are joined by antipodal pairs on a twisted
ladder. C2 rotation about the x axis makes both transverse first moments
EXACTLY zero for uniform mass. The remaining centroid coordinate is integrated
over the actual convex hull at every evaluation. The base is always a genuine
stable facet and the apex a genuine unstable vertex; all extra roots count.

No triangulation is counted as facets: the two base fan triangles form one
maximal coplanar facet. All remaining coplanar coincidences are rejected for
discovery, and any purported goal needs the independent exact point-hull audit.
"""
import sys,json,time
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
import jax
import jax.numpy as jnp
from support_persistence import ROOT,barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

@jax.jit
def coordinates(q):
    xb=-jnp.exp(q[0]);b=jnp.exp(q[1]);c=jnp.exp(q[2]);p=q[3:].reshape(-1,3)
    xx=xb+(1-xb)*jax.nn.sigmoid(p[:,0]);half=jnp.c_[xx,p[:,1:]]
    base=jnp.array([[1.,0.,0.],[xb,b,0.],[xb,-b,0.],[xb,0.,c],[xb,0.,-c]])
    return jnp.concatenate([base,half,half*jnp.array([1.,-1.,-1.])],axis=0)

@jax.jit
def physical(q,T,R):
    X=coordinates(q);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1)
    raw=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six))
    # These two zeroes are an exact physical symmetry theorem, not a guessed
    # centroid. raw is also returned and independently checked numerically.
    center=jnp.array([raw[0],0.,0.]);Z=X-center;Y=jnp.linalg.solve(Z[R],jnp.ones((len(R),3,1))).squeeze(-1)
    return X,Z,Y,center,six.sum()/6,raw

@jax.jit
def core(q,T,R,bp,bw,bq,qw,tau):
    def fun(q):
        X,Z,Y,center,volume,raw=physical(q,T,R)
        def bars(A,p,w):
            root,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];delta=b-a;t=jnp.clip(-jnp.sum(a*delta,1)/jnp.maximum(jnp.sum(delta*delta,1),1e-40),0,1);birth=jnp.sum(root*root,1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*delta)**2,1),0)*w/jnp.maximum(birth,1e-40)
            return jnp.where(tau<0,jnp.sum(depth*depth),jnp.log1p(depth/jnp.maximum(tau,1e-12)).sum())
        return bars(Z,bp,bw)+bars(Y,bq,qw)
    return jax.value_and_grad(fun)(q)

def state(q):
    X=np.asarray(coordinates(q));h=ConvexHull(X);T=h.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
    base=np.all((T>=1)&(T<=4),axis=1)
    if base.sum()!=2:raise ValueError('diamond base did not give exactly two fan triangles')
    representatives=np.r_[T[np.flatnonzero(base)[:1]],T[~base]];labels=np.empty(len(T),int);labels[base]=0;labels[~base]=np.arange(1,1+(~base).sum())
    edgefaces=defaultdict(list)
    for k,t in enumerate(T):
        for i,j in zip(t,np.roll(t,-1)):edgefaces[tuple(sorted((int(i),int(j))))].append(labels[k])
    if not all(len(v)==2 for v in edgefaces.values()):raise ValueError('nonmanifold numerical hull')
    eu=np.array([e for e,ff in edgefaces.items() if ff[0]!=ff[1]],int);es=np.array([ff for ff in edgefaces.values() if ff[0]!=ff[1]],int)
    if len(eu)<17:raise ValueError('outside the requested lower complexity domain')
    XX,Z,Y,g,vol,raw=map(np.asarray,physical(q,T,representatives))
    if abs(raw[1:]).max()>1e-10 or vol<=0 or not np.isfinite(Y).all():raise ValueError('symmetry or volume check failed')
    distance=np.linalg.norm(Y[:,None]-Y[None,:],axis=2);np.fill_diagonal(distance,np.inf)
    if distance.min()<1e-10:raise ValueError('additional near-coplanar facet event needs a new explicit hull audit')
    if len(h.vertices)-len(eu)+len(Y)!=2:raise ValueError('true base-facet Euler identity fails')
    mask=np.zeros(len(X));mask[h.vertices]=1;bp,bw,P=barcode(Z,mask,eu);bq,qw,Q=barcode(Y,np.ones(len(Y)),es);P/=np.sum(Z[bp[bw>0,0]]**2,axis=1);Q/=np.sum(Y[bq[:,0]]**2,axis=1)
    us=angular_scores(Z[h.vertices]).max(1);ss=angular_scores(Y).max(1)
    return dict(X=X,Z=Z,Y=Y,T=T,R=representatives,bp=bp,bw=bw,bq=bq,qw=qw,vertices=h.vertices,eu=eu,es=es,V=len(h.vertices),E=len(eu),F=len(Y),S=int((ss<0).sum()),U=int((us<0).sum()),Pmax=float(P.max()),Qmax=float(Q.max()),P=P,Q=Q,loss=float(P@P+Q@Q),centroid=g.tolist(),volume=float(vol),minimum_nonroot=float(min(np.sort(us)[1],np.sort(ss)[1])))

class NumericalGoal(Exception):pass
class Search:
    def __init__(self,out,n,tau):
        self.out=out;out.mkdir(parents=True,exist_ok=False);self.n=n;self.tau=tau;self.calls=0;self.invalid=0;self.best=np.inf;self.fewest=(999,np.inf);self.start=time.time();self.hist=[]
        (out/'producer.py').write_bytes(Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(pairs=n,maximum_input_points=2*n+5,tau=tau,symmetry='(x,y,z)->(x,-y,-z)',scope='actual homogeneous hull; two base fan triangles count as one facet; all results numerical until exact audit'),indent=2)+'\n')
    def eval(self,q):
        try:s=state(q);value,grad=core(q,s['T'],s['R'],s['bp'],s['bw'],s['bq'],s['qw'],self.tau);value=float(value);grad=np.asarray(grad)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):self.invalid+=1;return 1e4,np.zeros_like(q)
        if not np.isfinite(value) or not np.isfinite(grad).all():self.invalid+=1;return 1e4,np.zeros_like(q)
        self.calls+=1;row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','loss','centroid','volume','minimum_nonroot']};row.update(calls=self.calls,invalid=self.invalid,objective=value,tau=self.tau,seconds=time.time()-self.start)
        if value<self.best:self.best=value;np.save(self.out/'best_q.npy',q);np.save(self.out/'best_points.npy',s['X']);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
        key=(s['S']+s['U'],s['loss'])
        if key<self.fewest:
            self.fewest=key;self.hist.append(row);np.save(self.out/'fewest_q.npy',q);np.save(self.out/'fewest_points.npy',s['X']);(self.out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('C2_LADDER_FEWEST',row,flush=True)
        if s['S']==s['U']==1 and 17<=s['E']<=248:
            np.save(self.out/'NUMERICAL_NOMINATION_q.npy',q);np.save(self.out/'NUMERICAL_NOMINATION_points.npy',s['X']);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');raise NumericalGoal()
        if self.calls%300==0:print('C2_LADDER_CALLS',self.calls,'best',self.best,'fewest',self.fewest,flush=True)
        return value,grad

def initial(n,seed):
    rng=np.random.default_rng(43028+seed);xb=-rng.uniform(.5,1.3);b=rng.uniform(.15,.65);c=b*rng.uniform(.7,1.4);x=np.linspace(xb+.06*(1-xb),.93,n);t=(x-xb)/(1-xb);u=2*t-1;omega=[np.pi,2*np.pi,3*np.pi,5*np.pi][seed%4];phase=omega*t+.1*np.sin(3*np.pi*t);radius=rng.uniform(.5,1.)*np.sqrt(1-u*u)*(1+rng.uniform(-.4,.4)*u);half=np.c_[np.log(t/(1-t)),radius*np.cos(phase),radius*np.sin(phase)];return np.r_[np.log(-xb),np.log(b),np.log(c),half.ravel()]

def run(out,n=38,seeds=8):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    bounds=[(-4,1),(-4,1),(-4,1)]+[x for _ in range(n) for x in [(-8,8),(-3,3),(-3,3)]]
    for seed in range(seeds):
        q=initial(n,seed)
        for stage,tau in enumerate([-1.,.03,.003,.0003]):
            s=Search(out/f'seed{seed:02d}_stage{stage}',n,tau)
            try:opt=minimize(s.eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=600,maxls=35,maxcor=15,ftol=1e-13,gtol=1e-10))
            except NumericalGoal:
                (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(folder=str(s.out)),indent=2)+'\n');print('C2_NUMERICAL_GOAL_REQUIRES_EXACT',str(s.out),flush=True);return
            q=np.load(s.out/'best_q.npy');(s.out/'history.json').write_text(json.dumps(s.hist,indent=2)+'\n');print('C2_LADDER_STAGE_DONE',seed,stage,s.fewest,opt.message,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(seeds=seeds,pairs=n,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 38,int(sys.argv[3]) if len(sys.argv)>3 else 8)
