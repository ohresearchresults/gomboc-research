"""Convex hull of a deformable support body and finitely many physical points.

Each point is inserted by the exact visible-facet/horizon construction, in
floating arithmetic during search. Old maximal polygon facets are preserved;
new facets are horizon triangles. Integration triangulations never change the
genuine incidence count. All free coordinates belong to one filled body.
"""
from collections import defaultdict
import numpy as np
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from support_persistence import barcode
from geometry import angular_scores


class MultipleCapFamily:
    def __init__(self, m, point_count=2, search_edge_limit=280):
        if point_count < 1:
            raise ValueError('positive number of explicit physical points required')
        self.m=m; self.point_count=point_count; self.search_edge_limit=search_edge_limit
        self.base=ApexFamily(m,allow_top_retirement=True,edge_limit=249)
        K=3*point_count
        @jax.jit
        def physical(z,R,T,A):
            baseR,kept,children,used=R
            H=self.base.unpack(z[:-K])
            P=jnp.r_[jnp.array([[0.,0.,1.]]),jnp.linalg.solve(H[baseR[1:]],jnp.ones((len(baseR)-1,3,1))).squeeze(-1),z[-K:].reshape(-1,3)]
            newH=jnp.linalg.solve(P[children],jnp.ones((len(children),3,1))).squeeze(-1)
            bodyH=jnp.r_[H[kept],newH]
            a,b,c=P[T[:,0]],P[T[:,1]],P[T[:,2]]
            six=jnp.sum(a*jnp.cross(b,c),1)
            g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
            X=P[used]
            return X,X-g,bodyH/(1-bodyH@g)[:,None],g,six.sum()/6
        self.physical=physical

    def independent_physical(self,z,R,T,A):
        K=3*self.point_count; m=self.m; q=z[:-K]
        baseR,kept,children,used=R
        H=np.r_[np.c_[q[:2*m].reshape(m,2),np.ones(m)],q[2*m:].reshape(-1,3)]
        P=np.r_[[[0.,0.,1.]],np.linalg.solve(H[baseR[1:]],np.ones((len(baseR)-1,3,1))).squeeze(-1),z[-K:].reshape(-1,3)]
        newH=np.linalg.solve(P[children],np.ones((len(children),3,1))).squeeze(-1)
        bodyH=np.r_[H[kept],newH]
        a,b,c=P[T[:,0]],P[T[:,1]],P[T[:,2]]
        six=np.sum(a*np.cross(b,c),1)
        g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
        X=P[used]
        return X,X-g,bodyH/(1-bodyH@g)[:,None],g,six.sum()/6

    def state(self,z):
        K=3*self.point_count
        base=self.base.state(z[:-K]); points=z[-K:].reshape(-1,3)
        P=np.r_[base['X'],points]; nbase=len(base['X'])
        fs=[(int(i),list(f)) for i,f in zip(base['A'],base['faces'])]
        H=base['H'][base['A']].copy(); minimum=base['minimum_noncontact']; counts=[]
        for k,point in enumerate(points):
            side=H@point-1
            if np.min(abs(side))<1e-12:
                raise ValueError('an added point lies on a visibility transition')
            minimum=min(minimum,float(np.min(abs(side))))
            visible=side>0; counts.append(int(visible.sum()))
            adj=defaultdict(list)
            for i,(_,f) in enumerate(fs):
                for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(i)
            if not all(len(v)==2 for v in adj.values()):
                raise ValueError('intermediate hull is not a closed manifold')
            horizon=[e for e,ij in adj.items() if visible[ij[0]]!=visible[ij[1]]]
            retained=[v for i,v in enumerate(fs) if not visible[i]]
            HH=[h for i,h in enumerate(H) if not visible[i]]
            for a,b in horizon:
                tri=[a,b,nbase+k]; normal=np.linalg.solve(P[tri],np.ones(3))
                if np.cross(P[b]-P[a],point-P[a])@normal<0:tri=tri[::-1]
                retained.append((None,tri));HH.append(normal)
            fs=retained;H=np.asarray(HH)
        # Stable ordering: genuine base polygons first, then derived facets.
        fs=[v for v in fs if v[0] is not None]+[v for v in fs if v[0] is None]
        kept=np.array([i for i,_ in fs if i is not None],int)
        children=np.asarray([f for i,f in fs if i is None],int).reshape(-1,3)
        fullfaces=[f for _,f in fs]
        used=np.array(sorted(set(v for f in fullfaces for v in f)),int)
        V=len(used);F=len(fs);E=V+F-2
        if V<4 or not 17<=E<=self.search_edge_limit:
            raise ValueError('actual multipoint hull exceeds the declared search budget')
        remap={int(v):i for i,v in enumerate(used)}
        faces=[[remap[v] for v in f] for f in fullfaces]
        T=np.array([[f[0],f[i],f[i+1]] for f in fullfaces for i in range(1,len(f)-1)],int)
        A=np.arange(F);R=(base['R'],kept,children,used)
        X,Z,Y,g,v=map(np.asarray,self.physical(z,R,T,A))
        bodyH=np.r_[base['H'][kept],np.linalg.solve(P[children],np.ones((len(children),3,1))).squeeze(-1)]
        # Check both containment and strictness of every declared noncontact.
        gaps=1-bodyH@X.T; contact=np.zeros((F,V),bool)
        for i,f in enumerate(faces):contact[i,f]=True
        if abs(gaps[contact]).max()>1e-8 or gaps.min()<-1e-8 or gaps[~contact].min()<1e-11:
            raise ValueError('multipoint hull has an undeclared contact or lost convexity')
        minimum=min(minimum,float(gaps[~contact].min()))
        adj=defaultdict(list)
        for i,f in enumerate(faces):
            for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(i)
        if len(adj)!=E or not all(len(f)==2 for f in adj.values()) or v<=0:
            raise ValueError('multipoint hull incidence or mass failed')
        eu=np.array(list(adj),int);es=np.array(list(adj.values()),int)
        pp,pw,BP=barcode(Z,np.ones(V),eu);qp,qw,BQ=barcode(Y,np.ones(F),es)
        BP/=np.sum(Z[pp[:,0]]**2,1);BQ/=np.sum(Y[qp[:,0]]**2,1)
        us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
        return dict(H=bodyH,baseH=base['H'],cap_points=points,X=X,Z=Z,Y=Y,g=g,volume=float(v),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=BP,Q=BQ,Pmax=float(BP.max()),Qmax=float(BQ.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(V),up],sguards=ss[np.arange(F),sp],V=V,E=E,F=F,minimum_noncontact=minimum,visible_facets=counts)
