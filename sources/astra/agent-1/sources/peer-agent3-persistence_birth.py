"""Full upper-level persistence on physical and centered-polar edge graphs.
Zero features are retained algebraically in the numerical formula; no positive-bar
cutoff enters the objective. Diagnostics are nominations, never exact acceptance.
"""
import numpy as np
from scipy.spatial import ConvexHull

def bars_loss(A,edges,eta=.01):
 aa=np.einsum('ic,ic->i',A,A);i,j=edges.T;e=A[j]-A[i];ee=np.einsum('ic,ic->i',e,e);rawt=-np.einsum('ic,ic->i',A[i],e)/np.where(ee>0,ee,1);t=np.clip(rawt,0,1);feet=A[i]+t[:,None]*e;death=np.einsum('ic,ic->i',feet,feet)
 rootmax=int(aa.argmax());R=aa[rootmax];parent=np.arange(len(A));G=np.zeros_like(A);loss=0.;vals=[];rootgrad=0.
 def find(k):
  while parent[k]!=k:parent[k]=parent[parent[k]];k=parent[k]
  return k
 for k in np.argsort(death)[::-1]:
  u,v=find(int(i[k])),find(int(j[k]))
  if u==v:continue
  if (aa[u],u)>(aa[v],v):u,v=v,u
  parent[u]=v;dep=aa[u]-death[k]
  if dep<-1e-12*R:raise ValueError('edge enters above an endpoint')
  if dep<=0:continue
  birth=aa[u];coeff=1/(eta*birth+dep);loss+=np.log1p(dep/(eta*birth));G[u]+=coeff*(1-dep/birth)*2*A[u];G[i[k]]-=coeff*2*(1-t[k])*feet[k];G[j[k]]-=coeff*2*t[k]*feet[k];vals.append(float(dep/birth))
 assert rootgrad==0
 return float(loss),G,sorted(vals,reverse=True)

def evaluate(X,eta=.01):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ic,ic->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];vol6=np.einsum('ic,ic->i',a,np.cross(b,c));D=vol6.sum();g=np.sum(vol6[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g;H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 edges=np.unique(np.sort(np.concatenate([T[:,[0,1]],T[:,[1,2]],T[:,[2,0]]]),axis=1),axis=0)
 qe=np.unique(np.sort(np.column_stack((np.repeat(np.arange(len(T)),3),hull.neighbors.ravel())),axis=1),axis=0)
 active=hull.vertices;mapv=np.full(len(X),-1,int);mapv[active]=np.arange(len(active));pe=mapv[edges]
 lp,GP,P=bars_loss(Z[active],pe,eta);lq,GQ,Q=bars_loss(H,qe,eta);G=np.zeros_like(X);G[active]=GP
 w=np.linalg.solve(np.swapaxes(Z[T],1,2),GQ[...,None])[...,0];dZT=-w[:,:,None]*H[:,None,:];np.add.at(G,T.reshape(-1),dZT.reshape(-1,3))
 tg=-G.sum(axis=0);s=(a+b+c-4*g)@tg
 for k,cr in [(0,np.cross(b,c)),(1,np.cross(c,a)),(2,np.cross(a,b))]:np.add.at(G,T[:,k],(vol6[:,None]*tg+s[:,None]*cr)/(4*D))
 info=dict(V=len(active),triangles=len(T),loss=lp+lq,Ploss=lp,Qloss=lq,P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),centroid=g.tolist())
 return lp+lq,G,info
if __name__=='__main__':
 rng=np.random.default_rng(329);X=rng.normal(size=(21,3));d=rng.normal(size=X.shape);d/=np.linalg.norm(d);v,G,info=evaluate(X)
 for h in [1e-4,1e-5,1e-6,1e-7]:print(h,(evaluate(X+h*d)[0]-evaluate(X-h*d)[0])/(2*h),np.sum(G*d))
