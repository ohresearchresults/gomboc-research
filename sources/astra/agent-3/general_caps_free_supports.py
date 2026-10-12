"""Release nonsimple cap vertices in a <=84-halfspace family.
The saved normal perturbation is a literal new physical body, not a claim that
the exact old incidence survived. Every final accepted body is exact-frozen.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from polyhedral_stable_cap import Cap
from support_geometry import geometry
from support_quota_polish import run as repair
from free_support_persistence import run as optimize
from exact_audit_supports import audit
from exact_barcode_report import report

def run(source,scout,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);scout=Path(scout);c=Cap(source);records=[];start=time.time()
 for k,label in enumerate(['P1e-07','P0.001','P0.01','P0.1','P1e-10']):
  d=out/label;d.mkdir();nom=json.loads((scout/('best_'+label+'.json')).read_text());g,info=c.score(np.array(nom['controls']));Q=g['H'];assert len(Q)<=84;noise=np.random.default_rng(80400+k).normal(size=Q.shape)*1e-10;Q+=noise;np.save(d/'initial_Q.npy',Q);np.save(d/'literal_noise.npy',noise);(d/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),nomination=str((scout/('best_'+label+'.json')).resolve()),noise_seed=80400+k,noise_std=1e-10,formula='intersection of saved literal initial_Q dot x<=1; uniform density1',source_census_only_numerical=info,max_support_count=84),indent=2));repair(d/'initial_Q.npy',d/'direct211',2,1,400,1e-7);p=d/'direct211/success_Q.npy';row=dict(label=label,initial_F=len(Q))
  if p.exists():
   a=audit(p,d/'exact_direct_g12',10**12);report(d/'exact_direct_g12');row.update(direct_counts=a['counts'],direct_E=a['E'],direct_evidence=str(d/'exact_direct_g12'))
  else:row['direct_result']='finite quota repair failed'
  if k<3:
   optimize(str(p if p.exists()else d/'initial_Q.npy'),d/'search',len(Q),80500+k,3500);repair(d/'search/final_Q.npy',d/'optimized211',2,1,500,1e-7);pp=d/'optimized211/success_Q.npy'
   if pp.exists():
    a=audit(pp,d/'exact_optimized_g12',10**12);report(d/'exact_optimized_g12');row.update(optimized_counts=a['counts'],optimized_E=a['E'],optimized_evidence=str(d/'exact_optimized_g12'))
   else:row['optimized_result']='finite quota repair failed'
  row['seconds']=time.time()-start;records.append(row);(out/'trials.json').write_text(json.dumps(records,indent=2));print('GENERAL_CAP_FREE_SUPPORTS',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('scout');p.add_argument('out');a=p.parse_args();run(a.source,a.scout,a.out)
