# C622: an exact polyhedron with one stable and one unstable equilibrium

C622 is a convex polyhedron with 176 vertices, 311 edges and 137 faces. As a solid of uniform density it has exactly one stable equilibrium (on a face) and one unstable equilibrium (on a vertex), measured about its own centre of mass. It has no saddle equilibrium and no degenerate one.

The name is the size measure C = V + E + F − 2 = 622. Faces are counted after merging coplanar faces, and only edges between two different faces are counted. In the source files the same body is called `C622_ROUTED` or `VQ20_C622_ROUTE88_118_G12`.

## Files

- `EXACT_MODEL.json`: the definition. Rational vertex coordinates, faces listed counter-clockwise seen from outside, edges and the centre of mass. Fractions are written as strings and must be parsed exactly, without conversion to floating point. Subtract `raw_centroid` from each vertex to put the centre of mass at (0,0,0).
- `gomboc_C622_views.png`: three orthographic views at true proportions; stable face blue, unstable vertex red.
- `gomboc_C622_V176_view.stl`: a rounded mesh for viewing, 348 triangles. Triangulating the faces adds 211 diagonals that are not edges of the body. See the precision limits below.
- `verified/A.json`, `verified/B.json`: the reports of the two exact checkers, with coordinates, faces, centre of mass and the sign of every equilibrium test. The two files are identical byte for byte.
- `verified/raw.json`: the same body as 137 integer half-spaces. Each `[a,b,c,d]` means `ax+by+cz <= d`, in coordinates where the centre of mass is not at the origin.
- `verified/RECEIPT.json`: record of the verification run of 16 September 2026.
- `PRECISION_AND_MESH_CHECK.json`: what happens to the mesh when coordinates are rounded.

## Check it yourself

Python 3.11 or newer, standard library only. From this folder:

    python3 -B -S VERIFY.py fresh-proof

The output folder must not exist yet. Do not use `-O`: the checks are assert statements. The run takes about 20 seconds.

Expected last line: `LOCAL_C622_ENDPOINT_TWO_EXACT_AUDITS_AND_THIRD_MASS_PASS`

The program:

1. checks the SHA-256 of all 75 files listed in `source/MANIFEST.json`;
2. decodes the stored integers and rebuilds the body;
3. finds all vertices, edges and faces with two independent programs, `check_A.py` and `check_B.py` in `source/methods/parent/`;
4. computes the volume and centre of mass exactly in each, and a third time in integers;
5. tests every face, vertex and edge for equilibrium, including degenerate cases;
6. runs both checkers on small test bodies with known answers and on malformed inputs that must be rejected.

It does not repeat the numerical search or check the other nine bodies in `source/`; [source/README.md](source/README.md) describes how to do that.

## Precision and printing

Written over a common denominator, the centred coordinates need a denominator of 56,802 bits (17,099 decimal digits). That figure describes the exact representation. It does not say how many digits, or what manufacturing tolerance, are needed to keep the two equilibria.

The STL file uses 25 significant decimal digits per coordinate. Read back, it has 176 distinct vertices and 348 non-degenerate triangles, every mesh edge appears twice with opposite orientation, and all tetrahedra from the origin have positive volume.

A supporting-plane diagnostic, using the rounded mesh's recomputed centre of mass, finds one strict supporting-vertex candidate in the ASCII mesh and 50 after rounding to 32-bit floats. This is a diagnostic only: it is not a full check of the rounded bodies, and faces that are exactly flat need not stay flat after rounding.

CAD programs, viewers and mesh tools often use 32-bit floats, merge nearby vertices, simplify faces or apply tolerances. The shape they produce, and its equilibria, may differ from the exact body. No printing tolerance has been established and no printed copy has been tested.

## Other files

`source/` contains the stored construction, the programs that rebuild it and the programs used in its numerical construction. `ENDPOINT_A.json` and `ENDPOINT_B.json` are the expected reports that `VERIFY.py` compares against.

`EXPORT_VIEWS.py` regenerates the image, the STL file and the precision diagnostic; it needs matplotlib and numpy. `SHA256SUMS.txt` lists the hashes of the files in this folder.
