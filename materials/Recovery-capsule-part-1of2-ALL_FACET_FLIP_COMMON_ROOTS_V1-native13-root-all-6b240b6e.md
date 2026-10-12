# material-6b240b6eb8a2

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""ALL_FACET_FLIP_COMMON_ROOTS_V1 complete exact recovery 13:root.
Dependencies: [internal-source-reference] as flip_moments.py;
[internal-source-reference] as common_roots.py;
[internal-source-reference] as native55.txt.
Run python -S recover_common_13_root.py with assertions enabled.
The complete coefficients are frozen signed little-endian16-bit integers.
No numerical library, network, or original sandbox is needed for recovery.
"""
from pathlib import Path
import json,hashlib,base64,lzma,struct,subprocess,sys
assert __debug__
HERE=Path(__file__).resolve().parent
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
SOURCE_PINS={'flip_moments.py':[13811,'7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7'],
'common_roots.py':[6011,'4d3e16daf49c9dbb4c4d5a88fce37f0337409502be51f1049ceaac3f6c4f0d62'],
'native55.txt':[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e']}
RAW_PIN=[27680, '8341381cf5223adb7d1cd2c9404e5ea86f74a86fa61963b2ee44588b6220adcd']
RECORD_PIN=[55137, '048c59685d993834a5863af88806c7cea203edeb36eb8c58d54c1d967e3c556b']
REPORT_PIN=[5116, 'd4797f84e0d43381d390af92c3dfc55febad0842fa0e958b13832e1470a61aa2']
RECORD={'identity': 'ALL_FACET_FLIP_COMMON_ROOTS_V1', 'mode': 'root', 'native_index': 13, 'rounding_power': 12, 'system_pin': [7519, '0a74fc4564a088d0f84add35a856b9a1ed588c7e92f468e871198cea75a9c5b8']}
DATA="""

[Encoded source block omitted; the code in this passage is incomplete.]
