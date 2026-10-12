"""Complete own-mass vertex retraction to strict2S/1U numerical nomination.
The two polar roots are re-identified by full edge-graph persistence.
No tiny positive bar is interpreted as zero or as a Figure.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape
from polish_121 import forest
from persistence_birth import evaluate
OPTIONS={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def polar_roots(g):
 A=g['H'];aa=np.einsum('ic,ic->i',A,A);T=g['T'];owners={}
 for f,tri in enumerate(T):
  for a,b in zip(tri,np.roll(tri,-1)):owners.setdefault(tuple(sorted((a,b))),[]).append(f)
 edges=np.array(list(owners.values()));i,j=edges.T;e=A[j]-A[i];ee=np.einsum('ic,ic->i',e,e);t=np.clip(-np.einsum('ic,ic->i',A[i],e)/np.where(ee>0,ee,1),0,1);death=np.einsum('ic,ic->i',A[i]+t[:,None]*e,A[i]+t[:,None]*e);par=np.arange(len(A));best=(-1,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;depth=1-death[k]/aa[u]
  if depth>best[0]:best=(depth,int(u))
 return [int(aa.argmax()),best[1]]

def guards(g,derivative=True):
 rr=polar_roots(g);H=g['H'];idx=np.unique(H,axis=0,return_index=True)[1];idx=np.sort(idx);mapping={int(j):int(i) for i,j in enumerate(idx)}
 # A root is represented by its exact-equal nominated plane when duplicates occur.
 roots=[int(np.flatnonzero(np.all(H[idx]==H[r],axis=1))[0]) for r in rr]
 assert len(set(roots))==2
 out=[];JJ=[];classes=[]
 for A,DA,rs in [(g['Z'],g.get('DZ'),[int(np.argmax(np.sum(g['Z']**2,axis=1)))]),(H[idx],g['DH'][idx] if derivative else None,roots)]:
  pp=forest(A,rs);sign=np.ones(len(A));sign[rs]=-1
  if derivative:v,_,J=escape(A,DA,True,pp);JJ.append(sign[:,None]*J)
  else:v,_=escape(A,angular=True,chosen=pp)
  out.append(sign*v);classes.append(int(np.sum(escape(A)[0]<0)))
 return np.r_[tuple(out)],np.vstack(JJ) if derivative else None,classes

def run(path,out,steps,eps):
 X=np.load(path);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);trust=.002;hist=[];start=time.time()
 for it in range(steps):
  g=geometry(X);v,J,cl=guards(g);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,minimum=float(v.min()),merit=merit,U=cl[0],S=cl[1],trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('POLISH211',row,flush=True)
  if cl==[1,1]:
   from goal_nomination import preserve
   preserve(X,out/f'goal_nomination_it{it}','actual S1U1 before211quota repair')
  if min(v)>eps*.85:
   np.save(out/'success.npy',X);row.update(persistence=evaluate(X)[2]);(out/'success.json').write_text(json.dumps(row,indent=2));print('NUMERICAL_STRICT211_REQUIRES_EXACT',row,flush=True);return
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,options=OPTIONS,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   xx=X+alpha*dx;vv,_,cc=guards(geometry(xx,False),False);mm=np.maximum(eps-vv,0).sum()
   if cc==[1,1]:
    from goal_nomination import preserve
    preserve(xx,out/f'goal_nomination_it{it}_alpha{alpha:g}','actual S1U1 in211retraction line search')
   if np.isfinite(mm) and mm<merit*(1-1e-6):X=xx;accepted=True;row['alpha']=alpha;break
  if accepted and alpha==1:trust=min(.03,trust*1.3)
  if not accepted:trust*=.4
  if trust<1e-11:break
 print('POLISH211_INCOMPLETE',hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.out,a.steps,a.epsilon)
