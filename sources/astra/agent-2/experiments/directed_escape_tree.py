"""Minimum-cost directed spanning tree oriented toward one fixed root.
Cycle contraction is exact for the supplied numeric edge-cost matrix. Search
uses a complete physical escape graph; these chords are not hull edges.
"""
import numpy as np

def minimum_tree(cost,root):
    C=np.asarray(cost,float).copy();n=len(C);np.fill_diagonal(C,np.inf);parent=C.argmin(1);parent[root]=root
    done=np.zeros(n,bool);done[root]=True;cycle=None
    for start in range(n):
        if done[start]:continue
        path=[];where={};v=start
        while not done[v] and v not in where:
            where[v]=len(path);path.append(v);v=int(parent[v])
        if v in where:cycle=np.array(path[where[v]:],int);break
        done[path]=True
    if cycle is None:return parent
    others=np.array([i for i in range(n) if i not in set(cycle)],int);k=len(others);supernode=k
    contracted=np.full((k+1,k+1),np.inf);contracted[:k,:k]=C[np.ix_(others,others)]
    incoming=C[np.ix_(others,cycle)];entry=incoming.argmin(1);contracted[:k,k]=incoming[np.arange(k),entry]
    outgoing=C[np.ix_(cycle,others)]-C[cycle,parent[cycle]][:,None];exit_vertex=outgoing.argmin(0);contracted[k,:k]=outgoing[exit_vertex,np.arange(k)]
    newroot=int(np.flatnonzero(others==root)[0]);higher=minimum_tree(contracted,newroot)
    for i,node in enumerate(others):
        par=int(higher[i]);parent[node]=int(cycle[entry[i]]) if par==supernode else int(others[par])
    par=int(higher[supernode])
    if par==supernode:raise ValueError('contracted nonroot cycle did not receive an exit')
    broken=int(cycle[exit_vertex[par]]);parent[broken]=int(others[par]);parent[root]=root
    return parent

def checked_tree(cost,root):
    parent=minimum_tree(cost,root);n=len(parent)
    for start in range(n):
        seen=set();v=start
        while v!=root:
            if v in seen:raise ValueError('minimum escape tree contains a cycle')
            seen.add(v);v=int(parent[v])
    mask=np.arange(n)!=root;total=float(np.asarray(cost)[np.arange(n)[mask],parent[mask]].sum())
    if not np.isfinite(total):raise ValueError('minimum escape tree is disconnected')
    return parent,total

if __name__=='__main__':
    import itertools,json,time
    from pathlib import Path
    rng=np.random.default_rng(491802);results=[];start=time.time()
    for n in [3,4,5]:
        for repeat in range(12):
            C=rng.integers(0,11,size=(n,n)).astype(float);root=repeat%n;np.fill_diagonal(C,np.inf);p,value=checked_tree(C,root);best=np.inf;vertices=[i for i in range(n) if i!=root]
            for choices in itertools.product(*[[j for j in range(n) if j!=i] for i in vertices]):
                trial=np.arange(n);trial[vertices]=choices;good=True
                for i in vertices:
                    seen=set();v=i
                    while v!=root:
                        if v in seen:good=False;break
                        seen.add(v);v=int(trial[v])
                    if not good:break
                if good:best=min(best,float(C[vertices,trial[vertices]].sum()))
            if value!=best:raise ValueError(('cycle-contraction failed independent exhaustive comparison',n,repeat,value,best))
            results.append(dict(n=n,repeat=repeat,root=root,minimum=value,exhaustive_minimum=best))
    out=Path(__file__).resolve().parents[1]/'artifacts/directed_escape_tree_validation.json';out.write_text(json.dumps(dict(cases=results,seconds=time.time()-start,scope='all possible rooted trees enumerated independently for these36 finite matrices; no polyhedron claim'),indent=2)+'\n');print('DIRECTED_TREE_VALIDATION',len(results),'cases passed',flush=True)
