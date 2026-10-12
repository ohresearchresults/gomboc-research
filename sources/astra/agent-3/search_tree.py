"""Shortest-path-to-root physical escape loss; continuous for fixed feature set.
Unlike summing each selected tree edge once, this correctly counts path multiplicity.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,argparse,time,sys
from pathlib import Path
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
from scipy.optimize import minimize
import search_vertices as core

def escapes(A,eps,weight=1.):
 aa=np.sum(A*A,axis=1);q=A@A.T/aa[:,None]-1;np.fill_diagonal(q,-1e10);root=int(aa.argmax())
 r=np.maximum(eps-q,0);cost=r*r+1e-18;np.fill_diagonal(cost,0)
 dist,j=dijkstra(csr_matrix(cost.T),indices=root,return_predecessors=True);j[root]=(root+1)%len(A)
 multiplicity=np.ones(len(A));multiplicity[root]=0
 children=np.bincount(j[np.arange(len(A))!=root],minlength=len(A));queue=[int(i) for i in np.flatnonzero(children==0) if i!=root];processed=0
 while queue:
  i=queue.pop();parent=int(j[i]);multiplicity[parent]+=multiplicity[i];children[parent]-=1;processed+=1
  if children[parent]==0 and parent!=root:queue.append(parent)
 assert processed==len(A)-1,'cyclic Dijkstra predecessor graph'
 multiplicity[root]=0;i=np.arange(len(A));val=q[i,j];res=np.maximum(eps-val,0)
 gi=(A[j]-2*A)/aa[:,None]-2*val[:,None]*A/aa[:,None];gj=A/aa[:,None]
 coef=-2*weight*multiplicity*res;grad=coef[:,None]*gi;np.add.at(grad,j,coef[:,None]*gj)
 mx=q.max(axis=1)
 return weight*dist.sum(),grad,dict(root=root,roots=np.where(mx<0)[0].tolist(),margin=float(np.min(np.delete(mx,root))),resmax=float(res.max()),escape=mx)
core.escapes=escapes

def run(X,out,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);np.save(out/'initial.npy',X);best=1e100;calls=0;start=time.time()
 def fun(z):
  nonlocal best,calls
  calls+=1;x=z.reshape(-1,3);v,G,info=core.evaluate(x,eps)
  if v<best:
   best=v;np.save(out/'best.npy',x);(out/'best.json').write_text(json.dumps(dict(info,calls=calls,elapsed=time.time()-start),indent=2)+'\n')
  if calls%200==0:print('TREE',calls,info,flush=True)
  if info['S']==info['U']==1 and min(info['marginV'],info['marginF'])>1e-9:
   np.save(out/'potential.npy',x);(out/'potential.json').write_text(json.dumps(info,indent=2));print('POTENTIAL_TREE110',out,info,flush=True)
  return v,G.ravel()
 res=minimize(fun,X.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':steps,'maxfun':steps*5,'maxcor':30,'maxls':50,'ftol':1e-16,'gtol':1e-10})
 (out/'termination.json').write_text(json.dumps({'success':bool(res.success),'message':str(res.message),'calls':calls,'iterations':int(res.nit)},indent=2))
 print('DONE_TREE',out,res.message,json.load(open(out/'best.json')),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--steps',type=int,default=5000);p.add_argument('--epsilon',type=float,default=1e-7);p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:core.gradient_check()
 else:run(np.load(a.input),a.output,a.steps,a.epsilon)
