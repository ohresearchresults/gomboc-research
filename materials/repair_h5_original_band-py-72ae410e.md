# material-72ae410eb853

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Reconstruct the exact verified source from its immutable transport copy.
Usage: python repair_h5_original_band.py [input.txt] [output.py]
The one corrected comprehension belongs only to optional numerical search.
"""
from pathlib import Path
import hashlib
import sys
SOURCE_SHA='7d3e8927d60dabd004a751f699f3d52e58d5fde25f58be81e6e528452005b3f4'
OUTPUT_SHA='d6755a22a6ac68b9a865ea260113501ddba0abb81dd730f43d1dc533a7f91e4a'
source=Path(sys.argv[1] if len(sys.argv)>1 else 'h5_original_band.py.txt')
out=Path(sys.argv[2] if len(sys.argv)>2 else 'h5_original_band.py')
data=source.read_bytes()
if len(data)!=13199 or hashlib.sha256(data).hexdigest()!=SOURCE_SHA:
    raise RuntimeError('Immutable input differs from the preserved source')
bad=b'    keys=sorted({k for row in G for p in row.d})\n'
good=b'    keys=sorted({k for row in G for p in row for k in p.d})\n'
if data.count(bad)!=1:raise RuntimeError('Expected exactly one search-only line')
fixed=data.replace(bad,good)
if len(fixed)!=13210 or hashlib.sha256(fixed).hexdigest()!=OUTPUT_SHA:
    raise RuntimeError('Reconstructed source differs from the verified source')
out.write_bytes(fixed)
print('H5_ORIGINAL_BAND_EXACT_SOURCE_RECOVERY_PASS',len(fixed),OUTPUT_SHA)
