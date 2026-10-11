"""Continuous chord-score loss for dynamic incidence, own mass unchanged in definition."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import search_vertices as core
import numpy as np
from pathlib import Path
import argparse,json

def escapes(A,eps,weight=1.):
 aa=np.sum(A*A,axis=1);B=A@A.T;score=B/aa[:,None]-1.;np.fill_diagonal(score,-np.inf)
 j=score.argmax(axis=1);i=np.arange(len(A));val=score[i,j];root=int(aa.argmax());res=np.maximum(eps-val,0);res[root]=0
 gi=(A[j]-2*A)/aa[:,None]-2*val[:,None]*A/aa[:,None];gj=A/aa[:,None]
 coef=-2*weight*res;grad=coef[:,None]*gi;np.add.at(grad,j,coef[:,None]*gj)
 return weight*np.sum(res*res),grad,dict(root=root,roots=np.where(val<0)[0].tolist(),margin=float(np.min(np.delete(val,root))),resmax=float(res.max()),escape=val)
core.escapes=escapes
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=31928);p.add_argument('--n',type=int,default=85);p.add_argument('--steps',type=int,default=5000);p.add_argument('--trials',type=int,default=4);p.add_argument('--epsilon',type=float,default=1e-5);p.add_argument('--source',default='primal');p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.check:core.gradient_check();raise SystemExit
 for seed in range(a.seed,a.seed+a.trials):
  folder=Path(f'artifacts/score_search/{a.source}_{a.n}_{seed}');folder.mkdir(parents=True,exist_ok=False)
  core.trial(seed,a.n,a.steps,a.epsilon,folder,a.source)
