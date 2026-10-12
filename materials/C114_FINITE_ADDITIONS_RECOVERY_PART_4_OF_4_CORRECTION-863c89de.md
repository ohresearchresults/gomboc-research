# material-863c89de8c24

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C114_FINITE_ADDITIONS — Recovery capsule part 4/4 — required extraction-header correction

The complete canonical recovery set now has FOUR ordered parts, superseding the three-part count printed in parts1–3: (1) [internal-source-reference], (2) [internal-source-reference], (3) [internal-source-reference], (4) this correction. The numerical/exact source units, literal bodies and scientific results are unchanged.

Part3's @@FILE MANIFEST.json header was incorrectly transcribed as 3498 bytes and SHA1527c44f1c60317d9680b54a153eb190871e7be3db69d0eb8106b5b4f8079be8. Neither value was measured and neither is authoritative. The COMPLETE literal MANIFEST.json content following that header is unchanged: its actual measured size is **2923 bytes**, SHA256 **43c0997f9ae32a4bf959bf7498342bafaddc4dfb69949817f665f4b4f64810ea**. The original decoder would fail on that header. This complete replacement decoder corrects ONLY that explicitly identified header and still checks the actual source bytes against the correct digest. No output hash, body coordinate, precision rule or mathematical predicate changes.

Save the program below as RECOVER_FIXED.py. Run `python -B -S RECOVER_FIXED.py part1.md part2.md part3.md`, then `cd recovered && python -B -S REPLAY.py`. Read and retain part4 with the other three materials. All eight literal source files and all14 reproduced output hashes remain those in the literal MANIFEST.json. This is a transport recovery correction, not independent mathematical verification.

```python
from pathlib import Path
import sys,re,hashlib
out=Path('recovered');out.mkdir(exist_ok=True)
seen=set()
for arg in sys.argv[1:]:
 b=Path(arg).read_bytes()
 for m in re.finditer(rb'^@@FILE ([A-Za-z0-9_.-]+) ([0-9]+) ([a-f0-9]{64})\n',b,re.M):
  name=m[1].decode();n=int(m[2]);sha=m[3].decode()
  if name=='MANIFEST.json':
   assert n==3498 and sha=='1527c44f1c60317d9680b54a153eb190871e7be3db69d0eb8106b5b4f8079be8'
   n=2923;sha='43c0997f9ae32a4bf959bf7498342bafaddc4dfb69949817f665f4b4f64810ea'
  data=b[m.end():m.end()+n]
  assert len(data)==n and hashlib.sha256(data).hexdigest()==sha,name
  assert name not in seen;seen.add(name);(out/name).write_bytes(data)
assert seen=={'cap_search.py','centered_caps.py','exact_addition.py','exact_landscape.py','INPUTS.json','CAMPAIGN.json','REPLAY.py','MANIFEST.json'},seen
print('C114_ADDITION_EIGHT_SOURCE_UNITS_RECOVERED_WITH_HEADER_FIX')
```
