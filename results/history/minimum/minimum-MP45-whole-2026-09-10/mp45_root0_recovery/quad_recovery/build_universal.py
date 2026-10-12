"""Regenerate 285 complete universal apex-superset certificates.
CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, one BLAS thread, four fork workers.
There is one deliberately separate final broom proof; no V10 assertion here.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import engine as e
import itertools,json,hashlib,multiprocessing,sys
from pathlib import Path
import scipy,numpy
assert __debug__ and sys.version_info[:3]==(3,13,5)
assert numpy.__version__=='2.3.5' and scipy.__version__=='1.17.0'
A1=[246,247,248,249,250,251,265,266,267,268,269,270,271,272,273,274,275,276,279,280,281,282]
A2=[277,283,284,285]
PARENT='asg_VOkJgQeJI85JsScj0zkUI191'
PH='3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94'
def encoded(o):return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def canon(p):
 ch=[[]for _ in p]
 for i in range(1,len(p)):ch[p[i]].append(i)
 def walk(i):
  ss=sorted(walk(j)for j in ch[i])
  return '('+''.join(s for s,t in ss)+')',(i,)+sum((t for s,t in ss),())
 _,order=walk(0);inv={j:i for i,j in enumerate(order)}
 return tuple(0 if j==0 else inv[p[j]]for j in order)
def trees():
 return sorted({canon((0,)+p)for p in itertools.product(*(range(i)for i in range(1,9)))})
def supersets(aa):
 return [[(a,)+t for t in itertools.combinations([i for i in range(9)if i!=a],3)]for a in aa]
def recover(task):
 ix,p=task;aa=[0,1]if ix in A1 else [0,2]if ix in A2 else [0]
 z=e.certify(p,supersets(aa),cov=len(aa)>1,eps=1e-7,maxouter=11,power=8)
 assert z is not None,('UNVERIFIED_LOCATOR',ix)
 return dict(index=ix,parent=p,apices=aa,covariance=len(aa)>1,z=z)
def main():
 ps=trees();assert len(ps)==286 and ps[278]==(0,0,1,2,3,4,5,6,0)
 with multiprocessing.get_context('fork').Pool(4)as pool:
  rr=list(pool.imap(recover,[(i,p)for i,p in enumerate(ps)if i!=278]))
 o=dict(version=1,identity='NOVA24_UNIVERSAL_285_TREE_COVARIANCE_V1',
        parent_assignment=PARENT,parent_sha256=PH,records=rr,
        excluded_rooted_shapes=285,remaining_rooted_shapes=[list(ps[278])])
 b=encoded(o);Path('universal285.json').write_bytes(b)
 print('UNIVERSAL_285_SOURCE_RECONSTRUCTION_PASS',len(rr),sum(56*len(r['apices'])for r in rr))
 print('DATA',len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
