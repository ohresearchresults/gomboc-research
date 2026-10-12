# figure-0548

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Mixed H-core/apex continuation: detached stability, exact high-contact bodies, and the remaining P defect

## Outcome

**No strict own110 body was obtained.** The useful new construction is a mixed physical body
\[
K(q,a_1,\ldots,a_k)=\operatorname{conv}\bigl(\{x:q_i\cdot x\le1\},a_1,\ldots,a_k\bigr),
\]
with freely changing core supports and exterior apices, actual homogeneous mass integration, and exact preservation of the resulting facet concurrences.

The simplest useful principal endpoint is **HINGE_WIDE_REC_G6**: **V125/E240/F117, C480, strict own121, additional weak000, primitive zero000, P1/Q0**. Its sole P relative depth is approximately **0.21842561646101927**, versus **0.395680550242498** for CN64_G6: a **44.7975% reduction**, still macroscopic. Its actual vertex numerators and denominators require at most60 and61 bits, respectively. It has nine edges of headroom to E249.

The slightly shallower **PHYSICAL_METRIC_G7**, with the same125/240/117 complex counts and own121 census, has P depth **0.21838242670673963**. This is only a small additional improvement, not a separate cancellation mechanism or a global record claim. Two roomier alternatives are retained: **TWO_APEX_G6**,121/229/110, C458, own121, depth **0.23170513339400295**,20 spare edges; and **MIXED_LONG_G7**,120/196/78, C392, own121, depth **0.32250253325599587**,53 spare edges.

All four have a **triangular stable facet avoiding both unstable vertices**. In the principal body all three inserted physical apices are non-U; the two U are changed core vertices. Both old CN64_G6 unstable material positions lie strictly outside the new body. Thus this continuation genuinely replaces the old attached stable carrier and root geometry; it does not merely rename a surviving old junior vertex.

A second substantive result is an **exact finite-interval theorem**: a specified physical pyramid insertion over CN64_G6's stable heptagon detaches the stable carrier while retaining own121/no-weak throughout an entire nonzero interval, and strictly decreases the complete sole P bar throughout that interval. This initial improvement is small, but the theorem establishes an actual homogeneous geometric mechanism, not a free-reference construction or an unexecuted derivative argument.

The continuation produced **23 fully audited rational bodies**,22 satisfying E≤249. Every one has additional weak000 and primitive zero000. All **28 positive P records and5 positive Q records** across these bodies are preserved. Deliberately releasing the S1 guard produced an instructive opposite-landscape transfer: P≈0.01619 but Q≈0.53169, class222—not near110.

## Reading and source authority

The entire newly supplied1213-line,308813-byte journal was read through EOF, including its literal required parent. The journal SHA-256 is `e4e59658f1f499e9fe2d519b82f56290e0a54aa6fb93db2d942ac57ecebc012e`. The controlling parent is `figure-0546`, delivered with immutable identity `6e33955763950defbd9a3d503706547d3a0ec6f361a18f15d468b1997953c59e`. Its exact CN64_G6 entrance, not a similarly named historical object, is V124/E186/F64, own121, P1/Q0. :contentReference[oaicite:0]{index=0}

The unchanged earlier W51 and CN recovery sources were retained from their completed readings in this chat. No required dependency is missing. The original58-direction W51 own-S1 exclusion was accepted as given; no generic re-audit was performed. The coordinator's independent82-height union was not used as the construction family. The prior three-cut theorem was respected in its actual scope; complete packet removal was not repeated as the proposed cancellation mechanism. :contentReference[oaicite:1]{index=1}

The included literal parent input is2173 bytes, SHA-256 `b8b1a9a4ca0d2626185a91e5844dc707b8456259f7f69cb43a77af7a79c31ec0`. All new exact definitions below are independently recoverable from the complete inline source; none requires an originating sandbox, an archive service, or numerical optimizer execution.

## 1. A finite physical mechanism: detach the stable carrier without creating another equilibrium

Let the parent stable support, input row14, be \(n\cdot x\le h\). Define
\[
a_1=\frac{(-291734,-593428,159292)}{10^6},\qquad
b=a_1-\frac{n\cdot a_1-h}{n\cdot n}\,n,
\]
and
\[
a(t)=b+t(a_1-b),\qquad K_t=\operatorname{conv}(K_{\rm CN64},a(t)).
\]

**Executed exact theorem.** For every **\(0<t\le1\)**, the actual uniformly filled \(K_t\) has
\[
(V,E,F)=(125,193,70),\quad(S,U,H)=(1,2,1),
\]
with additional weak000 and primitive zero000. Its unique stable facet is a triangle which **avoids both U**. Its sole complete P relative depth is **strictly decreasing throughout the interval**; Q has no positive finite bar.

The proof checks exactly that \(b\) lies in the relative interior of the old stable heptagon, \(a_1\) lies beyond that support, and both points strictly satisfy all other old supports. This proves the complete physical hull chart on the interval: all old vertices remain, one apex is added, the old heptagon is replaced by seven triangles, and no other old maximal facet is lost.

With \(W=6\operatorname{Vol}\) and \(T=24\int x\,dx\), the exact boundary calculation gives **degree1 \(W(t)\)** and **degree2 \(T(t)\)**; the actual centroid is \(T/(4W)\). Rational Bernstein certificates prove the signs of **1544 primitive polynomials**, grouped into70 facet,125 vertex, and193 mixed-edge tests. Initial powers of \(t\) are removed only because the left endpoint is open; \(t=1\) is included. No primitive is allowed to have an unproved zero.

A separate complete P certificate tracks its52-vertex component,46-edge cut, an above-death spanning tree, and an attaining path. Exact comparisons establish the same positive bar throughout the interval and the strict sign of its relative-depth derivative. This is not merely descent of one escape dot.

At \(t=1\), **MIXED_SEED_G6** has P depth approximately0.3956786953629625, only a small improvement over the parent. The theorem establishes stable-carrier detachment, **not U cancellation**, and it does not certify any later optimizer trajectory or all exterior apex positions.

Observed interval artifacts:

```text
PYRAMID_INTERVAL.json
30460 bytes
ac3dc7b11f8d2c2418648cafd312213b8feff2146d6c68a740aea774318644f4

PYRAMID_INTERVAL_FULL.json
13591639 bytes
2a1fd32ebd45d256a4fb1046681f0879871092e5253caa7437538bf4a698fba6
```

The large coefficient certificate is completely regenerated by the included8926-byte source. It is not needed as an unsupplied external dependency.

## 2. From the detached triangle to a high-contact physical body

The productive next freedom was **joint core/apex motion**, not continued movement of a fixed-centre foot. Each trial reconstructs the current physical hull and integrates its own uniform volume and first moment. Exterior apices are inserted into the **current** body in order. An apex that is exactly contained is recorded as redundant; it is not silently treated as a new exposed vertex.

The initial restricted run moved parent core rows `[0,8,14,22,23,40,59]` and the new apex. It retained own121 but barely improved the bar. Full core/apex freedom produced MIXED_ALL and then MIXED_LONG. A second exterior apex gave the roomier TWO_APEX endpoints. A third apex and a genuine split/opening of a core support produced the useful hinge endpoints.

The hinge experiment replaces core row0 by two nearby physical supporting planes, then separates their unit normal directions while requiring both actual facets to have area at least0.001. The two opening targets were chord separations0.02 and0.1, with P ceilings0.24 and0.26. The rational hinge seed is audited as its own body: **no exact old pivot relation, centroid identity, or class is transferred through rounding**. It actually has tiny additional P/Q bars. The repaired endpoints have separate complete own121 audits.

### Why F117 can still be under budget

These are not generic simple H-bodies. Exact fan planes are constructed from the exact core/apex geometry, preserving real multi-facet incidences. Independently rounding those fan normals would destroy the construction and can change E.

For a visible disk containing \(f\) old facets, \(s\) old interior vertices and \(b\) horizon edges, with no unintended mergers,
\[
\Delta(V,E,F)=(1-s,\ b-s-f+1,\ b-f).
\]
For stacking on one \(k\)-gon this becomes \((1,k,k-1)\). The formula follows by the disk Euler identity, not by counting integration triangles as true edges.

For MIXED_LONG_G7, its core is122/183/63; the apex sees six facets, has21 horizon edges, and removes three old vertices. The actual result is120/196/78. In HINGE_WIDE_REC_G6,
\[
D_V=2E-3V=105.
\]
The three apex degrees are24,31,6, contributing52 to this excess; other horizon vertices contribute the remaining53. **Apex concurrence alone does not account for the entire complexity credit.** True rebuilt E, not F≤85, is the acceptance test.

The separate H_RELEASE_G7 control frees the physical supporting planes without retaining the same fan construction. It has148/222/76, own121, P≈0.3121043. This is a useful alternative physical architecture, not evidence that concurrence is necessary or that the mixed family is globally superior.

### Numerical objective and status

Ordinary runs use the largest **complete current P log birth/death**, and guard all current polar nonroots and all primal vertices except the two allowed P roots. Roots are chosen from the current essential and largest finite bars rather than frozen old labels. The default witness is
\[
m_{ij}=\frac{X_i\cdot(X_j-X_i)}{\|X_i\|^2},
\]
**not a cosine**. A row-normalized dual QP predicts a step; live nonlinear corrections and full-hull backtracking check actual mass, both landscapes, and geometry. Numerical visibility/bar thresholds are discovery aids only; the final exact census suppresses no positive bar.

The run named physical_metric changes the physical body. Its metric is a **parameter-space preconditioner**, formed from the Jacobian \(D\) of all actual vertex coordinates:
\[
G=D^TD/N_V+10^{-4}I,\qquad B=G^{-1/2},\qquad\delta=Bw,
\]
with eigenvalue floor \(10^{-6}\lambda_{\max}\). It is not a fixed-body affine-metric certificate. It produced only the small improvement from the already useful hinge endpoint to PHYSICAL_METRIC_G7.

## 3. Complete exact endpoint ledger

Every body in this table has **additional weak000 and primitive zero000**; its closed-weak census therefore equals the strict census shown. Depths displayed here are approximate. Every strictly positive rational bar, including the small controls, is retained in the reconstructed audit.

| Endpoint | V/E/F | Own S/U/H | Positive P/Q | P relative depth; Q where nonzero |
|---|---:|---:|---:|---|
| MIXED_SEED_G6 |125/193/70|1/2/1|1/0|0.3956786953629625|
| MIXED7_G7 |125/193/70|1/2/1|1/0|0.39526773825570943|
| MIXED_ALL_G6 |123/191/70|1/2/1|1/0|0.3751749138883263|
| MIXED_ALL_G7 |123/191/70|1/2/1|1/0|0.3751750565021285|
| MIXED_LONG_G6 |120/196/78|1/3/2|2/0|3.3171387254390403e-10;0.3225025354961822|
| MIXED_LONG_G7 |120/196/78|1/2/1|1/0|0.32250253325599587|
| TWO_APEX_SEED_G8 |121/224/105|1/2/1|1/0|0.3225001395251882|
| TWO_APEX_G6 |121/229/110|1/2/1|1/0|0.23170513339400295|
| TWO_APEX_G7 |121/229/110|1/2/1|1/0|0.23170516653791834|
| THREE_APEX_G7 |122/235/115|1/2/1|1/0|0.2205421177484459|
| PRUNE_FOUR_SEED_G7 |115/218/105|1/4/3|3/0|0.0025528011695788795;0.0009745491058168193;0.23170909274062912|
| PRUNED_REPAIRED_G7 |115/218/105|1/2/1|1/0|0.25012816865269505|
| HINGE_SEED_G8 |124/238/116|2/4/4|3/1|P:7.218838378362577e-10;1.638437213627272e-11;0.22061068949259058. Q:4.1498184892948195e-10|
| HINGE_OPEN_G7 |124/239/117|1/2/1|1/0|0.22303829275474088|
| HINGE_WIDE_REC_G6 |125/240/117|1/2/1|1/0|0.21842561646101927|
| HINGE_WIDE_REC_G7 |125/240/117|1/2/1|1/0|0.2184249386170291|
| PHYSICAL_METRIC_G7 |125/240/117|1/2/1|1/0|0.21838242670673963|
| H_RELEASE_G7 |148/222/76|1/2/1|1/0|0.31210426869767366|
| BUDGET_ELDER_G7 |116/246/132|1/2/1|1/0|0.2367193518784127|
| ELDER_ROOF_G7 |122/257/137|1/2/1|1/0|0.23160939120533908; **outside E budget**|
| QUOTA_EARLY_G7 |107/221/116|2/2/2|1/1|P:0.02034028559055673. Q:0.5095237631838408|
| QUOTA_FINAL_G8 |104/217/115|2/2/2|1/1|P:0.016185825051280002. Q:0.5316949505140796|
| QUOTA3_FINAL_G8 |104/216/114|3/2/3|1/2|P:0.016006420289737328. Q:0.0015303597847486669;0.5321249560000106|

The four-plane pruning repair genuinely removes two extra P bars, but worsens the main P from approximately0.231709 to0.250128. It is not promoted as a senior-bar improvement. ELDER_ROOF_G7 has **E257/C514** and is retained only as an outside-budget nonrecord.

## 4. Principal continuation data: HINGE_WIDE_REC_G6

The exact input is6689 bytes, SHA-256 `0a2d9b22cd25a74b3f513b93f68783e04bcd6c8b75ea28255b934d04a04fdfa6`. Its complete audit is122019 bytes, SHA-256 `6d8e6f4135280ceeef190743c606e4a5813357fc153070f5d344b5ee6b367679`; its physical insertion recipe is179037 bytes, SHA-256 `7c43197a92b6e54bdd18881ee219020fae5b76e0572b2bb9859426d6a811071c`.

Actual homogeneous mass, approximately:

```text
Volume       1.1929070088937064
First moment (-0.20239436366502683,
              -0.1448234866155504,
              -0.155441536536127)
Centroid     (-0.16966482899008695,
              -0.1214038357858746,
              -0.13030482290508327)
```

The exact reduced rational V/M/c tuple is regenerated, not defined by these decimals. Its canonical encoding is50017 bytes, SHA-256 `b95d4bc26629e375ba98a18bf7be1f884c7fda095dbb0a5a98702807dbbf9e1f`. The largest centroid denominator requires12764 bits; low vertex arithmetic does not imply a small homogeneous-centroid denominator.

In exact lexicographic vertex/canonical facet numbering:

```text
S facet14: triangle [3,77,94]
U vertices: [2,120]
H edge: [19,28]
Physical apex labels: [3,115,55]
Apex degrees: [24,31,6]
Degree histogram: {3:77,4:37,5:8,6:1,24:1,31:1}
```

The stable triangle avoids both U, and none of the apices is U. The two U coordinates are exactly
\[
u_2=\frac{(-403746659638500000,-265540060707000000,185557879883750000)}{365614485024406363},
\]
\[
u_{120}=\left(\frac{3341357003562500}{4746989589729079},-\frac{267288160737500}{678141369961297},-\frac{920808907300000}{4746989589729079}\right).
\]
The old parent's U1 position violates19 new halfspaces and its U123 position violates17; both are strictly outside. This is an endpoint material statement, not a certified continuous identity for a moving root.

The sole positive P is **120→2**. Its complete45-vertex component is

```text
[28,31,44,53,54,57,62,68,72,76,79,83,86,88,91,94,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]
```

Its complete50-edge cut is

```text
[[3,28],[3,57],[3,62],[3,76],[3,94],[3,95],[3,97],[3,103],[3,106],[3,109],[3,111],[3,114],[3,117],[7,121],[8,119],[9,118],[11,116],[12,113],[14,112],[16,110],[17,108],[18,107],[19,28],[20,105],[21,104],[22,102],[24,122],[31,34],[32,123],[32,124],[34,44],[43,101],[53,58],[54,81],[55,122],[55,124],[72,77],[76,77],[77,94],[78,99],[83,85],[86,90],[88,93],[89,100],[92,95],[92,97],[93,99],[93,115],[96,117],[96,120]]
```

The attaining edge is19–28. An attaining path is

```text
[120,117,114,111,109,106,103,98,95,94,91,88,86,83,79,72,68,62,57,54,53,44,31,28,19,15,10,5,0,1,2]
```

Exact births, deaths, relative depths, every primitive sign, and **all** interfaces of all23 bodies are generated by the inline recovery. Q has zero positive finite bars exactly.

### Smaller arithmetic and roomier alternatives

TWO_APEX_G6 has maximum vertex numerator/denominator sizes61/62 bits and20 spare edges. Its stable triangle is canonical13=`[1,76,90]`; U=`[3,115]`; H=`[21,27]`; its sole P has45 vertices and48 cut edges. Its mass is V≈1.2156729467511003, M≈(-0.20798949789096768,-0.1535383203161395,-0.16114375161557754), c≈(-0.1710900110484666,-0.12629903521870123,-0.1325551843908644). Input SHA-256: `777fa7b65fa55b230639dd3412832359adaf08ece29017bf891673afb8e0a3ec`.

MIXED_LONG_G7 has53 spare edges and one non-U apex of degree21. Its stable triangle is canonical10=`[1,53,93]`; U=`[2,117]`; H=`[21,29]`; P has46 vertices and44 cut edges. Actual V≈1.2805342005996034, c≈(-0.1969176340688151,-0.14001099879489215,-0.12913755771820415). Input SHA-256: `47d159644aa112d4edde58d42d0452bb3218e8eb034f38ca777c653be82f9b33`. Its G6 rounding control has a real second P bar and must not be substituted for it.

PHYSICAL_METRIC_G7 has the same principal S/U/H labels as HINGE_WIDE_REC_G6 but different exact coordinates and mass: V≈1.1935202443432704, c≈(-0.1703707021495724,-0.12197038451068025,-0.13031508359544072). Input7709 bytes, SHA-256 `a312b00010214ade1d074716680e1c688182be3d2bf76d2c32adfc4ca1a7d287`; audit144007 bytes, SHA-256 `ac00d27eb7cd406085c52ad653f6b2a72ac895d3cf51844a4e112997043a24e8`. Its72/73-bit vertex arithmetic is more expensive for very little P improvement, so the G6 hinge remains a useful principal continuation entrance.

## 5. What did not work, and what that does—and does not—exclude

Allowing two stable roots while continuing to reduce the complete P led to QUOTA_FINAL_G8, own222. Its P component shrank to11 vertices/cut14 and depth≈0.0161858, but its Q component has44 facets/cut44 and depth≈0.531695. Allowing three S produced own323, with the additional genuine Q≈0.00153036. These are physically realized opposite-landscape transfers, not scalar evidence for110. The first apex becomes redundant in these endpoints; changed exposure alone does not confer cancellation.

Direct U1 repairs, including all-pair cosine-normalized attempts, remained incomplete. The finite screens—21 bounded affine-metric starts,24 bounded projective/affine starts,120 radial-bridge cases,147 terminal-apex cases, and one fixed reference-witness-cell LP—yielded no target. They are **not** full-orbit, all-insertion, centroid-reachability, or global exclusion proofs. Their complete source and starting data are included, but no second execution of all long numerical searches is claimed.

The exact endpoints were cold reconstructed. Numerical trajectory counts are distinguished in `RUNS.json`: recorded states include repeated trust-radius failures and are not accepted-step counts. The mixed7,mixedall,mixedlong,two-apex and H-release runs completed their requested40,120,1200,400,600 steps respectively; several later runs stopped early or reached an opening target. The included27-run ledger records each actual starting pin, all non-default parameters, and the observed state counts. In particular mixedall started independently from MIXED_SEED, **not** from the mixed7 endpoint.

The concrete next departure is a different **finite horizon/junction configuration with opposite-landscape repair**, potentially allowing temporary more-than-two-U states, or returning to the roomier one/two-apex body before changing that configuration. The hard two-U numerical quota was a search choice, not a necessary property of a constructive path. Neither the necessity nor success of releasing it is proved. Further fixed-packet coverage or a smaller isolated gate is not the supported next criterion.

## 6. Exact verification and self-contained recovery

The exact engine enumerates plane triples rationally, tests all inequalities, reconstructs maximal polygonal facets and genuine edges, and checks rank, area closure, positive mass, centroid interiority, and Euler. Integration diagonals do not contribute to E. It computes every strict and closed-weak facet, vertex, and mixed-edge configuration, plus all positive P/Q bars.

Each exterior insertion has two exact containment checks establishing equality to the intended convex hull: every old vertex/apex satisfies the generated H description, and every vertex of the bounded new H-body belongs to the old vertex/apex set. Visible-pyramid volume and first-moment increments match the full new boundary integration. Additional checks use a separate-origin positive-tetrahedron mass calculation and direct global S/U predicates.

`check_bars.py` independently batches **all equal filtration levels simultaneously** and compares the positive births/deaths/components with the stored audit. Every cut maximum and attaining-path minimum is checked. This is one complete hull/mechanics engine with independent mass, insertion, and persistence checks—not two independent hull engines or a proof-assistant formalization.

All23 bodies were generated and cold reconstructed; **all68 input/audit/recipe files matched byte-for-byte**. An initial H_RELEASE input JSON key-order mismatch was corrected without changing geometry or its audit, then its cold replay matched too. The exact interval certificate was also regenerated and matched. Repeated byte recovery is not counted as an independent geometric proof.

### Commands and observed markers

Save the complete decoder below as `RECOVER_MIXED_RELEASE.py`, with LF endings, then run without Python `-O`:

```sh
python -B -S RECOVER_MIXED_RELEASE.py MIXED_RELEASE
cd MIXED_RELEASE
python -B -S REPLAY_MIXED.py --out REPORTS --workers 4 --check --interval
python -B -S VERIFY_ALL.py REPORTS
python -B -S INDEX_MIXED.py REPORTS
```

For only the simpler principal endpoint:

```sh
python -B -S REPLAY_MIXED.py --out SIMPLE --workers 1 --check --names HINGE_WIDE_REC_G6
```

Observed markers:

```text
MIXED_SOURCE_RECOVERY_PASS 60 227661 be9b5f6c480e3f66f121ca70c0c2e18ec099197974a8adf434731366291bbf77
ALL_MIXED_EXACT_BYTE_RECEIPTS_PASS 23 68 28 5 8058 12176abc373909ca0dd78a7815f1d6090c28419a6606305347624aa39dd4075c
MIXED_LINEAGE_AND_INTERFACE_INDEX_PASS 23 632122 2b9ed8aae919a2d73f48372d70e466f7bc68b5bb96dad2f948163e38c44bf791
DETACHED_STABLE_PYRAMID_OWN121_INTERVAL_EXACT_PASS [1, 2, 1] 389 0 30460 ac3dc7b11f8d2c2418648cafd312213b8feff2146d6c68a740aea774318644f4
FULL 13591639 2a1fd32ebd45d256a4fb1046681f0879871092e5253caa7437538bf4a698fba6
```

Exact replay: CPython3.13.5, standard library only. Numerical producing environment: NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, BLAS/OMP/Torch threads1. The decoder includes all23 literal rational endpoint definitions, the complete exact audit/proof and numerical sources, all27 run configurations, and20 lossless numerical starting pins containing4098 binary64 numbers. Cross-version optimizer byte identity is not asserted; exact endpoint reconstruction does not run an optimizer.

Recovery identities:

```text
RECOVER_MIXED_RELEASE.py
96709 bytes
d61c223fc90fc94987035c0516dbf479ed4f630f2fe0a2fb7edba9dadb727023

Verified decoded payload
227661 bytes
be9b5f6c480e3f66f121ca70c0c2e18ec099197974a8adf434731366291bbf77

EXACT_INPUTS.json
61168 bytes
361d147ba04fe0b08f85c95dc9483162440bd45e6ed6156ecda4fc9fdcba8911

CHANGED_NORMAL_EXACT.py
8881 bytes
57732bab47ac8957f540438da2c97fad639942e72bde886969f6bf2dcf371f6e

pyramid_interval.py
8926 bytes
8b97cb0007bbe0265cb36c5c1fb6a53650689b0a3d5de7bda94faed2ae32f941

check_bars.py
2949 bytes
39e11c5c762ceb1bfe4643242f9f505b1ea1032de76b38beafbfe491b98264b9
```

The shortened exact engine removes unused old arrays and constructors only; its13 retained function bodies are AST-identical to the parent engine, with provenance included. The full inline capsule follows.


[Encoded source block omitted; the code in this passage is incomplete.]


Convenience artifacts supplement—not replace—the complete inline recovery: [recovery script](sandbox:/mnt/data/RECOVER_MIXED_RELEASE.py), [all exact reports and interval certificates](sandbox:/mnt/data/MIXED_EXACT_REPORTS.zip), and [original numerical source, pins, and trajectory history](sandbox:/mnt/data/MIXED_FULL_HISTORY.zip).
