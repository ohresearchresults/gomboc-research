"""Finite repeated physical cap replacement/deletion with exact checkpoints.
Intermediate cuts may exceed the edge budget; each free-hull restart has at
most84literalpoints, and every accepted stage is fully exact-audited under
both strict complexity bounds. A121improvement is always a nonwinner.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction
from cap_clip_scout import run as scout
from exact_clip_audit import audit as freeze_clip
from cap_free_retirement import run as retire
from exact_audit_vertices import audit as freeze_vertices
from exact_barcode_report import report

def run(source,out,seed,rounds):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);source=Path(source);b=json.loads((source/'exact_bars.json').read_text());best=float(Fraction(b['P'][0]['depth']));hist=[];start=time.time()
 for k in range(rounds):
  d=out/f'round{k:02d}';d.mkdir();(d/'source.json').write_text(json.dumps(dict(exact_source=str(source.resolve()),P=best,allow_over_budget_intermediate=True,final_point_count_limit=84),indent=2));scout(source,d/'scout',seed+71*k,6000,True)
  for label in ['Q1e-07','Q1e-05','Q0.001','Q0.01','Q0.1']:
   freeze_clip(source,d/'scout'/('best_'+label+'.json'),d/'scout/definition.json',d/'caps'/label/'exact_cap_g12',10**12)
  retire(d/'caps',d/'free',seed+1000+17*k);trials=json.loads((d/'free/trials.json').read_text());candidates=sorted([a for r in trials for a in r['stages']if a['result']=='strict121 numerical'],key=lambda a:a['P']);accepted=False;row=dict(round=k,prior_P=best,seconds=time.time()-start)
  for idx,c in enumerate(candidates):
   if c['P']>=best-1e-5:break
   pp=d/f'exact_improvement{idx}';a=freeze_vertices(c['path'],pp,10**11);report(pp);bars=json.loads((pp/'exact_bars.json').read_text());p=max([float(Fraction(t['depth']))for t in bars['P']],default=0.);q=max([float(Fraction(t['depth']))for t in bars['Q']],default=0.)
   if a['counts']==[1,1,0] and a['weak']==[0,0,0] and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:
    row.update(result='potential complete exact Figure requires final source review',source=str(pp));hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));(out/'POTENTIAL_GOAL.json').write_text(json.dumps(row,indent=2));return
   if a['counts']==[1,2,1] and a['weak']==[0,0,0] and a['V']+a['E']+a['F']<500 and p<best-1e-5:
    source=pp;best=p;accepted=True;row.update(result='exact121 improvement, NOT Figure',P=p,Q=q,V=a['V'],E=a['E'],F=a['F'],source=str(pp));break
  if not accepted:row['result']='no strictly improved exact121 in finite batch'
  hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('CAP_RETIREMENT_CYCLE',row,flush=True)
  if not accepted:break

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--seed',type=int,default=79800);p.add_argument('--rounds',type=int,default=3);a=p.parse_args();run(a.source,a.out,a.seed,a.rounds)
