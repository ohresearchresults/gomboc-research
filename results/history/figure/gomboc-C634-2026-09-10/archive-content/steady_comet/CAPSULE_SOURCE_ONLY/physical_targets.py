"""Direct physical contact closure with every currently correct escape protected.
This explores full rational contact-atlas coordinates, including the filled centroid.
"""
from pathlib import Path
import numpy as np,json,time,sys
from atlas_opt import Atlas,optimize
from numeric import recover,mechanics,topology
from condition_events import merge_rechart
R=Path(__file__).parent
g=json.loads((R/'C642_Q7_AS_D12_GENERATOR.json').read_text());fs=json.loads((R/'C642_QGRID_D10000000_faces.json').read_text());m=Atlas(g,fs);base=m.state(m.u0);rank=[]
for (a,b),pol in m.ef.items():
    length=np.linalg.norm(base['P'][a]-base['P'][b]);targets=[(v,j) for v,w in ((a,b),(b,a)) for j in set(m.owners[w])-set(m.owners[v])]
    if not targets:continue
    tg=min(targets,key=lambda p:base['gaps'][p]/np.linalg.norm(base['q'][p[1]]))
    rank.append((length,a,b,tg,pol))
rank.sort();ledger=[]
for length,a,b,target,pol in rank[:12]:
    print('PHYSICAL_TARGET',a,b,pol,'length',length,'target',target,'gap',base['gaps'][target],flush=True)
    u,st,status=optimize(m,steps=260,target=target,trust=.0005,keep=7e-6,goal=.001)
    prefix=f'PHYS_TARGET_{a}_{b}';z=m.save(u,R/(prefix+'_GENERATOR.json'));(R/(prefix+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')))
    rr=mechanics(recover(z)[:137],fs,tol=1e-11);entry=dict(edge=[a,b],polar=pol,target=target,status=status,remaining_gap=float(st['gaps'][target]),census=rr);ledger.append(entry);(R/'PHYS_TARGET_LEDGER.json').write_text(json.dumps(ledger,indent=2));print('PHYSICAL_TARGET_END',entry,flush=True)
    nearest=sorted((np.linalg.norm(st['P'][v]-st['P'][w]),v,w) for v,w in m.ef)
    for dist,v,w in nearest[:8]:
        if dist>0.005:break
        try:
            zz,ff,depth=merge_rechart(z,fs,v,w,controls=st['X']);new=mechanics(recover(zz)[:137],ff,tol=1e-10);print('TARGET_MERGE',v,w,dist,depth,new,flush=True)
            if new['counts']==[1,1,0] and new['min_gap']>1e-10 and min(new['polar_escape_min'],new['primal_escape_min'])>1e-6:
                tag=f'C{2*new["E"]}_PHYSICAL_{v}_{w}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(R/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(new,indent=2));print('PHYSICAL_CONTACT_NUMERIC_WINNER',tag,flush=True);sys.exit(0)
        except Exception as exc:print('TARGET_MERGE_FAIL',v,w,str(exc),flush=True)
