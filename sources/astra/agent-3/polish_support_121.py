"""Strict own-centroid1S/2U physical halfspace retraction; exact audit required."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from support_geometry import geometry,escape,census
from polish_121 import forest
from persistence_birth import bars_loss
OPTIONS={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def feature(g):
 A=g['Z'];aa=np.sum(A*A,axis=1);ed=np.array(sorted({tuple(sorted((i,j))) for f in g['faces'] for i,j in zip(f,f[1:]+f[:1])}));i,j=ed.T;e=A[j]-A[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(A[i]*e,axis=1)/np.where(ee>0,ee,1),0,1);dd=np.sum((A[i]+t[:,None]*e)**2,axis=1);par=np.arange(len(A));best=(-1,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(dd)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;dep=1-dd[k]/aa[u]
  if dep>best[0]:best=(dep,int(u))
 return [int(aa.argmax()),best[1]],best[0]

def guards(g,derivative=True):
 rr,val=feature(g);out=[];JJ=[]
 for A,DA,rs in [(g['Z'],g.get('DZ'),rr),(g['H'],g.get('DH'),[int(np.argmax(np.sum(g['H']**2,axis=1)))])]:
  pp=forest(A,rs);sign=np.ones(len(A));sign[rs]=-1
  if derivative:v,_,J=escape(A,DA,True,pp);JJ.append(J*sign[:,None])
  else:v,_=escape(A,angular=True,chosen=pp)
  out.append(sign*v)
 return np.r_[tuple(out)],np.vstack(JJ) if derivative else None,val

def run(path,out,steps,eps):
 Q=np.load(path);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',Q);trust=.002;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(Q);v,J,val=guards(g);merit=float(np.maximum(eps-v,0).sum());cl=census(g);row=dict(it=it,minimum=float(v.min()),merit=merit,U=cl['U'],S=cl['S'],relative_basin=float(val),C=2*cl['E'],trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',Q);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('SUPPORT_POLISH121',row,flush=True)
  if min(v)>eps*.85:
   np.save(out/'success.npy',Q);(out/'success.json').write_text(json.dumps(row,indent=2));print('NUMERICAL_SUPPORT_STRICT121_REQUIRES_EXACT',row,flush=True);return
  d=Q.size;m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(Q.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   xx=Q+alpha*dx;vv,_,_=guards(geometry(xx,False),False);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-6):Q=xx;accepted=True;row['alpha']=alpha;break
  if accepted and alpha==1:trust=min(.03,trust*1.3)
  if not accepted:trust*=.4
  if trust<1e-11:break
 print('SUPPORT_POLISH121_INCOMPLETE',hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon)
