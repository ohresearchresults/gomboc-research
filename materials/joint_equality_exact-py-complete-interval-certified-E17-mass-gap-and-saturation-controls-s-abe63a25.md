# material-abe63a2592e8

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact recovery for JOINT_MASS_EQUALITY_AND_E17_NO_UNIFORM_GAP_V1.
python -S joint_equality_exact.py build
python -S joint_equality_exact.py check
Standard library only; assertions must remain enabled. No stochastic input.
This verifies a whole parameter interval by exact polynomial certificates.
It does not certify a Gomboc, an E17 exclusion, or a minimum complexity.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
EMAX=F(1,8)

# Polynomials are immutable tuples of rational coefficients, low degree first.
def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p) if p else (F(0),)
def pc(x):return (F(x),)
def pa(*ps):
    out=[F(0)]*max(map(len,ps),default=1)
    for p in ps:
        for i,x in enumerate(p):out[i]+=x
    return trim(out)
def ps(p,c):return trim([F(c)*x for x in p])
def pm(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return trim(out)
def pp(p,n):
    out=pc(1)
    for _ in range(n):out=pm(out,p)
    return out
def pe(p,x):
    out=F(0)
    for c in reversed(p):out=out*x+c
    return out
def psub(a,b):return tuple(pa(x,ps(y,-1)) for x,y in zip(a,b))
def pdot(a,b):return pa(*(pm(x,y) for x,y in zip(a,b)))
def pcross(a,b):
    return (pa(pm(a[1],b[2]),ps(pm(a[2],b[1]),-1)),
            pa(pm(a[2],b[0]),ps(pm(a[0],b[2]),-1)),
            pa(pm(a[0],b[1]),ps(pm(a[1],b[0]),-1)))
def pdet(a,b,c):return pdot(a,pcross(b,c))
def positive_certificate(p):
    """Certify strict positivity on 0<e<=EMAX, including all interior e."""
    p=trim(p);assert p!=(F(0),)
    order=next(i for i,x in enumerate(p) if x)
    q=p[order:];n=len(q)-1
    local=tuple(x*EMAX**i for i,x in enumerate(q))
    co=tuple(sum(local[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1))
    assert all(x>0 for x in co)
    back=[F(0)]*(n+1)
    for i,x in enumerate(co):
        for j in range(i,n+1):back[j]+=x*comb(n,i)*comb(n-i,j-i)*(-1)**(j-i)
    assert tuple(back)==local
    return {'zero_order':order,'positive_bernstein':co,'reduced_power':q}

def point_polynomials():
    e=(F(0),F(1));one=pc(1);zero=pc(0)
    e2=pp(e,2);u=pa(one,ps(e,-1));v=pa(one,ps(e,F(-1,2)))
    xy=pm(u,v)
    return [(zero,zero,zero),(zero,zero,one),(zero,one,zero),(one,zero,zero),
            (u,one,ps(u,F(-1,2))),(one,u,ps(u,F(-1,2))),
            (xy,xy,ps(xy,F(-1,2))),
            (pa(one,ps(e,F(-1,4))),pa(one,ps(e,F(-3,4))),pa(pc(F(-1,2)),ps(e,F(3,8)))),
            (xy,xy,pa(pc(F(-1,2)),ps(e,F(9,4)),ps(e2,F(-3,4)))),
            (pa(one,ps(e,F(-3,4))),pa(one,ps(e,F(-1,4))),pa(pc(F(-1,2)),ps(e,F(5,8))))]

# True hull enumeration uses every supporting plane determined by three points.
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def rank3(rows):return any(det(a,b,c) for a,b,c in combinations(rows,3))
def hull(points):
    p=list(dict.fromkeys(tuple(map(F,x)) for x in points));planes={}
    for i,j,k in combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if not any(n):continue
        vals=[dot(n,sub(x,p[i])) for x in p]
        if not (all(v>=0 for v in vals) or all(v<=0 for v in vals)):continue
        if not any(vals):continue
        if any(v<0 for v in vals):n=tuple(-x for x in n);vals=[-v for v in vals]
        planes[tuple(t for t,v in enumerate(vals) if not v)]=n
    vs=[i for i in range(len(p)) if rank3([n for face,n in planes.items() if i in face])]
    faces=sorted(set(tuple(i for i in f if i in vs) for f in planes))
    edges=sorted(set(tuple(sorted(set(f)&set(g))) for f,g in combinations(faces,2) if len(set(f)&set(g))==2))
    assert len(vs)-len(edges)+len(faces)==2
    assert all(sum(set(edge)<=set(face) for face in faces)==2 for edge in edges)
    origin=tuple(sum(p[i][k] for i in vs)/len(vs) for k in range(3))
    cycles=[];vol=F(0);moment=[F(0)]*3
    for face in faces:
        adj={i:sorted(j for j in face if i!=j and tuple(sorted((i,j))) in edges) for i in face}
        assert all(len(js)==2 for js in adj.values())
        cyc=[face[0],adj[face[0]][0]]
        while True:
            nxt=next(j for j in adj[cyc[-1]] if j!=cyc[-2])
            if nxt==cyc[0]:break
            assert nxt not in cyc
            cyc.append(nxt)
        assert len(cyc)==len(face);cycles.append(cyc)
        for j in range(1,len(cyc)-1):
            tri=[p[cyc[0]],p[cyc[j]],p[cyc[j+1]]]
            v=abs(det(*(sub(x,origin) for x in tri)))/6
            vol+=v
            for k in range(3):moment[k]+=v*(origin[k]+sum(x[k] for x in tri))/4
    assert vol>0
    return {'points':p,'vertices':vs,'facets':faces,'cycles':cycles,'edges':edges,
            'f_vector':[len(vs),len(edges),len(faces)],'V':vol,'M':tuple(moment),'g':tuple(x/vol for x in moment)}

CYCLES=((0,1,2),(0,1,3),(0,2,4,6),(0,3,5,7,6),(1,2,4,9,8),
        (1,3,5,8),(4,7,5,9),(4,6,7),(5,8,9))
FACETS=tuple(sorted(tuple(sorted(c)) for c in CYCLES))
EDGES=tuple(sorted({tuple(sorted((a,b))) for cy in CYCLES for a,b in zip(cy,cy[1:]+cy[:1])}))
ROOT=(4,5,7,9)

def family_certificate():
    p=point_polynomials();anchor=F(1,100)
    records=[]
    for inds in combinations(range(10),4):
        a,b,c,d=[p[i] for i in inds]
        poly=pdet(psub(b,a),psub(c,a),psub(d,a))
        if poly==pc(0):records.append({'indices':inds,'power':poly,'sign':0});continue
        val=pe(poly,anchor);assert val
        sign=1 if val>0 else -1
        cert=positive_certificate(ps(poly,sign))
        records.append({'indices':inds,'power':poly,'sign':sign,**cert})
    assert len(records)==210 and sum(r['sign']==0 for r in records)==15
    # The signs of all four-point determinants fix the oriented matroid.
    # Thus the complete exact hull at anchor has these same true faces throughout.
    H=hull([tuple(pe(x,anchor) for x in v) for v in p])
    assert H['f_vector']==[10,17,9]
    assert tuple(H['facets'])==FACETS and tuple(H['edges'])==EDGES
    assert tuple(tuple(x) for x in H['cycles'])==CYCLES
    assert H['vertices']==list(range(10))
    e=(F(0),F(1));ell=lambda pt:pa(pc(2),ps(e,-1),ps(pt[0],-1),ps(pt[1],-1))
    root_certs=[]
    for i,pt in enumerate(p):
        slack=ell(pt)
        if i in ROOT:assert slack==pc(0)
        else:root_certs.append({'vertex':i,'power':slack,**positive_certificate(slack)})
    # Integrate a positive fan from A=0 over the actual polygonal facets.
    V=pc(0);M=[pc(0)]*3;triangles=[]
    for cy in CYCLES:
        for j in range(1,len(cy)-1):
            ids=(cy[0],cy[j],cy[j+1]);tri=[p[i] for i in ids]
            poly=pdet(*tri)
            if poly==pc(0):continue
            sign=1 if pe(poly,anchor)>0 else -1
            cert=positive_certificate(ps(poly,sign));vol=ps(poly,F(sign,6));V=pa(V,vol)
            for k in range(3):M[k]=pa(M[k],ps(pm(vol,pa(*(pt[k] for pt in tri))),F(1,4)))
            triangles.append({'indices':ids,'orientation':sign,'volume_power':vol,**cert})
    A=(24,0,0,-32,26,-8,1)
    Z=(8,0,0,16,-22,8,-1)
    Q=(8,0,0,-4,1)
    assert V==ps(tuple(map(F,Q)),F(1,24))
    assert M[0]==M[1]==ps(tuple(map(F,A)),F(1,192))
    assert M[2]==ps(tuple(map(F,Z)),F(1,192))
    assert pa(M[0],M[2])==ps(V,F(1,2))
    J=pa(M[0],M[1]);gap=pa(ps(pm(V,V),F(3,2)),ps(V,F(1,4)),ps(J,-1))
    f1=(F(6),F(-6),F(1));f2=(F(8),F(-6),F(-2),F(1))
    assert gap==ps(pm(pp(e,3),pm(f1,f2)),F(1,384))
    B=pa(pm(pa(pc(2),ps(e,-1)),V),ps(J,-1))
    TN=pm(J,pa(pc(5),ps(e,-3)));TD=ps(pm(V,B),6)
    guards={'volume':V,'Mx':M[0],'Mz':M[2],'root_integral':B,
            'joint_integral_gap':gap,'trace_above_3_2':pa(TN,ps(TD,F(-3,2))),
            'trace_below_2':pa(ps(TD,2),ps(TN,-1)),
            'h_above_1_2':pa(pc(1),ps(V,-3))}
    guard_records={name:{'power':poly,**positive_certificate(poly)} for name,poly in guards.items()}
    # Exact limiting coefficients: gap/(2V^2) = (9/16)e^3+O(e^4).
    assert gap[:3]==(F(0),)*3 and gap[3]/(2*V[0]**2)==F(9,16)
    assert V[0]==F(1,3) and TN[0]/TD[0]==F(3,2)
    samples={}
    for ep in [F(1,10000),F(1,100),F(1,8)]:
        H=hull([tuple(pe(x,ep) for x in v) for v in p])
        assert H['f_vector']==[10,17,9] and tuple(H['facets'])==FACETS and tuple(H['edges'])==EDGES
        assert H['V']==pe(V,ep) and H['M']==tuple(pe(x,ep) for x in M)
        h=1/(6*H['V']);delta=pe(gap,ep)/(2*H['V']**2);trace=pe(TN,ep)/pe(TD,ep)
        assert 0<delta and F(1,2)<h<1 and F(3,2)<trace<2
        assert H['g'][0]==H['g'][1]>0 and H['g'][2]>0
        assert H['g'][0]+H['g'][2]==F(1,2)
        H.update(epsilon=ep,tetrahedron_fraction=h,mass_deficit=delta,trace=trace,
                 root=ROOT,stable_coordinate_facets=[(0,1,2),(0,1,3)])
        samples[str(ep)]=H
    return {'points_power':p,'four_point_determinants':records,'root_slacks':root_certs,
            'positive_fan_triangles':triangles,'facets':FACETS,'cycles':CYCLES,'edges':EDGES,
            'V_power':V,'M_power':M,'J_power':J,'gap_power':gap,
            'trace_numerator_power':TN,'trace_denominator_power':TD,'guards':guard_records,
            'samples':samples,'limit_deficit_over_epsilon_cubed':F(9,16)}

def saturation_controls():
    base=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    inputs=[(F(2),F(1),F(-1,2)),(F(7),F(2),F(-2)),(F(3,2),F(2,5),F(-1,3)),
            (F(2),F(2),F(-1)),(F(5),F(5),F(-4))]
    out=[]
    for t,r,z in inputs:
        s=t-r;assert r>0 and s>=0 and 1-t<=z<=0
        H=hull(base+[(r,s,z)]);V=H['V'];g=H['g'];h=1/t
        assert V==t/6
        assert g==((r*t+s)/(4*t),(s*t+r)/(4*t),(1+z)/4)
        d1=g[0]/(2*V);d2=g[1]/(2*V)
        assert d1+d2==3*(1+h)/4
        # Nonnegative root affine function through A,C,R: ell(B)=r, ell(D)=-z.
        ell=lambda p:r*p[2]-z*p[0]
        assert all(ell(p)>=0 for p in H['points'])
        mu=ell(g);assert mu>0
        trace=(d1*r+d2*(r-z))/(3*mu)
        cap=2-(1-h)**2
        assert trace<=cap
        if s==0 and z==1-t:assert trace==cap
        else:assert trace<cap
        H.update(parameters=(t,r,s,z),h=h,fixed_triangle_masses=(d1,d2),trace=trace,cap=cap,
                 fixed_triangles_are_actual=(s>0 and 1-t<z<0))
        out.append(H)
    return out

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def build():
    family=family_certificate();controls=saturation_controls()
    data={'identity':'JOINT_MASS_EQUALITY_AND_E17_NO_UNIFORM_GAP_V1','epsilon_domain':{'lower':0,'lower_included':False,'upper':EMAX,'upper_included':True},
          'family':family,'saturation_controls':controls,
          'scope':'Exact parameter-wide geometric controls. The E17 family has at least two stable equilibria in the displayed Euclidean metric and is not an admissible 110 construction. The equality classification and compactness separation are proved in the companion text, not inferred from finite samples.'}
    return (json.dumps(encode(data),sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'check';assert mode in ('build','check')
    raw=build();out=Path('joint_equality_exact.json')
    if mode=='build':out.write_bytes(raw)
    else:assert out.read_bytes()==raw
    obj=json.loads(raw);family=obj['family'];records=family['four_point_determinants']
    print('E17_INTERVAL_ORIENTED_MATROID_PASS',len(records),sum(x['sign']==0 for x in records),sum(x['sign']!=0 for x in records))
    print('E17_TRUE_FACETS_EDGES_PASS',10,17,9)
    print('E17_NO_UNIFORM_MASS_GAP_PASS',len(family['samples']),'9/16','at_least_two_stable')
    print('SATURATION_TRACE_CAP_CONTROLS_PASS',len(obj['saturation_controls']),2)
    print('JOINT_EQUALITY_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
