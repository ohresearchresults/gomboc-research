"""Joint physical deformation and adjacent stable-escape choice.

A mixed-integer local model chooses a genuine adjacent escape for each
non-root polar vertex while preserving one actual unstable equilibrium.
The full physical hull, centroid, complete persistence and census are
recomputed after every trial. Integer feasibility is never body feasibility.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import milp,Bounds,LinearConstraint,linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from physical_multiple_cap_family import MultipleCapFamily
from apex_polygon_supports import ApexFamily
from directed_escape_tree import checked_tree

def bottleneck_tree(escape,root):
    n=len(escape);capacity=np.full(n,-np.inf);capacity[root]=np.inf;parent=np.full(n,-1,int);parent[root]=root;done=np.zeros(n,bool)
    for _ in range(n):
        u=int(np.argmax(np.where(done,-np.inf,capacity)))
        if done[u] or capacity[u]==-np.inf:raise ValueError('target escape graph is disconnected')
        done[u]=True
        for v in np.flatnonzero(~done):
            value=min(capacity[u],escape[v,u])
            if value>capacity[v]:capacity[v]=value;parent[v]=u
    mask=np.arange(n)!=root;actual=escape[np.arange(n)[mask],parent[mask]].min();computed=capacity[mask].min()
    if abs(actual-computed)>1e-12:raise ValueError('independent bottleneck tree edge minimum mismatch')
    return parent,float(computed)

def run(src,out,m=44,points=2,iterations=250,escape_eps=1e-7,loss_weight=20.,second_apex=0,rooted_tree=False,escape_kind='dot',target='stable',seeded_solver=False,tree_loss='sum',bar_weight=1.):
    if escape_kind not in ['dot','angular']:raise ValueError('unknown explicit escape normalization')
    if target not in ['stable','unstable']:raise ValueError('unknown target equilibrium type')
    if tree_loss not in ['sum','max'] or (tree_loss=='max' and not rooted_tree):raise ValueError('bottleneck objective requires rooted connectivity')
    if bar_weight<0 or (bar_weight==0 and not rooted_tree):raise ValueError('pure escape feasibility requires globally rooted paths')
    guard_key='U' if target=='stable' else 'S'
    if seeded_solver and not rooted_tree:raise ValueError('explicit feasible-tree seeding requires rooted connectivity')
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    raw=src.read_bytes();(out/'source_z.npy').write_bytes(raw);q=np.load(out/'source_z.npy');D=len(q)
    if second_apex:
        if points:raise ValueError('explicit two-star family is separate from additional cap points')
        from flexible_two_apex_supports import FlexibleTwoApexFamily
        fam=FlexibleTwoApexFamily(m,second_apex,249)
    else:fam=ApexFamily(m,allow_top_retirement=True,edge_limit=249) if points==0 else MultipleCapFamily(m,points,249)
    start=time.time();history=[];trust=.05
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,points=points,second_apex=second_apex,escape_eps=escape_eps,escape_kind=escape_kind,loss_weight=loss_weight,rooted_tree=rooted_tree,target=target,seeded_solver=seeded_solver,tree_loss=tree_loss,bar_weight=bar_weight,physical_interpretation='One unchanged physical support construction, integrated at its own volume centroid. Target unstable uses primal X-g paths and preserves one stable equilibrium using the polar normalized normals; target stable exchanges these two feature roles. The mass distribution is never dualized.',connectivity='one unit per nonroot target feature, routed along selected directed edges to the unique target root' if rooted_tree else 'local escape disjunction only',method=__doc__),indent=2)+'\n')
    @jax.jit
    def pieces(q,R,T,A,up,edges,qp):
        X,Z,Y,g,v=fam.physical(q,R,T,A)
        if target=='unstable':Z,Y=Y,Z
        ug=jnp.sum(Z*(Z[up]-Z),1)/jnp.sum(Z*Z,1)
        B=Y[edges[:,0]];d=Y[edges[:,1]]-B
        escape=jnp.sum(B*d,1)/(jnp.sqrt(jnp.sum(B*B,1)*jnp.sum(d*d,1)) if escape_kind=='angular' else jnp.sum(B*B,1))
        root,a,b=Y[qp[:,0]],Y[qp[:,1]],Y[qp[:,2]];d=b-a;t=jnp.clip(-jnp.sum(a*d,1)/jnp.sum(d*d,1),0,1);birth=jnp.sum(root*root,1)
        bars=jnp.maximum(birth-jnp.sum((a+t[:,None]*d)**2,1),0)/birth
        return jnp.r_[ug,escape,bars,Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);Z=s['Z'] if target=='stable' else s['Y'];Y=s['Y'] if target=='stable' else s['Z'];ur=int(np.argmax(np.sum(Z*Z,1)));sr=int(np.argmax(np.sum(Y*Y,1)))
        raw=Z@Z.T/np.sum(Z*Z,1)[:,None]-1;np.fill_diagonal(raw,-np.inf);up=raw.argmax(1)
        graph=s['es'] if target=='stable' else s['eu'];edges=np.r_[graph,graph[:,::-1]];edges=edges[edges[:,0]!=sr]
        B=Y[edges[:,0]];d=Y[edges[:,1]]-B;e=np.sum(B*d,1)/(np.sqrt(np.sum(B*B,1)*np.sum(d*d,1)) if escape_kind=='angular' else np.sum(B*B,1))
        owners=np.array([i for i in range(len(Y)) if i!=sr]);best=np.array([e[edges[:,0]==i].max() for i in owners]);deficit=float(np.maximum(escape_eps-best,0).sum())
        if rooted_tree:
            if tree_loss=='sum':
                costs=np.full((len(Y),len(Y)),np.inf);costs[edges[:,0],edges[:,1]]=np.maximum(escape_eps-e,0);parent,deficit=checked_tree(costs,sr)
            else:
                capacity=np.full((len(Y),len(Y)),-np.inf);capacity[edges[:,0],edges[:,1]]=e;parent,bottleneck=bottleneck_tree(capacity,sr);deficit=max(escape_eps-bottleneck,0);s['bottleneck']=bottleneck
            s['route_parent']=parent
        bars=s['Q'] if target=='stable' else s['P'];pairs=s['qp'] if target=='stable' else s['pp']
        s.update(up=up,ug=raw.max(1),ur=ur,sr=sr,edges=edges,owners=owners,deficit=deficit,objective=bar_weight*float(bars.max())+loss_weight*deficit,guard_size=len(Z),target_size=len(Y),guard_coordinates=Z,target_coordinates=Y,target_pairs=pairs,target_bars=bars)
        return s
    def args(s):return [s[k] for k in ['R','T','A','up','edges','target_pairs']]
    def repair(qq,W,radius,ueps=1e-11):
        for correction in range(14):
            try:s=model(qq)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):return None
            ix=np.flatnonzero(np.arange(s['guard_size'])!=s['ur']);guard=s['ug'][ix]
            if guard.min()>.999*ueps:return qq
            J=np.asarray(derivative(qq,*args(s)));C=J[ix]@W;bound=radius/np.sqrt(D);I=eye(D)
            matrix=vstack([hstack([-csr_matrix(C*1000),csr_matrix((len(C),D))]),hstack([I,-I]),hstack([-I,-I])],format='csr')
            sol=linprog(np.r_[np.zeros(D),np.ones(D)],A_ub=matrix,b_ub=np.r_[(guard-ueps)*1000,np.zeros(2*D)],bounds=[(-bound,bound)]*D+[(0,None)]*D,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=5.))
            if not sol.success:return None
            step=W@sol.x[:D];old=float(np.maximum(ueps-guard,0).sum());accepted=False
            for back in range(14):
                trial=qq+step*2**-back
                try:t=model(trial)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
                if np.maximum(ueps-np.delete(t['ug'],t['ur']),0).sum()<old*(1-1e-7):qq=trial;accepted=True;break
            if not accepted:return None
        return None
    first=model(q)
    if first[guard_key]!=1:raise ValueError('disjunctive search requires one actual guarded equilibrium')
    aa=args(first)
    def independent(qq):
        R,T,A,up,edges,qp=aa;X,Z,Y,g,v=fam.independent_physical(qq,R,T,A)
        if target=='unstable':Z,Y=Y,Z
        ug=np.sum(Z*(Z[up]-Z),1)/np.sum(Z*Z,1);B=Y[edges[:,0]];d=Y[edges[:,1]]-B;escape=np.sum(B*d,1)/(np.sqrt(np.sum(B*B,1)*np.sum(d*d,1)) if escape_kind=='angular' else np.sum(B*B,1))
        root,a,b=Y[qp[:,0]],Y[qp[:,1]],Y[qp[:,2]];d=b-a;t=-np.sum(a*d,1)/np.sum(d*d,1);t=np.where(t.real<0,0.,np.where(t.real>1,1.,t));birth=np.sum(root*root,1);v= birth-np.sum((a+t[:,None]*d)**2,1);bars=np.where(v.real>0,v,0.)/birth
        return np.r_[ug,escape,bars,Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(57942).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*aa));ve=float(np.max(abs(independent(q)-np.asarray(pieces(q,*aa)))));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('disjunctive physical derivative gate failed')
    checkpoint_topology=None;checkpoint_roots=np.inf
    for it in range(iterations):
        s=model(q);V,F=s['guard_size'],s['target_size'];edges=s['edges'];L=len(edges);N=F-1;aa=args(s);values=np.asarray(pieces(q,*aa));J=np.asarray(derivative(q,*aa))
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','deficit','objective','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,trust=trust)
        topology=(s['V'],s['E'],s['F']);root_count=s['S']+s['U']
        if topology!=checkpoint_topology or root_count<checkpoint_roots:
            name=f'state_{it:04d}_V{s["V"]}_E{s["E"]}_F{s["F"]}';np.save(out/(name+'_q.npy'),q);(out/(name+'.json')).write_text(json.dumps(row,indent=2)+'\n');row['checkpoint']=name;checkpoint_topology=topology;checkpoint_roots=min(checkpoint_roots,root_count)
        history.append(row);np.save(out/'latest_z.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('DISJUNCTIVE_PHYSICAL_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_z.npy',q)
            if points:
                np.save(out/'NUMERICAL_NOMINATION_base_H.npy',s['baseH']);np.save(out/'NUMERICAL_NOMINATION_cap_points.npy',s['cap_points'])
            else:np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H'])
            (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        if s[guard_key]!=1:raise ValueError('actual guarded equilibrium census was lost')
        embedding=J[V+L+N:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['guard_coordinates']**2)),embedding[3*V:]/np.sqrt(np.mean(s['target_coordinates']**2)),np.eye(D)*.03]);_,sing,Vt=svd(metric,full_matrices=False,check_finite=False);W=Vt.T/sing;bound=trust/np.sqrt(D)
        # Variables: physical step, one nonnegative deficit per nonroot facet,
        # one max-Q epigraph, then one binary per adjacent directed escape.
        nv=D+N+1+L+(L if rooted_tree else 0);uindex=np.flatnonzero(np.arange(V)!=s['ur']);A=[];lo=[];hi=[]
        M=np.zeros((len(uindex),nv));M[:,:D]=J[uindex]@W;A.append(M);lo.extend(1e-11-s['ug'][uindex]);hi.extend([np.inf]*len(uindex))
        C=J[V:V+L]@W;g=values[V:V+L];big=np.maximum(escape_eps-g+bound*np.sum(abs(C),axis=1)+1e-9,1e-9);owner={int(x):i for i,x in enumerate(s['owners'])}
        M=np.zeros((L,nv));M[:,:D]=C
        for k,(a,b) in enumerate(edges):M[k,D+owner[int(a)]]=1;M[k,D+N+1+k]=-big[k]
        A.append(M);lo.extend(escape_eps-g-big);hi.extend([np.inf]*L)
        M=np.zeros((N,nv))
        for k,(a,b) in enumerate(edges):M[owner[int(a)],D+N+1+k]=1
        A.append(M);lo.extend([1.]*N);hi.extend([1.]*N)
        M=np.zeros((N,nv));M[:,:D]=J[V+L:V+L+N]@W;M[:,D+N]=-1;A.append(M);lo.extend([-np.inf]*N);hi.extend(-s['target_bars'])
        if rooted_tree:
            # A one-outgoing-edge graph carrying all unit supplies to the
            # root cannot contain a directed nonroot cycle.
            flow_start=D+N+1+L;M=np.zeros((L,nv))
            for k in range(L):M[k,flow_start+k]=1;M[k,D+N+1+k]=-N
            A.append(M);lo.extend([-np.inf]*L);hi.extend([0.]*L)
            M=np.zeros((F,nv))
            for k,(a,b) in enumerate(edges):M[a,flow_start+k]+=1;M[b,flow_start+k]-=1
            balance=np.ones(F);balance[s['sr']]=-N;A.append(M);lo.extend(balance);hi.extend(balance)
        if tree_loss=='max':
            M=np.zeros((N-1,nv))
            for i in range(1,N):M[i-1,D+i]=1;M[i-1,D]=-1
            A.append(M);lo.extend([0.]*(N-1));hi.extend([0.]*(N-1))
        A=np.vstack(A);lo=np.asarray(lo);hi=np.asarray(hi);scale=np.r_[np.full(len(uindex)+L,1000.),np.ones(N),np.full(N,1000.),np.ones(L+F if rooted_tree else 0),np.ones(N-1 if tree_loss=='max' else 0)]
        c=np.r_[np.zeros(D),np.full(N,loss_weight/N if tree_loss=='max' else loss_weight),bar_weight,np.zeros(L+(L if rooted_tree else 0))];lower=np.r_[np.full(D,-bound),np.zeros(N+1+L+(L if rooted_tree else 0))];upper=np.r_[np.full(D,bound),np.full(N+1,np.inf),np.ones(L),np.full(L if rooted_tree else 0,N)];integer=np.r_[np.zeros(D+N+1),np.ones(L),np.zeros(L if rooted_tree else 0)]
        if seeded_solver:
            from seeded_escape_milp import solve
            seed=np.zeros(nv);chosen={};parents=s['route_parent'];edge_index={tuple(map(int,e)):k for k,e in enumerate(edges)}
            for node in s['owners']:
                k=edge_index[(int(node),int(parents[node]))];chosen[int(node)]=k;seed[D+N+1+k]=1;seed[D+owner[int(node)]]=max(escape_eps-g[k],0)+1e-8
            if tree_loss=='max':seed[D:D+N]=seed[D:D+N].max()
            for node in s['owners']:
                now=int(node)
                while now!=s['sr']:
                    k=chosen[now];seed[D+N+1+L+k]+=1;now=int(parents[now])
            seed[D+N]=float(s['target_bars'].max())+1e-8
            sol=solve(c,A,lo,hi,lower,upper,integer,scale,seed,D+N+1,L)
            row.update(seed_objective=sol.seed_objective,seed_violation=sol.seed_violation,mip_gap=sol.mip_gap,solver_version=sol.solver_version,enclosed_coefficients=sol.enclosed_coefficients,maximum_coefficient_enclosure=sol.maximum_coefficient_enclosure)
        else:
            sol=milp(c,integrality=integer,bounds=Bounds(lower,upper),constraints=LinearConstraint(csr_matrix(A*scale[:,None]),lo*scale,hi*scale),options=dict(time_limit=8.,mip_rel_gap=.01,mip_feasibility_tolerance=1e-9))
        row['solver_status']=int(sol.status);row['solver_message']=sol.message
        if sol.x is None:
            trust*=.5
            if trust<1e-10:break
            continue
        violation=max(float(np.maximum(lo-A@sol.x,0).max()),float(np.maximum(A@sol.x-hi,0).max()),float(np.maximum(lower-sol.x,0).max()),float(np.maximum(sol.x-upper,0).max()))
        integer_values=sol.x[D+N+1:D+N+1+L];integer_error=float(abs(integer_values-np.round(integer_values)).max());row.update(linear_violation=violation,integer_error=integer_error)
        if violation>1e-7 or integer_error>1e-6:
            np.savez(out/'FAILED_LOCAL_MODEL.npz',A=A,lo=lo,hi=hi,lower=lower,upper=upper,solution=sol.x)
            (out/'FAILED_LOCAL_MODEL.json').write_text(json.dumps(row,indent=2)+'\n')
            raise ValueError(f'mixed integer candidate violates its explicit local model: violation={violation}, integer_error={integer_error}')
        step=W@sol.x[:D];accepted=False
        for back in range(20):
            trial=repair(q+2**-back*step,W,max(trust*2**-back,1e-7))
            if trial is None:continue
            try:t=model(trial)
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError):continue
            if t[guard_key]!=1 or np.delete(t['ug'],t['ur']).min()<1e-12:continue
            if t['objective']<s['objective']*(1-1e-10):q=trial;row['alpha']=2**-back;accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-11:break
    np.save(out/'final_z.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(goal_complete=False,iterations=iterations),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 2,int(sys.argv[5]) if len(sys.argv)>5 else 250)
