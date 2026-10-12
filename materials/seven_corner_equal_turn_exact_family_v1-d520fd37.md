# material-d520fd37fe17

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# SEVEN_CORNER_EQUAL_TURN_FAMILY_V1

## Exact family, not a global seven-corner exclusion
Let f(t)=8t^3-8t^2+3t-1, let t0 be its unique real root, and set u=2t-1,d=sqrt(t(1-t)),lambda=t*u. For64/89<=t<=t0 define the seven planar vertices
q0=(1,0),
q1=(u*(8-8t-1/t),4*u^2*d/t),
q2=(u*(3-4t),u*d*(4t-1)/t),
q3=(-u^2,2*u*d),
q4=(-t*u,u*d),
q5=(-t*u,0),
q6=(u^2,-2*u*d).

The polygon is strictly convex, has0 in its interior, satisfies -lambda Q subset Q, and has exactly one STRICT radial-maximum corner0. Its selected true-boundary arborescence has parents(0,0,1,2,3,4,0) and allows weak arrows. The arrow1->0 has D10=-u*f(t)/t^2>=0. The other five selected arrows are identically0. Both outgoing arrows at0 are strictly negative. The containment constraint on edge5->6 applied to-lambda*q1 is -2*d*u^2*f(t)>=0. Structural containment equalities are edge4->5 and5->6 applied to-lambda*q0=q5; all other support constraints are strictly positive, except the additional f-dependent equality at t0.

The derivative f'(t)=24(t-1/3)^2+1/3 is positive. Exact endpoint signs isolate t0 in(64/89,13/18). Therefore lambda0=t0*(2*t0-1)<26/81<1/3. Numerically lambda0 is approximately0.31738271052. This explains the earlier numerical equal-turn candidate, now as a certified exact family. It does NOT prove arbitrary seven-corner shapes satisfy lambda<=lambda0, or exclude seven corners at lambda=1/3. The missing global reduction is substantive.

Four last long-chain steps are multiplication by t+i*d. Thus q6=-q3, and q5=(-lambda,0). Within this displayed equal-turn ansatz and its chosen rooted routing, the first arrow imposes t<=t0 for1/2<t<1; lambda grows there, so the limiting lambda0 is its exact optimum. This is an ansatz statement, not a global optimality theorem. Convexity puts the whole polygon to the right of its true vertical edgeq4q5, so no coefficient larger than lambda works for the individual polygon, because-lambda' q0 would have x<-lambda.

At t=64/89,d=40/89 the coordinates are rational:
(1,0),(190281/506944,7605/15842),(429/7921,32565/63368),(-1521/7921,3120/7921),(-2496/7921,1560/7921),(-2496/7921,0),(1521/7921,-3120/7921), with lambda=2496/7921.

For every positive lambda'<lambda0, a STRICT rooted seven-corner control exists with strict -lambda' containment: start at t0, for which decreasing the containment coefficient makes every support inequality strict because0 is interior. Then multiply each qi by rho^depth(i), with depths(0,1,2,3,4,5,1) and rho<1 sufficiently close to1. Every selected weak child-to-parent arrow becomes strictly positive since its parent is shrunk less; the previously strict root arrows, convexity, interiority and strict containment persist by openness. This does not reach1/3 and gives no actual centred homogeneous3D lift.

## Exact certificate and recovery
The code below proves the entire parameter interval, not just a sample. It checks92 positive rational polynomial blocks by exact Bernstein coefficients on[64/89,13/18], treating the sole exceptional support constraint and first arrow as positive factors times-f(t). It includes the true-corner, origin, root-strict and equal-turn identities. All computations are exact. The coordinator executed it successfully with CPython3.13.5 and SymPy1.14.0. No other nonstandard package or input file is required. Do not disable assertions.

Save as verify_seven_equal_turn_v1.py using UTF-8/LF. Run:
python -B verify_seven_equal_turn_v1.py > seven_equal_turn_v1.out
Expected terminal ALL_VERIFIED_SEVEN_EQUAL_TURN_V1.

Pins for the stated environment:
verify_seven_equal_turn_v1.py:4227bytes,SHA256bc7111320973eb51ea3099ab81f4599ab86a7dface064f89ccb54c324a9fb342
seven_equal_turn_v1.json:31549bytes,SHA2561bf864dc6fc2e2a07c669b0db4ab5b3f08d9630979023608dadb6a3565ba431e
seven_equal_turn_v1.out:33bytes,SHA2563572326642b4b68b71b7f517930d0cc09e8952790789af197ff217cf746eec72
The JSON contains environment strings, so its byte hash is environment-specific. The symbolic assertions do not use floating arithmetic. Earlier numerical locator source is separately preserved in [internal-source-reference]; it is not an input to this certificate.

```python
#!/usr/bin/env python3
"""Exact equal-turn seven-corner family; no global seven-corner exclusion."""
import hashlib
import json
from math import comb
from pathlib import Path
import platform
import sympy as s

t = s.symbols('t')
a, b = s.Rational(64, 89), s.Rational(13, 18)
u = 2*t-1
lam = t*u
f = 8*t**3-8*t**2+3*t-1
# Physical coordinates are (X, sqrt(t*(1-t))*Y).
q = ((s.Integer(1), s.Integer(0)),
     (u*(8-8*t-1/t), 4*u*u/t),
     (u*(3-4*t), u*(4*t-1)/t),
     (-u*u, 2*u), (-lam, u), (-lam, s.Integer(0)),
     (u*u, -2*u))
parent = (0,0,1,2,3,4,0)

def sub(x,y): return tuple(xx-yy for xx,yy in zip(x,y))
def scale(x,c): return tuple(xx*c for xx in x)
def cross_scaled(x,y): return s.cancel(x[0]*y[1]-x[1]*y[0])
def dot(x,y): return s.cancel(x[0]*y[0]+t*(1-t)*x[1]*y[1])

def bernstein(poly):
    z = s.symbols('z')
    p = s.Poly(s.expand(poly.subs(t,a+(b-a)*z)),z)
    n = p.degree()
    power = list(reversed(p.all_coeffs()))
    return tuple(sum(power[j]*s.Rational(comb(k,j),comb(n,j))
                     for j in range(k+1)) for k in range(n+1))

def positive(rat):
    num, den = s.fraction(s.cancel(rat))
    bn, bd = bernstein(num), bernstein(den)
    assert min(bn)>0 and min(bd)>0, (rat,bn,bd)
    return {'numerator':str(num),'denominator':str(den),
            'numerator_bernstein':list(map(str,bn)),
            'denominator_bernstein':list(map(str,bd))}

def verify():
    # f has one real root t0, isolated by [a,b]; it is strictly increasing.
    assert s.expand(s.diff(f,t)-24*(t-s.Rational(1,3))**2-s.Rational(1,3))==0
    assert f.subs(t,a)<0<f.subs(t,b)
    assert lam.subs(t,b)==s.Rational(26,81)<s.Rational(1,3)
    certificates={}
    zeros=[]
    f_cells=[]
    for i in range(7):
        edge=sub(q[(i+1)%7],q[i])
        certificates[f'origin_{i}']=positive(cross_scaled(q[i],q[(i+1)%7]))
        for j in range(7):
            if j not in (i,(i+1)%7):
                certificates[f'convex_{i}_{j}']=positive(cross_scaled(edge,sub(q[j],q[i])))
            value=cross_scaled(edge,sub(scale(q[j],-lam),q[i]))
            if value==0:
                zeros.append([i,j])
            elif (i,j)==(5,1):
                assert s.cancel(value+2*u*u*f)==0
                certificates[f'contain_factor_{i}_{j}']=positive(value/(-f))
                f_cells.append([i,j])
            else:
                certificates[f'contain_{i}_{j}']=positive(value)
    assert zeros==[[4,0],[5,0]] and f_cells==[[5,1]]
    selected=[dot(q[i],sub(q[parent[i]],q[i])) for i in range(1,7)]
    assert s.cancel(selected[0]+u*f/t**2)==0
    assert all(value==0 for value in selected[1:])
    certificates['first_arrow_factor']=positive(u/t**2)
    for j in (1,6):
        certificates[f'root_strict_{j}']=positive(-dot(q[0],sub(q[j],q[0])))
    # The four equal-turn steps preserve the prescribed weak reverse arrows.
    for i in range(1,5):
        transformed=(t*q[i][0]-t*(1-t)*q[i][1],q[i][0]+t*q[i][1])
        assert all(s.cancel(c)==0 for c in sub(transformed,q[i+1]))
    # Rational endpoint: t=a, sqrt(t*(1-t))=40/89.
    d=s.Rational(40,89)
    assert d*d==a*(1-a)
    rational_q=[[str(s.cancel(x.subs(t,a))),str(s.cancel(d*y.subs(t,a)))] for x,y in q]
    report={
        'identity':'SEVEN_CORNER_EQUAL_TURN_FAMILY_V1',
        'python':platform.python_version(),'sympy':s.__version__,
        'root_polynomial':str(f),'isolating_interval':[str(a),str(b)],
        'parameter_domain':'64/89 <= t <= the unique real root t0 of f',
        'lambda':'t*(2*t-1)', 'lambda_upper_bound':'26/81 < 1/3',
        'containment_zero_pairs':zeros,'containment_minus_f_pair':f_cells,
        'rational_endpoint_lambda':str(lam.subs(t,a)),
        'rational_endpoint_points':rational_q,'parent':parent,
        'strict_radial_maxima':[0], 'selected_weak_arrows':'2,3,4,5,6; also 1 at t0',
        'global_seven_corner_impossibility_proved':False,
        'actual_centred_3d_lift_claimed':False,
        'certificates':certificates,
        'terminal':'ALL_VERIFIED_SEVEN_EQUAL_TURN_V1'
    }
    return report

if __name__=='__main__':
    report=verify()
    data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
    Path('seven_equal_turn_v1.json').write_bytes(data)
    print(report['terminal'])
```
