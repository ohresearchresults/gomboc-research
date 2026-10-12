# figure-0487

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Clear Willow 56 — opened planar gates, systematic oblique apex-U1 construction, and complete height-chart decisions

## Outcome

No strict110/additionalweak000 body was obtained. The work did resolve a substantial new geometry layer and produced six exact rational, homogeneous, own-centred ordinary bipyramids.

The principal advances are:

1. The orthogonal coupled planar gate is now crossed exactly, including on a certified continuous family. A translation-to-contact lemma explains how to open this gate while preserving a unique planar unstable vertex; it need not be treated as a difficult standalone optimization target.
2. For one new gate-open 15-gon, the complete orthogonal height arrangement was executed: 842 interior ratio events and 4,394 physical-U1 cells. None is S1. This closes every orthogonal height choice over that particular base, rather than merely failing to find suitable heights.
3. A root-lifting construction systematically converts a suitable planar U1 polygon into a homogeneous ordinary bipyramid whose unique U is an apex. It supplies an exact physical-U1 height criterion in a genuinely oblique family. Thus the nonorthogonal apex-root direction is demonstrably nonempty, not just formally unexcluded.
4. The remaining S/U problem in the two-parameter root-lifting family has an exact arrangement with ratio events of degree at most four. For the new 15-gon, I executed this full arrangement and closed the entire ordinary root-lifting family against strict110/weak000.
5. Exact controls include an orthogonal C90 strict211 body, an orthogonal C90 strict121 body, an oblique C90 apex-root strict211 body, and a distinct oblique C186 apex-root strict211 body. Every promoted endpoint has a complete maximal-hull, actual-mass, strict/weak S/U/mixed-H, and physical/polar landscape audit.

These are scoped decisions. The ordinary octagonal problem, arbitrary planar bases, general oblique apex motion, and the complete ordinary-bipyramid family remain open.

## 1. Source authority and reading

I read the new journal completely through EOF, including the literal parent `figure-0485`, metadata SHA-256 `681b247960483bd6c334be85c335aa20eb810feae413dbe64ccadd3699fb976a`, and all thirteen decoded parent source units. The parent decoder passed its source-hash checks, and both parent exact controls were reproduced. Earlier unchanged sources remained available; no required exact dependency was missing.

The new journal has 229,604 bytes and SHA-256 `381a15083fc5a132feabab2e6edfc8f63b7711f53ebaad16a379ba6aff1b3cd0`. The supplied previous decoder has 16,634 bytes and SHA-256 `3cfca31a93e2108fe08d088d254f2f49a3a81f2151b1b941988289b72de05eb4`.

The parent owns the sharp orthogonal criterion with κ=7−4√3, and explicitly distinguishes the coupled reserve gate from S1. The work below uses that distinction rather than promoting a gate crossing to a construction.

All weak tests use complete outgoing maxima. A zero primitive accompanied by a positive outgoing arrow is not an additional weak equilibrium. No abstract-tree representative is used as a substitute for all labelled geometric embeddings.

## 2. A convenient complete physical mass-closed form

Let Y=conv(y_i) be a counterclockwise strictly convex planar polygon, let c be its exact area centroid, and set p=−3c. For a,b,η>0 and any planar vector v, define

`z0=η(b−a)/4`,

`B_i=(y_i,z0)`,

`T=(p+bv, η(3a+b)/4)`,

`D=(p−av, −η(a+3b)/4)`.

The apex segment crosses the base plane at

`q=p+(b−a)v`.

Require q∈int(Y). The actual uniform filled centroid is identically zero, and

`Vol=area(Y) η(a+b)/3`.

Indeed the weighted apex projection is

`[a(p+bv)+b(p−av)]/(a+b)=p=−3c`,

and the vertical mass equation gives z0 exactly. Conversely, after a Euclidean rotation making the base horizontal, every own-centred ordinary bipyramid has this representation with η=1, a and b its vertical apex distances, and v the difference of the apex projections divided by a+b. Normalizing |v|²+η² to one is optional, not an additional geometric requirement.

This form keeps the physical planar base fixed and makes the crossed dependence on the two heights explicit. It does not replace the full SPD orbit of a fixed raw body by one scalar.

For every endpoint below, the maximal facets use base labels 0,…,n−1, top label n and bottom label n+1:

`face i=(n,i,(i+1) mod n)`,

`face n+i=(n+1,(i+1) mod n,i)`.

The verifier does not merely assume this hull. It exhaustively enumerates supporting planes from every vertex triple and proves that these are exactly the maximal facets. It then reconstructs the 3n true edges, giving V=n+2, E=3n, F=2n and C=6n.

## 3. The new exact gate-open planar base

The following complete rows, divided by 10,000,000, define the principal 15-gon Y:

```text
[(9999750,0),(7043289,4562555),(4819259,6270852),
 (2530135,7087336),(246294,7165203),(-1917099,6529380),
 (-3788317,5153026),(-5066423,2976332),(-5033603,-2438745),
 (-4115906,-4334074),(-2594544,-5779590),(-643972,-6655841),
 (1585590,-6872146),(3965098,-6323766),(6395739,-4800502)]
```

Its exact area and centroid are

`area=157165560947977/100000000000000`,

`c=(264251628242479064191/1571655609479770000000,
    14301951957167488963/785827804739885000000)`.

The point p=−3c is strictly inside Y. Vertex 0 is the unique planar strict U; every other vertex has a positive cycle escape, so D2=0. The exact gate data are

`L=1211104399775049189910663205662537650921 /
   123505067740461365214501962645000000000000`,

`Fmin=11628628590706379620708463972103226643 /
      230437214724686604344316021650000000000000`.

Thus Fmin/L≈0.00514611016094, strictly below κ≈0.07179676972449. The certificate uses the rational comparison

`0<Fmin<L` and `Fmin²−14L Fmin+L²>0`,

not a floating approximation to κ.

### Exact bodies over this same base

With v=0 and η=1:

| Exact body | a,b | Strict S/U/H | Equilibria |
|---|---|---|---|
| `C90_COUPLED_GATE_312` | 2/25, 12/325 | 312 | S=[0,7,15], U=[0], H=[(7,15),(7,16)] |
| `C90_ORTHOGONAL_BASE_U1_211` | 1/200, 1/400 | 211 | S=[0,15], U=[0], H=[(7,8)] |
| `C90_SAME_BASE_TALL_121` | 200, 1999/10 | 121 | S=[7], U=[15,16], H=[(0,15)] |

All have V17/E45/F30, additionalweak000 and primitivezero000. The first actually crosses a short-side reserve: B=b(a−b)/4=42/105625>Fmin. The smaller-height 211 body does not cross that reserve; it is preserved because it improves the parent C90 strict413 entrance to strict211 at the same complexity. The tall 121 body proves that the fixed-base obstruction below is genuinely coupled: this same planar base can produce S1 or U1 separately, but not both in the orthogonal family.

The complete landscapes are regenerated in the reports. In particular, the orthogonal 211 has Pbars empty and one Q packet of 15 vertices/15 cut edges. The tall 121 has Qbars empty and one P packet with component [0,16], 17 cut edges, and attaining path [16,0,15]. The reserve-crossing 312 has two Q packets, of sizes 2/4 and 14/16.

A provisional filename for the new gate body contained 413. That alias was rejected immediately after its audit: the new body is 312. This correction is separate from the parent's older 413-versus-211 filename correction.

## 4. Complete orthogonal height decision on this gate-open base

I implemented and executed the parent's quadratic-event arrangement, rather than optimizing a and b continuously. Put t=b/a∈(0,1), k=a². The rows comprise all required polar cycle signs, bottom lateral signs, and the physical-U1 bounds L−A+>0 and B−D2>0. Each is β+kA(t), with deg A≤2 and constant β.

The exact algorithm isolates all poles and pair crossings, deduplicates algebraically identical events, chooses rational ratio samples between isolated roots, and sweeps the positive k zeros using integer signs. It retains identically zero rows and classifies vertices by the maximum of all outgoing signs.

Executed result:

```text
77 rows
842 interior ratio events; 844 including endpoints 0 and 1
4394 open physical-U1 height cells
S2: 2263 cells
S3: 1332 cells
S4:  799 cells
No additional weak-S in these open cells
```

The only stable-root sets are [0,15], [0,7,15], and [0,7,15,22]. Every open U1 cell retains stable facets 0 and 15.

A hypothetical weak-free S1/U1 point lying on a noncritical primitive-sign event would have an open neighborhood preserving its strict roots and positive escape witnesses. It therefore cannot evade this open-cell enumeration. The inherited apex-root theorem covers the remaining orthogonal U chambers, equal heights force S≥2, and exchanging the two caps covers a<b. Consequently:

**Every orthogonal positive-height bipyramid over this exact planar base fails strict110/additionalweak000.**

This is a fixed-base theorem, not an exclusion of all 15-gons, octagons, or affine images. The report is `C90_COUPLED_GATE_312_HEIGHT_ATLAS.json`, 4,390,635 bytes, SHA-256 `495d1a7e8559f603b65368b82812b1c604334c1a8ebd0c3af543ffd42b066f67`.

The supplementary all-height S arrangement was also run once and found S1 outside the U1 chamber; its exact tall 121 endpoint is audited above. Its generator is preserved, but this large supplementary report is not needed for either main exclusion or any endpoint recovery.

## 5. New translation-to-contact gate-opening lemma

This explains why crossing the planar gate is not, by itself, the central remaining difficulty.

Let X0 have area centroid c0, p0=−3c0∈int(X0), and one strict planar U root r. Choose one positive cycle escape e_i at every nonroot. Suppose a nonzero direction v satisfies

`v·e_i≥0` for every chosen nonroot escape,

and `v·(x_j−x_r)≤0` for both root exits.

Translate the planar polygon by s v while retaining the actual mass coupling:

`X(s)=X0+s v`, `c(s)=c0+s v`, `p(s)=p0−3s v`.

Every chosen positive cycle sign is preserved, because its value changes by s v·e_i. Both root signs stay negative. Thus D2=0 throughout this translation ray.

For the fixed outward edge normal n_i, the crossing gap is

`g_i(s)=n_i·(x_i−p0)+4s n_i·v`.

Let s* be its first positive contact time. Suppose the contact is in the relative interior of one edge e, and p(s*) has a nonzero tangential component on that edge. Then L(s*)>0: one endpoint of the contact edge has positive p(s*)·(x−p(s*)). Meanwhile

`F_e(s)=[n_e·(x_e+s v)] g_e(s)/|n_e|² → 0`.

The first factor remains positive, since the planar centroid remains interior and 0=(3c+p)/4 remains interior even at this contact limit. Therefore, for all s<s* sufficiently close to s*,

`max(D2,min_i F_i)<κL`.

This is a conditional constructive lemma with explicit geometric hypotheses, not a claim about every planar U1 polygon or every translation direction.

### Exact continuous realization

The recovery source includes all fifteen literal rows of the parent's `C90_ORTHOGONAL_BASE_U1_413`. Apply the lemma with

`v=(1,1/100)`,

`s*=3733200335772189/3139172823038000000`,

`s0=s*−1/100000000`.

The first contact is edge 7, in its relative interior, and all escape-cone hypotheses are checked exactly. At fixed rational heights

`a=1/512`, `b=3/3328`,

the entire interval **s0≤s<s*** has physical strict U1, no additional weak-U, and the strict short-side reserve failure B>F7. Three exact quadratic Bernstein certificates on [s0,s*] prove

`L_8−100F7>0`, `L_8−A+>0`, `B−F7>0`.

Here L_8 is the support witness from base vertex 8. Since 1/100<κ, the first certificate also proves the sharp coupled planar gate. The endpoint s* itself is excluded because ordinary crossing becomes non-strict.

At s=s0 the complete audit gives `C90_TRANSLATION_GATE_312`, V17/E45/F30, strict312/weak000/primitivezero000, with S=[0,7,15], U=[0], H=[(7,15),(7,16)]. Its full S/H/weak census has only been promoted at this endpoint. The interval certificate is U1/weak-U0 plus the reserve gate, not a claim of full weak000 or S1 on the entire interval.

## 6. New systematic oblique apex-root construction

Assume Y has p=−3c∈int(Y), a unique strict planar U at y0, and a positive cycle escape at every other base vertex. Put r=y0−p. For λ,h>0 define

`B_i=(y_i,h(1−λ)/4)`,

`T=(y0,h(1+3λ)/4)`,

`D=(p−λr,−h(λ+3)/4)`.

This is the physical mass-closed form with a=λ, b=1, v=r and η=h. Its crossing is

`q=(1−λ)y0+λp`.

Hence it is an ordinary bipyramid for every 0<λ<1. Its two component-pyramid centroids are `(r/4,h/4)` and `(-λr/4,-λh/4)`, with volume ratio λ:1, so the actual filled centroid is exactly zero.

The top apex is strict U for every λ>0: its planar outgoing dots are those of the strict planar root, and each receives an additional negative vertical term. All nonroot base vertices retain their positive cycle escapes. For 0<λ<1, base vertex 0 escapes to T because

`B0·(T−B0)=h²λ(1−λ)/4>0`.

Only D remains to be classified. Define

`E_i(λ)=(p−λr)·(y_i−p+λr)`,

`L_D(λ)=max_i E_i(λ)`.

Then

`D·(B_i−D)=E_i(λ)−h²(λ+3)/4`.

Therefore the following is an exact necessary-and-sufficient physical criterion in 0<λ<1:

**The body has strict U1 and no additional weak-U iff**

**`0<h²<4L_D(λ)/(λ+3)`.**

In particular, if L=L_D(0)>0, choose rational h with h²<4L/3 and then a sufficiently small positive rational λ. This constructs a rational homogeneous ordinary bipyramid with its sole U at the top apex. No adjustable centre or point masses are involved.

There is also an exact closure on the other side. For λ≥1, B0 cannot escape to T. If a weak-U-free U1 system with root T existed, B0 would have to escape to D, and D would have to escape to some base vertex. Following the preserved positive base-cycle path back to B0 would create a positive directed cycle, impossible because squared radius strictly increases along every positive arrow. Thus **no ordinary member with λ≥1 is weak-U-free U1**.

### Exact compact apex-root control

Using the new fifteen rows above, λ=1/10000 and h=1/100 gives

`C90_ROOT_LIFT_211`: V17/E45/F30, strict211/weak000/primitivezero000,

`S=[7,15]`, `U=[15]`, `H=[(7,16)]`.

Its P landscape has no positive bars. Its sole Q packet has 14 vertices/16 cut edges; the attaining path is [15,16,17,18,19,20,21,22,7]. This is a genuine own-centred oblique apex-root U1 example. It does not contradict the orthogonal apex-root theorem.

## 7. Complete two-parameter root-lifting atlas: quartic ratio events

The remaining stable problem in this family can be decided without an unconstrained height optimizer.

Let n_i be the outward, not necessarily unit, planar normal of edge i, and set

`σ_i=n_i·y_i`, `g_i=σ_i−n_i·y0`, `R_i=n_i·r`,

`d_i(λ)=g_i+(1+λ)R_i`,

`T_i(λ)=λσ_i+(1−λ)g_i/4`,

`D_i(λ)=σ_i−(1−λ)d_i(λ)/4`.

For 0<λ<1, T_i,D_i and the crossing gap g_i+λR_i are positive. The polar vertices are

`q_i^+=(λ n_i/T_i, g_i/[h T_i])`,

`q_i^-=(n_i/D_i, −d_i/[h D_i])`.

Put H=h². After clearing positive factors, the top and bottom cycle signs i→j are respectively

`H λ[(n_i·n_j)T_i−|n_i|²T_j] + g_i(g_jσ_i−g_iσ_j)`,

`H[(n_i·n_j)D_i−|n_i|²D_j] + d_i(d_jσ_i−d_iσ_j)`.

The lateral top→bottom and bottom→top signs are

`H λ(1−λ)|n_i|²/4−g_iσ_i`,

`−H(1−λ)|n_i|²/4−d_iσ_i`.

The removed lateral factor is `(1+λ)(g_i+λR_i)>0`. The physical D rows are `E_i(λ)−H(λ+3)/4`.

Thus every required row has the form

`A(λ)H+B(λ)`, with `deg A,deg B≤2`.

Its positive-H zero curves change order only at roots of A, B, or `A_iB_j−A_jB_i`. All such ratio events have degree at most four. Exact factorization and rational real-root isolation, followed by rational λ samples and positive-H sign sweeps, give a complete arrangement. Constant zero rows remain zero; complete three-arrow maxima classify each polar vertex.

### Executed full decision for the new 15-gon

```text
105 rows
5085 distinct nonzero event polynomials
4790 distinct irreducible factors
2394 interior ratio events
13 open physical-U1 cells
9 cells with S2; 4 cells with S3
Stable-root sets: [7,15] or [7,15,22]
```

The complete report is `C90_ROOT_LIFT_FULL_2D_ROOTLIFT2D_ATLAS.json`, 795,229 bytes, SHA-256 `91e85efb6cc60541d8d3e84f1ce8f7855c49d3d329731cabbd475cb62950ee3f`.

The open-cell continuity argument excludes weak-free11 exceptions on primitive-sign events. Combining this complete λ∈(0,1), H>0 arrangement with the λ≥1 positive-cycle theorem yields:

**For this exact planar base, no ordinary member of the entire root-lifting family, for any λ,h>0, is strict110/additionalweak000.**

This is a two-parameter geometric/axis-stretch family, not the full SPD orbit or all possible apex projections. The earlier one-dimensional h=1/100 slice was also exactly enumerated: 24 events, 25 intervals, no11; its source and report are retained, but the full two-parameter result supersedes that narrower decision.

## 8. Distinct C186 oblique apex-U1 checkpoint outside the root-aligned chart

For continuation beyond the closed root-aligned family, preserve `C186_OBLIQUE_APEX_U1_211`.

Use the complete following planar rows divided by 100,000,000:

```text
[(100000000,0),(91340210,27801891),(88356684,34856229),
 (82444878,45244784),(68747120,60530146),(57383111,69660774),
 (47094856,75839600),(37355250,80182208),(28037244,83139627),
 (18889672,84994455),(9629493,85859192),(-231057,85661093),
 (-10257768,84269070),(-20542525,81502612),(-33579039,75524138),
 (-50237784,61767560),(-67728196,-26639710),(-62795945,-39574309),
 (-56345784,-50085172),(-48455251,-59186378),(-39338997,-66844875),
 (-29590747,-72759225),(-19130510,-77180323),(-7832556,-80141975),
 (4377650,-81494582),(17143769,-80969795),(29622141,-78494567),
 (42668215,-73748422),(55881542,-66298645),(71482056,-53374754),
 (85294986,-35173466)]
```

In the complete physical form of §2 take

`a=1/1000`, `b=1446823/1000000`, `η=7/25`, `ρ=24/25`,

`τ=444529/25000000`,

`v=(ρ(1−τ²)/(1+τ²), 2ρτ/(1+τ²))`.

Here |v|²+η²=1 exactly. Its exact volume is

`108039116315266993463971/375000000000000000000000`.

The full audit gives V33/E93/F62, C186, strict211/additionalweak000/primitivezero000, S=[15,31], U=[31], H=[(15,16)]. Pbars is empty. The sole Q packet has 32 vertices/32 cut edges, peak31→elder15, death edge [15,46], and attaining path [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,15]. Complete rows, cuts, radii and signs are in the regenerated report.

The exact literal τ is twenty grid units below nearest 10^-8 rounding of tan(theta/2) from the stored numerical nomination. Recovery explicitly applies this −20/10^8 adjustment and sets a=1/1000, rather than falsely claiming that the accepted body is an unmodified nearest-grid freeze. The exact object and its audit are unaffected by that provenance correction.

No full height, metric, or geometric exclusion is claimed for this C186 checkpoint.

## 9. Verification tier and finite-search scope

All six endpoints have one complete exhaustive rational maximal-hull and mechanics implementation. Each has two positive volume/moment decompositions: coning the maximal boundary facets from the actual origin, and the common-apex tetrahedra (T,D,B_i,B_(i+1)). Both give the same positive volume and exactly zero first moment. Same-centre polar-U classification independently agrees with the face-foot stable census within this implementation. This is not two independent full auditors.

Every edge is explicitly checked using its perpendicular-foot parameter and both adjacent-normal cone coefficients. Euler, Morse, and bar-count equalities are additional checks, not substitutes for the mixed-H audit.

The complete sources preserve these finite numerical windows:

| Campaign | Completed runs | Iterations/evaluations |
|---|---:|---:|
| Planar gate nomination | 11 of a 16-case request | 87 / 1472 |
| rho=3/5, n15 | 8 | 7069 / 11425 |
| n23 Q-bar objective | 5 | 910 / 2268 |
| n23 prescribed-Q-root objective | 6 | 3841 / 5541 |
| rho=24/25, n31 apex-root nomination | 3 of a 6-case request | 298 / 1406 |
| n41 root-lifting search | 5 | 1246 / 3073 |

A separate 125,000-height orthogonal scout found no S1 in its sampled apex-escape chamber. None of these finite campaigns excludes a geometry family. Near-zero penalties, fragile crossing margins, or floating blocker outcomes were not accepted as exact constructions.

Projection-chain parametrizations were motivated by the Conway-spiral literature. Its point-mass constructions and its special homogeneous spiral exclusions were not transferred to these uniformly filled arbitrary bipyramids; the new conclusions rest on the explicit mass calculations and certificates above.

## 10. Most useful continuation

Do not repeat height optimization over the new fifteen-row base: both its complete orthogonal height family and its complete root-aligned oblique lifting family are now closed against weak-free11.

The translation lemma supplies a cheap, certified way to enter the coupled gate while preserving physical U1. The unresolved task is the full polar cycle obstruction. A constructive successor should change the planar interfaces around edges 0 and 7, or release the top apex's planar alignment with the base root, while rebuilding the exact area centroid and maintaining the appropriate physical escape witnesses. The C186 non-root-aligned apex-U1 body is an independent open checkpoint. The octagonal D2>0 chambers are also not covered by the single-planar-root design subclass used here.

## 11. Durable source-only recovery

The inline decoder below reconstructs all 21 source/data units. It includes the complete exact hull/mass/S/U/H/weak/landscape auditor, both full arrangement generators, the narrower slice generator, the translation interval certificate, universal symbolic identities, both material nomination pins and exact freeze recipes, all numerical producers and finite receipts, and the ten-report expected manifest. No parent file, library item, network access, or optimizer run is needed to recover the exact objects or certificates.

Versions actually used: CPython3.13.5; exact bodies use the standard library. Symbolic factorization/root isolation uses SymPy1.14.0 with Python ground types. Optional numerical producers use NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, float64 and one thread as set in their sources.

Commands:

```text
python -B -S RECOVER_C48_GATE_ROOTLIFT.py OUT
cd OUT
python -B REPLAY.py all
```

Separate phases are `python -B -S REPLAY.py bodies`, `python -B REPLAY.py atlases`, `python -B REPLAY.py theory`, and `python -B -S REPLAY.py collect`.

A fresh source-only directory completed all phases and matched all ten exact report sizes/hashes. Expected terminal markers include:

```text
C48_GATE_ROOTLIFT_COMPLETE_SOURCE_RECOVERY_PASS 21
SIX_OWNCENTRED_BIPYRAMIDS_FULL_HULL_MASS_MIXED_AUDIT_PASS
C90_TRANSLATION_INTERVAL_U1_AND_RESERVE_PASS 8
ORTHOGONAL_AND_ROOTLIFT_FULL_PARAMETER_EXCLUSIONS_PASS
ROOTLIFT_UNIVERSAL_FOUR_POLAR_IDENTITIES_PASS
ROOTLIFT_105_CLEARED_ROWS_DIRECT_AUDIT_AGREE
TWO_FULL_PARAMETER_ATLAS_EXCLUSIONS_PASS
C48_GATE_ROOTLIFT_SIX_BODIES_TEN_REPORTS_PASS 10
```

Optional producer commands are `gate_chain.py 7 7 16`, `search_oblique.py 7 8`, `search_oblique_bars.py 11 5`, `search_oblique_root.py 11 6`, `search_oblique_apex.py 15 3`, `search_root_lift.py 20 5`, and `probe_orth_S.py`, each invoked with Python. The three-case apex command reproduces the completed prefix, not the unfinished six-case request. Optional all-height stable enumeration is `python -B -S height_atlas_fullS.py GATE_ROWS.json 10000000 C90_GATE_FULL_S`; its previously generated report has 66,869,995 bytes and SHA-256 `cd2c01b71fe265eaaa0575e06d43317b692512c69e122519c1a018167877f798`.

Main exact report receipts:

```text
C90_COUPLED_GATE_312_AUDIT.json
73375 b6a8e8e3db548be0299d356726fda1dd706d7be6a1a996a5fad6b97fc6b9fafd
C90_ORTHOGONAL_BASE_U1_211_AUDIT.json
71268 1acc730b3931d660c72d4a46dfdd5971cf4207f60841d161dad64768bccae973
C90_SAME_BASE_TALL_121_AUDIT.json
75692 9d0ae2c88c7999907b0a74cba6fdfae67264e7b9e7267f286b4d0415126409d3
C90_ROOT_LIFT_211_AUDIT.json
63542 1282089ce72f5c0e62124443454427f8a9a324e0462d73c085119578cae28c39
C186_OBLIQUE_APEX_U1_211_AUDIT.json
243888 1381790092be8c5bbe03af2162341d64220ffe33a00b40a86d8dfb48bb07c8db
C90_TRANSLATION_GATE_312_AUDIT.json
85041 5071426e57bb7babafc9a534d71d557251380b077201b17bc65560ee72e4788e
TRANSLATION_GATE_PLANAR.json
2651 efaf93a0ab6c763e4cceb1d531c584a8de2453d7bf750927958853a18b48c757
C90_COUPLED_GATE_312_HEIGHT_ATLAS.json
4390635 495d1a7e8559f603b65368b82812b1c604334c1a8ebd0c3af543ffd42b066f67
C90_ROOT_LIFT_FULL_2D_ROOTLIFT2D_ATLAS.json
795229 91e85efb6cc60541d8d3e84f1ce8f7855c49d3d329731cabbd475cb62950ee3f
C90_ROOT_LIFT_211_ROOTLIFT_ATLAS.json
52851 4646c2473d2b008d5be8c71558ebe7d62e12f61002a78cb2fe268907db6523ed
```

The source dictionary has 94,281 bytes, SHA-256 `a7e2257ce307dca3f7301259b8a1700c1d1c75992d7d936a1b1ff113a9bad159`; XZ payload 22,260 bytes, SHA-256 `d29b445e55e29325d8ae3fc05216328f4105bd4e0be3641e3a2000d95414ccea`. The decoder has 29,371 bytes, SHA-256 `751262b25734a37abd3dd0596adf3a36045aa7535bc65bbe13cbd0f9ceaadd26`. A convenience copy is RECOVER_C48_GATE_ROOTLIFT.py; the complete decoder is also included inline:

```python
import base64,hashlib,json,lzma,pathlib,sys
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'C48_GATE_ROOTLIFT_REPLAY')
out.mkdir(parents=True,exist_ok=True)
B85=(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;c!S+vt0l^h=gMi&V3R6-h~i0X6I8#Z_*MQGIdbF`jg_NPr4^bI@#k=Yrf=^WGThU7bovb'
'VmOwR#lN!ev6`-+^a$2^{OMkok@CmLk{dv)ABhygGt)sDz_I8_==XbTR@*wL86K*?Gdyu0;ys05A`{tROXF6O{Ttu2rp)PYI=wO7'
'IDVAm&RILXhY-HjIy}~gSZB;DG5RIb#jv+Q%e@_PqbYcJs!@y;+gIM=SC56xNcTv8aIEnz(`=xX@U@2k6!nf<X+Umpj<6Sv5svYq'
'o#M$Viq%lIAx{KcA|1nfzrn3P#k}#CM-Oz=VUXvtR*`w0YaTt$YYlpOh_q=rrLti;P&zog&leW*X*t-JZ1q`j9JzL{#5T{-H-j7z'
'E*AW&3m>S?X$JvgrPY^?3jB5t<&w+b<4D32K5x<C?ztR-sVGDDwYI_hjRrhV7x>9OVpOZ}_H)V&0L&AVjEE)cbfI?b?%ZRDZ*OXb'
'`WP{}hCVk2aX<47feHz*A=S8=e>jC_q~Qcl&ay?=)1ahlu01?ltFjJ95cY(7`4Jk-a{*fjt42Irr(8*jeWQ;!6I!w{a?pZ%I#Hm^'
'PIA*WLwvk1xKbPg+}Chrk&^_3`Z}i{6|S`1IX|8kTn@By)h|C_j%sTFLHQ_%dGVg+H>&}PkG2~U_R_SvBve0ZU9-h1>JP+4q;lds'
'L>PEvaIuf<OlRnh5_r&Ve#{+hemS?x-uwjEi)C-UT5;vv<<l#w43;2OoBG7j%83Ppek`Z!4CVhr1t-~Za8QFE)haKAHh4=9C2c<?'
'JuQ6~V8Dt_@>RqHYBy>K(1hSt!#I6m{NuS+d@IWw(27=Ge1~!p>K=F3#A$qtl4G`Ne@NU}VPLo~WNR4xJ(#vXbH9Yh#km8YJ`K3^'
'zE9}An*qvKZ|*JPn`LSJ0B}C77!AZ(5b)z?@^i}{0jI>OD@LMF*-39bBNA;uV~M(qK-w(fOS>fYmMC_3y#YIoHzDP$3UDy*0(SUJ'
'0iP?n!;5(j2hg@SRlcZ6sCGH}v-JCxsHN*F*dEB^L5B5DN`CYm2}>K+aC0)mq7=o9_iZQkOsPG)E5y$*{(^S9Y!D-5l;6M?t>zwW'
'6i$`%T*vG}L@K(GrYv$5Mkrbo&y+=IP<qe5NI#B_c6AZ%$z~cxck)u5f`F|neK^YJ0QRU<9(SWYB5B$VgBdH`J&kNIy0HD#4E~eo'
'^mR+sWQQ(5%~r2K77U^y*}ed$sBg)Wu2eP9@%&Q$c=i|viL-y74BBLy(Y0mpjuTBTS|XX%j~dff+q~M}!Q4GGT2hh%EY1rrXOL5S'
'r7r?&y@`4aN&emA1W*Q?`)TgSFTS){_WU$WNUpJ^-mdR&4V1zNON04lvEe~=MO0Z~knr3v$7gcIUr=}HB0pZdL$@#bkg+y#41nnu'
'jzXcwkt#yV2jLm)?g&wZJ?S~$u>ZUmGWzGvA?je4SF+!;Gnt9>!t5kUd1D1rlT&m*D(cE~(=p;@z{5^%a&*&14~KqoLP<TgK6UT^'
'_RJs?sKKExTTw}XeIn3R4v0p2#XDkyyp#u1vvB)O&%iqVPhAb63<%mLN3ZuzO6sBdaIoq|i2F2FqDi4{3ABojNtN0G1<_)__S-?4'
'8ge|Sq%w32GTvz*YWUg@lwDA7fl;*K#03|@kurd@7I{Dd%EBgfjs>9kd6u1HGX{YEt@$o>m9<-?wM6*h6*8lHjH~BrtjP+coT!vw'
'7bCUq8z#34E+^;HWMrmE_WB*$`_I(IPZPdu-LI&&@YknTYuk6`?OBEOTIhhmjGk7X!6Um4Rr(-l#Yk^a*mssXm;_Zc4Ziuwy$!Fv'
'#`29eLPwtSY7Hc*Yrfo!K0k+~Q*FX8w#_WT=P_eQ(4FS-J|~Sri=IXo0t3O7YHEO*wxGP5wXrHS!n-fvwo`YLMZ|D6)KFuB--bhu'
'y8O~%*5)S#EPbG0!uJgTO#`Mh9Jq~^kx+lBDJn61B??xXnU76hF)pMJ<$Sv)e^PC?A4PEpfx0PQ=10o7=hGHlcW4jN!RK%biR<Y7'
'eI+M#&#!Edh&2jN-_j`qis7yp8Szs34OINPC*DYvzI20EJ8pK>x<2UAUM-xGAR%XWPnB{=#MjBm15B<~`anWQGgy*L*xJ59R{I()'
'F94kQuvNw?P&KKy61z;_{knr7uO(|8GvMzx9T6k2{s6T?!`IS<f)WUy`r017d@y*B7Vt#nrTc+%)eKFPlt5{2Ckj8gdTKODW4LAY'
'Us$(Gb}P3js3U>!ZQFrH-NsK$OHk2@WUSRU<i)09fqkHo|3}By2MXHdCdqAV5D6@AyAw`^5mHvcD@3F?<ZtK**cjjjy@=vCZ_q0A'
'n8{m=DNbZMCbHu%n59~>Ge@L$mCqjkS#aXlzg*Vbk&_Jurwb;uA}MYR@YLjubEcEAcvwlg{T`VoG`va+NwR~+WK|3pnn^zVV#Li-'
'>EJm?gGGT}v3^QQu+S}KRTf+?&DN^x1q7g>dp=?d!VUh>N=BU#MsNtfTVpfN++QfxGxv=gjW!{f=K*w;4O)f7MkPkfq@PPyKaO2T'
'Il43p@-qXpgF^zy`AfQ|51sNgvKtdD8!N;B8dT@|IVj+MU!a8(H8{`YI7oMqvT!aRU6WeV0~|=exZ0t#%VXw$a*kI(Xliiebut%Z'
'9kb790hIHlumpi@CcEcU#Ye5PMPsmbF*L5omcD;%k@v2CE12mx&h<Rxe1z(07{1w9t&D;cC9sE<0rB|H<}+b!96_;!|C}T#q99KT'
's$FH+b9dFAe4*Koo4Kzr_Gp=^K)1T4F?q<@*jJjPFdu0g<8@67Dg9McS1#rQB(ed4eGBvx@+vQ{E8th{-h(b?Q_E@iiXxfwu?iZ6'
'$ziz<4Il#2j~plUZ|3syV8TKB-!+b|&yx5xKUaWruG$YOzS(gwyldN}qhIv?xszA8Nen0fy4}*VTB(m3XXin129yvz6*26WaI~%S'
'p~jPymB|-q>NPk~a!nKqfWBe*I0o*959J7nKh?DYCzl1R$625-a@3Xbom00Ghw>dgd=z7;SipugW$zWhzwL`rV5Xv+J0@=Z&oT@w'
'auXdcTRIst$85qq@gw>oHnkJ+E?8L+VDWR*1SsY7Ff#jK9M)aD6Xs^yzw61D%V~u5qm>UXo>A4JUVOu(TZ0LAN_(z+S9<xR0--U^'
'ME7#M!ZQ<2q3~1{L{HHHGfu8%^39M;5l~oH)#)VABhA3VIEqoq!z+TKXYb=bE2X@IpI30bRlc%B$t@`3tZkwn@w2Umu&kz^m@2&Z'
'$MaZ?&#;?WH=!Etc)#>jNDg#wn87Mik6JJx&yaO8Xwhp6tmtE;gbrkx*@a+|9<}ckGDc%Gf~8NeJE6<r|I<`40v$8F$%}7o6rIyL'
'QJ|<trC;lZNMSU=^YI$YL9Xbzbw<1@+QgMB*$9|zIqFUAj{Wrz9X$2kyN%+hOsL8NwYIy(t)``p!4@Q-L;6L0mVR*O7ii5+SUQ)@'
'PheFOw@lt@vkb@zS6~`iXpWGi9zMMC^mFu=Aj$n*aRbIqFJ1<Mn9eyDGoZ2{Uv&%3lrBdvXClNh|1~2fsgZR1Opp5$($W?vF*~!C'
'tgL=|-SCCnkA6vp<r)8RkO47##A0a0#Hg`ongvU&Tr=-@ZRcf)fBxgY{+8gR?+|*$K`EJ<6RqiZvuVCFV#5DHSD&OYjj`2Fki4bm'
'Ldo=xNWI;(>}39gBnc+z*DZOW6Sm(Xb7hLd$(45;8>qJyT_?o%-t`pI2Cy{NYQUbN6`V_FJzCBd^%vd49?B}<umK%;%?|i5ar|;p'
'!O)=P$fzvaU%CFToR{q(q7?ngruc{B+;L87O9PTeqidP(R>9E0RWN#NcVJ`u+SHFF^P!f*@FEYq;H9|-Q%J5AfR^?TLe&0E6s5BQ'
'Hd}zNHK3KoZb?9gaISh&)lOtT3Q+c9`b8!*OM^YRTb;Q-9t!)oH{Jou=34tjiRM4ftd5DXBaMmXwtCnyVh0atqWVnYl@ino6Q{w5'
'{rLa}y#5*VXIi<+uE2gnQ!utqmweCV_z4E73t)s6(sCziH|OJj$5)LgDvf@zKFkp3ul@%BhHt7jIOHo+DIWZUdoW#Vn7@SliBpHC'
'C7zY`^^`zWscSka;><j!g!~6<I6|Ei`rp2F^qJNApn%iBx)W|ag4!@*VyIK<Uh%Sh5B*cLUr~$f*m&F5O2Cn&Hq8r3Yx|0|82G7?'
'X9#&Tr7W%CiU=ZX(d>w}<5Ld-AgJ0;`|~-;5783q;cj5$>l7ufKFzZ*=S4qLl|w^WcSOq`fU~Rpv-(cK6OBD9;Y(Lsi*RaE2PVV;'
'O$VEyYEdr;*SEewlTe>Q@I9UwNrDq;!2XhuyMPz$AvAyaUi8O`Jw58t%#smca@KNS`>5Q;YZ9Lu8oQbeXJVwNZ+F`%i$>gYDcHtH'
'(}j#6%=f$*(3FC<@_vu4C8VS3gx?t~i+8@r%mw?2MSPhYo)cl(#dVYYqJ)Mb)fpGH4hvqoLV~*z>$k<*FDG$zi6!%_Ulj5htuzS='
'Q8#mo{@CekdsW0Z=-B4`QvzvRt2-H;{maFn94g`iK%szIG<nR?JNfS-kHYsPeJc)Pk6@lu>aSfyqUucqELv+JdYTdliucjL$k)Df'
'%#$-vF}-gVwK+j9^>ea5zI5%x{jKPg?X4;0d+7`mend?E?d~mI_O_?XlHxX&947XfgjVl5uMCI+B`4$ulYi5<H$$=CS$BTF`N<D3'
'jOM~!?k0&R&^~71Mw6XE<_04kQf%D1-J}=-1(E3OGkfiD&3}z>o<zk<i>M06CVTY@xo|UmN-!MUB1RB*EB`9$v|RB$w7^80!@<$V'
'-sRI_w;_x5rrM-BWL;<4t?6xaw}#~S#Ha@93j%WvWlNsoA;bpg8pOL5v*}jd#n*XSSOg!ppSIOAp{s)5Uco~nS2O2-Z`M7j)3lQc'
'ogXmUY%rtlqcj#OkvfQy>n-c(i*-`pk{6s5iu%Hr0S@Qi@c8PFxP#WK>G9NmT-C+W3m;uK`5>A@{6>%B#wXcZt=cE>(;)b=v>881'
'+FkT#OAt}QZ*Q72%jDKY+t75^lF@fi>bPSgztavde}qM%wPA9-kB-&{62!$M+Sc(sS5a@~G8HMlnKRWI#LGN}1O*05>d}e@!$r%m'
'XEaED_Xj5@fmF>i2b*TyV<{WPr!Y~s%-Bn+XSo;O8G_li&Mav1%sqMPJ?Cmgs><vD6z$dWry{m=PM$(^JyYqv^j#<NdwDqXZ?QAg'
'Muc2xA3CGgAG^@mjqB@Xh$puCHg(zWt!MWORje{sn^~W$4zEwTtfWH&yksoRrH;JO-+_+T^j-n;a&Uytf|J>6UAh_tGJV=mvkjq%'
'vjwIHq8<}W0j13Z$UF9rHnq?usWb)@8O+~)7I$kObHn~rXS`HN9r2_$oQf)UTJAVcM&kJ71)}|@ET+H;0oDDh=M7N3IwpC@oY6#g'
'Aw~b4cJw@iRJrSUDX7_MCFgP5R^807KJc2pP1_L0hV>2lSDXBTy7fTZgM0*!o+ktnQ&B4o=}5k+(QY5~iuTf~6H^%)({_r>$V=wE'
'<qN++QaF?`zyMv@5cE5$(5@))agS$VEIVqIhRyE%+$&odVi*J0rSWxM3rBg6@dN@Sy&*$dOkMxCLibNP9n7mKfluzy3?2V+;K2mL'
'jL->&kG)`0t2B}rGe=&2(>l}JTGkMT!7=!=(C%bTPenD+ekL6eQY#1N<wIv9VtY4rj(^r*9;u@0tk~MY=ek6BVWHsd2P*p(!2C}b'
'p72f9qNF1#p-p$}iE!6mCq-fqp}sI>NFK5U6hQ){-e+zr6xWs;E|h|PD|~ZmTp=>X_O}l4rPO<01S|mIERRtglddw|mvyX0JtVm('
'TW1_kL5SO^aVE;&4-Z4F%3%m;csuAtU@wLBCrGJc%OF`iXKrw}bBPFap6VFgHZ+H>0W~M8wJ-w5M=7|~nPLdt&h9&*Hb7UD@hLId'
'GS3qL!a@F8jNv%TaeXkdbmCoQm|p^W+l_<PB=dq0q`>v+rA61ds>b<mJ(`p|Twm{E4S^XiUFe)QD%VLzc`~imttja+ga|DFLreTo'
'97#Iq!co5#<GgwC^mBf<x^tJ0wOX(<SSSTU+tAK_Q3u@&(i&Vt6^jV-|GBe`6jP2B0Z_Jj$fZbja#<bheFp}E9lf@~00i@pY+Z{p'
'w;Uum4N>Fl5@37}FmpRvP0h|lOae&*fIW<#Kq`$4voIY(6jQ}`(00;3!rVD=mb)kY@z#8*h~Hiss)Zc9aY@^1&j>x%)ge_wdNs0j'
'03zyYLcOpNeLYJR)KR?|aA=O1;e?MP<2LYfiw!q+HI^J2vlz~?IHNj$NPmCebR#<!8dV0zkOvm&-Je+$?P8|z=t%Re7KblFP<j)6'
'AYOcl*<x-I_oJqBFO2X!!z^c#dh;XE)=I1Vq*c}#@5QK<$y@X<Q(YyD1A6zqUA~o(p_-UyN86x}IX9f`WIZg-ZBiWf!+Osy6esS<'
'6JJ;uPmcsRzeCmT3j(mMUEFd}tX!lG3!i1%VLdt3GraM>c^j>Df`C>$*x5-#6p0ac#Hh$~rXj5hL4pFo(PbB#D5;704IfQT_(`Yh'
'DMEI{f0Lk~-QA01t;Do2NS&b4c}D=2ZkxDpDbknzcb&WIWwuVrC&JD0Ux(x@beJX;vX&~D9CcDh=!XgI%igM3++cPrjyph$E>!k@'
'HPC%Od{B>b6=C5JliO)`j~*KrWMy5_wdD2<a^8(LwhcTGOV}mM*N%l!G02w&+InqtOvV?N^mhk$*Vn8QiJL_P^$qIN%KVZHM!63D'
'XSPJ}J<9-tGQyuG>Z~j)aaCs%wy%&ds~&AS<ZWxqi6bIvcv8sfwh$*_2#4h)YskHRII3jq7pQ_6gs7m8MNu`nYqWXk@;-M^cWDpK'
'W;cq)*KTk0<S|$Rw%vXV^8N4LZIhgz7nx&|@zm^hujkO?s76oP&qjN4IUMW1V9r68EBKR;shjIV6NB`sVl7E?jC#sRoic@Xl1{)C'
'@n|zrWWNi4KBp{`we_PAD@|o}w?8Q^zi{KjfFxZ{m*rGTH?#O!d2f69;N=k#H8PH_p1l+HHOx5U`mOPH5w3B9OZGE4L6rYb6dWE^'
'X2Y@`59|_Y)7-d{!jAUY7}@abxp5Ex?V!+~OFUP->m6T@=h6flXvJ=YTOWfcY(-R`$;RkCgbL|#Wln@2)Pf@1-mGvU2nEe`8z7BY'
'k1S>q<F#Z;j84#vBY4#b7sC5t5V-zAgKut)<&HN5x8!*z?86Bl-8vJp#)pH^DjH#rpZ>t%a4^g!py<~f>oKX#kh$A?=(c`P3PWO~'
'ltC(7s<oIiY@d6|YcbH-rU23e9%d}fD0#*afi6aFfDQH<M6snx*6MIZXmX!&@k2$7buRr)9B{kPbIh_c>5WBzrS7`So=%ah;;o@$'
'zCM;0ShwdMbmu`BFH4H$-Fap$-&$*`Q&f_vcHoM9@XrF_yjdrynm;&y3>+nmPPyg_A1Q+LN}0)W#DM~}!Wdv12u8TQ{jKJM>#K$K'
'a5A^rSK7s#ti%@420E$b)*knSadImZK;Gxnhq7=?eb`a#Zp|XSDJx0Xg%Y^2!=s35Qra(SIx|>i?MievTqnY$+;9}9=$FF8AIalV'
'xjs{Ht{=GwO%bt%;Tl_PFJk|!XW%DWgD32~g;Ybbh<DViKp!y3!43rC#(Gd;s!C-TE})28^D@e%$g#&Sbkq*yXmJE&*jL^Ne%4Hu'
'hwf(`Xre2L>0@S$<<bKs=1x?Gfb%f%otC9xZbLKLdZFpyl!=JPj&-=8Kw0^gqg;SWwKZGb(;z{yYX>BtCxoYcNKiraF-T>x2WgE@'
'0%s0%*SARkvQDrtNVkZOAAa`pOmBKb{!yz`?J}^vlZcQ;N$n6OJ&A;r<xo)kLjp!33PVR)xD>!`JA`ZHF_qc7OLxKdbZefVxm_E{'
'PYCi7ojNp}YPd_^sb<<KFzA_ucpmc~IoJ?8s1L&rBkXwn=Xp|;lCq+oz?>kaho?U~SfS_M`Ki5!U8}y}@`M>?z@||3dQBt%uC!Pi'
'!oES&mtCC@mo{@(pbBH*nZdcXT%1o-pT`@!^j_6mj|&E=cHQk;^9$29_3smOl)R`+s`(b(_5ui0TEgY7U!=b6{*l^!&6{eA^*x*)'
'X286z8P{v%UXx;v@ETKE$jTc9UZPb|)W~=9C(l__MeTR&q0Yn^X6|ju{ebwS;n$ej!%<!tCjnU8I)1e-E3Jqn_MB$NQRVLhi12@6'
'WD6pOilql-l;>d1H2VcFVY+PX#kyljuiWvGGiRhrc*TQoDpAeAE0SFpp4R}->diUmk|~t0*BWvngqy#4NBgI%G0q2w&0d5Cp$8`s'
'ISCDjhz+U}SUn%l1&%9K=5I#*|5}?9;x)gK6y%t04l^|05Ky(4{l$_5bd#IG5Z0uu1P-Mtzy;b!j?A6PLj@0a<*$5?cL6|vcqiCi'
'BNqsncA^I8-x5e68ddflAG4azm|kZ-d-ggO-9VjS;<KwG6xd-CpDME$f;b`Tb8hGjAZ-SAiW36Af4U~(GhbnHP!7I!ss@f6w5JMT'
'*=kBl823$Ayj~ID#ju3S<$KmDbrgUT!MPR)GqC>_oAwa*W{Iby^ie@zL1bXYSZk~6+4HMEo3X;eQo?B;iR1Py$vlc{%mqrUuiYsY'
'7ds}AcCp2Bjyjqux8k-<qcf#P>3mdWE{@giL(34E*3moWFv%4$MCiohWr=upHOW2CC^O3|jnzB{LOWT#=2T+uYAk2Ivnv~ES8}C{'
'8ePe-5C;6mPC{tOQZo7vW2#TWpy1Hi0x8>;+)$2|UvekJwP^~i1#7_tuxRdNm3AW;c64_*E2{}OhfppC|3d3{_6J^<`u;nbGi+xv'
'#YN(fu3Ptq1_L~2Fjt!??H6?yFaFXt4utBS5>On+x+8YKwq+SS-_NJ~p;W8Z`@##g<Gkw2CN!AQD%x4R5V?nh2gs{HtF+y;)_&ue'
'y?d{b1^RwT6S=AwQNvEmZ}WBpQTt=N5kX&wP*2w6tmfY>DX-T!@w_c&q-O1Zsr)o)2ZEdFp|O1f=TL2`OP&q8s1~1e>;exM9MT1F'
'^Dg+g?%R)$Gmgd4R?h)Kq3)h#!vpaA_&{Gj%5FC3wn!~*ZSTb+)W#7GoH4*K<qklo)(ikiZP)HuPgI!=AWN^CBuG^?UH|4Lir}&o'
'#gIMYI4Gho?pnP2k8g64w3*aFO;wF(EaySJvFN;$Zs^Lwb3fdU0I~EQbZ9cn4o@>4?fp%x<1`C~Y4N#nYhwoCkEWVzlCVyc76;hB'
'*C_9KZv4T%A*H%kGKC{En+1>yS1N7?27j8U<@=Z$6OmeHS%_z6q?|YXJvn2|`hQY0sSBKmer19cV|mZWp7VH!!c_&iJ_Z?>bOB9e'
'RicLHh59rQUI2iF4s4|*kQlaKD`4d5kOT*nYdz2APuADSWVzFe;AzWfh@u?_k?wy!mIC{FF3UoRC(84tcRipVEy_-k?iO^AB*b<q'
'lp%_%q<!r^wW?Vrov9*Wj%7t*%H8mlo$#p%3NZ89$k))0sKJG^SVarw+1=Y`zzg<ezOL|=laLTT(pNWx<O#O>YaOC%FtDF#d3zT9'
'v;R6x(_jq&(2t@X{*Axhk)uDvk;qcWYvDbodw{5bMtPfO%{lVbK_C&*qZC?sGr^m1&V=AMYO*EOvLMI?E~#)qpvm2tR3MDrUzpN~'
'8l({Zluq`1?C~qnF1ZQwL5`4yah%Nw4O91t1plWy--(7LPBAgi#<h=U?l-dgBU-9<8-e0;mB*(eaQ~2Mf?oxW^a{$?X13NwXSAv$'
'WE%>7J>`vjimtxsb=ioF{YU?xRw1zQr9p)IySSg1>;q#sdhj6!043j?Vmc=(kb}Fa)5N^fhuWWRJe!fe<88ChIOoILb^TQ&y6j4;'
'SfCrm_%M4n)2Z0uKQ2Il<Zp1TvAUC`Gvi1~2o^<;5k@PI84K1D21$j;FA7;fXTdgfO2$3K9kq+V0;&}WK^B=b-D8X-)lWM#@#L%Y'
'3LC{2bHO(KkNmGI!@1_GL5NYLSRoNTVP?P)A`)$@>sZ`T;-op{N49%H@2jWku`7_5Mtta{fVUsNx~hO|NIGspKWr>}oA{8@MawLL'
'-;v~Cp`2$l-^oMjQl=o*;KjR39^o|0`OiX-`#`}`RN#vmBiDS^uiA+9ZeFIUuL^K>VB=hfK5CZR-LJlwn2s~^Verc{wt2&a#WR<P'
'mj*C22Pnb*`a_ZwmyD^@*X)FrHlG$#DIoAhQa3<nNjwN+O?z3*U(2AFV_sl2o)<lbo=pkM^y{%n&-T=$b+W-I%^GhHr%l$)?LB_a'
';y6;o27p9$nu;oVK-4>EcIfE<F$QV7|LrGn8)bXJddEXa#~1abzb1OjzNSMW8~byKn~~AWYNanwlIvwb#nza?FE;(h<jo_B_>Nng'
'8~m#8Qi`{J#=Ca=fU#&?mDXdU4Jy#vS1THfnaXDw0*b1AIdLHHTmDNbx#lkH&g5*}ttBQaUAYy^R*cCpb>Am9wOzy;J66wg_>Q%8'
'ylO3btEt2Prrig4)#ae?@mI!S9_u3lsyQok#Hp>v_6dC6g#byID|SkuAjP82>fmu~`ztfXT}{^7RFI6pNI`f@sbA2e+VKk!j}})Q'
'#xJO(xMa8`&g+4vuMe~wZ;@K0k91h8bdHeVp9G8k&rb>39t|I;sdg)ZZW;_FXE%R^R#IcdyyiH_(rBI(Vie94{3SE1?d^Ef)TlV0'
'otA|U0F`J|$Cr!88PfTLq$Cmxm}LDbpWJ^x9AXNzfVH5^c$>>7@NT*U&0=;fk~I6ALU%-#OfOqhfOGai?eft~cn4Ve;%6qhW+cB@'
'lteD}wTkho*ePSz^sF4dMEt|eNz=$OZ~EtWMFQb)N57;DMZ+2Bjz_Wm=8h~`QEe%(&YVk!t<cPQ4WwA&93Yu0y+pY11$%~v!+)lz'
'OCfI_tRXBZvo>E!X77tDM<fapFset!BQ31a1IgT_F|vS?W!Y|mnij=YSe+R3AwcMxFbk(x9)%a|rriNRfPY+Bd<ZvB?j>zt0f6>v'
'S>!_OY~V)B_o6bU_;C@{QDCxMaF?+YCq(#cOq7HBlRkMCEQ2LQ^FuiWhT?P@P^)fm13kKst435ftyn$9Mvo%xP}-`RrA5A;7fI#D'
'9@HtwnFj*%R=D7E-CmO@c~@sOVeEbE!%*S*eJO1n3y!s-$MndsNonw0!N<?L{2JO9?(Xg|Qx)KMtc)Vlg0A}}*+C7#gL(wHR72Pq'
'*GPhDz0Khy@jxc??E=nEwfd@q!}k92hH3#R&La`zo<_PoQDaOQ<uLS|sRu#YN!JH(d8doBvMQX|t(zf(mjWwBaA!XlHQ5J{h=u3)'
'G?8ADwHwN_a$OR<Ff}Y$u=b&UI3{F{vIOJQL-t&3xAiFv15}6<YeHqwIU<3y*cPs@7RNJ=fyR1X9n-@XreL>;StD?qzQRxU4e5`)'
'Z@Jc%saS+;*>AQHD*k4=Tt&Q*_-JwfW|5tyx)fwIcB0+yh1S8T1=O8fLdiw>7z%~0I(y~2t}QDw2%1APK-)NRlFp88L5#83jd9*F'
'>$??LfEgUEi&)OcMNY4$gQl024--JBBit+U-se}+r$|275??P6pCvX8FM_`iJ6LiI3Sjj|bL>Tm2%cZHln~U<&(3kRCy~i9S(9gv'
'YrG$5k=?Y5`^OX1CSs?s#stawKnyL!TjV2Z{CmB}!)k3pDfo0rYc%Xc7*QgdNWnL4s<-^ImE!|3LQHzKgC-w8{uFPQ;MKjnn}fTF'
'_jg`%R;21HV$so39o=a>^DPn5f9cL6v>hOLRqn^|vR%rl$`#zGUXu8;S!-14oEZT;3XIh1lz9T}(@|A~QB+;HQq<1+fMr?E^BBFN'
'uQXKu)N!3nw4VdwYGf@MY%U;kh#JwzRlrsP6oRf)lb5Jf6HQOj-z20BTHgcTV8#f`<jCA$K9^oT1&q<y#rV?-nnPkO3oq@eu0s13'
'>ePsT{v@OpA^XIldqi#AI!-^|1#0)*F4}(3Cc9x2nihY{Yj?6pen=-Z>MWHxO9<V1DkdE=SxQ!|h9+V$H5fooWv?=l&AaA0((ssm'
'42{PVENL<S4Q5)P%-LHrp7x^vH(j_TD>L7W(HLnpn(UBj8&yb5Uu_|Wi;~Kvp{;(L#AQj1k*`0wH!AED><S{BrMm}*3zM+z{-Y@J'
'&hM-HQu5%LgmAT~kBL)i%A@DOM&pNGY-UrQ6>AH_qVRX9FkbCu|CHQTgz8fEw$ZBvrU@}NMM$N5Sbuis0;-ei`7UU3_i?LL*W`eq'
'X6~D&fYkfb5rASvT2#^j!W*b6MTnwVlf?BmALe~(u>>jM3N7e?f0+h#Ik-#GexK0P$lJ|g+pzwBdm7OdDvd)=phwwnqGJnt+{sd1'
'd@?cbUHP4`n>@%AOh;xmK!wtwzx958F|%Z;u=%A-OA}tC4_i(7t4MSTB!9?ji;~)MB*g5WXw(#8^V;?JLimeS*`9*5x*6m+yg&v_'
'wzAtQPbgTOR%0ucp+Y+1PO;ONRr)?2o<PS-`>xW&t+1p~PL~96Anlcjg6ac#v$}Q;m^H3&&E|p(2~7hCk)U@C6yDQ%S${zjgT$ka'
'@stoJvUG=iJj>zCN<a|^chu4WC90KYePBm4>HlmhraMBofhW~h<^^gVt2M{5SW`Z2m~x5(S8|U}bXGl}6)bNnLUYuJU@tOQ?mrWN'
'Ln@(igW-qeuyUR(`^PYy`AwNQ+Tv)hCXDC}nh?QvO%8(eri?~!9(b!!!ubTa+>DZfG=|9^PByw0z%_pzSEl^I2OOsJidH*G=u+$D'
'6;h7$)LXBd{{C3i1VF?_;~5S?E51_>pd?J)vR{CfQq#n7$b<eUD?>20pN~JG>UVYgw{sz-N|4~xO7DzdiFo%70EDd|l8Q@K^7_Ee'
'_ZRAzg2UB>W`6tk2qt8=LT0f9-f}R&G%v><A&ZIS*R)po_}QS<^L@eRlY2n$PHI*|2Wnvc5_cmFkz4CVAFyfwGvogJf*{L1{<)@G'
'|B)HyYz#phK}+Whj8P<nn{?YI7JZ>*@V~ZDMge=vmH{}Tu=1DyglhDv<m~0`!0emKtc$J*P?oJM{gL6OFL_s>a3UQL&{(UF%;|G_'
'8<k-!#gX?CpU=>y&-`m_qI{B@bTOJM3@YYZCIxZW{2@lfjcGqWsvTV$HjIs>Q%oC9MvkLufq*eKB;N5f$_7%7L!$al<RiT;_49-n'
'BUbkiy-Z_n2}!lFC<s^S8b!V5Zh<=dDPvsN+MTbO7Q?=`1qj=vPt$H_^d8|Nax&?md~wRX&|13{Ql@2}Jle-8V+q-{)Cw3l+0d92'
'F<+Covzs%U^2qc&7C`T<AZMtJGvpbG93wFnlGd};9E^l3V+7gA95cX!$8GlnNO_ZjNaWiZn+A<42GP4_Fl*pq<gmB<s*l;qPwih#'
'9AmUtos?`F{pSj3o8frT3+=mt$<LVo2qZAKApKLpzEJ5Q2oz?eUE{K+@zS&4T@B&GCI^=stsxBGwEhcWe|50m&I_d6`oC(oK;I#l'
'PQ@wn=PbQukzW*akgv(>@}l<HA2vo&7^BzgLLfc@-Jv{&Z5=ae^2PaB{N`e3oNN0`PAToz`uv&i;ubceqqHE8074o{nuYN@3`1H*'
'#?$<r#c5N(ZlY~1W$3uT1ugb7DPIG9KXD52);X~xRcaA8kLqzG<t{r)Hu&Y%h*%m2g7JUzD{7gkina4fu7fvsKSvaJdGPKlJ;Za<'
'&7m1saC2CeqFPek$)`_i`7X;+c~yR#f_7qvCBD|m_BDz=2U1M=lIXMV<xAR%5DV6gg&(p+=V^2!=w9=n5=~nw1<ExC`%=inyv>)+'
'enCWAG@cc(QS1oC%sas2<7-K@iHCgD**)2Fs*83ycN{{a4TtTkR8i?4Y(}bfbqWul-p)TyrzKEbdIn}9e!|@72vd?JQ2ICTbO8R0'
'?;0>^W>Za$t%)xE#<~l=Qt?f*_tejBNwnop7&x>TIkL6VU?Euf-VBQUBTn|gdqR|*7(p@k)19yRd$5gS0cX}D0<aL;D^KGYw*Vj~'
'Bb)N<u@Vrqrl4!o$jVviHma+R1Yh9uL#Th4c<vt8qbNO~J<jE$>{}nxLpDuY|BKo|B}?gLt5BU4ye6G9NaM1bVY@1O5s4SM@u9A='
'51-%%cMGrE)4&+M=;C9e<SoaX_K4bqXE7X&5mCai3TgEXUE+1__<3mLaPd)9gduOPfpNSCIA=#o4{&RFQk^;}V7G(RB^P)Iv6SW*'
'Wj)PwU~|+?Dc8=)VrX5mS(F7gUrLM1$f)LO|2MsKZ}Q0J^r#nUEJYKqtXxEeOr;LD3{e}n5k^AZ@Z}F6WK<w10X9(OIz6~fec9LQ'
'W7>S2uc7tzZW1MTOHJ2b#LAfdtJ7X5XdrybdJ^opgYz=4e{qTHEc_+EVYCj<M5hyt0x1V$kmC6271$Owz!E-pC6T;%huj^#02nrI'
'1~cvETwiwBPF7Ot>@ga`cZvD4qkSBHg?<KppuYf|pYu{1dlU}G=R8N=ctj<s)@ARrBALYxHu(`WbgFpRVKHh4Y$z}0{a`ATR8D~q'
'A;Y1hKSj;il*B&VKdcaB_ads?L%Xpa2u&Kx$>Be_M_&#wHTR%TRYX_(3+N6Kizg}k|0$r7U~5Iel&P-#^Je#E{-gx#k-k4KBHF@K'
'+JrDTXGD;R)IWU|NiDKi@iRF|R=Y{F)%@+*jr^spCScJutH_nmm45{SWAweijDZ-(vAtya(0DwRqRtO>_ZpjyH+xzatxus1mI2qo'
'$?SA+#SCJsKs6-7MAhjZWzs1v{0bPvz<2><wF7S(*_H|GX4&;itD@M5_4a?@ZH?lvI#5vhKub-zirs~@RsLc~a24<o<WwZtN0J$`'
'#MgZTcA77_!Gr6$v-~?&y!AaGB(VV*tq@qfcOkz<cB2uRUTm&XW~+T`%fi@|(_MjVjoFsC<$Y`El)42v7zo5iz7(kaaWL|bg{F(7'
'7!@k>#@|XM(qgX$BRwei4{xvMxKlRYwcsQBh%({JySeK?g`#fr+#|51?|(gn0kvoI04{3fX&&lByEl|__X^9zcHYP35UYbok~>~y'
'Smzh3x2Mv66z3Ed4-zXgwfH${T|Ofb3?I!arzyDSRxhbt-bQTZ4+nGd&<#1oAkfu{Zq#%oVCU5oxwrUR-}Oa>{(9Ej>dJ%~4fY%3'
'G?6|?T9)V6w4^JKjS@))`yaAPF0KdH%F5XF>Sse#i$N|kV}NNyKBnN0;rF@?IFo5uazI-(8rxMAF5O+&AM<LdzmejY>;a|X{Ww^8'
'|EXQ9Qg0>z^gH(7VrgbHzeQ#F2k)-<-Z6(Ag&ThMaxVtU-WJCtr{q&PM!@N_d!rG-T7i|-qHErU+=q#>W{yIK>~L{v1NUkdk`cW)'
'5b^~%C4PDAd?eU2WfE)bKsZ`FUTbGi6+_qLPiAr)1HZBG#HNml6C_BRmlFYmiImfF#%b>!nrGUk|HJi>S?N7P(`3<(UqG{f@tX7!'
'JV?x)gVZI=wR*EW9D71=T^$<wCOus0F7-8Pd)%^4jg?%e_EP3w>@+QY2GPZck)bS#>T8J-ks|GdR{VB*`HY4-$HK+i>0##XV_B+b'
')-jE#sJ~Khi!%xJ6r|WgVBVk1mFR#tGZ1aWH)wc$ONq(-T%f100`!)ca%RdO*AYYYZ%mYwH}_+2+{m*7JH@bM;d-~xwC9gRaD`%8'
'0w-_&TLyFoN;t*iPkq6&^mgy_ye4SQUJ%Oy@x6|4S|JwKzQSqcuP^nz(J;867cS(%-LsjX3bVWy1VjC$)l)5!%;WXm_Tr$*zu-jG'
'sofFn6anH$#|Rnubt@xbnDa4|Un*MK%7;z<oF%Hv>PkB132hOvg6RS=LW{dumh8Wo5W}$)(xv6kJmRf<AR^^txeTY-fr**rJ*-0R'
'5Wob2`hg-wP#H6QYw6rOAzK^Kc*Bb;?vNqp_9@N*z}3-jIsEhczfRE#uq$V?5{k|G*>SDcaAZ8kF2m*6QZzW$Mma03!W*qBb}>(F'
'@An6I(@e5l2<WVm>K^`>1CQTf53bO@oht5$qNpH2dWGDTDQV;P%N8#JlYp%krT3a7piG>>0zgZD719JywFVStJt!g$Jc?e6mf%=J'
'EQ63eVS~l-22UA$$Iuk7{*4K&j!Hy!IG#rq;eBklLg#;ICRk6KZ%)ZQON-;W16X7+mkA=Vz#kxcZY;LeOxmC=^4QltxJ>543D3SQ'
'(ilB1eh|HmZ~yR}iZ2y(e+8X)?@mrBDe-f^)XiU(<VY^1)|2mYKn2^kWIpp2q(f>JZaU6AzvsX`o=CI>>O~?#TNz;TTA{z+(3o@V'
'i2}})gvW=`)8p6NsB4G#x`$zm^uEA#7T!?IpKs;S-@@|=LPoOTEt=X{!~wMJeVtmU=SyiyWa%^3paOp?c%$#!m9I`nRw1bymZSsz'
'uYqsPcz^2yNi0ns=>*t>H`_p67VL~0lnfF}l#cQmmXD@058XibIa4uC4?Od>?GZj`t6Dxl!TtXc6oT#u@zyonbY$LX1?RM-J3jq$'
'tWIwhP7*8Xk}E=^V&aFRlMPsUikVOKglCehcqH<(&2BFvGOfsi$Cz5b<V?Zs%@eHhcQeL3mRsZUm6a9`+;Iz;9QF=Ao`^f4$sqnZ'
'ys~S$V`s$^>X|%w9t}%HCtR{q%(-`stb^>w#Oeu~3q<oO=BA!+7-(XY(&F5bd&t|SD-c~o!eYW|;eeGyzdHp*lur_uI`y;COHlGr'
'bQ|6geZf^ZYzgj&0z-WF?s=QTDE$UX7qgcnowNCN!y63|C=*nl&%!8yY|c}%wQ`U%tG&dg3K89^1n8qpUrU~7J)rgRawA8!K$KQ>'
'OrS_m<+#JcwhD2_v~9xxY<FNrVpS$~hV*|oK~<~7J*ldH@*m^8V=?RwZ2BbL>jE5d$X0zQYc3P+EEl2mNTt}25Wlu&Ep+CS*=vaq'
'#1+%?76FWyj{_L74?<Lk4^NW2c!ZqgSTx521<`9n9?!FHmZ-3g8o#h9af}EWVyGXXCV&L>*=I>9%8n0W{LK6*wO9j%?Hp-1==az}'
'z%hsv4D#5C99BzR<L@eJt$Fr{<D(Yj!yy>)JsDUc?ULHMA84bHG`%|gurl+Ey}P!G5>X&y)qj5QaB-U~956KKnr>4(WJy(oRRlgG'
'VFqGL{n*~u+KD$w!k5VT)hsS8hl&;l9BKwPIDnawq9AM|=e(y&&!&8pOUIDYC*L4ycv#epXW{$LnnZpat;cu?aw*irLde?j#&*Kq'
'i6r*y%{M1`a7|_<X*1I5IiV08zl`i%bFb@-@20V@ArsNCLbBAVLK<0q0I859o27IwspB|=++f8At?OF`@@ing6{E11OEe=rw^qLp'
'GHriOHT-x`cqP<^59Dk!mf9>&U;Pg_L%^t@o86djnhr69Ztqk>LC?T>eIJ_M!9#su>eiUnz`Bhog4j9JwHqSq1p3p<<a8)GMHvcb'
'!vGS0Y<H+UG#{>8u6}p}4MI9a92aqleA!_rVW9PW?2Ef4+lY$`C-erA*djw3_b213`Y((!qd5YG6``?kqVb1M_2XPKE(??zkhZ!`'
'&Rqf8WW0soWq&H-Q+HS=Z~nA?$j&RQdaK{Ky1l&jN3Q@3aUVH+UhUI~O*OtcI;_faT(S)u?yY;aK3YW?i}uvNM9hz`M9f>(v{G%W'
'Gb^@-(US6+gcLJLC~biV#|cJw%EUe#0b4X@D5s`S#il&@&EH!((i*4mOFc7MAT7~-m4G-ijlSHSHsZn`xo`t<8Ki$t3i`r<oU-~p'
'6Z$wsLlz}S%=9Vm`{kpnl8kKXSW_|foy%6Hml7|x(w2qXqqv}s|50TRB7eRu7q6(GF%{kUJ&&(VB0F`HcvJ3bRceejvM-M3s%UKY'
'I{5O@pGr|I)cPdLX>+xIN#23|&=GX-6+EDDM5ho-*<_!Yoh4b(O;gLgdgswYmV2tqfN=mKj~QinhowJCekFcM{%DBlat7%r3r3Cd'
'OEmq`9X3qTIYB}`nz_jl=0`Mi0EN3t+dr{EJ=qYw@}F$QpEQuOK>II4>_bp5Dbd4N9RedT)Yc-I8fFu@H?RXR9UM>EQF8%wUlV{F'
'$BsJNbEUCY>gf#jpQfL`PqWMmS+<rSSK6HRmlFb8DQ?g^(e@NKTP6vL>;yl}?MW%AvUgU}GmxX$a0UDt5~Yg9t+>&1H&drTMrE<#'
'(kNa7Dur_y*{Oxpb{#6rBFnQKfh>+GFkB@)xi$btOH#t>RNfpnzl|n`vkDAn%!7+_k*nMzsMvx&{T7yHh+5myAPH;9!k-|$x!&C9'
'ulwOj^pK&8U9#=xRf?JVm`gKl6YQbh$O%a{847;fBF28plpkI;gu$6D78At^h->xZwE6&nac1OVDCX+PdW<kPqFQKnFJpjqM4n)t'
'-t7A}-0Q{#F)rD@GEL@Te-&BP^<bdIp^O%9%XiMyVIX~z(fx}}Oy{?O9YyhLqw?5VQ=XmxQpHaMJX2f$l6Xb<V6S(cEU{AFtdOBX'
'haUs*4X(Bbh3l;Dg?g0(=>u;Wwj(ZkE3v;ZbxW8O2UtTTV^75CvAO9HiArt?((2$n$c;7QJ}-<4U+5^yER0l$S~Ft8dc!4Zjwvm!'
')~bTpLbBz?olv;9D+g@bzzlM!3g8t|9Dbi*C6YAeCrajjZg~u+iQ=<+!Fh=+16B@d_?#E{0XsDj13cBNRZ#h@GWnjSRk&_;5EL(o'
'YaqE!b>&!k)TPnoAl(mT8_Htll7VmSQXzGarYAl>OMpH`JB}u)Dlv$)Zy!t1Hz;;3gJ82QJ1981R`7LZB#bAyX>T8~Zi`UXX$Uid'
'G5Uz36FU1v`_^DBec@g633&gI71<JxX^HPUjxQ;MJPWSDnLwA*#V0RV&Bm6O@B^#kFJuO}3@QOUmH!~m6*}dbM53V~v;D%FL8<f4'
'6l0t`dIPY5UFOT8O-TbQpbF9Ox5&IN5sQx-?uJpKc??BV2_)0|VY5IblaZ=1?YV)jPhn;Jvgq4H)|7Z08Hcfc`YA?%ubn;6tNN?P'
'!%tg+iY(95fFO9fM<8i3f0Fq7^_S4^zB~mSKO+Pdl{H0IMQ58AM{Oy-i1;n~uf`Glw_kN|tvy46BGT;OBs-zsBnL6;TwX!?#(%Se'
'cen8uX<y)(IDb<-`7J*AFx#<Tw9cG))KZjdCn16DzSj4bE6S^Cr>enho?j>7S`pp--0CxQY&J2H%%!-Enu$bWX#p@uw<!$2vuBYo'
'$s{E|O8t{wk3@(^)6~OkicaP24+0%&29|T2)+rbqDDUk|GIb5pZO@=uS3%LDpvs2C`2!%5uw~){F}FA&ev~~qUu^D?nK5XNdk07A'
'{$C8F?0ryP7j@=K&MI43c(4eOWXq=KP|4uCj$Sy?!&m+gLJETCJ@FT5^G`v%mzA@pz-*G?$rDseD3?;wYuK0)2MHX`!eaPn<rSpk'
'QV5Ds3A!#oms~D#E%v_nP_jNK$2Zhh?!)5Lx<vUYm{?xLJTZb^rX+u3i}tYXT9v^L{&bT{$g(zYZ!=K(tHNXTRTIWyPvt<{a%O8<'
't<{kev;*vgl#T)WMMm7_MwaT{HsDkpC_eImeY*b*E&B00$AuyGJYD}f57S(^P@|{sqy9z<K410ctj{%6_Q-%x<X?-Df5`Djc!b%u'
'2++J%-))m$!i&VJK&Ijpj(Te^t#rExACw?qW7tmU`ETt^_uxxUMXTS4wyYI$h{9?vwz&Qv)l2|K^AN5q0-{XW<(fQ-Rk=v1PqBaj'
'7MB<D<KH&9v)E2gRKUKo9aAuIVdb?0sD))X#@%G+NSkkAGFW4=9;~Ev><7IqeuX0*@PoLP7l;pCMNr@wBzo(;7X32aP%DBPgcDA$'
'<APrG60W>Tem={kw}6t@i2y)s8%BHe4AAp$UtNF4yMJUIa!a%{3KI(j)HE?g%ViQ!<RU_Qgh8lZO=3v4vS>BjR4sjkSY4@skaXWA'
'JJ#z=GaV5lH<H*}ZtoP4Ur?!H7A&v2!l|sLRVGR(DLFu}-_3SLPJ26Wgx1zN9Couf@fAC6fn|aA(5@QMk`cH2-W%VMU&s~YTpZ?<'
'u=T?TnvWQ}fcM$1<wu4PBfOKFXJKP^xH`<6(g<M_NwwH75ay7^po*2WqaRbX8N-vv%F`qL@TK5Q=72S0`SbaS`DB8QzTB&+KE;AD'
'#B(4a6Lqa|%_&l&W|MF@Wcg!oc0y<xjLjMU*~(t{wuJFWHqBT%OgzbzYkePdUui*FZma=1BtqUetdZYng$_^Q0QKp{sO}bBMc*>G'
'!Wld=cZW&q<EeGU+zWrUs;Dap+XUsz@)O{Q>LVXAiMfcjEoM(mt{+K*n|yj(5+-b1(KZexS^PK6K8&PtX9924t$LU54+w^)fq?jJ'
'rVV+fE*Ue#2u>|SCk5BB3yu>wU6kW<&hxH*b*YUh=r@0@gqZ1%U?rCAhGB>(VZ823YHUIGQ}iSZE~z~s@SRI}Fb;MfcAP0m&JU9C'
'nF>H#EJhp}tO|w6mFwfB%=r{pQ=-@aBK{o-P9dsf6992DpAbInfIuSnMqS|N?(X|a^uJnGT%Zo})Ws4-KMuvGfiny+*6^EqF-AvN'
'<T!SR;T{r@#dA`Nm~&IeH~YEK@u>3*miBw(ZJOL(I3a!Wxmf{$kz3e~J*$R2C}4rUlg;QBOQ|g76lNS>1#Ba$tJ3Cte9k~?5L66{'
'lRr*W01O8-4z2Hc!`9op1Hk<mo%sDnLaV{|^u!6`=yU)#6Wou(4nf2ZjIPvqi*y%9&@fj#AeDfco6rDO1ug}yQ39(*a2{m<D|)1)'
'wrG<Q<75I#o!fOEBfn{$ZTz*1M!~#GgD8|~yRVxv>9Uh--}vRf3gk>n?Zw>mC)1U{Ik-S%{|LXAN$AxSsrDE>+gBmUbqW<A8tIYb'
'k!<c2>yOJ!iOKN^)Mhi6v<d2!Z!Vf)m*zeXa+CBEu6>{1KK_1Dl_CW!#{;VqA@(vUUe?+f=r)~9zhu;z$#E-IWYBBI(aWltb--wB'
'5!be!SC~XXGRkjm-KLk(zY5*wzgKQC10)udlqGJhtei%u+`%lK;QC^->%lC5o=@Y3*z0r%6wSJYjaqzT<kG%Q$BUNE3e*2xhBfsL'
'5;{^?^9C!h(P=|=L@fX>9MuX#d3Ry9*8Hp%$i)Lbj+w;THB@KC{O3Zxx7(<=Z$B=JzS2tK;!tfVOAKz+F^O#k*)v^j2S1A@yL92+'
'kFMqk0**=UDQMU92cWu}9m^1OPX>^7z1{8~HPxesE;eta;OIp_a)xw~01YgZ4~h&Fw_}Q@17E!pyQkJyg9vSVF!*Ck*n6M;4gLSw'
'(n+>rM!#qY3gh5APDP?4OhZQe4~6Pim}>O>)7)x%99Pd_t$vxxMa@MwJ=>?lvI@ce>={=YMJJ$5C3M7y)*I(lRieB<GAIv$BS1{p'
'?V~rzHPc+1bU{{xj<co}2qcZ-2#sAxdg>p_@Lyydfy;>ZZHhG_ZYn?bF%+qns#EE_pw*(o6ZP`3W~(qr8GsiY3$b6!$#CK(I9mf7'
'GNK1gS?M5E4vJOO?=p5%mTey}*&qI=>X9VJA|;*DrPDD1-yaK%|7&~ra~3Mt1BwPQIJNwQQdF5DMU?d1j?5??+_hK~qP4xTm+ASb'
'udR3S*hM5g4M{5opvA%7@&}DPtT^IS!6E9D8`8RS1484uN6Evx7J=byP)uoF9Yxn3&kEE5lr=*a1s9@4Gh5S^65PFS;WH#TL(e`e'
'oB_;QW#W07sFo#0MLg#)^5!(1uuQ2C!Q*%G)o^&OxdGAw_JV7@QV@BN#lKM<r<UK^oB8WIS69t8@JrT%p`9#0BFSo_blL(Gbq<f@'
'7-|`|OpOFgP7Q;UtCvWiJ@Su)>lyWEQ+@MVIZzF*T4qs|tu_~CqjoQA_&nCv>J}(-xf(vPO7f-X)<4pvWuUE68@U(5axTjg6wZpR'
'bT2|LQePNa5Cbh&ItO_l9%sn0zn*_pc2h`V65OzVD=W#B-_OC~TP7wgv{#T{zGo;X`F5q)4%>_>VbBL8)jJhReR8YgJY6X!NbsHf'
'{r@bBNfI_Hc~U4?E3R)~9H4MooB)vSDs8WVF<=wpqP=;((gU*|M}1L9S~6@ay8bo72=_XfLo6kXv=K^k%Roj3bp@%9N**UtS~hG0'
'`_yK8kgKb5xDlq*6>39jbQ1~ydd=sCvMm9}ObXkOZUUd`Ud8RZ%l3(#9hF;iXA}wiPj*&=z*D5RZ5%8?YA#F?)mu(Vg>IM$2#v?V'
'L$G0GuuS2K&0(m4rp~t^O9kmxAnLAOTc3DfBOBv-?5NOaKH=U%*513q?#N?JkpJe)9Db0wF?G6t(^WufHZaeU|5R^CDwisJHNVG6'
'nO<V3+o?EXA*f2Q>uyq#!@AZ_Z)e~XsH*)jCcL0!>1LD(?mGs>VMF96h@2Hd%c#j6pSpVI2LfPu_>*zzwCy>G*^8^>8&lHgCEpnS'
'7B*3Uskz2lu`a=))awW`vg!nwk4xa|=CC#as2={JX|~OFk>@P)Tgqm4h`uT4m?|n-X4wfYy7}_OBvknUE+i_O;v@qiokr?gcEB9R'
'eJ_@DjHWAWdF<BGI(tQe-4^a3DSAW8-0*l-K{nKFREZ4P$4e`A;fb^lAx#{ZXmQ45{z<lPd->ApCKl||UQM--Nw!_AGZlmKas}Bn'
'ZjCWXaI<-CoYq_vix}78uH~L+0q<T-iWS2y!LX!^lHBd#%G{SPA#+1;tUXFwSIpH>I%MLT9#_WX(jhjrbZ}n$?Pqihu`Hgk17p#v'
'Y1R!h;z^4U?(06`R-wfuPk+Py4eJ0C=Jn7eW*Y?&)`8;m)x#VEa^Y_QT1MI($<;!}4{G&#DL1oONHp>1HJ!i{{1&r}6Q++C=FU=W'
'3^itBl7VBUMu(~XT>Q|}#vFa&??>5YH5SnKfF<g#=GHz#Tp%%rc60m!2v(7rC_G<O5o4r*LRt=LR0#DxuJIXKm0QG4oN6KL`gAAt'
'5rv?{ol+xTBYhN3?|)`RIqBy&fBn2-q&(xKOPSD1N$sv~yCL_1=dzgT?FH+9V``=Lf%qOtm&zijONac}Qtvu^FxO?6%9H5PA+#Yg'
' tU(enZMV`9uA8rfp(J%CjU@y~^|>?X#{Q_drSg*CQ@B4{$4Zv@AB5-tQnjcJL?5n(BT`-2TatR8p26;wgP@jTX|y`!h1LWW6qw^i'.lstrip()
'xeZzwUx8=Q3JN%Sx)B!2|9EENW9pr-<O60{aW<E>yVTp+C52p(Gom@pxW;I8-iiH32KDQ{xF0_W;5>_23<V|RK|;_Eh4w8)Z1AqQ'
'fKYzWvsZh4?SQdgo&xE6vH;rGHuMX2tKlh`R8@c?sv)0gBV|@FMG=AO3{y}Cf<^h7*ke6$_~OOI?!6irq&5awg`hEU&Sk`KwRG8i'
'aJf9mv==nKt{!1m9MHC|OC&K&pGHO^E1IV-oI)|7mok~wcJ1H5^>M!5wQ8tpi=4L&etK*T`o;JN?)1yOy5~yYrtE6JudWq&hszE+'
'<hR{oLPPeK6>;U(g27q%TtKN*gm(%cm;{YM9Wgg47(iy~LQF4rUz!9ArC<YiVab#qj56nC9N)0<*bT<VZUgiU)dKH!<Oq4#%aiEG'
'hlzfp-s)USMYW))Ad&ah*P^`!8u|JQ0{6RRq?h6Us2}I$xUbhMf}!ni@KmOh8xw%_8d1169T9+QO@W4_C(1-=vSfl4<IWzG`=c=b'
'vkX>G+EnMDWeMQuF5qAN6fxMvt$aj&;MOXbCfR2aREjd3@u?1fWDnD089VHoB1*X2B!g0gD9+;ni5NmcLC@aM2pNg9Bk*O45$WFW'
'cXy@`c=RF${A{0%UT|GbjIrOFP=t@;Co)8NNMwXTR~5hHDGaG3KGS5!2w|EIs6x87;n3yF_QlK6mISVQFospwYp-^WxM0_?OTxz;'
'At&vYHlEupg%(ahls3Z!D*3Upd@NnLkK$0Ju@ee3mEw9|xnG5pk@5Ng=1I0XpvQu((l-Ys+-=;3OkgbZ@eLam#FtyTA{XHm)nI%J'
'&$}4|q3x!A<fK!|0j2f*LkB2cCRG@?IT(y=fp*CRZ-@nk>%<v88BfYK>mWUN?(1=_FBGUxc5}duFdoQ>O3Gt?U<Q$+z|ZUtY<a?$'
'BkkO~2u_a)5(<h1v}(3DoSM&daHPeN5O*|{r=I)H@KrP!^QlwbG;N@7Sd<MyhF(K2{AiCP6n!A|Kk6`}r-RLtQcWe9?gx77i;B|7'
'kik(9WtU7?uylqz#*RSzMHsYP75lf*b!N#rmQ?082CdtZBOjQcpPn(YUE%;HoSkLY>Tz|W7)MYk&~T5(1mO3IaMisl{w6P(_Cl8F'
'*_Or)6Daz%2g8n2#t1?~-Ix3~hpPeNxk<A#l~Y3g`xD5_%SZO9mE5K1722R2<XB$fAd#P#6m0L%`C03VobASTXaR^^spl)DABOD_'
'YBBJL?L{9N=a^jW_@oiEIAwi{pL&gFRvC5x2L-NTwO4S@L0XD4#Vc;m(@g0}gdkGdBCYzZW@HOSGR%V;#X{n#Tc0~valGUv)+@;|'
'<Mt}DOe}4lXy+5}g$%Q<k_|&$65>U@mdNqnQdE>DG;vmNg3Q_H;t7Fk2}OecqXFX+N8)j*@o!^#wulWWadIcrM@xtBWK@*!Pmo4n'
'oS={&<V`w72Dy@yP2H`Ky)l)esk7?;@%X{~76F8Q_*zF*L{Bn6bW+T9&piWIIis@;*Tc4>fp=ir?5Ca_w6_YW>Fr_#_b&T)uz&wF'
'5XXQ|LZ`^&t;1mjh}fN`gur5##sQ}U@fdQrhx5ikOy3itP;1Lj>l>nvlPOTsJ<bN38o-;w#06wu?a0a(Y`>vO5&VDZaj$PMD_4tB'
'oY32LS_+~a#TwUPH&I*(UlFgMckj<%vw|o`cZw{FWsIC_ihqJ@H^w6}!}Q?)Q|iFnPVXpMQSuE5O^ch~w7lz6+h0zGvkiKEGgMu$'
'O*C*9)E{kr(x%w>7U#-MYJOS}Jt32n!v_aqs^*LH7!TTj0@FiV?-1ooO+yvrny7b|JT^xdpI2W{&s7zTdY{ue%@-!4X7~$7tUp79'
'8G`3S?FdV)gB9l>I}U2Eb}TNom&(PeoK>iy37U+hu+JT1LS(ooB_xxBHV6zhK<o6$3hC$=HnAY-KBv6uR3f&3Pzw%$CjSDc2sk!f'
'c2URvQ05zg+C>RHXi+XH8>^5n!#=Z$;)R{F{C!H!OW2Q{se9hAf>u0#0z4^EJhZ|+!wSJc^VaYPm&P+gb=+ES2-nIORP)<`dWiuq'
'Au69a?F^XP8#h}`AJ5!(XPirw5PyZ&&O37@d8?CD4N*_*_G1WrNsG7kxD;Dar$qQ31Mm@Bc)vcv7k__vpZ)-|u|3_b;sOt2srP#b'
'`J$!*olMM7)1MD{f*1dL*%a~h%jLQ_9>cEu$w_jsctk};v7uZgaJt%Ii!}e}3<>7y&^`<I8TY<X1W(ud_lEpwlovjOcb<(H!(c+g'
'<u4IBeJBm&<R3tPth>&4zi~PT(5lPW?5f1v{}xSUo5Ys>2I={oF~~OgK?9jtnT;KDkAbW*@xtEW4Tt;=ncYS6!R`&*A!1Q%JA=z&'
'5WB3KCoGctdIp1X2{i4mj@Gv0!@K*U_%9UOT`{p-4v#EF&smdoCy7D<bJ4bM2xF-*qPTma6?DG`IQJk6{nm%r&2%Vo7p=VYAd7Ue'
'AR%ZVXVTsDoX1dChp(XH&M^z$T2Ifl8%8ZM{9~b(hjNhYk9-#P(X^tawJyjIz8Q84j*H1-y${kRq?r^crh?Qq4t|W@3^gG4UJNVM'
'zyz5(!ZO_~>xi?=DZQ$X6y}aYhGkC3Mu`Q2Vd8R>1@Ih*=9!64J0r;bs>1iy7|SFDxkC)0y7qpWuASB3yH!|=)3cY1-v826?J2+F'
'GW@K_1+QQdiKkHvLRR|Aztnteh?Vb0QP4KQS8U-Kwjg?$exqbfD+Kio$7QAWwanosj#giK{51}4u}~V`EAV}nI|p}OF1=m6kQgTz'
'OY}9g>Gt|a*0x!Kv#FPe+z_(sswgZRsJ2#Lq~it>1uKH^>u)mAJu3^+fUW<3SWW|tOB5YbRpm0=(cwD;X!}l?4Vguf9do-b4D4KO'
'%Hj2XWWiHK6m|lJAY0KN!%)KEH4!}ZNgU5QdVXP{AC9;)!(yIWB*(POA0P*fcLqp6LxR#b49K4vG2#(Xp?_qDhc$MLd)LHTug%o;'
'OI7PCU;=u?$lB8wCiNY@^|nXA(@!M+0AAFJp1BqNhQLoBx~iU=_Mx4kNOH-@=KV2G1s&_^x(PEOrx5t)Wgg_5`j)x&+XziL7kA_|'
'B<OG?B3yRd&|m4-%-Av8%Je?5jxPnPMMGxc_SHsmC#1HyT)ydbzpVP;Ce8~i?CBy8&l4=mWy<2%a_ZovxkXQbNalQ~PEEG%+8;lO'
'2G_m3<<2<2U!QZ56z`2Pg7W~?F<jm_9Iu%A&62#oRhH>;Jg<@e9AKp`resl+M;^mc_5)Jj#Z2nc3$3QgXQ+Mrak2T1z6j{KLV}!S'
'e9iHLovt)=d5O0=U}{MgEf5IXUwo}KWwY_D8~YVxM%rXGR7@OVA;X1C=4&d8QR*Bj(vyLr_79Q;@|&wkYkm!-UPO}OWWqmST*TsI'
'5Wj@uPb-tG3cgh!F@da!-kjI{n)EiqhV4i=rGBR2Q#YhB`X|#WcOHq!jRH+O?c{efL6_cRPlR1$hzSSKuYK$f%PZ$2Jj?I4XoNU$'
'iZZz&6;FMK1xcdMVFXqqr%cPK5MjvP+f<!Em?D>nMW=p)vWD1o;~{EA*+-+kc#lI*=Sj{tUY6?AWk=EMN9#PGv(m=^RfZ5kcE;wN'
'C9^izxuCaUYaZ0PfL+($=*MD6B_sb5$P`+c;<!%Y6;@hM<;Hv{R|bRb(MlIO@>kHBR!urhWLQf5VLE}~Emnq}qbE@ya)p3{Y<6x6'
'-h#OtNr|hRL3RPt(nDG&kX`Aq$jz6B5BZ$iH?Wi(l7g%4_i?FgVsi3{B}3NjBzLhpQyR!8nilT4Own8$zjw|KhelS}HDi+NG4R{h'
'stm8|tpf8g8!(WafQLZ$6JWSJUZ=jv%nkmH%S47c2T|Fm8I|*uiBk)PcoOkbv-K1+?`R`$em;BH=?JfGLw#3asV8?0`crAyBa;S{'
'Z`#q9Ef=0`Fw;=lt5E+)V(21TG;JHQ<g;PYED>VT=Lk*&4y_bBY+g@~d#N#jFk=*CbkN|k#Lv$t`FsF|Z#n+7!vem%J18_6TX?Y5'
'Sv@$rGt2ty$0#7LJtaZg7(pMkrJ@;P<|0%Gf{*kKX3*a)8h!}PRTs`snj*DmLb;;Vzu)v^RUWi881P({=XPs`h(J`12}=QjBVUVS'
'`C=V6$u{E`Zoox(xbgw$CbqZe5!>xOsdDy8z=*y@MFjzVhHaC^=blZlR~gUfq2QYHMew+Ffz|<_fB58|*BD@~6+>MfFV?dYoLXg%'
'HuhM+iT%R*aEJup%Y+$MwBr2yX9tsJDB%296ex-zjwf$Pq`_X)-UwhAqYSQQR4JH7Kv)HP(Lf_tEHJwUw(bg5Gyjng)|1x%ZPDCO'
'<H_vi;Y7c@QOc2ixn9c%k_NN`*+PvI4(msO(j*zCT_1taar@nMAWg9$Ip}kh<gAe@|Gu6lQ%3_Iv!wsEe!bdT0mK5r=ZIoJ1MCWZ'
'g9CQOSo=R0s&RFLIBdwL95Wh6F+V+s97YdV%Q^GUSIPted9~gGLXQY=GK(!Nd23wqm!Tlbx}sEBITfBhqSIXuy2TKHX1&lefhTr7'
'E5N~FE0F!{H4*TPpNBeNhUl1_FA!gBPb%=4GwSeKjOiw{#cWeLUY(cf9q(!Mv2#Z!tbO%!RP`8civfpvOVyn^Y@cz4PmeS<2{GCA'
'Z|~Q*QCZfTOWXjrI(;MHp%QER2*4iOm?QLP=Uus}Qq|{<OC?)c*U+35*O;q(JKJ?cm(>xobR&c|m~=hc$QHO^Lkjk2OHt^8lLoBy'
'G(N<Y%SkIAbS^XLV-(|9aJL!Ehj@qnLSFdzt<_|aa4-8ADxN}O=&)zT=j|$R*78%F&DXm~<J$tMRb5wMCev-LIvg<a5k&b_VK&%>'
'l$D7#7M=n2SGFTDF)TN4;x197jdDaCb_~Hcf+4IAfv;o(M7Sjed0WYbQz>lKz%Df2cgb3$rW%%}32kJoDnSxr1o0S*{$(#kFtBgQ'
'%2TOEp2&(K#SYAWVt2QdEMZuAs!ysW&&I;DqGNndE-F-=0TCo5{J?`!-f<Zf+|%=fkqQSF^FDGuSn77TB*D|8Yu&=l5|7>nsdF9z'
'h0J|hT>_qrLpQ^jn$=4j2*a3CyCyzZl!SotHbZDh<jrwqk?7W#t5E}qLxL?0B;95m2{5WrBETAhH8mF298T(A|Hoi8Li%@>t$Ye9'
'<#*<1BoqV{r{FhX-%sX*SYt%0fE6Whh^q1`h?wBMe~!Y8_ku??vl*Iizp#lD5S8r4oGcai5)@iaKRcdK6KAvhE(Hh&MUG^Q0iU0C'
'K<GRDI&+20(QF<5xeqtmETMMP{q&M<H`-?3dG;0%;B+#J;>H8HV2Bm=SYfc6*w`^~he`X0sAznL*do?k37&xe`!Uk8MRp6-M3voE'
'%0S<NOK>uyfZK31f9*5|-`V?oYQj^F-Cg-^(}3G8(P60H-gp@{;wN4rKsYC6ObQiFy+#Rujo^6CR7wLCyNvHzd&-qN%~Y&DxAV!W'
'xBFVatLzW+t(vM1`9TYW+m`TAgmZ&RILQ=Gni&Si2PKwe_-r5$+A{9>5L<WC1rT?25N`$&d~##9^?E$&RMr3hHs4p)3hR3`00Gaf'
'0m<M6QtpbQvBYQl0ssI200dcD'
)
compressed=base64.b85decode(B85)
assert len(compressed)==22260 and hashlib.sha256(compressed).hexdigest()=='d29b445e55e29325d8ae3fc05216328f4105bd4e0be3641e3a2000d95414ccea'
raw=lzma.decompress(compressed)
assert len(raw)==94281 and hashlib.sha256(raw).hexdigest()=='a7e2257ce307dca3f7301259b8a1700c1d1c75992d7d936a1b1ff113a9bad159'
data=json.loads(raw)
assert len(data)==21
for n,s in data.items():
    assert pathlib.Path(n).name==n
    (out/n).write_bytes(s.encode())
print('C48_GATE_ROOTLIFT_COMPLETE_SOURCE_RECOVERY_PASS',len(data))
```

The durable successors are the six audited nonwinners, the continuous translation gate certificate, the general root-lifting physical-U1 theorem, and the two complete fixed-base parameter decisions. No finite search failure is promoted to an all-bipyramid exclusion.
