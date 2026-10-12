"""Direct stable-root feasibility with an actual-centred primal Thales chart.

Strict primal escape is imposed algebraically at reference zero, and each
accepted physical body is separately projected to its actual volume centroid.
The objective uses maximum-escape deficits on all facets. Its continuity claim
is local to a fixed set of distinct facet covectors; a hull change is evaluated
on the new physical body and is not assigned the old chart's census.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from primal_log_thales import Chart,evaluate,metric,project
from support_geometry import escape
from vertex_geometry import geometry
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def guards(e,angular):
 v,j,J=escape(e['H'],e['DH'],angular=angular);root=int(np.argmax(np.sum(e['H']**2,axis=1)));keep=np.arange(len(v))!=root
 return v[keep],J[keep],root

def run(source,out,steps,eps,angular,constrained_projection=False):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);g=geometry(np.load(source),False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));assert len(X)<=84;c=Chart(X);z=c.z0.copy();np.save(out/'initial.npy',X);(out/'method.json').write_text(json.dumps(dict(source=source,epsilon=eps,angular=angular,centroid_tolerance=1e-14,radial_log_margin=1e-10),indent=2));trust=.04;hist=[];start=time.time()
 projection=project
 if constrained_projection:
  from constrained_mass_projection import project as projection
  (out/'projection.json').write_text(json.dumps(dict(method='LP centroid correction with radial and interior bounds',rho_floor=1e-9),indent=2))
 for it in range(steps):
  e=evaluate(c,z,.01);v,J,root=guards(e,angular);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,merit=merit,minimum=float(min(v)),Q=max(e['Q'],default=0.),S=e['S'],U=e['U'],mass_norm=float(np.linalg.norm(e['g'])),V=len(e['vertices']),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',e['X']);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('THALES_STABLE_FEASIBILITY',out,row,flush=True)
  assert e['U']==1 and np.linalg.norm(e['g'])<1e-12
  if e['S']==1 and min(v)>eps*.9:
   np.save(out/'potential.npy',e['X']);print('THALES_STABLE_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
  W,sx=metric(e);d=len(z);m=len(v);I=eye(d);O=csr_matrix((d,m));rad=np.arange(2,d,3);R=np.vstack((-e['DI']@W,W[rad],-W[rad]));bR=np.r_[e['inside']*.9,-1e-10-z[rad],z[rad]+25];n=len(bR);sc=.001
  A=vstack([hstack([-csr_matrix(J@W/sc),-eye(m),csr_matrix((m,d))]),hstack([csr_matrix(R),csr_matrix((n,m+d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/sc,bR,np.zeros(2*d)];AE=hstack([csr_matrix(e['Dg']@W/sx),csr_matrix((3,m+d))]);obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];bound=trust/np.sqrt(d);sol=linprog(obj,A_ub=A,b_ub=b,A_eq=AE,b_eq=-e['g']/sx,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=OPT)
  if not sol.success:row['error']=sol.message;trust*=.4;continue
  dz=W@sol.x[:d];ok=False
  for k in range(16):
   try:zz,ee=projection(c,z+2.**-k*dz,.01);vv,_,_=guards(ee,angular)
   except (ValueError,np.linalg.LinAlgError):continue
   mm=float(np.maximum(eps-vv,0).sum())
   if ee['U']==1 and mm<merit-max(1e-14,merit*1e-7):
    z=zz;ok=True;row.update(alpha=2.**-k,new_merit=mm)
    if k==0:trust=min(.4,trust*1.2)
    break
  if not ok:trust*=.4
  if trust<1e-9:break
  if ok and it%10==9:
   X=ee['X'][ee['vertices']];c=Chart(X);z=c.z0.copy();(out/f'rechart{it}.json').write_text(json.dumps(dict(parent=c.parent.tolist(),root=c.root,tetra=c.tetra.tolist())))
 print('THALES_STABLE_FEASIBILITY_DONE',out,hist[-1],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=1000);p.add_argument('--epsilon',type=float,default=1e-8);p.add_argument('--angular',action='store_true');p.add_argument('--constrained-projection',action='store_true');a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon,a.angular,a.constrained_projection)
