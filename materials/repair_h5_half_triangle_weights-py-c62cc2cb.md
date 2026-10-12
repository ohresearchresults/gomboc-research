# material-c62cc2cb9e0a

AI research material

---

#!/usr/bin/env python3
"""Restore the exact 303-row checkpoint from its immutable transport copy.
Eleven consecutive rows (532 bytes) were omitted in that copy, not in the
verified computation. Both complete input and output hashes are required.
Usage: python repair_h5_half_triangle_weights.py input.txt output.txt
"""
from pathlib import Path
import hashlib
import sys
INPUT_SHA='fd119b3865ea589d5637c59292213a7778958e44e313b5b60a227f2468828469'
OUTPUT_SHA='e79e0c50f9b102f81d64b1f3892af660c066bcabd117255442918b0d5b4e70b9'
INSERT=b'''8:3393137742 11:2872534340 23:3734327918
7:1639263438 19:7499512373 23:861224189
9:2761948583 20:4216923516 27:3021127901
1:4535298806 6:2665488437 19:2196670211 27:602542546
9:1722949307 14:1504597859 15:3084431882 30:3688020953
10:1419234530 14:2140007103 17:2076289477 26:4364468890
7:2997844852 10:1901210956 13:3073912783 20:2027031408
8:3130296664 19:4727306843 31:2142396493
2:3599832106 6:1961575025 22:4438592869
9:1737806146 12:3719822430 15:3578520252 22:963851172
10:1718320691 13:3185904916 18:3807883171 30:1287891222
'''
BEFORE=b'11:2972619725 12:740551300 17:2871342061 27:3415486913\n'
a=Path(sys.argv[1]).read_bytes()
if len(a)!=15549 or hashlib.sha256(a).hexdigest()!=INPUT_SHA:
    raise RuntimeError('Transport checkpoint differs from the immutable input')
if len(INSERT)!=532 or a.count(BEFORE)!=1:
    raise RuntimeError('Exact insertion precondition failed')
b=a.replace(BEFORE,INSERT+BEFORE)
if len(b)!=16081 or hashlib.sha256(b).hexdigest()!=OUTPUT_SHA:
    raise RuntimeError('Reconstructed checkpoint differs from the verified object')
Path(sys.argv[2]).write_bytes(b)
print('H5_HALF_TRIANGLE_CHECKPOINT_RECOVERY_PASS',len(b),OUTPUT_SHA)
