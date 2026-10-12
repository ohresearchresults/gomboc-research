"""Full parameter refinement of one exact negative-self-polar construction.
No metric surrogate or mass-point centroid: final uniform solid integration.
All historical cuts vary simultaneously; saved Cayley rotations remain exact
rational operations, followed by physical centroid closure and its derivative.
"""
import argparse,json,time,copy
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from selfpolar_addcut_goal import topology,mass,center,cayley,audit_numeric,save
from dual_shadow_goal import bars
from support_geometry import escape


def objective(g,mode,derivative):
    if mode=='escape':
        if derivative:v,_,J=escape(g['Z'],g['JZ'],angular=True)
        else:v,_=escape(g['Z'],angular=True);J=None
        root=np.argmax(np.sum(g['Z']**2,axis=1));mask=np.arange(len(v))!=root
        return 1e-8-v[mask],-J[mask]if derivative else None
    return bars(g,derivative)


def cstep(X,DX,b):
    Y=cayley(X,b)
    if DX is None:return Y,None
    den=1-b@b-2*X@b
    A=(1+b@b)*np.eye(3)-2*np.outer(b,b)
    J=(A[None]+2*Y[:,:,None]*b[None,None,:])/den[:,None,None]
    return Y,np.einsum('icj,ijp->icp',J,DX)


def mass_derivative(X,DX,T):
    V,g,M=mass(X,T);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc);DV=dv6.sum(0)/6;DM=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24
    return V,g,M,(DM-g[:,None]*DV)/V


class Chart:
    def __init__(self,source):
        self.source=Path(source);self.definition=json.load(open(self.source/'construction.json'));self.ops=self.definition['operations'];z=np.load(self.source/'body.npz');self.X=z['X'];self.D=z['D'];self.top=topology(self.X,self.D);q=[]
        for op in self.ops:
            if op['kind']=='addcut':
                w=np.array(op['weights']);q.extend(np.log(w[:-1]/w[-1]));q.append(np.log(op['t']))
        self.q=np.array(q);self.d=len(q);self.bounds=[(-35.,35.)]*self.d
        assert self.d==len(self.X)-4

    def construct(self,q,derivative=True):
        X=np.array(self.definition['scaffold'],float);DX=np.zeros((4,3,self.d))if derivative else None;at=0;hist=[]
        for op in self.ops:
            if op['kind']=='cayley':
                X,DX=cstep(X,DX,np.array(op['b']));hist.append(op);continue
            k=op['vertex'];face=np.array(op['face']);nbr=np.array(op['edge_neighbors']);n=len(X);w=np.r_[np.exp(q[at:at+len(face)-1]),1.];t=float(np.exp(q[at+len(face)-1]));W=sum(w);y=w@X[face]/W;x=(1+t)*y;s=X@x
            if s[k]>=-1 or min(np.delete(s,k))<=-1:
                raise ValueError('a historical add-cut left its exact construction cell')
            lam=(-1-s[k])/(s[nbr]-s[k]);z=X[k]+lam[:,None]*(X[nbr]-X[k]);old=np.arange(n)!=k
            if derivative:
                Dy=np.einsum('i,icp->cp',w,DX[face])/W
                for h in range(len(face)-1):Dy[:,at+h]+=w[h]*(X[face[h]]-y)/W
                Dx=(1+t)*Dy;Dx[:,at+len(face)-1]+=t*y;Ds=np.einsum('icp,c->ip',DX,x)+X@Dx;Dl=(-Ds[k]-lam[:,None]*(Ds[nbr]-Ds[k]))/(s[nbr]-s[k])[:,None];Dz=DX[k]+lam[:,None,None]*(DX[nbr]-DX[k])+(X[nbr]-X[k])[:,:,None]*Dl[:,None,:];DX=np.concatenate((DX[old],Dx[None],Dz))
            X=np.vstack((X[old],x,z));h=copy.copy(op);h['weights']=w.tolist();h['t']=t;h.pop('fraction',None);h.pop('interval',None);hist.append(h);at+=len(face)
        if at!=self.d:raise ValueError('construction parameter count mismatch')
        Y,steps=center(X,self.top['tris'])
        if derivative:
            for op in steps:X,DX=cstep(X,DX,np.array(op['b']))
            V,g,M,Dg=mass_derivative(X,DX,self.top['tris']);Db=np.linalg.solve(2*(np.eye(3)+5*M-4*np.outer(g,g)),-Dg);DX+=2*Db[None]+2*np.einsum('ic,ij,jp->icp',X,X,Db)
        else:X=Y
        row,top=audit_numeric(X,self.D,self.top);hist+=steps;g=np.array(row['centroid']);H=-X/(1+X@g)[:,None];data=dict(X=X,Z=X-g,H=H,edges=top['edges'],row=row,history=hist,D=self.D,top=top)
        if derivative:
            _,_,_,Dg=mass_derivative(X,DX,top['tris']);data['DX']=DX;data['JZ']=DX-Dg;data['Jslack']=np.einsum('icp,jc->ijp',DX,X)+np.einsum('ic,jcp->ijp',X,DX);data['Dg']=Dg
        return data


def run(source,out,steps=800,mode='max'):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Chart(source);q=F.q.copy();g=F.construct(q);err=float(max(abs(g['X']-F.X).ravel()));rng=np.random.default_rng(141);d=rng.normal(size=F.d);d/=np.linalg.norm(d);h=1e-7;fp=F.construct(q+h*d,False);fm=F.construct(q-h*d,False);check=dict(source_replay_error=err,physical_centered_derivative_error=float(max(abs((fp['X']-fm['X'])/(2*h)-np.einsum('icp,p->ic',g['DX'],d)).ravel())),centroid_derivative_residual=float(max(abs(g['Dg']).ravel())));(out/'derivative_check.json').write_text(json.dumps(check,indent=2));assert err<1e-8 and check['physical_centered_derivative_error']<3e-6
    (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),parameters=F.d,mode=mode,uniform_mass=True,construction=F.definition),indent=2));trace=[];trust=.1;start=time.time();best=np.inf
    for it in range(steps):
        g=F.construct(q);P,J=objective(g,mode,True);merit=float(max(P,default=0.))if mode in ['max','escape']else float(sum(P));row=dict(it=it,merit=merit,mode=mode,trust=trust,seconds=time.time()-start,**g['row']);trace.append(row);save(g,out/'latest');np.save(out/'latest_parameters.npy',q);(out/'latest.json').write_text(json.dumps(row,indent=2));(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if merit<best:best=merit;save(g,out/'best');np.save(out/'best_parameters.npy',q)
        if it%10==0:print('SELFPOLAR_REFINE',row,flush=True)
        if row['S']==row['U']==1:
            save(g,out/f'potential_{it:05d}');raise RuntimeError('Potential physical110 saved; exact construction audit required')
        n=F.d;ns=len(P)if mode=='sum'else 1;O=csr_matrix((n,ns));I=eye(n);mask=np.triu(~F.D,1);v=(1+g['X']@g['X'].T)[mask];G=g['Jslack'][mask];floor=np.minimum(v*.05,1e-8);A=[hstack((csr_matrix(J),-eye(len(P))if mode=='sum'else -np.ones((len(P),1)),csr_matrix((len(P),n)))),hstack((-csr_matrix(G),csr_matrix((len(v),ns+n)))),hstack((I,O,-I)),hstack((-I,O,-I))];rhs=np.r_[-P,v-floor,np.zeros(2*n)];bounds=[(max(lo-x,-trust),min(hi-x,trust))for x,(lo,hi)in zip(q,F.bounds)]+[(0,None)]*(ns+n);lp=linprog(np.r_[np.zeros(n),np.ones(ns),np.full(n,1e-9)],A_ub=vstack(A,format='csr'),b_ub=rhs,bounds=bounds,method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.));ok=False
        if lp.success:
            for k in range(19):
                qq=q+2.**-k*lp.x[:n]
                try:gg=F.construct(qq,False)
                except(ValueError,np.linalg.LinAlgError):continue
                pp=objective(gg,mode,False)[0];mm=float(sum(pp))if mode=='sum'else float(max(pp,default=0.))
                if gg['row']['S']==gg['row']['U']==1:
                    save(gg,out/f'potential_{it:05d}_line{k}');raise RuntimeError('Potential physical110 saved; exact construction audit required')
                if mm<merit-max(1e-13,merit*1e-9):q=qq;ok=True;row['alpha']=2.**-k;break
        else:row['lp_error']=lp.message
        if ok:
            if k==0:trust=min(.5,trust*1.3)
            elif k>5:trust*=.7
        else:trust*=.4
        if trust<1e-9:break
    g=F.construct(q,False);save(g,out/'endpoint');np.save(out/'endpoint_parameters.npy',q);print('SELFPOLAR_REFINE_FINITE_END',g['row'],time.time()-start,flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=800);p.add_argument('--mode',choices=['max','sum','escape'],default='max');a=p.parse_args();run(a.source,a.out,a.steps,a.mode)
