"""Genuine planar-quad polyhedra with independently tilting section planes.

Section k is z=z_k+t_k.x. Its projected edge equations are n_ki.x=h_ki.
The side plane through that edge is
  (n_ki-s_ki t_k).x + s_ki z = h_ki+s_ki z_k.
Consequently n_(k+1),i=n_ki+s_ki(t_(k+1)-t_k), and
h_(k+1),i=h_ki-s_ki(z_(k+1)-z_k). This exact recursion preserves every
side quadrilateral as one physical plane even though sections can tilt.
The top closes at (0,0,1). True V=F=mL+1, E=2mL. All physical mass is
integrated on the resulting single closed convex body at its own centroid.
"""
import numpy as np
import jax
import jax.numpy as jnp
from parallel_section_family import SectionFamily
from support_persistence import barcode
from geometry import angular_scores

class TiltingSectionFamily(SectionFamily):
    def __init__(self,normals,L):
        super().__init__(normals,L);m=self.m;H=m*L;T=jnp.asarray(self.T)
        @jax.jit
        def construct(q):
            h=q[:m];slopes=q[m:H].reshape(L-1,m);z=q[H:H+L];tilt=q[H+L:H+3*L].reshape(L,2);theta=q[-m:];n=jnp.c_[jnp.cos(theta),jnp.sin(theta)];ns=[];hs=[]
            for k in range(L):
                ns.append(n);hs.append(h)
                if k<L-1:n=n+slopes[k,:,None]*(tilt[k+1]-tilt[k])[None,:];h=h-slopes[k]*(z[k+1]-z[k])
            ns=jnp.stack(ns);hs=jnp.stack(hs);matrices=jnp.stack([ns,jnp.roll(ns,-1,axis=1)],axis=2);rhs=jnp.stack([hs,jnp.roll(hs,-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices,rhs[:,:,:,None]).squeeze(-1);zz=z[:,None]+jnp.sum(xy*tilt[:,None,:],axis=2);X=jnp.r_[jnp.c_[xy.reshape(-1,2),zz.ravel()],jnp.array([[0.,0.,1.]])];ss=jnp.r_[slopes,(hs[-1]/(1-z[-1])).reshape(1,m)];N=jnp.r_[jnp.c_[(ns-ss[:,:,None]*tilt[:,None,:]).reshape(-1,2),ss.ravel()],jnp.array([[tilt[0,0],tilt[0,1],-1.]])];d=jnp.r_[(hs+ss*z[:,None]).ravel(),-z[0]];return X,N,d,ns
        @jax.jit
        def physical(q):
            X,N,d,ns=construct(q);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
        self.construct=construct;self.physical=physical
    def independent_construct(self,q):
        m,L=self.m,self.L;H=m*L;h=q[:m];slopes=q[m:H].reshape(L-1,m);z=q[H:H+L];tilt=q[H+L:H+3*L].reshape(L,2);theta=q[-m:];n=np.c_[np.cos(theta),np.sin(theta)];ns=[];hs=[]
        for k in range(L):
            ns.append(n);hs.append(h)
            if k<L-1:n=n+slopes[k,:,None]*(tilt[k+1]-tilt[k])[None,:];h=h-slopes[k]*(z[k+1]-z[k])
        ns=np.stack(ns);hs=np.stack(hs);matrices=np.stack([ns,np.roll(ns,-1,axis=1)],axis=2);rhs=np.stack([hs,np.roll(hs,-1,axis=1)],axis=2);xy=np.linalg.solve(matrices,rhs[:,:,:,None]).squeeze(-1);zz=z[:,None]+np.sum(xy*tilt[:,None,:],axis=2);X=np.r_[np.c_[xy.reshape(-1,2),zz.ravel()],[[0.,0.,1.]]];ss=np.r_[slopes,(hs[-1]/(1-z[-1])).reshape(1,m)];N=np.r_[np.c_[(ns-ss[:,:,None]*tilt[:,None,:]).reshape(-1,2),ss.ravel()],[[tilt[0,0],tilt[0,1],-1.]]];d=np.r_[(hs+ss*z[:,None]).ravel(),-z[0]];return X,N,d,ns
    def independent_physical(self,q):
        X,N,d,ns=self.independent_construct(q);T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
    def state(self,q):
        m,L=self.m,self.L;H=m*L;z=q[H:H+L];theta=q[-m:];angles=np.diff(np.r_[theta,theta[0]+2*np.pi])
        if np.diff(np.r_[z,1.]).min()<1e-8 or angles.min()<1e-6 or angles.max()>np.pi-1e-6:raise ValueError('tilted section levels or initial normals out of order')
        X,N,d,ns=self.independent_construct(q);det=ns[:,:,0]*np.roll(ns[:,:,1],-1,axis=1)-ns[:,:,1]*np.roll(ns[:,:,0],-1,axis=1)
        if det.min()<1e-9:raise ValueError('a tilted polygon changes its cyclic edge order')
        X,Z,Y,g,v,N,d=self.independent_physical(q);gap=(d[:,None]-N@X.T)/np.linalg.norm(N,axis=1)[:,None]
        if abs(gap[self.contact]).max()>1e-8 or gap[~self.contact].min()<1e-11 or v<=0 or np.min(d-N@g)<=0:raise ValueError('tilted section body is not the declared strict convex hull')
        V=F=H+1;E=2*H;pp,pw,P=barcode(Z,np.ones(V),self.eu);qp,qw,Q=barcode(Y,np.ones(F),self.es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y)
        return dict(X=X,Z=Z,Y=Y,g=g,volume=float(v),N=N,d=d,faces=self.faces,T=self.T,eu=self.eu,es=self.es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),V=V,E=E,F=F,minimum_noncontact=float(gap[~self.contact].min()),uguards=us.max(1),sguards=ss.max(1))

def from_parallel(q,normals,L):
    m=len(normals);h=q[:m*L].reshape(L,m);z=q[m*L:m*L+L];theta=q[-m:] if len(q)>m*L+L else np.unwrap(np.arctan2(normals[:,1],normals[:,0]));slopes=-np.diff(h,axis=0)/np.diff(z)[:,None];return np.r_[h[0],slopes.ravel(),z,np.zeros(2*L),theta]
