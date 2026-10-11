"""Deterministic proposal screen, not an exact construction certificate.
Input is the exact, hash-pinned C486 R12 audit. Recompute filled mass after
projective deformation, then evaluate primal/polar escapes under a metric.
Usage: OPENBLAS_NUM_THREADS=1 python projective_metric_screen.py A.json OUT.json
"""
import hashlib,json,os,sys,time
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy
from scipy.optimize import least_squares
assert __debug__
sys.set_int_max_str_digits(0)
SEED=20260915;NSTARTS=18;MAX_NFEV=700;MARGIN=2e-7
EXPECTED='8ee12742068e4246b3b7daf688703b3ce6f1c9803202a7d05f96e3ad8806ac21'
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def load(path):
 b=path.read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED
 raw=json.loads(b);P=np.array([[float(Fraction(s)) for s in p] for p in raw['raw_vertices']])
 Q=np.array([[float(Fraction(v,h)) for v in n] for n,h in zip(raw['normals'],raw['offsets'])])
 e=np.array(raw['edges']);edges=np.concatenate([e,e[:,::-1]])
 tri=[];inc={tuple(x):[] for x in raw['edges']}
 for k,f in enumerate(raw['faces']):
  tri.extend([[f[0],f[j],f[j+1]] for j in range(1,len(f)-1)])
  for i,j in zip(f,f[1:]+f[:1]):inc[tuple(sorted((i,j)))].append(k)
 de=np.array([v for _,v in sorted(inc.items())]);assert de.shape==(243,2)
 return raw,P,Q,np.array(tri),edges,np.concatenate([de,de[:,::-1]])
class Model:
 def __init__(self,path):self.raw,self.P,self.Q,self.tri,self.edges,self.dedges=load(path)
 def evaluate(self,x):
  z=x[:3];den=1+max(0.,float(np.max(-self.P@z)));w=z/den
  pd=1+self.P@w;assert np.min(pd)>0
  Y=self.P/pd[:,None]
  u,v,wtri=[Y[self.tri[:,j]] for j in range(3)]
  ds=np.einsum('ij,ij->i',u,np.cross(v,wtri));D=np.sum(ds)
  assert D>0 and np.min(ds)>-1e-12
  g=np.sum(ds[:,None]*(u+v+wtri),axis=0)/(4*D)
  A=np.array([[np.exp(x[3]),x[5],x[6]],[0.,np.exp(x[4]),x[7]],[0.,0.,np.exp(-x[3]-x[4])]])
  Xi=(Y-g)@A.T
  normals=self.Q+w;heights=1-normals@g;assert np.min(heights)>0
  pol=(normals/heights[:,None])@np.linalg.inv(A)
  def exits(points,edges):
   p=points[edges[:,0]];d=points[edges[:,1]]-p
   values=np.einsum('ij,ij->i',p,d)/np.sqrt(np.einsum('ij,ij->i',p,p)*np.einsum('ij,ij->i',d,d))
   result=np.full(len(points),-np.inf);np.maximum.at(result,edges[:,0],values)
   return result
  pu=exits(Xi,self.edges);ps=exits(pol,self.dedges)
  return pu,ps,w,A,g,D/6
 def residual(self,x,root_mode):
  pu,ps,*_=self.evaluate(x);ru=np.minimum(pu-MARGIN,0);rs=np.minimum(ps-MARGIN,0)
  ur=int(np.argmin(pu)) if root_mode==-1 else root_mode
  ru[ur]=0;rs[int(np.argmin(ps))]=0
  return np.concatenate([ru,rs])
 def record(self,x,mode):
  pu,ps,w,A,g,volume=self.evaluate(x)
  return dict(parameters=list(map(float,x)),projective_w=list(map(float,w)),linear_A=A.tolist(),projected_filled_centroid=g.tolist(),projected_volume=float(volume),root_mode=mode,S=np.flatnonzero(ps<0).tolist(),U=np.flatnonzero(pu<0).tolist(),primal_second=float(np.sort(pu)[1]),polar_second=float(np.sort(ps)[1]),cost=float(np.sum(self.residual(x,mode)**2)),near_zero_vertex_indices=np.flatnonzero(np.abs(pu)<1e-10).tolist(),near_zero_face_indices=np.flatnonzero(np.abs(ps)<1e-10).tolist(),minimum_projective_denominator=float(np.min(1+self.P@w)))
def main(src,out):
 m=Model(src);rng=np.random.default_rng(SEED);records=[]
 base=m.record(np.zeros(8),-1);assert base['S']==m.raw['stable_face_ids'] and base['U']==m.raw['unstable_vertices']
 print('BASE',len(base['S']),len(base['U']),base['cost'],flush=True)
 bounds=([-6]*3+[-1.5]*2+[-2]*3,[6]*3+[1.5]*2+[2]*3)
 best=np.zeros(8)
 for k in range(NSTARTS):
  mode=[-1,79,117][k%3]
  if k<3:x=np.zeros(8)
  elif k<9:x=np.r_[rng.normal(0,.45,3),rng.normal(0,.12,2),rng.normal(0,.12,3)]
  else:x=best+rng.normal(0,.18,8)
  x=np.clip(x,np.array(bounds[0])+1e-6,np.array(bounds[1])-1e-6)
  ans=least_squares(lambda v:m.residual(v,mode),x,bounds=bounds,jac='3-point',max_nfev=MAX_NFEV,ftol=1e-12,xtol=1e-12,gtol=1e-12,diff_step=1e-5)
  rec=m.record(ans.x,mode);rec.update(start=k,initial_parameters=list(map(float,x)),nfev=int(ans.nfev),status=int(ans.status),message=str(ans.message));records.append(rec)
  if rec['cost']<=min(r['cost'] for r in records):best=ans.x.copy()
  report=dict(status='NUMERICAL_PROPOSALS_ONLY',source_sha256=EXPECTED,seed=SEED,nstarts_requested=NSTARTS,max_nfev=MAX_NFEV,margin=MARGIN,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),baseline=base,results=records)
  out.write_bytes(B(report));print('TRIAL',k,'S/U',len(rec['S']),len(rec['U']),'cost',rec['cost'],'nfev',rec['nfev'],'second',rec['primal_second'],rec['polar_second'],flush=True)
  if len(rec['S'])==1 and len(rec['U'])==1 and min(rec['primal_second'],rec['polar_second'])>0:print('NUMERICAL_OWN110_PROPOSAL_NEEDS_EXACT_GATE',flush=True);break
 print('C486_PROJECTIVE_METRIC_SCREEN_TERMINAL',len(records),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
