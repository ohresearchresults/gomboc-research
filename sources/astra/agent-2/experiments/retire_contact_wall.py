"""Literal support retirement on a certified near-coplanar cap endpoint.
These are new physical halfspace bodies, with fresh exact mass and census.
"""
from pathlib import Path
import sys,json,hashlib,time
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
src=ROOT/'artifacts/canonical_atlas/detached_C496_large/exact_contact_wall_g14/H.json';raw=json.loads(src.read_text());base=ROOT/'artifacts/contact_wall_retire';base.mkdir(exist_ok=True)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
for which in [75,109]:
 out=base/f'delete{which}';out.mkdir(exist_ok=False);H={'H':[row for i,row in enumerate(raw['H']) if i!=which]};(out/'H.json').write_bytes(B(H));(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),removed_input_index=which),indent=2));r=check_B.run(H);(out/'audit.json').write_bytes(B(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary['C']=2*r['E'];summary['audit_sha256']=hashlib.sha256(B(r)).hexdigest();(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_CAP_RETIREMENT',which,summary,flush=True)
