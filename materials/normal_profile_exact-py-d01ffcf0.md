# material-d01ffcf04ad0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact rational algebra for actual facet normal variance and profile bounds.
CPython 3.13.5 standard library only. This checks polynomial identities and
rational controls; the continuum comparison proof is in the accompanying note.
"""
from fractions import Fraction as F
from math import comb
import hashlib, json
from pathlib import Path


def trim(p):
    p = tuple(map(F, p))
    while len(p) > 1 and not p[-1]:
        p = p[:-1]
    return p


def add(a, b):
    return trim(tuple((a[i] if i < len(a) else F(0)) +
                      (b[i] if i < len(b) else F(0))
                      for i in range(max(len(a), len(b)))))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def deriv(a):
    return trim(tuple(i*a[i] for i in range(1, len(a))) or (F(0),))


def evaluate(a, x):
    out = F(0)
    for c in reversed(a):
        out = out*x + c
    return out


class R:
    def __init__(self, n=0, d=1):
        self.n = trim(n if isinstance(n, (tuple, list)) else (F(n),))
        self.d = trim(d if isinstance(d, (tuple, list)) else (F(d),))
        assert self.d != (F(0),)
    @staticmethod
    def cast(x):
        return x if isinstance(x, R) else R(x)
    def __add__(self, other):
        other = R.cast(other)
        return R(add(mul(self.n, other.d), mul(other.n, self.d)), mul(self.d, other.d))
    __radd__ = __add__
    def __neg__(self):
        return R(neg(self.n), self.d)
    def __sub__(self, other):
        return self + -R.cast(other)
    def __rsub__(self, other):
        return R.cast(other) + -self
    def __mul__(self, other):
        other = R.cast(other)
        return R(mul(self.n, other.n), mul(self.d, other.d))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = R.cast(other)
        return R(mul(self.n, other.d), mul(self.d, other.n))
    def __rtruediv__(self, other):
        return R.cast(other) / self
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = R(1)
        for _ in range(n):
            out = out*self
        return out
    def diff(self):
        return R(add(mul(deriv(self.n), self.d), neg(mul(self.n, deriv(self.d)))), mul(self.d, self.d))
    def __eq__(self, other):
        other = R.cast(other)
        return mul(self.n, other.d) == mul(other.n, self.d)
    def at(self, x):
        return evaluate(self.n, x)/evaluate(self.d, x)


r = R((0, 1))
S0 = r*r+r+1
B0 = 3*r*r+2*r+1
# Exact integral of z**moment * (r+(1-r)*z)**power on [0,1].
def integral(power, moment=0):
    return sum((comb(power, j)*r**(power-j)*(1-r)**j / (j+moment+1)
                for j in range(power+1)), R(0))

v = integral(2)
m = integral(2, 1)/v
h = 1-m
var_z = integral(2, 2)/v-m*m
alpha = h/v
normal_variance = var_z/(h*h)
assert v == S0/3
assert m == (r*r+2*r+3)/(4*S0)
assert h == B0/(4*S0)
assert alpha == 3*B0/(4*S0*S0)
assert alpha.diff() == -9*r*r*(r+1)/(2*S0**3)
S = 3*(r**4+4*r**3+10*r*r+4*r+1)/(5*B0**2)
assert normal_variance == S
normal_gap = 3*r**4*(r*r+2*r+3)*(r*r+4*r+1)/(S0**2*B0**2)
assert 5*(1-alpha)*S-alpha == normal_gap
prism_factor = 6*r**6+48*r**5+81*r**4+72*r**3+36*r*r+8*r+1
prism_gap = (r-1)**2*prism_factor/(10*S0**2*B0**2)
assert S-F(2, 3)*alpha == prism_gap
Rnormal = (1-alpha)*S/alpha
Rtangent = integral(4)/(v*alpha)
assert Rnormal-F(1, 5) == 4*r**4*(r*r+2*r+3)*(r*r+4*r+1)/(5*B0**3)
assert Rtangent-F(4, 5) == 4*r**3*(r**3+2*r*r+3*r+3)/(5*B0)
assert all(c > 0 for c in prism_factor.n)
# The projected all-apex control has a positive, nonconcave normal density.
marginal = (F(6,13), F(0), F(3,26))
def even_integral(p, k=0):
    return sum((2*c/F(i+k+1) if (i+k)%2 == 0 else F(0)
                for i,c in enumerate(p)), F(0))
assert even_integral(marginal) == 1
assert even_integral(marginal, 1) == 0
control_alpha = evaluate(marginal, F(1))
control_variance = even_integral(marginal, 2)
assert control_alpha == F(15,26)
assert control_variance == F(23,65)
assert control_variance-F(2,3)*control_alpha == F(-2,65)
assert 5*(1-control_alpha)*control_variance-control_alpha == F(29,169)
# Exact examples are actual square-base homothetic frusta, not 110 bodies.
controls = []
for x in (F(0),F(1,4),F(1,2),F(1),F(2),F(4)):
    A, s, rn, rt = (f.at(x) for f in (alpha,S,Rnormal,Rtangent))
    assert 0 < A <= F(3,4) and s >= F(2,3)*A
    assert 5*(1-A)*s >= A and rn >= F(1,5) and rt >= F(4,5)
    controls.append(dict(r=str(x),alpha=str(A),normal_variance=str(s),
                         B_Sigma_normal=str(rn),B_Sigma_tangent=str(rt)))
report = {
    'polynomial_identities': 'All displayed identities checked by exact coefficient arithmetic',
    'frustum_controls': controls,
    'projected_nonphysical_control': {
        'density_coefficients': [str(x) for x in marginal],
        'alpha':str(control_alpha),'variance':str(control_variance),
        'variance_minus_two_alpha_over_three':'-2/65',
        'five_one_minus_alpha_variance_minus_alpha':'29/169'},
    'scope': 'Exact algebra and rational actual-frustum controls; continuum proof is analytic. No E17 exclusion or 110 construction.'}
blob = (json.dumps(report, indent=2, sort_keys=True)+'\n').encode()
name = Path('normal_profile_exact_report.json')
name.write_bytes(blob)
print('FACET_NORMAL_PROFILE_EXACT_V1 PASS',len(blob),hashlib.sha256(blob).hexdigest())
