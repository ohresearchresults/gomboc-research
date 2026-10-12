# figure-0197

AI research report · 2026-09-02 UTC

---

The supplied journal's accepted boundary was the completed quartet collar: all 16 adjacent chambers were nonwinners, `PRE_16494` remained the strongest fixed-lattice endpoint, and the requested successor was a nonlocal stable-component exit preserving row `2092` and vertex `2693`. :contentReference[oaicite:0]{index=0} The run's non-negotiable acceptance gate requires an exact finite own-centred polyhedron with actual incidence, exhaustive strict mechanics, independent verification, and matching mesh data. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact nonlocal preserved-row obstruction

## Literal disposition

**RIGOROUS COMPONENT-LEVEL NONWINNER.** No strict own-centred `(S,U,H)=(1,1,0)` metric exists anywhere in the fixed 4,324-row trace-one SPD orbit while stable face `2092` is preserved as the intended unique stable equilibrium. This is stronger than another path or local fan exclusion: it covers every connected or disconnected SPD route satisfying the accepted spectral necessary condition, uniformly over the complete Santaló root box.

It is not a theorem that the entire fixed-lattice orbit has no winner. A winner with another unique stable row remains unexcluded. The provisional 1,710-exit protocol is not used.

## Exact family

The fixed polar is `Q=conv{Qint_i/2^48}`, with 4,324 irredundant support rows. Its unique Santaló point lies in

```text
a_* = 2^-120(-39878490350125864373364388380978345,
              88581653811863381217051,
              819441514472273259270856)
      +[-2^-90,2^-90]^3.
```

For trace coordinates `x=(K00,K11,K01,K02,K12)`, set `K22=1-K00-K11`. Every accepted metric has `K≻0`, `tr K=1`, and `P_K=K^-1/2 P_*`. Santaló stationarity gives `centroid(P_*)=0` exactly, and the invertible linear map preserves zero centroid. The actual lattice is

```text
(H,V,E)=(4324,8644,12966),
face walls=25932,
vertex walls=25932,
true-edge four-component cones=12966,
boundary triangles=17284.
```

## Parent spectral reduction

The accepted exact parent certificate proves that any still-unexcluded winner must satisfy

```text
lambda2/lambda1>1/32,
lambda3/lambda2>19/64,
cond(K)>17179/16384,
lambda_min(K)>19/4115.
```

The exact parent archive has SHA-256 `0f7f44f05688ac3f1102c23d2ea02a0854dcd454e8b9e60a319b24bd5476efb7`. Its stored global verification receipt records 2,546,727 component-boundary checks and the same `(4324,8644,12966)` lattice. The new proof therefore works on `K >= (19/4115)I`; the parent certificate covers the complement.

## Exact obstruction

For every face define

```text
r_i=(q_i-a_*)^T K(q_i-a_*).
```

For adjacent faces `i,j`, the exact identity is

```text
2 S_ij = r_i-r_j+(q_i-q_j)^T K(q_i-q_j).
```

Any global maximizer of `r_i` is therefore strictly stable for every SPD `K`. Consequently, if `2092` were the unique stable face, it would be the unique global energy maximizer.

The exact outer relaxation contains 4,891 linear inequalities in `(K00,K11,K01,K02,K12,epsilon)`:

- 4,323 robust global-energy inequalities comparing row `2092` with every other row;
- six robust strict stability inequalities for row `2092`;
- eleven trace-coordinate bounds;
- 551 exact rational directional inequalities necessary for `K >= (19/4115)I`.

At each internal node a non-target face is required to be nonstable, so at least one of its six outgoing walls must be at most `-epsilon`. Branching over all six choices gives a complete 67-node, 56-leaf tree of maximum depth four. The only adaptive relay faces are

```text
{2110,2145,2163,2180,2181,2216}.
```

Every leaf has an exact nonnegative six-support Farkas dual satisfying

```text
sum y_k A_k = e_epsilon,
sum y_k b_k < 0.
```

Thus every leaf forces `epsilon<0`. The least-negative exact upper bound is

```text
-74887394123148600489845491712961632320857587687664038246666885529737046578745346105836080114645435199771771781321268990136725543485784639373449058067202033085874788121904243977087057542631228998227403111811/76909538360099296576379253498345670776627776112457645141227853663896555038693900239240484217082374167921680538996138424447845640634070271308736502885547342126833181990314521987715592188857529695794195215360720896
≈ -9.7370749740451189e-07.
```

This contradicts the common positive strictness margin of any open winner chamber. Hence row `2092` cannot be the unique stable face.

The argument deliberately omits all vertex and saddle requirements, so it is an outer relaxation of the requested mechanics. In particular, imposing that vertex `2693` remain strictly unstable and requiring exactly one unstable vertex and no saddle edge can only shrink the feasible set. The nonexistence conclusion therefore remains valid under the requested preservation of vertex `2693`.

## First exact boundary

The six outgoing death walls of row `2092` are

| wall | transition | true edge |
|---:|---|---:|
| 12265 | `2092→2021` | 6132 |
| 12475 | `2092→2056` | 6237 |
| 12479 | `2092→2057` | 6239 |
| 12686 | `2092→2127` | 6343 |
| 12688 | `2092→2128` | 6344 |
| 12690 | `2092→2163` | 6345 |

`ROW2092_BOUNDARY_AND_RELAY_ATLAS.json` stores their exact trace-chart coefficients, full Santaló uncertainty bounds, reverse-wall indices, and energy identities, together with all outgoing walls of the six forced relay faces.

Within the fixed lattice, any possible winner must abandon row `2092` by crossing this boundary and then solve a different stable-component problem. If row `2092` must remain the intended stable equilibrium, no SPD continuation exists; the mathematically first admissible continuation is topology-changing, changing the support generator or its incidence so that this exact relay obstruction no longer applies.

## Strongest materialized endpoint

No new endpoint can improve the stable count while preserving row `2092`. The strongest exact endpoint in the connected accepted source component therefore remains `PRE_16494`, a radius-`2^-120` trace-one SPD box with

```text
(S,U,H)=(2,2,2),
stable rows={2092,2180},
unstable vertices={2028,2693},
saddle true edges={1603,11125}.
```

Its exact metric centre is

```text
38058021622708567468779065052408831524229350396217253673801/200867255532373784442745261542645325315275374222849104412672
68823866389011966411118542450225602174405647045336189891889011937526327289495/231584178474632390847141970017375815706539969331281128078915168015826259279872
-8086040717562568807395971691478655583608068878925139121630417916381129006345/231584178474632390847141970017375815706539969331281128078915168015826259279872
9867350667506478391637498328764300086051839715332526886288437858398697026017/231584178474632390847141970017375815706539969331281128078915168015826259279872
16509551414496109865973574542484601728952021384059036974122042120134933195101/57896044618658097711785492504343953926634992332820282019728792003956564819968
```

Its exact box-wide Sylvester lower bounds are positive; the determinant lower bound is approximately `0.01148465559399398`. Its minimum complete directed face-wall margin is approximately `1.0764356602832737e-7`, and its minimum directed vertex-wall margin is approximately `2.0022328508613284e-9`. The deterministic H/V tables, true-edge table and watertight OBJ/STL are included. The complete prior joint-four archive, SHA-256 `a9ca7d09a00e1bf23a5bc69ae226c1dd5874356c8f482462001f6f2cdf74c5aa`, independently reconstructs and verifies all 51,864 primitives and every true-edge cone for this endpoint.

## Verification

`verify_unique_stable2092.py` is independent of the builder. It reconstructs the exact lattice and edge-component partition from `generator.json`, `topology.json` and `wall_system_manifest.json`; verifies all 25,932 energy identities; rebuilds all 4,891 base inequalities and 551 PSD cuts; walks the full branch tree; and checks all 56 exact dual identities and negative bounds. It returns `PASS`.

`verify_package.py` checks every manifested hash, the exact parent and prior-archive hashes, the parent spectral receipt, the PRE materialization counts and mesh multiplicity, and reruns the new independent verifier. A clean extraction with `--full-prior` also extracted and reran the complete prior joint-four verifier. Both returned `PASS`.

The large parent spectral-collar archive is included and hash-checked against the accepted immutable SHA-256. Its full long-running collar replay was not repeated in the clean receipt; `verify_package.py --full-parent` is supplied for that replay.

## Honest boundary

Closed exactly: every fixed-lattice trace-one SPD route, local or nonlocal, connected or disconnected, that attempts to retain row `2092` as the unique stable equilibrium.

Not closed: fixed-lattice chambers whose unique stable row is different from `2092`; topology-changing families; the provisional 1,710-exit protocol.

The exact next fixed-lattice question is a simultaneous exchange across one of the six row-`2092` death walls that installs a different unique stable row while also reducing the unwanted unstable/saddle packet. The exact next question under the user's preservation constraint is topology-changing rather than metric-only.

## Delivered artifacts

- [Complete exact NONWINNER archive](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER.zip) — SHA-256 `dafc244ec044481775fbd0a33d3b7ad75b7d6b9ab87f7c4ef207a3c67320df95`.
- [Full Markdown handoff](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/CALM_QUARTZ_NONLOCAL_ROW2092_HANDOFF.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/CALM_QUARTZ_NONLOCAL_ROW2092_RESULT.json)
- [Exact 67-node/56-leaf obstruction certificate](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/UNIQUE_STABLE_2092_EXACT_BRANCH_CERTIFICATE.json)
- [Independent exact verifier](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/verify_unique_stable2092.py)
- [Verifier PASS output](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/UNIQUE_STABLE_2092_VERIFY_OUTPUT.json)
- [Exact row-2092 boundary and relay atlas](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/ROW2092_BOUNDARY_AND_RELAY_ATLAS.json)
- [Clean verification receipt](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/CLEAN_VERIFICATION.json)
- [Package verifier](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/verify_package.py)
- [PRE endpoint H data](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/pre16494_H.csv)
- [PRE endpoint V data](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/pre16494_V.csv)
- [PRE endpoint true-edge data](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/pre16494_true_edges.csv)
- [PRE endpoint OBJ](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/pre16494_mesh.obj)
- [PRE endpoint STL](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/pre16494_mesh.stl)
- [Accepted parent global spectral archive](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/Bright_Atlas_91_fixed_cover_SPD_global_frontier.zip)
- [Prior complete quartet archive](sandbox:/mnt/data/Calm_Quartz_90_nonlocal_row2092_exact_NONWINNER/Calm_Quartz_90_joint4_exact_NONWINNER.zip)

## Final statement

**NONWINNER, rigorously delimited.** The requested nonlocal metric-only continuation preserving stable row `2092` is impossible throughout the entire fixed-lattice trace-one SPD orbit. The obstruction is independent of the unstable and saddle requirements, so preserving unstable vertex `2693` cannot evade it. No new `(1,1,0)` metric exists in this branch. The first exact fixed-lattice boundary is the six-wall death set of row `2092`; preserving that row beyond this result requires a topology-changing support/incidence family rather than another SPD chamber search.
