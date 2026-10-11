# LOG

## 2026-09-01T02:26:09Z — exact source and pair diagnosis

- Bound `far_u1.csv` (`9f6c8438…ed77`) to the accepted death certificate
  (`f799513e…0996`) and independent death verification (`86b1fb7f…ed03`).
- Rebuilt the hull from the CSV rather than consuming a saved face ledger:
  103 maximal faces, 162 true edges, 61 active rows, Euler value 2, fresh face
  digest `dcf2f45a…82e0`.
- Rebuilt mechanics `(2,2,2)` with stable faces enlarged-base and
  `(7,8,245)`, unstable vertices `1,8`, and saddle edges `(5,6),(10,11)`.
- Audited all four stable+saddle pairings.  Exactly two are incident, both on
  the enlarged base.  Corrected the initial exploratory owner convention:
  when base is incidence face 0, the shared owner is `beta2`, not `beta1`.
  Both corrected face/beta identities vanish exactly.
- Computed a 165-mode exact first-jet chart and ordered all 7,922 primitive
  rows for each min-norm shared-owner ray.  Before the target wall there are
  336 rows for `(5,6)` and 312 for `(10,11)`.  These are bounded ray failures,
  not a global impossibility result.
- Selected the common first topology candidate `(8,245)`: it is an edge of the
  extra stable face `(7,8,245)` and can potentially transfer that stable
  carrier under a certified flip/rechart.  No event is claimed yet.

Reproduction:

```sh
env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 \
  tracks/global_carrier_support/stage31_h1011_attack/u54_u1_segmented_relay_attack/stable_first_topology_front/diagnose_stable_pairs.py
```

Result: `stable_pair_diagnosis.json`, SHA-256
`891374ef74011e364bcb2cb0b1fe64814904f8517b6d6b7bb932f024f7e53e4f`.

## 2026-09-01T03:41:45Z — exact first stable-carrier transfer

- Followed the selected `(10,11)` diagnostic ray only to its true first wall.
  Isolated the irreducible circuit `{7,8,245,246}` at
  `t≈0.002546739185167658` in an exact bracket of width below `10^-30`.
- Rebuilt all 7,922 old-ledger primitives.  The complete zero family has five
  rows: the two adjacent support slacks, edge `(8,245)` `beta1`, `beta2`, and
  `gram` (circuit multiplicity two).  All other 7,917 rows are Bernstein-strict.
- Recharted diagonal `(8,245)->(7,246)`.  The stable face transfers from
  `(7,8,245)` to `(7,8,246)` while class remains `(2,2,2)`.
- Rejected the initially tested FAR `t=3/1000`: a second circuit
  `{8,9,263,264}` changes `(8,263)->(9,264)` before it.  Chose the ordered FAR
  `t=13/5000`; its ledger equals the post ledger.
- Proved all 7,922 post-ledger primitives strict from just after the algebraic
  root through `13/5000`.  Pre/post/FAR all preserve 61 active rows,
  `f=(61,162,103)`, Euler 2, 37 rails, strict row230 margins, dead `H(9,10)`,
  and the enlarged stable base.
- Primary certificate PASS:
  `flip_8245_certificate.json`, SHA-256
  `d1d4cc70538432eb0cc6cdf943dfb47c0bab3988699ec734049654ff744b3cf3`.
- Replaced a contaminated verifier draft before execution.  The final
  self-contained verifier imports neither `front_common`, locator, nor builder;
  it independently reproduced hulls, factor multiplicities, complete strict
  audits, checkpoints and hash bindings.
- Independent verification PASS:
  `flip_8245_verification.json`, SHA-256
  `cc0b288d8f2e2c9d624596e2ceb4e208a82a068e17770b6722fa0efb5b24b072`.

This is a proved carrier transfer, not yet the requested class reduction.  The
next epoch starts only from `flip_8245_far.csv` and must first cross the known
`{8,9,263,264}` circuit before separately locating the observed
`(10,11)->(9,10)` saddle transfer.
