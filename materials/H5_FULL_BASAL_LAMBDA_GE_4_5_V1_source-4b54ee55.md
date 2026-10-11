# material-4b54ee5513f1

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_FULL_BASAL_LAMBDA_GE_4_5_V1 — exact recovery source

This is a new coordinator-authored continuous all-root exclusion for the literal H5 family. It is not an E17-wide exclusion or an attaining construction. The earlier tetrahedral cluster collar was lambda>=511/512; this source proves lambda>=4/5 for every genuine H5 body on the full x,r square and p,q triangle, under every invertible affine transformation. Thus U>=2, even when weak equilibria are allowed elsewhere. At collapsed endpoints only the polynomial matrix assertion is claimed.

## Reconstruction and evidence
Save the complete Python block as `h5_collar_weighted.py`. It is self-contained; no input file is required. Executed by the coordinator with Python 3.13.5 and NumPy 2.3.5. NumPy only adds bounded signed integer arrays; all polynomial arithmetic, coefficient conversion, and Sylvester tests use exact integers/Fractions. Float timing text is not evidence.

Command:
`OPENBLAS_NUM_THREADS=1 python h5_collar_weighted.py --s-max 1/5 --output h5_weighted_1_5_report.json`

Source: 9389 bytes, SHA-256 `18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d`.
Expected output JSON: 1186 bytes, SHA-256 `b2df636ad6d0fc9b52ca431a94367213d25b497bd0e348f69bb9621749fe30a7`.
Expected verdict PASS; 4879 unrooted / 48790 rooted trees, 260 distinct three-arrow supports, 800 exact Bernstein coefficient matrices per support, 624000 positive leading principal minors. The four possible weights are (1,1,1), (1,1,2), (1,2,1), (2,1,1), used respectively 230,10,10,10 times. The chosen support/weight list is deterministically regenerated and has SHA-256 `dfe325fbf9506329c57567096fcfb9b417206eca6ce0d70b7b7a911d5dabaa23` in the code's specified canonical JSON encoding.

Integer coefficient scale L=13271040000. Minimum leading minors are 17822592, 69930457275614976, 592113901045689421450444800. Maximum trace is 49766400000. Every scaled stress P=sym(sum w*(D zi-K)*(zi-zj)^T), D=6V, K=6J, is at least delta I, where delta=2361227178409/32768000000000000>0. This follows from lambda_min(M)>=4 det(M)/trace(M)^2 for each PD coefficient matrix and nonnegative Bernstein partition of unity.

The original geometric source and endpoint mechanism are `[internal-source-reference]` and `[internal-source-reference]`; this unit contains all literal coordinates, facets, actual moments and graph generation needed for its own computation and does not depend on those files for recovery.

## Mathematical argument
Put s=1-lambda. Coordinates and outward facet cycles are in exact_geometry/FACETS. The domain is 0<=x,r<=1, p,q>=0, p+q<=1, 0<=s<=1/5. The formula A=(31-24xp-24rq)/64 gives 7/64<=A<=31/64. Hence D=1-s+2As^2>0. Boundary tetrahedral integration verifies all four polynomial identities D=6V, K=6J. The physical center is g=K/D, never the arithmetic vertex mean.

For any rooted spanning tree of the 17-edge graph, collapse vertex labels 0,...,6 into one cluster and retain 7,8,9 as singleton clusters. Each cluster has a directed quotient path to the root cluster because the original tree does. Reverse breadth-first distances select one literal original arrow per nonroot cluster which decreases that distance. This gives three arrows, with no connected-cluster assumption. Exhaustive connected nine-edge subsets and all ten roots give the 48790 trees and 260 selected supports.

For every selected support one of the four nonnegative weight triples produces a positive definite polynomial stress on the entire domain. The exact product Bernstein basis has degrees 3 in x, 3 in r, total degree 3 on the p,q triangle, and degree 4 in u=s/(1/5): 4*4*10*5=800 matrices. The coefficient of x^a in degree 3 is binom(i,a)/binom(3,a); the triangular coefficient of p^h q^j is binom(k,h)binom(l,j)/[binom(3,h+j)binom(h+j,h)]; the s^d coefficient adds binom(m,d)/binom(4,d)*(1/5)^d. Code enforces all degree bounds, integer denominators and integer-addition safety before checking all three exact Sylvester minors of every coefficient matrix.

Let H be a common nonzero PSD metric. If all selected tree arrows satisfy (zi-g)^T H(zj-zi)>=0, then trace(H P)<=0. But P>=delta I implies trace(H P)>=delta trace(H)>0, contradiction. Thus no complete weak rooted tree exists under any such H. For an actual SPD metric, a body with just one strict unstable vertex would supply this tree: every other vertex has an adjacent weakly increasing radial derivative; the squared metric norm grows strictly along that arrow since its edge has positive metric length. Consequently all such arrows lead acyclically to the unique sink. Weak facet/edge equilibria do not invalidate this implication; weak vertex contacts allow zero first derivative but still strictly increasing squared norm. Therefore every genuine body in the stated H5 domain has at least two strict unstable vertices. A singular-coordinate endpoint remains a matrix limit, not a proper ten-vertex construction.

Global accepted 34<=C_min<=622 is unchanged. Failure of this fixed stress family outside the domain is not a feasible full rooted cone.

```python
"""Exact H5 all-tree stress certificate on a continuous five-parameter domain.

The branch is the literal heptagon/triangle family, not arbitrary E=17 types.
No floating point enters polynomial construction, Bernstein conversion or the
Sylvester tests. NumPy is used only for checked integer coefficient additions.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, math, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import numpy as np

FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),
        (9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FACETS for i in range(len(f))}))
ZERO=(0,)*5

def const(q):
    q=F(q)
    return {ZERO:q} if q else {}
def variable(k):
    e=[0]*5;e[k]=1
    return {tuple(e):F(1)}
def add(*pp):
    out={}
    for p in pp:
        for e,v in p.items():out[e]=out.get(e,F(0))+v
    return {e:v for e,v in out.items() if v}
def scale(p,a):
    return {e:v*a for e,v in p.items() if v*a}
def neg(p):return scale(p,-1)
def sub(p,q):return add(p,neg(q))
def mul(*pp):
    out=const(1)
    for p in pp:
        tmp={}
        for e,v in out.items():
            for f,w in p.items():
                g=tuple(a+b for a,b in zip(e,f));tmp[g]=tmp.get(g,F(0))+v*w
        out={e:v for e,v in tmp.items() if v}
    return out
def cross(a,b):return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]
def dot(a,b):return add(*(mul(i,j) for i,j in zip(a,b)))

def exact_geometry():
    x,r,p,q,s=[variable(k) for k in range(5)];o=const(1);z0=const(0)
    la=sub(o,s)
    B=((const(F(1,4)),z0),(sub(o,scale(x,F(3,4))),z0),(sub(o,p),p),(q,sub(o,q)),
       (z0,sub(o,scale(r,F(3,4)))),(z0,const(F(1,4))),(const(F(1,16)),const(F(1,16))))
    z=[[mul(s,b[0]),mul(s,b[1]),z0] for b in B]+[[z0,z0,o],[la,z0,o],[z0,la,o]]
    A=scale(sub(const(31),scale(add(mul(x,p),mul(r,q)),24)),F(1,64))
    bx=add(const(F(509,3072)),scale(mul(x,p),-F(3,8)),scale(mul(x,x,p),F(3,32)),scale(mul(x,p,p),F(1,8)),scale(mul(r,q,q),-F(1,8)))
    by=add(const(F(509,3072)),scale(mul(r,q),-F(3,8)),scale(mul(r,r,q),F(3,32)),scale(mul(r,q,q),F(1,8)),scale(mul(x,p,p),-F(1,8)))
    cx=sub(o,scale(mul(x,p),F(3,4)));cy=sub(o,scale(mul(r,q),F(3,4)))
    D=add(mul(la),scale(mul(A,s,s),2))
    K=[add(scale(mul(s,s,s,bx),F(3,2)),scale(mul(s,s,la,cx),F(1,4)),scale(mul(la,la),F(1,4))),
       add(scale(mul(s,s,s,by),F(3,2)),scale(mul(s,s,la,cy),F(1,4)),scale(mul(la,la),F(1,4))),
       add(scale(mul(A,s,s),F(1,2)),scale(la,F(1,2)),scale(mul(la,la),F(1,4)))]
    # Derive the same moments directly from the entire oriented boundary.
    DD={};KK=[{}, {}, {}]
    for f in FACETS:
        for k in range(1,len(f)-1):
            a,b,c=[z[i] for i in (f[0],f[k],f[k+1])]
            vol=dot(a,cross(b,c));DD=add(DD,vol)
            KK=[add(KK[j],scale(mul(vol,add(a[j],b[j],c[j])),F(1,4))) for j in range(3)]
    assert DD==D and KK==K,'The actual moments disagree with the literal boundary.'
    # The clockwise basal boundary in FACETS[0] is outward at height zero.
    # All subsequent matrix identities use D=6V and K=6J, not a vertex mean.
    return z,D,K

def orient(es,root,n=10):
    adj=[[] for _ in range(n)]
    for i,j in es:adj[i].append(j);adj[j].append(i)
    par=[None]*n;par[root]=root;queue=[root]
    for j in queue:
        for i in adj[j]:
            if par[i] is None:par[i]=j;queue.append(i)
    return tuple((i,par[i]) for i in range(n) if i!=root) if len(queue)==n else None

def quotient_lift(arrows,root):
    cl=lambda i:0 if i<7 else i-6
    cr=cl(root);back=[[] for _ in range(4)]
    for i,j in arrows:
        if cl(i)!=cl(j):back[cl(j)].append(cl(i))
    dist={cr:0};queue=[cr]
    for j in queue:
        for i in back[j]:
            if i not in dist:dist[i]=dist[j]+1;queue.append(i)
    assert len(dist)==4
    support=tuple(sorted(min((i,j) for i,j in arrows if cl(i)==a and dist[cl(j)]<dist[a]) for a in range(4) if a!=cr))
    assert len(support)==3 and set(support)<=set(arrows)
    return support

def catalogue():
    supports=set();nt=0;rows=[]
    for es in itertools.combinations(EDGES,9):
        if orient(es,0) is None:continue
        nt+=1
        for root in range(10):
            ar=orient(es,root);su=quotient_lift(ar,root);supports.add(su);rows.append((root,su))
    assert nt==4879 and len(rows)==48790 and len(supports)==260,(nt,len(rows),len(supports))
    return sorted(supports),rows

BASIS=tuple((i,j,k,l,m) for i in range(4) for j in range(4) for k in range(4) for l in range(4-k) for m in range(5))

def choose(n,k):return math.comb(n,k) if 0<=k<=n else 0

def bernstein_coefficients(poly,S,L):
    out=[0]*len(BASIS)
    for e,c in poly.items():
        a,b,h,j,d=e
        assert a<=3 and b<=3 and h+j<=3 and d<=4,e
        vx=[F(choose(i,a),choose(3,a)) for i in range(4)]
        vr=[F(choose(i,b),choose(3,b)) for i in range(4)]
        vt={(i,k):F(choose(i,h)*choose(k,j),choose(3,h+j)*choose(h+j,h)) for i in range(4) for k in range(4-i)}
        vs=[F(choose(i,d),choose(4,d))*S**d for i in range(5)]
        for k,(i,j,h,l,m) in enumerate(BASIS):
            term=c*vx[i]*vr[j]*vt[h,l]*vs[m]*L
            assert term.denominator==1,('scale insufficient',term,e)
            out[k]+=term.numerator
    return out

def matrix_polynomials(z,D,K,i,j):
    v=[sub(mul(D,z[i][a]),K[a]) for a in range(3)]
    w=[sub(z[i][a],z[j][a]) for a in range(3)]
    return [scale(add(mul(v[a],w[b]),mul(v[b],w[a])),F(1,2)) for a,b in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))]

def minors(row):
    a,b,c,d,e,f=map(int,row)
    return a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b

def run(S,output):
    start=time.monotonic();z,D,K=exact_geometry();supports,rows=catalogue()
    arrows=sorted(set(a for su in supports for a in su))
    polynomials={ar:matrix_polynomials(z,D,K,*ar) for ar in arrows}
    # Universal denominator for the chosen degree-(3,3,3,4) product basis.
    # The triangle is p>=0,q>=0,p+q<=1; only total degree <=3 is used.
    pd=math.lcm(*(c.denominator for pp in polynomials.values() for p in pp for c in p.values()))
    L=pd*648*S.denominator**4
    table={}
    for ar,pp in polynomials.items():
        cols=[bernstein_coefficients(p,S,L) for p in pp]
        coeff=np.array(cols,dtype=object).T
        largest=max(abs(int(t)) for t in coeff.flat)
        assert largest*4<2**63,('integer addition range',largest)
        table[ar]=coeff.astype(np.int64)
    print('coefficients_ready',len(arrows),len(BASIS),'scale',L,'seconds',round(time.monotonic()-start,2),flush=True)
    minimum=[None]*3;fail=[];max_trace=0;selection=[];counts={}
    choices=((1,1,1),(1,1,2),(1,2,1),(2,1,1))
    for k,su in enumerate(supports):
        chosen=None
        for weights in choices:
            coeff=sum((w*table[a] for w,a in zip(weights,su)),np.zeros((len(BASIS),6),dtype=np.int64))
            # All integer additions are safe by the input bound and sum(weights)<=4.
            leading=[minors(row) for row in coeff]
            if all(min(mm)>0 for mm in leading):
                chosen=weights;break
        if chosen is None:
            fail.append({'support_index':k,'support':su});continue
        selection.append({'support':su,'weights':chosen})
        counts[str(chosen)]=counts.get(str(chosen),0)+1
        for row,mm in zip(coeff,leading):
            for h,v in enumerate(mm):minimum[h]=v if minimum[h] is None else min(minimum[h],v)
            max_trace=max(max_trace,int(row[0])+int(row[3])+int(row[5]))
    encoded=json.dumps(selection,sort_keys=True,separators=(',',':')).encode()
    gap=F(4*minimum[2],max_trace**2*L) if not fail else None
    report={'identity':'H5_FULL_BASAL_LAMBDA_GE_4_5_V1','s_max':str(S),'lambda_min':str(1-S),
            'domain':'0<=x,r<=1; p,q>=0; p+q<=1; 0<=s<=s_max',
            'actual_moments':'D=6V, K=6J; four exact boundary polynomial identities passed',
            'unrooted_trees':4879,'rooted_trees':len(rows),'distinct_supports':len(supports),
            'literal_arrows':len(arrows),'basis_matrices_per_support':len(BASIS),
            'total_sylvester_minors':3*len(supports)*len(BASIS),'integer_matrix_scale':L,
            'minimum_integer_leading_minors':minimum,'maximum_integer_trace':max_trace,
            'uniform_scaled_stress_gap':str(gap),'weight_counts':counts,
            'selection_sha256':hashlib.sha256(encoded).hexdigest(),'failed_supports':len(fail),
            'first_failures':fail[:5],'verdict':'PASS' if not fail else 'FOUR_WEIGHT_FAMILY_TEST_FAILED',
            'limitations':['Only the literal H5 family, not all E=17 polyhedra.',
                'Collapsed shape endpoints are polynomial matrix limits, not proper ten-vertex bodies.',
                'A failed Bernstein control matrix does not show a feasible rooted cone.']}
    Path(output).write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2));print('elapsed',round(time.monotonic()-start,2))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--s-max',default='1/5');parser.add_argument('--output',default='h5_weighted_1_5_report.json');args=parser.parse_args()
    S=F(args.s_max)
    if not 0<S<1:parser.error('s-max must be strictly between zero and one')
    run(S,args.output)
```
