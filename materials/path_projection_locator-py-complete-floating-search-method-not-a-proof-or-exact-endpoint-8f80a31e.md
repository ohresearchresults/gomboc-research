# material-8f80a31e11a5

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Floating locator for chain projection certificates; no floating outcome is proof.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONHASHSEED=0 python path_projection_locator.py
Inputs are exactly the finite plan below and the specified zero-randomness initial point.
Output contains all full-precision floating results, including negative/failed searches.
"""
from itertools import combinations
from pathlib import Path
import hashlib,json,os,platform,sys
import numpy as np
import scipy
from scipy.optimize import minimize
HERE=Path(__file__).resolve().parent

def locate(m,terms):
    mats=np.zeros((m+1,m+1,m+1));mats[0,0,0]=1
    constant=np.zeros((m+1,m+1))
    for t in terms:constant[0,t]=constant[t,0]=.5
    for j in range(1,m+1):
        mats[j,j,j]=1;mats[j,j,j-1]=mats[j,j-1,j]=-.5
    def con(z):return np.linalg.eigvalsh(constant+np.einsum('i,ijk->jk',z,mats))
    def jac_con(z):
        values,vectors=np.linalg.eigh(constant+np.einsum('i,ijk->jk',z,mats))
        return np.einsum('ij,kil,lj->jk',vectors,mats,vectors)
    gradient=np.array([1.]+[0.]*m)
    answer=minimize(lambda z:z[0],np.array([10.]+[1.]*m),jac=lambda z:gradient,
      method='SLSQP',bounds=[(0,None)]*(m+1),
      constraints={'type':'ineq','fun':con,'jac':jac_con},
      options={'ftol':1e-12,'maxiter':1000})
    return {'terms':terms,'chain_length':m,'success':bool(answer.success),
      'message':str(answer.message),'B':float(answer.fun),'x':answer.x.tolist(),
      'min_eigenvalue':float(con(answer.x)[0]),'iterations':int(answer.nit)}

def main():
    # Initial seven targets supplied the three small exact certificates.
    initial=[(5,6),(4,6),(3,6),(3,4,6),(3,5,6),(2,5,6),(4,5,6)]
    # Larger systematic pass covers every pair/triple of depths in a nine-edge chain.
    plan=[('initial',t) for t in initial]+[('systematic',t) for k in(2,3) for t in combinations(range(1,10),k)]
    records=[]
    for phase,terms in plan:
        row=locate(max(terms),terms);row['phase']=phase;records.append(row)
        print(phase,terms,row['success'],row['B'],row['min_eigenvalue'],flush=True)
    obj={'identity':'MINIMUM_PATH_PROJECTION_FLOAT_LOCATOR_V1',
      'python':sys.version,'platform':platform.platform(),'numpy':np.__version__,
      'scipy':scipy.__version__,'blas':np.__config__.CONFIG,
      'environment':{k:os.environ.get(k) for k in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','PYTHONHASHSEED')},
      'records':records,'status':'Floating search history only. Rational positive-definiteness and physical triangulation proofs are independent requirements.'}
    data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    (HERE/'path_projection_locator.json').write_bytes(data)
    print('PATH_PROJECTION_FLOAT_LOCATOR_HISTORY',len(records),len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
