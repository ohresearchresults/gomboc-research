"""Cold replay of both the rational trial and exact algebraic mass closure.
Usage: python -B -S REPLAY_MASS_GATE.py CORE C592_SOURCE R12_METHOD NEW
"""
import hashlib,json,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
assert len(sys.argv)==5
here=Path(__file__).resolve().parent
core,c592,r12,out=[Path(x).resolve() for x in sys.argv[1:]]
sha=lambda b:hashlib.sha256(b).hexdigest()
for name,spec in json.loads((here/'MANIFEST.json').read_bytes()).items():
 b=(here/name).read_bytes();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
out.mkdir(parents=True,exist_ok=False)
def run(script,*args):
 subprocess.run([sys.executable,'-B','-S',str(script),*map(str,args)],check=True)
run(r12/'REPLAY_OPPOSITE.py',core,c592,out/'rational')
base=out/'rational'/'C592';rat=out/'rational'/'OPPOSITE'
# The upstream driver is authoritative for its output-directory spelling.
if not rat.exists():
 candidates=[p for p in (out/'rational').iterdir() if p.is_dir() and p.name!='C592' and (p/'A.json').exists()]
 assert len(candidates)==1;rat=candidates[0]
run(here/'mass_chamber.py',base,out/'mass_chamber.json')
run(here/'quartic_isolate.py',out/'mass_chamber.json',base/'A.json',out/'quartic_proof.json')
run(here/'algebraic_census.py',out/'mass_chamber.json',out/'quartic_proof.json',base,rat,out/'algebraic_census.json')
for name,spec in json.loads((here/'EXPECTED.json').read_bytes()).items():
 b=(out/name).read_bytes();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
print('SOURCE_ONLY_C486_RATIONAL_AND_ALGEBRAIC_MASS_GATE_PASS',flush=True)
