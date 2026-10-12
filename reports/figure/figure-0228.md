# figure-0228

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Nova 91 — exact one-boundary triple-spine continuation

## Immutable determination

**EXACT NONWINNER.** No strict homogeneous convex polyhedral Gömböc was obtained. The materialized body is a finite exact-dyadic uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, but its exhaustive equilibrium class is

```text
(S,U,H) = (2,2,2).
```

It is nevertheless the first exact topology-changing endpoint on this branch to delete all three true-edge channels of the inherited unstable triangle in one one-boundary operation and to provide a connected positive-volume triple-spine carrier. It does not supersede the run-wide rational M42 `(61,163,104),(2,1,1)` benchmark.

## Journal basis

The run acceptance gate is a materialized finite uniform-density convex polyhedron at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete finite incidence/mechanics evidence, independent verification and OBJ/STL; near-objects and artificial-centre results do not qualify.

The supplied journal records the accepted 3,494/1,624-support linked-octahedra parent, its strict `(2,2,2)` replacement packet, the exact three-edge forcing theorem for `T=(1836,2775,500011)`, and the triple-spine finite-thickness successor required here.

## 1. Source and deterministic reconstruction

The accepted parent is encoded completely in:

```text
source/parent_terminal_rows.hex
SHA-256 57542467905453bae2a40c33b38a3172a7dc6668ce0b3ec5436e89900c23ec75
```

Each hexadecimal binary64 coordinate is interpreted as its exact dyadic rational. `src/build_endpoint.py` applies IEEE-754 round-to-nearest-ties-to-even multiplication

```text
q_500015 *= 3/4
q_1802   *= 7/8
q_2592   *= 7/8
q_500011 *= 1/2
```

and appends the three exact connected supports

```text
600000 = (-0x1.12d908a06b6b3p-5,
           0x1.4d3d48dcdc1cap-7,
           0x1.6d003dd22f97cp-2)

600001 = (-0x1.1c2d2459eb8dep+0,
          -0x1.6f658eda52157p-5,
           0x1.aee6b70781e33p-3)

600002 = (-0x1.6977540954289p-1,
           0x1.2070d6ef0542cp-1,
           0x1.6b9e0b2863eb7p-3).
```

The exact recipe is `source/construction_recipe.json`. The regenerated terminal source is

```text
data/supplied_endpoint_rows.hex
SHA-256 1b9e2bda6ba2742cdc3b9cd00a2819b5848c7da5d2000969f29f3c9cd4cd09b3.
```

The equivalent common-denominator integer H source is `data/supplied_endpoint_rows_integer.csv`, with denominator `2^109`. Active rows are separately listed in exact hexadecimal and integer form.

## 2. Complete irredundant incidence

The independent exact all-row reconstruction gives

```text
supplied H rows                         3497
active irredundant H rows / primal F    1624
strictly inactive supplied rows         1873
primal vertices V                       3244
true primal edges E                     4866
oriented surface triangles              6484
Euler V-E+F                             2
exact nonincident determinant checks    11334536
extra coplanar supplied rows             0
outside supplied rows                    0.
```

Complete files:

```text
data/active_rows_integer.csv
geometry/primal_vertices_exact.csv.gz
geometry/maximal_face_cycles.json
geometry/true_edges.csv
geometry/q_facets.csv
geometry/surface_triangles.csv
```

Every primal vertex is an exact Cramer rational. `geometry/true_edges.csv` contains exactly the maximal-face boundary edges; fan triangulation diagonals used only for mass integration and STL output are not promoted to true edges.

Exact separation lower bounds are

```text
minimum nonincident primal slack   1.4689227575116868179486308837739759907224637992927916971036166648929600e-09
minimum inactive supplied-row slack 4.6086039101879198905893571962756910424148480471921048009986360964623681e-04.
```

## 3. Exact volume, moments, and ordinary centroid

The GMP rational engine sums all 6484 consistently oriented exact boundary triangles and obtains

```text
V  = 5.418287994892484569034370667805119261430873036865263368647774565327923282993532184453118607e+00
Mx = -3.880329586354202267215679344645182433852539431909912835118853167967205358129874169764974455e-01
My = 2.130815733920103594136882201320853267150567593739694998395987068850036614133563955821280402e-01
Mz = 4.484817974197362959246868973128650984244205499426195954140259418346158531185240821818890744e-01

cx = -7.161541782223408544242747358947996149170662294158497228268772604902607794618904272579502153e-02
cy = 3.932636537461101687623589056354849635228987939630450524620627381634622428163815680325849325e-02
cz = 8.277186407265447479454012193769095200202416157241399562740108516217187444852896762873096345e-02.
```

The complete reduced fractions are in `certificates/exact_mass_centroid.json`; exact cross-products prove `M_i-Vc_i=0` for all three coordinates. The accepted own-centred body is `P_raw-c`. Equivalently, normalized centred supports are `q_i/(1-q_i·c)`.

The three centroid variables remain dependent hard equations because

```text
F(a,c)=M(P(a))-V(P(a))c,
dF/dc=-V I_3,
rank(dF/dc)=3,
det(dF/dc)=-V^3<0.
```

The construction has thirteen explicit shape controls—four old-row scale controls and all nine coordinates of the three new supports—with a nonzero diagonal input-map minor. See `certificates/control_space.json`.

## 4. Exhaustive own-centroid mechanics

The exact strict endpoint features are

```text
stable maximal faces
  3911
  500004

unstable vertices
  (2024,2377,500004)
  (2775,600000,600002)

saddle true edges
  (1838,500004)
  (2627,500004).
```

Thus intended `S3911` and intended `U(2024,2377,500004)` are preserved. The inherited packet is gone, but a replacement packet is strict:

```text
S500004,
U(2775,600000,600002),
H(1838,500004),
H(2627,500004).
```

A 768-bit outward MPFR audit independently varies every active H coordinate by `±2^-100`, recomputes all vertices, volume, moments and centroid interval-wise, and checks

```text
stable directed components      9732
unstable normal-cone components 9732
saddle full-cone components    19464
ambiguous components               0.
```

Certified decisive intervals:

```text
minimum positive stable   ['1.067608474430894519588801781442975065083042545e-05', '1.067608474430894520081965368427620346891702826e-05']
closest negative stable   ['-1.091970955242123210643782846378050553766735513e-05', '-1.091970955242123210198965326796667484157396336e-05']
minimum positive unstable ['9.522770819746023933161780265355934103428281860e-03', '9.522770819746024349349699798756035124827379889e-03']
closest negative unstable ['-2.819219215687199414927251491828782052078482863e-03', '-2.819219215687199226388574806457713019814856568e-03']
minimum positive saddle   ['1.424121106547355611941998656833987209457884156e-03', '1.424121106547355613442083107277445425098911471e-03']
closest negative saddle   ['-7.898183575264934141736531448983055146845732739e-05', '-7.898183575264934140303756635532446196046479090e-05'].
```

The full midpoint inspection ledgers are compressed in `certificates/*_component_ledger.csv.gz`; the interval certificate is authoritative.

## 5. Open topology and mechanics cell

`certificates/exact_topology_radius_2^-100.json` proves that independent perturbation of every coordinate of every one of the 3497 supplied rows by `±2^-100` preserves the complete active/inactive set, all Q facets, all maximal primal faces and all true edges. The interval mechanics certificate preserves `(2,2,2)` over the same box. This is an open nonwinner, not a wall point.

## 6. Exact one-boundary topology change and feature genealogy

The parent-to-terminal symmetric difference is one connected disk-to-disk exchange. Both disks have

```text
(V,E,F)=(20,41,22), chi=1,
boundary length=16,
boundary components=1.
```

Their common boundary cycle is

```text
1801-1836-2811-2775-2774-2838-2662-2697-
2661-2626-2591-2556-2485-500004-1838-1837-1801.
```

The operation deletes the entire inherited packet

```text
S500015,
U(1836,2775,500011),
H(1802,500004),
H(2592,500015)
```

and all three true edges

```text
(1836,2775), (1836,500011), (2775,500011).
```

The full removed and added triangle lists and exact genealogy are in `certificates/exact_one_boundary_disk_exchange.json` and `certificates/exact_feature_genealogy.json`.

## 7. Falsification of the naive transition shell

The obvious abstract sphere obtained by gluing the removed parent disk to the added endpoint disk is **not embedded**. Exact triangle-intersection tests find three nonadjacent intersections, including the old unstable triangle with two new terminal triangles. It is therefore explicitly rejected in `certificates/naive_surface_shell_rejection.json` and is not used as the positive-volume certificate.

This correction is material: the valid transition carrier below was reconstructed independently as a convex tetrahedral 3-ball rather than inferred from the surface symmetric difference.

## 8. Valid connected finite-thickness triple-spine 3-ball

The exact carrier begins with the combinatorial octahedron

```text
O={1836,2775,500011,600000,600001,600002},
```

whose old face is `T=(1836,2775,500011)` and whose opposite new face is `(600000,600001,600002)`. Its exact positive volume is

```text
1637580384373187866623885709395698474257937990671 /
4489733029880533764721719806104421436383024772022272
= 3.6473892177432248181307189079043857295364297298705767260716989995319362E-4.
```

Exact beyond-beneath insertions in order

```text
2592,2627,500015,500004,1838,1802
```

attach across one connected visible boundary disk at every step. The final convex complex has

```text
tetrahedra                 18
vertices                    12
all edges                   39
boundary triangles          20
3-complex Euler              1
boundary Euler               2
boundary components          1
connected tetrahedral dual  yes.
```

Its exact union volume is

```text
2435895540157235390247993797760006394156545764778715 /
4489733029880533764721719806104421436383024772022272
= 5.4254796976693546378946361524112887894315325475415143551914591626535354E-1.
```

The minimum exact tetrahedron volume is `1.6622332382822834421546425690805378220077836722432102529415283982799740E-5`. The central octahedron places all three inherited T channels on one face and all three new supports on the opposite face; the six coned pages include both old saddle edges, old stable row, terminal stable/saddle stars and the replacement unstable triangle. This is a genuine higher-valence positive-volume event, not a serial surface sheet or supporting-face concurrence.

## 9. Death-versus-birth chronology

For the exact named natural chord

```text
q500015(t)=(1-t/4)q500015(0)
q1802(t)=q2592(t)=(1-t/8)q(0)
q500011(t)=(1-t/2)q500011(0)
q600000(t)=t q600000(1), and likewise 600001,600002,
```

all other supplied rows fixed, the exact checkpoint `t=5/1024` is already

```text
(S,U,H)=(3,2,3)
S={3911,500004,500015}
U={(1836,2775,500015),(2024,2377,500004)}
H={(1802,500004),(2592,500015),(500004,500015)}.
```

New strict `S500004` and `H(500004,500015)` have appeared while inherited `S500015` and both inherited saddles remain strict. Therefore this actual-hull chord fails the required death-before-birth ordering. This is an exact obstruction for the named chord only, not a continuum exclusion of every route through the topology.

## 10. Complete terminal forcing component

The replacement unstable triangle

```text
T'=(2775,600000,600002)
```

has all three edges true. For each edge, every nonmutual endpoint support is an exact positive rational and the mutual supports obey

```text
sigma(A->B)+sigma(B->A)=||A-B||^2>0.
```

The three squared edge lengths are

```text
6.982552260322333398732699618169884789420524546244881853463219e-04
5.055387002782819599646171853011753711793058830407653718711849e-01
2.807962072084112500873889439028340152753588330610629366109522e-06.
```

If the common owner is unstable, the terminal component supplies an extra maximum. If not, each of the three distinct opposite endpoints is forced unstable. The disjoint protected vertex `(2024,2377,500004)` is independently strict. Hence `U>=2` throughout every fixed-incidence/external-positive chamber retaining these signs. A successor must delete the complete forcing triangle/component or reverse an external sign in the same actual incidence event as the stable and saddle deaths.

## 11. Search scope

The discovery layer recorded 800 broad edge-anchored proposals, 8000 vertex-prism proposals, a 20-generation differential-evolution search, and 300 one-support stable-carrier breaker probes. No `(1,1,0)` sample occurred. These files are retained under `discovery_nonproof/`, explicitly as finite discovery evidence—not as an exclusion theorem.

## 12. Smallest genuinely nonrepeating successor

Within this branch, the first unclassified continuation is a **one-boundary two-stage cubical / chained-three-octahedron finite-thickness 3-ball**, or a smaller strictly stronger higher-valence equivalent. It must, in one shared positive-volume event:

1. delete all three true-edge channels of `T'=(2775,600000,600002)`;
2. kill `S500004`, `H(1838,500004)` and `H(2627,500004)` before any replacement equilibrium becomes strict;
3. preserve `S3911` and `U(2024,2377,500004)`;
4. retain the three ordinary moments as dependent hard equations.

Branch-local incidence requires at least four connected new extreme supports, or three supports plus coordinated deactivation/motion of `500004,2775,600000,600002,1838,2627`. One interior cell should reverse/delete the forcing triangle; a second communicating prismatic/octahedral cell must couple the opposite triangle to the stable/two-saddle star, supplying independent antibirth timing. This is not claimed globally topologically minimal.

## 13. Independent verification and mesh

`src/verify_exact_incidence.py` imports no discovery evaluator. It reconstructs the exact recipe, checks every Cramer equality, rebuilds all face cycles and true edges, verifies the exact mass identities and binds the transition, forcing, chronology and mesh certificates. The full `boost::multiprecision::cpp_int` verifier performs all 11,334,536 exact nonincident checks. The 768-bit MPFR mechanics programs are separate compiled implementations.

Fresh replay markers and byte-identical SHA comparisons are in

```text
logs/FRESH_REPLAY_TRANSCRIPT.txt
replay/FRESH_REPLAY_MATCHES.json.
```

The OBJ contains 3244 exact-centred display vertices and 1624 maximal polygon faces. The STL contains 6484 consistently oriented triangles. Both reload watertight; the OBJ polygon boundaries reproduce exactly all 4866 true edges.

Run bundled optimized verifiers:

```bash
./verify_all.sh
```

Recompile every C++ verifier from source before running:

```bash
BN91_RECOMPILE=1 ./verify_all.sh
```

## Final status

```text
WINNER                                      NO
DISPOSITION                                 EXACT NONWINNER
PARENT SUPPLIED/ACTIVE                      3494 / 1624
TERMINAL SUPPLIED/ACTIVE                    3497 / 1624
TERMINAL PRIMAL (V,E,F)                     (3244,4866,1624)
TERMINAL CLASS                              (2,2,2)
INTENDED S3911 / U(2024,2377,500004)        PRESERVED
ALL THREE OLD T CHANNELS                    DELETED
OLD STABLE AND BOTH OLD SADDLES             DELETED
ONE-BOUNDARY DISK EXCHANGE                  EXACT PASS
NAIVE OLD/NEW SURFACE SHELL                 EXACTLY REJECTED
CONNECTED FINITE-THICKNESS 18-TET 3-BALL    EXACT PASS
NATURAL CHORD DEATH-BEFORE-BIRTH            FAILS EXACTLY
REPLACEMENT FORCING TRIANGLE                T'=(2775,600000,600002)
FIXED-INCIDENCE TERMINAL CHAMBER            U>=2
EXACT ORDINARY CENTROID                     PASS
FULL H/V/E RECONSTRUCTION                   PASS
FULL FOUR-COMPONENT EDGE-CONE AUDIT         PASS
OPEN COORDINATE BOX                         2^-100
INDEPENDENT REPLAY                          PASS
WATERTIGHT OBJ/STL                          PASS
GLOBAL NONEXISTENCE CLAIM                   NONE
NEXT CELL                                   TWO-STAGE CUBICAL /
                                            CHAINED-THREE-OCTAHEDRON 3-BALL
```

## Reproducible archive

Download the complete exact archive (`Bright_Nova_91_triplespine_exact_NONWINNER.zip`)

```text
archive bytes  = 12638939
archive SHA-256 = d9cd53625dccd2707f7d382ddf2e8564b70ff0c5a1e9ae77ec2a8cc914abcaf8
manifest SHA-256 = f392e8716703fa47b29f3eeb324ced76ef6fd71bf84f3f6deb05004ede07a015
```

The ZIP was extracted into a clean directory, its 125-file manifest was checked, and both the independent exact reconstruction and watertight-mesh verifier passed from the extracted copy.
