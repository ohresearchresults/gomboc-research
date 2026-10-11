# material-a97b63ccc19b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact K3 TREE585 delta for COMMON_VOLUME_PROJECTION_PROFILE_C_V1.
python -S common_profile_c_k3.py build|check; standard library only.
"""
from collections import Counter,deque
from functools import lru_cache
from itertools import combinations,permutations
from pathlib import Path
import hashlib,json,sys
if not __debug__:raise RuntimeError('Assertions must be enabled')
HERE=Path(__file__).resolve().parent
PINS={
 'k3_census.py':(13141,'9d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a'),
 'k3_domains.json':(2724409,'f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6'),
 'common_profile_c.py':(10718,'d7069f70083d752f16268d7d3b06998f9c0e28398e45567c22dbcb05ccdcbbe1'),
}
def pin(b):return (len(b),hashlib.sha256(b).hexdigest())
for name,want in PINS.items():assert pin((HERE/name).read_bytes())==want
import k3_census as C
import common_profile_c as Q
OLD_BAD={(0,7,9),(0,8,9),(1,8,9),(7,8,9)}
ALL_TRI=set(combinations([i for i in range(10) if i!=3],3))
OLD_GOOD=ALL_TRI-OLD_BAD
NEW_GOOD={tuple(row['triangle']) for row in Q.certificates()}
assert len(OLD_GOOD)==80 and len(NEW_GOOD)==78

def canonical(row,root):
    rot=C.rotations(row['facet_cycles']);marked=frozenset(map(tuple,row['tree_edges']))
    return min(C.rooted_code(rot,root,v,s,marked) for v in rot[root] for s in (1,-1))

def path_order(row,r):
    adj=[[] for _ in range(10)]
    for a,b in row['tree_edges']:adj[a].append(b);adj[b].append(a)
    leaves=[i for i in range(10) if len(adj[i])==1]
    assert len(leaves)==2 and all(1<=len(x)<=2 for x in adj)
    p=[-1]*10;p[r]=r;todo=deque([r])
    while todo:
        v=todo.popleft()
        for w in adj[v]:
            if p[w]<0:p[w]=v;todo.append(w)
    assert min(p)>=0
    chains=[]
    for leaf in leaves:
        chain=[leaf]
        while chain[-1]!=r:chain.append(p[chain[-1]])
        chains.append(chain)
    short,long=sorted(chains,key=len)
    path=tuple(short+long[-2::-1])
    assert len(path)==len(set(path))==10 and path[3]==r and len(short)==4 and len(long)==7
    assert {C.edge(a,b) for a,b in zip(path,path[1:])}==set(map(tuple,row['tree_edges']))
    assert set(map(tuple,row['tree_edges']))<=set(map(tuple,row['edges']))
    return path

def triangulate(face,good):
    face=tuple(face)
    @lru_cache(None)
    def rec(i,j):
        if j-i<2:return ()
        for k in range(i+1,j):
            t=tuple(sorted((face[i],face[k],face[j])))
            if t not in good:continue
            a,b=rec(i,k),rec(k,j)
            if a is not None and b is not None:return a+b+(t,)
        return None
    result=rec(0,len(face)-1)
    if result is not None:
        assert len(result)==len(face)-2
        boundary={C.edge(v,face[(j+1)%len(face)]) for j,v in enumerate(face)}
        counts=Counter(C.edge(v,t[(i+1)%3]) for t in result for i,v in enumerate(t))
        assert {e for e,n in counts.items() if n==1}==boundary
        assert all(n==(1 if e in boundary else 2) for e,n in counts.items())
        pos={v:i for i,v in enumerate(face)}
        diagonals=[tuple(sorted((pos[a],pos[b]))) for (a,b),n in counts.items() if n==2]
        assert all(not(a<c<b<d or c<a<d<b) for (a,b),(c,d) in combinations(diagonals,2))
    return result

def old_block_family(face):
    s=set(face)
    return (s=={0,7,9} and len(face)==3) or ({8,9}<=s<={0,1,7,8,9} and C.edge(8,9) in {C.edge(v,face[(j+1)%len(face)]) for j,v in enumerate(face)})

def polygon_classification():
    oldbad=[];newbad=[];total=0
    for size in range(3,10):
        for vertices in combinations([i for i in range(10) if i!=3],size):
            # Genuine path edges with both ends in a facet must be boundary edges.
            forced={C.edge(a,a+1) for a in range(9) if a in vertices and a+1 in vertices}
            a=vertices[0]
            for tail in permutations(vertices[1:]):
                if tail[0]>tail[-1]:continue
                face=(a,)+tail
                edges={C.edge(v,face[(j+1)%size]) for j,v in enumerate(face)}
                if not forced<=edges:continue
                total+=1
                old=triangulate(face,OLD_GOOD) is None
                assert old==old_block_family(face)
                if old:oldbad.append(face)
                if triangulate(face,NEW_GOOD) is None:newbad.append(face)
    assert len(oldbad)==10
    return {'all_path_compatible_cycles':total,'old_blocked_cycles':oldbad,'new_blocked_cycles':newbad}

def transport_check(source,target,p):
    assert sorted(p)==list(range(10))
    assert {C.edge(p[a],p[b]) for a,b in source['edges']}==set(map(tuple,target['edges']))
    assert {C.edge(p[a],p[b]) for a,b in source['tree_edges']}==set(map(tuple,target['tree_edges']))
    dest={tuple(sorted(f)):i for i,f in enumerate(target['facet_cycles'])};fm=[];orient=[]
    for f in source['facet_cycles']:
        image=tuple(p[v] for v in f);i=dest[tuple(sorted(image))];fm.append(i)
        if C.cyc(image)==C.cyc(target['facet_cycles'][i]):orient.append(1)
        else:assert C.cyc(image)==C.cyc(tuple(reversed(target['facet_cycles'][i])));orient.append(-1)
    assert sorted(fm)==list(range(9)) and len(set(orient))==1
    assert all(sorted(fm[f] for f in inc)==target['incidence'][p[v]] for v,inc in enumerate(source['incidence']))
    return fm,orient[0]

def build():
    data=json.loads((HERE/'k3_domains.json').read_text());rows=data['rows']
    assert data['identity']=='MINIMUM_TREE253_K3_LITERAL_DOMAINS_V1' and len(rows)==2307
    groups={}
    for row in rows:
        for q in row['roots']:
            if q['status']=='open':
                key,labels=canonical(row,q['vertex'])
                groups.setdefault(key,[]).append((row['k3_index'],q['vertex'],labels))
    groups=sorted(groups.values(),key=lambda g:min((i,r) for i,r,_ in g))
    assert len(groups)==8739 and sum(map(len,groups))==11743
    cindex={(i,r):ci for ci,group in enumerate(groups) for i,r,_ in group}
    prior=[];removed=[];remaining=[];witnesses=[];paths={}
    for row in rows:
        for q in row['roots']:
            if q['status']!='open' or q['tree_index']!=585:continue
            r=q['vertex'];key=(row['k3_index'],r);path=path_order(row,r);paths[key]=path
            inv={v:i for i,v in enumerate(path)}
            faces=[tuple(inv[v] for v in f) for f in row['facet_cycles'] if r not in f]
            blocked=[f for f in faces if triangulate(f,OLD_GOOD) is None]
            assert all(old_block_family(f) for f in blocked)
            if not blocked:continue
            prior.append(key)
            tris=[triangulate(f,NEW_GOOD) for f in faces]
            if all(t is not None for t in tris):
                removed.append(key)
                witnesses.append({'k3_index':key[0],'root':r,'class_index':cindex[key],
                                  'path':path,'facets':[{'cycle':f,'triangles':t} for f,t in zip(faces,tris)]})
            else:remaining.append(key)
    oldclasses=sorted({cindex[k] for k in prior});newclasses=sorted({cindex[k] for k in removed});leftclasses=sorted({cindex[k] for k in remaining})
    assert len(prior)==1039 and len(oldclasses)==729
    assert len(removed)==788 and len(remaining)==251
    assert not set(newclasses)&set(leftclasses)
    transports=[]
    for ci in oldclasses:
        group=sorted(groups[ci]);i,r,a=group[0];source=rows[i]
        assert (i,r) in paths
        for j,s,b in group:
            inv={v:k for k,v in enumerate(b)};p=[inv[v] for v in a]
            assert p[r]==s
            fm,o=transport_check(source,rows[j],p)
            assert tuple(p[v] for v in paths[i,r])==paths[j,s]
            assert ((i,r) in removed)==((j,s) in removed)
            transports.append({'class_index':ci,'source':(i,r),'target':(j,s),'vertex_map':p,'facet_map':fm,'orientation':o})
    summary={'prior_positions':len(prior),'prior_classes':len(oldclasses),
             'newly_excluded_positions':len(removed),'newly_excluded_classes':len(newclasses),
             'remaining_positions':len(remaining),'remaining_classes':len(leftclasses),
             'global_k3_remaining_positions':6659-len(removed),'global_k3_remaining_classes':4817-len(newclasses),
             'census_domain_count':2307,'new_whole_domain_count':'not recomputed by this layer',
             'actual_tetrahedra':sum(len(f['triangles']) for w in witnesses for f in w['facets'])}
    print('COMMON_PROFILE_C_K3_COUNTS',summary)
    return C.enc({'identity':'COMMON_PROFILE_C_K3_DELTA_V1','input_pins':PINS,
                  'summary':summary,'prior':prior,'removed':removed,'remaining':remaining,
                  'newly_excluded_classes':newclasses,'remaining_classes':leftclasses,
                  'witnesses':witnesses,'transports':transports,'polygon_classification':polygon_classification(),
                  'scope':'Literal TREE585 positions and whole genuine rooted facet/tree classes only. No unmarked type count, C>=36 or exact minimum is asserted.'})

def main():
    assert sys.argv[1:] in (['build'],['check'])
    b=build();p=HERE/'common_profile_c_k3.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('COMMON_PROFILE_C_K3_EXACT_DELTA_PASS',*pin(b))
if __name__=='__main__':main()
