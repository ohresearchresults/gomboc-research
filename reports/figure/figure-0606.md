# figure-0606

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 18 — finite cap execution, exact envelope obstruction, and a macroscopic own-U1 successor

## Result and acceptance boundary

**No own110/weak000 body was obtained.** The previously unobserved cap is now resolved computationally. Its whole original one-parameter ray is exactly excluded from own110, and a broader, label-independent old-one-step-envelope obstruction explains why adding more of the original safe controllers cannot finish near the old centroid. A genuine new-to-new physical witness construction escapes that envelope; finite physical mass correction then yields a macroscopic, source-complete **own514/weak000** family with **V54/E156/F104, C312**.

The most useful simple input is **BH18_WIDE_COVER_G6**. It has 21-bit rational coordinates, 68 submitted material points, 54 extreme vertices, P exactly empty, and four genuinely positive Q bars. Both original stable supporting planes retire, two tested old directions are lifted beyond the old Q merger support, and the main saddle changes from45--47 to62--66. Nevertheless, a low-support region remains around triangle **{6,49,27}**. This is substantial finite geometric and mass freedom, **not simultaneous cancellation or an improved equilibrium class**. Its largest Q is worse than the original parent's.

A distinct companion, **BH18_WIDE_EXACT_CENTER**, has exactly the same volume as the G8 wide body and exactly the original parent centroid G0, after a finite correction of actual material coordinates. Here “exact center” means **M=VG0**, not zero absolute first moment, a translated reference origin, or altered density.

All promoted endpoint claims below were executed with exact rational hull, mass, strict/additionalweak census, and no-floor P/Q computations. A cold source-only reconstruction completed **39 exact output identity checks**. The canonical own110 result in the supplied research record remains C622, outside the target.

## Source authority and reading

The new403079-byte research-journal.md, SHA256 **d0a9e98a7ec6179edff1f7f6e79001be1c854d87fb365e29248df0f03082c6db**, was read through **EOF1977**, including the entire direct immutable parent **figure-0605**, SHA256 **99e7202b5c1842e9fcdcb80543981fe5834bb5774be8ab4815955fe0fcfbda7c**. Its complete BH18_MAIN_CAP.py was extracted unchanged:17940 bytes, SHA256 **fd78f9d253871dfef02fd0939785a5e2a94113039c9b1485fabe7e94c9179a56**.

That parent supplied the finite reference-U1 cap but explicitly had no observed own census. Its literal underlying body is BH18_FINAL49_REPAIRED_G6 from **figure-0592**, SHA256 **d577f7aba424866ea8acf49ca911ab012bab826aff94dad92b447caa5505773a**:49/141/94, own211/weak000, P[], Q≈.6626794440888322, original junior triangle{7,27,18}, elder{20,36,48}, U12, H45--47. These identities were not replaced by an alias or by the former unconfirmed FOREST/EV/CCBEST files.

Earlier unchanged same-chat evidence was retained. I did not rerun the older37-unit/51-output parent package merely for authentication, and do not claim to have decoded and read every old inner module in this turn. The complete new recovery below has no dependency on that old workspace. One initial ambiguous Files reference returned the older2047-line journal; using the explicit new file ID resolved it. This was a retrieval-reference mismatch, not a conflict between constructions.

## 1. Actual raw cap landscapes and an exact exclusion of the entire ray

Let the original exact centroid and volume be

    G0=(-4351737373287920915403716,
         1060086063540384458338581,
         1282958296459800267966153)/114321127532794563848000000,
    V0=14290140941599320481/3000000000000000000.

Using the original49 literal points, define

    u=p12-G0, R2=u.u,
    n=(p27-p7) cross(p18-p7), h=n.(p7-G0),
    t=n/maxabs(n), lambda=(99/100)R2/(R2+t.t),
    q(tau)=G0+u/2+tau lambda t,
    K(tau)=conv(old49,q(tau)), 0<=tau<=1.

The original junior-plane crossing is

    tau_hit=(h-n.u/2)/(lambda*n.t)
            ≈.41541436098647977,
    3/8<tau_hit<1/2.

The first visibility contact is earlier, approximately.40360954291555695. The plane crossing is not the first fan event or a mechanical pair-death certificate.

The four executed exact raw audits have additionalweak000:

| Parameter | True V/E/F | Own strict(S,U,H) | Number of positive P/Q |
|---|---:|---:|---:|
|3/8|49/141/94|2,1,1|0/1|
|tau_hit|50/143/95|3,17,18|16/2|
|1/2|50/144/96|6,23,27|22/5|
|1|49/141/94|6,28,32|27/5|

The first entry is the original physical body with an interior submitted point, not a new construction. At tau_hit the old junior facet is an expanded quadrilateral. At1/2 and1 its original plane no longer supports the body.

At tau=1/2 the actual volume is about4.80161846519497 and centroid is(-.04520164419733801,.007107985595979416,.015847731995718792). Every positive Q is approximately

    [.6643103031002991, .04134588837280737,
     .000003774081861088808, .000002140668150215086,
     .0000005878066243854072].

At tau=1 the volume is about5.3587783911387055 and centroid is(-.1268872123695056,-.008224774561960076,.08099442726150702), with Q

    [.7096982273455231, .15239113233717483,
     .002071994271168017, .0006260578457450792,
     .0000005024749668029508].

All P fractions, not merely their maxima, are generated in the exact raw reports. Reference U1 at G0 survives as the parent proved; actual homogeneous U1 emphatically does not.

### Entire-ray theorem, not a sampled failure

The cap volume and first moment are integrated by the full visible-pyramid formula. For every outward original triangle(a,b,c),

    d_f(tau)=det(b-a,c-a,q(tau)-a),
    V=V0+sum max(0,d_f)/6,
    M=V0*G0+sum max(0,d_f)*(q+a+b+c)/24.

All visibility roots in[0,1] and tau_hit partition the domain into **20 exact rational intervals**. On each, V is affine and the moment relative to G0 is quadratic. The proof clears the positive volume denominator and checks the resulting guard polynomials by rational Bernstein coefficients.

For **0<=tau<=tau_hit**, both original stable triangles retain supporting planes and strictly interior feet at the **actual moving centroid**. Thus S>=2. For **tau_hit<=tau<=1**, original material vertices **12 and29** are strict radial supporting maxima against every other submitted point at that actual centroid. Thus U>=2. These statements overlap at tau_hit and cover the entire closed interval.

All **1684 guard tests** passed with1684 positive Bernstein leaves. No small bar was erased and no unchanged fan was extrapolated. Therefore **no member of this entire specified raw ray is own110**. Arbitrary additional or moved material, a different cap direction, and a larger construction are outside this theorem.

## 2. Why arbitrarily many original one-step controllers still cannot finish near G0

Put p_i=old_vertex_i-G0 and let

    Omega=conv(union_i closed_ball(p_i/2, |p_i|/2)).

This contains every point with a nonnegative old-one-step chord to some old material point. Its support function in a unit direction a is

    H_Omega(a)=max_i (a.p_i+|p_i|)/2.

**Exact theorem.** Any convex polytope L satisfying K subset L subset Omega, at any interior reference center c with ||c-G0||infinity<=1/2000, cannot have S1 without additional weak stable equilibria. Consequently no homogeneous own110 in that family can have its centroid in that cube. The theorem permits arbitrarily many added points, changed facets, and retirement of both original stable labels; it is stronger than protecting the two old triangles.

### Continuous separating-circle certificate

Use the exact integer vector **w=(-102,186,1000)**. The central section of the original centered polar by w.x=0 has exactly **33 vertices**, obtained from all crossing true polar edges; no old polar vertex is on this plane. Every section vertex has squared norm less than(500/587)^2; their maximum is about.7246480869545752. Convexity bounds the **entire section**, so

    h_K(a)>=587/500=1.174

for every unit a with w.a=0. This is a continuous spherical separating circle, not a finite directional sample.

On opposite sides, use the outward normals of original triangles **(27,37,38)** and **(19,28,36)**. Exact outward-rounded square-root bounds certify, respectively,

    H_Omega(a_positive)<1172/1000,
    H_Omega(a_negative)<1007/1000.

The computed upper bounds are approximately1.171838117074506 and1.0065269942986717. A center change of infinity norm1/2000 changes any normalized support by less than7/8000. Therefore at level1173/1000 the two tested directions remain strictly low, while the whole separating circle remains strictly high:

    both tested heights <9383/8000,
    selected level       =9384/8000,
    separating circle    >9385/8000.

Each hemisphere must contain a support minimum. For a weak-stable-free polytope these give two strict stable facets. This obstruction is independent of a retained witness policy, controller count, optimizer, or particular old stable carrier.

The same proof has a useful **joint perturbation extension**. Allow each old point to move by rho in infinity norm and every added point to lie in Omega+[-rho,rho]^3. If the center moves by epsilon and **rho+epsilon<=1/2000**, the conclusion persists. This correctly covers the small physical old-point corrections below without falsely asserting K subset L after old vertices move.

The theorem does not exclude larger actual-center excursions, larger old-boundary changes, cuts/removal, or genuine new-to-new routes outside Omega. It is a scoped geometric obstruction, not a global impossibility result or a numerical mass-capacity failure.

## 3. Finite physical correction, actual envelope escape, and useful exact nonwinners

A numerical all-pair two-star trial on the raw half/full caps produced248 candidates within the chosen coordinate-motion bound:79 half-cap/G0,160 half-cap/midpoint, zero full-cap/G0, and9 full-cap/midpoint. None retained its inherited fan or achieved actual U1. These were only the specified minimum-norm corrections, not all possible two-star motions.

Adding actual material in old witness balls instead restored ownU1 but created several stable facets. Joint movement of the primary cap and its two controllers reduced subsidiary Q bars without overcoming the envelope theorem. All these finite endpoints were then frozen rationally and exactly audited.

The next construction introduced a **real physical route52->53->30**, alongside49->12,50->40,51->38,54->36. Point52 has normalized support greater than1.184 in the old(27,37,38) direction, whereas the entire old Omega has support below1.172. It is outside the **convex hull of all old one-step balls**, not merely outside one selected ball. Every required new-to-new chord is an actual chord between retained material points, with exact positive scores.

Finite opposing material and joint actual-mass optimization closed the mass equations numerically. Selected rational endpoints, including a subsequent exact finite correction on current stars28/46, retain actual U1. The exact centered companion has the same volume as its G8 seed and exactly centroidG0. Its maximum corrective coordinate motion is about2.4301286913524494e-7.

The ten repaired/escaped exact bodies are distinct rational objects. All have **additionalweak000 and P=[]**:

| Body | True V/E/F | Own strict | Every positive Q, decimal display |
|---|---:|---:|---|
|BH18_SAFE2_G8|51/147/98|7,1,6|.654993474182; .041469190357; .005507914872; .001866100375; .001468182662; .000061535791|
|BH18_SAFE2_EXACT_CENTER|51/147/98|7,1,6|.654993484567; .041469181230; .005507911184; .001866098660; .001468180585; .000061535356|
|BH18_JOINT0_G8|51/147/98|6,1,5|.660756071964; .000925280615; .000005347749; .000003911139; .000000111998|
|BH18_JOINT1_G8|52/150/100|4,1,3|.662266355353; .000273211625; .000009455310|
|BH18_TWO_STEP_0_G8|51/147/98|8,1,7|.655727990502; .037803953480; .011686136443; .010373344949; .005151680226; .001842325810; .000868853611|
|BH18_TWO_STEP_1_G8|51/147/98|6,1,5|.658717628266; .008187024986; .002873346838; .000287387860; .000040322680|
|BH18_TWO_STEP_EXACT_CENTER|51/147/98|6,1,5|.658717628311; .008187025011; .002873346826; .000287387853; .000040322686|
|BH18_WIDE_COVER_G6|54/156/104|5,1,4|.694834922866; .053191980510; .004073579816; .001316872538|
|BH18_WIDE_COVER_G8|54/156/104|5,1,4|.694834894762; .053191826086; .004073595838; .001316823125|
|BH18_WIDE_EXACT_CENTER|54/156/104|5,1,4|.694834896759; .053191825594; .004073595737; .001316823130|

The table rounds values only for display. The recovered audits regenerate every exact positive fraction with no floor. No zero is inferred from a displayed decimal.

SAFE2_EXACT_CENTER and TWO_STEP_EXACT_CENTER preserve the original main Q death level **as exactly the same rational number**, at physical edge45--47. The stable carriers have changed, but that fact and the surviving Q lists show why label retirement and mass closure cannot be taken as a completed cancellation. No complete continuous pairing genealogy or weak-free path is claimed.

## 4. Macroscopic geometry with actual homogeneous U1

The wide continuation imposed a finite original-junior plane violation of.23 and normalized support1.19 in the previously obstructed direction. It used a live acyclic material forest and recomputed whole convex-hull moments, not a sum of potentially overlapping caps. After an initial seven-stage search, seven further controller additions closed the numerical first moment relative to G0 with **68 submitted material points**. New controllers could use earlier new material as witnesses; they were not confined to Omega.

The exact G6/G8 freezes and a physically corrected exact-G0 companion all have the54/156/104 own514 class above. Their old stable planes **both** cease supporting. Exact squared inequalities certify that support in the original junior direction and in the old(27,37,38) direction exceeds the original merger support, approximately **1.1872328868782425**.

Nevertheless, the recomputed largest-Q stable carrier is **{6,49,27}**, with support about.716863 at G0, on the positive side of the exact separating circle. A substantial low-support region therefore remains despite coverage of the two selected directions. The new main saddle is **62--66**, not45--47; its support is approximately1.297683275923229. The four stable/saddle pairs have not all disappeared.

The five stable cycles in the supplied material ordering are

    [1,11,64], [6,49,27], [27,49,37], [31,37,49], [62,67,66].

The unique U is12; saddles are

    [27,49], [37,49], [62,66], [62,67].

The selected full material U1 forest has maximum depth24. Calling the new52->53->30 link “two-step” does not claim that the entire body's forest has depth<=2 or<=3, and does not contradict the earlier shallow-tree centroid obstructions.

### Arithmetic, mass, and budget

For **BH18_WIDE_COVER_G6**,

    volume=101473752842666109/15625000000000000,
    centroid=(-5933080209329642826130933,
               1445293601728142474263729,
               1749166017940004894056942)
              /155863684366335143424000000.

Its volume ratio to the original49-point body is1.3633847717397953. Its centroid differs from G0 by about7.86329548e-8 in infinity norm, **not zero**. Coordinate numerator/denominator length is at most21bits; the common centroid denominator has88bits.

For **BH18_WIDE_EXACT_CENTER**,

    volume=12988642583360951386729633/2000000000000000000000000,
    centroid=G0 exactly.

The current-star correction uses material vertices0/46, has maximum coordinate displacement about.00011491695943375801, and preserves the G8 wide body's volume exactly. The actual hull and mass are rebuilt and agree with the finite correction identity. It has up to778-bit coordinates versus the simpler G6 input. This is an endpoint result, not a certified convex/equilibrium path along the entire correction segment.

The raw G6/G8 wide bodies retain all original49 coordinates and contain the original body. The exact-G0 companion moves two old points; do not silently apply unchanged-host inclusion statements to it.

With68 submitted points,17 further points retain the sufficient N<=85/E<=249 guarantee. Removing the14 already nonextreme rows changes no physical body and leaves54 extreme points, permitting31 further points under the same bound. Preserve the returned material-index map before compacting; the labels above would otherwise change. **F104 gives no analogous arbitrary-halfspace allowance.**

For immediate access to the simple G6 geometry, append these19 rows to the49 original G6 rows in the embedded generator, all divided by1000000. They are material49..67:

    [[-891236,-132425,1201276],[1014590,559119,-692273],
     [871557,733983,-657638],[384467,1270036,-249011],
     [396997,1179939,-665941],[684942,-627207,-356073],
     [282889,689836,-1229114],[87907,159953,-1308090],
     [1096812,-740853,215454],[1001544,813751,-227422],
     [1051119,263466,-739151],[1300669,-127621,376455],
     [1012837,-127737,-720637],[1317569,-91630,76039],
     [497173,440025,-1223202],[767849,-462148,-771276],
     [594564,62515,-1188432],[1146747,449609,-463716],
     [1096797,80251,-682947]]

Their corresponding exact positive own-chord witnesses are

    [12,40,38,53,30,36,24,55,32,40,50,46,59,60,55,61,63,50,59].

The capsule also contains the complete old49 rows; these appended rows are not a substitute for missing parent coordinates.

## 5. Further executed continuation and what it does not prove

The numerical methods are complete in the capsule; frozen final coordinates/parameters preserve the material nonwinners independently of optimizer reruns. Their strict threshold1e-12 and bar floor1e-13 are **nomination limits**, not exact physics tests. All promoted bodies above instead use rational no-floor auditing.

The main completed numerical scopes were: eight old-one-step mass-controller stages; two joint three-cap searches; a five-cap two-step trial; the completed six-cap mass and sum-Q stages; seven initial and seven further wide mass stages; and the separately described free-shape/current-basin probes below. Bounds, seeds, analytic derivatives, tolerances, and commands are in the complete source/README.

A250-iteration mass-constrained wide sum-Q search ended with numericalS7/U1 rather thanS1. A separate **free-own-centroid** search moving all19 wide cap points, without imposing G0, completed58 iterations and returned numerical **S12/U1 with11 positive Q**, largest≈.6105383961733872. The centroid moved to approximately(-.03804536,.02709360,.02522338). Thus an apparently attractive reduction of the largest Q was accompanied by substantial fragmentation. This state is preserved but has not been promoted to an exact body or a class improvement.

A free51-point search ended infeasible with extra U. A feasible dynamic-witness LP continuation completed56 attempts/42 accepted moves, retaining numericalU1 but ending withS5 and a larger main Q≈.67054746. These do not exclude other finite shape paths or witness changes.

A finite deletion/reclosure search from the wide G6 body accepted two deletions, ending with52 extreme points and numericalS5/U1; its third stage found no eligible child under the specified frame policy. The actual stars and hull were rebuilt. This is not an exclusion of arbitrary subset retirement, other corrections, or simultaneous moved-point surgery.

### The current low-support region, not the old plane, was tested next

A real two-link route was constructed to lift the current{6,49,27} direction beyond its **new** merger support. Eleven complete controller-growth trials, with up to66 submitted points, reduced the first-moment residual norm from about.68848 to **.26467436**, but did not close mass or preserve actualU1. The two later requested outer stages were not reached; no COVER_CLOSED endpoint exists.

A different finite architecture used **three whole opposed routes**, rather than independently adding local controller caps. All25 combinations of link counts2/3/4/6/8 and spreads.2/.4/.7/1/1.5 completed. Three route amplitudes in[0,1] were optimized from three starts with actual global-hull moments and analytic derivatives. No mass closure was found. The smallest residual norm was **.36625702088756795**, at6-link routes, spread.2, amplitudes approximately(.9880599355377123,1,1),74 submitted points, numericalS12/U43. These are bounded failure results, **not a theorem that deeper or differently arranged routes lack sufficient physical capacity**.

One execution remains explicitly incomplete: the final square-root-Q stage of deeper_mass.py had at least300 logged callbacks of400 requested, but no final endpoint was saved before interruption. Its completed mass and power1 stages are preserved; no output or terminal marker is invented for the unfinished stage. Earlier interrupted containing calls that were rerun successfully are not continuing source gaps.

## 6. Verification, exact output identities, and self-contained recovery

The exact engine enumerates supporting triples, reconstructs maximal coplanar polygons and true edges, checks outward support/strict polygon convexity/opposite two-face edge incidences/Euler, integrates the homogeneous body, computes its own centered polar, counts strict and additionalweak S/U/H, and retains every positive primal/dual persistence bar. A second tetrahedral sum based at the actual centroid has the same volume and zero relative first moments. Tetrahedron446 and cube6/8/12 controls both reject110. Global directed primal/polar chord equality counts are0/0 for the ten repaired families; **full primitivezero000 is not claimed**.

This is one census implementation with additional finite mass, polynomial, and support-section proofs, not two independently developed equilibrium engines. The interval/ray and envelope statements have their explicit scopes above. No numerical optimizer success flag is an exact-census certificate.

Selected exact identities:

| File | Bytes | SHA256 |
|---|---:|---|
|BH18_WIDE_COVER_G6_INPUT.json|3893|14b87166f543704633c9c8d5ca9b38950b21059da30c99cfd6ea978a67cf1138|
|BH18_WIDE_COVER_G6_AUDIT.json|18242|f3c7be789cb26987b09ea99134e0ab48be605b400d00d4700f1c11c3ea2fa706|
|BH18_WIDE_EXACT_CENTER_INPUT.json|50756|2b89247b2d3e60e86e7989de0e4ad41bef6d2e940472ae759da24191a951d11d|
|BH18_WIDE_EXACT_CENTER_AUDIT.json|30454|ac7209ca47d4b84eff42f7551333e096be86f060d9508d9e768eda857b7319c0|
|CAP_RAY_EXACT_EXCLUSION.json|495305|21593e9985a812e9b179fcd8790fcc06f23c6c179d55d67c4541d2bde60fc649|
|OLD_ONE_STEP_ENVELOPE_EXACT.json|33311|fbe6dc7e00de374fb043a21e1983ca5e737bcfe60fae902932117b8c23a1f22c|
|WIDE_DIAGNOSTICS_EXACT.json|29991|02c8bf2e18645e0908296e57bd1c00c4808f7bba77806929c4c7065e9d115ee6|

All39 generated exact input/report identities, including the remaining nonwinners and controls, are in the complete EXPECTED_EXACT.json recovered below. They are output checks, not substitute source data.

### Commands and observed markers

Save the complete capsule as RECOVER_BH18_CAP_CONTINUATION.py, then:

    python RECOVER_BH18_CAP_CONTINUATION.py BH18_CAP_RECOVERED
    cd BH18_CAP_RECOVERED
    # Read README.md and the complete recovered source units.
    python -B -S REPLAY_EXACT.py

Exact verification needs only standard-library Python; observed version3.13.5. The numerical producers additionally used NumPy2.3.5, SciPy1.17.0 and PyTorch2.10.0+cpu, float64, one Torch/BLAS/OMP thread. Frozen G8 nominal coordinates use explicit binary64-to-rational ties-to-even rounding; geometric predicates and final mass/census comparisons are exact.

Observed markers include:

    BH18_ENTIRE_CAP_RAY_OWN110_EXCLUDED_EXACT 20 1684 1684
    BH18_ALL_OLD_ONE_STEP_OUTER_SHAPES_CENTRE_CUBE_NO_S1_EXACT_PASS 33 98
    BH18_MACROSCOPIC_COVER_ACTUAL_MASS_U1_EXACT_PASS_NO_110
    BH18_WIDE_GEOMETRY_AND_SURVIVING_COMPONENT_EXACT_PASS_NO_110 3
    BH18_TETRA_AND_CUBE_CONTROLS_REJECT_110_EXACT_PASS
    BH18_CAP_CONTINUATION_COLD_EXACT_HASHES_PASS_NO_110 39

The cold replay was completed in stages after a containing tool call ended during freeze_deep. Every exact replay source was then checked byte-identical to the decoded capsule. The separate capsule extraction passed all31 source/data identities. No old sandbox is required.

The capsule preserves **31 complete units**, decoded dictionary **192351 bytes**, SHA256 **db2d1c1441be40465343d0e72e5e7569ed2c82ea3a7e54d0bbd967a64881ceee**. Recovery script **67282 bytes**, SHA256 **84dce221e4588c2aeece3038d808a8c2528d85d241cabed942adb6c47c98fe1d**. It includes every exact generator, proof, auditor and input; all materially used numerical producing units; exact output/source manifests; complete warm inputs; and frozen material terminal states. Selected numerical reports intentionally omit optimizer traces or retain only the last completed warm checkpoint, as documented in README. The full original traces are supplemental, not required by the exact or continuation recovery.

## 7. Most useful continuation

Use the simple **BH18_WIDE_COVER_G6**, or its exact-G0 companion when exact moment closure is useful. Attack the **current** low-support region at{6,49,27} and current saddle62--66, with the actual remaining Q list and full material forest. The old49-point junior plane and old45--47 interface are no longer the live target in this family.

The newly established obstruction says not to keep the geometry inside the entire old-one-step envelope nearG0. The wide family shows that leaving that envelope and physically restoring ownU1 is possible. The remaining issue is continuous/angular coverage of the whole current low-support region without producing replacement minima, coupled to actual finite mass and convexity. The executed route-growth, opposed-route, deletion, and free-centroid trials delimit specific policies only. Larger boundary replacement, controller reallocation, legitimate center movement, and retirement of old U/S labels remain available.

No simultaneous110, full-bar cancellation, optimality claim, or global family impossibility is inferred. The primary gain is a source-complete finite mass/geometric escape and two exact exclusions that materially change which next construction is worth attempting.

Supplementary copies: complete execution and traces (`BH18_CAP_CONTINUATION_FULL.zip`), recovery script (`RECOVER_BH18_CAP_CONTINUATION.py`), complete Markdown handoff (`BH18_CAP_RESULT.md`). The inline capsule below, not these links, supplies durable recovery.

## Complete lossless source/input capsule

```python
"""BH18 finite-cap continuation source recovery. Exact verification is separate.
Run python RECOVER_BH18_CAP_CONTINUATION.py NEW_DIRECTORY, read all recovered
source units and README.md, then run python -B -S REPLAY_EXACT.py there.
"""
import base64,hashlib,json,lzma,sys
from pathlib import Path,PurePosixPath
PAYLOAD=(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;_qI@+FbxWh=fFel*pi>%ZqawSFupLsVe5mjzm^$Pdn_}glEYHLpK8<LqynW?8XW`jKHF0'
'*G&i|^L2ydn+)&gSjY=Gw3sAMdauDO2$qeX2E`}e^j=q&Oz(=xg`#NSe<!q>6mV+Vn*@~udf5Wl;?>olFu&}zy_bYtN=3!69ZuR$'
'JBz1_w#pyII_CUlp?|_erf~bBv42TX3vXrbo=QAIX?Kgh?Ti<b0s2(dl_UVi*)+7g9t5Q%34&4|ze1ci6$rSc8~pxSe>;}?H&7xN'
')XQmXkCKoyvRb`xY|LQ2nb-'
'<Ner(L<+#kI70j`kFnR6Q2`H&JfS<30wdlb(1oScX&b6&%3IXI7GF#7@6>|qp1#Iq9uWVJUq+^h9<kK36#SdatZIGmZqfIK!Eh=u'
'hY^+v?GS|;=T@b<EAA9hb(b4<NG&exUD=P0R6NJANb5~r}Gt9|8nZ_9q@I@j}b9!+ZmkwVv4eA?j_vdRjoEMV}EjziR31_8daFQO'
'LAO9{a2CV}4-vwczNAp|EHD)JTG-WZ@kwtloZ69g>4fJaZSNq;>6R~j7F(c^Gp_(HM%=E;kY4YFT`I49bPD$BLbAnFheffd;d{8T'
'#0{Q`fUPecSaJGVZSK?$_8K{u&7o5lJpSX02<MSFgIsHDJ+`UbTK!pibyL9Kb!SAs-'
'W$(bm<jr7vM^GIH<p%=fjE9s=4@dDatuB`E@)&m_DU)8^f3+gIEb>s4(8$;ZOV#I6a=-'
'>6A*BO~=sGl@qh8lK;!~PeziG3(l{pE*}=iY&Xi@Ka+YArit?IAt(*+Io<uYB0WTF$k{Uh0qVYY*&Dgv|u~q9XoF11^3-'
'#Og*ZgW!;%egUeMzA-ww>%W}9)Fy|)n!4|BpADIhhdh+oNS@d|L#IHp0)ugp7NnEH(F{XbG}OUrPjA4nFItphB8_S+@d9J{Z)n;>'
'oLFo`<#qvG6MatzSDC3hkk{Kd2s*gDbuE;buU);+dabQk0YM%bR_t1F<yMXwWRLI^;MeRM-'
'v(?Q)_L%skdSpV&UFeO6j7qom+Li_nG1y|q?+RHoT_FcASO6Zhrn%nPhq7AW=lpc9@g&yE)79r9BtHfPDfS=TBAJ}6_pEKW3Z;m$'
'_een1UFDcwT0m{V5ANiuuW?qo>?@ksCdfzN_8cJNqqtlz+<y&3#Rm~zmR-'
'{3K<1djs`{r+iAB8_}xDv2C=z7fsxScW)vE@AvVT{bl=$d=@aY~@m|a!H|r4~5%}L|=TLW(+;0j3f;Cjf)^;@9$0L4`*1p3`_#b#'
'&3dWK<c17}6h-(t!fUFJ%H<NK<t9tcw;cn@eOqv?JGA4t##qVJ)2|vhVlP)Q|m9W2<-qhVeYj*m*!NW53_t<)@h4+0dU-CN9Q%n<'
'OEzF$fE!H=EIflSr(q}Ock3Z7POAj2>#!h4@9BAY%-CUjK<*Y_&dLN(!qJ~a|NG5vp^ofc{-SuenWJRyal|zT`CSSzi-'
'<It=yJhqcTv(K!1ch_xWfDozoeW*PBZH5*@l@^S173HAm&ZQCade`#9S^&`SFmhhyS#wEAWiK%$@l0Ins%2h%$tB`x|d{tJIz2T9'
'OsY}oKK;&%6X!Z2g2k$jIoA<w_0x_X_oOoOw-'
'$~WKOrE_~AOD<SeDi`3m2#3sis>@K`F156VZ0Vj=`@!twnET{xYVVfetxSQ|Sc@v1hQU6+46|K+XhX-'
';WcGJ|N+L3oO({(0b2)3N*>bf~DOK&iO*TyS)WAvQ>yV*szDdsO~jU^|XeiW;rF<f9FK@o<l&T04*|mJsIQ&1;UF9&WkjQvpg=>`'
'-u<SH{~#7*_-'
'TL85Q1ioiAsq1&WkO+HKpGjx*Mo7Zd+lCQh9uDK>J1Y&g29zEYwPW5!i<T^{!r#B7f7#nGpiX`;cblB9@sPl~T!Bz|Z_5-'
'mP`m8=GOUq8X$%R18rOI&!{`u^F3)nncQuJP91l)_?X88~-'
'xG=klU)!_NEY>%4ol_(bg^@_P>sO&@Uo=63uP?@_4Jw60FyfskGS{ELk&C)moOPy`AeRwCKS^%+NjdbS)x?G{NXx<kR%ujGD`NyY'
'@=I<1g(2=_^V%gcdGK?Uvoxy-vtQRv{NlaZZY>np*w?!9HF}uV*RarIz63g34Ig=Y^&Xh*AL(H~TOUM?hOEIJ;o25?hl06bUfJiP'
'M6;@ZcMl-E$39Er3yjWn2YbnVSibp1xfc`*Tk}?+PSip{)47oNrFCZTT>P*Y`s-'
'$b7y!Bsr(#4am*Y<9;g>UCzZY4<M!`j0Ls7t4>buLN%GGv$Q7<Vg1Q5LV2LEZBBol-EW({gW@`Fux(};HY%<Djc8PZ>SOm-uvu&C'
'YuP-r>+jf<vFkN7f({U7R!9jtbXy)#x+K2*fXg!p8*ASfxC*v0#e<5Kvr1+ylqwXD7-'
'tlc8~;*mp*hgPwq5^y!cyr1Izx_muN$iC{n&GpSzBo*_BI}5*-'
'H|y}B$*)tG0h9Dj<nC1U6*G`@{9hjCMxxc<(dyXtxaRq=3T$wzU_R2o(*0`I%P!XHRf^VV>b1=qS1i^<I~FOTe2=EN(r3(3tsc{>'
'HPs_OJ}g*B9=&jR<su`?qR(yl36d_8xLSSOK|9_~FiZ58$T9LwPOJ{M+aRG2aCLZ`e8$k3S>!8U5sF@~#emGV=hFojNdmLUlX5dr'
'QrU-5i-;2aR;?!&s?Y!aY{xH=XE+b^{;POGtjS`;CHo)f&5e9LDit7OGiqwg-AkYU_9_`H`JR`O6)2m+9Ig33b<^Z^x3y85$Zn`E'
'>T|M=EGZ~`@lkZENNtb1d5zqLIU$3zt&ST~+j>WWS%jp5o(+<e`B@HLhIO5tw-'
'F4eCW<JF9}mqkuH>FV20Is#?DO(^fzCDzS;MuKfV8@%RcWk>Pydh$7B3v43&WyJFEII7m?owrV|}tZf_Kkdr_wNIMwr{3XB?7qSD'
'4Qrd|@Y=JVDV(?*%~uRVg_vb{8(ImFM(bs4z9J#MBYd3@if+KZYSf2A{7214XMd#ix0Iw(fUS$Odf7C@l5Kty~$G5Sj~#b2rVvZT'
'x1Q77+!e_|X3{>pSRq^j;jEeWMbs`d_vct5D^x`Uy)JEutuCGPbUtJbwmN;}gZ?o4D+;#}M%kUu#$Jl_aUqhEAd0Ap)Kv7ieKqL~'
'eUX@GHkTCMmT=1d4^WMG9^9EO^8}l60Pxy^c9V6F!c$1ZYT_Alv$&GAl>Tqn-'
'&~{T|o_O*uC;EzV^YGMpYxqz3eCBZfakY<p8JIVA%#X<}VCN@_i8wnV}K5~%Yeedl$m`jwnmWZTM?#9v<UdT&pu!c_P*5GbBK)E&'
'Zlf<DVjvmL*Cqesh3&`M_NgKq%$adeL{ttprP?|^)f(<%EO)osUq*%d<6>v=jd^+y!AQ%b|H&xw=G-'
'%7PE(u|~eaC_fuCyA3k|7VUVr}CF8OCSjx+Oo#*xkI0~a}77<uYtL>(GZ6Y&ZYaI2A$x;^?~auh7x5l3xo=C`SUAgKI=Md6O_YA3'
'|8D8)iWZYJUvv~k)Z~Po`Jz(n~R>NBm`NX$-'
'+jLlz+(GI_;2vwYSUjwWUxANF3kXjr(=ZBLr~L=O7d3>YcwVwrV3#e$r#!1W;jtJ&LjL04=}A7LDOdu^$|+6G4N-'
'Z50q2?N?l2C_qF@^Eytv%ZhwcYe_Z=0oBUZgSE>saEl-nL!u5|Q?-'
'zyU)DZ4HbJ57q2A=UX>)P4<dJ&tz|M&rBW0BG1>Hv{`?&JDMsEx6dBvt7o09v?eJn~$_>rnA&n~OI4&q<<69s_`+owfMI$BV%<vt'
'4PhLd+#TF7x+0boy!xOC-&QftW`iHWT-hj?+p4*5zftYUCxPim-'
'q7fR0W=b3;`AH(2%KwqIxPCSO$Da!(`wOAJ1$39&)Wl55!R>C&af01TPr^UX&4XfU<2ksAYa`F3MXZeYhk?rh*8n%!K@$N`}Rdk4'
'cS(0;R$!CKSnTAMj1H~u}n+Pb6^V&y+15-cjaoLP`k*7D;!Ugr*SGsasXwN=6@4=~Rziy~}eL5VYydflrEk|TK-'
'?|3f^3ARgl29re%5pPbd=Y$JXo`|a-Y53JMt_;)?87!co29RIzLG@~?XJj2%UGxwc%df_!yuN&+`b}H+|pBX_G~;Z-'
'Mmk72o=by?L8C!=@`PvTx5lhzCe(63VX-'
'I8dXkwq<8!XjqOmlJiXj?^d~0jZwo~DSnq%Kd3dNibk>@R6Fj!ct=Wwz`rV0U#+Q%#aefy!32R3+dSTFIqf`SPl^JYKDlam9fj5*'
'4aksO|b{vE=J_yl|XBZTwgY?zZV!aekIxk{sz_p<#oHYI!M~hu)sV%~>)H~T%IU{h>7y+=xgU}Nf|3KWrF7Cef1u?BU76T3IpCkc'
'tQ@MdT$Vng?S;Der*wC)5V_%abgtT_dPTiw=k&oKXUGr2O7xqx0=@T5F=VnBi=7QvPW{o6~Ps@TGt(M9|^a80cJY5!%S@v?=dw`R'
'+1^>vp;8593@pQbfNSim`uckv`AZ|7!(ad<(rz21)W--l4qc;*fyrvF3q0K|5C|rLyZx4Ph*}v9t1~Qsa*bFZ@cgbJR+6<)m1~yE'
'v^X+U+zyAA>u$B%Nsz<2q54hVP4fk3uiz_a73q;wdRzh~2Ut;)FB7kE4RK;b%!RrJkNpsw-'
'j?BgDSE`{1zOi61y1}RQ?bE}Q{q|l`n5%W>ovPA-'
';wbX<#g^Qr0Fa2ffXL2B)XP?1KPx3iFsGh8^uhEgxuOV%zEucr(81df50F=vstHOBYH(@ObJ=;VUq+V9R8l=a`ulXtrr>Uj7R#aj'
'Q!^^cqeJS-9VW|B|6GTLbeAgbk*pm{SUQGt(yLSEcy1rHKNR0C%<S^6U4fr2MK+P-Y-'
'G?b2CMKsUGn}bRuxPBB0=J2Y!3dRx%q*_JlwQBD{;LV-I_C*-'
'=eomR}%i7uCwIdCdBWd!tixXg?JxwseAFOLaPCutEa~vpsWWxteLo{+l5RX)Rh0N3k)&;R$`RH(ucZt!x|N)(SbnR(IUz`cj+esD'
'Q^Hmouts47Skzt;F3X$IzTr*418Jp0*u-Q=A>RR5aZ-P_f{(X*{h6A)xd!HCC_{#0tkjBOCFLfrIq9#R%_Dy@t`}qH2}=2ZWAGDW'
'F5d_vYzI^`F5W9w6v@7>>FD_61;Ne%1ARFI7anspE6yQ6SO7ZI5!lpcScg_=3=ZWNq)a2*N38<WJV9Waehc57@T>T(K|cTGl-'
'v^$s5Ws18w7J)^JlRB%$zaFUir_hQgW!l3`>jw{Vo(pW+Tp*}qa8{CU878Xp}8Yl_LmDgUqV$0uX2NNFoRNe0a;6WAK$8Vbi0Dhi'
'3?EIO&a+pe;XIhv!z<bLFe;?+W=bqe;oJLt+zzb;mJ4Web<SKKSN?ufCJ4Lu1>oMOg_qS)z`ZSO$=ER#(4;0aXJ#}j6Hq|0-'
'<5^R(~C}g#PK|Uv^0~}kGxg*F00B?1kDO@30e^OqEpC7M9fL<tMW-JRS)Ke)oT)+mkTTSL<f>{I(g&Nw<Fv==GWar?Hgq>lEXVRy'
'um;%K;(NhkE`8x4H)0-'
'DM2dI);QEWR9uma6}yQ`R>Fq>Y4CXC?bccmGL&)E<#wcqdfwt~C~kp*<uAqRb;JU&!f_jy_N+!W>W*sB%0JR^NCoiOEAdmmeS7VY'
'u9NElxJD6Kn@82~?z!0cq*U!$=LtITS*G6fl&k#o&hi(n5ajGLwp`{}cLYEpFcT%s=dfl^LLsONoeYt0=ljZ)`j@X-'
'FwgelOg$=w6`Du5sfkrf)g6othYiP|m<O<peAXN<6R-'
'$4pn0L~VUx$En>PKuUkM#rJDtX`2V#;pj1sh_w9$~rIRQ(`PeM~hs0{sMsc+!%$62N_x2gKM3rIl^;$(=@7XKSlkeQk(4meTreFv'
'R67qbyelPGP7q&%t&GirT~wB{^nF4TiT91vR1$$?tk8Wkbv=hI2ibFvBhL3U!%btUqusCw*s_LS)0Ym3Hl?xTouVJ5)(Uu(wrvOo'
'4@?Dg-CaY<Mje-ZfDJgky!x7#OSJx>>+G3yJ1Gho%ABQ!<K2XAhm(W(CPbi+4LWOsVti6SK@KngZ9Cbo-wT{E#Ex=ytpjj?R>Fnv'
'g}~k9w<&gV#Hc5B)V>34E1%`pn7K%C)-C5t|-<n-'
'fn<diDTr*J5shXVNm`;mN;6rx|UN$VsxO0<RZ=csfBSW2FOG4K`@W|lg(IbKZr#xm~T<%yD1eQ3r&hg5Ms6I<@NH1H-'
'FM9x{SN?4|0NGQX;AB(}9F*!@|B+3q2QfGQK+t<Z+rc5fvWz<SoszB399GJxUMnYK099>+d82#x$4)N%Lqab^`1Zm!rMFF1#ByxI'
'WP|2)>m>{W#mxB-oG1cOCozOK1+NL-bTfQY`vHA$04{(jIR@Pqbu;uwn1?ylpbUqu^VK95b9!ejq>mmm6R&@4Bd}AakjzYdOH%C('
'uCINBg58XF9N<AGuQ2&>K+V-NzvF-4JtR=hU{k59n-'
'Y78W<gvDIYUa8b_Jzl#=Ba9oxZ`3g*vLE0L*i&3uk0RG@XUgz%@<I@h31`q{o&U@;tzs)ezVzpugsI+Cm<;Z7kBE69a`2NS%^c}w'
'r$xp03=%prdB?YgT-zfw+ZzCFs3{&4CE2msfz1!UjAgT?`5>-(yXv5uF;+^OfgS{O0zN*IFKIVv)Nl#F|^-'
'{Nhe}^n;%U<fL#=Gu+(CTSo>C&(g5bSx>f~5=nnCGEhk^PB)sHeL#G0Ts>%4AoCm|1!U+*P++5ce-'
'9c0akzjGIBCU}L1z1c7E6mw2qP0A$wb_&?1=Z|<A!U`ucZuyp?P2wVAnPx0l@;(3qA(;d>mStQ?Q_~EJc{H{TQ7}lSJ0E`*k1PJ!'
'S*ZKqto;v<tT=o_jFKK2~6J=93wdjQ`a>xUK9K^=IN{}ninpA}CVIR1ha>)=^|A4|$^zk%FFKAr=r~_W#BPkBQP(Q|NL6H<tkU~F'
'6fq@?=CMt$hWs`mbT2~MKq*e^>G$-'
'HCA~pPM2t}2e?URAB4d{J_b#UeftndY*BpHahquzaemEy^zevsY4jEr#7c5ZM_{6h17PF8K}*Qi2rVt;K6cGT42(w0?W6j3Amq&r'
'zub5)?h1mcEE<Dr^1{F(EM5(G#4;ic=<onaGcpWB~1qg1uPqdRw$eNeUIdjO{lG@P<eyo>iX?Fx=5OZ7*Dk+SF-+Fy2)`-'
'W_vR{+0;D1#mA*zr^OPe7+NciDP^GlMi3qmF8k0q<i(kLWn=P%evGLdt53;M;DwgZ(=hq02>;QeXQoEbdm_NXR@6E=a|&eqjh&U<'
't_FuArhV+nS)7Cw6s}lh{dnZdmQVbVas1+67xvCrnK7p|(zUuQJ!g3N+%j`is%(tWR6&7R-'
'91IQi~fObG$=c2<?(JD6N}{}|KR$#lrVGaT2FT`LVJh)axs46p^z__62vt|EFFIU$ViM~Vz7*Mx(c>gAD>J6D3C2JB50aSb53<5f'
'44$n{6qgB9;bq7`#Jx9%lci0G-'
'gmW=*XID=G~{@oS?UQl5KhAbBbxdw>nUe{z^B))qUepgg~`!f?)A0f6DD$${bNZjUl{#7A9>ddKPX8pYzsp2{mE$_Ibg@GwR$@YT'
'<;F!@P_LCtg7}4x}^0Yp+DwDHUxZwZs&c!dzQxxKK+4wt$d@#8AOdSz|Bf)h}StC^lNU(|nGa96z)<lwuR<g_M5FBijSAYnbDN91'
'EzOF<fB$CDjwL;pS=Va_P){qwk9c^##7z%0=#whg3J3{I6XMf|NLKnGF&b-'
'#KgupRw+1zun)vw0LWs(oAp!GLl`o?nqK1OvxxIzD>X_~ScMUQip5?;U)EX$F;xXim7wPpjH@sGxhHSt+DG-'
'w7Q4o7C2H~a8{SI|*zcn%}u+Zue{4dImgpqb++t+Ok?%y@E8hu^lrgqfth2*z*O<lxxkg^t%tN)*ZPkigU}yMLvGnS)WM@{z=S|3'
'^Zdri?d{$+~rq71haO@?R|ql9AYYU-|TOSS|D53)p&X4I#yofF`)e^C37WhkzQ3m*|AVQIA-'
'N*}<#MfS1JdqJ)xRo8xRBOoLI{1*eCyI&zqU<CF@Yi`XcY9W;9=SaAm2@vMW&uyx_mNYZ(d%R4XPW$IdmYHDRhIbRyKrgrU-'
'=Po@TXO$yQLv7JbeLl-)78pA!pSURr`kes?xuh`JIwu~Gh#`Wm5o+A!np6;Y-'
'_nA#rb*mv#QuoDx<it$s}UgM0Ys~A0W6rIIKA<ZSUX?S<i><N(`=+7=Ypu=hL!e1D#923icZ4w^s6YtkSUOb>1CsSEza+T;S4_54'
'xTH?MBEKJpSA3T<8)2nq)4j?K8;1%MqEH;H5r@Gkh{~u<tK1$&J+Ji9eIJLQ;A61VZEkn>)_bPQ6WDSoWjXM^Uus^lbHAAX(I7JG'
'^|a9`IX_#d4Es%lR<`(=ac*N0kuikoX}KbzmAsTv)gWY-w-Njm9}!x9JL%g;~d{u*@$<QC=JwhFI75WVibwKcEvg)-'
'+r)oqOc((o2?_Bl8D-{MQ7SRrUttuCF7D){ZQ6et5T*to?RR=O9bZ93rb^hWA{$eR{n0LaCh;_m|3Cj$mCa1-'
'n!=Pu*=q#KNLU$KRLewat}cZPZX#}C+IzgaC{wf(BDt^9#pYmpRc#7LE72ja!c1D3N-'
'43_$dy{Gfco~PkYG7S<UW9x;e?Q>{G@Cn%7ZcOghf0tLu^vrdbTT?U}`E{Gq2aT+(dRillgTG+xBFg+aZPc<e%$A5~yLmgqXhX66'
'Rv@bFOSEsPd-)!2WZmqO}U@%yahfL^(L`SMfqU|LVvq7*)dwhZfc@l}8m-O{wOAHMs4TKO|Yu<H3NaXkL`Z!-'
'$nt+~svQTj#WL_&}4Gv4oM2s9Z_4s5h=mJRDcxBd8V>JS40)C;C>gE6ED1_vaV7*O*3;$#}#ncYVX1+k_?WdwGXOob7fJCJ%;rss'
'5bA>FYE-|q!blSP;diXO^!-H|0~&xki9T{%#&EpSOqd9VvNBKFh1ml;oj-f%k04w1#QY7bj7Cm0z-'
'j6H6fN$A;(#_uV{hS)6_!Fb=hBOL*a_1T7F+hc^3LkYcF8xYC#ItExP9bsp@g*#nCl1Xcu_C~QwNRM2-'
'1S<N<!Oxa37<Iu~mLP}u{iKgA4Xmqk7wQ&45lj)17Y24yGu4ET!X9y(ZE2?u^PY#L`Zb`*8ARPmy}_4pV@c$irrPG#<FvPYYY$3T'
'LPhDU>FA6qtw;;2x#70qu9d&TKqgQv>XWPTNK<(%6tR{`qk)BYz);C{3>{7yDhtk5C#l(B$U4f8l>>Py0QF$1gQinlK7QJzq<%B*'
'(?Y{4SkK!q&X-'
'k#(mjnJ&K8Ql;di1DyM<7w;hNp0Ml(_BVhT#E&=OK+9(vlSdF{25QPx3t5Pi%<Emqlm0)jG55fE~zUUM#lx#vstI{d+FtKbg$?6G'
'|{JBDf!x4*(v1?29m>F<H){~sR)$$iHVu{Vk^cIt&$(E0e+<z?$f2GvGq&PMDgaJVVa!pSn>jn?zYTg;nkXADL2d9wH#AWjPEBgH'
'sNL=>LCAqN?-8c9A!Ne`I#qyt9K)uW0SH5u1=o6#70IG%~9n5~N^k(s+xNc%>{tnRQkK-=mQ-'
';Zw75W>iv1K4kktkm0qSB<DuJ&Z=as!|Sz=bo*kP#|J5mqm|b<P#rcbio5SZrYoDccHJTq@$z$qFf@!>4rw;wZIB>)y>bfZW7%-'
'Zxeg1npC$$P=`qCX)NxT#8dpOLX-'
'h&SJI<T_?Nq0Sn+Wp;S#qFm3=INeH##*@dQt@dvF`c)A5V3!^&;?k9;Ty8J!haYgY*?B;SXlmRW%Y3uy4-'
'*Nh;Q^c%3X2UBXJORpFnVo#{Ap`~}t`c1F~kcGuQWkLp_@kDfUZN7S8*~4)mOMCv?JvXJm4hZ{_Rb)Jl+1P~qNQXTSLJy!zZ6y+7'
'58oMUl{Rp#yR_BG=y-'
'l&M^6|m#&vH|iph1BW`4mi<z!Js+QJw=Xf|&9wJJY6DYT@%#cgXIlbqO(Oj)1msx`i`gbzl@gnz|=Jo{6%7e~u9lxbAduswXFEvZ'
'pVvL_B}YnF)Qg_C7LtN7PyR9%csj-Uk!sukB&?8@YT8TI~+GyhSm+g0}q(~^u(tE2CiNOa@d6Rh|vQ%CUaXr?A$7!7OuO+C%W;>u'
'*w2)%Y5l4)y3UAyeYTmm7?5OT<mjkC=u=f}-'
'r%M!Hd`bjsJXCJ3%Yk|<}<n%eGw+e3~o`pg=YIQx!a8;{Pi7MCi1ZKWte{mvql4GTfeJm^QWeafDR0?s{4TZvUTA$tul89clnQ~k'
'gYZ7)e(TCWo&3tz*xij;_nSAt*1m3^Rt;L=g)w8j(Us^m}(xdGGZ5$`b;QOx2+ZAaJE|cVq*3q_HL=raE%-'
'aVy1#qcCCvARaQ@F7?<vg83H_k-'
'J!P31P_o>|PT%MoTG5{y?FnxwBz919!qiFYETOM{S&8ba&<_Fx}$DGmJCoL#)_1;p3C5rbyk>JNED&|Ndk&h;A*3-'
'(Yf|bh{cMbmFpJ<>RIwg^I8o`stOdrPfF}7{p?Iiq0ehy!{C&5&CtiFL6y`0c|!yo9gx(38I_9)7&Dxz+XV4=_<4xZvO#>nmnYm)'
'r3w7Um5@vg)?2Msms+~r(eYWanqWOiVi(vT3NplhsIhzqgN^?R)(M2DQcgDwO3$ayFX4wl+{{xWVfG;rzCg%4!DuVR4<Mr3#z<?M'
'Dj0%Y>a4KkPZuR)7vY_A_t=S`X!1GM~=CoB!hLi=LhKBxj3U4p7&?^D&~;e#y3H;jDx3M=n^5Z5`Usu*oyo&NHsiR+HICv4*C^a7'
'R4gPzqexZwAH=k6!Q{M$s5uPR^5*(mQ`L37*uq(z1`u+sO3LZOU<PAsh{x;&{AW+2V_A{r6bq*8a4znn+ZQTZcW^i+*ix|K|ItBP'
'&mUW4E`vGn*nlbJ`dpvf32bGzUW7SIgFfcKGehg~`{zxK~kEZ(r;^vJ{nKKo0w?0qFK1<S~x1WXCDeh4`91`e@{pgRlgWki9;8CA'
'~X2m`1bME%I<66V1%J41V3Dv2bt7tCx<K8<G!vycKe2XrJJOg?(v%ne=C#`z29^ULf#qbL!RUEQ$im$)C*TTCPzgr+7A(bK7wCP1'
'm)CgGQkQ#H)C&Ba2?0aeJcWc`JouO`AMnAt2B2g?N(T79~RFq&`|&+*$>AZkRoksoKHZPzq!M+-'
'_~S5yJYunkx=y?9hEzC2W&YsTr8$NnP(9_K@Zb14yi6N~xt5hE$~Y_k@onpt0?&gMAE3q!rtWY1a#w*eQR+Y|(brEXBj!2VW`{&k'
'M{V~E3wX4v8-'
'WuAPN<*Fpg6RsKBXezoiz#+g6vgvC4=yI#D?aDKcHy_aiX2a~_d#5Nwe#w=O4Cht2*!`Xy8olKd)b0l#s<9iBY0Z7XXKA6PpO)Gr'
'Y^X{I#7e&6Fcm|E+XFgbL@_?PN7bkO*ehtc&!?977;1v7STtpsDb%P-)M}H-D{9uJ;#RN%WjdTi^^`0N-'
'y)Z8Z%hQXV49bK4jyRXsKINNgwMjp^Ez4=Ia4p&4X{a~0bSRHA#zXarCX_)(}R~t3C|?T+xm*;Q;)9vBvP$vrC7lar%2v9w@ynnn'
'2Pq6D6M~JYoXv17odr>`<tG`mqhFST%JH%bExK`)2<RrzOz<nZQJ~Xe!^wuFmXSei13stl=adpYk%ZJc`NnQx(?p{AITdQt%+wm('
'7YpI)Fr+tx^W68|FY=rwAdEmsCdP(Q+uLdz8OD8<vg8u(fI_w8aU~vo+JAz^^Ol>vby(MX|(;1n_9R{t}E2H)|p}(2bibfp43w;f'
'E1UQ!?jc}i=Cm6w;yC=u-'
'4WAAKxmXnV~(YczOU~HFDJFU7B(uB5x5a%w)yrtd+R<pXe(KeoyU>(W*4KT!@coqVMu(HL3ZCll=0Dw$1P+k8!C;=r!tHIrXNM)R'
'cx!5kQG?pZADP-t>o~FJ`Y|AZ`9gS<3tXdr#m5S0%iLPW{m;XgHSvw;-'
'UT0aR@=k%bJh9&iQe;@$|GPr1WS%<Df9d|WuXMGU^Binl6)uBb={VZsApraP~cm2<;>|Nlrqu2KbuV`xk#(x9{=Z<m91iP-'
'*a)7P+EiWEN8X&YmSWOmx6eA+U5ArHtF?Q;kq8-_tHOLVxvJeaN)HX-'
'M<a?LOYKoDYO2SioU=?IwpctxFRRfc|hkFUK&*Z&v^nVhl-&IHLqX-'
'O*i>Fl~mv$^fucH69_U2svF8sH+C<YKrObWEN5CKMvavA`@bdbi`LjXVCONk-'
'7bQo~Yq2<V;NtVOr*(j*1E%X(_&jlx6Rn;OKLN<2ETnUT3{y^-'
')R<k1xjfyrm*>e3r6TGP}`OE28tD;GwqzCbwL)#%<0*sq7?>LUcr@81fy6}Baih3A#etVVqzjN>{_qMHo+sfzh?Qvw*?v{Zcz7gN'
'AARs%eHp=wW1JX0Q~rcB%C<=?~k7Rm+W`yeqP561p}FxfG3hC{_Cr6ll~1PtI8Es0L`^EW<?igbcf+12d)_Wo$x0nwwy<MbIr*A`'
'#|&qxRbvWj<71UhMQhbO8n-'
'&DSs%)X`in?WJNAMhU$Wx}*G)p;e_I<I7=_I4ZcUshm+#9v8NnC9YugUvwz8}CTmOh+LJtJvq+!j%`9R@;IN7f2rVc>y;@6Oa~uX'
'=Q1x7ga#GY=#foDbzHJ0V*+dp}KX0^s>=naO~e~rf!;Q=!DlU2hDD_<OnSSNf|4V{M||&xj8!4eNX?Yt>7&8Vs^(sF`_Q8SX-'
'0bYMML>)lz;`TDKX~jBg`Y`*b?kY@Qja=x)HHY_2w>8{fHPl&x)kan)Ox^<0CnuJ?4fqT0BUVu*!B$y?Bz?F!*rv)UVJT%k8OUAJ'
'9);|UOf$9~a*99LuB*}*+KjLxeO?m3P2>e5a*3Fe8>YPpk>wL1Bu!W*F|#oErx3JMJcROcy=Sw2UMmbsOD?y--1X%<(R(_cS(zus'
'5N7Z50emkfOkYjOo;yMNKtZYf>gBg_IQ{NY$M-$-'
'dRC=6BAA6cC2nlAePW#5aawOHn3Ew7d_UOJ0<Qu4%7)HUFois$)yY7nxvwoXmZup(U4t~f|eB3$pesAH<^4?+0N1LtM!!V4=);^I'
'o9Y6e%i80mT(T$?x>;uxR;0<mVOgTpJr6pO&P#lm{_pFCun2CDifoO-j=4g3bD-eHpQ&B<L5WSYrM<~H1#9trQRSrd{sJ|?`7JFL'
'gC{(gx}F7`e~p)E;74^`XWPcb-v%}X9rjY?q$aU_&zv6AA{+*fg^F|S);bdkeK{%@n%w<_mU=D~<-'
'9{40<@)USM{Q~>3fLoR5pVd;76yGz-GrBRE2EJRRzkBh=aBwlNYf0y=7D882XdZOPiB)RuFBTMG+2R5VZ(Xn`Jz9oh+l5$Sp^?V}'
'KhYXe^vb-e=ltL~f|xwVBQ?o}2Ja0m18$h$JS_N>(!AXmFz~-'
'}7%~cj0PA{9?0|XgXwC2mSZy87wi+|K2gtV=&hFa$+4X!3u}(^f@(tD%61Pv`nnER87p-KUAWrh4!Lzi-Jtam~ARFs-rB%;GFUq|'
'>v$qIf<f($k1xTs*v9x1k7u?!R3cLifoUUH7vZO=-Gcg3#iyE9eJ%9-'
'QShd7egh+p_z8}(4=V))g3v$nv;<RNexexKF=C$8`n0XrY`WX~HtY45vIn_Q1g_V{O5C11xi-yG*fd{`=9fR5n!Lc?7$gi{dY%Zz'
'4NmqEG-'
'~g?u8xrF*bT9jZ9Ndp4XS8bvcD_4o`y)`HX?40SM($U~pD!!>;2%iSeBLf=$^;WgMM#s3v3lX%$fJ)MLN$ThHPAFMwDtlrk5&()t'
'J)wMl_GX3`U47erjV2^{5J6BA(r1#GS-'
'Z2mv9n9AR*AXjq<9P7Z%p3={tIDJI5G^uO>fBJ1dTyrnZ?5cuo5|HRp|4sDhb{87>2HGObQlR}0hYnV9XuEk)!#<%PjVal?9ER8c'
'^p1SQ+;vcCbbo&JIyE;~BtWUfV#&R3T2H7zB*>2y;j@0-'
'0o*#U$*_8fhpmpN7?fv=bzLk=q#N>XDFesE`c<4j#w3q5g~)(yTAbw+eYyUN<b&FjdZTlr#?cd-JTayu{{I4zQN{W4kBlb@9+jqm'
'|IUkt@Y>gu%2ujDdRTwoi?l4i{TJ|MYaj@e`zD&-~<;Ru>YML6M*Aw(nmx^0B_LMA6>Jf!J*dGrg{a2B?Y=q<Pt_;;-'
'c1e4yK{acC8j$FHL0@N~zgG=pD^v^XS&Y`Pe;IpUov|`k&8xRJ<xO_;Z9)l{vqr)uZh#R`Buo!9eu7s4X(OTdp7XWAfai1uICcQ`'
'6M#+v<Tv|Rkr;yD7#_sIuPI}OIvcwj^Wj;D$6vUo>Nt!+Dpx^&^5oUO{Xd^mQBWxFBy9)2$^GAG~i}>QDF<=)0IJ)<2*~z_r0v<E'
'm`SqvBhC<f;6iaPUlYtiS0EFLPv~W?-'
'BPI@{L^Qa_5Mxwh)s5{E^_do5mia<+WGjR4wHknsc;|_|xMB*Y14dib(u;h`)5&v^aMVz?>)tv^o5S8;!ioEDeCy{S=8F@5vZ=a3'
'NuR1|m_3@|Ue5iXGFk9Jfamb1FfvSo{JcBOd4Li<JI&U=7LMa&NrbOlVkJ$p!(4mbPJ7+TE?;51{am=Xu{G#{k|@6nbKLUhCnI0c'
'pCxHy#m{EUH=`Fs=G@#O$CI`TVA7JJ*^~)b1Vm-'
'4p@EGmbjQW_eVF@C8`MIy;|U**Dc|QJOFITU#HQdI=AxE<_grX|hv&N8XlV6)s?WPomD2e%EL#`va=sV!)7r-'
'&HlVbgYT9iJ9nB;F-'
'kW#|B6*qD`?%1Uo6i4A$D7fyA!VO3(E9WOt~Eo@S}T<h!ctWNsv87CgxBsYm)Re0m2C2(q1#%pAbTRtd`S#ucBzRvB54vG<n~=is'
'gPWB4wD_sD@UUU)Do8Q&q^{8knbdp?vS*iUzbJk%iqqKnzs){Hl-'
'8hjBpvNVKSnebtho|wn6+k`$S~OEb6=Qhn583DUXFoKRNQQBP2YmGhjn19|U}5Gz{a<>7N2f_ap38a!f@zpxQ@i2JKWKFO=4ykEG'
'eF{r{bA2RMnf4+=-'
'3zhQt=r!cN0c40%E_)vIfslBFr7vlt(f&blG(V`$8*_8~e4b4L7WqCgh#rM%%owU|ok%z6R;29Sh*4GKc%xJ8iw}eBaTeq$FSYmb'
'h33e;wjMU|VmU261725~?dhNJ|8iAT#-aaP1eF)&!M?2a%gRxvq3O-jws~N3|0p-'
'=Oru}A&^Os%G;(xvkM!OH%1d=<Ra@=tEL1d8V;vaqAJ`(;@VFNC`^zcG~8TCb&^gs?yatYq%wx_}jYsv8VPn`OS*R6bqWhn<3;+Y'
'lQSJ|q94~#39v8q~)t@$p?uttYo8;#po901CYb)Q=}jBbC6lK(hvAl&EWWhB|9rH}FEGgU|87aUw5cU~OdDrqL2t;EIun9577M}D'
'i}?8Gb-t-YlPVil{@3jPkqJ$z@ICtA5{3T;EZV@N=?U61FF9{GU)f7wPkV?p&AB_BF`e30Pd8vM)P1wj9Z{qaf}ldkcSGD6peykW'
';t*{kfyH0AK3LRX{6aauOp4U*O;{bx+eTQU1RdxWh0z=)g4x7A9w5`4m~Ls$I@x>cB*TTqAL&LS*it&?{CsMDvf7N5BJSLEG}PA1'
'`R)P4h-;+*JV2^g|OI(VUJ@Dd(keIgJH9FHN4#=+j-Q!CQk8=hE$MwnJY3Uf1h`MIx>x?RFuMZiPwx};69^04m|8-'
'@uBveQN!HFrTbHy>ZF`H2o*zf^Oas<pQs)J#47n10KTh1gmln*8xo!|%->UDp1hs75-rqO_PwQWig+)K^i#PKT$UWRr$x2r-'
'1sa4DQT&Q93|mzhd#NjMgvMe$Ta>m5pN#fMdaILO~PEL$~q8yX7RUM;ur6XyTSdV5Rf`b4qo-'
'G8~COTgK?>Vc;a6Yh34a1yrIxKQPvhYt^Rz&!b4)<cXs{@L`bA!tjjX}gb2T8jLiqH|#lmfPS_OR9q9zh{1D9r7pId*Ox)H>$wBn'
'hfTdPLGesusF%mdE>YsLPN#zS?M)f0~EnFvaLJ;Efk3-u1;i%5jw6N!}-ph7CU!U$tBtELztWxGQO){@7FF*mhY8-'
'RKVqQj$hR5FVSh4hQl|9MR)hKry$&(lY3a`;#6wnw{5%$0p)<Ix-'
'a%hO=icZDz8;0;k0t*>z0o8@Uma|Vo6qTZonU9i$F#B3K%ee<q(~-'
'$VH}q%uT9`h<Mb*<LX4WoS2Nc?E+@wAaqOg)bFd%PC3s#V?P5VAqdY-QrH9rrL70Y$oJ`}%8hn7@>_vz1G36+83I%7DeFA<FQMP5'
'PO`q)y=f~waANo>`8p&b5g97G%kuQgE=~b%nJ`b=@&IqvWp7hIGA6zoPq}pxHL%&bd#CM?7@ks<y2MPcfMEtA#=ODjge=wWxD^;*'
'WUfa34dmLaDKQ@~+IQ@2Q!0cGN<(lyN%RYhHGqz>+#zrzTR?yiI5UCNON<|E2qQAWF2V@P%8jpq@W_hP-xPLRUv~-'
'81FWY};Kj%=o2283w}9iq5<fdRH+D<IcJ8s^I0=$?(!R(BGF7~(JzL5Zq?ybaz+;1ZdU%Z%$y^rVN4D)V=Bi%4ojaCwq{1@^krCv'
'6YQr=?b0_xrDMhmz-'
'I1{+Z*wmsqlg%3JIp3XRxlF5P%d5oCA6aVgkN2R(L*BB#*<BvnO9;my|0l>e&vUGyuJv{?<Z32qMlnP3`jA(ml?G7PN|kS9|4mNF'
'7fpv>h?3{gwXvL#a3ly*Xb`HQSbyGStdTM)uI{t(vyd3|2rzE0r!|md5_g-'
'M(aa=@QC1DjF5+=zvLi@(Xgc#?SHX&8aET+^ZE9ENQi3+@7E`BLcXMYK<8Twi=UQ#u^d~a>N|MVh?zbcs*8A+)-'
'8W14deRq@&DX~Lh8d7Q8haD*hFAmFdMz5mCgtrxzh{y3>=2S|MBGy>9Hfb!ANXV<dk+LBIrIL!F0f8DCJQhUji2<oYg)4&nARF`Q'
'tLsHcHT2YWqV9N+W1eB<=#~DBh3&JN?B}{|1P@tuDBulAijV`R0Xa8s>|W0=QwJ6Puhu6$0HG)8vHp^B5U>UP|H=Gu?f!uvTK&Yv'
'D<^trMk_!1pf^z^zYSo)WJfA~{XDLVUp#7O7MfbU~fbakD3s3NJ@7oTz$Rxhqqor=NHp%jT57@fc^Jj|Yr00RgkD*>WY2UItSx7-'
'i<39xsu``ZcsR6`xjj4`3eB>`-7s`4t{!&Q`uo$Kz^<D@sJS-'
'=16kC>kD8%JOYf4N+g|%2xKv!cA@RW@QWY&Cez8CrE#tBnLYuFYIY2y}J2s{*%Ta5ncN4VemH*C4X~-'
'Q1pA+e4dlt+HX+~NC#R5UJ*CqVMuJjQBzRd^lLf!qMGK!J`jo@cZ8aNY4;?2DuN(GhVy!>icWhn6151d#hcK`jN9=v+2W2Wcfks^'
'Xsc<tzIY)fYmkgk`E53DN|C=?rO*SHeHKXw!z1Ej;k-'
'P$SLJ<NOdAqVk=D*?w%Hi9e?{$3(9M6CjdRG&0+1a_&AH&|ynRj+G>G>p$JgJ=R~Wzx*vG4%gUig_3<(F3pm**d!der1BVsjZ)@u'
'>9+nU?K6R+aLY&DNqIb9!BMIxQ8OVs0$R^iwBiOtJ*hj%DvMfN$p77JSuTbD7P`sI(x82&j+!c>ZA%y_V&<fxmKiN)4<o&OIbV0w'
'W+il0BN6896+*{SQ&J0lD><s~gLHjyMnA;nR;B%khSur&0x@Lc6;(iRikJ4SW}nfs`G1qNT<TM`5^eAdV}u0f9n0u8+Xy?Ur88>R'
'Xdgh;Be>qLcen7=G2x3t)j<|Q&Nt@E^uyRo(p4p4J!4-'
'{hhK(<7dya{*2irU6(Q^{9weD3DJt^E^@|MJ(5g^D{M4jF@Zl6QkA$5eg#Y2}0Ug~p^4=!b@b58nwAlus6MRKQ4-'
'(egzRadcH@%{&*l)o|Euu3zqOItdFBT%rg1Hh_%Cv43<;vfToW)Q(Rml)|`C4HV4zqR-Oc8OA&<2`RD}H|65g|L7ijQb^%!>6<F7'
'p~1p{1PQ)<zX*F(_{aeCzsJ5E+-6X7=*hlwy0p{nhI5GxC?TE@eJ@QOjwN1%?<hFq6<|r=*gTO|``?mjLC_sbX%mUf1c8SW-'
'r1bNYXO<7g<t@xtniv22s**z{VskTifEy<j(VurpN`q|=D2iHsDIer9%;00#oD1RaEo^Zs{FiT@Bqh~qP~FfZ8gb;dC0Xd>P-'
'AoKB6~eoFN~#%jE};o0F8y+~XF@$^x2Hf2UWX{6);s*AnJ%3Vfcq9xiG8Q8ScO_3V*&-n#+5^Z0q1occl4w-'
'fWtf}vavSPGG=gLWtaV&dDFyBk;;Bv{@jf+_}$ddFjrE_<;olg$V{EtGk3){WP|8-HgbycR5DNR?)v5guKQBKo81%34f!h>)-'
'3Dyv$ZGl?7BX@38N`avaem3TX6oj*|>dq!+va-GNA`@rAD6!q`NhY>-~PJ{P1a{(|;52l96DF`8_y9-%e%M-'
'?S1i6eH{^p=be+SPLo<INd0XeU6LW_<?=kOnA4R?pg1F*p2*n%$!a0sqgzW3<mT;dfaa*5*9C(WrA5WN!S;^X)s_Y_9)uA#kNDu6'
'PW?qQVd1n8f&!;SrDagdRscz*;7&^j*+FlXy^n;D>Ctgl+OFJ6{fe6IMgX{i{2$a-'
'9f6U%iz(L`rTgL|(vl(@I`dr6x;B6Ta7*dfC=$=T4KpE~Eq#;Ov%)d-'
'G;DNM8x9?4|e1s&6tJ9C0qo$Xw0ea~aTcvBNVMQSX#qkWRQ@#S49HH!Q$1E88^c<T2If|y4Sude_HI(`yCLnFz$DJ-'
'$Ba7b(}ymD%$bnLy!%sPT@J=V<SZHwoTUmGuwX__?s`0x6tbX*tWmYBnK7{w>NJ@~|W7C<8g`z1E8P~VOw-T1-'
'j4WipK<K;Y~z5j7=LW99Zk`q#-'
'IM7zTo4PgJ98>q_b9T45&YcH?RMumskkPwI<gQwX?Q1e#IDnQCYjYugSJ`d@H9U+g+;n3rgXETgQ!Wvjg!BdNq1K8}D=4)=*!)`='
'cNzDi{u)d>xb##DNZQpb3n9!0fPO;iSz;1skJRa9>>dsDqG5$PPXAerfz;E!85C~o1wI+}UlbF0|2zWED=wisWz3b-'
'z1YjleKHIzNjtdU^e__ZP^`1G+7~7fV~GXY40y8ZnOm#0wA&gfrx@_N;4tX;YXTZWEQ^!L-'
'X{&4EhHYCq>}z(t0vG7EB@Ry^2JsY0d0><Sqt8DWy+Cd73KWglL+sX=HFltsS3rkWJ~1P*Rw5+#dUEH^*{njc}y44LL}Ixi>i*si'
'9_K5iQBv!h<CAd9Yl8Pzv?$Vv7*rx(@d6(!FMsQkBpV!iM*8h+*(AxYti+7J?Ebi+qE8eM~ig&%LgiI#US~M_Qt29Z8Afj-jA3{B'
'CBvIJWk6nS=yaixM@yEN-p$%+(n0C&zAwg10!Vi^7hlS@2#OHn=>xWHCSGiZ~<aO;m@Z4$7*H@HrRjw)WRAPIB*iK{0Ae=GC?-'
'NBu<5KAoiIdu^9F%Ac5p@20p4>=Kl5S-X^l7(S3n%xB6EU;qd%oBXl{jZf4GRqFYQECFhGIX=tw{Q=Ot@u9|EQh7-'
'*z0E^qW?l70&N!-kbunGv5+zpkM%@ya_7k>+~BvpKe=tVU|^nMZU_0<Cezv$2ZXh703$nW-'
'02a<I6GnLvAM46+oOI=DlQIHm>kI}=qL(81~&wsuqE1flP2%?*Ji&MA@E1gAg7X(jc(k1D5zsvly@}QRl-Se}Ds*YGe$c=fB+FT<'
'88udo3(u6a(Xk5T7(OA0t^;lMaC8TZEO=>?=eTs@fz6_5BjDb=6d?f*g1m271^2{-'
'J@3xE!$n$wc%!#(<sL1#qsrk4_fZy(ew(tgg_Hm{Y5qktRKm39!Lu&A<2oz&rF`Sk(&rFYeQY9;Du8spUrZHCn$lrWD`BYjCPeQa'
'sdJ$<miw3wm`7+x-T}=fQJ&U&-'
'inpn;r}jd+qq~nB++>P_IxUdBBQ5(SqWkfxV1>{ImM(K9+4j(;&C+(pWtj#PHTHag^vWu?!1%kYmdwkM^=BZc*XgeTW(W1mV$~*L'
'{4hKcVHm49|54tH;Zf56FZH35M%lb+F6LvwW4`Z7Q)Ub9pKHWS_V%$$dPfpp8HgKb(w>q83~Xd^tY;_Ki3nSUL}|C5LD&UCg4{c&'
'8zsVa00ia|LL5}+D19se^$vHUio7$om2IXv;@AF=S&D#c$I}(!WZ`5R$FW1WVX=xZ?<X8gO@G>jH1y-'
'T5;XeKK(*D2=d#5Dto*$x)<YF-?=B-'
'(I!iy6kque~5&^z<`AbF3KH)imi<HEXpyv+~bCA&OeffhA{zF5!@awpC_&#upNu!t;43{FR-@fUPRT-pQ7QX>8{0zVMEe=>JlvUu'
'MqjISVm_afsGg~xc1M#N_ane2N7p%q3Q_ZDXka^Pej+r|G3gf$|!`6e;W6I9lvMz({sa8>w>PQ$=k<_Tznsa7nGSi-'
'6F!c|Z#PP6&DX3l_3FTYtKD-wznfzRsWE5Q=15j+k-'
'jpL<#8zQjm2Eyuls$Zs*1C;A$Or<&CvqYL5j5n&a_1pQ>6y#F&7tI~K)ih@vw1cpA>FvLzc{<~7_>Vn#WPMVMWMNbz&?kD(FxjLN'
'O!Ad^|duSwE!{WyTtoXKYZK~a=ex`F;uCFkS%tS;#pe^^Qj@wyO=@?G*iCj?;{yBt}Idz=vaXXd0dM1b7O3^d^%B3ohk7lchR26D'
'^6s9M&euY7&(6`ttWN*!_GBTjROxJ;~Y&|GcyAy%WwO)8Y=qo%}f{UF)m{*$Cl-A?;JP>^b!mzXcZCj-'
'U>t@BsD8X26YCoC0`0s=obBVZ=uI9tCH=pbPVz$lp5%Vm#(Y8dRC2l)9G=B?-'
'%0oMMd09XA9l7^r1gUvqIwco)Zq3JX`mnI}nDlhAPGPa5mAEZXg@bMbGudi=hxD2~ErcV*5c#5{`6xA<zaI7T=0Z3a2>WN&VjCR4'
'w~&(!O={eHrk3ag=~h4fB*R5A<K9LGsMa|1$Dt`=96n{YWBrxUg;HE!OyQ_AxPvMp64RMflUm{2?Cmz+2WY0Fx$FB;<LTf<@P4L@'
'v=L61EkhW4nIaPV!jS0o%s#gDU#Iq|-'
'1DaK2Br%&Uu=yY~#H>I#U1&TMMBmG7`=ls1t&RP_r4$qs;EkMcK>)!2JS8?LDYuFkt}ic;hG^4DTu*K8NW3c|AGYMiM-jL5XWR~y'
'*gS$Z~WZPdM5{9O&O#+>beT|e5l(Hf!<<8}jvkgh)k166v}pSna826nv9<w?J2V(RnXQLvajx1#RrOVV+4rCAfiKi;pCF$kUfHe;'
'f2p;4UJWa1EK7Y23tw@kXhF<~{D^*lEH_g@~u6IpW(Yjm}9zO8{M1sq}~s)ol%p7azx4yC%r1tG!$sM|677J>Ed?e#U#AdO$}Do;'
'S|933f9J!io<cT{cmYR|TYe4Hmmn@(~v7$Uddn8mj<mL+S?WYjHNCQ7!04<8<IUOu!4IQvj@UR5>Z6C=QdqPC}ix_ulaej57Mw|$'
'*Z@DeFNXAihq*)y>^wlGfR^3!2!3I{Iv>_P`tWc*uCI{S1Hm0_(Sn#R399lUu-'
'k4v$$E;zfS9)4p<AHmeCJ9V+a0Ineugu!#)&={PI8uJQb*=ELJuURzcuD=Jn_~0E#vW*p^i(S|QGdIzIWLn%V)m-'
'Il%ZBK0^sc{6=HdNivmHFmAx;TykD>4nVL7Ghd^Ce|$CRbBZWthc<4LCK(Oi>?Y+E%j|EssV1#Dxl=lKE6M?pWxoPL_DS$nyU+YY'
'-|Tlmc5#)KfjLLgBv)(FH=1|0Mc3PUJEf7cggozJW0J1>g2t~859&o1AUKsD^cZD$k(V8gHkDb7CLYyx}ntw2($zGXxW=?ddrO9z'
'=)ubn~(7!Vz0Ca>fyW=YYZ{9~n5x@aaZ%A_s0ezV!wqjb*(d55x#U{W9`&Ml!X0>(?BrG~jd>d}Cnc-iiUsF-'
'*F>w`#cdGD8nQtd%lw{)YFPT|O4V3LrZRz-'
'i;mByb{D)?c%o?Ebb(7b?Z;BG15h)DIDa5tSk`E_B~rNliXC}fjDZasOMdA|&1ra^gJZE>2ZmpSCtWs-'
'(njLrW+R+t=Y9(+LvSp<>e+GZ8wDG`QowHY-'
'M2Q!22l(L)lnJld)Q!YbGeAocjQLec}uVlJJi4u1;+KF5|Kjw<Q@THp~LA~xKz7<*&5m%YqL!1M1OJo04;#5N(v)mmI$~Oh(&}iI'
'@g5mo4&%;MFEWWnoZ{>#|w>)5C_@Ih-'
'Q&n20m}?E~?pf;Hh>bxAXPBOd#TB15Dt)Z#E#n>j6{p0mF!O5w0;^~*D_WHcb4_|h;^|f64_1e7Up#%MP0A@^c)VU_))PRLsIYzT'
'+b>P|18Udk>Rt!X&EzvpRCd|cV%Mh?k|VPiWFZ~L-'
'?a}%g4*zfvdwVC?h{3@O|E<b$U=b#1r(%R5q<6GCP9)Bd{_p3z`2x|MPI*EJ~_6@{I_-gokgM(pSQ~mV8Jqf+tpk<TcBK-'
'1wJ!Exv7u6w@ugReC&!!POX+idU{P~!$^Jv4g<tSeoVPahz$uYTPHS}M*Y5DltpQwp5f;c>>`18mUL0r;PrvZy5Y0ibX6;U;6ePn'
'pHAlYPu}T$pG;p3FZ-7*FJC_&=P&Gn$onglUm0E%5^ieD5(vlA&Wi4L-0-Mx^n@Y(f<yHPvu<x)IE-'
'b4i@vK~Jz|U%O96D+X;Vp+e{F`-P62MNreezoATDe8+;3~7n;Kn0p*Gq-'
'i(@!I>V#0_AjIB>w<JMhaGE}dR^;dLY@vrZd+L_gIaGovTaj4|Jhqz6*hj8}Kq)Jh!N7C!C@0s>Nf6eWC>vZk7`e(RsN88guzTJN'
'>m(rtYgmoz10S~ozd<+2{dMmHIA7L3nFvf`zBY}LH4l-'
'&Q1gi4TfX*h*Kp840Z=}IYe4bE<(9%6twI>*8w2cc7q2l9O`&?$JDBrVa3>Eq<iXnTVhlD1a;6eF%^?t^12(3_*b<KZau71b;pbI'
'Z=S@Q&8fWq9w}6C=v}QwoQRdi9aZ1gm!3oeM!lib&^WV^6Xv<iP3FmDeu9MzNXU({~FE&8ZQJ@DB%T0C1ZHSA@Y>AjDC5NI_9k~|'
'WCIf`g^U&}_j6J<DK;S%rSv6Pv?A)*CBlJyX0ZlxB?N!+`hziwPn3|^XHsjLmb^6lXOuO{V^fwq*T-'
'fFR*`P}nNggNbrIlvODAOnFXxy~6PqixgYh4)9@0cUSHXLtzHT-'
'&g=}{Sq`+mk#(JRWh_kdIk2h*hteTk9ws2OzW;iJ_o5Tqcb(F`DNO?o5QUi~zj!yZ4(SPy~?p3X@*R8B7Nt$}xN1ZrNnEOqLMfl!'
'ThlnILk5|v)I;-'
't~cDk&B*oisb!z8pv(r<Db>_G|+mG{n~JslXin74e$N3S|dvximS3F6&^ZaRs!SDBWjur(REC{}Qbb9y0_3(_KNC`|#23)e?lof('
'NbD3$XkmP<8|MW3y!ikt<RG5UtQ=;9DuvC(a}@F@d3JMV~<$Kz0RaXP7l2^~f?8(7phhVgi3q`a?YeSEv1_z^ay^_7O0iM!&hE4q'
'$seMPci(ocF-'
'><?0DpbAJu{qpb}j$`_oFls!7_I!F!jw#e9E^2M9<zXj8N+R7|;rd0utSBpac2XDb)%DC%2R*g+{2yyKm0IwXg5l<*#^+p~RBs+R'
'%8s{Op>e!Sr8uk6b71J25W$?SNtyA9fm`sg|Ugj>!@t>;BA5SR_Q?KDWqNjWCtS4Uk6l<KhB?x!8ID81l`K$fX+Q2H^7m(o2VH7'
'--EB^|cZQ<9*sVG1x!9?n6=UBk(t^eO)H$;^w`(OgwjJa~a;i;N*n{NSrT$E79N&}VOQFkZ#YT1>ZN#Y`$J2GQD_YncC`|l*E4$?'
'*{aRK$O7)@^oacp4e*{Ilp_`%`O;_EwB)MN%|G4%yl5SKvWBl94SjJ5ln8!P(pbLc=JO)4Wuck-&xzQA9z4mL*Ba->urN-As3>im'
'at@>OK*U-{X{OWj2Mr=7r-_U)yA_4#w`#sF*M+nj(&-tGa^>Ai02Ru(HOB{%jAh-*)cs%4}zze<e6F97cB>1t6!$z&-'
'3DXXGplyQ%miBjGT7B8#YpwgEr_HJiE=Xa|3i~%W#l<O0#e1$SK*bJ3sEu&*!<i5oL**6pbDi)h-'
'fsHXDWlWOpCl7W&>FdSWd;Mv{@a8*&4&#LF<#>xS4tE5EyU$1wRA?%W-'
'~8>dH~}nGSw{xn9NcC~5eSFdlWu>nP<e()U1%n2bOZS1#3^{HmXD)dc{SC}qn(YzNY&QY?uV-3a82-'
'sg4FyiWMarZd7=DR7Yu_`<I$`dz-5@vYJHC%U?cKRkv|7n4tH_KZws2lUL_$P+KsdkkVrHsi8-'
'zR^5s6G6DBz6X@y7)a(@gP+jonlP!MzAxf6-'
'BAxIGf$vG+%V07<*f8zCVm4vO8nFjb15LC~eBJKn`mO!$WFsBUy`bW`UH83UTH29XDm);S4AFCD<J8l(zP*h#Vnq_W}wtCq~#|5i'
'Dk0q6cy8|RjVebLAmlUuUQRz(SZ}e&2h7+?4y!)-'
'St}S>TmaS@wogM?eZMbis%u7m6mw!A#m^kwrKn6Rmu;d!0@4<ugFf6a)1w_Aq5WsHk&Kbhfe6N)WtK&=CZNf4|B34BC{ocbB_~xy'
'Re?X0~A32ZobnFU;dWNJwJ+opbmd{S+ER@uK#tYR+uW)<$g9k_@&CwBg5SI@&IiWX=*sMW#*1A_DDQHTH${Z+m6j!ESb0gNcb#}~'
'@Noi?&I<s9i@mE=k`{Rqq&29fR$N#64E4YFdWJ7T3KQB(ESP%2wyUR=vjOyuB=eds}xXy2WTAK;(0mD=0YpuqTt;HGx(cj&zJM+1'
'p6Tq0AsG9%_HE~7<EW&)Ovc86qv7=T#%+p_hcPaa9N-'
'9G$OkK07T&p{kleVxGi&+WS4kbZmG3?Brik#<aG#&y4W65x<N(L1IN8~MssIfB;&|>Q}H*q7i0Ih0iR*$A_D8Re!hjcALbECB|E`'
'o}RuE60JVYSB@PYFL1fNvKPBREFH8z@p!*Ebsg>0?!TEcs{4<Dz(61i)_u*w&?JZ+v9zjwdm0jsG5KDnem5!M;Y*x1nFQI`>?23R'
'tReK@c>U%<dzC^CRUN?RdX@Ux#91!8gxFiUweLna6lLzJ;Mg24L?&1@eNQvFo>GSImlc0vzW|40$?C$-'
'!_`MxgR)T~@Oa<(fMOSHZe#XrLqzZ?dJ+F&drF?8c)D6&Y#-Q*jGG-{C|dOl6JqbuE>QyhT(PEHld_^5*8*aWp%E20ny}4dfU+)-'
'RNa91-rxG;?nl8P@qG<F?kznqDF2M{i;VAbA0zc5acJ3O$<Zdf=E#pF3;5W=lJJ76^ulA)PQW>8OO7w#PLo%#WTN6-'
'Lw1+`$JDXn?fHc&~T=s{7kWC=P7Ck&TlrS5pE#1F^1U-dnnZVUzf!zqy3e3(Cj<pLP^1s-cn)Wr(~{uX^c~>6-'
')ZYO0AUqR%1qSd6p?rqipuNkKn&(K8zno}D0g+uQD>YE+e|HW7o10Z!SdYo^>36<!5<%&qD0Yu1>`qVL}4FQN7*VNthKff1nm1=w'
's$`i1{3qwHn6#OxptMZxRkBdf?nb<8IA1k<w-nMqzyHskiuXW1#6o3K!B%DI>ddJ=~UTowR9)5yscqHRMjRIy>)k(?I*Typqa-'
'u4Jf)N(fv+p)*_T}XK>Ku@kdJ?)ajQv1uc(z1W$mHu8}*=EvI&FL1A^z*17rekh<#x0cYD>pVU-'
'c9EzKL_yKuVPk`DyC~S!@YDAPMHXvQe=y5sHL`G-hiu+r6xJM?QH#r@cF>I6yz-'
'<a+?T64gZ9MM2EI0c5xzT4DHx&U|;qVJ=Dm|V8cxC$+<T5%}C!Sx6SaF_{h-'
';`)tg@!#Z(xsm4q0n8mx?UL*faxa)&Np=H%osnR5{*6_UWyMLt<{!$a`QOZ;tReon8y@E1`G@kqdKlwWphXtxx!<7|Bo4X=>zYY='
'i3fM|C`=ptXx7n1qp}M5ocNfQMP1@3)$6vfulEhxohAQfpM0NIR06KJ0LLyQIj}5a`mem&T!3vXHD4%<YqLx>v>OQt=2A<<g=jjx'
'%Dj``=qYW)SzY$YxCPhTME17bGr@oAjJ|980cwI#=+=CLvX6Dv;v6_AoESXdXH~v+1n!&AGaXYiw23<X>5lXWQIo#_FO*x7b4(Z@'
'YRIr=Z&`5b?pY=5@!L6{9l1uEC9;vsw2Cr3MXh~_`kc1~>ao+5gX-'
'`^vPOBGv7$o!F<4f`cw1YA9q3Bdg{Gmxh6Ops%Kw<KJj7{dUGHIhZrC<WCc=(iQ7`kVw_QEnT?Bb~T1zgCIu!1!?QutkB&ir1!ve'
'8wWWpe}FjNPa>g2EHz;{^%qKBw=QWUr;_lyB32Z+L<^%_wc*>y_9C3^HoPnyM@)k3i#rv$G_~5(Zq&<K)X(vJkWu;Y}5Tj$qidN1'
'||DHB$Hvx0Fxh7sl`~1Cg1&oIuOk?Y%b7x25KDM5Q}|3$GGuHkc_bq{?3SLEgD{dWVx)hHW79M+(4cSjmZkr&PVxPsd=f`O&mF3K'
'Og#k&-'
'`LzpX3fb)5;tpG5WE{J9<x<NdJQtQZO|D{&+#`Pe0rt?EJJmKA78MZe`+zFC@~6b=ajgCW(14A*gLz6)Xi=bhs=nj;?%QTsl|(qq'
'I9aK@s?6}BT4?8q-h2PciB6_C)oY|{^-ZU#mv9gk&{mnVFz;r6WIkCIl0Jc=|RwJef$_KtC{Bz<8vXZU?8Q-'
'PMkPHNQP?hA<y^9+mCe0f3?{%zX$G=OKM>USB(Q4O+5i8he0t>yyCN5+!NpnDRlC6#fw7uRiUpE1(PxycJrNgwo<pS0(^3m@f}#b'
'=0v97*TTqANU8Akhw?W%rl5i<=0vH{kO23!z!xxCkJiB;CA?l{n!}eOSgMlE=^CO;>J@&OA3>UA?SgaQ_Q^z0lr*emA?|f*IME#J'
'`BOIVoBvKKBYm9U)8tc^rr7$rifHTL0DQJ7*RI*mk-~Zq_uz(sKGnXM^wB&093r8qx$gP_+F1_}v}BAiXlrXR5Y%yKs-ftls&L>2'
'5BQhEnS0T$WxoHBiqCgk_tZMW9U&0Rj!vx5h{LX)8Lr&V}#>8$Gm>GkuYz5*$j74p-'
'=qkC~RFS8LsG&=xF*@{|(!iM%{`6uW4Vb+;Pl&*Z<0&LF}U*w{#PFdvtxNG!DUm>JX>vsAbaN;L6ZwgH1<{Sov03`bRlvMgbV)>f'
'L<)S1;_y{RZfg|-zRUmEnA?EN3yn8Q^SPY(9Z6LyuBWsqUPm!+O<@yO{3YIn3;O{<Ao-ZkDblM&U?@eQlOjz~~lo2^`49ZAXq1Db'
'z~-'
'nNyu;J&+<U(u(9dQj3w9?Z7ug6_M4NE)r5W{=mg0i#QOzWnNeIjq>x&R}bFlfqdFFIPlKq#%rkpks4l3zy!TiZIXS0b;a<18r;RV'
'YnhZ&2+}sC5|CT4VPTvSl>ti&2Cqy6WMP0G;^k`Y@K}M*)*464F=&sVQ<3MB}gQOrsgVdO8R*g4p6EZia_RPaNXL*`Bi-@T-'
'_IY3F#gfmDK#JSx2U6@6Z>*BB8s{YV9k*F#IfySFrudwQW8g;uRU)xC@GiVW+<BcU~<Hu#2L+lX(b0<`^S0hirhA6967u+(Wxz*O'
'3M@V)K7Zu~Oc6IEGadhn2(X6-tReoC&@R!PQkBjk-'
'3j8XE%)s6lCDi67nfY{4l4|3+|%1Wjm7uMb2rn>uiQKt40FzVF{_Pe7NV7771gOlLqD!1QJQDF!4NA%j+E$9`XAnK}Lm4(-'
'b>?E2rf#`RDeIlPA;)asiKG%f6nddkfnCkbZGE0WRz^_qwWkYE)G8K1laoj{{bKUr^Ii&R(45MBuso{ab!zzY5EyjzM)-'
'uq#3m&Q!+n<Odj@?8W0CDos1$zor&EQ8V=et7}0V1|PmOKf!UBewvdS!n0?f8NkIzEuc{zl;jGdI%OfsoT-'
'}W&w4}yU{%LOn0<)oqkJS<H2zHG}b7l(m*sy_)GUA&;jHf!%P2mGV*!O(?+%3H)m5`p?D>-r34b|(*8@^d+<f4rZ(p7j%ySq4-'
'nSgc#qK)2(XN6Wu3f4rCt)OZlQMSGy%@;rAa4%IH^9K&N6JsS?u}s2mgxLj;vwA!7&Ll6hXos^!jlSF&Ty<$R<3e?$lsk<wVxd^H'
'ar!m{fL+$iKq15u!FtpcAf(K`SMHv4^c|zl!S-xj_L#+N{}857~uW*B;1O@B3x4YIDe-'
't@%BTt3l%x83ppxWsubd<7&o6Op*ci1zS`<xwM%_KI-_qtz!Mz0gAE^v4-'
'U4><bvk*XGaj7W|q@R+!_GhJbN`#Cm*u!7w}Ns3J@^LX_-'
'D1CRQ`bL~PbJjsgjs!VZWB7&rD6bwY+O5TJD79a`HJ+fxU&sYE@1x5I2JmYHYD^BEmauTt{|GbS!#oBsvrYSpe7<8x1m-'
'*PO)KRtZWI23HA?qx4^WpmM=G$e#i<g@li$m>2(|i?VuHIId_3GqQrezygJ_+8iVNJ-'
'&<&c)~{hd0^54@;fuuBK8Oe*NudUc%HyP8bD4)R@<85+keUz(Hg{8>MxKUkedwSmURyhg_g*DT$czX=TrfNI6PKfUS9LpaTT?5Ue'
'9(~Ksm4i~Vch`F)c$5w@%_6BCOPd2;l(KIAEkm@fvnEbtisOb@75|r$|L!P{A?c}pki*^YRcNBWiK%0njOgNLaNDI}OjB7a9oW6P'
'+SOjU>f@$+Fqh!+Gw~|es-rdDH?40;;YpV>I_8`(@uOL_#^=QO3WF${(ezt|&JsD2LtAoj7Z)lQmak!V3l=ozZs$4TZf}usW*Zub'
'dloQ$@{pLp6vhV$ITLkUu6f(|&{S$)#f}RG^NaPlAbI6!Q2NKw^9OoHaQUg-'
'h8~VyxK5lioP2#78zW<+OrVZEgFAX^sTaQfz&5yn4`x>E2-'
'*44Fe@!a!Q>W`gexWPqXKH%KqHEK1(C5AM9x0fGe*erv<BJqRwr@s3?8&%!5e412jg-'
'K{kOf)QLH2!h3hR%r3^`_Kgi9G&IggftbRAhUD>m5>U24p)RPD@6xypKF=a<yp0f8xu$zu{pLx^zt6q;Q{$xW3|aCyDviF5!RgKk'
'_#)o#h#=bF3Z1mmG11vb=Ct=WhGgXCeX@8^;SmJf74`<idCa>yzmM+zl|g-'
'`@Vh?kl#o}l3PZpKi8onlQ1e;CSnt6x;9&pFv^_;x+*W)-'
'tFkLbbB!xFxVzSYf9F#L=<fJWJJWt<R61>d~q@4#j`7KQ}YT)|)2YjXL1$smOVIXkLWZID`=;9S61I>!i&B#ylBD}RQ)qLgGc`Wt'
'-?j-iu<vj!QEh24d(+)5o51ts6gWtSYl6L^%;@y~J*>-'
'>5RFX3@i)izuo_$HA(KLPy7UnGf8J9)1JMbiv}v16N%R$oTgO#zFkIPaKx(9@;bre)yp<=I#F8F~meE}?7^<oPw~ms1bt-lTipuw'
'`Y=YC&cewg&w03G|2BDTYT`Oab9Na%4R>fi8q)gCIg}JV=9c$?9^H8V&3@P_-'
'O8B0w?~A(C8z1Y*#=U$}!W+f5G;>!@Q^k&QyQd3&5WqE9%p0tBV*KKLJzGW!)4wyf>txrGf}!_$8~2aAGtg96WKrZh#PZN!TVd7~'
'on?i@|>*UIvX%aPlp`I>QGNn56x*3XcD)XE~Aj~?X3T^}FeC0nCGVE93~t^D%FAAt%sw%h$ZdCW+-'
'eW?3Rr$GZ6j)}_G=X5SpYbxa6Q+6T+1Jgi1Ozw+2?Ix#tZ5T<YLY2>HTm9_bom#GL+-'
'DDrr0UH{`f$E(ZECL$OU!J=caMU7{Zf>pnF~BE*k2Z#?=kL8aiFi#s)qJSTh`#V&<7>J0H?_{FLjq}0~Hq4OXE`QXZ|;AMtLD3x^'
'jT*CXaJIcyT$zn2S3@DwvX(4ZAgmv_rG4;Nj6L*b(rW`kKf?7@U!>1(wX`ozS*;v)zHr4{<N)oDU_c3#r6*jb5T>kpKmHJ=8mt<L'
'VIJZIXO0g%2OhH)G)jhl7bgxv}`MT=a{MDfn%RJ-tS)cfv)ApZq>m3#AA9`~1ddUW`@h@}cyJvXPAB2gb8}yOtV=J|-'
'sI5h_0e$QDp|7<W{AirSo<RwmWgIwB3bgV=~}=jl}bfx}+j8_76IH)ZR5EI&SMRZVB`*DB*W+qhxva8cDKH!gF%|KLMBD~*1;s4R'
'I`+aJA;8b)w6`3+bJkE#GsQx&bniQT^<qdW;-D{R2Jj|6*$u3eXh9A3CnDBm_M-u7=aksa$V>d8TXn0qW9*qBt-'
'i#=Hv9AYxwFHGmOFqeEc-1d$Ao-n2|DW?#ou&+sPRZ&U(?W?2PWPfkLo+dfYduqQQXKqy8oQxEidheRUGd4PVz~PCp|3-'
'&`O}c;t=URVwkBOf|U14h-'
'g5vqVYvQ<IU&!Usi7O(VTKAdOm{LsyaocITOkl0!958@$1V1FXIm@Ohlc8}e4hFY`shn5m!Oy?*nG<w&SFs5?sGw|S-'
'AHUQ3fjIb3tX5@2MgGfL!R@0m+;7^P7l6ZP!zR?a)g$+dIS?K!5p;J(5S~Q3$&a{(^9PNf7~N&+Pd%@`l5^v3=}mC|LXW$mWXZ7>'
'g`6?yLPj#&MTO4jwAMru*#!`Jy?{$)cij>lQ}WerFYd;Ki?&1PXt8GI`E~kAtXV>GpMD(@l46lIBq5Aa*v0d7K|aa1}_QPTc!8T6'
'(e5PpsoR?K4Et-x@lWvvywvzQSLRM2;+D!1KgG)8{!EMx#jAId(qb{Ucevz6WXGB8(i3F=S3L#*Ji23-'
'c2|VxejBdej|UQ_<xKs!hj>~r87Z=VqRIzq_^E-FM^?VQ)DEgL&3PmMxX^|IM!&XB}i6J*Oo;uYv>is2#P-'
'Rnh`v9SvriN8fi&Dc}Oy#5Yn*fWgXK>Oz{@Ad6K}oQ|LO3>{0H<^Nr*mbo3d%kv6Bd6B}@%6l+o647nr2>KbP&f4Ivy$^1REjmF9'
'ggN3c(z9%w50&s!wH}Se)^kl^M8TJJtPIaxZ1l59<KtNS-'
'099v+ZJ3U=V!;kvA<Pku!+3)+EdTK#m@{g}QPbP9y$6bgz~!@MRCjGe0BsykItS=w_hDiR#$oS2m|UdS^tIT8jQ0cv|68_9U@K)r'
'd=$qFpiWSmn@sAGKJ;w>#SxDX%ZHX~zkaQPgu<d*ez_cb8dk-ls9L%|5U<C8)tZBN(md65JN>b-'
'T&0r6RCj_8%4y(4g0{P;0veu$2D8iaT9x|1!w^Qlsf2!=#lFt~)t(NSo4XuY6%+@p+g1H0C8j64JQi`>h2Ayk5RPtO8_6Qpye(wg'
'1$CMu0rBrH<Ub@*t8J9cM3F&?*K3)s-'
'SL@WQO9L~eYw#4<URLZF|(dpu!tBkI>RYcJm!@*3p|Pk1#+tFA;}lPPC+!|h|MO{`C3Z}cQ<k$`v!yg3??B@1J1Vri?+`6=Nr5V;'
'a-nr2}Bro7?ymO!_V!Jf8mq`ZxYzc)?HafI)%NZ5u|PtXO9qf+PV_S&C7^B6J>f7(-zhcwJxJc)}<eCxI`kyt-'
'B^|kP^#2nJM~WtKnNrfZL7<uX?j@x~P;OS-'
'*VmlYB*=TG+7M>`2B?mb%4TB`y)%Y*H?yOx%o$q6vJ%I)+uiAX6&3oJrnmK*J%aiyIbw3Mzp+7;eg9+gD|RAf()i3a$;hg8jAR_N'
'OWMUQL(hs)T#9A6u=ls2fLl^J@$Fn5PFFMP|1J<QB(0warY+)Gz#IzbQM$+=DogYe94b7wfeBUr5iUVOd;4Z{)B#0ILxuQ`Jm!PZ'
'8&h;Bnu0jjId<VmQJOzYXef0o3LD*Yi>mukt*Wlda;2w(gF3?D>+PUzwkT$YP;p)q#}%OGTIz&S1~+Q?xXu%HU`~50&6Yp}tEerd'
'Ne+QpPIsMk6ZoHpN6gbr5~QURQeweE?CLZ(j=FKKn=8#RfaV`<&-'
'CZWL6EH;+dQ3Ez)HYoMa#%?j96U*SL}ZsV<)dt?HBxV;`Hf)4mUTNuZBvN5%imYUd5WR;r~2C}7bua=PMzbccY%gsnk1ObG?(}lt'
'0vwEMJkCSG_jcT;aYidmfWq>QgF>_{gsmS>S9H_1q+)utlNPR^6FC5(3)MoY{uQ)9XXa2uHHPttSjxs-'
'v6pMBaOLu*kiy$9`Cu;WNz;QP;+~tN-=q;!Hljd?4kT7D`JP^j!-N4PjN6YAOSeu2#%x&URRuGL;9yJ<P-$DuX+CjDO`p{Zg@-'
'Ixg$V$Mm&=R;=lOlO)U|K4!{berJ>@T1n{_r)5OR+QizO5O5?#{#RFZYl_X^<&tmL%m<ri^R*9ZQIF*s~hI82cu!pg7SXhdM){d%'
'}TM%!fFHeK2q4@|jm!ePBu~hCS1S?i9~RY?1dj6v$`BJqjEEmNCIg#4=B;5o;bn;Hs)FIa7!HZxww=JSB3ML+LE`SKRcv+Sc*aVF'
'&g`4nJi-IYvRsYNQ3xmd61Sq`#yJSkGdxB`~m$1CnI;2rPj`FX42|fT&a<%{{_Vvu+A9=k4mdYH<}}O3c2EuO|6%NVw>DV8C-'
'YxTcK$28*bAOw`fP&{$R=B0q+A@N#q7Iny|GAE0W{J>Fmj@zIv!<^BXazg>hfmA|6o)N+1lWTilnB#Sh`P`uUKJj7J>+ka6@s1}N'
'|7Bnq|2z7OK8h3HXOFwi#8PnEDCuteg)@(zE5U)x-<yPLZ!Hp$}rcmryoBe(5LE|wpRL%t<Hr5sTg;-4S8QXKo%!wIIzV<-'
'tNS|4|<9vDD(QcM)6xP_xg(1i6bH(noF!97;6*^{iN?((N#e5AifsP~_;)l9k0*w_DplcRaflzfBEfSOawzVQShpAZA&=)MPKeIw'
'1v-'
'ODGz3p)<j5g<BAv&tK>3|aF$Nj&&ulp)xr2>aHuonuypCi%Pl~>^GZM*u5tP)nNQoH#bO$R*A6_zn7c~CKkW*`<!<fHeXVm`I5v3'
'G?JLdZYo0>Y_yBipqsk>I#JGyg}ggq=@1)!^P{UEz3`aTsT9{6c#}inzRNq-KDNpIjAz=cxk0{u-D9X-'
'Nkty0G0n_Xz6OjC7)WVe3Rw;@qdE#A42+-Wuv?Urj&BP%c}LPE4NnC_U>2>x;A0@0Y}gU~a%2Joh%}>50+FyJ~8)rr2{-'
'nfsTbx%w-'
'+zY%5|TE*vw%SEkV{Q<0`vNqLUQ%rkCO$d##e4f<{)&xd$?|Ldopc!GxRk9XIX;8TGL%mPHj%ZiOO*S1niN*%;_h~EXCA?p%<Nf$'
'cjZ~SohlS#EMq~0%vN)OG{!NQeG?PfrP+vl_kCuqs#z6kr@cO;SpI7S~g%Men8802WfzGdR`&Jc5WXcest>Bf9MJS+J^cHedRIq<'
'fchtv9G<psF<g$}|5c#rXtqIk+aG}0n_OCViO^t(2jz+DG+dmk@()q;jfg=UCbqdWU#+00l10K(7&KViu80HVw?Ul7>Xt6;Cxfiu'
'FBI}L|Fhfi6ZjSecxe8a3$ofz$h~==P<Ih;ljx5?+wTVLE;cI(*CQ|;OGO{q`6wiFzyp;q3Q$oEZI+>=9G$}EDb`8lEG`hPyx~9|'
'U^`&K(WH*$4k>8+VbT2`qg3yga=6W>k3Ut6xpNQ&1!~s~J)mw`Pfz%TT08NaSPYWUWP(TLSPJRT=y5IEUhR?TJ@qVehLcIFy#0k+'
'niQ&s8ecixhTTQWU`K9!HqiG_gm#=n&{|Vrcm`o}jbm&R1Y>PJ)XezTOYi+H>W=?|c$GUxN(6NlN_)zx{2`P|5W&|rQWN|6=9F+z'
'a<#7!W*_EuPT-e%->Hsxq@uw0#E?^8_l`ycMRUzA(p^^S+q*kNI{G-'
'd>3LDRX?4z6&)HY#pd9TJyg?<#uFwXKDk3Mc5N`1`0Zjn0vd32OZ*<TCAUA+X+fDBYf2XtYEzJ0DcOv=*`e`V!h_>3#)sB~JTivF'
'Mz<-Qo2Cz8Ap!{R=qZGcb}f9tHU*ogKY&(u*b%XZ1a9GEC^J+`ga3``fI)Y4Hae&Sw%%w*$E@-'
'6sWPQA%e%dzca{YEcD$MVv<p3mH|a6Kz$i|lATt&VYT=@kPpGLGt0Omz_M<!|Wl`LSEdzdE7!m$+ObrB=7FEXMs(U-'
'VC({ghM5?yiwh#wkN4V2`TUm1?7YOf)jAt-F!@m-'
'n%ly;N$*NeNpg(p+PphlEQ<VU#q4G)X7oE>KHxXqu#nMgPS0w|D~Mvv0|to)U(pt(Na9R99`25AA|BH}e1!xA&n&-)u-'
'@4#f<uorvLy)}zLHNwxSO<gMbS@#wh?jYoHuSB2xo-(tkAo5RkXVAxy2btnG6ooLf7Piz2&U(GBF-ng|&3}lyMiGZy4E;%y{NjJd'
'J7b}haO~hLbj^w#8f`B-'
'5PJ*MnQ4`8x8s}}z%<c26Q{vL!eZL=S7sljrM~KCugsU%F9y=33NA?c45WY)Xuf5zrjKaIlTjl5k5NzF^z=k8}UYwGGhMpo?EA&A'
'rRY$6%_ozbwP1elZhiK!$OyWa25^HqRDj4k+wVEX!-'
'es9vxqRt8q3(y?>HAO+&oY5QoIt@PZmj&RcWzMoXgnfuy?17w<XS5ywFi3>@u#V*%)<sHFU1392@*)YRP;(|{L=I>c#6f568Rp~?'
'&gm1b<1Jwxf2(yp6X&}4^Ht&P9id2rr1p4otVXI65auhWm7<nzJDUlhjj45co+pxWC2yn1sLJhW|@{msp1<Cho3xrU8B%_FA5JA3'
'!s5#zNKfS7F!+^F3X4H5MaV2YyuHZ@#0*)mI!L&#3u{6AO;U-XG%h9!>hl*0{3vj#(p_FliS$d_?}a7=C3t1Uh2Gel7(h#(n-'
'@K`DCfXPI)oZ3$nIuwCclsRRdw$lByH?xES4bjxs~e_w?#l%=ky8WM=h`x=<R%mEQ^f;>EWw`*x%UW6la8#Wy@g#u?<>SR<hzddo'
'3qKo<-^CI;m$rOb7PY6-'
'gpPaox6^wm)9kKMV8sesn?Gk@F7dlT2X_x}L=!3%+HYf_G@w5w2#?iV9HGlU9BDhgtUV~RO#F}oupiqW)UIV`PXZ<5I!J2*OZ>9%'
'>G&ZBf&$|3CRJYl&%%aihEbVhf%%oEfj-}i@Bu#)qeGya=@SVptJcU@$5sp^4WR~RD-ZG}SUl>RK9UdeiOo#>`@DsGxr(`T`6*?^'
'pcgUByf!cy<h<hV4oHmzb{r4sKaVNm0*h`;02Cv&YtPCmgdaO|Q~lO!;2JA^%!d#)mYzo2FMrc^|R-'
'`2cj>+s8EJYJtF>5wUqliYQ4t@57;3?lL;0Wz|{{K5Y(Ygm(+nHY1J)#bq{F~Cp6r48KSkLA+vuH<9db2RjCH6p%7xg~SO2EN8NS'
'jErW)!en;0x=kRgN{ZW+N+f&aUQza)EzD5L*w$8TzZlmf;x>dk(;ckPqG~}iX@=yx?)cTnS3+3%rY8u#?Xc9rw#1<dO#TIeig$gO'
'QP;AZI7eW>&|^;FEVF1so|8q{MPK50+JT#73}v&<$ZLnz{SCp&re{t_^l5CYLviq6n+hrJ^BAQ7+5OE0tYEH=*2)EIZDUvAnTDBd'
'cD;$<yCXld015i+jez(E|FBx+hr4(w+4{iqV|;r3h2i28GI36hpOs&*VfTXat=5}N_^7~5k!rmfQqrEgRr`&<^cu0Q}5zxhRygDC'
'X?<Hktm0R0Sp@+czbR^tKC0+92aCGac!ablLYJL%PoDjGwoJwS@|$Qg^JyX*Jmb1lGPl`iGZ=-&(81!Wi;!A-'
'y?84*@x>19hYKk(FP1R+D#(!QvtNDL8>@ujtt^2gLElEJKFPCab=%+te_81;?axy*yxA`IY@*>8m8$vHgCtzVa?+Uf3vd7Cl!5Ao'
'o!KKjHL7i2LMg`6-'
'u6nR)q?wi!(wTKn<|qucDw@PW<(@KR3}pwOJ`hO)4s<xRk&&CiJKD0VCg|R3VeCr<97n&K}%LDq}XiR7M*BTD9KUHfs+_scR9sAh'
'M~m*HCu7jc&ZsIt<*jQyerh-'
'l`C31CfwZ`P$<>8SJFrNmw3H*jKS_r$xXV;3XJT0$l`RJH1C$)7)G^_4CC|cZR!b0hVyprQIol+6+q}HJXu$5{`DpP5CKPVUmIU<'
'<XondO4Q6jo8865klNmqAF=6sfP!ND>@l~UqOHjovHvl6kzVLfn}>(DS9TMC`zi{6r^5yx6N7+;iriA<QbbiJkFNI5NEDYRrNQnO'
'b>*6hFfpj>?Vx*n&rh_C%y-fL%?`&x28W&dUq12u6D0=#`myzt<IH$*Kon)xozClo2RVZIF<50!JM-fut#u`JS_V@-'
'8iK&w0vt>>52d;RAp7YBa7~cxb~2<4azdcW%6uy-O;71+o1i!tc*79`gb`K798g2V{JQqJ;<HjUy?xpEVvgXZovSD=Kg-qB(%t}9'
'Wu2+Ug}$~+Rx1@4Wt=CR}5l<#4o989OHKb5(GJ489WacqTY!_O{#S;De!GO@~uGlZ(x@03)x%2xL!67+K;@M1{W+-'
'eK@wP0Qyv#P#j1dhGE}tN;xV(<x039;u`H2P;IoKOcejZ-<dDHyekrI-@l~1KVy5H%%7#a_rcEM$x98Rf=)|fF}y;M1gJ_-CEzGK'
'WE1*O!qiT~DE}cv)|A{ta*5Tps+1@{;MR~pvou|cGHbdrnGRCQsqk;T-'
'uGx8gPD{_7BDMbLezGC5h}$Z>T2A`081R4g5t>D{UlmF-GtbC9QTCy77K&Pl0&CS8F$gh!|JAnFUw42Bk#YiLU6PStHD0?!J=Z=r'
'p{>3XFwVL<Swf{s44wh%i2=2|8e~iUaq*1jxj%MaAOhN22lQM7<rp=?@U8p^E^6t>{o%;0jbOdu!cAGXA@dl$h1jf$77zdz<-'
'Gwh4<zcN?NKJ-=UK4f-'
'@oasyXl~y~Ydy?|1}ybluCh_IItnj;2;KyN>t(T+A4qp>W|pEKsw_i(|K>E6#x#0AMfT;Bz%XfmdmMEH9z!hGCIsfL>vx!qEsR2j'
'*dw2+hVYJ}EA~&6R1Vf+x1v#sba7sFlrP#Eu&OVH~7;GXDn-'
'4Ph2?l`+kf{8DM5#aLf(r5PDv?m|jFh@^}~>9dNq%*Lq5vGXyn99~-`=Hg)2g#uwcy3wLoji68%OFiAkXJA+E&l<v&-'
'KsGQy}1v?eJG26j1_ydEN<x`#p!>_=QRoN$#OfBjBN@GFhmx5a9CMk-vVcufIwm7PpNXp%+sommmM%lQ>jW1efQ%W$O_4o3MQI@l'
'GJ_sf*D=UX3T+LfV}T$%|f@JI7_AP?m=4(N14MR=~g8?JQ`Np3Lyy`_OvC8vrSfQ$Bll0>sH_P_9F(XH3587ayDS;mO$ZUTj#J2<'
'IUG)STzB3Gdb>`)QR*cqje3JkHp^vGvIr14O9gL>ux0DORKFMC|l;;2kVs-qny1`J53lY<f@+Hz)TYSVUaprMMCR4nis^_XRavAf'
'4Oq21)z4H)XfMR6$K8{2wVY^_O)sSP}Hj82vR$Ms6R;m4@Oyr>wQvfUjCR%WML!}u5|NP#vl;#d4Z#^ul1)d*XX}mHXL5qOQkf1f'
'-jF^vfVGC6uY%Lp507}k&QisJi3O}jEKc}5NI3pp2F|M$VxJ!V8jh1E;C&I3zOe>3uxy2WSkqnQV^WdEpfV_9Xi>eFQ>pMm@8mW;'
'Inkq_OCANuiZzaha9rDCjL0uOZoxFbE7K<YdtJuj$AiFM!X05sTGr+CE{=ECaYfp%^-' 
'kzdp1pt4>xnnvufh>)9sT#cH@95<Wom>bMt+a`|5He<s~RG@&qTXps>rN=$+D4`?k0~L$Wj%F*mBe#7iZbXW$A%Jn4&mqZ%;1?UH'
'XVl6f<td*BAN!Fo@+ZY92`E$Klsfp#reqr8@<$4Q7qyKCU{1lr-0jP3=`|NVH4+&dm)LFvA*8tpW2OYy-Yll5pT!A*?!xCG+jr%7'
'FdK~*i)veZRTWoEQWIJ3R$x%D#?&%EijP}k~*laOzR53uiU7{Sl3^a!87T)_aTpAIb)Bp3yPt}YeQkXUp4;^z}t+<ZSG!8L>O<WR'
'#F<oV+wlEn=*#xLLLLVQTNd|XyF8K%m`9mMB@xYw;I38YjtP{mH-'
'f$WeTcJKnhrQYZ7m(tXgrJ8WmxNqa^v0Vo2yVpGDex1No>X9xIgYVYmPlH|}ZwO>2h>-24+K@R+`30t~3a=~p$!wo_ns6{4Uhjn-'
'99r;wq;8&_sTphpF-'
'^WW!@RvOF7AxKYICywe~qeiIZM`;7pcxAqAWz^Pr*4v<j!rs7Qwt@0XQb+csTw^?ye}QW^g%1hDIwMJ8I{w0uoH@&wvF27Njp^;;'
'?X)JTgf0`VcVb0XUX66ee;>^PZ4~Mls-'
'3>xa+MYD^dOa|bXdv6Pc>ICS8EoR=C)WIDBeORyAE8ndddX{*lNwz#@#&3NXEW}P`{lCAs$#NcdlcvVLMBy+Uie}8q?AN)Jwo8=W'
'JO1GkLO?|4g?4%&#qQo&&h<fe&Y=ZZ5Qd}g0!H56ACYX#Rlp#(?LYXtd`!CbA2Jx?S4H5rqQ&@|kS<Cql^Ruzc&AcD~iK^OVT?D-'
'^iJs=`frXZ^@UPPlkBH=e0b(RA4W$0o#KpRMpoIadkYI?h+879d7Uvv&uZV?=0Byot(1gW<2}R=X{Y#H|k}2tE=HDKvzuD*TyAPK'
'>U2vU*II=^NvK5f2Oj(f7!D^IxQGm-ZN}QRv|JC>I!(?9?@sGA%w3hRe9X3+F&luG@5j5Sl{mEE>-|+7Xw~@-'
'3`m$%{l6vU!T1)tVvOPoS%`Czj&Hi?DRgv#oZ??Ss!UHhk%z_E-mDfd0cK{@Xl+2MOxPNlBGK?ZZ!6OhnQ3&@?bq?^IimK${U;)d'
'&q4C5H2uLgGu)UH$gk9g>;L5LFR(8I^bsd43NgD!D#_RHQ`L^lQNOWmvWJMs}6;jiEo`7A+U%dQBsHJshs5ej99zx5n5I$9_-'
'm*0C>-&5dDVlJb(D7N_{CE;^n=HTC@;7ky_{53&|G|glPIa`$-'
'TSinxcMlib&!j{<f!P|SW1L)i5BP0as6!aULXz}QRnO>S6oIdqYP7g_bbZ2?4!RtfwLMRD5AIxCUx;j>Rs2Az`Y^a0ht>?HWzR&l'
'f}R65g~ICPip2iS?9Fg(CI<-`OF&{q)%WB(LdjaIS#%2x4ZJ(r!`3~=@cb%%g`op&M3~(-'
'fQuEHQh9ow}mc;!03*fn4d9En1(Dm?t#kbc9(ZX^Xc5xaQyFY@2ca~Z^G`F^5`rMA49nNb}V@Ssgv5J3HuVF1!KbR3)j!}6~{xYl'
'f{95cqTNh_2AaT@JP&5zEgCEBX}Fux1$J&sbFXT(*AK$e>?c3P}XA+T1WP9f5#~4KOUydiUF9x@gl8X;XNy%uJ>cX4Jz3-'
'1!OBy;WIOatD1jv8hFiveT_Ils3$50pgb_tZQ*5P6B-u5u6P^hJY%5J-zHW`aynFoPLt-GP8*~2bklxXbX;-'
'gyWgU`ww21Tu5<FOBMSPrAa5)tFO@{Ae~w}`$&^c5mwd0{3t&HRFf0NVAAZAmFD?gezCC6Uz426ON3sK8l6JF+$DY(LU7}fJf!^m'
'F(`|*=a7f0M=sE0Kr&0WK3v}qbJ9>=PNZ!-Q-90<Tsi4M0TN&IdXHtR@B6-'
'jxssYYJlZt3tFAW{AY)X|`JSFMXujpCvtmMx4ObPW6&q7+#!GgTSz?qNJq|c}2t7}><2?Zuy5y(kGC_SS?Vj2j?P+{i`$LmKh>A!'
'ou2J}$d{FdP@?R7daYjp4zon5B(GfFQ|@>EiV6_%3wGL!JLtbv~fSqFiZLn<?}Q%rrwh=n+e0#qRUxIE9myqP!dj%_kktU@wCF&p'
'=vr^cCpN0>Qx9DmI&BIRGp&Zk)bp|umX2DDGxDOtD{`WtD?;j{t)lUGkd)h)1kTjF@DQks9YPja5ZRH9TmWEGX^YLczAyeR<9C9&'
')*r2~?(_-(B~3+p*Dk;VkD5urG;=lJ+TQFl_Evh9n2ZjFW=JlP<Q_IsE2f!6I(Y$-v^eFmFr5onr5chK>(JRq-'
'^Z8x87(U8p${^lof^dSHhlq}Nl<ufwzyYqUDjD_``+4AkJJ}u29!(3v{xkTIHFl$!Q5pd#SofeRJS9O(Ix|xuL+!7ess&JZ7Z|{<'
'+pneFjyw8|r<O0fGh5~sHo#cA|KW;ccwPInv{3ecC<D)mBYp|;oe)^EQQu=ZY!@F;X95!Q!Q#eAv=PlqM2K!HWk|Vo1k^-'
'd;%WS^=e>86%p7y*MNCjQvHISN?M!?_Ne64IcyD0Gb5YktKY10V(O7%D>VtiC^p8p6N8tb%TWRMt))VB%opY6>@;4w(_w)JKCyn>'
'`0-5H=2&pSOeHKKjW9;coC7n`7v+epOY9=;T~)5CcMGeAwex+$SOoXH>Sa}-I%!l8TtF8-'
'R$xDe2P^;n1NLMkr9Z$dt)b))7a(5c7H{B5oq2jesALXUD__76m8CfFU6c;s1`(H`944|`t!%MA~L1jSrg66J#hbFHP|3vAmZ%LC'
'e>3wI~W{|XD~Nl!lAR8vMuDv;3pw}GR;u00Gq;h6$_ILi<4Zm>rKsd{BpD4s$YWn9OY%q-zsR7)byG<3Y--T$ENHY9kt`tU7o<KJ'
'9@Ey999=^eQbVnUiGkSj?n#sfob3t}e7=w*1uTk$IJn{ybL!ySrgN)O)({h!0AgIxkT^=&eMkTLtag9HsYIo5c}yHbMaIjby2xvU'
'YUP!0L&1ZwcDuh3BTUwF#RcV3S7^db+5w$4&q)Ak78fEf~!pN!kYau%oD19$R#Xah$7Y(MfObhUx5KeVt0p5C{~(Z`9VCfKAF6|0'
'jK#1NPo=h&(Lpxg<n^vms4>t*m;ztuz7;#Vz?!Ejho{^xnwEH{YYrG;Cl(rN1$>7|x5^McwfgRkfvi?UwlQ-JFKhGaAJgE)3S>M&'
'!P-?)uJb^&4n=JT66<r#rWZZaG~c4}fnFc1j~8FUpN{$D`s&pJpxKi8xFkIho#YSxDh;sz8uHSF|%XfUD*TYh|h&-oQ)35uwdN-'
'9Sj4gqOL3Zt^{3)AaCer;tleDSai07Lw>)BIIhE4ADwr`KL66d>_FVv{91n2l)w?2Xf>?M5h6(&4d><)hVJQRwZU0z>-'
'odBX{;tHm;h_0qN}oyR8DIGYLM%e~=G1L9M4robU>T!u&xxm&Pc@6~Cf8`iz=kV)ul(%YDElwGsEnPAhvrul|Ok^Zy29-'
'x*BT${@i&a<WDRn4cNdp?s7j&|<ezuv39glitY#LI0M_0zv%Un9NSMEoAWCQ0lJfPK@%#=8^3Td4hH7;KoVBV$Uf$E>gmgWgr(W@'
'Tfi3rkr*M0-'
'6RCVPP?d*zZI!uRE}38PgXeB_9Loec^CftRhV{v((lQ+A^b2!Mi9`X`lQz)$RkYswcsEC;lZMpX0Pqxn8yTrtxr2ET1Elj5xz{`2'
'GhW0hPZqxIcrkwhCCG}^PhoOQ&fA_hASkgZ-TRBfd&_q`BpRnNlycggo8Jt}V7{TC^>quoNXY5_#M*S8Lf7odtk#=9QrrR^CMmqr'
'Eg6v<16S9}VC(w*LimST>2B;L*swV6E6I4UURPwU5F$r{(SNVBbzJq00IDtiRfp%T)9()wrfgIJ(dLH1rY0>}PlX5G46r9s`ZILg'
'U*0bd3?5+mV&1WEoTc}#^?0=0+&Zz_L81rG>?CmI4MJg{fr$}bJ7;y{dgV82S02LsbX<|&_vjWZbluSiNy2eE=FJ{d0YY!k@;CLu'
'xC+I;}YT9GU;X}zs$i&ja!*4gFP<$(W;r<X10Bvyc!@vfOaSP8&Ae*N7;iBQ})sU7PQXs%Y)8~1CD7RWR{*aQC>6|O&&NnoNf|Ek'
'q|f^B;7Cq6Q$Vg59ogl-E}mH%m|YE5-'
'N|8cUOEXbe78&x`(maHX>^Vocu3bVYCikAE!Kb3eZaeppeJ++&!Cuzy+xBEF0CTku6SnTZu^aQe)btdSW$s|VncwTSPk=seLcwxh'
'qDrYcB`@Hw^z<PrTVxOO`+YK?Lq2C@qeIe^W!B$P;4Mkq<vnn*tpeJqYV4>U19?h*v$J21z*xi6fE?%UygjT&kv*c&<H$UwqF8Bi'
'uaru_<b0!1&r!D3^l?uHs4pArngpczPfY<Dl2V;9{2i`;ts7D9~F2bMP&#H_jvwE#p7^ka?BUkmPr+Z>mN8WKvo1Dn@sDeFV)CT_'
'0mR+1v<SI6Ls|e=UVB6lzNX8sD+Pqe?+EAJkglbZSyq`V(bUm0}XJswdQ<gMf#w=vv|8p+8nwKL5>KPDg=@SORxT<XaQE6Z8`>^<'
'64&15$9Aj@xdpJ9R)tPEDKr-Q}yb1sDwSkSeAG7tB%-'
'XmKZBOXji@)3?m&2?;r56)whg3K!wI5(BiskN?jTgsZ{lYrCc5r<+^T(HkrrJLQAkOD=zDY<V+jyUF;-'
'JyJgQ!#EVoeT3IA8>Nc~g*qM<v&!puy~22U5UhP9?@S{QOl?hcunTi-9giy2$>r;w&qRj$pOhExF~pZ0Ad>^+}AIfom1dY*hx-qW'
'vOfq$aluFolIr$2w_+5!IuBjpT>?9?Mg>hr_{1GT9inME|yaJ3b0?3v8|M@<;GkEv772e-'
'wS2S;=UHD*M}~a7ST^*`qbbpk^hh%%JX|?33P2g&lA)O^QD=u?K_|xD~ATtl@%yuHQ@;?p^vo#>lZT1COf}$XKjQ-'
'~x@M2q7N%P=-~e=(?5}5dYKrNdzXil4ahER$ikfINaU5s~-1e_fPtyqFi;;{fvHud3o-'
'ysSf4wHAKDF5B~QAen(^sGfsPNz|0(irM=}M8Jx=zgRh!o4J*Y!^Ab-qW4zk}3Cly&PxXJ?$J%cun`vgGjerECuysViACV(Bw^g}'
'jJsDb9iz_R&Q!xt^OR5E^DMpQ{9|^M3Byp#vXJ1oK8*<O4`&N-HitPmmV{pNk7$+{qm46`3Q?^9^IFAg3cPx-'
'F)2ZItGV|^PYpGLtpb#vq*PBQ0EILrE*`}k^2DF4@6cbV@{2M}+GhjV0F@seK@+&g^DQfIQz1&l5(!CS$Gc{MpF=cDQ`0YpMgB<K'
'Rk1j%n($*yxNJ`JYxUkEDTP?qtHN)Zdx)G@;TpDY2l`e$#Tn&tz1OIxXZKwB}Rz{>`i>FgKqg;e|vCL0RBJFC}s~GLY4tbl)<quo'
'>-rH97^|R2g$v)LP+NJ`<BYqGgA)Cx$NX19;neZLBb!-'
'_lJd1Pq3Y6YP)l0ez6k|!3M0Aac69zpoSgxJ$1H6Ui7r}l&7LSqtXek%NpOr&|g2_ouENJ)I2VmGAr1vh_gGPBQB>&LB{A>o{NoN'
'tD5iyQ>**51`_Qhq#wZkcuSSm}W11n7Mr7gqCA3Fjg^RlOMRhMso%o41|>Eut;8suV5VR%5i6)Ykf`DK;&lp_TmIKe?Cgs47N&Vr'
'z$&_m~26=F{M@#LBMqgIfV&yXDjWKNm~SdI56eX$TS`27kTcJkIisUJ%5cuPNpISTh0;!K0-'
'r0FyN+yuaC1gx?54#5C$PH^P~fmZ`TzabrWuTpss4M=OB$XvV?P`uWf$1wZ(+D7EZIH&ExB6h69$+-'
')xo@NZ#l8h1t*3#Kya!^HY?UWH<eSps1Vso6%HYtL!7Z8q4g>e8Ih~r46=BWs;5bDb{64kjs6|`_aR=wtlA;mSIUPR?)e33Iqg#m'
'<Eg2SE{r5TN&S#>dyT<uTa2|xhjA{jK=mb>XAikz2ev5Q_1=&d@#Ki422c^bsEboA0FZsIh@(`=fiu~f>(VdlOf;6F8jlcHSl95#'
'th^7=pObK9wC@fSjjeOC+pc*Q=ZC;y?Hz1GY&j~yFxUT^Y*G>>dF-@eOU6+6D&hI_TQEz#-'
'PG1}v*w=5Z)kMHB29WYYq+N$(Me%J?+Y`AkjrQ@2nH*|g))mz$CoSJ(>Y-'
'o1XoY#@XrS3Dyl((A0fGRFxE8>=^fYX6%+e3*QN%#yBFKfu(z#r|k33TZqsa9t(=?^W;So8!34c`4-'
'X;zlYbYDa1giw55W+bJNrisy^D$O2Ge?riFKn=bQ)u+<B0#-'
'xmCVcX<Fl|KZ<Drzi5Yvqg>dS?+om68<r^0v>)uPeceS{64y5hgxC8x`+*XY&^`GRH1(F8`+alM3eiO=*H2l@+9^w3r1ISSV=ZiF'
'd(kr$W85(&M;vg~*bq;}@Buw`A<H^3_r0t;)&xq{hmHfpM-W<2kqvUY3}Wj8s~p|sf;_Ku#VKZq}nvq`k-'
'FUnW!BApQGITzB$Q>Kd{Kvx@!z-'
'48k&F!;)txKymlp@7<>L$qXzYG0X>+Q4Ij9*a}tyTlNYQ&h=AFlzWm_R%d6!^W%!k?0PbUBuoaYw&`zTx^}j_m>uqQKMz+f5vH>_'
'E`z{vq`SEabqJF~l9LcX#(|4mvsK7{HgUoWUg?H(wO)SO?xSBho4UNv`965eidB(Ui`Fs6EWFqUnIB8nVwA7SUf1B5uCyTdKWYD9'
'2Q%5Xv*D^IWRVB0lT<{8sz;O@y?E!p@tc{*bK>0x5((GS5>cv&REq-AJcPm*pJl+Uix^r<d6q8ACyhkEZsM>#Yj0_|&y%L7+cF^T'
'r<c)vM$L_QR2T0;fp`<5Q?nVT$c@CzuUS%a?Lh>*8t9czM=jKNyBXdCzk$NU*tyU>e>Y?dgy$mvjlSqvU%YHD*RXCUuaP&zimsA{'
'3OtzP1eFGKG2G&B1lL*Us|_a_>6{KcJJ^=|9<gRDodE$4R)uL@oFt<yiRmYwp2?TdZ)FtXBCmkdb#vvB14j0qrD)?5%N-VQ-'
'L94id$kxs1VRJZDS6aHqOjch0AGvjCp337}j%-~@-PU`W{<S{#Ws9PRzfLTd%f&cxFXW8_I@Dqq4TVXveWQK`+BY&waZfH7BlKb-'
'{;>vdoDBELQ`%H?#S%I1dQU_8&#3_);^9S94mtX&AN`fT?wZ0tK>k17$gV_D1>`jv7!liHey*AS{wJRWCdL$Z-'
'&V&au?F5PW4yr}+AC`WfM<;=q7%9@M2hqUi9A><ojRg$!AAyn$SP{2g<?1N3w2gEG*g)^<lLIz0NibJXWW8NaF#1wtLe#UD>yQoi'
'Go$612*qfyMJpRTBMi|~2buHDjtep`*OfhaF<FA|cW#Q4e!YpYkF%AuK)*U)`EUq6^Y-'
'ccewp^{vXr#a~@W^PFXc0V+aY<{5yb*`BbWORbwvKNfaEG(|A)%;d<JvOeS)zoDxv7c^UNG$C;<z!!K&It)_l@?aLl%XS&p$uw8#'
'}}~96Y#UPX{H`%?T5TLmDtGo$Q&><Ov$!vF@@VM*=y7XL#<KH(qwk>>BhCXCUsEC$%m}%ke>&3_qJCEMxN1x#V60QYft1+NU-'
'd0==gOCZcF6jPFuUzll#+PyN---?c^?5$civQH@Ro@3Ui|+&mEb^5T-'
'9&}jW#TJ+|S7@vc^#voxLHS#p8?|bn&=vVS<{`Syud*n(yvQvy71qAGv)dKQ(9Scr1PWm8s_c;<S#b(LErN2}r=rtWq7^*MppLhp'
'ND8aKLwwWwfx`$mx1iSM2FM#bZR#>0f03;N-k3jgH*J`yvn}Ovt$v9sCu!PayH;r8yO_{84@OuNngblzVH|9i;X#mf0$-'
'IZ{Z?~iS#Rrp6h+)DI8r{SerCVFQ^;|M>np94+jY)m9m6%m2%$W6H){H-'
'svCYKjEZhjrZe#|3c{Ps~Q*A7oN=0B3+yC0~Pk1Pn=WsoITsu5@I&spFf`_*V&|3?e!YEpz5M2!Q9FyKVL8(eQp%7wfg8!`WH$d('
'ADe$;+sVP?5TQ}J)N^3?+bIQKEBIpX4mdJpgCQH<SwDDmC%h6B_@q)a+K*5GsqHu~X7Wf#60D!Y>z~f4z6%^NclIkWhP-Uh?Ba|M'
'nU^A5u%)ii&W!ZOy86C&ROBEH7@z)v~ipYI;a(Ea(fZ%8Bj>AH&dNnn%?^hX%Uyb(qTiKAoT@&F^v?`)GkHgo&DDbBLoJiEz1pmN'
'3QrwaUfpR*M$VlzaM?I%><falDJ;+=!^Qa)E5*cF+H&rKJ7MSrB=L<gr?+|3`XV}K~U0#ljU6z4!)>6cLJbZqS=yE>v7&ivEjEi+'
'o`oiNu9-zHGcjfH)HjyP?1;6V%SXb{=f9Ir!GoZ8<)i}co3=)!KahW*A?MKz?i|S^IzbDN#822Z6;?R-'
'QL*Rb3AOtc1E9q)qov}5-UkP&K-OP>rY=Z*-^2<gR8$=9<YN-po@?KM-Ds#c^AmgSDo@+b#ihaMP0!8hBk3PuXhFSiJmpLsW0ONe'
'7TaUZhF+A6HKjyDJ_<Xn=9hp#NV>X{}`lsc1Dc_)B$mA$^zI=0z_`oLIF)}ITh53XcX(;zD+aw_$<uyq}7))(ETOA$wBcGx5@>v<'
'PHac*{ZW8_zLW{E*o#9dhoFHz$$cr3g*IxWtQGlD7aK$}2p3RLk{MmZ0ts2EK_-R_7WsJ&~i=~+9)cvn`$!NBN^M#AUE_U^EOTVk'
'ef4h31>alRQT=C{UfdxI=xwQVA1HV5%t~$Z$#V0~v{<o3s{twfX$2;cFg80Nd4XsL7M?u(O0nP4=U(L`X0xA%m6t>?Fz%B4Rt}Gp'
'_xw4fx+5tnm&nKVF2|&SpzX*ny^x`b5DFAaA<YgiQE-'
'$tjL~>yB?CdMbn|F^mp9za?4JDVc%F_XSw|@f$893d#{|N7J49>L8V(zO-dB7p(G-'
'1GUsfsKUV&;KYLZJW%8O&F&yt&RE<%zF9bFO0|ji4PUmw|h7Kr^%cZ@E!k)SzaN1(if#(JzYj&_7;VccR?c1XYT2w;Y4kU{`KE#E'
'rHD>Pj0=i(Jpz&t{6rZWs69I`lDpFbd1;K)dIdo}=ll(nvROm6T@~=~6)UJTdyhUpT*uT*9lt4<vA3s5@s`?>gP7mxcjWMky-'
'T9;<jT{Rkd7{Ccy>yS1HdEZ{4ophq5ttXV2f^&{S#ouA!@<5TmwI(A9m)T!bR?-'
'Z2dzHetF9Y8Yi9nFcbB24DW2$Ti#^F*MV0Dg$7g~IlCcHMjgYA&w~z~&M<sJ}JFHskS@&d-'
'+FBHi3FqnY@y(empn{CxRSSZ~GkRDZ#1n4*0ly6e5b=RMI`6B<^(Wxl0E`Zxyy1w$lKR=XqNNgsdnC5D4YMDj+vr;xcJ!&02m)N?'
'T$m30EufcpwB1(p8;<9eEn{+3?}>|QKe`Y_UBIA*r0(kJ>2)+_BcpN42YghI&_2;SzLN=xqmZ#LhKR(D_s?hjQ=E4NHFt5L`}G$@'
'PG?}6ab2r%iVjo#a_XR?b!?0x<6Gm(W3h}P<lnMg57n#888w2G8UYzmT&YM{hJAss}grac5ZJp|MxWlDn*f|TRayc#BUzzd>cZQo'
'#^Bru^uvffLz=i|dR=)212=*5lNijMHpvKumC6ya@44U9FU5*lAWr0eBYg@N1bPu1=R+9`d}v#aVglSzQ<&?jY42ynjs1XXu)vpO'
'=tlg<B@7*QgkL9yubL%MYiM=Bb2QyJP!-'
'@=zycQ}H_F*kmRHAJ|GAC7}>G{B|54C#R_wSBxiZ9W{v$y3J$>MnAH<dzaN2K&jd`i5xA)=kfX1}&sSksS6D_<<<g22{0!wR4P)q'
'<fVxQ)=09b#17Rw<XgTTc2$}BgM>K2Tr`=w2AH%o1aZwG}Vtc{SVj%Rd<%eVqpLIUZW<{zl~_tP|VCHMnPf`G3nDBwuco>+^TnVQ'
'5!2$Q}u0gSu%H@`RUcIr5C8SrOGzTY|*!h9}O*2-6yY9@kyCK8CWX)rX>8M-7Y-'
'h7ZB@>afiCNAyt14Sdf7l4iQLJzS=v{7ZJPGu-8<j0^+w(t+a6a!fEM6NA#SkONU8koSwu4YbNEJ@Qr31a=q4Vt4uIM{<sc-'
'o3S|$jkz2ZVxtX)y4%`L!k;!65lp7|^N>1Np?IxOyX3L!jnP*_NV-'
'p7EIVLq!*sH}TT^qpihZ|08mdJrp%J0%FLoG)yj5@R1@X&r1BSf%;a6n=gs_a*;O>S`b{rS%8gZmAA)<%vBufwAUWXe#&vSHKHD9'
';u19ipp6_)~rbGJ5B=fk~_H6`c5cT@fDI@Fo~W&IMP_#4ibS8HI0g$41)*-'
'pr^9A~q`ax`goVEUmu8fASCClwroGwkJrrlyVd<mbKZ<#jo``zAjUtr@axDmLY}@j_5KA!{G0O>hRP#9xKyZH9_Nu(*-'
'gQW6EK_0|;JbLFh_j72z@umDHl`#1Mx4R6ow24jl0gA53fu7T@P2RPX$RDp*=&RCk%uMN@L$BUrO+#tO=&%B&Gw&IUkcUaFvohzc'
'K6nJs+WVqAQ>i}3`KFOu{IpZ1wwM8MIUoxfEm7JZ5AkxLfID^zDt!q{+qd+(Ueh7!Pl1IgA01z~hf>OvACF#;nFVJdSOWVY7^>p8'
'8N%AU@k4sS=5;>sEJx@RWx1K0<-(xXYg)xpiasVj1BU8rGfA~g$JSS$r<s-'
'JP{xY>^%<OU*Wr;tytW5&eicyYUDp8$h36&qWbOLCpR$nYLl*ROK>367=?bNg?yz<#R@Z%jIwt4(|@cWp^oF{$jppuHpF0gvYnc>'
'doj=}~FZ)WY58yYd%WLu)Eeh<f!Iy%>;*DZvQ9ns<+u0NtAVKuQEQ%)gmUBRfYvfkQ&;O78ndE9S-'
'$q`zklU7*yGU%kktC|PjUrXwWrJDU6>%(2kz0}pgbW5~hLIpWEO-'
';pAe^qBoJ^6kgBhPk>62F6MW{)}N{%v%K#OIOF&^kJ38MqJ*i>d-'
'A&#C$33oU<Zwl)Cmf!n4{ibz^oDQ(mz{nf90pKN2q0CY%F(M;MqF<=FV%Gq~M|B{7-(lgj4!hhZK<)`2_<2qj4QvB-~gps0eHQ-'
')?8X-)*Nq2|#HX0{S3jZkxb`nfn4X%&>G(<<NTLC_H?4+zae?P~@O3@DNF;Y3Vg9>mjn(2`nS0`L67F<{d(f#9{s03A|KS=O?rJ-'
'p&fwnfSUMfO3&#J0Rk-%79=wrl5iSGJk4U8Lnc0j2FA)|0c{m#X}8O}iU<Ms1hdo>p;@!d&(MKQm`7Q;&TPo&Z{TgJ|q9jET=-'
'Qr`Qt-AA^Y5gd7f`YTUrs<fr+r;?qy8fS4T<OjevU!5cu$|E}VYa%uyCts00I^1M3`ox<^O-'
'^abt)XSg4cI_G_&OhL2mwxj@Hx9?_O>&%s{AiFbBX?kf;@dHdz`Rr;37ioajor?!#v560a0K<G&jukC`RY!V#D4hHN0z=0FnCu$`'
'@!^iijg98~1kk|-kc*pG#G((|R$=jB)tEbi<DgWR0Nw9XA-'
'2<dugF1%5eL98w<;O*pR9>6ICJ8<88Wy{_{$B4*^k0jg%aUI6c?T|+8l%TEjHfJcOCLG`ci8!3#ZKL%dWaF%DG;SgYEd8>R1eC^t'
'L)GD&Ka*7{9adArt9QvNX|o}4Sn_AD?l)`JY0y#o)uxdobVDTo;GbD*ZcE^gvd7J7#7I3~pP0Cnr21i1?|Js(2EZvQkX2Bc#AN)x'
'0T@gOY|I_6>j@v$nHFYJgT%&5Qp+o2t0zzx&ROct*7yl4Icp(Rai1)+v51V?-'
'Tmws)rBw36=?{PC=mJ`$1|!%wnd|?K?Y`JrzBO^S2N}AN<luAj7{3mPQtdVtNL3=uY_xiVE|s2dsV60KjI5jW`?R|_b%t@Qj$+er'
'fM?y#2D*%R`B*R7_>(UFg)&n|1y)FM?afqo8`dQOg2~OSevzN<JI$pAYGGMfwEi6=$;rYIvy1Zj(Si8A+GJuwnpgq1D^Ov_7y!Lo'
'=6Se=z0@U6wqlU;!34Pp(E{XaHkUg`b`2??rNP7#}B_BcJf1IhQhjrn&>bfM3$DPEn*H^Ova;<9u08srMss(WVsgdSp_}L?a7lab'
'7)MA2O2`vWo`=n@6Nn%xRICrdXvE`%t~vw)q0Pu-'
'~Mb!2m%ZC6%u~OMh+Wjw}SJ}Bk9Siv4<Ju<#hkKPSw?|W_AImwy^*^<uB2o`avC(51@nQN~|9#vi|v`e8lf!E!xJZb0q@{n0%$oI'
'x;ORIV(G>%pxq#)g*)6{_I_mP9oGg?m5PzWJ}=A8KU}p(F&B$2GAsU<yU&^&?_Fv#g}(SC$aHn&%mb1lkI+`@fS<S#y{#g9*$YH+'
'Dp=^Plce|lZxlBRXHt6@tN)AhavpbLAyW)xHE|5J31IDaYi_x>1g<AL`8X0J;)BGgI4FMZ?6vF75m91+=s^knz6-'
'nlQpSK4?>2$1zCv`lP-'
'*Kk)yEwC|R!YOY_$5NN1~Utbd5gD>!Hd*(2K?hf#vc8@NTr)4^zg%J>u3IFFMOuGP0#x;x(+y`^eWsHA)vQ3UV8p1;2ea6dDa@v0'
'pQ<8UjaNJ0wsG^i!MZiBnwP!#4|9p`Mbn3ZYJ^&2V{M2Q8mcGl}arHTJrN#h671IZk$%5))s^zZ|@{imX}EJ@rm*(3K-'
'X8(BIeB`Yo<oH3}C^LX);?H!XH=>yByqS^>>*X7gnqPo3ewSmV=(3lMekdmy|0&}ryZ=CL{%)1LZx@-'
'91}^J%#!5ufvElfBWgN@Ibx>3p$-'
'#UZStV+B9YJEZ%@V(JgCcqwXW4(>6UY7hfh0vfZQWuq8YBPv<1QzEG7yu2M>r3hqzsGmuNF;e$>!e2A-y&9-m-'
'RY=M*pOLVUx;!QYapJm4)c6E1=b|NjKaDehW)BdP>_baFLwaCji);}j{=hY$gR(ty?K|Bc&Iuw}?tLNYX$K_<(JRAShxfsb83++X'
'}@=G`oeWv{8I1%&xwC~)FCWqMRa@n2%qQ)q<a$)8ALx!$n!TZIcJy4qmOlXZ>%j<$n_KS7TAPSL9@V9>Qc=|n5oOoTirKA<{!q9D'
'Rw?%<62%T<dHPEjr;0{r@+R^h?9;0r-cr@sC701YZWVDBQH=jNWrr-!UXI|LpnC-'
'x}Byt>n6(?h!rDV5F>u(DQG6<)3&%aPCnPGjuv(fZrmSemGI3<}hv%#=!S;+4O#*d1<v-'
'M8g*l&?n@B{)Exs+3w(KU^v%j<=WdLQ@#2h>q%_IM(VxK&{oZUc@Ut$Oe^%OT-~XR}!A1^e`+4tBPR-'
'G;V8!pCk>NH&<SQ7*3zvW@wb5<E#l#rF6us%d1BMZvLWp`dm#lR1L(4l{}(JG#>IQ0V*R#qkieDzjVZV{B(8n0GaQfo+tM0F`0R{'
'GU=o)*nau?>1sob1irZfOhf#$$a@!-85|z_^Nx;vDEY``9S&+>VLt1PQFK-$L%-6=4(7$+xYOx2i@-'
'fC)zN_8lWvW6G<|yw?!{Qy?F~6bbJ~7zTR=I5faiw(o&`+zU5a7+0_l!N7_N0Go#F16*cv0#_YW}u7$AXH$t2>CPZw{;WV>JU)<*'
'Cd8}$r+4Et(Xq2sW<p%}+oz4P<c(kG&-UZ%G$1K1@`-'
'UN$^+sDp1^x+fHo*dWQ{jwf@hH1OqR=Q$Chdf|fN={i6FL(z&oe^98N2gs74P5m$#Sfprpj^=<6hQ*KG!-%LZMZ%{-'
'Il+9Prn?&+p*PhGWWD<1mlC8T!il^u+jZ}8y-Mu_RGBTU0vjaNG;f=kaT-BompW9c9Q&>X$WZ0x5|<X4TvC7{>6BE)(yO&ua?b$`'
'N=(uUsbvN(3d1NDZ?|PabYdH2^fx};w6l3U*%zh8LV5C>o9Uj7EPuX?f|bt{a!7mFu}>x^1UaVPl>`7?k^Z}ItPc2;(>+YEzN*qx'
'ssI8v`OjjQKnBMgPnfZvB8Ho){n4ax};9?h8gs6lThFcc8>J;;kOcRbkp;K^z<?BmhOtXR}-'
'6j1J|=tt$WGAiv|eTevytehe?Ug6PJV4>*InP(<9@K=ZjS9U$P0fqgwXAAGslMmcdpN^Q;o$rK|dlKx4}(Jm1S<EE|#K_(1GyvnA'
'(~)J?-xoYSu45Yd-hRtDsbfWG*N<yI+Gd>?dTJ9S_!&OM$gEb69`rMqf-'
'4<hvY`I)!tNqfvJW~NiZOn?{7qRZL*{kJctc}Yp!v(cql>iFp_P+rqO1W2UGEMrXYYGcs*9TN?|nzz5$)gAA}Pdb3??TDL*)wklY'
'PzWjkrp2F^$V#<LCT*dy+&kRDh+~&a_nbx*^U8{oW-K>L5kSBd5>htxtH)=o8}NL@<KCd&mH9J<2~f3N5CMh_F*{JAuPkeQp9-'
'v*zBczzK~C#qW+=2O<N1;UjH)n)-d22Vw3O|ikcOUxzXPg(VQIUK`=jqdix?rH33CKE1#~raWn;VfxaV7o-'
'xlS?>h1$2GeZg85_Ew?YZrn3J({o#09{Ekh3&633SJ))&lAz@kZ3=bSHiUK#mh-'
'8KGTlFkIApxYWUC?7lvq(XB$Gv5Ni1D5l~Q5CqRx$q<cHSpTzmfJE=Dba`)3HIeBmn94L4+PISZ$#{ow=rcXx=mKd>(ydBfTaw$X'
'<3<(@zot+9a5+ZOt`<pe|{so$R8Qw`~KhibIZ_G){AHR~{ISq5Y9JmIhqy#F3B<Wmu@kHy2!R1S`c%>jV&8lTbF<e_!<A8~^LzOf'
'C4w-g(->HA3)mLy1fB6kU<x#M8#fyp8n(*_Fj=yJ8vQ-wlmuu^NP?U;~<p5o^ftGVz$nvjQNgQ=**df{BD>s4DqD8JCLK!ud1TPi'
'Sm>3<|`0TM=Faq_cl!8EYmDk2A89hiNd=^$@%C;e_F(FPOVYMJ5>S_KL-4HE*+Mv!Gge{vKanOqY-'
'3V0Cc<FmQ@d1AkDo*Z7I{gnX>BKuC11VmaplZ+3&N+o7-'
'a<MuMmhSC=6Ax+!_xA@V%GlSY0naZT13WT56NM1PuFS0N<D>PbYFwZt{GRDC?ew>9AXwek@<2QTT4Hb)CXh8YR}U2+l>xo%8j(~u'
'EEm%(okzmf838bpXYP4l3y;Qo>C4BGzqBQOTYgHjHmX~@w_6n2+y!0RZmr-'
'8<x`uX=~DgVNXMnTeS6bB9c8aLgbNLPenSSJG}jy({0S9fGb`tM~HTJM(n=1>!_m^4|Rgkbm8Ym{y-'
'*;n!Fs<E2sC9V<nLWp5faz=k-d0EFIJ8KyH|<Lw-'
'xuz1`@FhYQCxHCyD|sFyM0UBqs>PYTLlmZO1KO~zWCi4vqfu5Vl?F#xV($ypD*E=61Da?`AO8`JE?(ZD-LkWqc<;wzd`z`yXuuQ&'
'zms%aYgZ;yB8J=`InW{-gaEJ!N<crQ1?e5vt|{*lWm4OsJ{ngCgbSh~wLrs)q-T}Y|h6J6+x%-'
'#k#kZEq?^o?xcfn)c}1YW_`j3=@gY^AX3FD1;?;-^AViS%#Gf}o>LsWE6%^{Wj*Mq|%G(?b2Zi#Q*<3Lc;dAP+-Z`_f@Hy-'
'{;5#~<}O=6Yf5Di4N+&51A*kc7x@Pxv%sC7P`lDuci-WbLUgibBtZ)RM0hvv^TNh~r{5>n};Z4AZIJ`MB63o*ZaEn%=03UbF(V=f'
'xAn-4J@oPL@94Uvt}8a4E(){9<GPwXlaG(L_1&UaN!i)rOajWG&!J(xU9ztNym0ZlHn7Q6{f5a_-qUU9ik$ioQ5jM)~2FK%n(OTx'
'#H&ok!b?F=9DN679}Zk`RXKs(@m$5VM2_!VqQoy4h9zvFOf0(hRp-'
'w+fcgWff)5O`7}1=DAy$P}ZJQ52<;=v!nw2k;1^a&J!(~ASX3iKDoA_isT0FKu$+U?gdF+$~Q}ty*MTRdZM&5Vx~<Q(Btv0P>(+W'
'ETDe@|08TsfR(I3hXKnStPJZl!=gV=(rG59rq9*!NVgdh5bV1wShK`vD#R(F#mheffMjGz`z3JvrsJCReAK?A_iBSdzwukKJt5p#'
'XFE8Y1rI_76tyFhypB8dWF6z;ZpJz5wZ^vx`GV8IJDghovZW6!`v*&4@$ql22qsP#3)()Tzmz)ahg^y5CE?F0U=x+el{{fd!@0hW'
'qxp(%st5zM)d#S|SDYdv#m;+KcPR#6pD4AcKmEz=D-dLbe|iG^#CeYrMf&}#Z*{)i-'
'ZQEFLW0NaL}>ht4LV7~gHnK$N`+K^<^qFoLgf;jcEys*?$Hwb!)VE5>-'
'9miP{P7Jqh(`n%Wj6h7HGXI3)q|chUj;u1oeOub9#amNVNTwkhJJm$Yphc1;t@^p3zKKDG}A2rH9k5THbu)j6sYr2O6to>mVy83('
'?I@ovQE<2a3}R*{eZ~ghCDi)=>(!4$$#|ZosTeKG8ZLgVi*P^`Ob>1p5pY>ddga1@Q)Gos)-{TFVBRl>wxX5--~k@-'
'cU@?+zEg*t*Lir?j~-'
'kqo$P=zU@5G4RIy#$moM5Vx3B&UlvI4|sZJ)A<LndHthSXKlX7<SsTc%*Qj@BQ7O5%6GXw)ekd?*@m~zo*?1^1|u+_Pu)OH_{!?|'
'Zb9#Q75IwATjtfC$1i5$8~SkGo*1PO$ou<u8@x%wZMlgabN4#y_X`|SY^2fJyt>S<Ns@S-'
'b7<qB6Qo*XFJARz%pvYS*q)2EDUZ;j2Ei=;uZ#PFJj=`G&z+CzIp@(yx!L9mnI9ZWw0HNdfpIvyk1P0ys<ifYC7I5az2f(&za*47'
'M}7HeHQhEe)7!J=aV^;gLI_62O-'
'Pb8sUKpf$}pQzkF{FmS#ydBs{d)ZF&^w{4%7}!+Tc|hOEMC<xja0Gh^ryCbT<v*bo=hEo3fkA17?Kff@hB`74QxXZgRGsH9_S4(T'
'9p<VU&*yF^7jRGR?e41gm6y&FJc5iTJivsYi#@LU%3EPOwpdpgI1>a{Fl5+ote%%kDq!eg0S)aVYnKEoIt09Xq^cgARlF{J&3=in'
'axfRK7WMM>m^E)kK3RRy3`JdmfxN@ZrqJ0#`gLc^b48BDw|6H#~Lw7!|3n1$9Fr9DZgQ3m|5>B(!mC@JwJ$Jz)#xUqq{EF3+=ixB'
'|GFz9G(!)Y|F3Px#YpLX5y!EZ0zWnXfsycG@8<#99oU{FFui0Pn^RXQc<y3{|#O&?H+^LhGW++i<aS{m=~bh6RAsYYkQDh~L2^>s'
'&96AAM5l2YpbBVmX01R~f+C@^>E6%)K-'
'A8nEGJ5Q2`x1{Bbh>NjGyIvz#0M0~dxXIB9XITZb+7!05|%)xgcZY0lde&TP+OwGpeCCS-wXy=JDDL%3)<CZrF3@bj^p<dwL5*hJ'
'R4hj~IkI|m6H*UU66%vsr^zE_S=KnIK;QT!qU_>vTU5bId#3Kfk*=ahY1;mS$Hp34qxql?(tsPjPx7yXr^MV4Z*hY|#h`wBb7`Rf'
'{S;^jHknt$^+dHuX|7p#bvS$S>h2oR*jTW(D@@Qh=H!$iqF6rag1dTC=6ikZ$^7C&dW2R9NB0|`%2)*qSQxc2-'
'$_bI;)rd7^?O$#g0>KUpZPhzldS=`8rcVq+cu`5){QGl!9)qGG^gH4tMN(U;{)KNo3%2qztf{sZ17kL%=Wtej*tNjkrL);jVS+a$'
'{<en_mjA?jO+wdWYTSl1Zzu6A{uI1}<P;-'
'Pe9K>QK$LWP{+eWrP&)U`+?)~|3}`~TL>J`|2!FV&%?8cZ64>ll;1a~9SF1dMrLq0(%4&O77oBfAF!wWnEXpkyvqkM_i5=Mv(G~u'
'VZML~m4VY>_CSlcsa)95scs%5jV)_iy&i%(2q3F<5`#Xx{0@o|`<tYL_EijcWb>d5l6n#%<poffbe!zF1yJc`I7tnVXd2ze1`cJs'
'6%qo8tE#cqU2z#|EC$ktSli&{CI=C`}btk<=CGX5@%363nwrb7(quM{*=R$t5RA*pUV7n?^QJUVuD?&F<h?g$)#n0~@+WZjwWQ;>'
'`9TY~%tnPI9(@7e2U@9l!nP|>Q#zxd`Mt4vrH?mtbh;I%>&V&X=X%41bcOTK=&+u+>G<KXool}mC>}(Mbi4Ng?1-'
';EZ?>jX49_17&ccx`N9Y=IoKlU65^&)Tis3?pu?c1h_(G`>*x{=Y;ok6Qo*82$p!gf&*sx&H<38s-'
'8{Ou3pPf@^h<X)h2Pop;d!3qm5<fK|*PxZp(b+mXqfE<%)J}5!^l>&fnSy@!|7CJ6p|Kz$x4%3q;xB^<<pvK{I`KoJyAnA|ot4x9'
'w2rQ=y^e!W@i7Bria7`)G1FPN@p8(Uu1@|6TiEs;aHrcF-'
'(Gk*RNpM#DfuA^|EYmTtndN}oG>1$9k}~kk0;vGF>3eUY5AZ_TFysA7syICiry|9(CPV<x-Ka*3&0v@~{cZ$lIN5NEEEdqqx-Hvg'
'aoz_+&UPhnVsZUX$M3D7?{QCA&-'
'SB}o%OO%PS!6<oK4WFH#?+`zN9X+`_L)A`O*rV?CRCYdLwHN8`YKi2W>m4E8zH8$Rh*@Eqzux4+_xqbD(0y|8724nQ+z>&8!{v>B'
'{-0z<yGt&@^MDq0u*R1O$)!kZx1~jNKo2n4{`I!B>>?;O&xI0@k-zQ-~L+?<CPSkpm=dehZe}NFhT-'
'=g*GiAj09i0pnIgZ;Av)JF|-FgE+t-n%WZ1BApy<q8)=P@Z<8an8N_q-yggZcsZNtmwl%#+MepC)!<V}2Lkv^!>&SntJ|qwJQX}$'
'KvE45Oj3#bbz(q4b39+{b0A?{{Cnl(+|G@`u>$gR)oflzS^Ua~cvU%NwI7L<e_~(!BLww_+Yc)H47*<lH$He#rT})oJNI2Yf*Wyi'
'UyJ@cwq;$-^4}n_w*%?3yy|PZ6Gd*0;P}B|I=St6>iH<Odr-T{QqMweYou#;>LAqf(Va}W#}*z@%KXztylow6a~^ccw-'
'B)WLhWk$SbV!@Frq-MwJ%0XNTNVofqn8&)A+xh6lpA4D$-'
'VaQG;h9e4@>rdX3K{ihbeA_AcSQGMQoqh@wcZs|DHD9EWXyK(m~U3j98Ha<1!+k?eB!%FoYR@N6KQ6QLu$YpE#^&}zK~(u!gf#<7'
'tgLK3#GXq9h%as9zk2X9^M(%lT%?mvNW20dAt8I;vCbE~ub`5CmOSgIeT-Yw8GU!$xUi^VhS>KDaPiaHJ*Bl#G2iTXwH@psa^#?J'
'4!d`Uvs)`D?;E5{N<C^PmR8|fs#Q^#S7I}p+{2CLRgUqGJjf`mWuwl`98h0%qvxWEstobx>pMMMd;ExBO=&%AXgtZXFd>5GiI3fv'
'ThC&XVR8)N88l%zcY0kC!PE=?yD_wP202bd8x5^nj=aOnGG8zBG}albOxealF%eK~QELv?T-'
'ncXXp^w(>n<(R<l!x>egVL74`CU=L)wr5-iQeMPtV(nS%m`7ksO5j1A7^Qw8eh)b6F@)YGF-6a)Z38nNW|^p@-'
'q}E=vC{uBN*V7Bx7L}EU=7(PU#UY=J-'
'<FXywBucM*`A=r+NYoo4!{Knrn#1qvN)(Z*{+bbUebd5p1)>f@?RLEQtz3seTGa$?U<3{ZAuidZn3GX0V53%U$5hIwq!~3?u832r'
'MVBEntd43CEviVFos~iR*z$zM6oId;hY)^bQgP%v`r$3U*mkp8pv>Dhl*Kqp|FsxMA!Vf4F1^Dci_GFfAHhks(_Rl$j=x3RSL$z&'
'rsmfiVU^8;=l<yje~ZuxMePjBvhT-u0y^-7LS<Np%Ph(~S>ipQ>f0wPr-i+JP@4SGjH95=#Yvzm<Avfi8Mzr{(ZT)-'
'Psd0N#<$0ghGrsli!2dYVIit8vdzLH}#2MHmDB71hT;8XMF1ug$%B5}{SY79@Cv9<KQKSr^;4<Bk`T$(y_Mwdu!}F6@(}*+jP?21'
'D%NrU4W}&zs01#e>C2mmm_OL4gP=@=kD=5u#g#{ev7@7f)zxj0!SKrn#=GF3A4J+juDKR(Ukj*gwFLlC^8HPLScs-fl^ehkmQtzc'
'c2S^IL|bq>8QWc4jsSPQrZRcRYQwBjC9e9~vrS-'
'(Trw2qEkg>A@w+Ii;7?4TPwXWsB&w0yYeN?ev7LHRdGIh8@xYVJ<rhL#V45cv0cRePM9q$6Ap2t`%_2JwOQg1-'
'fA=Fd9B0hh|)tn@o~bC3w;?O=9?m+AIJ@;>7ziaGewx*<Bf>JM;MTde)u_(lGKM4)^2nmB=#+mKnMPQ~166!6$m7)nfu2wZ<#!t9'
'&Obi5^9VR%O7dsg9`qPM2bZg*t9$U0EUx9X+u5tbR3r$Nt#)y*V;;EP%hCeh_n&gImWBa%lo{w_xg<B;FH$EE)W`V4d&KS;Zj7Z>'
'MQY&X09_ajV$M9gdS&5Plk{g$<YX&48-'
'z6AB`437~?VI%*w+PPT+McXqyv0_+K1l0@Dl`b>ctxF_bun6}FBSCBKgxj2T@+H91S;$vpf{)OKbsroQE0R~vqT)|iFSQQx>nJ^J'
'd)k^}#&6on!ZtpLJIE#}l@z800Cbt=DFfQ&oDgx38&ZoV2c$;GccI5M63OW!Ys_Pu+&PJ)4a0OKS0)4rM#}_XoziL;4k_eJ~t)MN'
'RulWxUx2H}OQQ?t_`<n0(Rlqt__9<Y$R1r}-pHX(35Qe#R-'
'`5f7fSD@fe0J{eY=N6pA(VK|(ASi70{mAUCHRW&O;kH4B?QTt_R5id?CT*uvVp@0`-'
'7x9O#Q*3(^?t2J&Ht3Yq2$d2xQsb8h}U$Je7H2TUZk4HT_vlnWWXgJjPWMQN~fV4dXQ&DXPkGUxSCAfbr1Q&{yFb1&3DYVv{DAuF'
'Z%6-'
'qHb|#v?W&s>j;N6<ihS^#pq|%eSw%kH$T6R;ihPky`TH`{4{Kl#L+`01spJ6Qv@(VYLg@mx~|IEDroM<E=b~wTS0^XGK+w5Nlmni'
'`2z09F4=sRvPMuVB7jMje$hk$`Dy1%$PN9&yMJ`lTG<5+iZ9elfyTB4aWreLWHh`W8ym^QUz~~!+23-'
'BjyGhM8;LIX07;`Zs6nVn==v~u*W2bIsvGV^#_wu6SehAjJ<Dx5%>2=KK?~~R1fCe`YiR`CRh^~jkcm*HlDvMvD<h-k-jO#7VtQK'
'bHStVzLDs;3{rf4g^|^ar}li9P$0=wXyw%Zbv?P@_OkkKjV<4Pwwc(h8?}ps9K9m^yIP`?bQH*LGPY$+1djUT@PrUj)mD9B2y71U'
'5(W3AB@5LB)VvV-K`-'
'ix+MFsIBKJFy&m(BTeHLh7D+lndE#9VUKxU`2EzqK!$#TuQpt@?lqlv{@m8RXq5?ZK#IQDN>>dzOdexT&R$-'
'=bTF@@QWcvHakEsNslhsU#Ll@qaek|34du?r|Ea*r-ibO?TI_8IdwmdPe-'
'66wS)seUUhp0p(3`JsXl<`9x#RB%eG;q}z3=1F=T>BtdOd(4F6^0Jk7g|gQ3D=}1WaJ7SM0;ykf^z&rlp7~<mX47UR#5Y{8=8m<|'
'gr2qCHve98E{7O3QbFR6%SWv<5fF>cTXAh0$T&0tb1-9&a7RVXzYDZV@Xc((lYEI2nvrU8O#wSt2M@>nBQ@ZCea-'
'1^T=%8`r*9ti_f@;;mwX(dSGScz=6bsh9f_o#rFR!@ny*2?OtXjnX=%yYONh@C#ByL=|B7KqG5a9a*)2sp%oRiF%MoeW?<wg;95~'
'MSCuHTi6v6F6ncmTCHvJq*1N)jPW8Fj960UIvqa&g&EYS!jPL7Kt?&s>8Y&9%I@y|X7TR=W-%&>|4vwcrET~QRZuz;#L+pz-ZqBZ'
'Nx*cS*9G$nV9uH4?j_m&w_riaQcIK4G~Gb;GWa4(yQ#e(5c<r+tYI`5E2v2uwg&6&8=&}lCo6K+&!;GE@zHYX+Ly_<dDv(U=v#0u'
'}gtO*{jM>fyKhaiFCKuQ!}D}zXt&H=`_Y3=iKoL?_8#r2TUmpL4HoBz{G-'
'ER!*3WwCp25iB~=!@WnH~K|PXNy|>g(>g!G8e!07nR0%`|P^I4eY9lmbxr^8Gt_<76pP>MJ1gzn8xtj%Ro`p*hn}PYL?|0umtY8N'
'<Yd#t_*rVVK|$z|BKmO&@0h2G}Xe6qD(&=tD=gv);dVrv-'
';m^Y`R3}?x&N8R4bCXUcD!0HX_?pnxFrB{%&){_i73fp}EUtvK;GG8;=^2w%To}Q&A!6>Ujc`1f4&xorNAnt$rL`O;l$Ex5y}>+H'
'FF4te8a^w+ihU_4*V6C_)~h41-D$pU#A|dLB!w8J3W~sz-DB1-'
't$W?x_=&mhzV~{Zp<*!1lY~<aK~Hp`#Yf1pz+|nvryllxqovW1;piHlp9%?sCa6c}91W=}dcz7I5(}+$+X*VD8eEm=TPE78sS}=V'
'WjoSM4cw6F_~EMcNeDMIhYQzq-'
'N0RHQ1?K8a_%;Lx)41b!_V)~srdVL(%?cR<cT8PgtVCsHhP|0*h|Vx$|QjG5xHwozM#21o<~9v}CQ4YAh|BkOahslJoPES@JCt50'
'jPVq?;>!F{FSIE#QMTrH1h*|pgVJ`qzczK?azxOX#q)T&E?9`2|XNQ@KEO_!ziZO@<#sK11$Zi)_6d}0!tJP>z0C4?q3Vf@$Tk_E'
'iQ>O#!hYDPOgsjE_cYfJ?_j%Xg$U=k@3AiO;a^EVKmy)_F{^XZ!gaP`Ei%ZFXqdhHSh*Cl_f$aKCab??D|P9q@8ISE9`@qS?@@$s'
'T0f=$|!MN&|Ftt$a{q*t)X7v&!!%gn!oj$Nv&{~+k^b78PIBp0dZs!a_}<wz@ebG}X**QYD#&XUy-'
'EufSjp9{o@3e+t}bE}HG8VKQ#+`09J_`{ztFjTXhEwcylHZW59!g}0-Z6{xE(uezf$!-^M>8!EmndzBZN$haOLp-FEub(z%4)FQ2'
'drO?`ginz3s`<`phAlWQL;_@thhZAXn|fE=0PR642+tcm6F@4(GSWlr5*C2)ge>lLo5)nrt5qu!J4h$S;-'
'JjcrhWAl>tH9NwvuR_|0D=a+ap`qF~37c&|^-'
'XPjDw_NdD+XWH0+FzZh|}*CDXpoNGsA%_L~g#^g%C)GIE!O#G%}IeeLdzY$sukxS&*Ip_6_pmlmQ2!~U*W>7;rqdso?v9qpAxL_Y'
'Wh#|D4F}9i_X6NoARxzB=yH;iQT_<1gbFWx<;>cZ;?g0I08xMU5AD18NQ3i*+lHSQ<IBZrZu5;V^D!{XLXxq`$YAYULAWr8ZK(WU'
'd$;1zLqmAZue0+}0COCYsvmXWd$~P6>7EUl)&1TJtPj3%cM%7xcF%d5!GRG8de?2Yi_NVFn>2p$qMxE_biuzmK-'
'w*bZ2$oK<{NzK7h;ojAQJ7d7XSoGUPagKZ7uQKSMJK4nS;h+2&<d;~1>b@>L1~mq*OdC>^4AXNX&tGPiYFP565KkmFuzgPqMdt~N'
'Y9(7D$E+&K7g#D3aLM?;a|~>&M4kxR#hPvRaG~MSAK;nEkE0S5w1x5r6R0wjr=5xoD%aKv7foshAQpJ1NvP#wV#ZTZ9M|`WaDKK7'
'pxa-Hm2iEL@(8vC#lRTHh*s1$M~gv4V}9zes?WhTKG;UXNGx`BX(Kr#8XGtZ<4+Dw@>kHfkoFd1j#>{*1C{Ye@DFlDkVyQuD2sYL'
'(gmd;;-'
'9vzdMSwEMYQNio?z5l0y9xuR@;AOiA({X3nK9kAXK8<4RUbuA8X14Y4(Ri4wxNj`!Ocr`U<Wg*F4&E>ST@Sv{_1StrZ|$#4*37VO'
'oyRu(CHxPp;~_QXkXDtgf<9iRKQnZ*AmlxEE!8UU^z)WgF#`GD!q!;g{3frO_8{UdruqDQPzQ$sGJReGLEdPgpM!^$`?kMcTyc>H'
'sj_YcIJ&CwyY_ieEG-HTRB?_8SHj3!9x!i}D^BzmtUkPx@et<=^k*4-'
'BfM8L+FI8c<f3JpffjcpXQOUt4RJ10^t@2Xp>&4Ys89C8m=s-'
'`j*?jc~8u`ew2Dy^n;Z5XgbJ4HC0(`orq;<x~Cfv?8T6QP_)^(#asNF$HOxpfN%5X3I8$3^X^;aB=9!!NB%%u(dF&iTQ4Y%%+4l7'
'Nz5Bd6hw4fv||?xy*(W-~tJT|&+5i_;Ixc4vgH*ut$uBOt5UBp@6BH8;TrCo_}%GAVB6_<lza9-'
'Yherr%D7ghIURO9@x|myW0n(^gf<Pk*9WH45t}T`>I<L?DI)WuQ0mNiAIb=;eHu+(fRn`zT;9+b1~wuFuFGv$xGTjV$*iVEj`Opq'
'2gbMvliIlEqL4Cby6K>I}7&720~(!d9n%0;xs4{m?oZQHyvbio?J~#e~3|;0+<rZ$z^M!m6R(+w_p@bxyUC#PZY@<Tbs27qJmYz1'
'Y!S1JHcCw2bSkl2hL>tGl&C<HF?-@zk()#n)C1McToDYZb(!O!4B=*BCaa5`elIshDsUpStESSII~DoC8Z0AHs~%X-'
'@3JiFc;lnu8i{Ara0G54PUaE0}$oL4O<yEXE@wt_=R+Qxpu>@pZ{{Sqm^@dCbrkz>K&8V@Cg*(y7_9I9uGVPcL^)kEtQQnbYOLni'
'AbTvjw)18~R<9XxH*WXZ7#Myk~fnOo&oXfFiU|mGh`{dR<;pc@wxZhFS1Cli@U2U#y@RbrJVfmvc#o6Kx&f>14obI}dVB$iChP%>'
'srj%#C8Aci+lq{s(e|de$jrkpIf^<PC}1nS*Uu*oT#!;s&0}tF}5s%<xc<PU3**y{soLM=IAzs#<K*9yOVvp4Nh?Y<)w0)3a<?_w'
'qU$CQlZ=3Flgp;`JUQ6%a9HE{u9%<tyKv{d99tB|I!MX%mS(?WMwuuPtu;4;hEI^dM-bIuZ3!w}VRO#D|d&16Zw030&l1xWW|^9r'
'N$=jtdW$<C%+R4ipuy^x>(fn&_cK+kA(RQk+GRlgjsn$kRfVqPxoA-'
'b;Cdc`Ow6FjQvW1G@KX65D5u8>al_1z@sAfo1%K3VUr(z&IR!|KD046UuO-RVDarX;oa3X_?pW?`0dr-'
'$Q+$|64+F<ZngPRFFZoi&lC(4QG?Dj4Aes5KPr+GX(gWOW6j{`u4^U2qNa2qyLtgyMY_Jg($fTQR9k$U6lnlwX_J9w^)J&QcQo|X'
'mQ>RMRYIU>MW4DHY^=Hb$&gUnFlR05G(^0FU2lKjQ3mIrb0BWG;x2>2#y-'
'Voy27+$Roh)Nda+w@=&R`m)QLASZP_WRFf||cpe#6ZnlwIP_eNY7(-'
'WIY6`&KbP0Rp;<>wH0H~1$_iu2JL(j*qC&~0FJ1B{W93o8_fbd%=VEG<BrrUOPQ|AXRsH^1&raKV7baWc^B!Kngi4A7{2g#1v^-'
'R{_?XA3-'
'EHnlV``Vv=h%+K>s09=l8^@I!D+qG6O4L?0iWWGvZ2cRGTu5n9JH@#|dl2Gw5)fpXPXG})>W7<jjAQsz0U64hk;g?<#gQRI!HMG-'
'@33W$9-'
'}4H1_&&*d46)InDfT3>ftM|u(d9&o<Pnifj8jidJX@E4Aw7vd)`6%w2btwaH&>0*B)e#`0MUJiaJiP&f8@x&y=tRNVpQYPz*p1u4'
'byKd@|<j=(Qf%6bbZ~KoROhK}8Q$?9HSrzOvaBsC^&XH3QGI$&WzVpe2qOy6TrJA_BF_j9|ItyH0$Z>_7C$1IMLmBDx^lI~Q;r@t'
'L^%_Fo&tgquo=SiLVW^-'
'm*qwk}hy@MS{TpT2JO^<x|BoEr4on&7w41+xLQeClg+PDhm#)^{1y9j}5szqrCmomf>*Dm4D9IG7WkLPo$O2{d#;KBSc^Uzex-En'
'^AcATk4(+(pr?)5NEkkxfLhw={Uk{mTE^i<kT@OAQN=4i`NFUxhg*okhQQP3#PiqO@^)(i8!?oI%&!IBJOjff=~bSxe6zrN2dGv5'
'wk<lX6BTnOsjS1TX_tO<JQO644l_JDYX#4!P3dL--sZHmW!NZJTkB(cJTY0DzcGB8Zm}e7m7`0HD+Kf0InTz#t`-'
'sOz>T`|j2D+nE|yxvz+?_I7H{0ZMCuK1#T1<o8ObyE||ku8awF<RI0t&Fd0C(+=ED`$aTeT*e`%!|?xFk^m!+G>&@Rs?otGLt>?I'
'{Z{xxF#+A8Dr3AoXDQmwbLaigS`0_IIE5!MAD)~NDHBXKlGAo9kv`t2sDX%<;ybcC`GFE|>P3U@Vo(3@T#r}2HQ2CrzK2|jRY%g1'
'FuH$Tgv*%22-a&&eyGvh3@n%Rq(g?UgioBe89#>^VWwjZhKa|M5T?$x0KKO%z`IM2A?~ZwlHuIU$GcY_6t&{aQ-1NX^-'
'Zz?tkB~rJc%4T3nP}Hc8eI15h%j-'
'I#5@W%HNR!;>_*XMj847*^OB3v6$3AnmQOLlJhe4nr_v`^bsEg$&xb^V9FfEyt(2p`Od!qBIHr4K*b#nR3|`!p@YD&+#QK@4EOTa'
'T3KgBh_$USW}z@wUwgcvD*<`=?|vj$iZoU!V;<2;FY<$UQtApLSTs+LkkTHyW8`X6*gu4$yrs$I6zf^zS^G+z{xX3y99^nTj=@g8'
'X8|yZH_&L#QJ`yB*v^nByY$P<1b^Yoje_70URjMuhJ>t(TdKeG>hhxn0ZQL)8pv~DeJKHo@>l=q=pWwBN?SXOq`jTGyEO%CVu4%='
'2;!bCkN6<Z8wT)Qpm2AeCb7%{H&~x;9Re<UOBF+Sh(YvxeOFvnHlHH$O`)FOCaV)(Ryxha%Uxi$iD}cPaY`7iuZ`dt4ae_qr>fkE'
'lZFyjAsNiG^~yAQNTp1)DP3_?b11Q`r&v=<RaO^@_a-'
'}u@Xf`Psv4T%@I$zvL$jCE!5~pB_!|cD_4t|OF`4BUNtU>`AnC~eYa{WMmKG51h*>x#DKxD86T8|#IWCgsT_q--'
'Z5?m{OkrZ|_ULH*L6{f|?617S%kxN(LG}=CcWClonx;ltyiGg-wpV~3mFn=sT1|A6j(uHO%9ltwD*wMrRh<l@a81>^?tetf26PBN'
'z7bV#CFE~AY<9k9V&e_RwHY)6&rd@ra7vSQLurv5@Tf{Tukj|da;BEX&|N@Y``SycM5f!CXK+kpiQV{~o#Sbu_Xg#!O0H)DED|bF'
'4b)q8XQZ+Yu87Wj-'
'vN++VB4H#J3?fJ8cX~lTVM^6m;baJsd>oMx**HHOUq*f<H-Rr>jofBpy)NIaraic$nFbxl<LUhcVtGI*@SOujO_1r`NAD;1jf-ph'
'Mzgn?1wZpjEhP#GP5S<M;b8fJ_gz{$mPYELN!~yxlTJ$K)G8}fp8@vB8{fVWJ7qwBS4}4Xt$#3z2^U`_`0?}S);K?SUPbSxf(<7Q'
'%JE(N|nzw={E@!;1x@A!tQEQ``XrcNIX;+g{RE&<a57UJs+YuID8GLXO8*__&%!Aim~p9Fz?B4JT}8HwT1TofK}dEmNs!PbDANep'
'xkWHvn<!MkOBq5^s8jQO{VZJ*WpdW++dvB#C3*BB#of&OKr-Cv~coN{n`MxwlSvtbR1d8a56pLLFtfSK7%fF!fR|*HsnU)x?+vJ_'
'7egu+~{i<cNneDU+#!9&WBM^?(ImLj*`jN!k(pBkdk2#v*G5P{~;1G3fEnbqHMy6_Dr~;;J3sWHY~|SN0YX}22>o=?V+x1|Lau}8'
'7~7n)9BXHEFIky(v=M7lxS{ZxS2x`7RCa4OHlw<N9XsEVPWQ3t8muHk>T^u?4RU2lKh7dTHOkLRigpMo|j#{{BS#$6jvFh+_WLg#'
'SWrexAgt?uSxuRjAzAhPk{?vC8ut!7>GmWnY274!IG_)us^~D58-2A&0Nd*7`J~qSgMxYl?_gD7P_&fL=b$y8QCtN4=V1!{+K-'
'Y0Oho->NW5QV=!d-!B&i_;evF^_|Zo`C)!Z#0Fknqe9lH|x@qf8on9-0lHLtFYalx|iJKdeRSX`uPz&*9bVurR35B%=5-'
'jkP;_qKU`7qFI0?y0%972JkFkA`{4-'
's>bVXda^jK5d+QPayHCZi19Mu~L&i0;loupspu)frBm@Da5GKP&I`58Ny^W}M%AY<HlT@JEx-kI-peE83m=psv%U2+3w(Khz}7u?'
'iRI<80OaARnK~s{he7Wnnet%V>kD8JGDDKPFCDR`cG{^6o|;__;epL!|)-'
'w3u1fR3P6f8n!!>RQ3NZFpCY10lF<@`e`dLEzpUnM+~6=UErOk+Pp&l!6w44#sRIDkG}8!pv0iSx3GFXjwcj3rf47xve(S%fWYrj'
'?#KGL>Tt&{`dAToBk9sAUuFx)(xdF>_aPwd2>TLA;_mRy*?5;-Q*$Z9Vd19Uf&c&j|LdtX^ivUF00H)m1K-'
'{Y0Jh;(vBYQl0ssI200dcD'
)
RAW_BYTES=192351
RAW_SHA256='db2d1c1441be40465343d0e72e5e7569ed2c82ea3a7e54d0bbd967a64881ceee'
def main():
 raw=lzma.decompress(base64.b85decode(PAYLOAD))
 assert len(raw)==RAW_BYTES and hashlib.sha256(raw).hexdigest()==RAW_SHA256
 files=json.loads(raw);root=Path(sys.argv[1] if len(sys.argv)>1 else 'BH18_CAP_RECOVERED');root.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  rel=PurePosixPath(name);assert not rel.is_absolute() and '..' not in rel.parts
  p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
  if name.endswith('.py'):compile(text,name,'exec')
 manifest=json.loads(files['SOURCE_MANIFEST.json'])
 for name,want in manifest.items():
  data=(root/name).read_bytes();assert want==dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest()),name
 print('BH18_CAP_SOURCE_RECOVERY_PASS',len(files),RAW_BYTES,RAW_SHA256)
if __name__=='__main__':main()
```
