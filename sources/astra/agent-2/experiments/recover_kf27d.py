from pathlib import Path
import ast,sys,hashlib,json
import numpy as np
p=Path(__file__).resolve().parents[1]
f=p/'sources/KF27D_exact_component.py';data=f.read_bytes()
assert hashlib.sha256(data).hexdigest()=='1e1c634dba92bd6e9d470df6de7b0b9dcf1ebe50333564dd85a00ab15ce2d4f4'
tree=ast.parse(data)
text=next(ast.literal_eval(s.value) for s in tree.body if isinstance(s,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='INPUT_TEXT' for t in s.targets))
assert hashlib.sha256(text.encode()).hexdigest()=='52a71e8f9dbfe781d3a0aeafe053045e7cedb2fa588661f822d05990c5a86421'
lines=text.splitlines();n,D=map(int,lines[0].split());H=[list(map(int,l.split()))+[D] for l in lines[1:]];assert len(H)==n
out=p/'artifacts/kf27d';out.mkdir(exist_ok=True)
(out/'H_exact.json').write_text(json.dumps({'H':H})+'\n');(out/'input.txt').write_text(text)
sys.path.insert(0,str(p/'sources/full76/decoded/methods/parent'));import check_B
rep=check_B.run({'H':H});(out/'B_exact.json').write_text(json.dumps(rep,sort_keys=True,separators=(',',':')))
np.save(out/'supports.npy',np.array([r[:3] for r in H])/D)
print('Independent exact audit',*[rep[k] for k in ('V','E','F','counts','weak')],flush=True)
