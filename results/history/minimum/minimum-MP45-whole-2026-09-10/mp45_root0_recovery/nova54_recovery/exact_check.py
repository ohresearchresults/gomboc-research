"""Independent exact proof checker. No numerical imports or locator imports.
Scalar polynomial expansion, integer Bareiss and rational LDL are separate.
Combinatorial coverage uses parent choices, not the locator's edge subsets.
"""
import collections,hashlib,itertools,json,multiprocessing,sys
from fractions import Fraction as F
from pathlib import Path
import comb
assert __debug__
NAME='NOVA54_MP9_ACTUAL_MOMENTS_V1'
UNKNOWN=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,34,35,36,37,38,39]
G=None

def fan(fs,a):
    assert 0<=a<9
    return [(a,)+tuple(f)for f in fs if a not in f]

def rankmod(rows,prime=65521):
    a=[[v%prime for v in row]for row in rows]
    if not a:return 0
    r=0
    for j in range(len(a[0])):
        k=next((i for i in range(r,len(a))if a[i][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];u=pow(a[r][j],-1,prime)
        a[r]=[(u*v)%prime for v in a[r]]
        for i in range(r+1,len(a)):
            if a[i][j]:
                u=a[i][j];a[i]=[(v-u*w)%prime for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def verify_relations(fs,spec,cells,relations):
    sig={}
    for a,s in spec:
        assert s==0
        for t in fan(fs,a):
            v=(-1)**sum(t[i]>t[j]for i in range(4)for j in range(i+1,4))
            key=tuple(sorted(t));assert key not in sig or sig[key]==v;sig[key]=v
    assert set(sig)==set(cells)
    triples=list(itertools.combinations(range(9),3));ti={t:i for i,t in enumerate(triples)}
    R=[[0]*len(cells)for _ in triples]
    for j,t in enumerate(cells):
        for k in range(4):R[ti[t[:k]+t[k+1:]]][j]=sig[t]*(-1)**k
    assert rankmod(relations)==len(relations)
    assert rankmod(R)+len(relations)==len(cells)
    for row in relations:
        assert len(row)==len(cells) and all(type(x)is int for x in row)
        boundary=collections.Counter()
        for t,w in zip(cells,row):
            for k in range(4):boundary[t[:k]+t[k+1:]]+=w*sig[t]*(-1)**k
        assert not any(boundary.values()),'INVALID_AFFINE_VOLUME_RELATION'

def scalar_matrices(rec,fs=None,generic=False):
    p=rec['parent'];r=rec['root'];z=rec['z'];kind=rec['kind']
    spec=rec['fans'];A=len(spec);norm=rec.get('comparisons',[])
    assert kind in('ordinary','shared','volume','cycle')
    assert type(r)is int and p[r]==r and len(p)==9
    assert all(type(x)is int for x in z)
    assert len({tuple(s)for s in spec})==len(spec)
    if generic:
        assert r==0 and spec==[[0,0]] and kind=='ordinary' and not norm
        ff=[[(0,)+t for t in itertools.combinations(range(1,9),3)]]
    else:
        assert all(type(a)is int and 0<=a<9 and s==0 for a,s in spec)
        ff=[fan(fs,a)for a,s in spec]
    if norm:
        o=rec['order'];assert o in comb.norm_orders(p)
        assert norm==comb.comparisons(p,o)
    shared=kind!='ordinary';cycle=kind=='cycle';volume=kind in('volume','cycle')
    if shared:
        cells=sorted({tuple(sorted(t))for f in ff for t in f})
        fi=[[int(t in {tuple(sorted(t0))for t0 in f})for t in cells]for f in ff]
        inst=[(None,t)for t in cells]
        if cycle:
            assert spec==[[a,0]for a in range(9)]
            fi=[fi[r]]+rec['relations'];A=len(fi)
    else:inst=[(a,t)for a,f in enumerate(ff)for t in f]
    k=len(inst);m=8+len(norm);start=9*A;end=start+m*k
    if volume:
        assert not norm
        rel=rec['relations'];verify_relations(fs,spec,cells,rel);nr=len(rel)
    else:nr=A-1
    assert len(z)==end+45*nr+((A-1)if shared else 0)
    assert min(z[start:end])>=0
    nodes=[i for i in range(9)if i!=r]
    for u,(a,t)in enumerate(inst):
        poly=collections.defaultdict(int)
        def add(i,j,x):poly[min(i,j),max(i,j)]+=x
        ga=[sum(fi[b][u]*z[9*b+i]for b in range(A))for i in range(9)]if shared else z[9*a:9*a+9]
        for i in range(9):
            for j in t:add(i,j,2*ga[i])
        ls=z[start+m*u:start+m*(u+1)]
        for i,w in zip(nodes,ls[:8]):add(i,i,2*w);add(i,p[i],-2*w)
        for (i,j),w in zip(norm,ls[8:]):add(i,i,2*w);add(j,j,-2*w)
        for b in range(nr):
            h=rel[b][u]if volume else((fi[b][u]-fi[-1][u])if shared else int(a==b)-int(a==A-1))
            at=end+45*b
            for i in range(9):
                for j in range(i,9):add(i,j,2*h*z[at]);at+=1
        if shared:
            eta=z[end+45*nr:]
            q=sum(eta[b]*rel[b][u]for b in range(nr))if cycle else sum(eta[b]*(fi[b][u]-fi[-1][u])for b in range(A-1))
            for i in t:
                for j in t:add(i,j,2*q)
                add(i,i,2*q)
        Q=[[0]*9 for _ in range(9)]
        for (i,j),v in poly.items():
            if i==j:Q[i][j]=v
            else:assert v%2==0;Q[i][j]=Q[j][i]=v//2
        yield Q

def bareiss(Q):
    A=[r[:]for r in Q];prev=1;out=[]
    for i in range(9):A[i][i]-=1
    for k in range(9):
        d=A[k][k];assert type(d)is int and d>0,('NOT_UNIT_PD',k,d)
        out.append(d)
        for i in range(k+1,9):
            for j in range(i,9):
                v=d*A[i][j]-A[i][k]*A[k][j];assert v%prev==0
                A[i][j]=A[j][i]=v//prev
        prev=d
    return out

def ldl(Q):
    A=[[F(x-int(i==j))for j,x in enumerate(row)]for i,row in enumerate(Q)]
    prod=F(1);out=[]
    for k in range(9):
        d=A[k][k];assert d>0;prod*=d;assert prod.denominator==1;out.append(int(prod))
        for i in range(k+1,9):
            for j in range(i,9):A[i][j]=A[j][i]=A[i][j]-A[i][k]*A[j][k]/d
    return out

def checked(rec,fs=None,generic=False):
    h=hashlib.sha256();n=0
    for Q in scalar_matrices(rec,fs,generic):
        b=bareiss(Q);assert b==ldl(Q)
        h.update(comb.encoded([Q,b]));n+=1
    return n,h.hexdigest()

ACTUAL={};GENERIC={};SHAPES=[];GOOD=set()

def check_root(task):
    gi,r=task;g=G[gi];pp=comb.parent_trees(g,r)
    counts=collections.Counter();h=hashlib.sha256();front=bytearray();matrix_count=0;cert_count=0
    partial=[]
    for ix,p in enumerate(pp):
        key=(gi,r,ix)
        if comb.safe(p,r,g['facets']):counts['depth']+=1;assert key not in ACTUAL;continue
        if comb.code(p,r)in GOOD:counts['generic']+=1;assert key not in ACTUAL;continue
        row=ACTUAL.get(key)
        closed=False
        if row is not None:
            assert row['parent']==list(p)
            cases=row['cases'];assert cases
            seen=set()
            for rec in cases:
                assert rec['parent']==list(p) and rec['root']==r
                order=tuple(rec['order'])if 'order'in rec else None
                assert order not in seen;seen.add(order)
                n,hh=checked(rec,g['facets']);matrix_count+=n;cert_count+=1
                h.update(comb.encoded([ix,order,n,hh]))
            if None in seen:assert len(seen)==1;closed=True
            else:
                allorders={tuple(o)for o in comb.norm_orders(p)}
                assert seen<=allorders;closed=seen==allorders
                if not closed:partial.append([ix,[list(o)for o in sorted(allorders-seen)]])
        if closed:counts['actual']+=1
        else:counts['remaining']+=1;front.extend(bytes([gi,r]+list(p)))
    assert sum(counts.values())==len(pp)
    orbit={a[r]for a in g['aut']}
    out=dict(graph=gi,root=r,degree=sum(r in e for e in g['edges']),root_orbit=sorted(orbit),
             tree_orbits=len(pp),labeled_trees_per_root=g['trees'],counts=dict(counts),
             actual_certificates=cert_count,integer_matrices=matrix_count,scalar_minor_stream_sha256=h.hexdigest(),
             partial_orders=partial)
    return out,bytes(front)

def volume_structure():
    fs=G[48]['facets'];ff=[fan(fs,a)for a in range(9)]
    cells=sorted({tuple(sorted(t))for f in ff for t in f})
    triples=list(itertools.combinations(range(9),3));ti={t:i for i,t in enumerate(triples)};sig={}
    for f in ff:
        for t in f:
            sg=(-1)**sum(t[i]>t[j]for i in range(4)for j in range(i+1,4))
            key=tuple(sorted(t));assert key not in sig or sig[key]==sg;sig[key]=sg
    R=[[0]*len(cells)for _ in triples]
    for j,t in enumerate(cells):
        for k in range(4):R[ti[t[:k]+t[k+1:]]][j]=sig[t]*(-1)**k
    ft=[[int(t in{tuple(sorted(u))for u in f})for t in cells]for f in ff]
    old=[[v-w for v,w in zip(row,ft[-1])]for row in ft[:-1]]
    terms={'0126':1,'0127':-1,'0146':1,'0147':-1,'0267':1,'0467':1,'1267':-1,'1467':-1}
    beta=[terms.get(''.join(map(str,t)),0)for t in cells]
    assert len(cells)==63 and rankmod(R)==49 and rankmod(old)==7
    assert not any(sum(v*w for v,w in zip(row,beta))for row in R)
    assert rankmod(old+[beta])==8
    row=ACTUAL[48,0,2764];rec=row['cases'][0]
    assert rec['kind']=='volume' and rec['parent']==[0,0,0,8,7,1,5,6,4]
    assert rec['fans']==[[a,0]for a in [0,1,7,6,5,3,8,2]]
    assert len(rec['z'])==1213 and len(rec['relations'])==14
    verify_relations(fs,rec['fans'],cells,rec['relations'])
    return dict(tetrahedra=63,boundary_rank=49,kernel_dimension=14,fan_difference_rank=7,
                extra_relations=7,literal_relation=terms,last_tree=[0,0,0,8,7,1,5,6,4],
                last_tree_apices=[0,1,7,6,5,3,8,2],last_tree_coefficients=1213,
                last_tree_record=comb.pin(comb.encoded(rec)))

def main():
    global G,ACTUAL,GENERIC,SHAPES,GOOD
    comb.verify_caps();G=comb.catalogue(True);SHAPES=comb.shapes()
    assert len(G)==50 and sum(len(g['roots'])for g in G)==328
    Path('mp9.json').write_bytes(comb.encoded(G))
    gb=Path('generic.jsonl').read_bytes();ab=Path('actual.jsonl').read_bytes();ck=json.loads(Path('checkpoint.json').read_bytes())
    assert comb.pin(gb)==ck['generic']and comb.pin(ab)==ck['actual']
    xs=[json.loads(l)for l in gb.splitlines()];seen=set();GH=hashlib.sha256();gn=0
    for x in xs:
        i=x['shape'];assert i not in seen;seen.add(i);p=SHAPES[i]
        rec=x['record'];assert rec['parent']==list(p)
        n,hh=checked(rec,generic=True);gn+=n;GH.update(comb.encoded([i,n,hh]))
    depth={i for i,p in enumerate(SHAPES)if comb.generic_safe(p)}
    assert len(depth)==172 and len(seen)==87 and not depth&seen
    assert sorted(set(range(286))-depth-seen)==UNKNOWN
    GOOD={comb.code(SHAPES[i])for i in depth|seen}
    print('NOVA54_GENERIC_259_OF_286_PASS',gn,flush=True)
    rows=[json.loads(l)for l in ab.splitlines()]
    for x in rows:
        key=x['graph'],x['root'],x['index'];assert key not in ACTUAL;ACTUAL[key]=x
        g=G[x['graph']];assert x['root']in g['roots']
    tasks=[(g['id'],r)for g in G for r in g['roots']]
    results=[];total=collections.Counter();fn=0
    with Path('frontier.bin').open('wb')as f,multiprocessing.get_context('fork').Pool(4)as pool:
        for out,front in pool.imap(check_root,tasks,chunksize=1):
            f.write(front);fn+=len(front);results.append(out);total.update(out['counts'])
    # Every certificate must have been matched to a complete enumerated root/tree.
    assert sum(x['counts'].get('actual',0)+len(x['partial_orders'])for x in results)==len(ACTUAL)
    assert sum(total.values())==8116253
    assert total['depth']==4322310 and total['generic']==2677681
    closed=[(x['graph'],x['root'])for x in results if x['counts'].get('remaining',0)==0]
    degree8=[(x['graph'],x['root'])for x in results if x['degree']==8]
    assert len(degree8)==12
    assert set(degree8)<set(closed) and (48,0)in closed and(48,2)in closed
    assert sorted(map(list,closed))==sorted(ck['closed_roots'])and len(closed)>=14
    assert total['remaining']==ck['remaining']and total['actual']==ck['actual_trees']
    assert fn==11*total['remaining']
    whole=[g['id']for g in G if all((g['id'],r)in closed for r in g['roots'])]
    assert 48 in whole
    frontier=Path('frontier.bin').read_bytes()
    structure=volume_structure()
    methods=dict(collections.Counter(rec['kind']for row in rows for rec in row['cases']))
    report=dict(identity=NAME,source_parent=['asg_VOkJgQeJI85JsScj0zkUI191','3b737649ca4e531383c349e6a3e088fdf458b5b826662c391f655f628f843a94'],
        graph_catalogue=comb.pin(comb.encoded(G)),generic_input=comb.pin(gb),actual_input=comb.pin(ab),
        generic_shapes=259,generic_remaining_shapes=UNKNOWN,generic_matrices=gn,generic_scalar_minor_stream_sha256=GH.hexdigest(),
        total_tree_orbits=sum(total.values()),counts=dict(total),closed_roots=closed,whole_graphs=whole,
        all_degree_eight_roots=degree8,frontier=comb.pin(frontier),frontier_record_width=11,
        root_reports=results,actual_method_counts=methods,volume_structure=structure,integer_matrices=gn+sum(x['integer_matrices']for x in results),
        leading_minors=9*(gn+sum(x['integer_matrices']for x in results)),
        universal_V10_established=False,global_bracket=[32,1374],vertex_bound=9,facet_bound=9)
    raw=comb.encoded(report);Path('report.json').write_bytes(raw)
    print('NOVA54_MP9_50_GRAPHS_328_ROOTS_PASS')
    print('NOVA54_ALL_ROOT_TREE_CASES',sum(total.values()),dict(total))
    print('NOVA54_WHOLE_MP9_GRAPHS',whole)
    print('NOVA54_WHOLE_MP9_48_PASS')
    print('NOVA54_AFFINE_VOLUME_CYCLE_63_49_14_VS_7_PASS')
    print('NOVA54_ALL_TWELVE_DEGREE8_ROOTS_PASS')
    print('NOVA54_REPORT',*comb.pin(raw))
    print('NOVA54_STANDARD_LIBRARY_INDEPENDENT_CHECK_PASS')
if __name__=='__main__':main()
