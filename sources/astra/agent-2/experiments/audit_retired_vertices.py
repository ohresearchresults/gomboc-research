"""Exact physical hull of selected original benchmark vertices.
Floating hull triangles nominate planes only. Each nominated plane must support
ALL literal rational inputs, the exact bounded intersection is reconstructed, and
both hull inclusions are checked. Failure is explicit; no approximate hull claim.
"""
from pathlib import Path
from math import gcd,lcm
from fractions import Fraction
import json,sys,time,hashlib,numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def audit(source,out):
 out.mkdir(exist_ok=False,parents=True);meta=json.loads(source.read_text());ids=meta['selected'];r=json.loads(Path(meta['parent_report']).read_text());ref=[mpq(int(round(float(mpq(v))*10**12)),10**12) for v in r['raw_centroid']];P=[sub(tuple(mpq(v) for v in r['raw_vertices'][i]),ref) for i in ids];X=np.array(P,dtype=float);h=ConvexHull(X);planes=set();rejects=0
 for ia,ib,ic in h.simplices:
  a,b,c=P[ia],P[ib],P[ic];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);sign=[dot(n,p)-hh for p in P]
  if max(sign)>0 and min(sign)<0:rejects+=1;continue
  if max(sign)>0:n=tuple(-v for v in n);hh=-hh
  assert hh>0
  row=(*n,hh);den=lcm(*(int(v.denominator) for v in row));ints=[int(v*den) for v in row];div=gcd(*ints);planes.add(tuple(v//div for v in ints))
 H={'H':sorted(planes)};(out/'H.json').write_bytes(blob(H));(out/'coordinates.json').write_bytes(blob(dict(source=str(source),selected_ids=ids,translation=[str(v) for v in ref],points=[[str(v) for v in p] for p in P],floating_nominations_rejected=rejects)));print('NOMINATED_EXACT_PLANES',len(planes),'rejected',rejects,flush=True)
 rr=check_B.run(H);Ps=set(P);Vs={tuple(mpq(v) for v in p) for p in rr['raw_vertices']};assert Vs==Ps,'Exact halfspace intersection differs from submitted vertex hull';assert all(dot(row[:3],p)<=row[3] for row in H['H'] for p in P)
 (out/'audit.json').write_bytes(blob(rr));summary={k:rr[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary['C']=2*rr['E'];summary['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()};(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_SELECTED',summary,flush=True)
 return rr
if __name__=='__main__':audit(ROOT/sys.argv[1],ROOT/sys.argv[2])
