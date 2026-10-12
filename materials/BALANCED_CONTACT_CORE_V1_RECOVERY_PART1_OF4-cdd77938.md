# material-cdd77938ee30

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/4 — BALANCED_CONTACT_CORE_V1

All 4 ordered parts are required. This part has 13044 base64 characters, SHA256 f2e4c4b8b7be5cdf3ab6d04b806fb998b60c7c2d6e11a08b1a9642b0c7f9b8d6. Complete source/data dictionary 35 files, 145500 bytes, SHA256 87fa0fda9216309f0bd4ccea398bdd124174278161b4af7a29f2c412b33c5551. No credentials or ancestor sandbox are included.

Self-contained complete balanced-contact, quotient, positive-edge-shortening, hard-QP and gradual-max-min producers with full old-helper closure and exact canonical C622/older C620own121 inputs. This core preserves methods, not a record or a family exclusion. Derivative checks and both exact parent B identities were cold-replayed successfully. Observed final marker BALANCED_CONTACT_COMPLETE_CORE_PARENTS_DERIVATIVE_REPLAY_PASS. NumPy2.3.5, SciPy1.17.0, CPython3.13.5, BLAS/OMP1thread; assertions enabled. Exact preparation/checkers use standard library only. Newer V2 adaptive continuation/integer-grid methods are separate patches, not silently substituted here.

Save the Python block as RECOVER_JOIN.py, retain these ordered material texts as part1.md etc., and run `python -B -S RECOVER_JOIN.py part1.md part2.md part3.md part4.md SOURCE`. Expected marker BALANCED_CONTACT_CORE_V1_COMPLETE_SOURCE_RECOVERED 35. Then `python -B SOURCE/CORE_REPLAY.py output` verifies complete source hashes, exact parent identities and the observed numerical derivative receipt. Decoder 1215bytes SHA256 848ad397994c208008c1b5976742845982965130cf82b022184cffe5c7f02f6a.

```python
"""Recover ordered exact source/data parts; existing files may only match byte-for-byte."""
from pathlib import Path
import sys,re,json,base64,lzma,hashlib
assert __debug__
assert len(sys.argv)==6
chunks=[]
for i,name in enumerate(sys.argv[1:-1],1):
 t=Path(name).read_text(encoding='utf-8');assert "BALANCED_CONTACT_CORE_V1" in t and 'Recovery capsule part '+str(i)+'/4 ' in t
 m=re.findall(r'```text\s*([A-Za-z0-9+/=\s]+?)```',t);assert len(m)==1;chunks.append(''.join(m[0].split()))
p=''.join(chunks);assert len(p)==52176 and hashlib.sha256(p.encode()).hexdigest()=="0c7d4b7effb90b13672b1f380ef9975fec687f6ab0e97b1f994a4a5319a5f5be"
b=lzma.decompress(base64.b64decode(p,validate=True));assert len(b)==145500 and hashlib.sha256(b).hexdigest()=="87fa0fda9216309f0bd4ccea398bdd124174278161b4af7a29f2c412b33c5551"
d=json.loads(b);assert len(d)==35;out=Path(sys.argv[-1]);out.mkdir(parents=True,exist_ok=True)
for n,t in d.items():
 q=Path(n);assert not q.is_absolute() and '..' not in q.parts;p=out/q;p.parent.mkdir(parents=True,exist_ok=True);data=t.encode('utf-8')
 if p.exists():assert p.read_bytes()==data,n
 else:p.write_bytes(data)
print("BALANCED_CONTACT_CORE_V1_COMPLETE_SOURCE_RECOVERED",len(d),flush=True)
```

## Ordered payload


[Encoded source block omitted; the code in this passage is incomplete.]
