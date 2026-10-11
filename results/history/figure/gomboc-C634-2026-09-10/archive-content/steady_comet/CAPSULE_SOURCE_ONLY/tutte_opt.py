"""Full physical positive-stress optimization, including true filled centroid.
No frozen mechanical reference point is used. The polar anchor is only a shape parameter.
"""
from pathlib import Path
import json,time,sys,itertools
import numpy as np
from scipy.optimize import minimize
from tutte_physical import TutteBody
from numeric import triangles,topology,mechanics
from tree_repair import rooted_parent

class PhysicalTutte(TutteBody):
    def setup(self,stable=3,unstable=None):
        self.W=len(self.free_edges);self.K=self.W+9;self.theta0=np.zeros(self.K)
        self.features=np.array(self.ref['original_q']);self.features=(self.features-self.features.mean(0))/self.features.std(0)
        self.tri=triangles(self.primal_faces);self.owners,self.ef=topology(self.primal_faces)
        self.inc=np.zeros((len(self.faces),self.N),bool)
        for i,c in enumerate(self.faces):self.inc[i,c]=True
        self.sroot=stable
        first=self.fullstate(self.theta0,jac=False,roots=False)
        self.uroot=int(np.linalg.norm(first['x'],axis=1).argmax()) if unstable is None else unstable
        if stable is None:self.sroot=int(np.linalg.norm(first['n'],axis=1).argmax())
        self.si=np.array([i for i in range(self.N) if i!=self.sroot]);self.ui=np.array([i for i in range(len(self.faces)) if i!=self.uroot])
        self.trees(self.theta0)
    def fullstate(self,theta,jac=True,roots=True):
        W=self.W;K=self.K
        w=self.w0*np.exp(theta[:W]);L=(self.BI*w[None,:])@self.BI.T;rhs=-self.BI@(w[:,None]*(self.BB.T@self.xyB));xy=np.zeros((self.N,2));xy[self.B]=self.xyB;xy[self.internal]=np.linalg.solve(L,rhs)
        delta=xy[self.EF[:,1]]-xy[self.EF[:,0]]
        if jac:
            dxy=np.zeros((self.N,2,W))
            rh=np.concatenate([self.BI*(w*delta[:,j])[None,:] for j in range(2)],axis=1)
            dx=np.linalg.solve(L,rh);dxy[self.internal,0]=dx[:,:W];dxy[self.internal,1]=dx[:,W:]
            ddelta=dxy[self.EF[:,1]]-dxy[self.EF[:,0]]
        forces=self.BB@(w[:,None]*delta);bw=self.Kinv@(-forces.ravel());omega=dict(zip(self.free_edges,w));omega.update(zip(self.bedges,bw))
        if jac:
            df=np.einsum('be,ec,ek->bck',self.BB,delta,np.diag(w))+np.einsum('be,e,eck->bck',self.BB,w,ddelta)
            dbw=self.Kinv@(-df.reshape(6,W));dw={e:np.eye(W)[k]*w[k] for k,e in enumerate(self.free_edges)};dw.update({e:dbw[k] for k,e in enumerate(self.bedges)})
        plane=np.zeros((len(self.faces),3))
        if jac:dp=np.zeros((len(self.faces),3,W))
        for f,g,u,v in self.plan:
            dd=xy[v]-xy[u];e=tuple(sorted((u,v)));ww=omega[e];rd=np.array([-dd[1],dd[0]]);dg=ww*rd
            plane[g]=plane[f]+np.r_[dg,-dg@xy[u]]
            if jac:
                ddd=dxy[v]-dxy[u];dr=np.vstack([-ddd[1],ddd[0]]);ddg=rd[:,None]*dw[e][None,:]+ww*dr
                dp[g,:2]=dp[f,:2]+ddg;dp[g,2]=dp[f,2]-xy[u]@ddg-dg@dxy[u]
        plane*=self.height_sign
        if jac:dp*=self.height_sign
        vf=np.array(self.vface,int);z=np.einsum('ic,ic->i',plane[vf,:2],xy)+plane[vf,2];cap=np.column_stack([xy,z])
        if jac:
            dcap=np.zeros((self.N,3,K));dcap[:,:2,:W]=dxy;dcap[:,2,:W]=np.einsum('icp,ic->ip',dp[vf,:2],xy)+np.einsum('ic,icp->ip',plane[vf,:2],dxy)+dp[vf,2]
        ll=np.log(self.lam)+self.features@theta[W:W+3];ll-=ll.max();lam=np.exp(ll);lam/=lam.sum();o=lam@cap
        if jac:
            do=np.einsum('i,icp->cp',lam,dcap);dl=lam[:,None]*(self.features-lam@self.features)
            do[:,W:W+3]+=cap.T@dl
        normals=np.column_stack([plane[:,:2],-np.ones(len(plane))]);h=-plane[:,2]-normals@o;pcap=normals/h[:,None]
        if jac:
            dn=np.zeros((len(plane),3,K));dn[:,:2,:W]=dp[:,:2];dh=-np.einsum('icp,c->ip',dn,o)-normals@do;dh[:,:W]-=dp[:,2]
            dpcap=dn/h[:,None,None]-normals[:,:,None]*dh[:,None,:]/h[:,None,None]**2
        rel=cap-o;P0=pcap@self.linear;q0=rel@self.invlinear.T
        mt=theta[W+3:];T=np.array([[np.exp(mt[0]),0,0],[mt[3],np.exp(mt[1]),0],[mt[4],mt[5],np.exp(mt[2])]]);iT=np.linalg.inv(T);P=P0@T;q=q0@iT.T
        if jac:
            dP0=np.einsum('icp,cj->ijp',dpcap,self.linear);dq0=np.einsum('icp,cj->ijp',dcap-do[None,:,:],self.invlinear.T)
            dP=np.einsum('icp,cj->ijp',dP0,T);dq=np.einsum('icp,cj->ijp',dq0,iT.T)
            for k,(a,b) in enumerate([(0,0),(1,1),(2,2),(1,0),(2,0),(2,1)]):
                dT=np.zeros((3,3));dT[a,b]=np.exp(mt[k]) if k<3 else 1;di=-iT@dT@iT
                dP[:,:,W+3+k]+=P0@dT;dq[:,:,W+3+k]+=q0@di.T
        a,b,c=[P[self.tri[:,k]] for k in range(3)];det=np.einsum('ij,ij->i',a,np.cross(b,c));V=det.sum()/6;M=np.einsum('t,tc->c',det,a+b+c)/24;cent=M/V
        hh=1-q@cent;n=q/hh[:,None];x=P-cent;gaps=1-P@q.T
        def cos(z):
            num=z@z.T-np.einsum('ij,ij->i',z,z)[:,None];den=np.linalg.norm(z,axis=1)[:,None]*np.linalg.norm(z[None,:,:]-z[:,None,:],axis=2)
            vv=np.divide(num,den,out=np.full_like(num,-np.inf),where=den>1e-13);np.fill_diagonal(vv,-np.inf);return vv
        cs=cos(n);cu=cos(x);out=dict(q=q,P=P,cap=cap,lam=lam,origin=o,V=V,M=M,c=cent,n=n,x=x,cs=cs,cu=cu,gaps=gaps,det=det)
        if roots:
            sw=np.array(self.sparent)[self.si];uw=np.array(self.uparent)[self.ui];vals=np.r_[cs[self.si,sw],cu[self.ui,uw]];out['vals']=vals
        if jac:
            da,db,dc=[dP[self.tri[:,k]] for k in range(3)]
            ddet=np.einsum('tcp,tc->tp',da,np.cross(b,c))+np.einsum('tcp,tc->tp',db,np.cross(c,a))+np.einsum('tcp,tc->tp',dc,np.cross(a,b));dV=ddet.sum(0)/6
            dM=(np.einsum('tp,tc->cp',ddet,a+b+c)+np.einsum('t,tcp->cp',det,da+db+dc))/24;dcent=(dM-cent[:,None]*dV[None,:])/V
            dhh=-np.einsum('icp,c->ip',dq,cent)-q@dcent;dn=dq/hh[:,None,None]-q[:,:,None]*dhh[:,None,:]/hh[:,None,None]**2;dx=dP-dcent
            def dcoss(z,dz,ii,jj):
                aa=z[ii];bb=z[jj]-aa;daa=dz[ii];dbb=dz[jj]-daa;aa2=np.einsum('ic,ic->i',aa,aa);bb2=np.einsum('ic,ic->i',bb,bb);den=np.sqrt(aa2*bb2);uv=np.einsum('ic,ic->i',aa,bb)
                duv=np.einsum('icp,ic->ip',daa,bb)+np.einsum('icp,ic->ip',dbb,aa)
                return duv/den[:,None]-(uv/den)[:,None]*(np.einsum('icp,ic->ip',daa,aa)/aa2[:,None]+np.einsum('icp,ic->ip',dbb,bb)/bb2[:,None])
            if roots:out['J']=np.vstack([dcoss(n,dn,self.si,sw),dcoss(x,dx,self.ui,uw)])
            out.update(dq=dq,dP=dP,dc=dcent,dV=dV,dM=dM)
        return out
    def trees(self,theta):
        st=self.fullstate(theta,jac=False,roots=False)
        self.sparent=rooted_parent(st['cs'],{tuple(sorted(p)) for p in self.ef.values()},self.sroot)
        self.uparent=rooted_parent(st['cu'],set(self.ef),self.uroot)
        return self.fullstate(theta,jac=False)
    def census(self,theta):
        st=self.fullstate(theta,jac=False);return mechanics(st['q'],self.primal_faces,P=st['P'],tol=1e-9)


def optimize_tutte(body,R,prefix,rounds=10,maxiter=500,bound=3.,goal=1e-4):
    theta=np.zeros(body.K);start=time.time();best=theta.copy();bestloss=np.inf
    for epoch in range(rounds):
        tree=body.trees(theta);print('TUTTE_ROUND',epoch,'root',body.sroot,body.uroot,'min',tree['vals'].min(),'bad',int((tree['vals']<0).sum()),'census',body.census(theta),flush=True)
        calls=0;cache_t=None;cache=None
        def fun(t):
            nonlocal calls,cache_t,cache,best,bestloss
            st=body.fullstate(t);v=np.minimum(st['vals']-goal,0);loss=float(v@v);grad=2*v@st['J'];calls+=1
            if loss<bestloss and st['gaps'][~body.inc].min()>-1e-7:bestloss=loss;best=t.copy()
            if calls%50==0:
                print('TUTTE_OPT',epoch,calls,'time',time.time()-start,'loss',loss,'min',st['vals'].min(),'bad',int((st['vals']<0).sum()),'gap',st['gaps'][~body.inc].min(),'theta',np.max(abs(t)),flush=True)
                np.savez(R/(prefix+'_RUNNING.npz'),theta=best,q=body.fullstate(best,jac=False)['q'],P=body.fullstate(best,jac=False)['P'])
            return loss,grad
        bounds=[(-bound,bound)]*body.W+[(-1.5,1.5)]*3+[(-.8,.8)]*3+[(-1.,1.)]*3
        res=minimize(fun,theta,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':maxiter,'ftol':1e-15,'gtol':1e-10,'maxls':40,'maxcor':25})
        theta=res.x;st=body.fullstate(theta,jac=False);rr=body.census(theta)
        np.savez(R/(prefix+f'_ROUND{epoch}.npz'),theta=theta,q=st['q'],P=st['P'],sparent=body.sparent,uparent=body.uparent)
        (R/(prefix+f'_ROUND{epoch}_numeric.json')).write_text(json.dumps(rr,indent=2))
        print('TUTTE_ROUND_END',epoch,res.message,'loss',res.fun,'min',st['vals'].min(),rr,flush=True)
        if rr['counts']==[1,1,0] and st['vals'].min()>1e-6 and rr['min_gap']>1e-8:
            print('TUTTE_NUMERIC_WINNER',prefix,epoch,flush=True);return theta
    return theta

if __name__=='__main__':
    R=Path(__file__).parent;ref=json.loads((R/'TUTTE_C650_REFERENCE.json').read_text());data=json.loads((R/'H249_RESTORATION.json').read_text());body=PhysicalTutte(ref,data['edges']);body.setup(stable=3,unstable=2)
    t=time.time();st=body.fullstate(body.theta0);print('STATE_TIME',time.time()-t,'K',body.K,flush=True)
    rng=np.random.default_rng(123);direction=rng.normal(size=body.K);direction/=np.linalg.norm(direction);eps=1e-5
    pl=body.fullstate(eps*direction,jac=False);mi=body.fullstate(-eps*direction,jac=False)
    for name,tr,ap in [('P',np.einsum('icp,p->ic',st['dP'],direction),(pl['P']-mi['P'])/(2*eps)),('q',np.einsum('icp,p->ic',st['dq'],direction),(pl['q']-mi['q'])/(2*eps)),('c',st['dc']@direction,(pl['c']-mi['c'])/(2*eps)),('J',st['J']@direction,(pl['vals']-mi['vals'])/(2*eps))]:print('DERIVATIVE',name,'error',np.max(abs(tr-ap)),'scale',np.max(abs(tr)),flush=True)
    optimize_tutte(body,R,'H249_STRESS',rounds=12,maxiter=500,bound=3.)
