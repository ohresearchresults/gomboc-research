# figure-0462

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Sharp Raven 30 — exact NW37 whole-physical-basin continuation

## Status

No strict110 endpoint was found. The strongest exact continuation is a new `MONO85` own121 descendant with a genuinely smaller complete physical dying packet, followed by a complementary one-cap exact checkpoint with a lower global P depth but a slightly larger packet. A low-edge `MONO47` descendant also lowers TP substantially but *expands* its packet. These three exact bodies make the main lesson sharp: decreasing TP alone is not whole-basin cancellation; packet/interface size has to be an explicit acceptance criterion.

The preferred new continuation parent is **`NW37_R30_MONO85_DESCENT_G6`**. It has **V166/E249/F85, C498, strict121, additional-weak000, primitive-zero000, Q positive bars empty**, so it keeps 61 true-edge units of headroom below E310. Relative to immutable parent `NW37_MONO85_QUARTER_G6`, its complete physical basin contracts **41 vertices / 33 cut edges -> 36 / 32**, while TP falls from about 0.295235277655 to the exact 1e-12 bracket **[290736815983,290736815984]/1e12**. This is a finite whole-packet contraction, not merely a local witness improvement.

Authoritative immutable parent: `figure-0447`, SHA-256 `efbc9084f0bedab80a14b39769917edcf445ab6af765170cb4e101f77ad12022`. I found no conflict between the literal parent and the journal summary.

## Source reading and execution closure

I read the complete supplied `research-journal.md` through EOF, including the full literal parent payload. I then reconstructed the parent's embedded 41-unit source dictionary and read every recovered source/data unit completely through EOF before research. Parent reconstruction marker:

`NW37_CONTINUATION_SOURCE_CAPSULE_PASS 41 939ee82786c952c9abebbb2f8df72c02a2c9c862cf7a5948cd69116f3be2cb1c`

The new primary endpoint was also cold-replayed from a fresh parent extraction plus the new recovery capsule. Exact cold markers were:

```text
NW37_GMP_FRACTION_ARITHMETIC_CONTROLS_PASS 6.3.0
TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS
HULL_EXACT 166 249 85
POSITIVE_CENTERED_TETS_AND_ZERO_MOMENTS_PASS
BOUNDARY_MASS_PASS
MASS_MECH_EXACT [1, 2, 1] [0, 0, 0]
INDEPENDENT_MECHANICS_PASS
LANDSCAPES_PASS
FULL_PQ_BASINS_EXACT 1 0
NW37_EXACT_H_DOUBLE_MECHANICS_PASS NW37_R30_MONO85_DESCENT_G6_EXACT.json 166 249 85 [1, 2, 1] {'bytes': 27668137, 'sha256': 'cabb535d9d97b56f0cfdc0ac26a640d96c51ae99a9f9b85161f8b957cb84c749'}
NW37_DIRECTIONAL_MOMENT_WITNESSES_PASS 164 84 True NW37_R30_MONO85_DESCENT_G6_EXACT_CHAMBERS.json {'bytes': 2545862, 'sha256': '6aab724fa7bcb87bbfce2aca5642d8c26f9883fc95866607eacc27bd20685119'}
```

The full H audit uses exact triple intersections, maximal polygon reconstruction, true edges, exact filled volume/first moment, strict and additional-weak S/U/mixed-H predicates, same-physical-centre polarity, exact elder landscapes, and a second AREA_RADIUS mechanics/mass implementation. As in the parent, the two mechanics implementations share the exhaustive hull enumerator; this is not claimed as two independent hull enumerators.

## Exact lead: `NW37_R30_MONO85_DESCENT_G6`

**Combinatorics and class**

- V/E/F = **166/249/85**, C=498; all 166 vertices trivalent.
- Face histogram: 10 triangles, 17 quads, 26 pentagons, 14 hexagons, 3 heptagons, 9 octagons, and one each 9-,10-,12-,13-,20-,29-gon.
- Strict equilibria: S face **36**, U vertices **3,162**, H edge **21-23**.
- Unique stable maximal-face cycle: **[1,113,130,134,2]**.
- Additional weak census = **000**; primitive mechanical zero counts = **000**.
- Same-physical-centre polar has unique root **36** and **no positive Q bars exactly**.
- Physical roots are **3,162** and there is exactly one positive P bar.

**Exact mass and incidence.** The exact uniform filled volume, first moment, actual centroid, all 85 maximal face cycles, all 249 true edges, the exact strict/weak/zero census, and the complete integer halfspace input are literal fields in `R30_ENDPOINT_CERTS.json` inside the embedded recovery capsule below. They are thousands of decimal digits, so I do not duplicate those rational strings outside the capsule. They are part of this `result_markdown`, not an external file dependency. For orientation only, the exact values evaluate to:

```text
Vol ~= 1.3591746904334312
c ~= (0.016037054284307312, -0.03712487291500429, -0.008415423857063214)
centered common-denominator bits = 16494
```

**Exact/global metric brackets**

```text
TP                         in [290736815983,290736815984]/1e12
minimum positive P arrow   in [3902948,3902949]/1e12
minimum true edge / R      in [773215560,773215561]/1e12
inradius / R               in [382656898278,382656898279]/1e12
Vol / R^3                  in [699297376108,699297376109]/1e12
minimum positive Q arrow cosine ~= 7.5199959467e-5
```

The minimum true-edge/R is about **4.85x** the immutable MONO85_G6 value, while the selected positive P-forest reserve is smaller than the parent's; this is therefore an interface/edge-conditioning gain, not a uniform witness-margin gain.

**Complete surviving physical positive basin certificate**

```json
{"peak":162,"older":3,"death_edge":[21,23],"component":[23,24,25,29,30,34,50,56,58,59,62,64,67,71,82,97,117,129,130,134,138,139,142,150,154,155,156,157,158,159,160,161,162,163,164,165],"boundary":[[134,2],[139,3],[156,4],[159,5],[23,21],[23,84],[24,28],[25,27],[29,27],[30,92],[34,73],[50,72],[155,53],[157,53],[56,91],[71,57],[58,107],[59,60],[62,60],[64,109],[67,114],[117,70],[82,116],[97,131],[130,113],[150,128],[142,131],[165,137],[150,144],[154,151],[155,152],[154,153]],"path":[162,138,129,117,97,82,71,67,64,62,59,58,56,50,34,30,29,25,24,23,21,19,11,9,0,1,2,3]}
```

Every cut edge has level at most the exact death level and the attaining path has minimum level exactly the death level, checked over the complete true-edge set by the exact landscape auditor. Compared with the immutable MONO85_G6 component, eleven old carriers disappear (`26,27,28,33,49,55,81,140,151,152,153`) and six new carriers enter (`23,34,50,56,82,142`), giving the net 41->36 contraction. The death interface turns from old edge 21-24 to **21-23** and the stable cycle changes at the 114/113 carrier. The TP reduction is about **1.5237%**, but the more important gain is the strict-upper packet contraction.

**Receipts**

```text
NW37_R30_MONO85_DESCENT_G6.json
2887 bytes; SHA256 d61f4b02c5541ddbe61a7fc4bce7660628d807295e489a8ed97d10e9dfbeb755

NW37_R30_MONO85_DESCENT_G6_EXACT.json
27668137 bytes; SHA256 cabb535d9d97b56f0cfdc0ac26a640d96c51ae99a9f9b85161f8b957cb84c749

NW37_R30_MONO85_DESCENT_G6_EXACT_CHAMBERS.json
2545862 bytes; SHA256 6aab724fa7bcb87bbfce2aca5642d8c26f9883fc95866607eacc27bd20685119
```

The chamber checker verifies all **164 physical** and **84 polar** selected positive arrows by both the direct centered-vector Fraction expression and the homogeneous `(Vol,M)` numerator identity; the polar is always formed at this body's actual physical centroid.

## Complementary exact checkpoint: `NW37_R30_CAP1_G6`

A targeted finite cap scout on the new MONO85 descent produced a second exact own121 body. Numerically the proposal is one extra active physical cap after translating the seed to its own centre; exact G6 freezing rounds all normalized rows independently, so the exact object is defined by the complete 86-row integer input in the capsule, not by pretending only one literal parent row changed.

- V/E/F = **168/252/86**, C504; all 168 vertices trivalent; 58-edge headroom.
- Strict S/U/H = **1/2/1**; weak000; primitive-zero000.
- S face40 cycle **[1,113,130,134,2]**, U **3,162**, H **21-23**.
- Q root40; Q positive bars empty exactly.
- TP in **[272412111927,272412111928]/1e12**: about **7.7305%** below immutable MONO85_G6 and **6.3028%** below the new descent seed.
- P minimum selected positive arrow cosine ~=1.4238663e-5; minedge/R ~=0.000741124594; inradius/R ~=0.382668713373; Vol/R^3 ~=0.699313568051.
- Complete surviving packet is **38 vertices / 32 cut edges**. Thus the cap lowers radial depth materially and is still a net contraction relative to the immutable 41/33 parent, but it *expands* the new descent packet from 36 to 38. This is useful exact evidence that scalar bar reduction and packet contraction are different objectives.

Its complete packet is:

```json
{"peak":162,"older":3,"death_edge":[21,23],"component":[23,24,25,29,30,34,50,56,58,59,62,64,67,71,82,97,117,129,130,134,138,139,142,150,154,155,156,157,158,159,160,161,162,163,164,165,166,167],"boundary":[[134,2],[139,3],[156,4],[159,5],[23,21],[23,84],[24,28],[25,27],[29,27],[30,92],[34,73],[50,72],[155,53],[157,53],[56,91],[71,57],[58,107],[59,60],[62,60],[64,109],[67,114],[117,70],[82,116],[97,131],[130,113],[150,128],[142,131],[167,137],[150,144],[154,151],[155,152],[154,153]],"path":[162,138,129,117,97,82,71,67,64,62,59,58,56,50,34,30,29,25,24,23,21,19,11,9,0,1,2,3]}
```

Receipts:

```text
NW37_R30_CAP1_G6.json 2915 bytes SHA256 6da33d1f534df473c7577dd61468ecfc50fb380893a989ad35bca111c546edc5
NW37_R30_CAP1_G6_EXACT.json 28480594 bytes SHA256 644fa9666e1b15f28cfd6e9313d518104f4f4277afa0dfb808a01f4702ed1f26
NW37_R30_CAP1_G6_EXACT_CHAMBERS.json 2620759 bytes SHA256 9aef504a21609888b68fdbdeac26edafc2538d655ef1370dcc926db844b75c01
```

## Complementary low-edge exact checkpoint: `NW37_R30_MONO47_DESCENT_G6`

A whole-support continuation from the low-edge MONO47 entrance gives another exact own121 body:

- V/E/F = **90/135/47**, C270; all 90 vertices trivalent; **175** edge units of headroom.
- strict S/U/H = **1/2/1**, weak000, primitive-zero000.
- S face23 cycle **[0,3,65,71,74,1]**, U **1,85**, H **20-21**; Q root23 and no positive Q bars.
- TP in **[497366779216,497366779217]/1e12**, about **11.1713%** below immutable MONO47_G6's ~0.559916987898.
- Complete P packet = **44/34**, versus the immutable MONO47 42/32. Thus this substantial TP gain makes the whole packet *larger* and should not be treated as progress toward cancellation without an explicit interface term.

Complete packet:

```json
{"peak":85,"older":1,"death_edge":[20,21],"component":[21,24,27,31,32,33,35,38,42,49,51,55,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89],"boundary":[[74,1],[83,2],[65,3],[79,4],[76,5],[75,6],[77,7],[80,8],[70,10],[66,11],[62,12],[64,14],[60,16],[63,16],[35,18],[51,18],[57,19],[21,20],[21,25],[55,22],[24,25],[27,45],[49,28],[31,34],[32,50],[33,52],[72,37],[78,37],[38,54],[42,56],[49,47],[67,56],[58,59],[69,59]],"path":[85,86,68,61,51,42,38,35,33,32,31,27,24,21,20,17,13,0,1]}
```

Receipts:

```text
NW37_R30_MONO47_DESCENT_G6.json 1586 bytes SHA256 6a77fbc244b23fcb7623f85727b9df333adb12d3d8174fd24c404cf008dcfb84
NW37_R30_MONO47_DESCENT_G6_EXACT.json 8541231 bytes SHA256 31c3fea6704e2cac9e0f48417b9146d1ac2f2a05cf5a37d54a3d8798cd88fe22
```

## Executed finite campaigns and what they do / do not say

1. **Whole-support descent.** From immutable MONO85_G6, an 800/1872 full-P stage retained numerical S1/U2 and reduced TP to ~0.292081. A second stronger full-P stage was interrupted by the outer execution after callback 992 / nfev1807; its last S1/U2 callback froze to the exact lead above. The exact integer endpoint is durable and does not depend on the interrupted numerical file. The same mechanism on MONO47 produced the exact C270 checkpoint above. These runs demonstrate a real finite interface move, not convergence or local optimality.

2. **Targeted multi-cap scout.** On the new MONO85 descent, seed30031 was requested for 20000 one-to-four-cap proposals; the outer execution ended after the printed 3000-case checkpoint. No numerical S1/U1 occurred in that completed prefix. The exact CAP1 body came from the best retained S1/U2 proposal near case952. This is finite evidence only; no cap-family exclusion follows.

3. **Fixed-geometry SPD metric scout.** A new source-complete scout sampled **500000** SPD Gram metrics on the exact MONO85 descent, cycling log-eigenvalue scales 0.25,0.75,1.5,3,5 with seed30033. It found no S1/U1; the best root-count merit remained two extra total roots. This is not an affine theorem, connected-component certificate, or exclusion of high-condition / unsampled cells.

4. **Existing projective-affine source on the new seed.** `projective_scout.py` completed 50000 proposals, seed30032: no U1 sample and only two S1 samples; the best S1 sample was S1/U13 with Qbars empty. Again, finite only.

5. **Dropping the physical witness guard is counterproductive.** From the new MONO85 descent, a 700/1307 full-P run with `ppen=0` kept S1 and Qbars empty while lowering numerical TP to ~0.268306, but exploded to U23 / 22 positive P bars. A pallow1 restoration then failed immediately (2 accepted /120 evaluations, S3/U23 terminal with new Q bars). This is direct evidence on the executed path that smooth TP descent can fragment the packet before annihilation.

6. **Fresh physical logarithmic bridge scout on the new exact seed.** The updated peak/elder geometry requires minimum short/long link counts 12/30. A 12-link short bridge numerically drove TP to ~0.0950 but produced S15/U30 and TQ~3.879 at E270. A 17-short +30-long bridge stayed under E310 at E306 and drove TP to ~0.02850, but produced S16/U38 and TQ~4.143. These are useful finite whole-packet perturbations, not endpoints: bridge insertion can nearly destroy the old radial bar while spawning many physical and polar equilibria. The immediate free-point restoration attempt did not reconsolidate and also entered an over-budget triangulated regime, so no exact successor is promoted from it.

None of these bounded failures is an exclusion theorem.

## Scientific interpretation and next continuation

The best entrance for the next executor is **`NW37_R30_MONO85_DESCENT_G6`**, not the lowest-TP CAP1 and not the low-edge MONO47 descendant. It is the one exact endpoint that improves the objective the assignment actually asks for: the entire remaining P packet contracts from 41/33 to 36/32 while S1 and Qbars-empty survive at the actual uniform centroid. CAP1 is the complementary lower-depth checkpoint; MONO49_G3 remains the much higher witness-reserve alternative if a larger nonlinear move needs margin.

The next move should explicitly span the **21-23 death interface and several boundary carriers at once**. In particular the new cut begins with `[23,21],[23,84],[24,28],[25,27],[29,27],[30,92]`; an acceptance rule should score the complete strict-upper component/cut after every actual-mass rebuild, not merely TP or a chosen escape witness. The exact descent already removed eleven old basin carriers and admitted six replacements, so root/interface turnover is occurring and should be exploited rather than suppressed.

A useful finite program is: (a) propose a coordinated 2-6 support replacement/motion acting on several cut carriers; (b) rebuild the full H hull and filled `(Vol,M)` each trial; (c) protect a selected Q rootward chamber with the exact homogeneous moment inequalities, but permit temporary P/H births; (d) accept only if the complete P component/cut shrinks or a genuine interface event occurs; (e) reconsolidate afterward with support replacement/pruning; (f) independently freeze promising checkpoints at adjacent grids and exact-audit. Do not use a pure TP gradient as the principal merit function: both CAP1 and MONO47_DESCENT prove exactly that it can improve while the packet expands.

The 164 physical /84 polar directional-moment identities of the lead are exact finite sign guards, but their coefficients must be recomputed after geometry/support changes. Same-centre polarity and actual uniform mass remain mandatory. No density freedom is introduced.

## Self-contained new recovery capsule

The complete literal recovery capsule is the following Python source. It contains the three exact new inputs, exact primary mass/centroid and complete maximal-face/true-edge incidence certificate, all three exact basin/census receipts, numerical recipes, and both newly written producer/scout sources. It has been decoded in a fresh directory and the lead endpoint was cold-replayed against a freshly recovered immutable parent.

Decoder source receipt: **51386 bytes**, SHA-256 `119688ff9da520b798919485f5417b679b252491bd47029a034bd01de9f1c835`. Compressed payload: **38072 bytes**, SHA-256 `a438fcaabcb71e058cba8fadc1378eec1a87c05c55712e747133544b18d20fe0`. Decompressed seven-unit dictionary: **89518 bytes**, SHA-256 `f837f39c500218d9c965701d5438dadd5bea8564fd698c4c7013ba980a54ae34`.

Recovery after reconstructing the immutable parent's embedded 41-source pack:

```text
python -B -S RECOVER_R30_HANDOFF.py R30_HANDOFF
cp R30_HANDOFF/NW37_R30_*_G6.json PARENT_RECOVERY_DIR/
cd PARENT_RECOVERY_DIR
python -B -S [internal-source-reference].py NW37_R30_MONO85_DESCENT_G6.json NW37_R30_MONO47_DESCENT_G6.json NW37_R30_CAP1_G6.json
python -B -S CHECK_WITNESS_CHAMBERS.py --gmp --direct NW37_R30_MONO85_DESCENT_G6_EXACT.json NW37_R30_CAP1_G6_EXACT.json
```

The capsule's observed extraction marker is:

`R30_HANDOFF_CAPSULE_PASS 7 89518 f837f39c500218d9c965701d5438dadd5bea8564fd698c4c7013ba980a54ae34`

Its seven recovered units are exactly `NW37_R30_MONO85_DESCENT_G6.json`, `NW37_R30_MONO47_DESCENT_G6.json`, `NW37_R30_CAP1_G6.json`, `R30_ENDPOINT_CERTS.json`, `R30_NUMERIC_RECIPES.md`, `r30_cap_target.py`, and `r30_metric_scout.py`.

No new C<622 strict110 body is claimed. The canonical accepted strict110/weak000 C622 record is unchanged.
