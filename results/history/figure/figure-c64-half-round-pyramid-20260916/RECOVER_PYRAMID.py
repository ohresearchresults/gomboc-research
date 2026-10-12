import base64,hashlib,json,lzma,sys
from pathlib import Path,PurePosixPath
assert __debug__
b=b''.join(Path(sys.argv[1]).read_bytes().split())
assert len(b)==41630 and hashlib.sha256(b).hexdigest()=='5b7b03d281f7043916ff07230aa8e78bf646b98bdd471934ab672aea81f32e9a'
r=lzma.decompress(base64.b85decode(b))
assert len(r)==112610 and hashlib.sha256(r).hexdigest()=='b4febc9d9e7ad0f8e2e9e67ac1aeae4a5fd1fad9d524a94da9ea6cd7daaeb637'
d=json.loads(r);assert len(d)==28
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for n,t in d.items():
 q=PurePosixPath(n);assert not q.is_absolute() and '..' not in q.parts
 p=out/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.encode('utf-8'))
for sub,m in [('exact','SOURCE_MANIFEST.json'),('numerical','NUMERICAL_MANIFEST.json')]:
 for n,s in json.loads((out/sub/m).read_bytes()).items():
  x=(out/sub/n).read_bytes();assert len(x)==s['bytes'] and hashlib.sha256(x).hexdigest()==s['sha256']
print('PYRAMID28_COMPLETE_SOURCES_AND_CHECKPOINTS_RESTORED')
