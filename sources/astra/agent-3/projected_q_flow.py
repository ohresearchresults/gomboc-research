"""Actual-mass descent of remaining Q basin with strict1U/2S retraction."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape
from polish_121 import forest
from polish_211 import guards as quota_guards
OPTIONS={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def feature(g,derivative=True):
 A=g['H'];aa=np.sum(A*A,axis=1);owners={}
 for f,t in enumerate(g['T']):
  for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 ed=np.array(list(owners.values()));i,j=ed.T;e=A[j]-A[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(A[i]*e,axis=1)/np.where(ee>0,ee,1),0,1);foot=A[i]+t[:,None]*e;dd=np.sum(foot*foot,axis=1);par=np.arange(len(A));best=(-1,None,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(dd)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;dep=1-dd[k]/aa[u]
  if dep>best[0]:best=(dep,int(u),int(k))
 val,u,k=best;grad=None
 if derivative:grad=2*dd[k]/aa[u]**2*(A[u]@g['DH'][u])-2/aa[u]*(foot[k]@((1-t[k])*g['DH'][i[k]]+t[k]*g['DH'][j[k]]))
 return float(val),grad,[int(aa.argmax()),u]

def guards(g,roots,derivative=True):
 out=[];JJ=[];cl=[]
 for k,(A,DA,rs) in enumerate([(g['Z'],g.get('DZ'),[int(np.argmax(np.sum(g['Z']**2,axis=1)))]),(g['H'],g.get('DH'),roots)]):
  pp=forest(A,rs);sign=np.ones(len(A));sign[rs[0]]=-1;keep=np.ones(len(A),bool)
  if k==1:keep[rs[1]]=False
  if derivative:v,_,J=escape(A,DA,True,pp);JJ.append((sign[:,None]*J)[keep])
  else:v,_=escape(A,angular=True,chosen=pp)
  out.append((sign*v)[keep]);cl.append(int(np.sum(escape(A)[0]<0)))
 return np.r_[tuple(out)],np.vstack(JJ) if derivative else None,cl

def retract(X,eps):
 for it in range(12):
  g=geometry(X);v,J,cl=quota_guards(g);merit=np.maximum(eps-v,0).sum()
  if v.min()>eps*.9:return X,True,it
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));s=.001;A=vstack([hstack([-csr_matrix(J/s),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/s,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-.01,.01)]*d+[(0,None)]*m+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:return X,False,it
  dx=sol.x[:d].reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125]:
   xx=X+alpha*dx;vv,_,cc=quota_guards(geometry(xx,False),False);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-5):X=xx;ok=True;break
  if not ok:return X,False,it
 return X,False,12

def run(source,out,steps,eps):
 X=np.load(source);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);trust=.002;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(X);value,grad,roots=feature(g);v,J,cl=guards(g,roots);row=dict(it=it,relative_basin=value,S=cl[1],U=cl[0],min_guard=float(v.min()),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('Q_FLOW',row,flush=True)
  if cl==[1,1]:np.save(out/'potential.npy',X);print('POTENTIAL_Q_FLOW110',row,flush=True);return
  target=np.minimum(eps,v*.98);slack=1-g['H']@g['Z'].T;mask=slack<.03
  for f,t in enumerate(g['T']):mask[f,t]=False
  Ds=-(np.einsum('fkp,vk->fvp',g['DH'],g['Z'])+np.einsum('fk,vkp->fvp',g['H'],g['DZ']));sv=slack[mask];SJ=Ds[mask];st=np.minimum(sv*.95,1e-9);vv=np.r_[v,sv];JJ=np.vstack((J,SJ));tt=np.r_[target,st]
  d=X.size;I=eye(d);s=.001;A=vstack([hstack([-csr_matrix(JJ/s),csr_matrix((len(vv),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[(vv-tt)/s,np.zeros(2*d)];obj=np.r_[grad,np.full(d,1e-7)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   xx=X+alpha*dx;gg=geometry(xx,False);v0,_,r0=feature(gg,False);_,_,cc=guards(gg,r0,False)
   if cc==[1,1]:np.save(out/'potential.npy',xx);print('POTENTIAL_Q_FLOW110',row,flush=True);return
   xx,ok,corr=retract(xx,eps)
   if not ok:continue
   new,_,_=feature(geometry(xx,False),False)
   if new<value-max(1e-12,abs(value)*1e-7):
    X=xx;accepted=True;row.update(alpha=alpha,corrections=corr)
    if alpha==1:trust=min(trust*1.3,.03)
    break
  if not accepted:trust*=.4
  if trust<1e-10:break
 print('Q_FLOW_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon)
