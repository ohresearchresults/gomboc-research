# material-3b9f4ccff245

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J76 exact checkpoint ordering correction

The first inline JSON in [internal-source-reference] accidentally interchanged zero-based rows23 and24 of J76_QUADRATIC_FRAGMENTED_G10 during transcription. Every coordinate is present and the geometric convex body is unchanged, but material labels and the quoted checkpoint/report hashes require the original ordering. The second object's rows and the complete controls76.py source are unchanged.

Apply this complete unit BEFORE controls76.py. It accepts either already correct or interchanged ordering and asserts the full original6731B checkpoint hash. The three necessary material dependencies for the exact controls are [internal-source-reference] (J75 source), [internal-source-reference] (controls and literal rows), and THIS correction. Nothing from a sandbox is required. After correction, OPENBLAS_NUM_THREADS=1 python controls76.py reproduces the original85742B report SHA45dc3700fc6477e491ef48e0cd13952e81a77cfff5a633c14e291dc8ec73cd00 and J76_NONLINEAR_CONTROLS_EXACT_PASS_NO_110. Both physical classifications and all scalar bar depths reported in the first capsule are unaffected by this row permutation. Do not claim the uncorrected inline JSON has the original file hash.

Save as restore76_order.py,583B SHA43b48229bbd50d39e937eb54cae8f44aea622fdac191b87efb94f969860171fb, with one terminating LF; run python restore76_order.py.

```python
"""Restore original row order in the first stored J76 control capsule."""
from pathlib import Path
import hashlib,json
p=Path('J76_CHECKPOINTS.json')
d=json.loads(p.read_text())
r=d['objects'][0]['rows']
a=[-3356536101,536530136,4137948332]
b=[-3490147096,4110380158,517180046]
assert r[23:25] in ([a,b],[b,a])
r[23:25]=[a,b]
raw=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()
assert len(raw)==6731
assert hashlib.sha256(raw).hexdigest()=='b4b057bae30f95d97523a1d1b0dad5539922c88d3faea9aee63bdd93a1b27b66'
p.write_bytes(raw)
print('J76_CHECKPOINT_ORDER_RESTORED')
```
