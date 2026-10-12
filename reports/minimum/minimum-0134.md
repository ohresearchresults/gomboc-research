# minimum-0134

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# BEVEL_INTERIOR_CONTINUATION_PARTIAL_COFACTOR_BRIDGE_V1

## Outcome and verification boundary

**This continuation does not establish a new excluded interior region and does not produce an actual S=U=1 body.** The requested interior determination remains open. The last accepted actual-body result remains BEVEL_JOINT_QUANTIFIED_HORIZON_V1, parent minimum-0127, SHA-256 7070b3528882b3586838f64485c50da178985ebc36eae815e7536b276ebd1ddd.

The additional mathematical contribution below is a directly proved **reciprocal-cofactor obstruction** for combining primal and polar weak-arrow inequalities under the same metric. It can detect incompatibility even when the two scalar inequalities are individually feasible. It is a potential economical certificate mechanism for the interior problem, not a completed certificate for any remaining bevel root/shape domain.

No new SAT, CAD, interval-cover, optimization or coefficient-certificate computation was completed. No numerical nonfeasibility claim, new tree count, physical counterconstruction or new recovery checkpoint is asserted. The interrupted attempt is not evidence of mathematical infeasibility.

## Input reading and retained authority

The complete latest research-journal(20260920-150804).md, including its literal parent and the complete embedded joint_bevel.py, was read through EOF. Its exact mounted identity is 298513 bytes, 1828 lines, SHA-256 45b0ea4973fa03be72f0ac2d41dcf86d006e96bb3af83434a0601d0d80537c92. The initially truncated line 569 was separately retrieved in full. Earlier unchanged evidence remains supplied in this conversation; it was not represented as newly executed work.

The mounted standalone joint_bevel.py was confirmed to be 16510 bytes, SHA-256 b41d54ce690bf3b1d81a53aa24817b2514f6098a23c4635ffef59841cd978434, matching the accepted parent. This was a source-identity check, not a rebuild or solver run. No mathematical conflict with the required literal parent was found.

The accepted parent closes the full projective horizon quantitatively and supplies the nine-variable exact common-metric model. It expressly leaves interior feasibility undecided. Its original exact expansion and control checks are inherited evidence, not new results of this continuation.

## 1. A reciprocal-cofactor obstruction

Write sym(x,y)=(xy^T+yx^T)/2. For a symmetric 3 by 3 matrix A, write adj(A) for its cofactor adjugate.

### Lemma

Let A and B be real symmetric 3 by 3 matrices. Suppose:

1. A has inertia (one positive, two negative eigenvalues).
2. For some c>0, B is at most c adj(A) in the positive-semidefinite order.

Then there is **no** positive-definite M satisfying both

```
tr(A M) >= 0,
tr(B M^(-1)) >= 0.
```

All inequalities on the proposed arrow side may be weak. The matrix comparison may also be non-strict; equality B=c adj(A) is sufficient.

### Proof

Suppose tr(A M)>=0 and put C=M^(1/2) A M^(1/2). Congruence preserves inertia, so the eigenvalues of C have the form a,-b,-d with a,b,d>0. Its nonnegative trace gives a>=b+d. Consequently

```
tr(adj(C)) = bd-a(b+d)
           <= bd-(b+d)^2
           = -(b^2+bd+d^2) < 0.
```

The adjugate congruence identity gives

```
adj(C) = det(M) M^(-1/2) adj(A) M^(-1/2),
tr(adj(A) M^(-1)) = tr(adj(C))/det(M) < 0.
```

Since M^(-1) is positive definite, B<=c adj(A) implies

```
tr(B M^(-1)) <= c tr(adj(A) M^(-1)) < 0,
```

contradicting the second inequality. This proves the lemma, including every equality case in either assumed weak trace inequality.

A convenient sufficient exact test for the required inertia is det(A)>0 together with one displayed vector u having u^T A u<0. A nonsingular symmetric matrix with positive determinant has either zero or two negative eigenvalues; the negative direction rules out the former. This avoids numerical eigenvalue tolerances.

### Literal algebraic control

Take

```
A = B = diag(1,-1,-1),
c = 1.
```

Here adj(A)=A. The first scalar inequality alone is feasible with M=diag(3,1,1), giving tr(A M)=1. The second alone is feasible with M=diag(1,3,3), giving tr(B M^(-1))=1/3. The lemma proves they cannot hold for the same M.

This is a complete literal matrix control of reciprocal incompatibility. **It is not a polyhedron, a selected bevel tree or a physical equilibrium construction.** Its role is to distinguish the joint obstruction from separately finding feasible primal and polar metrics.

## 2. Application to the actual bevel, with no change of centroid convention

For a positive projective parameter p, let

```
Y_i = X_i/(1+p·X_i),
g = the actual uniform volume centroid of conv(Y_i),
Z_i = Y_i-g.
```

Let q_f be the actual facet poles of this same own-centered body. Define the true-edge matrices

```
F_ij(p) = sym(Z_i,Z_j-Z_i),
E_fk(p) = sym(q_f,q_k-q_f).
```

Then the actual primal and polar primitives are exactly

```
D_ij = tr(M F_ij),
D*_fk = tr(M^(-1) E_fk).
```

Choose any finite sets of true primal and true polar arrows, with nonnegative weights alpha_ij and beta_fk, and form

```
A(p) = sum alpha_ij F_ij(p),
B(p) = sum beta_fk E_fk(p).
```

If all these chosen arrows are available weak escapes, the two trace inequalities in the lemma hold. Therefore the following is a sufficient **joint arrow-pattern exclusion** on an actual parameter domain Omega:

```
A(p) has inertia (+,--),
B(p) <= c(p) adj(A(p)),  c(p)>0,
for every p in Omega.
```

It follows that, for every p in Omega and every SPD M, at least one chosen primal or polar escape inequality is false. The contradiction uses the same reciprocal pair throughout. It does not assume complementary trees, H=0, weak000, a bound on metric conditioning, or a particular unstable/stable root.

This is not yet an exclusion of S=U=1: a complete domain proof would need to show that every possible joint weak-arrow system contains a certified pattern. Alternatively, the selected patterns could be integrated into the parent's root/neighbor Boolean model. **No such complete cover was produced here.**

### Exact continuous certification conditions

For fixed rational weights and a fixed rational negative-direction vector u, a cell certificate could verify

```
det A(p)>0,
u^T A(p)u<0,
c(p)>0,
all seven nonempty principal minors of c(p)adj(A(p))-B(p) >= 0.
```

These conditions are sufficient throughout a whole real parameter cell. Rational denominators may be cleared only after their signs are established. The semidefinite comparison need not be strengthened to positive definiteness: the strict contradiction is supplied by the inertia-and-trace argument itself. This may matter on weak walls where a strictly positive-definite certificate cannot persist.

These are proposed acceptance conditions, not results of an interval or Bernstein run. No cell size, root coverage or successful numerical locator is being inferred from them.

## 3. Affine covariance of the obstruction

Under one invertible affine coordinate change, after translating the actual centroid to zero, write Z'_i=L Z_i. The actual poles and metric pair must transform as

```
q'_f=L^(-T)q_f,
M'=L^(-T) M L^(-1),
N'=L N L^T=(M')^(-1).
```

The certificate matrices transform as

```
A'=L A L^T,
B'=L^(-T) B L^(-1),
adj(A')=det(L)^2 L^(-T)adj(A)L^(-1).
```

Thus B<=c adj(A) becomes

```
B' <= [c/det(L)^2] adj(A').
```

The inertia condition and both physical traces are unchanged. Consequently this certificate mechanism is compatible with the accepted actual-body normalization charts, provided the same L transports all quantities. No singular limit is used in this argument.

## 4. Self-contained exact data for continuing this method

The following is the complete literal geometry needed to reconstruct the rational matrix fields above. Put X_i=U_i/4, with labels in this order:

```
U0=(-4,-4,-3)   U1=(-4,-4,4)   U2=(-4,-3,-4)
U3=(-4,4,-4)    U4=(-4,4,4)    U5=(4,-4,-3)
U6=(4,-4,4)     U7=(4,-3,-4)   U8=(4,4,-4)
U9=(4,8,12).
```

The nine outward maximal facet cycles are

```
(0,1,4,3,2), (1,9,4), (3,4,9), (0,5,6,1), (1,6,9),
(2,3,8,7), (3,9,8), (5,7,8,9,6), (0,2,7,5).
```

Their supporting pairs a_f·X<=b_f, in the same order, are

```
(-1,0,0):1
(-2,0,2):4
(-1,2,0):3
(0,-1,0):1
(0,-2,3):5
(0,0,-1):1
(0,4,-1):5
(1,0,0):1
(0,-4,-4):7.
```

True edges are consecutive unordered pairs in these maximal cycles, with duplicates removed. Two facets are true polar neighbors precisely when they share one of those true edges. The literal parent's dataset uses exactly these conventions.

For any p in D, put h_i=4+U_i·p and Y_i=U_i/h_i. Triangulate each displayed facet cycle (v0,...,vk) into (v0,vj,vj+1), j=1,...,k-1, and denote the resulting sixteen triangles by T. The origin is interior, their oriented determinants are positive, and exact actual mass is

```
d_t = det(Y_a,Y_b,Y_c) for t=(a,b,c),
D6  = sum_t d_t,
V   = D6/6,
g   = [sum_(t=(a,b,c)) d_t (Y_a+Y_b+Y_c)]/(4D6).
```

For each facet set

```
n_f=a_f+b_f p,
support_f=b_f-n_f·g,
q_f=n_f/support_f.
```

Every support_f is positive because g is the actual interior volume centroid. These formulas give the required F_ij and E_fk directly, without rebuilding the parent's expanded 750976-monomial library or using a transported centroid. They are also a complete reconstruction recipe for the proposed matrix certificate fields at rational p. No new code-produced finding or coefficient array needs recovery in this continuation.

## 5. Established domain and remaining complement

The accepted horizon result remains

```
K=184025088000000000,
eta=2^(-K-2),
J(B) subset (1-eta)D.
```

The existing C9 cone and the whole pencil p=(0,h,0), -1/2<h<1, remain excluded by their inherited all-SPD U2 theorems. They have not been enlarged here. The parent's explicit remaining shape region is therefore still contained in

```
[(1-eta) closure(D)] minus
[C9 union {(0,h,0):-1/2<h<1}].
```

For completeness, with d_f=-a_f/b_f from the literal supports above,

```
F9=conv(d1,d2,d6,d7,d4),
c9=(-1/30,-16/75,-9/50),
C9=conv(0,c9+(3/4)(F9-c9)) intersect D.
```

This is the inherited domain boundary, not a newly computed complement or an exhaustive overlap classification with every affine-family theorem.

The most useful next step for the new lemma is to seek actual small-support primal/polar weight pairs on a nontrivial remaining interior cell, verify their inertia and cofactor comparisons exactly, and then establish complete Boolean or root-pattern coverage of that cell. Until those steps are executed, the lemma is a reusable joint-compatibility tool only.

**Final scientific status:** no new interior actual-body exclusion, no physical110 point, no full-orbit conclusion, no E17 registry change and no improvement of 34<=C_min<=622. The accepted quantified-horizon parent remains the last reconstructible actual-body checkpoint; the complete proof and literal matrix control above preserve the additional analytic method without upgrading it into an uncomputed certificate.
