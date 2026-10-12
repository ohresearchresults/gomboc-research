"""Exact C622 G10 reconstruction and two independent audits from canonical FULL76."""
import copy,hashlib,json,sys,math
from fractions import Fraction as F
from pathlib import Path
assert __debug__,'Assertions must be enabled'
sys.set_int_max_str_digits(0)
assert len(sys.argv)==4,'Usage: RECOVER_G10.py FULL76_SOURCE C622_FULL_PROOF NEW_OUTPUT'
source,proof,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(source/'methods/parent'))
import RECONSTRUCT,check_A,check_B,centred_mass
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
sha=lambda x:hashlib.sha256(x).hexdigest()
G0=json.loads((proof/'C622_ROUTED/GENERATOR.json').read_bytes());R=json.loads((proof/'C622_ROUTED/A.json').read_bytes())
assert sha(B(G0))=='3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7'
assert sha(B(R))=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
G=copy.deepcopy(G0);G['grid']=10**10;G['controls']=[[round(F(v*G['grid'],G0['grid'])) for v in row] for row in G0['controls']]
assert sha(B(G))=='8e7065ce6e79b7fc8cd10c3c759748c6c7ea94f5281fc66b8e7188980b66c9cd'
raw=RECONSTRUCT.recover(G);assert sha(B(raw))=='492e33c118f40698edcc3e095d51f82b4eda863b7e12e3a6cb41cc9612eb081f'
for name,obj in [('GENERATOR.json',G),('raw.json',raw)]: (out/name).write_bytes(B(obj))
A=check_A.run(raw);(out/'A.json').write_bytes(B(A));print('G10_INDEPENDENT_A_COMPLETE',flush=True)
C=check_B.run(raw);(out/'B.json').write_bytes(B(C));print('G10_INDEPENDENT_B_COMPLETE',flush=True)
assert B(A)==B(C) and sha(B(A))=='b397575230d5af70de7cf0743b150dd69257455b4ae5c9685c6992724563910d'
assert [A[k] for k in ['V','E','F']]==[176,311,137] and A['counts']==[1,1,0] and A['weak']==[0,0,0]
for k in ['active_input_indices','faces','edges','stable_face_ids','unstable_vertices']:assert A[k]==R[k],k
mass=centred_mass.run(A);assert mass['filled_first_moments']==[0,0,0] and mass['common_centred_denominator_bits']==46717
(out/'MASS.json').write_bytes(B(mass))
receipt=dict(identity='COORD_C622_GRID10_OWN110',V=176,E=311,F=137,C=622,counts=A['counts'],weak=A['weak'],incidence_and_root_labels_equal_parent=True,parent_common_centred_denominator_bits=56802,common_centred_denominator_bits=46717,primitive_support_max_bits=max(abs(t).bit_length() for r in raw['H'] for t in r),outputs={name:dict(bytes=(out/name).stat().st_size,sha256=sha((out/name).read_bytes())) for name in ['GENERATOR.json','raw.json','A.json','B.json','MASS.json']})
(out/'RECEIPT.json').write_bytes(B(receipt));print('COORD_C622_GRID10_TWO_EXACT_AUDITS_COLD_PASS',sha(B(receipt)),flush=True)
