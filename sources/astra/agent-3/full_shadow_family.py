"""Complete positive-shadow graph, arbitrary apex direction and planar base.

Every nonroot input participates in the radial graph, including base points;
base-to-base and upper-to-base escape paths are allowed. The unit root uses a
stereographic chart. Three raw base-height equalities accompany the three
actual mass equations. The interpreted physical body always uses one literal
common basal height; exact own-centroid audit remains the sole acceptance.
"""
import numpy as np

class Family:
    def __init__(self,X,cost_floor=1e-8):
        assert len(X)<=85
        assert cost_floor>0;self.cost_floor=cost_floor
        self.n=len(X)-1;self.ad=2*self.n;self.cost_end=self.ad+self.n;self.d=self.cost_end+2
        phi=np.mod(np.arctan2(X[:4,1],X[:4,0]),2*np.pi);order=np.argsort(phi);self.source_order=np.r_[order,np.arange(4,len(X))];P=X[self.source_order];r=np.linalg.norm(P,axis=1);root=P[-1]/r[-1];assert root[2]>-1+1e-8
        U=P/r[:,None];angles=np.column_stack((np.arctan2(U[:-1,2],np.hypot(U[:-1,0],U[:-1,1])),np.arctan2(U[:-1,1],U[:-1,0])));angles[:4,1]=phi[order]
        rr=r/r[-1];C=U[:-1]@U.T;np.fill_diagonal(C[:,:self.n],-np.inf);caps=np.max(C*rr[None],axis=1);cost=-np.log(rr[:-1]/caps);assert min(cost)>0,'all nonroot inputs require a positive reference escape'
        self.q=np.r_[angles.ravel(),np.maximum(cost,cost_floor),root[:2]/(1+root[2])]
        self.bounds=[(-np.pi/2,-.001),(-20,20)]*4+[(-np.pi/2,np.pi/2),(-20,20)]*(self.n-4)+[(cost_floor,2.)]*self.n+[(-20,20)]*2
        self.mass_controls=np.r_[np.arange(self.ad),np.arange(self.cost_end,self.d)]
        self.fixed_parent=None

    def freeze_tree(self,q,seed=None):
        self.construct(q);R=self.last_radii.copy();C=self.last_cosines.copy();parent=self.last_parent.copy();order=self.last_order.copy();q=q.copy()
        if seed is not None:
            rng=np.random.default_rng(seed)
            for i in range(self.n):
                cap=R*C[i];valid=np.flatnonzero((cap>R[i]*np.exp(1.0001*self.cost_floor))&(R>R[i]))
                if len(valid):parent[i]=int(rng.choice(valid))
                q[self.ad+i]=max(self.cost_floor,float(np.log(R[parent[i]]*C[i,parent[i]]/R[i])))
            order=list(map(int,np.argsort(R)[::-1]));assert order[0]==self.n
        self.fixed_parent=parent;self.fixed_order=order
        return q

    def domain(self,q):
        ids=2*np.arange(4)+1;ph=q[ids];gap=np.r_[np.diff(ph),ph[0]+2*np.pi-ph[-1]];J=np.zeros((4,self.d))
        for k in range(4):J[k,ids[(k+1)%4]]=1;J[k,ids[k]]=-1
        return np.r_[gap-1e-10,np.pi-1e-10-gap],np.vstack((J,-J))

    def construct(self,q):
        n=self.n;d=self.d;theta,phi=q[:self.ad].reshape(n,2).T;U=np.column_stack((np.cos(theta)*np.cos(phi),np.cos(theta)*np.sin(phi),np.sin(theta)));DU=np.zeros((n,3,d))
        for i in range(n):
            DU[i,:,2*i]=[-np.sin(theta[i])*np.cos(phi[i]),-np.sin(theta[i])*np.sin(phi[i]),np.cos(theta[i])];DU[i,:,2*i+1]=[-np.cos(theta[i])*np.sin(phi[i]),np.cos(theta[i])*np.cos(phi[i]),0]
        a,b=q[-2:];den=1+a*a+b*b;raw=np.array([2*a,2*b,1-a*a-b*b]);root=raw/den;Droot=np.zeros((3,d));Droot[:,-2]=(np.array([2,0,-2*a])*den-raw*2*a)/den**2;Droot[:,-1]=(np.array([0,2,-2*b])*den-raw*2*b)/den**2
        W=np.vstack((U,root));DW=np.concatenate((DU,Droot[None]),axis=0);C=W@W.T;cost=np.full_like(C,np.inf);ok=C>1e-12;cost[ok]=-np.log(np.minimum(C[ok],1));cost+=np.r_[q[self.ad:self.cost_end],0.][:,None]
        if min(q[self.ad:self.cost_end])<0:raise ValueError('negative shadow cost')
        if self.fixed_parent is None:
            dist=np.full(n+1,np.inf);dist[n]=0;parent=np.full(n+1,-1,int);used=np.zeros(n+1,bool);order=[]
            for _ in range(n+1):
                j=int(np.argmin(np.where(used,np.inf,dist)))
                if not np.isfinite(dist[j]):raise ValueError('disconnected shadow graph')
                used[j]=True;order.append(j);new=dist[j]+cost[:,j];take=(new<dist)&(~used);dist[take]=new[take];parent[take]=j
            R=np.exp(-dist)
        else:
            parent=self.fixed_parent;order=self.fixed_order;R=np.zeros(n+1);R[n]=1.
            for i in order[1:]:
                j=parent[i]
                if C[i,j]<=0:raise ValueError('fixed positive-shadow parent angle became nonpositive')
                R[i]=R[j]*C[i,j]*np.exp(-q[self.ad+i])
        DR=np.zeros((n+1,d))
        for i in order[1:]:
            j=parent[i];Dc=DW[i].T@W[j]+DW[j].T@W[i];DR[i]=np.exp(-q[self.ad+i])*(C[i,j]*DR[j]+R[j]*Dc);DR[i,self.ad+i]-=R[i]
        X=R[:,None]*W;DX=DR[:,None,:]*W[:,:,None]+R[:,None,None]*DW
        self.last_plane=X[1:4,2]-X[0,2];self.last_Jplane=DX[1:4,2]-DX[0,2]
        # This is the actual literal body definition; the raw height equations
        # are restored separately, rather than assumed to hold numerically.
        h=float(np.mean(X[:4,2]));Dh=DX[:4,2].mean(0);X[:4,2]=h;DX[:4,2]=Dh
        self.last_radii=R;self.last_cosines=C;self.last_parent=parent;self.last_order=order
        return X,DX
