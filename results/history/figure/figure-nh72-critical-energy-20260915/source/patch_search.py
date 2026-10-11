"""Actual-critical-geometry discovery; all printed own counts use filled mass.
Modes ref: six critical controls at original centre (diagnostic only).
own: critical plus physical caps, with each actual own centroid.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time,heapq
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from patch_model import Patch

def route(n,src,dst,v,root):
 rev=[[] for _ in range(n)]
 for k,(i,j) in enumerate(zip(src,dst)):rev[j].append((int(i),k))
 dist=np.full(n,np.inf);dist[root]=0;par=np.full(n,-1,int);done=set();q=[(0,root)]
 while q:
  d,j=heapq.heappop(q)
  if j in done:continue
  done.add(j)
  for i,k in rev[j]:
   if i in done:continue
   cost=1e-10+max(-v[k],0)**2
   if d+cost<dist[i]:dist[i]=d+cost;par[i]=k;heapq.heappush(q,(dist[i],i))
 assert len(done)==n
 return par[np.arange(n)!=root]

def main(mode,starts,out):
 m=Patch(Path(os.environ['NH72_BASE_REPORT']));out=Path(out);out.mkdir(exist_ok=False);rng=np.random.default_rng(141417);clock=time.monotonic();allrows=[];best=None;bestloss=np.inf
 ref=mode=='ref';n=6 if ref else (17 if mode=='metric' else 12)
 zbase=np.zeros(n)
 if not ref:zbase[[8,9,10]]=[-.2508314428450225,.02424207684755533,.00857532527947764]
 def pad(z):return np.r_[z,np.zeros(6)] if ref else z
 lo=np.r_[[-2,-2,-1,-1,-1,-1],np.full(n-6,-.85)];hi=np.r_[np.full(6,2.),np.full(n-6,3.)]
 if n==17:lo[12:]=[-1,-1,-3,-3,-3];hi[12:]=[1,1,3,3,3]
 gscale=100.;length=m.mesh.n+m.mesh.nf-2+(~m.mesh.inc).sum()+13+n-6
 for start in range(starts):
  zz=zbase.copy() if start==0 else (best.copy() if best is not None and start%2 else zbase.copy())+rng.normal(size=n)*10**rng.uniform(-3,-.45)
  zz=np.clip(zz,lo+1e-9,hi-1e-9)
  # Keep one physically meaningful exit from critical124 to outside its old basin.
  for outer in range(4):
   pv,dv,*_=m.calc(pad(zz),ref)
   if start==0 and outer==0:
    trial=pv.copy();trial[(m.src==m.ix[124])&(m.dst==m.ix[146])]=.0001
    pi=route(m.mesh.n,m.src,m.dst,trial,m.rU)
   else:pi=route(m.mesh.n,m.src,m.dst,pv,m.rU)
   di=route(m.mesh.nf,m.fs,m.fd,dv,m.rS)
   def vals(z):
    v,w,g,gap,den,_=m.calc(pad(z),ref)
    return np.r_[v[pi]-1e-7,w[di]-1e-7,gscale*(gap[~m.mesh.inc]-1e-8),gscale*(den-.01),gscale*(1+pad(z)[6:12]-.01)]
   def fun(z):return np.minimum(vals(z),0)
   def jac(z):
    v=vals(z);J=np.empty((len(v),n));cx=z.astype(complex)
    for k in range(n):
     xx=cx.copy();xx[k]+=1j*1e-27;J[:,k]=vals(xx).imag/1e-27
    J[v>=0]=0
    return J
   sol=least_squares(fun,zz,jac=jac,bounds=(lo,hi),max_nfev=250,ftol=1e-11,xtol=1e-12,gtol=1e-12)
   zz=sol.x;r=m.brief(pad(zz));P,_=m.points(pad(zz));refstate=m.mesh.brief(m.mesh.state(P,m.c));r['reference_counts']=refstate['counts'];r['reference_U']=[m.keep[i] for i in refstate['U']];r['reference_S']=[m.labels[i] for i in refstate['S']];r.update(start=start,outer=outer,mode=mode,nfev=sol.nfev,loss=float(np.linalg.norm(sol.fun)))
   valid=r['min_gap']>0 and r['planarity']<1e-8 and r['min_den']>0
   if valid and r['loss']<bestloss:
    bestloss=r['loss'];best=zz.copy();(out/'BEST.json').write_text(json.dumps(r,sort_keys=True));print('BEST',mode,start,outer,r['counts'],r['reference_counts'],r['loss'],r['min_gap'],r['z'],flush=True)
   allrows.append(r);(out/'ALL.json').write_text(json.dumps(allrows,sort_keys=True))
   if valid and (refstate['counts'] if ref else r['counts'])==[1,1,0]:print('NUMERICAL110',mode,flush=True);return
   if sol.nfev<5:break
  print('START_DONE',mode,start,'seconds',time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(dict(mode=mode,starts=starts,seed=141417,max_nfev=250,outer=4)))
 print('FINITE_PATCH_SEARCH_DONE',mode,len(allrows),flush=True)
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),sys.argv[3])
