# Bound-300 exact support-relay chain

Every state is audited by rebuilding the full hull. Ratios use the fixed branches quad, U54, H67=`1-t`, H910=`t` and are relative to the original combined wall.

| state | fresh lattice | LP δ | quad | U54 | H67 | H910 | topo margin | exact entering circuit @ local α | inactive |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| combined wall | (61, 161, 102) | 0.968550799 | 1.000000000 | 1.000000000 | 1.000000000 | 1.000000000 | 1.042e-07 | — | — |
| interiorized pre-q73 | (61, 161, 102) | 0.968858005 | 0.997617266 | 0.998815932 | 0.994263235 | 0.997838551 | 7.020e-08 | — | — |
| post-q73 | (60, 158, 100) | 0.958845143 | 0.992562966 | 0.997000048 | 0.988025705 | 0.996153796 | 1.035e-08 | `{14,72,73,261}` @ 0.00149629034692 | 73 |
| post-relay-1 | (60, 158, 100) | 0.969260545 | 0.990110578 | 0.996711542 | 0.987729843 | 0.995729300 | 2.944e-08 | `{198,228,258,259}` @ 0.000249670732152 | 73 |
| post-relay-2 | (60, 158, 100) | 0.959431502 | 0.986150875 | 0.995714554 | 0.983384986 | 0.994706366 | 1.903e-08 | `{198,228,229,259}` @ 0.000693318567742 | 73 |
| post-relay-3 | (60, 158, 100) | 0.962611515 | 0.984601719 | 0.995423435 | 0.983090574 | 0.993952541 | 1.122e-08 | `{69,228,235,255}` @ 0.000263000347991 | 73 |
| post-relay-4 (fifth exact support event) | (60, 158, 100) | 0.962611515* | 0.984442913 | 0.995262323 | 0.982930661 | 0.993790831 | 7.546e-10 | `{69,228,235,255}` @ 0.000160902819704 | 73 |

`*` The fifth-event row inherits the certified direction from the preceding actual cell; no post-event LP rebuild is needed to establish the stopping criterion.

Result: **five consecutive exact support events**, all forced rails retained, class `(2,2,2)` retained, only row 73 inactive after the deliberate q73 support exit, and every one of the four fixed residual series is monotone nonincreasing. No mechanical-sign wall is encountered. The next exact event is independently bracketed as `{198,234,235,236}` at local `α=0.0001706449472203067`.
