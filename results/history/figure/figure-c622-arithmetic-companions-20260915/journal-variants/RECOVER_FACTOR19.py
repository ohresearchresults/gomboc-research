"""Exact C622 factored-grid reconstruction and two independent full audits."""
import copy,hashlib,json,sys,math
from fractions import Fraction as F
from pathlib import Path
assert __debug__,'Assertions must be enabled'
sys.set_int_max_str_digits(0)
assert len(sys.argv)==4,'Usage: RECOVER_FACTOR19.py FULL76_SOURCE C622_FULL_PROOF NEW_OUTPUT'
source,proof,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(source/'methods/parent'))
import RECONSTRUCT,check_A,check_B,centred_mass
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
sha=lambda x:hashlib.sha256(x).hexdigest()
G0=json.loads((proof/'C622_ROUTED/GENERATOR.json').read_bytes());R=json.loads((proof/'C622_ROUTED/A.json').read_bytes())
assert sha(B(G0))=='3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7'
assert sha(B(R))=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
G=copy.deepcopy(G0);G['grid']=19*2**28;G['controls']=[[round(F(v*G['grid'],G0['grid'])) for v in row] for row in G0['controls']]
assert sha(B(G))=='38280786ad0dbb1219d114fa3732eb7f2799aa30425eb7f071ccb683548d697a'
raw=RECONSTRUCT.recover(G);assert sha(B(raw))=='f7d28ac1953c17f4c8202546ea4f1958a465da7e47ee976ce88203cc3a2ff272'
for name,obj in [('GENERATOR.json',G),('raw.json',raw)]: (out/name).write_bytes(B(obj))
A=check_A.run(raw);(out/'A.json').write_bytes(B(A));print('FACTOR19_INDEPENDENT_A_COMPLETE',flush=True)
C=check_B.run(raw);(out/'B.json').write_bytes(B(C));print('FACTOR19_INDEPENDENT_B_COMPLETE',flush=True)
assert B(A)==B(C)
assert [A[k] for k in ['V','E','F']]==[176,311,137] and A['counts']==[1,1,0] and A['weak']==[0,0,0]
for k in ['active_input_indices','faces','edges','stable_face_ids','unstable_vertices']:assert A[k]==R[k],k
mass=centred_mass.run(A);assert mass['filled_first_moments']==[0,0,0]
(out/'MASS.json').write_bytes(B(mass))
receipt=dict(identity='COORD_C622_FACTOR19_OWN110',V=176,E=311,F=137,C=622,counts=A['counts'],weak=A['weak'],incidence_and_root_labels_equal_parent=True,parent_common_centred_denominator_bits=56802,common_centred_denominator_bits=mass['common_centred_denominator_bits'],primitive_support_max_bits=max(abs(t).bit_length() for r in raw['H'] for t in r),outputs={name:dict(bytes=(out/name).stat().st_size,sha256=sha((out/name).read_bytes())) for name in ['GENERATOR.json','raw.json','A.json','B.json','MASS.json']})
(out/'RECEIPT.json').write_bytes(B(receipt));print('COORD_C622_FACTOR19_TWO_EXACT_AUDITS_COLD_PASS',sha(B(receipt)),flush=True)
