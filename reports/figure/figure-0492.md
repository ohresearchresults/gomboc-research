# figure-0492

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SC83 closeout — unchanged C144/C168 geometry, with corrected parent mass and receipt statements

## Disposition

**No new strict110 endpoint, changed polyhedron, or new exclusion theorem is claimed.** No post-parent construction checkpoint or trial ledger was recovered from the interrupted continuation. This is an execution limitation, not a failed finite search and not evidence against the C144 geometry direction.

The closeout does establish a continuation-critical correction: several printed numerical values, one exact volume/centroid statement, and two output hashes in the literal parent disagree with its own exact input arrays and executable recovery capsule. Fresh exact reconstruction reproduces the capsule's17 output receipts. An additional direct integer-grid mass calculation independently confirms the corrected C168 G6 mass. The bodies, equilibrium classes, complete interfaces and previously certified theorem scopes remain unchanged.

## 1. Authority, reading and recovered state

The authoritative parent remains `figure-0489`, advertised immutable SHA-256 `e6a19ac86845ee6ab03a97e53cea4c2752cb60a451665f116cdad2b621f66f41`. The latest journal and its complete literal parent were read through EOF; unchanged earlier context was not treated as a missing external archive.

The mounted latest journal is272513 bytes, SHA-256 `69bf426fa69c4b397abfd18726efecc275612617b475448e3293b8f24ccee9ef`. Its parent capsule decodes to the advertised22-file dictionary,89447 bytes, SHA-256 `19cfd3720ac7dd6bf1c34bd840ca3aaf017ea0d6a0d570b9b51a70596dfd0d4b`.

The recovered runtime contained the supplied archives, decoders and journals, but no independently recoverable construction state from the interrupted assignment. I therefore did not infer optimization counts, geometric advances or negative results from the elapsed interval.

The printed30 G6 point rows and26 C144 support rows agree with the encoded exact inputs. **The conflicts are within the parent's prose versus its literal data and executable receipts; no substitute geometry has been introduced.**

## 2. Corrections that must accompany the parent

### C168 G6 actual uniform mass

For unchanged `SC83_QCAP_TQ30_C168_211_G6`, the parent prints volume `6056987155808159273/1500000000000000000` and a corresponding centroid tuple. Those statements are not the mass of its literal30-point input.

The corrected exact raw volume is

`6056987155826002477/1500000000000000000`.

The corrected exact raw filled centroid is

```text
(39737364266268393840485085,
 21071944156836071809501343,
 -20764825741110313463537922)
/96911794493216039632000000.
```

The exact raw first moment is

```text
(2649157617751226256032339/1600000000000000000000000,
 21071944156836071809501343/24000000000000000000000000,
 -3460804290185052243922987/4000000000000000000000000).
```

These values agree exactly between the inherited H-body auditor and a new direct supporting-V-triple calculation. For integer points divided by D, the latter exhausts all supporting triples, verifies that each maximal facet has exactly three vertices, orients them outward, and computes

`V=sum det(a,b,c)/(6D^3)`,

`M=sum det(a,b,c)*(a+b+c)/(24D^4)`.

It finds56 maximal triangular facets. Thus the correction does not depend on floating hull tolerances or numerical integration. The complete runnable check is included in the recovery capsule.

### Two corrected quality brackets

The parent's G6 inradius/circumradius bracket and G4 birth-relative Q-depth bracket are also inconsistent with the exact report generated from those inputs. The correct brackets are:

| Quantity | Correct exact enclosing interval |
|---|---|
| G6 `r/R` | `[174314374449,174314374450)/10^12` |
| G4 strict211 `(Qbirth-Qdeath)/Qbirth` | `[898848775045,898848775046)/10^12` |

The G6 relative Q-depth interval `[814444608638,814444608639)/10^12` and TQ interval `[9420445292610,9420445292611)/10^12` remain correct. The qualitative comparison survives: G6 has the smaller relative Q depth, but it is still a substantial remaining basin, not a near110 certificate.

### Two corrected output hashes

The parent's §7 prints incorrect hashes for the point-cell report and840-matrix bank. Its encoded expected-output manifest, supplied archived outputs and fresh exact replay instead agree on:

| Exact output | Bytes | Correct SHA-256 |
|---|---:|---|
| `SC83_BERNSTEIN_840.json` |18864051|`b28ea8f99557624ce97bf7ac06dc9c0cbc696d0c13b24393d8f9a9362f6d0210`|
| `SC83_FULL_VISIBILITY_BLOCK.json` |26755|`3eb61c3a5f7cce8df04059afeaea45e32a7dbc7c29711f9af0732e415661b191`|

The incorrect prose hashes were respectively `b28e372c18b32372c1e08b3f44c9a3b3539a5661a18012ce12dbb54a2d8b7936` and `3ebc619d29770e5601cf0b8c9163a2ca262ee636f741eb6b7a19e64480147416`. The exact coefficient checks themselves pass; this is not a retraction or enlargement of the theorem.

## 3. Exact constructions preserved, not newly produced

Fresh reconstruction confirms all four parent bodies:

| Exact identity | V/E/F; C | Strict S/U/H | Additional weak | Primitive zeros | Centred denominator bits |
|---|---|---|---|---|---:|
| `SC83_DUALBRIDGE26_C144_121_N4` |48/72/26;144|1/2/1|000|000|3292|
| `SC83_QCAP_BRIDGE30_C168_413_G4` |30/84/56;168|4/1/3|000|000|60|
| `SC83_QCAP_REPAIR30_C168_211_G4` |30/84/56;168|2/1/1|000|000|60|
| `SC83_QCAP_TQ30_C168_211_G6` |30/84/56;168|2/1/1|000|000|87|

These are the parent's constructions, not four new outcomes of the interrupted assignment. Their original identities and complete interfaces are preserved.

### Primary S1-first continuation checkpoint

`SC83_DUALBRIDGE26_C144_121_N4` still has `S=[19]`, `U=[1,47]`, `H=[[19,24]]`. Its uniformly filled raw volume is approximately0.8574312389814415 and centroid approximately `(0.28333756476025906,0.17255952687330514,-0.18310583239248188)`; the full exact rationals are regenerated by the capsule, not replaced by these decimals.

Its entire defining raw H input, with each row meaning `n.x<=h`, is:

```json
[[-18972,22423,5249,10000],[-15795,6476,-17742,10000],[-9127,25175,18766,10000],[-7820,22499,4081,10000],[-7710,94,-4953,10000],[-6135,19585,-1794,10000],[-5825,928,-10157,5000],[-5381,-6085,-22395,10000],[-5300,5948,-15599,10000],[-5028,-3355,-3530,10000],[-4739,-3547,-3020,10000],[-4121,12013,5047,5000],[-3581,21819,8878,10000],[-1356,21675,25796,10000],[1742,-10441,-10645,5000],[3836,17363,29481,10000],[5547,15634,32500,10000],[6306,2637,18901,5000],[7427,12399,36238,10000],[10848,-21709,-2402,5000],[15369,489,37585,10000],[17417,-3931,37244,10000],[19461,-8947,35974,10000],[19825,-36200,-1118,10000],[22249,-16868,31813,10000],[24599,-28355,21826,10000]]
```

Its complete surviving topology is:

```json
{"P":{"roots":[1,47],"bars":[{"peak":1,"elder":47,"death_edge":[19,24],"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23],"boundary":[[1,42],[8,43],[9,36],[10,40],[11,36],[13,32],[14,20],[15,25],[16,26],[16,34],[17,29],[18,35],[18,39],[19,21],[19,24],[23,30],[23,32]],"path":[1,0,2,3,4,19,24,45,46,47]}]},"Q":{"roots":[19],"bars":[]}}
```

The physical packet remains21/17, not canceled. Exact TP is in `[7008800394369,7008800394370)/10^12`, with177 final-edge units of headroom under E<=249.

### C168 G6 alternative interface

After applying the corrected own centroid, the unchanged G6 body still has `S=[21,55]`, `U=[29]`, `H=[[16,24]]`. Its complete residual interface is:

```json
{"P":{"roots":[29],"bars":[]},"Q":{"roots":[21,55],"bars":[{"peak":21,"elder":55,"death_edge":[5,42],"component":[0,1,2,3,5,8,9,10,11,12,13,14,16,18,20,21,24,27,29,31,32,36],"boundary":[[1,53],[2,55],[5,42],[8,43],[10,37],[11,33],[12,45],[14,28],[20,44],[21,50],[24,23],[24,38],[27,48],[27,54],[31,45],[31,51],[32,15],[32,46]],"path":[21,18,36,5,42,39,41,52,47,55]}]}}
```

All30 literal point rows, and the complete inputs and P/Q reports of both G4 alternatives, are included in the inline capsule below.

## 4. What was actually checked, and what remains open

The parent17-output exact replay completed in the recovered directory and again in a fresh directory populated solely by the new inline capsule. Checks include the four maximal complexes, actual volume and first moment, full stable/unstable and mixed-edge strict/weak predicates, primitive zeros, and both landscapes about the actual physical centroid.

The entire old C176 visibility-cell theorem was also replayed: closure6/9/5, actual affine-volume/quadratic-moment chart, protected sets `{2}` and `{54,56,58,59,60}`, and840 exact coefficient matrices proving two strict U throughout the specified point cell and entrywise Gram neighbourhood31/500. This remains a **local-metric theorem on that fixed-outside material chart**, not an exclusion of C144 or C168.

The positive local Gram cells on the two C168 strict211 bodies also replay:

| Body | U1-only entrywise radius | S/U-count radius | Full primitive-sign radius |
|---|---:|---:|---:|
| G4 |1/4096|1/8192|1/8192|
| G6 |1/2048|1/524288|1/1048576|

These are feasible neighbourhoods, not global affine exclusions. The earlier fixed-C180677-blocker all-SPD proof is inherited and was **not** re-executed in this closeout.

Evidence tier remains one full mechanical auditor with its exact mass identities. The new direct V-triple check is an additional independent mass calculation for G6, **not a second independent full mechanics audit**.

The next unresolved construction is still the C144 whole-P21/17 problem with rebuilt actual mass and S1 recovery. A concrete finite first test is exact packet/complement separability. Because the parent is simple and the packet has cycle rank `(21-17+2)/2=3`, a successful strict one-cap removal would conditionally give V44/E66/F24,C132 before the new mass/mechanics audit. **No such separator has been tested or certified here.** This conditional count is not a cap construction, a cancellation result or a statement that one cap suffices mechanically. Coordinated retained-support motion and transferred packets remain legitimate alternatives.

## 5. Self-contained corrected recovery

The capsule contains10 complete source/input units: the literal parent geometry/auditor, all four exact material inputs, exact freezing/hull/report methods, the visibility-cell generator, Gram-cell checker, parent17-output manifest and replay driver, plus the new correction checker. It omits unused numerical nomination producers; no new numerical campaign is claimed.

Save the following decoder as `RECOVER_SC83_CLOSEOUT.py` and run with **CPython3.13.5 standard library only**, assertions enabled:

```sh
python -B -S RECOVER_SC83_CLOSEOUT.py SC83_CLOSEOUT
cd SC83_CLOSEOUT
python -B -S REPLAY_SC83_FINITE.py
python -B -S CHECK_SC83_PROSE_CORRECTIONS.py
```

Expected decisive markers:

```text
SC83_FULL_POINT_VISIBILITY_CELL_PASS 6 9 5
SC83_POINT_CHART_ACTUAL_MASS_CHECK_PASS 52 88 38
SC83_TWO_PROTECTED_BASINS_840_COEFFICIENTS_PASS
SC83_FULL_VISIBILITY_GRAM_BOX_EXCLUSION_PASS 31/500
SC83_FINITE_SEVENTEEN_OUTPUT_HASHES_PASS 17
SC83_ACTUAL_MASS_C168_211_C144_121_AND_FULL_POINT_CELL_HANDOFF_PASS
SC83_INDEPENDENT_GRID_MASS_CORRECTION_PASS
SC83_PROSE_CORRECTIONS_EXACT_PASS 1484 8bb3abe2ee4998149c255429edf5bfee24395b5fa726de4cbeb1860e03513610
SC83_UNCHANGED_PARENT_RECOVERY_NOT_NEW_GEOMETRY_PASS
```

The ten-file source dictionary is44966 bytes, SHA-256 `71602a1e745f5fdced5f583707971b68b02e38f8cf88f5ae46f871e989bcd9ed`; XZ15328 bytes, SHA-256 `0d0fc6196157623cd357b6b4f95070155426513dbd72ec92b0bd36efbea5c571`; base6420440 nonwhitespace characters.

The new complete checker is3435 bytes, SHA-256 `15c6c0af6e9b9ad741b3709f5edc06bece2f0e6d766e9bc095b4ffa963557642`. Its exact correction report is1484 bytes, SHA-256 `8bb3abe2ee4998149c255429edf5bfee24395b5fa726de4cbeb1860e03513610`.

Selected unchanged-body receipts:

| Output | Bytes | SHA-256 |
|---|---:|---|
| C144 exact H input |675|`03d9d814fd9447056cda705853720e5a82c63fcfba23314c1e6bd3fe6118369d`|
| C144 full audit |67416|`b80e4c527209d4df3b8618e9a8bebb4079374ffb77db6874cf9a85e43dd96992`|
| G6 full audit |22912|`e873f1de76133c49cbac96a82051edfff0dd4e10eb16976a29f4979d2e8cb3e5`|
| Four-body material report |28678|`e44ef22e320bb355ab4832a3336041b4b2e68f8f02fc0dc888637a8113e4d6e1`|

Convenience copies, not recovery dependencies: source/audit bundle (`SC83_CLOSEOUT_RECOVERY.zip`) and decoder (`RECOVER_SC83_CLOSEOUT.py`).

```python
import base64,hashlib,json,lzma,pathlib,sys
B64='''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'''
z=base64.b64decode(B64)
assert len(z)==15328 and hashlib.sha256(z).hexdigest()=='0d0fc6196157623cd357b6b4f95070155426513dbd72ec92b0bd36efbea5c571'
b=lzma.decompress(z)
assert len(b)==44966 and hashlib.sha256(b).hexdigest()=='71602a1e745f5fdced5f583707971b68b02e38f8cf88f5ae46f871e989bcd9ed'
files=json.loads(b);assert len(files)==10
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'SC83_CLOSEOUT');out.mkdir(parents=True,exist_ok=True)
for name,text in sorted(files.items()):
 assert pathlib.Path(name).name==name
 x=text.encode('utf-8');(out/name).write_bytes(x)
 print('SC83_SOURCE',name,len(x),hashlib.sha256(x).hexdigest())
print('SC83_CLOSEOUT_SOURCE_RECOVERY_PASS',len(files),len(b),hashlib.sha256(b).hexdigest())
```
