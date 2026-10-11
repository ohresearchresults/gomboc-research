"""Physical two-root arborescence feasibility with free cap points.
All actual primal and polar vertices get escape paths to their current global
radial maximum. Positive paths prohibit hidden root cycles. Intermediate
equilibria may appear; only the complete own-centroid census nominates a body.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,eye
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from physical_multiple_cap_family import MultipleCapFamily
from apex_polygon_direct_goal import minimum_route

def run(src,out,m=44,point_count=2,iterations=2000,eps=1e-6,search_edge_limit=249,geometry='caps',second_apex=12):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    raw=src.read_bytes();(out/'source_z.npy').write_bytes(raw);q=np.load(out/'source_z.npy');D=len(q)
    if geometry=='caps':fam=MultipleCapFamily(m,point_count,search_edge_limit)
    elif geometry=='two-apex':
        from two_apex_supports import TwoApexFamily
        fam=TwoApexFamily(m,second_apex,search_edge_limit)
    elif geometry=='flexible-two-apex':
        from flexible_two_apex_supports import FlexibleTwoApexFamily
        fam=FlexibleTwoApexFamily(m,second_apex,search_edge_limit)
    else:raise ValueError('unknown physical construction')
    start=time.time();history=[];trust=.03
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,point_count=point_count,geometry=geometry,second_apex=second_apex,eps=eps,search_edge_limit=search_edge_limit,method=__doc__),indent=2)+'\n')
    @jax.jit
    def pieces(q,R,T,A,up,sp):
        X,Z,Y,g,v=fam.physical(q,R,T,A)
        def angle(B,p):
            d=B[p]-B;val=jnp.sum(B*d,1)/jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(d*d,1),1e-40))
            return jnp.where(p==jnp.arange(len(B)),0.,val)
        return jnp.r_[angle(Z,up),angle(Y,sp),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q)
        ur=int(np.argmax(np.sum(s['Z']**2,1)));sr=int(np.argmax(np.sum(s['Y']**2,1)))
        up,uw,uc=minimum_route(s['Z'],ur,eps);sp,sw,sc=minimum_route(s['Y'],sr,eps)
        s.update(up=up,sp=sp,uw=uw,sw=sw,ucost=uc,scost=sc,objective=uc+sc)
        return s
    def args(s):return [s[k] for k in ['R','T','A','up','sp']]
    first=model(q);aa=args(first)
    def independent(qq):
        R,T,A,up,sp=aa;X,Z,Y,g,v=fam.independent_physical(qq,R,T,A)
        def angle(B,p):
            active=p!=np.arange(len(B));values=np.zeros(len(B),dtype=qq.dtype);d=B[p[active]]-B[active]
            values[active]=np.sum(B[active]*d,1)/np.sqrt(np.sum(B[active]*B[active],1)*np.sum(d*d,1));return values
        return np.r_[angle(Z,up),angle(Y,sp),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(821009).normal(size=D);direction/=np.linalg.norm(direction)
    J=np.asarray(derivative(q,*aa));ve=float(np.max(abs(independent(q)-np.asarray(pieces(q,*aa)))))
    de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('independent actual multipoint derivative check failed')
    best_count=100000
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];K=V+F;aa=args(s);f=np.asarray(pieces(q,*aa));weights=np.r_[s['uw'],s['sw']];active=np.flatnonzero(weights>0)
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','ucost','scost','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        history.append(row);np.save(out/'latest_z.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%10==0:print('MULTIPLE_CAP_DIRECT_GOAL',row,flush=True)
        if s['S']+s['U']<best_count:
            best_count=s['S']+s['U'];np.save(out/'fewest_z.npy',q);(out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n')
        if s['S']==s['U']==1:
            label='NUMERICAL_NOMINATION' if s['E']<=249 else 'ABOVE_BUDGET_110'
            np.save(out/(label+'_z.npy'),q)
            if geometry=='caps':np.save(out/(label+'_base_H.npy'),s['baseH']);np.save(out/(label+'_cap_points.npy'),s['cap_points'])
            else:np.save(out/(label+'_H.npy'),s['H'])
            (out/(label+'.json')).write_text(json.dumps(row,indent=2)+'\n');print(label,row,flush=True);return q
        J=np.asarray(derivative(q,*aa));embedding=J[K:]
        metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03])
        _,sing,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sing;B=J[active]@W;bound=trust/np.sqrt(D);N=len(active)
        A=hstack([-csr_matrix(B),-eye(N)],format='csr');b=f[active]-eps
        sol=linprog(np.r_[np.zeros(D),weights[active]],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*N,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.4;continue
        step=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+step*2**-back
            try:t=model(trial)
            except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.5,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-12:print('FINITE_MULTIPLE_CAP_DIRECT_STALLED',row,flush=True);break
    np.save(out/'final_z.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(iterations=iterations,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 2,int(sys.argv[5]) if len(sys.argv)>5 else 2000)
