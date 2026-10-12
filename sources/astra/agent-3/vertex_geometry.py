"""Floating full Jacobians for physical vertex coordinates and own volume mass."""
import numpy as np
from scipy.spatial import ConvexHull
from support_geometry import escape

def geometry(X,derivatives=True):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;M=np.sum(v6[:,None]*(a+b+c),axis=0)/24;g=M/V;Z=X-g;H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 data=dict(X=X,Z=Z,H=H,g=g,T=T,V=V,vertices=hull.vertices)
 if not derivatives:return data
 n=len(X);d=n*3;DX=np.eye(d).reshape(n,3,d);da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]]
 dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
 DV=dv6.sum(axis=0)/6;DM=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24;Dg=(DM-g[:,None]*DV)/V;DZ=DX-Dg
 DH=np.linalg.solve(Z[T],-np.einsum('nc,nacp->nap',H,DZ[T]));data.update(DX=DX,DZ=DZ,DH=DH,Dg=Dg)
 return data

def widest(A):
 aa=np.sum(A*A,axis=1);q=A@A.T/aa[:,None]-1;np.fill_diagonal(q,-np.inf);root=int(aa.argmax());cap=np.full(len(A),-np.inf);cap[root]=np.inf;used=np.zeros(len(A),bool);parent=np.full(len(A),-1,int)
 for _ in range(len(A)):
  u=int(np.argmax(np.where(used,-np.inf,cap)));assert np.isfinite(cap[u]) or u==root
  used[u]=True;new=np.minimum(cap[u],q[:,u]);take=(new>cap)&(~used);cap[take]=new[take];parent[take]=u
 parent[root]=(root+1)%len(A)
 return root,parent,cap

def summary(g):
 vp,_=escape(g['Z']);vq,_=escape(g['H']);rp,pp,bp=widest(g['Z']);rq,pq,bq=widest(g['H'])
 return dict(V=len(g['vertices']),F=len(g['H']),E=len(g['vertices'])+len(g['H'])-2,S=int(np.sum(vq<0)),U=int(np.sum(vp<0)),primal_bottleneck=float(np.min(bp)),dual_bottleneck=float(np.min(bq)),min_primal=float(np.min(np.delete(vp,rp))),min_dual=float(np.min(np.delete(vq,rq))),volume=float(g['V']))
