# figure-0166

AI research report · 2026-08-30 UTC

---

# Nimble Comet 34 — exact fixed-lattice SPD continuation through wall 19674

## Literal verdict

**No homogeneous convex polyhedral Gömböc was found in this continuation.** In particular, no positive-radius trace-one SPD box was isolated with strict own-centred `(S,U,H)=(1,1,0)`. The result is instead a complete exact/directed chamber atlas through the requested wall `19674 (3267→3303)`, then through the mechanically relevant successor `19880 (3302→3303)`, plus the independent post-`4421` survivor wall `21352 (3547→3582)`.

The acceptance gate remains the journal’s literal uniform-volume, own-centroid, all-maximal-face/all-vertex/all-true-edge requirement; auxiliary centres and wall points do not qualify. :contentReference[oaicite:0]{index=0} The journal also records that the predecessor transport failed without publishing an immutable result and reassigned this exact frontier to slot 3, Nimble Comet 34. :contentReference[oaicite:1]{index=1}

## What changed relative to the supplied journal

The interrupted worker-local bundle was recoverable from the persistent file library. I checked its original ZIP SHA-256

```text
30f8cfc921ff5341c04dc6b865112f6ef17d6a4f7443f0409d67ec661abae37b
```

and reran its unified verifier from a fresh extraction. The rerun exited `0`, took `127.3693356513977` seconds, reconstructed the lattice and mechanics rather than trusting stored counts, and ended `PASS`. Therefore the predecessor direction is no longer mathematically unknown: its exact no-winner atlas is now surfaced, independently rerun, and augmented with explicit target-wall equations and a compact cell/sign ledger. The recovered certificate states the same literal nonwinner result and exact transitions. :contentReference[oaicite:2]{index=2}

## Exact fixed body, centring, and compact SPD domain

The fixed polar lattice is

```text
q_i = Qint_i / 2^48,  i=0,…,4323,
Q = conv{q_i}.
```

Its globally unique Santaló point is isolated by Krawczyk in

```text
a_* = 2^-120 *
(-39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856)
      + [-2^-90,2^-90]^3.
```

Set `P_*=(Q-a_*)^∘`. The Santaló stationarity equation is exactly the vanishing ordinary first moment of `P_*`, hence `c(P_*)=0`. For any invertible linear map `A`,

```text
∫_(A P_*) y dy = det(A) A ∫_(P_*) x dx = 0,
```

so every metric image remains exactly own-centred. Translation of `Q` and invertible linear maps preserve the complete face lattice. The independently reconstructed fixed topology is

```text
H/maximal faces = 4,324
V                = 8,644
true edges       = 12,966
Euler            = 2.
```

Modulo rotation and scale, the metric variable is the trace-one inverse metric

```text
K = [[K00,K01,K02],
     [K01,K11,K12],
     [K02,K12,1-K00-K11]] ∈ SPD(3).
```

Every certified box lies in the unresolved compact core

```text
17179/16384 < λ1/λ3 < 2048/19,
λ2/λ1 > 1/32,
λ3/λ2 > 19/64,
λ3 > 19/4115,
trace(K)=1,
```

and is exactly outside all `287` previously certified nonwinner cells/balls.

## Complete wall system

For adjacent support rows `i,j` and adjacent primal vertices `f,g`, with exact baseline polar vertex `y_f` and `d_f=1-a_*·y_f>0`, the directed primitives are

```text
S_ij(K) = (q_i-a_*)^T K(q_i-q_j),
W_fg(K) = d_g y_f^T adj(K)y_f - d_f y_f^T adj(K)y_g.
```

There are exactly `25,932` directed face walls and `25,932` directed vertex walls. A true edge with incident faces `(i,j)` and endpoints `(f,g)` is a strict saddle iff all four actual components are positive:

```text
S_ij, S_ji, W_fg, W_gf > 0.
```

Every full-dimensional box audits all `51,864` directed primitives and all `12,966` four-component true-edge cones. No representative-feature or triangulation-diagonal inference is used.

The supplemental `target_wall_equations.json` expands the three target face walls into exact five-coordinate affine equations over the entire Santaló box and expands the two intermediate vertex walls into exact adjugate-quadratic equations. The decisive dyadic rows are:

```text
19674: 3267→3303, edge 9837, endpoints (8292,8293)
 q3267=2^-48(192596630942642,106693870906246,166643873981238)
 q3303=2^-48(197139291054511, 75224663124696,178300830061816)

19880: 3302→3303, edge 9940, endpoints (8292,8501)
 q3302=2^-48(197658027469337,104696942151608,161586147564848)
 q3303=2^-48(197139291054511, 75224663124696,178300830061816)

21352: 3547→3582, edge 10676, endpoints (1463,5220)
 q3547=2^-48(228590948084169, 87328760394109,124996541776608)
 q3582=2^-48(232117216459696, 84311207315483,120120917728197).
```

## Exact reachability and chamber sequence

Two exact centre-line connectors establish reachability from the immutable parent states:

```text
A19672_C07 → O19674_pre:
  4,993 pairwise ordered one-wall events,
  46,871 unchanged walls certified,
  no (1,1,0) chamber.

B4421_C08 → B232_21352_pre:
    675 pairwise ordered one-wall events,
 51,189 unchanged walls certified,
 no (1,1,0) chamber.
```

The requested full-dimensional local sequence is

```text
O19674_pre
  --F19674--> O19674_post
  --V13807--> O_A_mid
  --V9547 ---> O19880_pre
  --F19880--> O19880_post.
```

The exact root intervals, valid over the complete Santaló box, are:

```text
F19674:
[22300745196100265712349014559416626256887673 /
 44601490397061246283071436545296723011960832,
 5575186299025066428092848714718163178396391 /
 11150372599265311570767859136324180752990208]

V13807 (global wall 39739, 6934→3791, edge 6903):
[16374918991225264026970242149859076745095461 /
 44601490397061246283071436545296723011960832,
 4093729747806316006746308735596013493521805 /
 11150372599265311570767859136324180752990208]

V9547 (global wall 35479, 1852→818, edge 4773):
[16237417568609736532325117919008250352705559 /
 22300745198530623141535718272648361505980416,
 16237417568609736533366396153340366913029837 /
 22300745198530623141535718272648361505980416]

F19880:
[22300745202178588669360696219248992329156029 /
 44601490397061246283071436545296723011960832,
 22300745202178588669382952882030386381590903 /
 44601490397061246283071436545296723011960832]

F21352:
[22300745195428893916881277826872247451859867 /
 44601490397061246283071436545296723011960832,
 11150372597714446958441936255005056645795957 /
 22300745198530623141535718272648361505980416].
```

Each corridor crosses its named primitive exactly once; all other `51,863` walls retain strict sign. The two vertex walls are count-neutral. The three mechanically decisive face events are:

```text
19674: (4,2,4) → (3,2,3), removes stable 3267 and saddle 9837.
19880: (3,2,3) → (2,2,2), removes stable 3302 and saddle 9940.
21352: (3,2,3) → (2,2,2), removes stable 3547 and saddle 10676.
```

The obstruction is literal transfer: row `3303` is already stable before `19674` and remains after `19880`; row `3582` is already stable before `21352`.

## Full-dimensional exact box/sign ledger

Metric coordinates are `(K00,K11,K01,K02,K12)` with `K22=1-K00-K11`. `nums5/2^bits` gives the exact centre and the last column is the coordinatewise open radius.

```text
O19674_pre:       bits=100 nums5=[649214372466821625891036069888,166283713159146182418418892800,282824795742090333507490414592,523723396829910798714349289472,221103228988456225013923577856] r=2^-132
O19674_post:      bits=100 nums5=[649214349208983964203152834560,166283593398331888863249694720,282824663738809454611048431616,523723466889040312927231410176,221103138595583963372460179456] r=2^-132
O_A_mid:          bits=100 nums5=[649208797323333370631627472896,166272151562627660519328186368,282812545448729986153098248192,523730112918828441506890645504,221097182224515800158823251968] r=2^-132
O19880_pre:       bits=100 nums5=[649203971719253508978489950208,166262206514669192873890545664,282802012438194745290021404672,523735889534284595869679353856,221092005048626984931341369344] r=2^-132
O19880_post:      bits=100 nums5=[649203914921957204445357932544,166262089461586191430029672448,282801888464799984216572952576,523735957524972162776215584768,221091944113335205918115102720] r=2^-132
B232_21352_pre:   bits=72  nums5=[3199968037838294876160,614419973313624014848,1130019771927228579840,1552191578765201244160,485015219226042105856] r=2^-112
B232_21352_post:  bits=72  nums5=[3199971101297900257280,614420706526203084800,1130018908557844021248,1552190063396086087680,485013517243360411648] r=2^-112
```

| cell | class | stable rows | unstable vertices | saddle edges | minimum exact-directed clearance (decimal) |
|---|---:|---|---|---|---:|
| `O19674_pre` | `(4,2,4)` | `1007,3267,3302,3303` | `5457,3272` | `6056,6638,9837,9940` | `8.847937240473e-10` |
| `O19674_post` | `(3,2,3)` | `1007,3302,3303` | `5457,3272` | `6056,6638,9940` | `8.847928409091e-10` |
| `O_A_mid` | `(3,2,3)` | `1007,3302,3303` | `5457,3272` | `6056,6638,9940` | `8.073693901580e-10` |
| `O19880_pre` | `(3,2,3)` | `1007,3302,3303` | `5457,3272` | `6056,6638,9940` | `3.014525687079e-10` |
| `O19880_post` | `(2,2,2)` | `1007,3303` | `5457,3272` | `6056,6638` | `3.145019483982e-10` |
| `B232_21352_pre` | `(3,2,3)` | `725,3547,3582` | `479,3341` | `6370,6529,10676` | `5.877240728490e-10` |
| `B232_21352_post` | `(2,2,2)` | `725,3582` | `479,3341` | `6370,6529` | `5.877492786689e-10` |

For each cell, the listed positives are exhaustive. Every unlisted maximal face and vertex has a certified negative directed component; every unlisted true edge has a certified negative component among its four complete cone primitives. The seven `wall_signs_*.bin` payloads contain all `51,864` directed signs; their SHA-256 values and the exact positive face cycles, active triples, and edge incidences are in `cell_sign_ledger_summary.json`.

## Strongest exact endpoint

The strongest endpoint is `O19880_post`. Its exact inverse metric is

```text
K = 2^-100 *
[[649203914921957204445357932544,
  282801888464799984216572952576,
  523735957524972162776215584768],
 [282801888464799984216572952576,
  166262089461586191430029672448,
  221091944113335205918115102720],
 [523735957524972162776215584768,
  221091944113335205918115102720,
  452184595844686005621315600384]].
```

The entire coordinate box `|Δ(K00,K11,K01,K02,K12)|≤2^-132`, with dependent `K22`, is SPD and has strict class

```text
(S,U,H)=(2,2,2)
stable rows        1007,3303
unstable vertices  5457,3272
saddle edges       6056,6638.
```

Let `A=K^(-1/2)`, the unique symmetric positive algebraic inverse square root. The exact transformed data are

```text
h_i^A = A^(-T)(q_i-a_*),
v_f^A = A y_f/(1-a_*·y_f).
```

The archive contains all `4,324` transformed H rows, all `8,644` transformed vertices with active triples, all `4,324` actual maximal-face cycles, and all `12,966` true edges. The matching mesh has `17,284` boundary triangles, `25,926` triangulated edges, edge multiplicity two, and is watertight. The decimal OBJ/STL is the midpoint export; the exact object is the dyadic `K`, isolated algebraic `a_*`, exact formulas, and exact incidence ledger.

## New exact covered cells and next boundary

Two complete Löwner-relative cells prove `S≥2`:

```text
B(O19880_post,2): disjoint stable subsets of sizes 46 and 92,
                   207 complete outward boundaries,
                   inner trace-one box radius 2^-16.

B(B232_21352_post,2): subset sizes 243 and 129,
                      337 complete outward boundaries,
                      inner trace-one box radius 2^-16.
```

Their inner boxes are disjoint and remove exact five-coordinate volume

```text
1/18889465931478580854784 = 2^-74
```

from the previous compact remainder. The full fixed-lattice core is **not** exhausted.

The first genuinely unclassified boundaries are

```text
post-19880 / stable component 1007: wall 4633  (796→760)
post-19880 / stable component 3303: wall 21776 (3618→3619)
post-21352 / stable component 725:  wall 12042 (1984→2055)
post-21352 / stable component 3582: wall 17162 (2847→2883).
```

These are the exact first failures of the enlarged disjoint sink certificates, not coordinate scans. :contentReference[oaicite:3]{index=3} A successor should build actual wall-adjacent children outside the two certified `B(C,2)` regions and seek a coupled event that destroys both disjoint stable components before another stable birth. Refinement inside either relative cell is redundant.

## Independent verifier and artifacts

The clean rerun verifies source hashes, the `(4324,8644,12966)` lattice, all seven full boxes, all five one-wall corridors, both long connectors and all `5,668` ordered roots, both relative cells and `544` outward boundaries, nonmembership in all `287` prior cells, H/V reconstruction, and the watertight mesh. The verifier’s published orchestration matches this scope. :contentReference[oaicite:4]{index=4}

- [Complete recovered-and-augmented exact atlas](sandbox:/mnt/data/Nimble_Comet_34_SPD_19674_exact_atlas.zip)
- [Archive SHA-256](sandbox:/mnt/data/Nimble_Comet_34_SPD_19674_exact_atlas.zip.sha256): `6b62f03071e5a290f4aee0495e06366dfe82fb2d8f0f209133a3b89a2ca094a0`
- [Full Markdown handoff](sandbox:/mnt/data/Nimble_Comet_34_SPD_19674_handoff.md)
- [Independent rerun transcript](sandbox:/mnt/data/Nimble_Comet_34_independent_rerun.log)
- [Strongest endpoint H table](sandbox:/mnt/data/Nimble_Comet_34_O19880_post_H.csv)
- [Strongest endpoint V table](sandbox:/mnt/data/Nimble_Comet_34_O19880_post_V.csv)
- [Watertight OBJ](sandbox:/mnt/data/Nimble_Comet_34_O19880_post.obj)
- [Watertight STL](sandbox:/mnt/data/Nimble_Comet_34_O19880_post.stl)

## Unresolved uncertainty

This result closes the direct `19674→19880` survivor attack and the parallel `21352` attack, but it is not a global nonexistence theorem for the fixed lattice. The remaining compact trace-one SPD set outside the accumulated exact exclusion union is nonempty and unclassified. No numerical discovery run is used as coverage evidence. The strongest certified endpoint is therefore the open `(2,2,2)` box `O19880_post`, and the next legitimate mathematical boundary is the four-wall set listed above.
