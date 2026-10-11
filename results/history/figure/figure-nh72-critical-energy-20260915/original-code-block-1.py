import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_CRITICAL_'+'B64_BEGIN',1)[1].split('NH72_CRITICAL_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==35896
assert hashlib.sha256(u.encode()).hexdigest()=='0a45fce544afa3efce761946508184e050a1a80cb31f122d2e582af52f3d4f2b'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==87442
assert hashlib.sha256(b).hexdigest()=='91a931bdc8b2470fad2b527b5455f2eaf5f1de62524aecb9c3d462f95d308152'
f=json.loads(b);assert len(f)==28
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    target=out/p;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
