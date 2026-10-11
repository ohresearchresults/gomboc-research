# material-f0bffb1fb754

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact radial basins and quantitative centred-Hausdorff obstruction

This is a coordinator-computed diagnostic and local-deformation obstruction, not a new own110 construction and not an exclusion of large deformations. The accepted own110 C622 endpoint remains unchanged.

## Exact inputs and reconstruction

C508 inputs come from complete standalone source [internal-source-reference], 14236bytes SHA12c3e1fa064498a760c0c7eb5ef0d79d00276584b0053dab531b7c6cc5cb3838. Save as RECOVER_C508.py and run `python RECOVER_C508.py`. It produces:
- G6_CHAIN_M60_I1_G5_EXACT_GEOMETRY.json,46853bytes,SHA986270e0b0f5d396fe78b5ecc93ed28b6154999dc3d9c2e79fa016c8a3c67510.
- G6_CHAIN_M60_I1_G12_EXACT_GEOMETRY.json,79549bytes,SHA504c86dedd6b9293ce1bf0c34f3db8349f0fe95db534f6b88e28c6e57cfe6f35.

LOW121 comes from BOTH [internal-source-reference] (BH81_FINITE_PRIMARY.md,18447bytes,SHA c97bda903918b05112ff8d03e8b030d02df4620b7c7c75ed7703ac0b097f37fa) and mandatory launcher/syntax correction [internal-source-reference] (BH81_PRIMARY_RECOVER.py.md,3147bytes,SHA0054a22972a02a4a8dc57326b62f047150a4826789a5f387311ae894e166e8f4). Extract RECOVER_PRIMARY.py as instructed there, run `python RECOVER_PRIMARY.py`. Expected BH81_PRIMARY_DURABLE_COLD_PASS. It produces LOW121_EXACT.json,29855bytes,SHA d77653ab141e4978e434ae7ba1c58041a8e8277a80537eb99720754b796a2396. All five BH81 primary output hashes were reproduced in this coordinator turn.

Save the complete fence below as exact_radial_tree.py (5846bytes,SHAf713980c378509e071c416eb419277c6deecd68a6bccab1c9e80410d1f872d5c). Reconstruction/verification command:
`python exact_radial_tree.py G6_CHAIN_M60_I1_G5_EXACT_GEOMETRY.json G6_CHAIN_M60_I1_G12_EXACT_GEOMETRY.json LOW121_EXACT.json`
Python3.13.5; the diagnostic itself uses the standard library only. Exact source reconstruction also uses numpy2.3.5/scipy1.17.0. Expect EXACT_RADIAL_TREE_PASS three times. Each output includes exact event order, complete basin memberships, true maximal-boundary edges, exact closed-cut assertions, and rational enclosures of all reported quantities. No rounded coordinates or floating comparison affects these results.

Expected outputs:
- G6_CHAIN_M60_I1_G5_EXACT_GEOMETRY_EXACT_RADIAL_TREE.json:8157bytes,SHA8a369d502f04cd614042f2e9c2ac5f7d48ca31dc89051f1605c4bf9d72856295.
- G6_CHAIN_M60_I1_G12_EXACT_GEOMETRY_EXACT_RADIAL_TREE.json:8157bytes,SHA7b49cb6de876ede4c46294edf9ad77ae415cd1cd2bf5da6cfdcdb2b93a3d432d.
- LOW121_EXACT_EXACT_RADIAL_TREE.json:2541bytes,SHA73f8b6366a9acfdc1990e22eaa2d358cbd4ceefbfbee6fe3eabcf59e7562134d.

## Exact scientific results

C508 G5 and G12 have the SAME dominant79-vertex basin, born at raw-lex U84 and merging through true edge70--76. Every outgoing true-edge derivative from that basin is strictly negative at the exact own centroid. The maximum edge bottleneck crossing its boundary equals its recorded merge level exactly. The unique stable input83 is the quadrilateral [135,147,160,163]; the basin contains160,163 and cuts its boundary at147--160 and135--163. Whole-basin surgery must account for this stable interface; the observation is not a proof that every possible deformation must move the stable facet.

With R=max||vertex-centroid|| and bar=(peak squared radius minus merge squared radius)/R^2, exact C508 G5 dominant bar lies in [482413367711,482413367712]/10^12; G12 in [482414958779,482414958780]/10^12. The other five G5 bars, by peaks61,124,162,91,70, are enclosed respectively by adjacent numerators2274531787,8450174696,5919829844,2285888714,180791820 over10^12. Thus five shallow peak cancellations would leave a much deeper global basin, not an almost-completed own110 body.

LOW121 has an exact21-vertex closed basin, born at U1 and merging through edge10--33, dominant relative bar in [244278161090,244278161091]/10^12. Stable face23 is [3,17,23,33,10,8,4]; the basin contains17,23,33 and crosses its boundary at3--17 and10--33. This preserves the literal parent identity (V44/E66/F24,C132,own121), not a triangular rounded companion.

## Quantitative perturbation lemma and proof

All bodies are translated to their respective TRUE uniform-volume centroids. Let K contain the centred ball of radius r and lie inside the centred ball of radius R. Write f_K(u)=rho_K(u)^2 on the unit sphere. Suppose its superlevel merge tree has a finite positive bar born at height b and dying at height d, delta=b-d>0; another higher surviving maximum exists. Any function f_L with sup|f_L-f_K|<delta/2 retains at least two superlevel components at some level, hence at least two maxima: choose epsilon below delta/2 and a threshold tau with d+epsilon<tau<b-epsilon. Both old peak directions lie in {f_L>tau}, while this set is contained in {f_K>tau-epsilon}, whose relevant components are still disjoint. Therefore an own-U1 convex polyhedron L requires sup|f_L-f_K|/R^2 >= bar/2.

For centred convex bodies with Hausdorff distance e<r, support-function inclusions give (1-e/r)K subset L subset (1+e/r)K. Indeed L subset K+eB subset (1+e/r)K, while L contains(r-e)B and K subset L+eB subset r/(r-e)L. Consequently sup|rho_L^2-rho_K^2|/R^2 <= 2(e/r)+(e/r)^2. Thus every centred own-U1 L obeys

d_H(K,L)/R >= (r/R)*(sqrt(1+bar/2)-1).

If e>=r, the same lower bound is automatic. This is a necessary finite-distance change, NOT an exclusion of the entire family. R and r are measured in the centred parent K, not separately renormalized for L.

The exact-centred inradius is min over maximal facets of support/sqrt(normal squared norm). Integer square-root enclosures at grid10^18 certify the displayed algebraic bounds. The resulting necessary d_H/R thresholds are:
- C508 G5: [45822219279,45822219280]/10^12, about0.045822219279 (4.5822% of parent R).
- C508 G12: [45822367581,45822367582]/10^12.
- LOW121: [1720995026,1720995027]/10^12, about0.001720995026.

The stronger C508 Hausdorff obstruction is not captured by simply comparing C or the number of unwanted equilibria: its r/R is about0.4016, versus LOW121 about0.0290. This supports finite nonlocal basin redesign for C508, while not proving LOW121 is globally easier.

Why the true-edge graph suffices: squared distance is strictly convex on each flat facet, so facet interiors have only minima, not maxima or saddle mergers. Descending superlevel connectivity is born at vertices and changes through true-edge bottlenecks; filling a facet minimum cannot merge distinct components because its small surrounding level curve is already connected. The script uses exact clamped minima along each true edge and a disjoint-set merge tree, then checks positive bars against the independently recomputed strict vertex maxima. It does not use a triangulated edge count. Stable-feature identity in the interface report is inherited from the accepted sources (input83 for C508; recorded strict face for BH81), not independently re-certified here; do not reuse that hard-coded C508 identity for a different descendant without its own S audit.

## Complete exact_radial_tree.py

```python
"""Exact true-edge radial merge trees for centred convex polyhedra.
Input: exact C508 geometry from RECOVER_C508.py, or BH81 *_EXACT.json.
Output contains exact interval bounds, all event identities, and basin membership;
large rational heights are recomputed deterministically, not rounded as inputs.
"""
import json,sys,hashlib,time,math
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sqrt_bounds(x,g=10**18):
 k=math.isqrt((x.numerator*g*g)//x.denominator)
 return F(k,g),F(k if k*k*x.denominator==x.numerator*g*g else k+1,g)
def enclosing_interval(lo,hi,g=10**12):
 a=lo*g;b=hi*g
 return [a.numerator//a.denominator,-((-b.numerator)//b.denominator),g]
def load(path):
 raw=Path(path).read_bytes();j=json.loads(raw)
 if 'centroid_homogeneous' in j:
  cc=j['centroid_homogeneous'];c=tuple(F(z,cc[3]) for z in cc[:3]);points=[tuple(F(z,row[3]) for z in row[:3]) for row in j['vertices']];faces=j['facets']
 else:c=tuple(map(F,j['centroid']));points=[tuple(map(F,row)) for row in j['points']];faces=j['faces']
 p=[sub(x,c) for x in points]
 return p,faces,hashlib.sha256(raw).hexdigest(),j
def interval(x,g=10**12):
 a=(x*g).numerator//(x*g).denominator
 return [a,a if x==F(a,g) else a+1,g]
def tree(path):
 p,faces,sha,source=load(path);edges=sorted({tuple(sorted((i,k))) for f in faces for i,k in zip(f,f[1:]+f[:1])})
 r2=[dot(x,x) for x in p];R2=max(r2);events=[(h,0,(i,)) for i,h in enumerate(r2)];nr=[set() for _ in p]
 for i,k in edges:
  nr[i].add(k);nr[k].add(i);e=sub(p[k],p[i]);ee=dot(e,e);t=-dot(p[i],e)
  assert ee>0
  if t<=0:h=r2[i]
  elif t>=ee:h=r2[k]
  else:h=r2[i]-t*t/ee
  assert h>0 and h<=r2[i] and h<=r2[k]
  events.append((h,1,(i,k)))
 events.sort(key=lambda a:(-a[0],a[1],a[2]));par=list(range(len(p)));peak=list(range(len(p)));members=[{i} for i in range(len(p))];records=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for h,kind,ids in events:
  if kind==0:continue
  i,k=ids;a,b=root(i),root(k)
  if a==b:continue
  if (r2[peak[a]],-peak[a])<(r2[peak[b]],-peak[b]):a,b=b,a
  birth=r2[peak[b]];bar=(birth-h)/R2
  if bar>0:
   records.append(dict(peak=peak[b],radius2=interval(birth),merge2=interval(h),relative_barrier=interval(bar),necessary_relative_squared_radial_change=interval(bar/2),edge=list(ids),basin=sorted(members[b])))
  par[b]=a;members[a]|=members[b]
 ur=[i for i in range(len(p)) if all(dot(p[i],sub(p[k],p[i]))<0 for k in nr[i])]
 assert len(records)+1==len(ur)
 assert all(row['peak'] in ur for row in records)
 survivor=peak[root(0)];assert survivor in ur
 dominant=max(records,key=lambda r:r['relative_barrier'][0])
 # Exact centered inradius and quantitative Hausdorff stability bound.
 supports=[]
 for face in faces:
  n=cross(sub(p[face[1]],p[face[0]]),sub(p[face[2]],p[face[0]]));d=dot(n,p[face[0]])
  assert d>0
  supports.append(d*d/dot(n,n))
 rin2=min(supports);rrlo,rrhi=sqrt_bounds(rin2/R2)
 # Every edge leaving a death component has height <= its death level.
 # This is an exact check of the decisive graph-cut boundary.
 A=set(dominant['basin']);boundary=[(h,ids) for h,k,ids in events if k==1 and ((ids[0] in A)!=(ids[1] in A))]
 death=next(h for h,k,ids in events if k==1 and list(ids)==dominant['edge'])
 assert boundary and max(h for h,ids in boundary)==death
 bar=(r2[dominant['peak']]-death)/R2
 qlo,qhi=sqrt_bounds(1+bar/2)
 hausdorff=enclosing_interval(rrlo*(qlo-1),rrhi*(qhi-1))
 # Every outgoing physical edge derivative across the dominant cut is negative.
 cut_derivatives=[]
 for h,(i,k) in boundary:
  if k in A:i,k=k,i
  cut_derivatives.append(dot(p[i],sub(p[k],p[i])))
 assert max(cut_derivatives)<0
 # The accepted source supplies the stable-feature identity; no new S audit here.
 stable_index=source['active'].index(83) if 'active' in source else source['own']['strict_features'][0][0]
 stable_face=faces[stable_index]
 stable_crossings=[sorted((i,k)) for i,k in zip(stable_face,stable_face[1:]+stable_face[:1]) if ((i in A)!=(k in A))]
 out=dict(input_sha256=sha,V=len(p),E=len(edges),F=len(faces),strict_U=ur,survivor=survivor,R2=interval(R2),r2=interval(rin2),r_over_R=enclosing_interval(rrlo,rrhi),necessary_centered_Hausdorff_over_R=hausdorff,bars=records,
  dominant_peak=dominant['peak'],dominant_basin_vertices=len(A),dominant_boundary_edges=[list(e) for h,e in boundary],
  dominant_boundary_max_equals_merge=True,dominant_closed_physical_escape_cut=True,stable_face_index=stable_index,stable_face_input=83 if 'active' in source else None,stable_face_vertices=stable_face,stable_basin_intersection=sorted(A.intersection(stable_face)),stable_boundary_crossings=stable_crossings,event_order=[[k,list(ids)] for h,k,ids in events],
  interval_convention='[floor(value*grid),ceil(value*grid),grid]; bounds are exact rational',
  status='exact merge-tree diagnostic, not an own110 construction or an exclusion of large deformations')
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();target=Path(path).stem+'_EXACT_RADIAL_TREE.json';Path(target).write_bytes(raw)
 receipt=dict(file=target,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),U=len(ur),necessary_centered_Hausdorff_over_R=hausdorff,dominant_peak=dominant['peak'],dominant_basin_vertices=len(A),relative_barrier=dominant['relative_barrier'],necessary_relative_squared_radial_change=dominant['necessary_relative_squared_radial_change'])
 print('EXACT_RADIAL_TREE_PASS',json.dumps(receipt,sort_keys=True),flush=True);return receipt
if __name__=='__main__':
 result=[tree(path) for path in sys.argv[1:]]
 Path('EXACT_RADIAL_TREE_RECEIPTS.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
```
