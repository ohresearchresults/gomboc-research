# material-102a63fc514e

AI research material

---

#!/usr/bin/env python3
"""Deterministic search for an actual H5 stress separating two scalar maps.
NumPy 2.3.5 proposal only; exact acceptance is part of spectral_floor.py.
"""
from spectral_floor import *
import numpy as np
p=F(7024915,10**6);q=F(6832329,10**6);alpha=1/(p*q+q-2)
packet=(((7,0),31),((8,7),24),((9,4),45))
def check(th):
 Z=np.array(vertices(tuple(map(float,th))),float);D=0.;K=np.zeros(3);J=np.zeros((3,3))
 for f in FACETS:
  for k in range(1,len(f)-1):
   a,b,c=Z[[f[0],f[k],f[k+1]]];d=np.dot(a,np.cross(b,c));u=a+b+c;D+=d;K+=d*u/4;J+=d*(np.outer(u,u)+np.outer(a,a)+np.outer(b,b)+np.outer(c,c))/20
 g=K/D;S=J/D-np.outer(g,g);Si=np.linalg.inv(S);Q=np.zeros((3,3))
 for (i,j),w in packet:
  a=Z[i]-g;e=Z[j]-Z[i];Q-=w*(np.outer(a,e)+np.outer(e,a))/2
 t=np.sum(Si*Q);C=np.linalg.inv(np.linalg.cholesky(S));T=C@Q@C.T;eig=np.linalg.eigvalsh(T)
 return eig[0]+t/144,eig[0]+float(alpha)*t,t
base=tuple(map(F,('13/20','3/4','4/5','1/10','3/10')))
found=None
for i in range(1,600):
 th=base[:4]+(F(i,1000),);old,new,t=check(th)
 if old < -.01 and new > .01:
  found=(th,old,new,t);break
if found is None:raise SystemExit('NO_CONTROL_FOUND; not a feasibility conclusion')
th,old,new,t=found
out={'theta':list(map(str,th)),'packet':[(list(e),w) for e,w in packet],'proposal_old_floor_eigenvalue':old,'proposal_new_floor_eigenvalue':new,'proposal_trace':t}
raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();Path('spectral_floor_proposal.json').write_bytes(raw)
print(json.dumps(out));print('SPECTRAL_FLOOR_PROPOSAL_ONLY',len(raw),hashlib.sha256(raw).hexdigest())
