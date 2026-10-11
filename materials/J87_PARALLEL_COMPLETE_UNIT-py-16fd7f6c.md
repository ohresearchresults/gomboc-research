# material-16fd7f6c76de

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Common-direction exact-polynomial chart; floats only nominate later exact tests."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize, LinearConstraint, linprog
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent

def hull(p):
    h=ConvexHull(p)
    f=h.simplices.copy()
    wrong=np.einsum('ij,ij->i',np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]),h.equations[:,:3])<0
    f[wrong]=f[wrong][:,[0,2,1]]
    # Canonical indexing, independent of Qhull ordering for ordinary comparisons.
    f=np.array([np.roll(t,-np.argmin(t)) for t in f]);f=f[np.lexsort(f[:,::-1].T)]
    return f

def mass(p,f):
    tr=p[f];D=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));return D.sum()/6,(D[:,None]*tr.sum(axis=1)).sum(axis=0)/(4*D.sum())

def edges(f):
    ed={}
    for i,tri in enumerate(f):
        for a,b in zip(tri,np.roll(tri,-1)):ed.setdefault(tuple(sorted([int(a),int(b)])),[]).append(i)
    assert all(len(v)==2 for v in ed.values())
    return np.array(list(ed),dtype=int),np.array(list(ed.values()),dtype=int)

def bars(p,e,grad=False):
    rad=np.einsum('ij,ij->i',p,p);dv=p[e[:,1]]-p[e[:,0]];dd=np.einsum('ij,ij->i',dv,dv)
    t=np.clip(-np.einsum('ij,ij->i',p[e[:,0]],dv)/dd,0,1)
    foot=p[e[:,0]]+t[:,None]*dv;levels=np.einsum('ij,ij->i',foot,foot)
    par=np.arange(len(p));out=[];gg=[]
    def root(i):
        while i!=par[i]:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.argsort(-levels,kind='stable'):
        a,b=e[k];i,j=root(a),root(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        depth=1-levels[k]/rad[j]
        if depth>1e-14:
            out.append((float(depth),int(j),[int(a),int(b)]))
            if grad:
                g=np.zeros_like(p);g[j]+=2*levels[k]/rad[j]**2*p[j]
                g[a]-=2*(1-t[k])*foot[k]/rad[j];g[b]-=2*t[k]*foot[k]/rad[j]
                gg.append(g)
        par[j]=i
    return out,gg

def report(p,f=None):
    if f is None:f=hull(p)
    V,q=mass(p,f);p=p-q;ed,dual=edges(f)
    n=np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]);h=np.einsum('ij,ij->i',n,p[f[:,0]]);pp=n/h[:,None]
    P,_=bars(p,ed);Q,_=bars(pp,dual)
    return dict(V=len(np.unique(f)),E=len(ed),F=len(f),volume=float(V),centroid=q.tolist(),P=P,Q=Q)

class Chart:
    def __init__(self,p,d,f=None,anchor=0):
        self.f=hull(p) if f is None else np.array(f)
        self.V,q=mass(p,self.f);self.p=np.array(p)-q;self.q0=q
        self.d=np.array(d,dtype=float);self.d/=np.linalg.norm(self.d)
        self.N=len(p);self.ed,self.dual=edges(self.f)
        a,b,c=self.p[self.f].transpose(1,0,2)
        D=np.einsum('ij,ij->i',a,np.cross(b,c));self.T=np.zeros((len(self.f),self.N));self.R=self.T.copy()
        for k,col in enumerate([np.cross(b,c)@self.d,np.cross(c,a)@self.d,np.cross(a,b)@self.d]):
            self.T[np.arange(len(self.f)),self.f[:,k]]=col
            self.R[np.arange(len(self.f)),self.f[:,k]]=1
        self.A=self.T.sum(axis=0)/6
        self.B=((a+b+c).T@self.T+np.outer(self.d,D@self.R))/24
        perp=null_space(self.d[None,:]);C=np.vstack([self.A,perp.T@self.B])
        C=C/np.linalg.norm(C,axis=1)[:,None]
        if anchor is not None:
            C=np.vstack([C,np.eye(self.N)[anchor]])
        self.C=C;self.Z=null_space(C);self.linear_c=self.d@self.B/self.V
        self.H=(self.T.T@self.R+self.R.T@self.T)/(48*self.V)
        self.n0=np.cross(b-a,c-a);self.h0=np.einsum('ij,ij->i',self.n0,a)
        self.dn=np.zeros((len(self.f),3,self.N));self.hlin=np.zeros((len(self.f),self.N))
        for i,(ia,ib,ic) in enumerate(self.f):
            nb=np.cross(self.d,c[i]-a[i]);nc=np.cross(b[i]-a[i],self.d)
            self.dn[i,:,ib]+=nb;self.dn[i,:,ic]+=nc;self.dn[i,:,ia]-=nb+nc
            self.hlin[i]=a[i]@self.dn[i];self.hlin[i,ia]+=self.n0[i]@self.d
        self.nd=self.n0@self.d
        # Signed supporting tetrahedron conditions, affine even for adjacent moving vertices.
        K=[];rhs=[];walls=[]
        for i,(ia,ib,ic) in enumerate(self.f):
            u=self.p[ib]-self.p[ia];v=self.p[ic]-self.p[ia]
            for j in range(self.N):
                if j in (ia,ib,ic):continue
                w=self.p[j]-self.p[ia];beta=np.cross(u,v)@w
                l1=np.cross(v,w)@self.d;l2=np.cross(w,u)@self.d;l3=np.cross(u,v)@self.d
                row=np.zeros(self.N);row[ib]+=l1;row[ic]+=l2;row[j]+=l3;row[ia]-=l1+l2+l3
                fac=np.linalg.norm(row)
                if fac<1e-16:
                    assert beta<=1e-10;continue
                K.append(row/fac);rhs.append(-beta/fac);walls.append((int(i),int(j)))
        self.K=np.array(K);self.rhs=np.array(rhs);self.walls=walls
        self.KZ=self.K@self.Z
        assert self.rhs.min()>-1e-10
    def points(self,s):
        shift=self.linear_c@s+s@self.H@s
        return self.p+(s-shift)[:,None]*self.d
    def loss(self,z,wq=1.,power=1.):
        s=self.Z@z;cg=self.linear_c+2*self.H@s;p=self.points(s)
        n=self.n0+np.einsum('ikj,j->ik',self.dn,s)
        h=self.h0+self.hlin@s-self.nd*(self.linear_c@s+s@self.H@s)
        q=n/h[:,None]
        P,PG=bars(p,self.ed,True);Q,QG=bars(q,self.dual,True)
        v=0;g=np.zeros(self.N)
        for (dep,_,_),gp in zip(P,PG):
            v+=dep**power;gs=gp@self.d;g+=power*dep**(power-1)*(gs-gs.sum()*cg)
        for (dep,_,_),gq in zip(Q,QG):
            v+=wq*dep**power
            a=np.einsum('ik,ikj->j',gq/h[:,None],self.dn)
            b=np.einsum('ij,ij->i',gq,n)/h**2
            gs=a-b@self.hlin+(b@self.nd)*cg
            g+=wq*power*dep**(power-1)*gs
        return v,self.Z.T@g
    def optimize(self,limit=.3,weight=2.,maxiter=250):
        # Keep original chamber strictly inside numerical tolerances, rational endpoint later audited exactly.
        eps=np.minimum(1e-10,self.rhs*.001)
        con=[LinearConstraint(self.KZ,-np.inf,self.rhs-eps),LinearConstraint(self.Z,-limit,limit)]
        z=np.zeros(self.Z.shape[1]);initial=self.loss(z,weight)
        out=minimize(lambda zz:self.loss(zz,weight),z,jac=True,method='SLSQP',constraints=con,
                     options=dict(maxiter=maxiter,ftol=2e-12,disp=False))
        s=self.Z@out.x;p=self.points(s)
        return p,dict(success=bool(out.success),message=out.message,iterations=int(out.nit),fun=float(out.fun),initial=float(initial[0]),maxs=float(abs(s).max()),chamber_slack=float((self.rhs-self.K@s).min()),linear_residual=float(abs(self.C@s).max()),reported=report(p,self.f),s=s.tolist(),d=self.d.tolist())

if __name__=='__main__':
    from scipy.optimize._numdiff import approx_derivative
    dat=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text());p=np.array(dat['points'])/dat['denominator']
    print('BASE',report(p),flush=True)
    chart=Chart(p,[1,2,3]);z=np.zeros(chart.Z.shape[1]);v,g=chart.loss(z)
    gn=approx_derivative(lambda zz:chart.loss(zz)[0],z,method='3-point').ravel()
    print('gradient_error',abs(g-gn).max(),'dof',chart.Z.shape[1],flush=True)
    s=chart.Z@np.random.default_rng(8701).normal(0,1e-5,chart.Z.shape[1]);pp=chart.points(s)
    print('chart_mass_check',mass(pp,chart.f),flush=True)
