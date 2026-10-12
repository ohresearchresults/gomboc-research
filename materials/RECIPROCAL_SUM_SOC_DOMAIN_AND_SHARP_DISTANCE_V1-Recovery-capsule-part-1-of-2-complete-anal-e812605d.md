# material-e812605dc955

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RECIPROCAL_SUM_SOC_DOMAIN_AND_SHARP_DISTANCE_V1
## Recovery capsule part 1/2: exact quadratic spectral domain, second-order cone, all sharp tangents and optimal forbidden radius

Coordinator analytical research with complete exact symbolic execution. This gives an EXACT replacement for the earlier nested-radical adjacent-ratio test on a normalized reciprocal SUM. It does not close an actual E17 packet, shape cell, rooted orbit or type, and does not construct a110 body. The accepted interval34<=C_min<=622 is unchanged. The lower prohibition and attaining construction remain separate.

The earlier complete proof NORMALIZED_RECIPROCAL_SUM_FIBERS_V1, [internal-source-reference], SHA78bae956b24aa6da5628796f3012bcc0ffe146367531cb62fccc0d154da8d124, was read from0 throughEOF. Branch [internal-source-reference] was also read completely. Those results remain valid. The earlier sharp extreme coupling [internal-source-reference] is the FIRST endpoint of the tangent family below, not an incorrect bound. This proof is self-contained for its matrix theorem; it needs no inherited computational data. Physical specialization uses the accepted actual-covariance joint S_eq=U=1 ratio9 theorem in [internal-source-reference], not an U1-only premise.

The complete runnable source is part2, [internal-source-reference],4525bytes,SHA620ac2b7b8d02703b374ded6d47a6a0941b13530b5affb796286a7af09da7405. Both parts constitute the recovery capsule. There are no encoded payloads or omitted helpers.

## 1. Definitions and exact domain
Let A be a real symmetric positive definite3x3 matrix with trA=1, and let
 B=A^(-1)/tr(A^(-1)), S=A+B.
S denotes the MATRIX sum, not the stable-equilibrium count S_eq. Let a>=b>=c be its ordered eigenvalues. For k>1, the ratio-k class means BOTH consecutive ordered eigenvalue ratios of A are at mostk. The strict class requires both strictly less thank. Inversion reverses these two ratios.

Put d=k^2+k+1 and
 Phi_k(a,c)=(k^2-1)^2(1-a-c)
             +(k^4+k^3+2k^2+k+1)ac
             -k(k^2+k+1)(a^2+c^2).                         (1)

THEOREM. A real symmetric S is the sum of at least one normalized reciprocal pair in the ratio-k class if and only if
 0<S<I, trS=2, and Phi_k(lambda_max(S),lambda_min(S))>=0.    (2)
For the strict ratio class replace the last inequality by>0. Moreover every reciprocal pair over that same S has the same maximum adjacent ratio, so the test is not merely an existential choice among inequivalent ratio spectra.

Equivalently, inside 0<S<I,trS=2, the exact condition is the second-order-cone inequality
 a+c + (k+1)/(k-1)*sqrt((a-c)^2+4k(k-1)^2/d^2)
       <= 2(k+1)^2/d.                                    (3)
Again strictness is equivalent. This is a genuine convex cone constraint in the TWO ORDERED EXTREME-EIGENVALUE VARIABLES. It is NOT a convex matrix constraint in the entries of S: the minimum-eigenvalue substitution is nonlinear, and the full orthogonally invariant matrix image remains nonconvex. It must not be advertised as a new global affine separator stronger than the exact PAIR hull.

At k=9 the complete scalar criterion is
 Phi_9=6400(1-a-c)+7462ac-819(a^2+c^2)>=0,                 (4)
and its wholly rational conic form is
 norm_2((455(a-c),240)) <= 800-364(a+c).                  (5)
No eta variable, nested radical, inverse matrix variable or eigenvector choice occurs in(4). Eigenvalue orientation and the fixed-S two-branch/exceptional-circle arrow tests still remain when applying this domain to a particular geometry.

## 2. Why every unrestricted S in the stated domain has a reciprocal lift
For an actual A with positive eigenvalues x,y,z and x+y+z=1, put q=xy+xz+yz. The corresponding B eigenvalues are yz/q,xz/q,xy/q. Thus
 1-x-yz/q=x(y^2+yz+z^2)/q>0,
and cyclically. Hence every actual sum has0<S<I andtrS=2.

Conversely let0<S<I,trS=2 have ordered eigenvalues a>=b>=c>0. They obey the strict triangle inequalities, because a<1 and a+b+c=2. Set T=a^2+b^2+c^2,Q=a^4+b^4+c^4 and
 p(e)=48e^2-8Te+T^2-2Q.
The identities
 p(0)=(-a+b+c)(a-b+c)(a+b-c)(a+b+c)>0,
 p(c^2/4)=-(a^2-b^2)^2<=0
show that the smaller root eta lies in(0,c^2/4]. If a=b, the derivative at c^2/4 is16(c^2-a^2)<=0, so the same endpoint is the smaller root. The double-root scalar case is included. Put
 rho_1=sqrt(a^2-4eta),rho_2=sqrt(b^2-4eta),rho_3=sqrt(c^2-4eta).
Expanding p(eta)=0 gives
 2sum rho_i^4-(sum rho_i^2)^2=0.
The Heron factorization for the nonnegative ordered rho_i yields rho_1=rho_2+rho_3, including zeros. In an orthonormal S eigenbasis define
 D=diag(rho_1,-rho_2,-rho_3), A=(S+D)/2,B=(S-D)/2.
Then trD=0, A,B>0,trA=trB=1, and AB=eta I. Thus B is the normalized inverse of A. This proves unrestricted surjectivity without an assumption about generic eigenvalues.

## 3. The global sign factorization, including every ratio and repeated-eigenvalue boundary
Take any reciprocal lift. After interchanging A and B if necessary and removing an overall scale, its ordered raw spectrum is
 (rt,t,1), 1<=t<=r.
Here r is exactly the LARGER adjacent ratio. Write
 P=rt+t+1, Q=rt+r+1.
The ordered sum eigenvalues are
 a=rt/P+1/Q,
 b=1/P+rt/Q,
 c=t/P+r/Q.                                             (6)
Indeed
 a-b=(r-t)(rt-1)/(PQ)>=0,
 b-c=(t-1)(r^2t-1)/(PQ)>=0.
Thus the ordering remains correct at both double-eigenvalue walls and at the scalar point.

Substitution in(1) gives the COMPLETE factorization
 Phi_k(a,c)=(k-r)(kr-1)H/[(rt+r+1)^2(rt+t+1)^2],           (7)
where
 H=(k-1)^2(t^2+t+1)(r^2t^2+rt+1)+3k(rt^2-1)^2.          (8)
For k>1,r>=t>=1, every denominator and kr-1 is positive and H is strictly positive. Consequently
 sign Phi_k(a,c)=sign(k-r).                              (9)
This proves(2) and its strict version for every actual lift. Combined with the unrestricted existence proof it also proves sufficiency. Applying(9) for all k>1 shows that different reciprocal lifts of the same S cannot have different maximum adjacent ratios. No additional genericity assumption or a squared-root branch selection is hidden here.

The factorization is the decisive continuum proof. The finite exact controls in the executable are supplementary checks, not the justification of its range.

## 4. Second-order-cone equivalence
Put z=a+c,w=a-c. Directly,
 4Phi_k=d[(k-1)^2 z^2-(k+1)^2 w^2]
           +4(k^2-1)^2(1-z).
Completing the square gives
 [2(k+1)^2/d-z]^2
   -[(k+1)/(k-1)]^2*[w^2+4k(k-1)^2/d^2]
       =4Phi_k/[(k-1)^2 d].                            (10)
Because a,c<1, z<2, whereas2(k+1)^2/d>2, the first square's unsquared quantity is strictly positive. Taking the nonnegative square root is therefore equivalent, not a relaxation, and gives(3).
For k9 the exact rational identity is
 [800-364(a+c)]^2-[455(a-c)]^2-240^2=91Phi_9(a,c).        (11)
The right side in(5) is positive on the entire unrestricted sum domain. Strict/non-strict equivalence is preserved.

## 5. A continuum of sharp extremal spectral inequalities
The curved ratio-k boundary is parameterized by the raw spectra(kt,t,1),1<=t<=k. Define a_t,c_t by(6) with r=k. Every admissible sum satisfies
 a+m_k(t)c <= h_k(t),                                  (12)
where
 m_k(t)=k(k-t)(2kt+k+t+2)/[(k^2t-1)(k^2t+2kt+2k+1)],
 h_k(t)=(k-1)(k+1)(k^2t^2+kt^2+2kt+k+1)
                       /[(k^2t-1)(k^2t+2kt+2k+1)].     (13)
Strict adjacent ratios imply strict(12). The bound is sharp at that exact raw spectrum and its inverse, up to orthogonal conjugacy.

Proof: the left side of(3) is a differentiable convex function of(a,c), with strictly positive derivative in a. Its sublevel set is convex. At each boundary point(a_t,c_t), its tangent halfplane contains the whole sublevel set. Differentiating the rational boundary curve gives
 m_k(t)=-a_t'/c_t', h_k(t)=a_t+m_k(t)c_t,
which are exactly(13). Here
 c_t'=-(k^2t-1)(k^2t+2kt+2k+1)
                  /[(kt+k+1)^2(kt+t+1)^2]<0.
The curvature numerator is
 a_t''c_t'-a_t'c_t''
 =2k(k-1)(k+1)(k^2+k+1)/[(kt+k+1)^3(kt+t+1)^3]>0.
Thus m_k(t) decreases strictly. Its endpoints are
 m_k(1)=3k/(k^2+4k+1), h_k(1)=1;
 m_k(k)=0, h_k(k)=(k^2+1)/(k^2+k+1).
The first is exactly the earlier EXTREME_COUPLING inequality. The second is the linear SUM cap. Intermediate t give additional sharp spectral supports. These are inequalities in ordered eigenvalues, not global affine functionals of matrix entries.

For fixed ordered-spectrum geometry, the full conic test(3) is preferable to retaining just its first tangent. The original nonlinear fixed-S fibre reconstruction remains necessary to synchronize the signs of all primal and polar arrows.

## 6. The EXACT operator-norm distance from the formal forbidden control
Let
 S0=diag(9/10,11/20,11/20),
 D9={actual reciprocal sums with both adjacent ratios<=9}.
The earlier robust1/50 exclusion is improved to its OPTIMAL radius:
 dist_operator(S0,D9)=delta_*=(4189-40sqrt(10721))/1820
                         =0.0259942438889897... .        (14)
An exact rational bracket is2599/100000<delta_*<13/500. It is the smaller positive root of
 36400delta^2-167560delta+4331=0.
The open operator-norm ball of radius delta_* contains no member of D9. The closed ball meets D9 on its ratio9 boundary but contains NO sum with BOTH adjacent ratios STRICTLY below9. In particular the full closed ball is forbidden for the accepted physical jointS_eq=U1 covariance-normalized sums. These open/closed distinctions are essential.

To prove optimality put
 t_*=(89+sqrt(10721))/180 in(1,9),
 a_*=(40sqrt(10721)-2551)/1820,
 c_*=11/20,
 b_*=29/20-a_*.
Formula(6) at r9,t=t_* gives precisely(a_*,b_*,c_*), with a_*>b_*>c_*>0. Hence
 S_*=diag(a_*,b_*,c_*) belongs toD9,
 S_*-S0=diag(-delta_*,delta_*,0).
This attains the distance upper bound. It is a FORMAL reciprocal matrix control, not a polyhedron or a rooted-tree witness.

For the lower bound take the sharp tangent(12) at t_*, denote its coefficients m_*,h_*. We have0<m_*<1 by the strict decrease in Section5. If an arbitrary S inD9 has distance delta fromS0, its ordered a,b,c obey the variational eigenvalue bounds
 a>=9/10-delta, b<=11/20+delta.
Since trS=2,
 a+m_*c=(1-m_*)a+m_*(2-b)
        >=9/10+(11/20)m_*-delta.
But the sharp tangent requires a+m_*c<=h_*=a_*+(11/20)m_*. Therefore delta>=9/10-a_*=delta_*. This argument permits arbitrary eigenvectors, so a rotated matrix cannot evade the lower bound. For the strict ratio class the tangent is strict, which gives delta>delta_* and proves the closed-ball claim.

As an exact check, Phi_9(9/10,11/20)=-38979/400<0. The same optimal distance and ball statements hold for every orthogonal conjugate ofS0, by invariance.

## 7. Mechanical meaning and remaining bridge
For a genuine uniformly filled body use its ACTUAL covariance C and ONE physical SPD M:
 A=C^(1/2)MC^(1/2)/tr(CM),
 B=C^(-1/2)M^(-1)C^(-1/2)/tr(C^(-1)M^(-1)).
These are a normalized reciprocal pair. Under the accepted simultaneous S_eq=U1 theorem, their adjacent ratios are strictly below9, so(4),(5) are strict and the closed delta_* ball is impossible. This does not follow for an U1-only problem, an arbitrary independent C, a split-centroid relaxation, or an independently optimized polar matrix.

Passing the exact SUM condition guarantees that SOME reciprocal fibre exists, not that a particular relaxed pair is reciprocal or that either finite/circle fibre satisfies all geometric arrows. All actual moving centroid/covariance, true-facet incidence, same-origin polar and weak-equilibrium tests remain. Conversely, a shape cell whose necessary sums all violate(4), or all lie in the closed delta_* ball, would now be excluded without reconstructing inverse branches. NO such new actual cell has been certified in this material.

The useful next research move is applying this exact curved domain or its selected tangents to a genuinely compatible complementary packet from a still-open E17 shape sector. Replacing geometry by the formal S0 control does not establish that bridge. This research advances the nonlinear metric interface, not the numerical global bounds or the attainment question.

## 8. Complete reconstruction and observed evidence
Save the exact raw text of part2, [internal-source-reference], as reciprocal_sum_soc.py, UTF8/LF with its final newline. It contains all20 symbolic identities, every input to81 rational controls, the exact radical nearest point and distance bracket, and the deterministic report writer. No previous source, archive, random seed or non-default precision is needed.
Dependencies: Python>=3.11, SymPy1.14.0. Actual author environment was CPython3.13.5,SymPy1.14.0 with assertions enabled. Run
 python -B reciprocal_sum_soc.py build
 python -B reciprocal_sum_soc.py check
Both author executions completed and printed IDENTICALLY
 RECIPROCAL_SUM_SOC_EXACT_PASS 20 81 867 780c3025768b0a0ebab12d10b3198bc4a848fcd8d4c707c4b76448e3e134a3ae
Pins:
 reciprocal_sum_soc.py:4525bytes,SHA620ac2b7b8d02703b374ded6d47a6a0941b13530b5affb796286a7af09da7405;
 reciprocal_sum_soc.json:867bytes,SHA780c3025768b0a0ebab12d10b3198bc4a848fcd8d4c707c4b76448e3e134a3ae.
The continuum conclusions follow from the complete analytical proof, especially the globally positive factorization(7)-(8), not from81 controls or a numerical optimizer. These are the coordinator author's executions, not an independent second-author verification or proof-assistant formalization.
