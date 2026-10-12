# figure-0086

AI research report · 2026-08-26 UTC

---

# Rapid Atlas 90 — P17 four-support three-circuit continuation

## Determination

**No homogeneous convex polyhedral Gömböc was obtained.** I do not claim a `(1,1,0)` winner. The run’s acceptance gate remains an ordinary uniform-density finite polyhedron evaluated at its own exact volume centroid, with one stable maximal face, one unstable vertex, no saddle true edge, complete H/V and lattice data, strict open margins, an independent verifier, and matching OBJ/STL; auxiliary-center, wall-point, theorem-only, and near-solution outputs are inadmissible.

Starting from the journal’s exact P17 body, the assignment was to replace stable row `35`, extra unstable facet `[2,18,27]`, and saddle pairs `[15,27]`, `[25,32]` in one four-support operation while retaining row `27`, rebuilding the intended unstable lineage, and keeping the three uniform-volume moments hard.

The strongest fully materialized endpoint is the ordinary uniform-density rational H-polytope

```text
P15 = {x in R^3 : H_i · x <= 1, i=0,...,14}
```

with

```text
(F,E,V,C) = (15,39,26,78)
Euler      = 26-39+15 = 2
exact uniform-volume centroid = (0,0,0)
exact first moment             = (0,0,0)
exact class                    = (S,U,H)=(2,2,2)
exact volume, decimal view     = 4.028875335852742
minimum raw inactive slack     = 0.004216627886514301
minimum oriented tetra determinant = 0.016455651234222577
```

This is a genuine post-circuit endpoint, not a fixed-lattice polish. All four inserted support rows `100,101,102,103` are irredundant actual maximal faces. Complexity falls from P17’s `80` to `78`, and raw inactive separation increases by roughly a factor of six.

## What changed relative to P17

P17’s complete residual block was

```text
extra stable row:       35
extra unstable facet:   [2,18,27]
old saddle edges:       [15,27], [25,32]
protected stable row:   27
protected unstable lineage: incident to row 27
```

At exact P15:

```text
old stable row 35:             deleted/deactivated
old extra-U facet [2,18,27]:   absent
old saddle edge [15,27]:       absent
old saddle edge [25,32]:       absent
protected stable row 27:       strict
rebuilt intended U facet:      [1,27,103], strict
```

The index-zero excess transferred to a different connected block:

```text
new extra stable row:          0
new extra unstable facet:      [18,32,102]
new saddle edges:              [2,9], [26,102]
Euler excess:                  1+1-2=0
```

Thus every inherited P17 defect label was genuinely removed, but the coupled operation transferred rather than cancelled the Morse block.

# Exact finite object

## Row organization

The 15 irredundant source labels are

```text
[0,1,2,9,13,15,18,25,26,27,32,100,101,102,103].
```

Rows `100–103` are the four inserted cross-coupled supports. `generate_p15_exact.py` stores every input coefficient as binary64 hexadecimal and interprets it as its exact dyadic rational value. It then, using `Fraction` arithmetic only:

1. enumerates all feasible support-plane triples;
2. reconstructs all 26 actual vertices and their exact active triples;
3. derives all 15 maximal-face cycles and 39 true edges from raw exact incidences;
4. integrates ordinary uniform volume and all three first moments over outward maximal-face tetrahedra;
5. translates to the exact own centroid by support renormalization;
6. audits every maximal face, actual vertex, and true edge/full normal cone;
7. exports exact CSV data plus OBJ and ASCII STL.

A clean-directory regeneration check reproduces the certificate, H/V tables, incidence files, OBJ, and STL byte for byte.

## Exact first-moment identity

Let the exact precenter rows be `B_i·x <= 1`, and triangulate each actual maximal-face cycle into outward tetrahedra. Define

```text
V = (1/6)  Σ_T det(v0,v1,v2),
M = (1/24) Σ_T det(v0,v1,v2)(v0+v1+v2),
c = M/V.
```

All terms are rational. Set

```text
y   = x-c,
h_i = 1-B_i·c,
H_i = B_i/h_i.
```

Then the final body is exactly `H_i·y <= 1` and

```text
M_y = M - Vc = (0,0,0)
```

identically. There are no external cubature weights, point masses, or auxiliary mechanical centers.

# Complete exact lattice certificate

The independent verifier starts from the embedded dyadic input rows rather than importing the generator or trusting the saved lattice. It independently obtains

```text
candidate support triples checked: C(15,3)=455
actual vertices:                    26
true edges:                         39
maximal faces:                      15
Euler characteristic:               2
all active sets:                    exactly three rows
all four inserted rows:             active and irredundant
exact first moment:                 (0,0,0)
exact centroid:                     (0,0,0)
```

Every active equality vanishes exactly; every inactive H/V slack is strictly positive. The exact certificate SHA-256 is

```text
8037f2734c701815037c674e8b78bdc15448015950049850d3464dfd1432d156.
```

# Exhaustive equilibrium audit at the body’s own centroid

## Stable maximal faces

| Source row | Exact raw limiting slack, decimal | In-face Euclidean margin | Limiting row |
|---:|---:|---:|---:|
| `0` | `0.02579174675214908` | `0.06852263450849874` | `2` |
| `27` | `0.21715435337059646` | `0.22060534985945454` | `103` |

Row `27` is the preserved target; row `0` is the transferred extra stable sink.

## Unstable actual vertices

| Active source labels | Exact raw limiting derivative, decimal | Normalized cosine margin |
|---|---:|---:|
| `[1,27,103]` | `0.011782658587028304` | `0.02650129085855835` |
| `[18,32,102]` | `0.007223524618286071` | `0.025142072584409942` |

The first is the rebuilt intended unstable lineage. The second is the transferred extra unstable feature.

## Saddle true edges and full normal cones

| Incident source labels | Exact minimum component, decimal | `t` | `1-t` | Normal-cone coefficients |
|---|---:|---:|---:|---|
| `[2,9]` | `0.025778321179052915` | `0.7147187345852455` | `0.28528126541475457` | `[0.025778321179052915, 0.4754948235622219]` |
| `[26,102]` | `0.024110757930460216` | `0.9256426302634563` | `0.07435736973654376` | `[0.024110757930460216, 0.4457911058827576]` |

For every true edge the verifier reconstructs the perpendicular line parameter and both coefficients in the complete two-face normal cone. Every nonsaddle edge has an exact nonpositive limiting component.

The closest excluded witnesses are

```text
face:   row 9, cut by row 13, raw -8.919689273603508e-5
vertex: active [18,32,103], raw -1.1994244803622541e-4
edge:   [9,13], limiting cone coefficient -2.5069148643203966e-4
```

Therefore P15 is a strict open `(2,2,2)` body, not tolerance dust.

# Certified perturbation radius

`verify_coefficient_radius.py` uses outward-rounded interval arithmetic on a full 45-dimensional box: every coefficient of every precentering support row varies independently by

```text
|δB_ij| <= 3e-9.
```

For every member of that box it solves the same active triples, reconstructs the realized body, recomputes its ordinary uniform-volume centroid, translates by that centroid, and proves

```text
same (F,E,V,C) = (15,39,26,78)
same class      = (2,2,2)
all four inserted rows remain irredundant
minimum inactive-slack lower bound       0.0042164570258784728
minimum face-orientation lower bound     0.024041873674875147
minimum active-triple determinant bound  0.13994847661962750
minimum equilibrium-sign lower bound     0.00007597247827151321
```

The `3e-9` radius is certified but not claimed maximal.

# Three coupled circuit crossings

`topology_path_numeric.json` stores 37 strict globally rebuilt samples of a deterministic support homotopy from exact P17 to exact P15. Each sample recomputes the body’s integrated uniform centroid and records every active Q facet, actual P feature, and equilibrium. `verify_topology_path_numeric.py` independently replays all 37 samples. The path is a discovery/topology record rather than a root-isolating exact homotopy certificate; both endpoints and the accepted P15 chamber are separately exact/directed-certified.

The three principal quadrilateral circuits are:

## 1. Extra-U circuit `C_U={1,2,18,27}`

```text
[1,2,18] + [2,18,27]
    ->
[1,2,27] + [1,18,27]
```

The Q diagonal `[2,18]` is replaced by `[1,27]`; the inherited extra unstable P vertex/Q facet `[2,18,27]` disappears.

## 2. Arm-A circuit `C_A={9,15,27,100}`

```text
[9,15,27] + [15,27,100]
    ->
[9,15,100] + [9,27,100]
```

The Q diagonal `[15,27]` is replaced by `[9,100]`; the inherited saddle P edge `[15,27]` disappears.

## 3. Arm-B circuit `C_B={18,25,32,102}`

```text
[18,25,32] + [25,32,102]
    ->
[18,25,102] + [18,32,102]
```

The Q diagonal `[25,32]` is replaced by `[18,102]`; the inherited saddle P edge `[25,32]` disappears, while the unstable feature transfers to `[18,32,102]`.

The old stable row `35` deactivates in the coupled stellar subevent

```text
[0,9,35] + [0,25,35] + [9,25,35]
    ->
[0,9,25].
```

This deletes the old stable face but transfers the stable sink to row `0`.

# Search performed

1. **One support per old defect.** Four direct cuts were placed at the old stable foot, extra-U tangent, and two saddle cones. The inserted supports became stable sinks or split the saddle cones; typical class was `(5,3,6)`.
2. **Global witness restriction.** The row-foot witness norm/angle bound proved that old rows `34,35,36` could not be routed to row `27` by any four-row chain, forcing simultaneous deactivation rather than local polishing.
3. **Cross-coupled two-arm architecture.** The successful scaffold used

   ```text
   arm A: 9 -> 13 -> 15 -> 100 -> 101 -> 27
   arm B: 25 -> 102 -> 32 -> 103 -> 27.
   ```

   At a fixed reference point it had a unique stable sink, but its own centroid moved by norm about `0.393`; recomputing the true centroid restored an Euler-neutral block.
4. **Hard moment solve.** Fifteen coefficient controls on rows `0,2,26,18,1` solved all three uniform-volume moments while every candidate was scored only at its own integrated centroid.
5. **Irredundant deletion.** Removing obsolete row `30` preserved the post-circuit class and yielded exact P15 with larger incidence separation.
6. **Endpoint-breaking attempts.** A 48-coordinate finite-difference LP, full-coordinate differential evolution, row-scale differential evolution, and 3,494 random target-preserving perturbations found no class below `(2,2,2)`. Nearby rebuilt classes included `(2,3,3)`, `(3,2,3)`, `(2,4,4)`, `(3,3,4)`, and `(4,2,4)`.
7. **False-positive rejection.** One floating apparent success was discarded after independent hull reconstruction and correct maximal-face volume integration changed its class. No artifact from that state is retained.

# Localized obstruction

If support row `j` cuts the perpendicular foot of row `i`, then

```text
a_j·a_i > ||a_i||².
```

Thus every witness arrow strictly increases support-row norm and the directed witness graph is acyclic. If an `m`-arrow path joins radii `r0,r1`, concavity of `log(cos)` gives the necessary bound

```text
angle(a0,am) < m acos((r0/r1)^(1/m)).
```

A directed interval certificate proves:

```text
row 0 -> target row 27:
  angular separation = 164.3158503285393... degrees
  first arrow count not excluded by the bound = 25

row 2 -> target row 27:
  angular separation = 168.9661665973450... degrees
  first arrow count not excluded by the bound = 24

maximum arrows available with 15 active rows = 14.
```

For 14 arrows, row `27` would need radius at least `3.4052832462` to absorb row `0`, versus its actual `3.0036895888`, a rigorously lower-bounded increase of `13.3700%`. Row `2` requires at least `3.4137222439`, or `13.6510%`.

This rules out another appended one-to-four-row witness chain at the present endpoint geometry. Serial deletion also fails: deleting row `0` gives `(7,4,9)`, while deleting `0,2` gives `(7,2,7)`.

# Smallest genuinely new continuation

The next operation not subsumed by the failed four-support family is a **whole pentagonal-star replacement**:

1. deactivate rows `0` and `2` only inside one connected topology change;
2. replace row `0`’s complete Q star bounded by its neighbors `9,18,25,26` and the row-2 side of the fan;
3. simultaneously replace the extra-U triangle `[18,32,102]` and residual saddle sectors `[2,9]`, `[26,102]`;
4. preserve stable row `27` and the rebuilt target unstable facet `[1,27,103]`;
5. reserve three full-rank mechanically inactive controls and solve all three uniform-volume moments as dependent equations in every enumerated cell;
6. require raw inactive slack above `1e-4` before exactification.

The only smaller alternative is excluded by the witness-length certificate. A longer ascent alternative needs at least eleven additional active support vertices beyond P15 and must be coupled to the same star deactivation; a serial rail is not new.

# Reproducible artifacts

- Complete P15 exact fallback bundle (`p15_four_support_exact_fallback_bundle.zip`) — SHA-256 `5b3ec86620937b9d6869d901ce35fe71c40743457562a993d0ac074786af6579`.
- README and reproduction guide (`README.md`)
- Full exact certificate (`p15_exact.json`)
- Deterministic exact generator (`generate_p15_exact.py`)
- Independent exact verifier (`verify_p15_exact.py`)
- Exact H rows (`H_exact.csv`)
- Exact V coordinates (`V_exact.csv`)
- Maximal-face cycles (`faces.txt`)
- True-edge list (`edges.txt`)
- OBJ export (`p15_exact.obj`)
- STL export (`p15_exact.stl`)
- Full coefficient interval verifier (`verify_coefficient_radius.py`)
- Interval-radius certificate (`coefficient_radius.json`)
- Complete adjacent-cell path (`topology_path_numeric.json`)
- Independent path replay (`verify_topology_path_numeric.py`)
- Three-circuit summary (`circuit_summary.json`)
- Directed witness-length verifier (`verify_witness_length_obstruction.py`)
- Witness-length certificate (`witness_length_obstruction.json`)
- Search record (`SEARCH_RECORD.md`)
- Combined verifier script (`RUN_ALL_VERIFIERS.sh`)
- Combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)
- Integrity manifest (`manifest.json`)

Reproduction:

```bash
cd p15_four_support_exact_fallback
bash RUN_ALL_VERIFIERS.sh
```

The captured transcript ends with

```text
ALL VERIFIERS PASSED
```

The delivered result is therefore a completely exact and independently reconstructible complexity-78 post-circuit body with class `(2,2,2)`, plus a complete transfer path and a directed obstruction delimiting the next operation—not a claimed Gömböc.
