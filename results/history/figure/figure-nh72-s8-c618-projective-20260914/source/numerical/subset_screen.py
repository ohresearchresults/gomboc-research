"""Finite numerical support-subset screen; no tolerance-based geometry is promoted."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import sys,json,itertools
import numpy as np
from scipy.spatial import ConvexHull,cKDTree

def screen(q):
 hull=ConvexHull(q)
 if hull.equations[:,-1].max()>=0:raise ArithmeticError('unbounded')
 points=-hull.equations[:,:3]/hull.equations[:,3,None]
 tree=cKDTree(points);used=set();X=[]
 for i in range(len(points)):
  if i in used:continue
  used.update(tree.query_ball_point(points[i],1e-8));X.append(points[i])
 X=np.array(sorted(X,key=lambda x:tuple(x)));phys=ConvexHull(X);tr=X[phys.simplices];w=np.abs(np.einsum('ni,ni->n',tr[:,0],np.cross(tr[:,1],tr[:,2])));W=w.sum();g=np.sum(w[:,None]*tr.sum(axis=1),axis=0)/(4*W)
 faces=[];active=[];owners={}
 for i,n in enumerate(q):
  ids=np.flatnonzero(abs(X@n-1)<1e-8)
  if len(ids)<3:continue
  Z=X[ids]-X[ids].mean(axis=0);axis=np.eye(3)[np.argmin(abs(n))];u=np.cross(n,axis);v=np.cross(n,u)
  cy=ids[np.argsort(np.arctan2(Z@v,Z@u))].tolist();f=len(faces);faces.append(cy);active.append(i)
  for a,b in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted([a,b])),[]).append(f)
 if any(len(v)!=2 for v in owners.values()) or len(X)-len(owners)+len(faces)!=2:raise ArithmeticError('Numerical incidence inconsistent')
 poles=q[active]/(1-q[active]@g)[:,None];P=X-g;Umat=P@P.T-np.sum(P*P,axis=1)[:,None];np.fill_diagonal(Umat,-np.inf);Smat=poles@poles.T-np.sum(poles*poles,axis=1)[:,None];np.fill_diagonal(Smat,-np.inf)
 U=np.flatnonzero(Umat.max(axis=1)<0).tolist();S=np.flatnonzero(Smat.max(axis=1)<0).tolist();H=[]
 for (i,j),fs in owners.items():
  e=P[j]-P[i];tau=-P[i]@e/(e@e);h=P[i]+tau*e;n,m=q[np.array(active)[fs]];k=np.cross(n,m);kk=k@k
  vals=[tau,1-tau,np.cross(h,m)@k/kk,np.cross(n,h)@k/kk]
  if min(vals)>0:H.append([i,j])
 return dict(V=len(X),E=len(owners),F=len(faces),counts=[len(S),len(U),len(H)],weak_unchecked=True,S=[active[i] for i in S],U=U,H=H,volume=float(W/6),centroid=g.tolist())
def main():
 raw=json.loads(Path(sys.argv[1]).read_text());q=np.array([[a/r[3] for a in r[:3]] for r in raw['H']]);out=Path(sys.argv[2]);out.mkdir(exist_ok=False);sets=set()
 for d,owners in [(99,[44,81,100]),(117,[55,94,118]),(84,[82,103,105])]:
  for size in range(4):
   for extra in itertools.combinations(owners,size):sets.add(tuple(sorted([d,*extra])))
 for d in [99,117]:
  for j in range(137):
   if j not in [3,d]:sets.add(tuple(sorted([d,j])))
 records=[]
 for deleted in sorted(sets):
  keep=[j for j in range(137) if j not in deleted]
  try:
   a=screen(q[keep]);a['S_original']=[keep[i] for i in a['S']];a['deleted']=list(deleted);records.append(a)
   if sum(a['counts'][:2])<=4:print(deleted,a['V'],a['E'],a['F'],a['counts'],flush=True)
  except Exception as e:records.append(dict(deleted=list(deleted),error=repr(e)))
 (out/'ALL.json').write_text(json.dumps(records,sort_keys=True))
 print('FINITE_COARSENED_SUPPORT_SCREEN_FINISHED',len(records),flush=True)
if __name__=='__main__':main()
