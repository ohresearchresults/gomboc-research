"""Projective/metric root turnover on the exact C476 untransformed frame.
Usage OPENBLAS_NUM_THREADS=1 python metric476_screen.py BEFORE_A OUT
Imports the preserved generic C486 physical-mass evaluator and exact affine controls.
"""
import hashlib,json,os,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np,scipy
from scipy.optimize import least_squares
import projective_metric_screen as old
import REPLAY_AFFINE334 as aff
assert __debug__;sys.set_int_max_str_digits(0)
EXPECTED='9918f3cb6a779b46c3817cc8fdbb5d36a8e12e242f2e98f33c747e99bdfe2681'
SEED=2026091503;STARTS=24;MAX_NFEV=1200
B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':')).encode()
class Model(old.Model):
 def __init__(self,path):
  b=path.read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED;r=json.loads(b);self.raw=r
  self.P=np.array([[float(F(s)) for s in p] for p in r['raw_vertices']]);self.Q=np.array([[float(F(x,h)) for x in n] for n,h in zip(r['normals'],r['offsets'])])
  e=np.array(r['edges']);self.edges=np.concatenate([e,e[:,::-1]]);tri=[];inc={tuple(e):[] for e in r['edges']}
  for k,f in enumerate(r['faces']):
   tri.extend([[f[0],f[j],f[j+1]] for j in range(1,len(f)-1)])
   for i,j in zip(f,f[1:]+f[:1]):inc[tuple(sorted((i,j)))].append(k)
  de=np.array([v for _,v in sorted(inc.items())]);assert de.shape==(238,2)
  self.tri=np.array(tri);self.dedges=np.concatenate([de,de[:,::-1]])
  self.primary=next(i for i,p in enumerate(r['raw_vertices']) if list(map(F,p))==[F(0),F(0),F(1)])
 def initial(self):
  w=np.array(aff.W)/aff.D;m=max(0.,float(max(-self.P@w)));z=w/(1-m)
  a=np.array(aff.AA)/aff.D;a/=np.cbrt(np.linalg.det(a))
  return np.r_[z,np.log(a[0,0]),np.log(a[1,1]),a[0,1],a[0,2],a[1,2]]
def main(src,out):
 m=Model(src);base=m.initial();baseline=m.record(base,-1);assert(len(baseline['S']),len(baseline['U']))==(2,2)
 other=next(i for i in baseline['U'] if i!=m.primary);print('BASE_C476',baseline,'roots',m.primary,other,flush=True)
 rng=np.random.default_rng(SEED);bounds=(np.array([-12]*3+[-3]*2+[-6]*3),np.array([12]*3+[3]*2+[6]*3));best=base;rows=[]
 for k in range(STARTS):
  mode=[-1,m.primary,other][k%3]
  if k<3:x=base.copy()
  elif k<9:x=base+rng.normal(0,.12,8)
  elif k<15:x=base+rng.normal(0,.5,8)
  else:x=best+rng.normal(0,.22,8)
  x=np.clip(x,bounds[0]+1e-6,bounds[1]-1e-6)
  sol=least_squares(lambda z:m.residual(z,mode),x,bounds=bounds,jac='3-point',diff_step=1e-5,max_nfev=MAX_NFEV,ftol=1e-12,xtol=1e-12,gtol=1e-12)
  r=m.record(sol.x,mode);r.update(start=k,initial_parameters=x.tolist(),nfev=int(sol.nfev),status=int(sol.status),message=str(sol.message));rows.append(r)
  if r['cost']<=min(q['cost'] for q in rows):best=sol.x.copy()
  out.write_bytes(B(dict(status='NUMERICAL_C476_METRIC_PROPOSALS_ONLY',input_sha256=EXPECTED,seed=SEED,starts_requested=STARTS,max_nfev=MAX_NFEV,numpy=np.__version__,scipy=scipy.__version__,openblas_threads=os.environ.get('OPENBLAS_NUM_THREADS'),baseline=baseline,results=rows)))
  print('C476_PM',k,'S/U',len(r['S']),len(r['U']),'cost',r['cost'],'second',r['primal_second'],r['polar_second'],flush=True)
  if len(r['S'])==len(r['U'])==1 and min(r['primal_second'],r['polar_second'])>1e-10:print('C476_NUMERICAL110_NEEDS_EXACT_HULL_GATE',flush=True);break
 print('C476_METRIC_SCREEN_TERMINAL',len(rows),hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
