"""Targeted root0 locator. Negative attempts are not infeasibility claims."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sys,json,multiprocessing
sys.path.insert(0,'nova54_recovery')
import comb,exact_check as C
D=json.loads(Path('root0_enumeration.json').read_bytes());G=D['graph']

def work(row):
 import locator
 i,p=row['index'],row['parent'];attempts=[]
 plans=[['ordinary',[0]]]+[['ordinary',[0,a]]for a in range(1,9)]+[['shared',[0,a]]for a in range(1,9)]+[['volume',list(range(9))],['cycle',list(range(9))]]
 for k,aa in plans:
  try:
   rec=locator.make_record(G,0,p,k,aa,8,None)
   n,h=C.checked(rec,G['facets'])
   out=dict(**row,record=rec,matrices=n,scalar_sha=h,plan=[k,aa,8],attempts=attempts)
   Path('root0_records/%s.json'%i).write_bytes(comb.encoded(out))
   print('ROOT0_FOUND',i,k,aa,n,flush=True)
   return out
  except AssertionError as e:
   attempts.append([k,aa,str(e)])
 out=dict(**row,attempts=attempts)
 Path('root0_records/%s.unknown.json'%i).write_bytes(comb.encoded(out))
 print('ROOT0_UNKNOWN',i,flush=True)
 return out

if __name__=='__main__':
 Path('root0_records').mkdir(exist_ok=True)
 with multiprocessing.get_context('fork').Pool(4)as pool:
  rows=list(pool.imap(work,D['terminal']))
 Path('root0_exploration.json').write_bytes(comb.encoded(rows))
 print('ROOT0_TARGETED_LOCATOR_FINISHED',len(rows),sum('record'in r for r in rows),flush=True)
