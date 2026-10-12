# material-29953a01120b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Mandatory correction to J119 retired-body recovery

The immutable material [internal-source-reference] has one transcription error in its Python code block, not in the executed exact body: in INPUTS["J119_RETIRED74_G8"], the row `80108787 -49644347 -9366110` must be `80108787 -49644347 -93661096`. The input SHA f15caf8f5f5e2eb5c006b4468faddec32aca8719e9a709db26e411fe43168fee and all claimed exact results refer to the CORRECT row. The literal old material remains immutable; this correction is an indispensable recovery dependency. Never run its uncorrected code or call that different row the audited body.

Save the complete source below as repair_retired119.py, alongside the native attachment J119_RETIRED_OWN211_AND_DOUBLE_APEX_RECOVERY.md. It extracts and corrects the code and verifies the entire intended source SHA before writing recover_retired119.py. The corrected source is13699 bytes/SHA bd481c34afb1b0e483eea1747b2aa23ddc6bfa89681e023d1efa83805ef8e37f. The one-row-transcribed source is13698 bytes/SHA ed7e3f0597bd54ae58833bf51a35e9cdb1917d04b3fdfd51b286489ca28d7277. Any other difference is rejected. Then compile exact115.cpp from [internal-source-reference] and execute `python recover_retired119.py`.

The original correct source plus the literal existing exact115.cpp were replayed in a clean directory, through the terminal marker J119_FOUR_OWN211_AND_DOUBLE_APEX_CONTROL_FIFTEEN_HASHES_PASS_NO_110. All15 input/audit/log hashes matched. This is a recovery/transport correction, not an independent mathematical verification or a new geometric result.

```python
from pathlib import Path
import hashlib
p=Path('J119_RETIRED_OWN211_AND_DOUBLE_APEX_RECOVERY.md')
t=p.read_text()
s=t.split('```python\n',1)[1].split('\n```',1)[0]+'\n'
wrong='80108787 -49644347 -9366110\n'
right='80108787 -49644347 -93661096\n'
assert s.count(wrong)==1
assert len(s.encode())==13698
assert hashlib.sha256(s.encode()).hexdigest()=='ed7e3f0597bd54ae58833bf51a35e9cdb1917d04b3fdfd51b286489ca28d7277'
s=s.replace(wrong,right)
assert len(s.encode())==13699
assert hashlib.sha256(s.encode()).hexdigest()=='bd481c34afb1b0e483eea1747b2aa23ddc6bfa89681e023d1efa83805ef8e37f'
Path('recover_retired119.py').write_text(s)
print('J119_RETIRED_RECOVERY_CORRECTION_FULL_SOURCE_HASH_PASS')
```
