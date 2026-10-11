"""Sequential true-contact homotopy in the full own-centred physical atlas.
Records here are only numerical until the separate exhaustive exact replay.
"""
from pathlib import Path
import json,time,numpy as np,sys,itertools
from atlas_opt import Atlas,optimize
from numeric import recover,mechanics,topology,merge_faces
from condition_events import merge_rechart

def run(startgen,startfaces,outdir,epochs=20,tries=12,steps=350):
 R=Path(__file__).parent;out=Path(outdir);out.mkdir(exist_ok=True,parents=True);g=json.loads(Path(startgen).read_text());fs=json.loads(Path(startfaces).read_text());H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines());ledger=[];t0=time.time()
 for epoch in range(epochs):
  m=Atlas(g,fs);base=m.state(m.u0);E=len(m.ef);start_audit=mechanics(recover(g)[:137],fs,tol=1e-11);assert start_audit['counts']==[1,1,0] and base['vals'].min()>0;print('HOMOTOPY_EPOCH',epoch,'E',E,'mincos',base['vals'].min(),'elapsed',round(time.time()-t0,2),flush=True)
  if E<=249:print('HOMOTOPY_E249_NUMERIC',flush=True);return
  rank=[]
  for (a,b),pol in m.ef.items():
   if tuple(sorted(pol)) in H or m.Uroot in (a,b):continue
   try:merge_faces(fs,a,b)
   except Exception:continue
   candidates=[(v,j) for v,w in ((a,b),(b,a)) for j in set(m.owners[w])-set(m.owners[v])]
   if not candidates:continue
   target=min(candidates,key=lambda p:base['gaps'][p]/np.linalg.norm(base['q'][p[1]]));distance=base['gaps'][target]/np.linalg.norm(base['q'][target[1]]);length=np.linalg.norm(base['P'][a]-base['P'][b]);rank.append((length,a,b,target,pol,distance))
  rank.sort();print('HOMOTOPY_CANDIDATES',[(a,b,pol,float(length),float(dis)) for length,a,b,target,pol,dis in rank[:tries]],flush=True);success=False
  for ri,(length,a,b,target,pol,distance) in enumerate(rank[:tries]):
   keep=max(5e-7,min(5e-6,base['vals'].min()*.45));print('HOMOTOPY_TRY',ri,a,b,pol,target,'keep',keep,flush=True)
   try:u,st,status=optimize(m,steps=steps,target=target,trust=.0003,keep=keep,goal=.001)
   except Exception as exc:print('HOMOTOPY_ERROR',repr(exc),flush=True);continue
   prefix=f'E{E}_epoch{epoch}_try{ri}_{a}_{b}';z=m.save(u,out/(prefix+'_GENERATOR.json'));(out/(prefix+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')));rr=mechanics(recover(z)[:137],fs,tol=1e-11);row=dict(epoch=epoch,sourceE=E,edge=[a,b],polar=pol,target=target,status=status,gap=float(st['gaps'][target]),census=rr);ledger.append(row);(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));print('HOMOTOPY_TARGET_END',row,flush=True)
   nearest=sorted((np.linalg.norm(st['P'][v]-st['P'][w]),v,w) for v,w in m.ef)
   for dist,v,w in nearest[:8]:
    if dist>.001 or tuple(sorted(m.ef[v,w])) in H:continue
    try:
     zz,ff,depth=merge_rechart(z,fs,v,w,controls=st['X']);new=mechanics(recover(zz)[:137],ff,tol=1e-11);print('HOMOTOPY_MERGE',v,w,dist,depth,new,flush=True)
     if new['counts']==[1,1,0] and new['min_gap']>1e-10 and new['max_incidence_error']<1e-8 and min(new['polar_escape_min'],new['primal_escape_min'])>1e-7:
      tag=f'C{2*new["E"]}_HOMOTOPY_{epoch}_{v}_{w}';(out/(tag+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')));(out/(tag+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')));(out/(tag+'_numeric.json')).write_text(json.dumps(dict(removed_polar=m.ef[v,w],**new),indent=2));g=zz;fs=ff;success=True
      (out/'LATEST_GENERATOR.json').write_text(json.dumps(g,sort_keys=True,separators=(',',':')));(out/'LATEST_faces.json').write_text(json.dumps(fs,separators=(',',':')));print('HOMOTOPY_NUMERIC_WINNER',tag,flush=True);break
    except Exception as exc:print('HOMOTOPY_MERGE_ERROR',v,w,repr(exc),flush=True)
   if success:break
  if not success:print('HOMOTOPY_STOP_NO_NEXT',flush=True);return
 print('HOMOTOPY_EPOCH_BUDGET',flush=True)

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('generator');p.add_argument('faces');p.add_argument('outdir');p.add_argument('--epochs',type=int,default=20);p.add_argument('--tries',type=int,default=12);p.add_argument('--steps',type=int,default=350);a=p.parse_args();run(a.generator,a.faces,a.outdir,a.epochs,a.tries,a.steps)
