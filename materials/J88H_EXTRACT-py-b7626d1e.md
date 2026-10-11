# material-b7626d1ef1a0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Extract all exact literal units from named J88H readable bundles.
Usage: python J88H_EXTRACT.py OUTPUT_DIRECTORY BUNDLE.md [BUNDLE.md ...]
Existing identical files are accepted; conflicting bytes fail without overwrite.
"""
import sys,json,hashlib
from pathlib import Path
if len(sys.argv)<3:raise SystemExit(__doc__)
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
count=0
for name in sys.argv[2:]:
 raw=Path(name).read_bytes();pos=0
 while True:
  begin=raw.find(b'<!-- BEGIN UNIT ',pos)
  if begin<0:break
  line_end=raw.index(b' -->\n',begin)
  meta=json.loads(raw[begin+16:line_end]);start=line_end+5
  end=raw.index(('<!-- END UNIT '+meta['name']+' -->').encode(),start)
  payload=raw[start:end]
  assert len(payload)==meta['bytes'] and hashlib.sha256(payload).hexdigest()==meta['sha256'],meta['name']
  dest=out/meta['name'];assert dest.parent==out,'unsafe filename'
  if dest.exists():assert dest.read_bytes()==payload,('conflicting source',dest)
  else:dest.write_bytes(payload)
  pos=end;count+=1
print('J88H_LITERAL_UNITS_EXTRACTED',count)
