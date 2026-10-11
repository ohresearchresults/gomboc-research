from pathlib import Path
import json,numpy as np
from numeric import *
from condition_events import merge_rechart
R=Path(__file__).parent;g=json.loads((R/'coarsening_v2/E322_try7_edge162_186_q86_GENERATOR.json').read_text());fs=json.loads((R/'coarsening_v2/E322_try7_edge162_186_q86_faces.json').read_text());q=recover(g)[:137];r=mechanics(q,fs,details=True,tol=1e-12);owners,ef=topology(fs);H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines())
print('C644',{k:v for k,v in r.items() if not isinstance(v,np.ndarray) and k!='owners'})
for dist,a,b in sorted((np.linalg.norm(r['P'][a]-r['P'][b]),a,b) for a,b in ef)[:15]:
 print('edge',a,b,ef[a,b],dist,'protected',tuple(sorted(ef[a,b])) in H,flush=True)
 if dist>1e-5:continue
 try:
  z,ff,depth=merge_rechart(g,fs,a,b);audit=mechanics(recover(z)[:137],ff,tol=1e-11);print('MERGED',depth,audit,flush=True)
  tag=f'C642_CONTACT_{a}_{b}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(audit,indent=2))
 except Exception as e:print('ERROR',repr(e),flush=True)
