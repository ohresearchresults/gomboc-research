# Post-C17 recovery2 log

## Frozen handoff recovery

- Parent `manifest.sha256` passed all 18 entries unchanged.
- The monolithic parent verifier was not accepted after lifecycle exits without
  a terminal marker.  Its exact blocks were isolated and then rerun by the
  portable aggregate verifier.
- Accepted marker:
  `INDEPENDENT_EXACT_POST_C17_RECOVERY2_PORTABLE_PASS`.
- Verification artifact SHA-256:
  `60fda4965bc24435f82018697a3a7874fe7eb07fc0300d44b4c9c5193d8a0108`.
- Frozen endpoint remains a NONWINNER with
  `(V,E,F)=(61,150,91)` and own-centroid class `(2,4,4)`.

## Exact chart opening

- Directly loaded frozen `cells/endpoint.csv` and `cells/endpoint.json`; C5-C17
  was not replayed.
- The exact fixed-plane affine chart has 150 modes and preserves the 17-gon
  base and 16-gon shell identically.  All eight remaining death walls have
  exact rank 8; targets plus the 30 protected base/U8 components have rank 38.
- Chart marker: `EXACT_POST_C17_FIXED_PLANE_FULL_CHART_AUDIT_PASS`.

## Independently accepted safe-flip chain

Every round enumerates 12,363 primitives: 10,529 supports, 33 in-face turns,
300 face components, 300 vertex components, 900 edge components, 300 face
references and the volume primitive.  Each support wall has odd multiplicity
in both support rows and `beta1/beta2`, and even multiplicity two in `gram`.
All rational checkpoints use their own exact uniform-volume centroid; all 61
active rows, enlarged base, protected U8 and all 37 rails are retained.

1. Circuit `(0,16,54,72)`, diagonal `(0,72) -> (16,54)` at
   `t ~= 14.937712503820268`.
   - Builder: `EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS`.
   - Clean verifier: `INDEPENDENT_EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS`.
   - Certificate SHA-256:
     `953bc91a30f0860c443208d42164d19a00ca68aa6cfbdfd1f81087fd2d07e3ee`.
   - Verification SHA-256:
     `a0ee5d210281f1ce51ebe4c631312c56b547fb8bf3dd640253e9205fd0d0cfde`.

2. Circuit `(3,4,88,237)`, diagonal `(3,237) -> (4,88)` at
   `t ~= 11.374032228994446`.
   - Builder: `EXACT_POST_C17_SECOND_SAFE_FLIP_PASS`.
   - Clean verifier: `INDEPENDENT_EXACT_POST_C17_SECOND_SAFE_FLIP_PASS`.
   - Certificate SHA-256:
     `98035a4676d48a0eee813500a0ca8e19716ab53f0124e8c3d44ea266b29ee989`.
   - Verification SHA-256:
     `fe5f717c2cdb9f0fdc7b1160a0cc06e5a4da9eb1741ab15b1905f985e4f42cff`.

3. Circuit `(14,15,72,73)`, diagonal `(14,72) -> (15,73)` at
   `t ~= 4.896533968084259`.
   - Builder: `EXACT_POST_C17_THIRD_SAFE_FLIP_PASS`.
   - Clean verifier: `INDEPENDENT_EXACT_POST_C17_THIRD_SAFE_FLIP_PASS`.
   - Certificate SHA-256:
     `e7237b89281a3b1f161b33a4e774eb84aa04a034ec5d720a089a1456b4033d56`.
   - Verification SHA-256:
     `c765120e647dfb384d7e18f9abcfa88bd5f6e6052e9bec16d13b24b287528ea7`.

4. Circuit `(11,12,262,263)`, diagonal `(11,262) -> (12,263)` at
   `t ~= 78.61319941351637`.
   - Builder: `EXACT_POST_C17_FOURTH_SAFE_FLIP_PASS`.
   - Clean verifier: `INDEPENDENT_EXACT_POST_C17_FOURTH_SAFE_FLIP_PASS`.
   - Certificate SHA-256:
     `c1225d2a1cbc5a8a4fc7ec0cc9978b1894e869ea1f996d892aee9425d7bee8d1`.
   - Verification SHA-256:
     `feb064d828c1c5dabb40313db5d6a1a551c3924036f24d84f9e8bfce7653ac42`.
   - The far checkpoint is `t=100`, strictly before the linked face/edge birth
     found near `t=112.46` on the old ray.

All four flips preserve class `(2,4,4)` and strictly improve all eight selected
residuals.  They are material adjacent-cell progress, not a winner or a class
reduction.  The active attack continues from the fourth far checkpoint with a
fresh chart.
