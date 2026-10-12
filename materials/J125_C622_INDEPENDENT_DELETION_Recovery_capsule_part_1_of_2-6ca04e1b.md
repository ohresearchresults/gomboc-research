# material-6ca04e1b6567

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J125 C622 independent-deletion theorem — Recovery capsule part 1/2

## Executed exact finding
For EVERY independent set I in the original true-edge graph of canonical C622, let K be the convex hull of the UNMOVED original vertices not in I. If K is full dimensional and has exactly ONE STRICT unstable equilibrium at its OWN homogeneous-volume centroid, then E(K)>=267, hence C(K)>=534. In particular NO member of this entire family is an own110/weak000 target with E<=249. This is not a global bound on monostatic polyhedra, not an exclusion of adjacent vertex patches, and not an exclusion of moving vertices or adding material. No new own110 was constructed or promoted. Canonical accepted own110 remains V176/E311/F137,C622.

The proof does not require weak000: one strict U alone implies the bound in this fixed deletion family. Its two cases allow deletion of the old degree44 root or retention; it does not freeze the identity of a hypothetical new root without justification.

Additional exact incidence bounds from the same certificate: independent SIMPLE-vertex deletions save at most53 edges (E>=258). Independent deletions of arbitrary-degree vertices preserving every vertex of the original stable face3 save at most119/2 edges, hence at most59 integrally (E>=252). Deleting original apex94 in an independent set saves at most59/2, hence at most29 (E>=282), even without any equilibrium requirement.

A numerical MILP found an unrestricted independent set saving65 edges. Its literal survivor hull was actually reconstructed and classified by exact A: V120/E246/F128,C492, own(S,U,H)=(60,59,117), weak000. Thus simultaneous corners can meet the complexity target while badly destroying the landscape. This exact useful negative body, not a new record, is recovered in part2.

## Mathematical proof
### Independent cap geometry
For any linear functional, the nonempty strict superlevel set of vertices of a convex polytope is connected in its true-edge graph. Every nonmaximizing vertex has an increasing incident edge by its tangent cone; iteration reaches the maximizing face, which is connected. A strict superlevel set contained in an independent set therefore has at most one vertex.

Let P be the parent and Q_i=conv(V(P) minus {i}). For independent I, Q=conv(V(P) minus I)=intersection_{i in I} Q_i. For a direction h, let a=max_Q h. The original vertices strictly above a all lie in I, hence there is at most one. Some Q_i consequently has support a, proving the support equality for the intersection (I empty is P).

The lost caps P minus Q_i have disjoint interiors for independent i,j. If x is outside Q_i, choose a separating h and a level strictly between max_Qi h and h(x). The clipped cap above that level has vertices i or points on original edges incident to i. Since i,j are nonadjacent, all those points lie in Q_j; thus x cannot be outside Q_j. This proves exact additivity of removed volume and first moments.

Each new facet of Q_i has all its vertices among ORIGINAL neighbors of i: its supporting functional has only i above its plane; every original vertex on the plane has an increasing incident edge, necessarily to i. None of these facet vertices is removed by another independent deletion. Hence every such 2D facet persists in Q. Facets from different deletions cannot coincide with the same orientation, since one would need to exclude i and the other j while each includes the other vertex. Opposite orientations on the same plane would force a lower-dimensional Q, excluded here. No such new plane is an old supporting plane of P.

The checker gives n_i distinct exactly certified new facets for each i. Every i except94 has degree<=6, and exhaustive neighbor-triple enumeration proves these lists complete. At94,42 distinct facets suffice as a LOWER bound; no completeness of a numerical nomination is needed for that case. All certified facets here are triangular and n_i=degree(i)-2.

### True-edge saving model
Every original surviving vertex stays extreme, so V(Q)=176-|I|. An original k-gon can lose at most floor(k/2) vertices under independence. Thus its 2D face disappears only when one vertex of a triangle is deleted or both opposite vertices of a quadrilateral are deleted. Faces of size>=5 survive. Write t_i for the number of original triangles incident to i, and y_i in{0,1} for deletion. With z_ij=y_i*y_j for each original quadrilateral diagonal,

  E(P)-E(Q) <= sum_i (1-n_i+t_i)y_i + sum_quad_diagonals z_ij.

Equality holds when all n_i are complete; lower counts suffice for the upper bound. Original triangle losses do not double-count because their deleted vertices are independent; each erased quadrilateral contributes exactly one diagonal product. The relaxation uses y_i+y_j<=1 on original edges, z_ij<=y_i,z_ij<=y_j, and0<=y,z<=1. For a real deletion its literal products give a feasible point. Missing lower AND inequalities only enlarge the relaxation and cannot invalidate its upper bounds.

For each model the supplied nonnegative rational duals lambda,mu are checked against EVERY coefficient: A^T lambda+mu>=c and bound=lambda.b+sum(mu). Therefore c.x<=bound for all feasible x, with no reliance on a floating solver or its optimality status. The three basic bounds are53,119/2,59/2 as stated above.

### Actual-centroid enclosure when apex94 survives
The apex-deleted bound already excludes E<=281, independently of U. In the retained-root case the caps at the other175 vertices are complete. Their exact tetrahedral volumes and first moments are computed. O is ties-to-even rounding of the ORIGINAL exact centroid on denominator10^8, merely a compact bounding reference. All individual positive volumes and absolute O-centred cap moments are rounded OUTWARD on denominator10^18 before summation. With V_L<=V<=V_U, T bounding all nonroot cap volumes and J_k their absolute moments,

  |g_Q,k-O_k| <= (V_U*|g_P,k-O_k|_upper+J_k)/(V_L-T).

The executed rational bounds display approximately (.00332796313022284,.004195829739851344,.007628465690983875), all strictly below eps=1/125. Summing incompatible caps only weakens the enclosure and is legitimate. This is the actual homogeneous centroid of every independent child retaining94, not a selected reference centre.

For each original i define J_i to contain every j!=i satisfying

  (x_i-O).(x_j-x_i)+(1/125)||x_j-x_i||_1 >=0.

The exact calculation finds450 such ordered potential chords. Every other chord is strictly negative throughout the whole centroid cube. J_94 is empty, so surviving94 is a strict U throughout the cube. For every other i, J_i contains an original neighbor of i.

If Q has only one strict U, every retained i!=94 must have a retained j in J_i, otherwise ALL its surviving chords are strictly negative. If i itself is deleted, an original neighbor belonging to J_i must survive by independence. Consequently, for EVERY original i!=94 regardless of whether it survives,

  sum_{j in J_i} y_j <= |J_i|-1.

This strengthened integral implication is essential: merely subtracting y_i on the left leaves a much weaker relaxation. Add these175 covering rows and y_94<=0 to the saving model. Its supplied rational dual proves edge saving<=44. Hence E(Q)>=311-44=267. Together with the apex-deleted case E>=282 this proves the stated ALL-independent-deletion one-U bound.

## Exact reconstruction dependencies and observed execution
This two-part capsule requires BOTH already immutable canonical source materials:
- [internal-source-reference], COORD_C622_CANONICAL_SCOPED16_Recovery_capsule_part_1_of_2.md,15305B,SHA d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa.
- [internal-source-reference], part2,20685B,SHA c4a0ef05c36066f7b2851dc18ea1c3cda599f724130ec0ce7a89785613cde5b1.
Both were read completely. Their full decoder, literal generator and core exact modules reconstruct the input without an old sandbox. This is a complete16-source computational closure, NOT the full76-file worker package. A C622-dependent fresh worker must still receive all eight FULL76 native bundles under the owner's source rule; those eight IDs were not located in this turn. No such worker was dispatched. The coordinator used the actual complete generator and needed exact code for this concrete computation; no claim to reread or replay all76 files is made.

Save RECOVER_C622_SCOPED16.py from the original source part2. Save c622_certify125.py below and the two literal JSON inputs from this new part2, with final newline. In a fresh directory run:
```
python -B -S RECOVER_C622_SCOPED16.py C622_SOURCE CANONICAL_PART1.md CANONICAL_PART2.md
python -B -S C622_SOURCE/core/RECONSTRUCT.py C622_SOURCE/GENERATOR.json C622_raw.json
python -B -S C622_SOURCE/core/check_A.py C622_raw.json C622_A.json
python -B -S c622_certify125.py
```
These reconstruction and certificate commands actually ran. Python3.13.5 standard library, assertions enabled. Canonical raw15437B/SHA ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5; C622_A.json311825B/SHA142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0. This single original A computation supplies exact geometry/mass; it is not a newly claimed independent second hull engine.

Observed terminal (literal spelling): J125_C622_ALL_INDEPENDENT_DELETIONS_U1_IMPLES_E_GE_267_EXACT_PASS_NO_110.
Output C622_INDEPENDENT125_EXACT.json2219B/SHA129b8660631b0eda893edf7d064516b2b82a4aa31d60062d4f8d32c3a414dd52. Exact dual matrix sizes: simple171rows/150variables; stable-protected355/201; apex-deleted444/242; one-U619/242. Bounds53,119/2,59/2,44. All coefficient slacks nonnegative rationally.

## c622_certify125.py
6897B,SHA29f06cd8962bc05515ce16d5401b17233164167c3380a5b7f6f3cdc4c4be3a0a.
```python
"""Exact fixed-input certificate: independent deletions of canonical C622.
Any full-dimensional surviving hull with exactly one strict U has E>=267.
Standard-library rational arithmetic; no optimizer is part of this proof.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import gcd,lcm
import json,sys,hashlib
sys.set_int_max_str_digits(0)
ROOT=94
SOURCE_SHA='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def canon(n,h):
 D=lcm(*(z.denominator for z in (*n,h)));v=[int(z*D)for z in (*n,h)];d=gcd(*v);return tuple(z//d for z in v)
def floorq(x,D=10**18):return F(x.numerator*D//x.denominator,D)
def ceilq(x,D=10**18):return -floorq(-x,D)
def certify_facet(i,tri,X,HX,adj):
 u,v,w=[X[j]for j in tri];n=cross(sub(v,u),sub(w,u));h=dot(n,u)
 if not any(n):return None
 if dot(n,X[i])<h:n=tuple(-z for z in n);h=-h
 if dot(n,X[i])<=h:return None
 z=canon(n,h);scores=[dot(z[:3],y[:3])-z[3]*y[3]for y in HX]
 if any(s>0 for j,s in enumerate(scores)if j!=i):return None
 face=tuple(j for j,s in enumerate(scores)if s==0);assert set(face)<=adj[i]
 assert len(face)==3,(i,face)
 return z,face

def model(a,adj,counts,mode,potential=None):
 excluded=set(a['faces'][a['stable_face_ids'][0]])if mode=='protected'else set()
 ids=[i for i in range(a['V'])if i not in excluded and(mode!='simple'or len(adj[i])==3)];idx={i:k for k,i in enumerate(ids)};pairs=[]
 for face in a['faces']:
  if len(face)==4:
   for i,j in [(face[0],face[2]),(face[1],face[3])]:
    if i in idx and j in idx:pairs.append((i,j))
 c=[1-counts[i]+sum(i in f for f in a['faces']if len(f)==3)for i in ids]+[1]*len(pairs);rows=[];b=[]
 for i,j in a['edges']:
  if i in idx and j in idx:rows.append({idx[i]:1,idx[j]:1});b.append(1)
 for k,(i,j)in enumerate(pairs):
  for t in [i,j]:rows.append({len(ids)+k:1,idx[t]:-1});b.append(0)
 if mode=='apex_deleted':rows.append({idx[ROOT]:-1});b.append(-1)
 if mode=='one_U':
  assert ids==list(range(a['V'])) and potential is not None and not potential[ROOT]
  for i in range(a['V']):
   if i==ROOT:continue
   J=potential[i];assert set(J)&adj[i]
   rows.append({idx[j]:1 for j in J});b.append(len(J)-1)
  rows.append({idx[ROOT]:1});b.append(0)
 return ids,pairs,c,rows,b

def check_dual(c,rows,b,w):
 lam=[F(0)]*len(rows);mu=[F(0)]*len(c)
 for name,dest in [('lambda_sparse',lam),('mu_sparse',mu)]:
  seen=set()
  for i,s in w[name]:assert i not in seen and 0<=i<len(dest);seen.add(i);dest[i]=F(s)
 assert min(lam)>=0 and min(mu)>=0
 cover=list(mu)
 for weight,row in zip(lam,rows):
  for j,v in row.items():cover[j]+=weight*v
 assert all(v>=x for v,x in zip(cover,c))
 bound=dot(lam,b)+sum(mu);assert bound==F(w['bound'])
 return dict(bound=str(bound),rows=len(rows),variables=len(c),nonzero_lambda=sum(x!=0 for x in lam),nonzero_mu=sum(x!=0 for x in mu),min_dual_slack=str(min(v-x for v,x in zip(cover,c))))

def main():
 raw=Path('C622_A.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA;a=json.loads(raw)
 assert [a[k]for k in ('V','E','F')]==[176,311,137] and a['counts']==[1,1,0] and a['unstable_vertices']==[ROOT]
 nom=json.loads(Path('C622_DUAL125_NOMINATION.json').read_text());esc=json.loads(Path('C622_ESCAPE125_NOMINATION.json').read_text())
 X=[tuple(map(F,x))for x in a['raw_vertices']];HX=[]
 for x in X:
  d=lcm(*(z.denominator for z in x));HX.append(tuple(int(z*d)for z in x)+(d,))
 adj=[set()for _ in X]
 for i,j in a['edges']:adj[i].add(j);adj[j].add(i)
 assert len(nom['cap_triangles'])==len(X);facets=[]
 for i,tris in enumerate(nom['cap_triangles']):
  ff={}
  for tri in tris:
   result=certify_facet(i,tri,X,HX,adj);assert result is not None;z,face=result;assert z not in ff;ff[z]=face
  if i!=ROOT:
   complete={}
   for tri in combinations(sorted(adj[i]),3):
    result=certify_facet(i,tri,X,HX,adj)
    if result is not None:complete[result[0]]=result[1]
   assert complete==ff
  facets.append(ff)
 counts=list(map(len,facets));assert all(n==len(adj[i])-2 for i,n in enumerate(counts))
 proofs={}
 for w in nom['certificates']:
  ids,pairs,c,rows,b=model(a,adj,counts,w['mode']);proofs[w['mode']]=check_dual(c,rows,b,w)
 assert F(proofs['apex_deleted']['bound'])==F(59,2)
 # For a retained root, cap losses have no contribution from its large cap.
 V=F(a['ordinary_volume']);g=tuple(map(F,a['raw_centroid']));O=tuple(F(round(z*10**8),10**8)for z in g);eps=F(1,125);T=F(0);J=[F(0)]*3
 for i,ff in enumerate(facets):
  if i==ROOT:continue
  dv=F(0);m=[F(0)]*3
  for face in ff.values():
   u,v,w=[X[j]for j in face];d=abs(dot(sub(u,X[i]),cross(sub(v,X[i]),sub(w,X[i]))))/6;assert d>0;dv+=d
   for k in range(3):m[k]+=d*(X[i][k]+u[k]+v[k]+w[k])/4
  T+=ceilq(dv)
  for k in range(3):J[k]+=ceilq(abs(m[k]-dv*O[k]))
 VL=floorq(V);VU=ceilq(V);assert VL>T
 drift=[(VU*ceilq(abs(g[k]-O[k]))+J[k])/(VL-T)for k in range(3)];assert max(drift)<eps
 potential=[];excluded_pairs=0;closest=None;closest_pair=None
 for i,x in enumerate(X):
  row=[]
  for j,y in enumerate(X):
   if i==j:continue
   d=sub(y,x);upper=dot(sub(x,O),d)+eps*sum(map(abs,d))
   if upper>=0:row.append(j)
   else:
    excluded_pairs+=1
    if closest is None or upper>closest:closest=upper;closest_pair=[i,j]
  potential.append(row)
 assert potential==esc['potential'] and esc['eps']==str(eps)
 ids,pairs,c,rows,b=model(a,adj,counts,'one_U',potential);proofs['one_U']=check_dual(c,rows,b,esc);assert F(proofs['one_U']['bound'])==44
 out=dict(name='J125_C622_INDEPENDENT_DELETION_ONE_STRICT_U_IMPLIES_E_GE_267',source_sha256=SOURCE_SHA,cap_facet_counts=counts,reference_O=[str(z)for z in O],centroid_cube_radius=str(eps),all_nonroot_cap_volume_upper=str(T),parent_volume_lower=str(VL),parent_volume_upper=str(VU),nonroot_cap_absolute_moment_upper=[str(z)for z in J],uniform_centroid_drift_bounds=[str(z)for z in drift],drift_display=[float(z)for z in drift],potential_chord_count=sum(map(len,potential)),strictly_excluded_chord_count=excluded_pairs,closest_excluded_pair=closest_pair,closest_excluded_upper=str(ceilq(closest)),proofs=proofs,conclusion='For EVERY independent subset of the original C622 true-edge graph, any full-dimensional unmoved-survivor convex hull with exactly ONE strict unstable vertex has E>=267 (C>=534). This excludes own110 with E<=249 in this family, not adjacent deletions or changed coordinates.')
 data=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('C622_INDEPENDENT125_EXACT.json').write_bytes(data)
 print('DUALS',proofs);print('BOX',out['drift_display'],'ARCS',out['potential_chord_count']);print('OUTPUT',len(data),hashlib.sha256(data).hexdigest())
 print('J125_C622_ALL_INDEPENDENT_DELETIONS_U1_IMPLES_E_GE_267_EXACT_PASS_NO_110')
if __name__=='__main__':main()
```

The exact inputs, sparse duals and nonwinner recovery are in this object's Recovery capsule part2/2. Both parts plus the two named canonical source materials are required. Hashes alone are not recovery data.
