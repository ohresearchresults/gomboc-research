# Exact C630 and C632 nonwinners

These are preserved research candidates, NOT mono-monostatic polyhedra. The verified Gömböc benchmark remains C634.

| Candidate | V | E | F | Complexity | Strict S/U/H | Weak S/U/H |
| --- | --- | --- | --- | --- | --- | --- |
| C630_COORD_NONWINNER_OWN121 | 180 | 315 | 137 | 630 | 1/2/1 | 0/0/0 |
| C632_COORD_NONWINNER_OWN121 | 181 | 316 | 137 | 632 | 1/2/1 | 0/0/0 |

Both exact generators were recovered from the complete journal capsule. Local execution of both supplied exact auditors completed successfully; A/B outputs agree with the author-pinned hashes (see LOCAL_VERIFY.log and each candidate's A.json/B.json). These checks use the body's own volume centroid. Neither body has the required 1/1/0 equilibrium counts.

The decoded generator map has SHA-256 7ca0ac9c66ac744a8590eb24fb0fab7c0394fd65c5079077063eb5fe60cfbf5b. RECOVER.py authenticates and reconstructs the definitions; VERIFY.py performs endpoint checks and refuses to overwrite existing outputs.

The author's additional degree-two moment-suite replay is reported in the journal, not independently rerun here. This is a local replay using the supplied auditors, not external mathematical review or a proof of impossibility.

Complete source capsule and discovery methodology: ../research-results-2026-09-09/figure-C630-C632-nonwinners-20260910-0855.md. Methods include actual-centroid contact contraction and a widest-path escape forest that detects misleading shrinking-edge local scores. Additional optimizer implementation files have not yet been recovered; do not represent the method description as preservation of all optimizer sources.
