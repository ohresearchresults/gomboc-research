# figure-0208

AI research report · 2026-09-02 UTC

---

# Calm Raven 06 — exact post-CU10 eleven-plane bridge-cell determination

## Complete reusable artifact

[Download the exact bridgecell11 replay bundle](sandbox:/mnt/data/Calm_Raven_06_bridgecell11_exact_NONWINNER.zip). Archive SHA-256: `6e7c756808bf1caad525ecc39909e5f3228d6c85e9a849492158a858d440696b`. The companion hash file is [here](sandbox:/mnt/data/Calm_Raven_06_bridgecell11_exact_NONWINNER.zip.sha256).

A clean extraction was replayed with `./RUN_ALL_VERIFIERS.sh`; it checked all 92 immutable manifest entries, independently reconstructed the geometry and mechanics, and ended with `ALL_EXACT_BRIDGECELL11_VERIFIERS_PASS` and `INDEPENDENT_EXACT_BRIDGECELL11_PASS`.

The inherited acceptance gate remains a finite uniform-density H/V object at its own exact ordinary-volume centroid, strict `(S,U,H)=(1,1,0)`, with exhaustive true-feature audit, independent verification and matching OBJ/STL; auxiliary-centre or wall-point mechanics do not qualify. :contentReference[oaicite:0]{index=0}

## Work actually attempted

I reconstructed the accepted two-page/ninth-plane endpoint, searched the exact covector arrangement for a one-plane third page, enumerated every compatible strict sign mask, and derived affine-circuit contradictions rather than relying on a failed optimizer. After the exact tenth-plane obstruction emerged, I escalated immediately to two adjacent added planes. Several numerical and exact cell searches were used only to locate candidate page normals; each promoted state was then replaced by exact rational data and rebuilt from scratch. I rejected candidates that made an old row redundant without increasing facet count, candidates that birthed an additional U–H pair, and candidates whose labelled packet changed without a corresponding actual H/V/E fan change. The promoted endpoint is the strongest exact open cell found, not a global optimum or a continuum exclusion.

## Literal disposition

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The direct one-plane tenth-facet packet-contact topology is exactly insufficient; after escalation, a literal irredundant eleven-plane summand and a finite-thickness adjacent two-cell / three-page higher-valence complex were materialized. The final Minkowski sum is exactly ordinary-own-centred and strictly `(S,U,H)=(2,2,2)`.

The parent accepted endpoint had `D:(V,E,F)=(13,20,9)`, common refinement `(65,121,58)`, and residual packet `D368, D0136, D24/D48, D01/D36`. This construction clips `D0136`, changes the return carrier, and links the C sector through a second adjacent page while preserving the intended `D045` and `D048` lineages.

## 1. Exact tenth-plane insufficiency

The direct packet-contact contract requires one strict new plane to remove `D0136` and `D248`, preserve `D017,D045,D048,D245`, and change old edge carriers `D01,D36,D24,D48`. All 128 compatible sign masks were enumerated on the exact parent vertex configuration. Exactly 126 are impossible by explicit rational affine-circuit sign contradictions. The only two realizable covectors remove `D368` and make row 6 redundant; their final active facet counts are nine and eight, and both corresponding common sums remain strict `(2,2,2)`. Thus no genuine irredundant tenth-facet page realizes this direct simultaneous coupling. This is an exact scoped obstruction, not a global exclusion of every imaginable ten-plane geometry.

Certificate: `tenth_plane_insufficiency_certificate.json`.

## 2. Exact eleven-plane summand

The irredundant supporting system is:

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
```

Its exact f-vector is `(V,E,F)=(18,27,11)`. Every row supports a nondegenerate facet. The exact vertex coordinate table is fully expanded in `endpoint/D_V.csv` and embedded verbatim in `bridgecell11_master_certificate.json`; each entry is independently reconstructible as the unique solution of its listed active rows. The active sets are:

```text
017; 019; 038; 039; 045; 048; 057; 1710; 1910; 245; 2410; 2510; 368; 369; 4810; 5710; 6810; 6910
```

The 27 exact true edges, written as `vertex0-vertex1[incident rows]`, are:

```text
0-1[0,1]; 0-6[0,7]; 0-7[1,7]; 1-3[0,9]; 1-8[1,9]; 2-3[0,3]; 2-5[0,8]; 2-12[3,8]; 3-13[3,9]; 4-5[0,4]; 4-6[0,5]; 4-9[4,5]; 5-14[4,8]; 6-15[5,7]; 7-8[1,10]; 7-15[7,10]; 8-17[9,10]; 9-10[2,4]; 9-11[2,5]; 10-11[2,10]; 10-14[4,10]; 11-15[5,10]; 12-13[3,6]; 12-16[6,8]; 13-17[6,9]; 14-16[8,10]; 16-17[6,10]
```

The exact oriented facet cycles are:

- row 0 `D0`: `5;2;3;1;0;6;4`
- row 1 `D1`: `8;7;0;1`
- row 2 `D2`: `10;9;11`
- row 3 `D3`: `2;12;13;3`
- row 4 `D4`: `9;10;14;5;4`
- row 5 `D5`: `15;11;9;4;6`
- row 6 `D6`: `12;16;17;13`
- row 7 `bridge7`: `7;15;6;0`
- row 8 `bridge8`: `5;14;16;12;2`
- row 9 `bridge9_U_return`: `3;13;17;8;1`
- row 10 `bridge10_C_link`: `14;10;11;15;7;8;17;16`

The newly added page 9 is the pentagon `039–369–6910–1910–019`. Page 10 is the octagon `4810–2410–2510–5710–1710–1910–6910–6810`. Page 10 shares true edges `1710–5710`, `4810–6810`, and `1910–6910` with pages 7, 8, and 9 respectively.

## 3. Positive-volume shared cells

The nested exact D volumes decrease strictly from the nine-plane parent to the row-9 and row-10 cuts:

- nine planes: `0.1665021453245461`;
- after row 9: `0.16648042059383192`, removed cap `2.1724730714186889e-05`;
- after row 10: `0.1636178834367554`, removed cap `0.0028625371570765107`.

Coning rows 7, 8, 9, and 10 from the exact strict interior point gives positive volumes `0.0015421849660674943`, `0.013656200629491015`, `0.0002831301716789937`, and `0.0036264503841195702`. The row-10 cone shares a full nondegenerate triangular face with each of the other three. The union is therefore a connected finite-thickness 3-ball complex, not a boundary coincidence.

## 4. Rebuilt actual common-fan atlas

| cell | active D planes | D `(V,E,F)` | common `(V,E,F)` | own-centroid class | minimum inactive slack |
|---:|---:|---:|---:|---:|---:|
| 0 | 9 | `[13, 20, 9]` | `[65, 121, 58]` | `(2, 2, 2)` | `0.000304990218115` |
| 1 | 10 | `[16, 24, 10]` | `[75, 139, 66]` | `(2, 2, 2)` | `0.000304990218115` |
| 2 | 11 | `[18, 27, 11]` | `[80, 148, 70]` | `(2, 2, 2)` | `4.98069372657e-05` |

Both transitions have explicit nonempty H/V/E symmetric differences in `common_fan_transition_atlas.json`; no fixed-fan coordinate polish is being reported. Plane 9 changes `D0136→D019` and `D01/D36→D09/D39`. Plane 10 replaces the `D248` sector by `D2410,D2510,D4810` and changes the C saddle to `D4,10/D4,8`.

## 5. Exact moments and common polyhedron

The promoted sum is

`P = B + t1 C1 + t2 C2 + t3 C3 + λD`, with exact `λ=10677075263/4294967296`.

The exact positive ordinary-moment root is `(t1,t2,t3)=(1,1,1)`, isolated in the rational box `[1±2^-20]^3`. The exact Jacobian determinant is nonzero (decimal locator `-1856890100.800446`). Exact tetrahedral integration gives volume `69779.616147652254` and first moment `(0,0,0)`, so the uniform-volume centroid is exactly the origin.

The actual centred common refinement has `(V,E,F)=(80,148,70)`, Euler 2 and complexity 296. Its complete exact H/V/E data are in `endpoint/common_H_affine.csv`, `endpoint/common_V_affine.csv`, `endpoint/common_edges.csv`, `endpoint/final_centered_H.csv`, and `endpoint/final_centered_V.csv`. Minimum exact nonincident slack is positive; decimal locator `4.9806937265745393e-05`.

## 6. Exhaustive own-centroid mechanics

All 70 maximal faces, 80 vertices, 148 true edges, and 592 full edge-cone components are exactly nonzero. The only equilibria are:

- stable `P9:15|Dvertex(3;6;8)`; normalized margin `0.0013990179685297668`.
- stable `P9:27|Dvertex(0;4;5)`; normalized margin `0.031851771459333794`.
- unstable `P9[9;100;103]|D[0;1;9]`; normalized margin `0.0062702092127574927`.
- unstable `P9[15;26;27]|D[0;4;8]`; normalized margin `0.20086231293891144`.
- saddle `P9edge(13;26)|Dedge(4;10) || P9edge(13;26)|Dedge(4;8)`; normalized margin `0.11505897154191393`.
- saddle `P9edge(15;27)|Dedge(0;9) || P9edge(15;27)|Dedge(3;9)`; normalized margin `0.20722346584737408`.

Thus the exact class is `(2,2,2)`, not `(1,1,0)`.

The extra unstable common vertex is `P9[9;100;103]|D[0;1;9]`. All five of its directed true-edge supports are exact and positive, with minimum `0.39625612645499519`. The intended `P9[15;26;27]|D[0;4;8]` vertex is distinct and also strict unstable. Therefore `U≥2` throughout the certified fixed-incidence/external-positive cell. A successful successor must change this star, not polish coordinates inside it.

## 7. Independent bridge controls after centring

The independent coordinates are

`bridge9_dnx, bridge9_dny, bridge9_dh, bridge10_dnx, bridge10_dny, bridge10_dh`,

with `dnz=0` for both new planes and rows 0–8 fixed. `C1,C2,C3` are retained solely as dependent rank-three ordinary-moment controls.

- A six-dimensional shape-only box of radius `2^-32` preserves D `(18,27,11)`, common `(80,148,70)`, `D045/D048`, and class `(2,2,2)` at each member's own interval centroid.
- A full shape×control product box with both radii `2^-34` preserves the same actual common fan and class.
- A 120-digit directed parametric Krawczyk proof gives shape radius `2^-66` and dependent-control radius `2^-36`: for every six-coordinate shape in the box, there is exactly one positive `t` in `[1±2^-36]^3` solving all three ordinary first moments. Hence six independent physical shape dimensions remain after centring, exceeding the requested minimum of three.

## 8. Independent replay and watertight mesh

`verify_bridgecell11_cleanroom.py` imports neither generator geometry module. It reconstructs all three D/common cells from rational CSVs, recompiles the GMP mixed-moment and directed-interval engines, rechecks the 128-mask tenth-plane census, all exact moments and full normal cones, positive-volume cell complex, open boxes, local U obstruction, and OBJ/STL correspondence. Terminal marker: `INDEPENDENT_EXACT_BRIDGECELL11_PASS`.

The actual final mesh has 80 vertices, 156 outward-oriented triangles and 234 mesh edges; every mesh edge has incidence two and `80-234+156=2`. Files: `endpoint/endpoint_centered.obj` and `.stl`.

## Immutable evidence ledger

- master certificate: `bridgecell11_master_certificate.json`, SHA-256 `65e0827c066098c1498450a5decceafbf7d9cbe558d56b5f7bcbd38c8b4c0b86`;
- exact endpoint certificate: `47ee917326ce640001a7a71fc38027cee91bff54d04d441196b11a36ef446ca6`;
- exact root certificate: `16e8bd7fa04210814ffb3234a964ca9cba4a0e03f9582dddac485ca4455f434d`;
- D H/V/E/F tables: `714c2d27…`, `7025c5c3…`, `c4ea0e06…`, `9822b58c…` respectively;
- tenth-plane certificate: `536fad1400a6c4e068daad263f3491076577553b22f601c043b259ac5f300bc1`;
- actual common-fan atlas: `7ab9f8d7b71afaa2c5847afb19dad98eb7a37171a8c75d795bca909639ec344b`;
- positive-volume cell certificate: `d1f0a78cee02689a25d015a3aa8b95f5d457782a46dce884355f024aabf1c16b`;
- forced-extra-U certificate: `f2a50b3bc97be7310a765c9d740c313562a7247cf4233b30d044d48e4caa05bc`;
- shape-only / shape×control / implicit-root boxes: `6ebdbbe2…`, `129a5dd9…`, `bd80692e…`;
- independent verifier: `81b2f177ce87e81f4865be0ca1abdc949110457acd4a43dc02950e2cf2ec8882`;
- OBJ/STL: `75d3e3f358d37577b1677abc85492c088c0f8ceda423fd0b146809c61e6bd09e` / `4f156b8d42422a6b5d4cc58c9f66dbe48f8fc15ba6b7e2570787a01e76187565`;
- complete immutable manifest: `09ea593116b8f9a4744e9daaa38770b2c27cba87af640d73763f5ece2335906d`.

## 9. Scope and first unclassified successor

The eleven-plane cell is the first exact realizable successor under the direct packet-contact escalation, but it relays rather than cancels the Euler-neutral block: extra stable `D368`, extra unstable `D019`, C saddle `D4,10/D4,8`, and return saddle `D09/D39` remain.

The first unclassified operation is not a serial fourth page. It is a non-stellar double-cap/double-octahedral terminal volume—minimally a twelfth plane or two linked new supports—that deactivates `D019` or changes its entire true-edge star while simultaneously removing `D368` and crossing both saddle carriers before replacement birth. It must preserve `D045/D048`, solve all three moments through dependent controls, and retain at least three independent shape coordinates.
