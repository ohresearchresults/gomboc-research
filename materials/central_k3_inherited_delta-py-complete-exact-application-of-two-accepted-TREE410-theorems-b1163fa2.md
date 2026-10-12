# material-b1163fa23106

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Literal application of two accepted TREE410 theorems to central K3 roots.
python -S central_k3_inherited_delta.py build|check
No new numerical certificate is asserted. The named immutable results are premises.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib,json,sys

if not __debug__:
    raise RuntimeError('Run with assertions enabled')
HERE=Path(__file__).resolve().parent
PINS={
 'central_k3_delta.py':(8054,'32548fcc62506a2eb7d5ad6e73d7660a318eb2e9fcb29f1030ad7a836562c556'),
 'central_k3_delta.json':(38699,'e619a9380936f7b499accb7ce6de3aeb5c6dc5e721035d4ca1963d6ec257de95'),
 'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'),
 'k3_classes.json':(2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c'),
}
PARENTS={
 'simple5_two_corners':('minimum-0073','1d49014bba25c54efd672b63e069a237360b910db645931aa1438fcb489295d2'),
 'quadrivalent4_no589':('minimum-0066','eb053ba6ddf8744442c3ac67938e4cef95225e83636a679bae4eab8ce9b77c70'),
}
PARENT=(0,0,1,2,3,4,0,6,7,8)
def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
def enc(a):return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
for name,want in PINS.items():assert pin((HERE/name).read_bytes())==want,('INPUT',name)
import central_k3_delta as B
C=B.C

def true_edges(faces):
    found={}
    for j,f in enumerate(faces):
        assert len(f)>=3 and len(set(f))==len(f)
        for k,v in enumerate(f):found.setdefault(C.edge(v,f[(k+1)%len(f)]),[]).append(j)
    assert all(len(q)==2 for q in found.values())
    return found

def neighbors(edges,v):return sorted(b if a==v else a for a,b in edges if v in(a,b))
def vertex_link(faces,v):
    out=[]
    for f in faces:
        if v in f:
            k=f.index(v);out.append(C.edge(f[k-1],f[(k+1)%len(f)]))
    assert len(out)==len(set(out))
    return sorted(out)

def check_faces(faces,vertices):
    assert set().union(*map(set,faces))==set(vertices)
    assert len({tuple(sorted(f)) for f in faces})==len(faces)
    edges=true_edges(faces)
    assert len(vertices)-len(edges)+len(faces)==2
    for a,b in combinations(faces,2):
        inter=set(a)&set(b)
        assert len(inter)<=2
        if len(inter)==2:assert C.edge(*inter) in edges
    for v in vertices:
        link=vertex_link(faces,v);verts=set(neighbors(edges,v))
        assert set(x for e in link for x in e)==verts
        assert all(sum(vv in e for e in link)==2 for vv in verts)
        reached={min(verts)}
        while True:
            nxt=reached|{b for a,b in link if a in reached}|{a for a,b in link if b in reached}
            if nxt==reached:break
            reached=nxt
        assert reached==verts
    # Three-vertex connectivity of the actual surviving graph.
    for removed in combinations(vertices,2):
        remaining=set(vertices)-set(removed);seen={min(remaining)}
        while True:
            nxt=seen|{b for a,b in edges if a in seen and b in remaining}|{a for a,b in edges if b in seen and a in remaining}
            if nxt==seen:break
            seen=nxt
        assert seen==remaining
    return edges

def interpret(z,rows):
    i,v=z['k3_index'],z['root'];row=rows[i];p=z['path'];r=z['path_root']
    assert r in(4,5) and p[r]==v and p==B.path_order(row)
    s=1 if r==4 else -1
    role=[p[r+s*k] for k in range(6)]+[p[r-s*k] for k in range(1,5)]
    assert sorted(role)==list(range(10)) and role[0]==v
    inverse={w:j for j,w in enumerate(role)}
    faces=[tuple(inverse[w] for w in f) for f in row['facet_cycles']]
    edges=check_faces(faces,list(range(10)))
    assert len(edges)==17 and len(faces)==9
    assert {C.edge(role[a],role[b]) for a,b in edges}==set(map(tuple,row['edges']))
    arrows={(j,PARENT[j]) for j in range(1,10)}
    assert {C.edge(*e) for e in arrows}=={C.edge(inverse[a],inverse[b]) for a,b in row['tree_edges']}
    assert all(C.edge(*e) in edges for e in arrows)
    for child,parent in arrows:
        assert abs(p.index(role[child])-r)==abs(p.index(role[parent])-r)+1
    assert {4,5,9} in list(map(set,faces))
    n5=neighbors(edges,5);n4=neighbors(edges,4);link4=vertex_link(faces,4)
    simple=False;j=None;qfaces=None;nq4=None;nq9=None
    if len(n5)==3:
        assert {4,9}<=set(n5)
        j=next(w for w in n5 if w not in(4,9))
        qfaces=[tuple(w for w in f if w!=5) for f in faces]
        qfaces=[f for f in qfaces if len(f)>=3]+[tuple(n5)]
        qe=check_faces(qfaces,[w for w in range(10) if w!=5])
        assert {e for e in edges if 5 not in e}<=set(qe)
        nq4=neighbors(qe,4);nq9=neighbors(qe,9)
        simple=(j in(6,7) and (len(nq4)==3 or len(nq9)==3)) or (j==8 and len(nq4)==3)
    quad=(n4==[0,3,5,9] and link4==[(0,3),(0,5),(3,9),(5,9)]
          and {5,8,9} not in list(map(set,faces)))
    return {'k3_index':i,'root':v,'role_to_census':role,'role_facets':faces,
       'role_edges':sorted(edges),'role_arrows':sorted(arrows),'N5':n5,'N4':n4,
       'link4':link4,'simple5_extra_neighbor':j,'Q_facets':qfaces,'NQ4':nq4,'NQ9':nq9,
       'simple5_two_corners':simple,'quadrivalent4_no589':quad}

def build():
    d=json.loads((HERE/'central_k3_delta.json').read_text())
    assert d['identity']=='MINIMUM_K3_CENTRAL_FORCED_FACET_DELTA_V1'
    rows=json.loads((HERE/'k3_domains.json').read_text())['rows']
    classes=json.loads((HERE/'k3_classes.json').read_text())['classes']
    prior={tuple(p) for p in d['old_positions']+d['new_excluded_positions']}
    priorclasses=set(d['old_classes']+d['new_excluded_classes'])
    original={(i,z['vertex']) for i,row in enumerate(rows) for z in row['roots'] if z['status']=='open'}
    assert len(original-prior)==9393 and len(classes)-len(priorclasses)==6985
    central=d['central_passing_positions'];assert len(central)==45
    records={(z['k3_index'],z['root']):interpret(z,rows) for z in central}
    sets={name:{p for p,a in records.items() if a[name]} for name in PARENTS}
    simple,quad=(sets[name] for name in PARENTS)
    assert len(simple)==23 and len(quad)==9 and len(simple&quad)==4
    new=simple|quad;passing=set(records)-new
    assert len(new)==28 and len(passing)==17 and not new&prior
    assert quad-simple=={(296,3),(382,1),(676,3),(677,3),(872,8)}
    mapping={};newclasses=set();passclasses=set();simpleclasses=set();quadclasses=set()
    for c in classes:
        members={(m['k3_index'],m['root']) for m in c['members']}
        for p in members:assert p not in mapping;mapping[p]=c['class_index']
        if not members&set(records):continue
        assert members<=set(records)
        i,r=c['representative'];a=records[i,r]
        for m in c['members']:
            j,t=m['k3_index'],m['root'];b=records[j,t]
            B.transport(rows[i],rows[j],m,r)
            # Unequal branch lengths canonically distinguish every TREE410 role.
            assert [m['vertex_map'][w] for w in a['role_to_census']]==b['role_to_census']
            for name in PARENTS:assert a[name]==b[name]
        for selected,collector in ((new,newclasses),(passing,passclasses),(simple,simpleclasses),(quad,quadclasses)):
            if members&selected:assert members<=selected;collector.add(c['class_index'])
    assert len(newclasses)==26 and len(passclasses)==15
    assert len(simpleclasses)==21 and len(quadclasses)==9
    assert not newclasses&priorclasses
    remaining=original-prior-new
    remainingclasses=set(range(len(classes)))-priorclasses-newclasses
    assert len(remaining)==9365 and len(remainingclasses)==6959
    opendomains={i for i,r in remaining}
    assert opendomains=={i for i,r in original-prior} and len(opendomains)==1949
    assert {mapping[p] for p in remaining}==remainingclasses
    for p,a in records.items():a['class_index']=mapping[p]
    output={'identity':'MINIMUM_K3_CENTRAL_INHERITED_DELTA_V1','input_pins':PINS,
      'parent_results':PARENTS,'prior_delta_proof':'[internal-source-reference]',
      'simple5_positions':sorted(simple),'simple5_classes':sorted(simpleclasses),
      'quad4_positions':sorted(quad),'quad4_classes':sorted(quadclasses),
      'overlap_positions':sorted(simple&quad),'new_excluded_positions':sorted(new),
      'new_excluded_classes':sorted(newclasses),'central_remaining_positions':sorted(passing),
      'central_remaining_classes':sorted(passclasses),'literal_records':[records[p] for p in sorted(records)],
      'positions_remaining':len(remaining),'classes_remaining':len(remainingclasses),
      'open_domains':len(opendomains),'whole_excluded_domains':len(rows)-len(opendomains),
      'new_whole_excluded_domains':[],
      'remaining_class_kinds':dict(sorted(Counter(classes[j]['kind'] for j in remainingclasses).items())),
      'scope':'Exact K3 mapping of accepted geometric theorems; no new TREE410 global count, K2 closure, or complexity bound. Remaining is not feasibility.'}
    return enc(output)

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'central_k3_inherited_delta.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b,('OUTPUT',p.name)
    else:p.write_bytes(b)
    print('K3_CENTRAL_INHERITED_THEOREMS_PASS',23,9,4,28,26,17,15,9365,6959,1949,358,*pin(b))
if __name__=='__main__':main()
