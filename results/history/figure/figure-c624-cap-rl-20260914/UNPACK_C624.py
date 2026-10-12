import sys,json,lzma,base64,hashlib
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==15935 and hashlib.sha256(s.encode()).hexdigest()=='e494943aec3ecc12589b2c900a3b1d09ae61fd2edf58670df37a47adfc969730'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==37489 and hashlib.sha256(b).hexdigest()=='481ab0d864b0fc208b0e97f98e2678018a6956b7ae86b8504bf0b97ba1ee628d'
d=json.loads(b);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for f,t in d.items():
 p=out/f;assert not Path(f).is_absolute() and '..' not in Path(f).parts
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.encode())
for f,m in json.loads(d['MANIFEST.json']).items():
 x=(out/f).read_bytes();assert len(x)==m['bytes'] and hashlib.sha256(x).hexdigest()==m['sha256']
print('C624_SOURCE_CAPSULE_OK',len(d))
