import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sys,json,multiprocessing,hashlib
sys.path.insert(0,'nova54_recovery')
import comb,exact_check
DATA=json.loads(Path('input.json').read_bytes())
def work(row):
 import locator
 k,s,sel,powr=row['plan'];p=row['parent']
 rec=locator.make_record(DATA['graph'],3,p,k,s,powr,sel)
 n,h=exact_check.checked(rec,DATA['graph']['facets'])
 return dict(**row,record=rec,matrices=n,scalar_sha=h)
if __name__=='__main__':
 if sys.argv[1]=='build':
  rows=[];Path('old_records').mkdir(exist_ok=True)
  with multiprocessing.get_context('fork').Pool(4)as pool:
   for r in pool.imap(work,DATA['old']):
    rows.append(r);Path('old_records/%s.json'%r['index']).write_bytes(comb.encoded(r))
    print('OLD_EXACT',r['index'],r['matrices'],r['scalar_sha'],flush=True)
  Path('mp45_old55.json').write_bytes(comb.encoded(rows))
 else:rows=json.loads(Path('mp45_old55.json').read_bytes())
 assert [{k:r[k]for k in ('index','parent','serial','plan')}for r in rows]==DATA['old']
 for r in rows:assert exact_check.checked(r['record'],DATA['graph']['facets'])==(r['matrices'],r['scalar_sha'])
 b=Path('mp45_old55.json').read_bytes();print('OLD55_PIN',len(b),hashlib.sha256(b).hexdigest(),flush=True)
 print('NOVA54_MP45_ROOT3_55_OLD_PLANS_INDEPENDENT_EXACT_PASS',sum(r['matrices']for r in rows),flush=True)
