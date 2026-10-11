# figure-0177

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

The supplied durable journal identifies the exact unresolved fixed-lattice task as the 25 rank-four arrangements `[7919,17700,bA,bB]` with the stated five-by-five blocker sets. :contentReference[oaicite:0]{index=0} The run's acceptance gate requires a materialized exact finite object or exact exclusion rather than an unverified near-solution. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact adaptive rank-four determination

## Literal disposition

**RIGOROUS COMPLETE RANK-FOUR NONWINNER.** No strict own-centred `(S,U,H)=(1,1,0)` trace-one SPD box exists in any of the 25 nominated arrangements

```text
[7919,17700,bA,bB],
bA ∈ {7705,7709,7911,7916,7920},
bB ∈ {17697,17901,17906,17908,17910}.
```

Five systems have no trace-one SPD common plaque. The other twenty have exact rank-four plaques, but every point of every plaque and every full-dimensional chamber adjacent to them lies in an explicitly certified positive-radius neighborhood containing two disjoint stable trap sets. In addition, 320 concrete positive-radius orthant boxes were audited wall-by-wall and all have `S≥2`.

This settles the bounded rank-four frontier requested by the journal. It is **not** a global impossibility theorem for the rest of the five-dimensional trace-one SPD family.

The result is a complete rank-four **winner exclusion** and a materially smaller exact residual frontier. It does not pretend to enumerate every mechanically neutral `U/H` subchamber along all common lines: the transverse trap theorem subsumes any such internal multiwall chamber by proving `S≥2` throughout an open tube. The 320 boxes below provide complete classes for explicit adjacent orthants; all further chambers inside the tubes are excluded without needing a combinatorial explosion.

## What changed relative to the supplied journal

The journal stopped with the rank-two/rank-three transfer mechanism closed and the above 25 rank-four arrangements unresolved. This work supplies:

1. an exact rank-four line and perturbation certificate for all 25 arrangements;
2. an 89-interval exact cover of every possible common-wall parameter domain;
3. 1,744 exact Sylvester-failure intervals proving that all five arrangements with `bA=7911` have no SPD common plaque;
4. 74 explicit transverse trap tubes covering the twenty existing plaques;
5. twenty complete local rank-four hypercubes: 320 positive-radius boxes and 640 certified one-wall adjacencies;
6. complete face, vertex and true-edge-cone mechanics, an independently reconstructed lattice, and a deterministic H/V/mesh materialization.

## Exact fixed family and own centring

The fixed polar generator is

```text
Q = conv{q_i},       q_i=Qint_i/2^48,       i=0,…,4323.
```

The unique Santaló point is isolated by the strict Krawczyk certificate

```text
a_* ∈ a_c+[-2^-90,2^-90]^3,
a_c=2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856
).
```

Let `P_*=(Q-a_*)^polar`. Santaló stationarity gives `centroid(P_*)=0` exactly. Metrics use

```text
x=(K00,K11,K01,K02,K12),
K22=1-K00-K11,
K=[[K00,K01,K02],[K01,K11,K12],[K02,K12,K22]],
K ≻ 0,       tr(K)=1.
```

For `A=K^-1/2`, define `P_K=A P_*`. Its centroid remains exactly zero because

```text
∫_(A P_*) y dy = det(A) A ∫_(P_*) x dx = 0.
```

The transformed finite representation is deterministic:

```text
h_i(K)=A^-T(q_i-a_*),
v_f(K)=A y_f/(1-a_*·y_f),
```

where `y_f` is reconstructed from the exact active triple stored in `generator.json`. Since every certified K is positive definite, `A` is invertible. Hence this is an actual linear isomorphism, not a frozen-incidence assumption: every accepted cell has the exact lattice

```text
(H,V,E)=(4324,8644,12966),
8644-12966+4324=2,
boundary triangles=17284.
```

`topology.json` contains all 8,644 active triples, 4,324 maximal-face cycles, 12,966 true edges and 17,284 oriented boundary triangles.

## Complete mechanics

For adjacent maximal faces `i,j`,

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j).
```

There are 25,932 directed face walls. A face is stable exactly when all of its outgoing `S_ij` are positive.

For adjacent vertices `f,g`, with `d_f=1-a_*·y_f`,

```text
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g.
```

There are 25,932 directed vertex walls. A vertex is unstable exactly when all outgoing `W_fg` are positive. A true edge with incident faces `(i,j)` and endpoints `(f,g)` is a saddle exactly when

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

Every explicit box reconstructs all 51,864 directed signs and all four components of all 12,966 true-edge cones.

## The twelve rank-four wall identities

| wall | directed face transition | true edge |
|---:|---|---:|
| 7919 | 1343 → 1308 | 3959 |
| 17700 | 2938 → 2973 | 8850 |
| 7705 | 1308 → 1272 | 3852 |
| 7709 | 1308 → 1273 | 3854 |
| 7911 | 1308 → 1307 | 3955 |
| 7916 | 1308 → 1309 | 3958 |
| 7920 | 1308 → 1344 | 3960 |
| 17697 | 2973 → 2937 | 8848 |
| 17901 | 2973 → 2972 | 8950 |
| 17906 | 2973 → 2974 | 8953 |
| 17908 | 2973 → 3008 | 8954 |
| 17910 | 2973 → 3009 | 8955 |

The reverse-wall energy identity

```text
S_ij+S_ji=(q_i-q_j)^T K(q_i-q_j)>0
```

holds for every SPD metric and prevents a directed zero from being paired with a simultaneous reverse zero.

## Exact common-wall parameterization

For each target quadruple, write each scaled face equation as

```text
c_w(a)·x+b_w(a)=0.
```

Set `t=K00` and `y=(K11,K01,K02,K12)`. At `a_c`, the four equations give

```text
M y = -p t-b,
d=det(M)≠0,
y=(u+v t)/d.
```

All exact integers `d,u,v` are stored per arrangement in `RANK4_COMMON_WALL_SCC_ATLAS.json`. The pivot determinants have 830–839 bits. For the full Santaló box,

```text
||M(a_c)^-1 ΔM||_∞ ≤ η,
2.844094912163178e-25 ≤ η ≤ 1.071034657428450e-24 < 1.
```

Therefore every target system keeps rank four. Its actual line is uniquely defined, and its dependent coordinates differ from the central line by at most

```text
2.580119303952271e-25 ≤ ε ≤ 2.402028596269349e-24
```

in coordinate sup norm. Positive diagonal entries give an exact necessary `t` interval for every SPD solution. The 89 rational intervals in the atlas tile those domains without gaps.

## Global two-trap exclusion

For a parameter domain `D`, form a directed graph on the 4,324 faces. Put `i→j` in the **unsafe graph** when `S_ij` is not uniformly certified positive on `D`. If `C` is a sink strongly connected component, every directed wall leaving `C` is uniformly positive.

For a fixed SPD metric define

```text
r_i=(q_i-a_*)^T K(q_i-a_*).
```

Choose `i∈C` maximizing `r_i`. For every neighboring `j∈C`,

```text
2 S_ij = r_i-r_j+(q_i-q_j)^T K(q_i-q_j)>0.
```

For `j∉C`, positivity is supplied by the boundary certificate. Thus `i` is stable. Two disjoint sink components give two distinct stable faces.

The exact common-line atlas finds two such components on every one of its 89 intervals. More strongly, for the twenty systems with an SPD plaque, their outgoing boundary walls stay positive in a transverse coordinate tube. If `m` is the exact common-line boundary margin and `C` bounds the perturbed coefficient `l1` norm, the stored dyadic radius `ρ` satisfies

```text
Cρ ≤ m/4.
```

Hence at least `3m/4` remains throughout the tube. Internal walls may cross jointly in any order; the two sets remain stable traps because only their outgoing boundary walls matter. The 74 exact tubes have radii from `2^-13` through `2^-22`. The smallest exact physical tube-boundary clearance is stored in `RANK4_COMMON_WALL_TRAP_TUBES.json` and is approximately

```text
3.5051629118475243e-07.
```

Therefore **every full-dimensional SPD chamber whose closure meets any of the twenty rank-four plaques has `S≥2`**, even if many non-target walls cross simultaneously. This is the all-wall exclusion that the preceding one-wall analyses did not provide.

## Five systems with no SPD common plaque

All five use `bA=7911`. Their exact line enclosures are partitioned as follows:

| system | exact intervals | failed Sylvester upper bounds |
|---|---:|---|
| `7911/17697` | 45 | leading `2×2` determinant in all 45 |
| `7911/17901` | 5 | leading `2×2` determinant in all 5 |
| `7911/17906` | 106 | determinant in 102; leading `2×2` in 4 |
| `7911/17908` | 1,221 | determinant in 1,208; leading `2×2` in 13 |
| `7911/17910` | 367 | determinant in 363; leading `2×2` in 4 |

Each interval supplies an exact nonpositive upper bound, and the 1,744 intervals tile the full necessary parameter ranges. Thus no trace-one positive-definite metric can satisfy any of these five four-wall systems.

## Complete local all-wall chamber atlas

For each of the twenty existing plaques, an exact positive-radius collar was built. The actual Santaló-dependent plaque lies strictly inside it; only its four target face walls can vanish; every other face wall and every vertex wall is strict. Collar radii range from `2^-32` to `2^-36`.

All 16 target sign orthants are realized by full-dimensional dyadic boxes of radii `2^-68` through `2^-72`. The compact sign encoding consists of one complete non-target face ledger and one complete vertex ledger per plaque, plus four target signs per box. This reconstructs all 51,864 signs, every equilibrium list and all 12,966 four-component edge cones for every box.

`RANK4_LOCAL_ADJACENCY.json` gives the complete 4-cube adjacency: 32 one-wall adjacencies per plaque, 640 total, with an exact root bracket for the crossed wall. Every other target wall keeps its sign along the segment and every non-target wall remains strict in the convex collar.

Certified global minima over the 320 boxes are

```text
non-target face-wall clearance  = 4.3411194985290303e-08
vertex-wall clearance           = 5.6449047551185246e-13
target-face clearance           = 6.9768521805118959e-17
SPD determinant lower bound     = 4.0182227219485946e-04
```

All exact rational values and their attaining boxes/walls are in `CALM_QUARTZ_RANK4_RESULT.json`.

Total class histogram:

- `2,3,3`: 68
- `2,4,4`: 16
- `2,5,5`: 20
- `2,7,7`: 24
- `2,8,8`: 4
- `2,11,11`: 20
- `2,14,14`: 32
- `2,18,18`: 16
- `2,22,22`: 16
- `2,24,24`: 16
- `2,27,27`: 16
- `3,3,4`: 8
- `3,5,6`: 8
- `3,7,8`: 8
- `3,8,9`: 8
- `3,11,12`: 8
- `4,3,5`: 4
- `4,5,7`: 20
- `4,8,10`: 4
- `4,11,13`: 4

Every class has at least two stable faces. No box is `(1,1,0)`.

## Per-arrangement disposition

| `bA` | `bB` | disposition | common-line intervals | trap-tube intervals | explicit 16-box class histogram | min `S` |
|---:|---:|---|---:|---:|---|---:|
| 7705 | 17697 | exact nonwinner | 4 | 4 | `(2,4,4)`×16 | 2 |
| 7705 | 17901 | exact nonwinner | 4 | 4 | `(2,3,3)`×16 | 2 |
| 7705 | 17906 | exact nonwinner | 3 | 3 | `(2,3,3)`×16 | 2 |
| 7705 | 17908 | exact nonwinner | 5 | 5 | `(2,3,3)`×16 | 2 |
| 7705 | 17910 | exact nonwinner | 3 | 3 | `(2,14,14)`×16 | 2 |
| 7709 | 17697 | exact nonwinner | 3 | 3 | `(2,27,27)`×16 | 2 |
| 7709 | 17901 | exact nonwinner | 3 | 3 | `(2,22,22)`×16 | 2 |
| 7709 | 17906 | exact nonwinner | 5 | 5 | `(2,7,7)`×16 | 2 |
| 7709 | 17908 | exact nonwinner | 2 | 2 | `(4,5,7)`×16 | 4 |
| 7709 | 17910 | exact nonwinner | 5 | 5 | `(2,11,11)`×16 | 2 |
| 7911 | 17697 | no SPD plaque; 45 exact Sylvester intervals | 3 | — | — | — |
| 7911 | 17901 | no SPD plaque; 5 exact Sylvester intervals | 2 | — | — | — |
| 7911 | 17906 | no SPD plaque; 106 exact Sylvester intervals | 2 | — | — | — |
| 7911 | 17908 | no SPD plaque; 1221 exact Sylvester intervals | 5 | — | — | — |
| 7911 | 17910 | no SPD plaque; 367 exact Sylvester intervals | 3 | — | — | — |
| 7916 | 17697 | exact nonwinner | 4 | 4 | `(2,3,3)`×16 | 2 |
| 7916 | 17901 | exact nonwinner | 4 | 4 | `(2,5,5)`×16 | 2 |
| 7916 | 17906 | exact nonwinner | 4 | 4 | `(2,3,3)`×4, `(3,3,4)`×8, `(4,3,5)`×4 | 2 |
| 7916 | 17908 | exact nonwinner | 3 | 3 | `(2,18,18)`×16 | 2 |
| 7916 | 17910 | exact nonwinner | 4 | 4 | `(2,24,24)`×16 | 2 |
| 7920 | 17697 | exact nonwinner | 3 | 3 | `(2,7,7)`×8, `(3,7,8)`×8 | 2 |
| 7920 | 17901 | exact nonwinner | 3 | 3 | `(2,11,11)`×4, `(3,11,12)`×8, `(4,11,13)`×4 | 2 |
| 7920 | 17906 | exact nonwinner | 5 | 5 | `(2,8,8)`×4, `(3,8,9)`×8, `(4,8,10)`×4 | 2 |
| 7920 | 17908 | exact nonwinner | 3 | 3 | `(2,14,14)`×16 | 2 |
| 7920 | 17910 | exact nonwinner | 4 | 4 | `(2,5,5)`×4, `(3,5,6)`×8, `(4,5,7)`×4 | 2 |

## Representative actual materialization

A representative full-dimensional box is arrangement `7705/17901`, orthant `++++`, radius `2^-68`, with exact metric centre

```text
K00 = 2108023700437773/4503599627370496
K11 = 41230036286841154914436350564871957222523205408591572116039/200867255532373784442745261542645325315275374222849104412672
K01 = 417354480642796303666917839592713694665114860546329180017851/1606938044258990275541962092341162602522202993782792835301376
K02 = 443314595461431797547862051961283413328410284465971376237691/1606938044258990275541962092341162602522202993782792835301376
K12 = 327215976279021386860842743061115093782020026220887302047399/1606938044258990275541962092341162602522202993782792835301376
```

Its class is

```text
(S,U,H)=(2,3,3)
stable rows       = {1076,3231}
unstable vertices = {1939,6027,6029}
saddle edges      = {3641,7892,9266}.
```

Numerical eigenvalues are

```text
0.036528489751339203, 0.11260530869078746, 0.8508662015578734.
```

The deterministic materialization reconstructs 4,324 H rows, 8,644 vertices, 12,966 true edges and 17,284 triangles. The triangulated mesh has 25,926 edges, each of multiplicity two. Numerical checks give

```text
centroid norm                  = 1.0330635033692486e-15
max active incidence residual = 2.1094237467877974e-15
max halfspace violation       = 1.1102230246251565e-15.
```

The zero-centroid statement itself is exact and structural; the CSV/OBJ/STL files are deterministic numerical realizations of the isolated Santaló body.

## Independent verification

`verify_calm_quartz_rank4.py` is independent of the construction scripts. It reconstructs the lattice from active triples and face cycles, rebuilds every face-wall coefficient, re-solves every rank-four line, verifies every Neumann error bound and all 89 SCC covers, checks all 1,744 no-SPD intervals, recomputes every collar and all 320 box ledgers, classifies all true-edge cones, and verifies the representative mesh. It returned

```text
PASS, elapsed 175.092153 seconds.
```

`verify_rank4_trap_tubes.py` independently reconstructs all outgoing trap boundaries and the coefficient Lipschitz bounds for the 74 transverse tubes. It returned `PASS`.

`verify_rank4_local_adjacency.py` independently reconstructs all 640 one-wall adjacencies and their exact root intervals. It returned `PASS`.

Run all checks with

```bash
python verify_all.py
```

## Exact scope and next unresolved transition

The rank-four frontier is closed. A candidate cannot be obtained by further subdivision inside these common plaques, by changing the order of their internal target walls, or by adding another chamber sample inside their certified tubes. Any successful continuation must:

1. leave a two-trap tube—at least `2^-22` in coordinate sup norm in the worst certified case;
2. cross an outgoing boundary wall of one trap set;
3. keep or destroy the other trap in the same higher-dimensional event;
4. rebuild all face, vertex and true-edge mechanics on the far side.

`RANK5_DISCOVERY_ONLY.json` records 173 double-precision full-rank fifth-wall proposals. None had numerical `S=1`, but that file is explicitly **not** part of the exact exclusion. The next rigorous task is an adaptive exact tube-exit/rank-five atlas, not another scan of the now-closed 25 four-wall systems.

## Final statement

**NONWINNER, complete for the requested rank-four frontier.** Five arrangements have no SPD common plaque. The other twenty and every chamber adjacent to them have at least two stable faces on explicit positive-radius domains. No strict own-centred polyhedral Gömböc occurs in these 25 arrangements. The rest of the fixed-lattice trace-one SPD family remains unresolved only beyond the certified tube exits.

## Delivered artifacts

- [Complete exact rank-four NONWINNER bundle](sandbox:/mnt/data/Calm_Quartz_90_rank4_exact_NONWINNER.zip) — SHA-256 `86f07aff05003c5583b16e1a505b9cb2aa71660b45bbbdbc0914be44230b26cb`.
- [Full Markdown handoff](sandbox:/mnt/data/Calm_Quartz_90_rank4_handoff.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_rank4_result.json)
- [Independent main verifier output](sandbox:/mnt/data/Calm_Quartz_90_rank4_verify_output.json)
- [Clean-extraction verification receipt](sandbox:/mnt/data/Calm_Quartz_90_rank4_clean_verification.json)
- [Main independent verifier](sandbox:/mnt/data/calm_quartz_rank4/verify_calm_quartz_rank4.py)
- [Trap-tube verification output](sandbox:/mnt/data/Calm_Quartz_90_rank4_trap_tube_verify.json)
- [Adjacency verification output](sandbox:/mnt/data/Calm_Quartz_90_rank4_adjacency_verify.json)

The archive contains the exact generator, topology, 51,864-wall manifest, Santaló certificate, 89-interval common-wall atlas, 1,744-interval no-SPD proof, 74 transverse trap tubes, 320 orthant boxes, 640 adjacencies, all compressed sign ledgers, representative H/V/E tables and watertight OBJ/STL mesh, three independent verifiers, their PASS receipts, and a complete SHA-256 manifest. A fresh extraction independently passed all 49 manifest entries and all three verifiers.
