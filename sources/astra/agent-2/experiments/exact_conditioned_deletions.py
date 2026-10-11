from pathlib import Path
import sys,json,time,hashlib
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0);sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
for removed in [17,35]:
 source=ROOT/'artifacts/CONDITIONED_C624/H_exact.json';H=json.loads(source.read_text());out=ROOT/'artifacts/conditioned_deletions'/f'C624_delete{removed}';out.mkdir(exist_ok=False);raw={'H':[v for i,v in enumerate(H['H']) if i!=removed]};(out/'H.json').write_bytes(B(raw));(out/'source.json').write_text(json.dumps(dict(source=str(source),removed=removed,sha256=hashlib.sha256(source.read_bytes()).hexdigest()),indent=2));r=check_B.run(raw);(out/'audit.json').write_bytes(B(r));summary={k:r[k] for k in ['V','E','F','counts','weak']};summary['audit_sha256']=hashlib.sha256(B(r)).hexdigest();(out/'summary.json').write_text(json.dumps(summary,indent=2));print('EXACT_CONDITIONED_DELETION',removed,summary,flush=True)
