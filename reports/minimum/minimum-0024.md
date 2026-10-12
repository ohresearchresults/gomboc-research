# minimum-0024

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_F9_SYNTHESIS_AND_RECIPROCAL_ACTUAL_TRACE_V1

## Determination and authority

The facet lower bound is established: **every full-dimensional homogeneous convex three-polytope with exactly one strictly stable maximal facet has at least nine maximal facets**. Equivalently, every such polytope with at most eight maximal facets has at least two strictly stable facets, even when other features have degenerate equilibrium tests. The physical coefficient bound that closes the eight-facet argument is

`Lambda_ai <= c3 = max_{r>=0} 3(1+2r+3r^2)/[(1+r+r^2)(3+2r+r^2)] < 10/9 < 7/6`.

The same exact finite-vector lemma also recovers `U=1 => V>=9`. Thus a strict homogeneous `110` body has `E>=16` and `C=V+E+F-2=2E>=32`; equality requires `(V,E,F)=(9,16,9)`. This establishes a lower bound, not an exact minimum or an attaining body.

The immutable parent is `minimum-0021`, SHA-256 `5eba4891ccbcf0917f0390ff3e42f18b1fcd040b72f92a3a7fc8a18f1b2a6557`, entitled `NOVA24_WEIGHTED_CAP_7_6_AND_PHYSICAL_FLUX_V1`. I read its complete literal payload and the complete later journal text `NOVA24_ACTUAL_TRACE_CAP_F9_V1`. The latter was preserved late text, not another immutable parent. The old parent correctly left the actual 7/6 exterior open; the later trace theorem closes it. No mathematical parent/alias conflict was found. Historical catalogue counts in the decoded reports are not fresh enumerations and are unnecessary to this universal proof. The attached late theorem and literal parent are the source of the inherited proof below. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The new nine-facet work produces a further universal, genuinely coupled physical inequality,

`Lambda_ai Lambda_ia <= [Vol(conv(F_a union F_i))/Vol(P)]^2 <= 1  (a != i)`,

proved in Section 6, and an exact shared projective integral formulation for all nine-facet bodies. A separate argument excludes the complete base-stable chamber of centrally symmetric octagonal pyramids, with unrestricted positive-definite metrics. **Neither the reciprocal inequality nor the integral formulation excludes all nine-facet monostable bodies or all C32 bodies. No C32 attainer, whole-C32 exclusion, or F>=10 theorem was obtained.**

## 1. Sharp affine boundary-trace theorem

Let K be a compact, full-dimensional convex three-polytope. Let t be nonconstant affine, nonnegative on K, with `{t=0}` an actual maximal facet F. Let y be affine and nonnegative on K, with positive integral. Define

```
Z = Vol(K),
m = (1/Z) integral_K t dx > 0,
Y = integral_K y dx > 0,
B0 = (1/|grad t|) integral_F y dH^2.
```

Then `m B0/Y <= c3`. There is no aspect-ratio, simplicity, or metric bound.

### Classical input and its hypotheses

Fradelizi's author restatement of Fradelizi–Guedon, printed p.17 of arXiv:0807.0080, applies to compact convex K, upper-semicontinuous f, `s in [-infinity,1/2]`, and convex upper-semicontinuous functionals on probabilities with the weak topology. The supremum over s-concave probabilities satisfying `integral f>=0` is attained either at a Dirac mass with `f>=0`, or at an s-affine segment measure with `integral f=0`. On that segment [a,b], either `integral_[a,x] f dnu>0` for every interior x, or `integral_[x,b] f dnu>0` for every interior x. Borell's density conversion on p.3 is `gamma=s/(1-ds)` in affine support dimension d. Thus `s=1/3,d=1` gives squared nonnegative affine density. Uniform volume in dimension three is 1/3-concave. I checked both printed pages as primary-source page images. The original reference is Fradelizi–Guedon, DCG 31 (2004), 327–335, DOI 10.1007/s00454-003-2868-y. :contentReference[oaicite:2]{index=2}

Only **one** constraint is used below. The integral of y remains in the objective. We prove the requisite bound for all squared-affine needles, so the extra one-sided-integral condition can be discarded, not presumed absent from the theorem.

### The needle calculation, including zero endpoints

On `[0,1]`, write

```
ell(s)=(1-s)u+sv,   y(s)=(1-s)p+sq,
u,v,p,q>=0.
```

An identically zero density is not a probability; an identically zero y cannot give a positive objective. Otherwise normalize `u+v=p+q=1`. Direct integration gives

```
A = integral ell^2 = (u^2+uv+v^2)/3,
T = integral s ell^2 = (u^2+2uv+3v^2)/12,
W = integral y ell^2 = p(A-T)+qT,
J = p u^2 T/(A W).
```

If p or u is zero, J=0. Otherwise `W>=p(A-T)` and, putting `r=v/u`,

`J <= u^2 T/[A(A-T)] = R(r) <= c3`.

Uniformly over all normalized endpoints,

```
A>=1/4,   1/12<=T<=1/4,   1/12<=A-T<=1/4,
W>=1/12,  T/(A W)<=12.
```

For example, `12T=(u+v)^2+2v^2` and `12(A-T)=(u+v)^2+2u^2`. Both normalized affine functions take values in `[0,1]` and have slope of absolute value at most one; hence `y ell^2` is 3-Lipschitz. These estimates include a zero density or weight at either endpoint.

### The uniform thin-layer limit

Let

`B(z)=|grad t|^-1 integral_{K intersect {t=z}} y dH^2`.

This is right-continuous at zero with value B0. Indeed, translate the section planes to `{t=0}`. Compactness puts every limit point in F; segments from F to a fixed interior point give the reverse Hausdorff approximation. The sections converge to the full-dimensional polygon F, and their area integrals of affine y converge as well.

Suppose the claimed inequality fails. Choose `c3<C<mB0/Y`. For `0<epsilon<min(1/2,m/2)`, take continuous nonnegative `psi_epsilon` equal to `1/epsilon` on `[0,epsilon-epsilon^2]`, decreasing linearly to zero at epsilon, and zero thereafter. Its integral is `1-epsilon/2`. Coarea and section continuity imply

`integral_K y psi_epsilon(t) dx -> B0`.

Consequently the uniform probability mu on K has positive objective

`Phi_epsilon(mu)=integral y[psi_epsilon(t)-C/m] dmu`

for every sufficiently small epsilon. This is a continuous affine, hence convex upper-semicontinuous, functional on probabilities. Apply localization with the continuous constraint `f=t-m`; the uniform probability is feasible at equality.

A Dirac alternative has `t>=m>epsilon` and objective `-Cy/m<=0`, impossible. A constant-t segment has t=m and is likewise impossible. Orient a remaining positive-objective segment so `t=a+Ls`, `s in [0,1]`. Positivity forces `0<=a<epsilon`; its equality constraint gives

`m=a+L T/A`, and therefore `L>=m-epsilon`.

After clearing the positive density normalization and changing variables from s to t,

```
(C/m)LW
 < integral_a^(a+L) y((z-a)/L) ell((z-a)/L)^2 psi_epsilon(z) dz
 <= p u^2 + 3epsilon/(m-epsilon).
```

For the last bound, the nonzero integration interval has length at most epsilon, `psi_epsilon<=1/epsilon`, and `s<=epsilon/(m-epsilon)` there. The endpoint/Lipschitz estimates do not depend on which segment localization selected. Substitute `L=(m-a)A/T` to obtain

`C(m-epsilon)/m < J + 36epsilon/(m-epsilon) <= c3+36epsilon/(m-epsilon)`.

Let epsilon decrease to zero. This contradicts `C>c3`. In particular, no segment is incorrectly held fixed while epsilon changes, no lower bound on endpoint density is assumed, and no extra centroid constraint was inserted into the localization theorem. This completes the continuous trace proof.

### Exact value and strict rational cap

Put `D(r)=(1+r+r^2)(3+2r+r^2)`. The exact identity

```
10D(r)-27(1+2r+3r^2)
 = (r-7/15)^2[10r^2+(118/3)r+203/15]
   +(44/675)r+178/3375
```

is strictly positive for every r>=0. Thus `R(r)<10/9`. Its maximum is attained, because `R(0)=1`, `R(1/2)=132/119>1`, and R tends to zero at infinity. Hence **c3<10/9**, not merely c3<=10/9.

Moreover,

```
R'(r)=-3E(r)/D(r)^2,
E(r)=6r^5+15r^4+16r^3+6r^2-6r-1.
```

Descartes' rule and E(0)<0<E(1) give exactly one positive root r*, the unique maximizer. The replayed 100-step rational bisection proves

```
296613340109674521241811084097/633825300114114700748351602688
 < r* <
593226680219349042483622168195/1267650600228229401496703205376.
```

The decimal values `r*=0.467973335959091383778198129018...` and `c3=1.1097905767027248783781309760...` are descriptive, not proof inputs. In particular `7/6-c3>1/18`.

The independent polynomial checker also verifies, before endpoint normalization,

```
36(10AW-9pu^2T)
 = p[(v-7u/15)^2(10v^2+118uv/3+203u^2/15)
      +44u^3v/675+178u^4/3375]+360qAT.
```

It integrates in five formal variables and does not import the trace builder. The source and its independent checker are fully recoverable in Section 8.

## 2. Application to one actual coefficient matrix

Translate the ordinary uniform-volume centroid of P to zero, and write its actual maximal facets as `q_i.x<=1`. Let V be its volume and let `A_i,h_i,c_i` be the actual area, centroid-to-plane distance, and uniform-area centroid of facet i. Set

`omega_i=A_i h_i/(3V)`, `Lambda_ai=3omega_i(1-q_a.c_i)`.

Apply the trace theorem to this same body with `t=1-q_i.x`, `y=1-q_a.x`. Both are nonnegative. Actual centering gives m=1 and Y=V, while `|grad t|=1/h_i`. Therefore

`Lambda_ai=A_i h_i(1-q_a.c_i)/V <= c3 <10/9`.

This holds simultaneously in the **same** physical matrix. It does not center Q=P^polar and does not replace any area centroid with an optimized coefficient vector.

Cone integration and the divergence theorem give

```
sum omega_i=1,       sum omega_i q_i=0,
sum omega_i c_i=0,   3 sum omega_i c_i q_i^T=I,
Lambda_aa=0,         Lambda_ai>0 for a!=i,
sum_i Lambda_ai=3,   sum_i Lambda_ai q_i=-q_a.
```

Here the cone `conv(0,F_i)` has centroid `3c_i/4`. Strict off-diagonal positivity follows because c_i is in the relative interior of its actual maximal facet.

For row matrices Q,C, put `Omega=diag(omega)`, `Pi=1 omega^T`, `R=QC^T Omega`. Then

```
Pi^2=Pi, Pi R=R Pi=0, R^2=R/3, Lambda=3Pi-3R,
Lambda^2+Lambda=12Pi, omega^T Lambda=3omega^T,
sum_i Lambda_ai Lambda_ia=12omega_a.
```

The rank is four; the nonzero eigenvalues are 3,-1,-1,-1. Stationary weighted flux balances across every subset. These are identities of the real body, not realizability claims about arbitrary matrices with that spectrum.

The retained incidence bounds also have direct proofs. Coning P from a vertex minimizing `q_a.x` shows `min q_a.x>=-3`, since every positive tetrahedron has mean at most `(min q_a.x+3)/4` and the actual mean is zero. Thus every slack is in `[0,4]`. Triangulating an actual facet from a shared vertex, or using the two shared-edge vertices of a triangular facet, gives

```
Lambda_ai<=12omega_i;
Lambda_ai<=8omega_i                  if distinct F_a,F_i meet;
Lambda_ai<=4omega_i<=1               if F_i is triangular and shares an edge with F_a.
```

For the last inequality, `omega_i<=1/4` follows directly from slicing: if U(t) is volume beyond inward distance t from F_i, Brunn–Minkowski makes `U(t)^(1/3)` concave, so `U(t)<=V(1-A_i t/(3V))^3`. Its tail integral gives `h_i<=3V/(4A_i)`.

Define the optimized cap gamma_a as the minimum maximum coefficient in a nonnegative apex-excluded representation of -q_a with coefficient sum three. The physical row is feasible, so

`gamma_a<=max_i Lambda_ai<=c3<7/6`.

No matrix-square or flux identity is being asserted for independently optimized gamma rows.

## 3. Complete finite-vector proof behind the facet conclusion

The finite lemma is dimension-free: at most eight distinct nonzero vectors cannot have both a unique-root weak escape tree and an apex-excluded representation of -q_a, coefficient sum three and cap 7/6, at every apex. The exact data and both replay implementations are included below; this section gives the logical use of every certificate family.

For an arrow `i->p(i)`, put `D_i=q_i.(q_p(i)-q_i)>=0`. Distinctness makes squared norm increase strictly. Relabel parent-before-child with root 0. Put `tau=7/6`, `delta=2/3`. The capped coefficient polytope on seven non-apex entries has exactly 105 extreme rows, with two entries tau, one delta, and four zeros.

### Projection bounds

Along a depth-d path, radial contraction and concavity of log cosine give negative root projection at most `b_d |q_0|^2`, where

`b0=b1=0, b2=1/8, b3=1/4, b4=(11+5sqrt(5))/64<89/256, b5=27/64`.

To see this, append the angle from the last vector to the opposite root direction to the d edge angles. Their sum is at least pi; the product of their nonnegative cosines is at most `cos(pi/(d+1))^(d+1)`.

If at most four nodes have depth at least two, three negative parts sum to less than `(15/16)|q_0|^2`. Only a six-node chain marked at depths 3,4,5 and a fork marked at 3,4,4 need more than the individual bounds. Their integer matrices have M00=75 and respective remaining diagonals/parents

```
(128,208,352,336,192), (-1,0,1,2,3,4);
(128,208,368,176,176), (-1,0,1,2,3,3).
```

Put minus half the child diagonal at each symmetric parent entry, and add 40 at each symmetric root/marked-node entry. M/80 represents the claimed 15/16 expression minus positive shadow multipliers. The leading minors are, respectively,

```
75,5504,333632,15370240,434778112,56623104;
75,5504,333632,9116672,817229824,5266866176.
```

For at most six nodes, or at most four deep nodes, two negative parts sum to less than `K=373/500`. The only remaining pair is depths 4,5 in a six-node chain. The positive-definite form is

```
K x0^2+x0(x4+x5)-sum_(i=1..5) ell_i(x_i x_(i-1)-x_i^2),
ell=(1081814,1568749,2274907,3298981,2102980)/1000000.
```

At common denominator 2000000 its leading minors are

```
1492000,
2057811445404,
2784606944230667192,
2019854042353942830803092,
2564678406430668704815146192,
578053859419041267994547507520.
```

One or two negative members of a triple use this pair bound; three use the triple bound. Summing the scalar forms over physical coordinates establishes the assertions. Retaining the partial coefficient gives the decisive estimate

`delta(15/16)+(tau-delta)K=499/500<1`.

### Exhaustive tree cases

The 5040 increasing-label arrays reduce to 115 rooted types. The disjoint class counts, written types/arrays, are

```
four-deep-root          30/2556
four-deep-first-child   28/600
shallow-first-child     7/52
shallow-root           30/1638
height-four-broom       1/7
easy-long               2/56
matrix                 17/131.
```

The first two use 499/500, projected onto the root or its unique first child; in the latter case the root projects at least the child's squared norm. The shallow-child margin is 1/4. At a shallow root at most two depth-four nodes occur, giving bound `3/4+25tau/128` and margin `17/768`.

For the broom `(-1,0,1,2,3,3,3,0)`, normalize root=e, write a=q1, t=|a|, z=q7. We have `e.a>=t^2`, and z is in the diameter ball of 0,e. For t>9/16, the a-projection of a root extreme row, divided by t, is at least `t/4+lambda_z(3t/4-1/2)`. Its minimum before t=2/3 is greater than `(9-5tau)/64=19/384`; afterward positivity is immediate. For t<=9/16, append the root-to-a angle to the three-link tail estimate. Each negative e-projection is at most `t(1+sqrt((1-t)/2))^2/4`. This is increasing on the stated interval and is less than `19881/65536`; total coefficient mass three gives margin `5893/65536`.

The easy arrays `(-1,0,1,2,3,4,1,0)` and `(-1,0,1,2,3,4,0,6)` have a four-deep marked ancestor closure or weighted depth bound at most `1507/1536`, giving margin `29/1536`. The program checks every marked triple and every location of its delta coefficient, not a sample of geometric realizations.

### Secondary-apex disjunction and common-direction certificates

The five root-only exceptional arrays are

```
(-1,0,1,2,3,4,5,6)
(-1,0,1,2,3,4,5,5)
(-1,0,1,2,3,4,5,4)
(-1,0,1,2,3,4,5,3)
(-1,0,1,2,3,4,4,4).
```

Put b=q2. A cap-tau row at either q1 or q2 has an extreme apex-plus-triple of nonpositive b-projection. The 499/500 estimate forces it to contain q0. If q0 has coefficient tau, the remaining weighted pair gives

`-q0.b>(14003/56000)|b|^2>|b|^2/4`.

If it has coefficient delta, the universal conclusion is `H0=-q0.b-(389/2000)|b|^2>0`. For the non-chain arrays, the height-four bounds improve the constants to `145/512` and `557/1792`, both above 1/4. In the chain, all partial-q0 triples except the pair q6,q7 give constant `83/256>1/4`. The last possibility retains exactly

`J=-(2/3)q0.b-|b|^2-(7/6)b.(q6+q7)>=0`.

Thus the complete alternatives are `H=-q0.b-|b|^2/4>0`, or, only for the chain, `H0>0 and J>=0`. No choice of favorable independent coefficient rows is assumed.

The embedded 17 literal C,A tables fix one direction `d=sum C_i q_i/1000` per tree. Twenty-two literal multiplier overrides produce 1785 identities, one per tree and extreme root row s:

```
x^T Q_s x=d(x)(x0+sum_(i>0)s_i x_i)
          -sum_i lambda_i(x_i x_parent(i)-x_i^2)-lambda_H H(x).
```

The H term is omitted where not needed. Another 105 identities for the chain, with nine additional literal overrides and the same d, use H0 and J. **Every one of the 1890 matrices `Q_s-I/4096` is positive definite.** Shadow multipliers are positive, with minimum 29/500; additional multipliers are nonnegative.

The main checker verifies coefficient equality, Bareiss positive leading minors, and a separate Fraction LDL factorization. The independent checker parses only literal source inputs, reconstructs monomials, and checks Schur pivots and the same minors without importing the builder. Summing an identity over physical coordinates shows that every extreme root expression has strictly positive projection on the same d. Averaging to a feasible capped root row would give zero, a contradiction. This closes all eight-vector cases.

For 4 through 7 vectors, a root with at least two children has at most four deep nodes; with one child b, its subtree has at most six nodes and at most four deep nodes. Project onto root or b and use the same 499/500 bound. All 870 increasing-label arrays are checked, partitioned as 718 root cases and 152 child cases. The argument, including all norm ties away from an escape edge, is not restricted to rank three.

## 4. Mechanics, strictness, and the universal lower bound

For any positive-definite pole metric M,

`D(i,j)=q_i^T M(q_j-q_i)>=0 => |q_j|_M^2-|q_i|_M^2=2D(i,j)+|q_j-q_i|_M^2>0`.

Every maximum-radius pole is strictly unstable: equality in the relevant Cauchy–Schwarz bound would require identical poles. Thus multiple maximum-radius poles already give multiple strict unstable vertices. Every non-strictly-unstable vertex has a nonnegative derivative on some true edge, since its incident edge directions generate its tangent cone. A unique strictly unstable pole therefore gives the required weak escape tree.

Use the reciprocal primal metric `M^-1`. The foot on facet i is `Mq_i/(q_i^T Mq_i)`. It is in the relative interior precisely when `q_i^T M(q_j-q_i)<0` for every j!=i. Hence strictly stable P facets correspond exactly to strictly unstable Q vertices relative to the **same origin**. Under `Q->TQ`, `P->T^-T P`, this metric is `M=T^T T`; there is no independently adjustable dual metric. Actual centroid zero and the quantities omega_i, q_a.c_i, and Lambda are preserved under this paired affine transformation.

Combining the weak escape lemma with all the actual row caps below 7/6 proves `S=1 => F>=9`. It covers nonsimple and nonsimplicial bodies, pyramids, all actual face lattices, weak escape equalities, and arbitrarily large but finite anisotropy. No generic perturbation is needed to handle a zero primitive elsewhere. It does not cover lower-dimensional bodies or nonuniform density.

For completeness, at any actual vertex a of an own-centered P, triangulate nonincident maximal facets and cone them from a. The actual positive tetrahedral volume fractions w_T give

`-a=sum_T w_T(b_T+c_T+d_T)`, `sum_T w_T=1`.

Each triangle has three distinct vertices different from a. Thus every apex-excluded coefficient is at most one, and the same lemma proves `U=1 => V>=9`, without assuming that the polar has its own centroid at zero. The earlier journal vertex bound is thereby recovered from the included certificate. :contentReference[oaicite:3]{index=3}

For strict 110, Euler now gives `E=V+F-2>=16` and C>=32. No enumeration of C30 is needed to exclude every C30 realization.

## 5. Sharpness and a completely reconstructed physical control

Let B have cyclic planar vertices

`(1,0),(3/5,4/5),(-3/5,4/5),(-1,0),(-3/5,-4/5),(3/5,-4/5)`.

For r>0, put `K_r=conv((B,0),(rB,1))`. It has exactly eight facets: two hexagons and six quadrilaterals. Its centroid is `(0,0,m_r)` with

`m_r=(1+2r+3r^2)/[4(1+r+r^2)]`.

For `P_r=K_r-(0,0,m_r)`, the upper-apex/lower-column physical coefficient is R(r). All six side poles have common height `(1-r)/[1-(1-r)m_r]`. The height equation and coefficient sum three therefore force the lower-pole coefficient in **every** upper-apex-excluded representation to equal R(r). At r=r*, the trace bound gives all coefficients <=c3 and the forced one equals c3. Hence `gamma_upper(P_r*)=c3`. This is sharp even for exactly eight actual facets, but it is not monostable.

The fully replayed rational member r=1/2 has raw vertices `(B_i,0),(B_i/2,1)`, translation `(0,0,11/28)`, volume `112/75`, and P/Q f-vectors `(12,18,8)/(8,18,12)`. Its poles in bottom/top/cyclic-side order are

```
(0,0,-28/11), (0,0,28/17),
(56/45,28/45,28/45), (0,14/9,28/45),
(-56/45,28/45,28/45), (-56/45,-28/45,28/45),
(0,-14/9,28/45), (56/45,-28/45,28/45).
```

Its complete top physical row is

`(132/119,0,1125/3808,675/1904,1125/3808,1125/3808,675/1904,1125/3808)`.

The reverse coefficient is `51/77`. The exact ordinary centroid of Q is `(0,0,728/8415)`, not zero. P's identity-metric class is `(8,12,18)`. The decoder reconstructs both hulls by supporting triples, all facet and edge lists, two distinct-apex volume integrations, every facet centroid and cone weight, the full physical matrix, all true-edge components, and all 255 nonempty-subset mass/flux checks. This is the unchanged late trace control, independently rerun here, not a new 110 candidate. :contentReference[oaicite:4]{index=4}

## 6. New reciprocal actual-facet trace theorem

For two distinct actual facets of a compact full-dimensional convex three-body K, let u,v be their nonnegative affine defining functions. Define

`B_u(v)=|grad u|^-1 integral_{u=0} v dA`, and analogously B_v(u).

Then

`B_u(v) B_v(u) <= Vol(K)^2`.

This raw statement does not require centering. In fact, writing d_a(c_i) for the inward distance of the actual area centroid c_i from facet a, the normalized pair product is `A_i A_a d_a(c_i)d_i(c_a)/V^2`, independent of the interior reference used to normalize individual rows. Applied at the actual centroid of P it gives, in the one physical matrix,

**`Lambda_ai Lambda_ia<=1` for every pair of distinct facets.**

### Independent gradients: projective slicing

Choose affine w so that `(u,v,w)` are coordinates and `dx=J du dv dw`, J>0 constant. Except on the measure-zero set u=v=0, make the projective change

```
s=u/(u+v), z=w/(u+v), r=1/(u+v),
(u,v,w)=(s/r,(1-s)/r,z/r).
```

The image L is convex, lies in `0<=s<=1,r>0`, and has volume Jacobian `J r^-4`. On u=0, the weighted trace element `v dv dw` becomes `r^-4 dz dr`; the other facet has the same formula. If

`A(s)=integral_{L_s} r^-4 dz dr`,

then

`Vol(K)/J=integral_0^1 A(s) ds`, `B_u(v)/J=A(0)`, `B_v(u)/J=A(1)`.

This also handles facets meeting at an edge or vertex: their common zero set has zero weighted facet contribution. Because K is compact, r has a positive lower bound. Truncate `L_R=L intersect {r<=R}`; these are compact convex sets. For all sufficiently large R their endpoint sections E0,E1 are full-dimensional and of positive weighted area.

On the fixed compact convex set `conv(E0 union E1)` in the (z,r) plane, the density `r^-4` is gamma-concave with gamma=-1/4. Borell's conversion in dimension two therefore gives measure parameter -1/2. This is an application of the same primary density theorem, not an assumption of concavity for arbitrary weights. :contentReference[oaicite:5]{index=5}

Since `(1-s)E0+sE1` is contained in the s-section of L_R,

`A_R(s)>=[(1-s)A_R(0)^(-1/2)+s A_R(1)^(-1/2)]^-2`.

Integrating the harmonic chord gives

`integral_0^1 A_R(s) ds >= sqrt(A_R(0)A_R(1))`.

The integral identity is valid also when the two endpoint values coincide. Monotone convergence as R tends to infinity proves the claimed product bound. This avoids assuming boundedness of the projective image, or an unjustified endpoint-continuity limit in that image.

### Parallel facets

Write `u=alpha t`, `v=beta(H-t)` with alpha,beta,H>0, and let A0,AH be the endpoint areas. Then `B_u(v)B_v(u)=H^2 A0 AH`. Brunn–Minkowski gives

`Vol(K)>=H(A0+sqrt(A0 AH)+AH)/3>=H sqrt(A0 AH)`.

This proves the remaining case. Thus every relative position of the two actual facets is covered.

### What this adds and what it does not

There is an incidence-sensitive strengthening. Put `K_ai=conv(F_a union F_i)` and `v_ai=Vol(K_ai)/V`. The two actual facets and their two weighted traces are unchanged in K_ai. Applying the just-proved theorem to K_ai gives

`Lambda_ai Lambda_ia <= v_ai^2 <= 1`.

If even one actual P vertex belongs to neither facet, then `v_ai<1`. This is a strict volume statement, not a presumed uniform gap over degenerating shapes. Combined with the same physical matrix-square identity it gives

`12omega_a <= sum_(i!=a) v_ai^2`.

For exact rational data, each v_ai is recovered by taking the convex hull of the two complete actual facet vertex sets and summing its oriented boundary determinants divided by six. No triangulation diagonal is a new actual edge. This strengthening retains missing mass outside the two-facet hull; it is still a necessary inequality, not a C32 exclusion.

Every 2-by-2 principal minor of `I+Lambda` is nonnegative; in particular, over-unit physical coefficients cannot form a directed two-cycle. This is stronger than the individual cap alone and is imposed simultaneously with the matrix-square, flux, incidence and actual centroid identities. It is affine-invariant and holds for all facet counts, hence for all nine-facet and C32 candidates. It is not asserted to be independent of every other possible geometric identity.

The constant one cannot be made universally strict even at nine facets: any right heptagonal prism, at its own centroid, has both base coefficients equal to one. Its two bases are strictly stable, so this is a sharpness example for the inequality, not a monostable candidate. The finite algebra checker below verifies the projective and weighted-boundary Jacobians, the harmonic-chord antiderivative, and the already exact frustum pair. The continuous theorem is the proof above, not a finite test of bodies.

## 7. Actual nine-facet boundary: a closed chamber and a common-mass formulation

### A complete continuous C32 subfamily that is excluded

Let C be any full-dimensional centrally symmetric planar octagon with center zero, and put

`Q=conv({(c_i,1):i=1,...,8} union {(0,0,-3)})`, `P=Q^polar`.

P is an octagonal pyramid with `(V,E,F)=(9,16,9)`. Its apex is `(0,0,1)` and its base at z=-1/3 is `(4/3)C^polar`. Since that base has area centroid zero, P's actual uniform-volume centroid is zero. This model covers arbitrary pyramids with centrally symmetric octagonal base, together with unrestricted affine deformations through the reciprocal metric.

Write any positive-definite pole metric as `M=[[B,b],[b^T,d]]`. Choose a largest-M-norm vertex `(c_i,1)` among the eight base vertices of Q. Its opposite `( -c_i,1)` implies `b.c_i>=0`. It has strictly negative derivatives toward every other base vertex by the maximum-radius argument, including tied maximum radii. Toward the apex q0=(0,0,-3), its derivative is

`(c_i,1)^T M(q0-(c_i,1))=-c_i^T B c_i-5b.c_i-4d<0`.

It is therefore a strictly unstable vertex of the full Q. Equivalently, P always has a strictly stable lateral facet. Consequently **whenever the base facet of P is strictly stable, P has S>=2**. This chamber is explicitly `max_i |b.c_i|<4d`, since it is exactly the strict instability condition at q0. No assertion is made for its equality boundary or the complementary stable-root chambers. This excludes the whole base-root chamber of this continuous C32 subfamily, with arbitrary octagon geometry, all metric shears, ties, and unbounded anisotropy. It does not exclude the other possible stable roots or a noncentrally symmetric octagonal base.

### An exact shared projective chart for all nine facets

For a general own-centered nine-facet P, choose any three linearly independent actual poles q1,q2,q3 and put `u_i=1-q_i.x`. Some such choice always exists. For the other six poles write

`q_l=sum_i alpha_li q_i`, `beta_l=1-sum_i alpha_li`.

Their actual slacks are `f_l=beta_l+alpha_l.u`. Let `J=1/|det(q1,q2,q3)|` and set

```
r=1/(u1+u2+u3), p_i=u_i/(u1+u2+u3),
p_i>=0, sum p_i=1, u_i=p_i/r.
```

The transformed body is given by r>0, the standard triangle in p, and the **six same physical planes**

`ell_l(p,r)=beta_l r+alpha_l.p>=0`.

For the three chosen facets set `ell_i=p_i`. At each p the allowed r form an interval `[r_-(p),r_+(p)]`, possibly empty or with r_+=infinity. Positive beta gives a lower bound, negative beta an upper bound, and beta=0 remains an inequality in p; it must not be divided out. The lower and upper envelopes are piecewise affine. Original boundedness gives a positive lower bound on nonempty r intervals.

With `infinity^-k=0`, define

```
A(p)=(r_-^-3-r_+^-3)/3,
H(p)=(r_-^-4-r_+^-4)/4.
```

The Jacobian is `J r^-4`. If D is the set of nonempty intervals,

```
V/J=integral_D A(p) dp1 dp2,
centroid(P)=0  iff
integral_D p_i H(p) dp1 dp2 = integral_D A(p) dp1 dp2, i=1,2,3.
```

These are the actual three uniform-volume equations, not the centroid of Q and not free section weights. Every physical coefficient is recovered from this same L by one-sided coarea:

```
Lambda_ab=(J/V) integral_{L intersect {ell_b=0}}
                    ell_a r^-4/|grad ell_b| dH^2,
3omega_b=(J/V) integral_{L intersect {ell_b=0}}
                    r^-3/|grad ell_b| dH^2.
```

For two of the three chosen facets this specializes to

`Lambda_ab=[integral_{p_b=0} p_a A(p) d sigma_b]/[integral_D A(p) dp]`,

where d sigma_b is the ordinary one-dimensional coarea measure of p_b on the triangle. Thus even these boundary entries cannot be chosen independently.

To restrict this chart to C32 one must still impose that the **same** original H-polytope has exactly nine actual vertices and sixteen true edges, including all nonsimple incidences; all nine rows must remain irredundant. The original recession cone `{d>=0:alpha_l.d>=0 for all six l}` must be trivial. There are no suppressed metric variables: M ranges over the full positive-definite cone and the primal metric is M^-1.

This chart is a recovery recipe for the full actual moment problem, not an elimination certificate. A promising remaining target is a three-cycle analogue of the reciprocal inequality using its three boundary integrals; no such inequality sufficient to close nine poles was proved here. The journal's rank-three, all-apex cap-one nine-vector controls already prevent an unqualified extension of the old eight-vector lemma. :contentReference[oaicite:6]{index=6}

The remaining gap is consequently precise: the actual coupled nine-pole system, with the six physical planes, the three displayed moment equations, full incidence and reciprocal mechanics, has not been proved infeasible or given a strict 110 solution. Strengthening a necessary system is not being recorded as exclusion of that system's entire geometric domain.

## 8. Complete deterministic F9 recovery capsule

Environment actually executed: **CPython 3.13.5, standard library only, assertions enabled**. The immutable ancestor is the assignment/hash above; the immediate proof text is the preserved `NOVA24_ACTUAL_TRACE_CAP_F9_V1`. The following is the complete unchanged late decoder, including every compressed source byte. It reconstructs four complete runnable units, all 17 literal tables, all 31 multiplier overrides, the finite tree proof, trace polynomials, and the exact physical frustum audit. It needs no journal, previous sandbox, optimizer, network access, or unstated parameter.

Save as `recover_nova_f9.py` with UTF-8/LF and final LF. In an empty directory run `python -S recover_nova_f9.py > f9_transcript.txt`. I performed two separate clean-directory recoveries in this assignment and compared every generated source, report, ledger and transcript byte-for-byte. The full immutable parent recovery, including its separate physical controls, was also executed successfully; its old exterior question is superseded, not reopened.

Decoder: 18655 bytes, SHA-256 `7a08d32e43454546cc3f594d31e8e04dd08a2aee5cf0e31afe4a8717e559bd2c`.

Whitespace-free base85: 16670 bytes, SHA-256 `850bc4bc8541284b3f5a0d0d4254be3827ddcad65f80495734dc21218f11b15b`.

Decompressed source-bundle JSON: 32147 bytes, SHA-256 `29ae72db8272ba0d1dfa3162377a26700b8aba70cc4d7267afcf274874ad56b9`.

The full file manifest is checked by the decoder. Its transcript is 879 bytes, SHA-256 `6d924e23233c05562e44de91bc1b3eea22a63a9c0c5d5d45ede1ccf799b68628`. Expected substantive terminal markers are


[Encoded source block omitted; the code in this passage is incomplete.]


```python
"""NOVA24_ACTUAL_TRACE_CAP_F9_V1 recovery.
CPython3.13.5; standard library; assertions enabled.
Run in an empty directory: python -S recover_nova_f9.py
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
B=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;C+%a)m;ERh=^uXP~}q`MmN;rF2NM6)|{c94(n^!{(r34d4ee~M(PO}?IWy9j-yfksloos
{`j_LMk)=(G>gDL7?Pe%rB)<VbsvZoGs;cp*q7YGVSt+1SJ-%0{P{`<HJ2xa1Vxg^bI8<MJ0qySI_jSVJ*6iu^w=pr)kK!ax)ero
;{*Ai4mr=ks7tEG`hl>*kX<jh9uE{*q=75xP1MTx#Ll))rKN=7r=zx}cB!~Nq@aT?-p{(-I;orx4~L)dW(hE`)lg`{-Z+PN@DvI*
xu>OkV%c+`T+`|stvm@k^`YHo0Hm(-h_H8gT)5+AIbO5QPr8b#I&Nr~QS>&iJn<KW^z5JsY+VTBn^_F8X19I8xLyc)XE8qqvm-oV
JF(%`0wgd@y*(*1tv;24D@{v^5iXdMu;F;s!mi@d{)h7m?`o?Xzk(^P<lVfzTJ_Fm{Ls8W4c(Ocuj|;jKKPfSx@o_q9smNV8&Jn_
+^_r@ymH_I3ObbjTE%9-f32+fCrH>>=rUob8?@7=3p*t&XL$S+*Ew^iCo^*EuXDh{ScJ@K4rJl0$|nt9BB9;qBrm0TW-*XxFj&SK
OaMTiXl~4cOJMT|Z+`)>KAYPkZL;kqX|w7X3-?=KAREU6sSk6BJ{*U!8yeM@0FO*gXIJ)v=A>r?-n&!l>a@xpsOT^$j|iE^%e*`6
y<~N(ysVF9UB~w<iCg0VSW1}UYyYNOb1Xk$!7o8%<*kUIMAz=M4>~ds1+}skRwr{X9mKV)QcSt%kZGdoG~!Wr+UiOq+_d(;IF>mT
5zd~kMz|OxPr)3$yytrrk=KQWG2SWeFV&UHjSOrkR()yXK=bM~$ro#Y%s{}StXwshxv;vJu92EM8{oE5M^&QljJLF}O~aaG%`TTm
aY11kMURW>a8*MRD>XFPEk{Yr9as#Su63%KaclK_=8xuD(xubol3ANJs?H+6Wh^^t!TiUm5let)$ffyYy87ThG$y2PK21@KdmAeD
Tx#lXW%y@Hg1(cn70rMb{eExI&(wEp1Du{B&lJ`UhXHlqpEr3Xa+Xth{wvm}?58QWZPo@#VMt9R30LawA@AauW`)1-;m6!dT6>A1
NuU1eSN;scFxe`U`bRib>R}xIMq{_Ks2=3m@y!>1yhAGhYCWdPu?NvAUXESo7v!@wLID?M3iu}S+F+$pK{`i4YXn6ziojB!z$~*s
6HvvPJhN=Ga^)I=<vTj69<Stg%UUR06LO>7m%!<y5@~Zz9BIwll}ncC%DPs2*nRE6H~IGP<Z5R3WNs><2C^@i>Lz!e1x8oo1iRd2
)nGPPi!e~<)2M7Fqui%Em~uTcsk46U{5mrI*uXIpY8Iz+r|r99^al!YHPm2od<GrMYVr(o5pBJ}b{7%5VUxkeSlUg9lF43FJ3|Sc
I3d$!8Cta&+)gnAtlIQ1vEQ6PN;@Mmp)OAQTG{nWfv*eOpU|S|s1Qakw#ldEn6TXC%xXU-IT*WEV5O_~E~lNwkym$-sS4_1PDFhr
!`8|PMcx0>hKr`!l#cz7_M<A}bHIKU=!z&V`^mGpXQG-XXPU|UT7Vq{Z7IOhmqDKtFPdyxBYLrl5_sHW@joPjv~Dx1D=FX(bd-jM
H~n*ND;&K9WT9GS`?DJG)(_e^g>ey-p%8@3^#ReLEN{hulvM8dfRtYenYwYMj3Lj_HKMI(+xbB0$eWw30ND{F?(rWWf{~5Hm1X;e
kqB!Q0c0RIiJ#oO)1{%kYBPtt^m7^(kGNHUYi`~M|H6%)OI5pVn3O`z)}KLr>cH-eL9_bz>1>U^<9+cn?v9;UPHXUbskDIK-TRb|
qoRZ&9|O6*lw3bW8ht)A!Z5<?3SX9Rw?dE})m&IQp|+M7z^CSx?Vm@Ins}fRRzLpv!)=z{Ka8EKQNw*DgQ){md=nM-`>z|+^a!@6
CWvKO>5YdM%;B7CAwq5li3JTCLSoaM&Hii2DR*qQCGB>c;48r1sNL`o*rumUyxv|w29aJ-gSS^DKh=~r?Ox=Yc4m^b%68)|0W}_b
_$24#xbGZ~m308Mh`hII5z{D&vxbq7xIx&erU+Xw7HSe%YQ>-R7~W^}+Ps6(sO*n)?dc(DvOR`uyblgfhZ}P&5a|&fWXC~0Gf?r)
&&;Vz@_U(KNJ6~x^+j8M#x`PeMCt3j?+o0Ht!&B1XZz!@m;!~Z@gv&WH};jr3BA6KHL{kcoIUsGy9kW9JrFao%Obn$rM?q_!e4L}
C#^4}x*K;&FlhstCIJGp)rO$gg~h?iat3p{x6=Gc<5#nZX|p+I#$_Pce>7h&mLv)dYzF0(Ldp~E@7WAQGV!C#XX9T9P*saE=yo8r
c38Qt*9=+s^giFPb<a2wnA?DtRSW<<g~+Z|4tKdh=EolOh?C4HLPOBujgn>`RVhQa^`zP+p${hUH(Vn%(%8gQ_>%7{W_aqpVyx;J
BJ#4C*m~Ek(w4>bMi{~Ndqx0I1<3^aQABf)Ld`CLbKQ7Mu>LO08ByP8#*s&RO#4%=0OQ;+;dt8c$-|jdYt3Ja{Q3SaR8q}Rn>H>(
=jNQcuH9LE=O%`9#_NpJF*VwJc7eN-jT;D>B9#d`q_KL-9-ldKlO<a>E$6P%8z7EKOk^SczT_oGxZ@NdAeJ{Oif1d!bFxV^_}<~}
Rxjf#hGad@`_G(kC419X1|a_5as!39ZeCd2K8p*=?{o5Omr-x2a0~eXpHw!xB=wIj6=`JL^-Nl79!t4$qKWAadzfDYsVVsBL->bq
@tKDQ6Q?tj>_=0rSDxxhLC;5-Ieu-#_@z;LIK7T|mWqkw0@4{jdx6zMR6%-oQ|UAjdUc5SI}EB~&rE7dleW0ky<qk#M3?pvCHPu6
3Th7vC{IP;7&V?z3rt&()?|Vm$>o-}dDQ&i$NG)dr3!oK44%B&uoC@Q9w5g(;iUlRjWz9J%x5ibT{42kx0`Nucx&%e)-x>POjRT&
G@0oS4s=J!MmjEirOCf)xd6YR`VEwb7#WJX9A`v!XQEC8@I%|AzT+0{=?vqOvg12V?*mNyWckPvs;?hps=V+}!u+dfFaJ!vA3&fH
RKd}*E!mu*b=_3Hy<mx0;hBxZRraCHQF;;Pp5u6m|I@`2kHasdcVvGn-cmgU3d2^`3Ox)UFY|5p);d-mBH!OS0j^HqJ~ibWf!T2(
?;?EW6h_hM+0gg1X{Nhkia{hE?<y3KRH*PnR(&}3)OoZ1Z*`nfxDhf}y5C4j<SYNREWk;-Y;r7?#a>m(_x}TJlbnqm2`FW;`U7kU
&SIaxJ(ooRhV+%qas}f9ODB|~a^>zwW{-XzdI&v0*p$Fp>#4@8Fr&#L2Mj~=8vTyz8i;@%Y0ylbL@b`nAn5{HA=t;luvchMJ!DG&
W(*I|#cs|F8gQZoeYv#CiH^6kZIVa$f97xAY_)OkJ+;W(SW20|a%>-1f+TfekdJ!8WBFtII@~LNi{%F@#_WS#<O+FTEs|_6q)C%x
LU6yCSLY2;PBzjc35cO-WGF=DYl~<)3q8b-Nyk^sf^9M+zBvN8X{&$q6L5J5q9x6*-g>jTDvE%Qvi(fhU~o>Q`r7fj<Qb7*zdkuz
?_7NW8+u8+JKbwzqqRnW7wi+-_2P8a>5>JlflSg5(9C#j<Qa&ShxE3cp~IwM`mFE@aUY-^=QO;r^+trt_I6jNks>EGSw280pHK}j
O556vZEv*_WSUYf^}|Kq1ts_FkSp4m@JP_6ydPt{bQ?+CNH{`7E6>nD&_&a^edsjt3glamLV0x-FErba*n68f9++GKs%&bj-Hf4@
W@d&yKaNtbUKxxQ7VL~07V{)<5=3j$zddCb3D(K0pcgHK;u|A2Y)Lt!7f#LrR_!;AZ)U+N(}QDwnAEe34`N8zL)nCFuCfvCasF&y
X_ulkG2!bqqgw^g;OEC$LyIo`d1JSzd{e!`f4_kYwKB;Nt7rQ+69WNX^lXgr<Q5-N!MNh;h6ulnpEFc**@1!T7NS>7ibv>*3DQYX
@k^UW@aKO$kw=<0maiaWl~n(n(D=fnQyVg#_;3`eKpYJ-%`q>|F0=v&VPHLb0M$%b^OvQF6m*Vn$W4Nis7E(OIa7fg^q;24pCMIL
#?u8*=iz1N6*V9#SNhwr&<m-1lLjYqtmMCzd~KOh-$Wu7VXn-YX};&{x12S`DK2}1v$Vx0_@K2jCBwUml$T$GSO8>FxF;SoBgs!%
9?U$9`GJ?@RlH(aoT>j`z^gAW==HEJn;8QOTvAY>Y`zPxIrkeI@3MP=NFuMq9UFgqi*22t(CYk7iY51r!aK{j@Dr)oys?&tbcI@%
3y}lSccvr>A)pi9s;M05XwAfn-yD>rCcvwF_Mk?p+;HSthrnSZyX>XoH5|IWWAaH7GOP5&Wee!W<S>L1Ur0JrzgYhGDXyXmHvAx)
HHP<zQ{JW_S@}?*4nIyat?{N^dvGf~pvH^IrM*G56PqTu`g<u)TNC*I%T3yxzs`Yn_yUp-=`(WM2b2kXAbE--_*=r!{`4ZM)F`$v
249*=(r_2x2T@D37e$Rc7<%~o#6a`pF%4^<H)y0PZ}`cWb0DZ2-&Q@U!|j-L<E+YltajK*-axE!hDWmP|80f;Ehi)+?SPNy2EisI
blv9&QG*<gGPqw-3b#ztm|gbSf=3#&<kOX1pMr}8&=bl;O5)r-(Vdcnfeyz~WAADkmGo!VyIeI10Uz7bB-d}NhyxHguMZ-V{9z}8
w<j32ie!TmK||MR8ee^D_Enj6mOrue6`Z1Xl&e?f;9}1DtH<AH@8AFFHJkpm0-&eviGY{x*CF!<-Du6Rg1ftB7qk6-k&V|N;?qhP
KX5kv#YAyk`A!@w6!teQob!P$FMa<mLiCQ;m>1zRRt^h{Pt+QI@+*M)X1`m+mzHG;BY2PQWVY(uT!C8ojrYIW{DB&w2hUd$L`R64
sIV)w$How@Nl*=ZugVHIW)1-JHEK-Vm*T?x<sp#OMCJzz6u?k;{~EOphIH&Krz@GZ94EVjrzfVkdcW)zlqm%+-i%rvOO1tlGbtl`
-|Q*m!(=1IBb?4jr3_R^3ifu`?y76%roEa%^pK$NUn<1Pd<qU82EN_Re{j8nVy1^<EYwk`3g*afmM14EU8=P;;ye>JUp=deDk5JL
xW$<YJ8IJzyjaC1M?K@RJCI|eU-r-@>L2ZWQ5z|z<`_UHPi2Iu8E`?nw*Z#~F$Y|ux##l7GDKf7zRm7DOy}w?a2|A$Rmcmf{uPgk
G_cHmaPNZ3hgn*{sB4JdtNh_f%sm!SR*BDt#7?Jr+d^8~(_i@WhjT{p<qt-p{}bi8uSjOuK+jnPW?zg3iUURO@~^PMJSdLjnw*Yz
+2|pgFO^ygGRm+~<+g+fVi}(rvRez^L@@4a;H7$ZD_4P%#h6p!{!9SiHf%=Y600j=`j}f3fkQB|!;k?c30y4cA<Yl@<bFZguU~{3
QJl11!M`+z3oc93@XBvNy>U(AB3RAba_HLSLeT`#@d5#ZZ26K$8kBSL`j!%=<wa0RYAAiKuIyucLG=m=MtCO8LLwF;0MAIa9isx!
w--b|9(Xe*^O9JhJQ-R+52K3~!{$EFkM%**UPc$54`iqw-F)%$)ewV!Q@Tkc#^v|qh?PAmyD0bSTr(_&c;pB3YH#-?6|j|hWU|Uo
X18MbG>vM+U5%Vc2xV=GpOzkt?ytsbsY~D0aw7Bw%Hvyqg@p$O9=>48uOVU{wER^3zO^l*cu)=76ues8(^-JRJoIhbwb49^cBEKf
J)RbHBb0W;)sI(CqsyOTfneMwMN)z?k3d-Rs!bX%#x$I~s1=xyCW-x)6lFan#W-hk*1fa(Gr#>ES@<F$oL2{K1BAjsgto&v<yjuh
qGK(latg5!ssHkdyy=X(ni9EAj2IYlBeypJIAX8TtcYA+eEGr_P_iSYtNA6#a#1m^R$%rzk1%ByIXCY6h^%#8mex)`Jt?tAsV+2?
(oV52W$a!iminfDC^f(`F)ZB6ouF<pjog<W61B|4xusMqGNrUeqX^J<m!8VCoqK?2X&yM@U<xxFOnXo!YC#0{b&{u*eFDlF(4Pq<
fY<w?Ey|!qk(jqBAToiAUq2h^t-M_{BKrOMo?P70OaxVhKtrO;>wZ05QtHJoKAUwX#hlP`QP2{S^J=vgYE9hQ!VQMZ%q_brUn9zD
_aB)wO3x1_Hl!p&sBYQ}i*Xsf_7Py6hfr8O1_mMrY=Gi^4?u1NNzg(s+cLouQ)alWa-S+jH*GtW7W*JGt0$R4D0?1>%8_B=vJ*k#
i}WYyHxdpfAe4V-)w%%9`Ggo~3_fpZjY6u|tfiB(R_-Ra?IiVA&CxFVQfvtQgTVRso)FN=9R3so$qsg>#@+w!>}1xnt__G*4>MhI
j^pIvcf@%{J#zn<{-Y0O=$S<F#OpGW*D)QsfW7vj`Fsd|QphgiLeVdUsZSFtKe!GWNOE3Sv3I&C24}$tY|^TC=b7mee*048YKC~x
OO5Pg=bHRHg%bM;NpV#FkN}U&iq<v);Ek8rA5T%At7EO1h*<Rl*Nvc`tmWE+HSqcoAm&tvVZT&QF(en$rK;CX)x>rkiZ2;d+xhH&
!Z`~iITT;{=xm7LWJqcek7IrD-h#7mQqvj01&i!n=6=Z)kuWgJ^$_*)&GFQf91rTSf5?|fb0R4j>5Kg9_@Im6FY3!N@Tp7^m4C)u
CpRM4@FRtbp(kki1w|TM-w7e&D~|TAZNVYSonf=)=Mpu7eRtgduJ%DulM<GwV!Ia9VUy0l45{Cw@QQO6KoTqKJbQlfS77k#K4h+3
1VG0z1v;EY7MPOcaWBS54HBhb>GKz<U>zt!(ff+NOep6~*gkD{jlfq?&S?xEVEd^;KpY>l{M^YIdATseUDmH&ZM3Rw8(_$Ra?AAq
`84Wc#PhE_b`EWxlceu?OrJlw%u0=BjjoOL1=)1w(e$+8e9f+Be~x}GM&N?5E(j}kLhWepOSPGTOTtp#>f79hSLp!Mn<CwDyt;mY
r4l2^(J5>RABgcZv_Jb~(vvLHQUVS*FG=uOfB=5k5A#(4hph~yEM}aRQ<<`@=7AQDqW&#aYZ}>CxUKpbP%(3yt?ZQnmD2tm?^U1V
n+4Kgsos{_3>hf|Q)Yq^B+JkE-9!AAO`>Mgnk$Kg4FG96<T6k)kWF&1JAh8=e2c2SB~8kfsRMz}>G3yOGRLl~u*o(-R;14IArsS)
6o_=OKGMA9<_J^}3<WWC7VsbE@iN=Md1KeUP!+?C$XH<-@aS-p@w%Zb)R~kOGp3Z)n<dReE*=3N`>}_fhBOF9pK=*jj6K4@5J8^d
3-=W2JxLvY$QR}&4+vK>YAv1bxqr|hK@XjRYG_UT5V<BeYk{@H1Ugzl2GR=k+UL$M0`6BOHHE{d@8o5{-E%%O{!7?k0Vob!|G<oB
E8jqVN2HjMkAMDGX5?+rKyR0gw7kS2Lz#5XT6d*{=2k$GvJ<091J^|b0qZLbKYShG$PE+ok29<LQw=t!cSBq3fwuj+bc+HA_vrL$
h&gRWyIRl!f5KI$dl{NzB>zF`aX}OuxocO;*im+#ng~Iis)QY>vM!trld$eI(zHC|YL=MjW_@$4$AIFEwIef5Mw#_&7}n7ZS{Hlr
(~PEsuPdK_Qx_IQt)xQ32>YDv_*lw)_N8D{v{7Xq_aa>~PLa4CO_r_NsC%_>$_f3Y<|=Z(%Lzx@WvTIjlp9<@`eezbqxRoPJ*M(K
lT4%^9OA^CFQs%VT7sjl0jS0FdAzCdnQCRiB-*dlMD)y~>s@rU5@DLv68r*-R_M6EvMqbj(&dQZI_pqvWoaYvycto7v1NRQYkDGw
m?&U!lviE-f$7nA?(yJ<oh}aT|G;#`U#Qp_Y9CF5W>Q`&m<F^+BYTmko^DsreJ7VjeeTRnyh0WeO80ES<66e)Y>+5j(MXRBVIIjt
edSm6y)c*`VCM-VBKiJ-{wf%d0?r9LHxNlPOXB*UuJCdT{MnLURAJ`0Sy@Om{#J3p2?_X~FvFw)`U>X^#}11at~jg2RbOX^#+4T}
9f<5cSfgj}lX*MXB5cHjb*aAO_#+R-WbMj55RBt1L>sMU<1u<UhABsS3_vMe_XuSNMQySpcN5=SACk*|4J{Jx&Ti?d4^brZAir!Y
Y2!hc5V3_!@ndLoGLK;`h$PAjZvPGK0;zsFTL;x<dQ#3`#_(qndq;J*!`c!fK`f*~c=%_NaXc0cky{U$>x<b|i234a552;IdL7`O
qLg{s&W6ShRcU|1SXP}Cp|-?TrJgwsurBH%&vE_lEcY}+I>x`_l4%BrUQHa>bo+Ny8DA2P^gi5iguq!o%BJkIN^eGlhO17`f`V(o
Y|Xdd1}N6-solwQjwJF341g{oYt>S5{&C0ZD*KLHJc9=+ES=GhBA3P|PeXbN9L;l7Il~;*JUIdNm&H`pT}K_#h3$KprjEB*2o?I?
h;6s=Xwm{A6{;OyER8xtLN|u3-IWw)Sc8Vob_F#xsk{9&MZ-mPK;1lTXxf>vDj4>L*ydBFZMP2?nY*`*%;TZ6Bu10I^TXtuh3eTP
e9b@df<2(tP!)CIN4qi0Q%2#2Ad=DX;>Y^N<`A!!WIGo}Y=rnbzGJmbC<0jT4C>!kks<Ont{%N?;5v6wS?BiwprOswkd37p>9eaC
<Op%3&>5E_L}<K%Q)V0e2byk~CxVhmz7ZMbkCBnEy2d66v_;eI7z*f=lnN9=`_WDj?p3hoP+OP+no67Qu)-VD@mTFZ2((ZMN?Y@H
4cq!Y*i03ZYxq}vlHsQjq9RwpLc<y9D=?m-;#`T5@T!RA8^HGtWxeCSN|1yor`<Tl5RrAzOzV{?$#%a^aZB-=*!I=mWjZUg=&T^t
b2ni+BqF8Q^-C#ikOVljjU`)o3|^LrPri!+Rq_cLC3a1w)sc-dQ3zfKl=0ZT-@b*1hFZFoNXv=MGaf#QxLwHz%cc{aX8>yRL=N1Q
5$&iaqRlZ|wPviw?CGe*OSH5x(R1Ge)XD*YHCi*!KBb#|0|Ob`+&%3Qj6#y<)n-Yg9;eU{+%qCSUZjrXKj+cQ_Eh^M0aEc5$hk!1
^juNZbFI#Dj`_6Uq<@C`->*ewHNbv{bU2RF<#e;Hx>3e6B)++`A<z0j#cfhk)M8~RZn=O#(xnsUdSEVz8Mcex28l-BsnDj`h8r)p
@*9XHO_ltLRc_Y)$5Nq<38EqVvALuAz};o;ZkS>sb4m{2en*jz`m(oR=185t_)ipB@5N7x#wWG2{$3(USqN<lo)HurmpQ$|^m#is
Vwn_58O`G*kF9!j)=YafNm&Bjt;K%xea>=Juj?o(XN6Q^9K-!pEP3HUB2n?ncG=NYp$QZ~S;(HeRB1~=oQ;D*CW?kGx|Q^-NJLwr
ZF8NtCfgL{C;DN2Y0>Qq@43M}zAt52yqi}5)352aE7pj`fPOwYY<DK)sY(kc>2tAcCY9-|q&?X<7{jA*1WdJB<D0NV_H^F#D~u`A
M(a^5j<OsgEdiL&7Mz!FFUVnz#kQZLvL~-lN8SczgqnoaK$mVLhQPmp&qYmJ+E*2r2yieT;iOfYyZp2{4FCWPYg&|9M?u?*&bP>-
W9NIQ+t6$~?<h4lbb%2d%36`heB0qEgq_+=SDp~69VymnumKruLE!|ksg^N*K%1dy29z^87X#L&U~&8hN_=C_t$?c_SR_{KZQ-OA
n^+9tjbxq)2p-f~9)}tHUMX#-=U4mavMU68uFrgW=T6$QKv$&F9=-_qvxGB-6ukWIRNwjz^7#qd1J<sRkyf}XDLR4S-Ee4z-|9ws
Qhs1LQVuQ>C;k1gyjq|Zf>E%xZY@SPN=`@A$T$cM$cwU8d+5~XnUIn9D8C~48YC#KBY&V}BIE7@v}0rco|cWhdYEB*C^O~UyNg8R
eTQoU|JB8yR$PeX&0AgCg*iQc|Az@m4u;ZfKUtgHoPip;HnImkrU^b!D)ztMAL%NU#$Est-=gf#1OCa8ezxuH&pqzvsdG5X4GrpJ
k!4&E6ZOFVr5nl7uu9)mwz@{v$!3&|G4P@A2ihe%zT`m3wJ+>Di?ReR#90gCnxa1CbG#7wvMbV_wlc}3BkTH1o88vLsE=pml@f44
EinS~MYJQbp%P=kUF=kCerzfY4~QPr0ugp0$NnBV{qz-rMv=xOo<k=$37f4*B$!ND8%BLoorr|KwN9)VaUq<E!usvlvKK?uY+D~^
WSGdMMTNys83$l|g~Q$T2Rz-e?&&oZZ3&6M{sTtGT0U{~glR8lLz{JbB1O&I21uyLt6@^dO4EVmf3s-~yaV3^3dXJ+4%23XFn95J
^eg9NBvs<c?RTCfMET}A_Xlk5R6vIbZ#l9?@5>A}jcHd(>~_-Lb+I9DzQXr<zln;PMK$+=F>+h{JG5|a0S~X5DNvsNb;SFbMXwGO
Jq>vLNtwC!`mM^lo9MKWM-G+yvkoUjwIs?2gwO!agdhL1Z<N@(%i1NG<LL54W>7xSNPd`V3jZ!GB1*bRRdy3R1+*P>YM$e<K}yH~
V}4)ceD{g&Q|Z986;142v)|1SnTTOS#1;9<3cjx9{(Zr<`<bAl3X^$9g5@yU*lXgeCZbV4^dk005bh!v7;mCBv;i^hw8)~Yec8R}
nph#uwLmWug#TGkQEeFou1vVz)8g1f+ZwB7As<<foD@awU(^eRR1tz<W15*CaQiwS5Yk#?i`uq%@4SSXLtS}w_We{!>Rt{WS>l`z
lGxgVCBeGln?OcllN^(UqYl9Xe>k)P^#dJm!!6xTE~q3qrX<z-nuQtB<gk>X$>7`d?2LICK_TMSlt%H0bQP{`Zz$GQO7AP<VzvMN
D~jh>W30%5Dlm4hh*|;hBNS)6fCmbV*hWnS^{;fA*bm=o1<UTQ4X`G@P~;09p(d5dfpEfz){v+of3T~*U8_KTI8!7tyt?BpTywIv
qQslsQ&#06(9s1`>0}tmA3nc>s3TYsl6~+Yo6r&7i>zqODup{sbvlxv!v?^BoK#z_@u){4E<SiA2W6`nG*j|7Aw&TsQmqnyT)Vs=
b-)4ChHScHat&*lphcdyIiS2~uO|HiE9V0+dOU9s*_B~G9(N+Tn1ypelG}__UIWDqYM-gmRd-%Y^=GG=y1<ff-g{9XEaC4BdY~uy
{=o4aF%j+AFryg|k>k-K^>l3}sYr5$Mv~vWIBpx`TfiVr$#S>36t*(c#ytJxR8u}Ptqc9)d@wS9<;TcxK9dHUy6Ljj2djo`Z)Cm6
^6|P{0z*`~)?)5;HE3+x`-pu$m;jT_o8rE%`cdrZ?N+r6+r~l+<oZ*na}VB(bXd}qq^=VLmCTy3GyN6GQs#^GQn(SX*skUhh~x<4
Hc2OYuk=n}Q0RZ}mh?#5CVHCZ(bq#xgR5WMeo1!Z9uq#?e99G@vfyU=2!~IC#{M6^A|Ay+@XvKpdOPQdoqFsZ&GoA^RqMph2(cp{
etOV$BE?3;B>5K|*WQQ3Uh#8(mF2?AZMj0>!a&#w*32`519wCEBe@qtUy3+@72LZmZB=<`>I}mG=Hlz3W(QW4mh&iJ;Ceup2%zxg
l)$G}6YH{);M!duY3wLLqp0P|yd^TtUbjz_*bXm(77=tK{QYrKW%irg9S08q#V9?6Ae|kam^y$IYfG6OwI7I}Q4(73m_cj=nhb2h
^?st!tnC4=Fz%=ob8S6mqYoRr29ld$Z>=Q?mI8X67MH`eLW-E66c$!Rg046|Qs6BmHzC8jR;|hzeur6KoBWKZi|Q2=jfIn1!fl{j
op0EEgIZR~&cu)a%g5S<c;%$z(RZ)AK+`??*||45<?<V0gRf#5Jr$_4-5Ckh0`XYvq$udkynnp0gc1F!hBpt`fg*e?PERa;cDxmb
6`4C5YA-j()ASdFw%>WTegL50ru&2-Cl09ERmxis&dnT{ZipTrs0233NDH{0sI`-L8E5R{m%Wix7#nY#nOL9M<RT!y%ZS}smZgT!
rh*4X3z(IfOsKh7hRd^0G^D2+=w)qJnJZ=}Jw1x<cHY+2KaQ4za>xd5h=d}>C10c1$6?&_$A{5S>Ay^;Z$~6gsiR{v;ey&1ER*>j
bn!*tpYsA9Zi<e1q@OtHk3ES1lI(heQ<<rRH%h3F{@r~`VQarAA2JcqM4?6a(c7#UfqG_lRY5(Lxx{GnfB@1?O(3U7t5_a`A41W$
MdE;r-$bN2aWHI|Fr#e{t)r>^(F=shwo-e-@BzHYn73Q^;(}qpMC=J=0`@aBIx5P4_XDsy<}H0vCmH-F8IJGJiO|}?CKjiBTT=%7
MP9NalX;33%6k+GSfnRk<dA=~rEBHbHlmFs1P*LOe{TQX_^Xh}+Y0MZFb82<yAUX0bQY7LE~orjEZ!|JI4<Au5tJ~%>14=*FcF?p
<HbsVivQRrOB2)GvP#GzXFPGu3RF1AEjm0fi>?!Thsm)ic8k4s!DqgJsgCu91K2N4Lpanym-&p86I^HcSM!IAwMy&ux!VFO-@L_;
)y+=HkXU2|IPV57M_1_BNBM@d?dweJ)cYdOyt<)!D}4ATw(Flq9!z|lZoSJe1otaR#g^f(czS=})pSt*!)-@*4(mY6XMaj4&wm}(
2Guq~)10iN-d@e#&|te}cytnQz3QESd&UF%b|jX*qpJ21GHlqlK(LWV(qi08z%@h6PR@xM9~|ov){K$gFC~zwN@6qRvKCot8*o}V
Ov6$pDRsu7TQU8WVhWOZHJy<f1ykZdBQwpPnZTzdqEI~3yc2j<y_ecQDUjmKczH1+EBg^ez8ZP0{61CMD|223A68-uK$4b@Nnal-
k+-PHiEpDZv%-VOSqhHCt+puHC$6w-d7M`Gv)~@l{veJL>oKfD?Q+4S(KU9xI@AzG>oNvSih_q8A$VQs#yPuyF7~w&i~2u0KvQNi
m^yGq4VP+nUFMAsl2ugzRkeGpbAcuCW33!fkxfbK{HJc0V1*&`<O7j+Z_>1PQaKAw3A1A!NLFC8=eTE8UHHa?Uql!jO;S;XDxs3o
m#XmE7vH)3GfsB6^la*1el!pOr@9`EM<Zt!RbW44=XoY~dTYV>O9i_Q-sBio$927^I`#M>W@e9^X~B`Z53`skRdWubD9$Sn$cF&p
hpq5@b`U)idYLE$no=z~w9Oe&Z_*&|IU#=dC`=9tx(&58Dg_BwF`7CYsYUp%Y21BJpm6fGR))z{i96vAlOH0X+iA~on%AEB{H_I1
Y@xOlCURtw+PL>jg&t>J$zny?heYIgf#8Fc*$Z&#mBIs26mG&p(|Mr<YhrES!mFz;kGr_x{e$iCBL}kd;V3F9<JM`Vi&Fy+S<Ho?
y5>dzW+>69IHGyNP(ak|2Ji^W<*4SzX48ywrEjmr(d0M?ZbvgdVTA<AkHG)C&P9W$>0#sJA^4NXA0|gm_y8U+xo>pdYTq=9=4d0P
-;&@PWdBnO<Gr*?8<_w{Ok>B10}>b0wus?!r$b1m_;L3kL{~gtkaeolb$-a!iW#R}4%Q|T?HkRP9aF^~b~JBMh@f9FRRObOKXL{^
0u?_9ctO17bNKrVJqxy?1H4q)7zHQQeOM$aB1Ac69!uEs&V1d4=S7Pl5?bmF{5BFcziRLgl4kAEEdCs$Dl9+}AN;o}HSG`uAU#Qb
f<=0oy+GR{Uvtli`KnbW9qZhQvqt(SZoHgYoe3D-yS$a3Ant86!ZZZAFEZ1)w08vM`aPG*K&5Dbs~LEf5b-=eaG!n*=tWNH8CI-`
#10%JB^2K((X8P?xl*2=t^`1Ceb9eattqAm;DEH|+EzG^$gG$#Kt_HGv4pimc;&R+*SV;RLPN4+<RtfGc~nQzk%3^>9nafy;$heb
=T2NM#W1G?;ft%952CpJS!&jk%sb~6Nr*!b638<r*rVs^%Twp&Q5>Q~(w4xu@~bqR6xcA0svjbjV2(_IjYD<6E+Is~BVBwok}g=i
wxUxmn)U1=S_u2dx+-;c7v)G%;q+@tdSK?+#chmgQDHREo+E3X#AIK<{J9idz;|x>>W`?hvmv!P;x3ogh&vb|xkX_7qT@X>#nc;F
7EN~RW%ehGuGK(FbUh*21a$DMhG&hLz=IVlB6~~1_{A20Y4S4`$ND?yo@FvC3GxzGiX@TS=5qX-*6E0|`gcw_o)1HJFv-vE+YyB|
-jZ4faA@Sd%*4Q{zO=sbb_Zj8ZnS^-QuzzbYmt)eFckn7U@bA{fWEK16tRlFJw;^OE+kyRXBJ*7^$MBW@v3GPONq|KO5+Gbhsyl?
Geo1TA=W3>kl|5lLu*0Unpk0og#@1a%9%q(ZX>5~3g%4>_&K*l0B#>{dLm@kz+rmz=G_CW-Qh-TObfWdqCdz}D3>^IsxfspIBM;*
@Rjj#$_`|aM`P*Z|C1ad$DiIVdvGub*LTSPXNR9l7B5n|UjDZMD2dn+;1r!p2(YoFqgIOULh>pQ1vzA}BWhL6h!{{B8ffEODi)-7
WaGM9qzMaQ@K>9d%~qt{5YRdDW%K7h3qx(qJA5fUO8|g}N+~do=ny(Al{?6wsPVKAU)tGEahj5~s2SouJ*sN6+R2_fl~d0`$;V;#
Fd-l+=)+rM^yKDoZIpK5hmEe5y$gXKoA4}w@eI|JhR>d=M#N|rf<o^;FBMZ;4ncKM_z2kbdenL#tPA-=m-Xh9s32(`pl`4?t*ouh
u?z=N*$q+{j)v-&VDD5Q4O6ZTb-Q2UnWY(06ooVhemu=6X;}%hE)a%awGvnxG)I@L1KCfab-hru;%7@UB&a1VfZwZ5%pm{U;&<g5
463@1CKz=qOki0+oIv2FXaMbdk5xp&iFjaYF;vti_kQW~!pH>AuF40nzAV1i70t+|kN?v=>~k1w7BB*DYC?l59@lnQM4*pbHkx0o
bz6gH&ba^yN^_1F>AkAWWZaw!`M|;n|6$1EtQIjuIy09$HH#GKl!`_qrNWqBt>&86;+7kR^V4=ntrW-3!jtCPD7Ia7ij^G!tB)<b
^u_xTSV<Ol1Sv<ba%Uz~#fSZo?>514Ol{tYiI*n9Ei_*<M^yxH6seB7`e!+^j$n!OT^@^r1gR%ir`tp6=&y*dq|!I1`f_AKaZo!&
OdrBAT0A|>m#Y>VOX9_=(J=koeIQ(|uZj(@?o)&r*hIP})^^k}=SrpzIPO)YD%Ltk*<~6cV%SCLUD9Jx&PMazjW}IlB-z+qvum$X
XzB)MPKE(9{h;KL0Frx=DM9J^n~(&0TI6)#qhB<8;hWVz6zq1&NC4SS@)&WzHK-}j?IY|0Z9PPr#-gHaBY9r03M=6_$D}9oY?02q
Lm&95{=tG-$W2?%HEn(j4@h-RoyEx~SL_cSoMZP$oYhIprfg2j{yOy4g8nw?)ii+2jtN}5w9V&zr3sU9#n4?>PzEEBDejdV9D8te
XSQ$f<%M!4?Ti|3<dV{ydR$NUt?z~FF_c7kSh5(eF^T~Sb{=k(grsMJ{xqbmheZsWxVxkOF9rU7_Ah}=g}R9pPo6;8QCW0aC*u`A
V|6{l+%eOOlf!RpGLL!(6bD;^p|x;nv{$4n(Y5Bwc&T;($AndlY@iNvGAV8Tg7yI|A>8cl0mBFX&2MbZ3a5hyX)*L>nMXQ1dVgrw
G6L|g))E|Yx`zMVQG2oD=vSgPbiC~m8`Qt#Ufu>51ar{`(Z#%gu<vhTqB7~+*SJ7_?DbVbcvm`K4Zd2M-AXzN`r+KO9fN3wql@3j
y(2EM3^=)4W8PV3vv}<<uOV&8YsI-kKIk}uhUi7wpYE2hHmv6!AE%;1W(8xMInewL5r4LB8^3@yF~Z=^r&@`#4N$6AXn8x@*^z|R
qmK>g@^y1@^)guC%_Zt&VkzzB3RSE;w3<ara{r>vtP_F=o#`AOl56i{HZlr4PVA&_NgHXwnL+x&G!Inid#GEiN^lay{}p$QrPU2#
{2<$c5{WDGbz48L=UEMAdI@GAeikY?04Tjr1qtZLqHHm6xQOs73<nur++^n1c5WwZj1!@xWpKP{=Uv!HL{`@J(CoOpijutX^Th8P
iPY*0=74Uh!U&zmiHc)0^4$B1RSZ-LCCz%Fyv=2#3s>*#T|Gd^HH)r$f@)R;QObU@*3(J-|4wBX);oc71zV=UC#lsS37C8$kD$zG
vspQ@B~}4~&B)Pv(QttDL$gDK$d%n-{~m8YoPB1pHV87~dm1rx1t2vRJ%R>&QJabFpPg<^0gO#|b%VKGc;u@G7Fk4G--p&Y(cj(+
VA244pmF=Vu@l+%wo+SOvRmb-lq-gZPAC$Ak01V!&j;@djK2EsrH%A^T{N+)WFoq11>XMfLg^NKkd5tI?VD(r{wmcP#H_7tZQeA&
Va>nvqS};lBWi>A2=fbx%c?FLAoW9tbxv5#AXDn=MhD<w8JI*z#W3jZNdQcAWC6Q<gf7RL;R`1fT6P((IwSA23!48uK?MNj^cHeE
@C4U)d^dbee}?&^CBcjNa(Hs2*=E~IEG~6NDOZF@cr={<wCnttoQhTn?chHh7&-t8Y95u&(2gWo1B2SsxYpL%uL65R@w4F2(uK~~
CMY;oQLIAa5z=vlLa?#BLuxPj__=Vz3CN50?f7q*(&@)%th89F{<FzsP#DB0qeXi>oEV1Qq2^<L)+G(42f50dluip8oK@pGw*b;f
w^mO8%vV+@uQ|!8zUsh;`ET56QvhiBh)Ab$lbpqe`z;!1>q^^_0#IOsT16MCaZbcwNW761;@_{FFE8S~2;6nr?Pg|qp&_;Mw6|VF
fb3~lI>XF>cy?e5Jb5)2((51WK#g?`do<MmZB1-0-$n8*h{_@>|9?NO%y9N#6wpoei-fwTgPTo^ErCsyNtNKG%ez#_%@6bubg=Tm
i3zG5pAkD51bvcQ#b{eYQ3E!I$1ujtvb9+)BR6XjfTAbKzs=v=j>_F=Mb~K`CLQY|rUNi`a}xkty-Q|JCL2!-38TEPTPd3JmQUH<
G1q==blql4!QVEDFpNvqIHAQPqSV3^Zh8<k1J=RL)Zy5`?|6thd+<FRbzDZs0s(_JjY1W<4)Bn4!UmnW`!V!}U0gT+*>r=E_Rjkf
<=+t9DALUA2=b$%(@!pvu(b;qX@By6j22B}4>@34rgWLLJ%u|<!@ryf2xBL4s8_1CD1zZLsPHM*8cz|B;Z--YtX893wT3yd;^$l~
!d(rK;XZQC9r$%oBg@7L=m`J-000009P|nwA{f;L00Hr5lluVx23GbtvBYQl0ssI200dcD
"""
b=''.join(B.split()).encode('ascii')
assert len(b)==16670 and hashlib.sha256(b).hexdigest()=='850bc4bc8541284b3f5a0d0d4254be3827ddcad65f80495734dc21218f11b15b'
r=lzma.decompress(base64.b85decode(b))
assert len(r)==32147 and hashlib.sha256(r).hexdigest()=='29ae72db8272ba0d1dfa3162377a26700b8aba70cc4d7267afcf274874ad56b9'
sources=json.loads(r)
MANIFEST={'trace_bound.py': [10100, '24a61369a3a894cab668371f9c95f1859946218315071f47e879af6ba7e16bce'], 'independent_trace.py': [2195, '9792f5678ff5eb25f9802cb7a34d9ed1e5fa7b163d4a0484a7dbb1eeb8b03cfd'], 'cap7_6.py': [16484, '7bd3464dd5e8ba0aa3e7737a879820a921010749fc5ead3cbce90e0b432fb55c'], 'independent_7.py': [2656, '514c9e63094c74c0b168a12d64f5a044809a14d9b16e3c481061127d901dbd0b'], 'trace_bound_report.json': [15721, '822cbc7fdc41331cff2553892511a7451a5d08207a808fb82ccc7ca963986a2b'], 'cap7_pd_ledger.json': [535760, '0231bb8d5d044cbf48dd9635003c40a08bf62389698dc4ee3848e677d718aa79'], 'cap7_proof.json': [4584, '7f5c2625d6d2745806122db0c3fb3d88bb04d24d2cb9823c931da619f1250238']}
assert set(sources)=={'cap7_6.py','independent_7.py','trace_bound.py','independent_trace.py'}
for n,s in sources.items():
 d=s.encode('utf-8');assert [len(d),hashlib.sha256(d).hexdigest()]==MANIFEST[n]
 Path(n).write_bytes(d)
for n in ('cap7_6.py','independent_7.py','trace_bound.py','independent_trace.py'):
 subprocess.run([sys.executable,'-S',n],check=True)
for n,expected in MANIFEST.items():
 d=Path(n).read_bytes();assert [len(d),hashlib.sha256(d).hexdigest()]==expected
print('NOVA24_ACTUAL_TRACE_CAP_F9_RECOVERY_PASS')
```

## 9. Complete recovery for the new reciprocal-trace finite algebra

Save the following exact source as `pair_trace_exact.py` with UTF-8/LF and final LF; run `python -S pair_trace_exact.py > pair_trace_transcript.txt`. There are no arguments, random seeds or external dependencies. The analytic input is Borell's theorem and the proof in Section 6; the script does not purport to formalize that theorem.

Source: 2983 bytes, SHA-256 `011737e8883520dcd69d8472d33c3c4c14a1e1054cac374a6e33518db55babe6`.

Generated `pair_trace_exact.json`: 586 bytes, SHA-256 `5469fb96a0e36b8ba4326310f4e51344aec77bd813e2fc71a8d9c2e5f6edeadf`.

Transcript: 232 bytes, SHA-256 `6245f297d93998e597d5cef30b3dad1357ae33253505c6c12b7147b21b7760dc`.

Expected markers:

```
PROJECTIVE_VOLUME_AND_WEIGHTED_FACET_JACOBIANS_PASS
HARMONIC_CHORD_INTEGRAL_IDENTITY_PASS
NOVA24_RECIPROCAL_ACTUAL_TRACE_FINITE_ALGEBRA_PASS
```

The second clean execution reproduced both output and transcript byte-for-byte.

```python
"""NOVA24_RECIPROCAL_ACTUAL_TRACE_V1: finite algebra, not a BBL formalization.
CPython 3.13.5, standard library, assertions enabled. python -S pair_trace_exact.py
Independent mathematical parent: NOVA24_ACTUAL_TRACE_CAP_F9_V1;
immutable ancestor minimum-0021,
5eba4891ccbcf0917f0390ff3e42f18b1fcd040b72f92a3a7fc8a18f1b2a6557.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib,json
assert __debug__
# Laurent polynomials in (s,z,r): exact inverse projective coordinates.
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,u in p.items():
        for b,v in q.items():
            k=tuple(a[i]+b[i] for i in range(3));out[k]=out.get(k,F(0))+u*v
    return {k:v for k,v in out.items() if v}
def diff(p,i):
    out={}
    for k,v in p.items():
        if k[i]:
            h=list(k);h[i]-=1;out[tuple(h)]=v*k[i]
    return out
def det(A):
    ans={}
    for p in permutations(range(len(A))):
        x={(0,0,0):F((-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p))))}
        for i,j in enumerate(p):x=mul(x,A[i][j])
        ans=add(ans,x)
    return ans
u={(1,0,-1):F(1)}
v={(0,0,-1):F(1),(1,0,-1):F(-1)}
w={(0,1,-1):F(1)}
jac=det([[diff(x,i) for i in range(3)] for x in (u,v,w)])
assert jac=={(0,0,-4):F(1)}
# On u=0, v=1/r and w=z/r; dv dw has absolute Jacobian r^-3.
v0={(0,0,-1):F(1)}
bjac=det([[diff(x,i) for i in (1,2)] for x in (v0,w)])
assert bjac=={(0,0,-3):F(1)}
assert mul(v0,bjac)==jac
# In variables now named (s,a,b), verify the antiderivative
# s/[a*(a+(b-a)*s)] of 1/[a+(b-a)*s]^2 by its cleared numerator.
s={(1,0,0):F(1)};a={(0,1,0):F(1)};b={(0,0,1):F(1)}
L=add(a,mul(add(b,scale(a,-1)),s))
assert add(L,scale(mul(s,diff(L,0)),-1))==a
# Therefore integral_0^1 L^-2 ds=1/(a*b), also when a=b>0.
frustum=(F(132,119),F(51,77))
assert frustum[0]>1 and frustum[0]*frustum[1]<1
report={
 'identity':'NOVA24_RECIPROCAL_ACTUAL_TRACE_V1',
 'inverse_coordinates':['s/r','(1-s)/r','z/r'],
 'volume_jacobian':'r^-4','weighted_boundary_jacobian':'r^-4',
 'section_concavity':'A(s)^(-1/2) is convex; Borell in dimension two',
 'harmonic_chord_integral':'1/(a*b)',
 'parallel_area_gap':'(sqrt(A0)-sqrt(A1))^2/3',
 'same_actual_frustum_pair':[str(t) for t in frustum],
 'same_actual_frustum_pair_product':str(frustum[0]*frustum[1]),
 'analytic_conclusion':'Lambda_ai*Lambda_ia <= 1',
 'all_nine_facets_excluded':False,
 'C32_attainer_found':False}
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
Path('pair_trace_exact.json').write_bytes(data)
print('PROJECTIVE_VOLUME_AND_WEIGHTED_FACET_JACOBIANS_PASS')
print('HARMONIC_CHORD_INTEGRAL_IDENTITY_PASS')
print('pair_trace_exact.json',len(data),hashlib.sha256(data).hexdigest())
print('NOVA24_RECIPROCAL_ACTUAL_TRACE_FINITE_ALGEBRA_PASS')
```

## Final scope and continuation

The eight-facet problem is closed by the actual-volume trace theorem and the replayed finite cap lemma. The new reciprocal trace inequality, its two-facet-volume refinement, and the base-root central-octagon exclusion are rigorous across their stated complete continuous domains. The all-nine-facet and full joint-C32 problems remain unresolved here. No sampled failure, missing source, metric cutoff, relaxed coefficient matrix, or small residual is used as an impossibility proof or an attainer.

The next substantive step is to combine true C32 incidence with the shared projective moment chart and physical reciprocal inequalities, or to construct and certify an actual nine-facet body. The old eight-facet 7/6 exterior is not a remaining branch. These are mathematical proofs with exact computational certificates for their finite portions, not proof-assistant formalizations or claims of external peer review or historical priority.
