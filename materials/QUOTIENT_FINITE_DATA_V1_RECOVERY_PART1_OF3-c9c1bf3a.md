# material-c9c1bf3a5fcf

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/3 — QUOTIENT_FINITE_DATA_V1

All 3 ordered parts are required. This part has 16080 base64 characters, SHA256 a5480d814356ef83b6b982d954cc9bd17d8d5a21a226217d3bbf4b06ef5a66e5. Complete source/data dictionary 33 files, 183991 bytes, SHA256 7f06fb8f9ce430feb0407e4f41ff5457ce4d0aa8235d203c03f9ea9642d13366. No credentials or ancestor sandbox are included.

This data unit depends on all parts of BALANCED_CONTACT_CORE_V1, but not other data directions. Recover both units into the same directory; the decoder only permits byte-identical shared files. Frozen coordinates, nondefault configurations, complete finite classification/ranking values and outcomes are preserved. No unaudited endpoint is promoted to own110.

Save the Python block as RECOVER_JOIN.py, retain these ordered material texts as part1.md etc., and run `python -B -S RECOVER_JOIN.py part1.md part2.md part3.md SOURCE`. Expected marker QUOTIENT_FINITE_DATA_V1_COMPLETE_SOURCE_RECOVERED 33. With the core merged, `python -B -S SOURCE/REPLAY_EXACT.py exact_output` gives BALANCED_QUOTIENT_C620_EXACT_NONWINNER_AB_MASS_PASS; the exact quotient is175/310/137,strict95/104/197,weak000,NOTthe olderC620own121. Decoder 1213bytes SHA256 df08b003218ad8510ccdfabe6bf5d1e600beee5c0a30652b123944ce7dade66a.

```python
"""Recover ordered exact source/data parts; existing files may only match byte-for-byte."""
from pathlib import Path
import sys,re,json,base64,lzma,hashlib
assert __debug__
assert len(sys.argv)==5
chunks=[]
for i,name in enumerate(sys.argv[1:-1],1):
 t=Path(name).read_text(encoding='utf-8');assert "QUOTIENT_FINITE_DATA_V1" in t and 'Recovery capsule part '+str(i)+'/3 ' in t
 m=re.findall(r'```text\s*([A-Za-z0-9+/=\s]+?)```',t);assert len(m)==1;chunks.append(''.join(m[0].split()))
p=''.join(chunks);assert len(p)==48232 and hashlib.sha256(p.encode()).hexdigest()=="d49499f0735df3097f6a48fb6143f08ad42e0bac615a97cb311b82279e152385"
b=lzma.decompress(base64.b64decode(p,validate=True));assert len(b)==183991 and hashlib.sha256(b).hexdigest()=="7f06fb8f9ce430feb0407e4f41ff5457ce4d0aa8235d203c03f9ea9642d13366"
d=json.loads(b);assert len(d)==33;out=Path(sys.argv[-1]);out.mkdir(parents=True,exist_ok=True)
for n,t in d.items():
 q=Path(n);assert not q.is_absolute() and '..' not in q.parts;p=out/q;p.parent.mkdir(parents=True,exist_ok=True);data=t.encode('utf-8')
 if p.exists():assert p.read_bytes()==data,n
 else:p.write_bytes(data)
print("QUOTIENT_FINITE_DATA_V1_COMPLETE_SOURCE_RECOVERED",len(d),flush=True)
```

## Ordered payload


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
