# C622: source of the construction and the steps that led to it

This folder holds the stored integers and programs needed to rebuild C622 and nine related bodies, check them exactly, and replay the selected numerical construction path.

C622 has 176 vertices, 311 edges and 137 faces. About its own centre of mass it has one stable equilibrium, one unstable equilibrium, no saddle and no degenerate equilibrium. It has one edge fewer than the earlier 624 body used for comparison, and two fewer than the 626 body it was derived from. No claim is made that it is the smallest possible, or that nobody else found one earlier.

## Words used here

- **Equilibrium counts** are written (stable, unstable, saddle), always about the solid's own centre of mass at uniform density. These are strict counts; weak cases are listed separately. The target is (1,1,0) with no weak cases.
- **Strict / weak.** Strict equilibria satisfy all inequalities for their class strictly. Weak (degenerate) equilibria satisfy the non-strict conditions with at least one equality: for example, the centre-of-mass projection lies on the boundary of a face. The checkers report these separately as `counts` and `weak`.
- **Faces and edges** are counted after merging coplanar faces. Diagonals added only to triangulate a face are not edges.
- **Size** is C = V + E + F − 2 = 2E. The number in a name such as C622 or C624 is this size.
- **Generator**: the list of integers from which a body is rebuilt exactly.

## The ten stored bodies

| File in `inputs/` | V / E / F | Counts | What it is |
| --- | --- | --- | --- |
| `C622_ROUTED` | 176 / 311 / 137 | (1,1,0) | The result |
| `PARENT` | 178 / 313 / 137 | (1,1,0) | The 626 body the search started from |
| `C624_NONSIMPLE` | 177 / 312 / 137 | (1,1,0) | Intermediate body after merging two vertices of the parent |
| `C622_ROUTING_WARM` | 176 / 311 / 137 | (8,1,7) | Intermediate body after removing one more edge; too many equilibria |
| `CONDITIONED_C626`, `CONDITIONED_C624` | 178 / 313 / 137 and 177 / 312 / 137 | (1,1,0) | Adjusted versions of the 626 and 624 bodies with larger safety margins |
| `S8_DEPENDENCY` | 177 / 312 / 137 | (1,1,0) | A separate, earlier 624 body, kept for comparison. It is not an ancestor of C622 |
| `C624_233_NONWINNER`, `C624_132_NONWINNER`, `C620_121_NONWINNER` | see `EXPECTED.json` | (2,3,3), (1,3,2), (1,2,1) | Failed attempts, kept as exact counterexamples |

A failed attempt shows only that one specific proposed step did not work. It does not show that no body of that size exists.

## Exact check of all ten bodies

Standard library only; run with assertions enabled.

    python -B -S REPLAY.py --out proof

Expected last line: `VQ20_C622_TWO_INDEPENDENT_EXACT_AUDITS_COLD_SOURCE_ONLY_PASS`

For each body the program:

- decodes the stored integers and checks their hashes;
- rebuilds the polyhedron with two independent programs (`check_A.py`, `check_B.py`);
- tests every face, vertex and edge for equilibrium, including weak cases;
- computes the volume and centre of mass exactly, and repeats that computation a third time in integers.

It also checks small test inputs that must be rejected or must report weak equilibria.

In `C620_121_NONWINNER`, half-space number 114 does not touch the body. The program reports it as inactive and does not count the point where it would have met the body as a vertex.

The same run rebuilds the correspondence between the faces and vertices of the 626 body and those of the 624 and 622 bodies, together with a system of edge forces in equilibrium on each (a Maxwell stress diagram). Every force balance, every reverse transformation and 9,454 connectivity tests are checked exactly. For C622 the force is exactly zero on four pairs: (18,94), (71,109), (87,127) and (88,118). All weights and parameters are derived from the stored inputs; none is supplied as a separate floating-point number.

The full volume and first-moment fractions are in each body's `A.json` and `B.json`. The centred body is the raw body shifted by its centre of mass. The raw vertex (0,0,1) is only a fixed reference point for the encoding; it has no special role in the mechanics.

The files in `inputs/` are read with `G_FREE_CODEC.py`. Each contains every free integer, the contact structure and the order of reconstruction, plus small corrections that reproduce the original generator byte for byte. No file outside this folder is needed.

## Replaying the numerical construction

Optional. This command replays the selected construction path from stored checkpoints. It does not repeat the broader search across candidates. Environment used: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, CPU, one BLAS/OpenMP thread.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B REPLAY_NUMERICAL.py --proof proof --out numerical --first-union --local

Expected last line: `C622_FINITE_INPUT_NUMERICAL_REPLAY_IDENTICAL_PASS`

The replay has three stages:

1. **626 to 624.** The adjacent parent vertices represented by free contact nodes 155 and 156 are merged at parameter 17/20. This reproduces `C624_NONSIMPLE`.
2. **624 to 622, first attempt.** A second contraction joins a triangle and a quadrilateral at the polar edge between support/face indices 88 and 118. The run allows up to 100 numerical correction iterations, recomputing the volume centroid as the shape changes. This reproduces `C622_ROUTING_WARM`, which has counts (8,1,7).
3. **Removing the extra equilibria.** From that body the program computes cycle-free paths to two roots, one in the body and one in its polar (shortest paths by Dijkstra's algorithm, with directed cost max(−escape angle, 0) + 1e−14). It then applies the 8 recorded corrections of shape and mass and reproduces C622 byte for byte. The paths are stored in `C622_ROUTES.json`.

Omit `--first-union` and `--local` to repeat only stage 3.

A body with slightly different floating-point output is not an alternative verified result: only the exact stored bodies are verified. The paths in stage 3 are a search aid; they are not edges of the body.

The exact checks cover the stored bodies and the specified incidence relationships between them. Numerical replay checks the outputs of the named construction stages against stored hashes. It is not proved that no extra equilibrium appears along the continuous deformation between two stored bodies.

## Continuing the search

    python -B -S PREPARE_METHODS.py proof

This installs the verified 626 parent and recreates the earlier list of 75 candidates. To work from another stored body, use `PREPARE_CHART.py` to rebuild its face structure. The structures for `C624_NONSIMPLE` and `C622_ROUTED` are already produced by the exact check above.

The numerical methods are in `methods/`; add `methods/parent` to `PYTHONPATH` if needed. `PROTOCOLS.json` lists the parameters of every run that mattered: successes, failures and initial scans. A gap in a scan or a solver failure is not a mathematical exclusion.

The general merge programs (`ANY_UNION`, `LOCAL_UNION`) are not limited to the triangle-with-triangle merges of that list. A contraction that would eliminate a node of degree three requires removing a vertex and rebuilding the whole face structure; the current code rejects that case rather than miscount.

`CONDITIONED_C626` has a smallest escape angle above 1/125000, against less than 9/20000000 for the parent: more than 160/9 times larger in that measure. `CONDITIONED_C624` has a smallest value above 6/10^6. These numbers are not manufacturing tolerances on the coordinates.

## Other files

- `MANIFEST.json`: SHA-256 of every file in this folder; checked before each run.
- `EXPECTED.json`: expected sizes, counts and report hashes for the ten bodies.
- `AUTHORITIES.json`: where each source file came from.
- `PROTOCOLS.json`: also records the version of the numerical scanner and one correction that affected displayed diagnostics only.

`methods/` includes complete helper programs reused from the wider research as well as the minimal exact checkers. Earlier search buffers are not needed for any stored body or for the replay above.

The Python files were reformatted for readability on 12 October 2026. Only layout and comments changed: each file parses to the same syntax tree as before, and the exact check still reproduces the stored reports byte for byte. The original bytes are in the Git history and in the historical-constructions download.
