"""Recover the complete finite 42-denominator C622 screen capsule."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
assert __debug__,'Assertions must be enabled'
assert len(sys.argv)==3,'Usage: RECOVER_FACTORED_SCREEN.py PARTS_DIRECTORY NEW_OUTPUT'
root,out=map(Path,sys.argv[1:]);sha=lambda b:hashlib.sha256(b).hexdigest();parts=[]
for i,n,h in [(1,6750,'7fbbfe1800efa853721cc8995b609df7b8edce254b9264d2a8c13c60021b9531'),(2,6700,'f361c2597c46ea34485bc423807c21284e23610591548125325cbd6780c24af4')]:
 b=''.join((root/f'PART_{i}.b85').read_text(encoding='ascii').split()).encode()
 assert len(b)==n and sha(b)==h,(i,len(b),sha(b));parts.append(b)
b=b''.join(parts);assert len(b)==13450 and sha(b)=='dc9db9eadd523ddae4b808302c52e012f8dae64f0cc5ae6b4b5e0d0315f8d8f4'
b=lzma.decompress(base64.b85decode(b));assert len(b)==42238 and sha(b)=='f70e75bcd87255d3b3566200013d180a6cac129761e98ebb93e3864adcad944c'
files=json.loads(b);assert len(files)==47
m=files['MANIFEST.json'].encode();assert len(m)==5917 and sha(m)=='0be14448f5f963f8a2c6b98712fb65189b4f5d409d4609028aba2796f7284cc7'
manifest=json.loads(m);assert set(manifest)==set(files)-{'MANIFEST.json'}
for name,spec in manifest.items():
 b=files[name].encode();assert len(b)==spec['bytes'] and sha(b)==spec['sha256'],name
out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
 p=out/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
print('C622_FACTORED_SCREEN_47FILE_RECOVERY_PASS')
