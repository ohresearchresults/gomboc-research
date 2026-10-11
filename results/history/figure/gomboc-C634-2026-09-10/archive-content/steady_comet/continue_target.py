from pathlib import Path
import json,numpy as np
from atlas_opt import Atlas,optimize
from numeric import recover,mechanics
from condition_events import merge_rechart
R=Path(__file__).parent;g=json.loads((R/'PHYS_TARGET_140_141_GENERATOR.json').read_text());fs=json.loads((R/'PHYS_TARGET_140_141_faces.json').read_text());m=Atlas(g,fs)
u,st,status=optimize(m,steps=1600,target=(140,45),trust=.00005,keep=3e-6,goal=.001)
z=m.save(u,R/'PHYS_CONTINUE_140_141_GENERATOR.json');(R/'PHYS_CONTINUE_140_141_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('CONTINUE_FINISH',status,st['gaps'][140,45],st['vals'].min(),flush=True)
for dist,a,b in sorted((np.linalg.norm(st['P'][v]-st['P'][w]),v,w) for v,w in m.ef)[:12]:
 print('CONTINUE_CLOSEST',a,b,m.ef[a,b],dist,flush=True)
 if dist>.001:continue
 try:
  zz,ff,depth=merge_rechart(z,fs,a,b,controls=st['X']);rr=mechanics(recover(zz)[:137],ff,tol=1e-11);print('CONTINUE_MERGE',a,b,depth,rr,flush=True)
  if rr['counts']==[1,1,0] and rr['min_gap']>1e-9 and min(rr['polar_escape_min'],rr['primal_escape_min'])>2e-7:
   tag=f'C{2*rr["E"]}_TARGET_{a}_{b}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(rr,indent=2));print('CONTINUE_NUMERIC_WINNER',tag,flush=True)
 except Exception as e:print('CONTINUE_MERGE_ERROR',a,b,str(e),flush=True)
