"""New critical vertex124 movement, outside the former frozen-star hypotheses."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import root
from patch_model import Patch
m=Patch(Path(os.environ['NH72_BASE_REPORT']));rows=[]
eta=np.array([-.2508314428450225,.02424207684755533,.00857532527947764])
for s in [i/20 for i in range(-10,21)]:
 def f(eta):
  z=np.zeros(12);z[0]=s;z[[8,9,10]]=eta;return m.calc(z)[2]-m.c
 r=root(f,eta,tol=1e-11);z=np.zeros(12);z[0]=s;z[[8,9,10]]=r.x;P,d=m.points(z)
 b=m.brief(z);b['s']=s;b['error']=float(np.linalg.norm(f(r.x)));rows.append(b)
 if b['min_gap']>1e-10 and b['error']<1e-10:eta=r.x.copy();print(s,b['counts'],b['Uold'],b['Sold'],b['min_gap'],eta,flush=True)
Path(sys.argv[1]).write_text(json.dumps(rows,sort_keys=True))
print('SHIFT124_COMPENSATED_FINITE_SCREEN_DONE',len(rows),flush=True)
