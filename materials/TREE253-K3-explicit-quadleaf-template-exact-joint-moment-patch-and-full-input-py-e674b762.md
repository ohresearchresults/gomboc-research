# material-e674b7621db2

AI research material

---

"""Exact patch + literal input for one genuine TREE253/K3 template.
Usage: python -S make_k3_joint.py PATH_TO_RECOVERED_joint_exact.py
The base source is completely preserved in the two-part K2 recovery capsule.
This template index0 is NOT native55 index0 and not a canonical K3 census id.
"""
from pathlib import Path
import hashlib,sys
assert __debug__ and len(sys.argv)==2
root=Path(__file__).resolve().parent
b=Path(sys.argv[1]).read_bytes()
assert len(b)==14595 and hashlib.sha256(b).hexdigest()=='160343c32a9362961247308dc845709241b9ef00efa72a716411fbe35dd6590b'
row='0: 012 016 023 037 067 1256 2345 3478 458 5678\n'
data=row.encode();sha=hashlib.sha256(data).hexdigest()
s=b.decode()
changes=[("'native55.txt'","'k3_explicit_templates.txt'"),
("INPUT_PIN=[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e']",f"INPUT_PIN=[{len(data)},'{sha}']"),
("IDENTITY='MINIMUM_JOINT_MOMENT_V2'","IDENTITY='MINIMUM_TREE253_K3_EXPLICIT_JOINT_V1'"),
('assert sorted(d)==list(range(55))','assert sorted(d)==list(range(1))'),
('all(1<=r<=8 for r in roots)','all(0<=r<=9 for r in roots)'),
('native_index','template_index')]
for old,new in changes:
 assert old in s,old;s=s.replace(old,new)
s=s.replace('Requires only the pinned native55.txt.', 'Requires only the pinned k3_explicit_templates.txt.')
s=s.replace('not native labels.','not the lexicographic incidence-vertex labels.')
(root/'k3_explicit_templates.txt').write_bytes(data)
(root/'k3_joint_exact.py').write_text(s)
for name in ['k3_explicit_templates.txt','k3_joint_exact.py']:
 q=(root/name).read_bytes();print('K3_EXPLICIT_INPUT',name,len(q),hashlib.sha256(q).hexdigest())
print('K3_EXPLICIT_JOINT_PATCH_RECOVERED_NOT_CANONICAL_CENSUS_ALIAS')
