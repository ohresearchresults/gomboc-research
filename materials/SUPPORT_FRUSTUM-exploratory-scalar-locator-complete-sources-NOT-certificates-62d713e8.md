# material-62d713e83ee2

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# SUPPORT_FRUSTUM exploratory scalar locators

Status: numerical locators only, NOT an existence proof, NOT a full body or metric/Lambda system, NOT a universal exclusion. The independently executable rational certificate [internal-source-reference] reconstructs the final formal scalar point without these numerical outputs. No floating-point conclusion is promoted here.

Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. No random search was invoked; differential_evolution was imported but not used. All optimization bounds, sample grids and tolerances are below. Scalar floating outputs are platform-sensitive and are not exact recovery objects.

Reconstruct the two complete files below as UTF-8/LF with final LF, in the same directory. Commands:
python explore_pair_tail.py
python explore_frustum.py

explore_pair_tail.py:1793bytes,SHA256093b085093dd031e803d47adbfc09804a6e733eb2941f83871cb3387f07acc57.
explore_frustum.py:1119bytes,SHA256b56599ab251b3d95fa81c0c6735c90e543a4b3112388fc3b48f5c6127741b67f.

The numerical exploration found positive new support-conditioned tail violations at joint-mass h=.16,.2,.25, and no sampled positive violations for several h>=.3. This is not a proved exclusion or feasibility assertion for those ranges. The exact rational formal control subsequently chosen is r=2/5,h=1/4,T=51/25,L=4(1+r+r*r)/(1+2*r+3*r*r),m=h+(T-h)/L,c=L+3*h/m*(1-L); its exact continuous proof is independent of the locator. The high-trace pair theorem remains open.

## Complete file explore_pair_tail.py
```python
from math import comb
import numpy as np
from scipy.optimize import minimize_scalar, differential_evolution
TAU=51/25

def hinge(vals,t):
    v=sorted(vals);p=len(v)
    d=[max(x-t,0.)**p for x in v]
    for k in range(1,p):
        d=[comb(p,k)*max(v[i]-t,0.)**(p-k) if v[i+k]==v[i] else (d[i+1]-d[i])/(v[i+k]-v[i]) for i in range(len(d)-1)]
    return d[0]/p

def pars(h,m,T=TAU):
    A=(T-h)/(m-h)
    C=A+(3*h/m)*(1-A)
    return A,C

def gap(h,m,t,T=TAU):
    A,C=pars(h,m,T)
    return m*hinge([1,A,A,C],t)/3+(3-m)*hinge([1]+[(3-T)/(3-m)]*3,t)/3-max(1-t/4,0.)**4

def maxgap(h,m,T=TAU):
    A,C=pars(h,m,T)
    breaks=sorted(set([0.,1.,4.,A,C,(3-T)/(3-m)]))
    points=[(gap(h,m,t,T),t) for t in breaks if 0<=t<=4]
    for a,b in zip(breaks,breaks[1:]):
        a=max(0.,a);b=min(4.,b)
        if a>=b:continue
        res=minimize_scalar(lambda t:-gap(h,m,t,T),bounds=(a,b),method='bounded',options={'xatol':1e-12})
        points.append((-res.fun,res.x))
    return max(points)

def cuts(h,m,T=TAU):
    a,c=pars(h,m,T);q=2*a
    vals=[]
    for k in np.linspace(.001,min(1,m/(3*h)-1e-7),200):
        t=1-3*h*k/m
        Ak=t*t+t*(1-k)+(1-k)**2
        Bk=k*(t+2*(1-k))
        L=t*k/3*(m*q*Ak+(3*T-m*q)*Bk+m*(1-t)*(2*t+1-k))
        f=3*k*k-2*k**3;I=2*k**3-1.5*k**4;Z=f-3*h/m*I
        J=q*(1.5*k*k-2*k**3+.75*k**4)+2*c*(k**3-.75*k**4)
        if 1-h*J<=0 or 1-h*f<=0:return 1e9
        vals.append(L*(1+h*Z/(t*(1-h*f)))/(1-h*J))
    return max(vals)

if __name__=='__main__':
    for h in [.16,.2,.25,.3,.4,.5,.6,.7,.8,.9]:
        m=.75*(1+h)
        A,C=pars(h,m)
        if C<0:continue
        print('jointmax',h,m,A,C,maxgap(h,m),cuts(h,m))
    for h,m in [(.3,.95),(.3,.97),(.4,1.02),(.5,1.1),(.6,1.15),(.8,1.3)]:
        print('interior',h,m,pars(h,m),maxgap(h,m),cuts(h,m))
```

## Complete file explore_frustum.py
```python
from explore_pair_tail import pars,hinge,TAU
from scipy.optimize import minimize_scalar
import math

def radius(H):
    aa=3*H-4;bb=2*H-4;cc=H-4
    return (-bb+math.sqrt(bb*bb-4*aa*cc))/(2*aa)

def cap(H,t):
    if t<=0:return 1-t
    if t>=H:return 0.
    r=radius(H);q=r-1;z=t/H;u=1-z
    # polynomial integration in y=(s-t)/H to avoid cancellation near H
    return 3*H/(1+r+r*r)*((1+q*z)**2*u*u/2+2*q*(1+q*z)*u**3/3+q*q*u**4/4)

def exactgap(h,m,t,T=TAU):
    A,C=pars(h,m,T)
    return m*hinge([1,A,A,C],t)/3+(3-m)*hinge([1]+[(3-T)/(3-m)]*3,t)/3-cap(A,t)

def worst(h,m,T=TAU):
    A,C=pars(h,m,T);vals=sorted(set([0.,1.,A,C,(3-T)/(3-m)]));out=[]
    for a,b in zip(vals,vals[1:]):
        a=max(a,0.);b=min(b,A)
        if b<=a:continue
        z=minimize_scalar(lambda t:-exactgap(h,m,t,T),bounds=(a,b),method='bounded')
        out.append((-z.fun,z.x))
    return max(out)
if __name__=='__main__':
    for h in [.16,.2,.25,.3,.4,.5,.6,.7,.8]:
        m=.75*(1+h)
        print(h,m,pars(h,m),worst(h,m))
    for h,m in [(.3,.95),(.4,1.02),(.5,1.1),(.6,1.15)]:
        print('interior',h,m,pars(h,m),worst(h,m))
```

## Complete rational-parameter selection invocation
```python
from fractions import Fraction as F
from explore_pair_tail import maxgap,cuts
from explore_frustum import worst
for r in [F(1,3),F(2,5),F(3,7),F(4,9),F(9,20)]:
    L=4*(1+r+r*r)/(1+2*r+3*r*r)
    h=F(1,4);T=F(51,25);m=h+(T-h)/L;c=L+3*h/m*(1-L)
    print(r,L,m,c,'old',maxgap(float(h),float(m)),
          'new',worst(float(h),float(m)),'cuts',cuts(float(h),float(m)))
```

The selected r=2/5 had an observed new maximal gap approximately0.00721 near threshold1.44, whereas the old continuous-tail locator found no positive gap above numerical roundoff and the sampled old cut maximum was approximately0.958. These observations alone were insufficient. Exact source [internal-source-reference] subsequently proves all the claimed old continuous inequalities by Bernstein certificates and rejects the point at the rational threshold7/5 with a positive rational gap. Numerical continuation at h>=.3 remains UNKNOWN, not a feasible body and not a proved barrier to the full new system.
