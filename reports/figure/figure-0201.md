# figure-0201

AI research report · 2026-09-02 UTC

---

# Nimble Comet 79 — exact J45 higher-valence terminal determination

## Disposition

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The strongest realized continuation is the rational, uniform-density, ordinary-own-centred polyhedron `J47_D12_terminal_post8`, with irredundant `(H,V,E)=(8,12,18)` and exhaustive strict class `(S,U,H)=(2,2,2)`. The accepted global benchmark therefore remains the exact M42 `(2,1,1)` near-object.

This work nevertheless leaves the serial-sheet regime. It realizes the smallest convex higher-valence **boundary incidence** available in the reopened J45/J46 chart—a 12-triangle D12 base concurrence—and proves that this incidence transfers rather than cancels the full residual packet. It also isolates the first remaining nonserial successor: a genuinely communicating shared terminal **volume** carrying one S–H death and one U–H death at the same incidence event.

## Reproducible artifacts

- Exact archive: source, H/V/E tables, certificates, transition atlases, verifier, OBJ and STL (`Nimble_Comet_79_J47_D12_exact_NONWINNER.zip`)
- Archive SHA-256 receipt (`Nimble_Comet_79_J47_D12_exact_NONWINNER.zip.sha256`)
- Expanded report (`Nimble_Comet_79_J47_D12_exact_NONWINNER_RESULT.md`)
- Deterministic exact endpoint source (`J47_D12_terminal_post8_exact_source.json`)
- Exact tables: active H (`J47_H_active_exact.tsv.gz`), all supplied H (`J47_H_supplied_exact.tsv.gz`), V (`J47_V_exact.tsv.gz`), face cycles (`J47_maximal_face_cycles.tsv.gz`), true edges (`J47_true_edges.tsv`), nonincidence ledger (`J47_nonincident_per_row.tsv.gz`), full mechanics ledger (`J47_mechanical_ledgers_point.json.gz`)
- Meshes: watertight OBJ (`J47_D12_terminal_post8.obj`), watertight binary STL (`J47_D12_terminal_post8.stl`)
- Verifiers: main exact verifier (`verify_nimble_comet79.py`), parallel full-atlas verifier (`verify_full_atlas_parallel.py`)

Archive SHA-256: `90d44db112428f35ab134bfbb71b3baf1a5380f0d419396bd496f29e04cdffca`. A fresh extraction passed `sha256sum --quiet -c MANIFEST.sha256`; the main independent verifier passed with `NIMBLE_COMET79_ALL_INDEPENDENT_CHECKS_PASS`.

## Branch state and change from the journal

The input state was exact `J45_two_sheet_terminal13`, `(H,V,E)=(13,22,33)`, class `(2,2,2)`, with forcing edges `(2463,2490)` and `(2475,2481)`, followed by exact `J46_double_circuit_cell9`, `(9,14,21)`, class `(2,2,2)`. J46 genuinely removed the old forcing configuration but transferred the packet to stable rows `1160,2475`, unstable facets `(1160,2475,4137),(2453,2481,4137)`, and saddles `(0,4229),(2475,4137)`.

The reopened search found:

1. a unique abstract 8-triangle terminal disk;
2. an exact convex-closure obstruction: its nine nonapex rows must be coplanar, so the disk cannot be an isolated maximal face and all 12 nonapex triangles coalesce;
3. an exact D12 concurrence with 126 simultaneous nonapex four-row circuit zeros and no earlier oriented-matroid root on ingress;
4. an exact egress to `J47_D12_terminal_post8`;
5. a complete mechanics/topology atlas and a branch-local obstruction specifying the first true shared-volume successor.

## Exact endpoint and ordinary centroid

Supplied local row labels are `[2475,4229,2490,5001,0,2463,2467,5000,5003,5002]`. Active rows are locals `[0,1,2,3,4,7,8,9]`, i.e. labels `[2475,4229,2490,5001,0,5000,5003,5002]`; rows `2463,2467` are strictly inactive.

Exact volume:

`2152677681728190382194252898303945283662886825637974463406154602676819658187814135712502313792249623700438648395639235441732707963344975792191343843110629078901827316474689423745794790804910318251949935756250510241436315953658392565380760796381353478609025748569862275471926605202557032976530929770237257498019485991861179555873890194489007764684446112813954978163401221391935018481156396077091816403453881891160064/728559647218628561685849590858530594683302063388223517943714100368842476956401370275825193895287079697326597524708656513669742936022047665398759703258870090225273321353563515749378295453479526339520318135034294714662845467639087949562637135234105998895935787941042541662730126511680346673284465983835001711502161103969734760247405494442696014032583037369347591285933745813503695208088350171473949837904903825373315`

Decimal volume is `2.9547034205727947`. The oriented surface identities, recomputed with exact `Fraction` arithmetic, are

`V = Σ det(v_a,v_b,v_c)/6`,

`M = Σ det(v_a,v_b,v_c)(v_a+v_b+v_c)/24 = (0,0,0)`.

The dependent projective translation is `q_i(u)=q_i/(1-q_i·u)`, representing `P_raw-u`. Its exact moment equation is `M(u)=M_raw−V_raw u`; the unique root is `u=M_raw/V_raw`, numerically `(-0.92751537201432843, 0.40378800537521914, -19.261940251788094)`. The Jacobian is exactly `−V_raw I`, so the root is isolated. All projective denominators are positive; the exact minimum is stored in `certificates/J47_exact_ordinary_centroid.json` and is approximately `0.49312547449694505`.

The topology signature is `836a99b40aeb152c3784a16f3965930bf0edacdc44ab316d7ad8d91f1e3afc30`. The minimum supplied-row/nonincident-vertex separation is an exact positive rational stored in `certificates/J47_exact_incidence_irredundancy.json`, approximately `0.049289691582604038`, attained by inactive row `2467` against vertex 4 incident to `[2475,0,5000]`.

## Actual maximal faces and every true edge

Maximal primal face cycles `(H label : oriented V-cycle)`:

- `2475 : 5,4,2,3,1,0`
- `4229 : 0,1,7,6,8`
- `2490 : 6,7,10,9`
- `5001 : 11,9,10,3,2`
- `0 : 2,4,11`
- `5000 : 4,5,8,6,9,11`
- `5003 : 8,5,0`
- `5002 : 1,3,10,7`

All 18 true primal edges, given by their incident H-label pair:

`2475–4229, 2475–5001, 2475–0, 2475–5000, 2475–5003, 2475–5002, 4229–2490, 4229–5000, 4229–5003, 4229–5002, 2490–5001, 2490–5000, 2490–5002, 5001–0, 5001–5000, 5001–5002, 0–5000, 5000–5003`.

The exact surface has 20 coherently oriented triangles. Every mesh edge has multiplicity two and `V−E+F=12−30+20=2`; OBJ and STL use identical connectivity.

## Exhaustive full-normal-cone mechanics

Every actual feature was classified exactly: all 8 maximal faces, all 12 full vertex normal cones, and all 18 full true-edge cones; no triangulation diagonal was counted as a true edge.

- Stable faces: `2475`, `2490`.
- Unstable vertices/facets: `[2475,4229,5002]`, `[2475,5000,5003]`.
- Saddle true edges: `(2475,4229)`, `(2490,5001)`.

Point-margin extrema `(minimum positive; closest excluded)` are:

- stable: `(0.021745442496242863; -0.0079367779282922164)`;
- unstable: `(0.0016836581900523252; -0.0020311936259343041)`;
- saddle: `(0.30625868982617183; -0.016316888673844579)`.

Thus the strict point class is exactly `(2,2,2)`.

## Exact perturbation box and forcing theorem

For

`A=I+s0 diag(1,0,−1)+s1(E12+E21)+s2(E13+E31)+s3 diag(0,1,−1)+s4(E23+E32)`

with every `s_i∈[−2^−17,2^−17]`, use `p→Ap`, `q→qA^−1`. Incidences are preserved identically and the zero ordinary centroid remains zero. The exact interval verifier proves

- `det A ∈ [1125865547235325/1125899906842624, 281483566776321/281474976710656]`;
- Gershgorin eigenvalue lower bound `32767/32768`;
- all active/inactive decisions and all full cone signs remain strict;
- class remains `(2,2,2)` throughout.

Certified interval bounds `(positive lower; excluded upper)` are stable `(9.6482794528455962; -3.3545657277773731)`, unstable `(0.0015405240045309407; -0.0018295867337182058)`, saddle `(0.30596154240926599; -0.0046888496733278311)`.

Two row-disjoint true dual edges survive: `(2475,5001)` and `(4229,2490)`. At both endpoints of each edge every external-neighbour face-stability numerator is exactly positive. If neither endpoint were stable, adding the two mutual failures would give `−||q_a−q_b||²≥0`, contradicting `q_a≠q_b`. Each edge therefore forces one stable endpoint, and row-disjointness gives **`S≥2`** throughout the certified cell/box.

## Higher-valence D12 transition complex

The unique abstract 8-triangle disk is not physically realizable as an isolated maximal face: exact affine convexity forces all nine nonapex supplied rows into one supporting plane and all 12 nonapex triangles into the same face. The smallest realized terminal boundary event is therefore D12.

For the exact ingress family, all `C(10,4)=210` affine circuits were evaluated. No circuit root occurs in `(0,1)`. At the terminal wall, all `C(9,4)=126` nonapex quartets vanish simultaneously. The wall has outer quadrilateral `[2475,4229,2490,5001]`, apex `5002`, and common-base rows `[2475,4229,2490,5001,0,2463,2467,5000,5003]`.

- J46-side sample `t=2^−16`: `(H,V,E)=(10,16,24)`, class `(2,2,2)`.
- D12 wall `t=0`: `(5,5,8)`, class `(2,2,2)`.
- Collapsed side `t=−2^−16`: `(5,6,9)`, class `(2,2,2)`.

The exact fixed-lattice mechanics atlas contains 24 isolated paired events and 25 open cells: 14 S–H and 10 U–H events; class histogram `(2,2,2):12`, `(3,2,3):7`, `(2,3,3):5`, `(2,4,4):1`.

Physical wallward motion decreases `t`. Its first event is event 23 at `t≈0.99999871368169946`, isolated in

`[17592163415265/17592186044416, 70368653661061/70368744177664]`

with width `1/70368744177664`. It births the replacement pair `U(2490,5000,5001)` and `H(2490,5001)` before the D12 incidence.

An exact positive-determinant projective map identifies the direct and egress D12 wall representatives on the four outer rows and apex while preserving all base interiors. This is an exact orientation-preserving wall-stratum equivalence, not a claim that an unaudited straight interpolation preserves mechanics. On the complete exact egress, four supplied-row circuit roots occur, each involving inactive `2463` or `2467`; active witnesses strictly straddle every corresponding plane, so there are zero active-lattice events before J47.

At the egress wall the two residual routes already have positive margins: `S2490=10.093767976061752`, `H(2490,5001)=0.22319259203861605`, `U[2475,4229,5002]=0.029874319308210814`, `H(2475,4229)=0.43097272727450781`. Therefore the D12 incidence transports, rather than absorbs, the Euler-neutral packet.

Complete exact transition files are inside the archive: `source/J46_to_D12_direct_exact_family.json`, `certificates/D12_exact_incidence_certificate.json`, `atlas/J46_to_D12_directed_mechanics_atlas.json`, both wall audits, the projective-equivalence certificate, `source/D12_to_J47_egress_exact_family_reconstructed.json`, `atlas/D12_to_J47_incidence_roots_all_supplied.json`, and `certificates/D12_transition_complex_summary.json`.

## First remaining nonserial successor

The required count change is `(2,2,2)→(1,1,0)`, i.e. `Δ=(-1,-1,-2)`. Every isolated generic mechanics wall in the exact atlas performs one Euler-neutral S–H or U–H event. Cancellation in one incidence event therefore needs a joint wall supporting both deaths.

The first branch not excluded by the exact data is a codimension-three incidence–Morse stratum satisfying all of:

1. a D12-or-stronger shared nonsimplicial incidence;
2. simultaneous owner equalities for `S2490` and `H(2490,5001)`;
3. simultaneous owner equalities for `U[2475,4229,5002]` and `H(2475,4229)`;
4. destruction of at least one block of the forcing matching;
5. suppression, deactivation, or merger of the event-23 replacement U–H birth;
6. after reserving three exact ordinary-moment controls, at least two independent mechanical controls remain on the incidence stratum.

Generic codimension is one incidence equation plus two independent mechanical owner equations. Geometrically the successor must be a prismatic, octahedral, multi-tetrahedral, or stronger shared terminal **volume** whose interior communicates between both route stars. Another serial sheet, witness relocation, or a larger coplanar D12 face cannot satisfy the exact conditions.

This is a rigorous branch-local obstruction, not a global nonexistence theorem.

## Falsification search and verification

Heuristic searches found no winner: 4,000,000 determinant-one fixed-topology J47 metric samples; 2,000,000 five-parameter D12-wall metric samples using the full quadrilateral cone; and 90 full-shape 24-coordinate L-BFGS starts. The best valid full-shape result remained `(2,2,2)`; target-like raw counts violated volume, projective-denominator, or nonincidence validity. These searches are not used as proof.

From the extracted archive run:

`python verifier/verify_nimble_comet79.py`

and, for every atlas sample,

`python verifier/verify_full_atlas_parallel.py --jobs 5`.

The main verifier reconstructs the exact body, oriented volume and moments, irredundant H/V/E lattice, all full normal cones, five-dimensional perturbation box, forcing certificate, D12 wall, egress, and watertight meshes. The full-atlas replay evaluates all 48 event-bracket endpoints and all 25 open-cell representatives—73 exact evaluations—and ends with `NIMBLE_COMET79_FULL_ATLAS_PARALLEL_EXACT_REPLAY_PASS`.

## Final handoff

- `J47_D12_terminal_post8`: **USED exact robust nonwinner**.
- D12 concurrence: **USED exact higher-valence topology result**, but it is a supporting-face event, not yet the required communicating volume.
- Fixed-incidence metric tuning and further serial sheets: **EXCLUDED inside the certified endpoint region**.
- Continuation: construct the codimension-three shared-volume joint incidence–Morse cell above, keeping the three ordinary moments as dependent hard equations.
