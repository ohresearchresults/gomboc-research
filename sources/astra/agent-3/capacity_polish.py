"""Continuous widest-path capacity merit for complete own-mass equilibrium repair.
Peer1 identified a discontinuity of direct selected-tree edge sums. Here each
node contributes its actual max-path/min-edge capacity, with active witnesses.
Full exact physical auditing is still required for a numerical nomination.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape
from polish_211 import polar_roots
from polish_121 import persistent_root
from persistence_birth import evaluate
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def capacities(A,DA,roots):
 n=len(A);e=A[None]-A[:,None];aa=np.sum(A*A,axis=1);ee=np.sum(e*e,axis=2);W=np.einsum('ic,ijc->ij',A,e)/np.sqrt(np.maximum(aa[:,None]*ee,1e-60));np.fill_diagonal(W,-np.inf);cap=np.full(n,-np.inf);cap[roots]=np.inf;done=np.zeros(n,bool);ii=np.full(n,-1,int);jj=ii.copy()
 for _ in range(n):
  j=int(np.argmax(np.where(done,-np.inf,cap)));done[j]=True;candidate=np.minimum(cap[j],W[:,j]);take=(candidate>cap)&(~done)
  for i in np.flatnonzero(take):
   cap[i]=candidate[i]
   if W[i,j]<=cap[j]:ii[i]=i;jj[i]=j
   else:ii[i]=ii[j];jj[i]=jj[j]
 signs=np.ones(n)
 for r in roots:ii[r]=r;jj[r]=int(W[r].argmax());cap[r]=-W[r,jj[r]];signs[r]=-1
 assert np.all(ii>=0) and np.all(jj>=0)
 if DA is None:return cap,None
 u=A[ii];v=A[jj];du=DA[ii];dv=DA[jj];e=v-u;de=dv-du;uu=np.sum(u*u,axis=1);ee=np.sum(e*e,axis=1);dote=np.einsum('ic,icp->ip',e,du)+np.einsum('ic,icp->ip',u,de);c=W[ii,jj];J=dote/np.sqrt(uu*ee)[:,None]-c[:,None]*(np.einsum('ic,icp->ip',u,du)/uu[:,None]+np.einsum('ic,icp->ip',e,de)/ee[:,None]);return cap,J*signs[:,None]

def guards(g,S,U,derivative=True):
 pr=persistent_root(g) if U==2 else [int(np.argmax(np.sum(g['Z']**2,axis=1)))];qr=polar_roots(g) if S==2 else [int(np.argmax(np.sum(g['H']**2,axis=1)))];H=g['H'];idx=np.sort(np.unique(H,axis=0,return_index=True)[1]);qr=[int(np.flatnonzero(np.all(H[idx]==H[r],axis=1))[0]) for r in qr];v,J=capacities(g['Z'],g['DZ'] if derivative else None,pr);w,K=capacities(H[idx],g['DH'][idx] if derivative else None,qr);cl=[int(np.sum(escape(g['Z'])[0]<0)),int(np.sum(escape(H[idx])[0]<0))];return np.r_[v,w],np.vstack((J,K)) if derivative else None,cl

def run(source,out,S,U,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);trust=.002;history=[];start=time.time();np.save(out/'initial.npy',X)
 for it in range(steps):
  g=geometry(X);v,J,cl=guards(g,S,U);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,minimum=float(v.min()),merit=merit,S=cl[1],U=cl[0],trust=trust,seconds=time.time()-start);history.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(history,indent=2))
  if it%10==0:print('CAPACITY_POLISH',out,row,flush=True)
  if cl==[1,1]:
   from goal_nomination import preserve
   preserve(X,out/f'goal_nomination_it{it}','actual own110 before capacity-margin target reached')
  if min(v)>eps*.9:
   np.save(out/'success.npy',X);row['persistence']=evaluate(X)[2];(out/'success.json').write_text(json.dumps(row,indent=2));print('CAPACITY_STRICT_NOMINATION_REQUIRES_EXACT',row,flush=True);return
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.4;continue
  dx=sol.x[:d].reshape(X.shape);ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625]:
   xx=X+alpha*dx;vv,_,cc=guards(geometry(xx,False),S,U,False);mm=np.maximum(eps-vv,0).sum()
   if cc==[1,1]:
    from goal_nomination import preserve
    preserve(xx,out/f'goal_nomination_it{it}_alpha{alpha:g}','actual own110 trial in full physical capacity repair')
   if np.isfinite(mm) and mm<merit*(1-1e-6):X=xx;ok=True;row['alpha']=alpha;break
  if ok and alpha==1:trust=min(.03,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-11:break
 print('CAPACITY_POLISH_NONWINNER',out,history[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--S',type=int,choices=[1,2],default=1);p.add_argument('--U',type=int,choices=[1,2],default=1);p.add_argument('--steps',type=int,default=600);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(a.input,a.out,a.S,a.U,a.steps,a.epsilon)
