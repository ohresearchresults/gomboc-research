"""Finite critical-star geometry + physical projective/metric proposal search.
Usage: OPENBLAS_NUM_THREADS=1 python critical476_primal_screen.py BEFORE_A OUT
Every finite promising point set must receive separate exact hull/own-mass audits.
"""
import hashlib,json,os,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import least_squares
import metric476_screen as base
assert __debug__;sys.set_int_max_str_digits(0)
SEED=2026091504;STARTS=12;MAX_NFEV=600;MARGIN=2e-6;GROUP_DIGITS=9
MOVING=[63,77,105,107,110,111,114]
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
class Model:
 def __init__(self,path):
  self.source=base.Model(path);self.P0=self.source.P.copy();self.n=len(self.P0);self.initial=np.r_[np.zeros(21),self.source.initial()]
 def evaluate(self,x):
  P=self.P0.copy();P[MOVING]+=x[:21].reshape(7,3)
  hull=ConvexHull(P);T=hull.simplices.copy();p=P[T]
  sg=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),hull.equations[:,:3]);fl=sg<0;T[fl]=T[fl][:,[0,2,1]]
  if min(-hull.equations[:,3])<1e-8:raise ValueError('origin not strictly inside preprojective hull')
  z=x[21:24];w=z/(1+max(0.,float(max(-P@z))));Y=P/(1+P@w)[:,None]
  t=Y[T];ds=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]));D=ds.sum();assert D>0 and min(ds)>-1e-11
  g=np.einsum('i,ij->j',ds,t.sum(axis=1))/(4*D)
  v=x[24:];A=np.array([[np.exp(v[0]),v[2],v[3]],[0,np.exp(v[1]),v[4]],[0,0,np.exp(-v[0]-v[1])]])
  Q=hull.equations[:,:3]/(-hull.equations[:,3])[:,None]
  _,idx=np.unique(np.round(Q,GROUP_DIGITS),axis=0,return_index=True);idx=np.sort(idx);Q=Q[idx]+w
  heights=1-Q@g;assert min(heights)>0
  X=(Y-g)@A.T;Z=Q/heights[:,None]@np.linalg.inv(A)
  def escape(X):
   dif=X[None,:,:]-X[:,None,:];den=np.linalg.norm(X,axis=1)[:,None]*np.linalg.norm(dif,axis=2);np.fill_diagonal(den,1)
   out=np.einsum('ij,ikj->ik',X,dif)/den;np.fill_diagonal(out,-np.inf);return out.max(axis=1)
  u=escape(X);s=escape(Z);active=np.zeros(self.n,bool);active[hull.vertices]=True;u[~active]=1.
  return u,s,P,w,A,g,D/6,hull,idx
 def residual(self,x,root=-1):
  u,s,_,_,_,_,_,h,_=self.evaluate(x)
  ru=np.minimum(u-MARGIN,0);ru[np.argmin(u) if root<0 else root]=0
  rs=np.minimum(s-MARGIN,0);rs[np.argmin(s)]=0
  vals=np.sort(rs);out=np.zeros(2*self.n-4);out[:len(vals)]=vals
  return np.r_[ru,out,1e-3*max(0,len(h.vertices)+len(s)-2-310)]
 def record(self,x,root):
  u,s,P,w,A,g,V,h,idx=self.evaluate(x)
  return dict(parameters=x.tolist(),moving_before_raw_lex=MOVING,moved_points=P[MOVING].tolist(),projective_w=w.tolist(),linear_A=A.tolist(),projected_actual_centroid=g.tolist(),projected_volume=float(V),S=int(sum(s<0)),U=int(sum(u<0)),U_before_labels=np.flatnonzero(u<0).tolist(),stable_input_triangles=h.simplices[idx][s<0].tolist(),V_est=len(h.vertices),F_est=len(s),E_est=len(h.vertices)+len(s)-2,root_mode=root,cost=float(sum(self.residual(x,root)**2)),primal_second=float(np.sort(u)[1]),polar_second=float(np.sort(s)[1]),nearU=np.flatnonzero(abs(u)<1e-9).tolist(),nearS=np.flatnonzero(abs(s)<1e-9).tolist(),proposal_only=True)
def main(src,out):
 m=Model(src);rng=np.random.default_rng(SEED);initial=m.record(m.initial,-1);assert(initial['S'],initial['U'],initial['E_est'])==(2,2,238)
 print('BASE',initial['S'],initial['U'],initial['E_est'],initial['cost'],flush=True)
 lo=np.array([-.4]*21+[-12]*3+[-3]*2+[-6]*3);hi=-lo;rows=[];best=m.initial.copy();bestcost=np.inf
 for k in range(STARTS):
  mode=[77,63,-1][k%3]
  if k==0:x=m.initial.copy()
  elif k<6:x=m.initial+np.r_[rng.normal(0,.003 if k<3 else .02,21),rng.normal(0,.04,8)]
  else:x=best+np.r_[rng.normal(0,.012,21),rng.normal(0,.03,8)]
  x=np.clip(x,lo+1e-6,hi-1e-6)
  try:
   ans=least_squares(lambda z:m.residual(z,mode),x,bounds=(lo,hi),jac='3-point',diff_step=1e-5,max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
   r=m.record(ans.x,mode);r.update(start=k,initial_parameters=x.tolist(),nfev=int(ans.nfev),status=int(ans.status),message=str(ans.message))
   if r['cost']<bestcost:best=ans.x.copy();bestcost=r['cost']
   print('CRITICAL476',k,'S/U',r['S'],r['U'],'E',r['E_est'],'cost',r['cost'],'nfev',r['nfev'],flush=True)
  except(QhullError,ValueError,AssertionError,np.linalg.LinAlgError)as e:
   r=dict(start=k,initial_parameters=x.tolist(),error=type(e).__name__,message=str(e));print('ERROR',k,r['error'],flush=True)
  rows.append(r);report=dict(status='NUMERICAL_CRITICAL_STAR_PROPOSALS',source_sha256=base.EXPECTED,seed=SEED,starts_requested=STARTS,max_nfev=MAX_NFEV,moving=MOVING,margin=MARGIN,group_digits=GROUP_DIGITS,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),baseline=initial,results=rows)
  out.write_bytes(B(report))
  if r.get('S')==r.get('U')==1 and r['E_est']<=310 and min(r['primal_second'],r['polar_second'])>1e-9:print('CRITICAL476_NUMERICAL110_NEEDS_EXACT_GATE',flush=True);break
 print('CRITICAL476_PRIMAL_SCREEN_TERMINAL',len(rows),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
