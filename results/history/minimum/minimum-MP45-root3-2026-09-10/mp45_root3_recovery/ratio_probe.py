import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib
from pathlib import Path
sys.path.insert(0,'nova54_recovery')
import comb,exact_check
from mp45_norm80_fixed import FS,P,broom,_relations

def diagonal(items):
 K=[[0]*9 for _ in range(9)]
 for i,v in items:K[i][i]+=2*v
 return K

def constraints(ix,lo,hi,den,mode=0):
 b=broom(P[ix]);forms=[diagonal([(b[1],1),(b[8],-1)])]
 forms += [diagonal([(b[0],lo),(b[8],-den)]),diagonal([(b[8],den),(b[0],-hi)])]
 if mode==34:
  red=[(i,j)for i in range(2,8)for j in range(i-1)]+[(i,8)for i in range(1,8)if i!=2]+[(8,j)for j in range(1,8)]
  for i,j in red:
   i,j=b[i],b[j];K=[[0]*9 for _ in range(9)];K[i][i]=-2;K[i][j]=K[j][i]=1;forms.append(K)
 return forms

def check(row):
 forms=constraints(*row['job']);ix=row['job'][0];z=row['z'];m=len(forms)
 rel=_relations(FS,tuple(range(9)))[1]
 assert row['parent']==P[ix]and len(z)==1063+63*m and min(z[1063:])>=0
 rec=dict(root=3,parent=P[ix],kind='cycle',fans=[[a,0]for a in range(9)],relations=rel,z=z[:1063]);h=hashlib.sha256()
 for u,Q in enumerate(exact_check.scalar_matrices(rec,FS)):
  for K,v in zip(forms,z[1063+u*m:1063+(u+1)*m]):
   for i in range(9):
    for j in range(9):Q[i][j]+=K[i][j]*v
  a=exact_check.bareiss(Q);assert a==exact_check.ldl(Q);h.update(comb.encoded([Q,a]))
 return h.hexdigest()

def build(job):
 import numpy as np,locator,schur
 ix=job[0];forms=constraints(*job);x,B,ls,bi,mat,info=locator.cycle_problem(P[ix],FS)
 extra=np.array(forms)/2;k=len(mat);m=len(forms);N=len(x)
 xx=np.r_[x[:-1],np.zeros(k*m),x[-1]];BB=np.r_[B[:-1],np.ones(k*m),B[-1]]
 ll=np.r_[ls,np.arange(N-1,N-1+k*m)];xx[ll]=1/(k*(8+m));ii=[];mm=[]
 for u,(ids,L)in enumerate(zip(bi,mat)):
  ii.append(np.r_[ids[:-1],np.arange(N-1+u*m,N-1+(u+1)*m),N-1+k*m])
  mm.append(np.concatenate([L[:-1],extra,L[-1:]]))
 v=schur.locate((xx,BB,ll,ii,mm,info),verbose=True)
 assert v is not None
 print('RATIO_MARGIN',job,float(v[-1]),flush=True)
 row=dict(job=list(job),parent=P[ix]);sc=max(abs(float(a))for a in v[:-1])
 for power in (6,8,10,12):
  row['z']=[round(float(a)/sc*10**power)for a in v[:-1]]
  try:h=check(row)
  except AssertionError:continue
  row.update(power=power,scalar_sha=h);raw=comb.encoded(row)
  name='ratio_'+'_'.join(map(str,job))+'.json';Path(name).write_bytes(raw)
  print('RATIO_EXACT_PASS',job,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
  return row
 print('RATIO_NO_EXACT_CERTIFICATE',job,flush=True)

if __name__=='__main__':
 if sys.argv[1]=='check':
  r=json.loads(Path(sys.argv[2]).read_bytes());assert check(r)==r['scalar_sha'];print('RATIO_FROZEN_EXACT_CHECK_PASS',r['job'])
 else:build(tuple(map(int,sys.argv[1:])))
