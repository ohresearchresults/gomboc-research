"""Convex polyhedra with parallel polygon edges in successive sections.

m fixed ordered horizontal normal directions n_i, L horizontal levels z_k,
and sectional support heights h_ki define each polygon by n_i.x <= h_ki.
Linearly interpolate each h_i in z, ending at h_i(1)=0 at apex (0,0,1).
Strict concavity of each profile and strict polygon convexity give genuine
quadrilateral side facets, m apex triangles, and a maximal bottom m-gon.
The actual closed hull has V=mL+1, F=mL+1, E=2mL. This permits up to 124
section vertices, while preserving every intentional coplanar quadrilateral.
All mass is the uniform three-dimensional volume mass of this ONE body.
"""
from collections import defaultdict
import numpy as np
import jax
import jax.numpy as jnp
from support_persistence import barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

class SectionFamily:
    def __init__(self,normals,L):
        self.normals=np.asarray(normals,float);self.m=len(normals);self.L=L;m=self.m
        if not 9<=m*L<=124 or m<3 or L<2:raise ValueError('section construction outside true edge budget')
        self.matrices=np.stack([self.normals,np.roll(self.normals,-1,axis=0)],axis=1)
        if np.linalg.det(self.matrices).min()<=0:raise ValueError('section normal directions must be in strict cyclic order')
        faces=[]
        for k in range(L-1):
            for i in range(m):faces.append([k*m+(i-1)%m,k*m+i,(k+1)*m+i,(k+1)*m+(i-1)%m])
        for i in range(m):faces.append([(L-1)*m+(i-1)%m,(L-1)*m+i,m*L])
        faces.append(list(range(m-1,-1,-1)));self.faces=faces;self.T=np.asarray([[f[0],f[j],f[j+1]] for f in faces for j in range(1,len(f)-1)],int)
        adj=defaultdict(list)
        for j,f in enumerate(faces):
            for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(j)
        self.eu=np.array(list(adj),int);self.es=np.array(list(adj.values()),int)
        if len(adj)!=2*m*L or not all(len(v)==2 for v in adj.values()):raise ValueError('section incidence construction failed')
        contact=np.zeros((m*L+1,m*L+1),bool)
        for j,f in enumerate(faces):contact[j,f]=True
        self.contact=contact;self.non=np.argwhere(~contact)
        matrices=jnp.asarray(self.matrices);normals=jnp.asarray(normals);T=jnp.asarray(self.T)
        @jax.jit
        def physical(q):
            h=q[:m*L].reshape(L,m);z=q[m*L:];rhs=jnp.stack([h,jnp.roll(h,-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);X=jnp.r_[jnp.c_[xy.reshape(-1,2),jnp.repeat(z,m)],jnp.array([[0.,0.,1.]])]
            hh=jnp.r_[h,jnp.zeros((1,m))];zz=jnp.r_[z,1.];slope=jnp.diff(hh,axis=0)/jnp.diff(zz)[:,None];intercept=h-slope*z[:,None];N=jnp.r_[jnp.c_[jnp.tile(normals,(L,1)),-slope.ravel()],jnp.array([[0.,0.,-1.]])];offset=jnp.r_[intercept.ravel(),-z[0]]
            a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(offset-N@g)[:,None]
            return X,Z,Y,g,six.sum()/6,N,offset
        self.physical=physical
    def independent_physical(self,q):
        m,L=self.m,self.L;h=q[:m*L].reshape(L,m);z=q[m*L:];rhs=np.stack([h,np.roll(h,-1,axis=1)],axis=2);xy=np.linalg.solve(self.matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);X=np.r_[np.c_[xy.reshape(-1,2),np.repeat(z,m)],[[0.,0.,1.]]]
        hh=np.r_[h,np.zeros((1,m))];zz=np.r_[z,1.];slope=np.diff(hh,axis=0)/np.diff(zz)[:,None];intercept=h-slope*z[:,None];N=np.r_[np.c_[np.tile(self.normals,(L,1)),-slope.ravel()],[[0.,0.,-1.]]];offset=np.r_[intercept.ravel(),-z[0]]
        T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(offset-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,offset
    def state(self,q):
        m,L=self.m,self.L;z=q[m*L:]
        if np.diff(np.r_[z,1.]).min()<1e-8:raise ValueError('section levels are not strictly ordered')
        X,Z,Y,g,v,N,d=self.independent_physical(q);gaps=d[:,None]-N@X.T;scale=np.linalg.norm(N,axis=1);normalized=gaps/scale[:,None]
        if np.max(abs(normalized[self.contact]))>1e-8 or np.min(normalized[~self.contact])<1e-11 or v<=0 or np.min(d-N@g)<=0:raise ValueError('section polygons or profiles are not a strict convex hull')
        V,F=m*L+1,m*L+1;E=2*m*L;pp,pw,P=barcode(Z,np.ones(V),self.eu);qp,qw,Q=barcode(Y,np.ones(F),self.es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y)
        return dict(X=X,Z=Z,Y=Y,g=g,volume=float(v),N=N,d=d,faces=self.faces,T=self.T,eu=self.eu,es=self.es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),V=V,E=E,F=F,minimum_noncontact=float(normalized[~self.contact].min()),uguards=us.max(1),sguards=ss.max(1))
