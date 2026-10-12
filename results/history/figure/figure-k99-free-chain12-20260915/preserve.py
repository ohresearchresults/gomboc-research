"""Preserve the exact declared source, without executing the scientific calculation."""
import ast,base64,hashlib,json,lzma,re
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
root=Path(__file__).resolve().parent
parent=root.parent/'figure-nh72-critical-energy-20260915'
s=json.loads((root.parent/'reconnect-20260915-1034-tOsXwk/figure-heartbeat-1137.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
j=Path('/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md').read_bytes()
if not s['journal']['prefixPreserved']or sha(j[:s['journal']['bytes']])!=s['journal']['sha256']:raise ValueError('Canonical snapshot changed')
entry=s['journal']['delta'].encode();start=s['journal']['bytes']-len(entry)
if j[start:s['journal']['bytes']]!=entry:raise ValueError('Journal interval differs')
blocks=re.findall(r'^\x60\x60\x60python\n(.*?)^\x60\x60\x60',entry.decode(),re.M|re.S)
if len(blocks)!=1:raise ValueError('Ambiguous source block')
code=blocks[0].encode()
if len(code)!=2771 or sha(code)!='e3803c9a4af82ba08dcd19a847169c95f02b0a978bee82470c925471a7c40bff':raise ValueError('Source pin differs')
ast.parse(code)
cap=(parent/'SOURCE_CAPSULE.b64').read_bytes()
if len(cap)!=35896 or sha(cap)!='0a45fce544afa3efce761946508184e050a1a80cb31f122d2e582af52f3d4f2b':raise ValueError('Parent capsule pin differs')
dec=lzma.LZMADecompressor(memlimit=134217728);raw=dec.decompress(base64.b64decode(cap,validate=True),max_length=87443)
if not dec.eof or dec.unused_data or len(raw)!=87442 or sha(raw)!='91a931bdc8b2470fad2b527b5455f2eaf5f1de62524aecb9c3d462f95d308152':raise ValueError('Parent decoded pin differs')
files=json.loads(raw);manifest=json.loads(files['MANIFEST.json'])
if len(files)!=28 or set(manifest)!=set(files)-{'MANIFEST.json'}:raise ValueError('Parent manifest incomplete')
for name,text in files.items():
 p=PurePosixPath(name)
 if not p.parts or p.is_absolute()or '..'in p.parts or chr(92)in name or str(p)!=name:raise ValueError('Unsafe path')
 b=text.encode()
 if(parent/'source'/name).read_bytes()!=b:raise ValueError('Parent source readback differs')
 if name in manifest and(len(b)!=manifest[name]['bytes']or sha(b)!=manifest[name]['sha256']):raise ValueError('Parent file pin differs')
pin=json.loads(files['EXPECTED.json'])['BASE/B.json']
if pin!={'bytes':246114,'sha256':'ae904b54ebc2b09cc034d913b48ae37b7877dc709b521abfc9ff5baca93bcc88'}:raise ValueError('Reconstructible input pin differs')
outputs={'free_chain12.py':code,'journal-entry.md':entry}
for name in [*outputs,'integrity-receipt.json']:
 if(root/name).exists():raise FileExistsError(root/name)
for name,b in outputs.items():
 with(root/name).open('xb')as f:f.write(b)
 if(root/name).read_bytes()!=b:raise ValueError('Archive readback differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'identity':'K99_FREE_ASCENT_111_TO_150_LAMBDA_GRID10','sourceEvent':1285,'sourceBytes':2771,'sourceSha256':sha(code),'journalBytes':len(entry),'journalSha256':sha(entry),'parentDirectory':str(parent/'source'),'parentFilesVerified':28,'parentArchiveDuplicated':False,'input':pin,'expectedReport':{'bytes':818,'sha256':'a89e4f2ab425bdb8585db6aa04112e1bdf9b239d4b45109ef3aa619cd3ab9e26'},'sourceComplete':True,'localMathematicalReplay':False,'verification':'Exact canonical interval/source pin, all28 parent source bytes and27 manifest pins, reconstructible input hash, Python syntax and written readbacks passed. No scientific code executed.','scope':'Author rational12-link free-space ascent chain showing sharpness of the K99 input/output link budget. It violates retained supporting halfspaces; not a convex-polyhedral repair, a new body or a smaller Gomboc. Generic angular criterion/proof retained as author mathematics, not independently reviewed.'}
with(root/'integrity-receipt.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))
