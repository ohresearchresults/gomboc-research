# material-6aaabcf70df6

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J125 C622 independent-deletion theorem — Recovery capsule part 3/3: exact source correction

The complete new recovery capsule now has THREE required parts. Earlier part1/part2 headers saying two parts are superseded by this explicit dependency correction:
1. [internal-source-reference], SHA6ca04e1b6567023bf363021e5cc1ad2124597a67c2a5b4d80f409576ca3728b0.
2. [internal-source-reference], SHA8b790b33f104b4b9ba76a123523f0ca935d4c366c163d528bcb0d5f4b6fc1c41.
3. This complete correction program.
Also supply the two canonical source materials named in part1. No scientific bound, exact executed calculation or nonwinner changed.

During storage of part2, the literal C622_ESCAPE125_NOMINATION.json graph row potential[86] was transcribed as [93] instead of the executed [90]. The one-row faulty JSON is3520B/SHA15828ebba02653596d1fa3e86d4e49967f1ad9a19a3f6bbba9582532effc10b7; its claimed correct hash in part2 applies ONLY AFTER this correction. Do not use that uncorrected row in the proof. The exact checker itself rejects the erroneous graph before concluding anything.

The complete patch below recomputes the ENTIRE graph from the exact canonical coordinates and rational1/125 cube, rather than trusting any typed label. It preserves the literal sparse duals and numerical witness, checks the complete corrected byte identity3520B/SHA7733cb9e2416e5ad39b8f34b09a29e257709ee1c57812ebf383e3a9c4a03164e, and checks the other6596B input hash. It also works idempotently on the already correct file. It was executed on the deliberately reproduced bad3520B input; the recovered file was byte-identical to the original successful computation input. This corrects source delivery, not mathematics, and is not a second hull audit.

After extracting all code/JSON blocks and reconstructing C622_A.json, execute in this order:
```
python -B -S repair_c622_escape125.py
python -B -S c622_certify125.py
python -B -S recover_c492125.py
python -B -S C622_SOURCE/core/check_A.py C622_DELETE_FREE_RAW.json C622_DELETE_FREE_A.json
```
Observed repair marker: J125_C622_ESCAPE_SOURCE_REPAIRED_EXACT_PASS. The previously executed exact theorem output2219B/SHA129b8660631b0eda893edf7d064516b2b82a4aa31d60062d4f8d32c3a414dd52 and child output225831B/SHAda96a39b19eb55c210120ad3dcfe7f1e182997899b4af3ffaa20a25f005d0fa8 remain unchanged.

## repair_c622_escape125.py
1129B,SHA dfa9e123209c5cb24813948068e7bc1e20c14fbc89ea005beba4459c68467016. Save with final newline. Its imported complete module is supplied in part1.
```python
"""Repair the part2 transcription of potential[86] before the exact J125 check.
Recompute the entire potential graph from exact coordinates, not a guessed label.
"""
from c622_certify125 import *
def run():
 raw=Path('C622_A.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA;a=json.loads(raw)
 p=Path('C622_ESCAPE125_NOMINATION.json');payload=json.loads(p.read_text());X=[tuple(map(F,x))for x in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));O=tuple(F(round(z*10**8),10**8)for z in g);eps=F(1,125)
 payload['potential']=[[j for j,y in enumerate(X)if j!=i and dot(sub(x,O),sub(y,x))+eps*sum(map(abs,sub(y,x)))>=0]for i,x in enumerate(X)]
 data=(json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode();assert len(data)==3520 and hashlib.sha256(data).hexdigest()=='7733cb9e2416e5ad39b8f34b09a29e257709ee1c57812ebf383e3a9c4a03164e'
 assert hashlib.sha256(Path('C622_DUAL125_NOMINATION.json').read_bytes()).hexdigest()=='a4f3aacb2b87716b3bb1a7401172ea1f88f5149fec829b75ac63083b43c5fbc5'
 p.write_bytes(data);print('J125_C622_ESCAPE_SOURCE_REPAIRED_EXACT_PASS')
if __name__=='__main__':run()
```
