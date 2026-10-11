"""NEW deterministic producer: no unavailable cap9 file is an input.
CPython3.13.5, NumPy2.3.5, SciPy1.17.0, threadpoolctl3.6.0, one BLAS thread, no randomness.
python build.py produces cap9_new.json; python -S verify.py is independent.
"""
from pathlib import Path
import hashlib,json
import engine
import numpy as np
assert __debug__
ROWS01=[246,247,248,249,250,251,260,261,262,263,264,265,267,268,269,270,271,273,274,275,276,279,280,281]
ROWS02=[277,282,283,284]
REMAINING=[253,266,272,278,285]

def positive(a):
 # Fraction-free elimination, using a symmetric trailing update.
 a=[r[:] for r in a];old=1
 for k in range(9):
  pivot=a[k][k]
  if pivot<=0:return False
  for i in range(k+1,9):
   for j in range(i,9):
    z=a[i][j]*pivot-a[i][k]*a[k][j]
    assert z%old==0
    a[i][j]=a[j][i]=z//old
  old=pivot
 return True

def matrices(p,rows,g,u):
 off=[[0]*9 for _ in range(9)]
 if len(rows)==2:
  t=18
  for i in range(9):
   for j in range(i,9):off[i][j]+=g[t];off[j][i]+=g[t];t+=1
 for r,a in enumerate(rows):
  gamma=g[9*r:9*r+9]
  for t,w in enumerate(engine.weights(a)):
   b=[[gamma[i]*w[j]+w[i]*gamma[j]+(9*off[i][j]*(1 if r==0 else -1)) for j in range(9)] for i in range(9)]
   for i,mu in enumerate(u[168*r+t],1):
    b[i][i]+=18*mu;b[i][p[i]]-=9*mu;b[p[i]][i]-=9*mu
   yield b

if __name__=='__main__':
 records=[];tt=engine.trees();nm=0
 for ordinal,p in enumerate(tt):
  if ordinal in REMAINING:continue
  rows=[0,1] if ordinal in ROWS01 else [0,2] if ordinal in ROWS02 else [0]
  if ordinal==0:
   # Small exact continuation checkpoint; no numerical locator for this tree.
   gi=[900]+[9]*8
   ui=[[100*w[i]+9 for i in range(1,9)] for w in engine.weights(0)]
  else:
   result=engine.locate(p,rows)
   assert result is not None,('LOCATOR_UNKNOWN',ordinal,rows)
   g,u,margin=result;scale=max(np.max(np.abs(g)),np.max(np.abs(u)))
   gi=np.rint(g/scale*10**8).astype(np.int64).tolist()
   ui=np.rint(u/scale*10**8).astype(np.int64).tolist()
  assert all(v>=0 for r in ui for v in r)
  for b in matrices(p,rows,gi,ui):
   for i in range(9):b[i][i]-=1
   assert positive(b),('EXACT_REJECTION',ordinal)
   nm+=1
  record=dict(ordinal=ordinal,parent=p,rows=rows,g=gi,mu=ui)
  records.append(record)
  Path('partial').mkdir(exist_ok=True)
  Path('partial/%03d.json'%ordinal).write_text(json.dumps(record,sort_keys=True,separators=(',',':'))+'\n')
  if ordinal%25==0:print('NEW_CAP9_GENERATED',ordinal,len(ui),flush=True)
 assert len(records)==281 and nm==51912
 obj=dict(tag='NOVA24_CAP9_NEW_281_V1',specification_parent='asg_6qT-ogbqQKnPgSL8OYGdvVHm',specification_sha256='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36',remaining=REMAINING,records=records)
 data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
 Path('cap9_new.json').write_bytes(data)
 print('NEW_CAP9_INTEGER_GENERATION_PASS',len(records),nm)
 print('DATA',len(data),hashlib.sha256(data).hexdigest())
