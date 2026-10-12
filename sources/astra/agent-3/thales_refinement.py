"""Add literal physical stellar controls within the universal85-vertex bound.
Every initial new point has a positive reference escape, verified explicitly.
All subsequent evaluations integrate the actual uniform hull mass.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from vertex_geometry import geometry
from support_geometry import escape
from thales_chart import Chart,Search
from polish_211 import run as polish
from persistence_birth import evaluate

def add_points(X,target,seed):
 rng=np.random.default_rng(seed);g=geometry(X,False);X=g['Z'][g['vertices']];g=geometry(X,False);T=g['T'];n=g['H'];n/=np.linalg.norm(n,axis=1)[:,None];m=(X[T].sum(1))/3
 w=rng.dirichlet([3,3,3],size=len(T));p=np.einsum('ti,tic->tc',w,X[T]);A=np.linalg.norm(np.cross(X[T[:,1]]-X[T[:,0]],X[T[:,2]]-X[T[:,0]]),axis=1)
 score=np.max(p@X.T,axis=1)-np.sum(p*p,axis=1);ok=np.flatnonzero(score>1e-5);assert len(ok)>=target-len(X)
 # Random weighted priority, retained seed and literal points define the trial.
 priority=np.log(rng.random(len(ok)))/np.sqrt(A[ok]);which=ok[np.argsort(-priority)[:target-len(X)]]
 Y=np.vstack((X,p[which]+1e-6*n[which]));ref=escape(Y)[0];assert int(np.sum(ref<0))==1
 return Y,dict(source_count=len(X),added_facets=which.tolist(),triangles=T[which].tolist(),barycentric=w[which].tolist(),outward_height=1e-6,seed=seed)

def run(source,out):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);start=np.load(source);rows=[]
 for N in [60,75,85]:
  for k in range(3):
   seed=48600+N+k;d=out/f'n{N}_s{seed}';d.mkdir();Y,meta=add_points(start,N,seed);np.save(d/'added.npy',Y);(d/'construction.json').write_text(json.dumps(meta,indent=2))
   polish(d/'added.npy',d/'initial_polish',250,1e-6);sourcepath=d/'initial_polish/success.npy'
   if not sourcepath.exists():rows.append(dict(N=N,seed=seed,result='initial strict211 correction failed'));(out/'trials.json').write_text(json.dumps(rows,indent=2));continue
   Y=np.load(sourcepath);g=geometry(Y,False);Y=g['Z'][g['vertices']];Y/=np.max(np.linalg.norm(Y,axis=1));c=Chart(Y);s=Search(c,d/'search',[.02,.05,.005][k]);s.run(4000)
   polish(s.out/'best.npy',d/'final_polish',400,1e-6);p=d/'final_polish/success.npy'
   if p.exists():row=dict(N=N,seed=seed,result='strict211 numerical',path=str(p),persistence=evaluate(np.load(p))[2])
   else:row=dict(N=N,seed=seed,result='final strict211 correction failed')
   rows.append(row);(out/'trials.json').write_text(json.dumps(rows,indent=2));print('REFINEMENT_TRIAL',row,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');a=p.parse_args();run(a.input,a.out)
