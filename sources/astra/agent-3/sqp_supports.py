"""Physical support deformation with acyclic escape witnesses and live hull.
Each step uses full uniform mass derivatives; exact certification remains separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from scipy.sparse.csgraph import dijkstra
from support_geometry import geometry,escape,census

def policy(A,eps=1e-8):
 aa=np.sum(A*A,axis=1);q=A@A.T/aa[:,None]-1;np.fill_diagonal(q,-1e30);root=int(np.argmax(aa))
 cost=np.maximum(eps-q,0)+1e-12;np.fill_diagonal(cost,0)
 dist,prev=dijkstra(csr_matrix(cost.T),indices=root,return_predecessors=True)
 prev[root]=(root+1)%len(A)
 assert np.all(prev>=0)
 return root,prev

def guards(g,derivatives=True,mode='tree',eps=1e-8):
 vals=[];jacs=[]
 for name,dname in [('Z','DZ'),('H','DH')]:
  A=g[name];root,p=policy(A,eps)
  if mode=='max':p=None
  if derivatives:v,j,J=escape(A,g[dname],chosen=p)
  else:v,j=escape(A,chosen=p)
  keep=np.arange(len(A))!=root;vals.append(v[keep])
  if derivatives:jacs.append(J[keep])
 return np.concatenate(vals),np.vstack(jacs) if derivatives else None

def run(path,out,steps,eps,mode):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);Q=np.load(path);np.save(out/'initial.npy',Q);trust=.003;start=time.time();hist=[];best=1e30
 for it in range(steps):
  g=geometry(Q);v,J=guards(g,True,mode,eps);res=np.maximum(eps-v,0);merit=np.sum(res);mx=res.max();ci=census(g)
  row=dict(it=it,merit=float(merit),maximum=float(mx),trust=trust,elapsed=time.time()-start,**ci);hist.append(row)
  print('SQP',mode,row,flush=True);(out/'history.json').write_text(json.dumps(hist,indent=2)+'\n')
  np.save(out/'latest.npy',Q)
  if merit<best:
   best=merit;np.save(out/'best.npy',Q);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
  if ci['S']==ci['U']==1 and min(ci['minV'],ci['minF'])>1e-10:
   np.save(out/'potential.npy',Q);(out/'potential.json').write_text(json.dumps(row,indent=2));print('POTENTIAL_110',out,flush=True)
   if min(ci['minV'],ci['minF'])>eps*.8:break
  d=Q.size;m=len(v);I=eye(d,format='csr');O=csr_matrix((d,m));Oma=csr_matrix((m,d))
  A=vstack([hstack([-csr_matrix(J),-eye(m),Oma]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr')
  b=np.r_[v-eps,np.zeros(2*d)];c=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)]
  sol=linprog(c,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,method='highs')
  if not sol.success:
   row['lp_failure']=sol.message;trust*=.5
   if trust<1e-10:break
   continue
  dq=sol.x[:d].reshape(Q.shape);accepted=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625]:
   qq=Q+alpha*dq
   try:
    gg=geometry(qq,False);vv,_=guards(gg,False,mode,eps);mm=np.maximum(eps-vv,0).sum()
   except (ValueError,np.linalg.LinAlgError):continue
   if mm<merit*(1-1e-5):
    Q=qq;accepted=True;row['alpha']=alpha
    if alpha>.99:trust=min(trust*1.2,.03)
    break
  if not accepted:trust*=.35
  if trust<1e-10:break
 print('DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=200);p.add_argument('--epsilon',type=float,default=1e-8);p.add_argument('--mode',default='tree');a=p.parse_args();run(a.input,a.output,a.steps,a.epsilon,a.mode)
