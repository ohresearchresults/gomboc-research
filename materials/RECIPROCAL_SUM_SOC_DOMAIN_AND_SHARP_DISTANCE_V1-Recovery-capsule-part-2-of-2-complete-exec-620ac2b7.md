# material-620ac2b7b8d0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact identities for RECIPROCAL_SUM_SOC_DOMAIN_AND_SHARP_DISTANCE_V1.
Python >=3.11, SymPy 1.14.0. Run with assertions enabled:
  python -B reciprocal_sum_soc.py build
  python -B reciprocal_sum_soc.py check
No external input, random seed, inherited code or numerical optimization.
The continuum theorem is in the accompanying complete analytic proof.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as sp

assert __debug__ and sys.version_info >= (3, 11)
if len(sys.argv) != 2 or sys.argv[1] not in ('build', 'check'):
    raise SystemExit('usage: python -B reciprocal_sum_soc.py build|check')

k, r, t = sp.symbols('k r t', positive=True)
u, v = sp.symbols('u v', real=True)
P, Q = r*t+t+1, r*t+r+1
a = r*t/P + 1/Q
b = 1/P + r*t/Q
c = t/P + r/Q
d = k*k+k+1

def phi(kk, aa, cc):
    return ((kk*kk-1)**2*(1-aa-cc)
            +(kk**4+kk**3+2*kk**2+kk+1)*aa*cc
            -kk*(kk*kk+kk+1)*(aa*aa+cc*cc))

identities = []
def identity(name, value):
    assert sp.factor(value) == 0, name
    identities.append(name)

identity('trace_sum', a+b+c-2)
identity('ordered_top_difference', a-b-(r-t)*(r*t-1)/(P*Q))
identity('ordered_bottom_difference', b-c-(t-1)*(r*r*t-1)/(P*Q))
H = ((k-1)**2*(t*t+t+1)*(r*r*t*t+r*t+1)
     +3*k*(r*t*t-1)**2)
identity('global_ratio_sign_factorization',
         phi(k,a,c)-(k-r)*(k*r-1)*H/(P*P*Q*Q))
right = 2*(k+1)**2/d-u-v
radicand = (u-v)**2+4*k*(k-1)**2/d**2
identity('exact_soc_square_identity',
         right**2-(k+1)**2/(k-1)**2*radicand
         -4*phi(k,u,v)/((k-1)**2*d))
identity('scalar_positive_margin', phi(k,sp.Rational(2,3),sp.Rational(2,3))
         -(k-1)**4/9)

ak, ck = a.subs(r,k), c.subs(r,k)
m = k*(k-t)*(2*k*t+k+t+2)/((k*k*t-1)*(k*k*t+2*k*t+2*k+1))
h = (k-1)*(k+1)*(k*k*t*t+k*t*t+2*k*t+k+1)/(
    (k*k*t-1)*(k*k*t+2*k*t+2*k+1))
identity('boundary_exact', phi(k,ak,ck))
identity('tangent_slope', sp.diff(ak,t)+m*sp.diff(ck,t))
identity('tangent_intercept', ak+m*ck-h)
identity('first_tangent_slope', m.subs(t,1)-3*k/(k*k+4*k+1))
identity('first_tangent_intercept', h.subs(t,1)-1)
identity('last_tangent_slope', m.subs(t,k))
identity('last_tangent_intercept', h.subs(t,k)-(k*k+1)/d)
identity('positive_curvature_numerator',
         sp.diff(ak,t,2)*sp.diff(ck,t)-sp.diff(ak,t)*sp.diff(ck,t,2)
         -2*k*(k-1)*(k+1)*(k*k+k+1)/(
             (k*t+k+1)**3*(k*t+t+1)**3))
identity('rational_k9_soc',
         (800-364*(u+v))**2-(455*(u-v))**2-240**2-91*phi(9,u,v))

controls = 0
for kk in (sp.Rational(3,2), sp.Integer(3), sp.Integer(9)):
    for rr in (sp.Integer(1),sp.Rational(5,4),sp.Integer(2),sp.Integer(3),
               sp.Rational(9,2),sp.Integer(8),sp.Integer(9),sp.Integer(10),sp.Integer(12)):
        for tt in (sp.Integer(1),(rr+1)/2,rr):
            aa,bb,cc = [sp.factor(x.subs({r:rr,t:tt})) for x in (a,b,c)]
            assert 1>aa>=bb>=cc>0 and aa+bb+cc==2
            f = sp.factor(phi(kk,aa,cc))
            assert sp.sign(f)==sp.sign(kk-rr)
            assert (f>=0)==(rr<=kk) and (f>0)==(rr<kk)
            controls += 1

root = sp.sqrt(10721)
t0 = (89+root)/180
a0,c0 = sp.Rational(9,10),sp.Rational(11,20)
astar = (40*root-2551)/1820
bstar = sp.Rational(29,20)-astar
delta = (4189-40*root)/1820
identity('nearest_boundary_top', ak.subs({k:9,t:t0})-astar)
identity('nearest_boundary_bottom', ck.subs({k:9,t:t0})-c0)
identity('distance_formula', a0-astar-delta)
identity('distance_polynomial', 36400*delta**2-167560*delta+4331)
identity('formal_control_gap', phi(9,a0,c0)+sp.Rational(38979,400))
assert bool(1<t0) and bool(t0<9)
assert bool(astar>bstar) and bool(bstar>c0)
assert bool(sp.Rational(2599,100000)<delta) and bool(delta<sp.Rational(13,500))
m0 = sp.simplify(m.subs({k:9,t:t0}))
assert bool(m0>0) and bool(m0<1)
assert sp.simplify(bstar-c0-delta)==0

report = {
  'object':'RECIPROCAL_SUM_SOC_DOMAIN_AND_SHARP_DISTANCE_V1',
  'identity_names':identities,
  'exact_rational_controls':controls,
  'phi9_S0':str(-sp.Rational(38979,400)),
  'distance':str(delta),
  'distance_polynomial':[36400,-167560,4331],
  'distance_rational_bracket':['2599/100000','13/500'],
  'nearest_ordered_spectrum':[str(astar),str(bstar),str(c0)],
  'boundary_t':str(t0),
}
data=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
path=Path(__file__).with_suffix('.json')
if sys.argv[1]=='build':
    path.write_bytes(data)
else:
    assert path.read_bytes()==data
print('RECIPROCAL_SUM_SOC_EXACT_PASS',len(identities),controls,
      len(data),hashlib.sha256(data).hexdigest())
