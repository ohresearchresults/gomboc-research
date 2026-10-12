# figure-0071

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Comet 68 — low-vertex frontier handoff

## Determination

**No strict homogeneous convex polyhedral Gömböc was found.** I found no own-centroid open cell with `(S,U,H)=(1,1,0)`, and I produced no exact exclusion certificate for any of the inherited unresolved `V=8` systems. The rigorous frontier count therefore does not move.

The acceptance gate used here is the journal's original one: uniform volume density; equilibrium at the body's own exact volume centroid; exactly one stable maximal face, one unstable vertex, and no saddle true edge; a complete finite H/V representation, realized face lattice, exhaustive positive-margin audit, verifier, and mesh. The inherited theorem excludes every `V<=7` body but leaves `24,835` labeled necessary `V=8` systems, `17,253` rooted orbits, and `207,036` stable-face chambers unresolved. This continuation followed the reopened discovery-first instruction to search those cells and permit `V=9–12`, nonsimplicial cells, and controlled splits without converting numerical nonhits into proofs.

## What changed relative to the supplied journal

1. I materialized and exactly audited a new **12-vertex rational own-centered near-object** with `(V,E,F,C)=(12,30,20,60)` and strict `(S,U,H)=(2,3,3)`. It is the strongest new object from this direction by equilibrium count.
2. I materialized a second **8-vertex rational own-centered wall object** with `(V,E,F,C)=(8,18,12,36)` and strict `(2,4,4)`. Its four saddle edges and two tiny additional unstable vertices resolve into two coherent degree-three endpoint-transfer blocks.
3. I independently recovered representatives of all fourteen journal-listed simplicial `V=8` graph types and fifty distinct simplicial `V=9` graph types. The latter collection is empirical; I did not generate an independent exhaustiveness certificate for the number fifty.
4. Controlled splits through `V=12` exposed a concrete obstruction mechanism: the best 12-vertex trajectory consists of two local degree-three transfer vertices. Deleting those two vertices exposes a robust 10-vertex `(2,2,2)` core whose saddle edges are `(0,4)` and `(2,5)`. Isolated caps, short rails, and endpoint stacks transfer these pairs rather than cancel them.
5. **Exact systems closed in this continuation: zero.** The inherited unresolved count remains unchanged.

## Strongest materialized near-object: exact rational `V=12`

### Exact construction and verdict

The floating search state was rationalized by rounding each uncentered coordinate to denominator `10^14`, computing its uniform-volume centroid from the complete oriented boundary, and subtracting that centroid in exact `Fraction` arithmetic. The resulting body has:

- exact uniform centroid `(0,0,0)`;
- exact volume
  `1296356029314345639362710989739353554916871 / 6000000000000000000000000000000000000000000`;
- `(V,E,F,C)=(12,30,20,60)` and Euler value `12-30+20=2`;
- every listed triangle strictly supporting, with minimum normalized nonincidence slack `5.532793302851994e-5`;
- exact strict equilibrium class **`(S,U,H)=(2,3,3)`**, hence **not** a Gömböc.

All incidence, centroid, and equilibrium signs were checked with rational arithmetic. Face stability uses exact barycentric coordinates of the perpendicular projection; vertex instability uses the exact signs of `-v·(w-v)` on every incident true edge; edge saddles use exact segment parameter `t` and exact positive-cone coefficients in the two incident outward face normals. The decimal values below are renderings only; the artifact contains every coordinate, normal, support, slack, and predicate as a reduced fraction.

### Centered coordinates

```text
 0  (-1.6168592779976956,  -0.28127395745270334, -0.71175690098767153)
 1  ( 0.98801523330563434,  0.064034551742696677,-0.14362071525207151)
 2  (-1.2412726683257056,  -0.14311995548321332,  0.32807589374326845)
 3  ( 0.098504337717214327, 0.21023673941108667,  0.098696294564448478)
 4  ( 1.8407076679021843,   0.086233892586906669,-0.05994956716225152)
 5  ( 1.2817885379895444,   0.13467473432988666,  0.47286010218840846)
 6  (-0.021826584290555669,-0.0092226029975333267,0.3980455967622985)
 7  (-0.027257720800775671,-0.014054166835083325, 0.39301483306269847)
 8  (-0.023242223226595669,-0.0013156449273733258,0.39695204420893848)
 9  ( 0.075420816634494334,-0.10220548200629333, -0.39051177607659154)
10  ( 0.083679590234634324,-0.098562110889473323,-0.39125819247388149)
11  ( 0.08431798517670433, -0.099071470344303331,-0.39141297217052151)
```

### Complete maximal-face cycles

```text
(5,4,3)   (2,3,0)   (1,0,3)   (1,3,4)
(9,0,4)   (9,2,0)   (9,4,2)   (7,4,5)
(7,2,4)   (8,5,3)   (8,3,2)   (8,2,5)
(10,0,1)  (10,1,4)  (6,5,2)   (6,7,5)
(6,2,7)   (11,4,0)  (11,0,10) (11,10,4)
```

### Complete true-edge list

```text
(0,1) (0,2) (0,3) (0,4) (0,9) (0,10) (0,11)
(1,3) (1,4) (1,10)
(2,3) (2,4) (2,5) (2,6) (2,7) (2,8) (2,9)
(3,4) (3,5) (3,8)
(4,5) (4,7) (4,9) (4,10) (4,11)
(5,6) (5,7) (5,8)
(6,7) (10,11)
```

The audit JSON gives the two incident maximal faces for every edge, so this list plus the cycles is a complete face lattice.

### Positive equilibria and nearest wall

| kind | feature | normalized margin |
|---|---:|---:|
| stable face | `(1,0,3)` | `0.15041479993271917` |
| stable face | `(9,4,2)` | `0.2778286779411772` |
| unstable vertex | `0` | `0.6955203316836567` |
| unstable vertex | `4` | `0.7406813053699614` |
| unstable vertex | `11` | `2.78800874594586e-6` |
| saddle edge | `(0,11)` | `6.606546276276092e-7` |
| saddle edge | `(4,11)` | `7.160038534614398e-7` |
| saddle edge | `(5,6)` | `5.730401913918308e-7` |
| nearest inactive edge | `(2,6)` | `-6.137727219354285e-8` |

These exact signs show a strict `(2,3,3)` body, but also show that it is a transfer-wall near-object rather than a robust candidate for rational polishing. There is no target-cell perturbation radius to report. I did **not** derive a certified coordinate radius preserving even this non-target class; the full exact sign data are supplied so a later interval calculation can do so without reconstructing the body.

### Independent verification and files

The standalone verifier uses only Python's standard library and `fractions.Fraction`; it does not call SciPy, Qhull, NumPy, or the search evaluator. Its literal output is:

```json
{"verified":true,"V":12,"E":30,"F":20,"centroid":["0","0","0"],"S":2,"U":3,"H":3,"target":false}
```

- Exact rational candidate JSON (`slot8_v12_exact_near_candidate.json`)
- Full exact face/vertex/edge/support audit (`slot8_v12_exact_near_audit.json`)
- Standalone exact verifier (`slot8_v12_exact_near_verify.py`)
- Verifier transcript (`slot8_v12_exact_near_verification.txt`)
- Vertex CSV (`slot8_v12_exact_near_vertices.csv`)
- OBJ (`slot8_v12_exact_near.obj`)
- STL (`slot8_v12_exact_near.stl`)
- V12 exact bundle (`slot8_v12_exact_near_bundle.zip`), SHA-256 `c61dd15aa38080edf0a2d46f5b955481d6d9d9b59df15260d150342ee5577d03`

## Exact `V=8` wall object

A second exactification gives a bounded simplicial rational polyhedron with exact centroid zero, exact volume
`11727885812005263097590911760433817 / 93750000000000000000000000000000000`, `(V,E,F,C)=(8,18,12,36)`, minimum normalized nonincidence slack `1.5613222555248794e-4`, and exact class `(2,4,4)`.

Its stable faces are `(2,0,5)` at `0.15799105893872503` and `(1,0,3)` at `0.15007990226579848`. Its robust unstable vertices are `0` and `5`; vertices `4` and `7` are additionally unstable by only `1.3706524649028658e-7` and `4.217674789590734e-7`. Its four saddles are `(0,7)`, `(2,4)`, `(4,6)`, and `(5,7)`, with margins from `4.205845951547612e-8` to `2.2219558612978527e-7`. The nearest inactive edge is already separated at about `-9.410809803696821e-4`. This is an exact witness of a coherent multi-transfer wall, not an open `(1,1,0)` cell.

- Exact V8 candidate (`slot8_v8_exact_near_candidate.json`)
- Full V8 exact audit (`slot8_v8_exact_near_audit.json`)
- V8 exact verifier (`slot8_v8_exact_near_verify.py`)
- V8 OBJ (`slot8_v8_exact_near.obj`)
- V8 STL (`slot8_v8_exact_near.stl`)
- V8 exact bundle (`slot8_v8_exact_near_bundle.zip`), SHA-256 `cee70381a7bd65ec6f7c2e3db8efd7f6faff350e78f6ddd36ff2525870d3f85f`

## Search coverage and falsification attempts

### Numerical work performed

- Direct own-centroid random search completed `200,000` samples for `V=9–12`; the surviving V8 log proves at least `30,730` additional samples. Every evaluation rebuilt the convex hull, integrated the volume centroid, and audited all triangular maximal faces, vertices, and true edges.
- All fourteen simplicial `V=8` graph types from the journal were independently recovered and searched with fixed-cell differentiable models. Fifty distinct simplicial `V=9` graph types were also recovered and given quick fixed-cell searches; this collection is not claimed as a new exhaustive enumeration theorem.
- Fixed-cell searches optimized the exact-in-cell centroid formula together with supporting slacks, face-projection barycentrics, vertex directional inequalities, and four edge normal-cone witnesses.
- Topology-free CMA-ES runs allowed complete hull rebuilds, row/vertex deactivation, and real circuit changes rather than staying in one triangulation.
- Controlled degree-three vertex splits produced active `V=9` and `V=12` states; the best floating V9 state was `(2,4,4)` with maximum positive saddle score `2.4903515306595736e-6`, while the exactified V12 state above reached `(2,3,3)` with maximum saddle score `7.160038534614398e-7`.
- Explicit branch experiments selected a concrete negative witness for every non-target face, vertex, and edge cone, rather than relying only on a smooth minimum surrogate.
- Nonsimplicial adjacent architectures were tested through general six-plane combinatorial hexahedra and skew prismatoids with merged maximal faces. These searches also converged to transfer walls and produced no strict target.
- From the V12 state I deleted transfer vertices `6` and `11`. The realized ten-vertex body is a robust `(2,2,2)` core with saddle edges `(0,4)` and `(2,5)`, at margins about `0.22390346` and `0.19108946`. One-point caps, two-point caps, and short one- to three-vertex rails on those edges never reduced the strict saddle count below two in the realized samples; larger rails merely transferred the block.

### What this does **not** prove

None of those nonhits is an exact infeasibility certificate. The searches sampled only portions of the continuous realization spaces and branch assignments. They do not exclude any complete `V=8` necessary system, any `V=9–12` combinatorial type, any nonsimplicial cell, or any algebraic isolated realization. I deliberately leave all numerical failures outside the exact closed count.

## Exact frontier accounting

| quantity | inherited | exactly closed here | remaining |
|---|---:|---:|---:|
| labeled necessary `V=8` systems | `24,835` | `0` | `24,835` |
| rooted automorphism orbits | `17,253` | `0` | `17,253` |
| stable-face chambers | `207,036` | `0` | `207,036` |

The same accounting is available as machine-readable JSON (`slot8_frontier_counts.json`). No lower-bound statement stronger than `V>=8` is justified by this continuation.

## Most useful continuation

The strongest concrete continuation is **not** another local split of vertices `6` or `11`. Their contraction exposes the real two-pair core. A nonredundant search should start from the exact V12/V10 data and replace the complete neighborhoods of saddle edges `(0,4)` and `(2,5)` by one connected strip or Y-patch whose branches communicate before either endpoint transfer occurs. The three first-moment equations should be imposed as hard rational/algebraic constraints while complete circuit cells are enumerated. A candidate should be accepted only after both robust core saddles disappear in the same realized cell and every new true edge has an exact negative normal-cone witness.

For the literal `V=8` frontier, the next copy should consume the inherited necessary-system enumeration directly and attach exact rational feasibility or Gordan/Positivstellensatz certificates to complete branch cells. The new V8 wall object is useful as a seed for identifying one circuit boundary, but it closes no chamber.

## Reproducibility package

- Complete combined bundle (`slot8_low_vertex_frontier_bundle.zip`), SHA-256 `1e0be26793034277cb73a1c006ad390d247c7811aa03fcf56c9835861f8bed46`
- Combined manifest (`slot8_low_vertex_frontier_manifest.json`)
- Machine-readable search report (`slot8_search_report.json`)
- Standalone Markdown handoff (`slot8_research_handoff.md`)

The combined archive contains both exact candidates, complete audits, independent verifiers and transcripts, OBJ/STL files, the unresolved-count record, representative `V=8` and recovered `V=9` graph realizations, and the principal search/evaluation scripts.
