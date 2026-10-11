# figure-0212

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Calm Raven 06 — exact post-CU10 linked double-cap determination

## Complete artifact and replay receipt

- [Exact replay bundle](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER.zip)
- [Archive SHA-256 file](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER.zip.sha256)
- [Human-readable report](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER/RESULT.md)
- [Embedded exact master certificate](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER/doublecap13_master_certificate.json)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER/endpoint/endpoint_centered.obj) and [STL](sandbox:/mnt/data/Calm_Raven_06_doublecap13_exact_NONWINNER/endpoint/endpoint_centered.stl)

Archive SHA-256: `18007b481c4be60182374a7ad162d0ff6d74898bdb5fbb199a4254d620e121dd`.

A pristine extraction passed all 95 immutable manifest entries. Its replay ended with both `INDEPENDENT_EXACT_DOUBLECAP13_PASS` and `ALL_EXACT_DOUBLECAP13_VERIFIERS_PASS`.

## Literal outcome

**EXACT NONWINNER.** I reconstructed the accepted eleven-plane endpoint, traversed its first genuinely unclassified non-stellar terminal-volume topology, and materialized two linked exact supporting planes. The resulting summand has `D:(V,E,F)=(22, 33, 13)`; the ordinary-own-centred common Minkowski refinement has `(V,E,F)=(101, 188, 89)` and exhaustive strict class `(S,U,H)=(2, 2, 2)`. It is therefore not the requested homogeneous polyhedral Gömböc.

The acceptance gate remains a finite uniform-density object evaluated at its own exact volume centroid, with strict `(1,1,0)`, complete actual H/V/E incidence, exhaustive positive-margin mechanics, independent verification and matching meshes; auxiliary-centre, wall, smooth, near, or unexpanded objects do not qualify. :contentReference[oaicite:0]{index=0}

## Reusable artifact

The complete bundle contains exact rational input rows, all summand vertices/edges/facets, every common-refinement vertex/maximal face/true edge, exact mixed-volume and mixed-first-moment systems, interval boxes, a clean-room verifier, and OBJ/STL. Run `./RUN_ALL_VERIFIERS.sh` after extraction.

## 1. Exact construction and what changed

The parent four-feature block was extra stable `D368`, extra unstable `D019`, C saddle `D(4,10)/D(4,8)`, and return saddle `D(0,9)/D(3,9)`, with intended lineages `D045` and `D048` protected.

Row 11 deletes `D019`, replacing the extra-U carrier by `D(1,9,11)` and the return saddle by `D(6,11)/D(9,11)`. Row 12 deletes `D368`, replacing the extra stable carrier by `D(3,6,12)` and the C saddle by `D(4,12)/D(4,8)`. Rows 11 and 12 share the genuine true edge `D61112--D91112`. Thus every inherited mechanical identity is absent from the final exact ledger, but the Euler-neutral block is relayed rather than cancelled.

## 2. Irredundant exact plane system

```text
0 D0: (-13153/32768, -27937/65536, -53127/65536; h=1516059357/2147483648)
1 D1: (-1361/65536, -10805/32768, 61855/65536; h=-61753030599584781385807608441346358116846527699/310810949179262687143965090288773323565704413184)
2 D2: (9313/16384, 4455/8192, 10115/16384; h=-352797091482846540514804485565826624474423927/19425684323703917946497818143048332722856525824)
3 D3: (10039/16384, -4513/8192, -18567/32768; h=3702610017626632720309376484242546264871389323/2428210540462989743312227267881041590357065728)
4 D4: (26213/65536, 13729/16384, 24333/65536; h=-96737211/1073741824)
5 D5: (-19289/65536, 7561/32768, 15195/16384; h=-242832957/268435456)
6 D6: (56045/65536, -16661/32768, -6603/65536; h=90301/65536)
7 bridge7: (-12225/65536, -2399/32768, 64207/65536; h=-2295307548643407433816811540070135540036341203095945005507575/3916822130433258859832783870198263388589283412013047353442304)
8 bridge8: (16291/16384, -5945/65536, 3645/65536; h=214505787219754136715603574458414145391198136777824126622566059565244263873/237881794492947352987653140187185697870657453663791039663324963028160479232)
9 bridge9_U_return: (-3666715/8388608, -1/1, -6432769/16777216; h=18253823/16777216)
10 bridge10_C_link: (1/1, -1315675/16777216, 6723747/8388608; h=3495493/8388608)
11 doublecap11_U_return: (-6700819/16777216, -4329037/8388608, -12712661/16777216; h=3237293/4194304)
12 doublecap12_C_stable: (3663287/4194304, -162535/2097152, 8066567/16777216; h=8500857/16777216)
```

Every row is active and supports a nondegenerate facet. The exact D vertices, each obtained as the unique intersection of its active rows, have active sets

```text
038; 0311; 045; 048; 057; 0711; 1710; 1711; 1911; 1912; 11012; 245; 2410; 2510; 3611; 3612; 3812; 4812; 41012; 5710; 61112; 91112
```

Their full rational coordinates are verbatim in `endpoint/D_V.csv` and embedded in `doublecap13_master_certificate.json`. The 33 true edges are

```text
038--0311[0,3]; 038--048[0,8]; 038--3812[3,8]; 0311--0711[0,11]; 0311--3611[3,11]; 045--048[0,4]; 045--057[0,5]; 045--245[4,5]; 048--4812[4,8]; 057--0711[0,7]; 057--5710[5,7]; 0711--1711[7,11]; 1710--1711[1,7]; 1710--11012[1,10]; 1710--5710[7,10]; 1711--1911[1,11]; 1911--1912[1,9]; 1911--91112[9,11]; 1912--11012[1,12]; 1912--91112[9,12]; 11012--41012[10,12]; 245--2410[2,4]; 245--2510[2,5]; 2410--2510[2,10]; 2410--41012[4,10]; 2510--5710[5,10]; 3611--3612[3,6]; 3611--61112[6,11]; 3612--3812[3,12]; 3612--61112[6,12]; 3812--4812[8,12]; 4812--41012[4,12]; 61112--91112[11,12]
```

The thirteen exact facet cycles are

```text
row 0 D0: 3;0;1;5;4;2
row 1 D1: 8;9;10;6;7
row 2 D2: 12;11;13
row 3 D3: 1;0;16;15;14
row 4 D4: 11;12;18;17;3;2
row 5 D5: 19;13;11;2;4
row 6 D6: 14;15;20
row 7 bridge7: 6;19;4;5;7
row 8 bridge8: 3;17;16;0
row 9 bridge9_U_return: 21;9;8
row 10 bridge10_C_link: 18;12;13;19;6;10
row 11 doublecap11_U_return: 1;14;20;21;8;7;5
row 12 doublecap12_C_stable: 17;18;10;9;21;20;15;16
```

The intended vertices survive exactly: `D045=(91/16384, 11831/32768, -1089/1024)`, while `D048` is retained with its exact coordinate in the same table.

## 3. Genuine finite-thickness linked terminal volume

| cell | exact-D volume (decimal locator) | newly removed cap volume |
|---|---:|---:|
| eleven_plane_parent | 0.1636178834367554 | — |
| after_row11 | 0.16354306686408998 | 7.481657266541246e-05 |
| after_row12 | 0.16343615004164047 | 0.00010691682244952225 |

Both cuts remove strictly positive exact rational volume. Coning the row-11 and row-12 facets to the displayed exact strict interior point gives positive volumes `0.0010429326254582812` and `0.001319176057700139`. Their boundary facets share the true edge `D61112--D91112`; the corresponding coned 3-balls share a nondegenerate full triangle. `positive_volume_doublecap_certificate.json` proves this exactly, so the topology is not a boundary coincidence or coplanar page artifact.

## 4. Actual common-fan transition atlas

| cell | planes | D `(V,E,F)` | common `(V,E,F)` | class | inactive slack |
|---:|---:|---:|---:|---:|---:|
| 0 | 11 | `(18, 27, 11)` | `(80, 148, 70)` | `(2, 2, 2)` | `4.98069372657e-05` |
| 1 | 12 | `(20, 30, 12)` | `(86, 159, 75)` | `(2, 2, 2)` | `4.98069372657e-05` |
| 2 | 13 | `(22, 33, 13)` | `(101, 188, 89)` | `(2, 2, 2)` | `3.71641889986e-05` |

| transition | entering plane | common V removed/inserted | common F removed/inserted | common E removed/inserted |
|---|---:|---:|---:|---:|
| 0→1 | 11 | 19/25 | 11/16 | 29/40 |
| 1→2 | 12 | 28/43 | 12/26 | 39/68 |

Both transitions change the rebuilt actual common H/V/E refinement. The complete inserted and removed lineage sets are in `common_fan_transition_atlas.json` and are independently recomputed by the clean verifier.

## 5. Ordinary-volume moments

The exact family is

`P(t)=B+t1 C1+t2 C2+t3 C3+λD`, with `λ=10677075263/4294967296`.

The three ordinary first-moment equations have the exact positive root `(t1,t2,t3)=(1,1,1)`. The Jacobian determinant is the nonzero rational stored in `endpoint/root_certificate.json` (decimal locator `-1855354338.355378`). A rational Krawczyk proof isolates the root in `[1±2^-20]^3`. Exact tetrahedral integration gives volume `69748.99558138214` and first moment exactly `(0,0,0)`, so the uniform-volume centroid is exactly the origin.

The final common refinement is `(101,188,89)`, Euler 2, complexity 376, with minimum nonincident exact slack `230371704397873727072907875303568096752599121557560917660862247048762142641247601312185643/6198755054408607775342065733873321815624005665833108424524096632020213219810096992335203139584` (decimal `3.716418899856858e-05`).

## 6. Exhaustive own-centroid mechanics

All 89 maximal faces, 101 vertices, 188 true edges, and 752 four-component edge-cone primitives are exact and nonzero. The complete positive set is:

- stable `P9:15|Dvertex(3;6;12)`; normalized margin `0.0010922823467706404`.
- stable `P9:27|Dvertex(0;4;5)`; normalized margin `0.031850280482200705`.
- unstable `P9[9;100;103]|D[1;9;11]`; normalized margin `0.005190681961399554`.
- unstable `P9[15;26;27]|D[0;4;8]`; normalized margin `0.20086706085774128`.
- saddle `P9edge(13;26)|Dedge(4;12) || P9edge(13;26)|Dedge(4;8)`; normalized margin `0.11785696983630539`.
- saddle `P9edge(15;27)|Dedge(11;12) || P9edge(15;27)|Dedge(9;11)`; normalized margin `0.07955310667571168`.

Every other feature has at least one strict negative exclusion component. The relayed extra unstable vertex `P9[9;100;103]|D[1;9;11]` has five incident true edges, and all five exact supports `-x·(y-x)` are positive; the minimum is `0.16010940283511504`. The intended `P9[15;26;27]|D[0;4;8]` is a distinct strict unstable vertex. Therefore `U>=2` throughout the certified fixed-incidence/external-positive cell.

## 7. Open boxes and shape freedom after centring

The six independent physical coordinates are `(dnx,dny,dh)` for row 11 and row 12, with both `dnz=0` and rows 0–10 fixed.

- Shape-only radius: `2^-40`; fixed actual D/common fan and own-centroid `(2,2,2)`.
- Shape × dependent-control box: shape radius `2^-42`, `C1,C2,C3` radius `2^-38`; fixed fan and class.
- Uniform parametric moment theorem: shape radius `2^-68`, dependent-control radius `2^-36`. For every shape in the six-dimensional box, exactly one positive `(t1,t2,t3)` solves the moments.

Thus `C1,C2,C3` remain dependent full-rank moment controls and six independent shape dimensions survive centring.

## 8. Scoped obstruction and attempted falsification

The exact obstruction is deliberately local but watertight: the complete D(1,9,11) true-edge star remains strictly unstable on the certified open shape/control box, independently of the protected D(0,4,8) unstable carrier. Fixed-star coordinate deformation of this endpoint therefore cannot reach `U=1`.

The broader locator search is not promoted as proof. One reproducible random batch rebuilt 272 linked two-plane samples and found no winner; a follow-up over 177 compatible third-plane masks rebuilt 1,062 representatives, with classes only `(2,2,2)`, `(2,3,3)`, `(3,2,3)`, `(3,3,4)`, `(2,4,4)`, `(3,4,5)`, and `(3,5,6)`. Exact counts and the explicit non-exclusion warning are in `search_provenance/empirical_search_scope.json`.

## 9. Independent replay and mesh

`verify_doublecap13_cleanroom.py` imports neither `exact_core.py`, `shared_build_lib.py`, the generator, nor search state. It reconstructs every summand row/vertex, exhausts all D row triples, rebuilds every common maximal face and true edge, recomputes exact moments and all mechanics, recompiles fresh GMP/directed interval binaries, verifies the terminal-volume certificates and boxes, and matches the final mesh.

The mesh has `101` vertices, `198` outward triangles and `297` triangulated edges; every mesh edge has incidence two and Euler 2. Files: `endpoint/endpoint_centered.obj` and `.stl`.

## 10. Exact scope and next genuinely new topology

This work closes only the displayed linked-double-cap incidence/sign cell and its certified boxes. It does not exclude all thirteen-plane summands or all double-octahedral realizations.

A nonrepeating successor must not append another serial page. The smallest evidence-supported topology is a cross-linked two-cell terminal volume with at least two additional supports—nominally a 15-plane summand—that deactivates the entire `D(1,9,11)` common-vertex star and `D(3,6,12)` in the same nonsimple three-dimensional event, while deleting both saddle cones `D(4,12)/D(4,8)` and `D(11,12)/D(9,11)` before replacement birth. It must preserve `D045/D048`, keep the three moments dependent, and retain at least three independent post-centering shape coordinates.

## Immutable evidence ledger

- `MANIFEST.sha256`: `fd0c4e1c2ddf37cf3515eaa479ccef3ad92a000538fbe3188e2155e8745aebaf`
- `doublecap13_master_certificate.json`: `d9fbf7e4de72c5d752e4cc2c52c2954c803e133d7b7d7a5fdac3bd9b14f64fdb`
- `endpoint/exact_certificate.json`: `0376c03475e483df912772ca87eb5f92304a004c6e7f8ad020652f7fc54c3c34`
- `endpoint/root_certificate.json`: `e23897e04f45a0de8067b27db23ea9670bbe6cd998376bebb7872f8c071f0f2c`
- `common_fan_transition_atlas.json`: `b3958764415f71f9f335403d09c121e7f3ffdbb9cc30eb345eee21cf44dee137`
- `positive_volume_doublecap_certificate.json`: `3b11c553c188972c92e6116a169466f201d716215706db1df0c5b58c0eae9b4b`
- `doublecap_terminal_transition_certificate.json`: `206e53b65d19ae93e8a952104fe82896b030b29470483d1d4cfe56cb770c1752`
- `extraU_relay_obstruction_certificate.json`: `8901fff2e33822378db0f4956caa6023a1f2c3ed3c62dc4ffbbe0959573913ad`
- `doublecap13_shape_box_directed.json`: `99980b400522d48561ee0597ca924f844871a3694ad08e81c5890f4777e4a6ef`
- `doublecap13_shape_control_mechanics_box.json`: `f80c5a0657828d79f2d7f18ad03dc276eb6ef3128c07488e957c1b8360c3e0c4`
- `doublecap13_shape_moment_implicit_box.json`: `2f934c3b412fd0e1ee34e139a865e965183cae91503b7ddd6d4baa244b94bf00`
- `verify_doublecap13_cleanroom.py`: `4a1d68812e68e01f83e79647c2d250feb2db54d1e7aecfe5c665c6b72d1754f3`
- `endpoint/endpoint_centered.obj`: `2a05c8e464e68bfc96b3b5963d7d6b7c6d782a6f5c11bbccb04c066c1461dcbc`
- `endpoint/endpoint_centered.stl`: `def12d0c3461d459dc560bc343b035b9f517de874ecf0747464650b9c5b155d6`
