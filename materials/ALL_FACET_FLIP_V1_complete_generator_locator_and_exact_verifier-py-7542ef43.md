# material-7542ef43f2e0

AI research material

---

"""Complete local-flip compression of actual tetrahedral moment identities.
Input native55.txt is the unchanged 2630-byte literal incidence catalogue.
Commands: python -S flip_moments.py census
          python flip_moments.py locate INDEX ROOT
          python -S flip_moments.py check RECORD.json
No floating point is used by census or check. Unknown numerical outcome is
not geometric feasibility or impossibility. Exact accepted data must be
persisted before a successful candidate changes research coverage.
"""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json,sys,os
assert __debug__
HERE=Path(__file__).resolve().parent
N=10
DUAL={(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(0,7),(7,8)}
INPUT_PIN=[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e']
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(x):return [len(x),hashlib.sha256(x).hexdigest()]
def inputs():
    b=(HERE/'native55.txt').read_bytes();assert pin(b)==INPUT_PIN
    d={int(l.split(':')[0]):l.split(':')[1].split() for l in b.decode().splitlines()}
    assert sorted(d)==list(range(55));return d

def geometry(row):
    inc=[set(map(int,s)) for s in row]
    assert len(inc)==N and len(set(map(tuple,map(sorted,inc))))==N
    edges=[(i,j) for i,j in combinations(range(N),2) if len(inc[i]&inc[j])==2]
    assert len(edges)==17
    pe=[(i,j) for i,j in edges if tuple(sorted(inc[i]&inc[j])) not in DUAL]
    ad={i:[] for i in range(N)}
    for i,j in pe:ad[i].append(j);ad[j].append(i)
    ends=sorted(i for i in ad if len(ad[i])==1)
    assert len(pe)==9 and len(ends)==2 and all(len(ad[i])==2 for i in ad if i not in ends)
    path=[ends[0]]
    while len(path)<N:
        c=[j for j in ad[path[-1]] if j not in path];assert len(c)==1;path+=c
    assert path[-1]==ends[1]
    inv={v:i for i,v in enumerate(path)};faces=[]
    for a in range(9):
        vs=[i for i in range(N) if a in inc[i]]
        adj={i:sorted(j for j in vs if tuple(sorted((i,j))) in edges) for i in vs}
        assert all(len(v)==2 for v in adj.values())
        cy=[min(vs)]
        while len(cy)<len(vs):
            c=[j for j in adj[cy[-1]] if j not in cy];assert c;cy.append(c[0])
        assert cy[0] in adj[cy[-1]]
        faces.append([inv[v] for v in cy])
    fe={}
    for a,cy in enumerate(faces):
        for i,v in enumerate(cy):fe.setdefault(tuple(sorted((path[v],path[cy[(i+1)%len(cy)]]))),[]).append(a)
    assert sorted(fe)==edges and all(set(a)==inc[i]&inc[j] for (i,j),a in fe.items())
    return path,edges,faces

@lru_cache(None)
def triangulations(poly):
    if len(poly)<3:return ((),)
    ans=[]
    for j in range(1,len(poly)-1):
        for a,b in product(triangulations(poly[:j+1]),triangulations(poly[j:])):
            ans.append(tuple(sorted(a+b+(tuple(sorted((poly[0],poly[j],poly[-1]))),))))
    assert len(ans)==len(set(ans));return tuple(ans)

def add_sparse(*vs):
    d={}
    for v in vs:
        for k,x in v.items():d[k]=d.get(k,0)+x
    return {k:v for k,v in d.items() if v}
def neg(v):return {k:-x for k,x in v.items()}
def tri_fan(cy):return [tuple(sorted((cy[0],cy[j],cy[j+1]))) for j in range(1,len(cy)-1)]
def quad(cy,q):
    a,b,c,d=[cy[i] for i in q]
    return {tuple(sorted(t)):s for t,s in [((a,b,c),1),((a,c,d),1),((a,b,d),-1),((b,c,d),-1)]}
def lift(ap,tri):return {tuple(sorted((ap,)+t)):s for t,s in tri.items()}

def independent(rows):
    piv={};selected=[]
    for row in rows:
        d={k:F(v) for k,v in row.items()}
        while d:
            p=min(d)
            if p not in piv:
                scale=d[p];piv[p]={k:v/scale for k,v in d.items()};selected.append(row);break
            s=d[p];d=add_sparse(d,{k:-s*v for k,v in piv[p].items()})
    return selected

def system(row):
    path,edges,faces=geometry(row);fans=[];raw=[];labels=[]
    for a in range(N):
        fan={}
        for fi,cy in enumerate(faces):
            if a in cy:continue
            fan=add_sparse(fan,lift(a,{t:1 for t in tri_fan(cy)}))
            for triple in combinations(range(1,len(cy)),3):
                raw.append(lift(a,quad(cy,(0,)+triple)));labels.append(['flip',a,fi,list(triple)])
        assert all(v==1 for v in fan.values());fans.append(fan)
    relations=[add_sparse(f,neg(fans[0])) for f in fans[1:]]+raw
    basis=independent(relations)
    cells=sorted(set().union(*(set(f) for f in fans),*(set(f) for f in raw)))
    assert independent(basis+[fans[0]])==basis+[fans[0]]
    for rel in relations:assert len(independent(basis+[rel]))==len(basis)
    return dict(path=path,edges=edges,faces=faces,cells=cells,reference=fans[0],basis=basis,
                raw_relations=len(relations),local_relations=len(raw),whole_fans=fans)

def boundary(tris):
    d={}
    for (a,b,c),s in tris.items():d=add_sparse(d,{(b,c):s,(a,c):-s,(a,b):s})
    return d

def polygon_audit(m):
    cy=list(range(m));ts=triangulations(tuple(cy));base={t:1 for t in tri_fan(cy)}
    qs=[quad(cy,(0,)+s) for s in combinations(range(1,m),3)]
    for q in qs:assert not boundary(q)
    for tr in ts:
        delta=add_sparse({t:1 for t in tr},neg(base))
        assert not boundary(delta)
        reconstructed={}
        for s in combinations(range(1,m),3):
            c=-delta.get(s,0)
            reconstructed=add_sparse(reconstructed,{k:c*v for k,v in quad(cy,(0,)+s).items()})
        assert delta==reconstructed
    dim=len(independent(qs));assert dim==len(qs)
    assert len(independent([add_sparse({t:1 for t in tr},neg(base)) for tr in ts]))==dim
    return dict(vertices=m,triangulations=len(ts),flip_basis_rank=dim)

def description(d):
    return {'path':d['path'],'edges':d['edges'],'faces':d['faces'],'cells':d['cells'],
            'reference':[[list(t),v] for t,v in sorted(d['reference'].items())],
            'basis':[[[list(t),v] for t,v in sorted(h.items())] for h in d['basis']]}

def census():
    report={'identity':'TREE253_K2_ALL_FACET_TRIANGULATION_SPAN_V1','input_pin':INPUT_PIN,
            'polygons':[polygon_audit(m) for m in range(3,8)],'rows':[]}
    for i,row in inputs().items():
        d=system(row)
        report['rows'].append({'native_index':i,'facet_sizes':list(map(len,d['faces'])),
            'cells':len(d['cells']),'raw_relations':d['raw_relations'],
            'independent_volume_relations':len(d['basis']),
            'system_pin':pin(enc(description(d)))})
    b=enc(report);(HERE/'flip_census.json').write_bytes(b)
    print('ALL_FACET_TRIANGULATIONS_EXACT_SPAN_PASS',55,*pin(b));return report

def pencil(row,root):
    import numpy as np
    from scipy.sparse import coo_matrix
    d=system(row);cells=d['cells'];ci={t:i for i,t in enumerate(cells)}
    R=[];C=[];V=[];bounds=[]
    def col(entries,positive=False):
        p=len(bounds);bounds.append((0,1) if positive else(-1,1))
        for t,i,j,v in entries:
            if v:R.append(ci[t]*N*N+i*N+j);C.append(p);V.append(v)
    # First moment at the reference fan; all other moments are differences.
    for h in [d['reference']]+d['basis']:
        for i in range(N):
            ent=[]
            for t,s in h.items():
                for j in t:ent.extend([(t,i,j,s),(t,j,i,s)])
            col(ent)
    for h in d['basis']:
        for i in range(N):
            for j in range(i,N):
                ent=[(t,i,j,s) for t,s in h.items()]
                if i!=j:ent +=[(t,j,i,s) for t,s in h.items()]
                col(ent)
        col([(t,i,j,s*(1+(i==j))) for t,s in h.items() for i in t for j in t])
    free=len(bounds)
    for t in cells:
        for i in range(N):
            if i==root:continue
            p=i+1 if i<root else i-1
            col([(t,i,i,2),(t,i,p,-1),(t,p,i,-1)],True)
    A=coo_matrix((V,(R,C)),shape=(len(cells)*N*N,len(bounds))).tocsr()
    return d,A,bounds,free

def locate(index,root):
    os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
    import numpy as np
    from scipy.optimize import minimize
    from scipy.special import logsumexp
    import platform,scipy,time
    row=inputs()[index];assert 1<=root<=8
    d,A,bounds,free=pencil(row,root);n=len(d['cells']);x=np.zeros(A.shape[1]);history=[]
    print('PENCIL',index,root,n,len(d['basis']),A.shape,A.nnz,flush=True)
    start=time.time()
    for tau in (0.1,0.03,0.01,0.003,0.001,0.0003,0.0001,0.00003):
        def objective(x):
            mat=(A@x).reshape(n,N,N);lam,U=np.linalg.eigh(mat)
            z=-lam/tau;lse=logsumexp(z);weights=np.exp(z-lse)
            gradmat=np.einsum('bik,bk,bjk->bij',U,weights,U)
            return tau*lse, -A.T@gradmat.ravel()
        r=minimize(objective,x,method='L-BFGS-B',jac=True,bounds=bounds,
                   options=dict(maxiter=2500,maxcor=30,ftol=1e-15,gtol=1e-10,maxls=40))
        x=r.x;lam=float(np.linalg.eigvalsh((A@x).reshape(n,N,N)).min())
        history.append(dict(tau=tau,minimum=lam,iterations=r.nit,status=int(r.status)))
        print('STAGE',index,root,tau,lam,r.nit,'elapsed',round(time.time()-start,1),flush=True)
        proposal={'identity':'FLIP_MOMENT_NUMERICAL_PROPOSAL_V1','native_index':index,'root':root,
                  'coefficients':x.tolist(),'history':history,'system_pin':pin(enc(description(d))),
                  'environment':[platform.python_version(),np.__version__,scipy.__version__]}
        (HERE/f'proposal_{index}_{root}.json').write_bytes(enc(proposal))
        if lam>1e-5:break
    for power in (12,14,16,18,20,24):
        scaled=np.rint(x*2**power);assert np.max(np.abs(scaled))<2**62
        record={'identity':'TREE253_K2_ALL_FACET_FLIP_CERTIFICATE_V1','native_index':index,'root':root,
                'system_pin':pin(enc(description(d))),'rounding_power':power,
                'coefficients':scaled.astype(np.int64).tolist()}
        try:report=check(record)
        except (AssertionError,ZeroDivisionError):continue
        p=HERE/f'certificate_{index}_{root}.json';p.write_bytes(enc(record))
        (HERE/f'exact_{index}_{root}.json').write_bytes(enc(report))
        print('EXACT_PASS_EPHEMERAL_NOT_YET_PERSISTED',index,root,power,report['cells'],*pin(p.read_bytes()),flush=True)
        return True
    print('UNKNOWN_NO_EXACT_CERTIFICATE',index,root,flush=True);return False

def bareiss(A):
    a=[row[:] for row in A];previous=1;minors=[]
    for k in range(len(a)):
        pivot=a[k][k];assert pivot>0,(k,pivot);minors.append(pivot)
        if k==len(a)-1:break
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                val=a[i][j]*pivot-a[i][k]*a[k][j];assert val%previous==0
                a[i][j]=val//previous
        previous=pivot
    return minors

def schur(A):
    a=[[F(v) for v in row] for row in A];pivots=[];prod=F(1);minors=[]
    for k in range(len(a)):
        p=a[k][k];assert p>0;pivots.append(p);prod*=p;assert prod.denominator==1;minors.append(int(prod))
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):a[i][j]-=a[i][k]*a[k][j]/p
    return pivots,minors

def check(record):
    assert record['identity']=='TREE253_K2_ALL_FACET_FLIP_CERTIFICATE_V1'
    index=record['native_index'];root=record['root'];assert 1<=root<=8
    d=system(inputs()[index]);assert record['system_pin']==pin(enc(description(d)))
    x=record['coefficients'];assert all(type(z)==int for z in x)
    rank=len(d['basis']);nc=len(d['cells']);assert len(x)==10*(rank+1)+56*rank+9*nc
    mats={t:[[0]*N for _ in range(N)] for t in d['cells']};pos=0
    for h in [d['reference']]+d['basis']:
        for i in range(N):
            g=x[pos];pos+=1
            for t,s in h.items():
                for j in t:mats[t][i][j]+=s*g;mats[t][j][i]+=s*g
    for h in d['basis']:
        for i in range(N):
            for j in range(i,N):
                c=x[pos];pos+=1
                for t,s in h.items():
                    mats[t][i][j]+=s*c
                    if i!=j:mats[t][j][i]+=s*c
        c=x[pos];pos+=1
        for t,s in h.items():
            for i in t:
                for j in t:mats[t][i][j]+=s*c*(1+(i==j))
    for t in d['cells']:
        for i in range(N):
            if i==root:continue
            mu=x[pos];pos+=1;assert mu>=0
            p=i+1 if i<root else i-1
            mats[t][i][i]+=2*mu;mats[t][i][p]-=mu;mats[t][p][i]-=mu
    assert pos==len(x)
    bh=hashlib.sha256();mh=hashlib.sha256();ph=hashlib.sha256();minimum=None
    for t,A in sorted(mats.items()):
        assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
        for i in range(N):A[i][i]-=1
        m=bareiss(A);p,m2=schur(A);assert m==m2
        bh.update(enc([t,A]));mh.update(enc([t,m]));ph.update(enc([t,list(map(str,p))]))
        minimum=min(m+[minimum]) if minimum is not None else min(m)
    return {'identity':'ALL_FACET_FLIP_EXACT_VERIFICATION_V1','native_index':index,'root':root,
            'cells':nc,'positive_leading_minors':nc*N,'basis_rank':rank,
            'system_pin':record['system_pin'],'coefficient_pin':pin(enc(x)),
            'blocks_sha256':bh.hexdigest(),'minors_sha256':mh.hexdigest(),
            'rational_pivots_sha256':ph.hexdigest(),'minimum_leading_minor':minimum}

if __name__=='__main__':
    if sys.argv[1:]==['census']:census()
    elif len(sys.argv)==5 and sys.argv[1]=='locate':raise ValueError('Use locate INDEX ROOT without extra arguments')
    elif len(sys.argv)==4 and sys.argv[1]=='locate':locate(int(sys.argv[2]),int(sys.argv[3]))
    elif len(sys.argv)==3 and sys.argv[1]=='check':
        b=Path(sys.argv[2]).read_bytes();r=check(json.loads(b));p=Path(sys.argv[2]).with_suffix('.verified.json');p.write_bytes(enc(r));print('ALL_FACET_FLIP_EXACT_CHECK_PASS',r['native_index'],r['root'],r['cells'],*pin(enc(r)))
    else:raise ValueError('Commands: census | locate INDEX ROOT | check RECORD.json')
