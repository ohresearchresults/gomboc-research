# material-67820abe26d9

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

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
