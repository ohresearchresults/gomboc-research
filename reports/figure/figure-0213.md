# figure-0213

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Nimble Comet 79 — exact J48 codimension-three interior-cell determination

## Literal verdict

**EXACT NONWINNER.** I replaced the failed `J47_D12_terminal_post8` supporting-face concurrence by a genuine positive-volume, one-boundary-component three-dimensional attachment and exactified the resulting body. The strongest endpoint, `J48_C3_terminal7`, is a rational homogeneous convex polyhedron at its own exact ordinary-volume centroid with irredundant `(H,V,E)=(7,10,15)` and strict full-normal-cone class `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

This materially advances the journal frontier: the accepted parent was `(8,12,18)`, own-centred `(2,2,2)`, and its D12 construction collapsed into a supporting face while two row-disjoint forcing edges certified `S>=2`; the journal therefore required a true codimension-three interior volume rather than another boundary concurrence. :contentReference[oaicite:0]{index=0} No accepted winner supersedes the exact M42 `(2,1,1)` benchmark. :contentReference[oaicite:1]{index=1}

## Reproducible artifacts

- [Complete exact archive](sandbox:/mnt/data/Nimble_Comet_79_J48_C3_terminal7_exact_NONWINNER.zip)
- [Archive SHA-256 receipt](sandbox:/mnt/data/Nimble_Comet_79_J48_C3_terminal7_exact_NONWINNER.zip.sha256)
- [Expanded result report](sandbox:/mnt/data/Nimble_Comet_79_J48_C3_terminal7_exact_NONWINNER_RESULT.md)
- [Deterministic exact source](sandbox:/mnt/data/J48_C3_terminal7_exact_source.json)
- [Positive-volume cell certificate](sandbox:/mnt/data/J47_to_J48_C3_positive_volume_cell.json)
- [Exact perturbation-box certificate](sandbox:/mnt/data/J48_exact_metric_perturbation_box.json)
- [Independent verifier](sandbox:/mnt/data/verify_nimble_comet79_J48.py)
- [Watertight OBJ](sandbox:/mnt/data/J48_C3_terminal7.obj)
- [Watertight binary STL](sandbox:/mnt/data/J48_C3_terminal7.stl)

Archive SHA-256 is `c4cc381b6685aac83189de2ae27a39fbca25af56630ff120922b245e7813f958`. From a fresh extraction, `sha256sum --quiet -c MANIFEST.sha256`, the independent verifier, and a second manifest check all passed. The terminal marker is `NIMBLE_COMET79_J48_C3_ALL_INDEPENDENT_CHECKS_PASS`.

## Exact deterministic construction

Start from the exact parent source included as `source/J47_parent_exact_source.json`. In its raw projective gauge, scale all ten supplied parent rows by `1/10`, retain parent labels

`[2475,4229,2490,5001,0,2463,2467,5000,5003,5002]`,

and append three new dyadic rows:

- `q_6000=(-580135/524288, -86267547/16777216, -447823/8388608)`;
- `q_6001=(-57990701/4194304, -138137953/8388608, -1343845/8388608)`;
- `q_6002=(22473051/8388608, 17461039/16777216, -785611/8388608)`.

The raw active set is exactly `[2475,0,5000,5003,6000,6001,6002]`. Form the polar primal, compute its exact ordinary volume `V_raw` and first moment `M_raw`, set `c=M_raw/V_raw`, and apply the exact projective translation gauge

`q_i -> q_i/(1-q_i·c)`.

This represents translation of the primal by `-c`; hence `M(u)=M_raw-V_raw u`, the unique dependent root is `u=c`, and the Jacobian is exactly `-V_raw I_3`. Numerically, `c=(3.5191348470542376,-1.7592623730004875,91.25355237774367)`. Every projective denominator is positive; the minimum is approximately `0.5139201659940735`. The centred first moments recompute exactly as `(0,0,0)`.

The exact centred primal volume is

`37908839685022874629548811380843761633225034270661638754940492733905925394989591765728387263200557373062401598029582064827333940333341426232177464789890060042848239234798382488558924510159169507215699190781599876393241409653547166910464539206921984506571464598708215415915122967416292606089847196932729780817372583161043559280010203786608539172693195111676303547633701492215074068413861730799954780797216554244517755092992 / 391613031890748137664607096558756561442871268808819887558065449376969429563317809216482161385170276668082452084066945530970715069009295234037059178529732618834738228801425736842829222321513047749972925167474896136511090334325803471104499964739708879525995363509706467244786164781693189701898950977449998330500187132462722204062728691127843803743263547858400713306908921515164855224868075805964412521769130933991476838615`,

approximately `96.801782877334503`.

## Actual irredundant H/V/E lattice

There are thirteen supplied rows and seven active maximal faces. Parent rows `4229,2490,5001,5002` become strictly inactive; inherited inactive rows `2463,2467` remain inactive. The minimum exact supplied-row/nonincident-vertex gap is positive and approximately `0.035502602007211691`. The topology signature is `f0fac387981d4a2a8058f860f5ebf84b7caf8aa21e4eff22044e3fef91d7bbb7`.

With primal vertices numbered as in `body/V_exact.tsv.gz`, the actual maximal-face cycles are:

- `2475 : 0,1,5,4,3,2`
- `0 : 6,1,0`
- `5000 : 0,2,7,8,6`
- `5003 : 2,3,7`
- `6000 : 3,4,9,8,7`
- `6001 : 4,5,9`
- `6002 : 6,8,9,5,1`

All fifteen true edges, listed by their two incident H labels, are:

`2475-0, 2475-5000, 2475-5003, 2475-6000, 2475-6001, 2475-6002, 0-5000, 0-6002, 5000-5003, 5000-6000, 5000-6002, 5003-6000, 6000-6001, 6000-6002, 6001-6002`.

The exported triangulation has ten vertices, twenty-four mesh edges, and sixteen oriented triangles, so `10-24+16=2`; every mesh edge has multiplicity two. Grouping coplanar triangles into the seven actual maximal faces gives the irredundant polyhedral identity `V-E+F=10-15+7=2`. The nine triangulation diagonals are not true polyhedral edges and are never classified as mechanical saddle edges. Both OBJ and STL are watertight.

## Positive-volume codimension-three interior cell

The parent and post dual support hulls share exactly the preserved intended-pair disk

- `(2475,0,5000)`;
- `(2475,5000,5003)`.

The complementary ten-triangle J47 attachment disk—which contains the complete non-target packet—is replaced by an eight-triangle free disk. Their common boundary cycle is

`2475 -> 0 -> 5000 -> 5003 -> 2475`.

The closed transition complex is one connected three-ball with:

- 11 vertices;
- 35 edges;
- 41 triangular faces;
- 16 positive-volume tetrahedra;
- 23 internal triangular faces;
- boundary `(V,E,F)=(11,27,18)` and Euler characteristic 2;
- ball Euler characteristic `11-35+41-16=1`.

Its exact support-space volume is

`141387135570941741843802643249437111353901960604363710169299887761099 / 78984218751417890023438520762752824239171321550411833440733233152000`,

approximately `1.7900681655904032`. The minimum tetrahedron volume is the positive exact rational

`41230993337070125493442301714573801945049266810124322621199871 / 526561458342785933489590138418352161594475477002745556271554887680`.

For each insertion of `6000`, `6001`, and `6002`, the certificate identifies the visible boundary facets, proves every coned tetrahedron has positive orientation, and proves that their exact volume sum equals that convex-hull volume increment. Across all sixteen tetrahedra, the multiplicity-one faces are exactly the old attachment disk together with the new free disk; every other face has multiplicity two, and the tetrahedron adjacency graph is connected. The sixteen tetrahedra are therefore a shelling/replay of **one** finite-thickness boundary-cell attachment, not sixteen serial sheets.

The three new supports are locally minimal in this fixed preserved-pair architecture. Removing `6000` leaves parent row `2490` outside the candidate hull; removing `6001` leaves an exact separating facet `(2475,6000,6002)` with the origin outside; removing `6002` leaves separating facet `(0,5000,6001)`. Thus all three supports are individually necessary for this C3 attachment. This is deliberately a local minimality statement, not a theorem excluding every unrelated two-support construction.

## Packet removal and preservation of the intended pair

The old attachment disk contains all inherited non-target features:

- extra stable row `2490`;
- extra unstable facet `(2475,4229,5002)`;
- saddles `(2475,4229)` and `(2490,5001)`;
- row-disjoint forcing edges `(2475,5001)` and `(4229,2490)`.

At `J48_C3_terminal7`, rows `4229,2490,5001,5002` are all strictly inactive. Both inherited forcing edges and every inherited non-target equilibrium are absent. The intended pair is preserved exactly:

- stable maximal face `2475`;
- unstable vertex with incident H triple `(2475,5000,5003)`.

Thus the construction actually leaves the J47 forcing chamber; it does not merely move the old witnesses along another sheet.

## Exhaustive full-normal-cone mechanics

Every one of the seven maximal faces, ten primal vertices, and fifteen true edges was classified with exact rational primitives and complete normal cones.

The exact equilibrium set is:

- stable faces: `2475`, `6000`;
- unstable vertices, by incident H triples: `(2475,5000,5003)`, `(2475,6001,6002)`;
- saddle true edges: `(2475,6000)`, `(6000,6002)`.

Point margins `(minimum positive; closest excluded)` are:

- stable: `(0.36886681225670803; -0.58209901700665945)`;
- unstable: `(0.0019766128445717272; -0.0021730536732610275)`;
- saddle: `(0.035261545909964095; -0.00046531973474686362)`.

Therefore the endpoint is an open strict `(2,2,2)` body, not a wall point.

## Precise residual obstruction

Both inherited forcing edges were removed, but the post-cell topology creates a new row-disjoint true-edge matching:

- `(2475,0)`;
- `(6000,6001)`.

For each edge `(a,b)`, every external face-stability primitive at both endpoints is exactly positive. If neither endpoint were stable, the two mutual inequalities would sum to

`||q_a||^2-q_b·q_a + ||q_b||^2-q_a·q_b = ||q_a-q_b||^2 <= 0`,

contradicting the certified positive squared difference. Hence each row-disjoint edge forces at least one stable endpoint. The matching proves `S>=2`, and the exhaustive audit attains equality. This is the first exact residual obstruction after the genuine interior-cell exit.

The transferred post packet is:

- extra stable `6000`;
- extra unstable `(2475,6001,6002)`;
- saddles `(2475,6000)` and `(6000,6002)`;
- forcing edge `(6000,6001)` as the nonprotected matching component.

## Positive perturbation margin

Let

`A(s)=I+s0 diag(1,0,-1)+s1(E12+E21)+s2(E13+E31)+s3 diag(0,1,-1)+s4(E23+E32)`

with every `|s_k|<=2^-17`, and transform `p -> A p`, `q -> q A^-1`. Incidences are preserved algebraically and a body centred at zero remains centred at zero.

The independent outward-rational interval replay proves throughout this full five-dimensional box:

- `det A` lies in `[1125865547235325/1125899906842624, 281483566776321/281474976710656]`;
- the Gershgorin eigenvalue lower bound is `32767/32768`;
- all active and inactive incidence decisions remain strict;
- every full face, vertex, and true-edge cone retains its sign;
- the class remains `(2,2,2)`;
- unstable positive lower / excluded upper margins are `0.0018164981731893775 / -0.0019556661322739752`;
- saddle positive lower / excluded upper margins are `0.035227930917569643 / -0.00016341589277088018`.

Metric polishing inside this box is therefore rigorously closed.

## What was tried and what changed relative to the supplied journal

I reconstructed the exact J47 source and its true maximal-face/edge lattice, isolated the complete complementary boundary disk carrying the two forcing mechanisms, searched connected three-support replacements rather than appending a sheet, exactified the first robust full-packet replacement, and then tried to break it by:

- deleting each new support separately;
- testing all supplied-row/nonincident-vertex inequalities;
- recomputing ordinary volume and all first moments independently;
- rebuilding every maximal face and true edge from the exact H data;
- auditing every full face, vertex, and edge cone;
- certifying a full five-dimensional nonsingular linear/metric chamber around the endpoint;
- replaying the cell as a positive tetrahedral shelling;
- verifying both mesh formats independently.

The decisive change is that the old D12 face coincidence is gone and the old forcing matching is genuinely deleted through a positive-volume 3-ball. The failure mode is no longer inherited J47 geometry: it is the newly identified `(2475,0)/(6000,6001)` matching and its attached Euler-neutral packet.

## First remaining nonserial successor

The smallest topology not excluded by the exact endpoint theorem is a single connected double-octahedral or triangular-prismatic terminal three-ball spanning the entire `6000` star and the cap `(2475,6001,6002)`. In one actual boundary-incidence event it must simultaneously:

1. delete true forcing edge `(6000,6001)`;
2. destroy stable row `6000`;
3. destroy saddle `(2475,6000)`;
4. destroy saddle `(6000,6002)`;
5. destroy unstable facet `(2475,6001,6002)`;
6. suppress every replacement U-H birth until those deaths have occurred;
7. preserve stable row `2475` and unstable facet `(2475,5000,5003)`.

After reserving three dependent controls for the ordinary moments, the incidence stratum needs at least two independent mechanical controls: one governing deletion of the `6000-6001` forcing component and one governing the `2475-6001-6002` cap/antibirth channel. Another supporting-face concurrence, another serial sheet, or motion confined to the certified metric box is not a distinct continuation.

## Independent replay and scope

From the extracted archive root run:

`bash [internal-source-reference].sh`

The standard-library verifier independently reconstructs the exact raw source, projective centroid gauge, complete irredundant H/V/E lattice, exact volume and moments, all normal-cone mechanics, the 16-tetrahedron positive-volume cell, inherited-packet deletion, residual forcing proof, three-support local minimality, perturbation box, and OBJ/STL topology.

This is a complete exact finite determination for the realized J47-to-J48 architecture. It is **not** a global nonexistence theorem for homogeneous polyhedral Gömböcs or for every conceivable two-support volume. `J48_C3_terminal7` is the strongest exact endpoint of this branch, while the exact M42 body remains the run-wide best equilibrium-count benchmark at `(2,1,1)`.
