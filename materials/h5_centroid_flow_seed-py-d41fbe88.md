# material-d41fbe881b2e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact global actual-centroid flow at the H5 all-single-cut barrier.
Requires the unchanged h5_path_schur_barrier.py in the same directory.
Python>=3.11 standard library. Optional --locate: NumPy2.3.5/SciPy1.17.0.
"""
from pathlib import Path
import hashlib,argparse,json
BASE='f9d94c90a9b70bc248e93424433d3776978acc9af6655d170b38b78c5b48ca42'
f=Path(__file__).with_name('h5_path_schur_barrier.py')
if not f.exists()or hashlib.sha256(f.read_bytes()).hexdigest()!=BASE:raise RuntimeError('Missing or altered exact base source.')
from h5_path_schur_barrier import (F,POINT,TREE,PAIRS,geometry,add,sub,mul,sym,outer,minors,
 component,integer_matrix,point_fidelity,save,product)

def locate():
 import numpy as np
 import scipy
 from scipy.optimize import linprog
 def matrix(row):
  A=np.zeros((3,3))
  for (i,j),v in zip(PAIRS,row):A[i,j]=A[j,i]=float(v)
  return A
 z,V,J=geometry(POINT);U=tuple(sub(v,mul(1/V,J))for v in z);parent=dict(TREE);mats=[]
 for i in range(10):
  k=i;path=[]
  while k!=2:path.append((k,parent[k]));k=parent[k]
  mats.append(matrix(add(*(mul(-1,sym(U[a],sub(U[b],U[a])))for a,b in path)))if path else np.zeros((3,3)))
 mats=np.array(mats);u=np.array(U,float)
 ds=[np.array(v,float)/np.linalg.norm(v)for v in product((-1,0,1),repeat=3)if any(v)]
 rows=[np.r_[-np.einsum('i,kij,j->k',v,mats,v),1.]for v in ds]
 eq=np.zeros((4,11));eq[0,:10]=1;eq[1:,:10]=u.T
 for iteration in range(150):
  sol=linprog(np.r_[np.zeros(10),-1.],A_ub=rows,b_ub=np.zeros(len(rows)),A_eq=eq,b_eq=[1,0,0,0],bounds=[(0,None)]*10+[(None,None)],method='highs')
  if not sol.success:raise RuntimeError(sol.message)
  C=np.einsum('i,ijk->jk',sol.x[:10],mats);ev,vs=np.linalg.eigh(C)
  if ev[0]>1e-9:break
  if sol.x[-1]<1e-9 or sol.x[-1]-ev[0]<1e-10:raise RuntimeError('Numerical flow proposal lacks a strict gap.')
  v=vs[:,0];rows.append(np.r_[-np.einsum('i,kij,j->k',v,mats,v),1.])
 else:raise RuntimeError('Numerical iteration limit reached.')
 print('H5_GLOBAL_CENTROID_FLOW_OPTIONAL_LOCATION_PASS',np.__version__,scipy.__version__,iteration)

def main(out):
 if not __debug__:raise RuntimeError('Assertions required; do not use -O.')
 out.mkdir(parents=True,exist_ok=True)
 z,V,J=geometry(POINT);g=mul(1/V,J);u=tuple(sub(v,g)for v in z)
 x,r,p,q,l=POINT;s=1-l;w=[F(0)]*10
 w[6]=F(1,10);w[8]=g[2]
 w[2]=(g[0]-w[6]*z[6][0]-w[8]*l)/(s*(1-p))
 w[4]=(g[1]-w[6]*z[6][1]-w[2]*z[2][1]-(1-w[6]-w[8]-w[2])*z[5][1])/(z[4][1]-z[5][1])
 w[5]=1-sum(w)
 assert sum(w)==1 and min(w)>=0 and add(*(mul(a,v)for a,v in zip(w,z)))==g
 expected={2:F(8298396377,30462980800),4:F(5759595581,38078726000),5:F(32379219391,152314904000),6:F(1,10),8:F(647965,2456692)}
 assert {i:a for i,a in enumerate(w)if a}==expected
 flows=[(a,b,sum(w[i]for i,d in component(a)))for a,b in TREE]
 C=add(*(mul(-m,sym(u[a],sub(u[b],u[a])))for a,b,m in flows))
 K=add(*(mul(a,outer(v))for a,v in zip(w,u)))
 E=add(*(mul(m,outer(sub(u[b],u[a])))for a,b,m in flows))
 rhs=mul(F(1,2),sub(add(K,E),outer(u[2])))
 assert C==rhs and min(minors(C))>0
 assert w[2]!=F(1,4)
 report={'title':'H5_GLOBAL_CENTROID_FLOW_PASSES_LOCAL_CUT_BARRIER_POINT_V1','base_sha256':BASE,
  'parameters':POINT,'tree':TREE,'volume':V,'first_moment':J,'centroid':g,'vertices':z,
  'fidelity':point_fidelity(z,V,J),'centroid_weights':w,'flows':flows,'C':integer_matrix(C),
  'identity_entries':6,'scope':'One actual rational body and T56, not a uniform parameter domain or all roots. Root mass need not equal1/4; no fixed-centroid substitution.'}
 pin=save(out/'h5_centroid_flow_seed_report.json',report)
 print('H5_GLOBAL_ACTUAL_CENTROID_FLOW_EXACT_PASS',4,6,3)
 print(json.dumps(pin,sort_keys=True))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('out',type=Path,nargs='?',default=Path('flow-output'));ap.add_argument('--locate',action='store_true');args=ap.parse_args()
 if args.locate:locate()
 main(args.out)
