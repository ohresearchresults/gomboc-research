"""Joint strict-escape feasibility on both graphs of ONE homogeneous body.

Both its own-centroid primal vertex graph and its normalized polar facet graph
receive a rooted directed tree. A shared worst-edge deficit is minimized while
physical support coordinates and both trees change jointly. Unit-supply flows
exclude cycles. Extra equilibria of either type may occur during search.
Actual mass, complete persistence and strict numerical counts are reconstructed
for every accepted physical body. Only exact whole-body verification can qualify.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.spatial import QhullError
import jax
import jax.numpy as jnp
from apex_polygon_supports import ApexFamily
from cap_disjunctive_goal import bottleneck_tree
from seeded_escape_milp import solve

def run(src,out,m=44,n=0,iterations=300,eps=1e-6):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);q=np.load(out/'source_q.npy');D=len(q)
    if n:
        from flexible_two_apex_supports import FlexibleTwoApexFamily
        fam=FlexibleTwoApexFamily(m,n)
    else:fam=ApexFamily(m,allow_top_retirement=True,edge_limit=249)
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,eps=eps,method=__doc__,physical_embedding='Primal X-g and polar H/(1-H.g) both derive from the same raw physical halfspace intersection and its uniform volume centroid.'),indent=2)+'\n')
    @jax.jit
    def pieces(q,R,T,A,ue,se):
        X,Z,Y,g,v=fam.physical(q,R,T,A)
        def escape(B,edges):
            a=B[edges[:,0]];d=B[edges[:,1]]-a
            return jnp.sum(a*d,1)/jnp.sqrt(jnp.sum(a*a,1)*jnp.sum(d*d,1))
        return jnp.r_[escape(Z,ue),escape(Y,se),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0))
    def model(q):
        s=fam.state(q);graphs=[];capacities=[]
        for B,undirected in [(s['Z'],s['eu']),(s['Y'],s['es'])]:
            root=int(np.argmax(np.sum(B*B,1)));edges=np.r_[undirected,undirected[:,::-1]];edges=edges[edges[:,0]!=root];a=B[edges[:,0]];d=B[edges[:,1]]-a;e=np.sum(a*d,1)/np.sqrt(np.sum(a*a,1)*np.sum(d*d,1));C=np.full((len(B),len(B)),-np.inf);C[edges[:,0],edges[:,1]]=e;parent,capacity=bottleneck_tree(C,root);capacities.append(capacity);graphs.append(dict(size=len(B),root=root,edges=edges,parent=parent,escape=e))
        s.update(graphs=graphs,capacities=capacities,objective=max(eps-min(capacities),0.));return s
    def args(s):return [s['R'],s['T'],s['A'],s['graphs'][0]['edges'],s['graphs'][1]['edges']]
    first=model(q);aa=args(first)
    def independent(qq):
        R,T,A,ue,se=aa;X,Z,Y,g,v=fam.independent_physical(qq,R,T,A)
        def escape(B,edges):
            a=B[edges[:,0]];d=B[edges[:,1]]-a;return np.sum(a*d,1)/np.sqrt(np.sum(a*a,1)*np.sum(d*d,1))
        return np.r_[escape(Z,ue),escape(Y,se),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(128904).normal(size=D);direction/=np.linalg.norm(direction);J=np.asarray(derivative(q,*aa));ve=float(np.max(abs(independent(q)-np.asarray(pieces(q,*aa)))));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('joint physical derivative gate failed')
    trust=.05;history=[];start=time.time();topology=None;fewest=np.inf
    for it in range(iterations):
        s=model(q);graphs=s['graphs'];lengths=[len(g['edges']) for g in graphs];L=sum(lengths);J=np.asarray(derivative(q,*args(s)));values=np.asarray(pieces(q,*args(s)));V,F=s['V'],s['F'];row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact','capacities','objective']};row.update(it=it,seconds=time.time()-start,trust=trust)
        if topology!=(V,s['E'],F) or s['S']+s['U']<fewest:
            name=f'state_{it:04d}_V{V}_E{s["E"]}_F{F}';np.save(out/(name+'_q.npy'),q);(out/(name+'.json')).write_text(json.dumps(row,indent=2)+'\n');row['checkpoint']=name;topology=(V,s['E'],F);fewest=min(fewest,s['S']+s['U'])
        history.append(row);np.save(out/'latest_q.npy',q);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('JOINT_ROOTED_PHYSICAL_FEASIBILITY',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);np.save(out/'NUMERICAL_NOMINATION_H.npy',s['H']);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        if s['objective']==0:raise ValueError('rooted feasibility and complete actual equilibrium census disagree')
        embedding=J[L:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D);C=J[:L]@W;g=values[:L];big=np.maximum(eps-g+bound*np.sum(abs(C),1)+1e-9,1e-9)
        nv=D+1+2*L;binary=D+1;flow=binary+L;blocks=[];lo=[];hi=[];scales=[]
        A=np.zeros((L,nv));A[:,:D]=C;A[:,D]=1
        for k in range(L):A[k,binary+k]=-big[k]
        blocks.append(A);lo.extend(eps-g-big);hi.extend([np.inf]*L);scales.extend([1000.]*L);offset=0;seed=np.zeros(nv)
        for graph in graphs:
            size=graph['size'];root=graph['root'];edges=graph['edges'];length=len(edges);owners=[i for i in range(size) if i!=root];owner={i:k for k,i in enumerate(owners)};A=np.zeros((size-1,nv))
            for k,(i,j) in enumerate(edges):A[owner[int(i)],binary+offset+k]=1
            blocks.append(A);lo.extend([1.]*(size-1));hi.extend([1.]*(size-1));scales.extend([1.]*(size-1))
            A=np.zeros((length,nv))
            for k in range(length):A[k,flow+offset+k]=1;A[k,binary+offset+k]=-(size-1)
            blocks.append(A);lo.extend([-np.inf]*length);hi.extend([0.]*length);scales.extend([1.]*length)
            A=np.zeros((size,nv))
            for k,(i,j) in enumerate(edges):A[i,flow+offset+k]+=1;A[j,flow+offset+k]-=1
            balance=np.ones(size);balance[root]=-(size-1);blocks.append(A);lo.extend(balance);hi.extend(balance);scales.extend([1.]*size)
            parent=graph['parent'];index={tuple(map(int,e)):k for k,e in enumerate(edges)};chosen={i:index[(i,int(parent[i]))] for i in owners}
            for i,k in chosen.items():seed[binary+offset+k]=1;seed[D]=max(seed[D],eps-g[offset+k]+1e-8)
            for i in owners:
                now=i
                while now!=root:
                    k=chosen[now];seed[flow+offset+k]+=1;now=int(parent[now])
            offset+=length
        A=np.vstack(blocks);lo=np.asarray(lo);hi=np.asarray(hi);scales=np.asarray(scales);lower=np.r_[np.full(D,-bound),0.,np.zeros(2*L)];upper=np.r_[np.full(D,bound),np.inf,np.ones(L),*[np.full(lengths[k],graphs[k]['size']-1) for k in range(2)]];integer=np.r_[np.zeros(D+1),np.ones(L),np.zeros(L)];cost=np.zeros(nv);cost[D]=1
        sol=solve(cost,A,lo,hi,lower,upper,integer,scales,seed,binary,L)
        violation=max(float(np.maximum(lo-A@sol.x,0).max()),float(np.maximum(A@sol.x-hi,0).max()),float(np.maximum(lower-sol.x,0).max()),float(np.maximum(sol.x-upper,0).max()));integral=float(abs(sol.x[binary:flow]-np.round(sol.x[binary:flow])).max());row.update(seed_objective=sol.seed_objective,seed_violation=sol.seed_violation,linear_violation=violation,integer_error=integral,mip_gap=sol.mip_gap,solver_version=sol.solver_version,maximum_coefficient_enclosure=sol.maximum_coefficient_enclosure)
        if violation>1e-7 or integral>1e-6:raise ValueError('joint MIP proposal fails its original complete local model')
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

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 0,int(sys.argv[5]) if len(sys.argv)>5 else 300)
