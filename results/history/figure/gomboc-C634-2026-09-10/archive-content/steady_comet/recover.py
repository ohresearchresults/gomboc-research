from pathlib import Path
import re,base64,lzma,json,hashlib
s=Path('/mnt/data/research-journal(3).md').read_text()
root=Path(__file__).parent
p=s[s.index('# Clear Lynx 14 —'):]
(root/'immutable_parent.md').write_text(p)
print('parent text',hashlib.sha256(p.encode()).hexdigest(),len(p))
part=s[s.index('The following is the WHOLE seventeen-file'):]
b=re.search(r'```text\n(.*?)\n```',part,re.S).group(1)
b=''.join(b.split()); assert len(b)==19565
z=lzma.decompress(base64.b85decode(b)); assert hashlib.sha256(z).hexdigest()=='081ff87dc9dd54f14cba01f745b659c7bdd7f76dffac35b115a12f5ba4dc0048'
for k,v in json.loads(z).items():
 f=root/'parent650'/k; assert not Path(k).is_absolute() and '..' not in Path(k).parts
 f.parent.mkdir(parents=True,exist_ok=True);f.write_text(v)
for heading,name in [('## 7. Exact minimum','VERIFY_MIN213.py'),('## 8. Exact Tutte','BUILD_TUTTE_XY.py'),('## 9. Exact positive','REALIZE_AUDIT_H213.py')]:
 t=p[p.index(heading):]; code=re.search(r'```python\n(.*?)\n```',t,re.S).group(1)
 (root/name).write_text(code+'\n')
t=p[p.index('## 2. Exact minimum'):]; es=re.search(r'```text\n(.*?)\n```',t,re.S).group(1)+'\n'
assert hashlib.sha256(es.encode()).hexdigest()=='171a223c0e2ee52c36ba1076ec588d34aa056cc07efbde2f5d2c6104a805d911'
(root/'H213_edges.txt').write_text(es)
print('recovered',len(json.loads(z)), 'files')
