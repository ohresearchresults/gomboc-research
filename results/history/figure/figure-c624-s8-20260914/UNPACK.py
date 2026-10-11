"""Restore the complete exact construction, numerical methods and inputs."""
import sys,json,base64,lzma,hashlib
from pathlib import Path
if not __debug__:raise RuntimeError('Do not disable assertions.')
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==59100 and hashlib.sha256(s.encode()).hexdigest()=='e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==170010 and hashlib.sha256(b).hexdigest()=='44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3'
d=json.loads(b);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for n,t in d.items():
 p=Path(n);assert not p.is_absolute() and '..' not in p.parts
 p=out/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.encode())
for n,m in json.loads(d['SOURCE_MANIFEST.json']).items():
 x=(out/n).read_bytes();assert len(x)==m['bytes'] and hashlib.sha256(x).hexdigest()==m['sha256']
print('C624_STRONG_G8_SOURCE_RESTORED',len(d))
