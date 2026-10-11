"""Exact finite covering of all positive diagonal metrics by stable-face cones.
The proof checker verifies a disjoint rational convex partition of the entire
closed weight simplex. Its base face is strictly stable for every positive weight.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
EXPECTED='f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7'
ORDER=[0,20,1,9,8,19,6,17,15,16,2,3,4,7,10,11,12,14,18,5]
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def val(c,p):return c[0]*p[0]+c[1]*p[1]+c[2]
def area(P):return sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(P,P[1:]+P[:1]))/2 if len(P)>2 else F(0)
def clean(P):
 out=[]
 for p in P:
  if not out or p!=out[-1]:out.append(p)
 if len(out)>1 and out[-1]==out[0]:out.pop()
 if area(out)==0:return []
 assert area(out)>0
 return out
def clip(P,c):
 if not P:return []
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  x,y=val(c,p),val(c,q)
  if x<=0:out.append(p)
  if x*y<0:out.append(tuple((y*a-x*b)/(y-x) for a,b in zip(p,q)))
 return clean(out)
def integer(c):
 d=lcm(*(v.denominator for v in c));a=[int(v*d) for v in c];g=gcd(*a)
 return tuple(x//g for x in a) if g else tuple(a)
def setup(path):
 b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED
 A=json.loads(b);g=list(map(F,A['raw_centroid']));Q=[]
 for n,h in zip(A['normals'],A['offsets']):
  nn=list(map(F,n));hh=F(h)-sum(x*y for x,y in zip(nn,g));assert hh>0;Q.append([x/hh for x in nn])
 assert Q[13][0]==Q[13][2]==0 and Q[13][1]>0
 assert all(Q[j][1]<Q[13][1] for j in range(len(Q)) if j!=13)
 tests={}
 for i in ORDER:
  cs=[]
  for j,q in enumerate(Q):
   if j==i:continue
   x,y,z=[Q[i][k]*(q[k]-Q[i][k]) for k in range(3)]
   cs.append(integer((x-z,y-z,z)))
  tests[i]=cs
 return tests
TRI=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
def create(tests):
 remaining=[TRI];covered=[];trace=[]
 for i in ORDER:
  next_remaining=[]
  for P in remaining:
   inter=P
   for c in tests[i]:inter=clip(inter,c)
   if not inter:next_remaining.append(P);continue
   R=P
   for c in tests[i]:
    outside=clip(R,tuple(-x for x in c))
    if outside:next_remaining.append(outside)
    R=clip(R,c)
    if not R:break
   assert R==inter
   covered.append({'face':i,'vertices':[[str(v) for v in p] for p in inter]})
  remaining=next_remaining;trace.append({'face':i,'covered_pieces':len(covered),'residual_pieces':len(remaining),'residual_area':str(sum(map(area,remaining),F(0)))})
  if not remaining:break
 assert not remaining,'Cover incomplete: no exclusion is established'
 return {'source_audit_sha256':EXPECTED,'metric_weights':'positive (lambda_x^-2,lambda_y^-2,lambda_z^-2), normalized to sum one','always_strict_face':13,'pieces':covered,'trace':trace}
def check(cert,tests):
 assert cert['source_audit_sha256']==EXPECTED and cert['always_strict_face']==13
 polys=[];total=F(0)
 for r in cert['pieces']:
  assert r['face']!=13;P=[tuple(map(F,p)) for p in r['vertices']];ar=area(P);assert ar>0;total+=ar
  for p in P:
   assert p[0]>=0 and p[1]>=0 and sum(p)<=1
   assert all(val(c,p)<=0 for c in tests[r['face']])
  # Convexity and outward edge halfspace representation of each proof polygon.
  hs=[]
  for p,q in zip(P,P[1:]+P[:1]):
   c=(q[1]-p[1],p[0]-q[0],q[0]*p[1]-p[0]*q[1]);assert all(val(c,v)<=0 for v in P);hs.append(c)
  for prev,old_hs in polys:
   inter=P
   for c in old_hs:inter=clip(inter,c)
   assert not inter,'Proof pieces have positive-area overlap'
  polys.append((P,hs))
 assert total==F(1,2)
 # Finite union of closed polygons has closed complement-relative boundary.
 # An uncovered point in the open simplex would have an uncovered open disk;
 # positive disk area contradicts the exact disjoint partition area 1/2.
 return {'status':'EXACT_C80_ALL_POSITIVE_DIAGONAL_STRETCH_EXCLUSION_PASS','pieces':len(polys),'faces':sorted(set(r['face'] for r in cert['pieces'])),'covered_area':'1/2','full_positive_metric_domain':True,'base_strict_plus_another_stable_or_weak_face':True,'no_claim_for_general_shear_or_changed_base':True}
def main():
 p=argparse.ArgumentParser();p.add_argument('audit');p.add_argument('out');p.add_argument('--check',action='store_true');a=p.parse_args();tests=setup(a.audit);out=Path(a.out)
 if a.check:cert=json.loads((out/'COVER.json').read_bytes())
 else:out.mkdir(parents=True,exist_ok=False);cert=create(tests);(out/'COVER.json').write_bytes(enc(cert))
 receipt=check(cert,tests)
 if not a.check:(out/'RECEIPT.json').write_bytes(enc(receipt))
 else:assert json.loads((out/'RECEIPT.json').read_bytes())==receipt
 print(receipt['status'],json.dumps(receipt),flush=True)
 for f in sorted(out.iterdir()):b=f.read_bytes();print(f.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
