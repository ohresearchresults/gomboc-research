# material-3e00ec4e7db5

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact one-moving-vertex volume-divided quartic stress criterion.
Run: python edge_slide_quartic.py [report.json]
Python >=3.11, SymPy. No solver, random choices or external data.
This is NOT an all-root free-r H5 atlas or a new proper110 body.
"""
import hashlib
import json
import sys
from pathlib import Path
import sympy as S

R = S.Rational
t = S.symbols('t')

def expand(m):
    return m.applyfunc(S.expand) if isinstance(m, S.MatrixBase) else S.expand(m)

def iszero(m):
    return expand(m) == S.zeros(*m.shape) if isinstance(m, S.MatrixBase) else expand(m) == 0

def sym(a, b):
    return (a*b.T+b*a.T)/2

def pd2(m):
    return [S.factor(m[0, 0]), S.factor(m.det())]

def sign_variations(vals):
    vals = [S.sign(v) for v in vals if v != 0]
    assert all(v in (-1, 1) for v in vals)
    return sum(a != b for a, b in zip(vals, vals[1:]))

def strict_poly_interval(poly, a=R(0), b=R(1)):
    poly = S.Poly(poly, t, domain=S.QQ)
    if poly.is_zero:
        return False, {'zero': True}
    if poly.degree() == 0:
        return poly.LC() > 0, {'constant': str(poly.LC())}
    # Repeated zeros also exclude strict positivity; Sturm counts distinct zeros.
    seq = S.sturm(poly.as_expr(), t)
    va = [S.factor(e.subs(t, a)) for e in seq]
    vb = [S.factor(e.subs(t, b)) for e in seq]
    roots = sign_variations(va)-sign_variations(vb)
    positive = poly.eval(a)>0 and poly.eval(b)>0 and roots == 0
    return bool(positive), {
        'degree': int(poly.degree()),
        'coefficients_descending': [str(v) for v in poly.all_coeffs()],
        'sturm_at_left': [str(v) for v in va],
        'sturm_at_right': [str(v) for v in vb],
        'variations': [sign_variations(va),sign_variations(vb)],
        'distinct_interior_roots': int(roots),
        'endpoint_values': [str(poly.eval(a)), str(poly.eval(b))],
    }

def bernstein(poly):
    poly = S.Poly(poly, t, domain=S.QQ)
    n = max(0, int(poly.degree()))
    return [sum(poly.nth(j)*S.binomial(i,j)/S.binomial(n,j)
                for j in range(i+1)) for i in range(n+1)]

def h5():
    x,p,q,l=R(1,2),R(3,8),R(1,4),R(1,2)
    s=1-l
    z=[S.Matrix(v) for v in (
        (s/4,0,0),(s*(1-3*x/4),0,0),(s*(1-p),s*p,0),
        (s*q,s*(1-q),0),(0,s*(1-3*t/4),0),(0,s/4,0),
        (s/16,s/16,0),(0,0,1),(l,0,1),(0,l,1))]
    area=(31-24*x*p-24*q*t)/64
    bx=p*p*x/8+3*p*x*x/32-3*p*x/8-q*q*t/8+R(509,3072)
    by=-p*p*x/8+q*q*t/8+3*q*t*t/32-3*q*t/8+R(509,3072)
    v=area*s*s/3+l/6
    j=S.Matrix((s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
        s**3*by/4+s*s*l*(1-3*q*t/4)/24+l*l/24,
        area*s*s/12+l/12+l*l/24))
    return z,expand(v),expand(j)

FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=((0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),
       (3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9))
TETS=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
      (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))

def main(dest):
    # Generic symmetric 3x3 rank-two determinant identity; exact symbolic algebra.
    a,b,c,d,e,f=S.symbols('a b c d e f')
    v=S.symbols('v')
    j=S.Matrix(S.symbols('j0:3')); flux=S.Matrix(S.symbols('f0:3'))
    q=S.Matrix([[a,b,c],[b,d,e],[c,e,f]])
    cr=j.cross(flux)
    rhs=-v*v*q.det()+v*(flux.T*q.adjugate()*j)[0]+(cr.T*q*cr)[0]/4
    assert iszero((-v*q+sym(j,flux)).det()-v*rhs)

    # Generic one-slide degree pattern, independently of a particular H5 stress.
    zz=S.symbols('u0:23')
    q=S.Matrix([[zz[0],zz[1],zz[3]+zz[4]*t],
                [zz[1],zz[2],zz[5]+zz[6]*t],
                [zz[3]+zz[4]*t,zz[5]+zz[6]*t,zz[7]+zz[8]*t+zz[9]*t*t]])
    j=S.Matrix([zz[10]+zz[11]*t,zz[12]+zz[13]*t,zz[14]+zz[15]*t+zz[16]*t*t])
    flux=S.Matrix([zz[17],zz[18],zz[19]+zz[20]*t]);v=zz[21]+zz[22]*t
    cr=j.cross(flux)
    terms=[-v*v*q.det(),v*(flux.T*q.adjugate()*j)[0],(cr.T*q*cr)[0]/4]
    degs=[S.Poly(S.expand(z),t).degree() for z in terms]
    assert all(d<=4 for d in degs)
    h=-v*q+sym(j,flux)
    assert all(S.Poly(h[i,k],t).degree()<=1 for i in (0,1) for k in (0,1))

    z,v,j=h5()
    # True closed-interval volume and independent actual solid fan moments.
    assert min(v.subs(t,0),v.subs(t,1))>0
    vv=0;jj=S.zeros(3,1);fan=[]
    for cell in TETS:
        a,b,c,d=(z[i] for i in cell)
        w=S.factor(S.det(S.Matrix.hstack(b-a,c-a,d-a))/6)
        if w.subs(t,R(1,2))<0:w=-w
        bs=bernstein(w)
        assert all(b>=0 for b in bs) and any(b>0 for b in bs)
        vv+=w;jj+=w*(a+b+c+d)/4;fan.append(str(w))
    assert iszero(vv-v) and iszero(jj-j)

    # True supporting facets, maximal cycle incidence and nonincident supports.
    supports=[];incident=0
    for face in FACES:
        a,b,c=(z[i] for i in face[:3]);n=(b-a).cross(c-a)
        for i in face:
            assert iszero(n.dot(z[i]-a));incident+=1
        for i in set(range(10))-set(face):
            inward=S.factor(-n.dot(z[i]-a));bs=bernstein(inward)
            assert all(b>=0 for b in bs) and any(b>0 for b in bs)
            supports.append(str(inward))
    assert incident==34 and len(supports)==56
    face_edges={tuple(sorted((a,b))) for face in FACES for a,b in zip(face,face[1:]+face[:1])}
    assert face_edges==set(EDGES)
    for a,b in EDGES:
        fs=[set(face) for face in FACES if a in face and b in face]
        assert len(fs)==2 and fs[0]&fs[1]=={a,b}
    turns=[]
    for i in range(7):
        u=z[(i+1)%7]-z[i];w=z[(i+2)%7]-z[(i+1)%7]
        turn=S.factor(u.cross(w)[2]);bs=bernstein(turn)
        assert all(b>=0 for b in bs) and any(b>0 for b in bs)
        turns.append(str(turn))

    chosen=((7,0),(8,2),(9,4));W=R(len(chosen));eta=R(1,500)
    flux=sum((z[k]-z[i] for i,k in chosen),S.zeros(3,1))
    q=sum((sym(z[i],z[k]-z[i]) for i,k in chosen),S.zeros(3))
    g=expand(-v*q+sym(j,flux))
    direct=sum((-sym(v*z[i]-j,z[k]-z[i]) for i,k in chosen),S.zeros(3))
    assert iszero(g-direct)
    # Volume-scaled margin preserves the exact rank-two determinant structure.
    qt=q+eta*W*S.eye(3);h=expand(g-eta*W*v*S.eye(3));cr=j.cross(flux)
    quartic=expand(-v*v*qt.det()+v*(flux.T*qt.adjugate()*j)[0]+(cr.T*qt*cr)[0]/4)
    assert iszero(h.det()-v*quartic)
    assert S.Poly(quartic,t).degree()==4  # Quartic degree is genuinely attained.
    transverse=h.extract((0,2),(0,2)) # only label 4 moves, in the Y direction
    assert all(S.Poly(e,t).degree()<=1 for e in transverse)
    endpoint_minors=[pd2(transverse.subs(t,a)) for a in (0,1)]
    assert all(m>0 for row in endpoint_minors for m in row)
    passed,sturm=strict_poly_interval(quartic)
    assert passed
    # A larger proposed margin fails and must not be accepted by endpoint A alone.
    rejected_eta=R(1,100)
    hr=expand(g-rejected_eta*W*v*S.eye(3))
    rejected_quartic=S.cancel(hr.det()/v)
    rejected,rejection=strict_poly_interval(rejected_quartic)
    assert not rejected and rejection['distinct_interior_roots']==1
    assert all(m>0 for a in (0,1) for m in pd2(hr.extract((0,2),(0,2)).subs(t,a)))

    report={
        'claim':'ONE_VERTEX_SLIDE_EXACT_QUARTIC_STRESS_CRITERION_V1',
        'scope':'one stress on a true free-r H5 interval; not an all-root atlas',
        'generic_quartic_term_degrees':[int(d) for d in degs],
        'volume':str(v),'first_moment':[str(e) for e in j],
        'fan_volumes':fan,'incident_identities':incident,'strict_inward_supports':len(supports),
        'basal_turns':turns,'true_edges':[list(e) for e in EDGES],
        'chosen_unit_arrows':[list(e) for e in chosen],
        'metric_scope':'every nonzero PSD M; no condition number restriction',
        'mean_arrow_margin':str(eta),
        'transverse_endpoint_minors':[[str(e) for e in row] for row in endpoint_minors],
        'quartic_sturm':sturm,'rejected_mean_margin':str(rejected_eta),'rejection_sturm':rejection,
        'closed_parameter_interval':['0','1'],
        'genuine_parameter_interval':'0<r<1; r=0 has collinear basal labels 2,3,4; r=1 has collapsed labels 4=5',
    }
    blob=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(dest).write_bytes(blob)
    print('GENERIC_VOLUME_DIVIDED_QUARTIC_IDENTITY_PASS',*[int(d) for d in degs])
    print('H5_FREE_R_THREE_ARROW_EXACT_STURM_PASS',str(eta),sturm['distinct_interior_roots'],incident,len(supports))
    print('OVERSIZED_MARGIN_REJECTED_PASS',str(rejected_eta),rejection['distinct_interior_roots'])
    print('REPORT_BYTES_SHA256',len(blob),hashlib.sha256(blob).hexdigest())
    print('PYTHON_SYMPY',sys.version.split()[0],S.__version__)

if __name__=='__main__':
    if not __debug__ or sys.version_info<(3,11):
        raise RuntimeError('Python >=3.11 with assertions enabled required')
    main(sys.argv[1] if len(sys.argv)>1 else 'edge_slide_quartic_report.json')
