# Global carrier-support result

## Exact supporting shell

The lost local preconditioning was reconstructed from the exact M42 fifth
endpoint as a new, independently checkable global object.  Only row `228` is
changed.  Let `p` be its orthogonal projection to the supporting plane of
`[224,229,247]`.  Write the projection of `p` to edge `(229,247)` using the
normalized two edge barycentrics as `q`.  The replacement is

```text
w = -(1/100) x_224 + (101/100) q
x'_228 = w - (1/100) (x_228 - p).
```

All operations are rational and are materialized in `shell63_exact.csv`.
Exact support and topology reconstruction gives

```text
(V,E,F) = (63,169,108),  Euler = 2.
```

The two additional active labels are the dormant predecessor rows `226,227`.
They form a finite supporting shell around the moved carrier rather than an
infinitesimal or local-only event.

After exact ordinary-volume centring, the exhaustive strict class is

```text
(S,U,H) = (2,1,1)
S = base [0..16], [198,224,258]
U = 8
H = (228,229).
```

Thus the global shell deletes the old saddle `(229,247)` and does **not** pay
the usual compensating `U228` plus second saddle.  It transfers the sole
remaining saddle to `(228,229)` while retaining the extra stable face.  The
smallest absolute raw exact mechanics component is approximately
`1.7546310112574e-3`; this is a strict chamber, not a boundary rounding.

Relative to the fifth sphere, 18 maximal faces are removed and 22 are added.
The four-face excess is exactly consistent with adding two vertices and six
edges.  Every stored face is checked against all 119 input rows with exact
determinants, every true edge belongs to two maximal faces, and the exact
volume centroid is recomputed before the mechanics audit.

Run:

```bash
python build_shell63_exact.py
python verify_shell63_exact.py
```

## Concrete obstructions

`audit_direct_wall_template.py` proves with exact determinant ratios that all
eight one-row orthogonal routes to the two natural circuit walls are pre-empted
by an unrelated hull circuit.  The earliest target parameters range from
`2.9057e-4` to `3.7825e-2`, while the intended wall is at parameter `1`.
Therefore fixed-other-row direct flattening is impossible; finite tangential
preconditioning is genuinely necessary.

On the exact 63-vertex shell, the two natural stable-edge actuators were then
continued through the actual convex hull and its own centroid.  The scans
`scan_shell63_258.json` and `scan_shell63_241.json` contain 600 full
evaluations.  Neither produces `(1,1,0)`.  Before the stable wall, rail
vertices become unstable together with matching saddle edges: for row `258`
the clean `(2,1,1)` interval ends near `t=0.1`, and for row `241` it ends near
`t=0.01`, versus the intended stable coplanarity at `t=1`.  This excludes the
explicit shell-plus-one-stable-actuator template, not coordinated multi-row
preconditioning.
