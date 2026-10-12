"""Finite physical homotopies own211 -> own121, with <=67 support planes.
All intermediate centroids are integrated from their actual hulls.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,time,argparse
from scipy.spatial import ConvexHull
from scipy.optimize import linear_sum_assignment
from geometry import halfspace_mesh,census
from audit_exact import R

def centered(Q):
 m=halfspace_mesh(Q);return Q/(1-Q@m['g'])[:,None]*m['volume']**(1/3)
def frame(Q):
 m=halfspace_mesh(Q);p=m['X']-m['g'];q=Q/(1-Q@m['g'])[:,None]
 u=p[np.argmax((p*p).sum(1))];u=u/np.linalg.norm(u);s=q[np.argmax((q*q).sum(1))];s=s-(s@u)*u;s=s/np.linalg.norm(s)
 return np.column_stack([u,s,np.cross(u,s)])
def augment(Q,directions,count):
 h=ConvexHull(Q);U=Q/np.linalg.norm(Q,axis=1)[:,None];D=directions/np.linalg.norm(directions,axis=1)[:,None];dist=np.min(np.linalg.norm(D[:,None]-U[None],axis=2),axis=1);ix=np.argsort(-dist)[:count];rows=[]
 for u in D[ix]:
  dots=h.equations[:,:3]@u;ok=dots>1e-12;r=np.min(-h.equations[ok,3]/dots[ok]);rows.append(.94*r*u)
 return np.vstack([Q,rows])
def run(out,angles=16,nt=151):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 A=centered(np.load('artifacts/j90-c390/seed.npz')['Q']);data=json.load(open('sources/peer-agent2-KF27D-H_exact.json'))['H'];B=centered(np.array([[float(R(v,row[3])) for v in row[:3]] for row in data]));FA=frame(A);FB=frame(B);records=[];t0=time.time();best=999
 print('ENDPOINTS',census(halfspace_mesh(A)),census(halfspace_mesh(B)),flush=True)
 for reflect in [1,-1]:
  for k in range(angles):
   theta=2*np.pi*k/angles;ct,st=np.cos(theta),np.sin(theta);turn=np.array([[1,0,0],[0,ct,-st],[0,st,ct]])@np.diag([1,1,reflect]);rot=FA@turn@FB.T;Y=B@rot.T;Y=augment(Y,A,len(A)-len(Y));da=A/np.linalg.norm(A,axis=1)[:,None];dy=Y/np.linalg.norm(Y,axis=1)[:,None];cost=np.sum((da[:,None]-dy[None])**2,axis=2)+.05*(np.log(np.linalg.norm(A,axis=1))[:,None]-np.log(np.linalg.norm(Y,axis=1))[None,:])**2;ii,jj=linear_sum_assignment(cost);Y=Y[jj]
   for ti in range(nt):
    t=ti/(nt-1);Q=(1-t)*A+t*Y
    try:
     m=halfspace_mesh(Q);s=census(m);row=dict(reflect=reflect,angle=k,t=t,**s);records.append(row);key=s['S']+s['U']
     if key<best:
      best=key;np.savez(out/'best.npz',Q=Q,A=A,B=Y);(out/'best.json').write_text(json.dumps(row,indent=2));print('BEST',reflect,k,t,s['S'],s['U'],s['E'],'seconds',time.time()-t0,flush=True)
     if s['S']==s['U']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
      np.savez(out/'NOMINATION110.npz',Q=Q,A=A,B=Y);(out/'NOMINATION110.json').write_text(json.dumps(row,indent=2));print('NUMERIC110_REQUIRES_EXACT',row,flush=True);return
    except Exception as e:records.append(dict(reflect=reflect,angle=k,t=t,error=str(e)))
   (out/'history.json').write_text(json.dumps(records,separators=(',',':')));print('ANGLE_DONE',reflect,k,'best',best,'seconds',time.time()-t0,flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--angles',type=int,default=16);ap.add_argument('--nt',type=int,default=151);a=ap.parse_args();run(a.out,a.angles,a.nt)
