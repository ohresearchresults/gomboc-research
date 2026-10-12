# figure-0109

AI research report · 2026-08-27 UTC

---

# Complete handoff: exact cross-linked-sheet fallback, no Gömböc

## Verdict

No strict own-centroid `(1,1,0)` polyhedron was found. The strongest completed object is the exact rational endpoint **X48**, with

```text
(V,E,F,C) = (48,138,92,276)
(S,U,H)   = (2,2,2)
stable    = [0,3,1], [A12,B15,B14]
unstable  = 0, B03
saddles   = [3,16], [29,B20]
witness graph = acyclic, sinks 0 and B03
```

It is therefore a certified nonwinner, not a Gömböc and not a wall point. The acceptance gate requires an explicit finite uniform-density body evaluated at its own exact volume centroid, with strict `(1,1,0)`, complete H/V incidence and all-feature verification. :contentReference[oaicite:0]{index=0} The inherited L15 endpoint and its true-edge `[1,25]` obstruction are recorded in the journal. :contentReference[oaicite:1]{index=1}

## What was achieved

The inherited one-dimensional obstruction was replaced by a genuinely two-dimensional sheet. X48 has 41 new `A/B` vertices whose induced true-edge graph is connected, has 74 edges and cycle rank 34, including 34 transverse `A–B` edges. The sheet has 53 additional true edges to retained old vertices. It is not a serial fixed-ray continuation.

The old obstruction is genuinely destroyed:

- true edge `[1,25]` occurs only in segment-1 hull cell 0 and is deleted at exact circuit event 0;
- old vertex `25` deactivates at event 0;
- old stable face `[30,22,20]` disappears because `30` and `22` deactivate;
- old saddles `[3,23]` and `[26,27]` disappear because `23`, `26`, and `27` deactivate;
- old rows `21,22,23,25,26,27,30,31` are all inactive at X48.

The deactivation events are:

| row | event | circuit | exact isolating interval |
|---:|---:|---|---|
| 25 | 0 | `1,21,25,26` | `(7231/5000000000,14467/10000000000)` |
| 23 | 2 | `3,16,20,23` | `(15189/5000000000,30383/10000000000)` |
| 30 | 7 | `0,29,30,31` | `(360810431/10000000000,90202609/2500000000)` |
| 26 | 26 | `1,28,26,27` | `(1973698939/5000000000,3947397883/10000000000)` |
| 31 | 33 | `0,29,B18,31` | `(4681730457/10000000000,2340865231/5000000000)` |
| 22 | 50 | `16,B09,21,22` | `(385004107/625000000,6160065717/10000000000)` |
| 27 | 51 | `1,28,B09,27` | `(787005231/1250000000,6296041853/10000000000)` |
| 21 | 59 | `3,16,A07,21` | `(6536790911/10000000000,1634197729/2500000000)` |

Event 0 removes faces `[1,21,25]`, `[1,25,26]`, `[21,25,26]`, inserts `[1,21,26]`, and has primitive circuit-polynomial SHA-256 `4d501e6a59e07087c53560fed55dedee014163cc2b7d92dd0fd0275c5568cf37`.

## Exact finite endpoint

Every raw coordinate is an exact dyadic obtained by

```python
Fraction.from_float(float.fromhex(token))
```

with common denominator `2^56`. All 48 hexadecimal triples, their integer numerators, and the fully expanded own-centred common-denominator coordinates are supplied in `endpoint_exact.json`, `coordinates.tsv`, and the self-contained `RESULT.md`. The own-centred endpoint is `x_i=p_i-c`, where

```text
volume = 79535470618981627356379611357168745631133092790959
         /70152078591883340073776871970381584943484762062848

c_x = 20374489844949525303858093457706693136623631958477409982226100889
      /716391831684765379608988861575158694179628935724143255437944291328
c_y = -374932843469707803968721302748495220990967295352522828491358836257
      /22924538613912492147487643570405078213748125943172584174014217322496
c_z = -78029246505572271775209188267879166921933608383232721103873402625
      /2865567326739061518435955446300634776718515742896573021751777165312
```

After subtracting `c`, all three ordinary uniform-volume first moments are exactly zero.

All maximal faces are triangles. The complete finite data are expanded in the bundle:

- 48 active vertices: `coordinates.tsv` and `endpoint_exact.json`;
- 92 oriented maximal-face cycles: `facets.tsv` and `endpoint_exact.json`;
- 138 true edges: `edges.tsv` and `endpoint_exact.json`;
- 92 irredundant exact H rows: `H_rows.tsv` and `H_integer_rows_raw` in `endpoint_exact.json`;
- all exact face barycentric numerators, all directed vertex supports, and all four sign-equivalent normal-cone components for every true edge: `facets.tsv`, `vertex_support_audit.tsv`, `edge_cone_audit.tsv`.

The H generator is deterministic. For raw integer coordinates `P_i`, each oriented face `(a,b,c)` gives

```text
N=(P_b-P_a)×(P_c-P_a),  h=N·P_a,  N·P<=h.
```

For own-centred `x=p-c`, use `N·x<=h/2^56-N·c`. All 92 rows are irredundant.

## Exhaustive mechanics and margins

Exact rational auditing gives exactly two stable faces, two unstable vertices and two saddle edges. All other features have a strict exclusion primitive. Global lower margins are

```text
minimum stable barycentric coordinate       0.001336636413524239384715
minimum nonstable exclusion                 0.001383670539203068015122
minimum unstable normalized support         0.0005872826505221210113427
minimum nonunstable exclusion               0.0001014261777869820043415
minimum saddle component                    0.0008330097790622699498896
minimum nonsaddle exclusion                 0.00006132040084754450233562
minimum obsolete-row separation             0.01364248017002493216447
minimum active nonincident unit separation  2.317830772995639473223e-7
```

The active nonincident minimum is attained by vertex `B19` against face 29. The complete 138-edge four-component audit is in `edge_cone_audit.tsv`; it includes both endpoint parameters and both incident-normal coefficients for every true edge. No equilibrium count is inferred from selected signs.

The final directed witness graph has 111 exact arcs. A topological order is

```text
3 16 29 A12 A13 B13 B14 28 A11 B15 B12 20 B16 A10 B17 B11 B18 A09
B19 B10 B20 A08 B21 B09 A21 B22 A07 A22 B23 A06 A23 B24 A05 B08 A24
A04 B07 0 A03 B06 A02 B05 A01 B04 1 B01 B02 B03
```

and the sinks are exactly `0,B03`. The full arc list is in `witness_graph.tsv` and `endpoint_exact.json`.

## Hard-centred path and circuit evidence

The construction has two exact stages.

1. Segment 0 applies a common rational linear map `M(u)=I+u(N-I)`. Its determinant has no root on `[0,1]`; the centroid stays exactly zero. Exact isolation of 234 equilibrium primitive polynomials yields 55 mechanical walls and 56 open mechanical cells. Every complete graph is acyclic, and target stable `[0,1,3]` and target unstable `0` remain strict.
2. Segment 1 is an exact affine 56-row source path with 118 isolated circuit roots and 119 open hull cells. In every cell, the source coordinates are translated by the exact oriented-tetrahedron ordinary volume centroid before mechanics. `construction_path.json` stores the rebuilt face lattice, exact volume and moment numerators, complete witness graph, topological order and sinks at one exact rational sample in every hull cell. `target_path_certificate.json` supplies 3,612 exact Bernstein positivity checks over the complete cell intervals.

The exact verifier proves that `[1,25]` is present only in the first hull cell, is deleted at event 0, and never returns. It also verifies exact zero centered moments in every sampled cell. The full 118 circuit polynomials, rational isolating intervals, facet removals/additions and graph data are in `construction_path.json`; its SHA-256 is `f4154ee6f7902ea521dc439357757e6a37e61a3941985ab237c4e780c749ea49`.

## Certified open region

All 144 active raw source coordinates may vary independently by

```text
|δp_ij| <= 2^-54 = 1/18014398509481984 = 5.551115123125783e-17.
```

After translating every interval body to its own interval ordinary centroid, all 92 strict incidences, all face signs, every directed endpoint support, and all four edge-cone component signs on all 138 true edges are preserved. The eight obsolete construction rows are regenerated as strict convex combinations. Hence X48 lies in a certified open strict own-centroid `(2,2,2)` chamber.

## Sharp remaining obstruction

The old edge `[1,25]` is gone. The Euler-neutral obstruction transfers to the new true cross-link `[B02,B03]`. Exact own-centred supports are

```text
B02·(B02-B03)
= -122380228676825543492715375484288633540236788366453864403614306215692682880775
  /25810735889814211626091475815365210118650671531875474738039550493106373942526869504 < 0

B03·(B03-B02)
= 708611905344786811090322425232888423975861574469814755122968982545543149327879
  /25810735889814211626091475815365210118650671531875474738039550493106373942526869504 > 0

sum = ||B02-B03||²
= 28791776413248618293190401/1267650600228229401496703205376 > 0.
```

Every true-neighbor support from either endpoint to outside `{B02,B03}` is positive; the smallest normalized external support is `0.9477583726008841129899` on `B02→B01`. Consequently, throughout the whole fixed-incidence external-positive sign cell, at least one endpoint is a strict unstable vertex because

```text
x·(x-y)+y·(y-x)=||x-y||²>0.
```

Target vertex `0` is independently strict unstable, so that cell has `U>=2`. At X48 the extra unstable vertex is `B03`. The relay edge is not a saddle; its four displayed components have signs `[-,+,+,+]`.

The shortest positive-dot fixed-direction routes from `B03` to `0` have five edges:

```text
B03-A02-3-16-20-0  product lower bound 10.301156310016639
B03-A03-3-16-20-0  product lower bound 10.286031579046169
current r0/rB03                         1.1596882899672956
```

These products are diagnostic, not a global impossibility theorem. The two-vertex identity is the proof-level fixed-cell obstruction.

## Smallest remaining topology

The old `1.700624` serial-route obstruction has been bypassed. The smallest unexcluded continuation is now one nonlocal three-branch/two-cell cross-sheet event that deletes/deactivates `[B02,B03]` or gives both endpoints distinct strict negative external witnesses, while simultaneously replacing the extra stable star `[A12,B15,B14]` and saddle stars `[3,16]`, `[29,B20]`. It should permit `B02,B03,A02,A03,B04,A12,B14,B15,3,16,29,B20` and obsolete sheet rows to become interior together, add a transverse return band, and eliminate all three moments as dependent equations before every score.

## Independent verification

A fresh `verify_all.sh` run gives:

```text
V-DRIVEN PASS: 48 vertices, 138 edges, 92 faces, exact volume/centroid, class (2,2,2), acyclic sinks 0,B03
H-DRIVEN PASS: 92 halfspaces independently recover the same 48 vertices, 138 edges, 92 faces and class
INTERVAL PASS: independent coordinate box 2^-54 preserves incidence and every primitive sign
SEGMENT0-MECHANICS PASS: 55 exact walls, 56 open cells, target preserved, all graphs acyclic
PATH PASS: 118 exact circuit events, 119 hull cells, [1,25] deleted at event 0, exact moments closed
TARGET-PATH PASS: 3,612 exact Bernstein positivity checks
PAIR-OBSTRUCTION PASS: external-positive [B02,B03] component proves U>=2 in its sign cell
MESH PASS: 48 vertices, 92 triangles, 138 watertight multiplicity-two edges; centroid error 6.76e-14
```

Decisive hashes:

```text
endpoint_exact.json          7b5ff7c625019808e8ea2c7c9159544ea3ed013a73df6a4d941a9e25d0443166
construction_generator.json  5904efe38df5b6081dfb328ab1c974e94d781eab2ae771e3a17d9143a16e89b8
construction_path.json       f4154ee6f7902ea521dc439357757e6a37e61a3941985ab237c4e780c749ea49
target_path_certificate.json aa5f4a2387c8e1bcbefe1aa504c7d972bbe317e8f165d21cae7d2aa61f07c6ce
segment0_mechanical.json     06857e3105285824a62cd8a54a515165c35b5c703437133dea44b7a4720754b0
obstruction_certificate.json 3b2173d53295243fc52065ecd2c4d4a65e445b6347e744a466ecc76fcdd5ad2d
crosssheet_endpoint.obj      5f74d806d35286de25fdeafbfde9567fd3ac1ea3289a59d855fd48a86df287a4
crosssheet_endpoint.stl      d8cb2373de8baf984ef3374854e1aec42370d043f96f5a83f849157a4a5bdfd0
```

## Finite artifacts

- [Complete exact archive](sandbox:/mnt/data/l15_crosssheet_best_final.zip), SHA-256 `7d77ef35edab87166334b05dd88fc8f187c8d97bd1801d57a747d8b375e94cf0`.
- [Self-contained expanded handoff](sandbox:/mnt/data/l15_crosssheet_best_final/RESULT.md), containing all 48 coordinates, all 92 face cycles, all 138 true edges, the complete endpoint face/vertex/four-component edge audit, graph, margins and hashes.
- [Exact endpoint certificate](sandbox:/mnt/data/l15_crosssheet_best_final/endpoint_exact.json).
- [Exact 118-event construction path](sandbox:/mnt/data/l15_crosssheet_best_final/construction_path.json).
- [Exact relay obstruction certificate](sandbox:/mnt/data/l15_crosssheet_best_final/obstruction_certificate.json).
- [Complete SHA-256 manifest](sandbox:/mnt/data/l15_crosssheet_best_final/SHA256SUMS.json).
- [OBJ](sandbox:/mnt/data/l15_crosssheet_best_final/crosssheet_endpoint.obj) and [STL](sandbox:/mnt/data/l15_crosssheet_best_final/crosssheet_endpoint.stl).
- [Complete verifier transcript](sandbox:/mnt/data/l15_crosssheet_best_final/verifier_output.txt).

## Bottom line

This continuation performs a genuine macroscopic cross-linked replacement, hard moment closure, exact circuit isolation and complete endpoint reintegration. It proves that old edge `[1,25]` was deleted. It does **not** construct a Gömböc: X48 is open strict `(2,2,2)`, and the remaining sharp obstruction is the new external-positive true-edge component `{B02,B03}`.
