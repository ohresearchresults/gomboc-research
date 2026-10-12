"""Root-reaching escape-tree selection avoids impossible local two-cycle repairs."""
import json,time,sys,itertools
from pathlib import Path
import numpy as np
import networkx as nx
from atlas_opt import Atlas,optimize
from numeric import *

def rooted_parent(cos,edges,root,mode='barrier'):
    n=len(cos);G=nx.DiGraph();G.add_nodes_from(range(n))
    for a,b in sorted(edges):
        for i,j in [(a,b),(b,a)]:
            if i==root:continue
            c=float(cos[i,j]);negative=max(0,1e-5-c)
            weight=negative**2 if mode=='barrier' else negative
            weight+=1e-10*(1-c)+1e-14*(n*i+j)
            # Standard directed arborescences point away from their root.
            G.add_edge(j,i,weight=weight)
    T=nx.minimum_spanning_arborescence(G,attr='weight',default=1,preserve_attrs=True)
    assert len(T.edges)==n-1 and T.in_degree(root)==0
    parent=[-1]*n
    for j,i in T.edges:assert i!=root;parent[i]=j
    for i in range(n):
        seen=set();v=i
        while v!=root:
            assert v not in seen and parent[v]>=0;seen.add(v);v=parent[v]
    return parent

def assign_trees(m,u=None,mode='barrier'):
    u=m.u0 if u is None else u
    st=m.state(u,False)
    sparent=rooted_parent(st['cs'],{tuple(sorted(p)) for p in m.ef.values()},m.Sroot,mode)
    uparent=rooted_parent(st['cu'],set(m.ef),m.Uroot,mode)
    m.sparent=sparent;m.uparent=uparent
    after=m.state(u,False)
    return dict(sparent=sparent,uparent=uparent,initial_bad_s=[i for i in m.si if st['cs'][i,sparent[i]]<0],initial_bad_u=[i for i in m.ui if st['cu'][i,uparent[i]]<0],min_selected=float(after['vals'].min()))

def repair(gen,faces,outbase,steps=250,mode='barrier',stable=3,unstable=None,trust=.0005):
    m=Atlas(gen,faces,stable=stable,unstable=unstable);trees=assign_trees(m,mode=mode)
    outbase=Path(outbase);trees={k:[int(t) for t in v] if isinstance(v,list) else v for k,v in trees.items()};outbase.with_name(outbase.name+'_TREES.json').write_text(json.dumps(trees,sort_keys=True,separators=(',',':')))
    print('TREES',trees,flush=True)
    u,st,status=optimize(m,steps=steps,trust=trust,keep=1e-5,goal=5e-5)
    z=m.save(u,outbase.with_name(outbase.name+'_GENERATOR.json'));outbase.with_name(outbase.name+'_faces.json').write_text(json.dumps(faces,separators=(',',':')))
    rr=mechanics(recover(z)[:z['n_supports']],faces,tol=1e-10)
    outbase.with_name(outbase.name+'_numeric.json').write_text(json.dumps(dict(status=status,**rr),indent=2));print('TREE_REPAIR_FINISH',status,rr,flush=True)
    return z,rr

if __name__=='__main__':
    R=Path(__file__).parent
    g=json.loads((R/'C642_CONTACT_69_71_GENERATOR.json').read_text());fs=json.loads((R/'C642_CONTACT_69_71_faces.json').read_text())
    for a,b,moved in [(118,121,17),(173,175,123),(111,115,21),(175,176,104)]:
        z,ff=snapped(g,fs,a,b,moved)
        for mode in ['barrier','linear']:
            tag=f'TREE_E320_{a}_{b}_q{moved}_{mode}';print('TREE_CASE',tag,flush=True)
            out,rr=repair(z,ff,R/tag,steps=180,mode=mode)
            if rr['counts']==[1,1,0] and rr['min_gap']>1e-11 and min(rr['polar_escape_min'],rr['primal_escape_min'])>1e-6:
                print('TREE_WINNER',tag,flush=True);sys.exit(0)
