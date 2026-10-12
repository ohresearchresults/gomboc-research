"""Decode exact source transport without running the mathematical programs."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import re

root=Path(__file__).resolve().parent
def sha(data):return hashlib.sha256(data).hexdigest()
def check(data,size,digest):
    if len(data)!=size or sha(data)!=digest:raise ValueError('Integrity pin differs')
    return data
raw=check((root/'result.json').read_bytes(),62962,'7e8eda113c99db67ace3bff7aa33826a111440287005131cf80f9803a973b359')
md=json.loads(raw)['result_markdown']
check(md.encode(),62668,'d9a951e519d769bfd6f9f5dbd1a7d24031014fcc10b13eebe9917743f20bcff0')
if (root/'result.md').read_bytes()!=md.encode():raise ValueError('Markdown readback differs')
start,end='\nNH72_FINITE_CAP_B64_BEGIN\n','\nNH72_FINITE_CAP_B64_END'
if md.count(start)!=1 or md.count(end)!=1:raise ValueError('Ambiguous capsule')
capsule=check(''.join(md.split(start)[1].split(end)[0].split()).encode(),35068,'da1b64945f3f80c622d10720596c27ab567bd5dd7fe152cde0aeadee4f03ec07')
decoder=lzma.LZMADecompressor(memlimit=134217728)
decoded=decoder.decompress(base64.b64decode(capsule,validate=True),max_length=83583)
if not decoder.eof or decoder.unused_data:raise ValueError('Unexpected compressed extent')
files=json.loads(check(decoded,83582,'03f6c84c0dc60d90d2f5744646d1a855be12a796d1dd6fe5ef1131e00f9be087'))
if not isinstance(files,dict) or len(files)!=23:raise ValueError('Unexpected file count')
for name,text in files.items():
    p=PurePosixPath(name)
    if not isinstance(text,str) or not p.parts or p.is_absolute() or '..' in p.parts or '\\' in name or str(p)!=name:raise ValueError('Unsafe path')
    if name.endswith('.py'):ast.parse(text,filename=name)
    elif name.endswith('.json'):json.loads(text)
manifest=json.loads(files['MANIFEST.json'])
if set(manifest)!=set(files)-{'MANIFEST.json'}:raise ValueError('Incomplete manifest')
for name,pin in manifest.items():check(files[name].encode(),pin['bytes'],pin['sha256'])
restore=re.findall(r'^```python\n(.*?)^```\s*$',md,re.M|re.S)
if len(restore)!=1:raise ValueError('Ambiguous original decoder')
ast.parse(restore[0])
payloads={'source/'+name:text.encode() for name,text in files.items()}
payloads.update({'restore_original.py':restore[0].encode(),'SOURCE_CAPSULE.b64':capsule})
for name in [*payloads,'integrity-receipt.json']:
    if (root/name).exists():raise FileExistsError(root/name)
for name,data in payloads.items():
    p=root/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f:f.write(data)
    check(p.read_bytes(),len(data),sha(data))
# Clarify the author's parent-hash warning without altering the original result.
old=root.parent/'figure-nh72-s8-c618-projective-20260914'
parent_raw=check((old/'result.json').read_bytes(),73144,'c00d707b68ac1ed80be88960dad668969b21b25ef57afbd02f4bef9d22299ffb')
parent_md=json.loads(parent_raw)['result_markdown'].encode()
check(parent_md,72505,'0e08a04fc60eca3c02232781fa6c142c99609d2c0bc38a9981c35341b0147b55')
if (old/'result.md').read_bytes()!=parent_md:raise ValueError('Prior markdown differs')
receipt={'at':datetime.now(timezone.utc).isoformat(),'identity':'NH72_TWO_FINITE_CAP_COMPENSATORS','sourceFiles':23,'standalone':True,'completeSourcePreservedLocally':True,'localMathematicalOrNumericalReplay':False,
 'resultBytes':len(raw),'resultSha256':sha(raw),'markdownBytes':len(md.encode()),'markdownSha256':sha(md.encode()),
 'capsule':{'base64Chars':len(capsule),'base64Sha256':sha(capsule),'decodedBytes':len(decoded),'decodedSha256':sha(decoded)},
 'verification':'Immutable result, base64/decoded pins, all22 manifest entries, JSON/Python syntax and exact source readbacks passed. Original decoder preserved, not executed because it launches mathematical replay.',
 'scope':'PAIR99 rational and isolated-root algebraic variants C618 own929weak000; TRIPLE117 variants C616 own10/3/11weak000. Author finite exact moment closure, rational dual audits, algebraic all-feature interval proof, frozen-cone conditional exclusion and9 compensated conditional covers. None is a Gomboc; no global lower bound.',
 'parentDigestClarification':'Both previously preserved streams verify: advertised c00d... is73144-byte immutable version2 JSON;0e08... is exactly its72505-byte result_markdown. The differing digest is explained by different serialization boundaries, not corrupt geometry. New author PROVENANCE.json kept verbatim; clarification is monitor evidence, no mutation of result.',
 'limitations':'Monitor did not run mathematical replay or independently validate theorem logic. Two independent full hull enumerators apply to rational proxies, not the algebraic roots. No continuous compensation path or global minimum claimed.',
 'files':{name:{'bytes':len(data),'sha256':sha(data)} for name,data in payloads.items()}}
with (root/'integrity-receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
