# material-e04cae85dad9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/4 - ROOTED_C620_CHECKPOINTS_V1

All FOUR ordered parts are one complete 50-file exact source, input and checkpoint unit. These are three C620 own121 nonwinners, NOT a record; canonical C622 own110 is unchanged. This part: 14000 base64 characters, SHA256 d125a0b567ada0139d9f75000f13f6a47e14492fa235f046dd751e1cc3e69085.

Required external dependencies: CONDITION25 ALL THREE materials [internal-source-reference], [internal-source-reference], [internal-source-reference]; and TWO_C620_CONTACTS [internal-source-reference]. Together they completely recover source/ and two_contact_cold/ with exact original seeds and independent auditing code. Do not omit any part or dependency.

Joined base64:55296chars SHA256d5bd4fe430e366d3824464bbbc4f9e37a058b304d33a0d115827d846ff0ae2e6. LZMA-decoded UTF8 dictionary:178935bytes SHA256ccdca06fd9b6dec3440e3bbc1b36e4bafe7a817ac1361bc61e92b0c241fc8879. All file bytes/hashes are in MANIFEST.json and exact output receipts are complete.

The frozen bodies rooted_69_rank0, rooted_174_rank0 and locked_69_rank0 all have V175/E310/F137,C620,strict121/weak000,primitivezero000,346positive centered tetrahedra and zero filled first moments. Their centered denominator bit lengths are57364,56827,57377. Free69 and locked69 have S3,U67/93,H67-72; free174 has S3,U94/171,H173-174. Independent complete A and B agree bytewise for all three. Exact receipt2759bytes SHA2562e729b2e16ea62be56774557c6aec92920f62bff5417dc4a345ad8485a3cf893.

Includes complete original rooted continuation, centroid-lock and affine-screen source; exact rounded generators; exact float.hex restart states; complete restart program; source/input manifests; exact replay driver. Four branch checkpoints lambda .1759765625,.0125,.1125,0 were explicitly stopped at a coordinator segment boundary, not optimizer terminal budgets. Next target lambdas .206494140625,.028125,.190625,.025. In-progress unaccepted iterates are not preserved; resume retries from last accepted states. Nonessential inner histories are reduced to completed-stage summaries. Both13-start affine screens completed with no winner; this is no affine-orbit exclusion. Numeric CPython3.13.5/NumPy2.3.5/SciPy1.17.0,OPENBLAS/OMP1thread; exact audits standard library only. Every nondefault parameter and input dependency is literal or deterministically regenerated and hash-checked by complete code.

Save the Python block as RECOVER_ROOTED_JOIN.py. Run `python -B -S RECOVER_ROOTED_JOIN.py part1.md part2.md part3.md part4.md rooted_capsule`. Expected ROOTED_C620_COMPLETE_SOURCE_CHECKPOINT_UNIT_RECOVERED 50. Then `python -B rooted_capsule/REPLAY_ROOTED_CAPSULE.py --source source --seeds two_contact_cold --out rooted_cold`. Expected ROOTED_CONTACT_CAPSULE_EXACT_AND_RESUME_PASS. Exact-only command: `python -B -S rooted_capsule/AUDIT_ROOTED_CHECKPOINTS.py --source source --checkpoints rooted_capsule/checkpoints --out exact_cold --expect rooted_capsule/EXPECTED_EXACT_RECEIPT.json`; observed THREE_ROOTED_C620_CHECKPOINTS_COLD_EXACT_OWN121_PASS. README has parent recovery commands and continuation examples. Reconstructed output path is not itself durable state.

RECOVER_ROOTED_JOIN.py 1174bytes SHA2561fd31cd20c85e4e4e343f465c61c1f8b8649b7dd36e2b17e3210ab478c48f022.

```python
"""Recover the complete ROOTED_C620_CHECKPOINTS_V1 source and checkpoint unit."""
from pathlib import Path
import sys,re,json,base64,lzma,hashlib
assert len(sys.argv)==6,'Give part1.md part2.md part3.md part4.md output_directory'
parts=[]
for i,name in enumerate(sys.argv[1:5],1):
 t=Path(name).read_text(encoding='utf-8');assert 'Recovery capsule part '+str(i)+'/4' in t
 matches=re.findall(r'```text\s*([A-Za-z0-9+/=\s]+?)```',t);assert len(matches)==1
 parts.append(''.join(matches[0].split()))
p=''.join(parts);assert len(p)==55296 and hashlib.sha256(p.encode()).hexdigest()=='d5bd4fe430e366d3824464bbbc4f9e37a058b304d33a0d115827d846ff0ae2e6'
b=lzma.decompress(base64.b64decode(p,validate=True));assert len(b)==178935 and hashlib.sha256(b).hexdigest()=='ccdca06fd9b6dec3440e3bbc1b36e4bafe7a817ac1361bc61e92b0c241fc8879'
d=json.loads(b);assert len(d)==50;out=Path(sys.argv[5]);out.mkdir(parents=True,exist_ok=False)
for name,t in d.items():
 q=Path(name);assert not q.is_absolute() and '..' not in q.parts;p=out/q;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf-8')
print('ROOTED_C620_COMPLETE_SOURCE_CHECKPOINT_UNIT_RECOVERED',len(d),flush=True)
```

## Ordered base64 payload


[Encoded source block omitted; the code in this passage is incomplete.]
