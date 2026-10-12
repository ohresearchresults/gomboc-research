from pathlib import Path
from hashlib import sha256
import base64,lzma,json,re
assert __debug__
s=Path('CAPSULE.md').read_text(encoding='utf-8')
parts=[]
for i in range(1,9):
 a='CAPSULE_PART_'+str(i)+'_BEGIN'
 b='CAPSULE_PART_'+str(i)+'_END'
 assert s.count(a)==s.count(b)==1
 parts.append(''.join(s.split(a,1)[1].split(b,1)[0].split()))
e=''.join(parts).encode('ascii')
assert len(e)==70520 and sha256(e).hexdigest()=='6b03a1cca45201b01290d7ac5a9203474f7d7dffc1da1c4be01fb5cc76461405'
b=lzma.decompress(base64.b64decode(e,validate=True))
assert len(b)==298453 and sha256(b).hexdigest()=='f8cef59a1664795f9ae5ba5434fc3cd6dcad9280a8011e4d4738aed217cb3cd4'
d=json.loads(b);assert len(d)==74
root=Path('F49_50_SOURCE');root.mkdir(exist_ok=False)
for k,v in d.items():
 q=Path(k);assert not q.is_absolute() and '..' not in q.parts
 p=root/q;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(v,encoding='utf-8')
for k,r in json.loads((root/'SOURCE_MANIFEST.json').read_text()).items():
 z=(root/k).read_bytes();assert len(z)==r['bytes'] and sha256(z).hexdigest()==r['sha256']
print('F49_50_COMPLETE_SOURCE_CAPSULE_DECODED')
