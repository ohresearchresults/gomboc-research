"""Coupled material/own-centroid continuation with two fully movable physical planes.
Actual convex hull and mass are recomputed for every trial, allowing contact changes.
All displayed f-vectors and equilibrium counts here are NUMERICAL PROPOSALS only."""
import sys,json,argparse,time
import numpy as np
from scipy.spatial import HalfspaceIntersection,ConvexHull,cKDTree
from scipy.optimize import least_squares
from fractions import Fraction as F
from pathlib import Path
import radial
sys.set_int_max_str_digits(0)
class Planes:
 def __init__(self,G,rows=(114,121)):
  raw,P=radial.reconstruct(G);self.q=np.array([[float(F(v,h[-1])) for v in h[:3]] for h in raw['H']]);self.rows=np.array(rows);self.scale=np.linalg.norm(self.q[self.rows],axis=1);self.last=None;self.val=None
 def calc(self,z):
  q=self.q.copy();q[self.rows]+=z.reshape(-1,3)*self.scale[:,None]
  try:
   P=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3)).intersections;tree=cKDTree(P);dead=set();keep=[]
   for i in range(len(P)):
    if i not in dead:keep.append(i);dead.update(tree.query_ball_point(P[i],1e-9))
   P=P[keep];H=ConvexHull(P);T=H.simplices.copy();X=P[T];cr=np.cross(X[:,1]-X[:,0],X[:,2]-X[:,0]);bad=(np.einsum('ni,ni->n',cr,H.equations[:,:3])<0);T[bad]=T[bad][:,::-1];X=P[T];dt=np.einsum('ni,ni->n',X[:,0],np.cross(X[:,1],X[:,2]));vol=dt.sum()/6;g=np.einsum('n,ni->i',dt,X.sum(axis=1))/(4*dt.sum());Z=P-g;diff=P[None,:,:]-P[:,None,:];leng=np.linalg.norm(diff,axis=2);length=leng*np.linalg.norm(Z,axis=1)[:,None];esc=np.einsum('ijc,ic->ij',diff,Z)/np.maximum(length,1e-30);np.fill_diagonal(esc,-1);u=esc.max(axis=1);root=np.argmin(np.linalg.norm(P-[0,0,1],axis=1));rr=np.delete(1e-5-u,root);ru=np.sort(np.maximum(rr,0))[::-1];outU=np.zeros(450);outU[:min(450,len(ru))]=ru[:450]
   norms=np.linalg.norm(q,axis=1);h=1-q@g;foot=g+q*(h/(norms**2))[:,None];sl=foot@q.T-1;np.fill_diagonal(sl,-1);f=(sl/norms[None,:]).max(axis=1);active=(abs(P@q.T-1)<1e-7).sum(axis=0)>=3;rf=np.maximum(1e-6-f,0);rf[~active]=0;rf[114]=0;v=np.r_[rf,outU,max(0,u[root]+1e-5),max(0,f[114]+1e-6)];s={'S':np.flatnonzero((f<0)&active).tolist(),'U':np.flatnonzero(u<0).tolist(),'g':g.tolist(),'volume':float(vol),'V_proposal':len(P),'F_proposal':int(active.sum()),'E_proposal':len(P)+int(active.sum())-2,'loss':float(v@v),'row_normalized':q[self.rows].tolist()};return v,s
  except Exception as e:return np.full(len(self.q)+452,100.),{'error':str(e),'loss':1e9}
 def fun(self,z):
  if self.last is None or not np.array_equal(z,self.last):self.last=z.copy();self.val=self.calc(z)
  return self.val[0]
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--start',default='generators/QUOT_11_1_G6.json');a.add_argument('--tag',default='PLANE2');a.add_argument('--starts',type=int,default=12);a.add_argument('--maxeval',type=int,default=120);v=a.parse_args();G=json.load(open(v.start));M=Planes(G);rng=np.random.default_rng(5982121);best=1e9;trace=[]
 for it in range(v.starts):
  z=np.zeros(6) if it==0 else (bestz+rng.normal(size=6)*.025 if it%3==0 else rng.normal(size=6)*.035);z=np.clip(z,-.249,.249);t=time.time();r=least_squares(M.fun,z,bounds=(-.25,.25),jac='3-point',diff_step=1e-5,max_nfev=v.maxeval,ftol=1e-9,gtol=1e-9,xtol=1e-9,x_scale=.03);rr,s=M.calc(r.x);row={'it':it,'x':r.x.tolist(),'nfev':r.nfev,'success':bool(r.success),'seconds':time.time()-t,**s};trace.append(row);print(row,flush=True);Path(v.tag+'.json').write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if s['loss']<best:best=s['loss'];bestz=r.x.copy()
  if len(s.get('S',[]))==len(s.get('U',[]))==1 and s['E_proposal']<312:break
