# figure-0038

Historical AI scientific report · saved 2026-08-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Verifier-gated circumscribed polyhedral Gömböc result

The complete branch-specific research result is serialized in the [canonical worker payload](sandbox:/mnt/data/worker_final_payload.json). The corresponding [canonical machine status](sandbox:/mnt/data/polyhedral_gomboc_final.json) records whether an exact rational witness passed the independent verification gate; when no candidate passes, it instead identifies the quantitatively strongest reproducible circumscribed near-witness.

## Work performed

The attached smooth-seed transcript was mined for the explicit centered spectral-phase construction with `beta=1/60` and mixed phase `sin(2t)/50+cos(4t)/100`. Several independent deterministic pipelines then constructed circumscribed halfspace families using rationally adapted normal fans, including a dedicated stable-minimum support plane and a three-plane cap around the unstable maximum. Ordinary inscribed triangulation was not used as the construction method.

Candidates were first audited numerically at their own uniform-volume centroids. Rationalization was attempted only after obtaining strict numerical predicate margins. Each rationalized candidate was rebuilt from its integer halfspaces, with exact vertices, active-plane incidences, ordered face cycles, edges, volume, and centroid reconstructed using rational arithmetic. Stable-face, unstable-vertex, and edge-equilibrium predicates were then evaluated over the complete lattice.

Promotion to an exact result required a fresh independent verifier run reporting `verified=true`, `S=1`, `U=1`, and `H=0`. The verifier also checks all H/V incidences, exact halfspace feasibility, face boundaries, two-face edge incidence, Euler characteristic, the exact tetrahedral volume and centroid calculation, and every strict equilibrium predicate. No numerically plausible but independently unverified candidate is labeled an exact witness.

## Reusable artifacts

- [Complete artifact bundle](sandbox:/mnt/data/polyhedral_gomboc_bundle.zip)
- [Canonical worker result](sandbox:/mnt/data/worker_final_payload.json)
- [Canonical verifier-gated status](sandbox:/mnt/data/polyhedral_gomboc_final.json)
- [Research report](sandbox:/mnt/data/polyhedral_gomboc_artifact/REPORT.md)
- [Artifact manifest with SHA-256 hashes](sandbox:/mnt/data/polyhedral_gomboc_artifact/MANIFEST.json)

The bundle contains the deterministic generators, rationalizers, exact verifier implementations, search records, predicate audits, and—when promoted—the complete rational certificate together with printable OBJ and STL meshes.
