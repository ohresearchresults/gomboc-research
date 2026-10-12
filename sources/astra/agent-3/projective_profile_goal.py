"""Rationally reproducible quadrilateral profile family at E<=248.

A convex body has rectangular horizontal sections, with two positive strictly
concave piecewise linear width functions sharing m break heights, plus one
axial apex. Its genuine graph is V=4m+1,E=8m,F=4m+1. A single physical
projective map followed by an affine map preserves every genuine incidence;
uniform mass is integrated after this map. m<=31 gives sum<=498.
"""
import argparse,json,hashlib,time
from pathlib import Path
from math import gcd,lcm
import numpy as np
from gmpy2 import mpq
from scipy.optimize import minimize
from scipy.spatial import ConvexHull
from persistence_birth import bars_loss
from support_geometry import escape
from exact_audit_vertices import check_B,cross,sub,dot
from goal_nomination import ExactGoalCandidateFound

class Family:
    def __init__(self,m=31,eta=.02,asymmetric=False):
        assert 3<=m<=31
        self.m=m;self.asymmetric=asymmetric;self.k=4 if asymmetric else 2;self.base_d=self.k*m;self.d=self.base_d+8;self.eta=eta;self.t=np.arange(m)/m
        tt=self.t[:,None];kn=self.t[1:][None]
        self.K=np.column_stack((1-self.t,np.minimum(tt,kn)*(1-np.maximum(tt,kn))))
        self.signs=np.array([[1,1],[-1,1],[-1,-1],[1,-1]])
        self.faces=[list(range(3,-1,-1))]
        for i in range(m-1):
            for k in range(4):self.faces.append([4*i+k,4*i+(k+1)%4,4*(i+1)+(k+1)%4,4*(i+1)+k])
        for k in range(4):self.faces.append([4*(m-1)+k,4*(m-1)+(k+1)%4,4*m])
        owners={}
        for f,cy in enumerate(self.faces):
            for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
        assert all(len(fs)==2 for fs in owners.values()) and len(owners)==8*m
        self.pe=np.array(list(owners));self.qe=np.array(list(owners.values()));self.T=np.array([(cy[0],cy[k],cy[k+1])for cy in self.faces for k in range(1,len(cy)-1)]);self.tri=np.array([cy[:3]for cy in self.faces])
        self.inc=np.zeros((len(self.faces),4*m+1),bool)
        for f,cy in enumerate(self.faces):self.inc[f,cy]=True

    def geometry(self,q,derivative=True):
        m=self.m;D=self.d;base_d=self.base_d;expq=np.exp(q[:base_d]);width=np.column_stack([self.K@expq[j*m:(j+1)*m]for j in range(self.k)])
        B=np.zeros((4*m+1,3));B[:-1,2]=np.repeat(2*self.t-1,4);B[-1,2]=1
        DB=np.zeros((len(B),3,D))
        for i in range(m):
            for k,s in enumerate(self.signs):
                jx=(0 if s[0]>0 else 1)if self.asymmetric else 0;jy=(2 if s[1]>0 else 3)if self.asymmetric else 1
                B[4*i+k,0]=s[0]*width[i,jx];B[4*i+k,1]=s[1]*width[i,jy]
                DB[4*i+k,0,jx*m:(jx+1)*m]=s[0]*self.K[i]*expq[jx*m:(jx+1)*m];DB[4*i+k,1,jy*m:(jy+1)*m]=s[1]*self.K[i]*expq[jy*m:(jy+1)*m]
        aa,bb,c,d,e=q[base_d:base_d+5];A=np.array([[np.exp(aa),c,d],[0,np.exp(bb),e],[0,0,np.exp(-aa-bb)]]);DA=np.zeros((3,3,D));DA[0,0,base_d]=A[0,0];DA[1,1,base_d+1]=A[1,1];DA[2,2,base_d:base_d+2]=-A[2,2];DA[0,1,base_d+2]=1;DA[0,2,base_d+3]=1;DA[1,2,base_d+4]=1
        u=q[-3:];Du=np.zeros((3,D));Du[:,-3:]=np.eye(3);j=int(np.argmin(B@u));den0=1-B[j]@u;p=.97*u/den0;Dp=.97*Du/den0+.97*u[:,None]*(u@DB[j]+B[j]@Du)/den0**2
        bd=1+B@p
        if min(bd)<=0:raise ValueError('nonpositive physical projective denominator')
        W=B/bd[:,None];X=W@A.T;T=self.T;a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));vol=v6.sum()/6
        if vol<=0:raise ValueError('nonpositive uniform physical volume')
        centre=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-centre;Y=np.linalg.solve(X[self.tri],np.ones((len(self.tri),3,1)))[:,:,0];dd=1-Y@centre
        if min(dd)<=0:raise ValueError('centroid outside physical support')
        H=Y/dd[:,None];g=dict(X=X,Z=Z,H=H,Y=Y,centroid=centre,volume=vol,widths=width,B=B,A=A,p=p,faces=self.faces,pe=self.pe,qe=self.qe,V=len(X),E=len(self.pe),F=len(self.faces))
        if not derivative:return g
        Dbd=np.einsum('icd,c->id',DB,p)+B@Dp;DW=DB/bd[:,None,None]-W[:,:,None]*Dbd[:,None,:]/bd[:,None,None];DX=np.einsum('ic,acd->iad',W,DA)+np.einsum('icd,ac->iad',DW,A)
        da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];dv=np.einsum('ic,icd->id',np.cross(b,c),da)+np.einsum('ic,icd->id',np.cross(c,a),db)+np.einsum('ic,icd->id',np.cross(a,b),dc)
        Dg=(np.einsum('id,ic->cd',dv,a+b+c-4*centre)+np.einsum('i,icd->cd',v6,da+db+dc))/(4*v6.sum());DY=np.linalg.solve(X[self.tri],-np.einsum('fc,facd->fad',Y,DX[self.tri]));Ddd=-np.einsum('fcd,c->fd',DY,centre)-Y@Dg;DH=DY/dd[:,None,None]-Y[:,:,None]*Ddd[:,None,:]/dd[:,None,None]**2
        g.update(DX=DX,DZ=DX-Dg,DH=DH);return g

    def score(self,q,derivative=True):
        g=self.geometry(q,derivative);lp,GP,P=bars_loss(g['Z'],self.pe,self.eta);lq,GQ,Q=bars_loss(g['H'],self.qe,self.eta)
        cl=dict(S=int(sum(escape(g['H'])[0]<0)),U=int(sum(escape(g['Z'])[0]<0)),Pmax=max(P,default=0.),Qmax=max(Q,default=0.),positive_P=len(P),positive_Q=len(Q),V=g['V'],E=g['E'],F=g['F'])
        J=np.einsum('ic,icd->d',GP,g['DZ'])+np.einsum('ic,icd->d',GQ,g['DH'])if derivative else None
        return lp+lq,J,cl,g

    def freeze(self,q,out):
        out=Path(out);out.mkdir(parents=True,exist_ok=False);g=self.geometry(q,False);A=[tuple(mpq(float(v))for v in row)for row in g['A']];p=tuple(mpq(float(v))for v in g['p']);width=[tuple(mpq(float(v))for v in row)for row in g['widths']];heights=[mpq(float(2*t-1))for t in self.t];B=[]
        for widths,z in zip(width,heights):
            for sx,sy in self.signs:
                jx=(0 if sx>0 else 1)if self.asymmetric else 0;jy=(2 if sy>0 else 3)if self.asymmetric else 1
                B.append((int(sx)*widths[jx],int(sy)*widths[jy],z))
        B.append((mpq(0),mpq(0),mpq(1)));X=[]
        for x in B:
            den=1+dot(p,x);assert den>0;X.append(tuple(dot(row,x)/den for row in A))
        rows=set()
        def add(n,h):
            rr=(*n,h);D=lcm(*(int(v.denominator)for v in rr));ii=tuple(int(v*D)for v in rr);gg=gcd(*ii);rows.add(tuple(v//gg for v in ii))
        for cy in self.faces:
            a,b,c=[X[i]for i in cy[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
            assert all(dot(n,X[i])==h for i in cy),'exact quad coplanarity failed'
            assert all(dot(n,x)<h for i,x in enumerate(X)if i not in cy),'exact strict noncontact failed'
            add(n,h)
        for axis in range(3):
            for s in [-1,1]:
                n=tuple(mpq(s if k==axis else 0)for k in range(3));add(n,max(dot(n,x)for x in X)+1)
        enc=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();raw=dict(H=sorted(rows));(out/'raw.json').write_bytes(enc(raw));(out/'coordinates.json').write_bytes(enc(dict(points=X,density=1)));np.save(out/'parameters.npy',q)
        (out/'construction.json').write_bytes(enc(dict(profile_heights=heights,profile_side_offsets=width,independent_profiles=self.k,preimage_points=B,affine=A,projective_p=p,faces=self.faces,definition='uniform density on the physical convex hull after x -> A*x/(1+p.x); exact shared ring heights and signed side offsets preserve all genuine quadrilateral facets')))
        a=check_B.run(raw);assert {tuple(map(mpq,x))for x in a['raw_vertices']}==set(X),'native intersection differs from exact physical vertex hull'
        assert(a['V'],a['E'],a['F'])==(4*self.m+1,8*self.m,4*self.m+1)
        (out/'audit.json').write_bytes(enc(a));s={k:a[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest());s['goal_met']=a['counts']==[1,1,0]and a['weak']==[0,0,0]and s['C_2E']<500 and s['VplusEplusF']<500;(out/'summary.json').write_text(json.dumps(s,indent=2));print('PROFILE_EXACT',s,flush=True)
        if s['goal_met']:raise ExactGoalCandidateFound('Exact physical homogeneous projective profile Figure '+str(out))

def run(out,m,seed,iterations,asymmetric=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Family(m,asymmetric=asymmetric);rng=np.random.default_rng(seed);q=np.zeros(F.d);q[:F.base_d]=rng.normal(-2.,.8,F.base_d)
    for i in range(F.k):q[i*m]=rng.uniform(-4,-1)
    q[F.base_d:F.base_d+5]=rng.normal(0,.3,5);q[-3:]=rng.normal(0,.7,3)
    d=rng.normal(size=F.d);d/=np.linalg.norm(d);h=1e-7;v,J,cl,g=F.score(q);check=dict(fd=(F.score(q+h*d,False)[0]-F.score(q-h*d,False)[0])/(2*h),analytic=float(J@d));hh=ConvexHull(g['X']);T=hh.simplices.copy();a,b,c=g['X'][T[:,0]],g['X'][T[:,1]],g['X'][T[:,2]];sg=np.einsum('ic,ic->i',np.cross(b-a,c-a),hh.equations[:,:3]);T[sg<0]=T[sg<0][:,[0,2,1]];a,b,c=g['X'][T[:,0]],g['X'][T[:,1]],g['X'][T[:,2]];dv=np.einsum('ic,ic->i',a,np.cross(b,c));cg=np.sum(dv[:,None]*(a+b+c),axis=0)/(4*dv.sum());check.update(volume_error=float(abs(hh.volume-g['volume'])),centroid_error=float(np.max(abs(cg-g['centroid']))),initial_counts=cl)
    gap=1-g['Y']@g['X'].T;check.update(min_noncontact=float(min(gap[~F.inc])),max_contact=float(max(abs(gap[F.inc]))));(out/'method_check.json').write_text(json.dumps(check,indent=2));assert abs(check['fd']-check['analytic'])<1e-4 and check['volume_error']<1e-10 and check['centroid_error']<1e-10 and check['min_noncontact']>0 and check['max_contact']<1e-9
    bounds=[(-10.,3.)]*F.base_d+[(-2.,2.)]*2+[(-3.,3.)]*3+[(-5.,5.)]*3;calls=0;start=time.time();history=[]
    for stage,eta in enumerate([.03,.005,.0005]):
        F.eta=eta;sd=out/f'stage{stage}';sd.mkdir();best=np.inf
        def objective(q):
            nonlocal calls,best
            calls+=1;v,J,cl,g=F.score(q)
            if v<best:
                best=v;np.save(sd/'best_parameters.npy',q);np.save(sd/'physical_vertices.npy',g['X']);(sd/'best.json').write_text(json.dumps(dict(loss=v,eta=eta,calls=calls,seconds=time.time()-start,**cl),indent=2))
            if cl['S']==cl['U']==1:F.freeze(q,sd/f'exact_goal_{calls:06d}')
            if calls%250==0:print('PROJECTIVE_PROFILE_GOAL',out,stage,calls,v,cl,flush=True)
            return v,J
        r=minimize(objective,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=iterations,maxls=50,maxcor=25,ftol=1e-15,gtol=1e-9));q=np.load(sd/'best_parameters.npy');row=dict(stage=stage,eta=eta,calls=calls,loss=best,message=str(r.message),iterations=int(r.nit));history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('PROFILE_STAGE_FINITE_STOP',out,row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--rings',type=int,default=31);p.add_argument('--seed',type=int,default=771840);p.add_argument('--iterations',type=int,default=1500);p.add_argument('--asymmetric',action='store_true');a=p.parse_args();run(a.out,a.rings,a.seed,a.iterations,a.asymmetric)
