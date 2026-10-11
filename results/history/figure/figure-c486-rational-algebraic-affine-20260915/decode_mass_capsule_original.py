import base64,hashlib,json,sys,zlib
from pathlib import Path
assert __debug__
assert len(sys.argv)==4
sha=lambda b:hashlib.sha256(b).hexdigest()
a=b''.join(Path(sys.argv[1]).read_bytes().split())
b=b''.join(Path(sys.argv[2]).read_bytes().split())
assert len(a)==7200 and sha(a)=='2bcace8eff917f80c274b3fa2426d39be3388f82fe0c00289abdc06954d9ad66'
assert len(b)==7174 and sha(b)=='c746ca828d29e3413633d61e2bac5114380463476cda64664245bb708105994c'
encoded=a+b
assert sha(encoded)=='719d9f2c5b9eb068bb3c7be9f0a987717397667ba17c0dd4c4815cdb9c9df1ff'
raw=zlib.decompress(base64.b85decode(encoded))
assert len(raw)==29649 and sha(raw)=='57ca2d325f2ae5d50a0857321d32bfc71216977c6ddbd9cb33259ff973508f6d'
files=json.loads(raw);assert len(files)==8
out=Path(sys.argv[3]);out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 assert Path(name).name==name and name not in ('.','..')
 (out/name).write_bytes(text.encode('utf-8'))
for name,spec in json.loads((out/'MANIFEST.json').read_bytes()).items():
 data=(out/name).read_bytes()
 assert len(data)==spec['bytes'] and sha(data)==spec['sha256']
print('C486_MASS_CAPSULE_ALL_EIGHT_SOURCE_FILES_RESTORED')
