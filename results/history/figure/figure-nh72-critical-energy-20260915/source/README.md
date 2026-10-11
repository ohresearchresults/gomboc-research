# New critical-disk rational body and quantitative graph-energy obstruction

Exact parent: S8 COORD_CAP_RL_C624_STRONG_G8, not another C624 object.
BASE_GENERATOR.json SHA bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2.
The physical support99 is deleted AFTER reconstruction of137 supports; anchor137
is unchanged. K99 vertex indices are Cartesian raw-lex. BUILD then removes the
physical vertices129,145 and adds the two PAIR99 triangles. CRITICAL changes ten
actual vertices and seven supports. No compensating cap point moves.

Exact definition: BASE_GENERATOR + RECONSTRUCT + explicit H-row99 deletion;
then CRITICAL with PARAMETERS. The final own volume centroid is recomputed,
never replaced by the approximately matched old centre. The body is173/309/138,
strict468,weak000. It is not a winner.

Exact proof: python -B -S REPLAY.py --out fresh-output.
Bounded stages: BASE,BUILD,A,B,REPORT,ENERGY,FINISH in that order.
Assertions must be enabled. Standard library only; tested CPython3.13.5.
ENERGY_CERT proves a conditional obstruction for the whole ten-vertex patch,
including arbitrary internal rewiring with at most ten interior vertices in its
smaller centre/metric region. It is not a global impossibility theorem.

Numerical methods: python SEARCH_REPLAY.py local_mass exact-output new-search.
Other modes: reference6,reference12,guard,two_roots,free_metric,shift124.
The shift124 output is a JSON filename, other outputs are new directories.
Tested NumPy2.3.5,SciPy1.17.0, BLAS/OMP1. Numerical searches require those packages.
Actual completed/interrupted scopes are RUN_STATUS.json; a requested total is not
a completed search. All helpers and the complete material proposal are present.
Only the local_mass proposal supplied the new exact coordinates. FREEZE.py checks
its exact ties-to-even round on denominator10^12. No numerical run is needed to
reconstruct the exact endpoint. Future floating trajectories may differ.
