"""Numerical nominations only; all accepted conclusions require a rational audit."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.sparse.csgraph import dijkstra

def halfspace_mesh(Q):
 Q=np.asarray(Q,dtype=float);h=ConvexHull(Q)
 if np.max(h.equations[:,3])>=-1e-8:raise ValueError('polar origin outside')
 # Maximal coplanar polar facets correspond to single primal vertices.
 keep=[];groups=[];eq=[]
 for k,e in enumerate(h.equations):
  hit=next((i for i,z in enumerate(eq) if np.max(abs(e-z))<1e-8),None)
  if hit is None:eq.append(e);groups.append(set(h.simplices[k]));keep.append(k)
  else:
   groups[hit].update(h.simplices[k])
   if abs(np.linalg.det(Q[h.simplices[k]]))>abs(np.linalg.det(Q[h.simplices[keep[hit]]])):keep[hit]=k
 triples=h.simplices[keep]
 X=np.linalg.solve(Q[triples],np.ones((len(triples),3,1)))[:,:,0]
 faces=[];active=[];triangles=[];edges=set()
 for j in h.vertices:
  ids=[i for i,ss in enumerate(groups) if j in ss]
  if len(ids)<3:continue
  centre=X[ids].mean(0);a=X[ids[0]]-centre;a/=np.linalg.norm(a);b=np.cross(Q[j],a);b/=np.linalg.norm(b)
  cy=np.array(ids)[np.argsort(np.arctan2((X[ids]-centre)@b,(X[ids]-centre)@a))].tolist()
  active.append(int(j));faces.append(cy)
  for u,v in zip(cy,cy[1:]+cy[:1]):edges.add(tuple(sorted((u,v))))
  triangles.extend([cy[0],cy[k],cy[k+1]] for k in range(1,len(cy)-1))
 if len(X)-len(edges)+len(faces)!=2:raise ValueError('numerical hull inconsistent')
 t=np.array(triangles,dtype=int);v=np.einsum('ij,ij->i',X[t[:,0]],np.cross(X[t[:,1]],X[t[:,2]]))/6
 if np.min(v)<-1e-10:raise ValueError('orientation')
 volume=v.sum();g=np.sum(v[:,None]*X[t].sum(1),axis=0)/(4*volume)
 return dict(Q=Q,X=X,triples=triples,faces=faces,active=np.array(active,dtype=int),triangles=t,edges=np.array(sorted(edges),dtype=int),g=g,volume=float(volume))

def arrows(X,angular=True):
 D=X[None,:,:]-X[:,None,:];r=np.linalg.norm(X,axis=1);l=np.linalg.norm(D,axis=2)
 W=np.einsum('ik,ijk->ij',X,D)
 if angular:W=W/np.maximum(r[:,None]*l,1e-30)
 np.fill_diagonal(W,-np.inf)
 return W

def routes(X,root,power=2):
 W=arrows(X);cost=np.maximum(-W,0)**power+1e-14
 np.fill_diagonal(cost,0)
 dist,pre=dijkstra(cost.T,directed=True,indices=root,return_predecessors=True)
 ii=np.delete(np.arange(len(X)),root)
 if np.ndim(dist)==2:
  chosen=np.argmin(dist[:,ii],axis=0);return ii,pre[chosen,ii]
 return ii,pre[ii]

def census(mesh,tol=1e-10):
 X=mesh['X']-mesh['g'];Q=mesh['Q'][mesh['active']];Q=Q/(1-Q@mesh['g'])[:,None]
 U=np.flatnonzero(np.max(arrows(X),axis=1)<-tol)
 S=np.flatnonzero(np.max(arrows(Q),axis=1)<-tol)
 return {'V':len(X),'E':len(mesh['edges']),'F':len(Q),'C':2*len(mesh['edges']),'S':len(S),'U':len(U),'H_inferred':len(S)+len(U)-2,'S_ids':mesh['active'][S].tolist(),'U_ids':U.tolist(),'min_primal_nonroot':float(np.sort(arrows(X).max(1))[1]),'min_polar_nonroot':float(np.sort(arrows(Q).max(1))[1]),'g':mesh['g'].tolist(),'volume':mesh['volume']}

if __name__=='__main__':
 import json
 m=halfspace_mesh(np.load('artifacts/baseline/float.npz')['H']);print(json.dumps(census(m),indent=2))
