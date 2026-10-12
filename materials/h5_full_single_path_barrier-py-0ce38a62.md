# material-0ce38a627507

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""All nine full unit-path cut cones fail, but two cuts separate actual H5.
Requires the exact h5_path_schur_barrier.py source named below, in this directory.
Python>=3.11, standard library, assertions enabled. No generated input files.
Optional --locate uses NumPy2.3.5 / SciPy1.17.0 for discovery only.
"""
from pathlib import Path
import hashlib, argparse, json
BASE_SHA='f9d94c90a9b70bc248e93424433d3776978acc9af6655d170b38b78c5b48ca42'
base=Path(__file__).with_name('h5_path_schur_barrier.py')
if not base.exists() or hashlib.sha256(base.read_bytes()).hexdigest()!=BASE_SHA:
 raise RuntimeError('Supply the complete unchanged h5_path_schur_barrier.py, SHA '+BASE_SHA)
from h5_path_schur_barrier import (F,P,PAIRS,TREE,POINT,PRISM,FAN,FACES,EDGES,geometry,
 component,var,add,sub,mul,dot,sym,cross,minors,rectangular,integer_matrix,
 point_fidelity,save,clean,product)

TITLE='H5_ALL_FULL_UNIT_PATH_CUTS_FAIL_BUT_TWO_CUTS_SUFFICE_V1'
OMEGA=tuple((x-F(1,2048),x+F(1,2048))for x in POINT)
RAY_GAP=F(1,65536)
PAIR_GAP=F(1,2048)
PAIR_WEIGHTS=((0,1,2),(1,2,2),(5,6,5),(7,0,2))
DUALS={
 0:(388629,-480023,-54147,599940,68524,11431),
 1:(531828,-494838,-59369,461155,55240,7016),
 3:(478306,408762,280337,356112,238960,165582),
 4:(479085,298864,-357016,202306,-218627,318609),
 5:(72460,163193,139487,539916,438721,387623),
 6:(41736,-121836,-111543,476927,457984,481337),
 7:(49465,-199365,-24047,926335,109643,24200),
 8:(875956,-12831,289409,15924,6946,108120),
 9:(139748,283470,160780,657967,361955,202285)}
DEN=1000000

def trace(A,B):return sum(a*b*(1 if i==j else 2)for a,b,(i,j)in zip(A,B,PAIRS))
def generators(a):
 parent=dict(TREE);out=[('exit',((a,parent[a]),))]
 for i,d in component(a):
  if not d:continue
  path=[];k=i
  while k!=a:path.append((k,parent[k]));k=parent[k]
  out.append((i,tuple(path)))
 return out

def extensions():
 fixed={a:b for a,b,_ in PAIR_WEIGHTS}
 adj={i:tuple(b if a==i else a for a,b in EDGES if i in(a,b))for i in range(10)}
 out=[]
 for root in range(10):
  if root in fixed:continue
  free=[i for i in range(10)if i!=root and i not in fixed]
  for targets in product(*(adj[i]for i in free)):
   parent=dict(fixed);parent.update(zip(free,targets));ok=True
   for i in range(10):
    k=i;seen=set()
    while k!=root:
     if k in seen:ok=False;break
     seen.add(k);k=parent[k]
    if not ok:break
   if ok:out.append((root,tuple(sorted(parent.items()))))
 assert len(out)==439 and (2,TREE)in out
 counts=[sum(root==i for root,_ in out)for i in range(10)]
 assert counts==[0,0,176,90,46,0,23,0,56,48]
 return out,counts

def locate():
 import numpy as np
 import scipy
 from scipy.optimize import linprog
 def matrix(row):
  A=np.zeros((3,3))
  for (i,j),v in zip(PAIRS,row):A[i,j]=A[j,i]=float(v)
  return A
 def feat(v):return np.array([v[i]*v[j]*(1 if i==j else 2)for i,j in PAIRS])
 def feath(A):return np.array([A[i,j]*(1 if i==j else 2)for i,j in PAIRS])
 z,V,J=geometry(POINT);u=tuple(sub(v,mul(1/V,J))for v in z)
 for a,b in TREE:
  mats=np.array([matrix(mul(-1,add(*(sym(u[i],sub(u[j],u[i]))for i,j in path))))for _,path in generators(a)])
  vecs=[np.array(v,float)for v in product((-1,0,1),repeat=3)if any(v)]
  rows=[np.r_[feath(A),1.]for A in mats]+[np.r_[-feat(v),float(v@v)]for v in vecs]
  for iteration in range(100):
   sol=linprog(np.r_[np.zeros(6),-1.],A_ub=rows,b_ub=np.zeros(len(rows)),
       A_eq=[[1.,0,0,1,0,1,0]],b_eq=[1.],bounds=[(None,None)]*7,method='highs')
   if not sol.success:raise RuntimeError(sol.message)
   M=matrix(sol.x[:6]);ev,vs=np.linalg.eigh(M)
   if ev[0]>1e-8 and min(-np.einsum('ij,kji->k',M,mats))>1e-8:break
   if sol.x[-1]<1e-9:raise RuntimeError('Numerical dual locator lacks a strict gap.')
   v=vs[:,0];rows.append(np.r_[-feat(v),float(v@v)])
  else:raise RuntimeError('Numerical dual iteration limit reached.')
  proposed=tuple(int(round(v*DEN))for v in sol.x[:6])
  if proposed!=DUALS[a]:raise RuntimeError('Rediscovery differs from the literal accepted dual; exact main remains available.')
 print('H5_FULL_UNIT_PATH_DUAL_REDISCOVERY_PASS',np.__version__,scipy.__version__,9)

def main(out):
 if not __debug__:raise RuntimeError('Assertions must be enabled; do not use -O.')
 out.mkdir(parents=True,exist_ok=True)
 pt=tuple(var(i)for i in range(5));z,V,J=geometry(pt)
 vf=P(0);jf=(P(0),)*3
 for ids in FAN:
  a,b,c,d=(z[i]for i in ids);dv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
  vf+=dv;jf=add(jf,mul(dv/4,add(*(z[i]for i in ids))))
 assert V==vf and all(x==y for x,y in zip(J,jf))
 rows=[];labels=[];certs=[]
 pz,pV,pJ=geometry(POINT);pu=tuple(sub(v,mul(1/pV,pJ))for v in pz)
 for a,b in TREE:
  M=tuple(F(v,DEN)for v in DUALS[a]);mm=minors(M);assert min(mm)>0
  point_values=[]
  for label,path in generators(a):
   H=add(*(sym(sub(mul(V,z[i]),J),sub(z[j],z[i]))for i,j in path))
   rows.append(P(trace(M,H)-RAY_GAP));labels.append((a,label,path))
   HH=add(*(sym(pu[i],sub(pu[j],pu[i]))for i,j in path))
   val=trace(M,HH);assert val>0;point_values.append((label,val))
  certs.append({'source':a,'target':b,'matrix':integer_matrix(M),'point_ray_values':point_values})
 rn,rd,rg=rectangular(rows,OMEGA)
 assert len(rows)==19 and rg==(3,3,3,3,4)and len(rn)==1280
 assert min(v for row in rn for v in row)>0
 guard_pin=save(out/'h5_full_unit_path_dual_guards.json',{'omega':OMEGA,'gap_in_V_trace':RAY_GAP,'degrees':rg,
  'labels':labels,'denominator':rd,'coefficient_numerators':rn,'duals':certs})
 C=add(*(mul(-w,sym(sub(mul(V,z[a]),J),sub(z[b],z[a])))for a,b,w in PAIR_WEIGHTS))
 shifted=[v-(PAIR_GAP if i==j else 0)for v,(i,j)in zip(C,PAIRS)]
 cn,cd,cg=rectangular(shifted,PRISM)
 assert cg==(3,2,3,2,4)and len(cn)==720
 mins=None
 for row in cn:
  mm=minors(row);assert min(mm)>0
  mins=mm if mins is None else tuple(min(a,b)for a,b in zip(mins,mm))
 matrix_pin=save(out/'h5_two_unit_path_cut_matrices.json',{'prism':PRISM,'weights':PAIR_WEIGHTS,
  'gap_in_VC':PAIR_GAP,'degrees':cg,'denominator':cd,'upper_numerators':cn})
 # Explicit two-cut decomposition: cut1 exit eta=2 plus descendant7 path weight2;
 # cut5 exit eta=5. Both use mu_source=1 and all other mu=0.
 ga=dict(generators(1));assert ga['exit']==((1,2),)and ga[7]==((7,0),(0,1))
 combined={}
 for factor,path in [(2,ga['exit']),(2,ga[7]),(5,dict(generators(5))['exit'])]:
  for e in path:combined[e]=combined.get(e,0)+factor
 assert combined=={(a,b):w for a,b,w in PAIR_WEIGHTS}
 trees,counts=extensions()
 pointC=add(*(mul(-w,sym(pu[a],sub(pu[b],pu[a])))for a,b,w in PAIR_WEIGHTS))
 assert min(minors(pointC))>0
 assert all(PRISM[i][0]<OMEGA[i][0]<OMEGA[i][1]<PRISM[i][1]for i in range(5))
 report={'title':TITLE,'base_source_sha256':BASE_SHA,'facets':FACES,'edges':EDGES,'fan':FAN,'tree':TREE,
  'moment_identities':4,'point':{'parameters':POINT,'volume':pV,'first_moment':pJ,'centroid':mul(1/pV,pJ),
   'fidelity':point_fidelity(pz,pV,pJ),'two_cut_matrix':integer_matrix(pointC)},
  'single_cut_failure':{'omega':OMEGA,'matrices':certs,'positive_metric_minors':27,'rays':19,
   'positive_scalar_coefficients':24320,'gap_in_V_trace':RAY_GAP,
   'minimum_shifted_scalar_coefficient':F(min(v for row in rn for v in row),rd),
   'scope':'All eta,v,mu in each full rational UNIT-path cut, NOT arbitrary weighted path identities or sums of cuts.'},
  'two_cut_success':{'prism':PRISM,'weights':PAIR_WEIGHTS,'weight_sum':11,'gap_in_VC':PAIR_GAP,
   'source_cuts':(1,5),'cut1_eta':2,'cut1_v7':2,'cut1_mu1':1,'cut5_eta':5,'cut5_mu5':1,
   'blocks':720,'positive_leading_minors':2160,'minimum_shifted_leading_minors':[F(v,cd**(i+1))for i,v in enumerate(mins)],
   'mean_arrow_gap':6*PAIR_GAP/11,'extension_total':439,'root_counts':counts,'complete_extensions':trees,
   'scope':'A439-tree subset of the earlier664 three-arrow extensions on the SAME prism; not extra coverage.'},
  'guard_file':guard_pin,'matrix_file':matrix_pin,'global_scope':'No full H5/all-root/E17 exclusion, actual weak-arrow survivor, or minimum/attainment improvement.'}
 pin=save(out/'h5_full_single_path_barrier_report.json',report)
 print('H5_FULL_UNIT_PATH_ACTUAL_FAN_IDENTITIES_PASS',4)
 print('H5_ALL_NINE_FULL_UNIT_PATH_CONES_FAIL_PASS',9,27,19,24320)
 print('H5_TWO_UNIT_PATH_CUTS_SUFFICE_PASS',720,2160,439)
 print('H5_ALL_FULL_UNIT_PATH_CUTS_FAIL_BUT_TWO_CUTS_SUFFICE_PASS')
 print(json.dumps({'report':pin,'guards':guard_pin,'matrices':matrix_pin},sort_keys=True))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('out',type=Path,nargs='?',default=Path('full-path-output'));ap.add_argument('--locate',action='store_true');args=ap.parse_args()
 if args.locate:locate()
 main(args.out)
