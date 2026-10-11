"""Finite 23-parameter search: twelve critical controls, six caps, five physical
metric parameters. Global roots can change. Complete numerical geometric and
true-edge screens are saved; numerical small losses never constitute a proof.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from atlas_model import Atlas
m=Atlas(Path(os.environ['NH72_BASE_REPORT']));out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
seed=np.r_[json.loads(Path(os.environ['NH72_LOCAL_MASS_CHECKPOINT']).read_text())['z'],np.zeros(5)]
n=23;rows=[];rng=np.random.default_rng(141421);clock=time.monotonic();best=(1e10,seed.copy());calls=0;win=False
low=np.r_[np.full(12,-10),np.full(6,-.85),[-1.5,-1.5,-3,-3,-3]];hi=np.r_[np.full(12,10),np.full(6,3),[1.5,1.5,3,3,3]]
def data(z,record=False):
 global calls,best,win
 pv,dv,g,gap,den,vol=m.calc(z);P,_=m.points(z);X=P-g;ft=X[m.ft];N=np.cross(ft[:,1]-ft[:,0],ft[:,2]-ft[:,0]);Y=N/(N*ft[:,0]).sum(axis=1)[:,None]
 ru=np.argmax((X*X).sum(axis=1).real);rs=np.argmax((Y*Y).sum(axis=1).real)
 pi=np.array([np.where(m.src==i)[0][np.argmax(pv[m.src==i].real)] for i in range(m.mesh.n) if i!=ru]);di=np.array([np.where(m.fs==i)[0][np.argmax(dv[m.fs==i].real)] for i in range(m.mesh.nf) if i!=rs])
 mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1);geo=gap[np.arange(m.mesh.nf),j]
 E=X[m.ep[:,1]]-X[m.ep[:,0]];lengths=np.sqrt((E*E).sum(axis=1));baseE=m.P[m.ep[:,1]]-m.P[m.ep[:,0]];limit=np.sqrt((baseE*baseE).sum(axis=1))*1e-3
 def neg(v):w=v.copy();w[v.real>=0]=0;return w
 vals=np.r_[neg(pv[pi]-1e-7),neg(dv[di]-1e-7),1e4*neg(geo-1e-9),100*neg(den-.01),100*neg(1+z[12:18]-.01),100*neg(lengths-limit)]
 if record:
  calls+=1
  if geo.min()>1e-10 and den.min()>.01 and min(1+z[12:18])>.01 and min(lengths-limit)>0:
   S=1+sum(dv[di]<0);U=1+sum(pv[pi]<0);score=S+U+min(np.linalg.norm(vals),.9)
   if score<best[0]:
    b=m.brief(z);b.update(loss=float(np.linalg.norm(vals)),calls=calls,rootU=m.keep[int(ru)],rootS=m.labels[int(rs)])
    if b['planarity']<1e-9 and b['counts'][0]+b['counts'][1]-b['counts'][2]==2:
     best=(score,z.copy());(out/'BEST.json').write_text(json.dumps(b,sort_keys=True));print('BEST',b['counts'],b['loss'],b['min_gap'],'calls',calls,'sec',time.monotonic()-clock,flush=True)
     if b['counts']==[1,1,0]:win=True
 return vals

def jac(z):
 J=np.empty((len(data(z)),n))
 for i in range(n):
  a=z.astype(complex);a[i]+=1e-26j;J[:,i]=data(a).imag/1e-26
 return J
for k in range(int(sys.argv[2])):
 z=seed.copy() if k==0 else best[1].copy()
 if k:
  if k%3==0:z[18:]+=rng.normal(size=5)*.3
  z[:18]+=rng.normal(size=18)*10**rng.uniform(-5,-.3)
 z=np.clip(z,low+1e-8,hi-1e-8)
 sol=least_squares(lambda z:data(z,True),z,jac=jac,bounds=(low,hi),max_nfev=300,ftol=1e-11,xtol=1e-12,gtol=1e-12,x_scale='jac')
 b=m.brief(sol.x);b.update(start=k,nfev=sol.nfev,loss=float(np.linalg.norm(sol.fun)));rows.append(b);(out/'ALL.json').write_text(json.dumps(rows,sort_keys=True));print('START_DONE',k,b['counts'],time.monotonic()-clock,flush=True)
 if win:break
(out/'CONFIG.json').write_text(json.dumps(dict(seed=141421,starts=len(rows),calls=calls,max_nfev=300,positive_target=1e-7,dimension=23,win_numerical=win)))
print('TWENTYTHREE_PHYSICAL_PATCH_SEARCH_DONE',len(rows),calls,flush=True)
