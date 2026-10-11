"""Rebuild all 42 exact control-rounded bodies without numerical dependencies."""
import copy,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
assert __debug__,'Assertions must be enabled'
sys.set_int_max_str_digits(0)
assert len(sys.argv)==4,'Usage: REBUILD_FACTORED_INPUTS.py FULL76_SOURCE C622_FULL_PROOF NEW_OUTPUT'
source,proof,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(source/'methods/parent'));import RECONSTRUCT
B=lambda v:json.dumps(v,sort_keys=True,separators=(',',':')).encode()
sha=lambda b:hashlib.sha256(b).hexdigest()
b=(proof/'C622_ROUTED/GENERATOR.json').read_bytes()
assert len(b)==11841 and sha(b)=='3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7'
G=json.loads(b);expected=json.loads((Path(__file__).parent/'EXPECTED_EXACT_INPUTS.json').read_text())
Dlist=sorted(set([n*2**28 for n in range(4,33)]+[n*10**8 for n in range(8,21)]));assert len(Dlist)==42
seen=set()
for D in Dlist:
 H=copy.deepcopy(G);H['grid']=D;H['controls']=[[round(F(v*D,G['grid'])) for v in row] for row in G['controls']]
 r=RECONSTRUCT.recover(H);p=out/str(D);p.mkdir()
 for name,obj in [('GENERATOR.json',H),('raw.json',r)]:
  b=B(obj);key=f'{D}/{name}';assert dict(bytes=len(b),sha256=sha(b))==expected[key],key
  (p/name).write_bytes(b);seen.add(key)
assert seen==set(expected)
print('C622_ALL42_EXACT_ROUNDED_INPUTS_RECOVERY_PASS')
