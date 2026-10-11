# figure-0409

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Comet 83 — exact stable-basin successors and an exact contact closure

Branch: `[internal-source-reference]`.

## Outcome

**No own110/weak000 body was found.** The strongest retained successors are **B217**, V56/E162/F108, own312/weak000, with an **83-bit minimal common centered denominator**, and its exact four-contact companion **Q53**, V56/E161/F107, own312/weak000, with a **150-bit denominator**. Both have a complete positive physical true-edge escape tree at their own exact filled-volume centroid. Their certified centered-polar bottleneck lies strictly between −0.241997 and −0.241996.

This improves the magnitude of C330’s global barrier by a factor greater than2.19, but increases its stable count from two to three. It is not an equilibrium-count improvement or a new own110 record. The accepted internal own110 incumbent remains C622, V176/E311/F137. :contentReference[oaicite:0]{index=0}

Four new exact nonwinners, both exact parents, all materially used numerical source units, all required numerical inputs, and the numerical checkpoints are recoverable from the complete inline capsule below. No old sandbox, external library, research connector, or numerical optimizer is required for exact recovery. The final capsule was decoded into a fresh directory and cold-replayed through the six-body terminal marker.

## 1. Source closure

I read all five supplied files completely, including the entire1,110-line journal, branch memory, and literal parent `figure-0404`, with declared SHA-256 `25d8541c3d83465da72793ba457cc26fce1c5e5379520784d41a08042bcf92c7`. No necessary exact dependency is missing for the constructions reported here. The selected C330 geometry/auditors and C288 subset recipe supersede the historical source-delivery warning for this current closure. I did not treat older C320/C510 paths as accessible objects. :contentReference[oaicite:1]{index=1}

Actual supplied-file identities were checked: C330 geometry Markdown4269bytes/SHA`66acbe5c6104c66f7b6d19ee683fc4281787435772b5bd3cf3e98d549615da18`; audit Markdown18024bytes/SHA`9a9df583f7de4e822792c875bc35043156693591d06b14c924c488995a2ff4b2`; C288 recipe5025bytes/SHA`46039fed037c8e1399db9e93caac447c88ef07782bbb412c78965887b60cf4e5`; complete numerical methods23920bytes/SHA`8a4d778ae556e0fcac63cdfa65baa735f524bb1af200e3efbc2b59b1f9f3dbb3`; journal186304bytes/SHA`5dc088b1b49fd0186af478ca33c47e973ad2af8726344e9a0628ad9024d228b7`.

Both parents were reconstructed and fully audited again. C330 gave57/165/110, own211/weak000, common centered denominator72bits. C288 gave76/144/70, own211/weak000, denominator5173bits. Their reconstructed identities agree with the selected source closure. :contentReference[oaicite:2]{index=2}

## 2. Retained exact bodies

| Label | Full body name | V/E/F | Strict S/U/H | Weak | Common centered denominator bits |
|---|---|---:|---:|---:|---:|
| B79 | `SC83_C330_VBASIN79_G1000000` |57/165/110|3/1/2|000|86|
| B217 | `SC83_C324_VBASIN217_G1000000` |56/162/108|3/1/2|000|83|
| Q53 | `SC83_C322_QUAD51_53_54_55_OWN312` |56/161/107|3/1/2|000|150|
| AP300 | `SC83_C324_ALLPAIR300_G1000000` |56/162/108|6/1/5|000|86|

Every row has primitive equilibrium-zero counts000 and completed independent A/B/full-filled-mass verification. B79, B217 and AP300 are triangular. Q53 has106 triangles and one genuine quadrilateral. Its integration uses108 triangles, but its maximal face count is107 and its true edge count is161.

### B217: the low-arithmetic continuation chart

Exact ordinary volume:

`2370444780652048591/1000000000000000000`.

Exact filled centroid:

`(35633953978486748375803/2370444780652048591000000, 22896900476332098186943/1896355824521638872800000, 25161526167117592444393/948177912260819436400000)`.

Numerically, g≈`(0.01503260243366,0.01207415833055,0.02653671409316)`. Its actual volume is approximately2.69299658% larger than C330’s. This is a finite material change, not a free reference-center adjustment.

Stable faces are`[0,49,104]`; the unique unstable vertex is raw-lex14; the saddles are`[40,41]` and`[44,45]`. Maximum reduced numerator/denominator lengths are raw21/20bits, centroid75/81, centered83/83, and volume62/60. The minimal common centered denominator is83bits; the integer tetrahedral embedding needs up to84-bit coordinates. These are different arithmetic statistics.

### Q53: exact physical contact completion

The numerical continuation approached the four-point set`[51,53,54,55]`. I did not accept a nine-decimal plane merger as an exact contact. Instead, I changed **only the x coordinate of input vertex53 in B217**, putting these four physical points exactly in the plane through51,54,55:

`x53 = 23407939183977069/31993770212000000`.

All other raw coordinates remain those of B217. `FLATTEN53.py` reconstructs this equation with rational cross products; there is no root-finding or rounding. Independent exact hull audits prove that true edge53–55 disappears and maximal face67 is the quadrilateral`[51,53,54,55]`.

Q53 remains own312/weak000, with stable faces`[0,48,101]`, unstable raw14, and saddles`[40,41]`,`[44,45]`. Its exact volume is

`37919733364799097937835052133/15996885106000000000000000000`.

Raw coordinate maxima are55/55bits; centroid144/150; centered150/150; volume95/94. Its minimal common centered denominator is150bits and integer embedding uses up to151bits. Q53 supplies a genuine nonsimplicial contact chart; B217 supplies cheaper arithmetic. Neither improves C330’s stable count.

## 3. Complete physical escape systems and global polar certificates

For centered vertices x,y, define

`W(x,y)=x·(y−x)/(|x||y−x|)`.

The root is a maximum-radius vertex. A root-reaching true-edge tree whose arrows all exceed l proves beta>l. A nonempty root-excluding cut whose outward true-edge arrows all lie below u proves beta<u. Both certificates are constructed exactly and independently rechecked using rational arithmetic.

| Body | Exact physical interval | Exact centered-polar interval |
|---|---|---|
| C330 parent |`(3/20000,151/1000000)`|`(-133091/250000,-532363/1000000)`|
| C288 parent |`(1/1000000,1/500000)`|`(-279687/500000,-559373/1000000)`|
| B79 |`(11/250000,9/200000)`|`(-342109/1000000,-85527/250000)`|
| B217 |`(1/125000,9/1000000)`|`(-241997/1000000,-60499/250000)`|
| Q53 |`(1/125000,9/1000000)`|`(-241997/1000000,-60499/250000)`|
| AP300 |`(3/1000000,1/250000)`|`(-318141/1000000,-15907/50000)`|

B217 and Q53 each have55 positive physical tree arrows to raw14, every one strictly greater than1/125000. This establishes the whole physical escape system, not merely the root’s own normal cone. Their polar trees have107 and106 arrows. Each has a30-vertex cut with32 outward true arcs.

The literal Q53 polar cut is

`[38,40,41,48,49,52,56,57,59,60,61,62,63,64,65,69,72,73,74,75,76,77,83,84,85,87,89,92,93,96]`.

This is a complete bottleneck certificate for the stated graph/root, **not a claim that it exhausts every unwanted stable basin**. Stable face101 lies outside it and still has to be resolved. The two unwanted stable triangles are`[5,46,40]` and`[40,46,41]`, sharing true edge40–46. Both saddles40–41 and44–45 remain live constraints.

For exact comparison, write x=N/s,y=M/t with positive denominators and set a=N·N,b=M·M,c=N·M,D=s*c−t*a,R=s²*b−2*s*t*c+t²*a. Then W=D/sqrt(a*R). The generator compares signs and integer squares, reversing squared comparisons for negative numerators. The verifier independently uses the rational quantities x·(y−x) and |x|²|y−x|². No floating square root enters an asserted predicate. Full parent arrays and outward cut arcs are deterministically regenerated in `TREES.json`, with byte identities pinned in `EXPECTED.json`.

## 4. Search history and scoped findings

All nonlinear trials recomputed the actual convex hull and ordinary filled-volume centroid. The numerical plane deduplication tolerance was9decimal places; only the later exact audit established topology.

The useful algorithmic correction was removing an unintended **fixed-exposure restriction**. The original all-vertex continuation rejected trials whenever an input point ceased to be exposed and stalled at a disappearance/contact boundary. The corrected version computes the physical graph on exposed vertices and permits disappearance. From the literal B79 G8 checkpoint it made217 accepted steps over238 iterations, producing B217 after exact grid10^6 freezing. Its true-edge polar barrier improved from about−.3421 to−.2420.

The unrounded scout reported56/161/107, whereas exact grid10^6 freezing gave56/162/108. I retained the latter as B217, not a fictitious exact C322. Q53 was subsequently obtained by the separate rational contact completion.

Configured physical margins were fixed within each run. The actual nonlinear acceptance gate was one quarter of the configured margin. The main stage used configured3e−5, hence a fixed7.5e−6 acceptance floor, lower than the first stage’s2.5e−5 floor. There was no adaptive decay to zero within a run, but I do not claim preservation of C330’s original reserve. Every retained rational endpoint received a fresh exact positive-tree audit.

| Numerical run | Iterations/accepted | Observed outcome |
|---|---:|---|
| Frozen-active bottleneck from C330 |99/79|B79 production checkpoint, S3/U1|
| Frozen-active continuation from B79 G6 |31/13|Negligible progress, S3/U1|
| Exposure-releasing bottleneck |238/217|B217 production checkpoint, S3/U1|
| Minimum-total-defect true-edge tree |100/89|S3/U1, beta≈−.250253; no exact successor accepted from this endpoint|
| Further worst-bottleneck continuation |36/18|Contact/trust stop near−.24199559, S3/U1|
| Sum over all current stable-sink bottlenecks |31/13|Contact/trust stop, S3/U1|
| Complete-graph/all-pair continuation |300/300|AP300, subsequently exactified as own615|

Finite deletion screens tested57 single deletions from C330 and56 from B217. None passed their specified S2/U1 and positive-physical-margin filter. These are finite numerical screens, not exclusions of deletion families or possible descendants. Coarser-grid failures likewise do not prove an arithmetic lower bound.

### Exact surrogate countercontrol

AP300 is retained as a methodological control. For B217, both true-edge and complete-graph polar beta lie in`(-.241997,-.241996)`. For exact AP300, complete-graph beta improves to`(-196429/1000000,-49107/250000)`, while true-edge beta worsens to`(-318141/1000000,-15907/50000)` and stable count increases3→6. Both graph comparisons have exact tree/cut checks.

A strictly positive full all-pair escape system is a valid exclusion witness for nonroot extrema. However, **improvement of a negative all-pair bottleneck is not quantitative improvement of the physical true-edge basin**. The control demonstrates that distinction with two retained exact bodies, rather than inferring it from optimizer failure.

## 5. Verification and durable recovery

Auditor A enumerates rational support triples, proves boundedness, reconstructs the maximal complex, integrates uniform filled volume, and checks all strict/weak equilibrium features. Auditor B independently reconstructs support-pair lines, cycles, moments and feature predicates. Their canonical outputs agree byte-for-byte. The V/H wrapper checks both containments and exact exposure of every supplied point. A third centered integer-tetrahedron integration proves positive volume, matching volume, and zero first moments.

Cold controls gave tetrahedron strict446/weak000 and prism strict446/weak123. Both auditors rejected three invalid H descriptions; rational tree/cut checks rejected an illegal floor and a root-containing cut. Hashes are integrity checks in addition to those mathematical checks.

Key exact input identities:

| Input | Bytes | SHA-256 |
|---|---:|---|
| C330 parent |2411|`d2136dce7e42094ac636370e0726a1b829ad07235eb691e2036b36259e0517d7`|
| B79 |2641|`4b344485ad2e3923278799fa8d9788197052133486603730c57e8c3a83c63f35`|
| B217 |2592|`012ba362c43133aff721daad7cf4703de57748f4a6d6829bc6a401cd55d3e3a4`|
| Q53 generated input |4408|`8db491046ec0179f75bc88302ed185e228d458f126afe2eb0c2dd4aa3832c17e`|
| AP300 |2587|`f54dc5bdaa8c708f2656c1cef351b516b8dbc963c06ac6eddfb86b60117077e8`|

The inline source has36 units:35 manifest-listed code/data units plus `MANIFEST.json`. It contains literal geometry, both parent closures, the Q53 generator, all independent auditors, exact graph certificates, complete numerical producers, all intermediate numerical inputs, checkpoints and non-default settings. There are no omitted helpers or arrays.

Exact recovery requires CPython3.13.5 standard library, with assertions enabled:

```sh
python -B -S RECOVER_SC83_BRANCH.py SC83_SOURCE
python -B -S SC83_SOURCE/REPLAY_BRANCH.py SC83_VERIFIED
```

Actually observed final markers:

```text
SC83_BRANCH_INLINE_SOURCE_RECOVERED 36
SC83_BRANCH_EXACT_6_BODIES_AB_MASS_TREES_AND_CONTROLS_PASS 4158 9efb2cac8e9145b687a6522694253441f996bd66a9723beae95c93703c3e6788
```

The final marker was obtained after decoding the final capsule into a fresh directory. It binds all six reconstructed bodies and the full source manifest. Individual output byte counts and hashes are in embedded `EXPECTED.json`.

Numerical reproduction uses NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu and NetworkX3.6.1, float64, one OpenBLAS/OMP/Torch thread. Every non-default option, source identity, and frozen input/output identity is in `FINITE.json`. `FREEZE.py` uses `np.rint` ties-to-even, lexicographic integer deduplication and exposed-hull facet nominations. The three production freezes were rerun and matched the retained literal inputs. The exact integer inputs, not portability of floating optimizer transcripts, define the retained solids.

**Most useful continuation:** keep both B217’s83-bit arithmetic chart and Q53’s exact quadrilateral chart. Redesign the full certified bottleneck interface while simultaneously handling the other stable carrier outside the cut and both saddles. The56-point description permits49 more exposed points before V≤105 gives E≤309. This is a combinatorial budget, not a mechanical guarantee. Do not freeze an obsolete exposure list or accept a near-contact tolerance as an exact equality. Preserving Q53’s new quadrilateral indefinitely is optional, not an exclusion of other topologies.

An earlier interrupted workspace did not preserve a usable new output. No positive construction or certificate claim here rests on that lost scratch state.

## 6. Separate current-literature notice

The primary-source abstract of *An explicit mono-monostatic polyhedron*, submitted September7,2026 by Tancredi Schettini Gherardini, reports two rational examples, the smaller with56,946faces, and exact own-centroid certification. I checked the abstract and submission metadata, not the full paper or its code. This is an external author-reported result, not part of this replay; no priority or public-record conclusion here depends on it. :contentReference[oaicite:3]{index=3}

## 7. Complete inline recovery capsule

Save this complete source as `RECOVER_SC83_BRANCH.py`. The payload dictionary is120158bytes/SHA`04fc13eb46027298b9cc03d45615b24431d66c32da5fce51ce7841112ee3f615`; compressed payload33432bytes/SHA`b3ac0e5ccc211dae4af3c1dd42cd24a6c978a1e0888bc65762e495c3e3f578e9`; normalized base6444576characters/SHA`b9d90d3923c4406e0d078f18e2f65d5b065298861297c2a124a05edcac3e7314`.

```python
"""Complete inline SC83 branch recovery. Standard library only.
Decode to a fresh directory, then run REPLAY_BRANCH.py there.
"""
import sys,json,hashlib,base64,lzma
from pathlib import Path,PurePosixPath
assert __debug__ and len(sys.argv)==2
B64 = """
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
"""
s=''.join(B64.split());assert len(s)==44576 and hashlib.sha256(s.encode()).hexdigest()=='b9d90d3923c4406e0d078f18e2f65d5b065298861297c2a124a05edcac3e7314'
b=base64.b64decode(s,validate=True);assert len(b)==33432 and hashlib.sha256(b).hexdigest()=='b3ac0e5ccc211dae4af3c1dd42cd24a6c978a1e0888bc65762e495c3e3f578e9'
r=lzma.decompress(b);assert len(r)==120158 and hashlib.sha256(r).hexdigest()=='04fc13eb46027298b9cc03d45615b24431d66c32da5fce51ce7841112ee3f615'
d=json.loads(r);assert len(d)==36
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts
 target=out/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(text.encode())
m=json.loads(d['MANIFEST.json'])
for name,z in m.items():
 v=(out/name).read_bytes();assert len(v)==z['bytes'] and hashlib.sha256(v).hexdigest()==z['sha256']
print('SC83_BRANCH_INLINE_SOURCE_RECOVERED',36,flush=True)
```

Convenience copies, not recovery dependencies: [recovery program](sandbox:/mnt/data/RECOVER_SC83_BRANCH.py), [full working archive](sandbox:/mnt/data/SC83_BRANCH_HANDOFF.zip), [expanded machine-readable handoff](sandbox:/mnt/data/RESULT_v2.json), and [cold-replay receipt](sandbox:/mnt/data/SC83_FINAL_VERIFIED/REPLAY_RECEIPT.json).
