from pathlib import Path
import sys,json,time,hashlib
sys.set_int_max_str_digits(0)
root=Path('sources/FULL76').resolve();sys.path[:0]=[str(root/'methods'),str(root/'methods/parent')]
import G_FREE_CODEC,RECONSTRUCT,check_B
from gmpy2 import mpq
out=Path('artifacts/c622');out.mkdir(exist_ok=True)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
t=time.time();G=G_FREE_CODEC.decode(json.loads((root/'inputs/C622_ROUTED.json').read_text()));(out/'GENERATOR.json').write_bytes(B(G));raw=RECONSTRUCT.recover(G);(out/'raw.json').write_bytes(B(raw));print('RECONSTRUCT',time.time()-t,flush=True)
check_B.Q=mpq
rep=check_B.run(raw);payload=B(rep);(out/'audit.json').write_bytes(payload)
expected=json.loads((root/'EXPECTED.json').read_text())['cases']['C622_ROUTED'];assert hashlib.sha256(payload).hexdigest()==expected['report_sha256']
print('C622_EXACT_AUDIT_MATCH',time.time()-t,rep['V'],rep['E'],rep['F'],rep['counts'],rep['weak'],hashlib.sha256(payload).hexdigest(),flush=True)
