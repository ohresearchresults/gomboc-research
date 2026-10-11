import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text().split())
assert len(s)==7095 and hashlib.sha256(s.encode()).hexdigest()=='f9ee5fc1060be31f8694da3c1bab3ef93c24ee992f2a2149db65a2ebce758c26'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==15925 and hashlib.sha256(b).hexdigest()=='57d0644b73858349341fad8f3f55fd83a00c4485efef5d0cdc49afb9b5a16320'
d=json.loads(b);assert len(d)==6
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=False)
for n,t in d.items():
 assert Path(n).name==n
 (root/n).write_bytes(t.encode())
for n,r in json.loads(d['MANIFEST.json']).items():
 q=(root/n).read_bytes()
 assert len(q)==r['bytes'] and hashlib.sha256(q).hexdigest()==r['sha256']
print('C592_EXPOSED_CHAIN_SOURCE_RECOVERED')
