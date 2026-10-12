# material-d2fe3ab67865

AI research material

---

"""CENTERED_CIRCUIT_RANK3_V1: exact controls, not a finite proof of the theorem.
Standard library only. Run python -S centered_rank3_audit.py, then --verify.
All inputs and nondefault choices are literal below. Fractions are exact.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent

def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def transpose(a):return list(map(list,zip(*a)))
def multiply(a,b):return[[dot(r,c) for c in transpose(b)] for r in a]
def mv(a,v):return[dot(r,v) for r in a]
def gram(x):return multiply(x,transpose(x))
def rank(a):
 a=[[F(v) for v in r] for r in a];p=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(p,len(a)) if a[k][j]),None)
  if k is None:continue
  a[p],a[k]=a[k],a[p];s=a[p][j];a[p]=[v/s for v in a[p]]
  for k in range(len(a)):
   if k!=p:
    s=a[k][j];a[k]=[v-s*w for v,w in zip(a[k],a[p])]
  p+=1
  if p==len(a):break
 return p

def determinant(a):
 a=[[F(v) for v in r] for r in a];z=F(1)
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]),None)
  if k is None:return F(0)
  if k!=j:a[k],a[j]=a[j],a[k];z=-z
  p=a[j][j];z*=p
  for k in range(j+1,len(a)):
   q=a[k][j]/p
   for i in range(j+1,len(a)):a[k][i]-=q*a[j][i]
 return z

def inverse(a):
 n=len(a);a=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
  s=a[j][j];a[j]=[v/s for v in a[j]]
  for k in range(n):
   if k!=j:
    s=a[k][j];a[k]=[v-s*w for v,w in zip(a[k],a[j])]
 return[row[n:] for row in a]

def determinants(x):
 return{t:determinant([[x[i][j]-x[t[0]][j] for j in range(3)] for i in t[1:]])
        for t in combinations(range(len(x)),4)}
def circuits(d,n,sets=None):
 ans=[]
 for s in combinations(range(n),5) if sets is None else sets:
  c=[(-1)**j*d[s[:j]+s[j+1:]] for j in range(5)]
  z=[F(0)]*n;m=[F(0)]*n
  for j,a in enumerate(s):
   z[a]=c[j]
   for i in s:
    if i!=a:m[i]+=c[j]
  ans.append((s,sum(c),z,m))
 return ans

def verify_moments(g,d,sets=None):
 cs=circuits(d,len(g),sets)
 badv=sum(v!=0 for s,v,z,m in cs)
 badm=sum(any(mv(g,m)) for s,v,z,m in cs)
 return badv,badm

def anchor_matrix(g,a):
 n=len(g);t=[[F(i==a[j])-F(i==a[0]) for j in range(1,4)] for i in range(n)]
 return t,multiply(transpose(t),multiply(g,t))

def kernel_frame(g,d,b,a):
 n=len(g);rows=[]
 assert d[a] and sum(b)
 for j in range(n):
  if j in a:continue
  s=tuple(sorted(a+(j,)));cs=circuits(d,n,[s]);_,v,z,m=cs[0]
  assert v==0 and not any(mv(g,m)) and not any(mv(g,z))
  assert z[j]
  z=[v/z[j] for v in z]
  assert sum(z)==0 and all(z[k]==(k==j) for k in range(n) if k not in a)
  rows.append(z)
 rows.append(b)
 assert not any(mv(g,b)) and rank(rows)==n-3
 return rows

def centered(xs):
 n=len(xs);means=[sum(F(x[j]) for x in xs)/n for j in range(len(xs[0]))]
 return[[F(v)-means[j] for j,v in enumerate(x)] for x in xs]

def main():
 x=[list(map(F,q)) for q in product((-1,1),repeat=3)];n=len(x)
 faces=[[0,1,3,2],[4,6,7,5],[0,4,5,1],[2,3,7,6],[0,2,6,4],[1,5,7,3]]
 q=[[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
 edges=sorted({tuple(sorted((a,b))) for cy in faces for a,b in zip(cy,cy[1:]+cy[:1])})
 g=gram(x);d0=determinants(x);reference={}
 for cy in faces:
  if 0 in cy:continue
  for j in range(1,len(cy)-1):reference[tuple(sorted((0,cy[0],cy[j],cy[j+1])))]=1
 # Convex actual facet-apex cells and coherent determinant signs.
 epsilon={};flats=set()
 for cy in faces:
  flats.update(combinations(sorted(cy),4))
  for tri in combinations(range(len(cy)),3):
   for a in range(n):
    if a in cy:continue
    seq=(a,)+tuple(cy[i] for i in tri);t=tuple(sorted(seq))
    e=(-1)**sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))
    assert e*d0[t]>0
    if t in epsilon:assert epsilon[t]==e
    epsilon[t]=e
 assert len(epsilon)==56 and len(flats)==6 and all(d0[t]==0 for t in flats)
 total=sum(epsilon[t]*d0[t] for t in reference);assert total==48
 d={t:v/total for t,v in d0.items()};b=[F(0)]*n
 for t in reference:
  for i in t:b[i]+=epsilon[t]*d[t]
 assert sum(b)==4 and not any(mv(g,b))
 assert verify_moments(g,d)==(0,0)
 a=(0,1,2,4);frame=kernel_frame(g,d,b,a);t,k=anchor_matrix(g,a)
 leading=[determinant([row[:j] for row in k[:j]]) for j in (1,2,3)]
 assert leading==[4,16,64] and rank(g)==3
 # Check every second moment without taking it as a premise.
 quadratic_checks=0
 for s in combinations(range(n),5):
  z=[[F(0)]*3 for _ in range(3)]
  for j in range(5):
   cell=s[:j]+s[j+1:];coef=(-1)**j*d[cell]
   u=[sum(x[i][a] for i in cell) for a in range(3)]
   for a0 in range(3):
    for a1 in range(3):
     z[a0][a1]+=coef*(u[a0]*u[a1]+sum(x[i][a0]*x[i][a1] for i in cell))
  assert not any(v for row in z for v in row);quadratic_checks+=9
 # Same-span polar coordinates, support incidences and all strict features.
 h=multiply(transpose(x),t);u=multiply(inverse(h),transpose(q))
 B=multiply(multiply(g,t),u);J=multiply(transpose(u),multiply(k,u))
 assert B==multiply(x,transpose(q)) and J==gram(q)
 assert all(B[v][f]==1 if v in cy else B[v][f]<1 for f,cy in enumerate(faces) for v in range(n))
 stable=[f for f in range(6) if all(J[f][j]<J[f][f] for j in range(6) if j!=f)]
 unstable=[i for i in range(n) if all(g[i][j]<g[i][i] for j in range(n) if tuple(sorted((i,j))) in edges)]
 saddles=[]
 for i,j in edges:
  fs=[f for f,cy in enumerate(faces) if i in cy and j in cy];assert len(fs)==2
  f,hf=fs;A=g[i][i]-g[i][j];C=g[j][j]-g[i][j]
  if A>0 and C>0 and J[f][f]>J[f][hf] and J[hf][hf]>J[f][hf]:saddles.append((i,j))
 assert (len(stable),len(unstable),len(saddles))==(6,8,12)
 # Centering is necessary for rank<=3, even when all moments hold.
 g4=gram([[F(1)]+r for r in x]);assert rank(g4)==4
 assert verify_moments(g4,d)==(0,0) and any(mv(g4,b))
 # Noncollapse is necessary; rank1 projections obey all equalities.
 g1=gram([[r[0]] for r in x]);assert rank(g1)==1
 assert verify_moments(g1,d)==(0,0) and not any(mv(g1,b))
 assert determinant(anchor_matrix(g1,(0,1,2,4))[1])==0
 # Without a positive anchor, symmetry+rank3 allow indefinite matrices.
 signx=[[r[0],r[1],-r[2]] for r in x];gi=multiply(x,transpose(signx))
 assert rank(gi)==3 and verify_moments(gi,d)==(0,0) and not any(mv(gi,b))
 assert determinant(anchor_matrix(gi,(0,1,2,4))[1])<0
 # Volume and centering without first moments allow rank4.
 y=[[F(i==j) for j in range(4)] for i in range(4)]+[[-F(1)]*4]
 gy=gram(y);dy=determinants([r[:3] for r in y]);by=[F(1)]*5
 assert rank(gy)==4 and not any(mv(gy,by))
 assert verify_moments(gy,dy)==(0,1)
 # Anchor-only circuits do not determine the other determinant coordinates.
 z=centered([[i,i*i,i*i*i] for i in range(6)]);gz=gram(z);dz=determinants(z)
 az=(0,1,2,3);dz[(0,1,4,5)]+=1
 anchor_sets=[(0,1,2,3,4),(0,1,2,3,5)]
 assert verify_moments(gz,dz,anchor_sets)==(0,0)
 assert verify_moments(gz,dz)!=(0,0)
 out={'identity':'CENTERED_CIRCUIT_RANK3_EXACT_AUDIT_V1','cube':{
  'vertices':8,'true_edges':12,'true_facets':6,'full_determinants':len(d),
  'five_sets':len(list(combinations(range(n),5))),'positive_supported_cells':56,
  'cofacial_flat_cells':6,'reference_cells':len(reference),'normalized_mass':1,
  'gram_rank':rank(g),'kernel_frame_rank':rank(frame),'anchor':[0,1,2,4],
  'anchor_leading_minors':list(map(str,leading)),'quadratic_equalities_checked':quadratic_checks,
  'equilibria_S_U_H':[6,8,12]},'controls':{
  'without_centering_rank4_all_moments':True,'rank1_projection_all_equalities':True,
  'indefinite_rank3_without_positive_anchor':True,
  'rank4_volume_and_centering_without_first_moments':True,
  'anchor_only_insufficient_for_full_D_recovery':True},
  'scope':'exact controls; universal claims follow from the separate analytic proof'}
 data=enc(out);p=HERE/'centered_rank3_audit.json'
 if sys.argv[1:]==['--verify']:assert p.read_bytes()==data
 else:assert not sys.argv[1:];p.write_bytes(data)
 print('CENTERED_CIRCUIT_RANK3_EXACT_AUDIT_PASS 8 70 56 3 5 504 5',*pin(data))
if __name__=='__main__':main()
