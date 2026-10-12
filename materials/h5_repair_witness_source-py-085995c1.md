# material-085995c1fc18

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Repair the one-colon transport typo in immutable witness material.
The input is [internal-source-reference], not executable source as stored.
This exact patch restores the already tested complete 49-case input.
Usage: python -B -S h5_repair_witness_source.py INPUT.txt
"""
from pathlib import Path
import hashlib,sys
source=Path(sys.argv[1]).read_bytes()
assert len(source)==11576
assert hashlib.sha256(source).hexdigest()=='56681bc92cc5603db9a2f1c88699973bfa5ab32f9316678a10ded88f989be438'
old=b'assert len(a)==4 and 0<=a[0]<=4 and any(a[1:]):\n'
new=b'assert len(a)==4 and 0<=a[0]<=4 and any(a[1:])\n'
assert source.count(old)==1
fixed=source.replace(old,new)
assert len(fixed)==11575
assert hashlib.sha256(fixed).hexdigest()=='5661daf87600dfc871e9a4656eca05a332db54ee2ed51c9b361c8a4dc8c4729e'
Path('h5_paired_arrow_witnesses.py').write_bytes(fixed)
print('H5_PAIRED_ARROW_EXACT_WITNESS_SOURCE_RESTORED')
