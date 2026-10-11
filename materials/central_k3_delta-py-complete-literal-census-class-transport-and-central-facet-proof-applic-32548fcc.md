# material-32548fcc6250

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Exact application of CENTRAL_ROOT_FORCED_FACET_V1 to the K3 census.
Usage: python -S central_k3_delta.py build|check. Standard library only.
The old singleton is inherited from its named accepted proof, not re-proved here.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib,json,sys

if not __debug__:
    raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent
PINS={
 'central_root.py':(6759,'c0fa7d4662c6863efb88ac356e3518a82cbac40bea2fda838be416797868ccaf'),
 'k3_census.py':(13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'),
 'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'),
 'k3_classes.json':(2332920,'e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c'),
}
def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
def enc(a):return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
for name,want in PINS.items():assert pin((HERE/name).read_bytes())==want,('INPUT',name)
import central_root as R
import k3_census as C

def path_order(row):
    adj=[[] for _ in range(10)]
    for a,b in row['tree_edges']:adj[a].append(b);adj[b].append(a)
    if max(map(len,adj))!=2:return None
    ends=[v for v in range(10) if len(adj[v])==1]
    assert len(ends)==2
    p=[min(ends)]
    while len(p)<10:
        following=[v for v in adj[p[-1]] if len(p)==1 or v!=p[-2]]
        assert len(following)==1
        p.append(following[0])
    assert len(set(p))==10 and p[-1]==max(ends)
    return p

def transport(a,b,m,root):
    p=m['vertex_map'];f=m['facet_map'];o=m['orientation']
    assert sorted(p)==list(range(10)) and sorted(f)==list(range(9)) and o in(-1,1)
    assert p[root]==m['root']
    for key in ('edges','tree_edges'):
        assert {C.edge(p[x],p[y]) for x,y in a[key]}==set(map(tuple,b[key]))
    for i,face in enumerate(a['facet_cycles']):
        image=tuple(p[v] for v in face);target=tuple(b['facet_cycles'][f[i]])
        assert C.cyc(image)==C.cyc(target if o==1 else target[::-1])
    for v,inc in enumerate(a['incidence']):
        assert sorted(f[j] for j in inc)==b['incidence'][p[v]]

def build():
    R.main()
    d=json.loads((HERE/'k3_domains.json').read_text())
    q=json.loads((HERE/'k3_classes.json').read_text())
    assert d['identity']=='MINIMUM_TREE253_K3_LITERAL_DOMAINS_V1'
    assert q['identity']=='MINIMUM_K3_ROOTED_TRUE_FACET_TREE_CLASSES_V1'
    rows=d['rows'];classes=q['classes'];assert len(rows)==2307 and len(classes)==8739
    old={(287,6)};oldclasses={1491}
    assert rows[287]['incidence']==[list(t) for t in R.ROWS]
    assert path_order(rows[287])==list(R.PATH)
    assert rows[287]['roots'][6]=={'vertex':6,'tree_index':718,'status':'open'}
    assert classes[1491]['representative']==[287,6]
    assert classes[1491]['members']==[{'k3_index':287,'root':6,
       'vertex_map':list(range(10)),'facet_map':list(range(9)),'orientation':1}]
    original={(i,z['vertex']) for i,row in enumerate(rows) for z in row['roots'] if z['status']=='open'}
    assert len(original)==11743 and old<=original
    new=set();passing=set();details={};fans=0;hist=Counter()
    bounds=R.verify_pairs()
    for i,row in enumerate(rows):
        assert row['k3_index']==i
        p=path_order(row)
        for z in row['roots']:
            v=z['vertex'];assert row['roots'][v]==z
            if z['status']!='open' or z['tree_index']!=410:continue
            assert p is not None
            root=p.index(v);assert root in(4,5)
            pos=(i,v);inv={w:j for j,w in enumerate(p)}
            ex={p[j] for j in R.exception(root)}
            facets=[j for j,f in enumerate(row['facet_cycles']) if set(f)==ex]
            assert len(facets)<=1
            detail={'k3_index':i,'root':v,'path':p,'path_root':root,
                    'exception_vertices':sorted(ex),'exception_facet':facets,
                    'window':row['window'],'kind':row['kind']}
            details[pos]=detail
            if facets:
                passing.add(pos);hist['passing_'+row['kind']]+=1
                assert C.edge(p[0],p[9]) in set(map(tuple,row['edges']))
            else:
                new.add(pos);hist['excluded_'+row['kind']]+=1
                for face in row['facet_cycles']:
                    if v in face:continue
                    anchors=set(face)-ex;assert anchors
                    for t in R.fan(tuple(face),min(anchors)):
                        gap,kind=R.margin(root,[inv[w] for w in t],bounds)
                        assert gap is not None and gap>=R.EPS
                        fans+=1
    assert len(new)==2349 and len(passing)==45 and not(new&old)
    assert len(details)==2394 and new|passing==set(details)
    # Each genuine rooted primal incidence/tree isomorphism is checked literally.
    newclasses=set();passclasses=set();seen=set();remainingclasses=[]
    for j,c in enumerate(classes):
        assert c['class_index']==j
        i,r=c['representative'];a=rows[i]
        mem={(m['k3_index'],m['root']) for m in c['members']}
        assert mem<=original and not(mem&seen);seen|=mem
        for m in c['members']:
            b=rows[m['k3_index']];transport(a,b,m,r)
            assert a['roots'][r]['tree_index']==b['roots'][m['root']]['tree_index']==c['tree_index']
            if (i,r) in details:
                left=details[i,r];right=details[m['k3_index'],m['root']]
                image=[m['vertex_map'][v] for v in left['path']]
                assert image in(right['path'],right['path'][::-1])
                assert {m['vertex_map'][v] for v in left['exception_vertices']}==set(right['exception_vertices'])
                assert {m['facet_map'][f] for f in left['exception_facet']}==set(right['exception_facet'])
        if mem&new:assert mem<=new;newclasses.add(j)
        if mem&passing:assert mem<=passing;passclasses.add(j)
        if not mem<=(old|new):
            assert not mem&(old|new);remainingclasses.append(j)
    assert seen==original and len(newclasses)==1753 and len(passclasses)==41
    assert not(newclasses&oldclasses) and set(remainingclasses)==set(range(8739))-newclasses-oldclasses
    remaining=original-old-new
    prior_open_domains={i for i,r in original-old}
    open_domains={i for i,r in remaining}
    assert len(remaining)==9393 and len(remainingclasses)==6985
    assert open_domains==prior_open_domains and len(open_domains)==1949
    assert (287,8) in new and (287,9) in new
    classkinds=Counter(classes[j]['kind'] for j in remainingclasses)
    treecounts=Counter(classes[j]['tree_index'] for j in remainingclasses)
    assert treecounts[410]==41
    data={'identity':'MINIMUM_K3_CENTRAL_FORCED_FACET_DELTA_V1',
      'input_pins':PINS,'prior_singleton_proof':'[internal-source-reference]',
      'analytic_proof':'[internal-source-reference]',
      'old_positions':sorted(old),'old_classes':sorted(oldclasses),
      'new_excluded_positions':sorted(new),'new_excluded_classes':sorted(newclasses),
      'central_passing_positions':[details[p] for p in sorted(passing)],
      'central_passing_classes':sorted(passclasses),
      'positions_remaining':len(remaining),'classes_remaining':len(remainingclasses),
      'open_domains':len(open_domains),'whole_excluded_domains':2307-len(open_domains),
      'new_whole_excluded_domains':[],
      'remaining_class_kinds':dict(sorted(classkinds.items())),
      'remaining_class_trees':dict(sorted(treecounts.items())),
      'position_histogram':dict(sorted(hist.items())),
      'actual_fan_triangles_checked':fans,
      'scope':'Only this literal K3 register delta. K2/global TREE410/C bounds unchanged. Passing is not feasibility.'}
    return enc(data)

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'central_k3_delta.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b,('OUTPUT',p.name)
    else:p.write_bytes(b)
    print('K3_CENTRAL_FACET_EXACT_DELTA_PASS',2349,1753,45,41,9393,6985,1949,358,*pin(b))
if __name__=='__main__':main()
