"""Strict physical equilibrium-forest retraction within a convex section family.
Supports target110 as well as preparing nonwinning121/211 bodies. Actual
homogeneous centroid and every selected escape derivative are recomputed.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from triangular_sections import Family
from side_curvature_sections import SideFamily
from rectangular_sections import RectFamily
from polish_121 import forest
from support_geometry import escape
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def roots(A,edges,count):
 aa=np.sum(A*A,axis=1);r=[int(aa.argmax())]
 if count==1:return r
 i,j=edges.T;e=A[j]-A[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(A[i]*e,axis=1)/ee,0,1);dd=np.sum((A[i]+t[:,None]*e)**2,axis=1);par=np.arange(len(A));best=(-1,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(dd)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;depth=1-dd[k]/aa[u]
  if depth>best[0]:best=(depth,int(u))
 return r+[best[1]]

def guards(f,q,S,U):
 g=f.physical(q);vs=[];Js=[];counts=[]
 for A,DA,edges,count in [(g['Z'],g['DZ'],f.pe,U),(g['H'],g['DH'],f.qe,S)]:
  rr=roots(A,edges,count);pp=forest(A,rr);sg=np.ones(len(A));sg[rr]=-1;v,_,J=escape(A,DA,angular=True,chosen=pp);vs.append(v*sg);Js.append(J*sg[:,None]);counts.append(int(np.sum(escape(A)[0]<0)))
 return np.r_[tuple(vs)],np.vstack(Js),counts,g

def run(f,source,out,S,U,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(source);np.save(out/'initial_params.npy',q);trust=.03;hist=[];start=time.time()
 for it in range(steps):
  v,J,counts,g=guards(f,q,S,U);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,S=counts[1],U=counts[0],minimum=float(v.min()),merit=merit,trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_params.npy',q);np.savez(out/'latest_construction.npz',**g['construction']);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('SECTION_POLISH',out,row,flush=True)
  if v.min()>eps*.9:
   np.save(out/'success_params.npy',q);np.savez(out/'success_construction.npz',**g['construction']);row['persistence']=f.evaluate(q,.01)[2];(out/'success.json').write_text(json.dumps(row,indent=2));print('SECTION_STRICT_NOMINATION_REQUIRES_EXACT',row,flush=True);return
  d=len(q);m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.5;continue
  dq=sol.x[:d];ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   qq=q+alpha*dq;vv,_,cc,gg=guards(f,qq,S,U);mm=np.maximum(eps-vv,0).sum()
   if mm<merit*(1-1e-6):q=qq;ok=True;row['alpha']=alpha;break
  if ok and alpha==1:trust=min(.3,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-10:break
 print('SECTION_POLISH_NONWINNER',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('family',choices=['tri','side','rect']);p.add_argument('input');p.add_argument('out');p.add_argument('--layers',type=int,required=True);p.add_argument('--S',type=int,choices=[1,2],default=1);p.add_argument('--U',type=int,choices=[1,2],default=1);p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();f={'tri':Family,'side':SideFamily,'rect':RectFamily}[a.family](a.layers);run(f,a.input,a.out,a.S,a.U,a.steps,a.epsilon)
