"""Finite numerical moment-closing routed-hull proposals; NOT exact audits.
Construct the actual hull of C592 with a logarithmic-radius geodesic chain
from its old apex to a free opposite endpoint, targeting the C602 centroid.
Usage: OPENBLAS_NUM_THREADS=1 python spiral_bridge_screen.py C592_A C602_A OUT
"""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import least_squares
import scipy
assert __debug__
sys.set_int_max_str_digits(0)
CHILD='d200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d'
PARENT='2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'
LINKS=[4,6,8,10,12,16,19,24,28,32]
A0=np.array([874577931702,454209162144,-558471315966],dtype=float)/1e12
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def centroid(P,h):
 T=P[h.simplices];ds=np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2]))
 orient=np.einsum('ij,ij->i',np.cross(T[:,1]-T[:,0],T[:,2]-T[:,0]),h.equations[:,:3]);ds*=np.sign(orient)
 D=np.sum(ds);assert D>0 and np.min(ds)>-1e-10
 return np.sum(ds[:,None]*np.sum(T,axis=1),axis=0)/(4*D),D/6
class Model:
 def __init__(self,base,parent):
  bb=base.read_bytes();pb=parent.read_bytes();assert hashlib.sha256(bb).hexdigest()==CHILD and hashlib.sha256(pb).hexdigest()==PARENT
  a=json.loads(bb);p=json.loads(pb);self.P=np.array([[float(Fraction(s)) for s in x] for x in a['raw_vertices']]);self.c=np.array([float(Fraction(s)) for s in p['raw_centroid']]);self.r=np.array([0.,0.,1.]);assert any(np.array_equal(v,self.r) for v in self.P)
 def points(self,a,n):
  u=self.r-self.c;v=a-self.c;R=np.linalg.norm(u);L=np.linalg.norm(v);e=u/R
  trans=v-e*(e@v);tl=np.linalg.norm(trans);assert L>1e-9 and tl>1e-9
  f=trans/tl;phi=np.arctan2(tl,e@v);s=np.arange(1,n)/n
  route=self.c+(R*np.exp(np.log(L/R)*s))[:,None]*(np.cos(phi*s)[:,None]*e+np.sin(phi*s)[:,None]*f)
  return np.concatenate([self.P,route,[a]]),float(phi),float(L/R)
 def residual(self,a,n):
  P,_,_=self.points(a,n);h=ConvexHull(P);g,V=centroid(P,h);return g-self.c
 def report(self,a,n):
  P,phi,ratio=self.points(a,n);h=ConvexHull(P);g,V=centroid(P,h)
  def features(c):
   X=P[h.vertices]-c;dot=X@X.T;vals=dot-np.diag(dot)[:,None];np.fill_diagonal(vals,-np.inf);ex=vals.max(axis=1)
   q=h.equations[:,:3]/(-h.equations[:,3]-h.equations[:,:3]@c)[:,None]
   # Numerical duplicate grouping ONLY, never a true-edge exact certificate.
   _,idx=np.unique(np.round(q,9),axis=0,return_index=True);q=q[np.sort(idx)]
   Q=q@q.T;ev=Q-np.diag(Q)[:,None];np.fill_diagonal(ev,-np.inf);pe=ev.max(axis=1)
   return dict(S_est=int(np.sum(pe<1e-9)),U_est=int(np.sum(ex<1e-9)),U_input_labels=h.vertices[ex<1e-9].tolist(),V_est=len(h.vertices),F_est=len(q),E_est=len(h.vertices)+len(q)-2,uncertain_U=int(np.sum(np.abs(ex)<1e-9)),uncertain_S=int(np.sum(np.abs(pe)<1e-9)))
  return dict(links=n,endpoint=a.tolist(),volume=float(V),actual_centroid=g.tolist(),target_centroid=self.c.tolist(),mass_residual=self.residual(a,n).tolist(),angle=phi,radius_ratio=ratio,ascent_product=ratio*np.cos(phi/n)**n,reverse_ascent_product=(1/ratio)*np.cos(phi/n)**n,own=features(g),reference=features(self.c),route_points=P[len(self.P):].tolist(),exposed_input_labels=h.vertices.tolist(),proposal_only=True)
def main(base,parent,out):
 m=Model(base,parent);records=[];previous=A0.copy()
 for n in LINKS:
  for variant in range(2):
   start=A0.copy() if variant==0 else previous.copy()
   ans=least_squares(lambda a:m.residual(a,n),start,bounds=([-2.,-2.,-3.],[3.,3.,-.1]),jac='3-point',max_nfev=250,ftol=1e-12,xtol=1e-12,gtol=1e-12,diff_step=1e-5)
   r=m.report(ans.x,n);r.update(start_endpoint=start.tolist(),variant=variant,nfev=int(ans.nfev),status=int(ans.status));records.append(r)
   if np.linalg.norm(r['mass_residual'])<1e-8:previous=ans.x.copy()
   out.write_bytes(B(dict(status='NUMERICAL_ROUTED_MASS_PROPOSALS_ONLY',C592_sha256=CHILD,C602_sha256=PARENT,links=LINKS,numpy=np.__version__,scipy=scipy.__version__,coplanar_q_group_round_decimals=9,classification_tolerance=1e-9,results=records)))
   print('ROUTE',n,variant,'res',np.linalg.norm(r['mass_residual']),'own',r['own'],'product',r['ascent_product'],'a',r['endpoint'],flush=True)
 print('SPIRAL_BRIDGE_MASS_SCREEN_TERMINAL',len(records),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
