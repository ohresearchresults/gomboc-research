# material-cae66b715ce3

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

#!/usr/bin/env python3
"""Recovery capsule part 3 of 3 for PRISMATOID_ALL_KERNEL_SHADOW_OCTAGON_REDUCTION_V1.
Input: exact text of immutable material [internal-source-reference].
Usage: python -B repair_prism_shadow.py PART2_PATH OUTPUT_PY
Python >=3.11; standard library only; assertions enabled.
"""
from pathlib import Path
import hashlib,sys
assert __debug__ and sys.version_info >= (3,11)
assert len(sys.argv)==3
source=Path(sys.argv[1]).read_bytes()
assert len(source)==12509
assert hashlib.sha256(source).hexdigest()=='336ba77e923ba1b362135d91c5bfb112825d1d09288a2f3396d90c7f357cadb9'
old=b'"98":["2/5","3/5","1/5","1/5","-6/5","1/5"]'
new=b'"98":["2/5","3/5","1/5","2/5","-6/5","1/5"]'
assert source.count(old)==1 and source.count(new)==0
out=source.replace(old,new)
assert len(out)==12509
assert hashlib.sha256(out).hexdigest()=='5023d1f20dea0654406ca5812431110f2218bd9262e5e2913146e0745f9383c7'
target=Path(sys.argv[2])
if target.exists():assert target.read_bytes()==out
else:target.write_bytes(out)
print('PRISM_SHADOW_SOURCE_SINGLE_WITNESS_REPAIR_PASS',len(out),hashlib.sha256(out).hexdigest())
