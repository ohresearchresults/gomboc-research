# Exact C622 check with SageMath

SageMath 10.6 reconstructs the published 137 halfspaces over the rational field `QQ`, using its PPL backend. Its built-in volume-centroid calculation and a separate equilibrium census recover 176 vertices, 311 edges and 137 facets, with strict counts `(S,U,H)=(1,1,0)` and weak counts `(0,0,0)`.

The reconstructed vertices, volume and volume centroid agree exactly with the archived report. The checker imports none of the original search or verification programs. It tests every maximal facet, edge and vertex at the recomputed volume centroid. A tetrahedron, cube and prism with weak equilibria exercise its classification before the C622 calculation.

From the repository root, with SageMath 10.6 installed:

```sh
sage -python checks/sagemath/verify.py C622/verified/raw.json sage-result.json C622/verified/A.json
```

The optional last argument compares the new result with the archived report only after the geometry and equilibrium census have been computed. `C622-result.json` records the successful run on 13 October 2026 (Europe/Kyiv), limited to one CPU, in 67 seconds. Exact geometry computation is provided by SageMath/PPL; the equilibrium classification is the supplied script. This is a software cross-check, not an external mathematical review.

The tested container was `sagemath/sagemath:10.6` (Linux x86-64). SageMath documentation: [rational polyhedra](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/constructor.html) and [volume centroids](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/base7.html).

## C694: larger escape separation, fewer facets

SageMath also confirms this body’s strict counts `(1,1,0)` and weak counts `(0,0,0)` in 43 seconds; `C694-result.json` records the result. Its vertices, centroid and volume agree exactly with a fresh run of the archived checking program.

The [published C694 source package](../../results/history/figure/gomboc-C694-2026-09-09/) reconstructs a different body with 217 vertices, 347 edges and 132 facets, of complexity 694. `C694-input.json` contains its reconstructed halfspaces in the same input format as C622. Its exact escape certificate was rerun and gives a normalized escape score strictly above `1/150000` for every nonroot physical and polar vertex; the certificate is `C694-margins.json`. This is a bound on escape angles for this geometry, not a coordinate-rounding or fabrication tolerance.

```sh
sage -python checks/sagemath/verify.py checks/sagemath/C694-input.json c694-sage-result.json
```

To reproduce the input and margin certificate, extract the named texts in the source package's `source-map.json` into an empty working directory, then run:

```sh
python3 -B -S GENERATE694.py
python3 -B -S exact_A.py RAW.json --out A.json
python3 -B -S margin_certificate.py RAW.json A.json --out MARGINS.json --denominator 150000
```

`RAW.json` uses normals `I` and a common offset `D`; convert each row to `I[i] + [D]` under the `H` key for this SageMath checker. The input geometry is unchanged by that format conversion.
