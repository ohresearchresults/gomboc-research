"""Verify exact source transport and preserve it without executing the mathematical replay."""
import ast,base64,hashlib,json,lzma,re
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
root=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
raw=(root/'result.json').read_bytes()
if len(raw)!=57630 or sha(raw)!='8f5a615c012602e68ecf21b25dd3a7d2d5a2f00e1bc176818aea539a411193a6':raise ValueError('Immutable result pin differs')
md=json.loads(raw)['result_markdown']
if (root/'result.md').read_bytes()!=md.encode()or len(md.encode())!=56985 or sha(md.encode())!='337a42a241795c67a1e21741cba955f45ff6959e2ffdb9b99e1d3735cccb6dab':raise ValueError('Markdown identity differs')
start,end='\nNH72_EXTERNAL_B64_BEGIN\n','\nNH72_EXTERNAL_B64_END'
if md.count(start)!=1 or md.count(end)!=1:raise ValueError('Ambiguous source markers')
cap=''.join(md.split(start)[1].split(end)[0].split()).encode()
if len(cap)!=36384 or sha(cap)!='45f6257619278cf1cf3a373047c86ab19b67679def04b82c60612d2ec61d8009':raise ValueError('Encoded source pin differs')
dec=lzma.LZMADecompressor(memlimit=134217728);decoded=dec.decompress(base64.b64decode(cap,validate=True),max_length=92707)
if not dec.eof or dec.unused_data or len(decoded)!=92706 or sha(decoded)!='f5fba1517674ad24e05f3580f995fe3ac1868a4feb6bcea988a69c654d10e692':raise ValueError('Decoded source pin differs')
files=json.loads(decoded)
if len(files)!=31:raise ValueError('Wrong source count')
for name,text in files.items():
 p=PurePosixPath(name)
 if not isinstance(text,str)or not p.parts or p.is_absolute()or '..'in p.parts or chr(92)in name or str(p)!=name:raise ValueError('Unsafe source path')
 if name.endswith('.py'):ast.parse(text,filename=name)
 elif name.endswith('.json'):json.loads(text)
manifest=json.loads(files['MANIFEST.json'])
if set(manifest)!=set(files)-{'MANIFEST.json'}:raise ValueError('Incomplete manifest')
for name,pin in manifest.items():
 b=files[name].encode()
 if len(b)!=pin['bytes']or sha(b)!=pin['sha256']:raise ValueError('Per-file pin differs')
restore=re.findall(r'^\x60\x60\x60python\n(.*?)^\x60\x60\x60',md,re.M|re.S)
if len(restore)!=1:raise ValueError('Ambiguous original decoder')
ast.parse(restore[0])
outputs={'source/'+name:text.encode()for name,text in files.items()}
outputs.update({'SOURCE_CAPSULE.b64':cap,'restore_original.py':restore[0].encode()})
for name in [*outputs,'integrity-receipt.json']:
 if(root/name).exists():raise FileExistsError(root/name)
for name,b in outputs.items():
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb')as f:f.write(b)
 if p.read_bytes()!=b:raise ValueError('Source readback differs')
parent=root.parent/'figure-nh72-critical-energy-20260915/result.json'
parent_raw=parent.read_bytes()
if sha(parent_raw)!='cdfd56c04915598cfff007d85526937819e3fefd19b645d3c9abfd56d9ff9313':raise ValueError('Existing parent JSON pin differs')
parent_md=json.loads(parent_raw)['result_markdown'].encode()
if len(parent_md)!=66346 or sha(parent_md)!='f8f5cbf5f8792d541f65564fc5c6180ad5badd7557da12745ade722490ca8e1e':raise ValueError('Parent Markdown boundary differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'identity':'NH72_PAIR99_EXTERNAL13_CRITICAL12_MASS_E309_R12','assignmentId':'asg_WRxoC0zdr4NGKG_Cuaysphxh','sourceFiles':31,'standalone':True,'completeSourcePreservedLocally':True,'resultSha256':sha(raw),'resultBytes':len(raw),'markdownSha256':sha(md.encode()),'capsuleBytes':len(cap),'capsuleSha256':sha(cap),'decodedBytes':len(decoded),'decodedSha256':sha(decoded),'verification':'Immutable JSON/Markdown, encoded/decoded pins, all30 manifest entries, JSON/Python AST and exact archive readbacks passed. Original decoder preserved, not executed because it launches replay.','localMathematicalOrNumericalReplay':False,'scope':'Author exact C618 own7/18/23weak000 changed-interface nonwinner, actual173/309/138; conditional support-segment/routing/centroid-cube exclusion. Not a smaller Gomboc or global minimum.','parentDigestClarification':'Reported cdfd... hashes the immutable parent JSON, while f8f5... hashes its exact66346-byte result_markdown. Both locally match; different serialization boundaries, not evidence of a coordinate conflict. Original PROVENANCE remains unchanged.','files':{n:{'bytes':len(b),'sha256':sha(b)}for n,b in outputs.items()}}
with(root/'integrity-receipt.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in receipt.items()if k!='files'}))
