"""Independent upper points and an arbitrary four-point planar stable base.

Positive radial shadow costs ensure referenceU1. Four cyclic base directions
with every angular gap strictly below pi put reference0 inside the base facet.
The four base points share one exact negative height. No symmetry is imposed.
"""
import numpy as np

class Family:
    def __init__(self,X):
        assert len(X)<=85
        self.n=len(X)-5;self.ad=2*(self.n+4);self.cost_end=self.ad+self.n;self.d=self.cost_end+3
        phi=np.mod(np.arctan2(X[:4,1],X[:4,0]),2*np.pi);order=np.argsort(phi);P=np.vstack((X[4:-1],X[order]));r=np.linalg.norm(P,axis=1);angles=np.column_stack((np.arcsin(P[:,2]/r),np.arctan2(P[:,1],P[:,0])));angles[self.n:,1]=phi[order]
        rootnorm=np.linalg.norm(X[-1]);root=X[-1]/rootnorm;assert root[2]>0
        radii=np.r_[r[:self.n]/rootnorm,1.];U=np.vstack((P[:self.n]/r[:self.n,None],root));C=U[:-1]@U.T;np.fill_diagonal(C[:,:self.n],-np.inf);caps=np.max(C*radii[None],axis=1);cost=-np.log(radii[:-1]/caps);assert min(cost)>0
        self.q=np.r_[angles.ravel(),np.maximum(cost,1e-8),root[:2]/root[2],0.];Y,_=self.construct(self.q);self.q[-1]=float(np.clip(1-(X[0,2]/rootnorm)/Y[0,2],1e-7,.6))
        self.bounds=[(-1.55,1.55),(-20,20)]*self.n+[(-1.55,-.05),(-20,20)]*4+[(1e-8,2.)]*self.n+[(-5.,5.)]*2+[(1e-7,.6)]

    def domain(self,q):
        ids=2*np.arange(self.n,self.n+4)+1;ph=q[ids];gaps=np.r_[np.diff(ph),ph[0]+2*np.pi-ph[-1]];J=np.zeros((4,self.d))
        for k in range(4):J[k,ids[(k+1)%4]]=1;J[k,ids[k]]=-1
        return np.r_[gaps-1e-5,np.pi-1e-5-gaps],np.vstack((J,-J))

    def construct(self,q):
        n=self.n;d=self.d;a=q[:self.ad].reshape(n+4,2);th,ph=a.T;U=np.column_stack((np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),np.sin(th)));DU=np.zeros((n+4,3,d))
        for i in range(n+4):
            DU[i,:,2*i]=[-np.sin(th[i])*np.cos(ph[i]),-np.sin(th[i])*np.sin(ph[i]),np.cos(th[i])];DU[i,:,2*i+1]=[-np.cos(th[i])*np.sin(ph[i]),np.cos(th[i])*np.cos(ph[i]),0]
        rawroot=np.r_[q[self.cost_end:self.cost_end+2],1.];rootnorm=np.linalg.norm(rawroot);root=rawroot/rootnorm;Droot=np.zeros((3,d));Droot[:,self.cost_end:self.cost_end+2]=((np.eye(3)-np.outer(root,root))/rootnorm)[:,:2]
        W=np.vstack((U[:n],root));DW=np.concatenate((DU[:n],Droot[None]),axis=0);C=W@W.T;cost=np.full_like(C,np.inf);ok=C>1e-12;cost[ok]=-np.log(np.minimum(C[ok],1));cost+=np.r_[q[self.ad:self.cost_end],0.][:,None]
        if min(q[self.ad:self.cost_end])<0:raise ValueError('negative shadow cost')
        dist=np.full(n+1,np.inf);dist[n]=0;parent=np.full(n+1,-1,int);used=np.zeros(n+1,bool);order=[]
        for _ in range(n+1):
            j=int(np.argmin(np.where(used,np.inf,dist)))
            if not np.isfinite(dist[j]):raise ValueError('disconnected positive-shadow graph')
            used[j]=True;order.append(j);new=dist[j]+cost[:,j];take=(new<dist)&(~used);dist[take]=new[take];parent[take]=j
        R=np.exp(-dist);DR=np.zeros((n+1,d))
        for i in order[1:]:
            j=parent[i];Dc=DW[i].T@W[j]+DW[j].T@W[i];DR[i]=np.exp(-q[self.ad+i])*(C[i,j]*DR[j]+R[j]*Dc);DR[i,self.ad+i]-=R[i]
        upper=R[:n,None]*W[:n];Dupper=DR[:n,None,:]*W[:n,:,None]+R[:n,None,None]*DW[:n]
        heights=[];Dheights=[]
        for i in range(n,n+4):
            if U[i,2]>=-.01:raise ValueError('basal direction is not downward')
            cs=W@U[i];caps=R*cs*(1-1e-9);j=int(np.argmax(caps))
            if caps[j]<=0:raise ValueError('basal direction has no shadow parent')
            Dc=DU[i].T@W[j]+DW[j].T@U[i];Dr=(1-1e-9)*(cs[j]*DR[j]+R[j]*Dc);heights.append(caps[j]*U[i,2]);Dheights.append(Dr*U[i,2]+caps[j]*DU[i,2])
        k=int(np.argmax(heights));h=heights[k]*(1-q[-1]);Dh=Dheights[k]*(1-q[-1]);Dh[-1]-=heights[k];base=[];Dbase=[]
        for i in range(n,n+4):
            r=h/U[i,2];Dr=Dh/U[i,2]-h*DU[i,2]/U[i,2]**2;b=r*U[i];Db=r*DU[i]+U[i,:,None]*Dr;b[2]=h;Db[2]=Dh;base.append(b);Dbase.append(Db)
        return np.vstack((base,upper,root)),np.concatenate((Dbase,Dupper,Droot[None]),axis=0)
