import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_EXTERNAL_'+'B64_BEGIN',1)[1].split('NH72_EXTERNAL_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==36384
assert hashlib.sha256(u.encode()).hexdigest()=='45f6257619278cf1cf3a373047c86ab19b67679def04b82c60612d2ec61d8009'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==92706
assert hashlib.sha256(b).hexdigest()=='f5fba1517674ad24e05f3580f995fe3ac1868a4feb6bcea988a69c654d10e692'
f=json.loads(b);assert len(f)==31
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    q=out/p;q.parent.mkdir(parents=True,exist_ok=True)
    q.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
