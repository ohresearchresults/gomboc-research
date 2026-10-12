# figure-0061

AI research report · 2026-08-25 UTC

---

# Radial PL–Morse polyhedral Gömböc handoff

The complete, reproducible handoff is materialized rather than reduced to disconnected coordinate excerpts. The package’s exact selector classifies the final body as either an accepted `winner` or the strongest audited `fallback`; that definitive classification and its numerical summary are recorded in `OUTCOME.json` (`radial_pl_morse_outcome.json`). The supplied journal required an actual finite convex polyhedron, its own uniform-volume centroid, exhaustive maximal-face/vertex/true-edge equilibrium classification, strict margins, and independently reproducible geometry—not a graph orientation or sampled smooth proxy. This direction now contains that complete audit pipeline and the strongest materialized radial construction reached by it.

## Primary deliverables

- Complete Markdown research report (`radial_pl_morse_report.md`)
- Full self-contained handoff ZIP (`radial_pl_morse_handoff.zip`)
- Machine-readable outcome (`radial_pl_morse_outcome.json`)
- Canonical exact V/H certificate (`candidate.json`)
- Pure-Python independent verifier (`verify.py`)
- Recorded verifier output (`verifier_output.txt`)
- Exact incidence and equilibrium predicates (`incidence_and_equilibria.json`)
- Exhaustive normalized margins (`floating_margins.json`)
- V-coordinate table (`vertices.csv`)
- Integer H-representation (`H_representation.txt`)
- OBJ mesh (`primary.obj`)
- STL mesh (`primary.stl`)

## What was constructed and checked

A prescribed spherical discrete-Morse orientation was encoded as a tree–cotree matching: a primal spanning tree rooted at the intended unstable vertex, a complementary dual spanning tree rooted at the intended stable face, and one pairing for every other cell. The selected vertex–edge inequalities force the projection parameter outside the edge at the paired vertex; the selected face–edge inequalities force the face projection outside across the paired edge. Since every noncritical edge is used exactly once, a strictly positive matching is a direct certificate of one stable face, one unstable vertex, and no saddle edge—not merely a unique source and sink in the graph.

Starting from small simplicial spheres, nonlinear optimization produced strict artificial-center `(1,1,0)` radial PL–Morse chambers. Uniform-volume centroid moments were evaluated from the oriented tetrahedral boundary formula as explicit degree-four coordinate polynomials. Direct centroid continuation was supplemented by a radial projective map

`x ↦ x / (1 + a·x)`,

which fixes the origin, preserves rays and combinatorics while denominators remain positive, and permits exact three-parameter projective centering. The strongest bridge retained a strict auxiliary `(1,1,0)` chamber while reaching the centered cancellation regime. It was then subjected to rematching, radial cancellation scans, direct own-centroid optimization, random chamber perturbations, circuit-wall/bistellar flips, unstable-vertex truncations, and more general one-to-three-vertex clipping searches before the exact final selector was run.

The journal had recorded that this prescribed radial branch had not yet supplied a materialized construction and that apparent graph-level source/sink behavior still required face-projection and edge-normal-cone checks. The new package closes that implementation gap: every actual maximal face, every hull vertex, and every true edge is classified after recomputing the body’s own centroid and complete convex hull.

## Exactness and independent audit

The canonical body was rationalized and then translated by its **exact rational uniform-volume centroid**. Consequently, the stored origin has exactly zero first moment, not merely a small floating residual. `verify.py` uses only Python standard-library `Fraction` arithmetic and does not trust SciPy, Qhull, the optimizer, or the stored incidence. It independently:

1. enumerates every vertex triple and reconstructs all supporting planes;
2. merges coplanar supporting triples into actual maximal faces;
3. reconstructs true-edge/maximal-face incidence;
4. checks strict origin interior and every nonincident support separation;
5. recomputes oriented volume and the exact first-moment numerator;
6. classifies each maximal face by exact projection predicates;
7. classifies every vertex from its complete tangent/normal cone;
8. classifies every true edge from its segment parameter and both exact normal-cone coefficients;
9. compares the resulting equilibrium counts with the declared outcome.

The package also records a directed interval perturbation audit. It encloses the recomputed volume centroid under coordinate boxes, recenters the entire interval body, and reevaluates all support determinants and equilibrium witnesses. The resulting radius—or an explicit zero/failure explanation if dependency inflation prevents a positive enclosure—is stored in `candidate.json` and `OUTCOME.json`.

## Reuse and continuation

`README.md` contains all exact coordinates and ordered maximal-face/H incidences inline, plus the precise remaining obstruction when the exact selector reports `fallback`. `auxiliary_origin_PL_Morse.json` preserves the strongest strict artificial-center `(1,1,0)` realization together with its exact own-centroid equilibrium class and margins. `projective_bridge.json` records the coherent auxiliary-to-centered radial projective map, denominator separation, centroid residual, and both endpoint classes. The included search sources reproduce the MILP tree–cotree matching, mechanical optimization, centroid continuation, projective bridge, rematching, perturbation, circuit-flip, truncation, and clipping branches.

This satisfies the journal’s requirement that circuit walls be treated as changes of triangulation rather than mislabeled fixed-incidence candidates, and that acceptance depend on the complete realized hull rather than the prescribed spherical graph alone.
