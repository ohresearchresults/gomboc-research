# material-db02c3d623c7

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# The adapted-test density Hessian: a stronger global gate and an exact same-incidence ascent

## Scope and dependencies
This coordinator theorem strengthens the actual affine-density clipping conditions in the fully read literal minimum-0295, SHA c5da795d12e9ffc99d28fd53e74ba1cc2494cdcc24117b6b85633536d62c0819. It uses the actual planar reduction in minimum-0290 and the already accepted normal3/2 theorem. The complete triangular-lift bound45/32 and its exact moment formulas are independently preserved in [internal-source-reference]. The full convex-height gate including density zeros is [internal-source-reference].

The new condition is NECESSARY at a hypothetical global strong maximum above3/2. It is not a proof that every remaining conic candidate fails. The exact control below is a genuine uniform6/9/5 body and an actual same-incidence perturbation, with proper Euclidean class569 and no weak equilibria. It is NOT a110 construction, not a violation of3/2, and does not change34<=Cmin<=622.

## 1. Exact orthogonal test at a supercritical maximum
Use actual convex planar K, nonnegative affine ell, whole edge e={t=0},t>=0, and actual-centered affine Y. Put

    V=int_K ell, J=int_K t ell, I=int_K ell Y²,
    Bj=int_e ell Y^j d_sigma, h=J/V,
    R=h B2/I, eta=B1/B2, kappa=B0/B2,
    d_sigma=ds/|grad t|.

At test stationarity, int_K ell tY/I=-h eta. A supercritical R>3/2 cannot be the pure normal test. Hence

    Z=t-h+h eta Y

is a nonzero independent actual-centered affine test. It is orthogonal to Y for BOTH the volume and facet quadratic forms:

    int_K ell YZ=0, int_e ell YZ=0.

Let D=int_K ell Z²>0 and C=int_e ell Z²=h²(B0-B1²/B2). Define R_Z=h C/D. The normal test t-h=Z-h eta Y is a variance-weighted average of the two diagonal Rayleigh ratios R and R_Z. Since its ratio is at most3/2 and R>3/2, R_Z<=3/2<R. Thus

    gamma=D/I-C/B2=(D/I)(1-R_Z/R)>0.

In particular the maximizing horizontal test is simple: a repeated horizontal eigenvalue above3/2 would also violate the normal theorem. The transverse block is already below3/2. No unproved eigenvalue-gap assumption is needed here.

More generally, the formulas below hold for any centered independent Z orthogonal to Y for both forms, with gamma>0. This version is used in the exact subcritical control, where Y itself is normal and the displayed normal-residual construction of Z would vanish.

## 2. Mixed density/test derivative
For an affine density perturbation psi, use actual clipping

    ell_s=ell+s psi, K_s=K intersect{ell_s>=0}.

Recenter BOTH fixed affine tests under the actual ell_s distribution. Let

    pY=int_K psi Y/V, pZ=int_K psi Z/V,
    B_Z=int_e ell Z d_sigma,
    K_psi=int_e psi YZ d_sigma/B2
           -pY B_Z/B2-pZ B1/B2-int_K psi YZ/I.

All unweighted bulk integrals in these derivative expressions are literal area integrals, not ell-weighted surrogates. At the base point the first test derivative is zero and the exact second test derivative of log R(Y+epsilon Z) is -2 gamma. The mixed derivative with respect to density and test is 2 K_psi. The actual-centroid terms pY and pZ in K_psi cannot be omitted.

For the supercritical normal-residual Z above, B_Z=-h B2(kappa-eta²), so an equivalent useful formula is

    K_psi=int_e psi YZ/B2+h(kappa-eta²)pY
           -eta pZ-int_K psi YZ/I.

Clipping changes raw moments only at second order. Consequently it does not change this mixed FIRST-in-density derivative. Its second-order bulk and marked-endpoint contributions to the density Hessian remain exactly those in the literal clipping parent.

## 3. The stronger necessary Hessian
At a density-stationary base, normalize psi by subtracting a scalar multiple of ell so that int_K psi=0. This only removes scale, which leaves the ratio and K_psi unchanged. Put

    p=int_K Y psi/V, j=int_K t psi/J,
    q=int_K Y² psi/I, E1=int_e Y psi d_sigma.

The fixed-test formal log Hessian from the clipping parent is

    H_form=2j(q-j)+2p²(B0/B2+V/I)-4p E1/B2.

Let C_plus(psi),C_minus(psi) be its actual one-sided clipping corrections. In particular the bulk correction for positive s is

    int_Gamma Phi (-psi)_+² ds/|grad ell|,
    Gamma=K intersect{ell=0},
    Phi=t/J-1/V-Y²/I-2 eta Y/V,

with the separate marked-endpoint term Y(p)²(-psi(p))_+²/[B2 |D_e ell| |grad t|]. Negative s uses the positive part. The full parent's point-contact and leverage qualifications remain unchanged.

Now choose the simultaneously adapted test

    Y_s + s (K_psi/gamma) Z_s,

where subscripts denote the ACTUAL new centering. Its second log derivative is

    H_adapted,plus/minus
      =H_form+C_plus/minus(psi)+2 K_psi²/gamma.

This is the exact scalar Schur-complement improvement: for a general first-order tilt k the additional term is4k K_psi-2gamma k², maximized at k=K_psi/gamma. The clipping correction is unchanged, since an O(s) change of test times an O(s²) clipped mass first contributes at third order. Therefore a global maximum must satisfy

    H_form+C_plus/minus(psi)+2 K_psi²/gamma <=0

for BOTH signs and every affine psi. Passing only the fixed-test density Hessian is insufficient.

If the positive-length zero edge Gamma is disjoint from the marked edge, the parent's cap signs give Phi>0 in its relative interior. Adding the two one-sided conditions yields the stronger quotient condition

    H_form+2 K_psi²/gamma
      <=-int_Gamma Phi psi² ds/(2|grad ell|)<0

for every psi not proportional to ell. In any two-dimensional affine-density quotient basis this is the matrix gate

    H_form_matrix + 2 k k^T/gamma + G_Gamma/2 <=0,

where k records K on that basis and G_Gamma records the displayed positive boundary Gram form. This is an exact positive rank-one strengthening of the earlier gate. It applies to the remaining forced-density one/two-arc candidates, but their complete exclusion has not been established.

## 4. Exact countercontrol to fixed-test second-order adequacy
Let

    K=conv((0,-1),(0,1),(1,0)),
    ell=1+a t+k y, a0=sqrt(6)-2, k=0,
    Y=t-h, Z=y.

At this base, every affine-density first variation modulo scale and every projective horizontal-test first variation vanish. The normal test is the larger horizontal eigenvector. Its ratio and the other horizontal ratio are

    R0=243/25-171sqrt(6)/50,
    R_Z=16-6sqrt(6)<R0.

For psi=y the fixed-normal-test density Hessian is EXACTLY zero: this density direction does not change any normal raw moment. Nevertheless

    K_psi=-3/2+11sqrt(6)/18,
    gamma=7/18-sqrt(6)/9>0,
    K_psi/gamma=-3+sqrt(6)/2,
    2K_psi²/gamma=-19/6+3sqrt(6)/2>0.

Thus joint adaptation is a strict ascent even though the separate density second-order test sees no gain. This also refines the earlier single-apex control in [internal-source-reference]: that control need not be treated as a full joint local maximum merely because its first derivatives and all single-apex tests pass. The earlier ridge ascent remains valid and is a different admissible deformation.

The exact same-incidence route is

    ell_z=1+(sqrt(6)-2)t+z y,
    mu_y=z/[2(1+sqrt(6))],
    Y_z=t-h+(-3+sqrt(6)/2)z(y-mu_y).

Here h is unchanged because the odd density perturbation has zero normal moments. Its exact gain is

 R(z)-R0 =
  -3 z²(-324+131sqrt(6))
      [z²+2733842/99515+1190544sqrt(6)/99515]
  /{100[z^4+z²(-392/15-44sqrt(6)/5)-704/75-256sqrt(6)/75]}.

The complete source verifies this identity and certifies positive numerator/denominator Bernstein controls after sign normalization for0<|z|<=1/100. At z1/100 the positive gain is

    8070385933223717643522259298480497
      /13925357650630788991695974747950
    -19768318427260600218429573591802803 sqrt(6)
      /83552145903784733950175848487700,

approximately0.00003376743718823913. The perturbed ratio is approximately1.34277884631838549, still strictly below3/2 and below the proved triangular45/32 bound.

## 5. Actual uniform bodies, maximal incidence and physical controls
For z=0 and z1/100, use these SIX raw vertices, with a=a0:

    (0,-1,-(1-z)/2), (0,-1,(1-z)/2),
    (0, 1,-(1+z)/2), (0, 1,(1+z)/2),
    (1, 0,-(1+a)/2), (1,0,(1+a)/2).

The FIVE maximal cycles, in that order, are

    (0,2,3,1), (0,1,5,4), (2,4,5,3), (0,4,2), (1,3,5).

The first WHOLE quadrilateral is marked. Both bodies have true6/9/5,C18. Exact supporting-plane exhaustion finds no hidden facet; positive tetrahedral fans reproduce the actual volume, centroid and full covariance; an independent marked-face fan reproduces its second moments. The actual centroid is(h,mu_y,0). The code uses exact arithmetic in Q(sqrt(6)), not floating hull tolerances.

Under the SAME physical Euclidean metric and inverse M=N=I, both controls have all36 true-edge primitives nonzero and strict S/U/H=5/6/9, hence physicalweak000. These are material nonattainers. The construction changes neither vertex count nor maximal incidence, unlike the earlier ridge lift with8/12/6. It is a diagnostic of necessary optimization conditions, not an upper-bound improvement for class110.

## 6. Complete runnable recovery
Save the following block, with final LF, as mixed_density_test_exact.py. CPython3.13.5,SymPy1.14.0,assertions enabled,no external input files. Run

    python -B mixed_density_test_exact.py > mixed_density_test_exact.log

Source8856B, SHA256 410e2f606eb92d05b054f3fca558b98e3e28f05a4a31a0c2e320d5528b122868.
Report mixed_density_test_report.json12600B, SHA256 a701c729d1cc602416061317ec73b66f0b1bc5feecb7c9c586a491547ab90ac89.
Stdout mixed_density_test_exact.log338B, SHA256 616f303b8d2a4979f56045ed391e3f14281e038736664605c0d919f1b92c63a62.
Normal and fresh-directory source-only runs reproduced both output files byte-identically. Final marker MIXED_DENSITY_TEST_SCHUR_GATE_AND_ACTUAL_ASCENT_PASS. No seed, numerical locator, cached data or absent helper is used in this proof or control.

```python
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
```
