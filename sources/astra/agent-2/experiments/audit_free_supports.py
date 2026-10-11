"""Freeze literal free support coordinates as integer halfspaces, exact own audit."""
from pathlib import Path
import sys,json,hashlib,numpy as np
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def audit(src,out,grid=10**12):
 out.mkdir(exist_ok=False,parents=True);raw=src.read_bytes();H=np.load(src);rows=[[int(round(x*grid)) for x in n]+[grid] for n in H];body={'H':rows};(out/'H.json').write_bytes(B(body));(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),grid=grid),indent=2)+'\n');r=check_B.run(body);(out/'audit.json').write_bytes(B(r));s={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],audit_sha256=hashlib.sha256(B(r)).hexdigest());(out/'summary.json').write_text(json.dumps(s,indent=2)+'\n');print('EXACT_FREE_SUPPORTS',s,flush=True);return r
if __name__=='__main__':audit(ROOT/sys.argv[1],ROOT/sys.argv[2],10**int(sys.argv[3]) if len(sys.argv)>3 else 10**12)
