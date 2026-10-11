"""Numerical globally mass-centred spiral-hull screen; no exact certificate.
Usage OPENBLAS_NUM_THREADS=1 python centred_bridge_scan.py C592_A C602_A OUT
"""
import hashlib,json,sys
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
import scipy
import spiral_bridge_screen as old
assert __debug__
LINKS=[2,3,4,5,6,8,10,12,16,20,24,28,32]
SCALES=[.6,.8,1.,1.15,1.35,1.6,2.,2.5,3.5]
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def moments(P,T):
 p=P[T];s=p.sum(axis=1);d=np.einsum('ij,ij->i',p[:,0],np.cross(p[:,1],p[:,2]));assert min(d)>-1e-10
 V=d.sum()/6;g=np.einsum('i,ij->j',d,s)/(24*V)
 Q=(np.einsum('i,ij,ik->jk',d,s,s)+np.einsum('i,ilj,ilk->jk',d,p,p))/(120*V)
 return V,g,Q

def mass_centre(P,T):
 w=np.zeros(3);steps=[]
 for j in range(60):
  den=1+P@w;assert min(den)>0
  V,g,Q=moments(P/den[:,None],T)
  if np.linalg.norm(g)<2e-13:return w,V,g,steps
  # dg/dw=-5 E(XX^T)+4gg^T, by differentiating the actual filled moments.
  step=np.linalg.solve(5*Q-4*np.outer(g,g),g);lam=1.
  for k in range(50):
   nw=w+lam*step;dd=1+P@nw
   if min(dd)>1e-8:
    nv,ng,nq=moments(P/dd[:,None],T)
    if np.linalg.norm(ng)<np.linalg.norm(g):break
   lam*=.5
  else:raise RuntimeError('Newton line search did not decrease physical centroid norm')
  w=nw;steps.append(lam)
 raise RuntimeError('centroid Newton limit')

def make(P):
 hull=ConvexHull(P);T=hull.simplices.copy();x=P[T];flip=np.einsum('ij,ij->i',np.cross(x[:,1]-x[:,0],x[:,2]-x[:,0]),hull.equations[:,:3])<0
 T[flip]=T[flip][:,[0,2,1]]
 return hull,T

def features(P,Q):
 D=P@P.T;v=D-np.diag(D)[:,None];np.fill_diagonal(v,-np.inf);u=v.max(axis=1)
 D=Q@Q.T;v=D-np.diag(D)[:,None];np.fill_diagonal(v,-np.inf);s=v.max(axis=1)
 return dict(S_est=int(sum(s<1e-9)),U_est=int(sum(u<1e-9)),U_indices=np.flatnonzero(u<1e-9).tolist(),S_indices=np.flatnonzero(s<1e-9).tolist(),near_U=np.flatnonzero(np.abs(u)<1e-9).tolist(),near_S=np.flatnonzero(np.abs(s)<1e-9).tolist(),secondU=float(np.sort(u)[1]),secondS=float(np.sort(s)[1]))
def evaluate(model,a,n):
 P,phi,ratio=model.points(a,n);P-=model.c
 h,T=make(P);w,V,g,steps=mass_centre(P,T);Y=P/(1+P@w)[:,None]
 norms=h.equations[:,:3];hs=-h.equations[:,3];Q=norms/hs[:,None]+w
 _,idx=np.unique(np.round(Q,9),axis=0,return_index=True);idx=np.sort(idx);Q=Q[idx]
 # Correct for the tiny residual actual filled centroid, not a frozen numerical zero.
 own=features(Y[h.vertices]-g,Q/(1-Q@g)[:,None]);ref=features(P[h.vertices],Q-w)
 return dict(links=n,endpoint=a.tolist(),projective_w=w.tolist(),origin=model.c.tolist(),new_centroid=g.tolist(),volume=float(V),minimum_projective_denominator=float(min(1+P@w)),newton_steps=steps,V_est=len(h.vertices),F_est=len(Q),E_est=len(h.vertices)+len(Q)-2,own=own,reference=ref,angle=phi,radius_ratio=ratio,original_route_ascent_product=ratio*np.cos(phi/n)**n,route_points=(P[len(model.P):]+model.c).tolist(),exposed_input_labels=h.vertices.tolist(),proposal_only=True)
def main(base,parent,out):
 m=old.Model(base,parent);rows=[]
 for n in LINKS:
  for scale in SCALES:
   a=m.c+scale*(old.A0-m.c)
   try:r=evaluate(m,a,n)
   except Exception as e:r=dict(links=n,scale=scale,error=repr(e),proposal_only=True)
   r['scale']=scale;rows.append(r)
   out.write_bytes(B(dict(status='NUMERICAL_MASS_CENTRED_ROUTE_SCAN_ONLY',C592_sha256=old.CHILD,C602_sha256=old.PARENT,links=LINKS,scales=SCALES,numpy=np.__version__,scipy=scipy.__version__,rounding_decimals=9,feature_tolerance=1e-9,results=rows)))
   if 'error' in r:print('ERROR',n,scale,r['error'],flush=True)
   elif r['E_est']<=310:print('ROUTE',n,scale,'E',r['E_est'],'own',r['own']['S_est'],r['own']['U_est'],'ref',r['reference']['S_est'],r['reference']['U_est'],flush=True)
 print('CENTRED_BRIDGE_SCAN_TERMINAL',len(rows),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
