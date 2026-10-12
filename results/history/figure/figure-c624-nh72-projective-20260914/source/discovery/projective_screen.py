"""Completed finite screens are numerical only; own filled mass is recomputed."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,sys,time
from pathlib import Path
from orbit_search import Orbit

def state(m,t,A=None):
 den=1+m.X@t
 if den.min()<=0:raise ValueError('projective horizon')
 y=m.X/den[:,None];tri=y[m.tri];w=np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2]));s=tri.sum(axis=1);W=w.sum()
 g=np.sum(w[:,None]*s,axis=0)/(4*W);m2=(np.einsum('i,ij,ik->jk',w,s,s)+np.einsum('i,iaj,iak->jk',w,tri,tri))/(20*W);cov=m2-np.outer(g,g)
 if A is None:return y,g,cov,den,W/6
 P=(y-g)@A.T;b=m.q+t;Y=(b/(1-b@g)[:,None])@np.linalg.inv(A)
 vv=[];roots=[];counts=[]
 for X,(i,j),n in zip((P,Y),m.edges,m.n):
  e=X[j]-X[i];v=np.einsum('ij,ij->i',X[i],e)/(np.linalg.norm(X[i],axis=1)*np.linalg.norm(e,axis=1));ma=np.full(n,-np.inf);np.maximum.at(ma,i,v)
  roots.append(np.flatnonzero(ma<0).tolist());counts.append(len(roots[-1]));r=np.argmax(np.einsum('ij,ij->i',X,X));ma[r]=1;vv.extend(ma.tolist())
 return dict(t=t.tolist(),A=A.tolist(),U=roots[0],S=roots[1],min_nonroot=min(vv),l1_deficit=sum(max(-v,0) for v in vv),l2_deficit=sum(min(v,0)**2 for v in vv),condition=float(np.linalg.cond(A)),min_den=float(den.min()),volume=float(abs(np.linalg.det(A))*W/6),centroid=(A@g).tolist())

def main():
 import argparse
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--directions',type=int,default=256);args=p.parse_args();out=Path(args.out);out.mkdir(exist_ok=False);m=Orbit(args.report)
 _,_,cov0,_,_=state(m,np.zeros(3));L0=np.linalg.cholesky(cov0);vals=[];best={};start=time.monotonic();records=open(out/'ALL.jsonl','w');win=False
 levels=[0,.001,.003,.01,.03,.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.975,.99,.995,.999]
 directions=[]
 for k in range(args.directions):
  z=1-2*(k+.5)/args.directions;a=k*np.pi*(3-np.sqrt(5));directions.append(np.array([np.sqrt(1-z*z)*np.cos(a),np.sqrt(1-z*z)*np.sin(a),z]))
 for l,rho in enumerate(levels):
  for k,u in enumerate(directions if rho else [directions[0]]):
   t=u*rho/np.max(-m.X@u);y,g,C,den,V=state(m,t);L=np.linalg.cholesky(C)
   matrices=[('identity',np.eye(3)),('covariance',L0@np.linalg.inv(L)),('isotropic',np.linalg.inv(L))]
   for name,A in matrices:
    info=state(m,t,A);info.update(mode=name,level=rho,direction=k);records.write(json.dumps(info)+'\n');key=(len(info['U'])+len(info['S']),info['l1_deficit'])
    if name not in best or key<best[name][0]:
     best[name]=(key,info);(out/(name+'_BEST.json')).write_text(json.dumps(info,sort_keys=True));print('BEST',name,key,info['condition'],rho,flush=True)
    if key[0]==2 and info['min_nonroot']>1e-8:
     (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));win=True;break
   if win:break
  print('LEVEL_FINISHED',rho,'seconds',time.monotonic()-start,flush=True)
  if win:break
 records.close();(out/'CONFIG.json').write_text(json.dumps(vars(args),sort_keys=True));print('FINITE_FULL_PROJECTIVE_SCREEN_FINISHED',flush=True)
if __name__=='__main__':main()
