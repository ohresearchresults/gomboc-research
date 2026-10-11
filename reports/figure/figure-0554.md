# figure-0554

Historical AI scientific report · saved 2026-09-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# RA43 — finite material replacement, compact two-basin bodies, and exact retained-material obstructions

## Result

**No own-centred strict110 body was obtained.** This continuation did execute the literal input and new constructions. Its durable results are:

1. A complexity-safe, 57-parameter material-replacement family in which **at least14 strict unstable and4 strict stable equilibria survive at the actual homogeneous centroid**. Even a much smaller retained core—eight original points and all six bridge points—forces two strict unstable equilibria while the other67 original points move arbitrarily inside the specified outer body.
2. Two finite two-apex replacements with **own222, weak000**, reduced to **37/105/70, C210**, and **43/123/82, C246**. They have new critical carriers and substantial edge reserve, but **worse persistence depths than JOINT75**, not a persistence record.
3. An actual short reference bridge and physical mass repair on the37-vertex replacement. The final exact rational body is **74/147/75, C294, own323, weak000**, with a literal45-gon cap. Both previous unstable vertices cease to be hull vertices; two new unstable vertices appear on the cut front. Mass repair now fits the complexity budget, but the mechanical defect transfers.

A cold, source-only standard-library replay completed with exit0, reproduced **44 byte receipts**, and audited **29 distinct bodies through32 named audit entries**, including the original parent, original bridge and two regression boxes. Across those distinct bodies, **all197 positive P bars and136 positive Q bars** are retained. Every audited endpoint has additional closed weak000 and primitive-zero000. These are endpoint and explicitly stated family certificates, not a class-preserving path theorem.

## 1. Source and exact entrance

The entire supplied345921-byte journal was read through EOF and checked at SHA-256 `a8ed9f06c667803906f4ff20e08381277a2db1dd3695dfce6941c9e6ff5b4c09`. The controlling literal parent is `figure-0552`, declared immutable SHA-256 `ad8dc7c434c78f9d6a7bbd334969fdbfdab83f3a56202484b2698ad9bf1c95d4`. Its previously unexecuted complete `exact_replacement42.py` was extracted as `exact42.py` and actually run. No FULL76 or older WIDE source was needed.

Let P0,…,P74 be the parent's literal lexicographic75 rows divided by10^7, and A0,…,A5 its six bridge points divided by10^8. All81 rows are embedded in the recovery source below. Re-execution confirms JOINT75 **75/219/146, own222**, and O=conv(P,A) **79/231/154, own15/32/45**, both weak000. The primary's exact volume and centroid match its older authority `figure-0549`, SHA-256 `f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605`:

```text
V0 = 942901189534998471379 / 750000000000000000000
c0 = (-53286920506055854442174018051,
      -42633799180986064597953397917,
      -43819041531080084398689329023)
     / 301728380651199510841280000000
```

The current primary P component used here is exactly

```text
J = [22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70].
```

Material labels0…74 mean original P points; labels75…80 mean A0…A5. Later canonical hull labels are explicitly different.

## 2. Executed finite replacements

### The37-vertex body: delete five old points, replace the exposed geometry with two apices

Define

```text
D5 = [4,6,54,59,64]
a  = (1051667,183396,90843)/1000000
b  = (1009714,1735049,646854)/1000000
T37 = conv({Pi : i not in D5} union {a,b}).
```

This direct recipe equals `TWO_CUTCORE_APEX_G6`. The name records how its core was discovered; **no clipping calculation is required to define T37**.

The exact physical insertion sequence is:

| Stage | True V/E/F | Strict S/U/H | Positive P/Q counts |
|---|---:|---:|---:|
| Seventy retained original points |70/204/136|10/14/22|13/9|
| Add a |60/174/116|7/15/20|14/6|
| Add b: T37 |37/105/70|2/2/2|1/1|

The first insertion sees33 maximal facets and hides11 old extreme vertices. The second sees64 facets and hides24 old extreme vertices. Its independently summed visible-pyramid increments are

```text
Delta V = 0.533771274675186...
Delta M = (0.20475336038347947..., 0.34064543683473725...,
           0.05948959699369181...).
```

Exact rational increments equal the differences of the separately re-hulled volumes and first moments. Thus the terminal insertion reconsolidates20 finite bars into two; it is not an assertion of20 isolated continuous cancellations.

The old elder P6 is absent; P62 remains extreme but is no longer unstable. The current unstable material is **P0 and b**. Both old stable planes disappear. The new stable triangles are **[P13,b,P22]** and **[P28,P74,a]**. They are disjoint, but the first contains the new unstable vertex b; the original detached-stable-carrier property is not inherited.

T37 has144 edges of room to249. Its volume is17.1775164111% larger than the original primary's, and its own centre has genuinely moved. Its remaining barriers are macroscopic:

```text
P relative depth = 0.6448411572184589
Q relative depth = 0.5493430245084087
```

In the new canonical hull, S=[26,58], U=[0,35], H=[[12,35],[31,36]]. P peak0→elder35 has component25/cut30, attaining edge[31,36], path `[0,20,24,27,29,31,36,35]`. Q peak58→elder26 has **component9/cut7**, attaining edge[21,29], path `[58,45,29,21,19,32,11,18,22,16,17,33,26]`. Complete components and cuts are regenerated, not inferred from the original primary's labels.

### The43-vertex body: replace the entire old P component

Define

```text
u = (-2159,-200782,-1240421)/1000000
v = (384604,-951251,2432752)/1000000
T43 = conv({Pi : i not in J} union {u,v}).
```

This is `TWO_CORE56_APEX_G6`, exactly43/123/82, own222, weak000. The core is56/162/108, own6/13/17. Adding u gives56/162/108, own19/10/27; adding v gives the final222. The second insertion sees45 facets, hides14 old extreme vertices, and changes27 positive bars into two. Both final unstable vertices are new apices. P6 survives as an extreme point but loses U status; the old junior is not retained as a vertex.

The two stable triangles are [P16,v,P31] and[P6,u,v]. They share v, and the second contains both current U. This is another actual architecture, not a detached-carrier or110 claim.

The final P depth is0.534156753678623, component10/cut33. Q is0.6560198891955281, **component45/cut27**. These are worse than the primary's depths but accompanied by126 spare edges and simple direct construction data.

### Arithmetic controls

Rounding **every input coordinate**, including retained old material, by exact nearest-ties-to-even gives distinct rational bodies:

| Body | Grid | V/E/F | Strict S/U/H | All positive relative depths P ; Q |
|---|---:|---:|---:|---|
| T37 fine |old10^-7, tips10^-6|37/105/70|222|0.6448411572184589 ; 0.5493430245084087|
| T37 all-G5 |10^-5|37/105/70|222|0.6448417192007265 ; 0.5493370542473731|
| T37 all-G4 |10^-4|37/105/70|233|0.6447965117974865, **1.0528296338559018e-8** ; 0.5493749227908618|
| T37 all-G3 |10^-3|37/105/70|233|0.644575223467175, **3.972197152935893e-6** ; 0.5487931785882091|
| T43 all-G3 |10^-3|43/123/82|222|0.5341742685943558 ; 0.655896727661406|

T37 all-G5 has at most72-bit own-centroid denominators. T43 all-G3 has at most46-bit own-centroid denominators; it is a useful low-arithmetic nonrecord. Its P cut changes to32 edges, while its Q component remains45/cut27. T43's other G4/G5/G6 freezes also pass own222/weak000. None of these rounding results is assumed from a nearby grid.

For rapid independent reuse, the **complete43 extreme integer rows of T43 all-G3**, divided by1000, are:

```python
[[-1131,-380,23],[-1127,-283,-218],[-1086,-225,-391],[-1013,-181,-547],[-945,-683,646],[-931,-156,-666],[-871,-801,885],[-869,-137,-738],[-780,-129,-818],[-668,-131,-892],[-635,202,-115],[-589,230,-7],[-559,224,54],[-528,217,107],[-496,331,-186],[-445,199,212],[-382,425,-214],[-366,407,-88],[-316,410,9],[-307,448,-285],[-230,462,-332],[-215,439,46],[-128,476,-366],[-30,481,-367],[-2,-201,-1240],[126,415,143],[140,485,-321],[295,502,-44],[325,457,97],[385,-951,2433],[389,393,124],[432,342,135],[462,305,132],[491,268,127],[517,230,121],[553,-80,-600],[564,161,93],[602,94,61],[633,24,23],[657,-49,-23],[674,-125,-78],[675,-281,-220],[681,-203,-143]]
```

### Actual uniform mass

T37's exact volume, first moment about the construction origin, and own centroid are:

```text
V = 1473157594810301572137 / 10^21
M = (10458831248555578167410430807/80000000000000000000000000000,
     9806540521541147141861245217/30000000000000000000000000000,
    -7319087401598389940641147737/40000000000000000000000000000)
c = (3486277082851859389136810269/39284202528274708590320000000,
     9806540521541147141861245217/44194727844309047164110000000,
    -2439695800532796646880382579/19642101264137354295160000000)
```

Numerically c≈(0.08874501347819445,0.2218939000164911,−0.12420747493992434). T43 all-G3 has

```text
V = 11420873431/6000000000
M = (-133950605119/800000000000,
     -98742775463/250000000000,
      3578427321923/8000000000000)
c = (-401851815357/4568349372400,
     -296228326389/1427609178875,
      10735281965769/45683493724000).
```

No metric change, point-mass ballast, or transported density is used.

## 3. A compact reference bridge followed by an affordable physical repair

Let c be T37's exact own centroid above. Add the following eight points, divided by10^8:

```python
[[-121966840,-14228477,29614435],[-121873124,14211476,55877316],[-112170670,45611326,79020825],[-92861643,77933684,97040808],[-64631970,108906257,108175676],[-28849023,136152128,111047741],[12473116,157339921,104794124],[56751748,170357950,89181269]]
```

Call the resulting hull B. All nine successive chord escapes from T37's P peak through these eight points to its elder are **strictly positive at c**, checked exactly. The full reference census is211, weak000—not reference110. B has39/111/74 and its actual own class is2/19/19, weak000; its volume is2.2162729210902326, a50.4437% increase over T37.

Now define the literal rational cut

```text
q = (-127766266,103253739,105841617)/100000000
L = B intersect {x : q·(x−c) ≤ 1}.
```

This is `COMPACT_REBRIDGE8_CUT`, exactly **74/147/75, own323, weak000, primitive-zero000**. Its actual centroid differs from c by

```text
(5.57786102323098e-10, 1.08449854238289e-10, -1.3852117422635677e-11),
```

with the strict infinity bound **<10^-9 proved rationally**. This is not exact centroid equality or an algebraic-root certificate. Acceptance uses L's own freshly integrated centroid.

Its volume is1.5033628831009627, only2.0503772575% above T37; its first moment is approximately(0.13341596016196713,0.3335870534343483,−0.1867289076492). Exact fractions regenerate from the cut definition.

The **45-gon cap is literal**: every new intersection vertex is computed rationally on the same plane. The original T37 stable planes remain stable, one now supporting a quadrilateral and the other a triangle. The cap supplies the third stable facet. Neither old T37 unstable vertex remains a hull vertex; both new U lie exactly on the cut plane.

In L's canonical labels S=[0,24,54], U=[1,72], H=[[33,44],[40,52],[58,73]]. Every positive bar is:

```text
P: 0.6265753148173572, peak1→72, component46/cut23,
   attaining edge58–73, path[1,2,31,42,43,49,53,55,58,73,72].
Q: 0.5939887250581012, peak54→24, component20/cut22,
   attaining edge0–47, path[54,47,0,24].
Q: 0.1904592298796357, peak0→24, component1/cut45,
   attaining edge0–3, path[0,3,18,20,29,24].
```

Thus the old bridge's E275 mass-repair obstacle is not intrinsic to all short-route constructions. Compaction makes mass repair affordable, but **both the new cut roots and the stable carriers still matter**.

A further exact control adds w=(4/5,3/16,2/3) to T37. It sees **exactly its entire Q9 component and no complementary facet**. The actual body is36/102/68, own6/3/7, weak000, not a cancellation. Its P depths are[0.7061911225737728,0.0010768837864528777]; Q depths are[0.4281203897506869,0.08853430428075257,0.010349237745476799,0.004518208877863264,0.000010005285210821484]. Visible-pyramid mass equals full-hull mass exactly. A small complete visibility packet is useful access, not sufficient mechanics.

## 4. Exact whole-family obstructions: which material really must be released?

### Full replacement of the original P19 while retaining the old complementary material and bridge

Set

`W = conv({Pi : i not in J} union {A0,...,A5})`.

W is62/180/120, own9/23/30, weak000. It has volume1.6586113974293848, only4.41105% less than O's1.7351497170913521.

**For every uniformly filled full-dimensional convex L with W⊆L⊆O, there are at least14 strict U and4 strict S at L's own centroid.** The protected U material labels are

```text
[0,1,2,3,6,7,8,51,65,73,74,75,76,77].
```

The protected stable triangles are the material sets

```text
[6,14,18], [51,65,66], [47,51,65], [6,63,80].
```

This includes **arbitrary independent repositioning of all19 omitted P points anywhere in O**, with the other56 old points and six bridge points fixed. It is a finite57-coordinate family, not a local chart. Every such point-generated member automatically has at most81 vertices and E≤237, so its failure is not exhausted complexity. Additional weak equilibria elsewhere do not invalidate the strict witnesses.

### Releasing almost all the old core is still not enough inside this outer body

Let W14 be the convex hull of material labels

```text
[0,5,6,13,20,57,65,69,75,76,77,78,79,80].
```

This is **eight original points plus all six bridge points**. For every uniform convex W14⊆L⊆O, **P6 andP65 are strict U**. Hence allowing all other67 original points to move independently inside O still cannot produce110 while this geometric core remains contained.

A second certified core W12 uses

```text
[0,5,6,13,17,20,47,65,69,75,77,79]
```

and forces the same two U. W14 itself is14/36/24, own7/12/17; W12 is12/30/20, own10/11/19. These cores were greedily nominated and exactly verified; no minimal-cardinality assertion is made.

**Proof certificate.** Write VW,MW for the exact inner volume and moment, δ=VO−VW. For a retained vertex v, outer vertex w≠v, d=w−v and ℓ(x)=(v−x)·d,

`V_L ℓ(c_L) ≤ (VW v−MW)·d + δ max(0,max_{x∈O} ℓ(x)).`

Every required right-hand side is a strictly negative rational. The outer-vertex inequalities cover the entire outer tangent cone, so the conclusion concerns the actual centroid and actual hull of every intermediate body.

For an oriented common facet edge a→b with outward normal n, set u=n×(b−a). The exact lower bound

`u·(MW−VW a) + δ min(0,min_{x∈O} u·(x−a)) > 0`

places every actual centroid's face projection strictly inside the retained facet polygon. The common support plane remains a support for L. All inequalities are enumerated in the recovered certificates; no floating margin or assumed inherited incidence is used.

### A quantitative deletion-volume threshold without a large retained core

For the same original bridge O, every full-dimensional uniform convex L⊆O retaining P6 andP65 and satisfying

`vol(L) ≥ (213/250) vol(O)`

has these **two strict U**. Thus deletion of at most14.8% of O's volume cannot suffice within that retention condition, irrespective of the number of new faces or other removed vertices.

For Δ=VO−VL and T=(VO v−MO)·d, the exact bound is

`V_L (v−c_L)·d ≤ T − Δ min_{x∈O}(v−x)·d.`

The minimum is negative, and every upper bound remains strictly negative at Δ=(37/250)VO for both vertices. The computed per-vertex sufficient relative thresholds are approximately0.3777759392 for P6 and0.1483045617 for P65; the theorem uses the simpler safe rational37/250. This is neither a minimum deletion theorem nor an exclusion after moving these roots, adding exterior material, or changing the metric.

The earlier prescribed-centre dual test was also actually evaluated: at the literal rational old-centre trial q, ΦO≈1.2911051518351 and ΨW≈1.0827060483233 are both below VW≈1.6586113974294. That excludes centring this retained-material envelope at c0. The **own-centred U/S envelope above is stronger for the present task**, because it does not prescribe c0.

T37 andT43 deliberately leave O and change the critical material; neither is covered by these exclusions.

## 5. Finite search, negative controls, and limits

The capsule preserves all producing units, literal retained numerical pins, exact rational freezes, seeds and nondefaults. Discovery uses current convex hulls and uniform-volume moments, not point means or transported density.

Three single-apex differential-evolution runs on differently released cores completed, seeds4301–4303,180 generations,population multiplier10,5430 objective calls each. Two six-coordinate/two-apex runs, seeds4311–4312, requested250 generations but were **interrupted**; retained best-score evaluations9830 and9895 are not total-call or completed-generation counts. Their rounded pins give the exact T43/T37 bodies above.

Three18-coordinate quadratic material-field runs moved all75 original points, re-hulling and re-integrating actual mass. Seeds43040–43042 used L-BFGS-B with a700-iteration ceiling; all exited with line-search failure before that ceiling. They are finite unsuccessful experiments, not a proof against nonaffine redistribution. Twenty compact route/repair nominees used link counts9–12 and transverse phases0,−0.1,−0.04,0.04,0.1; none yielded a target. The8-point, phase−0.04 pin is the exact retained control above.

A48-step material-deletion search starting from the old bridge's rational centroid-repair cut gives these exact controls:

```text
step25: 99/249/152, C498, own6/5/9;
step28: 96/245/151, C490, own6/4/8;
step48: 76/200/126, C400, own15/12/25.
```

All have weak000 and full positive-bar ledgers. Step48 includes a genuine positive P bar **4.004510027180926e-15**. The exact classes, not the floating screen's small-feature counts, are authoritative. The old rational cut itself is124/275/153, own244, outside budget; the retained `CONE_A4` control is91/239/150, own8/7/13. Both are now actually audited, not unexecuted recipes.

These finite searches establish no global obstruction. The exact obstructions above apply only to their stated Euclidean material envelopes or retained-volume conditions.

## 6. Most useful continuation

T37 offers a direct37-point, C210 physical entrance with **Q9/cut7**, a changed root and new stable carriers. Its larger depths mean it should coexist with, not replace, the shallower JOINT75 record. The coarse43-point G3 entrance offers a different low-arithmetic architecture.

The compact bridge experiment separates the remaining issues: finite mass repair can fit E249, yet preserving both current stable planes leaves two stable carriers and the new cut front creates a third, while unstable roots move onto that front. The next substantive replacement should jointly change **those current stable carriers and the new cut-root junction**, rather than retain the old core, insist on c0, or merely add a longer reference chain. From a37-vertex body, at most seven additional points give at most44 vertices and84 facets; one further cut then gives at most85 facets and E≤249. This is a useful unconditional complexity budget, not an equilibrium theorem. The observed eight-point example also fits because its actual hull is smaller.

## 7. Self-contained recovery, actual checks, and receipts

The inline capsule below contains **25 complete source/input/manifest units**. Decoded JSON: **83096 bytes**, SHA-256 `fb7a6537d4fd28774bae02d14f344cceb572db7cba948825c56889f9f2b91ab4`. It includes all75+6 parent coordinates, exact general auditor, all new generators, all numerical producing programs and pins, and the44 output receipts. It needs neither this sandbox nor an older source library.

Exact replay used **CPython3.13.5, standard library only**. Numerical discovery used NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, CPUfloat64 and one BLAS/OMP/Torch thread. Numerical plane grouping and tiny-bar reporting floors are discovery conventions only; every exact endpoint recomputes all maximal facets, true edges, strict and closed-weak constraints and every positive bar with rational arithmetic.

There is one full exact supporting-triple hull implementation, with two-origin exact volume/moment checks and independent visible-pyramid insertion identities—not two independent hull engines. Equal radial levels are batched simultaneously. Exact polygonal coplanarity is preserved in the clipped bodies. No continuous class claim is inferred from endpoint audits.

Save the following program as `RECOVER_RA43.py`, then run:

```sh
python -B RECOVER_RA43.py
cd RA43_RECOVERED
python -B REPLAY43.py
```

Observed source-ready and cold-replay markers:

```text
R43_SOURCE_CAPSULE_READY 25 83096 fb7a6537d4fd28774bae02d14f344cceb572db7cba948825c56889f9f2b91ab4
R43_FULL_REPLACEMENT_ENVELOPE_PASS 14 4
R43_RELEASED_CORE_ENVELOPE_PASS 12 14 2
R43_VOLUME_TOLL_PASS 37/250 6 65
REFERENCE_U1_OWN_REPAIR_323_NEW_CUT_ROOTS_EXACT_PASS
R43_COLD_EXACT_RECEIPTS_PASS 44
R43_ALL_EXACT_GEOMETRIES_BARS_WEAK_PASS 32 29 197 136 NO_OWN110_CLAIM
```

Selected executed receipts:

| Output | Bytes | SHA-256 |
|---|---:|---|
| T37 fine audit `TWO_CUTCORE_APEX_G6.json` |12865|`49b6bece9899228cf4716eba151dc9dc8e0e4299fa6109055fb816e86b2edbdc`|
| T37 all-G5 literal37-row input |842|`da50a8d1a6001a155eff1766abdaadd0ecd6948134a73867d330ae1111fff40e`|
| T43 all-G3 literal43-row input |669|`6b538b2436128c1b17daefb2a51f8bb70b14583ebf520488928e9f6656c4ae71`|
| `COMPACT_REBRIDGE8_CUT.json` |99669|`3548cc3bced1c59c6910eb54b27c945e661945e489a447b801c4f4e17997df0c`|
| `COMPACT_REBRIDGE_CERT.json` |9557|`aff82de4011873a865afebe77d297ecf59cc378f2d8527a5497db2d4402919ad`|
| `ENVELOPE.json` |101111|`2c493384f82f6c4fdcfe16b4849cacda1e13075b7b770e62ebbb90b0aa858582`|
| `PHYSICAL_CERTIFICATE.json` |46970|`bc9ee57a30f4a08ed6b3268b2687874512ac2902a937d0d288c1a2da8115cfa1`|
| `INSERTION_LEDGER.json` |5220|`ec8f58a591d2b1b0ffc2557b7d9d2b0cead805a92810c8f1aa0410b69951e011`|

The supplementary [source-and-audit archive](sandbox:/mnt/data/RA43/RA43_sources_and_exact_audits.zip) is1033130 bytes, SHA-256 `0eb8b97adddbeb4d4a524cf771e263e7931b7394f7a098f6963fc24f82d6350e`. It is convenient but not required by the literal recovery capsule.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
