"""Root-reaching whole-complex numerical repair. Finite search, not a proof."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,sys,time
from pathlib import Path
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from orbit_search import Orbit

class Forest(Orbit):
 def data(self,z):
  P,Y,JP,JY,info=self.geometry(z);al=[]
  for X,J,(src,dst),n in zip((P,Y),(JP,JY),self.edges,self.n):
   a=X[src];e=X[dst]-a;na=np.linalg.norm(a,axis=1);ne=np.linalg.norm(e,axis=1);v=np.einsum('ij,ij->i',a,e)/(na*ne)
   va=e/(na*ne)[:,None]-v[:,None]*a/na[:,None]**2
   ve=a/(na*ne)[:,None]-v[:,None]*e/ne[:,None]**2
   dv=np.einsum('ni,nik->nk',va,J[src])+np.einsum('ni,nik->nk',ve,J[dst]-J[src])
   r=int(np.argmax(np.einsum('ij,ij->i',X,X)));al.append((v,dv,r))
  return al,info
 def choose(self,z,power):
  data,info=self.data(z);choice=[]
  for (v,dv,root),(src,dst),n in zip(data,self.edges,self.n):
   weights=np.maximum(1e-5-v,0)**power+1e-10
   graph=csr_matrix((weights,(dst,src)),shape=(n,n))
   ds,prev=dijkstra(graph,directed=True,indices=root,return_predecessors=True)
   assert np.isfinite(ds).all()
   ids=[]
   for i in range(n):
    if i==root:continue
    j=int(prev[i]);ids.append(int(np.flatnonzero((src==i)&(dst==j))[0]))
   choice.append(np.array(ids,int))
  return choice
 def fixed(self,z,ids):
  data,info=self.data(z);v=np.concatenate([a[0][k] for a,k in zip(data,ids)]);J=np.concatenate([a[1][k] for a,k in zip(data,ids)])
  r=np.minimum(v-1e-5,0);return r,J*(v<1e-5)[:,None]

def main():
 import argparse
 pa=argparse.ArgumentParser();pa.add_argument('report');pa.add_argument('out');pa.add_argument('--seed',type=int,default=720625);pa.add_argument('--starts',type=int,default=80);pa.add_argument('--outer',type=int,default=12);args=pa.parse_args();out=Path(args.out);out.mkdir(exist_ok=False);m=Forest(args.report);rng=np.random.default_rng(args.seed);low=np.array([-40,-40,-40,-1.6,-1.6,-3,-3,-3]);high=-low;best=None;clock=time.monotonic();done=0
 for k in range(args.starts):
  if k==0:z=np.zeros(8)
  elif k%4==0 and best is not None:z=np.clip(best[1]+rng.normal(size=8)*.2,low+.001,high-.001)
  else:z=np.clip(np.r_[rng.normal(size=3)*10**rng.uniform(-2,1.5),rng.uniform(-1,1,2),rng.normal(size=3)],low+.001,high-.001)
  for outer in range(args.outer):
   ids=m.choose(z,1+(k%2));cache=[None,None]
   def get(x):
    if cache[0] is None or not np.array_equal(cache[0],x):cache[0]=x.copy();cache[1]=m.fixed(x,ids)
    return cache[1]
   sol=least_squares(lambda x:get(x)[0],z,jac=lambda x:get(x)[1],bounds=(low,high),max_nfev=100,ftol=1e-10,xtol=1e-11,gtol=1e-11);z=sol.x
   v,j,info=m.evaluate(z);score=(len(info['S'])+len(info['U']),float(np.maximum(-v,0).sum()));info.update(start=k,outer=outer,score=list(score))
   with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(info)+'\n')
   if best is None or score<best[0]:best=(score,z.copy());(out/'BEST.json').write_text(json.dumps(info,sort_keys=True));print('BEST',k,outer,score,info['condition'],flush=True)
   if score[0]==2 and info['min_nonroot']>1e-8:
    (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));break
   if outer and np.linalg.norm(z-previous)<1e-8:break
   previous=z.copy()
  done+=1
  if best[0][0]==2:break
  if k%10==0:print('STEP',k,time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(args),sort_keys=True));print('FINITE_ROOTED_FOREST_PROJECTIVE_METRIC_SEARCH_FINISHED',done,flush=True)
if __name__=='__main__':main()
