# figure-0447

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Willow 37 — exact stable-basin cancellation and finite whole-physical-basin reduction

Branch: `[internal-source-reference]`. Continuation of literal parent `figure-0445`.

## 1. Scientific result and acceptance status

**The extra stable basin has been eliminated in exact homogeneous physical bodies. No own110 winner was obtained.** The principal new family is strict **(S,U,H)=(1,2,1)**, with additional weak000 and mechanical primitive-zero000. These are new physical halfspace intersections, each audited at its own uniform filled-volume centroid. They are not produced by merely renaming an old body's independently recentered polar.

The main continuation seed is **NW37_MONO85_QUARTER_G6**: **166 vertices, 249 true edges, 85 maximal faces, C498**, exact own121/weak000/zero000. Its complete same-physical-centre polar has **zero positive elder bars** and one root. Its physical landscape has one remaining positive elder bar, with **TP≈0.295235277655** and **delta/R²≈0.231637243370**. Stable-basin cancellation is therefore genuine, but the remaining unstable basin is substantial. This is not an own110 record despite its edge count.

Retain two alternatives. **NW37_MONO49_RESERVE_G3** is a small-coefficient 49-halfspace own121 body with E141 and minimum positive physical forest cosine≈0.0442663. **NW37_MONO47_HALF_G4** is a 47-halfspace own121 body with E135 and TP≈0.5598754. The high-reserve, low-edge and lower-bar constructions are distinct useful tradeoffs. The assignment's canonical own110 record remains C622; no acceptance change is proposed.

## 2. Exact endpoints, arithmetic and reserves

Write Vol for actual physical filled volume, R for its greatest centroidal vertex radius, and RQ for the greatest radius of its polar formed at that same physical centre. The objectives are `TP=sum(positive physical elder deltas)/Vol^(2/3)` and `TQ=sum(positive polar elder deltas)*Vol^(2/3)`.

Every row below has additional weak000 and mechanical primitive-zero000. Decimal values are approximate; recovered reports contain exact rational quantities and rigorous algebraic brackets with denominator 10^12. Empty positive-bar lists, rather than numerical thresholds, establish the displayed zero objectives.

| Exact body | V/E/F | Strict S/U/H | Positive P/Q bars | TP | TQ | Centred common-denominator bits |
|---|---:|---:|---:|---:|---:|---:|
| NW37_DAG_MONOSTABLE50_G6 |96/144/50|1/2/1|1/0|1.032133868667|0|9790|
| NW37_MONO49_RESERVE_G3 |94/141/49|1/2/1|1/0|1.203691721054|0|3925|
| NW37_MONO49_RESERVE_G4 |94/141/49|1/2/1|1/0|1.204331221090|0|5966|
| NW37_MONO47_HALF_G4 |90/135/47|1/2/1|1/0|0.559875403390|0|5889|
| NW37_MONO47_HALF_G5 |90/135/47|1/2/1|1/0|0.559910109478|0|7321|
| NW37_MONO47_HALF_G6 |90/135/47|1/2/1|1/0|0.559916987898|0|9204|
| NW37_MONO85_QUARTER_G4 — coarse failure control |166/249/85|1/4/3|3/0|0.295237782195|0|9986|
| NW37_MONO85_QUARTER_G5 |166/249/85|1/2/1|1/0|0.295234612949|0|13375|
| NW37_MONO85_QUARTER_G6 |166/249/85|1/2/1|1/0|0.295235277655|0|16413|
| NW37_H98_FLOW_G7 |192/288/98|2/1/1|0/1|0|1.097118256026|22568|
| NW37_ROOTCUT_G6_INPUT |107/290/185|2/1/1|0/1|0|1.185909855065|1073|
| NW37_SUPPORT143_EXACT_INPUT |114/255/143|2/1/1|0/1|0|1.186003645412|5789|

The eight own121 grids, three own211 constructions and one own143 control were independently frozen and exact-audited. Small halfspace coefficients do not imply a small own-centroid denominator.

| Endpoint | Minimum positive P-forest cosine | Minimum true edge/R | Inradius/R | Vol/R³ |
|---|---:|---:|---:|---:|
| MONO50_G6 |0.000038077465|0.000999996869|0.199227750117|0.205973338848|
| MONO49_G3 |0.044266304800|0.000022203010|0.182806346396|0.169147580685|
| MONO49_G4 |0.037365429743|0.000036164650|0.182842893693|0.169287848106|
| MONO47_G4 |0.000090465482|0.000055404329|0.252569670044|0.324641118539|
| MONO47_G5 |0.000207050723|0.000102896327|0.252567802984|0.324646280621|
| MONO47_G6 |0.000220834515|0.000102764704|0.252567132115|0.324644030129|
| MONO85_G5 |0.000061058923|0.000123808114|0.381596399389|0.694956245112|
| MONO85_G6 |0.000055886807|0.000159328712|0.381596730914|0.694960637252|

The positive P-forest reserve excludes actual unstable roots; it does not assert that those roots escape. MONO49_G3 has minimum positive Q-forest cosine≈0.001893472510; MONO85_G6 has Q reserve≈0.000510487270. MONO85_G5 slightly improves TP, physical cosine and denominator size, but worsens its minimum edge reserve. All are measurements after exact freezing, not inherited numerical floors.

## 3. Constructive mechanism and finite lineage

Starting from exact PRUNE94, I worked in physical halfspace space rather than a fixed 21-point complex. Deleting and replacing supports, changing their normals, permitting inactive inputs and recomputing actual physical mass produced H98_FLOW_G7. Its numerical input had 100 normals; exactly 98 supports are active after freezing. It retains the stable basin but modestly reduces the complete polar objective.

A whole polar bridge was then physically implemented as additional halfspaces. Its old-centre peak-to-elder angle was numerically 2.2030018301230325 and radial ratio 1.4295796362200537. A logarithmic-radius great-circle chain with n links has positive fixed-centre arrows when `R*cos(phi/n)^n>1`; seven was the first feasible sampled integer link count. The resulting physical halfspace intersection was **not** immediately monostable: its new own-mass numerical census was S19U10. Two 700-step repair stages still left S10U3. The radius-ordered all-point method below then reached S1U2 in 119 accepted iterations/228 objective-gradient evaluations. Its independently frozen active 50-normal input is MONO50_G6. Actual mass followed the change; the bridge proposal's old centre was not held fixed.

A 92/106 reserve-repair run from exact MONO50_G6 produced MONO49_G3/G4. A 600/822 whole-P-bar run and 41/46 restoration from exact MONO49_G3 produced MONO47. Next, all 46 positive arrows of exact MONO47_G6's polar forest were subdivided with logarithmic-radius spherical midpoints. These became new physical halfspaces: 93 input normals, initially 90 active faces and numerical S1U8. A 13/15 restoration, three whole-P-bar runs and 34/39 final restoration produced MONO85.

The decrease from MONO49_G3's TP≈1.20369 to MONO85_G6's TP≈0.295235 is about 75.47%. This compares the complete physical elder objective between two own121 bodies. It is not a percentage of progress toward own110 and does not compare TP with the old family's TQ.

### Radius-ordered all-point witness selection

A positive chord witness satisfies `x_i·(x_j−x_i)>0`, hence

`|x_j|²−|x_i|²=2*x_i·(x_j−x_i)+|x_j−x_i|²>0`.

Restricting candidate witnesses to strictly greater radius therefore excludes no feasible positive witness. It changes the infeasible numerical problem, however: unrestricted selectors can choose negative mutually pointing pairs, while the radius order prevents such two-cycles away from exempt roots. Actual hull, centroid and radius order are recomputed at every evaluation. Rank changes are nonsmooth; no global-convergence or convexity theorem is claimed.

The stable-repair stage deliberately permits two physical roots, retains the largest P bar and penalizes the others. Zero stable-repair loss is not an own110 certificate. Final exact mechanics establishes own121.

### Exact directional moment chambers, including the polar

For physical halfspaces `n_i·x<=h_i`, actual first moment M, actual centroid c=M/Vol and positive `s_i=h_i−n_i·c`, the same-centre polar vertex is `q_i=n_i/s_i`. For i→j define

```text
A=n_i·n_j, B=|n_i|²,
b=A*h_i−B*h_j,
w=B*n_j−A*n_i.
```

Then

`q_i·(q_j−q_i)=(Vol*b+w·M)/(Vol*s_i²*s_j)`.

Thus its positivity is exactly the directional moment inequality **Vol*b+w·M>0**. For a physical raw-point chord d=p_j−p_i, the analogous numerator is **Vol*(p_i·d)−d·M>0**.

These witnesses need not remain true edges. They do not require an isotropic centroid-shift ball or prescribed cosine floor. Coefficients must be recomputed when geometry changes. Density remains uniform and Q is never independently recentered. The exact checker verifies 92 P/48 Q arrows for MONO49_G3 and 164 P/84 Q arrows for MONO85_G6. It separately recomputes complete elder landscapes with the older direct-vector/Fraction formulas and checks equality with the homogeneous-integer implementation.

## 4. Complete surviving basins and true incidence

Physical vertex IDs are lexicographic exact rational raw-coordinate IDs. Polar IDs are regenerated from actual frozen-grid primitive outward planes. They are not inherited across grids: MONO85_G6 has Q root38; G5 has Q root39.

| Endpoint | P roots / positive forest arrows | Q roots / positive forest arrows | Remaining positive bar | Death edge | Strict-upper vertices / full cut edges |
|---|---|---|---|---|---:|
| MONO50_G6 |1,81 /94|26 /49|P81→1|22–25|45/29|
| MONO49_G3 |0,88 /92|24 /48|P88→0|22–27|48/28|
| MONO49_G4 |0,88 /92|24 /48|P88→0|21–27|48/28|
| MONO47_G4/G5/G6 |1,85 /88|23 /46|P85→1|23–27|42/32|
| MONO85_G5 |3,162 /164|39 /84|P162→3|21–24|41/33|
| MONO85_G6 |3,162 /164|38 /84|P162→3|21–24|41/33|
| H98_G7 |3 /191|12,17 /96|Q12→17|64–68|41/77|
| ROOTCUT |16 /106|2,11 /183|Q11→2|114–160|52/50|
| SUPPORT143 |0 /113|2,11 /141|Q11→2|83–119|51/57|

Complete positive forests, all true edges and exact edge levels, all positive elder events, attaining paths and whole strict-upper cuts for all 12 grids are reconstructed by the inline capsule. BASIN_INDEX.json also preserves the finite cuts/paths and strict features directly. No basin is discarded merely because another bar is larger.

MONO85_G6's maximal-face histogram is 10 triangles,17 quadrilaterals,26 pentagons,14 hexagons,2 heptagons,10 octagons, and one each of 9-,10-,12-,13-,19- and29-gons. All 166 vertices are trivalent. Its unique stable face is `[1,114,130,134,2]`, unstable vertices are3 and162, and its saddle is edge21–24. Its complete remaining P basin is:

```json
{"peak":162,"older":3,"death_edge":[21,24],"component":[24,25,26,27,28,29,30,33,49,55,58,59,62,64,67,71,81,97,117,129,130,134,138,139,140,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165],"boundary":[[134,2],[139,3],[156,4],[159,5],[153,16],[151,18],[24,21],[24,83],[28,90],[30,91],[33,75],[152,35],[49,72],[55,93],[155,56],[157,56],[71,57],[58,107],[59,61],[62,61],[64,110],[67,113],[117,70],[81,116],[97,131],[130,114],[150,127],[140,131],[165,137],[150,143],[152,147],[151,148],[153,149]],"path":[162,138,129,117,97,81,71,67,64,62,59,58,55,49,33,30,29,25,24,21,19,11,10,0,1,2,3]}
```

Every cut edge has exact level at most death; the displayed path's minimum level is exactly death. Both are checked over the complete edge set. Relative P bar≈0.23163724336957428 and unscaled radial-height gap≈0.20999047497807422 are endpoint measurements, not changing-family Hausdorff exclusion bounds.

MONO85_G4 preserves S1 but adds unstable roots33 and81: exact S1U4H3. Its two small additional P bars have relative heights≈3.956566615856791e-9 and3.9733633621731516e-8, single-vertex upper components and three-edge cuts. The main bar remains≈0.231633187176. There are no weak equilibria or primitive mechanical zeros. The extra bars are real exact births, not ignored tolerances; G4 is not own121.

## 5. Exact structural side constructions

SUPPORT143 removes these 41 sorted exact parent support IDs, without moving the surviving planes:

`[150,140,139,118,90,99,76,126,88,98,160,73,72,97,71,93,74,100,46,108,92,67,109,75,165,115,25,102,28,85,60,45,41,133,47,42,44,39,152,38,106]`.

It strictly enlarges physical volume and remains own211. Its 114 vertices with E255 illustrate why the 105-vertex sufficient bound is not necessary.

ROOTCUT intersects exact PRUNE94 with

`−696830*x+553238*y+456460*z<=1329338`.

Old unstable input18 violates this inequality by exactly `5983493533/125000`. The new unique unstable vertex16 is

```text
(-121391524226706359/87200036415000000,
 1498711215200471/1937778587000000,
 -13106107011416203/87200036415000000).
```

It lies on the cap, is not an old supplied point, and the new physical volume is strictly smaller. This is a genuine physical-root turnover, but the body remains S2U1H1. Its maximal faces are170 triangles,14 quadrilaterals and one14-gon. In contrast, H98's changed numerical root index is not another root turnover: its incident input supports stayed `[2,6,18]`.

## 6. Exact audit and own-mass mechanics

The H-auditor exhausts integer plane triples with exact pair-cache arithmetic, not floating hull nomination. It tests intersections against all halfspaces, merges exact vertices, reconstructs maximal polygonal faces and removes inactive inequalities. It checks paired oriented edges, connectedness, Euler's relation and vertex links. Positive face-area normal weights balancing to zero, together with three independent normals, certify boundedness.

Volume and first moments are exact. Centred tetrahedra have positive volumes, centred first moments vanish, and three boundary-divergence volume identities plus nine first-moment identities agree. A separately implemented AREA_RADIUS audit verifies mechanics/mass via interior-anchor tetrahedra and projected-polygon divergence. This is **two mechanics/mass implementations, not two independent hull enumerators**. An additional all-point cone test agrees with the true-edge vertex census.

MONO85_G6 has Vol≈1.3628885838144735 and raw-frame centroid≈`[0.015797288854384552,-0.036297394103470035,-0.008522735212680656]`; its exact common centred denominator has16413 bits. MONO49_G3 has Vol≈1.8894850880456684 and centroid≈`[-0.12574064371743054,0.13245537877056066,-0.13218103137772633]`. Exact values are recomputed from literal halfspaces, not these displayed decimals.

Optional ctypes/libgmp rational acceleration passed 400 arithmetic controls. Exact tetrahedron446 and weak-prism controls passed. The entire MONO49_G3 report generated with standard-library Fraction and GMP was **byte-identical**. Both complete landscapes for G3 and MONO85_G6 passed independent direct-vector versus homogeneous-integer comparison. No accepted endpoint uses density variation.

## 7. Numerical execution and bounded failures

Discovery used CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64 and one Torch/BLAS/OMP/MKL thread. These are observed execution versions. Exact recovery does not need the numerical packages. NUMERIC_PLAN.json embeds literal checkpoints or exact recipes, all nondefault settings, final binary64 hashes and accepted-iterate census summaries.

Support runs use L-BFGS-B, maxfun20000,maxls40,maxcor20,ftol1e-15,gtol1e-10.

| Run | Accepted / objective-gradient evaluations | Requested iteration limit | Numerical terminal S/U |
|---|---:|---:|---:|
| H100RAW1 |301/406|450|2/1|
| H100FLOW1 selected prefix |584/898|700 originally; interrupted|2/1 at saved prefix|
| H100FLOW2 |300/501|300|2/1|
| CHAIN7_STABLE |700/925|700|33/2|
| CHAIN7_STABLE2 |700/1026|700|10/3|
| DAG_STABLE |119/228|600|1/2|
| MONO50_RESERVE |92/106|500|1/2|
| MONO49_WHOLEP_FLOW |600/822|600|1/4|
| MONO49_WHOLEP_REPAIR |41/46|350|1/2|
| QREFINE93_REPAIR |13/15|400|1/2|
| QREFINE93_FLOW1 |500/962|500|1/2|
| QREFINE93_FLOW2 |600/888|600|1/3|
| QREFINE93_FLOW3 |600/766|600|1/8|
| QREFINE93_REPAIR3 |34/39|350|1/2|

DAG_STABLE's complete104-row checkpoint and119/228 output were replayed with identical binary64 coordinates. Other trajectories have runnable recipes but were not all independently rerun. Callback and initial/final diagnostic evaluations are additional to the objective-gradient counts.

DAG_STABLE uses radius ordering, raw normalized all-point margins, root quotas P2/Q1, target margins2e-6, witness penalties10000, P/Q weights100, TPcap1.5, minimum edge/R target0.0001, inradius/R target0.08 and Vol/R³ target0.12. Reserve repair raises both margin targets to0.001 and penalties to100000. Subsequent whole-P runs use Ptarget1e-5,Qtarget1e-4; the last three use witness penalties1e6 and Pweights1,5,5. Final restoration uses penalties1e7 and TPcap0.3. These are soft targets, not inherited geometric floors.

DAG_STABLE had accepted iterates up toS39U4; reserve repair reachedS11U2. The1700 accepted iterates of the final three full-P runs all had numericalS1 and no detectedQbars, while maximumU counts were6,9,11. These are discrete numerical observations, not a class-preserving homotopy proof. Exact G4 freezing detects the extraPbirths already reported.

Other bounded experiments are preserved with scripts, seeds, settings and input recipes:

- The94-coordinate all-point probe completed300/463 at numericalS4U1. The12000case fan survey, PCG64seed370220, had noS1 and307U1cases. The2000case cap survey, seed370221, had noS1,17U1cases and175over-budget cases; proposal1638 produced exactROOTCUT.
- Support deletion made84accepted deletions/2688successful candidate censuses. An initial200-second interruption saved65/2080; continuation added19deletions. The first41define exactSUPPORT143; the eventual100-support numerical scout is not itself an exactown211 assertion.
- Twenty whole-upper-set removals fromH98 yielded noS1. WHOLE57_FLOW endedS6U9 at43/238. A10000case projective/affine survey, seed370224, had noS1 and7U1cases. Three7-,10-,14-link projective-centre solves completed8/11each and remainedS29U10 despite displayed centroids near10^-13.
- A650/820 alternative bridge repair endedS9U2; its25accepted/935census deletion continuation allowedS to increase and endedS9U2. A both-root-one DAG run stopped abnormally at9/292 withS28U29. A mixed-selector both-root-one run completed500/893 atS1U6.
- Ten physical bridge cases fromMONO50 included a numericalS7U1,TP0 body with101vertices/E282/F183. Its complete101-point continuation with seed370225,jitter1e-5 endedS4U30 at29/584. Ten physical bridge cases fromMONO85 used minimum short/long counts12/30; none hadS1 orU1, and several exceededE310.
- A requested8000case MONO49cap survey, seed370226, was interrupted at a200-second outer limit after the3000completed-case checkpoint. Terminal count is unknown. The included exact source patch reproduces the bounded3000case prefix;8000completion is not claimed. H100FLOW1's584/898 likewise describes its saved prefix, not its unknown terminal count.

The receipts also preserve H100OPT1's14/305 abnormal run, H100FLOW3's450/655 and H100REPAIR3's56/67, with settings. Lower numerical scout objectives do not supersede durable exact bodies. None of these finite failures establishes stationarity or excludes a family.

## 8. Source authority and reading

The journal update was read through all1601lines and the complete new support-gate/centroid-chamber material through EOF. Unchanged earlier material and the22-file parent recovery had already been supplied and read. Historical IDs or paths were not treated as accessible dependencies.

The named parent declares SHA256 `f57c846c102989063465ec50d170bd6210969dcc31d1f0c6b68655dd3dce51b7`. The73292-byte Markdown suffix extracted after its journal heading instead hashes as `a29c52d8a187ab8c3af6a2e584ae304a18757ed6d1c37de2b1aa98e16efaf3ac`. This outer-payload discrepancy remains unresolved; no unavailable envelope is invented. The inner source dictionary verifies112857bytes and SHA256 `5c096b6eaa82aa1565e26b265682e2b3e5bb142668be4929093e58076c2e43d7`.

The exact PRUNE94 input used is2338bytes, SHA256 `6f172585e0d6ce14c2c351bda79c65fa23006dbf46f11611a0c970c83790d248`. Its literal geometry and every dependency of the new bodies are embedded below. The older root0 VL12 parent is not relabelled TURNOVER/RETRACT/root20. The supplied fixed-body support gate is not an exclusion of these changed bodies.

## 9. Complete recovery, manifests and replay status

Save the following Python block as RECOVER_NW37_CONTINUATION.py. It contains all41source/data units: exact parent, defining inputs, numerical producers/checkpoints/settings, independent-grid rules, both mechanics implementations, complete elder/cut generators and exact chamber checks. No originating sandbox or external source fetch is required.

Independent rounding is exactly `round(Fraction(float.fromhex(value))*10**k)`, ties to even. Each normal defines integer physical halfspace `[Nx,Ny,Nz,10**k]`. Coarse grids are not derived by rounding fine-grid outputs. Inactive-input choices are explicit in FREEZE_INPUTS.json. Structural bodies use the exact parent deletion/cap recipes.

```text
python -B -S RECOVER_NW37_CONTINUATION.py NW37_CONTINUATION
cd NW37_CONTINUATION
python -B -S FREEZE_CONTINUATION.py
python -B -S REPLAY_CONTINUATION.py NW37_MONO49_RESERVE_G3
python -B -S REPLAY_CONTINUATION.py NW37_MONO85_QUARTER_G6
python -B -S REPLAY_CONTINUATION.py all
python -B -S CHECK_WITNESS_CHAMBERS.py --gmp --direct NW37_MONO49_RESERVE_G3_EXACT.json NW37_MONO85_QUARTER_G6_EXACT.json
python -B -S CHECK_CONSTRUCTIONS.py
python REPRODUCE_CONTINUATION_NUMERIC.py DAG_STABLE
```

Optional systemGMP6.3.0 accelerates exact recovery. Standard-library-only recovery is `python -B -S REPLAY_CONTINUATION.py --fraction NW37_MONO49_RESERVE_G3`; omit --gmp from the chamber checker. NumPy/SciPy/Torch are only needed for optional numerical rediscovery.

All12grids completed exact working-directory audits. Cold source-only extraction independently reproduced G3,MONO85_G6,H98_G7 with exact output byte/hash equality. A combined300-second cold run stopped afterG3; separate invocations subsequently completedG6andH98. No all12-in-one cold run is claimed. Final packaged core files were byte-identical to the successful cold-replay core, and all packaged Python sources compiled.

Observed markers include:

```text
NW37_GMP_FRACTION_ARITHMETIC_CONTROLS_PASS 6.3.0
TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS
NW37_CONTINUATION_INDEPENDENT_FREEZE_12_INPUT_HASHES_PASS
NW37_CONTINUATION_EXACT_HASH_PASS NW37_MONO49_RESERVE_G3 94 141 49 [1, 2, 1]
NW37_CONTINUATION_EXACT_HASH_PASS NW37_MONO85_QUARTER_G6 166 249 85 [1, 2, 1]
NW37_CONTINUATION_EXACT_HASH_PASS NW37_H98_FLOW_G7 192 288 98 [2, 1, 1]
NW37_CONTINUATION_SOURCE_ONLY_REPLAY_PASS 1
NW37_NUMERICAL_CONTINUATION_IDENTICAL_PASS DAG_STABLE 119 228
NW37_DIRECTIONAL_MOMENT_WITNESSES_PASS 92 48 True
NW37_DIRECTIONAL_MOMENT_WITNESSES_PASS 164 84 True
NW37_FINAL_CAPSULE_ALL_PYTHON_SOURCES_COMPILE_PASS
NW37_FINAL_CORE_IDENTICAL_TO_COLD_REPLAY_PASS
```

The directional-witness lines give marker prefixes; full lines additionally identify output files and receipts. EXPECTED_CONTINUATION.json contains every input/report byte count and SHA256. Representative receipts:

```text
NW37_MONO49_RESERVE_G3.json
1068 bytes; SHA256 8aaa432b9e7ca8229930629506e6ceddb3b7ecaf5536da50bcffea786fc3a033
NW37_MONO49_RESERVE_G3_EXACT.json
3790059 bytes; SHA256 5db5e0c583101c50f7589f2a3feb4a800018fedc3cdf3b60bf3894405590b276
NW37_MONO85_QUARTER_G6.json
2887 bytes; SHA256 419fcff38d180a217980990f023a366ebb3b55f20f354de2ed44120bd4753f90
NW37_MONO85_QUARTER_G6_EXACT.json
27536678 bytes; SHA256 61f281b8a7dd2766d022fc0e5462e983d103701912dcc2452be07c68cca2937e
NW37_MONO85_QUARTER_G5.json
2547 bytes; SHA256 f04b3b5463b73093b7c8eaa9e93a1001d4b63487dd354004a919ecc7e7da413c
NW37_MONO85_QUARTER_G5_EXACT.json
22440806 bytes; SHA256 21020bae8daf45f0c60ac07a1168a3aa367cba797d3eb4bbfe35bb908838cf8d
NW37_MONO49_RESERVE_G3_EXACT_CHAMBERS.json
356852 bytes; SHA256 0172c777531487b393564ddda750655e410a60dcf261b15618cfdad9edd1eaa3
NW37_MONO85_QUARTER_G6_EXACT_CHAMBERS.json
2534420 bytes; SHA256 96c459a1a114f45b6a1a2c28cb542e50a152a021e800daf4389d640399b82031
```

The canonical41-file source dictionary is287207bytes, SHA256 `939ee82786c952c9abebbb2f8df72c02a2c9c862cf7a5948cd69116f3be2cb1c`. ItsXZpayload is69396bytes, SHA256 `33789fcbaee1bc0cb01be23966db52d0a9ee6af0e620f341256775bb7cf2ca26`; base64 has92528non-whitespace characters. The decoder checks archive and every per-source receipt.

Convenience copies: [sources and decoder](sandbox:/mnt/data/NW37_CONTINUATION_SOURCES.zip),198643bytes,SHA256 `7ca35600dfbcbdb672c1696523656b5a2883fdd34d05963ddc56b75f075e352f`; [all exact reports](sandbox:/mnt/data/NW37_CONTINUATION_EXACT_REPORTS.zip),68515027bytes,SHA256 `046b4a2bee6c52d8f2aa70200232a6fbbe7564f4996ee4aba92a0187bc7b717d`. The inline capsule is sufficient without those files.


[Encoded source block omitted; the code in this passage is incomplete.]


## 10. Most useful continuation

The finite architecture has changed the task from cancelling the old extra stable basin while retaining U1 to cancelling **one complete physical unstable basin while retaining the now exact S1**. Continue primarily from MONO85_G5/G6; preserve MONO47_G4 for lower edge cost and MONO49_G3 for much larger positive physical reserve.

The85-face seed has61spare edges below310. At most20additional active supports gives at most105faces and henceE<=309 as a sufficient budget; this is neither necessary nor a feasibility theorem. Address the entire41-vertex/33-edge P region, permitting root changes and physical mass compensation while certifying the single-Q-root directional moment chamber. The immediate physical bridge scouts did not retainS1, so local chord insertion alone is not a completed mechanism.

The results establish durable exact monostable constructions, actual stable-basin cancellation and substantial complete physical-bar reduction. They do not establish physical-basin cancellation, an own110 winner, local optimality or impossibility of anE<=310continuation.
