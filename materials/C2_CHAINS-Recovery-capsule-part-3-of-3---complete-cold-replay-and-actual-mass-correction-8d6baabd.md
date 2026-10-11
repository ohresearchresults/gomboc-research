# material-8d6baabddd90

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C2_CHAINS: Recovery capsule part 3 of 3

## Exact object identity and evidence boundary

This completes recovery of the FOUR literal exact polyhedra and their full exact audits, not recovery of their original floating-point nomination search. Required complete earlier parts:

1. `[internal-source-reference]`, save its exact text as `recover_c2_inputs.py`, 7129 bytes, SHA-256 ae3d1acd2f286fd8ebc92d15e463bb0f8a68f82eb48d9f8bce07161e0029e3be.
2. `[internal-source-reference]`, save its exact text as `exact_c2.py`, 11240 bytes, SHA-256 7d76776bac625c37d356814813e8bcf28fbe8c8858ec1d02d6fcda55a52f8b49.
3. Save the complete code block below as `replay_c2.py`.

The earlier part-1 docstring anticipated nomination methods in part 3. Those original numerical producer/checkpoint source units were not preserved in the available exact materials. This part explicitly does NOT invent or reconstruct their historical search. Literal integer coordinate rows in part 1 are authoritative and are sufficient to reconstruct all four exact bodies. The new coordinator's later numerical methods are different source units, not a replay or alias of that missing old search.

All four are useful nonrecords, NOT strict110: RECT75 G6 and G3 are strict312; MASS75 G6 is strict716; DROP41 G3 is strict(3,15,16). Each has additional weak000 and primitive zero000. CPython3.13.5 standard library only; no numerical dependency is needed for exact recovery/auditing. The full supporting-triple hull, maximal polygons, true edges, actual filled-volume centroid, two-origin mass equality, S and independent face-foot tests, U tests, full mixed-edge H tests, simultaneous-equal-level P/Q landscapes and prescribed physical chain are reconstructed by part 2. This is one complete exact auditor with internal geometric/mass cross-checks, not two independently written full auditors.

## Correction of archived prose by the literal exact source

All eight input/audit byte counts and SHA-256 values below were observed again by cold replay. The earlier archived coordinator prose assigned incorrect small axial-centroid values to the RECT bodies. Their actual centroids are NOT near zero. Correct exact values and complete labels are asserted or generated below; do not substitute old prose approximations or labels.

RECT75_G6: V/E/F/C=75/218/145/436, volume 26507786068363523/120000000000000000, centroid (0,251704614026438023764917/1325389303418176150000000,0), axial coordinate approximately .1899099482524058. Strict S=[37,90,144], U=[70], H=[[71,72],[73,74]]. Q has two bars: the main peak90/elder37 bar has relative (birth-death)/death approximately13.521428388828355, component63/cut65; base144/elder37 has relative approximately.00014091372427395144, component1/cut4. P is empty.

RECT75_G3: same V/E/F/C and strict312, volume331330813/1500000000, centroid (0,62984179381/331330813000,0), axial coordinate approximately.19009454270406176. Strict S=[36,88,144], U=[70], H=[[71,72],[73,74]]. Main Q peak88/elder36 has relative approximately13.56490494377385, component63/cut65; base144/elder36 relative approximately.00012250460950606582, component1/cut4. P is empty. This low-arithmetic exact U1 body uses only integer-thousandth coordinates.

MASS75_G6: V/E/F/C=75/218/145/436, strict716, volume1733948372228521349/1500000000000000000, centroid (0,-648696605966673477/6935793488914085396000000,0), axial coordinate approximately-9.352882363114271e-8. Strict S=[4,11,45,65,75,104,144], U=[70], H=[[0,51],[1,53],[2,54],[16,35],[18,36],[19,37]]. Six Q bars and P empty; the two large Q bars have peak104/elder45 relative approximately1.4065562010804638, component42/cut44, and peak144/elder45 relative approximately.9445036415673351, component45/cut36. The other four bars have relative approximately.00166430359471027 twice and .0003864393433048002 twice. A near-zero actual centroid does not imply the stable landscape has been solved.

DROP41_G3: V/E/F/C=41/116/77/232, strict(3,15,16), volume1026629/4687500, centroid (0,249186035739/1314085120000,0). Its shortened prescribed chain is NOT all physically positive; removing every other chain point created fourteen additional physical basins. This finite failed shortcut is not a universal lower-complexity exclusion.

## Full reconstruction and verification command

Run in a clean directory containing the three source files:

`python -B -S replay_c2.py`

Expected final markers:

`C2_FOUR_LITERAL_BODIES_EIGHT_BYTE_MATCHES_PASS`

`C2_ACTUAL_CENTROID_CORRECTION_PASS`

The exact auditor also prints `EXACT_C2_CONSTRUCTION_AUDIT_PASS` once for each body. The following driver is 2623 bytes, SHA-256 e77bc9f64ad769da1765fedee323dd25dc55551f5bf94027cb00728123eae0a0. Its code block includes one final newline.

```python
"""Complete cold replay of the four literal C2 polyhedra, not their lost scout.
Dependencies: recover_c2_inputs.py and exact_c2.py, supplied without changes.
Python3.13.5 standard library. Run: python -B -S replay_c2.py
"""
import hashlib,json,subprocess,sys
from pathlib import Path
from fractions import Fraction
SOURCES={
'recover_c2_inputs.py':(7129,'ae3d1acd2f286fd8ebc92d15e463bb0f8a68f82eb48d9f8bce07161e0029e3be'),
'exact_c2.py':(11240,'7d76776bac625c37d356814813e8bcf28fbe8c8858ec1d02d6fcda55a52f8b49')}
EXPECTED={
'C2_RECT75_G6_312':([75,218,145,436],[3,1,2],'251704614026438023764917/1325389303418176150000000'),
'C2_RECT75_G3_312':([75,218,145,436],[3,1,2],'62984179381/331330813000'),
'C2_MASS75_G6_716':([75,218,145,436],[7,1,6],'-648696605966673477/6935793488914085396000000'),
'C2_DROP41_G3_CONTROL':([41,116,77,232],[3,15,16],'249186035739/1314085120000')}
def receipt(p):
    b=Path(p).read_bytes();return len(b),hashlib.sha256(b).hexdigest()
def main():
    for name,r in SOURCES.items():assert receipt(name)==r,(name,receipt(name),r)
    import recover_c2_inputs as inputs
    inputs.main()
    summary={}
    for name,(vefc,suh,cy) in EXPECTED.items():
        src=name+'.json';dst=name+'.audit.json'
        subprocess.run([sys.executable,'-B','-S','exact_c2.py',src,dst],check=True)
        for p in (src,dst):assert list(receipt(p))==inputs.RECEIPTS[p],p
        d=json.loads(Path(dst).read_text())
        assert [d[k] for k in ('V','E','F','C')]==vefc
        assert [len(d['strict'][k]) for k in ('S','U','H')]==suh
        assert d['actual_centroid']==['0',cy,'0']
        assert not any(d['additional_weak'].values())
        assert not any(d['primitive_zero_counts'].values())
        summary[name]={k:d[k] for k in ('V','E','F','C','actual_volume','actual_centroid','strict','additional_weak','primitive_zero_counts')}
        summary[name]['P_bars']=len(d['physical_landscape']['bars'])
        summary[name]['Q_bars']=[{k:b[k] for k in ('peak','elder','birth','death','relative','component','cut','path','death_edges')} for b in d['polar_landscape']['bars']]
        summary[name]['physical_chain_positive']=d['tree']['all_actual_positive']
        summary[name]['axis_interval_raw']=d['tree']['axis_interval_raw']
        summary[name]['minimum_positive_cosine_squared']=d['tree']['minimum_positive_cosine_squared']
    p=Path('C2_FOUR_EXACT_SUMMARY.json');p.write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(p.name,*receipt(p))
    print('C2_FOUR_LITERAL_BODIES_EIGHT_BYTE_MATCHES_PASS')
    print('C2_ACTUAL_CENTROID_CORRECTION_PASS')
if __name__=='__main__':main()
```

## Observed exact output receipts

C2_RECT75_G6_312.json 4949 bytes SHA1868b33e6c846399ae3d9e23076326c47c59a39d7659b8d92103f10de4b01a2c.
C2_RECT75_G6_312.audit.json 149008 bytes SHA89fcd0a18e2682d609f73af019578f5ecf187ff853a60b8c3761aebdf1ae3264.
C2_RECT75_G3_312.json 4284 bytes SHA3f7312457cc67ae144d6c3980f0e1e679b3a75a7b182825bbb3cc4dd23c66985.
C2_RECT75_G3_312.audit.json 105226 bytes SHA64d2f776e3405fd2bed97c114787f8cf437fbcd3adb22c71c221873872b9afb9.
C2_MASS75_G6_716.json 4965 bytes SHA5c239abaa67f0d158f0be23b3d14d0fae4da8f76b5426cc2bc789ba694d0677e.
C2_MASS75_G6_716.audit.json 157547 bytes SHA01d5d79ef98595f01ed913968a93301d1c3ddd6cd2980fd54b2959c5663c4072.
C2_DROP41_G3_CONTROL.json 2460 bytes SHAb0928f0c86d7fd830484430b23a7ef0ef10816cf56e7cb02c976febd87eef197.
C2_DROP41_G3_CONTROL.audit.json 71304 bytes SHAca8b69fcca2786f9ab43422a3b375161b102c5bb3fda277851b23dc82e6aa1d6.
C2_FOUR_EXACT_SUMMARY.json 34774 bytes SHAffc510ebc24920ab9ecc79d7309cfe37d2b450352c46ec0ec6b2bb5839d5c302.

The last summary contains exact volume/centroid, all equilibrium labels and each full remaining Q component, cut, attaining path and death-edge set. Full audits additionally contain the complete maximal incidence and physical landscape. No coordinate, incidence, precision rule or input array is omitted from the complete three-part recovery.
