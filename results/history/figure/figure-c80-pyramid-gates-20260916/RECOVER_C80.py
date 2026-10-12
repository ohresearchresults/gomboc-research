import base64,hashlib,json,sys,zlib
from pathlib import Path,PurePosixPath
spec={
 'exact':(18184,'0288a5d5270903ed2d68a568c3b7b51df6583dc8629bc6e652f887e3e31cd7a8',40141,'aa445774cd849878f912eb8356986699e44d56d4a4f5f61ed4507fd46e16c6ee',11),
 'numerical':(19245,'7dfefaa04166f1a073f11e6854b42111a94adfeb4371f9a1c56e073874319bab',41498,'0c98e0d793ff5c4b916ee37399bda99678c9222bf6acc59ee0b55805ff1f57e7',6)
}
kind,payload,destination=sys.argv[1:]
n,hs,m,hr,count=spec[kind]
s=''.join(Path(payload).read_text(encoding='ascii').split())
assert len(s)==n and hashlib.sha256(s.encode()).hexdigest()==hs
b=zlib.decompress(base64.b85decode(s))
assert len(b)==m and hashlib.sha256(b).hexdigest()==hr
files=json.loads(b);assert len(files)==count
root=Path(destination);root.mkdir(parents=True,exist_ok=False)
for name,text in sorted(files.items()):
 p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts
 out=root/name;out.parent.mkdir(parents=True,exist_ok=True)
 out.write_bytes(text.encode('utf-8'))
 print(name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
print('C80_CAPSULE_DECODE_PASS',kind,count)
