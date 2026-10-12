# material-e4a124f9605d

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""H5_CONDITIONED_FIVE_ARROW_EXTENSION_V1 exact actual-centroid control.
CPython 3.13.5 and SymPy 1.14.0. No inputs, solver, seed or parent files.
The general conditioned five-arrow proof is in the accompanying theorem.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

F = S.Rational
THETA = tuple(map(F, ('13/20','3/4','4/5','1/10','3/10')))
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)])))
                      for f in FACETS for i in range(len(f))}))
ARROWS = tuple(sorted(e for i,j in EDGES for e in ((i,j),(j,i))))
EF = tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f)
           for i,j in EDGES)
DUAL = tuple(sorted(e for i,j in EF for e in ((i,j),(j,i))))
PACKET = ((4,3),(5,7),(6,5),(9,4))
WEIGHTS = (1,2,3,2)
N_ROUND = S.Matrix(((229,-360,208),(-360,654,-439),(208,-439,330)))/100000
M_CONTROL = S.Matrix(((808,65,-2),(65,190,-17),(-2,-17,2)))/1000
K_CERT = S.Integer(63)


def encoded(x):
    if isinstance(x,S.MatrixBase):
        return [[str(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x,S.Basic):
        return str(x)
    if isinstance(x,dict):
        return {str(k):encoded(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encoded(v) for v in x]
    return x


def pd(A):
    m = tuple(S.factor(A[:k,:k].det()) for k in (1,2,3))
    assert all(x>0 for x in m)
    return m


def geometry():
    x,r,p,q,la=THETA
    assert 0<x<1 and 0<r<1 and p>0 and q>0 and p+q<1 and 0<la<1
    s=1-la
    B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
       (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
    z=tuple(S.Matrix((s*a,s*b,0)) for a,b in B)+(S.Matrix((0,0,1)),
        S.Matrix((la,0,1)),S.Matrix((0,la,1)))
    d=F(0);first=S.zeros(3,1);second=S.zeros(3);supports=[]
    for f in FACETS:
        a,b,c=(z[i] for i in f[:3]);n=(b-a).cross(c-a);h=n.dot(a)
        assert n!=S.zeros(3,1)
        for i in range(10):
            assert n.dot(z[i])==h if i in f else n.dot(z[i])<h
        supports.append((n,h))
        for k in range(1,len(f)-1):
            a,b,c=(z[i] for i in (f[0],f[k],f[k+1]))
            v=a.dot(b.cross(c));t=a+b+c
            d+=v;first+=v*t/4
            second+=v*(t*t.T+a*a.T+b*b.T+c*c.T)/20
    assert d>0
    g=first/d;cov=(second/d-g*g.T).applyfunc(S.factor);pd(cov)
    assert d/6==F(22241,240000)
    assert g==S.Matrix((F(18537583,142342400),F(13363403,71171200),F(37841,88964)))
    poles=tuple(n/(h-n.dot(g)) for n,h in supports)
    assert len(EDGES)==17 and len(DUAL)==34 and all(len(f)==2 for f in EF)
    assert 0<g[2]<1
    tensors={}
    for i,j in ARROWS:
        a=z[i]-g;b=z[j]-z[i]
        tensors[i,j]=(a*b.T+b*a.T)/2
    return z,d/6,g,cov,poles,tensors


def full_control(z,g,poles,tensors):
    m=M_CONTROL;n=m.inv().applyfunc(S.factor)
    assert m*n==S.eye(3)
    minors=pd(m)
    primal={e:S.factor(S.trace(m*a)) for e,a in tensors.items()}
    polar={(i,j):S.factor((poles[i].T*n*(poles[j]-poles[i]))[0])
           for i,j in DUAL}
    uu=tuple(i for i in range(10) if all(v<0 for (a,b),v in primal.items() if a==i))
    ss=tuple(i for i in range(9) if all(v<0 for (a,b),v in polar.items() if a==i))
    hh=tuple(e for e,(a,b) in zip(EDGES,EF)
             if max(primal[e],primal[e[::-1]],polar[a,b],polar[b,a])<0)
    assert len(ss)+len(uu)-len(hh)==2
    zero_count=sum(v==0 for v in primal.values())+sum(v==0 for v in polar.values())
    assert zero_count==0  # Every physical weak contact requires a zero edge primitive.
    assert (len(ss),len(uu),len(hh))==(2,3,3)
    assert all(primal[e]>0 for e in PACKET)
    assert primal[0,6]<0
    feet=tuple(g+n*q/(q.T*n*q)[0] for q in poles)
    return {'metric':m,'inverse_metric':n,'metric_leading_minors':minors,
            'packet_values':[primal[e] for e in PACKET],
            'omitted_old_five_packet_arrow_value':primal[0,6],
            'S':ss,'U':uu,'H':hh,'counts':(len(ss),len(uu),len(hh)),
            'physical_weak_count':0,'zero_primitives':zero_count,
            'primal':[(i,j,v) for (i,j),v in primal.items()],
            'polar':[(i,j,v) for (i,j),v in polar.items()],
            'raw_facet_feet':feet}


def raw_containment_count():
    counts=Counter();total=0;spanning=0
    need=set(PACKET)
    for es in combinations(EDGES,9):
        adj=[[] for _ in range(10)]
        for i,j in es:adj[i].append(j);adj[j].append(i)
        for root in range(10):
            parent={root:root};queue=[root]
            for j in queue:
                for i in adj[j]:
                    if i not in parent:parent[i]=j;queue.append(i)
            if len(parent)!=10:break
            if root==0:spanning+=1
            total+=1
            arrows={(i,parent[i]) for i in range(10) if i!=root}
            if need<=arrows:counts[root]+=1
    assert spanning==4879 and total==48790
    return {'raw_spanning_trees':spanning,'raw_rooted_trees':total,
            'containing_by_root':dict(sorted(counts.items())),
            'containing_total':sum(counts.values()),
            'scope':'Literal packet containment only, not whole-shape coverage or canonical registry subtraction.'}


def main():
    z,volume,g,cov,poles,at=geometry()
    q=-sum((w*at[e] for e,w in zip(PACKET,WEIGHTS)),S.zeros(3))
    n=N_ROUND+cov/1000;p=q+n
    np=pd(n);pp=pd(p)
    sinv=cov.inv().applyfunc(S.factor)
    gap63=S.factor(S.trace(sinv*(p-K_CERT*n)))
    gap48=S.factor(S.trace(sinv*(p-48*n)))
    assert gap63>0 and gap48>0 and q==p-n
    assert q[0,0]<0  # This stress is NOT PSD.
    assert q[2,2]>0
    critical=S.factor(S.trace(sinv*p)/S.trace(sinv*n))
    assert critical>K_CERT
    control=full_control(z,g,poles,at)
    pairing=S.factor(S.trace(q*M_CONTROL))
    assert pairing==-sum(w*v for w,v in zip(WEIGHTS,control['packet_values']))<0
    assert F(7024915,1000000)*F(6832329,1000000)<48<K_CERT
    assert F(281,40)**2<K_CERT
    counts=raw_containment_count()
    report={'identity':'H5_CONDITIONED_FIVE_ARROW_EXTENSION_V1',
            'python':sys.version.split()[0],'sympy':S.__version__,
            'theta':THETA,'vertices':z,'maximal_facets':FACETS,'true_edges':EDGES,
            'volume':volume,'actual_centroid':g,'actual_covariance':cov,
            'actual_poles':poles,'packet':PACKET,'weights':WEIGHTS,
            'stress_Q':q,'positive_part_certificate_P':p,'negative_part_certificate_N':n,
            'P_leading_minors':pp,'N_leading_minors':np,
            'condition_cap_certified':K_CERT,'dual_trace_gap_63':gap63,
            'dual_trace_gap_48':gap48,'certificate_critical_condition':critical,
            'stress_pairing_with_unrestricted_SPD_control':pairing,
            'unrestricted_SPD_control':control,'raw_tree_containment':counts,
            'scope':'The four-arrow packet is impossible for every actual covariance-weighted metric of condition <=63, but strictly feasible for the displayed unrestricted SPD metric. General conditioned five-arrow theorem is proved in the companion text. No whole-H5 or whole-shape exclusion, U1 witness, proper110 construction, or minimum-bound change.',
            'status':'PASS'}
    raw=(json.dumps(encoded(report),sort_keys=True,indent=2)+'\n').encode()
    path=Path('h5_conditioned_packet_report.json');path.write_bytes(raw)
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('CONDITION_CAP',K_CERT,'TRACE_GAP_POSITIVE',bool(gap63>0))
    print('UNRESTRICTED_CONTROL',control['counts'],'WEAK',control['physical_weak_count'])
    print('RAW_CONTAINING_TREES',counts['containing_total'])
    print('H5_CONDITIONED_FIVE_ARROW_EXTENSION_V1_PASS')


if __name__=='__main__':
    main()
