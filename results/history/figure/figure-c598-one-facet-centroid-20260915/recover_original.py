import base64,hashlib,json,lzma,sys
from pathlib import Path
if not __debug__:raise RuntimeError('Run with assertions enabled')
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==18505 and hashlib.sha256(s.encode()).hexdigest()=='4d1641e75f5203290850778adade56a2e69fe594d04a76860e3c39a9ba4e2590'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==46051 and hashlib.sha256(b).hexdigest()=='1370cbde8a0dcfc72a736edbcd7c25cf0b9864749442ffa3a5eb4cb2c3a72872'
d=json.loads(b);assert len(d)==9
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name
 (root/name).write_bytes(text.encode())
for name,r in json.loads(d['EXPECTED.json'])['sources'].items():
 q=(root/name).read_bytes()
 assert len(q)==r['bytes'] and hashlib.sha256(q).hexdigest()==r['sha256']
print('ONE_FACET_SOURCE_PATCH_RECOVERED',len(d))
