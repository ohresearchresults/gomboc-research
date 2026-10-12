# material-7b9227b2e70f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# LOW121 affine metric finite screens: no construction and NO global exclusion

This coordinator-owned direction is separate from nonlinear cap/basin work. Affine maps preserve the true own-centroid relation exactly, and preserve the44/66/24 face lattice. Physical escape is x_i^T G(x_j-x_i)>0 on at least one true incident edge, G positive definite; dual polar escape uses G^{-1}. The numerical search did not produce an own110 body. It does not prove that LOW121 has no such affine image.

## Exact inputs, commands and software

Required exact source pair: [internal-source-reference] (BH81_FINITE_PRIMARY.md,18447bytes,SHA c97bda903918b05112ff8d03e8b030d02df4620b7c7c75ed7703ac0b097f37fa) and [internal-source-reference] (mandatory RECOVER_PRIMARY syntax patch,3147bytes,SHA0054a22972a02a4a8dc57326b62f047150a4826789a5f387311ae894e166e8f4). Follow that launcher to produce LOW121_EXACT.json,29855bytes,SHAd77653ab141e4978e434ae7ba1c58041a8e8277a80537eb99720754b796a2396. This is literal LOW121, not G7/G8 rounded companions. All five primary hashes matched cold replay in this turn.

Python3.13.5,numpy2.3.5,scipy1.17.0. Complete sources below:
- affine_low121.py4473bytes,SHAd387be0834679e7bc85120b98ee956045d7d267e47b9a3156612dc2cb4124181.
- affine_milp.py3439bytes,SHAcebe332755c7f1b0b6436a6ac03db9cec9bb687867a93ec6962796ec6916fe96.

Commands actually executed:
`python affine_low121.py --runs 4 --maxiter 1200`
`python affine_low121.py --runs 3 --maxiter 1200 --mode U --seed 290929`
`python affine_milp.py`

The first command uses seed190929 and successive seeds; the second starts290929. Both use determinant-one lower-triangular maps with parameter bounds[(-3,3),(-6,6),(-3,3),(-6,6),(-6,6)], population16, DE1200 generations, then bounded Nelder-Mead5000 evaluations. Expected reporting marker AFFINE_SCREEN once per completed run, no exact-acceptance marker. The report's `objective` and the carried `best` are JOINT scores even in U-only mode; the per-run optimizer is U-only in that mode. Thus U-only restarts are not seven independent global optimizations, and small displayed loss is not an exclusion or a certificate.

An earlier exploratory version omitted Nelder-Mead bounds and failed when an out-of-box polished point was reused as DE x0; it is superseded by the complete bounded source below. Its unbounded3/3 scout is not promoted as a construction.

## Numerical observations and literal diagnostic checkpoints

At identity LOW121 has S1/U2; its second physical escape cosine is about-0.0152623082 and second polar escape cosine about+2.10643e-5. Four joint bounded runs all ended S3/U3, stable roots6,21,22 and unstable8,9,23. Best joint score1.0232212727458365e-6, matrix condition265.9242800486683. Complete five-parameter checkpoint:
`[-0.12345172828072294,-6.0,1.02555234916837,0.18089044480808247,-5.839694173649771]`.
Three U-only runs all ended S2/U3, not U1. The last checkpoint is
`[0.01649452819361847,0.2586970631628579,2.1643957286835604,-1.6490696987577582,4.410326556494724]`, with second U cosine about-5.0854827487e-8, Sroots9,23,Uroots8,9,23,condition180.1486502832. These floating checkpoints are enough to re-evaluate the highlighted scout endpoints through Affine.report; neither was rationalized/promoted as an exact body.

The MILP uses a trace-one symmetric G, vertex-edge activation disjunctions allowing one root, and a finite OUTER approximation of the PSD cone from coordinate/edge/random directions. Six60-second rounds added negative-eigenvector cuts. All six timed out with large unresolved objective bounds. The apparent positive-margin U1 incumbents in rounds0 and1 are NOT positive definite:

Round0:
G=[[1.1508808154304637e-5,-7.809741817168205e-6,-0.0034043699406482264],[-7.809741817168205e-6,5.259064309298494e-6,0.0022922587906569415],[-0.0034043699406482264,0.0022922587906569415,0.9999832321275365]].
Delta2.722443355712527e-9, apparent root8, eigenvalues[-8.152646656140524e-8,4.932252132401335e-9,1.0000000765942147], minimization dual bound-0.051290324845164416.

Round1:
G=[[0.19615833914214836,-0.29296080429448845,-0.26805637402113114],[-0.29296080429448845,0.43753442778282353,0.40033989149626814],[-0.26805637402113114,0.40033989149626814,0.3663072330750281]].
Delta1.2056869391763314e-10, apparent root33, eigenvalues[-1.0487197266435391e-8,1.0576297069610349e-12,1.0000000104861395], dual bound-0.08775274288792395.

Both use the literal preconditioning B=[[-4.802308662314878,-2.846991294686971,-0.00518404862893446],[2.4141599674328624,-3.260229667555546,-0.15280975284570567],[-1.972488543165538,2.9411653761245025,-0.17440496042868436]]. Remaining rounds had zero/negligible margin and indefinite or numerically rank-one matrices. Last dual bound-0.05244182420223217 still leaves a positive possible maximum margin in the relaxation. No infeasibility proof, exact affine obstruction, or genuine U1 metric resulted. Time-limited MILP trajectories need not be bitwise reproducible across machines; the source, exact geometry input, options, and the two important false-positive checkpoints are preserved here.

The mathematical reusable opening is the positive-edge witness formulation, not the current numerical nonwinner. A useful successor could strengthen PSD control or use exact conditional-root/sign-cell reasoning; do not merely rerun these same bounded settings and call their failure global. No active worker was diverted to generic verification.

## Complete affine_low121.py

```python
"""Reproducible numerical affine/SPD screening, never an exact acceptance test.
Input LOW121_EXACT.json is reproduced by the two BH81 primary materials.
A triangular linear map preserves the exact own-centroid relation.  Equilibrium
predicates are evaluated on vertices and their exact-complex polar neighbours.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,sys,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import differential_evolution,minimize
sys.set_int_max_str_digits(0)

def prepare(name):
 j=json.loads(Path(name+'_EXACT.json').read_text())
 p=[list(map(F,x)) for x in j['points']];c=list(map(F,j['centroid']))
 x=[[p[i][k]-c[k] for k in range(3)] for i in range(len(p))]
 def sub(a,b):return [a[k]-b[k] for k in range(3)]
 def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
 def dot(a,b):return sum(u*v for u,v in zip(a,b))
 f=j['faces']; edges={};y=[]
 for k,row in enumerate(f):
  n=cross(sub(x[row[1]],x[row[0]]),sub(x[row[2]],x[row[0]]));d=dot(n,x[row[0]])
  y.append([u/d for u in n])
  for i,t in zip(row,row[1:]+row[:1]):edges.setdefault(tuple(sorted((i,t))),[]).append(k)
 vn=[set() for _ in x];fn=[set() for _ in f]
 for (i,k),(a,b) in edges.items():vn[i].add(k);vn[k].add(i);fn[a].add(b);fn[b].add(a)
 def pack(x,nn):
  a=np.array(x,dtype=float);a/=np.max(np.linalg.norm(a,axis=1))
  nbr=np.array([sorted(row)+[i]*(max(map(len,nn))-len(row)) for i,row in enumerate(nn)])
  good=np.array([[True]*len(row)+[False]*(nbr.shape[1]-len(row)) for row in nn])
  return a,a[nbr]-a[:,None,:],good
 return pack(x,vn),pack(y,fn),j

class Affine:
 def __init__(self,name):self.v,self.f,self.j=prepare(name)
 def matrices(self,t):
  t=np.atleast_2d(t);a,b,c,d,e=t.T
  z=np.zeros((len(t),3,3));z[:,0,0]=np.exp(a);z[:,1,0]=b;z[:,1,1]=np.exp(c)
  z[:,2,0]=d;z[:,2,1]=e;z[:,2,2]=np.exp(-a-c)
  return z
 def margins(self,t):
  L=self.matrices(t);R=np.linalg.inv(L).transpose(0,2,1)
  def one(pack,M):
   p,e,good=pack
   pp=np.einsum('vi,kij->kvj',p,M);ee=np.einsum('vni,kij->kvnj',e,M)
   num=np.einsum('kvj,kvnj->kvn',pp,ee)
   den=np.linalg.norm(pp,axis=-1)[:,:,None]*np.linalg.norm(ee,axis=-1)
   q=num/np.maximum(den,1e-300);q=np.where(good[None],q,-1e6)
   return np.max(q,axis=-1)
  return one(self.v,L),one(self.f,R)
 def objective(self,t,mode='both'):
  vv,ff=self.margins(np.asarray(t).T if np.asarray(t).ndim==2 else t)
  v=np.sort(vv,axis=1)[:,1:];f=np.sort(ff,axis=1)[:,1:]
  eps=1e-5
  vo=np.sum(np.minimum(v-eps,0)**2,axis=1);fo=np.sum(np.minimum(f-eps,0)**2,axis=1)
  loss=vo+fo if mode=='both' else (vo if mode=='U' else fo)
  return loss if np.asarray(t).ndim==2 else float(loss[0])
 def report(self,t):
  v,f=self.margins(t)
  return dict(t=list(map(float,t)),A=self.matrices(t)[0].tolist(),strict_U=int(np.sum(v[0]<0)),strict_S=int(np.sum(f[0]<0)),
   Uroots=np.flatnonzero(v[0]<0).tolist(),Sroots=np.flatnonzero(f[0]<0).tolist(),U_second=float(np.sort(v[0])[1]),S_second=float(np.sort(f[0])[1]),
   objective=self.objective(t),condition=float(np.linalg.cond(self.matrices(t)[0])),U_margins=v[0].tolist(),S_margins=f[0].tolist())

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--name',default='LOW121');ap.add_argument('--seed',type=int,default=190929);ap.add_argument('--runs',type=int,default=6);ap.add_argument('--mode',default='both');ap.add_argument('--maxiter',type=int,default=1200);args=ap.parse_args()
 m=Affine(args.name);base=m.report(np.zeros(5));print('BASE',base,flush=True)
 best=None;bounds=[(-3,3),(-6,6),(-3,3),(-6,6),(-6,6)]
 for k in range(args.runs):
  r=differential_evolution(lambda t:m.objective(t,args.mode),bounds,seed=args.seed+k,popsize=16,maxiter=args.maxiter,tol=1e-9,atol=1e-15,vectorized=True,updating='deferred',polish=False,x0=np.zeros(5) if best is None else np.clip(best['t'],np.array(bounds)[:,0],np.array(bounds)[:,1]))
  rr=minimize(lambda t:m.objective(t,args.mode),r.x,method='Nelder-Mead',bounds=bounds,options=dict(maxiter=5000,xatol=1e-11,fatol=1e-16))
  out=m.report(rr.x if rr.fun<r.fun else r.x);out.update(run=k,mode=args.mode,seed=args.seed+k,numpy=np.__version__)
  print('AFFINE_SCREEN',json.dumps(out),flush=True)
  if best is None or out['objective']<best['objective']:best=out
  Path(args.name+'_AFFINE_'+args.mode+'_SCREEN.json').write_text(json.dumps(dict(base=base,best=best,last=out),sort_keys=True,separators=(',',':'))+'\n')
if __name__=='__main__':main()
```

## Complete affine_milp.py

```python
"""Finite PSD-outer MILP search of LOW121 affine U1, NOT an exclusion proof.
Each selected outgoing true edge has x_i^T G(x_j-x_i)>delta, with one
exceptional root allowed.  Negative-eigenvector cuts refine the outer PSD cone.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,time,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,csc_array
sys.set_int_max_str_digits(0)
def coeff(u,v):
 return np.array([u[0]*v[0],u[1]*v[1],u[2]*v[2],u[0]*v[1]+u[1]*v[0],u[0]*v[2]+u[2]*v[0],u[1]*v[2]+u[2]*v[1]])
def mat(a):return np.array([[a[0],a[3],a[4]],[a[3],a[1],a[5]],[a[4],a[5],a[2]]])
j=json.loads(Path('LOW121_EXACT.json').read_text());p=np.array([[float(F(v)) for v in row] for row in j['points']]);c=np.array([float(F(v)) for v in j['centroid']]);p-=c
# Invertible numerical preconditioning changes coordinates, not search space.
w,Q=np.linalg.eigh(p.T@p);B=Q@np.diag(1/np.sqrt(w));p=p@B
p/=np.max(np.linalg.norm(p,axis=1));nbr=[set() for _ in p]
for f in j['faces']:
 for u,v in zip(f,f[1:]+f[:1]):nbr[u].add(v);nbr[v].add(u)
arcs=[(i,k) for i,nn in enumerate(nbr) for k in sorted(nn)]
co=[]
for i,k in arcs:
 u=p[i];e=p[k]-p[i];co.append(coeff(u,e)/np.linalg.norm(u)/np.linalg.norm(e))
co=np.array(co);v=len(p);e=len(arcs);n=7+e+v
low=np.r_[[0.,0.,0.,-.5,-.5,-.5],0.,np.zeros(e+v)];up=np.r_[[1.,1.,1.,.5,.5,.5],1.,np.ones(e+v)]
integ=np.r_[np.zeros(7),np.ones(e+v)];obj=np.zeros(n);obj[6]=-1
rng=np.random.default_rng(190930);dirs=[np.eye(3)[i] for i in range(3)]+[p[k]-p[i] for i,k in arcs]+list(rng.normal(size=(240,3)))
records=[]
for iteration in range(6):
 rows=[];lbs=[];ubs=[]
 def add(row,l=-np.inf,u=np.inf):rows.append(row);lbs.append(l);ubs.append(u)
 add({0:1.,1:1.,2:1.},1,1)
 add({7+e+i:1. for i in range(v)},u=1)
 for i in range(v):add({**{7+k:1. for k,(a,b) in enumerate(arcs) if a==i},7+e+i:1.},l=1)
 for k,a in enumerate(co):
  # exact box minimum of linear expression for the numerical coefficients
  amin=np.sum(np.where(a>=0,a*low[:6],a*up[:6]));big=1-amin
  row={i:float(a[i]) for i in range(6)};row[6]=-1;row[7+k]=-big
  add(row,l=-big)
 for d in dirs:
  d=d/np.linalg.norm(d);a=coeff(d,d);add({i:float(a[i]) for i in range(6)},l=0)
 A=lil_matrix((len(rows),n))
 for r,row in enumerate(rows):
  for col,value in row.items():A[r,col]=value
 start=time.time();res=milp(obj,integrality=integ,bounds=Bounds(low,up),constraints=LinearConstraint(csc_array(A),lbs,ubs),options={'time_limit':60.,'mip_rel_gap':1e-7,'presolve':True})
 rec=dict(iteration=iteration,status=int(res.status),message=res.message,elapsed=time.time()-start,mip_gap=getattr(res,'mip_gap',None),dual_bound=getattr(res,'mip_dual_bound',None))
 if res.x is not None:
  G=mat(res.x[:6]);ev,E=np.linalg.eigh(G);esc=co@res.x[:6]
  scores=np.array([max(esc[k] for k,(a,b) in enumerate(arcs) if a==i) for i in range(v)])
  rec.update(G=G.tolist(),B=B.tolist(),delta=float(res.x[6]),eigenvalues=ev.tolist(),Uroots=np.flatnonzero(scores<=0).tolist(),root_binary=np.flatnonzero(res.x[7+e:]>0.5).tolist(),score=scores.tolist())
  dirs.extend(E[:,i] for i in range(3) if ev[i]<1e-8)
 records.append(rec);print('MILP_SCREEN',json.dumps(rec),flush=True)
 Path('LOW121_AFFINE_MILP_SCREEN.json').write_text(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n')
 if res.x is None or (ev[0]>1e-8 and res.x[6]>1e-8):break
```
