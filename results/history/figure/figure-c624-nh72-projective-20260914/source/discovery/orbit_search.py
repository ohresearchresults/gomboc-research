"""Numerical finite projective/physical-metric search. Not an exact certificate."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,time,hashlib
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import least_squares
sys.set_int_max_str_digits(0)

def f(x): return float(Fraction(x))
def pairs(faces):
 d={}
 for k,cy in enumerate(faces):
  for a,b in zip(cy,cy[1:]+cy[:1]):d.setdefault(tuple(sorted((a,b))),[]).append(k)
 assert all(len(v)==2 for v in d.values())
 e=np.array(sorted(d),int);dual=np.array([d[tuple(v)] for v in e],int)
 return e,dual
class Orbit:
 def __init__(self,report):
  r=json.loads(Path(report).read_text());assert (r['V'],r['E'],r['F'])==(177,312,137)
  self.X=np.array([[f(v) for v in x] for x in r['raw_vertices']]);self.q=np.array([[n/h for n in nn] for nn,h in zip(r['normals'],r['offsets'])])
  self.tri=np.array([(cy[0],cy[j],cy[j+1]) for cy in r['faces'] for j in range(1,len(cy)-1)])
  self.ep,self.ed=pairs(r['faces']);self.edges=[]
  for e in (self.ep,self.ed):self.edges.append((np.r_[e[:,0],e[:,1]],np.r_[e[:,1],e[:,0]]))
  self.n=[len(self.X),len(self.q)];self.last=None;self.calls=0
 def geometry(self,z):
  # Onto chart z -> t of the full admissible projective domain (no finite cutoff here).
  v=z[:3];dots=-self.X@v;k=int(np.argmax(dots));h=dots[k];d=1+h;t=v/d
  Dt=np.eye(3)/d+np.outer(v,self.X[k])/d**2
  den=1+self.X@t;assert den.min()>0
  y=self.X/den[:,None];tr=y[self.tri];w=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));W=w.sum();assert w.min()>0
  ss=tr.sum(axis=1);g=np.sum(w[:,None]*ss,axis=0)/(4*W)
  m2=(np.einsum('i,ij,ik->jk',w,ss,ss)+np.einsum('i,iaj,iak->jk',w,tr,tr))/(20*W)
  dg=-5*m2+4*np.outer(g,g)
  p=y-g;dp=(-np.einsum('ni,nj->nij',y,y)-dg[None,:,:])@Dt
  b=self.q+t;hh=1-b@g;assert hh.min()>0
  pole=b/hh[:,None];dh=-g[None,:]-b@dg
  dpol=(np.eye(3)[None,:,:]/hh[:,None,None]-b[:,:,None]*dh[:,None,:]/hh[:,None,None]**2)@Dt
  a,c=z[3:5];ex=np.exp([a,c,-a-c]);U=np.eye(3);U[0,1]=z[5];U[0,2]=z[6];U[1,2]=z[7];A=ex[:,None]*U;B=np.linalg.inv(A).T
  DA=np.zeros((5,3,3));DA[0]=np.diag([1,0,-1])@A;DA[1]=np.diag([0,1,-1])@A;DA[2,0,1]=ex[0];DA[3,0,2]=ex[0];DA[4,1,2]=ex[1]
  DB=np.array([-B@da.T@B for da in DA])
  P=p@A.T;Y=pole@B.T
  JP=np.concatenate((np.einsum('ij,njk->nik',A,dp),np.einsum('kij,nj->nik',DA,p)),axis=2)
  JY=np.concatenate((np.einsum('ij,njk->nik',B,dpol),np.einsum('kij,nj->nik',DB,pole)),axis=2)
  return P,Y,JP,JY,dict(t=t.tolist(),A=A.tolist(),volume=W/6,centroid_projective=g.tolist(),centroid=(A@g).tolist(),min_den=float(den.min()),condition=float(np.linalg.cond(A)))
 def evaluate(self,z):
  z=np.asarray(z,float)
  if self.last is not None and np.array_equal(z,self.last[0]):return self.last[1]
  P,Y,JP,JY,info=self.geometry(z);phi=[];jac=[];roots=[];maxes=[]
  for X,J,(src,dst),n in zip((P,Y),(JP,JY),self.edges,self.n):
   e=X[dst]-X[src];a=X[src];na=np.linalg.norm(a,axis=1);ne=np.linalg.norm(e,axis=1);assert ne.min()>0
   v=np.einsum('ij,ij->i',a,e)/(na*ne)
   va=e/(na*ne)[:,None]-v[:,None]*a/(na**2)[:,None]
   ve=a/(na*ne)[:,None]-v[:,None]*e/(ne**2)[:,None]
   dv=np.einsum('ni,nik->nk',va,J[src])+np.einsum('ni,nik->nk',ve,J[dst]-J[src])
   # Lexicographic max tie-break is stable; true graph rather than virtual corners.
   idx=np.zeros(n,int);best=np.full(n,-np.inf)
   for k in range(len(src)):
    i=src[k]
    if v[k]>best[i]:best[i]=v[k];idx[i]=k
   root=int(np.argmax(np.einsum('ij,ij->i',X,X)));roots.append(root);maxes.append(best.copy());best[root]=1.
   jj=dv[idx].copy();jj[root]=0
   phi.append(best);jac.append(jj)
  info.update(U=np.where(maxes[0]<0)[0].tolist(),S=np.where(maxes[1]<0)[0].tolist(),roots=roots,z=z.tolist(),min_nonroot=float(min(v.min() for v in phi)))
  ret=(np.r_[*phi],np.concatenate(jac),info);self.last=(z.copy(),ret);self.calls+=1;return ret
 def residual(self,z,target=1e-5):
  v,j,info=self.evaluate(z);return np.minimum(v-target,0.)
 def jacobian(self,z,target=1e-5):
  v,j,info=self.evaluate(z);return j*(v<target)[:,None]

def main():
 import argparse
 pa=argparse.ArgumentParser();pa.add_argument('report');pa.add_argument('out');pa.add_argument('--starts',type=int,default=200);pa.add_argument('--seed',type=int,default=720624);pa.add_argument('--evals',type=int,default=1200);args=pa.parse_args()
 out=Path(args.out);out.mkdir(exist_ok=False);model=Orbit(args.report);rng=np.random.default_rng(args.seed)
 zero=np.zeros(8);v,j,info=model.evaluate(zero);print('BASE',json.dumps(info),flush=True)
 # Central difference check of all current selected witness derivatives away from walls.
 zz=np.array([.13,-.24,.09,.2,-.15,.06,-.1,.2]);vv,jj,_=model.evaluate(zz);num=[]
 for k in range(8):
  e=np.eye(8)[k]*1e-6;num.append((model.evaluate(zz+e)[0]-model.evaluate(zz-e)[0])/2e-6)
 err=np.max(np.abs(np.array(num).T-jj));assert err<1e-6,err
 print('ANALYTIC_DERIVATIVE_CHECK',err,flush=True)
 low=np.array([-50,-50,-50,-2.3,-2.3,-4,-4,-4]);high=-low
 best=None;rows=[];start=time.monotonic()
 for k in range(args.starts):
  if k==0:z=np.zeros(8)
  elif k%5==0 and best is not None:z=np.clip(best[1]+rng.normal(size=8)*(.05 if k%10==0 else .5),low+.001,high-.001)
  else:
   z=np.r_[rng.normal(size=3)*10**rng.uniform(-1.5,1.5),rng.uniform(-1.5,1.5,2),rng.normal(size=3)]
   z=np.clip(z,low+.001,high-.001)
  sol=least_squares(model.residual,z,jac=model.jacobian,bounds=(low,high),max_nfev=args.evals,ftol=1e-11,xtol=1e-12,gtol=1e-11)
  v,j,info=model.evaluate(sol.x);score=float(np.sum(np.minimum(v-1e-5,0.)**2));info.update(score=score,nfev=int(sol.nfev),start=k)
  rows.append(info);(out/'ALL.jsonl').open('a').write(json.dumps(info)+'\n')
  key=(len(info['U'])+len(info['S']),score)
  if best is None or key<best[0]:
   best=(key,sol.x.copy());(out/'BEST.json').write_text(json.dumps(info,sort_keys=True));print('BEST',k,key,info['min_nonroot'],info['condition'],info['min_den'],flush=True)
  if len(info['U'])==1 and len(info['S'])==1 and info['min_nonroot']>1e-8:
   (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));print('NUMERICAL_ONLY_110',k,flush=True);break
  if k%10==0:print('STEP',k,'time',time.monotonic()-start,'calls',model.calls,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(args),sort_keys=True));print('FINITE_PROJECTIVE_METRIC_SEARCH_FINISHED',len(rows),flush=True)
if __name__=='__main__':main()
