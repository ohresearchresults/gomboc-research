from pathlib import Path
import json,sys,numpy as np
from numeric import recover,mechanics,topology
from condition_events import merge_rechart
from atlas_opt import Atlas,optimize
R=Path(__file__).parent;g=json.loads((R/'greedy_h638/E318_try0_edge56_60_q17_GENERATOR.json').read_text());fs=json.loads((R/'greedy_h638/E318_try0_edge56_60_q17_faces.json').read_text());q=recover(g)[:137];r=mechanics(q,fs,details=True,tol=0);print('OLD',r['counts'],r['S'],r['U'],r['Hpolar'],flush=True);o,ef=topology(fs);P=r['P']
for dist,a,b in sorted((np.linalg.norm(P[a]-P[b]),a,b) for a,b in ef)[:3]:
 try:
  z,ff,depth=merge_rechart(g,fs,a,b);rr=mechanics(recover(z)[:137],ff,tol=0);print('CLOSED',dist,a,b,ef[a,b],rr,flush=True)
  tag=f'C{2*rr["E"]}_NEAR_NONWINNER_{a}_{b}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')))
  if rr['counts']==[1,1,0] and rr['min_gap']>1e-10:print('NEAR_NUMERIC_WINNER',tag,flush=True);break
  if rr['min_gap']>1e-10:
   m=Atlas(z,ff);m.checkpoint=R/(tag+'_REPAIR_CURRENT');u,st,status=optimize(m,steps=250,keep=1e-6,goal=1e-5);nz=m.save(u,R/(tag+'_REPAIR_GENERATOR.json'));rs=mechanics(recover(nz)[:137],ff,tol=0);print('REPAIRED',tag,status,rs,flush=True)
 except Exception as e:print('CLOSE_ERROR',a,b,repr(e),flush=True)
