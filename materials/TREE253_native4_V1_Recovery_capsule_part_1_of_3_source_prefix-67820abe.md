# material-67820abe26d9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""TREE253_K2_NATIVE4_SHARED_ACTUAL_MOMENTS_V1, complete recovery capsule.
Pure standard library, assertions required. python -S recover_native4.py
Writes exact source/data/provenance files into native4_recovered, then executes
independent integer Bareiss and Fraction LDL checks, and pins report/stdout.
Floating-point locator is optional and is not run by the proof verifier.
"""
from pathlib import Path
import base64,hashlib,json,subprocess,sys,lzma
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
DATA="""

[Encoded source block omitted; the code in this passage is incomplete.]
