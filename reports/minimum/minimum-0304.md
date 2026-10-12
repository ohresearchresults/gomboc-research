# minimum-0304

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# POSITIVE_MARKED_DENSITY_PARALLEL_CAP_EXCLUSION_AND_JOINT_CURVATURE_GATE_V1

## 1. Findings and exact scope

I obtain one complete remaining geometric exclusion and a stronger, finite-dimensional test for the genuinely coupled remaining curvature mechanism.

**Complete exclusion.** Suppose the density-zero edge is parallel to the marked edge and is the entire upper graph in coordinates adapted to the distinguished nonnormal test. The actual directional ratio satisfies **R<1**, without any stationarity assumption and for an arbitrary convex lower graph. In particular, this excludes every supercritical one-arc maximum in that complete alternative, including an opposite corner that is not on the stationary parabola. The lower graph need not be polygonal, quadratic, symmetric, or have a bounded number of pieces.

This is a directional theorem in the distinguished test coordinates, not a full-matrix theorem for all tests on a fixed body. Parallel marked and zero-density lines alone are insufficient for its geometric hypothesis: a positive-density upper connector preceding the zero edge can prevent the zero edge from being the entire upper graph. That alternative remains open here.

**Full release of every off-marked zero edge.** At a conic maximum with strictly positive marked density, every zero edge has positive corner angles at its two endpoints. Consequently it admits a compact convex extension across the whole zero edge, with the original body recovered by the original density halfspace. The full boundary Gram penalty G_Gamma, previously proved for a chord between two arcs, therefore applies to every off-marked zero edge in the remaining one-arc problem as well.

**Complete joint second-variation reduction.** Simultaneously varying the affine density, arbitrary compactly supported displacements of all free curved arcs, and the actually recentered optimizing test reduces exactly to a six-dimensional quadratic-form test. The reduction does not restrict the arc displacement to a quadratic polynomial. It includes a cubic mode that appears when the optimizing test tilts the stationary parabola's axis. Nonpositivity of this six-dimensional form is equivalent to nonpositivity of all second variations in this specified infinite-dimensional family. A strict failure produces a genuine uniformly filled convex-body ascent. Passing the test is not sufficient for a local or global maximum.

I have not excluded every positive-marked-density one-arc maximum, nor the complete same-side two-arc class. I have no actual supercritical counterexample. No universal three-halves, general weaker-leverage, equilibrium, E17, or minimum conclusion is claimed.

## 2. Authority and input limitation

The immediate literal parent is `[internal-source-reference]-`, SHA-256 `c8de49bdf65a55f24866cb2169b19b3484fa8d4fbd90d14c272d638f69ee6128`. Its marked-zero closure, sharp sequences, isolated marked-zero ascent and same-side chord release are retained with their reported scopes. In particular, its zero-length opposite-wing chart is not reclassified as every one-arc body.

The retained continuation context contains the reading of the current journal through lines244–1955, including the literal parent. In this execution, attempted reads of journal lines1–243 and the two newly supplied tilted-facet capsule files did not expose readable tool content to me. I therefore cannot certify a complete current-input reading or a new executed source run. This is a delivery limitation, not a claim that those files or their complete sources are absent. The supplied manifest identifies them as:

```
research-journal.md:392911 bytes
1a785d11cdd2bfa71a1635aea0c91a5a7c7563ff933a6140ac4af03e5e7bde0f
Recovery capsule part 1 of 2 - TILTED_WHOLE_FACET_AND_WEIGHTED_LINE_REACTIONS_V1.md:12004 bytes
8a20c5640edc147e4938916f7777b60ea88900043a675af64950b863d722e9fd
Recovery capsule part 2 of 2 - MARKED_FACET_VARIATION_COMPLETE_EXECUTABLE_V1.md:11336 bytes
3c3a1548d1643bb82eff6d5d47f161acda3da2dd61195e07e6fc565008b6bcb2
```

No new argument below relies on an uninspected detail of those two tilt files. The required clipping, conic, convex-height and adapted-test premises are already present in the unchanged supplied context. The exact two-mean reduction and actual planar conventions remain those of `minimum-0290`; the new theorems do not repeat or modify that reduction. fileciteturn11file0L24-L27

## 3. Actual conventions

In affine coordinates(t,Y), let K be a compact full-dimensional convex planar support, t>=0, with genuine whole marked edge e={t=0}. Let ell>=0 be affine and not identically zero. All bulk integrals below are over K with ordinary planar area unless an ell factor is written. Put

```
V=int_K ell,                 J=int_K t ell,              m=J/V,
int_K ell Y=0,               I=int_K ell Y²,
Bj=int_e ell Y^j d_sigma,    eta=B1/B2,
R=J B2/(V I),                alpha=J B0/V².
```

The actual uniformly filled lift is

```
P={(t,Y,z):(t,Y) in K, 2|z|<=ell(t,Y)}.
```

Its volume is V and its centroid is the ell-weighted planar centroid together with z-coordinate0. Actual recentering always means recentering under the new uniform volume law. Replacing t by t/m retains the second mean equality E(t/m)=1 and does not change R.

At a nonnormal self-consistent strong maximum the free arcs lie on

```
f(Y)=m+A Y²+2m eta Y,         A=J/I>0,
Phi(t,Y)=(t-f(Y))/J.
```

At R>3/2, f has strictly positive minimum. Off-marked extreme points satisfy Phi>=0. Positive-density straight edges must meet a marked endpoint, and the remaining curved boundary is made from arcs of this same parabola. These are imported conic facts, not a new finite-vertex localization. fileciteturn11file0L56-L62

At a full joint maximum, actual affine clipping gives

```
nu(psi)=int_K Phi psi + int_e Y² psi/B2 =0
```

for every affine psi, including density-zero cases. The derivative bulk integrals here are unweighted. fileciteturn11file0L88-L94

## 4. Complete parallel-ceiling directional theorem

### Theorem 1

Let H>0, let [a,b] be a nondegenerate compact interval, and let L:[a,b]->[0,H] be continuous and convex. Suppose its zero set is a positive-length interval C. Define

```
K={(t,r):a<=r<=b, L(r)<=t<=H},
ell(t,r)=H-t,
P={(t,r,z):(t,r) in K, 2|z|<=H-t}.
```

The marked facet is the ENTIRE support face t=0, so its r-projection is exactly C. Let mu be the actual ell-weighted r-mean and let Y=c(r-mu), c!=0. Then

```
R=m int_e ell Y² / int_K ell Y² <1.
```

The assertion includes arbitrary knots, curved pieces and nonsmooth convex floors. It allows an endpoint of the upper zero edge to lie strictly above the trial or stationary parabola. It requires no reflection symmetry and imposes no independent slice moments.

### Proof

Write q(r)=H-L(r). It is nonnegative and concave, and q=H on C. Set

```
Q2=int_a^b q² dr,             Q3=int_a^b q³ dr.
```

Direct integration through each actual t-fibre gives

```
V=Q2/2,
J=H Q2/2-Q3/3,
m=H-(2/3)(Q3/Q2).
```

I first prove, with the strictness needed here,

```
Q3/Q2 >3H/4.                                      (4.1)
```

Let W(s) be the length of {r:q(r)>=s}, 0<=s<=H. Concavity of q implies

```
(1-theta){q>=s}+theta{q>=u}
    subset {q>=(1-theta)s+theta u}.
```

Since these superlevel sets are intervals, their lengths show that W is concave. Moreover W(H)=length(C)>0. For 0<=s<u<H, concavity with the endpoint H yields

```
W(u)/(H-u) > W(s)/(H-s).
```

Thus g(s)=W(s)/(H-s) is strictly increasing. Under the positive reference weight s(H-s)ds on(0,H), the weighted mean of s is H/2. The covariance of the strictly increasing functions s and g(s) is strictly positive; this follows directly by integrating

```
(s-u)(g(s)-g(u))>0
```

over two distinct interior points with the product reference measure. Consequently

```
[int_0^H s² W(s)ds]/[int_0^H s W(s)ds] > H/2.
```

Layer-cake integration gives Q3=3 int s²W and Q2=2 int sW, proving(4.1). In particular,

```
H/3 <= m < H/2.                                   (4.2)
```

On the whole marked interval C, q=H and ell(0,r)=H. Therefore, for the ACTUALLY centered Y,

```
B2=H int_C Y²dr,
I=(1/2)int_a^b q²Y²dr >= (H²/2)int_C Y²dr.
```

The marked interval has positive length and Y is nonconstant, so the last integral is positive. Combining this with(4.2),

```
R=m B2/I <= 2m/H <1.
```

Both means are actual: int_K ell Y=0 by the definition of mu and E(t/m)=1 by the displayed fibre integral. No facet has been recentered at its own mean. ∎

### Consequence for the assigned mechanism

In the coordinates of the distinguished maximizing test, suppose an off-marked density-zero edge is parallel to e and forms the entire upper graph of K. Affine scaling makes ell=H-t. The remaining lower graph is convex and nonnegative, with its zero set precisely the marked edge. Theorem1 then contradicts R>3/2, indeed R>=1.

This is a complete stationary-mechanism exclusion in that geometric alternative. It is not the old opposite-wing argument: it uses neither two arcs nor a conic equality at the opposite corner, and it proves an unconditional directional inequality for every floor in the class.

A parallel zero edge preceded in the upper graph by a positive-density connector is NOT included. Nor does this prove a full-matrix inequality for all affine tests on every fixed body in the displayed class. Changing the distinguished test can change which boundary is its upper graph. These restrictions are essential.

## 5. Exact actual one-arc control with positive marked density

The following rational-data curved body illustrates Theorem1 without incident marked density zeros:

```
H=3,       -2<=r<=3,       ell=3-t,
L(r)=-3(r+1)                    on[-2,-1],
L(r)=0                          on[-1,1],
L(r)=r-1                        on[1,2],
L(r)=r²-3r+3                    on[2,3],
P={L(r)<=t<=3, 2|z|<=3-t}.
```

The lower slopes are -3,0,1 and2r-3; they are nondecreasing, including the tangent join at r=2. The whole marked facet is the rectangle

```
t=0, -1<=r<=1, -3/2<=z<=3/2.
```

The zero-density upper edge t=3 is disjoint from it. The parabolic piece has positive minimum3/4, but it is NOT asserted to be the body's self-consistent stationary parabola. This is a nonstationary control, not an extremal candidate or a polytope.

With q=3-L, direct polynomial integration gives

```
int q²=871/30,          int q³=11159/140,        int q⁴=141703/630,
int r q²=553/60,        int r²q²=3494/105,       int r q³=5813/280.
```

Its actual moments, in coordinate order(t,r,z), are

```
V=871/60,
g=(7132/6097,553/1742,0),
Sigma=
[[116823505/223040454,553902/5310487,0],
 [553902/5310487,22205529/21241948,0],
 [0,0,141703/438984]],

T_marked=
[[50865424/37173409,1971998/5310487,0],
 [1971998/5310487,3951991/9103692,0],
 [0,0,3/4]],
alpha=2567520/5310487.
```

The marked-facet centroid relative to the actual volume centroid is(-7132/6097,-553/1742,0). Its pole is(-6097/7132,0,0), and T_marked times that pole is exactly that relative facet centroid.

For the actual centered test Y=r-553/1742,

```
R=855840*3951991/(758641*22205529)<1.
```

The displayed matrices also give a strictly positive full marked three-halves gap for this particular control. For example, exact rational interval comparisons give

```
Gtt>1/10,       Grr>4/3,       |Gtr|<1/40,       Gzz>1/10,
G=(3/2)Sigma-alpha T_marked,
```

which certify positive definiteness. This control check is not promoted to a full-matrix theorem for Theorem1's arbitrary floors.

There are five positive-area maximal flat support faces: the marked rectangle, the two straight lower sides and the two height-graph faces. The latter have curved boundaries. The remaining side is curved, so no finite V/E/F or equilibrium census is assigned. The standalone source below reconstructs all five whole-flat-face moments independently.

## 6. Every off-marked conic zero edge admits full release

### Lemma 2 — convex carrier across an angular zero edge

Let K be a compact convex planar body, ell>=0 affine on K, and let Gamma=K intersect{ell=0} be a positive-length edge disjoint from the whole marked edge. Suppose the boundary has a positive corner angle at each endpoint of Gamma. Then there is a compact convex Q such that

```
K=Q intersect{ell>=0},
Q intersect{t=0}=e,
```

and every relative interior point of Gamma is an interior point of Q.

**Proof.** Choose a point q just outside the relative interior of Gamma, in the negative-ell halfplane. The positive corner angles imply that, for sufficiently small displacement, the two tangent contacts from q to K are precisely the endpoints of Gamma. Therefore

```
Q=conv(K,q)=K union conv(Gamma,q)
```

is a convex extension only across Gamma, and intersection with ell>=0 recovers K exactly. Since min_Gamma t>0, q may be chosen with positive t and the added triangle may be kept away from t=0. Thus the whole marked edge is unchanged. ∎

For a concrete rational or algebraic conic candidate, this is reconstructible: take the midpoint of Gamma plus2^(-N) times an outward normal, increasing N until the two adjacent tangent halfplanes and the remaining essential supporting lines/arcs contain q on their permitted side. Positive endpoint angles and compactness ensure termination. The tests are affine or quadratic inequalities in the conic chart.

### Why the angle hypothesis holds at every remaining conic maximum

A zero edge meeting another straight piece has a positive angle because it is a genuine maximal edge. Suppose instead that it joined a free parabolic arc tangentially. On that tangent line, if the tangency has test coordinate c,

```
J Phi=-A(Y-c)².
```

The other endpoint of a positive-length zero edge would then have Phi<0. It is an off-marked extreme point, contradicting the accepted cap sign Phi>=0. A vertical zero edge cannot be tangent to the graph t=f(Y). Thus every off-marked zero edge at a conic maximum has the two positive angles required by Lemma2.

This argument uses actual support signs and the same self-consistent parabola; it does not extend the chord identity to an independently chosen trial curve.

### Full second-order correction for both signs

Fix Q as in Lemma2 and any affine psi. Use the actual uniformly filled family

```
P_s={(x,z):x in Q, 2|z|<=ell(x)+s psi(x)},
K_s=Q intersect{ell+s psi>=0}.
```

For a continuous raw test a(x), coarea through Gamma gives, for BOTH signs of small s,

```
int_Q a(ell+s psi)_+
 =int_K a(ell+s psi)
  +s²/(2|grad ell|) int_Gamma a psi² ds +o(s²).       (6.1)
```

The positive and negative strips are both available inside Q. On almost every interior normal fibre, the scalar positive-part integral has exactly the quadratic correction psi²/2. The added triangle has vanishing width only at the endpoints; the bounded strip estimate and dominated convergence make their contribution o(s²). No uniform cubic remainder is needed.

Because min_e ell>0 and Q agrees with K near e, there is no marked density-zero endpoint term in this class. This is a proved exclusion of that term's geometric premise, not a deletion of a nonzero correction. The actual recentering and normalization E(t/m_s)=1 are performed after the deformation.

Consequently the full boundary quadratic form is

```
G_Gamma(psi)=int_Gamma Phi psi² ds/|grad ell|,
```

for each sign. Phi is strictly positive in the relative interior of Gamma: its endpoint values are nonnegative, and its restriction is strictly concave when Y varies; if Y is constant, it is nonconstant affine in t. Therefore G_Gamma is positive definite on the two-dimensional affine-density quotient by scaling ell.

The full adapted-test gate is accordingly

```
H_form(psi)+2Kpsi²/gamma+G_Gamma(psi)<=0,             (6.2)
```

not merely the former averaged condition with G_Gamma/2. The parent's release proof supplied this for a chord between two arcs. Lemma2 extends it to every remaining off-marked conic zero edge, including those with an endpoint strictly above f.

## 7. Simultaneous density, free-curvature and test variation

This section gives a complete second-order reduction for a larger family than independent density/test or fixed-test curvature checks.

Assume a self-consistent nonnormal stationary configuration with R>3/2, min_e ell>0, and at least one positive-length free arc. Let Acal be the union of its free arc intervals in the Y-coordinate. On those arcs t=f(Y). The density ell(f(Y),Y) is positive almost everywhere. Isolated density zeros can be avoided by compact supports and do not affect the Gram matrix.

The adapted centered test and spectral gap are

```
Z=t-m+m eta Y,
D_Z=int_K ell Z²,           C_Z=int_e ell Z²,
gamma=D_Z/I-C_Z/B2>0,
B_Z=int_e ell Z=-m(B0-B1²/B2).
```

The positivity of gamma is the accepted consequence of actual test stationarity and the strict normal spectral gap, not an extra numerical hypothesis. Both Y and Z are centered and orthogonal in the original volume and facet quadratic forms. fileciteturn12file0L17-L23

Let psi be an affine density variation and let h be any twice continuously differentiable function compactly supported inside the free arcs, away from their joins and any density-zero points. Move each lower arc by

```
f_s(Y)=f(Y)+s h(Y)
```

while using ell_s=ell+s psi. At a zero edge use the released carrier from Section6. For sufficiently small signs of s the lower graph remains convex, the whole marked edge is unchanged and the lift is a genuine convex uniform body. The actual centered tests are Y_s=Y-E_sY and Z_s=Z-E_sZ.

Define the four arc moments of the displacement

```
w_i=int_Acal ell(f(Y),Y) h(Y) Y^i dY,        i=0,1,2,3.
```

Define the actual unweighted density-derivative moments

```
a0=int_K psi,       at=int_K t psi,
a1=int_K Y psi,     a2=int_K Y² psi,
az=int_K Z psi,    ayz=int_K YZ psi,
E1=int_e Y psi,     E2=int_e Y² psi,    EYZ=int_e YZ psi.
```

The total first raw bulk variation is psi dx minus ell h on the moving lower arcs. Since

```
f=m+A Y²+2m eta Y,
Z|arc=A Y²+3m eta Y,
```

its normalized first moments are exactly

```
u=(a0-w0)/V,
p=(a1-w1)/V,
q=(a2-w2)/I,
j=(at-m w0-A w2-2m eta w1)/J,
d=(E2-2B1 p)/B2,
pz=(az-A w2-3m eta w1)/V,
c_yz=ayz-A w3-3m eta w2.
```

Here u is a normalized volume derivative, not a support coordinate. The first logarithmic derivative is j-u-q+d. It vanishes for every such(psi,h), because affine density stationarity kills the psi part and Phi=0 kills every arc part.

### Exact nonlinear moment Hessian

For these first derivatives put

```
H_raw=-j²+u²+q²-d²+4 eta u p
      +2p²(B0/B2+V/I)-4p E1/B2,                    (7.1)

K_total=EYZ/B2-p B_Z/B2-pz B1/B2-c_yz/I.             (7.2)
```

Both test means occur in(7.2). Neither can be omitted.

The complete second logarithmic derivative, after choosing the optimal first-order test tilt

```
Y_s+s(K_total/gamma)Z_s,
```

is

```
H_raw+2K_total²/gamma+G_Gamma(psi)
       -(1/J)int_Acal ell h² dY.                    (7.3)
```

If the density has no zero edge, set G_Gamma=0. An isolated off-marked density-zero point contributes only o(s²), as in the literal clipping theorem.

### Derivation of the local terms

For a raw bulk test a(t,Y), differentiating the lower limit twice gives

```
-int_Acal [(ell a)_t h²+2psi a h]dY.
```

The first differential of log R with respect to raw mass is Phi. At the stationary arc, Phi=0 and Phi_t=1/J. Thus all local density/shape cross terms cancel and the remaining local term is precisely

```
-(1/J)int_Acal ell h²dY.
```

The zero-edge contribution is(6.1). The rest is the ordinary Hessian of the moment functional. To see(7.1) directly, use the formal linear raw paths

```
V_s=V(1+s u),    J_s=J(1+s j),
c_s=s p/(1+s u),
I_s=I(1+s q)-s² V p²/(1+s u),
B2_s=B2+sE2-2c_s(B1+sE1)+c_s²(B0+sE0).
```

Twice differentiating log[J_s B2_s/(V_s I_s)] gives(7.1). This formal calculation only computes the nonlinear Taylor coefficient. The local terms above supply the actual moving-support and clipping corrections. The formal path is not asserted to be a signed-density realization.

The mixed density-or-shape/test derivative is2K_total, while the pure test second derivative is-2gamma. Completing the square yields the term2K_total²/gamma in(7.3).

## 8. Exact six-dimensional criterion for all these second variations

Choose any two independent affine density directions psi_1,psi_2 after removing scaling:

```
int_K psi_i=0.
```

A deterministic construction starts with1,t,Y, replaces each a by a-(int_K a/V)ell, and takes the first two coefficient-independent results. Their kernel before this quotient is exactly the scaling direction ell.

Let

```
G_ij=int_Acal ell(f(Y),Y)Y^(i+j)dY,      0<=i,j<=3.
```

G is positive definite: a nonzero cubic polynomial cannot vanish on a nonempty interval of positive arc density. For fixed w=(w0,w1,w2,w3), Hilbert-space projection gives

```
inf int_Acal ell h²dY = w^T G^-1 w,                 (8.1)
```

where the infimum over compactly supported admissible h equals the L² minimum. The unconstrained minimizer is the cubic polynomial with coefficient vector G^-1w. Smooth compact cutoffs away from joins and isolated zero-density points approximate it in L². Convexity is not lost: each fixed cutoff has finite second derivative, so a sufficiently small deformation parameter preserves f''=2A>0.

Write psi=theta1 psi_1+theta2 psi_2 and use the corresponding actual density moments in(7.1)–(7.2). Define the homogeneous quadratic form on six real coordinates(theta,w)

```
Q_joint(theta,w)
 =G_Gamma(psi)-w^T G^-1w/J
  +H_raw(theta,w)+2K_total(theta,w)²/gamma.           (8.2)
```

### Theorem 3

At the stated stationary configuration, the following are equivalent:

1. Every simultaneous affine-density, compact free-arc, and recentered horizontal-test variation described above has nonpositive second logarithmic derivative.
2. The six-by-six symmetric matrix of Q_joint is negative semidefinite.

A strict positive direction of Q_joint gives an actual strict ascent, not a formal-moment counterexample.

**Proof.** For every admissible h, its four moments satisfy(8.1), so(7.3) is bounded above by(8.2). Conversely, a strict positive direction of(8.2) remains positive for sufficiently accurate smooth cutoffs of its minimizing cubic. The corresponding actual convex support/density path has zero first derivative and positive second derivative, and its actually recentered tilted test gives a strict increase for sufficiently small nonzero s. The whole marked edge remains fixed and both actual mean normalizations remain exact. ∎

For exact acceptance, negative semidefiniteness means that all principal minors of minus this six-by-six matrix are nonnegative; checking only leading minors would not suffice. All inputs must be reconstructed from the same actual candidate. This is an arithmetic stability test, not a realization theorem for independently chosen moments.

This theorem is necessary and sufficient for nonpositivity of this complete family of second variations. It is NOT sufficient for local maximality, especially when the quadratic form has a kernel, and does not replace the global convex-height cone.

### A simpler new cubic obstruction

The pure-arc specialization has psi=0. Its nonlinear quadratic form in w is

```
F(w)=-2w0w2/(V I)-4eta w1w2/(V I)
     +2(B0/B2+V/I-4eta²)w1²/V²,

K_arc=m(4eta²-B0/B2)w1/V+4m eta w2/I+A w3/I.
```

Thus the exact four-dimensional pure-arc criterion is

```
-w^T G^-1w/J+F(w)+2K_arc²/gamma <=0 for all w.       (8.3)
```

Let G2 be the upper-left three-by-three block of G and let b=(G03,G13,G23)^T. Define the positive cubic residual norm

```
C3=G33-b^T G2^-1b.
```

Taking h to be the residual of Y³ after projection onto1,Y,Y² gives w0=w1=w2=0 and w3=C3. Therefore every surviving maximum must obey

```
C3 <= gamma I²/(2J A²) = gamma I⁴/(2J³).            (8.4)
```

A strict reverse inequality constructs the ascent by the cutoff argument. This direction is absent from a test that only moves the three coefficients of the parabola while keeping its axis fixed. When the optimizing affine test changes, its value on the old arc is quadratic in Y; differentiating the parabola with respect to that test introduces a cubic term. This is the geometric source of the extra mode, rather than an imposed vertex or knot bound.

I have not produced an actual self-consistent candidate that separates the old gates from(8.2), and do not claim that every remaining candidate violates it. Its completeness is for the specified second-order variation family.

## 9. Exact data needed for continuation

The finite criterion uses only the following coupled actual integrals:

```
V,J,I,B0,B1,B2 and gamma;
for each of two affine density basis functions:
  int psi, int tpsi, int Ypsi, int Y²psi, int Zpsi, int YZpsi,
  int_e Ypsi, int_e Y²psi, int_e YZpsi;
arc Gram moments int_Acal ell(f(Y),Y)Y^k dY, 0<=k<=6;
zero-edge Gram int_Gamma Phi psi_i psi_j ds/|grad ell|.
```

For the finite conic supports these are exact polynomial integrals over intervals, straight edges and the actual planar pieces. The arc density is quadratic in Y. If ell_t!=0, the zero-edge coarea factor is dY/|ell_t|; if ell_t=0, parameterize the zero edge by t instead. No irrational arc length integral is required.

The useful remaining one-arc alternatives are now more precise: positive marked density with a nonparallel off-marked zero edge; a parallel zero edge that is not the whole upper graph; strictly positive density; and isolated off-marked zero contacts. Same-side two-arc candidates use the same joint criterion with the arc Gram matrix summed over both arcs and the full released zero-edge Gram. None of these is declared empty here.

The complete incident-zero families and isolated marked-zero cases remain closed by the literal parent and are not reassigned. The whole marked-facet translation and tilt conditions from the supplied journal remain separate first-order obligations. A trial parabola, a finite list of convex-height tests, or a passing six-dimensional quadratic form is not a supercritical actual body.

## 10. Recovery source and verification status

The new findings above are analytical. The literal control geometry, raw integrals and matrices in Section5 are a complete recovery capsule; no saved file is required. The source below independently checks those data, all five whole-flat-face moments, the generic moment-Hessian identity, and supplies the exact six-dimensional matrix assembler.

**No current-run completion or checksum is claimed.** Readable execution results were not available in this continuation. The source is therefore supplied as an unobserved verifier, not as an executed finite certificate. It targets the already used CPython3.13.5 / SymPy1.14.0 stack, with assertions enabled. It has no external input files, optimizer, seed, omitted helper or saved coefficient array. It prints hashes of its source and generated report when run; I do not invent expected hashes that I could not observe.

Save as `positive_marked_curvature_gate.py` and run:

```
python -B positive_marked_curvature_gate.py > positive_marked_curvature_gate.log
```

Expected terminal markers, specified by the source rather than reported as observed, are:

```
ACTUAL_PARALLEL_CAP_CONTROL_AND_FIVE_WHOLE_FLAT_FACES_PASS
GENERIC_MOMENT_AND_CUBIC_CURVATURE_IDENTITIES_PASS
POSITIVE_MARKED_CURVATURE_GATE_RECOVERY_PASS
```

```python
"""POSITIVE_MARKED_DENSITY_PARALLEL_CAP_AND_CURVATURE_GATE_V1.
Target: CPython 3.13.5 / SymPy 1.14.0, assertions enabled.
Standalone verifier for the analytical identities and literal curved control.
No current-worker execution receipt is asserted in the accompanying handoff.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as S

Q = S.Rational
t, y, s = S.symbols('t y s', real=True)


def simp(x):
    return S.factor(S.cancel(x))


def zero(x):
    assert simp(x) == 0, simp(x)


def integ(f, x, a, b):
    return simp(sum(c * (b**(m[0]+1)-a**(m[0]+1)) / S.Integer(m[0]+1)
                    for m, c in S.Poly(S.expand(f), x).terms()))


def log_second(f):
    f0 = f.subs(s, 0)
    return simp(S.diff(f, s, 2).subs(s, 0)/f0
                - (S.diff(f, s).subs(s, 0)/f0)**2)


def formal_identities():
    V, J, I, B0, B1, B2 = S.symbols('V J I B0 B1 B2', positive=True)
    u, jj, q, p, E0, E1, E2 = S.symbols('u jj q p E0 E1 E2', real=True)
    eta = B1/B2
    vs = V*(1+s*u)
    js = J*(1+s*jj)
    cs = s*p/(1+s*u)
    ii = I*(1+s*q)-s*s*V*p*p/(1+s*u)
    bb = B2+s*E2-2*cs*(B1+s*E1)+cs*cs*(B0+s*E0)
    d = (E2-2*B1*p)/B2
    H = (-jj*jj+u*u+q*q-d*d+4*eta*u*p
         +2*p*p*(B0/B2+V/I)-4*p*E1/B2)
    zero(log_second(js*bb/(vs*ii))-H)
    w0, w1, w2, w3 = S.symbols('w0 w1 w2 w3', real=True)
    m, A = J/V, J/I
    us = -w0/V
    ps = -w1/V
    qs = -w2/I
    jjs = us+qs+2*eta*ps
    F = (-2*w0*w2/(V*I)-4*eta*w1*w2/(V*I)
         +2*(B0/B2+V/I-4*eta*eta)*w1*w1/(V*V))
    zero(H.subs({u:us, p:ps, q:qs, jj:jjs, E1:0, E2:0})-F)
    BZ = -m*(B0-B1*B1/B2)
    pz = -(A*w2+3*m*eta*w1)/V
    K = -ps*BZ/B2-pz*B1/B2+(A*w3+3*m*eta*w2)/I
    expected = (m*(4*eta*eta-B0/B2)*w1/V
                +4*m*eta*w2/I+A*w3/I)
    zero(K-expected)
    return {'raw_moment_Hessian':H, 'pure_arc_F':F, 'pure_arc_K':expected}


def assemble_joint_quadratic_form(V, J, I, B0, B1, B2, gamma,
                                  arc_gram, zero_edge_gram, density_rows):
    """Arithmetic assembler, NOT a realization or stationarity theorem.

    Inputs must come from ONE actual self-consistent stationary candidate.
    arc_gram[i,j] = int_arc ell*Y**(i+j), i,j=0..3.
    zero_edge_gram[i,j] = int_Gamma Phi*psi_i*psi_j/|grad ell|.
    Use the FULL release Gram, or zero when no zero edge exists.
    Each of two density_rows is:
    [int psi, int tpsi, int Ypsi, int Y2psi, int Zpsi, int YZpsi,
     int_edge Ypsi, int_edge Y2psi, int_edge YZpsi].
    Both density directions have int psi=0 and annihilate nu.
    The analytical hypotheses, including min_edge ell>0 and the actual
    self-consistent arcs, are not established by supplying arbitrary arrays.
    """
    V, J, I, B0, B1, B2, gamma = map(S.sympify, (V,J,I,B0,B1,B2,gamma))
    assert all(a > 0 for a in (V,J,I,B0,B2,gamma))
    G = S.Matrix(arc_gram)
    GG = S.Matrix(zero_edge_gram)
    D = S.Matrix(density_rows)
    assert G.shape == (4,4) and GG.shape == (2,2) and D.shape == (2,9)
    assert G == G.T and GG == GG.T
    assert all(simp(G[:i,:i].det()) > 0 for i in range(1,5))
    eta, m, A = B1/B2, J/V, J/I
    for i in range(2):
        zero(D[i,0])
        zero(D[i,1]/J-D[i,0]/V-D[i,3]/I
             -2*eta*D[i,2]/V+D[i,7]/B2)
    theta = S.Matrix(S.symbols('theta0:2', real=True))
    w = S.Matrix(S.symbols('w0:4', real=True))
    raw = theta.T*D
    a0, at, a1, a2, az, ayz, E1, E2, EYZ = list(raw)
    u = (a0-w[0])/V
    p = (a1-w[1])/V
    q = (a2-w[2])/I
    jj = (at-m*w[0]-A*w[2]-2*m*eta*w[1])/J
    d = (E2-2*B1*p)/B2
    pz = (az-A*w[2]-3*m*eta*w[1])/V
    cyz = ayz-A*w[3]-3*m*eta*w[2]
    BZ = -m*(B0-B1*B1/B2)
    K = EYZ/B2-p*BZ/B2-pz*B1/B2-cyz/I
    H = (-jj*jj+u*u+q*q-d*d+4*eta*u*p
         +2*p*p*(B0/B2+V/I)-4*p*E1/B2)
    zero(jj-u-q+d)
    form = ((theta.T*GG*theta)[0]-(w.T*G.inv()*w)[0]/J
            +H+2*K*K/gamma)
    coords = list(theta)+list(w)
    matrix = (S.hessian(form, coords)/2).applyfunc(simp)
    zero(form-(S.Matrix(coords).T*matrix*S.Matrix(coords))[0])
    return matrix


def all_principal_minors_nonnegative(matrix):
    """For an exact symmetric matrix; leading minors alone are insufficient."""
    M = S.Matrix(matrix)
    assert M == M.T
    for size in range(1, M.rows+1):
        for ids in combinations(range(M.rows), size):
            if not bool(simp(M.extract(ids, ids).det()) >= 0):
                return False
    return True


def actual_control():
    ell = 3-t
    pieces = [(-2,-1,-3*(y+1)), (-1,1,S.S.Zero),
              (1,2,y-1), (2,3,y*y-3*y+3)]
    def bulk(f):
        return simp(sum(integ(integ(f,t,L,3),y,a,b) for a,b,L in pieces))
    V = bulk(ell)
    g = S.Matrix([bulk(t*ell),bulk(y*ell),0])/V
    raw2 = S.Matrix([[bulk(t*t*ell),bulk(t*y*ell),0],
                     [bulk(t*y*ell),bulk(y*y*ell),0],
                     [0,0,bulk(ell**3)/12]])
    cov = (raw2/V-g*g.T).applyfunc(simp)
    expected_cov = S.Matrix([
        [Q(116823505,223040454),Q(553902,5310487),0],
        [Q(553902,5310487),Q(22205529,21241948),0],
        [0,0,Q(141703,438984)]])
    assert V == Q(871,60)
    assert g == S.Matrix([Q(7132,6097),Q(553,1742),0])
    assert cov == expected_cov
    assert all(cov[:i,:i].det()>0 for i in (1,2,3))
    floors = [(-2,-1,-3*(y+1)),(-1,1,S.S.Zero),
              (1,2,y-1),(2,3,y*y-3*y+3)]
    qmom = {}
    for power,ypower in [(2,0),(3,0),(4,0),(2,1),(2,2),(3,1)]:
        value = sum(integ(y**ypower*(3-L)**power,y,a,b) for a,b,L in floors)
        qmom[str((power,ypower))] = simp(value)
    assert list(qmom.values()) == [Q(871,30),Q(11159,140),Q(141703,630),
                                   Q(553,60),Q(3494,105),Q(5813,280)]
    faces = []
    def lower_face(name,L,a,b):
        density = ell.subs(t,L)
        W = integ(density,y,a,b)
        X = S.Matrix([L-g[0],y-g[1],0])
        c = X.applyfunc(lambda z:integ(density*z,y,a,b)/W)
        T = (X*X.T).applyfunc(lambda z:integ(density*z,y,a,b)/W)
        T[2,2] = integ(density**3,y,a,b)/(12*W)
        slope = S.diff(L,y)
        n = S.Matrix([-1,slope,0])
        support = -L.subs(y,0)
        distance = simp(support-n.dot(g))
        return {'name':name,'alpha':simp(distance*W/V),
                'c':c.applyfunc(simp),'T':T.applyfunc(simp),'pole':n/distance}
    faces.append(lower_face('whole marked rectangle',S.S.Zero,-1,1))
    faces.append(lower_face('whole left straight side',-3*(y+1),-2,-1))
    faces.append(lower_face('whole right straight side',y-1,1,2))
    area = bulk(S.S.One)
    for sign in (-1,1):
        X = S.Matrix([t-g[0],y-g[1],sign*ell/2])
        c = X.applyfunc(lambda z:bulk(z)/area)
        T = (X*X.T).applyfunc(lambda z:bulk(z)/area)
        n = S.Matrix([1,0,2*sign])
        distance = 3-g[0]
        faces.append({'name':'whole graph '+str(sign),
                      'alpha':simp(distance*area/(2*V)),
                      'c':c,'T':T,'pole':n/distance})
    for face in faces:
        assert face['alpha']>0
        assert (face['T']*face['pole']-face['c']).applyfunc(simp)==S.zeros(3,1)
        zero(face['pole'].dot(face['c'])-1)
    F = faces[0]
    expected_T = S.Matrix([
        [Q(50865424,37173409),Q(1971998,5310487),0],
        [Q(1971998,5310487),Q(3951991,9103692),0],
        [0,0,Q(3,4)]])
    assert F['T']==expected_T and F['alpha']==Q(2567520,5310487)
    gap = Q(3,2)*cov-F['alpha']*F['T']
    assert gap[0,0]>Q(1,10) and gap[1,1]>Q(4,3)
    assert abs(gap[0,1])<Q(1,40) and gap[2,2]>Q(1,10)
    assert all(gap[:i,:i].det()>0 for i in (1,2,3))
    Y = y-g[1]
    zero(bulk(ell*Y))
    zero(bulk(ell*t/g[0])/V-1)
    ratio = simp(g[0]*integ(3*Y*Y,y,-1,1)/bulk(ell*Y*Y))
    assert ratio == Q(855840*3951991,758641*22205529) < 1
    return {'density':ell,'pieces':pieces,'upper':3,'volume':V,
            'centroid':g,'Sigma':cov,'q_moments':qmom,
            'whole_flat_faces':faces,'actual_centered_test':Y,'R':ratio,
            'scope':'Curved actual uniform body; not a stationary candidate or polytope.'}


def encode(x):
    if isinstance(x,S.MatrixBase):
        return [[encode(v) for v in row] for row in x.tolist()]
    if isinstance(x,S.Basic):
        return str(x)
    if isinstance(x,dict):
        return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encode(v) for v in x]
    return x


def main():
    assert __debug__
    report = {'name':'POSITIVE_MARKED_DENSITY_PARALLEL_CAP_AND_CURVATURE_GATE_V1',
              'parent':'[internal-source-reference]-',
              'parent_sha256':'c8de49bdf65a55f24866cb2169b19b3484fa8d4fbd90d14c272d638f69ee6128',
              'algebra':formal_identities(),'actual_control':actual_control(),
              'scope':'Analytical subclass exclusion and complete specified second-order gate; no universal determination.'}
    data = (json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('positive_marked_curvature_gate_report.json').write_bytes(data)
    print('ACTUAL_PARALLEL_CAP_CONTROL_AND_FIVE_WHOLE_FLAT_FACES_PASS')
    print('GENERIC_MOMENT_AND_CUBIC_CURVATURE_IDENTITIES_PASS')
    source = Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('POSITIVE_MARKED_CURVATURE_GATE_RECOVERY_PASS')

if __name__ == '__main__':
    main()
```

The most useful continuation is to evaluate the full six-dimensional form on genuinely self-consistent positive-marked one-arc candidates, with any off-marked zero edge released as above. A strict positive direction is already a reconstructible actual ascent mechanism. A passing form leaves the first-order whole-facet, full convex-height and higher-order obligations intact; it must not be promoted to a counterexample or to a completed maximum.
