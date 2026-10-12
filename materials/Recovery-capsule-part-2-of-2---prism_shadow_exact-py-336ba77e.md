# material-336ba77e923b

AI research material

---

#!/usr/bin/env python3
"""PRISMATOID_ALL_KERNEL_SHADOW_OCTAGON_REDUCTION_V1.
Exact stdlib-only verifier; Python >=3.11, assertions enabled.
Usage: python -B prism_shadow_exact.py build|check
No solver, RNG, tolerance, network, parent file or external data is needed.
The complete Farkas witnesses below certify all 128 strict sign patterns.
"""
from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib,json,sys
assert __debug__ and sys.version_info >= (3,11)
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),
       (9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
BASE=((1,0,0,0,0,0),(0,0,1,0,0,0),(0,0,0,1,0,0),
      (-1,1,0,0,0,0),(2,-1,0,0,0,0))
# Variable order a,b,p,q,u,v; side-face order F1,...,F7.
NORMAL_ROWS=((0,0,0,0,0,-1),(0,-1,0,0,-1,-2),(0,0,-1,0,1,0),
             (0,0,0,0,1,1),(0,0,0,-1,0,1),(0,0,0,0,-1,0),
             (-1,0,0,0,-1,-1))
LITERALS=json.loads(r'''{"counts":{"5":3,"6":8,"7":10,"8":5},"feasible_witnesses":{"1":["5/14","4/7","2/7","1/7","1/7","-2/7"],"11":["2/11","3/11","7/11","1/11","6/11","-5/11"],"112":["2/5","3/5","1/5","1/5","-6/5","2/5"],"114":["2/5","3/5","1/5","1/5","-8/5","2/5"],"12":["2/5","3/5","1/5","2/5","2/5","1/5"],"13":["2/5","3/5","1/5","1/5","2/5","-1/5"],"15":["2/5","3/5","1/5","1/5","6/5","-1"],"24":["1/3","1/2","1/3","1/6","1/6","1/3"],"28":["2/5","3/5","1/5","1/5","2/5","2/5"],"3":["2/7","3/7","3/7","1/7","2/7","-3/7"],"32":["2/5","3/5","1/5","2/5","-2/5","1/5"],"33":["3/7","5/7","1/7","1/7","-1/7","-1/7"],"35":["5/8","3/4","1/8","1/8","-1/8","-3/8"],"40":["1/3","1/2","1/6","1/2","-1/6","1/3"],"48":["2/5","3/5","1/5","1/5","-3/5","2/5"],"5":["3/7","5/7","1/7","1/7","2/7","-3/7"],"56":["2/5","3/5","1/5","1/5","-1/5","2/5"],"67":["1/3","1/2","1/3","1/6","1/6","-2/3"],"7":["2/5","3/5","1/5","1/5","2/5","-3/5"],"71":["2/5","3/5","1/5","1/5","2/5","-1"],"8":["1/3","1/2","1/3","1/3","1/6","1/6"],"9":["2/7","3/7","3/7","1/7","2/7","-1/7"],"96":["2/5","3/5","1/5","2/5","-4/5","1/5"],"97":["4/9","7/9","1/9","1/9","-4/9","-1/9"],"98":["2/5","3/5","1/5","1/5","-6/5","1/5"],"99":["2/5","3/5","1/5","1/5","-2/5","-1/5"]},"infeasible_stresses":{"0":[[5,1],[8,1],[10,1]],"10":[[3,2],[4,1],[5,2],[6,1],[10,1]],"100":[[0,1],[1,1],[5,1],[7,1],[11,1]],"101":[[1,1],[4,1],[6,1],[7,1],[11,2]],"102":[[1,1],[3,2],[4,1],[5,2],[6,1],[7,1]],"103":[[1,1],[7,1],[10,1]],"104":[[3,1],[4,1],[8,1],[11,1]],"105":[[0,1],[8,1],[11,1]],"106":[[3,2],[4,1],[6,1],[8,2],[10,1]],"107":[[3,2],[4,1],[6,1],[8,2],[10,1]],"108":[[1,1],[4,1],[6,1],[7,1],[11,2]],"109":[[0,1],[8,1],[11,1]],"110":[[1,1],[3,2],[4,1],[5,2],[6,1],[7,1]],"111":[[3,2],[4,1],[6,1],[8,2],[10,1]],"113":[[2,1],[5,1],[9,1]],"115":[[2,1],[5,1],[9,1]],"116":[[1,1],[3,1],[4,1],[5,1],[7,1],[11,1]],"117":[[2,1],[5,1],[9,1]],"118":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"119":[[0,1],[1,1],[2,1],[7,1],[9,1],[11,1]],"120":[[3,1],[4,1],[8,1],[11,1]],"121":[[0,1],[8,1],[11,1]],"122":[[2,1],[3,2],[4,1],[6,1],[8,1],[9,1]],"123":[[2,1],[3,2],[4,1],[6,1],[8,1],[9,1]],"124":[[1,1],[4,1],[6,1],[7,1],[11,2]],"125":[[1,1],[4,1],[6,1],[7,1],[11,2]],"126":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"127":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"14":[[3,1],[5,1],[6,1],[11,1]],"16":[[2,1],[8,1],[9,1],[10,1]],"17":[[2,1],[8,1],[9,1],[10,1]],"18":[[2,2],[3,2],[4,1],[6,1],[9,2],[10,1]],"19":[[0,1],[2,2],[3,1],[6,1],[9,2],[10,1]],"2":[[0,1],[3,1],[5,2],[6,1],[10,1]],"20":[[1,1],[2,1],[7,1],[8,1],[9,1]],"21":[[2,1],[5,1],[9,1]],"22":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"23":[[0,1],[2,2],[3,1],[6,1],[9,2],[10,1]],"25":[[2,1],[5,1],[9,1]],"26":[[2,2],[3,2],[4,1],[6,1],[9,2],[10,1]],"27":[[0,1],[2,2],[3,1],[6,1],[9,2],[10,1]],"29":[[2,1],[5,1],[9,1]],"30":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"31":[[0,1],[2,2],[3,1],[6,1],[9,2],[10,1]],"34":[[3,1],[5,1],[6,1],[11,1]],"36":[[1,1],[7,1],[10,1]],"37":[[1,1],[7,1],[10,1]],"38":[[1,1],[7,1],[10,1]],"39":[[1,1],[7,1],[10,1]],"4":[[5,1],[8,1],[10,1]],"41":[[5,1],[8,1],[10,1]],"42":[[3,2],[4,1],[6,1],[8,2],[10,1]],"43":[[0,1],[3,1],[6,1],[8,2],[10,1]],"44":[[1,1],[7,1],[10,1]],"45":[[5,1],[8,1],[10,1]],"46":[[3,2],[4,1],[6,1],[8,2],[10,1]],"47":[[0,1],[3,1],[6,1],[8,2],[10,1]],"49":[[2,1],[5,1],[9,1]],"50":[[2,1],[3,1],[6,1],[9,1],[11,1]],"51":[[2,1],[3,1],[6,1],[9,1],[11,1]],"52":[[1,1],[7,1],[10,1]],"53":[[1,1],[7,1],[10,1]],"54":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"55":[[1,1],[7,1],[10,1]],"57":[[2,1],[5,1],[9,1]],"58":[[2,1],[3,2],[4,1],[6,1],[8,1],[9,1]],"59":[[0,1],[2,1],[3,1],[6,1],[8,1],[9,1]],"6":[[1,1],[3,2],[4,1],[5,2],[6,1],[7,1]],"60":[[1,1],[7,1],[10,1]],"61":[[1,1],[7,1],[10,1]],"62":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"63":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"64":[[0,1],[5,1],[10,1],[11,1]],"65":[[4,1],[6,1],[10,1],[11,2]],"66":[[3,2],[4,1],[5,2],[6,1],[10,1]],"68":[[1,1],[3,1],[4,1],[5,1],[7,1],[11,1]],"69":[[4,1],[6,1],[10,1],[11,2]],"70":[[1,1],[3,2],[4,1],[5,2],[6,1],[7,1]],"72":[[4,1],[6,1],[10,1],[11,2]],"73":[[0,1],[8,1],[11,1]],"74":[[3,2],[4,1],[5,1],[6,1],[8,1]],"75":[[3,1],[4,1],[8,1],[11,1]],"76":[[1,1],[4,1],[6,1],[7,1],[11,2]],"77":[[0,1],[8,1],[11,1]],"78":[[1,1],[3,2],[4,1],[5,2],[6,1],[7,1]],"79":[[3,1],[4,1],[8,1],[11,1]],"80":[[4,1],[6,1],[10,1],[11,2]],"81":[[4,1],[6,1],[10,1],[11,2]],"82":[[2,2],[3,2],[4,1],[6,1],[9,2],[10,1]],"83":[[0,1],[2,2],[3,1],[6,1],[9,2],[10,1]],"84":[[1,1],[4,1],[6,1],[7,1],[11,2]],"85":[[1,1],[2,1],[3,1],[4,1],[7,1],[9,1],[11,1]],"86":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"87":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"88":[[4,1],[6,1],[10,1],[11,2]],"89":[[4,1],[5,1],[6,1],[8,1],[11,2]],"90":[[2,2],[3,2],[4,1],[6,1],[9,2],[10,1]],"91":[[2,2],[3,2],[4,1],[6,1],[9,2],[10,1]],"92":[[1,1],[4,1],[6,1],[7,1],[11,2]],"93":[[1,1],[4,1],[6,1],[7,1],[11,2]],"94":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]],"95":[[1,1],[2,2],[3,2],[4,1],[6,1],[7,1],[9,2]]},"octagon_cycles":{"11":[0,1,8,2,3,9,7,6],"114":[0,6,5,4,3,9,8,7],"35":[0,1,8,9,4,5,7,6],"71":[0,1,2,8,9,7,5,6],"97":[0,1,8,9,4,5,6,7]}}''')

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def sgn(x):return (x>0)-(x<0)
def canon(c):
    a=list(c);j=a.index(min(a));a=a[j:]+a[:j]
    b=[a[0]]+a[:0:-1]
    return min(a,b)
def family(a,b,p,q):
    return tuple(tuple(Q(t) for t in x) for x in
      ((b,0,0),(1-p,0,0),(1-p,p,0),(q,1-q,0),(0,1-q,0),
       (0,a,0),(2*a-b,b-a,0),(0,0,1),(1,0,1),(0,1,1)))
def halfspaces(a,b,p,q):
    return (((0,0,-1),0),((0,-1,0),0),((-1,-2,-b),-b),
            ((1,0,-p),1-p),((1,1,0),1),((0,1,-q),1-q),
            ((-1,0,0),0),((-1,-1,-a),-a),((0,0,1),1))
def hull2(P):
    # Exact monotone chain. Distinct generic silhouette points are retained.
    pts=sorted(set((x,y) for x,y in P))
    def cr(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>=2 and cr(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>=2 and cr(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def actual_moments(Y):
    o=tuple(sum(x[k] for x in Y)/10 for k in range(3))
    D=Q(0);J=(Q(0),)*3;cells=[]
    for fi,f in enumerate(FACES):
        for k in range(1,len(f)-1):
            ids=(f[0],f[k],f[k+1]);a,b,c=(Y[i] for i in ids)
            d=det(sub(a,o),sub(b,o),sub(c,o))
            assert d>0
            D+=d;J=add(J,mul(d,add(add(o,a),add(b,c))))
            cells.append((fi,ids,d))
    assert len(cells)==16 and D>0
    g=mul(1/(4*D),J)
    return D/6,g,cells

def main():
    assert sys.argv[1:] in (['build'],['check'])
    E=sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACES for k in range(len(f))})
    assert len(E)==17 and 10-17+9==2
    EF={e:tuple(i for i,f in enumerate(FACES) if set(e)<=set(f)) for e in E}
    assert all(len(x)==2 for x in EF.values())
    bad={int(m):c for m,c in LITERALS['infeasible_stresses'].items()}
    good={int(m):v for m,v in LITERALS['feasible_witnesses'].items()}
    assert set(bad).isdisjoint(good) and set(bad)|set(good)==set(range(128))
    certs=[];witnesses=[];counts=Counter();octagons={};oct_masks=[]
    for mask in range(128):
        ss=[1 if (mask>>i)&1 else -1 for i in range(7)]
        A=list(BASE)+[mul(ss[i],NORMAL_ROWS[i]) for i in range(7)]
        signs=[-1]+ss+[1]
        silhouette=[e for e,(f,g) in EF.items() if signs[f]!=signs[g]]
        n=len(silhouette)
        if mask in bad:
            pairs=bad[mask]
            assert 1<=len(pairs)<=7 and len({i for i,w in pairs})==len(pairs)
            assert all(0<=i<12 and isinstance(w,int) and w>0 for i,w in pairs)
            assert all(sum(w*A[i][j] for i,w in pairs)==0 for j in range(6))
            certs.append(dict(mask=mask,silhouette_edges=n,positive_zero_stress=pairs))
            continue
        v=tuple(Q(x) for x in good[mask]);a,b,p,q,u,z=v
        assert all(dot(row,v)>0 for row in A)
        assert p>0 and q>0 and p+q<1 and 0<a<1-q and a<b<min(2*a,1-p)
        Y=family(a,b,p,q);HS=halfspaces(a,b,p,q)
        for fi,(nn,h) in enumerate(HS):
            f=FACES[fi]
            assert all(dot(nn,Y[i])==h if i in f else dot(nn,Y[i])<h for i in range(10))
            for k in range(len(f)):
                x0=Y[f[k]];x1=Y[f[(k+1)%len(f)]]
                assert all(dot(nn,cross(sub(x1,x0),sub(Y[j],x0)))>0
                           for j in f if j not in (f[k],f[(k+1)%len(f)]))
        assert [sgn(dot(nn,(u,z,1))) for nn,h in HS]==signs
        volume,g,cells=actual_moments(Y)
        X=[sub(x,g) for x in Y]
        shadow=[(x[0]-u*x[2],x[1]-z*x[2]) for x in X]
        hh=hull2(shadow)
        assert len(hh)==n and n<=8
        ids=[shadow.index(x) for x in hh]
        assert all(shadow.count(x)==1 for x in hh)
        cy=canon(ids)
        assert {tuple(sorted((cy[k],cy[(k+1)%n]))) for k in range(n)}==set(silhouette)
        counts[n]+=1
        if n==8:octagons[mask]=cy;oct_masks.append(mask)
        witnesses.append(dict(mask=mask,parameters=v,volume=volume,actual_centroid=g,
                              centred_vertices=X,kernel=(u,z,1),shadow_cycle=cy,
                              shadow=shadow,positive_cone_cells=cells))
    assert len(bad)==102 and len(good)==26
    assert dict(counts)=={5:3,6:8,7:10,8:5}
    assert oct_masks==[11,35,71,97,114]
    assert octagons=={int(k):v for k,v in LITERALS['octagon_cycles'].items()}
    assert all((a^b).bit_count()!=1 for a,b in combinations(oct_masks,2))
    def enc(o):
        if isinstance(o,Q):return str(o)
        if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
        if isinstance(o,(tuple,list)):return [enc(v) for v in o]
        return o
    report=dict(identity='PRISMATOID_ALL_KERNEL_SHADOW_OCTAGON_REDUCTION_V1',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                variable_order=('a','b','p','q','u','v'),faces=FACES,edges=E,
                positive_shape_cone_rows=BASE,side_visibility_rows=NORMAL_ROWS,
                rejected=certs,feasible=witnesses,counts=dict(counts),octagon_cycles=octagons,
                scope='All open four-cut heptagon-triangle prismatoids, arbitrary affine images. Generic shadows have at most8 corners; all visibility walls have at most7 by nonadjacent octagon masks and semicontinuity. Kernels parallel to the level planes give at most4. This code proves the finite linear classification; the wall and mechanical deductions are in the accompanying theorem. It does not exclude the five octagon chambers, certify U1, or improve the global minimum bound.')
    data=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path(__file__).with_name('prism_shadow_exact.json')
    if sys.argv[1]=='check' or path.exists():assert path.read_bytes()==data
    else:path.write_bytes(data)
    print('EXACT_ALL_128_VISIBILITY_PATTERNS_CLASSIFIED 26 102')
    print('EXACT_GENERIC_CORNER_COUNTS 5:3 6:8 7:10 8:5')
    print('EXACT_FIVE_NONADJACENT_OCTAGON_CHAMBERS 11 35 71 97 114')
    print('ACTUAL_UNIFORM_CENTROIDS_AND_26_RATIONAL_SHADOW_WITNESSES_PASS')
    print('PRISMATOID_SHADOW_OCTAGON_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
