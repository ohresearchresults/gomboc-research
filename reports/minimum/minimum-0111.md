# minimum-0111

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# LARGE_ENDPOINT_FLOORS_AND_TRUE_PROJECTIVE_REDUCTION_V1

## 1. Main result and exact scope

Two **unbounded, full large-positive-endpoint domains** are now closed. Write A0=max(a,b), where a=ell(A), b=ell(B), c=ell(C), d=ell(D), and assume ell is nonnegative and not identically zero on the one actual body. Then

```text
c,d >= (3/4) A0   ==> T < 51/25,
c,d >= (13/16) A0 ==> T < 2.
```

There is no restriction on projection, either height graph, the number of vertices/facets, the location or size of the overhang, or whether ell=0 is a facet. These are not continuations of the old small-c/d box. Each includes arbitrarily large c,d. The full closed parameter boundaries are included. Their new exact certificates cover 479 closed cells with 5748 strictly positive rational Bernstein coefficients; every coefficient was separately recovered from the unexpanded scalar formulas.

Two additional unrestricted endpoint domains are closed at 51/25:

```text
min(a,b) <= max(a,b)/25;

R(m,n,h) >= 0,
where m=max(c,d), n=min(c,d), h=a+b, and
R=9405 m^2+1013 mn+10418 mh+1750 n^2-6737 nh-8487 h^2.
```

The second domain uses the shared actual centroid and the two individual physical boundary-trace caps, not two independently realizable rows. In particular every potential counterexample must satisfy m < (943/1352)(a+b). At n=0 the sharper boundary is m/h approximately 0.5457578563180926; at m=n it is 943/1352. The exact quadratic R, not these decimals, defines the result.

There is also a complete bijective projective reduction of the remaining positive-a,b problem to an actual body with balanced endpoint density, a specifically linked inverse-fourth-power volume weight, and an inverse-fifth-power objective. A transverse symmetrization gives a complete two-dimensional concave-width formulation of the entire c=d class. Neither reduction is presented as a proof of its remaining optimization problem.

**The universal T<51/25 theorem is not completed here. No actual T>=51/25 body was found.** Six new rational original controls and five genuinely refilled projective images are durable below. One six-vertex control has T>2 in the new endpoint remainder, but is not a threshold counterexample. One formal value 169/82 is explicitly a nonbody, and its failure of true-facet incidence is proved. FULL253, the whole 10/17/9 layer, and pairs of sizes 5,3 are not closed. The accepted minimum bracket remains 34<=C_min<=622.

## 2. Input authority, reading and mathematical dependencies

Read the entire new `research-journal(20260919-130619).md` through EOF, all 1943 logical lines, including the full literal parent and its complete encoded source. It is 314533 bytes, SHA256 `aebfa1519f145d360785afa8ba4df11717a6c604a888511f9b6de39d2b106ea9`. Truncated display windows were filled consecutively; no part of the new journal is being treated as read from a preview. The earlier unchanged journal and result remain the same-chat context; their completed reading was not restarted.

The literal authority is `minimum-0108`, immutable envelope SHA256 `9d2258a0428a16c3385c0eef316795821c6d613f5191ecd44257927d51393770`, UNRESTRICTED_TRIANGLE_TRACE_TWO_ENDPOINT_CHAMBERS_V1. Its small-c/d conclusions and its distinction between actual and formal controls are retained unchanged. No scientific conflict with that payload was found.

The parent's source-only extraction was authenticated and both complete source units were read: `endpoint_chambers_exact.py`, 9960 bytes, SHA `43a04827cc017d9acb19c734914129739d3833c91272f9d13256522a89fa4692`; `section_trace_exact.py`, 16575 bytes, SHA `b93e8851742110527b2c53d1d692e08f1e0b6c4b68fc1ede51748450144e7d48`. Extraction is not a new replay of the parent's certificates. The new recovery reproduces the needed hull/fan primitives in full and imports no parent file.

The new floor proofs use these **already accepted general actual-body lemmas**, explicitly recorded in the delivered branch memory. With t=6Vol(P), g=(gx,gy,zeta):

```text
1/4 <= gx,gy <= t/4;
gx+gy <= (t+1)/4;
zeta <= (t+2)/4-gx-gy;
T>=51/25 implies t<45/7;
T>=2 implies t<25/3.
```

These are accepted mathematical inputs, not newly inferred from sampled controls. Their original older full source units were not supplied separately here, so no new computational replay of those lemmas is claimed. The volume and x/y/s bounds are recorded in the branch memory; the height corridor is recorded with its original endpoint-corridor authority. The improved quadratic cone additionally uses the accepted physical single-facet boundary bound c3<10/9, whose analytic proof and normalization are in the delivered common memory. Neither new floor certificate uses the old 393-cell free-prism program or the parent's 19-cell endpoint program.

## 3. One actual geometry and two exact deficit identities

Normalize by swapping A,B when necessary and scaling ell so that a=1>=b>=0. The swap is the affine involution z -> 1-x-y-z, which fixes C,D and preserves the trace. Use

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
ell=1-(1-d)x-(1-c)y-(1-b)z,
h=1+b, alpha=1-b, K=h+c, k=h+d,
t=6Vol(P), mu=ell(g), u=4gx, v=4gy, z0=4zeta.
```

Then 1<=u,v<=t, 2<=u+v<=t+1, and

```text
4mu = 4-(1-d)u-(1-c)v-alpha*z0,
e_z = t+2-u-v-z0 >= 0,
T = (K u+k v)/(4t mu).
```

The height corridor also has a short direct derivation. Put W=Vol(P intersect {z<=0}) and As=Area(P intersect {z=0})>=1/2. For W>0, the negative-height tail U(r) has U(0)=W, U'(0)=-As and concave cube root; its tangent bound gives integral_{z<=0}(-z)<=3W^2/(4As). The positive part contains T0 and therefore has integral z>=1/24. Since W<=(t-1)/6, one obtains zeta>=(2-t)/4. Applying the same bound after the A/B involution gives zeta<=(t+2)/4-gx-gy. This uses genuine section area and genuine negative-part volume. When W=0, the lower height bound follows directly from integral_P z>=1/24.

The actual fan from C has the **true facet ABD** as a mandatory base cell of volume 1/6. The fan from D similarly has ABC. Nonnegative ell at every other true cell vertex gives

```text
delta_C = 4t mu - c t - h-d >= 0,
delta_D = 4t mu - d t - h-c >= 0.
```

More precisely, for any genuine C-fan triangulation retaining ABD,

```text
delta_C = 6 sum_{other C-fan tetrahedra Q}
                 Vol(Q) * sum_{three base vertices p of Q} ell(p).
```

This is an exact expression in real tetrahedral volumes. Selected flat cells contribute zero; no unselected determinant is declared zero. The D-fan formula is identical with the roles exchanged. The code independently computes both residues from these true fans and compares them with the volume-centroid formulas.

For any q>=0 and tau>0 define the two low-degree expressions, with w=u+v,

```text
F_q,tau = tau [q(t+1)+h] - (h+q)w,
G_q,tau = tau t [2h-alpha*t+(q-b)w] - (h+q)w.
```

For the SAME P and SAME ell, let D_tau=4t mu(tau-T). There are two exact identities:

```text
D_tau = F_q,tau
 +(c-q)[tau(t+1)/2-u] +(d-q)[tau(t+1)/2-v]
 +(tau/2)(delta_C+delta_D),

D_tau = G_q,tau
 +(c-q)[tau t v-u] +(d-q)[tau t u-v]
 +tau t alpha e_z.
```

The first averages two genuine facet fans. The second uses the affine density identity and the true centroid defect. Thus the original volume/mass product has not been separated: `6 tau V int_P ell - int_P n = (V/4)D_tau` exactly.

When tau>=2 and c,d>=q, every added endpoint term is nonnegative, since

```text
tau(t+1)/2-u >= tau(t+1)/2-t >=1,
tau t v-u >= (tau-1)t >0,
```

and likewise with u,v exchanged. Therefore

```text
D_tau >= max(F_q,tau,G_q,tau).
```

This establishes the full asymmetric extension c,d>=q from a symmetric lower endpoint q. It is not an assumption c=d, nor an assertion that the scalar moments or residues can be assigned independently.

### A strict true-incidence fact

If P is not T0 and a,b,d are all positive, then delta_C>0. Otherwise every positive C-fan cell outside ABD would have three zero-density base vertices. But unless P=T0, at least one facet adjacent to ABD does not contain C: if all three adjacent facets contained C, their three support planes together with ABD would bound exactly T0. That extra facet contains an edge of ABD, has positive C-cone volume, and has positive endpoint density. This contradicts a zero residue. Similarly, a,b,c>0 and P!=T0 imply delta_D>0.

For a nonpolyhedral compact convex body the same strictness follows from the radial endpoint map about C: if its direction domain extends beyond the cone over ABD, radial endpoints on an open set just outside a side of that cone remain near an edge of ABD, where ell is positive; they give a positive residue. If the direction domain does not extend, the ABD support forces P=T0. This is a genuine root-incidence constraint. It does not supply a uniform positive lower bound on the residue over degenerating geometry. Quantifying that lower bound from the same actual S, Pc and Po remains useful work.

## 4. Complete continuous certificates for the two endpoint floors

Assume T>=tau. The accepted volume tail places t in the corresponding closed overcover [1,tmax]. Parameterize the entire remaining scalar box by

```text
b=B, t=1+(tmax-1)R, w=2+(t-1)U,
(B,R,U) in [0,1]^3.
```

Both F and G have multidegree at most (1,2,1). The following two covers were generated and checked exactly:

| q | tau | tmax | Closed leaves | Maximum depth | Strictly positive coefficients | Minimum coefficient |
|---|---|---|---:|---:|---:|---|
| 3/4 | 51/25 | 45/7 | 47 | 15 | 564 | 641629/40140800 |
| 13/16 | 2 | 25/3 | 432 | 30 | 5184 | 3655/12582912 |

A path bit subdivides coordinate B, R or U according to depth modulo three. Every leaf chooses one of F,G whose full 12-component tensor Bernstein vector is strictly positive. There is **no feasibility pruning**. Prefix-freeness and the exact sum `sum 2^(-path_length)=1` prove coverage of the complete closed cube, including every shared wall.

The independent checker does not import the builder. On each leaf it evaluates the unexpanded scalar formula at the 12 tensor interpolation nodes of multidegree (1,2,1). Along the quadratic coordinate it uses `B1=2 f(1/2)-(f(0)+f(1))/2`; the two other coordinates are linear. This reconstructs all polynomial coefficients exactly, rather than sampling positivity. Every recovered coefficient agrees with the builder's de Casteljau/direct-power vector and is positive. The global degree-bounded polynomial identities are also independently checked.

Consequently max(F,G)>0 everywhere in each closed box, contradicting D_tau<=0. The two theorems in §1 follow. The boundaries b=0, b=1, c=q, d=q and t=tmax are covered, not removed as genericity exceptions. When a=b=0, ell=c y+d x and the accepted coordinate bounds give `c gx+d gy <= t(c gy+d gx)`, so T<=1; this separately handles the normalization's zero stratum.

## 5. Additional complete endpoint domains

### 5.1. A global bound and every root meeting AB

After a=1>=b and c>=d, the actual mean bounds give `K u+k v <= K t+k`. An A-fan gives 4mu>=1, while the C-fan gives 4t mu>=ct+k. Hence

```text
T <= min(K+k/t, (K t+k)/(c t+k)).
```

For c<1 the two envelopes cross at t*=k/(1-c). The second increases up to that crossing and the first decreases afterwards; their common value is 2+b. For c>=1 the second is strictly below K/c<=2+b. Therefore **T<=2+b for every actual body and every nonnegative density** in this normalization.

If b>0, the A-fan inequality 4mu>1 is strict: a positive-volume boundary patch incident to B but not A has positive density. For polytopes this is immediate from a non-A facet incident to B; the same radial-patch argument applies to a convex body. Thus T<2+b for b>0. At b=0, T<=2 is enough. This proves the entire closed strip b<=1/25 at the threshold 51/25. In unnormalized form this is the first additional domain in §1.

In particular, **any nonnegative density vanishing at A or B has T<=2**. Equality can occur: T0 with ell=1-x-y-z has a genuine root facet BCD and T=2. It is not legitimate to make this conclusion strict at 2 on the zero-endpoint stratum.

### 5.2. The joint individual-trace cone

Let tau=51/25, kappa=10/9 and L=tau-kappa=209/225. The actual individual contributions satisfy

```text
U1=K gx/(t mu)<kappa,
U2=k gy/(t mu)<kappa.
```

Suppose T=U1+U2>=tau. Because K>=k,

```text
u+v = (4t mu)(U1/K+U2/k)
    >= (4t mu)[kappa/K+L/k]
    >= (ct+k)[kappa/K+L/k].
```

Together with u+v<=t+1 this requires the affine function

```text
H(t)=(ct+k)[kappa/K+L/k]-(t+1)
```

to be nonpositive. At t=1 it is at least tau-2=1/25>0, because c+k>=K,k. At t=45/7 its nonnegativity is exactly

```text
(250k+209K)(45c+7k)-11700Kk >=0.
```

Expansion is R(c,d,1+b) from §1. If R>=0, H is strictly positive on 1<=t<45/7, contradicting the accepted high-trace volume tail. This proves the complete quadratic cone, including its boundary.

A useful form is

```text
R(m,n,h)=9(n+h)(1352n-943h)
          +(m-n)(19823n+10418h)+9405(m-n)^2.
```

It follows that R<0 forces m<(943/1352)h. To see the uniform maximum bound directly, R increases strictly with m for fixed n. At m=(943/1352)h it decreases with n on 0<=n<=m and reaches zero at n=m; if n exceeds that value, R(n,n)>0 already. This also supplies an exact check on the unbounded endpoint directions.

## 6. A complete actual-root and projective reformulation

### 6.1. Reducing arbitrary density to a true facet root

For one fixed P with its true interior centroid g, normalize ell(g)=1. Every admissible density is `ell(x)=1-q.(x-g)` with q in the actual polar `(P-g)^o`. The objective T is linear in q under this normalization. For a polytope a maximum is attained at an actual polar vertex, hence at the slack of a **true maximal facet of P**. The body and its filled centroid are not changed.

Therefore an actual polytope counterexample with any affine density would also give one with a true facet root. By §5.1 that root cannot meet A or B. This is a reduction of the universal polytope problem, not an assertion that endpoint domains are invariant when the density is replaced by another maximizing density. The subsequent projectivity itself applies to compact convex bodies whether or not their density zero set is a facet.

### 6.2. Exact balanced-endpoint projectivity

For a,b>0, put S0=a+b+c+d and

```text
f=ell+n=a+(b+c+d)(x+y)+(b-a)z,
x'=S0*x/f, y'=S0*y/f, z'=b*z/f.
```

Since f=ell+n, x,y>=0, and ell is positive on AB, f>0 on the compact actual body. This is an invertible projectivity fixing A,B,C,D. It preserves the complete true face lattice, the maximal triangles ABC,ABD, their true edge AB, and any genuine root facet. Its Jacobian is `J/f^4`, where J=a*b*S0^2.

The new affine density and inverse denominator are

```text
ell'=ell/f=1-x'-y'+(d/S0)x'+(c/S0)y',
L=(1-x'-y'-z')/a+z'/b+(x'+y')/S0=1/f>0.
```

Thus a'=b'=1, c'=c/S0, d'=d/S0, c'+d'<1; the actual root is vertical in the z' direction. Set, on the actual projective image P',

```text
I4 = integral L^(-4),
Iell = integral ell' L^(-5),
In = integral (1-ell') L^(-5).
```

The original quantities are exactly

```text
V=I4/J, integral_P ell=Iell/J, integral_P n=In/J,
T_original=J*In/(6*I4*Iell).
```

This is not the uniform balanced trace of P'. Both the volume law and the numerator have changed. Uniform refilling and recentering of P' cannot be omitted.

Conversely, choose 0<b<=1, gamma,delta>=0 with gamma+delta<1, set

```text
S0=(1+b)/(1-gamma-delta),
ell'=1-(1-delta)x'-(1-gamma)y',
L=1-(1-1/S0)(x'+y')+(1/b-1)z'.
```

Any compact actual canonical P' with ell'>=0 and L>0 gives an actual original body by

```text
x=x'/(S0 L), y=y'/(S0 L), z=z'/(b L),
ell=ell'/L,
(a,b,c,d)=(1,b,gamma*S0,delta*S0).
```

All required incidences are preserved. This is a complete two-way geometric reformulation, not a relaxation with independent weights. Zero gamma or delta is allowed. A vanishing L on P' would not define a compact inverse body and is excluded explicitly. The b=0 boundary has already been closed at T<=2, rather than silently divided out.

For a tetrahedron of volume Vq with positive vertex values Li,

```text
integral_q L^(-4)=Vq/product(Li),
integral_q H L^(-5)=Vq/[4 product(Li)] * sum_i H_i/L_i
```

for every affine H. The second identity follows by differentiating the first with respect to L+epsilon H. The recovery evaluates these identities on two actual positive tetrahedral fans of every projective control, verifies all original volume, density, numerator and first-moment integrals, and independently recomputes the uniform centroid of the image.

### 6.3. Quantitative bounds on any remaining transformed candidate

Normalize a=1>=b. Combining the new domains with the already closed balanced case, any potential counterexample must have

```text
1/25 < b < 1,
0<=n=min(c,d)<3/4,
n<=m=max(c,d)<(943/1352)(1+b),
R(m,n,1+b)<0.
```

In particular m<943/676 and c+d<725/338. The original canonical geometry has a useful exact pointwise bound. For p=(x,y,z) in P, s=x+y,

```text
6 Vol(conv(T0,p))=1+(-z)_+ +(s+z-1)_+ <=t.
```

This is the actual union of T0 and its visible-face pyramids. Consequently `s<=t`, `1-t<=z<=t-s`. With t<45/7, the original body lies in a fixed bounded polytope; no shape realization follows merely from this containment.

For its balanced projective image the following bounds follow without any independently selected mass:

```text
26/25 < S0 < 1401/338,
gamma+delta < 943/1619,
0<=gamma,delta < 943/2295,
0<=x'+y' < 2295/1352,
z' > -38/7,
L > 2366/50201.
```

For example f<=b+(1+c+d)t<50201/2366 proves the last bound, and ell'>=0 together with gamma,delta<943/2295 proves the projection bound. These estimates supply no uniform upper bound on z'; no compactness assertion for the transformed body space is being smuggled in. The remaining issue is a linked weighted positive-height tail and the real root/section geometry, not an arbitrary four-parameter scalar completion.

## 7. Exact concave-width reduction of the whole symmetric-density class

When c=d=q, both ell=1-(1-q)s-(1-b)z and n=(1+b+q)s depend only on s=x+y and z. Project P to the (s,z) plane, obtaining a compact convex domain D. At fixed (s,z), its x-fibre is an interval contained in [0,s]; let its length be w(s,z).

The actual width w is nonnegative, upper-semicontinuous and concave. Let

```text
D0={(s,z):s>=0,z>=0,s+z<=1}.
```

The mandatory T0 and the exact maximality of ABC,ABD imply

```text
D0 subset D, 0<=w<=s, {w=s}=D0,
D intersect {s=0}={(0,z):0<=z<=1}.
```

Indeed, an interval contained in [0,s] has length s exactly when it reaches both coordinate axes. Any extra such point would enlarge a prescribed triangular facet.

Centering every x-fibre at s/2 produces

```text
P_sym={(x,s-x,z):(s,z) in D, |x-s/2|<=w(s,z)/2}.
```

This is a genuine convex body with the same prescribed triangles and edge. It preserves V, integral ell, integral n, and hence T **exactly**. This is transverse symmetrization along (1,-1,0), not the previously disproved vertical Steiner monotonicity.

Conversely, every D,w satisfying the displayed conditions and ell>=0 on D constructs a true body of this form. A claimed root must additionally have positive two-dimensional area, equivalently positive integral of w along the segment D intersect {ell=0}; an edge-only zero set is not a root facet. Thus the complete symmetric problem is

```text
T=(1+b+q) integral_D s w /
      [6 (integral_D w)(integral_D (1-(1-q)s-(1-b)z)w)]
```

over this actual concave-width class. The equality set w=s and root-area condition are part of the model, not dispensable boundary decorations. No universal bound for this remaining variational problem is claimed here.

## 8. New exact physical controls and negative results

All six original bodies are `conv(T0 union Root(x,y))`, with the complete input recipe

```text
Root(x,y)=(x,y,[1-(1-d)x-(1-c)y]/(1-b)).
```

The first four vertices are A,B,C,D in that order; subsequent vertices have the following exact ordered xy rows. No row is omitted.

```text
FLOOR7: (a,b,c,d)=(1,1/3,3/4,3/4)
[(37/50,19/25),(19/25,37/50),(41/20,41/20)]

STRONG7: (1,1/3,13/16,13/16)
[(56/25,113/50),(113/50,56/25),(107/40,107/40)]

CONE7: (1,1/2,5/6,0)
[(2/5,1/2),(1/2,2/5),(6/5,6/5)]

BZERO7: (1,0,1/3,1/4)
[(1/100,7/10),(7/10,1/100),(3/2,3/2)]

RESIDUAL6: (1,1/6,1/14,0)
[(2/3,1/10000),(1/10000,139999/130000)]

FALSE_TWO7: (1,1/40,1/40,1/40)
[(1/1000000,39999961/39000000),
 (39999961/39000000,1/1000000),(11/40,11/40)]
```

Exact supporting-triple hull reconstruction verifies every input point is a true vertex, reconstructs all maximal facets and true edges, and checks the required ABC,ABD,AB and root facet. Two positive volume fans agree on all volume and first moments. Mechanics uses the body's own exact centroid and Euclidean metric I; all true-edge four-primitive packets are evaluated and physical weak points are merged by exact location. None of the controls is 110.

| Body | (vertices,edges,facets) | Volume | Exact T | Strict S/U/H; weak |
|---|---|---|---|---|
| FLOOR7 | 7/15/10 | 21949/24000 | 12031540000/10561880749 | 8/7/13; 0 |
| STRONG7 | 7/15/10 | 187853/192000 | 4181823236800/3482589296671 | 5/5/8; 0 |
| CONE7 | 7/14/9 | 137/200 | 1776770/1526043 | 7/6/11; 0 |
| BZERO7 | 7/14/9 | 961/1600 | 5451944/4156325 | 3/4/5; 0 |
| RESIDUAL6 | 6/12/8 | 22401400039/117000000000 | 46714316414498394400000/23272618494382340960647 | 4/4/6; 0 |
| FALSE_TWO7 | 7/13/8 | 631419955111/3559140000000 | 32370768654153242859000000/16158933220075142220545701 | 4/4/6; 0 |

The root cycles are respectively (4,5,6), (4,5,6), (3,6,4,5), (1,5,6,4), (3,5,4), (4,6,5). The complete remaining facets, edges, true centroids, fan cells and mechanics are generated in the capsule, not inferred from these cycle labels.

FLOOR7 and CONE7 both have t<45/7; STRONG7 has t<25/3. Thus they are not merely large-volume controls already disposed of by the coarse tail. FLOOR7 and STRONG7 have negative R, whereas CONE7 has R=458>0 and d=0. They distinguish the new floor and anisotropic-cone mechanisms.

For the first five bodies the actual section S:x+y=1 has min z<0<max z. The recovery constructs Pc,Po,S from true crossing edges, re-hulls both parts, checks their own volumes and first moments, and verifies V=Vc+Vo, B=Bc+Bo, N=Nc+No. For example CONE7 has normalized section area Area(S)/sqrt(2)=28/45, section centroid `(1759/3600,1841/3600,26/135)`, and z-range `[-1/3,41/45]`. Its own body centroid is `(7639/16440,7859/16440,7817/49320)`.

RESIDUAL6 has T approximately 2.007265165532384, m=1/14>1/15, b=1/6>1/25, n=0, and R=-1563433/147. It is a real **endpoint-remainder** control, not a claim that every inherited Phi/Phi_S test fails on it. Its density root is a real triangle. Its actual centroid is

```text
(700042706150117/2688168004680000,
 784111324715117/2912182005070000,
 4017752890053479/15680980027300000).
```

FALSE_TWO7 has b=c=d=1/40 yet T approximately 2.00327386797646>2. It rigorously refutes the tempting stronger claim `min(c,d)>=min(a,b) => T<=2`. It does not refute 51/25. It is preserved even though its trace is smaller than earlier record controls.

### Five new refilled projective images

The projectivity in §6 is applied to every original control with b>0. These are five further actual bodies, with unchanged face lattices but newly integrated uniform centroids. Their strict S/U/H are, in original order omitting BZERO7,

```text
7/5/10; 7/5/10; 7/6/11; 4/4/6; 5/4/7.
```

Their full coordinates, maximal facets, edges, own centroids, exact weighted inverse integrals and mechanics are in the source-generated report. In particular

```text
T(P'_RESIDUAL6)=6327768874880836419534573385 /
                3224032287059156674148497736 <2,
T(P'_FALSE_TWO7)=5273816102113771864080000000 /
                 2669209397510828598237505861 <2.
```

Both original traces exceed 2. In both cases the newly integrated centroid differs from the projective image of the old centroid. This is an exact negative control against replacing the weighted inverse problem by the uniform balanced problem.

### A formal high point which is provably not a body

Take

```text
(a,b,c,d)=(1,1/4,7/10,7/10), t=6,
g=(13/16,13/16,41/120), mu=41/160.
```

The resulting formal trace is 169/82>51/25. It satisfies the displayed centroid bounds, the A-fan density bound, both non-strict C/D fan bounds, the ordinary endpoint corridor, and both individual 10/9 caps. However delta_C=delta_D=0 while t>1 and all four endpoint values are positive. The strict true-incidence lemma in §3 rules this out. **There is no hull, section or actual volume law associated with this point.** It records a real limitation of the non-strict scalar relaxation, not a counterexample or evidence of physical feasibility.

## 9. Additional complete non-record class: all pyramids

A separate analytic observation gives T<=2 for every genuine pyramid having the prescribed adjacent triangles, for every nonnegative affine density. This is a trace statement; the broader mechanical pyramid exclusion was already accepted and no registry count changes.

Here is a self-contained planar lemma used in the proof. Let Q be a convex polygon in the nonnegative quadrant whose two true edges from the origin are the unit coordinate segments, so Delta=conv(0,e1,e2) is contained in Q. Put A=Area(Q), t2=2A, and let qbar be its area centroid. True vertex fans and the one-dimensional section-tail bound give

```text
1<=3 qbar_x,3 qbar_y<=t2,
3(qbar_x+qbar_y)<=t2+1.
```

For the last inequality, Q outside x+y<=1 is an actual convex cap with base CD of normalized length 1. If its area is L=A-1/2, the concavity of the square root of its tail area gives `integral_cap(x+y-1)<=2L^2/3`. Thus `integral_Q(x+y)<=(2A^2+A)/3` exactly.

For an affine f>=0 on Q, write its values at 0,e2,e1 as beta,gamma,delta. Then

```text
[(beta+gamma) qbar_x+(beta+delta) qbar_y]/[2A f(qbar)] <=2.
```

When beta>0 normalize beta=1, order gamma>=delta and use the same two envelopes as §5.1, now K=1+gamma, k=1+delta: their crossing value is exactly 2. The necessary denominator bounds are the origin fan `3 f(qbar)>=1` and the e2 fan retaining the true origin-e1 edge `3t2 f(qbar)>=gamma t2+1+delta`. When beta=0, the coordinate bounds give the stronger value <=1. No numerical search proves this lemma.

For a pyramid with apex A, its base lies in x+y+z=1 and projects to such a Q. Its volume is A/3 and its centroid projects to 3 qbar/4. Split the density into `a(1-x-y-z)` and `b z+c y+d x`; both are nonnegative on the pyramid. The second component gives exactly the planar functional above. The first gives `3(qbar_x+qbar_y)/(2A)<=1+1/(2A)<=2`. The original trace is their density-mass-weighted average. An apex B is handled by swapping A,B. In a nontetrahedral pyramid, two adjacent triangular facets share the pyramid apex, so these are the only apex cases. A triangular pyramid is a tetrahedron. Equality at 2 is permitted and does not affect the strict 51/25 result.

## 10. Exact remaining obstacle and continuation

The work removes an entire high-c/high-d quadrant, an anisotropic high-endpoint cone, and the small common-edge endpoint strip, without making a projection restriction. A potential counterexample must lie in the explicit bounded endpoint remainder in §6.3 and still satisfy all inherited necessary conditions: it is nonbalanced, has t<45/7, rho>(204/203)^(1/4), Psi>204/203, and fails the applicable old Phi and actual-area/centroid Phi_S sufficient tests. The inherited small-c/d exclusions and the one-sided S condition remain in force. These are joint necessary conditions, not a claimed realization of their scalar intersection.

The most useful continuation is the exact weighted balanced-root normal form. Its true root is vertical when the density has a facet root, its projection and endpoint parameters are now bounded, its inverse denominator has the explicit positive lower bound above, and the original mass is fixed by L^-4 rather than freely chosen. For c=d, the complete concave-width formulation is a further geometric reduction. The positive-height weighted tail and the compatibility of the actual root, D0 equality set, real S and the two true fan residues are still unresolved.

An alternative continuation is to lower-bound delta_C+delta_D quantitatively using mandatory pyramids meeting the actual section S. The strict-incidence lemma explains why setting those residues to zero is false, but strictness alone has no uniform margin near degenerating incidence. The exact joined identities preserve all these terms for reuse.

Exploration also considered extending C,D to the zero-density plane and replacing the body by a root-only hull. No general trace-preserving or high-trace-preserving extension theorem was established. The failed stronger endpoint claim was replaced by its exact FALSE_TWO7 control. Floating locator failures were not turned into exclusion proofs. No old control was renamed E17, and the literal old P* and its z-cut remain the distinct 9/19/12 and 10/19/11 bodies of the parent.

## 11. Complete deterministic recovery and execution receipts

Environment actually used for all exact work: CPython 3.13.5, standard library only, assertions enabled. No random input, solver, network, archive, old coefficient table or parent source file is needed to recover the new objects. The finite proof and all eleven physical original/image constructions are generated by the three complete embedded units below.

Commands in an empty destination:

```bash
python -S recover_large_endpoint.py sources large_endpoint_replay
python -S recover_large_endpoint.py build large_endpoint_replay
python -S recover_large_endpoint.py check large_endpoint_replay
```

A clean source-only build and subsequent check in a new directory were actually executed. Both reports were reproduced byte for byte. The independent floor checker imports no builder.

| Object | Bytes | SHA256 |
|---|---:|---|
| recover_large_endpoint.py | 12658 | 2aa52e3765c3e6db20859808957510b13dfae11de356fc824db46fc7636c912d |
| Decoded complete source payload | 23392 | 021ffce739e57d5c50f4b040fd5f2b6619a01a33bc0e49590157f8261e9fb670 |
| floor_cert.py | 4016 | fb9ed372c646ed972fada3dbe330f1fcc875114df0694848428a7cae3c0e4163 |
| floor_check.py | 2831 | 3ae8a37a9652206aaf43474477856aa63b993b425acdf1c4e8bf6eed5df13bf7 |
| large_endpoint_geometry.py | 15977 | d36aafe85305981fca016dd1244adb3c5417fd5817d4490f3ef17df7e042dd32 |
| floor_cert.json | 144247 | 883c3df9321bdbca2793a7e724420dd21257b8f9a89ae7f9deb65f7b81908a64 |
| large_endpoint_geometry.json | 121071 | b31ddef5b17fd7ba9c6268db1e5101e7af1516614cb2904ba3b246d54655e652 |
| Cold build stdout | 928 | 36df858e45e65eaba21105c389b0b1e04934a0677615c63449a940a0bbc32b69 |
| Cold check stdout | 928 | 9e26eb85ef2acf62a8b13b5c059ae50be61da5611f5cca42258600ea55e0185a |

Actual terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


These receipts certify the stated finite algebra, complete closed-cell cover and exact physical constructions. They are not proof-assistant formalization of the accepted geometric premises or a universal theorem derived from the number of controls.

Convenience copies: recovery source (`recover_large_endpoint.py`), complete floor certificate (`floor_cert.json`), complete physical geometries and weighted integrals (`large_endpoint_geometry.json`). None is required in addition to the full source capsule below.

### Complete autonomous source capsule

The base85/zlib string contains all three full source units, not paths, source IDs or partial fragments. The `sources` command writes their ordinary readable Python text and authenticates each byte pin before any execution.

```python
"""LARGE_ENDPOINT_FLOORS_AND_PROJECTIVE_REDUCTION_RECOVERY_V1.
CPython 3.13.5 standard library; assertions enabled; no downloads or parent files.
Parent minimum-0108, immutable SHA256
9d2258a0428a16c3385c0eef316795821c6d613f5191ecd44257927d51393770.
Run: python -S recover_large_endpoint.py sources|build|check DIRECTORY.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
PAYLOAD=(23392, '021ffce739e57d5c50f4b040fd5f2b6619a01a33bc0e49590157f8261e9fb670')
SOURCES={'floor_cert.py': (4016, 'fb9ed372c646ed972fada3dbe330f1fcc875114df0694848428a7cae3c0e4163'), 'floor_check.py': (2831, '3ae8a37a9652206aaf43474477856aa63b993b425acdf1c4e8bf6eed5df13bf7'), 'large_endpoint_geometry.py': (15977, 'd36aafe85305981fca016dd1244adb3c5417fd5817d4490f3ef17df7e042dd32')}
REPORTS={'floor_cert.json': (144247, '883c3df9321bdbca2793a7e724420dd21257b8f9a89ae7f9deb65f7b81908a64'), 'large_endpoint_geometry.json': (121071, 'b31ddef5b17fd7ba9c6268db1e5101e7af1516614cb2904ba3b246d54655e652')}
BLOB='''
c-qB$@psxdv*_>dui)G7yn}5-f`KGWh<Xl9LYi)xkdXH4F6H<b+XN?IsBH+z-u~}zW+d4%khZ(`-t)3sY)dnvku)=!8Oi?Zx6x!a
iybeB)1CSAZ%4m<rT;G5x94Zh+0|+H`r_)&x%<zx)49C9zU?{9gG1-!?DDebe71MKMkn3pbUcenjUBtOvsX$|H}c)sFHOQ>?8eWm
<R%Hw4rftP3L<wn3H(;colHt|H+H8%8pKH{j3!|e0I{wc2T=+r_fGJ6@@{<Lcjnd3&CtL6=)doE{`{l6Vx`{uc71REYjo(>>w9n9
TC@JfwfDV7<ISE|3xZL@-ak0pdsDZ)eShC>jP~q9JMjEwv%Yt5SU>Rh?8af^;Gl-g&!$u0H#sWJMK7woQeiww!$mmp|H~T(-Xp+^
vH2Q};@Pw`id|3iE1b?}aa!ug0^q-NBY{HbU^<&kGN5@p^A}z!tEX-{RyE#iI{X^RhlgYqv9X(sVH{cVoP3Q=xnZ+9v&~lN;`9rj
gh^^hVuoeJZgd|Qe#JIRqgh<?VN6S>rfGhS{^UlD!GCb;2cy#5SeZw0kS^k=^w*z9H}Lpf)VRKHSo6d@`WlsHi<JKb<wR^gM{4r~
E2!X+EvaO_1Kpb@hIs_={l@`^%g%j}8jtM8sF`ME2^gxa$D^f=jGz*`6pl(u$;5OqF<ds>WFlZIM02wy6*D9Dj1|K|Md^{Ji}@rl
!pZ|dh3o;LUc$K%u#suDUg3CUJ^yW<6VHW~T;}Bi3y7Adqq+q|%af?{+0z^_BjP&dbHg@ee;vdUvkJ8_$AO8NYv$a=AdiyB<T)|E
vD96#bn32%*pUAP@`CdYb8MU6TQL;Wn4K3ar~ry&0U)Iug#fu=qEj&utlBVOPqMDA>I6p%GY1*x=tE?*L(g(}3U?_(D3g6N+1NzJ
b)pC`27qq>@MJP14aCkhVhEM8{CUjk>jbn;42c9wi4@BLzO4Z~ndUF@B5WF(F$4cS9&=w#wx3HGs2>$}vB>DKbMYA9V^^EUK2#0F
Ob&xMGP*(-WM#6L8lHuUZrm7XB8-p)CZjta?o27(LEiKu8)uD=nMdvE;)g5;$2?S+8lEZ99<dC}jO2@&ccqZt<U%S`@+h|WYKvSZ
^GTQ*@0hy^g;g0&xgUbL!p49&dj~QznSzeD;%Tnwagd~BUe=7;Y5!q>_6>UQ@Gp);OTi=wq>@O(_mHbi13E*-;4yekcwgEBLgzX<
GzXNoV2km|i%$E9g**(9Y&?4cvi;!{>_|Rn*w}#TpT^-NC{2RMK*)a89++?KBfQ^n=kp-)jlSVlhURXau)*r7iBRxN-Sq9FfjKa9
`@0fGk7f-TWc|2b6HLU!FW?QZ5O9m7{i7o&8<<BEWSg&G<ngK*y?%dE>=B9q(Aq4N!r_N;0MpcE!`W(^-7X3s%?K=tQ!sX3)}sd&
Ayg18ra|ncfe}bMK4D`HbYX&8Oa7ObLmTJtk@E*Jfwi2gZ0e52)d~CaX!4ziP;+E6;D(XSU4qS}){$9Ma=0?A))bSp5z6JtNv^=U
neFlo>)V<H?lJ(;7__Eggjaw=0{1ge2Ivf%!>TX(w{#}}0AR*ah#M^y??`^2lR(Zu5c6$K495e<BGFASc`)~U;!cOYTY5M`Ko}>p
C9Tstc;H;k4m{8ViBTmEl^BvvB2OHD7|5+R=H<?LS>oUXfWZkyBaSpdX|Z1lJ8M>q8q${xpy*Rqj~n~UKqAx^f&fM0S^fWQw0gWR
%*9fe3w<zJN(e~(T2pRJDq~O^B|O8B>_s1zvVj<;;ZXQT*x}Z2C=daSP04%!0_Qc79%Bkdk8ogi`bi(Egp{LKTIvm$5V_&dq*<#Z
X>0%t$qr(WjOcUM9WcW{UxMAx3TIjkRxWFc1{(Ambmc4y2VmJRBjNJE)QE`rF*&yZ534~)GQf4PL2*HfW^mmBKRiy8r!XBGLqXUj
n~Jo=pyiLaB>aohian3RDAk0Sl|>t6hP+C)SlJKezzIWHoVs%;k7#rf=x-Th18P8`QAqIFT}|Eio=Op(N=K7LGUj*jBGB}W<nSA(
*16(<6B~YT9|r+HWu$E&E8rsszOhnP#mtu@m;kAOl3k&_9y~>cP+I74m;fITt9XI2VmF!NhSN(rvJQg0>F%8%CnsL|co{d}w-7K$
kQj=knGxz2$Os~Xd_Z7P1u~8kL7?O~oR=ME>V}cyl#lW`cN{+$F76$t1d$Bs9E1xyFyc#)pE?z)f<CMU=!=xel$BYT;u;~GT$r~T
qrsXeyL%v^dwA2_V+Ww}!wkS~Fnb?s>h!b68l(-e`@{_lTXy`#be<TZYkgSO2H;S^d^xlZ<D9c3!00cX#R)fn4OTuXgYRAb`ZX$>
J3-{l{J_vu#-K&i1^-J%L_5jYg&2^^cE-WV5AR_W2QlCfBtf9pJYeNFZyH|1A00O8_Rt@CZvEh};T{ABb*QiTe%*#}aQJ3)=)O60
gM-l_jN<;@2#V~(+8cMjS(aj;4Ia#Z7`dYvm_DPdg^Jj5=*QC#I`9;O91w3n0gcR&?8j?ZF=EAm>l@Gkz{?b|jB)p;t9RF*u1?QR
^Kg746yG~&zHz$Oy^Fhx&u7lNv)ilQ-Py&Jb8>yw>0F##oL$}ZoNl|<E9YAN%Y*tg`i-eH0R_TZp5OwM3zq>5+tF)w<0{Y&V$f5U
VqwAv;#Mh|i4`=6Rltj(<?IQbgVo%P5`cyf`^@#m==v=KAA`X(6slj6!7l|n(QF#J6VNYE6b~R{fTeKSt^+Ly!f{<)zykL*x*G!&
{I8=Svtjy7$e^I{f}(a-Ld%)BQ&@(gdq7CSG+YAQ&yyUj&GdmBr~i$d0a{vUSXFl6ackP(YqV}5zDB5|h_ESzLI9oNa~dS5d;h;x
&v#RolR25pTtAWOw2}G9Tp{K9F;!wp!%w1MkW<5k3<6fR=E9+a$nA<D!&obZP`3_`c)x&{)~*Z%6c_{H8-a6FRwf)sS;jZZNFgi$
ucT^>E8k4(NnmI&sb$oyan-P^L(@tt#y7k^Y4CEHLN_b)LJ-kJF%6E>Cd)#?g`Zt2sT>DW&bfrbzajZfwLw1|v|_r4fTA|281mL0
RI@_Ux-lLgm~Jfyus#5%Kc^(x>{B}f{=<P4Na$SCsxB~1o!3V_#>=M>tcjcQx~X*lQ#B#8vCX=b@qo`&BYUjDV<mg4!;|z7vsvhi
l+Sv6`!!1Dfd@XtYil0^k+%2XX}@Xj*AH2<W;bhZYBg|nG9I@ti>%qGvqlXb8~b~E48;CT{m=%{gl4_j0;ZUP0}=G1{xaS5iWs?B
=u3su1$wR`;6u$|#IqVCsjI?Oy)gtW=&BaW8|81X&;V`x1?pu|*o_I3lq7|+u)Sqi`1)ji2bqtdAf$UZ0BVsSA>Gxu;I4}Ja}8%u
Xp=mbKm;NQau-o!TYO9iYH(l**lS+(TzZ7_%*&O|bdK@g_LWJJ7m+UlJSo@Ex6!t~>iP%~RllEw2!r)>U&GW?P6Wp?!pXy9Y$gjF
G}>DKBu=?zms=EWJwTW><v37TES0H<#+#_=+gYGgu9an=J>b(ETr~r|q3*0SAADI1Qh-$e%O)KE-tmH^6F_83%7b-_x6$T1XtCI!
z$cQ>j1U|MLEb^&tdAwkR)xRY5Id?s0jXP2hN}vt`U#|emo$fG@+`cYQaTRggo7h;KbZ}|%h+@{LUKsdqzb#)RZ5NFHd8`FK~8aE
*D{W^V;-oaqn7!LXHQ_nnN(J(15lWy95tzWWwj71#*Gm|K+m(q;Kq0~i!e(rRL(Q4p=AZotQF(c9#{*!)(3_3kGWMwm;6^&5n(D-
z9Gt;6P!D=hFPE^jVkYh$p+gC@+ST03-F)2;68&N?6fa0h39;E-2<mubD+<@v`_Aw-bwqiefu*fS`uE{CnLuk5I&#XwxRs$+UcCN
dl&C6E-&u>aJsjjt}d?5iG#D7Pi-i?ILk?bmks{&ec(Vh=QAMh+y}F1kjBqH*qQ6JfkEKx_WI(~>AwG?cLD4J2UzlpdvvX>dvxHh
2P^PIBb4B1zDQAeFVQ!J0^GL>;3xE4+R6LruHDy2Y}=Lo2X^h=FD8@SkxOyR6rJ=SDFF+pg5*vFqz@y25>Y`qc2mhDbxVaGV5n0d
ce{u*|NZqD_{V#Jo!9(&OyY+T#YqYK$<83V_k1?-roRvbsBJ?E259eaGZ46If8rhK=(I{F?JhjoHFhYSW`CB7Z8+sTp|Y>6XJK*k
<TJuZlw>h1q6l|nRs9i?7tfNUh-SEGLxx~LsxJJ%ojqXku7+hbQOo3=jb*l|Ron-}J#NTlxh3k5XbvkRq`SoJmLkX4)w$Xcm<#K*
i>9W#ZHqzB8Q0~u4g7Vv%ub;<(>0|LLnv%yoiQWpm1!BC>J7vNS<k3k!Q_6m?sX)=H*)g2tSb`y`qBaRKLb_>)GfeTGyH`u3-hf_
MwPh6m8Dvz9SPc*n48DEc7(Kd=Cir6X5O(_n(Mh)aO5i-DIkjl-yCZ6-OT%0q>m?zuH3#sPq4!Z-d%S90^A1it-<w+y#7Jge1H}r
Lx<9bV`Lu<Dlk&Taq{^BB?=Qg)dfn_5*~qch5Ndj^aY+R13@bYVD9cibF$3FG8@YZK1N%4A$p>d>`TJC3=EUY+iVJkCQ7;Sh5dmt
Bjt19hYB<w4~l@1$PU^9Osg5M4v)lzF_}-?=(UJZw?r}+6B2Ji7^96*#Dxl>veTAA7otj&iN{Cz2yOWs6)qCbIXbwM<Z?&PxTy`T
f?pIZf*c^3xZWf03*@<3_4Ro!&_NfCpv~jjF$M|Z0h3C373X;kM|s_Bu|VoA!bI}uKy{V-ml5@;>TA*xL>$bqVHv9(xCc)!!h~jy
VptHsnWo-*3i!}%SXqE#uET<``Qeg-p*Jj=v>f%l<f&t<c6R|t!(D?Ev)q3_fR^MO&x^4`m-aw#h~M{*8mP*gzwbAccRq5xASqav
_bl{jJ4Dbf9<&gH5zpp40(Zf9*ff#Y+I!j|D!D5p{R+&(zc|v-rg=J7TYe}<g-u$dWFCe27A>&&U9)k}3ErR1`*Y2VgBc;sna)kK
C`>pQx?m$Z=rPJO-PQ(~kkfO$SY<LANsz=NYI!FPmO-2Zx>-z8PE{f3HSK~J_=vhf1Fp=aRAeHZq+q7#?kGutf%i(71O~1$2H-Ez
b;CK6%g$e7R1k>0Cr=2$^O3^G?~+pB-)o3+{S!|H7zcG6U@NWsL=9DoG0QjxEBM{qh_n>1W)+{Pb+bYt7}7;QUNcS<NlFCW27w6C
cyDD5_g&P}U^9LK%Y)v5m5Pp~8^#Yjv4*Lw9CSK@7(LQ+4Y;-kum<9FBnL@jBkzeDB~Ks=xEl;rQBkwvU?kS<zUn8+69ccLj}pH*
3<FbFyU%j9`^fuvGq4)e#>Q&DHb!fU{+cq{OwET`wbyeCq%VHL4JrF#)*sZhVxyL)F<)aJPzIZXo;Xbf>D(NG-;uU#rLjpXs~qwt
u*{nTK3DkDX6eRhfTPk!SepRWGN2K>6)xW6V6DC87GiFcsV4LS&j@KkCFV8*_$+seKbk_Xqv963I}cVIIAC5dnIvEiBD1I=k{*mJ
=jvYO-0~{;U%3;X*+-sN{J_P?OoX~&!phSx6Gni3*@znjJ!QF`vRqG1_L*bjAKATJm{z-=^Cjt{$w<`kCv#=I30R6-7R}<RI{{kD
V8W8n4|2EW7Be5naT#<)oQxnxKw!+#W&qNrM?l{2T$Jm69-TIzEj(z(T7n1-3a$@ALYvgPLWVA+U4sNf*pjCkj%#a*ka7vJYsj0b
ItWn&#503Z2(+aPWH7bJgM!<tEHbwoWHDcJlR<<)X(B(%0b^Lfd>;7)47XzVRoArUl=1h(t&Pclaa)&%c%soF`W1S3VyWUOdidZA
iju1+4!to>v(M&k81oJcN;btX*zd{%oafKwfrUMQ+xzkWn{8q3RbERB<<$i}5p>?xvRqv@7`bq0!enN~0}Ag%6VTGGv2V%71VPyd
m~@al@T^~gXw$p{DCt0!&3p;Kao{<)=92)dQl#<#rAl^LF$UAlD95Nm6{w46v(yO_2OCL&S0XQ>wKU20p>S+Bvx7MkbkehKnhKFd
YOT7lR*i*bQ6~yhf2%}q8hB$j3cbX*RWtjA_k|S~Gq!ymK&v6RTXQb+wJ9H2t!FRfnpSgfRW^{V3@>_ym&g~@ZMFN78z$kV$-$m4
`Cs8tfAGqDeFtv8twZFY5jAC+(&rRs0ilCWf%}LD8cT`m`=YO{(%6lsa9`~Bj||X=jd}l3o-GmX)qAt(#pk1C7JMF>%7-l;&?z@?
6u+R*;aq*eW%~=oYfMx;sEQCP9#jSOv_BG+;$b{ss<Z$!)`3O}Xgnx{LGvXvpeE@QL+BP1J!nPfMa;hefxM_LipE+|LpQbhu}WI|
a8Nn<u(Z~t=(FHi<5PZW79&y&5l_i?mvfdc_~-#|gXOvDafeA^C*qU>&Gp3sySYo9t%&Z4xLhutU-Bj4i(C@EyuKu?rEEapc0h+g
G2O*PuKBD#FkkCMFu^@6@Pk))22SJqD3jA|s7Z=>;Vh`6aPXTN5}26~!yl0KMYIianL#ck<Th^w^@V;}p4r8GQNkomabZ~->V_$8
lULUJ^j<hJqF(qe3R*l#P(0U-I@`}ZCjKa0qT=x`85hxjt7B&amg%;-A&2K(yLZO>^2G}#kJ&SM{+`K$`7j3E_U+l#9WVbVcV1Rt
PVar2m;bv7bRc*3rF(XAcZP42)a}}V&C0`u?SlmE4ef)Ge=u|pz5V+B8-HjAdv?tZ4&0HwXYcRZO>bB~tTl&jV_0wQ`+Lp(y}e+6
uU^jGyjc`D`R11aJ_H-9WkOE(VY9Ypd6riJ+6}nz;ihT7fxB_VKG>^SzU5c<4;lw>Gp@dAzB#bQ)>ySL0kLp!+lSnYO@Bq5e|0$*
3C!9tA0DgS-;}FWzqMdX_QH*(r6qdQ@-kiUqJJW==`={|cRsFotw;Ek&XMo&rj=ULMb)#?>bUB+d|#FLRN@K1dw0&$O1-+ME~_sE
p9XD-4;}Csz~mkas0|8hVP!JkHgod>-S+W#uq5MqZ~q3Sr(^mGQx@3Ad~wWELV)|Fx?fcAwqh4nzI<Jy?K?V;Yjnhcio5nFkok@}
A<@CZIr?h%#256Yko@a(_zw@&;NST<|D{7U3clUp;QT_FL8OuHF3f_7-tl_rQZttAa~&_WmTNevwJ5-!(yU_*%>3_A`DiUS+_Y29
JDp0qQ=wLUuj2cKjrbhw{JhdWugIQKCqX!Vu;}TBXFJdcI|mXh+sx|lb|-&2=k0U08S$3#zMNth=fnZTPm6#Txcw2L7er}13;hD7
)&aGo{JV4-#GuTj0MGp4h90PQ;9*Wi-(#o!t~hWfr8G!mcO3ZfEGjK$6L5vpj=F|X5Jn8S9ZI<|c$7PXeWT8l2h2c3m9wnNB*p5w
tDaLDv;><X`69?Vf*ozwK@0@O`LAbVwtBq(8z~u?2<R7MkDujdpihMi4GzJUorT?fWpM#vYn}!}aEy$6%!^S-MT2G@6$Y=u;kt=T
2WZ8JSHN}yjD_i&Eg_#|Xp;oZLm`a=RLsqDCB?bK9Z|Ml$lqr|wwc$_Bu$EkxX5G={jQ~ZG<ulVDGLNVZRLApX>|a*2;gt}PvA|m
1&2kA<FfX`U<sQpfSF0^Iwu_07P>tJWVUULq|)LN1^*Z><a~WKM;8tVnRLLPZpP*oV#5XaPpS0Xv|czT&Z$GGA+0cT9Z<)e#PJqs
VPzMYAWAr3qM>SU4=%G+FMDYQcPQlmT|qwtzzLT*3bC~&vr;hA<e7EwtwDMjF!GstJpul%e~u-PHWC$|ak@_ETDhjnI>bkWkilwY
W3&8(0N6EM%x!rPBL7a1hYLxL%%xz>m8iK=4bSI!vg}2*q77u8Hhba!lNqy#JN?z1*?eA%;frPqBPAea6^cdFv;p{olv<Cgo#wuQ
!o@HdrdyLa7*21+Ja7?LyS;uH_i5#EMsgLQNbK2WnIjLZFkskKLNhm2)SJZtKVh>)8pQmXB>|lgaaJ$9mpv#&<X*BxvlJ94P7<ci
<fH;12p)R@oy5~>25L#(kDitY+d}XK-?5>{>{YBxL5J=H-)8ZhaO%QX{>1&3`MIHTD|?)BhZVo|fxFhw>RCORzn%Dn+%Ime_A~ol
$y1X#dw??7bf1GLJMY(p=&MIr%H0v`QHBz3hLrK#RT~X#q~ssyF+`U{Bj4r*X*K<LyFKRb_T+@#6m3Bl)!x>PMXsH>=gs*|AsHx@
RB95{7IJQq#$P{ALw@J{Rj8XBYMr(9JR@?jR+b-Jxise4J4@ik;jmW87L(5Gx)mDMVa3R-w7J{cm>;B~AF5GvCFUZ|6ZbG1rV2}l
<Sxu5Vw;R6QhS1CjiGqLcV{;C+|YrgR|$$a$0!?}sA$N<Vk36b_FMQu=%xcF9SHCdM4Bz?muY$5aO0HQMIh)Pz%o_&>DCxBP#h{j
XV99*=#!Y6z9QN2NpdugE&j5e9}4fsDHr_i&f|@PI=nAHn79<2D~N|))|U#w3`1{bx4A70(CC1y<fMK^Yp}suslrQrjU1lJ`U#QE
qXlbZ#RP9zXt4s1H<<%5?d$#`3?GvauWtd;+L;O6rkAKmf^-b2tzX&)lnzdlg+uVEA{MS#_{_qWjV(Z>IT<J(_5UEV9_)kM?GQIt
+2WO9!D0u5@#kfCXe!s_!&;W)<2vF83tGZGm9S}rh$l8%q|Jo2QtcXmvB`H3ZnmtF!<qlgZ?Zr&;b>n!@DJ?L$u=_AG^9J&B8ftB
aJh=o;6BEQ&xeX-wQ8%9rfdrth&iJ~9PW0&GUW@j7?^&~5?La$Q^llFWo;MB+!{7#1nhrEV5kVxe@;MK&SN_A06w?pCP99nCzvM`
`q;Iac6Kp&p5j5+&@*C)EaUtYRwLf6R{@8?wE|ZNspTD$H70Ihz&)d1vzYqrs}31uIy`+)X4%S%uh7UGlDL>GX9G*>SkXjQO>Jn5
a_{c;`s#d>RF;7fH$`%Xf}CADVD&Y6C)ZbJ1!@Gj$A}ib2!y$=I@?o~BHbmRu$Z3rMLk~3flmG1pJ%t%8u^;eG4;A{s0o3h1L`h9
(;ZV)R3yiwLHP{5k=wK0#p$Q^<-XpHeTm&H_M?#zRb<rzlpn&Me6paT$?S$%(ZCC>cG{P{GyHl~Vf31{jjPs2)ljp>8i!_8FC|{K
l(P*WJEJbh56poQ`w^WdaH3g+h9(pHAs3_F^0?3C*tRgqvv0QUxv?QUQu0t#T9Gf^MRJ0r*2om{J?(C9%QfGdt=}=9Ou1yd`bC#%
fhh=VW4~sS!$`VJ^mYx*Et{01*gs@%>gL<K_NQ&hXuCSxNJnFtS7-}xIKaq#tyG@;MW@Y{efpcpVS1=n(_{W}tTNsO0!?7%Ed?H`
1ws*AzU4y;h+wc#K>FRfCo4;xKR#)93Fi??ZM}4JNl8*ST_n8RxxW3_zI3jx@0_;t?)vnP7QXTi5MbpOL6sa|=^lFc+Kv~L;>9FL
@Z?2FrBZ6;Eml}xtr(_a?)kk;!QADu^v}{U*^WVGx<_FYrh(&5?t@|MW-|Qm(#dQJi&7ethWPqY;8*4A)7##EhQ%}-g&wT}+M7wV
W23*E3GQ$RHer1iylD>9>zai#!W+9I+5~Rj9Rl~HzE`szEA`r;^}A^q%{|Mj99WNL)wU06HS2flG3Sq@g{2!D);Bn8<Qz724*%IU
g?5%)IG?}XdShGCc4IFIH=T?o?q>L=wZN-qT1&aR@v`-J+AnWB>3>@`q4d93_g@T9?k(BXAMM2u%1`kB>E6sg-J|)ny_#Rzv-#l;
O)>EUa<3H6xsSnn+;6f6Fc{!eifrjxb+d8M)XvW3A1@Kvw!*hXI-B1w*#h;qKVh<k#^3siNj?UvEQ3Vf5K;Z0z+8TP2;a`)VxOCd
Cnp)ZJm2|d(%A8J+sDL$&ezv<%wU5Jr5zaUKrenw1+%-WXQ8TFec){;;IxPyxA!Z37>{QLlP(l?B^CA=7H1R$Qx7m#&srFITTCFy
ZHp}9+<G-hvtdrxQcQHZT|c5EHfS{2zkMwZyUm)#7c`1s{W6|;(3`*HYn$*bZ;|r#{Jo+G1^5XLB%J5r)$1Ux$fD%lf9||1w>xu?
H7E9!m!6@iei;*?<-u|7SU$O{@?fJ;{D^~SQDvGg`(+s8<BoXiUuEbZggwq&t0KN)bb|oB{I3(JZ$lTo`$6lM_(pRS6izy#qjW45
tZg*qNGYO2<<Ut#_*O>pQQbbM_2YaT#A~*1$=}{HWrCMtoxL@tk84}UJP!yoCei!U_<XCgiK%A3E%Qt-sJ|7T@%oWqX_1fK{3{Yf
4dDCg{xeEG&EBz|%J?xngxUY%vh20Qfldikh(?SoRe4ZI8PS-Ly()N@WEED=eD%yIRdUP7kX|y<Jr4g^al8aWYiEfOCp*#Uf@rOM
P2!(^NeWxo`Y9-B`~UIBpyanD<o9b{drwz<%qCmCwtl?{$%wBs$?x6BZ#AjiW;p@`rhgSjeVj><R;Q?R+jjI1KAWTH$S#Wa%6k`I
oU60{ICr<7KwfVz+E?e7XU^?41TGM^;9KMLN#^!d&$<2&zM}roX<wa+H_K1Y&z$b<#Yg%Wl=j)DoH|kMo;clWrw46cTwgh`&bE8m
o8&#B_VMD&8T<nNb}}9M*i`$neRTqG-P`LANDRs@KDN&RMZ8b{pR<ee_s~D*;_CC+EvVnc)!o_oEokC4nrpAOe}G>=ExhG^fv@q4
SLcz-ET+4{fbJJ)o}XQRJiEL7L-KcfM(^uOO!hZEi}l*a*@QZMjeh(7fBqj>o*@b
'''
def verify(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin

def main():
    assert len(sys.argv)==3 and sys.argv[1] in ('sources','build','check')
    mode=sys.argv[1];out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())));verify(raw,PAYLOAD)
    data=json.loads(raw);assert set(data)==set(SOURCES)
    for name in sorted(data):
        b=data[name].encode();verify(b,SOURCES[name]);p=out/name
        if p.exists():assert p.read_bytes()==b
        else:p.write_bytes(b)
    if mode!='sources':
        commands=[['floor_cert.py',mode],['floor_check.py'],['large_endpoint_geometry.py',mode]]
        for command in commands:
            subprocess.run([sys.executable,'-S',str(out/command[0]),*command[1:]],cwd=out,check=True)
        for name,pin in sorted(REPORTS.items()):verify((out/name).read_bytes(),pin)
    print('LARGE_ENDPOINT_FLOORS_AND_TRUE_PROJECTIVE_REDUCTION_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
