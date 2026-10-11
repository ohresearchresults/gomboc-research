"""Large-scale polynomial deformation modes in a complete physical contact chart.
Predictor uses48 projected polynomial modes; strict nonlinear correction uses
the entire exact-incidence chart. Actual uniform mass enters every evaluation.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd,qr
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from contact_numpy import Chart
from polynomial_body_search import features
from section_polish import roots
from support_geometry import escape
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def basis(c,g):
 sx=np.sqrt(np.mean(g['X']**2));sy=np.sqrt(np.mean(g['Y']**2));M=np.vstack((g['DX'].reshape(-1,c.d)/sx,g['DY'].reshape(-1,c.d)/sy,.05*np.eye(c.d)));_,d,V=svd(M,full_matrices=False,check_finite=False);W=V.T/d;X=g['X']-g['centroid'];X/=np.max(np.linalg.norm(X,axis=1));F=features(X);F-=F.mean(0);F/=np.maximum(np.sqrt(np.mean(F*F,axis=0)),1e-12);target=np.kron(F,np.eye(3));R=(g['DX'].reshape(-1,c.d)@W/sx).T@target;Q,_=qr(R,mode='economic');return W,W@Q
def guards(c,g,rr):
 vals=[];Js=[];cl=[]
 for A,DA,root in [(g['Z'],g['DZ'],rr[0]),(g['H'],g['DH'],rr[1])]:
  v,j,J=escape(A,DA,angular=True);mask=np.ones(len(A),bool);mask[root]=False;vals.append(v[mask]);Js.append(J[mask]);cl.append(int(np.sum(v<0)))
 return np.r_[tuple(vals)],np.vstack(Js),cl
def correct(c,q,W,rr,eps,gapfloor):
 d=c.d
 for it in range(12):
  g=c.physical(q,require_valid=False);v,J,cl=guards(c,g,rr);values=np.r_[g['noncontact'],v];targets=np.r_[np.full(len(g['noncontact']),gapfloor),np.full(len(v),eps)];JJ=np.vstack((g['Dgap'][~c.incidence],J))@W;merit=float(np.maximum(targets-values,0).sum());bound=.03/np.sqrt(d)
  if g['valid'] and min(v)>eps*.9 and min(g['noncontact'])>gapfloor*.9:return q,True,it
  keep=values-targets<=bound*np.sum(abs(JJ),axis=1)+1e-10;VV=values[keep];TT=targets[keep];J0=JJ[keep];m=len(VV);I=eye(d);O=csr_matrix((d,m));sc=.001;A=vstack([hstack([-csr_matrix(J0/sc),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(VV-TT)/sc,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:return q,False,it
  dq=W@sol.x[:d];ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125]:
   qq=q+alpha*dq
   try:gg=c.physical(qq,require_valid=False);vv,_,_=guards(c,gg,rr);val=np.r_[gg['noncontact'],vv];mm=np.maximum(targets-val,0).sum()
   except (ValueError,np.linalg.LinAlgError):continue
   if np.isfinite(mm) and mm<merit*(1-1e-5):q=qq;ok=True;break
  if not ok:return q,False,it
 return q,False,12

def run(source,out,steps,eta,eps,gapfloor,target='211',all_controls=False):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();hist=[];start=time.time();trust=.03;g=c.physical(q)
 rr=[roots(g['Z'],c.pe,1 if target=='211' else 2),roots(g['H'],c.qe,2 if target=='211' else 1)]
 (out/'source_construction.json').write_text(Path(source).read_text());(out/'roots.json').write_text(json.dumps(rr));(out/'method.json').write_text(json.dumps(dict(target=target,all_controls=all_controls,eta=eta,epsilon=eps,gap_floor=gapfloor),indent=2))
 for it in range(steps):
  g=c.physical(q);cost,grad,info=c.loss(g,eta);v,J,cl=guards(c,g,rr);row=dict(it=it,S=cl[1],U=cl[0],loss=cost,Q=info['Qmax'],P=info['Pmax'],guard=float(v.min()),gap=float(g['noncontact'].min()),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%5==0:print('CONTACT_POLYNOMIAL',row,flush=True)
  if cl==[1,1]:np.save(out/'potential_q.npy',q);print('CONTACT_POLYNOMIAL_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
  assert cl[0]<=len(rr[0]) and cl[1]<=len(rr[1])
  W,R=basis(c,g)
  if all_controls:R=W
  d=R.shape[1];gap=g['noncontact'];JG=g['Dgap'][~c.incidence]@R;bound=trust/np.sqrt(d);rhs=gap-gapfloor;keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;sol=linprog(grad@R,A_ub=-JG[keep],b_ub=rhs[keep],bounds=[(-bound,bound)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.5;continue
  dq=R@sol.x;ok=False
  for k in range(15):
   trial=q+2.**-k*dq
   try:qq,good,corr=correct(c,trial,W,rr,eps,gapfloor)
   except (ValueError,np.linalg.LinAlgError):continue
   if not good:continue
   gg=c.physical(qq);new,_,ii=c.loss(gg,eta)
   if new<cost-max(1e-12,abs(cost)*1e-8):q=qq;ok=True;row.update(alpha=2.**-k,corrections=corr);break
  if ok and k==0:trust=min(.3,trust*1.25)
  if not ok:trust*=.4
  if trust<1e-8:break
 print('CONTACT_POLYNOMIAL_DONE',hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=700);p.add_argument('--eta',type=float,default=.03);p.add_argument('--epsilon',type=float,default=1e-7);p.add_argument('--gap-floor',type=float,default=1e-8);p.add_argument('--target',choices=['211','121'],default='211');p.add_argument('--all-controls',action='store_true');a=p.parse_args();run(a.input,a.out,a.steps,a.eta,a.epsilon,a.gap_floor,a.target,a.all_controls)
