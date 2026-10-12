# figure-0318

AI research report · 2026-09-05 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NH13-NFSC-R567: exact rational successor, C3384

## 1. Determination and provenance

**The new finite homogeneous convex polyhedron has (V,E,F)=(567,1692,1127), strict own-volume-centred (S,U,H)=(1,1,0), and C=3384. C<1000 is not achieved.** The counts use actual maximal facets and true edges, not display triangles. Relative to the material parent NH13-B5375-NO55-R943/C5644, this removes376 vertices and1130 true edges, reducing C by2260, or **40.04%**.

The material parent is the literal R943 archive, SHA256 `4c7699bcbc0ca03fa159821023a3534f5c3afdc69785ab0bb912c26304bdc173`. Its943 vertices,2822 true edges and1881 maximal facets remain a different body. The earlier immutable assignment `figure-0314` belongs to R1213, not R943; no new immutable assignment identifier for R943 was supplied in this continuation. There is no source-authority conflict: the new endpoint is separately defined by its complete literal rational data below.

This is **not frozen-pool deletion**. Low-degree fields in source-normal parameters move the geometry, a directed-ascent objective creates shorter routes from the stable region, the critical collar moves with the ordinary filled-body centroid included in every numerical screen, and source-aware contractions replace vertices. The final coordinates are then promoted to a seven-decimal rational lattice and independently re-centred and completely verified. The original B5375 source is unchanged; I do not claim that the modified finite shape is a sampling of a newly proved smooth Gömböc.

A second new result delimits continuation: within the stated actual-centroid band, frozen C2 subsets of this567-point pool with triangular nonbase facets have **C>=1048**, or C>=1056 when retaining the full hexagonal base. This excludes that restricted deletion-only finish, not moved coordinates or general low-complexity Gömböcs.

## 2. Exact finite definition

The capsule in section8 contains every raw integer vertex, every oriented triangle and the complete portable proof. It needs no numerical hull, previous archive or optimizer. Define

```text
D  = 10000000
V6 = 1775115502582929931214
M24= (-2116553767312804881806725088,0,0)
C0 = 887557751291464965607
B0 = (-264569220914100610225840636,0,0)
Q  = 8875577512914649656070000000
v_i=(C0 I_i-B0)/Q.
```

Here I_i are the decoded raw integer triples in canonical lexicographic order. These constants are not trusted input to the mass proof: the replay recomputes

`V6=sum_f det(I_i,I_j,I_k)`,
`M24=sum_f det(I_i,I_j,I_k)(I_i+I_j+I_k)`.

It obtains C0=4V6/g and B0=M24/g for g=gcd(4V6,M24_x,M24_y,M24_z), and Q=D C0. The exact ordinary volume is

`887557751291464965607/3000000000000000000000`, approximately0.2958525837638216552.

The raw ordinary centroid is `(gamma,0,0)`, where

`gamma=-66142305228525152556460159/2218894378228662414017500000`, approximately-0.02980867673445834860.

This is the unique root of the linear centring equation `4 D V6 gamma-M24_x=0`. Translation by this computed point merely expresses the uniformly filled body in its own-centroid coordinates. All three centred first moments are separately reintegrated and equal exactly zero. There is no freely positioned mechanical centre, altered density or hidden point mass.

### Critical features and global radii

The unique stable facet is a hexagon with cycle `[0,3,4,5,2,1]`. Raw rows0..5 are

```text
(-3903112,-791250,-2929749)
(-3903112,-614454,-2966118)
(-3903112,-126669,-2374039)
(-3903112,126669,2374039)
(-3903112,614454,2966118)
(-3903112,791250,2929749).
```

The unique unstable vertex is566, raw row `(4698782,0,0)`, with12 true neighbours. The centred axial coordinates are

`S_x=-3199668088844631794614428348/Q`,
`U_x=4435009606642912944250631310/Q`.

The inradius r is approximately0.3605025232655416514, maximum radius R approximately0.4996868767344583486, and r/R approximately0.7214568563847204986. The certificate checks **all** supporting-plane distances and **all** vertex radii: the stable facet uniquely attains the minimum support distance, and the apex uniquely attains maximum radius.

There are1130 outward display triangles and1695 triangulated edges. Three exactly coplanar internal diagonals triangulate the stable hexagon. Removing them gives1692 true edges and1127 maximal facets:1126 triangles and one hexagon. The complete true-edge table and maximal-face cycles are reconstructed by the capsule.

A geometry detail matters for replication. At the573-row checkpoint, seven-decimal promotion made two near-cap collar triangles exactly coplanar with the base, enlarging the former quadrilateral to a true hexagon. The final branch resumed from that exact rounded geometry, not the preceding floating quadrilateral. This is an actual coordinate change followed by exact support and mechanics checks, not tolerance-based face merging. The final567 rows underwent a fresh separate promotion and verification.

## 3. Executed full acceptance

The primary standard-library verifier reconstructs connected closed oriented two-manifold incidence, every vertex link, Euler characteristic2, all1130 positive radial determinants, every exact hinge and exact coplanar components. Each maximal facet is a single cycle; **each oriented boundary edge puts every other vertex of its polygon strictly on its interior side**. Every listed vertex has three linearly independent incident supporting normals.

It executes **639009 exact maximal-plane/all-point support comparisons**, checks each complete equality-contact set, and proves every asserted maximal facet is a genuine facet of the convex hull. Together with the closed outward degree-one boundary these certify the actual whole convex hull. The independent generic ray(5,7,19) lies strictly in exactly triangle599, with no boundary cone or zero cone-side signs. Qhull was only a discovery tool.

For each true edge i->j, use centred numerators P and oppositely oriented incident outward normals N_f,N_g:

```text
p=P_i dot(P_j-P_i), q=P_j dot(P_i-P_j),
u=N_f dot(P_i cross P_j), w=N_g dot(P_j cross P_i).
```

A saddle requires p<0,q<0,u>0,w>0. The first two conditions put the perpendicular line foot strictly inside the edge; the last two test both components of the full normal cone. Stable facets require all their boundary side tests positive; unstable vertices require all outgoing vertex dots negative. Weak versions detect degenerate equilibria. Every true feature is tested. Result: **one stable facet, one unstable vertex, no saddles, no degeneracies, and no zero true-edge primitive**. The saddle conclusion is not inferred from Euler's equilibrium identity.

A second distinct inherited exact implementation reads the new rational table and independently passes its volume, manifold, coplanar-face, rank-three cone and exhaustive mechanics checks, using the different ray(3,11,17). The two executed statuses are `EXACT_RATIONAL_GOMBOC_PASS` and `INDEPENDENT_EXACT_AUDIT_PASS`. These are software-independent replays within this research, not external mathematical peer review or proof-assistant formalization.

The regular tetrahedron fixture gives(4,4,6), and six deliberately invalid/nonwinning fixtures are rejected. The exact raw OBJ is read as Fractions and compared vertex-for-vertex and facet-for-facet; centred OBJ and binary STL are checked as display approximations. No fabrication-tolerance claim follows from their decimal or float32 coordinates.

### Certified centring neighbourhood

The common strict axial primitive-sign chamber containing the actual gamma is

```text
-2279125819/76179000000 < c
< -32068298661035469140803/1076866755419419240000000.
```

All7898 affine guards stay strictly signed through `gamma±1/100000`:1130 radial face-plane guards and four guards for each1692 true edge. For fixed raw geometry each guard is a-D c b. Its sign at gamma is that of C0 a-B0_x b. The exact replay verifies

`|C0 a-B0_x b| > C0 D |b|/100000`

for every guard. This is an actual mechanical neighbourhood of the one physical centring root; it is not a maximal class interval, a coordinate-perturbation tolerance, or permission to choose another mechanical centre independently of mass.

## 4. Successful geometric mechanism

### Preserved source and a warning about offsets

The source remains B5375, e=43/800, with filled horizontal disks of radius sqrt(1-z²) and centre e(f(z²),z g(z²)). Its full ascending lists are

```text
f=[1,-6369176696657/744797625000,23934959/5375000,
   14614229/268750,-43952184/134375,167391552/134375,
   -378236032/134375,476622336/134375,
   -311093248/134375,3284992/5375]
g=[78131603/21500000,-30554969/5375000,-59706319/1343750,
   197504148/671875,-872518688/671875,105637424/26875,
   -990534144/134375,1099447296/134375,
   -663220224/134375,167575552/134375].
```

The source's exact volume4pi/3, centroid0, strict convexity and two equilibria S=(-757/800,0,0), U=(843/800,0,0) were replayed. With t=z²,

`H=f²+t g²`, `J=(1-t)H`, `L=-J'-1/10`,
`Kc=(1-t)^3[(2f'+4t f'')²+t(6g'+4t g'')²]`.

Exact Bernstein coefficients are positive for H-1/2 on two halves,25-H on the whole unit interval,L and L²-e²J(H')² on two halves, and (19/20)²-e²Kc on four quarters. Exact principal minors also give both physical critical half-Hessians>(1/100)I. The capsule contains the complete Fraction implementation and rational inputs; it executes rather than trusts these statements.

The reference normal image remains `Y(n)=X_B5375(n)-(11/20)n`. It is **not** assumed a convex parallel body. At the source U, putting a=78131603/400000000 and d=13297526696657/6928350000000 gives tangent support derivative `J_U=[[1+a²/d,a/d],[a/d,1/d]]`, with

`det(J_U-(11/20)I)=-20401119871098485973333/851041708586048000000000<0`.

The capsule rechecks this fold exactly. Neither the identity Y cross n=X cross n nor the original source gap is used to transfer equilibrium counts to the modified finite shape.

### Low-degree fields in source parameters

Every point carries a source-frame label n, paired by C2. These labels are **auxiliary search parameters, not asserted current outward normals**. For Legendre polynomial P_a, use scalar fields

`h(n)=P_a(n_x) n_z^(2b)(n_y n_z)^c`,

where a,b>=0,c in{0,1},a+2b+2c<=d. Displacements include -h n; when degree<=d-2 they also include h times each of `(0,-n_z,n_y)`, `(0,n_y,n_z)` and `(0,n_z,n_y)`. Add the three axial fields `(n_z^(2j)(1-n_z²),0,0)`, j=1,2,3. Initial ordinary fields are zero on the base and nonconstant fields zero at the apex. Later add six critical controls: common cap x-displacement, the four entries of its in-plane yz linear map, and apex x-displacement.

These are additive raw-world-coordinate deformations. They move the source-normal image's finite realization rather than only deleting its points. Degrees5,6,7,8 and10 were tried. An SVD preconditions the flattened fields, retaining singular values>10^-6 and scaling orthonormal fields by sqrt(V). At each numerical step the current triangulation supplies differentiable volume/centroid formulas. Central differences of step10^-7 form a small LP maximizing selected normalized face/vertex exclusion margins. Initial parameter trust is.0003, accepted trust grows by1.15, rejected trust shrinks by.4, and backtracking tests powers of1/2. These numerical constants are discovery settings, not proof tolerances.

The decisive change was a **directed-ascent shortcut objective**, not only increasing the smallest local margin. At the actual current volume centroid c, build the all-point graph with i->j when `(v_i-c) dot(v_j-v_i)>0`. Choose a shortest base-to-apex path and target disjoint two-edge skips along it. The LP maximizes their minimum normalized radial-ascent margin, scaled by max(|initial target margin|,1/1000), while retaining existing exclusions above max(2e-7,.15 times the initial selected minimum). Each proposed endpoint rebuilds the actual hull, reintegrates its filled-body centroid and reruns the complete numerical face/vertex/edge screen before acceptance. Topology changes are permitted; no infinitesimal LP prediction substitutes for the actual endpoint check.

This moved an849-point checkpoint's shortest numerical base route from153 to96 before vertex removal. The eventual exact comparison is stronger: at their respective actual centroids the parent943 pool's shortest positive-ascent path from its base is176 edges, while the new567 pool's shortest is79. Both comparisons use all ordered point pairs, not merely currently incident edges.

### Contractions tied to the deformed source image

Let A be the exact reference frame printed below, and set residual `R_i=v_i-A Y(n_i)` using raw coordinates. For an edge i,j, take alpha in{1/2,1/4,3/4}, normalized n=alpha n_i+(1-alpha)n_j, chord q=alpha v_i+(1-alpha)v_j, and

`surf=A Y(n)+alpha R_i+(1-alpha)R_j`.

Try q+beta(surf-q) for beta in{1,1/2,0,3/2,2}; use only beta0 when |surf-q| exceeds.8 times the original edge length. Move the C2 partner by exact reflection, protect the current cap and apex in this contraction routine, and accept only after recomputing the actual hull and ordinary centroid. The residual term is important: projecting back to the undeformed source would discard the successful normal-field changes.

The final two paired contractions used a bounded three-coordinate patch search. Its basis is the old edge direction, the perpendicular component of n_i+n_j, and their cross product, scaled by edge length. Bounds are[-.48,.48],[-.45,.65],[-.55,.55]; Powell uses xtol10^-5,ftol10^-7,maxiter10,maxfev160 and RNG seed8819. A strict negative complete numerical defect below-2e-7 triggers an actual hull/centroid recount. It accepted two C2 contractions in40041 evaluations. These numerical searches are not proofs of global optimization or continuum class preservation.

### Actual branch and discarded alternatives

The main branch is normal-field conditioning of the943-row restart, deletion to889, and source contractions. It then uses the **saved849-row checkpoint**, not the same run's later837-row endpoint. Shortcut conditioning, deletion and contractions reached657. Four subsequent flow/deletion/contraction stages had row counts

```text
657 -> 641 -> 623
623 -> 619 -> 607
607 -> 603 -> 579
579 -> 579 -> 573.
```

An independent max-margin-only branch ended at619 and was inferior. The final branch promoted573 to exact seven-decimal geometry, added critical-collar controls, deleted one pair to571, accepted two paired patch contractions to567, and finally promoted and exactly verified the new567 table. Unsuccessful parameter variants or numerical stopping rules are not global lower bounds. No exact certificate for the entire historical numerical path is claimed; the accepted endpoint is independently proved from its literal data.

## 5. Exact ascent evidence and a scoped lower bound

The replay tests all321489 ordered pairs of the new567-point table at its exact ordinary centroid. It finds1922 positive arcs. Reverse BFS from566 yields stable-cycle distances `[88,79,89,88,79,89]` and maximum distance107. The rank-string SHA256 is `46105b4253974882dacd108a704bcd8e98fae9e7c343b7a37ffaeeb0494cb23e`; the complete rank and actual witness paths are reconstructible from the capsule. The separately checked R943 pool has3162 positive arcs and stable-cycle distances[176,189,176,189]. This measures genuinely shorter available radial-ascent routes, not just removed display triangles.

**Scoped theorem.** Consider a C2-invariant convex hull of a subset of these fixed567 raw points, with no extra degenerate equilibria, and suppose its ACTUAL ordinary centroid is `(c,0,0)` with `|c-gamma|<=10^-5`. If its class is(1,1,0) and all nonbase maximal facets are triangular, then C>=1048. Retaining the full six-point base gives C>=1056.

For K=100000 and d=I_j-I_i, the outer positive-arc test is the exact integer inequality

`K(C0 I_i dot d-B0_x d_x)+C0 D |d_x|>0`.

It contains every real positive radial-ascent arc throughout the entire centre interval. Reverse BFS followed by an exhaustive all-pairs rank audit gives C2 base-pair ranks79,88,89, with no violating arc. Exact coordinate grouping finds a single axial point566 and a single equal-x group of at least three points: the negative six-point base. A unique unstable vertex must be566 by symmetry. A unique stable facet must be axis-normal and must use four or six base points; the positive-x support is only the apex.

A quadrilateral base contains at least two C2 pairs, hence a point of rank at least88; the hexagon contains a point of rank89. Every nonunstable vertex needs a strictly positive adjacent radial witness, and these paths strictly increase squared radius. A path and its half-turn image share only the apex, since distinct paired nonaxis points have equal radii. Therefore the quad case requires V>=177 and the hex case V>=179. For one maximal k-gon and otherwise triangular facets, C=6V-2k-6, yielding1048 or1056. Without the triangular-side hypothesis the degree bound is only C>=532, not an exclusion of C<1000.

This does not constrain moved coordinates, nonsimplicial side facets, another symmetry or another source. A subset whose own centroid leaves the interval is also outside its scope; leaving the interval must result from changing the actual body, not moving an independent mechanical centre.

**Next construction gate:** shorten the two slower base-orbit routes88 and89 while preserving the complete actual-centroid mechanics, or change the restricted facet architecture. Improving only the fastest79 route misses the proven obstruction. With a hexagon and triangular sides, C<1000 requires odd V<=169, so each paired base-ascent route must fit within84 edges. That is necessary, not sufficient: global inball coverage, actual mass and every mixed normal cone still need the full finite certificate.

## 6. Continuation without the numerical filesystem

The capsule contains not only all exact vertices and triangles but also567 source-frame integer labels L_i at scale10^9. Normalize n_i=L_i/sqrt(L_i dot L_i). The exact reference affine matrix is

```text
A=[[1,0,0],
   [0,2251557855505727/2251799813685248,
      -8740830045692191/147573952589676412928],
   [0,0,4504138944756847/4503599627370496]].
```

The supplied vertices already contain all deformations: **do not apply A to them again**. A is used only to evaluate the reference source image and residuals for new proposals. The auxiliary labels are not geometric normal certificates. The normal-image support map can be reconstructed from the source lists: for unit n with h=|n_h|, solve the unique source root

`n_z-h z/sqrt(1-z²)+n_h dot c'(z)=0`,

then `X_B(n)=(c(z)+sqrt(1-z²)n_h/h,z)`; vertical normals use the poles. Use Y=X_B-(11/20)n and the residual formula above. This makes a new source-aware numerical restart possible from the handoff alone. The final exact object itself needs none of this numerical evaluation.

Canonical raw little-endian signed-int64 hashes are

```text
I: 2a6c9c815509ee1ced6fdb4df29f372d6c4a073a4ba2e7f52cbf2f1c858576ca
F: 2b9ce889355545780f2dd4572cbffb4465032963f1d5786de3bdc1be625ac360
labels: a9c3db096c716fbd4460fd4e3c5b7f2809206f108339ec00b6d106d75105df56.
```

The inner literal stream has SHA256 `ae957fa2524ca98af5c0a59cf812772d4d7bc9016740186b062de98fdb411a7f`. It stores283 half-turn representatives plus one axial point, with source labels and1130 oriented triangles. The outer self-contained text capsule has SHA256 `d611ce8d28c77aaa60568213ce88462094e51e21d6d3e59e1ee58f4577c95ec8`, expanding36223 bytes. It includes the literal data, source/frame definitions, complete standard-library global verifier, centre-interval checker, exact ascent and frozen-rank checkers, source certificate and fixtures.

No global minimum, C<1000 success, prize eligibility, fabrication tolerance, external peer review or proof-assistant certification is claimed. The exact finite successor, not an unchanged parent or a source-only margin, is the constructive result of this continuation.

## 7. Archive and fresh replay

[Verified exact tables, both implementations, source-frame restart, construction scripts and display meshes](sandbox:/mnt/data/NH13_NFSC_R567_VERIFIED.zip).

[Complete self-contained handoff](sandbox:/mnt/data/NH13_NFSC_R567_HANDOFF.md).

The archive is **249473 bytes**, SHA256 `361471aa063dc22bdeeb4978a31d101b6bd7cd6bd4b0628579b75c873831749e`. Its fresh extraction completed `NH13_NFSC_R567_ARCHIVE_REPLAY_PASS` with both implementations. All76 manifest entries passed before and after replay. The raw and centred vertex tables, triangles, source labels, definition, maximal faces and true-edge table were reconstructed byte-for-byte in a separate temporary directory. The exact source, offset-fold, centring interval, full ascent graph, scoped frozen-pool theorem and fixtures were also executed. The final archive bytes were unchanged after replay.

## 8. Complete literal reconstruction and exact proof

Save the following block as a Python file and run `python3 -S` without `-O`. It expands the complete checksum-validated text capsule and executes the standard-library global convex-hull, ordinary-centroid, full-equilibrium, centring-chamber, ascent, scoped-rank, source and fixture checks. No prior file, numerical hull, optimizer or nonstandard package is required. The second implementation and numerical construction history supplement this self-contained proof in the archive.


[Encoded source block omitted; the code in this passage is incomplete.]
