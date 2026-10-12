# minimum-0043

AI research report · 2026-09-10 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA54_C32_MP45_103_GENUINE_TRANSPORTS_V1

## 1. Determination

**There are exactly103 canonical C32 types admitting a genuine same-vertex cofacial boundary triangulation isomorphic to the literal parent MP9:45 sphere. Every homogeneous convex realization of each of those103 types has at least two strict unstable vertices at its own uniform-volume centroid, for every positive-definite physical metric.**

Of these, **99 are new whole-type exclusions** relative to the specified accepted17. The four inherited overlaps are `{33,34,293,294}`. The combined whole-type set therefore has **116 types**, leaving **180 types not wholly excluded by that union**. Every vertex root and every actual stable-facet choice is covered in each new whole type. No additional partial-only root exclusion is claimed.

The direct transport frontier of this parent is **exhausted**, not merely sampled. I checked all20349 five-edge deletion choices in the parent sphere and independently checked all12912 labelled products of genuine polygon triangulations across the complete canonical296 catalogue. These routes agree on1269 parent-labelled coarsenings,121 matching canonical-labelled refinements and1452 complete vertex bijections. Every positive witness is certified as a collection of oriented, noncrossing polygonal disks, with exact true-edge containment and actual flat-cell accounting.

The remaining193 types have **no direct transport of this specified kind**, in any realization retaining their stated maximal-facet lattice. Thirteen of those193 were already wholly excluded by other accepted results; the exact remaining180 are listed in Section8. Failure of this transport is not physical feasibility, and does not reverse inherited partial-root exclusions.

The inherited bound remains **32<=C_min<=1374**. There is no C32 attainer, no C>=34 theorem, and no restoration of the old57-type or MP9:30/48 claims.

## 2. Authority and exact inputs

The sole physical theorem parent is `minimum-0041`, `NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4`, SHA-256 `9a59df6d6b44ecb690b30e3711222fc549b3553f268e6b90a2c37c0ff728ceae`. It covers all nine roots, genuine cofacial boundary triangulations, actual zero-volume cells, weak escapes, norm ties and arbitrary SPD metrics. Its own `canonical_C32_transports=[]` is respected: the canonical transports below are new.

I authenticated the parent's45936-byte compact UTF-8 version2 JSON envelope, with the Markdown's final LF included, from `research-journal(8).md`:

```
3543813 bytes
b5a6d65bcaa9b885046083b25e6202ac01c4c1f3a42b757fcffd20b3d2200216
```

The literal parent facets, indexed0 through13, remain

```
014,021,032,043,125,154,235,347,365,376,458,487,568,678.
```

Its21 graph edges are

```
01,02,03,04,12,14,15,23,25,34,35,36,37,45,47,48,56,58,67,68,78.
```

The strict parent sphere has `(V,E,F)=(9,21,14)`. **It is not canonical C32:45 or C32:139.** Canonical45 is newly excluded below by an explicit polygon/vertex/triangle map, not by renaming the parent. Canonical139 has no direct transport to this sphere and retains its separate inherited exclusion.

The complete canonical296 input is the unchanged `C32_POLYHEDRAL_MAP_CATALOGUE_V1`:

```
c32_catalogue.json
240929 bytes
efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d
```

The journal's6337-byte `recover_c32_complete.py`, SHA-256 `35da62544738dbc2177f4c6ef09768d41b5fd208bd6042006421481b9d9168a0`, was recovered literally and run. Its generator and independent completeness/orbit checker reproduced all advertised pins and the642-byte transcript SHA-256 `0b6c9fc3c56411623406c54b3f6ae8f707cc402635adc0ae635ef2d98f21e743`. The baseline is296 unoriented three-connected spherical maps with `(9,16,9)`,50 self-dual types and21682 joint vertex/facet root orbits; its source-only recovery is part of the supplied journal.

No new parent/source/label conflict was found. **I did not rerun root0, root3, their numerical locators, or the old multimillion-tree search.** This work applies the immutable physical theorem and computes the previously missing geometric-combinatorial transport. The separate complementary-matching frontier is neither regenerated nor used as a new premise.

## 3. Exhaustion in both directions

### Parent-to-catalogue enumeration

A C32 map has16 true edges. Any boundary refinement isomorphic to the21-edge parent must add exactly5 diagonals. The first enumeration therefore examines every subset of5 parent edges, exactly

`binom(21,5)=20349`.

Of these,17889 leave a vertex of degree below3, and1191 of the remaining choices fail three-connectivity. These cannot be graphs of the required convex polytope. The1269 survivors are processed without an incidence guess: remove the chosen edges, merge their incident oriented triangles, recover every boundary cycle, and certify each resulting component as a disk with no interior vertices and noncrossing diagonals. Every survivor is a nine-polygon sphere with all nine vertices and exactly16 remaining edges.

The catalogue's rooted-dart canonical labeling, including both orientations, identifies the canonical type. The generator also recovers the actual inverse vertex permutation rather than only a canonical graph key. Composing it with every canonical-map automorphism gives all1452 canonical-to-parent vertex bijections. There are114 orbits of parent-labelled deletions under the parent's twelve automorphisms, distributed across103 canonical types.

### Catalogue-to-parent verification

A separately written checker imports neither the transport generator nor the catalogue canonicalization engine. For each of the296 literal polygonal maps, it recursively enumerates **every** triangulation of each convex polygon from its cyclic vertex list. A k-gon contributes exactly `Catalan(k-2)` triangulations, independently checked against the binomial formula. Cartesian products over all nine facets give12912 labelled refinements in total. An independent ear-removal checker validates the polygon disks and their orientations.

For each refinement, every possible face isomorphism to the parent is covered. The image of one oriented source triangle has84 possibilities:14 target triangles, three cyclic starting points and either orientation. Propagation across adjacent triangles uniquely determines the rest of a map. Necessary degree tests may reject a candidate early, but no possible bijection is omitted. This covers all relevant relabelings without presuming that one arbitrary graph embedding is the correct one.

Exactly121 refinements match, each with12 target automorphisms, giving1452 maps. The other12791 refinements do not match. The matching-refinement counts per canonical type are

```
193 types: 0
 86 types: 1
 16 types: 2
  1 type : 3
```

The checker recovers the entire parent-labelled deletion ledger from these forward maps and compares the **complete map sets**, not just their counts. It additionally repeats all20349 deletion connectivity tests with a different set/DFS implementation. The three-channel ledger is therefore closed:

```
20349 deletion choices = 17889 degree failures + 1191 two-cut failures + 1269 valid coarsenings
12912 polygon refinements = 12791 nonmatches + 121 matches
121 matches x 12 parent automorphisms = 1452 complete vertex maps
103 direct whole types = 99 new + 4 inherited overlaps
```

The verified per-refinement stream, including all nonmatches, has SHA-256

`ba1d90de1bea60f05f50350ee757baac6fa6b74c26675b12b2ea37267d684a86`.

### Why the negative transport result is whole-domain

Any genuine flat boundary triangle of a convex polytope lies in a maximal supporting facet. A no-new-vertex triangulation of its boundary therefore induces a triangulation of each actual maximal polygon, and retains every true edge. Conversely, every certified noncrossing triangulation of a convex polygon is geometric in **every** realization of that polygon's cyclic face lattice. Thus transport existence here is exactly the finite predicate checked above; it is not a generic-coordinate property with a missed exceptional shape. The193 negative types may admit other useful refinements or other physical theorems, but none admits this particular parent refinement under the stated rules.

## 4. Why each positive map is a whole-realization physical theorem

Fix one of the literal witnesses in Section6 and any full-dimensional homogeneous convex realization `P=conv(v_0,...,v_8)` with exactly those actual maximal-facet cycles. All nine listed points must be actual vertices. Its facets are strictly convex polygons: a collinear intermediate point or a point inside another face is not an actual vertex ofP.

Each witness partitions the14 parent triangles into nine groups. After the displayed vertex relabeling and, if indicated, one common orientation reversal, a group is an oriented noncrossing triangulation of the corresponding actual polygon. The checks include its boundary cycle, paired internal edges, connected triangle adjacency, Euler characteristic1, no interior vertices, and a separate ear-removal verification. Convexity then makes the triangles nondegenerate with disjoint interiors and exactly the full polygon as their union, throughout every realization of the type. Adjacent polygons meet on their actual common edges; their orientations agree as an oriented sphere.

No vertex is inserted, removed or moved. The solid, its uniform density, its volume centroid and its physical metric are **literally unchanged**. The sixteen true edges map to sixteen of the parent's21 edges. The other five edges are identified as internal polygon diagonals and are never asserted to be available physical escapes.

Translate by the actual solid centroid and let `X` have the centered vertex rows. For any common SPD metricM, put `G=X M X^T`. If there were a sole strict unstable vertexr, each other vertex would supply a weak escape along a **true edge**, with

```
D_i=x_i^T M(x_p(i)-x_i)>=0.
```

Distinct endpoints imply

```
||x_p(i)||_M^2-||x_i||_M^2
  =2D_i+||x_p(i)-x_i||_M^2>0.
```

These arrows form a rooted spanning tree contained in the parent graph. No diagonal is chosen to manufacture such a tree, and no extra comparison between incomparable norms is imposed. The immutable whole-parent theorem excludes every possible image root `pi(r)` using the same body and metric.

### Common actual masses and the zero-cone boundary

For every distinct parent cell `t={a,b,c,d}` use one common actual determinant mass

`d_t=|det(x_b-x_a,x_c-x_a,x_d-x_a)|`.

The63 cells are the union of all nine genuine apex fans. A cell has the same mass in every occurrence; fan incidence is not mistaken for volume. With `f_at` its fan indicator, `chi_t` its vertex indicator, `J_t=chi_t chi_t^T+diag(chi_t)` and `D=6 Vol(P)>0`, the actual simplex formulas give

```
Σ_t f_at d_t = D,
X^T Σ_t f_at d_t chi_t = 0,
Σ_t f_at d_t X^T J_t X = 20 D Cov(P).
```

All components of the same covariance tensor are retained. The sum over the union of distinct cells is not asserted equal toD.

Cone every boundary triangle not containing the apex, **including triangles elsewhere in the same actual facet as the apex**. Such cofacial cones have exactly zero determinant and zero moments; they stay in the ledger. A nonincident supporting facet has a strict supporting-plane gap at the apex, so its cone has positive determinant magnitude. Thus each cell's zero/nonzero status is determined exactly by the displayed actual-facet ownership, with no fitted positive weights and no genericity assumption.

The full oriented parent chain complex is unchanged by the vertex permutation and common orientation sign. For every boundary-cycle relationbeta, the same actual masses satisfy

```
Σ_t beta_t d_t = 0,
X^T Σ_t beta_t d_t chi_t = 0,
Σ_t beta_t d_t X^T J_t X = 0.
```

One proof integrates polynomial moments over the associated closed oriented tetrahedral chain: boundary fluxes cancel, using `div(x q(x)/(3+deg q))=q(x)` for a homogeneous polynomialq. Flat cells contribute zero. This transports the **complete** cycle identities, not merely selected scalar moment constraints.

Consequently every positive-definite contradiction in the parent is applicable with the body's actual determinants and common first/second moments. Nothing in this argument asserts that an independently feasible mass system is physical. Exceptional moment-rank strata require no deletion or division by a minor because actual determinants are substituted directly.

### Continuous domain and all ties

The closure holds for **every** set of real vertex coordinates giving a full-dimensional convex polytope with the stated exact maximal-facet cycles, and **every** real symmetric positive-definite3-by-3 metric, at that body's own uniform-volume centroid. There is no coordinate box, conditioning bound, rational-coordinate restriction, positive lower bound on cone masses, or norm-order restriction. Every weak-escape equality and norm tie is included. No affine frame, especially0123, is fixed; hence its possible zero determinant is not an omitted branch.

Different limiting maximal-face lattices are not silently called the original canonical type. They are covered by this parent as well whenever their same nine actual vertices and the displayed triangles still form a genuine boundary triangulation, but no additional canonical-type count is inferred from that observation. Nonuniform densities, nonvertices, lower-dimensional hulls and singular metrics are outside the theorem.

## 5. An additional exact geometric consequence: a triangulation-independent flat-mass count

For a convex k-gon triangulated without new vertices, the union of all vertex-apex fan cells lying in its plane contains exactly

`(k-3)^2`

distinct flat four-sets. There are `(k-2)(k-3)` occurrences: each of thek-2 triangles can be coned from each of its otherk-3 polygon vertices. A four-set appears twice precisely when it is the union of the two triangles adjacent to one of thek-3 internal diagonals. No four convex polygon vertices support three selected triangulation triangles. Subtracting those duplicate occurrences gives `(k-3)^2`.

Different actual facets cannot share a four-set, because two distinct facets of a convex three-polytope meet in at most an edge. Therefore every transport of a C32 type with facet sizesk_j has exactly

```
z = Σ_j (k_j-3)^2  distinct zero determinant masses,
z+5               zero cone occurrences among the84 parent fan occurrences,
63-z               positive distinct determinant masses.
```

Here `Σ_j(k_j-3)=32-27=5`. This is an exact all-realization count, not a numerical control. The generator checks the complete zero ledger for all1452 transports, and the independent checker reconstructs it for each chosen literal witness.

| Actual facet-size profile | Transportable types | Distinct zero masses | Positive masses |
|---|---:|---:|---:|
|Four triangles, five quadrilaterals|21|5|58|
|Five triangles, three quadrilaterals, one pentagon|50|7|56|
|Six triangles, one quadrilateral, two pentagons|15|9|54|
|Six triangles, two quadrilaterals, one hexagon|15|11|52|
|Seven triangles, one pentagon, one hexagon|2|13|50|

No other facet-size profile in canonical296 admits this parent transport. The zero masses are never replaced by positive lower bounds, and all nonzero masses remain common actual determinants.

## 6. Complete literal canonical polygon and root/triangle maps

Each row below is a whole-type witness. The fields are:

`id | F0,...,F8 | pi(0)...pi(8) | o(0)...o(13) | orientation | status`.

Every vertex/facet label is a single digit0 through8. Polygon strings are the complete oriented canonical cycles. The nine-characterpi string maps **canonical vertices and unstable roots to parent labels**. The fourteen-charactero string assigns each parent triangle, in the fixed parent order, to its actual canonical maximal facet. The orientation is that of pulled-back parent triangles relative to the canonical cycles.

Reconstruction is literal: for facetf take exactly `{pi^-1(T_j):o(j)=f}`, reversing all triples together when the sign isminus. A joint root `(r,f)` is mapped to `(pi(r),{j:o(j)=f})`; the second entry is the full polygon's triangle group, **not** a claim that its individual triangles are separate stable facets. The parent excludes the unstable root independently of the stable-facet choice, so all nine vertex roots and all81 labelled vertex/facet choices are closed for every row.

`NEW` marks precisely the99 additions. The four rows marked `inherited` add no whole type to the prior register. The same complete table is frozen as7910 bytes/SHA-256 `7fcc294ca52348f3911f285dc2473c7d89bf9647b8458967e3f3a9d885e163f2` and is independently parsed back against the verified witnesses.

```text
id|canonical facets F0..F8|canonical-to-parent vertices and roots|parent triangles 0..13 to facet|orientation|status
0|013,0241,0352,1463,2574,3685,476,587,678|012453867|01221345473568|+|NEW
3|013,0241,0352,1463,254,3685,457,4786,587|012453867|01221345683577|+|NEW
4|013,0241,0352,1463,254,3685,4587,476,678|012453867|01221345663578|+|NEW
10|013,0241,0352,14763,254,3685,457,587,678|012453867|01221345673538|+|NEW
12|013,0241,0352,14763,254,365,4587,568,678|012453786|01221345673368|+|NEW
13|013,0241,0352,14763,2584,365,487,568,678|012453786|01221345473368|+|NEW
15|013,0241,0352,14763,254,3685,458,487,678|012453786|01221345653378|+|NEW
16|013,0241,0352,14763,254,365,458,487,5678|012453786|01221345683378|+|NEW
17|013,0241,0352,143,25874,346,3685,476,678|012453867|01221346445678|+|NEW
19|013,0241,0352,143,2574,3476,3685,587,678|012453867|01221346475658|+|NEW
21|013,0241,0352,143,25874,3476,365,568,678|012453786|01221346475548|+|NEW
22|013,0241,0352,143,254,3476,3685,4587,678|012453786|01221346765578|+|NEW
23|013,0241,0352,143,2584,3476,3685,487,678|012453786|01221346465578|+|NEW
24|013,0241,0352,143,2584,3476,365,487,5678|012453786|01221346485578|+|NEW
26|013,0241,0352,1473,25874,365,376,568,678|012453786|01221345473648|+|NEW
27|013,0241,0352,1473,254,3685,376,4587,678|012453786|01221345753678|+|NEW
29|013,0241,0352,1473,25684,365,376,487,678|012453786|01221345443678|+|NEW
30|013,0241,0352,1473,2584,3685,376,487,678|012453786|01221345453678|+|NEW
31|013,0241,0352,1473,2584,365,376,487,5678|012453786|01221345483678|+|NEW
32|013,0241,0352,1473,2584,365,3786,487,568|012453786|01221345483676|+|NEW
33|013,0241,0352,1473,2584,365,376,4867,568|012453786|01221345483677|+|inherited
34|013,0241,0352,1473,254,365,3786,4568,487|012453786|01221345773686|+|inherited
35|013,0241,0352,1473,254,3685,376,458,4867|012453786|01221345753688|+|NEW
37|013,0241,0352,14873,2584,365,376,568,678|012453786|01221345473638|+|NEW
39|013,0241,0352,14873,254,365,376,4568,678|012453786|01221345773638|+|NEW
40|013,0241,0352,14873,254,365,376,458,5678|012453786|01221345783638|+|NEW
42|013,0241,0352,143,25874,347,3685,376,678|012453786|01221346465748|+|NEW
43|013,0241,0352,143,25874,347,365,3786,568|012453786|01221346485747|+|NEW
44|013,0241,0352,143,25684,347,365,3786,487|012453786|01221346445787|+|NEW
45|013,0241,0352,143,2584,347,3685,376,4867|012453786|01221346465788|+|NEW
46|013,0241,0352,143,25684,3487,365,376,678|012453786|01221346445758|+|NEW
47|013,0241,0352,143,2584,3487,365,376,5678|012453786|01221346485758|+|NEW
55|013,0241,036852,1463,254,457,476,587,678|012453867|01221342573268|+|NEW
59|013,0241,03652,1463,2584,476,487,567,578|013246587|10213324245678|-|NEW
64|013,0241,03652,14763,254,458,487,568,678|012453786|01221342573368|+|NEW
66|013,0241,036852,143,2574,346,476,587,678|012453867|01221342475268|+|NEW
67|013,0241,03652,143,2574,346,4786,568,587|014257386|10223152674468|-|NEW
69|013,0241,036852,143,254,346,457,4786,587|012453867|01221342685277|+|NEW
70|013,0241,036852,143,254,346,4587,476,678|012453867|01221342665278|+|NEW
71|013,0241,036752,143,2584,346,476,487,578|014257368|10223152624478|-|NEW
74|013,0241,036852,143,254,3476,457,587,678|012453867|01221342675258|+|NEW
76|013,0241,03652,143,254,3476,4587,568,678|012453786|01221342675568|+|NEW
77|013,0241,03652,143,2584,3476,487,568,678|012453786|01221342475568|+|NEW
78|013,0241,03652,143,2584,3476,487,567,578|014257368|10223152574468|-|NEW
79|013,0241,036852,143,254,3476,458,487,678|012453786|01221342625578|+|NEW
82|013,0241,03652,1473,254,376,4587,568,678|012453786|01221342673568|+|NEW
83|013,0241,03652,1473,2584,376,467,486,568|307246518|33015621227484|-|NEW
85|013,0241,03652,1473,2584,376,487,568,678|012453786|01221342473568|+|NEW
87|013,0241,03652,1473,254,376,4568,487,678|012453786|01221342663578|+|NEW
88|013,0241,036852,1473,254,376,458,487,678|012453786|01221342623578|+|NEW
89|013,0241,03652,1473,254,376,458,487,5678|012453786|01221342683578|+|NEW
90|013,0241,03652,1473,254,3786,458,487,568|012453786|01221342683575|+|NEW
91|013,0241,03652,1473,254,376,458,4867,568|012453786|01221342683577|+|NEW
93|013,0241,03652,14873,254,376,458,568,678|012453786|01221342673538|+|NEW
98|013,0241,03652,143,25874,347,376,568,678|012453786|01221342475648|+|NEW
99|013,0241,036852,143,254,347,376,4587,678|012453786|01221342725678|+|NEW
100|013,0241,03652,143,2584,347,376,487,5678|012453786|01221342485678|+|NEW
101|013,0241,03652,143,2584,347,3786,487,568|012453786|01221342485676|+|NEW
102|013,0241,036852,143,254,347,376,458,4867|012453786|01221342725688|+|NEW
103|013,0241,03652,143,2584,3487,376,568,678|012453786|01221342475658|+|NEW
105|013,0241,03652,143,254,3487,376,4568,678|012453786|01221342775658|+|NEW
119|013,0241,032,1463,23685,2574,476,587,678|013247586|10213345446587|-|NEW
120|013,0241,032,1463,2365,2574,4786,568,587|013246578|10213345456678|-|NEW
122|013,0241,032,1463,23675,2584,476,487,578|013246587|10213345456748|-|NEW
124|013,0241,032,14763,23685,254,457,587,678|013247586|10213345443687|-|NEW
128|013,0241,032,14763,2365,2584,487,567,578|013246587|10213345453678|-|NEW
138|013,0241,0362,1463,2574,2685,476,587,678|013247586|10213324556487|-|NEW
140|013,0241,0362,14763,254,2685,457,587,678|013247586|10213324553687|-|NEW
143|013,0241,0362,143,254,2685,34786,457,587|014258367|10223165664578|-|NEW
144|013,0241,0362,143,2584,2675,3476,487,578|014257368|10223165654478|-|NEW
157|013,0241,0362,14873,254,2675,376,458,578|034278156|22016531335487|+|NEW
165|013,0241,03762,1473,254,265,4568,487,678|013247658|10213324257686|-|NEW
166|013,0241,03762,1473,254,2685,458,487,678|013247658|10213324257685|-|NEW
167|013,0241,03762,14873,254,265,458,568,678|013247658|10213324253687|-|NEW
170|013,0241,037862,143,254,265,347,4587,568|014258736|10223162724578|-|NEW
171|013,0241,03762,143,254,265,3487,4568,678|014258736|10223162684577|-|NEW
172|013,0241,03762,143,254,2685,3487,458,678|014258736|10223162684575|-|NEW
173|013,0241,03762,143,254,265,3487,458,5678|014258736|10223162684578|-|NEW
194|013,02541,032,1463,23685,457,476,587,678|013247586|10213341446587|-|NEW
195|013,025841,032,1463,2365,476,487,567,578|013246587|10213341415678|-|NEW
208|013,025841,0362,143,2675,346,476,487,578|014257368|10223154641178|-|NEW
209|013,02541,0362,143,2685,3476,457,587,678|014258367|10223154581467|-|NEW
212|013,025841,0362,143,265,3476,487,567,578|014257368|10223154571168|-|NEW
242|013,02541,03762,143,265,347,4587,568,678|014258736|10223152681467|-|NEW
243|013,025841,03762,143,265,347,487,568,678|014258736|10223152681417|-|NEW
244|013,025841,03762,143,265,347,487,567,578|307218654|13015621228174|-|NEW
245|013,02541,03762,143,265,347,4568,487,678|014258736|10223152781466|-|NEW
246|013,02541,03762,143,2685,347,458,487,678|014258736|10223152781464|-|NEW
247|013,02541,03762,143,265,347,458,487,5678|014258736|10223152781468|-|NEW
248|013,02541,03762,143,265,347,458,4867,568|014258736|10223152771468|-|NEW
250|013,02541,03762,143,265,3487,458,568,678|014258736|10223152581467|-|NEW
253|013,025841,032,1463,236,2675,476,487,578|013246587|10213341516758|-|NEW
254|013,02541,032,14763,236,2685,458,487,678|031274568|12014531335687|+|NEW
261|013,02541,032,1473,2376,265,4568,487,678|013247658|10213341457686|-|NEW
262|013,02541,032,1473,2376,2685,458,487,678|013247658|10213341457685|-|NEW
263|013,02541,032,1473,2376,265,458,487,5678|013247658|10213341457688|-|NEW
264|013,02541,032,1473,23786,265,458,487,568|013247658|10213341457648|-|NEW
265|013,02541,032,1473,2376,265,458,4867,568|013247658|10213341457678|-|NEW
268|013,02541,0372,1483,265,276,387,456,4678|306247851|33016821218754|-|NEW
271|013,021,03652,124,1473,2584,376,487,5678|012453786|01223452584678|+|NEW
272|013,021,03652,124,14873,2584,376,568,678|012453786|01223452574648|+|NEW
293|013,0251,0372,1483,154,265,2786,387,4568|034267815|22017631346588|+|inherited
294|013,0251,0372,1483,154,2645,2786,387,468|013452678|01124352563786|+|inherited
```

## 7. Worked distinction: canonical C32:45 is now closed, not renamed

Canonical45 has the nine actual polygon cycles

```
013,0241,0352,143,2584,347,3685,376,4867.
```

Its witness is

```
pi = [0,1,2,4,5,3,7,8,6]
o  = [0,1,2,2,1,3,4,6,4,6,5,7,8,8]
orientation = +1.
```

The actual polygons correspond, in their canonical order, to the parent-triangle groups

```
[0], [1,4], [2,3], [5], [6,8], [10], [7,9], [11], [12,13].
```

The only added parent-label edges are

```
03,12,35,37,68.
```

They are genuine internal diagonals, not physical escape edges. The exactly flat parent four-sets are

```
0125,0234,2356,3467,5678.
```

All other58 used determinant masses are positive for every realization retaining these actual maximal faces. The body and its centroid do not change when those five polygons are triangulated. The parent's all-root theorem therefore excludes a unique strict unstable vertex at **each** of canonical45's nine vertices, for every SPD metric. This is an explicit new whole-canonical45 consequence; it is neither an alias of the parent nor a restoration of an old coarsening claim.

## 8. Exact whole-type complement and root accounting

The specified inherited whole set is

```
33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295.
```

Its overlap with the103 direct transports is exactly

```
33,34,293,294.
```

The inherited types outside the direct transport domain are exactly

```
72,139,149,152,159,163,164,178,192,217,284,288,295.
```

The complete complement of the **116 whole-type union**, containing180 canonical IDs, is

```
1,2,5,6,7,8,9,11,14,18,20,25,28,36,38,41,48,49,50,51,52,53,54,56,57,58,
60,61,62,63,65,68,73,75,80,81,84,86,92,94,95,96,97,104,106,107,108,109,
110,111,112,113,114,115,116,117,118,121,123,125,126,127,129,130,131,132,
133,134,135,136,137,141,142,145,146,147,148,150,151,153,154,155,156,158,
160,161,162,168,169,174,175,176,177,179,180,181,182,183,184,185,186,187,
188,189,190,191,193,196,197,198,199,200,201,202,203,204,205,206,207,210,
211,213,214,215,216,218,219,220,221,222,223,224,225,226,227,228,229,230,
231,232,233,234,235,236,237,238,239,240,241,249,251,252,255,256,257,258,
259,260,266,267,269,270,273,274,275,276,277,278,279,280,281,282,283,285,
286,287,289,290,291,292.
```

The193-type **no-direct-transport** set is exactly the disjoint union of this180 list and the preceding13 inherited-outside-direct list. Both complete arrays are also generated and independently checked in the report. There is no unexamined triangulation, relabeling or special-shape remainder in the direct-transport question.

The direct103 types contain7542 catalogue joint-root orbits. The99 newly whole-excluded types contain7364 such orbits. Combined with the specified17 whole types, the116-type union covers8232 of21682 joint-root orbits, leaving13450 **before intersecting separately established partial-root exclusions**. These are exact whole-type accounting figures, not a claim that7364 root orbits were all previously unexcluded or that every root of the180 types remains open. All inherited partial results retain their own scope; they were not naively added or regenerated here.

## 9. Observed execution and exact pins

Executed environment: **CPython3.13.5, standard library only, assertions enabled**. The recovery fixes `PYTHONHASHSEED=0` before subprocess startup. There is no optimizer, floating-point geometry, random sampling, numerical margin or numerical-library dependency. The sources contain the literal parent sphere, the accepted17 comparison set and all enumeration parameters.

The source-only capsule below was run in an empty directory through catalogue reconstruction, independent catalogue verification, the complete deletion-side builder and the independently authored polygon-refinement checker. It then completed a separate frozen check. All source/output pins matched. A clean extraction of the supplementary archive also repeated the frozen check byte-for-byte. These are completed observed executions, not expectations inferred from partial counts.

The literal cold-reconstruction transcript is:

```text
MP45_C32_FIVE_COMPLETE_SOURCES_EXTRACTED 36495 ee1cb42bffec5f7abfac73baf92a00058bd2320c339cc30089b8f4599dd82580
SOURCE_MANIFEST 478 e71aff5e0e6b8940fb0e88c889ff7a918ac5a7508540df4a8c4729ad895e58c8
TRIANGULATIONS 50
POLYHEDRAL_LAYER 20 219
POLYHEDRAL_LAYER 19 558
POLYHEDRAL_LAYER 18 768
POLYHEDRAL_LAYER 17 633
POLYHEDRAL_LAYER 16 296
C32_COMPLETE_MAPS 296 SELF_DUAL 50 JOINT_ROOT_ORBITS 21682
REPORT 240929 efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d
SOURCE 7169 eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20
C32_COMBINATORICS_ONLY_NO_ATTAINER_OR_C34_CLAIM
ELEMENTARY_E3_E4_COMPLETENESS_THROUGH_NINE_PASS {4: 1, 5: 1, 6: 2, 7: 5, 8: 14, 9: 50}
C32_MAPS_296_OP_MAPS_541_BURNSIDE_ROOT_ORBITS_21682_PASS
C32_INDEPENDENT_COMPLETENESS_AND_ORBIT_REPLAY_PASS
mp45_c32_deletions.json 57177 7d83d93b627aaabd9011c7a0d6b9653636af1a965df57b247220b067271239b1
mp45_c32_transports.json 306565 c81bee658d6bcea0b89c34f0807934120cf3eefbec78122aada5212b956c6e44
mp45_c32_literal_maps.txt 7910 7fcc294ca52348f3911f285dc2473c7d89bf9647b8458967e3f3a9d885e163f2
MP45_ALL_20349_FIVE_EDGE_DELETIONS_CHECKED 1269 103
GENUINE_DISKS_ORIENTATIONS_TRUE_EDGES_AND_ALL_63_ACTUAL_CELLS_PASS 1452
NEW_WHOLE_CANONICAL_TYPES 99 [0, 3, 4, 10, 12, 13, 15, 16, 17, 19, 21, 22, 23, 24, 26, 27, 29, 30, 31, 32, 35, 37, 39, 40, 42, 43, 44, 45, 46, 47, 55, 59, 64, 66, 67, 69, 70, 71, 74, 76, 77, 78, 79, 82, 83, 85, 87, 88, 89, 90, 91, 93, 98, 99, 100, 101, 102, 103, 105, 119, 120, 122, 124, 128, 138, 140, 143, 144, 157, 165, 166, 167, 170, 171, 172, 173, 194, 195, 208, 209, 212, 242, 243, 244, 245, 246, 247, 248, 250, 253, 254, 261, 262, 263, 264, 265, 268, 271, 272]
COMBINED_WHOLE_TYPES 116 REMAINING 180
ALL_296_POLYGON_REFINEMENTS_AND_84_FLAG_MAPS_COMPLETE_PASS 12912 121 1452
INDEPENDENT_ALL_20349_EDGE_DELETION_AND_THREE_CONNECTIVITY_PASS {'accepted': 1269, 'degree_below_three': 17889, 'two_cut': 1191}
ALL_LITERAL_FACETS_DISKS_ORIENTATIONS_TRUE_EDGES_ROOTS_AND_FLAT_CELLS_PASS 103
NEW_99_WHOLE_TYPES_COMBINED_116_REMAINING_180_PASS_NO_BOUND_INCREASE
mp45_c32_verification.json 71373 b3bc0fe238efa6793f0ad3a58acec1a1b3d6e085ab443d310bc8667ceaf22146
NOVA54_C32_MP45_TRANSPORT_ALL_SOURCE_OUTPUT_PINS_AND_INDEPENDENT_CHECKS_PASS
```

The cold transcript is2238 bytes/SHA-256 `07def803ced4fcb9fbdeddce36dfdc6976765833ad111de7caa3ca9cbd4ad4f7`. The separate frozen transcript is918 bytes/SHA-256 `34932d226c256f70bcee8c5654e0bf2a8df602ed82b1da3db55d874c33019d11`; it contains the two extraction/manifest lines, the three catalogue-verification lines, the five transport-verification lines and the final PASS line, without the builder output.

The separate176-byte provenance transcript, SHA-256 `cf4cfe05b260c49525e93d5b3cc30904b282aa39bd96c52b83bfdae7bfd6b15f`, is

```
IMMUTABLE_V1_45936_BYTES_AND_6337_BYTE_C32_RECOVERY_AUTHENTICATED_PASS
BOTH_CATALOGUE_SOURCES_IDENTICAL_TO_JOURNAL_CAPSULE_PASS
NO_ROOT0_ROOT3_OR_MULTIGRAPH_COEFFICIENT_REPLAY
```

### Complete source identities

| File | Bytes | SHA-256 |
|---|---:|---|
|`c32_catalogue.py`|7169|`eb78c9ea5e89db65b791e8ac0298f0a21e6607e97c05cd32be8ecee6e8317d20`|
|`verify_c32.py`|3133|`0ccbfb67b413046531801adef23567e2f791396070c3976ad70f201b912570ff`|
|`transport45.py`|11290|`5c93b61c34e5749a24d1737f8edc517716780368d723b6a65fff23ddd5e262a9`|
|`verify_transport45.py`|12360|`debbde0086edb305cce52caee9432ca9832f5f616589271121bb529042e8f451`|
|`provenance_transport45.py`|1625|`e1c4b763928ac1e072cd850ebf43aab70b1df6de3cad0d5d2b28dc7f5a6f0a7b`|
|`source_manifest.json`|478|`e71aff5e0e6b8940fb0e88c889ff7a918ac5a7508540df4a8c4729ad895e58c8`|

### Complete generated proof/data identities

| File | Bytes | SHA-256 |
|---|---:|---|
|`c32_catalogue.json`|240929|`efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`|
|`mp45_c32_deletions.json`|57177|`7d83d93b627aaabd9011c7a0d6b9653636af1a965df57b247220b067271239b1`|
|`mp45_c32_transports.json`|306565|`c81bee658d6bcea0b89c34f0807934120cf3eefbec78122aada5212b956c6e44`|
|`mp45_c32_literal_maps.txt`|7910|`7fcc294ca52348f3911f285dc2473c7d89bf9647b8458967e3f3a9d885e163f2`|
|`mp45_c32_verification.json`|71373|`b3bc0fe238efa6793f0ad3a58acec1a1b3d6e085ab443d310bc8667ceaf22146`|

The306565-byte transport report contains all1452 vertex maps, the complete103 chosen polygon[private-runtime-path] witnesses, all63-cell zero ledgers, every fan's triangle/cell/flat occurrence list, and the exact type/root accounting. The verification report contains all296 refinement counts and all121 matching refinement ordinals/maps. Nonmatching refinements are deterministically regenerated, and their complete stream is pinned in Section3; no missing opaque checkpoint is needed.

The proof is a finite exact transport computation combined with the parent's physical theorem. It is not a newly replayed PD theorem or proof-assistant formalization. No source-recovery failure or unexecuted check remains within the transport determination.

## 10. Complete standalone recovery capsule

Save the following as `recover_mp45_c32_transport.py`, UTF-8/LF including its final LF:

```
17443 bytes
77e6a7ca89c5a45c24bafdae14eac473230c1e2571c0fbe9adbd25353752d174
```

Its inline payload contains the complete five source files, including both unchanged catalogue units and all newly required helpers. The decoded source JSON is36495 bytes/SHA-256 `ee1cb42bffec5f7abfac73baf92a00058bd2320c339cc30089b8f4599dd82580`. There is no external source, journal, archive, coordinate, coefficient or plan input to the reconstruction.

In an empty directory run

```
python -S recover_mp45_c32_transport.py
python -S recover_mp45_c32_transport.py check
```

`extract` writes sources only and is not itself a verification. The optional historical authentication command, after extraction, is

```
cd mp45_c32_transport
python -S provenance_transport45.py '/path/to/research-journal(8).md'
```

That optional audit is the only command that needs the named journal checkpoint. The physical parent remains the stated immutable theorem; the capsule does not pretend to prove it anew.

```python
"""NOVA54_C32_MP45_103_GENUINE_TRANSPORTS_V1: complete source recovery.
Sole physical theorem parent: minimum-0041,
SHA256 9a59df6d6b44ecb690b30e3711222fc549b3553f268e6b90a2c37c0ff728ceae.
Save as recover_mp45_c32_transport.py, UTF-8/LF/final LF, in an empty directory.
CPython3.13.5, standard library, assertions enabled. No random or numeric solver.
python -S recover_mp45_c32_transport.py        # fresh catalogue + both transport routes
python -S recover_mp45_c32_transport.py check  # independent frozen checks and all pins
python -S recover_mp45_c32_transport.py extract
No journal, archive, coordinate, certificate or historical plan file is a build input.
Optional provenance_transport45.py takes the exact journal checkpoint described in the result.
This applies the parent theorem; it does not replay root0/root3 or the old57 claims.
"""
from pathlib import Path
import sys,os,json,hashlib,base64,zlib,subprocess
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
B=r'''
c-qx{YggmQlHm9K74Cb_wyh>{`w7^toHI0Ky0}9D2dKW=$K}zLEy);c*=5N*iei8JMnpc8DanTF?wQ@~J_Sh1j7&vF#w#O2&wm>?
8}8UkyxC&14ywzizjgoinf~uTdgG+DoOzMA+MRpLQV^}@!OBafi>R~+OUX@8ih_sI5pOn1;qHAfP8O?DrNiobtm9NaM;A}Y4K!_5
>-C*doOqG%t^Cq#I$C+Fr(Vg6<6wor;?gSkvYxI2A39yGqi$&_dhTA8va|af9WCa|S&#%#5XYr;9K@yZB8p(}z^7YsX8zQhEFy2V
8_uT7(q!c=Z}3sPya`r8DOpXuXtJKs%fv9Oc;(MgxLV8s;A{o}X=>B?a<NKEM~iio1S?kZVXA>_H-$UNVlmUL#*6uA8VR7X&C*M5
;FVR23%L9o$%`8=#%HW_8!sYOil3m9z)Hz={b017xbElZjCWvukspMm@zZz~R6?iwIV!<_s~}mgqSAaCRl>ovJKPBe-RZCt!ZJ)t
)2Ot9cMK}C03JJzqku$<)!ds+zXG5*11VVpYAZ3!E$}O1FmVg|6W9>JLN^U;8jYuZ5RFY>0e^mxU>6A=Jiky^H=WU$GZfG9{v9Kr
invTb_@Bgwc!_`G%@UB2yy6^x$3cSAOM4*DTjphenlSOd5f2BI+nu`eKLxO1uQY~Rx4ZSB-B3=T;<1qfxJwAG-6R;m!y&&b>^N4P
02u=>16<r2jE8(A9>`AKY*wj^nCH-F^hz)UT{tP~RuXJ6x>g!ph@ussi+)${z1cd5D<;bBc@#V*6{Kfq==4f4zlR?|5K$ka<-^T%
7L@MQJ7JS9{j7SvU%7XB_k1<DALb@>52Nd)!}fCZR*v=FXS;YaaDM)|u|w+;L%W7WqXC0A)*Hf$7SVL<%?zp$TlsqRR0{3`_~`>@
LGA#Uf=LJdB%q0m7Rilb2aDA-h!V{V5XxaB??Ojpe$yDXKHvv78{8Q^!RC(<_ktb5)=h$WkA{H9zZ_p-2R*y0IWxIQ@HM!#eZ+%N
5GVX>5d}T^GmPmXUG#W5i4gUbI@_(ARJ~g96|PE1O*pTYf>|7t2G66eXHw9r3hO)v0(h~AXlU;sMQ)jGGxJ6Ol|Osk+DoqltZ*H0
pkUzU(fDSu!Uv-l#KS|(2N_~Vu#X6ox@7<hG89k-k3#~HgP@?eHg{WL563Bhi2ngXG`))HZ)ljlA5bt+r?_%@G~ueZTm}&lxtu1n
dMpM7lUL0(MA{oTQ)_=1Jz~{G@LafK?$ONdmQ&;W%x-cQJaOGW&h!UVAWb1{B2kr){RU6(@LmB<h!Wv>!5RQn0>$QNO$;oD$K4l$
94U|;MI!;oR5A$=5_ONmlypK9mfkaxH6R!!U?~QX+^mAY)fz%2&}<?KrhHHv{&bdZEk*Nj7oP%If8+Ic?<8l2clDyD%42mjO#mRM
0~P08Go2aqaJq6L#~xrq!d=g1yaHg(oZWhEC{tmmDB;K&mH?d177u~X5zv1kAkU#+BVg0X!e4ON;KyD0hh*HfEYrrunN_~$c=N|y
{3)RQr(*oy_`Tg0pMK+rmwQ415aA@bslZzee^gWW-`F$lhU5V^eo#{^K##n0y+Wl*E*a@&GZayBx<DF(N{!V4F${h;Ssi}Y;Wu74
;CIbZC{pIoVrLdA*@%IVkE_eYvQjfuhPVpy54T<g<vhCsxX_e-kC_L*71hFaU@)Cj?pWFsEXiH8c!>BjwCjfPi{Kobl*Y;+jE548
SdlCr1i*sR!2D)G2n5y(V&)b}i3}Y{l`V*~Oc1H|-$q^70Le63XY`g3a4`sC(q4wWiM#@}W0+x3W1$~B8v76-KPt9L%28%t`?)@o
SNp(oz_;(nU06KpG2qTOc*P)*DqoV*BN5=O9#Fn1lkeyZcLq2bOoLT?SZ&W4X6ADT%4ujUHVvJh^WB{qgI2#wKL>YrLmq~<><B}f
V^K>*_<n$PjXU$6Kn+{KK$=rMXpNefUyMUR1Fgy#i~e6rFl=Iy4BJRBKv{#ZI)&GItay&FOw#L2;|ZS(Ci3A38&3w^^txCb4+r%j
=OfbOCiJ&wx4Yp$U=Dz4(CGE<F!!D)MsJ)Sv=wm!Dn#*n2Lb89fUVtUqFYAF`AZHYl0i=71kQg0CEvV_c6&ffk}@qqgxi`7*OodB
1hqj^HBB=^6IrYit+)}znTDT1Z6nj@AUg>8XJ{#Xsj^26GPD}1Z6)#H^hR7-R3ifjOvu)(w7Do>zKEMcC&vN(Kw-sOCkq!0f%p~F
^l*o9G|2<J$RgwWwfFn(ntHC;{oA#7**M6my7MJ!=xa9W-oNxndl(Qs4|_i7gTmPBE$+CG$7at|hoC*TxGPW?AK4Qr6eM2@)I4JU
FfANw!<Hb)0guU?d~|w`k9@vFd*JB_|9Bb}LM0;r79Oksv7J%RhKnw|3Mm`C(JJunwiy%Dd$R@cgpKCQEtUf`q6z-MpPpVFm#7Dx
Z-@6JM@{+sTi}XyhMB-bid)bc$sJL7Vvn%zp18mObVF1N{0*L-@?3Lqr|tOp5_f$!x4&TYyc_CF>rl8Sr2IjGqn*~1%tYD_ss{<W
bz<#Sx)z&q?!i7&y9fj#H+07y>F8jpHtJoREDBV~u$QYTXz%6g%ag;iUq785UZ0$wU6q+?#lqP-zM(yk=XBVB^L8!W()08k8=$1N
GaDPHm6Pmpa)Y_BGZ&UtA*Xk7e){`|{`<?rQ}^`n_x@#>&9_Vu6wX*-l|~@>35sZUDprEs*+K<7qzGAru)Sk0-JF0uX~6@NK<DcU
H2#>^dT}rdQ9kfmM&Cwgwk8Xc7~Bne#XQmnoJcW~a~1hM0;K61&wyqu7Hp0cz}yDmYVkFQgg4N%H%-pyje`UM@PQNr*i~v8Y5z&a
;<U|Ix|rYv%*Oz}3YK~So{|3pob{0148o!8!)~zG*XgnXJ(-@2gugboN;;yt^J2WQu_il$-ND$7UYs2c=rz5O_e*Yhc7@~3k{_@G
!%Qof8@6O<*I3jkXk~D}WZ`nS!|MhP3@3&^9fNT9IbjzlLA-Db`XfUhoW_-KtXk$bDWPECvW&F~)Db+oelP(AE9N*pf^=h$*8q3P
h%&`^zCUD0FZ0D}c{7dYF;Y(k-t7YRnTswv7ZA7#V&Mb42VjIy)6=?m5Qut+yOK=t?*aT6lyTVdaH#&^obFEj@=)<D^!9U!5Ex{d
Jn`~Tv*8+B{Nv$;dvthxczXWpr@s4Jz0B}+r(>ARnM7E9k6svW=ohgLGK5<Km=hyT17<358J0XPp_dSn53$3LP+Xj>E1oFANx|Y3
%+i$`zoPr@sJ7^$Wd;UiOM^61XqvqY2nS*v_4?7$iJ3=&5Gq7k4vP#+MZr+&k27SnlW|t*NRwbO50cfB8$6DIL!w)S*O-?iASi;B
8^S2Qkf2Hf^d5Kxk6)_(dJddLtQEsSU1F)oVgX@G518fxP+BQ7_`h3roSpLL&r#W_0#{r3fzo&IfTvQnkF5|sG<;aW+}+Vr5}>c=
!Lfu9lEcyY$BWbcbsvdA$|JF0<*WYbvHSkh;c1!a#VY^f{N(J~y*xj^cF!+=Ik|=|2KsIAm;H<L%WDY}#%A*DsT$vSjrJbhtKI~U
{uC%J(T4+w9(p6!MeMt-Qw7DtmoMS;B=oEEPnSpi?}l!_`Y$JEhu7zqCr4NA`Pu33?%BC}czu0%a@N0u_j8Y$E%)g3@Z@8e4xfNU
xNhXlVNRTvT^CgW*DZI2O7J=Q8~YoO%zY4fAavXW*l3I^+iIIfoQLb=2KOT@RY0ePGqgs$8UDRk1$cV5g6E|01aus#7ZvDoy&4B#
!v*8JCGLaj=jccrc{Z!{X0^=<&OFnD&5e^Q{R5DBc6bWlu5a+vVF3&g4Zl^eTH~Pv+G?|>(iqu8_=HYLHO)B?f0X=u@gCZa7b`z|
uDR_jGJc8~9Yd-^$&nWadoA`A{w_L|MD=S4s2*vj=KxoKlw13ewer9cM}neYz^b>J+=KCM6O|rKfaiSBY`2;R^(HHi+TNbO*B*^M
uQNJ0XxCbMwS(rU(GK<+wT3sY)yJ)IJ#2cd#%RC2ACAM&Z`4LjztO1G8udNo$T1&P{eZS?d7Xs22W3z`xzYm4fB!q+MJ#$e0Y3b3
Z+db8V&UR!_VJ(o#l@%p_4VxV3Te>nR60BV?XcZ)KVG!j?ms`ApZ48fFApz1xQ9pApOCwsf9#)KU%9`v%FKhlOAZ!mcUWD;z`(&)
61?Oym|zAkQp^(B7;i8TQ0rL&guc4-(Z>i367-ezDsa7cJe>-*R?Mml9%bM*K-{+4o#q}Zcf5AT4*|KORx22f_Bw#ITF~6D*BgyS
IBvH(qh`C^3>$j~!QQA-^BUvk{<s!~`;CKf;01_T10jO!UJ-HV{idUQB3C-A!;KbBBiMx~?WZB`OnCb$;`^%s{&V!NfBg$l*~9nZ
6~yM(VV)x!Z;Q9^h4-4xeO7L^eQ&SPZngHC2mWZ>sPFHGt?^zE);jxp2Y#zQY9r|!jQqV?3y5d0)u^`)>Z6X|sqY<lHGJQMBTPk1
PH!~g<#H8eVkN1@OW-Ay@-KWPa8YJ;2S{DrH*VI{O=OEJjvJ0(&QT?aD`Fp3M+a>=(1_fo#+%{M?x0@VtJmSZy#0fwR}X!d_;`Q6
KCbz&kbWa<@9l^6*8YB{)jkLsold9T41)cGeculb_V<EjqXx^_9^rcd0fA5^LYyr;Kc+)kIUefA^c==~E@z`NfZS-=o?Li>*I-|u
Ku12!K<1P8in=Q?uCys)3E0f$1)O6qV?m|JIQjVT)Aivmr$|OFk+A#A@7Mh+_wek!iz`f*E)w8n|LFX;{^jrP;iu~lunA9q1pDvZ
i^D70#S-8z=hq($;uHey$~}26dYrn~=dNVT(Cp&s6AYaJ0rCoEagBa9QDlAmbb5Uv_`uP5|M>Xi=%kMlyMF-&U0DdJ4U$Rn6MO;U
DZlp5K7k|zILC)aCpe$W!?P=t>41S$@{~4-9%hEyfZQ3)@SrGKpnc(kXuw56%MiU_ut>{wB4Tk$UI-FVZBUmMT<%(!t{JIgzsTnZ
W$OYo9@40lK<#ejs-VaHSw8e8k@x1{oy~zjxfmYYF8ZdmFW{9+M@1s^;_wp4ftR-m8r96b`f$kqJevkeIlR6&Ipc#ytJZ0BSUCts
^_th(Ywvppo%-0XH^aSfui=k6t@>VT<hNjiT07{}4*YSu?Rmg1{86i2>ojZOeyv4T&M`Mne$jA*9l?}kOUD)ETD?^Q8C<G08>L#S
S*kbMrFy$nYBbxWW^2FH+=JiydnMpcrPjfIsl9hl+S@-U8_e<i^gVxWHd(X9_8Y9;?67(Z{<Y!nHin%w;a`i@_YYXT(_p~US>vDu
{|;EA(}aKUcc%?3sc##)&(>8X9NdDjDuaWXL&voLkA;IiHO!k}n8VDD`lqK?TcP4%gmNVq9`TL^9PM7^<PQn(r>p)Ie-63=*j;hN
)UhLuS`!fI@3;(zqNV{h?7wL0Llv!$AvJaF#G|RhtvwMdgpo&h`yN{n4Dux7Jj}?UKcfI*PngZrn^hLNvuT7a{-FJZfXT=rNx~M&
4L9O?xSk<sOnYpkY#HkLlXx-P%ZAX&5YNZWZKEI=Ugp?tq%0lDAiWnc%xaNT5{(*kCM6W#mu!mfON{tFe;VIamW$aF1KrXNiuwiZ
Uyuf1wSbw#O8xaLSpAG0R1oF#9?X7*SNFjq#T!mBfGrxY7I8d{CRH<rDI%W&4(0TIBf6u%b3W7GfR-Xna5yWt-fbB1U<ok|?SiA3
JEB!CE>87Gut6H&mH_GhM!2EvgAhblUwbtHi?A?By0xw5`K_%YvV8tbZ-%|;w*U}H07jokc~p)0-s548-bj8n{!X@h4$=+l<8}@P
-R^FEsMvx3!uiOT=S~5)DK0R#yZ_P~$#ve=Y~;(SVx%k&f?d_AXRI7Pqh%0yjzoA~;OwLeDcyh4-F)A@m1mguHjg68Fb=T;;SIF{
U~n`$_(ij|AH@M}!Ko1*x5@VtuD|<XitPXl1m@Q^H@M0BpAq2|@7?&_=$&6f#c2G_gTLO5WK)W+d9JDRv)a%M>Bt1xc!lR-IQl5F
fsx?zNAV*w(9+s3&;d_Oe^h^uhPWLXT^)-F9L+rE8RfU75r&!W7RhrY!f5?<u;s#A#pG?CtEsL-KAQqt7cWw8DWVok47k|Td?|sV
bvT#~f8f*Zl+&N43!TQE8dO490=>~*Z)6q-o}pM81jGCydOxU$S}{$)kBShOtQPBKY(-QU+!WrSD_T?mweTJu7~K{5E^IJ#6hfzY
go=KE(oPz;WSsrpk|HF57ldxWBJja6FqxFA+?vN179+bOMs~N6k=+$AGRe#aud$k8FM5>z>XGjh1{XsENjg@GaJq^UI{n55y^s&+
&aijS;fB1}7)=~@LnFvibSaJ{CP2ARa2(S>7s^3(;7<~z7seX`0br$$s#YkMwYXaBix}#@vrD1Wun(+eN7ZcX$5GWf_yT5OZ?iN|
QO6*-BndOo%vYe5z@{3{yj9>EPDl|U$x08?<Oa}D3LZgO9#0XQ6n!brOfZ7klH5Mp;7o-t^UO4RX$&%+)qYp}v51HMqd~~jd$=uP
iDvF>i%L#|lC7BJKOd63Eh2dxt>b_WE-A$K?V-s3ZwDN2jVAuWtuWoZX4=Vu10wgQKBxm6kDu8WhD7pujI!>wHBwo(DvDR;e>7S-
4-DCa#Vy_#tXu#JcNbv-fw3<}jH$T6b?k%6LQ&6v6CG8p><2rpP=OG0`yw5uQ>So=q~$bCFoCKvVM`<MHZ|$#FE$yJ#i?Bx!?l3T
$QH}(L(p*#hC-W2hu#*|B!(P2R>2|<QLw^51YA0bNKlzwwr~}$MHs;#k6UP>)X}goq)r(Q!e$;8in?25`}H18L~WScIA!IV;AbT}
P7cI&Ryu>iL18rr9v*XkYl?i3bAOT4w+svbTO|15_KU@QAG{SBKOvpp%Yl_an;kGUVKYdC!MTKmyBRN^)yR5EvVqZ?_G+E@fdPPa
?rvR>gIbOZ8-Z;(i2{lS%1ffmeoq`5jTZ7Hp{d|-(kMbE!8=77bwYEAQ5R2LEE*6-4v9|53S^Wr%anHE^yc_NzItGL6_y~<*pd`|
D_$bW#VJX98X!s1?mKDBmbeeo+mn5KKOND~Ze&9nvS|E$^Gn}efchG&7Wu79ZYX2RjBRgPo>e%Om58YsIP0<A%oZ2#;-FeUqQ#OF
EFU&P6>mMSNNV0~IzRo?C=dvt7sZ>RTsv0y*La+ZXw3!q9v4Mn(`#;u91b)qH64seR^Wy+4`Z+HVQIwl2ZGPs4mX5VV|y+zgkw+u
9-+l<4sWHfIk;uCc9Q>7FNU5pgyj^OX0TMqaPYZA$C%Lt2K$Z2ra9rIdpv!js2rB*%b+2M0$S1wLI=A3BCn)nK(DYP_Z~&9Sc|t}
WNm?L+Z+>AHkCSRrZE8Bf$&#DHn@8Och8srDo$!5LWYbmDH-pSEL?HE&zDU6;i@o4d`9g#4ZsRCj5M>66K4Xs#gJpTBBlucG_Kug
qy`iFzW^lh09Ws7qYFKurIdGEq=uLy_6q>XHn2+R3t<PBs1TPDSnW(K#&quCbcryRP604u;bdF7;}nL9>adpLKpiW@#XM;B9#HS1
0~F~?u+K^1`JjwpN#&vHH<0U^h7C?)AOpi|(&+4|Z97{m?$%4oH6gngv_~mOp{4$9Rnqc15PH9&*NKS?V5p%YOl$8AR0BhuQNe}u
#M$_cSWo~=wP}}v&9llPHhk&LkQhnpTLrgZNvCnChR+7H{c#X)$f9f19oDw2(_k*&xo-&)3C4kukVJ~@d*RZ;utPnQd&@uN2@OU$
9WBv>-Vo8bIsvHntmdR`wTk?%*%j|PD2v7}m=lW!mplq(472RzMFAPZ{P~MzS*NohCRi~NR!rqgW~=0V7Sh62vq>Hn?s%PSngZsS
7=FQ?wmg<R<I)JhT;K*_6*ykOu*wrAT9zhp8lk95ZXdRR3Iew7umHWOjF#}M;L!5$rP$52TuK2_+$-bLC44WlNdksa285M4D*A#-
)0e!`B*!DB46~ED`xZgcMuJw=_0lH~`_hpcM++v}fr`S}l!+T(9CNl>9vNa)tbKY?LGFG58=cIxW=ncFJv=cA_+VPJkCDXGB$bm~
*qDK>J5fIYs%v9(X-0rbP)=7{s(1<3s^L)N_A}gjx}Vc~7?h*n!F{+{pzM5F!p7oLW&NC=zVGSzDHN(GO<Z{N5vDQd$BubWLeEjF
*2M~>@&M|x<!Kg+0c)|OcN0j>@Tup%<ph>}jJ-<{p5$h=sHrb?u#93jcpNfs@Ps5LR{oJaNlsyI4Dkw9K)ZSc(-l5t#JC+gWT1)2
KI@2-3^6Jo^BcAktLjkRnQ3Im`@7K2*%l@JU2!mFsUL9>GNH8usc4AvXr9JXFs*@*%5|)+g=*AimJ&lst_G=f1{V|qsS>dCriiPC
O~6Fzhfgrw@y&uFx@iY#SYo#Uq0qZaB*`tPqMaQEn{nzZy^5SoKs&DFz0+tS0=(rW&Az(Hw^XP$ZgdsnZ?3i8^(hn;^5do~T`H#(
gKa{h-Btucl;JS;Ud#m%FndeJ9InBDxC!uh-ghzXXyz>q!uru9EDhi2u})&3AXkiNblkN%rX9?|)7B~IXdz*xp}JdG9<me7_L$I3
GK0`oG1ea?HY}k_!B$qw&BJKEMZks{n#hTe;qpMcQM?8)g7e=288I?%Bg3*K%jwRMs+>5um1t1fPGMrmgQaCsZ_1L;Ow=)g^)qCU
&m6#M8IpFJA?9SIM!HlvxM-ea3G9yz1yHOVkzLlm?44*q)1gGdl1`^#ng-#nw1+m!%3*=2q?iJ+CQKWVvz3`dnh~J3I%O3tHZnw*
f=;D+y7W@sQ#4L_z692drj{Bq7N!=H?5dY-m%gKHD5QfjlK}JZ@?e&H(+o+_eOx-ORjbDb>HXbgu`9#lRYDE<!f+MhZ}N#w8!SQZ
db5-)1h{X8`TQ-0-|M(+=q)z28$z5Ws8opZHyIQ>h?7-CW(GMJ#UyU4m|@&j(1KYf5au2;monQ4+GX7ZxGPyfyG=d>YHtp)Q${`m
Jq#>hdXw~|mUqjnR6gtfQ#H$~R<fDqv#Ih9`l`n%j9X5R5SEMR62V$2RmkiN5<1o7G0EiAAXGcEWOGju;zd33xs<XuDIABVr!I+W
_xR+uzT1EQYu|m}KkZY_sC)FGfAk;y_agH}$zIY2C12VETj??HPp<ys%00itz+jPw3L4EPF^-64#tG~-RU!dtAtLgaZ56wl28Q*L
2?|GtXXj@kw)yvqzRWiwCWiueQ-6`D(|<347+odXDqr?L9-f??oc&s6z$SK$M;6RCrSMqM<eAEZpcA6fIP*l>0B{z}exc|#vqT^z
==5>{(WON+d$MAjv%&0UaI-a!@5rioTXgWeC_4B%d{kC=r*Kk<=wAKcm3%Bf|DO&622^H!VV|SFmyS`vc*i>;)({yRa$w=&D81t?
65@6mW3_ZB8|;#A0>Q{Q2BA&I$e=yVwT<@SV!bMC8-G~?+v_1H5Ao#1NeNGvl^YX}o4pYVKDbS(U<>$x(GGsVu-qHo`p07Bdy$G|
uOhJPn{}*%Es%}Eg^sgFvQ*E^32G@=f;nkw1$gu78E<`#?pVm@hI_B_O7SCPtC(i~eAf+MdL@<k-s;v>{zWRe+pJzwelZ*_>WT6)
7;a-0sM=a&MtJS1RMOblcJP^2ISJ!I_jb4gzixNx-QkWXv~({EE#1pPOZT||gbXU?#<{zwXd+9R40&i4!Qoh^B^gwv@~BjYB^H!c
5$W-nf{}^y@)s7)xn(n+DcbUCg{2ss0N-C_3Hr@m?<W>TMnOpo6d#dmJEH<GQ3z&-S2Bx;q~X(VpBDK~FDg<u+)-r{BC~9Qs<SDm
p2(iH;on}j!S=gtcF?W2Sf|^ry;xaHqL2ffbXJYB5otaT2zgA}JG}he?Kj<iOQ+|a^{+rmf4DsV^y>%r45he`$6^M=_4<^}7EY0~
h}yHrUqor3UF~WG?t)uiRG}m#7UQ%^M<}sMfj7QEP~w;f8k;seGAZ&>5RU<XF&F~Gyi!%ISNa7yA_GH?6(KBi51~#9O)!I$=1YYv
fw2V`Sq73C1m$R^0>>zk2ro%PbcEvxOJu_2rYo!i(KBj8q~${O$;G8Q56MQ9r~tfF)iqBbRN07mb$i{R0DW%FG?JV`^g47ouNKt)
lL0o&wdfB+-XzdFGvKzTgK6*d&_TjgxVk<#$$EwDd733nI-;Zrg2}~+i+0{%gnom9AR5)t@Yt!Vk-E~pG!i=8tV3vaDlQmH-VrAa
Up1rCE9h)YJ&A1YJ(`Y1)2%qkx~(l-$wwwjP?0@0zkS?rppO4NWlBe3_0Qhdw1kb_+6on+fD$Sa1x<$ooIVy08+;wA&=O}Oa?;Qa
(@RRI{-#e?IoD!z`iPMgprzwKZ?J}E>ujwLSlFNNaaw-F%fygzzNxf{W3Q@Bb~HK#>(Dc<O17AffBxBcPL7IKoD`B9%hDrR7(K}q
cDTffrI^ZabFc|SqLJhvye$G{Bp>08`rbi9cWnHGHbmOCRoDEPe8PtpS1z=0&o9K^(7^rW)8*OK$@{)p8o?#7*_2HLadP&)f6+g~
L{FQ;qwz(ZWx}TJoZ2NDk~dFMHd_iFZ@hI(Iglc$W*0LdK<5O?0r@~S%g^D=n^1{$E9v?5tWGjwD2-E^7Fhf|os)>2RE9<nO<=ry
iS@#F`QvGn%hkePj}vAd%Ccp!ny(Wpw=!HuW2@tAwFWZ>%(XWpUs8iP%)(6GWH_|8vdm%zMfTNyQ_kWWlRW>b?9RU`MbgUBdo0Y-
d;Akwdgy$4v=av(bBTkGMTvtHBp&>c>^POb=Mp20HGo|5-jre;r>`XMO^YHQFEXj6dc0#trHTGmWQl%`{$1~$3Pw#k*;2YXq*qqU
TZ(`Kv8WY?ImNXb%}6FD`q@GM*a%D2vek5QBVusH{;wEg54v|d^&#b8=v#N)e8uiuAvs;IDol20fSrn5e}GWKXu~`Fv0F#irQ>Xf
$fN>uLcZajoFlWSG=8ec7iu_6|Mm0F75$o<KaD^TH={l9RxY`na%q^x%tZE_PM}nYj%t1I9;mi?O$}p-xk3XqV;H<*lu;%N*n?e|
4@c9W9jOKhTw+e+9bi#pH{Pi%M;-1<U4}vhO=DzLatsV5^=giP!@~3u{@t*1K?t%vWoM)T3s%yh`XqpbZ=kl}j_8b@1{DHtfxx%_
@&ixO=yx)64DSW*1oPmYd>vx@cXPEi*@KR>VPomi@T4_7%8|K><%f>?ixMy#=GqM4-jF}!zXfs6)~XnyS>O{1v8XsASgpVIulYc{
)iG>6`s4MC2jEk%x)<;JzZOM0UG(iJC;1JKIJJIqnM=YFmS0d<N7FCsVD==mPjst!#%C5lLG(4tDpd|zC3#-%Sh-6<z)d#ZQ}y5q
<{Je0s4NT!m#IXeW9l{kL7o2M`=__Hn38laDnD^eF=!_G6peuwqQ;o<*$fJC_EwXC7Fw)KcbjiXG|u^#FshLgiHQcH<Za#w6+Njp
14H5mj_(3Sj%lG`2|}DRBbXbj9?zE|A|cycWmwTol$P{cyV|nSv6(I5{I*iFG|1*!v#<fuV(A--&59lN9R+8pgVV!E6<p#0?7Cs^
;ektp&zFPyA%mamVR0SWhpkm&MTOW0Sd)i`S1Y-0sSb++J!C4wqN=Y}{Xwnz!^7}R6=P{uFsb}gfni-6f6X3%t34o+oL39Ob_%Ai
N=z13i0u@88bUcBQX6==F=r@@4Ua=wOyIZ(E^Sj<^kre@Gd*|G>d*c(aaC;D1Dj+7x;)k8Dp-~<VVvF419c(K(<Ca2Pi~bzN}cCB
RyeK3)Eo1!dhvv3&vEq#lQf%C<u+i9()Ivhk(RafG&x^77yF>_Zt0>8>J~*e+OI}AQ)c$`)}#rQi<r+7v5N^z-qpIQt(Jga3Sy*j
MqgAi2_huToN#(DH>IdbJ?D$FH5&{8nA4>saN82VB>uN#hnaIt6`zn1NL!1dh!9IUXGe5WY_CnRO7m6ONY8K2LwYI7Ly`mp#F8c&
l&M?+UTa#|&@#<05Pig?tZ~GxcL?NSYpT<RX>H7C5F<*syXMGW0V{U$l9Ij8ITCy+NJ%0Dzk;n?B88aF*L>d6D@jW<m{gt~mm=2i
|G(TNdlPO;U&0Yc&v`X#>ARDbbi&aWm95lMDBYN-lyb@9R2LKv3P`qNCIP0b(khm@A#w>Y*mf{ju~6nF-DZo`SiI#HT8Hx7Va38X
q(coYu_@^A&t}`$>`SNI{H4XpUdh{$amdEwOcYW!HqCwm`xOK*wf?vw!XGF?(5#0tJQ>?ueK_0##Z8q8A_WQof<I8tDS|8cZMHRV
v~6=$94FficTJ|_ccnN9RT|5=TY|}srq_*(h<Z`&S<W$&V>LG>K;`)H`Nk<oHI6?^t*!fzM)RowbW~q?_@Z*NCYX?f8<M8-{L+gS
(cDWw0ORqe@Kf@P57XI}$@OY_y{K%Ty3ICMw#U0Hj+J#6#u%lai&4-5D~`LS?vP}Q%X9SN>EJQ~<@9c*3B0Fa-==w5_Dt@WFx)d0
prm8)Cjl-qHB|R3p&%SKquF9i>X3w}SuZ`<@_js67s)XS9BIvyPL7qXBO5j9HmK#&CeXA(k|F1oMW$XheW>0*%whJFusPCnoqXR+
{>~j+F0&>+8HOq4S@ritfHl&g8bx~W)fQy}VqU)8?bNv_-frm2%9`noXWn$4YJz6KG42HlZcf>v-ZG|SCaU2QP<mcZRu<yuC%}>Q
(K}Z{=G4a0;^|JYQ*CO5<kBe8$P#yGq6O9#7v39b^5v9}jP<8su}LxgnWN?Mjd;b(I5L%aTv+`YvWW!Mqj{u-cqBv0eQQA!fOqZB
8;f;iL@=0Tka-G-XPdtyW9E6JD<+bBNkpKw44V@)1BD@u51HbOGAdTS=-*41qLeHJ)ae4yVkLG}T8oa5lN+K$=Y2pFs!RltUDXbD
u+pq#dX=IhU2eD_y)3thg{SR}R!=5TFY|d{oph?g&oVp_%@wS}p_W^C*fugX%-GT;B#aG#rRqs|5hnB(D#Yago(?H6VVa#CJ-6zd
1#_k|yr^Ea<srcmN}Cm<OmP1;y-0uBKz;>S%p^74B=T2SWyLHI^$@?PE@?d?dJYp;i*9|TL*hVL{BwtPAhV4v;KeC{ny2@g4$bnI
C6QDks&1h}9!Yr;L;)Rsmg5ozG6ZlN`LKX0gVPGqnB~&FC51T%ROz-&bfmu!hf8j7Q~#C^3e&AS&W6wa0ulMQK=P`TAYP5cm6uO%
R*C|&qD*EPruQA0%#+2!&$xoOe<rn)`An+$sZ`6GwEGM|UPN>neV0eJa%2HV(h(^(Wzz@G3d@3R`_7pT@u?u%?)CRkF|9m^(h`kp
yF}wUuVC1pPbDN3dUIvk88*<!e<g8SHS@;fU`g2-*iLU7lcD5}=0xB0ghb{9%V5MTTziif+8inc5*t6?b??noG&z{$;Pk!CA9xD>
MOEdT3CD&i7_(Il2<6R5zprVerYcAxIkjh{wOY@=rSd!TI{92jd@<G0GSV`+Y1odw#aI9}mlH`q3nupC#))l8k~AQxJV_0$7*bJQ
BSIl`74|5|q9hl^>luz}D#H!5voU@0jqpVVr4jWIJV{$>P$_RpSfnrU2n?}G`7L>eWk%UGmGYaC2g^)k%?$G)0P@YLI>#T(F^pp?
md{e2q!Ix8!{7l08Wh0K=b&G_H3|Jz$|>_;a&XZn2fGmflez*j>F@Ezq;!~<lRH75YsW?=?NRY32^5nar8|LAA8nt4V|_30|4LeI
%5~H1+QNNNln9J3EAN=8l&|O6kt&DZ;;1+xxQ#ki@>-q9<O7SY)=DV~Z;BWRbWTtc{30(Kq?VFFnrgS_KHbfH7BH+h90lq-D&NX^
TNeGe9!%lEIEx#p4y=s+#B5rmRRzvifP9gXG3Rg0y`*vd!sgpjFmodYps>Cn7gLNEVq+sG6A_SFo4JfkB>{<xtUzZdFdwB~jWlqu
Ii22(YQ4dt%yzJ71S|11I&~4Ue}fky{MYcM!M*)XJ#Q~a1p=S%30=d?fYc&BO@c&+PrFeN6DIjKQfX7$9LStG?{xGH!GEDq=KLt*
C@rY1P?mgI%}w%_bY{wO#V<N-D0xBIr`Z5yOa{H|AD^7{<@cmE*1X6Ry})W0cFhXqT_?oJm}EDNNsf71prE7|+I)V))S6|Vq-)7c
_W>@3@rgmjhV7yl>1|QDz^sX3Yl3FBayFHHEAkoa!oZs=)JTV!5o(&kEi9%WFImyMyGzhONT35bB#X()oAV6QfBVMKZ)&`#)S%RN
8;Ot$D`>o-@I+x@i>>M!OO-7X?3+|EgES?Mc*-60CpyHQ$fbT;f$;_3Qyke@%9OR;*`u$I{d#_8?HP>gKWMqfr-#3aoB{pWMUlo8
u^Wb@YD3KKLXi`0rGpdX>kpTGEKhTG)<3#F`R(Ld<_)lIgq)xJ>B)5;znOM?c+`hEZ%-4)JO}Y!@KV=SjyN#5eExT*V`gu=I;9&J
ovX9A-TFa|fZ&H1e>wjI&`-{eF8ha9{qlw^`}`uQFR8pO-}~i%{2v)b?Y;
'''
b=''.join(B.split()).encode('ascii')
assert pin(b)==[14158, '647e75a5acf3a3891f9d3f274fb76f5f87067d77545143b881456fe8440e91e6']
raw=zlib.decompress(base64.b85decode(b))
assert pin(raw)==[36495, 'ee1cb42bffec5f7abfac73baf92a00058bd2320c339cc30089b8f4599dd82580']
S=json.loads(raw);assert len(S)==5
root=Path('mp45_c32_transport');root.mkdir(exist_ok=True);manifest={}
for n,t in sorted(S.items()):
 p=Path(n);assert not p.is_absolute() and '..'not in p.parts
 b=t.encode('utf-8');manifest[n]=pin(b);p=root/p
 if p.exists():assert p.read_bytes()==b,('SOURCE_CHANGED',n)
 p.write_bytes(b)
m=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
(root/'source_manifest.json').write_bytes(m)
print('MP45_C32_FIVE_COMPLETE_SOURCES_EXTRACTED',*pin(raw),flush=True)
print('SOURCE_MANIFEST',*pin(m),flush=True)
OUT={'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'], 'mp45_c32_deletions.json': [57177, '7d83d93b627aaabd9011c7a0d6b9653636af1a965df57b247220b067271239b1'], 'mp45_c32_transports.json': [306565, 'c81bee658d6bcea0b89c34f0807934120cf3eefbec78122aada5212b956c6e44'], 'mp45_c32_literal_maps.txt': [7910, '7fcc294ca52348f3911f285dc2473c7d89bf9647b8458967e3f3a9d885e163f2'], 'mp45_c32_verification.json': [71373, 'b3bc0fe238efa6793f0ad3a58acec1a1b3d6e085ab443d310bc8667ceaf22146']}
mode=sys.argv[1]if len(sys.argv)>1 else'build'
assert mode in ('build','check','extract')
if mode!='extract':
 tasks=['c32_catalogue.py','verify_c32.py','transport45.py','verify_transport45.py']if mode=='build'else['verify_c32.py','verify_transport45.py']
 env=dict(os.environ,PYTHONHASHSEED='0')
 for name in tasks:
  r=subprocess.run([sys.executable,'-S',name],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (root/(name+'.log')).write_bytes(r.stdout)
  print(r.stdout.decode('utf-8'),end='',flush=True)
  assert r.returncode==0,('SUBPROCESS_FAILED',name,r.returncode)
 for n,v in OUT.items():assert pin((root/n).read_bytes())==v,('OUTPUT_CHANGED',n)
 print('NOVA54_C32_MP45_TRANSPORT_ALL_SOURCE_OUTPUT_PINS_AND_INDEPENDENT_CHECKS_PASS',flush=True)
```

## 11. Continuation and remaining boundary

Retire the99 new whole types and preserve the exact180-type whole-exclusion complement. The direct genuine-cofacial application of this particular parent to canonical296 is finished: revisiting its other polygon triangulations, norm ties or exceptional shapes cannot enlarge the103-type direct set. A further exclusion among the180 requires an additional physical theorem or a genuinely different justified parent sphere/geometry, not a new alias, a partial graph embedding or the unaccepted old57 rollup. The existing partial-root/matching results can be intersected with this whole-type partition without replaying their independent research direction.

Convenience files: standalone recovery source (`recover_mp45_c32_transport.py`) and complete frozen transport bundle (`NOVA54_C32_MP45_103_GENUINE_TRANSPORTS_V1.zip`).

The archive has86551 bytes/SHA-256 `fdb10c587e364aecb75b379bf432a86cc613a04cf946cf7ab48456d694622d51`. All19 manifest entries and ZIP integrity passed; a clean extraction reproduced the918-byte frozen-check transcript exactly. The archive is supplementary: every continuation-critical map, generator, checker and reconstruction input is present literally above or reconstructible from the complete inline source capsule.
