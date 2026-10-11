"""Iterated exact coarsening with a fixed, explicit P-depth allowance.
Every accepted union is a new rational physical body at its own uniform centroid.
The target census remains110;121checkpoints never count as success.
"""
import argparse,json,time
from pathlib import Path
from gmpy2 import mpq
from facet_union_scout import run as scout

def run(source,out,rounds,allowance):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);start=time.time();b=json.loads((source/'exact_bars.json').read_text());anchor=float(mpq(b['P'][0]['depth']));limit=anchor*allowance;hist=[]
 for k in range(rounds):
  d=out/f'round{k:02d}';scout(source,d,4);candidates=[]
  for p in d.glob('pair*/exact_repair_g14'):
   a=json.loads((p/'summary.json').read_text());bb=json.loads((p/'exact_bars.json').read_text())
   if a['goal_met']:(out/'POTENTIAL_GOAL.json').write_text(json.dumps(dict(source=str(p.resolve()),summary=a),indent=2));return
   if a['counts']!=[1,2,1]or a['weak']!=[0,0,0]:continue
   value=float(mpq(bb['P'][0]['depth']))
   if value<=limit:candidates.append((value,p,a))
  if not candidates:
   hist.append(dict(round=k,result='no admitted exact union within fixedPallowance',limit=limit,source=str(source)));(out/'history.json').write_text(json.dumps(hist,indent=2));print('REPEATED_UNION_FINITE_STOP',k,flush=True);return
  value,source,a=min(candidates,key=lambda t:t[0]);row=dict(round=k,source=str(source.resolve()),P=value,anchor_P=anchor,allowed_P=limit,V=a['V'],E=a['E'],F=a['F'],counts=a['counts'],weak=a['weak'],seconds=time.time()-start);hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('REPEATED_EXACT_FACET_UNION',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--rounds',type=int,default=15);p.add_argument('--allowance',type=float,default=1.04);a=p.parse_args();run(a.source,a.out,a.rounds,a.allowance)
