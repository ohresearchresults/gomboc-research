# material-18d44bfc27e0

AI research material

---

#!/usr/bin/env python3
"""Exact algebra for H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1.
CPython 3.13.5 / SymPy 1.14.0. No numerical search or external input.
The analytic covariance and finite-height lemmas are cited in the proof.
This unit does not claim a whole-H5 exclusion or an attaining polyhedron.
"""
import hashlib
import json
from pathlib import Path
import sympy as S

R = S.Rational
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                      for f in FACETS for k in range(len(f))}))
CONTROLS = {
    'A': ('13/20','3/4','4/5','1/10','3/10'),
    'B': ('1/5','2/5','2/3','1/4','1/5'),
    'C': ('9/10','1/10','7/8','1/16','1/10'),
}

def vertices(theta):
    x,r,p,q,la = theta
    s = 1-la
    basal = ((R(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
             (0,1-3*r/4),(0,R(1,4)),(R(1,16),R(1,16)))
    return tuple(S.Matrix((s*a,s*b,0)) for a,b in basal) + (
        S.Matrix((0,0,1)),S.Matrix((la,0,1)),S.Matrix((0,la,1)))

def moments(z):
    """Signed origin tetrahedra: D=6V, K=6 integral x, L=6 integral xx^T."""
    D = S.Integer(0)
    K = S.zeros(3,1)
    L = S.zeros(3)
    for f in FACETS:
        for k in range(1,len(f)-1):
            a,b,c = (z[j] for j in (f[0],f[k],f[k+1]))
            d = a.dot(b.cross(c))
            t = a+b+c
            D += d
            K += d*t/4
            L += d*(t*t.T+a*a.T+b*b.T+c*c.T)/20
    return S.expand(D),K.applyfunc(S.expand),L.applyfunc(S.expand)

def encode(a):
    if isinstance(a,S.MatrixBase):
        return [[str(a[i,j]) for j in range(a.cols)] for i in range(a.rows)]
    if isinstance(a,S.Basic):
        return str(a)
    if isinstance(a,dict):
        return {str(k):encode(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)):
        return [encode(v) for v in a]
    return a

def minors(A):
    return [S.factor(A[:k,:k].det()) for k in range(1,A.rows+1)]

def pd(A):
    out = minors(A)
    assert all(t > 0 for t in out),out
    return out

def main():
    x,r,p,q,la = S.symbols('x r p q la')
    theta = (x,r,p,q,la)
    z = vertices(theta)
    D,K,L = moments(z)
    s = 1-la
    area = (31-24*x*p-24*r*q)/64
    bx = R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by = R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    expectedD = la+2*area*s*s
    expectedK = S.Matrix((3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,
                          3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,
                          area*s*s/2+la/2+la*la/4))
    expectedLzz = area*s*s/5+3*la/10+3*la*la/10
    assert S.expand(D-expectedD) == 0
    assert (K-expectedK).applyfunc(S.expand) == S.zeros(3,1)
    assert S.expand(L[2,2]-expectedLzz) == 0
    # Exact sectional moments, independently integrating the quadratic area.
    h = S.symbols('h')
    Ah = area*s*s*(1-h)**2+s*la*h*(1-h)+la*la*h*h/2
    assert S.expand(6*S.integrate(Ah,(h,0,1))-D) == 0
    assert S.expand(6*S.integrate(h*Ah,(h,0,1))-K[2]) == 0
    assert S.expand(6*S.integrate(h*h*Ah,(h,0,1))-L[2,2]) == 0
    # Beta(1,3), Beta(2,2), Beta(3,1) probability weights.
    w0,w1 = S.symbols('w0 w1')
    w2 = 1-w0-w1
    mean = w0/4+w1/2+3*w2/4
    second = w0/10+3*w1/10+3*w2/5
    variance = S.expand(second-mean*mean)
    lower_remainder = w1/80+(w1*(w0+w2)+4*w0*w2)/16
    upper_remainder = w1/20+(w2-w0)**2/16
    assert S.expand(variance-R(3,80)-lower_remainder) == 0
    assert S.expand(R(1,10)-variance-upper_remainder) == 0
    physical_weights = (2*area*s*s/D,s*la/D,la*la/D)
    assert S.cancel(sum(physical_weights)-1) == 0
    assert S.cancel(variance.subs({w0:physical_weights[0],w1:physical_weights[1]})
                    -(L[2,2]/D-(K[2]/D)**2)) == 0
    # All six actual halfspaces of the common inscribed triangular bipyramid.
    common = ((4,4,-1,0),(4,4,1,1),(-4,-12,1,0),
              (-4,-12,-1,-1),(-12,-4,1,0),(-12,-4,-1,-1))
    centre = S.Matrix((R(1,21),R(1,21),R(1,2)))
    radius = R(1,50)
    guards = []
    for a,b,c,d in common:
        n = S.Matrix((a,b,c)); slack = d-n.dot(centre)
        guard = S.factor(slack*slack-radius*radius*n.dot(n))
        assert slack > 0 and guard > 0
        guards.append({'normal':n,'support':d,'slack':slack,'squared_guard':guard})
    # The three basal anchors belong to Delta and are literal H5 vertices.
    anchors = ((R(1,4),0),(0,R(1,4)),(R(1,16),R(1,16)))
    for a,b in anchors:
        assert a >= 0 and b >= 0 and a+b <= 1
        assert a+3*b >= R(1,4) and 3*a+b >= R(1,4) and a+b <= R(1,4)
    # Complete-square shear bound for a two-dimensional compression.
    kap,t = S.symbols('kap t',positive=True)
    expr = t-kap*(1+t)**2/(kap+1)**2
    rhs = (kap-1)**2/(4*kap)-kap/(kap+1)**2*(t-(kap*kap+1)/(2*kap))**2
    assert S.factor(expr-rhs) == 0
    kappa = S.Integer(48)
    spectral_shear_square = (kappa-1)**2/(4*kappa)
    kantorovich = 1+spectral_shear_square
    assert spectral_shear_square == R(2209,192)
    assert kantorovich == R(2401,192)
    sigma_floor = radius**2/15
    assert sigma_floor == R(1,37500)
    raw_cond = kappa*R(3,4)/sigma_floor
    tangential_cond = kappa*R(1,2)/sigma_floor
    eta_floor = sigma_floor/(2*kappa*R(1,10))
    shear_component_square = kantorovich*R(1,4)/R(3,80)
    assert raw_cond == 1350000
    assert tangential_cond == 900000
    assert eta_floor == R(1,360000)
    assert shear_component_square == R(12005,144) < 100
    # A U1 cap has radius squared at most 2/(4*(1/4)^2)=8.
    eta_ceiling = R(2)/(4*R(1,4)**2)
    mzz_ceiling = R(2)/R(1,4)**2+2
    assert eta_ceiling == 8 and mzz_ceiling == 34
    controls = {}
    for name,values in CONTROLS.items():
        th = tuple(map(R,values)); zz = vertices(th)
        for f in FACETS:
            a,b,c = (zz[j] for j in f[:3]); n=(b-a).cross(c-a); H=n.dot(a)
            assert n != S.zeros(3,1)
            for j in range(10):
                assert n.dot(zz[j]) == H if j in f else n.dot(zz[j]) < H
        assert len(EDGES)==17
        dd,kk,ll = moments(zz)
        assert dd>0
        gg=kk/dd; Sigma=(ll/dd-gg*gg.T).applyfunc(S.factor)
        lower_minors=pd(Sigma-sigma_floor*S.eye(3))
        assert R(3,80) < Sigma[2,2] < R(1,10)
        aa=Sigma[:2,:2]; bb=Sigma[:2,2]; cc=Sigma[2,2]
        C=(aa-bb*bb.T/cc).applyfunc(S.factor)
        pd(C-sigma_floor*S.eye(2)); pd(R(1,2)*S.eye(2)-C)
        # Exact covariance-isotropic metric, normalized by tr G=1.
        M=Sigma.inv(); scale=M[0,0]+M[1,1]; M=(M/scale).applyfunc(S.factor)
        assert Sigma*M == S.eye(3)/scale
        G=M[:2,:2]; v=(G.inv()*M[:2,2]).applyfunc(S.factor)
        eta=S.factor(M[2,2]-(v.T*G*v)[0])
        assert G.trace()==1 and eta>eta_floor
        assert all(a*a<100 for a in v)
        assert G.det()>tangential_cond/(tangential_cond+1)**2
        # Isotropy forces the regression-centred shear to vanish.
        assert (v+bb/cc).applyfunc(S.factor)==S.zeros(2,1)
        controls[name]={'theta':th,'volume':dd/6,'centroid':gg,'covariance':Sigma,
                        'covariance_floor_minors':lower_minors,
                        'covariance_isotropic_metric':M,'G':G,'shear':v,'eta':eta}
    output={
        'identity':'H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1',
        'environment':{'python':'3.13.5','sympy':S.__version__},
        'scope':'Necessary joint S1/U1 metric chart for actual homogeneous H5. No full H5 or E17 exclusion; no attaining example. The uniform lower metric bounds do not apply to U1 alone.',
        'true_vertices':10,'true_edges':17,'true_maximal_facets':9,
        'common_ball_centre':centre,'common_ball_radius':radius,'common_ball_guards':guards,
        'exact_z_variance_interval':[R(3,80),R(1,10)],
        'covariance_floor':sigma_floor,'covariance_trace_ceiling':R(3,4),
        'conditional_horizontal_covariance_ceiling':R(1,2),
        'covariance_metric_condition_strict_ceiling':kappa,
        'raw_metric_condition_strict_ceiling':raw_cond,
        'trace_one_G_condition_strict_ceiling':tangential_cond,
        'trace_one_G_eigenvalue_strict_floor':1/(tangential_cond+1),
        'trace_one_G_disk_radius_square_strict_ceiling':((tangential_cond-1)/(tangential_cond+1))**2,
        'regression_shear_ellipsoid_square_strict_ceiling':spectral_shear_square,
        'shear_component_square_strict_ceiling':shear_component_square,
        'normal_eta_strict_interval':[eta_floor,eta_ceiling],
        'U1_Mzz_ceiling':mzz_ceiling,
        'six_raw_second_moment_polynomials':{f'{i}{j}':L[i,j] for i in range(3) for j in range(i,3)},
        'controls':controls,'exact_checks':'PASS'}
    data=(json.dumps(encode(output),sort_keys=True,indent=2)+'\n').encode()
    path=Path('h5_joint_compact_report.json');path.write_bytes(data)
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('H5_JOINT110_UNIFORM_METRIC_COMPACTNESS_V1_PASS')

if __name__ == '__main__':
    main()
