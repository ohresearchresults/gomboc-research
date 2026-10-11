# material-964b2db06ab5

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Mandatory exact literal-copy correction for J98 release input

Material [internal-source-reference] J98_EXACT_ELDER_RELEASE_CAPACITY.md has one documented transcription error in its FILE RELEASE98_INPUT.json, omega_negative.faces: the original polygon [7,9,3,36,35] was incorrectly copied as [7,9,3,39,172]. The originating successful exact computation used the CORRECT polygon and the promised17159-byte input with SHA1cfb4aa8b96d0b0f5446dd83b032ce12d039561160efcac8fd44efbbd6bf984a. The uncorrected archived literal is not that input and must NOT be used or advertised as independently runnable. This correction is a complete exact patch, not a changed body or changed mathematical result. Include this material with the release material in every relevant computational delivery.

Extract the complete FILE below together with the other J98 FILE blocks, then run `python REPAIR_RELEASE98.py` BEFORE `python -B -S caprelease98.py`. It accepts only the documented malformed hash or the already-correct exact input, then verifies the complete final length and SHA; any other discrepancy fails loudly. Expected marker: J98_RELEASE_INPUT_REPAIR_OR_ALREADY_CORRECT_PASS. REPAIR_RELEASE98.py has685 bytes SHA8bd916a876cf48fc4cbc3130b26312f5566ccd71b5ea3507158384af4948270f.

### FILE REPAIR_RELEASE98.py
```python
"""Correct the single documented literal-copy error in the archived release input.
This is a transport repair, not a changed construction or a changed proof.
"""
from pathlib import Path
import hashlib
p=Path(__file__).with_name('RELEASE98_INPUT.json')
good='1cfb4aa8b96d0b0f5446dd83b032ce12d039561160efcac8fd44efbbd6bf984a'
bad='55dd4b2b96ff4c31995323913d93e99d6151ed7c4a609701a950005616c3e327'
b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
if h==bad:
    assert b.count(b'[7,9,3,39,172]')==1
    b=b.replace(b'[7,9,3,39,172]',b'[7,9,3,36,35]')
assert len(b)==17159 and hashlib.sha256(b).hexdigest()==good
p.write_bytes(b)
print('J98_RELEASE_INPUT_REPAIR_OR_ALREADY_CORRECT_PASS')
```
