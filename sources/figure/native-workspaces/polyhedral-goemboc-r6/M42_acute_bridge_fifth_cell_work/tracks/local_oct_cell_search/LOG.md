# Local octahedron / row54 track log

## 2026-08-31 — baseline restoration

- Ran `RUN_COMBINED_QUICK.sh` in the restored M42 fifth-cell bundle.
- Exact generator, exhaustive supporting-triple reconstruction, class,
  centroid, rails, cell closure, robustness box, OBJ/STL and all combined
  verifiers passed.
- Stored the complete 81-line transcript in `baseline_verifier.log`.

## 2026-08-31 — six-row core

- Identified the exact octahedral core and opposite pairs
  `(198,247)`, `(224,228)`, `(258,229)`.
- Audited the baseline with both fixed facets and a fresh hull.
- Built independent finite-difference controls for stable-foot death,
  saddle-beta death and relay overlap.
- Located the naive common direction's first actual boundary flip at
  `t=0.003954448137390238`; the intended mechanics were still far from zero.
- Built the complete 12,444-inequality target/guard LP and extracted a
  normalized Farkas vector.
- Reduced the obstruction to beta1 death plus 162 fixed anti-edge witnesses;
  stored the 18-term certificate in `guarded.json`.
- Ran fresh-hull three-mode, core-active, relay-supremum and pure-beta searches.
  Relay overlap was achieved, but stable/saddle transfer remained; beta death
  outside the protected chamber produced class `(2,4,4)`.

## 2026-08-31 — rail-valid row54 carrier

- Loaded the independently rebuilt `row54_far_rebuilt` atlas cell and verified
  its `(61,162,103)`, `(2,2,2)` baseline.
- Defined a 13-DOF coplanarity-preserving local chart and four independent
  target actuators; coupled the two saddle actuators into the requested shared
  three-dimensional basis.
- Evaluated 6,301 support/base/U8/structural-rail/anti-birth guards.
- Extracted full-13D and shared-3D numerical Farkas certificates.
- Located and freshly rebuilt the two earliest shared-H flips at
  `1.19607444e-6` and `3.32384e-6`.
- Ran a first 1,409-evaluation shared-3D global/local search and materialized an
  all-active rail-valid endpoint where original `S` and `U54` die but transfer
  to `[245,8,246]` and `U1`; both saddles persist.
- Ran three independent 3,388-evaluation deep searches.  All converged to the
  same `(2,2,2)` transfer pocket and none produced a supporting cell.
- Added `verify_local_oct_cell_search.py`; fresh endpoint/face reconstruction,
  transfers, rail edges, Farkas residuals and both flips all pass.

## Scope boundary

The baseline certificate is exact.  The local obstruction certificates use
central finite differences and floating-point LP duals; they are numerical
certificates for the stored charts.  The flip and endpoint claims are actual
fresh convex-hull reconstructions.  No claim of exact or global impossibility
outside these local/shared coordinate families is made.

