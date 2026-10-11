"""Reconstruct the persisted S8 and a literal support-deletion family."""
import sys,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'source'))
import REPLAY,RECONSTRUCT
R=Path(__file__).resolve().parent
D=REPLAY.generator('S8'); raw=RECONSTRUCT.recover(D)
def dump(p,x):p.write_bytes(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
for deleted in (None,99,117,84):
 out=R/('S8' if deleted is None else 'DEL'+str(deleted));out.mkdir(exist_ok=True)
 ids=[i for i in range(137) if i!=deleted]
 d=dict(D);d['active_ids']=ids
 dump(out/'GENERATOR.json',d);dump(out/'raw.json',dict(H=[raw['H'][i] for i in ids]));dump(out/'active_ids.json',ids)
 print(out.name,len(ids),hashlib.sha256((out/'raw.json').read_bytes()).hexdigest())
