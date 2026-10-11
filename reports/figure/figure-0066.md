# figure-0066

Historical AI scientific report · saved 2026-08-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Outcome

No finite homogeneous polyhedral Gömböc was found in this direction. I did, however, move the ψ-ring branch from an unmaterialized construction idea to two **fully expanded exact rational polyhedra** with rebuilt incidence, exact own-centroid integration, exhaustive maximal-face/vertex/true-edge normal-cone audits, two independent exact verifiers, and matching OBJ/STL exports. This respects the run’s acceptance boundary: no auxiliary-center mechanics, no tolerance-merged incidence, and no facetwise substitute for mixed normal-cone tests. :contentReference[oaicite:0]{index=0} The construction starts exactly from the journal’s analytically centered original Sloan body and its explicit untwisted coordinate `ψ=t`. :contentReference[oaicite:1]{index=1}

**Complete reproducible archive:** [sloan_psi_ring_handoff.zip](sandbox:/mnt/data/sloan_psi_ring_handoff.zip)  
**SHA-256:** `884c84ffd873dcdabe449fb2c23e8238c88fef882e69a7f607f3c863cb668aa8`

The archive contains exact source generators, centered V and H tables, maximal-face cycles, true-edge incidence, every individual feature audit, exact volume/centroid certificates, OBJ/STL, a hash manifest, and verifier transcripts. The two exact verifiers pass from clean reconstruction:

```text
faithful_psi29 PASS VEF (29, 62, 35) class (3, 3, 4) inactive 0.010313629812503557
trimmed_psi8    PASS VEF (8, 17, 11) class (2, 2, 2) inactive 0.008797645031580974
```

# What was constructed and tried

I parameterized the original Sloan surface by

`R(t)=(1+4βt)^(1/4)`, `β=0.034`,

with the journal’s untwist

`v=(t,√(1-t²)cos λ,√(1-t²)sin λ)`, `θ=acos(v_z)`, `φ=atan2(v_y,v_x)+η(θ)`.

Analytic surface derivatives supplied tangent support rows on whole `ψ=t` rings. I then pursued two architectures.

1. **Faithful C2 architecture.** Three explicit ψ levels, four supports per level, physical lower/upper x cuts, one separate lower planar cap, and one axial apex fan. Independent ring phases were optimized rather than using a latitude-longitude or quasi-uniform mesh. Exact C2 pairing `(x,y,z)↦(x,-y,-z)` was imposed before rationalization.
2. **Trimmed asymmetric architecture.** The old lower and upper cut-boundary vertices were removed, replaced by separate lower and upper boundary rings, and C2 was broken. This produced a much smaller and mechanically more concentrated body, although the intended cap/apex equilibria migrated to side features.

Empirical searches included broad C2 ring/cap/apex perturbations, 8,000 asymmetric trimmed-ring samples across two runs, 6,000 determinant-one metric samples around the strongest eight-vertex state, local Powell/Nelder–Mead metric optimization, and 8,000 direct coordinate perturbations. None produced `(1,1,0)`. A direct coordinate continuation reduced a floating hard defect to about `0.0833`, but only by reaching a weaker `(2,3,3)` cell with normalized inactive slack `3×10^-5`; it was rejected as a fallback. These searches are evidence about the explored neighborhoods, not an exact global exclusion.

A significant exactification failure was also resolved. Quantizing the *final* floating face planes split intended nonsimple incidences, created 83 exact vertices, and drove inactive slack to approximately `10^-14`; that route was rejected. Quantizing the ring generator first, solving its vertices exactly, and only then rebuilding the final V-hull preserved the intended topology and gave the strict certificates below.

# Strongest mechanically concentrated reframe: `trimmed_psi8`

Files: [certificate](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/certificate.json), [exact vertices](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/vertices_exact.csv), [exact halfspaces](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/halfspaces_exact.csv), [maximal faces](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/maximal_faces.json), [true edges](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/true_edges.csv), [OBJ](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/polyhedron.obj), [STL](sandbox:/mnt/data/sloan_psi_ring_handoff/trimmed_psi8/polyhedron.stl).

## Exact construction

The generator hard-codes eight dyadic source vertices with common denominator `D=2^44`; the complete numerator table and the originating two-ring parameters are in `source_generator.py` and `certificate.json`. Every source point is an actual hull vertex. Exact integration gives source centroid

`(0.10033002577557198…, 2.3918283128910325…, 2.2310162024180458…)`,

with the literal rational values recorded in the certificate. The exported coordinates subtract that **exact uniform-volume centroid**, so their exact first moments are `(0,0,0)`. This is only a coordinate translation of the same uniform body, not evaluation at an auxiliary point.

## Incidence and convexity

- `(V,E,F)=(8,17,11)`, complexity `C=34`, Euler value `2`.
- Exact class at its own centroid: **`(S,U,H)=(2,2,2)`**.
- Exact volume: `673.47732763689…`; the full rational volume is in the certificate.
- Minimum nonincident vertex-to-plane geometric slack: **`0.008797645031580974`**, or `0.000472372896448214` of RMS radius.
- Every H row is an exact supporting plane of `conv(V)`. The V-driven verifier enumerates all supporting planes from all vertex triples; the independent H-driven verifier enumerates every feasible intersection of H triples and recovers exactly the same eight vertices. All inactive exact evaluations are strictly negative.

## Complete remaining equilibrium block

Face margins below are perpendicular-projection margins divided by RMS radius. Vertex margins are cosines. Edge margins are the minimum of `t`, `1-t`, and the two **unit-normal** cone-coefficient shares.

- Stable `F0=[1,6,2]`, margin **`0.151502915771119`**.
- Stable `F10=[1,7,6]`, margin **`0.159059599243727`**.
- Unstable `V1`, margin **`0.983986998286241`**.
- Unstable `V6`, margin **`0.770038292929600`**.
- Saddle `E6=[1,6]`, incident to `F0,F10`, margin **`0.409935647707188`**.
- Saddle `E12=[4,5]`, incident to `F3,F7`, margin **`0.192153345358116`**.

Every other feature has an explicit strict separator witness. The closest non-equilibrium margins are:

- face: **`-0.0618627718099109`**;
- vertex: **`-0.220336695747353`**;
- edge/full normal cone: **`-0.0550569847146886`**.

Thus this is not wall dust. Its defect is one coherent central block plus one second saddle: the two stable faces share the saddle edge `[1,6]`, and both endpoints of that edge are unstable. The other saddle `[4,5]` lies in the adjacent lower/side strip. The exact mixed-cone audit is essential here; the journal already showed why incident-facet residuals cannot certify an edge. :contentReference[oaicite:2]{index=2}

## Smallest modification not excluded

Metric-only motion and independent local moves are exhausted empirically. The smallest still-plausible operation is a **single connected two-circuit replacement spanning both saddle stars**, not another scalar ring phase or isolated point:

- replace the complete star of `[1,6]`, allowing one of `F0/F10` and one of `V1/V6` to disappear in the same circuit change;
- simultaneously replace the star of `[4,5]`, rather than transferring that saddle to a neighboring edge;
- permit deletion of one obsolete lower-boundary vertex and add approximately two connected strip vertices;
- impose the three exact first-moment equations as hard constraints during the circuit crossing.

This would most naturally search 9–10 vertices and still remain far below complexity 100. A one-edge flip or determinant-one metric cannot perform both required cancellations in the audited cell.

# Faithful requested architecture: `faithful_psi29`

Files: [certificate](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/certificate.json), [fully expanded ring generator](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/source_generator.py), [exact vertices](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/vertices_exact.csv), [exact halfspaces](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/halfspaces_exact.csv), [maximal faces](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/maximal_faces.json), [true edges](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/true_edges.csv), [OBJ](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/polyhedron.obj), [STL](sandbox:/mnt/data/sloan_psi_ring_handoff/faithful_psi29/polyhedron.stl).

## Exact generator

The three ring levels and independent phases are

```text
t = (-0.4944289900937243, -0.11947815756400615, 0.25547267496571197)
phase = (0.3655217011499099, 0.21339876168204208, 0.44633240173518907)
```

Each ring has four tangent-support directions. The exact generator stores the 14 dyadic core rows with denominator `2^44`, enumerates their 20 feasible exact triple intersections, appends eight exactly C2-paired cap vertices and one axial apex, then performs an exhaustive exact V-hull rebuild. All 29 source points remain actual vertices.

Exact C2 symmetry forces the source centroid’s y and z coordinates to zero. The remaining discretization moment is purely axial: source centroid `x=0.5039064210969553…`, represented by an exact 533-digit rational in the certificate. The exported body is translated by that exact own centroid, and every equilibrium predicate is evaluated there.

## Incidence, margins, and exact class

- `(V,E,F)=(29,62,35)`, `C=124`, Euler value `2`.
- Exact class: **`(3,3,4)`**.
- Exact volume: `16.075174024493233…`.
- Minimum nonincident geometric slack: **`0.0103136298125036`**, or `0.00426604265336884` of RMS radius.
- Closest non-equilibrium margins: face **`-0.00450940428520237`**, vertex **`-0.0225809366729990`**, edge **`-0.00816322751267908`**.

The intended equilibria survive robustly:

- dedicated lower cap `F16=[20,21,22,23,24,25,26,27]`, margin **`0.203725410531802`**;
- axial apex `V28`, margin **`0.296517214018920`**.

The complete unwanted block is:

- extra stable apex triangles `F25=[10,13,28]` and `F26=[11,12,28]`, each margin **`0.157455096966159`**;
- extra unstable vertices `V14,V19`, each margin **`0.276535893290994`**;
- lower-boundary saddle edges `[1,4]` and `[3,6]`, each margin **`0.362907635878932`**;
- apex saddle edges `[14,28]` and `[19,28]`, each margin **`0.109198795496816`**.

The C2 symmetry explains the paired defects. Broad C2 parameter searches never reduced the strict class below `(3,3,4)`. The robust positive and negative margins show that further arithmetic refinement cannot alter the class.

## Smallest faithful-architecture continuation

The exact block identifies why adding a cap outside an existing cut is insufficient: the old cut boundary remains mechanically active. The next nonexcluded faithful ψ-ring surgery is therefore:

1. delete the complete old lower x-cut boundary and make the dedicated cap boundary itself a full `ψ=t_-` ring;
2. delete the complete old upper x-cut boundary and make the apex fan base itself a full `ψ=t_+` ring;
3. break C2 only inside one connected half-strip spanning the lower and upper defect pairs, while retaining three remote exact moment controls;
4. rebuild the entire hull and re-audit every maximal face and full normal cone after each circuit change.

The `trimmed_psi8` experiment confirms that deleting the old boundaries is the correct topology-changing direction, but it also shows that unconstrained trimming lets the stable and unstable equilibria migrate away from the dedicated cap and apex. The next search must keep those two target inequalities hard while performing the connected strip replacement.

# Verification and reproducibility

Two independent exact paths are included:

1. `verify_rebuild.py`: starts from each exact source generator, enumerates every supporting plane from V triples, reconstructs actual maximal faces and true edges, integrates the exact uniform centroid, and audits all complete feature predicates.
2. `verify_independent.py`: starts from the published centered H/V tables, enumerates all feasible H-triple intersections, reconstructs the vertex set and incidence independently, integrates the exact first moments, and reclassifies every face, vertex, and complete two-normal edge cone.

Both pass; their transcripts are [here](sandbox:/mnt/data/sloan_psi_ring_handoff/verify_rebuild.log) and [here](sandbox:/mnt/data/sloan_psi_ring_handoff/verify_independent.log). No tolerance is used to decide incidence or equilibrium signs. Decimal OBJ/STL files are generated from the exact centered V tables and the certified maximal-face cycles; `SHA256SUMS.txt` binds every artifact.

A formal coordinate perturbation radius is intentionally **not claimed**, because neither body is a successful `(1,1,0)` witness. The exact strict margins do establish that the reported fallback classes are open, but the deliverable does not convert that fact into an all-coordinate box certificate.

# Bottom line for the coordinator

The ψ-ring direction did not yield a Gömböc, but it now has two reusable exact endpoints rather than another qualitative construction:

- **Best mechanical endpoint:** `trimmed_psi8`, exact own-centered `(2,2,2)`, `C=34`, robust raw incidence and one tightly localized two-circuit cancellation problem at the rigorous eight-vertex frontier.
- **Best architecture-faithful endpoint:** `faithful_psi29`, exact own-centered `(3,3,4)`, `C=124`, with the requested dedicated cap and apex preserved and all eight unwanted equilibrium features localized to four C2-paired lower/apex blocks.

The highest-value continuation is the connected two-circuit surgery on `trimmed_psi8`, with exact moment equations hard-wired and the target stable/unstable inequalities fixed. The faithful 29-vertex branch should be retained as the separator-certified ring/cap/apex reference and as evidence that merely refining or retuning the rings will not remove the boundary block.
