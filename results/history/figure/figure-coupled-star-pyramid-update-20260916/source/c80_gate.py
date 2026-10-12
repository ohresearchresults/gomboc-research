"""Exact fixed-base pyramid centroid test and height obstruction certificate.
All arithmetic and output definitions use only the Python standard library.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm,isqrt
from pathlib import Path
sys.set_int_max_str_digits(0)
POINTS=[[-66294190,227941,2608697],[-66539507,227941,-12351907],[-63292228,227941,17048174],[-63717145,227941,-27612608],[-57823754,227941,30439587],[-57515357,227941,-42510726],[-50192873,227941,42502470],[-47518485,227941,-56391110],[-40722545,227941,52969394],[-33461658,227941,-68086491],[-15099182,227941,-76015914],[-29598263,227941,61750890],[7302524,227941,-77602682],[32327466,227941,106281898],[9316983,-4558809,-76697552],[79500788,227941,46525186],[84345871,227941,39971911],[90059112,227941,29647108],[97069983,227941,-15011783],[94470034,227941,18198055],[97382431,227941,4337405]]
REF=[F(7695683),F(168054),F(-75622586)]
def encode(o):return json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()
def save(p,o):p.write_bytes(encode(o))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det2(a,b):return a[0]*b[1]-a[1]*b[0]
def polygon(P):
 ids=sorted(i for i in range(len(P)) if i!=14);ids.sort(key=lambda i:(P[i][0],P[i][2]));out=[]
 def turn(i,j,k):return det2((P[j][0]-P[i][0],P[j][2]-P[i][2]),(P[k][0]-P[i][0],P[k][2]-P[i][2]))
 for seq in [ids,ids[::-1]]:
  cy=[]
  for i in seq:
   while len(cy)>1 and turn(cy[-2],cy[-1],i)<=0:cy.pop()
   cy.append(i)
  out+=cy[:-1]
 assert len(out)==20 and len(set(out))==20
 return out

def hull(P):
 rows=set()
 for a,b,c in combinations(P,3):
  n=cross(sub(b,a),sub(c,a))
  if not any(n):continue
  h=dot(n,a);s=[h-dot(n,p) for p in P]
  if all(x<=0 for x in s):n=tuple(-x for x in n);h=-h
  elif not all(x>=0 for x in s):continue
  assert h>0
  v=n+(h,);D=lcm(*(x.denominator for x in v));r=[int(D*x) for x in v];g=gcd(*r);rows.add(tuple(x//g for x in r))
 return {'H':[list(r) for r in sorted(rows)]}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--parent',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();assert __debug__
 root=a.parent.resolve()
 for name,spec in json.loads((root/'MANIFEST.json').read_bytes()).items():
  b=(root/name).read_bytes();assert len(b)==spec['bytes'] and hashlib.sha256(b).hexdigest()==spec['sha256']
 sys.path.insert(0,str(root));import check_A,check_B,centred_mass
 a.out.mkdir(parents=True,exist_ok=False);P=[tuple(map(F,p)) for p in POINTS];cy=polygon(P);B=[(P[i][0],P[i][2]) for i in cy];edges=list(zip(B,B[1:]+B[:1]));area2=sum(det2(p,q) for p,q in edges);assert area2>0
 bc=[sum((p[k]+q[k])*det2(p,q) for p,q in edges)/(3*area2) for k in range(2)];base=(bc[0],F(227941),bc[1]);squared=[]
 for p,q in edges:
  e=sub(q,p);gap=det2(e,sub(bc,p));assert gap>0;squared.append(gap*gap/dot(e,e))
 R=min(isqrt(x.numerator//x.denominator) for x in squared)-1;assert R>0 and all(x>R*R for x in squared)
 original_g=tuple((3*b+x)/4 for b,x in zip(base,P[14]));forced=tuple(4*g-3*b for g,b in zip(REF,base));forced_h=base[1]-forced[1];assert 0<forced_h<R
 save(a.out/'PYRAMID_CERTIFICATE.json',{'base_cycle_original_indices':cy,'base_centroid':base,'area':area2/2,'base_edge_distance_squared':squared,'base_centred_disk_radius':R,'original_centroid':original_g,'old_apex':P[14],'target_centroid':REF,'forced_apex':forced,'forced_height':forced_h,'theorem_scope':'For this fixed planar base and ANY apex tangential coordinates, any nondegenerate uniform pyramid of height 0<h<R has at least two stable equilibria; otherwise two stable-or-weak equilibria. Not a claim for h>=R or different bases.'})
 summary={}
 for name,apex,g in [('C80_ORIGINAL_CENTRED',P[14],original_g),('C80_FORCED_REFERENCE_CENTROID',forced,REF)]:
  out=a.out/name;out.mkdir();Q=P[:];Q[14]=apex;X=[sub(p,g) for p in Q];raw=hull(X);save(out/'POINTS.json',{'points':X});save(out/'RAW.json',raw)
  aa=check_A.run(raw);bb=check_B.run(raw);assert aa==bb;assert {tuple(map(F,p)) for p in aa['raw_vertices']}==set(X);assert all(F(x)==0 for x in aa['raw_centroid']);cm=centred_mass.run(aa)
  save(out/'A.json',aa);save(out/'B.json',bb);save(out/'MASS.json',cm)
  summary[name]={'V':aa['V'],'E':aa['E'],'F':aa['F'],'C':2*aa['E'],'strict':aa['counts'],'weak':aa['weak'],'stable_faces':aa['stable_face_ids'],'unstable_vertices':aa['unstable_vertices'],'saddle_edges':aa['saddle_edges'],'centred_mass':cm,'disposition':'ephemeral_nonwinner_pending_canonical_capsule'}
  print(name,summary[name],flush=True)
 save(a.out/'SUMMARY.json',summary)
 mf={}
 for p in sorted(a.out.rglob('*')):
  if p.is_file():b=p.read_bytes();mf[str(p.relative_to(a.out))]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 save(a.out/'OUTPUT_MANIFEST.json',mf);print('C80_FIXED_BASE_EXACT_CENTROID_AND_HEIGHT_GATE_PASS',R,flush=True)
if __name__=='__main__':main()
