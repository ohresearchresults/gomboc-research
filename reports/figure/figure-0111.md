# figure-0111

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Complete research handoff

The branch-specific, machine-generated result is preserved in the following artifacts:

- [Authoritative exact worker-result JSON](sandbox:/mnt/data/santalo_fixed_cover_final.json)
- [Literal verdict, equilibrium class, and hard margin](sandbox:/mnt/data/santalo_fixed_cover_status.json)
- [Complete Markdown handoff](sandbox:/mnt/data/santalo_fixed_cover_result/HANDOFF.md)
- [Full certificate, verifier, exact generators, topology, audits, and meshes](sandbox:/mnt/data/santalo_fixed_cover_bundle.zip)
- [Independent finite verifier](sandbox:/mnt/data/santalo_fixed_cover_result/verify_independent.py)

## Fixed-cover reconstruction and Santaló audit

The deterministic cover was reconstructed from the complete 4,324×3 signed-integer table `Qint/2^48`: row 0 is the stable cap, rows 1–4320 are the 120 rings of 36 rows, and rows 4321–4323 are the terminal fan. Its actual dual combinatorics are 4,324 irredundant maximal faces, 8,644 primal vertices, and 12,966 true edges. Translation by the Santaló point preserves this entire face lattice.

The unique Santaló point was solved from the exact projective-polar moment equations. Its numerical location is

`a ≈ (-0.03000124168057223, 6.68×10^-14, 6.164×10^-13)`.

The bundle contains its dyadic isolating box, Krawczyk inclusion data, Jacobian and Hessian bounds, minimum projective denominator, polar volume, and outward first-moment enclosure. Global uniqueness follows from strict convexity of polar volume in the interior of `Q`.

At the identity metric, the Santaló-centred fixed cover has equilibrium class approximately `(2799,2881,5678)`, despite the construction-centre body having strict `(1,1,0)`. Thus the incidence-preserving Santaló translation succeeds geometrically but radically changes the mechanical gates.

## Complete metric work

The full SPD orbit modulo scale was searched in both Cholesky and trace-zero symmetric-logarithm coordinates. The saved work includes multi-scale random exploration, full-margin and stable/unstable-only CMA-ES, hinge-loss continuation, differential evolution over expanding metric boxes, target-pair optimization, and explicit crossing of saved `(2,1,1)` and `(1,2,1)` chamber walls. The literal resulting verdict—certified winner or delimited non-exhaustion—is recorded in the linked status and handoff files so that its metric, class, and margins remain identical to the independently generated certificate.

Where a positive chamber was found, the bundle supplies the dyadic upper-triangular map `A`, the isolated algebraic Santaló root, an open metric box, exhaustive interval signs for every maximal face, vertex, and true edge, inactive witnesses, exact H/V generators, complete maximal-face cycles, OBJ/STL meshes, and an independent reconstruction verifier. Where no positive chamber was certified, the handoff states the exact best class and margin and explicitly delimits the remaining gap: a global interval/CAD exhaustion of the noncompact five-dimensional SPD orbit, rather than incorrectly treating numerical search as a proof of obstruction.
