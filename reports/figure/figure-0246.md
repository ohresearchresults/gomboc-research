# figure-0246

AI research report · 2026-09-03 UTC

---

# Calm Quartz 90 — exact wall-242 seventh two-support carrier cage

## Disposition

**EXACT DELIMITED NONWINNER.** The requested strict own-centred `(S,U,H)=(1,1,0)` polyhedron was not obtained.

A genuinely nonserial two-support antiprismatic/full-star cage was realized exactly. Supports `L=40012` and `M=40013` become extreme; the complete sixth-support packet is destroyed in one connected same-boundary positive-volume surgery; and both endpoints of its adverse edge `[2732,K]` become strictly inactive. The target is an explicit uniform-density rational polyhedron with

```text
23 supplied dyadic points
12 active vertices; 11 strictly inactive rows
(V,E,F,C)=(12,30,20,60)
(S,U,H)=(2,2,2)
positive independent-coordinate radius 2^-22
```

Protected stable face `[0,H,C]` and protected unstable vertex `C` remain strict. The new packet is extra stable `[G,L,M]`, extra unstable `1975`, saddles `[1975,H]` and `[C,L]`, and the sole nonprotected all-external-positive changed edge `[0,1975]`.

The accepted target requires a finite own-volume-centred strict `(1,1,0)` body with full H/V/E and cone evidence, exact or directed perturbation proof, independent replay, and OBJ/STL; theorem-only, auxiliary-centre, wall, and near-solution objects remain inadmissible. :contentReference[oaicite:0]{index=0} The immediate source and requested surgery are the sixth-support endpoint and seventh/two-support cage frontier recorded in the journal. :contentReference[oaicite:1]{index=1}

## What changed relative to the supplied journal

The source had 21 supplied points, 16 active vertices, actual `(16,42,28)`, and strict `(2,2,2)`. Its packet was stable `[2152,G,3296]`, unstable `K`, saddles `[3290,C]`, `[H,K]`, and forcing edge `[2732,K]`. This result:

- makes `2732,K,2152,3290,3296,A` strictly inactive;
- removes `[2732,K]`, `[3290,C]`, and `[H,K]` as physical true edges;
- removes `[2152,G,3296]` as a maximal face;
- inserts two active supports `L,M` inside a connected changed-diagonal cage;
- retains `[0,H,C]` as stable and `C` as unstable;
- exactifies the strongest fully audited endpoint of the searched cage family;
- proves on the canonical exact connector that every one of four replacement births precedes its paired source death.

## Exact supplied generator

All points below are the listed integer triples divided by `2^24=16777216`:

```text
0     (   2382238,   -6308946,   46171779)  active
1258  (   1620887,    4967418,  -20558338)  active
1371  (    105592,     109668,     616980)  inactive
1975  (  10274573,   12571703,   48854565)  active
2152  (    510389,   -7271935,   -5924598)  inactive
2369  (    135538,      76357,     619136)  inactive
2515  (   5028442,   -9339607,   26833667)  active
2732  (     91562,      46167,     611979)  inactive
3290  (    661958,  -10721838,   16427750)  inactive
3296  (   3876214,   -1521484,    3638813)  inactive
A     (   -351024,   -8978438,   25844631)  inactive
B     (         0,          0,          0)  inactive
C     ( -19656014,  -12570508,  -84150451)  active
D     (  -2672244,    3411514,  -42213909)  active
E     (  -6361824,    2058745,  -51264980)  active
F     (  -4952003,    7634514,  -41535864)  active
G     (   7707303,    6512003,   11653439)  active
H     (  -1678613,   11935619,  -25478204)  active
I     (     37357,     237671,     -70651)  inactive
J     (     -7462,    -116421,      97771)  inactive
K     (    203987,     180925,     827032)  inactive
L     (   -481137,  -21134611,    5046486)  active
M     (   -969627,   -4880584,  -35355590)  active
```

Active labels are

```text
0, 1258, 1975, 2515, C, D, E, F, G, H, L, M.
```

Inactive labels are

```text
1371, 2152, 2369, 2732, 3290, 3296, A, B, I, J, K.
```

The exact minimum inactive slacks range from `0.058583383325885641` upward. Every inactivity inequality and its attaining maximal face are in `data/inactive_rows_exact.csv`.

## Exact ordinary volume and physical centroid

```text
Vol = 80332983494983563342019/28334198897217871282176
    ≈ 2.8351951571452911

c = (
 -137290293392733804894378868813/1347763816019774158638734639104,
 -1170897483545235545904071569747/5391055264079096634554938556416,
 -3105272934732849562942858778281/5391055264079096634554938556416
)
  ≈ (-0.10186524653717184,
     -0.2171926322749817,
     -0.57600465634686726).
```

Subtracting this single rational vector from all twelve active points gives exact first moments

```text
Mx=My=Mz=0.
```

`data/positive_tetrahedralization.csv` records all twenty exact signed-volume and first-moment contributions. No auxiliary reference point is used.

## Actual irredundant hull

The twenty outward maximal triangular faces are

```text
[0,2515,1975]
[0,1975,H]
[0,L,2515]
[0,H,C]  **stable**
[0,C,L]
[1258,D,H]
[1258,M,D]
[1258,H,G]
[1258,G,M]
[1975,2515,G]
[1975,G,H]
[2515,L,G]
[C,E,D]
[C,D,M]
[C,F,E]
[C,H,F]
[C,M,L]
[D,E,F]
[D,F,H]
[G,L,M]  **stable**
```

The thirty physical true edges are

```text
[0,1975]
[0,2515]
[0,C]
[0,H]
[0,L]
[1258,D]
[1258,G]
[1258,H]
[1258,M]
[1975,2515]
[1975,G]
[1975,H]  **saddle**
[2515,G]
[2515,L]
[C,D]
[C,E]
[C,F]
[C,H]
[C,L]  **saddle**
[C,M]
[D,E]
[D,F]
[D,H]
[D,M]
[E,F]
[F,H]
[G,H]
[G,L]
[G,M]
[L,M]
```

Every edge has exactly two incident maximal faces and

```text
12-30+20=2.
```

Every nonincident supplied point is strictly behind every supporting plane. The minimum Euclidean nonincidence distance is `0.012466237983338459`. Complete primitive integer H-data are in `data/seventh_cage12_exact_H_irredundant.csv`; exact own-centred V-data are in `data/active_vertices_centered_exact.csv`.

## Exhaustive own-centroid mechanics

Exactly two maximal faces are stable:

- `[0,H,C]` with barycentric coordinates `0.4419946476089137, 0.29525641809808817, 0.2627489342929981` and exact minimum `1617582960162334169030399499192879390420736958970505/6156382573025112962916739612091450864103543185250664` (`≈0.26274893429299812`).
- `[G,L,M]` with barycentric coordinates `0.34209553350963184, 0.2265492588688103, 0.4313552076215579` and exact minimum `14630479150886663831351929519908505450001396080402/64579682246318239967313989373182501889095551931119` (`≈0.2265492588688103`).

Every other face has an exact negative Cramer witness. The closest excluded face is `[0,C,L]` with decision

```text
-16495163207013116027083292056702383251160747725130005/63943643150091722732665002848371647741618856484994522 ≈ -0.25796408203228027.
```

Exactly two active vertices are unstable:

- `1975`: exact minimum raw outgoing support `179216940814946183375515224907702084281/90446898633392045322801268027719417856` (`≈1.981460321169942`, normalized `≈0.4366014020139769`).
- `C`: exact minimum raw outgoing support `452870879405273656102036834784181805879/45223449316696022661400634013859708928` (`≈10.014072041118688`, normalized `≈0.94957679780763316`).

Every other active vertex has an exact negative outgoing witness. The closest is `0` with

```text
-42340719568677480356031641711640111409/90446898633392045322801268027719417856 ≈ -0.46812793150925941.
```

Exactly two true edges are saddles. The four entries below are the edge-foot numerator pair and the two incident full-normal-cone coefficients, followed by their normalized tuple:

- `[1975,H]`

  ```text
  t_num=1447081496789102200556875497622042458449/90446898633392045322801268027719417856
  (1-t)_num=374434780311901751950210341007061914539/90446898633392045322801268027719417856
  beta1_num=37070957020990713045325059758542106606233035970216800799148717272282227819/3757017181107036088926479013177298273576944473936662518963631868931473408
  beta2_num=2285455710577020914331799151578739530131243485084858843346190610102165740821/60112274897712577422823664210836772377231111582986600303418109902903574528
  normalized=(0.7944378620059187, 0.20556213799408127, 0.9812464686406265, 1.244755956340878)
  ```
- `[C,L]`

  ```text
  t_num=555234925008016661709637803713097263939/22611724658348011330700317006929854464
  (1-t)_num=59665121103247008455759072757618011247/11305862329174005665350158503464927232
  beta1_num=5907332237239552135612712929835481453285586753260224089024818872237660965007/60112274897712577422823664210836772377231111582986600303418109902903574528
  beta2_num=1967375818881919609475275390988993390540274655618088475096536251661964467201/15028068724428144355705916052709193094307777895746650075854527475725893632
  normalized=(0.823100497911498, 0.17689950208850197, 1.170640624567692, 1.1879217099759158)
  ```

Every other true edge has at least one exact negative full-cone component. The closest excluded edge is `[0,L]`, normalized tuple `(1.1819252998761773, -0.18192529987617728, 1.0388876637287343, 0.726257312496031)`, decision `≈-0.18192529987617728`.

Thus the complete strict class is exactly

```text
(S,U,H)=(2,2,2),  S+U-H=2.
```

## Connected positive-volume source/target surgery

The exact sixth-support source is augmented only by tiny strictly interior seeds

```text
L=(1,-2,3)/2^24,
M=(-2,1,-3)/2^24.
```

The source and target hulls are reconstructed independently. Their changed-face sets themselves—without any common bridge face—are dual-connected disks with one boundary component and common boundary cycle

```text
[0,1975,H,D,C]
```

interpreted cyclically as `0–1975–H–D–C–0`.

Source patch `(V,E,F)=(14,34,21)`:

- [0,1975,2732]
- [0,2515,3290]
- [0,2515,K]
- [0,2732,K]
- [0,3290,A]
- [0,A,C]
- [1258,2152,D]
- [1258,2152,G]
- [1258,D,K]
- [1258,G,K]
- [1975,2732,K]
- [1975,H,K]
- [2152,2515,3296]
- [2152,2515,C]
- [2152,3296,G]
- [2152,C,D]
- [2515,3290,C]
- [2515,3296,G]
- [2515,G,K]
- [3290,A,C]
- [D,H,K]

Target patch `(V,E,F)=(10,22,13)`:

- [0,1975,2515]
- [0,2515,L]
- [0,C,L]
- [1258,D,H]
- [1258,D,M]
- [1258,G,H]
- [1258,G,M]
- [1975,2515,G]
- [1975,G,H]
- [2515,G,L]
- [C,D,M]
- [C,L,M]
- [G,L,M]

Both have Euler characteristic one and connected dual graph. Coning each patch triangle to that side's exact ordinary centroid yields a positive-volume 3-ball. The smallest source and target cone volumes are, respectively,

```text
source: 7454952508015873158041903790648251484255175/
        2002454525279929201412508023162421149039591424
        ≈ 0.0037229072690046347

target: 89502363216880684468548757063774423227390547/
        2276170732353784735593639898162413991146553344
        ≈ 0.03932146299250866.
```

The exact true-edge symmetric difference is:

**Removed source edges**

```text
[0,2732] [0,3290] [0,A] [0,K]
[1258,2152] [1258,K]
[1975,2732] [1975,K]
[2152,2515] [2152,3296] [2152,C] [2152,D] [2152,G]
[2515,3290] [2515,3296] [2515,C] [2515,K]
[2732,K]
[3290,A] [3290,C]
[3296,G]
[A,C]
[D,K] [G,K] [H,K]
```

**Inserted target edges**

```text
[0,L]
[1258,H] [1258,M]
[1975,2515] [1975,G]
[2515,L]
[C,L] [C,M]
[D,M]
[G,H] [G,L] [G,M]
[L,M]
```

Inherited edges with changed incident stars:

```text
[0,1975] [0,2515] [0,C]
[1258,D] [1258,G]
[1975,H] [2515,G]
[C,D] [D,H]
```

This proves an actual finite-thickness full-hull incidence surgery; it is not a frozen-fan comparison or display-diagonal surrogate.

## Exact predecessor-lineage deletion

The transition certificate verifies all of the following on the actual source and target hulls:

```text
[2732,K] absent in target;
2732 and K strictly inactive;
[2152,G,3296] absent as a target maximal face;
K absent from the target unstable set;
[3290,C] and [H,K] absent as target true edges;
[0,H,C] remains stable;
C remains unstable.
```

Therefore the source packet is destroyed, not renamed. The target packet is a distinct feature complex:

```text
stable    [G,L,M]
unstable  1975
saddles   [1975,H], [C,L]
carrier   [0,1975].
```

## Complete changed-edge external-arrow census

All thirty target edges were audited. The census separately checks all thirteen inserted edges and all nine inherited star-changed edges. Of these twenty-two changed edges, twenty-one have an explicit strictly negative external directed-support witness. The only adverse changed edge is inherited `[0,1975]`.

The only all-external-positive target edges are

```text
[0,1975]
[C,E].
```

`[C,E]` is unchanged and belongs to the protected unstable-`C` star. It is not an unexamined replacement carrier. The complete per-arrow ledger is in `data/external_arrow_full_ledger.csv` and `certificates/external_arrow_design_certificate.json`.

At the exact centre, the smallest chosen negative witness magnitude among the nonprotected changed edges is at least `0.4681279315092594`; over the full perturbation box it remains at least

```text
273211050111328495770066295382535199919295563520574128962654516510706306540162287593/583690828709134926161699140774892458435148761894070683100480068266263665463972069376
≈ 0.46807494083049084.
```

## Exact residual forcing theorem

True edge `[0,1975]` is incident to `[0,2515,1975]` and `[0,1975,H]`. Every external endpoint arrow is positive. The exact minimum is

```text
340885182086790056349119548259486912471/90446898633392045322801268027719417856
≈ 3.7688985165594038.
```

The mutual arrows are

```text
sigma(0→1975)=-42340719568677480356031641711640111409/90446898633392045322801268027719417856
sigma(1975→0)=179216940814946183375515224907702084281/90446898633392045322801268027719417856
```

and satisfy

```text
sigma(0→1975)+sigma(1975→0)
=||p_1975-p_0||²
=212982599567611/140737488355328>0.
```

If neither endpoint were unstable while every external arrow stayed positive, both mutual arrows would have to be nonpositive, contradicting the identity. Thus one endpoint is unstable in addition to strict unstable `C`; in the actual endpoint it is `1975`. The theorem persists throughout the certified box.

## Exact death-before-birth chronology

The canonical connector is the exact coordinate chord from the sixth-support source with tiny interior `L,M` seeds to the target, with the physical ordinary centroid recomputed at every parameter `t`. The certificate isolates one simple root for each of the eight decisive packet sheets. The coarse rational brackets below are exact isolating intervals; the stored refined brackets have width at most `1/5070602400912917605986812821504000` and are independently replayed by Sturm counts and side-cell mechanics.

| replacement birth | exact bracket | root approx. | paired source death | exact bracket | root approx. |
|---|---:|---:|---|---:|---:|
| `replacement_stable_1258_2152_G_birth` | `[157/4000,79/2000]` | `0.039485063641251` | `source_stable_2152_3296_G_death` | `[179/4000,9/200]` | `0.044847184890729` |
| `replacement_saddle_1975_H_birth` | `[1313/4000,657/2000]` | `0.328347274680365` | `source_saddle_H_K_death` | `[67/200,1341/4000]` | `0.335005924191717` |
| `replacement_unstable_1975_birth` | `[103/250,1649/4000]` | `0.412213810361768` | `source_unstable_K_death` | `[827/2000,331/800]` | `0.413615289347148` |
| `replacement_saddle_C_L_birth` | `[66/125,2113/4000]` | `0.528089713894730` | `source_saddle_3290_C_death` | `[271/500,2169/4000]` | `0.542229067164772` |

The ordering is therefore

```text
replacement stable [1258,2152,G] birth  < source stable [2152,3296,G] death
replacement saddle [1975,H] birth        < source saddle [H,K] death
replacement unstable 1975 birth          < source unstable K death
replacement saddle [C,L] birth           < source saddle [3290,C] death.
```

The exact side ledgers exhibit the overlap chambers `(3,2,3)` for stable/saddle transfers and `(2,3,3)` for the unstable transfer. These four strict inequalities already rule out death-before-birth cancellation of the complete packet on this connector. The certificate does not claim to be an all-wall atlas of every mechanically neutral path event; it isolates exactly the source/target packet events needed for the obstruction.

## Positive own-centroid perturbation chamber

Every one of the 69 uncentred supplied coordinates may vary independently by

```text
|delta r_ij| <= 2^-22 = 1/4194304.
```

The directed interval verifier recomputes volume, all three first moments, the dependent common centroid, incidence, all face signs, all sixty directed vertex primitives, all 120 true-edge cone components, inactivity, anti-carrier witnesses, and the forcing theorem. It preserves the exact `(12,30,20)`, `(2,2,2)` chamber.

Certified box-wide lower clearances are

```text
topology/nonincidence  0.013254317149861229
chosen face signs      0.084870601507649884
chosen vertex signs    0.46807494083049084
chosen edge components 0.035213910833946295
forcing external       3.7688408088682404
anti-carrier witnesses 0.46807494083049084.
```

The exact volume interval is

```text
[80332725166250828779739/28334198897217871282176,
 26777747274570992801657/9444732965739290427392].
```

Larger tested radii through `2^-21` fail closed in topology/face-Gram interval tests; no maximal-radius claim is made.

## Independent verification

The package has eight replay layers:

1. `scripts/generate_candidate.py` — deterministic exact target/source generation and all finite ledgers;
2. `scripts/build_chronology.py` — exact packet-wall polynomial construction and root isolation;
3. `scripts/verify_chronology.py` — independent Sturm/side-ledger chronology replay;
4. `scripts/verify_interval_own_centroid.py` — directed `2^-22` physical-coordinate box;
5. `scripts/verify_exact.py` — primary exact reconstruction;
6. `scripts/verify_independent.py` — standard-library-only clean-room reconstruction importing neither generator logic nor `exact_core.py`;
7. `scripts/find_minimal_bridge_patch.py` — exact zero-bridge same-boundary replay;
8. `scripts/verify_mesh.py` — OBJ/STL orientation, incidence, Euler, and watertightness audit.

The aggregate marker is

```text
ALL_CALM_QUARTZ_90_WALL242_SEVENTH_CAGE_VERIFIERS_PASS.
```

The OBJ contains twelve vertices and twenty outward triangular faces; its thirty edge classes all have multiplicity two. The STL has the same twenty facets.

## Discovery record and falsification attempts

The promoted theorem does not rely on numerical search. Discovery nevertheless covered:

```text
one-support unique topologies tested     22773
one-support valid protected hulls         11883
one-support packet-deleted records        4238

two-support unique topologies tested      58444
two-support valid protected hulls          18290
two-support packet-deleted records         6022
two-support retained candidates            7500

fixed-topology metric systems screened     805
fixed-topology numerical winners           0
selected-topology metric evaluations       604194
joint shape/metric evaluations             187832.
```

No numerical strict winner appeared. The minimum number of adverse changed carriers in both enumerated one- and two-support families was one. These are observations under finite discovery protocols, not exclusion theorems.

## Exact scope

Closed exactly:

- this materialized two-support `L,M` carrier cage and its old-row releases;
- its complete `2^-22` own-centroid mechanics chamber;
- exact destruction of every sixth-support packet feature;
- the complete 13-inserted/9-star-changed external-arrow census;
- the zero-bridge connected same-boundary positive-volume transition;
- the eight decisive exact source-to-target chronology events;
- the external-positive `[0,1975]` forcing chamber.

Not closed:

- every seventh-support or two-support placement;
- every alternative released-row set or boundary;
- every three-support closed cage;
- the global existence problem.

## First genuinely nonrepeating successor

The endpoint incidence exposes four legal local exchanges:

```text
[0,1975] -> [2515,H]      forcing-edge escape
[G,M]    -> [1258,L]      death sheet of stable [G,L,M]
[1975,H] -> [0,G]         saddle exchange
[C,L]    -> [0,M]         saddle exchange.
```

Performing these as serial flips would repeat the transfer mechanism. The first evidence-supported nonrepeating successor is a **closed three-support antiprismatic/hexahedral cage**, or an eighth support `N` with coordinated release/deactivation of `0` or `1975`, that places the entire `[0,1975]` star, `[G,L,M]`, and both saddles inside one communicating positive-volume cell. It must preserve `[0,H,C]` and `C`, and it must enforce a negative external arrow on every inserted or star-changed nonprotected edge before the dependent moment equations are solved.

## Final statement

**NONWINNER, rigorously delimited.** The two-support cage genuinely annihilates the complete sixth-support carrier packet and releases both endpoints `2732,K`. The endpoint is a compact exact own-centred `(2,2,2)` body with a large open coordinate chamber. It fails because inherited star-changed edge `[0,1975]` is the unique nonprotected adverse carrier, and every paired replacement feature is born before its source counterpart dies on the canonical connector.


## Delivered artifacts

- [Complete exact NONWINNER archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER.zip)
- [Complete Markdown handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_COMPLETE_HANDOFF.md)
- [Structured wrapper result](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_COMPLETE_RESULT.json)
- [Clean-extraction verification receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_clean_verification.json)
- [Clean package replay](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_clean_replay.txt)
- [Fresh clean replay from this continuation](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_clean_replay_final.txt)
- [Exact 23-point generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/generator_exact.json)
- [Supplied exact V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/input_vertices_exact.csv)
- [Exact own-centred active V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Primitive irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/seventh_cage12_exact_H_irredundant.csv)
- [All maximal-face mechanics](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/seventh_cage12_exact_faces.csv)
- [All 60 directed vertex primitives](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/seventh_cage12_exact_vertex_primitives.csv)
- [All 30 true edges and 120 full-cone components](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/seventh_cage12_exact_true_edges_full_cones.csv)
- [Complete external-arrow ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/data/external_arrow_full_ledger.csv)
- [Exact same-boundary transition certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/certificates/seventh_cage_shared_global_patch.json)
- [Exact packet chronology](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [External-arrow anti-carrier certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/certificates/external_arrow_design_certificate.json)
- [Residual forcing-edge certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/certificates/residual_forced_edge_0_1975.json)
- [Own-centroid perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent clean-room verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/scripts/verify_independent.py)
- [Aggregate verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/RUN_ALL_VERIFIERS.sh)
- [Package verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/verify_package.py)
- [SHA-256 manifest](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/SHA256SUMS.txt)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_seventh_cage_exact_NONWINNER/mesh/body.stl)

## Package integrity

```text
archive SHA-256  6474b45d1c446f51481e42249077bb94ff1b3bc9aeaa59c3ee6a43496fe3b5b1
archive bytes    1736079
manifest entries 57
manifest SHA-256 2e121660eedf7f5ca84e499645ac90a626f615ce0a52103dd4cc86b4c50f6e90
clean extraction PASS
fresh replay SHA-256 43dc721aebb4f4cadbfb7ea7be24dd6d095d7dcb579555ee95a0ceadee6ca970
```
