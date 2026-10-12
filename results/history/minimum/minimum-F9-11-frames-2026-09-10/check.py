"""Independent exact verifier; CPython3.13.5, standard library only.
No numerical producer imports. Scalar expansion, Bareiss, and Fraction LDL.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
from inputs import PARENTS,TREES,PLAN
assert __debug__
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for t in product((0,7,10),repeat=8):
  if sum(t)!=27 or t.count(10)!=2 or t.count(7)!=1:continue
  w=[0]*9;w[a]=9
  for i,v in zip(ids,t):w[i]=v
  out.append(w)
 assert len(out)==168 and len(set(map(tuple,out)))==168
 return sorted(out)
def expand(h,w,mu,edges,off,z,factor,sign):
 c={}
 def add(i,j,v):
  key=(min(i,j),max(i,j));c[key]=c.get(key,0)+v
 for i in range(9):
  for j in range(9):add(i,j,40*h[i]*w[j])
 for (i,j),v in zip(edges,mu):add(i,i,360*v);add(i,j,-360*v)
 k=0
 for i in range(9):
  add(i,i,-1)
  for j in range(i,9):add(i,j,360*sign*off[k]+2*factor*z[k]);k+=1
 a=[[0]*9 for _ in range(9)]
 for (i,j),v in c.items():
  if i==j:a[i][i]=v
  else:assert v%2==0;a[i][j]=a[j][i]=v//2
 return a
def bareiss(a):
 a=[r[:] for r in a];previous=1;out=[]
 for k in range(9):
  pivot=a[k][k];assert pivot>0;out.append(pivot)
  for i in range(k+1,9):
   for j in range(k+1,9):
    z=pivot*a[i][j]-a[i][k]*a[k][j];assert z%previous==0;a[i][j]=z//previous
  previous=pivot
 return out
def ldl(a,minors):
 L=[[F(i==j) for j in range(9)] for i in range(9)];D=[];prod=F(1)
 for k in range(9):
  pivot=F(a[k][k])-sum(L[k][j]**2*D[j] for j in range(k));assert pivot>0
  D.append(pivot);prod*=pivot;assert prod==minors[k]
  for i in range(k+1,9):L[i][k]=(F(a[i][k])-sum(L[i][j]*L[k][j]*D[j] for j in range(k)))/pivot
if __name__=='__main__':
 raw=Path('shadow_exact.json').read_bytes();obj=json.loads(raw)
 assert raw==serial(obj) and obj['tag']=='NOVA24_F9_11_SHADOW_FRAMES_V1'
 assert obj['parents']==[list(p) for p in PARENTS] and len(obj['records'])==len(PLAN)==12
 streams={k:hashlib.sha256() for k in ('weights','matrices','minors','couplings')};nm=0;nz=0;nfree=0;nmu=0
 for ix,(o,ex,rows) in enumerate(PLAN):
  r=obj['records'][ix];assert (r['index'],r['ordinal'],r['extra'],r['rows'])==(ix,o,list(ex),list(rows))
  g=r['g'];mu=r['mu'];assert len(g)==(108 if len(rows)==2 else 9) and all(type(v) is int for v in g)
  assert len(mu)==168*len(rows) and all(len(u)==9 and all(type(v) is int and v>=0 for v in u) for u in mu)
  off=g[18:63] if len(rows)==2 else [0]*45;z=g[63:108] if len(rows)==2 else [0]*45
  edges=[(i,TREES[o][i]) for i in range(1,9)]+[ex]
  assert len(set(edges))==9
  if len(rows)==2:
   Z=[[0]*9 for _ in range(9)];k=0
   for i in range(9):
    for j in range(i,9):Z[i][j]=Z[j][i]=(2 if i==j else 1)*z[k];k+=1
   minors=bareiss(Z);ldl(Z,minors);nz+=1;streams['couplings'].update(serial([ix,Z,minors]))
  for ri,a in enumerate(rows):
   for wi,w in enumerate(weights(a)):
    factor=20*w[rows[1-ri]]-181 if len(rows)==2 else 0
    A=expand(g[9*ri:9*ri+9],w,mu[168*ri+wi],edges,off,z,factor,1 if ri==0 else -1)
    minors=bareiss(A);ldl(A,minors)
    for key,val in [('weights',w),('matrices',A),('minors',minors)]:streams[key].update(serial([ix,a,wi,val]))
    nm+=1
  nfree+=len(g);nmu+=sum(map(len,mu));print('EXACT_NEW_SHADOW_PASS',ix,o,list(ex),len(mu),flush=True)
 assert (nm,nz,nfree,nmu)==(3024,6,702,27216)
 report=dict(tag='NOVA24_F9_11_SHADOW_VERIFIED_V1',parents=PARENTS,cases=len(PLAN),matrices=nm,coupling_matrices=nz,positive_leading_minors=9*(nm+nz),free_integers=nfree,multiplier_integers=nmu,coefficient_bytes=len(raw),coefficient_sha256=hashlib.sha256(raw).hexdigest(),streams={k:v.hexdigest() for k,v in streams.items()})
 b=serial(report);Path('shadow_verified.json').write_bytes(b)
 print('INDEPENDENT_SCALAR_BAREISS_FRACTION_LDL_PASS',nm,nz,9*(nm+nz))
 print('ONE_PHYSICAL_LAMBDA_RECIPROCAL_PAIR_AVERAGING_PASS')
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
