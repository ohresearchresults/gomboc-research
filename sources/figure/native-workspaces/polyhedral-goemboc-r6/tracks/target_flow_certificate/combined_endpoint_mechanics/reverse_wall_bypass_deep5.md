# Two-dimensional bypass of the relay-4 reverse wall

The main axis is the post-relay-3 bound-300 four-death direction. The transverse axis uses only rows 69 and 255 and lies in the four-death Jacobian nullspace.

- Local rank/nullity: `4/2`.
- Reverse-gradient nullspace projection: `0.000313316759567`.
- Maximum fractional death-rate leakage from y: `6.617e-24`.
- Independent-circuit volume change from y: `0.000e+00`.

## Four fresh quadrant cells

| quadrant (x,y) | lattice | reverse volume | reverse diagonal | valid |
|---:|---:|---:|---|---:|
| (-1, -1) | (60, 158, 100) | 4.036297e-12 | `[69, 228, 235]` + `[69, 228, 255]` | True |
| (-1, 1) | (60, 158, 100) | -6.659885e-12 | `[69, 235, 255]` + `[228, 235, 255]` | True |
| (1, -1) | (60, 158, 100) | 6.710761e-12 | `[69, 228, 235]` + `[69, 228, 255]` | True |
| (1, 1) | (60, 158, 100) | -3.986088e-12 | `[69, 235, 255]` + `[228, 235, 255]` | True |

The two diagonals occupy opposite half-planes in this 2D atlas. The L-path uses positive y, so it passes the scalar reverse-root location while retaining faces `[69,235,255] + [228,235,255]`.

## Fresh-hull L-path and independent event

| waypoint | lattice | topology margin | reverse volume | independent volume | quad | U54 | H67 | H910 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| start | (60, 158, 100) | 1.919e-09 | -1.311797e-12 | -2.047819e-12 | 0.984449668 | 0.995269196 | 0.982937523 | 0.993797771 |
| lifted | (60, 158, 100) | 6.260e-09 | -6.659885e-12 | -2.047819e-12 | 0.984449668 | 0.995269196 | 0.982937523 | 0.993797771 |
| crossed | (60, 158, 100) | 2.080e-09 | -3.986088e-12 | -6.805265e-13 | 0.984440019 | 0.995259379 | 0.982927720 | 0.993787857 |
| before_independent | (60, 158, 100) | 2.223e-10 | -2.790764e-12 | -7.272848e-14 | 0.984435930 | 0.995255217 | 0.982923562 | 0.993783651 |
| at_independent | (60, 157, 99) | 3.874e-09 | -2.647479e-12 | 0.000000e+00 | 0.984435448 | 0.995254726 | 0.982923072 | 0.993783156 |
| after_independent | (60, 158, 100) | 1.444e-09 | -1.186841e-12 | 7.399292e-13 | 0.984430631 | 0.995249823 | 0.982918172 | 0.993778200 |

The next independent circuit `{198,234,235,236}` is reached at main-axis `alpha=0.000170644947243409`. Its root shifts by only `2.310e-14` because the y control moves none of its vertices. At the wall the lattice is `(60,157,99)`; immediately after it returns to `(60,158,100)` with the new diagonal `[198,234,236] + [234,235,236]`.

All sampled path points retain the enlarged base, U8, every forced rail, class `(2,2,2)`, and inactive set `{73}`. The exact cubic segment audits find no reverse-circuit root on any L-path segment. Therefore the observed reverse flip is an **avoidable codimension-one wall, not a genuine limit cycle**.
