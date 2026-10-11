"""Physical halfspace family with one prescribed arbitrary-valence apex.

First m normals lie in z=1 and form a strictly convex m-gon; all other
normals have z<1. The body is H.x<=1, with genuine apex (0,0,1). For F
active planes, E <= 3F-m-3. Only this one nonsimple contact is prescribed;
every other hull incidence is obtained from the actual current geometry.
"""
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull
import jax
import jax.numpy as jnp
from support_persistence import barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

class ApexFamily:
    def __init__(self,m,allow_top_retirement=False,edge_limit=248):
        if not 3<=m<=100:raise ValueError('unsupported explicit apex valence')
        if edge_limit not in [248,249]:raise ValueError('explicit research edge budget required')
        self.m=m;self.edge_limit=edge_limit;self.maxF=(edge_limit+m+3)//3;self.allow_top_retirement=allow_top_retirement
        @jax.jit
        def unpack(q):return jnp.concatenate([jnp.c_[q[:2*m].reshape(m,2),jnp.ones(m)],q[2*m:].reshape(-1,3)],axis=0)
        @jax.jit
        def physical(q,R,T,A):
            H=unpack(q);other=jnp.linalg.solve(H[R[1:]],jnp.ones((len(R)-1,3,1))).squeeze(-1);X=jnp.concatenate([jnp.array([[0.,0.,1.]]),other],axis=0)
            a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
            return X,Z,Y,g,six.sum()/6
        self.unpack=unpack;self.physical=physical
    def pack(self,H):
        if abs(H[:self.m,2]-1).max()>1e-8:raise ValueError('input normals do not share the declared apex')
        return np.r_[H[:self.m,:2].ravel(),H[self.m:].ravel()]
    def independent_physical(self,q,R,T,A):
        m=self.m;H=np.r_[np.c_[q[:2*m].reshape(m,2),np.ones(m)],q[2*m:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());return X,X-g,H[A]/(1-H[A]@g)[:,None],g,six.sum()/6
    def state(self,q):
        m=self.m;H=np.asarray(self.unpack(q));N=len(H)
        if not m<N<=self.maxF or np.max(H[m:,2])>=1-1e-10:raise ValueError('outside the declared apex support domain')
        genuine_top=ConvexHull(H[:m,:2]).vertices;top_degree=len(genuine_top)
        if not self.allow_top_retirement and top_degree!=m:raise ValueError('apex lost a genuine incident plane')
        if top_degree<3:raise ValueError('apex polygon is degenerate')
        h=ConvexHull(H)
        if h.equations[:,3].max()>=-1e-9:raise ValueError('unbounded intersection or boundary origin')
        dualtri=h.simplices;top=np.all(dualtri<m,axis=1)
        if top.sum()!=top_degree-2:raise ValueError('prescribed polar polygon is absent')
        R=np.r_[dualtri[np.flatnonzero(top)[:1]],dualtri[~top]];labels=np.empty(len(dualtri),int);labels[top]=0;labels[~top]=np.arange(1,1+(~top).sum());adj=defaultdict(list)
        for k,t in enumerate(dualtri):
            for i,j in zip(t,np.roll(t,-1)):adj[tuple(sorted((int(i),int(j))))].append(labels[k])
        if not all(len(v)==2 for v in adj.values()):raise ValueError('polar adjacency is not closed')
        ep=np.array([e for e,ff in adj.items() if ff[0]!=ff[1]],int);ed=np.array([ff for ff in adj.values() if ff[0]!=ff[1]],int);A=h.vertices
        X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        incidence=np.zeros((N,len(X)),bool);incidence[:m,0]=True
        for j,tri in enumerate(R[1:],1):incidence[tri,j]=True
        gaps=1-H@X.T;active_noncontacts=gaps[A][~incidence[A]]
        # Redundant input planes can touch a true edge without becoming a
        # facet. Such contacts are not extra physical facets or equilibrium
        # contacts. Separation is required among actual facet incidences.
        if abs(gaps[incidence]).max()>1e-8 or gaps.min()<-1e-8 or active_noncontacts.min()<1e-11:raise ValueError('additional nonsimple contact or inadequate separation')
        faces=[]
        for owner in A:
            links=defaultdict(list)
            for edge,dual in zip(ep,ed):
                if owner not in edge:continue
                a,b=map(int,dual);links[a].append(b);links[b].append(a)
            if not links or not all(len(v)==2 for v in links.values()):raise ValueError('primal facet adjacency fails')
            start=min(links);cy=[start];previous=None;now=start
            while True:
                nxt=next(x for x in links[now] if x!=previous)
                if nxt==start:break
                if nxt in cy:raise ValueError('primal cycle pinched')
                cy.append(nxt);previous,now=now,nxt
            if len(cy)!=len(links):raise ValueError('primal cycle incomplete')
            # Entire polygon area has a stable orientation even when its first
            # three vertices happen to be close to collinear.
            area=np.sum(np.cross(X[cy],X[np.roll(cy,-1)]),axis=0)
            if area@H[owner]<0:cy=cy[::-1]
            faces.append(cy)
        T=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)],int);X,Z,Y,g,v=map(np.asarray,self.physical(q,R,T,A));remap={int(v):i for i,v in enumerate(A)};eu=ed;es=np.array([[remap[int(a)],remap[int(b)]] for a,b in ep]);E=len(eu)
        # Every retired top normal reduces F by one and k by one, reducing
        # the upper bound by two. Thus a pool of N normals, of which m lie
        # on the apex plane, always satisfies E <= 3N-m-3 even when some
        # apex candidates become redundant. Count only genuine hull facets.
        if not 17<=E<=self.edge_limit or E>3*len(A)-top_degree-3 or E>3*N-m-3 or len(X)-E+len(A)!=2 or v<=0:raise ValueError('counts or volume outside the family')
        pp,pw,P=barcode(Z,np.ones(len(Z)),eu);qp,qw,Q=barcode(Y,np.ones(len(Y)),es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1)
        us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
        return dict(H=H,X=X,Z=Z,Y=Y,g=g,volume=float(v),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(len(Z)),up],sguards=ss[np.arange(len(Y)),sp],V=len(X),E=E,F=len(A),minimum_noncontact=float(active_noncontacts.min()))
