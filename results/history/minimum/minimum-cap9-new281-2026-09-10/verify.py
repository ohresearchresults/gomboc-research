"""Independent exact CAP9 verifier; CPython 3.13.5, standard library only.
Imports neither engine nor builder. No floating-point operations.
Run: python -S verify.py [cap9_new.json]
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,sys
assert __debug__
R01={246,247,248,249,250,251,260,261,262,263,264,265,267,268,269,270,271,273,274,275,276,279,280,281}
R02={277,282,283,284}
REST={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
def parse(s):
 p=[];stack=[]
 for c in s:
  if c=='(':p.append(stack[-1] if stack else 0);stack.append(len(p)-1)
  else:assert stack;stack.pop()
 assert not stack
 return tuple(p)
def multisets():
 levels={1:['()']}
 for n in range(2,10):
  pool=sorted((s,k) for k in range(1,n) for s in levels[k]);out=[]
  def walk(left,start,parts):
   if left==0:out.append('('+''.join(parts)+')');return
   for i in range(start,len(pool)):
    s,k=pool[i]
    if k<=left:walk(left-k,i,parts+[s])
  walk(n-1,0,[]);assert len(out)==len(set(out));levels[n]=sorted(out)
 return levels
def array_code(p):
 def descend(i):return '('+''.join(sorted(descend(j) for j in range(i+1,len(p)) if p[j]==i))+')'
 return descend(0)
def weights(a):
 ids=[i for i in range(9) if i!=a];out=[]
 for t in product((0,7,10),repeat=8):
  if sum(t)!=27 or t.count(10)!=2 or t.count(7)!=1:continue
  w=[0]*9;w[a]=9
  for i,v in zip(ids,t):w[i]=v
  out.append(w)
 out.sort(key=lambda w:(tuple(i for i,v in enumerate(w) if v==10),w.index(7)))
 assert len(out)==168 and len(set(map(tuple,out)))==168
 return out
W=[weights(a) for a in range(9)]
def scalar_matrix(p,g,mu,w,offset,sign):
 # Expand 2(g.x)(w.x)+18 sum mu_i(x_i^2-x_i*x_parent)
 # +18 sign sum_{i<=j} offset_ij*x_i*x_j - sum x_i^2.
 coeff={}
 def add(i,j,v):
  key=(min(i,j),max(i,j));coeff[key]=coeff.get(key,0)+v
 for i in range(9):
  for j in range(9):add(i,j,2*g[i]*w[j])
 for i,v in enumerate(mu,1):add(i,i,18*v);add(i,p[i],-18*v)
 k=0
 for i in range(9):
  add(i,i,-1)
  for j in range(i,9):add(i,j,18*sign*offset[k]);k+=1
 out=[[0]*9 for _ in range(9)]
 for (i,j),v in coeff.items():
  if i==j:out[i][i]=v
  else:assert v%2==0;out[i][j]=out[j][i]=v//2
 return out

def bareiss(a):
 b=[r[:] for r in a];previous=1;minors=[]
 for k in range(9):
  pivot=b[k][k];assert pivot>0;minors.append(pivot)
  for i in range(k+1,9):
   for j in range(k+1,9):
    z=pivot*b[i][j]-b[i][k]*b[k][j]
    assert z%previous==0;b[i][j]=z//previous
  previous=pivot
 return minors

def fraction_ldl(a,minors):
 lower=[[F(int(i==j)) for j in range(9)] for i in range(9)];diag=[];prod=F(1)
 for k in range(9):
  pivot=F(a[k][k])-sum(lower[k][j]**2*diag[j] for j in range(k))
  assert pivot>0;diag.append(pivot);prod*=pivot;assert prod==minors[k]
  for i in range(k+1,9):
   lower[i][k]=(F(a[i][k])-sum(lower[i][j]*lower[k][j]*diag[j] for j in range(k)))/pivot
 return diag

if __name__=='__main__':
 levels=multisets();counts=[len(levels[n]) for n in range(1,10)]
 assert counts==[1,1,2,4,9,20,48,115,286]
 arrays={(0,)+p for p in product(*(range(i) for i in range(1,9)))}
 assert len(arrays)==40320
 codes={array_code(p) for p in arrays};assert codes==set(levels[9])
 tt=sorted(parse(s) for s in codes);assert {i:tt[i] for i in REST}==REST
 print('TWO_INDEPENDENT_TREE_ENUMERATIONS_PASS',counts,40320,flush=True)
 raw=Path(sys.argv[1] if len(sys.argv)>1 else 'cap9_new.json').read_bytes();data=json.loads(raw)
 assert raw==serial(data) and data['tag']=='NOVA24_CAP9_NEW_281_V1'
 assert data['specification_parent']=='asg_6qT-ogbqQKnPgSL8OYGdvVHm'
 assert data['specification_sha256']=='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36'
 assert data['remaining']==sorted(REST)
 rec=data['records'];assert [r['ordinal'] for r in rec]==[i for i in range(286) if i not in REST]
 streams=[hashlib.sha256() for _ in range(3)];nm=0;nr=0;freeints=0;multints=0
 for r in rec:
  o=r['ordinal'];p=tt[o];assert r['parent']==list(p)
  rows=[0,1] if o in R01 else [0,2] if o in R02 else [0];assert r['rows']==rows
  g=r['g'];mus=r['mu'];assert len(g)==(63 if len(rows)==2 else 9) and len(mus)==168*len(rows)
  assert all(type(v) is int for v in g)
  assert all(len(u)==8 and all(type(v) is int and v>=0 for v in u) for u in mus)
  freeints+=len(g);multints+=sum(map(len,mus));offset=g[18:] if len(rows)==2 else [0]*45
  for ri,a in enumerate(rows):
   for wi,w in enumerate(W[a]):
    mat=scalar_matrix(p,g[9*ri:9*ri+9],mus[168*ri+wi],w,offset,1 if ri==0 else -1)
    minors=bareiss(mat);fraction_ldl(mat,minors)
    for h,obj in zip(streams,([o,a,wi,w],[o,a,wi,mat],[o,a,wi,minors])):h.update(serial(obj))
    nm+=1
  nr+=len(rows)
  if o%25==0:print('EXACT_CAP9_TREE_PASS',o,len(mus),flush=True)
 assert nm==51912 and nr==309 and freeints==4041 and multints==415296
 report=dict(tag='NOVA24_CAP9_NEW_EXACT_VERIFICATION_V1',trees=286,excluded=281,remaining=sorted(REST),remaining_parents=[REST[i] for i in sorted(REST)],row_count=nr,extremes_per_row=168,matrices=nm,leading_minors=9*nm,free_integers=freeints,multiplier_integers=multints,coefficient_bytes=len(raw),coefficient_sha256=hashlib.sha256(raw).hexdigest(),tree_sha256=hashlib.sha256(serial(tt)).hexdigest(),streams=dict(zip(('weights','shifted_matrices','leading_minors'),(h.hexdigest() for h in streams))))
 b=serial(report);Path('cap9_checked.json').write_bytes(b)
 print('ALL_CAP_EXTREME_ROWS_EXACTLY_COVERED_PASS',nr,nm)
 print('INDEPENDENT_SCALAR_BAREISS_FRACTION_LDL_PASS',nm,9*nm)
 print('NEW_281_OF_286_UNIVERSAL_CAP9_THEOREM_PASS',sorted(REST))
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
 print('NO_F10_V10_C34_OR_WHOLE_C32_TYPE_ASSERTION')
