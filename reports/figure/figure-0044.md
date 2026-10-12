# figure-0044

AI research report · 2026-08-23 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Decisive result for the verifier-gated circumscribed branch

## Literal gate status

**No exact rational body passed the required gate.** The prior canonical file says, literally:

```json
{
  "exact_success": false,
  "selected_near_result": null,
  "best_near_witness": null,
  "result_files_scanned": 1,
  "attempt_records_scanned": 0
}
```

Thus there was no prior object with `verified=true, S=1, U=1, H=0` at its own uniform-volume centroid; the previous payload did not even select a near-witness. Its prose said “strongest recorded witness,” but the embedded witness was `null`.

The attached transcript defines the intended target as a uniform-density convex polyhedron with one stable face, one unstable vertex, no edge equilibrium, exact coordinates and centroid, a complete finite audit, and printable geometry.

## Materialized exact circumscribed near-witness

I replaced the empty wrapper with a deterministic exact object. Start from the exact affine-corridor mechanical seed at `u=v=0` and clip it by the rational halfspace

```text
(-351893317/15625000000, -1, 2022143389/500000000000) · x
    <= 346719814154737/1000000000000.
```

The clipping retains five old hull vertices and creates sixteen exact rational edge intersections. Translate the result by its exactly computed uniform-volume centroid. The resulting rational polyhedron has

```text
(V,E,F) = (21,40,21),   Euler = 2,
centroid = (0,0,0) exactly.
```

Its complete exact V-representation, primitive-integer H-representation, oriented face cycles, true edge list, edge-face incidences, reduced-rational volume and all predicate values are in the exact certificate (`rational_circumscribed_near_witness.json`). The compact deterministic construction is in the generator (`build_exact_near_witness.py`). The construction and exact topology are independently described in the recovered result.

The complete own-centroid mechanics is

```text
(S,U,H) = (2,3,3)
stable faces       = [5,20]
unstable vertices  = [0,18,20]
saddle edges       = [25,28,38]
```

The inherited target cells survive: stable face `5` and unstable vertex `0`. Every excess equilibrium is on the balancing cap:

```text
extra stable cell       = face 20, a 16-gon
extra unstable cells    = vertices 18 and 20
extra saddle cells      = edges 25, 28 and 38
```

All three excess saddle edges touch face 20. The exact classification and its Poincaré identity are recorded in the source result.

The normalized margins, reported only after exact sign verification, are:

| predicate family | minimum positive equilibrium margin | minimum absolute cell margin |
|---|---:|---:|
| face | 0.08094658360890059 | 0.0005826870472033029 |
| vertex | 0.12779237935373494 | 0.0003250385443298796 |
| edge | 0.14857473120318834 | 0.0020928029861054655 |

The unwanted cut face has stable margin `0.21284628865545738`; this is an open failure, not floating-point dust.

For every primitive halfspace `n·x <= H`, exact arithmetic proves

```text
H > 2 ||n||_1 >= 2 ||n||_2.
```

Therefore the body contains the closed Euclidean radius-2 ball. The requested smooth spectral-phase seed obeys `r^4 <= 16/15 < 2^4`, so the rational body strictly circumscribes it.

## Fresh independent exact verifier

A fresh run of the independent verifier (`verify_exact_fresh.py`) produced this output (`verify_exact_fresh.out`):

```json
{
  "verified": true,
  "certificate_sha256": "4c8276ec5cc1489d0b36a50fbddccd326467dc0dc6a2fa3246aab70afb084343",
  "exact_arithmetic": "fractions.Fraction / integer determinants",
  "topology": {"V": 21, "E": 40, "F": 21, "Euler": 2, "triangles_in_face_fans": 38},
  "exact_centroid": ["0", "0", "0"],
  "classification": {"S": 2, "U": 3, "H": 3},
  "stable_faces": [5,20],
  "unstable_vertices": [0,18,20],
  "saddle_edges": [25,28,38],
  "all_face_predicates_nonzero": true,
  "all_vertex_predicates_nonzero": true,
  "all_edge_predicates_nonzero": true,
  "strict_ball_radius_2_containment": true,
  "exact_smooth_seed_containment": true,
  "verdict": "PASS_NEAR_WITNESS_NOT_GOMBOC"
}
```

The independently captured verifier result agrees exactly.

## Continued cap search: explicit failure pattern

The continuation did not stop at the one-plane object. The reproducible search record contains:

- 120 independent one-plane centroid solves: every run reached the same strict `(2,3,3)` chamber and the same angular root to about `1e-13`;
- 250 two-plane wedge closures: no winner; best count patterns `(2,3,3)` and `(3,2,3)`;
- 48 one-apex centroid closures: every converged result was `(3,2,3)`;
- 495 radial successor-chain variants: 11 reached `(3,1,2)`.

The 40-link zero-bulge chain removes one added unstable equilibrium and one adjacent saddle, but leaves two bridge stable-saddle pairs. This isolates the remaining combinatorial task: replace the balancing 16-gon by a support patch whose two bridge strips are simultaneously nonstable and nonsaddle without creating a new unstable cap vertex.

## New exact five-dimensional obstruction

I then completed a new exact exclusion around the materialized body. Consider every linear image `A P` whose Gram matrix is

```text
Q(t) = I
     + t1 diag(1,0,-1)
     + t2 diag(0,1,-1)
     + t3 (E12+E21)
     + t4 (E13+E31)
     + t5 (E23+E32),
|tk| <= 1/16384.
```

This is a full five-dimensional trace-fixed neighborhood in the affine metric cone. For every parameter in the box:

1. `Q` is positive definite because `||Q-I||_infinity <= 1/4096 < 1`.
2. For any `A` with `A^T A=Q`, `centroid(A P)=A centroid(P)=0` exactly.
3. Invertibility preserves the complete face lattice.
4. Vertex predicates are linear in `Q`.
5. Face-foot and edge normal-cone predicates become linear in `R=Q^{-1}` after multiplication by positive denominators.
6. The Neumann bound gives `||R-I||_infinity <= 1/4095`.
7. A set of 124 exact frozen witnesses covers every face, vertex and edge branch and stays strict throughout the box.
8. The transformed body still circumscribes the smooth seed: `lambda_min(Q)>1-1/4096>9/16`, so `A P` contains a radius greater than `3/2`, while the seed radius is below `(16/15)^(1/4)<3/2`.

The complete exact certificate is metric_neighborhood_exclusion.json. A separately written verifier reconstructed the source lattice and centroid, recomputed every one of the 124 coefficient forms, checked the full Boolean coverage, and returned:

```json
{
  "verified": true,
  "source_sha256": "4c8276ec5cc1489d0b36a50fbddccd326467dc0dc6a2fa3246aab70afb084343",
  "exclusion_certificate_sha256": "9f1400e8bea42055c5500aef3848af9b9923da4c3018560730af0fb90d74ae5b",
  "metric_family_dimension": 5,
  "epsilon": "1/16384",
  "constraints_recomputed": 124,
  "classification_everywhere": {"S": 2, "U": 3, "H": 3},
  "gomboc_excluded_everywhere": true,
  "smooth_seed_circumscribed_everywhere": true,
  "minimum_preserved_raw_margin_lower_decimal": 623.0181047218814,
  "verdict": "PASS_EXACT_METRIC_NEIGHBORHOOD_EXCLUSION"
}
```

The independent verifier and complete output are here (`verify_metric_exclusion.py`) and here (`verify_metric_exclusion.out`). Consequently, ordinary affine polishing cannot repair this cap: the entire full-dimensional metric box remains exactly `(2,3,3)`. A successful construction must change the balancing-cap combinatorics or leave this neighborhood.

## Hashes and printable geometry

```text
exact rational certificate  4c8276ec5cc1489d0b36a50fbddccd326467dc0dc6a2fa3246aab70afb084343
deterministic generator     3915532bf6cdd76e3d3b1bbd3ba0b5405fc3954977f1378b504d16e52aa56978
fresh source verifier       9bb6a71894137f6b5ea843a74b0dd9031883b2fff8e667f111fa30d19ee99745
source-verifier output      70a4dc1c36da54b4391fed655be17b362b6039ae28c5e32d6d107a8457cc5944
metric exclusion            9f1400e8bea42055c5500aef3848af9b9923da4c3018560730af0fb90d74ae5b
metric verifier             908c225d27cbe7c756490b44dfef3cb2a77755a746b536fe15ec9bd92a977db7
metric-verifier output      05015589427a7101bfdc2a3cbbf62c5e235fa87c8169409a0f339bd807ab268e
OBJ                          5d532bec1bc1e25302fafb1ac29db900b4823f7874b0dffe3cc6b93883025480
exact-scale STL             574962302491711c143f89fdd49844eaab259452efb82d534b06dd92efa526b7
printable 100 mm STL        5b8342dd14a4cf7af24b1e8f4a280e0d3b75ca07412cf81ad4a37611dce1a572
complete package            f5b4de7eb1dc9fcc172cc859e4688d4f635bb305d3952754b0fba54b363b76cc
```

- OBJ (`rational_circumscribed_near_witness.obj`)
- Exact-scale STL (`rational_circumscribed_near_witness_exact_scale.stl`)
- Printable 100 mm STL (`rational_circumscribed_near_witness_printable_100mm.stl`)
- Full result report (`RESULT.md`)
- Manifest (`MANIFEST.json`)
- Complete reproducibility package (`circumscribed_decisive_artifact.zip`)

## Final verdict

**The requested homogeneous polyhedral Gömböc was not found in this branch.** The prior canonical gate status is unambiguously negative. The decisive replacement is a fully materialized exact rational circumscribed near-witness with exact own-centroid classification `(2,3,3)`, a fresh independent verifier, printable geometry, a quantified cap-local failure, and a new rigorously verified five-dimensional no-go neighborhood. No `(1,1,0)` success is claimed.
