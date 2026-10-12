# Post-relay class-reduction front

## Ordered transfer 1 — accepted

- Source: parent `far_u1.csv`, SHA-256 `9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77`.
- Exact event: complete zero family `edge:(1,54):one_minus_t == vertex:54:1` only; root near original `lambda = 0.009851128366103941`.
- Ordering: all other 7,920 primitives are Bernstein-strict over the entire epoch.
- Class: `(2,2,2) -> (2,3,3)`; endpoint retains 61 active rows, `(V,E,F)=(61,162,103)`, all 37 rails, strict row230, and no H910/U10 resurrection.
- Rational FAR: `transfer1_far.csv`, SHA-256 `1e77e096ea1285457aa4427ecc1772a82289dbcabb6a0d186651d98cc4471191`.
- Primary certificate: `transfer1_certificate.json`, SHA-256 `2fb33c49221ee09146ccfe5db0f060757ab61ef6d2bbe7d7ebb5ea2d13f66f7f`.
- Accepted clean-room verification: `transfer1_verification.json`, SHA-256 `62480d82f3bc428616a81f65f194e2eded2c1d0e8b377447c47853d0e489839b`.
- Stdlib-only verifier: `verify_transfer1.py`, SHA-256 `0a35f6f1196bdae360b556c3b915479bfffdd2608670c843cd5b3a51c14996c0`.
- Clean-room verdict: `INDEPENDENT_CLEAN_ROOM_EXACT_ORDERED_TRANSFER1_D_VERIFICATION_PASS`.
- `transfer1_shared_owner_crosscheck.json` is explicitly non-independent and is not acceptance authority.

## Ordered transfer 2 — primary-only, paused

- Source is strictly the accepted `transfer1_far.csv` above.
- Fresh rechart: `transfer2_rechart_audit.json`, SHA-256 `f3769aa2fae7501ba8c83cc11042c3af4c487e693e8d1a7e4294cec799ab6632`; verdict `EXACT_TRANSFER2_FRESH_165D_RECHART_H910_FIRST_JET_PASS`.
- Exact event: complete zero family `edge:(9,10):one_minus_t == vertex:10:9` only; local root near `0.026309174389703725`.
- Primary ordering: all other 7,920 primitives are Bernstein-strict over the entire epoch.
- Exact class: `(2,3,3) -> (2,4,4)`; H910 and U10 are born together.
- Rational FAR: `transfer2_far.csv`, SHA-256 `3e15e92981bf9437e76578feeec3d5b512505a11017878b0c453fd5ed104c253`.
- Primary certificate: `transfer2_certificate.json`, SHA-256 `2a3690164a6dd950d4b06372035da3ef85d5527b0cebad2d9645608be369afdd`; verdict `EXACT_ORDERED_TRANSFER2_H910_EPOCH_PASS`.
- The stdlib-only verifier `verify_transfer2.py` was safely interrupted during its independent 7,922-row recomputation. No `transfer2_verification.json` exists.
- Transfer2 is **not accepted or promoted**. Accepted boundary remains transfer1.
- U1/H1011 target-wall work is gated on accepted primary plus clean-room transfer2 verification.
