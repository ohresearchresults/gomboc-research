# C622: an exact homogeneous mono-monostatic polyhedron

Object: VQ20_C622_ROUTE88_118_G12 (C622_ROUTED).
176 vertices, 311 true edges, 137 maximal facets. C = V + E + F - 2 = 622.
The supplied exact checks return (S,U,H) = (1,1,0), with no weak/degenerate equilibria, about the filled solid's own uniform-density volume centroid.

## Start here

- `EXACT_MODEL.json`: rational vertex coordinates, outward polygonal faces, true edges and the volume centroid. Fractions are strings. Subtract `raw_centroid` from each vertex to place the centroid at (0,0,0). Parse fractions exactly, without floating-point conversion.
- `gomboc_C622_views.png`: three orthographic views at original proportions; stable face blue, unstable vertex red.
- `gomboc_C622_V176_view.stl`: rounded ASCII viewing mesh with 348 triangles. Triangulation adds 211 face diagonals to the true edges. See the precision limits below.
- `verified/A.json`, `verified/B.json`: exact verification reports, including incidence, coordinates, centroid and equilibrium predicates. The files agree byte for byte.
- `verified/RECEIPT.json`: verification record from 16 September 2026.
- `PRECISION_AND_MESH_CHECK.json`: rounded-STL readback and float32 import diagnostic.

## Reproduce the exact endpoint

Use Python 3.11 or newer, standard library only. From the `C622` directory, run:

    python3 -B -S VERIFY.py fresh-proof

The output directory must not already exist. Assertions must be enabled (do not use -O).
The program verifies all 75 source-manifest entries, decodes and reconstructs the exact generator, independently enumerates the polyhedron by two supplied algorithms, computes all strict/weak face/edge/vertex equilibria and the uniform volume centroid, runs a third centred integer mass integration, and checks positive/weak/malformed fixtures.
Expected terminal status: `LOCAL_C622_ENDPOINT_TWO_EXACT_AUDITS_AND_THIRD_MASS_PASS`.

`verified/raw.json` gives an alternative exact definition using integer halfspaces `H`. Each `[a,b,c,d]` means `ax+by+cz <= d` in the raw coordinate system. The raw centroid is away from the origin; the viewing mesh uses centred coordinates.

## Precision and printing

The common centred denominator has 56,802 bits / 17,099 decimal digits. Its size does not specify the decimal precision or manufacturing tolerance needed to preserve the equilibria.
The STL uses 25 significant decimal digits per coordinate. Its readback retains 176 distinct vertices and 348 nondegenerate triangles; every mesh edge occurs twice with opposite orientation, and all origin-based oriented tetrahedra have positive volume.
A supporting-plane vertex test using the rounded mesh's recomputed volume centroid finds one strict supporting vertex in the literal ASCII data. Repeating that test after rounding coordinates to float32 finds 50. This diagnostic is not a full convex-hull audit or a proof of all equilibrium counts for either rounded mesh. Coplanar polygonal facets need not remain exactly coplanar after rounding.
Some CAD/viewer/mesh pipelines may use float32, weld vertices, simplify faces or apply tolerances. Their geometry and equilibrium counts may differ from the exact rational body. No physical printing tolerance or successful mono-monostatic print has been established.

## Source and verification scope

`source/` contains the original generator, reconstruction methods and 75-entry scientific manifest. Expected verification reports are `ENDPOINT_A.json` and `ENDPOINT_B.json`. `VERIFY.py` reconstructs and checks C622 and the small test fixtures; it does not run the numerical search or the other constructions in the ten-case source bundle.

`EXPORT_VIEWS.py` reproduces the display files and precision diagnostic; plotting requires matplotlib and numpy. `SHA256SUMS.txt` lists hashes for the files in this directory.
