"""Broad literal cap replacements, retaining a Pareto set for physical repair.
Searches across equilibrium-class changes and retains full geometry and mass.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from unstable_cap_clip import Clip

def run(source,out,seed,trials,allow_over_budget=False):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Clip(source);rng=np.random.default_rng(seed);records=[];chosen={};start=time.time();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),scale=c.scale,center=c.center.tolist(),seed=seed,formula='exact source body intersect one literal physical halfspace after normalized frame conversion',scope='numerical candidates only until exact clip and complete contact repair'),indent=2));np.save(out/'n0.npy',c.n0);np.save(out/'basis.npy',c.B)
 for it in range(trials):
  slope=rng.normal(size=2)*rng.choice([.2,.6,1.5,4.]);ratio=float(rng.choice([1e-5,.01,.1,.3,.6])*rng.random());t=np.r_[slope,1-ratio];loss,g,info=c.score(t);row=dict(it=it,controls=t.tolist(),normal=g['n'].tolist(),offset=g['h'],Pmax=info['Pmax'],Qmax=info['Qmax'],S=info['S'],U=info['U'],V=info['V'],E=info['E'],F=info['F'],P_count=len(info['P']),Q_count=len(info['Q']),loss=loss)
  if (info['VplusEplusF']>=500 and not allow_over_budget) or info['C_2E']<34:continue
  records.append(row)
  for limit in [1e-10,1e-7,1e-5,.001,.01,.1,1.]:
   if info['Qmax']>limit:continue
   key=f'Q{limit:g}';score=info['Pmax']
   if score<chosen.get(key,dict(Pmax=np.inf))['Pmax']:
    chosen[key]=row;(out/('best_'+key+'.json')).write_text(json.dumps(row,indent=2))
  if it%500==0:
   (out/'trials.json').write_text(json.dumps(records,indent=2));(out/'best_by_Q.json').write_text(json.dumps(chosen,indent=2));print('CAP_SCOUT',it,{k:(v['Pmax'],v['Qmax'],v['E'])for k,v in chosen.items()},flush=True)
  if info['S']==info['U']==1:
   (out/f'potential{it}.json').write_text(json.dumps(row,indent=2));np.save(out/f'potential{it}.npy',g['X']);print('CAP_SCOUT_POTENTIAL_REQUIRES_EXACT',row,flush=True)
 (out/'trials.json').write_text(json.dumps(records,indent=2));(out/'best_by_Q.json').write_text(json.dumps(chosen,indent=2));print('CAP_SCOUT_DONE',out,len(records),time.time()-start,{k:(v['Pmax'],v['Qmax'],v['E'])for k,v in chosen.items()},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=79201);p.add_argument('--trials',type=int,default=5000);p.add_argument('--allow-over-budget-intermediate',action='store_true');a=p.parse_args();run(a.input,a.out,a.seed,a.trials,a.allow_over_budget_intermediate)
