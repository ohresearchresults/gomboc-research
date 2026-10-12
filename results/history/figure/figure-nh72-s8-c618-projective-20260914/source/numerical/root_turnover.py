"""Whole-complex max-min rooted forests with explicit alternative critical carriers."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,time,heapq,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from centroid_metric import CentroidOrbit
from isotropic_metric import IsotropicOrbit

def widest(m,z,roots):
 data=m.all_data(z)[3];choices=[];levels=[]
 for (v,J,_),(src,dst),n,r in zip(data,m.edges,m.ns,roots):
  incoming=[[] for i in range(n)]
  for k,j in enumerate(dst):incoming[j].append(k)
  quality=np.full(n,-np.inf);quality[r]=np.inf;parent=np.full(n,-1,int);seen=set();heap=[(-np.inf,r)]
  while heap:
   neg,j=heapq.heappop(heap)
   if j in seen:continue
   seen.add(j)
   for k in incoming[j]:
    i=src[k];val=min(quality[j],v[k])
    if i not in seen and val>quality[i]:quality[i]=val;parent[i]=k;heapq.heappush(heap,(-val,int(i)))
  assert len(seen)==n and all(parent[i]>=0 for i in range(n) if i!=r)
  choices.append(np.array([parent[i] for i in range(n) if i!=r]));levels.append(float(np.min(quality)))
 return choices,levels

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--starts',type=int,default=100);p.add_argument('--outer',type=int,default=12);p.add_argument('--evals',type=int,default=80);p.add_argument('--seed',type=int,default=720621);p.add_argument('--chart',choices=['raw','isotropic'],default='raw');p.add_argument('--sigma',type=float,default=.03);a=p.parse_args()
 out=Path(a.out);out.mkdir(exist_ok=False);m=(CentroidOrbit if a.chart=='raw' else IsotropicOrbit)(a.report);rng=np.random.default_rng(a.seed)
 z0=np.r_[m.b0,np.zeros(5)]
 if a.chart=='isotropic':
  _,g,K,_,_=m.state(np.zeros(3));L=np.linalg.cholesky((K-np.outer(g,g))/5);Q,R=np.linalg.qr(L);R=np.diag(np.sign(np.diag(R)))@R;R/=np.linalg.det(L)**(1/3)
  z0[3:]=[np.log(R[0,0]),np.log(R[1,1]),R[0,1]/R[0,0],R[0,2]/R[0,0],R[1,2]/R[1,1]]
 low=np.r_[[-30]*3,[-2]*2,[-4]*3];high=-low;clock=time.monotonic();best={};fail=0;baseline=m.all_data(z0)[2]
 def record(z,k,outer,roots):
  v,J,info,data=m.all_data(z);cnt=(len(info['S']),len(info['U']));score=float(np.minimum(v-1e-5,0)@np.minimum(v-1e-5,0));key=f'S{cnt[0]}U{cnt[1]}'
  info.update(start=k,outer=outer,chosen_roots=list(map(int,roots)),loss=score)
  with (out/'ALL.jsonl').open('a') as f:f.write(json.dumps(info,sort_keys=True)+'\n')
  if sum(cnt)<=6 and info['condition']<100 and (key not in best or score<best[key]):
   best[key]=score;(out/(key+'.json')).write_text(json.dumps(info,sort_keys=True));print('BEST',k,outer,cnt,score,roots,info['min_den'],info['condition'],flush=True)
  if cnt==(1,1) and info['min_nonroot']>1e-8:
   (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));return True
  return False
 for k in range(a.starts):
  if k<len(baseline['U']):roots=[baseline['U'][k],baseline['S'][0]];z=z0.copy()
  else:
   z=np.clip(z0+np.r_[rng.normal(size=3)*10**rng.uniform(-3,1),rng.normal(size=5)*rng.uniform(.1,1.2)],low+.001,high-.001)
   try:
    info=m.all_data(z)[2]
   except ArithmeticError:fail+=1;continue
   roots=[int(rng.choice(info['U'])),int(rng.choice(info['S']))]
   if k%5==0:roots=[int(rng.integers(m.ns[0])),int(rng.integers(m.ns[1]))]
  try:
   for outer in range(a.outer):
    ids,levels=widest(m,z,roots)
    rid=[np.flatnonzero(src==r) for (src,dst),r in zip(m.edges,roots)]
    def evaluate(x):
     data=m.all_data(x)[3];v=np.concatenate([d[0][sel] for d,sel in zip(data,ids)]+[-d[0][sel] for d,sel in zip(data,rid)])
     J=np.concatenate([d[1][sel] for d,sel in zip(data,ids)]+[-d[1][sel] for d,sel in zip(data,rid)])
     return np.minimum(v-1e-5,0),J*(v<1e-5)[:,None]
    sol=least_squares(lambda x:evaluate(x)[0],z,jac=lambda x:evaluate(x)[1],bounds=(low,high),loss='soft_l1',f_scale=a.sigma,max_nfev=a.evals,ftol=1e-11,xtol=1e-11,gtol=1e-11)
    step=np.linalg.norm(z-sol.x);z=sol.x
    if record(z,k,outer,roots):break
    if outer>1 and step<1e-8:break
  except (ArithmeticError,ValueError,np.linalg.LinAlgError) as ex:
   fail+=1;m.last_t=np.zeros(3);m.last=None
   with (out/'FAILURES.txt').open('a') as f:f.write(str(k)+' '+repr(ex)+'\n')
  if (out/'NUMERICAL_WINNER.json').exists():break
  if k%10==0:print('STEP',k,'seconds',time.monotonic()-clock,'failures',fail,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True));(out/'SUMMARY.json').write_text(json.dumps(dict(starts=k+1,failures=fail,calls=m.calls,newton=m.newton_calls,seconds=time.monotonic()-clock),sort_keys=True))
 print('FINITE_ALTERNATIVE_ROOT_MAXMIN_FOREST_FINISHED',k+1,fail,flush=True)
if __name__=='__main__':main()
