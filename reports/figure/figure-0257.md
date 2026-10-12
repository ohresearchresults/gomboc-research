# figure-0257

AI research report · 2026-09-03 UTC

---

# Bright Harbor 30 — J54 five-arm shared-face exact determination

## Disposition

**USED — exact connected topology-changing NONWINNER.** `J54_FA5_sharedface8` advances the accepted `J53_CF3_octahedral6` endpoint through a genuine five-new-support, shared-interior-face, positive-volume terminal event. It is a finite rational uniform-density convex polyhedron at its own exact ordinary-volume centroid, but its strict class is `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The J53 packet is genuinely gone: rows `11000,11001,11002` are strictly inactive, so stable `11002`, unstable cap `(2475,11000,11001)`, saddles `(2475,11000),(2475,11001)`, and carrier `(11000,11002)` are absent. Protected stable `2475` and unstable `(2475,5000,5003)` remain strict. A new packet is born on stable `12003`, unstable `(2475,12000,12001)`, saddles `(2475,12000),(2475,12001)`, and carrier `(12003,12004)`. The complete row-star sink set is `{2475,12003}` and the tested exact ingress fails death-before-birth at `t=3/10`; no completion ticket is justified.

## Artifacts and replay

- Complete exact archive (`Bright_Harbor_30_J54_FA5_sharedface8_exact_NONWINNER.zip`), 1,728,458 bytes, SHA-256 `fce67b547a245bbfa883bec5916d78d820ed8ca3d2f747e340c7d6e1b1b4b910`.
- Verification receipt (`Bright_Harbor_30_J54_VERIFICATION_RECEIPT.json`), SHA-256 `4da69173e8f8e53295cab8edc68c12f3bb0e6869ffc9d7694abb99787e224589`.
- Fresh clean-extraction transcript (`Bright_Harbor_30_J54_CLEAN_VERIFICATION_TRANSCRIPT.txt`), SHA-256 `a254d16a6293d5fb45247d740e4797ea2799c0f7f31c51870edfa389e797c46a`.
- Exact source (`J54_FA5_sharedface8_exact_source.json`), SHA-256 `f378f83fec589e6054fe8b42f22b6b505a69dbfbc27d4494b4198dca08c864e6`.
- Complete row-star graph (`J54_complete_directed_row_star_graph.json`), transition shell (`J53_to_J54_FA5_connected_positive_volume_shell.json`), chronology (`J54_death_before_birth_chronology.json`), shape box (`J54_exact_two_parameter_shape_box_full.json`), and radial bound (`J54_radial_ascent_lower_bound.json`).
- Watertight OBJ (`J54_FA5_sharedface8.obj`), SHA-256 `dae8edbddda9b5c6f81a2e517bfb77fe9812110815edcedb27e90c6efe7b87a0`; watertight STL (`J54_FA5_sharedface8.stl`), SHA-256 `035cf060e72df334f0f23abaed708a9d3120ad960d71a2c5b9ba790c121ad8f2`.

A fresh unzip, pre-manifest check, complete independent replay, and post-manifest check were rerun. The terminal markers include `BRIGHT_HARBOR30_J54_ALL_INDEPENDENT_CHECKS_PASS`, all source/shell/chronology/control/shape/radial byte-identical passes, `BRIGHT_HARBOR30_J54_PACKAGE_ALL_CHECKS_PASS`, and `BRIGHT_HARBOR30_J54_CLEAN_EXTRACTION_ALL_PASS`.

## Deterministic exact H source

Parent source SHA-256 is `9e5e790ca160ba39f8d1fd84800fbc482cf2ca7a23c3f96bbf3ab5134d5185a5`. Let `A_0,A_1,A_2` be its raw rows `2475,5000,5003`:

```text
A_0=(131619609/16777216, 367860745/16777216, 1805573/8388608)
A_1=(5159793/16777216, -9737161/16777216, -157333/16777216)
A_2=(-8590229/8388608, -9021087/4194304, -135919/16777216)
```

For labels `12000,…,12004`, set `Q_i=C_i0 A_0+C_i1 A_1+C_i2 A_2` with

```text
12000: (-36170665187/549755813888, -1372039142193/1099511627776, -49033389179/137438953472)
12001: (-17257564513/274877906944, 2132518450183/1099511627776, -1001911976383/1099511627776)
12002: (-9859784667/34359738368, 654172362815/1099511627776, 189106665485/274877906944)
12003: (-1468843885649/1099511627776, 263557148185/1099511627776, -400333466843/1099511627776)
12004: (-1187321279047/1099511627776, -356581735699/549755813888, 320883031711/1099511627776)
```

Every other inherited row is contracted by `2^-24`. Apply exact projective ordinary centering `q_i -> q_i/(1-q_i·c)`, where `c=M_raw/V_raw`. `repro/build_exact_source.py` regenerates the complete source byte-for-byte.

Supplied labels are

```text
[2475,5000,5003,12000,12001,12002,12003,12004,0,7001,7002,7003,8000,8001,8002,9000,9001,9002,10000,10001,11000,11001,11002]
```

Active labels are `[2475,5000,5003,12000,12001,12002,12003,12004]`; the remaining 15 are strictly inactive. Counts are `H_supplied/H_active/H_inactive=23/8/15`, primal `(V,E,F)=(12,18,8)`, complexity `36`.

## Exact mass and incidence

Raw centering translation is approximately `(-0.22723725332485045,0.07178834808687254,1.9631642897603774)`; all exact projective denominators are positive, minimum `0.7861081570973086`. Final ordinary-volume centroid and first moments are exactly `(0,0,0)`. Exact volume is

```text
4474555420406084139564879744270319622660971590427081106090672404098508310386953364339233312908752764714914586379303079914617256905238122896874879527659816337438134597935679015994222873939865935001651521736678053469709433731940920557407585915269539406972997341436811101888675907629973455765504/124204162624277115050164316473068016236718267613299250902170763990636187573497124311616243863613388264606117132174612202409699528412032939629273782307611867702225250337934642238084357237059419931495696550291139687223949881168918173610302086099384808158110573203635584714759756558602971475025
```

(`36.02580884460213`). Topology signature is `d37b25b4b3bfa13aa701b6fb0e45118813bc4cd6260eed4ed5abbcd648eb1709`; minimum nonincidence gap is `0.0036733427981656824`, and minimum inactive gap is `0.9999998987557012`.

Maximal dual triangles / exact primal vertices:

```text
(2475,5000,5003) (2475,5000,12001) (2475,5003,12000)
(2475,12000,12001) (5000,5003,12002) (5000,12001,12002)
(5003,12000,12004) (5003,12002,12004)
(12000,12001,12003) (12000,12003,12004)
(12001,12002,12003) (12002,12003,12004)
```

Actual maximal primal face cycles:

```text
2475:0,1,3,2; 5000:4,5,1,0; 5003:0,2,6,7,4
12000:2,3,8,9,6; 12001:5,10,8,3,1; 12002:7,11,10,5,4
12003:10,11,9,8; 12004:9,11,7,6
```

Every true edge:

```text
(2475,5000) (2475,5003) (2475,12000) (2475,12001)
(5000,5003) (5000,12001) (5000,12002)
(5003,12000) (5003,12002) (5003,12004)
(12000,12001) (12000,12003) (12000,12004)
(12001,12002) (12001,12003)
(12002,12003) (12002,12004) (12003,12004)
```

## Exhaustive strict mechanics and row-star audit

All 8 maximal faces, 12 complete vertex normal cones, 18 true edges, and all 72 four-component edge-cone primitives were checked exactly.

```text
stable:   [2475,12003]
unstable: [(2475,5000,5003),(2475,12000,12001)]
saddles:  [(2475,12000),(2475,12001)]
```

Point positive-lower / excluded-upper margins are: stable `+0.0008292801542532781/-0.0003561848064122704`; unstable `+0.004726933556094214/-0.006247246550685058`; saddle `+0.004970129895482279/-0.004163742624699142`.

For `sigma(i->j)=||q_i||^2-q_j·q_i`, all 36 directed arcs were audited. Row-star minima `sigma/||q_i||^2` are

```text
2475:+1.0041226279779056 sink; 5000:-8.221440353677568
5003:-7.880642702839671; 12000:-8.741046405385124
12001:-2.7014516248877776; 12002:-1.8946166772388155
12003:+0.0008292801542532781 sink; 12004:-0.0003561848064122704
```

All 18 inserted/star-changed true edges were externally audited. Exactly `(12003,12004)` is all-positive, with minimum external primitive `335.6547035020198`; every other edge has a nonpositive external arrow. Its exact squared endpoint difference is positive (`0.243132330991795` decimal). Hence one carrier endpoint must be stable; protected `2475` is independently stable and disjoint, forcing `S>=2`, attained exactly.

## Positive-volume topology and chronology

Between the exact J53 active dual scaled by `2^-2` and J54, the annular complex has 14 vertices, 52 edges, 70 triangular faces, 30 positively oriented tetrahedra, 50 internal faces, 20 boundary faces, 22 interior edges, two boundary components, and Euler characteristic 2. Exact shell volume is

`120071905403073186897743679326222448657073766585735528886034254049990129/374564674634225478438271422781875239732864910180565220624810341262426112` (`0.32056387997700875`),

and the minimum tetrahedron volume is

`7133706320340113747011250918893103/36069266149385848373930620736174555136` (`0.0001977779722713205`).

A connected 12-tetrahedron spine has 16 interior edges and 11 shared interior faces; it meets the old carrier, stable/cap/both saddle sectors, protected triangle, and all five new supports. Shared face `[3,9,10]` joins tetrahedra `[15,23]`.

On the exact affine raw-support ingress, recentered exactly at every rational sample, death-before-birth fails at `t=3/10`: replacement stable `12003` has margin `0.09009596444541394`, while inherited cap `(2475,11000,11001)` has `0.2055201176927275` and inherited saddles `(2475,11000),(2475,11001)` have `0.05243841168251718,0.06575732909327726`.

Two post-centering timing controls remain independent. Moving raw `12000,12003` in `+z` gives response matrix `[[12.423591643644267,15.217004602140673],[-35.36025454967042,0]]`, determinant

`3541633650970187996881455681996628399367391451118402623287822702581/6582018229284824168619876730229402019930943462534319453394436096` (`538.0771562152005`).

## Positive chamber and stronger obstruction

The centroid-preserving family `p->diag(x,y,1)p`, `q->q diag(1/x,1/y,1)`, `|x-1|,|y-1|<=2^-24`, preserves incidence and strict `(2,2,2)`. Outward-rounded margins are: stable `+0.0008292783605316135/-0.0003561830258000013`; unstable `+0.0047269335555353165/-0.006247246549963247`; saddle `+0.0049701267683185755/-0.004163738588080897`.

For exact rows `12003` and `2475`, angle `Theta` lies in `[3.13488473402060612365448355355637757979982014774470038762249552063149781380044108708005366991512534695747,3.13488473402060612365448355355637757979982014774470038762249552063149781380044108708005366991512535815875]`, while `||q_2475||/||q_12003||` lies in `[1.30738841077572032743571745014168475263125167393891695555399949609561605623048419474369062566377385982635,1.3073884107757203274357174501416847526312516739389169555539994960956160562304841947436906256637738598835]`.

For a chain with every `sigma(q_i->q_{i+1})<=0`, multiplication plus spherical triangle inequality and concavity of `log cos` gives the necessary condition `(r_m/r_0)cos(Theta/m)^m>=1`. Directed interval evaluation gives `m=18` upper `0.993674192645393048102356711516080406628559032751769942155138526399669565658374217759373667933806182517236<1`, whereas `m=19` lower `1.0082650707072734927722620152805611963715488474767679325147618082291675631326038152109807473476720450175>1`. Thus, if the exact endpoint positions of `12003` and `2475` are retained, any nonpositive-arrow ascent route needs at least 19 true-edge arcs and 18 intermediate supports.

## First genuinely new continuation

The next branch-local topology is either (a) one macroscopic connected finite-thickness cell that deactivates or substantially relocates both `12003,12004` while simultaneously killing the cap and both saddle stars, or (b) a distributed full-row-star ascent prism/belt with at least 19 links, preferably two staggered rails sharing interior quadrilateral/tetrahedral pages. It must preserve `S2475` and `U(2475,5000,5003)`, leave `2475` as the sole sink, assign a nonpositive external arrow to every nonprotected new/star-changed edge before activation, enforce inherited death before every replacement birth, and retain at least two timing controls after exact moment closure. The 19-link bound is conditional on retaining the exact endpoint rows, not a global minimality theorem.

The mesh has 12 vertices and 20 coherently oriented triangles; every mesh edge has multiplicity two and `12-30+20=2`. The actual lattice has `12-18+8=2`. Integrate J54 as the strongest exact endpoint in this direction, but retain the run-wide exact M42 `(2,1,1)` object as the stronger equilibrium-count benchmark.
