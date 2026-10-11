"""Physical free-halfspace quota repair allowing the unwanted root to disappear."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from support_geometry import geometry,escape
from section_polish import roots
from free_support_persistence import evaluate
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def guards(g,S,U,derivative=True):
 owners={}
 for f,cy in enumerate(g['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 pe=np.array(list(owners));qe=np.array(list(owners.values()));values=[];rows=[];counts=[]
 for A,DA,edges,count in [(g['Z'],g.get('DZ'),pe,U),(g['H'],g.get('DH'),qe,S)]:
  rr=roots(A,edges,count);mask=np.ones(len(A),bool);mask[rr]=False;v,j=escape(A,angular=True);values.append(v[mask]);counts.append(int(np.sum(v<0)))
  if derivative:rows.append(escape(A,DA,angular=True,chosen=j)[2][mask])
 return np.r_[tuple(values)],np.vstack(rows)if derivative else None,counts

def run(source,out,S,U,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(source);assert len(Q)<=84;np.save(out/'initial_Q.npy',Q);trust=.02;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(Q);v,J,cl=guards(g,S,U);merit=float(np.maximum(eps-v,0).sum());info=evaluate(Q,.01)[2];row=dict(it=it,merit=merit,minimum=float(min(v)),S=cl[1],U=cl[0],P=info['Pmax'],Q=info['Qmax'],V=g['nv'],E=g['ne'],F=g['nf'],trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_Q.npy',Q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('SUPPORT_QUOTA',out,row,flush=True)
  if min(v)>eps*.9 and cl[0]<=U and cl[1]<=S:
   np.save(out/'success_Q.npy',Q);(out/'success.json').write_text(json.dumps(row,indent=2));print('SUPPORT_QUOTA_NOMINATION_REQUIRES_EXACT',out,row,flush=True);return
  d=Q.size;sx=np.sqrt(np.mean(g['Z']**2));sq=np.sqrt(np.mean(Q**2));M=np.vstack((g['DX'].reshape(-1,d)/sx,np.eye(d)/sq));_,s,V=svd(M,full_matrices=False,check_finite=False);W=V.T/s;m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J@W/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];bound=trust/np.sqrt(d);sol=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=OPT)
  if not sol.success:
   row['error']=sol.message;trust*=.4
   if trust<1e-10:break
   continue
  dq=(W@sol.x[:d]).reshape(Q.shape);ok=False
  for k in range(14):
   Y=Q+2.**-k*dq
   try:gg=geometry(Y,False);vv,_,cc=guards(gg,S,U,False)
   except (ValueError,np.linalg.LinAlgError):continue
   mm=float(np.maximum(eps-vv,0).sum())
   if cc==[1,1] and min(vv)>0:
    np.save(out/'potential110_Q.npy',Y);print('SUPPORT_QUOTA_POTENTIAL110_REQUIRES_EXACT',out,flush=True)
   if mm<merit-max(1e-13,merit*1e-7):Q=Y;ok=True;row['alpha']=2.**-k;break
  if ok and k==0:trust=min(.2,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-10:break
 print('SUPPORT_QUOTA_NONWINNER',out,hist[-1],flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--S',type=int,choices=[1,2],default=2);p.add_argument('--U',type=int,choices=[1,2],default=1);p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-7);a=p.parse_args();run(a.input,a.out,a.S,a.U,a.steps,a.epsilon)
