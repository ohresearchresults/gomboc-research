import sys,json,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R));from check_centre import dot,solve
sys.set_int_max_str_digits(0)
z=json.loads(Path(sys.argv[1]).read_text());P=[tuple(map(F,p))for p in z['raw_vertices']];q=[tuple(F(x,h)for x in n)for n,h in zip(z['normals'],z['offsets'])]
cs=json.loads(Path(sys.argv[2]).read_text());names=sorted({n for t in cs['triples']for n in t['guards']});rows=[]
for nm in names:
 kind,i,j=nm.split(':');i=int(i);j=int(j)
 if kind=='primal':n=tuple(P[j][k]-P[i][k]for k in range(3));b=dot(P[i],n)
 else:a=dot(q[i],q[i]);v=dot(q[i],q[j]);n=tuple(v*q[i][k]-a*q[j][k]for k in range(3));b=v-a
 rows.append((n,b))
A=np.array([[float(v)for v in n]for n,b in rows]);B=np.array([float(b)for n,b in rows]);scale=np.linalg.norm(A,axis=1);A/=scale[:,None];B/=scale
out=[]
for i in range(3):
 for sg in [-1,1]:
  c=np.zeros(3);c[i]=sg;r=linprog(c,A_ub=A,b_ub=B,bounds=[(None,None)]*3,method='highs');print('CELL_BOUND',i,sg,r.status,r.fun if r.success else r.message)
v=85
for a,b in z['edges']:
 if v not in(a,b):continue
 j=b if a==v else a;d=tuple(P[j][k]-P[v][k]for k in range(3));const=dot(P[v],d);r=linprog(np.array([float(x)for x in d]),A_ub=A,b_ub=B,bounds=[(None,None)]*3,method='highs');upper=float(const)-r.fun if r.success else None
 if upper is None or upper>=0:print('APEX_NOT_FORCED',j,r.status,upper);out.append(dict(neighbour=j,upper=upper,status=r.status));continue
 best=np.argsort(r.ineqlin.residual)[:6];found=None
 for k in itertools.combinations(best,3):
  try:lam=solve([[rows[t][0][a]for t in k]for a in range(3)],tuple(-x for x in d))
  except AssertionError:continue
  U=const+sum(lam[ii]*rows[t][1]for ii,t in enumerate(k))
  if min(lam)>=0 and U<0:found=dict(neighbour=j,guards=[names[t]for t in k],upper_float=float(U));break
 print('APEX_CERT',j,found)
 out.append(found or dict(neighbour=j,upper=upper,exact_failed=True))
Path(sys.argv[3]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
