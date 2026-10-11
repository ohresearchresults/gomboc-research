# figure-0229

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Nimble Comet 79 — J50 cross-linked terminal determination

## Disposition

**EXACT NONWINNER.** `J50_XL2_terminal10` is a finite rational uniform-density convex polyhedron at its own exact ordinary-volume centroid. Its irredundant primal lattice is `(V,E,F)=(16,24,10)`, complexity `48`, and its exhaustive strict equilibrium class is `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The run's acceptance gate requires a materialized finite own-centred body with exactly one stable maximal face, one unstable vertex, no saddle true edges, a complete exact incidence/mechanics audit, an independent verifier, and matching meshes; auxiliary-centre, degenerate, smooth, near-solution, or unexpanded-generator claims do not qualify. :contentReference[oaicite:0]{index=0}

The accepted parent `J49_DO4_terminal8` was exact own-centred `(12,18,8)`, `(2,2,2)`. Its linked double-octahedral ball removed the preceding J48 packet but created stable `7000`, unstable `(2475,7001,7002)`, saddles `(2475,7000)` and `(7000,7002)`, and forcing edge `(7000,7001)`; the journal identified a cross-linked two-circuit terminal volume as the first unclassified successor. :contentReference[oaicite:1]{index=1}

The present branch makes that nonserial topology exit. A connected exact positive-volume 32-tetrahedron annular shell replaces the complete literal J49 dual boundary, removes support `7000`, forcing edge `(7000,7001)`, stable `7000`, cap `(2475,7001,7002)`, and both inherited saddles. Intended stable face `2475` and intended unstable vertex `(2475,5000,5003)` remain strict. The failure is a newly born Euler-neutral packet, not survival or mere relocation of the old labels.

## Reproducible artifacts

- [Complete exact archive](sandbox:/mnt/data/Nimble_Comet_79_J50_XL2_terminal10_exact_NONWINNER.zip)
- [Archive SHA-256 receipt](sandbox:/mnt/data/Nimble_Comet_79_J50_XL2_terminal10_exact_NONWINNER.zip.sha256)
- [Independent verification receipt](sandbox:/mnt/data/Nimble_Comet_79_J50_XL2_terminal10_VERIFICATION_RECEIPT.json)
- [Expanded result report](sandbox:/mnt/data/Nimble_Comet_79_J50_XL2_terminal10_exact_NONWINNER_RESULT.md)
- [Deterministic exact source](sandbox:/mnt/data/J50_XL2_terminal10_exact_source.json)
- [Exact centroid certificate](sandbox:/mnt/data/J50_exact_ordinary_centroid.json)
- [Exact incidence/irredundancy certificate](sandbox:/mnt/data/J50_exact_incidence_irredundancy.json)
- [Exact mechanics summary](sandbox:/mnt/data/J50_exact_mechanics_summary.json)
- [Full exact mechanics ledger](sandbox:/mnt/data/J50_mechanical_ledgers_point.json.gz)
- [Connected positive-volume transition shell](sandbox:/mnt/data/J49_to_J50_connected_positive_volume_shell.json)
- [Residual forcing certificate](sandbox:/mnt/data/J50_residual_forcing_obstruction.json)
- [Two-control response certificate](sandbox:/mnt/data/J50_two_control_exact_response.json)
- [Exact perturbation certificate](sandbox:/mnt/data/J50_exact_metric_perturbation_box.json)
- [First remaining topology certificate](sandbox:/mnt/data/J50_first_remaining_nonserial_successor.json)
- Exact lattice tables: [active H](sandbox:/mnt/data/J50_H_active_exact.tsv.gz), [supplied H](sandbox:/mnt/data/J50_H_supplied_exact.tsv.gz), [V](sandbox:/mnt/data/J50_V_exact.tsv.gz), [maximal-face cycles](sandbox:/mnt/data/J50_maximal_face_cycles.tsv.gz), [true edges](sandbox:/mnt/data/J50_true_edges.tsv)
- Verifiers: [endpoint](sandbox:/mnt/data/verify_nimble_comet79_J50.py), [connected shell](sandbox:/mnt/data/verify_j50_connected_shell.py)
- Meshes: [watertight OBJ](sandbox:/mnt/data/J50_XL2_terminal10.obj), [watertight binary STL](sandbox:/mnt/data/J50_XL2_terminal10.stl)

Archive SHA-256 is `75e71a51ebf1bf6a0d98ebfd19fb9485595a92c83423f0a129177b14c2af730c`. Exact-source SHA-256 is `38ffb964e74ca3ad18e4a8f3e1d54279f8aa6a2ee966f4f2beabf55329660724`; manifest SHA-256 is `06248cab1f92ac25c5fe2094661e6dfdac0ab476b47e81828d939c0f6a45c3c4`; verification-transcript SHA-256 is `a0a29edfba39d7dc0c8f72b2827903872851d14544210a79fb0dfc51b6e45ee7`.

A clean extraction passed the manifest before and after execution. Independent terminal markers are `NIMBLE_COMET79_J50_ENDPOINT_INDEPENDENT_PASS`, `NIMBLE_COMET79_J50_SHELL_INDEPENDENT_PASS`, and `NIMBLE_COMET79_J50_ALL_INDEPENDENT_CHECKS_PASS`.

## Exact finite source and ordinary centroid

The ten supplied supports are all active. In compact local order they are

```text
0  2475
1  0
2  5000
3  5003
4  7001
5  7002
6  7003
7  8000
8  8001
9  8002
```

Their raw dyadic coordinates, with denominators dividing `2^24`, are

```text
2475 = (131619609/16777216, 367860745/16777216, 1805573/8388608)
0    = (26670185/16777216, 10628423/4194304, 240903/16777216)
5000 = (5159793/16777216, -9737161/16777216, -157333/16777216)
5003 = (-8590229/8388608, -9021087/4194304, -135919/16777216)
7001 = (-4007509/2097152, -72289659/16777216, -505463/16777216)
7002 = (-21855311/1048576, -482687007/16777216, -503387/4194304)
7003 = (-244036763/16777216, -283301211/16777216, -661369/8388608)
8000 = (-87611543/16777216, -167071717/8388608, -5373547/16777216)
8001 = (-41463111/16777216, -6139121/524288, -381345/2097152)
8002 = (5235853/8388608, -687349/4194304, -203347/16777216)
```

Build the raw polar primal, compute its exact ordinary volume `V_raw` and first moment `M_raw`, set `c=M_raw/V_raw`, and apply the exact projective translation gauge

`q_i -> q_i/(1-q_i·c)`.

This represents primal translation by `-c`, so `M(u)=M_raw−V_raw u`; the unique moment root is exactly `u=c`, with Jacobian `−V_raw I_3`. Numerically,

`c=(1.5462733228634837,-1.1949954081504457,62.11090753730595)`.

Every projective denominator is positive; the exact minimum is stored in the certificate and is approximately `0.41335812000916072`. The centred moments recompute identically as `(0,0,0)`.

The exact centred volume is

`124450622757253711965609615886153713905066447617441436564091436262484380305653251432380573222243070393571076015439836026722482336953314612244767924206220535649819191712319839655354915961956467359836368449851953854481430046236736207154729533497525692004305710601719762648688228513169990161259899354166807389685997407699332090560512/5498001732259219538453159876594237244227285613367415903506613749151750044030091430135045189789455845990393286935264455769196023255200308893225399857220071823789463333745699523279575414583319172791691212364219544540276453780723862253645961848985548069959150192939599094608440712513845768223994415933374007308901890889191877218025`,

approximately `22.63560995753177`.

## Irredundant H/V/E incidence

The endpoint has `(H,V,E)=(10,16,24)`, 28 coherently oriented display triangles, topology signature `6356b71076b8250ab301742b4dcf8493bac27bfb8dc9e098aa9883092162b12e`, and exact positive minimum supplied-row/nonincident-vertex gap approximately `0.20777915813447398`.

Actual maximal primal face cycles, in exact stored vertex indexing, are

```text
2475 : 0,1,6,5,4,3,2
0    : 7,8,1,0
5000 : 0,2,9,10,11,7
5003 : 2,3,12,9
7001 : 12,13,10,9
7002 : 3,4,14,15,13,12
7003 : 4,5,14
8000 : 5,6,15,14
8001 : 8,11,10,13,15,6,1
8002 : 11,8,7
```

All 24 true primal edges, expressed by their incident maximal-face labels, are

```text
(2475,0)       (2475,5000)   (0,5000)       (2475,8001)
(0,8001)       (2475,5003)   (5000,5003)    (2475,7002)
(5003,7002)    (2475,7003)   (7002,7003)    (2475,8000)
(7003,8000)    (8000,8001)   (0,8002)       (5000,8002)
(8001,8002)    (5000,7001)   (5003,7001)    (5000,8001)
(7001,8001)    (7001,7002)   (7002,8001)    (7002,8000)
```

The OBJ/STL triangulation has 16 vertices, 42 mesh edges, and 28 triangles; every mesh edge has multiplicity two and `16−42+28=2`. Grouping coplanar triangles gives the true lattice identity `16−24+10=2`. Triangulation diagonals are excluded from the true-edge and saddle ledgers.

## Exhaustive full-normal-cone mechanics

Every actual maximal face, all 16 full vertex normal cones, and all 24 full true-edge cones were classified exactly.

```text
stable maximal faces:
  2475
  7001

unstable vertices by incident H labels:
  (2475,5000,5003)
  (2475,7003,8000)

saddle true edges:
  (2475,7002)
  (0,5000)
```

Point margins `(minimum positive / closest excluded)` are

```text
stable:   +0.2078646568186755  / -0.20775972633622397
unstable: +0.20793714427676582 / -0.3184930009448888
saddle:   +0.20774048721345575 / -0.21190141984302854
```

Thus the endpoint is a well-separated open `(2,2,2)` chamber, not a wall point or precision artefact.

## Connected positive-volume transition complex

The transition uses the literal exact J49 raw active dual hull, uniformly scaled by `1/16`, as the inner boundary and the exact J50 raw dual hull as the outer boundary. Uniform scaling preserves J49 mechanics. The old boundary lies strictly inside the new hull, with exact minimum support-plane containment gap approximately `0.0064353165606300996`.

The exact tetrahedral shell has

```text
vertices                  18
edges                     62
triangular faces          78
tetrahedra                32
internal triangular faces 50
boundary triangular faces 28
boundary components        2
Euler characteristic       2
```

The tetrahedron-adjacency graph is connected. Both boundary components are spheres, so the complex is an `S^2×I`-type annular shell. Every tetrahedron has exact positive orientation; every internal triangle has multiplicity two; and the multiplicity-one triangles are exactly the complete old and new boundaries. Its exact rational volume is stored in `J49_to_J50_connected_positive_volume_shell.json` and is approximately `10.249870211965845`. The minimum exact tetrahedron volume is

`46583595171926707714479/1237373475934543186277433344 > 0`,

approximately `3.7647158338143473e-05`.

This is one connected global finite-thickness boundary replacement, not a serial sheet, isolated stellar page, or supporting-face concurrence. It is stronger than the originally suggested one-page cell. It does **not** certify the desired one-parameter chronology: the materialized outer boundary already carries a strict replacement packet.

## Exact old/new feature genealogy

The complete J49 unwanted packet is absent at J50:

- support/stable face `7000` is removed;
- unstable cap `(2475,7001,7002)` is absent;
- saddles `(2475,7000)` and `(7000,7002)` are absent;
- forcing edge `(7000,7001)` is absent.

The intended pair is retained:

- stable face `2475`;
- unstable vertex `(2475,5000,5003)`.

The new strict packet is

- extra stable face `7001`;
- extra unstable vertex `(2475,7003,8000)`;
- saddles `(2475,7002)` and `(0,5000)`;
- residual forcing edge `(7001,7002)`.

Therefore the connected event deletes all named parent defects but relays their Morse packet onto a new free-boundary sector.

## Exact residual forcing theorem

Two row-disjoint true edges survive:

`(2475,0)` and `(7001,7002)`.

For both endpoints of each edge, every external face-stability primitive is exactly positive. Suppose neither endpoint of a true edge `(a,b)` were stable. The only possible failures would be toward one another, giving

`||q_a||²−q_b·q_a <= 0` and `||q_b||²−q_a·q_b <= 0`.

Their sum is `||q_a−q_b||² <= 0`, contradicting the certificate's exact positive squared difference. Each edge therefore forces a stable endpoint, and row-disjointness makes the contributions distinct. Hence `S>=2`; the exhaustive audit attains equality. This is the decisive exact nonwinner obstruction for the certified endpoint chamber.

## Two independent controls after moment elimination

After solving the three exact ordinary-moment equations, two physical support controls remain independent:

- `a` moves support `7001` in the raw `+x` direction;
- `b` moves support `7003` independently in the raw `+x` direction.

The monitored responses are

1. the forcing-sector circuit determinant `det(q7001−q5003,q7002−q5003,q8001−q5003)`;
2. the selected barycentric owner of `2475` for cap `(2475,7003,8000)`.

The exact `2×2` response Jacobian is stored in the certificate. Its determinant is exactly nonzero, approximately `0.0219684811308473`, so the post-centering response rank is two. Forcing-edge deletion and cap/antibirth timing are genuinely independent controls rather than gauge copies of the moment equations.

## Open perturbation chamber

For

`p -> diag(x,y,1)p`, `q -> q diag(1/x,1/y,1)`, with `|x−1|,|y−1| <= 2^-18`,

incidences and exact centroid zero are preserved algebraically. Directed interval replay proves the complete class remains `(2,2,2)` throughout. Certified `(positive lower / excluded upper)` margins are

```text
stable:   +0.20786148415019723 / -0.20775655329407705
unstable: +0.20793714279745037 / -0.31849300020518606
saddle:   +0.2077388986525693  / -0.2118971315353569
```

Thus metric/anisotropic polishing inside this chamber cannot produce a Gömböc.

## Search and attempted falsification

The discovery programme rebuilt the full hull, ordinary centroid, maximal faces, true edges, and mechanics at every accepted state. It enumerated 55 valid one-step topology states and 990 valid two-step states, ranked and retained 300 depth-two states, and optimized selected cells. The exactified endpoint came from depth-two state `d2_244` and path

`[[6,[0,3,4],0.1],[5,[4,6,9],1.0]]`,

with floating pre-exactification hard margin about `0.2077321591213377`. No strict `(1,1,0)` state was found. These searches are empirical discovery/falsification evidence only; the exact nonwinner conclusion follows from the forcing theorem.

## First genuinely unclassified successor

The residual is split over three communicating sectors:

1. forcing component `(7001,7002)` together with stable face `7001`;
2. extra cap `(2475,7003,8000)`;
3. saddle stars `(2475,7002)` and the remote protected-disk edge `(0,5000)`.

The smallest topology not excluded is a **two-boundary-component cross-link or Y-shaped connected terminal three-cell**, equivalently linked octahedral/triangular-prismatic pages sharing an interior edge or face, that spans all three sectors in one actual full-hull incidence event. It must

- preserve stable `2475` and unstable `(2475,5000,5003)`;
- delete true edge `(7001,7002)` and stable `7001`;
- delete extra cap `(2475,7003,8000)`;
- delete both saddles `(2475,7002)` and `(0,5000)`;
- suppress every replacement S–H or U–H birth until those deaths occur;
- retain at least two independent mechanical controls after exact moment elimination.

Within this branch, the smallest robust architecture uses two new extreme supports plus coupled motion and possible deactivation of existing terminal rows. A single stellar page, one-edge clip, supporting-face coincidence, another nested shell lacking an all-sector cross-link, or deformation inside the certified endpoint box is a repetition rather than the next cell.

## Final handoff

`J50_XL2_terminal10` is **USED as an exact topology-changing nonwinner**. It satisfies the finite-source, exact own-centroid, irredundant H/V/E, exhaustive full-cone mechanics, positive-volume connected transition, feature-genealogy, independent-control, perturbation, integrity, independent-replay, and watertight-mesh requirements. It fails the literal Gömböc gate because the exact post-cell matching proves `S>=2`, attained by the audit, and because replacement critical features are already strict at the outer endpoint.

No global nonexistence claim is made. The exact rational M42 `(61,163,104)`, `(2,1,1)` body remains the run-wide equilibrium-count benchmark.
