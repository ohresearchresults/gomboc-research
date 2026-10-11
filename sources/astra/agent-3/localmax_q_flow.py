"""Own-mass Q descent with refreshed local-maximum witnesses and full retraction.
Root exclusions are not forced to stay equilibria: actual110 is nominated as
soon as it occurs. Redundant linear rows are removed only by a trust-box bound.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape
from projected_q_flow import feature
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def guards(g,derivative=True):
 value,_,sroots=feature(g,False);vs=[];Js=[];cl=[]
 for A,DA,roots in [(g['Z'],g.get('DZ'),[int(np.argmax(np.sum(g['Z']**2,axis=1)))]),(g['H'],g.get('DH'),sroots)]:
  v,j=escape(A,angular=True);mask=np.ones(len(A),bool);mask[roots]=False;vs.append(v[mask]);cl.append(int(np.sum(v<0)))
  if derivative:_,_,J=escape(A,DA,angular=True,chosen=j);Js.append(J[mask])
 return np.r_[tuple(vs)],np.vstack(Js) if derivative else None,cl
def retract(X,eps):
 for it in range(12):
  g=geometry(X);v,J,cl=guards(g);merit=np.maximum(eps-v,0).sum()
  if v.min()>eps*.9 and cl[0]==1 and cl[1]<=2:return X,True,it
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));sc=.001;A=vstack([hstack([-csr_matrix(J/sc),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/sc,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-.01,.01)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:return X,False,it
  dx=sol.x[:d].reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   xx=X+alpha*dx;vv,_,cc=guards(geometry(xx,False),False);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-5):X=xx;ok=True;break
  if not ok:return X,False,it
 return X,False,12
def run(source,out,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);trust=.003;hist=[];start=time.time();np.save(out/'initial.npy',X)
 for it in range(steps):
  g=geometry(X);value,grad,_=feature(g);v,J,cl=guards(g);row=dict(it=it,Q=value,S=cl[1],U=cl[0],min_guard=float(v.min()),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('LOCALMAX_Q_FLOW',out,row,flush=True)
  if cl==[1,1]:np.save(out/'potential.npy',X);print('LOCALMAX_Q_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
  slack=1-g['H']@g['Z'].T;mask=np.ones(slack.shape,bool)
  for f,t in enumerate(g['T']):mask[f,t]=False
  DS=-(np.einsum('fkp,vk->fvp',g['DH'],g['Z'])+np.einsum('fk,vkp->fvp',g['H'],g['DZ']));sv=slack[mask];SJ=DS[mask];vv=np.r_[v,sv];JJ=np.vstack((J,SJ));target=np.r_[np.minimum(eps,v*.98),np.minimum(1e-9,sv*.95)];rhs=vv-target;keep=rhs<=trust*np.sum(abs(JJ),axis=1)+1e-10;JJ=JJ[keep];rhs=rhs[keep];row['linear_rows']=len(rhs);d=X.size;I=eye(d);sc=.001;A=vstack([hstack([-csr_matrix(JJ/sc),csr_matrix((len(rhs),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[rhs/sc,np.zeros(2*d)];obj=np.r_[grad,np.full(d,1e-8)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   xx=X+alpha*dx;gg=geometry(xx,False);_,_,cc=guards(gg,False)
   if cc==[1,1]:np.save(out/'potential.npy',xx);print('LOCALMAX_Q_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
   xx,success,corr=retract(xx,eps)
   if not success:continue
   val,_,_=feature(geometry(xx,False),False)
   if val<value-max(1e-12,abs(value)*1e-7):
    X=xx;ok=True;row.update(alpha=alpha,corrections=corr)
    if alpha==1:trust=min(.03,trust*1.25)
    break
  if not ok:trust*=.4
  if trust<1e-10:break
 print('LOCALMAX_Q_DONE',hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=1600);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon)
