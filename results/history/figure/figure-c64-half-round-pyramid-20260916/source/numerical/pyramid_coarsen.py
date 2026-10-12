"""Numerical changed-base coarsening into exact candidates, not exclusions.
Uniform solid pyramid, true area centroid used at each evaluation. At least
8 base vertices (C>=32). This auxiliary search targets U=1, S<=2, not a winner.
Complete geometric checkpoints are saved independently of optimizer replay.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
import pyramid_search as ps
TAU=1e-3;CONVEX=1e-4;MIN_EDGE=.01;HEIGHT=.04

def shape(x,n):
 B=np.array(x[:2*n]).reshape(n,2);a=np.array(x[-2:]);N=np.roll(B,-1,axis=0)
 area=(B[:,0]*N[:,1]-B[:,1]*N[:,0]);total=area.sum()
 if abs(total)<1e-12:raise ValueError('zero area')
 c=((B+N)*area[:,None]).sum(axis=0)/(3*total);B-=c;a-=c
 scale=np.max(np.linalg.norm(B,axis=1))
 if scale<1e-8:raise ValueError('zero scale')
 B/=scale;a/=scale;return B,a,total

def residual(x,n,detail=False):
 try:
  B,a,area=shape(x,n);N=np.roll(B,-1,axis=0);D=N-B
  W=B[None,:,:]-B[:,None,:];gap=D[:,None,0]*W[:,:,1]-D[:,None,1]*W[:,:,0]
  mask=np.ones((n,n),dtype=bool);mask[np.arange(n),np.arange(n)]=False;mask[np.arange(n),(np.arange(n)+1)%n]=False
  turn=gap[mask];edge=np.linalg.norm(D,axis=1);P=np.vstack([np.c_[B,np.zeros(n)],np.r_[a,HEIGHT]]);g=np.r_[a,HEIGHT]/4;P-=g
  u=ps.score(P);p=np.maximum(TAU-u[0],0);p[u[1]]=0
  result=np.r_[p,10*np.maximum(CONVEX-turn,0),10*np.maximum(MIN_EDGE-edge,0)]
  if not detail:return result
  valid=bool(area>0 and np.min(turn)>0 and np.min(edge)>0)
  loss,PP,QQ,uu,ss,gg=ps.census(B,a,HEIGHT) if valid else (None,None,None,None,None,None)
  return {'n':n,'C':4*n,'x':list(map(float,x)),'squared_loss':float(result@result),'convex':valid,'minimum_convex_turn':float(turn.min()),'minimum_edge_length':float(edge.min()),'min_nonroot_u':float(np.min(np.delete(u[0],u[1]))),'U':int(sum(u[0]<0)),'S':int(sum(ss[0]<0)) if valid else None,'root_vertex':u[1],'primal_eta':u[0].tolist(),'height':HEIGHT,'base':B.tolist(),'apex':list(map(float,a))+[HEIGHT],'raw_points':np.vstack([np.c_[B,np.zeros(n)],np.r_[a,HEIGHT]]).tolist(),'own_centroid':g.tolist(),'numerical_own211':bool(valid and sum(u[0]<0)==1 and sum(ss[0]<0)==2 and np.min(np.delete(u[0],u[1]))>1e-7)}
 except (ValueError,FloatingPointError,AssertionError):
  return {'invalid':True,'squared_loss':1e6} if detail else np.ones(n+1+n*(n-2)+n)*100

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,required=True);ap.add_argument('--seed',type=int,default=160926);ap.add_argument('--tries',type=int,default=4);ap.add_argument('--max-nfev',type=int,default=150);ap.add_argument('--out',required=True);a=ap.parse_args();assert 8<=a.n<=20
 B,ix,c=ps.polygon(np.array(ps.POINTS,dtype=float));scale=np.max(np.linalg.norm(B,axis=1));B/=scale;apex=(np.array([9316983.,-76697552.])-c)/scale
 rng=np.random.default_rng(a.seed);records=[]
 for k in range(a.tries):
  inds=np.sort(np.unique(np.r_[6,rng.choice([i for i in range(20) if i!=6],a.n-1,replace=False)]))
  x=np.r_[B[inds].flatten(),apex]
  if k>0:x+=rng.normal(0,.02,len(x))
  r=least_squares(residual,x,args=(a.n,),max_nfev=a.max_nfev,ftol=1e-10,xtol=1e-10,gtol=1e-10,diff_step=None,method='trf')
  d=residual(r.x,a.n,True);records.append({'initial_kept_indices':inds.tolist(),'success':bool(r.success),'message':str(r.message),'nfev':int(r.nfev),**d})
  out={'method':'changed-base U1 coarsening with true pyramid volume centroid; auxiliary nonwinner search','seed':a.seed,'n':a.n,'tries':a.tries,'max_nfev':a.max_nfev,'tau':TAU,'convex_target':CONVEX,'min_edge_target':MIN_EDGE,'height':HEIGHT,'records':records,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':hashlib.sha256(Path(ps.__file__).read_bytes()).hexdigest(),'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'terminal':'CHANGED_BASE_COARSENING_FINITE_SCREEN_COMPLETE' if k+1==a.tries else 'PARTIAL_CHECKPOINT','certified_exclusion':False}
  Path(a.out).write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print(a.n,k,d.get('squared_loss'),d.get('min_nonroot_u'),d.get('S'),d.get('U'),d.get('convex'),d.get('numerical_own211'),flush=True)
if __name__=='__main__':main()
