# Actual-cell descent through five independent support events

All state rows use a fresh hull at `plane_tol=1e-11`; exact walls in the final tight cluster additionally use raw fresh-hull grouping at `1e-13`.

## Cumulative states

| state | lattice | LP δ | quad | U54 | H67 | H910 | topology | rails/inactive |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| post initial independent relay | (60, 158, 100) | 0.962399498 | 0.984430631 | 0.995249823 | 0.982918172 | 0.993778200 | 1.444e-09 | True / [73] |
| after three epoch-1 bypasses | (60, 158, 100) | 0.969355481 | 0.984235500 | 0.995053040 | 0.982498108 | 0.993551670 | 9.208e-09 | True / [73] |
| post {198,229,259,260} | (60, 158, 100) | 0.965182990 | 0.982339852 | 0.994221476 | 0.980645049 | 0.992778890 | 5.650e-09 | True / [73] |
| after epoch-3 reverse bypasses | (60, 158, 100) | 0.967877878 | 0.980656136 | 0.993833880 | 0.979366825 | 0.992382698 | 6.323e-09 | True / [73] |
| post five-independent-event cluster | (60, 158, 100) | 0.965949537 | 0.979893341 | 0.993044197 | 0.978217409 | 0.991593008 | 8.985e-09 | True / [73] |

## Exact event order

| epoch | type | circuit | local α | action | control rows/nullity |
|---:|---|---|---:|---|---|
| 1 | reverse | `{198,234,235,236}` | 3.54522372359773e-05 | nullspace bypass | [198, 234, 236] / 5 |
| 1 | reverse | `{69,228,235,255}` | 4.14942653266006e-05 | nullspace bypass | [69, 255] / 2 |
| 1 | independent #1 | `{224,228,251,252}` | 0.000140203987316866 | nullspace bypass | [251, 252] / 2 |
| 2 | independent #2 | `{198,229,259,260}` | 0.000768588409831786 | cross | — |
| 3 | reverse | `{69,228,235,255}` | 0.00017859447839548 | nullspace bypass | [69, 255] / 2 |
| 3 | reverse | `{198,234,235,236}` | 0.000268214368973476 | nullspace bypass | [198, 234, 236] / 5 |
| 4 | reverse | `{198,234,235,236}` | 0.000375552085440739 | nullspace bypass | [198, 234] / 2 |
| 4 | independent #3 | `{69,235,236,255}` | 0.000627524953843194 | cross | — |
| 4 | independent #4 | `{228,235,236,255}` | 0.000628411737345825 | cross | — |
| 4 | independent #5 | `{69,228,236,255}` | 0.000628902462253582 | cross | — |

The three final independent roots are strictly ordered inside a `1.38e-6` interval; fresh raw hulls show `(60,158,100) -> (60,157,99) -> (60,158,100)` at each root.

## Decision

All four fixed residual series are monotone, but the final worst ratio is `0.993044197` (U54), not below `0.9`. Thus the support relay mechanism is traversable but does **not** produce material four-defect descent on this scale. No mechanical-sign wall occurs; every accepted cell retains class `(2,2,2)`, base/U8, all forced rails, and only row 73 inactive.
