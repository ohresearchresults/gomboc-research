"""Joint physical feasibility using strictly radius-ordered escape witnesses.

At each true own-centroid body, order each of its primal and polar point sets
by squared radius. Every nonroot chooses its best angular escape to a later
point. These choices always form a rooted tree. Positive escape necessarily
increases radius, so a positive minimum is equivalent to unique strict maxima
in both fields. We optimize the actual recomputed objective, not a fixed graph
or prescribed center. Nearby genuine noncontact gaps guide local LP steps.
Only a complete exact frozen-body audit can establish the requested Figure.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.spatial import QhullError
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from geometry import angular_scores

def ordered_witness(B):
    order=np.argsort(np.sum(B*B,axis=1),kind='stable');rank=np.empty(len(B),int);rank[order]=np.arange(len(B))
    score=angular_scores(B);score[rank[None,:]<=rank[:,None]]=-np.inf
    parent=score.argmax(1);parent[order[-1]]=order[-1]
    values=score[np.arange(len(B)),parent];values[order[-1]]=np.inf
    for i in order[:-1]:
        if rank[parent[i]]<=rank[i]:raise ValueError('nonincreasing radial witness')
    return parent,values,int(order[-1])

def run(src,out,m=44,n=0,iterations=1200,eps=1e-6,mode='max',gap_count=96):
    if mode not in ['max','sum']:raise ValueError('explicit objective required')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');D=len(q)
    if n:
        from flexible_two_apex_supports import FlexibleTwoApexFamily
        fam=FlexibleTwoApexFamily(m,n)
    else:fam=ApexFamily(m,allow_top_retirement=True,edge_limit=249)
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,eps=eps,mode=mode,gap_count=gap_count,method=__doc__),indent=2)+'\n')
    def model(q):
        s=fam.state(q);parents=[];values=[];roots=[]
        for B in [s['Z'],s['Y']]:
            p,v,r=ordered_witness(B);parents.append(p);values.append(v);roots.append(r)
        deficit=np.maximum(eps-np.r_[*values],0)
        s.update(parents=parents,roots=roots,objective=float(deficit.max() if mode=='max' else deficit.sum()),deficit=deficit)
        gap=1-s['Y']@s['Z'].T;contact=np.zeros_like(gap,dtype=bool)
        for k,face in enumerate(s['faces']):contact[k,face]=True
        pairs=np.argwhere(~contact);pairs=pairs[np.argsort(gap[~contact])[:gap_count]];s['gap_pairs']=pairs
        return s
    @jax.jit
    def pieces(q,R,T,A,up,sp,pairs):
        X,Z,Y,g,v=fam.physical(q,R,T,A)
        def escape(B,p):
            d=B[p]-B;norm=jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(d*d,1),1e-40))
            return jnp.where(p==jnp.arange(len(B)),0.,jnp.sum(B*d,1)/norm)
        gap=1-jnp.sum(Y[pairs[:,0]]*Z[pairs[:,1]],1)
        return jnp.r_[escape(Z,up),escape(Y,sp),gap,Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def args(s):return [s['R'],s['T'],s['A'],*s['parents'],s['gap_pairs']]
    first=model(q);aa=args(first)
    def independent(qq):
        R,T,A,up,sp,pairs=aa;X,Z,Y,g,v=fam.independent_physical(qq,R,T,A)
        def escape(B,p):
            active=p!=np.arange(len(B));value=np.zeros(len(B),dtype=qq.dtype);d=B[p[active]]-B[active]
            value[active]=np.sum(B[active]*d,1)/np.sqrt(np.sum(B[active]*B[active],1)*np.sum(d*d,1));return value
        return np.r_[escape(Z,up),escape(Y,sp),1-np.sum(Y[pairs[:,0]]*Z[pairs[:,1]],1),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(1837209).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*aa));f=np.asarray(pieces(q,*aa));ve=float(np.max(abs(independent(q)-f)));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('radius-ordered derivative gate failed')
    history=[];trust=.04;start=time.time();topology=None;fewest=np.inf;best=np.inf
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];K=V+F;G=len(s['gap_pairs']);active=np.setdiff1d(np.arange(K),[s['roots'][0],V+s['roots'][1]]);N=len(active);aa=args(s);f=np.asarray(pieces(q,*aa));J=np.asarray(derivative(q,*aa))
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        if topology!=(V,s['E'],F) or s['S']+s['U']<fewest:
            name=f'state_{it:04d}_V{V}_E{s["E"]}_F{F}';np.save(out/(name+'_q.npy'),q);(out/(name+'.json')).write_text(json.dumps(row,indent=2)+'\n');row['checkpoint']=name;topology=(V,s['E'],F);fewest=min(fewest,s['S']+s['U'])
        if s['objective']<best:best=s['objective'];np.save(out/'best_q.npy',q);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
        history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('RADIUS_ORDERED_PHYSICAL_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        if s['objective']==0:raise ValueError('radius-ordered escape and actual census disagree')
        embedding=J[K+G:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D)
        C=J[active]@W;geo=J[K:K+G]@W;floor=np.minimum(f[K:K+G]*.05,1e-7);count=N if mode=='sum' else 1;slacks=eye(N) if mode=='sum' else csr_matrix(np.ones((N,1)))
        A=vstack([hstack([-csr_matrix(C),-slacks]),hstack([-csr_matrix(geo),csr_matrix((G,count))])],format='csr');b=np.r_[f[active]-eps,f[K:K+G]-floor]
        sol=linprog(np.r_[np.zeros(D),np.ones(count)],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*count,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:
            row['lp_failure']=sol.message;trust*=.4
            if trust<1e-12:break
            continue
        violation=float(np.maximum(A@sol.x-b,0).max());row['linear_violation']=violation
        if violation>1e-7:raise ValueError('local radial-order LP failed original-row check')
        step=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+2**-back*step
            try:t=model(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;row['alpha']=2**-back;accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-12:break
    np.save(out/'final_q.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(iterations=iterations,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 1200,mode=sys.argv[6] if len(sys.argv)>6 else 'max')
