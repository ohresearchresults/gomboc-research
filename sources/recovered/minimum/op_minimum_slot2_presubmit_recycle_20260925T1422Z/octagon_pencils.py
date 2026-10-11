"""OCTAGON_COMMON_POLE_PENCILS_DEGREE4_V1.
CPython 3.13.5 / SymPy 1.14.0; assertions enabled; no external inputs.
python octagon_pencils.py build
python octagon_pencils.py check
Literal Nyhe B8_SIX_VE, NOT S1U1. Local sign-equivalence, not a parameter-box proof.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

SIG, TAU = S.symbols('sigma tau')
Q = S.Rational
V = S.Matrix
FACES = ((0,1,2,3,4,5,6,7),(0,1,8,9),(1,2,8),(2,3,8),
         (3,4,8),(4,5,8),(5,6,8),(6,7,9,8),(7,0,9))
XY = ((1,0),(1,Q(1,4)),(0,1),(-Q(1,3),1),
      (-1,0),(-1,-Q(1,2)),(0,-1),(Q(2,3),-1))
INITIAL = [V((x,y,1)) for x,y in XY] + [
    V((-Q(742,5463),Q(1901,7284),-Q(5399,1821))),
    V((Q(4222,5463),-Q(5447,7284),Q(377,1821)))]
METRIC = S.diag(Q(108626543272,1008891919),Q(417435378368,9080027271),1)
QF = V((0,0,1))


def simp(x):
    return S.cancel(x)


def vsimp(x):
    return x.applyfunc(simp)


def zero(x):
    if isinstance(x, S.MatrixBase):
        assert all(simp(t)==0 for t in x)
    else:
        assert simp(x)==0


def determinant(a,b,c):
    return a.dot(b.cross(c))


def orient(x, faces):
    c = sum(x,S.zeros(3,1))/len(x)
    ans=[]
    for f in faces:
        n=(x[f[1]]-x[f[0]]).cross(x[f[2]]-x[f[0]])
        ans.append(tuple(reversed(f)) if n.dot(c-x[f[0]])>0 else f)
    return tuple(ans)


def boundary_numerators(x,faces):
    d=0
    j=S.zeros(3,1)
    for f in faces:
        for k in range(1,len(f)-1):
            a,b,c=[x[i] for i in (f[0],f[k],f[k+1])]
            w=determinant(a,b,c)
            d+=w
            j+=w*(a+b+c)
    return simp(d),vsimp(j)


def poles(x, faces):
    return [S.Matrix.vstack(*(x[i].T for i in f[:3])).inv()*S.ones(3,1)
            for f in faces]


def polynomial(x):
    x=simp(x)
    n,d=S.fraction(x)
    assert not d.has(SIG,TAU), ('not polynomial',x)
    return S.Poly(x,SIG,TAU)


def degrees(x):
    p=polynomial(x)
    if p.is_zero:
        return [-1,-1]
    return [int(p.degree(SIG)),int(p.degree(TAU))]


def scalar(x):
    return str(S.factor(x))


def vector(x):
    return [scalar(t) for t in x]


def pdata(x):
    p=polynomial(x)
    return [[list(ij),str(c)] for ij,c in p.terms()]


def build():
    x=INITIAL
    faces=orient(x,FACES)
    ee=tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                     for f in faces for k in range(len(f))}))
    assert (len(x),len(ee),len(faces))==(10,17,9)
    base=set(range(8))
    outside={8,9}
    assert (8,9) in ee
    assert all(sum(tuple(sorted((i,w))) in ee for w in outside)==1 for i in base)
    p0=poles(x,faces)
    assert p0[0]==QF
    for f,ids in enumerate(faces):
        assert all((p0[f].dot(x[i])==1) if i in ids else (p0[f].dot(x[i])<1)
                   for i in range(10))
    d0,j0=boundary_numerators(x,faces)
    zero(j0)
    assert d0/6==Q(130321,32778)
    # Decompose from a=vertex8: a cone over F and tetrahedra (a,b,u,v).
    a,b=x[8],x[9]
    C=0
    CB=S.zeros(3,1)
    B=0
    HB=S.zeros(3,1)
    for k in range(1,7):
        u,v,w=x[0],x[k],x[k+1]
        vol=abs(determinant(u-a,v-a,w-a))/6
        C+=vol
        CB+=vol*(u+v+w)
    for f in faces[1:]:
        if 8 not in f:
            assert len(f)==3 and 9 in f
            u,v=[x[i] for i in f if i!=9]
            vol=abs(determinant(b-a,u-a,v-a))/6
            B+=vol
            HB+=vol*(u+v)
    assert C>0 and B>0 and C+B==d0/6
    zero((C+B)*a+B*b+CB+HB)
    ha=1-QF.dot(a)
    hb=1-QF.dot(b)
    da=1+SIG*ha
    db=1+SIG*hb
    W=C*db+B
    H=db*CB+HB
    DEN=S.expand(ha*db*W+B*hb*da)
    Na=vsimp(B*hb*a-ha*B*b-ha*db*H)
    Nb=vsimp((ha*b-hb*a)*W-hb*da*H)
    assert DEN.subs(SIG,0)==4*(C+B)>0
    assert all(degrees(t)[0]<=2 for t in list(Na)+list(Nb)+[DEN])
    assert all(degrees(t)[0]<=1 for t in Nb-Na)
    nums=[DEN*t for t in x[:8]]+[Na,Nb]
    moving=[vsimp(t/DEN) for t in nums]
    assert moving[8].subs(SIG,0)==a and moving[9].subs(SIG,0)==b
    # The ORIGINAL uniform solid remains actually centred for the full rational curve.
    dn,jn=boundary_numerators(nums,faces)
    zero(jn)
    assert simp(dn.subs(SIG,0)/DEN.subs(SIG,0)**3)==d0
    zero(DEN-QF.dot(Na)-4*ha*db*W)
    zero(DEN-QF.dot(Nb)-4*hb*da*W)
    # Exact pole pencils, reduced to linear numerator/denominator for the two quads.
    side={}
    actual_poles=[QF]
    quad=[]
    for f,ids in enumerate(faces[1:],start=1):
        assert len(set(ids)&base)==2
        svec=p0[f]-QF
        w=next(i for i in ids if i in outside)
        nw=nums[w]
        hw=ha if w==8 else hb
        pw=4*(db if w==8 else da)*W
        Lw=simp(svec.dot(nw)/hw)
        assert Lw.subs(SIG,0)>0 and pw.subs(SIG,0)>0
        if outside.issubset(ids):
            quad.append(f)
            pf=4*W
            lf=simp(-svec.dot(H))
            zero(pw/Lw-pf/lf)
            assert degrees(pf)[0]<=1 and degrees(lf)[0]<=1
        else:
            pf,lf=pw,Lw
        rf=vsimp(QF+(pf/lf)*svec)
        assert lf.subs(SIG,0)>0
        for i in ids:
            zero(rf.dot(moving[i])-1)
        actual_poles.append(rf)
        side[f]=(svec,pf,lf)
    assert len(quad)==2
    N=METRIC.inv()
    s=simp(QF.dot(N*QF))
    MT=METRIC+TAU*QF*QF.T
    K=N+TAU*(s*N-N*QF*QF.T*N)
    zero(MT*(K/(1+TAU*s))-S.eye(3))
    rows={}
    initial_rows={}
    for i,j in ee:
        f,h=[f for f,ids in enumerate(faces) if i in ids and j in ids]
        for u,v in ((i,j),(j,i)):
            exact=simp(moving[u].dot(MT*(moving[v]-moving[u])))
            if u in base and v in base:
                reduced=simp(x[u].dot(MT*(x[v]-x[u])))
                factor=S.Integer(1)
                kind='base_source_base'
                bound=0
            elif u in base:
                reduced=simp(x[u].dot(MT*(nums[v]-DEN*x[u])))
                factor=1/DEN
                kind='base_source_outside'
                bound=2
            else:
                reduced=simp(nums[u].dot(MT*(nums[v]-nums[u])))
                factor=1/DEN**2
                kind='outside_source_outside' if v in outside else 'outside_source_base'
                bound=3 if v in outside else 4
            zero(exact-factor*reduced)
            assert factor.subs({SIG:0,TAU:0})>0
            deg=degrees(reduced)
            assert deg[0]<=bound and deg[1]<=1
            name=f'P:{u}:{v}'
            initial_rows[name]=exact.subs({SIG:0,TAU:0})
            rows[name]=dict(edge=[i,j],kind=kind,degree=deg,
                positive_factor=scalar(factor),polynomial=pdata(reduced),
                full_rational_numerator_degree=degrees(S.fraction(exact)[0]))
        for u,v in ((f,h),(h,f)):
            exact=simp(actual_poles[u].dot(K*(actual_poles[v]-actual_poles[u]))/(1+TAU*s))
            if u==0:
                sv,pv,Lv=side[v]
                reduced=simp(QF.dot(K*sv))
                factor=pv/(Lv*(1+TAU*s))
                kind='carrier_source'
                bound=0
            elif v==0:
                su,pu,Lu=side[u]
                reduced=simp(-(QF*Lu+pu*su).dot(K*su))
                factor=pu/(Lu**2*(1+TAU*s))
                kind='carrier_target'
                bound=2
            else:
                su,_,_=side[u]
                sv,_,_=side[v]
                if i in outside and j in outside:
                    assert u in quad and v in quad
                    p=4*W
                    Lu=simp(-su.dot(H))
                    Lv=simp(-sv.dot(H))
                    kind='outside_spine'
                    bound=2
                else:
                    w=i if i in outside else j
                    assert w in outside
                    nw=nums[w]
                    hw=ha if w==8 else hb
                    p=4*(db if w==8 else da)*W
                    Lu=simp(su.dot(nw)/hw)
                    Lv=simp(sv.dot(nw)/hw)
                    kind='basal_spoke'
                    bound=4
                reduced=simp((QF*Lu+p*su).dot(K*(sv*Lu-su*Lv)))
                factor=p/(Lu**2*Lv*(1+TAU*s))
            zero(exact-factor*reduced)
            assert factor.subs({SIG:0,TAU:0})>0
            deg=degrees(reduced)
            assert deg[0]<=bound and deg[1]<=1
            name=f'Q:{u}:{v}'
            initial_rows[name]=exact.subs({SIG:0,TAU:0})
            rows[name]=dict(edge=[i,j],kind=kind,degree=deg,
                positive_factor=scalar(factor),polynomial=pdata(reduced),
                full_rational_numerator_degree=degrees(S.fraction(exact)[0]))
    assert len(rows)==68
    zeros=sorted(k for k,v in initial_rows.items() if v==0)
    assert zeros==sorted(['P:0:1','P:2:3','P:4:5','P:6:7','P:8:3','P:9:7'])
    roots={}
    for typ,size in (('P',10),('Q',9)):
        roots[typ]=[i for i in range(size)
                    if all(v<0 for k,v in initial_rows.items() if k.startswith(f'{typ}:{i}:'))]
    assert roots=={'P':[1,3,5,7],'Q':[0,7]}
    max_degrees={typ:max(v['degree'][0] for k,v in rows.items() if k.startswith(typ))
                 for typ in ('P','Q')}
    assert max_degrees=={'P':4,'Q':4}
    full_degrees={typ:max(v['full_rational_numerator_degree'][0]
                         for k,v in rows.items() if k.startswith(typ)) for typ in ('P','Q')}
    # A degree-four algebraic strip has row order eight, not a physical-packet example.
    lo=SIG**4
    hi=SIG**4/(1-SIG**4)
    mid=(lo+hi)/2
    strip=[simp(-SIG**4+mid),simp(SIG**4-(1-SIG**4)*mid)]
    assert all(S.limit(v/SIG**8,SIG,0)==Q(1,2) for v in strip)
    return dict(version=1,name='OCTAGON_COMMON_POLE_PENCILS_DEGREE4_V1',
        source_parent='asg_Nyhe15n5S0NCzWND7BzdCzUM',
        source_parent_sha256='a4bef2adf830eae50e01705edefbc80edc6388626b8e4e627efe6db99c7bb875',
        fixture='B8_SIX_VE; strict244; NOT S1U1',
        vertices=[vector(v) for v in x],faces=faces,edges=ee,
        M=[vector(METRIC.row(i)) for i in range(3)],volume=scalar(d0/6),
        constants=dict(C=scalar(C),B=scalar(B),CB=vector(CB),HB=vector(HB),ha=scalar(ha),hb=scalar(hb)),
        denominator=scalar(DEN),Na=vector(Na),Nb=vector(Nb),quad_facets=quad,
        poles=[vector(v) for v in actual_poles],rows=rows,
        zero_rows=zeros,strict_unstable=roots['P'],strict_stable=roots['Q'],
        max_sign_polynomial_sigma_degrees=max_degrees,
        max_full_rational_numerator_sigma_degrees=full_degrees,
        abstract_strip_rows=[scalar(v) for v in strip],
        allorders_bound=dict(mixed_degree=4,comparison_degree=8,
                            positive_orders=8,conditional_carrier_order=9),
        scope='Exact identity and local positive factors on one actual non-S1U1 control. General theorem is analytic. No whole-cell, feasibility or new C bound.')


def main():
    assert __debug__ and sys.version_info[:3]==(3,13,5)
    assert S.__version__=='1.14.0'
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    r=build()
    data=(json.dumps(r,sort_keys=True,indent=2)+'\n').encode()
    target=Path('octagon_pencils_report.json')
    if sys.argv[1]=='build':
        target.write_bytes(data)
    else:
        assert target.read_bytes()==data
    print('OCTAGON_COMMON_POLE_PENCILS_ALL68_SIGN_DEGREE4_PASS')
    print('REDUCED',r['max_sign_polynomial_sigma_degrees'],'RAW',r['max_full_rational_numerator_sigma_degrees'])
    for p in (Path(__file__),target):
        b=p.read_bytes()
        print(p.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':
    main()
