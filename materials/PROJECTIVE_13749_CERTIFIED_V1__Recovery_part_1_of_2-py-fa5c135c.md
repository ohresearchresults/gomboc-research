# material-fa5c135c09db

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
from math import comb
import hashlib, json, sys
assert __debug__
PARENT=('minimum-0072',
 '30637df80e99ee64340d83d17e4876e9e873313d20cd83efa2d97f9d1103eba7')
TREE=[0,0,1,2,3,4,0,6,7,8]
WEIGHTS=[9,4,1,38,22,8,4,1,15]
RAYS=[[0,0,1,0],[0,15,15,7],[0,1,0,0],
 [15,0,90,14],[15,90,0,14],[45,0,60,28],
 [45,60,0,28],[1,0,0,0],[15,0,0,7]]
CENTER=[44,41,41,21]
FACES=[[0,2,1],[0,3,5,8,7],[2,7,8,6,4],[0,7,2],
 [0,1,3],[1,5,3],[1,8,5],[1,6,8],[1,4,6],[1,2,4]]
TRIANGLES=[[f[0],f[j],f[j+1]]
 for f in FACES for j in range(1,len(f)-1)]
Z=[(F(1,2),0),(F(3,4),F(1,8)),(F(3,4),F(1,4)),
   (F(1,4),F(3,4)),(F(1,8),F(3,4)),(0,F(1,2))]
I=[[F(i==j) for j in range(3)] for i in range(3)]

def enc(x):
 return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def prod(xs):
 a=1
 for x in xs:a*=x
 return a
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def det(A):
 n=len(A)
 return sum(((-1)**sum(p[i]>p[j] for i in range(n)
                      for j in range(i+1,n))*
             prod(A[i][p[i]] for i in range(n))
             for p in permutations(range(n))),F(0))
def inverse(A):
 n=len(A)
 T=[list(map(F,r))+[F(i==j) for j in range(n)]
    for i,r in enumerate(A)]
 for j in range(n):
  p=next(i for i in range(j,n) if T[i][j])
  T[j],T[p]=T[p],T[j]
  z=T[j][j];T[j]=[x/z for x in T[j]]
  for i in range(n):
   if i!=j:
    z=T[i][j];T[i]=[x-z*y for x,y in zip(T[i],T[j])]
 return [r[n:] for r in T]
def mv(A,v):return [dot(r,v) for r in A]
def cross(a,b):
 return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
         a[0]*b[1]-a[1]*b[0]]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def six(A):return [A[0][0],A[0][1],A[0][2],A[1][1],A[1][2],A[2][2]]
def matrix(v):
 a,b,c,d,e,f=v
 return [[a,b,c],[b,d,e],[c,e,f]]
def psd(v):
 a,b,c,d,e,f=v
 p=[a,d,f,a*d-b*b,a*f-c*c,d*f-e*e,
    a*(d*f-e*e)-b*(b*f-e*c)+c*(b*e-d*c)]
 assert min(p)>=0
 # Separate rational Schur-pivot acceptance, independent of the minors.
 S=[[F(x) for x in r] for r in matrix(v)];rank=0
 while S:
  j=next((j for j in range(len(S)) if S[j][j]>0),None)
  if j is None:
   assert all(x==0 for r in S for x in r)
   break
  if j:
   S[0],S[j]=S[j],S[0]
   for r in S:r[0],r[j]=r[j],r[0]
  q=S[0][0];assert q>0
  S=[[S[i][j]-S[i][0]*S[0][j]/q
      for j in range(1,len(S))] for i in range(1,len(S))]
  rank+=1
 return p,rank

def root_check():
 W=[[[4480,-864,-3368],[-864,39168,3384],[-3368,3384,12400]],
    [[11536,3672,-4943],[3672,39168,3384],[-4943,3384,12400]],
    [[4480,2664,-3368],[2664,48240,1809],[-3368,1809,12400]],
    [[4480,-864,160],[-864,39168,7920],[160,7920,9250]]]
 expected=[[F(2580),F(28944),F(3972)],
           [F(16293,2),F(17712),F(822)],
           [F(2130),F(33966),F(9519,2)],
           [F(4184),F(19872),F(4970)]]
 t=[F(1),F(1,4),F(1,2)]
 k=[F(1,4)]*3
 centers=[k]+[[k[j]+F(7,32)*(i==j) for j in range(3)]
              for i in range(3)]
 p=[F(1,9),F(10,9),F(0)];r=[F(1,9),F(0),F(10,9)]
 def sym(a,b):return [[(a[i]*b[j]+b[i]*a[j])/2
                      for j in range(3)] for i in range(3)]
 for c,A,want in zip(centers,W,expected):
  terms=[sym(sub(p,c),sub(I[0],p)),sym(c,I[1]),
         sym(sub(r,c),sub(I[0],r))]
  B=[[-9*terms[0][i][j]+26*terms[1][i][j]-5*terms[2][i][j]
      for j in range(3)] for i in range(3)]
  assert [[2592*x for x in row] for row in B]==A
  gaps=[A[i][i]-sum(abs(A[i][j])*t[j]/t[i]
                    for j in range(3) if j!=i) for i in range(3)]
  assert gaps==want and min(gaps)>=822
  assert psd(six([[F(A[i][j])-F(822)*(i==j)
                   for j in range(3)] for i in range(3)]))[1]>=1
  for v in (p,r):
   z=[2*v[j]-I[0][j]-c[j] for j in range(3)]
   assert dot(z,z)<=F(456689,82944)
 assert 400*456689<2209*82944
 assert F(137,432)-F(47,20)*F(2,15)==F(41,10800)
 print('ROOT_NEIGHBOR_13749_ANALYTIC_CERTIFICATE_PASS')

def parameter_cover():
 cs=[(F(0),[1,0,0]),(F(0),[0,1,0]),
     (F(1),[-1,-1,0]),(F(0),[0,0,1])]
 for y,z in Z:cs.append((7*z,[7*(1-z),7*(y-z),-15*(y+z)]))
 found=set()
 for ids in combinations(range(10),3):
  A=[cs[i][1] for i in ids]
  if not det(A):continue
  x=tuple(mv(inverse(A),[-cs[i][0] for i in ids]))
  if all(c+dot(n,x)>=0 for c,n in cs):found.add(x)
 vertices=[tuple(F(r[j],sum(r[:3])) for j in (0,1,3)) for r in RAYS]
 assert vertices==sorted(found)
 center=tuple(F(CENTER[j],sum(CENTER[:3])) for j in (0,1,3))
 assert center==tuple(sum(v[j] for v in vertices)/9 for j in range(3))
 assert all(c+dot(n,center)>0 for c,n in cs)
 actual={tuple(i for i,x in enumerate(vertices) if c+dot(n,x)==0)
         for c,n in cs}
 assert actual=={tuple(sorted(f)) for f in FACES}
 edges={}
 for f in FACES:
  n=cross(sub(vertices[f[1]],vertices[f[0]]),
          sub(vertices[f[2]],vertices[f[0]]))
  signs=[]
  for a,b in zip(f,f[1:]+f[:1]):
   e=tuple(sorted((a,b)));edges[e]=edges.get(e,0)+1
   for j in f:
    if j not in (a,b):
     signs.append(dot(n,cross(sub(vertices[b],vertices[a]),
                              sub(vertices[j],vertices[a]))))
  assert min(signs)>0 or max(signs)<0
 assert len(edges)==17 and set(edges.values())=={2}
 assert len(TRIANGLES)==14
 for t in TRIANGLES:assert det([CENTER]+[RAYS[i] for i in t])!=0

def model(pp,unit,absolute=False):
 A,B,C,w=pp;z=0*unit
 LL={1:2*A+B-w,2:8*A+6*B+C-7*w,3:4*A+3*B+C-4*w,
     8:4*A+B+3*C-4*w,7:8*A+B+6*C-7*w,6:2*A+C-w}
 V={0:[unit,z,z],4:[z,unit,z],5:[z,z,z],9:[z,z,unit],
    1:[2*A,B,z],2:[8*A,6*B,C],3:[4*A,3*B,C],
    8:[4*A,B,3*C],7:[8*A,B,6*C],6:[2*A,z,C]}
 ids=[1,2,3,6,7,8];cache={}
 def factors(power,drop=()):
  key=tuple(power-drop.count(i) for i in ids);assert min(key)>=0
  if key not in cache:
   p=unit
   for i,k in zip(ids,key):
    for _ in range(k):p*=LL[i]
   cache[key]=p
  return cache[key]
 R=factors(1);FF=factors(2);DD=R;NN=[FF,FF,FF]
 cells=[([0,4,2,1],w*C,(1,2)),([0,4,3,2],3*w*C,(2,3)),
        ([0,3,4,9],4*w,(3,)),([0,3,9,8],8*w*B,(3,8)),
        ([0,6,7,9],w*B,(6,7)),([0,7,8,9],3*w*B,(7,8))]
 for labels,mu,den in cells:
  DD+=mu*factors(1,den)
  for i in labels:
   fac=mu*factors(2,den+((i,) if i in LL else ()))
   NN=[x+fac*y for x,y in zip(NN,V[i])]
 UU=[[z]*3 for _ in range(3)];E=[z]*3
 sign=1 if absolute else -1
 for i,ww in enumerate(WEIGHTS,1):
  j=TREE[i];di=(i,) if i in LL else ();dj=(j,) if j in LL else ()
  cr=factors(2,di+dj);sq=factors(2,di+di)
  e=[factors(1,dj)*V[j][k]+sign*factors(1,di)*V[i][k]
     for k in range(3)]
  E=[a+ww*b for a,b in zip(E,e)]
  for a in range(3):
   for b in range(3):
    UU[a][b]+=ww*(2*sq*V[i][a]*V[i][b]
                 +sign*cr*(V[i][a]*V[j][b]+V[j][a]*V[i][b]))
 out=[4*DD*UU[a][b]+NN[a]*E[b]+E[a]*NN[b]
      +sign*(FF*DD if a==b else z)
      for a,b in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))]
 return out,8*FF*DD,LL

def audit_identity(cone,coefficients):
 rays=[CENTER]+[RAYS[i] for i in TRIANGLES[cone]]
 pad=1 if cone==8 else 2 if cone==13 else None
 degree=18 if pad is None else 20
 p=[sum(r[j] for r in rays) for j in range(4)]
 bound,_,_=model(p,1,True)
 if pad is not None:bound=[x*(p[0]+p[pad])**2 for x in bound]
 assert all(sum(k)==degree for k in coefficients)
 assert all(abs(v[i])<=bound[i] for v in coefficients.values() for i in range(6))
 bits=(4*max(bound)).bit_length();radix=degree+1
 lam=[1,1<<bits,1<<(bits*radix),1<<(bits*radix*radix)]
 p=[sum(r[j]*x for r,x in zip(rays,lam)) for j in range(4)]
 want,_,_=model(p,1)
 if pad is not None:want=[x*(p[0]+p[pad])**2 for x in want]
 got=[0]*6
 for k,v in coefficients.items():
  shift=bits*(k[1]+radix*k[2]+radix*radix*k[3])
  got=[x+(y<<shift) for x,y in zip(got,v)]
 assert got==want
 return degree

def projective_check():
 import sympy as S
 assert S.__version__=='1.14.0'
 parameter_cover()
 xx=S.symbols('l:4');unit=S.Poly(1,*xx,domain=S.ZZ)
 count=0;pdcount=0;missing=0;minor_hash=hashlib.sha256()
 path=Path('projective13749_candidate.jsonl')
 with path.open('wb') as stream:
  for cone,tri in enumerate(TRIANGLES):
   rays=[CENTER]+[RAYS[i] for i in tri]
   pp=[S.Poly(sum(r[j]*x for r,x in zip(rays,xx)),*xx,domain=S.ZZ)
       for j in range(4)]
   out,den,LL=model(pp,unit)
   assert all(min(p.as_dict().values())>=0 for p in LL.values())
   pad=1 if cone==8 else 2 if cone==13 else None
   if pad is not None:out=[p*(pp[0]+pp[pad])**2 for p in out]
   tables=[p.as_dict() for p in out]
   keys=sorted(set().union(*(set(t) for t in tables)))
   co={k:[int(t.get(k,0)) for t in tables] for k in keys}
   co={k:v for k,v in co.items() if any(v)}
   degree=audit_identity(cone,co)
   for k,v in sorted(co.items()):
    minors,rank=psd(v)
    count+=1;pdcount+=rank==3
    stream.write(enc([cone,list(k),v]))
    minor_hash.update(enc([cone,list(k),minors,rank]))
   assert psd(co[(degree,0,0,0)])[1]==3
   missing+=comb(degree+3,3)-len(co)
   print('EXACT_CONE_PASS',cone,len(co),degree,flush=True)
 assert count==19332 and missing==170
 report={'parent':PARENT,'literal_index':13749,'tree':TREE,
         'weights':WEIGHTS,'shift':'1/8','coefficient_count':count,
         'pd_count':pdcount,'zero_count':missing,
         'coefficient_pin':pin(path.read_bytes()),
         'minor_stream_sha256':minor_hash.hexdigest()}
 raw=enc(report);Path('projective13749_candidate_report.json').write_bytes(raw)
 print('SOURCE_PIN',pin(Path(__file__).read_bytes()))
 print('REPORT_PIN',pin(raw))
 print('COEFFICIENT_PIN',report['coefficient_pin'])
 print('PROJECTIVE_13749_CANDIDATE_EXACT_ACCEPTANCE_PASS')

if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'root'
 assert mode in ('root','projective')
 root_check()
 if mode=='projective':projective_check()
