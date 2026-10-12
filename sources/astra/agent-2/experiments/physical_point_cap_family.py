"""Full convex hull of a deformable support body and one free physical point.
All visible facets, true horizon triangles and retired old vertices are
computed explicitly. Exact old polygon planes and cap corner contacts are
preserved. No integration triangulation is counted as extra hull incidence.
The search edge ceiling is distinct from the final E<=249 qualification.
"""
from collections import defaultdict
import numpy as np
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from support_persistence import barcode
from geometry import angular_scores

class PointCapFamily:
    def __init__(self,m,search_edge_limit=280):
        self.m=m;self.search_edge_limit=search_edge_limit;self.base=ApexFamily(m,allow_top_retirement=True,edge_limit=249)
        @jax.jit
        def physical(z,R,T,A):
            baseR,kept,children,used=R;H=self.base.unpack(z[:-3]);P=jnp.r_[jnp.array([[0.,0.,1.]]),jnp.linalg.solve(H[baseR[1:]],jnp.ones((len(baseR)-1,3,1))).squeeze(-1),z[-3:].reshape(1,3)];newH=jnp.linalg.solve(P[children],jnp.ones((len(children),3,1))).squeeze(-1);bodyH=jnp.r_[H[kept],newH];a,b,c=P[T[:,0]],P[T[:,1]],P[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());X=P[used];return X,X-g,bodyH/(1-bodyH@g)[:,None],g,six.sum()/6
        self.physical=physical
    def independent_physical(self,z,R,T,A):
        m=self.m;baseR,kept,children,used=R;q=z[:-3];H=np.r_[np.c_[q[:2*m].reshape(m,2),np.ones(m)],q[2*m:].reshape(-1,3)];P=np.r_[[[0.,0.,1.]],np.linalg.solve(H[baseR[1:]],np.ones((len(baseR)-1,3,1))).squeeze(-1),z[-3:].reshape(1,3)];newH=np.linalg.solve(P[children],np.ones((len(children),3,1))).squeeze(-1);bodyH=np.r_[H[kept],newH];a,b,c=P[T[:,0]],P[T[:,1]],P[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());X=P[used];return X,X-g,bodyH/(1-bodyH@g)[:,None],g,six.sum()/6
    def state(self,z):
        s=self.base.state(z[:-3]);p=z[-3:];side=s['H'][s['A']]@p-1
        if np.min(abs(side))<1e-12:raise ValueError('point lies on a visibility transition')
        visible=side>0;kept=s['A'][~visible];fullfaces=[ff.copy() for i,ff in enumerate(s['faces']) if not visible[i]];oldadj=defaultdict(list)
        for i,ff in enumerate(s['faces']):
            for a,b in zip(ff,ff[1:]+ff[:1]):oldadj[tuple(sorted((a,b)))].append(i)
        horizon=[e for e,ij in oldadj.items() if visible[ij[0]]!=visible[ij[1]]];P=np.r_[s['X'],p.reshape(1,3)];children=[]
        for a,b in horizon:
            tri=[a,b,len(P)-1];normal=np.linalg.solve(P[tri],np.ones(3))
            if np.cross(P[b]-P[a],p-P[a])@normal<0:tri=tri[::-1]
            children.append(tri);fullfaces.append(tri)
        used=np.array(sorted(set(v for ff in fullfaces for v in ff)),int)
        if len(used)<4:raise ValueError('the actual cap hull is not three dimensional')
        V=len(used);F=len(fullfaces);E=V+F-2
        if not 17<=E<=self.search_edge_limit:raise ValueError('cap body outside declared search budget')
        remap={int(v):i for i,v in enumerate(used)};faces=[[remap[v] for v in ff] for ff in fullfaces];children=np.asarray(children,int).reshape(-1,3);A=np.arange(F);R=(s['R'],kept,children,used);T=np.array([[ff[0],ff[i],ff[i+1]] for ff in fullfaces for i in range(1,len(ff)-1)],int);X,Z,Y,g,v=map(np.asarray,self.physical(z,R,T,A));adj=defaultdict(list)
        for i,ff in enumerate(faces):
            for a,b in zip(ff,ff[1:]+ff[:1]):adj[tuple(sorted((a,b)))].append(i)
        if len(adj)!=E or not all(len(ff)==2 for ff in adj.values()) or v<=0:raise ValueError('cap incidence or mass failed')
        eu=np.array(list(adj),int);es=np.array(list(adj.values()),int);pp,pw,BP=barcode(Z,np.ones(V),eu);qp,qw,BQ=barcode(Y,np.ones(F),es);BP/=np.sum(Z[pp[:,0]]**2,1);BQ/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1);bodyH=np.r_[s['H'][kept],np.linalg.solve(P[children],np.ones((len(children),3,1))).squeeze(-1)]
        return dict(H=bodyH,baseH=s['H'],cap_point=p,X=X,Z=Z,Y=Y,g=g,volume=float(v),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=BP,Q=BQ,Pmax=float(BP.max()),Qmax=float(BQ.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(V),up],sguards=ss[np.arange(F),sp],V=V,E=E,F=F,minimum_noncontact=float(min(s['minimum_noncontact'],abs(side).min())),visible_facets=int(visible.sum()))
