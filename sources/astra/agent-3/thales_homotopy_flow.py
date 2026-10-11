"""Feasible predictor/retraction flow for homogeneous centroid closure.
Linear constraints nominate a step. Every accepted finite body has its own
uniform mass reintegrated and both complete reference equilibrium tests checked.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from thales_centroid_homotopy import Homotopy
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def retract(s,w,lam):
 w=w.copy();w[-1]=lam;d=len(w)-1
 for it in range(15):
  e,DE,v,DV,X,info=s.calc(w);merit=np.linalg.norm(e,1)+np.maximum(-v,0).sum()
  if np.linalg.norm(e)<1e-9 and min(v)>-s.eps*.05 and info['reference_S']==info['reference_U']==1:return w,True,it
  m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001
  A=vstack([hstack([-csr_matrix(DV[:,:-1]/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[v/scale,np.zeros(2*d)];AE=hstack([csr_matrix(DE[:,:-1]),csr_matrix((3,m+d))],format='csr');obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-6)]
  sol=linprog(obj,A_ub=A,b_ub=b,A_eq=AE,b_eq=-e,bounds=[(-.03,.03)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:return w,False,it
  dx=np.r_[sol.x[:d],0.];good=False
  for alpha in [1.,.5,.25,.125,.0625,.03125]:
   ww=w+alpha*dx;ee,_,vv,_,_,_=s.calc(ww);mm=np.linalg.norm(ee,1)+np.maximum(-vv,0).sum()
   if mm<merit*(1-1e-5):w=ww;good=True;break
  if not good:return w,False,it
 return w,False,15

def run(source,out,steps,eps,resume=None):
 X=np.load(source)
 if resume is None:X/=np.max(np.linalg.norm(X,axis=1))
 s=Homotopy(X,out,eps);lam0=0.
 if resume is not None:
  base=Path(resume);s.g0=np.array(json.loads((base/'construction.json').read_text())['g_initial']);s.scale=np.linalg.norm(s.g0)
  # Infer lambda from this saved physical body, never from a possibly newer
  # separately written checkpoint metadata file.
  from vertex_geometry import geometry
  lam0=1-float(geometry(X,False)['g']@s.g0/(s.g0@s.g0));(s.out/'resume.json').write_text(json.dumps(dict(source=str(base),lambda_start=lam0,g_initial=s.g0.tolist()),indent=2));meta=json.loads((s.out/'construction.json').read_text());meta['g_initial']=s.g0.tolist();(s.out/'construction.json').write_text(json.dumps(meta,indent=2))
 w=np.r_[s.c.z0,lam0];s.callback(w);trust=.01;records=[]
 for it in range(steps):
  e,DE,v,DV,X,info=s.calc(w);d=len(w);I=eye(d);scale=.001;floor=np.minimum(v*.98,0.);A=vstack([hstack([-csr_matrix(DV/scale),csr_matrix((len(v),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[(v-floor)/scale,np.zeros(2*d)];AE=hstack([csr_matrix(DE),csr_matrix((3,d))],format='csr');obj=np.r_[np.zeros(d-1),-1.,np.full(d,1e-7)]
  bounds=[(-trust,trust)]*(d-1)+[(0,min(.02,1-w[-1]))]+[(0,None)]*d;sol=linprog(obj,A_ub=A,b_ub=b,A_eq=AE,b_eq=-e,bounds=bounds,method='highs',options=OPT)
  if not sol.success:trust*=.5;records.append(dict(it=it,status='predictor infeasible',message=sol.message));continue
  dw=sol.x[:d];accepted=False
  if dw[-1]<1e-12:trust*=.5
  else:
   for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
    ww=w+alpha*dw;ww,ok,corr=retract(s,ww,ww[-1])
    if ok and ww[-1]>w[-1]+1e-10:
     w=ww;accepted=True;s.callback(w);records.append(dict(it=it,lambda_value=float(w[-1]),alpha=alpha,corrections=corr,trust=trust));
     if alpha==1:trust=min(trust*1.2,.1)
     break
   if not accepted:trust*=.4
  (s.out/'flow.json').write_text(json.dumps(records,indent=2))
  if it%10==0:print('FEASIBLE_HOMOTOPY',it,'lambda',w[-1],'trust',trust,flush=True)
  if w[-1]>1-1e-10:
   np.save(s.out/'lambda_one_requires_exact.npy',s.calc(w)[4]);print('LAMBDA_ONE_REQUIRES_EXACT_PHYSICAL_AUDIT',flush=True);break
  if trust<1e-9:break
 print('FEASIBLE_HOMOTOPY_DONE','lambda',w[-1],'trust',trust,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);p.add_argument('--epsilon',type=float,default=1e-8);p.add_argument('--resume');a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon,a.resume)
