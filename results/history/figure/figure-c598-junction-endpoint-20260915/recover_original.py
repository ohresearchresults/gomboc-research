import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==12685 and hashlib.sha256(s.encode()).hexdigest()=='26908efcc8c8e339049eb136153ab50b65ee408ebc6e5d2520ebc150ec1356d2'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==30459 and hashlib.sha256(b).hexdigest()=='31504bae5b7e5e19949e7657b05d385fbae1ed2ed4549019819d40045c57f2ee'
d=json.loads(b);assert len(d)==9
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=False)
for n,t in d.items():
 assert Path(n).name==n
 (root/n).write_bytes(t.encode())
for n,r in json.loads(d['SOURCE_MANIFEST.json']).items():
 q=(root/n).read_bytes()
 assert len(q)==r['bytes'] and hashlib.sha256(q).hexdigest()==r['sha256']
print('C598_JUNCTION_AND_ENDPOINT_SOURCES_RECOVERED')
