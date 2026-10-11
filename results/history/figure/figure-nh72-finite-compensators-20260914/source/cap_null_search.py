"""Finite exploration of the actual three-dimensional mass-closed cap manifold."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import root,least_squares
from cluster import Cluster

def run(report,j,remove,starts,output):
 m=Cluster(report,j,remove);base=m.close();dep0=np.array(base['eta'])[[2,3,4]];initial=m.mesh.state(m.P,m.c);allowed=set(initial['U']);seed=140926+sum(remove);rng=np.random.default_rng(seed);rows=[];best=(1e99,None);out=Path(output);out.mkdir(exist_ok=False)
 def evaluate(free,depstart=dep0):
  def pack(dep):return np.array([free[0],free[1],dep[0],dep[1],dep[2],free[2]])
  def eq(dep):
   P,den=m.points(pack(dep));return m.mesh.mass(P)[2]-m.c
  sol=root(eq,depstart,options={'xtol':1e-10});z=pack(sol.x);P,den=m.points(z);st=m.mesh.state(P);st['eta']=z;st['min_den']=float(den.min());st['com_error']=float(np.linalg.norm(eq(sol.x)));return st
 def res(free):
  try:
   st=evaluate(free);pv=st['ptop'].copy();dv=st['dtop'].copy();pv[list(allowed)]=1;dv[initial['S']]=1
   return np.r_[np.minimum(pv-1e-7,0),np.minimum(dv-1e-7,0),30*min(st['min_gap']-1e-8,0),1000*st['com_error'],10*min(st['min_den']-.01,0),10*np.minimum(1+st['eta']-.001,0)]
  except (ValueError,np.linalg.LinAlgError,FloatingPointError):return np.full(len(m.P)+len(m.faces)+9,1e3)
 for k in range(starts):
  free=np.zeros(3) if k==0 else (best[1] if best[1] is not None and k%3 else np.zeros(3))+rng.normal(size=3)*10**rng.uniform(-3,-.2)
  free=np.clip(free,-.8,2)
  sol=least_squares(res,free,bounds=(-.9,3.),max_nfev=200,ftol=1e-9,xtol=1e-10,gtol=1e-10,diff_step=1e-5)
  st=evaluate(sol.x);r=m.mesh.brief(st);r['eta']=st['eta'].tolist();r.update(free=sol.x.tolist(),loss=float(np.linalg.norm(res(sol.x))),start=k,nfev=sol.nfev)
  rows.append(r);(out/'ALL.json').write_text(json.dumps(rows,sort_keys=True))
  good=r['min_gap']>0 and r['min_den']>0 and min(1+st['eta'])>0 and r['com_error']<1e-10
  if good and r['loss']<best[0]:best=(r['loss'],sol.x.copy());(out/'BEST.json').write_text(json.dumps(r,sort_keys=True));print('BEST',j,remove,k,r['counts'],r['loss'],r['eta'],flush=True)
  if good and r['counts']==[1,2,1]:break
 print('FINITE_MASS_CLOSED_NULL_SEARCH_DONE',j,len(rows),best[0],flush=True)
 (out/'CONFIG.json').write_text(json.dumps(dict(deleted=j,remove=remove,starts=starts,seed=seed,max_nfev=200),sort_keys=True))
if __name__=='__main__':
 report,j,remove_text,starts,out=sys.argv[1:];run(report,int(j),list(map(int,remove_text.split(','))),int(starts),out)
