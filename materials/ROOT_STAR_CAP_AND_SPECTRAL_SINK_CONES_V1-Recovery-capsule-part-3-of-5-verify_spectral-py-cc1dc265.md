# material-cc1dc2652109

AI research material

---

"""Standard-library verifier; no symbolic engine, no floating arithmetic.
65 exact identity evaluations, with degree <=64, are NOT positivity sampling.
Every positivity assertion uses a full positive Bernstein coefficient vector.
Run: python -S verify_spectral.py [two_sink_report.json]
"""
from cap_geometry import *
from math import comb
from pathlib import Path
import sys, hashlib

FACETS=((0,3,2,1),(0,1,9,8),(0,6,3),(0,7,6),(0,8,7),(1,2,4,9),(2,3,5,4),(3,6,5),(4,5,6,7,8,9))
B=tuple(map(vec,((23,-13,-10),(-13,22,9),(-10,9,12))))
HALF=Q(1,2)
def vertices(t):
    return list(map(vec,[(-2,-2,0),(2,-2,0),(2,2,0),(-2,2,0),(3,3,Q(5,2)),(-1,3,Q(5,2)),(-2,1,Q(5,2)),(-2+t,0,Q(5,2)),(-1,-1,Q(5,2)),(3,-1,Q(5,2))]))
def geometric_values(t):
    vv=vertices(t);c=mul(Q(1,10),tuple(sum(v[j] for v in vv)for j in range(3)));values={};planes=[];edges={}
    for i,cyc in enumerate(FACETS):
        a,b,d=[vv[k]for k in cyc[:3]];n=cross(sub(b,a),sub(d,a));h=dot(n,a);planes.append((n,h))
        for j,v in enumerate(vv):
            slack=h-dot(n,v)
            if j in cyc:assert slack==0
            else:values[f'incidence_{i}_{j}']=slack
        for a,b,d in zip(cyc,cyc[1:]+cyc[:1],cyc[2:]+cyc[:2]):
            values[f'facet_turn_{i}_{a}']=dot(n,cross(sub(vv[b],vv[a]),sub(vv[d],vv[b])))
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(i)
    assert len(edges)==17 and all(len(fs)==2 for fs in edges.values())
    vol=Q(0);first=ZERO
    for cyc in FACETS:
        for j in range(1,len(cyc)-1):
            a,b,d=cyc[0],cyc[j],cyc[j+1];vs=[c,vv[a],vv[b],vv[d]]
            w=det(sub(vs[1],c),sub(vs[2],c),sub(vs[3],c))/6
            values[f'volume_tetra_{a}_{b}_{d}']=w
            vol+=w;first=add(first,mul(w/4,tuple(sum(v[k]for v in vs)for k in range(3))))
    g=mul(1/vol,first);D=105-2*t
    assert vol==5*D/12 and g==vec(((-2*t*t+15*t+133)/(4*D),(2*t+105)/(2*D),5*(215-6*t)/(8*D)))
    values['true_volume']=vol;q=[]
    for i,(n,h) in enumerate(planes):
        den=h-dot(n,g);values[f'own_COM_pole_denominator_{i}']=den;q.append(mul(1/den,n))
    arcs=sorted(tuple(a) for fs in edges.values()for a in (fs,fs[::-1]))
    for label,C,k,sets in [('two_fixed_facets',ID,7,((0,),(8,))),('two_moving_sinks',B,4,((0,5),(6,7,8)))]:
        for ss in sets:
            for i,j in arcs:
                if i in ss and j not in ss:
                    u=q[i];v=sub(q[j],u);d=dot(u,mv(C,v));r2=dot(u,mv(C,u))*dot(v,mv(C,v))
                    values[f'{label}_{i}_to_{j}_negative']=-d
                    values[f'{label}_{i}_to_{j}_strict_cone']=(k+1)**2*d*d-(k-1)**2*r2
    return values

def evaluate(coeffs,t):
    v=Q(0)
    for a in coeffs:v=v*t+a
    return v

def check_bernstein(coeffs,reported):
    assert coeffs and coeffs[0]!=0
    n=len(coeffs)-1;aa=[a*HALF**i for i,a in enumerate(reversed(coeffs))]
    out=[sum(aa[i]*Q(comb(k,i),comb(n,i))for i in range(k+1))for k in range(n+1)]
    assert out==list(map(Q,reported)) and all(b>0 for b in out)
    return len(out)

def main():
    assert __debug__
    p=Path(sys.argv[1]if len(sys.argv)>1 else 'two_sink_report.json');data=p.read_bytes();obj=json.loads(data)
    assert obj['identity']=='TWO_SINK_PRISMATOID_V1' and obj['parameter']=='0<t<1/2' and obj['height']=='5/2'
    assert tuple(map(tuple,obj['facets']))==FACETS and tuple(map(vec,obj['B']))==B
    assert B[0][0]>0 and B[0][0]*B[1][1]-B[0][1]**2>0 and det(*B)>0
    records=obj['certificates'];rows={};bc=0
    for r in records:
        name=r['label'];assert name not in rows
        n=list(map(Q,r['numerator']));d=list(map(Q,r['denominator']));a,b=r['endpoint_factor_powers']
        assert isinstance(a,int) and isinstance(b,int) and a>=0 and b>=0
        assert len(n)-1+a+b<=30 and len(d)-1<=30
        assert r['interior'] or a+b==0
        bc+=check_bernstein(n,r['bernstein_numerator'])+check_bernstein(d,r['bernstein_denominator'])
        rows[name]=(n,d,a,b)
    # Geometric degrees: coordinates <=1; planes <=1; fan volumes <=3;
    # first moments <=4; g <=4/3; poles <=4/5. Cone D <=13/15,
    # cone square margin <=26/30. Combined with report degrees <=30,
    # cross-multiplied differences have degree <=60 (we use bound64).
    tests=0
    for j in range(1,66):
        t=Q(j,132);actual=geometric_values(t);assert set(actual)==set(rows)
        for label,value in actual.items():
            n,d,a,b=rows[label]
            assert value==t**a*(HALF-t)**b*evaluate(n,t)/evaluate(d,t),label
            tests+=1
    P=hull(vertices(Q(1,4)))
    assert tuple(P['facets'])==FACETS and [len(P['X']),len(P['edges']),len(P['facets'])]==[10,17,9]
    assert P['volume']==Q(1045,24) and P['g']==vec((Q(1093,3344),Q(211,418),Q(2135,1672)))
    for name,N,counts in [('identity',ID,(9,9,16)),('moving_sink_center',B,(6,7,11))]:
        m=mechanics(P,N);assert not m['zeros'];assert tuple(len(m[k])for k in ('S','U','H'))==counts
        assert m['S']==obj['controls'][name]['S'] and m['U']==obj['controls'][name]['U']
        assert list(map(tuple,obj['controls'][name]['H']))==m['H']
    qq=P['poles'];arcs=[]
    for fs in P['edges'].values():
        for i,j in (fs,fs[::-1]):
            u=qq[i];v=sub(qq[j],u);d=dot(u,mv(B,v));r2=dot(u,mv(B,u))*dot(v,mv(B,v))
            if d>=0 or 25*d*d<=9*r2:
                assert d>0 or 25*d*d<9*r2;arcs.append((i,j))
    arcs.sort();assert arcs==list(map(tuple,obj['possible_arcs_at_quarter']))
    assert all(any(a==i for a,b in arcs)for i in range(9))
    cuts=((0,5),(6,7,8))
    assert not any(a in c and b not in c for c in cuts for a,b in arcs)
    assert (0,5) in arcs and (5,0) in arcs
    assert (6,7) in arcs and (7,8) in arcs and (8,7) in arcs and (7,6) in arcs
    # Every vertex outside the two components reaches one of them.
    reach=[{i}for i in range(9)]
    for a,b in arcs:reach[a].add(b)
    for k in range(9):
        for i in range(9):
            if k in reach[i]:reach[i]|=reach[k]
    assert all(reach[i]&set(sum((list(c)for c in cuts),[]))for i in range(9))
    qb=qq[0];good=[];out=[]
    for i in range(4,10):
        a=P['X'][i];delta=(2-dot(qb,a))**2-dot(qb,qb)*dot(a,a)
        out.append([i,str(delta)])
        if delta>0:good.append(i)
    assert out==obj['cap_deltas_at_quarter'] and good==[5,6,7,8,9]
    assert all(any(v in good for v in FACETS[j]) for fs in P['edges'].values()if 0 in fs for j in fs if j!=0)
    assert len(records)==162 and bc==894 and tests==10530
    print('GEOMETRIC_RATIONAL_IDENTITIES_DEGREE_64_PASS',tests)
    print('COMPLETE_POSITIVE_BERNSTEIN_VECTORS_PASS',len(records),bc)
    print('ACTUAL_OWN_COM_10_17_9_AND_MOVING_SINK_MECHANICS_PASS')
    print('ROOT_STAR_CAP_PASSES_ALL_VERTEX_CAP_FAILS_PASS')
    print('TWO_SINK_PRISMATOID_V1_STDLIB_VERIFICATION_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
