"""Centroid-metric LP continuation with fixed positive identity floors.
Max witnesses may change; their floors do not fade. Full final audits are separate.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from centroid_metric import CentroidOrbit

def raw_exits(m,z):
 data=m.all_data(z)[3];vv=[];JJ=[]
 for (v,J,root),pad,n in zip(data,m.padded,m.ns):
  ids=pad[np.arange(n),np.argmax(np.r_[v,-np.inf][pad],axis=1)]
  vv.append(v[ids]);JJ.append(J[ids])
 return np.r_[*vv],np.concatenate(JJ),data

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--steps',type=int,default=400);p.add_argument('--trust',type=float,default=.03);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False);m=CentroidOrbit(a.report);z=np.r_[m.b0,np.zeros(5)]
 r=m.report;mainroot=int(np.argmax(np.sum((m.X-m.b0)**2,axis=1)));bad=next(i for i in r['unstable_vertices'] if i!=mainroot)
 saddle=r['saddle_edges'][0];assert bad in saddle;dst=next(i for i in saddle if i!=bad)
 ids=np.flatnonzero((m.edges[0][0]==bad)&(m.edges[0][1]==dst));assert len(ids)==1;goal=int(ids[0])
 v,J,_=raw_exits(m,z);healthy=np.array([i for i in range(len(v)) if i not in [mainroot,bad,m.ns[0]+r['stable_face_ids'][0]]]);assert (v[healthy]>0).all();floors=np.minimum(1e-6,.2*v[healthy]);floor_min=float(floors.min());print('FROZEN_FLOORS',floor_min,'target',bad,dst,flush=True)
 (out/'FLOORS.json').write_text(json.dumps(dict(identities=healthy.tolist(),floors=floors.tolist(),source=bad,target=dst,protected_root=mainroot),sort_keys=True))
 history=[];clock=time.monotonic()
 for k in range(a.steps):
  vals,J,data=raw_exits(m,z);objective=float(data[0][0][goal]);grad=data[0][1][goal]
  P,Y,JP,JY,info=m.geometry(z)
  Q=np.r_[JP.reshape(-1,8)/np.linalg.norm(P),JY.reshape(-1,8)/np.linalg.norm(Y)]
  U,s,Vt=np.linalg.svd(Q,full_matrices=False);T=Vt.T/np.maximum(s,s[0]*1e-5)
  A=-(J[healthy]@T);b=vals[healthy]-floors;scale=np.maximum(np.linalg.norm(A,axis=1),1e-10);A/=scale[:,None];b/=scale
  sol=linprog(-grad@T,A_ub=A,b_ub=b,bounds=[(-a.trust,a.trust)]*8,method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not sol.success:print('LP_STOP',sol.message,flush=True);break
  delta=T@sol.x;slope=float(grad@delta)
  if slope<1e-13:print('NO_POSITIVE_LINEARIZED_PROGRESS',slope,flush=True);break
  alpha=1.
  for back in range(60):
   try:
    zz=z+alpha*delta;values,jj,dd=raw_exits(m,zz);obj=float(dd[0][0][goal])
    if np.min(values[healthy]-floors)>=-1e-14 and obj>=objective+alpha*slope*.0001:
     z=zz;break
   except (ArithmeticError,ValueError,np.linalg.LinAlgError):pass
   alpha*=.5
  else:print('NONLINEAR_GUARD_STOP',flush=True);break
  info=m.all_data(z)[2];entry=dict(iteration=k,objective=obj,alpha=alpha,slope=slope,guard_excess=float(np.min(values[healthy]-floors)),**info);history.append(entry)
  with (out/'HISTORY.jsonl').open('a') as f:f.write(json.dumps(entry,sort_keys=True)+'\n')
  (out/'FINAL.json').write_text(json.dumps(entry,sort_keys=True))
  if len(info['U'])==len(info['S'])==1 and info['min_nonroot']>1e-8:
   (out/'NUMERICAL_WINNER.json').write_text(json.dumps(entry,sort_keys=True));print('NUMERICAL_ONLY_110',flush=True);break
  if k%10==0:print(k,obj,alpha,info['min_den'],info['condition'],info['U'],info['S'],flush=True)
  if alpha*np.linalg.norm(delta)<1e-12:print('FINITE_STEP_STOP',flush=True);break
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));(out/'SUMMARY.json').write_text(json.dumps(dict(accepted_steps=len(history),seconds=time.monotonic()-clock),sort_keys=True));print('GUARDED_CENTROID_METRIC_CONTINUATION_FINISHED',len(history),flush=True)
if __name__=='__main__':main()
