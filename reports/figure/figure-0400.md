# figure-0400

AI research report · 2026-09-17 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Finch 97 — live-mass root locking, exact root turnover, and cyclic-cap continuation

## Disposition

**No new homogeneous own110 body is claimed.** The accepted winner remains VQ20_C622_ROUTE88_118_G12. This handoff supplies four new, completely reconstructible exact nonwinners; a quantified projective-plus-arbitrary-affine-metric obstruction in three explicitly defined six-arrow chambers; an entire-parameter-family exclusion with the actual mass moving; and a certified counterexample to interpreting a tiny local escape loss as proximity to root closure.

The constructions, including the deliberately nonwinning C598 cyclic cap, are retained. None is labelled a record. The three parent bodies were freshly reconstructed and checked, rather than treated as numerical point clouds. All seven retained physical bodies passed independent complete A/B maximal-hull, true-edge, filled-mass, direct strict/weak face/vertex/edge checks, followed by the third centered integer-tetrahedron integration. The source capsule below contains every exact input and every helper needed to reproduce those results, without retrieving an upstream sandbox or archive.

| Exact body | V/E/F; C=2E | Own strict S/U/H | Weak-only | Common centered denominator bits |
|---|---|---|---|---:|
| Parent A_G1067 | 174/307/135; 614 | 1/2/1 | 000 | 30445 |
| Parent A_G388 | 175/308/135; 616 | 2/1/1 | 000 | 37766 |
| Parent A_G458 | 175/308/135; 616 | 2/1/1 | 000 | 36040 |
| VF97_C616_THROUGH_T1_10 | 174/308/136; 616 | 1/2/1 | 000 | 30445 |
| VF97_C616_THROUGH_T1_100 | 174/308/136; 616 | 1/3/2 | 000 | 30445 |
| VF97_C620_QUAD_COLLAPSE_EXACT | 176/310/136; 620 | 1/2/1 | 000 | 31109 |
| VF97_C598_CYCLE18_G8 | 169/299/132; 598 | 27/29/54 | 000 | 28964 |

For the four new bodies, respectively, maximum primitive support-coefficient lengths are 525, 526, 217, 217 bits; individual centered-coordinate numerator/denominator maxima are 30431/30432, 30431/30432, 31095/31097, 28950/28951 bits. All have raw-coordinate maxima 292/293 bits. Their third integrations use 344, 344, 348, 334 positive tetrahedra. All three ordinary zero-count fields are zero. The bit-length distinctions matter: the rank-event cap has more expensive support coefficients without increasing its common centered denominator; the larger cyclic deletion reduces the mass-arithmetic cost.

## 1. Exact evidence and scope

The consumed immutable parent is **figure-0396**, SHA-256 **a2312bcd5094e74b2fbe922e30880be9be25931da68c1f0341fe7652ed9e2653**. Its complete 42-file capsule, not an alias, supplied the three original generators and complete verification sources. The recovered decoder was 90496 bytes, SHA e2dccd1f00286c28a1bc8806ea7d50c9a3a0e2480bbe9aa02f82f19b8024bea9. The present capsule scopes this evidence to the complete three original generators and consumed sources; no encoded unrelated case is required.

The fresh full A/B report hashes are:

```
A_G1067 e5359803ec5ceab18589e6e48138ac86c3aeb62700cb308ef2c24c863348d915
A_G388  125467bbf318278b4144dc6d8c1827bdc7eb1d10579235af94ded0800b5a6845
A_G458  568484b3919574dc4404ff640dfe9e3a5682e9ac85515141e668ff85ae69e881
```

No conflicting parent geometry was substituted. In A_G1067 the apex is **old raw-lex93**, not94; the extra unstable point is old99. Its owners are child supports57/71/134, whose parent labels are57/71/135. These are different indexing systems. The two parent stable roots in A_G388 are child3/38, and in A_G458 child3/45.

The research library was independently catalogued/searched and the relevant prior metric material was read, including figure-0392, SHA f7ab06ff50542624db5298c8e19c5c1f174c50f979e07bae78759b4341166fb7. Its existence is not treated as an orbit exclusion for these different bodies. The last complete navigation-brief read was revision1929, SHA6fa52a875b6d63345927f5a7df7afa3fe65bf353410f6d1bbb75f8d821fd8e81; it still reported no smaller own110. Other newly listed architectures were not silently imported as dependencies.

Projective centroid fitting is established background, not a novelty claimed here; see Ivan Izmestiev, *Fitting centroids by a projective transformation*, arXiv:1409.6176. The input-specific certificates and cap constructions below are the present findings.

## 2. Six-arrow root locking with the actual projective mass and every affine metric

For each parent, first translate by its exact own filled centroid. Let its centered vertices be Z and its centered polar vertices be P_f=n_f/(h_f−n_f·g). For any p with positive denominators, form Y_i=Z_i/(1+p·Z_i), compute the **uniform filled centroid c(p) of the new solid**, and use physical points Y_i−c(p) and polar points

`Q_f(p)=(P_f+p)/(1−(P_f+p)·c(p))`.

An arbitrary nonsingular affine linear part L gives physical metric M=LᵀL and polar metric M⁻¹. No eigenvalue, condition-number or closeness-to-identity bound is imposed on L.

An arrow i→j means a_iᵀM(a_j−a_i) in the physical case, or a_iᵀM⁻¹(a_j−a_i) in the polar case, evaluated at these **moved, own-centered** points. The following implication is exactly certified: if all six listed arrows are nonnegative and ||p||∞≤rho, both listed roots remain strict.

| Parent; domain | Six arrow premises | Forced roots | Certified rho |
|---|---|---|---|
| A_G1067; physical | 57→49, 96→99, 33→35, 145→147, 122→118, 168→171 | unstable vertices93 and99 | 1/2097152 |
| A_G388; polar | 29→19, 112→91, 11→1, 74→26, 13→37, 131→27 | stable physical facets3 and38 | 1/16777216 |
| A_G458; polar | 60→62, 62→94, 65→64, 81→45, 93→32, 1→31 | stable physical facets3 and45 | 1/33554432 |

Thus an own110 endpoint must leave the indicated projective box **or strictly reverse at least one listed arrow**. Merely allowing a premise arrow to reach zero does not evade this certificate. Root turnover is not prohibited by assumption: the two particular roots are conclusions within the stated chamber. Outside that chamber, or for larger p, the assertion makes no claim. In particular this is **not** a complete projective/metric-orbit exclusion. The boxes are conservative sufficient bounds, not maximal radii.

### Certificate mechanism

Put A(a,b)=sym[a(b−a)ᵀ]. For every neighbor j of each root r, the stored certificate is

`S=2^(−e_rj) A(r,j)+Σ_k (w_k/10^8)2^(−e_k) A(i_k,j_k)`.

All six integer weights are nonnegative. Each S is verified exactly to be strictly negative diagonally dominant, hence negative definite. There are47 target matrices for A_G1067 and24 each for A_G388/A_G458. The complete exponent and weight arrays are in the literal FRAME files inside the capsule. Taking trace against any SPD metric proves the root arrow negative whenever the six premise arrows are nonnegative. Testing all incident edges gives strict radial exposure. In the polar case radial exposure is equivalent to an interior perpendicular foot on the corresponding physical facet.

The persistence estimate does **not** freeze the centroid. For projective parameter increments,

`Dc=−5 E[YYᵀ]+4 ccᵀ`,

where the expectation is over the newly filled uniform solid. Let R bound the initial centered physical coordinates in infinity norm, Q bound the initial centered polar coordinates, and a=3Rrho<1. Along the entire parameter box the source uses

```
dy = R*a/(1-a)
dg = 27*R^2*rho/(1-a)^2
dz = dy+dg
Ephysical = 2*R*(dz+dy)+2*dz*dy
b = 3*(Q+rho)*dg < 1
dq = (rho+Q*b)/(1-b)
Epolar = 4*Q*dq+2*dq^2
```

Each escape-matrix entry changes by at most the appropriate E. If K is the sum of its nonnegative normalized coefficients, its diagonal-dominance gap decreases by at most3KE. The exact dyadic base-gap lower bounds still exceed3KE for the reported rho. Positive projective denominators preserve maximal incidence. This closes geometry, actual mass and all-SPD root inequalities in the same proof.

## 3. A finite exact root-turnover cap, and why its whole scalar family cannot finish

All coordinates in this section are in the original exact A_G1067 raw frame. Let

`u=X99, a=X96, b=X108, d=X64−X99, v(t)=u+t*d`.

For **0<t<1**, cut by the unique plane through a,b,v(t), retaining the origin side. The only old vertex removed is99; old96 and108 are exact contacts, not almost-coincident intersections. The new vertex is v(t). The maximal complex has **174 vertices,308 edges,136 facets** throughout this open interval. This saves two edges relative to the generic one-vertex triangular truncation and leaves two edges of headroom under310.

The two audited rational inputs are t=1/10 and t=1/100. At1/10 the new exact raw-lex unstable list is[93,97], with child97 **exactly equal to old96**; the saddle is97–108. At1/100 the unstable list is[93,96,99], where child99 is the new cut point, not the erased old99; saddles are96–99 and99–108. Both have unique stable facet3. Exact equality maps are regenerated by the replay.

There is also a complete **entire-family exclusion**, not merely a999-point scan. Define

`W=|det(a−u,b−u,d)|/6`,

and let V0,M0 be the exact parent volume and first moment. The removed region is exactly the tetrahedron[u,a,b,u+td], so

```
V(t)=V0-t*W
M(t)=M0-t*W*(2*u+a+b)/4-t^2*W*d/4
g(t)=M(t)/V(t).
```

For affine vertex paths x_i(t), every expression

`V(t)*(x_i(t)−g(t))·(x_j(t)−x_i(t))`

is a rational polynomial of degree at most3. The source proves strict negativity using exact Bernstein coefficients on rational intervals, with no floating sampling in acceptance. It also verifies the plane/support signs over the whole interval from their affine endpoint expressions, and independently matches the moment formulas to both fully audited rational endpoints.

The proof has two pieces. Old apex93 is strict unstable throughout[0,1]. On[1/100,1], old96 is also strict unstable, checking its four new neighbors87,92,108,v(t). On[0,1/100], the two-point pool{old96,v(t)} has strictly negative arrows to every adjacent point outside the pool. A greatest-radius member of that pool has a strictly negative arrow to the other member as well; it is a second unstable point. Therefore **every body in0<t<1 has at least two strict unstable equilibria at its actual filled centroid**. Weak events elsewhere are not excluded or counted for the whole continuum. This theorem does not cover an additional affine metric, projective deformation or movement of other supports.

The generated complete polynomial certificate is2149620bytes, SHA3fd569a10b7e265296f2e480371302be533130856fbc0baaee05db85a2c19307. It is not an unavailable dependency: `through_proof.py` regenerates every coefficient from the embedded parent and verifies it.

## 4. A fully exact false-small-loss endpoint

The C620 quadrilateral cap adds exactly this rational inequality to the parent:

```
(-2268252468891471/144115188075855872)*x
+(7238232549142285/4503599627370496)*y
-(6427399126840869/9007199254740992)*z <= 1.
```

It removes old96 and99. Its exact own class is121, not110. In its own raw-lex labels, the extra unstable point98 and nearby point97 satisfy

```
1/30000000 < |X98-X97| < 1/25000000
-1/5000000 < max_j escape_normalized(98,j) < -1/10000000.
```

The maximizing arrow is98→97; the return arrow97→98 is positive. But **every arrow from either member of{97,98} to every outside vertex is less than−1/25** after normalization by |a||b−a|. All348 outside pairs are verified by integer inequalities after exact centering. Consequently every vertex-to-vertex path from this pool to apex93 must incur a negative arrow of magnitude greater than1/25, despite the local defect being below2×10^−7.

This is a concrete failure mode for local maximum-escape loss: a nearly collapsed internal edge conceals a robust closed basin. It motivated the supplied minimax rooted-path routing and monotone re-routing line search. The certificate concerns this finite vertex set, not all possible inserted relay points or future geometries.

## 5. Cyclic caps can pay for releasing a nonsimple scaffold

For a generic one-plane cut, let v be the number of removed old vertices, D the number of edges internal to them, k the number of crossing edges, r=D−v+1 their connected cycle rank, and e=sum_removed(degree−3). Exact edge bookkeeping gives

`Delta V=k−v, Delta E=k−D=3−3r+e`.

Thus cutting a connected collection of degree-three vertices costs at most three edges, regardless of its size. More importantly, erased cycles can pay for removing nonsimple vertices. This is a combinatorial/geometric budget fact, not a mechanical cancellation theorem.

The exact C598 cyclic cap adds the particularly small row

```
87691904*x + 43103003*y - 194968361*z <= 100000000.
```

It removes22 old vertices, including the entire99–96–87 obstruction chain and old108. There are25 internal edges and17 crossings: r=4,e=1, hence Delta E=−8. Old input facets16,18,99,100 vanish; the new cut is a maximal17-gon. There are152 exactly unchanged old vertices and17 new intersections. Actual V/E/F is169/299/132, not a triangulation count. The complete removed list and cap cycle are generated and certified by `cap_budget.py`.

This gives **eleven edges of headroom** under310 and genuinely leaves the protected degree-four87 scaffold, unlike the scalar cap just excluded. Its own27/29/54 class shows the remaining joint geometry/mass limitation: deleting the old unwanted root and saddle region, even below budget, does not preserve the fragile opposite mechanical landscape when the material moves. It is retained as an inexpensive geometric/mass-reallocation seed, not presented as a promising110 endpoint merely because C is smaller.

## 6. Finite work, retained methods, and continuation

The optional production sources and `EXPERIMENTS.json` preserve the exact commands, inputs, nondefault options and versions. Completed work included36 attempted global projective/metric starts (34 recorded endpoints, two domain failures), four50-step full-contact/root-turnover runs, three200-step minimax contact runs,120 triangular-cap and120 variable-fan cap starts, four rooted-path cut continuations, the999-point scalar scan plus60 projective/metric scalar-cap starts, and75 cyclic-cap starts. None yielded an accepted own110.

The three complete-adjacency MILP screens each made six90-second-bounded outer-PSD refinements. All18 returned incumbent matrices were indefinite. Their positive surrogate margins are therefore **not physical metric solutions**, and time limits/outer relaxations are not infeasibility certificates. No global metric exclusion is inferred from them.

Exact source and all seven retained physical inputs take priority over optimizer histories. Low-dimensional frozen endpoints and terminal diagnostics are included. Unsuccessful high-dimensional free-control iterates were not designated exact successors. Both SLP seed13 rows are preserved literally, not reconstructed from a similarly named later run. Optional numerical dependencies are CPython3.13.5, NumPy2.3.5, SciPy1.17.0 with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1. Cross-build bit-identical optimizer trajectories are not promised; exact acceptance uses only the standard library.

The most useful next move is **intentional exit from the six-arrow chamber coupled to a genuine geometry change**, checking global rooted reachability rather than only each vertex's best local arrow. For A_G1067 the arrow96→99 is an explicit obstruction witness, but the simple two-contact cap proves that merely handing the unstable role from99 to96 cannot close the mass/roots. Releasing the87 scaffold with cycle-paid facet loss is a concrete alternative; the C598 row is a fully exact seed with room for compensating geometry. The undeformed scalar cap family is closed by the theorem; its larger joint projective/metric/contact space remains open. No claim here forces the old roots to survive after the stated hypotheses are abandoned.

## 7. Standalone recovery and observed verification

Save the complete following Python block as `RECOVER_VF97.py`, then run:

```
python -B -S RECOVER_VF97.py VF97_RECOVERED
python -B -S VF97_RECOVERED/REPLAY.py --workers 4
```

Do not use `-O`. The decoder recovers51 files and verifies all50 manifest entries. `REPLAY.py` reconstructs three parents and four new nonwinners, runs the independent strict446/weak123 and invalid-input controls, all A/B/third-mass audits, three live-mass frame certificates, the entire scalar-family certificate, the exact local-loss barrier and both cap-budget receipts. It asserts the frozen full report hashes, not just counts.

Dictionary233652bytes SHA7f00138c4a87b5874e8becb2e2d188fdf5fbda47941c23029d589a35ea0bd67c; XZ58512bytes SHA8984209562095a08ad2c3937b5c908d66a4caa9d05b0afa420c97a95f544b94d; base6478016characters SHAced4bd9f0c7eb37b688f210b6d5b1ca590aaba2cac36a575f6747eae8f3c8342. Decoder79983bytes SHA0ee31362550f8348e361123436ffc6ea72c0f385f2c59f251a38e43bc66fdbb9. Both the selected-source cold replay and a separate decode-to-new-directory replay completed with `VF97_COLD_SOURCE_ONLY_THREE_PARENTS_FOUR_NONWINNERS_AB_MASS_ALL_CERTIFICATES_PASS 5519 c2c2911210ec4ee5f0d2d45ad5671ccac2f566e2409aa28c05bcd63079b9f751`. Their final report bytes matched. All continuation-critical arrays, generators, exact new rows, production and verification helpers are included below; the supplemental files are not dependencies.


[Encoded source block omitted; the code in this passage is incomplete.]


Supplemental copies: standalone decoder (`RECOVER_VF97.py`), complete source, exact reports and working evidence (`VF97_COMPLETE_RESEARCH.zip`), and the same complete handoff JSON (`VF97_RESULT.json`). These downloads are conveniences; the capsule above is sufficient.
