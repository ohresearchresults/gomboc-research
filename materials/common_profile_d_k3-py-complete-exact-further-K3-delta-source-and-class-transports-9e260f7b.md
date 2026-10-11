# material-9e260f7b6dd4

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact further K3 TREE585 delta for common-volume profile D.
python -S common_profile_d_k3.py build|check.
"""
from pathlib import Path
from itertools import combinations,permutations
import hashlib,json,sys
if not __debug__:raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent
PINS={
 'common_profile_c_k3.py':(9186,'a97b63ccc19bf76cf71dee4f24dcb46fbfe058f2abb4a014d7de23d1c5068aeb'),
 'common_profile_c_k3.json':(437927,'52ea6972118e05a23568a0570ba620dd218acf175391006e69875289bc2c5e91'),
 'common_profile_d.py':(10944,'39645ab603eb042278e64b130fb60a3435b291e43f9b464a1768a9a4c8c6ee71'),
}
def pin(b):return(len(b),hashlib.sha256(b).hexdigest())
for n,want in PINS.items():assert pin((HERE/n).read_bytes())==want
import common_profile_c_k3 as K
import common_profile_d as D

def build():
    prev=json.loads((HERE/'common_profile_c_k3.json').read_text());assert prev['identity']=='COMMON_PROFILE_C_K3_DELTA_V1'
    data=json.loads((HERE/'k3_domains.json').read_text());rows=data['rows']
    prior=list(map(tuple,prev['remaining']));assert len(prior)==251
    good={tuple(r['triangle']) for r in D.certificates()};assert len(good)==82
    lookup={tuple(t['target']):t['class_index'] for t in prev['transports']}
    assert {lookup[k] for k in prior}==set(prev['remaining_classes'])
    removed=[];remaining=[];witnesses=[];paths={}
    for i,r in prior:
        row=rows[i];path=K.path_order(row,r);paths[i,r]=path;inv={v:j for j,v in enumerate(path)}
        faces=[tuple(inv[v] for v in f) for f in row['facet_cycles'] if r not in f]
        tris=[K.triangulate(f,good) for f in faces]
        if all(t is not None for t in tris):
            removed.append((i,r))
            witnesses.append({'k3_index':i,'root':r,'class_index':lookup[i,r],'path':path,
                              'facets':[{'cycle':f,'triangles':t} for f,t in zip(faces,tris)]})
        else:remaining.append((i,r))
    gone={lookup[k] for k in removed};left={lookup[k] for k in remaining};assert not gone&left
    assert len(removed)==169 and len(remaining)==82
    prior_set=set(prior);removed_set=set(removed);transports=[]
    for t in prev['transports']:
        target=tuple(t['target'])
        if target not in prior_set:continue
        source=tuple(t['source']);assert source in prior_set
        i,r=source;j,s=target;p=t['vertex_map'];assert p[r]==s
        fm,o=K.transport_check(rows[i],rows[j],p)
        assert fm==t['facet_map'] and o==t['orientation']
        assert tuple(p[v] for v in paths[source])==paths[target]
        assert (source in removed_set)==(target in removed_set)
        transports.append(t)
    assert len(transports)==251
    blocked=[];total=0
    for size in range(3,10):
        for vs in combinations([i for i in range(10) if i!=3],size):
            forced={K.C.edge(a,a+1) for a in range(9) if a in vs and a+1 in vs}
            for tail in permutations(vs[1:]):
                if tail[0]>tail[-1]:continue
                f=(vs[0],)+tail
                edges={K.C.edge(v,f[(j+1)%size]) for j,v in enumerate(f)}
                if not forced<=edges:continue
                total+=1
                if K.triangulate(f,good) is None:blocked.append(f)
    assert total==1470 and blocked==[(0,8,9),(7,8,9),(0,7,8,9)]
    actual089=[];other=[]
    for i,r in remaining:
        facet=frozenset(paths[i,r][j] for j in (0,8,9))
        (actual089 if facet in {frozenset(f) for f in rows[i]['facet_cycles']} else other).append((i,r))
    assert len(actual089)==45 and len(other)==37
    summary={'prior_positions':251,'prior_classes':228,'newly_excluded_positions':169,
             'newly_excluded_classes':len(gone),'remaining_positions':82,'remaining_classes':len(left),
             'global_k3_remaining_positions':5871-169,'global_k3_remaining_classes':4316-len(gone),
             'actual_tetrahedra':sum(len(f['triangles']) for w in witnesses for f in w['facets']),
             'remaining_with_maximal_089':45,'remaining_without_maximal_089':37,
             'whole_domain_count':'not recomputed by this layer'}
    print('COMMON_PROFILE_D_K3_COUNTS',summary)
    return K.C.enc({'identity':'COMMON_PROFILE_D_K3_DELTA_V1','input_pins':PINS,'summary':summary,
                    'prior':prior,'removed':removed,'remaining':remaining,'removed_classes':sorted(gone),
                    'remaining_classes':sorted(left),'witnesses':witnesses,'transports':transports,
                    'blocked_facet_cycles':blocked,'actual089_remaining':actual089,'other_remaining':other,
                    'scope':'Further exact literal TREE585 positions and whole true rooted facet/tree classes. No complete E17 exclusion or exact minimum.'})
def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'common_profile_d_k3.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('COMMON_PROFILE_D_K3_EXACT_DELTA_PASS',*pin(b))
if __name__=='__main__':main()
