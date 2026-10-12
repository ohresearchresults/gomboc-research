# NH72 opposite-point mass compensation gate

Native assignment `asg_ousVKm3QLVe7jHESNGmiuItK`, result event1365 at2026-09-15T17:59:21.541Z. This is an analytical result and method, not a new Gömböc construction. The response's C624 benchmark is stale; C622 is already accepted and locally verified elsewhere.

Fix the previously preserved C592 body and the old C602 filled centroid c0. The author proves that adding one point in the specified opposite-side box, with the augmented body's actual centroid in a specified exact rho-cube around c0, leaves at least two strict unstable equilibria: the old apex and the farther added point. Visibility changes and the new point's degree are not frozen. This does not exclude moved old geometry, another metric, another centroid region or a different cap/chain.

The same source supplies actual filled-volume and first-moment formulas within a fixed visible-facet chamber: volume is affine in the new point and first moment quadratic. A mass-equation solution alone is not a proof of own110.

`opposite_mass_gate.py` is the complete5120-byte literal method from the immutable result. It was syntax-checked and read back, and both dependency packages were hash-verified. The monitor did not execute the final method or prove its mathematical claims. The author explicitly did not claim observing a completed replay of this final unit. All proof text and exact constants remain in `native-result.md`.

Inputs are complete C592 and C602 A records, reproducible using the already preserved sixteen-file core plus six-file C592 extension:

```sh
python -B -S ../figure-c592-exposed-chain-20260915/source/REPLAY_C592.py ../figure-four-frontiers-core-20260915/source NEW_C592_PROOF
python -B -S opposite_mass_gate.py NEW_C592_PROOF/A.json NEW_C592_PROOF/PARENT_A.json NEW_GATE_REPORT.json
```

The trial point is (874577931702,454209162144,-558471315966)/10^12, not the previously added C592 chain point. Its resulting body, an exact moment root and any unbound118/243 or other intermediate counts are not certified successors by this package. Their missing source-parameter-audit binding remains explicit.
