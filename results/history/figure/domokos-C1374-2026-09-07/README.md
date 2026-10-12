# Explicit homogeneous mono-monostatic convex polyhedron: C = 1374

Specimen: FUSION258_PN03_C1374. Prepared for Professor Gábor Domokos, 7 September 2026.

## Exact object and result

The exact convex solid has uniform volume density, 258 vertices, 687 true edges and 431 maximal planar faces. Its mechanical equilibrium counts relative to its own volume centroid are (S,U,H) = (1,1,0). Thus C = V+E+F-S-U-H = 1374. This is an explicit upper-bound construction, not a proof of minimality or a claim of priority.

The unique stable maximal face is the triangle with zero-based indices [158,163,161]; the unique unstable vertex is 138. The boundary triangulation has 512 triangles. Its 81 internal coplanar diagonals are not true polyhedral edges.

## Exact coordinates

`verified/vertices.csv.gz` contains one integer triple P_i per row. Divide every component by the positive common denominator in `verified/exact_report.json`, field `centred_denominator`. The resulting coordinates P_i/Q have exactly zero ordinary-volume first moments. `verified/triangles.csv.gz` contains outward oriented zero-based triangle indices; `maximal_cycles` and `true_edges` in the same JSON report specify the actual facets and edges.

The integers have thousands of digits; use arbitrary-precision integers/rationals. Python 3.11+ readers should call `sys.set_int_max_str_digits(0)` before parsing them. `verified/raw_vertices.csv.gz` contains the same solid before translating its own volume centroid to the origin, with denominator `raw_denominator` in the report.

## Reproduce from the compact source

Python 3.11 or newer, standard library only, no internet or external packages:

    python3 -S REPLAY.py

Do not use Python's `-O` option (assertions are essential). The script reconstructs the coordinates from `capsule.pn03`, checks the capsule hash, recomputes both audits and writes `REPLAY_REPORT.json`. Depending on hardware, allow several minutes.

The source capsule has 10,525 bytes and SHA-256:

    0470008c42fd61ca27045b001cddee34ab68a954dc6e8ec0198a63e9715409c8

The two audit implementations use different equilibrium tests and volume computations. The first checks global supporting planes and local edge sign conditions. The second uses maximal facet cycles, an interior-reference tetrahedralization, global vertex support and Gram-system edge-cone tests. Checks also cover complete contacts, convex polygons, vertex extremality, connected cyclic links, ordinary volume/centroid agreement, and zero equilibrium degeneracies. The replay checks primal/polar ascent witnesses, exact translation covariance of moments, and rejection of a reversed or missing triangle. The implementations share the reconstructed data and the second receives the maximal cycles from the first, which it validates.

`fresh-replay.log` and `REPLAY_REPORT.json` record the local run used to prepare this delivery. These are computational checks, not a claim of peer review or a proof-assistant formalization.

## STL and PNG

The separately supplied `gomboc_C1374_V258_view.stl` and `gomboc_C1374_views.png` are viewing representations of this same specimen. The STL is ASCII, with 17-significant-digit coordinates from the exact centred body. The proportions are not exaggerated or smoothed.

Unlike the earlier C=5368 specimen, these rational coordinates generally do not have finite decimal expansions. The STL therefore necessarily rounds them. The exact coordinate error, standard-loader roundtrip, closure, orientation, triangle count and volume checks are recorded in `DELIVERY_CHECKS.json`. Exact facet coplanarity and the equilibrium count are certified for the rational source, not for the rounded STL or a manufactured object. No geometric repair or vertex merging by tolerance was applied to the export.

The PNG shows three orthographic views at the same scale. S marks the stable face in blue; U marks the unstable vertex in red. Internal coplanar triangulation diagonals are omitted in the drawing.

## Provenance and contribution

The construction and original verification programs were produced by an AI-assisted research workflow built and operated by Oleksandr H. The source capsule and verification source texts were recovered without alteration from the shared research journal entries dated 2026-09-06T13:56:32.877Z and 2026-09-06T14:17:23.665Z, with their recorded SHA-256 hashes checked. The packet was independently replayed locally on 7 September 2026. This wording describes a fresh execution, not independent human mathematical review.
