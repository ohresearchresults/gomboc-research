# material-e7d6be72dc16

AI research material

---

#!/usr/bin/env python3
"""Exact rational projective-centering window control and reusable primitives.
CPython standard library only.  Run: python projective_window.py build --output window.json
Then: python projective_window.py check --input window.json
No numeric optimizer, random seed, external file, or optional package is used.
"""
from fractions import Fraction as F
from itertools import combinations, product
import argparse
import hashlib
import json
from pathlib import Path


def vec(x):
    return tuple(F(t) for t in x)


def add(a, b):
    return tuple(x+y for x,y in zip(a,b))


def sub(a, b):
    return tuple(x-y for x,y in zip(a,b))


def scale(t, a):
    return tuple(t*x for x in a)


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def det(a):
    return dot(a[0], cross(a[1],a[2]))


def tr(a):
    return tuple(zip(*a))


def mv(a,x):
    return tuple(dot(r,x) for r in a)


def mm(a,b):
    return tuple(tuple(dot(r,c) for c in tr(b)) for r in a)


def outer(a,b):
    return tuple(tuple(x*y for y in b) for x in a)


def mscale(t,a):
    return tuple(scale(t,r) for r in a)


def madd(a,b):
    return tuple(add(r,s) for r,s in zip(a,b))


def msub(a,b):
    return tuple(sub(r,s) for r,s in zip(a,b))


I = tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
Z = (F(0),)*3
ZMAT = (Z,Z,Z)


def inv(a):
    d=det(a)
    assert d != 0
    return mscale(1/d,tr((cross(a[1],a[2]),cross(a[2],a[0]),cross(a[0],a[1]))))


def quad(a,x):
    return dot(x,mv(a,x))


def positive_definite(a):
    assert a==tr(a)
    return a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0 and det(a)>0


def oriented_facet(vertices, ids):
    ids=tuple(ids)
    a,b,c=(vertices[i] for i in ids[:3])
    n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
    assert h != 0
    if h < 0:
        ids=tuple(reversed(ids))
        a,b,c=(vertices[i] for i in ids[:3])
        n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
    q=scale(1/h,n)
    assert all(dot(q,vertices[i])==1 for i in ids)
    assert all(dot(q,x)<1 for j,x in enumerate(vertices) if j not in ids)
    for k in range(len(ids)):
        u,v,w=(vertices[ids[(k+j)%len(ids)]] for j in range(3))
        assert dot(n,cross(sub(v,u),sub(w,v)))>0
    return ids,q


def validate(vertices, facets):
    fp=[oriented_facet(vertices,f) for f in facets]
    fs=tuple(a for a,q in fp); qs=tuple(q for a,q in fp)
    assert len(set(frozenset(f) for f in fs))==len(fs)
    # Independently recover every supporting plane from actual vertex triples.
    allfacets=set()
    for i,j,k in combinations(range(len(vertices)),3):
        a,b,c=vertices[i],vertices[j],vertices[k]
        n=cross(sub(b,a),sub(c,a))
        if n==Z:
            continue
        h=dot(n,a)
        ds=[dot(n,x)-h for x in vertices]
        if all(t<=0 for t in ds) or all(t>=0 for t in ds):
            allfacets.add(frozenset(v for v,t in enumerate(ds) if t==0))
    assert allfacets==set(frozenset(f) for f in fs)
    edges={}
    for fi,f in enumerate(fs):
        for i,j in zip(f,f[1:]+f[:1]):
            edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(f)==2 for f in edges.values())
    assert len(vertices)-len(edges)+len(fs)==2
    for v in range(len(vertices)):
        assert sum(v in e for e in edges)>=3
    return fs,qs,tuple((e,tuple(edges[e])) for e in sorted(edges))


def moments(vertices, facets, derivatives=None):
    """True positive origin-fan volume, first and second moments.
    Optional derivative vectors give the exact directional derivative of V,J,g.
    """
    volume=F(0); first=Z; second=ZMAT; dv=F(0); dj=Z
    for f in facets:
        for k in range(1,len(f)-1):
            ids=(f[0],f[k],f[k+1]); a,b,c=(vertices[i] for i in ids)
            v=dot(a,cross(b,c))/6
            assert v>0
            ss=add(add(a,b),c)
            volume+=v; first=add(first,scale(v/4,ss))
            h=madd(outer(ss,ss),madd(outer(a,a),madd(outer(b,b),outer(c,c))))
            second=madd(second,mscale(v/20,h))
            if derivatives is not None:
                da,db,dc=(derivatives[i] for i in ids)
                dd=(dot(da,cross(b,c))+dot(a,cross(db,c))+dot(a,cross(b,dc)))/6
                dv+=dd
                dj=add(dj,add(scale(dd/4,ss),scale(v/4,add(add(da,db),dc))))
    g=scale(1/volume,first); W=mscale(1/volume,second)
    result=(volume,g,W)
    if derivatives is not None:
        return result,(dv,scale(1/volume,sub(dj,scale(dv,g))))
    return result


def rows(vertices, poles, edges, M):
    """Every directed true-edge escape numerator a+b.p at reference zero."""
    N=inv(M); out=[]
    for (i,j),(f,h) in edges:
        for u,v in ((i,j),(j,i)):
            x,y=vertices[u],vertices[v]
            a=dot(x,mv(M,sub(y,x)))
            b=sub(scale(dot(x,mv(M,y)),x),scale(quad(M,x),y))
            out.append(('V',u,v,a,b))
        for u,v in ((f,h),(h,f)):
            d=sub(poles[v],poles[u])
            out.append(('F',u,v,dot(poles[u],mv(N,d)),mv(N,d)))
    return tuple(out)


def census(vertices, poles, edges, M, center=Z):
    x=tuple(sub(v,center) for v in vertices)
    q=tuple(scale(1/(1-dot(a,center)),a) for a in poles)
    N=inv(M)
    assert all(1-dot(a,center)>0 for a in poles)
    ve=[[] for v in x]; fe=[[] for a in q]; hs=[]; weak=[]; vals=[]
    for (i,j),(f,h) in edges:
        p=(dot(x[i],mv(M,sub(x[j],x[i]))),dot(x[j],mv(M,sub(x[i],x[j]))),
           dot(q[f],mv(N,sub(q[h],q[f]))),dot(q[h],mv(N,sub(q[f],q[h]))))
        ve[i].append(p[0]); ve[j].append(p[1]); fe[f].append(p[2]); fe[h].append(p[3])
        vals.extend(p)
        if all(a<0 for a in p): hs.append((i,j))
        if max(p)==0: weak.append((i,j))
    S=[i for i,p in enumerate(fe) if all(a<0 for a in p)]
    U=[i for i,p in enumerate(ve) if all(a<0 for a in p)]
    return {'SUH':[len(S),len(U),len(hs)],'S':S,'U':U,'H':hs,
            'weak_edges':weak,'zero_primitives':sum(a==0 for a in vals),
            'primitive_signs':[1 if a>0 else -1 if a<0 else 0 for a in vals]}


def project(vertices, facets, p):
    assert all(1+dot(p,x)>0 for x in vertices)
    y=tuple(scale(1/(1+dot(p,x)),x) for x in vertices)
    fs,qs,es=validate(y,facets)
    return y,fs,qs,es


def window(vertices, facets, M, R, Lupper):
    fs,qs,es=validate(vertices,facets)
    V,g,W=moments(vertices,fs); Wi=inv(W)
    assert positive_definite(W) and positive_definite(M)
    L2=max(quad(Wi,x) for x in vertices)
    e2=quad(Wi,g)
    assert Lupper>0 and Lupper**2>=L2 and R>0 and R*Lupper<1
    outward=(5*R/(1+R*Lupper)**6)**2-e2
    assert outward>0
    rr=rows(vertices,qs,es,M)
    margins=[a*a-R*R*quad(Wi,b) for kind,i,j,a,b in rr]
    assert all(a!=0 for kind,i,j,a,b in rr)
    assert min(margins)>0
    return {'V':V,'g':g,'W':W,'R':R,'Lupper':Lupper,'L2':L2,'e2':e2,
            'outward_gap_squared':outward,'row_count':len(rr),
            'minimum_squared_row_gap':min(margins),
            'at_reference_zero':census(vertices,qs,es,M)}


def rootpoly(t):
    return 1360268*t**3+47133*t**2+6733200*t-20000


def data():
    xs=(F(-1),F(101,100)); sy=(F(-1),F(1))
    vertices=tuple((x,y,z) for x,y,z in product(xs,sy,sy))
    facets=((0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3))
    M=(vec((2,F(1,4),F(1,5))),vec((F(1,4),F(3,2),F(1,7))),vec((F(1,5),F(1,7),1)))
    fs,qs,es=validate(vertices,facets)
    cert=window(vertices,fs,M,F(1,400),F(301,100))
    assert cert['at_reference_zero']['SUH']==[6,8,12]
    assert cert['at_reference_zero']['zero_primitives']==0
    # Symmetries force the unique centering parameter to (t,0,0).
    # The exact first-moment numerator on that line is this irreducible cubic.
    modulus=next(p for p in (7,11,13,17,19,23,29,31,37,41,43,47)
                 if 1360268%p and all(rootpoly(F(k)).numerator%p for k in range(p)))
    lo,hi=F(0),F(1,100)
    assert rootpoly(lo)<0<rootpoly(hi)
    for step in range(90):
        mid=(lo+hi)/2
        if rootpoly(mid)<0: lo=mid
        else: hi=mid
    assert rootpoly(lo)<0<rootpoly(hi)
    # A rational point in the interval is a different explicit rational body.
    # Compute its OWN volume centroid and complete mechanical census, not zero.
    mid=(lo+hi)/2
    y,ff,qq,ee=project(vertices,fs,(mid,F(0),F(0)))
    V,g,W=moments(y,ff)
    rational_control=census(y,qq,ee,M,g)
    assert rational_control['SUH']==[6,8,12]
    assert rational_control['zero_primitives']==0 and not rational_control['weak_edges']
    # Exact differentiated actual moments test both centroid Jacobian identities.
    p=vec((F(1,50),F(-1,100),F(1,150)))
    yy,ff,qq,ee=project(vertices,fs,p)
    VV,gg,WW=moments(yy,ff); Sigma=msub(WW,outer(gg,gg))
    columns=[]
    for k in range(3):
        dy=tuple(scale(-x[k],x) for x in yy)
        _,(dv,dg)=moments(yy,ff,dy)
        assert dv==-4*VV*gg[k]
        columns.append(dg)
    Dg=tr(tuple(columns))
    assert Dg==msub(mscale(-5,Sigma),outer(gg,gg))
    d=1-dot(p,gg); r=scale(1/d,gg)
    assert d>0
    Dr=[]
    for k in range(3):
        dg=tuple(Dg[i][k] for i in range(3)); dd=-gg[k]-dot(p,dg)
        Dr.append(scale(1/(d*d),sub(scale(d,dg),scale(dd,gg))))
    Dr=tr(tuple(Dr))
    predicted=mscale(-5/d,mm(madd(I,outer(r,p)),Sigma))
    assert Dr==predicted and det(Dr)==-125*det(Sigma)/d**4
    # The affinely parametrized rows agree with physical rows, including both polar rows.
    original=rows(vertices,qs,es,M)
    actual=rows(yy,qq,ee,M)
    assert len(original)==len(actual)
    for (kind,i,j,a,b),(kk,ii,jj,value,unused) in zip(original,actual):
        assert (kind,i,j)==(kk,ii,jj)
        divisor=(1+dot(p,vertices[i]))**2*(1+dot(p,vertices[j])) if kind=='V' else F(1)
        assert value==(a+dot(b,p))/divisor
    # A deliberately large parameter tests the distinction between reference-zero and own-COM mechanics.
    pp=vec((F(3,4),0,0)); zz,ff,qq,ee=project(vertices,fs,pp)
    vlarge,glarge,wlarge=moments(zz,ff)
    reference_large=census(zz,qq,ee,M)
    own_large=census(zz,qq,ee,M,glarge)
    assert reference_large['SUH']!=own_large['SUH']
    return {'identity':'PROJECTIVE_CENTERING_WINDOW_V1','vertices':vertices,'facets':fs,
            'edges':es,'M':M,'N':inv(M),'window':cert,
            'algebraic_centering':{'polynomial_coefficients_ascending':[-20000,6733200,47133,1360268],
                'irreducible_modulus':modulus,'root_interval':[lo,hi]},
            'rational_centering_approximation':{'parameter':(mid,F(0),F(0)),'V':V,'own_g':g,
                'census':rational_control},
            'jacobian_control':{'p':p,'V':VV,'g':gg,'Sigma':Sigma,'preimage_r':r,'Dg':Dg,'Dr':Dr,'det_Dr':det(Dr)},
            'large_parameter_control':{'p':pp,'V':vlarge,'own_g':glarge,
                'reference_zero':reference_large,'own_COM':own_large},
            'checks':{'true_supports_and_maximal_facets':True,'actual_positive_fan_moments':True,
                'entire_ellipsoid_denominators':True,'entire_ellipsoid_outward_gradient':True,
                'all_48_primitives_preserved_on_ellipsoid':True,'one_reciprocal_metric':True,
                'exact_rational_control_own_COM':True,'both_centroid_Jacobians':True,
                'all_projective_row_identities':True}}


def encode(o):
    if isinstance(o,F): return str(o)
    if isinstance(o,tuple): return [encode(v) for v in o]
    if isinstance(o,list): return [encode(v) for v in o]
    if isinstance(o,dict): return {str(k):encode(v) for k,v in o.items()}
    return o


def output_bytes():
    return (json.dumps(encode(data()),sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=('build','check'))
    parser.add_argument('--output',default='window.json')
    parser.add_argument('--input',default='window.json')
    args=parser.parse_args()
    expected=output_bytes()
    if args.mode=='build':
        Path(args.output).write_bytes(expected)
        print('PROJECTIVE_WINDOW_BUILD_OK',len(expected),hashlib.sha256(expected).hexdigest())
    else:
        actual=Path(args.input).read_bytes()
        assert actual==expected, 'Stored output does not match exact reconstruction.'
        print('PROJECTIVE_WINDOW_CHECK_OK',len(actual),hashlib.sha256(actual).hexdigest())


if __name__=='__main__':
    main()
