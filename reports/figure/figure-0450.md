# figure-0450

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Willow 00 — actual-centroid stable cancellation on the compact H frontier

Branch: `[internal-source-reference]`.

## 1. Outcome and acceptance boundary

**The extra stable basin was cancelled at actual uniform-volume centroids, but uniqueU was not simultaneously recovered. No own110 endpoint was obtained.** The constructive frontier has changed from own211 to new exact own121 solids. These are genuine uniformly filled bodies, not reference-centre certificates.

The most useful compact continuation obtained here is **BF35REC_G4: V66/E99/F35/C198, strict121, additionalweak000**. A lower complete physical-basin alternative is **BA69REC_G5: V122/E183/F63/C366, strict121, additionalweak000**. A separate **C5REF_G5: V132/E198/F68/C396, strict121** has a certified five-link reference escape chain, but the newly filled enlarged hull is not certified own110.

The exact recovery preserves **52 new rational solids: 34 strict121, nine strict211, one strict413, and eight coarse-grid controls. All52 have additionalweak000 and primitivezero000. All52 satisfy true E≤310.** None replaces the supplied journal's canonical own110 C622 record.

A new scoped theorem supplies a necessary radius/complexity condition for a uniqueU endpoint while permitting arbitrary root and witness exchanges. It excludes three particular retained-two-point, fixed-centre circumradius envelopes—not nonlinear H-space generally.

## 2. Source authority

Authoritative parent: **`figure-0449`**, runtime-declared SHA-256 **`edd94807597b747cda0838eb6a3d37f99686637a6c6d3dfd2bc7848998176c9d`**.

The entire supplied 1617-line journal, its literal parent payload and all26 decoded parent units were read before the new research. `research-journal(20260921-033321).md` is322767 bytes, SHA-256 `18c87a5e01cc1f74d643c8664c9ee6ade0052beb13dad641030b3becd2ee008c`. The verified parent dictionary is120599 bytes, SHA-256 `7d8f743fdc6419dac8b3fd2178636667b9d8dc1a9edf5163e0ee519f90a2b4a2`. The enclosing runtime result hash is not asserted to be the hash of a differently serialized Markdown file.

The literal entrances retain their identities:

- `H38_G6.json`:1292 bytes, SHA-256 `29e84d28aa484aa11ba45691e457e03cbbbf33afbacb42ad84b45afd9cebb0bb`.
- `ROB12_G4.json`:341 bytes, SHA-256 `a93df9dafb8494780f57da64fcde4ec4d053b0a55f92991970f0d734c422b3b3`.

H38's shallower, thicker geometry was the productive entrance. ROB12's small support count did not compensate for its deep polar basin in the executed searches. No old affine-component exclusion was transferred to these bodies. No conflicting parent coordinates/classes or missing dependency for the exact endpoints was found.

## 3. Exact endpoint map

Here C=2E. D is the bit length of the **common own-centred coordinate denominator**, not the raw grid. TP is the sum of all positive physical squared-radius bars divided by volume^(2/3); it is not a distance-to-solution. Every row below has strict121, additionalweak000, primitivezero000, exactly one positive physical Pbar and no positive same-physical-centre polar Qbar. Displayed decimals abbreviate regenerated exact outward enclosures.

| Exact body | V/E/F/C | D | TP approximately | inradius/R approximately |
|---|---:|---:|---:|---:|
| Q121_G6 |38/57/21/114|4043|7.895161512|.080028102|
| R155_G4 |36/54/20/108|2587|7.597334282|.080027400|
| MONO14_G6 |24/36/14/72|2458|197.692069904|.007521167|
| C16R_G6 |34/51/19/102|3723|4.961702|.080000026|
| C12R_G4 |34/51/19/102|2398|4.316223855|.079996385|
| C8REF_G4 |68/102/36/204|4664|1.534663308|.152397222|
| C6REF_G5 |66/99/35/198|5787|1.198114417|.151022417|
| C5REF_G5 |132/198/68/396|10765|1.036902590|.150006550|
| **BF35REC_G4** |**66/99/35/198**|4252|**.822447828**|**.236791770**|
| **BA69REC_G5** |**122/183/63/366**|10104|**.553693211**|**.268750220**|

BF35REC supplies37 inequalities but only35 are active; BA69REC supplies69 but only63 are active; C5REF supplies69 but only68 are active. The exact active-only representation is regenerated from the audited maximal faces:

`[list(f['n'])+[f['h']] for f in audit['faces']]`.

After removing inactive inequalities, the sufficient105-support budget leaves70,42 and37 new support slots respectively. Keeping inactive rows leaves68,36 and36 slots. A bounded full-dimensional three-polyhedron with F≤105 has E≤3F−6≤309. This is a sufficient architectural allowance, not a universal105-row restriction or an equilibrium guarantee.

### BF35REC_G4: complete mechanical and basin data

Actual uniform volume is approximately1.0582618191923876. Actual centroid is approximately

`(.022181569976865403,.007698692430637609,.016995806402297538)`.

Exact fractions are regenerated from the literal H input; these decimal displays are not the definition. Strict features are **S=[1], U=[5,65], H=[[47,65]]**. Additional weak and primitive-zero counts are000.

The entire remaining physical basin is:

```text
peak5; elder65; death edge47--65
path [5,2,1,0,20,24,35,38,41,46,47,65]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,20,21,23,24,25,27,35,38,40,41,46,47]
cut [[2,57],[4,36],[5,59],[6,32],[7,64],[8,39],[9,45],[10,30],[11,31],[11,55],[12,19],[12,49],[14,63],[15,16],[15,29],[18,62],[21,61],[25,60],[27,42],[27,44],[40,48],[41,26],[46,51],[47,43],[47,65]]
```

There is no positive Qbar. P/Q forest depths are15/20. The selected positive true-edge cosine minima lie in `[1209524552,1209524553)/10^12` and `[1071457833,1071457834)/10^12`. The physical forest has two roots and is not a U1 certificate.

TP lies in `[822447828147,822447828148)/10^12`; minedge/R in `[3036170434,3036170435)/10^12`; inradius/R in `[236791770015,236791770016)/10^12`; volume/R³ is approximately.256601901083. Independently frozen G4/G5/G6 are all exact121.

Input991 bytes/SHA-256 `252e9c4811d4bf05bcc9d1eb152340810ae4682c10cf0819e76bbbcfd958cc3e`. Full report75642 bytes/SHA-256 `c88080e6d89ea91da096d413cc041be8838eabdc0083d2f53e1c526d81b683d8`.

### BA69REC_G5: complete mechanical and basin data

Actual uniform volume is approximately1.0010688112351225. Actual centroid is approximately

`(.00047891293891255254,.00004397357050187568,.00044496002545986213)`.

Strict features are **S=[1], U=[20,121], H=[[92,115]]**. Additional weak and primitive-zero counts are000.

```text
peak20; elder121; death edge92--115
path [20,28,33,37,43,38,42,46,48,70,71,76,85,86,87,89,92,115,121]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,20,28,33,37,38,42,43,46,48,70,71,76,78,85,86,87,89,92]
cut [[2,29],[3,72],[5,94],[6,56],[7,15],[7,59],[8,104],[9,55],[10,52],[11,18],[12,112],[13,17],[13,26],[14,116],[16,97],[20,83],[28,108],[33,106],[37,93],[42,101],[43,90],[46,100],[76,36],[78,100],[85,84],[86,84],[87,88],[89,88],[92,109],[92,115]]
```

Qbars are empty. P/Q forest depths are21/36. The selected true-edge cosine minima lie in `[1097434092,1097434093)/10^12` and `[954754447,954754448)/10^12`. TP lies in `[553693210872,553693210873)/10^12`; minedge/R in `[264229596,264229597)/10^12`; inradius/R in `[268750219553,268750219554)/10^12`; volume/R³ is approximately.28556701538. G5/G6 are both exact121.

Input2104 bytes/SHA-256 `0c0b888242cc7972f71db6c8fd36c20c2a5fb5029210a59a32878284c173405e`. Full report176232 bytes/SHA-256 `92f02c275e419f6c25e7a00feced785267023a276ad7cfad6dd80bbcdaddb558`.

### Other material nonwinners

**MONO14_G6** has only14 active supports and E36, but severe thinness and a deep physical basin. Its actual volume is approximately9.768293773989763, centroid `(.11493991120878072,.07767250621510847,.08618758969238559)`, S1, U0/23 and H11--23. Its Pbar0→23 has a12-vertex/14-edge basin and path `[0,9,11,23]`; Qbars are empty. G5 is222; G6/G7/G8 are121. The full literal14-row input and all audits are in the inline recovery.

**AXREC_G5/G6/G7** preserve a genuinely nonsimple common-apex architecture: V49/E76/F29/C152, strict211. The apex `(0,0,1)` is **eight-valent**, not nine-valent or12-valent. Eight of the12 nominated apex planes are active; the other48 vertices are trivalent. At G5, S0/5, U20 and H2--20; Pbars are empty, and Qbar5→0 dies22--24 with12 vertices/28 cut edges. Its normalized half support gap is approximately.13659, worse than H38.

**AM38REC_G5/G6/G7** are distinct exact211 bodies with72/108/38. At G6 the remaining Qbar3→1 dies31--33, with16 vertices/38 cut edges; Pbars are empty. Its normalized half support gap is bounded by `84643264233/995750220760` and `84643264234/995750220759`, approximately.0850045 versus H38's.0950967. This is a limited same-complexity improvement, not cancellation.

**VR20_G5** and **VC35_G5** are distinct physical V-hull arithmetic companions, both strict121 with71-bit common centred denominators. VR20 has36/102/68 and VC35 has66/192/128. Loss of exact parent coplanarity creates genuine extra edges; it is not a harmless coordinate simplification. Their complete own masses and P/Q basins are regenerated.

**VC46P1_G6** is a material exact413 body with48/138/92; **VC46P2_G5/G6/G7** are exact211 bodies with the same counts. VC46P2_G5 is a thicker uniqueU reserve: inradius/R≈.300475167 and volume/R³≈.61272415, but its normalized full stable support gap≈.46227 is worse than H38. This was an explicit switch to a free-physical-vertex contact chart, not a relabelling of the lead's V20 route.

The eight coarse controls are Q121_G4=222, C16R_G4=222, MONO14_G5=222, C6REF_G4=323, VR20_G3=525, VR20_G4=222, VC35_G3=(13,4,15), and VC35_G4=233. All have complete exact maximal geometry and mechanics; all are additionalweak000/primitivezero000. Fine-grid classes are never transferred to coarser grids.

## 4. Executed nonlinear methods and the remaining mass obstacle

The direct H38 quota flow moved all support normals while recomputing the actual filled hull and centroid. It targeted dynamic P2/Q1, not fixed roots or a fixed positive escape tree. It obtained exact Q121_G5/G6/G7. The independent R155 route used a common-apex chart, whole polar-interface replacement and actual-centroid consolidation. These demonstrate actual stable cancellation, not merely a reference-root change.

A subsequent whole-H resource objective used the current dominant physical peak u and elder z:

`F_n = log(|z|/|u|) + n*log(cos(angle(u,z)/n))`.

It targeted F_n≥.005, allowing support contacts, root exchanges and temporary extra equilibria, while recomputing actual mass and penalizing loss of thickness. This changed the parent geometry rather than repeating the old94-link bridge. C16R/C12R, followed by support enrichment, led to C8REF, C6REF and C5REF.

Four exact rational **reference** chains are retained:12 links for C12R_G4,8 for C8REF_G4,6 for C6REF_G5 and5 for C5REF_G5. Every chain arrow is checked by exact strict `p·(next−p)>0`, and complete rational interior points are embedded. **These do not certify the newly filled enlarged hull at its new actual centroid.** The chain reports explicitly contain `claimed_new_hull_own110:false`.

C6REF's adopted source is its feasible checkpoint, not its near-edge-collapsed END. REF69 was formed from that binary64 feasible checkpoint, not silently from G5. C5REF_G5 has one58-vertex/48-edge physical basin, no Qbar, and only a very small minimum true edge/R≈.000016308774. Its better reference-chain resource does not solve mass closure.

The complete-basin runs leading to the primary frontiers allowed additional roots. BF35 ran1800 iterations/3116 objective-gradient evaluations and ended numerically S1/U15; BF35REC performed40/154 and consolidated to the exact121 grids. BA69 ran1800/3663 and ended S1/U7; BA69REC performed28/31 and consolidated to121. C5REF performed720/1131. These are completed counts, not requested budgets or stationarity claims. Consolidation increased persistence from the many-U endpoints; no smaller positive bars are suppressed in the reported exact endpoints.

### Surface metric with actual moment constraints

For a physical facet q·x=1, a normal change δq gives boundary-normal velocity `−x·δq/|q|`. Define the facet metric

`G_F = ∫_F xx^T dA / |q|²`.

The actual mass derivatives are

`dV/dq = −∫_F x dA / |q|`,

`dc/dq = (−∫_F xx^T dA + c(∫_F x dA)^T)/(|q|V)`.

For a triangle with vertices a,b,d, its second moment is

`area*((a+b+d)(a+b+d)^T + aa^T + bb^T + dd^T)/12`.

The new implementation projects the inverse-metric gradient onto four first-order volume/centroid constraints. Every finite trial then reconstructs the actual H hull and mass. Optional projective normalization changes the geometry of a uniformly filled body; it does not assign artificial density weights.

Three derivative checks, on H38,ROB12 and C6REF, agreed with independently differentiated tetrahedral-mass Jacobians to relative error≤4.103e-15. Rank was4; projected neutrality residuals were≤8.932e-18, with negative directional slopes. These are numerical derivative checks, not exact equilibrium certificates.

SM38,SA38 and SM12 each completed800 accepted steps, respectively11359,11338 and11166 evaluations, with no caught geometry exception. They stopped at iteration limits and did not supply an own110 certificate.

The full research ledger contains65 optimizer invocations and12 finite scouting campaigns. Their failures are not family exclusions. The inline capsule below closes eight principal invocations completely—BF35,BF35REC,BA69,BA69REC,C5REF,SM38,SA38,SM12—with runnable source, actual initial data and all parsed settings. The complete historical ledger and remaining producer/restart provenance are also preserved in the supplementary full handoff; their scope limitation is stated explicitly below.

## 5. New two-terminal radius/complexity obstruction

### Statement

Let a uniformly filled full-dimensional convex polyhedron L have unique strictU and no additionalweakU at its actual centroid g. Suppose L retains two specified points u,z, not necessarily as vertices. Write

`A=|u−g|²`, `B=|z−g|²`, `D=|u−z|²`, `R=max_{x in L}|x−g|`.

If L has V vertices, then

**`D ≤ (V+1)*(2R²−A−B)`**.

For E≤310, every vertex has degree≥3, so V≤206. Hence a necessary condition is

**`R² ≥ (A+B+D/207)/2`**.

Writing m=(u+z)/2 gives the equivalent actual-centroid condition

`R² ≥ |m−g|² + D/4 + D/414`.

This permits root turnover and every witness/incidence change. It does not make g freely selectable.

### Proof

Centre at g. Every nonroot true vertex p has a positive true-edge escape p→q; otherwise p lies in a strict or weak unstable normal cone. Selecting one at each nonroot produces an acyclic directed tree to the uniqueU root because squared radius strictly increases. Every such edge satisfies

`|q−p|² < |q|²−|p|²`.

For a retained nonvertex u, express u as a convex combination of true vertices. The weighted mean of `u·(v−u)` is zero, so some true vertex v gives a nonnegative attachment arrow. Its squared length is at most `|v|²−|u|²`. Do the same for z. Follow the two tree paths until they first meet. The two true-edge branches together have at most V−1 edges, with at most two attachment chords. Their total squared length telescopes to at most `2R²−A−B`. Triangle inequality and Cauchy–Schwarz on this at-most-V+1-segment path yield the result.

### Exact scoped consequences

At each named parent's own centre, require that the target retain its two U points and not increase its centred circumradius beyond the larger parent-root radius. Then `D/(B−A)≤207` is necessary. Exact calculations give:

| Source | D/(B−A), approximately | Necessary V in this envelope | Necessary E |
|---|---:|---:|---:|
| Q121_G6 |3598.358811768|3598|5397|
| R155_G4 |833.532402912|833|1250|
| MONO14_G6 |318.183028950|318|477|

These three specified envelopes therefore cannot contain an E≤310/uniqueU endpoint. The integer comparisons and rational quantities are regenerated by `child_metrics.py`; floating comparisons are not the proof.

C16/C12/C8/C6/C5 have corresponding ratios approximately7.188,5.527,4.049,3.154,2.684, so this particular gate does not exclude them. They nevertheless remain own121. Moving the actual centroid, enlarging the circumradius envelope, discarding the retained pair or changing architecture can evade the earlier obstructions. No global lower bound or minimal-link theorem is claimed.

## 6. Exact verification and replay status

All52 grids have full actual-centroid strict S/U/mixed-H, additionalweak and primitive-zero censuses. The H auditor exhausts supporting-plane triples, checks boundedness, reconstructs true maximal facets and edges, and checks containment, Euler, two-face ownership and vertex links. Mass is checked by origin tetrahedra, coordinate-boundary divergence and positive own-centred tetrahedra. Integration diagonals are not true edges.

Nine selected H solids also have matching independently constructed V hulls and complete mechanics, plus separate positive vertex-anchor mass integration: R155_G4_ACTIVE,Q121_G6_ACTIVE,AXREC_G5_ACTIVE,MONO14_G6,C16R_G6,C12R_G6,C8REF_G5,C6REF_G5,BF35REC_G4. This is not a two-independent-mechanics claim for all52.

The exact landscape emits every positive P/Qbar, exact birth/death levels, attaining paths, complete strict-upper components and full cuts. It uses no objective epsilon to erase a basin. Empty exact bar lists and exact zero sums establish zero; an enclosure `[0,1)/10^12` alone does not.

Tetra446/weak000, prism446/additionalweak123 and unbounded-H rejection controls executed. The inherited complete-chord method was tested with true-edge maximum spanning trees, complete cuts, redundant points and tiny uniformly scaled bodies; it is reused, not claimed as a second discovery.

The full65-unit source pack was cold-replayed:52 bodies, nine independent checks, all52 complete metrics, four reference chains, and **108 matching input/report receipts**. The108 receipts were checked again during delivery, with zero mismatches. The13 exact-auditor/input/metric units in the inline reduced capsule are byte-identical to the successful cold-replay sources.

The reduced32-unit capsule itself was decoded and its52 inputs checked. Eight of its full body reports were regenerated and matched before the shell-limited repeated run was stopped. **A second complete52-body cold run of this reduced packaging is not claimed.** Its exact core and expected outputs are unchanged from the completed full-pack replay.

Important receipts:

```text
CHILD_METRICS.json:2473627 bytes
34c7da11a97ad6edfaf431867d4a0386d5e1ee142740b46eb78ee8b1f1d1934c
CHAIN_POINTS.json:1242 bytes
721d36172ca575fd882981d4ba17108b480faf2899d0e00908e9a93338ab9002
CHAIN_CERTIFICATES.json:75115 bytes
15a7d8f7bdca5325f436759fa4b0003e3d756d22671cded7d41716b80b220413
INDEPENDENT_NINE.json:2672 bytes
fbdf1b2ee1475b3565622ae5289d191af40e91cd28ee3f3e9cc62ec7f2dd4cc6
```

## 7. Continuation and recovery scope

The compact-H route now has actual S1. The unresolved problem is **cancelling the physical basin without recreating a stable basin**, rather than continuing to repair the unchanged two-S interface. BF35REC_G4 retains the strongest small-support/thickness tradeoff here. BA69REC_G5 reduces the whole Pbar further but has a much smaller minimum edge. C5REF_G5 offers a shorter reference chain, not actual-mass closure. These are different resources, not a single ranking by closeness.

A continuation can remove inactive inequalities and change the whole physical-root/interface region while redistributing actual material and allowing root exchanges. The radius gate rules out spending the complexity budget on a nearly equal-radius retained pair inside the wrong circumradius envelope. Neither a reference chain nor moment neutrality to first order solves the finite filled-mass problem.

**Inline recovery scope:** the following32-unit capsule is self-contained for all52 exact solids, both hull/mechanics implementations, complete masses/forests/PQ basins, all conditioning/radius gates, four rational reference chains and108 expected output receipts. It also contains complete runnable producers, exact initial data and all nondefault parameters for the eight principal finite invocations listed above. No exact endpoint requires an external parent, sandbox or floating-point restart.

The other57 historical numerical invocations and the12 scouting campaigns are not fully replayable from this reduced inline capsule alone. Their complete65-unit source/restart pack is preserved in the linked full handoff and standalone full decoder. This is a provenance limitation of the reduced inline delivery, not an ephemeral-exact-object claim: every one of the52 exact successors is reconstructed and audited by the inline source.

Exact replay uses CPython3.13.5 standard library. Numerical production used NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, float64, one BLAS/OMP/MKL/Torch thread. Cross-platform optimizer-trajectory identity is not promised.

Save the following complete unit as `RECOVER_NWC_FRONTIER.py` and run:

```text
python -B -S RECOVER_NWC_FRONTIER.py NWC_FRONTIER
cd NWC_FRONTIER
python -B -S REPLAY_CHILD.py bodies --jobs 4
python -B -S REPLAY_CHILD.py independent --jobs 3
python -B -S REPLAY_CHILD.py metrics
python -B -S REPLAY_CHILD.py collect
```

Expected terminal markers include `NWC_PORTABLE_SOURCE_RECOVERY_PASS 32`, `NWC_PORTABLE_EXACT_INPUTS_AND_SELECTED_PHASE_PINS_RESTORED 52 2`, `NWC_52_SOURCE_ONLY_EXACT_BODIES_MATCH_PASS 52`, `NWC_NINE_INDEPENDENT_H_V_HULL_MECHANICS_MASS_PASS 9`, `NWC_EXACT_OWN_CENTER_FORESTS_FULL_BASINS_CONDITION_GATES_PASS 52`, `NWC_EXACT_REFERENCE_ESCAPE_CHAINS_NOT_OWN_CERTIFICATES_PASS 4`, and `NWC_COMPLETE_COLD_RECOVERY_ALL_RECEIPTS_PASS 108`.

Optional closed numerical replay: `python RUN_NUMERICAL.py --list`, then, for example, `python RUN_NUMERICAL.py --phase BF35REC --work NEW_EMPTY_DIRECTORY`. Every parsed parameter is restored from PRODUCTION.json; upstream floating outputs are not silently substituted.

Portable dictionary156800 bytes/SHA-256 `2ab044fb2306d7ffe31d58a05e5458e2b6b06c593ccfd255d828d9831be708db`; XZ47316 bytes/SHA-256 `45b634630ba18cf489f4dd1487eb60d42feee425cc5cad8009b7b1aea99558b0`; normalized Base64 length63088. Standalone portable decoder64921 bytes/SHA-256 `4ae558207d092fb8eea680ca3a73e4ff3160fc197b4a021e327bca8de12de0c8`.


[Encoded source block omitted; the code in this passage is incomplete.]


## Supplementary complete archive

The larger archive preserves the complete65-unit historical numerical provenance in addition to the exact recovery above. Its dictionary is393632 bytes/SHA-256 `a45b24c6ab9251c4ac65b1d0c15a5208ff2d0130c7e8c05128e28c0d7cad8d40`; standalone full decoder170577 bytes/SHA-256 `19e96567c00043c109c51fec794e192144a6c84adbaba5f3c77b1d84f47a61c7`.

[Portable standalone decoder](sandbox:/mnt/data/RECOVER_NWC_FRONTIER.py) · [Full65-unit recovery decoder](sandbox:/mnt/data/RECOVER_NWC_H.py) · [Full scientific and provenance handoff](sandbox:/mnt/data/NWC_HANDOFF.md) · [Full JSON handoff](sandbox:/mnt/data/NWC_HANDOFF.json) · [Complete evidence archive](sandbox:/mnt/data/NWC_EVIDENCE.zip).

The exact successors are supplied by the inline capsule; these files supplement rather than define their recovery.
