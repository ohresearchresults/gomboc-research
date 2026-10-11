"""Direct two-root feasibility on one integrated physical convex body.

For each primal and polar vertex, find a minimum-cost directed path to the
designated root; chord cost is max(eps-angular_escape,0). The sum of all
shortest-path costs is a continuous piecewise-smooth objective on a fixed
hull cell. Its fixed-tree derivative weights each edge by its descendant
count. Zero cost certifies positive escape to the sole root in each graph;
the actual strict/weak census must still be audited on the frozen body.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from scipy.spatial import ConvexHull,QhullError
from scipy.sparse import csr_matrix,hstack,vstack,eye
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from geometry import angular_scores
from support_persistence import ROOT
from directed_escape_tree import checked_tree

def route(B,root,eps):
    angle=angular_scores(B);cost=np.maximum(eps-angle,0);n=len(B);dist=np.full(n,np.inf);dist[root]=0;parent=np.full(n,-1,int);done=np.zeros(n,bool);order=[]
    for _ in range(n):
        u=int(np.argmin(np.where(done,np.inf,dist)))
        if done[u] or not np.isfinite(dist[u]):raise ValueError('escape route is disconnected')
        done[u]=True;order.append(u)
        for v in np.flatnonzero(~done):
            value=dist[u]+cost[v,u]
            if value<dist[v]:dist[v]=value;parent[v]=u
    parent[root]=root;weight=np.ones(n);weight[root]=0
    for u in reversed(order):
        if u!=root:weight[parent[u]]+=weight[u]
    weight[root]=0;active=np.arange(n)!=root
    value=float(dist.sum());treevalue=float(weight[active]@cost[np.flatnonzero(active),parent[active]])
    if abs(value-treevalue)>1e-9*max(1,value):raise ValueError('shortest-path objective and derivative tree disagree')
    return parent,weight,value

def minimum_route(B,root,eps):
    cost=np.maximum(eps-angular_scores(B),0);parent,value=checked_tree(cost,root);weights=np.ones(len(B));weights[root]=0.;return parent,weights,value

def run(src,out,m=44,iterations=3000,eps=1e-7,allow_top_retirement=False,route_kind='shortest',edge_limit=248):
    if route_kind not in ['shortest','minimum-tree']:raise ValueError('unknown directed escape objective')
    route_function=route if route_kind=='shortest' else minimum_route
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src).copy();D=len(q);fam=ApexFamily(m,allow_top_retirement=allow_top_retirement,edge_limit=edge_limit);start=time.time();history=[];trust=.04
    first=fam.state(q);stable_root=int(first['A'][np.argmax(np.sum(first['Y']**2,1))]);cycle=ConvexHull(np.asarray(fam.unpack(q))[:m,:2]).vertices;pg=np.empty((0,3),int) if allow_top_retirement else np.array([[a,b,c] for a,b in zip(cycle,np.roll(cycle,-1)) for c in cycle if c not in [a,b]],int)
    (out/'source.npy').write_bytes(src.read_bytes());(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex_candidates=m,allow_top_retirement=allow_top_retirement,edge_limit=edge_limit,edge_bound='3N-m-3; each redundant top plane reduces actual bound by two',stable_root=stable_root,eps=eps,route_kind=route_kind,method=__doc__,minimum_tree_definition='sum of nonnegative costs on the minimum directed rooted arborescence, each edge weight one; finite algorithm comparison saved separately'),indent=2)+'\n')
    @jax.jit
    def pieces(q,R,T,A,up,sp):
        X,Z,Y,g,v=fam.physical(q,R,T,A);H=fam.unpack(q)
        def angle(B,p):
            d=B[p]-B;value=jnp.sum(B*d,1)/jnp.sqrt(jnp.maximum(jnp.sum(B*B,1)*jnp.sum(d*d,1),1e-40));return jnp.where(p==jnp.arange(len(B)),0.,value)
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a;geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/jnp.sqrt(jnp.sum(d*d,1))
        return jnp.r_[angle(Z,up),angle(Y,sp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);si=np.flatnonzero(s['A']==stable_root)
        if not len(si):raise ValueError('designated stable root facet retired')
        up,uw,uc=route_function(s['Z'],0,eps);sp,sw,sc=route_function(s['Y'],int(si[0]),eps);s.update(up=up,sp=sp,uw=uw,sw=sw,ucost=uc,scost=sc,objective=uc+sc);return s
    def args(s):return [s[k] for k in ['R','T','A','up','sp']]
    def gauge(q):
        s=fam.state(q);u=np.array([0.,0.,1.])-s['g'];radius=np.linalg.norm(u);ez=u/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);H=s['H']/(1-s['H']@s['g'])[:,None];H=H@np.column_stack([ex,ey,ez])*radius;return fam.pack(H)
    first=model(q);aa=args(first);f0=np.asarray(pieces(q,*aa));G=len(pg)+len(first['H'])-m;K=first['V']+first['F'];geometry_floor=np.minimum(f0[K:K+G]*.01,1e-8)
    if geometry_floor.min()<=0:raise ValueError('initial apex polygon is not strictly convex')
    def independent(qq):
        R,T,A,up,sp=aa;H=np.r_[np.c_[qq[:2*m].reshape(m,2),np.ones(m)],qq[2*m:].reshape(-1,3)];X=np.r_[[[0.,0.,1.]],np.linalg.solve(H[R[1:]],np.ones((len(R)-1,3,1))).squeeze(-1)]
        a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum());Z=X-g;Y=H[A]/(1-H[A]@g)[:,None]
        def angle(B,p):
            active=p!=np.arange(len(B));v=np.zeros(len(B),dtype=qq.dtype);d=B[p[active]]-B[active];v[active]=np.sum(B[active]*d,1)/np.sqrt(np.sum(B[active]*B[active],1)*np.sum(d*d,1));return v
        a,b,c=H[pg[:,0],:2],H[pg[:,1],:2],H[pg[:,2],:2];d=b-a;e=c-a;geo=(d[:,0]*e[:,1]-d[:,1]*e[:,0])/np.sqrt(np.sum(d*d,1))
        return np.r_[angle(Z,up),angle(Y,sp),geo,1-H[m:,2],Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(79243).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*aa));value_error=float(np.max(abs(independent(q)-f0)));error=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=value_error,complex_step_relative_error=error),indent=2)+'\n')
    if value_error>1e-8 or error>1e-7:raise ValueError('independent direct-goal derivative mismatch')
    best_count=100000
    for it in range(iterations):
        s=model(q);V,F=s['V'],s['F'];K=V+F;aa=args(s);f=np.asarray(pieces(q,*aa));weights=np.r_[s['uw'],s['sw']];active=np.flatnonzero(weights>0);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','ucost','scost','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust);history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_H.npy',s['H']);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
        if s['S']+s['U']<best_count:best_count=s['S']+s['U'];np.save(out/'fewest_q.npy',q);np.save(out/'fewest_H.npy',s['H']);(out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n')
        if it%10==0:print('DIRECT_PHYSICAL_GOAL',m,row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');from audit_free_supports import audit;audit(out/'NUMERICAL_NOMINATION_H.npy',out/'exact_nomination_g16',10**16);return q
        J=np.asarray(derivative(q,*aa));emb=J[K+G:];metric=np.vstack([emb[:3*V]/np.sqrt(np.mean(s['Z']**2)),emb[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sing;C=J[K:K+G]@W;B=J[active]@W;bound=trust/np.sqrt(D);N=len(active)
        A=vstack([hstack([-csr_matrix(C),csr_matrix((G,N))]),hstack([-csr_matrix(B),-eye(N)])],format='csr');b=np.r_[f[K:K+G]-geometry_floor,f[active]-eps]
        sol=linprog(np.r_[np.zeros(D),weights[active]],A_ub=A*1000,b_ub=b*1000,bounds=[(-bound,bound)]*D+[(0,None)]*N,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=10.))
        if not sol.success:trust*=.4;continue
        step=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+step*2**-back
            try:t=model(trial);tv=np.asarray(pieces(trial,*args(t)));tk=t['V']+t['F'];tg=tv[tk:tk+G]
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if np.min(tg/geometry_floor)<.9:continue
            if t['objective']<s['objective']*(1-1e-10):
                try:trial=gauge(trial);t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if t['objective']>=s['objective']*(1-1e-10):continue
                q=trial;accepted=True;row['alpha']=2**-back;break
        if accepted and back==0:trust=min(.5,trust*1.4)
        if not accepted:trust*=.4
        if trust<1e-12:print('FINITE_DIRECT_GOAL_STALLED',row,flush=True);break
    np.save(out/'final_q.npy',q);np.save(out/'final_H.npy',fam.state(q)['H']);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(iterations=iterations,goal_complete=False),indent=2)+'\n');return q

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 3000,allow_top_retirement=len(sys.argv)>5 and sys.argv[5]=='retire-top',route_kind=sys.argv[6] if len(sys.argv)>6 else 'shortest',edge_limit=int(sys.argv[7]) if len(sys.argv)>7 else 248)
