# VQ20 C622: exact endpoint and finite full-contact continuation

The primary endpoint is C622_ROUTED, named VQ20_C622_ROUTE88_118_G12.
V176/E311/F137; own-filled-volume-centroid strict110/weak000.
It improves the supplied S8/C624 benchmark by one true edge and the assigned
immutable VQ20/C626 parent by two. No global minimum or external priority is claimed.

## Exact source-only reconstruction

Run with assertions enabled. Exact programs need only the Python standard library.

    python -B -S REPLAY.py --out proof

This decodes ten literal finite rational generators and checks their byte hashes,
independently reconstructs each maximal hull with both complete auditors, checks all
face, vertex and true-edge mixed-cone equilibria including weak cases, integrates
uniform volume and first moments, and performs a third centred integer integration.
The positive sources also have full exact contact-atlas forward/inverse checks.
The C620 nonwinner has inactive support114; its ghost mixed contact is explicitly
not misrepresented as a maximal physical vertex. Negative/weak fixtures are checked.

The replay additionally reconstructs exact C626-to-C624 and C626-to-C622 incidence
quotients and faithful common Maxwell charts. It checks every nodal force, panel
jump, cocycle, positive inverse denominator, round trip and 9454 graph-connectivity
tests. Refinement diagonals exposing old zero stresses are never counted as true
edges. Four exact zero stresses for C622 are (18,94),(71,109),(87,127),(88,118).
Every exact weight and all outer-chart parameters are generated from the finite
inputs; no stress or transformation is an omitted numerical parameter.

Expected terminal:
VQ20_C622_TWO_INDEPENDENT_EXACT_AUDITS_COLD_SOURCE_ONLY_PASS

Full volume and raw first-moment fractions are in each case's A.json and B.json.
They are finite determinant sums over the reconstructed maximal boundary. The
centred body is raw body minus M/V, with density one and exactly zero first moments.
The raw apex001 is an anchor, not an independently assigned reference centre.

inputs/*.json use G_FREE_CODEC.py. They contain every free integer control,
complete contact groups and acyclic plan, plus sparse corrections that reproduce
all original dependent control integers and the ORIGINAL generator bytes. No
external parent file is needed. Both the decoder and RECONSTRUCT validate contacts.

## Complete successful numerical reconstruction

Observed environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, CPU, single BLAS/OMP
thread. Numerical discovery is optional; it is not the exact acceptance proof.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B REPLAY_NUMERICAL.py --proof proof --out numerical --first-union --local

The first phase identifies physical contact nodes155/156 at parameter17/20 and
reproduces C624_NONSIMPLE. The second uses a new full 3-degenerate contact atlas for
polar edge(88,118), a triangle-plus-quadrilateral union, parameter1 and100 full-mass
correction steps. It reproduces the exact C622_ROUTING_WARM own817 nonwinner.
The third independently reconstructs that warm body and computes cycle-free rooted
routes with directed cost max(-angular_escape,0)+1e-14, Dijkstra to the physical and
centred-polar roots. It binds both full trees to C622_ROUTES.json, then replays the
observed8 full-geometry/mass corrections and reproduces the C622 winner bytewise.
A different floating rounded hash is explicitly NOT an alternative certified body.
Omit --first-union and --local to replay only the decisive routed correction.

Expected final terminal: C622_FINITE_INPUT_NUMERICAL_REPLAY_IDENTICAL_PASS

Only final finite endpoints and the observed discrete computations are certified;
there is no claimed no-birth theorem for the entire continuous interpolation.
Routing arrows are search witnesses, not added physical edges or a fixed drawing.

## Further continuation and preserved non-record objects

    python -B -S PREPARE_METHODS.py proof

This installs the independently verified C626 parent and recreates the old75-list.
For any of the other complete supplied finite generators, use PREPARE_CHART.py to
reconstruct its own maximal chart. C624_NONSIMPLE_CHART and C622_ROUTED_CHART are
already emitted by the complete exact replay.

Run numerical methods from methods/, with PYTHONPATH=parent if necessary.
PROTOCOLS.json specifies all parameters of the material successes, nonwinners and
finite initial screens. Gaps and solver failures are not mathematical exclusions.
The general ANY_UNION/LOCAL_UNION mechanisms are not restricted to the old75
triangle-triangle unions. Degree-three polar endpoint loss requires genuine vertex
suppression and a rebuilt maximal complex; the current nominal quotient explicitly
rejects that case rather than counting a triangulation or a vanished vertex.

The recovered midpoint C624_NONSIMPLE and the separately reconditioned C624 and
C626 bodies are positive non-record resources. CONDITIONED_C626 has exact minimum
full-point angular escape >1/125000, while the assigned parent's minimum is
<9/20000000: a strict >160/9 improvement in that specified quantity. CONDITIONED_C624
has floor >6/10^6. These are not independent-coordinate manufacturing tolerances.
C624_233_NONWINNER, C624_132_NONWINNER, C620_121_NONWINNER and C622_ROUTING_WARM are
complete finite counterexamples to their specific proposed promotion, not exclusions
of their continuous realization spaces. S8_DEPENDENCY is the distinct supplied C624
benchmark, not the parent of the new construction.

The source map deliberately contains complete reused research helpers as well as
the minimal exact auditors. Optional old discovery buffers are not needed for any
finite input or for the complete successful replay above. AUTHORITIES.json preserves
source identities; PROTOCOLS.json records the purely numerical scanner version and
one display-only diagnostic correction. No shared journal mutation is performed.
