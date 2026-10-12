# material-3d4046f897a9

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# W51_STACK424 Recovery capsule part 3/3

Complete interval certificate program. Requires both previous parts: exact_audit.py and stack_family.py with its literal W51 input. No originating sandbox is required. Save the code below as stack_interval.py (UTF-8, LF, final newline), 9833bytes, SHA-256 292afcec6c96a7bfca4d9955e40d7e8e68c982f6eda9b7a644118679be2e70e4. Python3.13.5 standard library only.

Reconstruction and exact verification command:

    python -B -S stack_interval.py stack_interval_certificate.json

Expected terminal marker:

    STACK_INTERVAL_EXACT_PASS 2973 delta 92097297554728442267067614728413760140823011800502046681/620699302727971710640470954959122086455729813942160229729936 strict [4, 2, 4] weak [0, 0, 0] zeros [0, 0, 0] Q>43/56

The output certificate is168670bytes, SHA-256 0bcda775cdf39132689f84e4cbf75052e710479047c0b682410b36c32e0aaa8f. Its exact delta is approximately0.00014837667313296644, controlled by edge_gram_39. There are2973 sign records, maximal polynomial degree8. Earlier scratch/compaction counts3109 and a different smaller delta are NOT this literal source/output; the values above are the actual regenerated certificate.

Scientific theorem: with c the original true homogeneous centroid, junior facet n.x=h, set a(t)=c+(1+t)(h-n.c)n/(n.n). For 0<t<=delta, conv(K,a(t)) at its recomputed uniform-volume centroid has V32/E90/F60,C180, strict[4,2,4], additional weak000, primitive zero000. A polar component has a witness of squared radius>14/5, all its vertices have squared radii<3, an outside elder has squared radius>4, and every edge leaving the component has radial minimum<13/20. Thus a genuine positive polar persistence bar has relative depth>1-(13/20)/(14/5)=43/56. The fixed cut is certified by evaluating a rational convex-combination point on each crossing edge, giving an upper bound for its radial minimum.

For a vertex z_i, consider max over all other genuine vertices of z_i.(z_j-z_i), normalized either by ||z_i||^2 (raw) or ||z_i||*||z_j-z_i|| (cosine). Exclude the single largest-radius vertex in each primal and polar set and sum squares of the negative parts. BOTH such losses tend to zero as t approaches0+, even though the main Q bar stays bounded below. Exact limiting witnesses verify positivity at t=0 for unchanged nonroots. The new primal apex has zero limiting gap and a nonzero limiting chord. New polar vertices have pairwise chord-squared order2 and gap order at least2, with nonzero limiting radius and support denominators; therefore their cosine deficits are O(t), and raw deficits are O(t^2). This proves noncoercivity of both zero-margin surrogates, not a global obstruction to own110 constructions or to a positive-margin acceptance test. Neither this family nor a small optimizer loss reaches the requested target. Accepted own110 C622 remains unchanged.

```python
"""Exact punctured-interval certificate for the shallow W51 stack family.
Standard library only; requires exact_audit.py and stack_family.py.
All polynomial signs are proved by a rational leading-coefficient domination bound.
Run: python -B -S stack_interval.py stack_interval_certificate.json
"""
from __future__ import annotations
from fractions import Fraction as F
from math import lcm,gcd
from pathlib import Path
import json,sys
from exact_audit import audit
from stack_family import make,POINTS,DEN

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)
def C(n):return (n,)
def A(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def N(a):return tuple(-x for x in a)
def S(a,b):return A(a,N(b))
def M(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)
def scale(n,a):return trim([n*x for x in a])
def va(a,b):return tuple(A(x,y) for x,y in zip(a,b))
def vs(a,b):return tuple(S(x,y) for x,y in zip(a,b))
def vm(s,a):return tuple(M(s,x) for x in a)
def vd(a,b):
    z=C(0)
    for x,y in zip(a,b):z=A(z,M(x,y))
    return z
def vx(a,b):return (S(M(a[1],b[2]),M(a[2],b[1])),S(M(a[2],b[0]),M(a[0],b[2])),S(M(a[0],b[1]),M(a[1],b[0])))
def ev(a,t):
    z=F(0)
    for x in reversed(a):z=z*t+x
    return z

def main():
    data,base,oldface,ap1=make(F(1));_,_,_,ap0=make(F(0))
    coords0=[tuple(F(x,DEN) for x in row) for row in POINTS]+[ap0]
    apdelta=tuple(x-y for x,y in zip(ap1,ap0))
    D=lcm(*(x.denominator for row in coords0 for x in row),*(x.denominator for x in apdelta))
    p=[tuple(C(int(x*D)) for x in row) for row in coords0]
    p[-1]=tuple((int(x*D),int(dx*D)) for x,dx in zip(ap0,apdelta))
    small,_,_,_=make(F(1,10**6));ref=audit(small['points'],small['denominator'])
    ff=[f['vertices'] for f in ref['facets']];edges=[(e['vertices'],e['owners']) for e in ref['edges']]
    vv=ref['vertices'];v6=C(0);T=(C(0),C(0),C(0));normals=[]
    for face in ff:
        if len(face)!=3:raise ValueError('Expected triangular fixed complex')
        a,b,c=[p[i] for i in face];n=vx(vs(b,a),vs(c,a));normals.append(n)
        d=vd(a,vx(b,c));v6=A(v6,d);T=va(T,vm(d,va(va(a,b),c)))
    W=scale(4,v6);Y=[vs(vm(W,a),T) for a in p]
    records=[];delta=F(1,100);worst=None
    def sign(poly,label,expected=None):
        nonlocal delta,worst
        poly=trim(poly);k=next((i for i,x in enumerate(poly) if x),None)
        if k is None:
            if expected not in (None,0):raise AssertionError((label,'unexpected zero',expected))
            records.append(dict(label=label,sign=0,order=None,degree=0));return 0
        coef=poly[k:];sg=1 if coef[0]>0 else -1
        if expected is not None and sg!=expected:raise AssertionError((label,'leading sign',sg,expected))
        den=2*sum(abs(x) for x in coef[1:]);bound=F(abs(coef[0]),den) if den else F(1)
        if bound<delta:delta=bound;worst=label
        records.append(dict(label=label,sign=sg,order=k,degree=len(poly)-1))
        return sg
    sign(v6,'positive_volume',1)
    H=[]
    for fi,(face,n) in enumerate(zip(ff,normals)):
        h=vd(n,Y[face[0]]);H.append(h);sign(h,f'positive_COM_support_{fi}',1)
        for j in range(len(p)):
            z=vd(n,vs(p[j],p[face[0]]))
            sign(z,f'hull_{fi}_{j}',0 if j in face else -1)
    signs=[[],[],[]];zeros=[0,0,0]
    for fi,(face,n) in enumerate(zip(ff,normals)):
        ss=[]
        for i,j in zip(face,face[1:]+face[:1]):ss.append(sign(N(vd(vx(n,vs(p[j],p[i])),Y[i])),f'S_{fi}_{i}_{j}'))
        signs[0].append(ss);zeros[0]+=ss.count(0)
    nbr={i:set() for i in vv}
    for (i,j),owners in edges:nbr[i].add(j);nbr[j].add(i)
    for i in vv:
        ss=[sign(N(vd(Y[i],vs(p[j],p[i]))),f'U_{i}_{j}') for j in sorted(nbr[i])]
        signs[1].append(ss);zeros[1]+=ss.count(0)
    for ei,((i,j),(a,b)) in enumerate(edges):
        e=vs(p[j],p[i]);ee=vd(e,e);ye=vd(Y[i],e);n,m=normals[a],normals[b]
        nn,mm,nm=vd(n,n),vd(m,m),vd(n,m)
        sign(S(M(nn,mm),M(nm,nm)),f'edge_gram_{ei}',1)
        vals=[N(ye),A(M(W,ee),ye),S(M(mm,vd(n,Y[i])),M(nm,vd(m,Y[i]))),S(M(nn,vd(m,Y[i])),M(nm,vd(n,Y[i])))]
        ss=[sign(z,f'H_{ei}_{j}') for j,z in enumerate(vals)];signs[2].append(ss);zeros[2]+=ss.count(0)
    strict=[sum(min(v)>0 for v in rows) for rows in signs];weak=[sum(min(v)>=0 and 0 in v for v in rows) for rows in signs]
    assert strict==[4,2,4] and weak==[0,0,0] and zeros==[0,0,0],(strict,weak,zeros)
    # Fixed retained global roots: index0 in the primal, base global stable facet in the polar.
    xr=0
    for i in vv:
        if i!=xr:sign(S(vd(Y[xr],Y[xr]),vd(Y[i],Y[i])),f'primal_global_root_{i}',1)
    baseq=[];cb=tuple(F(s) for s in base['centroid'])
    for f in base['facets']:
        n=tuple(f['normal']);hc=F(f['offset'],DEN)-sum(a*b for a,b in zip(n,cb));baseq.append(tuple(a/hc for a in n))
    rr=[sum(x*x for x in z) for z in baseq];br=max(range(len(rr)),key=rr.__getitem__)
    fmap={frozenset(f['vertices']):i for i,f in enumerate(base['facets'])};jun=fmap[frozenset({10,29,30})]
    mapping=[jun if 32 in f else fmap[frozenset(f)] for f in ff];qr=next(i for i,j in enumerate(mapping) if j==br)
    qnum=[vm(scale(D,W),n) for n in normals]
    qnorm=[vd(n,n) for n in qnum]
    for i in range(len(ff)):
        if i!=qr:sign(S(M(qnorm[qr],M(H[i],H[i])),M(qnorm[i],M(H[qr],H[qr]))),f'polar_global_root_{i}',1)
    # Barrier cut certificate: a junior component with peak >14/5, inside radii <3,
    # outside root >4, and every cut edge with minimum squared radius <13/20.
    component=set(base['Q'][0]['component']);inside={i for i,j in enumerate(mapping) if j in component}
    witness=next(i for i,j in enumerate(mapping) if j==jun)
    sign(S(scale(5,qnorm[witness]),scale(14,M(H[witness],H[witness]))),'Q_peak_above_14over5',1)
    sign(S(qnorm[qr],scale(4,M(H[qr],H[qr]))),'Q_elder_above_4',1)
    for i in inside:sign(S(scale(3,M(H[i],H[i])),qnorm[i]),f'Q_component_below_3_{i}',1)
    cut=[]
    for ei,(_,owners) in enumerate(edges):
        i,j=owners
        if (i in inside)==(j in inside):continue
        a,b=baseq[mapping[i]],baseq[mapping[j]];diff=tuple(y-x for x,y in zip(a,b));dd=sum(x*x for x in diff)
        t=max(F(0),min(F(1),-sum(x*y for x,y in zip(a,diff))/dd))
        l=t.denominator;k=t.numerator
        numerator=va(vm(scale(l-k,H[j]),qnum[i]),vm(scale(k,H[i]),qnum[j]));den=scale(l,M(H[i],H[j]))
        sign(S(scale(13,M(den,den)),scale(20,vd(numerator,numerator))),f'Q_cut_below_13over20_{ei}',1)
        cut.append(dict(edge=ei,owners=owners,base_minimizer=str(t)))
    assert cut and qr not in inside
    # Exact limiting witnesses for both raw and cosine chord-margin losses.
    # q_i = qnum_i/H_i; primal physical vectors are Y_i/(W*D).
    def order(poly):return next((i for i,a in enumerate(poly) if a),None)
    limiting=[]
    for i in vv:
        if i==xr:continue
        witnesses=[(j,vd(Y[i],vs(Y[j],Y[i]))) for j in vv if j!=i]
        if i!=32:
            j,g=next((j,g) for j,g in witnesses if g[0]>0)
            limiting.append(dict(landscape='P',vertex=i,witness=j,kind='positive_at_zero'))
        else:
            j=oldface['vertices'][0];g=vd(Y[i],vs(Y[j],Y[i]));dd=vd(vs(Y[j],Y[i]),vs(Y[j],Y[i]))
            assert g[0]==0 and dd[0]>0 and vd(Y[i],Y[i])[0]>0
            limiting.append(dict(landscape='P',vertex=i,witness=j,kind='vanishing_gap_nonzero_chord',gap_order=order(g),chord_squared_order=order(dd)))
    cluster=[i for i,face in enumerate(ff) if 32 in face]
    for i in range(len(ff)):
        if i==qr:continue
        def gap(j):return S(M(H[i],vd(qnum[i],qnum[j])),M(H[j],qnorm[i]))
        if i not in cluster:
            j=next(j for j in range(len(ff)) if j!=i and gap(j)[0]>0)
            limiting.append(dict(landscape='Q',vertex=i,witness=j,kind='positive_at_zero'))
        else:
            j=next(j for j in cluster if j!=i);g=gap(j);diff=vs(vm(H[i],qnum[j]),vm(H[j],qnum[i]));dd=vd(diff,diff)
            assert order(dd)==2 and (order(g) is None or order(g)>=2) and qnorm[i][0]>0 and H[i][0]>0 and H[j][0]>0
            limiting.append(dict(landscape='Q',vertex=i,witness=j,kind='coalescing_polar_pair',gap_order=order(g),chord_squared_order=order(dd)))
    cert=dict(interval='0 < t <= delta',delta=str(delta),delta_float=float(delta),controlling_polynomial=worst,
        V=32,E=90,F=60,C=180,strict=strict,additional_weak=weak,primitive_zero=zeros,
        Q_lower_bound='43/56',Q_lower_bound_float=43/56,Q_cut=cut,polar_component=sorted(inside),
        primal_global_root=xr,polar_global_root=qr,polynomial_count=len(records),max_degree=max(r['degree'] for r in records),sign_records=records,
        proof_rule='For p=t^m(a0+...+ak*t^k), delta<=1 and delta<=abs(a0)/(2*sum(abs(aj),j>=1)) imply sign(p)=sign(a0) on 0<t<=delta. Zero polynomials are explicitly recorded.',
        centroid_rule='Coordinates polynomial of degree1; W=4*sum det, T=sum det*(a+b+c), Y_i=W*p_i-T. All denominator factors W,D,H_i are positive.',
        limiting_witnesses=limiting,surrogate_limit='Exact limiting witnesses establish that both raw-radius-normalized and cosine-normalized zero-margin squared positive-part losses tend to zero. All pre-existing nonroot escape witnesses remain positive. The new primal apex has an old-face chord with limiting zero numerator. Each new polar vertex has a cluster chord with squared length of order t^2 and gap numerator of order at least t^2. Hence zero-margin raw squared positive-part losses tend to zero while Q>43/56. No claim of own110.')
    Path(sys.argv[1]).write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n')
    print('STACK_INTERVAL_EXACT_PASS',len(records),'delta',delta,'strict',strict,'weak',weak,'zeros',zeros,'Q>43/56')
if __name__=='__main__':main()
```
