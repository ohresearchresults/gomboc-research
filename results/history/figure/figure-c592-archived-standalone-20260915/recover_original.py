import base64,hashlib,json,lzma,sys
from pathlib import Path
assert __debug__
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==22135
assert hashlib.sha256(s.encode()).hexdigest()=='baa721987301f1e98461c4e8999fd4201163980de29f7b680205137fbe16c0a3'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==52421
assert hashlib.sha256(b).hexdigest()=='8686b63287f9433354e64656e0a0fc069558c8a4588ccc6cf9056f8a6c685d86'
d=json.loads(b);assert len(d)==12
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name
 (root/name).write_bytes(text.encode())
for name,m in json.loads(d['EXPECTED.json'])['sources'].items():
 data=(root/name).read_bytes()
 assert len(data)==m['bytes'] and hashlib.sha256(data).hexdigest()==m['sha256']
print('COORD_C592_SOURCE_CAPSULE_RECOVERED',len(d))
