# figure-0183

AI research report · 2026-09-01 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Harbor 62 — exact shared-cell continuation from J45

## Literal disposition: **EXACT NONWINNER**

No homogeneous convex polyhedral Gömböc was obtained. The required gate remains a finite uniform-density convex polyhedron, evaluated at its own ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge incidence, positive exhaustive margins, independent verification, and matching meshes.

The direction nevertheless advances materially beyond `J45_two_sheet_terminal13`. I constructed and exactified a literal three-dimensional shared cell containing two edge-sharing circuit sheets and a transverse return circuit, enumerated every adjacent orthant, reconstructed an exact 52-event ingress/egress incidence atlas, and materialized the strongest post-cell body:

```text
J46_double_circuit_cell9
supplied H rows = 4324
active H rows   = 9
(V,E,F)         = (14,21,9)
complexity      = 42
strict class    = (2,2,2).
```

Both old forcing edges, both old unstable facets, and both old saddle labels are destroyed. A new open Euler-neutral packet is born, and a new row-disjoint forcing matching proves `S>=2` throughout the endpoint root box. Thus the proposed shared-cell architecture leaves both old forcing-edge sign chambers but still transfers rather than cancels the last packet.

## 1. Deterministic exact source

Let

```text
P(Q)={x in R^3 : q_i·x <= 1, i=0,...,4323}.
```

The source is reconstructed deterministically from the canonical exact-dyadic J45 family and the recorded optimized support vectors:

1. Start with all 4,324 supplied J45 polar rows.
2. Replace the rows with labels

```text
0,1160,2453,2463,2475,2481,2490,4137,4229
```

by the corresponding optimized vectors in `jax_fixed_seed2_m0.9.json`, divided by `8` and rounded exactly to denominator `2^32`.
3. Scale every other predecessor row by the exact factor `2^-20`.
4. Compute the exact rational volume `V_raw` and first moment `M_raw` of the resulting bounded raw polyhedron, set

```text
c=M_raw/V_raw,
```

and projectively translate every row by

```text
q_i -> q_i/(1-q_i·c).
```

This last operation represents exactly the translated body `P_raw-c`; it is not an approximate recentering. All denominators are positive and are certified away from zero.

Reconstruction inputs:

- Accepted exact J44/J45 predecessor archive (`Steady_Harbor_62_J44_J45_exact_NONWINNER.zip`)
- Recorded optimized support vectors (`jax_fixed_seed2_m0.9.json`)
- Exact arithmetic polyhedron engine (`exact_poly.py`)
- Directed interval engine (`int_poly.py`)
- Package construction source (`build_final_package.py`)
- Package completion source (`complete_package.py`)

The generated package root is

```text
/mnt/data/sh62_j46/package/
  Steady_Harbor_62_J46_double_circuit_exact_NONWINNER/
```

and contains 144 files, including all 4,324 exact centred H rows, the filtered active H table, exact Cramer vertices, maximal-face cycles, true edges, oriented surface triangles, mechanics ledgers, wall and atlas certificates, OBJ, STL, source recipes, and verifier.

## 2. Exact ordinary-volume centring

The three dependent controls are the coordinates `u=(u_x,u_y,u_z)` of the projective translation family

```text
q_i(u)=q_i/(1-q_i·u),
P_u=P_raw-u.
```

Translation gives the exact identities

```text
V(u)=V_raw,
M(u)=M_raw-V_raw u.
```

Consequently the unique solution of all three ordinary first-moment equations is

```text
u*=M_raw/V_raw,
M(u*)=(0,0,0),
D_u M=-V_raw I_3,
det(D_u M)=-V_raw^3 != 0.
```

This is stronger than a local floating-point solve: the dependent root is exact rational and globally unique wherever the projective denominators remain positive. The exact rational volume is stored as numerator and denominator in `certificates/J46_exact_centering.json`; its decimal readback is

```text
V = 2.333872329058951... .
```

The endpoint therefore has uniform-volume centroid exactly at the origin.

## 3. Literal shared three-dimensional double-circuit wall

Use the local-to-global row map

```text
local:  0,   1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12
global: 0,1160,2453,2463,2467,2468,2475,2481,2490,2505,4101,4137,4229.
```

The exact common wall has active local rows

```text
0,1,2,3,5,6,7,8,9,12
```

and three simultaneous affine circuits.

### Circuit A — first forcing sheet

```text
global rows: (0,2463,2475,2481)
coefficients: (3403/4096, 973/2048, -1253/4096, -1)
```

Its two diagonals are the old forcing edge `(2475,2481)` and the replacement edge `(0,2463)`.

### Circuit B — second forcing sheet

```text
global rows: (2453,2463,2481,2490)
coefficients: (-1, 2839/2048, -4955/4096, 3373/4096)
```

Its two diagonals are the old forcing edge `(2463,2490)` and the replacement edge `(2453,2481)`.

Circuits A and B share the edge carrier `(2463,2481)`, so this is not a pair of disjoint serial flips.

### Circuit C — transverse return tetrahedron

```text
global rows: (0,2468,2505,4229)
coefficients: (1/2, -1, -1/10, 3/5)
```

Its two diagonals are the old saddle edge `(2468,2505)` and the return edge `(0,4229)`. It is transverse to the two forcing sheets and couples the replacement to the required rows `0` and `4229`.

All three affine determinants vanish exactly. Independent signed controls move rows `2475`, `2453`, and `2468` by `2^-18` times their exact circuit-normal directions. The central wall has

```text
(H,V,E)=(10,13,21)
```

and three nonsimplicial quadrilateral maximal faces. Each of the eight exact sign orthants has

```text
(H,V,E)=(10,16,24),
strict class=(2,5,5),
```

with a distinct topology signature. Thus no adjacent orthant is a hidden `(1,1,0)` chamber.

The edge states in orthant-bit order `0,...,7` are:

```text
bits  old A  old B  new (2453,2481)  return (0,4229)  old saddle C
0       yes    no          no                no              yes
1       yes    yes         no                no              yes
2       no     no          yes               no              yes
3       no     yes         yes               no              yes
4       yes    no          no                yes             no
5       yes    yes         no                yes             no
6       no     no          yes               yes             no
7       no     yes         yes               yes             no.
```

Orthant `1` is the certified ingress side carrying both old forcing edges; orthant `6` is the certified egress side carrying neither old forcing edge and carrying the return edge.

This is the requested literal shared three-dimensional topology. What fails is the intended Morse ordering: the old packet does not disappear into an open `(1,1,0)` cell before replacement features are born. Every exact adjacent orthant contains at least two stable features and five saddles.

## 4. Complete exact transition atlas

The transition from the exact rational J45 anchor into the common wall and onward to J46 was reconstructed across every generic incidence event:

```text
ingress generic events = 36
 ingress open cells     = 37
central simultaneous event = one exact rank-three wall
 central orthants       = 8
egress generic events  = 16
 egress open cells      = 17
--------------------------------
total generic events   = 52
total path open cells  = 54.
```

For every generic event the atlas records:

- the exact rational segment endpoints;
- the primitive owner circuit;
- its exact sign-changing univariate rational polynomial;
- a rational isolating bracket;
- exact endpoint signs;
- exact Sturm root count `1` inside the bracket;
- the centred active H representation on both sides;
- exact Cramer vertices;
- maximal faces and every true edge;
- volume and zero first moments;
- complete directed all-feature mechanics.

The 54 open-cell class histogram is

```text
(2,2,2): 21
(2,3,3): 11
(2,4,4):  8
(2,5,5):  5
(2,6,6):  3
(3,2,3):  5
(3,4,5):  1.
```

No open cell has `S=1`, `U=1`, or `H=0` simultaneously. The first ingress signature agrees with the exact J45 anchor after global/local relabelling, the final ingress signature agrees with common-wall orthant `1`, the initial egress signature agrees with orthant `6`, and the final egress signature agrees with J46.

- Complete compressed exact transition atlas (`path_atlas_exact_start.json.gz`)
- Deterministic exact atlas builder (`path_atlas_exact_start.py`)

This atlas is an exact incidence chronology. Its mechanical labels are audited at every open representative; it is not asserted that every possible mechanics-zero time between incidence events has been algebraically isolated.

## 5. Exact endpoint incidence

### Active H rows

```text
0, 1160, 2453, 2463, 2475, 2481, 2490, 4137, 4229.
```

The other 4,315 supplied rows are strictly inactive.

### Exact vertices

Number the 14 actual vertices by their incident active-H triples:

```text
v0  = (0,1160,2475)
v1  = (0,1160,4229)
v2  = (0,2463,2475)
v3  = (0,2463,2481)
v4  = (0,2481,4229)
v5  = (1160,2475,4137)
v6  = (1160,2490,4137)
v7  = (1160,2490,4229)
v8  = (2453,2481,2490)
v9  = (2453,2481,4137)
v10 = (2453,2490,4137)
v11 = (2463,2475,4137)
v12 = (2463,2481,4137)
v13 = (2481,2490,4229).
```

Their full exact rational Cramer coordinates are materialized in `cells/J46_double_circuit_cell9/V_exact.tsv.gz`.

### Maximal-face cycles

One valid cyclic orientation is

```text
H0:    0,1,4,3,2
H1160: 0,1,7,6,5
H2453: 8,9,10
H2463: 2,3,12,11
H2475: 0,2,11,5
H2481: 3,4,13,8,9,12
H2490: 6,7,13,8,10
H4137: 5,6,10,9,12,11
H4229: 1,4,13,7.
```

The cycle lengths sum to `42=2E`, and `V-E+F=14-21+9=2`.

### Every true edge

In the form `(endpoint vertices ; incident H rows)`:

```text
(0,1;0,1160)
(2,3;0,2463)
(0,2;0,2475)
(3,4;0,2481)
(1,4;0,4229)
(0,5;1160,2475)
(6,7;1160,2490)
(5,6;1160,4137)
(1,7;1160,4229)
(8,9;2453,2481)
(8,10;2453,2490)
(9,10;2453,4137)
(2,11;2463,2475)
(3,12;2463,2481)
(11,12;2463,4137)
(5,11;2475,4137)
(8,13;2481,2490)
(9,12;2481,4137)
(4,13;2481,4229)
(6,10;2490,4137)
(7,13;2490,4229).
```

These are actual polyhedral edges derived from maximal-face intersections. Surface-triangulation diagonals are not included.

## 6. Exhaustive endpoint mechanics

The complete equilibrium set at the exact ordinary centroid is

```text
stable maximal faces:
  1160
  2475

unstable vertices, by incident H triples:
  (1160,2475,4137)
  (2453,2481,4137)

saddle true edges:
  (0,4229)
  (2475,4137).
```

Both old J45 forcing edges are absent:

```text
(2463,2490) absent
(2475,2481) absent.
```

Both old J45 unstable facets are absent:

```text
(0,2453,2481) absent
(2475,2505,4229) absent.
```

For the old saddles, `(2468,2505)` is absent because both rows are inactive, while `(2453,2481)` survives as a true edge but is strictly nonsaddle.

The directed endpoint margins are approximately

| primitive decision | certified margin |
|---|---:|
| included stable minimum | `+1.911228e-3` |
| closest excluded face | `-1.2108e-3` |
| included unstable minimum | `+5.12129793e-2` |
| closest excluded vertex | `-6.3902107e-3` |
| included saddle minimum | `+2.46711454e-2` |
| closest excluded true edge | `-1.46502906e-3` |

All 4,324 supplied rows are checked against every nonincident actual vertex. The minimum directed nonincidence gap is approximately

```text
0.116255...
```

and every inactive row is separated strictly from the endpoint hull. Every one of the 21 true edges is checked through all four normal-cone components: both endpoint projection parameters and both incident-normal coefficients.

## 7. Positive perturbation box

After exact projective centring, five independent trace-free symmetric metric controls are used:

```text
B0 = [[1,0,0],[0,0,0],[0,0,-1]]
B1 = [[0,1,0],[1,0,0],[0,0,0]]
B2 = [[0,0,1],[0,0,0],[1,0,0]]
B3 = [[0,0,0],[0,1,0],[0,0,-1]]
B4 = [[0,0,0],[0,0,1],[0,1,0]].
```

For

```text
A(s)=I+sum(s_k B_k),  |s_k|<=2^-16,
```

these controls have rank five, preserve the zero ordinary centroid identically, and satisfy

```text
minimum singular value >= 0.9999237060546875
det A in [0.9999389653093876,1.0000610370189282].
```

Across the entire box:

```text
minimum incidence lower bound       = 0.11238574133098998
included stable lower bound          = +0.001501917845587841
closest excluded face upper bound    = -0.0008007500788118626
included unstable lower bound        = +0.05084407493347963
closest excluded vertex upper bound  = -0.000995350257506406
included saddle lower bound          = +0.024183750031508962
closest excluded edge upper bound    = -0.0006238907584044705.
```

Hence J46 is an open robust `(2,2,2)` nonwinner, not a wall point.

## 8. Exact residual forcing obstruction

The endpoint contains the row-disjoint actual true edges

```text
(2463,2475)
(1160,2490).
```

For each edge, the exact certificate enumerates every external true neighbour of both endpoints and proves that its stability numerator is positive. The global minimum external-numerator lower bound is

```text
141.40650634057403,
```

and the global minimum squared cross-normal separation is

```text
685.9832358163093.
```

If both endpoints of either edge were nonstable, after all external alternatives have been excluded, the two remaining mutual failures would add to

```text
-||q_a-q_b||^2 >= 0,
```

contradicting the strict positive squared separation. Therefore each edge has at least one stable endpoint. Because the two edges are row-disjoint,

```text
S>=2
```

throughout the exact root and perturbation box. The exhaustive audit attains equality. This is the first residual obstruction and establishes the exact NONWINNER disposition independently of the numerical search history.

## 9. Residual topology and continuation threshold

All six nonprotected J45 equilibrium labels have been replaced, but the new residual is again one connected Morse component:

```text
stable terminals:   1160,2475
unstable terminals: (1160,2475,4137), (2453,2481,4137)
saddles:            (0,4229), (2475,4137)
carrier rows:        0,1160,2453,2463,2475,2481,2490,4137,4229.
```

The smallest evidence-supported successor is not another diagonal flip or serial support transfer. It is a nonannular **double-return three-dimensional shared cell** over these nine rows. It must simultaneously:

1. destroy both new forcing edges `(2463,2475)` and `(1160,2490)`;
2. span both new saddle stars and both unstable facets;
3. include two independent cancellation circuits;
4. include an independent return/antibirth relay through the `0–4229` side;
5. retain three dependent controls for the ordinary moments;
6. reach one open cell in which both forcing edges and both saddles are absent before any replacement S–H or U–H pair is born.

This is not claimed as a global row-minimality theorem. It is the smallest topology forced by the exact endpoint obstruction and the complete local atlas.

## 10. Independent reconstruction and mesh audit

The standalone verifier performs independent endpoint, J45-anchor, common-wall, orthant, transition-atlas, and mesh checks. Its completed transcript ends with

```text
STEADY_HARBOR62_J46_DOUBLE_CIRCUIT_EXACT_NONWINNER_ALL_CHECKS_PASS
```

and independently reproduces:

```text
endpoint class        (2,2,2)
endpoint (H,V,E)      (9,14,21)
wall (H,V,E)          (10,13,21)
each orthant (H,V,E)  (10,16,24)
orthant classes       eight copies of (2,5,5)
atlas generic events  52
atlas open cells      54
watertight mesh        yes
Euler characteristic   2.
```

- Independent verifier (`verify_steady_harbor62_J46.py`)
- Completed independent-verification transcript (`verify_stage2.log`)
- Package-generation transcript (`complete_package.log`)

### Artifact integrity limitation

The mathematical package and all endpoint/atlas/mesh files were generated, and the independent verifier passed from that package root. The runtime ended before the 144-file directory could be sealed into a final immutable ZIP and before a clean-extraction manifest receipt could be produced. Therefore no ZIP SHA-256 is claimed here. This is an artifact-transport incompleteness, not an unresolved endpoint classification: J46 itself, its exact centring, complete incidence, mechanics, shared wall, atlas, forcing theorem, and watertight mesh were all constructed and independently checked.

## Final boundary

```text
J46_double_circuit_cell9
(V,E,F)=(14,21,9)
ordinary centroid=(0,0,0) exactly
strict (S,U,H)=(2,2,2)
EXACT NONWINNER.
```

The requested J45 double-circuit/return topology has now been realized literally and exhaustively crossed. It destroys the complete old labelled residual packet but transfers it to a new robust packet forced by true edges `(2463,2475)` and `(1160,2490)`. Continue only with the nine-row nonannular double-return cell; remaining inside the J46 incidence/external-sign box is rigorously excluded by `S>=2`.
