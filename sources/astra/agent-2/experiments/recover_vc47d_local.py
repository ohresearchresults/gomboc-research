"""Recover literal H25 inputs from local preserved scientific source; no network.
AST literal extraction executes none of the source capsule.
"""
from pathlib import Path
import ast,json,sys,hashlib
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
src=ROOT.parent/'shared/sources/VC47D_RESULT_20260929T1627Z.md';b=src.read_bytes();sha=hashlib.sha256(b).hexdigest();assert sha=='cf2b89995ece3b1fd5d23ee214e65ef589724db37719b161aefdab6e6b95805c';s=b.decode();code=s.split('```python\n',1)[1].split('\n```',1)[0];tree=ast.parse(code);data={}
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ['G6','G5']:data[node.targets[0].id]=ast.literal_eval(node.value)
out=ROOT/'sources/VC47D';out.mkdir(exist_ok=False);(out/'source.md').write_bytes(b);(out/'PROVENANCE.json').write_text(json.dumps(dict(local_source=str(src),sha256=sha,recovery='AST literal assignments G6,G5 only; separate native check_B replay'),indent=2)+'\n')
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
blob=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
for key,scale in [('G6',10**6),('G5',10**5)]:
 rows=data[key]
 if key=='G5':rows[10][1]-=1
 dest=ROOT/'artifacts'/('VC47D_'+key);dest.mkdir(exist_ok=False);H={'H':[row+[scale] for row in rows]};(dest/'H.json').write_bytes(blob(H));r=check_B.run(H);(dest/'audit.json').write_bytes(blob(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary['audit_sha256']=hashlib.sha256(blob(r)).hexdigest();(dest/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('INDEPENDENT_NATIVE_AUDIT',key,summary,flush=True)
