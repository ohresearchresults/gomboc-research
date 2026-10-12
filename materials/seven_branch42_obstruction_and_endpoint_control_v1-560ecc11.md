# material-560ecc1119af

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# SEVEN_CORNER_BRANCH42_OBSTRUCTION_V1

## Result and precise scope
Let Q be a convex planar polygon,0 in its interior,with a true boundary weak escape tree rooted at A. Normalize A=(1,0) by an orientation-preserving Euclidean similarity. Suppose one branch away from the root has at most FOUR edges and the other at most TWO. Orient the longer branch counterclockwise. Then the ENTIRE polygon lies in the strict halfplane

    -x-y/2 < 3/10.

Consequently -(3/10)A is not in Q. In particular -Q/3 cannot be contained in Q. This closes the full4+2 rooted-boundary form of a seven-corner polygon,including every weak selected-arrow wall,without any equal-turn ansatz,radial-tightness premise,uniform-area centroid assumption,or numerical search inference.

The3+3 form is already excluded by the root-axis bound x>=-1/4. For a seven-corner polygon with only one strict radial maximum,the remaining POSSIBLE forms are5+1 and6+0,up to reflection. The6+0 endpoint-root form must not silently be omitted: it was not covered by the earlier numerical search over m=3,4,5 in [internal-source-reference]. This result does not claim that6+0 is feasible at coefficient1/3. An exact coefficient3/10 endpoint-root countercontrol below shows that the new4+2 halfplane bound itself does not extend to all root positions.

Every true shadow of a uniformly filled own-centred3D polytope satisfies -Q/3 subsetQ. Thus a seven-corner rank2shadow supporting a true weak rooted system cannot have the4+2 or3+3 boundary form. This is a universal reduction,not a whole seven-corner exclusion,an actual3D construction,or a change to34<=Cmin<=622.

## Sources and distinction from inherited work
The completely read immutable parent minimum-0209,SHAadebd2f62354466c4f5cdadbb45aec998631c8d8854876b6c92411d83403ff1c,proves the<=6corner theorem,actual -P/3 containment via root-star volume moments,and genuine closed exposed-fibre transport. Its radial-chain estimate is reproved below for the exact use here. [internal-source-reference] was also read throughEOF; it preserves only a finite numerical exploration of internal root forms. The exact equal-turn5+1 family [internal-source-reference] remains an ansatz theorem,not a global exclusion. No parent object or labels are changed here.

## 1. Angular-chain support mechanism
For a counterclockwise boundary chain v0=A,v1,...,vj with weak arrows vi->v(i-1),write polar angles0=theta0<theta1<...<thetaj<2pi. Each increment delta_i lies in(0,pi/2),because

    |vi|^2 <= vi.vi-1 = |vi||vi-1|cos(delta_i).

Therefore |vj|<=product cos(delta_i). For j<=m,append m-j zero increments only in this scalar estimate. Concavity of log cos yields

    |vj| <= cos^m(thetaj/m).

No fictitious corners or zero edges are inserted into the actual polygon. This estimate includes equality in every chosen weak arrow. The analogous estimate holds after reflecting a clockwise branch into the upper orientation.

More generally,for a direction of argument phi and a monotone m-step chain,the positive directional support is bounded by maximizing cos(theta-phi)cos^m(theta/m). On an applicable positive-cosine interval the stationary maximum is cos^(m+1)(phi/(m+1)). This explains the observed4+2 numerical value near0.268861,but no sharp-optimum or attainment claim is needed or promoted here. The following rational certificate proves the strict3/10 bound directly on the WHOLE angular ranges.

## 2. Four-edge branch: exact global angular inequality
Put ell(x,y)=-x-y/2. On the long branch,theta belongs to(0,2pi). If -cos(theta)-sin(theta)/2<=0,then ell(v)<=0<3/10. Otherwise the chain estimate gives

    ell(v) <= [-cos(theta)-sin(theta)/2]cos^4(theta/4).

Set t=tan(theta/4)>0. Elementary quadruple-angle identities give

    3/10 - [-cos(theta)-sin(theta)/2]cos^4(theta/4)
      = P4(t)/[10(1+t^2)^4],
    P4(t)=3t^8+12t^6+28t^4-20t^3-48t^2+20t+13.

P4 is strictly positive for every t>=0. On[0,1/2] its degree8 Bernstein coefficients are

    13,57/4,211/14,1727/112,611/40,205/14,6075/448,775/64,2675/256.

On[1/2,1] they are

    2675/256,1125/128,775/112,5,1829/560,33/16,53/28,7/2,8.

Every coefficient is positive. For t=1+u,u>=0,

    P4(1+u)=8+72u+324u^2+500u^3+418u^4+240u^5+96u^6+24u^7+3u^8>0.

These two closed intervals and the full unbounded tail exhaust all angles. Thus every long-branch corner satisfies ell<3/10.

## 3. Two-edge clockwise branch
Reflect a short-branch point to polar angle theta in(0,pi). Its radius is at most cos^2(theta/2). In the original coordinates ell is bounded,whenever its angular factor is positive,by

    [-cos(theta)+sin(theta)/2]cos^2(theta/2).

With t=tan(theta/2)>0,

    3/10 - [-cos(theta)+sin(theta)/2]cos^2(theta/2)
      = P2(t)/[10(1+t^2)^2],
    P2(t)=3t^4-4t^2-10t+13.

On[0,1] its degree4 Bernstein coefficients are13,21/2,22/3,7/2,2,all positive. For t=1+u,u>=0,

    P2(1+u)=3u^4+12u^3+14(u-3/14)^2+19/14>0.

Hence ell<3/10 on every short-branch corner too. At the root ell(A)=-1. A finite convex hull of these strictly separated vertices is strictly separated. Since ell(-(3/10)A)=3/10,this proves the theorem. In particular ell(-A/3)=1/3 is impossible.

For any polygon with a sole strict radial maximum,every other corner has exactly one weak outgoing boundary arrow: both cannot be weak because -v is a positive combination of its two inward edge directions. Norms strictly grow along nonzero weak edges. Deleting the one unused boundary edge therefore gives the two rooted branches,including the possibility that one has length0. For seven corners their unordered lengths are(3,3),(4,2),(5,1),(6,0). Thus endpoint6 is a genuine remaining form,not a relabelling of5+1.

## 4. Exact strict endpoint6 control at coefficient3/10
This is a separate rational PLANAR polygon,not a six-pole atlas object or actual centred3D body. Divide the following seven cyclic coordinates by10^9:

    (1000000000,0),
    (440691788,496425691),
    (-52229194,437541480),
    (-222140726,319275645),
    (-305493139,156661940),
    (-303007708,-4612753),
    (-131243132,-152453615).

Parents are(0,0,1,2,3,4,5). All six selected arrows are STRICTLY positive. All14 boundary primitives are nonzero and the only strict radial maximum is0. Every nonincident support determinant is positive,the origin is strictly interior,and -(3/10)Q lies strictly inside Q.

Exact minimum margins:

    convexity:216356249387751/15625000000000000;
    origin:5698653538325253/125000000000000000;
    containment3/10:578809579116303/1250000000000000000;
    selected arrow:2023532137951/500000000000000000.

At coefficient1/3 the minimum support determinant is

    -4556747864895167/300000000000000000 <0.

Thus it fails the NECESSARY actual-volume-centroid shadow condition and is not a3D attaining construction. It establishes only that the strict3/10 obstruction is specific to the balanced branch structure. The complete exact primitive list is regenerated by the source below.

## 5. Executed evidence and complete recovery
The analytical theorem is proved above; the finite polynomial identities and literal rational control were checked with exact Fraction arithmetic. Observed environment CPython3.13.5,standard library,assertions enabled. Build and check both exited0 and stdout matched. This is one implementation,not a proof-assistant formalization or independently authored audit.

Save the complete source below as seven_branch42.py,UTF-8/LF. Run

    python -B -S seven_branch42.py build > build.out
    python -B -S seven_branch42.py check > check.out
    cmp build.out check.out

Pins:

    seven_branch42.py:4410bytes,SHA4840c74f78ce961cecccf0e85d1011823889f681eb0381d0bd384c8dda97a1c1
    seven_branch42.json:2033bytes,SHA3c5e89f81016f5dd78858e060dee6edf34e6ac5dc2e380d8c3d8cd6789000b67
    identical stdout:366bytes,SHA3a72f27fc095b570ef94bd3e806ebf0cca7efd2d4e09c083df16479bde18beca

Expected markers:


[Encoded source block omitted; the code in this passage is incomplete.]

```python
#!/usr/bin/env python3
"""Exact finite identities for SEVEN_CORNER_BRANCH42_OBSTRUCTION_V1.
CPython >=3.11, standard library only; assertions must be enabled.
Run: python -B -S seven_branch42.py build; then replace build by check.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys

def affine(p,a,b):
    q=[F(0)]*len(p)
    for j,c in enumerate(p):
        for i in range(j+1):
            q[i]+=c*comb(j,i)*a**(j-i)*b**i
    return q

def bernstein(p,a,b):
    q=affine(p,a,b-a); n=len(q)-1
    out=[sum(q[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]
    # Independent inverse reconstruction in the scaled power variable.
    back=[F(0)]*(n+1)
    for k,c in enumerate(out):
        for j in range(n-k+1):
            back[k+j]+=c*comb(n,k)*comb(n-k,j)*(-1)**j
    assert back==q
    return out

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def serial(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {str(k):serial(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [serial(x) for x in v]
    return v

P4=list(map(F,(13,20,-48,-20,28,0,12,0,3)))
P2=list(map(F,(13,-10,-4,0,3)))
blocks=[]
for name,p,a,b in [('long_left',P4,F(0),F(1,2)),('long_right',P4,F(1,2),F(1)),('short',P2,F(0),F(1))]:
    coeff=bernstein(p,a,b);assert min(coeff)>0
    blocks.append(dict(name=name,interval=(a,b),coefficients=coeff))
shift4=affine(P4,F(1),F(1));assert shift4==list(map(F,(8,72,324,500,418,240,96,24,3)))
assert min(shift4)>0
shift2=affine(P2,F(1),F(1));assert shift2==list(map(F,(2,-6,14,12,3)))
# For u>=0: 3u^4+12u^3+14(u-3/14)^2+19/14 is positive.
assert F(14)*F(3,14)**2+F(19,14)==2 and -2*14*F(3,14)==-6
# Verify the two rational trigonometric numerator identities exactly.
assert P4==[F(3*comb(4,j//2) if j%2==0 else 0)+F({0:10,1:20,2:-60,3:-20,4:10}.get(j,0)) for j in range(9)]
assert P2==[F(3*comb(2,j//2) if j%2==0 else 0)+F({0:10,1:-10,2:-10}.get(j,0)) for j in range(5)]

DEN=10**9
NUM=((1000000000,0),(440691788,496425691),(-52229194,437541480),(-222140726,319275645),(-305493139,156661940),(-303007708,-4612753),(-131243132,-152453615))
Q=tuple(tuple(F(a,DEN) for a in row) for row in NUM)
E=tuple(sub(Q[(i+1)%7],Q[i]) for i in range(7))
conv=[cross(E[i],sub(Q[j],Q[i])) for i in range(7) for j in range(7) if j not in (i,(i+1)%7)]
inside=[cross(Q[i],Q[(i+1)%7]) for i in range(7)]
contain=[cross(E[i],sub(tuple(-F(3,10)*a for a in Q[j]),Q[i])) for i in range(7) for j in range(7)]
selected=[dot(Q[i],sub(Q[i-1],Q[i])) for i in range(1,7)]
primitives=[(i,j,dot(Q[i],sub(Q[j],Q[i]))) for i in range(7) for j in ((i-1)%7,(i+1)%7)]
assert min(conv)>0 and min(inside)>0 and min(contain)>0 and min(selected)>0
assert all(v!=0 for _,_,v in primitives)
roots=[i for i in range(7) if all(v<0 for a,j,v in primitives if a==i)]
assert roots==[0]
third=[cross(E[i],sub(tuple(-F(1,3)*a for a in Q[j]),Q[i])) for i in range(7) for j in range(7)]
assert min(third)<0
report=dict(theorem='SEVEN_CORNER_BRANCH42_OBSTRUCTION_V1',lambda_bound=F(3,10),P4=P4,P2=P2,bernstein_blocks=blocks,positive_shift4=shift4,short_shift_sos=dict(shift=shift2,square_weight=14,square_center=F(3,14),constant=F(19,14)),endpoint_control=dict(denominator=DEN,numerators=NUM,parents=(0,0,1,2,3,4,5),lambda_containment=F(3,10),convexity_min=min(conv),origin_min=min(inside),containment_min=min(contain),selected_arrow_min=min(selected),all_14_primitives=primitives,strict_radial_maxima=roots,third_containment_min=min(third)),scope='No seven-corner global exclusion or actual homogeneous 3D lift is asserted. Unresolved rooted branch forms5+1 and6+0 remain.')
data=(json.dumps(serial(report),sort_keys=True,separators=(',',':'))+'\n').encode()
path=Path('seven_branch42.json')
assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
if sys.argv[1]=='build': path.write_bytes(data)
else: assert path.read_bytes()==data
print('BRANCH42_SEPARATING_HALFPLANE_LT_3_OVER_10_EXACT_IDENTITIES_PASS')
print('THREE_POSITIVE_BERNSTEIN_BLOCKS_AND_TWO_UNBOUNDED_TAIL_PROOFS_PASS')
print('ENDPOINT6_STRICT_ROOTED_SEVEN_CORNER_3_OVER_10_CONTROL_PASS')
print('ENDPOINT_CONTROL_FAILS_1_OVER_3_NO_ACTUAL_3D_CLAIM_PASS')
print('NO_GLOBAL_SEVEN_CORNER_OR_C34_EXCLUSION_CLAIMED')
print(len(data),hashlib.sha256(data).hexdigest())
```

## 6. Complete exploratory locator for the endpoint form,not proof
The control was located by the following standalone search,NumPy2.3.5/SciPy1.17.0/CPython3.13.5. Five starts all reported local lambda about0.30322951385713. This is NOT a global bound. After selecting the largest reported value,scale qi by(9999/10000)^i and round coordinates to denominator10^9; the exact literal control above,not a potentially platform-dependent optimizer output,is the proof input. All search constraints,seed and settings are retained below. No external helper is needed.

```python
import numpy as np
from scipy.optimize import minimize
from math import pi,cos,sin

def cross(a,b): return a[...,0]*b[...,1]-a[...,1]*b[...,0]
def constraints(v):
    q=np.vstack(([1.,0.],v[:-1].reshape(-1,2)));e=np.roll(q,-1,axis=0)-q;lam=v[-1]
    inc=cross(e[:,None,:],-lam*q[None,:,:]-q[:,None,:]).ravel()
    cv=cross(e[:,None,:],q[None,:,:]-q[:,None,:]);mask=np.ones((7,7),bool)
    for i in range(7):mask[i,i]=mask[i,(i+1)%7]=False
    ar=[q[i]@(q[i-1]-q[i]) for i in range(1,7)]
    return np.r_[inc,cv[mask]-1e-8,np.array(ar),cross(q,np.roll(q,-1,axis=0))-1e-8]
rng=np.random.default_rng(260923);runs=[]
for j in range(5):
    aa=rng.uniform(1.03,1.5)*pi/6
    q=np.array([[cos(aa)**i*cos(i*aa),cos(aa)**i*sin(i*aa)] for i in range(7)])
    x=np.r_[q[1:].ravel(),.15]
    fit=minimize(lambda x:-x[-1],x,method='SLSQP',constraints=[{'type':'ineq','fun':constraints}],bounds=[(-1,1)]*12+[(.01,.7)],options={'maxiter':700,'ftol':1e-12})
    runs.append(fit);print(j,fit.success,fit.x[-1],constraints(fit.x).min())
best=max(runs,key=lambda f:f.x[-1]);q=np.vstack(([1.,0.],best.x[:-1].reshape(-1,2)))
nums=np.rint(np.array([row*(9999/10000)**i for i,row in enumerate(q)])*10**9).astype(np.int64)
print(nums.tolist())
```

Next scientific task: a valid global5+1 and6+0 argument under ALL-direction -Q/3 containment. The exact halfplane method settles the balanced forms but is insufficient for these remaining ones. Actual concave fibre-density/centroid lift constraints are a further,independent layer. No numerical failure or endpoint-control feasibility below1/3 settles them.
