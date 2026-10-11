# figure-0214

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Keen Quartz 89 — exact M42 acute-bridge fifth-cell handoff

## Disposition

**NONWINNER. No strict own-centred homogeneous convex polyhedron with `(S,U,H)=(1,1,0)` was obtained.** I therefore make no Gömböc claim.

I recovered and independently reconstructed the accepted exact M42 fifth-cell benchmark, explored several genuine full-hull replacements of its residual stable–saddle component, and localized the next nonrepeating topology more sharply. The strongest new constructions are double-precision discovery objects rather than exact or interval-certified endpoints, so they do **not** satisfy the assignment’s acceptance gate. The strongest accepted exact body remains the rational fifth-cell benchmark `(V,E,F)=(61,163,104)`, strict `(2,1,1)`; the strongest recovered exact topology-changing successor remains the independently verified six-flip local-octahedral branch, but its far cell is `(2,2,2)`, not a Gömböc. The journal likewise records that the benchmark remains the closest accepted body and that no higher-valence branch had yet won. :contentReference[oaicite:0]{index=0}

## Exact material recovered and checked

The complete M42 bundle was recovered from the user’s Library and unpacked. It contains exact rational V-data, centred H-data, maximal-face cycles, true edges, exact volume and first-moment calculations, exhaustive face/vertex/edge mechanics, perturbation certificates, independent clean-room verification, and matching OBJ/STL meshes. The benchmark has:

- `(V,E,F)=(61,163,104)`;
- stable maximal faces `[0,1,...,16]` and `[198,224,258]`;
- unique unstable vertex `8`;
- sole saddle true edge `(229,247)`;
- strict margins approximately `0.8846185088` on the intended base, `0.6819299931` on the extra stable face, `0.1716177490` at `U8`, and `0.4958836882` on the saddle;
- minimum nonincidence/topology separation approximately `3.8691692825e-6` in the numerical replay;
- a certified nonzero rational perturbation neighbourhood in the supplied exact certificate.

This is the assignment’s independently accepted starting point and not a new result. The journal identifies the six-row residual octahedral star and the requirement that the stable and saddle death sheets meet inside one shared three-dimensional cell rather than through serial flips. :contentReference[oaicite:1]{index=1}

Exact benchmark archive: [M42 acute-bridge fifth-cell complete bundle](sandbox:/mnt/data/m42_recovered/M42_acute_bridge_fifth_cell_complete%281%29.zip)

The recovered exact six-flip local-octahedral successor can be audited through its frozen certificate and independent verifier:

- [Exact six-flip certificate](sandbox:/mnt/data/m42_recovered/checkpoint/pro-research-native-transfer-20260831/tracks/local_oct_cell_search/clean_flip_topology_escape/certificate.json)
- [Independent six-flip verifier](sandbox:/mnt/data/m42_recovered/checkpoint/pro-research-native-transfer-20260831/tracks/local_oct_cell_search/clean_flip_topology_escape/verify_certificate.py)

That passage changes actual boundary incidence in six exact support flips and reaches a strict far cell with residual packet `S[198,243,245]`, `U1`, `H(4,5)`, and `H(12,13)`. It is rigorous reusable material, but it increases the defect to `(2,2,2)` and therefore is not preferable to the fifth-cell benchmark as an equilibrium result.

## New full-hull work

### 1. Two-plane finite-thickness clipping replacement

I intersected the exact benchmark geometry numerically with two independently oriented clipping halfspaces. The first removes old extreme vertex `224`, and the second removes old extreme vertex `229`. Consequently:

- the old stable triangle `[198,224,258]` is absent;
- the old saddle edge `(229,247)` is absent because vertex `229` itself is absent;
- the operation changes the actual full hull rather than merely changing equilibrium signs on the inherited lattice.

The best structurally separated two-plane sample has:

```text
(V,E,F) = (89,193,106)
(S,U,H) = (2,1,1)
intended base margin = 0.8861337836109797
U8 margin            = 0.17161829414386176
extra stable          = [198,1000,1025,258]
extra stable margin   = 0.00907608629477301
sole saddle           = (1028,1029)
saddle margin         = 0.0031243018162241194
minimum replayed topology margin = 3.869169282480489e-6
```

The replacement therefore performs the requested old-feature deletion but relays the Euler-neutral packet to a new stable quadrilateral and a new cap edge. The two clipping planes, in the numerical normalization used by the search, are approximately:

```text
n1 = ( 0.012573828372327971,
       0.026234764257716533,
      -0.9995767284127844 )
d1 = 0.46356895997831116

n2 = ( 0.39096084192899627,
      -0.9203468864861833,
      -0.010546497682109366 )
d2 = 28.608418274611044
```

Reproducible discovery data:

- [Two-plane search ledger](sandbox:/mnt/data/m42_slot7/opt_two_plane/result.json)
- [Two-plane best structural sample](sandbox:/mnt/data/m42_slot7/opt_two_plane/best_001.npz)
- [Two-plane construction and search code](sandbox:/mnt/data/m42_slot7/opt_two_plane.py)

These coordinates are floating-point discovery data only. I did not promote them to an exact endpoint because they are a strict nonwinner and exactifying them would not advance the accepted equilibrium frontier.

### 2. Two linked exterior supports on the clipped body

I next added two independently controlled extreme points to the two-plane body: one at the replacement stable star and one at the replacement saddle star. This creates two additional actual full-hull insertions and permits the two residual margins to be reduced independently.

The strongest balanced sample obtained has:

```text
(V,E,F) = (91,203,114)
(S,U,H) = (2,1,1)
intended base margin = 0.8861311762692193
U8 margin            = 0.17161831472823919

q3000 = (-0.8969999677401457,
          2.3980480578152905,
         -0.41209751482101453)
q3001 = (11.280923517580213,
        -26.285677727220957,
         -0.5794569231467949)

extra stable        = [1000,1025,3000]
extra stable margin = 2.9098653144253046e-5
sole saddle         = (1027,3001)
saddle margin       = 5.93987471931734e-4
closest extra-U margin = -9.370131757518324e-5
minimum topology margin = 1.3822279304465113e-7
```

This reduces the stable defect by more than two orders of magnitude relative to the two-plane sample while retaining a reasonably separated saddle-side star. A different sample drives the saddle down to `9.594769366461087e-6`, but its stable relay remains `0.0027594069116610134`; thus the two deaths can be approached separately but were not made simultaneous.

Around the balanced sample, the complete near-zero stable fan is:

```text
[1000,1025,3000]  +2.9098653144253046e-5
[198,3000,258]    -1.8110143961068140e-5
[258,3000,1025]   -2.5021511181470227e-5
[198,1000,3000]   -2.5065193861952510e-5
```

The near-zero saddle fan is:

```text
(1027,3001)  +5.939874719317340e-4
(1028,3001)  -1.3342352902685484e-3
(1029,3001)  -2.5205472309160174e-3
(1026,1028)  -3.0259573201771920e-3
```

This is direct evidence for two local relay mechanisms: pushing the positive stable triangle through zero promotes one of the three adjacent triangles, while pushing the positive saddle through zero moves the carrier among adjacent cap edges. It is not evidence of impossibility in a larger topology.

Reproducible discovery artifacts:

- [Two-support search implementation](sandbox:/mnt/data/m42_slot7/add_two_point_on_twoplane.py)
- [Two-support search ledger](sandbox:/mnt/data/m42_slot7/add_two_point_on_twoplane/result.json)
- [Best balanced two-support sample](sandbox:/mnt/data/m42_slot7/add_two_point_on_twoplane/best_000.npz)

### 3. Connected radial-arc support chains

I tested chains of three through eight exterior points along the spherical/radial arc joining the stable-foot and saddle-foot directions. Four hundred fresh full-hull samples produced no `(1,1,0)` body. The dominant classes were `(2,2,2)` and `(2,1,1)`; smaller populations of `(3,1,2)`, `(3,2,3)`, and higher-defect classes occurred.

The arc points commonly retopologized and reduced the stable star, reaching extra-stable margins as low as roughly `3.8e-5`, but the saddle `(1028,1029)` remained near `0.0031243`. Most intermediate points were swallowed by the hull; only two to four became extreme. This falsifies the simplest thin one-spine bridge, but not a finite-thickness two-page or prismatic bridge.

- [Arc-chain search implementation](sandbox:/mnt/data/m42_slot7/add_arc_chain_search.py)
- [Arc-chain search ledger](sandbox:/mnt/data/m42_slot7/add_arc_chain_search/result.json)

### 4. Additional cutting-plane tests

A third independently oriented clipping plane was tested both systematically and randomly on the two-plane body. No strict target appeared. A plane capable of separating the stable star, saddle star, and their connector from the protected base and `U8` necessarily removed a very large cap—typically dozens of inherited vertices—and generated multiple unstable/saddle births. The observed valid classes were chiefly `(2,3,3)` and `(2,4,4)`.

This is stronger than the previous generic statement that serial cuts transfer the packet: **one additional halfspace cannot localize the required connected surgery on the current two-plane hull.** A useful cutting construction needs several adjacent pages whose union is one finite-thickness boundary component.

Relevant scripts and ledgers are retained under:

```text
/mnt/data/m42_slot7/third_common_scan.py
/mnt/data/m42_slot7/third_common_scan/result.json
/mnt/data/m42_slot7/third_random_clip.py
/mnt/data/m42_slot7/third_random_clip/result.json
/mnt/data/m42_slot7/scan_connected_cap.py
```

### 5. Local linear and trust-region attack

I linearized the full near-zero face, vertex, and edge decision set with respect to the six coordinates of the two added supports. Small trust-region steps reduce one named primitive but immediately encounter the adjacent relay sheets. Larger steps produce `(3,1,2)` or `(2,2,2)` before a common negative chamber is reached. In particular, one linearized step reduced the named saddle prediction but created an extra unstable point and two saddle carriers; another crossed the stable fan and generated a stable–saddle pair on edge `(1000,3000)`.

This six-coordinate chart is therefore not the missing higher-valence cell. The calculation is reproducible with [the local decision-Jacobian and LP script](sandbox:/mnt/data/m42_slot7/local_linear_step.py).

## Observation, inference, and limitation

### Direct observations

1. Actual removal of old vertices `224` and `229` deletes both assignment-named defects but creates a new stable–saddle packet.
2. Independent exterior controls can make either replacement margin very small while leaving the intended base and `U8` strong.
3. The stable and saddle carrier fans remain separated in the true-edge graph of the clipped body.
4. A one-plane connected cut is necessarily global and births several equilibria.
5. A thin radial chain is mostly nonextreme and does not affect both stars.

### Inference

The smallest still credible operation is not another serial flip, single clipping plane, or one-dimensional support chain. It is a **one-boundary-component finite-thickness multi-page cell**, with at least two genuinely transverse support layers, spanning both residual stars and the intervening boundary strip. This is consistent with the journal’s repeated exact finding that realizable shell changes transfer the Euler-neutral packet unless the full component is deleted in one event. :contentReference[oaicite:2]{index=2}

### Limitation

All new samples in this handoff were evaluated using double-precision Qhull plus an independent reconstruction of maximal coplanar faces, true edges, ordinary centroid, and all equilibrium decisions. They have positive numerical topology margins, but they are **not** rational certificates or interval enclosures. They must not be integrated as accepted bodies. No new OBJ/STL was promoted because no new exact endpoint passed the equilibrium gate.

## Sharply delimited nonrepeating successor

Start from the two-plane topology, not from another perturbation of the original six-row octahedron. The old defects are already absent there, and the complete transferred component is explicit.

The replacement stable star is based on:

```text
{198,258,1000,1025}
```

The replacement saddle/cap star is based on:

```text
{1026,1027,1028,1029,247,228}
```

A shortest true-edge route joining the stars in the two-plane body is:

```text
258 — 54 — 69 — 228 — 1026 — 1028
```

The first untested topology should replace a neighbourhood of this complete route by one finite-thickness complex. The smallest defensible templates are:

1. a coupled pair of triangular prisms sharing a quadrilateral page;
2. a double-octahedral cell sharing one interior diagonal;
3. a three- or four-page clipping book whose adjacent page intersections are all true edges;
4. an equivalent `2↔3 / 3↔2` compound event with at least two inserted extreme supports and simultaneous deactivation of at least one old connector vertex.

The event must include the stable fan and saddle fan in one regular-subdivision circuit. It must not merely connect their graphs after the fact. Before accepting the far chamber, require all of the following simultaneously:

```text
all non-base face decisions < -epsilon
all non-U8 vertex decisions < -epsilon
all true-edge saddle decisions < -epsilon
base decision > epsilon
U8 decision > epsilon
all inserted supports irredundant
all connector pages exposed
one unchanged full-hull incidence event deletes the complete replacement component
```

At least six independent geometric controls should remain before centring, so that three survive elimination of the ordinary first moments. A practical parameterization is:

```text
2 page-depth controls
2 transverse skew controls
1 shared-diagonal or prism-twist control
1 connector-vertex deactivation control
3 dependent moment controls
```

The decisive anti-transfer ledger should explicitly include the four near-zero stable faces and four near-zero saddle edges printed above, not only the currently positive labels. The first admissible far cell is one where all eight are negative with a common strict margin before any unrelated face, vertex, or edge becomes critical.

## Recommended exactification route after a winning numerical chamber

1. Express every new support or clipping plane with a common rational denominator, initially `10^12` or larger.
2. Starting from the benchmark’s exact rational V-data, perform every edge/plane intersection with `Fraction` arithmetic:

```text
t = g(p)/(g(p)-g(q)),
new_vertex = p + t(q-p).
```

3. Reconstruct candidate maximal faces numerically only as a proposal; prove each supporting plane, incidence, nonincidence, and irredundancy exactly.
4. Triangulate every maximal face deterministically and compute signed volume and all first moments exactly.
5. Translate by the exact rational volume centroid and rerun the equilibrium audit from the translated V-data.
6. For every face, vertex, and true edge, certify all normal-cone components rather than replaying labels.
7. Derive a perturbation radius from the minimum exact normalized support, polygon-edge, vertex-dot, and edge-cone margins.
8. Write a clean-room verifier that reads only the final V/H data and reconstructs the hull and equilibrium class independently.
9. Generate OBJ and binary or ASCII STL from the certified maximal-face cycles and verify manifold edge multiplicity, orientation, Euler characteristic, and triangle parity.

The benchmark bundle’s `build_exact_endpoint.py`, `verify_exact_cleanroom.py`, interval verifier, and mesh verifier are suitable scaffolding once a true winning chamber exists.

## Reusable implementation

The principal evaluator used for the discovery work is [fast_eval2.py](sandbox:/mnt/data/m42_slot7/fast_eval2.py). It independently performs Qhull reconstruction, adjacent-simplex coplanar merging, maximal-face boundary cycles, exact-form ordinary centroid formulas in floating arithmetic, true-edge incidence, and exhaustive stable/unstable/saddle decisions. It should remain a proposer only; the exact benchmark verifiers remain authoritative.

## Bottom line

The old extra stable triangle and old saddle edge can be deleted together at the level of actual boundary incidence, but every tested one-plane, two-plane, thin-chain, and two-independent-support realization recreates an Euler-neutral stable–saddle packet. I did not obtain the required strict `(1,1,0)` polyhedron or a new exact nonwinner certificate. The strongest materially new frontier is the explicit two-plane-plus-two-support topology above: it leaves only a `2.91e-5` stable relay and a `5.94e-4` saddle relay while retaining strong intended equilibria, and it exposes the exact connector route that a finite-thickness multi-page terminal cell must replace. The next worker should build that connected prismatic/double-octahedral terminal directly rather than continue independent polishing of the two relay points.
