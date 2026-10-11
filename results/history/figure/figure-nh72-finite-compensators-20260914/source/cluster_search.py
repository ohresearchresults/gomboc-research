"""Finite whole-complex search after multivertex removal with two physical caps.
A rooted widest-path forest, never a local-argmax cycle, supplies each trial merit.
All samples recompute the filled-volume centroid. Only an exact later audit can win.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import sys,json,heapq,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from cluster import Cluster

def forest(n,src,dst,val,root):
 rev=[[] for _ in range(n)]
 for e,(i,j) in enumerate(zip(src,dst)):rev[j].append((int(i),e))
 cap=np.full(n,-np.inf);cap[root]=np.inf;par=np.full(n,-1,int);done=set();pq=[(-np.inf,root)]
 while pq:
  neg,j=heapq.heappop(pq)
  if j in done:continue
  done.add(j)
  for i,e in rev[j]:
   if i in done:continue
   v=min(cap[j],val[e])
   if v>cap[i]:cap[i]=v;par[i]=e;heapq.heappush(pq,(-v,i))
 assert len(done)==n
 for i in range(n):
  q=i;seen=set()
  while q!=root:
   assert q not in seen;seen.add(q);q=int(dst[par[q]])
 return par[[i for i in range(n) if i!=root]]

def main(report,j,remove,starts,output):
 m=Cluster(report,j,remove);clock=time.monotonic();rng=np.random.default_rng(140927+j);out=Path(output);out.mkdir(exist_ok=False);closed=m.close();start=np.r_[closed['eta'],np.zeros(5)];records=[];calls=0;best=(1e9,None);meritbest=(1e9,None)
 def state(z):
  P,d=m.points(z[:6]);a,b,c,e,f=z[6:];A=np.array([[np.exp(a),c,e],[0,np.exp(b),f],[0,0,np.exp(-a-b)]]);P=P@A.T;st=m.mesh.state(P);st['min_den']=float(d.min());st['z']=z;st['A']=A;return st
 def residual(z):
  nonlocal calls
  calls+=1
  try:
   st=state(z);P,d=m.points(z[:6]);P=P@st['A'].T;c=np.array(st['centroid']);X=P-c;tt=X[m.mesh.ft];N=np.cross(tt[:,1]-tt[:,0],tt[:,2]-tt[:,0]);h=np.einsum('ij,ij->i',N,tt[:,0]);Y=N/h[:,None]
   ru=int(np.argmax((X*X).sum(axis=1)));rs=int(np.argmax((Y*Y).sum(axis=1)));pi=forest(len(X),m.mesh.src,m.mesh.dst,st['pv'],ru);di=forest(len(Y),m.mesh.fs,m.mesh.fd,st['dv'],rs)
   v=np.r_[st['pv'][pi],st['dv'][di]]
   return np.r_[np.minimum(v-1e-6,0),30*min(st['min_gap']-1e-8,0),10*min(st['min_offset']-.001,0),30*min(st['min_den']-.01,0)]
  except (ValueError,np.linalg.LinAlgError,AssertionError,FloatingPointError):return np.full(m.mesh.n+m.mesh.nf+1,1e3)
 for k in range(starts):
  z=start.copy() if k==0 else (meritbest[1] if k%3 and meritbest[1] is not None else start.copy())+rng.normal(size=11)*10**rng.uniform(-3,-.4)
  lo=np.r_[np.full(6,-.85),[-.9,-.9,-2,-2,-2]];hi=np.r_[np.full(6,3),[.9,.9,2,2,2]];z=np.clip(z,lo+1e-7,hi-1e-7)
  sol=least_squares(residual,z,bounds=(lo,hi),max_nfev=150,ftol=1e-8,xtol=1e-9,gtol=1e-9,diff_step=2e-6)
  s=state(sol.x);r=m.mesh.brief(s);r['z']=sol.x.tolist();r['A']=s['A'].tolist();r['loss']=float(np.linalg.norm(residual(sol.x)));r.update(start=k,nfev=sol.nfev,calls=calls);records.append(r);(out/'ALL.json').write_text(json.dumps(records,sort_keys=True))
  valid=r['min_gap']>1e-10 and r['min_offset']>0 and r['min_den']>0 and r['planarity']<1e-8 and r['counts'][0]+r['counts'][1]-r['counts'][2]==2
  if valid and r['loss']<meritbest[0]:meritbest=(r['loss'],sol.x.copy())
  key=sum(r['counts'])+min(r['loss'],.9)
  if valid and key<best[0]:best=(key,sol.x.copy());(out/'BEST.json').write_text(json.dumps(r,sort_keys=True));print('NEW_BEST',j,remove,k,r['counts'],r['loss'],'gap',r['min_gap'],'secs',time.monotonic()-clock,flush=True)
  if valid and r['counts']==[1,1,0] and r['loss']<1e-10:print('NUMERICAL110_EXACT_CHECK_REQUIRED',flush=True);break
  print('FINISHED_START',k,r['counts'],r['loss'],'valid',valid,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(dict(j=j,remove=remove,starts=starts,seed=140927+j,max_nfev=150),sort_keys=True));print('FINITE_TWO_CAP_CLUSTER_SEARCH_FINISHED',j,len(records),calls,flush=True)
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),list(map(int,sys.argv[3].split(','))),int(sys.argv[4]),sys.argv[5])
