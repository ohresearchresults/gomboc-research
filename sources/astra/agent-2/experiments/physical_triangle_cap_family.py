"""One physical point cap on a freely deforming homogeneous base polyhedron.

The base is an apex-polygon halfspace family. The point is a separate free
3-vector and sees exactly one declared triangular facet. Original polygon
facets remain exact planes; three new child planes are derived from actual
points. This preserves the three new nonsimple corner contacts and costs
exactly three genuine edges, without triangulation inflation. Every mass
calculation below integrates the capped body, not its base.
"""
from collections import defaultdict
import numpy as np
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from support_persistence import barcode
from geometry import angular_scores

class TriangleCapFamily:
    def __init__(self,m,carrier,edge_limit=249):
        self.m=m;self.carrier=carrier;self.edge_limit=edge_limit;self.base=ApexFamily(m,allow_top_retirement=True,edge_limit=edge_limit)
        @jax.jit
        def physical(z,R,T,A):
            baseR,kept,children=R;H=self.base.unpack(z[:-3]);X=jnp.r_[jnp.array([[0.,0.,1.]]),jnp.linalg.solve(H[baseR[1:]],jnp.ones((len(baseR)-1,3,1))).squeeze(-1),z[-3:].reshape(1,3)]
            newH=jnp.linalg.solve(X[children],jnp.ones((len(children),3,1))).squeeze(-1);bodyH=jnp.r_[H[kept],newH];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=jnp.sum(a*jnp.cross(b,c),1);g=jnp.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=bodyH/(1-bodyH@g)[:,None]
            return X,Z,Y,g,six.sum()/6
        self.physical=physical
    def independent_physical(self,z,R,T,A):
        m=self.m;baseR,kept,children=R;q=z[:-3];H=np.r_[np.c_[q[:2*m].reshape(m,2),np.ones(m)],q[2*m:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[baseR[1:]],np.ones((len(baseR)-1,3,1))).squeeze(-1),z[-3:].reshape(1,3)];newH=np.linalg.solve(X[children],np.ones((len(children),3,1))).squeeze(-1);bodyH=np.r_[H[kept],newH];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());return X,X-g,bodyH/(1-bodyH@g)[:,None],g,six.sum()/6
    def state(self,z):
        s=self.base.state(z[:-3]);p=z[-3:];where=np.flatnonzero(s['A']==self.carrier)
        if len(where)!=1:raise ValueError('declared cap carrier retired')
        f=int(where[0]);face=s['faces'][f]
        if len(face)!=3:raise ValueError('declared cap carrier ceased to be triangular')
        side=s['H'][s['A']]@p-1
        if list(np.flatnonzero(side>0))!=[f] or np.min(abs(side))<1e-12:raise ValueError('point does not strictly see exactly its carrier')
        V=s['V']+1;F=s['F']+2;E=s['E']+3
        if not 17<=E<=self.edge_limit:raise ValueError('actual capped body exceeds its edge budget')
        kept=np.delete(s['A'],f);faces=[ff.copy() for j,ff in enumerate(s['faces']) if j!=f];X=np.r_[s['X'],p.reshape(1,3)];children=[];childkeys=[]
        owner={}
        for i,ff in enumerate(s['faces']):
            if i==f:continue
            for a,b in zip(ff,ff[1:]+ff[:1]):owner[tuple(sorted((a,b)))]=int(s['A'][i])
        for a,b in zip(face,face[1:]+face[:1]):
            tri=[a,b,V-1];n=np.linalg.solve(X[tri],np.ones(3))
            if np.cross(X[b]-X[a],p-X[a])@n<0:tri=tri[::-1]
            children.append(tri);faces.append(tri);childkeys.append(len(s['H'])+owner[tuple(sorted((a,b)))])
        children=np.array(children,int);A=np.r_[kept,childkeys];R=(s['R'],kept,children);T=np.array([[ff[0],ff[i],ff[i+1]] for ff in faces for i in range(1,len(ff)-1)],int);X,Z,Y,g,v=map(np.asarray,self.physical(z,R,T,A));adj=defaultdict(list)
        for i,ff in enumerate(faces):
            for a,b in zip(ff,ff[1:]+ff[:1]):adj[tuple(sorted((a,b)))].append(i)
        if len(adj)!=E or not all(len(ff)==2 for ff in adj.values()) or V-E+F!=2 or v<=0:raise ValueError('cap hull incidence or mass failed')
        eu=np.array(list(adj),int);es=np.array(list(adj.values()),int);pp,pw,P=barcode(Z,np.ones(V),eu);qp,qw,Q=barcode(Y,np.ones(F),es);P/=np.sum(Z[pp[:,0]]**2,1);Q/=np.sum(Y[qp[:,0]]**2,1);us=angular_scores(Z);ss=angular_scores(Y);up=us.argmax(1);sp=ss.argmax(1)
        bodyH=np.r_[s['H'][kept],np.linalg.solve(X[children],np.ones((3,3,1))).squeeze(-1)]
        return dict(H=bodyH,baseH=s['H'],cap_point=p,X=X,Z=Z,Y=Y,g=g,volume=float(v),R=R,T=T,A=A,faces=faces,eu=eu,es=es,pp=pp,pw=pw,qp=qp,qw=qw,P=P,Q=Q,Pmax=float(P.max()),Qmax=float(Q.max()),S=int((ss.max(1)<0).sum()),U=int((us.max(1)<0).sum()),up=up,sp=sp,uguards=us[np.arange(V),up],sguards=ss[np.arange(F),sp],V=V,E=E,F=F,minimum_noncontact=float(min(s['minimum_noncontact'],abs(side).min())))
