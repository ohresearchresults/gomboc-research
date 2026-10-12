# material-0e782a6e4b40

AI research material

---

# J89 minimal exact-input numerical continuation pack

All required complete source units for a successor starting from J89_C444_G10_MINIMAL76. Extract with J88H_EXTRACT.py, then run python continue89.py. The entrypoint defaults are proposed, not a claimed completed run. Own-centroid reconstruction and eventual exact certification remain essential. No old optimizer archive or FULL76 dependency.

<!-- BEGIN UNIT {"bytes": 7146, "name": "parallel.py", "sha256": "16fd7f6c76dea98e28e8fc59df14a622c16954e01521c7e56b4114862fe78b45"} -->
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
<!-- END UNIT parallel.py -->

<!-- BEGIN UNIT {"bytes": 3296, "name": "witness.py", "sha256": "39a5230e2ed16be12077ef500816eea6fd4aa76580295744c0a3a341c00e7dd3"} -->
"""Finite parallel-chart optimization with all nonstable-facet guards."""
import numpy as np
from scipy.optimize import minimize,LinearConstraint,NonlinearConstraint
from parallel import Chart,report,mass,ROOT
import json

def scores(x):
    rad=np.einsum('ij,ij->i',x,x);val=x@x.T/rad[:,None]-1
    np.fill_diagonal(val,-np.inf);j=val.argmax(axis=1)
    f=val[np.arange(len(x)),j];G=np.zeros((len(x),len(x),3))
    for i,k in enumerate(j):
        G[i,i]+=x[k]/rad[i]-2*np.dot(x[i],x[k])/rad[i]**2*x[i]
        G[i,k]+=x[i]/rad[i]
    return f,G,j

def witnesses(c,z):
    s=c.Z@z;cg=c.linear_c+2*c.H@s;p=c.points(s)
    n=c.n0+np.einsum('ikj,j->ik',c.dn,s)
    h=c.h0+c.hlin@s-c.nd*(c.linear_c@s+s@c.H@s)
    q=n/h[:,None]
    fp,Gp,jp=scores(p);fq,Gq,jq=scores(q)
    gp=Gp@c.d;gp-=gp.sum(axis=1)[:,None]*cg
    dh=c.hlin-c.nd[:,None]*cg
    dq=c.dn/h[:,None,None]-n[:,:,None]*dh[:,None,:]/h[:,None,None]**2
    gq=np.einsum('afk,fkj->aj',Gq,dq)
    return fp,fq,gp@c.Z,gq@c.Z,jp,jq

def optimize(c,limit=.6,maxiter=500,qweight=1.,eps=1e-7,guards=True,start=None):
    z=np.zeros(c.Z.shape[1]) if start is None else start
    fp,fq,*_=witnesses(c,z);rootp=int(np.argmin(fp));rootq=int(np.argmin(fq))
    ip=np.arange(c.N)!=rootp;iq=np.arange(len(c.f))!=rootq
    def fun(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        loss=np.minimum(fp[ip]-eps,0);lq=np.minimum(fq[iq]-eps,0)
        rootlp=max(fp[rootp]+eps,0);rootlq=max(fq[rootq]+eps,0)
        v=loss@loss+qweight*(lq@lq)+rootlp**2+qweight*rootlq**2
        gg=2*loss@gp[ip]+2*qweight*lq@gq[iq]+2*rootlp*gp[rootp]+2*qweight*rootlq*gq[rootq]
        return v,gg
    def qguards(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        return np.r_[fq[iq]-eps,-fq[rootq]-eps,-fp[rootp]-eps]
    def qguardsjac(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        return np.vstack([gq[iq],-gq[rootq],-gp[rootp]])
    con=[LinearConstraint(c.KZ,-np.inf,c.rhs-np.minimum(1e-9,c.rhs*.001)),LinearConstraint(c.Z,-limit,limit)]
    if guards:con.append(NonlinearConstraint(qguards,0,np.inf,jac=qguardsjac))
    out=minimize(fun,z,jac=True,method='SLSQP',constraints=con,
                 options=dict(maxiter=maxiter,ftol=1e-15,disp=False))
    s=c.Z@out.x;pp=c.points(s);fp,fq,*_=witnesses(c,out.x)
    res=dict(success=bool(out.success),message=out.message,iterations=int(out.nit),fun=float(out.fun),
             pviolations=int((fp[ip]<eps).sum()),qviolations=int((fq[iq]<eps).sum()),
             rootp=rootp,rootq=rootq,minp=float(fp[ip].min()),minq=float(fq[iq].min()),
             slack=float((c.rhs-c.K@s).min()),maxs=float(abs(s).max()),s=s.tolist(),d=c.d.tolist(),reported=report(pp,c.f))
    return pp,res

if __name__=='__main__':
    dat=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text());p=np.array(dat['points'])/dat['denominator']
    for i,d in enumerate([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,0,1],[-1,1,1]]):
        c=Chart(p,d);pp,r=optimize(c,limit=.7,maxiter=250,eps=1e-7)
        print(i,d,{k:r[k] for k in r if k not in ['s','d','reported']},'P',[(round(x[0],10),x[1]) for x in r['reported']['P']], 'Q', [(round(x[0],10),x[1]) for x in r['reported']['Q']],flush=True)
        np.savez(ROOT/f'witness_{i}.npz',points=pp,s=r['s'],d=d)
        (ROOT/f'witness_{i}.json').write_text(json.dumps(r,indent=2)+'\n')
<!-- END UNIT witness.py -->

<!-- BEGIN UNIT {"bytes": 4455, "name": "hlive88.py", "sha256": "816b25ce76a82eb2683ab1fda672e2452848923981306321352f8650af9c5e9e"} -->
"""Actual homogeneous primal body represented by independently offset H planes.
For <=85 planes every bounded 3D result has E<=3F-6<=249. Numerical candidates
must still receive an exact maximal-facet, own-centroid and full weak census.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from scipy.spatial import ConvexHull,cKDTree
from parallel import bars
from witness import scores

class HLive:
 penalty_tau=1e-6
 penalty_weight=.001
 def __init__(self,n,h,merge_tol=1e-12):
  self.n=np.array(n,float);self.h=np.array(h,float);self.K=len(h)
  if min(h)<=0:raise ValueError('nonpositive offset')
  dual=ConvexHull(self.n/self.h[:,None]);self.tr=dual.simplices.copy();N=self.n[self.tr]
  inv=np.linalg.inv(N);raw=np.einsum('vij,vj->vi',inv,self.h[self.tr])
  par=np.arange(len(raw))
  def root(i):
   while par[i]!=i:par[i]=par[par[i]];i=par[i]
   return i
  for a,b in cKDTree(raw).query_pairs(merge_tol):
   a,b=root(a),root(b)
   if a!=b:par[b]=a
  ids=sorted({root(i) for i in range(len(raw))});mp={a:j for j,a in enumerate(ids)}
  index=np.array([mp[root(i)] for i in range(len(raw))]);self.praw=raw[ids];self.inv=inv[ids];self.tr=self.tr[ids]
  incidence=[set() for _ in ids]
  for r,v in enumerate(index):incidence[v].update(dual.simplices[r])
  faces=[];active=[]
  for i in sorted(dual.vertices):
   vv=[j for j,a in enumerate(incidence) if i in a]
   p=self.praw[vv];center=p.mean(axis=0);nn=self.n[i]/np.linalg.norm(self.n[i])
   basis=np.eye(3)[np.argmin(abs(nn))];u=np.cross(nn,basis);u/=np.linalg.norm(u);v=np.cross(nn,u)
   order=np.argsort(np.arctan2((p-center)@v,(p-center)@u));f=np.array(vv)[order].tolist()
   faces.append(f);active.append(i)
  self.faces=faces;self.active=np.array(active)
  self.V=0.;M=np.zeros(3);edges=set();self.area=np.zeros(self.K);fc=np.zeros((self.K,3));self.face2=np.zeros((self.K,3,3));self.fc=fc
  for i,f in zip(active,faces):
   for a,b in zip(f,f[1:]+f[:1]):edges.add(tuple(sorted((a,b))))
   a=self.praw[f[0]];aa=0.;cm=np.zeros(3)
   for j in range(1,len(f)-1):
    b,c=self.praw[f[j]],self.praw[f[j+1]];D=np.dot(a,np.cross(b,c));self.V+=D/6;M+=D*(a+b+c)/24
    ar=np.dot(np.cross(b-a,c-a),self.n[i])/(2*np.dot(self.n[i],self.n[i]));aa+=ar;cm+=ar*(a+b+c)/3;sv=a+b+c;self.face2[i]+=ar*(np.outer(sv,sv)+np.outer(a,a)+np.outer(b,b)+np.outer(c,c))/12
   if aa<=0:raise ValueError('invalid face orientation')
   self.area[i]=aa;fc[i]=cm/aa
  self.g=M/self.V;self.p=self.praw-self.g;self.ed=np.array(sorted(edges));self.Jg=(self.area[:,None]*(fc-self.g)/self.V).T
  qden=self.h-self.n@self.g
  if min(qden)<=0:raise ValueError('own centre outside H')
  self.q=self.n/qden[:,None];self.qden=qden
  self.fp,self.Gp,self.jp=scores(self.p);self.fq,self.Gq,self.jq=scores(self.q)
  self.rp=np.flatnonzero(self.fp<0);self.rq=np.flatnonzero(self.fq<0)
  self.P,self.PG=bars(self.p,self.ed,True)
 def pull(self,G):
  out=np.zeros(self.K)
  for i in range(len(self.p)):
   out[self.tr[i]]+=G[i]@self.inv[i]
  out-=G.sum(axis=0)@self.Jg
  return out
 def objective(self):
  tau=self.penalty_tau;weight=self.penalty_weight
  value=sum(a[0]+weight*a[0]/(a[0]+tau) for a in self.P)
  G=sum(((1+weight*tau/(a[0]+tau)**2)*g for a,g in zip(self.P,self.PG)),np.zeros_like(self.p))
  return value,self.pull(G)
 def qjac(self):
  a=np.sum(self.Gq*self.n,axis=-1)/(self.qden**2)
  return -a@(np.eye(self.K)-self.n@self.Jg)
 def summary(self):
  return dict(V=len(self.p),E=len(self.ed),F=len(self.active),C=2*len(self.ed),volume=float(self.V),centroid=self.g.tolist(),S=len(self.rq),U=len(self.rp),P=self.P,root_planes=self.rq.tolist(),roots=self.rp.tolist(),min_nonstable=float(np.delete(self.fq,self.rq).min()))

if __name__=='__main__':
 from pathlib import Path
 from fractions import Fraction as R
 import json
 root=Path(__file__).resolve().parent;data=json.loads((root/'J88_COFACIAL_B_EXACT_INPUT.json').read_text());rep=json.loads((root/'J88_COFACIAL_B_EXACT_EXACT.json').read_text())
 p=np.array([[float(R(x)) for x in a] for a in data['points']]);g=np.array([float(R(x)) for x in rep['centroid']]);n=[]
 for f in rep['facets']:
  no=np.cross(p[f[1]]-p[f[0]],p[f[2]]-p[f[0]]);n.append(no/np.dot(no,p[f[0]]-g))
 n=np.array(n);h=np.ones(len(n));c=HLive(n,h)
 print('BASE',c.summary(),flush=True)
 (root/'H88_BASE_NUMERIC.json').write_text(json.dumps({'normals':n.tolist(),'offsets':h.tolist(),'source':'J88_COFACIAL_B_EXACT'},indent=2)+'\n')
<!-- END UNIT hlive88.py -->

<!-- BEGIN UNIT {"bytes": 2552, "name": "polar_live88.py", "sha256": "39a402a880df17cb4b9833c0d41ce7661033c83b53fe3dc64cd6f02de4ef20c4"} -->
"""Independent polar-point (support-normal) derivatives for actual homogeneous mass.
Physical body is intersection n_i.x<=1, at most83 planes => E<=243.
Inputs n are not assumed to have zero physical centroid: all derivatives use
actual volume integrals. S1 centered-normal constraints need exact own g=0,
which is imposed numerically and must be audited exactly on a rational endpoint.
"""
import numpy as np
from hlive88 import HLive
from witness import scores
class PolarLive(HLive):
 def __init__(self,n):
  super().__init__(n,np.ones(len(n)),merge_tol=1e-12)
  # Jn[i,a,b] = derivative of centroid component a w.r.t normal i component b.
  self.Jn=-(self.face2-self.area[:,None,None]*self.g[None,:,None]*self.fc[:,None,:])/self.V
 def pulln(self,G):
  out=np.zeros_like(self.n)
  for i in range(len(self.p)):
   vals=G[i]@self.inv[i]
   out[self.tr[i]]-=vals[:,None]*self.praw[i][None,:]
  out-=np.einsum('a,iab->ib',G.sum(axis=0),self.Jn)
  return out
 def objective_n(self):
  tau=self.penalty_tau;weight=self.penalty_weight
  val=sum(d[0]+weight*d[0]/(d[0]+tau) for d in self.P)
  G=sum(((1+weight*tau/(d[0]+tau)**2)*g for d,g in zip(self.P,self.PG)),np.zeros_like(self.p))
  return val,self.pulln(G)
 def center_jac(self):return self.Jn.transpose(1,0,2).reshape(3,-1)
 def volume_grad(self):return -self.area[:,None]*self.fc
if __name__=='__main__':
 import json
 from pathlib import Path
 root=Path(__file__).resolve().parent;d=json.loads((root/'H88_BASE_NUMERIC.json').read_text());n=np.array(d['normals']);c=PolarLive(n)
 rng=np.random.default_rng(880726);delta=rng.normal(size=n.shape);delta/=np.linalg.norm(delta);nn=n+rng.normal(0,1e-5,n.shape);c=PolarLive(nn)
 PolarLive.penalty_weight=0
 c=PolarLive(nn);grad=c.objective_n()[1];jg=c.center_jac()@delta.ravel();jv=np.sum(c.volume_grad()*delta)
 report=[]
 for hh in [1e-6,1e-7,1e-8]:
  p,m=PolarLive(nn+hh*delta),PolarLive(nn-hh*delta)
  row={'step':hh,'centroid_error':float(max(abs((p.g-m.g)/(2*hh)-jg))),'volume_error':float(abs((p.V-m.V)/(2*hh)-jv)),'P_error':float(abs((p.objective_n()[0]-m.objective_n()[0])/(2*hh)-np.sum(grad*delta)))};report.append(row);print('NORMAL_GRAD',row)
 (root/'POLAR88_GRADIENT.json').write_text(json.dumps({'seed':880726,'rows':report},indent=2)+'\n')

def qjac_n(self):
 """Jacobian of each global polar outgoing score at the true own centroid."""
 a=np.einsum('ijk,jk->ij',self.Gq,self.n)/(self.qden[None,:]**2)
 return self.Gq/self.qden[None,:,None]+a[:,:,None]*self.g[None,None,:]+np.einsum('ic,jcb->ijb',a@self.n,self.Jn)
PolarLive.qjac_n=qjac_n
<!-- END UNIT polar_live88.py -->

<!-- BEGIN UNIT {"bytes": 4511, "name": "polar_free88.py", "sha256": "d4d6e5aaa5c93536437bcbb47343a68da5fa6c8b21e5fa602c4e516fa41304e8"} -->
"""Free support normals with analytically pulled-back actual-centroid S1 guards.
No reference-centre condition and no nonlinear mass-equality solve is used: the
uniform-volume centroid is integrated on every evaluation, with its full shape
Jacobian in every primal and polar derivative. This is the translation gauge
quotient of the centered-normal problem, not a change in physical density.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,time,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,Bounds,NonlinearConstraint
from polar_live88 import PolarLive
from hlive88 import HLive
ROOT=Path(__file__).resolve().parent
class Budget(Exception):pass
class FreeNormals:
 def __init__(self,n,h,trust=.003,eps=1e-10,max_seconds=20.):
  c=HLive(n,h);self.n=n/(h-n@c.g)[:,None];self.trust=trust;self.last=None;self.c=None;self.evals=0;self.start=None;self.max_seconds=max_seconds
  c=self.at(self.n);self.root=int(c.rq[0]);self.iq=np.arange(len(n))!=self.root;self.target=np.maximum(eps,np.minimum(1e-5,c.fq[self.iq]*.03));self.rt=min(1e-5,-c.fq[self.root]*.03);self.hist=[];self.best=[c.objective_n()[0],self.n.copy(),0];self.best121=None
 def at(self,n):
  if self.start is not None and time.monotonic()-self.start>self.max_seconds:raise Budget('Bounded numerical solve stopped; no optimum claim')
  if self.last is None or not np.array_equal(n,self.last):self.last=n.copy();self.c=PolarLive(n);self.evals+=1
  return self.c
 def nz(self,z):return self.n+self.trust*z.reshape(self.n.shape)
 def fun(self,z):
  v,g=self.at(self.nz(z)).objective_n();return v/self.trust,g.ravel()
 def guards(self,z):
  c=self.at(self.nz(z));return np.r_[c.fq[self.iq]-self.target,-c.fq[self.root]-self.rt]/self.trust
 def gj(self,z):
  j=self.at(self.nz(z)).qjac_n();return np.concatenate([j[self.iq],-j[self.root][None]]).reshape(len(self.n),-1)
 def cb(self,z):
  n=self.nz(z);c=self.at(n);v=c.objective_n()[0];feas=len(c.rq)==1 and min(self.guards(z)*self.trust)>-1e-12
  if feas and len(c.rp)<=2 and (self.best121 is None or v<self.best121[0]):self.best121=[v,n.copy()]
  if feas and v<self.best[0]:
   self.best=[v,n.copy(),self.best[2]+1];self.hist.append({'evaluation':self.evals,'value':float(v),'actual':c.summary(),'normals':n.tolist()});print('FBEST',self.best[2],v,'S/U',len(c.rq),len(c.rp),'maxP',max((b[0] for b in c.P),default=0.),flush=True)
 def run(self,iterations=160):
  con=NonlinearConstraint(self.guards,0,np.inf,jac=self.gj);self.start=st=time.monotonic()
  try:
   out=minimize(self.fun,np.zeros(self.n.size),jac=True,bounds=Bounds(-1,1),constraints=[con],method='SLSQP',callback=self.cb,options={'maxiter':iterations,'ftol':1e-11,'disp':False})
  except Budget as e:
   from types import SimpleNamespace
   out=SimpleNamespace(success=False,message=str(e),nit=-1,x=((self.best[1]-self.n)/self.trust).ravel())
  self.start=None;self.cb(out.x);self.final=self.nz(out.x);return self.best[1],{'success':bool(out.success),'message':out.message,'nit':int(out.nit),'seconds':time.monotonic()-st,'best':self.best[0],'updates':self.best[2],'actual':PolarLive(self.best[1]).summary(),'final':PolarLive(self.final).summary(),'history':self.hist,'tau':PolarLive.penalty_tau,'weight':PolarLive.penalty_weight,'trust':self.trust,'target':self.target.tolist(),'max_seconds':self.max_seconds}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='CANCEL88_CANDIDATE1.json');ap.add_argument('--prefix',default='PF88');ap.add_argument('--trust',type=float,default=.003);ap.add_argument('--iterations',type=int,default=160);ap.add_argument('--tau',type=float,default=1e-6);ap.add_argument('--weight',type=float,default=.001);ap.add_argument('--eps',type=float,default=1e-10);ap.add_argument('--seconds',type=float,default=20.);args=ap.parse_args()
 PolarLive.penalty_tau=args.tau;PolarLive.penalty_weight=args.weight
 d=json.loads((ROOT/args.input).read_text());pr=FreeNormals(np.array(d['normals']),np.array(d['offsets']),args.trust,args.eps,args.seconds);nn,r=pr.run(args.iterations)
 for tag,v in [('BEST',nn),('FINAL',pr.final)]+([('121',pr.best121[1])] if pr.best121 is not None else []):(ROOT/(args.prefix+'_'+tag+'.json')).write_text(json.dumps({'normals':v.tolist(),'offsets':[1.]*len(v)},indent=2)+'\n')
 (ROOT/(args.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n');print('FRESULT',{k:v for k,v in r.items() if k not in ['history','target']},flush=True)
<!-- END UNIT polar_free88.py -->

<!-- BEGIN UNIT {"bytes": 3977, "name": "retract88.py", "sha256": "df414afd0e5716fa8c82d23124e31f5cb2f12024abcb6b4f8bdd9d9b3db977e4"} -->
"""Own-S1 restoration with an acyclic radial envelope and actual-mass Jacobian.
A label-setting envelope chooses a full-root polar witness tree (not independent
best arrows that can cycle). Small support-normal corrections solve a scaled
linear Chebyshev projection. Every accepted point is recounted at its own mass.
This is a finite numerical method, not a guarantee of global convergence.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,argparse,heapq
import numpy as np
from scipy.optimize import linprog
from polar_live88 import PolarLive
from hlive88 import HLive
ROOT=Path(__file__).resolve().parent

def envelope(q,root,eta=1e-11):
 rr=np.linalg.norm(q,axis=1);unit=q/rr[:,None];cs=unit@unit.T;old=1/rr;label=np.full(len(q),np.inf);label[root]=old[root];par=np.full(len(q),-1);seen=np.zeros(len(q),bool);heap=[(label[root],root)]
 while heap:
  val,j=heapq.heappop(heap)
  if seen[j] or val!=label[j]:continue
  seen[j]=True
  for i in range(len(q)):
   if seen[i] or cs[i,j]<=0:continue
   new=max(old[i],val/cs[i,j]*(1+eta))
   if new<label[i]:label[i]=new;par[i]=j;heapq.heappush(heap,(new,i))
 assert seen.all();return par,label,old

def fixed(c,parent,root):
 K=len(c.n);ids=[i for i in range(K) if i!=root];f=[];G=np.zeros((K-1,K,3))
 for l,i in enumerate(ids):
  j=parent[i];rad=c.q[i]@c.q[i];ij=c.q[i]@c.q[j];f.append(ij/rad-1);G[l,i]=c.q[j]/rad-2*ij*c.q[i]/rad**2;G[l,j]+=c.q[i]/rad
 a=np.einsum('ijk,jk->ij',G,c.n)/(c.qden[None,:]**2)
 J=G/c.qden[None,:,None]+a[:,:,None]*c.g[None,None,:]+np.einsum('ic,jcb->ijb',a@c.n,c.Jn)
 return np.array(f),J.reshape(K-1,-1)

def restore(n,eps=1e-8,maxiter=12):
 c=PolarLive(n);root=int(np.argmax(np.sum(c.q*c.q,axis=1)));history=[];initial=c.summary()
 for it in range(maxiter):
  c=PolarLive(n);good=np.delete(c.fq,root).min()
  if len(c.rq)==1 and c.rq[0]==root and good>=eps:return n,{'success':True,'initial':initial,'actual':c.summary(),'history':history,'eps':eps}
  parent,label,old=envelope(c.q,root);f,J=fixed(c,parent,root);target=2*eps
  scale=max(1e-8,10*np.max(np.maximum(target-f,0)/np.maximum(np.sum(abs(J),axis=1),1e-15)))
  A=np.zeros((len(f)+2*n.size,n.size+1));b=np.zeros(len(A));A[:len(f),:-1]=-J;b[:len(f)]=(f-target)/scale
  A[len(f):len(f)+n.size,:-1]=np.eye(n.size);A[len(f)+n.size:,:-1]=-np.eye(n.size);A[len(f):,-1]=-1
  cost=np.zeros(n.size+1);cost[-1]=1
  out=linprog(cost,A_ub=A,b_ub=b,bounds=[(-1,1)]*n.size+[(0,1)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not out.success:
   history.append({'iteration':it,'success':False,'message':out.message,'scale':scale,'min_fixed':float(f.min())});break
  delta=scale*out.x[:-1].reshape(n.shape);nn=n+delta;d=PolarLive(nn)
  rec={'iteration':it,'scale':float(scale),'correction_infinity':float(abs(delta).max()),'min_fixed_before':float(f.min()),'min_fixed_after':float(fixed(d,parent,root)[0].min()),'envelope_relative_max':float(max(label/old-1)),'parent':parent.tolist(),'actual':d.summary()};history.append(rec);print('RESTORE',it,rec['correction_infinity'],rec['min_fixed_before'],rec['min_fixed_after'],'S/U',len(d.rq),len(d.rp),flush=True)
  n=nn
 return n,{'success':False,'initial':initial,'actual':PolarLive(n).summary(),'history':history,'eps':eps}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='PF88_FINAL.json');ap.add_argument('--prefix',default='REST88');ap.add_argument('--eps',type=float,default=1e-8);args=ap.parse_args();d=json.loads((ROOT/args.input).read_text());n=np.array(d['normals'])/np.array(d['offsets'])[:,None];nn,r=restore(n,args.eps)
 (ROOT/(args.prefix+'_H.json')).write_text(json.dumps({'normals':nn.tolist(),'offsets':[1.]*len(nn)},indent=2)+'\n');(ROOT/(args.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n');print('RESTORED',{k:v for k,v in r.items() if k not in ['history','initial']},flush=True)
<!-- END UNIT retract88.py -->

<!-- BEGIN UNIT {"bytes": 4762, "name": "hpolicy88.py", "sha256": "37555c44c3c9ad000791876284b0488a05b8ce60a84a53613c91259c470cc881"} -->
"""Fixed-normal centered H equilibrium cells: linear geometric/witness nomination.
For a simple vertex x_T=N_T^-1 a_T, its normal-cone coefficients are
alpha_T=(N_T N_T^T)^-1 a_T. Thus non-U can be enforced by one negative
coefficient, linear in a. Non-S polar witnesses are linear in a too.
This is a numerical MILP, NOT a proof of feasibility or physical centering.
All retained triple intersections obey every support halfspace; actual mass
is imposed only to first order in this nomination and must be restored later.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,argparse,time
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,csc_matrix
from hlive88 import HLive
ROOT=Path(__file__).resolve().parent

def cells(n,a):
 c=HLive(n,a,merge_tol=1e-14);K=len(a);geom=[];qa=[];ua=[]
 for T,iv in zip(c.tr,c.inv):
  for j in range(K):
   if j in T:continue
   row=np.eye(K)[j];row[T]-=n[j]@iv
   norm=np.linalg.norm(row)
   if norm>1e-12:geom.append(row/norm)
  G=iv.T@iv;rr=np.zeros((3,K));rr[:,T]=-G;rr/=np.linalg.norm(rr,axis=1)[:,None];ua.append(rr)
 rootq=int(c.rq[0])
 for i in range(K):
  if i==rootq:continue
  j=c.jq[i];row=np.zeros(K);row[i]=n[i]@n[j];row[j]=-n[i]@n[i];row/=np.linalg.norm(row);qa.append(row)
 return c,np.array(geom),np.array(qa),np.array(ua),rootq

def nominate(n,h,trust=.01,limit=20.,all_disjunctions=False,linear_mass=True):
 c=HLive(n,h);a=h-n@c.g;c,geo,qa,ua,rootq=cells(n,a);K=len(a);rootp=int(np.argmax(np.einsum('ij,ij->i',c.p,c.p)))
 vv=np.einsum('vjk,k->vj',ua,a);choice=np.argmax(vv,axis=1)
 bad=[i for i in range(len(c.p)) if i!=rootp and (max(vv[i])<=0 or all_disjunctions)]
 fixed=[i for i in range(len(c.p)) if i!=rootp and i not in bad]
 m=K+1+3*len(bad);rowdata=[];lower=[];upper=[]
 def add(vals,lo=-np.inf,hi=np.inf):rowdata.append(vals);lower.append(lo);upper.append(hi)
 for row in geo:add({j:float(v) for j,v in enumerate(row) if v},lo=float(-row@a/trust))
 for row in list(qa)+[ua[i,choice[i]] for i in fixed]:
  d={j:float(v) for j,v in enumerate(row) if v};d[K]=-1;add(d,lo=float(-row@a/trust))
 for b,i in enumerate(bad):
  for k,row in enumerate(ua[i]):
   val=float(row@a/trust);M=float(np.sum(abs(row))+abs(val)+1.)
   d={j:float(v) for j,v in enumerate(row) if v};d[K]=-1;d[K+1+3*b+k]=-M;add(d,lo=-val-M)
  add({K+1+3*b+k:1. for k in range(3)},lo=1.,hi=1.)
 if linear_mass:
  for row in c.Jg:add({j:float(v) for j,v in enumerate(row) if v},lo=0.,hi=0.)
 add({rootq:1.},lo=0.,hi=0.)
 A=lil_matrix((len(rowdata),m))
 for i,d in enumerate(rowdata):
  for j,v in d.items():A[i,j]=v
 A=csc_matrix(A);cost=np.zeros(m);cost[K]=-1.;integ=np.zeros(m);integ[K+1:]=1
 lo=np.r_[np.maximum(-1,(.05-a)/trust),-1000.,np.zeros(3*len(bad))];hi=np.r_[np.ones(K),1.,np.ones(3*len(bad))]
 st=time.monotonic();out=milp(cost,integrality=integ,bounds=Bounds(lo,hi),constraints=LinearConstraint(A,np.array(lower),np.array(upper)),options={'time_limit':limit,'mip_rel_gap':1e-8,'presolve':True})
 rep={'status':int(out.status),'message':out.message,'seconds':time.monotonic()-st,'trust':trust,'rootp':rootp,'rootq':rootq,'bad':bad,'fixed_count':len(fixed),'constraints':len(rowdata),'variables':m,'all_disjunctions':all_disjunctions,'linear_mass':linear_mass,'base':c.summary()}
 if out.x is not None:
  a1=a+trust*out.x[:K];rep['margin']=float(trust*out.x[K]);rep['linear_residual']=float(max(abs(c.Jg@(a1-a))));rep['true']=HLive(n,a1).summary();rep['selected']={str(i):int(np.argmax(out.x[K+1+3*b:K+4+3*b])) for b,i in enumerate(bad)};rep['fixed']={str(i):int(choice[i]) for i in fixed};rep['offsets']=a1.tolist();rep['base_offsets']=a.tolist();rep['min_geometry']=float((geo@a1).min());rep['min_constraint']=float(np.min((A@out.x-np.array(lower))[np.isfinite(lower)]))
 return rep
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='HC88_BEST.json');ap.add_argument('--prefix',default='HP88');ap.add_argument('--trust',type=float,default=.01);ap.add_argument('--seconds',type=float,default=20);ap.add_argument('--all',action='store_true');ap.add_argument('--no-linear-mass',action='store_true');args=ap.parse_args()
 dat=json.loads((ROOT/args.input).read_text());n=np.array(dat['normals']);h=np.array(dat['offsets']);r=nominate(n,h,args.trust,args.seconds,args.all,not args.no_linear_mass)
 print('POLICY_RESULT',{k:v for k,v in r.items() if k not in ['offsets','base_offsets','fixed','selected','base']},flush=True)
 (ROOT/(args.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n')
 if 'offsets' in r:(ROOT/(args.prefix+'_H.json')).write_text(json.dumps({'normals':n.tolist(),'offsets':r['offsets']},indent=2)+'\n')
<!-- END UNIT hpolicy88.py -->

<!-- BEGIN UNIT {"bytes": 4080, "name": "cleanall88.py", "sha256": "7a903f01883df63ec68f53f75d73ca29ed2d3f0879ea64b19826f91a11ab20ab"} -->
"""Full small-basin cleanup via a two-root edge forest in fixed-normal H space.
Unlike independent best-edge choices, the multi-source envelope is acyclic.
All true non-root vertices receive a linear cone exclusion, including positive
bars below a numerical persistence cutoff. Recount own mass after finite steps.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,argparse,heapq
import numpy as np
from scipy.optimize import linprog
from hlive88 import HLive
from hpolicy88 import cells
ROOT=Path(__file__).resolve().parent

def tree(c,roots,eta=1e-12):
 rad=np.linalg.norm(c.p,axis=1);u=c.p/rad[:,None];old=1/rad;label=np.full(len(rad),np.inf);parent=np.full(len(rad),-1);seen=np.zeros(len(rad),bool);adj=[[] for _ in rad];heap=[]
 for a,b in c.ed:adj[a].append(b);adj[b].append(a)
 for i in roots:label[i]=old[i];heapq.heappush(heap,(label[i],i))
 while heap:
  val,j=heapq.heappop(heap)
  if seen[j] or val!=label[j]:continue
  seen[j]=True
  for i in adj[j]:
   if seen[i] or i in roots:continue
   cs=u[i]@u[j]
   if cs<=0:continue
   v=max(old[i],val/cs*(1+eta))
   if v<label[i]:label[i]=v;parent[i]=j;heapq.heappush(heap,(v,i))
 assert seen.all();return parent,label/old-1

def cleanup(n,h,trust=.0001,eps=1e-10,keep_policy=False):
 c=HLive(n,h);a=h-n@c.g;c,geo,qa,ua,rq=cells(n,a);K=len(a);glob=int(np.argmax(np.sum(c.p*c.p,axis=1)));large=max(c.P,key=lambda b:b[0])[1] if c.P else glob;roots=sorted(set([glob,large]));parent,inc=tree(c,roots);A=[];b=[];labels=[]
 def add(row,target,label):A.append(-row);b.append(float((row@a-target)/trust));labels.append(label)
 for j,row in enumerate(geo):add(row,max(0.,min(float(row@a)*.01,1e-12)),['geometry',j])
 for j,row in enumerate(qa):add(row,max(eps,min(float(row@a)*.03,1e-8)),['nonS',j])
 for i in range(len(c.p)):
  if i in roots:continue
  j=int(parent[i]);missing=[k for k,t in enumerate(c.tr[i]) if t not in c.tr[j]]
  if len(missing)!=1:raise ValueError(('non-simple edge not supported',i,j,c.tr[i],c.tr[j]))
  k=missing[0];row=ua[i,k];add(row,max(eps,min(float(row@a)*.03,1e-7)),['nonU',i,j,k])
 # The global maximum is kept in its cone. The second allowed root is NOT forced to persist.
 for k in range(3):
  row=-ua[glob,k];add(row,max(eps,min(float(row@a)*.03,1e-7)),['globalU',glob,k])
 AA=np.zeros((len(A)+2*K,K+1));bb=np.zeros(len(AA));AA[:len(A),:K]=A;bb[:len(A)]=b;AA[len(A):len(A)+K,:K]=np.eye(K);AA[len(A)+K:,:K]=-np.eye(K);AA[len(A):,-1]=-1
 eq=np.zeros((4,K+1));eq[:3,:K]=c.Jg;eq[3,rq]=1;eq/=np.linalg.norm(eq,axis=1)[:,None];cost=np.zeros(K+1);cost[-1]=1
 out=linprog(cost,A_ub=AA,b_ub=bb,A_eq=eq,b_eq=np.zeros(4),bounds=[(-1,1)]*K+[(0,1)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 r={'success':bool(out.success),'message':out.message,'base':c.summary(),'trust':trust,'eps':eps,'roots_allowed':roots,'parent':parent.tolist(),'max_radial_envelope_increase':float(max(inc)),'constraints':len(A)}
 if out.success:
  hh=a+trust*out.x[:K];r['offsets']=hh.tolist();r['delta']=list(trust*out.x[:K]);r['actual']=HLive(n,hh).summary();r['linear_mass_residual']=float(max(abs(c.Jg@(hh-a))));r['correction_infinity']=float(max(abs(hh-a)))
 if keep_policy:r['_Aub']=np.array(A);r['_bub']=np.array(A)@a+trust*np.array(b);r['_rootq']=rq
 return r
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='REST88_H.json');ap.add_argument('--prefix',default='ALL88');ap.add_argument('--trust',type=float,default=.0001);ap.add_argument('--eps',type=float,default=1e-10);args=ap.parse_args();d=json.loads((ROOT/args.input).read_text());n=np.array(d['normals']);h=np.array(d['offsets']);r=cleanup(n,h,args.trust,args.eps)
 (ROOT/(args.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n');print('ALLCLEAN',{k:v for k,v in r.items() if k not in ['base','offsets','delta','parent']},flush=True)
 if 'offsets' in r:(ROOT/(args.prefix+'_H.json')).write_text(json.dumps({'normals':n.tolist(),'offsets':r['offsets']},indent=2)+'\n')
<!-- END UNIT cleanall88.py -->

<!-- BEGIN UNIT {"bytes": 3150, "name": "repair89.py", "sha256": "9a0fa30152cb6bc6068675f6284ad9447479951dc3b0de718c331a756ff7eb9c"} -->
"""Coupled Chebyshev own-S1 repair, without a rowwise guessed radius cap.
The old rowwise lower bound for linear feasibility is NOT an upper bound on
required joint correction. All decisions here remain floating nomination.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,argparse,time
from pathlib import Path
from scipy.optimize import linprog
from retract88 import envelope,fixed
from polar_live88 import PolarLive
ROOT=Path(__file__).resolve().parent

def linear_minimum(J,f,target):
 m,k=J.shape
 A=np.zeros((m+2*k,k+1));b=np.zeros(m+2*k)
 A[:m,:k]=-J;b[:m]=f-target
 A[m:m+k,:k]=np.eye(k);A[m+k:,:k]=-np.eye(k);A[m:,-1]=-1
 cost=np.zeros(k+1);cost[-1]=1
 fac=np.linalg.norm(A[:m,:k],axis=1);A[:m]/=fac[:,None];b[:m]/=fac
 res=linprog(cost,A_ub=A,b_ub=b,bounds=[(None,None)]*k+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 return res

def restore(n,eps=1e-8,maxiter=30,maxstep=.01,verbose=True):
 c=PolarLive(n);root=int(np.argmax(np.sum(c.q*c.q,axis=1)));hist=[];initial=c.summary();t0=time.monotonic()
 for it in range(maxiter):
  c=PolarLive(n);parent,label,old=envelope(c.q,root);f,J=fixed(c,parent,root);merit=max(0.,float((eps-f).max()))
  if len(c.rq)==1 and c.rq[0]==root and merit<=eps*.05:
   return n,dict(success=True,initial=initial,actual=c.summary(),history=hist,eps=eps)
  out=linear_minimum(J,f,np.full_like(f,eps*2))
  row=dict(iteration=it,LP_success=bool(out.success),message=out.message,merit=merit)
  if not out.success:hist.append(row);break
  delta=out.x[:-1].reshape(n.shape);rho=float(max(abs(delta).ravel()));row['linear_minimum_radius']=rho
  alpha=min(1.,maxstep/max(rho,1e-30));found=False
  for ls in range(20):
   nn=n+alpha*delta
   try:
    d=PolarLive(nn);ff,_=fixed(d,parent,root);newmerit=max(0.,float((eps-ff).max()));found=newmerit<max(eps*.05,merit*(1-.02*alpha))
   except (ValueError,np.linalg.LinAlgError):found=False
   if found:break
   alpha*=.5
  row.update(alpha=alpha,accepted=found)
  if not found:hist.append(row);break
  n=nn;row.update(merit_after=newmerit,actual=d.summary(),parent=parent.tolist())
  hist.append(row)
  if verbose:print('REPAIR89',it,'rho',rho,'alpha',alpha,'merit',merit,newmerit,'S/U',len(d.rq),len(d.rp),flush=True)
 return n,dict(success=False,initial=initial,actual=PolarLive(n).summary(),history=hist,eps=eps)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='FREE89_A_FINAL.json');ap.add_argument('--prefix',default='REPAIR89_A');ap.add_argument('--eps',type=float,default=1e-8);ap.add_argument('--steps',type=int,default=30);ap.add_argument('--maxstep',type=float,default=.01);a=ap.parse_args();d=json.loads((ROOT/a.input).read_text());n=np.array(d['normals'])/np.array(d['offsets'])[:,None];nn,r=restore(n,a.eps,a.steps,a.maxstep)
 (ROOT/(a.prefix+'_H.json')).write_text(json.dumps({'normals':nn.tolist(),'offsets':[1.]*len(nn)},indent=2)+'\n');(ROOT/(a.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n');print('REPAIR_RESULT',r['success'],r['actual'],flush=True)
<!-- END UNIT repair89.py -->

<!-- BEGIN UNIT {"bytes": 3356, "name": "center89.py", "sha256": "34cec8392d38a5efc853d28fa5791ebdc0e3098daf3e984e1bc42169111dd538"} -->
"""Coupled support-cell projection with actual own-centroid recomputation.
Removes the unjustified residual-to-radius guess from center_project88.
A minimum joint correction is solved before testing the nonlinear finite step.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,argparse
from pathlib import Path
from scipy.optimize import linprog
from cleanall88 import cleanup
from hlive88 import HLive
ROOT=Path(__file__).resolve().parent

def joint(A,b,Jg,root):
 m,k=A.shape;mat=np.zeros((m+2*k,k+1));rhs=np.zeros(m+2*k)
 mat[:m,:k]=A;rhs[:m]=b;mat[m:m+k,:k]=np.eye(k);mat[m+k:,:k]=-np.eye(k);mat[m:,-1]=-1
 eq=np.zeros((4,k+1));eq[:3,:k]=Jg;eq[3,root]=1;eq/=np.linalg.norm(eq,axis=1)[:,None]
 norm=np.linalg.norm(mat[:m,:k],axis=1);mat[:m]/=norm[:,None];rhs[:m]/=norm
 scale=max(1e-8,10*max(0.,-float(rhs[:m].min())))
 rhs[:m]/=scale
 cost=np.zeros(k+1);cost[-1]=1
 out=linprog(cost,A_ub=mat,b_ub=rhs,A_eq=eq,b_eq=np.zeros(4),bounds=[(None,None)]*k+[(0,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 if out.x is not None:out.x*=scale;out.fun*=scale
 return out

def project(n,h,trust=.015,eps=1e-9,maxiter=30):
 r=cleanup(n,h,trust,eps,keep_policy=True);A=r.pop('_Aub');b=r.pop('_bub');rq=r.pop('_rootq');hist=[];K=len(h)
 if not r['success']:return h,{'success':False,'initial_projection':r,'history':hist}
 h=np.array(r['offsets'])
 for it in range(maxiter):
  c=HLive(n,h);a=h-n@c.g;res=float(max(A@a-b));hist.append({'iteration':it,'own_linear_violation':res,'actual':c.summary(),'offsets':h.tolist()})
  print('CENTER89',it,'S/U',len(c.rq),len(c.rp),'violation',res,'g',max(abs(c.g)),'P',max((p[0] for p in c.P),default=0.),flush=True)
  if len(c.rq)==1 and len(c.rp)<=2 and res<eps*.5 and np.delete(c.fq,c.rq).min()>0:
   return h,{'success':True,'initial_projection':r,'history':hist,'actual':c.summary()}
  d=HLive(n,a);out=joint(A,b-A@a,d.Jg,rq);hist[-1].update(repair_success=bool(out.success),repair_message=out.message)
  if not out.success:break
  delta=out.x[:K];rho=max(abs(delta));hist[-1]['minimum_linear_radius']=float(rho)
  alpha=min(1.,trust/max(rho,1e-30));found=False
  for ls in range(20):
   hh=a+alpha*delta
   try:
    cc=HLive(n,hh);aa=hh-n@cc.g;newres=float(max(A@aa-b));found=newres<max(eps*.45,res*(1-.02*alpha))
   except (ValueError,np.linalg.LinAlgError):found=False
   if found:break
   alpha*=.5
  hist[-1].update(alpha=alpha,accepted=found)
  if not found:break
  h=hh
 return h,{'success':False,'initial_projection':r,'history':hist,'actual':HLive(n,h).summary()}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='CYCLE89_A_03_RESTORE.json');ap.add_argument('--prefix',default='CENTER89_A');ap.add_argument('--trust',type=float,default=.015);ap.add_argument('--eps',type=float,default=1e-9);ap.add_argument('--steps',type=int,default=30);a=ap.parse_args();d=json.loads((ROOT/a.input).read_text());n=np.array(d['normals']);h=np.array(d['offsets']);hh,r=project(n,h,a.trust,a.eps,a.steps)
 (ROOT/(a.prefix+'_H.json')).write_text(json.dumps({'normals':n.tolist(),'offsets':hh.tolist()},indent=2)+'\n');(ROOT/(a.prefix+'_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n');print('CENTER_RESULT',r['success'],r.get('actual'),flush=True)
<!-- END UNIT center89.py -->

<!-- BEGIN UNIT {"bytes": 3223, "name": "cycle89b.py", "sha256": "8ebc47e283139aaeb748e2f1017d0feda3c9c3fb13871863b546dd0e4260dd15"} -->
"""Finite normal-release / coupled polar repair / actual-mass primal cleanup.
No bounded optimizer success is treated as an exact class certificate.
All checkpoints, final optimizer points, projections and outcomes are retained.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,argparse,time
import numpy as np
from polar_free88 import FreeNormals
from polar_live88 import PolarLive
from hlive88 import HLive
from repair89 import restore
from center89 import project
ROOT=Path(__file__).resolve().parent

def save(name,n,h=None):
 h=np.ones(len(n)) if h is None else h
 (ROOT/(name+'.json')).write_text(json.dumps({'normals':n.tolist(),'offsets':h.tolist()},indent=2)+'\n')

def run(input_file,cycles,prefix,trust,eps,iterations):
 dat=json.loads((ROOT/input_file).read_text());n=np.array(dat['normals']);h=np.array(dat['offsets']);history=[];best=HLive(n,h);bp=max(b[0] for b in best.P);t0=time.monotonic()
 for it in range(cycles):
  tag=f'{prefix}_{it:02d}';print('CYCLE_START',it,'P',bp,'trust',trust,flush=True)
  pr=FreeNormals(n,h,trust,eps/100,35.);nn,r=pr.run(iterations);save(tag+'_FREEBEST',nn);save(tag+'_FREEFINAL',pr.final)
  (ROOT/(tag+'_FREE_REPORT.json')).write_text(json.dumps(r,indent=2)+'\n')
  chosen=pr.final
  # A failed SLSQP final point can be valuable only after real class restoration.
  nr,rr=restore(chosen,eps=eps,maxiter=20,maxstep=.01);save(tag+'_RESTORE',nr)
  (ROOT/(tag+'_RESTORE_REPORT.json')).write_text(json.dumps(rr,indent=2)+'\n')
  rec=dict(cycle=it,trust=trust,restore_success=rr['success'],release_final=r['final'])
  if rr['success']:
   try:
    hh,cr=project(nr,np.ones(len(nr)),trust=.015,eps=eps/100,maxiter=15);cc=HLive(nr,hh)
    save(tag+'_PROJECT',nr,hh);(ROOT/(tag+'_PROJECT_REPORT.json')).write_text(json.dumps(cr,indent=2)+'\n')
    p=max((b[0] for b in cc.P),default=0.);rec.update(project_success=cr['success'],candidate=cc.summary())
    good=cr['success'] and len(cc.rq)==1 and len(cc.rp)<=2 and np.delete(cc.fq,cc.rq).min()>eps/1000 and p<bp-1e-7
    if good:
     n,h=nr,hh;bp=p;best=cc;save(prefix+'_BEST',n,h);trust=min(trust*1.3,.025)
    else:trust=max(trust*.55,.0001)
    rec['accepted']=good
   except (ValueError,np.linalg.LinAlgError) as e:
    rec['error']=repr(e);rec['accepted']=False;trust*=.6
  else:rec['accepted']=False;trust*=.6
  history.append(rec)
  (ROOT/(prefix+'_SUMMARY.json')).write_text(json.dumps({'history':history,'actual':best.summary(),'seconds':time.monotonic()-t0,'input':input_file,'eps':eps,'iterations':iterations},indent=2)+'\n')
  print('CYCLE_RESULT',it,'accepted',rec['accepted'],'P',bp,'S/U',len(best.rq),len(best.rp),'E',len(best.ed),flush=True)
  if len(best.rp)==1:break
 return n,h,history
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',default='PROJ89_B_H.json');ap.add_argument('--cycles',type=int,default=8);ap.add_argument('--prefix',default='CYCLE89');ap.add_argument('--trust',type=float,default=.003);ap.add_argument('--eps',type=float,default=1e-7);ap.add_argument('--iterations',type=int,default=180);a=ap.parse_args();run(a.input,a.cycles,a.prefix,a.trust,a.eps,a.iterations)
<!-- END UNIT cycle89b.py -->

<!-- BEGIN UNIT {"bytes": 4065, "name": "J89_C444_G10_MINIMAL76_H_INPUT.json", "sha256": "6c615d3a9729fdcf5986913ee6d9feace2610ffb491207c092a7ce85da1d20d3"} -->
{"name":"J89_C444_G10_MINIMAL76","planes":[[-9759740520,11025398055,-5009610205,10001651257],[-5122988217,5868306247,-1003478017,5000353431],[-9060609931,10567891131,-6682670930,10002116173],[-7618365170,10939708724,-7593920013,10002115449],[-10387317917,11875734050,-465983767,10000233981],[-6056276262,10743309481,-8895133485,10002290608],[-10031080302,11460997439,-3520006337,10001176878],[-2909201330,-12009987267,-11020368860,10009500344],[-9477754203,11715999538,5660072546,9998208104],[-9014455998,11353850975,7183197252,9997707632],[-1277969332,3128033295,16629522802,9994599860],[-145583606,1504690879,17021738269,9994507222],[-12490184930,8798118883,-1014047624,10001962270],[-7688511915,9640425245,10746515869,9996612134],[-3971703317,3326599352,729073945,3334779054],[-2856469597,-13668445125,-11091172828,10010021050],[-3339322248,4489448367,6030625104,4998063530],[-5639563179,8136655314,13262649952,9995696040],[-4578764434,7121304951,14335874544,9995323920],[-3497421534,5941758234,15266584315,9995014196],[-4390335731,10723130771,-9673525264,10002263245],[-8176893330,10299008887,9628222537,9996951823],[-10064668379,11750829182,4136623939,9998771068],[-1412195669,-7076014817,-5555494239,5005065848],[-10523648960,11815665581,1065916555,9999789034],[-2868848172,3627589912,2812754209,3332438009],[-2397047868,4608339970,16037188934,9994771243],[-10588551374,11619255553,2592036125,9999352039],[-4571308959,5045270843,4100916208,5001000019],[-1146304563,-13617684260,-11373471513,10007524373],[-1262643199,10331500644,-10672947171,10002113880],[-2630359462,10533426740,-10315856027,10002200333],[-1749825805,-13503482600,-11280314418,10009800135],[-246309594,10234223004,-10788191296,10001995549],[798632280,10134118833,-10804533215,10001842159],[2050576536,9890752153,-10789331131,10001664236],[916909346,-17290236405,-8081160756,10002037021],[2081011717,-2066457596,17097465114,9994590963],[9142201427,2008598420,864784230,10002275794],[9152402582,934943987,545588088,10002605013],[5043119142,10146303100,-9174482527,10000634970],[9023277932,-342713569,72608744,10002758255],[5705766996,-10375218021,13605652238,9996178707],[8814979824,-1246719396,-713970155,10003338235],[1002111658,-280655948,17189368722,9994503089],[7173018927,5522927380,2935795328,10001287392],[4216306511,-6146116095,16020434894,9995114511],[7646122315,4630698264,2964279419,10001363297],[8073358867,4003905570,2719496458,10001491606],[4496403810,12938048195,-2942086891,10002886203],[8485675907,3627576623,2125585279,10001751197],[4524787307,1328148551,595478405,5001084551],[8879508182,3287110150,1434567384,10002070753],[2734635512,5461662527,-3891406313,5000014790],[3974826773,-19197172676,-3805560794,10003038846],[5038502961,-8275655890,14987975957,9995581538],[8648213837,797245931,-3960292099,10004109686],[3105042322,-4057841563,16732507504,9994799488],[6388772861,-12402121995,11775305641,9996903319],[4824321001,3732030134,-10372553705,9997577250],[6618207579,-14447490777,9499237310,9997842676],[4455652289,9193505896,-10552637181,10001285205],[8588769190,1908774631,-3104934910,10003710734],[5444701480,-18718267098,223873333,10001481832],[5569547075,11639460993,-6388860021,10000033667],[7601478185,-227055467,-6454771937,10005191708],[6511884318,-16183483638,6936787298,9998885395],[3182862837,-8944326611,1551582063,5000163121],[8749349229,3873617849,897038629,10002178562],[5681053076,12169166665,-4956967003,9999140999],[-98487857,-4455227271,-11188097040,10005312707],[6210051878,7794473524,1788331093,10001802766],[2799038635,13309847658,-2874720650,10003092902],[1333856381,-5600706374,-10999762629,10003629623],[3412664239,9474414073,-10723317370,10001474902],[4102303542,9279753898,-10626837939,10001356355]],"source_active_plane_indices":[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82],"source_input_sha256":"9bf5e64f57837cf16c47947ef856a3c078db7fa73f675ce83a2e7fc2316d70f0"}
<!-- END UNIT J89_C444_G10_MINIMAL76_H_INPUT.json -->

<!-- BEGIN UNIT {"bytes": 1066, "name": "continue89.py", "sha256": "cae205143b4d48594d9eb0ccff5a1a6c4cee2ca6c612263febc11cac49797e58"} -->
"""Numerical continuation from the literal exact minimal76 H input.
The float conversion is a nomination input, not the definition of the exact body.
Default continuation parameters are proposed; this entrypoint itself was not run
in the generating turn. Every resulting endpoint still needs exact certification.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,argparse,numpy as np
from cycle89b import run
ROOT=Path(__file__).resolve().parent
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--cycles',type=int,default=8);ap.add_argument('--trust',type=float,default=.006);ap.add_argument('--prefix',default='CONTINUE89');a=ap.parse_args()
 d=json.loads((ROOT/'J89_C444_G10_MINIMAL76_H_INPUT.json').read_text());p=np.array(d['planes'],dtype=float)
 (ROOT/'NEXT89_NUMERIC.json').write_text(json.dumps({'normals':(p[:,:3]/p[:,3,None]).tolist(),'offsets':[1.]*len(p)},indent=2)+'\n')
 run('NEXT89_NUMERIC.json',a.cycles,a.prefix,a.trust,1e-7,180)
<!-- END UNIT continue89.py -->
