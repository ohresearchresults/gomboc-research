"""Replay preserved numerical checkpoints without rerunning either optimizer.
This validates observation recovery, not exact geometry or an exclusion theorem.
"""
import argparse,json
from pathlib import Path
import numpy as np
from pyramid_search import Pyramid
from c80_dual_chain import Model

def main():
 p=argparse.ArgumentParser();p.add_argument('--points',required=True);p.add_argument('--audit',required=True);p.add_argument('--out',required=True);a=p.parse_args();root=Path(__file__).resolve().parent
 s=json.loads((root/'PYRAMID_OBSERVATIONS.json').read_bytes());d=json.loads((root/'dual27/SEARCH.json').read_bytes());pyr=Pyramid(a.points,s['parameters']['tau']);dual=Model(a.audit);rows=[]
 for old in s['records']:
  new=pyr.report(np.array(old['x']))
  assert all(new[k]==old[k] for k in ['S','U','Su','Uu','S_ids','U_ids'])
  assert all(abs(new[k]-old[k])<1e-12 for k in ['convex_min','height'])
  rows.append({'method':'pyramid','start':old['start'],'S':new['S'],'U':new['U']})
 for old in d['records']:
  new=dual.report(np.array(old['chart']),old['n'],old['bow'],old['gain'])
  assert all(new[k]==old[k] for k in ['S','U','S_uncertain','U_uncertain','V_proposal','F_proposal','E_proposal'])
  assert all(abs(new[k]-old[k])<1e-10 for k in ['closure','budget','volume'])
  rows.append({'method':'dual','n':old['n'],'bow':old['bow'],'gain':old['gain'],'S':new['S'],'U':new['U'],'closure':new['closure']})
 assert len(s['records'])==11 and len(d['records'])==27
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 (out/'CHECKPOINTS.json').write_text(json.dumps({'status':'NUMERICAL_CHECKPOINTS_REPLAY_11_AND_27_PASS_NOT_EXACT_CONSTRUCTIONS','records':rows},sort_keys=True,separators=(',',':')))
 print('NUMERICAL_CHECKPOINTS_REPLAY_11_AND_27_PASS_NOT_EXACT_CONSTRUCTIONS',flush=True)
if __name__=='__main__':main()
