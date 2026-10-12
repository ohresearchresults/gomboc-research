"""New exact physical H-body after literal removal of specified input planes."""
from pathlib import Path
import sys,json,hashlib
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
src=ROOT/sys.argv[1];raw=json.loads(src.read_text());base=ROOT/sys.argv[2];base.mkdir(exist_ok=True,parents=True)
for arg in sys.argv[3:]:
 removed=list(map(int,arg.split(',')));out=base/('delete_'+'_'.join(map(str,removed)));out.mkdir(exist_ok=False);H={'H':[row for i,row in enumerate(raw['H']) if i not in removed]};(out/'H.json').write_bytes(B(H));(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),removed_input_indices=removed),indent=2));r=check_B.run(H);(out/'audit.json').write_bytes(B(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],audit_sha256=hashlib.sha256(B(r)).hexdigest());(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_SUPPORT_RETIREMENT',removed,summary,flush=True)
