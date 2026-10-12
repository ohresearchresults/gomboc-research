# material-afab63e1051a

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""TWO_APEX_ROOT_LEAF_OBSTRUCTION_V1. Exact standalone recovery.
CPython 3.13.5, standard library, no input files, assertions enabled.
python -S two_apex_root_leaf.py build
python -S two_apex_root_leaf.py check
Counts labeled selected tree pairs, not all physical bodies or old catalog orbits.
The companion proof establishes the continuous own-centroid obstruction.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY='TWO_APEX_ROOT_LEAF_OBSTRUCTION_V1'
SOURCES=[
 ['[internal-source-reference]','af169f4ded154478fff382b79d1beaa91071ef51b625dec2db222b0e470c48ab'],
 ['minimum-0087','b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5'],
 ['minimum-0086','8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10'],
 ['[internal-source-reference]','b6430662481d69144271f8cd75276f17e45c5e6b03ba86155b5eb1450622b17d']]

def determinant(a):
    a=[list(map(Q,row)) for row in a];out=Q(1);n=len(a)
    for k in range(n):
        i=next((i for i in range(k,n) if a[i][k]),None)
        if i is None:return Q(0)
        if i!=k:a[i],a[k]=a[k],a[i];out=-out
        p=a[k][k];out*=p
        for j in range(k+1,n):
            f=a[j][k]/p
            for t in range(k+1,n):a[j][t]-=f*a[k][t]
    return out

def tree_cofactor(vertices,edges):
    vertices=list(vertices);index={v:i for i,v in enumerate(vertices)};n=len(vertices)
    ll=[[0]*n for _ in vertices]
    for a,b in edges:
        if a not in index or b not in index:continue
        i,j=index[a],index[b]
        ll[i][i]+=1;ll[j][j]+=1;ll[i][j]-=1;ll[j][i]-=1
    ans=determinant([r[:-1] for r in ll[:-1]])
    assert ans.denominator==1
    return ans.numerator

def rooted(n,edges,root):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    par=[None]*n;par[root]=root;todo=[root]
    while todo:
        a=todo.pop()
        for b in adj[a]:
            if par[b] is None:par[b]=a;todo.append(b)
    return par if all(a is not None for a in par) else None

def facets(t):
    assert t in (1,2,3)
    return [tuple(range(8))]+[(i,i+1,8) for i in range(t)]+[(i,i+1,9) for i in range(t+1,7)]+[(t,t+1,9,8),(7,0,8,9)]

def incidence(ff):
    ef={}
    for i,f in enumerate(ff):
        for a,b in zip(f,f[1:]+f[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(i)
    assert len(ff)==9 and len(ef)==17 and all(len(v)==2 for v in ef.values())
    return sorted(ef),ef

def full_chain_starts(ff,pq,x):
    inc={i for i,f in enumerate(ff) if x in f}
    result=[]
    for start in sorted(inc):
        if pq[0]!=start:continue
        path=[start]
        while pq[path[-1]] in inc and pq[path[-1]] not in path:path.append(pq[path[-1]])
        if set(path)==inc:result.append(path)
    return result

def model(t):
    ff=facets(t);edges,ef=incidence(ff)
    total=0;leaves={x:[] for x in (8,9)};chain_records={x:[] for x in (8,9)}
    for kk in combinations(range(17),9):
        tt=[edges[k] for k in kk]
        if rooted(10,tt,8) is None:continue
        total+=1;mask=sum(1<<k for k in kk);ss=set(kk)
        dual=[tuple(ef[edges[k]]) for k in range(17) if k not in ss]
        assert rooted(9,dual,0) is not None
        for x in (8,9):
            z=17-x;neighbors=[b if a==x else a for a,b in tt if x in (a,b)]
            if neighbors!=[z]:continue
            leaves[x].append(mask)
            for stable in range(9):
                pq=rooted(9,dual,stable)
                for path in full_chain_starts(ff,pq,x):
                    assert set(ff[path[0]])&set(ff[path[-1]])=={x,z}
                    chain_records[x].append({'mask':mask,'U':x,'S':stable,'chain':path})
    assert total==tree_cofactor(range(10),edges)
    assert total==tree_cofactor(range(9),[tuple(ef[e]) for e in edges])
    for x in (8,9):
        assert len(leaves[x])==tree_cofactor([v for v in range(10) if v!=x],edges)
    expected={1:(3885,608,23),2:(4053,286,56),3:(4095,129,129)}
    assert (total,len(leaves[8]),len(leaves[9]))==expected[t]
    if t==2:assert len(chain_records[9])==24
    if t==3:assert len(chain_records[8])==len(chain_records[9])==66
    return {'t':t,'facets':ff,'lex_edges':edges,'all_primal_trees':total,
            'outside_degrees':[t+2,8-t],
            'root_leaf_masks':{str(x):leaves[x] for x in (8,9)},
            'root_leaf_count':[len(leaves[8]),len(leaves[9])],
            'all_stable_root_pair_count':9*(len(leaves[8])+len(leaves[9])),
            'old_full_xz_chain_overlap':{str(x):chain_records[x] for x in (8,9)}}

def build():
    balanced=[(0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),(3,8,9,4),(4,9,5),(5,9,6),(6,9,7),(7,9,8,0)]
    new_to_balanced=[0,1,2,3,5,6,7,4,8]
    assert all(set(f)==set(balanced[new_to_balanced[i]]) for i,f in enumerate(facets(3)))
    assert incidence(facets(3))[0]==incidence(balanced)[0]
    rows=[model(t) for t in (1,2,3)]
    assert [r['all_stable_root_pair_count'] for r in rows]==[5679,3078,2322]
    assert sum(r['all_stable_root_pair_count'] for r in rows)==11079
    return {'identity':IDENTITY,'source_identities':SOURCES,'scope':'THREE_NATIVE_LABELED_ROOF_MODELS_NOT_A_GLOBAL_CATALOG_DELTA',
            'balanced_vertex_map':list(range(10)),'new_t3_facet_to_old_balanced':new_to_balanced,
            'models':rows,'total_raw_selected_pair_exclusions':11079}

def encoded(obj):return (json.dumps(obj,ensure_ascii=True,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    out=Path('two_apex_root_leaf.json');data=encoded(build())
    if sys.argv[1]=='build':out.write_bytes(data)
    else:assert out.read_bytes()==data
    print('TWO_APEX_ROOT_LEAF_NATIVE_THREE_MODEL_COUNTS_11079_PASS')
    print('BALANCED_OLD_FULL_XZ_CHAIN_OVERLAP_132_PASS')
    print('LITERAL_ROOF8_DEG6_FULL_XZ_OVERLAP_24_PASS')
    print(out.name,len(data),hashlib.sha256(data).hexdigest())
    print('TWO_APEX_ROOT_LEAF_OBSTRUCTION_RECOVERY_PASS')

if __name__=='__main__':main()
