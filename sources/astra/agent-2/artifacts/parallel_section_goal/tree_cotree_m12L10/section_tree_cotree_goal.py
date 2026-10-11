"""Joint physical shape and complementary primal/polar escape-tree search.

This is an explicit constructive restriction, not a claimed characterization
of every mono-monostatic polyhedron. Primal and polar rooted trees partition
the genuine edges. A primal spanning tree has a complementary dual spanning
tree, so one primal flow certificate suffices together with both out-degree
conditions. Every selected edge must become a strictly positive escape at the
same physical body's actual uniform centroid. The actual complete census is
checked separately. No relaxed tree, metric or residual qualifies the Figure.
"""
import sys,json,hashlib,time
from pathlib import Path
from collections import deque
import numpy as np
from scipy.linalg import svd
import jax
import jax.numpy as jnp
from parallel_section_family import SectionFamily
from cap_disjunctive_goal import bottleneck_tree
from seeded_escape_milp import solve

def run(src,normal_src,out,L,iterations=200,eps=1e-6):
    src=Path(src);normal_src=Path(normal_src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();nraw=normal_src.read_bytes();(out/'source_q.npy').write_bytes(raw);(out/'normals.npy').write_bytes(nraw);q=np.load(out/'source_q.npy');normals=np.load(out/'normals.npy');fam=SectionFamily(normals,L);m=fam.m;D=m*L;V=F=D+1;E=2*D;G=L+m*L+m*(L-1);s=fam.state(q);ur=int(np.argmax(np.sum(s['Z']**2,1)));sr=int(np.argmax(np.sum(s['Y']**2,1)))
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),normal_source=str(normal_src),normal_sha256=hashlib.sha256(nraw).hexdigest(),m=m,L=L,eps=eps,roots=[ur,sr],fixed_levels=True,method=__doc__),indent=2)+'\n')
    for name in ['parallel_section_family.py','section_tree_cotree_goal.py','seeded_escape_milp.py']:(out/name).write_bytes((Path(__file__).parent/name).read_bytes())
    graphs=[]
    for undirected,root in [(fam.eu,ur),(fam.es,sr)]:
        directed=np.r_[undirected,undirected[:,::-1]];edgeids=np.tile(np.arange(E),2);active=directed[:,0]!=root;graphs.append(dict(edges=directed[active],ids=edgeids[active],root=root,size=V))
    ue,se=graphs[0]['edges'],graphs[1]['edges'];Lu,Ls=len(ue),len(se);Le=Lu+Ls
    @jax.jit
    def pieces(q):
        X,Z,Y,g,v,N,d=fam.physical(q)
        def angle(B,edges):
            a=B[edges[:,0]];delta=B[edges[:,1]]-a;return jnp.sum(a*delta,1)/jnp.sqrt(jnp.sum(a*a,1)*jnp.sum(delta*delta,1))
        xy=X[:-1,:2].reshape(L,m,2);tangent=jnp.c_[-jnp.asarray(normals)[:,1],jnp.asarray(normals)[:,0]];length=jnp.sum((xy-jnp.roll(xy,1,axis=1))*tangent[None,:,:],axis=2);z=q[m*L:];h=q[:m*L].reshape(L,m);dz=jnp.diff(jnp.r_[z,1.]);slope=jnp.diff(jnp.r_[h,jnp.zeros((1,m))],axis=0)/dz[:,None];curv=slope[:-1]-slope[1:]
        return jnp.r_[angle(Z,ue),angle(Y,se),dz,length.ravel(),curv.ravel(),Z.ravel(),Y.ravel()]
    derivative=jax.jit(jax.jacfwd(pieces,argnums=0));values=np.asarray(pieces(q));floor=np.minimum(values[Le:Le+G]*.01,1e-7)
    if floor.min()<=0:raise ValueError('strict section convexity is required')
    def independent(qq):
        X,Z,Y,g,v,N,d=fam.independent_physical(qq)
        def angle(B,edges):
            a=B[edges[:,0]];delta=B[edges[:,1]]-a;return np.sum(a*delta,1)/np.sqrt(np.sum(a*a,1)*np.sum(delta*delta,1))
        xy=X[:-1,:2].reshape(L,m,2);tangent=np.c_[-normals[:,1],normals[:,0]];length=np.sum((xy-np.roll(xy,1,axis=1))*tangent[None,:,:],axis=2);z=qq[m*L:];h=qq[:m*L].reshape(L,m);dz=np.diff(np.r_[z,1.]);slope=np.diff(np.r_[h,np.zeros((1,m))],axis=0)/dz[:,None];curv=slope[:-1]-slope[1:]
        return np.r_[angle(Z,ue),angle(Y,se),dz,length.ravel(),curv.ravel(),Z.ravel(),Y.ravel()]
    direction=np.random.default_rng(315408).normal(size=len(q));direction/=np.linalg.norm(direction);J=np.asarray(derivative(q));ve=float(np.max(abs(independent(q)-values)));de=float(np.max(abs(np.imag(independent(q.astype(complex)+1e-25j*direction))/1e-25-J@direction))/max(1,np.max(abs(J@direction))))
    (out/'independent_derivative_check.json').write_text(json.dumps(dict(value_error=ve,complex_step_relative_error=de),indent=2)+'\n')
    if ve>1e-8 or de>1e-7:raise ValueError('tree-cotree physical derivative gate failed')
    matrix=np.full((V,V),-np.inf);matrix[ue[:,0],ue[:,1]]=values[:Lu];up,_=bottleneck_tree(matrix,ur);ui={tuple(map(int,e)):k for k,e in enumerate(ue)};chosen_u=np.array([ui[(i,int(up[i]))] for i in range(V) if i!=ur],int);used=set(map(int,graphs[0]['ids'][chosen_u]));remaining=[i for i in range(E) if i not in used];adj=[[] for _ in range(F)]
    for i in remaining:a,b=map(int,fam.es[i]);adj[a].append(b);adj[b].append(a)
    sp=np.full(F,-1,int);sp[sr]=sr;queue=deque([sr])
    while queue:
        a=queue.popleft()
        for b in adj[a]:
            if sp[b]<0:sp[b]=a;queue.append(b)
    if len(remaining)!=F-1 or (sp<0).any():raise ValueError('complement of primal tree is not a dual spanning tree')
    si={tuple(map(int,e)):k for k,e in enumerate(se)};chosen_s=np.array([si[(i,int(sp[i]))] for i in range(F) if i!=sr],int);selected=np.r_[chosen_u,Lu+chosen_s];history=[];start=time.time();trust=.04;fewest=np.inf
    binary=D+1;flow=binary+Le;nv=flow+Lu
    def flow_seed(chosen):
        seed=np.zeros(nv);seed[binary+chosen]=1.;seed[D]=max(0.,float(np.max(eps-values[chosen])))+1e-7;parent={int(ue[k,0]):int(ue[k,1]) for k in chosen if k<Lu};index={int(ue[k,0]):int(k) for k in chosen if k<Lu}
        for i in range(V):
            if i==ur:continue
            now=i;visited=set()
            while now!=ur:
                if now in visited or now not in parent:raise ValueError('saved primal certificate is not rooted')
                visited.add(now);seed[flow+index[now]]+=1;now=parent[now]
        return seed
    for it in range(iterations):
        s=fam.state(q);values=np.asarray(pieces(q));J=np.asarray(derivative(q))[:,:D];objective=max(0.,float(np.max(eps-values[selected])));row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(it=it,seconds=time.time()-start,objective=objective,trust=trust)
        if s['S']+s['U']<fewest:
            fewest=s['S']+s['U'];np.save(out/f'fewest_{it:04d}_q.npy',q);(out/f'fewest_{it:04d}.json').write_text(json.dumps(row,indent=2)+'\n')
        history.append(row);np.save(out/'latest_q.npy',q);np.save(out/'latest_selected.npy',selected);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('PHYSICAL_TREE_COTREE_GOAL',row,flush=True)
        if s['S']==s['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return q
        if objective==0:raise ValueError('positive complementary trees disagree with complete actual census')
        embedding=J[Le+G:];metric=np.vstack([embedding[:3*V]/np.sqrt(np.mean(s['Z']**2)),embedding[3*V:]/np.sqrt(np.mean(s['Y']**2)),np.eye(D)*.03]);_,sing,Wt=svd(metric,full_matrices=False,check_finite=False);W=Wt.T/sing;bound=trust/np.sqrt(D);C=J[:Le]@W;geo=J[Le:Le+G]@W;big=np.maximum(eps-values[:Le]+bound*np.sum(abs(C),1)+1e-9,1e-9);blocks=[];lo=[];hi=[];scales=[]
        A=np.zeros((Le,nv));A[:,:D]=C;A[:,D]=1.;A[np.arange(Le),binary+np.arange(Le)]=-big;blocks.append(A);lo.extend(eps-values[:Le]-big);hi.extend([np.inf]*Le);scales.extend([1000.]*Le)
        A=np.zeros((G,nv));A[:,:D]=geo;blocks.append(A);lo.extend(floor-values[Le:Le+G]);hi.extend([np.inf]*G);scales.extend([1000.]*G)
        offset=0
        for graph in graphs:
            owners=[i for i in range(V) if i!=graph['root']];order={i:k for k,i in enumerate(owners)};A=np.zeros((V-1,nv))
            for k,(a,b) in enumerate(graph['edges']):A[order[int(a)],binary+offset+k]=1
            blocks.append(A);lo.extend([1.]*(V-1));hi.extend([1.]*(V-1));scales.extend([1.]*(V-1));offset+=len(graph['edges'])
        A=np.zeros((E,nv));allids=np.r_[graphs[0]['ids'],graphs[1]['ids']];A[allids,binary+np.arange(Le)]=1;blocks.append(A);lo.extend([1.]*E);hi.extend([1.]*E);scales.extend([1.]*E)
        A=np.zeros((Lu,nv));A[np.arange(Lu),flow+np.arange(Lu)]=1;A[np.arange(Lu),binary+np.arange(Lu)]=-(V-1);blocks.append(A);lo.extend([-np.inf]*Lu);hi.extend([0.]*Lu);scales.extend([1.]*Lu)
        A=np.zeros((V,nv))
        for k,(a,b) in enumerate(ue):A[a,flow+k]+=1;A[b,flow+k]-=1
        balance=np.ones(V);balance[ur]=-(V-1);blocks.append(A);lo.extend(balance);hi.extend(balance);scales.extend([1.]*V)
        A=np.vstack(blocks);lo=np.asarray(lo);hi=np.asarray(hi);scales=np.asarray(scales);lower=np.r_[np.full(D,-bound),0.,np.zeros(Le+Lu)];upper=np.r_[np.full(D,bound),np.inf,np.ones(Le),np.full(Lu,V-1)];integer=np.r_[np.zeros(D+1),np.ones(Le),np.zeros(Lu)];cost=np.zeros(nv);cost[D]=1;seed=flow_seed(selected);sol=solve(cost,A,lo,hi,lower,upper,integer,scales,seed,binary,Le);violation=max(float(np.maximum(lo-A@sol.x,0).max()),float(np.maximum(A@sol.x-hi,0).max()),float(np.maximum(lower-sol.x,0).max()),float(np.maximum(sol.x-upper,0).max()));integral=float(abs(sol.x[binary:flow]-np.round(sol.x[binary:flow])).max());row.update(linear_violation=violation,integer_error=integral,seed_objective=sol.seed_objective,solver_version=sol.solver_version)
        if violation>1e-7 or integral>1e-6:raise ValueError('tree-cotree MIP proposal fails original complete local model')
        proposed=np.flatnonzero(sol.x[binary:flow]>.5);step=np.zeros_like(q);step[:D]=W@sol.x[:D];accepted=False
        for back in range(24):
            trial=q+2**-back*step
            try:t=fam.state(trial);tv=np.asarray(pieces(trial))
            except (ValueError,AssertionError,np.linalg.LinAlgError):continue
            if np.min(tv[Le:Le+G]/floor)<.99:continue
            newobjective=max(0.,float(np.max(eps-tv[proposed])))
            if t['S']==t['U']==1:
                np.save(out/'NUMERICAL_NOMINATION_q.npy',trial);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps({k:t[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']},indent=2)+'\n');return trial
            if newobjective<objective*(1-1e-10):q=trial;selected=proposed;row['alpha']=2**-back;accepted=True;break
        if accepted and back==0:trust=min(.5,trust*1.35)
        if not accepted:trust*=.4
        if trust<1e-12:break
    np.save(out/'final_q.npy',q);(out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(goal_complete=False,iterations=iterations),indent=2)+'\n');return q

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]) if len(sys.argv)>5 else 200)
