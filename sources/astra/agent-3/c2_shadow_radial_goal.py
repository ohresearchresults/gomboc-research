"""Constructive U1 C2 family with shortest positive-shadow radial paths.

Upper radii are products of positive direction cosines along a root-reaching
tree. Basal leaves lie strictly within an upper point's Thales ball and share
one exact height. Whenever the uniform centroid lies below zero, raising the
axial apex closes it; every escape witness remains positive. The actual final
body and full exact hull still decide success. At most85 inputs, base>=4.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq,minimize
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from goal_nomination import preserve
from persistence_birth import evaluate as persistence

class Family:
    def __init__(self,X,margin=1e-4,eta=None,radial_costs=False):
        self.n=(len(X)-5)//2;assert len(X)==2*self.n+5 and len(X)<=85
        self.margin=margin;self.eta=eta;self.radial_costs=radial_costs;self.ad=2*(self.n+2);self.d=self.ad+1+(self.n if radial_costs else 0)
        P=np.vstack((X[4:4+self.n],X[[0,2]]));r=np.linalg.norm(P,axis=1)
        angles=np.column_stack((np.arcsin(P[:,2]/r),np.arctan2(P[:,1],P[:,0]))).ravel()
        if radial_costs:
            upper=P[:self.n]/X[-1,2];rr=np.linalg.norm(upper,axis=1);UU=upper/rr[:,None];WW=np.vstack((UU,[0.,0.,1.]));radii=np.r_[rr,1.]
            cc=np.maximum(UU@WW.T,(UU*[-1,-1,1])@WW.T);np.fill_diagonal(cc[:,:self.n],-np.inf);caps=np.max(cc*radii[None],axis=1);costs=-np.log(rr/caps)
            assert min(costs)>0,'source must have strict referenceU1 for radial-cost initialization'
            self.q=np.r_[angles,np.maximum(costs,1e-8),.02]
        else:self.q=np.r_[angles,.02]
        self.source_h=float(X[0,2])

    def construct(self,q):
        n=self.n;d=self.d;a=q[:self.ad].reshape(n+2,2);th,ph=a.T
        U=np.column_stack((np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),np.sin(th)))
        DU=np.zeros((n+2,3,d))
        for i in range(n+2):
            DU[i,:,2*i]=[-np.sin(th[i])*np.cos(ph[i]),-np.sin(th[i])*np.sin(ph[i]),np.cos(th[i])]
            DU[i,:,2*i+1]=[-np.cos(th[i])*np.sin(ph[i]),np.cos(th[i])*np.cos(ph[i]),0]
        W=np.vstack((U[:n],[0.,0.,1.]));DW=np.concatenate((DU[:n],np.zeros((1,3,d))),axis=0)
        flip=np.array([-1,-1,1.]);C0=W@W.T;C1=(W*flip)@W.T;sign=np.where(C0>=C1,1,-1);C=np.maximum(C0,C1)
        nodecost=np.r_[q[self.ad:self.ad+n],0.]if self.radial_costs else np.full(n+1,-np.log1p(-self.margin))
        if min(nodecost)<0:raise ValueError('negative radial shadow cost')
        cost=np.full_like(C,np.inf);ok=C>1e-12;cost[ok]=-np.log(np.minimum(C[ok],1));cost+=nodecost[:,None]
        dist=np.full(n+1,np.inf);dist[n]=0;parent=np.full(n+1,-1,int);used=np.zeros(n+1,bool);order=[]
        for _ in range(n+1):
            j=int(np.argmin(np.where(used,np.inf,dist)))
            if not np.isfinite(dist[j]):raise ValueError('disconnected positive-cosine graph')
            used[j]=True;order.append(j);new=dist[j]+cost[:,j];take=(new<dist)&(~used);dist[take]=new[take];parent[take]=j
        radii=np.exp(-dist);DR=np.zeros((n+1,d))
        for i in order[1:]:
            j=parent[i];s=np.array([sign[i,j],sign[i,j],1.]);cc=C[i,j]
            Dc=np.einsum('cp,c->p',DW[i],W[j]*s)+np.einsum('c,cp->p',W[i]*s,DW[j])
            DR[i]=np.exp(-nodecost[i])*(cc*DR[j]+radii[j]*Dc)
            if self.radial_costs:DR[i,self.ad+i]-=radii[i]
        upper=radii[:n,None]*W[:n];Dupper=DR[:n,None,:]*W[:n,:,None]+radii[:n,None,None]*DW[:n]
        leafcaps=[];Dleafcaps=[];leafparents=[]
        leaf_margin=1e-8 if self.radial_costs else self.margin
        for i in range(n,n+2):
            c0=W@U[i];c1=(W*flip)@U[i];sg=np.where(c0>=c1,1,-1);cs=np.maximum(c0,c1);caps=radii*cs*(1-leaf_margin);j=int(np.argmax(caps))
            if caps[j]<=0 or U[i,2]>=-.01:raise ValueError('invalid basal leaf')
            ss=np.array([sg[j],sg[j],1.]);Dc=np.einsum('cp,c->p',DU[i],W[j]*ss)+np.einsum('c,cp->p',U[i]*ss,DW[j])
            Dr=(1-leaf_margin)*(cs[j]*DR[j]+radii[j]*Dc)
            leafcaps.append(caps[j]*U[i,2]);Dleafcaps.append(Dr*U[i,2]+caps[j]*DU[i,2]);leafparents.append(j)
        k=int(np.argmax(leafcaps));low=leafcaps[k];Dlow=Dleafcaps[k];frac=q[-1];h=low*(1-frac);Dh=Dlow*(1-frac);Dh[-1]-=low
        base=[];Db=[]
        for i in range(n,n+2):
            rr=h/U[i,2];Drr=Dh/U[i,2]-h*DU[i,2]/U[i,2]**2
            b=rr*U[i];D=rr*DU[i]+U[i,:,None]*Drr
            b[2]=h;D[2]=Dh;base.extend((b,b*flip));Db.extend((D,D*flip[:,None]))
        X=np.vstack((base,upper,upper*flip,[0.,0.,1.]));DX=np.concatenate((Db,Dupper,Dupper*flip[None,:,None],np.zeros((1,3,d))),axis=0)
        return X,DX,dict(parent=parent.tolist(),leafparents=leafparents,margin=self.margin)

    def evaluate(self,q,derivative=True):
        X,DX,meta=self.construct(q);gg=geometry(X,False);initial_g=float(gg['g'][2]);closed=False
        if initial_g<0:
            def mass(t):X[-1,2]=t;return float(geometry(X,False)['g'][2])
            hi=2.
            while mass(hi)<0 and hi<64:hi*=2
            X[-1,2]=brentq(mass,1.,hi,xtol=5e-15,rtol=9e-16);closed=True
        full=geometry(X,derivative)
        if derivative:
            centre_J=full['Dg']@DX.reshape(X.size,self.d)
            if closed:DX[-1,2]=-centre_J[2]/full['Dg'][2,-1];centre_J[:]=0
            g=dict(full,DX=DX,DZ=DX,Z=X)
        else:g=dict(full,Z=X)
        # The face score is relative to the reference0, which equals the
        # actual uniform centroid ONLY in the explicit closed branch.
        f,Jf,_=face_scores(g,derivative);nonbase=~np.all(g['T']<4,axis=1)
        H=np.linalg.solve(X[g['T']],np.ones((len(g['T']),3,1)))[:,:,0];hn=np.linalg.norm(H,axis=1);height=1/hn;h=X[0,2]
        global_gap=height/(-h)-1
        if derivative:
            DH=np.linalg.solve(X[g['T']],-np.einsum('ic,iacp->iap',H,DX[g['T']]));Jh=-np.einsum('ic,icp->ip',H,DH)/hn[:,None]**3
            Jglobal=Jh/(-h)+height[:,None]*DX[0,2]/h**2
        lower=X[4:-1,2]-h
        vf=f[nonbase];vg=global_gap[nonbase];eps=1e-6
        loss=float(np.maximum(eps-vf,0).sum()+.2*np.maximum(eps-vg,0).sum()+100*np.maximum(1e-5-lower,0).sum()+30*max(initial_g,0))
        grad=None
        if derivative:
            grad=-Jf[nonbase][vf<eps].sum(0)-.2*Jglobal[nonbase][vg<eps].sum(0)-100*(DX[4:-1,2]-DX[0,2])[lower<1e-5].sum(0)
            if not closed:grad+=30*centre_J[2]
        bars={}
        if self.eta is not None:
            value,G,info=persistence(X,self.eta)
            loss=float(value+100*np.maximum(1e-5-lower,0).sum()+30*max(initial_g,0))
            bars=dict(Pmax=info['Pmax'],Qmax=info['Qmax'],positive_P=len(info['P']),positive_Q=len(info['Q']))
            if derivative:
                grad=np.einsum('nc,ncd->d',G,DX)-100*(DX[4:-1,2]-DX[0,2])[lower<1e-5].sum(0)
                if not closed:grad+=30*centre_J[2]
        vv,_=escape(full['Z'][full['vertices']],angular=True);S=1+int(sum(vf<0));U=int(sum(vv<0));base_valid=bool(len(g['T'])-int(sum(nonbase))==2 and min(lower)>0)
        row=dict(loss=loss,reference_S=S,actual_U=U,closed=closed,base_valid=base_valid,V=len(full['vertices']),initial_centroid_z=initial_g,actual_centroid_z=float(full['g'][2]),tip=float(X[-1,2]),min_global_gap=float(min(vg)),min_face=float(min(vf)),min_height_gap=float(min(lower)),**bars)
        return loss,grad,X,row,meta

def run(source,out,iterations,seed,jitter,eta=None,radial_costs=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Family(np.load(source),eta=eta,radial_costs=radial_costs);q=F.q.copy();rng=np.random.default_rng(seed);q[:F.ad]+=rng.normal(0,jitter,F.ad);q[-1]=.02
    bounds=[(-1.55,1.55),(-20.,20.)]*F.n+[(-1.55,-.05),(-20.,20.)]*2+([(1e-8,2.)]*F.n if radial_costs else [])+[(.00001,.6)]
    q=np.array([np.clip(v,*b)for v,b in zip(q,bounds)]);calls=0;best=np.inf;trace=[];start=time.time()
    # Compare the scalar derivative on a generic cell, not an optimized tie.
    test=q+rng.normal(0,1e-5,len(q))
    if radial_costs:test[F.ad:-1]=np.maximum(test[F.ad:-1],1e-4)
    d=rng.normal(size=len(q));d/=np.linalg.norm(d);h=2e-8
    v,J,_,_,_=F.evaluate(test);vp=F.evaluate(test+h*d,False)[0];vm=F.evaluate(test-h*d,False)[0];check=dict(fd=(vp-vm)/(2*h),analytic=float(J@d));(out/'gradient_check.json').write_text(json.dumps(check,indent=2));assert abs(check['fd']-check['analytic'])<1e-4*max(1,abs(check['fd']))
    def objective(q):
        nonlocal calls,best
        calls+=1
        value,J,X,row,meta=F.evaluate(q);row.update(calls=calls,seconds=time.time()-start)
        if row['closed']and row['base_valid']and row['reference_S']==row['actual_U']==1:
            d=out/f'exact_goal_{calls:06d}';d.mkdir();np.save(d/'parameters.npy',q);(d/'construction.json').write_text(json.dumps(meta,indent=2));preserve(X,d/'exact','C2 shortest positive-shadow radial construction, actual axial homogeneous mass closed, numerical110')
        if value<best:
            best=value;trace.append(row);np.save(out/'best.npy',X);np.save(out/'best_parameters.npy',q);(out/'best.json').write_text(json.dumps(row,indent=2));(out/'best_construction.json').write_text(json.dumps(meta,indent=2))
            if len(trace)%20==1:print('C2_SHADOW_RADIAL',out,row,flush=True)
        return value,J
    r=minimize(objective,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=iterations,maxls=40,ftol=1e-14,gtol=1e-10,maxcor=20))
    (out/'trace.json').write_text(json.dumps(trace,indent=2));(out/'result.json').write_text(json.dumps(dict(message=str(r.message),iterations=int(r.nit),calls=calls,best=best),indent=2));print('C2_SHADOW_RADIAL_FINITE_STOP',out,calls,best,str(r.message),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--iterations',type=int,default=2000);p.add_argument('--seed',type=int,default=86042);p.add_argument('--jitter',type=float,default=0);p.add_argument('--eta',type=float);p.add_argument('--radial-costs',action='store_true');a=p.parse_args();run(a.source,a.out,a.iterations,a.seed,a.jitter,a.eta,a.radial_costs)
