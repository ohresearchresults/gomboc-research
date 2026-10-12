# minimum-0116

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# B8_THREE_FULL_PROJECTIVE_PENCILS_ALL_SPD_V1

## Result and source authority

The main result is stronger than a conditional S1/U1 bridge: **every uniform, own-centroid body in each of the three explicitly defined full positive projective pencils below has at least two strict unstable equilibria for every positive-definite three-dimensional metric.** The projective parameter ranges over its entire admissible interval, `-5/6 < alpha < 5/4`; the metric is unrestricted SPD3, including arbitrarily anisotropic horizontal geometry and arbitrary horizontal/vertical coupling.

There is also a genuine boundary countercontrol for the corrected parent method. Throughout `3/4 <= alpha <= 1`, in all three pencils, the base-parallel central section has only vertex 8 in its upper open half. Its unique stress has E=0, and its stress-center basal foot lies strictly outside the true octagon. Consequently **neither H nor L of the parent can hold for this half, for any horizontal G**, regardless of support optimization or exterior-edge choice. Nevertheless the new all-metric theorem proves U>=2. Actual rational anisotropic examples at alpha=1 are recovered below, with three coherent central sections of the same refilled body and the same M,N.

A separate new algebraic result shows that **support at most three is sufficient for the entire parent H-or-L condition**, not only for maximizing E. This uses height-squared reweighting, not the old E-only Helly argument. It cannot repair the singleton/bad-foot countercontrols, which identify a geometric limitation rather than a lack of stress support.

Source authority is the corrected literal parent `minimum-0113`, declared SHA-256 `56095b5a69677862f21172ac88fa384dc8ddde057e9060de4086e4f94bb08b19`. The supplied pack was `research-journal(20260919-152416).md`, 323931 bytes, SHA-256 `c7a7c2950bf4ea4394011315d593333ac47392208a97cfd65deb007e8ee377e1`, through line 1729, including its complete recovery bundle. The parent explicitly restricts its new lens family to a fixed horizontal metric and retains whole-E17/global questions as open. The withdrawn alpha=1/2 and previous control claims are not used. The parent's actual alpha=1/2 apex heights are positive; the below-COM examples in this handoff use alpha=1 and have independently recomputed uniform centroids.

This handoff changes no registry counters. The accepted global interval remains `34 <= C_min <= 622`.

## 1. Full geometric domain and true incidence

For m=1,2,3, let the following be cyclic lists of integer or rational pairs. A listed pair (x,y) means the actual basal vertex `(x/100,y/10,0)`.

```text
m=1:
(-10,-10), (-7,10), (7,10), (14,6),
(16,1), (14,-5), (8,-9), (3,-10)

m=2:
(-10,-10), (-14,1), (-6,10), (7,10),
(14,13/2), (16,-1), (13,-7), (4,-10)

m=3:
(-10,-10), (-14,-4), (-12,5), (-6,10),
(7,10), (14,6), (16,-3), (5,-10)
```

Number these vertices 0 through 7, and set

```text
P8=(-4/5,0,1),  P9=(6/5,0,1).
T_alpha(x,y,z)=(x,y,z)/(1+alpha*x).
P_m(alpha)=conv{T_alpha(Pi):0<=i<=9}.
```

The theorem covers every `A P_m(alpha)+t`, where A is any invertible real 3x3 matrix, t is any translation, and `-5/6<alpha<5/4`. Fill the projective image uniformly before taking its centroid. Subsequent affine transformation preserves uniformity up to a constant density multiplier.

This is the entire positive-denominator interval: the extreme raw x-coordinates are -4/5 and 6/5, at the two apices. Neither endpoint is an actual body in the theorem.

The complete maximal-facet list, in the numbering used for the equilibrium audits, is generated in this order:

```text
(0,1,2,3,4,5,6,7);
(i,8,i+1) for 0<=i<m;
(m,8,9,m+1);
(i,9,i+1) for m+1<=i<=6;
(7,9,8,0).
```

The complete true-edge set is the basal 8-cycle, `(i,8)` for `0<=i<=m`, `(i,9)` for `m+1<=i<=7`, and `(8,9)`. Thus every interior parameter has true `(V,E,F)=(10,17,9)`, with six triangular facets, two quadrilateral facets and one octagonal facet. Basal degrees are all 3; apex degrees are respectively `(3,7)`, `(4,6)` and `(5,5)`.

The checker independently enumerates supporting triples, merges coplanar triangles into maximal facets, checks strict turns and strict off-facet supports, and reconstructs the true edges. Positivity of all projective denominators then preserves this entire face lattice continuously. Triangulation diagonals used for mass integration are never counted as mechanical edges.

### Theorem

For every body in this domain, relative to its own uniform centroid,

`U_nd >= 2`.

No weak-free hypothesis is required. In particular, strict S1/U1 is impossible, including on metrics that have additional physical weak contacts elsewhere.

The bound is attained within each pencil: at alpha=1, the single integer metric

```text
M0 = [[36,34,58], [34,77,121], [58,121,261]]
   = A0^T A0,
A0 = [[4,8,16], [-4,-2,2], [2,-3,1]]
```

has strict counts `(S,U,H)=(3,2,3)` and no physical weak contacts for all three m. This establishes sharpness for each pencil as a family, not a claim about this particular M0 at every alpha.

## 2. Uniform refilling and the common metric

Write `fi(alpha)=1+alpha*Pi_x`. Triangulate the true facets not containing vertex 9 and cone them to vertex 9. Each selected tetrahedron sigma has strictly positive raw six-volume `d_sigma`. Its actual projective-image volume is

`d_sigma / (6 product_{i in sigma} fi)`.

Consequently the actual uniform centroid is

```text
g(alpha) =
 [sum_sigma (d_sigma/product fi) sum_{i in sigma} Pi/fi]
 /[4 sum_sigma d_sigma/product fi].
```

This integrates the newly filled image tetrahedra. It is not a projective transport of the old centroid and is not a reassignment of vertex masses.

The recovery computes cleared centroid polynomials `g=N/D`. An independent oriented-boundary moment construction produces another rational expression, and the verifier proves equality by exact polynomial cross-multiplication for all alpha, in all three families. The actual controls are additionally checked with both vertex-8 and vertex-9 fans. The stored audit fans are nonnegative fans including zero-volume incident-facet pieces; their selected nonincident pieces are strictly positive.

For centered coordinates Xi, physical affine realization gives `M=A^T A` and `N=M^-1`. Pole vectors are recomputed from the actual maximal facets and the actual centroid, so that `qf dot Xi <= 1`. All strict primal, dual and weak tests use these same X,q,M,N.

To compactify the two parameter ends for the polynomial proof, use

```text
Ls(alpha)=I+alpha*Ps*e_x^T,
s=9 on [-5/6,0],  s=8 on [0,5/4].
```

Inside the physical interval, `det Ls=fs>0`, and `Ls T_alpha(Ps)=Ps`. The normalized centroid is `Ls g(alpha)`. An original metric M becomes

```text
M_normalized = Ls^(-T) M Ls^(-1),
N_normalized = Ls N Ls^T.
```

This is a bijection of SPD3; it does not introduce an independent horizontal metric or independent section variables. The two normalizations agree at alpha=0. Cleared polynomial expressions extend to the certificate endpoints, but no claim is made that those auxiliary limiting vertex arrays retain true 10/17/9 incidence.

## 3. Exact all-metric proof

For a true directed edge i->j define

`Dij = Xi^T M (Xj-Xi)`.

A vertex is strict U precisely when all its true incident escape values are negative. If a vertex is not strict U, it has a true neighbor with Dij>=0. Along such an escape,

`||Xj||_M^2-||Xi||_M^2 = 2 Dij + ||Xj-Xi||_M^2 > 0`.

Therefore, if U=1, choosing one nonnegative escape at every other vertex yields a directed spanning tree toward the unique U. This includes zero escape values. A global maximum of the norm is always a strict U, so ruling out U=1 gives U>=2 rather than merely U!=1.

In each normalization, the recovery constructs polynomial vectors wi and eij positively proportional, throughout the open physical interval, to the centered vertex and its actual true-edge direction. It cancels only factors fi known to be positive there and positive rational constants. Set

`Cij(alpha)=-(wi eij^T + eij wi^T)`.

A weak escape Dij>=0 implies `tr(M_normalized Cij)<=0`. Each certificate row lists actual directed-edge IDs and positive integer multipliers lambda. It forms

`K(alpha)=sum lambda_ij Cij(alpha)`.

Every coefficient matrix of K in the Bernstein basis on the row's closed parameter cell is positive definite. This is checked by its three exact Sylvester leading minors, with rational arithmetic. Bernstein coefficients are nonnegative and sum to one; hence K(alpha) is positive definite at every parameter in the cell. But any metric satisfying all escapes in the row would give `tr(M_normalized K)<=0`, contradicting positivity of both matrices.

Finally, the checker enumerates every undirected spanning tree and every root, and verifies that every resulting weak-escape tree contains the support of at least one certified row. Thus U=1 is excluded for every SPD metric, every root location and every physical interior parameter.

The complete certificate statistics are:

| m | normalization s | closed certificate cell | degree | rows | terms | rooted trees covered |
|---|---:|---|---:|---:|---:|---:|
| 1 | 9 | [-5/6,0] | 13 | 254 | 836 | 38850 |
| 1 | 8 | [0,5/4] | 13 | 294 | 1016 | 38850 |
| 2 | 9 | [-5/6,0] | 15 | 258 | 888 | 40530 |
| 2 | 8 | [0,5/4] | 15 | 289 | 990 | 40530 |
| 3 | 9 | [-5/6,0] | 15 | 285 | 924 | 40950 |
| 3 | 8 | [0,5/4] | 15 | 312 | 1069 | 40950 |

Totals are **1692 rows, 5723 positive multiplier terms, 25976 positive-definite coefficient matrices and 77928 positive leading minors**. Independent exact Kirchhoff determinants give 3885, 4053 and 4095 spanning trees, agreeing with enumeration. These are local proof-space counts, not registry counters.

The numerical locator only proposed integer rows. Acceptance, polynomial identities, positivity, incidence and complete tree coverage are exact. No failed optimizer or finite parameter sample is used as an exclusion proof.

## 4. Continuous countercontrol to the entire base-parallel parent lens

For the actual base-parallel central section, use centered Xi=(ui,zi), horizontal G>0 and

```text
M(G,v,y)=[[G,Gv],[v^T G,v^T G v+y]], y>0.
```

Let R^2 be the maximum G-norm squared of the actual section vertices. For a stress lambda on an open half,

```text
S=sum lambda_i zi^2,
b=sum lambda_i zi ui,
v_lambda=-b/S,
E=sum lambda_i ||ui||_G^2-||b||_G^2/S,
d=(R^2-E)/S.
```

The parent H condition is E>=R^2. Its L condition, when d>0, requires the stress-center basal foot `beta_lambda=g_xy+gamma*v_lambda` to lie in the relative interior of the actual octagon. It additionally requires an actual edge with both endpoints outside B and a point r=(ur,zr) on it such that

`||ur+zr*v_lambda||_G + (gamma+|zr|)*sqrt(d) <= dist_G(beta_lambda,partial B)`.

Now take any of the three families and `3/4<=alpha<=1`. Vertex 8 is the sole vertex above the actual centroid. Every basal vertex and vertex 9 is below it. Thus the upper-half stress is forced to be lambda8=1. For every G it has E=0<R^2, while its foot satisfies

`beta_lambda,x > max_{b in B} b_x = 4/(25+4 alpha)`.

So H fails and the essential interior-foot hypothesis of L fails, for every G and every exterior-edge witness.

This is proved continuously, not from the alpha=1 controls. With the exact standard-coordinate centroid g=N/D, the checker proves positive Bernstein coefficients on [3/4,1] for all four polynomials

```text
D;
D-(1-4 alpha/5) Nz;
(1+6 alpha/5) Nz-D;
(1+4 alpha/25) Nx+(24/25) Nz-(4/25) D.
```

The middle two give the actual apex height signs. The final polynomial gives the strict separating inequality for beta_x after multiplication by positive denominators.

For a compact literal height check, at m=3, alpha=1,

```text
g_z = 442171831/335627688,
X8_z = 1235966609/335627688 > 0,
X9_z = -289613791/335627688 < 0,
beta_x = 8174341946371541783/37111539347650926396 > 4/29.
```

These are new own-centroid below-COM examples at alpha=1. They do not revive the withdrawn alpha=1/2 claim.

### Actual anisotropic bodies and coherent central sections

For each m at alpha=1, compute the actual g and X, and set

```text
v=-X8_xy/X8_z,
G=[[9,3],[3,5/4]],
y=1/10000,
A=[[3,1,3*v0+v1],[0,1/2,v1/2],[0,0,1/100]].
```

Then A^T A is exactly M(G,v,y). The horizontal eigenvalue ratio is `(41+sqrt(1537))/(41-sqrt(1537))>40`. The uniform physical body is `conv{A Xi}` and its centroid is exactly zero.

The audited central planes, in the same centered coordinates, are

```text
z=0;
x+v0*z=0;
3*x+y+(3*v0+v1)*z=0.
```

All section vertices are constructed from the actual true edges, including the actual vertex 8 when it lies in a section. In the first plane, the sole upper vertex has norm strictly below the section radius; the parent all-height stress bridge is unavailable as proved above. In each of the other two planes, both open halves have strict positive half-max gaps, and the witnesses are actual strict U vertices 0 and 9.

For each plane, the report gives a full basis C with coordinates X=C X_section, and verifies

```text
M_section=C^T M C,
N_section=C^(-1) N C^(-T),
q_section=C^T q,
M_section N_section=I.
```

Primal and dual Gram values are checked to agree with those of the original body. There is no independent choice of a metric for either section.

The complete strict-count summary is:

| m | anisotropic singleton/bad-foot control | common integer M0 control |
|---|---|---|
| 1 | (S,U,H)=(4,4,6) | (3,2,3) |
| 2 | (3,3,4) | (3,2,3) |
| 3 | (3,3,4) | (3,2,3) |

All six controls have all 68 true-edge primal/dual primitives nonzero and no physical weak contacts. The recovery preserves their exact vertices, poles, volumes, centroids, maximal facets, true edges, strict labels, saddle edges and all section points. The nonwinning controls are retained because their bad-foot geometry, below-COM apex and coherent sections are the material boundary evidence.

### Strict and physical-weak semantics

For a true edge ij adjacent to maximal facets f,h, the four primitives are `(Dij,Dji,Dfh,Dhf)`, where `Dfh=qf^T N(qh-qf)`. Strict H requires all four to be negative. Physical weak contact requires all four to be nonpositive with at least one zero; a zero accompanied by a positive primitive is harmless. The checker reconstructs the edge parameter and nonnegative two-pole coefficients, classifies VF/VE/EF and deduplicates physical points when such a packet occurs. The present controls have none. The all-metric theorem itself allows such packets, because its contradiction starts from nonnegative primal escapes and therefore includes their boundary equalities.

## 5. New sparse theorem for the full H-or-L condition

Fix one actual open half, its nonzero zi, the actual G and R^2, and any stress lambda. Define

```text
theta_i=lambda_i zi^2/S,
a_i=ui/zi,
c_i=(R^2-||ui||_G^2)/zi^2,
q=sum theta_i a_i=-v_lambda.
```

Then `sum theta_i=1`, and direct substitution gives the exact identity

`d=(R^2-E)/S=||q||_G^2+sum theta_i c_i`.

At fixed q, minimize `sum theta_i c_i` subject to

```text
theta_i>=0,
sum theta_i=1,
sum theta_i a_i=q.
```

This is a nonempty compact linear program with at most three independent equality constraints. An extreme optimum theta' has support at most three. Recover the actual stress by

`lambda'_i=(theta'_i/zi^2)/(sum_j theta'_j/zj^2)`.

It has exactly the same v_lambda, hence the same basal foot and the same `ur+zr*v_lambda` for every fixed actual edge witness r, while d'<=d. If d'<=0, H holds. If d'>0 and the old L held, L remains true because only its nonnegative sqrt(d) term decreased. The same argument preserves an H witness that already had d<=0.

**Conclusion:** any successful full parent H-or-L witness can be replaced by one supported on at most three actual vertices, with the same stress center and the same exterior-edge point. No equal-height assumption is needed. The stress coefficients remain dual multipliers, not physical masses.

Equivalently, form the lifted points `(a_i,c_i)` in R^3. Their lower convex envelope kappa(q) gives the optimal normalized deficit `||q||_G^2+kappa(q)` at center -q. This provides a complete finite enumeration of support types, but weights and edge witnesses may still vary continuously. It is not justified to maximize E alone and assume the resulting center optimizes L.

The preceding singleton countercontrols show exactly why this new sparsity result does not make the one-plane lens complete: there is only one available upper support already, and its foot is outside the true base.

## 6. Verification status, frontier and continuation

The successful direction was an exact all-metric escape-certificate proof for the three asymmetric, genuinely refilled projective pencils, rather than another symmetric-a interval or another independent numerical S/U test. Endpoint affine normalization was essential: it made the entire admissible projective intervals accessible to finite Bernstein certificates without bounding the metric condition number.

All six locator cell outputs were replayed byte-identically. The final 1692-row pruned certificate was accepted by exact rational verification. A cold directory containing only the literal recovery wrapper reconstructed the sources and certificate, ran build and check, and produced identical logs and the pinned exact report. The optional floating locator is included for provenance/reproduction; build and check do not depend on running it or on accepting a floating eigenvalue as proof.

The remaining complement is substantial: arbitrary octagonal bases outside these three specified projective/affine orbits; other projective denominator directions; and the full shape families of the three incidence types. The graph labels alone do not transfer these geometry-dependent certificate rows to arbitrary realizations. Whole B8/two-apex, whole E17, and the global problem remain open.

The most useful continuation is to combine the new three-support full-lens reduction with genuinely different central planes of one body and one M,N, or to enlarge the exact polynomial certificate to additional shape parameters. In the singleton/bad-foot sectors, adding more stresses in the same half cannot help. The actual alternate-section controls give concrete starting points for a root-consistent multiple-plane argument; they are not claimed to provide such an argument for every metric.

No incidence-registry entries are removed or relabeled here. The local tree-coverage totals are not a registry delta. The accepted global bounds remain 34 and 622.

## 7. Complete durable recovery capsule

The following single source reconstructs all continuation-critical data. Its embedded bundle contains the complete exact geometry kernel, polynomial generator and optional locator, proof checker, deterministic locator/pruner, and the complete literal 1692-row certificate. No parent file, sandbox file, archive item or network source is required by the reconstruction.

Tested environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, assertions enabled; BLAS/OMP/MKL threads are fixed to one. The numerical locator is optional. The proof checker uses Fraction/integer arithmetic for incidence, moments, polynomial coefficients, Sylvester minors, metric inverses, physical weak packets and complete coverage.

Save the Python block as `recover_b8.py` and run:

```sh
python recover_b8.py sources
python recover_b8.py build
python recover_b8.py check
# Optional numerical discovery replay, followed by exact acceptance/pruning:
python recover_b8.py locate
```

Expected principal markers:

```text
THREE_TRUE_B8_FULL_POSITIVE_PROJECTIVE_PENCILS_ALL_SPD_U_GE_2_PASS
EXACT_OWN_COM_FAN_BOUNDARY_POLYNOMIAL_IDENTITIES_PASS
CELLS_ROWS_TERMS_PD_MINORS 6 1692 5723 25976 77928
SINGLETON_UPPER_BAD_FOOT_ENTIRE_INTERVAL_3_4_TO_1_ALL_G_PASS
ACTUAL_CONTROLS_COUNTS [[4,4,6],[3,2,3],[3,3,4],[3,2,3],[3,3,4],[3,2,3]]
ONE_M_INVERSE_AND_THREE_COHERENT_ACTUAL_SECTIONS_PASS
B8_FULL_PENCILS_DURABLE_RECOVERY_PASS
B8_FULL_PROJECTIVE_PENCILS_SELF_CONTAINED_CAPSULE_PASS
```

Whitespace in the printed count list is immaterial; the generated bytes are pinned:

| object | bytes | SHA-256 |
|---|---:|---|
| certificate.json | 44879 | afc0744aafac406f9f7ee07002730ea6044ade46e5228b2ac5f6c56c78b30302 |
| verified.json | 119519 | 505d676c62017785d8cbf0e9a553308d7b849f9c8bb387c9c94bdd178fadcef2 |
| decoded source/certificate bundle | 69467 | d0a2b9f5f6c842cde8cb29844ffd226ffc033c10a34ae8e6c5948c21d9614640 |
| recover_b8.py as printed | 28681 | 4b5830dfa742153d4ec4e84e1cee169b2a4cc4e2b758488c9b02c2949fa260b6 |

Individual source byte counts and hashes are embedded in SOURCE_PINS and checked before execution. Supplemental copies: recovery wrapper (`recover_b8.py`), exact verified report (`verified.json`), and literal coefficient certificate (`certificate.json`). These links are not needed by the literal capsule.


[Encoded source block omitted; the code in this passage is incomplete.]
