"""Whole-body widest-tree flow with a prescribed high-valence physical apex.
All mass and primal/dual coordinates belong to H.x<=1. Raw normalized radial
dot products are the exact-sign escape tests. Prescribed apex polygon
convexity is included explicitly in the LP. Other incidences may change.
Modes U, S, both are declared objectives, never hidden acceptance changes.
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

def widest(B,root=None):
    raw=np.einsum('ij,ikj->ik',B,B[None]-B[:,None])/np.sum(B*B,1)[:,None];np.fill_diagonal(raw,-np.inf)
    if root is None:root=int(np.argmax(np.sum(B*B,1)))
    n=len(B);cap=np.full(n,-np.inf);cap[root]=np.inf;parent=np.full(n,-1,int);done=np.zeros(n,bool)
    for _ in range(n):
        u=int(np.argmax(np.where(done,-np.inf,cap)))
        if done[u] or not np.isfinite(cap[u]) and u!=root:raise ValueError('widest tree is disconnected')
        done[u]=True
        for v in np.flatnonzero(~done):
            value=min(cap[u],raw[v,u])
            if value>cap[v]:cap[v]=value;parent[v]=u
    parent[root]=root;active=np.arange(n)!=root
    for i in np.flatnonzero(active):
        seen=set();v=int(i)
        while v!=root:
            if v in seen:raise ValueError('widest tree is cyclic')
            seen.add(v);v=int(parent[v])
    weights=raw[np.arange(n)[active],parent[active]]
    if abs(weights.min()-cap[active].min())>1e-12:raise ValueError('widest tree capacity mismatch')
    return parent,active,float(weights.min())

def run(src,out,m=44,mode='U',iterations=1400,eps=1e-9):
    if mode not in ['U','S','both']:raise ValueError('unknown scientific objective')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src).copy();D=len(q);fam=ApexFamily(m);start=time.time();history=[];trust=.03
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex=m,mode=mode,eps=eps,method=__doc__),indent=2)+'\n')
    cycle=ConvexHull(np.asarray(fam.unpack(q))[:m,:2]).vertices;pg=np.array([[a,b,c] for a,b in zip(cycle,np.roll(cycle,-1)) for c in cycle if c not in [a,b]],int)
    @jax.jit
    def pieces(q,R,T,A,up,sp):
        X,Z,Y,g,v=fam.physical(q,R,T,A);H=fam.unpack(q)
        def raw(B,p):return jnp.where(p==jnp.arange(len(B)),0.,jnp.sum(B*(B[p]-B),1)/jnp.sum(B*B,1))
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a
        geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/jnp.sqrt(jnp.sum(d*d,1))
        return jnp.r_[raw(Z,up),raw(Y,sp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);up,ua,uc=widest(s['Z'],0);sp,sa,sc=widest(s['Y']);s.update(up=up,sp=sp,ua=ua,sa=sa,ucap=uc,scap=sc)
        if mode=='S':
            Z=s['Z'];raw=np.einsum('ij,ikj->ik',Z,Z[None]-Z[:,None])/np.sum(Z*Z,1)[:,None];np.fill_diagonal(raw,-np.inf);s['up']=raw.argmax(1);s['u_guard']=raw.max(1)
        s['capacity']=uc if mode=='U' else sc if mode=='S' else min(uc,sc)
        return s
    def gauge(q):
        s=fam.state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);H=s['H']/(1-s['H']@s['g'])[:,None];H=H@np.column_stack([ex,ey,ez])*radius;return fam.pack(H)
    first=model(q);args=[first[k] for k in ['R','T','A','up','sp']];f0=np.asarray(pieces(q,*args));G=len(pg)+len(first['H'])-m;startgeo=first['V']+first['F'];geometry_floor=np.minimum(f0[startgeo:startgeo+G]*.01,1e-8)
    if np.min(geometry_floor)<=0:raise ValueError('nonpositive starting apex geometry')
    # Independent complex-step validation of mass, both escape trees and all
    # prescribed geometric inequalities, without JAX in the reference path.
    def independent(qq):
        R,T,A,up,sp=args;H=np.r_[np.c_[qq[:2*m].reshape(m,2),np.ones(m)],qq[2*m:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
        def raw(B,p):return np.where(p==np.arange(len(B)),0.,np.sum(B*(B[p]-B),1)/np.sum(B*B,1))
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a;geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/np.sqrt(np.sum(d*d,1))
        return np.r_[raw(Z,up),raw(Y,sp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(1746).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*args));value_error=float(np.max(abs(independent(q)-f0)));derr=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=value_error,complex_step_relative_error=derr,geometry_min=float(geometry_floor.min())),indent=2)+'\n')
    if value_error>1e-8 or derr>1e-7:raise ValueError('independent whole-body derivative failed')
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];args=[s[k] for k in ['R','T','A','up','sp']];f=np.asarray(pieces(q,*args));geo=f[V+F:V+F+G]
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','ucap','scap','capacity','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust,volume=s['volume'],centroid=s['g'].tolist());history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if it%10==0:print('POLYGON_TREE',mode,m,row,flush=True)
        if s['S']==s['U']==1 or mode=='U' and s['U']==1 and s['ucap']>eps:
            np.save(out/'NUMERICAL_ENDPOINT_q.npy',q);np.save(out/'NUMERICAL_ENDPOINT_H.npy',s['H']);(out/'NUMERICAL_ENDPOINT.json').write_text(json.dumps(row,indent=2)+'\n');from audit_free_supports import audit;ex=audit(out/'NUMERICAL_ENDPOINT_H.npy',out/'exact_endpoint_g16',10**16);print('EXACT_TREE_ENDPOINT',ex['counts'],ex['weak'],flush=True);return q
        if mode=='S' and (s['U']!=1 or s['u_guard'][1:].min()<.8*eps):raise ValueError('declared mode S requires actual unique U with positive guards')
        J=np.asarray(derivative(q,*args));embedding=J[V+F+G:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sing
        objective=np.flatnonzero(s['ua']) if mode=='U' else V+np.flatnonzero(s['sa']) if mode=='S' else np.r_[np.flatnonzero(s['ua']),V+np.flatnonzero(s['sa'])]
        hard=np.arange(V+F,V+F+G);floor=geometry_floor
        if mode=='S':hard=np.r_[np.arange(1,V),hard];floor=np.r_[np.full(V-1,eps),floor]
        C=J[hard]@W;O=J[objective]@W;A=np.r_[np.c_[-C,np.zeros(len(C))],np.c_[-O,np.ones(len(O))]];b=np.r_[f[hard]-floor,f[objective]];bound=trust/np.sqrt(D)
        sol=linprog(np.r_[np.zeros(D),-1.],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(-2.,2.)],method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.4;continue
        step=W@sol.x[:D];accepted=False
        for back in range(22):
            trial=q+step*2**-back
            try:t=model(trial);tv=np.asarray(pieces(trial,t['R'],t['T'],t['A'],t['up'],t['sp']));tg=tv[t['V']+t['F']:t['V']+t['F']+G]
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if np.min(tg/geometry_floor)<.9:continue
            if mode=='S' and (t['U']!=1 or t['u_guard'][1:].min()<.9*eps):continue
            if t['capacity']>s['capacity']+1e-13:
                try:trial=gauge(trial);t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if t['capacity']<=s['capacity']+1e-13:continue
                q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.5,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-12:print('FINITE_POLYGON_TREE_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q);np.save(out/'final_H.npy',fam.state(q)['H']);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(iterations=iterations,mode=mode,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,sys.argv[4] if len(sys.argv)>4 else 'U',int(sys.argv[5]) if len(sys.argv)>5 else 1400)
