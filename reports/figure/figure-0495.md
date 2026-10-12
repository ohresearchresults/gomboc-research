# figure-0495

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Clear Willow 56 — finite mass descent and a complete material-envelope obstruction

## Result

No strict110/additionalweak000 polyhedron was obtained. The complete labelled three-dimensional insertion chart requested in the assignment is now **excluded**, and the exclusion is stronger than a one-point or fixed-incidence result:

> Let P be the exact C186_OBLIQUE_APEX_U1_211 parent. Retain all its supporting halfspaces except those of facets14 and45. Every uniformly filled convex polyhedron K that contains P and satisfies those sixty retained halfspaces has at least two strict stable equilibria at its own volume centroid.

Thus arbitrarily many inserted points, intermediate carrier changes, and a second mass patch cannot cancel the stable basin while remaining inside this material envelope. The theorem does not assume preservation of U1, the saddle, a particular polar packet, or an escape tree.

Five finite exact bodies were fully audited: the parent's previously unobserved dyadic C192 witness, three farther C192 ray members, and the C180 outer envelope. The largest promoted U1 ray member is strict211/weak000 at t=1/3. Its complete polar birth/death ratio decreases by approximately **0.17665%** from C186; its basin remains deep and grows from32/32 to33/33 vertices/cut edges. A rigorously isolated physical-root birth occurs at t≈0.343026422042, after which the ray has two unstable vertices. These finite and continuous results replace the prior unobserved constructor status; none is a target110 construction.

## 1. Sources and execution boundary

I read the supplied journal through EOF, including the complete literal parent `figure-0491`, metadata SHA-256 `c467cb1e5178b0d64c9256a4c8531e7deeaafc90da6dadc4fd47c29b14a5caed`. Unchanged earlier evidence was retained rather than restarted. The current journal has264,694 bytes and SHA-256 `699b90e7aeef2d2bb1e99713a24d1e65d526015a428e53d4680e849017833db0`.

The parent's standalone Python unit was extracted without scientific modification:15,369 bytes, SHA-256 `8d69bf2e689022bb21622586b8ca5990ce562413ff094dc7072da643fad7ef3a`. It repeats the complete C186 input from `figure-0487`, SHA-256 `5899754f372a6a6c9505e188fb34f224c3c3c828a0077ce3556c5cb4341cf428`.

Temporary runtime files were lost during executor restoration, then reconstructed from the supplied literal source. The final three-unit capsule was replayed in a fresh directory and matched all seven report byte counts and hashes. There is no missing exact dependency for this result. Earlier numerical submissions without retained outputs remain unavailable and establish no trajectory, optimum, or exclusion here.

## 2. Geometry and label convention

Write the parent's physical vertices as P0,…,P32, with T=P31, D=P32, and its31 planar base rows as supplied in the recovery capsule. The actual uniform centroid is zero. Its exact volume is

`V0=108039116315266993463971/375000000000000000000000`.

Old top facet i is `(31,i,(i+1) mod31)`; old bottom facet31+i is `(32,(i+1) mod31,i)`. The parent has S=[15,31], U=[31], H=[(15,16)], no additional weak equilibria and no primitive zeros. Physical vertex31 and polar vertex31 are different objects.

Let `m=(P14+P15)/2`. The two-face insertion cell is

`C={x: Q14·x>=1, Q45·x>=1, Qi·x<=1 for i not in{14,45}}`,

where Qi are the parent's normalized outward supporting functionals. Its strict interior means that every displayed inequality is strict. In that interior, append x as vertex33; retain the old facets except14/45; append

`(31,14,33), (31,33,15), (32,15,33), (32,33,14)`.

This gives V34/E96/F64, C192. Old edge14–15 disappears and four spokes appear. The report's retained-face map sends old15→new14 and old31→new30.

### Complete spatial cell

Exhaustive rational enumeration of all **37,820** triples of the62 signed planes gives five vertices. In lexicographic coordinate order, their complete active-old-plane sets are

```text
[14,15,45,46]
[13,15,44,46]
[14,44,46]
[13,15,45]
[13,14,44,45]
```

The first and last are P15 and P14. The middle four-plane vertex is

`z=(-13641318018177446432729/27891505886943550000000,
     9561217833368790481703/13945752943471775000000,
     10120761/100000000)`.

The full cell has5vertices/9edges/6facets. A rational strict-interior witness is the mean of its five vertices. Boundedness is established by the independently reconstructed outer envelope below, not assumed from the list of finite intersections.

## 3. The outer envelope and its actual-mass capacity

Delete old supporting planes14 and45 altogether, and retain the other sixty. Their intersection is exactly

`O=conv(P union {z})`.

Old vertices14 and15 become redundant: they lie on the extended neighboring edges. The active vertex list is old0,…,32 excluding14/15, followed by z. Replace every occurrence of14 or15 in each retained facet by z, then use the active-list indexing. Exhaustive supporting-triple enumeration proves that these sixty triangles are the complete maximal hull. Their planes are checked to coincide exactly with all sixty retained old planes. Consequently O is bounded and contains the entire insertion cell.

The outer envelope has V32/E90/F60, C180, and its complete own-centred audit is strict222/weak000/primitivezero000. This is a new C186-lineage C180 control, **not** the unrelated SC83 compact-H C180 body.

Its additional volume satisfies the exact inequality

`0 < (Vol(O)-V0)/V0 < 11/5000`.

The ratio is approximately0.00219881691457. Thus the entire permitted envelope contains less than0.22% extra volume relative to the parent. This is a finite mass-capacity calculation, not a claim that a small displacement generally preserves equilibria.

### General integral certificate

For an old stable triangle f and one of its three barycentric coordinates, let `ell_fj(c)` be that coordinate of the perpendicular projection of c onto the old facet plane. It is an affine function of c. Set

`b_fj=ell_fj(0)`,

`m_fj=min_{x in O} ell_fj(x)`,

`N_fj=V0*b_fj+(Vol(O)-V0)*min(0,m_fj)`.

The minimum is evaluated exactly at every vertex of O. For any uniformly filled convex polyhedron `P subset K subset O`, with actual centroid g and volume VK,

`VK*ell_fj(g)=integral_K ell_fj(x) dx >= N_fj`.

Since `VK<=Vol(O)` and every N_fj is positive,

`ell_fj(g)>=N_fj/Vol(O)>0`.

The original stable triangle remains on a supporting plane of K. A foot strictly inside that original triangle is also strictly inside the containing maximal face of K, even if the latter becomes larger. Thus both stable equilibria persist without requiring the rest of the incidence to remain fixed.

### Exact numerical-free lower bounds

The regenerated certificate proves these simple strict lower bounds for the three barycentric coordinates, in the parent's oriented triangle order:

| Old facet | First coordinate | Second coordinate | Third coordinate |
|---|---:|---:|---:|
|15|3/8|9/50|21/50|
|31|2/3|17/100|7/50|

All six comparisons hold for **every** K between P and O. This proves the theorem in the opening paragraph and closes the complete labelled finite chart against110. There is no root-transfer loophole: U and H may change arbitrarily, yet S>=2.

As a separate direct check, I pulled the exact two-face volume/moment map back to the five-vertex simplex representation of C. All90 degree-two Bernstein coefficients of the six volume-cleared stable barycentric coordinates are strictly positive. The output preserves every coefficient. This direct cell certificate is narrower than the material-envelope theorem but provides a useful independent algebraic check of its one-point consequence.

## 4. Observed finite constructions

The original source's dyadic search now terminates at

`delta=1/16384`, `x=(1+delta)m`.

This is the first successful member in its declared search order k=8,9,…, delta=2^(-k). It is an observed C192 strict211/weak000/primitivezero000 construction, not a pending nomination.

For farther finite motion, use the exact planar ray

`x(t)=(1-t)m+t*z`, `0<t<1`.

Unlike the radial dyadic insertion, this ray keeps the inserted vertex in the base plane. All its interior points lie strictly in the same two-face visibility cell. The following endpoints have exhaustive maximal hull, actual volume/moment, strict/additional-weak S/U/mixed-H, and complete P/Q audits:

| Report identity | V/E/F | S | U | H |
|---|---|---|---|---|
|C192_EDGE14_15_MASS_DESCENT_211|34/96/64|14,30|31|15–16|
|C192_PLANAR_T_1_4|34/96/64|14,30|31|15–16|
|C192_PLANAR_T_1_3|34/96/64|14,30|31|15–16|
|C192_PLANAR_T_3_8|34/96/64|14,30|31,33|14–33;15–16|
|C180_TWO_FACET_RELAXED_ENVELOPE|32/90/60|14,30|29,31|13–31;14–31|

All five have additionalweak000 and primitivezero000. The three C192 ray reports use the same old-to-new face map as the dyadic body. The C180 report has its distinct active-vertex map; vertex29 there is old T, and vertex31 is z.

### Whole landscapes and the actual size of the descent

The parent Q birth/death ratio is approximately12.020381407484. The dyadic witness gives12.020305946443; the quarter ray gives12.004478970752; the third gives11.999147130068. The corresponding third-ray birth-relative depth is approximately0.916660743538. This is still a deep basin, not near cancellation.

Every U1 endpoint has Pbars empty. Its sole Q bar has peak30, elder14, death edge14–44, and the complete33/33 packet

```text
component = [29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,
             45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,63]
cut = [[0,29],[0,30],[1,31],[2,32],[3,33],[4,34],[5,35],[6,36],
       [7,37],[8,38],[9,39],[10,40],[11,41],[12,42],[13,43],
       [14,44],[15,45],[16,46],[17,47],[18,48],[19,49],[20,50],
       [21,51],[22,52],[23,53],[24,54],[25,55],[26,56],[27,57],
       [28,29],[28,58],[60,63],[61,62]]
path = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,63,62,44,14]
```

The t=3/8 body has this same Q packet and one new P bar: peak33→elder31, component[33], cut[[14,33],[15,33],[31,33],[32,33]], attaining path[33,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,31], death edge14–33. Its positive birth-relative P depth is approximately0.000733235068; it is retained, not thresholded away.

The C180 envelope has a materially different physical packet: peak31→elder29, component[31], cut[[13,31],[14,31],[29,31],[30,31]], death edge13–31, path[31,13,12,11,10,9,8,7,6,5,4,3,2,1,0,29]. Its Q packet is the complete bottom ring30,…,59, with cut[[i,30+i] for i=0,…,29], peak30→elder14, death edge14–44, and path[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,14]. Its P/Q birth-relative depths are approximately0.037666867228 and0.917691187446 respectively. The outer envelope is therefore a useful finite root-transfer control, not an improvement in every basin metric.

Every exact birth, death, tied level, cut, path and chord-min domination check is regenerated by the inline source. No positive P/Q feature is omitted.

## 5. Complete physical-root decision on the ray

Let V(t),M(t) be the exact actual mass of the insertion body. For a directed true edge i→j, define the volume-cleared score

`D_ij(t)=[V(t)P_i(t)-M(t)] dot [P_j(t)-P_i(t)]`.

Each is a polynomial of degree at most3. On the full closed parameter interval[0,1],67 exact Bernstein certificates prove: one positive escape for every old nonroot; all exits from T strictly negative; and all exits from vertex33 except33→14 strictly negative.

The remaining score `g(t)=D_33,14(t)` has a strictly negative derivative throughout[0,1]. In fact every Bernstein coefficient of -g' is greater than9/1000. Its unique zero t* lies strictly between343/1000 and43/125. A further exact bracket is

`294657453181/858993459200 <= t* <= 147328726591/429496729600`.

Consequently, for every interior ray parameter:

- `0<t<t*`: exactly one strict U, namely T, and no additional weak-U;
- `t=t*`: T is strict U and vertex33 is additional weak-U;
- `t*<t<1`: exactly two strict U, T and33, and no additional weak-U.

The full mixed-H and S census is certified at the finite endpoints in the table, not asserted by this vertex theorem alone. The independent material-envelope theorem already gives S>=2 everywhere. Thus the root birth is an exactly located finite obstruction to U1-preserving motion on this ray, not a failed numerical line search.

## 6. What must change next

The local cone did lead to real finite whole-bar descent, but the complete admissible mass envelope cannot remove either stable equilibrium. A staged second insertion that remains below the same sixty planes is now ruled out regardless of its point count or intermediate incidence. A genuine continuation must violate at least one more retained support, remove some original material, move retained geometry, or change the metric. None of those larger families is excluded here.

The neighboring retained carriers13/44 bound the upstream side of the patch;15/46 bound the saddle side. Releasing another carrier is therefore a concrete geometry change, not a repeat of the closed chart. The observed birth of U33 also shows why larger additions need coordinated physical escape reconstruction rather than preservation of the original tree at all costs. No all-SPD, all-bipyramid, arbitrary-insertion, or global complexity exclusion is claimed.

## 7. Verification tier and source-only recovery

Each finite endpoint has one complete exhaustive integer/rational maximal-hull and mechanics implementation. Positive tetrahedral mass integration agrees with all three coordinate-divergence volume and moment identities. Face-foot barycentric membership agrees with same-centre polar-U classification; every mixed edge is tested through its segment parameter and two adjacent-normal cone coefficients. Full P/Q landscapes batch equal levels and verify every complete-graph chord against true-edge bottleneck capacity. These are cross-checks within one full auditor, not two independent full auditors.

The exact replay used CPython3.13.5, standard library only, assertions enabled. No numerical optimizer, external package, parent file, or network retrieval is needed. The capsule contains three complete units:

```text
C186_mass_basin_descent.py  15369 bytes
SHA256 8d69bf2e689022bb21622586b8ca5990ce562413ff094dc7072da643fad7ef3a
C192_FINITE_CHART.py       10137 bytes
SHA256 8a7856bb4c728093786bf96f4fc2f3ac95f1bf2ca51471ce396b081c90f5f7e7
REPLAY.py                  1680 bytes
SHA256 b3bff576f3008cc9c2d4ad8f0ce758e333dcff18d6bde76f1db77a2dd00bc6d4
```

Commands:

```text
python -B -S RECOVER_C192_FINITE_ENVELOPE.py OUT
cd OUT
python -B -S REPLAY.py
```

Observed final markers:

```text
C192_COMPLETE_FINITE_ENVELOPE_SOURCE_RECOVERY_PASS 3
C186_PARENT_FULL_RECONSTRUCTION_PASS
C186_OPEN_CONE_MASS_BAR_DESCENT_PASS
DELTA 1/16384 EXPONENT 14
C192_STELLATION_211_WEAK000_FULL_AUDIT_PASS
C186_FULL_TWO_FACE_MATERIAL_ENVELOPE_S_GE_2_PASS 32 60
C192_FULL_3D_VISIBILITY_CELL_S_GE_2_PASS 5 90
C192_PLANAR_RAY_EXACT_U1_TO_U2_SINGLE_EVENT_PASS 67
C192_FINITE_MASS_CHART_FOUR_EXACT_BODIES_AND_ENVELOPE_PASS
C192_FIVE_EXACT_BODIES_SEVEN_COLD_RECEIPTS_PASS 7
```

Observed seven-report manifest:

```text
C186_EDGE14_15_DESCENT_CERTIFICATE.json
5028 58f4ba76b39aef026eb486960afae6f807652f2ee1fa448f1c73cd05523c3ee4
C192_EDGE14_15_MASS_DESCENT_211.json
521741 b10fe326c5f4fc9c41bb1c69e985809e7015e639b5cdb9a17be1c68e23ea3a0f
C180_TWO_FACET_RELAXED_ENVELOPE.json
446800 85377973bfba1141f661fb230f096f13a541deb1c8ca2e6a39fde8c65e8894f7
C192_PLANAR_T_1_4.json
483169 184d99e675f1207a8ddd133c994ca6f8be40581a3a4e61ba26018cb8fe601717
C192_PLANAR_T_1_3.json
478541 5616ab86b93f58e61ed7df013fc49d67f0173db134ae475b514ab0e7da9a56ea
C192_PLANAR_T_3_8.json
486985 1afed6f6ddacd4880e67b29f7ace9422034fff847832d24482805818a563b9fa
C192_FINITE_CHART_CERTIFICATE.json
153888 b6ff8f020eaf4989e0dab5ea5289e5fea7e2ae7f2ffedc638489298c9f163bbb
```

The source dictionary has27,937 bytes, SHA-256 `9821e87bdf743b8e1b9732bc2e3c40623e9b6b1cf5e41d9fba3bde6e3694ce1b`; its XZ payload has9,464 bytes, SHA-256 `ca4ae42b3f179d6a8d34a1a1254285ef7cf3662677c08543c924a1b922946839`. The decoder has12,746 bytes, SHA-256 `f6922c845714c89d5b73102476ab89764000261820427224f20717a250e6b15c`.

A convenience copy is RECOVER_C192_FINITE_ENVELOPE.py. The complete decoder follows inline; it reconstructs all exact source and input bytes independently of that link.


[Encoded source block omitted; the code in this passage is incomplete.]
