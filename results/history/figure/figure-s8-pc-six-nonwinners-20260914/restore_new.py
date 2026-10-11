import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text(encoding='ascii').split())
assert len(s)==64470
assert hashlib.sha256(s.encode()).hexdigest()=='e182149c7c1c850dcecf423563b6d8815d391ca8cf4c52160fe04c19ebbebafd'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==300482
assert hashlib.sha256(b).hexdigest()=='91f5a9f8a543ea9d03481fc781618ddd35fc75b0f3f7836e8287a64ab92371c4'
f=json.loads(b);assert len(f)==73
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
    p=out/rel;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
for name,spec in json.loads((out/'NEW_MANIFEST.json').read_text()).items():
    data=(out/name).read_bytes()
    assert len(data)==spec['bytes']
    assert hashlib.sha256(data).hexdigest()==spec['sha256']
print('S8_PC_NEW_SOURCE_CAPSULE_RESTORED',len(f))
