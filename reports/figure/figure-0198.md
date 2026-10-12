# figure-0198

AI research report · 2026-09-02 UTC

---

# Steady Quartz 25 — second finite-thickness cross-cap

## Literal disposition

**EXACT NONWINNER.** No strict homogeneous convex polyhedral Gömböc was obtained. The strongest accepted endpoint is a fully materialized exact-dyadic H-polytope, translated by its exact ordinary-volume centroid, with strict class `(S,U,H)=(2,2,2)`. The current journal had accepted the seven-hub predecessor and isolated loss of buttresses `500006` and `500002` as the preempting event; it therefore required the shared finite-thickness cross-cap attempted here. :contentReference[oaicite:0]{index=0}

The new cell **does overcome that incidence preemption**: both old buttresses and both new extreme supports remain active. It does **not** cancel the Euler-neutral block; it recreates it on a new carrier and exposes a rigorous forced-extra-unstable edge obstruction.

## Reproducible package

- [Complete archive](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER.zip), SHA-256 `493aded62e9ddfb627e3b4547707c0e95a6f13b34fb8f9586b5717517a51c025`
- [SHA-256 sidecar](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER.zip.sha256)
- [Standalone handoff](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/STEADY_QUARTZ_25_CROSSCAP2_HANDOFF.md)
- [Compact result certificate](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/result_summary.json)
- [Internal manifest](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/MANIFEST.sha256), SHA-256 `31ad1b2465e8c845054f2ef7c3a3403e2e08bce30628391e7573a282308aa02c`
- [One-command verifier](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/verify_steady_quartz25_crosscap2.sh)

## Exact final representation and incidence

The supplied raw body is

```text
P_raw={x in R^3 : q_i·x<=1, i=1,...,3490}.
```

All 3,490 supplied rows are given as exact hexadecimal dyadics in [supplied_endpoint_rows.hex](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/data/supplied_endpoint_rows.hex), and on a common `2^109` integer lattice in [supplied_endpoint_rows_integer.csv](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/data/supplied_endpoint_rows_integer.csv). The exact all-row audit proves precisely 1,631 active irredundant rows and 1,859 strictly inactive rows. The active rows are separately supplied on a common `2^69` lattice in [raw_polar_rows_integer.csv](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/data/raw_polar_rows_integer.csv).

The two inserted supports are

```text
q_500007=(-564137866310937,125731538513509,-781419066721)/2^48
q_500008=(-560143972966688,130772869826433,6134826260504)/2^48.
```

The reconstructed primal has

```text
supplied H rows                   3490
active maximal faces F            1631
vertices V                        3258
true edges E                      4887
oriented surface triangles        6512
Euler F-E+V                          2.
```

Every exact Cramer vertex is in [primal_vertices_exact.csv.gz](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/geometry/primal_vertices_exact.csv.gz), every maximal-face cycle in [maximal_face_cycles.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/geometry/maximal_face_cycles.json), and every true edge with its two incident maximal faces in [true_edges.csv](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/geometry/true_edges.csv).

The independent exact `cpp_int` verifier performs 11,360,646 nonincident determinant checks and proves: no extra coplanar supplied row, no outside row, all 3,258 dual facets connected, minimum nonincident primal slack

```text
>1.4689227575116868179486308837739759907e-9,
```

and minimum inactive supplied-row slack

```text
>1.7538767343858914579767352546038874965e-3.
```

The complete report is [exact_supplied_hull_report.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_supplied_hull_report.json).

## Exact cross-cap combinatorics and finite thickness

The operation is one simultaneous 15-triangle disk exchange inside the predecessor’s nonannular cap. The old and new disks each have `(V,E,F)=(14,28,15)`, Euler characteristic one, and the same 11-edge boundary:

```text
(1801,1802) (1801,1836) (1802,500005) (1836,2811)
(2592,2774) (2592,500002) (2774,2775) (2775,2811)
(500002,500003) (500003,500004) (500004,500005).
```

The old disk contains internal supports `500000,500001`; the new disk removes both and contains `500007,500008`. The retained internal edge `(1801,500006)` changes both incident sheets:

```text
old: (1801,1802,500006), (1801,500001,500006)
new: (1801,500006,500007), (1801,500006,500008).
```

Thus saddle side A `{1802,500006,500005,500001}` and side B `{2592,500002,500003,500000}` are changed in one connected cross-cap, not by serial star repairs. Full combinatorics are in [crosscap2_topology.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/crosscap2_topology.json).

Finite thickness is exact. Two positive-volume Delaunay tetrahedra in `conv(Q)` are

```text
T_A={500002,500006,500007,500008}
V_A=119645705502220441677513914879830678467141757 /
    35076039295941670036888435985190792471742381031424
   =3.411038073391130143e-6...

T_B={500002,500003,500007,500008}
V_B=2207936394842913301373802875771098297236187 /
    8769009823985417509222108996297698117935595257856
   =2.517885644059446020e-7....
```

They share the interior face `(500002,500007,500008)`, occupy exact opposite sides of it, share new edge `(500007,500008)`, and have strict empty circumspheres against all other 1,627 active rows. This is certified in [exact_finite_thickness_crosscap.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_finite_thickness_crosscap.json).

Activity after the crossing is exact:

```text
500002 active  +0.002046382902606725...
500006 active  +0.0000631838047288058...
500007 active  +0.012676633514007829...
500008 active  +0.009927883023664208...
500000 inactive -0.0031365866125301345...
500001 inactive -0.0022228393792237404....
```

## Shape rank and exact moment elimination

Nine independent shape pivots are used:

```text
500007-x, 500007-z, 500008-x, 500008-z,
500002-y, 500006-y, 500003-z, 500005-z, 500004-x.
```

Their exact supplied-row Jacobian contains a literal `9×9` identity minor, so shape rank is nine. The `500002-y` and `500006-y` columns are dedicated anti-inactivity controls for the predecessor’s first-lost buttresses. Details are in [control_space.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/control_space.json).

For every shape setting, the three dependent centroid variables satisfy exactly

```text
F(a,m)=M(P_raw(a))-V(P_raw(a))m=0,
m=M/V,
dF/dm=-V I_3,
rank(dF/dm)=3,
det(dF/dm)=-V^3<0.
```

Hence all nine shape dimensions survive local exact moment elimination. Eighteen actual-hull rebuilds give numerical rank four for the four unwanted wall functions, with singular values

```text
72.9036111354, 34.0469052834, 0.8647275565, 0.4592899465,
```

and rank six for the complete six-feature map. Control dimension is therefore not the diagnosed failure; the rank statement for wall action is numerical discovery evidence, while the H-lattice and moment ranks are exact.

## Rebuilt incidence path and search scope

The deterministic chord from the exact predecessor to this endpoint was rebuilt with the **actual all-row hull** at every sampled signature change. The recorded representatives occur at `t=0,0.01,0.06,0.94,0.95,1`; they show exact endpoint carriers `500000/500001` becoming inactive, support `500008` entering, and then the final simultaneous 15-triangle exchange with `500007` entering while `500002/500006` remain active. The complete changed-facet lists are in [crosscap2_actual_hull_path_scan.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/search/crosscap2_actual_hull_path_scan.json). These sampled parameter locations are discovery data, not claimed exact wall roots; the predecessor lattice, post-crossing lattice, and their disk symmetric difference are independently exact.

A separate 199-state two-support roof scan rebuilt the full hull, centroid, and complete mechanics for every retained candidate; every recorded state had class `(2,2,2)`. The nine-control common-descent continuation likewise found no sampled `(1,1,0)` cell before further incidence change. These scans support the selected endpoint and successor choice but are not global exclusions. The raw records are [roof grid](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/search/sq25_crosscap_roof_grid.json) and [post-wall common descent](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/search/common_descent_postwall_scan.json).

## Exact ordinary volume and first moments

The final mass is not obtained by floating recentering. The certificate starts from the predecessor’s exact full-body rational mass and recomputes every changed oriented maximal-face contribution with exact `Fraction` arithmetic: 1,617 unchanged faces, 12 changed common faces, two removed faces (`500000,500001`), and two added faces (`500007,500008`). A separate GMP finalizer regenerates the canonical rationals byte-for-byte.

Directed readback intervals are

```text
V  in [5.310004797811791582802631944505670236382641948666265576,
       5.310004797811791582802646545088336099127403957247556094]
Mx in [-0.3468645356266581870896060081968769665468193337413594145,
       -0.3468645356266581870896012240892910469534805759821122547]
My in [ 0.1648432291691341199070312926760092311078295781971595091,
        0.1648432291691341199070351918363251958909565846041586110]
Mz in [ 0.3014355735522715751061852053399502360986750901533898314,
        0.3014355735522715751061940553429057471476042452747799999].
```

The exact raw centroid `c=M/V` lies in

```text
cx [-0.06532282904331803079299273336506909738385619598272675872,
    -0.06532282904331803079299165278997174547532962141810727674]
cy [ 0.03104389458123740892518257253004467036590815551750133850,
     0.03104389458123740892518339219394909133062863525550229837]
cz [ 0.05676747668410594382313935749807581561732097432143833630,
     0.05676747668410594382314118025371542602651115317779568361].
```

The canonical certificate stores the complete reduced numerators and denominators and checks, by exact integer cross-products,

```text
Mx-Vcx=0, My-Vcy=0, Mz-Vcz=0.
```

The accepted own-centred body is `P_raw-c`; equivalently its normalized exact H rows are `q_i/(1-q_i·c)`. See [exact_mass_centroid.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_mass_centroid.json) and the independent [delta-circuit derivation](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_mass_centroid_delta_circuit.json).

## Exhaustive mechanics and strict margins

The actual own-centred endpoint equilibria are exactly

```text
stable rows:       3911, 500007
unstable vertices: (1836,2811,500008), (2024,2377,500004)
saddle true edges: (1802,500007), (2592,500003).
```

Thus strict `(S,U,H)=(2,2,2)`. Target `S3911` and target `U(2024,2377,500004)` survive. Old `S500000`, old `U(1836,2775,500001)`, and old `H(1802,500005)` disappear; `H(2592,500003)` persists; `500007/500008` carry the replacement packet.

A directed outward interval audit perturbs every coordinate of every **active irredundant** row independently by `±2^-100`, reconstructs interval vertices and the ordinary centroid, and exhaustively checks all 1,631 face tests, 3,258 vertex cones, and all four components of all 4,887 true-edge cones. No feature is ambiguous. Separately, an exact determinant certificate perturbs all 3,490 supplied rows—including the 1,859 inactive rows—by the same radius and proves that the active set and entire H/V/E lattice persist. Decisive intervals are

```text
minimum positive stable: S3911
[0.0007233225885748559781337916352425221,
 0.0007233225885748559781384453395172021]

minimum positive unstable component: U(1836,2811,500008)
[0.4764421077029864067123720481306999353,
 0.4764421077029864067123750509093962489]

protected-U strict component:
[0.820908630072741677640547702840191350,
 0.820908630072741677640550699789203398]

minimum positive saddle component: H(2592,500003)
[0.0952158386440844522425824553525069980,
 0.0952158386440844522425856011009103866].
```

Closest excluded margins are about `-3.169826338e-4` for faces, `-1.247011528e-2` for vertices, and `-7.891535217e-3` for edge-cone components. The complete audit and individual ledgers are [here](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/full_interval_mechanics_radius_2^-100.json), [stable](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/stable_margin_ledger.csv.gz), [unstable](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/unstable_margin_ledger.csv.gz), and [saddle](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/saddle_margin_ledger.csv.gz).

## Certified open cell

The exact determinant proof certifies the full independent supplied-coordinate box

```text
|delta q_ij|<=2^-100=7.888609052210118054e-31.
```

The all-row determinant certificate preserves the active/inactive set, all Q triangles, all primal maximal faces and true edges. Combined with the active-row interval mechanics certificate, this preserves `(2,2,2)` throughout the full supplied-row box. The endpoint is an open nonwinner, not a wall point. See [exact_topology_radius_2^-100.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_topology_radius_2^-100.json).

## Independent verification and mesh

A fresh replay after final packaging passed both the manifest and the normal verifier. The clean-room [verify_independent.py](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/src/verify_independent.py) imports no builder or search evaluator. It reconstructs the original 3,481-face source, predecessor and final all-row hull; rebuilds cycles and edges; checks exact Cramer equalities; independently recomputes the changed-face moment delta and exact centroid identities; reruns the finite-thickness, forced-edge and interval certificates; and reloads both meshes. It ends with

```text
INDEPENDENT_EXACT_CROSSCAP2_RECONSTRUCTION_PASS.
```

The independent exact [C++ verifier](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/src/verify_exact_supplied_hull.cpp) ends with

```text
INDEPENDENT_EXACT_SUPPLIED_HULL_PASS
rows=3490 active=1631 facets=3258 edges=4887 checks=11360646.
```

The [OBJ](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/geometry/crosscap2_own_centered.obj) has 3,258 vertices and 1,631 maximal polygon faces. The [STL](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/geometry/crosscap2_own_centered.stl) has 6,512 consistently oriented triangles and 9,768 undirected triangle edges; every edge has incidence two, Euler characteristic is two, and reload is watertight. Its float32 reload volume is `5.310004825149934`, differing from the exact volume by about `2.73e-8` solely at mesh encoding precision.

## First rigorous residual obstruction

The new true Q edge `(2811,500008)` has primal endpoints

```text
A=(1836,2811,500008),
B=(2775,2811,500008).
```

Every nonmutual endpoint support at A and B is an exact positive rational, with minima about `0.16416353170655848` and `1.7209055114475513`. The two mutual supports satisfy exactly

```text
support(A toward B)+support(B toward A)=||A-B||^2
||A-B||^2=1.950811276701591308e-6...>0.
```

They therefore cannot both be nonpositive. Since every external support is positive, at least one endpoint of this true edge is strictly unstable throughout every fixed-incidence chamber retaining these signs. The protected vertex `(2024,2377,500004)` is independently strict, so `U>=2` throughout that certified chamber. The exact proof is [exact_forced_unstable_edge_obstruction.json](sandbox:/mnt/data/Steady_Quartz_25_crosscap2_exact_NONWINNER/certificates/exact_forced_unstable_edge_obstruction.json).

This is a local chamber theorem, not a global nonexistence theorem. The edge is the current diagonal of circuit `{1836,2775,2811,500008}`; merely reversing it recreates the predecessor channel. Diagnostic isolated flips of the saddle channels also transfer rather than cancel.

## Forced nonrepeating successor

The smallest evidence-forced continuation is a higher-valence five-point `2↔3 / 3↔2` shared volumetric circuit that deletes edge `(2811,500008)` while the same finite-thickness cell absorbs

```text
S500007,
new U carrier adjacent to 500008,
H(1802,500007),
H(2592,500003),
```

without disturbing `S3911` or `U(2024,2377,500004)`. One additional extreme support is topologically sufficient to create a five-point event; two connected supports are preferable to retain finite thickness and independent antibirth freedom. The three ordinary moments remain dependent hard equations. This is forced within this architecture, not proved globally minimal.

## Final determination

```text
WINNER:                               NO
DISPOSITION:                          EXACT NONWINNER
PREDECESSOR INCIDENCE PREEMPTION:     OVERCOME
SECOND CROSS-CAP:                     EXACT FINITE-THICKNESS TWO-CELL PASS
OLD BUTTRESSES 500002/500006:         BOTH ACTIVE
NEW SUPPORTS 500007/500008:           BOTH ACTIVE
ENDPOINT (F,V,E):                     (1631,3258,4887)
ENDPOINT CLASS:                       (2,2,2)
EXACT ORDINARY CENTROID IDENTITIES:   PASS
EXACT IRREDUNDANT H/V/E AUDIT:        PASS
FULL-CONE INTERVAL AUDIT:             PASS
OPEN PERTURBATION RADIUS:             2^-100
INDEPENDENT RECONSTRUCTION:           PASS
WATERTIGHT OBJ/STL:                   PASS
MECHANICAL EFFECT:                    PACKET TRANSPORT/RECREATION
FIRST RIGOROUS OBSTRUCTION:           FORCED EXTRA U ON EDGE (2811,500008)
GLOBAL NONEXISTENCE CLAIM:            NONE
NEXT CELL:                            FIVE-POINT HIGHER-VALENCE SHARED CELL.
```
