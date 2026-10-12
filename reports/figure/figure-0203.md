# figure-0203

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Quartz 90 — global exact resolution of the alternate-stable-row frontier

## Literal disposition

**GLOBAL FIXED-LATTICE NONWINNER.** No positive-definite metric in the exact Santaló-centred 4,324-row trace-one SPD orbit has strict own-centred class `(S,U,H)=(1,1,0)`.

Consequently, none of the six row-`2092` death-wall entrances

```text
12265, 12475, 12479, 12686, 12688, 12690
```

can lead to a Gömböc, regardless of which other face becomes the intended unique stable equilibrium, which order subsequent face and vertex walls are crossed, or whether the continuation is local or nonlocal inside the unchanged lattice.

This is strictly stronger than an entrance-by-entrance chamber atlas. The recovered exact no-gap core atlas partitions the entire remaining trace-one metric domain and leaves zero unresolved cells. The assignment’s six entrances and every alternate-stable-row continuation behind them are therefore subsumed by a global obstruction.

The durable journal had only accepted the preserved-row theorem and explicitly left cells with a different unique stable row open. It requested the six-wall alternate-row continuation as the next nonrepeating problem.  The decisive new development is recovery and clean verification of an unintegrated Sharp Quartz 52 no-gap core archive whose earlier run had been lost at the lifecycle boundary. The proof is independent of the old incomplete 256-cell relative-condition atlas and independent of the provisional 1,710-exit protocol.

## Exact fixed body, Santaló centring, and metric normalization

Let

```text
Q = conv{q_i},
q_i = Qint_i/2^48,
i = 0,…,4323,
P_* = (Q-a_*)^polar.
```

The exact integer generator contains 4,324 irredundant support rows. The unique Santaló point is isolated in

```text
a_* ∈ a_c+[-2^-90,2^-90]^3,

a_c = 2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856
).
```

Every polar denominator remains strictly positive throughout this box. Santaló stationarity gives

```text
∫_(P_*) x dx = 0
```

exactly.

Use trace coordinates

```text
x=(K00,K11,K01,K02,K12),
K22=1-K00-K11,
K=[[K00,K01,K02],
   [K01,K11,K12],
   [K02,K12,K22]],
K ≻ 0.
```

Positive rescaling of `K` does not alter any equilibrium sign, so `tr K=1` loses no metric chamber. With `A=K^-1/2`, define

```text
P_K=A P_*.
```

Then

```text
∫_(P_K) y dy = det(A) A ∫_(P_*) x dx = 0,
```

so every member of the metric orbit is exactly centred at its own ordinary-volume centroid.

The deterministic transformed representation is

```text
h_i(K)=A^-T(q_i-a_*),
v_f(K)=A y_f/(1-a_*·y_f),
```

where every baseline vertex `y_f` is reconstructed from its exact active support triple. Because `A` is invertible, it preserves incidences, maximal faces, and true edges. The actual lattice throughout the family is

```text
(H,V,E)=(4324,8644,12966),
boundary triangles=17284,
8644-12966+4324=2.
```

The clean verifier reconstructs those counts directly from the 8,644 active triples and verifies that each of the 12,966 support-row pairs has exactly two incident vertices. It also reconstructs all 25,932 directed face adjacencies and all 25,932 directed vertex adjacencies.

## Complete mechanical wall system

For adjacent maximal faces `i,j`, define

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j).
```

A maximal face `i` is stable precisely when every outgoing `S_ij` is positive.

For adjacent vertices `f,g`, with

```text
d_f=1-a_*·y_f,
```

define

```text
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g.
```

A vertex `f` is unstable precisely when every outgoing `W_fg` is positive.

A true edge with incident maximal faces `(i,j)` and endpoints `(f,g)` is a saddle exactly when

```text
S_ij>0,
S_ji>0,
W_fg>0,
W_gf>0.
```

Thus the exact wall system has

```text
25,932 directed face primitives,
25,932 directed vertex primitives,
12,966 four-component true-edge cones.
```

The wall-manifest verifier checks the complete index maps and does not infer physical edges from triangulation diagonals.

## Spectral reduction to one exact compact root box

The immutable Bright Atlas 91 projective covers give two global implications:

```text
lambda2/lambda1 <= 1/32  => S>=2,
lambda3/lambda2 <= 19/64 => U>=2,
```

where the eigenvalues are ordered

```text
lambda1>=lambda2>=lambda3>0.
```

The independently rerun stable cover performs 1,708,848 exact outward boundary checks. The unstable cover performs 826,913 exact outward boundary checks. The end-to-end verifier extracts and reruns both verifiers from the hash-locked parent archive rather than trusting stored labels.

A possible winner surviving both collars must satisfy

```text
lambda2/lambda1>1/32,
lambda3/lambda2>19/64.
```

These inequalities imply the sharper trace-one bounds

```text
lambda3>19/2131,
lambda1<2048/2131.
```

Indeed,

```text
lambda1 < 32 lambda2 < (2048/19)lambda3,
lambda2 < (64/19)lambda3,
1=tr K < ((2048+64+19)/19)lambda3.
```

Similarly,

```text
1=tr K > ((2048+64+19)/2048)lambda1.
```

For every off-diagonal entry, the spectral spread bound gives

```text
|Kij| <= (lambda1-lambda3)/2 < 2029/4262.
```

Hence every still-possible trace-one winner lies in the explicit closed five-coordinate root box

```text
19/2131 <= K00,K11,K22 <= 2048/2131,
|K01|,|K02|,|K12| <= 2029/4262.
```

The recovered atlas records this sharpened box and the exact derivation.

## Exact no-gap core atlas

The recovered `core_atlas.json` is an exact binary coordinate partition of the entire root box. Every split is at a literal dyadic coordinate value. The clean-room verifier begins at the stored root bounds, recursively reconstructs both children at each split, visits every node exactly once, and proves that the leaves cover the root box with no overlap gap and no unvisited branch.

Every terminal has exactly one of three certificate types.

### Stable-subset terminal

A stable terminal contains two disjoint nonempty face subsets `C1,C2`. Every directed face wall leaving either subset is strictly positive throughout the complete terminal box and throughout the full Santaló uncertainty.

For fixed `K`, define

```text
r_i=(q_i-a_*)^T K(q_i-a_*).
```

The exact identity

```text
2S_ij=r_i-r_j+(q_i-q_j)^T K(q_i-q_j)
```

shows that a maximizer of `r_i` inside each subset is stable: internal neighbors have the positive quadratic term, and external neighbors are handled by the certified outgoing boundary. Since the subsets are disjoint, the terminal has at least two distinct stable faces. Therefore

```text
S>=2.
```

### Unstable-subset terminal

An unstable terminal contains two disjoint nonempty vertex subsets. Every directed vertex primitive leaving either subset is strictly positive throughout the terminal and throughout the Santaló box.

The dual radial-energy identity for `K^-1`, equivalently its denominator-cleared `adj(K)` form used by `W_fg`, proves that each subset contains an unstable vertex. Hence

```text
U>=2.
```

### Spectrally outside terminal

An outside terminal contains an exact nonzero integer direction `z`. Directed interval evaluation proves

```text
z^T K z / ||z||^2 < 19/2131
```

throughout that terminal. The Rayleigh principle then gives

```text
lambda_min(K)<19/2131,
```

contradicting the necessary strict spectral bound for any metric that survived both projective collars.

The clean-room verifier reconstructs every subset from its member hash, regenerates every complete outgoing boundary, evaluates every used `S_ij` and `W_fg` by outward exact arithmetic, verifies disjointness of the two subsets, checks every rank-one separator, walks the full split tree, and returns

```text
unresolved_cells=0.
```

Its implementation explicitly excludes discovery state, floating search margins, and stored unverified boundary lists from the proof.

## Consequence for the six assigned entrances

The six exact row-`2092` death walls are:

| wall | directed transition | true edge |
|---:|---|---:|
| `12265` | `2092→2021` | `6132` |
| `12475` | `2092→2056` | `6237` |
| `12479` | `2092→2057` | `6239` |
| `12686` | `2092→2127` | `6343` |
| `12688` | `2092→2128` | `6344` |
| `12690` | `2092→2163` | `6345` |

Each is an actual affine face wall in the complete 25,932-wall manifest. The prior boundary atlas records its support-row identities, true edge, reverse directed wall, and exact energy relation.

The new no-gap theorem does not assume that row `2092` remains stable. It partitions the entire metric root box, including both sides of all six walls and every later chamber. Its stable certificates may involve arbitrary alternate face subsets, and its unstable certificates exclude chambers even when only one stable component remains. Therefore it covers:

```text
all six entrance facets,
all 12 local sides,
every order of later face and vertex crossings,
every possible alternate stable row,
every connected and disconnected trace-one SPD chamber
of the unchanged 4,324-row lattice.
```

An explicit source-to-each-wall path is unnecessary for the nonexistence conclusion: a path can only enter leaves already classified by the global partition.

`ALTERNATE_STABLE_SIX_ENTRANCE_GLOBAL_COVERAGE.json` packages this deduction in machine-readable form.

## Strongest materialized endpoint

No new endpoint can be a winner because the whole fixed-lattice SPD orbit is excluded. The strongest connected, fully materialized endpoint remains the exact `PRE_16494` box from the accepted source component.

Its trace-coordinate centre is

```text
38058021622708567468779065052408831524229350396217253673801/
200867255532373784442745261542645325315275374222849104412672

68823866389011966411118542450225602174405647045336189891889011937526327289495/
231584178474632390847141970017375815706539969331281128078915168015826259279872

-8086040717562568807395971691478655583608068878925139121630417916381129006345/
231584178474632390847141970017375815706539969331281128078915168015826259279872

9867350667506478391637498328764300086051839715332526886288437858398697026017/
231584178474632390847141970017375815706539969331281128078915168015826259279872

16509551414496109865973574542484601728952021384059036974122042120134933195101/
57896044618658097711785492504343953926634992332820282019728792003956564819968.
```

Its coordinatewise radius is

```text
2^-120.
```

The exhaustive box class is

```text
(S,U,H)=(2,2,2),
stable rows       {2092,2180},
unstable vertices {2028,2693},
saddle true edges {1603,11125}.
```

The whole box is trace-one SPD. Its determinant lower bound is approximately

```text
0.01148465559399398.
```

Its minimum complete directed face-wall clearance is approximately

```text
1.076435660283274e-7,
```

and its minimum directed vertex-wall clearance is approximately

```text
2.002232850861328e-9.
```

The exact rational Sylvester bounds and all 51,864 primitive intervals are retained in the prior endpoint archive. Its H table contains 4,324 actual maximal-face rows; its V table contains 8,644 actual vertices; its edge table contains all 12,966 true edges. The OBJ/STL contain 17,284 oriented boundary triangles and are watertight, with every triangulated edge of multiplicity two.

The acceptance gate requires exactly this kind of finite H/V, true-edge, positive-margin and mesh evidence; a near-wall or merely theorem-level unexpanded candidate would not qualify as a winner.

## Independent verification

Three independent checks are packaged.

### 1. Core-atlas verifier

`verify_core_atlas.py` reconstructs:

```text
4,324 support rows,
8,644 active triples,
12,966 true edges,
25,932 directed face walls,
25,932 directed vertex walls,
the complete exact binary split tree,
all stable and unstable subset boundaries,
all rank-one separators.
```

It verifies the Santaló uncertainty in every used primitive and returns `PASS` with zero unresolved leaves.

### 2. Dual clean-room replay

`verify_core_atlas_dual.py` follows an independent reconstruction path and does not import the discovery or build scripts. It checks the generator, topology, Santaló certificate, wall manifest, subset hashes, exact split coordinates, terminal inequalities, compressed/uncompressed atlas equality, and source hashes.

### 3. End-to-end theorem verifier

`verify_full_theorem.py`:

1. SHA-checks the immutable Bright Atlas 91 global archive and wall supplement;
2. reruns the no-gap core verifier;
3. extracts and reruns the stable projective-collar verifier;
4. extracts and reruns the unstable projective-collar verifier;
5. independently checks the complete wall-index manifest;
6. verifies that the core atlas has `unresolved_cells=0`;
7. emits the theorem:

```text
No invertible linear/SPD image of the exact Santaló-centred fixed
4,324-row lattice has strict own-centroid class (1,1,0).
```

The verifier source expressly reads no discovery pickle or floating search result.

The complete recovered package was also extracted into a clean directory and replayed through `verify_package.py`. The package verifier checks every manifested SHA-256 before rerunning all three theorem verifiers.

## Source integrity

The proof is anchored to the established exact fixed-lattice lineage:

```text
Bright Atlas 91 global archive
SHA-256 0f7f44f05688ac3f1102c23d2ea02a0854dcd454e8b9e60a319b24bd5476efb7

Bright Atlas 91 wall-system supplement
SHA-256 b7eb42d9f9c502640bd89212963294132890437cf42fbb109483812fc9236c72

generator.json
SHA-256 96d1281f408b145fb2f6a6891e64d1f7fefc4169802f2e31685cc3039125fd88

topology.json
SHA-256 216b4fb2f49a1ee2fbc642fb110c164707e7e1fc22e164dbe5ce4f06bf9694c7

santalo_krawczyk_certificate.json
SHA-256 f8c172f5177094b3db118ff87ae4424ae21cf551f073116443311d79f495ac5a

wall_system_manifest.json
SHA-256 d2a7b6f902f3b38649abdaecf46d1a1775e7c136ff473ee25bb91b59f8526517.
```

The six historical random-core search files remain discovery-only and are not read by any theorem verifier.

## Honest scope

The conclusion is global for exactly this fixed support generator and its complete invertible linear/SPD orbit. It excludes every trace-one metric chamber, not merely the component connected to `PRE_16494`.

It does **not** prove that no homogeneous convex polyhedral Gömböc exists with a different support generator or a topology-changing incidence. It also does not promote the provisional 1,710-exit protocol; that protocol is irrelevant to the recovered no-gap theorem.

## First genuinely unclassified successor topology

The fixed-lattice metric programme is now complete. Continuing through walls `12265/12475/12479/12686/12688/12690`, adding further metric walls, changing the intended stable row, or searching another disconnected SPD chamber cannot succeed.

The first mathematically new frontier is therefore topology-changing:

```text
change the support generator or actual incidence,
retain exact Santaló/ordinary-centroid control,
rebuild the H/V/E lattice,
and only then resume equilibrium cancellation.
```

A useful successor must introduce a genuine circuit or support-row event that invalidates at least one of the global subset certificates. Metric-only polishing of the 4,324-row body is rigorously exhausted.

## Reusable artifacts

- Complete global fixed-lattice impossibility archive (`Calm_Quartz_90_fixed_SPD_global_impossibility.zip`)
- Complete Markdown handoff (`Calm_Quartz_90_global_fixed_handoff.md`)
- Structured result (`Calm_Quartz_90_global_fixed_result.json`)
- Clean package-verification transcript (`Calm_Quartz_90_fixed_SPD_global_impossibility_VERIFY.txt`)
- End-to-end theorem receipt (`Calm_Quartz_90_global_fixed_FULL_VERIFY_RESULT.json`)
- Core-atlas verification receipt (`Calm_Quartz_90_global_fixed_CORE_VERIFY_RESULT.json`)
- Exact compressed no-gap core atlas (`core_atlas.json.gz`)
- Independent core verifier (`verify_core_atlas_dual.py`)
- End-to-end theorem verifier (`verify_full_theorem.py`)
- Six-entrance global coverage certificate (`ALTERNATE_STABLE_SIX_ENTRANCE_GLOBAL_COVERAGE.json`)
- SHA-256 manifest (`SHA256SUMS.txt`)
- PRE endpoint H data (`pre16494_H.csv`)
- PRE endpoint V data (`pre16494_V.csv`)
- PRE endpoint true-edge data (`pre16494_true_edges.csv`)
- PRE endpoint OBJ (`pre16494_mesh.obj`)
- PRE endpoint STL (`pre16494_mesh.stl`)
- Prior fully audited endpoint archive (`Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER.zip`)

## Final statement

**GLOBAL NONWINNER FOR THE FIXED 4,324-ROW SPD FAMILY.** Abandoning row `2092` does not open a Gömböc chamber. The two projective spectral collars and the recovered exact no-gap core atlas cover the complete trace-one SPD orbit. Every metric either has at least two stable faces, has at least two unstable vertices, or violates the necessary spectral inequalities. No strict own-centred `(1,1,0)` polyhedron exists in this fixed lattice. The next legitimate construction must change topology or support data.
