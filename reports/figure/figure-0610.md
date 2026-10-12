# figure-0610

AI research report · 2026-09-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# KF27J — an actual-mass obstruction to the whole port40 route, followed by whole-Q cancellation with U1 still unresolved

## Outcome

**Own strict110/additionalweak000 has not been obtained.** The most consequential finding is an executed exact obstruction to the proposed **whole** junior-to-elder port40 mechanism, not merely to opening22→40. With the40 specified old halfspaces fixed, every other support reaching port40 within13 nonnegative radial steps is incompatible with an actual uniform centroid in the closed cube of radius1/200 about the parent centre. A second certificate covers19 steps in the cube1/1000. Arbitrarily many supports, arbitrary new directions, retired old facets and virtual intermediate vectors are allowed within these hypotheses.

A genuinely different finite route was also executed. A20-link connection to the **higher port61**, followed by release of the remaining support geometry and actual-mass reconstruction, produces **KF27J_FF2_G5 and G6: V80/E120/F42, own121/weak000/primitive000, Q=[]**. Their positive P is approximately.6271446411 and.6271407782. A further whole-component cut/reconstruction gives **KF27J_AF2_G5: V82/E123/F43, own121, P=.6130298395…, Q=[]**. Thus the whole Q landscape is actually cancelled, but **U1 is lost and has not been restored**. These are different useful nonwinners, not a simultaneous cancellation or a cross-lineage persistence record.

All **five distinct rational bodies** reported below have exact actual-centroid audits, additionalweak000 and primitivezero000. Two additional compact H files represent the same respective bodies, not extra constructions. The supplied journal’s canonical own110 remains C622, outside the present E249 target. fileciteturn80file0L7-L9

### Source authority and reading

Read the complete526456-byte new journal consecutively through EOF, including the immutable parent; SHA256 `7411a9f92b40f1224b70b424f1a4e7595b4558aec5969ee4296e315135c67b2d`. Direct parent is **figure-0609**, SHA256 `cc979b833c4a44c33611e9cb6dbd2845e5a94c2a569ae22af5bb286414f8a23d`.

Actual starting body is **KF27I_DETACHED_G6**, not an H array interpreted as points and not KF27H_EXACT_ZERO. Its1034-byte point input has SHA256 `a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50`. The previously supplied I capsule and the complete needed source units were accessible. There is no missing continuation-critical exact dependency. QW49F was read as shared scientific evidence but was **not** used as a computational input.

The source-only checks below reuse the inherited exact GMP mechanics engine. They are not two independently implemented physics engines and not a coordinator acceptance of a new record.

## 1. Exact whole-route actual-mass exclusion

Let b be the exact uniform centroid of KF27I_DETACHED_G6:

```text
b=(38946985201102467703899/2315943106719380468000000,
   36285365677586521554829/4052900436758915819000000,
  -276840702507758878921281/8105800873517831638000000).
```

Use the parent’s canonical90-row H representation, with literal raw inequalities N_i·x≤h_i. Define the fixed index set

```text
R=[3,7,12,16,26,28,29,33,34,36,38,39,40,41,44,46,48,49,50,51,
   52,55,58,59,61,63,65,66,67,71,72,73,75,77,79,80,81,85,86,89].
```

This is the complete40-node elder-reaching set, not the24-node persistence component. Set Ω=intersection of these40 **exact** halfspaces. Their directions AND offsets are retained. Ω is unbounded: the exact recession direction(−1,1,0) satisfies every fixed normal inequality. The proof does not pretend otherwise.

Consider any bounded full-dimensional homogeneous convex body L obtained by intersecting Ω with any finite number of further halfspaces. At a proposed actual centroid c, require every nonfixed centred normalized normal to reach

`r(c)=N40/(h40−N40·c)`

through at most m nonnegative radial chords q_i·(q_{i+1}−q_i)≥0. Intermediate vectors may be virtual, so this assumption is more permissive than requiring every intermediate to be an active adjacent support.

**Exact conclusions:**

| Maximum depth m | Closed own-centre cube about b | Strict positive separating-moment interval |
|---:|---:|---:|
|13|‖c−b‖∞≤1/200|(3075146497707,3075146497708)/10^12|
|19|‖c−b‖∞≤1/1000|(1717509162161,1717509162162)/10^12|

In either row, **c cannot be L’s actual uniform centroid**. There is no U hypothesis, no edge-count hypothesis and no requirement to preserve the six old protected vertices. Thus the conclusion also applies to the corresponding smaller protected-cone family.

This is **not** an exclusion of another first-entry port, a new ultimate root outside R, changed fixed halfspaces, greater path depths, or a farther actual centre. Six added supports do **not** imply depth≤19 in general: that bound follows only when those six supports merely subdivide the specified old depth13 forest. Reparenting the existing free supports can make much deeper paths.

### Complete analytic mechanism

The support function of the vectors that can reach r within m nonnegative radial steps is

`H_m(r,z)=|r||z| cos(angle(r,z)/(m+1))^(m+1)`.

For a positive projection onto z, append the angle from z to the first vector to the m successive chord angles. Each chord bounds the preceding norm by the next norm times the cosine of its angle. Concavity of log(cos), followed by the spherical triangle inequality, gives the displayed upper bound. Equal angular steps in the plane of r and z attain it. Every reachable vector also has norm at most|r|, so this support function is |r|-Lipschitz in z.

Put r=r(b), d=c−b. Exactly,

`r(c)=r/(1−r·d)`.

The program verifies `3|r|²<16`. Hence, for ‖d‖∞≤δ,

`H_m(r(c),z−d) ≤ [H_m(r,z)+|r|√3δ]/[1−δ|r|₁]`.

Therefore every z satisfying

`H_m(r,z)<η=1−δ(|r|₁+4)`

is strictly retained by every allowed nonfixed support at every such c. The program constructs98 rational points in this compulsory region and strictly inside the40 fixed inequalities. Their convex hull K is consequently contained in L−b.

The rational generator uses all integer directions in `{−2,−1,0,1,2}³` with maximum absolute coordinate2. It obtains an upper bound on `cos(angle(r,z)/(m+1))` through exact Chebyshev polynomial comparisons, not floating acos. On the interval starting at

`1−9/(2n²)+81/(24n⁴)`, n=m+1,

T_n is increasing; this left endpoint is greater than cos(π/n). Thirty-two rational bisections, integer square-root upper bounds, radial clipping to the fixed inequalities, and a strict9999/10000 contraction produce the complete grid10^6 core. Each of the196 directional certificates across the two cases is checked exactly.

Now fix the integer separator

`w=(−332,934,135)`, with `|w|₁=1401`,

and the affine functional

`ℓ(z)=w·z−δ|w|₁`.

Although Ω is unbounded, its negative section `(Ω−b)∩{ℓ≤0}` is bounded, with six exact conic boundedness certificates. Exact convex hulls and volume integrals give

`Γ=∫_((Ω−b)∩{ℓ≤0}) ℓ + ∫_(K∩{ℓ≥0}) ℓ >0`.

Since K⊆L−b⊆Ω−b, including every available negative contribution and only the mandatory positive core can only decrease the moment. Thus `∫_(L−b)ℓ≥Γ>0`. But an actual centroid c in the stated cube would give

`∫_(L−b)ℓ=Vol(L)[w·(c−b)−δ|w|₁]≤0`,

a contradiction. **The affine shift in ℓ removes any need for an upper bound on Vol(Ω).**

For m13, the positive and negative contributions are approximately52.73990174075371 and−49.66475524304636. For m19 they are49.19705485031482 and−47.47954568815296. All these quantities are rational in the [complete exact certificate](sandbox:/mnt/data/KF27J_PORT40_EXACT.json), not fit constants.

Both cores have98 submitted points and97 true vertices. Their E285 hulls are integration objects, **not** E249 candidates. The negative sections have45/84/41 and42/79/39; the positive core sections both have82/191/111. These auxiliary hulls and every source/input/output hash regenerate.

### Connection to the actual proposed route

The old literal policy was reconstructed exactly, rather than assumed from its filename. After reversing

`15→5→0→22→40`,

every one of its50 nonfixed nodes first enters R at40, and the maximum first-entry depth is exactly13. This is why solving that complete fixed-R policy near the parent centre cannot succeed, even after all its desired arrows become reference-feasible. The obstruction is physical mass, not an unexplained optimizer failure.

Two earlier finite diameter-ball reconstructions of this same full policy failed to close mass. Those searches alone establish no theorem; `portgate_j.py` supplies the separate finite-family proof above.

## 2. A different complete connection: higher port61

A20-link polar path was constructed from old junior15 to old elder61, with19 new support normals. Its initial directions follow the endpoint great circle with a transverse detour of amplitude.9·sin(πt); radii interpolate geometrically. The finite constrained solve enforces every path’s normalized chord margin at10^-5 and strict containment of the six protected physical points. It terminates after5 iterations. All settings and the complete frozen normal array are retained.

Only the19 new normals are rounded to denominator10^10. All90 old H rows remain **exactly unchanged**, preserving their non-simple incidence. The resulting exact body is

**KF27J_HIGHPORT20_G10: V97/E195/F100, own(17,6,21), weak000, primitivezero000.**

At the exact old centroid b, its separate census is **reference121**, P=.5328025892998739…, Q=[]. It is **not reference110**: U2 already exists before the own-mass shift. The exact full reference polar forest includes all109 submitted normals, including inactive ones, and reaches61. Every one of the20 new route chords is strictly positive.

The actual physical volume is approximately.5572744497479293 and its actual centre is

`(.03383994153686235,.027354763877148785,−.12444612060323668)`.

Because every old inequality remains, this is a genuine cut-only descendant. Removed volume is approximately.11820895637855665, or17.499905298402213% of the parent. The removed material’s first moment is approximately

`(−.007498597449135511,−.009196550041358203,.04628058484011993)`,

and its uniform centroid is

`(−.06343510406370335,−.0777990968121471,.39151504469686127)`.

These are actual subtraction identities between exact uniform integrals, not a density adjustment. The finite higher-entry connection escapes the port40 theorem but does not solve simultaneous mass and mechanics.

### Budget actually retained

Thirty original nonsimple vertices survive with their complete cones; their total degree surplus is99. All new supports strictly contain them. Nine old input rows become inactive:

`[6,26,27,29,37,38,39,48,58]`.

After permanently removing those rows, the identical body has100 input supports:81 fixed old rows and19 new rows. Keeping these30 cones intact gives

`E≤3(100+k)−6−99=195+3k`.

Thus **18 further strictly protecting halfspaces fit E249**. This is not permission to move all100 normals independently. Losing protected cones invalidates the bound. It is also not an equilibrium or mass-capacity certificate.

## 3. Whole Q is actually cancelled after releasing the old support restrictions

A subsequent family releases54 of the high-port body’s100 active support rows while selecting18 protected vertices with surplus51. Its two65-iteration numerical solves do not close the mass equations. Their terminal states are not exact accepted bodies.

The important next finite change is to abandon that protected frame. Its68 remaining active normals are frozen as a new numerical checkpoint, then **all non-root normals are allowed to move** through a complete acyclic polar forest. A child with parent p is reconstructed as

`q=p/2+min(1,((1/2−ε)|p|)/|z−p/2|)(z−p/2)`, ε=10^-5,

with the continuous centre value at z=p/2. Each child has a strict positive chord to its parent. The actual filled hull and its normalized centroid residual `g/Vol^(1/3)` are rebuilt at each evaluation. The old fixed-R and protected-cone hypotheses are no longer imposed.

This produces a numerical S1/U7 state in21 iterations. Attempting a one-root physical consolidation for95 iterations fragments P into23 roots. A deliberately **two-root** consolidation then succeeds in15 iterations and yields the rational own121 endpoints below. Its quota permits U2; it must not be advertised as a U1 solve.

A second finite route starts from FF2_G5. Forty new polar points, each with a positive old-polar witness, target vertices and internal edges of the whole current P component while retaining the old global farthest point at reference. The all-normal actual-mass reconstruction gives numerical S1/U4; a95-iteration one-root trial fragments to U18; a21-iteration two-root consolidation gives AF2_G5. Merely targeting all sampled component locations is not a proof that that component was removed. Its final exact P remains positive.

These operations yield actual Q=[], not merely disappearance of an old stable label. Nevertheless they **exchange the missing landscape**: the inherited ownU1 has become ownU2.

## 4. Complete exact physical ledger

Every row has additionalweak000 and primitivezero000. Decimal values display exact rational results; full fractions and carriers regenerate in the [exact ledger](sandbox:/mnt/data/KF27J_LEDGER.json). There is no positive-bar floor.

| Exact body | V/E/F | Own S/U/H | All positive P | All positive Q |
|---|---:|---:|---|---|
| HIGHPORT20_G10 |97/195/100|17/6/21|5, below|16, below|
| FF2_G4 |80/120/42|9/3/10|.6271147420594141;2.8263393354224845e-12|8, below|
| **FF2_G5** |**80/120/42**|**1/2/1**|**.6271446410753194**|**[]**|
| FF2_G6 |80/120/42|1/2/1|.6271407781574007|[]|
| **AF2_G5** |**82/123/43**|**1/2/1**|**.6130298395432991**|**[]**|

All names have prefix `KF27J_`. The exact positive lists not fully expanded in the table are:

```text
HIGHPORT20_G10 P=[
 .6929363212990538,.011416685349385322,.002446542463368782,
 .0013529381170391643,.0001336700054887104]
HIGHPORT20_G10 Q=[
 .19465879010699383,.02974338417587341,.018523646573228306,
 .009672181620846378,.004613816020233098,.002408800691621089,
 .002058000443175792,.0018426764296799387,.0018114279537211726,
 .0013535829180515572,.000687314783805145,.0006303958556704392,
 .00020550963585826485,.00017577460568764347,.00013382706102499557,
 .00007207754836658732]
FF2_G4 Q=[
 3.039763195129324e-8,1.426267581197998e-8,7.360674333533463e-9,
 5.353127986608288e-10,4.440649141295084e-10,2.9145184524931483e-10,
 2.089830708866827e-10,7.335362779700296e-11]
```

The coarse G4 input is **not** a simpler own121. Its tiny positive P and all eight Q bars are genuine strict defects, not weak equilibria. Likewise HIGHPORT’s smaller largest Q is fragmentation, not a better equilibrium class.

### Actual uniform mass of the freely movable entrances

FF2_G5:

```text
V≈.6289024004570145
g≈(−1.0608160721872027e-6,−2.8196859922369937e-7,3.137300169548102e-7)
M≈(−6.671497742419133e-7,−1.773307289052864e-7,1.973055607583e-7)
P in (627144641075319,627144641075320)/10^15.
```

FF2_G6 is a different rational body:

```text
V≈.6289019412874234
g≈(8.471532704222229e-8,1.1962047644947468e-8,9.772124716503734e-9)
M≈(5.3277633633652544e-8,7.522954985680113e-9,6.145708204712009e-9)
P in (627140778157400,627140778157401)/10^15.
```

AF2_G5:

```text
V≈.5893730442687712
g≈(−7.18585880755269e-7,−3.1351802270008484e-7,−2.5792334844323084e-7)
M≈(−4.2351514810928917e-7,−1.8477907147187473e-7,−1.52013069059982e-7)
P in (613029839543299,613029839543300)/10^15.
```

None has exactly zero moment or centroid. The full rational own centre, rather than0, was used for every predicate. FF2_G4 has V≈.628893856142731 and g≈(9.135889504279918e-6,2.7958005267508257e-6,1.8475837201727464e-6).

FF2_G5’s actual physical coordinate fractions have at most52 bits and its largest centroid denominator6824 bits. Corresponding values are63/8577 for FF2_G6 and53/7292 for AF2_G5. These H-based inputs do not retain I’s20-bit physical point arithmetic.

### Current carriers, entire remaining P and true reserve

FF2_G5 has sole stable **hexagon18**, cycle `[6,18,22,76,42,38]`, U2/U42, and saddle69−73. U42 belongs to the stable face; both U are not detached. In the compact42-row representation the U support triples are `{5,19,25}` and `{11,13,18}`. Compact stable18 corresponds to unpruned input39.

Its whole current P component is

```text
[38,41,42,43,44,47,54,56,59,60,62,63,64,66,67,68,70,71,73,74,75,77,78,79].
```

All18 outward true-edge scores are exactly negative. Every active polar vertex has an exact positive path to sole S18, with maximum depth21 for the selected certificate.

AF2_G5 has sole stable **nine-gon13**, cycle `[0,16,77,67,50,75,69,35,2]`, U0/U79, saddle51−78. Its compact support triples are `{4,9,13}` and `{2,21,36}`; stable13 corresponds to unpruned input18. Its whole current P component is

```text
[39,44,45,47,48,49,50,52,53,54,57,58,59,60,61,62,63,64,65,66,67,
 68,69,70,72,73,74,75,76,77,78,79,80,81].
```

It also has18 exactly negative outward crossings. Every polar vertex reaches its sole S, maximum selected depth23. All current crossing scores, their input owners, positive paths and exact moments are in the regenerated ledger.

The68 submitted FF2 rows reduce to **42 active rows**; AF2’s82 submitted rows reduce to **43**. Exact re-audits prove the reduced files have identical vertex sets, facets, edges, moments, counts and bars. With those inactive rows **permanently removed**, FF2 permits **43 arbitrary new halfspaces**, and AF2 **42**, by the sufficient total-F85/E249 bound. Their physical hulls are trivalent. This is not a point allowance or a guarantee of retaining S1.

## 5. Scope of failed continuations

The one-root attempts above were not successful constrained solves, despite lower principal P values. The two-root repairs explicitly accept an unwanted root. No joint own110 nominee is hidden behind those solver labels.

An additional whole-material forest trial used the parent’s38-point reserve and at most85 material positions. It enforced numerical mass equations while optimizing a complete polar forest, but stopped after100 iterations/419 evaluations with normalized mass residual.005415037564603804 and numerical S30/U33. A reference physical forest does not establish ownU1 when its mass equations remain unsatisfied.

No continuous weak-free path, optimizer convergence theorem, global-family exclusion, globally best separator, or cross-lineage record is asserted. The port40 theorem covers its exact stated family; the higher-entry and free-normal experiments genuinely leave it.

## 6. Complete recovery and execution status

The literal delta below contains **28 complete new source/input/checkpoint units** and hash-pins **14 unchanged used units** from KF27I. Its exact reconstruction does not need old numerical histories, the originating sandbox, QW49F coordinates, or C622 FULL76.

- `KF27J_DELTA.py`:55701 bytes, SHA256 `12aaf109e90e52e1f1e27a2005f5ac6fae2e2e59eb2568d8aa612f3b310af95f`.
- Decoded dictionary:96514 bytes, SHA256 `02dd75eac816e37fdb0a6fc028d57ba4bb7eced4e37c34cf9d878eff3dfe2056`.
- Parent standalone `KF27I_CAPSULE.py`:83290 bytes, SHA256 `9dfb6d8b95d4dfa7e28c3e9bffe1ee7265c22c3cab69c6ce747bd868644070fb`, already supplied in this chat. Its scientific parent is the direct immutable xnn result identified above.

A fresh directory populated only with those14 parent units and the literal new delta reproduced **all33 expected exact input/output receipts**. Both mass theorems, all five own audits, the distinct reference audit, compact-representation identities, current interfaces and controls passed. The tetrahedron gives446 and the maximal-facet cube6/8/12; both reject110. The exact engine retains its two uniform tetrahedral mass sums, complete strict/additionalweak/primitive checks, local/global root comparisons and every positive bar. These are crosschecks within one inherited mechanics engine.

The separate frozen producing-map replay reproduced all five exact input tables from the retained binary64 normal arrays. Full optimizer reruns are not claimed. Complete originating source and every non-default setting, including the frozen numerical starts for the final quota-two solves, are in `SCOPE27J.md` and the delta. Floating trajectories may vary; the exact bodies are defined by their complete literal rational tables.

```sh
python KF27I_CAPSULE.py KF27J_REPLAY/I
python KF27J_DELTA.py KF27J_REPLAY/J
cd KF27J_REPLAY/J
python REPLAY27J.py setup
python REPLAY27J.py gates
python REPLAY27J.py bodies
python REPLAY27J.py reference
python REPLAY27J.py proofs
python REPLAY27J.py terminal
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python PRODUCE27J.py
```

Exact stages use Python3.13.5 standard library and g++14.2.0/C++17/GMP6.3.0. Numerical and frozen-producing stages additionally use NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, binary64 and one thread. Assertions remain enabled.

Observed terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


Selected exact receipts:

| File | Bytes | SHA256 |
|---|---:|---|
|PORT40_EXACT.json|422252|a81feb894d77eaea1117bf98232f1f4fcc6b32e939c745b139e304aab127db83|
|HIGHPORT20 input|7166|39774257be155e66c7def8fa13aca597b585797623845f5b8063cd8e6558d6fc|
|HIGHPORT20 own audit|795655|d6bb3af4a77da704ccb8e0fd7592c6260b4fdf07544674ee152d6c6470b97d71|
|HIGHPORT20 reference audit|58182|bf695166bb7f699158e816ddf9e1c863188975dee021756dcecf9b0736030150|
|FF2_MIN42_G5 input|1173|bcf13e9681e7fc40297a7f82491373368dd005097fb059062caef577e0a08394|
|AF2_MIN43_G5 input|1199|6770708bf2bda4248128758d04e177a3c66869c197061a1328ca9932a95dce5f|
|KF27J_LEDGER.json|3184197|6cb97fb7dce353da0ce1ca3c4d44a1a3597a2de196d34fc2658208510998ad9c|

### Most useful next construction

On the retained I ownU1 line, do not continue forcing the depth13 port40 forest back into its excluded centre cube. A different entry or a real change of the fixed-R geometry is necessary for that approach. The high-port control shows why merely supplying a reference polar connection is insufficient even before mass restoration.

On the new actualS1 line, the42/43-support inputs offer unrestricted support reserve, but the task is now to cancel the **current complete24/18 or34/18 physical P component and interface** while retaining actualS1. One-root fragmentation and two-root repair must remain distinguished. The old protected vertices and old centre are not scientific requirements; their abandonment is already part of the executed finite path.

Supplementary copies: [complete new delta](sandbox:/mnt/data/KF27J_DELTA.py), [new working sources, exact outputs and used parent sources](sandbox:/mnt/data/KF27J_HANDOFF.zip). The following complete literal delta and its explicitly retained parent dependency are the durable recovery source, not those links.

## 7. Complete literal new-source/input delta


[Encoded source block omitted; the code in this passage is incomplete.]
