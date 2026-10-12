"""Exact stellar detachment of the stable carrier from the elder unstable vertex.
Adds p=(1-t)*foot+t*elder+epsilon*(foot-centroid) with rational t,epsilon.
The constructed homogeneous body's hull, actual mass and all signs are rebuilt.
"""
from pathlib import Path
from itertools import combinations
from math import lcm,gcd
import json,sys,time
from gmpy2 import mpq
import numpy as np
from exact_audit_vertices import check_B,dot,cross,sub
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()

def audit_points(X,out,meta):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);den=lcm(*(int(v.denominator) for p in X for v in p));P=[tuple(int(v*den) for v in p) for p in X];(out/'coordinates.json').write_bytes(B(dict(denominator=den,integer_points=P,construction=meta)));planes=set();t0=time.time()
 for ia,ib,ic in combinations(range(len(P)),3):
  a,b,c=P[ia],P[ib],P[ic];n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  h=dot(n,a);pos=False;neg=False
  for p in P:
   v=dot(n,p)-h;pos|=v>0;neg|=v<0
   if pos and neg:break
  if pos and neg:continue
  if pos:n=tuple(-x for x in n);h=-h
  assert h>0
  row=tuple(den*x for x in n)+(h,);d=gcd(*row);planes.add(tuple(x//d for x in row))
 raw={'H':sorted(planes)};(out/'raw.json').write_bytes(B(raw));rep=check_B.run(raw);assert {tuple(mpq(v) for v in p) for p in rep['raw_vertices']}<=set(map(tuple,X));(out/'audit.json').write_bytes(B(rep));su={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges']};su['stable_carriers']=[rep['faces'][f] for f in rep['stable_face_ids']];su['stable_U_intersection']=[sorted(set(rep['faces'][f])&set(rep['unstable_vertices'])) for f in rep['stable_face_ids']];su['seconds']=time.time()-t0;(out/'summary.json').write_text(json.dumps(su,indent=2));np.save(out/'hull_float.npy',np.array([[float(mpq(v)) for v in p] for p in rep['raw_vertices']]));print('EXACT_DETACH',out,su,flush=True)
 return rep

def main():
 source=Path('artifacts/projected_pflow1/exact_g9/audit.json');a=json.load(open(source));X=[tuple(mpq(v) for v in row) for row in a['raw_vertices']];g=tuple(mpq(v) for v in a['raw_centroid']);radii={i:dot(sub(X[i],g),sub(X[i],g)) for i in a['unstable_vertices']};elder=max(radii,key=radii.get);f=a['stable_face_ids'][0];assert elder in a['faces'][f];n=tuple(mpq(v) for v in a['normals'][f]);h=mpq(a['offsets'][f]);normal=tuple(v*(h-dot(n,g))/dot(n,n) for v in n);foot=tuple(u+v for u,v in zip(g,normal))
 for t in [mpq(1,4),mpq(1,2),mpq(3,4)]:
  for power in [7,6,5,4]:
   ep=mpq(1,10**power);p=tuple((1-t)*u+t*v+ep*w for u,v,w in zip(foot,X[elder],normal));out=Path(f'artifacts/detach_stable/t{str(t).replace("/","d")}_e{power}')
   audit_points(X+[p],out,{'source':str(source),'t':str(t),'epsilon':str(ep),'elder':elder,'stable_face':f,'formula':'(1-t)*orthogonal_foot+t*elder+epsilon*(orthogonal_foot-own_centroid)'})
if __name__=='__main__':main()
