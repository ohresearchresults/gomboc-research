# material-6bb7ae3b76de

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ROOTED_BOUNDARY_4_PLUS_3_STRICT_5_OVER_16_OBSTRUCTION_V1

## Statement
Let Q be a convex planar polygon with0 in its interior and a weak rooted boundary tree whose two branches have lengths at most4and3. Normalize the root A=(1,0) and orient the length-at-most4 branch counterclockwise. Then

    -x-y/5 <5/16 for EVERY point(x,y) in Q.

Consequently -(5/16)A is outside Q. In particular -Q/3 cannot be contained in Q. This includes every weak selected-arrow wall and arbitrary angular increments; no equal-turn or strict-arrow assumption is made.

For eight genuine corners,this closes the balanced rooted-boundary form4+3. The remaining forms are5+2,6+1,7+0; they are NOT excluded here. For seven corners,the already established3+3,4+2 and5+1 exclusions leave only6+0. This theorem neither settles that endpoint case nor upgrades a planar control to an actual homogeneous3D object. No global34<=Cmin<=622 bound changes.

## Source relation
The radial-chain estimate is already developed in the fully read source minimum-0209 and coordinator [internal-source-reference]. The new constants and complete whole-angle certificate below are independent exact additions. [internal-source-reference] is a separate two-target envelope proof closing the seven-corner5+1 form; it is not silently transferred to the present eight-corner geometry.

## Complete analytical proof
For a counterclockwise weak chain away from A,with j<=m arrows,cumulative angle theta and successive increments delta_i,the true-corner and origin-interior conditions give0<delta_i<pi/2. The weak inequalities imply

    radius<=product cos(delta_i)<=cos^m(theta/m).

The last inequality pads the scalar Jensen inequality by m-j zeros,not the actual polygon by fake vertices. The corresponding clockwise branch satisfies the reflected formula. Let ell(x,y)=-x-y/5.

On the m=4 counterclockwise branch,if -cos(theta)-sin(theta)/5<=0,then ell<=0<5/16. Otherwise

    ell<=(-cos(theta)-sin(theta)/5)cos^4(theta/4).

Writing t=tan(theta/4)>=0 yields

    5/16-(-cos(theta)-sin(theta)/5)cos^4(theta/4)
       =P4(t)/(80(1+t^2)^4),
    P4=25t^8+100t^6+230t^4-64t^3-380t^2+64t+105.

The full possible range0<=theta<2pi corresponds to0<=t<infinity. Thus no angular tail is omitted.

On the m=3 clockwise branch,reflecting its angle to theta>=0 gives ell/radius=-cos(theta)+sin(theta)/5. If this factor is nonpositive we again have ell<=0. Otherwise

    ell<=(-cos(theta)+sin(theta)/5)cos^3(theta/3).

Set t=tan(theta/3)>=0. Since0<=theta<3pi/2,the entire possible range is again0<=t<infinity. Triple-angle identities give

    5/16-(-cos(theta)+sin(theta)/5)cos^3(theta/3)
       =P3(t)/(80(1+t^2)^3),
    P3=25t^6+75t^4+16t^3-165t^2-48t+105.

Both polynomials are strictly positive on[0,infinity). On each of[0,1/2],[1/2,3/4],[3/4,1],the complete source below produces and exactly inverts positive Bernstein coefficients. The minimum coefficients in these three blocks are,respectively,

    P4:12809/256,348921/65536,58151/16384;
    P3:2997/64,45537/4096,19/20.

For t=1+u,u>=0,the ascending coefficient lists are

    P4(1+u):80,832,3008,4256,3480,2000,800,200,25;
    P3(1+u):8,120,708,816,450,150,25.

All coefficients are positive,including the constants. The three finite closed blocks and full unbounded tail prove strict positivity everywhere. Therefore every branch vertex satisfies ell<5/16. At the root ell(A)=-1. Taking the convex hull of this finite set preserves strict separation. Since ell(-(5/16)A)=5/16,the claimed exclusion follows. The stronger target -A/3 is also outside because1/3>5/16.

This is a purely planar support obstruction. Actual uniformly filled own-centred3D shadows meet -Q/3subsetQ by the root-star volume theorem,but their marginal density is not replaced by uniform area. Integration or projection diagonals are not asserted to be true mechanical edges.

## Complete exact source and observed execution
Save the source below as branch43.py,UTF-8/LF. CPython3.13.5 standard library was used,assertions enabled. Build and check both exited0;stdout was identical. The certificate is one exact implementation,not a proof-assistant formalization or independent replay.

    python -B -S branch43.py build > build.out
    python -B -S branch43.py check > check.out
    cmp build.out check.out

Pins:

    branch43.py:2279bytes
    SHA256ab930261199361e21fbedf1e289f409ce1cbe805985663bdd2a474a3e0c6844f
    branch43.json:1379bytes
    SHA256914a88174031b0aae90ec575288fdf0028e0c3573da2e1a90886ea24830f8210
    identical stdout:206bytes
    SHA25619e398d1c8eb6b1239825719877b1e7a0201a4a3335d7dc901b6fde364f1f65e

Expected terminal markers:

    WHOLE_4_PLUS_3_WEAK_ROOTED_BOUNDARY_STRICT_5_OVER_16_HALFPLANE_PASS
    SIX_POSITIVE_BERNSTEIN_BLOCKS_AND_TWO_POSITIVE_UNBOUNDED_TAILS_PASS

```python
#!/usr/bin/env python3
"""Exact whole-angle certificate for the weak rooted boundary form4+3.
CPython>=3.11, standard library, assertions enabled. Build then check.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys

def affine(p,a,b):
    out=[F(0)]*len(p)
    for j,c in enumerate(p):
        for i in range(j+1):out[i]+=c*comb(j,i)*a**(j-i)*b**i
    return out

def bernstein(p,a,b):
    q=affine(p,a,b-a);n=len(p)-1
    co=[sum(q[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]
    back=[F(0)]*(n+1)
    for k,c in enumerate(co):
        for j in range(n-k+1):back[k+j]+=c*comb(n,k)*comb(n-k,j)*(-1)**j
    assert back==q and min(co)>0
    return co

def pack(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [pack(v) for v in x]
    if isinstance(x,dict):return {str(k):pack(v) for k,v in x.items()}
    return x

P4=list(map(F,(105,64,-380,-64,230,0,100,0,25)))
P3=list(map(F,(105,-48,-165,16,75,0,25)))
assert P4==[F(25*comb(4,j//2) if j%2==0 else 0)+F({0:80,1:64,2:-480,3:-64,4:80}.get(j,0)) for j in range(9)]
assert P3==[F(25*comb(3,j//2) if j%2==0 else 0)+F({0:80,1:-48,2:-240,3:16}.get(j,0)) for j in range(7)]
blocks=[];tails={}
for name,p in [('long4',P4),('short3',P3)]:
    for a,b in [(F(0),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(1))]:
        blocks.append(dict(name=name,interval=(a,b),coefficients=bernstein(p,a,b)))
    tails[name]=affine(p,F(1),F(1));assert min(tails[name])>0
report=dict(theorem='ROOTED_BOUNDARY_4_PLUS_3_STRICT_5_OVER_16_OBSTRUCTION_V1',linear_functional=(-1,F(-1,5)),strict_upper=F(5,16),P4=P4,P3=P3,blocks=blocks,positive_tails=tails,scope='Any weak rooted convex boundary branches of lengths at most4and3. Not a global eight-corner exclusion or an actual3D construction.')
data=(json.dumps(pack(report),sort_keys=True,separators=(',',':'))+'\n').encode()
assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
out=Path('branch43.json')
if sys.argv[1]=='build':out.write_bytes(data)
else:assert out.read_bytes()==data
print('WHOLE_4_PLUS_3_WEAK_ROOTED_BOUNDARY_STRICT_5_OVER_16_HALFPLANE_PASS')
print('SIX_POSITIVE_BERNSTEIN_BLOCKS_AND_TWO_POSITIVE_UNBOUNDED_TAILS_PASS')
print(len(data),hashlib.sha256(data).hexdigest())
```

## Exploratory locator,not a sharpness claim
A directional envelope calculation suggested the rational normal(-1,-1/5). The following complete optional locator uses NumPy2.3.5/SciPy1.17.0. Its observed values are NOT accepted sharp bounds or attainment claims; the exact polynomial proof above is independent of this optimization.

```python
from math import pi,cos
from scipy.optimize import minimize_scalar
for m,n in [(4,2),(4,3),(5,2),(5,3),(4,4),(5,4)]:
    def bound(phi):
        return max(cos(phi/(m+1))**(m+1),cos((2*pi-phi)/(n+1))**(n+1))/(-cos(phi))
    fit=minimize_scalar(bound,bounds=(pi-.8,pi+.8),method='bounded',options={'xatol':1e-14})
    print(m,n,fit.fun,fit.x)
```

The remaining eight-corner5+2,6+1,7+0 forms must not be declared impossible from this balanced-branch theorem. The existing strict asymmetry-compatible octagon has a6+1 rooted form and is not contradicted. Its separate actual eight-corner-only3D lift obstruction remains a stronger centroid issue,not a consequence of the current support polynomial.
