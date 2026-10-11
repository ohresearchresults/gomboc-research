import base64, hashlib, json, lzma, sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text(encoding='ascii').split())
assert len(s)==30810
assert hashlib.sha256(s.encode()).hexdigest()=='4807ee686ca4052f1588bdc7d9356e212aaa5a34736e1b2e2688f756a30f35d4'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==93394
assert hashlib.sha256(b).hexdigest()=='35d4de0ce185e798c204c8a8c42cbadafe5d741ab590a435c54db24164017ab9'
f=json.loads(b)
assert len(f)==22
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    rel=Path(name)
    assert not rel.is_absolute() and '..' not in rel.parts
    p=out/rel;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
for name,spec in json.loads((out/'MANIFEST.json').read_text()).items():
    data=(out/name).read_bytes()
    assert len(data)==spec['bytes']
    assert hashlib.sha256(data).hexdigest()==spec['sha256']
print('ATLAS56_22_SOURCES_RESTORED')
