import numpy as np
from scipy.spatial import ConvexHull
import search_surface as m
rng=np.random.default_rng(625);X=rng.normal(size=(18,3));dir=rng.normal(size=X.shape);dir/=np.linalg.norm(dir)
def parts(X):
 hull=ConvexHull(X);T=hull.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0;T[flip]=T[flip][:,[0,2,1]]
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];d=np.einsum('ij,ij->i',a,np.cross(b,c));D=d.sum();g=np.sum(d[:,None]*(a+b+c),axis=0)/(4*D);Z=X-g;N=np.cross(b-a,c-a);area=np.linalg.norm(N,axis=1)/2
 H=-hull.equations[:,:3]/(hull.equations[:,3]+hull.equations[:,:3]@g)[:,None]
 return T,Z,H,area,g
T,Z,H,A,g=parts(X)
v,G,_,_=m.routes(Z,1e-6,np.ones(len(Z))/len(Z))
vh,GH,dh,_=m.routes(H,1e-6,A/A.sum())
h=1e-6;Tp,Zp,Hp,Ap,gp=parts(X+h*dir);Tm,Zm,Hm,Am,gm=parts(X-h*dir)
# hull simplices ordering same small step
print('Tmatch',np.array_equal(T,Tp),np.array_equal(T,Tm))
print('primal direct', np.sum(G*(Zp-Zm)/(2*h)),(m.routes(Zp,1e-6,np.ones(len(Z))/len(Z))[0]-m.routes(Zm,1e-6,np.ones(len(Z))/len(Z))[0])/(2*h))
print('polar fixedweights',np.sum(GH*(Hp-Hm)/(2*h)),(m.routes(Hp,1e-6,A/A.sum())[0]-m.routes(Hm,1e-6,A/A.sum())[0])/(2*h))
print('weights',np.dot((dh-vh)/A.sum(),(Ap-Am)/(2*h)),(m.routes(H,1e-6,Ap/Ap.sum())[0]-m.routes(H,1e-6,Am/Am.sum())[0])/(2*h))
a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];N=np.cross(b-a,c-a);unit=N/np.linalg.norm(N,axis=1)[:,None];gb=.5*np.cross(c-a,unit);gc=.5*np.cross(unit,b-a);ga=-gb-gc;da=np.einsum('ij,ij->i',ga,dir[T[:,0]])+np.einsum('ij,ij->i',gb,dir[T[:,1]])+np.einsum('ij,ij->i',gc,dir[T[:,2]])
print('area grad error',np.max(np.abs(da-(Ap-Am)/(2*h))),np.dot((dh-vh)/A.sum(),da))
v,G,i=m.evaluate(X);print('full analytic',np.sum(G*dir),'numeric',(m.evaluate(X+h*dir)[0]-m.evaluate(X-h*dir)[0])/(2*h))
