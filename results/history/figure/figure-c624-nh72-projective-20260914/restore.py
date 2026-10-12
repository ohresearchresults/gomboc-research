import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_PM_'+'B64_BEGIN',1)[1].split('NH72_PM_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==36464
assert hashlib.sha256(u.encode()).hexdigest()=='d06b4813e87a33dc14ed53897732882781874b3c22da71fe8ed9fbb2c36d395a'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==83135
assert hashlib.sha256(b).hexdigest()=='c3e1c908a17fb25744fb37323df081ec2d61cfc2b556489c341c8b94dc9a8017'
f=json.loads(b);assert len(f)==23
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    target=out/p;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
