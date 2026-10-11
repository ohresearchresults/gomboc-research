"""Actual uniform-mass strict equilibrium repair in a full physical contact chart."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.linalg import svd
from contact_numpy import Chart
from section_polish import roots
from support_geometry import escape
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def guards(c,g,S,U):
 vals=[];JJ=[];counts=[]
 for A,DA,ed,count in [(g['Z'],g['DZ'],c.pe,U),(g['H'],g['DH'],c.qe,S)]:
  rr=roots(A,ed,count);v,j,J=escape(A,DA,angular=True);keep=np.ones(len(A),bool);keep[rr]=False;vals.append(v[keep]);JJ.append(J[keep]);counts.append(int(np.sum(v<0)))
 return np.r_[tuple(vals)],np.vstack(JJ),counts

def metric(c,g):
 sx=np.sqrt(np.mean(g['X']**2));sy=np.sqrt(np.mean(g['Y']**2));M=np.vstack((g['DX'].reshape(-1,c.d)/sx,g['DY'].reshape(-1,c.d)/sy,.01*np.eye(c.d)));_,s,V=svd(M,full_matrices=False,check_finite=False);return V.T/s

def run(source,out,S,U,steps,eps):
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=c.q0.copy();(out/'source_construction.json').write_text(Path(source).read_text());hist=[];start=time.time();trust=.03
 for it in range(steps):
  g=c.physical(q);v,J,cl=guards(c,g,S,U);merit=float(np.maximum(eps-v,0).sum());cost,grad,inf=c.loss(g,.01);row=dict(it=it,S=cl[1],U=cl[0],merit=merit,minimum=float(min(v)),P=inf['Pmax'],Q=inf['Qmax'],min_gap=float(min(g['noncontact'])),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('CONTACT_QUOTA',out,row,flush=True)
  if min(v)>eps*.85 and cl[0]<=U and cl[1]<=S:
   np.save(out/'success_q.npy',q);(out/'success.json').write_text(json.dumps(row,indent=2));print('CONTACT_QUOTA_NOMINATION_REQUIRES_EXACT',out,row,flush=True);return
  W=metric(c,g);d=c.d;m=len(v);JW=J@W;gap=g['noncontact'];JG=g['Dgap'][~c.incidence]@W;target=np.minimum(1e-9,gap*.5);rhs=gap-target;bound=trust/np.sqrt(d);keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;JG=JG[keep];rhs=rhs[keep];n=len(rhs);I=eye(d);O=csr_matrix((d,m));sc=.001
  A=vstack([hstack([-csr_matrix(JW/sc),-eye(m),csr_matrix((m,d))]),hstack([-csr_matrix(JG/sc),csr_matrix((n,m+d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/sc,rhs/sc,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=OPT)
  if not sol.success:
   row['error']=sol.message;trust*=.4
   if trust<1e-10:break
   continue
  dq=W@sol.x[:d];ok=False
  for k in range(16):
   try:qq=q+2.**-k*dq;gg=c.physical(qq);vv,_,cc=guards(c,gg,S,U)
   except (ValueError,np.linalg.LinAlgError):continue
   mm=float(np.maximum(eps-vv,0).sum())
   if mm<merit-max(1e-13,merit*1e-7):
    q=qq;ok=True;row['alpha']=2.**-k
    if k==0:trust=min(.2,trust*1.3)
    elif k>=5:trust=max(1e-8,trust*.6)
    break
  if not ok:trust*=.4
  if trust<1e-10:break
 print('CONTACT_QUOTA_NONWINNER',out,hist[-1],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('construction');p.add_argument('out');p.add_argument('--S',type=int,choices=[1,2],default=1);p.add_argument('--U',type=int,choices=[1,2],default=1);p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-7);a=p.parse_args();run(a.construction,a.out,a.S,a.U,a.steps,a.epsilon)
