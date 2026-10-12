"""Finite mixed-integer correction of rounded free controls; proposals, not proofs."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,copy,hashlib,json,sys,platform
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
from scipy.optimize import milp,LinearConstraint,Bounds
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
sha=lambda x:hashlib.sha256(x).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('source',type=Path);ap.add_argument('proof',type=Path);ap.add_argument('out',type=Path);ap.add_argument('--grid',type=int,required=True);ap.add_argument('--radius',type=int,default=2);ap.add_argument('--goal',type=float,default=5e-9);ap.add_argument('--iterations',type=int,default=4);ap.add_argument('--seconds',type=float,default=60);ap.add_argument('--feasibility',action='store_true');a=ap.parse_args()
a.out.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(a.source/'methods'));sys.path.insert(0,str(a.source/'methods/parent'))
from flexible import FlexibleAtlas
import RECONSTRUCT
G0=json.loads((a.proof/'C622_ROUTED/GENERATOR.json').read_bytes());R=json.loads((a.proof/'C622_ROUTED/A.json').read_bytes());routes=json.loads((a.proof/'C622_ROUTED/ESCAPE.json').read_bytes())
assert sha(B(G0))=='3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7'
assert sha(B(R))=='142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0'
G=copy.deepcopy(G0);G['grid']=a.grid;G['controls']=[[round(F(v*a.grid,G0['grid'])) for v in row] for row in G0['controls']]
(a.out/'INPUT.json').write_bytes(B(dict(grid=a.grid,radius=a.radius,goal=a.goal,iterations=a.iterations,seconds=a.seconds,feasibility=a.feasibility,versions=[platform.python_version(),np.__version__,scipy.__version__],parent_generator_sha256=sha(B(G0)),parent_report_sha256=sha(B(R)),routes_sha256=sha(B(routes)))))
(a.out/'INITIAL_GENERATOR.json').write_bytes(B(G));history=[]
for it in range(a.iterations):
 raw=RECONSTRUCT.recover(G);Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,R,Q)
 s.base=np.array([G['controls'][i][k]/a.grid for i,k in s.free]);s.scale=np.ones(s.n);s.forcedp=dict(routes['physical']['witnesses']);s.forcedq=dict(routes['polar']['witnesses']);s.last=None
 v,J,geo=s.evaluate(np.zeros(s.n));m=s.mechlen-2;n=s.n
 row=dict(iteration=it,minimum_escape=float(v[:m].min()),root_margins=v[m:m+2].tolist(),nonowner_slack_min=float(geo['slack'].min()))
 print('INTEGER_SNAP_CURRENT',row,flush=True)
 if row['minimum_escape']>a.goal*.5 and min(row['root_margins'])>0 and row['nonowner_slack_min']>0:
  (a.out/'GENERATOR.json').write_bytes(B(G));(a.out/'raw.json').write_bytes(B(raw));(a.out/'HISTORY.json').write_bytes(B(history));print('INTEGER_SNAP_NUMERICAL_POSITIVE_ONLY',sha(B(G)),flush=True);break
 A=J[:m]/a.grid;b=np.full(m,a.goal)-v[:m];scale=np.maximum(np.linalg.norm(A,axis=1),1e-16);A=A/scale[:,None];b=b/scale
 AA=np.vstack([np.c_[A,np.zeros((m,n))],np.c_[np.eye(n),-np.eye(n)],np.c_[-np.eye(n),-np.eye(n)]])
 low=np.r_[b,np.full(2*n,-np.inf)];up=np.r_[np.full(m,np.inf),np.zeros(2*n)]
 c=np.r_[np.zeros(n),1+np.arange(n)*1e-6]
 if a.feasibility:c=np.zeros(2*n)
 res=milp(c,integrality=np.r_[np.ones(n),np.zeros(n)],bounds=Bounds(np.r_[np.full(n,-a.radius),np.zeros(n)],np.full(2*n,a.radius)),constraints=LinearConstraint(AA,low,up),options=dict(time_limit=a.seconds,mip_rel_gap=0.,presolve=True))
 row['solver']=dict(status=int(res.status),message=str(res.message),objective=None if res.fun is None else float(res.fun));print('INTEGER_SNAP_MILP',row['solver'],flush=True)
 if res.x is None:history.append(row);(a.out/'HISTORY.json').write_bytes(B(history));print('INTEGER_SNAP_NO_INCUMBENT',flush=True);break
 kk=np.rint(res.x[:n]).astype(int);row['linear_min_residual']=float((A@kk-b).min());row['corrections']=[[int(i),int(k),int(d)] for (i,k),d in zip(s.free,kk) if d]
 if row['linear_min_residual']< -1e-5:history.append(row);(a.out/'HISTORY.json').write_bytes(B(history));print('INTEGER_SNAP_REJECT_LINEAR',flush=True);break
 for (i,k),d in zip(s.free,kk):G['controls'][i][k]+=int(d)
 history.append(row);(a.out/f'GENERATOR_{it+1}.json').write_bytes(B(G));(a.out/'HISTORY.json').write_bytes(B(history))
else:print('INTEGER_SNAP_ITERATION_LIMIT',flush=True)
