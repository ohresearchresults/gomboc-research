# material-cf598be542b3

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_NONLOCAL_SEVEN_EXACT_NONWINNERS_V1 — Recovery capsule part 1/2

BOTH parts are required, in order. This complete source capsule preserves seven uniformly filled exact nonwinners and every materially used numerical production method. It does not replace the canonical C622 own110 record. The complete literal RL04 scientific parent source is included; parent immutable result figure-0395 was read fully. Two C156 own121 deletions and two C384 own312 arc bodies establish new exact continuation objects, not solutions. Other exact samples are C270 own367, C218 own233 and C138 own334. All seven have weak000. The 16-file source dictionary contains the full exact inputs, independent A/B and third-mass checks, binary64 hexadecimal checkpoints, strict rounding rules, complete numerical methods/parameters, precise finite-search/timeout limitations and expected output hashes. Its README distinguishes fixed-reference and actual homogeneous mass throughout.

Reconstruction: save the complete RECOVER_NONLOCAL_SPLIT.py from part1 and run `python -B -S RECOVER_NONLOCAL_SPLIT.py NEW_SOURCE NEW_PROOF PART1.md PART2.md`. Verification: `python -B -S NEW_SOURCE/REPLAY.py FRESH_PROOF`. Both commands were cold-tested. Expected terminal: `COORD_NONLOCAL_SEVEN_EXACT_NONWINNERS_COLD_REPLAY_ALL_PASS`, then `NO_NEW_OWN110_RECORD_CANONICAL_C622_UNCHANGED`. Exact replay needs CPython3.13.5 standard library only. Numerical search methods, not needed for replay, state their exact NumPy2.3.5/SciPy1.17.0/PyTorch2.10.0+cpu dependencies and all non-default parameters.

## Complete decoder

```python
#!/usr/bin/env python3
"""Join both immutable parts, reconstruct complete sources, and replay all seven bodies."""
from pathlib import Path
import re,sys,base64,lzma,json,hashlib,subprocess
assert __debug__
assert len(sys.argv)==5,'Usage: RECOVER_NONLOCAL_SPLIT.py NEW_SOURCE NEW_PROOF PART1.md PART2.md'
sha=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for i,name in enumerate(sys.argv[3:],1):
 text=Path(name).read_text()
 match=re.search(r'^BEGIN_NONLOCAL_PART_'+str(i)+r'\n(.*?)\nEND_NONLOCAL_PART_'+str(i)+r'$',text,re.M|re.S)
 assert match,name
 parts.append(''.join(match.group(1).split()))
encoded=''.join(parts).encode()
assert len(encoded)==32988 and sha(encoded)=='72befe34105c5ecfb6ae08faa1ed210d40fb10ba8aa005e893b33ad3727144cc'
raw=base64.b64decode(encoded,validate=True)
assert len(raw)==24740 and sha(raw)=='0eed2f23114b656cc8d5a2d2d88928fe5350b8ce938b9e695c4e9bcb21fde35c'
raw=lzma.decompress(raw)
assert len(raw)==74091 and sha(raw)=='3381617cb98f179806c21f5105046585c7899dc9d521fa68b653726bc626753b'
files=json.loads(raw);out=Path(sys.argv[1]).resolve();out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 p=out/name;assert out in p.resolve().parents
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
for name,want in json.loads(files['MANIFEST.json']).items():
 b=(out/name).read_bytes();assert len(b)==want['bytes'] and sha(b)==want['sha256'],name
print('NONLOCAL_LITERAL_SOURCE_MANIFEST_PASS',len(files),flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),str(Path(sys.argv[2]).resolve())],check=True)
```

## Literal payload fragment

BEGIN_NONLOCAL_PART_1

[Encoded source block omitted; the code in this passage is incomplete.]
