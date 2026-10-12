# minimum-0177

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ONE_NEGATIVE_ROOT_PAIRED_WEDGE_DOMINANCE_AND_DEPTH_NORMAL_FORM_V1

## Determination

The cap-linked interface admits an exact two-piece geometric decomposition and new whole-sector value theorems. The positive clipping auxiliary is paid for together with the same negative apex; it is not deleted by assuming that clipping stays root-only.

For exactly one negative root vertex, with `0<b,c,d<a`, I prove the requested strict comparison

```text
T(P) < max(2,T(Qroot)),  Qroot=conv(T0,F intersect {z>=0}),
```

throughout an explicit same-body volume/angle sector, including both of the following complete classes:

* The endpoint sector `b+2min(c,d)>=a+max(c,d)`, with arbitrary root polygon and negative depth.
* The coordinate-monotone negative extension sector defined in §5. It includes full unbounded-depth families outside both the preceding endpoint sector and the parent's endpoint-dominance sector.

In each of these classes, the inherited octant theorem then gives **`T(P)<203/100`**. Separately, a steep-direction sector, `(1-c/a)m>=354` in the D-oriented notation below, satisfies **`T(P)<51/25`**, without claiming the stronger deletion comparison there.

The entire one-negative-vertex comparison is **not yet proved**. Its remaining geometry is sharply specified below. The exact depth polynomial has a strictly positive quadratic coefficient on the whole low-endpoint domain. Thus the genuinely unresolved high-trace comparison reduces to the sign of a first coefficient for an actual positive root body and an admissible root direction, rather than to independently completed cap moments.

The starting authority is literal `minimum-0175`, SHA-256 `7fdabeeb8e9da0f3dde099dfe8da71f49287ef9d85d5ba6e17d4742f24a32bdd`. Its pyramidal-cap erasure, and its warning that a B-negative-root edge creates a positive-ell clipping vertex, are used at their stated scope. The newly supplied A-cone material is used only for the additional location inequalities in §8, not as a substitute for a body. :contentReference[oaicite:0]{index=0}

## 1. Actual bodies and normalization

Set `a=1` and

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b,c,d<1,
alpha=1-b, delta=1-d, epsilon=1-c,
ell=1-delta*x-epsilon*y-alpha*z,
n=(1+b+c)*x+(1+b+d)*y.
```

Let `F` be a compact convex positive-area root polygon in `{ell=0,x>0,y>0}` with exactly one negative-z vertex `p`; all other root vertices have nonnegative z. Put

```text
Fplus=F intersect {z>=0}, Q=conv(T0,Fplus), P=conv(T0,F),
V=int1, J=int(x,y,z), E=int ell, N=int n,
g=J/V, T=N/(6VE).
```

Every integral is original uniform volume. Each changed body has its own recomputed `J` and centroid. Neither centroid preservation nor an equilibrium census is assumed.

The main polygonal statement extends by approximation to `F=conv(Fplus,p)` with convex, possibly curved `Fplus`, positive x and y, and the same nondegenerate zero-height root segment. There is no bound on the number of positive root vertices. Proper `ABC/ABD` is retained throughout. Enlarged coordinate-face closure is not silently identified with this class.

Write `p_z=-h`, `h>0`. Let `[R,S]=F intersect {z=0}`, ordered by `r=R_y<s=S_y`. Then

```text
R=((1-epsilon*r)/delta,r,0),
S=((1-epsilon*s)/delta,s,0),
0<r<s<1/epsilon,
K0=Q intersect {z=0}=conv(A,D,R,S,C).
```

Denote the actual base area, centroid and means by

```text
A_K=area(K0), kbar=mean_K0 (x,y,0),
gamma=3mean_K0 ell, nbar=mean_K0 n,
t=6V_Q, M=4E_Q/V_Q,
n_D=1+b+c, n_C=1+b+d, n_R=n(R), n_S=n(S).
```

These data are recovered directly from the actual base:

```text
2A_K=(1-d*r+c*s)/delta,
gamma=(1+c-d^2*r+c^2*s)/(1-d*r+c*s),
3nbar=[r(n_D+n_R)+(s-r)(n_R+n_S)/delta+S_x(n_S+n_C)]/(2A_K).
```

In particular `A_K>=1/2` and `gamma>=1`.

## 2. The genuine visible wedge

The unique possible positive-ell clipping vertex is

```text
q=(p_x/(1+h),p_y/(1+h),0),
beta=ell(q)=b*h/(1+h) in (0,b).
```

The section identity is `P intersect {z>=0}=conv(Q,q)`. If `q in K0`, the parent's pyramidal-cap theorem already gives the desired comparison with `Q`.

Suppose `q notin K0`. The containing root triangle

```text
conv(A,D0,C0), D0=(1/delta,0,0), C0=(0,1/epsilon,0)
```

differs from `K0` by exactly the two corner triangles `DD0R` and `CC0S`. Since `q` has positive coordinates and `ell(q)>0`, it lies in the interior of exactly one. Reflect x and y, and c and d, so that it is the **D corner**.

Define

```text
m=(r-p_y)/h,
w=((alpha+epsilon*m)/delta,-m,-1),
p=R+h*w,
eta=[d*m+(d-b)*r]/(6delta)>0.
```

Convexity of the original root gives the genuine support condition

```text
y_u>=r+m*z_u  for every u in Fplus.                       (2.1)
```

Indeed the intersection of `[p,u]` with `z=0` must lie on `[R,S]`. The strict corner condition is `m>(b-d)r/d`. On the root, the plane through `B,D,R` has retained inequality proportional to

```text
y-r-[(b-d)r/d]z>=0.
```

Condition (2.1) proves that this plane supports `Q`; every positive-height root point is strictly on its retained side. Thus **BDR is a genuine maximal triangle of Q**, not an integration triangle being moved independently.

To check that there are no omitted visible facets, first note that the tangent cone of Q at A is the positive octant: its only incident facets are the two coordinate triangles and K0. A remaining nonroot facet meets the root in a root edge or vertex. Every inherited root edge, and the normal cone at every inherited positive-height root vertex, also supports the original F, so its facet cannot see p. The only new root normal directions are at the cut endpoints R,S. A nonbase facet using only one such root point must contain a canonical pair. The pair CD lies in the base plane; among the B pairs, the base supporting edges permit only BDR and BCS. The D-corner position satisfies the BCS halfspace, and p-B=(1+h)(q-B) preserves its side. The only facets of Q strictly visible from p are therefore K0 and BDR. This argument also covers coplanar original root-edge contacts: R may have been an integration point, rather than a vertex, of the original P.

Consequently, up to measure-zero interfaces,

```text
P minus Q = conv(p,K0) disjoint-union conv(p,B,D,R).       (2.2)
```

The full linked tetrahedron has volume `j=h*eta`. Its positive part is exactly `conv(q,B,D,R)`, with volume `j/(1+h)`; its negative part has volume `jh/(1+h)`. In particular the negative cone over K0 is **not** the whole negative cap when the clipping auxiliary is present.

For example the positive wedge has original moments

```text
V_wedge=j/(1+h),
E_wedge=V_wedge*(b+d+beta)/4,
N_wedge=V_wedge*[n_D+n_R+n(p)/(1+h)]/4.
```

Adding its negative partner gives `E_tetra=j(b+d)/4`. The beta terms cancel through the actual collinearity `p,q,B`, not through an independently selected mass.

## 3. The exact original depth polynomial

Keep Q and the root direction w fixed. Put

```text
a_n=n(w)=[alpha*n_D+(d-c)(b+c+d)m]/delta,
V1=A_K/3+eta,
E1=A_K*gamma/12+eta*(b+d)/4,
N1=A_K*(n_R+3nbar)/12+eta*(2n_R+n_D)/4,
N2=a_n*V1/4,
J1=A_K*(R+3kbar)/12+eta*(2R+B+D)/4,
J2=V1*w/4.
```

Actual coning and the genuine visible tetrahedron give

```text
V(P_h)=V_Q+hV1,
E(P_h)=E_Q+hE1,
N(P_h)=N_Q+hN1+h^2N2,
J(P_h)=J_Q+hJ1+h^2J2.                                    (3.1)
```

Here `P_h=conv(Q,R+h*w)` and its root is the convex hull of **the complete Fplus, including R and S**, with the new negative apex. Replacing the old negative vertex while dropping a retained cut endpoint would be a different family and need not preserve Q.

For the actual input depth h0, every `0<h<=h0` is admissible: the new apex lies on `[R,p]`, and the original nonnegative root cut is retained exactly. More explicitly, admissibility requires positive apex coordinates and

```text
h*(y_u-s-m*z_u)<=(s-r)*z_u for all positive-height u in Fplus. (3.2)
```

Together with (2.1), these conditions are sufficient to keep the cut exactly `[R,S]`. The D-corner condition implies `w_x>0`. Thus the coordinate restriction is only `h<r/m` when `m>0`; when `m<=0` there is no coordinate upper-depth bound. Equality in (3.2) is an allowed incidence wall. The domain is unbounded when `m<=0` and every coefficient `y_u-s-mz_u` is nonpositive.

Define

```text
C1=A_K[2t(gamma+M)-n_R-3nbar]/12
   +eta[2t(M+b+d)-2n_R-n_D]/4,
C2=V1*(12E1-a_n/4).
```

Then exactly

```text
12V(P_h)E(P_h)-N(P_h)
 =[12V_QE_Q-N_Q]+hC1+h^2C2.                              (3.3)
```

Equivalently, the original two-cross increment is

```text
12[V_Q(E_P-E_Q)+(V_P-V_Q)E_Q+(V_P-V_Q)(E_P-E_Q)]
 -(N_P-N_Q)=hC1+h^2C2.                                  (3.4)
```

## 4. Universal strict positivity of the quadratic coefficient

**For every admissible D-oriented one-negative-root configuration with `0<b,c,d<1`, `C2>0`.** This does not assume stationarity, high trace, or a small root collar.

Let

```text
Z0=1+c+b^2+bc+2c^2(s-r)
   -(d-c)(d^2+cd+bc+b^2)r/d.
```

Direct algebra yields

```text
4delta*(12E1-a_n/4)
 =Z0+6delta*(bc+bd+c^2+d^2)*eta/d.                        (4.1)
```

For `c>=d`, Z0 is already the sum of the positive constant `1+c+b^2+bc`, `2c^2(s-r)`, and the nonnegative term obtained by replacing `-(d-c)` with `c-d`.

For `c<=d`, its exact positive decomposition is

```text
Z0=delta*(b^2c+bc^2+d^2+d)/(d*epsilon)
   +2c^2(s-r)
   +(d-c)(d^2+cd+bc+b^2)(1/epsilon-r)/d.                 (4.2)
```

All denominators are positive, including on `c=d`. These two identities prove strict positivity on the full domain. The symbolic source verifies them as identities, not by sampled evaluations.

## 5. Whole comparison sectors

### 5.1. A same-body area, volume and direction test

Put

```text
L=n_D-2t(b+d),
Rcap=2A_K(gamma-b)+gamma-1>0,
theta=3eta/A_K
     =Vol(conv(p,B,D,R))/Vol(conv(p,K0)).
```

**Paired-wedge dominance theorem.** If

```text
theta*L <= Rcap,                                        (GUARD)
```

then `C1>=0`, and hence, for every positive admissible depth,

```text
T(P_h)<max(2,T(Q)).
```

The guard is independent of h along the entire admissible ray. It is not a fitted ratio of unrelated regions.

To prove it, let `Q0=conv(B,K0)` and `k0=24E(Q0)=2A_K(b+gamma)`. The actual five-point hulls inside Q0 give `n+ell<=k0` on K0, in particular `n_R<=k0`. Applying a planar A-fan to the nonnegative affine function `k0-n-ell` gives

```text
3nbar<=2k0-gamma+1.
```

Also `V_Q>=A_K/3` and `E_Q>=k0/24`. Substituting these bounds in the **exact** C1 formula gives

```text
C1 >= A_K*Rcap/12+eta*[2t(b+d)-n_D]/4
   =A_K*(Rcap-theta*L)/12.                              (5.1)
```

Strict positivity of C2 now makes (3.4) positive. Writing the full denominator as the Q denominator plus its positive cross increment expresses T(P) as a strict subconvex bound between T(Q) and 2.

### 5.2. Entire endpoint and volume sectors

The guard is automatic if

```text
2t(b+d)>=1+b+c.
```

Since `t>=1`, it is automatic throughout `b+2d>=1+c`. Reflection covers the C corner. Therefore, **independent of which corner is visible**, every one-negative-root body in

```text
b+2min(c,d)>=1+max(c,d)                                  (ENDPOINT)
```

satisfies the desired comparison. In the original normalization this is `b+2min(c,d)>=a+max(c,d)`.

The full actual-volume sufficient condition is

```text
t>=[1+b+max(c,d)]/[2(b+min(c,d))].
```

The endpoint sector is not a consequence of the parent's low-endpoint `b+c+d<=1` condition: its interior has `b+c+d>1`.

### 5.3. All coordinate-monotone negative extensions

The guard is also automatic whenever **`m<=0`**, equivalently `p_y>=R_y` in the D corner. This is a complete unbounded geometric sector, for all low endpoints. In the reflected C corner the condition is `p_x>=S_x`.

Here is an elementary global certificate. The corner condition and `m<=0` imply `b<d` and

```text
theta <= (d-b)r/(2delta*A_K).
```

If L is negative the guard is immediate. Otherwise use `t>=2A_K` and define

```text
Z=2delta*A_K=1-dr+cs,
H=Z*gamma,
F(b)=Z(H-bZ)+delta(H-Z)-delta(d-b)r(1+b+c)
     +2(d-b)rZ(b+d).
```

Then `delta*Z*(Rcap-theta*L)>=F(b)`. At fixed actual base geometry,

```text
F(b)=(1-b/d)F(0)+(b/d)F(d)+r(2Z-delta)b(d-b),             (5.2)
F(d)=delta*Z*Rcap evaluated at b=d>0,
F(0)=Z^2+delta*c*S_x*(Z+delta)
     +dr[(1+d)Z-delta(d+c)]>0.
```

Indeed `Z>=delta`, so the final bracket is at least `delta(1-c)>0`. All terms in (5.2) are nonnegative. Interpolation in b is solely an algebraic proof of this inequality; no endpoint-motion reaction or zero-endpoint body theorem is imposed.

### 5.4. A positive critical slope

When `L>0`, the guard is exactly

```text
m<=mcrit,
mcrit=[2delta*A_K*Rcap/L-(d-b)r]/d.                      (5.3)
```

The preceding argument proves `mcrit>0`: for `b>=d` this is immediate; for `b<d`, the strict m=0 certificate proves it. Thus a whole nonempty interval of actual directions, not merely a small-depth neighborhood, is closed.

### 5.5. Value corollaries

Whenever one of these comparison conditions holds, the proper positive-octant root-only theorem of J55 gives `T(P)<203/100`. If Fplus has zero area, both Q and the actual Pplus are B-pyramids over their respective zero-height bases, with trace below two; the original one-negative-cap theorem therefore gives T(P)<2 on that boundary directly. Positive root area is not presumed after a degenerate clip. The inherited J55 theorem is used only for the genuine root-only Q. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## 6. An additional steep-direction value theorem

A separate original-body estimate closes an unbounded part of the remaining m>0 sector.

**Slab lemma.** Suppose every non-B generator of a proper body containing T0 has `-h<=z<=zplus<1`, with `h,zplus>=0`, and ell is nonnegative on the body. Then

```text
T(P)<2(1+h)^4/(1-zplus)^7.
```

If `h+zplus<1`, the simpler bound is `T(P)<2/(1-h-zplus)^7`.

For clarity, this is a comparison between actual pyramids, not uniform projective refilling. Let Omega be the convex hull of the B-projections `(x/(1-z),y/(1-z))` of the non-B generators, and let `R0=conv(B,Omega times {0})`. The B-homothetic pyramids with factors `1-zplus` and `1+h` satisfy

```text
Rinner subset P subset Router.
```

Put `nu=b*zplus/(1-zplus)`. On R0, the affine function `ellhat=ell+nu` is nonnegative. Its corresponding numerator is `nhat=n+3nu(x+y)>=n`. The actual base-pyramid theorem gives `That(R0)<2`. Original affine scaling gives

```text
V_inner=(1-zplus)^3 V_R0,
E_inner=(1-zplus)^4(E_R0+nu V_R0),
N_outer=(1+h)^4 N_R0.
```

Use `V_P>=V_inner`, `E_P>=E_inner`, and `N_P<=N_outer`. The outer carrier is allowed to have negative ell; no trace is asserted for it. For the combined-height estimate, `1-zplus>=(1-h-zplus)(1+h)` suffices.

For the D-oriented root geometry with m>0, (2.1), the root equation and positive x give

```text
h<r/m,
zplus<(1-epsilon*r)/(alpha+epsilon*m),
h+zplus<1/(epsilon*m).
```

Therefore the **whole sector `epsilon*m>=354` has `T(P)<51/25`**. The exact numerical certificate is

```text
2(354/353)^7 < 51/25,
51/25-2(354/353)^7=22080495738387/17075087834907018425>0.
```

This proves a value bound, not the stronger Qroot deletion inequality. The constant 354 is a sufficient integer threshold for this estimate, not a claimed optimal geometric cutoff.

## 7. Exact remaining one-variable question

For any `tau>=max(2,T(Q))`, define

```text
a_tau=C2+6(tau-2)V1E1>0,
b_tau=C1+6(tau-2)(V_QE1+E_QV1),
c_tau=6tau V_QE_Q-N_Q>=0.
```

Then the exact actual-body threshold test is

```text
T(P_h)<=tau iff c_tau+h*b_tau+h^2*a_tau>=0.               (7.1)
```

In particular, when `T(Q)>2` and `tau=T(Q)`, a negative `b_tau` would produce **actual counterexamples at every sufficiently small admissible positive depth**, namely `0<h<-b_tau/a_tau`. Conversely any comparison failure on this ray forces `b_tau<0`. The new quadratic-positivity theorem therefore reduces that part of the problem to a genuine first variation at the root/base boundary, without assuming stationarity.

When `T(Q)<=2`, the discriminant and the admissible depth interval must also be retained. A negative first coefficient alone is insufficient, as the exact control below shows.

Any failure of the desired comparison in the D corner must now satisfy all of

```text
L>0, b+2d<1+c,
m>mcrit>0,
theta>Rcap/L,
C1<0,
0<h<min(r/m,-C1/C2),
```

together with (2.1), (3.2), and the exact negative interval of (7.1). For a possible `T>=51/25` body, the steep-direction theorem adds `epsilon*m<354`. These are restrictions on one actual positive root body and its actual direction, not a declaration that arbitrary scalars satisfying them are realizable.

No actual counterexample to the full `max(2,T(Qroot))` comparison was obtained. The sign of the remaining first coefficient above trace two, and the low-Q discriminant alternative, remain unresolved.

## 8. Connection to the supplied A-cone location theorem

For every one-negative-root body here, scale root coordinates by `(X,Y)=(delta*x,epsilon*y)`. Every Fplus point lies in the unit triangle, while the sole negative apex satisfies `X_p+Y_p=1+alpha*h`. Thus the actual A-projection polygon is exactly

```text
conv((0,0),(1,0),(0,1),(X_p,Y_p)),
kappa=2Area=1+alpha*h.
```

This specializes the supplied location theorem to an exact identity, rather than a free top-density coefficient. Its moment inequalities become

```text
24alpha*delta^2*epsilon*Jx(h)<=(1+alpha*h)^2,
24alpha*delta*epsilon^2*Jy(h)<=(1+alpha*h)^2,
24alpha*delta*epsilon*[delta Jx(h)+epsilon Jy(h)]
 <=(1+alpha*h)(2+alpha*h).                               (8.1)
```

By (3.1), all three are explicit quadratic inequalities along the same original depth ray. The exact body auditor checks them. They are available for the remaining coefficient problem, but they were not assumed sufficient for realization or used to claim an unproved threshold closure. :contentReference[oaicite:3]{index=3}

## 9. Exact controls, including a failed stronger implication

### A. A raw deletion countercontrol below two

The attempt to prove `C1>=0` for every actual one-negative-root body is false. Take endpoints

```text
b=1/5, c=9/10, d=1/100
```

and canonical vertices 0=A,1=B,2=C,3=D, followed by the root vertices

```text
4=(98/99,1/5,0),
5=(24599/24750,4/25,1/20000),
6=(1,1/10,0),
7=(13757/13750,19/200,-1/200000).
```

The actual maximal facet cycles are

```text
(0,1,2),(0,3,1),(0,2,7),(0,7,3),
(1,4,2),(1,3,7),(1,5,4),(1,6,5),(1,7,6),
(2,4,7),(4,5,6,7).
```

This is a proper `8/17/11` body with one negative root vertex and a true B-negative edge. Its original data are

```text
V=1473821/7425000,
E=229781099/2376000000,
N=71651212638827/392040000000000,
J=(845989876927/14701500000000,
   1215916831/23760000000,
   393016968257/7920000000000),
g=(13868686507/47838780000,
   1215916831/4716227200,
   1179050904771/4716227200000),
T(P)=1074768189582405/677312418218558.
```

Its Qroot is obtained by deleting vertex 7; it is `7/13/8`, with maximal facets

```text
(0,1,2),(0,3,1),(0,2,4,6,3),(1,4,2),
(1,3,6),(1,5,4),(1,6,5),(4,5,6).
```

Its exact moments are

```text
V_Q=1179001/5940000,
E_Q=11488951/118800000,
N_Q=2605282039/14256000000,
J_Q=(3075961259/53460000000,
     60795023/1188000000,
     7860006667/158400000000),
g_Q=(3075961259/10611009000,
     60795023/235800200,
     23580020001/94320080000),
T(Q)=21493576821750/13545484717951.
```

Thus `T(P) approximately 1.586813058 > T(Q) approximately 1.586770593`, but both are below two. This is **not** a counterexample to the requested max comparison.

Here `m=1000`, `eta=1109/660`, and

```text
C1=-5274029/11880000,
C2=856406/1815,
C1^2-4C2[12V_QE_Q-N_Q]
 =-38264983422697817671/426931560000000000<0,
hC1+h^2C2=-1442650321/653400000000000<0.
```

The same Q with `p(h)=(1+1120h/11,1/10-1000h,-h)` is admissible throughout `0<h<1/10000`. The negative discriminant proves `T(P_h)<2` on this entire family despite the negative first coefficient. This preserves both the failed stronger implication and the useful nonwinning construction.

### B. A full unbounded-depth sector outside the old endpoint condition

Take `b=1/5,c=3/5,d=3/10` and

```text
R=(48/35,1/10,0), S=(46/35,1/5,0), U=(43/35,3/20,1/10),
p(h)=(48/35+199h/175,1/10+h/100,-h), h>0.
```

All h>0 are admissible. There is always a genuine D clipping wedge. Here `m=-1/100`, `b+c+d=11/10>1`, the oriented endpoint guard is `-4/5`, and `L=6/25>0`; thus neither the parent's low-endpoint dominance condition nor the new volume-safe shortcut applies. The coordinate-monotone theorem closes the whole ray.

The fixed actual Q has

```text
V_Q=13/50, E_Q=9407/84000, N_Q=1093313/3920000,
J_Q=(4817/49000,11419/168000,5461/84000),
T(Q)=420505/263396,
C1=3082307/14700000, C2=6910003/39200000,
Rcap-theta*L=987487/381500>0.
```

The exact controls h=`1/1000,1,1000` all have original f-vector `8/17/11` and traces

```text
32852421653001/20583743419505,
101648211/77663531,
7943024809695/9160181341444.
```

They are retained for their unbounded geometry, not discarded for having lower trace.

### C. High-trace and boundary controls

The literal parent `8/17/11` clipping-auxiliary body now passes the paired guard, so its stronger comparison with Qroot is certified rather than merely its comparison with Pplus.

A new rational `8/17/11` control has endpoints `b=1/4,c=1/10000,d=1/20000` and root generated by

```text
e=1/10000, r0=5/6,
Root(x,y)=(x,y,[1-(1-d)x-(1-c)y]/(1-b)),
Root(e,r0-e), Root(r0-e,e), Root(e,1-2e),
p=((1+(1-b)h-(1-c)y)/(1-d),y,-h),
h=1/10000000, y=1/1000000000.
```

It has a true negative B-edge and

```text
T(P)=5197185744649517275257339196794935621128912500000
     /2561868474108315327150866656951016185503031518229
     approximately 2.028670010649,
T(Qroot) approximately 2.028670087007.
```

Its positive paired guard is approximately `0.75023744`; every exact coordinate, facet, original moment and centroid is rebuilt by the capsule. This is a nonstationary value control, not a new universal record or a mechanical attainer.

The remaining input records retain an unbounded large-D ray, the equality `b+2d=1+c`, a reflected C corner, equal c,d, an example in the whole endpoint sector, a steep-direction example with `epsilon*m=500`, and a no-negative-B-edge control. There are 15 input records, including depth values and a reflection, not 15 mechanical incidence exclusions. No S/U/H or weak-equilibrium census is claimed for these constructions.

## 10. Applicability and the useful continuation

The visible-tetrahedron theorem uses proper coordinate triangles, a root-only body and exactly one negative root extreme point. Multiple negative vertices, positive-ell original auxiliaries, or enlarged coordinate facets require another decomposition. No integration triangle is varied as though it were a maximal facet.

All main denominators are explicit: `delta,epsilon,d>0`, `h>0`, and the B-projection denominator `1+h>1`. The formulas have no division by `c-d` or `b-d`; both equality walls are covered. The wall `eta=0` is the no-extra-wedge boundary. Coordinate-zero endpoints and b=1 are algebraic limits, not extensions of the stated proper positive-endpoint theorem. Root-cut degeneracy and the absence of positive-height root area are handled separately as above.

The main comparison proof uses neither full joint stationarity nor the inherited high-trace endpoint, volume, J, or height-law relaxations. The separate high-endpoint negative-z theorem remains an accepted earlier result, not a new replay or a consequence of this work. :contentReference[oaicite:4]{index=4}

The most useful continuation is the exact actual-body coefficient problem (7.1) in the residual `m>mcrit` sector, using the genuine supporting inequality (2.1), retained cut endpoints, and the quadratic A-cone constraints (8.1). A negative above-two coefficient would immediately give a recoverable actual counterexample family; proving its nonnegativity, together with the low-Q discriminant alternative, would finish the one-negative-vertex comparison. Neither outcome is asserted here.

No E17 registry change, `110` construction, new minimum, or whole mechanical exclusion follows from these trace results.

## 11. Complete recovery and verification status

Save the following capsule as `recover_cap_pair.py`, UTF-8/LF with one final LF. It recovers both complete source units; no parent source, archive, external input, optimizer or random seed is required.

Executed dependencies: **CPython 3.13.5** standard library for recovery and the body auditor; **SymPy 1.14.0** for the separate symbolic identity audit. Assertions must remain enabled. The exact acceptance layer has no NumPy, SciPy, floating-point hull, or numerical positivity test.

```sh
python -S recover_cap_pair.py cap_pair_recovered
cd cap_pair_recovered
python -S cap_pair.py build cap_pair.json > build.txt
python -S cap_pair.py check cap_pair.json > check.txt
python cap_pair_identities.py > identities.txt
cmp build.txt check.txt
```

Expected terminal markers:

```text
CAP_LINKED_PAIRED_WEDGE_ALL_SOURCE_BYTES_RECOVERED
CAP_LINKED_ONE_NEGATIVE_ROOT_ORIGINAL_GEOMETRY_EXACT_PASS
PAIRED_WEDGE_POSITIVE_QUADRATIC_AND_MONOTONE_SECTOR_IDENTITIES_PASS
```

Exact pins:

```text
recover_cap_pair.py: 9726 bytes
SHA256 775187275a045f86c46a7b6cab213b5bc09d8cd8f085c7f05382ebfc08a3923e
cap_pair.py: 16009 bytes
SHA256 496a808189aaac79c7ec92bf96d498e24e28511cfd27166537b9e27fc8618182
cap_pair_identities.py: 1362 bytes
SHA256 d3849bc97a59610b910dcc8a7d942299f3f2e66cc344e616e09c6df1b6144d5d
cap_pair.json: 155647 bytes
SHA256 f1d30c8532cbd1214e98fe4036b2a7892e75b64a3c8106ee3a69f90a6b3bed9a
build.txt and check.txt: 3301 bytes each
SHA256 9f0ed6cc4e420b709f73f204e22a7b57098fdcf984ae970e98ab033d48b50aac
identities.txt: 68 bytes
SHA256 1846599b72f620572182e7b830a021bce81cbbbb69eef5c5554f853b6b61ea48
```

Normal execution and clean source-only recovery/build/check were completed. Reports and stdout matched byte-for-byte. The auditor reconstructs maximal facets and true edges, compares two independent positive interior fans, checks the visible cones against independently rehulled differences in V and the full vector J, and checks three actual intermediate depth bodies per oriented input. The slab comparisons use separately reconstructed inner, reference and outer pyramids; the outer carrier is explicitly not assigned an admissible trace when ell is negative there.

The symbolic unit verifies the full algebraic positivity identities. The continuous geometric proofs above are not inferred from the finite controls and are not proof-assistant formalizations.

Convenience copies: [recovery capsule](sandbox:/mnt/data/recover_cap_pair.py), [body and visibility auditor](sandbox:/mnt/data/cap_pair/cap_pair.py), [symbolic verifier](sandbox:/mnt/data/cap_pair/cap_pair_identities.py), [complete exact report](sandbox:/mnt/data/cap_pair/cap_pair.json). The literal capsule below is sufficient without those files.

```python
# ONE_NEGATIVE_ROOT_PAIRED_WEDGE_DOMINANCE_AND_DEPTH_NORMAL_FORM_V1
# Complete source-only recovery; no parent source or external inputs.
import base64,hashlib,json,sys,zlib
from pathlib import Path
DATA="""
c-pl*Yg6O6vVX;A&xhEK0&#$0NDx&_$gsoi1O`~{Ig?4b9NQsg65H4gBy8<}zuhg#mP43*)V(`JVoTkvR;yoXDf|0RzL&bG7
iBx?`ls$s|2F!kSMIN$hQAEX+{@v>9S+V<Z$I4)-0REBTepAt`Rerg)6M13y>q%oxbpnMNV4cYioLmUA0~^i$ksdGVxV)iE@
nw=?Cm&vI|oKycyZumfiaIJnU}4NB%ZH(hBu!ZQJgM|96E|H11ghno;(wYD=!P<!tnBY_aJ+it%kR)$Kv3fJNeJe&j+nf?tj
)HGj4u9?Hs&A@WW}~O~P>UK0FG%_H-`@!uHWoFb&@a-k~$yKkB?c45vrI`-9+M;=K!<!(jh#zccOZdwZQp5WtwzELj-S3}zK
2ac)G5G|39%qig_9jE@osnJtoJUIO{aVggbiL<y66#SEsaAg<u`TP$B@UXFe2Ax~nKuL0$hn;*@##mWz>_o3e8KvTbLaun1V
HaRuK{^^j9PT2?6XJ_MYaS%=oF9=MJO{{Jf7RxL)ie)+v%~f-4Oq0x5u{ErN@e-v3WC@&nIoXEO`Vr1zIX4UDZQvC4O5h-dC
qaXxsFBZ?3)5WL+o_A02}D0j^1Oy>dLw6SPez?_%YzSia>h(PwXv-&dYOE3u+0&@ikpzQVSY(e@Fxbtb_odj4r;jpYnJ0!w&
^SSR?95MqILx%D9x7hdB;qx?zh-Tc@BCJ24)U?q&SulO^taN!^<&u)Ho@$6RJ0#nvaBOWPCKn?^3{z)NDM@qIpOpGV8=KzyK
BR*{B7wfKQOp3dpy+VE;*KT7;MFcxf8Ofw`i0IdTTi@{tBltx*^7o8o2E#TU^e6)p=scN%4RA!q1uT*BT1AC;PlY;P=f%F>b
39XEj@(4&b2e1)sFMoF%4)z<LZ^O`)^?WlQ2h@W}!eQ0*9?!zb=L$__N@L>%f*6urGA<w~V4ez8~O~zwFMIW?9*;6bFc(Dqc
<F{O%-qiEMod5oZoI%7M*mvYX_XDP2NT6G6PfRD~LZ#5U($T{hCJg*B@%ml9lH@@F;sn@@*Jf;W{Uk1;co|~PjH7bK0=D<$&
2v5yEi0=vt27}UOFD}vHWAD^ZXYkam3Xd^L?G31((c9_ExF~e*y_!AYbFP2X?Bb)f_?x!k(9#|c7^eB0p7d_1wADG#5t^5kR
>U{afE30EcQKI^SQT}1fCIfy-9AyH2<Er3M;DB>h2M-=wBQu(dcQGfKG`;M0tQn3F(1+4N$Qv8o=qe=dXcokdF{?CxS&^fh7
r?M+A~)3B8sQAIer=H6N7`m&!+7ELRWSI(oAO(mQT<{q;^3K80Bx3Jd$rp+yXg>*B9ry1<l}0-$~e{fDpa_p#J7IXmeg5Pl3
KQ1wU)M*`@(m;<Sy1f>pZ+zW&Iy0-f3`Z5W?t}-WZZptA2HN)9Tme3}N*bW#1n2WcZ7iNt+;jS$<8e7VbL^x}he~~LE_q#{K
2rg)BF)Ufo`VUxrX{qx$na>kgUxz@1dJzYpTFWpu$yPK=rGcy#J`$YO#78kfpi)^rH8IJN0A+;yEf%g|>Ve@h0hW+(?t~A!k
WtvO_j-OfN5fFAOq)`7i*s@qG6O5va)h+Wcudk4lyf9Ln;_>Nct!TYM`>+gQG*HZDVcMOS*Up{V2@OAtsY+BLHImF$p#Qkcw
3A)#Wyj&ao6PV0&~I?;ew&r!~5<&qm%*u5^yT?0_?!bT4Ks-aZTWe0Rk<9l<Xb5U<9Njxd^>{nSq#vUlk%Hkqe1)<#l^rtO@
fujP7TU8^XNJ5hgifTR2k&Zy+RVQ@qmE%D|CGlfuN}*<L9*KC_ilZaDx0oLzzv?^Y#m<#ot#fjKqpx^9fRow25d00-;IIeue
2RC2LJ2YWStC8tRetj#ouV&DnV3l_-SU>-pj4I;nT!ORj|W-g&%HBi{E1*%EBN+pD891AIth*H$AXk5vWK*oQGC@iq@+^eqB
Gy~9S8$)%|^u;5j2j)aPc2Ep)Tp^fFbJFw`0=@(Sr4l1LM;HY15G|rvLWu|bPL6m{jd)RwcmX5!hCGhV3vFTUPTG_Q4fG5E<
toL=#gf8<HhC^YFm<0ozeqAJwTx9BhE*QMVs{*b$1m7DMNnrK-YhoY12*JCcFTvm<~#e&9;kFOoqMsDxo7}tO=-<jF5(cZ4=
5K2ASD4147dl${m4W=LD{jMOQosI!~A98`Y`7x06(wPhUL+H%!Lbj1QpmMj|zhzb_!wyfo~*gwIoMU><EPdL|kkeBO!#oM`b
VQKUU;iuzQz2TL`2a*9u)rwJ2LO{!xi6irt9^!Ss>g7mcfuIS``EaZxIds4SZqCgKnx1vPrWu%`AFkP>-Oj5^M;5cg_QNaAJ
G5Yuhc{k`fG%F`H=D5U>>tl1X^(Y^7wr)PmUdFi!RW#%W+Im#=r6;d)e$B&Rvh1HaAGtA$lE<sKdX6BXj8dnv!Dxm)USmik>
4)aKks{IG&zte{CkIGoKz&bkY*&n*cTbsY98#AqlYNEQTq-6a?{Ij?5an_ml>=t3U%@B^0r@beR>7<I06WElJIDPdHz=I5u4
`i!PTF}ERhF;JKTcx!<u?HpWeC|zLZy7{|dBw6MDKw7_88bRBRPxGoA&k{~q4by12YlE9A|3Y2Nww`8CNVB~vIy@z<rk{jfW
@i`06nX6!MF+D0Ty`IbXqI2HFU7$n^hl})+1i>iT#2gFII1oGCyTO%1twD#!CyD@r%$xippZjh&Y{l1*iD+hDRdifuj#&rsy
J`)LBF?(>{C|HEtW@V@%hgIFEvmk8m|UkP89kn8<rRSo$mkp3-?V(PUY?LT=9fB61YRVJ7Azc#tdHdrH_t@}u}DhqVL;Ktzu
*vh(doa|a0-gb)~F$W@qpNc1=fZ?JXG3$Iw_ywSfL-kyFMej1*;SO2{}{ru^yhrt>4b8BM~8ZpSdh@Qe8>?VyOgW;srg+W6%
LGYcG_gk?mO*Ufs7RAm@IGUgat9cz#sA)L|A>oV0Sf5JOsE2+M{it!*0Ea`mXxn=d^sez5ZlJ;K+d@kv_&^6IUPq0g0B_C+J
f2nnHB<tNr_DV(UfO1jd!1{X<s@0g0q@v~=&oeuup)g$1dn;e1BvsBSUlm?OjPro)_hkrqgl{!-&7zD11=o|xQ$u!<=CP4Q+
9Tco0;H8nHW(x<_cyb8$x&B&XeabbAvD~W_(5-&Rs$<hg^lSWd6c%j~r5Ml#_L{d=^a$9xowuPQxsW{m_NrFZCWaKc(SU031
chgsIV|P$(fLCge(=O!4Z9M)hhbhb(+?>@B3763gU{MMPM5sriv9m!$;JKAs$l;#m9GFQ0;Ar=H<HcAXYT5fm09CO-Q3=+NT
?A2%}G$1=lx)Ybh_ZU}%i<;Wk)1n;qO#XW)$uGCaRujIIE^u#b~&A$>}eJe}?IN^Jx-6AV81x7~XBj(tTus3eknIP*8?;(S!
w~JH&)4MXQz`+0%XgIx;!xL8MAPA;HDp$gZ_D_dREl~EpRLvV%Dh;o|(m6Oeg4}@8J&gobc`5~`EB1vUvelJAh6<Xw@6Ev|{
$3Q7^2g1aSON^B+v4YUF9kQC6+gvr)~FH|f^gU`k>1PzX9X*`#%vA!3FtyE2xHzsKZX!uXd1OzU4W1stJN_FiZ=YwV#*%Wl6
Bd$fv7N>3eXaeCVarI8XXJ7sM^ABTOg$fTx<|DUBD_Sl7PIGDlXTY3SH2m*ZUs3sDxJUhEk$8dMm=$|Kd0B_6ygyOrukF#;(
~7>jNPaJA3GGP5h%(X<f8XzW~^GpPLUI%!?!fCPnlp4;hSezGtIVeD|$h+{RrbJ{A0({e^sS?=#=WNAT9WvgMJRsYtaT0$>q
aJt~@|zftBkv1bD0c!E9(HX=gHe-Sy7(r4wcaibyvBC@(Gj9Rn~RI6=Hn&;N8)6qJIWoO*p-N$4X)&eXFbD<e&D!@~!n^JzX
$6&7DAD;x61la>b(I9fXblj{hgT7Y)ldCLKR}#%ipQ1dP%tKM@c})42H+EKE-q=*7+jdo3tF`srRc%KlnNWLFQ7w8!+LCFUN
a8TQa0)W@$VL;Rki*HxU2$+f^eUVX#}6h&kDs&$<-gFEo31l&5kaKG&8bS*TrUk*JY^qTEzmwPQMMER;o8vR3Nk+Ie6s}TeD
~QoKWC`BZC3DtedeE;oUV&IYF7=yWh=w|41a4=BljfL&ifa!-IvNKmYkIHOO>pM)(hEsK`UD(S|Y(|32<5!;Q*NcwZK43p@K
{(tfgVgG)U~EIu_#GigXhfYSi$7Nf@>fC*?fd4=!fc4YiX4H~{~*aUD+QAX+1b+;|omkVhHe3bJHKpEAfsj3_tGT4(Ln^$vi
awPCGy$$i$&TidcAOnrW3^F<b&)!o$@J8QFRa6-`4uXpuXzs+uF7Eyl2D_J8Is~6?{dRxEDVF3JJ9Qx%V<$ZB32s6{_Z5Xi_
MKId@DF{^TDsyT!+)M}r@~k3p&l;crkb1EZHrFa~Wyn*DBB_lUR}jX8GF(;4Q188!y|+RsYKzu)h3FeSYCdyCMF$unJ^@71s
xM`Y##u=t2<L^zVa0l3n!~r>^XBOcTPD4XUxQG3IlrlGK5+Gpv*Y~O*##V}AOeQ-62=tV)|Td^qzPfYq5}EFV%5v&1BR)wwO
KNG+*b1-*gv*ALGqmidjKyZ%O0bYN#aT!o(d{&KBep-t-u~%fk7JbREQ8%+on`@2>@h!&8LDE@wJ(9IyQKahFWNZN}o{CN=q
W8YpCcvq_xU#=}<}zS{l9tKmyV`aE|Q{AevNTVoN~M)>Avod>yn_bodHgke`-m@(RKRF43d5koDs)Eh&{}d><_Kx-rFar`#^
nuAdkSK~-T%W<794@CZpr;ZbJNTW~XLVOC*5FYJD3Z_$f0%uTMf2_qUe1ABqhamXGs3+v5f1RHyO^am$AYcA~9H7HfaJ>hM_
a$`<bW5>ZR(P{y8$Q&Wv@Nrio$J#Zi(+;fWJG%~n6A3B?VsWA#XHCd2+!&A69GTZN0kk&|Z}vIlCfI;<0*lg@q3kjN8FuDvs
|4xT&=ezBZwN`C8{2mdp#)JTqo*jz&tw*GO-}m4AsxmpJsY~#vmtuMIfx1&zI6bdiL%m}tX*GpXaF3Qm1EXzi=rW73B50=&D
ez_Mw!|0+_9`zHmPDOi0sbMY6sLlp!R{YS#O}uA$1PH&~5m_guJhW*s%-SJa2xsT5;Ce6eo0jrfq8rMcazy3jEsPP6x(nfrv
rY{SLo#>|Z<8&_Ep_Ou;WeHU)>kx78YIJOU~L0y<D5#$MW>+J19lPvFmQc5EO1nRzR-l*$Em(DdOCy8#T<PE)LXq3gg7=P&K
1RDDn%f<{bGM_W@!&~*Qp2NW@1QeJ`!1PPA12LnSiuymH1Z?R-j<Nyd7BAn-;qW{L^@Bl0L)5!roOp2ENC6$}^eutd>94{Dn
_mG+fEm}BSHVBY_2RWYDk-|cQnKsW`PVau{WdWDnE%G+DB2kTZe!?9Yyb16Gqb3bkF7%1eBccbIgR{k3fiC6Wx)PW|SzAIAV
8XRPW69mrtL6<f&;p^?Euq%B=hMc8T}xkRd%q*rm>9&<AaHZYwR~tI1ndM}(~#nQJJVF@KcB!t1}(@e#7L?g#^{z?Vj<aME{
F<d+5&z7!;^Br7=P((KuvhoL=;F;OwcuZp$?Ad<%I7Y?05C!e@c%qy~pU5Q*6Vcp*~3s1Tv{wwGB)0_D2(lvb}>nEF>O(G!G
osIVg{p#T4aa7O=(cNZTU?ks7qC;96yP3bZLLd?|KQtru<s7RP+y%W)QXTTR2590waBHNJ9v<lfJ1{?$J3-K-$XqdEm$pi7g
vIjJrXeznb?+pWpO{%SR)3xM~pR!hDBv&b#hcPCiXgC#H90C$4cM(61-VV1ynUnLdazFFC(d;`)*0%(A#e=SKj{o1l3XE<#l
CB=blfhDG=flVx`dQWzNo<M7w<qHJi44t?f$O4Z>GAAm9x8z%Nx?eaPi~@o;0JJ*Rb{F337aiX3Xkg^P3BS$X+0ZEKB+{y-v
1)#!=*XD~XkqlWv~?A^fEwCoAuYK;Q@;1oHoBE<^n1{Gg`L~TRf7{0M?%fIoA|eJJIg{a3BOo+crm#Mvj`8y#hG|Ar5$1p+a
$va7Ew+~zd;3ZBlFfw+}5Kj6yeHPBy?%`IfC9Pl3gSV*v90zj|AxImP_VQnu*m%=7^#r>&V(8srqaN{tTdcY09h21RAO|M%0
UQzO78x9Hru>T$a`Au<DLUFY|v`iOsdTO}T&1e6e%KZ;`-DT~QgmzB9}=5|}cB$+C?U26LFQr<T8n1O^sMrZ773H?t}&twPK
)u~Ns5Sq8KB)~W(T6&`f~oTG&0@yCpzfH;85V$jYqMFE-D{F>eH8@AvJhPgNVF_FB}r#Lo=-FyziVM@v%&%JXP<hKKdK`J|h
&ki4UfKPtm0Dt_V!}@52tdB-ktM&lfNgh!(<8kQ)z+dFMQ2<&M6>G>0SeXT=2c|Lr`OQS&r_Zv0<%&l2x-lfW3ixC22b=0}I
*okXj_2G2`($99@CWMZXTX^6&E-_hzwG|&(SwpDicHo9A0jpv&xwf7E*LP^;x!}BfFFzu96ull&w(%4AbJp|`wm!pYaeXgCN
MNY_|q<(P$5BHDu8uct;JyxTdm7Lfd>XFG|shEoy%a8Jet9dZKpG<^;q3jSR-voIb%6nuG#X1E!d2#{hFJCt}ixkRBOs)q3K
5J%vEPDJAczUmuq=0wR}-vGz^`%bMqRHq-Jyw012T$S(JmdX7+-$W}09|;AGfu>_*)wnulHtbMC5wQxxM5Jp9mHv5(b#{z9I
(Y=WSbl~BJU*mtWdXg<lScj6lHY9}hfMQ&2rWRr?0*D|~)WL3)}$jIu9ki2#QZ&hAM^rF}#{;^^tuN;bFLUg|e!V4d?;Xmn+
+q4rV=<-ezmCYLRmn&{czgKbnd6cG6eD8Y8RWy&hY~7IOkt6BiCDB9n9>3mo_79HOew&)<;OX!PfyB7#q3s+ULcS%y)L|7o?
IDj2J32a$J&Id=Y^i4nPh%s*(a~Y~45T~zhl+9=Z%<k^VeFTj)XDc|T(m<rX!X|R%aPR!d4&P~73mzXccf6FJYJgC$OIqd1u
ZallfD@~h0K9nObD#d*_%2ms~vxWrmj&-$8Ri49D13X&%7*k&)jFK{i<`}Lf>2yF8&mvDovh1TGZ~m7b22TdN$L7bi4Wq4!w
vt{YqrCzI*T{qi@~zt9ZXB6mG8`{^5B>M!0o)%a{^#NYE)nxs4_o5+JBaX4M(DHpRNnZ>S?+s?wY||75NQn=|;6$(9(MQpKg
FlCJ+?%6^h$0p2?d-9-Yq76gf{)7Fv$ZRQKu!-&ahjVkbzg7|@`jyFZ6WUyafzC)bZ8%p^+OXk&`2sfu2rKMiJl9&+DQC&@x
d#cRRs#S|{KT5}~kg=UOO*&hJ$2XWSm33dK9$M)?&{b3q>#cd0GY%nf0f)JEpS}6K@%MC<)6L&)<kgXZI=q1Ftvt9e@fexm%
?F0(kd}6tA*;K(YEIhsTNA>0xJgP0nRd(N&(_j8k`IS<b9lX)8y0q?G4&=_<zW{ce(UMl+kDm7*vB2c9zvwiS4|trrY%?B*=
Av-@%-51YHf6CD%&@yDfr{gR&sj2w~d)CIizImpGZ3|!Z3BqLa)3RB?~5hSKdw;z7N`3@P93F5d-UvjmkYglDwK;hiSuAtNN
xsy*@wH?pA3*ymW$?G^uRkpe?3&AQ}$Z)v)C=W*ghpNgm~GJ;bFg^fNc{=d(M(a*^hyNc;%jq966RcxjyD^=OudkehknX<^g
SVDPWou&id|+qbx3?S!$P1fgm53NO143y#0jHS;xyBD;T*C#85DUbWyI=*DCj&4Wf)pzJ(n=mREe+Aw?1ma6%x10n$h`=CGq
!EPDg)c!wtrn5g}UH+gGnsxxie0}%{f`679*a&~gnLLjgcyJ4w-p0qfL4(=UM0TQnv4DO3)0+VyE5T|+8n^D1>{Ir|pzVun)
9q0e88dBt%Cpw4BzOMX>Gc^Pmnz86H{d(E2zcqZSC==R@OR~+wS(c8?q+4akiQEa3<9NV)uh&w1KeExcHIYDx@wg9kTi&&Q|
~~!*Ex7cZ9B7Y6-4)8UYJ&ics;nfyuKBPxKNvj*j7WN3(AE0!ym?9UVl3OG(7#)Js(_t9^794*B$)lv=3rEy}7|VwjeRr#bt
6`5SZ)Y_QQ1>+HXu<NaH5Ud)Fl^rin>~16>h!eKZZE^h_!tYxuL!|K6~AVpH=i{)v@8>sQr*2uxf4!hb-&+Mh--=&a$*@54z
ZevS8fT34r^u3^6aGdMdRxM!E2VT!~4z`b*}{lp(xyjd@<)`qj=?C-R9U>7fb+;8Ao<_49z;viWV{w#_75G!Hw=kWP@k*@Lg
^*7(*YGaJ`lNozrAsh0W9e|l6^Bksa_(ou4MvjM_#>{v!LSxvV9|OF7)US?Azr|k>!p@q$o%epm^B8y&@6dw3!~eRgY8O`To
d3N06>G=fb+NDxn{Mj)1`+1}=ty+n@Y7f4oV`0}6=$K};_AFD#`Cv-dPMgBbGjw<_hx76p|3Hk1Gv^pyY(mMZx*F=n<QRRKo
wn+Np0mPxXfuX=UA`bDA)h(YW+X2)o(Hk9PQ-GNe+}*+iDTv?NiesCsZ?1^?IFv`KmFnT3d_x+ef+C38Lu~2V;QS!Q)%N7Fr
54Bvy4ec&eQYQrWW2mHK{tO<l+W<XAgCY};lWwDyq}iq`@$)aEM2{7e6b4LRUj2Tt-NY7aU(;);EFZ$|*MHZVCRKAraa_Wse
q;okeb_mF!Zwhs^5?+@Sa?H{!d+s^xaI?0m0zUKE-sB*vjc6xRV-m&kV4$s`rm&40jbeT7U{_W+p`{`^jyam9)P3iT2`s05A
U~tku
"""
raw=zlib.decompress(base64.b85decode("".join(DATA.split())))
assert len(raw)==17760 and hashlib.sha256(raw).hexdigest()=="a42d4f5c5849ba23eb02392a82fb1318bf5d40614531c9c18e1486970e53ac28"
PINS={'cap_pair.py': [16009, '496a808189aaac79c7ec92bf96d498e24e28511cfd27166537b9e27fc8618182'], 'cap_pair_identities.py': [1362, 'd3849bc97a59610b910dcc8a7d942299f3f2e66cc344e616e09c6df1b6144d5d']}
files=json.loads(raw)
assert set(files)==set(PINS)
out=Path(sys.argv[1] if len(sys.argv)>1 else "cap_pair_recovered")
out.mkdir(parents=True,exist_ok=True)
for name in sorted(files):
 data=files[name].encode()
 assert [len(data),hashlib.sha256(data).hexdigest()]==PINS[name]
 (out/name).write_bytes(data)
 print(name,*PINS[name])
print("CAP_LINKED_PAIRED_WEDGE_ALL_SOURCE_BYTES_RECOVERED")
```
