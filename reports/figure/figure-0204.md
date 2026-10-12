# figure-0204

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Quartz 58 — terminal-diamond continuation beyond `E19X`

## Literal disposition

**EXACT MATERIALIZED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The new endpoint `E21D` is an exact dyadic, uniform-density convex polyhedron at its own ordinary-volume centroid with actual `(V,E,F)=(21,57,38)` and strict `(S,U,H)=(2,2,2)`.

This is a genuine advance beyond the preceding `E19X` obstruction: the forcing edge `(12,E)` is deleted, two interacting supports `U,V` are inserted with true edge `(U,V)`, and an exact rank-four chart moves both the new supports and inherited old-plane geometry. A different, larger exact component theorem then forces `U>=2` throughout the certified terminal-diamond chamber.

## Immutable artifacts

- Portable exact archive (`vivid_quartz_58_terminal_diamond_nonwinner.zip`)
- Archive SHA-256 (`vivid_quartz_58_terminal_diamond_nonwinner.zip.sha256`): `6f9d8eb12e4400be4cd3edc37e11e83e1e538cfcc9c92c3c143213cda96266e3`
- Complete determination (`RESULT.md`), README (`README.md`), one-command verifier (`[internal-source-reference].sh`), 63-file manifest (`SHA256SUMS`)
- Exact endpoint report (`E21D_exact_report.json`), complete H representation (`E21D_H_representation.json`), exhaustive audit (`E21D_audit.md`), independent report (`E21D_independent_verification.json`)
- Perturbation certificate (`E21D_perturbation_certificate.json`), four-control certificate (`E21D_four_control_certificate.json`), component theorem (`E21D_component_certificate.json`), independent component verifier (`verify_E21D_component_independent.py`)
- Centred OBJ (`E21D_centered.obj`), centred STL (`E21D_centered.stl`), post-endpoint search receipt (`post_E21D_search_summary.json`)

The clean manifest-bound replay ends with `ALL VIVID QUARTZ 58 TERMINAL-DIAMOND VERIFIERS PASS`; the ZIP passes an independent compressed-data integrity test.

## 1. Exact incidence replacement

In `E19X`, the complete star of true edge `(12,E)` is the two-triangle disk

```text
[12,E,L] [12,M,E]
```

with boundary cycle `E-L-12-M-E`. Replace it by

```text
[E,L,U] [U,L,12] [12,V,U]
[12,M,V] [M,E,V] [E,U,V].
```

The source disk has f-vector `(4,5,2)`, the target disk `(6,11,6)`; each has Euler characteristic one and the same four boundary edges. Globally,

```text
(19,51,34) -> (21,57,38).
```

The old true edge `(12,E)` is absent and `(U,V)` is true. The patch certificate is an exact incidence comparison; no unstated source-to-target coordinate homotopy is claimed.

## 2. Complete V-representation and exact mass identities

Let `D=4503599627370496=2^52`. Before centring, `p_i=Q_i/D` with integer numerators:

```text
1  (-4662244859648,   -5464304475189248,  -3346162897152)
2  (154785842807040,  -3403120362611968,  -316559365142528)
8  (-393579918405120, -11528337076183296, 1364770516206848)
10 (-502071569605888, -8856383403215360,  1747424910280448)
12 (142503996318208,  14381066258599680,  -573845344637184)
11 (-492915428832256, -9864257436494848,  1600396534412544)
A  (551499514983424,  3049847149274112,   -1239107278422016)
B  (141734220332800,  1302277784208128,   66180542907648)
C  (376504764248832,  8295641315284480,   -830315363427840)
E  (4947583341312,    14380757199482624,  -632916240270336)
F  (505239940141056,  5996248775836160,   -1067179017724160)
L  (-314728119237632, 1082220216558336,   772761696218880)
M  (482105340265984,  5735851528281344,   -1131320804626944)
N  (500459801806336,  3199825623630336,   -1269975841739776)
P  (-551394653864192, -9361780687868160,  1638198585660928)
Q  (38183107019776,   5597318741813760,   -923307733349120)
R  (-80491997774336,  -5744421501184256,  71754109186048)
S  (69513356547584,   -326221904271360,   -931949538883328)
T  (-627633535233792, -8472227745949952,  1658335796246528)
U  (73104749399333,   14382266609182334,  -601939485368515)
V  (74164538542304,   14381954768263286,  -604466146574404)
```

The physical body is `conv{Q_i/D-C}`. Its exact ordinary volume is

```text
2821892852992141838960138385691401389629871
------------------------------------------------
33451117797795934712303577408972542258970624.
```

Exact uncentred first moments are

```text
Mx = -194670459455364211790353624330537985906607108029730462941
     /602601766597121353328235784627935975945826122668547313238016
My = 3811952059583332635472885289451127827064775235637462563167
     /150650441649280338332058946156983993986456530667136828309504
Mz = -687598900506809639362785039415300265371138868873112469009
     /602601766597121353328235784627935975945826122668547313238016.
```

The exact ordinary-volume centroid is

```text
Cx = -194670459455364211790353624330537985906607108029730462941
     /50834702404859503337336599537742211467157960611641702744064
Cy = 3811952059583332635472885289451127827064775235637462563167
     /12708675601214875834334149884435552866789490152910425686016
Cz = -6807909906008016231314703360547527379912266028446658109
     /503313885196628745914223757799427836308494659521204977664.
```

Numerically, `C≈(-0.0038294796712875973,0.29994880498947757,-0.01352617145332357)` and `V≈0.084358701256257385`. The exact verifier proves `M_j=V C_j` for all three coordinates, so translating by `C` gives first moments exactly `(0,0,0)`.

## 3. Actual maximal faces and true edges

All 38 irredundant maximal faces are triangular:

```text
[1,2,8] [1,S,2] [1,8,R] [1,R,S] [2,A,8] [2,S,A]
[8,10,11] [8,B,10] [8,11,P] [8,A,B] [8,P,T] [8,S,R]
[8,T,S] [10,B,12] [10,12,L] [10,P,11] [10,L,T] [10,T,P]
[12,B,C] [12,C,F] [12,F,M] [12,U,L] [12,M,V] [12,V,U]
[A,F,B] [A,M,F] [A,N,M] [A,S,N] [B,F,C] [E,T,L]
[E,L,U] [E,M,N] [E,V,M] [E,N,Q] [E,Q,T] [E,U,V]
[N,S,Q] [Q,S,T]
```

All 57 true edges are

```text
(1,2) (1,8) (1,R) (1,S) (2,8) (2,A) (2,S)
(8,10) (8,11) (8,A) (8,B) (8,P) (8,R) (8,S) (8,T)
(10,12) (10,11) (10,B) (10,L) (10,P) (10,T)
(12,B) (12,C) (12,F) (12,L) (12,M) (12,U) (12,V)
(11,P) (A,B) (A,F) (A,M) (A,N) (A,S) (B,C) (B,F) (C,F)
(E,L) (E,M) (E,N) (E,Q) (E,T) (E,U) (E,V)
(F,M) (L,T) (L,U) (M,N) (M,V) (N,Q) (N,S)
(P,T) (Q,S) (Q,T) (R,S) (S,T) (U,V)
```

Euler check: `21-57+38=2`.

For every oriented face `(i,j,k)`, the exact H-generator uses

```text
n = primitive((Q_j-Q_i) × (Q_k-Q_i)),
h = n·Q_i,
n·x <= h/D - n·C.
```

All 38 primitive integer normals, supports, centred rational right-hand sides, and every nonincident slack are in the linked H-representation. Every row is irredundant. The minimum exact integer nonincidence slack is

```text
7118081121879499786521485030315142912.
```

The minimum Euclidean nonincidence separation is `0.001247397740444841`, or `0.00017915854039296468` after circumradius normalization.

## 4. Exhaustive own-centroid mechanics

Every face is tested with all oriented in-face projection components; every vertex against every actual neighbour; every true edge with all four components `(t,1-t,alpha,beta)` of the cone generated by its two incident unit outward normals.

```text
stable maximal faces = [8,A,B], [E,Q,T]
unstable vertices    = 8, U
saddle true edges    = (12,L), (A,S)
strict class         = (2,2,2).
```

The smallest absolute normalized mechanical separation is `0.0017286567852296394`; the limiting inactive feature is face `[10,L,T]`. Protected stable face `[8,A,B]` has limiting component `+0.0024103268436112997`, and vertex `8` remains strictly unstable. The linked audit prints every component for all 38 faces, 21 vertices, and 57 true edges; the exact report stores every sign numerator.

## 5. Perturbation and independent reconstruction

Exact outward interval arithmetic permits every one of the 63 uncentred coordinate entries to vary independently by

```text
epsilon = 2^-22 = 1/4194304.
```

Throughout that box the verifier rebuilds the same `(21,57,38)` hull, recomputes volume and all three first moments, substitutes the dependent own centroid, and preserves strict `(2,2,2)`. The volume enclosure is

```text
[2821774519719461079400849387492813502964143/33451117797795934712303577408972542258970624,
 2822011186279334274073750036015702590120367/33451117797795934712303577408972542258970624].
```

A clean-room SciPy/Qhull implementation, importing neither the Fraction verifier nor its incidence maps, independently obtains `(21,57,38)`, `(2,2,2)`, volume `0.084358701256257412`, the same centroid and equilibrium labels, maximum volume discrepancy `2.78e-17`, and maximum centroid-coordinate discrepancy `5.55e-17`. Trimesh reads both supplied meshes as watertight and winding-consistent, with Euler number two and centre of mass at floating roundoff.

## 6. Genuine exact rank-four control cell

The four independent direct controls are

```text
c1=U.x, c2=V.z, c3=E.z, c4=Q.y.
```

They target, respectively through the full Jacobian, the limiting component of stable `[E,Q,T]`, directed instability `U->E`, the active cone component of saddle `(12,L)`, and the active cone component of saddle `(A,S)`. Exact forward differentiation gives a nonzero 474-digit rational determinant and rank four. The certificate stores an exact vector `v` with

```text
Jv=(-1,-1,-1,-1)
```

and a finite exact step whose largest coordinate displacement is `2^-24`, inside the `2^-22` class-preserving box; all four raw residual sheets strictly decrease. Thus lack of local control rank is not the obstruction.

## 7. Rigorous chamber-wide forcing theorem

Let

```text
K={E,U,V,12}.
```

Its internal true edges are

```text
(12,U) (12,V) (E,U) (E,V) (U,V).
```

On the larger all-coordinate box `|delta q|<=2^-19`, exact interval support signs preserve the full hull. All 13 directed instability components from a vertex of `K` to a neighbour outside `K` are strictly positive, all 10 directed components at protected vertex `8` are strictly positive, and every internal edge has a positive squared-length lower bound.

For centred positions `x_i`, `d=p_j-p_i`, and positive volume numerator `V6`, define

```text
u(i->j)=-4 V6 x_i·d.
```

If `u(i->j)<=0`, then

```text
||x_j||^2-||x_i||^2
 = 2 x_i·d + ||d||^2
 >= ||d||^2 > 0.
```

Suppose no vertex of `K` were unstable. Each would then have a nonpositive directed component. Because every external component is certified positive, each vertex must choose an internal neighbour of strictly larger squared radius. A functional digraph on finite `K` contains a directed cycle, contradicting strict radius increase. Therefore at least one of `E,U,V,12` is unstable at every point of the complete `2^-19` box. Vertex `8` is independently unstable there. Hence

```text
U>=2 throughout the entire certified terminal-diamond chamber,
including every internal mechanical wall.
```

An independent stdlib-only interval implementation reconstructs and replays this proof and ends with `INDEPENDENT_E21D_COMPONENT_FORCING_PASS`.

## 8. Attempts to break the conclusion

The exact negative claim is kept local. Further searches were used only as discovery evidence:

- A topology-aware rechart reached score `-0.00044119050998605273`, but support collapsed to `1.2874e-8`; the actual body remained `(2,2,2)`.
- Six independent 40,000-proposal W-X bridge searches, 240,000 proposals total, found no winner; best score `-0.010228100857091497`.
- Four cap-beam runs attempted 86,880 successive topology-changing additions through ten levels and retained 51,227 all-active bodies. No winner occurred; best score `-0.0009218828949442649`, class `(2,3,3)`, support about `1.32e-6`.
- Two BFS rechart searches reached `-8.2479e-7` and `-7.3944e-7`, but both were `(2,3,3)` with support only `1.11e-8` and `2.40e-8`, so they are wall receipts rather than exactification candidates.
- Eight bounded attempts to delete `N,Q` and realize a shared-edge `W,X` terminal disk never matched the requested sphere; best symmetric face difference was ten. This is not a nonrealizability theorem.

No searched JSON state had class `(1,1,0)`.

## 9. Exact scope and next minimum topology

Proved:

1. Exact `E19X -> E21D` connected disk replacement deleting `(12,E)` and inserting finite-thickness shared edge `(U,V)`.
2. Complete exact V/H/E data, exact ordinary-volume centroid and moments, exhaustive full-cone mechanics, strict incidence and perturbation margins, independent reconstruction, and matching meshes.
3. Exact rank-four old/new-geometry control chart and a finite simultaneous descent step.
4. Exact `2^-19` component theorem forcing `U>=2` throughout the complete certified chamber.

Not proved:

- No global exclusion of all 21-vertex bodies or all realizations of this graph.
- The incidence patch is not claimed as a continuous coordinate homotopy from the numeric `E19X` endpoint.
- Numerical search failures are not nonexistence proofs.

The next construction must invalidate the component theorem itself. It must, in one shared event, make at least one of `E,U,V,12` non-extreme, remove enough internal component edges to prevent the finite-chain closure, or create an external edge from the component to a strictly larger-radius relay leading to protected `8` with a nonpositive directed component. Simultaneously it must eliminate stable `[E,Q,T]` and saddle channels `(12,L),(A,S)` before replacement births.

The smallest explicit carrier supported by the exact incidence is a two-page higher-valence disk spanning boundary routes

```text
U-L-T-8
E-N-S-A
```

with one shared terminal edge and coordinated old-plane motion. One page must break the `{E,U,V,12}` radial component; the other must replace both saddle stars. Another serial subdivision inside the current component is rigorously redundant throughout the certified chamber.

## Reusable conclusion

`E21D` is the first exact object in this branch to remove the old chamber-forcing edge `(12,E)` through a genuine two-support terminal diamond. It is robust, exactly own-centred, completely audited, independently reconstructed, and meshed, but it remains strict `(2,2,2)`. Four independent controls decrease all inherited residual sheets, yet the larger exact component theorem forces another unstable vertex in addition to protected `8`. **Explicit disposition: exact materialized NONWINNER.**
