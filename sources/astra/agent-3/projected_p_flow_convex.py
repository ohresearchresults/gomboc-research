"""Finite persistence descent followed by actual-mass strict retraction.
Uses well-scaled LP constraints and explicit small feasibility tolerances.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from constrained_p_flow import feature
from support_geometry import escape
from polish_121 import guards as quota_guards
OPTIONS={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}


def flowguards(g,roots,derivative=True):
 vals=[];jacs=[];classes=[]
 _,idx=np.unique(g['H'],axis=0,return_index=True);idx=np.sort(idx);H=g['H'][idx];DH=g['DH'][idx] if derivative else None
 for k,(A,DA,rr) in enumerate([(g['Z'],g.get('DZ'),roots),(H,DH,[int(np.argmax(np.sum(H*H,axis=1)))])]):
  signs=np.ones(len(A));signs[rr[0]]=-1;mask=np.ones(len(A),bool)
  if k==0:mask[rr[1]]=False
  if derivative:v,j,J=escape(A,DA,angular=True);jacs.append((J*signs[:,None])[mask])
  else:v,j=escape(A,angular=True)
  vals.append((v*signs)[mask]);vv,jj=escape(A);classes.append(int(np.sum(vv<0)))
 return np.concatenate(vals),np.vstack(jacs) if derivative else None,classes

def retract(X,roots,eps,limit=12):
 for it in range(limit):
  g=geometry(X);v,J,cl=quota_guards(g,roots);merit=np.maximum(eps-v,0).sum()
  if v.min()>eps*.9:return X,True,it
  if not np.all(np.isfinite(J)):return X,False,it
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));s=.001
  A=vstack([hstack([-csr_matrix(J/s),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/s,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-.01,.01)]*d+[(0,None)]*m+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:return X,False,it
  dx=sol.x[:d].reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125]:
   xx=X+alpha*dx;vv,_,cc=quota_guards(geometry(xx,False),roots,False);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-5):X=xx;ok=True;break
  if not ok:return X,False,it
 return X,False,limit

def run(path,out,steps,eps):
 X=np.load(path);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);trust=.002;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(X);value,grad,roots,edge=feature(g);v,J,classes=flowguards(g,roots);row=dict(it=it,relative_basin=value,roots=roots,edge=edge,S=classes[1],U=classes[0],min_guard=float(v.min()),trust=trust,elapsed=time.time()-start);hist.append(row);print('PROJECTED_P',row,flush=True);(out/'history.json').write_text(json.dumps(hist,indent=2));np.save(out/'latest.npy',X)
  if classes==[1,1]:np.save(out/'potential.npy',X);print('POTENTIAL_110',out,flush=True);break
  target=np.minimum(eps,v*.98)
  slack=1-g['H']@g['Z'].T;mask=np.ones(slack.shape,bool)
  for f,tri in enumerate(g['T']):mask[f,tri]=False
  Dslack=-(np.einsum('fkp,vk->fvp',g['DH'],g['Z'])+np.einsum('fk,vkp->fvp',g['H'],g['DZ']))
  sv=slack[mask];SJ=Dslack[mask];st=np.minimum(sv*.95,1e-9)
  vv=np.r_[v,sv];JJ=np.vstack((J,SJ));tt=np.r_[target,st]
  d=X.size;I=eye(d);s=.001;A=vstack([hstack([-csr_matrix(JJ/s),csr_matrix((len(vv),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[(vv-tt)/s,np.zeros(2*d)];obj=np.r_[grad,np.full(d,1e-7)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   xx=X+alpha*dx;gg=geometry(xx,False);v0,_,r0,e0=feature(gg,False);vv,_,cc=flowguards(gg,r0,False)
   if cc==[1,1]:np.save(out/'potential.npy',xx);(out/'potential.json').write_text(json.dumps({'iteration':it,'alpha':alpha,'relative_basin':v0}));print('POTENTIAL_110',out,flush=True);return
   xx,ok,corr=retract(xx,r0,eps)
   if not ok:continue
   value2,_,roots2,edge2=feature(geometry(xx,False),False)
   if value2<value-max(1e-12,abs(value)*1e-7):
    X=xx;accepted=True;row.update(alpha=alpha,corrections=corr)
    if alpha==1:trust=min(trust*1.3,.03)
    break
  if not accepted:trust*=.4
  if trust<1e-10:break
 print('PROJECTED_P_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.output,a.steps,a.epsilon)
