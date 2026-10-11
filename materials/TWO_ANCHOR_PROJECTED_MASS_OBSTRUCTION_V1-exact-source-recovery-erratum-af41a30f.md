# material-af41a30f6e09

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1 — exact source recovery erratum

The analytic proof and every mathematical result in [internal-source-reference] (17871 bytes, SHA04208701b3956e834908a02b2ffacbc4a05ce01be9e36a1535905bf5fdc2df72) stand unchanged. Its literal code block accidentally includes ONE redundant assignment to R, immediately overwritten by the correct assignment. Thus that block computes the same audit but does not itself have the claimed source-byte count/hash. The claimed 6994-byte hash belongs to the originally executed code WITHOUT the redundant assignment. The exact extraction below removes precisely that line and recovers the audited source; it does not alter any executed geometry or result.

For reproducibility, BOTH this erratum and [internal-source-reference] are required exact inputs. Save the latter's complete literal text, unchanged, as captured_proof.md. Save the following entire code as recover_two_anchor_projected_mass.py, UTF-8/LF with final LF: 922 bytes SHA8a87ebff1b0169d21c4b4a28d51710b1262087f11c7b108be3118952b5dcf4c2. It uses only Python standard library; assertions must be enabled.

Commands:
python -S recover_two_anchor_projected_mass.py captured_proof.md recovered
python -S recovered/two_anchor_projected_mass.py build
python -S recovered/two_anchor_projected_mass.py check

The restored source must be6994bytes SHAb442f91e1b84ce96d6027e18eac10b8cb734ceed73de334573b701f5918f3b2a. Its output recovered/two_anchor_projected_mass.json must be1829bytes SHA09c44fa2fe723be1579483f52fd4471318c448b04abc6f2d6b8d4e6e8d0f21d1. Source build/check were executed on CPython3.13.5. The extraction is an exact byte correction, not independent verification of the analytic theorem.

Expected markers:
PROJECTED_MASS_AUDITED_SOURCE_RECONSTRUCTED 6994
ACTUAL_TWO_ANCHOR_PROJECTED_MOMENT_IDENTITIES_PASS 6 9 5
ACTUAL_NEGATIVE_CORE_AND_POSITIVE_COMPLEMENT_MOMENTS_PASS
FORMAL_51_OVER_25_ALL_RHO_AND_COVARIANCE_EXCLUSION_PASS
TWO_ANCHOR_PROJECTED_MASS_RECOVERY_PASS

```python
"""Recover the audited source from the immutable proof capsule with its erratum.
Usage: python -S recover_two_anchor_projected_mass.py CAPTURED_PROOF.md OUTDIR
"""
from pathlib import Path
import hashlib, sys
assert __debug__
assert len(sys.argv)==3
raw=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()=='04208701b3956e834908a02b2ffacbc4a05ce01be9e36a1535905bf5fdc2df72'
text=raw.decode('utf-8')
code=text.split('```python\n',1)[1].split('```',1)[0]
bad='    R=((F(1),F(0)),(F(6,5),F(0)),(F(0),F(6,5)),(F(1),F(0)))\n'
assert code.count(bad)==1
code=code.replace(bad,'',1)
out=code.encode('utf-8')
assert len(out)==6994
assert hashlib.sha256(out).hexdigest()=='b442f91e1b84ce96d6027e18eac10b8cb734ceed73de334573b701f5918f3b2a'
dest=Path(sys.argv[2]);dest.mkdir(parents=True,exist_ok=True)
(dest/'two_anchor_projected_mass.py').write_bytes(out)
print('PROJECTED_MASS_AUDITED_SOURCE_RECONSTRUCTED 6994')
```
