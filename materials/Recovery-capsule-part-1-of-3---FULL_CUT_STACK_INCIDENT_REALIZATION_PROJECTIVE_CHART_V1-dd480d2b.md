# material-dd480d2ba12b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL_CUT_STACK_INCIDENT_REALIZATION_PROJECTIVE_CHART_SEVEN_POSITIVE_TETS_V1

## Status and scope

This is a coordinator-authored analytical theorem and a complete three-part recovery capsule. It covers the entire labelled affine realization space of the ONE literal maximal-facet incidence below, not all E17 combinatorial types. The theorem is proved below independently of a finite scan. Five new rational controls, their actual homogeneous moments and full physical censuses, and a symbolic one-parameter moment calculation were executed normally and in a fresh directory containing only the two source files. Both cold outputs were byte-identical to the original outputs. No worker replay, proof-assistant formalization, U>=2 theorem, proper110 survivor or improvement of C_min is claimed.

The regular finite shapes at the formerly named ghost-apex horizons are internal sections of this complete chart. They cannot be removed with a <=9-vertex boundary theorem. The canonical attaining C622 and the accepted lower exclusion C>=34 remain unchanged.

This capsule is self-contained: Part 2 is the complete standard-library source [internal-source-reference], Part 3 is the complete SymPy source [internal-source-reference], and Part 1 is this proof/recovery description. The earlier CUT_STACK_ELEVEN_MODULI_REGULAR_RIGHT_HORIZON_V1 capsule ([internal-source-reference], [internal-source-reference], [internal-source-reference]) motivated the question but supplies no missing recovery input. The exact new chart and controls do not depend on the native-eight stress source.

## 1. Literal true incidence

Use labels B_j=j, L_j=3+j, R_j=6+j, j=0,1,2, and S=9. The outward cycles of the nine maximal facets are, in this order:

```
(0,3,4,1,7,6)
(0,2,5,3)
(0,6,8,2)
(1,4,5,2)
(1,2,8,7)
(3,9,4)
(3,5,9)
(4,9,5)
(6,7,8)
```

There are ten distinct true vertices, seventeen true edges and nine maximal facets. The edges are

```
02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

Facet fan diagonals and the seven tetrahedral integration cells below are not additional edges or facets. The statements are for this labelled incidence; a change of labels must carry all cycles and formulas with it.

## 2. Complete eleven-parameter affine chart

Choose the following independent data:

- beta in (0,1);
- p_j>0 and q_j>0 for j=0,1,2;
- u_j>0 with u_0+u_1+u_2=1;
- p_s>sum_j u_j p_j; write delta=p_s-u.p>0;
- a real number a such that d_j=1+a p_j>0, d_s=1+a p_s>0 and e_j=1+(1-a)q_j>0.

Equivalently, the last condition is the single open interval

```
-1/max(p0,p1,p2,p_s) < a < 1+1/max(q0,q1,q2).
```

It always contains the closed interval [0,1]. There are eleven parameters: one beta, six p/q, two independent u, one p_s and one a.

Set

```
B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
b_j=(B_j)_yz, b_u=sum_j u_j b_j,
L_j=(-p_j/d_j, b_j/d_j),
R_j=(q_j/e_j, b_j/e_j),
S=(-p_s/d_s, b_u/d_s).
```

THEOREM 1. Every parameter tuple in this domain is a convex uniformly fillable three-body with precisely the true incidence in Section 1. Conversely every labelled convex realization with exactly those maximal cycles is affinely equivalent to one of these tuples. The inverse construction is explicit in Section 4. Thus this is a full realization chart, not merely an eleven-dimensional example family inferred from a dimension count.

All coordinates are rational in the parameters. Rational parameters give an actual rational polyhedron, and its homogeneous centroid, covariance and every physical true-feature test under a rational SPD matrix are rational as well.

## 3. Direct construction and the two regular sections

For any point (x,y,z) define transverse barycentric affine functions

```
lambda0=(1-beta)(1-z)-y,
lambda1=beta(1-z)+y,
lambda2=z,
lambda0+lambda1+lambda2=1,
w=(1-beta,beta,0),
nu=lambda-x w.
```

First put a=0. The proposed body is exactly the intersection of the following nine inward halfspaces:

```
z>=0,
lambda0>=0, lambda1>=0,
nu0>=0, nu1>=0,
-x+q.nu>=0,
x+p.lambda+delta lambda_i/u_i>=0 for i=0,1,2.
```

To determine that intersection rather than assume its incidence, split at x=0. When x<=0, lambda is in the standard triangle, the right-side inequalities are automatic, and the left roof is

```
0 <= -x <= p.lambda+delta min_i(lambda_i/u_i).
```

The upper depth is positive and concave over the triangle. Its three affine pieces meet at lambda=u, producing exactly L0,L1,L2 and S. Each of the three triangular roof pieces has positive area, since delta and all u_i are positive. The lower boundary is the triangle B0B1B2. The two nonbasal left side facets are strict quadrilaterals.

When x>=0, nu>=0 and sum nu=1-x. The right cap implies x<1. Set rho=x/(1-x) and v=nu/(1-x); then v lies in the standard triangle and

```
0<=rho<=q.v.
```

This is the positive projective image of a triangular prism with a positive affine roof. Its six vertices are B_j and R_j. All left roof inequalities are strict here. The two nonbasal right side facets are strict quadrilaterals, and the upper cap is the strict triangle R0R1R2. The common z=0 facet is the strict hexagon B0,L0,L1,B1,R1,R0. In particular beta in (0,1) gives strictly different inward left/right slopes at B0 and B1; these two labels are not straight points of that hexagon. This lists all nine supporting facets and all ten true vertices.

For arbitrary a in the stated interval apply the projective map

```
Phi_a(X)=X/(1-a X_x)
```

to this a=0 body. Its denominator at B_j is 1, at L_j is 1+a p_j, at S is 1+a p_s, and at the a=0 right vertex is [1+(1-a)q_j]/(1+q_j). All are strictly positive. An affine denominator positive at all vertices is positive on the whole convex hull, so Phi_a is a nonsingular projectivity on the entire body. It carries line segments to line segments with positive weights and preserves the exact face lattice. Its vertex images are precisely Section 2. This proves the forward part of Theorem 1.

The a=0 section has three nonzero parallel true edges B_j L_j. The a=1 section has three nonzero parallel true edges B_j R_j. For 0<a<1 the side planes meet at the two opposite finite ghost apices (-1/a,0,0) and (1/(1-a),0,0). At a=0 or 1 one of these ghost points is at infinity, without losing any of the ten actual vertices. Values a<0 and a>1 are also allowed and give genuine shapes with one expanding side. They are not covered by the finite opposite-ghost operation domain.

Equivalently, relative to the a=1 body,

```
P_a={X/[1+(1-a)X_x]: X in P_1}.
```

These maps are projective, not affine. Uniformly refilling their images changes the own centroid and may change equilibria. No equilibrium exclusion may be transferred along this pencil merely from projective equivalence.

## 4. Proof of surjectivity and a rational affine inverse

Take any convex realization with exactly the cycles of Section 1. The true base hexagon has diagonal B0B1. Its strict convexity puts L0,L1 and R0,R1 on opposite sides of that line. The plane through B0,B1,B2 therefore separates these two pairs. In the true left quadrilateral B0,B2,L2,L0, the supporting edge B0B2 puts L2 on the same side of that plane as L0; the right quadrilateral gives the corresponding claim for R2. Thus L_j have negative transverse coordinate x and R_j have positive x after orienting x. This also proves that B0,B1,B2,L0 are affinely independent.

Use the affine frame whose origin is B0 and whose columns are

```
B0-L0, B1-B0, B2-B0.
```

In raw coordinates B0=(0,0,0), B1=(0,1,0), B2=(0,0,1), L0=(-1,0,0). Write raw lambda0=1-y-z and lambda1=y. The two left quadrilateral planes and the two right quadrilateral planes have equations

```
lambda0+A0 x=0, lambda1+A1 x=0,
lambda0+B0c x=0, lambda1+B1c x=0,
```

with their inward values normalized to 1 at the opposite B label. Their coefficients are obtained without an arbitrary choice of scale:

```
A0=-lambda0(L1)/x(L1), A1=-lambda1(L0)/x(L0),
B0c=-lambda0(R1)/x(R1), B1c=-lambda1(R0)/x(R0).
```

For example A1=0 in this raw frame, but keeping the formula makes its geometric meaning transparent. Evaluate a left inward form at the corresponding right vertex: since x(R_j)>0 and that vertex is strictly off the left facet, this gives

```
A0>B0c, A1>B1c.
```

Put h=A0+A1, k=B0c+B1c, Delta=h-k>0, and define

```
beta=(A1-B1c)/Delta in (0,1),
a=h/Delta,
x'=Delta x,
y'=y-beta+beta z+(A1-beta h)x,
z'=z.
```

This is an invertible affine map. In these canonical coordinates the two left forms are lambda_i+a w_i x for i=0,1, the two right forms are lambda_i+(a-1)w_i x, and the common basal form is z. The B coordinates are those in Section 2.

Let mu=(lambda0+a w0 x,lambda1+a w1 x,z). Each mu_i is nonnegative on the whole actual body. Their sum is 1+a x and is strictly positive everywhere: if it vanished at a point of the hull, all three left side forms would vanish there; no actual vertex belongs to all three corresponding facets, and positive convex combinations cannot make a sum of nonnegative forms zero unless their vertices already do. Hence

```
X -> X/(1+a X_x)
```

is a positive projectivity on the whole canonical body. It sends the left side forms to ordinary triangle barycentrics lambda and the right forms to nu=lambda-x w. It fixes the B triangle. Consequently the left vertices become (-p_j,b_j) with p_j>0. Right vertices have x in (0,1), nu=(1-x)e_j, and therefore have the exact form (q_j/(1+q_j),b_j/(1+q_j)) with q_j>0.

The stack label S is strictly off every left side facet. In the projected body its three transverse barycentrics u_i are therefore positive and sum to 1. Write its first coordinate as x_s. The roof face through S and L_j,L_k, where i is the omitted index, has an equation

```
x+p.lambda+gamma_i lambda_i=0,
gamma_i=-(x_s+p.u)/u_i.
```

The coefficient of x can be normalized this way because u_i>0. At B_j with j!=i the inward value is p_j>0. At L_i the strict off-facet inward value is gamma_i; hence gamma_i>0. It follows that x_s+p.u<0. Thus p_s=-x_s>p.u, exactly the domain condition. This argument does not assume that deleting S leaves an already known convex operation.

Undoing the positive projectivity gives exactly Section 2. Positivity of its inverse denominators gives every d_j,d_s,e_j>0. Direct recovery in canonical coordinates is

```
p_j=-x(L_j)/(1+a x(L_j)),
q_j=x(R_j)/(1+(a-1)x(R_j)),
f_s=1+a x(S), p_s=-x(S)/f_s,
u2=z(S)/f_s,
u1=y(S)/f_s+beta(1-u2), u0=1-u1-u2.
```

This establishes the converse and supplies a rational affine invariant inverse for labelled realizations. The apparent line "nu2" in the formula block denotes u2, not the right-side vector nu: explicitly u_2=z(S)/f_s. The complete source uses unambiguous variable names u2,u1,u.

## 5. Seven positive tetrahedra and true homogeneous moments

The body is partitioned, up to shared faces, into these seven tetrahedra:

```
(0,1,2,5), (0,1,4,5), (0,3,4,5), (3,4,5,9),
(0,1,2,8), (0,1,7,8), (0,6,7,8).
```

At a=0, the first three triangulate the positive affine left prism; the fourth is its actual stacked tetrahedron. One may split the remaining pyramid with apex L2 by the base-quad diagonal B0L1 to obtain the indicated left triangulation. The right prism has the analogous triangulation after its positive projective map. Positive projectivities preserve the decomposition. The determinant transformation divides a tetrahedral six-volume by the product of its four positive vertex denominators, proving the following seven positive six-volumes:

```
w1=p2/d2,
w2=p1/(d1 d2),
w3=p0/(d0 d1 d2),
w4=delta/(d_s d0 d1 d2),
w5=q2/e2,
w6=q1/(e1 e2),
w7=q0/(e0 e1 e2).
```

Let D=sum_t w_t. If C_t is the sum of the four vertex vectors of cell t and Q_t is the sum of their four outer products, the actual uniform moments are

```
Vol(P)=D/6,
g=sum_t w_t C_t/(4D),
E_P XX^T=sum_t w_t(C_t C_t^T+Q_t)/(20D),
Sigma=E_P XX^T-g g^T.
```

All weights are actual positive cell volumes. No prescribed centroid, ghost volume subtraction, freely assigned vertex mass, or independent polar centroid occurs. These formulas are nonsingular at a=0 and a=1 and throughout the entire domain.

For v=(v0,v1,v2), let s_i(v) be its elementary symmetric polynomial of degree i and set

```
P(v,k)=[s1(v)+k s2(v)+k^2 s3(v)]/product_j(1+k v_j).
```

Then

```
D(a)=P(p,a)+delta/[d_s product_j d_j]+P(q,1-a).
```

This formula, unlike (1-1/product(1+k v_j))/k, is valid directly at k=0. With denominator d_s product(d_j) product(e_j), D has numerator degree at most 5 and denominator degree at most 7 in a. The superficially possible degree-six numerator terms from the two prism contributions cancel: their leading coefficients are respectively -p_s product(p)product(q) and +p_s product(p)product(q). The cap contributes degree at most three. Therefore the numerator of D'(a) has degree at most 11.

## 6. The actual-centroid projective pencil

Fix beta,p,q,u,p_s, and vary a on its whole admissible interval. Let V(a), g(a), Sigma(a) be actual uniform volume, centroid and covariance. Relative to any fixed parameter, the infinitesimal projectivity is Y -> Y/(1-hY_x), whose Jacobian is (1-hY_x)^(-4). Differentiation under the integral is justified on any compact subinterval where all denominators stay positive. It gives

```
V'=4V g_x,
g'=5 Sigma e_x+g g_x,
g_x'=5 Sigma_xx+g_x^2>0,
(log V)''=20 Sigma_xx+4g_x^2>0.
```

For clarity, the vector identity follows from differentiating the numerator integral: its derivative is 5 integral Y Y_x; subtracting V'/V times the centroid gives 5 E[Y Y_x]-4g g_x=5Sigma e_x+g g_x. The strict inequalities use the actual positive-definite covariance of this full-dimensional uniform body.

At each finite endpoint of the admissible interval at least one positive tetrahedral weight diverges, while none is negative. Thus V tends to positive infinity at both endpoints. More explicitly, D is a positive rational function with a pole at each endpoint, so its logarithmic derivative tends to minus infinity on the left and plus infinity on the right. Since g_x=D'/(4D) is strictly increasing, it crosses zero exactly once. Consequently:

THEOREM 2. In each such projective pencil there is a unique a_c with actual g_x(a_c)=0. It is the unique volume minimizer of the pencil. The fixed geometric triangle plane B0B1B2 contains the actual centroid only at that member. For rational fixed data, a_c is a real algebraic number of degree at most 11, specified uniquely by the admissible interval and D'(a_c)=0.

This is an application of the projective uniform-centroid variation mechanism to the COMPLETE explicit incidence chart. It does not assert that all affine realizations may be replaced by the a_c member without changing physical rests; projective refilling is precisely the variation being measured.

## 7. New exact rational controls

Both source programs use the complete literal input

```
beta=2/5,
p=(1/5,2/5,3/5), q=(1/4,1/3,1/2),
u=(1/5,2/5,2/5), p_s=4/5, delta=9/25,
a in {-1,0,1/2,1,2},
M=((7,1,2),(1,5,-1),(2,-1,6)).
```

The whole admissible a interval is (-5/4,3). The first source reconstructs every maximal facet from all vertex triples, proves strict off-face supports and cyclic turns, checks the seventeen true edges, independently compares exact oriented-boundary moments with the seven positive tetrahedra, checks SPD covariance and the rational affine inverse, and verifies all 34 oriented primal VE and all 34 oriented dual EF signs with N=M^(-1). No tested sign is zero. Its own proper (S,U,H) results are

```
a=-1:  (3,5,6)
a=0:   (6,9,13)
a=1/2: (5,9,12)
a=1:   (5,8,11)
a=2:   (4,6,8)
```

All have physical weak census 000. The source reports the exact vertex lists, volumes, centroids, covariance matrices, poles, M,N and every oriented arrow value, not just the counts. None is a proper110 example or U1 survivor. These controls establish that both regular sections and both outer a sectors are actual bodies; they do not establish a continuous equilibrium exclusion.

The inverse and affine-moment checks additionally use the exact affine map with linear rows ((2,1,0),(0,1,1),(1,0,1)) and translation (2/3,-1/5,7/4). All parameters are recovered unchanged from that image. The reported metric M applies to the original chart points; it is not silently reused to assert affine-image equilibrium invariance.

For the fixed data, the exact rational six-volume is

```
D(a)=(-24a^5+14a^4+160a^3-3950a^2-44800a-81000)
     /(24a^7-38a^6-997a^5+1060a^4+11750a^3-1250a^2-45625a-37500).
```

The second program checks all three components of the mixed centroid derivative identity symbolically in a, the logarithmic-volume identity, the degree bounds, and the unique derivative root on (-5/4,3) by exact root counting. Forty-eight exact bisections give

```
404480252920165/562949953421312 < a_c
    < 808960505840347/1125899906842624.
```

Its output includes the full rational centroid and covariance functions and the integer/rational coefficient lists for D and D'. This is a complete exact mixed-moment test, not a numerical root estimate used as proof.

## 8. Complete recovery and verification

Recover the exact text of Part 2 as `full_cut_stack_chart.py` and Part 3 as `full_cut_stack_centroid_pencil.py` in one directory. Do not copy a Markdown fence into either file. All fixed inputs, helper functions and nondefault choices are in those two files. There is no seed, downloaded checkpoint, generated input array or hidden original sandbox dependency.

Input identity:

```
full_cut_stack_chart.py
  material [internal-source-reference]
  9133 bytes
  SHA-256 249a774019a71dadb0777992cf831a4173992f429df622f13c1ea3dd15a8f107
full_cut_stack_centroid_pencil.py
  material [internal-source-reference]
  4179 bytes
  SHA-256 15a94febb513c71c46cb5d61b7459b173077a517d494fb610bd93af72a364f4f
```

The executed environment was Python 3.13.5 and SymPy 1.14.0. Part 2 requires only the Python standard library and was also run with site initialization disabled. Keep assertions enabled; the programs reject optimized execution. Reconstruct and verify with

```sh
python -B -S full_cut_stack_chart.py > full_cut_stack_chart_report.json
python -B full_cut_stack_centroid_pencil.py > full_cut_stack_centroid_pencil_report.json
sha256sum full_cut_stack_chart.py full_cut_stack_centroid_pencil.py
sha256sum full_cut_stack_chart_report.json full_cut_stack_centroid_pencil_report.json
```

Expected outputs:

```
full_cut_stack_chart_report.json
  55765 bytes
  SHA-256 5f0d4e929fe0cd70587525482621f300bef342a88a2846fb1b2c360b4ca5ebdf
  marker FULL_CUT_STACK_CHART_SEVEN_POSITIVE_TETS_EXACT_PASS
full_cut_stack_centroid_pencil_report.json
  11307 bytes
  SHA-256 be909b8835fd75ee3a9acc940072e0b07107b0effa4e391add8ff8abe2ef9063
  marker FULL_CUT_STACK_MIXED_CENTROID_PENCIL_EXACT_PASS
```

Both commands were repeated from a fresh directory containing only the two source files. Exact byte comparisons of both outputs passed, with terminal confirmation `FULL_CUT_STACK_BOTH_COLD_SOURCE_ONLY_BYTEIDENTICAL_PASS`. These execution claims refer to the coordinator's own NEW computations. They are not routine reauthentication of a worker's theorem. Output hashes identify generated bytes; the actual recovery content is the two complete source materials and their literal inputs.

## 9. Consequence for the research map

The old eight-parameter model fixed further affine shape data, including the relation between the finite ghost apices and the stack barycentrics. Its max-deficit polynomial atlas and its <=9-vertex native-wall theorem remain valid only within that narrower domain. The eleven-parameter finite opposite-ghost operation additionally allows unequal ghost distances and arbitrary stacking position, but still corresponds only to 0<a<1 in the full chart. The a=0,1 regular sections and a<0,a>1 sectors show why a finite-operation exhaustion is not an incidence exhaustion.

The useful new mechanical object is the actual moment formula with seven positive tetrahedra across this entire incidence. A next computation can select one genuine tree under one unrestricted SPD metric and use these moments without singular ghost subtraction or an assigned centroid. An all-root theorem still needs every physical root and complete true-edge escape alternative, and any joint110 claim still needs its single inverse, true stable facets and physical weak-contact census. The present capsule solves the complete geometry and the own-centroid pencil, not those mechanical obligations. No lower layer is subtracted and no new minimum is announced.
