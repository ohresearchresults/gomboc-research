import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_FINITE_CAP_'+'B64_BEGIN',1)[1].split('NH72_FINITE_CAP_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==35068
assert hashlib.sha256(u.encode()).hexdigest()=='da1b64945f3f80c622d10720596c27ab567bd5dd7fe152cde0aeadee4f03ec07'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==83582
assert hashlib.sha256(b).hexdigest()=='03f6c84c0dc60d90d2f5744646d1a855be12a796d1dd6fe5ef1131e00f9be087'
f=json.loads(b);assert len(f)==23
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    q=out/p;q.parent.mkdir(parents=True,exist_ok=True)
    q.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
