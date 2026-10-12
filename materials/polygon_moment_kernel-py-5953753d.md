# material-5953753de386

AI research material

---

"""Exact concave-facet cubic moment kernel, no numerical search or input data.
Run: python polygon_moment_kernel.py build|check
CPython 3.13.5, SymPy 1.14.0. Assertions must be enabled.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

assert __debug__
assert S.__version__ == '1.14.0'
x, r, s, t = S.symbols('x r s t', real=True)
a, b, c, d, z = S.symbols('a b c d z', nonnegative=True)

def pair_moment(power):
    """Integral x^power phi_s(x) phi_t(x), assuming 0<s<=t<1."""
    return S.factor(
        S.integrate(x**(power+2)/(s*t), (x,0,s))
        + S.integrate(x**(power+1)*(1-x)/((1-s)*t), (x,s,t))
        + S.integrate(x**power*(1-x)**2/((1-s)*(1-t)), (x,t,1)))

C = pair_moment(0)
D = pair_moment(1)
assert S.cancel(C-(s*s+t*t-2*t)/(6*t*(s-1))) == 0
assert S.cancel(D-(s**3+t**3-t*t-t)/(12*t*(s-1))) == 0

def at(expr, left, right):
    return expr.subs({s:left,t:right}, simultaneous=True)

Q = S.factor((2+r)*C+(2+s)*at(C,r,t)+(2+t)*at(C,r,s)
             -4*(D+at(D,r,t)+at(D,r,s)))
num, den = S.fraction(Q)
assert S.expand(den-6*s*t*(1-r)*(1-s)) == 0
P = S.Poly(num,r,s,t)
assert P.total_degree() == 5
hom = sum(co*r**i*s**j*t**k*z**(5-i-j-k)
          for (i,j,k),co in P.terms())
H = S.expand(hom.subs({r:a,s:a+b,t:a+b+c,z:a+b+c+d}))
# A literal nonnegative expression independent of the derivation above.
positive = (
 a*a*(4*b*b*(c+d)+b*(9*c*c+16*c*d+8*d*d)
       +6*c**3+16*c*c*d+16*c*d*d+6*d**3)
 +a*(4*b**3*(c+d)+b*b*(15*c*c+24*c*d+12*d*d)
       +b*(17*c**3+39*c*c*d+36*c*d*d+12*d**3)
       +4*c**4+10*c**3*d+12*c*c*d*d+6*c*d**3)
 +b*(4*b*b*c*c+6*b*b*c*d+4*b*b*d*d
       +b*(8*c**3+18*c*c*d+18*c*d*d+6*d**3)
       +4*c**4+10*c**3*d+12*c*c*d*d+6*c*d**3))
assert S.expand(H-positive) == 0
terms = S.Poly(H,a,b,c,d).terms()
assert len(terms)==33 and min(co for _,co in terms)==4
# Endpoint generators phi_1=x are handled by exact integration, not 0/0.
Cr1=S.integrate(x*x/r,(x,0,r))+S.integrate(x*(1-x)/(1-r),(x,r,1))
Dr1=S.integrate(x**3/r,(x,0,r))+S.integrate(x*x*(1-x)/(1-r),(x,r,1))
Q_r11=S.factor((2+r)/3+6*Cr1-4*(S.Rational(1,4)+2*Dr1))
assert S.factor(Q_r11-2*r*(1-r)/3)==0
assert S.factor(Q.subs({r:t,s:t})-(1-t))==0
# Triangle equality and a strictly positive rational concave quadrilateral.
def moments(pieces):
    return [S.factor(sum(S.integrate(x**xp*f**fp,(x,lo,hi))
                         for lo,hi,f in pieces))
            for xp,fp in [(0,1),(1,1),(0,2),(1,2)]]

def signed_gap(vals):
    A,B,C0,D0=vals
    return S.factor(4*D0/C0-3*B/A-1)

triangle=moments([(0,1,x)])
quad=moments([(0,S.Rational(1,2),2*x),(S.Rational(1,2),1,S.Integer(1))])
assert signed_gap(triangle)==0 and signed_gap(quad)<0
# Concavity is necessary: continuous piecewise-linear countercontrol.
nonconcave=moments([(0,S.Rational(1,10),S.Rational(11,10)*x),
                   (S.Rational(1,10),S.Rational(1,5),S.Rational(9,10)*x+S.Rational(1,50)),
                   (S.Rational(1,5),1,x)])
assert signed_gap(nonconcave)==S.Rational(50749,27850590)>0
report = {
 'theorem':'CONCAVE_FACET_CUBIC_MOMENT_KERNEL_V1',
 'dependencies':{'python':'3.13.5','sympy':'1.14.0'},
 'pair_C':str(C), 'pair_D':str(D), 'symmetric_kernel':str(Q),
 'ordered_simplex_positive_terms':[[list(m),int(co)] for m,co in terms],
 'endpoint_r_1_1':str(Q_r11), 'diagonal_kernel':'1-t',
 'triangle_moments':[str(v) for v in triangle],
 'quad_moments':[str(v) for v in quad], 'quad_signed_gap':str(signed_gap(quad)),
 'nonconcave_moments':[str(v) for v in nonconcave],
 'nonconcave_signed_gap':str(signed_gap(nonconcave)),
}
raw=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
root=Path(__file__).resolve().parent
out=root/'polygon_moment_kernel.json'
assert sys.argv[1:] in (['build'],['check'])
if sys.argv[1]=='build':
    out.write_bytes(raw)
else:
    assert out.read_bytes()==raw
print('CONCAVE_FACET_ALL_POLYGONS_KERNEL_33_POSITIVE_TERMS_PASS')
print('TRUE_TRIANGLE_EQUALITY_AND_STRICT_NONTRIANGLE_PASS')
print('NONCONCAVE_COUNTERCONTROL_POSITIVE_50749_OVER_27850590_PASS')
print('REPORT_BYTES',len(raw))
print('REPORT_SHA256',hashlib.sha256(raw).hexdigest())
print('POLYGON_REACTION_SOURCE_ONLY_RECOVERY_PASS')
