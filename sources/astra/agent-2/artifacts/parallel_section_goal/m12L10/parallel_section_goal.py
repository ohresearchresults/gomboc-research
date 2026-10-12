"""Joint own-centroid equilibrium search in the exact quadrilateral-section family.
Both rooted all-pair escape trees and the full uniform mass are recomputed at
each accepted physical deformation. Complete section convexity is constrained
by ordered heights, positive polygon edge lengths, and decreasing side slopes.
The true feature count is fixed by genuine planar quadrilaterals, not triangles.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from parallel_section_family import SectionFamily
from apex_polygon_direct_goal import minimum_route

def run(src,normal_src,out,L,iterations=1500,eps=1e-6,mode='sum'):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nraw=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'normals.npy').write_bytes(nraw);q=np.load(out/'source_q.npy');normals=np.load(out/'normals.npy');fam=SectionFamily(normals,L);m=fam.m;D=len(q);K=2*(m*L+1);G=L+m*L+m*(L-1);V=m*L+1
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nraw).hexdigest(),m=m,L=L,eps=eps,mode=mode,method=__doc__),indent=2)+'\n')
    @jax.jit
    def pieces(q,up,sp):
        X,Z,Y,g,v,N,d=fam.physical(q)
        def angle(B,p):
            delta=B[p]-B;den=jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(delta*delta,1),1e-40));return jnp.where(p==jnp.arange(len(B)),0.,jnp.sum(B*delta,1)/den)
        xy=X[:-1,:2].reshape(L,m,2);tangent=jnp.c_[-jnp.asarray(normals)[:,1],jnp.asarray(normals)[:,0]];length=jnp.sum((xy-jnp.roll(xy,1,axis=1))*tangent[None,:,:],axis=2);z=q[m*L:];h=q[:m*L].reshape(L,m);dz=jnp.diff(jnp.r_[z,1.]);slope=jnp.diff(jnp.r_[h,jnp.zeros((1,m))],axis=0)/dz[:,None];curv=slope[:-1]-slope[1:]
        return jnp.r_[angle(Z,up),angle(Y,sp),dz,length.ravel(),curv.ravel(),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);ur=int(np.argmax(np.sum(s['Z']**2,1)));sr=int(np.argmax(np.sum(s['Y']**2,1)));up,uw,uc=minimum_route(s['Z'],ur,eps);sp,sw,sc=minimum_route(s['Y'],sr,eps);s.update(up=up,sp=sp,roots=[ur,sr],ucost=uc,scost=sc,objective=uc+sc);return s
    first=model(q);up,sp=first['up'],first['sp'];f=np.asarray(pieces(q,up,sp));floor=np.minimum(f[K:K+G]*.01,1e-7)
    if floor.min()<=0:raise ValueError('initial genuine-section convexity constraints are not strict')
    def independent(qq):
        X,Z,Y,g,v,N,d=fam.independent_physical(qq)
        def angle(B,p):
            active=p!=np.arange(len(B));a=np.zeros(len(B),dtype=qq.dtype);delta=B[p[active]]-B[active];a[active]=np.sum(B[active]*delta,1)/np.sqrt(np.sum(B[active]*B[active],1)*np.sum(delta*delta,1));return a
        xy=X[:-1,:2].reshape(L,m,2);tangent=np.c_[-normals[:,1],normals[:,0]];length=np.sum((xy-np.roll(xy,1,axis=1))*tangent[None,:,:],axis=2);z=qq[m*L:];h=qq[:m*L].reshape(L,m);dz=np.diff(np.r_[z,1.]);slope=np.diff(np.r_[h,np.zeros((1,m))],axis=0)/dz[:,None];curv=slope[:-1]-slope[1:]
        return np.r_[angle(Z,up),angle(Y,sp),dz,length.ravel(),curv.ravel(),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(2830291).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,up,sp));ve=float(np.max(abs(independent(q)-f)));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('independent quadrilateral-section derivative gate failed')
    start=time.time();history=[];trust=.04;fewest=np.inf
    for it in range(iterations):
        s=model(q);f=np.asarray(pieces(q,s['up'],s['sp']));J=np.asarray(derivative(q,s['up'],s['sp']));active=np.setdiff1d(np.arange(K),[s['roots'][0],V+s['roots'][1]]);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','ucost','scost','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        if s['S']+s['U']<fewest:
            fewest=s['S']+s['U'];np.save(out/f'fewest_{it:04d}_q.npy',q);(out/f'fewest_{it:04d}.json').write_text(json.dumps(row,indent=2)+'\n')
        history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%10==0:print('PARALLEL_SECTION_PHYSICAL_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        embedding=J[K+G:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D);B=J[active]@W;C=J[K:K+G]@W;N=len(active)
        if mode!='sum':raise ValueError('this producer uses the complete minimum-arborescence sum objective')
        A=vstack([hstack([-csr_matrix(B),-eye(N)]),hstack([-csr_matrix(C),csr_matrix((G,N))])],format='csr');b=np.r_[f[active]-eps,f[K:K+G]-floor]
        sol=linprog(np.r_[np.zeros(D),np.ones(N)],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*N,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:row['lp_failure']=sol.message;trust*=.4;continue
        if float(np.maximum(A@sol.x-b,0).max())>1e-7:raise ValueError('section LP failed original-row validation')
        step=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+2**-back*step
            try:t=model(trial);tf=np.asarray(pieces(trial,t['up'],t['sp']))
            except (ValueError,AssertionError,np.linalg.LinAlgError):continue
            if np.min(tf[K:K+G]/floor)<.99:continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;row['alpha']=2**-back;accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-12:break
    np.save(out/'final_q.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(goal_complete=False,iterations=iterations),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 1500)
