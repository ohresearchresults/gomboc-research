# material-f2fa7b03be35

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J76 complete numerical metric methods — finite negative evidence only

Both source units below require exact source [internal-source-reference] saved as J75_REFERENCE110_CAP233.py. Save each code fence verbatim with one final LF. metric76.py4131B SHAe2d787df39e0f224ebb3e8f9de7c7d66cc2dc2d7e62fdb4fbf746f9757a25f1d; frames76.py3173B SHAbc59760fdefa75a36a0198bbfc16023f7a7a2b42ea885eb2ec63431c40c7314f. Observed environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0; Shapely is used only for floating polygon unions. Its exact installed version is to be added to the shared notebook when recovered, not guessed here.

OPENBLAS_NUM_THREADS=1 python frames76.py 256 completed with seed760026, identity plus255 quaternion frames, eigenvalue floor1e-7 on the normalized scale simplex. It found no validated one-sided P1 or S1 hit; terminal FRAME_SWEEP_DONE 256 hits 0. The residual uncovered areas near1e-17 were not promoted to strict candidates. Output frames76.json159413B SHAac487f2ab02d18bd8f7344dbd12bcdb8302538db37b0e95936f92fc13860531c. This is a finite floating scan of256 orientations, NOT an exclusion of all SPD metrics. The separate exact native-diagonal proof is [internal-source-reference].

OPENBLAS_NUM_THREADS=1 python metric76.py implements a six-entry trace-one metric plus binary outgoing-witness MILP with necessary eigenvector cuts. The observed run was stopped during its repeated20-second solves because it kept proposing indefinite matrices and yielded no retained strict positive-definite solution. It did NOT complete the advertised maximum iterations and is not an infeasibility certificate. A positive MILP margin before positive-definiteness is satisfied is not physical evidence. The full implementation is retained as a reusable nomination method; do not cite its solver status as a geometry exclusion.

## metric76.py
```python
"""J76 metric experiments. Requires the exact preserved J75 source.
Floating nomination only, never a certificate of own110 or an exclusion.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json, time
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint, minimize
from scipy.sparse import lil_matrix, csr_matrix, vstack
import J75_REFERENCE110_CAP233 as m

def symmetric(c):
 return np.array([[c[0],c[3],c[4]],[c[3],c[1],c[5]],[c[4],c[5],c[2]]])
def vector(G):return G[[0,1,2,0,0,1],[0,1,2,1,2,2]]
def form(v,w):
 return np.array([v[0]*w[0],v[1]*w[1],v[2]*w[2],v[0]*w[1]+v[1]*w[0],v[0]*w[2]+v[2]*w[0],v[1]*w[2]+v[2]*w[1]])
def setup():
 K=m.hull(m.points());V,M=m.mass(K);centroid=m.mul(M,1/V)
 p=np.array([m.sub(v,centroid) for v in K['points']],float)
 n=np.array([m.cross(m.sub(K['points'][f[1]],K['points'][f[0]]),m.sub(K['points'][f[2]],K['points'][f[0]])) for f in K['faces']],float)
 heights=np.einsum('ij,ij->i',n,p[[f[0] for f in K['faces']]])
 q=n/heights[:,None]
 return K,centroid,p,q

def guards(p,edges):
 nb=[[] for _ in p]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 coeff=[];labels=[];groups=[]
 for i,js in enumerate(nb):
  group=[]
  for j in sorted(js):
   v,w=p[i],p[j]-p[i]
   group.append(len(coeff));coeff.append(form(v,w)/(np.linalg.norm(v)*np.linalg.norm(w)));labels.append((i,j))
  groups.append(group)
 return np.array(coeff),labels,groups

def counts(g,C,groups):
 values=C@vector(g)
 return [i for i,js in enumerate(groups) if max(values[js])<0]

def one_root_milp(C,labels,groups,root,time_limit=20,eps=1e-5,iterations=30):
 # G PSD with trace1; normalized outgoing scores are in [-1,1].
 n=len(C);N=7+n;A=lil_matrix((n+len(groups)+1,N));lo=np.full(A.shape[0],-np.inf);hi=np.full(A.shape[0],np.inf)
 A[:n,:6]=C;A[:n,6]=-1;A[np.arange(n),7+np.arange(n)]=-2;lo[:n]=-2
 for i,js in enumerate(groups):
  row=n+i
  if i!=root:A[row,7+np.array(js)]=1;lo[row]=1
  else:hi[row]=0
 A[-1,:3]=1;lo[-1]=hi[-1]=1
 A=A.tocsr()
 # The designated root has negative scores against all true neighbors.
 for k in groups[root]:
  r=np.zeros(N);r[:6]=-C[k];r[6]=-1;A=vstack([A,csr_matrix(r[None,:])]);lo=np.r_[lo,0];hi=np.r_[hi,np.inf]
 lb=np.r_[[eps]*3,[-.5]*3,0,np.zeros(n)];ub=np.r_[[1]*3,[.5]*3,1,np.ones(n)]
 lb[7+np.array(groups[root])]=ub[7+np.array(groups[root])]=0
 integ=np.r_[np.zeros(7),np.ones(n)];obj=np.zeros(N);obj[6]=-1
 # Necessary PSD inequalities, then eigenvector separation.
 for u in np.vstack([np.eye(3),np.array([[1,a,b] for a in [-1,0,1] for b in [-1,0,1]])]):
  r=np.zeros(N);r[:6]=form(u,u);A=vstack([A,csr_matrix(r[None,:])]);lo=np.r_[lo,eps*(u@u)];hi=np.r_[hi,np.inf]
 hist=[]
 for it in range(iterations):
  r=milp(obj,integrality=integ,bounds=Bounds(lb,ub),constraints=LinearConstraint(A,lo,hi),options={'time_limit':time_limit,'mip_rel_gap':.001})
  if r.x is None:
   print('MILP_NO_POINT',root,it,r.message,flush=True);return None,hist
  G=symmetric(r.x[:6]);ev,Q=np.linalg.eigh(G)
  hist.append({'iteration':it,'margin':r.x[6],'eigenvalues':ev.tolist(),'message':r.message,'dual_bound':getattr(r,'mip_dual_bound',None)})
  print('MILP',root,it,r.x[6],ev,r.message,flush=True)
  if ev[0]>=eps*.999:
   return {'G':G.tolist(),'margin':r.x[6],'chosen':[labels[k] for k in range(n) if r.x[7+k]>.5],'roots':counts(G,C,groups)},hist
  for u in Q.T[ev<eps*.999]:
   a=np.zeros(N);a[:6]=form(u,u);A=vstack([A,csr_matrix(a[None,:])]);lo=np.r_[lo,eps];hi=np.r_[hi,np.inf]
 return None,hist

def main():
 K,c,p,q=setup();CP,lp,gp=guards(p,K['edges']);CQ,lq,gq=guards(q,K['edge_faces'])
 print('baseline',counts(np.eye(3),CP,gp),counts(np.eye(3),CQ,gq),flush=True)
 for name,C,l,g,root in [('P',CP,lp,gp,6),('Q',CQ,lq,gq,53)]:
  result,hist=one_root_milp(C,l,g,root)
  out={'landscape':name,'result':result,'history':hist}
  Path(f'metric76_{name}.json').write_text(json.dumps(out,indent=2))
  if result:
   G=np.array(result['G']);other=np.linalg.inv(G);other/=np.trace(other)
   print('JOINT',name,counts(G,C,g),counts(other,CQ if name=='P' else CP,gq if name=='P' else gp),flush=True)
if __name__=='__main__':main()
```

## frames76.py
```python
"""Floating complete scale-simplex cell nomination per specified principal frame.
Requires metric76.py and its exact J75 input. No numerical union is a proof.
"""
import json,time,sys
from pathlib import Path
import numpy as np
from scipy.spatial.transform import Rotation
from scipy.optimize import minimize
from shapely.geometry import Polygon,GeometryCollection
from shapely.ops import unary_union
from metric76 import setup,guards,counts

def clip(poly,c):
 # c is the diagonal coefficient vector; c.lambda <=0.
 a=c[:2]-c[2];b=c[2]
 out=[]
 if not poly:return out
 for u,v in zip(poly,poly[1:]+poly[:1]):
  su=float(a@u+b);sv=float(a@v+b)
  if su<=0:out.append(u)
  if su*sv<0:out.append(u+(v-u)*su/(su-sv))
 return out

def single_regions(p,edges,Q,eps=1e-7):
 p=p@Q
 nb=[[] for _ in p]
 for i,j in edges:nb[i].append(j);nb[j].append(i)
 tri=[np.array([eps,eps]),np.array([1-2*eps,eps]),np.array([eps,1-2*eps])]
 allcells=[];seen=GeometryCollection();overlap=GeometryCollection()
 for i,js in enumerate(nb):
  poly=tri.copy()
  for j in js:
   poly=clip(poly,p[i]*(p[j]-p[i]))
   if len(poly)<3:break
  if len(poly)<3:continue
  cell=Polygon(poly)
  if not cell.is_valid:cell=cell.buffer(0)
  if cell.area<1e-18:continue
  allcells.append((i,cell))
  both=seen.intersection(cell)
  if not both.is_empty:overlap=overlap.union(both)
  seen=seen.union(cell)
 unique=Polygon(tri).difference(overlap)
 parts=[]
 for i,cell in allcells:
  region=cell.intersection(unique)
  if region.area>1e-15:parts.append((i,region))
 return parts,unique.area,len(allcells),seen.area

def pieces(g):
 if g.geom_type=='Polygon':return [g]
 if hasattr(g,'geoms'):return sum((pieces(h) for h in g.geoms),[])
 return []
def lam(pt):
 x,y=pt;return np.array([x,y,1-x-y])
def main(n=256):
 K,c,p,q=setup();CP,lp,gp=guards(p,K['edges']);CQ,lq,gq=guards(q,K['edge_faces'])
 rng=np.random.default_rng(760026)
 frames=[np.eye(3)]+[Rotation.from_quat(rng.normal(size=4)).as_matrix() for _ in range(n-1)]
 out=[];hit=[]
 for k,Q in enumerate(frames):
  P,pa,pn,pcov=single_regions(p,K['edges'],Q)
  S,sa,sn,scov=single_regions(q,K['edge_faces'],Q)
  row={'frame':k,'Q':Q.tolist(),'P_single_area':pa,'S_single_area':sa,'P_possible':pn,'S_possible':sn,'P_roots':[i for i,r in P],'S_roots':[i for i,r in S],'coverage':[pcov,scov]}
  for name,regions in [('P',P),('S',S)]:
   for root,reg in regions:
    for poly in pieces(reg):
     pt=poly.representative_point();la=lam((pt.x,pt.y));G=Q@np.diag(la)@Q.T
     if name=='S':G=np.linalg.inv(G);G/=np.trace(G)
     u=counts(G,CP,gp);s=counts(np.linalg.inv(G),CQ,gq)
     h={'frame':k,'name':name,'root':root,'lambda':la.tolist(),'G':G.tolist(),'U':u,'S':s}
     if len(u)==1 or len(s)==1:hit.append(h);print('ONE_SIDE',h,flush=True)
     if len(u)==1 and len(s)==1:print('NUMERICAL_110_CANDIDATE',flush=True)
  out.append(row)
  if k%8==0:print('FRAME',k,'areas',pa,sa,'possible',pn,sn,'hits',len(hit),flush=True)
  Path('frames76.json').write_text(json.dumps({'seed':760026,'epsilon':1e-7,'rows':out,'hits':hit},indent=2))
 print('FRAME_SWEEP_DONE',n,'hits',len(hit),flush=True)
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 256)
```
