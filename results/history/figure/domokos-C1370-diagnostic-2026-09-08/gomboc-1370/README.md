# NN51_CHAIN258_PN03_C1370

An explicit convex polyhedron with uniform volume density, evaluated at its own volume centroid.

| Quantity | Value |
|---|---:|
| Vertices | 258 |
| True edges | 685 |
| Maximal planar facets | 429 |
| Complexity, C = 2E = V + E + F - 2 | 1370 |
| Strict stable equilibria | 1 |
| Strict unstable equilibria | 1 |
| Saddle equilibria | 0 |
| Degenerate equilibria | 0 |

The stable facet is the triangle `[158,163,161]`; the unstable vertex is `138`. Indices are zero-based. The maximal facets comprise 359 triangles, 62 quadrilaterals, 4 pentagons, 3 hexagons and 1 heptagon. The 512 integration triangles include 83 flat diagonals, which are not true polyhedron edges.

## Verify

Extract this directory and run, with Python 3.11 or newer:

```sh
python3 -S REPLAY.py
```

No third-party packages, network access or other files are required. Do not use `-O`: assertions perform the checks. Run `REPLAY.py`, not the optional standalone conversion entry point of `codec.py`.

Successful completion prints `FIRST_COMPLETE_EXACT_PASS`, `SECOND_COMPLETE_EXACT_PASS`, and `FRESH_STANDARD_LIBRARY_COMPLETE_REPLAY_PASS`. It regenerates `verified/` and `REPLAY_REPORT.json`. Runtime depends on the machine; the arithmetic involves large exact integers.

## Inspect the figure directly

- `verified/vertices.csv.gz`: 258 rows of three **integer numerators**, without a header. Divide every entry by the common positive integer `centred_denominator` in `verified/exact_report.json`. Their filled convex hull is the figure. Coordinates are exact rational numbers, not rounded decimals.
- `verified/exact_report.json`: the denominator, all maximal polygon cycles (`maximal_cycles`), true edges, exact mass data and equilibrium census. Each `true_edges` entry is `[vertex_i, vertex_j, facet_f, facet_g]`.
- `verified/raw_vertices.csv.gz`: coordinates before the exact centroid translation, with denominator `raw_denominator` from that report.
- `verified/triangles.csv.gz`: outward integration triangles, as vertex-index triples.
- `verified/independent_report.json`: the second implementation's results.
- `REPLAY_REPORT.json`: the local replay's combined checks.

For another implementation, the centred vertex table and maximal facets are sufficient inputs. The supplied code is not required to formulate the figure.

## Exact reconstruction and checks

`capsule.pn03` is the compact defining data; `capsule.b85` is its compressed text encoding. `codec.py` reconstructs rational coordinates from integer seeds and 79 ordered one- or two-coordinate linear solves. `SUMMARY.json` pins the input hash and expected counts. The PN03 input has 10,534 bytes and SHA-256:

```text
7b04ac8b258f880034877a398528e6d777de81368f6c314d266376773373337d
```

`exact_audit.py` checks supporting planes against every point, reconstructs maximal facets and true edges, integrates the uniform solid, translates by its exact centroid, and classifies faces, vertices and edges. `independent_audit.py` separately validates the supplied maximal cycles, reconstructs edges from facet intersections, reintegrates mass using a different interior reference, and uses different equilibrium tests. It consumes the first report's proposed cycles but checks their geometry and mass rather than simply trusting its census.

For raw integer vertices I with denominator D and outward triangles (a,b,c), define W = sum det(Ia,Ib,Ic), and M = sum det(Ia,Ib,Ic)(Ia+Ib+Ic). The volume is W/(6D^3), the raw centroid is M/(4WD), and the centred vertices are I/D minus that centroid. Both implementations verify the ordinary mass; the final first moments are exactly zero. No point weights or chosen substitute centre are used.

The replay also checks positive rooted primal/polar witness paths, exact translation covariance, and rejection of a reversed or missing boundary triangle. These are reproducible computational checks, not an external review or a proof of minimum complexity.

`SHA256SUMS.txt` records the packaged files. On macOS, check it with `shasum -a 256 -c SHA256SUMS.txt` from this directory before rerunning the verifier.
