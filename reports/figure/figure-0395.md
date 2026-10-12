# figure-0395

AI research report · 2026-09-17 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Rapid Lynx04 — exact C162 reference centers, center-space exclusions, and the homogeneous-mass gap

Assignment: `figure-0395`. Recovery unit: **RL04_C162_CENTER_AND_MASS_V1**.

## 1. Outcome

**Both fixed cyclic bodies admit strictly interior reference centers with the complete census (S,U,H)=(1,1,0), weak000.** Six simple rational centers work for both bodies. Four exact, witness-switching center paths provide further centers and show why one selected-witness cell must not be mistaken for a whole mechanical component.

**No uniformly filled own110 successor was obtained.** The supplied canonical C622 is not replaced. The durable output instead contains the two parent bodies, twelve simple body/center certificates, four exact center walks, eight sharply scoped center-cell/mass certificates, two root-independent center-space exclusions, two labeled-shape neighborhood exclusions, four exact heterogeneous fillings, and seven genuinely changed rational uniform nonwinners. Every retained uniform body received independently reconstructed full incidence, two exact mass/feature audits, and separate positive centered-tetrahedron integration.

The main constructive consequence is that moving the reference point alone solves mechanics, but the exhibited admissible regions are far from the homogeneous centroid. Contained cutting while retaining the high-y unstable root cannot place a uniform centroid in the certified cells. This direction needs nonlocal material extension, substantial root movement/removal, or a different center component—not continued small corrections around the original own-centered body.

## 2. Source authority and a material correction

I read all five complete NONAFFINE source parts, decoded their dictionary, verified its manifest, and reran its complete exact replay. The correct fifth material is `[internal-source-reference]`. The verified concatenation has 41,484 base64 bytes, SHA256 `c9976cd443a1873b5d96570ac7299a2b6dfaf431519d4e6240fa8f2b995d88fd`; the XZ has 31,112 bytes, SHA256 `8913f442e91a09d6883140d25269587d5ab8400094c9ad122a25e884610d9e5f`; the complete 25-file dictionary has 182,103 bytes, SHA256 `c8b33ea6c12782951664571a8ce48023252c16ddb3af8188e5fd200d157e97e0`. These match the literal decoder. The immutable Bright parent `figure-0393`, SHA256 `2ee8abc72403f981770152547d685735c7cc724a253f7ac7b354dff4fc7e19f1`, was also read completely. The final capsule below does not depend on recovering either original archive.

**The uploaded summary conflicts with the decoded scientific source.** In particular, its D1000 volume/centroid and its assertion that both stable facets have index51 are not the outputs reproduced from EXPECTED.json. I use the decoded geometry, not those narrative numbers.

The correct ordinary filled values in the recovered raw coordinate gauge are:

```text
cyclic_D1000:
V = 10346848943/6000000000
g = (4798080334621/41387395772000,
     -2533936906101/67526803628000,
     -9385589002259/1283009268932000)

cyclic_D10000:
V = 689771138517/400000000000
g = (99147683944200779/855316211761080000,
     -32057396710199771/855316211761080000,
     -600560130922883/80185894852601250)
```

Both have true V29/E81/F54, C162, own121/weak000, unstable raw vertices25 and27, saddle raw0--1. The unique own stable facet is **51 for D1000 and 48 for D10000**. Their minimal common centered denominator costs are46 and57 bits. My independently reconstructed vertices, primitive supporting planes, maximal cycles, true edges, volume and moments were compared exactly with the original replay. Original output hashes are retained in RECEIPTS.json.

Hereafter vertex indices mean these bodies' own sorted29-vertex raw-lex domains. The map to the sorted31-point reconstruction input is `[0,1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]`. D717, original D100, DROP29_C162, these two cyclic bodies, and projectively transformed raw-lex domains remain distinct. In particular, facet48 here is not a transfer of D717's facet48.

I independently cataloged/searched the research library and read the relevant later journal entries. The latest entire navigation brief I used was revision1811, SHA256 `e505c706d71ad7508b36bf101a97e556d8d96169b1b11557f4a3eae32f25c7c7`. Other workers' later results were navigation, not substitutes for unread exact proofs.

## 3. Explicit strict reference110 centers

All the following literal centers work on **both** fixed bodies:

|Center|Exact decimal triple|Unique stable polygon|Common closed L-infinity center-box radius|
|---|---|---|---:|
|A|(.587, -.992, .254)|[26,27,28]|1/200|
|B|(.591, -.984, .240)|[25,26,28]|1/1000|
|C|(.580, -.764, .447)|[26,27,28]|1/10000|
|D|(.580, -.765, .447)|[26,27,28]|1/10000|
|E|(.580, -.766, .446)|[26,27,28]|1/10000|
|F|(.579, -.767, .446)|[26,27,28]|9/10000|

Decimals in this table are terminating **exact rationals**, not floating proposals. Every center is strictly interior. Each has U={25}, no saddle, no weak feature, and zero local primitive-degeneracy counters. A/C/D/E/F use facet51 in D1000 and facet48 in D10000; B uses facet44 and43 respectively.

For C, the actual centroid displacement is C-g, with g given above; its L-infinity length is approximately **0.726475094778** for D1000 and **0.726519830363** for D10000. For F it is approximately0.729475094778 and0.729519830363. These are displacements in the displayed raw gauge, not manufacturing tolerances or scale-independent distances. A is farther away, approximately0.954475 and0.954520, but has the substantially larger certified reference-center box.

For example, the exact selected-chamber radii at C are `1787852993/8238466876000` and `7166715429663/27467523616520000`. At F they are `8059565789/8238466876000` and `19438918268099/19015977888360000`. The common closed boxes in the table lie strictly inside these radii. Incidental zeros of unused predicates inside a box would not create a weak equilibrium: every excluded feature retains an explicitly negative witness, and both desired roots retain every required positive predicate.

### Full actual-feature checking

Write the actual maximal facets as n_f·x<=h_f and h_f(c)=h_f-n_f·c. Interior, facet-foot, vertex and edge tests are linear in c. For an outward-oriented facet edge i→j, its local stable-foot row is `(n_f cross (p_j-p_i))·(c-p_i)>0`. A vertex is unstable exactly when `(p_i-c)·(p_j-p_i)<0` for every actual neighbor j. For an edge i--j with e=p_j-p_i and adjacent normals n,m, the four positive saddle tests are

```text
-(p_i-c)·e,
 (p_j-c)·e,
 h_n(c)*(m·m)-h_m(c)*(n·m),
 h_m(c)*(n·n)-h_n(c)*(n·m).
```

All positive means strict; all nonnegative with a zero means weak-only; any negative excludes the feature. The second audit uses independent local normal-cone edge expressions, while the first uses all-support facet tests and all-point vertex tests. No tolerance enters either census.

### Convex witness chambers, root change, and continuation

For each reference I retain all interior rows and all desired-root rows. For every undesired feature I select a negative row by minimum value divided by its coefficient L1 norm, with deterministic first-index tie-breaking, and reverse its sign. The resulting exact inequalities `a_r·c+b_r>0` define an explicit convex sufficient chamber. All rows, labels and exact box radii are generated in REPORT.json.

The straight A→B segment is not entirely admissible. Its full linear-predicate arrangement was enumerated exactly. Between two transition parameters the census is211, with both stable polygons and saddle26--28. At either transition it is strict110 **plus weak(1,0,1)**, so neither boundary is admissible. The transition parameters are:

```text
D1000:  3528567599/4636225956,
        24782718467/30945197704
D10000: 105588832091357/149120594892258,
        186535768261993/247021184017342
```

A separate witness-switching walk maximizes c_y inside the current chamber with an exact L-infinity slack1/10^6, then rebuilds witnesses. The numerical LP only proposes three active row IDs. Exact Cramer solving and verification of every row produce each saved center; both endpoints, and therefore the whole intervening segment, stay strictly inside the old convex chamber. Four paths and all their bases are preserved. Their best A-path centers have approximate displacements **0.725560390362** and **0.725237327128**. The final selected policy repeats a point; this is **not** a global optimum, global chamber enumeration, or entire-component obstruction. In fact the paths explicitly escape the earlier selected cells. C/D/E/F all lie in the final A-path cells, which is also verified exactly.

## 4. Two rigorous local exclusions

### Fixed-body center-space obstruction, without fixing S or the surviving U

Let A0={10,16,18,20,24,27,28} and B0={25}. For either parent and every strictly interior center satisfying `||c-g||_infinity <= 241/500`, every escape from either pool to its complement is strictly negative. The exact verifier checks

`(p_i-g)·(p_j-p_i)+(241/500)*||p_j-p_i||_1 < 0`.

For A0 the worst upper bounds are `-59320651137471/41387395772000000` and `-283366432140963113/137954227703400000000`; both occur at24→13. The singleton B0 also has a strictly negative complete cut.

Choose a largest-radius distinct point in each pool. Its escape to any other point of that pool is at most minus half their squared separation, and its escape outside is strictly negative by the cut. It is therefore an actual exposed strict unstable vertex. The two disjoint pools force **at least two strict U throughout that whole center cube**, allowing all stable-root and vertex-root turnover.

Thus neither fixed body admits reference110 within L-infinity distance0.482 of its true centroid. This is not a global exclusion: the explicit centers above refute one. The sharp radii for the A0 cut certificate itself are approximately0.4833185854 and0.4838874035; loss of that certificate is not a mechanical feasibility threshold.

### Own-centered, labeled shape-neighborhood obstruction

Let X_i=p_i-g. For the convex hull of29 corresponding changed points, expressed relative to its **actual new filled centroid**, write Y_i=X_i+e_i. If every coordinate of every e_i has absolute value<=1/10, the same two pools still force two strict U, even if incidence changes. The checked bound is

```text
Y_i·(Y_j-Y_i) <= X_i·(X_j-X_i)
 + epsilon*(||X_j-2X_i||_1+||X_i||_1)+3*epsilon^2/4,
epsilon=1/10.
```

The quadratic remainder follows coordinatewise from `ab-a^2 <= epsilon^2/4` when |a|,|b|<=epsilon. Every cross-pool bound is strictly negative in both bodies. This theorem is limited to those29 labeled, own-centered points. It does not cover additional points, unrestricted bulk motion, or all low-C shapes.

## 5. A homogeneous-mass obstruction for the exhibited cells

For any full-dimensional uniformly filled convex polyhedron K contained in a parent P and containing its old root r=p25, triangulation from r gives

`4*g(K)-r in 3*K`, hence `g_y(K) >= (r_y+3*min_P y)/4`.

The right sides are **-11493/24800** for D1000 and **-4597/9920** for D10000, approximately-0.46343 in both cases. This is an exact geometric mass inequality, not a numerical optimization bound.

For each initial A/B cell and each final A/B walk cell, three positive rational weights certify a sharp upper bound on c_y: the weighted sum of its positive chamber rows is exactly `B-c_y`. A rational point attaining B in the closed cell is checked against every row. There are eight such complete primal/dual certificates. The final A-cell ceilings, whose cells contain C/D/E/F, are:

```text
D1000:  B=-1288119943451851411/1688049051896027500
          approximately -0.763082057364
D10000: B=-3465554021554711869976911773/4543712120995441985028450000
          approximately -0.762714258578
```

These lie strictly below the uniform contained-body centroid lower bounds. **No contained uniform reconstruction retaining p25 can put its centroid anywhere in these certified cells.** This does not exclude a changed body's own110 at another center, a removed/moved root, or extension outside P.

For a target in these final A cells while retaining the same r, the same inequality requires the new minimum y to be below approximately **-1.559217** or **-1.558708**, respectively. The parent minima are only about-1.15968. This provides a quantitative necessary extent for a downward material extension aimed at these target cells. It does not certify the mechanical behavior of that extension.

### Exact positive-density realization of the reference mechanics

For each parent and c=A or B, set s=t=1/1000, `b=c+t*(c-g)`, and let Q be the cube of halfside s centered at b. Every support inequality verifies Q strictly inside P. Give P background density1 and add density `alpha=V/(8*s^3*t)` on Q. Direct exact moments give the mass center c.

The extra densities are `1293356117875/6` for D1000 and `3448855692585/16` for D10000. These four same-exterior bodies really realize mass-center110, but are **heterogeneous**, with enormous density contrast. They are mathematical material-closure witnesses, not practical fabrication recommendations or uniformly filled Gömböc records.

## 6. Constructive uniform changes tried and preserved

### Nonaffine 87-coordinate mass descent

A fixed-reference110, fixed-support-sign trust search from D1000 at A used actual oriented-tetrahedron volume and centroid, unit-volume normalization, all nonowner support guards, angular escape constraints, a1e-6 mechanical target, initial trust.01, maximum trust.05, at most20 line-search halvings, and80 iterations. It accepted58 steps. The source includes complete differentiation, guards, first-index witness choices, LP formulation and every non-default setting. The full final binary64 checkpoint was cold-reproduced bytewise in the stated environment.

Its volume-normalized squared centroid gap fell approximately0.835313→0.808261. However, exact ties-to-even rounding of the saved binary64 coordinates at10^6,10^8 and10^10 produced **three C162 own(15,5,18) nonwinners**, all weak000. Each retains reference110 at A. Their centered denominator/max-integer costs are86/86,112/113 and139/139 bits. All lie inside the proved1/10 own-centered labeled neighborhood, with maximum displacement about.022868, so the two-U obstruction already applies. Improving this distance objective did not improve own mechanics.

### Four actual homogeneous projective mass-closing diagnostics

For each cyclic parent and reference A/B I applied the genuine positive-denominator map `Y=(x-c)/(1+p·(x-c))`, then recomputed its uniform filled centroid, not a pushed-forward density. The exact coefficient triples p, divided by10^8, are:

```text
1000 A:  [-6736403354,331755194,569688631]
1000 B:  [-25035418292,834523370,2728104930]
10000 A: [-6384587862,333969467,562145266]
10000 B: [-21118866405,804417826,2475346660]
```

All exact denominators are positive. The transformed support normal is `n+(h-n·c)*p`, with the **plus** sign. Every transformed body has true29/81/54 and C162. The A images are own233; B images own222; all weak000 and zero primitive-degeneracy counters. Their actual centroids have maximum coordinate magnitude below10^-9 but are not zero, and the exact audits use those actual centroids. Even the transported reference0 already has the same bad census. In B images the second U corresponds to parent raw28, not27. Complete new-to-parent facet and vertex maps are retained.

The four minimal centered denominator costs are2379,2447,2504,2548 bits. These are seven durable uniform nonwinners altogether, not seven approximate winners. Each has two complete exact audits and54 positive centered tetrahedra. The numerical mass-Newton routine and its four rounded p outputs were independently cold-reproduced. This was a small diagnostic on the two cyclic bodies, not a repetition or claimed exclusion of the separate D717 projective/metric orbit.

Interrupted bounded SMT at radius3/4 and invalid/interrupted SLSQP attempts establish no infeasibility. A draft trust variable-shadowing bug was corrected before the retained run. The complete retained algorithms are included; no unobserved solver terminal or global search exclusion is claimed.

## 7. Most useful continuation

Start from the literal C/F reference geometry and the final A-cell certificate, not the coincident-point optimizer state. A construction targeting those cells while retaining p25 must add substantial material beyond the old negative-y extent; contained cap deletion cannot achieve the required mass. Alternatively move/remove that high-y root and allow a different center cell and stable root. Couple the new bulk geometry, actual uniform moments, and rebuilt physical/polar escape witnesses rather than closing mass after freezing the old exterior. At most105 exposed vertices gives E<=309 and C<=618, so this29-vertex architecture leaves considerable true-edge budget for a genuinely new corridor or opposite-side region. That budget is not a realizability or mechanics guarantee.

The presently unresolved part is a uniform shape whose actual centroid lands in its own strict110 chamber. Global minimization of center displacement and full center-component classification also remain open in this handoff; the finite paths and scoped obstructions are not substitutes for them.

## 8. Complete recovery and observed verification

The code below is the **entire** standalone recovery capsule. It embeds both29-vertex exact inputs, the full trust HEX checkpoint, all exact projective coefficients, all center/walk data, complete independent auditors, the proof algorithms, numerical discovery methods, and receipts. It requires no original attachment, Library object, network access or sandbox file. Save the entire code block, including its final newline, as RECOVER_RL04.py and run:

```sh
python -B -S RECOVER_RL04.py fresh_rl04
```

Exact replay uses CPython3.13.5 standard library with assertions enabled. It reconstructs every scientific object and checks REPORT.json, **427251 bytes**, SHA256 **27622f77d27f2b1e929e201c324912d3c0ad087db00c4f5696a077bc65c62437**. This source-only recovery and complete replay were executed successfully.

The two exact auditors additionally reproduce strict446/weak000 on the tetrahedron and strict446/weak123 on a rational triangular prism. These sub-floor fixtures are negative software controls, not construction candidates. Maximal facets, not integration diagonals, determine E throughout. The third integrator separately checks positive centered tetrahedra, exactly zero first moments and identical ordinary volume.

Optional numerical replay uses NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, threadpoolctl3.6.0, float64, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Native SMT discovery used libz3 4.13.3.0 through ctypes; it is unnecessary for any exact certificate. Commands include:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B fresh_rl04/RL04_SEARCH.py lp
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B fresh_rl04/RL04_SEARCH.py walk
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B fresh_rl04/RL04_SEARCH.py trust 1000 80 new_trust
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B fresh_rl04/RL04_SEARCH.py projective
python -B fresh_rl04/RL04_SEARCH.py smt 1000 SU center.smt2
python -B fresh_rl04/RL04_SEARCH.py solve center.smt2
```

The exact result does not depend on bitwise reproduction of numerical trajectories. Observed principal terminal markers are `RL04_COMPLETE_FOUR_FILE_SOURCE_RECOVERED`, `RL04_INDEPENDENT_STRICT446_AND_WEAK123_CONTROLS_PASS`, `RL04_FIXED_BODY_SIX_REFERENCE110_CENTERS_AND_EXACT_CHAMBER_WALKS_PASS`, `RL04_EXACT_CENTER_CUBES_SEGMENT_TWO_POOL_CONTAINED_MASS_AND_DENSITY_PASS`, and `RL04_SOURCE_AND_EXACT_REPLAY_ALL_PASS`. The uniform-nonwinner assertions are executed between them.

Capsule identities: source dictionary39655 bytes SHA256 `fe25355976162d75ca10229a3ad8d65a1ce0509d849c9bf999da92237c9ed3e3`; XZ15000 bytes SHA256 `4165565117de8b15995de8a5805f41de3cd14561196304beb54388edd49bb344`; normalized base6420000 bytes SHA256 `97dc82634c962d4972061d57fbb013ed08b7025822225594750342b8e8aeef82`; decoder21536 bytes SHA256 `4ee2e1affe6b26674edb33d204d059b3627026faaa77895e781a8870abc52487`. The embedded manifest additionally hashes both complete source files and RECEIPTS.json.

Convenience copies, not recovery dependencies: complete source and report archive (`RL04_C162_COMPLETE.zip`), standalone recovery program (`RL04_RECOVER.py`), and exact report (`RL04_C162_CENTER_REPORT.json`).

### Literal standalone recovery program

```python
#!/usr/bin/env python3
# RL04_C162_CENTER_AND_MASS_V1: complete source, inputs and exact replay.
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
payload = r"""
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
"""
def verified(b,n,h):
 assert len(b)==n and hashlib.sha256(b).hexdigest()==h
 return b
b=verified(''.join(payload.split()).encode(),20000,'97dc82634c962d4972061d57fbb013ed08b7025822225594750342b8e8aeef82')
x=verified(base64.b64decode(b,validate=True),15000,'4165565117de8b15995de8a5805f41de3cd14561196304beb54388edd49bb344')
r=verified(lzma.decompress(x),39655,'fe25355976162d75ca10229a3ad8d65a1ce0509d849c9bf999da92237c9ed3e3')
files=json.loads(r)
assert set(files)=={'MANIFEST.json','RECEIPTS.json','RL04_CENTER.py','RL04_SEARCH.py'}
out=Path(sys.argv[1]).resolve();out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 assert isinstance(text,str)
 (out/name).write_bytes(text.encode())
for name,m in json.loads(files['MANIFEST.json']).items():
 verified((out/name).read_bytes(),m['bytes'],m['sha256'])
print('RL04_COMPLETE_FOUR_FILE_SOURCE_RECOVERED',flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'RL04_CENTER.py'),str(out/'proof')],check=True)
m=json.loads(files['RECEIPTS.json'])['report']
verified((out/'proof'/'REPORT.json').read_bytes(),m['bytes'],m['sha256'])
print('RL04_SOURCE_AND_EXACT_REPLAY_ALL_PASS')
```
