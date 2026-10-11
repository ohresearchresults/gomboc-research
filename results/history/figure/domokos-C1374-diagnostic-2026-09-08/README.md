# C1374: investigation of the reported extra unstable vertices

8 September 2026. This investigation addresses Professor Domokos's report of
multiple unstable points in the supplied STL. The specific cause in his software
is still unknown. The results below establish a reproducible precision effect;
they do not establish what settings his team used.

## Results

| Data tested | Method | Unstable vertices |
|---|---|---:|
| Exact rational C1374 coordinates | Fresh exact integer audit of volume centroid and global supporting planes | 1 |
| Original ASCII STL decimal strings, treated exactly | Direct integer supporting-plane test after independently computing its solid centroid | 1 |
| The same STL vertices rounded to IEEE binary64 | The same exact test on the rounded coordinates, with recomputed centroid | 1 |
| The same STL vertices rounded to IEEE binary32 | The same exact test on the rounded coordinates, with recomputed centroid | 46 |
| Convex hull of the binary32 vertices | Hull computed with SciPy/Qhull, then exact centroid and exact vertex support tests | 46 |

The rational source audit also gives V=258, E=687, F=431, S=1, U=1, H=0,
C=1374, with no equilibrium degeneracies. The stable face has source indices
158, 161, 163. The unstable vertex is source index 138.

The STL parser numbers vertices by first appearance in the STL, so its unstable
vertex is index 30, corresponding to source index 138. Both indices are zero-based.

## Definition and direct test

For every vertex v, recompute the filled solid's ordinary volume centroid c.
For each other vertex w, calculate

    d(v,w) = (v-c) dot (w-v).

The plane through v perpendicular to v-c supports the body strictly at v if and
only if every d(v,w) is negative. This is the nondegenerate unstable-vertex
condition. Positive d gives a concrete other point beyond the proposed support
plane, ruling out equilibrium at v. Zero is reported separately as degeneracy.

This follows the definition in Domokos, Lángi and Várkonyi (2023), section 1.3:
https://link.springer.com/article/10.1007/s00605-023-01847-w

`check_stl_vertices.py` imports no project verifier. It parses STL vertex strings
as exact fractions, calculates the volume centroid from oriented tetrahedra,
then performs every supporting-plane decision with integers. Binary64 and
binary32 are deliberately rounded *input geometry* variants; subsequent
classification is exact in both cases. Displayed magnitudes are floating-point
summaries only. Controls cover a regular tetrahedron, exact translation of its
centroid, and rejection of an open mesh.

Run with standard-library Python:

    python3 check_stl_vertices.py gomboc_C1374_V258_view.stl --output diagnostic.json

The included original local STL, attached to the email of 7 September, has SHA-256:

    2885a642210256a32458272f5508e30e784f13335355d81862e7750884408766

## Specific rounding counterexample

Source vertex 68 (STL first-appearance index 117):

    (0.6518017951393884, 0.6523600014666776, 0.29284936787784394)

For the original STL, source vertex 67 provides a strictly positive dot product
of about +9.637446324760367e-9, so vertex 68 is not an equilibrium. After binary32
rounding and recomputation of the solid centroid, the largest dot product over
all other vertices becomes approximately -1.1103661679203757e-8. Consequently it
becomes a strictly unstable equilibrium of that rounded model. There are 45
additional unstable vertices in total after this rounding.

Many exclusion margins are around 1e-8 at this coordinate scale. A tolerance in
the classification predicate can also change the count, even without changing
the stored geometry. The report gives the exact predicate, quantities, and
tolerance convention so the counts are not confused with a scale-invariant law.

## Exact-source and STL distinction

`check_rational_source.py` independently recomputes the centroid, facet support
planes, true edges and all S/U/H counts from the raw integer coordinates. Stable
faces are tested by projecting to the face plane and checking every halfspace;
edge equilibria are tested by global support of the radial closest point. It
uses gmpy2 solely for arbitrary-precision integer arithmetic and imports none of
the original verifiers. `rational-source-diagnostic.json` records its result.

The original ASCII STL itself also has tiny coplanarity perturbations: 92 of its
512 triangles fail exact global convex support, with maximum violation distance
about 2.20e-14. Its rounded triangle surface is therefore not literally the exact
convex C1374 polyhedron. This was already the reason the delivered README labeled
STL as a viewing copy. This finding does not produce extra unstable vertices in
the exact-decimal or binary64 STL tests. The convexity and C1374 claims belong to
the rational source, whose facets are exactly coplanar.

The earlier export check established vertex/triangle fidelity, closure,
orientation and volume; it did not test equilibrium preservation through
binary32 import. The standalone diagnostic fills that verification gap.

## What still needs clarification

Ask which file, program, coordinate precision, centroid convention and tolerance
were used, or request one extra unstable vertex's coordinates. Then compare that
specific observation to the exact source and the original ASCII STL. Do not
claim the professor's computation is wrong without that comparison.
