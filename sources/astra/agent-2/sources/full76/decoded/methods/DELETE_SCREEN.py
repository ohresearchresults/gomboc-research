import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from numeric import Chart
import json,numpy as np
from pathlib import Path
c=Chart();r=json.load(open(Path(__file__).parent/'baseline/A.json'));records=[]
for f,cy in enumerate(r['faces']):
 if len(cy)!=3:continue
 try:
  a=c.actual(np.delete(c.Q,f,axis=0));a.pop('Q');a['deleted_support']=f;records.append(a);print('DELETE_NUMERIC',f,a['V'],a['E'],a['F'],a['counts'],flush=True)
 except Exception as ex:records.append(dict(deleted_support=f,error=str(ex)));print('ERROR',f,str(ex),flush=True)
 Path(__file__).with_name('DELETE_SCREEN.json').write_text(json.dumps(records))
