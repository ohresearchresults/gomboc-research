"""Actual-volume, live-hull, acyclic-escape nonlinear discovery.
No finite experiment is a certificate of exclusion or of an exact winner.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np,json,time,argparse
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack
from geometry import geom,brief,escape_grad

def widest(A,root,ids=None):
 n=len(A);ids=np.arange(n) if ids is None else np.array(ids);allowed=np.zeros(n,bool);allowed[ids]=1
 cap=np.full(n,-np.inf);cap[root]=np.inf;parent=np.full(n,-1,dtype=int);done=~allowed
 for _ in range(len(ids)):
  k=np.argmax(np.where(done,-np.inf,cap));
  if done[k]:raise ValueError('disconnected complete forest')
  done[k]=1
  # every unprocessed i may escape into k, which already reaches the root.
  val=np.minimum(A[:,k],cap[k]);better=(val>cap)&~done
  cap[better]=val[better];parent[better]=k
 return parent,cap

def rows(G,rootpole=3,override=None,derivatives=True):
 vr=G['source'].index(('root',));ui=np.array([i for i in range(G['V']) if i!=vr]);si=G['active'][G['active']!=rootpole]
 if rootpole not in G['faces']:raise ValueError('target facet disappeared')
 pu,cu=widest(G['A_U'],vr);ps,cs=widest(G['A_S'],rootpole,G['active'])
 if override:
  for i,j in override.items():
   if i in G['faces'] and j in G['faces']:ps[i]=j
 v=np.r_[G['A_U'][ui,pu[ui]],G['A_S'][si,ps[si]]]
 if derivatives:A=np.vstack((escape_grad(G['Y'],G['JY'],pu,ui),escape_grad(G['Z'],G['JZ'],ps,si)))
 else:A=None
 return v,A,pu,ps,ui,si

def optimize(q,out,steps=40,trust=.003,rho=2e-7,override=None):
 out=Path(out);out.mkdir(exist_ok=True,parents=True);history=[];best=np.inf;st=time.time();rootmask=q[:,2]==1.0
 for it in range(steps):
  G=geom(q,True);v,A,*rest=rows(G,override=override);neg=np.minimum(v-rho,0);score=float(np.sum(-neg));sq=float(neg@neg)
  if score<best:best=score;np.save(out/'best.npy',q)
  rep=brief(G);rep.update(iteration=it,forest_deficit=score,forest_min=float(v.min()),max_deficit=float(-neg.min()),trust=trust,elapsed=time.time()-st)
  history.append(rep);(out/'history.json').write_text(json.dumps(history,default=lambda x: x.item() if hasattr(x,'item') else x))
  print(it,rep['VEF'],rep['counts'],'deficit',score,'max',-neg.min(),'bar',[b['B'] for b in G['bars']],flush=True)
  if G['S'].tolist()==[3] and len(G['U'])==1 and G['source'][G['U'][0]]==('root',) and not G['H']:
   np.save(out/'NUMERICAL_110.npy',q);print('NUMERICAL_110',flush=True);return q
  dim=3*len(q);nr=len(v);bounds=[(-trust,trust)]*dim
  for i in np.flatnonzero(rootmask):bounds[3*i+2]=(0,0)
  for i in np.flatnonzero(~rootmask):bounds[3*i+2]=(-trust,min(trust,1-1e-8-q[i,2]))
  # L1 minimum slack. Mild positive-guard preference; root-path deficits receive
  # no arbitrary suppression. Iterative exact geometry replaces affine predictions.
  c=np.r_[np.zeros(dim),np.ones(nr)]
  sol=linprog(c,A_ub=hstack([-csr_matrix(A),-eye(nr,format='csr')],format='csr'),b_ub=v-rho,bounds=bounds+[(0,None)]*nr,method='highs-ipm',options={'presolve':True,'dual_feasibility_tolerance':1e-8,'primal_feasibility_tolerance':1e-8})
  if not sol.success:print('LP',sol.message,flush=True);break
  d=sol.x[:dim].reshape(q.shape);pred=float(np.sum(np.maximum(rho-v-A@d.ravel(),0)))
  found=False
  for k in range(13):
   fac=2.**(-k);z=q+fac*d;z[rootmask,2]=1.0
   try:
    H=geom(z);vv,*_=rows(H,override=override,derivatives=False);ss=np.maximum(rho-vv,0).sum()
   except (ValueError,AssertionError,np.linalg.LinAlgError):continue
   if ss<score-max(1e-12,1e-5*fac*(score-pred)):
    q=z;found=True;np.save(out/'last.npy',q)
    if k==0:trust=min(.015,trust*1.15)
    elif k>4:trust=max(1e-7,trust*.7)
    break
  if not found:
   trust*=.3
   if trust<1e-8:print('LINE_STOP',flush=True);break
 return q

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',default=str(Path(__file__).resolve().parent/'checkpoints'/'B023_START.npy'));p.add_argument('--out',required=True);p.add_argument('--steps',type=int,default=50);p.add_argument('--trust',type=float,default=.003);p.add_argument('--delete',type=int);p.add_argument('--rho',type=float,default=2e-7);a=p.parse_args()
 q=np.load(a.input)
 if a.delete is not None:q=np.delete(q,a.delete,axis=0)
 optimize(q,a.out,a.steps,a.trust,a.rho)
if __name__=='__main__':main()
