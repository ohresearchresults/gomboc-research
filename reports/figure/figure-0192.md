# figure-0192

AI research report · 2026-09-02 UTC

---

# Steady Willow 02 — exact P9-XG4 fourth-page/shared-terminal determination

## Literal disposition

**EXACT NONWINNER.** The run’s acceptance gate remains a finite uniform-density convex polyhedron at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`, complete maximal-face/vertex/true-edge mechanics, positive margins, independent verification, and matching OBJ/STL. :contentReference[oaicite:0]{index=0} The supplied journal records XG3 as an exact `(V,E,F)=(14,21,9)`, `(2,2,2)` three-page book and names a fourth-page/higher-valence `L` cell as the first admissible successor. :contentReference[oaicite:1]{index=1}

I constructed and exactified that successor. It has an entrance four-page polar book on one new row `L`, followed by a genuine higher-valence terminal contraction in which `K` becomes inactive. This changes the XG3 incidences and destroys the old `K` support-norm sink, the old extra source `(SU,S102,K)`, and both `K` saddle edges. It does **not** cancel the Euler-neutral packet: before the terminal wall, all four unwanted mechanical identities transfer to `L`.

The exact endpoint is

```text
supplied rows = 40; active rows = 8
(V,E,F) = (12,18,8); complexity = 36
(S,U,H) = (2,2,2)
stable   = T27, L
unstable = (TR,S102,G), (SU,S102,L)
saddles  = (L,S102), (L,SA5)
```

Protected stable `T27` and protected unstable `(TR,S102,G)` survive. No homogeneous polyhedral Gömböc was obtained.

## Exact generator and all supplied rows

For the first 39 labels, use common denominator `D=2^48=281474976710656` and integer numerators

```text
old_o9    ( 4245018469535146, -1619664580614903, -173154193581811)
old_o26   ( -480096932460134,  1385859804970441,  596299903857803)
old_o27   (-9652144994745056,  2066479937650009,  -12452755042990)
old_o32   (-1627120337143338,   648779352466143,  256073884381717)
old_o102  (-3037439597868230,  1998572535345049,  637020287150957)
old_A0    ( 1980086097328590, -1343951560984291, -646049450463920)
old_B0    ( 1762836693943848, -1308640889495975, -409252462863352)
old_A1    ( 1093925313855956, -1276485136749701, -730151068589962)
old_B1    (  955135318314688, -1249198402266031, -463015709557556)
old_A2    (  497762906287329, -1139787832376309, -724710366602572)
old_B2    (  440571798642713, -1175362208949782, -479703404259243)
old_A3    (  100793413735337, -1239992848373271, -856706599241789)
old_B3    (   55355700726647, -1091490629206128, -478539800213201)
old_A4    ( -243569956965967,  -875936416864223, -654670719464205)
old_B4    ( -270439935613186,  -997153596349074, -466537272637156)
old_A5    ( -779542305588156, -1093027578182889, -892591790687755)
old_B5    ( -590332436875325,  -904410020312242, -454117567296014)
old_A6    ( -988917232010623,  -720976326879196, -665196325568968)
old_B6    ( -877606810028888,  -723975394477078, -399186365538798)
old_A7    (-1416857017734346,  -505912741905342, -584614908915974)
old_B7    (-1302711289888646,  -553544576761945, -359671631410939)
old_B8    (-1861391125171647,  -238516629756715, -264937533207784)
old_C0    ( 3214085448171353,  -704225950137427,  178181968371790)
old_C1    (  -76871202338646, -1113561128697661, -500329854295910)
old_XS    ( 2070506863739108,  1198716451095130,  786889445623964)
old_XR    ( -994075609868406,  -410830540041415, -943377459862798)
old_XU    ( -523582166743982,  -288213609479852,   69844473213904)
T27       (-14250485468324114,  2126152597363496, -253021606630764)
TR        ( -892363419092795,  -471882852180058,-1057533148263150)
S9        ( 6397706066723506, -2055292855184413,  -23702208362607)
SC0       ( 6409695107091788, -1902604141791882,   65369336133532)
SS        ( 3369985039421002,  1877598994209753, 1161790427417546)
SU        (-1088262959027350,  -774327665054824,  236577016428290)
SC1       ( -553435677660258, -2605078903801754, -914587118611940)
SA5       (-1735735365091297, -2190132466616797,-2075306589585777)
S102      (-6981300916998116,  5268329269809467, 1934562100355505)
G         ( 6380126026482460,   557092426276712,  289137245707036)
H         (14546216055843558, -3524637976588795,  415896045741617)
K         (36768004743420232, -5486895589312041, 1536914688578617)
```

The fortieth row is the exact affine path `L(s)=L0+s(Lt-L0)`, with endpoint `s=3/2` and `Lt=3K-2G`:

```text
L0 = (
  9116188274528206532422588359975175944822642875621932695164927062094601175874156892410409968302134032121867359/100014369507341053266557503575567013045764833890500367454634753652406984180130623734364065921383052831883264,
 -6640439869801572382081526887804234460676111328470443390722689647865498662489795081588520547573505231306785215/400057478029364213066230014302268052183059335562001469818539014609627936720522494937456263685532211327533056,
  1352683958531569245473864836594557013082658561575121114009608477646340470549292030061448466155952980891929891/400057478029364213066230014302268052183059335562001469818539014609627936720522494937456263685532211327533056)

Lt = (3048242568040493/8796093022208,
     -17574871620489547/281474976710656,
       4032469574321779/281474976710656)

L(3/2) ≈ (474.24319469645553,-85.35837295341275,19.79870270851295).
```

Endpoint active rows are exactly `T27,TR,SU,SC1,SA5,S102,G,L`. Inactive are all 27 `old_*` rows plus `S9,SC0,SS,H,K`. Every one of the 40 exact raw rows and all 40 normalized own-centred rows `H_i=B_i/(1-B_i·c)` is completely expanded in [P9_XG4_COMPLETE_TABLES.md](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/P9_XG4_COMPLETE_TABLES.md), [p9_xg4_source_rows.csv](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_source_rows.csv), and [p9_xg4_H_all.csv](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_H_all.csv). The eight active normalized-row locators are

```text
T27  (-80.45370632806817, 12.00358100481321, -1.428479477402775)
TR   ( -3.694066581155383,-1.953426863049582,-4.377810405355381)
SU   ( -3.623257927104672,-2.578043134991819, 0.787658481834841)
SC1  ( -1.937871136539903,-9.121759618803386,-3.202453420607413)
SA5  ( -7.716335737000423,-9.736390558609823,-9.225923907825029)
S102 (-28.58611026804412, 21.57205988191304,  7.921389749365022)
G    ( 20.60417680623938,  1.799091554113176, 0.933748786009694)
L    ( 91.17177414426821,-16.40988081065009,  3.806238807170268)
```

## Exact centring, boundedness, and irredundancy

The exact raw volume is the positive rational stored in `endpoint.volume` of [p9_xg4_exact.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_exact.json), with decimal locator `0.0016858357536371645`. The exact ordinary-volume centroid is the rational triple stored in `endpoint.centroid`, with locator

`c=(-0.004012591915208559,0.017183803062927334,-0.042018865598700356)`.

Normalizing every row by `H_i=B_i/(1-B_i·c)` gives the translated body `P_raw-c`. Its three centred first moments are exactly zero. The three dependent moment controls have Jacobian `-V I_3` and determinant `-V^3≠0`, so the centring root is isolated.

An exact positive dependence on `T27,TR,SU,G` sums to zero, proving boundedness. Every active row supports a maximal face, proving irredundancy. Minimum exact raw inactive slack is positive; the directed endpoint box gives centred nonincident lower bound `0.021772808049677957`.

## Exact endpoint incidence

All 12 actual vertices, listed by active triples, are

```text
v0  (T27,TR,SA5)     v1  (T27,TR,S102)
v2  (T27,SU,SC1)     v3  (T27,SU,S102)
v4  (T27,SC1,SA5)    v5  (TR,SA5,G)
v6  (TR,S102,G)      v7  (SU,SC1,L)
v8  (SU,S102,L)      v9  (SC1,SA5,L)
v10 (SA5,G,L)        v11 (S102,G,L)
```

Maximal face cycles:

```text
T27  [4,2,3,1,0]
TR   [6,5,0,1]
SU   [2,7,8,3]
SC1  [4,9,7,2]
SA5  [0,5,10,9,4]
S102 [3,8,11,6,1]
G    [10,5,6,11]
L    [9,10,11,8,7]
```

True edges:

```text
(0,1) (0,4) (0,5) (1,3) (1,6) (2,3) (2,4) (2,7) (3,8)
(4,9) (5,6) (5,10) (6,11) (7,8) (7,9) (8,11) (9,10) (10,11)
```

Exact coordinates, radii, supporting sets, and all incidence slacks are in [p9_xg4_vertices.csv](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_vertices.csv) and [p9_xg4_incidence.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_incidence.json).

## Exact four-page entrance and shared-terminal topology

At `s=0`, three exact dependencies vanish:

```text
{L,K,SU,S102}
{L,K,SA5,SC1}
{L,SS,S102,G}
```

The first two are actual supporting flips. The third fixes the return geometry but is not itself supporting because `K` lies strictly across its plane; this is recorded explicitly rather than promoted to a false hull event.

The four positive-volume polar pages are

```text
P_UL   = conv(0,K,L,SU,S102)
P_AL   = conv(0,K,L,SA5,SC1)
P_G102 = conv(0,K,G,S102)
P_GA5  = conv(0,K,G,SA5).
```

Exact separators prove pairwise-disjoint relative interiors and

```text
P_UL∩P_AL    = conv(0,K,L)
P_UL∩P_G102  = conv(0,K,S102)
P_G102∩P_GA5 = conv(0,K,G)
P_GA5∩P_AL   = conv(0,K,SA5)
opposite page pairs intersect exactly in [0,K].
```

Thus all pages share the same interior radial feature `[0,K]`. The three entrance circuit gradients with respect to `L` have exact nonzero determinant, so entrance shape rank is three; two explicit relative controls independently change page timing/diagonal choice. Together with the three dependent moment controls, the local block has rank six. Full exact volumes, separators, and controls are in [p9_xg4_entrance_topology.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_entrance_topology.json) and [p9_xg4_control_rank_exact.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_control_rank_exact.json).

At `s=1`, exactly `K=(2/3)G+(1/3)L`. The positive terminal cells

```text
C_A5  = conv(0,SA5,G,L)
C_102 = conv(0,S102,G,L)
```

are each pre-triangulated through `K`; exact subvolume sums equal the unsplit tetrahedral volumes. An exact separator places `SA5` and `S102` on opposite sides, proving `C_A5∩C_102=conv(0,G,L)` and disjoint relative interiors. Both share `[0,L]`. The event removes `(G,K,S102),(G,K,SA5),(K,L,S102),(K,L,SA5)`, adds `(G,L,S102),(G,L,SA5)`, and deactivates `K` in one actual higher-valence incidence event. See [p9_xg4_terminal_topology.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_terminal_topology.json).

An exact one-row concurrency theorem explains why this is not the desired single cancellation wall: the intersection line of the two entrance page planes differs from the terminal `G-K` line, and `L0,G,K` are not collinear. With surrounding rows fixed, one nondegenerate `L` cannot simultaneously enter through the page wall and contract `K`. A second shape row or old-plane motion is required.

## Complete wall order and own-centred cell audit

The complete affine atlas enumerates 520 distinct candidate roots and 558 occurrences on `s∈[0,3/2]`. Exact support testing leaves only three actual incidence roots: entrance `s=0`; exact `H` deactivation at `s≈0.05326589812394333`; terminal contraction `s=1`.

Six isolated simple mechanical roots occur:

```text
M1 U-H birth, SA5     0.02242071691660129
M2 U-H death, SA5     0.02305921742228353
M3 S-H birth, K/L     0.15147920222737976
M4 S-H death, K/L     0.15244089339457148
M5 U-H birth, S102    0.37526883061029082
M6 U-H death, S102    0.37875829906852659
```

Exact primitive polynomials, rational isolators, denominator certificates, and Bernstein root-free side covers are in [p9_xg4_event_polynomials.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_event_polynomials.json).

Every open cell was rebuilt from all 40 rows at its own recomputed exact centroid:

| cell | sample `s` | V/E/F | S/U/H | stable |
|---|---:|---:|---:|---|
| pre entrance | `-2^-20` | 16/24/10 | 2/2/2 | T27,K |
| post entrance | 1/1000 | 16/24/10 | 2/2/2 | T27,K |
| M1–M2 | 9/400 | 16/24/10 | 2/3/3 | T27,K |
| M2–H | 1/25 | 16/24/10 | 2/2/2 | T27,K |
| H–M3 | 1/10 | 14/21/9 | 2/2/2 | T27,K |
| M3–M4 | 19/125 | 14/21/9 | 3/2/3 | T27,K,L |
| M4–M5 | 1/4 | 14/21/9 | 2/2/2 | T27,L |
| M5–M6 | 47/125 | 14/21/9 | 2/3/3 | T27,L |
| M6–terminal | 1/2 | 14/21/9 | 2/2/2 | T27,L |
| post terminal | 5/4 | 12/18/8 | 2/2/2 | T27,L |
| endpoint | 3/2 | 12/18/8 | 2/2/2 | T27,L |

The 17 MB certificate [p9_xg4_path_cell_audits.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_path_cell_audits.json) contains, for every cell, every supplied-row face-foot decision, every vertex cone, and all four components of every true-edge cone. The clean-room verifier reconstructs and compares every entry.

## Endpoint equilibrium audit

Face-foot margins are `T27 +0.4142898484`, `L +0.3176702659`; every other active face is excluded, with closest face exclusion `SC1 -0.3712736923`.

The only unstable vertices are target `v6=(TR,S102,G)`, minimum cone coefficient `0.01874230418`, and extra `v8=(SU,S102,L)`, minimum `0.01753754299`. All ten others have a negative cone coefficient; closest excluded vertex is `v9`, margin `-0.01164392579`.

The only saddle edges are

```text
edge (8,11), faces (L,S102):
  (t,1-t,lambda_L,lambda_S102)
  ≈ (0.7479641906,0.2520358094,0.001435369069,0.003869683881)

edge (9,10), faces (L,SA5):
  (t,1-t,lambda_L,lambda_SA5)
  ≈ (0.2135466099,0.7864533901,0.0004748481272,0.005324000805)
```

All other 16 true edges have at least one strict negative component; the closest nonsaddle exclusion is `-0.0002107403193`. Every exact face, vertex, and four-component edge decision is expanded in [P9_XG4_COMPLETE_TABLES.md](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/P9_XG4_COMPLETE_TABLES.md) and [p9_xg4_edges.csv](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_edges.csv).

## How the old DAG obstructions are overcome—and recreated

At the terminal wall, `K` becomes inactive. The old stable sink `K`, old extra source `(SU,S102,K)`, and both old `K` saddle edges therefore genuinely disappear. However, exact wall ordering shows that stable status transfers `K→L` across M3/M4, the SA5 channel relays across M1/M2, and the S102 source channel relays across M5/M6 before `K` contracts.

The endpoint face-witness DAG has sinks exactly `T27,L`; the endpoint radius DAG has sinks exactly protected `v6` and extra `v8`. Exact gaps are

```text
||L||²-||T27||²      ≈ 1977.1386702108975 > 0
r²(v8)-r²(v6)        ≈ 0.060792253964604685 > 0.
```

Exact rational-function and Bernstein certificates keep both gaps positive throughout `s∈[1,3/2]`. Thus `L` cannot drain to `T27`, and `v8` cannot drain to `v6`, without another incidence change or a macroscopic reversal. Full DAGs and persistence proofs are in [p9_xg4_witness_obstruction_exact.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_witness_obstruction_exact.json).

## Positive perturbation box

Directed 190-decimal interval arithmetic permits every one of the 120 raw coordinates to vary independently by `2^-90`, followed by centroid recomputation and normalized-row rebuilding. The same supplied/active inventory, `(12,18,8)` lattice, and `(2,2,2)` class persist. Certified lower bounds are

```text
expected-vertex/nonincident slack  0.021772808049677957
nonvertex-triple violation         0.01909660802330628
oriented tetrahedron volume        3.0490060244161983e-6
projective denominator             0.6292798301474908
positive mechanical primitive      0.0004748481272462103
negative exclusion clearance       0.00021074031928519367
```

Certificate: [p9_xg4_perturbation_interval.json](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_perturbation_interval.json).

## Independent replay and meshes

`verify_p9_xg4_cleanroom.py` imports neither the constructor nor the geometry helper. With standard-library exact `Fraction` arithmetic it independently reconstructs all 11 wall-side bodies, integrates volume and moments, recentres, rebuilds every maximal face and true edge, audits every full normal cone, enumerates the complete affine circuit atlas, certifies all six mechanical roots, verifies the shared-cell topology, and rebuilds both witness DAGs. Terminal marker: `INDEPENDENT EXACT P9-XG4 CLEANROOM PASS`.

The mesh verifier gives 12 vertices, 8 polygonal faces, 18 manifold edges, and 20 triangulated faces in each export; OBJ and STL are watertight, consistently wound, Euler 2, and have zero directed vertex-Hausdorff discrepancy. Their volume errors against the exact solid are below `5e-19`.

A clean extraction of the final archive passed every internal SHA-256 check and reran `RUN_CORE_VERIFIERS.sh` successfully. The archive SHA-256 is `dd3e24cb5801d4a9546fcf11ea19675612feadd861fb26fb926f27dc6ee7f7d4`.

## Search scope, uncertainty, and next forced topology

One-row enumeration sampled 250,000 valid `L` positions; 15,544 deactivated `K` while preserving the target facet, but only three incidence signatures occurred. CMA, SLSQP, radial, common-metric, and added-row probes found no winner. These are empirical discovery results only, not continuum exclusions. The rigorous result is the exact XG4 endpoint, exact one-row concurrency obstruction, exact wall atlas, full mechanics, perturbation box, witness theorem, and clean replay.

The smallest nonrepeating successor requires **at least two independent new shape rows**, or equivalent old-plane motion. One row must enter the `L` residual star while another contracts or bypasses it so the stable-foot death, extra-source death, and both saddle deaths occur before replacement births. A suitable next topology is an octahedral or triangular-prismatic two-row terminal cell spanning `(L,SU,S102)`, `(L,SA5,SC1)`, and the `G/S102` return star, with one actual shared three-dimensional interior cell, two independent antibirth/diagonal controls, and the three translations retained only as dependent moment controls. The comparable alternative is a genuine macroscopic reversal making `||T27||>||L||` and `r²(target)>r²(extra)` in the same rebuilt incidence cell.

## Reusable artifacts

- [Complete exact archive](sandbox:/mnt/data/Steady_Willow_02_P9_XG4_exact_NONWINNER.zip)
- [Full handoff](sandbox:/mnt/data/STEADY_WILLOW_02_P9_XG4_HANDOFF.md)
- [Verification receipt](sandbox:/mnt/data/STEADY_WILLOW_02_P9_XG4_VERIFICATION_RECEIPT.txt)
- [ZIP checksum](sandbox:/mnt/data/STEADY_WILLOW_02_P9_XG4_ZIP_SHA256.txt)
- [Authoritative exact JSON](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_exact.json)
- [Complete exact H/V/E and mechanics tables](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/P9_XG4_COMPLETE_TABLES.md)
- [Entrance topology certificate](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_entrance_topology.json)
- [Terminal topology certificate](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_terminal_topology.json)
- [Every wall-side audit](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4_path_cell_audits.json)
- [Independent verifier](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/verify_p9_xg4_cleanroom.py)
- [OBJ](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4.obj) and [STL](sandbox:/mnt/data/p9_xg4_work/p9_xg4_exact/p9_xg4.stl)
