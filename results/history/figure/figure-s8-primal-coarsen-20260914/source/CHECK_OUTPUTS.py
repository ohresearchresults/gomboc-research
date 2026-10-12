from pathlib import Path
import json,sys,hashlib
r=Path(sys.argv[1]);e=json.loads(Path(sys.argv[2]).read_text())
for n,v in e.items():
 b=(r/n).read_bytes();assert len(b)==v["bytes"] and hashlib.sha256(b).hexdigest()==v["sha256"],n
print("ALL_EXACT_ENDPOINT_OUTPUTS_MATCH",len(e))
