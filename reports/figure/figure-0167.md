# figure-0167

AI research report · 2026-08-30 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Rapid Quartz 33 — recovered joint eight-edge breaker

## Disposition

**USED as rigorous exact nonwinner evidence.** The journal knew only that the Keen Quartz 40 transport turn had failed and reassigned its `R41` frontier to Rapid Quartz 33. :contentReference[oaicite:0]{index=0} I recovered a complete unpublished archive from that turn, verified its pristine manifest (`141/141` files), and reran `[internal-source-reference].sh` in the current environment. The rerun ended in `ALL_CHECKS_PASS` and reproduced every conclusion below.

No homogeneous polyhedral Gömböc was obtained. The strongest open own-centred endpoint is

```text
J40_final: (H_rows,V,E)=(2686,5368,8052), (S,U,H)=(7,39,44)
stable rows=[0,2348,2349,2351,2366,2367,2369].
```

It genuinely leaves the original `R41` forced-edge cell, destroys all eight original forcing edges and all eight intermediate transfer edges, and crosses an isolated actual circuit wall. A new seven-edge row-disjoint matching forces `S>=7`; the exhaustive audit attains equality. :contentReference[oaicite:1]{index=1}

## Reproducible artifact

- [Complete exact archive](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner.zip), SHA-256 `b6a4ed450a48585805e9c5a551d177a1f781397248b0714395304203dc4b7ce4`.
- [Archive hash](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner.zip.sha256); [141-file manifest check](sandbox:/mnt/data/RQ33_manifest_verification.txt).
- [Fresh verifier transcript](sandbox:/mnt/data/RQ33_current_environment_rerun.txt); [recovery report](sandbox:/mnt/data/RQ33_recovery_verification.json); [recovery note](sandbox:/mnt/data/RQ33_RECOVERY_NOTE.md).
- [Full original handoff](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/RESULT_FINAL.md); [machine result](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/RESULT.json).

The archive supplies deterministic exact-dyadic H-generators, all five isolated roots, complete H/V/E tables, maximal-face cycles, every true edge, full face/vertex/four-component edge-cone ledgers, topology differences, rank and obstruction certificates, independent verifier, OBJ and STL.

## 1. Exact parent `R41`

For exact-dyadic rows

\[
q_i(x)=q_i^0+\delta uD_i^{(0)}+\delta t_1D_i^{(1)}+\delta t_2D_i^{(2)},
\qquad P(x)=\{z:q_i(x)\cdot z\le1\ \forall i\},
\]

the actual rebuilt parent is

```text
topology be33fd821193f7611c1bda42889c0a132154fbbf5196d6d9016c9bb78f028919
(H_rows,V,E)=(2660,5316,7974), (S,U,H)=(9,39,46)
stable=[0,2348,2351,2366,2369,2384,2385,2402,2403].
```

Its unique ordinary-centroid root is isolated in `[-2^-38,2^-38]^3`, with Krawczyk image

```text
du  [-2.7414932644635611e-13, 2.6885999475028676e-13]
dt1 [-2.3956110197287757e-14, 2.3359778933878717e-14]
dt2 [-2.2371823400870795e-13, 2.2700366749128323e-13]
```

moment-Jacobian determinant `-0.0012368457567829094`, condition `133.98`, and inactive gap `1.4680964222080204e-9`. Full-box directed margins are `+9.462810843362534e-4` stable-included, `-3.333528618498782e-5` face-excluded, `+2.172011507777294e-2` unstable-included, `-8.795717345255747e-3` vertex-excluded, `+3.347222820719606e-2` saddle-included, and `-1.0409324270316602e-2` edge-excluded. :contentReference[oaicite:2]{index=2}

### Eight paired stable obstructions and edge/fan incidence

```text
pair         true-edge# primal endpoints stable endpoint degrees external fan, first ; second
2383-2348    4486       3001-3003       2348            6/6     2347,2382,2384,2418,2419 ; 2312,2313,2314,2347,2384
2386-2351    4490       3005-3006       2351            5/7     2385,2387,2420,2421 ; 2315,2316,2317,2352,2385,2387
2401-2366    4534       3033-3035       2366            6/6     2365,2400,2402,2436,2437 ; 2330,2331,2332,2365,2402
2404-2369    4538       3037-3038       2369            5/7     2403,2405,2438,2439 ; 2333,2334,2335,2370,2403,2405
2384-2419    4596       3078-3081       2384            6/6     2314,2348,2383,2385,2420 ; 2383,2418,2420,3470,3471
2385-2420    4599       3080-3082       2385            6/8     2314,2315,2351,2384,2386 ; 2384,2386,2419,2421,3471,3472,3473
2402-2437    4680       3144-3147       2402            6/6     2332,2366,2401,2403,2438 ; 2401,2436,2438,3488,3489
2403-2438    4683       3146-3148       2403            6/8     2332,2333,2369,2402,2404 ; 2402,2404,2437,2439,3489,3490,3491
```

[Full exact incidence JSON](sandbox:/mnt/data/RQ33_R41_forced_pair_incidence.json), SHA-256 `1a6e259e83a76d1f15a9c2d6773942e728ff2520a263b53dc706b781a905b447`, includes the exact dyadic anchor coordinates, every endpoint face cycle, all neighbours, edge indices and root-box signed margins; [readable ledger](sandbox:/mnt/data/RQ33_R41_forced_pair_incidence.md).

For each pair every external neighbour primitive is positive. If both endpoints were nonstable, only the mutual edge could fail, forcing `q_a·q_b>=||q_a||^2` and `q_a·q_b>=||q_b||^2`; Cauchy–Schwarz would then force equal norms and parallelism, impossible for a nonzero true edge. Hence one stable endpoint per row-disjoint pair, plus protected row `0`, forces `S>=9` in the `R41` sign cell.

## 2. Genuinely joint architecture and hard moments

The exact archive contains `83` binary64-dyadic fields:

```text
3 dependent moment fields, supports 802/910/2344
16 one-row R41 endpoint controls (both endpoints of all eight pairs)
2 complete 208-row cluster fields
2 three-row relay packets
8 disjoint 135-row projected nonlocal tangential fields
20 compensated R41 fields, supports 585/588/624/663
16 second-layer endpoint fields, support 585
4 rebreak fields, support 585
12 third-layer fields, support 585/586.
```

Exact anchor amplitudes are `7/8` (R41 endpoint), `3/2` (clusters), `1/4` (relays), `1` (second layer), and `2/5` (rebreak); rows `0,4321,4322,4323` remain protected. Sources: [generator](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/source/joint_architecture_generator.json) and [83-field archive](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/source/joint_architecture_fields.npz). :contentReference[oaicite:3]{index=3}

After eliminating `Mx=My=Mz=0`, exact Bareiss minors give endpoint rank `16`, nonlocal rank `8`, combined rank `24`, and circuit/stability response rank `16`. Thus nonlocal channels survive centring independently; this is not a common-amplitude path. :contentReference[oaicite:4]{index=4}

Every actual cell is rebuilt before evaluating

\[
v_T=Q_T^{-1}(1,1,1)^T,
\quad V=\sum_\tau\det(v_a,v_b,v_c)/6,
\quad M=\sum_\tau\det(v_a,v_b,v_c)(v_a+v_b+v_c)/24.
\]

Outward Krawczyk arithmetic isolates `Mx=My=Mz=0`; all volume intervals are positive. Stability uses every true neighbour, instability the complete incident cone, and saddles all four full-normal-cone components on every true edge. :contentReference[oaicite:5]{index=5}

## 3. Exact cells and topology ledger

| cell | `(H_rows,V,E)` | `(S,U,H)` | stable rows |
|---|---:|---:|---|
| `R41` | `(2660,5316,7974)` | `(9,39,46)` | `0,2348,2351,2366,2369,2384,2385,2402,2403` |
| `J20_simple` | `(2674,5344,8016)` | `(9,39,46)` | `0,2351,2369,2383,2401,2419,2420,2437,2438` |
| `J36_g1` | `(2686,5368,8052)` | `(7,41,46)` | `0,2348,2351,2366,2369,2384,2402` |
| `J40_final` | `(2686,5368,8052)` | `(7,39,44)` | `0,2348,2349,2351,2366,2367,2369` |
| `J41_postwall` | `(2687,5370,8055)` | `(7,39,44)` | same as J40 |

All five have unique roots in `[-2^-38,2^-38]^3`, positive volume, Euler `2`, and no ambiguous incidence or equilibrium primitive. [Complete atlas](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/atlas/complete_atlas.json). :contentReference[oaicite:6]{index=6}

| transition | `Delta(H,V,E)` | H removed/added | facets removed/added | true edges removed/added |
|---|---:|---:|---:|---:|
| `R41->J20` | `(+14,+28,+42)` | `36/50` | `397/425` | `341/383` |
| `J20->J36` | `(+12,+24,+36)` | `17/29` | `213/237` | `163/199` |
| `J36->J40` | `(0,0,0)` | `2/2` | `17/17` | `15/15` |
| `J40->J41` | `(+1,+2,+3)` | `0/1` | `1/3` | `0/3` |

All R41 edges are absent by J20. The intermediate transfer matching

```text
(2350,2420) (2351,2421) (2368,2438) (2369,2439)
(2383,2418) (2401,2436) (2419,2454) (2437,2472)
```

is entirely absent by J40. :contentReference[oaicite:7]{index=7}

The separately isolated connected wall solves `Mx=My=Mz=0` and `D_(4198,4232,4233,4234)=0`. It removes facet `(4198,4232,4234)`, adds `(4198,4232,4233)`, `(4198,4233,4234)`, `(4232,4233,4234)`, and has `Delta(H,V,E)=(+1,+2,+3)` with class unchanged. [Exact wall certificate](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/certificates/J40_outgoing_wall/wall_certificate.json). :contentReference[oaicite:8]{index=8}

**Proof boundary:** the first three distant anchor moves have complete exact before/after lattices and full symmetric-difference lists, but not an exhaustive ordered CAD decomposition of every intervening circuit wall. Only `J40->J41` is isolated as a single exact crossing. This is the principal unmet part of the ideal circuit-ledger request.

## 4. Strongest endpoint and first new obstruction

`J40_final` has unique hard-moment root

```text
du  [-1.9758862821044082e-13, 1.9706468071597974e-13]
dt1 [-1.9404619984052987e-14, 1.9358254581729922e-14]
dt2 [-1.6703701235201333e-13, 1.6529723403809862e-13]
volume [3.371288156755192,3.3712881567551927].
```

Full-box margins are nonincident `+1.4680964222080204e-9`, stable `+9.462810843362534e-4`, excluded face `-5.597850189253961e-5`, unstable `+3.96532065431393e-2`, excluded vertex `-2.439287856399241e-3`, saddle `+3.445008929895164e-2`, excluded edge cone `-4.29378264861625e-3`. [Root certificate](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/certificates/J40_final/root_certificate.json). :contentReference[oaicite:9]{index=9}

The new row-disjoint forcing matching is

| edge | external checks | external lower | squared-edge lower |
|---|---:|---:|---:|
| `(0,36)` | 39 | `1.0271636152303641e-5` | `7.415572048130184e-4` |
| `(2348,2453)` | 12 | `1.344061552513542e-3` | `1.275019011570655e-2` |
| `(2349,2384)` | 8 | `1.783821544947495e-3` | `8.834286766307861e-3` |
| `(2351,3404)` | 15 | `1.196036570668357e-3` | `7.691640613494443e-1` |
| `(2366,2471)` | 12 | `1.379707968835353e-3` | `1.273736442913061e-2` |
| `(2367,2402)` | 8 | `1.829612590786178e-3` | `8.980307816956993e-3` |
| `(2369,3386)` | 15 | `1.173407510014823e-3` | `7.68757583339044e-1` |

The same endpoint-pair theorem now forces `S>=7` over the entire root box. Since all sixteen old edges are absent, this is the first nonlocal obstruction not already present in `R41`. [Forcing certificate](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/certificates/J40_final_forcing_obstruction.json). :contentReference[oaicite:10]{index=10}

A five-dimensional parametric Krawczyk proof permits two free nonlocal coordinates of radius `2^-42` while solving the three moments in radius `2^-36`; throughout this positive box the same lattice and `(7,39,44)` audit persist. [Perturbation certificate](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/certificates/J40_final_perturbation/parametric_perturbation_certificate.json). :contentReference[oaicite:11]{index=11}

## 5. Independent verifier, mesh, and continuation

The standalone verifier imports no construction/certification module, rebuilds all five hulls, exact Cramer incidence, every edge/cycle, volume/moments, its own Krawczyk audit, exact ranks, walls, perturbation and forcing theorem, and reparses both meshes. The fresh run reproduces cell classes `R41 (9,39,46)`, `J20 (9,39,46)`, `J36 (7,41,46)`, `J40/J41 (7,39,44)`, ranks `16/8/24`, forcing `S>=7`, and a connected watertight Euler-2 mesh with `5368` vertices and `10732` triangles. :contentReference[oaicite:12]{index=12}

- [Verifier](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/verifier/verify_joint_breaker.py), SHA-256 `307a2b1daaca6dc939614e114d09801cbe019110506e7747f6c4fb021b0a8792`.
- [OBJ](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/meshes/strongest_J40_final.obj), SHA-256 `0b63c36a713be5a5a8253e1b82d95ed8afe4cbdddaa0fef452c593ebad1a10e1`.
- [STL](sandbox:/mnt/data/slot4_joint_breaker_exact_nonwinner/meshes/strongest_J40_final.stl), SHA-256 `71866f6abf2b0d453265cc810d9ad43cca6f7e45d6db14b8ee27ebd411165fcc`.

The first unclassified exit after J41 is the numerically bracketed quad `(2351,2456,3439,3474)` for `g in [0.06250000000000001,0.06350000000000001]`; it swaps two facets for two, but both bracket endpoints retain seven stable faces. No exact wall box is claimed. :contentReference[oaicite:13]{index=13}

The strongest continuation is from `J40_final`/`J41_postwall`, not R41: break the seven new edges in one connected event; use independent controls on both endpoints of the six nonprotected edges; insert a topology-changing cap around protected `(0,36)`; retain at least two projected nonlocal antibirth channels; keep all three moments dependent; and rebuild/audit every post-wall lattice. The mapped entrance is `(2351,2456,3439,3474)`. Other joint architectures remain unexcluded because no CAD exclusion of the full 24-dimensional projected control space is claimed. :contentReference[oaicite:14]{index=14}

## Acceptance statement

This is a complete, independently rerun, interval-exact **joint-topology nonwinner**. It supplies the requested ordinary-moment solution, actual post-deactivation H/V/E lattice, exhaustive full-cone audit, simultaneous destruction of all eight R41 pairs and all eight transfer pairs, positive perturbation box, verifier, and watertight OBJ/STL. It does **not** supply `(1,1,0)`: the open endpoint is `(7,39,44)`, and the exact new seven-edge matching is the first surviving nonlocal obstruction.
