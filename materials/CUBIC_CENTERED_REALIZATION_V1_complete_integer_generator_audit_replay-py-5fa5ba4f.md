# material-5fa5ba4f10c4

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""CUBIC_CENTERED_REALIZATION_V1. Complete integer polynomial systems.
Requires the three exact source/input materials pinned below for native55.
Standard-library commands:
  python -S cubic_realization.py audit
  python -S cubic_realization.py verify
  python -S cubic_realization.py census
  python -S cubic_realization.py case INDEX
  python -S cubic_realization.py case INDEX ROOT
ROOT optionally adds NECESSARY weak primal-path and polar-tree escapes only.
It does NOT add the full pole-arrow graph or H=0, and is not exact110 mechanics.
Monomial [coefficient,[variable IDs]] means coefficient times their product;
repeated IDs are powers. Every equality is polynomial=0; strict inequalities
are polynomial>0; optional weak inequalities are polynomial>=0.
"""
from pathlib import Path
from itertools import combinations,permutations
from fractions import Fraction as F
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
PINS={
'flip_moments.py':[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7'],
'native55.txt':[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e'],
'affine_moments.py':[5980,'fa8371daf690ac9ff0a9a61b3ad8e8ca2dc6652b2a0f76cc70826163fff01805']}
def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
def add(*rows):
 out={}
 for row in rows:
  for m,c in row.items():out[m]=out.get(m,0)+c
 return{m:c for m,c in out.items() if c}
def scale(row,s):return{m:s*c for m,c in row.items() if s*c}
def mul(a,b):
 out={}
 for m,c in a.items():
  for n,d in b.items():
   k=tuple(sorted(m+n));out[k]=out.get(k,0)+c*d
 return{m:c for m,c in out.items() if c}
def const(c):return{():c} if c else{}
def parity(p):return(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def det(a):
 terms=[]
 for p in permutations(range(len(a))):
  v=const(parity(p))
  for i,j in enumerate(p):v=mul(v,a[i][j])
  terms.append(v)
 return add(*terms)
def packed(p):return[[c,list(m)] for m,c in sorted(p.items())]
def evaluate(p,x):
 total=F(0)
 for c,m in p:
  v=F(c)
  for i in m:v*=x[i]
  total+=v
 return total

def make(n,faces,reference,epsilon,anchor=None,root=None):
 """Input vertices use one consistent index set0..n-1; cycles are coherent.
 reference maps sorted4-tuples to integer multiplicities; epsilon is coherent.
 """
 nf=len(faces);four=list(combinations(range(n),4));names=[]
 def variable(name):
  j=len(names);names.append(name);return{(j,):1}
 # Row-major upper-triangle order, including diagonals.
 G={(i,j):variable(['G',i,j]) for i in range(n) for j in range(i,n)}
 D={t:variable(['D',*t]) for t in four}
 U=[[variable(['u',f,k]) for k in range(3)] for f in range(nf)]
 def g(i,j):return G[tuple(sorted((i,j)))]
 a=tuple(anchor) if anchor is not None else min(epsilon)
 assert len(set(a))==4 and len(faces)>=4
 K=[[add(g(a[i],a[j]),scale(g(a[0],a[j]),-1),scale(g(a[i],a[0]),-1),g(a[0],a[0]))
      for j in range(1,4)] for i in range(1,4)]
 equations=[];strict=[];weak=[]
 def eq(label,p):equations.append([label,packed(p)])
 def gt(label,p):strict.append([label,packed(p)])
 def ge(label,p):weak.append([label,packed(p)])
 # Anchor0 boundaries span all five-simplex boundary coefficient rows.
 for q in combinations(range(1,n),4):
  s=(0,)+q;c=[scale(D[s[:j]+s[j+1:]],(-1)**j) for j in range(5)]
  eq(['volume',*s],add(*c))
  # Given volume=0, m_S=-z_S; use Gz=0 for the shorter polynomial.
  for i in range(n):eq(['first',*s,i],add(*(mul(g(i,j),v) for j,v in zip(s,c))))
 b=[{} for i in range(n)];N={}
 for t,multiplicity in sorted(reference.items()):
  w=scale(D[t],multiplicity*epsilon[t]);N=add(N,w)
  for i in t:b[i]=add(b[i],w)
 eq(['normalization'],add(N,const(-1)))
 for i in range(n):eq(['centroid',i],add(*(mul(g(i,j),b[j]) for j in range(n))))
 for k in (1,2,3):gt(['anchor_minor',k],det([r[:k] for r in K[:k]]))
 for v in range(n):
  for f,cy in enumerate(faces):
   B=add(*(mul(add(g(v,a[k+1]),scale(g(v,a[0]),-1)),U[f][k]) for k in range(3)))
   if v in cy:eq(['incidence',v,f],add(B,const(-1)))
   else:gt(['nonincidence',v,f],add(const(1),scale(B,-1)))
 def j(f,h):return add(*(mul(mul(U[f][k],K[k][l]),U[h][l]) for k in range(3) for l in range(3)))
 if root is not None:
  assert n==10 and nf==9 and 1<=root<=8
  edges={tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])}
  assert all((i,i+1) in edges for i in range(9))
  for i in range(10):
   if i!=root:
    p=i+1 if i<root else i-1;ge(['weak_primal_path',i,p],add(g(i,p),scale(g(i,i),-1)))
  parent=[0,0,1,2,3,4,5,0,7]
  for f in range(1,9):
   p=parent[f];assert len(set(faces[f])&set(faces[p]))==2
   ge(['weak_polar_tree',f,p],add(j(f,p),scale(j(f,f),-1)))
 allp=[p for group in (equations,strict,weak) for label,p in group]
 degree=max(len(m) for p in allp for c,m in p)
 assert degree<=3
 return{'identity':'CUBIC_CENTERED_REALIZATION_V1','vertices':n,'facets':faces,
   'anchor':list(a),'reference':[[list(t),m,epsilon[t]] for t,m in sorted(reference.items())],
   'variables':names,'equations':equations,'strict_positive':strict,'weak_nonnegative':weak,
   'maximum_degree':degree,'no_explicit_constraints':['PSD_G','rank_G','cofacial_D_zeros','positive_cell_D'],
   'physical_scope':'full fixed-incidence own-volume-centroid realization',
   'mechanical_scope':'necessary weak trees only; not full pole graph or H=0' if root is not None else'none'}

def native(i,root=None):
 for name,p in PINS.items():assert pin((HERE/name).read_bytes())==p,name
 import affine_moments as am
 fm=am.fm;d=am.system(fm.inputs()[i]);eps={tuple(t):s for t,s in d['affine_metadata']['epsilon']}
 out=make(10,d['affine_metadata']['oriented_faces'],d['reference'],eps,root=root)
 out['native_index']=i;out['source_pins']=PINS;out['path_position_to_native_vertex']=d['path']
 assert len(out['variables'])==292 and len(out['equations'])==1431 and len(out['strict_positive'])==59
 assert len(out['weak_nonnegative'])==(0 if root is None else 17)
 return out

def audit():
 # Same literal physical cube as in the separate exact rank audit; no import.
 x=[tuple(map(F,p)) for p in __import__('itertools').product((-1,1),repeat=3)]
 faces=[[0,1,3,2],[4,6,7,5],[0,4,5,1],[2,3,7,6],[0,2,6,4],[1,5,7,3]]
 q=[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
 def determinant(a):
  return sum((parity(p)*a[0][p[0]]*a[1][p[1]]*a[2][p[2]] for p in permutations(range(3))),F(0))
 D={t:determinant([[x[i][j]-x[t[0]][j] for j in range(3)] for i in t[1:]]) for t in combinations(range(8),4)}
 epsilon={};reference={}
 for cy in faces:
  for tri in combinations(range(len(cy)),3):
   for a in range(8):
    if a not in cy:
     seq=(a,)+tuple(cy[k] for k in tri);t=tuple(sorted(seq));e=parity(seq)
     if t in epsilon:assert epsilon[t]==e
     epsilon[t]=e;assert e*D[t]>0
  if 0 not in cy:
   for k in range(1,len(cy)-1):reference[tuple(sorted((0,cy[0],cy[k],cy[k+1])))]=1
 norm=sum(epsilon[t]*D[t] for t in reference);assert norm==48
 out=make(8,faces,reference,epsilon,anchor=(0,1,2,4));values=[]
 for label in out['variables']:
  if label[0]=='G':_,i,j=label;values.append(sum(a*b for a,b in zip(x[i],x[j])))
  elif label[0]=='D':values.append(D[tuple(label[1:])]/norm)
  else:
   _,f,k=label;values.append(F(q[f][2-k],2))
 assert all(evaluate(p,values)==0 for label,p in out['equations'])
 assert all(evaluate(p,values)>0 for label,p in out['strict_positive'])
 # The same source also constructs the path/pole necessary inequalities.
 s=native(43,4)
 assert len(s['weak_nonnegative'])==17
 r={'identity':'CUBIC_CENTERED_REALIZATION_EXACT_AUDIT_V1','cube':{
   'variables':len(values),'equations':len(out['equations']),'strict_inequalities':len(out['strict_positive']),
   'all_equations_exact_zero':True,'all_strict_inequalities_exact_positive':True,
   'system_pin':pin(enc(out))},'native43_root4':{
   'variables':len(s['variables']),'equations':len(s['equations']),
   'strict_inequalities':len(s['strict_positive']),'weak_tree_inequalities':len(s['weak_nonnegative']),
   'system_pin':pin(enc(s))},'maximum_degree':3,
   'scope':'actual cube substitution and finite system construction; not feasibility or exclusion of native43'}
 b=enc(r);(HERE/'cubic_realization_audit.json').write_bytes(b)
 print('CUBIC_CENTERED_REALIZATION_EXACT_AUDIT_PASS',*pin(b))
 return r

def census():
 rows=[]
 for i in range(55):
  out=native(i);b=enc(out)
  rows.append({'native_index':i,'anchor':out['anchor'],'system_pin':pin(b)})
 report={'identity':'CUBIC_CENTERED_REALIZATION_NATIVE55_CENSUS_V1','source_pins':PINS,
  'variables_per_row':292,'equations_per_row':1431,'strict_inequalities_per_row':59,
  'maximum_degree':3,'rows':rows,'scope':'complete system construction; zero new geometric exclusions'}
 b=enc(report);(HERE/'cubic_realization_census.json').write_bytes(b)
 print('CUBIC_CENTERED_REALIZATION_NATIVE55_CENSUS_PASS 55 292 1431 59 3',*pin(b))
if __name__=='__main__':
 if sys.argv[1:]==['audit']:audit()
 elif sys.argv[1:]==['census']:census()
 elif sys.argv[1:]==['verify']:
  audit();census()
  b=enc(native(43,4));(HERE/'cubic_realization_43_4.json').write_bytes(b)
  expected={
   'cubic_realization_audit.json':[610,'a66bf39dbf8a2024c3944e088b28a23b45a972c939329259997021bb8f5ff1f6'],
   'cubic_realization_census.json':[7563,'8f4f74a474f9d7301cd7461d2cb063fbc40aa28025000ee95b890c4002057d04'],
   'cubic_realization_43_4.json':[151770,'bc5203021cf50d362e639e20f587ce2c9e0a0894df05df0d36a8bd1a10d73132']}
  for name,p in expected.items():assert pin((HERE/name).read_bytes())==p,name
  print('CUBIC_CENTERED_REALIZATION_FROZEN_REPLAY_PASS 3')
 elif len(sys.argv) in (3,4) and sys.argv[1]=='case':
  i=int(sys.argv[2]);r=int(sys.argv[3]) if len(sys.argv)==4 else None
  out=native(i,r);b=enc(out);p=HERE/f'cubic_realization_{i}_{r}.json';p.write_bytes(b)
  print('CUBIC_CENTERED_REALIZATION_SYSTEM_WRITTEN',p.name,*pin(b))
 else:raise ValueError('audit | census | verify | case INDEX [ROOT]')
