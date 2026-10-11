"""Finite stable-cap additions with the primary cap tetrahedron held fixed.
Other physical vertices correct the actual homogeneous mass and equilibrium guards.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from pathlib import Path
from fractions import Fraction as R
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from constrained_p_flow import feature
from polish_121 import guards,persistent_root
OPTIONS={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def retract(X,roots,fixed,out,eps=1e-6,steps=200):
 out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);cols=np.array([3*i+k for i in range(len(X)) if i not in fixed for k in range(3)]);trust=.002;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(X);v,J,cl=guards(g,roots);J=J[:,cols];merit=np.maximum(eps-v,0).sum();row=dict(it=it,minimum=float(v.min()),merit=float(merit),S=cl[1],U=cl[0],trust=trust,elapsed=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if v.min()>eps*.85:
   np.save(out/'success.npy',X);row['relative_basin']=feature(g,False)[0];(out/'success.json').write_text(json.dumps(row,indent=2));print('FINITE_CAP_STRICT121',out,row,flush=True);return True
  d=len(cols);m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=np.zeros(X.size);dx[cols]=sol.x[:d];dx=dx.reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   xx=X+alpha*dx;vv,_,cc=guards(geometry(xx,False),roots,False);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-6):X=xx;ok=True;row['alpha']=alpha;break
  if ok and alpha==1:trust=min(.03,trust*1.2)
  if not ok:trust*=.5
  if trust<1e-10:break
 print('FINITE_CAP_NONWINNER',out,hist[-1],flush=True);return False

source=Path('artifacts/projected_pflow1/exact_g9/audit.json');a=json.load(open(source));X=np.array([[float(R(v)) for v in row] for row in a['raw_vertices']]);g=np.array([float(R(v)) for v in a['raw_centroid']]);f=a['stable_face_ids'][0];face=a['faces'][f];n=np.array([float(v) for v in a['normals'][f]]);h=float(a['offsets'][f]);normal=n*((h-n@g)/(n@n));foot=g+normal;roots=persistent_root(geometry(X,False));elder=roots[0];assert elder in face
for t in [.25,.5,.75]:
 for ep in [1e-4,.001,.01,.03,.1,.3]:
  point=(1-t)*foot+t*X[elder]+ep*normal;Y=np.vstack((X,point));out=Path(f'artifacts/finite_stable_cap/t{t:g}_e{ep:g}');meta=dict(parent=str(source),t=t,epsilon=ep,fixed=face+[len(X)],roots=roots)
  success=retract(Y,roots,face+[len(X)],out);(out/'input.json').write_text(json.dumps(meta,indent=2))
