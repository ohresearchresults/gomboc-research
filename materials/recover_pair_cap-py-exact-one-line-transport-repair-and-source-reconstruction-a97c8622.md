# material-a97c86222059

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Repair the one exact transcription error in immutable [internal-source-reference].
python -S recover_pair_cap.py STORED_SOURCE OUTPUT_DIRECTORY
This produces the complete frozen source, not a numerical replacement certificate.
"""
from pathlib import Path
import hashlib,sys
assert __debug__ and len(sys.argv)==3
b=Path(sys.argv[1]).read_bytes()
assert [len(b),hashlib.sha256(b).hexdigest()]==[5240,'6effed5f64ea9087ecb81f4a373c2c7f55b9fb5fd2aaad0103747a0b5095ebdd']
old=b' assert hn==scale(add(ONE,scale(mul(A,power(E,3),-1)),2))\n'
new=b' assert hn==scale(add(ONE,scale(mul(A,power(E,3)),-1)),2)\n'
assert b.count(old)==1;b=b.replace(old,new)
assert [len(b),hashlib.sha256(b).hexdigest()]==[5240,'a8fa3c2b514290229ad8ff417a5895a9d31c22302d0835546c4ee8c9f9a72bad']
p=Path(sys.argv[2]);p.mkdir(parents=True,exist_ok=True);target=p/'pair_cap_exact.py'
assert not target.exists() or target.read_bytes()==b
target.write_bytes(b)
print('PAIR_CAP_EXACT_SOURCE_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
