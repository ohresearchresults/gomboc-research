# minimum-0298

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# OPPOSITE_WING_MARKED_CUT_EXCLUSION_V1

## 1. Determination

**The forced-density opposite-wing maximum mechanism is excluded completely.** In the full coupled six-parameter domain of the literal parent, the actual inward motion of the whole marked facet has strictly positive first variation whenever the distinguished centered test has R≥1. In particular, no self-consistent supercritical maximum with two nonempty parabolic arcs on opposite sides can survive.

The proof is analytical over the entire parameter domain, including tangent stem joins and zero-length arc limits. It is not inferred from a finite search or a certified neighborhood. More specifically, the actual parabola self-consistency, affine-density stationarity and the two actual weighted stem reactions already force the cut derivative to vanish, while the geometric calculation makes it positive for R≥1. Test optimization, the density Hessian and the full convex-height gate cannot repair this contradiction; they are additional conditions that are not needed here.

**This is a stationary-mechanism exclusion, not an unconditional value theorem R<1 for every member of the family.** No universal three-halves proof, strict actual counterexample, separate weak-leverage closure or mechanical E17/minimum improvement is claimed. The remaining nonlinear boundary of a hypothetical global strong maximizer must lie on a single side of the marked-test interval. This does not say that the support itself cannot overhang the other side.

## 2. Input authority and evidence

I read the current 1833-line journal consecutively through EOF, including the literal current parent, and all three newly supplied exact sources, including the triangular source's complete program. The verified inputs are:

```
research-journal.md: 360253 bytes
  da85ec57f866bc77d21ec66bf9278ac7626acf988fa4fbfd4a9f5c54dfc86adf
TRIANGULAR_AFFINE_HEIGHT_SHARP_45_32_RECOVERY_V1.md: 17253 bytes
  cf56bbf56ecd632812debab69e297814f0d23188ab7135d455dae54ff18ec939
FULL_CONVEX_HEIGHT_CONE_AT_ZERO_DENSITY_V1.md: 7922 bytes
  e4696c06ab19d948168a41a0321e6ca150873b5f33d6f98116f7168a2a7f5bba
CONIC_EXTREMIZER_REDUCTION_V1.md: 12235 bytes
  703e40d96d509e9d8ce54ea5ea74481e283d5c31250b4baaaeb489bbb94814b5
```

The literal preceding result is `minimum-0295`, SHA-256 `c5da795d12e9ffc99d28fd53e74ba1cc2494cdcc24117b6b85633536d62c0819`; its reconstructed compact JSON envelope is 40675 bytes and matches that identity. The unchanged exact-reduction parent is `minimum-0290`, SHA-256 `a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8`. Its earlier full reading and exact source remain available in this chat. There is no new missing exact dependency for this result.

I used the preceding parent's existing exact `two_wing_control` evaluator: an executed, hash-checked comparison agrees with the new independent integration on the inherited fixture's volume, actual centroid, covariance, whole marked-facet matrix, alpha and R. The default new recovery needs no parent file.

Imported results retain their scopes. Strong global attainment and the common-parabola boundary theorem are the supplied conic source's analytical results, not a polygon-vertex localization. The parent's two-arc sharpening supersedes that source's older four-arc count. The new triangle theorem is the full matrix bound45/32, but no triangle-only localization is assumed. The convex-height comparison is a global necessary condition, not a condition for every local affine-density critical point.

## 3. The complete actual opposite-wing domain

Use coordinates (t,y), with the whole marked edge

```
e = {(0,y): -1≤y≤1}.
```

The distinguished affine test is Y=y−mu, where mu is the actual ell-weighted mean, not the facet mean. The coordinates t and y are independent. Let

```
a≤u<−1<1<v≤b,                  C>B²,
f(y)=y²+2By+C,
U(y)=(a+b+2B)y+C−ab,
kL=f(u)/(−1−u)>0,              kR=f(v)/(v−1)>0,
SL(y)=−kL(y+1),                SR(y)=kR(y−1).
```

Define the lower graph by the five consecutive pieces

```
f on [a,u];  SL on [u,−1];  0 on [−1,1];
SR on [1,v];  f on [v,b].
```

Require

```
f'(u)≤−kL,     kR≤f'(v),     U≥L.
```

These are the actual convexity and containment conditions. The actual support, affine height and uniformly filled lift are

```
K={(t,y): a≤y≤b, L(y)≤t≤U(y)},
ell(t,y)=U(y)−t,
P={(t,y,z):(t,y)∈K, 2|z|≤ell(t,y)}.
```

The two positive-length arcs correspond to a<u and v<b. The inclusion of equality cases above supplies their zero-length limits, not every possible one-arc geometry. In particular, a one-arc body with its other corner strictly off the parabola is not being silently included.

This is exactly the parent's forced-density chart: the upper boundary is the density-zero line and the density is not an independent profile. At an opposite-wing supercritical extremizer, the supplied conic theorem and parent's classification give this representation after affine normalization, with min f>0.

All following quantities come from this one body:

```
V=∫K ell,             J=∫K t ell,             m=J/V,
mu=(∫K y ell)/V,      Y=y−mu,                 I=∫K ell Y²,
Bj=∫[-1,1] U(y)(y−mu)^j dy,
R=J B2/(V I),         alpha=J B0/V²,
lambda=B1²/(B0 B2) ∈[0,1].
```

The lift has centroid (m,mu,0). Here d_sigma=dy on the marked edge. All denominators used below are positive.

## 4. Coupled geometry forces both endpoint gains above one

Put

```
d=−1−u>0,    eR=v−1>0,    A=u−a≥0,    D=b−v≥0,
fminus=C+1−2B>0,           fplus=C+1+2B>0,
delta=C−B²>0.
```

The stem slopes and join inequalities give

```
kL=d+2(1−B)+fminus/d,       d²≥fminus,
kR=eR+2(1+B)+fplus/eR,      eR²≥fplus.
```

The following identity is the essential coupled sign certificate:

```
d² eR²−(C−1)²
 = (d²−fminus)eR² + fminus(eR²−fplus) +4(C−B²) >0.
```

Thus d eR>|C−1|, and Z=d eR+C−1>0. Let Hminus=U(−1), Hplus=U(1). Direct expansion of the actual chord U gives

```
Hminus−kL = Z+(d²−fminus)/d +D d +(2+eR+D)A >0,
Hplus−kR  = Z+(eR²−fplus)/eR +A eR +(2+d+A)D >0.
```

Consequently

```
rL=Hminus/kL>1,       rR=Hplus/kR>1.                 (4.1)
```

No moment is used in this step. It is a geometric implication of the common parabola, both convex stem joins and the same upper chord. Treating the two endpoint heights or stem slopes as independent would lose it.

## 5. A genuine whole-marked-facet cut and its centered derivative

For s≥0 small, take the actual convex body and its full new marked facet:

```
K_s=K∩{t≥s},           P_s=P∩{t≥s},
t_s=t−s,              e_s=K_s∩{t=s}.
```

The two ends of the whole new edge remain on the stems and are exactly

```
yminus(s)=−1−s/kL,     yplus(s)=1+s/kR.
```

Let V_s, J_s=∫K_s(t−s)ell, mu_s, I_s and Bj,s be the ACTUAL cut-body quantities, with Y_s=y−mu_s. Both required mean equalities are retained exactly:

```
E_s Y_s=0,       E_s[(t−s)/(J_s/V_s)]=1.
```

The mean-one normalization changes neither R nor the subsequent conclusions.

For the derivative calculation only, hold the old mu fixed in the raw moving-slice moment and write

```
D2 = d/ds|0 ∫[yminus(s),yplus(s)] [U(y)−s](y−mu)² dy.
```

Leibniz differentiation and (4.1) give

```
D2 = rL(1+mu)²+rR(1−mu)²−2/3−2mu²
   = 4/3+(rL−1)(1+mu)²+(rR−1)(1−mu)² >4/3.       (5.1)
```

Holding mu fixed here is not a surrogate facet recentering. Its actual variation is included explicitly in the next identities:

```
V'_0=−B0,              J'_0=−V,              mu'_0=−B1/V,
I'_0=−B2,             (B2,s)'_0=D2+2B1²/V.
```

For example, the derivative of the actual central volume moment contains no first-order mean correction because ∫K ell Y=0. The moving facet does have the nonzero correction −2mu'_0 B1. Hence

```
d/ds|0 log R_s
 = −V/J+D2/B2+2B1²/(V B2)+B0/V+B2/I,
```

or, equivalently,

```
m d/ds|0 log R_s
 = R−1+alpha(1+2lambda)+(m/B2)D2.                 (5.2)
```

Every term after R−1 is positive. Therefore **R≥1 implies strict ascent by an actual whole-facet cut**. There is no stationary supercritical exception at a density-zero upper edge.

More generally, (5.2) is valid for any actual independent-coordinate model with differentiable inward slice moments, with its own D2. At a stationary supercritical point it forces

```
D2=−(B2/m)[R−1+alpha(1+2lambda)]<−B2/(2m)
```

when R>3/2. Thus a surviving one-sided mechanism must have a genuinely decreasing raw centered slice second moment. The opposite-wing geometry instead forces that derivative strictly positive.

## 6. The improving cut remains in the six-parameter family

The result does not rely on leaving the assigned actual-support class. Set

```
c_s=(s/2)(1/kR−1/kL),
w_s=1+(s/2)(1/kR+1/kL),
x=(y−c_s)/w_s,        T=(t−s)/w_s²,        z_new=z/w_s².
```

This is a nonsingular affine transformation of the uniformly filled cut body. Its whole marked edge is T=0, −1≤x≤1, and the transformed test differs from its actual centered x-coordinate by a positive scalar only. The six new parameters are

```
a_s=(a−c_s)/w_s,      u_s=(u−c_s)/w_s,
v_s=(v−c_s)/w_s,      b_s=(b−c_s)/w_s,
B_s=(B+c_s)/w_s,
C_s=(c_s²+2Bc_s+C−s)/w_s².
```

In particular,

```
C_s−B_s²=(delta−s)/w_s².
```

For 0≤s<delta the new parabola has positive minimum. The original joins lie strictly above delta: f'(u)≤−kL<0 and f'(v)≥kR>0 exclude the parabola's vertex at either join, so f(u),f(v)>delta. Thus the cut stays below the joins throughout that interval. The new stems have slopes kL/w_s and kR/w_s, and the transformed density is again its upper chord minus T. Convexity, the upper zero edge and the complete marked facet are retained.

This proves the asserted absence of a local maximum with R≥1 in the full positive-minimum chart, not merely in an ambient enlargement. Conditionally on an initial R≥1, its actual cut path remains increasing for as long as 0≤s<delta. This is not an existence assertion for such an initial value.

## 7. The existing coupled stationarity equations already contradict R≥1

Here is the precise connection to the literal parent's evaluator and necessary system. Define its actual centered first-variation kernel and affine density functional:

```
Phi(t,y)=t/J−1/V−(y−mu)²/I−2(B1/B2)(y−mu)/V,
nu(psi)=∫K Phi psi dt dy +(1/B2)∫[-1,1](y−mu)² psi(0,y)dy.
```

The parent's actual clipping argument proves nu(psi)=0 for every affine psi at a full joint maximum, including when the density vanishes. The global convex-height source gives further convex tests, but these are not needed in the present exclusion.

Write U(y)=p y+q, where p=a+b+2B and q=C−ab, and put

```
dc=(1/kR−1/kL)/2,       dw=(1/kR+1/kL)/2.
```

The normalized cut of Section6 has the affine density velocity

```
psi(y)=p dc−1−2q dw−p dw y
```

and common-parabola velocity

```
df(y)=2(dc−B dw)y+2B dc−1−2C dw.
```

Its stem velocities are −dw SL and −dw SR. Define exactly the parent's two actual weighted stem reactions:

```
W_L=∫[u,−1](y+1)[U(y)−SL(y)] Phi(SL(y),y)dy,
W_R=∫[1,v](y−1)[U(y)−SR(y)] Phi(SR(y),y)dy.
```

Differentiating the actual five-piece integrals gives the identity

```
d/ds|0 log R_s
 = nu(psi)+dw(−kL W_L+kR W_R)
   −∫[a,u] [U(y)−f(y)]Phi(f(y),y)df(y)dy
   −∫[v,b] [U(y)−f(y)]Phi(f(y),y)df(y)dy.          (7.1)
```

This is ordinary differentiation of actual integrals. At moving internal joins the endpoint contributions cancel because the graphs meet. At the moving outside endpoints the section has zero thickness. The upper boundary has ell=0, so its support motion contributes no first-order ell-mass. Nothing is being triangulated into independently movable facets.

Actual parabola self-consistency is

```
f(y)=m+(J/I)(y−mu)²+2m(B1/B2)(y−mu).
```

It makes both arc integrands in (7.1) zero. Affine density stationarity makes nu(psi)=0, and the two stem equations make the remaining term zero. Thus those existing coupled equations already imply zero cut derivative. Combining (5.1)–(5.2) yields the exact forced identity

```
R = 1−alpha(1+2lambda)
    −(m/B2)[4/3+(rL−1)(1+mu)²+(rR−1)(1−mu)²] <1.   (7.2)
```

**Consequently the complete self-consistent opposite-wing system has no solution with R≥1.** No assumption about independent unweighted slice moments appears: the unweighted bulk integral in nu is the correct density derivative of the actual ell-weighted body. This exclusion is already decisive before imposing test optimization or either Hessian gate.

## 8. Boundary alternatives and the distinct weaker functional

Tangent joins d²=fminus or eR²=fplus are included: the strict positive term4delta in Section4 still gives rL,rR>1. Setting either arc length A or D to zero preserves the same proof for that limit chart. These zero-length limits are not substitutes for the complete one-arc alternative with a corner off the common parabola.

At delta=0, provided the marked edge and both stems remain genuine, the same algebra gives rL,rR≥1 and D2≥4/3. The actual cut is still legitimate, but it need not remain in the positive-minimum chart. This causes no supercritical-maximizer gap: the imported conic theorem gives min f>m/2>0 there. Collapse of a stem or of the marked facet is not passed through by division; those cases are outside the genuine-edge chart and cannot arise from its asserted supercritical two-arc representation.

The zero-density line in this chart is disjoint from the marked facet, since Hminus>kL>0 and Hplus>kR>0. Therefore there is no density-zero marked-endpoint Hessian term to evaluate here. This is a proved property of this class, not deletion of the parent's endpoint correction. The first-order moving-endpoint contributions rL and rR in (5.1) are indispensable and have been included. The general zero-endpoint correction remains required in the one-sided alternatives.

For continuation, define D0,D1 analogously to D2, using the OLD mu only in the raw moving-slice derivative. For ell=u0+u1 t+v y and endpoint velocities a'(0),b'(0),

```
Dj=u1∫[-1,1](y−mu)^jdy
   +ell(0,1)b'(0)(1−mu)^j−ell(0,−1)a'(0)(−1−mu)^j.
```

For positive L=J B1²/(V B0 I), actual centering gives the different identity

```
d/ds|0 log L_s
 =−V/J+3B0/V+B2/I+2D1/B1−D0/B0,

m d/ds|0 log L_s
 =R−1+3alpha+m(2D1/B1−D0/B0).
```

The D2 sign does not determine this expression. No independent weak-leverage exclusion or weak global attainment is inferred. The exact source verifies both derivative identities separately.

The useful remaining strong target is now the one-sided conic geometry: one arc, or two arcs on the same side separated by the unique zero-density chord, with its actual negative inward-slice inertia derivative, density equations, stem work and convex-height conditions all coupled. The triangle45/32 result remains available for genuine triangular alternatives, not as a localization shortcut.

## 9. Exact actual curved cut control and executed evidence

The inherited parent fixture is

```
(a,u,v,b,B,C)=(-4,-3,3,4,0,1).
```

Thus U=17, f=y²+1 and kL=kR=5. The new actual control is its entire inward-cut interval0≤s≤1. Its lower graph is

```
f on[-4,−3];  −5(y+1) on[−3,−r_s];  s on[−r_s,r_s];
5(y−1) on[r_s,3];  f on[3,4],     r_s=1+s/5,
```

with height17−t. The whole marked facet is the rectangle

```
t=s,     |y|≤r_s,     |z|≤(17−s)/2.
```

It is a convex uniformly filled curved body, not a polytope. No V/E/F or mechanical census is assigned. Its actual moments are

```
V_s=2(s³−18s²−255s+4584)/15,
J_s=−(7s⁴−168s³−3570s²+128352s−913240)/210,
I_s=(14s⁵−35s⁴−4200s³−40250s²−148750s+16906000)/13125,
B0_s=2r_s(17−s),    B1_s=0,    B2_s=2r_s³(17−s)/3,
g_s=(s+J_s/V_s,0,0),
alpha_s=J_s B0_s/V_s²,
T_marked=diag((J_s/V_s)²,r_s²/3,(17−s)²/12),
R_s=J_s B2_s/(V_s I_s).
```

The source reconstructs the full actual covariance as an exact rational function of s and the actual centered matrices, centroids, poles and masses of all FIVE whole maximal flat facets: the marked rectangle, two stem facets and two height-graph facets. The curved boundary patches are not falsely counted as polygon facets.

At s=0,

```
V=3056/5,       g=(114155/16044,0,0),
Sigma=diag(4365294919/257409936,8453/4011,2759633/288792),
alpha=9703175/24515232,
T_marked=diag(13031364025/257409936,1/3,289/12),
R=122825/1961952.
```

At the new exact endpoint s=1,

```
V=8624/15,      g=(909355/120736,0,0),
Sigma=diag(3301186628137/218657725440,
           16712779/7546000,94848701/10866240),
alpha=7097571/16269176,
T_marked=diag(621919927161/14577181696,12/25,64/3),
R=851708520/9008187881.
```

Both centered tests are exactly Y=y. The cut endpoint s=1 is a positive-volume actual body in the zero-minimum closure of the normalized conic chart, not a claimed supercritical stationary point. The exact gain and initial logarithmic derivative are

```
R_1−R_0=564580557747215/17673632229503712>0,
(d/ds log R_s)|0=4339891407/9331942940>0,
D2|0=92/15.
```

Fifteen strictly positive Bernstein coefficients certify the degree14 numerator of R'_s on the WHOLE interval[0,1], with exact reconstruction of its power polynomial. Positive Bernstein certificates also verify V,J,I,B0,B2 and the scalar gap3/2−R throughout. The full marked three-dimensional matrix gap is checked exactly at the two endpoints. No whole-interval full-matrix certificate is being attributed to that endpoint check.

The control is nonstationary and nonviolating. The source checks (7.1) including its NONZERO arc residual; it does not pretend this fixture satisfies the stationary parabola. Its role is to audit the actual moving whole facet, centering and decomposition, not to supply the all-parameter proof.

## 10. Complete computational recovery

The all-parameter exclusion is the proof in Sections3–7. The executable checks the algebraic identities, the actual cut derivative including mean motion, the distinct weak derivative, the normalized path, exact actual curved moments and the continuous scalar control certificate.

Save the complete source below as `opposite_wing_marked_cut.py` with its final LF. Exact execution used CPython3.13.5 and SymPy1.14.0, assertions enabled. There are no random choices, optimizer, hidden coefficients, checkpoint arrays or required input files.

```
python -B opposite_wing_marked_cut.py > opposite_wing_marked_cut.log
```

The optional inherited-evaluator comparison, also actually executed, is

```
python -B opposite_wing_marked_cut.py --parent /path/to/affine_density_clipping.py
```

It verifies the exact parent source's length and SHA before import. It is not needed for source-only recovery. A fresh directory containing ONLY the new source reproduced the report and stdout byte-identically to the parent-comparison run.

```
opposite_wing_marked_cut.py: 10385 bytes
c0148e2ed2e4a0c7d036cb8f501c9a772079abbba2079e77811a458e5df6e472
opposite_wing_marked_cut_report.json: 14452 bytes
165ad4b62db22bec74746d5ed7c95b1ef2d66984577eb319e85a6917e7fb85
opposite_wing_marked_cut.log: 232 bytes
c7d4064f2783acc928e462f60f8f9012779342ae588f7b82d04379f8c72f622b
```

The complete report SHA-256, also enforced by the expected terminal pin below, is `165ad4b62db22bec74746d5ed7c95b1ef2d66984577eb319e85a691ea7e7fb85`.

Expected terminal output:

```
ALL_PARAMETER_CUT_AND_GEOMETRIC_IDENTITIES_PASS
ACTUAL_CURVED_CUT_INTERVAL [0,1]; ALL_FIVE_FLAT_FACETS_PASS
REPORT 14452 165ad4b62db22bec74746d5ed7c95b1ef2d66984577eb319e85a691ea7e7fb85
OPPOSITE_WING_MARKED_CUT_EXCLUSION_EXACT_PASS
```

These are current-worker executions, not a claimed coordinator replay or proof-assistant formalization. The exact report is an output, never an input. The following full source, together with the analytical proof, is the durable handoff. Convenience copies are the source (`opposite_wing_marked_cut.py`) and the complete capsule (`opposite_wing_marked_cut_capsule.zip`).

```python
"""OPPOSITE_WING_MARKED_CUT_EXCLUSION_V1.
CPython 3.13.5 / SymPy 1.14.0, assertions enabled. No input files.
Optional: --parent PATH compares the actual s=0 control with the exact
12669-byte evaluator in minimum-0295. Not needed to rebuild.
This program verifies algebra and one actual whole-facet cut interval.
The all-parameter geometric sign argument is in the accompanying proof.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json
from math import comb
import sympy as S
Q=S.Rational
t,y,s=S.symbols('t y s',real=True)
PARENT='minimum-0295'
PARENT_SHA='c5da795d12e9ffc99d28fd53e74ba1cc2494cdcc24117b6b85633536d62c0819'
EVALUATOR_SHA='04f2d11e49a192e5d9e0cbd0bcd63dda99a5059e9d12bbb1e5a9baa9ddc58c99'

def simp(x): return S.factor(S.cancel(x))
def zero(x): assert simp(x)==0, simp(x)
def integ(f,x,a,b):
    # The literal parent's exact polynomial integration rule.
    return simp(sum(c*(b**(k[0]+1)-a**(k[0]+1))/(k[0]+1)
                    for k,c in S.Poly(S.expand(f),x).terms()))
def bernstein(f,x,a,b):
    u=S.Symbol('u');p=S.Poly(S.expand(f.subs(x,a+(b-a)*u)),u);n=p.degree()
    v=[sum(p.nth(j)*Q(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    zero(sum(v[k]*comb(n,k)*u**k*(1-u)**(n-k) for k in range(n+1))-p.as_expr())
    return v

def universal_algebra():
    d,e,A,D,B,C,mu=S.symbols('d e A D B C mu',real=True)
    fm=C+1-2*B;fp=C+1+2*B
    kl=d+2*(1-B)+fm/d;kr=e+2*(1+B)+fp/e
    u=-1-d;v=1+e;a=u-A;b=v+D
    f=y*y+2*B*y+C;U=(a+b+2*B)*y+C-a*b
    Hm=U.subs(y,-1);Hp=U.subs(y,1);Z=d*e+C-1
    zero(f.subs(y,u)-d*kl);zero(f.subs(y,v)-e*kr)
    zero(-kl-S.diff(f,y).subs(y,u)-(d*d-fm)/d)
    zero(S.diff(f,y).subs(y,v)-kr-(e*e-fp)/e)
    zero(Hm-kl-Z-(d*d-fm)/d-D*d-(2+e+D)*A)
    zero(Hp-kr-Z-(e*e-fp)/e-A*e-(2+d+A)*D)
    product_certificate=(d*d-fm)*e*e+fm*(e*e-fp)+4*(C-B*B)
    zero(d*d*e*e-(C-1)**2-product_certificate)
    rL,rR=S.symbols("rL rR",real=True)
    raw_derivative=rL*(1+mu)**2+rR*(1-mu)**2-Q(2,3)-2*mu*mu
    zero(raw_derivative-Q(4,3)-(rL-1)*(1+mu)**2-(rR-1)*(1-mu)**2)
    c,w=S.symbols("c w",real=True,nonzero=True)
    BB=(B+c)/w;CC=(c*c+2*B*c+C-s)/(w*w)
    x=S.Symbol('x')
    zero(x*x+2*BB*x+CC-(f.subs(y,c+w*x)-s)/(w*w))
    zero(CC-BB*BB-(C-B*B-s)/(w*w))
    dc,dw,p,q=S.symbols('dc dw p q',real=True)
    cs=s*dc;ws=1+s*dw
    new_height=p*y/ws+(q+p*cs-s)/(ws*ws)-t
    psi=p*dc-1-2*q*dw-p*dw*y
    df=2*(dc-B*dw)*y+2*B*dc-1-2*C*dw
    zero(S.diff(new_height,s).subs(s,0)-psi)
    new_curve=(f.subs(y,cs+ws*y)-s)/(ws*ws)
    zero(S.diff(new_curve,s).subs(s,0)-df)
    # First-order raw integrals of an actual inward cut.
    V,J,I,B0,B1,B2,D0,D1,D2=S.symbols('V J I B0 B1 B2 D0 D1 D2',nonzero=True)
    Vs=V-s*B0;Js=J-s*V;mu_s=-s*B1/Vs
    Is=I-s*B2-s*s*B1*B1/Vs
    b0=B0+s*D0;b1=B1+s*D1-mu_s*b0
    b2=B2+s*D2-2*mu_s*(B1+s*D1)+mu_s*mu_s*b0
    RR=Js*b2/(Vs*Is);LL=Js*b1*b1/(Vs*b0*Is)
    dlog=simp(S.diff(RR,s).subs(s,0)/RR.subs(s,0))
    expected=-V/J+D2/B2+2*B1*B1/(V*B2)+B0/V+B2/I
    zero(dlog-expected)
    leverage=simp(S.diff(LL,s).subs(s,0)/LL.subs(s,0))
    zero(leverage-(-V/J+3*B0/V+B2/I+2*D1/B1-D0/B0))
    return dict(domain='d,e>0; A,D>=0; C>B^2; d^2>=C+1-2B; e^2>=C+1+2B',
                product_certificate=product_certificate,
                left_excess=Z+(d*d-fm)/d+D*d+(2+e+D)*A,
                right_excess=Z+(e*e-fp)/e+A*e+(2+d+A)*D,
                section_derivative=raw_derivative,
                cut_log_derivative=dlog,leverage_log_derivative=leverage,
                normalized_path=[(a-c)/w,(u-c)/w,(v-c)/w,(b-c)/w,BB,CC],
                path_c='s*(1/kr-1/kl)/2',path_w='1+s*(1/kr+1/kl)/2',
                normalized_density_velocity=psi,normalized_parabola_velocity=df)

def actual_control():
    # Exact parent fixture (-4,-3,3,4,0,1), now cut by t>=s, 0<=s<=1.
    # Actual original coordinates (t,y,z), uniform density in 3D.
    f=y*y+1;U=S.Integer(17);r=1+s/5;ell=U-t
    pieces=[(-4,-3,f),(-3,-r,-5*(y+1)),(-r,r,s),
            (r,3,5*(y-1)),(3,4,f)]
    def moment(p,q,power=1):
        return simp(sum(integ(integ(t**p*y**q*ell**power,t,L,U),y,a,b)
                        for a,b,L in pieces))
    V=moment(0,0);Jraw=moment(1,0);gt=simp(Jraw/V)
    zero(moment(0,1));zero(moment(1,1))
    I=moment(0,2);J=simp(Jraw-s*V)
    cov=S.diag(simp(moment(2,0)/V-gt*gt),simp(I/V),simp(moment(0,0,3)/(12*V)))
    B0=simp(2*r*(17-s));B1=S.S.Zero;B2=simp(Q(2,3)*r**3*(17-s))
    alpha=simp(J*B0/(V*V));R=simp(J*B2/(V*I));m=simp(J/V)
    TF=S.diag(m*m,r*r/3,(17-s)**2/12);cf=S.Matrix([-m,0,0]);pole=S.Matrix([-1/m,0,0])
    assert TF*pole==cf
    zero(R.subs(s,0)-Q(122825,1961952))
    zero(V.subs(s,0)-Q(3056,5));zero(J.subs(s,0)-Q(91324,21))
    zero(I.subs(s,0)-Q(135248,105))
    # Full physical moments of all five maximal flat facets, not integration pieces.
    flats=[dict(name='marked t=s',mass=alpha,c=cf,T=TF,pole=pole)]
    area=moment(0,0,0);mtA=simp(moment(1,0,0)/area);mt2A=simp(moment(2,0,0)/area)
    for sign in [-1,1]:
        cc=S.Matrix([mtA-gt,0,sign*(17-mtA)/2])
        TT=S.Matrix([[mt2A-2*gt*mtA+gt*gt,0,
                      sign*(17*(mtA-gt)-mt2A+gt*mtA)/2],
                     [0,moment(0,2,0)/area,0],
                     [sign*(17*(mtA-gt)-mt2A+gt*mtA)/2,0,
                      (289-34*mtA+mt2A)/4]]).applyfunc(simp)
        pp=S.Matrix([1,0,2*sign])/(17-gt)
        assert (TT*pp-cc).applyfunc(simp)==S.zeros(3,1)
        flats.append(dict(name='graph z='+str(sign)+'(17-t)/2',
                          mass=simp((17-gt)*area/(2*V)),c=cc,T=TT,pole=pp))
    xx=S.Matrix([5*y-5-gt,y,0]);hh=22-5*y
    edge_mass=integ(hh,y,r,3)
    cc=(xx.applyfunc(lambda z:integ(z*hh,y,r,3))/edge_mass).applyfunc(simp)
    TT=(xx*xx.T).applyfunc(lambda z:integ(z*hh,y,r,3)/edge_mass)
    TT[2,2]=integ(hh**3,y,r,3)/(12*edge_mass);TT=TT.applyfunc(simp)
    for sign in [-1,1]:
        refl=S.diag(1,sign,1);ccc=refl*cc;TTT=refl*TT*refl
        pp=S.Matrix([-1,sign*5,0])/(5+gt)
        assert (TTT*pp-ccc).applyfunc(simp)==S.zeros(3,1)
        flats.append(dict(name='stem t='+str(sign)+'5y-5',
                          mass=simp((5+gt)*edge_mass/V),c=ccc,T=TTT,pole=pp))
    # Continuous interval proof for this nonviolating control only.
    numerator,denominator=S.fraction(simp(S.diff(R,s)))
    bc=bernstein(numerator,s,0,1);assert all(c>0 for c in bc)
    bounds={}
    for name,z in [('V',V),('J',J),('I',I),('B0',B0),('B2',B2)]:
        v=bernstein(z,s,0,1);assert all(c>0 for c in v);bounds[name]=v
    # The derivative's denominator is a positive constant times V^2 I^2.
    factor=simp(denominator/(V*V*I*I));assert factor>0 and not factor.has(s)
    gapnum=simp((Q(3,2)-R)*V*I)
    gapbc=bernstein(gapnum,s,0,1);assert all(c>0 for c in gapbc)
    dlog0=simp((S.diff(R,s)/R).subs(s,0))
    zero(dlog0-Q(4339891407,9331942940))
    expected=(-1+alpha.subs(s,0)+R.subs(s,0))/m.subs(s,0)+Q(92,15)/Q(34,3)
    zero(dlog0-expected)
    V0=V.subs(s,0);J0=J.subs(s,0);I0=I.subs(s,0);edge2=B2.subs(s,0)
    phi=t/J0-1/V0-y*y/I0
    nu_one=simp((moment(1,0,0)/J0-moment(0,0,0)/V0-moment(0,2,0)/I0).subs(s,0)
                +Q(2,3)/edge2)
    WL=integ((y+1)*(22+5*y)*phi.subs(t,-5*(y+1)),y,-3,-1)
    WR=integ((y-1)*(22-5*y)*phi.subs(t,5*(y-1)),y,1,3)
    arc=2*integ((16-y*y)*phi.subs(t,f),y,3,4)
    decomposition=simp(-Q(39,5)*nu_one-WL+WR+Q(7,5)*arc)
    zero(decomposition-dlog0)
    records=[]
    for value in [S.S.Zero,S.S.One]:
        sub=lambda z:simp(z.subs(s,value))
        matrix=lambda M:M.applyfunc(sub)
        cv=matrix(cov);tt=matrix(TF);aa=sub(alpha)
        assert all(cv[:k,:k].det()>0 for k in (1,2,3))
        assert all((Q(3,2)*cv-aa*tt)[:k,:k].det()>0 for k in (1,2,3))
        records.append(dict(s=value,volume=sub(V),centroid=S.Matrix([sub(gt),0,0]),
                            Sigma=cv,marked_T=tt,marked_alpha=aa,R=sub(R),
                            centered_test='y',normal_mean=sub(m)))
    return dict(parameters=[-4,-3,3,4,0,1],interval=[0,1],pieces=pieces,
                density=ell,volume=V,J_inward=J,I_y=I,centroid=S.Matrix([gt,0,0]),
                Sigma=cov,marked_B=[B0,B1,B2],marked_T=TF,marked_alpha=alpha,R=R,
                all_five_flat_facets=flats,positive_derivative_Bernstein=bc,
                positive_raw_Bernstein=bounds,derivative_denominator_factor=factor,
                three_halves_scalar_gap_Bernstein=gapbc,
                log_derivative_at_zero=dlog0,normalized_cut_decomposition=dict(nu_one=nu_one,
                W_left=WL,W_right=WR,arc_error_integral=arc,total=decomposition),endpoint_gain=simp(R.subs(s,1)-R.subs(s,0)),
                endpoint_records=records,
                scope='Actual curved uniform lifts. No finite polytope census or equilibrium claim.')

def encode(x):
    if isinstance(x,S.MatrixBase):return [[encode(v) for v in row] for row in x.tolist()]
    if isinstance(x,S.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    assert __debug__
    parser=argparse.ArgumentParser();parser.add_argument('--parent');args=parser.parse_args()
    report=dict(theorem='OPPOSITE_WING_MARKED_CUT_EXCLUSION_V1',parent=PARENT,
                parent_sha256=PARENT_SHA,algebra=universal_algebra(),control=actual_control())
    if args.parent:
        path=Path(args.parent);raw=path.read_bytes()
        assert len(raw)==12669 and hashlib.sha256(raw).hexdigest()==EVALUATOR_SHA
        spec=importlib.util.spec_from_file_location('literal_parent',path)
        parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
        p=parent.two_wing_control(-4,-3,3,4,0,1)
        c=report['control']['endpoint_records'][0]
        assert p['volume']==c['volume'] and p['centroid']==c['centroid']
        assert p['Sigma']==c['Sigma'] and p['marked_T']==c['marked_T']
        assert p['marked_alpha']==c['marked_alpha'] and p['R']==c['R']
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('opposite_wing_marked_cut_report.json').write_bytes(data)
    print('ALL_PARAMETER_CUT_AND_GEOMETRIC_IDENTITIES_PASS')
    print('ACTUAL_CURVED_CUT_INTERVAL [0,1]; ALL_FIVE_FLAT_FACETS_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('OPPOSITE_WING_MARKED_CUT_EXCLUSION_EXACT_PASS')
if __name__=='__main__':main()
```
