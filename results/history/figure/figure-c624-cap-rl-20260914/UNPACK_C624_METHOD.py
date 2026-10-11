import sys,json,lzma,base64,hashlib
from pathlib import Path
hs=['22c07b987203ecfc9d00fb07fdce8739f330eca4accb353662451fea4aef204d','bd8b9156006ba091262c32010693769a91b0c5b8589fb74164d8ecf337ba9520','218af253bac92004536c802f567d5d7fa712501a6de571f08bfda08093930b13']
parts=[''.join(Path(p).read_text().split()) for p in sys.argv[1:4]]
assert len(parts)==3
for s,n,h in zip(parts,[9360,9360,8780],hs):
 assert len(s)==n and hashlib.sha256(s.encode()).hexdigest()==h
s=''.join(parts)
assert len(s)==27500 and hashlib.sha256(s.encode()).hexdigest()=='54410efa57199a39e8061f22c5097cc66b224b5c4b7869c749cadbaf1be5985b'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==74277 and hashlib.sha256(b).hexdigest()=='0f168fd265ce4ed15626ec13105c0b8ec4ff58517b8c4897e61ee02911157d96'
d=json.loads(b);out=Path(sys.argv[4]);out.mkdir(parents=True,exist_ok=False)
for f,t in d.items():
 assert not Path(f).is_absolute() and '..' not in Path(f).parts
 p=out/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.encode())
for f,m in json.loads(d['MANIFEST.json']).items():
 x=(out/f).read_bytes();assert len(x)==m['bytes'] and hashlib.sha256(x).hexdigest()==m['sha256']
print('C624_METHOD_SOURCE_CAPSULE_OK',len(d))
