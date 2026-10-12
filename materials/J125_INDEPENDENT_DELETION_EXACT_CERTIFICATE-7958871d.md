# material-7958871dd99f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J125 — every independent vertex deletion retains two strict unstable equilibria

## Exact statement and scope
Let P be the literal J124 APEX2_MATCH_G6 body, V164/E247/F85,C494, own strict121, additionalweak000, primitive000, sole positive P and Q[]. Let I be ANY independent set in its original true-edge graph, including either of its two degree-four vertices. If K=conv(vertices(P) minus I) is full dimensional, then K has at least TWO STRICT unstable vertices at its OWN uniform-volume centroid. The surviving unstable vertices need not be the original U10 or U153. No assertion about S, weak equilibria or the edge count of K is needed for this exclusion.

This rules out the complete family of unmoved, independent original-vertex deletions of this exact parent, not arbitrary vertex subsets, adjacent deletion patches, moved old vertices, or added material. It is not a global obstruction to own110 or to C<500. No new own110 was computed or promoted. The next constructive freedom is a correlated adjacent/whole-basin patch or actual geometry and mass change, not a larger search over the excluded independent family.

## Proof connecting the finite exact certificate to all subsets
For a linear functional h, a nonempty strict superlevel set of polytope vertices induces a connected graph. Every nonmaximizing vertex has an incident edge increasing h, by the tangent-cone description; iterating reaches the maximizing face, whose graph is connected. Consequently a strict superlevel set contained in an independent vertex set has at most one vertex.

Write Q_i=conv(vertices(P) minus {i}). For an independent set I, Q=conv(vertices(P) minus I) equals the intersection of Q_i, i in I. Indeed, for a support direction h and a=max_Q h, all original vertices above a are deleted and form a connected set, hence there is at most one. Thus some Q_i has support a; the intersection has the same support as Q in every direction. Empty I is P.

The lost regions P minus Q_i are disjoint for independent i,j. For x outside Q_i choose max_Qi h<a<h(x) and consider the clipped cap P intersect {h>=a}. Its vertices are i or points on original edges incident to i. None of those edges has j as an endpoint, since i and j are nonadjacent. Each cap vertex is in Q_j, so x is in Q_j. Hence x cannot lie in both lost regions. Boundary contacts have zero volume. Therefore lost homogeneous volumes and first moments add EXACTLY over I.

Each new facet exposed by deleting i uses only original neighbors of i: its supporting functional has only i strictly above its plane; every vertex on that plane must have an increasing incident edge, necessarily to i. The code enumerates every neighbor triple defining such a supporting facet and checks all other original vertices. For this parent all new facets are triangular; the 162 degree-three vertices have one cap tetrahedron each, and the two degree-four vertices have two each. Their positive tetrahedral volumes and first moments give d_i and d_i c_i exactly.

Let V,g be the original uniform volume and centroid. Choose O by exact ties-to-even rounding of g on denominator10^8; O is merely a compact bounding reference, not the assigned centre. For any independent deletion set,

  (V-sum d_i)(g_Q-O) = V(g-O)-sum d_i(c_i-O).

The code rounds every positive cap volume and every coordinate absolute cap moment OUTWARD on denominator10^15. With T bounding the sum over ALL164 individual cap volumes, J_k bounding all absolute cap moments, V_L<=V<=V_U and e_k>=|g_k-O_k|, it proves

  |g_Q,k-O_k| <= (V_U e_k+J_k)/(V_L-T) < 1/80.

This is valid even though the bound sums incompatible caps: that only enlarges the numerator and reduces the denominator. T is 0.029838958787113. The coordinate bounds display as approximately (0.011580621432323468,0.0049316042842675305,0.004169797259067262), all strictly below1/80.

The literal two disjoint blocks B1,B2 have66 and96 vertices. The code checks ALL6468 and6528 outward ordered pairs, respectively, using rational arithmetic:

  (x_i-O).(x_j-x_i)+(1/80)||x_j-x_i||_1 < 0, i in B, j outside B.

Thus at EVERY centre c in that cube, every outward chord from B is strictly negative. Worst pairs are76->56 and38->30; their upper values are below -924544990992/10^15 and -1771861398967/10^15, respectively. Each block contains an original edge, [67,77] and[120,131]. An independent deletion set cannot remove both endpoints, so each block has a surviving vertex.

In each surviving block choose a vertex x maximizing |x-c|^2. For any other surviving block vertex y,

  2(x-c).(y-x)=|y-c|^2-|x-c|^2-|y-x|^2 < 0.

The outward-block certificate handles every surviving vertex outside its block. Thus x satisfies the strict global radial support inequalities and is a strict U of Q. The blocks are disjoint, giving two distinct strict U at c=g_Q. This is a whole-basin argument allowing root turnover, not a test restricted to retaining the old U labels.

## Exact dependencies and reconstruction
Supply the complete three already immutable native source materials:
1. [internal-source-reference] J124_COMMON_APEX_RECOVERY_PART1OF2.md,13808 bytes,SHA00c8fba78bc8ab57b0fcd23a0435582536b3551fd23a64a346626d9da850d331. Its complete freeze_apex.py is1993 bytes,SHAcc69181a5423b82aa6d6942865fbe41f87a421f712602ec80a59266b6471343b.
2. [internal-source-reference] J124_COMMON_APEX_RECOVERY_PART2OF2.md,15977 bytes,SHAa1480109f3e78676a2bb770d273338513fab88172438a79b7671c94efb0b39ce. Its complete APEX2_MATCH_G6_INPUT.json is2199 bytes,SHA31a72debf79015aa68b9433ad3336c5a05b24065a44619eed1b0dd108ee20d43.
3. [internal-source-reference] J115_EXACT_AUDITOR_SOURCE.md,12486 bytes,SHAac3226f5ae6212be2bedfa4f5797dbd7fa9f4d0f1e3969c3753825a98b9ba4fc. Its entire exact115.cpp is11038 bytes,SHAd7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736.

Save the named code/data blocks below with terminal newline. Run:
```
python freeze_apex.py APEX2_MATCH_G6_INPUT.json APEX2_MATCH_G6
g++ -std=c++17 -O2 exact115.cpp -lgmpxx -lgmp -o exact115
./exact115 < APEX2_MATCH_G6.txt > APEX2_MATCH_G6_AUDIT.json 2> APEX2_MATCH_G6_AUDIT.log
python exact_deletion125.py
```
These commands actually ran in the coordinator's new computation. Assertions enabled. Python3.13.5,C++17,g++14.2.0,GMP; the new exact checker uses only the Python standard library. Parent H input reproduces3001 bytes/SHA c2f47eda1a85dbf160a5e0b82a1e86d028627d92a4955415579ad335f5dc3993. Parent audit reproduces139796 bytes/SHA86bf822bdd1b37e1215d34fb0afaa6b5692eac01743f35da9ef27e45c3714f88, with J115_EXACT_PASS. This reconstruction supplied actual data for the new deletion computation; it is not an independent second hull/mass engine.

The new observed terminal marker is J125_ALL_INDEPENDENT_VERTEX_DELETIONS_OWN_U_GE_2_EXACT_PASS_NO_110. J125_DELETION_EXACT.json is102680 bytes/SHA21cd0692682a9b6786bef3988ee011f18efaa940b4a4de77d8043023da01a792. It contains all164 exact cap-centroid rows, the cap triangulations and outward rational interval bounds, both block lists, worst crossings and the full moment bounds. This source and its exact inputs reconstruct that entire report without the originating sandbox.

## CUT125_NOMINATION.json
775 bytes,SHA8f58bc40ba8a8d7972682c699431e87ca26aee6514f73b03f92fe2d27d7aae75. The name indicates how the sets were discovered; their admissibility is checked exactly by the next program, not inferred from the numerical nomination.
```json
{"blocks": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 37, 39, 41, 42, 44, 47, 48, 49, 51, 54, 57, 58, 59, 61, 62, 63, 65, 67, 71, 72, 74, 75, 76, 77, 80, 81, 83, 84, 85, 86, 87, 95, 96], [31, 32, 36, 38, 40, 43, 45, 46, 50, 52, 53, 55, 60, 64, 66, 68, 69, 70, 73, 78, 79, 82, 88, 89, 90, 91, 92, 93, 94, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]], "cube_radius": "1/80", "edges": [[67, 77], [120, 131]]}
```

## exact_deletion125.py
5226 bytes,SHA55b30dcc1600b80eabe63fbcc60090583c4451b28b39fd6b98ebccbff595c3a6.
```python
"""Exact fixed-input certificate for all independent original-vertex deletions.
No floating-point predicate, optimizer, or original sandbox is needed.
Input is the exact J124 APEX2_MATCH_G6 audit plus a literal two-block witness.
This consumes its originating exact115 hull/mass computation, not a second engine.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,math,sys,hashlib
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def canonical(n,h):
 den=math.lcm(*(x.denominator for x in (*n,h)));v=[int(x*den)for x in (*n,h)];d=math.gcd(*v);return tuple(z//d for z in v)
def ceilq(x,D=10**15):return F(-((-x.numerator*D)//x.denominator),D)
def floorq(x,D=10**15):return F((x.numerator*D)//x.denominator,D)
def interval(x,D=10**15):return [int(x.numerator*D//x.denominator),int(x.numerator*D//x.denominator)+1,D]
def single_cap(i,X,adj):
 neighbors=sorted(adj[i]);planes={}
 for tri in combinations(neighbors,3):
  a,b,c=[X[j]for j in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  if not any(n):continue
  if dot(n,X[i])<h:n=mul(n,-1);h=-h
  if dot(n,X[i])<=h:continue
  if any(dot(n,x)>h for j,x in enumerate(X)if j!=i):continue
  face=tuple(j for j,x in enumerate(X)if j!=i and dot(n,x)==h)
  assert set(face)<=set(neighbors)
  planes[canonical(n,h)]=face
 assert planes
 dv=F(0);moment=(F(0),)*3;tetra=[]
 for row,face in sorted(planes.items()):
  # These two degree-four apices have two triangular newly exposed facets.
  # General polygon input is deliberately not silently triangulated.
  assert len(face)==3,(i,face)
  a,b,c=[X[j]for j in face];w=abs(dot(sub(a,X[i]),cross(sub(b,X[i]),sub(c,X[i]))))/6
  assert w>0;vcent=mul(add(add(a,b),add(c,X[i])),F(1,4));dv+=w;moment=add(moment,mul(vcent,w));tetra.append(list(face))
 assert len(tetra)==len(neighbors)-2
 return dv,mul(moment,1/dv),tetra

def main():
 src=Path('APEX2_MATCH_G6_AUDIT.json').read_bytes();assert hashlib.sha256(src).hexdigest()=='86bf822bdd1b37e1215d34fb0afaa6b5692eac01743f35da9ef27e45c3714f88'
 a=json.loads(src);X=[tuple(map(F,p))for p in a['vertices']];V=F(a['volume']);g=tuple(map(F,a['centroid']));edges=[tuple(e)for e in a['edges']];adj=[set()for _ in X]
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 assert Counter(map(len,adj))=={3:162,4:2};O=tuple(F(round(z*10**8),10**8)for z in g);eps=F(1,80)
 cap_data=[];T=F(0);J=[F(0)]*3
 for i in range(len(X)):
  d,c,tri=single_cap(i,X,adj);T+=ceilq(d)
  for k in range(3):J[k]+=ceilq(d*abs(c[k]-O[k]))
  cap_data.append(dict(vertex=i,degree=len(adj[i]),new_triangles=tri,volume_interval=interval(d),centroid=[str(z)for z in c]))
 VL=floorq(V);VU=ceilq(V);gerr=[ceilq(abs(g[k]-O[k]))for k in range(3)];assert VL>T
 box=[(VU*gerr[k]+J[k])/(VL-T)for k in range(3)];assert max(box)<eps
 # O is a fixed compact rational grid centre, not the actual centroid.
 witness=json.loads(Path('CUT125_NOMINATION.json').read_text());blocks=witness['blocks'];assert len(blocks)==2 and not(set(blocks[0])&set(blocks[1]))
 certificates=[]
 for Bi,edge in zip(blocks,witness['edges']):
  B=set(Bi);assert set(edge)<=B and tuple(edge)in edges
  worst=None;pair=None;count=0
  for i in sorted(B):
   p=sub(X[i],O)
   for j in range(len(X)):
    if j in B:continue
    d=sub(X[j],X[i]);upper=dot(p,d)+eps*sum(map(abs,d));assert upper<0
    count+=1
    if worst is None or upper>worst:worst=upper;pair=[i,j]
  certificates.append(dict(vertices=sorted(B),retained_edge_witness=edge,all_outward_pairs=count,worst_pair=pair,worst_upper_interval=interval(worst)))
 out=dict(name='J125_ALL_INDEPENDENT_VERTEX_DELETIONS_RETAIN_TWO_STRICT_U',source='APEX2_MATCH_G6',VEF=[a[z]for z in ['V','E','F']],reference_O=[str(z)for z in O],centroid_cube_radius=str(eps),original_centroid_errors_upper=[str(x)for x in gerr],all_individual_cap_volume_upper=str(T),parent_volume_lower=str(VL),parent_volume_upper=str(VU),all_cap_absolute_moment_upper=[str(z)for z in J],uniform_subset_centroid_coordinate_bounds=[str(z)for z in box],mass_bounds_display=[float(z)for z in box],caps=cap_data,blocks=certificates,conclusion='Every full-dimensional conv of surviving original vertices after any independent original-graph vertex deletion has at least two STRICT unstable vertices at its OWN uniform-volume centroid. No bound on S, weak equilibria, or edge count is asserted.',scope='Fixed literal body and unmoved surviving vertices. Adjacent deletion sets, moved old vertices, and added material are not excluded.')
 b=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('J125_DELETION_EXACT.json').write_bytes(b)
 print('CAPS',len(cap_data),'TUP',float(T),'BOX',list(map(float,box)))
 print('BLOCKS',[(len(z['vertices']),z['all_outward_pairs'],z['worst_pair'],z['worst_upper_interval'])for z in certificates])
 print('OUTPUT',len(b),hashlib.sha256(b).hexdigest());print('J125_ALL_INDEPENDENT_VERTEX_DELETIONS_OWN_U_GE_2_EXACT_PASS_NO_110')
if __name__=='__main__':main()
```

## Relationship to the earlier separation theorem
The full archived coordinator material [internal-source-reference],SHA cad1d91f3c5664e6f261061af08d5532eed3367d89282a8a256990f651ac8d4a, was read completely before this computation. It derives graph-separated connected-patch intersection, additive moments, an exact common-centre equilibrium-set identity and pairwise edge-saving synergy. This new result executes a concrete whole-basin obstruction for the simplest independent-vertex family on J124; it does not refute that more general patch mechanism or require a reconstruction of C622. Numerical producing units are preserved separately; the exact certificate above does not depend on rerunning a floating solver.
