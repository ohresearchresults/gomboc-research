# material-b38db3007aae

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J76 — exact exclusion of weak-free U1 on every positive native diagonal metric

## Statement and scope
Let K be the literal homogeneous R22-B7 from immutable result figure-0566, SHA1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be. Its reconstructed density-one point file is4392B SHA bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59. For every G=diag(a,b,c) with a,b,c>0 in these native coordinate axes, its own centered vertices cannot have exactly one strict unstable equilibrium with no weak unstable equilibria. Consequently no homogeneous affine image with A^T A of this form is own strict110/weak000. Output rotations, translations and common scaling are immaterial. This is NOT an exclusion of general off-diagonal positive-definite G or nonlinear material changes.

## Proof mechanism
The homogeneous centroid transforms affinely. With original centered vertex x_i and true neighbor x_j, a strict U guard is x_i^T G(x_j-x_i)<0. Normalize a+b+c=1, giving a two-dimensional simplex. For each vertex its closed U-region is an exact rational convex polygon. The code partitions the simplex incrementally and discards a cell only when two distinct closed U labels cover it. Every split conserves exact rational area; only zero-area boundaries are discarded. There are71 positive-area U-polygons. Only19 in exact descending-area order suffice to eliminate every positive-area cell with fewer than two labels; at most7 live convex pieces occur.
Every primitive guard is verified nonidentically zero on this simplex. Away from finitely many guard lines, closed U is strict U, so almost every positive diagonal metric has at least two strict U. If a positive diagonal metric had exactly one strict U and no weak U, all strict inequalities at that U and a strictly violating inequality at every other vertex would persist in an open relative neighborhood. Such a neighborhood contains a generic point and has positive area, contradicting the exact cover. Boundary metrics with a zero diagonal entry are not claimed positive definite. No Poincare identity substitutes for this argument.

## Required exact input and reconstruction
This capsule deliberately reuses the already preserved complete source material [internal-source-reference]. Its11412 bytes, SHA e16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82, must be saved as J75_REFERENCE110_CAP233.py. It contains all75 rational rows, their planar correction and the exact supporting-hull/mass helpers. BOTH this capsule and that source are needed. No sandbox, old optimizer or FULL76 is needed.
Save the following complete4084-byte unit as diagonal76.py, SHA3309605cfcf002ca5336b01251ba0b7ac7d2a50f71a8953f030c42cd72df52ce. Run OPENBLAS_NUM_THREADS=1 python diagonal76.py. Executed environment CPython3.13.5, NumPy2.3.5, SciPy1.17.0. Qhull only nominates the parent facets; the imported source certifies their exact supporting closed hull. The parameter-space cover itself uses integer/Fraction arithmetic only.
Observed output diagonal76_exact.json21609B SHA21b8ffaa62642550d681e81444bfedc5066a8446e79f491dca391f1d2e494060. It contains every exact area transition and any remaining cells; final remaining_area2 is0 and remaining_pieces is empty. Observed terminal marker J76_ALL_POSITIVE_DIAGONAL_METRICS_NO_WEAKFREE_U1_EXACT_PASS. This is the coordinator's executed proof, not an independent second verifier.

```python
"""Exact two-fold covering of the positive diagonal metric simplex.
For the literal homogeneous R22-B7, each U-cell is a rational polygon.
The algorithm retains only parameter cells covered by fewer than two U-cells.
Zero-area boundaries are discarded; hence exclusion is for weak-free U1,
whose existence would imply an open parameter neighborhood of U1.
Requires exact J75 source; no floating geometry is used in the cover.
"""
from fractions import Fraction as F
from math import lcm,gcd
from functools import reduce
from pathlib import Path
import json,hashlib,time
import J75_REFERENCE110_CAP233 as m

def area2(p):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1]))) if len(p)>2 else F(0)
def value(a,p):return a[0]*p[0]+a[1]*p[1]+a[2]
def clip(p,a,sign=1):
 if not p:return []
 out=[]
 vals=[sign*value(a,v) for v in p]
 for k,(u,v) in enumerate(zip(p,p[1:]+p[:1])):
  su,sv=vals[k],vals[(k+1)%len(p)]
  if su<=0:out.append(u)
  if su*sv<0:
   t=su/(su-sv);out.append((u[0]+t*(v[0]-u[0]),u[1]+t*(v[1]-u[1])))
 clean=[]
 for v in out:
  if not clean or v!=clean[-1]:clean.append(v)
 if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
 return clean if area2(clean)>0 else []
def bbox(p):return (min(v[0] for v in p),max(v[0] for v in p),min(v[1] for v in p),max(v[1] for v in p))
def disjoint(a,b):return a[1]<=b[0] or b[1]<=a[0] or a[3]<=b[2] or b[3]<=a[2]
def partition(poly,guards):
 # Returned outside pieces have disjoint interiors and avoid this U-cell.
 outside=[];inside=poly
 for a in guards:
  if not inside:break
  pp=clip(inside,a,-1)
  if pp:outside.append(pp)
  inside=clip(inside,a,1)
 return outside,inside

def certificate():
 K=m.hull(m.points());V,M=m.mass(K);c=m.mul(M,1/V);p=[m.sub(v,c) for v in K['points']]
 D=lcm(*(v.denominator for row in p for v in row));z=[[int(v*D) for v in row] for row in p]
 nb=[[] for _ in z]
 for i,j in K['edges']:nb[i].append(j);nb[j].append(i)
 tri=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
 cells=[]
 for i,js in enumerate(nb):
  gg=[]
  for j in sorted(js):
   a=[z[i][k]*(z[j][k]-z[i][k]) for k in range(3)]
   row=(a[0]-a[2],a[1]-a[2],a[2]);g=reduce(gcd,(abs(v) for v in row),0)
   assert g>0, "An identically-zero guard cannot certify generic strict U"
   gg.append(tuple(v//g for v in row))
  poly=tri
  for a in gg:poly=clip(poly,a)
  if poly:cells.append((i,gg,poly,area2(poly),bbox(poly)))
 # Exact descending-area order, tie by original material index.
 cells.sort(key=lambda q:(-q[3],q[0]))
 parts=[(tri,())];trace=[]
 initial=area2(tri)
 for i,gg,cell,ar,bb in cells:
  new=[];removed=F(0);before=sum(area2(p) for p,old in parts)
  for poly,old in parts:
   if disjoint(bbox(poly),bb):new.append((poly,old));continue
   outside,inside=partition(poly,gg)
   # Local exact conservation: every discarded area has two explicit U labels.
   assert area2(poly)==sum(area2(s) for s in outside)+area2(inside)
   new.extend((s,old) for s in outside)
   if inside:
    if old:removed+=area2(inside)
    else:new.append((inside,(i,)))
  parts=new;after=sum(area2(p) for p,old in parts)
  assert before-after==removed
  trace.append({'vertex':i,'pieces':len(parts),'area2_remaining':str(after),'area2_newly_covered_twice':str(removed)})
  print('CELL',i,'pieces',len(parts),'remaining',float(after),flush=True)
  if not parts:break
 remaining=sum(area2(p) for p,old in parts)
 out={'input_parent_sha256':'bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59','family':'G=diag(a,b,c); a,b,c>0, trace normalized','positive_area_U_cells':len(cells),'initial_area2':str(initial),'remaining_area2':str(remaining),'trace':trace,'remaining_pieces':[{'polygon':[[str(x),str(y)] for x,y in p],'covered_labels':old} for p,old in parts]}
 bb=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('diagonal76_exact.json').write_bytes(bb)
 print('RECEIPT',len(bb),hashlib.sha256(bb).hexdigest(),flush=True)
 if not parts:print('J76_ALL_POSITIVE_DIAGONAL_METRICS_NO_WEAKFREE_U1_EXACT_PASS',flush=True)
 else:print('J76_DIAGONAL_COVER_NOT_COMPLETE',flush=True)
if __name__=='__main__':certificate()
```
