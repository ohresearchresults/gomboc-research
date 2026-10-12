import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_S8_'+'B64_BEGIN',1)[1].split('NH72_S8_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==44392
assert hashlib.sha256(u.encode()).hexdigest()=='90696271f17317024576b1d7b5ad4e9f094ed1577188abe28f4080e1c4263962'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==118588
assert hashlib.sha256(b).hexdigest()=='3ac9a8a2ab883259d9e40753b5d48ba8ce544450d161ebbed5a85cd83a76fe53'
f=json.loads(b);assert len(f)==28
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    target=out/p;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
