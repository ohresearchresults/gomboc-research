"""Finite true-own-mass external fan and metric searches. Numerical proposals only."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from fan_model import Fan
from atlas_search import route

def main(base,oldreport,mode,starts,outpath):
 m=Fan(base);out=Path(outpath);out.mkdir(exist_ok=False);rng=np.random.default_rng(150915)
 old=json.loads(Path(oldreport).read_text());Z0=np.zeros(20);Z0[:12]=np.array([-820002103986,-1548086488676,-112992330957,1089876949456,-1127081554446,844574678379,558751400795,-514007562035,-45599803363,29336576723,7513593536,-25355875470])/1e12
 oldP=np.array([[float(__import__('fractions').Fraction(x)) for x in p] for p in old['raw_vertices']]);
 # Original source114 is identified by its owner set instead of accidental new raw index.
 ff=[[i for i in range(len(old['faces'])) if j in old['faces'][i]] for j in range(old['V'])]
 k=next(j for j,own in enumerate(ff) if own==[17,71,73]);Z0[18]=(oldP[k,0]-m.u0[18])/.01
 if mode=='metric':Z0=np.r_[Z0,np.zeros(5)]
 n=len(Z0);lo=np.r_[np.full(20,-20.),[-1.5,-1.5,-3,-3,-3]][:n];hi=np.r_[np.full(20,20.),[1.5,1.5,3,3,3]][:n]
 def brief(z):
  s=m.brief(z);P,_=m.points(z);g=np.array(s['centroid']);u=P[m.ix[111]]-g;v=P[m.ix[150]]-g;s['energy10']=float(10*(v@v-u@u)-(v-u)@(v-u));return s
 records=[];best=None;bestscore=1e10;clock=time.monotonic()
 for it in range(starts):
  z=Z0.copy() if it==0 else np.clip((best if best is not None and it%3 else Z0)+rng.normal(size=n)*10**rng.uniform(-2,.2),lo+1e-6,hi-1e-6)
  for outer in range(5):
   pv,dv,g,gap,den,vol=m.calc(z);P,_=m.points(z);ps=m.mesh.state(P)
   root=int(np.argmax(np.sum((P-g)**2,axis=1)));fr=m.rS
   # Both root systems can turn over; polar root is a true maximal-norm pole.
   ft=(P-g)[m.mesh.ft];nn=np.cross(ft[:,1]-ft[:,0],ft[:,2]-ft[:,0]);hh=np.einsum('ij,ij->i',nn,ft[:,0]);YY=nn/hh[:,None];fr=int(np.argmax(np.sum(YY**2,axis=1)))
   ip=route(m.mesh.n,m.src,m.dst,pv,root);jp=route(m.mesh.nf,m.fs,m.fd,dv,fr)
   def values(z):
    pv,dv,g,gap,den,vol=m.calc(z)
    mask=gap.real.copy();mask[m.mesh.inc]=np.inf;js=mask.argmin(axis=1)
    geom=gap[np.arange(m.mesh.nf),js]-1e-9
    P,_=m.points(z);edges=P[m.mesh.ep[:,1]]-P[m.mesh.ep[:,0]];el=np.sqrt((edges*edges).sum(axis=1))
    return np.r_[pv[ip]-1e-7,dv[jp]-1e-7,1e3*geom,100*(el-1e-4),100*vol]
   def fun(z):return np.minimum(values(z),0)
   def jac(z):
    v=values(z);J=np.empty((len(v),n))
    for k in range(n):
     zz=z.astype(complex);zz[k]+=1e-25j;J[:,k]=values(zz).imag/1e-25
    J[v>=0]=0;return J
   try:sol=least_squares(fun,z,jac=jac,bounds=(lo,hi),max_nfev=180,x_scale='jac',ftol=1e-10,xtol=1e-11,gtol=1e-11)
   except (ValueError,np.linalg.LinAlgError) as e:
    records.append(dict(start=it,outer=outer,error=str(e)));break
   z=sol.x;s=brief(z);s.update(start=it,outer=outer,loss=float(np.linalg.norm(sol.fun)),nfev=sol.nfev,mode=mode)
   valid=s['min_gap']>1e-10 and s['min_offset']>0 and s['planarity']<1e-9
   s['valid_numeric']=bool(valid);records.append(s);(out/'ALL.json').write_text(json.dumps(records,sort_keys=True))
   score=s['loss']
   if valid and score<bestscore:
    bestscore=score;best=z.copy();(out/'BEST.json').write_text(json.dumps(s,sort_keys=True));print('BEST',mode,it,outer,s['counts'],score,s['energy10'],flush=True)
   if valid and s['counts']==[1,1,0]:print('NUMERIC110_NEEDS_AUDIT',flush=True);return
   if sol.nfev<4:break
  print('START_DONE',mode,it,'seconds',time.monotonic()-clock,flush=True)
 (out/'DONE.json').write_text(json.dumps(dict(mode=mode,starts=starts,seed=150915,max_nfev=180,outer=5,states=len(records))))
 print('FINITE_EXTERNAL_FAN_SEARCH_DONE',mode,len(records),flush=True)
if __name__=='__main__':
 sys.set_int_max_str_digits(0);main(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5])
