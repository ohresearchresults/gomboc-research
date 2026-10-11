# material-c08d19ff6b97

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Mandatory literal recovery repair for the J99 frozen numerical capsule

Material [internal-source-reference] contains one coordinator transcription error in J99_JOINT_0_FROZEN.json: new_points_raw[3][1] was copied as0.47735336514614625276. The originating frozen float literal is0.47735336514625276. The centred point array, all scientific computations, the original source manifest and the reported output hashes are unchanged. Cases2 and6 are unaffected. This is a byte-recovery correction, not a change to the computed body. Apply this complete standard-library patch AFTER extracting the FILE fences and BEFORE nominate_frozen99.py. The correct full case0 file has1982 bytes and SHA-2569d54a6296d07bc5770920435d44dcadd337a95f6e6a289702fb6d4787cb80371.

Save as repair_frozen_case0.py and run `python repair_frozen_case0.py`. It accepts either the exact uncorrected copied literal or the already-correct file; any other corruption fails the final complete-file hash.

```python
from pathlib import Path
import hashlib
p=Path('J99_JOINT_0_FROZEN.json')
s=p.read_bytes()
bad=b'0.47735336514614625276'
good=b'0.47735336514625276'
assert s.count(bad) in (0,1)
s=s.replace(bad,good)
assert len(s)==1982
assert hashlib.sha256(s).hexdigest()=='9d54a6296d07bc5770920435d44dcadd337a95f6e6a289702fb6d4787cb80371'
p.write_bytes(s)
print('J99_FROZEN_CASE0_LITERAL_REPAIR_PASS')
```

The complete numerical recovery dependency set is exact input [internal-source-reference], methods [internal-source-reference], frozen endpoints [internal-source-reference] AND this repair. The exact C464 source-only construction needs only [internal-source-reference] and is unaffected.
