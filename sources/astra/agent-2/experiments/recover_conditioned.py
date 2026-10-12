from pathlib import Path
import sys,json,hashlib,time
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];src=ROOT/'sources/full76/decoded';sys.path[:0]=[str(src/'methods'),str(src/'methods/parent')]
import G_FREE_CODEC,RECONSTRUCT,check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
for name in ['CONDITIONED_C624','CONDITIONED_C626']:
 out=ROOT/'artifacts'/name;out.mkdir(exist_ok=True);gen=G_FREE_CODEC.decode(json.loads((src/'inputs'/f'{name}.json').read_text()));H=RECONSTRUCT.recover(gen);(out/'generator.json').write_bytes(B(gen));(out/'H_exact.json').write_bytes(B(H));rep=check_B.run(H);h=hashlib.sha256(B(rep)).hexdigest();expected=json.loads((src/'EXPECTED.json').read_text())['cases'][name]['report_sha256'];assert h==expected;(out/'B_exact.json').write_bytes(B(rep));print(name,*[rep[k] for k in ['V','E','F','counts','weak']],h,flush=True)
