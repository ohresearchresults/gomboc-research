# minimum-0303

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# TRIANGULAR_PRISM_SECTION_OBSTRUCTION_AND_EFFECTIVE_EARLY_LARGE_LEFT_CUT_STACK_V1

## 1. New effective early-pencil regions

There is a new all-metric obstruction based on three vertical sections and one horizontal section of a triangular prism. It yields explicit early positive-pencil exclusions with all three left coefficients independently large and the entire closed stack-weight triangle retained. One of the regions allows right coefficients sixteen times larger than the assignment's 1/1024 scale.

The following three parameter boxes are excluded. In each row, require

```text
0 < beta < 1,  s > 0,
r s <= p_j < s,
0 < q_j <= epsilon min(1,s),
u_j >= 0,  u_0+u_1+u_2=1,
0 <= a s <= T.
```

| Region | r | epsilon | T |
|---|---:|---:|---:|
| Early large-left region A | 15/16 | 1/1024 | 1/32 |
| Larger-right region B | 19/20 | 1/64 | 1/64 |
| Longer early interval C | 49/50 | 1/1024 | 1/8 |

**Theorem.** Every actual uniformly filled cut-stack body in this union, centred at its own volume centroid, has **U >= 2 under every SPD metric**. Every complete true weak rooted tree is impossible under every nonzero PSD matrix. No assumption concerning S, a selected root, conditioning, or absence of incidental weak contacts is imposed.

All three left coefficients and all three right coefficients vary independently over the displayed intervals. Both independent stack weights remain free. These are early intervals beginning at a=0, not improvements of a large-a threshold. Since s is arbitrary, the raw parameter a need not be small: for sufficiently small s the regions include a=1 and a>1.

The proof provides an explicit affine normalization in which every selected true tree has an arrow

```text
D_ij < -(1/8192) tr(M).
```

Equivalently, every such tree admits probability weights, depending on the actual body and tree but not on M, with

```text
Q_tree = -sum_e w_e sym[(v_i-g)(v_j-v_i)^T] > Sigma_P/4096.
```

The covariance statement is invariant under undoing the affine normalization.

The full unrestricted-left interval 0 <= a s < 77 is **not** closed here. These new regions cover its large-left end and a substantially wider right-cut scale through a different geometric mechanism. The parent's complete 1/512 small-lateral maximal pencil and unrestricted-left tail a s >= 77 remain unchanged.

## 2. Input, provenance and verification status

Reading completed in the preceding attempt is retained: the entire current journal through line 1952, the complete literal parent, and the entire newly supplied nonzero-PSD refinement source were read.

```text
research-journal.md
349632 bytes
SHA-256 111d3887b2d2d3bd86a8c563b92e693a810d222ca7330431c1f9f6a7e2b65b5d

NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1.md
9577 bytes
SHA-256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b

Literal parent:
minimum-0299
SHA-256 5cc089095e6206c6840a1488aaa2561993c6e28c40bf9b167e7c2e9065cb09fd
```

The explicit results below do not require a numerical value of Gamma_7,10, an older numerical pencil package, or a missing certificate table. They are proved by the section argument and actual moment estimates given here. In particular, I do not infer epsilon_7 >= 1/1024 from the supplied qualitative refinement theorem.

The earlier exploratory Bernstein search on the seven-vertex model did not produce a durable, exact, complete cover in this handoff. Its provisional floating weights and margins are not used. The useful exact left-piece model is retained below.

The new proof and the two exact reference controls are analytical. A complete standard-library checker is included in Section 10, but **no newly observed execution receipt or output-file hash is asserted for it in this continuation**. The control coordinates, true cycles, volume centroids, inverse metric and every primitive category are literal below, so their recovery does not depend on an unobserved output file.

## 3. A quantitative triangular-prism section theorem

Let v_0,v_1,v_2 be the vertices of a regular planar triangle of circumradius one, centred at zero. Thus

```text
sum_i v_i=0,
v_i.v_i=1,
v_i.v_j=-1/2 for i!=j,
sum_i v_i v_i^T=(3/2)I_2.
```

Write Delta=conv(v_0,v_1,v_2) and

```text
Pi = Delta x [-1,1].
```

Let K be an actual uniformly filled convex polytope with centroid zero satisfying

```text
lambda Delta x [-rho,rho] subset K subset Pi,
0 < lambda <= 1,  0 < rho <= 1.
```

Put

```text
A=lambda^2/4,
B=1-rho^2,
C=rho^2,
D=1-lambda^2/2,
Gamma=(A C-B D)/(A+B+C+D).
```

Assume

```text
lambda^2 >= 2/3,
lambda rho >= 2/3,
A C > B D.
```

**Prism section theorem.** K has at least two strict unstable equilibria under every SPD metric. It admits no complete weak rooted tree under any nonzero PSD metric. These qualitative conclusions have no vertex-count restriction.

At most ten true vertices additionally give an arrow below -gamma tr(M) in every selected tree whenever

```text
18 gamma < Gamma.
```

This is a reference-relative geometric obstruction; in the cut-stack application the normalization is explicitly centred at the actual uniform centroid.

### 3.1 Three vertical alternatives

Write a nonzero PSD metric in blocks

```text
M = [[G,c],[c^T,d]],
T=tr(G),
n_i=v_i^T G v_i,
z_i=c.v_i.
```

Then

```text
0 <= n_i <= T,
sum_i n_i=3T/2,
sum_i z_i=0,
tr(M)=T+d.
```

The larger energy of the two contained points above column i is

```text
F_i=lambda^2 n_i+rho^2 d+2 lambda rho |z_i|.
```

For each i consider the central vertical plane

```text
H_i={ (x,h): v_i.x=0 }.
```

The planar section of Delta has endpoints +/-w_i/sqrt(3), where w_i is a unit vector perpendicular to v_i. Consequently the maximum quadratic energy on the outer prism's section is

```text
R_i=(T-n_i)/3+d+(2/3)|z_j-z_k|,
```

where {i,j,k}={0,1,2}.

Summing the three isolated-column gaps gives

```text
sum_i(F_i-R_i)
 = ((3lambda^2-1)/2)T-3(1-rho^2)d
   +2lambda rho sum_i|z_i|-(2/3)sum_i|z_j-z_k|.
```

The last line is nonnegative when lambda rho >= 2/3, because the sum of the three pairwise differences is at most twice the sum of absolute values. Hence some i satisfies

```text
F_i-R_i >= ((3lambda^2-1)/6)T-(1-rho^2)d
          >= (lambda^2/4)T-(1-rho^2)d.
```

The other open halfspace contains columns j and k. Their average supplies the same lower bound:

```text
(F_j+F_k)/2-R_i
 >= (3lambda^2/4-1/3)T+(1/3-lambda^2/2)n_i
    -(1-rho^2)d
 >= (lambda^2/4)T-(1-rho^2)d.
```

The first inequality again uses lambda rho >= 2/3; the second uses n_i<=T and lambda^2>=2/3.

Thus one of the three vertical planes has a contained witness in each open halfspace whose energy exceeds the entire actual section by at least

```text
A T-B d.
```

The witnesses may be interior points of facets; no assignment of the stack point to a prism corner is needed.

### 3.2 The horizontal alternative

The outer section at h=0 is Delta, with maximum energy at most T. Averaging the three contained points at h=+rho cancels the cross term, as does averaging at h=-rho. Each half therefore contains a witness with energy at least

```text
lambda^2 T/2+rho^2 d.
```

The horizontal plane has a two-sided gap at least

```text
C d-D T.
```

For T,d>=0, direct minimization of these two affine bounds gives

```text
max(A T-B d, C d-D T) >= Gamma(T+d).
```

Indeed, after T+d=1 their intersection is at T=(B+C)/(A+B+C+D), and the common value is Gamma. This proves that one of the four planes has a strictly positive two-sided gap for every nonzero PSD metric, including rank-one and rank-two metrics.

### 3.3 Every true root and every weak alternative

Maximize the quadratic energy on K clipped by either closed halfspace of the selected plane. Each half contains a witness strictly above the entire section, so a maximizing vertex lies off the section and is a true vertex of K, rather than a new clipping vertex.

For SPD M, a same-half neighbor has no larger energy, and

```text
2D_ij=f(v_j)-f(v_i)-|v_j-v_i|_M^2<0.
```

An edge leaving the half first crosses the lower section and also has a strictly negative initial primitive. The two open halves therefore contain two distinct strict U vertices.

For PSD M, any weak arrow D_ij>=0 makes the quadratic energy nondecreasing along the whole edge segment. A root path starting at the maximum in a half not containing the root cannot cross the lower section. This excludes every complete weak rooted tree. The same argument permits arbitrary additional contained labels as long as all true vertices are retained.

If all selected arrows on a tree with at most ten vertices were at least -gamma after tr(M)=1, the energy could decrease by at most 2gamma on a whole edge or any traversed fraction. A root path has at most nine edges. The inequality 18gamma<Gamma again forbids its first section crossing.

Separation then gives probability weights on each fixed actual tree with

```text
Q_tree > gamma I.
```

This is existence of a complete actual-tree stress, not a precomputed library of tree coefficients.

### 3.4 Actual covariance

The outer prism has covariance

```text
Sigma_Pi=diag(1/8,1/8,1/3).
```

The actual volume of K is at least lambda^2 rho times the prism volume. Therefore

```text
Sigma_K <= I/(3lambda^2 rho).
```

In particular, lambda^2 rho>2/3 implies Sigma_K<I/2 and

```text
Q_tree > 2gamma Sigma_K.
```

For example, lambda=9/10 and rho=13/15 are admissible. Their inner prism has 351/500 of the outer prism's volume. The theorem concerns every actual centred polytope between these two prisms, not only polytopes with vertices near six designated corners.

## 4. Actual cut-stack chart and true boundary

The literal labels are

```text
0,1,2 = B0,B1,B2;
3,4,5 = L0,L1,L2;
6,7,8 = R0,R1,R2;
9 = S.
```

Use

```text
B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
d_j=1+a p_j,
e_j=1+(1-a)q_j,
d_s=1+a s,
L_j=(-p_j,(B_j)_y,(B_j)_z)/d_j,
R_j=( q_j,(B_j)_y,(B_j)_z)/e_j,
S=(-s,sum_j u_j(B_j)_y,sum_j u_j(B_j)_z)/d_s,
Delta_s=s-sum_j u_j p_j.
```

For p_j<s, Delta_s>0 over the entire closed weight triangle. The maximal positive-denominator interval is -1/s<a<1+1/max(q_j). All denominators are positive in the three new boxes because a>=0 and a q_j<1 there.

For positive weights the true maximal cycles and genuine edges are

```text
F0=(0,3,4,1,7,6)  F1=(0,2,5,3)  F2=(0,6,8,2)
F3=(1,4,5,2)      F4=(1,2,8,7)  F5=(3,9,4)
F6=(3,5,9)        F7=(4,9,5)    F8=(6,7,8)

02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

The seven actual positive tetrahedra and their six-volumes remain

```text
(0,1,2,5): p2/d2
(0,1,4,5): p1/(d1 d2)
(0,3,4,5): p0/(d0 d1 d2)
(3,4,5,9): Delta_s/(d_s d0 d1 d2)
(0,1,2,8): q2/e2
(0,1,7,8): q1/(e1 e2)
(0,6,7,8): q0/(e0 e1 e2).
```

With weights w_t, vertex sums C_t and sums of outer products J_t, the one actual uniform centre is

```text
D_full=sum_t w_t,
Vol(P_a)=D_full/6,
g_a=sum_t w_t C_t/(4D_full),
E[XX^T]=sum_t w_t(C_t C_t^T+J_t)/(20D_full),
Sigma_a=E[XX^T]-g_a g_a^T.
```

Every projective member is refilled uniformly. The new argument does not transport an old centroid or a density along the pencil.

The true weight-boundary changes are retained:

```text
u0=0: merge F3/F7 and delete L1--L2;
u1=0: merge F1/F6 and delete L0--L2;
u2=0: merge F0/F5 and delete L0--L1.
```

Exactly one zero weight gives **10/16/8**. The first two mergers are pentagonal and the third heptagonal. At u_j=1, two mergers occur and L_j is strictly between B_j and S; removing that redundant label gives **9/14/7**. The section theorem is applied to the resulting true body. It does not retain deleted edges or use a nine-vertex theorem on a ten-vertex weight edge.

## 5. A seven-vertex left piece with exact moments

The comparison used here is the actual left piece

```text
P_left=P_a intersect {x<=0}=conv(B0,B1,B2,L0,L1,L2,S).
```

It is **not** the parent's harmonic seven-vertex core conv(L0,L1,L2,R0,R1,R2,S), and it is not either of the earlier comparison tetrahedra. Its centroid is not substituted for the centroid of P_a.

Put

```text
t=a s,
theta=t/(1+t),
r_j=p_j/s,
f_j=r_j(1+t)/(1+t r_j),
k_j=1-theta f_j,
k_s=1-theta.
```

Let O_beta=(1-beta)v_0+beta v_1. Define the nonsingular planar linear map A_beta by

```text
A_beta(1,0)=v_1-v_0,
A_beta(0,1)=v_2-O_beta.
```

The following is one affine change of coordinates, not a projective transport of a measure:

```text
H=-(1+t)x/s,
V=A_beta(y,z)+(1+a x)O_beta.
```

In these coordinates,

```text
B_j=(v_j,0),
L_j=(k_j v_j,f_j),
S=(k_s U,1),       U=sum_j u_j v_j,
R_j=((v_j+q_j O_beta)/e_j,-kappa_j),
kappa_j=(1+t)q_j/(s e_j).
```

Each right vertex satisfies

```text
(v_j+q_j O_beta)/e_j
 =(1+theta kappa_j)(v_j+q_j O_beta)/(1+q_j).
```

Thus every actual point belongs to the same cone

```text
V in (1-theta H)Delta.
```

If r_j>=r, then f_j>=r. The left piece contains the entire frustum

```text
0<=H<=r,   V in (1-theta H)Delta,
```

and its sections agree with that frustum for H<=r.

### 5.1 Exact left-piece transverse centroid

In the seven-label order B0,B1,B2,L0,L1,L2,S, the four positive-cell weights, after cancelling the common base-area factor, are

```text
f2,
f1 k2,
f0 k1 k2,
W=sum_i u_i(1-f_i)k_j k_k,  {i,j,k}={0,1,2}.
```

Define

```text
Kprod=k0 k1 k2,
L=Kprod-theta W=k_s sum_i u_i k_j k_k,
D=f2+f1 k2+f0 k1 k2+W.
```

For theta>0, D=(1-L)/theta. At theta=0, D=1+sum_i(1-u_i)f_i. The actual left-piece volume is Area(Delta)D/3, and its exact transverse first-moment identity is

```text
4D g_left,V = L sum_i f_i v_i+k_s W U.
```

One derivation subtracts the tetrahedron above the L-plane from the full cone tetrahedron and then adds the actual stack tetrahedron. Its volume and first moment are coupled actual quantities. Equivalently, the displayed four positive cells give the same identity directly.

The following bound is uniform over the entire weight triangle:

```text
g_left,V in delta_0 Delta,
delta_0=3(1-r)/(4(1+2r)).
```

To prove it, subtract the common coefficient Lr from the coefficients of v_i in the first-moment identity. All remaining coefficients are nonnegative. Moreover,

```text
k_s W/L
```

is a weighted average of the numbers 1-f_i, with weights proportional to u_i k_j k_k. If m=min f_i, their total is at most

```text
L[sum_i f_i-3r+1-m] <=3(1-r)L.
```

Finally L/D<=1/(1+2r). For theta=0 this is D>=1+2r. For theta>0 use

```text
L <= (1-theta)(1-theta r)^2,
1/[(1-theta)(1-theta r)^2] >=1+theta(1+2r).
```

This proves the centroid inclusion without assigning independent masses to cells.

### 5.2 Exact height control

The left piece is vertically downward closed: the projection of every point belongs to the base Delta, and the segment down to the base is contained in the body. Its section areas are nonincreasing on 0<=H<=1. Therefore

```text
g_left,H <=1/2.
```

All additional volume beyond the complete frustum 0<=H<=r lies at H>=r. Thus

```text
g_left,H >= mu_r(theta),
mu_r(theta)
 = r[1/2-(2/3)theta r+(1/4)(theta r)^2]
     /[1-theta r+(1/3)(theta r)^2].
```

This mean decreases with theta: the density ratio of two functions (1-theta H)^2 is decreasing in H when theta increases. These are actual section integrals, not a centroid of the seven vertices.

## 6. An explicit rational box criterion

The preceding model yields a general sufficient criterion, not just the three convenient boxes.

Choose

```text
1/2 < r < 1,
T>=0,
epsilon>0,
T epsilon<1.
```

For all chart members with r_j>=r, 0<=t<=T and q_j<=epsilon min(1,s), define the following rational bounds:

```text
Theta=T/(1+T),
K=(1+T)epsilon/(1-T epsilon),
R=1+Theta K,
ell=1-Theta r,
v=r ell^2,
w=K R^2,
chi=w/(v+w),
delta_0=3(1-r)/(4(1+2r)),
delta=delta_0+chi R,
x=Theta r,
mu=r[1/2-2x/3+x^2/4]/[1-x+x^2/3],
b=(1-chi)mu-chi K.
```

Require ell>delta and b>0. Set

```text
lambda_bar=(ell-delta)/(R+2delta),
rho_bar=min(
 b/(b+K),
 b/(1-b),
 (r-1/2)/(1/2+K),
 2r-1).
```

Any positive lambda<=lambda_bar and rho<=rho_bar satisfying the prism section theorem certify the whole continuous box, with the full weight triangle.

### Why these are actual-centroid bounds

The true right piece is P_right=P_a intersect {x>=0}=conv(B0,B1,B2,R0,R1,R2). In the affine coordinates above it has -K<=H<=0 and V in R Delta. Its actual volume is at most Area(Delta)w. The actual left-piece volume is at least Area(Delta)v. Hence the actual right-volume fraction is at most chi.

Combining the actual volume centroids of these two disjoint-interior pieces gives

```text
g_V in delta Delta,
b<=g_H<=1/2.
```

The first estimate uses g_left,V in delta_0 Delta and g_right,V in R Delta. The second uses g_right,H in [-K,0] and the actual left height bounds. The same true volume fraction is used for all three coordinates.

The actual body contains ell Delta x [0,r] and is contained in R Delta x [-K,1]. Since -Delta subset 2Delta,

```text
(ell-delta)Delta subset ell Delta-g_V,
R Delta-g_V subset (R+2delta)Delta.
```

Let

```text
B_g=max(g_H+K,1-g_H).
```

Subtract the actual g and divide the transverse coordinates by R+2delta and the height coordinate by B_g. This is an affine normalization of the genuinely refilled body, with actual centroid zero. The outer body is Pi. The contained balanced height fraction is

```text
min(g_H,r-g_H)/max(g_H+K,1-g_H).
```

On b<=g_H<=1/2, its lower bound is exactly the stated minimum of four endpoint ratios. The first two component ratios increase with g_H, and the other two decrease. Therefore the normalized body contains

```text
lambda_bar Delta x [-rho_bar,rho_bar].
```

This proves the rational box criterion. It also explains why the left-piece centroid must not be frozen: the right piece enters both the transverse and vertical bounds before the final normalization.

## 7. Exact guards for the three new regions

The following rational comparison prisms work:

| Region | lambda | rho | Gamma |
|---|---:|---:|---:|
| A | 23/25 | 43/50 | 39379/11177500 |
| B | 9/10 | 13/15 | 361/161775 |
| C | 87/100 | 53/60 | 1595479/260751600 |

Each row satisfies

```text
lambda^2>=2/3,
lambda rho>=2/3,
lambda^2 rho>2/3,
Gamma>18/8192.
```

For audit, the following simpler intermediate guards suffice.

### Region A

```text
K=33/32767 <1/900,
R=32768/32767 <1001/1000,
ell=171/176,
chi<1/875,
delta<9/512,
mu=2683365/5780032 >475/1024,
b>237/512.
```

For example, the height conclusion follows from

```text
b > (874/875)(475/1024)-1/(875*900) >237/512.
```

The displayed bounds give lambda_bar>23/25 and rho_bar>43/50.

### Region B

```text
K=1/63,
R=4096/4095 <2001/2000,
ell=1281/1300,
chi<1/59,
delta<3/100,
mu=188926177/399700880 >121/256,
b>13/28.
```

The last inequality has the exact positive slack

```text
58(121/256)-1/63-59(13/28)=43/8064.
```

Also

```text
(19/20-1/2)/(1/2+1/63)=567/650 >13/15.
```

These imply lambda_bar>9/10 and rho_bar>13/15. For this region,

```text
Gamma-18/8192
 =45362/(8192*161775)>0.
```

### Region C

```text
K=9/8191 <11/10000,
R=8192/8191 <1001/1000,
ell=401/450,
chi<1/700,
delta<13/2000,
mu=51244347/108750200 >241/512,
b>47/100.
```

These imply lambda_bar>87/100 and rho_bar>53/60.

Thus gamma=1/8192 works uniformly for all three boxes. Their inner-prism volume fractions are respectively

```text
22747/31250,
351/500,
401157/600000,
```

all strictly greater than 2/3. The covariance stress gap 1/4096 follows from Section 3.4.

These comparisons are rational endpoint guards for a proved continuous argument. They are not a finite sample of shapes or metrics.

## 8. Exact reference controls and a real limitation of the new sufficient condition

The controls below preserve the useful seven-vertex geometry without pretending that it is a ten-vertex cut-stack body. Both are actual uniformly filled rational polytopes, with a complete same-inverse physical census supplied analytically.

Use one physical pair

```text
M=[[3,3/2,0],[3/2,3,0],[0,0,1]],
N=[[4/9,-2/9,0],[-2/9,4/9,0],[0,0,1]]=M^(-1).
```

### Control 1: the comparison prism

Vertices 0..5 are

```text
(0,0,-1),(1,0,-1),(0,1,-1),
(0,0, 1),(1,0, 1),(0,1, 1).
```

True outward cycles are

```text
(0,2,1),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5).
```

The actual volume is 1 and centroid is (1/3,1/3,0). Its true f-vector is 6/9/5. The complete primitive categories are:

```text
Six horizontal edges:
  primal pair (-3/2,-3/2), polar pair (-1,-4).
Three vertical edges 03,14,25:
  primal pair (-2,-2), polar pair (-6,-6).
```

The order of the polar pair depends only on the ordering of its two incident facets. Every one of the 36 primitives is negative. Hence its strict physical census is

```text
(S,U,H)=(5,6,9), physical weak count 0.
```

This is a reference prism, not an attaining body or an interior ten-vertex chart member.

### Control 2: a middle-left seven-vertex core

Vertices 0..6 are

```text
(0,0,0),(1,0,0),(0,1,0),
(0,0,1/2),(1,0,1/2),(0,1,1/2),
(1/3,1/3,1).
```

True outward cycles are

```text
(0,2,1),
(0,1,4,3),(1,2,5,4),(2,0,3,5),
(3,4,6),(4,5,6),(5,3,6).
```

The true f-vector is 7/12/7. Its actual volume is 1/3 and centroid is

```text
(1/3,1/3,11/32).
```

It is the q=0, a=0 left-piece model with equal relative left cuts 1/2 and uniform stack weights. The complete 48-primitive categories are

```text
Bottom triangle edges 01,02,12:
  primal (-3/2,-3/2), polar (-1024/121,-4).
Vertical edges 03,14,25:
  primal (-11/64,-5/64), polar (-6,-6).
Upper rim edges 34,35,45:
  primal (-3/2,-3/2), polar (-20/21,-704/441).
Apex edges 36,46,56:
  primal (-59/64,-21/64), polar (-512/147,-512/147).
```

Again every primitive is negative, so the strict physical census is

```text
(S,U,H)=(7,7,12), physical weak count 0.
```

This actual middle-left core is outside the new large-left hypotheses. The general prism-envelope criterion does not close it: at the coarse r=1/2 limit its guaranteed balanced inner height is zero. That failure is not a U1 survivor; this displayed metric has seven U vertices, and the supplied nonzero-PSD refinement theorem separately applies to its seven-vertex uniformly centred hull.

These controls total 84 nonzero genuine-edge primitives. Their counts are not claimed to be counts on any new 10/17/9 body.

## 9. Reusable model and remaining obstacle

The exact seven-vertex left-piece model remains useful outside the newly proved region. For independent theta, f_0,f_1,f_2 in [0,1] and closed u, its vertices are

```text
B_i=(v_i,0),
L_i=((1-theta f_i)v_i,f_i),
S=((1-theta)sum_i u_i v_i,1).
```

Its four positive-cell formulas in Section 5 reconstruct D and the entire centroid. Its volume factor satisfies 1<=D<=3: it contains the base-and-S tetrahedron and is contained in Delta x [0,1]. The true interior left-core graph is

```text
01,02,12,03,14,25,34,35,45,36,46,56.
```

For future exact polynomial work, let J=4Dg from those actual cells and define

```text
A_ij=-sym[(4D X_i-J)(X_j-X_i)^T].
```

Then

```text
tr(M A_ij)=-4D D_ij.
```

These are polynomial actual-centroid arrow matrices. They must not be replaced by independent cell masses. A complete polynomial cover of this model could extend the present early result into the middle-left regime; no such cover is claimed here.

The parent's harmonic-core sandwich and positive but unevaluated Gamma_7,10 remain valid. This result does not evaluate that general constant. Instead it uses the special downward-closed left piece, its exact transverse moment cancellation, and a new explicit prism section obstruction.

For unrestricted 0<p_j<s at the assignment's 1/1024 right scale, the portions of 0<=a s<77 outside the new boxes, the rational prism gate and earlier accepted regions remain unresolved. Region B adds coverage at the larger 1/64 right scale, but it does not exclude arbitrary large right cuts or the complete eleven-parameter incidence.

No complete U1 or joint110 physical survivor was obtained. No whole cut-stack incidence, E17 type, canonical root registry count or global complexity bound is subtracted. The accepted working bracket remains **34<=C_min<=622**.

## 10. Complete supplementary exact checker

This source has no external inputs or parent imports. It checks the rational box guards, reconstructs the true supporting facets and actual volume centroids of both controls, verifies the common inverse, and checks all 84 primitive values against the complete categories above.

Save as `early_prism.py` and run with assertions enabled:

```text
python -B -S early_prism.py
```

CPython 3.13.5 and the standard library suffice. The expected final markers are

```text
EARLY_CUT_STACK_THREE_BOXES_ALL_RATIONAL_GUARDS_PASS
PRISM_6_9_5_STRICT_5_6_9_WEAK0_PASS
STACK_CORE_7_12_7_STRICT_7_7_12_WEAK0_PASS
ANALYTICAL_CONTROLS_84_NONZERO_PRIMITIVES_PASS
```

These are expected reconstruction markers, not an asserted execution receipt. The continuous theorem is proved in Sections 3–7; the checker is not a sampling argument for that continuum.

```python
from fractions import Fraction as F
from itertools import combinations


def box_bounds(r, T, eps):
    assert F(1,2) < r < 1 and T >= 0 and eps > 0 and T*eps < 1
    theta = T/(1+T)
    K = (1+T)*eps/(1-T*eps)
    R = 1+theta*K
    ell = 1-theta*r
    v = r*ell*ell
    w = K*R*R
    chi = w/(v+w)
    delta0 = 3*(1-r)/(4*(1+2*r))
    delta = delta0+chi*R
    x = theta*r
    mu = r*(F(1,2)-2*x/3+x*x/4)/(1-x+x*x/3)
    b = (1-chi)*mu-chi*K
    assert ell > delta and 0 < b < F(1,2)
    lam = (ell-delta)/(R+2*delta)
    rho = min(b/(b+K), b/(1-b),
              (r-F(1,2))/(F(1,2)+K), 2*r-1)
    return dict(K=K, R=R, ell=ell, chi=chi, delta=delta,
                mu=mu, b=b, lam=lam, rho=rho)


def prism_gap(lam, rho):
    assert 0 < lam <= 1 and 0 < rho <= 1
    assert lam*lam >= F(2,3) and lam*rho >= F(2,3)
    A = lam*lam/4
    B = 1-rho*rho
    C = rho*rho
    D = 1-lam*lam/2
    assert A*C > B*D
    return (A*C-B*D)/(A+B+C+D)


REGIONS = [
    (F(15,16), F(1,32), F(1,1024), F(23,25), F(43,50),
     F(39379,11177500), F(1,900), F(1,875), F(9,512),
     F(237,512), F(2683365,5780032)),
    (F(19,20), F(1,64), F(1,64), F(9,10), F(13,15),
     F(361,161775), F(1,63), F(1,59), F(3,100),
     F(13,28), F(188926177,399700880)),
    (F(49,50), F(1,8), F(1,1024), F(87,100), F(53,60),
     F(1595479,260751600), F(11,10000), F(1,700), F(13,2000),
     F(47,100), F(51244347,108750200))
]

for r,T,eps,lam,rho,expected,Kmax,chimax,deltamax,bmin,mu in REGIONS:
    z = box_bounds(r,T,eps)
    assert z['K'] <= Kmax
    assert z['chi'] < chimax and z['delta'] < deltamax
    assert z['b'] > bmin and z['mu'] == mu
    assert z['lam'] > lam and z['rho'] > rho
    gap = prism_gap(lam,rho)
    assert gap == expected and gap > 18*F(1,8192)
    assert lam*lam*rho > F(2,3)
print('EARLY_CUT_STACK_THREE_BOXES_ALL_RATIONAL_GUARDS_PASS')


def vec(x):
    return tuple(F(a) for a in x)


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))


def scale(a,x):
    return tuple(a*b for b in x)


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],
            x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0])


def det(A):
    return dot(A[0],cross(A[1],A[2]))


def mv(A,x):
    return tuple(dot(row,x) for row in A)


def mm(A,B):
    return [[dot(row,col) for col in zip(*B)] for row in A]


M = [[F(3),F(3,2),F(0)],
     [F(3,2),F(3),F(0)],
     [F(0),F(0),F(1)]]
N = [[F(4,9),F(-2,9),F(0)],
     [F(-2,9),F(4,9),F(0)],
     [F(0),F(0),F(1)]]
assert mm(M,N) == [[F(i==j) for j in range(3)] for i in range(3)]
assert M[0][0] > 0
assert M[0][0]*M[1][1]-M[0][1]**2 > 0 and det(M) > 0


def supporting_sets(V):
    result = set()
    for i,j,k in combinations(range(len(V)),3):
        n = cross(sub(V[j],V[i]),sub(V[k],V[i]))
        if n == (0,0,0):
            continue
        h = dot(n,V[i])
        slacks = [h-dot(n,x) for x in V]
        if min(slacks) >= 0 or max(slacks) <= 0:
            result.add(frozenset(a for a,s in enumerate(slacks) if s == 0))
    return result


def audit(V, cycles, expected_volume, expected_g, kind):
    V = [vec(v) for v in V]
    inside = tuple(sum(v[j] for v in V)/len(V) for j in range(3))
    cycles = [list(c) for c in cycles]
    assert {frozenset(c) for c in cycles} == supporting_sets(V)
    supports = []
    total = F(0)
    first = (F(0),F(0),F(0))
    for c in cycles:
        n = cross(sub(V[c[1]],V[c[0]]),sub(V[c[2]],V[c[0]]))
        h = dot(n,V[c[0]])
        if h-dot(n,inside) < 0:
            c.reverse()
            n = cross(sub(V[c[1]],V[c[0]]),sub(V[c[2]],V[c[0]]))
            h = dot(n,V[c[0]])
        assert h-dot(n,inside) > 0
        slacks = [h-dot(n,x) for x in V]
        assert min(slacks) >= 0
        assert {i for i,s in enumerate(slacks) if s == 0} == set(c)
        for k in range(len(c)):
            a,b,d = c[k],c[(k+1)%len(c)],c[(k+2)%len(c)]
            assert dot(cross(sub(V[b],V[a]),sub(V[d],V[b])),n) > 0
        supports.append((n,h))
        for k in range(1,len(c)-1):
            tet = [inside,V[c[0]],V[c[k]],V[c[k+1]]]
            w = abs(det([sub(tet[j],tet[0]) for j in (1,2,3)]))
            assert w > 0
            total += w
            C = tuple(sum(x[j] for x in tet) for j in range(3))
            first = add(first,scale(w,C))
    volume = total/6
    g = scale(1/(4*total),first)
    assert volume == expected_volume and g == expected_g
    edges = sorted({tuple(sorted((c[k],c[(k+1)%len(c)])))
                    for c in cycles for k in range(len(c))})
    assert len(V)-len(edges)+len(cycles) == 2
    X = [sub(v,g) for v in V]
    poles = [scale(1/(h-dot(n,g)),n) for n,h in supports]
    primal = {}
    polar = {}
    saddle_count = 0
    for i,j in edges:
        fs = [f for f,c in enumerate(cycles) if i in c and j in c]
        assert len(fs) == 2
        f,h = fs
        p = (dot(X[i],mv(M,sub(X[j],X[i]))),
             dot(X[j],mv(M,sub(X[i],X[j]))))
        q = (dot(poles[f],mv(N,sub(poles[h],poles[f]))),
             dot(poles[h],mv(N,sub(poles[f],poles[h]))))
        primal[i,j],primal[j,i] = p
        polar[f,h],polar[h,f] = q
        assert max(p+q) < 0
        saddle_count += 1
        if kind == 'prism':
            if j == i+3:
                ep = (F(-2),F(-2))
                eq = (F(-6),F(-6))
            else:
                ep = (F(-3,2),F(-3,2))
                eq = (F(-1),F(-4))
        else:
            if j < 3:
                ep = (F(-3,2),F(-3,2))
                eq = (F(-1024,121),F(-4))
            elif i >= 3 and j < 6:
                ep = (F(-3,2),F(-3,2))
                eq = (F(-20,21),F(-704,441))
            elif j == 6:
                ep = (F(-59,64),F(-21,64))
                eq = (F(-512,147),F(-512,147))
            else:
                assert j == i+3
                ep = (F(-11,64),F(-5,64))
                eq = (F(-6),F(-6))
        assert sorted(p) == sorted(ep) and sorted(q) == sorted(eq)
    U = sum(all(value < 0 for (i,j),value in primal.items() if i == v)
            for v in range(len(V)))
    S = sum(all(value < 0 for (i,j),value in polar.items() if i == f)
            for f in range(len(cycles)))
    assert S+U-saddle_count == 2
    if kind == 'prism':
        assert (len(V),len(edges),len(cycles)) == (6,9,5)
        assert (S,U,saddle_count) == (5,6,9)
        print('PRISM_6_9_5_STRICT_5_6_9_WEAK0_PASS')
    else:
        assert (len(V),len(edges),len(cycles)) == (7,12,7)
        assert (S,U,saddle_count) == (7,7,12)
        print('STACK_CORE_7_12_7_STRICT_7_7_12_WEAK0_PASS')
    return 4*len(edges)


prism = [(0,0,-1),(1,0,-1),(0,1,-1),
         (0,0,1),(1,0,1),(0,1,1)]
prism_faces = [(0,2,1),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)]
count = audit(prism,prism_faces,F(1),(F(1,3),F(1,3),F(0)),'prism')
stack = [(0,0,0),(1,0,0),(0,1,0),
         (0,0,F(1,2)),(1,0,F(1,2)),(0,1,F(1,2)),
         (F(1,3),F(1,3),1)]
stack_faces = [(0,2,1),(0,1,4,3),(1,2,5,4),(2,0,3,5),
               (3,4,6),(4,5,6),(5,3,6)]
count += audit(stack,stack_faces,F(1,3),
               (F(1,3),F(1,3),F(11,32)),'stack')
assert count == 84
print('ANALYTICAL_CONTROLS_84_NONZERO_PRIMITIVES_PASS')
```
