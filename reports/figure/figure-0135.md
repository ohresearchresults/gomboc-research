# figure-0135

AI research report · 2026-08-28 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Rapid Quartz 69 — finite AQ16 collar materialization

## Literal verdict

**The missing finite critical collar and every target/collar/background cross-seam feature were materialized and certified. The resulting complete finite body is not an own-centroid `(1,1,0)` polyhedron.**

The acceptance gate therefore remains unmet: the requested endpoint must have exactly one stable maximal face, one unstable vertex, no saddle true edges, exact own-volume centring, complete H/V incidence, positive all-feature margins, an independent verifier, and matching meshes.

This result changes the refinement-plus-Santaló diagnosis materially. The previously missing critical collar antecedent is now closed with a directed margin above `1.915868198716011e-6`. The first obstruction lies strictly outside that collar, in the deliberately coarse 16-sector noncritical angular background. That background violates the prior support-error budget by approximately `1.12952×10^6` and creates thousands of remote equilibria.

No local support controls were introduced after the hull rebuild because the actual rebuilt hull already proved that centring was not the remaining collar problem: the collar survives the exact Santaló correction, whereas the noncritical background is mechanically wrong before any three-control solve could repair it.

## Reusable artifact set

- Archive README (`README.md`)
- Deterministic finite generator (`generate_AQ16_exact.py`)
- Independent exact/directed verifier (`verify_AQ16_exact.py`)
- Machine-readable certificate (`AQ16_certificate.json`)
- Complete exact topology and coordinate arrays (`AQ16_exact_data.npz`)
- Exact Q vertex rows (`AQ16_Q_vertices_exact.csv`)
- Exact Q maximal faces (`AQ16_Q_maximal_faces_exact.jsonl`)
- Exact Q true edges (`AQ16_Q_true_edges.csv`)
- P halfspaces with Santaló root box (`AQ16_P_H_rows_root_box.csv`)
- P vertices at the root midpoint (`AQ16_P_vertices_root_midpoint.csv`)
- P maximal faces (`AQ16_P_maximal_faces.jsonl`)
- P true edges (`AQ16_P_true_edges.csv`)
- Complete collar/cross-seam mechanics ledger (`AQ16_local_collar_cross_seam_features.csv`)
- Directed collar margins (`AQ16_local_directed_margins.json`)
- High-precision Santaló enclosure (`AQ16_santalo_high_precision.json`)
- Exact root-box witness arrays (`AQ16_root_box_witnesses.npz`)
- Perturbation proof (`AQ16_perturbation_proof.json`)
- First failed background features (`AQ16_first_failed_background_features.json`)
- Q OBJ (`AQ16_Q.obj`)
- Q STL (`AQ16_Q.stl`)
- Own-centred P OBJ at the root midpoint (`AQ16_P_at_santalo_midpoint.obj`)
- Own-centred P STL at the root midpoint (`AQ16_P_at_santalo_midpoint.stl`)

The individual files form the complete result archive; a monolithic ZIP was not generated in this turn.

---

## 1. Exact finite generator

The smooth source is

```text
R(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-P(theta)),
beta = 1/160,
P(theta) = eta(theta) - (1/3) sin(3 eta(theta)),
eta(theta) = (3 pi/2)(cos(theta)-cos(theta)^3/3).
```

Every final Q coordinate is dyadic with common denominator

```text
D = 2^118
  = 332306998946228968225951765070086144.
```

### Exact target rows

The stable square is the four-point face

```text
(330241653278860971071379575221098836,
 ±649037107316853453566312041152512,
 ±649037107316853453566312041152512) / D.
```

The unstable apex is

```text
(-334416990645408040140947785717004757,0,0) / D.
```

### Graded critical collar

The collar uses 16 fixed azimuthal rays and 372 critical rings

```text
gamma_j = 0.0005·1.01^j,
```

with the final ring set exactly to `gamma=0.02`. This gives `5,952` collar rows.

For each ray, construction starts at the exact apex. Given the smooth polar contact `q` and the preceding finite point `p_prev`, the largest scale `s≤1` is selected such that

```text
p = s q,
p·(p_prev-p) >= 1.1·m0·||p_prev-p||,
m0 = 1.915868198716011e-6.
```

The minimum selected scale is

```text
0.9999998757249214,
```

and every ring is full-scale from

```text
gamma = 0.01532930924647033
```

onward.

This graded recurrence explicitly bridges the annular and rectangular-corner sectors that were missing from the prior quantitative theorem.

### Finite noncritical background

The materialized test background begins at `gamma=0.0202`, ends at `pi-0.012`, and has 984 rings with meridional steps at most `0.004`. Each ring retains the same 16 azimuthal rays, giving `15,744` background rows.

Together with the four square rows and apex, the exact Q generator has

```text
5,952 + 15,744 + 4 + 1 = 21,701 rows.
```

The generator independently reproduces all `21,701` stored integer triples, performs the exact topology repair, and reports:

```text
status                         PASS
dyadic rows match archive     true
collar rings                   372
background rings               984
exact diagonal repairs         533
Q f-vector                     (21701,65096,43397)
triangulation matches archive  true
maximal faces match archive    true
```

## 2. Exact inside-source checks

Each non-target smooth contact coordinate is rounded to a binary64 multiple of `2^-64` and multiplied by `1-2^-54`. The resulting exact numerator is

```text
round(2^64 x)·(2^54-1),
```

with denominator `2^118`.

The directed bounds are

```text
Euclidean coordinate-rounding error <= 4.6947331210536274e-20,
radial shrink support slack          >= 5.516952792557391e-17,
net guaranteed interior slack        >= 5.512258059436337e-17.
```

Thus every collar and background row is strictly inside the smooth source polytope. The square rows lie inside by the rolling-ball cross-section estimate, and the apex has inward error greater than `5.58e-17`.

## 3. Rigorous lower bound on collar depth

A single plane at the old depth cannot bridge the first rectangular corner sector.

The exact finite estimates are

```text
old plane depth tau                     = 6.103515625e-5,
first corner outer radius lower         = 0.01177862,
first corner outer depth upper          = 6.9385e-5,
required extreme-plane radius lower     = 0.010361171897519277,
rolling-ball inside radius upper        = 0.007866760651449969.
```

Therefore

```text
required/available = 1.317082387095322,
absolute gap       = 0.0024944112460693075.
```

This proves that at least one shallower transition layer is necessary. The 372-ring recurrence is not gratuitous refinement: it supplies the missing depth hierarchy demanded by this finite obstruction.

---

## 4. Actual exact incidence

Binary64 Qhull initially chooses incorrect diagonals in extremely shallow dyadic quadrilaterals. Treating that triangulation as exact would give false incidence and mechanics.

The archive therefore applies exact integer 4-point orientation predicates to every shared triangle edge. A positive local-convexity violation triggers an exact 2–2 flip. The process performs 533 flips without moving any coordinate.

The repaired sphere has

```text
Q vertices             21,701
Q triangulation faces  43,398
Q maximal faces        43,397
Q true edges           65,096
Euler value            2
```

All `21,701` rows are irredundant. The only exact coplanar triangulation diagonal is

```text
(21697,21698),
```

which lies inside the stable square and is removed from the true-edge list.

The smallest exact adjacent-plane distance is

```text
2.939343779797856e-18,
```

at edge `(166,181)`. The smallest physical tetrahedral orientation magnitude is

```text
3.464902217509549e-27.
```

The Santaló-centred polar has the dual f-vector

```text
P vertices = 43,397
P edges    = 65,096
P faces    = 21,701.
```

The exported OBJ and STL meshes are watertight: every triangulation edge occurs exactly twice.

---

## 5. Directed normalized Santaló root

The high-precision midpoint is

```text
( 0.00007229882669645963079431975628605771664124,
 -1.42276319590704674115879260205e-17,
 -6.3002029709899317623618849681e-18 ).
```

At this midpoint the polar has

```text
volume =
4.242898963670743475039680530044790102334819029626607995875390039723005
```

and first moment

```text
( 5.6543851999623881483328332758735005e-32,
 -1.4416029272385723231448134996798875e-33,
  1.6363260709029697311237482452286740e-33 ).
```

The scale-invariant residual is

```text
||M||/V = 1.3336610365653016435239943778963036e-32.
```

Additional directed data are

```text
||F||                         = 2.263435611972387145312393710890219e-31,
strong-monotonicity lower     = 16.22734043243270459653289820018515,
root Euclidean-ball radius    = 1.3948284510310643596281417466596843e-32,
certified coordinate-box      = 1e-30,
projective denominator range  =
[0.97642146402350052854496188694716145,
 1.00642169393306487083814929467693886].
```

Every denominator is strictly positive. Positive definiteness of the Santaló Jacobian gives global uniqueness of the root.

---

## 6. Literal collar and cross-seam all-feature audit

A collar feature means any actual maximal face, actual vertex/full normal cone, or true edge meeting one of the 5,952 collar rows. The seam with the first background ring is included. The target square and apex stars are included separately.

The verifier uses exact affine predicates over the entire `1e-30` Santaló coordinate box:

- maximal-face boundary primitive `det(E,c-U,N)`;
- vertex primitive `-(V-c)·E` for every true neighbor;
- edge projection primitives at both endpoints;
- both exact full-normal-cone coefficients for every true edge.

It does not use per-triangle residuals, a selected incident facet, or a triangulation diagonal.

### At the construction centre

There are no unwanted collar equilibria:

```text
extra collar stable faces     0
extra collar unstable vertices 0
extra collar saddle true edges 0
```

Directed lower margins are

```text
maximal-face exclusion  2.15496918637399912e-5,
vertex exclusion        2.10742761577035089e-6,
true-edge exclusion     2.10742761577035089e-6,
stable-square margin    0.001953125,
apex unstable margin    0.000502056565831938452.
```

### Throughout the Santaló root box

Again there are no unwanted collar equilibria:

```text
extra collar stable faces      0
extra collar unstable vertices 0
extra collar saddle true edges 0.
```

The directed root-box lower margins are

```text
maximal-face exclusion  2.15864675983227834e-5,
vertex exclusion        2.14352396601548059e-6,
true-edge exclusion     2.14352396601548059e-6,
stable-square margin    0.00195312499999998569,
apex unstable margin    0.000502092634911042134.
```

The weakest collar margin is therefore

```text
2.14352396601548059e-6
  = 1.1188264242 · 1.915868198716011e-6.
```

This is the central positive result: **the complete finite critical collar, its annular/corner sectors, every nonsimple full vertex cone, and every true cross-seam edge remain in the intended strict chamber after exact own-centroid correction.**

---

## 7. Complete global mechanics

The full exact Q class at the construction centre is

```text
(S,U,H)_Q = (899,3469,4366).
```

Throughout the Santaló root box it is

```text
(S,U,H)_Q = (889,3473,4360).
```

Polarity therefore gives the exact own-centred class of

```text
P = (Q-s(Q))^circ
```

as

```text
(S,U,H)_P = (3473,889,4360).
```

This is a decisive, well-separated nonwinner rather than a near-wall false positive.

## 8. Exact failed support inequalities

The local target and collar support deficits remain small:

```text
target critical L1 upper = 3.1335450593497304e-7,
collar L1 upper          = 1.6057666106487806e-10.
```

The 16-sector background has angular half-cell radius

```text
sqrt((pi/16)^2+0.002^2)
  = 0.19635972650152908.
```

Its directed support-error bounds are

```text
pointwise upper     = 0.028171692124538183,
background L1 upper = 0.35401592407057036.
```

Against the prior level-20 budget

```text
3.1342152657311286e-7,
```

this is a violation factor of

```text
1,129,520.1320129742.
```

The actual Santaló displacement is

```text
7.229882669645962e-5,
```

or `37.73684784000972` times the prescribed common margin. The collar nevertheless survives because its directed geometry is much better than the global isotropic estimate. The previous conditional level-20 support/Santaló theorem is simply inapplicable to this coarse background.

### First actual failed background features

At the construction centre, the first false unstable vertices occur in azimuth sectors `k=6` and `k=14` at

```text
gamma = 0.0405366200415868,
rows  = 7078 and 7086,
margin = 6.5207011338e-7.
```

They are paired with the first longitudinal saddle true edges, centered near

```text
gamma = 0.04033594370474726,
```

with the same positive primitive. The first false stable faces appear near

```text
gamma = 1.3170576220091166
```

with margin about `1.18850e-5`.

At the Santaló root, the first false unstable pair has moved only to

```text
gamma = 0.04176492016546692,
```

and the paired saddle edges have mean gamma

```text
0.04155816313494481.
```

Thus the obstruction is not hidden inside the target collar and is not caused by the Santaló translation. It is the first coarse noncritical angular strip.

---

## 9. Perturbation certificate

The exact coordinatewise perturbation radius is

```text
|delta q_ij| <= 2^-200
             = 6.223015277861142e-61.
```

The derived point radius is `1.0778578637532851e-60`. Directed multilinear changes are bounded by

```text
degree-2 primitive       4.3389651185711454e-60,
degree-4 face/cone       3.515459171698177e-59,
degree-5 edge denominator 1.768795729152387e-58,
orientation              2.619816289311992e-59,
face normal              8.677618089504948e-60,
edge vector              2.1557157275065702e-60,
Santaló-root displacement 3.765034718994071e-60.
```

The exact witness minima are

```text
topology orientation     3.464902217509549e-27,
triangle-normal norm     9.56513414573103e-10,
edge length              4.999487586148764e-6,
degree-2 witness         1.0718286128915981e-11,
degree-4 witness         4.145725753893034e-18,
degree-5 edge denominator 1.6259421822634266e-34.
```

The smallest safety ratio is still approximately `9.19×10^23`. The root remains inside the certified `1e-30` box. Hence the complete f-vector, Santaló isolation, local collar result, and global nonwinner class persist throughout a nonzero exact coordinate box.

The very small coordinate radius is caused by shallow exact dyadic background circuits, not by a small mechanical collar margin.

---

## 10. Independent reconstruction

Running

```bash
cd RQ69_AQ16_exact_collar
python generate_AQ16_exact.py
python verify_AQ16_exact.py
```

reproduces the exact coordinate table, repairs the exact incidence independently, reconstructs both dual lattices, reevaluates the normalized Santaló equations, checks the coordinate root box and positive denominators, classifies every maximal face, vertex/full tangent cone, and true edge/full normal cone, verifies the collar margins and `2^-200` perturbation box, and audits both meshes for watertightness.

The verifier returns

```text
status                    PASS
Q f-vector                (21701,65096,43397)
P f-vector                (43397,65096,21701)
root ball radius          1.3948284510310643596e-32
Q root-box class          (889,3473,4360)
own-centred P class       (3473,889,4360)
local collar extras       (0,0,0)
local root-box minima     (2.1586467598322783e-5,
                           2.1435239660154806e-6,
                           2.1435239660154806e-6)
coordinate perturbation   2^-200.
```

## 11. Attempt to break the conclusion

Three possible false explanations were checked and rejected:

1. **The coarse background equilibria are not triangulation artefacts.** All coplanar pieces were grouped into actual maximal faces, the square diagonal was removed, and all saddle counts use only true edges.
2. **They are not a floating Santaló-root error.** The normalized moment residual is approximately `1.33e-32`, the unique root lies in a `1e-30` coordinate box, and every relevant feature sign is interval-evaluated over that entire box.
3. **They are not leakage from the critical collar.** The complete collar/cross-seam audit has no extra equilibrium and retains a factor `1.1188` reserve over the prescribed margin. The first failed U-H pair is separated from the collar and begins near `gamma=0.0401`.

The negative global verdict is therefore robust.

---

## 12. Smallest geometry change now capable of succeeding

Do not deepen the critical collar, add a global axial correction, or append another cumulative axial rail. Those operations attack quantities already certified or repeat the measured `90.6645×` scaling failure.

The smallest evidence-directed continuation is:

1. Freeze the exact square, apex, all 5,952 collar rows, and the first seam ring.
2. Refine only azimuth sectors `k=6` and `k=14`, beginning with the cells between approximately `gamma=0.0401` and `0.0418`.
3. Replace each offending 16-sector cell by half-sector rays, producing a local `16→32` angular transition with explicit cross-links. Enumerate every transition circuit exactly; a nominal adaptive diameter estimate is insufficient.
4. Add the half-turn-paired return block at the same event so its weighted degree-one/projective response vanishes to first order. This prevents the local correction from recreating the cumulative axial Santaló mismatch.
5. Propagate angular refinement only while the exact active-star common separator fails. The next independent target is the false-stable band near `gamma=1.3170576220`; it should not be refined pre-emptively everywhere.
6. After the actual adaptive hull is rebuilt, introduce three local support coefficients as dependent normalized Santaló controls. Isolate the root inside one actual incidence chamber and re-run the complete exact feature audit.

The quantitative acceptance requirements for the next object are now literal:

```text
all new/transition face, vertex and edge exclusions
    > 1.915868198716011e-6;
background total L1 support deficit
    < 3.1342152657311286e-7;
all projective denominators
    > 0;
actual own-centred class
    = (1,1,0).
```

## Final status

- **Finite critical collar:** completed.
- **All annular and rectangular-corner sectors:** explicitly bridged.
- **Actual collar maximal faces/full vertex cones/true edges:** completely audited.
- **Collar margin after Santaló correction:** `2.14352396601548059e-6`, above the required margin.
- **Directed Santaló root:** isolated uniquely with normalized residual about `1.33e-32`.
- **Expanded exact H/V incidence:** completed for both Q and its own-centred polar P.
- **Perturbation box:** `2^-200` coordinatewise.
- **Independent verifier and watertight meshes:** completed and passing.
- **Accepted own-centroid `(1,1,0)` polyhedron:** not obtained.
- **Strongest finite endpoint:** exact Q/P pair with own-centred P class `(3473,889,4360)`.
- **Exact dominant obstruction:** coarse noncritical angular coverage, beginning with a strict paired U-H birth in sectors `6` and `14` outside the completed collar.
- **Most useful continuation:** a locally moment-balanced `16→32` adaptive angular transition at that first pair, followed by exact chamber-by-chamber refinement rather than global level-20 materialization.
