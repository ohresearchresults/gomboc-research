"""Freeze rational supports; exact integer homogeneous signs and rational mass."""
import sys,pathlib,json,hashlib,numpy as np
from audit_integer import run as audit
from audit_persistence import run as barcode
import subprocess
src=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);D=int(sys.argv[3]) if len(sys.argv)>3 else 10**15;out.mkdir(parents=True,exist_ok=False)
q=np.load(src)['Q'];assert np.isfinite(q).all() and np.max(abs(q*D))<2**63
rows=np.rint(q*D).astype(np.int64).tolist();H=[r+[D] for r in rows];(out/'H.json').write_text(json.dumps({'H':H},separators=(',',':')));(out/'SOURCE.json').write_text(json.dumps({'source':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'grid':D},indent=2))
a=audit(H);(out/'audit.json').write_text(json.dumps(a,separators=(',',':')));print('EXACT_CENSUS',{k:a[k] for k in ['V','E','F','C','counts','weak','primitive_zero']},flush=True)
subprocess.run([sys.executable,'certify_boundedness.py',str(out/'H.json'),str(out/'boundedness.json')],check=True)
barcode(out/'audit.json',out/'bars.json')
manifest={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in out.iterdir() if p.is_file()};(out/'manifest.json').write_text(json.dumps(manifest,indent=2));print('EXACT_FREEZE_COMPLETE',out,flush=True)
