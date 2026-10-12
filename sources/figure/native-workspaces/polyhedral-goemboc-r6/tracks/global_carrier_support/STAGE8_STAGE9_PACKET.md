# Stage 8–9 exact carrier packet

Verdict: both encountered walls are real and exactly localized, but neither is an obstruction.  Fresh-hull L-bypasses remain in the class `(2,2,2)` carrier cell, preserve the enlarged base, unstable vertex 8, all 61 active labels, and all 37 forced rails, while all four unwanted decisions decrease.

## Stage 8: linked own-centroid birth

- Common event: `S(8,245,246)` and `H(8,245)` share the cleared own-centroid numerator in `dot(cross(p245-p8, M-4*V*p8), cross(p245-p8, p246-p8))`.
- Exact dyadic polynomial degree: **6**; root `0.00059455957822758369`; rational isolation width `1.616e-31`.
- Independently conditioned roots differ by only `1.626e-14`; exact common-numerator signs are negative/positive on the directed samples.
- Fresh directed transition: `(2,2,2) -> (3,2,3)`, adding only face `(8,245,246)` and edge `(8,245)`, with unchanged hull.
- Four-quadrant audit: two `(3,2,3)` and two `(2,2,2)` cells.  The 23D keep Jacobian has rank 4/nullity 19; anti-birth projection norm `0.116649835`.
- L-bypass: 121 fresh path samples; all stay `(2,2,2)`, all hard constraints and six inherited circuit signs hold, and all four keep decisions decrease.

## Stage 9: protected rail wall

- Exact circuit: `(224,228,251,252)`, valid side `det < 0` (sign `-1`).
- Exact dyadic determinant polynomial degree: **1**; root `0.0029937197003675172`; rational isolation width `1.578e-34`.
- Scalar crossing replaces faces `(224,251,252),(228,251,252)` and rail `(251,252)` by faces `(224,228,251),(224,228,252)` and edge `(224,228)`.  Thus the post-side violates the forced rail.
- The 23D L-bypass has 81 fresh path samples, retains rail `(251,252)` and all other hard invariants, stays `(2,2,2)`, and keeps the linked stage-8 birth absent.
- H(9,10) needed an explicit nullspace repair: its raw wall-direction derivative was `0.000297278524`; the minimum-norm repair imposed `-0.000891835572`, yielding repair derivative `-0.000891835572` and a net decrease on the L-path.

## Fresh sample ledger

| Block | Fresh samples | Result |
|---|---:|---|
| Stage-8 directed exact sides | 2 | `(2,2,2)` / `(3,2,3)`, all hard |
| Stage-8 quadrants | 4 | 2 cells per side, all hard |
| Stage-8 bypass | 121 | all `(2,2,2)`, all hard |
| Stage-9 adaptive trace | 53 | all `(2,2,2)`, all hard |
| Stage-9 directed wall atlas | 9 | exact sign/topology ledger; rail lost only at/on post-side |
| Stage-9 bypass | 81 | all `(2,2,2)`, all hard |

## Cumulative packet reduction

| Decision | Initial | Stage-9 bypass endpoint | Reduction |
|---|---:|---:|---:|
| S(7,8,245) | 0.0094863188901 | 0.00131078991395 | 86.182312% |
| U54 | 0.0496252260557 | 0.00701252581829 | 85.869030% |
| H(6,7) | 0.283075235925 | 0.0400013312008 | 85.869011% |
| H(9,10) | 0.00278246245035 | 0.000384045796892 | 86.197629% |

Reproduce the complete exact/fresh audit with:

```bash
python tracks/global_carrier_support/verify_stage8_stage9_packet.py
```

Machine-readable details, including exact rational brackets and primitive integer coefficients, are in `stage8_stage9_ledger.json`.
