"""Two genuine high-valence physical vertices with free support planes.
The first vertex is (0,0,1). The second is a free physical point v, with
v_z nonzero. Two disjoint groups of normals satisfy h_z=1 and h.v=1
respectively. All other vertices and all uniform mass are reconstructed.
For N input supports and group sizes m,n, E<=3N-m-n, including retirements.
"""
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull
import jax
import jax.numpy as jnp
from support_persistence import barcode
from geometry import angular_scores
jax.config.update('jax_enable_x64',True)

class TwoApexFamily:
    def __init__(self,m,n,edge_limit=249):
        if min(m,n)<3:raise ValueError('each prescribed vertex needs at least three incident normals')
        self.m=m;self.n=n;self.edge_limit=edge_limit;self.maxF=(edge_limit+m+n)//3
        @jax.jit
        def unpack(q):
            first=q[:2*m].reshape(m,2);second=q[2*m:2*(m+n)].reshape(n,2);other=q[2*(m+n):-3].reshape(-1,3);v=q[-3:]
            return jnp.r_[jnp.c_[first,jnp.ones(m)],jnp.c_[second,(1-second@v[:2])/v[2]],other]
        @jax.jit
        def physical(q,R,T,A):
            H=unpack(q);X=jnp.r_[jnp.array([[0.,0.,1.]]),q[-3:].reshape(1,3),jnp.linalg.solve(H[R[2:]],jnp.ones((len(R)-2,3,1))).squeeze(-1)]
            a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
            return X,X-g,H[A]/(1-H[A]@g)[:,None],g,six.sum()/6
        self.unpack=unpack;self.physical=physical
    def pack(self,H,v):
        m,n=self.m,self.n
        if abs(H[:m,2]-1).max()>1e-8 or abs(H[m:m+n]@v-1).max()>1e-8:raise ValueError('planes do not meet at the specified physical vertices')
        return np.r_[H[:m,:2].ravel(),H[m:m+n,:2].ravel(),H[m+n:].ravel(),v]
    def independent_physical(self,q,R,T,A):
        m,n=self.m,self.n;first=q[:2*m].reshape(m,2);second=q[2*m:2*(m+n)].reshape(n,2);v=q[-3:]
        H=np.r_[np.c_[first,np.ones(m)],np.c_[second,(1-second@v[:2])/v[2]],q[2*(m+n):-3].reshape(-1,3)]
        X=np.r_[[[0.,0.,1.]],v.reshape(1,3),np.linalg.solve(H[R[2:]],np.ones((len(R)-2,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
        return X,X-g,H[A]/(1-H[A]@g)[:,None],g,six.sum()/6
    def state(self,q):
        m,n=self.m,self.n;v=q[-3:];H=np.asarray(self.unpack(q));N=len(H)
        if abs(v[2])<1e-5 or N>self.maxF or np.max(H[m:,2])>=1-1e-10 or np.max(np.r_[H[:m],H[m+n:]]@v)>=1-1e-10:raise ValueError('outside the two exposed polar planes')
        h=ConvexHull(H)
        if h.equations[:,3].max()>=-1e-9:raise ValueError('the primal support body is unbounded')
        tri=h.simplices;first=np.all(tri<m,axis=1);second=np.all((tri>=m)&(tri<m+n),axis=1);other=~(first|second)
        if not first.any() or not second.any():raise ValueError('a prescribed nonsimple vertex retired')
        R=np.r_[tri[np.flatnonzero(first)[:1]],tri[np.flatnonzero(second)[:1]],tri[other]];labels=np.empty(len(tri),int);labels[first]=0;labels[second]=1;labels[other]=np.arange(2,2+other.sum());adj=defaultdict(list)
        for k,t in enumerate(tri):
            for a,b in zip(t,np.roll(t,-1)):adj[tuple(sorted((int(a),int(b))))].append(int(labels[k]))
        if not all(len(f)==2 for f in adj.values()):raise ValueError('polar hull is not a manifold')
        ep=np.array([e for e,ff in adj.items() if ff[0]!=ff[1]],int);ed=np.array([ff for ff in adj.values() if ff[0]!=ff[1]],int);A=h.vertices
        X=np.r_[[[0.,0.,1.]],v.reshape(1,3),np.linalg.solve(H[R[2:]],np.ones((len(R)-2,3,1))).squeeze(-1)]
        incidence=np.zeros((N,len(X)),bool);incidence[:m,0]=True;incidence[m:m+n,1]=True
        for j,t in enumerate(R[2:],2):incidence[t,j]=True
        gaps=1-H@X.T;non=gaps[A][~incidence[A]]
        if abs(gaps[incidence]).max()>1e-8 or gaps.min()<-1e-8 or non.min()<1e-11:raise ValueError('undeclared contact or nonconvex reconstructed body')
        faces=[]
        for owner in A:
            links=defaultdict(list)
            for edge,dual in zip(ep,ed):
                if owner in edge:
                    a,b=map(int,dual);links[a].append(b);links[b].append(a)
            if not links or not all(len(v)==2 for v in links.values()):raise ValueError('noncyclic primal facet')
            start=min(links);f=[start];previous=None;now=start
            while True:
                nxt=next(x for x in links[now] if x!=previous)
                if nxt==start:break
                if nxt in f:raise ValueError('pinched primal facet')
                f.append(nxt);previous,now=now,nxt
            if len(f)!=len(links):raise ValueError('incomplete facet')
            if np.sum(np.cross(X[f],X[np.roll(f,-1)]),axis=0)@H[owner]<0:f=f[::-1]
            faces.append(f)
        T=np.array([[f[0],f[i],f[i+1]] for f in faces for i in range(1,len(f)-1)],int);X,Z,Y,g,vol=self.independent_physical(q,R,T,A);remap={int(k):i for i,k in enumerate(A)};eu=ed;es=np.array([[remap[int(a)],remap[int(b)]] for a,b in ep]);E=len(eu);F=len(A);V=len(X)
        if not 17<=E<=self.edge_limit or E>3*N-m-n or V-E+F!=2 or vol<=0:raise ValueError('true complexity or physical mass failed')
        pp,pw,P=barcode(Z,np.ones(V),eu);qp,qw,Q=barcode(Y,np.ones(F),es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
        return dict(H=H,X=X,Z=Z,Y=Y,g=g,volume=float(vol),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(V),up],sguards=ss[np.arange(F),sp],V=V,E=E,F=F,minimum_noncontact=float(non.min()),second_vertex=v)
