"""Find strict reference110 cells of a fixed literal physical polyhedron.
All candidate cells are expressed through affine primitive equilibrium guards.
This is preparation for actual homogeneous centroid closure, never completion.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from scipy.optimize import linprog
from sources.N40.N40_RECOVER import affine_guards,census

def run(source,out,trials):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads(source.read_text());X=[tuple(mpq(v) for v in row) for row in a['raw_vertices']];C=tuple(mpq(v) for v in a['raw_centroid']);faces=a['faces'];owners={tuple(e):[] for e in a['edges']}
 for i,f in enumerate(faces):
  for v,w in zip(f,f[1:]+f[:1]):owners[tuple(sorted([v,w]))].append(i)
 K=dict(points=X,faces=faces,edges=a['edges'],edge_faces=list(owners.values()));groups=affine_guards(K);ss,us,_=groups
 def arrays(group):
  result=[]
  for fc in group:
   M=np.array([[float(v) for v in aa] for aa,b in fc]);b=np.array([float(v) for aa,v in fc]);scale=np.linalg.norm(M,axis=1);assert min(scale)>0;result.append((M/scale[:,None],b/scale))
  return result
 F=arrays(ss);V=arrays(us);x=np.array(X,float);c0=np.array(C,float);rg=np.linalg.norm(x-c0,axis=1).max();rng=np.random.default_rng(65426);baseS=a['stable_face_ids'];baseU=a['unstable_vertices'];best=np.inf;hist=[];start=time.time()
 for run in range(trials):
  rs=baseS[run%len(baseS)];ru=baseU[(run//len(baseS))%len(baseU)];c=c0.copy() if run<len(baseS) else c0+rng.normal(size=3)*rg*min(.5,run/trials);sigma=1e-7*rg
  for it in range(40):
   rows=[];rhs=[]
   for group,root in [(F,rs),(V,ru)]:
    for i,(A,b) in enumerate(group):
     if i==root:
      rows.extend(A);rhs.extend(b-sigma)
     else:
      values=b-A@c
      if it==0 and min(values)>0:k=int(rng.integers(len(b)))
      else:k=int(values.argmin())
      rows.append(-A[k]);rhs.append(-b[k]-sigma)
   # Interior support constraints remain physical, independent of the cell.
   for n,h in zip(a['normals'],a['offsets']):
    nn=np.array([float(mpq(v)) for v in n]);sc=np.linalg.norm(nn);rows.append(nn/sc);rhs.append(float(mpq(h))/sc-sigma)
   A=np.array(rows);b=np.array(rhs);m=len(b);AA=np.block([[A,-np.eye(m),np.zeros((m,1))],[np.eye(3),np.zeros((3,m)),-np.ones((3,1))],[-np.eye(3),np.zeros((3,m)),-np.ones((3,1))]]);bb=np.r_[b,c0,-c0];obj=np.r_[np.zeros(3),np.ones(m),.001];res=linprog(obj,A_ub=AA,b_ub=bb,bounds=[(None,None)]*3+[(0,None)]*m+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10})
   assert res.success;cc=res.x[:3];merit=float(res.x[3:3+m].sum());move=np.linalg.norm(cc-c);c=cc
   if merit<1e-10:
    rc=tuple(mpq(int(round(v*1e12)),10**12) for v in c);ce=census(K,rc);own_distance=float(np.linalg.norm(c-c0));record=dict(run=run,it=it,S=rs,U=ru,centroid_distance=own_distance,reference_census=ce,reference_center=list(map(str,rc)),own_centroid=list(map(str,C)),source=str(source.resolve()),seconds=time.time()-start);hist.append(record)
    if ce['strict']==[1,1,0] and ce['weak']==[0,0,0] and own_distance<best:
     best=own_distance;(out/'best_reference.json').write_text(json.dumps(record,indent=2));np.save(out/'best_reference_points.npy',x-np.array(rc,float));print('EXACT_REFERENCE110_NOT_OWN',own_distance,rs,ru,flush=True)
    break
   if move<1e-10:break
  if run%20==0:print('REFERENCE_CENTER',run,'best',best,flush=True)
 (out/'references.json').write_text(json.dumps(hist,indent=2));print('REFERENCE_SEARCH_DONE',len(hist),'best',best,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--trials',type=int,default=150);a=p.parse_args();run(a.input,a.out,a.trials)
