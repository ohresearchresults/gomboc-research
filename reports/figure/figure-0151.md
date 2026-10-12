# figure-0151

AI research report · 2026-08-29 UTC

---

# Steady Willow 49 — exact first-exit atlas beyond R0/R1/R2

## Literal verdict

**No homogeneous convex polyhedral Gömböc was found.** The required acceptance gate remains a materialized uniform-density finite polyhedron at its own exact volume centroid with strict `(1,1,0)`, complete H/V/incidence and full-normal-cone audit, an independent verifier, and matching OBJ/STL. No trace-one SPD metric box with strict own-centroid `(S,U,H)=(1,1,0)` was reached, and the entire bounded five-dimensional core is not covered. Global fixed-lattice nonexistence is therefore **not** proved.

The previous durable frontier required exact children at walls `6112`, `21145`, and `21563`, while forbidding further refinement inside the already certified cells R0/R1/R2. This continuation resolves all three requested exits and strictly reduces the unresolved core.

## Exact delta

For every requested wall, the bundle now contains:

- two full-dimensional dyadic trace-one SPD boxes of radius `2^-70`, one on each side;
- an exact one-wall corridor proving that the named face wall crosses once and all other `51,863` directed walls retain sign;
- a complete interval audit of all `25,932` face walls, `25,932` vertex walls, and all `12,966` actual four-component true-edge cones on both boxes;
- a far-side merged-subset relative-condition cell proving `S>=2` on a substantially larger region;
- a closed inner trace-one box lying wholly in the previous unresolved remainder and outside all `282` prior relative-condition cells/balls.

The three pairwise-disjoint inner boxes have exact total five-coordinate volume

```text
1057/1208925819614629174706176
≈ 8.7432990746855025e-22.
```

This is an exact positive-volume witness for strict shrinkage. It is not claimed to be the full volume of the three semialgebraic relative cells.

## Exact body and bounded metric core

The immutable source is

```text
q_i = Qint_i / 2^48,  i=0,...,4323,
a_* in a_c + [-2^-90,2^-90]^3,
P_*=(conv{q_i}-a_*)^circ.
```

The isolated Santaló root makes the uniform-volume centroid of `P_*` exactly zero. Hence every invertible linear image remains exactly own-centred. The clean reconstruction gives

```text
(H,V,E)=(4324,8644,12966).
```

Modulo rotation and scale, the inverse metric is

```text
K=[[k00,k01,k02],
   [k01,k11,k12],
   [k02,k12,1-k00-k11]],
trace(K)=1, K∈SPD(3).
```

Every new box is certified throughout the old compact-core inequalities

```text
17179/16384 < λ1/λ3 < 2048/19,
λ2/λ1 > 1/32,
λ3/λ2 > 19/64,
λ3 > 19/4115,
```

above its exact direction-dependent stable and unstable collar thresholds, and outside the parent 23-ball tube, the 256 SQ52 cells, and R0/R1/R2.

## Complete mechanical wall basis

For adjacent support rows `i,j` and adjacent primal vertices `f,g`,

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j),
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g,
d_f=1-a_*^T y_f.
```

A true edge with incident faces `(i,j)` and endpoints `(f,g)` is a saddle only when all four actual components are positive:

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

The independent structure verifier reconstructs both adjacency graphs, every maximal-face cycle, every actual true edge and every edge-cone component from the exact source; it does not infer equilibria from feature representatives.

## Three exact first-exit transitions

| crossed wall | near class | far class | removed saddle | far-side sink subsets | certified κ | first renewed certificate failure |
|---|---:|---:|---:|---|---:|---|
| `6112` `1007→1042` | `[3, 2, 3]` | `[2, 2, 2]` | `3056` | `[1007, 1042]` + `[3267]` | `261/256` | `19672` (`3267→3302`, κ≈1.02163323809699) |
| `21145` `3547→3512` | `[3, 2, 3]` | `[2, 2, 2]` | `10572` | `[3547, 3512]` + `[760]` | `263/256` | `4421` (`760→725`, κ≈1.02847398992469) |
| `21563` `3617→3582` | `[3, 2, 3]` | `[2, 2, 2]` | `10781` | `[3617, 3582]` + `[689]` | `269/256` | `21559` (`3617→3581`, κ≈1.05328949312428) |

All three crossings are genuine `S-H` cancellations:

1. `6112: 1007→1042` removes stable row `1007` and saddle edge `3056`, but row `1042` was already stable. The count changes `(3,2,3)→(2,2,2)`.
2. `21145: 3547→3512` removes stable row `3547` and saddle edge `10572`, but row `3512` was already stable. Again `(3,2,3)→(2,2,2)`.
3. `21563: 3617→3582` removes stable row `3617` and saddle edge `10781`, but row `3582` was already stable. Again `(3,2,3)→(2,2,2)`.

Thus none reaches stable count one. Each formerly singleton proof is repaired exactly by absorbing the crossed pair into a two-row sink subset and retaining a second disjoint singleton subset.

### Wall isolation

The centre-to-centre corridors are exact dyadic segments. Their target parameter intervals over the entire Santaló box have widths

```text
wall 6112:  374720105913046377988130785727093807717791646653705633140296920200324688092355378137026707519963136/2157289035461533520481818403346179248943524773906381792055728524490351303703747213347438943999009209999089738786223633647  ≈ 1.7370e-22
wall 21145: 731966784297218238619894358650571775165250438105718458009725570895588736800976172945679485402873856/1178347922138555042574651745598008161346684125622418248143900565257134957877016050208379319139380867034234345284423133033  ≈ 6.2118e-22
wall 21563: 90784726475730747411332095970531590164916273441080460136994527458869015566230557749921774621949952/192626543183889962416401368352704439984766274534222787425224129437118017124731281132058352703260082722586500008150883961  ≈ 4.7130e-22.
```

No non-target wall requires subdivision: all `51,863` retain strict Bernstein sign on each complete segment.

## Renewed exact `S>=2` cells

For a trace-one dyadic centre `C` and rational `κ>1`, define

```text
B(C,κ)={K∈SPD(3), trace(K)=1:
        ∃μ>0 with μC≤K≤κμC}.
```

For an outward stable boundary, with `c=b^T C d`, `p=b^T C b`, `q=d^T C d`, the verifier proves over the complete Santaló box

```text
(1+κ)^2 c_lower^2-(κ-1)^2 p_upper q > 0.
```

The exact renewed cells are:

```text
Rexit_6112: κ=261/256, subsets {1007,1042} and {3267}, inner radius 2^-16
Rexit_21145: κ=263/256, subsets {3547,3512} and {760}, inner radius 2^-15
Rexit_21563: κ=269/256, subsets {3617,3582} and {689}, inner radius 2^-17.
```

All complete outward boundary lists are regenerated from the actual face graph. Every one of the 96 inner-box vertices satisfies both Löwner inequalities by exact rational Sylvester minors.

The exact new remainder is

```text
R_new = R_previous \ (Rexit_6112 ∪ Rexit_21145 ∪ Rexit_21563).
```

The three inner boxes prove this subtraction removes positive volume from `R_previous`; no unstated sampling assumption enters the claim.

## Strongest exact endpoint

The strongest far-side all-wall box is `W6112_far`, centred at

```text
K = 2^-56 *
[[37023033371544568, 16555496236033318, 29541738462459940],
 [16555496236033318, 10208116365533504, 13673008311374914],
 [29541738462459940, 13673008311374914, 24826444300849864]].
```

Its full independent-coordinate box has radius `2^-70`. Throughout it,

```text
(S,U,H)=(2,2,2),
stable rows        1042,3267,
unstable vertices  1047,6643,
saddle edges       5431,7691.
```

The minimum absolute directed-wall interval separation is

```text
16619195452138594253477352940659728035462862441097820307200880242733440638040410170692082548026983985509649978003376315238286688799132510224354437/13480963481671763929534903129934578327116970175771207113987894026489666106980522160245509117471917266446403151102880536137195898909073712889538127255830528
≈ 1.2327898873647614e-09.
```

This is a literal homogeneous exactly own-centred nonwinner with positive perturbation radius.

## Discovery beyond the certificate

Discovery tested `1,766,105` random/hyperplane metrics and adjacency beams with at least `180`, `183`, and `38` states on the three branches. The minimum sampled stable count was two; no sampled strict winner occurred. These computations selected the exact cells but are **not** used as coverage evidence.

The next exact finite branch is wall `19672 (3267→3302)`. It is the smallest renewed certificate failure and, unlike wall `21559`, attacks the *other* disjoint singleton subset. Wall `4421 (760→725)` is the second-priority analogue. Reaching either as an actual chamber facet may require promotion of some of the already enumerated intervening wall groups; only regions outside the complete renewed cells are relevant.

## Deterministic H/V object and watertight mesh

For the strongest endpoint let `A=K^(-1/2)`, the unique SPD algebraic square root. The exact transformed object is

```text
h_i^A=A^(-T)(q_i-a_*),
v_f^A=A y_f/(1-a_*^T y_f).
```

The deterministic exporter rebuilds all `8,644` exact baseline vertices from their active triples and the complete actual incidence before writing midpoint tables and mesh files. The mesh audit gives

```text
H rows / maximal faces   4,324
vertices                  8,644
true polyhedral edges    12,966
boundary triangles       17,284
triangulated edges       25,926
triangle-edge incidence       2
watertight                    yes.
```

The OBJ/STL are decimal midpoint visualizations; the exact object is specified by the dyadic metric, isolated Santaló root, algebraic transform formula and rebuilt incidence.

## Independent verification

Run from the extracted directory:

```bash
python verify_all.py
```

The completed full rerun independently checked six all-wall boxes, three one-wall corridors, the three renewed relative cells, all old-union nonmembership witnesses, the exact source incidence, and the deterministic mesh. Its transcript ends in

```text
PASS
```

with synthesis

```json
{"verified":true,"full_all_wall_boxes":6,"exact_one_wall_corridors":3,
 "renewed_relative_cells":3,
 "new_inner_box_volume":"1057/1208925819614629174706176",
 "strongest_endpoint":"W6112_far"}
```

## Artifact map

- `GLOBAL_CERTIFICATE.json` — compact machine-readable synthesis.
- `first_exit_atlas.json` — complete six-cell, three-corridor and three-relative-cell ledger.
- `cell_W*_near.json`, `cell_W*_far.json` — full exact metric/root-box and all-wall audits.
- `corridor_W*.json` — exact one-wall isolations.
- `relative_exit_*.json` — complete merged-subset and inner-box certificates.
- `verify_structure_cleanroom.py` — independent actual-incidence reconstruction.
- `verify_cell_exact.py`, `verify_corridor_exact.py`, `verify_relative_exit.py` — exact component verifiers.
- `verify_all.py` — clean rerun entry point.
- `FULL_VERIFICATION.txt` — completed full transcript.
- `rebuild_strongest_endpoint.py` — deterministic H/V and mesh exporter.
- `strongest_endpoint_H.csv`, `strongest_endpoint_V.csv`, `strongest_endpoint.obj`, `strongest_endpoint.stl` — strongest accepted nonwinner export.

## Final disposition

The three requested exits are no longer unresolved. Each is an exact S-H cancellation, but each transfers stability to an already stable neighbor and ends in `(2,2,2)`. The merged-subset repair produces three larger machine-checkable `S>=2` cells and a strict positive-volume reduction of the previous remainder. The first genuinely relevant successor is now the exact boundary `19672`, followed by `4421`; the global Gömböc acceptance gate remains unmet.

## Downloadable artifacts

- Complete self-contained bundle (`Steady_Willow_49_first_exit_atlas.zip`)
- Bundle SHA-256 (`Steady_Willow_49_first_exit_atlas.zip.sha256`)
- Complete Markdown handoff (`RESULT.md`)
- Global machine-readable certificate (`GLOBAL_CERTIFICATE.json`)
- Complete first-exit atlas (`first_exit_atlas.json`)
- Unified independent verifier (`verify_all.py`)
- Completed full verification transcript (`FULL_VERIFICATION.txt`)
- Manifest (`MANIFEST.sha256`)
- Strongest endpoint H table (`strongest_endpoint_H.csv`)
- Strongest endpoint V table (`strongest_endpoint_V.csv`)
- Watertight OBJ (`strongest_endpoint.obj`)
- Watertight STL (`strongest_endpoint.stl`)

Bundle SHA-256:

```text
7c73a4ae3195fa13948e1f7d98a67144ab8a89f692aec70fa98f6a03e15793e6
```
