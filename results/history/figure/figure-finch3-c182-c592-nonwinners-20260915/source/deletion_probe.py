"""Finite physical support deletion proposals. Floating f-vectors are diagnostic;
maximal exact facets/edges and all own equilibria must subsequently be rebuilt."""
import json,argparse,radial,numpy as np
from fractions import Fraction as F
from scipy.spatial import HalfspaceIntersection,ConvexHull,cKDTree
from pathlib import Path

def census(H):
 q=np.array([[float(F(v,h[-1])) for v in h[:3]] for h in H]);hs=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3));P=hs.intersections
 # Cluster roundoff duplicates; never used in exact definition.
 keep=[];T=cKDTree(P);dead=set()
 for i in range(len(P)):
  if i not in dead:keep.append(i);dead.update(T.query_ball_point(P[i],1e-8))
 P=P[keep];fac=[];active=[]
 for f,n in enumerate(q):
  ids=np.flatnonzero(abs(P@n-1)<1e-7)
  if len(ids)<3:continue
  a=np.eye(3)[np.argmin(abs(n))];u=np.cross(n,a);u/=np.linalg.norm(u);v=np.cross(n,u);pts=np.c_[P[ids]@u,P[ids]@v]
  try:cy=ids[ConvexHull(pts).vertices].tolist()
  except Exception:continue
  if np.dot(n,np.cross(P[cy[1]]-P[cy[0]],P[cy[2]]-P[cy[0]]))<0:cy.reverse()
  fac.append(cy);active.append(f)
 tri=np.array([(cy[0],cy[j],cy[j+1]) for cy in fac for j in range(1,len(cy)-1)]);X=P[tri];d=np.einsum('ni,ni->n',X[:,0],np.cross(X[:,1],X[:,2]));g=np.einsum('n,ni->i',d,X.sum(axis=1))/(4*d.sum());V=d.sum()/6;U=[]
 for i,p in enumerate(P):
  if max((P-p)@(p-g))<1e-10:U.append(i)
 S=[]
 for f,cy in zip(active,fac):
  n=q[f];p=P[cy];ex=-np.einsum('ni,i->n',np.cross(p-g,np.roll(p,-1,axis=0)-p),n)
  if max(ex)<1e-10:S.append(f)
 E={tuple(sorted((i,j))) for cy in fac for i,j in zip(cy,cy[1:]+cy[:1])};return {'V':len(P),'E_numerical':len(E),'F':len(fac),'S':S,'U':U,'centroid':g.tolist(),'volume':V,'min_area_det':float(d.min()),'euler':len(P)-len(E)+len(fac)}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--start',default='QUOT_11_1.json');p.add_argument('--tag',default='QDEL');a=p.parse_args();G=json.load(open(a.start));raw,P=radial.reconstruct(G);H=raw['H'];tr=[]
 for rem in [[],[121],[108],[125],[120],[122],[37],[57],[63],[70],[121,108],[121,125],[121,114]]:
  try:r=census([h for i,h in enumerate(H) if i not in rem]);r['delete']=rem;print(r,flush=True);tr.append(r)
  except Exception as e:print('error',rem,str(e));tr.append({'delete':rem,'error':str(e)})
 Path(a.tag+'.json').write_text(json.dumps(tr,sort_keys=True,separators=(',',':')))
