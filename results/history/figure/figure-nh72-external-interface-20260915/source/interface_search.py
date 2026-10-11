"""Finite moment-coupled contact-interface search, source-only numerical reproposal."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from interface_model import Interface
from atlas_search import route
OLD=[-.820002103986,-1.548086488676,-.112992330957,1.089876949456,-1.127081554446,.844574678379,.558751400795,-.514007562035,-.045599803363,.029336576723,.007513593536,-.025355875470]
def main(base,gen,mode,starts,outname):
 m=Interface(base,gen);out=Path(outname);out.mkdir(exist_ok=False);rng=np.random.default_rng(150916);n=30 if mode=='metric' else 25
 z0=np.r_[np.zeros(13),OLD,np.zeros(n-25)];lower=np.r_[np.full(25,-5),[-1.,-1.,-2.,-2.,-2.]][:n];upper=-lower
 best=z0.copy();score=1e30;records=[];clock=time.monotonic()
 for it in range(starts):
  if it==0:z=z0.copy()
  elif it==1:z=np.zeros(n)
  else:z=np.clip((best if it%3 else z0)+rng.normal(size=n)*10**rng.uniform(-3,-.2),lower+1e-8,upper-1e-8)
  for outer in range(4):
   try:
    p,d,g,gap,den,v=m.calc(z);P,_=m.points(z);root=m.rU;fr=m.rS
    ip=route(m.mesh.n,m.src,m.dst,p,root);jp=route(m.mesh.nf,m.fs,m.fd,d,fr)
    def values(z):
     p,d,g,gap,den,v=m.calc(z);mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1)
     P,_=m.points(z);e=P[m.mesh.ep[:,1]]-P[m.mesh.ep[:,0]];length=np.sqrt((e*e).sum(axis=1))
     return np.r_[p[ip]-1e-7,d[jp]-1e-7,1e3*(gap[np.arange(m.mesh.nf),j]-1e-8),100*(length-1e-4),1e3*v]
    def fun(z):return np.minimum(values(z),0)
    def jac(z):
     v=values(z);J=np.empty((len(v),n))
     for k in range(n):
      zz=z.astype(complex);zz[k]+=1e-25j;J[:,k]=values(zz).imag/1e-25
     J[v>=0]=0;return J
    sol=least_squares(fun,z,jac=jac,bounds=(lower,upper),max_nfev=180,x_scale='jac',ftol=1e-10,xtol=1e-11,gtol=1e-11)
   except (ValueError,np.linalg.LinAlgError) as ex:
    records.append(dict(start=it,outer=outer,error=str(ex)));break
   # A physical line search excludes convexity-destroying optimizer endpoints.
   zz=sol.x;s=m.brief(zz);valid=s['min_gap']>1e-11 and s['planarity']<1e-8 and s['min_offset']>0
   s.update(start=it,outer=outer,nfev=sol.nfev,loss=float(np.linalg.norm(sol.fun)),valid_numeric=bool(valid))
   records.append(s);(out/'ALL.json').write_text(json.dumps(records,sort_keys=True))
   if valid:
    z=zz
    if s['loss']<score:
     score=s['loss'];best=z.copy();(out/'BEST.json').write_text(json.dumps(s,sort_keys=True));print('BEST',mode,it,outer,s['counts'],s['loss'],s['min_gap'],flush=True)
   else:
    for step in [.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125]:
     zz=z+step*(sol.x-z);ss=m.brief(zz)
     if ss['min_gap']>1e-11 and ss['planarity']<1e-8 and ss['min_offset']>0:z=zz;break
    else:break
   if valid and s['counts']==[1,1,0]:print('NUMERIC110_REQUIRES_EXACT',flush=True);return
  print('START',mode,it,'elapsed',time.monotonic()-clock,flush=True)
 (out/'DONE.json').write_text(json.dumps(dict(starts=starts,states=len(records),seed=150916,max_nfev=180,outer=4,mode=mode)))
 print('FINITE_CONTACT_INTERFACE_SEARCH_DONE',mode,len(records),flush=True)
if __name__=='__main__':sys.set_int_max_str_digits(0);main(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5])
