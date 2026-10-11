# COORD_S8_PRIMAL_COARSEN_METHODS_AND_NONWINNERS

The parent is exactly COORD_CAP_RL_C624_STRONG_G8 (S8), from its complete six-part source capsule beginning 2026-09-14T03:02:48.720Z. Recover that source directory first. Do not substitute another C624 body. This package is not a lower-C Gomboc.

## Complete exact input normalization and audit

Use CPython 3.13.5, assertions enabled; these exact commands need no third-party modules. Set SOURCE to the recovered S8 source directory and METHOD to this decoded package. Set RAW to the 52119-byte exact S8 raw complex reconstructed by REPLAY_INPUT.py in the separate complete COORD_S8_FIXED_D12_CATALOG_EXCLUSION capsule (SHA256 fa3affc96322660cd6409cb963bfbe2f4793c552b9e626f7463bb62f5bd26ab4).

    python -B -S "$METHOD/RESTORE_CHECKPOINTS.py" "$SOURCE" INPUTS
    python -B -S "$METHOD/replay_coarse.py" "$SOURCE" INPUTS/elastic2_D176/GENERATOR.json INPUTS/elastic2_D176/INCIDENCE.json EXACT2_D176
    python -B -S "$METHOD/CHECK_OUTPUTS.py" EXACT2_D176 INPUTS/elastic2_D176/EXPECTED.json
    python -B -S "$METHOD/replay_coarse.py" "$SOURCE" INPUTS/elastic3_D147/GENERATOR.json INPUTS/elastic3_D147/INCIDENCE.json EXACT3_D147
    python -B -S "$METHOD/CHECK_OUTPUTS.py" EXACT3_D147 INPUTS/elastic3_D147/EXPECTED.json
    python -B -S "$METHOD/replay_coarse.py" "$SOURCE" INPUTS/elastic3_D176/GENERATOR.json INPUTS/elastic3_D176/INCIDENCE.json EXACT3_D176
    python -B -S "$METHOD/CHECK_OUTPUTS.py" EXACT3_D176 INPUTS/elastic3_D176/EXPECTED.json

Every output directory must be new. Expected markers: ALL_FIVE_EXACT_INPUTS_RESTORED; MOVED_COARSE_RATIONAL_A_B_PASS; ALL_EXACT_ENDPOINT_OUTPUTS_MATCH 6. CHECKPOINTS.json contains full literal 315-element free-control vectors, complete exact incidence/triple data, every numerical configuration and all expected output byte counts/hashes for the three audited bodies. No optimizer replay is needed to reconstruct those exact bodies. Generator normalization zeros only coordinates which the unchanged contact plan subsequently solves; all five reconstructed auxiliary H arrays were checked exactly equal to the corresponding original saved generators, and their hashes are asserted by RESTORE_CHECKPOINTS.py.

Exact named nonwinners (each V176/E311/F137, C622, weak-only000):
- COORD_S8_D176_ELASTIC2_G14_OWN65_64_127: input elastic2_D176, counts65/64/127, supports1186bits, raw coordinates833bits.
- COORD_S8_D147_WIDEST3_G14_OWN121: input elastic3_D147, counts1/2/1, supports399bits, raw coordinates837bits.
- COORD_S8_D176_WIDEST3_G14_OWN121: input elastic3_D176, counts1/2/1, supports1161bits, raw coordinates821bits.
The other two inputs are exact definitions but only numerically classified: elastic2_D147 numerical70/75/143, elastic2_D84 numerical67/68/133. They are preserved negative candidates, not exact equilibrium claims. Existing S8 raw coordinates needed only440bits, so these moved charts worsen arithmetic.

## Catalog proposal and independently checkable finite exclusion

Numerical discovery used NumPy2.3.5, SciPy1.17.0, CPython3.13.5, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Qhull proposes simplices only. deletion.py merges exact integer primitive planes and tests their support/zero sets. The independent verifier uses only integers, Fraction and outward-rounded intervals. Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$METHOD/build_deletion_certificate.py" "$RAW" CERT.json
    python -B -S "$METHOD/verify_deletions.py" "$RAW" CERT.json REPORT.json
    python -B -S "$METHOD/EXTRACT_CATALOG.py" CERT.json CATALOG.json

Expected CERT.json487976bytes SHA25681146851555b2a94dbbf2d51528a917b4c51e72daa9b5d3823d051e07e54b832; REPORT.json822bytes SHA256957abf77bd7033bdebd3d8db94f12665ddfc7f0a61e2bb86964b2ee79dc2ae8f; CATALOG.json11400bytes SHA25626f47d10d1958c1bf21538dd070fb51982520fff1a4314bf9e84fde22434208e. Expected markers ALL_DELETION_CERTIFICATE_PROPOSED 15753 924; ALL_FIXED_S8_ONE_TWO_VERTEX_DELETIONS_C_LT_624_EXCLUDED; CATALOG_REGENERATED_PASS. The stronger independence of the separately journaled catalog-only replay removes any reliance on floating witness selection or the proposer's complete per-case lists.

For the original numerical-only screens:

    python "$METHOD/deletion.py" "$RAW" SCREEN
    python "$METHOD/pairs.py" "$RAW" SCREEN

The 177-single and15576-pair screens are superseded, for the below624 question, by the exact finite exclusion. A separate support-deletion screen starts from D132, not original S8:

    S8_SOURCE="$SOURCE" python "$METHOD/support_screen.py" "$RAW" INPUTS/S8_H.json SUPPORT_SCREEN

It is numerical only, uses a1e-7 proposal clustering threshold and1e-8 facet membership threshold, and provides no continuum/metric exclusion. The unmodified original source is preserved in legacy/support_screen.py; the top-level file differs only in environment/CLI path handling.

## Constructive search with actual changed filled moments

coarse_atlas.py is a315-control auxiliary S8 contact DAG parameterization of the convex hull of a selected subset of its intersection vertices. The actual body is the retained primal hull, not the auxiliary H body. New triangular facets are solved exactly from3 retained vertices; nontriangular new facets are deliberately rejected unless separate rank constraints are supplied. Analytic Jacobians differentiate actual new volume, all moments, centroid, maximal support gaps, tetrahedral volumes, and primal/polar escape cosines. A central finite-difference probe has RNG seed5819, step1e-7, tolerance2e-6. All other parameters are in each configuration.

The current reverse widest-path tree fixes primal root95 and original polar root3; finalized-parent ordering prevents cyclic positive escape demands. The LP improves a common fraction of negative slacks while allowing half the surplus of positive slacks, with line search additionally guarding S<=1,U<=2. It did not reach110. It stalled near another mechanical guard; this is not proof the chart is infeasible. Execute the current numerical search with:

    S8_SOURCE="$SOURCE" OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python "$METHOD/repair_elastic_v3.py" "$RAW" INPUTS/S8_GENERATOR.json INPUTS/elastic3_D147/CONFIG.json NEW_SEARCH

Use elastic3_D176/CONFIG.json for its companion. Time limits and numerical libraries make discovery endpoints platform/runtime dependent; stored exact inputs, not rerunning wall-clock optimization, define the preserved bodies.

For version2 discovery, create a clean directory V2 and copy legacy/coarse_atlas_v2.py as V2/coarse_atlas.py, legacy/repair_elastic_v2.py as V2/driver.py, and deletion.py as V2/deletion.py. Run the same four positional arguments using INPUTS/elastic2_D176/CONFIG.json (or D147/D84). Version2 uses aggregate negative-slack norm acceptance and can make that norm smaller while producing scores of new equilibria, as the exact65/64/127 body demonstrates. It must not be treated as progress toward110 merely because its merit decreased.

Version1 sources and all four actually used initial configurations are preserved under legacy. Its checkpoints were corrupted when inherited Atlas.save used np.rint(...).astype(np.int64) on large auxiliary controls: the stored integer became -9223372036854775808. Those corrupted outputs are explicitly excluded and are not continuation parents. Current saving uses Python arbitrary-precision integers, bounds scaled auxiliary controls, adds chart regularization and verifies rounded-generator round-trip. No accepted S8/D132 object depended on the corrupted branch. The initial full-QP source and configuration D147 are also retained: immediate infeasible-or-illconditioned return is an algorithm failure, not a geometric exclusion. The top-level repair_coarse.py only makes the original path inputs portable (RAW, S8_GENERATOR, CONFIG, OUT); the original is legacy/repair_coarse.py.
