# material-472b56ebb9d8

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Required correction for J85_DYNAMIC_A_G10 literal serialization

The G10 JSON block in material [internal-source-reference] contains a transcription error at zero-based material row5,z: -9675388900 instead of the actually executed -9675389004. No other integer is changed by this correction. The G8 literal input and the four expected executed report/cube hashes are unchanged. The erroneous G10 serialization has1705B/SHA29eb219bd2af4a61ac10a8af646a55044d01197ad028dd0407a3705e91f4fb82. It is NOT the audited G10 object; do not silently treat it as such. The corrected1705B input matches the intended immutable identity ec1c1f91d911177b4cd23e9d5e1fd6ea63303e7890bd4bc3c3e91572021331f2.

This complete patch is a REQUIRED dependency when extracting G10 from that material. It accepts either precisely the erroneous bytes or the already-correct bytes, and rejects any other serialization. Save as correct_dynamic_g10.py with final LF, run python correct_dynamic_g10.py BEFORE python replay_recovered85.py. This corrects preservation, not an optimization step, and does not change the independently retained exact input that was used for the observed computations. G8-based stellar descendants do not depend on G10 or this patch.

```python
"""Repair the one identified G10 publication typo, with complete byte guards."""
import hashlib,json
from pathlib import Path
p=Path(__file__).resolve().parent/'J85_DYNAMIC_A_G10_INPUT.json'
raw=p.read_bytes();old=hashlib.sha256(raw).hexdigest()
wrong='29eb219bd2af4a61ac10a8af646a55044d01197ad028dd0407a3705e91f4fb82'
right='ec1c1f91d911177b4cd23e9d5e1fd6ea63303e7890bd4bc3c3e91572021331f2'
assert old in (wrong,right),(len(raw),old)
j=json.loads(raw)
assert j['denominator']==10**10 and len(j['points'])==45
assert j['points'][5][:2]==[-8050067857,-2393414918]
assert j['points'][5][2] in (-9675388900,-9675389004)
j['points'][5][2]=-9675389004
fixed=(json.dumps(j,sort_keys=True,separators=(',',':'))+'\n').encode()
assert len(fixed)==1705 and hashlib.sha256(fixed).hexdigest()==right
p.write_bytes(fixed)
print('J85_DYNAMIC_G10_LITERAL_SERIALIZATION_CORRECTED',right)
```
