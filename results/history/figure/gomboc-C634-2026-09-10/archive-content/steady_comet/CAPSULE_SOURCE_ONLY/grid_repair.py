"""Finite one-coordinate grid repair; no floating census is an exact promotion."""
from pathlib import Path
import json,time,numpy as np
from numeric import recover,mechanics
from atlas_opt import Atlas
R=Path(__file__).parent;g=json.loads((R/'C642_CONTACT26_82/GENERATOR.json').read_text());fs=json.loads((R/'C642_CONTACT26_82/A.json').read_text())['faces'];X=recover(g)
D=10**6;z=json.loads(json.dumps(g));z['grid']=D;z['controls']=[[int(round(t*D)) for t in row] for row in X];m=Atlas(z,fs);st=m.state(m.u0);initial=mechanics(recover(z)[:137],fs,tol=1e-12);print('GRID_INITIAL',initial,'bad',np.flatnonzero(st['vals']<0).tolist(),flush=True)
(R/'C642_GRID6_UNREPAIRED_GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
candidates=[]
for k,(i,c) in enumerate(m.free):
 for d in (-1,1):
  du=d/(D*m.scale[k]);v=st['vals']+st['J'][:,k]*du;candidates.append((float(v.min()),k,int(i),int(c),d))
candidates.sort(reverse=True);print('GRID_RANK',candidates[:10],flush=True);ledger=[]
for rank,(pred,k,i,c,d) in enumerate(candidates):
 zz=json.loads(json.dumps(z));zz['controls'][i][c]+=d
 try:rr=mechanics(recover(zz)[:137],fs,tol=1e-12)
 except Exception:continue
 ledger.append(dict(rank=rank,node=i,axis=c,delta=d,pred=pred,counts=rr['counts'],gap=rr['min_gap']))
 if rr['counts']==[1,1,0] and rr['min_gap']>1e-8 and min(rr['polar_escape_min'],rr['primal_escape_min'])>1e-6:
  tag=f'C642_GRID6_NODE{i}_AXIS{c}_DELTA{d}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(rr,indent=2));print('GRID_WINNER',tag,rr,flush=True);break
(R/'GRID6_REPAIR_LEDGER.json').write_text(json.dumps(ledger,indent=2))
