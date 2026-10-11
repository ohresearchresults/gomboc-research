import re,sys,json,lzma,base64,hashlib
from pathlib import Path
text=Path(sys.argv[1]).read_text()
parts=re.findall(r'CAP_SLIDE_B64_([1-4])_BEGIN\n([A-Za-z0-9+/=\n]+)\nCAP_SLIDE_B64_\1_END',text)
assert len(parts)==4 and sorted(i for i,s in parts)==list('1234')
s=''.join(''.join(p.split()) for i,p in sorted(parts))
assert len(s)==47960 and hashlib.sha256(s.encode()).hexdigest()=='e749e6b45436636c172a725c058b729a098c4ef5213a1d2371c40282fe6d0417'
x=base64.b64decode(s,validate=True)
assert len(x)==35968 and hashlib.sha256(x).hexdigest()=='c96bee088ebad0e41c85ea44f1bb55e580ce1a65cd0b9379075581f9e10df021'
b=lzma.decompress(x)
assert len(b)==121552 and hashlib.sha256(b).hexdigest()=='ef0a76e229b1b640b2b186d8792bb5f2ac81093f54f7440ede5dddf40e34b117'
f=json.loads(b);assert len(f)==27
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,value in f.items():
 assert Path(name).name==name and name not in ('.','..')
 (out/name).write_text(value)
print('COORD_S8_CAP_SLIDE_27_SOURCES_RECOVERED')
