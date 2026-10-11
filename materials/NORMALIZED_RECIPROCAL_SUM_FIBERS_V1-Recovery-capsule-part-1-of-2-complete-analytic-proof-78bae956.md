# material-78bae956b24a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# NORMALIZED_RECIPROCAL_SUM_FIBERS_V1
## Recovery capsule part 1/2: exact nonlinear reciprocity from the normalized sum

Coordinator analytical advance, with exact algebra/control execution. This is a self-contained dimension-three matrix theorem and a new necessary-domain tool for the first open mechanical layer. It is NOT an E17 exclusion, a canonical type subtraction, an actual polyhedron, or an attaining110 construction. The accepted interval remains34<=C_min<=622. The entire runnable companion is [internal-source-reference]; deliver BOTH parts for computational continuation.

The motivating exact PAIR-hull source was read completely: [internal-source-reference], SHAbdc9e45a6d95b687c51dfa89cb99db370748f61a95561be9c962f7f4007aeddd; its executable [internal-source-reference] and authoritative source-pin correction [internal-source-reference] were also read completely. Its three correct LMIs use k(k+1)/(k^2+k+1), hence90/91 for k9. There is no mathematical correction to that source. This new result goes BEYOND the convex hull by explicitly retaining nonlinear reciprocity. No historical-priority claim is made.

## 1. Definitions and exact image theorem
Work with real symmetric3x3 positive definite matrices. Write
 A>0, trA=1, B=A^(-1)/tr(A^(-1)), S=A+B.
The letter S in this material is a MATRIX SUM, not the number of stable equilibria. If necessary call the latter S_eq.

For every such pair there is eta>0 with AB=eta I and trB=1. Conversely, two positive definite trace-one matrices satisfying AB=eta I are such a normalized reciprocal pair.

THEOREM1. A real symmetric matrix S is the sum of a normalized reciprocal pair if and only if
 trS=2 and 0<S<I.
Moreover eta is determined by S alone. Put
 T=tr(S^2), Q=tr(S^4),
 eta(S)=[T-sqrt(6Q-2T^2)]/12.                     (1)
For ordered eigenvalues s1>=s2>=s3 of S define
 ri=sqrt(si^2-4eta(S)), i=1,2,3.                  (2)
All radicals are real, eta>0, and
 r1=r2+r3.                                       (3)
The complete fibre of reciprocal pairs with this fixed S is classified in section3.

Necessity: if a,b,c are the eigenvalues of A, a+b+c=1 and q=ab+ac+bc>0, then the corresponding eigenvalues of B are bc/q,ac/q,ab/q. For the first eigenvector,
 1-a-bc/q = a(b^2+bc+c^2)/q>0.
The other two identities are cyclic. Thus S<I and S>0, and trS=2. Also eta=abc/q.

## 2. Existence and uniqueness of the scalar eta
Suppose trS=2 and 0<S<I. Its positive ordered eigenvalues satisfy the STRICT triangle inequalities: the only nonautomatic one is s1<s2+s3, equivalent to s1<1.
Consider
 p(e)=48e^2-8Te+T^2-2Q.                          (4)
The exact identities are
 T^2-2Q=(-s1+s2+s3)(s1-s2+s3)(s1+s2-s3)(s1+s2+s3)>0,
 6Q-2T^2=2[(s1^2-s2^2)^2+(s1^2-s3^2)^2+(s2^2-s3^2)^2]>=0,
 p(s3^2/4)=-(s1^2-s2^2)^2<=0.                    (5)
If s1>s2, the upward quadratic therefore has exactly one root in(0,s3^2/4], its smaller root(1). If s1=s2, p(s3^2/4)=0 and p'(s3^2/4)=16(s3^2-s1^2)<=0, so this endpoint is again the smaller root, coinciding with the larger root only when all si coincide. This proves eta>0, eta<=s3^2/4, and its uniqueness in that interval.

For ri defined by(2), p(eta)=0 is precisely
 2(r1^4+r2^4+r3^4)-(r1^2+r2^2+r3^2)^2=0.          (6)
The nonnegative ordered r1>=r2>=r3 therefore form a degenerate triangle, which gives(3). This is also immediate from the Heron product factorization; no extraneous sign from squaring is retained.

In an orthonormal eigenbasis of S set
 D=diag(r1,-r2,-r3), A=(S+D)/2, B=(S-D)/2.        (7)
Equation(3) gives trD=0 and hence trA=trB=1. Each si>ri because eta>0, so A,B>0. They commute and AB=(S^2-D^2)/4=eta I. This proves existence, including every eigenvalue-degeneracy case.

For any actual pair with this S, D=A-B commutes with S, trD=0, and D^2=S^2-4eta I. Its eigenvalue magnitudes are ri. Their zero signed sum forces(3), so its eta must solve(4) in the just-proved unique interval. This proves uniqueness of eta for EVERY pair in the fibre, not merely for the constructed pair.

## 3. Complete fibres, including the exceptional circle
CaseA: s1>s2. There are EXACTLY TWO ordered pairs, interchanged by A<->B. In an S eigenbasis they are(7) and the same expression with D replaced by-D. If s2=s3, the two negative signs are identical on that entire eigenspace, so (7) is basis-independent there; there is no hidden orientation continuum. Indeed r1=r2+r3 with all ri>0 forces one sign opposite the other two. The largest magnitude has that single sign. For a double lower eigenspace, opposite signs inside it would have zero trace and could not cancel the nonzero largest entry.

CaseB: s1=s2=s>s3=t. Then eta=t^2/4, r3=0, r1=r2=r=sqrt(s^2-t^2)>0. On the top eigenspace E, every fibre point has
 D=r(2P-I_E), D|E_perp=0,                         (8)
where P ranges over rank-one orthogonal projectors on E. Conversely all these choices work. This is a circle of ordered pairs, and inversion is D->-D on that circle. It MUST NOT be collapsed to an arbitrary chosen diagonal representative when geometry fixes directions in E.

CaseC: S=(2/3)I. Its fibre is the single pair A=B=I/3.

These are all cases. Thus the sum usually determines the reciprocal pair up to inversion, but repeated LARGEST eigenvalues are an essential exception. Repeated SMALLEST eigenvalues are not that exception.

## 4. Exact adjacent-ratio test expressed solely in S
For a reciprocal pair let kappa be the LARGER of its two ordered consecutive eigenvalue ratios. Both A and B have the same kappa, with the two ratios reversed by inversion. Every pair in a fixed-S fibre has the same spectrum up to inversion, even in CaseB.

THEOREM2. Define
 kappa(S)=(s1+r1)/(s3-r3).                        (9)
Then the fixed-S fibre contains a pair with both adjacent ratios<=k if and only if kappa(S)<=k. Replace BOTH inequalities by strict ones for the strict-ratio class. In particular the actual-covariance joint S_eq=U=1 specialization requires kappa(S)<9.

Proof: for the choice(7), the ordered eigenvalues of A are
 x=(s1+r1)/2, y=(s3-r3)/2, z=(s2-r2)/2.           (10)
The smaller solution a_-(s)=(s-sqrt(s^2-4eta))/2 is decreasing in s, so x>=y>=z>0. With q=xy+xz+yz, the sum-eigenvalue difference associated to x and z satisfies
 s1-s2=(x-z)(xz-y^2)/q.                          (11)
Thus xz>=y^2, unless all three are equal in which case the conclusion holds anyway. Hence x/y>=y/z and their larger ratio is precisely(9). Inversion reverses the two ratios. The orientation circle changes neither spectrum nor this conclusion.

This is an EXACT nonlinear description of the image of the bounded-ratio reciprocal set under(A,B)->S, not its convex hull. It adds information even after the best joint-linear PAIR relaxation. It does not reduce the five continuous parameters of a directly parameterized trace-one A; rather it gives different five-dimensional coordinates with explicit finite/circle fibres instead of an independently relaxed inverse matrix.

## 5. A strict commuting hull point whose sum has NO ratio9 reciprocal lift
Take
 S0=diag(9/10,11/20,11/20), A_rel=B_rel=S0/2.
The matrices A_rel,B_rel are positive trace-one matrices, commute, and each has consecutive ratios18/11 and1, strictly less than9. They lie STRICTLY inside the exact pair hull D9:
 A_rel+B_rel<82I/91,
 9A_rel+B_rel>90I/91,
 A_rel+9B_rel>90I/91.
Nonetheless NO actual normalized reciprocal pair with this SAME sum has adjacent ratios<=9.

From(1), eta=1/30. CaseA applies, since9/10>11/20. The only two reciprocal pairs are the following pair and its inverse-swapped version:
 A=diag((27+sqrt609)/60,(33-sqrt609)/120,(33-sqrt609)/120),
 B=diag((27-sqrt609)/60,(33+sqrt609)/120,(33+sqrt609)/120).
Their largest adjacent ratio is
 K=(25+sqrt609)/4>9,
 and 2K^2-25K+2=0.
These are spectral/formal controls, NOT an actual polyhedron or a geometrically compatible rooted-tree packet. The conclusion is stronger than showing A_rel B_rel is not scalar: it excludes EVERY bounded-ratio reciprocal pair over their sum. Adding commutation alone to the pair hull cannot eliminate this point.

More generally, on the lower-double-eigenvalue stratum S=diag(u,1-u/2,1-u/2),2/3<=u<1, a fibre has spectrum proportional to(K,1,1),K>=1, or its reciprocal. Here
 u=K/(K+2)+1/(2K+1).
The right side is strictly increasing for K>1, because its derivative is2/(K+2)^2-2/(2K+1)^2>0. Therefore the exact ratio-k condition on this stratum is
 u<=k/(k+2)+1/(2k+1).                            (12)
For k9 the threshold is182/209, strictly below9/10. The linear SUM cap is(k^2+1)/(k^2+k+1), and its gap from(12) is
 k(k-1)^2/[(k+2)(2k+1)(k^2+k+1)]>0.
This supplies a full symbolic family of nonlinear gaps, not an isolated floating-point sample.

## 6. Fixed-S true-arrow systems: two checks or a circle problem
For a fixed actual geometry and preconditioner C, whitened true negative-arrow matrices are
 H_ij=C^(-1/2)[-sym(X_i(X_j-X_i)^T)]C^(-1/2),
 G_fg=C^(1/2)[-sym(q_f(q_g-q_f)^T)]C^(1/2),
where q_f are true same-origin poles, not independently recentered polar vertices. The selected weak arrows require
 tr(AH_ij)<=0 and tr(BG_fg)<=0.                   (13)
Normalization only divides the original contractions by their respective positive traces.

When s1>s2, write D_+ as in(7). For each epsilon in{+1,-1}, test ALL rows
 tr(SH)+epsilon tr(D_+H)<=0,
 tr(SG)-epsilon tr(D_+G)<=0.                      (14)
One common epsilon must work for the entire primal AND polar packet. This gives an exact two-branch test at fixed S; allowing an independent sign for each row is wrong.

For s1=s2>s3, fix any orthonormal basis of E and write
 D|E=r[[z1,z2],[z2,-z1]], z1^2+z2^2=1.
All rows(13) become affine halfplane constraints in(z1,z2). Hence exact weak feasibility is intersection of a circle with finitely many halfplanes. A finite candidate rule is: test(1,0), and all intersections of the unit circle with each NONCONSTANT boundary line. If the feasible portion is nonempty and not the whole circle, one of its endpoints lies on such a boundary; tangent singleton cases are included. Constant inconsistent constraints reject immediately. A line a.z=c with a!=0 intersects if c^2<=||a||^2, with points c*a/||a||^2 plus/minus sqrt(||a||^2-c^2)*a_perp/||a||^2. Thus at most2m+1 candidates suffice for m weak rows. Algebraic coefficients require exact sign evaluation, not an unqualified floating tolerance.

The scalar fibre has only A=B=I/3 to test. An actual proper110 census still additionally needs the genuine strict-root and physical-contact tests. Primitive zeros must not all be interpreted as weak equilibria. Formula(14) is a necessary/exact SELECTED WEAK-ARROW test, not a replacement for the full physical census. Strict rows on the exceptional circle require open-arc handling rather than blindly testing only boundary points.

For an individual joint functional, the generic conditional minimum is
 (tr(S(H+G))-|tr(D_+(H-G))|)/2.
On the exceptional circle it is
 tr(S(H+G))/2-r[lambda_max((H-G)|E)-lambda_min((H-G)|E)]/2.
These are fixed-S statements. Unconditional linear optimization over ALL pairs is already exactly solved by the preceding pair-hull SDP; no new global affine separator is claimed here.

## 7. Reproduction, evidence level and next use
Companion [internal-source-reference] is the COMPLETE literal Python source, with no omitted helpers, inputs, archives or seeds. Save its raw text as reciprocal_sum_fiber.py, UTF8/LF with final newline.
Dependencies: Python>=3.11, SymPy1.14.0; author executed CPython3.13.5, assertions enabled. Run
 python -B reciprocal_sum_fiber.py build
 python -B reciprocal_sum_fiber.py check
Both observed executions printed
 RECIPROCAL_SUM_FIBERS_EXACT_PASS 977 c5a61c731a9fa3a3cc10cbd8fb585081a086ba54f76bd742666e7350f8845470
Pins:
 reciprocal_sum_fiber.py5674bytes SHAaba5be49ea2a76f781ffcddee02127dc24be4570645e14aad47a1277109e9948;
 reciprocal_sum_fiber.json977bytes SHAc5a61c731a9fa3a3cc10cbd8fb585081a086ba54f76bd742666e7350f8845470.
The executable checks six entire symbolic identities,216 rational spectral controls, two distinct rotated members of the repeated-top fibre, and the exact radical countercontrol. The continuum image/fibre/ratio/arrow theorems rest on the complete analytic proof above, not on those216 tests. No independent second-authored replay or proof-assistant formalization is claimed.

Use this nonlinear domain only while keeping actual moving COM/covariance and one reciprocal pair. A useful next step is a genuine open E17 complementary packet/cell surviving the pair-hull relaxation but failing both nonlinear fibres, or a controlled analysis of the exceptional eigenplane. A formal spectral gap alone does not close any shape, rooted orbit or type. The upper construction search remains separate, and the exact minimum remains unresolved.
