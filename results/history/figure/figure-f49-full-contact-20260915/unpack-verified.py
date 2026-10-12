import ast,base64,hashlib,json,lzma,re
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
root=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
mdbytes=(root/'RECOVERY_CAPSULE.md').read_bytes()
if len(mdbytes)!=75607 or sha(mdbytes)!='28263d55358694e4c45ad28ad5291582a8314d65b20bfbde161be6f79ceee3ff':raise ValueError('Downloaded capsule changed')
md=mdbytes.decode();parts=[]
for i in range(1,9):
 begin=f'\nCAPSULE_PART_{i}_BEGIN\n';end=f'\nCAPSULE_PART_{i}_END'
 if md.count(begin)!=1 or md.count(end)!=1:raise ValueError('Missing/duplicate part')
 parts.append(''.join(md.split(begin)[1].split(end)[0].split()).encode())
cap=b''.join(parts)
if len(cap)!=70520 or sha(cap)!='6b03a1cca45201b01290d7ac5a9203474f7d7dffc1da1c4be01fb5cc76461405':raise ValueError('Encoded capsule differs')
dec=lzma.LZMADecompressor(memlimit=134217728);raw=dec.decompress(base64.b64decode(cap,validate=True),max_length=298454)
if not dec.eof or dec.unused_data or len(raw)!=298453 or sha(raw)!='f8cef59a1664795f9ae5ba5434fc3cd6dcad9280a8011e4d4738aed217cb3cd4':raise ValueError('Decoded capsule differs')
files=json.loads(raw)
if len(files)!=74:raise ValueError('File count differs')
for n,t in files.items():
 p=PurePosixPath(n)
 if not isinstance(t,str)or not p.parts or p.is_absolute()or '..'in p.parts or chr(92)in n or str(p)!=n:raise ValueError('Unsafe path')
 if n.endswith('.py'):ast.parse(t,filename=n)
 elif n.endswith('.json'):json.loads(t)
manifest_bytes=files['SOURCE_MANIFEST.json'].encode()
if len(manifest_bytes)!=8737 or sha(manifest_bytes)!='a95d9e6df933a5ea481ccd9547308197018ed1aecd4e4ac099a10a71600997d1':raise ValueError('Manifest pin differs')
manifest=json.loads(manifest_bytes)
if set(manifest)!=set(files)-{'SOURCE_MANIFEST.json'}:raise ValueError('Incomplete manifest coverage')
for n,pin in manifest.items():
 b=files[n].encode()
 if len(b)!=pin['bytes']or sha(b)!=pin['sha256']:raise ValueError('File pin differs')
outputs={'source/'+n:t.encode()for n,t in files.items()};outputs['SOURCE_CAPSULE.b64']=cap
for i,code in enumerate(re.findall(r'^\x60\x60\x60python\n(.*?)^\x60\x60\x60',md,re.M|re.S),1):ast.parse(code);outputs[f'original-decoder-{i}.py']=code.encode()
for n in [*outputs,'integrity-receipt.json']:
 if(root/n).exists():raise FileExistsError(root/n)
for n,b in outputs.items():
 p=root/n;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb')as f:f.write(b)
 if p.read_bytes()!=b:raise ValueError('Readback differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'sourceFiles':74,'standalone':True,'completeSourcePreservedLocally':True,'localMathematicalReplay':False,'capsuleBytes':70520,'capsuleSha256':sha(cap),'decodedBytes':len(raw),'decodedSha256':sha(raw),'verification':'Downloaded file pin,8 parts, encoded/decoded pins,73 manifest entries, JSON/Python syntax and exact source readbacks verified. Scientific programs not executed.','scope':'Three author-exact C622 bodies, own41/61/100,42/61/101,65/76/139. Their separately prescribed reference points have110; these are NOT own-centroid Gombocs. Full74 sources now durable, not only sandbox links.','files':{n:{'bytes':len(b),'sha256':sha(b)}for n,b in outputs.items()}}
with(root/'integrity-receipt.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in receipt.items()if k!='files'}))
