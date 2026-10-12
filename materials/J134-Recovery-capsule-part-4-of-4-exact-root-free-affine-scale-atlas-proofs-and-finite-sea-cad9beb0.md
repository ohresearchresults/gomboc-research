# material-cad9beb0fe55

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J134 Recovery capsule part 4 of 4 — exact affine scale elimination

## Dependencies, commands and evidence

Ordered recovery family: part1 [internal-source-reference], part2 [internal-source-reference], part3 [internal-source-reference], this part4. PART3'S SINGLE-TOKEN INPUT CORRECTION IS MANDATORY for TWIST_G10; it restores its original expected hash, not a new body. Parts1+2+the part3 correction recover endpoints. The remaining part3 units recover the selected numerical producer. All four parts give the selected complete scientific method closure including this exact scale census. Save each source unit under its filename. Python3.13.5/NumPy2.3.5/SciPy1.17.0, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1.

After corrected endpoint replay, exact commands actually executed: `python scale_exact134.py --tag SHORT --grid 4` and `python scale_exact134.py --tag TWIST --grid 4`. Their complete rational interval/cell/boundary ledgers are reconstructed from these inputs; no giant ledger needs to be copied from the old sandbox. Expected output identities:

- J134_C2_SHORT_G4.exact_scale.json:332280 bytes,SHA256287c1500a721796dfe2349725a02f957917c38026fc41db2fce86fe86eff8248. 28 nonempty carrier intervals,22 positive finite endpoints,23 open cells,zero identically-weak intervals,strict110_cells=[]. Class pairs (S,U)=(1,3),(3,3),(5,3),(7,3),(9,3),(11,3),(13,3),(15,3),(17,3).
- J134_C2_TWIST_G4.exact_scale.json:999204 bytes,SHA256eaa5682f9b3a314301f6834b8a0bcfb772e6c69566a540f0138ba52a1765f4b6. 52 intervals,46 positive finite endpoints,47 open cells,zero identically-weak intervals,strict110_cells=[]. Pairs (1,3),(3,3),(3,5),(5,3),(7,3),(9,3),(11,3),(13,3),(15,3),(17,3),(19,3),(21,3),(23,3),(25,3),(27,3).

Every finite positive interval endpoint in each ledger has a listed weak carrier. Thus neither body admits strict weak-free110 at ANY s>0 in the entire isotropic transverse slice G=diag(s,s,1). This is an exact unbounded one-parameter exclusion, NOT an exclusion of all SPD metrics, nonzero shear or changed geometry.

The floating outer search commands executed were `python capgate134.py` and `python free_metric134.py --tag SHORT --iterations 120`, likewise TWIST. Exact cap-projection tests fail the proposed gate for all three G4 bodies: SHORT180 negative edge-point tests/56 violating vertices, WIDE238/82,TWIST256/84. Thus the conditional projection lemma below does NOT exclude these bodies. A70-iteration two-parameter TWIST metric search finds no feasible scale and ends erosion score-.16244983673095703. The120-iteration four-parameter searches find no feasible scale: SHORT score-.2201528549194336 and TWIST-.16244983673095703. Printed U/S counts for negative scores are counts AFTER ARTIFICIAL INTERVAL EROSION, NOT equilibria of a constructed body. In particular printed U/S1/1 there is NOT a numerical110 candidate. Search parameters and every iteration limit/seed are literal in the code. Its shear is restricted to rho<=.99 of the retained cap-foot polygon; it is not an exhaustive arbitrary-shear search. The general exact formulas themselves allow any specified rational shear.

## Proof: all-scale and root-free census for a fixed physical affine slice

Let a full-dimensional convex rational body K have its own uniform-volume centroid g. Write its centred physical vertices p_i=(w_i,z_i), and its centred polar vertices q_f=n_f/(h_f-n_f.g). Fix a transverse positive-definite symmetric2x2 matrix A and a shear t. Apply T_t(w,z)=(w+t z,z), then an affine map whose metric is diag(sA,1),s>0. Overall metric G=T_t^T diag(sA,1)T_t. Every positive-definite3x3 metric has such a representation up to a positive overall scalar by its Schur complement; det(A)=1 can be imposed by absorbing scale in s. The actual centroid follows the physical affine transformation, since the density remains uniform and its Jacobian is constant. There is no independent reference-centre fit.

After the shear, each physical outgoing radial guard is

    p_i^T diag(sA,1)(p_j-p_i) = s a_ij + b_ij,
    a_ij = w_i^T A(w_j-w_i), b_ij = z_i(z_j-z_i).

The sheared polar vertices are (q_xy,q_z-t.q_xy). Their outgoing guards in the inverse metric diag(s^-1 A^-1,1), multiplied by positive s, are

    a^q_ij + s b^q_ij,
    a^q_ij = q_xy,i^T A^-1(q_xy,j-q_xy,i),
    b^q_ij = zq_i(zq_j-zq_i).

For ONE vertex, the set of s>0 for which ALL outgoing guards are nonpositive is the intersection of finitely many closed scalar half-lines. It is one closed interval relative to the positive axis, possibly empty, unbounded or a single point. A vertex is strictly unstable iff all guards are strictly negative; using all vertices instead of just neighbours is equivalent because a linear functional attains its maximum over the convex hull at the vertices. Polar strict unstable vertices are precisely primal strict stable facets. Equality on a nonadjacent vertex cannot be ignored: a supporting exposed face containing it and the tested vertex then also supplies an incident zero guard.

Collect positive finite endpoints of all nonempty physical AND polar intervals. On each open cell between them, a nonempty active carrier interval has every nonconstant guard strictly negative. Its only possible failure of strictness is an off-diagonal guard that is identically zero in s; the exact engine records this separately as a weak carrier. Isolated zero-length intervals survive as boundary weak events. Thus every cell's exact S,U and weakS,weakU are obtained simply by counting interval membership, with NO chosen physical or polar root and NO spanning-tree policy. Every finite positive endpoint of a nonempty carrier interval has a weak carrier. A strict weak-free110 cannot exist only at such an endpoint: strict inequalities persist on a neighbourhood in s.

If an open cell has S=U=1 and no weak face/vertex equilibria, it also has no weak edge equilibrium. A non-strict edge equilibrium has one of four nonnegative defining quantities zero: foot at an endpoint gives a weak vertex; zero coefficient in the two incident outward normals gives a weak facet with foot on its boundary. With weak cases absent, S+U-H=2 gives H=0. Hence the exact cell test is sufficient and necessary for strict weak-free110 along the specified affine slice. No inference is made about primitive incidence zeros that do not define an equilibrium.

For exact speed the polar rows can be cleared without forming huge centred polar denominators. With sheared unscaled normals n,m and their positive supports H,J, multiply the polar guard by H^2 J. Its coefficients become

    s[H n_z m_z - J n_z^2] + [H n_xy^T A^-1 m_xy - J n_xy^T A^-1 n_xy].

These retain exactly the same signs. The code uses primitive integer maximal support normals and the exact own centroid. It checks A is symmetric positive definite. Interval bounds and the complete cell census are Fractions, not tolerance tests.

## Conditional cap-projection gate, and why it does not apply here

Suppose an upper horizontal cap lies strictly above g and its transverse projection contains the projection of the ENTIRE C2-symmetric body. For any transverse SPD metric B, choose a cap vertex maximizing w^T B w. Every projected body point has B-norm at most this maximum by convexity. Cauchy-Schwarz gives w^T B(v-w)<=0, strictly for any different equally high cap vertex; for points strictly below the cap the vertical guard z(z'-z) is negative. Thus this cap vertex is strictly U under diag(B,1), as is its C2 partner. If a unique lowest axial vertex is retained it is strictly U too, so U>=3. This is a retained-geometry sufficient obstruction, not a symmetry theorem. The code tests the projection hypothesis exactly. It FAILS for SHORT,WIDE,TWIST, so none of the three receives an all-transverse-SPD exclusion from this lemma. The executed all-slice interval exclusions above are a different valid result.

## interval134.py — 4364 bytes; SHA256 3e92cb8c86b72b80bd2073f6a4df6cffdb10dfb831ecb47d3dd1ff0a07eab25c
```python
"""Eliminate the transverse scale exactly (up to floating evaluation) in a
C2-preserving affine search. Every undesired radial vertex has a CLOSED
forbidden scale interval: all its outgoing affine guards are <=0 there.
Physical guards are s*a+b; polar guards multiplied by s are a+s*b.
The union of these intervals, not a near-zero local-max loss, decides
whether a strictly feasible scale exists for each chosen shape matrix.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json,numpy as np,argparse
from pathlib import Path
from scipy.optimize import differential_evolution
import hspace134 as hs

def interval(a,b):
 with np.errstate(divide='ignore',invalid='ignore'):t=-b/a
 lo=np.max(np.where(a<0,t,-np.inf),axis=1);hi=np.min(np.where(a>0,t,np.inf),axis=1)
 invalid=np.any((a==0)&(b>0),axis=1)|(hi<=0)|(lo>hi)
 lo=np.maximum(lo,0)
 with np.errstate(divide='ignore',invalid='ignore'):lo=np.log(lo);hi=np.log(np.where(hi>0,hi,1.))
 return lo,hi,~invalid

class Problem:
 def __init__(self,Y,Q,proot,qroot):
  self.Y=Y;self.Q=Q;self.proot=proot;self.qroot=qroot
  self.bP=Y[:,2,None]*Y[None,:,2]-Y[:,2,None]**2
  self.bQ=Q[:,2,None]*Q[None,:,2]-Q[:,2,None]**2
  self.maskP=np.arange(len(Y))!=proot;self.maskQ=np.arange(len(Q))!=qroot
 def forbidden(self,v):
  eta,theta=v;cs,sn=np.cos(theta),np.sin(theta);R=np.array([[cs,-sn],[sn,cs]]);G=R@np.diag([np.exp(eta),np.exp(-eta)])@R.T;Gi=R@np.diag([np.exp(-eta),np.exp(eta)])@R.T
  aP=self.Y[:,:2]@G@self.Y[:,:2].T;aP-=np.diag(aP)[:,None]
  aQ=self.Q[:,:2]@Gi@self.Q[:,:2].T;aQ-=np.diag(aQ)[:,None]
  lp,up,vp=interval(aP,self.bP);lq,uq,vq=interval(self.bQ,aQ)
  valid=np.r_[vp&self.maskP,vq&self.maskQ];lo=np.r_[lp,lq][valid];hi=np.r_[up,uq][valid]
  ids=np.flatnonzero(valid);order=np.argsort(lo);return lo[order],hi[order],ids[order],G
 @staticmethod
 def gaps(lo,hi,epsilon=0):
  # epsilon>0 erodes each individual bad interval. Negative epsilon dilates it.
  l=lo+epsilon;h=hi-epsilon;valid=l<=h;l=l[valid];h=h[valid]
  if not len(l):return [(-np.inf,np.inf)]
  out=[];end=-np.inf
  for a,b in zip(l,h):
   if a>end:out.append((end,a))
   end=max(end,b)
  if end<np.inf:out.append((end,np.inf))
  return out
 def evaluate(self,v,full=False):
  lo,hi,ids,G=self.forbidden(v);gaps=self.gaps(lo,hi)
  if gaps:
   left,right=max(gaps,key=lambda t:t[1]-t[0]);score=(right-left)/2;centre=(left+right)/2
   if not np.isfinite(centre):centre=right-1 if np.isfinite(right)else left+1 if np.isfinite(left) else 0.
   score=min(score,100.)
  elif np.any(np.isneginf(lo)&np.isposinf(hi)):score=-100.;centre=0.
  else:
   lower,upper=0.,1.
   while not self.gaps(lo,hi,upper) and upper<64:upper*=2
   for _ in range(22):
    mid=(lower+upper)/2
    if self.gaps(lo,hi,mid):upper=mid
    else:lower=mid
   score=-upper;gg=self.gaps(lo,hi,upper+1e-7);left,right=max(gg,key=lambda t:t[1]-t[0]);centre=(left+right)/2
   if not np.isfinite(centre):centre=0.
  if full:return dict(score=float(score),logscale=float(centre),G=(G*np.exp(centre)).tolist(),lo=lo.tolist(),hi=hi.tolist(),ids=ids.tolist())
  return -score

def run(index=0,iterations=100):
 src=json.load(open('HEAD134_RESULTS.json'));rows=[x for x in src if 'H'in x and x['E']<=249];r=rows[index];z=hs.geometry(np.array(r['H']),np.array([0,0,r['c']]));Y=z['X']-z['centroid'];Q=z['Q'];u=int(np.argmin(Y[:,2]));q=z['root'];p=Problem(Y,Q,u,q)
 res=differential_evolution(p.evaluate,[(0.,8.),(0.,np.pi)],seed=134+index,maxiter=iterations,popsize=15,tol=1e-8,polish=True)
 d=p.evaluate(res.x,True);d.update(v=res.x.tolist(),index=index,c=r['c'],n=r['n'],nit=res.nit,nfev=res.nfev,success=bool(res.success));Path(f'INTERVAL134_{index}.json').write_text(json.dumps(d,separators=(',',':'))+'\n');print('INTERVAL',r['c'],r['n'],res.fun,res.x,'s',np.exp(d['logscale']),'nfev',res.nfev,flush=True)
 if d['score']>0:
  G=np.array(d['G']);w,V=np.linalg.eigh(G);A=V@np.diag(np.sqrt(w))@V.T;XX=z['X'].copy();XX[:,:2]=XX[:,:2]@A.T
  Path(f'INTERVAL134_CANDIDATE_{index}.json').write_text(json.dumps(dict(X=XX.tolist(),G=d['G'],source=dict(c=r['c'],n=r['n'],kappa=r['kappa'])),separators=(',',':'))+'\n');print('STRICT_NUMERICAL_FEASIBLE_SCALE',d['score'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--index',type=int,default=0);p.add_argument('--iterations',type=int,default=100);a=p.parse_args();run(a.index,a.iterations)
```

## capgate134.py — 2741 bytes; SHA256 035b43f4dd64a84d6e4e7ce786220558696e601eb90472b4ab3976b54447afca
```python
"""Exact cap-projection gate and finite affine-scale experiments on exact bodies.
If the upper horizontal cap projects over the entire C2 body and lies above
its own centroid, then every transverse SPD metric has a paired strict
unstable vertex on that cap. The lower axial root remains strict U, so U>=3.
This excludes this retained geometric gate, not all C2 geometries.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from fractions import Fraction as F
from pathlib import Path
import json,sys,numpy as np
from scipy.optimize import differential_evolution
import geom134 as e
from interval134 import Problem
sys.set_int_max_str_digits(0)
def load(tag,grid=4):
 name=f'J134_C2_{tag}_G{grid}';d=json.load(open(name+'.audit.json'));X=[tuple(F(t)for t in p)for p in json.load(open(name+'.points.json'))['points']];g=tuple(F(t)for t in d['centroid']);Y=[e.sub(p,g)for p in X];Q=[]
 for cy in d['faces']:
  a,b,c=[Y[i]for i in cy[:3]];n=e.cross(e.sub(b,a),e.sub(c,a));hh=e.dot(n,a);Q.append(e.mul(1/hh,n))
 return name,d,X,g,Y,Q

def cross2(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def gate(tag,grid=4):
 name,d,X,g,Y,Q=load(tag,grid);cy=d['S_cycles'][0];assert len(set(X[i][2]for i in cy))==1
 capz=X[cy[0]][2];assert capz>g[2];bad=[];allsg=[]
 for a,b in zip(cy,cy[1:]+cy[:1]):
  sg=[cross2(X[a],X[b],p)for p in X];allsg.extend(sg)
  for i,v in enumerate(sg):
   if v<0:bad.append([a,b,i,str(v)])
 out=dict(name=name,cap=cy,cap_above_g=True,all_points_below_cap=all(p[2]<=capz for p in X),projection_contains_entire_body=not bad,negative_tests=len(bad),violating_vertices=sorted(set(x[2]for x in bad)),minimum=str(min(allsg)),bad=bad)
 Path(name+'.cap_gate.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print('CAP_GATE',tag,not bad,'negative',len(bad),'vertices',out['violating_vertices'],flush=True);return out

def finite(tag,grid=4,iterations=70):
 name,d,X,g,Y,Q=load(tag,grid);root=next(i for i,p in enumerate(X)if p==(F(0),F(0),F(-1)));qroot=d['S'][0]
 assert Y[root][2]<0 and all(p[2]>Y[root][2]for i,p in enumerate(Y)if i!=root)
 assert Q[qroot][:2]==(F(0),F(0)) and all(p[2]<Q[qroot][2]for i,p in enumerate(Q)if i!=qroot)
 p=Problem(np.array(Y,float),np.array(Q,float),root,qroot);res=differential_evolution(p.evaluate,[(0.,8.),(0.,np.pi)],maxiter=iterations,popsize=12,seed=2134,tol=1e-8,polish=False)
 r=p.evaluate(res.x,True);r.update(name=name,parameters=res.x.tolist(),nfev=res.nfev,nit=res.nit,success=bool(res.success))
 Path(name+'.metric_intervals.json').write_text(json.dumps(r,separators=(',',':'))+'\n');print('EXACT_SHAPE_METRIC',tag,r['score'],res.x,flush=True)
if __name__=='__main__':
 for tag in ['SHORT','WIDE','TWIST']:gate(tag)
 finite('TWIST')
```

## free_metric134.py — 4718 bytes; SHA256 4d7835a3e0e594b44368797689bd311073cb744a743ce174f953e810a9836205
```python
"""Root-free one-scale census for a general SPD affine metric.
G = shear(t)^T diag(s*A,1) shear(t), A SPD det1, s>0.
All physical vertices and polar vertices have closed forbidden/all-outgoing-
nonpositive scale intervals. On each open endpoint cell, interval counts
are the strict U and S counts (except an identically-zero guard, separately
excluded in exact certification). A sweep removes both scale and root choice.
No negative erosion score is a theorem over the remaining four parameters.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import argparse,json,numpy as np
from scipy.optimize import differential_evolution
from interval134 import interval
from capgate134 import load

class FreeProblem:
 def __init__(self,tag,grid=4):
  self.name,self.d,self.X,self.g,yp,qp=load(tag,grid);self.Y=np.array(yp,float);self.Q=np.array(qp,float)
  cy=self.d['S_cycles'][0];Z=self.Y[cy[0],2];assert Z>0
  polygon=-self.Y[cy,:2]/Z;D=np.roll(polygon,-1,axis=0)-polygon
  self.normals=np.c_[D[:,1],-D[:,0]];self.heights=np.einsum('ij,ij->i',self.normals,polygon);assert min(self.heights)>0
 def decode(self,v):
  eta,theta,rho,az=v;cs,sn=np.cos(theta),np.sin(theta);R=np.array([[cs,-sn],[sn,cs]])
  A=R@np.diag([np.exp(eta),np.exp(-eta)])@R.T;Ai=R@np.diag([np.exp(-eta),np.exp(eta)])@R.T
  direction=np.array([np.cos(az),np.sin(az)]);den=self.normals@direction;rad=min(self.heights[den>0]/den[den>0]);t=rho*rad*direction
  return A,Ai,t
 def intervals(self,v):
  A,Ai,t=self.decode(v);Y=self.Y.copy();Q=self.Q.copy();Y[:,:2]+=Y[:,2,None]*t;Q[:,2]-=Q[:,:2]@t
  a=Y[:,:2]@A@Y[:,:2].T;a-=np.diag(a)[:,None];b=Y[:,2,None]*Y[None,:,2]-Y[:,2,None]**2
  ap=Q[:,:2]@Ai@Q[:,:2].T;ap-=np.diag(ap)[:,None];bp=Q[:,2,None]*Q[None,:,2]-Q[:,2,None]**2
  l,h,valid=interval(a,b);lq,hq,vq=interval(bp,ap)
  return np.r_[l[valid],lq[vq]],np.r_[h[valid],hq[vq]],np.r_[np.zeros(sum(valid),int),np.ones(sum(vq),int)],np.r_[np.flatnonzero(valid),len(Y)+np.flatnonzero(vq)],A,t
 @staticmethod
 def goodcells(lo,hi,typ,erosion=0):
  l=lo+erosion;h=hi-erosion;mask=l<=h;l=l[mask];h=h[mask];typ=typ[mask]
  p0=int(sum((typ==0)&np.isneginf(l)));q0=int(sum((typ==1)&np.isneginf(l)))
  ends=np.r_[l[np.isfinite(l)],h[np.isfinite(h)]];tt=np.r_[typ[np.isfinite(l)],typ[np.isfinite(h)]];sg=np.r_[np.ones(np.isfinite(l).sum(),int),-np.ones(np.isfinite(h).sum(),int)]
  if not len(ends):return [(-np.inf,np.inf,p0,q0)]if p0<=1 and q0<=1 else []
  vals,idx=np.unique(ends,return_inverse=True);dp=np.zeros(len(vals),int);dq=dp.copy();np.add.at(dp,idx[tt==0],sg[tt==0]);np.add.at(dq,idx[tt==1],sg[tt==1]);cp=np.r_[p0,p0+np.cumsum(dp)];cq=np.r_[q0,q0+np.cumsum(dq)]
  left=np.r_[-np.inf,vals];right=np.r_[vals,np.inf];mask=(cp<=1)&(cq<=1)&(right-left>1e-9)
  return [(float(a),float(b),int(p),int(q))for a,b,p,q in zip(left[mask],right[mask],cp[mask],cq[mask])]
 def evaluate(self,v,full=False):
  l,h,ty,ids,A,t=self.intervals(v);cells=self.goodcells(l,h,ty)
  if cells:
   a,b,pu,ps=max(cells,key=lambda x:x[1]-x[0]);score=min((b-a)/2,100.)
  else:
   low,up=0.,.25
   while not self.goodcells(l,h,ty,up) and up<64:up*=2
   if up>=64:score=-100.;a=b=0.;pu=ps=-1
   else:
    for _ in range(18):
     mid=(low+up)/2
     if self.goodcells(l,h,ty,mid):up=mid
     else:low=mid
    score=-up;a,b,pu,ps=max(self.goodcells(l,h,ty,up+1e-7),key=lambda x:x[1]-x[0])
  centre=(a+b)/2
  if not np.isfinite(centre):centre=b-1 if np.isfinite(b)else a+1 if np.isfinite(a)else 0.
  if full:return dict(score=score,logscale=centre,scale=float(np.exp(centre)),A=A.tolist(),shear=t.tolist(),U=pu,S=ps,lo=l.tolist(),hi=h.tolist(),types=ty.tolist(),ids=ids.tolist())
  return -score

def run(tag,iterations):
 p=FreeProblem(tag);res=differential_evolution(p.evaluate,[(0.,8.),(0.,np.pi),(0.,.99),(0.,np.pi)],popsize=12,maxiter=iterations,seed=3134,tol=1e-7,polish=False)
 r=p.evaluate(res.x,True);r.update(name=p.name,parameters=res.x.tolist(),nit=res.nit,nfev=res.nfev,success=bool(res.success));Path(p.name+'.free_metric.json').write_text(json.dumps(r,separators=(',',':'))+'\n');print('FREE_METRIC',tag,r['score'],res.x,'scale',r['scale'],'shear',r['shear'],'cells U/S',r['U'],r['S'],flush=True)
 if r['score']>0:
  T=np.eye(3);T[:2,2]=r['shear'];w,V=np.linalg.eigh(np.array(r['A'])*r['scale']);C=np.eye(3);C[:2,:2]=V@np.diag(np.sqrt(w))@V.T;C=C@T
  X=np.array(p.X,float)@C.T
  Path(p.name+'.free_candidate.json').write_text(json.dumps(dict(matrix=C.tolist(),X=X.tolist()),separators=(',',':'))+'\n')
if __name__=='__main__':
 q=argparse.ArgumentParser();q.add_argument('--tag',default='SHORT');q.add_argument('--iterations',type=int,default=120);a=q.parse_args();run(a.tag,a.iterations)
```

## scale_exact134.py — 3924 bytes; SHA256 3a35e5c74f4b5ed25ab7c1c3f0b5f3ab237134c039da0907c8ae641909183dad
```python
"""Exact root-free entire-scale census on a rational physical affine slice.
Physical G=diag(s*A,1), s>0; optional rational transverse shear t first.
For every primal or polar vertex, ALL outgoing guards are affine in s after
clearing positive support denominators. The exact closed interval where all
are <=0 contains every strict/weak radial maximum on that carrier. Interval
endpoints divide the entire positive scale axis into finitely many exact
cells. A cell census uses strictly negative rows; weak carriers are separate.
A zero-length carrier interval is retained as an isolated weak event.
"""
from fractions import Fraction as F
from pathlib import Path
import sys,json,argparse,hashlib
import geom134 as e
from capgate134 import load
sys.set_int_max_str_digits(0)

def bounds(rows):
 lo=F(0);hi=None;zero=False
 for a,b in rows:
  if not a:
   if b>0:return None
   if not b:zero=True
  elif a>0:
   t=-b/a;hi=t if hi is None else min(hi,t)
  else:lo=max(lo,-b/a)
 if hi is not None and (hi<=0 or lo>hi):return None
 return lo,hi,zero

def intervals(tag,grid=4,A=((F(1),F(0)),(F(0),F(1))),t=(F(0),F(0))):
 name,d,X,g,Y,Q=load(tag,grid);det=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert det>0 and A[0][0]>0 and A[0][1]==A[1][0]
 Ai=((A[1][1]/det,-A[0][1]/det),(-A[1][0]/det,A[0][0]/det))
 Z=[(p[0]+t[0]*p[2],p[1]+t[1]*p[2],p[2])for p in Y]
 def bilin(a,M,b):return sum(a[i]*M[i][j]*b[j]for i in range(2)for j in range(2))
 records=[]
 for i,p in enumerate(Z):
  rows=[]
  for j,q in enumerate(Z):
   if i!=j:rows.append((bilin(p,A,e.sub(q,p)),p[2]*(q[2]-p[2])))
  r=bounds(rows)
  if r is not None:records.append(dict(kind='U',id=i,lo=r[0],hi=r[1],identical_zero_guard=r[2]))
 # Integer primitive maximal support normals prevent enormous products of
 # two already centred polar-coordinate denominators.
 planes=[]
 for cy in d['faces']:
  a,b,c=[X[i]for i in cy[:3]];n=e.cross(e.sub(b,a),e.sub(c,a));hh=e.dot(n,a);nn=tuple(F(v)for v in e.prim((*n,hh)));H=nn[3]-e.dot(nn[:3],g);assert H>0
  planes.append(((nn[0],nn[1],nn[2]-t[0]*nn[0]-t[1]*nn[1]),H))
 for i,(n,H)in enumerate(planes):
  rows=[]
  for j,(m,J)in enumerate(planes):
   if i==j:continue
   a=H*n[2]*m[2]-J*n[2]*n[2];b=H*bilin(n,Ai,m)-J*bilin(n,Ai,n)
   rows.append((a,b))
  r=bounds(rows)
  if r is not None:records.append(dict(kind='S',id=i,lo=r[0],hi=r[1],identical_zero_guard=r[2]))
 endpoints=sorted({r[k]for r in records for k in ['lo','hi']if r[k]is not None and r[k]>0});cuts=[F(0)]+endpoints+[None];cells=[]
 for l,h in zip(cuts,cuts[1:]):
  q=(l+h)/2 if h is not None else max(F(1),2*l)
  roots={k:[]for k in ['S','U','weakS','weakU']}
  for r in records:
   if r['lo']<q and (r['hi']is None or q<r['hi']):roots[('weak'if r['identical_zero_guard']else '')+r['kind']].append(r['id'])
  cells.append(dict(lo=l,hi=h,sample=q,**roots))
 boundary=[]
 for q in endpoints:
  bad=[(r['kind'],r['id'])for r in records if r['lo']==q or r['hi']==q]
  assert bad;boundary.append(dict(scale=q,weak_carriers=bad))
 good=[j for j,r in enumerate(cells)if len(r['S'])==len(r['U'])==1 and not r['weakS'] and not r['weakU']]
 summary=dict(name=name,matrix=A,shear=t,interval_count=len(records),positive_endpoint_count=len(endpoints),open_cells=len(cells),strict110_cells=good,class_pairs=sorted({(len(r['S']),len(r['U']))for r in cells}),all_boundary_scales_have_weak_carrier=True,identically_weak_intervals=sum(r['identical_zero_guard']for r in records))
 out=dict(summary=summary,intervals=records,cells=cells,boundaries=boundary);b=(json.dumps(e.serial(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=name+'.exact_scale.json';Path(path).write_bytes(b)
 print(json.dumps(e.serial(summary)),dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest()),flush=True);return summary
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='TWIST');p.add_argument('--grid',type=int,default=4);a=p.parse_args();intervals(a.tag,a.grid)
```
