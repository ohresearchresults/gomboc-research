# material-ceb90083e17b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""REFERENCE_NERVE_QP_CELLS_V1, exact recovery, no external input.
CPython 3.13.5, standard library, assertions enabled.
python -S reference_cells.py build
python -S reference_cells.py check
Not an E17 exclusion or a class110 construction; see continuous proof.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY = 'REFERENCE_NERVE_QP_CELLS_V1'
PARENTS = [
 ['minimum-0087',
  'b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5'],
 ['minimum-0085',
  '0a5851220e64a183556867fe7de61661448316915225e1cd6e729afe8cf62ef5']]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def matvec(a,x):
    return [dot(row,x) for row in a]

def transpose(a):
    return list(map(list,zip(*a)))

def mm(a,b):
    return [[dot(row,col) for col in transpose(b)] for row in a]

def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]

def solve(a,b):
    n=len(a)
    assert len(b)==n and all(len(row)==n for row in a)
    t=[list(map(F,row))+[F(y)] for row,y in zip(a,b)]
    for k in range(n):
        p=next((i for i in range(k,n) if t[i][k]),None)
        if p is None:
            return None
        t[k],t[p]=t[p],t[k]
        divisor=t[k][k]
        t[k]=[v/divisor for v in t[k]]
        for i in range(n):
            if i!=k:
                factor=t[i][k]
                t[i]=[a-factor*b for a,b in zip(t[i],t[k])]
    return [row[-1] for row in t]

def inverse(a):
    cols=[solve(a,col) for col in identity(len(a))]
    if any(col is None for col in cols):
        return None
    return transpose(cols)

def gram(q,n):
    return mm(mm(q,n),transpose(q))

def subsets(items):
    for k in range(1,len(items)+1):
        yield from combinations(items,k)

def exterior_cells(q,n,labels):
    """All nonsingular support charts; inequalities row dot (1,c)>=0."""
    g=gram(q,n)
    h=[[F(1)]+[-x for x in row] for row in q]
    out=[]
    for support in subsets(labels):
        inv=inverse([[g[i][j] for j in support] for i in support])
        if inv is None:
            continue
        hj=[h[i] for i in support]
        multipliers=mm(inv,hj)
        rows=list(multipliers)
        for i in labels:
            if i not in support:
                v=matvec(transpose(multipliers),[g[i][j] for j in support])
                rows.append([a-b for a,b in zip(v,h[i])])
        quad=mm(transpose(hj),multipliers)
        assert quad==transpose(quad)
        out.append({'support':list(support),'inverse_gram':inv,
                    'multiplier_rows':multipliers,'cell_rows':rows,
                    'distance_squared_matrix':quad})
    return out

def distance_at(cells,c):
    z=[F(1)]+list(c)
    winners=[]
    for cell in cells:
        if all(dot(row,z)>=0 for row in cell['cell_rows']):
            radius2=dot(z,matvec(cell['distance_squared_matrix'],z))
            assert radius2>0
            winners.append((radius2,cell['support']))
    if not winners:
        return None,[]
    assert len(set(r for r,s in winners))==1
    return winners[0][0],[s for r,s in winners]

def simplex_weight(q,n,labels,c):
    """Original normalized-pole simplex problem, with singular Gram permitted.
    Enumerate affinely independent faces via bordered KKT systems, including w=0.
    """
    h=[1-dot(row,c) for row in q]
    assert min(h)>0
    qc=[[x/h[i] for x in row] for i,row in enumerate(q)]
    g=gram(qc,n)
    hits=[]
    for support in subsets(labels):
        size=len(support)
        a=[[g[i][j] for j in support]+[F(-1)] for i in support]
        a.append([F(1)]*size+[F(0)])
        sol=solve(a,[F(0)]*size+[F(1)])
        if sol is None:
            continue
        lam,w=sol[:-1],sol[-1]
        if min(lam)<0:
            continue
        if any(sum((g[i][j]*x for j,x in zip(support,lam)),F(0))<w for i in labels):
            continue
        assert w>=0 and sum(lam)==1
        hits.append(w)
    assert hits and len(set(hits))==1
    return hits[0]

def audit_geometry(q,n,refs,need_129=False):
    labels=[s for k in range(1,4) for s in combinations(range(len(q)),k)]
    all_cells={s:exterior_cells(q,n,s) for s in labels}
    m=inverse(n)
    assert m is not None and mm(m,n)==identity(3)
    full_rank_count=0
    for s in combinations(range(len(q)),3):
        inv=inverse([[gram(q,n)[i][j] for j in s] for i in s])
        if inv is not None:
            # Every rank-three support distance has exactly the same Hessian M.
            full=next(cell for cell in all_cells[s] if cell['support']==list(s))
            assert [row[1:] for row in full['distance_squared_matrix'][1:]]==m
            full_rank_count+=1
    checks=[]
    for c in refs:
        assert all(1-dot(row,c)>0 for row in q)
        row=[]
        for s in labels:
            d,supports=distance_at(all_cells[s],c)
            w=simplex_weight(q,n,s,c)
            assert (d is None)==(w==0)
            if d is not None:
                assert w*d==1
            row.append({'I':list(s),'weight':w,'distance2':d,'active_supports':supports})
        checks.append({'reference':c,'weights':row})
    if need_129:
        assert len(labels)==129
        assert sum(2**len(s)-1 for s in labels)==705
    return {'Q':q,'N':n,'M':m,'all_charts':[
                {'I':list(s),'charts':all_cells[s]} for s in labels],
            'full_rank_triple_hessian_checks':full_rank_count,
            'point_checks':checks}

def encode(obj):
    if isinstance(obj,F):
        return str(obj)
    if isinstance(obj,(list,tuple)):
        return [encode(x) for x in obj]
    if isinstance(obj,dict):
        return {k:encode(v) for k,v in obj.items()}
    return obj

def build():
    # EXACT original nine poles, labels unchanged, from H0_GLOBAL_NERVE129 parent.
    # This is NOT the different Finch22 E17 body.
    raw=[(-32,-16,-32,29),(128,-128,-128,119),(128,128,-128,127),
         (-64,64,-64,61),(-128,-128,128,129),(64,-64,64,67),
         (64,64,64,71),(-128,128,128,137),(0,0,256,143)]
    q=[[F(x,row[3]) for x in row[:3]] for row in raw]
    refs=[[F(0)]*3,[F(1,16),F(1,32),F(-1,64)],
          [F(-1,8),F(1,16),F(0)],[F(1,4),F(0),F(0)]]
    exact=audit_geometry(q,identity(3),refs,True)
    # Reciprocal metric test, not a new own-centroid or class110 example.
    n=[[F(2),F(1),F(0)],[F(1),F(2),F(0)],[F(0),F(0),F(1,2)]]
    metric=audit_geometry(q,n,[refs[1]],True)
    assert metric['M']!=n
    # Bounded prism control crossing an exact support wall, and antipodal zero.
    small_q=list(map(lambda row:list(map(F,row)),[
        (1,0,0),(1,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]))
    small_refs=[[F(0),y,F(0)] for y in [F(-1,4),F(0),F(1,4)]]
    charts=exterior_cells(small_q,identity(3),(0,1))
    tie=[]
    for c in small_refs:
        d,s=distance_at(charts,c)
        w=simplex_weight(small_q,identity(3),(0,1),c)
        assert d*w==1
        tie.append({'c':c,'distance2':d,'weight':w,'supports':s})
    assert [r['distance2'] for r in tie]==[F(17,16),F(1),F(1)]
    assert tie[0]['supports']==[[0,1]]
    assert tie[1]['supports']==[[0],[0,1]]
    assert tie[2]['supports']==[[0]]
    for c in small_refs:
        assert simplex_weight(small_q,identity(3),(0,2),c)==0
        assert distance_at(exterior_cells(small_q,identity(3),(0,2)),c)==(None,[])
    return (json.dumps(encode({'identity':IDENTITY,'exact_parents':PARENTS,
        'scope':'PARAMETRIC_METHOD_CONTROLS_NOT_WHOLE_E17_OR_ATTAINER',
        'h0_literal_e17_reference':exact,'h0_literal_e17_reciprocal_metric':metric,
        'support_wall_control':{'Q':small_q,'charts':charts,'points':tie},
        'zero_weight_control':'opposite poles 0,2; all three references; no exterior cell'}),
        sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')

if __name__=='__main__':
    if sys.argv[1:] not in (['build'],['check']):
        raise SystemExit('Usage: python -S reference_cells.py build|check')
    data=build()
    path=Path('reference_cells.json')
    if sys.argv[1]=='build':
        if path.exists():
            assert path.read_bytes()==data,'Refuse to replace different exact report'
        path.write_bytes(data)
    else:
        assert path.read_bytes()==data,'Exact report mismatch'
    print('REFERENCE_NERVE_129_WEIGHTS_705_SUPPORTS_EXACT_PASS')
    print('FIXED_REFERENCE_POLYHEDRAL_KKT_QUADRATIC_CHARTS_PASS')
    print('RECIPROCAL_METRIC_COMMON_FULL_TRIPLE_HESSIAN_PASS')
    print('ZERO_WEIGHTS_AND_SIMULTANEOUS_SUPPORT_TIES_PASS')
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('REFERENCE_NERVE_QP_CELLS_RECOVERY_PASS')
