# material-3939c857ea7c

AI research material

---

"""PRISMATOID_ALL_SPD_U2_V1: exact, source-only continuous certificate.
Requires only cap_geometry.py (immutable recovery part 1) and Python stdlib.
The inline table is literal proof data, not a numerical solver invocation.
Run with assertions enabled: python -S prismatoid_all_spd.py build/check
"""
from cap_geometry import *
from math import comb
from pathlib import Path
import argparse, hashlib

FACETS=((0,3,2,1),(0,1,9,8),(0,6,3),(0,7,6),(0,8,7),(1,2,4,9),(2,3,5,4),(3,6,5),(4,5,6,7,8,9))
HALF=Q(1,2)
TABLE_TEXT="""
0:1 6:1 10:2
0:1 6:1 21:1
0:1 6:1 25:1
0:1 6:1 28:2
0:1 7:1 8:1 14:1 19:1
0:1 7:1 10:1 14:1 17:1 19:1
0:1 7:1 10:1 32:1
0:1 7:1 11:1
0:1 7:1 28:1 32:1
0:1 8:1 13:1 20:1 24:2 25:2
0:1 8:1 14:1 15:1 24:2 25:2
0:1 8:1 14:1 18:1 24:2 27:2 28:1
0:1 10:1 20:1
0:1 10:2 14:1 17:1 24:2 27:2
0:1 11:1 18:1
0:1 11:1 25:1
0:1 11:2 17:1 22:2 31:1
0:1 14:1 17:1 24:2 25:2
0:1 14:1 21:1
0:1 15:1 21:1 32:1
0:1 20:1 24:1 27:1 28:1
0:1 25:1 32:1
0:2 15:2 19:1 32:1
1:1 5:1 13:1
1:1 5:1 14:1
1:1 5:1 31:1
1:1 6:1 9:1 25:1 31:1
1:1 7:1 13:1 19:1 32:1
1:1 10:1 12:1
1:1 10:1 13:1 19:1
1:1 12:1 15:1 25:2 32:1
1:1 12:1 28:1
1:1 13:1 19:1 25:1
1:1 13:1 19:1 28:1
1:1 14:1 19:1
1:1 15:1 21:1 32:1
1:1 21:1 31:1
1:1 21:2 29:1 33:1
1:1 25:1 33:1
1:1 28:2 33:1
1:2 12:1 25:2 31:1
2:1 5:1 8:1
2:1 5:1 9:1 13:2
2:1 5:1 14:1
2:1 5:1 31:1
2:1 5:1 32:1
2:1 6:1 10:1 13:1 19:1 23:2
2:1 6:1 10:2 12:1 23:2
2:1 7:2 12:1 23:2 32:2
2:1 9:1 11:1
2:1 10:1 30:1 32:1
2:1 10:2 33:1
2:1 11:1 19:1
2:1 11:1 30:1
2:1 12:1 22:1 32:1
2:1 14:1 19:1 23:1
2:1 19:1 32:1
2:1 28:2 33:1
3:1 5:1 8:1
3:1 5:1 9:1 13:1 29:3
3:1 5:1 10:1 23:2 32:1
3:1 5:1 23:2 28:1 32:1
3:1 5:1 30:1 31:2
3:1 6:1 10:1 12:1 23:2
3:1 6:1 10:1 13:1 19:1 23:2
3:1 7:1 10:1 12:1 23:2 32:1
3:1 7:1 13:1 19:1 23:2 32:1
3:1 8:1 19:1
3:1 9:1 11:1
3:1 9:1 14:1
3:1 10:1 11:1 19:1 23:2
3:1 10:1 30:1 32:1
3:1 11:1 30:1
3:1 12:1 22:1 32:1
3:1 14:1 19:1 23:1
3:2 5:1 10:2 23:1 31:1
3:2 5:1 13:2 22:2 32:1
3:2 5:1 22:1 31:2
3:2 5:1 23:1 28:2 31:1
3:2 10:2 23:1 29:1 33:1
3:2 13:2 19:1 22:2 32:1
3:2 28:2 33:1
4:1 5:1 8:1
4:1 5:1 22:1 29:2
4:1 5:1 23:1 29:2
4:1 6:1 10:1 23:2
4:1 7:1 8:1 11:1 30:1
4:1 7:1 8:1 19:1
4:1 7:1 10:1 11:1 19:1 23:2
4:1 7:1 10:1 23:2 32:1
4:1 7:1 13:1 23:2 32:1
4:1 7:1 14:1 19:1 23:2 32:1
4:1 9:1 11:1
4:1 9:1 14:1
4:1 10:1 11:1 30:1
4:1 10:1 14:1 17:1 19:1
4:1 22:1 32:1
4:1 30:1 32:1
5:1 8:1 15:1
5:1 14:1 17:1
5:1 14:2 16:1 18:2
5:1 15:1 23:1 29:2
5:1 17:1 31:1
5:1 18:1 29:2 31:1
6:1 9:1 11:1 17:1 25:2 31:2
6:1 9:1 13:1
6:1 9:1 28:1 31:1
6:1 9:2 14:2
6:1 10:1 16:1
6:1 15:1 23:2
6:1 18:1 23:2 31:1
6:1 22:1 31:1
6:1 30:2 31:2
7:1 8:1 13:1 19:1
7:1 9:1 14:1
7:1 9:1 15:1 32:1
7:1 10:1 16:1 32:1
7:1 11:1 15:1 23:1
7:1 14:2 17:1 19:1 30:1
7:1 23:2 29:3 33:1
7:2 8:1 16:1 32:1
7:2 8:2 12:1
7:2 8:2 33:1
7:2 10:1 14:2 16:1 33:1
7:2 12:1 15:1 23:2 32:2
8:1 12:1 25:1
8:1 13:1 21:1
8:1 15:1 19:1
8:1 15:1 21:1
8:1 16:1 21:1
8:1 21:1 31:1
8:2 12:1 18:2
9:1 11:1 15:1
9:1 11:1 17:1 21:2 31:2
9:1 13:1 20:1
9:1 13:1 32:1
9:1 14:1 15:1
9:1 14:1 18:1
9:1 14:1 21:1
9:1 15:1 25:1 32:1
9:1 15:1 28:1 32:1
10:1 12:1 17:1
10:1 16:1 20:1
10:2 17:1 33:1
11:1 15:1 22:1
11:1 16:1 20:2 22:2 31:1
11:1 16:1 21:1
11:1 18:1 30:1 31:1
11:2 16:1 18:2
12:1 20:1 22:1
13:1 17:1 19:1
13:1 20:1 30:1
14:1 16:1 18:1 24:1
14:1 18:1 30:1
14:1 20:1 30:1
14:1 21:1 30:1
14:1 24:1 27:1 30:1
15:1 22:1 32:1
15:1 30:1 32:1
16:1 18:2 32:2
16:1 20:1 22:2 32:1
16:1 20:1 25:1
16:1 20:1 28:1
16:1 21:1 32:1
17:1 19:2 31:2
17:1 21:1 33:1
17:1 25:1 33:1
17:1 28:2 33:1
18:1 23:2 29:3 33:1
20:1 30:1 31:1
22:1 29:2 33:1
"""
TABLE=tuple(tuple(tuple(map(int,item.split(':'))) for item in line.split()) for line in TABLE_TEXT.strip().splitlines())

def vertices(t):
    return list(map(vec,[(-2,-2,0),(2,-2,0),(2,2,0),(-2,2,0),(3,3,HALF*5),(-1,3,HALF*5),(-2,1,HALF*5),(-2+t,0,HALF*5),(-1,-1,HALF*5),(3,-1,HALF*5)]))

def edges():
    e={}
    for f,cyc in enumerate(FACETS):
        for i,j in zip(cyc,cyc[1:]+cyc[:1]): e.setdefault(tuple(sorted((i,j))),[]).append(f)
    assert len(e)==17 and all(len(v)==2 for v in e.values())
    for i,j in e:
        assert sum((i,j) in tuple(zip(c,c[1:]+c[:1])) for c in FACETS)==1
        assert sum((j,i) in tuple(zip(c,c[1:]+c[:1])) for c in FACETS)==1
    return e
EDGES=edges()
ARCS=tuple(sorted(a for i,j in EDGES for a in ((i,j),(j,i))))

# Exact polynomial interpolation, ascending monomial coefficients. Four values
# identify degree <=3; five identify degree <=4. These are algebraic identities,
# not positivity sampling. Positivity uses complete Bernstein coefficients.
def interpolate(xx,yy):
    n=len(xx); ans=[Q(0)]*n
    for i,(x,y) in enumerate(zip(xx,yy)):
        p=[Q(1)];den=Q(1)
        for j,z in enumerate(xx):
            if i==j: continue
            nxt=[Q(0)]*(len(p)+1)
            for k,a in enumerate(p):nxt[k]-=z*a;nxt[k+1]+=a
            p=nxt;den*=x-z
        for k,a in enumerate(p):ans[k]+=y*a/den
    return ans

def bernstein(coeff):
    n=len(coeff)-1
    return [sum(coeff[d]*HALF**d*Q(comb(k,d),comb(n,d)) for d in range(k+1)) for k in range(n+1)]

def geom(t):
    vv=vertices(t);D=105-2*t
    num=vec((-2*t*t+15*t+133,4*(2*t+105),5*(215-6*t)))
    # 8Dg = (2(-2t^2+15t+133),4(2t+105),5(215-6t)).
    num=(2*num[0],num[1],num[2]);g=mul(1/(8*D),num)
    c=mul(Q(1,10),tuple(sum(v[k]for v in vv)for k in range(3)))
    guards={};vol=Q(0);first=ZERO
    for f,cyc in enumerate(FACETS):
        a,b,d=[vv[i]for i in cyc[:3]];no=cross(sub(b,a),sub(d,a));h=dot(no,a)
        for i,v in enumerate(vv):
            slack=h-dot(no,v)
            if i in cyc:assert slack==0
            else:guards[f'support_{f}_{i}']=slack
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):
            for k in cyc:
                if k not in (i,j):guards[f'polygon_{f}_{i}_{j}_{k}']=dot(no,cross(sub(vv[j],vv[i]),sub(vv[k],vv[i])))
        guards[f'centroid_inside_{f}']=8*D*h-dot(no,num)
        for j in range(1,len(cyc)-1):
            a,b,d=cyc[0],cyc[j],cyc[j+1]
            w=det(sub(vv[a],c),sub(vv[b],c),sub(vv[d],c))/6
            guards[f'tetra_{f}_{j}']=w
            vol+=w;first=add(first,mul(w/4,add(add(c,vv[a]),add(vv[b],vv[d]))))
    guards['volume']=vol
    expected_volume=5*D/12
    assert vol==expected_volume and first==mul(expected_volume,g)
    return guards,vol,first,g

def certify_geometry():
    # Supports, oriented polygon guards, cleared centroid denominators, and
    # tetrahedron volumes all have degree <=3. First moments have degree <=4.
    ts=[HALF*Q(i,4) for i in range(5)]
    samples=[geom(t)for t in ts]
    names=sorted(samples[0][0]);assert all(sorted(s[0])==names for s in samples)
    records=[];positive=zero=0
    for name in names:
        coeff=interpolate(ts,[s[0][name]for s in samples])
        assert coeff[4]==0
        bb=bernstein(coeff[:4]);assert min(bb)>=0 and max(bb)>0,(name,bb)
        positive+=sum(b>0 for b in bb);zero+=sum(b==0 for b in bb)
        records.append(dict(name=name,monomial=coeff[:4],bernstein=bb))
    vcoeff=interpolate(ts,[s[1]for s in samples]);assert vcoeff==[Q(175,4),-Q(5,6),0,0,0]
    fcoeff=[interpolate(ts,[s[2][k]for s in samples])for k in range(3)]
    # Five identity values establish degree <=4 equality with Vol*g exactly.
    expected=[[Q(665,48),Q(25,16),-Q(5,24),0,0], [Q(175,8),Q(5,12),0,0,0], [Q(5375,96),-Q(25,16),0,0,0]]
    assert fcoeff==expected,(fcoeff,expected)
    return dict(records=records,positive_coefficients=positive,zero_endpoint_coefficients=zero,volume_coefficients=vcoeff,first_moment_coefficients=fcoeff)

def matrices(t):
    vv=vertices(t);D=105-2*t
    num=vec((2*(-2*t*t+15*t+133),4*(2*t+105),5*(215-6*t)))
    W=[sub(mul(8*D,v),num)for v in vv];out=[]
    for i,j in ARCS:
        e=sub(vv[j],vv[i]);out.append(matscale(-1,matadd(outer(W[i],e),outer(e,W[i]))))
    return out

def coefficients():
    ts=(Q(0),Q(1,6),Q(1,3),HALF);samples=[matrices(t)for t in ts];out=[]
    for a in range(34):
        polynomial=[[interpolate(ts,[s[a][i][j]for s in samples])for j in range(3)]for i in range(3)]
        out.append([tuple(tuple(bernstein(polynomial[i][j])[k]for j in range(3))for i in range(3))for k in range(4)])
    return out

def minor3(A):return (A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(*A))

def rooted_trees():
    count=0
    for ee in combinations(sorted(EDGES),9):
        adj=[[]for _ in range(10)]
        for a,b in ee:adj[a].append(b);adj[b].append(a)
        seen={0};stack=[0]
        while stack:
            a=stack.pop()
            for b in adj[a]:
                if b not in seen:seen.add(b);stack.append(b)
        if len(seen)!=10:continue
        count+=1
        for root in range(10):
            parent={root:root};stack=[root]
            while stack:
                a=stack.pop()
                for b in adj[a]:
                    if b not in parent:parent[b]=a;stack.append(b)
            ids=tuple(sorted(ARCS.index((i,j))for i,j in parent.items()if i!=j))
            yield sum(1<<i for i in ids),root,tuple(parent[i]for i in range(10))
    assert count==5299

def encode(o):
    if isinstance(o,Q):return str(o)
    if isinstance(o,dict):return {str(k):encode(v)for k,v in o.items()}
    if isinstance(o,(list,tuple)):return [encode(v)for v in o]
    return o

def build():
    geometry=certify_geometry();CC=coefficients();records=[];allminors=[]
    assert len(TABLE)==171 and tuple(sorted(TABLE))==TABLE
    for row in TABLE:
        ids=[i for i,w in row]
        assert len(ids)==len(set(ids)) and ids==sorted(ids)
        assert len({ARCS[i][0]for i in ids})==len(ids)
        assert all(0<=i<34 and 1<=w<=3 for i,w in row)
        blocks=[]
        for k in range(4):
            A=ZMAT
            for i,w in row:A=matadd(A,matscale(w,CC[i][k]))
            assert A==transpose(A)
            mm=minor3(A);assert all(x>0 for x in mm),(row,k,mm)
            allminors.extend(mm);blocks.append(dict(matrix=A,leading_minors=mm))
        records.append(dict(row=row,bernstein_blocks=blocks))
    masks=[sum(1<<i for i,w in row)for row in TABLE]
    coverage=[];seen=set();counts=[0]*171
    for mask,root,parents in rooted_trees():
        assert mask not in seen;seen.add(mask)
        hit=next((j for j,m in enumerate(masks)if mask&m==m),None)
        assert hit is not None,(root,parents)
        counts[hit]+=1;coverage.append(str(root)+'\t'+','.join(map(str,parents))+'\t'+str(hit)+'\n')
    assert len(coverage)==52990 and sum(counts)==52990
    coverage=''.join(coverage).encode()
    controls=[]
    B=tuple(map(vec,((23,-13,-10),(-13,22,9),(-10,9,12))))
    for t in (Q(1,4),Q(1,128),Q(63,128)):
        P=hull(vertices(t));assert tuple(P['facets'])==FACETS
        assert len(P['vertices'])==10 and len(P['edges'])==17
        _,V,J,g=geom(t);assert P['volume']==V and P['g']==g
        for name,N in [('identity',ID),('moving_sinks',B)]:
            R=mechanics(P,N);assert len(R['U'])>=2
            controls.append(dict(t=t,metric=name,N=N,M=inv(N),volume=V,centroid=g,mechanics=R))
    assert [len(controls[0]['mechanics'][k])for k in ('S','U','H')]==[9,9,16]
    assert [len(controls[1]['mechanics'][k])for k in ('S','U','H')]==[6,7,11]
    data=dict(identity='PRISMATOID_ALL_SPD_U2_V1',parameter='0<t<1/2',metric='ALL SPD M; N=M^-1',facets=FACETS,edges=sorted(EDGES),arcs=ARCS,geometry=geometry,certificates=records,total_rooted_trees=len(seen),tree_first_witness_counts=counts,coverage_bytes=len(coverage),coverage_sha256=hashlib.sha256(coverage).hexdigest(),minimum_leading_minor=min(allminors),total_PD_blocks=684,total_positive_leading_minors=len(allminors),controls=controls)
    report=(json.dumps(encode(data),sort_keys=True,indent=2)+'\n').encode()
    return report,coverage,data

def main():
    assert __debug__
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('build','check'));args=ap.parse_args()
    report,coverage,data=build()
    for name,raw in [('prismatoid_all_spd_report.json',report),('prismatoid_all_spd_coverage.tsv',coverage)]:
        if args.mode=='build':Path(name).write_bytes(raw)
        else:assert Path(name).read_bytes()==raw
        print(name,len(raw),hashlib.sha256(raw).hexdigest())
    g=data['geometry']
    print('ACTUAL_CONTINUOUS_10_17_9_GEOMETRY_AND_VOLUME_CENTROID_PASS',len(g['records']),g['positive_coefficients'],g['zero_endpoint_coefficients'])
    print('EXACT_ALL_52990_ROOTED_TREES_COVERED_BY_171_ROWS_PASS')
    print('ALL_684_BERNSTEIN_BLOCKS_2052_POSITIVE_MINORS_PASS',str(data['minimum_leading_minor']))
    print('ALL_SPD_M_PRISMATOID_U_AT_LEAST_TWO_FOR_ALL_T_PASS')
    print('PRISMATOID_ALL_SPD_U2_V1_SOURCE_ONLY_RECOVERY_PASS')
if __name__=='__main__':main()
