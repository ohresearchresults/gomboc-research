# material-216483bd9ebf

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule payload part 2/2 — two exact CONDITION25 descendants

This completes the data paired with [internal-source-reference]. Use the COMPLETE REPLAY_TWO.py code in [internal-source-reference], but EXCLUDE its malformed truncated payload. The complete durable closure is that code material, these TWO payload materials, and all THREE original CONDITION25 materials [internal-source-reference],[internal-source-reference],[internal-source-reference]. No originating sandbox is needed. Both exact bodies remain C622, not a complexity improvement.

Part2 length2900 SHA256a2146626f110c78888510a47cdd7170d57118d09978e41b319ead46f1f9265fa. Joined5900 SHA256ef74bf7dd77b0a2af2b659277b6be39069d94483d41b2df1d84b43ea14f6728c, decoded8728bytes SHA256b5865a3eb42ca37f36c66015324848b5fba8d8af98364bc97b171e0a49f0f343. Save this material and the preceding payload part as part2.md and part1.md. Run this COMPLETE ASSEMBLE.py with `python -B -S ASSEMBLE.py part1.md part2.md MATERIAL.md`:
```python
import sys,re,hashlib,base64,zlib
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for path,n,h in zip(sys.argv[1:3],[3000,2900],['1a0c956f137ae20b923737da29c8934af371db90d54af082d264a297741a2362','a2146626f110c78888510a47cdd7170d57118d09978e41b319ead46f1f9265fa']):
 m=re.findall(r'```base64\s*([A-Za-z0-9+/=\s]+)```',Path(path).read_text());assert len(m)==1
 b=''.join(m[0].split()).encode();assert len(b)==n and H(b)==h;parts.append(b)
b=b''.join(parts);assert len(b)==5900 and H(b)=='ef74bf7dd77b0a2af2b659277b6be39069d94483d41b2df1d84b43ea14f6728c'
r=zlib.decompress(base64.b64decode(b,validate=True));assert len(r)==8728 and H(r)=='b5865a3eb42ca37f36c66015324848b5fba8d8af98364bc97b171e0a49f0f343'
Path(sys.argv[3]).write_text('```base64\n'+b.decode()+'\n```\n')
print('TWO_SAMEC_EXACT_ENDPOINT_DATA_RECOVERY_PASS')
```
Then run `python -B -S REPLAY_TWO.py MATERIAL.md SOURCE NEW_OUTPUT` using the complete code from [internal-source-reference] and the decoded24-file parent source directory. Expected terminal CONDITION25_TWO_SAMEC_EXACT_AB_MASS_GATES_COLD_PASS, with all16body output files byte/hash checked. The two314-element free-coordinate delta arrays reconstruct the exact previously audited H representations; constrained-control placeholder bytes differ from the original full search dump but not the mathematical bodies.


[Encoded source block omitted; the code in this passage is incomplete.]
