# figure-0129

AI research report · 2026-08-28 UTC

---

# Exact/directed asymmetric-belt continuation — slot-4 handoff

## Verdict

**Sharply characterized nonwinner; no strict own-centroid `(1,1,0)` endpoint was found.** The supplied journal ended at the far-side exact root `(H,V,E)=(2638,5272,7908)`, class `(37,37,72)`, with first unclassified gate `(1390,1425,1426,2337)` and prescribed an azimuthally localized asymmetric belt with `(u,t1,t2)` kept as hard moment variables. The acceptance gate still requires a literal finite own-centroid `(1,1,0)` body with complete H/V/E, exhaustive strict audits, verifier, and mesh.

I rebuilt the named gate, reduced the inherited relay, then traversed an exact 220-row half-turn-odd localized field through **28 actual incidence cells and 27 isolated circuit walls**. The best and farthest pre-birth endpoint is `C26`, with `(H,V,E)=(2666,5328,7992)` and strict class `(5,39,42)`. The next certified circuit event `W26` is a birth, not a cancellation, and its post-cell `C27` is `(2665,5326,7989)`, class `(5,40,43)`. Thus 32 of the 36 inherited nonprotected stable equilibria are destroyed, but four extra stable rows remain.

## Exact family and hard moment equations

Parameter order is `p=(c1,c2,t0,t1,t2,u,a2,aH,aL,b)` and the normative 4,324 polar rows are

`q_i(p)=(Qint_i/2^48)(1+2^-24 Wint_i·p)`,  `P(p)={x:q_i(p)·x<=1}`.

The exact generator SHA-256 is `85011b6a70ee321b1e931900c9135f447f8ba4ab3e31a82ffc0d291bcdc81ef1`. Rows `0,4321,4322,4323` are frozen. Fixed controls are

`c1=0x1.dd5d71082df60p-30`, `c2=0x1.8858df5d891f7p-29`, `t0=0x1.1db0d4b1b0ad2p-15`,

`a2=0x1.5c28f5c28f5c3p-3`, `aH=0x1.47ae147ae147bp-7`, `aL=0x1.47ae147ae147bp-6`.

`b` is the independent localized coordinate. `Bsplit` is supported on exactly 220 complete one-ring rows, is half-turn odd, vanishes on protected rows, and has int64 SHA-256 `1520bf82f2fa68caaa3d5e25d830aa73d1df48a012958d224021f09bea66850d`.

For every rebuilt cell, `(u,t1,t2)` is re-solved from the actual ordinary first moments

`V=Σ det(v_a,v_b,v_c)/6`,

`M=Σ det(v_a,v_b,v_c)(v_a+v_b+v_c)/24`,

using the current oriented boundary triangles. Every vertex is recomputed from its actual active row triple by exact Cramer arithmetic. No H/V/E object, moment equation, or equilibrium label is inherited after a row deactivates or a circuit flips.

## Starting gate `(1390,1425,1426,2337)`

With the predecessor parameters fixed, the primitive circuit polynomial in `u` is

`c0+c1u+c2u^2+c3u^3`, where

`c0=12111506861501835055100695131035663988089252374363360768085407966193156614868959232`,

`c1=-49055861695053259214084167697032118009281325986138947855361050883736457515431362560`,

`c2=-2249845099898644049399174747398199628181113529138552728917773975308964229245203695`,

`c3=9301345342004075036341131013608340108704124582404995222823866901881218953904128`.

Its unique relevant root lies in the exact Sturm interval

`(4272041018522103868028636/17496833516492160199818945,2865087268539911582641321/11734427345270753994280054)`.

The actual diagonal change is

`(1390,1425,1426),(1425,1426,2337) <-> (1390,1425,2337),(1390,1426,2337)`.

Both strict pre/post rebuilds have `(H,V,E,F,T)=(2638,5272,7908,2638,10540)`, Euler `2`, and class `(37,37,72)`. This gate is mechanically neutral.

## Relay reduction and localized cell atlas

At `b=0`, after the exact asymmetric relay reduction, the actual root has signature `ff606b859aa6ba31e8e5ca62c73d79588206948f2f42adcb54fae410b942a12f`, `(H,V,E)=(2666,5328,7992)`, and class `(5,39,42)`. Relative to the inherited `(37,37,72)` body, exact rebuilt ledgers show: 32 stable rows removed and none born; 36 unstable vertices removed and 38 born; 68 saddle edges removed and 38 born; 146 rows deactivate and 174 activate; 516 facets disappear and 572 appear. The five persistent stable rows are `0,2384,2385,2402,2403`.

The complete atlas contains cells `C00`–`C27` and walls `W00`–`W26`. For `C00`–`C26`, every exact root rebuilds to

`H=2666`, `V=5328`, `E=7992`, maximal faces `2666`, boundary triangles `10652`, Euler `2`, class `(5,39,42)`.

`C27` rebuilds independently to

`H=2665`, `V=5326`, `E=7989`, maximal faces `2665`, boundary triangles `10648`, Euler `2`, class `(5,40,43)`.

All 28 cells have separately isolated exact ordinary-centroid roots. The canonical atlas stores every exact dyadic Krawczyk box, full signature, actual H/V/E files, maximal face cycles, surface triangles, all equilibrium ledgers, and all directed margins. Representative exact root boxes in variable order `(u,t1,t2)` are:

- `C00`: `u∈[0x1.c4f344b3c4b48p-3,0x1.c4f344b3c4b4cp-3]`, `t1∈[0x1.7e21fee48352bp-21,0x1.7e21fee483d2bp-21]`, `t2∈[-0x1.72e63b17bc888p-15,-0x1.72e63b17bc778p-15]`.
- `C26`: `u∈[0x1.c5ff15359421ep-3,0x1.c5ff15359424ap-3]`, `t1∈[0x1.27502eac7b5c7p-15,0x1.27502eac7e555p-15]`, `t2∈[-0x1.f7d0c52390db7p-12,-0x1.f7d0c5238c9bdp-12]`.
- `C27`: `u∈[0x1.c607d5b026a5bp-3,0x1.c607d5b026a5fp-3]`, `t1∈[0x1.30c326dcafb19p-15,0x1.30c326dcafb49p-15]`, `t2∈[-0x1.036ba3eefb3c4p-11,-0x1.036ba3eefb3a8p-11]`.

The ultrathin cell `C11`, between two near-coincident walls, was re-certified at 150 decimal digits with an exact `2^-220` rational box. Its four limiting nonincidences have positive lower gaps `1.5820470908434878e-16`, `1.5368769313790902e-16`, `1.2312374788811886e-16`, and `1.2037378115407718e-16`; the other `23,022,284` nonincidences have lower gap at least `1.468914878621774e-9`. The two limiting edge cones are strict non-saddles. The full rational endpoints are in the linked report and certificate.

The exact wall sequence is:

`(4155,4156,4190,4191)`, `(4147,4148,4182,4183)`, `(2410,2411,2867,2902)`, `(2392,2393,2849,2884)`, `(4105,4106,4141,4176)`, `(4169,4170,4204,4205)`, `(2410,2866,2902,2937)`, `(4165,4166,4200,4201)`, `(2392,2848,2884,2919)`, `(4151,4152,4186,4187)`, `(4203,4204,4238,4239)`, `(4185,4186,4220,4221)`, `(4141,4142,4177,4212)`, `(3829,3830,3864,3865)`, `(2382,2418,3363,3398)`, `(2400,2436,3381,3416)`, `(4153,4154,4188,4189)`, `(4123,4124,4158,4159)`, `(4232,4233,4267,4268)`, `(4159,4160,4194,4195)`, `(4195,4196,4230,4231)`, `(3758,3759,3793,3794)`, `(1692,2287,2321,2322)`, `(2379,2973,3008,3009)`, `(4170,4171,4205,4206)`, `(2397,2955,2990,2991)`, `(1657,1692,2287,2322)`.

Each wall certificate solves `(Mx,My,Mz,D_Q)=0` in `(u,t1,t2,b)` on the actual pre-cell by a strict four-dimensional Krawczyk inclusion and verifies the actual pre/post facet difference. `W00`–`W25` are class-neutral between their certified adjacent roots. `W26` has exact

`b∈[0x1.8460c8427df9dp-19,0x1.8460c845ba239p-19]`,

removes `(1657,1692,2287)`, `(1657,2287,2322)`, `(1692,2287,2322)`, adds `(1657,1692,2322)`, changes `(H,V,E,F)` by `(-1,-2,-3,-1)`, and changes `(S,U,H)` by `(0,+1,+1)`. It is the first certified incidence crossing that changes the class, and it worsens it.

## Complete own-centroid audits and margins

Every root box audits every maximal face for stability, every vertex for instability, and every true edge by its full four-component normal cone. Across the 28 exact cells:

- global minimum actual nonincident H/V gap is `1.2037378115407718e-16` in `C11`; all other generic cells have at least `1.468914878621774e-9`;
- minimum included stable margin is `0.0009462810843378077`;
- closest excluded face upper margin is at most `-1.1915694494213367e-5`;
- minimum included unstable margin is `0.006569820018885905`;
- closest excluded vertex upper margin is at most `-0.007212369696174955`;
- minimum included saddle margin is `0.004105699046674579`;
- closest excluded edge-cone upper margin is at most `-0.0012175796461570962`.

For strongest endpoint `C26`, the directed margins are: stable `>=0.0009462810843378077`, face excluded `<=-2.100009168293226e-5`, unstable `>=0.023285292448053902`, vertex excluded `<=-0.007212369696174955`, saddle `>=0.02894698594388946`, edge excluded `<=-0.004549938588307162`.

## The localized field changes the remote relay, not merely its position

The first hard-centred localized wall is remote quad `(4155,4156,4190,4191)`; none of its rows belongs to direct `Bsplit` support. Its exact circuit equation is `D(t2)=D0+B t2`, with

`D0=34211877905624732096329664277039755/5575186299632655785383929568162090376495104`,

`B=6283545950745982593186205651330563638359002399/46768052394588893382517914646921056628989841375232`,

and exact wall

`t2=-40998576099163838951589684627384272158720/897649421535140370455172235904366234051286057`.

A strict Krawczyk certificate simultaneously solves the actual pre-cell moments and this disjoint-support circuit. Its diagonal change is `(4155,4156,4191),(4155,4190,4191) -> (4155,4156,4190),(4156,4190,4191)`.

At the separately rebuilt hard-centred sample `b=5e-6`, six rows deactivate and one activates; 75 facets disappear and 65 appear, with 60 removals and 51 additions disjoint from direct support. Six stable rows `4174,4175,4176,4206,4207,4213` are born outside support, together with seven remote unstable births and thirteen remote saddle births. The class becomes `(11,46,55)`. This is coherent remote relay nucleation caused by moment closure, not nominal transport of a supported belt feature.

## First unclassified continuation circuit

Beyond `C27`, independently rebuilt fibres bracket the next incidence change at `b∈[3.825e-6,3.8375e-6]`, quad `(2382,3362,3363,3398)`. It removes `(2382,3362,3363)`, `(2382,3363,3398)`, `(3362,3363,3398)` and adds `(2382,3362,3398)`. Pre/post signatures are `d87d47ec1f701e780bf384885847501d437fa679645ca61a0ca90154e5112703` and `6e8661a540456a2fbeff24f71a42606d6149cb15f67eb90ce4b4a05f5ed751fa`. Exact row labels and actual facets are known, but no four-dimensional Krawczyk wall box is claimed for this next gate.

## Independent verification, meshes, and artifact

A standalone verifier re-read the normative integer generator and human-readable cell files, reconstructed all 28 H sets and every V by exact Cramer arithmetic, regenerated every E from dual row-pair incidence, checked maximal cycles, closed-manifold/Euler identities, root and wall inclusions, actual wall adjacency, remote-support evidence, and the terminal mesh. The portable staged rerun returned `PASS=true`, `cells_verified=28`, `walls_verified=27`. It does not read a serialized hull checkpoint.

- Complete 508-file exact bundle (`slot4_localized_asymmetric_belt_exact_nonwinner.zip`), SHA-256 `dddc3c1a61763a2e59aceb746465b0d3fe4946a4fca9365f1e33f24adf775934`.
- Full exact handoff with the 28-cell root-box table, 27-wall facet table, and all per-cell margins (`RESULT_FINAL.md`).
- Canonical machine-readable atlas (`complete_atlas.json`), source-atlas SHA-256 `34698dd70cd9489b7facf1f15d608079d7f74275c93e185bd7c216be0ceb5bc3`.
- Independent verifier (`verify_localized_independent.py`) and passing transcript (`verification_localized_bundle.txt`).
- Strongest pre-birth `C26` OBJ (`strongest_prebirth_C26.obj`) / STL (`strongest_prebirth_C26.stl`).
- Terminal `C27` OBJ (`terminal_C27.obj`) / STL (`terminal_C27.stl`).
- SHA-256 manifest (`MANIFEST.sha256`), manifest SHA-256 `7f88853e86753e7f187373c1a7df67af08c2c940b9954d88c75a33f8f34a3b3c`.

`unzip -t` reports no compressed-data error.

## Uncertainty and continuation

This is an exact finite atlas, not a CAD exclusion of every real `b` or every possible localized field. A transient mechanical cancellation and rebirth inside one open incidence interval has not been globally excluded, although every listed exact root is strict and dense actual-fibre rebuilding found no winner. The four extra stable rows are rigidly `2384,2385,2402,2403` at all certified roots, and the first class-changing incidence wall does not touch them.

The next nonduplicative move is therefore not more scalar `b`: introduce at least two azimuthally separated controls spanning the complete stars of the two stable pairs, project their moment images against the `(u,t1,t2)` Jacobian, solve all three moments hard, and track mechanical-zero surfaces together with incidence circuits. The first useful target is a simultaneous whole-pair cancellation with no remote birth.
