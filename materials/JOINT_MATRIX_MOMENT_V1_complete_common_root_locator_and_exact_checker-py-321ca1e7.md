# material-321ca1e7697b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Common-root separator using joint matrix elimination. Exact checker is stdlib.
Reconstruct with matrix_moments.py and pinned affine dependencies.
Commands: python matrix_roots.py locate INDEX MODE
          python -S matrix_roots.py check RECORD.json
Every passing result remains ephemeral until its complete data are preserved.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import json,sys,hashlib,time
from functools import lru_cache
import matrix_moments as mm
am=mm.am;fm=am.fm
import common_roots as cr
assert __debug__
HERE=Path(__file__).resolve().parent
IDENTITY='JOINT_MATRIX_MOMENT_COMMON_ROOTS_CERTIFICATE_V1'

@lru_cache(None)
def system(index):
 d=am.system(fm.inputs()[index]);m=mm.build(index,False)
 new=[{(tuple(t),q):c for t,q,c in row} for row in m['new_relations']]
 exponents=[max(abs(c) for c in row.values()).bit_length()-1 for row in new]
 # Scale by a power of two that bounds all coefficients in absolute value.
 exponents=[k if max(abs(c) for c in row.values())==2**k else k+1 for k,row in zip(exponents,new)]
 sp={'identity':'JOINT_MATRIX_MOMENT_SYSTEM_V1','affine_system_pin':fm.pin(fm.enc(fm.description(d))),
     'joint_matrix_pin':fm.pin(fm.enc(m)),'normalizing_powers':exponents}
 return d,new,exponents,sp

def pencil(index,mode):
 import numpy as np
 from scipy.sparse import coo_matrix,hstack,vstack
 fm.system=am.system
 d,A,bounds,fr,keys,maps=cr.pencil(index,mode)
 d,new,exponents,sp=system(index);cells=d['cells'];ci={t:j for j,t in enumerate(cells)}
 rr=[];cc=[];vv=[]
 for j,(row,e) in enumerate(zip(new,exponents)):
  for (t,q),c in row.items():
   a,b=mm.PAIRS[q];rr.append(ci[t]*100+a*10+b);cc.append(j);vv.append(c/2**e)
   if a!=b:rr.append(ci[t]*100+b*10+a);cc.append(j);vv.append(c/2**e)
 B=coo_matrix((vv,(rr,cc)),shape=(len(cells)*100,len(new))).tocsr()
 big=vstack([B]*8).tocsr()
 A=hstack([A[:,:fr],big,A[:,fr:]]).tocsr()
 return d,A,[(-1,1)]*(fr+len(new))+[(0,1)]*len(keys),fr,new,exponents,sp

def check(record):
 assert record['identity']==IDENTITY
 idx=record['native_index'];mode=record['mode'];x=record['coefficients']
 assert all(type(a)==int for a in x)
 d,new,exponents,sp=system(idx);assert record['system_pin']==fm.pin(fm.enc(sp))
 nc=len(d['cells']);rank=len(d['basis']);fr=10*(rank+1)+56*rank
 keys,maps=cr.mappings(mode,d['cells']);assert len(x)==fr+len(new)+len(keys)
 assert min(x[fr+len(new):])>=0
 scale=max(exponents,default=0);S=2**scale
 mats={t:[[0]*10 for _ in range(10)] for t in d['cells']};pos=0
 for h in [d['reference']]+d['basis']:
  for i in range(10):
   g=x[pos]*S;pos+=1
   for t,c in h.items():
    for j in t:mats[t][i][j]+=c*g;mats[t][j][i]+=c*g
 for h in d['basis']:
  for i in range(10):
   for j in range(i,10):
    c=x[pos]*S;pos+=1
    for t,s in h.items():
     mats[t][i][j]+=s*c
     if i!=j:mats[t][j][i]+=s*c
  c=x[pos]*S;pos+=1
  for t,s in h.items():
   for i in t:
    for j in t:mats[t][i][j]+=s*c*(1+(i==j))
 assert pos==fr
 for row,e in zip(new,exponents):
  c=x[pos]*2**(scale-e);pos+=1
  for (t,q),a in row.items():
   i,j=mm.PAIRS[q];mats[t][i][j]+=c*a
   if i!=j:mats[t][j][i]+=c*a
 assert pos==fr+len(new)
 reports=[]
 for root in cr.ROOTS:
  out={t:[row[:] for row in A] for t,A in mats.items()};mi=iter(maps[root-1])
  for t in d['cells']:
   for i in range(10):
    if i==root:continue
    mu=x[pos+next(mi)]*S;p=i+1 if i<root else i-1
    out[t][i][i]+=2*mu;out[t][i][p]-=mu;out[t][p][i]-=mu
  assert next(mi,None) is None
  bh=hashlib.sha256();mh=hashlib.sha256();ph=hashlib.sha256();minimum=None
  for t,A in sorted(out.items()):
   assert all(A[i][j]==A[j][i] for i in range(10) for j in range(10))
   for i in range(10):A[i][i]-=1
   m=fm.bareiss(A);p,m2=fm.schur(A);assert m==m2
   bh.update(fm.enc([t,A]));mh.update(fm.enc([t,m]));ph.update(fm.enc([t,list(map(str,p))]))
   minimum=min(m+[minimum]) if minimum is not None else min(m)
  reports.append({'root':root,'blocks':nc,'leading_minors':nc*10,'minimum_leading_minor':minimum,
   'block_sha256':bh.hexdigest(),'minor_sha256':mh.hexdigest(),'schur_sha256':ph.hexdigest()})
 return {'identity':'JOINT_MATRIX_MOMENT_COMMON_ROOTS_EXACT_REPORT_V1','native_index':idx,
  'mode':mode,'record_pin':fm.pin(fm.enc(record)),'system_pin':record['system_pin'],
  'new_matrix_relations':len(new),'common_integer_scale_power':scale,
  'total_blocks':nc*8,'total_leading_minors':nc*80,'reports':reports}

def locate(index,mode):
 import numpy as np,scipy,platform
 from scipy.optimize import minimize
 from scipy.special import logsumexp
 start=time.time();d,A,bounds,fr,new,exponents,sp=pencil(index,mode)
 n=len(d['cells'])*8;x=np.zeros(A.shape[1]);history=[]
 print('JOINT_MATRIX_PENCIL',index,mode,A.shape,A.nnz,len(new),max(exponents,default=0),flush=True)
 for tau in (.1,.03,.01,.003,.001,.0003,.0001,.00003):
  def objective(x):
   mats=(A@x).reshape(n,10,10);lam,U=np.linalg.eigh(mats)
   z=-lam/tau;lse=logsumexp(z);weights=np.exp(z-lse)
   grad=np.einsum('bik,bk,bjk->bij',U,weights,U)
   return tau*lse,-A.T@grad.ravel()
  r=minimize(objective,x,jac=True,method='L-BFGS-B',bounds=bounds,
     options=dict(maxiter=2500,maxcor=30,ftol=1e-15,gtol=1e-10,maxls=40))
  x=r.x;minimum=float(np.linalg.eigvalsh((A@x).reshape(n,10,10)).min())
  history.append(dict(tau=tau,minimum=minimum,iterations=r.nit,status=int(r.status)))
  print('JOINT_MATRIX_STAGE',index,mode,tau,minimum,r.nit,round(time.time()-start,1),flush=True)
  proposal={'identity':'JOINT_MATRIX_NUMERICAL_PROPOSAL_V1','native_index':index,'mode':mode,
      'coefficients':x.tolist(),'history':history,'system_pin':fm.pin(fm.enc(sp)),
      'environment':[platform.python_version(),np.__version__,scipy.__version__]}
  (HERE/f'matrix_proposal_{index}_{mode}.json').write_bytes(fm.enc(proposal))
  if minimum>1e-5:break
 for power in (12,14,16,18,20,24):
  q=np.rint(x*2**power);assert np.max(np.abs(q))<2**62
  record={'identity':IDENTITY,'native_index':index,'mode':mode,'system_pin':fm.pin(fm.enc(sp)),
      'rounding_power':power,'coefficients':q.astype(np.int64).tolist()}
  try:report=check(record)
  except (AssertionError,ZeroDivisionError):continue
  p=HERE/f'matrix_certificate_{index}_{mode}.json';p.write_bytes(fm.enc(record))
  p.with_suffix('.verified.json').write_bytes(fm.enc(report))
  print('JOINT_MATRIX_EXACT_PASS_EPHEMERAL',index,mode,power,report['total_blocks'],*fm.pin(p.read_bytes()),flush=True)
  return True
 print('JOINT_MATRIX_UNKNOWN_NO_EXACT_CERTIFICATE',index,mode,flush=True);return False

if __name__=='__main__':
 if len(sys.argv)==4 and sys.argv[1]=='locate':locate(int(sys.argv[2]),sys.argv[3])
 elif len(sys.argv)==3 and sys.argv[1]=='check':
  p=Path(sys.argv[2]);r=check(json.loads(p.read_bytes()));p.with_suffix('.verified.json').write_bytes(fm.enc(r))
  print('JOINT_MATRIX_EXACT_CHECK_PASS',r['native_index'],r['mode'],r['total_blocks'],*fm.pin(fm.enc(r)))
 else:raise ValueError('locate INDEX MODE | check RECORD.json')
