import base64,hashlib,json,lzma,sys
from pathlib import Path,PurePosixPath
assert __debug__
payload=b''.join(Path(sys.argv[1]).read_bytes().split())
assert len(payload)==14965 and hashlib.sha256(payload).hexdigest()=='df26c74e6682eda0a53b523c9c589f38d81422874622d3e62498d1967bc47aab'
raw=lzma.decompress(base64.b85decode(payload))
assert len(raw)==33578 and hashlib.sha256(raw).hexdigest()=='76fe98c57b6ed4e43d65c6517a59600fddec429c01062f853f90aa941e44ce40'
files=json.loads(raw);assert len(files)==8
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 q=PurePosixPath(name);assert not q.is_absolute() and '..' not in q.parts
 p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
for name,spec in json.loads((out/'SOURCE_MANIFEST.json').read_bytes()).items():
 b=(out/name).read_bytes();assert len(b)==spec['bytes'] and hashlib.sha256(b).hexdigest()==spec['sha256']
print('UPDATE_EIGHT_COMPLETE_FILES_RESTORED')
