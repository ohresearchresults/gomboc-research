"""Sparse meridian slope blocks with independently tilted section planes.
Equal vertical side coefficients make consecutive planes EXACTLY identical,
so ProfileFamily's maximal-facet and genuine-vertex incidence applies. Each
meridian's controls are its bottom support followed by the vertical coefficient
of each nonfinal block. The final block coefficient is derived to meet the
single physical apex (0,0,1). There is no independent rounding of derived planes.
"""
import numpy as np
import jax
import jax.numpy as jnp
from concave_profile_family import ProfileFamily
from support_persistence import barcode
from geometry import angular_scores

class TiltingProfileFamily(ProfileFamily):
    def __init__(self,m,L,breaks):
        super().__init__(m,L,breaks);K=self.K;offset=self.offset;T=jnp.asarray(self.T);kept=jnp.asarray(self.kept);segments=np.asarray(self.segments);owner=segments[:,0];start=segments[:,1];blocks=[[max(j for j,a in enumerate(breaks[i]) if a<=k) for i in range(m)] for k in range(L)]
        @jax.jit
        def construct(q):
            h=jnp.array([q[offset[i]] for i in range(m)]);z=q[K:K+L];tilt=q[K+L:K+3*L].reshape(L,2);theta=q[-m:];n=jnp.c_[jnp.cos(theta),jnp.sin(theta)];ns=[];hs=[];ss=[];last=jnp.zeros(m)
            for k in range(L):
                coeff=[]
                for i in range(m):
                    j=blocks[k][i]
                    if j<len(breaks[i])-1:value=q[offset[i]+1+j]
                    else:
                        if k==breaks[i][-1]:last=last.at[i].set(h[i]/(1-z[k]))
                        value=last[i]
                    coeff.append(value)
                slope=jnp.array(coeff);ns.append(n);hs.append(h);ss.append(slope)
                if k<L-1:n=n+slope[:,None]*(tilt[k+1]-tilt[k])[None,:];h=h-slope*(z[k+1]-z[k])
            ns=jnp.stack(ns);hs=jnp.stack(hs);ss=jnp.stack(ss);matrices=jnp.stack([ns,jnp.roll(ns,-1,axis=1)],axis=2);rhs=jnp.stack([hs,jnp.roll(hs,-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices,rhs[:,:,:,None]).squeeze(-1);zz=z[:,None]+jnp.sum(xy*tilt[:,None,:],axis=2);fullX=jnp.r_[jnp.c_[xy.reshape(-1,2),zz.ravel()],jnp.array([[0.,0.,1.]])];X=fullX[kept];slope=ss[start,owner];N=jnp.r_[jnp.c_[ns[start,owner]-slope[:,None]*tilt[start],slope],jnp.array([[tilt[0,0],tilt[0,1],-1.]])];d=jnp.r_[hs[start,owner]+slope*z[start],-z[0]];return X,N,d,ns
        @jax.jit
        def physical(q):
            X,N,d,ns=construct(q);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
        self.construct=construct;self.physical=physical;self.blocks=blocks
    def independent_construct(self,q):
        m,L,K=self.m,self.L,self.K;h=np.array([q[self.offset[i]] for i in range(m)]);z=q[K:K+L];tilt=q[K+L:K+3*L].reshape(L,2);theta=q[-m:];n=np.c_[np.cos(theta),np.sin(theta)];ns=[];hs=[];ss=[];last=np.zeros(m,dtype=q.dtype)
        for k in range(L):
            coeff=[]
            for i in range(m):
                j=self.blocks[k][i]
                if j<len(self.breaks[i])-1:value=q[self.offset[i]+1+j]
                else:
                    if k==self.breaks[i][-1]:last[i]=h[i]/(1-z[k])
                    value=last[i]
                coeff.append(value)
            slope=np.array(coeff);ns.append(n);hs.append(h);ss.append(slope)
            if k<L-1:n=n+slope[:,None]*(tilt[k+1]-tilt[k])[None,:];h=h-slope*(z[k+1]-z[k])
        ns=np.stack(ns);hs=np.stack(hs);ss=np.stack(ss);matrices=np.stack([ns,np.roll(ns,-1,axis=1)],axis=2);rhs=np.stack([hs,np.roll(hs,-1,axis=1)],axis=2);xy=np.linalg.solve(matrices,rhs[:,:,:,None]).squeeze(-1);zz=z[:,None]+np.sum(xy*tilt[:,None,:],axis=2);fullX=np.r_[np.c_[xy.reshape(-1,2),zz.ravel()],[[0.,0.,1.]]];X=fullX[self.kept];segments=np.asarray(self.segments);owner,start=segments[:,0],segments[:,1];slope=ss[start,owner];N=np.r_[np.c_[ns[start,owner]-slope[:,None]*tilt[start],slope],[[tilt[0,0],tilt[0,1],-1.]]];d=np.r_[hs[start,owner]+slope*z[start],-z[0]];return X,N,d,ns
    def independent_physical(self,q):
        X,N,d,ns=self.independent_construct(q);T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=N/(d-N@g)[:,None];return X,Z,Y,g,six.sum()/6,N,d
    def state(self,q):
        m,L,K=self.m,self.L,self.K;z=q[K:K+L];theta=q[-m:];angles=np.diff(np.r_[theta,theta[0]+2*np.pi])
        if np.diff(np.r_[z,1.]).min()<1e-8 or angles.min()<1e-6 or angles.max()>np.pi-1e-6:raise ValueError('sparse tilted profile levels or directions out of order')
        X,N,d,ns=self.independent_construct(q);det=ns[:,:,0]*np.roll(ns[:,:,1],-1,axis=1)-ns[:,:,1]*np.roll(ns[:,:,0],-1,axis=1)
        if det.min()<1e-9:raise ValueError('sparse tilted polygon loses cyclic edge order')
        X,Z,Y,g,v,N,d=self.independent_physical(q);gap=(d[:,None]-N@X.T)/np.linalg.norm(N,axis=1)[:,None]
        if abs(gap[self.contact]).max()>1e-8 or gap[~self.contact].min()<1e-11 or v<=0 or np.min(d-N@g)<=0:raise ValueError('sparse tilted profile is not the declared strict convex hull')
        V,E,F=self.V,self.E,self.F;pp,pw,P=barcode(Z,np.ones(V),self.eu);qp,qw,Q=barcode(Y,np.ones(F),self.es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y)
        return dict(X=X,Z=Z,Y=Y,g=g,volume=float(v),N=N,d=d,faces=self.faces,T=self.T,eu=self.eu,es=self.es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),V=V,E=E,F=F,minimum_noncontact=float(gap[~self.contact].min()),uguards=us.max(1),sguards=ss.max(1))
