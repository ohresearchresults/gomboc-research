"""General positive-shadow polyhedra with explicit actual centroid equality.

Only the four basal points are paired. Every upper direction and radial cost
is independent. Positive-cost radial paths imply referenceU1. The optimizer
imposes all three uniform-volume centroid equations directly; actual own-centre
counts are measured throughout and only an exact physical audit can succeed.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from vertex_geometry import geometry
from persistence_birth import evaluate as persistence
from direct_face_polish import face_scores
from support_geometry import escape
from goal_nomination import preserve

class Family:
    def __init__(self,X):
        assert len(X)<=85 and np.array_equal(X[1],X[0]*[-1,-1,1])and np.array_equal(X[3],X[2]*[-1,-1,1])
        self.n=len(X)-5;self.ad=2*(self.n+2);self.d=self.ad+self.n+1
        P=np.vstack((X[4:-1],X[[0,2]]));r=np.linalg.norm(P,axis=1);angles=np.column_stack((np.arcsin(P[:,2]/r),np.arctan2(P[:,1],P[:,0]))).ravel()
        radii=np.r_[r[:self.n]/X[-1,2],1.];U=np.vstack((P[:self.n]/r[:self.n,None],[0.,0.,1.]));C=U[:-1]@U.T;np.fill_diagonal(C[:,:self.n],-np.inf);caps=np.max(C*radii[None],axis=1);cost=-np.log(radii[:-1]/caps)
        assert min(cost)>0,'input must be a strict referenceU1 body'
        self.q=np.r_[angles,np.maximum(cost,1e-8),0.];Y,_=self.construct(self.q);self.q[-1]=float(np.clip(1-(X[0,2]/X[-1,2])/Y[0,2],1e-7,.6))

    def construct(self,q):
        n=self.n;d=self.d;a=q[:self.ad].reshape(n+2,2);th,ph=a.T;U=np.column_stack((np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),np.sin(th)));DU=np.zeros((n+2,3,d))
        for i in range(n+2):
            DU[i,:,2*i]=[-np.sin(th[i])*np.cos(ph[i]),-np.sin(th[i])*np.sin(ph[i]),np.cos(th[i])];DU[i,:,2*i+1]=[-np.cos(th[i])*np.sin(ph[i]),np.cos(th[i])*np.cos(ph[i]),0]
        W=np.vstack((U[:n],[0.,0.,1.]));DW=np.concatenate((DU[:n],np.zeros((1,3,d))),axis=0);C=W@W.T;cost=np.full_like(C,np.inf);ok=C>1e-12;cost[ok]=-np.log(np.minimum(C[ok],1));cost+=np.r_[q[self.ad:-1],0.][:,None]
        if min(q[self.ad:-1])<0:raise ValueError('negative shadow cost')
        dist=np.full(n+1,np.inf);dist[n]=0;parent=np.full(n+1,-1,int);used=np.zeros(n+1,bool);order=[]
        for _ in range(n+1):
            j=int(np.argmin(np.where(used,np.inf,dist)))
            if not np.isfinite(dist[j]):raise ValueError('disconnected positive-shadow direction graph')
            used[j]=True;order.append(j);new=dist[j]+cost[:,j];take=(new<dist)&(~used);dist[take]=new[take];parent[take]=j
        R=np.exp(-dist);DR=np.zeros((n+1,d))
        for i in order[1:]:
            j=parent[i];Dc=DW[i].T@W[j]+DW[j].T@W[i];DR[i]=np.exp(-q[self.ad+i])*(C[i,j]*DR[j]+R[j]*Dc);DR[i,self.ad+i]-=R[i]
        upper=R[:n,None]*W[:n];Dupper=DR[:n,None,:]*W[:n,:,None]+R[:n,None,None]*DW[:n]
        heights=[];Dheights=[];flip=np.array([-1,-1,1.])
        for i in range(n,n+2):
            if U[i,2]>=-.01:raise ValueError('basal direction is not downward')
            rr=[];DD=[]
            for s in [np.ones(3),flip]:
                u=U[i]*s;Du=DU[i]*s[:,None];cs=W@u;caps=R*cs*(1-1e-9);j=int(np.argmax(caps))
                if caps[j]<=0:raise ValueError('basal direction has no shadow parent')
                Dc=Du.T@W[j]+DW[j].T@u;rr.append(caps[j]);DD.append((1-1e-9)*(cs[j]*DR[j]+R[j]*Dc))
            j=int(np.argmin(rr));heights.append(rr[j]*U[i,2]);Dheights.append(DD[j]*U[i,2]+rr[j]*DU[i,2])
        k=int(np.argmax(heights));h=heights[k]*(1-q[-1]);Dh=Dheights[k]*(1-q[-1]);Dh[-1]-=heights[k];base=[];Dbase=[]
        for i in range(n,n+2):
            r=h/U[i,2];Dr=Dh/U[i,2]-h*DU[i,2]/U[i,2]**2;b=r*U[i];Db=r*DU[i]+U[i,:,None]*Dr;b[2]=h;Db[2]=Dh;base.extend((b,b*flip));Dbase.extend((Db,Db*flip[:,None]))
        X=np.vstack((base,upper,[0.,0.,1.]));DX=np.concatenate((Dbase,Dupper,np.zeros((1,3,d))),axis=0);return X,DX

def run(source,out,steps,seed,eta):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Family(np.load(source));q=F.q.copy();bounds=[(-1.55,1.55),(-20,20)]*F.n+[(-1.55,-.05),(-20,20)]*2+[(1e-8,2.)]*F.n+[(1e-7,.6)];cache={};calls=0;best=np.inf;trace=[];start=time.time()
    def geom(q):
        key=q.tobytes()
        if key==cache.get('key'):return cache['data']
        X,DX=F.construct(q);g=geometry(X);Jg=g['Dg']@DX.reshape(X.size,F.d);gap=X[4:-1,2]-X[0,2]-1e-5;Jgap=DX[4:-1,2]-DX[0,2];result=(X,DX,g,Jg,gap,Jgap);cache.update(key=key,data=result);return result
    rng=np.random.default_rng(seed);t=q+rng.normal(0,1e-4,len(q));t[F.ad:-1]=np.maximum(t[F.ad:-1],1e-4);d=rng.normal(size=F.d);d/=np.linalg.norm(d);h=2e-8;X,DX,g,Jg,gap,Jgap=geom(t);vp,Gp,info=persistence(X,eta);Jp=np.einsum('nc,ncd->d',Gp,DX);gp=geom(t+h*d);gm=geom(t-h*d);fd=(persistence(gp[0],eta)[0]-persistence(gm[0],eta)[0])/(2*h);check=dict(objective_fd=float(fd),objective_analytic=float(Jp@d),centroid_gradient_error=float(max(abs((gp[2]['g']-gm[2]['g'])/(2*h)-Jg@d))),scope='generic direction cell; the initial paired source has nondifferentiable equal shadow choices');(out/'gradient_check.json').write_text(json.dumps(check,indent=2));assert abs(fd-Jp@d)<1e-4*max(1,abs(fd)) and check['centroid_gradient_error']<1e-6
    def objective(q):
        nonlocal calls,best
        calls+=1;X,DX,g,Jg,gap,Jgap=geom(q);v,G,info=persistence(X,eta);J=np.einsum('nc,ncd->d',G,DX);f,_,_=face_scores(g,False);nb=~np.all(g['T']<4,axis=1);u,_=escape(g['Z'][g['vertices']],angular=True);basevalid=len(g['T'])-int(sum(nb))==2 and min(gap)>0
        # When the centroid is not exactly axial, the base foot must also be
        # checked; it is interior if the projected point lies in the quad.
        B=X[[0,2,1,3],:2];Bn=np.roll(B,-1,axis=0);cross2=B[:,0]*Bn[:,1]-B[:,1]*Bn[:,0];area=.5*sum(cross2);edge=Bn-B;rel=g['g'][:2]-B;turns=edge[:,0]*rel[:,1]-edge[:,1]*rel[:,0];base_stable=bool(np.all(turns*np.sign(area)>0))
        S=int(sum(f[nb]<0))+int(base_stable);U=int(sum(u<0));res=float(np.linalg.norm(g['g'],np.inf));feasible=res<1e-8 and min(gap)>-1e-9;row=dict(calls=calls,loss=v,S=S,U=U,centroid_residual=res,feasible=bool(feasible),base_valid=bool(basevalid),base_stable=base_stable,V=len(g['vertices']),Pmax=info['Pmax'],Qmax=info['Qmax'],positive_P=len(info['P']),positive_Q=len(info['Q']),seconds=time.time()-start)
        if feasible and v<best:
            best=v;trace.append(row);np.save(out/'best.npy',X);np.save(out/'best_parameters.npy',q);(out/'best.json').write_text(json.dumps(row,indent=2))
        if basevalid and base_stable and S==U==1:preserve(X,out/f'exact_goal_{calls:06d}','independent positive-shadow vertices with uniform-centroid equality; numerical actual own110 and genuine common base')
        if calls%100==1:print('SHADOW_CENTROID_GOAL',out,row,flush=True)
        return v,J
    r=minimize(objective,q,jac=True,method='SLSQP',bounds=bounds,constraints=[dict(type='eq',fun=lambda q:geom(q)[2]['g'],jac=lambda q:geom(q)[3]),dict(type='ineq',fun=lambda q:geom(q)[4],jac=lambda q:geom(q)[5])],options=dict(maxiter=steps,ftol=1e-11,disp=False));np.save(out/'endpoint_parameters.npy',r.x);(out/'trace.json').write_text(json.dumps(trace,indent=2));(out/'result.json').write_text(json.dumps(dict(message=str(r.message),iterations=int(r.nit),calls=calls,best_feasible=best if np.isfinite(best)else None),indent=2));print('SHADOW_CENTROID_FINITE_STOP',out,str(r.message),calls,best,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1200);p.add_argument('--seed',type=int,default=681503);p.add_argument('--eta',type=float,default=.01);a=p.parse_args();run(a.source,a.out,a.steps,a.seed,a.eta)
