"""Freeze exact supporting selectors from a numerical proposal. No numerical acceptance."""
import json,sys,hashlib
from pathlib import Path
from fractions import Fraction as Q
from math import lcm,gcd
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def point(row):
 x=list(map(Q,row));d=lcm(*(v.denominator for v in x));return tuple(int(v*d) for v in x)+(d,)
def plane(a,b,c):
 e=[b[i]*a[3]-a[i]*b[3] for i in range(3)];f=[c[i]*a[3]-a[i]*c[3] for i in range(3)];n=cross(e,f)
 if n==(0,0,0):return None
 h=dot(n,a[:3]);r=tuple(v*a[3] for v in n)+(h,);g=gcd(*r)
 if h<0:g=-g
 return tuple(v//g for v in r)
def supports(r,P):return r and r[3]>0 and all(dot(r[:3],p[:3])<=r[3]*p[3] for p in P)
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 ap,qp,out=map(Path,sys.argv[1:]);a=json.loads(ap.read_text());q=json.loads(qp.read_text());assert hashlib.sha256(ap.read_bytes()).hexdigest()==q['parent_audit_sha256'];out.mkdir(exist_ok=True)
 P=[point(r) for r in a['raw_vertices']]+[point([Q(v,q['grid']) for v in r]) for r in q['new_raw_points']]
 hmap={};rejected=[]
 for tri in q['floating_hull_triangles']:
  r=plane(*(P[i] for i in tri))
  if supports(r,P):hmap.setdefault(r,tri)
  else:rejected.append(tri)
 old={tuple(n)+(h,):i for i,(n,h) in enumerate(zip(a['normals'],a['offsets'])) if supports(tuple(n)+(h,),P)}
 allrows=sorted(set(old)|set(hmap));selected=[]
 for r in allrows:
  selected.append({'old':old[r]} if r in old else {'tri':hmap[r]})
 cfg={'object':'COORD_C602_EXPOSED_CHAIN5_G1E12','parent_case':'BQ13_C602','parent_audit_sha256':q['parent_audit_sha256'],'grid':q['grid'],'new_raw_points':q['new_raw_points'],'selectors':selected}
 (out/'SELECTORS.json').write_bytes(blob(cfg));(out/'raw.json').write_bytes(blob({'H':[list(r) for r in allrows]}));(out/'POINTS.json').write_bytes(blob([[str(Q(v,p[3])) for v in p[:3]] for p in P]));(out/'PREPARE.json').write_bytes(blob({'planes':len(allrows),'old_retained':len(old),'proposed_planes':len(hmap),'rejected_triangles':rejected}))
 print('EXACT_SUPPORTING_SELECTORS',len(allrows),len(old),len(hmap),'rejected',len(rejected),flush=True)
if __name__=='__main__':main()
