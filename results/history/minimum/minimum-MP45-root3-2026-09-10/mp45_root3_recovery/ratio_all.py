import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,hashlib,multiprocessing
from pathlib import Path
import ratio_probe as r
from mp45_norm80_fixed import P,WHOLE

def job(j):
 name='ratio_'+'_'.join(map(str,j))+'.json'
 if Path(name).exists():
  row=json.loads(Path(name).read_bytes());assert r.check(row)==row['scalar_sha'];return row
 return r.build(j)
if __name__=='__main__':
 jobs=[(ix,lo,lo+1,2,0)for ix in P if ix not in WHOLE for lo in range(2)]
 with multiprocessing.get_context('fork').Pool(4)as pool:
  rows=[]
  for j,row in zip(jobs,pool.imap(job,jobs)):
   print('COMPLETE_HALF',j,row is not None,flush=True);rows.append(row)
 raw=r.comb.encoded(dict(jobs=jobs,records=rows));Path('ratio16.json').write_bytes(raw)
 print('RATIO16_OUTPUT',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
 print('RATIO16_STATUS',sum(x is not None for x in rows),'OF',len(rows),flush=True)
