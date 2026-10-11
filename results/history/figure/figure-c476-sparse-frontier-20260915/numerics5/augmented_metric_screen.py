"""Proposal screen with a moving compensator in its strict visibility chamber.
Exact rational source and point-identity binding are mandatory; output is numerical.
Usage: OPENBLAS_NUM_THREADS=1 python augmented_metric_screen.py C592_A C486_A PREVIOUS OUT
"""
import hashlib,json,os,sys
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy
from scipy.optimize import least_squares
import projective_metric_screen as prev
assert __debug__
sys.set_int_max_str_digits(0)
SEED=2026091502;NSTARTS=24;MAX_NFEV=850;MARGIN=2e-7
CHILD='d200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d'
PREVIOUS='b6044c3b6820dbf9b776063ba48459348299641e7ed7b42935202f09bbe0e58e'
class Model(prev.Model):
 def __init__(self,base,path):
  super().__init__(path);b=base.read_bytes();assert hashlib.sha256(b).hexdigest()==CHILD
  data=json.loads(b);self.BQ=np.array([[float(Fraction(n,h)) for n in row] for row,h in zip(data['normals'],data['offsets'])])
  self.a0=self.P[117].copy();g=self.BQ@self.a0-1;self.sign=np.sign(g);assert np.min(np.abs(g))>1e-10
  self.gaps=np.abs(g);self.moving=np.array([i for i,f in enumerate(self.raw['faces']) if 117 in f]);assert len(self.moving)==33
  self.mtri=np.array([self.raw['faces'][i] for i in self.moving]);assert self.mtri.shape==(33,3)
 def evaluate(self,x):
  dz=x[:3];div=1+max(0.,float(np.max(-self.sign*(self.BQ@dz)/self.gaps)))
  a=self.a0+dz/div;P=self.P.copy();P[117]=a
  assert np.min(self.sign*(self.BQ@a-1))>0
  Q=self.Q.copy();u,v,wtri=[P[self.mtri[:,i]] for i in range(3)]
  n=np.cross(v-u,wtri-u);h=np.einsum('ij,ij->i',n,u);assert np.min(h)>0;Q[self.moving]=n/h[:,None]
  z=x[3:6];w=z/(1+max(0.,float(np.max(-P@z))));pd=1+P@w;assert np.min(pd)>0
  Y=P/pd[:,None];u,v,wtri=[Y[self.tri[:,i]] for i in range(3)]
  ds=np.einsum('ij,ij->i',u,np.cross(v,wtri));D=np.sum(ds);assert D>0 and np.min(ds)>-1e-12
  g=np.sum(ds[:,None]*(u+v+wtri),axis=0)/(4*D)
  A=np.array([[np.exp(x[6]),x[8],x[9]],[0.,np.exp(x[7]),x[10]],[0.,0.,np.exp(-x[6]-x[7])]])
  X=(Y-g)@A.T;normal=Q+w;hs=1-normal@g;assert np.min(hs)>0;polar=(normal/hs[:,None])@np.linalg.inv(A)
  def exits(points,edges):
   p=points[edges[:,0]];d=points[edges[:,1]]-p
   v=np.einsum('ij,ij->i',p,d)/np.sqrt(np.einsum('ij,ij->i',p,p)*np.einsum('ij,ij->i',d,d))
   r=np.full(len(points),-np.inf);np.maximum.at(r,edges[:,0],v);return r
  return exits(X,self.edges),exits(polar,self.dedges),w,A,g,D/6,a,float(np.min(self.sign*(self.BQ@a-1))),float(np.min(pd))
 def residual(self,x,mode):
  u,s,*_=self.evaluate(x);a=np.minimum(u-MARGIN,0);b=np.minimum(s-MARGIN,0)
  a[int(np.argmin(u)) if mode==-1 else mode]=0;b[int(np.argmin(s))]=0
  return np.concatenate([a,b])
 def record(self,x,mode):
  u,s,w,A,g,V,a,vg,pd=self.evaluate(x)
  return dict(parameters=list(map(float,x)),actual_added_point=a.tolist(),projective_w=w.tolist(),linear_A=A.tolist(),projected_filled_centroid=g.tolist(),projected_volume=float(V),root_mode=mode,S=np.flatnonzero(s<0).tolist(),U=np.flatnonzero(u<0).tolist(),primal_second=float(np.sort(u)[1]),polar_second=float(np.sort(s)[1]),cost=float(np.sum(self.residual(x,mode)**2)),minimum_visibility_gap=vg,minimum_projective_denominator=pd,near_zero_vertices=np.flatnonzero(np.abs(u)<1e-10).tolist(),near_zero_faces=np.flatnonzero(np.abs(s)<1e-10).tolist())
def main(base,src,previous,out):
 m=Model(base,src);oldbytes=previous.read_bytes();assert hashlib.sha256(oldbytes).hexdigest()==PREVIOUS
 old=json.loads(oldbytes);oldbest=min(old['results'],key=lambda r:r['cost'])['parameters'];rng=np.random.default_rng(SEED);records=[]
 r0=m.record(np.zeros(11),-1);assert r0['S']==m.raw['stable_face_ids'] and r0['U']==m.raw['unstable_vertices']
 bounds=([-8]*3+[-6]*3+[-1.5]*2+[-2]*3,[8]*3+[6]*3+[1.5]*2+[2]*3)
 best=np.r_[np.zeros(3),oldbest]
 for j in range(NSTARTS):
  mode=[-1,79,117][j%3]
  if j<3:x=np.zeros(11)
  elif j<6:x=np.r_[np.zeros(3),oldbest]
  elif j<12:x=np.r_[rng.normal(0,.4,3),rng.normal(0,.4,3),rng.normal(0,.15,5)]
  else:x=best+rng.normal(0,.25,11)
  x=np.clip(x,np.array(bounds[0])+1e-6,np.array(bounds[1])-1e-6)
  ans=least_squares(lambda t:m.residual(t,mode),x,jac='3-point',bounds=bounds,max_nfev=MAX_NFEV,ftol=1e-12,xtol=1e-12,gtol=1e-12,diff_step=1e-5)
  r=m.record(ans.x,mode);r.update(start=j,initial_parameters=list(map(float,x)),nfev=int(ans.nfev),status=int(ans.status),message=str(ans.message));records.append(r)
  if r['cost']<=min(k['cost'] for k in records):best=ans.x.copy()
  report=dict(status='NUMERICAL_PROPOSALS_ONLY',base_sha256=CHILD,source_sha256=prev.EXPECTED,previous_sha256=PREVIOUS,seed=SEED,nstarts_requested=NSTARTS,max_nfev=MAX_NFEV,margin=MARGIN,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),baseline=r0,results=records)
  out.write_bytes(prev.B(report));print('TRIAL',j,'S/U',len(r['S']),len(r['U']),'cost',r['cost'],'nfev',r['nfev'],'point',r['actual_added_point'],flush=True)
  if len(r['S'])==len(r['U'])==1 and min(r['primal_second'],r['polar_second'])>0:print('NUMERICAL_OWN110_PROPOSAL_REQUIRES_EXACT_GATE',flush=True);break
 print('MOVING_COMPENSATOR_METRIC_SCREEN_TERMINAL',len(records),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
