# Stage-31 H1011 sparse/full-control continuation log

## 2026-08-31 — exact post-cell source accepted

- Source: `../../exact_circuit_far.csv` with `../../exact_circuit_post_faces.json`.
- Parent independent verifier rerun: `INDEPENDENT_EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS`.
- Exact/fresh-hull state: 61 active rows, `(V,E,F)=(61,162,103)`, own-centroid class `(S,U,H)=(2,2,2)`, enlarged base present, all 37 rails present.
- Residual block: `S(7,8,245)>0`, `U54>0`, `H(5,6)>0`, `H(10,11)>0`; old carrier `H(9,10)<0` remains the closest forbidden equilibrium.
- Next material gate: a first real support/mechanics event on a chart that jointly decreases the four positive residuals while certifying `H(9,10)<0` throughout.

## 2026-08-31 — rejected forced H1011-death assumption

- A 165-mode full-control LP ray was rationalized with the enlarged base kept in its exact plane.
- The numerical ray did not survive exact event reconstruction as a local H1011 death: the exact degree-5 `edge:(10,11):t` polynomial has positive derivative at the source and no positive root in `(0,1)`; its positive floating root candidates are approximately `3.9871`, `5.4004`, and `21.4261`.
- Therefore no H1011-death certificate was emitted. The next attack must enumerate the first zero of the complete support/mechanics ledger instead of prescribing the event type.

## 2026-08-31 — guarded full-control chain independently accepted

- Integrated the separate guarded 165-mode actual-cell path and reconstructed it without importing its builder.
- The exact chain contains three class-preserving algebraic transfers at approximately `0.6304878300386273`, `0.6306469498254694`, and `0.6307902358341029`, followed by the support flip `(228,230) -> (229,231)` at approximately `1.8448744265342492`.
- Both pre- and post-cell ledgers contain 7,904 exact primitives. The body remains `(61,162,103)` and `(2,2,2)`, with its own exact uniform-volume centroid, 61 active rows, enlarged base, protected `U8`, all 37 rails, and a strict negative `H(9,10)` witness.
- Exact far decisions are `S=0.00010977891260888583`, `U54=0.0014687707610462019`, `H56=0.0011975249033894472`, and `H1011=4.49741035468303e-7`; all four are strictly improved but this is still a nonwinner.
- Independent command verdict: `INDEPENDENT_INTEGRATED_EXACT_FULL_CONTROL_CHAIN_PASS`.
- Frozen chain certificate SHA-256: `5cedb116b124cafb7346ca9110bd40ad01c5b10f15fb46cf4d219930850b8117`.

## 2026-08-31 — strict post-flip horizon-4 checkpoint

- The next guarded ray is exact and event-free on the full interval `t in [0,4]`: all 7,904 primitives have one strict Bernstein leaf, with minimum coefficient log10 magnitude `-39.841125754721816`.
- The first genuine event is later, at `t≈4.519179427877758`, where a common row-230 degeneracy hits three incident edge cones and three support rows. Crossing it is forbidden because all 61 active rows must survive.
- At the exact `t=4` checkpoint the body is still `(V,E,F)=(61,162,103)` and `(S,U,H)=(2,2,2)`, with own exact centroid, base, `U8`, all 37 rails and `H(9,10)<0`.
- Exact decisions improve again to `S=0.00010977820681371887`, `U54=0.0014687613378774832`, `H56=0.0011975172060876475`, `H1011=4.4971825138918166e-7`.
- Verdicts: `EXACT_POST_SAFE_FLIP_HORIZON4_CHECKPOINT_PASS` and `INDEPENDENT_EXACT_POST_SAFE_FLIP_HORIZON4_CHECKPOINT_PASS`.
