"""Exact literal caps, complete contact charts, and actual-mass quota repair.
Every failure remains explicit; a successful numerical repair is exact-frozen.
"""
import argparse,json,time
from pathlib import Path
from exact_clip_audit import audit as freeze_clip
from prepare_balanced_contact import prepare
from contact_quota_polish import run as repair
from exact_contact_audit import audit as freeze_contact
from exact_barcode_report import report

def run(scout,out):
 scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False);definition=scout/'definition.json';source=json.loads(definition.read_text())['source'];records=[];start=time.time()
 for label in ['Q1e-07','Q1e-05','Q0.001','Q0.01','Q0.1','Q1e-10','Q1']:
  d=out/label;d.mkdir();row=dict(label=label,source=str(scout/('best_'+label+'.json')))
  try:
   a=freeze_clip(source,scout/('best_'+label+'.json'),definition,d/'exact_cap_g12',10**12);row['literal_counts']=a['counts'];prepare(d/'exact_cap_g12/audit.json',d/'chart',10**16);repair(d/'chart/construction.json',d/'repair121',1,2,500,1e-7)
   if (d/'repair121/success_q.npy').exists():
    a=freeze_contact(d/'chart/construction.json',d/'repair121/success_q.npy',d/'exact_repair_g14',10**14);report(d/'exact_repair_g14');row.update(result='complete exact repair',counts=a['counts'],E=a['E'],evidence=str(d/'exact_repair_g14/summary.json'))
   else:row['result']='quota repair failed, endpoint retained'
  except (AssertionError,ValueError,ArithmeticError) as e:row.update(result='explicit failure',error=repr(e))
  row['seconds']=time.time()-start;records.append(row);(out/'trials.json').write_text(json.dumps(records,indent=2));print('CAP_SCOUT_REPAIR',row,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');a=p.parse_args();run(a.scout,a.out)
