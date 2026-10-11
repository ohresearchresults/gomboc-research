import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==25865
assert hashlib.sha256(s.encode()).hexdigest()=='ec0ad716235628338a7c3c6d371de170e30bd6184ae039c9b13eff096984c929'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==71405
assert hashlib.sha256(b).hexdigest()=='50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19'
d=json.loads(b);assert len(d)==16
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name
 (root/name).write_bytes(text.encode())
for name,r in json.loads(d['CORE_MANIFEST.json']).items():
 q=(root/name).read_bytes()
 assert len(q)==r['bytes'] and hashlib.sha256(q).hexdigest()==r['sha256']
print('FOUR_FRONTIERS_EXACT_CORE_RECOVERED',len(d))
