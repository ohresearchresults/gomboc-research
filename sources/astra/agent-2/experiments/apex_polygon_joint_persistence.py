"""All primal and polar persistence bars of one physical homogeneous body.
Preserve only the declared apex polygon and convexity, with the hard true
complexity bound built into ApexFamily. All roots may change. Every finite
bar enters the objective; an optimizer score is never a census certificate.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def run(src,out,m=44,mode='max',iterations=1200,allow_top_retirement=False):
    if mode not in ['max','square']:raise ValueError('unknown objective')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src).copy();D=len(q);fam=ApexFamily(m,allow_top_retirement=allow_top_retirement);start=time.time();history=[];trust=.03
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex_candidates=m,allow_top_retirement=allow_top_retirement,mode=mode,method=__doc__),indent=2)+'\n')
    cycle=ConvexHull(np.asarray(fam.unpack(q))[:m,:2]).vertices;pg=np.empty((0,3),int) if allow_top_retirement else np.array([[a,b,c] for a,b in zip(cycle,np.roll(cycle,-1)) for c in cycle if c not in [a,b]],int)
    @jax.jit
    def pieces(q,R,T,A,pp,qp):
        X,Z,Y,g,v=fam.physical(q,R,T,A);H=fam.unpack(q)
        def bars(B,p):
            root,a,b=B[p[:,0]],B[p[:,1]],B[p[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,1)/jnp.sum(d*d,1),0,1);birth=jnp.sum(root*root,1);return jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,1),0)/birth
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a;geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/jnp.sqrt(jnp.sum(d*d,1))
        return jnp.r_[bars(Z,pp),bars(Y,qp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);pq=np.r_[s['P'],s['Q']];s['objective']=float(pq.max()) if mode=='max' else float(pq@pq);return s
    def args(s):return [s[k] for k in ['R','T','A','pp','qp']]
    def gauge(q):
        s=fam.state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);H=s['H']/(1-s['H']@s['g'])[:,None];H=H@np.column_stack([ex,ey,ez])*radius;return fam.pack(H)
    first=model(q);aa=args(first);f0=np.asarray(pieces(q,*aa));G=len(pg)+len(first['H'])-m;K=first['V']+first['F']-2;geometry_floor=np.minimum(f0[K:K+G]*.01,1e-8)
    if geometry_floor.min()<=0:raise ValueError('apex polygon is not strictly convex')
    def independent(qq):
        R,T,A,pp,qp=aa;H=np.r_[np.c_[qq[:2*m].reshape(m,2),np.ones(m)],qq[2*m:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
        def bars(B,p):
            root,a,b=B[p[:,0]],B[p[:,1]],B[p[:,2]];d=b-a;t=-np.sum(a*d,1)/np.sum(d*d,1);t=np.where(t.real<0,0.,np.where(t.real>1,1.,t));birth=np.sum(root*root,1);diff=birth-np.sum((a+t[:,None]*d)**2,1);return np.where(diff.real>0,diff,0.)/birth
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a;geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/np.sqrt(np.sum(d*d,1))
        return np.r_[bars(Z,pp),bars(Y,qp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(67291).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*aa));value_error=float(np.max(abs(independent(q)-f0)));error=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=value_error,complex_step_relative_error=error),indent=2)+'\n')
    if value_error>1e-8 or error>1e-7:raise ValueError('independent full persistence derivative mismatch')
    best_count=100000
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];K=V+F-2;aa=args(s);f=np.asarray(pieces(q,*aa));row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust);history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if s['S']+s['U']<best_count:best_count=s['S']+s['U'];np.save(out/'fewest_q.npy',q);np.save(out/'fewest_H.npy',s['H']);(out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n')
        if it%10==0:print('JOINT_PHYSICAL_PERSISTENCE',m,mode,row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');from audit_free_supports import audit;audit(out/'NUMERICAL_NOMINATION_H.npy',out/'exact_nomination_g16',10**16);return q
        J=np.asarray(derivative(q,*aa));emb=J[K+G:];metric=np.vstack([emb[:3*V]/np.sqrt(np.mean(s['Z']**2)),emb[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sing;C=J[K:K+G]@W;B=J[:K]@W;bound=trust/np.sqrt(D)
        if mode=='max':A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[B,-np.ones(K)]];b=np.r_[f[K:K+G]-geometry_floor,-f[:K]];cost=np.r_[np.zeros(D),1.];bounds=[(-bound,bound)]*D+[(0.,1.)]
        else:A=-C;b=f[K:K+G]-geometry_floor;cost=2*f[:K]@B/max(f[:K].max(),1e-12);bounds=[(-bound,bound)]*D
        sol=linprog(cost,A_ub=A*1000,b_ub=b*1000,bounds=bounds,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.4;continue
        step=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+step*2**-back
            try:t=model(trial);tv=np.asarray(pieces(trial,*args(t)));tk=t['V']+t['F']-2;tg=tv[tk:tk+G]
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if np.min(tg/geometry_floor)<.9:continue
            if t['objective']<s['objective']*(1-1e-10):
                try:trial=gauge(trial);t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if t['objective']>=s['objective']*(1-1e-10):continue
                q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.5,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-12:print('FINITE_JOINT_PERSISTENCE_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q);np.save(out/'final_H.npy',fam.state(q)['H']);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(mode=mode,iterations=iterations,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,sys.argv[4] if len(sys.argv)>4 else 'max',int(sys.argv[5]) if len(sys.argv)>5 else 1200,allow_top_retirement=len(sys.argv)>6 and sys.argv[6]=='retire-top')
