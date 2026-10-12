"""Exact rational convex hull and actual uniform equilibrium audit of rounded points.
The arithmetic mean of all submitted points is only a coordinate origin, NOT
substituted for the independently integrated uniform volume centroid.
"""
import sys,json,hashlib,itertools
from pathlib import Path
from math import gcd,lcm
import numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def audit(src,out,grid=10**12):
 out.mkdir(exist_ok=False,parents=True);raw=src.read_bytes();X=np.load(src);N=len(X);ints=[tuple(int(round(v*grid)) for v in x) for x in X];ss=[sum(p[k] for p in ints) for k in range(3)];P=[tuple(N*p[k]-ss[k] for k in range(3)) for p in ints];den=N*grid;planes=set();qh=ConvexHull(np.array(P,dtype=float));bad=[]
 for tr in qh.simplices:
  a,b,c=[P[i] for i in tr];n=cross(sub(b,a),sub(c,a));h=dot(n,a);sg=[dot(n,p)-h for p in P]
  if max(sg)<=0:pass
  elif min(sg)>=0:n=tuple(-v for v in n);h=-h
  else:bad.append(tr.tolist());continue
  row=(*[v*den for v in n],h);gg=gcd(*row);planes.add(tuple(v//gg for v in row))
 if bad:
  (out/'rejected_numerical_hull.json').write_text(json.dumps(dict(invalid_nomination_triangles=bad,reason='Exact source point hull requires exhaustive supporting-plane enumeration'),indent=2)+'\n');planes=set()
  # Explicit exact enumeration, no approximation or artificial coplanarity.
  for i,j,k in itertools.combinations(range(N),3):
   n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
   if n==(0,0,0):continue
   pos=neg=False
   for p in P:
    d=dot(n,p)-h;pos|=d>0;neg|=d<0
    if pos and neg:break
   if pos and neg:continue
   if pos:n=tuple(-v for v in n);h=-h
   row=(*[v*den for v in n],h);gg=gcd(*row);planes.add(tuple(v//gg for v in row))
 H={'H':[list(p) for p in sorted(planes)]};assert all(p[3]>0 for p in H['H']);(out/'H.json').write_bytes(B(H));(out/'construction.json').write_bytes(B(dict(source=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),grid=grid,rounded_points=ints,coordinate_origin_mean_numerator=ss,coordinate_origin_mean_denominator=N*grid,shifted_points_integer=P,shifted_denominator=den)));r=check_B.run(H);supplied={tuple(mpq(x,den) for x in p) for p in P};actual={tuple(map(mpq,p)) for p in r['raw_vertices']};assert actual<=supplied;assert all(dot(row[:3],p)<=row[3]*den for row in H['H'] for p in P);(out/'audit.json').write_bytes(B(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],audit_sha256=hashlib.sha256(B(r)).hexdigest());(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_FREE_POINTS',src,summary,flush=True);return r
if __name__=='__main__':audit(ROOT/sys.argv[1],ROOT/sys.argv[2],10**int(sys.argv[3]) if len(sys.argv)>3 else 10**12)
