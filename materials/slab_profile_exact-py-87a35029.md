# material-87a350298080

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact identities and a piecewise-quadratic projected-law countercontrol.
CPython 3.13.5, SymPy 1.14.0. No files or inputs are required.
This is not an equilibrium construction; the analytic iff theorem is separate.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sy


def integrate(coeff, power, lo, hi):
    return sum(c * (hi**(i+power+1)-lo**(i+power+1)) / F(i+power+1)
               for i, c in enumerate(coeff))


def value(coeff, t):
    return sum(c*t**i for i,c in enumerate(coeff))


def slab(coeff, lo, hi):
    mass = integrate(coeff, 0, lo, hi)
    mean = integrate(coeff, 1, lo, hi)/mass
    variance = integrate(coeff, 2, lo, hi)/mass-mean**2
    h = hi-mean
    assert mass > 0 and h > 0 and variance > 0
    return (value(coeff, hi)*h/mass, variance/(h*h), mass, mean)


r = F(11,10)
A = 3*(3*r*r+2*r+1)/(4*(r*r+r+1)**2)
S = 3*(r**4+4*r**3+10*r*r+4*r+1)/(5*(3*r*r+2*r+1)**2)
a = F(1,5)
c = F(1,2)
b = (2*A*(1-a/3)-1+a)/((1-c)**2-2*A*(1-c)**3/3)
assert b == F(79712,231215)
central = (F(1), F(0), -a)
right = (1+b*c*c, -2*b*c, b-a)
left = (1+b*c*c, 2*b*c, b-a)
assert value(central,c) == value(right,c)
assert -2*a*c == right[1]+2*right[2]*c
assert value(central,-c) == value(left,-c)
assert 2*a*c == left[1]-2*left[2]*c
Z = 2*(integrate(central,0,F(0),c)+integrate(right,0,c,F(1)))
variance = 2*(integrate(central,2,F(0),c)+integrate(right,2,c,F(1)))/Z
alpha = value(right,F(1))/Z
assert Z == F(438244,231215)
assert alpha == A == F(51225,109561)
assert variance == F(703971,2191220)
assert variance-S == F(9071304927,1022180026580) > 0
# p(x)>=1-a and |p'(x)|<=2a+2b(1-c) for |x|<=1.
# Thus 2p(x)-(x-z)p'(x) has this strictly positive lower bound
# for ALL tested apices z in [-1,1]. Boundary terms are nonnegative.
euler_lower = 2*(1-a)-2*(2*a+2*b*(1-c))
assert euler_lower == F(25548,231215) > 0
# sqrt(p) has positive second derivative on each outer interval.
discriminant = right[1]**2-4*right[0]*right[2]
assert discriminant == F(-589668,1156075) < 0
local_alpha, local_variance, local_mass, local_mean = slab(right,F(89,100),F(91,100))
local_gap = local_variance-F(2,3)*local_alpha
assert local_gap < 0
assert F(49,100) < local_alpha < F(1,2)

# Exact Taylor identities at a smooth point. Variables aa,bb are rho'/rho
# and rho''/(2rho), respectively; e is the symmetric slab half-width.
e,aa,bb = sy.symbols('e aa bb')
v = 2+sy.Rational(2,3)*bb*e**2
m = sy.Rational(2,3)*aa*e/v
h = 1-m
al = (1+aa*e+bb*e**2)*h/v
vv = ((sy.Rational(2,3)+sy.Rational(2,5)*bb*e**2)/v-m*m)/(h*h)
jet = lambda f: sy.series(f,e,0,3).removeO().expand()
aljet = jet(al)
vjet = jet(vv)
assert sy.expand(aljet-(sy.Rational(1,2)+aa*e/3+(-aa**2/6+bb/3)*e**2)) == 0
assert sy.expand(vjet-(sy.Rational(1,3)+2*aa*e/9+4*bb*e**2/45)) == 0
rr = sy.symbols('r')
Ar = 3*(3*rr**2+2*rr+1)/(4*(rr**2+rr+1)**2)
Sr = 3*(rr**4+4*rr**3+10*rr**2+4*rr+1)/(5*(3*rr**2+2*rr+1)**2)
derA = lambda f: sy.diff(f,rr)/sy.diff(Ar,rr)
assert Ar.subs(rr,1) == sy.Rational(1,2)
assert Sr.subs(rr,1) == sy.Rational(1,3)
assert derA(Sr).subs(rr,1) == sy.Rational(2,3)
assert derA(derA(Sr)).subs(rr,1) == sy.Rational(7,5)
refjet = sy.Rational(1,3)+sy.Rational(2,3)*(aljet-sy.Rational(1,2))+sy.Rational(7,10)*(aljet-sy.Rational(1,2))**2
assert sy.expand(jet(vjet-refjet)-(aa**2-4*bb)*e**2/30) == 0
# One-sided density slopes produce the first-order kink test.
k = sy.symbols('k')
vk = 2+k*e
mk = sy.Rational(2,3)*aa*e/vk
hk = 1-mk
ak = (1+(aa+k)*e)*hk/vk
sk = ((sy.Rational(2,3)+k*e/2)/vk-mk*mk)/(hk*hk)
assert sy.simplify(sy.limit((sk-sy.Rational(1,3)-sy.Rational(2,3)*(ak-sy.Rational(1,2)))/e,e,0)) == -k/12

report = {
 'status':'EXACT_IDENTITIES_AND_NONPHYSICAL_CONTROL_PASS',
 'density':{'central':[str(x) for x in central], 'left':[str(x) for x in left],
            'right':[str(x) for x in right], 'knots':['-1','-1/2','1/2','1'], 'normalizer':str(Z)},
 'global':{'r':str(r),'alpha_both_ends':str(alpha),'variance':str(variance),
           'sharp_reference':str(S),'sharp_gap':str(variance-S)},
 'all_apex':{'unnormalized_bulk_numerator_lower':str(euler_lower),
             'Euler_exponent':3,'dimension_of_visible_law':1},
 'outer_quadratic_discriminant':str(discriminant),
 'violating_slab':{'lo':'89/100','hi':'91/100','mass_unnormalized':str(local_mass),
                  'mean':str(local_mean),'alpha':str(local_alpha),
                  'variance_normalized':str(local_variance),'gap_vs_two_alpha_over_three':str(local_gap)},
 'smooth_jet_gap':'(aa**2-4*bb)*e**2/30 + o(e**2)',
 'kink_jet_gap':'-k*e/12 + O(e**2)',
 'limitations':'No actual convex3D lift exists. No equilibrium census, E17 exclusion or110 attainer is claimed.'}
blob = (json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
Path('slab_profile_exact_report.json').write_bytes(blob)
print('SLAB_PROFILE_REALIZATION_EXACT_V1 PASS',len(blob),hashlib.sha256(blob).hexdigest())
