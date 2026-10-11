# Carrier stage 18--21 report

## Exact stage-18 transfer

The saved affine line has two distinct degree-five cleared centroid
numerators.  Their exact rational isolating intervals give

- `N11 = 0` at `0.00022381466204310162`: birth of `U10` and `H(10,11)`;
- `N9 = 0` at `0.00022383646336155587`: death of `H(9,10)` and `U10`.

The root gap is `2.1801318454250154e-8`.  Directed samples have classes
`222 -> 233 -> 222`, unchanged `(V,E,F)=(61,162,103)`, the enlarged base,
`U8`, and every one of the 37 named rails.

## FAR versus PRE-null route

The actual FAR cell is valid, but its best guarded H67 continuation reaches
the loss of vertex 250 and rails `(249,250)`, `(250,251)` after only a
`5.2594%` H67 reduction.

The PRE cell is much stronger.  Blocking the `U10/H(10,11)` birth while
allowing the tiny `H(9,10)` carrier to stay below `0.000303636`, then taking a
same-cell nullspace detour around circuit `(9,10,11,263)`, gives

- `H(6,7): 0.0271264880834 -> 0.000604670424337` (`97.7709%` reduction);
- `H(9,10) = 5.82465004395e-6`;
- `H(10,11) = -1.63775693705e-5`;
- `S(7,8,245) = 0.000944967709565`;
- `U54 = 0.00456120006542`.

Every sampled detour point has all 61 vertices, the enlarged base, `U8`, all
37 rails, the inherited linked-birth guards, and the protected topology
circuits.

## Exact vertex-6 transfer

The residual H67 wall is another two-root carrier transfer:

- `N5 = 0` at `0.007092765190310719`: birth of `U6` and `H(5,6)`;
- `N7 = 0` at `0.008405420930909631`: death of `H(6,7)` and `U6`.

The exact directed classes are again `222 -> 233 -> 222`; the root gap is
`0.0013126557405989119`.  In the FAR cell,

- `H(6,7) = -0.000302469639458` (dead);
- `H(5,6) = 0.00148063809350` (the transported carrier);
- `U6 = -0.00419632960000`;
- `S(7,8,245) = 0.000944059110903`;
- `U54 = 0.00455053398390`.

The hull remains `(61,162,103)`, class `222`, with base, `U8`, and all 37
rails.  A provisional H56-focused continuation reduces H56 by `27.2%`, but
it is not yet globally preferred because it lets H910 grow; its first
topological blocker is circuit `(7,8,245,246)`.  The certified handoff is the
stage-21 FAR cell, not that provisional continuation.

## Reproduction

Run:

```bash
python tracks/global_carrier_support/verify_stage21_vertex6_transfer.py
python tracks/global_carrier_support/verify_carrier_stage18_to_stage21.py
```

The literal success lines are
`EXACT_DIRECTED_STAGE21_VERTEX6_CARRIER_TRANSFER_PASS` and
`CARRIER_STAGE18_TO_STAGE21_BRANCH_AND_EXACT_TRANSFER_PASS`.
