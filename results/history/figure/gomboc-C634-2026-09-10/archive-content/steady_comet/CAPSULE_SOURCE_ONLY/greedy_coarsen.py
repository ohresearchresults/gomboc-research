"""Mass-aware geometric coarsening within the fixed C650/H213 graph interval.
No topology minimum claims, and no floating candidate is an exact promotion.
"""
import json,time,sys,argparse
from pathlib import Path
import numpy as np
from numeric import recover,topology,mechanics,snapped
from atlas_opt import Atlas,optimize

def run(start_gen,start_faces,outdir,steps=80,tries=8,iterations=220,unrestricted=False):
 R=Path(__file__).parent;out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
 H=set() if unrestricted else set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines())
 data=json.loads(Path(start_gen).read_text());faces=json.loads(Path(start_faces).read_text())
 ledger=[];t0=time.time()
 for epoch in range(steps):
  q=recover(data)[:data['n_supports']];base=mechanics(q,faces,details=True,tol=1e-10);owners,ef=topology(faces)
  assert {tuple(sorted(p)) for p in ef.values()}>=H
  assert base['counts']==[1,1,0] and base['min_gap']>0
  print('EPOCH',epoch,'E',base['E'],'elapsed',round(time.time()-t0,2),flush=True)
  if base['E']<=249:print('TARGET_NUMERIC',flush=True);return
  candidates=[]
  for a,b in sorted(ef,key=lambda ab:np.linalg.norm(base['P'][ab[0]]-base['P'][ab[1]])):
   if tuple(sorted(ef[a,b])) in H:continue
   for moved in sorted(set(owners[a])^set(owners[b])):
    try:
     z,fs=snapped(data,faces,a,b,moved);qq=recover(z)[:data['n_supports']];rr=mechanics(qq,fs,details=True,tol=1e-10)
     if rr['min_gap']<1e-10 or rr['max_incidence_error']>1e-8 or rr['min_tetra']<=0:continue
     ur=int(np.linalg.norm(rr['P']-[0,0,1],axis=1).argmin())
     vals=np.r_[np.delete(rr['scos'].max(1),3),np.delete(rr['ucos'].max(1),ur)]
     bad=int((vals<0).sum());minimum=float(vals.min());negative=float(np.maximum(0,-vals).sum())
     score=max(0,-minimum)+0.001*bad
     candidates.append((score,negative,bad,a,b,moved,z,fs,minimum))
    except (AssertionError,ValueError,np.linalg.LinAlgError,StopIteration):continue
  candidates.sort(key=lambda c:c[:6]);print('CANDIDATES',len(candidates),[(c[2],c[3],c[4],c[5],round(c[8],8)) for c in candidates[:10]],flush=True)
  accepted=False
  for rank,cand in enumerate(candidates[:tries]):
   score,negative,bad,a,b,moved,z,fs,minimum=cand
   tag=f'E{base["E"]-1}_try{rank}_edge{a}_{b}_q{moved}'
   print('TRY',tag,'bad',bad,'min',minimum,flush=True)
   model=Atlas(z,fs)
   try:
    if minimum>5e-5:u=model.u0;status='direct'
    else:u,st,status=optimize(model,steps=iterations,trust=0.0005,keep=1e-5,goal=5e-5)
    nz=model.save(u,out/(tag+'_GENERATOR.json'))
    (out/(tag+'_faces.json')).write_text(json.dumps(fs,separators=(',',':')))
    rr=mechanics(recover(nz)[:nz['n_supports']],fs,tol=1e-10)
    row=dict(tag=tag,status=status,edge=[a,b],polar_edge=ef[a,b],moved=moved,**rr)
    (out/(tag+'_numeric.json')).write_text(json.dumps(row,indent=2))
    ledger.append(row);(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2))
    if rr['counts']==[1,1,0] and rr['min_gap']>1e-11 and rr['min_tetra']>0 and rr['max_incidence_error']<1e-8 and min(rr['polar_escape_min'],rr['primal_escape_min'])>1e-6:
     data=nz;faces=fs;accepted=True
     (out/'LATEST_GENERATOR.json').write_text(json.dumps(nz,sort_keys=True,separators=(',',':')))
     (out/'LATEST_faces.json').write_text(json.dumps(fs,separators=(',',':')))
     print('ACCEPT_NUMERIC',tag,rr,flush=True);break
    print('REJECT',tag,rr,flush=True)
   except (ValueError,AssertionError,np.linalg.LinAlgError) as exc:print('ERROR',tag,str(exc),flush=True)
  if not accepted:print('STOP_NO_NEXT',flush=True);return
 print('STOP_EPOCH_BUDGET',flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('generator');ap.add_argument('faces');ap.add_argument('outdir');ap.add_argument('--steps',type=int,default=80);ap.add_argument('--tries',type=int,default=8);ap.add_argument('--iterations',type=int,default=220);ap.add_argument('--unrestricted',action='store_true');a=ap.parse_args();run(a.generator,a.faces,a.outdir,a.steps,a.tries,a.iterations,a.unrestricted)
