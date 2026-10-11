# Shared local-octahedron and row54 circuit search

## Verdict

No supporting shared three-control cell was found that simultaneously removes
the unwanted stable foot, unstable vertex and both saddle edges while
preserving the base, `U8`, all forced rail edges and the global hull.

The strongest result is a reproducible two-part obstruction:

1. On the original six-row core, even the linearized death of the limiting
   saddle component is incompatible with a fixed anti-edge witness system.
2. In the rail-valid row54 carrier, both the full natural 13-dimensional local
   chart and its requested shared three-dimensional restriction have numerical
   Farkas certificates.  Along the shared saddle actuator, two actual rebuilt
   hull flips occur at coefficients of order `1e-6`, whereas the two saddle
   deaths require coefficients `0.0979855` and `0.398828`.

Fresh-hull endpoints show the nonlinear mechanism: features transfer to a
neighboring carrier rather than disappear.  This is a numerical/local
obstruction and a concrete first-wall result, not an exact global
impossibility theorem for arbitrary motions outside the tested charts.

## Exact baseline restoration

`RUN_COMBINED_QUICK.sh` was rerun from the restored bundle.  The final line is:

```text
ALL COMBINED M42 FIFTH-CELL VERIFIERS PASS
```

The exact fifth endpoint has f-vector `(61,163,104)`, class `(2,1,1)`, stable
faces `base` and `[198,224,258]`, unstable vertex `8`, saddle edge
`(229,247)`, and both exact 19-edge rails.  The complete verifier transcript is
in `baseline_verifier.log`.

The six core rows form the combinatorial octahedron

```text
{198,224,258,229,247,228}
```

with opposite pairs `(198,247)`, `(224,228)`, `(258,229)`.

| Baseline quantity | Value |
|---|---:|
| limiting stable-foot component | `0.6819299931297` |
| saddle beta1 / beta2 | `2.213931236540` / `2.396177853680` |
| relay inward minimum | `-0.0301595352341` |
| base margin | `0.8846185087647` |
| U8 margin | `0.1716177489956` |
| class | `(2,1,1)` |

The relay centroid misses only the two core facets `[198,228,229]` and
`[198,228,258]`, with slacks `-0.0301595352341` and `-0.00525173203357`.

## Original core: octahedral local search

Three independent local objectives were used: death of the limiting component
of `S[198,224,258]`, death of the limiting beta component of `H(229,247)`, and
strict inclusion of the centroid in the six-row octahedron.  Base, `U8`, both
directed rails, every support slack and fixed anti-birth witnesses were guarded.

The target Jacobian has singular values
`(13.4455252, 3.40503235, 0.663601018)`.  A naive common improving direction
hits its first clean wall at

```text
t = 0.003954448137390238
```

when row `230` enters the plane `[224,229,247]`.  The actual boundary flip is

```text
[224,229,247] + [224,230,229]
       ->
[224,230,247] + [229,247,230].
```

At that wall the stable margin is still `0.677926`, the saddle decision is
`0.496047`, and relay overlap is still negative (`-0.0287281`).  Thus the
first event is a surface diagonal flip, not the desired shared volumetric
`2<->3`/`3<->2` carrier event.

The fully guarded finite-difference LP contains 10 target inequalities and
12,434 guards and is infeasible.  Its normalized Farkas vector satisfies

```text
b.y = -0.2272225328525601
||A^T y||_inf = 2.4492e-14.
```

A much smaller obstruction uses only beta1 death and 162 fixed anti-edge
witnesses.  It has 163 inequalities and certificate

```text
b.y = -0.20225608520388316
||A^T y||_inf = 2.8015e-15.
```

Its main weights are beta1 death `0.68784418`, anti-edge `228-247:c3`
`0.20686844`, `228-248:c3` `0.03495571`, `229-230:c0` `0.03224698`,
`247-248:c0` `0.03065173`, and `228-229:c2` `0.00657124`.  This certificate
does not need the topology, base, `U8` or rail constraints: at first order the
saddle death already forces a saddle transfer among the anti-edge witnesses.

Two fresh-hull controls separate carrier feasibility from mechanics:

- Relay overlap itself is achievable.  The relay-supremum endpoint has strict
  overlap `+0.02420750418`, all six core rows active, positive base/`U8`/rail
  guards and class `(2,1,1)`.  However, the stable face transfers to
  `[197,224,259]` with margin `1.29948` and `H(229,247)` persists with margin
  `0.432522`.
- The pure beta actuator first makes the original limiting beta negative at
  coefficient `6.5`.  Relay overlap is then `+0.0317710`, but the base and
  directed rails have failed and the rebuilt class is `(2,4,4)`: new stable,
  unstable and saddle features replace the target pair.

## Rail-valid row54 embedding

### Local chart

The source is `tracks/circuit_atlas/row54_far_rebuilt.csv`, a freshly rebuilt
rail-valid `(61,162,103)` hull of class `(2,2,2)`:

```text
S = base, [7,8,246]
U = 8, 54
H = (6,7), (9,10).
```

The natural local chart has 13 degrees of freedom: `q246` moves freely in
three dimensions and rows `54,6,7,9,10` move independently within the base
plane.  This preserves base coplanarity.  Four minimum-norm actuators were
constructed for deaths of `S[7,8,246]`, `U54`, `H67`, and `H910`.  The target
Jacobian has rank four and singular values

```text
36.7384260052, 0.8150197285, 0.2238581621, 0.0430944651.
```

The requested shared three-dimensional basis consists of the independent
`S` actuator, the independent `U54` actuator and the sum of the two saddle
actuators.  Its target response is, to rounding,

```text
S-column      = (1,0,0,0)
U-column      = (0,1,0,0)
shared-H      = (0,0,1,1).
```

All 6,301 fixed-chamber guards were included: every support-plane slack,
base/`U8`, structural preservation of all forced rail edges, and one fixed
anti-birth witness for every other stable/unstable/saddle candidate.  In this
atlas, "rail-valid" means the forced edges exist; inherited directed dot signs
are intentionally not imposed because the robust projective/SPD rebuild does
not preserve all of them.

### Numerical LP obstructions

| System | Variables | Result | `b.y` | `||A^T y||inf` |
|---|---:|---|---:|---:|
| full natural chart | 13 | infeasible | `-0.0379569764850` | `4.77e-16` |
| shared basis | 3 | infeasible | `-0.389841027170` | `7.76e-17` |

The 13-dimensional certificate already closes using target deaths `S`, `U54`
and `H67` plus four topology walls and small anti-edge terms; `H910` is not
needed.  The shared three-dimensional certificate is especially sparse:

| Inequality | Weight |
|---|---:|
| `U54-death` | `1.59037e-5` |
| `H67-death` | `0.98347367` |
| topology: face `[245,7,246]`, row `8` | `0.01648424` |
| anti-edge `263-264:c3` | `2.61877e-5` |

These are central finite-difference certificates (`h=1e-7`) checked by
HiGHS.  The residuals above certify the stored numerical matrices, not exact
rational inequalities.

### Actual first walls of the shared-H actuator

Fresh maximal-face reconstruction on both sides gives:

| Shared-H coefficient | Actual flip |
|---:|---|
| `1.19607444e-6` | `[5,244,245] + [5,6,245] -> [5,6,244] + [6,244,245]` |
| `3.32384e-6` | `[7,245,246] + [7,8,246] -> [7,8,245] + [8,245,246]` |

The second flip is the decisive `q246` carrier transfer: the original stable
triangle is replaced by `[245,8,246]`.  By comparison, the linearized zero
times are `0.0979855253` for `H910` and `0.3988279121` for `H67`, more than
four orders of magnitude beyond the first carrier walls.

### Rebuilt-hull endpoints

The primary endpoint artifact was chosen to exhibit target death and transfer,
not merely the best scalar minimax value.  It has coefficients

```text
(-0.2331712496551, 0.6366716632906, 0.0192195894771)
```

and independently rebuilds as:

| Property | Result |
|---|---|
| f-vector / active rows | `(61,162,103)` / all 61 |
| class | `(2,2,2)` |
| forced rails | all present |
| base / U8 margins | `1.5403809564` / `0.9961197451` |
| stable features | `base`, `[245,8,246]` |
| unstable vertices | `8`, `1` |
| saddle edges | `(6,7)`, `(9,10)` |

Thus the original `S[7,8,246]` and `U54` really are absent, but they have
transferred to `S[245,8,246]` and `U1`; both target saddles persist.  The fresh
audit is `endpoint_audit.json`; coordinates and maximal faces are
`row54_shared3d_endpoint.csv` and `row54_shared3d_endpoint_faces.json`.

Three deeper deterministic searches (`maxiter=90`, 3,388 evaluations each)
with seeds `54246247`, `83154247`, and `19824654` converged to the same
rail-valid `(2,2,2)` pocket.  Their best scores were respectively
`-0.3895470181`, `-0.3895498598`, and `-0.3895494601`, with shared-H
coefficients near `0.02225`.  Each has the transferred stable triangle
`[245,8,246]` while `U54`, `H67`, and `H910` remain.  No run found a joint
supporting cell.

## Reproduction

Run from `M42_acute_bridge_fifth_cell_work`:

```bash
bash RUN_COMBINED_QUICK.sh

python tracks/local_oct_cell_search/local_oct_cell_search.py \
  --mode baseline --output tracks/local_oct_cell_search/baseline.json
python tracks/local_oct_cell_search/local_oct_cell_search.py \
  --mode linear --output tracks/local_oct_cell_search/linear.json
python tracks/local_oct_cell_search/local_oct_cell_search.py \
  --mode guarded --output tracks/local_oct_cell_search/guarded.json
python tracks/local_oct_cell_search/local_oct_cell_search.py \
  --mode relay --output tracks/local_oct_cell_search/relay_supremum.json
python tracks/local_oct_cell_search/local_oct_cell_search.py \
  --mode scan --output tracks/local_oct_cell_search/pure_beta_scan.json

python tracks/local_oct_cell_search/row54_shared3d_embedding.py \
  --mode search --seed 54246247 --maxiter 35 \
  --output tracks/local_oct_cell_search/row54_shared3d_result.json \
  --endpoint-csv tracks/local_oct_cell_search/row54_shared3d_endpoint.csv \
  --endpoint-faces tracks/local_oct_cell_search/row54_shared3d_endpoint_faces.json

python tracks/local_oct_cell_search/verify_local_oct_cell_search.py \
  --output tracks/local_oct_cell_search/endpoint_audit.json
```

The verifier performs a coordinate round trip, rebuilds maximal faces from the
CSV, checks all rows, class, feature transfers, base/`U8`, forced rail edges,
both Farkas residuals, and reconstructs both first flips from points on their
two sides.  Its current result is `PASS`.

