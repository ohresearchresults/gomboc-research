"""Direct dual-hull incidence, physical mass, and exact floating derivatives.
No second hull or tolerance-based physical-facet merging is used in nomination.
"""
import numpy as np
from scipy.spatial import ConvexHull

def geometry(Q,derivatives=True):
 n=len(Q);d=3*n;hull=ConvexHull(Q)
 if max(hull.equations[:,3])>=0:raise ValueError('support hull excludes origin')
 T=hull.simplices;X=np.linalg.solve(Q[T],np.ones((len(T),3,1)))[:,:,0];nv=len(X)
 faces=[];labels=hull.vertices
 for f in labels:
  incident=np.flatnonzero(np.any(T==f,axis=1));start=int(incident[0]);prev=-1;current=start;cy=[]
  while True:
   cy.append(current);loc=np.where(T[current]==f)[0][0];links=[int(hull.neighbors[current,k]) for k in range(3) if k!=loc]
   nxt=links[0] if links[0]!=prev else links[1]
   if nxt==start:break
   if nxt in cy:raise ValueError('non-simple facet boundary')
   prev,current=current,nxt
  assert len(cy)==len(incident)
  pts=X[cy];area=np.sum(np.cross(pts,np.roll(pts,-1,axis=0)),axis=0)
  if area@Q[f]<0:cy.reverse()
  faces.append(cy)
 tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)])
 a,b,c=X[tris[:,0]],X[tris[:,1]],X[tris[:,2]]
 v6=np.einsum('ij,ij->i',a,np.cross(b,c));V=v6.sum()/6.;M=np.sum(v6[:,None]*(a+b+c),axis=0)/24.;g=M/V
 Z=X-g;h=1-Q[labels]@g;H=Q[labels]/h[:,None]
 result=dict(X=X,Q=Q,T=T,faces=faces,labels=labels,tris=tris,g=g,Z=Z,H=H,V=V,nv=nv,nf=len(labels),ne=nv+len(labels)-2)
 if not derivatives:return result
 DQ=np.eye(d).reshape(n,3,d);rhs=-np.einsum('nc,nacp->nap',X,DQ[T]);DX=np.linalg.solve(Q[T],rhs)
 da,db,dc=DX[tris[:,0]],DX[tris[:,1]],DX[tris[:,2]]
 dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
 DV=dv6.sum(axis=0)/6.;DM=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24.;Dg=(DM-g[:,None]*DV)/V
 DZ=DX-Dg;Dh=-np.einsum('icp,c->ip',DQ[labels],g)-Q[labels]@Dg;DH=DQ[labels]/h[:,None,None]-Q[labels,:,None]*Dh[:,None,:]/h[:,None,None]**2
 result.update(DQ=DQ,DX=DX,Dg=Dg,DZ=DZ,DH=DH)
 return result

def escape(A,DA=None,angular=False,chosen=None):
 aa=np.einsum('ic,ic->i',A,A);e=A[None,:,:]-A[:,None,:];dot=np.einsum('ic,ijc->ij',A,e)
 if angular:
  ee=np.einsum('ijc,ijc->ij',e,e);den=np.sqrt(np.maximum(aa[:,None]*ee,1e-60));scores=dot/den
 else:scores=dot/aa[:,None]
 np.fill_diagonal(scores,-np.inf);j=scores.argmax(axis=1) if chosen is None else np.array(chosen);i=np.arange(len(A));v=scores[i,j]
 if DA is None:return v,j
 diff=A[j]-A;Ddiff=DA[j]-DA;dots=np.einsum('ic,icp->ip',diff,DA)+np.einsum('ic,icp->ip',A,Ddiff)
 if angular:
  dd=np.einsum('ic,ic->i',diff,diff);dden=np.sqrt(aa*dd);jac=dots/dden[:,None]-v[:,None]*(np.einsum('ic,icp->ip',A,DA)/aa[:,None]+np.einsum('ic,icp->ip',diff,Ddiff)/dd[:,None])
 else:jac=dots/aa[:,None]-2*v[:,None]*np.einsum('ic,icp->ip',A,DA)/aa[:,None]
 return v,j,jac

def census(g):
 vp,jp=escape(g['Z']);vq,jq=escape(g['H']);u=np.argmax(np.sum(g['Z']**2,axis=1));s=np.argmax(np.sum(g['H']**2,axis=1))
 return dict(V=g['nv'],E=g['ne'],F=g['nf'],S=int(np.sum(vq<0)),U=int(np.sum(vp<0)),minV=float(np.min(np.delete(vp,u))),minF=float(np.min(np.delete(vq,s))),g=g['g'].tolist())
if __name__=='__main__':
 import sys
 Q=np.load(sys.argv[1]);g=geometry(Q);print(census(g));rng=np.random.default_rng(847);d=rng.normal(size=Q.shape);d/=np.linalg.norm(d)
 v,j,J=escape(g['Z'],g['DZ']);vv,jj,JJ=escape(g['H'],g['DH'])
 for eps in [1e-5,1e-6,1e-7]:
  p=geometry(Q+eps*d,False);m=geometry(Q-eps*d,False)
  print('gradient_centroid',eps,(p['g']-m['g'])/(2*eps),g['Dg']@d.ravel())
