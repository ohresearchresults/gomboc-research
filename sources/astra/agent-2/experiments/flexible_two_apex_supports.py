"""The same two coplanar support groups, with actual anchor retirement allowed.
The proposed common intersection points need not remain hull vertices. Only
exposed polar group faces create genuine nonsimple primal vertices. All other
vertices are actual polar facets; the true edge count alone enforces E<=249.
"""
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull
import jax
import jax.numpy as jnp
from two_apex_supports import TwoApexFamily
from support_persistence import barcode
from geometry import angular_scores

class FlexibleTwoApexFamily(TwoApexFamily):
    def __init__(self,m,n,edge_limit=249):
        super().__init__(m,n,edge_limit)
        @jax.jit
        def physical(q,R,T,A):
            anchors,tri=R;H=self.unpack(q);anchor_points=jnp.r_[jnp.array([[0.,0.,1.]]),q[-3:].reshape(1,3)]
            X=jnp.r_[anchor_points[anchors],jnp.linalg.solve(H[tri],jnp.ones((len(tri),3,1))).squeeze(-1)]
            a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
            return X,X-g,H[A]/(1-H[A]@g)[:,None],g,six.sum()/6
        self.physical=physical
    def independent_physical(self,q,R,T,A):
        m,n=self.m,self.n;first=q[:2*m].reshape(m,2);second=q[2*m:2*(m+n)].reshape(n,2);v=q[-3:]
        H=np.r_[np.c_[first,np.ones(m)],np.c_[second,(1-second@v[:2])/v[2]],q[2*(m+n):-3].reshape(-1,3)]
        anchors,tri=R;X=np.r_[np.array([[0.,0.,1.],v])[anchors],np.linalg.solve(H[tri],np.ones((len(tri),3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
        return X,X-g,H[A]/(1-H[A]@g)[:,None],g,six.sum()/6
    def state(self,q):
        m,n=self.m,self.n;v=q[-3:];H=np.asarray(self.unpack(q));N=len(H)
        if abs(v[2])<1e-5 or N>self.maxF:raise ValueError('invalid explicit two-plane parameterization')
        h=ConvexHull(H)
        if h.equations[:,3].max()>=-1e-9:raise ValueError('unbounded support intersection')
        tri=h.simplices;groups=[np.all(tri<m,axis=1),np.all((tri>=m)&(tri<m+n),axis=1)]
        anchors=np.array([i for i,g in enumerate(groups) if g.any()],int);other=~(groups[0]|groups[1]);labels=np.empty(len(tri),int)
        for k,i in enumerate(anchors):labels[groups[i]]=k
        labels[other]=np.arange(len(anchors),len(anchors)+other.sum());R=(anchors,tri[other]);adj=defaultdict(list)
        for k,t in enumerate(tri):
            for a,b in zip(t,np.roll(t,-1)):adj[tuple(sorted((int(a),int(b))))].append(int(labels[k]))
        if not all(len(ff)==2 for ff in adj.values()):raise ValueError('polar hull is not closed')
        ep=np.array([e for e,ff in adj.items() if ff[0]!=ff[1]],int);ed=np.array([ff for ff in adj.values() if ff[0]!=ff[1]],int);A=h.vertices
        X=np.r_[np.array([[0.,0.,1.],v])[anchors],np.linalg.solve(H[tri[other]],np.ones((other.sum(),3,1))).squeeze(-1)]
        incidence=np.zeros((N,len(X)),bool)
        for k,i in enumerate(anchors):incidence[:m,k]=True if i==0 else False;incidence[m:m+n,k]=True if i==1 else False
        for j,t in enumerate(tri[other],len(anchors)):incidence[t,j]=True
        gaps=1-H@X.T;non=gaps[A][~incidence[A]]
        if abs(gaps[incidence]).max()>1e-8 or gaps.min()<-1e-8 or non.min()<1e-11:raise ValueError('additional nonsimple contact or invalid reconstructed hull')
        faces=[]
        for owner in A:
            links=defaultdict(list)
            for e,du in zip(ep,ed):
                if owner in e:
                    a,b=map(int,du);links[a].append(b);links[b].append(a)
            if not links or not all(len(v)==2 for v in links.values()):raise ValueError('noncyclic primal facet')
            start=min(links);f=[start];previous=None;now=start
            while True:
                nxt=next(x for x in links[now] if x!=previous)
                if nxt==start:break
                if nxt in f:raise ValueError('pinched facet')
                f.append(nxt);previous,now=now,nxt
            if len(f)!=len(links):raise ValueError('incomplete facet')
            if np.sum(np.cross(X[f],X[np.roll(f,-1)]),axis=0)@H[owner]<0:f=f[::-1]
            faces.append(f)
        T=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)],int);X,Z,Y,g,vol=self.independent_physical(q,R,T,A);remap={int(v):i for i,v in enumerate(A)};eu=ed;es=np.array([[remap[int(a)],remap[int(b)]] for a,b in ep]);V=len(X);E=len(eu);F=len(A)
        if not 17<=E<=self.edge_limit or V-E+F!=2 or vol<=0:raise ValueError('actual complexity or volume failed')
        pp,pw,P=barcode(Z,np.ones(V),eu);qp,qw,Q=barcode(Y,np.ones(F),es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
        return dict(H=H,X=X,Z=Z,Y=Y,g=g,volume=float(vol),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(V),up],sguards=ss[np.arange(F),sp],V=V,E=E,F=F,minimum_noncontact=float(non.min()),active_anchors=anchors.tolist())
