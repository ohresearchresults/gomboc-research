"""Complete stable persistence descent at the actual centroid, keeping U1.
The family has one prescribed apex polygon and otherwise freely changing
physical incidence. Every finite polar persistence bar is included, without
a positive-bar cutoff. Modes max and square are separate declared objectives.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def run(src,out,m=4,mode='max',iterations=1200,eps=1e-10,edge_limit=248,allow_top_retirement=False,keep_stable_roots=False,cap_owner=None,stable_limit=None,cap_geometry='triangle',cap_search_edge_limit=280,cap_point_count=2):
    if mode not in ['max','square']:raise ValueError('unknown persistence objective')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw_source=src.read_bytes();(out/'source.npy').write_bytes(raw_source);q=np.load(out/'source.npy').copy();D=len(q)
    if cap_owner is None:family=ApexFamily(m,edge_limit=edge_limit,allow_top_retirement=allow_top_retirement)
    elif cap_geometry=='triangle':
        from physical_triangle_cap_family import TriangleCapFamily
        family=TriangleCapFamily(m,cap_owner,edge_limit)
    elif cap_geometry=='point':
        from physical_point_cap_family import PointCapFamily
        family=PointCapFamily(m,cap_search_edge_limit)
    elif cap_geometry=='multiple':
        from physical_multiple_cap_family import MultipleCapFamily
        family=MultipleCapFamily(m,cap_point_count,cap_search_edge_limit)
    else:raise ValueError('unknown explicit physical cap construction')
    start=time.time();history=[];trust=.025
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw_source).hexdigest(),apex=m,mode=mode,eps=eps,edge_limit=edge_limit,cap_geometry=cap_geometry,cap_point_count=cap_point_count if cap_geometry=='multiple' else 1,cap_search_edge_limit=cap_search_edge_limit,allow_top_retirement=allow_top_retirement,keep_stable_roots=keep_stable_roots,cap_owner=cap_owner,stable_limit=stable_limit,coordinate_frame='fixed base anchor, no recentering' if cap_owner is not None else 'actual-centroid apex similarity',method=__doc__),indent=2)+'\n')
    @jax.jit
    def pieces(q,R,T,A,up,sp,qp):
        X,Z,Y,g,v=family.physical(q,R,T,A);ug=jnp.sum(Z*(Z[up]-Z),1)/jnp.sum(Z*Z,1);sg=jnp.sum(Y*(Y[sp]-Y),1)/jnp.sum(Y*Y,1)
        root,a,b=Y[qp[:,0]],Y[qp[:,1]],Y[qp[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,1)/jnp.sum(d*d,1),0,1);birth=jnp.sum(root*root,1);bars=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,1),0)/birth
        return jnp.r_[ug,sg,bars,Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=family.state(q)
        for B,key in [(s['Z'],'u'),(s['Y'],'s')]:
            raw=np.einsum('ij,ikj->ik',B,B[None]-B[:,None])/np.sum(B*B,1)[:,None];np.fill_diagonal(raw,-np.inf);s[key+'p']=raw.argmax(1);s[key+'g']=raw.max(1)
        s['objective']=float(s['Q'].max()) if mode=='max' else float(s['Q']@s['Q']);return s
    def args(s):return [s[k] for k in ['R','T','A','up','sp','qp']]
    def jac(q,s):return np.asarray(derivative(q,*args(s)))
    def metric(s,J):
        V,F=s['V'],s['F'];G=J[V+2*F-1:];M=np.vstack([G[:3*V]/np.sqrt(np.mean(s['Z']**2)),G[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,d,Vt=svd(M,full_matrices=False,check_finite=False);return Vt.T/d
    def gauge(q):
        if cap_owner is not None:return q
        s=family.state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);H=s['H']/(1-s['H']@s['g'])[:,None];H=H@np.column_stack([ex,ey,ez])*radius;return family.pack(H)
    def repair(q,radius,W=None,nsteps=14):
        for k in range(nsteps):
            try:s=model(q)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return None
            ix,guard=guards(s)
            if guard.min()>.999*eps:return q
            J=jac(q,s)
            if W is None:W=metric(s,J)
            C=J[ix]@W;rhs=guard-eps;bound=radius/np.sqrt(D);I=eye(D);M=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            sol=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=M,b_ub=np.r_[rhs*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
            if not sol.success:return None
            step=W@sol.x[:D];old=np.maximum(eps-guard,0).sum();accepted=False
            for back in range(16):
                trial=q+2**-back*step
                try:t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if np.maximum(eps-guards(t)[1],0).sum()<old*(1-1e-7):q=trial;accepted=True;break
            if not accepted:return None
        return None
    first=model(q)
    if first['U']!=1:raise ValueError('source is not actual U1')
    allowed_stable=set(map(int,first['A'][first['sg']<0]))
    def guards(s):
        root=int(np.argmax(np.sum(s['Z']**2,axis=1)));ix=np.flatnonzero(np.arange(s['V'])!=root);values=s['ug'][ix]
        if stable_limit is not None:
            exempt=np.argsort(s['sg'])[:stable_limit];si=np.flatnonzero(~np.isin(np.arange(s['F']),exempt));ix=np.r_[ix,s['V']+si];values=np.r_[values,s['sg'][si]]
        elif keep_stable_roots:
            si=np.flatnonzero(~np.isin(s['A'],list(allowed_stable)));ix=np.r_[ix,s['V']+si];values=np.r_[values,s['sg'][si]]
        return ix,values
    aa=args(first)
    def independent(qq):
        R,T,A,up,sp,qp=aa;X,Z,Y,g,v=family.independent_physical(qq,R,T,A);ug=np.sum(Z*(Z[up]-Z),1)/np.sum(Z*Z,1)
        root,a,b=Y[qp[:,0]],Y[qp[:,1]],Y[qp[:,2]];d=b-a;t=-np.sum(a*d,1)/np.sum(d*d,1);t=np.where(t.real<0,0.,np.where(t.real>1,1.,t));birth=np.sum(root*root,1);diff=birth-np.sum((a+t[:,None]*d)**2,1);bars=np.where(diff.real>0,diff,0.)/birth
        sg=np.sum(Y*(Y[sp]-Y),1)/np.sum(Y*Y,1)
        return np.r_[ug,sg,bars,Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(11807).normal(size=D);direction/=np.linalg.norm(direction);J=jac(q,first);value_error=float(np.max(abs(independent(q)-np.asarray(pieces(q,*aa)))));error=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=value_error,complex_step_relative_error=error),indent=2)+'\n')
    if value_error>1e-8 or error>1e-7:raise ValueError('complete physical persistence derivative mismatch')
    if guards(first)[1].min()<.999*eps:
        prepared=repair(q,.08,nsteps=35)
        if prepared is None:raise ValueError('source unique-U margin could not be prepared')
        q=prepared
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','objective','minimum_noncontact']};root=int(np.argmax(np.sum(s['Z']**2,axis=1)));row.update(it=it,trust=trust,seconds=time.time()-start,Uguard=float(np.delete(s['ug'],root).min()));history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%10==0:print('APEX_COMPLETE_Q',m,mode,row,flush=True)
        if s['S']==s['U']==1:
            if s['E']>249:
                np.save(out/'ABOVE_BUDGET_110_q.npy',q);np.save(out/'ABOVE_BUDGET_110_H.npy',s['H']);(out/'ABOVE_BUDGET_110.json').write_text(json.dumps(row,indent=2)+'\n');print('ABOVE_BUDGET_110_IS_NOT_A_GOAL_BODY',row,flush=True);return q
            np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n')
            if cap_owner is None:
                from audit_free_supports import audit
                audit(out/'NUMERICAL_NOMINATION_H.npy',out/'exact_nomination_g16',10**16)
            else:
                np.save(out/'NUMERICAL_NOMINATION_base_H.npy',s['baseH']);np.save(out/('NUMERICAL_NOMINATION_cap_points.npy' if cap_geometry=='multiple' else 'NUMERICAL_NOMINATION_cap_point.npy'),s['cap_points'] if cap_geometry=='multiple' else s['cap_point']);print('NUMERICAL_CAP_GOAL_REQUIRES_CONTACT_PRESERVING_EXACT_CONSTRUCTION',row,flush=True)
            return q
        ix,guard=guards(s)
        if s['U']!=1 or guard.min()<.8*eps:raise ValueError('required actual equilibrium guards were lost')
        J=jac(q,s);W=metric(s,J);Cu=J[ix]@W;Cq=J[V+F:V+2*F-1]@W;bound=trust/np.sqrt(D)
        if mode=='max':
            A=np.r_[np.c_[-Cu,np.zeros(len(Cu))],np.c_[Cq,-np.ones(len(Cq))]];b=np.r_[guard-eps,-s['Q']];cost=np.r_[np.zeros(D),1.];bounds=[(-bound,bound)]*D+[(0.,1.)]
        else:A=-Cu;b=guard-eps;cost=2*s['Q']@Cq/max(s['Qmax'],1e-12);bounds=[(-bound,bound)]*D
        sol=linprog(cost,A_ub=A*1000,b_ub=b*1000,bounds=bounds,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.4;continue
        step=W@sol.x[:D];accepted=False
        for back in range(20):
            trial=repair(q+step*2**-back,max(trust*2**-back,1e-7),W)
            if trial is None:continue
            try:trial=gauge(trial);t=model(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if t['U']!=1 or guards(t)[1].min()<.9*eps:continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.4,trust*1.3)
        if not accepted:trust*=.4
        if trust<1e-12:print('FINITE_COMPLETE_Q_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q);np.save(out/'final_H.npy',family.state(q)['H']);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(mode=mode,iterations=iterations,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4,sys.argv[4] if len(sys.argv)>4 else 'max',int(sys.argv[5]) if len(sys.argv)>5 else 1200,edge_limit=int(sys.argv[6]) if len(sys.argv)>6 else 248,allow_top_retirement=len(sys.argv)>7 and sys.argv[7]=='retire-top',keep_stable_roots=len(sys.argv)>8 and sys.argv[8]=='keep-stable-roots')
