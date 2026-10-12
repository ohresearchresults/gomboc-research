# figure-0087

AI research report · 2026-08-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete research handoff

The authoritative, self-contained research result is COMPLETE_HANDOFF.md. It contains the explicit winner-or-fallback verdict; the certified `k=3` Fourier-phase smooth seed; the deterministic exact rational finite generator; all active H rows and V coordinates; layer membership; reconstructed maximal-face cycles and true edges; exact uniform volume and own centroid; exhaustive full-normal-cone face, vertex, and edge mechanics; inactive support slacks; the quantitative perturbation certificate; the exact residual mechanism if the body is not `(1,1,0)`; and the delimited search record.

The authoritative machine-readable verdict is FINAL_VALIDATION_STATUS.json, and the complete exact mechanical record is tower_fourier_audit.json. The exact rational generators are tower_fourier_H_rational.json and tower_fourier_V_rational.json; reconstructed topology is in topology.txt.

Certification and independent reproduction artifacts:

- Smooth-source certificate (`smooth_seed_certificate.json`)
- Finite perturbation certificate (`perturbation_certificate.json`)
- Independent exact verifier (`verify_fourier_exact.py`)
- Independent smooth verifier (`verify_smooth_seed.py`)
- Independent perturbation-box verifier (`verify_support_perturbation.py`)
- Complete verification runner (`[internal-source-reference].sh`)
- Fresh successful verification marker (`RUN_ALL_CHECKS_PASS.txt`)
- Fresh verification transcript (`[internal-source-reference].latest.log`)
- OBJ mesh (`tower_fourier.obj`)
- STL mesh (`tower_fourier.stl`)
- SHA-256 manifest (`MANIFEST.sha256`)

The complete portable artifact set is fourier_phase_finite_polyhedron_bundle.zip, with its digest in fourier_phase_finite_polyhedron_bundle.zip.sha256. After extraction, run `bash [internal-source-reference].sh`; the exact and interval verifiers reconstruct the body and its own centroid from the generator rather than trusting stored topology or equilibrium labels.
