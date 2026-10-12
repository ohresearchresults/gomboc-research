import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
from pathlib import Path
import sys,json,hashlib,multiprocessing
from functools import lru_cache
sys.path.insert(0,str(Path('nova54_recovery').resolve()))
import comb,exact_check
FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
P={
1200:[1,2,5,3,0,3,3,4,7],
1205:[1,2,5,3,0,3,3,8,4],
1472:[1,2,5,3,3,8,3,6,7],
1752:[1,4,0,3,3,2,5,3,6],
1775:[1,4,0,3,3,2,8,3,5],
3058:[1,4,3,3,7,6,3,8,5],
3124:[1,4,3,3,8,3,5,6,7],
3149:[1,4,3,3,8,6,7,3,5],
3966:[1,5,3,3,0,2,3,4,7],
5772:[2,0,5,3,1,3,3,4,7],
7000:[2,4,3,3,0,1,5,3,6]}
WHOLE={1200,1472,1752}
def _raw_relations(faces,apices):
    from mp45_mass_gate import geometry
    assert tuple(map(tuple,faces))==FS and tuple(apices)==tuple(range(9))
    cells,R,beta,f0=geometry()
    return cells,beta
@lru_cache(None)
def _relations(faces,apices):
    return _raw_relations(faces,apices)
def cached_relations(faces,apices):
    return _relations(tuple(map(tuple,faces)),tuple(apices))
exact_check.volume_relations=cached_relations

def emit(name,obj):
    b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(name).write_bytes(b)
    print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True)

def broom(p):
    paths=[]
    for i in range(9):
        q=[i]
        while q[-1]!=3:
            q.append(p[q[-1]])
            assert len(q)<=9
        paths.append(q)
    b=list(reversed(max(paths,key=len)))
    assert len(b)==8
    b.append(next(i for i in range(9) if i not in b))
    assert p[b[8]]==3
    return b

def comparisons(ix,o):
    b=broom(P[ix])
    return ([(b[8],b[o])] if o else [])+([(b[o+1],b[8])] if o<7 else [])

def cases():
    return [(i,o) for i in P for o in range(8) if i in WHOLE or o>0]

def graph():
    es=sorted({tuple(sorted((f[i],f[(i+1)%3]))) for f in FS for i in range(3)})
    L=[[sum(i in e for e in es) if i==j else -int(tuple(sorted((i,j))) in es)
        for j in range(8)] for i in range(8)]
    return dict(facets=FS,edges=es,aut=comb.auto_maps(FS),trees=comb.det(L))

def check_record(ix,o,z):
    pp=comparisons(ix,o)
    rel=exact_check.volume_relations(FS,list(range(9)))[1]
    assert len(rel)==10
    assert len(z)==1063+63*len(pp)
    assert all(type(v) is int for v in z)
    assert min(z[1063:])>=0
    rec=dict(root=3,parent=P[ix],kind='cycle',fans=[[a,0] for a in range(9)],
             relations=rel,z=z[:1063])
    h=hashlib.sha256();count=0
    for u,Q in enumerate(exact_check.scalar_matrices(rec,FS)):
        for (i,j),v in zip(pp,z[1063+u*len(pp):1063+(u+1)*len(pp)]):
            Q[i][i]+=2*v
            Q[j][j]-=2*v
        a=exact_check.bareiss(Q)
        assert a==exact_check.ldl(Q)
        h.update(comb.encoded([Q,a]));count+=1
    assert count==63
    return h.hexdigest()

def build_one(arg):
    import numpy as np
    import locator
    ix,o=arg
    x,B,ls,bi,mat,info=locator.cycle_problem(P[ix],FS)
    pp=comparisons(ix,o);k=len(mat);m=len(pp);N=len(x);E=np.eye(9)
    extra=[np.outer(E[i],E[i])-np.outer(E[j],E[j]) for i,j in pp]
    xx=np.r_[x[:-1],np.zeros(k*m),x[-1]]
    BB=np.r_[B[:-1],np.ones(k*m),B[-1]]
    ll=np.r_[ls,np.arange(N-1,N-1+k*m)]
    xx[ll]=1/(k*(8+m))
    ii=[];mm=[]
    for u,(ids,L) in enumerate(zip(bi,mat)):
        ii.append(np.r_[ids[:-1],np.arange(N-1+u*m,N-1+(u+1)*m),N-1+k*m])
        mm.append(np.concatenate([L[:-1],np.array(extra),L[-1:]]))
    v=locator.shared_locate((xx,BB,ll,ii,mm,info),eps=1e-8,maxouter=14)
    assert v is not None and np.isfinite(v).all()
    scale=max(abs(float(a)) for a in v[:-1])
    for power in (6,8,10,12):
        z=[round(float(a)/scale*10**power) for a in v[:-1]]
        try:
            hh=check_record(ix,o,z)
        except AssertionError:
            continue
        return dict(index=ix,parent=P[ix],order=o,pairs=[list(t) for t in pp],
                    power=power,z=z,scalar_sha=hh)
    raise AssertionError(('NO_EXACT_CERTIFICATE',ix,o))

def verify(rows):
    assert [(r['index'],r['order']) for r in rows]==cases()
    assert len(rows)==80
    parents=comb.parent_trees(graph(),3)
    assert len(parents)==9140
    for i,p in P.items():
        assert list(parents[i])==p
    for r in rows:
        i,o=r['index'],r['order']
        assert r['parent']==P[i]
        assert r['pairs']==[list(t) for t in comparisons(i,o)]
        assert r['power'] in (6,8,10,12)
        assert r['scalar_sha']==check_record(i,o,r['z'])
    remaining=[]
    for i,p in P.items():
        if i not in WHOLE:
            b=broom(p)
            remaining.append(dict(index=i,parent=p,broom_order=b,
                                  necessary_strict_norm_pair=[b[8],b[1]]))
    report=dict(graph='MP9:45',root=3,facets=FS,branches=80,matrices=5040,
                leading_minors_per_checker=45360,whole_assigned_indices=sorted(WHOLE),
                remaining_assigned_cases=remaining,
                scope='Assigned eleven only; no whole-graph or C32 propagation assertion')
    emit('mp45_norm80_report.json',report)
    print('NOVA54_MP45_80_CHAMBERS_3_WHOLE_ASSIGNED_TREES_8_STRICT_REMAINDERS_PASS',flush=True)

if __name__=='__main__':
    if sys.argv[1]=='build':
        with multiprocessing.get_context('fork').Pool(4) as pool:
            rows=[]
            Path('norm_records').mkdir(exist_ok=True)
            for r in pool.imap(build_one,cases()):
                rows.append(r)
                Path('norm_records/%s_%s.json'%(r['index'],r['order'])).write_bytes(comb.encoded(r))
                print('NORM_EXACT',r['index'],r['order'],r['power'],r['scalar_sha'],flush=True)
        emit('mp45_norm80.json',rows)
        verify(rows)
    elif sys.argv[1]=='check':
        verify(json.loads(Path('mp45_norm80.json').read_bytes()))
    else:
        raise SystemExit('use build or check')
