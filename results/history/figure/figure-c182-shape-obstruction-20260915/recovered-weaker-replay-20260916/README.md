# C182 geometric-obstruction source capsule

This package contains the complete 136-row exact definition of the existing
C182_TWO_PLANE222 nonwinner, both independent full reconstruction/mechanics
auditors, third own-centred integer-mass verification, and a new exact geometric
gate. It is not a new own110 construction. The new gate and proof are pending
canonical-journal persistence because scheduler authorization was unavailable.

Run with CPython 3.13.5, standard library only, assertions enabled:

    python -B -S REPLAY.py fresh

The output directory must not already exist. All expected deterministic hashes
are in EXPECTED.json. Successful execution prints

    A 54 91 39 [2, 2, 2] [0, 0, 0]
    B 54 91 39 [2, 2, 2] [0, 0, 0]
    EXACT_C182_TWO_STABLE_TWO_UNSTABLE_GEOMETRIC_GATE_PASS
    C182_GEOMETRIC_OBSTRUCTION_SOURCE_ONLY_PASS

The fresh directory contains the complete exact coordinates, maximal facets,
true edges, volume, first moments, own centroid and complete equilibrium census
in A.json and independently in B.json; MASS.json is the third integration;
GATE.json records the new containment inequalities. The gate checks all 136
supplied supports, including those currently inactive. None of these reports is
read as a cached input to either auditor.

See SHAPE_PROOF.md for the proof, exact constants and scope. In particular,
condition number below 21/5 is excluded for monostability in this affine orbit;
larger condition number does not imply success. The local canonical-journal
snapshot recovered in this turn reported a separate C622 own110 incumbent.
Live run state could not be read, so that is a snapshot benchmark only.
