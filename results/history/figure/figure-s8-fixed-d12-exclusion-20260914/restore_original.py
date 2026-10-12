from pathlib import Path
import base64,lzma,json,hashlib
s=''.join(Path('CATALOG_CAPSULE.b85').read_text().split())
assert len(s)==9130 and hashlib.sha256(s.encode()).hexdigest()=='f2b291ed0f7b97e9877995dab6a855b5f063e417c4e02405553f51ee3da76b8b'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==21269 and hashlib.sha256(b).hexdigest()=='996a73bcfc3480d6fe99d73de89e9b49f07198b0cc8fda2dff9222ce4c91695f'
p=Path('D12_SOURCE');p.mkdir(exist_ok=False)
for n,t in json.loads(b).items():
 assert Path(n).name==n
 (p/n).write_bytes(t.encode())
