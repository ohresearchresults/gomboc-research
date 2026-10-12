# figure-0209

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Quartz 58 — exact two-page higher-valence continuation beyond `E21D`

## Literal disposition

**EXACT MATERIALIZED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The run’s acceptance gate requires a finite uniform-density body evaluated at its own exact volume centroid, strict `(S,U,H)=(1,1,0)`, complete H/V incidence and full face/vertex/true-edge-cone audit, an open perturbation certificate, independent replay, and matching OBJ/STL; auxiliary-centre, wall-point, or unexpanded-generator claims do not qualify. :contentReference[oaicite:0]{index=0}

The strongest new endpoint is `E18P`, an exact dyadic own-centred convex polyhedron with actual `(V,E,F)=(18,48,32)` and strict `(2,2,2)`. This genuinely advances the accepted `E21D` frontier: the journal records `E21D` as exact `(21,57,38)`, strict `(2,2,2)`, with a `2^-22` box and a chamber theorem forcing `U>=2` on `K={E,U,V,12}`, and names a two-page higher-valence replacement on the two prescribed boundary routes as the next topology. :contentReference[oaicite:1]{index=1}

`E18P` removes the complete old component `K`, old vertex `Q`, stable face `[E,Q,T]`, unstable vertex `U`, and saddle edges `(12,L),(A,S)`. It preserves stable `[8,A,B]` and unstable `8`. Two new internal supports `W,X` form interacting pages joined by true terminal edge `(W,X)`. The old packet is not cancelled: it transfers to stable `[8,W,S]`, unstable `X`, and saddles `(2,A),(L,X)`.

## Immutable package

- [Portable exact archive](sandbox:/mnt/data/vivid_quartz_58_two_page_nonwinner.zip)
- [Archive SHA-256](sandbox:/mnt/data/vivid_quartz_58_two_page_nonwinner.zip.sha256): `001f448a0bafa751198da695b06bc2060ce5a1c153d92e153bf6f23fb43158ac`
- [Complete determination](sandbox:/mnt/data/vivid_quartz_58_two_page_result/RESULT.md), [README](sandbox:/mnt/data/vivid_quartz_58_two_page_result/README.md), [one-command verifier](sandbox:/mnt/data/vivid_quartz_58_two_page_result/[internal-source-reference].sh), [64-entry manifest](sandbox:/mnt/data/vivid_quartz_58_two_page_result/SHA256SUMS), [verification record](sandbox:/mnt/data/vivid_quartz_58_two_page_result/VERIFICATION_RECORD.json)

A clean replay ends with `ALL VIVID QUARTZ 58 TWO-PAGE VERIFIERS PASS`; the ZIP independently passes its integrity test.

## 1. Exact shared-disk replacement

The common oriented boundary is

```text
S-8-T-L-10-B-C-F-M-N-A-2-S.
```

The `E21D` source disk has internal vertices `{12,E,Q,U,V}`, disk f-vector `(17,36,20)`, and faces

```text
[S,8,T] [Q,S,T] [E,Q,T] [E,T,L] [E,L,U]
[N,S,Q] [N,Q,E] [A,N,S] [2,S,A]
[12,U,L] [12,L,10] [12,10,B] [C,12,B] [C,F,12]
[M,N,E] [M,12,F] [V,12,M] [V,M,E] [V,U,12] [V,E,U]
```

The replacement disk has internal vertices `{W,X}`, disk f-vector `(14,27,14)`, and faces

```text
[X,8,T] [X,T,L] [X,L,10] [X,10,B] [X,B,C] [X,C,F]
[W,F,M] [W,M,N] [W,N,A] [W,A,2] [W,2,S] [W,S,8]
[X,F,W] [W,8,X]
```

The `X` page spans `8-T-L-10-B-C-F`; the `W` page spans `F-M-N-A-2-S-8`; `[X,F,W]` and `[W,8,X]` are the spine. Boundary edges have multiplicity one, all other disk edges multiplicity two, both disks have Euler characteristic one, and the exterior 18-face complex is identical. Globally `(21,57,38)->(18,48,32)`.

Coning the 14 target triangles to the exact interior centroid yields 14 strictly positive tetrahedra. The two spine tetrahedra share internal triangle `[C,W,X]`, certifying finite three-dimensional thickness. Their exact total volume is

```text
1739497585365113934490508120751528780273262473364403011757
/29513880418164048124803073006681710421119043118984419344384.
```

Evidence: [patch complex](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E21D_to_E18P_patch_complex.json), [positive-volume cell certificate](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_two_page_volume_cell_certificate.json), [source reconstruction](sandbox:/mnt/data/vivid_quartz_58_two_page_result/source_E21D/E21D_exact_report.json).

## 2. Complete exact V-data and mass identities

Use `D=2^32=4294967296`. Before centring, `p_i=Q_i/D` with

```text
1  (58844160,-5395534092,-117496829)
2  (267008661,-3094734758,-652127596)
8  (-375347060,-10994278980,1301546589)
10 (-541756230,-6829637577,1885168973)
11 (-470080785,-9407288968,1526257071)
A  (525950923,2908560895,-1181704787)
B  (135168286,1241948876,63114684)
C  (162037644,7553732993,-929476944)
F  (483745352,5786557867,-1134738606)
L  (-483981081,956312969,657533427)
M  (479336169,5569692411,-1278060452)
N  (442580752,4950029481,-1288390153)
P  (-554548590,-8103727805,1596949959)
R  (-41201552,-5501163806,35861817)
S  (-9620656,-7026758,-662532711)
T  (-586864245,-6391139553,1438175701)
W  (-121995504,13343842065,-1699588828)
X  (-267498447,13442385035,-1326128851)
```

The physical body is `conv{Q_i/D-C}`. Exact ordinary volume and uncentred first moments are

```text
V  = 15521564282171723625413335881/158456325028528675187087900672
Mx = -4858309014304638259830609817773500843/2722258935367507707706996859454145691648
My = 1602109567775524195661150183070529957/63802943797675961899382738893456539648
Mz = -29519513394207512738995694064424043159/8166776806102523123120990578362437074944
```

and the exact ordinary-volume centroid is

```text
Cx = -4858309014304638259830609817773500843/266658443898757075308403328364633391104
Cy = 1602109567775524195661150183070529957/6249807278877118952540703008546095104
Cz = -29519513394207512738995694064424043159/799975331696271225925209985093900173312.
```

The Fraction verifier proves `M_j=V C_j` exactly for all three coordinates, so centred first moments are exactly zero.

## 3. Actual maximal faces and every true edge

All 32 maximal faces are triangular and irredundant:

```text
[1,2,8] [1,S,2] [1,8,R] [1,R,S] [2,A,8] [2,W,A]
[2,S,W] [8,10,11] [8,B,10] [8,11,P] [8,A,B] [8,P,T]
[8,S,R] [8,W,S] [8,T,X] [8,X,W] [10,P,11] [10,B,X]
[10,L,T] [10,X,L] [10,T,P] [A,F,B] [A,M,F] [A,N,M]
[A,W,N] [B,F,C] [B,C,X] [C,F,X] [F,M,W] [F,W,X]
[L,X,T] [M,N,W]
```

All 48 true edges are

```text
(1,2) (1,8) (1,R) (1,S) (2,8) (2,A) (2,S) (2,W)
(8,10) (8,11) (8,A) (8,B) (8,P) (8,R) (8,S) (8,T)
(8,W) (8,X) (10,11) (10,B) (10,L) (10,P) (10,T) (10,X)
(11,P) (A,B) (A,F) (A,M) (A,N) (A,W) (B,C) (B,F)
(B,X) (C,F) (C,X) (F,M) (F,W) (F,X) (L,T) (L,X)
(M,N) (M,W) (N,W) (P,T) (R,S) (S,W) (T,X) (W,X)
```

Thus `18-48+32=2`. For each oriented face `(i,j,k)`, the H-row is generated deterministically by

```text
n=primitive((Q_j-Q_i)x(Q_k-Q_i)),  h=n·Q_i,
n·x <= h/D-n·C.
```

[Complete H-representation](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_H_representation.json) lists all primitive integer normals, supports, centred rational right sides, and every nonincident slack. Minimum exact integer slack is `1098114392678909749470797`; minimum circumradius-normalized nonincidence separation is `0.0003760223927475944`.

## 4. Exhaustive own-centroid equilibrium audit

Every face uses all oriented in-face projection components; every vertex uses all actual neighbours; every true edge uses all four cone components `(t,1-t,alpha,beta)` from its two incident unit outward normals.

```text
stable faces      [8,A,B], [8,W,S]
unstable vertices 8, X
saddle edges      (2,A), (L,X)
(S,U,H)           (2,2,2)
```

Key normalized margins are

```text
[8,A,B] +0.01338806756869663     U8 +0.9463735044131103
[8,W,S] +0.0029621427805501662  UX +0.15782794093825545
H(2,A)  +0.07601631043838407    H(L,X) +0.021972555411093185
```

The smallest absolute signed mechanical separation, including inactive witnesses, is `0.0017614752984684244`. Every component for all 32 faces, 18 vertices, and 48 true edges is recorded in the [exact report](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_exact_report.json) and [human-readable exhaustive audit](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_audit.md).

## 5. Perturbation, independent verifier, and meshes

Exact outward interval arithmetic allows all 54 uncentred coordinate entries to vary independently by `2^-21`. At every point it recomputes volume, moments, and the dependent own centroid and preserves the complete `(18,48,32)` lattice and strict `(2,2,2)` class. See [perturbation certificate](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_perturbation_certificate.json).

A clean-room SciPy/Qhull implementation with an independent positive-tetrahedron mass integral and separately coded full edge-cone mechanics reproduces all faces, edges, centroid, and equilibria. Maximum discrepancies are `6.94e-17` in volume and `2.78e-16` in a centroid coordinate. Trimesh reads the [OBJ](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_centered.obj) and [STL](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_centered.stl) as watertight, winding-consistent, and Euler two. [Independent report](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_independent_verification.json).

## 6. Four independent controls and exact residual obstruction

Controls `W.z, X.y, 2.x, T.x` target respectively the limiting component of stable `[8,W,S]`, directed instability `X->W`, the limiting cone component of saddle `(2,A)`, and the endpoint component of saddle `(L,X)`. The exact rational Jacobian has rank four and nonzero determinant. Solving `Jv=(-1,-1,-1,-1)` and scaling to maximum displacement `2^-23`, inside the preserving box, strictly decreases all four raw sheets at a finite exact point. Thus lack of local differential rank is not the obstruction. [Four-control certificate](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_four_control_certificate.json).

The actual obstruction is topological-mechanical. Let `K2={W,X}`. On the larger all-coordinate box `2^-15`, the hull remains fixed, every directed component from `W` or `X` to a neighbour outside `K2` is strictly positive, all components at protected `8` are positive, and true edge `(W,X)` has strictly positive squared-length lower bound. Exact minima are

```text
external component lower =
846701675341422630677832707416345427291685114571
/91343852333181432387730302044767688728495783936

U8 component lower =
3487118509382971012809157331982612042866613004823
/1461501637330902918203684832716283019655932542976

|W-X|^2 lower = 85015316504648283/9223372036854775808.
```

For centred positions, if `u(i->j)=-4V6 x_i·(p_j-p_i)<=0`, then

```text
||x_j||^2-||x_i||^2 >= ||p_j-p_i||^2 > 0.
```

If neither `W` nor `X` were unstable, their only nonpositive arrows would have to point toward one another along `(W,X)`, forcing strict squared-radius increase in both directions, impossible. Hence one of `W,X` is unstable throughout the entire certified chamber, including mechanics walls; protected `8` is independently unstable. Therefore `U>=2` throughout. [Exact component theorem](sandbox:/mnt/data/vivid_quartz_58_two_page_result/E18P_component_certificate.json), [independent stdlib replay](sandbox:/mnt/data/vivid_quartz_58_two_page_result/verify_E18P_component_independent.py).

## 7. First topology outside the new theorem

The smallest adjacent simplicial change flips quadrilateral `F-W-8-X`:

```text
remove [X,F,W], [W,8,X], edge (W,X)
add    [F,W,8], [F,8,X], edge (F,8).
```

This graph is geometrically realizable. Exact dyadic endpoint `E18F` has `(18,48,32)`, strict `(8,8,14)`, minimum mechanics separation `0.004408293889573108`, normalized nonincidence `0.02775064519538477`, and box `2^-18`. It breaks the `{W,X}` theorem but greatly enlarges the Morse packet; its full realization space remains open. [Exact `E18F`](sandbox:/mnt/data/vivid_quartz_58_two_page_result/adjacent_E18F/E18F_exact_report.json), [flip certificate](sandbox:/mnt/data/vivid_quartz_58_two_page_result/adjacent_E18F/E18P_to_E18F_flip_certificate.json), [independent replay](sandbox:/mnt/data/vivid_quartz_58_two_page_result/adjacent_E18F/E18F_independent_verification.json).

The first explicit larger fallback inserts a central vertex `Y`, removes `(W,X)`, and replaces the two spine triangles by

```text
[W,F,Y] [F,X,Y] [X,8,Y] [8,W,Y].
```

This is an exactly verified triangulated-sphere architecture with `(19,51,34)`, but no geometric realization or minimality theorem is claimed. [Fallback specification](sandbox:/mnt/data/vivid_quartz_58_two_page_result/next_open_topology.json).

## 8. Exact scope and continuation

**Proved:** exact `E21D` reconstruction; exact two-page disk and positive 3-ball; exact `E18P` V/H/E data and own-centroid moments; exhaustive full-cone classification; `2^-21` class box; independent verifier and meshes; literal removal of all old residual features; rank-four common descent; chamber-wide `U>=2`; exact realization of the first adjacent component-breaking graph.

**Not proved:** the full `E18P` realization space outside the two boxes; the full `E18F` realization space; a continuous source-to-target event with all old deaths ordered before replacement births; nonexistence in the 19-vertex fallback.

The smallest unresolved cell overall is `E18P` outside the certified boxes. The smallest distinct adjacent incidence frontier is the `E18F` graph outside its exact `(8,8,14)` anchor. A successful continuation must preserve `[8,A,B]` and `8`, keep `(W,X)` absent, jointly deactivate the transferred stable and saddle routes, and create a certified nonpositive external arrow from `W` or `X` toward the protected basin before a replacement birth.

## Reusable conclusion

`E18P` is the first exact two-page higher-valence endpoint outside the `E21D` terminal-diamond theorem. It is smaller than its source, fully exact, own-centred, robust, independently reconstructed, and watertight-meshed. It breaks old component `K` and deletes every old residual feature, but transfers the packet. The new exact `{W,X}` component theorem forces `U>=2` throughout its certified chamber. **Explicit disposition: exact materialized NONWINNER.**
