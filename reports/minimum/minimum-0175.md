# minimum-0175

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NEGATIVE_ROOT_CAP_ERASURE_AND_UNBOUNDED_VALUE_SECTORS_V1

## Determination

I obtained a strict, actual geometric negative-cap erasure theorem. It does not assume endpoint, frame, root-edge, or joint stationarity. Its principal conclusions are:

1. **Every pyramidal negative cap can be erased:** `T(P)<max(2,T(P intersect {z>=0}))`, for all positive endpoint values `a>b`. In particular this applies whenever the actual polytope has exactly one negative-z vertex.
2. For arbitrary root-only bodies, the same strict erasure holds throughout the entire endpoint-dominance sector `2 max(a,c,d)>=a+b+c+d`, with no bound on negative depth, root size, or number of root vertices. In the normalization `a=1`, this includes the whole simplex `b+c+d<=1`, not merely a collar near zero endpoints.
3. Consequently, **all-negative root bodies in that entire endpoint sector satisfy `T<2`**. Mixed-sign roots in that sector satisfy `T<51/25` when the exact visibility condition below makes the clipped body root-only; the A-dominant sector then has the sharper `T<203/100`.
4. There is an exact high-trace countercontrol to the assertion that z-clipping automatically remains root-only. A proper `8/17/11` body with one negative root vertex and `T>1013/500` clips to a proper positive-octant `10/18/10` body with one genuine positive-ell vertex on `z=0`. The extra vertex changes the actual volume and trace.

The entire remaining negative-z root-only class is **not** closed by this result. The main unresolved interface is now explicit: strict negative-cap erasure can create positive-ell base vertices, whose removal is not licensed by the positive-octant root-only theorem. For one negative vertex, there is at most one such vertex, its height is strictly below `b`, and its position remains coupled to the erased root apex.

The inherited positive-octant endpoint is the literal parent `minimum-0173`, SHA-256 `389d10f39fee11d742407c78c13fb00db2dae152c7946e67f8b982b99b337ef2`. That parent and J55 together close the positive-octant proper root-only class, not arbitrary positive-octant bodies with positive-ell auxiliaries. The supplied branch memory makes this distinction explicit.

## 1. Conventions and the exact scope

Normalize `a=1`, and write

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b<1, c>0, d>0, alpha=1-b,
ell=1+(d-1)x+(c-1)y-alpha z,
ell0(x,y)=1+(d-1)x+(c-1)y,
n=(1+b+c)x+(1+b+d)y.
```

The main root-only applications concern `P=conv(T0,F)`, where `F` is compact, convex, has positive area, and lies in `{ell=0,x>0,y>0}`. Some point of `F` has negative z. The protected coordinate faces are the genuine maximal triangles `ABC` and `ABD`.

The cap-erasure lemma itself is more general: `P` may have other vertices, provided it is a compact convex body containing `T0`, lies in `x,y,ell>=0`, and has the stated proper protected triangles.

All quantities below are original uniform-volume integrals:

```text
V=int_P 1, J=int_P (x,y,z), E=int_P ell, N=int_P n,
g=J/V, T=N/(6VE).
```

Clipping changes these quantities. No preservation of the centroid, first vector moment, root area, or ell-marginal is asserted. Every comparison recomputes the actual moments of the resulting body.

For a genuine positive tetrahedral fan, the recovery uses

```text
v=abs(det(p1-p0,p2-p0,p3-p0))/6,
V=sum v,
J=sum v(p0+p1+p2+p3)/4,
E=V+(d-1)Jx+(c-1)Jy-alpha Jz,
N=(1+b+c)Jx+(1+b+d)Jy.
```

## 2. A general actual negative-cap erasure theorem

Set

```text
Pplus=P intersect {z>=0},
Q=P intersect {z<=0},
K=P intersect {z=0},
A0=area_xy(K),
e0=mean_K ell0, n0=mean_K n,
W=Vol(Q)>0, Eminus=int_Q ell, Nminus=int_Q n,
H=int_Q (-z)>0, e=Eminus/W.
```

Here `A0>=1/2`. Let `P0=conv(B,K)`, an actual B-pyramid contained in `Pplus`, and put

```text
kappa=b+3e0,
V0=A0/3,
E0=A0*kappa/12,
N0=A0*n0/4,
k=24E0=2A0*kappa.
```

**Cap-erasure theorem.** The sufficient same-body condition

```text
8e >= b+3e0                                             (MC)
```

implies

```text
T(P) < max(2,T(Pplus)).
```

Equality in `(MC)` is included. More generally, the computable original-moment criterion `Delta>0` below implies the same strict conclusion and can hold when `(MC)` fails.

### 2.1. A base inequality from actual five-point hulls

For `q=(x,y,0)` in `K`, let `s=x+y`. Then

```text
n(q)+ell0(q)*max(1,s) <= k.                              (2.1)
```

When `s<=1`, `q` lies in the canonical triangle, and

```text
n(q)+ell0(q)=1+(b+c+d)s <= 1+b+c+d=24E(T0)<=k.
```

When `s>=1`, the actual hull `conv(T0,q)` adds the tetrahedron `BCDq`. Direct original integration gives

```text
24E(conv(T0,q))=n(q)+s*ell0(q)<=24E(P0)=k.
```

In particular, `n+ell0<=k` on the whole base. A planar positive fan from `A`, using `ell0(A)=1` and `n(A)=0`, gives

```text
e0>=1/3,
n0<=2k/3,
T(P0)=3n0/(2A0*kappa)<=2.                                (2.2)
```

For the proper positive-endpoint bases here the last inequality is strict: a positive-area fan triangle incident to `C` or `D` has a strictly positive ell endpoint, hence a strict n-endpoint slack. The weak bound is already sufficient for the main comparison.

### 2.2. Pulling back a base inequality along actual B-segments

For `p=(x,y,-h)` in `Q`, `h>=0`, the segment `Bp` meets `K` at

```text
q=(x/(1+h),y/(1+h),0).
```

This is an actual point of the same body. Its values satisfy

```text
n(q)=n(p)/(1+h),
ell0(q)=(ell(p)+b*h)/(1+h).
```

Thus the affine function

```text
f(p)=k-n(p)-ell(p)+(k-b)(-z)
```

is nonnegative on `Q`. A positive tetrahedral fan from `A` gives

```text
int_Q f >= f(A)W/4=(k-1)W/4.
```

Consequently

```text
Nminus <= Uminus,
Uminus=(3k+1)W/4-Eminus+(k-b)H.                          (2.3)
```

Also, a fan from any of `A,C,D` gives

```text
e>=max(1,c,d)/4>=1/4.                                   (2.4)
```

These are positive fans of the actual cap. No fictitious cap centroid or independent scalar masses enter them.

### 2.3. A depth-moment bound valid even with lower-cap overhang

For every convex cap `Q` with base `K` as above,

```text
H <= 3W^2/(4A0).                                        (2.5)
```

Indeed, define the tail volume `U(h)=Vol(Q intersect {-z>=h})`. Convexity and Brunn–Minkowski give concavity of `U(h)^(1/3)`. At zero its right derivative is `-A0/(3W^(2/3))`, since the sections converge to the actual base. The tangent bound is

```text
U(h)<=W*(1-A0*h/(3W))^3
```

until the right side vanishes. The maximum depth is at most `3W/A0`, also directly from the cone over the entire base to a deepest point. Integrating the tail proves `(2.5)`. Equality holds for a pyramid. No assumption that the negative cap is vertically above its base projection is used.

### 2.4. Exact comparison, including a stronger computable test

Let `Vplus,Eplus,Nplus` be the actual positive-part integrals, and define

```text
Dplus=6Vplus*Eplus,
Dmix=6(Vplus*Eminus+W*Eplus+W*Eminus),
Delta=2Dmix-Uminus.
```

Then the exact denominator is `6VE=Dplus+Dmix`, and `(2.3)` proves

```text
T(P) <= 2+(T(Pplus)-2)*Dplus/(Dplus+Dmix)
          -Delta/(Dplus+Dmix).                          (2.6)
```

In particular, `Delta>0` is a sufficient actual-moment erasure test.

Using `Vplus>=A0/3`, `Eplus>=k/24`, `(2.5)`, and `k-b>0`, one gets

```text
Delta >= W*Phi,
Phi=(1+4A0+12W)e-(k+1)/4-3(k-b)W/(4A0).
```

With `w=W/A0`, this has the useful exact decomposition

```text
Phi=(e-1/4)+A0*(4e-kappa/2)*(1+3w)+3b*w/4.              (2.7)
```

Under `(MC)`, every displayed summand is nonnegative and the last is positive. Quantitatively,

```text
Delta >= W*Phi >= 3bW^2/(4A0)>0.                         (2.8)
```

This proves the theorem, including the equality wall of `(MC)`.

## 3. Automatic sectors: pyramidal caps and root-only endpoint dominance

### 3.1. All endpoint values when the negative cap is a pyramid

Suppose `Q=conv(K,p)` with `p` below `z=0`. Its actual mean is

```text
e=(ell(p)+3e0)/4.
```

Therefore

```text
8e-(b+3e0)=2ell(p)+3e0-b>=1-b>0.
```

So every such cap satisfies strict erasure, with no restriction on `c,d`, cap depth, or the positive part of the body. For a polytope, exactly one negative-z vertex makes the cap a pyramid over the full actual section `K`.

This is a theorem about genuine convex bodies, not a license to assign a pyramidal mean to a cap with several negative vertices. An exact countercontrol to that latter shortcut is retained below.

### 3.2. A root-only base-mean bound

For an arbitrary proper root-only body, including mixed-sign roots,

```text
e0 <= (1+c+d)/3.                                        (3.1)
```

Here is the geometric proof. Every noncanonical true vertex of `K` is either on the root at `z=0`, with ell value zero, or is the intersection of a true `B`-to-negative-root edge with `z=0`. The latter has

```text
ell0(q)=b*h/(1+h)<b.
```

Every such new base vertex lies outside the canonical triangle, hence has `x+y>1`. Put `m=max(c,d)` and `nu=min(c,d)`. If `m<1`, then

```text
ell0(q)<=1-(1-m)(x+y)<m.
```

If `m>=1`, its value is already below `b<1<=m`. Thus every new base vertex has ell value at most `min(b,m)`.

Triangulate the actual base from the canonical vertex with endpoint `nu`. One triangle is exactly `ACD`. Every additional triangle has endpoint-height sum at most either

```text
nu+m+min(b,m), or nu+2min(b,m),
```

both at most `1+nu+m`. Its actual area mean is therefore at most `(1+c+d)/3`. Averaging the actual triangle areas proves `(3.1)`.

For a nonpolygonal root, use inscribed root polygons converging to it. The section is an interior cut of the full body when negative material is present, so its actual area and first moments converge. The cap theorem's positive margin `(2.8)` remains a strict pointwise conclusion for the limiting body.

### 3.3. A whole unbounded endpoint sector

Combine `(2.4)` and `(3.1)`. Writing `M=max(1,c,d)`, the condition

```text
2M >= 1+b+c+d                                           (ED)
```

implies `(MC)` and therefore strict erasure for every proper root-only body in that sector, regardless of how its root crosses `z=0`.

The sector is the union

```text
b+c+d<=1,
c>=1+b+d,
d>=1+b+c.
```

In unnormalized endpoints it is `2 max(a,c,d)>=a+b+c+d`. These are sufficient conditions, not necessary conditions for low trace or cap erasure. Their equality walls are included.

**All-negative value theorem.** If the whole root satisfies `z<=0`, then `B` is the only positive-z extreme point, so

```text
Pplus=conv(B,K)=P0.
```

Thus throughout `(ED)` one has **`T(P)<2`**. This includes arbitrary convex roots, arbitrarily many negative root vertices, and arbitrarily large negative depth. Negative-root existence itself forces `min(c,d)<1`; no additional upper bound on the other endpoint is imposed.

The all-negative qualification matters. The exact mixed-root control `mixed_five_near_two` satisfies `b+c+d<1` but has `T>507/250>2`.

## 4. Exact visibility boundary for inheriting the octant theorem

For any root-only body the actual zero section is

```text
K=conv(Delta, F intersect {z=0},
       { (p_x/(1-p_z),p_y/(1-p_z),0): p in F, p_z<0 }),
Delta=conv(A,C,D).
```

This follows by intersecting segments between the positive and nonpositive generators. Root-to-root intersections remain in `F`; only the segments from `B` create nonroot section points.

Define

```text
K_F=conv(Delta,F intersect {z=0}).
```

Then the exact set condition

```text
Every B-projection of F intersect {z<0} lies in K_F       (VIS)
```

is equivalent to

```text
Pplus=conv(T0,F intersect {z>=0}).                        (4.1)
```

For a polygonal root, `(VIS)` is equivalent to **the absence of a true edge from B to a negative root vertex**. A true crossing edge gives a genuine clipping vertex: the two incident facet planes and the cut plane are independent. All other new clipping vertices remain on the root. Distinct such B-edges give distinct new vertices.

The proper protected triangles survive either way: they already lie in `z>=0`. What fails when `(VIS)` fails is root-only status, not `ABC/ABD` maximality.

The projection denominator is `1-p_z=1+h>=1`. Its inverse along the root uses `b-ell0(q)>0`; the wall `ell0(q)=b` is an infinite-depth limit, never a finite point of a bounded input root. The new erasure proof does not integrate a refilled projective image and does not require a uniform distance from this wall.

### Value consequences

If `(VIS)` holds and some root point has positive z, the clipped root has positive area. Therefore strict cap erasure, supplied by `(MC)`, `Delta>0`, pyramidal-cap geometry, or `(ED)`, combines with the inherited octant theorem to give

```text
T(P)<51/25.
```

When `b+c+d<=1`, all three endpoints are below one, and J55 gives the sharper

```text
T(P)<203/100.
```

The applicable inherited results are precisely the two proper root-only octant theorems recorded in the supplied branch memory and literal parent.

If no root point has positive z, use the B-pyramid argument instead; no positive-area clipped root is presumed.

For **one negative root vertex**, strict cap erasure holds at all endpoints. If it has no B-edge, this proves the value threshold outright. If it has a B-edge, a hypothetical `T>=51/25` body has an actual strictly higher-trace positive-octant successor with **exactly one positive-ell auxiliary vertex**, lying on `z=0` with ell value in `(0,b)`. This is a genuine dominance reduction, but that successor is outside the inherited root-only theorem. No stationary root reaction is imposed on it.

## 5. Exact actual countercontrol: clipping creates a positive-ell vertex above trace two

The following completely literal body uses

```text
b=1/5, c=1/50000, d=1/200.
```

In addition to canonical vertices `0=A,1=B,2=C,3=D`, take the four cyclic root vertices

```text
4=(1/10000, 7/8, 62459/400000),
5=(79/100, 1/100, 1019751/4000000),
6=(1000350001/995000000, 1/20000, -1/2000),
7=(1/1000, 997/1000, 101247/40000000).
```

Every root point has positive x and y and ell value zero. The exact maximal facet cycles are

```text
(0,1,2), (0,3,1), (0,2,6), (0,6,3),
(1,4,2), (1,3,6), (1,5,4), (1,6,5),
(2,4,7), (2,7,6), (4,5,6,7).
```

Thus the f-vector is `8/17/11`, both protected triangles are genuine, the root has positive area, and `(1,6)` is a true B-to-negative-root edge.

The original actual integrals are

```text
V=43041923645224747/238800000000000000,
E=810419757417390108249/15920000000000000000000,
N=1767005468967276331151042466249/15840400000000000000000000000000,
Jx=44454895834828322621766247/950424000000000000000000000,
Jy=878643241741085446427/19104000000000000000000,
Jz=1757816492860736382369509/38208000000000000000000000.
```

The actual centroid is exactly `J/V`. Its trace is

```text
T=23560072919563684415347232883320000000
  /11627341773113622281217342940754546001
 =approximately 2.026264762772 > 1013/500.
```

The B-edge creates the genuine clipping vertex

```text
q=(1000350001/995497500, 1/20010, 0),
ell(q)=1/10005>0.
```

The actual positive part has f-vector `10/18/10` and trace approximately `2.026663817791`. In contrast, the root-only hull

```text
Qroot=conv(T0,F intersect {z>=0})
```

has f-vector `9/17/10` and trace approximately `2.026663770380`. Their exact volume difference is

```text
Vol(Pplus)-Vol(Qroot)=740629711/48823227173880000>0.
```

The source reconstructs both complete hulls, their exact V/E/N/J/g, and the strict trace difference. This refutes the **geometric identity** that clipping stays root-only, and shows that the omitted vertex changes the value even above two. It does **not** refute an independently proved inequality `T(P)<=max(2,T(Qroot))`; that stronger deletion comparison remains a useful question.

No equilibrium census was performed for this body. In particular `8/17/11` is not the mechanical `10/17/9` layer, and no `110` claim is attached to its trace.

## 6. Additional exact controls and method boundaries

The complete source retains eleven input bodies, their actual negative and positive parts, base pyramids, and applicable root-clipped hulls.

The two `lower_star` controls have endpoints `(b,c,d)=(1/4,1/1000,1/2000)`. Their root is the exact intersection of the seven xy halfplanes in the source after the original root-plane substitution. The parameters `(u,v,omega)` are `(1/1000,1/2000,6/25)` and `(1/50,1/100,1/4)`. Both have three negative root vertices and no negative B-edge. They are proper `9/15/8` bodies with traces approximately `2.028047029748` and `2.021910749522`; their actual root-only positive parts have traces `2.028301613532` and `2.027102643592`. These demonstrate nonpyramidal cap erasure above two.

A separate triangular root uses `(b,c,d)=(2/5,1/1000,1/2000)` and root xy points `(4/5,1/50),(1/50,4/5),(501/1000,501/1000)`, with `z=ell0/alpha`. It has one negative vertex, no negative B-edge, f-vector `7/15/10`, and exact trace `403147187799924000/201012304782409351>2`. Clipping gives a genuine root-only `8/15/9` body and raises trace.

### Arbitrarily complex and deep nonwinning geometry is retained

For endpoints `b=1/4,c=1/3,d=1/4`, define, for `i=0,...,k-1`,

```text
y_i=(i+1)/(k+2), h_i=H+y_i^2,
p_i=((1+(c-1)y_i+(1-b)h_i)/(1-d), y_i, -h_i).
```

Every `k>=3,H>0` defines a proper positive-area all-negative root polygon in the endpoint sector. Thus the analytic theorem gives `T<2` for the whole unbounded family, not only the three audited choices.

The exact controls `(k,H)=(3,1/10),(9,1),(17,100)` have f-vectors `7/15/10`, `13/27/16`, and `21/43/24`, and exact traces

```text
185833235/119921499,
50763951689/40518212308,
2015454998252695/2281554128865004.
```

The last retains seventeen negative root vertices and depth exceeding one hundred. It is not discarded for its low trace. The same generator also audits `(b,c,d,k,H)=(9/20,2/5,1/10,7,2)` and `(1/3,5/2,1/4,5,1/10)`. The latter tests the genuinely high-C endpoint sector and has exact trace `196905311057/168505658809`.

### The convenient mean guard is not necessary

Use `b=97/100,c=1/50,d=39/100`, and the complete root yz list

```text
(1,-1/20), (2/25,-1), (7/10,-12/5), (49/50,-3/5),
x=(1+(c-1)y-(1-b)z)/(1-d).
```

This proper `8/17/11` body has trace `1887351325195/1766639501763`, and

```text
8e-(b+3e0)=-114787/600700<0.
```

Nevertheless the stronger actual `Delta` and `Phi` tests are positive. It also satisfies `4e-3e0<0`, so the pyramidal mean formula cannot be imposed on a general negative cap. Failure of `(MC)` is not a value obstruction or a counterexample to cap erasure.

### Uniformly refilled projective balancing is not monotone

A shallow all-negative quadrilateral is generated with `b=1/2,c=d=1/5` by

```text
(h,theta)=(1/1000,1/100),(1/1000,99/100),
          (1/500,99/100),(1/500,1/100),
s=(1+(1-b)h)/[(1-d)theta+(1-c)(1-theta)],
p=(theta*s,(1-theta)*s,-h).
```

Its trace is `43469898071648000/23985800361206453`. Apply the canonical-fixing projectivity

```text
Psi_v(x,y,z)=(x,y,v*z)/(1+(v-1)z), v=b.
```

All denominators are positive, and the transformed endpoint at B is one. But the actual uniformly refilled image has the smaller trace

```text
169039514063952840/95968732345950731.
```

The two values are approximately `1.812318013868` and `1.761401968451`. This refutes raw balancing monotonicity, not a comparison with an additional `max(2,...)`. Both true centroids are recomputed. No weighted-image integral is silently identified with the refilled image.

## 7. Retained same-body moment tools for the remaining sector

### 7.1. The correct negative-z C-fan has seven types

For a polygonal proper root-only body, an actual C-fan has cell types

```text
T0, CFFF, CBFF, CDFF, CBDF, CAFF, CADF,
```

with actual volume fractions

```text
1/t, rho, pB, pD, pBD, pA, pAD,    t=6V.
```

Their sum is one. Define the actual canonical incidences

```text
GammaA=1/t+pA+pAD,
GammaB=1/t+pB+pBD,
GammaD=1/t+pD+pBD+pAD.
```

Then

```text
E4=4E/V=c+GammaA+b*GammaB+d*GammaD,
rho*V=c*area_xy(F)/(3alpha).                             (7.1)
```

The extra A-containing pieces are real. Deleting them to reuse the positive-octant five-type formulas is invalid.

For an all-negative root, let `u=4gx,v=4gy,w=4gz` and

```text
X=u-GammaD, Y=v-1, Z=GammaB-w.
```

These are nonnegative original root-coordinate contributions in the same fan. The planar quadrant area-moment inequality gives

```text
XY>=alpha*t*rho^3/c,
YZ>=abs(1-d)*t*rho^3/c,
XZ>=abs(1-c)*t*rho^3/c,
rho*V/c<=W.                                             (7.2)
```

The final inequality is actual containment of `conv(A,F)` in the negative cap. These necessary constraints are not a certificate that arbitrary scalar assignments realize a body.

### 7.2. Actual endpoint-height sections retain two synchronized costs

For all-negative roots with `0<d<=b` and `d<min(1,c)`, put

```text
S=Vol(P intersect {ell>=d})/V,
Rd=Vol(conv(C,P intersect {ell=d}))/V,
f=1-1/t, gamma=1-d/c,
etaB=(b-d)pB+b*pBD,
etaA=(1-d)pA+pAD.
```

Original tetrahedral section integration gives

```text
1-S = rho*(1-gamma^3)+(f-rho)*(2d/c-d^2/c^2)
      -d*(2bc-bd-cd)*etaB/(b^2*c^2)
      -d*(2c-d-cd)*etaA/c^2,

Rd = rho*gamma^3+(f-rho)*gamma^2
     -(c-d)*(bc-bd-cd)*etaB/(b^2*c^2)
     -(c-d)*(c-d-cd)*etaA/c^2.                            (7.3)
```

The new `etaA` cannot be independently discarded. Both section quantities and `(7.1)` come from the same actual determinant fractions.

The affine function `ell-bz` is nonnegative on the whole all-negative-root body. Its normalized mean is `F4=E4-bw`. Applying the area-moment inequality to the actual section in coordinates `(y,ell-bz)`, and using genuine A- and C-fans of the actual upper cap, yields

```text
(v-S)(F4-S)>=b*(1-d)^2*t*Rd^3/(c-d)^2,
(v-S)(F4-cS)>=b*(1-d)*t*Rd^3/(c-d).                       (7.4)
```

The code independently constructs these sections and upper caps and verifies `(7.3)` and `(7.4)` on the applicable controls. This is a reusable necessary region, not a completed whole-domain threshold certificate. The wall `b=d` is allowed; `c=d` is excluded only from these section formulas, not from the cap-erasure theorem.

### 7.3. A complete original-density B-ray representation for all-negative roots

When `F<=0` in z, use the set chart

```text
q=(x,y)/(1-z), v=1/(1-z),
x=q_x/v, y=q_y/v, z=1-1/v.
```

The body minus B becomes

```text
q in K, v>=f(q),
```

where `f` is the actual convex lower envelope, `0<f_min<=f<=1`. The canonical base marks have height one. The root image has height

```text
g_root(q)=1-ell0(q)/b.
```

More precisely, `f` is the lower convex envelope generated by the three canonical height-one marks and the actual root-image graph, followed by vertical rays. Arbitrary free convex profiles are not declared root-only realizations.

Write `r=b(1-f)`. Then `r` is concave, `0<=r<=ell0`, and root contact means `r=ell0`. The inverse Jacobian is `v^-4`, so the original integrals are

```text
V=(1/3)int_K f^-3,
Jx=(1/4)int_K q_x*f^-4,
Jy=(1/4)int_K q_y*f^-4,
Jz=V-(1/4)int_K f^-4,
E=(1/12)int_K (b+3ell0-4r)*f^-4,
N=(1/4)int_K n(q)*f^-4.                                  (7.5)
```

Thus, with `I3=int f^-3`, `Ie=int(b+3ell0-4r)f^-4`, and `In=int n(q)f^-4`,

```text
T=3In/(2I3*Ie).
```

For a planar triangle of area `Atri` with affine positive f-values `f0,f1,f2`, the exact integration rules are

```text
int f^-3=Atri/(f0*f1*f2),
int H_aff*f^-4=Atri/(3*f0*f1*f2)*sum_i H_i/f_i.
```

The source applies these rules to the actual projected non-B facets and independently reproduces `V,J,E,N` from `(7.5)` on every all-negative control. This retains the original density; it is not uniform epigraph filling or balancing.

## 8. What is settled, and what still needs geometry

The main cap inequalities cover arbitrary negative-cap overhang, nonsimple incidence, curved limits, and equality in the displayed endpoint and mean conditions. They have no division by `1-c`, `1-d`, or `b-d`. The finite-depth B-projection uses only `1+h>0`. The assignment's `0<b<1` and positive root area remain explicit; no zero-endpoint or `a=b` value extension is claimed here.

The new results do not make every negative cap pyramidal, do not prove `(MC)` for every body, and do not establish universal strict z-clipping dominance. They also do not prove that the root-only hull of the clipped root dominates the original body when a negative B-edge exists.

The most useful continuation is to compare the positive-ell base-vertex contribution with the **same erased negative cap's** strict margin in `(2.6)`. For one negative root vertex, that auxiliary is exactly its B-projection, with `ell=b*h/(1+h)`, rather than a freely chosen positive-ell point. Proving that its subsequent deletion costs less than the already certified negative-cap gain would close the entire one-negative-vertex value sector without imposing any stationarity.

The updated stationary negative-z statements in the memory are not used as arbitrary-body value bounds. Their full-joint hypotheses remain separate. No E17 registry change, mechanical exclusion, `110` body, or new minimum is implied by these trace controls.

## 9. Exact recovery and verification status

The following capsule contains the complete standalone source, all eleven exact input bodies, all helpers, and all reconstruction and verification tests. It needs no parent import, archive, external file, seed, numerical optimizer, or third-party package.

Save it as `recover_negative_cap.py`, UTF-8 with LF and one final LF. Executed environment: **CPython 3.13.5, standard library only, assertions enabled**.

```sh
python -S recover_negative_cap.py negative_cap_recovered
cd negative_cap_recovered
python -S negative_cap.py build negative_cap.json > build.txt
python -S negative_cap.py check negative_cap.json > check.txt
cmp build.txt check.txt
```

Expected terminal markers:

```text
NEGATIVE_CAP_EXACT_SOURCE_RECOVERED
NEGATIVE_CAP_ORIGINAL_MOMENTS_AND_VISIBILITY_EXACT_PASS
```

Exact pins:

```text
recover_negative_cap.py
  8350 bytes
  SHA256 0f64bc98fcb29d1a8de71cdfe616b9791217c27e396e11700e985bfb3b4f379c
negative_cap.py
  15114 bytes
  SHA256 fa4a96b1337d27459904dcb5b5d2ae979921e8c41a0cd7f9e143a8554dda3d33
negative_cap.json
  100865 bytes
  SHA256 913cce88ea0a3e1c07d6d628ed8bbeb8226e1142a8ede6cd802e8ecdf36416ab
build.txt and check.txt
  3585 bytes each
  SHA256 ed963013216a83e33c4671fa65f53035ef7254fedb635b817b95a814223b98d6
```

Normal build/check and a clean source-only capsule recovery/build/check were completed, with byte-identical reports and stdout. The source reconstructs maximal facets and true edges before checking visibility. Two positive interior fans independently agree on the original first vector moment; the C-fan and, where applicable, the original-density B-chart give additional independent integrations. No mechanical S/U/H or weak-contact census is claimed. The continuous sector theorem is the analytic proof above, not an inference from the finite controls and not a proof-assistant formalization.

Convenience copies: recovery capsule (`recover_negative_cap.py`), complete source (`negative_cap.py`), exact report (`negative_cap.json`), execution receipt (`negative_cap.txt`). The literal capsule below is sufficient without those links.

```python
# NEGATIVE_ROOT_CAP_ERASURE_AND_UNBOUNDED_VALUE_SECTORS_V1
# Source-only recovery. CPython standard library. Parent analytic endpoint:
# minimum-0173
# SHA256 389d10f39fee11d742407c78c13fb00db2dae152c7946e67f8b982b99b337ef2
import base64,hashlib,sys,zlib
from pathlib import Path
DATA = """
c-pl)X>;1jmf!s=G<829iI&;y<OSTWvSX6i$#YVUFPSNZQVB^I*&u`jwn!@fea_OY1v|-oA138MFQ-qRK6@|xWn2&6pWR-LhVISh
&$sT|voG%O=Ira=H$!*S=^J70`5R-EMt4!{EsW_Z*a;&G{Y|ur4KEH1-%AW{8$_GKgTIWoUv`^0bo358y~AT8+W>@@2F4<qre3-;
R`FstFucXWh~i|s$)IBsrieFOtey@JX6b5a%u<igXGXM4R_Vrgry2||Gu|-_4%@6&ivq@9EvG;sjbo6++st8J4e$l32dX^xGVBuf
*(w&<E;~4r<~y@(iQ>Z=oY$K=(Db%w>S(A7Z0ghozCF8^<1=wC-inLKK@iRiF9=LeOs#$zZnkM`Y_`cFH1p=pn5|MH7dzmF@jXfi
$f6<HcKXr~=Ql%^+l9Fi-rkUno%0YJ;4x&d+SHI|+ofsd_RF|=RW!~|S6NmYX?o+%#Ga136UT!OD0L=6mD<?W=3b#n9c=4xuc9R+
T7+NVWa@Y>Y-c#oz%bqiHH%p++w?Vd%Q1_Ys9nPlqWN~Q=$eVuKQI!Rfi{GJnE??AOk_keV-dzsK9L<gNpfJ&IBzjC*Eq~b<#+;L
1zXqHXgtlMMM%R_>$F3*p@>e$4zK_|fjK##Zuir}WR;i}4oeTcBnjid%(1HGOb>L4rcJDI9|kwMGVWuAn^?cn&~s-|nr(Ppo<x}q
?&Y{pOQ3g8xQR%{o&KZ==l~h6AdopqX@|VaQA#_g4!oueT3xl=2uG)0d>5KstA9U^CeUk}ITm*CVYObt^jQYRX?UmYVilfXZM-jK
&{MQBFmqi>{8rK!%sfBL<d2_BdL-_}15RJHbdzb}(U$1ZI%3JngEo|m?<cTOpiFS}K~<62AnkYsgvL8Fw)*}m-bC>>gpRpHC5#zz
@aQcvIp&t!a^|JrlL=#4MzM)d)=B$h>E&FmB19P7e%kKG5{=dAh}as;r88GkI2BXH7Q!AtN2ECLh&^GvU4qZtgp3YxKS~Lb3er^~
aT;by&k_&ePA<IVH1Le5?@co^rlk+OJS?%6BJB~f=)WXl!pW0#1xm!CLtX$gY0N!26F_2>D1gw(z~2GdARFVr!zd2I988ACtPw~V
AM{#^b;#DLxO`MUl#!3xSBMR2-D<N1tUGD<{oP?2K89%)k}*9<Xy9p4B>oQ83MBCYVB`bnJACyYCQ7^1+LRkW_z9o@g(KA)Gt2`o
fRs-`QinAeguz`+Mg3h}LJZee)&tH<Tc5uZxKc$A8X%!M1l<P%@wSVNStE^ou_eY6OZ$rmRt!tuWZH}U@MspMfoA4e$!K;zLF~#f
7YnkON3gdpfv{c?0iaXcFf-9UDyB*ESPm8m%xYqhR|iN6JEs<*=wV1fV-LvgXCBz8V4xMUWyGH9N(ENS?hX8KfwrI=R%J2$=RT+-
kPHx;(;+64wV0$L$li!Qo50=ycs}u6j+2@+QD<@3<7y!>5TUN+Kp83BP8YsIfgGEmSpx8<vP~1tutIYiqo#y1EC%EKl|U1Rdh19~
{D=Q5a353wQb3p%uT{&_1Zo5fK-MdEj>MH97-rux^s;RVoF&i6Y$PT#kEM3211~N)_!LHWbI7z{x#k#im5I&nQa}xOW9>6lIa7`a
D`h;GB0Sl-=H8RYwI(b40*15*itAR%W$j$hLV+^9-nuf3``t;Ya{vZ1loG!o$Z3Aq+%BFio%w^wshO;z7|4M%K?EG+7ZC);Ao4ed
m=}Ui%oGqv06F}ekrhT4IRTr%33CTolb|+5lahS|G5IGbL8RI*=lxF83_yQv48Bd%=OP4qbIQdotUr!Rc(c=-Hhm3`m4HVS+(X|7
Q$R*h2~`$p>`;!>bXVncSLJk9Fx}u<#<6)-N@H}|rgUaliRj2r#YV|eghFN6k{3U7A7QVsN~KaOQMwROx)4i@B(P0hi93pnofgzA
F_c4bEw9C`yl$DV?2$cG$zZbZVlQ=3-?b=F(uw5w0&)RuqO~Wqb^-w>plBbP=nW{Zt!70@!s(R1-MBuiHwwUoYh4jpbQeo<Giwn1
K62C&gs>A}AaJ^#Z`D#3g|ACW1jA6mHikEdXKQU7=p}M;A=urbPX~dtZ_3eu6w-J>#n*~gQS44Vh>vT5UpT4G$$)t(K}B|~Q9<^T
L>xlnC{$4agO%D2Kz`#zG3vBPL)=&~cep%m@Io6kPp<n|VHy+UfpX33nlWKm>`f+vYBGnbRvtOm2^^<olq6syBv)#A?;tq}i^bli
kcV-yjC)lx_Ld?02$8N<8xiK4)RPeQfFNpyL@F`g36uRu5j)!_(-Y3^ePt8@83o{AKZ7M}@c(S!C_3y_Bw(K^ve`>5Nn$xtq)2?(
KCla|10mQp%z|b`@Xl(P9cNlM7#dd+RqjH@c`-p=PCx_$dqZdsB{^%@D>t#TNxUN=Sju$|63LKNMN(7!SeGeff?BYqXwm*D<qz6<
|0HI-0M@C3T|nLjzH*x}G5dBeVBrNZi(f(&K(I705LtCj<0=J!qFf7;(?xQC^<FCOr?Seyb-_UzjF>S#E<*{TVcFbIONF|}9k12$
(!nxD?|nbT%7O8v%~a#~=J<S~*Yi<!kL)k)abwt+3?4k-b+czL!-B)uHELi4PFp=<rUJ$m8wRvG-J<zgH811V5jB2<oX}>tT2T7v
0BLK>K`mWd_0^I4!NJS$6tcn&Z05?b@d+UOSfS*$F*)fTRG6!r>6-nh8mE1qiTZ&Gye1EdYEafF4zP1PFuqAr2wMDLxYRY|(sfaT
^$tErN7b$x6AYT694=emAf-(tOPVm~3L(%H9DhM>O}?_tQDP65&2RQF!H;FRYOVexhY|GB>UAs00>%uNwPupVb<(_EKErcGVuHZJ
R6tdfODL!Ppj^p^6WO!B+22~`5y;YF_rjt%0_fRHd#rW8F4rc=d1~1v^S7n|vsq2<YI<!GoT6+Y0z$sfvp+&|3ez7sz#c~Vp+I)M
Jdp&5hck<f2kOBbbyRCIk0f|8B)!?`+TScYbWFqu_<A;@(@QI`5~@@A&4$qj#@*IS1Nko)NO}y~MJ+(2)-M7)1vX79j6xq5$KjnE
KX*T<oRcD@L@4mp9n@Vf33G`Jc;+&nO9vY$G-%?!k&Vsg$_hX^fl$ix5Y!_3wUhx~b0<ip=!>DRM8+#o5sX$1RD0XaY6)4258T9a
1UlJ7cj0hIY6hGR<Dm)p>VAoE8J-}&d7uiKt=_YK#6iu`temdGQO)5xVHhI7@5(*jOOd;yVq3DxqD}M|*4U06n)9c~`E2e5tEXpv
8sZQpHq9}f**5nvz_c}Yt<k_H>(8F$WnxZBV%*h(#DHEVY9*1C(P~PJGMr%R4PGSZI7VAJb#h__bKwp}%5!2To`tb{WDGjj#CA)A
-&eq+Uw}ts)j<#j@(%%yR0X<#zeRciiKeoFm-Gnjf>5i&K%Uzw0q}HC1N`_;*w2`LRxlOp=iQ0M+EyBcfwP{bfFh^>isWn62qDol
u2*q*pj&Yet|@~olVn?_%4?wktY2}CUG4rbgxOOj#8Meno@g>t^)itNSuD2TeAQ?w0w{u)lqv~eZO~zin}@aLYu$X^(8qdgy8XQn
q{8;^0oe6)Ey2idX=%8>(o3M3tK?U`#Y-69na3T`J;tcz#V$AxPiEm`7`u1|!GOFCpny~naly>0kgGdj+($^-On_;q?JxvL#y~h_
Wq(o2a#b44vr~SFA54N&grJ`)_F!(ZOTA?j0H?)UBwgy&2s(c%{t+-HlMpa?WWM9PQr=Iw0SwVyhJa$JaL1||i;wc7_$I%JP=?}z
{2+ob+05PPY8wac9b}5tq`>*GH#J3H7s8l_a&co0(!!g~K#jq7Cxn6;o$I9tQ#uuKmtJ}o#bpqOE)u7^SUmwgnp{$g_yU0)qOL%4
T@KOoxkrc=hXN^LjVNftbD0Q_d5ch7_MN-zW7%gw`;)76jaXNVC7-c3wbD}(Ug^q9<T`k$Z_*OiUqp#Zm#w9#R(i-66`q54vVT@#
I{w<<MGZ!>l35O}WF<cwY#<{Y9T<<kxcB+!QSv#R2GSdM@wV6#n*<Gx)5KF7*rPx@Up-Ci*D6Nw(I#!|5h<OYfvN1BpsDj%FuXHz
i<^ur`&?D}l@I_`tJua3p5~E1rxV$50i(~Wqc8Mm20GF}XTJe@wU0@)clQUY_G8_?ho?vFS*WTVs3Ld9RGrXyacji;Mv;o-TqGCp
3IEUF??NK1<}#_1?6fvSFP^kwFQ$(N#(NJtn#mdbT@21cuARf*#o!{~+6C6I|G*d?$s@b6k7$kbB+w)M=6kO>wa>$5U|$3f=+o-P
RGlE~ZBKcFZ_#}rV@mB2paLJ!f=r%|4i4~GSCZQ-uJ~z*;>?X=KMKOw59NDLoL8#np}442F9HEH4v*M0z^y4a#}NV}2gd$7VU<H6
Ab_YCH^9P^=q~k=ImE6cUCp8e_)Iz*Qr4t5^;_{Mp6FQeh>j%(c`mokMKIXy<fGHUWc@sJo@)D?JQus2n9qw%EwH2IpHw!Nu)XjS
Fn~O_cRPm|WN+-$wtFof#zLO&;Dues2`cRXT(tXTd;R1W@$yaz58Jm1=E{^RyRgh)>x0=L2y^hvg&ZRU2A4h?oOFdwhbU+Ewoif+
Iptt`f>ZGZfetb&CtmB~#A{t1P^`-nuQhLLAa%-~?~yn|lrqpa?2s_EpP!+s<5Oea7W0neK~5mBkhY<u?q=p~d)~o&LYS+1w7RCF
)p@%G|DAb<PZiU)So5hWK5&tRrg!=kg+fetVDnwvf3MmFjIel7J=hhX-1Nzr67F|8L4%|KFMkLh6ezI|ePRb5!eFxb3znP$OPYvY
AK`qJFoa|T_IndZm=1Ks`>qTQ$|IyGoJwFj)W9E1ZS)9WFx;>F#Y}b_a1n!b8wx?ohe4lYia6G7&@b4}&zuzY^IaP{9TPq*+wKCB
v1w}i&eRSZ-v)%?v}I1Q$@Wz@(4@M&mWj=P{N@I*6KaJS%Imhn^qap%r~qC<snq`~cthtCDJU>R-rS%L&A?p%#wQjlY|G6@=PTfu
&EN|<m=|^z%;_dTd*XTQt|$S0y8>E+t8CEGB5(#azN+<M%7FXVK&Y2fk_3tA(5R3iRj;^;XER^rR{^WIDF$i#b;)zkOyyyItnR>m
<I2Eb{xZ(|&DL9B2sQk<2UM>mp7@e-ez$}H%D}||=-(#1!)t6Kf++d<=JNgJ_1P!Lvt!7Fc89;nE%-t=-&G%<3@(qjeaK(e`~{JP
zF)fX-Oo4Feiq+q=sj)auAuhVqIjY3k1mPt`I9b*)ASb^32M=p7?a}GlKNAcA}t~wpKn>}Pz6H~)J`bo8|yWwU5c-3W+KI>H8X`n
%=A@D3gsE8lff|!yu7-evDe_2THQhAp#79?pC8Brp~25)gnUN0XGkM(w@KZDQByu3^yLv0Y|I=wtr<;Elf$gELZ~lm&wD_K<K;w;
SwmS3TbER?*GM%VEg9jX9HZ}f+51~g&z?3R@vwh^h1MPe4t)W#u3ms3iqbKz*91M()P;()utXX@GHD%5+Kg)r87s)Rgp406i>Ten
Q?i2kf(h(eBAs$J6DsKlJq#9C(nL;yHsM!iB1X>TQR}EYRm8Md48=7>HNH$&x?O#VV1fq_VD<v?F#+4?%H1B(P}|b!%Tj$m3f6Ub
q_TDTR2u}0@cE8U<3zrz-2IIqbmwTCJFC3w!6qdy?0D(MC*ScEDR0ZNjh8Cym?W*1kV4R#t_8T^>0s_l669bWPyvE6p1I-C)&4t5
vH#W*sA_o&L4-k}xfMhh6!*J|j^?9P*@&4K)1dc_Qvf<0r;3F8u~7rOsrEb57A;83eK99LueSHvPkCbcLSjM-RM|-oN`CFwE+0s?
=^l?yK*$^A($qc0i%EpHT0uD2VP{(nb2PFxb*dDH9y+y~e#g$6epfx>^xMMk2*1mROGpw1r9Q8qcyNM#ztppuwy1|%>X`&zoGunc
j+l6<H(f0}1?|KBd?V)c@}s6@s9T%`H8~5KmsyZA*J;ok$wZxqnjOZ~>{<$4v)+n{$NqyA>a!-SnXq|YfOeWi$V<a)yVw*`n+q7D
=j(`0yUi+xCDy~T@y(lR>+x?I)o_YZcmPycE$0j{X_J$7_=Jjuj}eftLKx6!XF~Nt3D{GS4Z*5cKpsdOSLTCHV0GjhYrdHg^<{Oj
q+p8-m~w;0GRngM(pNmE3BA<aJgpk)PW+jDzkn1<ukcWfGUh+v55h1B)8Ar0t}s&YQV6qNTUQ+a2W!JkO?e8nQU^MX%9Vei>Zk}u
8u@WWve<$h)NtG`XD-Utq()+=#8RaZAm*~57i?OWp^{gW#bE{6DHHhz3*%L}b1)Ql16%4}FYxu7lCgW5POY!Szn*LVYqd&2o`Tm(
-lbyhY)U<a7-8QO9{e?y3cGlwq&+QX+WkCVDj2f+%;UI?X0}O{&8yY^Q_obD)f<oi&R<b0=zWUNXY=$}c8g=gELuY7&KrN85?9@Q
ZWM^FI5Go)JJqYQ6HXctX56SBT{b4PohZ52RXV1>4(K6Hx>{($@p&!o7=W~?2hQJ*;ybW`jk{dICn%6!MBP_H9$uwaAqDiHS#bt(
U*dhwq;l!5K*kMDXd07pBf#M=#>Wc9o_|o>vc{+FK?Q5!1L-ygy7?jp3sV}2MG_t@2gsm}as`7Zt}2VH>jmO&ftMNu)%fPT+Jd(e
<w(`z>Yu;3+c?4r-Dv57H<?HcQPHc{rJ=D4>9Oh2=F5mzu{y<vO&DzT`o?A+;*5`BjJZC(@r?Nv)QB?U`txmhO$s}%-FK<tmL(i^
BW$)^^u*M}b)<spUG2e+-Vj01*2AWWdJ<F((tkRt*nLOwd(mQ>7G_eO!;_B1p&w?Mm+q>rXiv2ihEi6lVO&85qF|dS`kq|~H1wmV
S9SqZ3VTHNK1avmbve&b2?#K-A1TLGFGX<fs>P9`I@X4V{%YZ+cLfK6735$Z*z4QEUHk(#aa_2}eNREi3s*t47n}kwUG>&<9Ci3F
<1!}I!r0(YY%tCpj21MPpgw)2f$ug9yk<ziQ_wTkFh}jX3*&7RhoE<>DMV|35lSL-+$(Gux7NCI-1y}^Nn?Ts)kHB~sg)!4?mjAS
yh@n50b@w%^eFM--`Eszczvd!el@!L0)9PiR2x^ndr|$RcOgEsC(o%nZodXwRK%5F&#s-&uXp!=Uf@RRJxLRPr*;@@mq}&<Z5|~2
IK-ld_Ab8ml=!|;WFhL<W|cw;3cE<r=)*p;+4$eMVI79CzY6GA5*t*Rjl|!>nb{7sF1>r?hdOx2svGd3Tw}V87D1!WBMzU^XagZ-
M^7)jCwj-6h5AxP0l^kEP%t2J06QoTONeT^`bi`DSyTgWP8$>0@DATMMEW9^MB|)#>4#Mn2z5mVnk5?VVDoIJRaxkF$2k6$P}k&S
6+|??eERz<kJftdd~8LtM1y}O`RVctbv+ZAXuSXX?B;?xtL_Y@R5RWTzkI&ARVxBM3iWfuLx{)S<5$#nI1lq6g7t0arx<Ev@l#Fw
m8L$BbN~JM-^1(MukP9Pg*&?ZdU<~N>GJk}+~I$py}fn6oPGV;Q15j~b#mM~;Lm)rD8}Ds`XOX@@5<i-LUNT`&mr&>q5%5w&}U?i
>X|?PGATa<1zCdNe?A{?;@vm@3d}0-jB8jJNBP=6KL8}Ii#p=EppCAJTOZeLls_ADVP`Sj-nlM2L;UfWQeaR%ekWDYXg+9Rr4|i;
9{LXry063y)xrM(+^ut<
"""
src=zlib.decompress(base64.b85decode("".join(DATA.split())))
assert len(src)==15114
assert hashlib.sha256(src).hexdigest()=="fa4a96b1337d27459904dcb5b5d2ae979921e8c41a0cd7f9e143a8554dda3d33"
out=Path(sys.argv[1] if len(sys.argv)>1 else "negative_cap_recovered")
out.mkdir(parents=True,exist_ok=True)
(out/"negative_cap.py").write_bytes(src)
print("SOURCE",len(src),hashlib.sha256(src).hexdigest())
print("NEGATIVE_CAP_EXACT_SOURCE_RECOVERED")
```
