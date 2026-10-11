"""Exact two-sided diagonal flip of a flattened true quadrilateral facet.
The chosen simple vertex moves on the exact intersection line of its other two
supporting facets. Their polygon planes stay fixed; the quad splits into two
true supporting triangles. Re-hull and actual homogeneous census are exact.
"""
from pathlib import Path
from itertools import combinations
from math import gcd,lcm
import sys,json,time,hashlib
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def prim(row):
 den=lcm(*(int(x.denominator) for x in row));z=[int(x*den) for x in row];d=gcd(*z);return [x//d for x in z]
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def construct(sign,exponent):
 source=ROOT/'artifacts/contact_wall_retire/delete75/audit.json';r=json.loads(source.read_text());X=[tuple(mpq(v) for v in p) for p in r['raw_vertices']];quad=108;vtx=104;vs=r['faces'][quad];other=[i for i,f in enumerate(r['faces']) if vtx in f and i!=quad];assert len(other)==2 and len(vs)==4;d=cross(r['normals'][other[0]],r['normals'][other[1]]);scale=max(map(abs,d));d=tuple(mpq(x,scale) for x in d);t=mpq(sign,10**exponent);old=X[vtx];X[vtx]=tuple(a+t*b for a,b in zip(old,d));rows=[]
 for i,(n,h) in enumerate(zip(r['normals'],r['offsets'])):
  if i==quad:continue
  assert all(dot(n,x)<=h for x in X),'step left retained support domain';rows.append([*n,h])
 children=[]
 for ids in combinations(vs,3):
  a,b,c=[X[i] for i in ids];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  if h<0:n=tuple(-z for z in n);h=-h
  if h<=0 or any(dot(n,p)>h for p in X):continue
  rows.append(prim((*n,h)));children.append(ids)
 assert len(children)==2,'not a valid two-triangle local flip'
 out=ROOT/'artifacts/contact_wall_flip'/f's{sign}_g{exponent}';out.mkdir(exist_ok=False,parents=True);H={'H':rows};(out/'H.json').write_bytes(blob(H));con=dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),quad=quad,quad_vertices=vs,moved_vertex=vtx,other_supports=other,step=str(t),direction=[str(z) for z in d],old_vertex=[str(z) for z in old],new_vertex=[str(z) for z in X[vtx]],child_triples=children);(out/'construction.json').write_bytes(blob(con));rr=check_B.run(H);assert {tuple(mpq(v) for v in p) for p in rr['raw_vertices']}==set(X);assert (rr['V'],rr['E'],rr['F'])==(r['V'],r['E']+1,r['F']+1);(out/'audit.json').write_bytes(blob(rr));s={k:rr[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C=2*rr['E'],audit_sha256=hashlib.sha256(blob(rr)).hexdigest(),child_triples=children);(out/'summary.json').write_text(json.dumps(s,indent=2)+'\n');print('EXACT_LOCAL_FLIP',sign,exponent,s,flush=True)
if __name__=='__main__':
 for sign in [-1,1]:
  for exponent in [9,7,5]:construct(sign,exponent)
