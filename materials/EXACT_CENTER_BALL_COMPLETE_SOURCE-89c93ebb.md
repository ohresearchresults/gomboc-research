# material-89c93ebb46db

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete source unit: exact every-center ball obstruction, fixed C620 body

Save the following fence including its final newline as EXACT_CENTER_BALL.py:2554bytes,SHA256 dd50a4454c1e16ea8d0492c0f6fc38a71a06e8cf2c987f9da64e971b5c5f8e2a. Standard library only, CPython3.13.5.

Exact input recovery: decode CONDITION25 ALL3 [internal-source-reference],[internal-source-reference],[internal-source-reference] into source/, and VIRTUAL BOTH [internal-source-reference],[internal-source-reference] into virtual_package/. Run `python -B -S virtual_package/REPLAY_VIRTUAL_CAPSULE.py source virtual_cold`, observed terminal C620_REFERENCE110_OWN_NONWINNER_COLD_CAPSULE_PASS. Its receipt3150bytes SHA19bf9fbca09565159fc3544ce9af33ad93b8364dbc8debe89e385561f21ee70d and all body hashes are fixed in those dependencies. No originating sandbox is needed.

Run `python -B -S EXACT_CENTER_BALL.py --body virtual_cold/body --out ball_exact`. Observed terminal C620_EVERY_CENTER_BALL_TWO_UNSTABLE_EXACT_PASS; output CERTIFICATE.json932bytes SHA c9f7bc412337b18713f5208f10920feb26b9f5124fe598260898911ca3b8c053.

For the unchanged exact body COORD_C620_VIRTUAL99_REFERENCE110_OWN60_78_136, EVERY center within closed radius1720637/10^10 of its own centroid leaves vertices80 and94 strictly unstable. For each selected vertex and every other vertex, exact e<0 and e²>r²|d|² imply e(c)<=e(g)+r|d|<0. The137 support tests keep the entire ball interior. This excludes all reference centers in this fixed-body ball, not shape deformations, other bodies, or all C620 constructions. The upper radius in the output bounds just the80→82 center-plane distance. It is not a global upper bound.

```python
"""Exact fixed-body obstruction for EVERY center in an explicit Euclidean ball.
At least two vertices remain strictly unstable. Thus no point in this ball is
a mono-monostatic reference center. The statement is not a shape-deformation
obstruction or a lower bound on edge complexity. Python stdlib only.
"""
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--body',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 r=json.loads((a.body/'A.json').read_text());raw=json.loads((a.body/'RAW.json').read_text());assert (r['V'],r['E'],r['F'])==(175,310,137)
 X=[[F(t) for t in row] for row in r['raw_vertices']];Q=[[F(x,row[3]) for x in row[:3]] for row in raw['H']];g=list(map(F,r['raw_centroid']));radius=F(1720637,10**10);upper=F(1720638,10**10);checks=0
 for i in [80,94]:
  for j in range(len(X)):
   if i==j:continue
   d=sub(X[j],X[i]);e=dot(sub(X[i],g),d);D=dot(d,d)
   # For |c-g|<=r, e(c)<=e(g)+r*sqrt(D)<0 by exact squaring.
   assert e<0 and e*e>radius*radius*D;checks+=1
 for q in Q:
  h=1-dot(q,g);assert h>0 and h*h>radius*radius*dot(q,q)
 d=sub(X[82],X[80]);e=dot(sub(X[80],g),d);D=dot(d,d);assert e*e<upper*upper*D
 rc=json.loads((a.body/'REFERENCE_CENTER.json').read_text());c=[F(x,rc['grid']) for x in rc['integer_row']];off=sub(c,g);assert dot(off,off)>radius*radius
 out=dict(marker='C620_EVERY_CENTER_BALL_TWO_UNSTABLE_EXACT_PASS',identity='COORD_C620_VIRTUAL99_REFERENCE110_OWN60_78_136',V=175,E=310,F=137,ball_center='own exact filled-volume centroid',closed_ball_radius=str(radius),strict_unstable_vertices=[80,94],all_other_vertex_tests=checks,strict_interior_plane_tests=len(Q),limiting_test_for_vertex80=[80,82],limiting_radius_upper=str(upper),scope='Every reference center in this fixed-body closed ball has at least two strict unstable vertices; no claim for shape changes or outside this ball.',body_hashes={f:H((a.body/f).read_bytes()) for f in ['A.json','RAW.json','REFERENCE_CENTER.json']},method_sha256=H(Path(__file__).read_bytes()),python=sys.version.split()[0])
 data=B(out);(a.out/'CERTIFICATE.json').write_bytes(data);print(out['marker'],len(data),H(data),flush=True)
if __name__=='__main__':main()
```
