"""Preserve the declared finite numerical method; execute no research code."""
import ast,base64,hashlib,json,lzma,re
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
root=Path(__file__).resolve().parent
parent=root.parent/'figure-c624-atlas57-depth2-20260915'
snapshot=json.loads((root.parent/'recovery-20260915-LyqbdO/figure-heartbeat-1018.json').read_text())
journal=Path('/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md').read_bytes()
def sha(b):return hashlib.sha256(b).hexdigest()
if not snapshot['journal']['prefixPreserved']or sha(journal[:snapshot['journal']['bytes']])!=snapshot['journal']['sha256']:raise ValueError('Canonical snapshot changed')
delta=snapshot['journal']['delta'].encode();start=snapshot['journal']['bytes']-len(delta)
if journal[start:snapshot['journal']['bytes']]!=delta:raise ValueError('Canonical delta differs')
md=delta.decode();mark='\n## 2026-09-15T10:13:58.335Z\n'
if md.count(mark)!=1:raise ValueError('Source entry ambiguous')
entry=mark+md.split(mark)[1]
blocks=re.findall(r'^\x60\x60\x60python\n(.*?)^\x60\x60\x60',entry,re.M|re.S)
if len(blocks)!=1:raise ValueError('Source block ambiguous')
code=blocks[0].encode()
if len(code)!=3729 or sha(code)!='d3c32587c415fb5ce60185ab8aa8a623d3d3236905b205871698300fedd6b96f':raise ValueError('Source pin differs')
ast.parse(code)
parts=re.split(r'(?=^## Recovery capsule part [1-4]/4 — ATLAS57_S8_CONTACT_TEN_EXACT_ENDPOINTS)',md,flags=re.M)
parts=[p for p in parts if p.startswith('## Recovery capsule part')]
if len(parts)!=4:raise ValueError('Missing/duplicated parent parts')
chunks=[]
for i,part in enumerate(parts,1):
 if not part.startswith(f'## Recovery capsule part {i}/4'):raise ValueError('Parent part order differs')
 b=re.findall(r'^\x60\x60\x60text\n(.*?)^\x60\x60\x60',part,re.M|re.S)
 if len(b)!=1:raise ValueError('Parent block ambiguous')
 chunks.append(''.join(b[0].split()).encode())
cap=b''.join(chunks)
if len(cap)!=41775 or sha(cap)!='9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d'or cap!=(parent/'SOURCE_CAPSULE.b85').read_bytes():raise ValueError('Canonical parent differs from existing archive')
dec=lzma.LZMADecompressor(memlimit=134217728);raw=dec.decompress(base64.b85decode(cap),max_length=112245)
if not dec.eof or dec.unused_data or len(raw)!=112244 or sha(raw)!='75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360':raise ValueError('Decoded parent differs')
files=json.loads(raw)
if len(files)!=26:raise ValueError('Parent source count differs')
manifest=json.loads(files['MANIFEST.json'])
if set(manifest)!=set(files)-{'MANIFEST.json'}:raise ValueError('Parent manifest incomplete')
for name,text in files.items():
 rel=PurePosixPath(name)
 if not rel.parts or rel.is_absolute()or '..'in rel.parts or chr(92)in name or str(rel)!=name:raise ValueError('Unsafe parent path')
 b=text.encode()
 if (parent/'source'/name).read_bytes()!=b:raise ValueError('Parent readback differs')
 if name in manifest and(len(b)!=manifest[name]['bytes']or sha(b)!=manifest[name]['sha256']):raise ValueError('Parent manifest mismatch')
expected=json.loads(files['EXPECTED.json'])
inputs={'STAR7':(248537,'3318a5f0516bc7476ac0d608c98e6d5bf85746fbf42a31e8fc48afa4dcf83205'),'STAR111':(248793,'b9c48463aa73767aec4a1d26b524643540f0a55bdaca2b20ead305b7efa0b2f1'),'C622_IMPROVED':(319558,'6b58d14e2ea5a973cce6b7888664fbc138e852f94d255a8d1b86868d2ea6f824'),'C622_D2_ADAPT':(255248,'3c31527bf827fe47d27523cf283da6ffd4b3455af39f294d17e7626ead4677bd')}
for name,(size,digest)in inputs.items():
 if expected[name]['record']!={'bytes':size,'sha256':digest}:raise ValueError('Exact input provenance differs')
outputs={'metric.py':code,'journal-entry.md':entry.encode()}
for name in [*outputs,'integrity-receipt.json']:
 if(root/name).exists():raise FileExistsError(root/name)
for name,b in outputs.items():
 with(root/name).open('xb')as f:f.write(b)
 if(root/name).read_bytes()!=b:raise ValueError('Output readback differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'sourceEvent':1266,'methodBytes':3729,'methodSha256':sha(code),'journalEntryBytes':len(entry.encode()),'journalEntrySha256':sha(entry.encode()),'parentDirectory':str(parent/'source'),'parentFilesVerified':26,'canonicalFourPartCopyEqualsExistingCapsule':True,'sourceComplete':True,'localMathematicalOrNumericalReplay':False,'verification':'Canonical delta/source pin, all parent file bytes/manifest and four exact input record pins checked. Python syntax and archive readback passed. No scientific code executed; no duplicate parent archive.','scope':'24 completed author numerical affine-metric SLSQP starts on four existing exact parents; no successful110 proposal. Not a global affine obstruction, exact endpoint classification or new construction record. Runtime-dependent numerical outputs include elapsed time.'}
with(root/'integrity-receipt.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))
