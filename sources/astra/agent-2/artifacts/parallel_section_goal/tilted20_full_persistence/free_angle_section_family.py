"""The genuine quadrilateral-section family with movable azimuth directions.
All levels share each horizontal normal, preserving exact planar side quads.
Controls are [section support values, level heights, unwrapped azimuth angles].
For exact freezing, each shared direction is rationalized ONCE, followed by
rational sectional intersections; independently rounded hull planes are wrong.
"""
import numpy as np
import jax
import jax.numpy as jnp
from parallel_section_family import SectionFamily
from support_persistence import barcode
from geometry import angular_scores

class FreeAngleSectionFamily(SectionFamily):
    def __init__(self,normals,L):
        super().__init__(normals,L);m=self.m;T=jnp.asarray(self.T)
        @jax.jit
        def physical(q):
            h=q[:m*L].reshape(L,m);z=q[m*L:m*L+L];theta=q[-m:];n=jnp.c_[jnp.cos(theta),jnp.sin(theta)];matrices=jnp.stack([n,jnp.roll(n,-1,axis=0)],axis=1);rhs=jnp.stack([h,jnp.roll(h,-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);X=jnp.r_[jnp.c_[xy.reshape(-1,2),jnp.repeat(z,m)],jnp.array([[0.,0.,1.]])]
            hh=jnp.r_[h,jnp.zeros((1,m))];zz=jnp.r_[z,1.];slope=jnp.diff(hh,axis=0)/jnp.diff(zz)[:,None];intercept=h-slope*z[:,None];N=jnp.r_[jnp.c_[jnp.tile(n,(L,1)),-slope.ravel()],jnp.array([[0.,0.,-1.]])];offset=jnp.r_[intercept.ravel(),-z[0]];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(offset-N@g)[:,None]
            return X,Z,Y,g,six.sum()/6,N,offset
        self.physical=physical
    def independent_physical(self,q):
        m,L=self.m,self.L;h=q[:m*L].reshape(L,m);z=q[m*L:m*L+L];theta=q[-m:];n=np.c_[np.cos(theta),np.sin(theta)];matrices=np.stack([n,np.roll(n,-1,axis=0)],axis=1);rhs=np.stack([h,np.roll(h,-1,axis=1)],axis=2);xy=np.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);X=np.r_[np.c_[xy.reshape(-1,2),np.repeat(z,m)],[[0.,0.,1.]]];hh=np.r_[h,np.zeros((1,m))];zz=np.r_[z,1.];slope=np.diff(hh,axis=0)/np.diff(zz)[:,None];intercept=h-slope*z[:,None];N=np.r_[np.c_[np.tile(n,(L,1)),-slope.ravel()],[[0.,0.,-1.]]];offset=np.r_[intercept.ravel(),-z[0]];T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(offset-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,offset
    def state(self,q):
        m,L=self.m,self.L;z=q[m*L:m*L+L];theta=q[-m:];angles=np.diff(np.r_[theta,theta[0]+2*np.pi])
        if np.diff(np.r_[z,1.]).min()<1e-8 or angles.min()<1e-6 or angles.max()>np.pi-1e-6:raise ValueError('section levels or horizontal normals out of cyclic order')
        X,Z,Y,g,v,N,d=self.independent_physical(q);normalized=(d[:,None]-N@X.T)/np.linalg.norm(N,axis=1)[:,None]
        if np.max(abs(normalized[self.contact]))>1e-8 or np.min(normalized[~self.contact])<1e-11 or v<=0 or np.min(d-N@g)<=0:raise ValueError('free-angle sections are not a strict convex hull')
        V=F=m*L+1;E=2*m*L;pp,pw,P=barcode(Z,np.ones(V),self.eu);qp,qw,Q=barcode(Y,np.ones(F),self.es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y)
        return dict(X=X,Z=Z,Y=Y,g=g,volume=float(v),N=N,d=d,faces=self.faces,T=self.T,eu=self.eu,es=self.es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),V=V,E=E,F=F,minimum_noncontact=float(normalized[~self.contact].min()),uguards=us.max(1),sguards=ss.max(1))
