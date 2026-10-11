"""Rational convex hull of exact old vertices and one rounded extra vertex.
Both containments are certified: all supplied points satisfy every new plane;
every vertex of the exact bounded H-hull is one of the supplied points.
"""
from pathlib import Path
from math import lcm,gcd
import json,sys,hashlib,numpy as np
from gmpy2 import mpq
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
src=ROOT/'artifacts/projected_contact_retire/delete_4_35_94_99/audit.json';raw=src.read_bytes();r=json.loads(raw);base=ROOT/'artifacts/single_vertex_augmentation_C490';rows=json.loads((base/'screen.json').read_text());center=tuple(map(mpq,r['raw_centroid']));old=[tuple(map(mpq,row)) for row in r['raw_vertices']];G=10**12
for index in map(int,sys.argv[1:]):
 row=next(x for x in rows if x['index']==index);out=base/f'exact_{index}_g12';out.mkdir(exist_ok=False);added=tuple(center[k]+mpq(round(row['point'][k]*G),G) for k in range(3));P=old+[added];data=dict(source_report=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),index=index,added_vertex=[str(x) for x in added],grid=G,centered_point_numerators=[round(x*G) for x in row['point']]);(out/'construction.json').write_bytes(B(data));X=np.array([[float(v) for v in sub(p,center)] for p in P]);h=ConvexHull(X);planes=set()
 for tr in h.simplices:
  a,b,c=[P[i] for i in tr];n=cross(sub(b,a),sub(c,a));d=dot(n,a);vals=[dot(n,x)-d for x in P]
  if all(v<=0 for v in vals):pass
  elif all(v>=0 for v in vals):n=tuple(-v for v in n);d=-d
  else:raise ValueError('Qhull nomination plane is not an exact support')
  den=lcm(*(int(x.denominator) for x in (*n,d)));ints=[int(x*den) for x in (*n,d)];gg=gcd(*ints);assert gg>0;planes.add(tuple(x//gg for x in ints))
 H={'H':[list(x) for x in sorted(planes)]};(out/'H.json').write_bytes(B(H));a=check_B.run(H);pv={tuple(map(mpq,x)) for x in a['raw_vertices']};assert pv<=set(P),'exactH contains vertices absent fromconv(P)';(out/'audit.json').write_bytes(B(a));summ={k:a[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summ.update(C=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],audit_sha256=hashlib.sha256(B(a)).hexdigest());(out/'summary.json').write_text(json.dumps(summ,indent=2)+'\n');print('EXACT_AUGMENTATION',index,summ,flush=True)
