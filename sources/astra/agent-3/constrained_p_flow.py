"""Decrease the surviving actual radial basin while retaining strict other exclusions.
Objective is 1-r_saddle²/r_birth², so elongating the unrelated elder cannot improve it.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,argparse,time
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from support_geometry import escape
from polish_121 import forest

def feature(g,derivative=True):
 X=g['Z'];aa=np.sum(X*X,axis=1);T=g['T'];edges=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0);i,j=edges.T;e=X[j]-X[i];ee=np.sum(e*e,axis=1);t=np.clip(-np.sum(X[i]*e,axis=1)/ee,0,1);foot=X[i]+t[:,None]*e;death=np.sum(foot*foot,axis=1);par=np.arange(len(X));best=(-1,None,None)
 def find(k):
  while par[k]!=k:par[k]=par[par[k]];k=par[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(i[k]),find(j[k])
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  par[u]=v;depth=1-death[k]/aa[u]
  if depth>best[0]:best=(depth,int(u),int(k))
 value,u,k=best;grad=None
 if derivative:
  DZ=g['DZ'];grad=2*death[k]/aa[u]**2*(X[u]@DZ[u])-2/aa[u]*(foot[k]@((1-t[k])*DZ[i[k]]+t[k]*DZ[j[k]]))
 return float(value),grad,[int(aa.argmax()),u],edges[k].tolist()

def guards(g,roots,derivative=True):
 vals=[];jacs=[];classes=[]
 _,idx=np.unique(g['H'],axis=0,return_index=True);idx=np.sort(idx);H=g['H'][idx];DH=g['DH'][idx] if derivative else None
 for k,(A,DA,rr) in enumerate([(g['Z'],g.get('DZ'),roots),(H,DH,[int(np.argmax(np.sum(H*H,axis=1)))])]):
  pp=forest(A,rr);signs=np.ones(len(A));signs[rr[0]]=-1;mask=np.ones(len(A),bool)
  if k==0:mask[rr[1]]=False
  if derivative:v,j,J=escape(A,DA,angular=True,chosen=pp);jacs.append((J*signs[:,None])[mask])
  else:v,j=escape(A,angular=True,chosen=pp)
  vals.append((v*signs)[mask]);vv,jj=escape(A);classes.append(int(np.sum(vv<0)))
 return np.concatenate(vals),np.vstack(jacs) if derivative else None,classes

def run(path,out,steps,eps):
 X=np.load(path);out=Path(out);out.mkdir(exist_ok=False,parents=True);np.save(out/'initial.npy',X);trust=.001;hist=[];t0=time.time()
 for it in range(steps):
  g=geometry(X);value,grad,roots,edge=feature(g);v,J,classes=guards(g,roots);row=dict(it=it,relative_basin=value,roots=roots,edge=edge,S=classes[1],U=classes[0],min_guard=float(v.min()),trust=trust,elapsed=time.time()-t0);hist.append(row)
  (out/'history.json').write_text(json.dumps(hist,indent=2));np.save(out/'latest.npy',X)
  if it%10==0:print('P_FLOW',row,flush=True)
  if classes==[1,1]:np.save(out/'potential.npy',X);print('POTENTIAL_110',out,flush=True);break
  target=np.minimum(eps,v*.95);d=X.size;I=eye(d);A=vstack([hstack([-csr_matrix(J),csr_matrix((len(v),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[v-target,np.zeros(2*d)];obj=np.r_[grad,np.full(d,1e-7)]
  sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,method='highs')
  if not sol.success:row['error']=sol.message;trust*=.5;continue
  dx=sol.x[:d].reshape(X.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125,.0009765625]:
   xx=X+alpha*dx;gg=geometry(xx,False);value2,_,roots2,edge2=feature(gg,False);vv,_,cc=guards(gg,roots2,False)
   if cc[1]==1 and cc[0]<=2 and vv.min()>eps*.1 and value2<value-max(1e-12,abs(value)*1e-7):
    X=xx;accepted=True;row['alpha']=alpha
    if alpha==1:trust=min(trust*1.2,.02)
    break
  if not accepted:trust*=.4
  if trust<1e-10:break
 print('P_FLOW_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=1000);p.add_argument('--epsilon',type=float,default=1e-7);a=p.parse_args();run(a.input,a.output,a.steps,a.epsilon)
