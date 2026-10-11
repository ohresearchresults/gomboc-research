# minimum-0133

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# BALANCED_RIDGE_DRIFT_AND_TWO_PLANE_COUNTERDOMAIN_V1

## Determination

**The apex-independent centroid plane has a previously unproved, shape-uniform limitation: throughout the COMPLETE strict balanced normal form, its normal lies outside both orientations of the ridge’s supporting-normal cone. Its defining cross product never vanishes, and the plane always cuts the relative interior of the octagonal base.** I prove a quantitative centroid-drift inequality establishing these statements below. No restriction on the eight cuts, either projective parameter, apex separation, metric conditioning, or root location is used in that theorem.

**The natural two-plane/base-rim bridge is false even inside the accepted necessary joint-metric bounds.** An executed exact own-centroid222/weak000 body has neither a two-high-half certificate from the persistent plane nor one from the base-parallel central plane, while the actual base facet is strictly nonstable. Its actual covariance-gauged condition number is rigorously below 128/3, and every vertex-pole product is below176. A second exact own-centroid323/weak000 body, also with condition number below43, has ALL stable feet and ALL unstable vertices in the SAME open half of its persistent plane.

These are counterexamples to proposed proof mechanisms, not110 constructions. A different, geometrically specified ridge-normal plane detects two unstable vertices in both controls. This leads to an exact quadratic angular reduction for the entire compact ridge-normal family. The full fourteen-outer-parameter joint S=U=1 obstruction remains unresolved; no minimum bound or incidence-register count changes.

## 1. Source authority and full domain

The complete 1,677-line journal update was read through EOF, including common memory, branch memory and literal parent. Its325218 bytes have SHA-256 `e6153bf6571fc2a5ddb690def9d8ce627cf5b7e5c0d62e42f8cf39031d15af98`. The literal parent `minimum-0129` authenticates as a27952-byte compact version-2 envelope with the required SHA-256 `7e0b1f5f3c7675c7733a26653deeb42edde348807a2a55883e4f5be444417d45`.

The supplied complete repair wrapper was read and executed, and both decoded source units were read completely. Its13001 bytes match SHA-256 `7fcf13683f4b90d836dcdff1d630703881e5aec93cfa3dd2ef8c9f1a34035ee7`. The repaired units match their parent pins. There is no authority conflict or missing computational dependency for the new work. The previous two expensive inner-fibre certificates were retained as inherited evidence, not unnecessarily rerun. The repair’s complete decoding and pin checks are explicit in the supplied material. :contentReference[oaicite:0]{index=0}

Use eight strictly positive cuts `((sx,sy),(wx,wy),(nx,ny),(ex,ey))`, with

` sx+ex<2, wx+nx<2, sy+wy<2, ny+ey<2. `

The raw vertices are

```text
P0=(-1+sx,-1,0)       P1=(-1,-1+sy,0)
P2=(-1,1-wy,0)        P3=(-1+wx,1,0)
P4=(1-nx,1,0)         P5=(1,1-ny,0)
P6=(1,-1+ey,0)        P7=(1-ex,-1,0)
P8=(-a,0,1)           P9=(a,0,1),       a>0.
```

Let `fi=1+u*Pi_x+v*Pi_y`, `Yi=Pi/fi`, requiring all ten denominators positive. The coefficients u,v are REAL, not individually positive. In particular `|u|a<1`. The actual maximal facets are

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1) F2=(1,8,2) F3=(2,8,3) F4=(3,8,9,4)
F5=(4,9,5) F6=(5,9,6) F7=(6,9,7) F8=(7,9,8,0).
```

Their cycles determine17 true edges. The parent’s complete coverage theorem identifies this domain, up to affine equivalence, with the whole balanced realization type. :contentReference[oaicite:1]{index=1}

Write the raw base as `l(y)<=x<=r(y)`, `-1<=y<=1`, where l is convex and r concave. Put

```text
f_l(y)=1+u*l(y)+v*y,    f_r(y)=1+u*r(y)+v*y,
b=2*integral_B (1+u*x+v*y)^(-3) dxdy,
L=integral_-1^1 f_l(y)^(-2) dy,
R=integral_-1^1 f_r(y)^(-2) dy,             c=L+R.
```

These are exact actual planar integrals. Equivalently they are the finite rational edge/fan sums in the recovery. Their derivatives hold the cuts fixed. Define

```text
c0=(-bu/(4b),-bv/(4b),1/4),
c1=(-cu/(4c),-cv/(4c),1/2),
d=(1,0,-u),   Delta=c1-c0,
k=1-u^2*a^2, W=b+a*c, lambda=b/W.
```

The parent’s actual mass identities give

```text
L-R=u*b,    c>|u|b,
Vol=W/(6k),
g(a)=lambda*c0+(1-lambda)*c1-a^2*u*d/(2k).
```

Here g is the TRUE centroid of the uniformly refilled projective image. The persistent central plane is `n.(Y-c0)=0`, with `n=Delta cross d`; after actual centering `X=Y-g`, it is `n.X=0`. These are the parent’s coupled actual moments, not independently chosen centers. :contentReference[oaicite:2]{index=2}

## 2. Full-domain theorem: strict ridge-normal drift

For `-1<=theta<=1`, define

`qtheta_raw=(u,v+theta,1)`.

Both apices satisfy `qtheta_raw.Y8=qtheta_raw.Y9=1`. On a base vertex,

`1-qtheta_raw.Yi=(1-theta*Pi_y)/fi>=0`.

The endpoint normals are exactly the uncentered supporting normals of F4 and F8. Positive multiples of this family describe the complete normal cone of the true ridge8--9.

### Theorem A

Throughout the full domain,

```text
q(+1)_raw.Delta >= L*R*(2-sx-ex)/(b*c*f0*f7) >0,
q(-1)_raw.Delta >= L*R*(2-wx-nx)/(b*c*f3*f4) >0.
```

Consequently `qtheta_raw.Delta>0` for every theta in the entire CLOSED interval[-1,1]. In fact, putting

`h0(theta)=1-qtheta_raw.c0`, `h1(theta)=1-qtheta_raw.c1`,

one has

```text
0<h1(theta)<h0(theta),
1-qtheta_raw.g(a)=[b*h0(theta)+a*c*h1(theta)]/(b+a*c),
d/da [qtheta_raw.g(a)]=b*c*qtheta_raw.Delta/(b+a*c)^2 >0.
```

Thus the true centroid moves strictly toward BOTH quadrilateral supporting planes as a increases. For every fixed reciprocal metric N, both actual quadrilateral pole norms increase strictly with a.

### Proof of the endpoint inequality

The needed one-dimensional lemma is elementary and useful independently. For a positive piecewise-affine function f on[-1,1], put

`J_-(f)=integral (1-y)f^(-3)dy / integral f^(-2)dy`.

If f is convex, `J_-(f)>=1/f(-1)`; if f is concave, the inequality reverses. The analogous assertion for `J_+(f)`, using1+y, has endpoint1.

To prove it, form the radial planar set

```text
K_f={(s,t)>=0 : (s+t)*f((s-t)/(s+t))<=1},
```

including the origin. Its area is `(1/4) integral f^(-2)`, and its first t-moment is `(1/12) integral (1-y)f^(-3`; hence its t-centroid is `J_-(f)/3`. Its intercept on the t-axis is `B=(0,1/f(-1))`.

For convex f, K_f is a convex polygon. A positive triangle fan from B shows that its t-centroid is at least `B_t/3`. For concave f, K_f lies inside the triangle with intercepts0, `(1/f(1),0)`, B. The complement of K_f in that triangle, up to measure-zero boundary, is convex: it is the intersection of the triangle with a superlevel set of the concave perspective of f. It contains B, so its t-centroid is at least `B_t/3` by the same fan argument. Subtracting its genuine area and moment from those of the triangle makes K_f’s t-centroid at most `B_t/3`. Zero-area complements give equality. This proves the lemma without independently fitted weights.

Suppose u>0. Then f_l is convex, f_r concave. Set

`I_l=integral (1-y)f_l^(-3)dy`, `I_r=integral (1-y)f_r^(-3)dy`.

Direct integration in x and differentiation of b,c give

```text
q(+1)_raw.Delta=(R*I_l-L*I_r)/[c*(L-R)]
              =L*R/[c*u*b] * (I_l/L-I_r/R).
```

The lemma bounds the bracket below by

```text
1/f_l(-1)-1/f_r(-1)
=u*(2-sx-ex)/(f0*f7).
```

Substitution proves the first assertion. The other endpoint uses1+y and the top edge. For u<0, interchange convex and concave boundary functions; the negative sign cancels with u and yields exactly the same positive lower bounds. At u=0, continuity inside the open basal-denominator domain gives the displayed inequalities; their right-hand sides remain strictly positive, so strictness is not lost in that limit.

Finally,

`h1(theta)=[integral (1-theta*y)(f_l^(-3)+f_r^(-3))dy]/(2c)>0`.

The endpoint inequalities and convex combination give `h0>h1`; the centroid identity then gives the derivative. The proof uses no metric and no special slopes of the four corner cuts. It also applies to any convex polygonal base with noncollapsed horizontal top/bottom edges in this explicitly specified two-apex chart.

### Corollaries resolving the persistent-plane geometry

First, **n never vanishes**: every ridge-cone normal annihilates d but has positive pairing with Delta, so Delta cannot be parallel to d. The parent’s possible-zero-cross-product fallback is therefore unnecessary on this strict domain.

Second, put `A=1/4+u*Delta_x+v*Delta_y`. The endpoint result says `A>|Delta_y|`. If `Delta_y!=0`, normalizing n to third coordinate1 gives

```text
n/n_z=(u,v+theta_star,1),
theta_star=-A/Delta_y,          |theta_star|>1.
```

If `Delta_y=0`, n is a nonzero multiple of e_y, the infinite-angle case. Thus neither orientation of the persistent normal belongs to the ridge’s supporting-normal cone.

Third, **the persistent plane always cuts the relative interior of B**. Otherwise all basal vertices would lie in one closed halfspace. Since the actual centroid is interior and both apices have the same plane height, the ridge would lie strictly in the opposite halfspace. Translating that plane through the ridge would then make one orientation of n a supporting normal of the ridge, contradicting the preceding result.

In a generic persistent section, the basal vertices opposite the apices therefore form a nonempty proper consecutive block of length k. Its true section vertices lie on the two crossing base edges and those k spokes: the section has k+2 vertices. The56 possible consecutive blocks, k=1,...,7, are a safe finite overcover, NOT an assertion that all56 occur. Vertex-on-plane and ridge-on-plane strata must remain separate.

## 3. Exact failure of the two-plane/base-rim bridge inside the joint-metric bounds

Define H(Pi) to mean that each open half of a central plane Pi contains an actual vertex whose squared M-norm is at least the maximum squared norm on the actual section. This premise yields a strict U in each half, including at equality, by the usual strict quadratic norm increment along true edges.

The following considerably weaker Boolean prerequisite already fails:

`H(persistent plane) OR H(base-parallel central plane) OR F0 strictly stable.`

This defeats a proposed proof that uses those two high-half tests and otherwise must force stability of the actual base via a base-rooted rim/lens argument. It does not refute the accepted conditional lens theorem, nor exclude a rescue using OTHER facets or OTHER planes.

### Primary control TWO

All decimal entries below are exact rational inputs, not floating tolerances:

```text
cuts=((.439,1.093),(.109,.771),(.152,.984),(.231,.614)),
a=7.214, u=-.125=-1/8, v=.114,
L=((1,0,0),(1.562,1.722,0),(-7.631,-.213,.174)),
M=L*L^T,                 N=L^(-T)*L^(-1).
```

An ordinary rational-coordinate Euclidean realization is `L^T*(Yi-g)`. Its actual volume centroid is0; its actual poles are `L^(-1)*qf`. No polar mass is refilled or recentered.

The exact full audit gives

```text
V/E/F=10/17/9,
S={F1,F4}, U={4,8}, H={(3,8),(7,9)},
physical weak points=0, zero primitives=0.
```

The chart volume is

`193701806040093925703029436312507000000000 / 5675649031432374833922642398060557943607`.

For orientation only, its exact generated centroid is approximately `(17.5767947945,-.0715971332,2.6266847012)`. The apex heights are exactly `4000/7607` and `4000/393`: apex8 is BELOW its own COM, apex9 above it. Both unstable vertices4,8 are below the base-parallel central plane.

For the persistent plane, the negative vertex set is `{0,6,7}` and the positive set is `{1,2,3,4,5,8,9}`. Its section is the genuine pentagon on

`(0,1),(0,8),(5,6),(6,9),(7,9)`.

Its squared section maximum is approximately27.3110693002. EVERY negative-half vertex has smaller squared norm; the exact minimum margin is greater than17. The persistent plane therefore fails H, regardless of which stress support is tried.

For the base-parallel central plane, the upper half contains ONLY vertex9. Its genuine pentagonal section lies on

`(4,9),(5,9),(6,9),(7,9),(8,9)`.

Its squared section maximum is approximately19.8308966053, exceeding vertex9’s squared norm by more than13. This plane also fails H. The actual base foot violates F1,F2,F3 strictly, so F0 is not stable.

This failure is not attributable to an inadmissibly ill-conditioned physical candidate gauge. Exact leading-minor certificates prove, for the actual uniform covariance Sigma,

```text
(3/40)N < Sigma < (16/5)N,
kappa(Sigma^(1/2) M Sigma^(1/2)) <128/3<43,
max_vertex ||x||_M^2<32,
max_pole ||q||_N^2<11/2,
every vertex-pole product <176.
```

These are stronger than the inherited convenient necessary kappa<48 and product caps for a joint candidate. They are NECESSARY-bound compatibility, not joint feasibility: this body really has two S and two U. The inherited bounds and their covariance gauge are explicit in the notebook. :contentReference[oaicite:3]{index=3}

For any stress on either demonstrated low half, its weighted actual squared norm is below the section maximum. The stress’s shear-minimized energy cannot exceed that weighted norm. Thus increasing support size, including allowing all vertices rather than at most three, cannot supply an H witness for that half at this SAME metric. A base-L fallback that forces the actual base to be stable cannot cover it either.

## 4. Companion: all stable and unstable features in one persistent half

The exact input ONE is

```text
cuts=((.31,.93),(.24,.05),(1.02,.90),(.63,.28)),
a=.18, u=-.32, v=.05,
L=((1,0,0),(1.13,1.17,0),(5.09,.26,2.82)),
M=L*L^T, N=M^-1.
```

Its complete physical census is

```text
S={F1,F6,F7}, U={0,9}, H={(4,9),(6,9),(7,9)},
V/E/F=10/17/9, physical weak points=0, zero primitives=0.
```

The persistent positive half contains basal vertices `{1,2,3,4,5}`; the negative half contains `{0,6,7,8,9}`. ALL three stable feet and BOTH unstable vertices are strictly negative. The positive-half vertices are all below the section maximum, with exact margin greater than12. F0 is strictly nonstable. Both apices are nevertheless above the ordinary vertical COM, so this phenomenon does not require the below-COM transition.

Exact covariance and reciprocal-norm certificates give

`(1/23)N<Sigma<(43/23)N`, hence kappa<43, and all vertex-pole products<176.

This directly disproves a universal assertion that the persistent plane must separate either a pair of stable features or a pair of unstable features.

Two earlier exact nonrecord controls are retained in the same complete source rather than discarded. Their exact16-parameter inputs are the literal `MAIN` and `CALIBRATION` arrays in the decoded unit; no new kappa<43 claim is made for them:

| Control | Strict S | Strict U | Strict H edges | Physical weak / zero primitives |
|---|---|---|---|---|
| high_metric |3,5|3,8|(3,8),(5,6)|0 /0|
| calibration |0,2|1,9|(0,7),(2,3)|0 /0|

The first has all four extrema in one persistent half and strict222. The second uses the parent’s independent-cut fingerprint but a different common metric; its S feet and U vertices occupy opposite persistent halves. Both are actual10/17/9 bodies with true refilled centroids and full exact audits, not110.

## 5. Executed continuous counterdomains and an actual successful replacement plane

The exact recovery certifies WHOLE closed boxes in all16 independent parameters

`(sx,sy,wx,wy,nx,ny,ex,ey,a,u,v,L21,L22,L31,L32,L33)`.

Every coordinate varies independently within radius10^-10 of TWO, or radius10^-5 of ONE. There are252 and242 strictly positive interval guards,494 total. They cover the geometric domain, all68 primitive signs, all nonincident supporting inequalities, relevant halfspace signs, the displayed low-half comparisons, the actual covariance Loewner inequalities, and all product bounds. Thus all stated counter-mechanisms persist throughout the boxes. These small boxes certify robustness of a FALSE proposed bridge; they are not offered as a substantial positive outer-domain exclusion.

For TWO, the alternative central plane with normal

`(u,v-239/1000,1)`

has, at the rational center, normal `(-1/8,-1/8,1)`, equivalently `(-1,-1,8)`. It belongs to the ridge’s supporting-normal cone, unlike the persistent normal, whose normalized theta is approximately-8.9890030322. The alternative has both apices positive and every basal vertex negative. Its squared section maximum is approximately2.5165851286. Vertices4 and8 lie in opposite halves and exceed that maximum by a common margin greater than25. On the WHOLE TWO box, the corresponding same-metric margin remains greater than24.

For ONE, the supporting-ridge normal `(u,v,1)` also supplies two high halves, with vertices0 and9. Its margin remains greater than1 on the whole ONE box. These controls are therefore NOT all-plane counterexamples.

At the exact TWO center, a separate complete angular certificate proves H for EVERY theta in the CLOSED interval `[-1,1/4]`, not just theta=-239/1000. It has3 actual incidence cells,25 quadratic positivity certificates, and4 explicitly checked vertex-on-plane/end-point strata. This is an executed angular certificate for this fixed body and metric, not an assertion about that whole angle interval throughout the outer boxes.

## 6. Full-domain finite angular reduction

The compact family `qtheta_raw=(u,v+theta,1)`, theta in[-1,1], is a useful replacement formulation. Both apices are ALWAYS strictly above its central plane, even when one apex is below the ordinary vertical COM. Theorem A gives its strict, controlled centroid drift as a varies.

For any fixed actual body and M, put

```text
Ai=u*Xi_x+v*Xi_y+Xi_z,    Bi=Xi_y,
hi(theta)=Ai+theta*Bi.
```

Only the eight basal height equations can change sign. Thus there are at most8 nonconstant angular event roots and at most9 open angular intervals. Persistent zero-height vertices must be retained explicitly. On an interval the half-vertex sets are fixed, so the maximum vertex norm in each half is fixed. Let T be the smaller of those two maxima.

For a true crossing edge ij, its actual section point has numerator

```text
V0=Aj*Xi-Ai*Xj,
V1=Bj*Xi-Bi*Xj,
d0=Aj-Ai, d1=Bj-Bi,
r_ij(theta)=(V0+theta*V1)/(d0+theta*d1).
```

The exact condition `||r_ij(theta)||_M^2<=T` is the quadratic inequality

```text
[T*d0^2-V0^T M V0]
+2*theta*[T*d0*d1-V0^T M V1]
+theta^2*[T*d1^2-V1^T M V1] >=0.
```

There are at most9 true section vertices in a generic interval. Zero-height vertices contribute their actual norm inequalities; angular walls are checked with those vertices and all genuinely crossing edges. Therefore searching the ENTIRE supporting-ridge angular family at a fixed outer point is an exact univariate quadratic sign problem, not a sampled direction search. Every U1 candidate must fail this complete angular test. This adds a compact auxiliary direction variable to the geometric strategy without introducing independent primal/polar metrics.

No theorem here says that some theta must succeed at every outer point. That is a substantive remaining question, and one-sided low-half certificates may still require genuinely nonbasal stable-facet arguments.

## 7. What was computed, what was not, and continuation

Each of the four exact controls was reconstructed by all120 supporting triples, all actual maximal facets and true edges, two positive apex-fan volume/centroid integrations, and two exact actual covariance integrations. The rational physical affine map was then checked by fresh mass integration and by every primal/polar Gram pairing. All17 edge feet were checked against their true normal-cone coefficients through `M*p=lambda_f*q_f+lambda_h*q_h`; full strict and physical-weak packets were retained. Thus a harmless zero could not have been mistaken for an equilibrium; in these controls all68 primitives are nonzero.

The exact interval arithmetic rounds OUTWARD to rational multiples of2^-80 after every elementary operation. Positive lower endpoints are certificates over whole closed boxes. The angular certificate minimizes each quadratic exactly at its interval endpoints and, where applicable, its stationary point, then checks all wall sections separately. None of these positivity claims rests on sampling.

The optional numerical source uses actual tetrahedral centroids and covariances and samples ONE covariance-gauged metric with eigenvalue ratio40. Seed937581 found the ONE locator at shape105/metric1141; rounding its parameters to two decimal places gives the exact ONE input. Seed937583 found TWO at shape14/metric1643; three-place rounding gives TWO. Both complete locator outputs were reproduced byte for byte after source-only recovery. Numerical locations are not the proof of their rational successors.

A stronger finite search, seed937582, tested3000 shapes with2000 metrics each for simultaneous two-plane/base failure AND all stable/unstable features in one persistent half. It found none. Its complete runnable mode and exact limits are retained; this SIX-MILLION-case nonfinding is NOT an exclusion of that continuous class.

The most useful continuation is the WHOLE supporting-ridge normal fan, with its new strict drift inequalities and exact quadratic angular elimination, coupled to the parent’s reciprocal height pencil. A successful outer proof may switch theta or use nonbasal stable facets, but must retain the same actual centroid and M,N. Restricting attention to the persistent plane, or simply adding the original base-parallel plane and a mandatory-base-stability fallback, is now ruled out as a universal bridge even under the known joint-metric caps.

The accepted34<=C_min<=622 interval and all register counts remain unchanged. No strict110, extraweakjoint1 construction, all-SPD shape exclusion, or entire balanced-incidence exclusion is asserted.

## 8. Complete source-only recovery capsule

The following COMPLETE wrapper embeds both runnable source units, including every exact input, hull/mass/covariance/physical-packet audit, interval certificate, angular certificate, and the optional numerical locator. It has no parent-file, archive, report-download, or connector dependency. The analytic proof above is not replaced by the finite audits.

Save it as `recover_ridge_bridge.py`, UTF-8/LF with one final LF. With assertions enabled, run in a fresh directory:

```sh
python -S recover_ridge_bridge.py
python -S balanced_ridge_bridge.py build
python -S balanced_ridge_bridge.py check
```

Executed exact environment: CPython3.13.5, standard library only. Both an ordinary build/check and a fresh wrapper-only reconstruction followed by build/check were executed; the full report matched byte for byte. Optional numerical replay requires NumPy2.3.5; the source fixes one BLAS/OMP thread:

```sh
python locate_ridge_bridge.py one
python locate_ridge_bridge.py two
python locate_ridge_bridge.py strong_two
```

Exact pins:

```text
recover_ridge_bridge.py 13560 bytes
58405c52016fba5e6440c4906ca04438e328778f1ed5239f79d5b5f61502f042
Decoded two-source JSON pack 23477 bytes
5c8f925c23c73c77e545625937828ebfb5ff99cde87135c8f6fdf07451eae43c
balanced_ridge_bridge.py 18217 bytes
5f38f53c8523c53538c42e17c5d9c775be749fe580d7f6bdf071a7eb4c1a5819
locate_ridge_bridge.py 4797 bytes
71ba029995da3e137514a5895cc08da5594cb5004dbe999a369c425de2a993ee
balanced_ridge_bridge.json 440210 bytes
b33520ddce783d0383aaca54bffe05688224d49a2c02f0dad2d8af966cfa068e
locator_one.json 574 bytes
3a143004b22b9ff5a4fac80e4f26613318925121eaab562fc40571d17679bf99
locator_two.json 609 bytes
1c12a091ee5b08225141ddafa7fe7860129472f7bdcfaa670bd598e4c0cf6ff2
locator_strong_two.json 118 bytes
132cb38d83117513e744c5bf25017c61b54f02bb540b9a7bc85aa7cc0829e76a
```

Expected terminal markers include:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]



[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


**Recovery limitation:** The inline compressed stream above is not a faithful copy of the tested wrapper and will not pass its integrity checks. It must not be treated as a durable source capsule. The analytic proofs, explicitly stated parameter inputs and reconstruction formulas in Sections1–7 remain self-contained, but the newly computed certificate reports remain ephemeral for an executor receiving only this response. Their complete tested computational dependency is the exact13560-byte wrapper or its two complete decoded source units; these contents must not be guessed from the corrupted inline stream.

The complete tested files are preserved for transfer: [recovery wrapper](sandbox:/mnt/data/recover_ridge_bridge.py), [readable exact generator/verifier](sandbox:/mnt/data/balanced_ridge_bridge.py), [complete optional numerical locator](sandbox:/mnt/data/locate_ridge_bridge.py), and [full exact audit and certificates](sandbox:/mnt/data/balanced_ridge_bridge.json).
