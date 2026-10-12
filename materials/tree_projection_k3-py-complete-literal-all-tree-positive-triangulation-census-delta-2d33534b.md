# material-2d33534bf728

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact true-tree projection/triangulation exclusion over the complete K3 remainder.
Run: python -S tree_projection_k3.py build|check. Python standard library only.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
if not __debug__:
    raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent
PINS={
 'path_projection_extra.py':(4786,'8fc3aab988f76dbe157b37b16e248ce910e6ca539883d11ed9533b4912939915'),
 'central_k3_delta.py':(8054,'32548fcc62506a2eb7d5ad6e73d7660a318eb2e9fcb29f1030ad7a836562c556'),
 'central_k3_delta.json':(38699,'e619a9380936f7b499accb7ce6de3aeb5c6dc5e721035d4ca1963d6ec257de95'),
 'central_k3_inherited_delta.py':(9259,'b1163fa23106f7fffd3a6739cb5b84c2f0da8ed6db62422e89efb4d8a31e5944'),
 'central_k3_inherited_delta.json':(30360,'8741265f2f347c16b0a3ef7b6c0cdc21ed80aa8b4e8e854d70fe9590b1d54630'),
 'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'),
 'k3_classes.json':(2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c'),
 'path_projection.py':(6201,'42f6a03f6756de1f8266c4923c59e2991b9486e01c7884720a1dfab17d54c289'),
}
def pin(b):return(len(b),hashlib.sha256(b).hexdigest())
def enc(a):return(json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
for name,want in PINS.items():assert pin((HERE/name).read_bytes())==want,('INPUT',name)
import central_k3_delta as B
import central_k3_inherited_delta as I
import path_projection_extra as E
C=B.C

def root_paths(row,root):
    edges=set(map(tuple,row['tree_edges']));assert len(edges)==9
    assert edges<=set(map(tuple,row['edges']))
    adj={v:[] for v in range(10)}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    paths={root:(root,)};queue=[root]
    for v in queue:
        for w in sorted(adj[v]):
            if w not in paths:paths[w]=paths[v]+(w,);queue.append(w)
    assert len(paths)==10
    assert {C.edge(p[-2],v) for v,p in paths.items() if v!=root}==edges
    return tuple(paths[v] for v in range(10))

def triangle_tester(paths,level):
    root=paths[0][0];assert all(p[0]==root and p[-1]==v for v,p in enumerate(paths))
    depth=[len(p)-1 for p in paths]
    cuts=E.OLD_PAIRS+(E.TRIPLES if level>=1 else [])+(E.EXTRA if level>=2 else [])
    @lru_cache(None)
    def bound(tri):
        assert len(set(tri))==len(tri)==3 and root not in tri
        best=sum((E.P.DEPTH[depth[v]] for v in tri),F(0));reason=('depth',)
        if best<1:return best,reason
        for terms,b in cuts:
            for path in paths:
                if len(path)<=max(terms):continue
                chosen={path[j] for j in terms}
                if chosen<=set(tri):
                    x=b+sum((E.P.DEPTH[depth[v]] for v in set(tri)-chosen),F(0))
                    if x<best:best=x;reason=('chain',terms,path)
                    if x<1:return best,reason
        return best,reason
    return bound

def triangulate(face,bound):
    @lru_cache(None)
    def go(a,b):
        if b-a<2:return ()
        for k in range(a+1,b):
            tri=(face[a],face[k],face[b])
            if bound(tuple(sorted(tri)))[0]>=1:continue
            left,right=go(a,k),go(k,b)
            if left is not None and right is not None:return left+right+(tri,)
        return None
    return go(0,len(face)-1)

def build():
    # These are exact identities, independently reproducible at every run.
    E.P.build();E.build()
    rows=json.loads((HERE/'k3_domains.json').read_text())['rows']
    classes=json.loads((HERE/'k3_classes.json').read_text())['classes']
    d=json.loads((HERE/'central_k3_delta.json').read_text())
    h=json.loads((HERE/'central_k3_inherited_delta.json').read_text())
    assert d['identity']=='MINIMUM_K3_CENTRAL_FORCED_FACET_DELTA_V1'
    assert h['identity']=='MINIMUM_K3_CENTRAL_INHERITED_DELTA_V1'
    original={(i,z['vertex']) for i,row in enumerate(rows) for z in row['roots'] if z['status']=='open'}
    prior=set(map(tuple,d['old_positions']+d['new_excluded_positions']+h['new_excluded_positions']))
    priorclasses=set(d['old_classes']+d['new_excluded_classes']+h['new_excluded_classes'])
    remaining=original-prior
    assert len(rows)==2307 and len(original)==11743 and len(remaining)==9365
    assert len(classes)==8739 and len(classes)-len(priorclasses)==6959
    passed=[set(),set(),set()];proofs={};pathmaps={};fan_count=0;used=Counter();minimum=F(1)
    for i,row in enumerate(rows):
        assert row['k3_index']==i
        edges=I.check_faces([tuple(f) for f in row['facet_cycles']],list(range(10)))
        assert set(edges)==set(map(tuple,row['edges'])) and len(edges)==17
        assert len(row['facet_cycles'])==9
        for v in range(10):
            assert sorted(j for j,f in enumerate(row['facet_cycles']) if v in f)==row['incidence'][v]
        for root in range(10):
            pos=(i,root)
            if pos not in remaining:continue
            paths=root_paths(row,root);pathmaps[pos]=paths
            for level in range(3):
                bound=triangle_tester(paths,level);fans=[]
                for j,face in enumerate(row['facet_cycles']):
                    if root in face:continue
                    ts=triangulate(tuple(face),bound)
                    if ts is None:break
                    E.P.verify_triangulation(face,ts)
                    fans.append((j,ts))
                else:
                    assert fans
                    passed[level].add(pos)
                    if level==2:
                        proof=[]
                        for j,ts in fans:
                            for tri in ts:
                                b,reason=bound(tuple(sorted(tri)));assert b<1
                                minimum=min(minimum,1-b);fan_count+=1
                                if reason[0]=='chain':used[reason[1]]+=1
                            proof.append((j,ts))
                        proofs[pos]=proof
    assert passed[0]<=passed[1]<=passed[2]
    new=passed[2];newclasses=set();seen=set();levelclasses=[set(),set(),set()]
    for c in classes:
        j=c['class_index'];i,root=c['representative']
        members={(m['k3_index'],m['root']) for m in c['members']}
        assert not members&seen;seen|=members
        if members&prior:assert members<=prior and j in priorclasses;continue
        assert members<=remaining
        for m in c['members']:
            k,r=m['k3_index'],m['root'];B.transport(rows[i],rows[k],m,root)
            p=pathmaps[i,root];q=pathmaps[k,r]
            for v,path in enumerate(p):assert tuple(m['vertex_map'][w] for w in path)==q[m['vertex_map'][v]]
        for level in range(3):
            if members&passed[level]:assert members<=passed[level];levelclasses[level].add(j)
        if members&new:newclasses.add(j)
    assert seen==original and newclasses==levelclasses[2]
    assert len(new)==2706 and len(newclasses)==2142
    left=remaining-new;leftclasses=set(range(len(classes)))-priorclasses-newclasses
    assert len(left)==6659 and len(leftclasses)==4817
    prior_domains={i for i,r in remaining};open_domains={i for i,r in left}
    new_whole=sorted(prior_domains-open_domains)
    assert len(prior_domains)==1949 and len(open_domains)==1776 and len(new_whole)==173
    pathnew={p for p in new if B.path_order(rows[p[0]]) is not None}
    ynew=new-pathnew
    assert len(pathnew)==2006 and len(ynew)==700
    assert not any(rows[i]['roots'][r]['tree_index'] in(410,718) for i,r in new)
    summary=[]
    for level in range(3):
        paths={p for p in passed[level] if B.path_order(rows[p[0]]) is not None}
        summary.append({'level':level,'positions':len(passed[level]),'classes':len(levelclasses[level]),
                        'path_positions':len(paths),'Y_positions':len(passed[level]-paths)})
    assert [r['path_positions'] for r in summary]==[595,1355,2006]
    out={'identity':'MINIMUM_TREE_PROJECTION_K3_DELTA_V1','input_pins':PINS,
      'prior_proof':'[internal-source-reference]','levels':summary,
      'new_positions':sorted(new),'new_classes':sorted(newclasses),
      'literal_positive_triangulations':[(i,r,proofs[i,r]) for i,r in sorted(new)],
      'new_whole_domains':new_whole,'positions_remaining':len(left),'classes_remaining':len(leftclasses),
      'open_domains':len(open_domains),'whole_excluded_domains':len(rows)-len(open_domains),
      'new_exclusions_by_tree':dict(sorted(Counter(rows[i]['roots'][r]['tree_index'] for i,r in new).items())),
      'remaining_class_trees':dict(sorted(Counter(classes[j]['tree_index'] for j in leftclasses).items())),
      'remaining_class_kinds':dict(sorted(Counter(classes[j]['kind'] for j in leftclasses).items())),
      'triangles_checked':fan_count,'minimum_projection_gap':str(minimum),
      'used_chain_certificates':[(t,n) for t,n in sorted(used.items())],
      'scope':'Literal K3 register only. Neither the global TREE410 register nor K2 nor C bounds change. Failure of this sufficient screen does not prove feasibility.'}
    return enc(out)

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'tree_projection_k3.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b,('OUTPUT',p.name)
    else:p.write_bytes(b)
    print('TREE_PROJECTION_K3_EXACT_DELTA_PASS',2706,2142,6659,4817,1776,531,173,*pin(b))
if __name__=='__main__':main()
