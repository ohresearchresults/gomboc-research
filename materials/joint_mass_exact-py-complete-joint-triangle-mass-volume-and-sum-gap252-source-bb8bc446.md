# material-bb8bc446bbb0

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact controls and finite algebra for a coupled true-triangle mass bound.
Reconstruct: python -S joint_mass_exact.py build
Verify:      python -S joint_mass_exact.py check
Only the Python standard library is used. Assertions must be enabled.
The universal continuous proof is in the accompanying immutable material.
This finite program does not prove equilibrium-class exclusions or a minimum.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
KAPPA, TAU, HCAP = F(203,100), F(51,25), F(25,26)
ZERO=(0,0,0)
ONE={ZERO:F(1)}

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def scale(p,a): return {k:F(a)*v for k,v in p.items() if a*v}

def mul(p,q):
    out={}
    for a,u in p.items():
        for b,v in q.items():
            k=tuple(x+y for x,y in zip(a,b))
            out[k]=out.get(k,F(0))+u*v
    return {k:v for k,v in out.items() if v}

def power(p,n):
    out=ONE
    for _ in range(n): out=mul(out,p)
    return out

def substitute(p,variables):
    out={}
    for exponents,a in p.items():
        term=ONE
        for variable,n in zip(variables,exponents): term=mul(term,power(variable,n))
        out=add(out,scale(term,a))
    return out

def value(p,x): return sum(a*x[0]**i*x[1]**j*x[2]**k for (i,j,k),a in p.items())

def polynomials():
    b,c,d=({(1,0,0):F(1)},{(0,1,0):F(1)},{(0,0,1):F(1)})
    q=add(ONE,b);q1=add(q,c);q2=add(q,d)
    u=add(ONE,scale(c,-1));v=add(ONE,scale(d,-1));w=mul(u,v)
    delta=scale(add(ONE,scale(w,-1)),10353)
    p1=add(scale(mul(q,mul(w,v)),5100),delta,scale(q1,-5075))
    p2=add(scale(mul(q,mul(w,u)),5100),delta,scale(q2,-5075))
    q1h=add(scale(p1,26),scale(p2,25),scale(delta,-25))
    qh1=add(scale(p1,25),scale(p2,26),scale(delta,-25))
    # Direct expansion of the new two mixed-vertex polynomials.
    explicit0={(0,0,0):1275,(0,1,0):-250372,(0,0,1):-250397,
               (0,2,0):127500,(0,0,2):132600,(0,1,1):251022,
               (0,2,1):-127500,(0,1,2):-132600}
    explicit1={(0,0,0):2550,(0,1,0):-637972,(0,0,1):-643097,
               (0,2,0):255000,(0,0,2):265200,(0,1,1):771222,
               (0,2,1):-255000,(0,1,2):-265200}
    assert substitute(q1h,[{},c,d])==explicit0
    assert substitute(q1h,[ONE,c,d])==explicit1
    assert substitute(q1h,[b,d,c])==qh1
    return {'P1':p1,'P2':p2,'Q1h':q1h,'Qh1':qh1}

def bernstein_check(p,degrees):
    assert all(all(e<=n for e,n in zip(ex,degrees)) for ex in p)
    indices=list(product(*(range(n+1) for n in degrees)))
    co={}
    for i in indices:
        total=F(0)
        for e,a in p.items():
            if all(x<=y for x,y in zip(e,i)):
                term=a
                for ii,ee,nn in zip(i,e,degrees): term*=F(comb(ii,ee),comb(nn,ee))
                total+=term
        co[i]=total
    back={}
    for i,a in co.items():
        for e in product(*(range(ii,nn+1) for ii,nn in zip(i,degrees))):
            term=a
            for ii,ee,nn in zip(i,e,degrees): term*=comb(nn,ii)*comb(nn-ii,ee-ii)*(-1)**(ee-ii)
            back[e]=back.get(e,F(0))+term
    assert {e:a for e,a in back.items() if a}==p
    return co

def finite_certificates():
    b,t,u=({(1,0,0):F(1)},{(0,1,0):F(1)},{(0,0,1):F(1)})
    ps=polynomials(); records={}
    subvars=[b,scale(mul(t,u),F(1,252)),scale(mul(t,add(ONE,scale(u,-1))),F(1,252))]
    for name,p in ps.items():
        local=substitute(p,subvars)
        co=bernstein_check(local,(1,3,3))
        assert len(co)==32 and all(a>0 for a in co.values())
        records[name]={'power':[[*e,a] for e,a in sorted(p.items())],
                       'local_power':[[*e,a] for e,a in sorted(local.items())],
                       'bernstein':[[*e,a] for e,a in sorted(co.items())],
                       'minimum':min(co.values())}
    f=lambda s: F(2550)-643097*s+265200*s*s
    assert f(F(1,252))==F(11663,5292)>0
    assert f(F(1,251))==F(-499597,63001)<0
    assert 643097**2-4*265200*2550==410868711409
    assert HCAP==1/(TAU-1)
    # Exact algebra of the positive remainder at b=1, with s=c+d.
    c,d=({(0,1,0):F(1)},{(0,0,1):F(1)})
    s=add(c,d);p=mul(c,d)
    fpoly=add(scale(ONE,2550),scale(s,-643097),scale(power(s,2),265200))
    remainder=add(mul(c,add(scale(ONE,5125),scale(c,-10200))),
                  mul(p,add(scale(ONE,240822),scale(c,-255000),scale(d,-265200))))
    assert substitute(ps['Q1h'],[ONE,c,d])==add(fpoly,remainder)
    return records

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def rank3(rows): return any(det(a,b,c)!=0 for a,b,c in combinations(rows,3))

def hull(points):
    """Enumerate true support facets/edges; integrate a positive fan from A=0."""
    p=[tuple(map(F,x)) for x in points]
    assert p[0]==(0,0,0) and len(set(p))==len(p)
    candidates={}
    for i,j,k in combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if n==(0,0,0): continue
        vals=[dot(n,sub(x,p[i])) for x in p]
        if not (all(v>=0 for v in vals) or all(v<=0 for v in vals)): continue
        if all(v==0 for v in vals): continue
        if any(v<0 for v in vals): n=tuple(-v for v in n);vals=[-v for v in vals]
        candidates[tuple(t for t,v in enumerate(vals) if v==0)]=n
    verts=[i for i in range(len(p)) if rank3([n for f,n in candidates.items() if i in f])]
    vset=set(verts)
    facets=sorted(set(tuple(i for i in f if i in vset) for f in candidates))
    assert all(len(f)>=3 for f in facets)
    edges=sorted(set(tuple(sorted(set(f)&set(g))) for f,g in combinations(facets,2) if len(set(f)&set(g))==2))
    assert len(verts)-len(edges)+len(facets)==2
    assert all(sum(set(e)<=set(f) for f in facets)==2 for e in edges)
    cycles=[];vol=F(0);moment=[F(0)]*3
    for facet in facets:
        adj={i:sorted(j for j in facet if i!=j and tuple(sorted((i,j))) in edges) for i in facet}
        assert all(len(js)==2 for js in adj.values())
        cyc=[facet[0],adj[facet[0]][0]]
        while True:
            nxt=next(j for j in adj[cyc[-1]] if j!=cyc[-2])
            if nxt==cyc[0]: break
            assert nxt not in cyc
            cyc.append(nxt)
        assert len(cyc)==len(facet)
        cycles.append(cyc)
        for j in range(1,len(cyc)-1):
            tri=[p[cyc[0]],p[cyc[j]],p[cyc[j+1]]]
            v=abs(det(*tri))/6
            vol+=v
            for k in range(3): moment[k]+=v*sum(t[k] for t in tri)/4
    assert vol>0
    return {'points':p,'vertices':verts,'facets':facets,'cycles':cycles,'edges':edges,
            'f_vector':[len(verts),len(edges),len(facets)],'V':vol,'moment':moment,
            'g':tuple(x/vol for x in moment)}

def evaluate(points,ell=None):
    H=hull(points);V=H['V'];g=H['g'];p=H['points']
    assert (0,1,2) in H['facets'] and (0,1,3) in H['facets']
    assert (0,1) in H['edges']
    assert p[:4]==[(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0))]
    h=F(1,6)/V;m1=g[0]/(2*V);m2=g[1]/(2*V)
    J=H['moment'][0]+H['moment'][1]
    gap=F(3,2)*V*V+V/4-J
    assert 0<h<=1 and 0<m1<=F(3,4) and 0<m2<=F(3,4) and gap>=0
    assert F(3,4)*(1+h)-m1-m2==gap/(2*V*V)
    H.update(tetrahedron_volume=F(1,6),tetrahedron_fraction=h,masses=(m1,m2),joint_moment_margin=gap)
    if ell is not None:
        ell=tuple(map(F,ell));slack=lambda x: ell[0]+dot(ell[1:],x)
        assert ell[0]==1 and all(slack(x)>=0 for x in p)
        root=tuple(i for i in H['vertices'] if slack(p[i])==0)
        assert root in H['facets'] and not ({0,1}&set(root))
        b,c,d=map(slack,(p[1],p[2],p[3]));assert 0<b<=1
        mu=slack(g);assert mu>0
        T=(m1*(1+b+c)+m2*(1+b+d))/(3*mu)
        assert mu>=h*(1+b+c+d)/4
        assert T<=1/h+(1+b)/(1+b+c+d)<=1+1/h
        H.update(ell=ell,root=root,gaps=(b,c,d),mu=mu,trace=T,
                 tetrahedron_trace_bound=1/h+(1+b)/(1+b+c+d))
    return H

def controls():
    base=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    out={'tetrahedron':evaluate(base)}
    assert out['tetrahedron']['joint_moment_margin']==0
    for T in [F(3,2),F(2),F(7),F(101,3)]:
        rho=F(2,5);z=-(T-1)/3
        H=evaluate(base+[(rho*T,(1-rho)*T,z)])
        assert H['f_vector']==[5,9,6]
        assert H['V']==T/6 and sum(H['moment'][:2])==T*(T+1)/24
        assert sum(H['masses'])==3*(T+1)/(4*T)
        assert H['joint_moment_margin']==0
        out['sharp_T_'+str(T)]=H
    # Root-disjoint, genuinely triangular control inherited by its full literal generator.
    b,c,d=F(1,4),F(1,300),F(1,3000)
    ell=(F(1),d-1,c-1,b-1);z=F(2,9);eps=F(1,1000)
    R1=((1-(1-b)*z-(1-c)*eps)/(1-d),eps,z)
    R2=(eps,(1-(1-b)*z-(1-d)*eps)/(1-c),z)
    z3=z+F(1,100000);t3=(1-(1-b)*z3)/(2-c-d)
    H=evaluate(base+[R1,R2,(t3,t3,z3)],ell)
    assert H['f_vector']==[7,15,10]
    assert H['trace']==F(6351293107535193486070764313536,3134004167240577467178194614243)
    assert 2<H['trace']<TAU and c+d<F(1,252) and c>F(1,504)
    assert H['joint_moment_margin']>0
    out['asymmetric_root_disjoint']=H
    # A false proposed pointwise fan estimate: sum of t over every opposite
    # boundary triangle need NOT be at most 6*V+1. This is not used in the proof.
    eps=F(1,100)
    H=evaluate(base+[(2,2,-1),(2+eps,2-eps,-1),(2,2,-1+eps)],(1,F(-1,4),F(-1,4),0))
    assert H['root']==(4,5,6)
    facet_t_sum=sum(sum(H['points'][i][:2]) for i in H['root'])
    assert facet_t_sum>6*H['V']+1 and H['joint_moment_margin']>0
    H['false_pointwise_fan_estimate_excess']=facet_t_sum-(6*H['V']+1)
    out['pointwise_fan_ansatz_counterexample']=H
    return out

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(t) for t in x]
    return x

def build():
    data={'identity':'ACTUAL_ADJACENT_TRIANGLE_JOINT_MASS_VOLUME_V1',
          'kappa':KAPPA,'tau':TAU,'high_trace_tetrahedron_fraction_cap':HCAP,
          'rational_sum_gap_threshold':F(1,252),'implied_max_gap_threshold':F(1,504),
          'algebraic_threshold_polynomial':[2550,-643097,265200],
          'algebraic_threshold_discriminant':410868711409,
          'certificates':finite_certificates(),'controls':controls(),
          'scope':'Exact finite checks and true-volume controls supporting the separate continuous proof. No sampled infeasibility, equilibrium exclusion, or exact minimum is asserted.'}
    return (json.dumps(encode(data),sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'check'
    assert mode in ('build','check')
    out=Path('joint_mass_exact.json');raw=build()
    if mode=='build': out.write_bytes(raw)
    else: assert out.read_bytes()==raw
    obj=json.loads(raw)
    print('JOINT_MASS_VOLUME_EXACT_CONTROLS_PASS',len(obj['controls']),5)
    print('SUM_GAP_252_EXACT_BERNSTEIN_PASS',4,128,128)
    print('POINTWISE_FAN_BOUND_EXACTLY_REFUTED',obj['controls']['pointwise_fan_ansatz_counterexample']['false_pointwise_fan_estimate_excess'])
    print('JOINT_MASS_VOLUME_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
