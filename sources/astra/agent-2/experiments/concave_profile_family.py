"""Independent concave meridian profiles with genuine maximal facet merging.

Each horizontal normal has its own retained section knots. Between knots its
support height is exactly linear; adjacent former section quads on that plane
form ONE maximal polygon. A grid point is a genuine vertex only if at least
one of its two adjacent meridian profiles breaks there. Thus coplanar facets
and collinear boundary points are removed by construction, not tolerance.
Controls: retained support values by meridian, all levels, shared azimuths.
"""
from collections import defaultdict
import numpy as np
import jax
import jax.numpy as jnp
from support_persistence import barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

class ProfileFamily:
    def __init__(self,m,L,breaks):
        self.m=m;self.L=L;self.breaks=[list(map(int,b)) for b in breaks]
        if len(breaks)!=m or any(not b or b[0]!=0 or sorted(set(b))!=b or b[-1]>=L for b in self.breaks):raise ValueError('invalid explicit meridian knot sets')
        self.K=sum(map(len,self.breaks));offset=np.cumsum([0]+list(map(len,self.breaks)));self.offset=offset
        kept=[k*m+i for k in range(L) for i in range(m) if k==0 or k in self.breaks[i] or k in self.breaks[(i+1)%m]]+[m*L];self.kept=np.array(kept,int);remap={p:i for i,p in enumerate(kept)};faces=[];segments=[]
        for i,bb in enumerate(self.breaks):
            full=bb+[L]
            for a,b in zip(full[:-1],full[1:]):
                left=[(k*m+(i-1)%m if k<L else m*L) for k in range(a,b+1) if (k*m+(i-1)%m if k<L else m*L) in remap];right=[(k*m+i if k<L else m*L) for k in range(a,b+1) if (k*m+i if k<L else m*L) in remap];raw=[left[0]]+right+list(reversed(left[1:]));f=[]
                for v in raw:
                    if not f or v!=f[-1]:f.append(v)
                if f[-1]==f[0]:f.pop()
                if len(set(f))!=len(f) or len(f)<3:raise ValueError('invalid merged profile facet cycle')
                faces.append([remap[v] for v in f]);segments.append((i,a,b))
        faces.append([remap[i] for i in range(m-1,-1,-1)]);self.faces=faces;self.segments=segments;self.T=np.array([[f[0],f[j],f[j+1]] for f in faces for j in range(1,len(f)-1)],int);adj=defaultdict(list)
        for j,f in enumerate(faces):
            for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(j)
        self.eu=np.array(list(adj),int);self.es=np.array(list(adj.values()),int);self.V=len(kept);self.F=len(faces);self.E=len(adj)
        if self.V-self.E+self.F!=2 or not 17<=self.E<=249 or not all(len(x)==2 for x in adj.values()):raise ValueError('true merged-profile hull incidence or edge budget fails')
        self.contact=np.zeros((self.F,self.V),bool)
        for i,f in enumerate(faces):self.contact[i,f]=True
        K=self.K;T=jnp.asarray(self.T);kept=jnp.asarray(kept);segments=np.asarray(segments,int)
        @jax.jit
        def expand(q):
            z=jnp.r_[q[K:K+L],1.];h=jnp.zeros((L+1,m))
            for i,bb in enumerate(self.breaks):
                full=bb+[L];values=jnp.r_[q[offset[i]:offset[i+1]],0.]
                for j,(a,b) in enumerate(zip(full[:-1],full[1:])):
                    t=(z[a:b]-z[a])/(z[b]-z[a]);h=h.at[a:b,i].set(values[j]*(1-t)+values[j+1]*t)
            return h,z
        @jax.jit
        def physical(q):
            h,z=expand(q);theta=q[-m:];n=jnp.c_[jnp.cos(theta),jnp.sin(theta)];matrices=jnp.stack([n,jnp.roll(n,-1,axis=0)],axis=1);rhs=jnp.stack([h[:-1],jnp.roll(h[:-1],-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);fullX=jnp.r_[jnp.c_[xy.reshape(-1,2),jnp.repeat(z[:-1],m)],jnp.array([[0.,0.,1.]])];X=fullX[kept];i,a,b=segments[:,0],segments[:,1],segments[:,2];slope=(h[b,i]-h[a,i])/(z[b]-z[a]);intercept=h[a,i]-slope*z[a];N=jnp.r_[jnp.c_[n[i],-slope],jnp.array([[0.,0.,-1.]])];d=jnp.r_[intercept,-z[0]];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
        self.expand=expand;self.physical=physical
    def independent_expand(self,q):
        m,L,K=self.m,self.L,self.K;z=np.r_[q[K:K+L],1.];h=np.zeros((L+1,m),dtype=q.dtype)
        for i,bb in enumerate(self.breaks):
            full=bb+[L];values=np.r_[q[self.offset[i]:self.offset[i+1]],0.]
            for j,(a,b) in enumerate(zip(full[:-1],full[1:])):
                t=(z[a:b]-z[a])/(z[b]-z[a]);h[a:b,i]=values[j]*(1-t)+values[j+1]*t
        return h,z
    def independent_physical(self,q):
        m,L=self.m,self.L;h,z=self.independent_expand(q);theta=q[-m:];n=np.c_[np.cos(theta),np.sin(theta)];matrices=np.stack([n,np.roll(n,-1,axis=0)],axis=1);rhs=np.stack([h[:-1],np.roll(h[:-1],-1,axis=1)],axis=2);xy=np.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);fullX=np.r_[np.c_[xy.reshape(-1,2),np.repeat(z[:-1],m)],[[0.,0.,1.]]];X=fullX[self.kept];segments=np.asarray(self.segments);i,a,b=segments[:,0],segments[:,1],segments[:,2];slope=(h[b,i]-h[a,i])/(z[b]-z[a]);intercept=h[a,i]-slope*z[a];N=np.r_[np.c_[n[i],-slope],[[0.,0.,-1.]]];d=np.r_[intercept,-z[0]];T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
    def state(self,q):
        m,L,K=self.m,self.L,self.K;z=q[K:K+L];theta=q[-m:];angle=np.diff(np.r_[theta,theta[0]+2*np.pi])
        if np.diff(np.r_[z,1.]).min()<1e-8 or angle.min()<1e-6 or angle.max()>np.pi-1e-6:raise ValueError('profile levels or azimuths out of order')
        X,Z,Y,g,v,N,d=self.independent_physical(q);gaps=(d[:,None]-N@X.T)/np.linalg.norm(N,axis=1)[:,None]
        if np.max(abs(gaps[self.contact]))>1e-8 or np.min(gaps[~self.contact])<1e-11 or v<=0 or np.min(d-N@g)<=0:raise ValueError('merged profile does not define the declared strict convex hull')
        V,E,F=self.V,self.E,self.F;pp,pw,P=barcode(Z,np.ones(V),self.eu);qp,qw,Q=barcode(Y,np.ones(F),self.es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y)
        return dict(X=X,Z=Z,Y=Y,g=g,volume=float(v),N=N,d=d,faces=self.faces,T=self.T,eu=self.eu,es=self.es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),V=V,E=E,F=F,minimum_noncontact=float(gaps[~self.contact].min()),uguards=us.max(1),sguards=ss.max(1))
