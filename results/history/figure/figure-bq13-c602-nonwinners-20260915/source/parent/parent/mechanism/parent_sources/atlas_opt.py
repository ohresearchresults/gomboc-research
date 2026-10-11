"""Deterministic filled-centroid-aware sequential linearization of a contact atlas.
Floating-point discovery code; certification is a separate exact computation.
"""
import json, itertools, time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from numeric import recover,topology,triangles,best_triples,mechanics

class Atlas:
    def __init__(self,data,faces,stable=3,unstable=None):
        self.data=json.loads(json.dumps(data)); self.faces=faces
        self.n=data['n_supports'];self.M=len(data['controls'])
        self.fixed=np.asarray(data['controls'],float)/data['grid'];self.fixed[self.n]=[0,0,1]
        self.plan=[(i,np.array(d,dtype=int),np.array(ax,dtype=int),np.array([k for k in range(3) if k not in ax],dtype=int)) for i,d,ax in data['plan']]
        free=[(i,k) for i,d,ax,rest in self.plan for k in rest]
        self.free=np.array(free,int);self.np=len(free)
        X=recover(data)
        self.scale=np.array([max(np.linalg.norm(X[i]),0.1) for i,k in free])
        self.u0=np.array([X[i,k] for i,k in free])/self.scale
        self.owners,self.ef=topology(faces); self.tri=triangles(faces)
        self.triples=best_triples(X[:self.n],self.owners)
        self.inc=np.zeros((len(self.owners),self.n),bool)
        for i,cy in enumerate(self.owners):self.inc[i,cy]=True
        P=np.linalg.solve(X[:self.n][self.triples],np.ones((len(self.owners),3,1)))[:,:,0]
        self.Sroot=stable
        self.Uroot=int(np.linalg.norm(P-[0,0,1],axis=1).argmin()) if unstable is None else unstable
        self.si=np.array([i for i in range(self.n) if i!=self.Sroot])
        self.ui=np.array([i for i in range(len(P)) if i!=self.Uroot])
        self.ni,self.nj=np.where(~self.inc)
    def chart(self,u,jac=True):
        X=self.fixed.copy();X[self.free[:,0],self.free[:,1]]=u*self.scale
        if jac:
            DX=np.zeros((self.M,3,self.np));DX[self.free[:,0],self.free[:,1],np.arange(self.np)]=self.scale
        for i,deps,ax,rest in self.plan:
            if len(deps):
                A=X[np.ix_(deps,ax)]
                y=np.linalg.solve(A,1-X[np.ix_(deps,rest)]@X[i,rest]);X[i,ax]=y
                if jac:
                    rhs=-np.einsum('rcp,c->rp',DX[deps],X[i])
                    if len(rest):rhs-=X[np.ix_(deps,rest)]@DX[i,rest]
                    DX[i,ax]=np.linalg.solve(A,rhs)
        return (X,DX) if jac else X
    def state(self,u,jac=True):
        if jac:XX,DXX=self.chart(u);q=XX[:self.n];dq=DXX[:self.n]
        else:XX=self.chart(u,False);q=XX[:self.n]
        A=q[self.triples];P=np.linalg.solve(A,np.ones((len(A),3,1)))[:,:,0]
        if jac:dP=np.linalg.solve(A,-np.einsum('vrcp,vc->vrp',dq[self.triples],P))
        a,b,c=[P[self.tri[:,k]] for k in range(3)]
        det=np.einsum('ij,ij->i',a,np.cross(b,c)); V=det.sum()/6
        M=np.einsum('t,tc->c',det,a+b+c)/24;cent=M/V
        h=1-q@cent;n=q/h[:,None];x=P-cent
        gaps=1-P@q.T
        def cosine(z):
            num=z@z.T-np.einsum('ij,ij->i',z,z)[:,None]
            diff=z[None,:,:]-z[:,None,:]
            den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(diff,axis=2)
            out=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-14)
            np.fill_diagonal(out,-np.inf);return out
        cs=cosine(n);cu=cosine(x)
        sw=cs[self.si].argmax(1);uw=cu[self.ui].argmax(1)
        if hasattr(self,'sparent'):sw=np.asarray(self.sparent,dtype=int)[self.si]
        if hasattr(self,'uparent'):uw=np.asarray(self.uparent,dtype=int)[self.ui]
        vals=np.r_[cs[self.si,sw],cu[self.ui,uw]]
        out=dict(X=XX,q=q,P=P,V=V,M=M,c=cent,h=h,n=n,x=x,gaps=gaps,det=det,cs=cs,cu=cu,sw=sw,uw=uw,vals=vals)
        if jac:
            da,db,dc=[dP[self.tri[:,k]] for k in range(3)]
            ddet=np.einsum('tcp,tc->tp',da,np.cross(b,c))+np.einsum('tcp,tc->tp',db,np.cross(c,a))+np.einsum('tcp,tc->tp',dc,np.cross(a,b))
            dV=ddet.sum(0)/6
            dM=(np.einsum('tp,tc->cp',ddet,a+b+c)+np.einsum('t,tcp->cp',det,da+db+dc))/24
            dcent=(dM-cent[:,None]*dV[None,:])/V
            dh=-np.einsum('icp,c->ip',dq,cent)-q@dcent
            dn=dq/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2
            dx=dP-dcent[None,:,:]
            def dcoss(z,dz,ii,jj):
                aa=z[ii];bb=z[jj]-aa;daa=dz[ii];dbb=dz[jj]-daa
                aa2=np.einsum('ic,ic->i',aa,aa);bb2=np.einsum('ic,ic->i',bb,bb)
                den=np.sqrt(aa2*bb2);uv=np.einsum('ic,ic->i',aa,bb)
                duv=np.einsum('icp,ic->ip',daa,bb)+np.einsum('icp,ic->ip',dbb,aa)
                return duv/den[:,None]-(uv/den)[:,None]*(np.einsum('icp,ic->ip',daa,aa)/aa2[:,None]+np.einsum('icp,ic->ip',dbb,bb)/bb2[:,None])
            J=np.vstack([dcoss(n,dn,self.si,sw),dcoss(x,dx,self.ui,uw)])
            out.update(dq=dq,dP=dP,dc=dcent,J=J,dV=dV,dM=dM,ddet=ddet)
        return out
    def gap_jac(self,st,vi,qi):
        return -np.einsum('icp,ic->ip',st['dP'][vi],st['q'][qi])-np.einsum('ic,icp->ip',st['P'][vi],st['dq'][qi])
    def save(self,u,path):
        z=json.loads(json.dumps(self.data));X=self.chart(u,False)
        z['controls']=np.rint(X*z['grid']).astype(np.int64).tolist()
        Path(path).write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
        return z


