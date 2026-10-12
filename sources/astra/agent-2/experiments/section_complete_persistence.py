"""All finite primal and polar persistence bars on one filled section body.
The discovery objective is sum log(1+bar/tau), with no discarded positive
bars. A reweighted positive-part LP majorizes the current complete barcode.
Every trial rebuilds both complete barcodes after actual volume integration.
Shared azimuths move while an explicit linear support projection restores
genuine polygon/quad convexity. Only the full exact census can qualify.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from free_angle_section_family import FreeAngleSectionFamily

def run(src,normal_src,out,L,iterations=1800,tau=.01):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nr=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'source_normals.npy').write_bytes(nr);oldq=np.load(out/'source_q.npy');normals=np.load(out/'source_normals.npy');m=len(normals);H=m*L;theta=np.unwrap(np.arctan2(normals[:,1],normals[:,0]));q=np.r_[oldq,theta] if len(oldq)==H+L else oldq.copy();fam=FreeAngleSectionFamily(normals,L);V=F=H+1;K=2*H;G=H+m*(L-1)+2*m;indices=np.r_[np.arange(H),np.arange(H+L,H+L+m)];D=len(indices)
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nr).hexdigest(),m=m,L=L,tau=tau,method=__doc__),indent=2)+'\n')
    for name in ['free_angle_section_family.py','section_complete_persistence.py','parallel_section_family.py']:(out/name).write_bytes((Path(__file__).parent/name).read_bytes())
    @jax.jit
    def geometry(q):
        h=q[:H].reshape(L,m);z=q[H:H+L];theta=q[-m:];n=jnp.c_[jnp.cos(theta),jnp.sin(theta)];matrices=jnp.stack([n,jnp.roll(n,-1,axis=0)],axis=1);rhs=jnp.stack([h,jnp.roll(h,-1,axis=1)],axis=2);xy=jnp.linalg.solve(matrices[None,:,:,:],rhs[:,:,:,None]).squeeze(-1);tangent=jnp.c_[-n[:,1],n[:,0]];length=jnp.sum((xy-jnp.roll(xy,1,axis=1))*tangent[None,:,:],axis=2);dz=jnp.diff(jnp.r_[z,1.]);slope=jnp.diff(jnp.r_[h,jnp.zeros((1,m))],axis=0)/dz[:,None];curv=slope[:-1]-slope[1:];angles=jnp.diff(jnp.r_[theta,theta[0]+2*jnp.pi]);return jnp.r_[length.ravel(),curv.ravel(),angles,jnp.pi-angles]
    geometry_jac=jax.jit(jax.jacfwd(geometry))
    @jax.jit
    def pieces(q,pp,qp):
        X,Z,Y,g,v,N,d=fam.physical(q)
        def bars(B,pairs):
            r,a,b=B[pairs[:,0]],B[pairs[:,1]],B[pairs[:,2]];delta=b-a;t=jnp.clip(-jnp.sum(a*delta,1)/jnp.sum(delta*delta,1),0.,1.);foot=a+t[:,None]*delta;birth=jnp.sum(r*r,1);return (birth-jnp.sum(foot*foot,1))/birth
        return jnp.r_[bars(Z,pp),bars(Y,qp),geometry(q),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);s['objective']=float(np.log1p(s['P']/tau).sum()+np.log1p(s['Q']/tau).sum());return s
    s=model(q);pp,qp=s['pp'],s['qp'];f=np.asarray(pieces(q,pp,qp));floor=np.minimum(f[K:K+G]*.01,1e-7);floor[-2*m:]=1e-5
    if np.min(f[K:K+G]-floor)<0:raise ValueError('source lacks the declared strict geometry margin')
    def independent(qq):
        X,Z,Y,g,v,N,d=fam.independent_physical(qq)
        def bars(B,pairs):
            r,a,b=B[pairs[:,0]],B[pairs[:,1]],B[pairs[:,2]];delta=b-a;t0=-np.sum(a*delta,1)/np.sum(delta*delta,1);t=np.where(np.real(t0)<0,0,np.where(np.real(t0)>1,1,t0));foot=a+t[:,None]*delta;birth=np.sum(r*r,1);return (birth-np.sum(foot*foot,1))/birth
        h=qq[:H].reshape(L,m);z=qq[H:H+L];theta=qq[-m:];n=np.c_[np.cos(theta),np.sin(theta)];xy=X[:-1,:2].reshape(L,m,2);length=np.sum((xy-np.roll(xy,1,axis=1))*np.c_[-n[:,1],n[:,0]][None,:,:],axis=2);slope=np.diff(np.r_[h,np.zeros((1,m))],axis=0)/np.diff(np.r_[z,1.])[:,None];angles=np.diff(np.r_[theta,theta[0]+2*np.pi]);geo=np.r_[length.ravel(),(slope[:-1]-slope[1:]).ravel(),angles,np.pi-angles];return np.r_[bars(Z,pp),bars(Y,qp),geo,Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(459182).normal(size=len(q));direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,pp,qp));ve=float(np.max(abs(independent(q)-f)));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('complete-persistence independent derivative gate failed')
    def repair(trial):
        geo=np.asarray(geometry(trial))
        if np.min(geo[-2*m:]-floor[-2*m:])<0:raise ValueError('trial directions violate strict cyclic order')
        if np.min(geo-floor)>=0:return trial,0.
        C=np.asarray(geometry_jac(trial))[:-2*m,:H];b=geo[:-2*m]-floor[:-2*m];A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[np.eye(H),-np.ones(H)],np.c_[-np.eye(H),-np.ones(H)]];rhs=np.r_[b,np.zeros(2*H)];r=linprog(np.r_[np.zeros(H),1.],A_ub=A*1000,b_ub=rhs*1000,bounds=[(None,None)]*H+[(0,None)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10))
        if not r.success:raise ValueError('convexity support projection failed: '+r.message)
        result=trial.copy();result[:H]+=r.x[:H]
        if np.min(np.asarray(geometry(result))/floor)<.99:raise ValueError('projected physical support controls fail geometry readback')
        return result,float(r.x[-1])
    history=[];trust=.04;fewest=np.inf;start=time.time()
    for it in range(iterations):
        s=model(q);f=np.asarray(pieces(q,s['pp'],s['qp']));J=np.asarray(derivative(q,s['pp'],s['qp']))[:,indices];row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        if s['S']+s['U']<fewest:
            fewest=s['S']+s['U'];np.save(out/f'fewest_{it:04d}_q.npy',q);(out/f'fewest_{it:04d}.json').write_text(json.dumps(row,indent=2)+'\n')
        history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%10==0:print('SECTION_COMPLETE_PERSISTENCE_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_normals.npy',np.c_[np.cos(q[-m:]),np.sin(q[-m:])]);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        emb=J[K+G:];metric=np.vstack([emb[:3*V]/np.sqrt(np.mean(s['Z']**2)),emb[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D);B=J[:K]@W;C=J[K:K+G]@W;A=vstack([hstack([csr_matrix(B),-eye(K)]),hstack([-csr_matrix(C),csr_matrix((G,K))])],format='csr');b=np.r_[-f[:K],f[K:K+G]-floor];weights=1/(tau+np.maximum(f[:K],0));r=linprog(np.r_[np.zeros(D),weights],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*K,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not r.success:row['lp_failure']=r.message;trust*=.4;continue
        if np.maximum(A@r.x-b,0).max()>1e-7:raise ValueError('complete-bar physical proposal fails original LP rows')
        step=np.zeros_like(q);step[indices]=W@r.x[:D];accepted=False
        for back in range(24):
            try:trial,correction=repair(q+2**-back*step);t=model(trial)
            except (ValueError,AssertionError,np.linalg.LinAlgError):continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;row['alpha']=2**-back;row['support_repair_Linf']=correction;accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-12:break
    np.save(out/'final_q.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(goal_complete=False,iterations=iterations),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 1800,float(sys.argv[6]) if len(sys.argv)>6 else .01)
