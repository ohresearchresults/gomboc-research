# figure-0092

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Rapid Atlas 90 — P15 whole-star continuation

## Determination

**No homogeneous convex polyhedral Gömböc was obtained.** I therefore do not claim a `(1,1,0)` winner. The run's acceptance gate remains a finite ordinary uniform-density polyhedron evaluated at its own exact volume centroid, with exactly one stable maximal face, one unstable vertex, no saddle true edge, complete H/V and face-lattice data, strict open margins, an independent verifier, and matching OBJ/STL; auxiliary centers, wall points, smooth bodies, near-solutions, and unexpanded existence generators are excluded.

The strongest fully materialized endpoint is the exact rational support polyhedron

```text
P9 = {x in R^3 : H_i · x <= 1, i=0,...,8}
```

where “P9” denotes nine irredundant maximal support planes. It has

```text
(F,E,V,C) = (9,21,14,42)
Euler      = 14-21+9 = 2
exact ordinary uniform-volume centroid = (0,0,0)
exact first moment                     = (0,0,0)
exact equilibrium class                = (S,U,H)=(2,2,2)
exact volume, decimal view             = 0.44114661530081456
minimum raw inactive H/V slack         = 0.011478213633222727
minimum Euclidean inactive separation  = 0.0018359115459220983
minimum oriented tetra determinant     = 0.0048459443137567615
```

This is a strict open post-star chamber, not a wall point. Its exact certificate SHA-256 is

```text
53ca1a1a53a255bac846352d5e55af04dbde83e1c65c9133d20d14852d2c00c4.
```

## What changed relative to P15

The durable journal recorded exact P15 with complexity `78`, own centroid zero, and the transferred block stable row `0`, unstable triple `[18,32,102]`, and saddles `[2,9]`, `[26,102]`, while stable row `27` and the intended unstable lineage were retained.

The connected whole-star deformation/deactivation keeps the source labels

```text
[9,13,15,26,27,32,100,102,103]
```

and makes these P15 rows non-extreme:

```text
[0,1,2,18,25,101].
```

At exact P9, every inherited P15 defect label is absent:

```text
old extra stable row 0:        absent
old extra U [18,32,102]:       absent
old saddle [2,9]:              absent
old saddle [26,102]:           absent
```

The intended stable row `27` remains strict. The unstable target lineage is deliberately rebuilt as `[15,26,27]`. The Euler-neutral excess transfers to

```text
new extra stable row:          15
new extra U:                   [9,100,103]
new saddles:                   [13,26], [27,100]
Euler excess:                  1+1-2=0.
```

Thus the requested whole-star topology change was real and substantial: complexity fell from `78` to `42`, raw inactive separation rose from about `0.0042166` to `0.0114782`, and no conclusion relies on stale feature labels. It did not cancel the Morse block.

# Compact exact generator

The following nine precentering rows have support constant one. Each hexadecimal binary64 coefficient is interpreted as its **exact dyadic rational** (`Fraction.from_float(float.fromhex(...))`), not as a tolerance-valued decimal:

```text
source 9:   [ 0x1.f9b5a727c027ap+2, -0x1.81e6cb4c6d6eap+1, -0x1.4a0af64ced04fp-2 ]
source 13:  [ 0x1.2312b52c53f2cp+3, -0x1.59f7623ebb977p+2, -0x1.f2e1addf798e5p+0 ]
source 15:  [ 0x1.1e27bebfbb450p+3, -0x1.609be75d7e57bp+2, -0x1.02e2854657074p+1 ]
source 26:  [ -0x1.825d860acd07ep+0, 0x1.16d2525ea2eb7p+2, 0x1.dfe0ae19e623ap+0 ]
source 27:  [ -0x1.5ed34a3e982c2p+3, 0x1.2c70c33c74c4ep+1, -0x1.cf8630f42f365p-7 ]
source 32:  [ -0x1.16a333bb56517p+3, 0x1.bc6717ba18082p+1, 0x1.5ed14b53bf699p+0 ]
source 100: [ 0x1.4dbecdd9c4575p+1, -0x1.c5781d3f7120ap+1, -0x1.70ccef918f03ap+0 ]
source 102: [ -0x1.8f22b39e7cba9p+2, 0x1.069f7cc4abd26p+2, 0x1.4ed4b718d4723p+0 ]
source 103: [ -0x1.120c08072fbc0p+3, 0x1.6ca725454c6cep+1, 0x1.002b4abeac9d2p+0 ]
```

A deterministic exact expansion is:

1. Enumerate all `C(9,3)=84` three-plane intersections.
2. Retain exactly those rational points satisfying all nine inequalities.
3. Reconstruct each point's exact active set, all maximal-face cycles, and all true edges from common active pairs.
4. Integrate ordinary volume and first moment over outward tetrahedra obtained from those maximal-face cycles.
5. Let `c=M/V`; translate by `y=x-c` and renormalize each row by `H_i=B_i/(1-B_i·c)`.
6. Re-enumerate/audit every active equality, inactive slack, maximal face, actual vertex, true edge, and full normal cone.

`generate_p9_exact.py` implements precisely this expansion using Python standard-library `Fraction` arithmetic. A clean-directory verifier reproduces the exact JSON, H/V CSVs, lattice files, OBJ, and STL byte for byte.

For inspection, the final support-one rows are approximately

```text
source 9:    (  6.153129924043580, -2.347693613355575, -0.250983522644849 )
source 13:   ( 11.558805651946614, -6.869336320235390, -2.476386277085998 )
source 15:   ( 11.432366803121852, -7.043650875834921, -2.585717434457248 )
source 26:   ( -1.709092455725430,  4.933484533074513,  2.122745562594608 )
source 27:   (-10.907207695284422,  2.335183795883429, -0.014073271163569 )
source 32:   ( -5.746349016976377,  2.291232315476389,  0.904365016080791 )
source 100:  (  2.514547204354069, -3.416586247960629, -1.389332319765825 )
source 102:  ( -6.585957068231688,  4.333424504298129,  1.381223771298187 )
source 103:  ( -5.908549382110957,  1.965511171661066,  0.690386980190219 ).
```

The 14 final vertices, with active source labels, are approximately

```text
0  (-0.105050729742031,-0.861029257736661, 1.494289731175065)  [9,13,15]
1  ( 0.251490017849690, 0.214463574756526, 0.175134961899796)  [9,13,26]
2  (-0.263621930892911,-1.341645376132391, 2.102418054229845)  [9,15,100]
3  (-0.158468265642336,-1.168278365542203, 3.058702109126394)  [9,26,32]
4  (-0.421015046718726,-1.867409660919855, 3.161743223858319)  [9,32,103]
5  (-0.429855893968108,-1.889090923958638, 3.147806376683753)  [9,100,103]
6  ( 0.439190477718514, 1.826157597573571,-3.419488071673711)  [13,15,26]
7  ( 0.580055866702163, 3.099800771547710,-6.266153744825130)  [15,26,27]
8  (-0.160058370699555,-0.320701660193672,-0.220803505609010)  [15,27,100]
9  ( 0.435827825768213, 2.434753667985735,-4.836636898342737)  [26,27,102]
10 (-0.125770306287438,-0.301901630352535, 1.071477421648221)  [26,32,102]
11 (-0.145991878480834,-0.248796797427245, 0.808446768569105)  [27,32,102]
12 (-0.277763466608295,-0.859991170047542, 1.519644957626242)  [27,32,103]
13 (-0.404541329202949,-1.448586921516722, 2.110354624968986)  [27,100,103].
```

The linked exact CSV/JSON files contain the full rational numerators and denominators.

# Complete actual face lattice

## Maximal-face cycles

```text
source 9:   0 1 3 4 5 2
source 13:  0 6 1
source 15:  0 2 8 7 6
source 26:  1 6 7 9 10 3
source 27:  7 8 13 12 11 9
source 32:  3 10 11 12 4
source 100: 2 5 13 8
source 102: 9 11 10
source 103: 4 12 13 5
```

## True edges and incident source faces

```text
(0,1):[9,13]       (0,2):[9,15]       (0,6):[13,15]
(1,3):[9,26]       (1,6):[13,26]      (2,5):[9,100]
(2,8):[15,100]     (3,4):[9,32]       (3,10):[26,32]
(4,5):[9,103]      (4,12):[32,103]    (5,13):[100,103]
(6,7):[15,26]      (7,8):[15,27]      (7,9):[26,27]
(8,13):[27,100]    (9,10):[26,102]    (9,11):[27,102]
(10,11):[32,102]   (11,12):[27,32]    (12,13):[27,103].
```

Every active equality is exact, every inactive inequality is strictly positive, every maximal-face boundary has degree two, every true edge belongs to exactly two maximal faces, and `V-E+F=2`.

# Exact uniform centroid certificate

For each outward face triangle `T=(v0,v1,v2)`, define

```text
V = (1/6)  sum_T det(v0,v1,v2),
M = (1/24) sum_T det(v0,v1,v2)(v0+v1+v2).
```

All values are rational. If `c=M/V`, then after `y=x-c`,

```text
M_y = M - Vc = (0,0,0)
```

as an exact algebraic identity. The support renormalization `H_i=B_i/(1-B_i·c)` describes precisely that translated body. No external weights, point masses, auxiliary center, or floating post-correction is used.

# Exhaustive equilibrium audit at the exact own centroid

## Stable maximal faces

| Source row | Exact raw limiting slack | In-face Euclidean margin | Limiting row |
|---:|---:|---:|---:|
| `15` | `0.0003476778729570234` | `0.001439897028249965` | `13` |
| `27` | `0.3414724136155108` | `0.10741963346400699` | `102` |

Row `27` is the protected target; row `15` is the transferred extra sink.

## Unstable actual vertices

| Active source labels | Raw limiting radial derivative | Normalized cosine margin |
|---|---:|---:|
| `[9,100,103]` | `0.0008876711173775433` | `0.008813582752039174` |
| `[15,26,27]` | `11.102746186899935` | `0.9982006723619017` |

The second is the rebuilt intended unstable lineage. The first is the transferred extra unstable vertex.

## Saddle true edges and full normal cones

| Incident source labels | Minimum strict component | `(t,1-t,lambda0,lambda1)` |
|---|---:|---|
| `[13,26]` | `0.015217187497544365` | `(0.015217187497544365, 0.9847828125024556, 0.036729006215806215, 0.09958335087525313)` |
| `[27,100]` | `0.01683097550924557` | `(0.01683097550924557, 0.9831690244907544, 0.04507515470778835, 0.1302305307060208)` |

For every true edge the verifier computes the perpendicular line parameter and both coefficients in the complete two-face normal cone. A saddle is counted only when all four exact quantities are positive.

The closest excluded features remain strictly on the non-equilibrium side:

```text
face:   source 13 cut by source 15, raw -3.578633268223459e-5
vertex: active [9,32,103], raw -1.4519766116654197e-4
edge:   incident [13,15], raw -6.135633349081738e-4.
```

The exact result is therefore

```text
(S,U,H)=(2,2,2),  S+U-H=2.
```

# Open perturbation certificate

A directed interval verifier permits every coefficient of every one of the nine precentering rows to vary independently by

```text
|delta B_ij| <= 1e-11
```

in a full 27-dimensional box. For every member it reconstructs the same active triples, recomputes and translates by that member's own ordinary uniform-volume centroid, and proves

```text
same (F,E,V,C) = (9,21,14,42)
same class      = (2,2,2)
all nine rows remain irredundant
precenter inactive-slack lower bound      0.017392894860055907
face-orientation lower bound               0.15899389019528606
active-triple determinant lower bound      0.6048600519637972
equilibrium-sign lower bound               2.4536919363438159e-5.
```

The exact final support-one body's separately verified raw inactive slack is `0.011478213633222727`. The interval radius is certified but not claimed maximal.

# Topology and circuit path

The stored deterministic P15-to-P9 homotopy uses a cubic interpolation for retained rows, decays obsolete rows, rebuilds the complete hull, discards non-extreme rows, and recomputes the integrated own centroid at every accepted state. It contains

```text
87 strict states
44 distinct realized topologies
86 transitions
29 elementary four-row flips
28 distinct elementary circuit supports.
```

The 28 observed elementary circuit supports are

```text
{0,25,26,102}       {9,13,100,101}      {9,18,27,101}
{1,2,15,100}        {1,27,100,101}      {18,27,32,103}
{1,27,100,103}      {9,13,15,100}       {0,18,26,102}
{0,9,18,26}         {1,2,25,26}         {1,15,100,103}
{1,2,15,25}         {15,27,100,103}     {25,26,32,103}
{25,32,102,103}     {25,27,102,103}     {9,18,32,101}
{2,9,13,26}         {2,25,26,102}       {2,25,27,102}
{27,100,101,103}    {0,2,13,26}         {9,32,101,103}
{0,2,27,102}        {0,2,13,15}         {0,13,15,26}
{15,26,27,102}.
```

The first strict sampled disappearance brackets are

```text
old extra U [18,32,102]: t in [0.06000,0.06250]
old stable row 0:        t in [0.07125,0.08250]
old saddle [2,9]:        t in [0.10625,0.11250]
old saddle [26,102]:     t in [0.54750,0.58625].
```

The path passes through larger transfer classes, including `(6,3,7)`, `(5,3,6)`, and `(5,2,5)`, before returning to `(2,2,2)`. `circuit_summary.json` records every row activation/deactivation event and all 86 adjacent transitions.

This replay is deliberately labeled numerical topology provenance: it does not pretend to isolate the algebraic crossing parameters. Both endpoint bodies and the accepted P9 chamber are separately exact/directed-certified, and no success claim depends on a sampled wall.

# Attempts to break P9

The following materially distinct searches were completed:

1. **P9 fixed-cell and adjacent-cell optimization.** JAX/L-BFGS, support-coordinate minimax, and all 55 depth-one flip seeds found only `(2,2,2)` or higher-count transfer cells.
2. **Six-row compression.** The residual block was compressed to an exact-center six-row laboratory. Optimized linear crossings follow `(2,2,2)->(2,3,3)->(2,2,2)` or expand further.
3. **Thirty thousand one-row insertions.** None yielded strict `(1,1,0)`; rows either transferred the block or became new critical supports.
4. **Global six-row hard/count/lexicographic search.** The best apparent count reductions approach an origin-boundary/unbounded degeneration. Loose epsilon can print `(1,2,2)`, but the omitted stable sign remains strictly positive and the positive-spanning margin collapses.
5. **Topology-free nine-row search.** Through 574 reported generations, its best fully active own-centroid state remained `(2,2,2)`, general hard score about `-0.00632773339`, inactive slack about `0.00896348`.
6. **Long single-arm diagnostic.** Among 919 fully active bodies from 2,400 random parameters, the best was `(2,3,3)`; the arm transported the centroid macroscopically.
7. **Paired transverse arms.** Of 1,800 trials only seven remained fully active; the best was `(2,4,4)`, with extra unstable and saddle features born along the arms.

False positives were explicitly rejected. States relying on tolerance merging, origin-interiority collapse, auxiliary-center mechanics, or selected witness signs without complete hull reintegration are not retained.

# Exact/directed obstruction at P9

For support-one rows, if row `j` cuts the perpendicular foot of row `i`,

```text
a_j·a_i > ||a_i||^2,
```

hence `||a_j||>||a_i||`. Witness arrows are therefore acyclic and strictly increase row norm. An `m`-arrow path spanning angular separation `Theta` and radii `r0,r1` must satisfy

```text
r1 cos(Theta/m)^m > r0.
```

The exact/directed certificate proves

```text
||row 15|| > ||row 27|| exactly;
target-27 norm increase required to drain row 15: >22.5949369459687%.

||row 13|| > ||row 27|| exactly;
target-27 norm increase required to drain row 13: >22.57143014841516%.

row 9 -> row 27 angle: 170.917971... degrees;
all 1..8-arrow paths are excluded;
first arrow count not excluded: 9;
maximum simple-path arrows with nine rows: 8.
```

Consequently another short appended rail cannot solve P9. Rows `13` and `15` cannot drain to the present target at all without deactivation or a macroscopic norm reversal; the row-9 branch also needs more active supports than the current body possesses.

# Smallest genuinely new continuation

The smallest operation not subsumed by the failed P15 four-support family, P9 depth-one cells, six-row compression, or short witness rails is a **communicating three-lobed annular/norm-reversal replacement**:

1. Deactivate rows `13` and `15` only inside one connected topology change.
2. Replace simultaneously the complete stars of stable `15`, extra U `[9,100,103]`, and saddles `[13,26]`, `[27,100]`.
3. If target row `27` keeps approximately its present norm, provide at least a nine-arrow row-9 branch; a practical first family should use roughly 10–14 new extreme supports.
4. Cross-link three branches so every inserted row has an outgoing witness and cannot terminate as a new stable sink.
5. Permit obsolete rows `13,15,100`, and possibly `9`, to become non-extreme only during the coupled circuit event.
6. Reserve three mechanically inactive full-rank controls and solve all three ordinary uniform-volume first moments as dependent equations in every enumerated adjacent cell.
7. Preserve target stable row `27` and the intended unstable lineage, or deliberately rebuild both with strict margins.
8. Require raw inactive slack above `1e-4` before exactification.

The alternative is to increase target-row-27 norm by more than `22.6%`, but that is itself a macroscopic topology-and-moment operation, not local polishing.

# Reproduction and artifacts

Run from the extracted directory:

```bash
bash RUN_ALL_VERIFIERS.sh
```

The captured transcript ends with

```text
ALL VERIFIERS PASSED
```

The exact verifier, deterministic regeneration, mesh correspondence, full coefficient interval box, 87-state topology replay, and directed witness obstruction all pass independently.

- Complete P9 exact fallback bundle (`p9_whole_star_exact_fallback_bundle.zip`) — SHA-256 `87d401e1f5bb154cf908df64f43f64d027a5bd15092f76a3ab7f59fb8b99e6b9`.
- README and reproduction guide (`README.md`)
- Full exact certificate (`p9_exact.json`)
- Deterministic exact generator (`generate_p9_exact.py`)
- Independent exact verifier (`verify_p9_exact.py`)
- Byte-identical regeneration verifier (`verify_regeneration.py`)
- Exact H rows (`H_exact.csv`)
- Exact V coordinates (`V_exact.csv`)
- Maximal-face cycles (`faces.txt`)
- True-edge list (`edges.txt`)
- OBJ export (`p9_exact.obj`)
- STL export (`p9_exact.stl`)
- Mesh correspondence verifier (`verify_mesh_exports.py`)
- Full coefficient interval verifier (`verify_coefficient_radius.py`)
- Coefficient-radius certificate (`coefficient_radius.json`)
- Complete numerical topology path (`topology_path_numeric.json`)
- Independent topology replay (`verify_topology_path_numeric.py`)
- Circuit and transfer summary (`circuit_summary.json`)
- Directed witness-obstruction verifier (`verify_witness_obstruction.py`)
- Witness-obstruction certificate (`witness_obstruction.json`)
- Search record (`SEARCH_RECORD.md`)
- Combined verifier script (`RUN_ALL_VERIFIERS.sh`)
- Combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)
- Integrity manifest (`manifest.json`)
- SHA-256 list (`SHA256SUMS.txt`)

The delivered endpoint is therefore an exact, independently reconstructible complexity-42 post-star body with class `(2,2,2)`, complete transferred-block topology, a certified open coefficient box, and a sharply delimited next operation—not a claimed Gömböc.
