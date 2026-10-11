# figure-0180

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vivid Quartz 58 — complete low-complexity realization-frontier handoff

## Literal disposition

**Exact NONWINNER.** I did not obtain a homogeneous convex polyhedral Gömböc. The governing gate requires a finite uniform-density polyhedron classified at its own exact volume centroid, with complete V/H incidence, maximal faces, true edges, full normal-cone mechanics, strict margins, independent verification, and meshes. :contentReference[oaicite:0]{index=0} The inherited journal left the full nine-vertex central-triangle realization space open and named the ten-vertex central-quadrilateral disk as the fallback. 

The new work does two things beyond the inherited `E9B` compact-box theorem:

1. It completes the **discrete** nine-vertex frontier: all 50 nonisomorphic simplicial nine-vertex sphere types were generated, connected by legal flips, geometrically realized, and independently checked. Broad and targeted searches over their continuous realizations found no winner, but this is not a CAD or a proof excluding every real realization.
2. It materializes the requested four-internal-vertex fallback exactly: a nonsimplicial central quadrilateral `E10Q`, both strict diagonal resolutions, a robust exact endpoint `E10R`, and a complete exact central-circuit line atlas. Every strict cell is `(2,2,2)`.

## Immutable artifact bundle

- [Portable exact archive](sandbox:/mnt/data/vivid_quartz_58_full_frontier_nonwinner.zip)
- [Archive SHA-256](sandbox:/mnt/data/vivid_quartz_58_full_frontier_nonwinner.zip.sha256): `3493bb012eed40d9d75aeea80fe948d8324daf81561b99789daf3e8f7ebd747e`
- [Complete 617-line determination](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/RESULT.md)
- [README and acceptance semantics](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/README.md)
- [Principal one-command verifier](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/[internal-source-reference].sh)
- [Extended source/census verifier](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/[internal-source-reference].sh)
- [Immutable 91-file manifest](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/SHA256SUMS)

A clean rerun on 1 September 2026 ended with `ALL VIVID QUARTZ 58 PRINCIPAL VERIFIERS PASS`; the independent source/census rerun ended with `ALL VIVID QUARTZ 58 EXTENDED SOURCE/CENSUS VERIFIERS PASS`.

## 1. Accepted exact source chain

The bundle reconstructs `E8A` from its dyadic `2^32` V-data, exact volume and moments, all 12 maximal faces and 18 true edges, strict `(2,2,2)` mechanics, the exact two-control `S>=2` atlas, its `2^-14` coordinate box, independent verifier, OBJ, and STL. See [source `E8A`](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/source_E8A/E8A_exact_report.json).

It likewise reconstructs the inherited `E9B` central-triangle endpoint with `(V,E,F)=(9,21,14)`, strict `(2,2,2)`, stable faces `[1,11,C]`, `[8,A,B]`, unstable vertices `8,C`, saddles `(1,A),(11,12)`, and a `2^-11` box. Its earlier affine-prism family is exactly `U>=2`; that theorem is retained but not promoted to a full realization-space exclusion. See [source `E9B`](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/source_E9B/E9B_exact_report.json) and [its exact three-control certificate](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/source_E9B/E9_prism_exact_certificate.json).

## 2. Complete nine-vertex combinatorial census and geometric search

An edge-flip BFS with graph-isomorphism deduplication gives exactly **50** pairwise nonisomorphic maximal planar graphs on nine vertices. The independent audit verifies all `1225` pairwise nonisomorphism checks, planarity, 3-connectivity, a connected 209-edge flip graph, and one fresh strict Qhull realization of every type. Every realization has `(V,E,F)=(9,21,14)`; the smallest stored nonincidence separation is `0.00032827078731201276`. See [census verification](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/nine_vertex_census_verification.json).

This is combinatorially complete, not a quantifier-elimination proof over all continuous coordinates. The empirical geometric search was deliberately broader than the previous affine-prism family:

|vertices|sampling|draws|strict all-extreme hulls|observed classes|best target score|best class|winners|
|---:|---|---:|---:|---:|---:|---|---:|
|9|sphere|500,000|10,657|42|`-0.015189223762013928`|`(3,2,3)`|0|
|9|normal|500,000|15,070|56|`-0.007436414104906194`|`(2,2,2)`|0|
|10|sphere|500,000|2,766|38|`-0.016479937820132056`|`(2,2,2)`|0|
|10|normal|500,000|4,050|55|`-0.02531279700443834`|`(2,2,2)`|0|

All retained bodies were reconstructed from their actual hulls and classified at their independently integrated ordinary-volume centroids. Targeted determinant-one affine/SPD sweeps covered all 50 types, every intended unstable vertex, and multiple starts. Their best apparent improvements collapsed toward support or volume walls; an independent actual-hull audit rejected all nominal winners. Two targeted `E10R` `(2,1,1)` precursor searches likewise stopped at guard walls. Exact claims and empirical receipts are separated in the [search ledger](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/search_ledger.json).

**Nine-vertex conclusion:** no winner was found in 25,727 strict random nine-vertex bodies or the targeted searches, but the full positive-dimensional realization space remains rigorously open.

## 3. Literal ten-vertex central-quadrilateral replacement

Keep boundary `[1,2,8,10,12,11]` and exterior faces `[11,10,8]`, `[11,12,10]`, `[1,11,8]`, `[2,1,8]`. Rename the old `E9B` internal vertex `C` to `D`, add a new internal vertex `C`, and replace the disk by

```text
[A,1,2] [A,2,8] [A,8,B] [B,8,10] [B,10,12]
[B,12,C] [C,12,D] [D,12,11] [D,11,1] [D,1,A]
[C,B,A,D]
```

The exact patch certificate checks every boundary/interior edge multiplicity and Euler identity. The source is `(9,21,14)`, the quadrilateral wall is `(10,23,15)`, and its strict resolutions are `(10,24,16)`: one selects `A-C`, the other `B-D`. See [exact patch complex](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E9B_to_E10_patch_complex.json).

### 3.1 Exact nonsimplicial wall `E10Q`

Use denominator `2^44`. The central coplanarity is

```text
256 C = -49 A + 207 B + 98 D.
```

Uncentred integer numerators are

```text
1  (10093742548992,-9247256281088,-64571988967424)
2  (20254250186752,-38366003956224,-56690476593152)
8  (32221947693056,-104787513012224,-10890450550784)
10 (17592186044416,0,0)
12 (5555380762624,50861491039744,0)
11 (0,0,0)
A  (26205901996032,59257787789312,-72483135666176)
B  (27661354434560,76150386706688,-26439056156672)
C  (19774490641696,91952991573303,-19955199905632)
D  (6331208511488,108984361185280,-32523675500544)
```

Its exact volume is

`36166131558144182682041072445186489/1298074214633706907132624082305024`.

Its exact ordinary-volume centroid is

```text
Cx = 33423039843067923367394165074091243816169179717/34084356154162348706088076291110631762519130112
Cy = 947037124176688360537487260122278098988546467867/1090699396933195158594818441315540216400612163584
Cz = -59673863753951925212082563673156882502422532751/34084356154162348706088076291110631762519130112
```

The exact moments satisfy `M=VC`; their literal fractions are in the report. Actual maximal faces are

```text
[1,2,8] [1,A,2] [1,8,11] [1,11,D] [1,D,A]
[2,A,8] [8,10,11] [8,B,10] [8,A,B] [10,12,11]
[10,B,C] [12,D,11] [12,C,D] [10,C,12] [C,B,A,D]
```

True edges are

```text
(1,2) (1,8) (1,11) (1,A) (1,D) (2,8) (2,A)
(8,10) (8,11) (8,A) (8,B) (10,12) (10,11) (10,B)
(10,C) (12,11) (12,C) (12,D) (11,D)
(A,B) (A,D) (B,C) (C,D)
```

The wall itself has strict mechanical class `(2,2,2)`: stable `[1,11,D]`, `[8,A,B]`; unstable `8,D`; saddles `(1,A)`, `(11,12)`. Minimum absolute normalized mechanical separation is `0.016201853781111684`; minimum normalized nonincidence separation is `0.018753517740288335`. Its complete polygon-face/full-cone audit is in the [exact wall report](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10Q_wall_exact_report.json) and [H representation](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10Q_wall_H_representation.json).

## 4. Strongest strict exact endpoint `E10R`

From `E10Q`, move only `C` by

```text
C(t)=C(0)+t*(3*2^32)*(-857,-517,217)/2^44,
```

and take `t=1`. With denominator `D=2^44`, the uncentred integer numerators are

```text
1  (10093742548992,-9247256281088,-64571988967424)
2  (20254250186752,-38366003956224,-56690476593152)
8  (32221947693056,-104787513012224,-10890450550784)
10 (17592186044416,0,0)
12 (5555380762624,50861491039744,0)
11 (0,0,0)
A  (26205901996032,59257787789312,-72483135666176)
B  (27661354434560,76150386706688,-26439056156672)
C  (8732129723680,85291497297207,-17159176195936)
D  (6331208511488,108984361185280,-32523675500544)
```

The physical body is `conv{Q_i/2^44-Centroid}`. Exact volume:

`213971509492598276792056534698080359/7788445287802241442795744493830144`.

Exact uncentred first moments:

```text
Mx = 461625902346521489493122309499016693996064659007/17126972312471518572699431633393941636592959488
My = 12354870924780799869144515963563658856821920342817/548063113999088594326381812268606132370974703616
Mz = -828770692768690464739155595431192136256310284605/17126972312471518572699431633393941636592959488
```

Exact ordinary-volume centroid:

```text
Cx = 65946557478074498499017472785573813428009237001/67218332199969876325510481123572617207584129024
Cy = 103822444746057141757516940870282847536318658343/126528625317590355436255023291430808861334831104
Cz = -118395813252670066391307942204456019465187183515/67218332199969876325510481123572617207584129024
```

The exact verifier proves `M_j=VC_j`, hence all centred first moments are exactly zero.

### 4.1 Actual irredundant incidence

Maximal faces:

```text
[1,2,8] [1,A,2] [1,8,11] [1,11,D] [1,D,A] [2,A,8]
[8,10,11] [8,B,10] [8,A,B] [10,12,11] [10,B,12]
[12,D,11] [12,B,C] [12,C,D] [A,D,B] [B,D,C]
```

True edges:

```text
(1,2) (1,8) (1,11) (1,A) (1,D) (2,8) (2,A)
(8,10) (8,11) (8,A) (8,B) (10,12) (10,11) (10,B)
(12,11) (12,B) (12,C) (12,D) (11,D)
(A,B) (A,D) (B,C) (B,D) (C,D)
```

Thus `(V,E,F)=(10,24,16)` and Euler characteristic is two. The true central diagonal is `B-D`; `A-C` is absent. For every oriented triangular face `(i,j,k)`, the deterministic exact H-generator is

```text
n = primitive((Q_j-Q_i) × (Q_k-Q_i)),
h = n·Q_i,
n·x <= h/2^44 - n·Centroid.
```

All 16 integer normals, supports, centred rational right-hand sides, and every exact nonincident slack are in the [complete H representation](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_H_representation.json).

### 4.2 Exhaustive own-centroid mechanics

The strict class is `(S,U,H)=(2,2,2)`: stable `[1,11,D]`, `[8,A,B]`; unstable `8,D`; saddles `(1,A)`, `(11,12)`. The tables below give every feature's normalized signed margin; the [exact endpoint report](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_exact_report.json) stores every exact rational/integer sign numerator and all individual components.

**Every maximal face**

|face|minimum|status|
|---|---:|---|
|`[1,2,8]`|`-0.260582089807641`|inactive|
|`[1,A,2]`|`-0.0237040278289764`|inactive|
|`[1,8,11]`|`-0.120493475715498`|inactive|
|`[1,11,D]`|`+0.156684215106533`|stable|
|`[1,D,A]`|`-0.137190056702279`|inactive|
|`[2,A,8]`|`-0.132917765460736`|inactive|
|`[8,10,11]`|`-0.091562275317205`|inactive|
|`[8,B,10]`|`-0.0180630782926909`|inactive|
|`[8,A,B]`|`+0.0841819574130944`|stable|
|`[10,12,11]`|`-0.0246290951048977`|inactive|
|`[10,B,12]`|`-0.117624070648434`|inactive|
|`[12,D,11]`|`-0.180851009864817`|inactive|
|`[12,B,C]`|`-0.320291952738080`|inactive|
|`[12,C,D]`|`-0.124600949037201`|inactive|
|`[A,D,B]`|`-0.344245866061136`|inactive|
|`[B,D,C]`|`-0.375581340939575`|inactive|

**Every vertex**

|vertex|minimum|status|
|---:|---:|---|
|1|`-0.0907928041686082`|inactive|
|2|`-0.238079547875559`|inactive|
|8|`+0.907587332784202`|unstable|
|10|`-0.0910678046396697`|inactive|
|12|`-0.145726499868903`|inactive|
|11|`-0.0461230121121406`|inactive|
|A|`-0.0482635671233322`|inactive|
|B|`-0.368077509325798`|inactive|
|C|`-0.430632758262508`|inactive|
|D|`+0.596721435927385`|unstable|

**Every true edge; each row uses all four components `(t,1-t,alpha/R,beta/R)`**

|edge|minimum|status|
|---|---:|---|
|`(1,2)`|`-0.347483965705485`|inactive|
|`(1,8)`|`-0.947093306531071`|inactive|
|`(1,11)`|`-0.408276634695343`|inactive|
|`(1,A)`|`+0.101770887558408`|saddle|
|`(1,D)`|`-0.308100390956483`|inactive|
|`(2,8)`|`-0.355603852923153`|inactive|
|`(2,A)`|`-0.0309162226144430`|inactive|
|`(8,10)`|`-0.104308037230026`|inactive|
|`(8,11)`|`-0.0510034846923229`|inactive|
|`(8,A)`|`-0.330442054137510`|inactive|
|`(8,B)`|`-0.0328126844176136`|inactive|
|`(10,12)`|`-0.0354263664745987`|inactive|
|`(10,11)`|`-0.885754035701750`|inactive|
|`(10,B)`|`-0.414654660535379`|inactive|
|`(12,11)`|`+0.129811001105183`|saddle|
|`(12,B)`|`-1.41414214330830`|inactive|
|`(12,C)`|`-0.459933344602788`|inactive|
|`(12,D)`|`-0.248010024645145`|inactive|
|`(11,D)`|`-0.542975232103673`|inactive|
|`(A,B)`|`-0.664933431385976`|inactive|
|`(A,D)`|`-0.0879986775074884`|inactive|
|`(B,C)`|`-2.00314026836488`|inactive|
|`(B,D)`|`-1.13167821597990`|inactive|
|`(C,D)`|`-1.85115324621690`|inactive|

All component quadruples are also printed in the [human-readable exhaustive audit](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_audit.md).

### 4.3 Convexity, separation, neighbourhood, and independent reconstruction

- Minimum exact integer nonincident support slack: `10890450550784`.
- Minimum Euclidean nonincidence distance: `0.13125234225024635`.
- Circumradius-normalized nonincidence distance: `0.018953264416228594`.
- Smallest absolute normalized mechanical separation: `0.018063078292690948`.
- Exact outward interval arithmetic permits all 30 uncentred coordinate entries to vary independently by `epsilon=2^-11=1/2048`, recomputes volume/moments/the dependent own centroid, and preserves `(10,24,16)` and `(2,2,2)`. See [perturbation certificate](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_perturbation_certificate.json).
- A clean-room SciPy/Qhull plus positive-tetrahedron integration plus direct full-cone implementation independently obtains `(10,24,16)`, `(2,2,2)`, volume `27.472942491835518`, centroid `(0.9810799423271623,0.820545109736709,-1.7613619585271878)`, volume discrepancy `3.55e-15`, and maximum centroid-coordinate discrepancy `2.22e-16`. See [independent report](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_independent_verification.json).
- [Centred watertight OBJ](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_centered.obj) and [centred watertight STL](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10R_centered.stl) are winding-consistent and have Euler number two.

## 5. Complete exact ten-vertex line atlas

For `-1/2<=t<=1`, move only `C` by the displayed formula. All `C(10,4)=210` affine circuits were expanded exactly; 18 distinct rational roots lie in the interval, and exactly three alter the actual hull:

|exact `t`|circuit|left diagonal|right diagonal|
|---|---|---|---|
|`-2371522198625001865757073707198545/8471323035938168698741428659945472`|`[8,10,B,C]`|`(8,C)`|`(10,B)`|
|`0`|`[A,B,C,D]`|`(A,C)`|`(B,D)`|
|`879071887965941434982814229041647/3093282218183480863278453416263680`|`[10,12,B,C]`|`(10,C)`|`(12,B)`|

The exact reconstruction yields four strict simplicial incidence chambers `(10,24,16)` and three quadrilateral walls `(10,23,15)`. Three additional component roots split the last incidence chamber, so there are seven strict mechanical cells. Every strict cell and every wall has exactly

```text
stable   [D,1,11], [B,8,A]
unstable 8, D
saddles  (1,A), (12,11)
class    (2,2,2)
```

and the winner-cell count is zero. For every chamber, the [exact line atlas](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10_line_exact_atlas.json) stores the actual maximal faces and true edges, exact coordinates, support signs, all face/vertex/full-edge-cone components, exact volume/moment polynomials, and wall ledgers. With denominator `D=2^44`,

```text
V(t)=V6(t)/(6D^3),
M_j(t)=N_j(t)/(24D^4),
C_j(t)=N_j(t)/(4D V6(t)),
```

so `M_j(t)=V(t)C_j(t)` identically; exact signs prove `V6(t)>0` on every incidence interval. The independent checker samples more than 8,000 strict parameters, reconstructs all four hull types, observes only `(2,2,2)`, and verifies the four-triangle symmetric difference at each flip. See [independent line report](sandbox:/mnt/data/vivid_quartz_58_full_frontier_result/E10_line_independent_verification.json).

## 6. Attempts to break the conclusion

The search did not stop at the inherited affine-prism family. It used all 50 nine-vertex simplicial types, unrestricted random coordinates, determinant-one affine/SPD maps, full-coordinate sequential linearization, actual-hull rechecks of nominal winners, and transverse ten-vertex precursor searches. The best objective values approached zero only while topology separation, volume, or conditioning collapsed. The exact ten-vertex line then crossed three genuine incidence walls without changing a single equilibrium label. These facts strongly support transfer rather than cancellation in the tested low-complexity cells, but they do not prove a global nine-vertex impossibility theorem.

## 7. Exact scope and next frontier

### Proved

- Exact reconstruction of `E8A` and `E9B` and their inherited local forcing theorems.
- A combinatorially complete 50-type census of simplicial nine-vertex convex-polyhedron graphs.
- Exact `E9B -> E10Q` disk insertion, both central-diagonal resolutions, and robust strict endpoint `E10R`.
- Exact volume/moment identities, irredundant H/V/E incidence, exhaustive own-centroid mechanics, `2^-11` perturbation box, independent verification, and matching meshes for `E10R`.
- A complete exact circuit/support/mechanical atlas of the declared ten-vertex line, containing no strict winner.

### Not proved

- The full continuous realization space of any one of the 50 nine-vertex types is not semialgebraically excluded.
- The complete ten-vertex central-quadrilateral realization space is not excluded; only the exact wall, both adjacent resolutions, the declared line, and tested transverse searches are closed.

### Smallest open continuation

The smallest rigorous open frontier remains the full continuous nine-vertex central-triangle realization space outside the inherited affine-prism generator. Within the materialized ten-vertex topology, the next nonrepeating cell must have at least four genuinely transverse controls: separately remove stable `[D,1,11]` and unstable `D`, and force the deaths of saddles `(1,A)` and `(11,12)` to overlap before any compensating birth, while retaining stable `[8,A,B]`, unstable `8`, strict support, and exact ordinary-volume centring. Another one-dimensional central-diagonal sweep is exhausted.

## Reusable conclusion

The requested fallback now exists as a literal exact finite object, but it is not a Gömböc. `E10R` is a robust exact own-centred `(10,24,16)` polyhedron with strict `(S,U,H)=(2,2,2)`. Its fourth internal vertex creates real central-circuit freedom and three actual topology walls, yet on the fully certified line the entire Euler-neutral block persists unchanged. **Explicit disposition: NONWINNER.**
