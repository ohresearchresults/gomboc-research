# material-db6ad3bc5724

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J141 exact-source correction — authoritative

The source material [internal-source-reference] contains one transcription error in its JOINT141_RECIPES.json literal: roots['9']['bases'][14] was copied as[45,19,2] instead of the executed[52,19,2]. Its stated recipe hash identifies the correct original, not that uncorrected literal. No coordinate, dual multiplier, claimed inequality or scientific scope changes. The theorem [internal-source-reference] is unchanged.

The complete recovery dependency is therefore BOTH [internal-source-reference] AND THIS CORRECTION. Extract the three files using the earlier material's extraction command, then save the complete code below as J141_FIX_RECIPE.py and run:

python -B -S J141_FIX_RECIPE.py
python -B -S replay_joint141.py

The correction is idempotent on the correct recipe. It normalizes the recipe's canonical JSON and verifies all three input file hashes. Its successful execution on the correct source was observed. The exact replay of that correct source was already executed and produced the reported1082059-byte output SHA256e885f9098aaa37404e5af3ee0c8ecbdf6efa41c73f6ae4c9734f190619471876. Do not represent the uncorrected material alone as sufficient for matching this output.

J141_FIX_RECIPE.py960bytes/SHA2561f64ed0e1d4df40dd750b80db8dc75db0d3841a4640aff4d4825964b2a28b421.
Expected correction marker:J141_COMPLETE_RECOVERY_INPUT_HASHES_PASS.

```python
"""Repair the explicitly identified transcription in material [internal-source-reference].
This changes one nominated basis index, not any coordinates, inequality or theorem.
"""
from pathlib import Path
import hashlib,json
p=Path('JOINT141_RECIPES.json');a=json.loads(p.read_text())
assert a['roots']['9']['bases'][14] in ([45,19,2],[52,19,2])
a['roots']['9']['bases'][14]=[52,19,2]
p.write_bytes((json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode())
manifest={
 'QW49J_LOW62_G9_INPUT.json':(2182,'90cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e'),
 'JOINT141_RECIPES.json':(12043,'6df5f66d188508824535ce7e5137ca9b09d769baf3484d6bfcdab06d114267fa'),
 'replay_joint141.py':(5378,'d51e02cae97592ae6770f017ecd4675533ed32ec5973251e92490f681b00947c')}
for name,(size,sha) in manifest.items():
 b=Path(name).read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==sha,name
print('J141_COMPLETE_RECOVERY_INPUT_HASHES_PASS')
```
