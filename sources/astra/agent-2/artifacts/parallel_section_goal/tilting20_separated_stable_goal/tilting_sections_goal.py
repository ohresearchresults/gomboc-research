"""Complete own-centroid persistence search with independent section tilts.
All noncontact support inequalities participate in the physical geometry
model. Only rows provably redundant in the explicit linear trust box are
omitted from a local LP. A bounded nonlinear correction solves the actual
support inequalities after a proposed step; the complete real hull and mass
are then recomputed. Every positive finite bar remains in the loss.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from tilting_section_family import TiltingSectionFamily

def run(src,normal_src,out,L,iterations=600,tau=.02,protect_stable_apex_fraction=0.):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nr=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'source_normals.npy').write_bytes(nr);q=np.load(out/'source_q.npy');normals=np.load(out/'source_normals.npy');m=len(normals);H=m*L;D=len(q);V=F=H+1;K=2*H;fam=TiltingSectionFamily(normals,L);non=np.argwhere(~fam.contact);s=fam.state(q);nscale=np.linalg.norm(s['N'],axis=1);ns0=fam.independent_construct(q)[3];det_scale=np.linalg.norm(ns0,axis=2)*np.linalg.norm(np.roll(ns0,-1,axis=1),axis=2);G=len(non)+L+H+2*m
    sr=int(np.argmax(np.sum(s['Y']**2,1)));other_faces=np.delete(np.arange(F),sr);protected=protect_stable_apex_fraction>0
    if protected:
        if not 0<protect_stable_apex_fraction<1:raise ValueError('explicit constructive separation fraction must lie in (0,1)')
        hits=np.flatnonzero((non[:,0]==sr)&(non[:,1]==V-1))
        if len(hits)!=1:raise ValueError('the source stable face already meets the apex')
        protected_gap_index=int(hits[0]);G+=F-1
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nr).hexdigest(),m=m,L=L,tau=tau,protect_stable_apex_fraction=protect_stable_apex_fraction,protected_stable_face=sr if protected else None,geometry_normalization='current Euclidean facet normals' if protected else 'fixed source facet scales',method=__doc__,controls='h0_m, side_vertical_coefficients_(L-1)*m, levels_L, section_tilts_2L, bottom_azimuths_m'),indent=2)+'\n')
    for name in ['tilting_section_family.py','tilting_sections_goal.py','parallel_section_family.py']:(out/name).write_bytes((Path(__file__).parent/name).read_bytes())
    @jax.jit
    def geometry(q):
        X,N,d,ns=fam.construct(q);scale=jnp.sqrt(jnp.sum(N*N,1)) if protected else jnp.asarray(nscale);gap=(d[non[:,0]]-jnp.sum(N[non[:,0]]*X[non[:,1]],1))/scale[non[:,0]];z=q[H:H+L];theta=q[-m:];angles=jnp.diff(jnp.r_[theta,theta[0]+2*jnp.pi]);det=(ns[:,:,0]*jnp.roll(ns[:,:,1],-1,axis=1)-ns[:,:,1]*jnp.roll(ns[:,:,0],-1,axis=1))/jnp.asarray(det_scale);geo=jnp.r_[gap,jnp.diff(jnp.r_[z,1.]),det.ravel(),angles,jnp.pi-angles]
        if protected:
            _,_,_,g,_,_,_=fam.physical(q);foot=g+N[sr]*(d[sr]-N[sr]@g)/(N[sr]@N[sr]);geo=jnp.r_[geo,(d[other_faces]-N[other_faces]@foot)/scale[other_faces]]
        return geo
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
    s=model(q);pp,qp=s['pp'],s['qp'];f=np.asarray(pieces(q,pp,qp));floor=np.minimum(f[K:K+G]*.01,1e-7);floor[len(non):]=np.minimum(f[K+len(non):K+G]*.01,1e-6)
    if protected:
        floor[protected_gap_index]=f[K+protected_gap_index]*protect_stable_apex_fraction;floor[-(F-1):]=np.minimum(f[K+G-(F-1):K+G]*.01,1e-8)
        if floor.min()<=0:raise ValueError('source selected stable face lacks strict interior foot margins')
    def independent_geometry(qq):
        X,N,d,ns=fam.independent_construct(qq);scale=np.sqrt(np.sum(N*N,1)) if protected else nscale;gap=(d[non[:,0]]-np.sum(N[non[:,0]]*X[non[:,1]],1))/scale[non[:,0]];z=qq[H:H+L];theta=qq[-m:];angles=np.diff(np.r_[theta,theta[0]+2*np.pi]);det=(ns[:,:,0]*np.roll(ns[:,:,1],-1,axis=1)-ns[:,:,1]*np.roll(ns[:,:,0],-1,axis=1))/det_scale;geo=np.r_[gap,np.diff(np.r_[z,1.]),det.ravel(),angles,np.pi-angles]
        if protected:
            _,_,_,g,_,_,_=fam.independent_physical(qq);foot=g+N[sr]*(d[sr]-N[sr]@g)/(N[sr]@N[sr]);geo=np.r_[geo,(d[other_faces]-N[other_faces]@foot)/scale[other_faces]]
        return geo
    def independent(qq):
        X,Z,Y,g,v,N,d=fam.independent_physical(qq)
        def bars(B,pairs):
            r,a,b=B[pairs[:,0]],B[pairs[:,1]],B[pairs[:,2]];delta=b-a;t0=-np.sum(a*delta,1)/np.sum(delta*delta,1);t=np.where(np.real(t0)<0,0,np.where(np.real(t0)>1,1,t0));foot=a+t[:,None]*delta;birth=np.sum(r*r,1);return (birth-np.sum(foot*foot,1))/birth
        return np.r_[bars(Z,pp),bars(Y,qp),independent_geometry(qq),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(72148).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,pp,qp));ve=float(np.max(abs(independent(q)-f)));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('independent tilted-section derivative gate failed')
    def repair(trial,W,limit):
        total=0.
        for k in range(12):
            geo=np.asarray(geometry(trial))
            if not np.isfinite(geo).all():raise ValueError('nonfinite trial support geometry')
            if np.min(geo/floor)>=.999:return trial,total,k
            C=np.asarray(geometry_jac(trial))@W;rhs=geo-floor;active=rhs<limit*np.sum(abs(C),1)+1e-10;A=np.r_[np.c_[-C[active],np.zeros(active.sum())],np.c_[np.eye(D),-np.ones(D)],np.c_[-np.eye(D),-np.ones(D)]];b=np.r_[rhs[active],np.zeros(2*D)];r=linprog(np.r_[np.zeros(D),1.],A_ub=A*1000,b_ub=b*1000,bounds=[(-limit,limit)]*D+[(0,limit)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9))
            if not r.success:raise ValueError('bounded actual-geometry corrector LP failed: '+r.message)
            if np.max(np.maximum(floor-geo-C@r.x[:D],0))>1e-7:raise ValueError('geometry corrector fails complete original local rows')
            trial=trial+W@r.x[:D];total+=float(r.x[-1])
        raise ValueError('bounded nonlinear support correction did not converge')
    history=[];trust=.04;fewest=np.inf;start=time.time()
    for it in range(iterations):
        s=model(q);f=np.asarray(pieces(q,s['pp'],s['qp']));J=np.asarray(derivative(q,s['pp'],s['qp']));row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        if s['S']+s['U']<fewest:
            fewest=s['S']+s['U'];np.save(out/f'fewest_{it:04d}_q.npy',q);(out/f'fewest_{it:04d}.json').write_text(json.dumps(row,indent=2)+'\n')
        history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('TILTING_SECTION_PHYSICAL_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_initial_normals.npy',np.c_[np.cos(q[-m:]),np.sin(q[-m:])]);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(row,m=m,L=L),indent=2)+'\n');return q
        emb=J[K+G:];metric=np.vstack([emb[:3*V]/np.sqrt(np.mean(s['Z']**2)),emb[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D);B=J[:K]@W;C=J[K:K+G]@W;rhs=f[K:K+G]-floor;active=rhs<bound*np.sum(abs(C),1)+1e-10;A=vstack([hstack([csr_matrix(B),-eye(K)]),hstack([-csr_matrix(C[active]),csr_matrix((active.sum(),K))])],format='csr');b=np.r_[-f[:K],rhs[active]];weights=1/(tau+np.maximum(f[:K],0));r=linprog(np.r_[np.zeros(D),weights],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*K,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not r.success:row['lp_failure']=r.message;trust*=.4;continue
        if max(float(np.maximum(A@r.x-b,0).max()),float(np.maximum(floor-f[K:K+G]-C@r.x[:D],0).max()))>1e-7:raise ValueError('tilted-section physical proposal fails complete original local rows')
        step=W@r.x[:D];accepted=False;row['retained_geometry_rows']=int(active.sum())
        for back in range(20):
            try:trial,correction,corrections=repair(q+2**-back*step,W,max(bound,.002));t=model(trial)
            except (ValueError,AssertionError,np.linalg.LinAlgError):continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;row.update(alpha=2**-back,geometry_correction_norm=correction,geometry_correction_iterations=corrections);accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-12:break
    np.save(out/'final_q.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(goal_complete=False,iterations=iterations),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 600,float(sys.argv[6]) if len(sys.argv)>6 else .02,float(sys.argv[7]) if len(sys.argv)>7 else 0.)
