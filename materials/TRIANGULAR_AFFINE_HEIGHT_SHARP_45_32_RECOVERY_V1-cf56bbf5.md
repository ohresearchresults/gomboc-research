# material-cf56bbf56ecd

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Sharp whole-facet constants on all affine-height triangular lifts

## Statement and scope
For any nondegenerate convex planar triangle K, any nonzero nonnegative affine height ell and any whole lateral facet of positive area in the actual uniform lift P={(x,z):x in K,2|z|<=ell(x)}, the centered full matrix inequality is

    alpha T <= (45/32) Sigma.

All moments and the facet distance are computed at P's ACTUAL volume centroid. The constant45/32 is sharp and is strictly smaller than3/2. This covers every affine image of these lifts and all test directions, not just the transverse fibre. It is NOT an assertion for arbitrary planar supports, a universal3D theorem, an E17 exclusion or a110 construction. The exact matrix sharpness control is an actual5/8/5 pyramid with Euclidean own558 physicalweak000. It therefore does not improve34<=Cmin<=622.

This is a new coordinator calculation. The earlier literal parent minimum-0290, SHA a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8, had proved the triangular TRANSVERSE bound5/4, not this full horizontal45/32 bound. Its triangle-only nonlocalization warning remains valid.

## Exact reduction and proof
Affine changes of planar coordinates, followed by a positive height scaling, reduce every marked case to

    K=conv((0,-1),(0,1),(1,0)),
    ell=1+(c-1)t+k y, c>=0, -1<=k<=1.

The three vertex heights are1-k,1+k,c. The sum of the two marked-edge heights is positive because the marked facet has positive area, so this normalization loses no admissible case. Let V=int_K ell and mu be its actual horizontal mean. Direct integration gives

    V=(c+2)/3,
    mu=((c+1)/(2(c+2)), k/(2(c+2))).

The horizontal covariance and alpha-weighted whole-facet second moment are

    Sigma_h = [[c²+6c+3, -k(3c+1)],
               [-k(3c+1), 2c²+12c-5k²+16]]/[20(c+2)²],

    Q_h=alpha T_h = [[3(c+1)³, -k(c+1)²(2c+1)],
      [-k(c+1)²(2c+1), (c+1)(4c²-4ck²+16c-5k²+16)]]/[4(c+2)^4].

Put G=(45/32)Sigma_h-Q_h and

    P(c)=3c^4-2c³-3c²+12c+4
        =3c²(c-1)²+c[(4c-3)²+39]/4+4>0.

Then G11=3P/[128(c+2)^4]>0, and

    8192(c+2)^6 det G=(1-k²)D0(c)+k²D1(c),
    D0=3(9c²-10c+8)P>0,
    D1=(c-2)²(9c²+4c+4)(9c²+16c+4)>=0.

The positivity of the remaining quadratic follows from
9c²-10c+8=(3c-5/3)²+47/9. Hence G is positive semidefinite on the ENTIRE closed density domain. It is singular exactly when c=2, |k|=1. Its null directions are(-3,1) for k=1 and(3,1) for k=-1.

Reflection z->-z makes every horizontal/vertical mixed covariance and whole-facet second moment zero. For general nonnegative vertex heights a,b,c, write

    S3=a³+a²b+ab²+b³,
    H3=S3+c(a²+ab+b²)+c²(a+b)+c³.

The vertical ratio is5(a+b+2c)S3/[4(a+b+c)H3]<=5/4, because

    (a+b+c)H3-(a+b+2c)S3
    =cab(a+b)+c²(2a²+3ab+2b²)+2c³(a+b)+c^4>=0.

The source independently derives the ratio from the actual volume and edge integrals. Since5/4<45/32, this closes the entire3D matrix, including all mixed tests after arbitrary affine transformations.

## Sharp centroid leverage in the same class
The facet centroid has no vertical component. Its exact leverage alpha c_F^T Sigma^-1 c_F is the function L(c,k) in the source. It is nondecreasing in w=k², with

    dL/dw=10c^4(c+1)(c+4)/[3(c+2)(-c³-10c²+7cw-27c+4w-12)²]>=0.

For c>0 its maximum over k is at |k|=1. There it equals

    L1(c)=5(c+1)(11c²+24c+12)/[3(c+2)²(c²+8c+4)],
    L1'(c)=-5c p(c)/[3(c+2)³(c²+8c+4)²],
    p(c)=11c^4+48c³-8c²-128c-80.

The coefficient signs have exactly one change. Together with p(0)<0 and its positive leading coefficient, Descartes' rule proves exactly one positive root c*. Thus the SHARP weaker constant in this triangular class is L1(c*). Exact rational isolation is

    1685181062944/10^12 < c* < 1685181062945/10^12.

Numerically c* is about1.68518106294445 and L1(c*) about1.35702653919915. The exact definition is the isolated root and rational function, not these decimals. Equality is realized by the genuine lift with vertex heights0,2,c* or its reflection; no physical equilibrium census is claimed for that algebraic weaker-sharpness object.

## Exact rational matrix-sharpness control
Object identity: TRIANGLE_AFFINE_SHARP_45_32_PYRAMID.
Raw vertices, in fixed order, are

    (0,-1,0),(0,1,-1),(0,1,1),(1,0,-1),(1,0,1).

The complete maximal cycles are

    (0,1,2),(1,3,4,2),(0,3,1),(0,2,4),(0,4,3).

The first whole triangular facet is marked. True counts are5/8/5,C16. Actual volume is4/3, centroid(3/8,1/8,0), and

    Sigma=[[19/320,-7/320,0],[-7/320,43/320,0],[0,0,1/5]],
    T_F=[[9/64,-5/64,0],[-5/64,17/64,0],[0,0,1/6]], alpha=9/16.

The generalized ratios are15/32,15/16,45/32. The sharp centered test is Y=y-3t+1. The source exhausts all supporting planes, verifies the maximal cycles and eight genuine edges, recomputes the uniform moments through a positive tetrahedral fan, and recomputes the whole marked-facet moments independently. For the Euclidean common metric M=N=I all16 VE and all16 EF true-edge primitives are strictly negative: proper S/U/H=5/5/8 and physicalweak000. This is an exact nonattaining control, not a minimum construction.

## Reproducibility and evidence
Save the complete code block below as triangle_affine_sharp_exact.py with its final LF. Exact acceptance requires CPython3.13.5 and SymPy1.14.0, assertions enabled, no input files. Run

    python -B triangle_affine_sharp_exact.py > triangle_affine_sharp_exact.log

Source:10710 bytes, SHA256 fef07e81f88de0a4533756461ac9ea7fca5d8b8ca31cf2dc268ee94869e6cafd.
Reproduced report triangle_affine_sharp_report.json:6873 bytes, SHA256 bdf1640cc5667ae043359e39fda1ac5639c92b8d9f25ae45e947e9a7992e02bf.
Reproduced stdout triangle_affine_sharp_exact.log:230 bytes, SHA256 9d2768447955b5cd462812a1cb078b887f0a2f06c952e84e7bee6787726c86f2.
Normal execution and a fresh directory containing ONLY the source reproduced both output files byte-identically. Terminal marker:

    TRIANGULAR_AFFINE_HEIGHT_FULL_MATRIX_AND_LEVERAGE_EXACT_PASS

The optional --locate discovery uses NumPy2.3.5/SciPy1.17.0, seed170029, popsize20,maxiter300,tol1e-12,polishTrue, log(c) bounds[-12,12],k[-1,1], single BLAS/OMP thread. Command OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B triangle_affine_sharp_exact.py --locate. It returned c about2.0000010158112222,k about.9999999999998836,ratio about1.406249999999963 after2883 evaluations. It is not the proof or an input checkpoint. All parameters and the complete locator are retained in the same source.

```python
"""Sharp whole-lateral-facet moments of every affine-height triangular lift.
Exact acceptance: CPython 3.13.5, SymPy 1.14.0, assertions enabled.
No input files. Optional --locate also uses NumPy 2.3.5/SciPy 1.17.0;
set OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 for that discovery replay.
"""
from pathlib import Path
import argparse
import hashlib
import itertools
import json
import sys
import sympy as s


def zero(expr):
    assert s.factor(expr) == 0, s.factor(expr)


def dump(value):
    if isinstance(value, s.MatrixBase):
        return [[str(s.factor(v)) for v in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {str(k): dump(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [dump(v) for v in value]
    if isinstance(value, s.Basic):
        return str(s.factor(value))
    return value


def triangle_integral(expr, t, y):
    expr = s.expand(expr)
    return s.factor(s.integrate(s.integrate(expr, (y, t - 1, 1 - t)), (t, 0, 1)))


def exact_triangle():
    t, y, c, k, w = s.symbols('t y c k w', real=True)
    ell = 1 + (c - 1) * t + k * y
    integ = lambda p: triangle_integral(p, t, y)
    V = integ(ell)
    mu = s.Matrix([integ(ell*t), integ(ell*y)]) / V
    cov = s.Matrix([[integ(ell*t*t), integ(ell*t*y)],
                    [integ(ell*t*y), integ(ell*y*y)]]) / V - mu*mu.T
    cov = cov.applyfunc(s.factor)
    edge = [s.S(0), y]
    E = s.Matrix([[s.integrate((1+k*y)*(edge[i]-mu[i])*(edge[j]-mu[j]),
                              (y, -1, 1)) for j in range(2)] for i in range(2)])
    Q = (mu[0]*E/V).applyfunc(s.factor)
    expected_cov = s.Matrix([[c*c+6*c+3, -k*(3*c+1)],
                            [-k*(3*c+1), 2*c*c+12*c-5*k*k+16]])/(20*(c+2)**2)
    expected_Q = s.Matrix([[3*(c+1)**3, -k*(c+1)**2*(2*c+1)],
                          [-k*(c+1)**2*(2*c+1),
                           (c+1)*(4*c*c-4*c*k*k+16*c-5*k*k+16)]])/(4*(c+2)**4)
    for v in cov - expected_cov:
        zero(v)
    for v in Q - expected_Q:
        zero(v)
    sharp = s.Rational(45, 32)
    G = (sharp*cov-Q).applyfunc(s.factor)
    P = 3*c**4-2*c**3-3*c**2+12*c+4
    P_sos = 3*c*c*(c-1)**2 + c*((4*c-3)**2+39)/4 + 4
    zero(P-P_sos)
    zero(G[0, 0]-3*P/(128*(c+2)**4))
    D0 = 3*(9*c*c-10*c+8)*P
    D1 = (c-2)**2*(9*c*c+4*c+4)*(9*c*c+16*c+4)
    det_num = s.factor(8192*(c+2)**6*G.det())
    zero(det_num-((1-k*k)*D0+k*k*D1))
    zero(9*c*c-10*c+8-((3*c-s.Rational(5, 3))**2+s.Rational(47, 9)))
    assert G.subs({c: 2, k: 1}).nullspace() == [s.Matrix([-3, 1])]
    assert G.subs({c: 2, k: -1}).nullspace() == [s.Matrix([3, 1])]

    # Full vertical block, with endpoint heights a,b,c all nonnegative.
    a, b, cc = s.symbols('a b cc', nonnegative=True)
    S3 = a**3+a*a*b+a*b*b+b**3
    H3 = S3+cc*(a*a+a*b+b*b)+cc*cc*(a+b)+cc**3
    gap = (a+b+cc)*H3-(a+b+2*cc)*S3
    positive_gap = cc*a*b*(a+b)+cc**2*(2*a*a+3*a*b+2*b*b)+2*cc**3*(a+b)+cc**4
    zero(gap-positive_gap)
    z_var = s.factor(integ(ell**3)/(12*V))
    z_edge = s.factor(s.integrate((1+k*y)**3, (y, -1, 1))/24)
    alpha = s.factor(2*mu[0]/V)
    z_ratio = s.factor(alpha*z_edge/z_var)
    vertical_formula = 5*(a+b+2*cc)*S3/(4*(a+b+cc)*H3)
    zero(z_ratio-vertical_formula.subs({a: 1-k, b: 1+k, cc: c}))

    # The weaker centroid-leverage constant, optimized over horizontal tests.
    delta = s.Matrix([-mu[0], k/3-mu[1]])
    leverage = s.factor(alpha*(delta.T*cov.inv()*delta)[0])
    L = 5*(c+1)*(2*c**3*k*k+9*c**3-8*c*c*k*k+54*c*c-21*c*k*k+81*c-12*k*k+36)/(3*(c+2)**2*(c**3+10*c*c-7*c*k*k+27*c-4*k*k+12))
    zero(leverage-L)
    Lw = leverage.subs(k*k, w)
    deriv_w = 10*c**4*(c+1)*(c+4)/(3*(c+2)*(-c**3-10*c*c+7*c*w-27*c+4*w-12)**2)
    zero(s.diff(Lw, w)-deriv_w)
    L1 = 5*(c+1)*(11*c*c+24*c+12)/(3*(c+2)**2*(c*c+8*c+4))
    zero(leverage.subs(k, 1)-L1)
    quartic = 11*c**4+48*c**3-8*c*c-128*c-80
    zero(s.diff(L1, c)+5*c*quartic/(3*(c+2)**3*(c*c+8*c+4)**2))
    # Coefficient signs +,+,-,-,- give one positive root by Descartes;
    # the two exact evaluations isolate it. No floating root is an input.
    root_interval = (s.Rational(1685181062944, 10**12), s.Rational(1685181062945, 10**12))
    assert quartic.subs(c, root_interval[0]) < 0 < quartic.subs(c, root_interval[1])
    assert [s.sign(v) for v in s.Poly(quartic, c).all_coeffs()] == [1, 1, -1, -1, -1]
    # Uniform rational strict separation from the strong constant.
    margin_num = s.factor((s.Rational(45, 32)-L1)*96*(c+2)**2*(c*c+8*c+4))
    # This margin is optional; the full matrix bound already proves it.
    return {
        'domain': 'c>=0, -1<=k<=1; endpoint heights 1-k,1+k,c; marked edge t=0',
        'V': V, 'mean': mu, 'covariance_horizontal': cov,
        'alpha_T_horizontal': Q, 'sharp_full_matrix_constant': sharp,
        'positive_pivot_polynomial': P, 'positive_pivot_decomposition': P_sos,
        'determinant_numerator': det_num, 'determinant_at_k0': D0,
        'determinant_at_k1': D1,
        'equality_density_parameters': [[2, -1], [2, 1]],
        'vertical_ratio': z_ratio, 'vertical_bound': s.Rational(5, 4),
        'vertical_nonnegative_gap': positive_gap,
        'centroid_leverage': leverage, 'leverage_derivative_in_k_squared': deriv_w,
        'sharp_leverage_boundary_function': L1,
        'sharp_leverage_unique_positive_root_polynomial': quartic,
        'sharp_leverage_root_interval': root_interval,
        'strong_minus_leverage_margin_numerator': margin_num,
    }, c, k, cov, Q


def actual_five_vertex_control():
    raw = [s.Matrix(v) for v in [(0,-1,0), (0,1,-1), (0,1,1), (1,0,-1), (1,0,1)]]
    cycles = [(0,1,2), (1,3,4,2), (0,3,1), (0,2,4), (0,4,3)]
    expected_g = s.Matrix([s.Rational(3,8), s.Rational(1,8), 0])
    X = [p-expected_g for p in raw]
    Qf = []
    for cyc in cycles:
        a,b,c = (X[i] for i in cyc[:3])
        n = (b-a).cross(c-a)
        q = n/n.dot(a)
        assert {i for i,p in enumerate(X) if q.dot(p)==1} == set(cyc)
        assert all(q.dot(p)<1 for i,p in enumerate(X) if i not in cyc)
        Qf.append(q)
    # Exhaustive supporting-plane enumeration finds no additional maximal facet.
    supports = set()
    for tri in itertools.combinations(range(5), 3):
        a,b,c = (raw[i] for i in tri)
        n = (b-a).cross(c-a)
        if n == s.zeros(3, 1):
            continue
        vals = [n.dot(p-a) for p in raw]
        if all(v>=0 for v in vals) or all(v<=0 for v in vals):
            supports.add(tuple(i for i,v in enumerate(vals) if v==0))
    assert supports == {tuple(sorted(f)) for f in cycles}
    edges = sorted({tuple(sorted(e)) for f in cycles for e in zip(f, f[1:]+f[:1])})
    assert len(edges)==8 and len(raw)-len(edges)+len(cycles)==2
    assert all(sum(a in f and b in f for f in cycles)==2 for a,b in edges)
    # A positive tetrahedral fan at the actual interior point recomputes V,g,Sigma.
    vol, first, second = s.S(0), s.zeros(3,1), s.zeros(3,3)
    for f in cycles:
        for j in range(1, len(f)-1):
            verts = [expected_g, raw[f[0]], raw[f[j]], raw[f[j+1]]]
            u,v,w = [p-verts[0] for p in verts[1:]]
            dv = abs(s.det(s.Matrix.hstack(u,v,w)))/6
            assert dv>0
            sm = sum(verts, s.zeros(3,1))
            ss = sum((p*p.T for p in verts), s.zeros(3,3))
            vol += dv; first += dv*sm/4; second += dv*(sm*sm.T+ss)/20
    g = first/vol
    cov = second/vol-g*g.T
    expected_cov = s.Matrix([[s.Rational(19,320),-s.Rational(7,320),0],
                            [-s.Rational(7,320),s.Rational(43,320),0],
                            [0,0,s.Rational(1,5)]])
    assert vol==s.Rational(4,3) and g==expected_g and cov==expected_cov
    # Independent whole marked-triangle moments, not a triangularized surrogate.
    fverts = [X[i] for i in cycles[0]]
    sm = sum(fverts, s.zeros(3,1))
    T = (sm*sm.T+sum((p*p.T for p in fverts),s.zeros(3,3)))/12
    area = (raw[1]-raw[0]).cross(raw[2]-raw[0]).norm()/2
    alpha = area/(Qf[0].norm()*vol)
    assert area==2 and alpha==s.Rational(9,16)
    eigen = (cov.inv()*(alpha*T)).eigenvals()
    assert eigen=={s.Rational(15,32):1, s.Rational(15,16):1, s.Rational(45,32):1}
    sharp_test = s.Matrix([-3,1,0])
    assert (s.Rational(45,32)*cov-alpha*T)*sharp_test==s.zeros(3,1)
    # A full exact Euclidean physical census: every primitive is strictly negative.
    ve, ef = {}, {}
    for a,b in edges:
        ve[(a,b)] = X[a].dot(X[b]-X[a])
        ve[(b,a)] = X[b].dot(X[a]-X[b])
        fs = [i for i,f in enumerate(cycles) if a in f and b in f]
        assert len(fs)==2
        i,j=fs
        ef[(i,j)] = Qf[i].dot(Qf[j]-Qf[i])
        ef[(j,i)] = Qf[j].dot(Qf[i]-Qf[j])
    assert len(ve)==len(ef)==16 and all(v<0 for v in list(ve.values())+list(ef.values()))
    return {'identity': 'TRIANGLE_AFFINE_SHARP_45_32_PYRAMID',
            'raw_vertices': raw, 'centered_vertices': X, 'maximal_cycles': cycles,
            'edges': edges, 'facet_vectors_at_actual_centroid': Qf,
            'V_E_F': [5,8,5], 'C':16, 'uniform_volume':vol,'actual_centroid':g,
            'actual_covariance':cov,'marked_facet_index':0,'whole_facet_T':T,
            'alpha':alpha,'generalized_ratios':sorted(eigen),
            'equality_linear_test':sharp_test,
            'euclidean_strict_census_S_U_H':[5,5,8], 'physical_weak_count':0,
            'VE_primitives':ve,'EF_primitives':ef}


def locate(c, k, cov, Q):
    import numpy as np
    from scipy.optimize import differential_evolution
    f=s.lambdify((c,k),(cov,Q),'numpy')
    def objective(z):
        cv,qq=f(np.exp(z[0]),z[1])
        chol=np.linalg.cholesky(cv)
        mat=np.linalg.solve(chol,qq) @ np.linalg.inv(chol.T)
        return -np.linalg.eigvalsh(mat)[-1]
    result=differential_evolution(objective,[(-12,12),(-1,1)],seed=170029,
                                  popsize=20,maxiter=300,tol=1e-12,polish=True)
    print('OPTIONAL_NUMERICAL_LOCATOR',result.x.tolist(),float(np.exp(result.x[0])),
          float(-result.fun),result.nfev)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--locate',action='store_true')
    args=parser.parse_args()
    theory,c,k,cov,Q=exact_triangle()
    report={'theorem':theory,'actual_control':actual_five_vertex_control()}
    data=(json.dumps(dump(report),sort_keys=True,indent=2)+'\n').encode()
    path=Path('triangle_affine_sharp_report.json')
    path.write_bytes(data)
    print('SHARP_TRIANGULAR_LIFT_MATRIX_CONSTANT',s.Rational(45,32))
    print('ACTUAL_CONTROL 5/8/5 C16 own558 physicalweak000')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('TRIANGULAR_AFFINE_HEIGHT_FULL_MATRIX_AND_LEVERAGE_EXACT_PASS')
    if args.locate:
        locate(c,k,cov,Q)


if __name__=='__main__':
    main()
```
