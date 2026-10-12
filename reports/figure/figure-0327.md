# figure-0327

AI research report · 2026-09-06 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Rapid Atlas 04 — exact homogeneous monostable construction and correction of the preceding normal-pool claim

## 1. Result

**No strict homogeneous (1,1,0) winner is obtained in this continuation.** A new explicit rational C3-invariant polyhedron has, however, been constructed and independently checked at its actual uniform-volume centroid:

**RA04-H139-S1U16-R: (V,E,F)=(274,411,139), (S,U,H)=(1,16,15), with no degenerate equilibria.**

Its true-edge budget is **2E=822**, below1000. Its formal mechanical complexity is **792**, because its total equilibrium count is32. These quantities must not be conflated.

This is a genuinely homogeneous **monostable** finite body, but not mono-monostatic. It removes the extra-stable-face difficulty at the accepted endpoint while leaving five threefold orbits of extra unstable vertices and saddle edges. It does not dominate the original79-point parent in equilibrium count or edge count, and it is not a completed stable–saddle cancellation without replacement births.

The new body is defined by47 literal integer support-plane representatives below. It has a different point table, different normal directions and different incidence from the immutable79-point parent. In particular, its274 vertices versus the parent’s79 prove that it is not an affine image of that parent.

**An important correction comes first:** the preceding handoff’s claimed global obstruction for arbitrary offsets of the parent139 normals was not proved. Its advertised replay actually failed, and a fresh exact calculation refutes its decisive numerical inequality. That obstruction and its claimed normal-direction neighborhood are withdrawn. The original79-point parent and its separately verified results remain intact.

## 2. Withdrawal and exact replacement of the erroneous normal-pool certificate

The recovered `C3_NORMAL_GATE_PROOF.zip` contains a run report with `proof_replay_pass:false`. Its `normal_obstruction.py` stops at the assertion `bound < 15/16`. The proposed independent check then fails because the expected certificate report was never generated. The external archive replay records returncode1, not a successful replay.

Thus the preceding final answer incorrectly described that packet as having passed. The original failed packet and reports are preserved under `withdrawn/` in the new archive, rather than silently overwritten.

Let `N_i` be the139 lexicographically sorted primitive outward integer normal directions of the literal79-point parent, and let `b=(-1,-1,-1)`. For positive dot products define

`w_ij=(N_i·N_j)/|N_i|²`.

Let `k_i` be the maximum product of these weights along a path from `i` to the base normal, with `k_b=1`. The quantity used in the preceding claimed obstruction was

`A=max_i k_i(N_ix+N_iy+N_iz)`.

Two executed exact calculations now establish

```text
2016784457297341/10^15 < A < 2016784457297342/10^15.
```

In particular, **A>2**, not `A<15/16`.

The maximizing normal has lexicographic index85 and is

```text
(67132522,67132522,-1854005).
```

The base normal has index79. An exact attaining path, with37 edges, is

```text
85,81,83,91,89,87,93,132,117,136,130,134,105,113,121,101,
64,54,58,56,23,65,48,9,27,17,5,16,28,29,10,11,13,15,
19,51,31,79.
```

Multiplying the rational weights along this path and multiplying by the coordinate sum of normal85 gives the displayed value of A. The generated potential also satisfies every required inequality

`k_i |N_i|² >= k_j(N_i·N_j)`

for all10045 ordered positive-dot pairs. The separate checker reconstructs the normal pool from the parent’s actual maximal facets, checks all10981 parent plane–point supports and complete contacts, checks those10045 rational inequalities, and reconstructs the path product independently.

Consequently the preceding claims of a universal `H_base/60` positive centroid residual and a `2^-14` excluded normal-direction neighborhood **must not be used**. The present calculation does not prove that a homogeneous monostable body exists with the unchanged parent normal pool; it establishes that the offered exclusion certificate was false.

The conditional general criterion remains valid: if a finite unit-normal pool rooted at the proposed stable normal has maximum positive cosine-path product times inward-axis projection `B<1/3`, then the support-height and slab-centroid argument excludes homogeneous monostability at that reference. Here the correctly normalized quantity is `B=A/3`, approximately0.6722614858, so the criterion gives no exclusion.

The previously specified B64 and A2 direction sets remain mathematically well-defined finite pools. They are not, however, demonstrated escapes from an established normal-pool obstruction, because the purported obstruction for the starting pool has been withdrawn.

## 3. Complete exact definition of RA04-H139-S1U16-R

Each row below is an integer quadruple `(a,b,c,h)`. For a nonaxial row impose all three inequalities obtained from the normal vectors

`(a,b,c)`, `(b,c,a)`, `(c,a,b)`,

with the **same** right-hand side h. For the final axial row, impose it only once. No normalization or rounding is part of this definition.

Let K be the intersection of these139 closed halfspaces. Fill K at constant density1. Let g be its actual rational uniform-volume centroid, computed from the complete finite boundary as specified in Section4. The exact own-centred body is

`P=K-g`.

Here are all47 representatives:

```text
-3537051546 -2990639257 -8862593556 11778694258
-3671407290 -3067046706 -8781092450 11364646869
-3821701306 -3204096917 -8667517153 10895930736
-4325670271 -3512121474 -8303778773 10256165977
-5056576301 -4112760547 -7584001052 10001000050
-6515379464 -4635425899 -6005493981 10001500113
-7746183927 -4821250182 -4089902241 10001000050
-8673899386 -4023556702 -2927784461 11909694297
-8673899386 -2949139232 -4007929925 11917107228
-8673899386 -4015375241 -2938998671 11915787335
-8129393684 -4205676685 -4028173331 10256165977
-8673899386 -2311302703 -4406388002 11917208756
-8673899386 -2990639257 -3977059520 11912117110
-8680823158 -2251585570 -4423641931 12027117211
-5298129428 -4056578691 -7448040046 10001000050
-8673899386 -2344053190 -4389053567 11916467438
-8673899386 -2829334506 -4093406547 11916467438
-8667517153 -3204096917 -3821701306 10895930736
-8673899386 -2655640340 -4208175379 11915787335
-8673899386 -2499104417 -4302967292 11915787335
-7818061266 -4347653408 -4469435604 10001440089
-6282935981 -5836617377 -5143921712 10000894447
-5317779615 -6550241758 -5368077551 10001000050
-4486316730 -8255939869 -3422689781 10493958050
-4337663020 -8934198707 -1168275396 13103905617
-4144172726 -9080205783 607471356 13418412231
-3597782450 -9080205783 2144913559 13484410703
-4623743719 -7323573257 -4998915555 10001500113
-3833516930 -9080205783 1688378163 13483713463
-2857147074 -8549379864 4330833284 13533189990
-2582338017 -7303546856 6323730267 13645995442
-2536937490 -9080205783 3340611182 13532177830
-2306025873 -7944391792 5618302499 13564537201
-4167288150 7557782179 5050882431 13426811639
-2189759039 7252618433 -6527201694 13645995442
-2444427129 7755600341 -5820709904 13564537201
-4258893017 6397735754 6397735754 12640126401
-2133812641 6908216882 -6908216882 13714688357
-2431486568 7415666563 -6252716084 13648923584
-3252589149 8086583752 4901417345 13532177830
-4640699025 6263533914 6263533914 12904723409
-4472135955 8944271910 0 13390056641
-4391625278 8843032467 1586111746 13483713463
-2501065878 8297807512 4990037927 13564537201
6259235355 6259235355 -4652294582 12922585549
6268024867 6268024867 -4628562367 12891354218
-5773502692 -5773502692 -5773502692 10000000000
```

The UTF-8 text consisting of these47 rows, one space between integers and a trailing newline after every row, has SHA-256

`f09e73df8aa01fac0bffca815f02d5769f37812ce369209c6598139a0475bcbc0ab`.

The inequalities are rational as printed. Although their numerical proposals were near unit-normal form, the integer vectors must not be treated as exactly unit vectors.

### Actual axial supports

For `l(x)=(x+y+z)/3`, the raw body K has attained extrema

```text
l_min = -2500000000/4330127019,
l_max = 2819168529/3952836620.
```

The latter is attained at the sole axis vertex, which has all three raw coordinates equal to `2819168529/3952836620`. Its canonical vertex index is209. The stable supporting plane is exactly

`-5773502692(x+y+z)=10000000000`.

These are not the parent’s old axial supports. The construction does not try to place mass into the old79-point reference chamber while retaining its old attained slab.

## 4. Deterministic reconstruction of every vertex, maximal facet, true edge and moment

This recipe uses only the47 rows above and exact integer/rational arithmetic.

### Vertices

Expand the cyclic orbits in the printed order. For every triple of planes `(n_i,h_i),(n_j,h_j),(n_k,h_k)`, calculate

```text
d = det(n_i,n_j,n_k),
p = h_i(n_j cross n_k)
  + h_j(n_k cross n_i)
  + h_k(n_i cross n_j).
```

Discard triples with d=0. If d<0, negate p and d. Retain the candidate `p/d` precisely when

`n_l·p <= h_l d`

for every one of the139 inequalities. Divide the homogeneous quadruple `(p_x,p_y,p_z,d)` by the gcd of its four entries. Deduplicate the retained quadruples and sort the resulting rational points lexicographically by their three actual coordinates.

This defines the canonical indices0 through273 used below. The executed builder examined all437989 plane triples and performed3302847 exact supporting comparisons while constructing the candidates. It produced274 distinct extreme vertices, not a list containing redundant points.

### Maximal facets and true edges

For each supplied plane, collect all reconstructed vertices satisfying its equality exactly. Project that contact set onto two coordinates complementary to any nonzero normal coordinate. Compute its ordinary exact two-dimensional convex hull with the monotone-chain algorithm, removing collinear interior points. Orient the resulting boundary cycle so that its cross product points along the supplied outward normal. A cycle may be rotated to start at its smallest vertex index without changing the geometry.

Every one of the139 supplied planes is active. These cycles are the complete maximal facets. True edges are exactly the deduplicated unordered consecutive pairs in the cycles, including their closing pairs.

The actual counts are

```text
V=274, E=411, F=139.
Face-size distribution:
3:4, 4:33, 5:30, 6:36, 7:21, 8:9, 12:3, 19:3.
```

Fan-triangulating each maximal cycle gives544 outward triangles and816 triangulated edges. Exactly405 triangulation diagonals are coplanar display diagonals. They are not included in E.

The implementation additionally proves complete contact sets, convexity of every polygon by all boundary-edge/all-polygon-vertex halfplane tests, global plane–point support, connected oriented boundary topology, single-cycle vertex links, and rank-three supporting normal cones at every listed vertex. The source H intersection and the certified complete convex boundary therefore define the same body.

### Uniform volume and all three first moments

Let `v_i=p_i/d_i` be the reconstructed raw rational vertices. For the outward fan triangles `(i,j,k)`, put

`Delta_ijk=det(v_i,v_j,v_k)`.

The exact raw volume and raw first moments are the finite rational sums

```text
V = (1/6) sum Delta_ijk,
M = (1/24) sum Delta_ijk (v_i+v_j+v_k),
g = M/V.
```

These sums are a complete exact reconstruction of the mass data; no quadrature, smooth-body approximation, auxiliary density or vertex average is involved. A second implementation obtains the same rational answers from nonnegative tetrahedra with a boundary vertex as apex, rather than from the origin-based signed sum.

The actual exact volume satisfies

```text
6547872790145/10^12 < V < 6547872790146/10^12.
```

The three raw centroid coordinates are exactly equal. Writing `g=(gamma,gamma,gamma)`, their exact value is the rational number defined by the preceding finite sums, and it satisfies

```text
2/10^12 < gamma < 3/10^12,
gamma ≈ 2.93898998510011 × 10^-12.
```

The exact own-centred coordinates are therefore

`x_i=p_i/d_i-gamma(1,1,1)`.

The first checker directly re-integrated their centred moment numerators and obtained

**`M_x=M_y=M_z=0` exactly.**

All mechanical counts below were evaluated at this exact own centroid, not at the nearby numerical origin. The numerical interpolation root used during discovery is not part of the final definition.

The full literal rational moments are stored in both independent reports. Their large numerator/denominator strings are unnecessary for reconstruction: the47-row H table, the deterministic intersection/facet recipe, and the displayed finite sums define them exactly.

## 5. Complete equilibrium census and exact margins

### Stable facet

There is exactly one stable maximal facet, with outward cycle

```text
[55,103,79].
```

### Unstable vertices

There are exactly16 unstable vertices:

```text
0,101,109,127,133,151,163,185,189,192,209,224,249,263,266,269.
```

Their C3 orbits are

```text
[209]                         — the sole axis vertex
[0,101,224]
[109,133,263]
[127,151,266]
[163,185,269]
[189,192,249].
```

These are canonical indices of the new274-point rational table, not indices of the79-point parent or of a numerical Qhull table.

### Saddle edges

All15 saddles are the following true edges:

```text
[104,108], [112,120], [120,127], [134,140], [143,148],
[148,151], [165,189], [182,192], [189,209], [192,209],
[209,249], [249,267], [260,262], [264,265], [265,266].
```

**There are no degenerate equilibria.** There are also no zero primitive signs in the first checker’s complete true-feature mechanical ledger.

### Direct mixed-normal-cone test

For a centred edge from a to b, let `d=b-a`, `L=d·d`, `T=-a·d`, and `W=L a+T d`. Let n,m be its two outward incident normals. The Gram determinant is

`G=|n|²|m|²-(n·m)²>0`.

The two normal-cone coefficient numerators are

```text
beta_n=(W·n)|m|²-(W·m)(n·m),
beta_m=(W·m)|n|²-(W·n)(n·m).
```

A strict saddle requires all four quantities

`T, L-T, beta_n, beta_m`

to be positive. Both independent full implementations tested every one of the411 true edges. The15 listed edges pass; all396 others have a strict exclusion. The saddle count was not inferred from Euler’s relation.

### Positive exact bounds

Conservative rational lower bounds for the first checker’s normalized predicates are:

| Predicate family | Strict bound |
|---|---:|
| Every nonincident support distance | >1/20000 |
| Minimum stable-face side margin | >3/50 |
| A negative side witness for every nonstable face | >1/20000 |
| Every unstable vertex’s minimum adjacent-edge cone margin | >1/1000 |
| A positive escape witness for every nonunstable vertex | >1/50 |
| Every saddle’s minimum four-component margin | >1/1000 |
| A negative component for every nonsaddle edge | >1/20000 |

For a common-denominator centred table `Z_i/Q`, the face-side normalization is

`N·(Z_a cross Z_b)/(||N|| ||Z_b-Z_a|| Q)`;

the endpoint/vertex normalization divides the corresponding radial dot product by `||Z_b-Z_a|| Q`. The edge test uses the two endpoint conditions and the two incident-face side conditions, whose signs are independently checked against the Gram coefficients. Integer ceilings of square roots supply rational denominator bounds.

These are strict margins for this one exact body. They are not a claim that arbitrary coordinate rounding, independent support perturbations or manufacturing errors of the same size preserve the body.

## 6. Executed independent acceptance

The new finite body has passed three implementations on the same exact data.

**First implementation.** The complete inherited integer checker validates the reconstructed maximal planes and every point against them, full contact sets, all polygon halfplanes, topology and links, rank-three cones, actual ordinary mass, exact centred-moment re-integration, and the full face/vertex/true-edge census. It executed38086 maximal-plane/point comparisons and4638 polygon halfplane comparisons on the new body.

**Second implementation.** The inherited separate Fraction checker was actually run, not merely included. It treats the boundary cycles as certificates to be checked, independently integrates boundary-apex tetrahedra, computes literal perpendicular feet, tests vertices against every other point, and solves every two-normal Gram cone. It returned the same exact volume, centroid, stable facet,16 unstable vertices,15 saddle edges and zero degeneracies.

**Third implementation.** A new independent homogeneous-integer checker imports neither the builder nor the first geometry checker. It separately validates all inequalities and contacts, polygons, links and normal ranks; performs boundary-apex mass integration; tests literal face feet; performs74802 global ordered vertex-support tests; and directly classifies all411 edge Gram cones. It agrees exactly with the other two implementations. Its homogeneous-integer formulation avoids repeated large-denominator Fraction reductions in the mechanical tests.

The frozen archive was then extracted into a new directory and its own replay executed. That fresh replay rebuilt the H polyhedron, reran two complete independent body checks, regenerated and independently checked the correction certificate, replayed the original79-point parent, tested exact raw translation by `(17,17,17)`, rejected five deliberately corrupted inputs, and verified mesh readback. Its terminal status is

**`C3_CORRECTION_AND_EXACT_S1_NONWINNER_FRESH_REPLAY_PASS`.**

The report explicitly records `new_winner:false`. Software independence here is not independent human peer review or proof-assistant formalization.

### Mesh exports

The OBJ uses the139 maximal polygons. The ASCII STL uses544 triangles. Both are labelled **display approximations of the raw rational body**, not alternative exact geometric definitions.

Fraction-based readback verifies every displayed coordinate against its exact rational source with error below `10^-49`, and checks every face and triangle. No claim is made that treating those rounded decimals as a new exact body preserves all mechanical properties. The rational inequalities, homogeneous vertices, maximal cycles and exact centroid are authoritative; the405 display diagonals remain excluded from the edge budget.

## 7. What was changed geometrically

The search starts from the parent’s facet-direction pool, not from a substitution of new coordinates into the parent’s name. Each nonaxial C3 normal orbit receives two independent tangent-direction variables. The normal representatives are moved non-affinely and then normalized numerically for proposal generation.

For the proposed unit normals, support heights are generated by shortest paths from the negative axial normal. A positive penalty `p=10^-5` is added to each nonroot step. If j is the selected predecessor of i, the assigned heights satisfy

`h_j=h_i(n_i·n_j) exp(-p) < h_i(n_i·n_j)`.

Thus the perpendicular foot of plane i is excluded by another support. The root plane has the smallest support height and remains stable. This provides origin-relative monostability during proposal generation, but it does not by itself centre the ordinary volume or control unstable vertices.

The actual finite hull’s volume and first moments were therefore evaluated inside the search. A bounded normal-direction optimization produced a negative axial moment after3814 numerical evaluations; the first retained negative centroid coordinate was approximately `-0.00094885114`. Interpolating the normal parameters from the positive-moment initial state to that proposal and rebuilding the actual finite hull gave a scalar numerical root near

`t=0.8090556303650835`.

This was only a discovery checkpoint. Its normals and heights were converted into the literal rational support table in Section3. The final actual rational H intersection was rebuilt from all plane triples, its own exact centroid was recomputed, and all mechanics were audited there. Neither a numerical root nor a frozen obsolete moment polynomial is used as the acceptance certificate.

The result is not a certified continuous deformation preserving the parent’s old equilibria throughout. It is a new finite endpoint built from a non-affine normal architecture. Its unique stable face, changed attained supports and new full incidence are real, but the remaining unstable/saddle orbits mean the requested complete cancellation is not finished.

## 8. A concrete next construction: moment-balanced noncritical cuts

The newly accepted own-centred S=1 body supplies a useful finite starting point for a different operation. The following preservation statement is valid independently of the withdrawn normal-pool claim.

Let an origin-monostable convex polyhedron K have inequalities `n_i·x<=h_i`. For a prospective nonzero normal w, define

```text
L(w)=min_{n_i·w>0} h_i |w|²/(n_i·w),
U(w)=max_{v in K} w·v.
```

Whenever

`L(w)<t<U(w)`,

the new halfspace `w·x<=t` makes an active cut, but its perpendicular foot `t w/|w|²` lies strictly outside the original K. Therefore the new face cannot be stable at the origin.

Every retained old nonstable supporting plane remains nonstable, since its old foot was already outside K. The unique old stable-plane foot remains strictly inside the cut: K contains its centred insphere of radius r, and

`w·p_stable <= |w|r <= L(w)<t`.

Consequently **any finite collection of cuts satisfying this strict condition relative to the original K preserves origin-relative S=1**, including all newly formed mixed incidences. This is not a claim that U or H is preserved, and it is not own-centroid preservation.

The physical continuation is to choose C3 cut orbits removing positive and negative axial first moments, then close the actual combined solid moment. In a fixed actual H-incidence cell, vertices are affine in the varying cut heights, volume is at most cubic, and the first moments are at most quartic. A moment root must be isolated inside a cell with the complete correct incidence; a circuit crossing requires rebuilding both the hull and moment polynomial.

This construction is a more specific next step than another unrestricted metric polish. It directly retains the already solved stable-face condition while permitting unstable–saddle basin removal. All remaining unstable orbits and saddle edges are listed in Section5 for selecting complete basins rather than isolated vertex truncations.

With139 starting normal directions, up to nine further threefold normal orbits give at most166 facets. Every three-dimensional convex polyhedron satisfies `E<=3F-6`, so this enlarged architecture still has

`2E<=6·166-12=984`.

A preliminary numerical cut screen was checkpointed with100 completed records retained. No exact cut successor was promoted, and the full scheduled scan was not completed. Those records do not establish an obstruction. Local numerical indices in that research screen are not canonical indices of the exact274-point table.

## 9. Parent identity and reproduction of the corrected normal calculation

The immutable parent is still `figure-0315`, SHA-256

`e2b1da58f6541c81b1649deadff55ddf618432bf0bec32fa489310b5795e350e`.

It remains the79-point body with `(V,E,F)=(79,216,139)`, own class `(4,1,3)`, edge budget432 and formal mechanical complexity426. Its exact stable facets are `[0,1,2]`, `[32,61,62]`, `[31,60,61]`, `[30,62,60]`; its sole unstable vertex is78; its saddles are `[0,1]`, `[0,2]`, `[1,2]`. These identities agree with the integrated parent record. 

For a self-contained reconstruction of that parent’s normal pool and the correction in Section2, use the following26 integer representatives:

```text
-455879583 -240434162 -589953430
-416144786 -207644525 -634038674
-362763803 -183227013 -677087572
-297169994 -168366266 -716267620
-221242218 -163613381 -748900894
-137190745 -168869864 -772597345
-47433098 -183400025 -785373637
45534869 -205869305 -785755303
139267703 -234405319 -772860969
231494193 -266677427 -746468445
320231636 -299988928 -707063854
403885596 -331372522 -655877734
481329739 -357671959 -594918524
551959521 -375573161 -527031744
615711991 -381483126 -456075162
673038997 -370816834 -387630902
724833518 -333464548 -333464548
771946352 -282279914 -282279914
813484194 -225505733 -225505733
848224962 -162872370 -162872370
874670621 -94048491 -94048491
890912573 -18590944 -18590944
894380950 64159157 64159157
881316953 155320218 155320218
845435090 257164713 257164713
773185820 375952703 375952703
```

For representative `(a,b,c)` at index j, assign `(a,b,c)`, `(b,c,a)`, `(c,a,b)` to indices `3j,3j+1,3j+2`, and append apex `(577350269,577350269,577350269)` at78. Divide by `10^9` for its raw physical coordinates.

To reconstruct its outward normal pool, enumerate all79079 point triples. Discard collinear triples and planes with points on both sides. Orient every remaining supporting plane outward, divide its normal by the positive gcd of its coordinates, deduplicate, and sort lexicographically. This yields the139 normals used in the corrected path certificate, with base index79.

The exact maximum-product potential is computed without logarithms or square roots. Initialize `k_b=1` and all other values to0. At each maximum-product Dijkstra step, finalize the unprocessed index having greatest rational priority `k_i² |N_i|²`; relax a positive-dot neighbor i from j using

`k_i=max(k_i,k_j(N_i·N_j)/|N_i|²)`.

Normal-length factors telescope around cycles, so cycle products are at most1. A maximizing path can be simple. The acceptance checker nevertheless does not trust the search algorithm: it verifies all pair inequalities, all positive values, the root value1, and an attaining path product. The37-edge path in Section2 is sufficient on its own to refute the preceding `15/16` bound; the super-potential additionally verifies the stated global maximum.

The parent’s original two complete geometric implementations and auxiliary checks were replayed successfully again. The later erroneous normal certificate does not invalidate that finite parent.

## 10. Portable artifacts and exact replay record

The complete proof packet is [C3_RECOVERY_AND_MONOSTABLE.zip](sandbox:/mnt/data/C3_RECOVERY_AND_MONOSTABLE.zip).

```text
Size: 1196344 bytes
SHA-256:
c674cc9e3464c24be46365eb4d90bfda9482da5866d0df44f9a51e4cd1405e97
```

It contains the47-row exact H definition; deterministic all-triples H constructor; complete rational homogeneous vertices, maximal facets and true edges; exact volume, centroid and feature reports; all three full checkers; the independently checked correction certificate; the original valid parent; the explicitly withdrawn failed packet; display meshes and rational readback; corruption fixtures; exact translation tests; and a self-contained standard-library replay.

The numerical construction programs, retained proposals, root checkpoint and partial cut-screen records are in [C3_RECOVERY_RESEARCH.zip](sandbox:/mnt/data/C3_RECOVERY_RESEARCH.zip).

```text
Size: 1108945 bytes
SHA-256:
713462c425507d33ad9bba59a90763481da05390d3b489d6335ae01690193f02b
```

The actual fresh-extracted replay report is [C3_RECOVERY_ARCHIVE_REPLAY.json](sandbox:/mnt/data/C3_RECOVERY_ARCHIVE_REPLAY.json). Archive sizes and hashes are also recorded in [C3_RECOVERY_DELIVERY.json](sandbox:/mnt/data/C3_RECOVERY_DELIVERY.json).

After extraction, run

`python -S REPLAY.py`

without `-O`. No optimizer, numerical geometry library or external source is required for the exact replay. The supplementary slower Fraction implementation can also be rerun with `python -S AUDIT_NEW.py`.

**Final disposition:** one new, fully reconstructed and independently verified homogeneous C3 monostable nonwinner with true-edge budget822; an explicit correction of the preceding false normal-pool certificate; and a concrete moment-balanced cut architecture for the remaining unstable–saddle orbits. The strict `(1,1,0)` target, minimality, a universal C3 exclusion, and manufacturing tolerance are not claimed.
