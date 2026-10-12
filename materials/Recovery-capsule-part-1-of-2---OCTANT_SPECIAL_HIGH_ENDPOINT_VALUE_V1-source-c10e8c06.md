# material-c10e8c06deef

AI research material

---

#!/usr/bin/env python3
"""OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1.
Exact symbolic certificate and actual rational controls, no external input.
CPython 3.13.5, SymPy 1.14.0; assertions must remain enabled.
The certificate proves T <= 3/2 for the stated seven-parameter corner-cut
family. Applying it to stationary S5/I4/I5 uses the analytic reduction
in the accompanying proof, not an inference from the finite controls.
"""
from itertools import combinations
from functools import cmp_to_key
from pathlib import Path
from math import comb
import hashlib
import json
import sys
import sympy as S

assert __debug__


def dump(path, obj):
    raw=(json.dumps(obj, sort_keys=True, ensure_ascii=True, separators=(',', ':'))+'\n').encode()
    Path(path).write_bytes(raw)
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def symbolic_family():
    b,c,d,u,v,t,z=S.symbols('b c d u v t z')
    alpha=1-b
    Delta=b*c*(v-u)+d*((c-b)*u+b*(1-v+u))
    A=S.zeros(3,1);B=S.Matrix([0,0,1]);C=S.Matrix([0,1,0]);D=S.Matrix([1,0,0])
    U=S.Matrix([0,u,(1+(c-1)*u)/alpha])
    R=S.Matrix([0,v,(1+(c-1)*v)/alpha])
    W=S.Matrix([b*c*(v-u)/Delta,
                d*u*((c-b)*v+b)/Delta,
                d*((c-b)*u+b)*(1+(c-1)*v)/(alpha*Delta)])
    beta=-(b+(c-1)*u)/(alpha*u)
    kappa=alpha*(1-v)/(1+(c-1)*v)
    ell=lambda p:1+(d-1)*p[0]+(c-1)*p[1]+(b-1)*p[2]
    nn=lambda p:(1+b+c)*p[0]+(1+b+d)*p[1]
    for p in (U,R,W): assert S.factor(ell(p))==0
    assert S.factor(1-W[0]-beta*W[1]-W[2])==0
    assert S.factor(1-W[0]-W[1]-kappa*W[2])==0
    pts=[A,B,C,D,U,W,R]
    tetra=[(1,0,2,3),(1,4,5,6),(1,2,5,6)]
    tetra=[(1,0,2,3),(1,4,5,6),(1,2,3,5),(1,2,5,6)]
    signs=[1,1,-1,-1]
    V=S.Integer(0);J=S.zeros(3,1);pieces=[]
    for ids,sign in zip(tetra,signs):
        pp=[pts[i] for i in ids]
        w=S.factor(sign*S.det(S.Matrix.hstack(*(p-pp[0] for p in pp[1:])))/6)
        V+=w;J+=w*sum(pp,S.zeros(3,1))/4;pieces.append(w)
    V=S.factor(V);J=J.applyfunc(S.factor)
    E=S.factor(V+S.Matrix([d-1,c-1,b-1]).dot(J))
    N=S.factor(S.Matrix([1+b+c,1+b+d,0]).dot(J))
    # The cut removes exactly the tetrahedron B,U,U_t,V_z.
    Ut=U+t*(R-U);Vz=U+z*(W-U)
    vc=S.factor(t*z*pieces[1])
    Jcut=vc*(B+U+Ut+Vz)/4
    assert S.factor(vc+S.Matrix([d-1,c-1,b-1]).dot(Jcut)-b*vc/4)==0
    nc=vc*(nn(U)+nn(Ut)+nn(Vz))/4
    assert S.factor(S.Matrix([1+b+c,1+b+d,0]).dot(Jcut)-nc)==0
    Vcut=S.factor(V-vc);Ecut=S.factor(E-b*vc/4);Ncut=S.factor(N-nc)
    multiplier=48*alpha**2*Delta**2
    gap=S.cancel(multiplier*(9*Vcut*Ecut-Ncut))
    num,den=S.fraction(gap);assert den==1
    poly=S.Poly(num,b,c,d,u,v,t,z,domain=S.ZZ)
    assert len(poly.terms())==502
    return {'vars':(b,c,d,u,v,t,z),'points':pts,'Ut':Ut,'Vz':Vz,
            'V':Vcut,'E':Ecut,'N':Ncut,'J':(J-Jcut).applyfunc(S.factor),
            'gap':poly,'Delta':Delta,'beta':beta,'kappa':kappa}


def certificate(fam):
    b,c,d,u,v,t,z=fam['vars']
    B,C,D,F,R,T,Z=S.symbols('B C D F R T Z')
    # Homogeneous Bernstein certificate: b in [0,1], c>=1, d>=0,
    # u=v*f with f in [0,1], v in [0,2], t,z in [0,1].
    base=S.Poly(S.expand(fam['gap'].as_expr().subs({c:1+C,u:v*F})),b,C,d,F,v,t,z)
    deg=base.degree_list()
    expr=sum(k*B**p[0]*(1+B)**(deg[0]-p[0])*C**p[1]*D**p[2]
             *F**p[3]*(1+F)**(deg[3]-p[3])*(2*R)**p[4]*(1+R)**(deg[4]-p[4])
             *T**p[5]*(1+T)**(deg[5]-p[5])*Z**p[6]*(1+Z)**(deg[6]-p[6])
             for p,k in base.terms())
    cert=S.Poly(S.expand(expr),B,C,D,F,R,T,Z,domain=S.ZZ)
    assert len(cert.terms())==12258 and min(cert.coeffs())>0
    # Leading homogeneous faces represent the closed t=1 and z=1 limits.
    for index,degree in ((5,deg[5]),(6,deg[6])):
        face=[k for powers,k in cert.terms() if powers[index]==degree]
        assert face and min(face)>0
    record={'variables':['B','C','D','F','R','T','Z'],
            'substitutions':{'b':'B/(1+B)','c':'1+C','d':'D',
                             'u':'2*R*F/((1+R)*(1+F))','v':'2*R/(1+R)',
                             't':'T/(1+T)','z':'Z/(1+Z)'},
            'homogenizing_degrees':list(deg),
            'positive_terms':len(cert.terms()),
            'minimum_coefficient':str(min(cert.coeffs())),
            'terms':[[list(p),str(k)] for p,k in cert.terms()]}
    return record


def order_face(points, ids, normal):
    omit=next(i for i in range(3) if normal[i]!=0)
    axes=[i for i in range(3) if i!=omit]
    center=[sum(points[i][k] for i in ids)/len(ids) for k in axes]
    vec={i:tuple(points[i][k]-center[j] for j,k in enumerate(axes)) for i in ids}
    def half(v):return 1 if v[1]<0 or (v[1]==0 and v[0]<0) else 0
    def cmp(i,j):
        a,b=vec[i],vec[j]
        if half(a)!=half(b):return -1 if half(a)<half(b) else 1
        q=a[0]*b[1]-a[1]*b[0]
        return -1 if q>0 else (1 if q<0 else 0)
    return tuple(sorted(ids,key=cmp_to_key(cmp)))


def exact_hull(points):
    found={}
    for i,j,k in combinations(range(len(points)),3):
        n=(points[j]-points[i]).cross(points[k]-points[i])
        if n==S.zeros(3,1):continue
        vals=[S.expand(n.dot(p-points[i])) for p in points]
        if min(vals)<0<max(vals):continue
        face=frozenset(j for j,x in enumerate(vals) if x==0)
        found.setdefault(face,n)
    faces=sorted([order_face(points,list(ids),n) for ids,n in found.items()])
    edges=sorted({tuple(sorted((f[j-1],f[j]))) for f in faces for j in range(len(f))})
    assert set(edges)=={tuple(sorted(f&g)) for f,g in combinations(found,2) if len(f&g)==2}
    assert len(points)-len(edges)+len(faces)==2
    def fan(apex):
        V=S.Integer(0);J=S.zeros(3,1)
        for f in faces:
            if apex in f:continue
            for j in range(1,len(f)-1):
                ids=(apex,f[0],f[j],f[j+1]);pp=[points[i] for i in ids]
                w=abs(S.det(S.Matrix.hstack(*(p-pp[0] for p in pp[1:]))))/6
                assert w>0
                V+=w;J+=w*sum(pp,S.zeros(3,1))/4
        return V,J
    V,J=fan(0);assert (V,J)==fan(1)
    return faces,edges,V,J


def controls(fam):
    b,c,d,u,v,t,z=fam['vars'];Q=S.Rational
    fixed={b:Q(1,5),c:Q(6,5),d:Q(1,100),u:Q(5,11),v:Q(35,41)}
    answer=[]
    for name,tt,zz,fvector in [('S5',0,0,[7,11,6]),('I5',Q(1,2),Q(1,2),[8,13,7]),('I4',1,Q(1,2),[7,12,7])]:
        sub={**fixed,t:tt,z:zz}
        original=[p.subs(sub) for p in fam['points']]
        pp=original[:4]+([original[4],original[5],original[6]] if name=='S5'
             else [fam['Ut'].subs(sub),fam['Vz'].subs(sub),original[5],original[6]])
        points=[]
        for p in pp:
            if p not in points:points.append(p)
        faces,edges,V,J=exact_hull(points)
        assert [len(points),len(edges),len(faces)]==fvector
        assert V==fam['V'].subs(sub) and J==fam['J'].subs(sub)
        E=V+S.Matrix([fixed[d]-1,fixed[c]-1,fixed[b]-1]).dot(J)
        N=S.Matrix([1+b+c,1+b+d,0]).subs(sub).dot(J)
        assert E==fam['E'].subs(sub) and N==fam['N'].subs(sub)
        trace=S.factor(N/(6*V*E));assert trace<Q(3,2)
        ell=[1+(fixed[d]-1)*p[0]+(fixed[c]-1)*p[1]+(fixed[b]-1)*p[2] for p in points]
        gg=[(1+fixed[b]+fixed[c])*p[0]+(1+fixed[b]+fixed[d])*p[1]-N/V-(N/E)*e for p,e in zip(points,ell)]
        assert gg[2]<0<gg[3] and min(gg[4:])<0
        answer.append({'name':name,'parameters':{str(k):str(x) for k,x in sub.items()},
                       'f_vector':fvector,'vertices':[[str(x) for x in p] for p in points],
                       'facets':[list(f) for f in faces],'edges':[list(e) for e in edges],
                       'V':str(V),'J':[str(x) for x in J],'g':[str(x/V) for x in J],
                       'E':str(E),'N':str(N),'T':str(trace),'ell':list(map(str,ell)),'G':list(map(str,gg)),
                       'status':'actual mixed-sign uniform geometry; fails auxiliary-G positivity; no mechanical 110 claim'})
    return answer


def sharp_limit(fam):
    b,c,d,u,v,t,z=fam['vars'];e=S.symbols('e',positive=True)
    sub={b:e,c:1,d:e,u:e,v:2*e,t:0,z:0}
    trace=S.factor((fam['N']/(6*fam['V']*fam['E'])).subs(sub))
    assert S.limit(trace,e,0,dir='+')==S.Rational(3,2)
    return {'family':'b=d=u=e,c=1,v=2e,t=z=0, 0<e<1/4',
            'T':str(trace),'limit':'3/2','status':'sharp for the stated geometric family, not for stationary bodies'}


def main():
    fam=symbolic_family();cert=certificate(fam)
    cp=dump('octant_special_high_endpoint_v1.coefficients.json',cert)
    report={'theorem':'OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1','bound':'T<=3/2',
            'symbolic_gap_terms':len(fam['gap'].terms()),
            'positive_coefficients':cert['positive_terms'],
            'coefficient_file':cp,'controls':controls(fam),'sharp_limit':sharp_limit(fam),
            'evidence':'exact rational algebra and positive-coefficient certificate; analytic applicability in proof'}
    rp=dump('octant_special_high_endpoint_v1.report.json',report)
    print('EXACT_ROOT_COORDINATES_AND_SAME_BODY_CORNER_CUT_MOMENTS_PASS')
    print('CLOSED_DOMAIN_HIGH_ENDPOINT_TRACE_LE_3_OVER_2_PASS')
    print('positive_coefficients='+str(cert['positive_terms']))
    print('ACTUAL_S5_I5_I4_TWO_POSITIVE_FANS_AND_TRUE_FACETS_PASS')
    print('SHARP_GEOMETRIC_LIMIT_THREE_HALVES_NOT_STATIONARY_CLAIM')
    print('coefficient_bytes='+str(cp['bytes']))
    print('coefficient_sha256='+cp['sha256'])
    print('report_bytes='+str(rp['bytes']))
    print('report_sha256='+rp['sha256'])
    print('OCTANT_SPECIAL_HIGH_ENDPOINT_VALUE_V1_RECOVERY_PASS')


if __name__=='__main__':main()
