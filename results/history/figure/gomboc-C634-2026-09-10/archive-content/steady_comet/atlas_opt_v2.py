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


def optimize(model,u=None,steps=200,target=None,log=None,trust=0.0005,keep=2e-5,goal=2e-4):
    """target=None maximizes minimum escape; target=(vertex,support) closes a gap.
    Strong positive existing escapes are separately retained. No center freezing.
    """
    u=model.u0.copy() if u is None else u.copy()
    best=u.copy();bestvalue=-np.inf
    def say(*a):
        print(*a,flush=True)
        if log:
            with open(log,'a') as f:print(*a,file=f)
    t0=time.time()
    initial=model.state(u,False)['vals']
    floors=np.where(initial>1e-10,np.minimum(keep,initial*0.5),-np.inf)
    for it in range(steps):
        st=model.state(u); vals=st['vals'];J=st['J'];ming=st['gaps'][~model.inc].min()
        value=vals.min() if target is None else -st['gaps'][target]
        if value>bestvalue:bestvalue=value;best=u.copy()
        if it%5==0:say('ITER',it,'elapsed',round(time.time()-t0,2),'min_escape',float(vals.min()),'bad',int((vals<=0).sum()),'gap',float(ming),'trust',trust,'target',float(st['gaps'][target]) if target else None)
        if not np.isfinite(vals).all() or ming<-1e-7 or st['det'].min()<-1e-8:raise ValueError('invalid iterate')
        if target is None and vals.min()>goal:return u,st,'goal'
        if target is not None and st['gaps'][target]<1e-10 and vals.min()>keep/4:return u,st,'contact'
        # Full scalar global check after every trial; dense derivatives only for near contacts.
        mask=(st['gaps']<max(0.03,trust*100))&(~model.inc)
        vi,qi=np.where(mask);gv=st['gaps'][vi,qi];G=model.gap_jac(st,vi,qi)
        n=model.np
        if target is None:
            obj=np.r_[np.zeros(n),-1.0]
            AA=[np.column_stack([-J,np.ones(len(vals))]), np.column_stack([-G,np.zeros(len(gv))])]
            bb=[vals,gv-1e-9]
            healthy=np.isfinite(floors)
            AA.append(np.column_stack([-J[healthy],np.zeros(healthy.sum())]));bb.append(vals[healthy]-floors[healthy])
            bounds=[(-trust,trust)]*n+[(None,goal*2)]
        else:
            ti,tj=target;TG=model.gap_jac(st,np.array([ti]),np.array([tj]))[0]
            obj=TG.copy()
            AA=[-J,-G];bb=[vals-keep,gv-1e-12]
            bounds=[(-trust,trust)]*n
        a=np.vstack(AA);b=np.concatenate(bb)
        # Normalize each constraint to avoid artificial feasibility from HiGHS tolerances.
        scale=np.maximum(np.linalg.norm(a,axis=1),1e-3)
        lp=linprog(obj,A_ub=a/scale[:,None],b_ub=b/scale,bounds=bounds,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:
            trust*=0.5;say('LP_FAIL',it,lp.message)
            if trust<1e-9:return best,model.state(best),'LP_stall'
            continue
        d=lp.x[:n]
        pred=(lp.x[-1]-vals.min()) if target is None else -float(obj@d)
        healthy=np.isfinite(floors)
        accepted=False
        for ls in range(24):
            lam=2.0**(-ls)
            try:ns=model.state(u+lam*d,False)
            except (np.linalg.LinAlgError,ValueError):continue
            nv=ns['vals'];ng=ns['gaps'][~model.inc].min()
            nvalue=nv.min() if target is None else -ns['gaps'][target]
            good=(ng>-1e-11 and ns['det'].min()>-1e-12 and ns['h'].min()>0)
            good=good and (not healthy.any() or np.min(nv[healthy]-floors[healthy])>-1e-12)
            if target is not None:good=good and nv.min()>keep*0.99
            if good and nvalue>=value+max(0.001*lam*pred,-1e-12):
                u+=lam*d;accepted=True
                born=(~np.isfinite(floors))&(nv>keep)
                floors[born]=np.minimum(keep,nv[born]*0.5)
                if ls<=1:trust=min(trust*1.3,0.01)
                elif ls>=3:trust=max(trust*0.6,1e-9)
                break
        if not accepted:
            trust*=0.35
            if trust<1e-9:return best,model.state(best),'line_stall'
        if pred<1e-10 and trust<1e-6:return best,model.state(best),'flat'
    return best,model.state(best),'budget'

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('generator');ap.add_argument('faces');ap.add_argument('--steps',type=int,default=200);ap.add_argument('--out',required=True);ap.add_argument('--target',type=int,nargs=2);ap.add_argument('--keep',type=float,default=2e-5);ap.add_argument('--goal',type=float,default=2e-4);args=ap.parse_args()
    data=json.loads(Path(args.generator).read_text());faces=json.loads(Path(args.faces).read_text());m=Atlas(data,faces)
    u,st,msg=optimize(m,steps=args.steps,target=tuple(args.target) if args.target else None,keep=args.keep,goal=args.goal)
    m.save(u,args.out);print('FINISH',msg,st['vals'].min(),st['gaps'][~m.inc].min(),flush=True)
