# figure-0096

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Result: exact post-three-lobe fallback, no Gömböc

## Literal verdict

No strict homogeneous polyhedral Gömböc was found. The strongest endpoint is a finite, exactly own-centred, open polyhedron with exhaustive class `(S,U,H)=(2,2,2)`, so it must not be reported as a winner. The journal's gate requires the body's own ordinary volume centroid and strict `(1,1,0)`, with complete maximal-face, vertex/full-normal-cone, and true-edge audits; auxiliary-centre and wall states are excluded.

The inherited MA300 state and the exact 36-row critical one-ring are the durable starting obstruction. Because the MA300 worker archive was unavailable, I rebuilt a clean-room equivalent frontier from the journal's exact P9-derived outer support data rather than claiming access to missing bytes.

## What was actually constructed

I did not append another rail. I built an exact-dyadic old frontier in which all 36 inherited one-ring rows are extreme, then ran one coupled old/new support homotopy:

```text
q_old(t) = (1-0.95 t) q_old
q_new(t) = (0.05+0.95 t) q_new
0 <= t <= 1
```

with seven outer rows fixed. At `t=0`, all 36 old rows and no new rows are extreme. At `t=1`, all 36 old rows are redundant and exactly 36 new annulus rows are extreme. The Q-hull path contains 168 reconstructed circuit/topology events; 167 are four-row events and event 152 is a simultaneous seven-row cluster at `t∈[0.9227369369714950,0.9227369369714951]` on rows `9,N0_03,N0_04,N1_03,N1_04,N1_06,N2_02`. After every crossing the tracer rebuilds Q, the polar P, ordinary uniform centroid, projective own-centering, maximal faces, true edges, and full vertex/edge cones. Circuit surfaces necessarily have zero combinatorial gap; the final gate state is strictly separated.

The complete deterministic path is materialized in circuit_path.json, circuit_path.csv, and the standalone circuit tracer (`trace_three_lobe_circuits.py`).

## New communicating support complex

The surviving new complex has three radial-ascent paths:

```text
A, 12 edges:
9-N0_01-N0_02-N0_03-N0_04-N1_07-N1_08-N1_09-N1_10-N0_06-N0_14-N0_15-26

B, 13 edges:
9-N1_03-N1_04-N1_05-N1_06-N2_09-N2_10-N1_11-N1_12-N1_13-N0_14-N1_14-N1_15-27

C, 12 edges:
100-N2_01-N2_02-N2_03-N2_04-N2_09-N2_10-N2_11-N2_12-N2_13-N2_14-N2_15-27
```

and two genuine transverse Q-graph cycles:

```text
lower: N0_02-N1_05-N2_08-N2_09-N1_06-N0_03-N0_02
upper: N0_14-N1_11-N2_10-N2_11-N1_13-N0_14
```

Their own-centred face-pyramid first moments are

```text
M_lower=(-1.5094757883353348e-4,-6.76790626240684e-4,-6.634295903807369e-3)
M_upper=( 5.6142820449500030e-3, 2.6785481209455595e-2,-5.545706070873549e-2)
```

so the horizontal components oppose. Together with the three branch sectors and retained outer sector, the total exact first moment is zero after projective elimination. No separate antipodal counter-cap is used.

Topological deviation from the ideal assignment is explicit: A and B share root `9`; B and C share terminal `27`; C starts at `100`, while A ends at `26`. Thus this is a connected three-lobe communicating annulus, but not a perfect common-root/common-terminal theta graph. That mismatch is part of the remaining obstruction.

## Exact finite generator and centering identity

All supplied coordinates are exact IEEE-754 dyadics interpreted by

```python
Fraction.from_float(float.fromhex(token))
```

The standalone exact generator/verifier (`three_lobe_generator.py`) embeds every old and final row; it needs no worker-local archive. It enumerates all `C(52,3)=22100` candidate triple intersections exactly, reconstructs the irredundant polar, integrates exact uniform volume and first moments, audits all features by exact rational signs, and exports H/V tables and meshes.

For raw support points, define

```text
T_u(q)=q/(1-q·u).
```

Exactly,

```text
(T_u Q_raw)^circ = P_raw-u.
```

If `c` is the exact ordinary volume centroid of `P_raw`, then

```text
F(u)=centroid((T_u Q_raw)^circ)=c-u,
DF=-I_3,
u*=c.
```

Thus the three centring variables are eliminated symbolically before mechanical scoring, not repaired after scoring. The unique exact root has decimal enclosure

```text
u*=(-0.025367332651498722,-0.080965485471001866,0.16998022570963792)
min_i(1-q_i·u*)=0.8860170201468278
volume(P_raw)=0.36059968903661122
centroid((T_u*Q_raw)^circ)=(0,0,0) exactly.
```

The full exact rational strings are in exact_scalars.txt, with hashes:

```text
volume 578a48bd99dd52b4de0711cf95f8490cc532f4e2a93a2bfff97654b1ea32b0ed
cx     e1fb9555c8be9290459c9dd1ab039f5f4466d7b129ff0ea4d8be24fb524ff5dc
cy     a213f43690df1fc57a6e5eafcfb73fa5ccb08230e8c3fc894870867a6a6076ea
cz     00fd69e054c71f642b95f537ad7462603b19f4498e3e0929ea2d46980c479d62
```

## Boundedness and origin interiority

Rows `9,26,27,100` give an exact positive-span certificate. Their weights are

```text
649847058284150208484420818207867276196846931152/5852900428444668056604392066350668068854346479057
1832094442577707007011421389341281311797617455924/5852900428444668056604392066350668068854346479057
696169018701964479093175717027900100862410760768/5852900428444668056604392066350668068854346479057
2674789908880846362015374141773619379997471331213/5852900428444668056604392066350668068854346479057
```

They are strictly positive, sum exactly to one, and their weighted Q-row sum is exactly zero. The minimum origin-to-Q-facet distance is `0.16834239823412475`, proving strict origin interiority and bounded polarity.

## Exact endpoint data

```text
P (V,E,F,C)                 = (82,123,43,246)
all P vertices simple       = yes, exact active triples
active final Q rows         = 43
active new annulus rows     = 36
redundant construction rows = 9
old one-ring rows active    = 0
ordinary own centroid       = exactly (0,0,0)
full class                   = (2,2,2)
```

Active rows:

```text
9 26 27 32 100 102 103 N0_01 N0_02 N0_03 N0_04 N0_05 N0_06 N0_14 N0_15 N1_03 N1_04 N1_05 N1_06 N1_07 N1_08 N1_09 N1_10 N1_11 N1_12 N1_13 N1_14 N1_15 N2_01 N2_02 N2_03 N2_04 N2_05 N2_06 N2_07 N2_08 N2_09 N2_10 N2_11 N2_12 N2_13 N2_14 N2_15
```

Redundant temporary rows:

```text
N0_07 N0_08 N0_09 N0_10 N0_11 N0_12 N0_13 N1_01 N1_02
```

Every exact raw row is listed in final_input_rows.tsv; every clean-room old-frontier row is in old_frontier_rows.tsv. The generator embeds both tables directly. Exact irredundant H data and exact P vertices are in final_centered_Q_exact.tsv and final_P_vertices_exact.tsv. All 43 maximal-face cycles and all 123 true edges are explicitly enumerated in maximal_face_cycles.txt and true_edges.txt.

## Exhaustive own-centroid mechanics

Stable maximal faces:

```text
row 27     margin 0.013120875677323233
row N1_07  margin 0.0007553666812949627
```

Unstable vertices/full normal cones:

```text
(9,100,103)           margin 0.0014919018891017546
(N1_14,N1_15,N2_15)  margin 0.2180497225694636
```

Saddle true edges/full two-normal cones:

```text
(26,N0_15)  margin 0.0013831799951013774
(27,N2_12)  margin 0.0008767499794112008
```

Closest strict exclusions:

```text
face N1_08          -0.00018068261324469766
vertex (9,32,103)   -0.003354652245742263
edge (N2_12,N2_13) -0.000283018687367838
edge (26,N0_06)    -0.00032438715504019334
```

The complete exact sign record for every face, every full vertex cone, and every true edge is exact_signs.txt, SHA-256 `0be2e080646f212649535fbf5bfaefa656d42910cc73ae0296643de0436cec16`.

## Inactive separations

```text
P unit inequality slack       2.0791784853868567e-4
P Euclidean inactive gap      1.7906486116527577e-5
Q Euclidean inactive gap      1.1477170604868953e-4
Q origin-interior facet gap   1.6834239823412475e-1
```

Both final Euclidean P and Q gaps exceed `1e-5`.

## Certified open perturbation region

The independent clean-room interval verifier (`verify_three_lobe_interval.py`) reads only the final TSV and does not import the generator. It certifies independent perturbations

```text
|Delta q_ij| <= 2^-40
```

for every coordinate of every irredundant raw row. Exact determinant bounds preserve the oriented matroid and origin cell; interval arithmetic reconstructs all P vertices, volume, centroid, projective denominators, maximal faces, full vertex cones, and full edge cones. The box gives

```text
raw centroid x [-0.02536742230812093,-0.025367242994949312]
raw centroid y [-0.08096587379834538,-0.08096509714397317]
raw centroid z [ 0.16997955295090775, 0.16998089846891298]
raw volume     [ 0.36059954328875315, 0.36059983478446916]
minimum interval inactive unit slack 2.3682718823424528e-4
minimum 4-point determinant/bound ratio 5208.096106629981
minimum origin-triple ratio 48630.63881528079
```

For every body in this box, projective own-centering is exact and the full class remains `(2,2,2)`. The report is interval_verifier_report.json.

## Matching finite meshes

The OBJ (`three_lobe_fallback.obj`) and STL (`three_lobe_fallback.stl`) use the same 82 vertices and 160 face-fan triangles. The triangulated mesh has 240 unique edges, zero boundary edges, zero nonmanifold edges, and Euler characteristic two.

```text
OBJ SHA-256 72c1b300d9f90faa1c0e9175a3357d53a5f784764607832771408e71234edff9
STL SHA-256 1926180e383f3a0efbdc8f6483799490ea3b88f144c9a0348a7d5ba72777c8ce
```

## Sharp remaining obstruction

The old one-ring is completely gone. The residual defect consists of two Euler-neutral relays inside the new complex:

```text
S-H relay:
  extra stable N1_07
  saddle (27,N2_12)
  nearest transfer walls:
    N1_08=-1.8068261324469766e-4
    (N2_12,N2_13)=-2.83018687367838e-4

U-H relay:
  extra unstable (9,100,103)
  saddle (26,N0_15)
  nearest transfer walls:
    (9,32,103)=-3.354652245742263e-3
    (26,N0_06)=-3.2438715504019334e-4
```

A finite-difference Jacobian of those four unwanted signs plus the retained stable and unstable margins has rank six, with singular values

```text
75.4058790794, 0.611770898666, 0.183091896956,
0.102652784927, 0.0658000327170, 0.00425926181066.
```

Thus rank is not the obstruction. A nominal full linear reversal requires `||Delta q||_infinity=0.2393129683492846` and `||Delta q||_2=0.5892341524018461`; after rebuilding the exact hull only 22 new supports remain active and saddle `(27,N2_12)` is still positive. At half correction the class has already changed to `(3,2,3)` and only 28 new supports survive. This is a scale/circuit-transfer obstruction after a genuine complete replacement, rather than the old two-sheet MA300 seam. The reproducible diagnostic is analyze_mechanical_obstruction.py with mechanical_obstruction.json.

## Most useful continuation

Another serial rail or local flip is redundant. The smallest nonexcluded continuation is one nonlocal four-block event that simultaneously deactivates or replaces the complete stars of

```text
N1_07,27,N2_12,N2_13,
9,32,100,103,
26,N0_06,N0_15
```

and inserts a third transverse return band coupling the lower-left and upper-right sectors. The exact elimination `u=c` should remain hard before scoring; 34–38 active new supports and both P/Q Euclidean gaps above `1e-5` should remain gate constraints. The present endpoint and its certified box sharply delimit the two transfer walls this event must cross together.

## Reproducibility bundle

Complete archive (`three_lobe_annulus_result.zip`) · README (`README.md`) · SHA256SUMS (`SHA256SUMS.txt`)

Archive SHA-256:

```text
2d2dbbb69f629d7a2c0c80510b0d257035a442fc253e3937f904d89df482b4d7
```

This is a complete reproducible negative endpoint: simultaneous deletion succeeded, 36 new supports survive as a strict connected three-lobe complex, exact own-centering and full all-feature audits succeed, but two stable/unstable-saddle relays remain, so no `(1,1,0)` body emerged.
