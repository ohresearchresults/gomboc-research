# material-f0e7529ccae5

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# DLV pole recovery capsule part2/2: complete exact executable
Object identity DLV_POLE_AND_MOBIUS_BOX_20260923. Companion proof is part1 [internal-source-reference]. Save the following exact block as pole_cert.py, including terminal newline. Source5684 bytes SHA25678ed9c52ac9908634cc63d0c4f7d854cafceba95d4c8373c4a22a3ef8192ea9f. CPython3.13.5 standard library only, assertions enabled. No other source/input dependencies. Run python -B -S pole_cert.py; output POLE_CERT.json1468 bytes SHA25644e0647a425ae87c86939929cf2c21ed0c4f745bc300a6079c9e74afd9b1c521. Expected marker DLV_MOBIUS_SCOPED_NONCONVEXITY_EXACT_PASS 1468 44e0647a425ae87c86939929cf2c21ed0c4f745bc300a6079c9e74afd9b1c521. Original and clean-directory replay outputs matched.

```python
"""Exact rational-interval certificate for a latitude-warp DLV meridian.
Python 3.13.5 standard library only. Run: python -B -S pole_cert.py
This proves a scoped raw-surface nonconvexity box, NOT absence of a polyhedron.
"""
from fractions import Fraction as F
import json, hashlib

class I:
    def __init__(self, lo, hi=None):
        if isinstance(lo,I): self.lo,self.hi=lo.lo,lo.hi;return
        self.lo=F(lo);self.hi=F(lo if hi is None else hi);assert self.lo<=self.hi
    def __add__(self,o):
        o=I(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I(o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=I(o);p=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi];return I(min(p),max(p))
    __rmul__=__mul__
    def inv(self):
        assert self.lo*self.hi>0
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o):return self*I(o).inv()
    def __rtruediv__(self,o):return I(o)*self.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2:return I(self.lo**n,self.hi**n)
        return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def rounded(self,scale=10**6):
        # Integer outward bounds, divided by the declared scale.
        low=(self.lo.numerator*scale)//self.lo.denominator
        high=-((-self.hi.numerator*scale)//self.hi.denominator)
        return [low,high,scale]

class J:
    """Value and first TWO derivatives (not Taylor coefficients) in normalized x."""
    def __init__(self,v,d=0,e=0):
        if isinstance(v,J):self.v,self.d,self.e=v.v,v.d,v.e;return
        self.v,self.d,self.e=I(v),I(d),I(e)
    def __add__(self,o):
        o=J(o);return J(self.v+o.v,self.d+o.d,self.e+o.e)
    __radd__=__add__
    def __neg__(self):return J(-self.v,-self.d,-self.e)
    def __sub__(self,o):return self+-J(o)
    def __rsub__(self,o):return J(o)+-self
    def __mul__(self,o):
        o=J(o);return J(self.v*o.v,self.d*o.v+self.v*o.d,self.e*o.v+2*self.d*o.d+self.v*o.e)
    __rmul__=__mul__
    def inv(self):return J(1/self.v,-self.d/self.v**2,2*self.d**2/self.v**3-self.e/self.v**2)
    def __truediv__(self,o):return self*J(o).inv()
    def __rtruediv__(self,o):return J(o)*self.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=J(1)
        for _ in range(n):out=out*self
        return out

def arctan_bound(q,terms=48):
    q=F(q);assert 0<q<1
    v=sum((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(terms))
    r=(-1)**terms*q**(2*terms+1)/F(2*terms+1)
    return I(min(v,v+r),max(v,v+r))

def sincos(t,terms=20):
    t=I(t);assert max(abs(t.lo),abs(t.hi))<=2
    si=I(0);co=I(0);fact=1
    for k in range(2*terms+1):
        if k:fact*=k
        if k%2:si+=((-1)**((k-1)//2))*t**k/F(fact)
        else:co+=((-1)**(k//2))*t**k/F(fact)
    # Lagrange remainder of degree 40 for each: |derivative|<=1 on R.
    rem=max(abs(t.lo),abs(t.hi))**(2*terms+1)/F(fact*(2*terms+1))
    err=I(-rem,rem)
    return si+err,co+err

def Fa(a,x):
    return (a*x*x+(1-a)*(1-x)**2*a*x/(a+x))/(a*x+(1-a)*(1-x)**2)

def main():
    # Compact rational box contains one of the numerical mass-balance scouts.
    a=I(F(17300,10**6),F(17310,10**6))
    d=I(F(1999,10000),F(2001,10000))
    b=I(F(3999,10000),F(4001,10000))
    pi=16*arctan_bound(F(1,5))-4*arctan_bound(F(1,239))
    assert I(F(3141592653589793238462643383279,10**30),F(3141592653589793238462643383280,10**30)).lo<pi.lo
    assert pi.hi<F(3141592653589793238462643383280,10**30)
    x=J(F(15,16),1,0)
    w=J(b)*x/(1+J(b-1)*x)
    f=Fa(J(a),w)
    angle=pi*(f.v-F(1,2))
    sn,cs=sincos(angle)
    # theta=pi(x-1/2); f_angle=pi(F_a(w)-1/2).
    # Therefore derivative of f_angle in theta is f.d, second is f.e/pi.
    r=1+d*sn
    rp=d*cs*f.d
    rpp=d*(-sn*f.d**2+cs*f.e/pi)
    curvature=r*r+2*rp*rp-r*rpp
    # At top and C=0, the incoming coefficient is R(d/b^2-R)/2.
    R=1+d;top=R*(d/b**2-R)/2
    # At bottom, radial r=B+d*b^2*eps^2/2; nonnegative curvature requires B-d*b^2>=0.
    bottom=1-d-d*b*b
    assert top.lo>0,top.rounded()
    assert bottom.lo>0,bottom.rounded()
    assert curvature.hi<0,curvature.rounded()
    out={
        'name':'DLV_MOBIUS_TOP_ESCAPE_NONCONVEX_BOX',
        'a':[str(a.lo),str(a.hi)],'d':[str(d.lo),str(d.hi)],'warp':[str(b.lo),str(b.hi)],
        'normalized_latitude_x':'15/16','meridian_phi':'0','theta':'7*pi/16',
        'pi':pi.rounded(10**30),'angle':angle.rounded(),
        'r':r.rounded(),'r_theta':rp.rounded(),'r_theta_theta':rpp.rounded(),
        'top_incoming_coefficient_at_reference_zero':top.rounded(),
        'bottom_axial_curvature_factor':bottom.rounded(),
        'meridian_convexity_numerator':curvature.rounded(),
        'bound_format':'[integer_lower,integer_upper,positive_denominator]',
        'scope':'Every raw radial surface in this closed parameter box fails convexity. No exact mass balance is asserted, and convex hulls of sampled points are not excluded.',
        'proof_checks':['48-term alternating Machin pi bounds','40th-degree sin/cos Lagrange remainder','exact rational interval automatic derivatives','strict positive top escape at reference zero','strict positive bottom pole curvature factor','strict negative meridian curvature over full parameter box']}
    raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode()
    open('POLE_CERT.json','wb').write(raw)
    print('DLV_MOBIUS_SCOPED_NONCONVEXITY_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
```
