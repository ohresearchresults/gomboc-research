import base64, hashlib, json, lzma, sys
from pathlib import Path
md = Path(sys.argv[1]).read_text(encoding='utf-8')
encoded = md.split('\nBEGIN_BQ13_CAPSULE\n', 1)[1].split('\nEND_BQ13_CAPSULE\n', 1)[0]
encoded = ''.join(encoded.split())
assert len(encoded) == 63500
assert hashlib.sha256(encoded.encode()).hexdigest() == 'fd17b83e231c8e9b3f4ef4dbc9acceeee583a414235012e8b8f0ff9c9e848b1f'
raw = lzma.decompress(base64.b85decode(encoded))
assert len(raw) == 223423
assert hashlib.sha256(raw).hexdigest() == 'e0d7ce4dea29c19075bc37fe667f005d186644296b618be5340c1437b020ea2a'
files = json.loads(raw)
assert len(files) == 37
root = Path(sys.argv[2])
root.mkdir(parents=True, exist_ok=False)
for name, text in files.items():
    relative = Path(name)
    assert not relative.is_absolute() and '..' not in relative.parts
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8'))
for name, expected in json.loads((root/'SOURCE_MANIFEST.json').read_text()).items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == expected
print('BQ13_COMPLETE_SOURCE_CAPSULE_RESTORED')
