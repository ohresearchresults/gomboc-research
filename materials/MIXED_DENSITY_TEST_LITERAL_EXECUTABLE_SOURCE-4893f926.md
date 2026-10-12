# material-4893f926def0

AI research material

---

"""Exact density/test Schur-complement gate and an actual triangular-lift ascent.
CPython 3.13.5; SymPy 1.14.0; assertions enabled; no input files.
The control is not a monostatic construction or a counterexample to 3/2.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as S

Q=S.Rational
rt=S.sqrt(6)
t,y,a,k,e,z=S.symbols('t y a k e z', real=True)


def simp(x):
    return S.factor(S.radsimp(S.simplify(x)))


def eq(x):
    assert simp(x)==0, simp(x)


def sign6(x):
    x=S.radsimp(S.simplify(x))
    u=S.simplify((x+x.xreplace({rt:-rt}))/2)
    v=S.simplify((x-x.xreplace({rt:-rt}))/(2*rt))
    assert u.is_Rational and v.is_Rational, (x,u,v)
    if not v:
        return S.sign(u)
    if not u:
        return S.sign(v)
    if S.sign(u)==S.sign(v):
        return S.sign(u)
    return S.sign(u)*S.sign(u*u-6*v*v)


def integral(p):
    return S.factor(S.integrate(S.integrate(S.expand(p),(y,t-1,1-t)),(t,0,1)))


def edge(p):
    return S.factor(S.integrate(S.expand(p).subs(t,0),(y,-1,1)))


def dump(x):
    if isinstance(x,S.MatrixBase):
        return [[str(simp(v)) for v in row] for row in x.tolist()]
    if isinstance(x,dict):
        return {str(key):dump(val) for key,val in x.items()}
    if isinstance(x,(list,tuple)):
        return [dump(v) for v in x]
    if isinstance(x,S.Basic):
        return str(simp(x))
    return x


def symbolic_gate():
    ell=1+a*t
    V=integral(ell);J=integral(t*ell);h=J/V
    Y=t-h;Z=y;psi=y
    I=integral(ell*Y*Y);D=integral(ell*Z*Z)
    B2=edge(ell*Y*Y);C=edge(ell*Z*Z)
    B1=edge(ell*Y);BZ=edge(ell*Z)
    pY=integral(psi*Y)/V;pZ=integral(psi*Z)/V
    K=S.factor(edge(psi*Y*Z)/B2-pY*BZ/B2-pZ*B1/B2-integral(psi*Y*Z)/I)
    gamma=S.factor(D/I-C/B2)
    R=S.factor(h*B2/I);RZ=S.factor(h*C/D)
    eq(K+2*(a+1)**2*(a+3)/(3*(a+2)*(a*a+8*a+10)))
    eq(gamma-2*a*(a+1)*(a+3)*(a+4)/(3*(a+2)**2*(a*a+8*a+10)))
    a0=rt-2
    lam=-3+rt/2
    eq((K/gamma).subs(a,a0)-lam)
    gain=simp((2*K*K/gamma).subs(a,a0))
    eq(gain-(-Q(19,6)+3*rt/2))
    assert sign6(gain)>0
    # At k=0 all affine-density and projective-test first variations vanish.
    # The a-direction is exact stationarity, not a numerical fit.
    eq(S.diff(R,a).subs(a,a0))
    rho=1+a*t+k*y
    V2=integral(rho);hy=integral(rho*t)/V2;my=integral(rho*y)/V2
    test=t-hy+e*(y-my)
    RR=S.factor(hy*edge(rho*test**2)/integral(rho*test**2))
    for var in (k,e):
        eq(S.diff(RR,var).subs({a:a0,k:0,e:0}))
    eq(S.diff(RR,k,2).subs({a:a0,k:0,e:0}))
    # Derivatives of log R at a stationary point use R''/R.
    eq((S.diff(RR,k,e)/RR).subs({a:a0,k:0,e:0})-2*K.subs(a,a0))
    eq((S.diff(RR,e,2)/RR).subs({a:a0,k:0,e:0})+2*gamma.subs(a,a0))
    route=S.factor(RR.subs({a:a0,k:z,e:lam*z}),extension=rt)
    R0=simp(R.subs(a,a0))
    delta=S.factor(route-R0,extension=rt)
    eps=Q(1,100)
    endgain=simp(delta.subs(z,eps))
    assert sign6(endgain)>0
    eq((S.diff(route,z,2)/route).subs(z,0)-gain)
    # Exact whole-bracket positivity: delta/z^2 has rational-in-z^2
    # numerator/denominator in Q(sqrt(6)); Bernstein controls certify it.
    w=S.symbols('w',nonnegative=True)
    num,den=S.fraction(S.cancel(delta/z**2,extension=rt))
    num=S.Poly(num,z);den=S.Poly(den,z)
    assert all(m[0]%2==0 for m,c0 in num.terms()+den.terms())
    pn=sum(c0*w**(m[0]//2) for m,c0 in num.terms())
    pd=sum(c0*w**(m[0]//2) for m,c0 in den.terms())
    if sign6(pd.subs(w,0))<0:
        pn=-pn;pd=-pd
    def bernstein(p):
        p=S.Poly(S.expand(p.subs(w,eps**2*w)),w);n=p.degree()
        controls=[simp(sum(p.nth(j)*Q(S.binomial(i,j),S.binomial(n,j)) for j in range(i+1))) for i in range(n+1)]
        assert all(sign6(c0)>0 for c0 in controls)
        return controls
    bn=bernstein(pn);bd=bernstein(pd)
    return {'base_a':a0,'base_R':R0,'other_horizontal_ratio':RZ.subs(a,a0),
            'general_a_cross_K':K,'general_a_gap_gamma':gamma,
            'base_K':K.subs(a,a0),'base_gamma':gamma.subs(a,a0),
            'optimal_first_order_test_tilt':lam,'fixed_test_density_hessian':0,
            'adapted_test_density_log_hessian':gain,'exact_route_R':route,
            'exact_route_gain':delta,'positive_gain_interval':'0<abs(z)<=1/100',
            'positive_numerator_Bernstein_controls':bn,'positive_denominator_Bernstein_controls':bd,
            'endpoint_gain':endgain}, a0, lam, R0


def actual_control(kk,a0,lam):
    heights=[1-kk,1+kk,1+a0]
    assert all(sign6(v)>0 for v in heights)
    raw=[]
    for (xx,yy),hh in zip([(0,-1),(0,1),(1,0)],heights):
        raw.extend([S.Matrix([xx,yy,-hh/2]),S.Matrix([xx,yy,hh/2])])
    rho=1+a0*t+kk*y
    V=integral(rho)
    mu=S.Matrix([integral(rho*t),integral(rho*y),0])/V
    cov=S.Matrix([[integral(rho*t*t),integral(rho*t*y),0],
                  [integral(rho*t*y),integral(rho*y*y),0],
                  [0,0,integral(rho**3)/12]])/V-mu*mu.T
    cov=cov.applyfunc(simp)
    cycles=[(0,2,3,1),(0,1,5,4),(2,4,5,3),(0,4,2),(1,3,5)]
    X=[v-mu for v in raw];normals=[]
    for f in cycles:
        aa,bb,cc=(X[i] for i in f[:3]);nn=(bb-aa).cross(cc-aa)
        q=(nn/nn.dot(aa)).applyfunc(simp)
        assert {i for i,v in enumerate(X) if simp(q.dot(v)-1)==0}==set(f)
        assert all(sign6(1-q.dot(v))>0 for i,v in enumerate(X) if i not in f)
        normals.append(q)
    support=set()
    for tri in itertools.combinations(range(6),3):
        aa,bb,cc=(raw[i] for i in tri);nn=(bb-aa).cross(cc-aa)
        if all(simp(v)==0 for v in nn):
            continue
        vals=[sign6(nn.dot(v-aa)) for v in raw]
        if all(v>=0 for v in vals) or all(v<=0 for v in vals):
            support.add(tuple(i for i,v in enumerate(vals) if v==0))
    assert support=={tuple(sorted(f)) for f in cycles}
    edges=sorted({tuple(sorted(vv)) for f in cycles for vv in zip(f,f[1:]+f[:1])})
    assert len(edges)==9
    vol=S.S(0);first=S.zeros(3,1);second=S.zeros(3,3)
    for f in cycles:
        for i in range(1,len(f)-1):
            vs=[mu,raw[f[0]],raw[f[i]],raw[f[i+1]]]
            det=S.det(S.Matrix.hstack(*(v-mu for v in vs[1:])))
            dv=simp(sign6(det)*det/6)
            assert sign6(dv)>0
            sm=sum(vs,S.zeros(3,1));ss=sum((v*v.T for v in vs),S.zeros(3,3))
            vol+=dv;first+=dv*sm/4;second+=dv*(sm*sm.T+ss)/20
    eq(vol-V)
    for v in first/vol-mu:
        eq(v)
    for v in second/vol-mu*mu.T-cov:
        eq(v)
    tf=S.zeros(3,3)
    for i in range(1,len(cycles[0])-1):
        vs=[X[j] for j in (cycles[0][0],cycles[0][i],cycles[0][i+1])]
        u=vs[1]-vs[0];v=vs[2]-vs[0];det=u[1]*v[2]-u[2]*v[1]
        ar=simp(sign6(det)*det/2)
        sm=sum(vs,S.zeros(3,1));ss=sum((p*p.T for p in vs),S.zeros(3,3))
        tf+=ar*(sm*sm.T+ss)/12
    tf=(tf/2).applyfunc(simp)
    alpha=simp(2*mu[0]/V)
    test=S.Matrix([1,lam*kk,0])
    RR=simp(alpha*(test.T*tf*test)[0]/(test.T*cov*test)[0])
    ve={};ef={}
    for i,j in edges:
        ve[(i,j)]=simp(X[i].dot(X[j]-X[i]));ve[(j,i)]=simp(X[j].dot(X[i]-X[j]))
        fs=[n for n,f in enumerate(cycles) if i in f and j in f]
        assert len(fs)==2
        f,g=fs;ef[(f,g)]=simp(normals[f].dot(normals[g]-normals[f]));ef[(g,f)]=simp(normals[g].dot(normals[f]-normals[g]))
    zeros=sum(v==0 for v in list(ve.values())+list(ef.values()))
    strictU=[i for i in range(6) if all(sign6(v)<0 for (src,dst),v in ve.items() if src==i)]
    strictS=[i for i in range(5) if all(sign6(v)<0 for (src,dst),v in ef.items() if src==i)]
    strictH=[]
    for i,j in edges:
        f,g=[n for n,ff in enumerate(cycles) if i in ff and j in ff]
        if all(sign6(v)<0 for v in (ve[(i,j)],ve[(j,i)],ef[(f,g)],ef[(g,f)])):
            strictH.append((i,j))
    if not zeros:
        assert len(strictS)+len(strictU)-len(strictH)==2
    return {'k':kk,'raw_vertices':raw,'true_cycles':cycles,'edges':edges,'V_E_F':[6,9,5],
            'actual_volume':V,'actual_centroid':mu,'actual_covariance':cov,
            'whole_marked_facet_T':tf,'alpha':alpha,'test_coefficients':test,'actual_R':RR,
            'euclidean_strict_S_U_H':[len(strictS),len(strictU),len(strictH)],
            'zero_primitive_count':zeros,'VE':ve,'EF':ef}


def main():
    theorem,a0,lam,R0=symbolic_gate()
    controls=[actual_control(kk,a0,lam) for kk in (Q(0),Q(1,100))]
    eq(controls[0]['actual_R']-R0)
    eq(controls[1]['actual_R']-R0-theorem['endpoint_gain'])
    out={'symbolic_gate_and_route':theorem,'actual_uniform_controls':controls}
    data=(json.dumps(dump(out),sort_keys=True,indent=2)+'\n').encode()
    Path('mixed_density_test_report.json').write_bytes(data)
    print('JOINT_AFFINE_DENSITY_AND_TEST_FIRST_STATIONARITY_PASS')
    print('ADAPTED_TEST_HESSIAN_POSITIVE_EXACT_PASS')
    print('WHOLE_SMALL_BRACKET_GAIN_BERNSTEIN_PASS')
    print('BOTH_ACTUAL_6_9_5_HULLS_CENTROIDS_AND_FACET_MOMENTS_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('MIXED_DENSITY_TEST_SCHUR_GATE_AND_ACTUAL_ASCENT_PASS')

if __name__=='__main__':
    main()
