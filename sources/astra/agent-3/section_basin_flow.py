"""Actual-mass basin continuation in genuine planar-quad section families."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from triangular_sections import Family
from side_curvature_sections import SideFamily
from rectangular_sections import RectFamily
from section_polish import guards as quota_guards,roots
from polish_121 import forest
from support_geometry import escape
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def feature(f,g,kind):
 A=g['Z'] if kind=='P' else g['H'];DA=g['DZ'] if kind=='P' else g['DH'];edges=f.pe if kind=='P' else f.qe;aa=np.sum(A*A,axis=1);i,j=edges.T;e=A[j]-A[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(A[i]*e,axis=1)/ee,0,1);foot=A[i]+t[:,None]*e;death=np.sum(foot*foot,axis=1);par=np.arange(len(A));best=(-1,None,None)
 def find(k):
  while k!=par[k]:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;val=1-death[k]/aa[u]
  if val>best[0]:best=(val,int(u),int(k))
 val,u,k=best;grad=2*death[k]/aa[u]**2*(A[u]@DA[u])-2/aa[u]*(foot[k]@((1-t[k])*DA[i[k]]+t[k]*DA[j[k]]));return val,grad,[int(aa.argmax()),u]

def guards(f,g,kind,rr):
 vals=[];jac=[];counts=[]
 for name,A,DA in [('P',g['Z'],g['DZ']),('Q',g['H'],g['DH'])]:
  rs=rr if name==kind else [int(np.argmax(np.sum(A*A,axis=1)))];pp=forest(A,rs);sign=np.ones(len(A));sign[rs[0]]=-1;mask=np.ones(len(A),bool)
  if name==kind:mask[rs[1]]=False
  v,_,J=escape(A,DA,angular=True,chosen=pp);vals.append((v*sign)[mask]);jac.append((J*sign[:,None])[mask]);counts.append(int(np.sum(escape(A)[0]<0)))
 return np.r_[tuple(vals)],np.vstack(jac),counts

def metric(f,g,cols):
 sx=np.sqrt(np.mean(g['X']**2));sh=np.sqrt(np.mean(g['H']**2));M=np.vstack((g['DX'][:,:,cols].reshape(-1,len(cols))/sx,g['DH'][:,:,cols].reshape(-1,len(cols))/sh));_,d,V=svd(M,full_matrices=False,check_finite=False)
 if min(d)<1e-13:raise ValueError('singular physical section metric after explicit gauge removal')
 return V.T/d

def retract(f,q,kind,eps,cols):
 S,U=(1,2) if kind=='P' else (2,1)
 for it in range(15):
  v,J,cl,g=quota_guards(f,q,S,U);merit=np.maximum(eps-v,0).sum()
  if min(v)>eps*.9:return q,True,it
  W=metric(f,g,cols);JJ=J[:,cols]@W;d=len(cols);m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(JJ/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I]),hstack([csr_matrix(W),csr_matrix((d,m+d))]),hstack([-csr_matrix(W),csr_matrix((d,m+d))])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d),np.full(2*d,.1)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-6)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-.02/np.sqrt(d),.02/np.sqrt(d))]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:return q,False,it
  dq=np.zeros(len(q));dq[cols]=W@sol.x[:d];ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125]:
   qq=q+alpha*dq;vv,_,_,_=quota_guards(f,qq,S,U);mm=np.maximum(eps-vv,0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-5):q=qq;ok=True;break
  if not ok:return q,False,it
 return q,False,15

def run(f,source,out,kind,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(source);cols=np.arange(len(q))
 # For rectangles A's diagonal scale is exactly redundant with the two pairs
 # of signed side curvatures and endpoint tilt; hold this gauge coordinate.
 if isinstance(f,RectFamily):cols=cols[cols!=len(q)-2]
 trust=.03;hist=[];start=time.time();np.save(out/'initial_params.npy',q)
 for it in range(steps):
  g=f.physical(q);value,grad,rr=feature(f,g,kind);v,J,cl=guards(f,g,kind,rr);row=dict(it=it,relative_basin=float(value),S=cl[1],U=cl[0],minimum=float(v.min()),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_params.npy',q);np.savez(out/'latest_construction.npz',**g['construction']);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('SECTION_BASIN',out,row,flush=True)
  if cl==[1,1]:np.savez(out/'potential_construction.npz',**g['construction']);print('SECTION_BASIN_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
  W=metric(f,g,cols);d=len(cols);JJ=J[:,cols]@W;I=eye(d);scale=.001;target=np.minimum(eps,v*.98);A=vstack([hstack([-csr_matrix(JJ/scale),csr_matrix((len(v),d))]),hstack([I,-I]),hstack([-I,-I]),hstack([csr_matrix(W),csr_matrix((d,d))]),hstack([-csr_matrix(W),csr_matrix((d,d))])],format='csr');b=np.r_[(v-target)/scale,np.zeros(2*d),np.full(2*d,.15)];obj=np.r_[grad[cols]@W,np.full(d,1e-8)];bound=trust/np.sqrt(d);sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.4;continue
  dq=np.zeros(len(q));dq[cols]=W@sol.x[:d];accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625]:
   qq=q+alpha*dq;gg=f.physical(qq);vv,_,rr0=feature(f,gg,kind);_,_,cc=guards(f,gg,kind,rr0)
   if cc==[1,1]:np.savez(out/'potential_construction.npz',**gg['construction']);np.save(out/'potential_params.npy',qq);print('SECTION_BASIN_POTENTIAL_REQUIRES_EXACT',row,flush=True);return
   qq,ok,corr=retract(f,qq,kind,eps,cols)
   if not ok:continue
   new,_,_=feature(f,f.physical(qq),kind)
   if new<value-max(1e-12,abs(value)*1e-7):
    q=qq;accepted=True;row.update(alpha=alpha,corrections=corr)
    if alpha==1:trust=min(.2,trust*1.25)
    break
  if not accepted:trust*=.4
  if trust<1e-9:break
 print('SECTION_BASIN_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('family',choices=['tri','side','rect']);p.add_argument('input');p.add_argument('out');p.add_argument('--layers',type=int,required=True);p.add_argument('--kind',choices=['P','Q'],required=True);p.add_argument('--steps',type=int,default=1200);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();f={'tri':Family,'side':SideFamily,'rect':RectFamily}[a.family](a.layers);run(f,a.input,a.out,a.kind,a.steps,a.epsilon)
