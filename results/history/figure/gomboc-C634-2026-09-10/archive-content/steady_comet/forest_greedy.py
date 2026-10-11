from pathlib import Path
import json,time,numpy as np
from forest_subsets import audit,core,pa,root,stable,P0
R=Path(__file__).parent;out=R/'forest_greedy_records';out.mkdir(exist_ok=True);S=set(range(len(P0)));cur=audit(S);t0=time.time();ledger=[]
for epoch in range(120):
 protected=stable|{root};candidates=[]
 for v in sorted(S-protected):
  gone={v}
  while True:
   more={w for w in S if pa[w] in gone}-gone
   if not more:break
   gone|=more
  if gone&protected:continue
  if len(gone)>8:continue
  ids=S-gone
  try:r=audit(ids)
  except Exception:continue
  if r['E']>=cur['E']:continue
  candidates.append((r,gone))
 winners=[(r,gone) for r,gone in candidates if r['counts']==[1,1,0] and r['minimum']>1e-7]
 print('FOREST_GREEDY_EPOCH',epoch,'V/E/F',cur['V'],cur['E'],cur['F'],'candidates',len(candidates),'winners',len(winners),'sec',round(time.time()-t0,2),flush=True)
 if not winners:
  ranked=sorted(candidates,key=lambda z:(z[0]['bad'],z[0]['score']));print('FOREST_GREEDY_BLOCKED',[(sorted(g),r['V'],r['E'],r['counts'],r['minimum'],r['centre_shift']) for r,g in ranked[:10]],flush=True)
  for j,(r,gone) in enumerate(ranked[:10]):(out/f'BLOCKED_{epoch}_{j}.json').write_text(json.dumps(audit(S-gone,True),sort_keys=True,separators=(',',':')))
  break
 r,gone=min(winners,key=lambda z:(z[0]['E'],-z[0]['minimum']));S-=gone;cur=r;full=audit(S,True);tag=f'C{2*r["E"]}_FOREST_GREEDY_{epoch}';(out/(tag+'.json')).write_text(json.dumps(full,sort_keys=True,separators=(',',':')));(out/'BEST.json').write_text(json.dumps(full,sort_keys=True,separators=(',',':')));ledger.append(dict(tag=tag,removed=sorted(gone),**r));(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));print('FOREST_GREEDY_NUMERIC_WINNER',tag,{k:v for k,v in r.items() if k!='ids'},flush=True)
 if r['E']<=249:break
