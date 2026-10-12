# figure-0122

AI research report · 2026-08-27 UTC

---

# Fixed-cover Santaló-centred SPD orbit: exact wall system, certified global collars, and the remaining compact core

## Literal determination

**No strict own-centroid `(S,U,H)=(1,1,0)` metric image has been certified in the fixed 4,324-row lattice.** The best exact metric image remains the open dyadic `(2,2,2)` chamber around `A0`. I do **not** claim a global fixed-lattice impossibility theorem: the certified work excludes both noncompact spectral ends, a near-isotropic region, and one connected finite tube, but leaves an explicit bounded five-dimensional spectral core unresolved.

This is materially stronger than the state recorded when the full-orbit copy failed at the lifecycle layer: the journal then had only the Santaló root, the open `A0` chamber, and an unproved global complement. The supplied acceptance gate also forbids treating a wall point, auxiliary centre, or unmaterialized theorem as the target.

The exact result now available is therefore the strongest permitted fallback in the assignment: a complete algebraic wall description, an exact connected exclusion containing `A0`, two global spectral-collar branch-and-bound covers, a global near-isotropic exclusion, and a precise boundary separating proved and unresolved parts of the SPD quotient. The recovered exact handoff states the same literal nonwinner verdict and compact-core conclusion.

## 1. Exact Santaló-centred body and invariant lattice

The normative support rows are

```text
q_i = 2^-48 Qint_i,  i=0,...,4323.
```

The globally unique Santaló point is isolated in the dyadic box

```text
a_c = 2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856)

X = a_c + [-2^-90,2^-90]^3.
```

Numerically,

```text
a_* ≈ (-0.03000124168057219827924251765521362054304,
        0.00000000000006664142953109821117263769920,
        0.00000000000061647927749850686002592625519).
```

A strict interval Krawczyk inclusion isolates the zero of the exact polar first-moment map; positive Jacobian/Hessian bounds and strict convexity of polar volume give global uniqueness. Put

```text
Q_* = conv{q_i-a_*},
P_* = Q_*^circ.
```

Then `P_*` has exact ordinary uniform-volume centroid zero. Translation of `Q` preserves its face lattice, all projective denominators stay positive on `X`, and the irredundant primal lattice is exactly

```text
maximal faces / H rows = 4,324
vertices               = 8,644
true edges              = 12,966
Euler V-E+F             = 2.
```

At the identity metric its exhaustive class is `(2799,2881,5678)`.

For every invertible linear map `A`,

```text
∫_(A P_*) y dy = det(A) A ∫_(P_*) x dx = 0,
```

so the ordinary centroid remains exactly zero. An invertible map also preserves the complete H/V incidence lattice. The exact transformed data are

```text
h_i^A = A^-T(q_i-a_*),
v_f^A = A y_f/(1-a_*·y_f),
```

where each baseline `y_f` is the exact rational vertex reconstructed from its active support triple.

## 2. Five-dimensional determinant-normalized quotient without redundant rotations

Write the polar decomposition of a general invertible map as `A=R S`, with `R` orthogonal and `S` symmetric positive definite. The left factor `R` merely rotates the entire body, and a positive scalar multiple of `S` merely rescales it. Hence the mechanical quotient is represented without redundancy by

```text
K = A^-1 A^-T ∈ SPD(3)/R_{>0},
G = K^-1 = A^T A.
```

A bijective determinant-one five-parameter algebraic chart is

```text
K = [[x,a,b],
     [a,y,c],
     [b,c,z]],

Δ = x y-a^2 > 0,
z = (1+x c^2+y b^2-2abc)/Δ,
x > 0.
```

Its leading principal minors are `x`, `Δ`, and `det K=1`; Sylvester's criterion therefore proves `K>0`. Conversely every determinant-one SPD matrix has unique coordinates `(x,y,a,b,c)` in this chart. The unique determinant-one SPD image is `A=K^-1/2`.

For interval chamber decomposition it is more convenient to impose `trace K=1`. Every wall sign below is homogeneous in `K`, so determinant-one and trace-one gauges describe exactly the same five-dimensional quotient.

## 3. Complete exact algebraic wall arrangement

Let

```text
b_i = q_i-a,
d_f = 1-a·y_f > 0,
x_f = y_f/d_f,
J = adj(K).
```

Here `a` ranges over the isolated Santaló box, every `q_i` and `y_f` is exact rational, and `J/det K=K^-1`. The following functions exhaust every metric wall because the face lattice is fixed under the SPD orbit.

### 3.1 Face walls

For every ordered adjacent-face pair `(i,j)`, define

```text
S_ij(K,a) = b_i^T K(b_i-b_j)
          = b_i^T K(q_i-q_j).
```

Face `i` is strictly stable exactly when `S_ij>0` for every adjacent face `j`. Each `S_ij` is linear in the six symmetric entries of `K` and affine in `a`; after substitution into the determinant-one chart and multiplication by the positive denominator `Δ`, it is an exact polynomial wall.

### 3.2 Vertex walls

For every ordered adjacent-vertex pair `(f,g)`, the primitive condition is

```text
U_fg = x_f^T K^-1(x_f-x_g).
```

Clearing only positive denominators gives the exact algebraic wall numerator

```text
W_fg(K,a)
 = d_g y_f^T J y_f - d_f y_f^T J y_g.
```

`W_fg` has the same sign as `U_fg`. Vertex `f` is strictly unstable exactly when every outgoing `W_fg` is positive. In trace-one coordinates these are quadratic hypersurfaces in `K`; in the determinant-one rational chart they become polynomial after clearing powers of the positive `Δ`.

### 3.3 Full four-component true-edge cone

For a true edge with endpoints `(f,g)` and incident faces `(i,j)`, the closest point is a strict saddle exactly when all four components are positive:

```text
S_ij(K,a) > 0,
S_ji(K,a) > 0,
W_fg(K,a) > 0,
W_gf(K,a) > 0.
```

The first pair places the perpendicular foot in the relative interior of the two-normal cone; the second pair places it in the relative interior of the edge segment. Thus every saddle birth, death, or transfer occurs on one of those four exact walls—no facetwise surrogate is used.

The fixed lattice has

```text
25,932 ordered face walls  S_ij,
25,932 ordered vertex walls W_fg,
51,864 unique algebraic walls total,
12,966 true-edge cones using four components each,
103,728 feature-component incidences in the exhaustive audit.
```

The supplement contains a complete index map from every directed wall and every true edge to its exact support/vertex labels. The compact handoff's shorter wall equations agree with these formulas.

## 4. Best exact metric endpoint: the open `A0` chamber

The exact symmetric map is

```text
            1  [ 4281  -1099   2522 ]
A0 =      ---- [ -1099   2157   -388 ]
           4096[ 2522   -388  10084 ].
```

Its leading principal minors are

```text
4281/4096,
2006579/4194304,
17181037455/17179869184,
```

so it is SPD. Its determinant is the last rational number above. A literal determinant-one representative of the same metric chamber is

```text
A0_hat = (17179869184/17181037455)^(1/3) A0.
```

Uniform scaling changes no equilibrium sign. Varying all six independent symmetric entries of `A0` by

```text
|ΔA_ij| <= 2^-26
```

while simultaneously varying `a` over the full Santaló box gives zero interval straddles and the strict own-centroid class

```text
(S,U,H)=(2,2,2).
```

The exact positive features and their complete limiting intervals are:

```text
stable row 1455:
  [0.0014998673448150079239027387956184612,
   0.0014999556539562015552990992262039072]

stable row 2805:
  [0.0011027582725084432348910956633858405,
   0.0011028442781363121186211095903217938]

unstable vertex 908, three cone coefficients:
  [3.0392145408272894790968621236970648,
   3.0392157443269542937969163176603615]
  [4.2224186714564719835607320419512689,
   4.2224553257415582407929832697845995]
  [0.058280416878978620609519367690154468,
   0.058316522025747004331908129870498669]

unstable vertex 3539, three cone coefficients:
  [1.1182499201890878648413263363181613,
   1.1182606154848404589330357339349575]
  [4.9420936713059351319543566205538809,
   4.9421208389178756803516989748459309]
  [1.3621541170454021241198461211752146,
   1.3621877095286101244653309549903497]

saddle edge 2363, four cone components:
  [0.44527643869154903688567515018803533,
   0.44840458275193323389729016525961924]
  [0.42183521988718436501741848587698769,
   0.42486517167086956803245811897795647]
  [0.88702903877672178989399753845646046,
   0.92958255970703818071854129811981693]
  [0.070417440292961860914822125323553337,
   0.1129709612232782517393658849869098]

saddle edge 10407, four cone components:
  [0.17560567557939554816925920022185892,
   0.1787544822578011893821070543708629]
  [0.68248333098533886520442592882318422,
   0.68828866562596147105068666860461235]
  [0.87506382576576269283208375782123767,
   0.93430503272652121182773043983615935]
  [0.065694967273478746538906136720470386,
   0.12493617423423730716791624217876233].
```

The immediate transfer guards are

```text
row 2840:
 [-0.00038560967221141557352906414912752098,
  -0.00038552340481854492550833901631790468]

vertex 907:
 [-0.050472507096726203223990836477241828,
  -0.050436760863160859380549538855120772]

edge 10513, four components:
 [-0.021109705099269553824070655423383869,
  -0.020888692700865487544836796018898895]
 [0.88317695208800095496570747855002992,
  0.88380630671232784933977200125809759]
 [0.54493783734065770474330747674684972,
  0.5788516607689204729325638254522346]
 [0.4211483392310795270674361745477654,
  0.45506216265934229525669252325315028].
```

The minimum all-feature sign clearance of the chamber is therefore

```text
0.00038552340481854492550833901631790468.
```

The complete 4,324-face, 8,644-vertex, and 12,966-edge ledgers—not only these limiting entries—are included in the exact bundle. The recovered certificate records the same positive features and open box.

## 5. Certified global exclusion over the SPD quotient

Let the ordered eigenvalues of the inverse metric be

```text
λ1 >= λ2 >= λ3 > 0.
```

### 5.1 Stable rank-one spectral collar

For a nonempty subset of support rows `C`, if every directed boundary primitive `S_ij` from `C` to its complement is positive, then `C` contains a strict stable face. Indeed, choosing `i∈C` maximizing `b_i^T K b_i` gives, for every internal neighbor `j`,

```text
2 S_ij
 = b_i^T K b_i-b_j^T K b_j+(b_i-b_j)^T K(b_i-b_j) > 0,
```

while outward directions are positive by hypothesis. Two disjoint certified subsets force `S>=2`.

An exact dyadic projective cover of every dominant eigendirection proves

```text
λ2/λ1 <= 1/32  ==>  S>=2.
```

Certificate size:

```text
7,013 exact dyadic direction centres,
9,024 projective cover leaves,
maximum subdivision level 9,
1,708,848 complete outward boundary checks,
minimum boundary lower bound 3.3839100674639865e-9,
minimum projective-cover slack 3.645924117204266e-7.
```

This is a global all-orientation branch-and-bound collar, not sampling.

### 5.2 Unstable rank-one spectral collar

The identical subset-maximum identity on the complete primal vertex graph, using `W_fg` and `G=K^-1`, proves that two disjoint vertex subsets with positive outward primitives force `U>=2`. A second exact projective cover proves

```text
λ3/λ2 <= 19/64  ==>  U>=2.
```

Certificate size:

```text
5,309 exact dyadic direction centres,
5,667 projective cover leaves,
maximum subdivision level 8,
826,913 complete outward boundary checks,
minimum boundary lower bound 3.0762240707031665e-9,
minimum projective-cover slack 3.6123677848126323e-6.
```



### 5.3 Global near-isotropic exclusion

For `I<=H<=κI`, the exact extremal formula

```text
min u^T H v
 = ((1+κ)u·v+(1-κ)||u||||v||)/2
```

certifies two disjoint stable subsets throughout

```text
cond(K)=λ1/λ3 <= 17179/16384.
```

The independent ledger has 348 complete boundary primitives and minimum doubled-form lower bound `2.458149196715884e-7`.

### 5.4 Connected finite tube containing `A0`

A separate exact connected exclusion consists of

```text
23 trace-one dyadic inverse-metric centres,
23 full-dimensional relative-condition balls,
22 rigorously sandwiched affine-invariant geodesic segments,
46 disjoint stable-subset cones,
10,618 outward interval boundary checks.
```

Every point in the union has `S>=2`; the minimum uniform lower bound is `7.312348300660213e-6`. The tube contains `A0` and reaches a metric of numerical condition about `119049.49`. This proves a connected no-winner component around the known chamber, although it is not a complete chamber atlas of the quotient.

The two spectral collars plus the isotropic certificate contain `2,536,109` new independent boundary checks; including the connected tube gives `2,546,727` certified checks.

## 6. Exact boundary between proved coverage and the unresolved SPD region

Any fixed-lattice winner not already excluded must satisfy simultaneously

```text
λ2/λ1 > 1/32,
λ3/λ2 > 19/64,
λ1/λ3 > 17179/16384.
```

The first two inequalities imply

```text
λ3/λ1 > 19/2048,
λ1/λ3 < 2048/19.
```

After `trace K=1`, they also imply

```text
λmin(K)=λ3 > 19/4115.
```

Therefore the exact unresolved domain is

```text
trace(K)=1,
17179/16384 < cond(K) < 2048/19,
λ2/λ1 > 1/32,
λ3/λ2 > 19/64,
λmin(K) > 19/4115,
```

with the certified 23-ball/46-cone tube removed.

This is a bounded, full-dimensional semialgebraic core. It has **not** been covered by a finite interval cell decomposition and has **not** been proved empty. Consequently:

- the fixed lattice is not globally excluded;
- no winner is known in the fixed lattice;
- no claim about the whole SPD orbit is made outside the certified union;
- point sampling and unconstrained local optimization are not used as evidence.

This exact compactification and its nonexistence boundary are stated in the recovered handoff.

## 7. Verification, irredundant expansions, and meshes

The exact global bundle contains:

- the 4,324 integer support rows and 8,644 exact active triples;
- all 4,324 maximal-face cycles;
- all 12,966 true edges with endpoint and incident-face data;
- full interval ledgers for every face, vertex, and true edge at identity and `A0`;
- the Santaló Krawczyk certificate;
- the exact spectral-collar, isotropic, and finite-tube atlases;
- clean-room verifiers that reconstruct the lattice and do not trust stored equilibrium labels;
- matching midpoint OBJ/STL files.

The meshes have

```text
vertices              8,644
boundary triangles   17,284
triangulated edges   25,926
edge multiplicity         2
true polyhedral edges 12,966.
```

The archived complete independent verifier transcript ends in `PASS`. In this turn I freshly reran the global synthesis, near-isotropic verifier, finite-tube verifier, and the new complete wall-index verifier; all passed. The two very large projective-atlas verifiers are preserved with their complete archived PASS transcripts rather than represented as freshly replayed to completion. The verifier and mesh inventory is documented in the exact handoff.

Artifacts:

- Exact fixed-cover SPD global-frontier bundle (`Bright_Atlas_91_fixed_cover_SPD_global_frontier.zip`)
- Exact determinant chart and complete wall-system supplement (`Bright_Atlas_91_SPD_wall_system_supplement.zip`)
- SHA-256 checksums (`Bright_Atlas_91_SHA256.txt`)
- A0 midpoint OBJ (`metric_A_midpoint.obj`)
- A0 midpoint STL (`metric_A_midpoint.stl`)
- Santaló-centred midpoint OBJ (`santalo_centered_midpoint.obj`)
- Santaló-centred midpoint STL (`santalo_centered_midpoint.stl`)

Bundle SHA-256:

```text
0f7f44f05688ac3f1102c23d2ea02a0854dcd454e8b9e60a319b24bd5476efb7
```

Wall supplement SHA-256:

```text
b7eb42d9f9c502640bd89212963294132890437cf42fbb109483812fc9236c72
```

## 8. First topology-changing extension beyond the SPD orbit

A topology change is **not yet logically justified**, because the compact SPD core remains unresolved. The mathematically prior continuation is an adaptive exact branch-and-bound on that core:

1. use the supplied stable/unstable subset cones as the initial certificate library;
2. certify each trace-one cell by two stable subsets, two unstable subsets, or one complete all-feature sign chamber;
3. otherwise bisect at the first exact `S_ij=0` or `W_fg=0` wall;
4. exactify and fully audit any apparent `(1,1,0)` cell;
5. claim fixed-lattice exclusion only after every compact-core cell is certified.

Conditional on a later global exclusion of that core, the first locally minimal topology-changing target around `A0` is a **simultaneous multi-star replacement**, not a single flip: remove the unwanted stable row `2805`, unstable vertex `908`, and saddle edges `2363` and `10407` while preventing transfer to guard row `2840`, guard vertex `907`, and guard edge `10513`. The complete affected stars must be changed together while preserving target stable row `1455` and target unstable vertex `3539`. This is the first extension identified by the exact local wall ledger, but it is conditional—not a proved global necessity. The earlier exact handoff likewise identifies the four blockers and immediate guards as the smallest adjacent target.

## Final disposition

- **Winner:** none certified.
- **Exact own centering:** proved for the isolated Santaló body and every linear image.
- **Exact fixed lattice:** `(H,V,E)=(4324,8644,12966)` throughout the SPD orbit.
- **Best open endpoint:** determinant-normalized image of `A0`, strict `(2,2,2)`.
- **Certified exclusion:** both noncompact spectral collars, the near-isotropic region, and the connected finite tube containing `A0`.
- **Unresolved:** the explicit compact trace-one five-dimensional core above.
- **Global fixed-lattice impossibility:** not proved.
- **Topology-changing extension:** deferred until the compact core is covered; conditional coupled four-block/three-guard replacement specified above.
