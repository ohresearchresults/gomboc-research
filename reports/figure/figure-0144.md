# figure-0144

AI research report · 2026-08-28 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Willow 49 — exact four-wall continuation inside the fixed 4,324-row trace-one SPD core

## Literal disposition

**No homogeneous convex polyhedral Gömböc was found.** No open own-centroid strict `(S,U,H)=(1,1,0)` metric chamber was encountered, and the whole compact five-dimensional core is still not covered. Global fixed-lattice nonexistence is therefore **not** proved.

The continuation nevertheless closes the requested local question at all four recorded decision-nearest walls and materially shrinks `R_SW49` by a machine-checkable adaptive atlas:

- `22` pairwise-disjoint full-dimensional all-wall boxes were certified, with complete sign vectors for all `51,864` directed walls and full four-component audits of all `12,966` actual true edges.
- `31` directed adjacency records, representing `20` distinct exact central segments, cross one and only one directed wall each.
- All four requested walls `F11907`, `F20290`, `V25755`, and `V25754` are crossed in exact full-dimensional children.
- Three larger relative-condition cells prove `S>=2` and contain **all 22** all-wall children. Their three pairwise-disjoint trace-one inner boxes remove exact new coordinate volume

```text
2^-50 + 2^-65 + 2^-75 - 2^-165
= 41539643756818888543025742236090367
  / 46768052394588893382517914646921056628989841375232
≈ 8.88205551224217e-16
```

from the prior remainder `R_SW49`. The subtraction `2^-165` removes the previously certified small root box already absent from `R_SW49`.

The decisive structural result is negative but sharp: the paired nearest vertex walls are opposite directed segment walls of the same actual true edge. They cross in the forced sign sequence

```text
(V25754,V25755): (+,-) -> (+,+) -> (-,+),
```

while the exhaustive class remains `(3,5,6)` in all three adjacent boxes. The event is a transfer, not a cancellation.

## 1. Exact body, Santaló root, and normalization

The fixed support generator is

```text
q_i = Qint_i / 2^48,  i=0,...,4323.
```

The globally unique Santaló point is isolated in

```text
a_* in a_c + [-2^-90,2^-90]^3,

a_c = 2^-120 *
  (-39878490350125864373364388380978345,
    88581653811863381217051,
    819441514472273259270856).
```

For

```text
P_* = (conv{q_i}-a_*)^circ,
```

the uniform-volume centroid is exactly zero. Its actual irredundant lattice is reconstructed as

```text
maximal faces / H rows = 4,324
vertices               = 8,644
true edges              = 12,966
Euler                    = 2.
```

Every invertible linear image remains exactly own-centred:

```text
integral_(A P_*) y dy = det(A) A integral_(P_*) x dx = 0.
```

Modulo rotation and scale, use the trace-one inverse metric

```text
K = [[k00,k01,k02],
     [k01,k11,k12],
     [k02,k12,1-k00-k11]] in SPD(3).
```

With ordered eigenvalues `lambda1>=lambda2>=lambda3>0`, the old compact core is

```text
17179/16384 < lambda1/lambda3 < 2048/19,
lambda2/lambda1 > 1/32,
lambda3/lambda2 > 19/64,
lambda3 > 19/4115,
trace(K)=1,
```

outside the parent 23-ball tube. After Sharp Quartz 52 it is further restricted to metrics above every applicable direction-dependent stable and unstable threshold and outside all 256 SQ52 relative-condition cells.

Boundedness is exact. The two ratio inequalities imply `lambda1/lambda3<2048/19`; trace one then gives `lambda3>19/4115`. Consequently the entire remaining search lies in

```text
k00,k11 in [19/4115,4077/4115],
k01,k02,k12 in [-2029/4115,2029/4115].
```

## 2. Complete mechanical wall basis

The clean-room reconstruction derives the actual row graph and primal graph from the `8,644` exact active triples and checks them against the exported true-edge list. It then reconstructs every wall in the manifest:

```text
25,932 directed face walls,
25,932 directed vertex walls,
12,966 actual true-edge four-component cones.
```

For adjacent support rows `i,j` and adjacent primal vertices `f,g`, the exact walls are

```text
S_ij(K) = (q_i-a_*)^T K(q_i-q_j),

W_fg(K) = d_g y_f^T adj(K)y_f
          - d_f y_f^T adj(K)y_g,

d_f = 1-a_*^T y_f.
```

An actual true edge with incident faces `(i,j)` and endpoints `(f,g)` is a strict saddle exactly when all four actual components are positive:

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

No feature-representative inference is used. Every claimed all-wall chamber is evaluated over the full isolated Santaló box and its full five-coordinate metric box.

## 3. Exact all-wall continuation at the four requested walls

The atlas contains `22` strict full-dimensional boxes. Their class histogram is

```text
(S,U,H)=(2,2,2):  7 boxes
(S,U,H)=(2,3,3): 12 boxes
(S,U,H)=(3,5,6):  3 boxes
```

There is no winner.

### Face wall `F11907`

An exact one-wall sequence reaches and crosses the target:

```text
V25062 -> F7701 -> V15590 -> V18958 -> V20106 -> F11907.
```

The first two boxes have class `(2,2,2)`. Crossing `V15590` creates one unstable vertex and one saddle; the remaining boxes, including both sides of `F11907`, have class `(2,3,3)`. The target face wall itself produces no reduction.

### Face wall `F20290`

The exact route is

```text
F7701 -> F20290.
```

Both sides remain strict `(2,2,2)`. Again the requested wall is mechanically neutral at the count level.

### Vertex walls `V25755` and `V25754`

These are not independent arbitrary walls. The reconstructed actual incidence is

```text
true edge:       12877
endpoints:       7473,7474
incident faces:  4281,4315
V25754:          7473 -> 7474
V25755:          7474 -> 7473.
```

Three exact adjacent boxes isolate the local swap:

```text
cell 19, before V25755:       (+,-), class (3,5,6)
cell 20, between the walls:   (+,+), class (3,5,6)
cell 21, after V25754:        (-,+), class (3,5,6).
```

The central segment `19->20` has exactly one straddling wall, `V25755`; after exact quadratic Bernstein refinement, all other `51,863` directed walls are fixed. Its certified minimum non-target margin outside the refined set is approximately `2.02934e-9`.

The central segment `20->21` similarly crosses only `V25754`, with corresponding certified margin approximately `3.53596e-10`.

This proves that the nearest directed pair exchanges orientation through a both-positive interval. It neither removes an unstable equilibrium nor cancels a saddle packet.

### Root-side prefix and remaining connection gap

The direct root-side continuation toward the pair has a certified exact prefix of ten one-wall cells:

```text
V25062, V15590, V20106, F7701, V18958,
V10276, V10757, F11907, V13261, V20503.
```

The straight route contains `2,175` wall groups before the target pair. The first ten are boxed exactly; the local target pair is boxed exactly; the intervening `2,164` groups are enumerated but have not all been promoted to five-dimensional exact boxes. This is the first sharply delimited unclassified connection, not an unstated sampling gap.

## 4. Adaptive relative-condition cover of every explored child

For an exact trace-one centre `C` and rational `kappa>1`, define

```text
B(C,kappa) = {K in SPD, trace(K)=1:
              exists mu>0 with mu C <= K <= kappa mu C}.
```

For a directed stable boundary, write

```text
b=q_i-a_*, d=q_i-q_j,
c=b^T C d, p=b^T C b, q=d^T C d.
```

Uniform positivity throughout `B(C,kappa)` follows from

```text
F=(1+kappa)c+(1-kappa)sqrt(pq)>0.
```

The verifier avoids floating square roots. Over the complete Santaló box it proves `c_lower>0` and the exact squared inequality

```text
(1+kappa)^2 c_lower^2
  > (kappa-1)^2 p_upper q.
```

Two disjoint singleton row subsets therefore force `S>=2` throughout the complete relative-condition cell.

### Relative cell R0 — root four-wall neighbourhood

```text
C0 = 2^-56 *
[[35859258939986176,13567318349124464,24491483560367872],
 [13567318349124464, 8245187686123360,10639816214971712],
 [24491483560367872,10639816214971712,27953147411818400]]

kappa = 26/25
fixed inner-box mu = 50/51
inner coordinate radius = 2^-16
stable singleton rows = 1007,3303
complete outward boundaries checked = 12.
```

All 18 root-side all-wall boxes `0..17`, including every exact face-wall route and the actual first adjacent wall `V2083`, lie in this one certified `S>=2` cell.

The weakest stored singleton boundary is

```text
row 1007 -> row 1042, directed wall 6112.
```

### Relative cell R1 — paired vertex-transfer neighbourhood

```text
C1 = 2^-56 *
[[45048473047577456,15317172888155046,21356362677351592],
 [15317172888155046,10502543916608118, 6435733861234656],
 [21356362677351592, 6435733861234656,16506577073742362]]

kappa = 27/25
fixed inner-box mu = 25/26
inner coordinate radius = 2^-11
stable singleton rows = 725,3547
complete outward boundaries checked = 11.
```

This single large box contains all three exact target-pair all-wall children `19,20,21`. Thus the whole isolated paired-wall transfer region is excluded by `S>=2`, not merely by three pointwise chamber labels.

Its weakest singleton boundary is

```text
row 3547 -> row 3512, directed wall 21145.
```

### Relative cell R2 — far-side endpoint neighbourhood

```text
C2 = 2^-56 *
[[47816454913415816,15844265365833882,20411999247596344],
 [15844265365833882,11182506428914504, 5169377067129493],
 [20411999247596344, 5169377067129493,13058632695597616]]

kappa = 53/50
fixed inner-box mu = 100/103
inner coordinate radius = 2^-14
stable singleton rows = 655,3617
complete outward boundaries checked = 14.
```

It contains exact all-wall cell `18` and proves `S>=2` throughout a substantially larger neighbourhood.

Its weakest singleton boundary is

```text
row 3617 -> row 3582, directed wall 21563.
```

### Exact inner-box validation

For each relative cell, all `32` vertices of its five-dimensional trace-one coordinate box satisfy both Löwner inequalities by exact rational Sylvester minors. Convexity then places the whole box inside the relative cell.

Every box also satisfies throughout:

- strict SPD positivity;
- every old compact-core spectral inequality;
- both eigenvalue ratios above the **global maxima** of the SQ52 direction-dependent overlays;
- exact nonmembership in all `279` earlier relative-condition balls, using `279` generalized-Rayleigh witness pairs per box.

The three new boxes therefore contribute

```text
37 complete singleton-boundary checks,
837 previous-ball nonmembership checks,
96 exact inner-box Löwner vertices,
22 contained all-wall child boxes.
```

The three inner boxes are pairwise disjoint in the five independent trace-one coordinates.

## 5. Strongest exact endpoint

The strongest endpoint retained for deterministic reconstruction is all-wall cell `18`:

```text
K_far = 2^-56 *
[[47816454913415816,15844265365833882,20411999247596344],
 [15844265365833882,11182506428914504, 5169377067129493],
 [20411999247596344, 5169377067129493,13058632695597616]].
```

Its full independent-coordinate box is

```text
|Delta(K00,K11,K01,K02,K12)| <= 2^-35,
K22=1-K00-K11.
```

Exact Sturm isolation and a rational Weyl enclosure prove strict trace-one SPD and all compact-core inequalities throughout the box. The complete wall audit has zero straddles and fixes

```text
(S,U,H)=(2,2,2),
stable rows        655,3617,
unstable vertices  1755,3337,
saddle edges       6266,6529.
```

The minimum absolute directed-wall interval separation is exactly stored in the ledger and is approximately

```text
7.91908916290427e-10.
```

This endpoint is not a Gömböc, but it is a literal exact own-centred homogeneous convex polyhedron with a certified perturbation box and a much larger surrounding `S>=2` relative-condition cell.

## 6. Deterministic H/V reconstruction and watertight mesh

Let

```text
A = K_far^(-1/2)
```

be the unique symmetric positive square root inverse. The exact transformed object is

```text
h_i^A = A^-T(q_i-a_*),

v_f^A = A y_f/(1-a_*^T y_f).
```

The generator rebuilds every exact baseline vertex from its actual active support triple, reconstructs all actual true edges, and exports deterministic midpoint H/V tables. The exact object is defined by the dyadic metric, the isolated algebraic Santaló root, these formulas, and the reconstructed incidence; the decimal OBJ/STL is a visualization of the midpoint representative.

The mesh verifier returns

```text
vertices                 8,644
boundary triangles      17,284
triangulated edges       25,926
triangle-edge incidence       2
true polyhedral edges    12,966.
```

The OBJ and binary STL are closed and watertight.

## 7. Discovery work not used as evidence

Discovery was deliberately broader than the final certificate:

```text
random trace-one core metrics tested       2,000,000
minimum sampled stable count                       2
minimum sampled unstable count                     2
sampled (S,U)=(2,2) metrics                    17,125
strict sampled winners                              0
local adjacency-beam states                       973
four-wall nonlinear systems                        64
actual SQ52-remainder samples                    3,072
actual-remainder numerical hits                  1,850.
```

Nonsmooth local optimization and wall-targeted solves also found no winner. None of these searches covers a continuum; none is used in any exclusion claim.

## 8. Exact new remainder and structural reason the present branch stops

Define

```text
R_SW49_2 = R_SW49 minus the three closed inner boxes
           listed in relative_condition_extension.json.
```

Their boundaries are also nonwinners because every box is contained in a complete `S>=2` relative-condition cell. The exact volume removed from the prior remainder is the fraction stated above.

`R_SW49_2` is **not** claimed empty, and its nonemptiness is not proved. The whole fixed-lattice core therefore remains unresolved.

The local obstruction is now explicit. The four nearest raw walls do not lead toward a four-feature cancellation:

- both face walls are count-neutral in the exact adjacent chambers;
- the paired vertex walls are opposite directions on one actual edge and exchange orientation without changing the class;
- all 22 explored chambers lie inside one of three independent two-stable-subset cells.

A continuation should not spend more boxes inside these regions. The next finite branch is to leave the three relative cells through their first exact singleton-boundary failures:

```text
wall 6112  (1007 -> 1042),
wall 21145 (3547 -> 3512),
wall 21563 (3617 -> 3582).
```

At each boundary, compute the first SCC merger exactly, construct a wall-aligned child, and then either:

1. renew a two-subset relative certificate on the far side;
2. certify a complete all-wall coordinate box;
3. or split at the first exact `S_ij=0` or `W_fg=0` straddle.

The other sharp finite task is the enumerated `2,164`-group connection between the ten-cell root prefix and the exact target-pair neighbourhood. It should be processed only outside R0, since every portion remaining in R0 already has `S>=2`.

## 9. Verification

From the extracted bundle, run

```bash
python verify_all.py
```

The clean default rerun reconstructs the actual wall system, verifies all atlas signatures, reruns the exact paired-wall adjacency proof, verifies all three relative cells and their `837` old-ball exclusions, and checks the H/V mesh. The recorded transcript ends in

```text
PASS
```

A separate fresh rerun of every one of the `22` complete all-wall cell ledgers is recorded in `FULL_CELL_VERIFY.json`; all 22 pass, with the same class histogram and zero winner cells.

Additional expensive reruns are available:

```bash
python verify_all.py --key-cells
python verify_all.py --full-cells
python verify_all.py --full-adjacency
```

`--full-cells` independently reevaluates all `51,864` directed walls and all `12,966` four-component edge cones for every one of the 22 all-wall boxes. `--full-adjacency` reruns every base exact central-segment certificate; the two paired-wall segments use the separate exact Bernstein verifier.

## 10. Artifact map

- Complete Markdown handoff (`RESULT.md`)
- Complete bundle (`Steady_Willow_49_four_wall_atlas.zip`)
- Bundle SHA-256 (`Steady_Willow_49_four_wall_atlas.zip.sha256`)
- Internal file manifest (`MANIFEST.sha256`)
- Global machine-readable certificate (`GLOBAL_CERTIFICATE.json`)
- Exact 22-cell all-wall atlas (`adjacent_metric_atlas.json`)
- Three-cell relative-condition extension (`relative_condition_extension.json`)
- Exact paired-wall transfer ledger (`target_pair_transfer_ledger.json`)
- Complete directed sign payload (`wall_signs.bin`)
- Default verifier (`verify_all.py`)
- Recorded verification transcript (`VERIFY_ALL.txt`)
- Fresh all-22-cell verification summary (`FULL_CELL_VERIFY.json`)
- Fresh all-22-cell verification transcript (`VERIFY_FULL_CELLS.txt`)
- Deterministic strongest-endpoint H table (`strongest_far_side_H.csv`)
- Deterministic strongest-endpoint V table (`strongest_far_side_V.csv`)
- Watertight OBJ (`strongest_far_side.obj`)
- Watertight STL (`strongest_far_side.stl`)

## Final disposition

The primary acceptance gate remains unmet: there is no certified finite own-centroid strict `(1,1,0)` polyhedron. Relative to the supplied journal, however, the four decision-nearest walls are no longer open questions. All four have exact adjacent children; the vertex pair is rigorously a transfer; every explored child is covered by a complete nonwinner certificate; and `R_SW49` is reduced by the exact positive volume above. The first unresolved continuation is now finite and explicit.
