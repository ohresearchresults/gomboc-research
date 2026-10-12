# material-39a35bbe9ddd

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/2 — PROJECTIVE_ROOTED_TWO_NONWINNERS_RECOVERED_V1

BOTH parts required, in order. This complete scoped 19-file capsule recovers two exact rational projective images, not rounded physical snapshots: both V23/E63/F42,C126,own312,weak000; centered bit costs2664/2665 and2812/2814. Independent complete A/B hull, filled centroid and all-feature checks, plus centered positive tetrahedra/zero moments and exact rooted path/cut certificates. Also complete original numerical producer/config/checkpoints and derived rooted separation/projective-mass lemmas. No record improvement or whole-orbit exclusion. Canonical remains C622.

Source-only replay was executed after recovering this scoped dictionary. Final marker PROJECTIVE_ROOTED_TWO_EXACT_NONWINNERS_AND_LITERAL_LABELS_SOURCE_ONLY_PASS. Input and all generated output byte counts/SHA256 values are in the recovered MANIFEST.json and PROJECTIVE_EXACT_LEDGER.json. Part1 whitespace-stripped base64 has11692ASCII bytes SHA25674bc41b2cfc60fc26db2062c91a1723aa0cc9376df1fb0df65c2308d6d12b5f3; part2 has11692bytes SHA256db59f274bad282a3b2f48176f66cff5dddce24afe824c5b28f95a0b7846a4faf. Concatenated base6423384bytes SHA25660e1c977667d7a536e685a1862f6d70741d3a1758a3f171d81ec9d1a8b3188e1; XZ17536bytes SHA256be6e68a7765c669b9d514f0b4c0f85fafe6dfd30094433056652aa67a16e199a; JSON dictionary70922bytes SHA256e93a15506c6df4a486867cf05a12d6e13fed4d44256a9c359b14fb1fbd7c4cbb.

Save both materials as part1.md,part2.md. Save the following complete loader as RECOVER_PROJECTIVE_ROOTED.py,1507bytes SHA256fc40623704d7d38c8507f555bc43ee01d7e891d62c19b53a1b26e93b7de0fb11. Run `python -B -S RECOVER_PROJECTIVE_ROOTED.py part1.md part2.md recovered`, then `python -B -S recovered/REPLAY_STORED.py`. CPython3.13.5 stdlib suffices; no optimizer or missing sandbox needed. The source uses anchored fenced-block extraction, avoiding the old unanchored metadata regex bug. The original34-file Library manifest is retained as inventory; this material preserves the scoped19-file set, not nonexistent old V3/TERMINAL_RECEIPTS source.

```python
#!/usr/bin/env python3
import base64,hashlib,json,lzma,re,sys
from pathlib import Path
assert __debug__ and len(sys.argv)==4,'two material Markdown files and output directory required'
parts=[]
for fn in sys.argv[1:3]:
 blocks=re.findall(r'(?ms)^```text\n(.*?)^```[ \t]*$',Path(fn).read_text())
 assert len(blocks)==1
 parts.append(''.join(blocks[0].split()))
expected=['74bc41b2cfc60fc26db2062c91a1723aa0cc9376df1fb0df65c2308d6d12b5f3','db59f274bad282a3b2f48176f66cff5dddce24afe824c5b28f95a0b7846a4faf']
for k,p in enumerate(parts):assert len(p)==11692 and hashlib.sha256(p.encode()).hexdigest()==expected[k]
s=''.join(parts);assert hashlib.sha256(s.encode()).hexdigest()=='60e1c977667d7a536e685a1862f6d70741d3a1758a3f171d81ec9d1a8b3188e1'
z=base64.b64decode(s,validate=True);assert len(z)==17536 and hashlib.sha256(z).hexdigest()=='be6e68a7765c669b9d514f0b4c0f85fafe6dfd30094433056652aa67a16e199a'
b=lzma.decompress(z);assert len(b)==70922 and hashlib.sha256(b).hexdigest()=='e93a15506c6df4a486867cf05a12d6e13fed4d44256a9c359b14fb1fbd7c4cbb'
f=json.loads(b);assert len(f)==19
out=Path(sys.argv[3]);out.mkdir(exist_ok=True,parents=True)
for n,t in f.items():
 p=Path(n);assert not p.is_absolute() and '..' not in p.parts
 q=out/p;q.parent.mkdir(exist_ok=True,parents=True);q.write_bytes(t.encode())
for n,v in json.loads(f['MANIFEST.json']).items():
 d=(out/n).read_bytes();assert len(d)==v['bytes'] and hashlib.sha256(d).hexdigest()==v['sha256']
print('PROJECTIVE_ROOTED_NINETEEN_SOURCE_FILES_RECOVERED')
```


[Encoded source block omitted; the code in this passage is incomplete.]
