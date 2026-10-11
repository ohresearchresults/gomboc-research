"""C2-symmetric SUPPORT family with its own primal homogeneous mass.

The 85 input vectors are points of one polar hull. Their true face cycles define
the actual primal intersections and maximal facets. The primal and polar are
never varied independently. The diamond polar facet guarantees E<=248 while
allowing up to165 genuine primal vertices. Centroid symmetry is exact in y,z.
"""
import sys,json,time
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from c2_twisted_ladder import coordinates,state as polar_structure,NumericalGoal
from c2_twisted_morse import initial
from support_persistence import ROOT,barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

@jax.jit
def physical(q,R,T,active):
    H=coordinates(q);X=jnp.linalg.solve(H[R],jnp.ones((len(R),3,1))).squeeze(-1);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),axis=1);raw=jnp.sum(six[:,None]*(a+b+c),axis=0)/(4*jnp.sum(six));g=jnp.array([raw[0],0.,0.]);Z=X-g;Y=H[active]/(1-H[active]@g)[:,None]
    return X,Z,Y,g,six.sum()/6,raw

@jax.jit
def core(q,R,T,active,bp,bw,bq,qw,tau):
    def fun(q):
        X,Z,Y,g,v,raw=physical(q,R,T,active)
        def bars(A,p,w):
            rr,a,b=A[p[:,0]],A[p[:,1]],A[p[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,1)/jnp.maximum(jnp.sum(d*d,1),1e-40),0,1);birth=jnp.sum(rr*rr,1);depth=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,1),0)*w/jnp.maximum(birth,1e-40)
            return jnp.where(tau<0,jnp.sum(depth*depth),jnp.log1p(depth/jnp.maximum(tau,1e-12)).sum())
        return bars(Z,bp,bw)+bars(Y,bq,qw)
    return jax.value_and_grad(fun)(q)

def state(q):
    old=polar_structure(q);H=old['X'];R=old['R'];X=np.linalg.solve(H[R],np.ones((len(R),3,1))).squeeze(-1);active=old['vertices'];faces=[]
    for owner in active:
        links=defaultdict(list)
        for edge,dual in zip(old['eu'],old['es']):
            if owner not in edge:continue
            a,b=map(int,dual);links[a].append(b);links[b].append(a)
        if not links or not all(len(v)==2 for v in links.values()):raise ValueError('dual facet adjacency fails')
        first=min(links);cy=[first];previous=None;now=first
        while True:
            nxt=next(x for x in links[now] if x!=previous)
            if nxt==first:break
            if nxt in cy:raise ValueError('dual facet is not a single cycle')
            cy.append(nxt);previous,now=now,nxt
        if len(cy)!=len(links):raise ValueError('dual facet cycle incomplete')
        if np.cross(X[cy[1]]-X[cy[0]],X[cy[2]]-X[cy[0]])@H[owner]<0:cy=cy[::-1]
        faces.append(cy)
    T=np.array([[f[0],f[k],f[k+1]] for f in faces for k in range(1,len(f)-1)],int);XX,Z,Y,g,vol,raw=map(np.asarray,physical(q,R,T,active))
    if vol<=0 or abs(raw[1:]).max()>1e-10 or not np.isfinite(Y).all():raise ValueError('dual body symmetry/mass failure')
    eu=old['es'];remap={int(v):i for i,v in enumerate(active)};es=np.array([[remap[int(a)],remap[int(b)]] for a,b in old['eu']]);bp,bw,P=barcode(Z,np.ones(len(Z)),eu);bq,qw,Q=barcode(Y,np.ones(len(Y)),es);P/=np.sum(Z[bp[:,0]]**2,1);Q/=np.sum(Y[bq[:,0]]**2,1)
    if len(Z)-len(eu)+len(Y)!=2:raise ValueError('primal Euler failure')
    us=angular_scores(Z).max(1);ss=angular_scores(Y).max(1)
    return dict(X=XX,H=H,Z=Z,Y=Y,R=R,T=T,active=active,bp=bp,bw=bw,bq=bq,qw=qw,V=len(Z),E=len(eu),F=len(Y),S=int((ss<0).sum()),U=int((us<0).sum()),Pmax=float(P.max()),Qmax=float(Q.max()),P=P,Q=Q,loss=float(P@P+Q@Q),centroid=g.tolist(),volume=float(vol),minimum_nonroot=float(min(np.sort(us)[1],np.sort(ss)[1])))

class Search:
    def __init__(self,out,tau):
        self.out=out;out.mkdir(parents=True,exist_ok=False);self.tau=tau;self.calls=0;self.invalid=0;self.best=np.inf;self.fewest=(999,np.inf);self.start=time.time();self.history=[]
        for f in ['c2_dual_morse.py','c2_twisted_morse.py','c2_twisted_ladder.py']:(out/f).write_bytes(Path(__file__).with_name(f).read_bytes())
    def eval(self,q):
        try:s=state(q);value,grad=core(q,s['R'],s['T'],s['active'],s['bp'],s['bw'],s['bq'],s['qw'],self.tau);value=float(value);grad=np.asarray(grad)
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):self.invalid+=1;return 1e4,np.zeros_like(q)
        if not np.isfinite(value) or not np.isfinite(grad).all():self.invalid+=1;return 1e4,np.zeros_like(q)
        self.calls+=1;row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','loss','centroid','volume','minimum_nonroot']};row.update(calls=self.calls,invalid=self.invalid,objective=value,tau=self.tau,seconds=time.time()-self.start)
        if value<self.best:self.best=value;np.save(self.out/'best_q.npy',q);np.save(self.out/'best_supports.npy',s['H']);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
        key=(s['S']+s['U'],s['loss'])
        if key<self.fewest:
            self.fewest=key;self.history.append(row);np.save(self.out/'fewest_q.npy',q);np.save(self.out/'fewest_supports.npy',s['H']);(self.out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('C2_DUAL_FEWEST',row,flush=True)
        if s['S']==s['U']==1 and 17<=s['E']<=248:
            np.save(self.out/'NUMERICAL_NOMINATION_q.npy',q);np.save(self.out/'NUMERICAL_NOMINATION_supports.npy',s['H']);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');raise NumericalGoal()
        if self.calls%300==0:print('C2_DUAL_CALLS',self.calls,'best',self.best,'fewest',self.fewest,flush=True)
        return value,grad

def run(out,n=40,seeds=12):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);bounds=[(-4,1),(-4,1),(-4,1)]+[b for _ in range(n) for b in [(-8,8),(-3,3),(-3,3)]]
    for seed in range(seeds):
        q,definition=initial(n,seed);(out/f'seed{seed:02d}_motivation.json').write_text(json.dumps(definition,indent=2)+'\n')
        for stage,tau in enumerate([-1.,.03,.003,.0003]):
            s=Search(out/f'seed{seed:02d}_stage{stage}',tau)
            try:opt=minimize(s.eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=700,maxls=40,maxcor=15,ftol=1e-13,gtol=1e-10))
            except NumericalGoal:(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(folder=str(s.out)),indent=2)+'\n');print('C2_DUAL_NUMERICAL_GOAL_REQUIRES_EXACT',str(s.out),flush=True);return
            q=np.load(s.out/'best_q.npy');(s.out/'history.json').write_text(json.dumps(s.history,indent=2)+'\n');print('C2_DUAL_STAGE_DONE',seed,stage,s.fewest,opt.message,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(seeds=seeds,pairs=n,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 40,int(sys.argv[3]) if len(sys.argv)>3 else 12)
