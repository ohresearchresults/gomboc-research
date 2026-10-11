# C622 homogeneous mono-monostatic polyhedron: review package

Object: VQ20_C622_ROUTE88_118_G12 (C622_ROUTED).
176 vertices, 311 true edges, 137 maximal facets. C = V + E + F - 2 = 622.
The supplied exact checks return (S,U,H) = (1,1,0), with no weak/degenerate equilibria, about the filled solid's own uniform-density volume centroid.

## Start here

- `EXACT_MODEL.json`: exact rational raw vertex coordinates, outward polygonal faces, true edges, and exact raw volume centroid. Fractions are strings. Subtract raw_centroid from each vertex to place the centroid at (0,0,0). Do not parse these fractions through floating point.
- `gomboc_C622_views.png`: three orthographic views at original proportions; stable face blue, unstable vertex red.
- `gomboc_C622_V176_view.stl`: rounded ASCII viewing mesh, 348 triangles (211 added face diagonals, not true edges). NOT a certified printable mono-monostatic model.
- `verified/A.json`, `verified/B.json`: fresh full reports, including incidence, exact coordinates, centroid and equilibrium predicates. The files agree byte for byte.
- `verified/RECEIPT.json`: fresh local endpoint verification on 16 September 2026, completed in about 18 seconds on the author's computer.
- `PRECISION_AND_MESH_CHECK.json`: rounded-STL readback and float32 import diagnostic.

## Reproduce the exact endpoint

Use Python 3.11 or newer, standard library only. In this extracted directory run:

    python3 -B -S VERIFY.py fresh-proof

The output directory must not already exist. Assertions must be enabled (do not use -O).
The program verifies all 75 source-manifest entries, decodes and reconstructs the exact generator, independently enumerates the polyhedron by two supplied algorithms, computes all strict/weak face/edge/vertex equilibria and the uniform volume centroid, runs a third centred integer mass integration, and checks positive/weak/malformed fixtures.
Expected terminal status: LOCAL_C622_ENDPOINT_TWO_EXACT_AUDITS_AND_THIRD_MASS_PASS.
This is a rerun of supplied AI-assisted verification programs, not external peer review or proof-assistant certification.

`verified/raw.json` is a compact alternative exact definition: integer halfspaces H, with each [a,b,c,d] meaning ax+by+cz <= d in the raw coordinate system. The raw centroid is NOT the origin. The displayed STL uses centred coordinates.

## Precision and printing

The common centred denominator has 56,802 bits / 17,099 decimal digits. This is an exact integer denominator size, NOT a statement that 17,099 decimal places are necessary, nor a manufacturing tolerance bound.
The STL uses 25 significant decimal digits per coordinate. Its readback retains 176 distinct vertices and 348 nondegenerate triangles; every mesh edge occurs twice with opposite orientation, and all origin-based oriented tetrahedra have positive volume.
A supporting-plane vertex test using the rounded mesh's recomputed volume centroid finds one strict supporting vertex in the literal ASCII data. Repeating that test after rounding coordinates to float32 finds 50. This diagnostic is not a full convex-hull audit or a proof of all equilibrium counts for either rounded mesh. Coplanar polygonal facets need not remain exactly coplanar after rounding.
Some CAD/viewer/mesh pipelines may use float32, weld vertices, simplify faces or apply tolerances. Their geometry and equilibrium counts may differ from the exact rational body. No physical printing tolerance or successful mono-monostatic print has been established.

## Provenance and scope

The endpoint source/data capsule is preserved unmodified under `source/`, including its manifest and reconstruction methods. `VERIFY.py` is the local endpoint-only runner adapted solely to accept a fresh output-directory argument. Original expected endpoint reports are `ENDPOINT_A.json` and `ENDPOINT_B.json`.
Public packaging omits process-start records and a duplicate later replay directory. The 75-entry scientific source manifest, exact generator and audit outputs are unchanged; the outer `SHA256SUMS.txt` describes this selected public package.
Other cases in source/ are preserved context, not additional claims made by this package. The full ten-case replay and numerical search have not been rerun for this delivery. Only the C622 endpoint and small fixtures were freshly checked.
`EXPORT_VIEWS.py` reproduces the display files and precision diagnostic; plotting additionally needs matplotlib and numpy. `SHA256SUMS.txt` identifies the packaged files.
No minimality, publication priority, or printability is claimed.
