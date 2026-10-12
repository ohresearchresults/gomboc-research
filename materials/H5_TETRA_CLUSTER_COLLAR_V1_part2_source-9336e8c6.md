# material-9336e8c66e3f

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/2 — H5_TETRA_CLUSTER_COLLAR_V1
Save the complete fence as verify_h5_tetra_collar.py. Proof and manifest are in Part1. No further input or dependency is required.

```python
#!/usr/bin/env python3
"""Exact checks for H5_TETRA_CLUSTER_COLLAR_V1; Python 3.13 standard library.
The continuum proof is in the accompanying recovery material. No sampling is
used here: the finite tree identities, graph lift, and rational bounds are exact.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque
from pathlib import Path
import json

FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                     for f in FACETS for k in range(len(f))}))
CLUSTER = (0,0,0,0,0,0,0,1,2,3)
REF = ((0,0,0),(0,0,1),(1,0,1),(0,1,1))
G0 = (F(1,4),F(1,4),F(3,4))


def determinant(a):
    n=len(a)
    if n==0: return F(1)
    if n==1: return F(a[0][0])
    return sum(((-1)**j)*a[0][j]*determinant(
        [row[:j]+row[j+1:] for row in a[1:]]) for j in range(n))


def leading_minors(a):
    return [determinant([row[:k] for row in a[:k]])
            for k in range(1,len(a)+1)]


def is_tree(edges,n):
    par=list(range(n))
    def find(i):
        while par[i]!=i:
            par[i]=par[par[i]]; i=par[i]
        return i
    for a,b in edges:
        a,b=find(a),find(b)
        if a==b: return False
        par[a]=b
    return len(edges)==n-1


def orient(edges,root,n):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    parent={root:root}; todo=deque([root])
    while todo:
        a=todo.popleft()
        for b in sorted(adj[a]):
            if b not in parent: parent[b]=a;todo.append(b)
    assert len(parent)==n
    return tuple(sorted((i,p) for i,p in parent.items() if i!=root))


def prufer_tree(seq):
    n=len(seq)+2; deg=[1]*n; edges=[]
    for a in seq: deg[a]+=1
    for a in seq:
        b=next(i for i in range(n) if deg[i]==1)
        edges.append(tuple(sorted((a,b))));deg[a]-=1;deg[b]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    edges.append((a,b))
    return tuple(sorted(edges))


def scalar_form(parent):
    # y0=-(y1+y2+y3); Q=sum_i y_i*(y_i-y_parent).
    c=[[-1,-1,-1],[1,0,0],[0,1,0],[0,0,1]]
    q=[[F(0) for _ in range(3)] for _ in range(3)]
    for i,j in parent:
        d=[c[i][k]-c[j][k] for k in range(3)]
        for a in range(3):
            for b in range(3):
                q[a][b]+=F(c[i][a]*d[b]+d[a]*c[i][b],2)
    return q


def endpoint_stress(arrows):
    q=[[F(0) for _ in range(3)] for _ in range(3)]
    for i,j in arrows:
        y=[F(REF[i][k])-G0[k] for k in range(3)]
        d=[F(REF[i][k]-REF[j][k]) for k in range(3)]
        for a in range(3):
            for b in range(3): q[a][b]+=(y[a]*d[b]+d[a]*y[b])/2
    return q


def quotient_lift(arrows,root):
    # Every cluster reaches the root cluster. Reverse BFS chooses a directed
    # quotient arborescence. Each selected quotient arc retains a literal edge.
    root_c=CLUSTER[root]
    q_arcs=sorted(set((CLUSTER[i],CLUSTER[j]) for i,j in arrows
                     if CLUSTER[i]!=CLUSTER[j]))
    distance={root_c:0};todo=deque([root_c])
    while todo:
        target=todo.popleft()
        for source,t in q_arcs:
            if t==target and source not in distance:
                distance[source]=distance[target]+1;todo.append(source)
    assert len(distance)==4
    selected=[]
    for c in range(4):
        if c==root_c: continue
        candidates=[(i,j) for i,j in arrows if CLUSTER[i]==c
                    and distance[CLUSTER[j]]==distance[c]-1]
        assert candidates
        selected.append(min(candidates))
    selected=tuple(sorted(selected))
    assert len(selected)==3 and all(e in arrows for e in selected)
    return selected



# Sparse polynomials in (x,r,p,q,s), with exact rational coefficients.
def pc(a):
    return {} if a==0 else {(0,0,0,0,0):F(a)}


def pv(k):
    e=[0]*5;e[k]=1
    return {tuple(e):F(1)}


def pa(*args):
    out={}
    for a in args:
        for e,c in a.items(): out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}


def ps(a,c):
    return {e:v*c for e,v in a.items() if v*c}


def pm(*args):
    out=pc(1)
    for a in args:
        temp={}
        for e,c in out.items():
            for f,d in a.items():
                h=tuple(e[i]+f[i] for i in range(5))
                temp[h]=temp.get(h,F(0))+c*d
        out={e:c for e,c in temp.items() if c}
    return out


def pd(a,b,c):
    positive=pa(pm(a[0],b[1],c[2]),pm(a[1],b[2],c[0]),pm(a[2],b[0],c[1]))
    negative=pa(pm(a[0],b[2],c[1]),pm(a[1],b[0],c[2]),pm(a[2],b[1],c[0]))
    return pa(positive,ps(negative,-1))


def check_moment_identities():
    x,r,p,q,s=[pv(k) for k in range(5)]
    one=pc(1);lam=pa(one,ps(s,-1));zero=pc(0)
    b=((pc(F(1,4)),zero),
       (pa(one,ps(x,F(-3,4))),zero),
       (pa(one,ps(p,-1)),p),(q,pa(one,ps(q,-1))),
       (zero,pa(one,ps(r,F(-3,4)))),(zero,pc(F(1,4))),
       (pc(F(1,16)),pc(F(1,16))))
    area=zero;mx=zero;my=zero
    for i in range(7):
        a,c=b[i],b[(i+1)%7]
        cross=pa(pm(a[0],c[1]),ps(pm(a[1],c[0]),-1))
        area=pa(area,ps(cross,F(1,2)))
        mx=pa(mx,ps(pm(cross,pa(a[0],c[0])),F(1,6)))
        my=pa(my,ps(pm(cross,pa(a[1],c[1])),F(1,6)))
    A=pa(pc(F(31,64)),ps(pm(x,p),F(-3,8)),ps(pm(r,q),F(-3,8)))
    bx=pa(pc(F(509,3072)),ps(pm(x,p),F(-3,8)),ps(pm(x,x,p),F(3,32)),
          ps(pm(x,p,p),F(1,8)),ps(pm(r,q,q),F(-1,8)))
    by=pa(pc(F(509,3072)),ps(pm(r,q),F(-3,8)),ps(pm(r,r,q),F(3,32)),
          ps(pm(r,q,q),F(1,8)),ps(pm(x,p,p),F(-1,8)))
    assert (area,mx,my)==(A,bx,by)
    z=tuple((pm(s,a),pm(s,c),zero) for a,c in b)+(
        (zero,zero,one),(lam,zero,one),(zero,lam,one))
    V=zero;J=[zero,zero,zero]
    for face in FACETS:
        for k in range(1,len(face)-1):
            a,c,d=(z[i] for i in (face[0],face[k],face[k+1]))
            det=pd(a,c,d)
            V=pa(V,ps(det,F(1,6)))
            for t in range(3):
                J[t]=pa(J[t],ps(pm(det,pa(a[t],c[t],d[t])),F(1,24)))
    cx=pa(one,ps(pm(x,p),F(-3,4)))
    cy=pa(one,ps(pm(r,q),F(-3,4)))
    ev=pa(ps(pm(A,s,s),F(1,3)),ps(lam,F(1,6)))
    ex=pa(ps(pm(s,s,s,bx),F(1,4)),ps(pm(s,s,lam,cx),F(1,24)),ps(pm(lam,lam),F(1,24)))
    ey=pa(ps(pm(s,s,s,by),F(1,4)),ps(pm(s,s,lam,cy),F(1,24)),ps(pm(lam,lam),F(1,24)))
    ez=pa(ps(pm(A,s,s),F(1,12)),ps(lam,F(1,12)),ps(pm(lam,lam),F(1,24)))
    assert (V,*J)==(ev,ex,ey,ez)
    return {'basal_identities':3,'volume_and_first_moment_identities':4,
            'monomial_counts_V_J':[len(V)]+[len(v) for v in J]}


def verify():
    moment_checks=check_moment_identities()
    expected=[(14,147,1372),(14,147,700),(14,83,476),(14,83,124)]
    templates=(((1,0),(2,0),(3,0)),((1,0),(2,0),(3,1)),
               ((1,0),(2,1),(3,1)),((1,0),(2,1),(3,2)))
    g=[[F(2 if a==b else 1) for b in range(3)] for a in range(3)]
    template_minors=[]
    for parent,exp in zip(templates,expected):
        q=scalar_form(parent)
        shifted=[[8*q[a][b]-g[a][b] for b in range(3)] for a in range(3)]
        minors=leading_minors(shifted)
        assert tuple(minors)==exp
        template_minors.append([int(v) for v in minors])
    four_trees=set(prufer_tree(s) for s in product(range(4),repeat=2))
    assert len(four_trees)==16
    endpoint_forms=set()
    for tree in four_trees:
        for root in range(4):
            arrows=orient(tree,root,4)
            q=endpoint_stress(arrows)
            shifted=[[q[a][b]-(F(1,32) if a==b else 0)
                      for b in range(3)] for a in range(3)]
            assert all(v>0 for v in leading_minors(shifted))
            endpoint_forms.add(arrows)
    assert len(endpoint_forms)==64
    sigma=F(1,512)
    xy_bound=(1+2*F(1,8)+3*F(1,8)**2)/(4*(1-F(1,8)))
    z_bound=(1+F(1,8))/(4*(1-F(1,8)))
    assert xy_bound==F(83,224) and z_bound==F(9,28)
    assert xy_bound<F(1,2) and z_bound<F(1,2)
    # Thus ||g-g0|| <= sqrt(3)*s/2 < s for s<=1/8.
    margin=F(1,32)-15*sigma-12*sigma*sigma
    assert margin==F(125,65536) and margin>F(1,1024)
    volume_lower=F(511,3072)
    assert volume_lower/F(1024)>F(1,8192)
    assert len(EDGES)==17
    tree_count=0;rooted_count=0;supports=set();quotients=set()
    for edges in combinations(EDGES,9):
        if not is_tree(edges,10): continue
        tree_count+=1
        for root in range(10):
            arrows=orient(edges,root,10)
            support=quotient_lift(arrows,root)
            qp=tuple(sorted((CLUSTER[i],CLUSTER[j]) for i,j in support))
            assert qp in endpoint_forms
            supports.add(support);quotients.add(qp);rooted_count+=1
    assert tree_count==4879 and rooted_count==48790
    return {
        'claim':'H5_TETRA_CLUSTER_COLLAR_V1',
        'status':'PASS',
        'arithmetic':'Python fractions.Fraction; standard library only',
        'parameter_domain':'0<=x,r<=1; p,q>=0; p+q<=1; 511/512<=lambda<=1',
        'scope':'all nonzero PSD common metrics; actual homogeneous centroid; not whole H5 or E17',
        'template_minors':template_minors,
        'symbolic_moment_checks':moment_checks,
        'four_vertex_unrooted_trees':16,
        'four_vertex_rooted_trees':64,
        'H5_edges':[list(e) for e in EDGES],
        'H5_spanning_trees':tree_count,
        'H5_rooted_trees':rooted_count,
        'distinct_three_arrow_supports':len(supports),
        'distinct_quotient_arborescences':len(quotients),
        'coordinate_stress_margin_lower':str(margin),
        'claimed_coordinate_stress_margin':'1/1024',
        'claimed_volume_scaled_stress_margin':'1/8192',
        'global_bracket':'34<=C_min<=622; unchanged'
    }


def main():
    report=verify()
    path=Path(__file__).with_name('h5_tetra_collar_report.json')
    path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('H5_TETRA_CLUSTER_COLLAR_V1 PASS')
    print('ROOTED_TREES',report['H5_rooted_trees'])
    print('THREE_ARROW_SUPPORTS',report['distinct_three_arrow_supports'])
    print('COORDINATE_MARGIN',report['coordinate_stress_margin_lower'])


if __name__=='__main__':
    main()
```
