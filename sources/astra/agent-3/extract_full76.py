from pathlib import Path
import re,hashlib,json
root=Path('sources/FULL76');root.mkdir(exist_ok=True)
manifest={}
for p in sorted(Path('sources').glob('FULL76_READABLE_*.md')):
 data=p.read_bytes();pos=0
 while m:=re.search(rb'^FILE (\S+) (\d+) ([a-f0-9]{64})\n',data[pos:],re.M):
  start=pos+m.end();name=m[1].decode();count=int(m[2]);sha=m[3].decode();payload=data[start:start+count]
  assert hashlib.sha256(payload).hexdigest()==sha,(name,'hash mismatch')
  assert not Path(name).is_absolute() and '..' not in Path(name).parts
  out=root/name;out.parent.mkdir(exist_ok=True,parents=True);out.write_bytes(payload)
  manifest[name]={'bytes':count,'sha256':sha,'bundle':p.name};pos=start+count
assert len(manifest)==76,len(manifest)
(root/'EXTRACTION.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('EXTRACTED_AND_HASHED',len(manifest))
