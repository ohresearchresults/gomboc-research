# figure-0237

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Comet 79 — J52 four-arm anti-carrier determination

## Reproducible handoff bundle

- Complete exact archive (`Nimble_Comet_79_J52_A4_terminal8_exact_NONWINNER.zip`)
- Archive SHA-256 receipt (`Nimble_Comet_79_J52_A4_terminal8_exact_NONWINNER.zip.sha256`)
- Expanded report (`Nimble_Comet_79_J52_A4_terminal8_exact_NONWINNER_RESULT.md`)
- Independent verification receipt (`Nimble_Comet_79_J52_A4_terminal8_VERIFICATION_RECEIPT.json`) and clean-extraction transcript (`Nimble_Comet_79_J52_A4_terminal8_VERIFICATION_TRANSCRIPT.txt`)
- Deterministic exact source (`J52_A4_terminal8_exact_source.json`)
- Endpoint certificates: ordinary centroid (`J52_exact_ordinary_centroid.json`), irredundant incidence (`J52_exact_incidence_irredundancy.json`), mechanics summary (`J52_exact_mechanics_summary.json`), full mechanics ledger (`J52_mechanical_ledgers_point.json.gz`)
- Transition certificates: positive-volume shell and all-sector spine (`J51_to_J52_A4_connected_positive_volume_shell.json`), feature genealogy (`J51_to_J52_feature_genealogy.json`), complete external-arrow census (`J52_complete_external_arrow_census.json`), residual forcing proof (`J52_residual_forcing_obstruction.json`), death-before-birth chronology obstruction (`J52_death_before_birth_chronology.json`), two-control response (`J52_two_control_exact_response.json`), perturbation chamber (`J52_exact_metric_perturbation_box.json`), and next topology (`J52_first_remaining_nonserial_successor.json`)
- Exact lattice tables: active H (`J52_H_active_exact.tsv.gz`), supplied H (`J52_H_supplied_exact.tsv.gz`), V (`J52_V_exact.tsv.gz`), maximal-face cycles (`J52_maximal_face_cycles.tsv.gz`), true edges (`J52_true_edges.tsv`), all nonincidences (`J52_nonincident_all.tsv.gz`)
- Independent code and meshes: endpoint verifier (`verify_nimble_comet79_J52.py`), perturbation verifier (`verify_j52_shape_box.py`), exact geometry library (`J52_exact_geometry.py`), watertight OBJ (`J52_A4_terminal8.obj`), watertight STL (`J52_A4_terminal8.stl`)

Archive SHA-256: `e390209e6f86890719a346a96d5d1b803e70ade7d8110332e82b22f1ae07b00b`. Exact-source SHA-256: `7564ed131a4df85d2f52bd1f4fc86464946295805e66a7c6ea59b36c5bb70661`. Integrity-manifest SHA-256: `aa8f67f304a55c20dfe7fbe0629915033fda8693c65c1bd4d9801a0ff580a9ef`. The clean extraction reproduced all three terminal markers and passed the internal manifest.

## Finite verdict

**EXACT NONWINNER.** `J52_A4_terminal8` is a finite rational homogeneous convex polyhedron at its own exact ordinary-volume centroid. Its irredundant lattice is

`(H,V,E)=(8,12,18)`, equivalently primal `(V,E,F)=(12,18,8)`, complexity `36`,

and its exhaustive strict equilibrium class is `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The operation is genuinely nonserial. A connected exact 43-tetrahedron two-boundary annular terminal complex, containing a connected 14-tetrahedron, three-branch, 18-interior-edge all-sector spine, deactivates the J51 extra stable support `9001`, removes forcing/all-positive edges `(7002,9001)` and `(2475,9001)`, removes cap `(2475,8000,9000)`, and removes saddles `(2475,9000)` and `(9001,9002)`. It preserves intended stable face `2475` and intended unstable vertex `(2475,5000,5003)`.

The requested anti-carrier sign condition fails at exactly one new exposed true edge: `(10000,10001)`. Every other inserted true edge and every inherited true edge whose star changes has at least one exact nonpositive external arrow. The unique all-positive edge forces a stable endpoint disjoint from independently stable row `2475`, proving `S>=2`; the full audit attains equality. The canonical exact ingress also fails death-before-birth: at `t=1/100`, the replacement unstable cap is already strict while old stable `9001`, both old saddles, and old forcing edge `(7002,9001)` are still strict.

The exact M42 `(2,1,1)` body therefore remains the stronger run-wide equilibrium-count benchmark.

## Exact finite source

The supplied labels are

`[2475, 0, 5000, 5003, 7001, 7002, 7003, 8000, 8001, 8002, 9000, 9001, 9002, 10000, 10001]`.

The active labels are

`[2475, 5000, 5003, 7003, 8000, 9002, 10000, 10001]`,

and inactive labels are

`[0, 7001, 7002, 8001, 8002, 9000, 9001]`.

The active raw supports are:

```text
2475 = (131619609/16777216, 367860745/16777216, 1805573/8388608)
5000 = (5159793/16777216, -9737161/16777216, -157333/16777216)
5003 = (-8590229/8388608, -9021087/4194304, -135919/16777216)
7003 = (-24904838233173362557520415/7082114414474861452722176, -55507469930496435319185063/7082114414474861452722176, -268103108610632462521365/3541057207237430726361088)
8000 = (-553323556521426629121301/442632150904678840795136, -9347761995539414071318985/1770528603618715363180544, -230602944165809381500335/3541057207237430726361088)
9002 = (-1541886005582361117568161/1770528603618715363180544, -4130808441302558056043539/885264301809357681590272, -202292641524826734050083/3541057207237430726361088)
10000 = (-26967380774760057740360813/7082114414474861452722176, -75576740433737489538962541/7082114414474861452722176, -345467609470213338608029/3541057207237430726361088)
10001 = (-9780437937723182149706387/3541057207237430726361088, -33773730745442692098507319/3541057207237430726361088, -87528265901513332182351/885264301809357681590272)
```

All other inherited J51 supports are supplied as their exact J51 raw coordinates divided by `2^18`. The two new supports `10000,10001` are the last two rows above. The active seed is a `2^-20` dyadic realization followed by the exact positive-determinant rational alignment

`det(B)=18661482973319786421/54032244983481303808 ≈ 0.34537678341932598`

that maps the protected raw triangle `(2475,5000,5003)` to its exact J51 raw triangle.

The exact projective ordinary-centering gauge is

`q_i -> q_i/(1-q_i·c)`, `c=M_raw/V_raw`.

Its moment equation is globally affine:

`M(u)=M_raw−V_raw u`, `D_uM=−V_raw I_3`.

The unique root is approximately

`c=(-3.8371311720913941e-06, 1.096731594709886e-05, -0.00097929277974805745)`.

Every projective denominator is positive; the exact minimum is stored in `certificates/J52_exact_ordinary_centroid.json` and is approximately `0.99998933271107227`.

## Exact ordinary volume and moments

The exact centred volume is

```text
622479634977836738350939249449445467976324010877594172600621426874931125511180101012835194533994615395937391956618743959552087320375064890057970388889510452870090115758932330125411642529323186107973632/12142602405589673523428855700392796818657826908590588228477322504443764200898905153187509638767871420796660327319560229843822575152805600479748687385192978822009346787216401996453537384221551043904725
```

approximately `51.26410419987787`.

The independently reconstructed oriented surface identities give

`V=Σ det(v_a,v_b,v_c)/6`,

`M=Σ det(v_a,v_b,v_c)(v_a+v_b+v_c)/24=(0,0,0)`.

Thus the origin used for mechanics is the body's own uniform-volume centroid.

## Irredundant H/V/E incidence

The topology signature is

`43ddab55c4dfb50d8414f67af306c378b5796dcd6406a065ca90e768f37d27d4`.

The minimum exact all-supplied-row/nonincident-vertex gap is positive, approximately `0.17903219220783825`. The minimum inactive-row gap is approximately `0.99990148471924811`.

Actual maximal primal face cycles, in the stored exact vertex indexing, are:

```text
2475: 0,1,4,3,2
5000: 5,6,1,0
5003: 0,2,7,8,5
7003: 2,3,9,10,7
8000: 3,4,11,9
9002: 6,11,4,1
10000: 10,8,7
10001: 8,10,9,11,6,5
```

All 18 true edges, by incident maximal-face labels, are:

```text
(2475,5000)
(2475,5003)
(2475,7003)
(2475,8000)
(2475,9002)
(5000,5003)
(5000,9002)
(5000,10001)
(5003,7003)
(5003,10000)
(5003,10001)
(7003,8000)
(7003,10000)
(7003,10001)
(8000,9002)
(8000,10001)
(9002,10001)
(10000,10001)
```

The display triangulation has 12 vertices, 30 mesh edges, and 20 oriented triangles; every mesh edge has multiplicity two and `12−30+20=2`. Grouping coplanar pieces gives the true identity `12−18+8=2`. Triangulation diagonals are not classified as true edges.

## Exhaustive full-normal-cone mechanics

Every maximal face, every complete vertex normal cone, and every full four-component true-edge cone was classified exactly.

```text
stable faces:
  2475
  10000

unstable vertices:
  (2475,5000,5003)
  (2475,7003,8000)

saddle true edges:
  (2475,7003)
  (2475,9002)
```

Point margins `(minimum positive / closest excluded)` are:

```text
stable:   +0.12524141185580659 / -0.13894153580785348
unstable: +0.069236073923119909 / -0.17663961793927643
saddle:   +0.046789317452916541 / -0.024316749767511966
```

## Connected positive-volume all-sector event

The transition uses the exact J51 raw active dual hull scaled by `2^-5` as the inner boundary and the exact J52 raw active dual hull as the outer boundary. Uniform scaling is a homothety of the primal and preserves J51 mechanics.

The exact terminal complex has:

```text
vertices:          19
edges:             75
triangular faces:  101
tetrahedra:        43
internal faces:    71
boundary faces:    30
interior edges:    30
boundary spheres:  2
Euler characteristic: 2
```

Every tetrahedron has exact positive orientation. Every internal triangular face has multiplicity two; the multiplicity-one faces are exactly the complete J51 and J52 boundary spheres. The tetrahedron-adjacency graph is connected.

Exact support-space shell volume:

`190875622884575223055206011617808667359625/1020640250816774544046769543584515434217472 ≈ 0.18701557451984249`.

Minimum exact tetrahedron volume:

`53357442316312099341/77371252455336267181195264 ≈ 6.8962877842921693e-07`.

A certified 14-tetrahedron connected spine has 18 interior edges and branch tetrahedra `[2, 8, 14]`. It intersects all seven named sectors: the old forcing edge, the `(2475,9001)` break sector, the old cap, both old saddle stars, and both new supports. This is a shared-interior-network equivalent stronger than a two-interior-edge four-arm cell; it is not an uncoupled shell.

## Exact old/new genealogy

At J52:

- row/stable face `9001` is inactive/absent;
- edges `(7002,9001)` and `(2475,9001)` are absent;
- cap `(2475,8000,9000)` is absent;
- saddles `(2475,9000)` and `(9001,9002)` are absent;
- intended stable face `2475` remains strict;
- intended unstable vertex `(2475,5000,5003)` remains strict.

The complete new packet is:

```text
extra stable:   10000
extra unstable: (2475,7003,8000)
saddles:        (2475,7003), (2475,9002)
forcing carrier:(10000,10001)
```

## Complete anti-carrier arrow audit

For an oriented endpoint `i` and an external neighbour `k`, the exact face-stability arrow primitive is

`A(i,k)=||q_i||^2−q_k·q_i`.

For inserted true edges:

```text
(5000,10001): min arrow -13.700715939469349; has nonpositive arrow
(5003,10000): min arrow -17.6682406427256; has nonpositive arrow
(5003,10001): min arrow -21.177321136294204; has nonpositive arrow
(7003,10000): min arrow -10.67289755729505; has nonpositive arrow
(7003,10001): min arrow -23.235483319541054; has nonpositive arrow
(8000,10001): min arrow -16.339540782932154; has nonpositive arrow
(9002,10001): min arrow -13.700715939469349; has nonpositive arrow
(10000,10001): min arrow 14.133046684355719; ALL POSITIVE
```

All seven inherited endpoint edges whose incident stars differ from J51 also have at least one exact nonpositive external arrow. Shell-interior tetrahedral edges that are not exposed endpoint true edges are not mechanical equilibrium carriers.

Exactly one exposed edge remains all-positive:

`(10000,10001)`, minimum external primitive `14.133046684355719`.

If neither endpoint were stable, their two mutual failures would sum to `||q_10000−q_10001||^2<=0`, contradicting the exact positive square in `J52_residual_forcing_obstruction.json`. Therefore one endpoint is stable. Since row `2475` is independently strict stable and is disjoint from this edge, `S>=2`. The exact audit gives stable rows `2475,10000`.

## Exact chronology obstruction

The canonical ingress is

`Q_raw(t)=(1−t)Q_J51+tQ_J52`,

with the two new rows contracted by `2^-18` at `t=0` and exact projective ordinary-centering at every rational `t`.

At `t=1/100`, exact reconstruction gives class `(2, 2, 2)` and:

```text
new cap (2475,7003,8000): strict, margin 0.16047214648185071
old stable 9001:           strict, margin 0.26129743838715014
old saddle (2475,9000):   strict, margin 0.040840362361393878
old saddle (9001,9002):   strict, margin 0.049441590345060203
old forcing (7002,9001):  still a true edge
minimum nonincidence:     0.00040691559184145463
```

Thus a replacement unstable feature becomes strict before the inherited stable/forcing/saddle packet is dead. This exactly rejects death-before-birth for the realized canonical ingress. It is not a theorem excluding every other path through the same endpoint topology.

## Two independent controls after moment elimination

Control `a` moves raw support `10000` in `+x`; control `b` moves raw support `10001` in `+z`. The response walls are the forcing-sector circuit `(5003,7003,10000,10001)` and the cap-sector circuit `(2475,7003,8000,10001)`.

The exact response Jacobian has decimal form

```text
[[-0.01676412723572055, 5.407159955928514]]
[[0.0, 38.396215360012846]]
```

and exact nonzero determinant

`-4543651787201673350706859429951236795113685348539255449763644925/7058877961233122054288558705539687400756315808162127203037872128 ≈ -0.64367903966538309`.

For every small `(a,b)`, the three moment variables are eliminated uniquely by `M(u)=M_raw(a,b)−V_raw(a,b)u=0`. Positive-denominator projective centering preserves the circuit zero loci, so the post-moment timing rank remains two.

## Positive perturbation chamber

Under the inverse-dual family

`p -> diag(x,y,1)p`, `q -> q diag(1/x,1/y,1)`,

with `|x−1|,|y−1|<=2^-20`, incidence and exact centroid zero are preserved algebraically. Exact rational polynomial interval replay proves the entire box remains `(2,2,2)`.

Certified interval `(positive lower / excluded upper)` margins:

```text
stable:   +0.12524093407522915 / -0.13894100575516286
unstable: +0.06923607377060946 / -0.17663961753947555
saddle:   +0.04678922819213862 / -0.024316703288898105
```

## Discovery and falsification

The exact endpoint was selected after full-hull searches that rebuilt the ordinary centroid, maximal faces, true edges, and complete mechanics at every accepted state. A separate 300,000-trial four/five-support search produced 69,144 valid states: 61,069 `(2,2,2)`, 7,632 `(3,2,3)`, 406 `(4,2,4)`, 22 `(2,3,3)`, 13 `(5,2,5)`, one `(3,3,4)`, and one `(6,2,6)`; it found no `(2,1,1)` or `(1,1,0)` state. Earlier targeted two/three-support and fixed-topology searches likewise found no winner. These searches are empirical evidence only; the exact nonwinner conclusion comes from the all-positive carrier theorem.

## First genuinely unclassified successor

The next nonrepeating topology must be a **carrier-free shared-interior-face five-arm terminal cell**, or a nonedge-coupled antiprismatic cage of equivalent strength. Within this branch it should use at least three connected extreme supports plus simultaneous motion/deactivation of `10000,10001` and one neighbour of protected row `2475`.

One actual incidence event must:

1. preserve stable face `2475`;
2. preserve unstable vertex `(2475,5000,5003)`;
3. delete edge `(10000,10001)` before either endpoint can be forced stable;
4. destroy stable `10000`;
5. destroy cap `(2475,7003,8000)`;
6. destroy saddles `(2475,7003)` and `(2475,9002)`;
7. certify a nonpositive external arrow on every nonprotected exposed carrier before activation;
8. exhibit a strict death-before-birth chamber;
9. retain at least two independent timing controls after the three moment equations.

Excluded repetitions are another two-support exposed-edge relay, a single stellar page/local clip, supporting-face concurrence, an uncoupled nested shell, and motion inside the certified inverse-dual box. This is a branch-local frontier, not a global nonexistence theorem.

## Independent verification

From the archive root run:

```bash
bash [internal-source-reference].sh
```

The standard-library exact verifier reconstructs the source, exact ordinary centroid, complete H/V/E lattice, every full normal cone, all external arrows, the forcing theorem, the 43-tetrahedron shell and 14-tetrahedron spine, all exact chronology samples, rank-two controls, and both meshes. The independent exact polynomial perturbation replay is byte-identical to the stored full certificate.

Expected markers:

```text
NIMBLE_COMET79_J52_A4_ALL_INDEPENDENT_CHECKS_PASS
J52_SHAPE_BOX_BYTE_IDENTICAL_PASS
NIMBLE_COMET79_J52_PACKAGE_ALL_CHECKS_PASS
```

`J52_A4_terminal8` is **USED as an exact all-sector topology-changing nonwinner**, but it does not supersede the exact M42 `(2,1,1)` benchmark.
