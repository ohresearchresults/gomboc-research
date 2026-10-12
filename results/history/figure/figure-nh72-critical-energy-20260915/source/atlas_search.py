"""Finite search in enlarged critical-support chart. Strict final exact audit separate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time,heapq
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from atlas_model import Atlas

def route(n,src,dst,v,root):
 rev=[[] for _ in range(n)]
 for k,(i,j) in enumerate(zip(src,dst)):rev[j].append((int(i),k))
 dist=np.full(n,np.inf);dist[root]=0.;par=np.full(n,-1,int);done=set();q=[(0.,root)]
 while q:
  d,j=heapq.heappop(q)
  if j in done:continue
  done.add(j)
  for i,k in rev[j]:
   if i in done:continue
   cost=1e-9 if v[k]>0 else 1.+abs(v[k])
   if d+cost<dist[i]:dist[i]=d+cost;par[i]=k;heapq.heappush(q,(dist[i],i))
 assert len(done)==n
 return par[np.arange(n)!=root]

def main(mode,starts,output):
 m=Atlas(Path(os.environ['NH72_BASE_REPORT']));ref=mode=='ref';n=12 if ref else 18
 out=Path(output);out.mkdir(exist_ok=False);rng=np.random.default_rng(141418);clock=time.monotonic();rows=[];best=None;bestloss=np.inf
 def full(z):return np.r_[z,np.zeros(6)] if ref else z
 lo=np.r_[np.full(12,-20.),np.full(n-12,-.9)];hi=np.r_[np.full(12,20.),np.full(n-12,4.)]
 base=np.zeros(n)
 if not ref:base[[14,15,16]]=[-.2508314428450225,.02424207684755533,.00857532527947764]
 for it in range(starts):
  z=base.copy() if it==0 else (best.copy() if best is not None and it%3 else base.copy())+rng.normal(size=n)*10**rng.uniform(-3,0)
  z=np.clip(z,lo+1e-9,hi-1e-9)
  for outer in range(6):
   pv,dv,*_=m.calc(full(z),ref)
   pi=route(m.mesh.n,m.src,m.dst,pv,m.rU);di=route(m.mesh.nf,m.fs,m.fd,dv,m.rS)
   def values(z):
    pv,dv,g,gap,den,vol=m.calc(full(z),ref)
    mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1)
    return np.r_[pv[pi]-1e-7,dv[di]-1e-7,100*(gap[np.arange(m.mesh.nf),j]-1e-8),100*(den-.01),100*(1+full(z)[12:18]-.01),100*np.minimum(vol.real,0)]
   def fun(z):return np.minimum(values(z),0)
   def jac(z):
    v=values(z);a=np.empty((len(v),n));c=z.astype(complex)
    for j in range(n):
     zz=c.copy();zz[j]+=1e-26j;a[:,j]=values(zz).imag/1e-26
    a[v>=0]=0;return a
   try:sol=least_squares(fun,z,jac=jac,bounds=(lo,hi),max_nfev=240,x_scale='jac',ftol=1e-11,xtol=1e-12,gtol=1e-12)
   except (ValueError,np.linalg.LinAlgError):break
   z=sol.x;s=m.brief(full(z));P,_=m.points(full(z));rs=m.mesh.state(P,m.c);s.update(reference_counts=rs['counts'],reference_U=[m.keep[i] for i in rs['U']],reference_S=[m.labels[i] for i in rs['S']],loss=float(np.linalg.norm(sol.fun)),start=it,outer=outer,mode=mode,nfev=sol.nfev)
   valid=s['min_gap']>1e-10 and s['min_den']>0 and s['min_offset']>0 and s['planarity']<1e-9
   rows.append(s);(out/'ALL.json').write_text(json.dumps(rows,sort_keys=True))
   if valid and s['loss']<bestloss:
    bestloss=s['loss'];best=z.copy();(out/'BEST.json').write_text(json.dumps(s,sort_keys=True));print('BEST',mode,it,outer,s['counts'],s['reference_counts'],bestloss,s['min_gap'],flush=True)
   if valid and (rs['counts'] if ref else s['counts'])==[1,1,0]:print('NUMERIC110_CHECK_REQUIRED',mode,flush=True);return
   if sol.nfev<5:break
  print('START',it,'seconds',time.monotonic()-clock,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(dict(mode=mode,starts=starts,seed=141418,outer=6,max_nfev=240)))
 print('ENLARGED_CRITICAL_ATLAS_FINITE_SEARCH_DONE',mode,len(rows),flush=True)
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2]),sys.argv[3])
