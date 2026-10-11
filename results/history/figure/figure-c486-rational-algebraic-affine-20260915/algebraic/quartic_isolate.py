"""Exact Sturm isolation and visibility classification of the mass quartic.
Only accepts the nonsingular case gcd(p,det(L+tI))=1; otherwise stops.
Usage: python -B -S quartic_isolate.py mass_chamber.json C592_A.json OUTPUT.json
"""
import hashlib,json,sys
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import mass_chamber as mc
assert __debug__
sys.set_int_max_str_digits(0)
EPS=Q(1,10**30)
GRID=10**18

def clean(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 g=gcd(*a)
 return [v//g for v in a] if g else [0]

def remainder(a,b):
 a=clean(a);b=clean(b);assert b!=[0]
 while a!=[0] and len(a)>=len(b):
  n=len(a)-len(b);v=a[-1];w=b[-1];s=1 if w>0 else -1
  a=[abs(w)*x for x in a]
  for i,x in enumerate(b):a[n+i]-=s*v*x
  a=clean(a)
 return a

def pgcd(a,b):
 while b!=[0]:a,b=b,remainder(a,b)
 return clean(a)

def sturm(p):
 seq=[clean(p),clean([i*p[i] for i in range(1,len(p))])]
 while seq[-1]!=[0]:
  r=remainder(seq[-2],seq[-1])
  if r==[0]:break
  seq.append([-x for x in r])
 return seq

def sign_at(p,x):
 n,d=x.numerator,x.denominator;v=p[-1];power=d
 for c in p[-2::-1]:v=v*n+c*power;power*=d
 return (v>0)-(v<0)

def variations(seq,x):
 s=[sign_at(p,x) for p in seq];s=[v for v in s if v]
 return sum(a!=b for a,b in zip(s,s[1:]))

def split(p,a,b):
 for d in range(2,8):
  m=a+(b-a)/d
  if sign_at(p,m):return m
 raise AssertionError('Nonzero quartic cannot vanish at six distinct split points')

def isolate(p):
 assert len(p)==5 and p[-1]>0
 bound=2+max((abs(v)+p[-1]-1)//p[-1] for v in p[:-1])
 lo,hi=Q(-bound),Q(bound);seq=sturm(p)
 assert len(seq[-1])==1,'Repeated-root polynomial requires squarefree handling'
 total=variations(seq,lo)-variations(seq,hi)
 stack=[(lo,hi,total)];answer=[]
 while stack:
  a,b,n=stack.pop()
  if not n:continue
  if n==1 and b-a<=EPS:answer.append((a,b));continue
  m=split(p,a,b);nl=variations(seq,a)-variations(seq,m)
  assert 0<=nl<=n
  stack.extend([(m,b,n-nl),(a,m,nl)])
 answer.sort();assert len(answer)==total
 return answer,seq,bound

class I:
 def __init__(self,a,b=None):
  self.a=Q(a);self.b=Q(a if b is None else b);assert self.a<=self.b
 def __add__(self,o):
  o=o if isinstance(o,I) else I(o);return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-o if isinstance(o,I) else self+I(-o)
 def __mul__(self,o):
  o=o if isinstance(o,I) else I(o);v=[x*y for x in [self.a,self.b] for y in [o.a,o.b]];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=o if isinstance(o,I) else I(o);assert not(o.a<=0<=o.b),'Denominator interval meets zero'
  return self*I(1/o.b,1/o.a)
 def sign(self):return 1 if self.a>0 else -1 if self.b<0 else 0
 def rounded(self):
  low=(self.a*GRID).__floor__();high=(self.b*GRID).__ceil__()
  return I(Q(low,GRID),Q(high,GRID))
 def encoded(self):return [str(self.a),str(self.b)]

def peval(p,t):
 value=I(p[-1])
 for c in p[-2::-1]:value=value*t+c
 return value

def basic_fixtures():
 assert sign_at([-2,0,1],Q(3,2))==1
 assert sign_at([-2,0,1],Q(1))==-1
 assert remainder([-1,0,1],[-1,1])==[0]
 # Four specified simple roots -3,-1,1,2.
 p=[6,-1,-7,1,1]
 s=sturm(p);assert variations(s,Q(-4))-variations(s,Q(4))==4
 assert len(pgcd(p,[p[i]*i for i in range(1,len(p))]))==1
 assert (I(-3,-2)*I(4,5)).encoded()==['-15','-8']
 assert (I(2,3)/I(-5,-4)).encoded()==['-3/4','-2/5']

def run(mp,ap,out):
 basic_fixtures();mb=mp.read_bytes();data=json.loads(mb)
 ab=ap.read_bytes();assert mc.SHA(ab)==data['C592_A_sha256']
 A=json.loads(ab);P=[tuple(map(Q,row)) for row in A['raw_vertices']]
 q=[tuple(Q(x,h) for x in n) for n,h in zip(A['normals'],A['offsets'])]
 c0=tuple(map(Q,data['target_centroid']))
 assert all(mc.dot(n,c0)<1 for n in q)
 poly=list(map(int,data['quartic_integer_coefficients_low_to_high']))
 delta=list(map(Q,data['determinant_coefficients_low_to_high']))
 N=[list(map(Q,row)) for row in data['adjugate_times_d_coefficients_low_to_high']]
 k=tuple(map(Q,data['chamber_k']));d=tuple(map(Q,data['closure_d']))
 L=[tuple(map(Q,row)) for row in data['closure_L']]
 # Check the adjugate-vector and scalar polynomial identities coefficientwise.
 for i in range(3):
  for j in range(4):
   lhs=sum(L[i][h]*N[h][j] for h in range(3)) if j<3 else Q(0)
   if j:lhs+=N[i][j-1]
   assert lhs==delta[j]*d[i]
 check=[Q(0)]*5
 for j in range(4):check[j+1]+=4*delta[j]
 for i in range(3):
  for j in range(3):check[j]+=k[i]*N[i][j]
 assert mc.primitive(check)==poly
 assert len(pgcd(poly,mc.primitive(delta)))==1,'Singular candidates must be handled separately'
 print('EXACT_MASS_POLYNOMIAL_IDENTITIES_AND_NONSINGULARITY_PASS',flush=True)
 roots,seq,bound=isolate(poly)
 print('EXACT_STURM_ALL_REAL_ROOTS_ISOLATED',len(roots),flush=True)
 visible=set(data['visible_facets']);cert=[]
 r=(Q(0),Q(0),Q(1));oldrad=mc.dot(mc.sub(r,c0),mc.sub(r,c0))
 assert r in P and all(mc.dot(mc.sub(r,c0),mc.sub(x,r))<0 for x in P if x!=r)
 assert all(mc.dot(mc.sub(x,c0),mc.sub(x,c0))<oldrad for x in P if x!=r)
 for lo,hi in roots:
  t=I(lo,hi);den=peval(delta,t);assert den.sign()!=0
  point=[(-peval(row,t)/den).rounded() for row in N]
  flags=[];wrong=[]
  for f,normal in enumerate(q):
   gap=sum((point[i]*normal[i] for i in range(3)),I(-1))
   flag=gap.sign();flags.append(flag)
   if flag and flag!=(1 if f in visible else -1):wrong.append(f)
  valid=not wrong and all(flags)
  assert wrong or valid,'Refine root isolation to settle visibility'
  rec=dict(t_interval=[str(lo),str(hi)],point_box=[x.encoded() for x in point],in_selected_visibility_chamber=bool(valid),contradicting_visibility_facets=wrong)
  if valid:
   volume=I(Q(data['body_volume'])+Q(data['chamber_k0']))+t*4
   assert volume.a>0
   diff=[point[i]-c0[i] for i in range(3)]
   norm=sum((x*x for x in diff),I(0))
   apex= sum(((point[i]-r[i])*(r[i]-c0[i]) for i in range(3)),I(0))
   two_U=norm.a>oldrad and apex.b<0
   rec.update(actual_centroid_equals_target_exactly=True,volume_interval=volume.rounded().encoded(),two_distinct_strict_U_certified=bool(two_U),new_point_radius_squared_exceeds_apex=bool(norm.a>oldrad),old_apex_support_strict=bool(apex.b<0))
  cert.append(rec)
  print('ROOT',float((lo+hi)/2),'point',[float((x.a+x.b)/2) for x in point],'valid',valid,'twoU',rec.get('two_distinct_strict_U_certified'),flush=True)
 result=dict(status='EXACT_MASS_QUARTIC_ALL_ROOTS_VISIBILITY_CLASSIFIED',input_bytes=len(mb),input_sha256=mc.SHA(mb),parent_A_sha256=mc.SHA(ab),root_isolation_epsilon=str(EPS),coordinate_enclosure_grid=GRID,sturm_degrees=[len(s)-1 for s in seq],sturm_primitive_max_bits=[max(abs(c).bit_length() for c in s) for s in seq],cauchy_bound=bound,singular_mass_parameters_excluded=True,total_real_roots=len(roots),valid_chamber_roots=sum(c['in_selected_visibility_chamber'] for c in cert),all_valid_chamber_roots_have_two_U=all(c.get('two_distinct_strict_U_certified',False) for c in cert if c['in_selected_visibility_chamber']),roots=cert)
 out.write_bytes(mc.B(result));print(result['status'],len(mc.B(result)),mc.SHA(mc.B(result)),flush=True)
if __name__=='__main__':run(*map(Path,sys.argv[1:]))
