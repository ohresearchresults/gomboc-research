from pathlib import Path
import json,sys,hashlib
p=Path(sys.argv[1]);q=Path(sys.argv[2]);d=json.loads(p.read_text());del d["cases"];b=json.dumps(d,sort_keys=True,separators=(",",":")).encode();assert len(b)==11400 and hashlib.sha256(b).hexdigest()=="26f47d10d1958c1bf21538dd070fb51982520fff1a4314bf9e84fde22434208e";q.write_bytes(b);print("CATALOG_REGENERATED_PASS")
