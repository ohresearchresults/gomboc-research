import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text(encoding='ascii').split())
assert len(s)==41775
assert hashlib.sha256(s.encode()).hexdigest()=='9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==112244
assert hashlib.sha256(b).hexdigest()=='75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360'
files=json.loads(b);assert len(files)==26
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
    rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
    p=out/rel;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
for name,w in json.loads((out/'MANIFEST.json').read_bytes()).items():
    data=(out/name).read_bytes()
    assert len(data)==w['bytes'] and hashlib.sha256(data).hexdigest()==w['sha256']
print('ATLAS57_26_EXACT_SOURCES_RESTORED')
