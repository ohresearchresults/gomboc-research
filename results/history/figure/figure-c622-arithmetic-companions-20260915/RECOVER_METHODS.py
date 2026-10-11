"""Recover 26 exact files for the finite C622 arithmetic experiments."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
assert __debug__,'Assertions must be enabled'
assert len(sys.argv)==3,'Usage: RECOVER_METHODS.py PARTS_DIRECTORY NEW_OUTPUT'
root,out=map(Path,sys.argv[1:]);sha=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for i,n,h in [(1,8500,'bfc511d13e061def6efcd1936012dedb67316f9ae03da5d8ea7495a6e20a7421'),(2,8460,'29fa3aeea9e39fcd63e9ded230d879d4f8bf404ba39f5356cb59383fee26b31f')]:
 b=''.join((root/f'METHODS_PART_{i}.b85').read_text(encoding='ascii').split()).encode()
 assert len(b)==n and sha(b)==h,(i,len(b),sha(b));parts.append(b)
b=b''.join(parts);assert len(b)==16960 and sha(b)=='d39b8bad6d29b22591c97c018132352a132d2c35c638f281869a82ec8a69b0fb'
b=lzma.decompress(base64.b85decode(b));assert len(b)==48930 and sha(b)=='ef1a7d9b1b74103a8c57b91b813138a59964d467f8ca4314df15e8bf501ac444'
files=json.loads(b);assert len(files)==26
m=files['MANIFEST.json'].encode();assert len(m)==3158 and sha(m)=='17efa7d4b8a0b9ccc5d300688bb44c61e9865bd1da9678e9369e097c772a456f'
manifest=json.loads(m);assert set(manifest)==set(files)-{'MANIFEST.json'}
for name,spec in manifest.items():
 b=files[name].encode();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
 p=out/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
print('C622_ARITHMETIC_26FILE_METHODS_RECOVERY_PASS')
