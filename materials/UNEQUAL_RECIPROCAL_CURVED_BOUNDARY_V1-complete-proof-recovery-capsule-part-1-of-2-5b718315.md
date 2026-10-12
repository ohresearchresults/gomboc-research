# material-5b718315136f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_V1
## Recovery capsule part 1/2: complete proof and mechanical scope

Coordinator analytical result. This proves a universal failure of the single-corner-orbit shortcut for unequal adjacent spectral bounds, and supplies a continuum of sharp valid matrix inequalities for the actual finite-height bounds. It does NOT determine the entire unequal-bound joint convex hull, exclude an E17 body, or construct110. The mechanical bracket remains34<=C_min<=622.

The complete equal-bound proof [internal-source-reference] was read through EOF, returned SHA256 bdc9e45a6d95b687c51dfa89cb99db370748f61a95561be9c962f7f4007aeddd. The complete finite-height proof/executable [internal-source-reference] was read through EOF, returned SHA256 e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db. Their embedded historical parent-hash spellings do not override these transport identities. The finite-height theorem explicitly left the unequal-bound hull open: no accepted equal-bound theorem is retracted here. No claim of historical priority or external proof-assistant verification is made.

## 1. Definition
For a positive definite real symmetric3x3 H set A=H/trH and B=H^-1/tr(H^-1). Let the ordered adjacent eigenvalue ratios be r=lambda1/lambda2 and s=lambda2/lambda3. In a common orthonormal eigenbasis,
 a(r,s)=(rs,s,1)/(rs+s+1),
 b(r,s)=(1,r,rs)/(rs+r+1).
Both traces are1 and every product a_i b_i is the same positive scalar. Write R_pq for all such pairs with1<=r<=p,1<=s<=q, where p,q>1. Its closed convex hull is compact. Simultaneous orthogonal conjugation preserves this set. Independent permutations of A and B are not permitted.

## 2. One corner orbit is insufficient for EVERY unequal pair of bounds
Assume p>q; the p<q case follows by exchanging A,B and p,q. Put D=pq+q+1,E=pq+p+1 and define the affine symmetric matrix
 Z(A,B)=[D A+q E B-q(p+1)I]/[(q-1)(pq-1)].
At the endpoint pair a(p,q),b(p,q), Z=diag(0,0,1). Hence Z is positive semidefinite on every simultaneous orthogonal conjugate of that endpoint and on their entire convex hull.
For any q<r<p, direct substitution at s=q gives
 Z_11(a(r,q),b(r,q))=
 q(p-r)(q+1)(q-r)/[(q-1)(pq-1)(qr+q+1)(qr+r+1)]<0.
Thus a genuine admissible normalized reciprocal pair lies outside that proposed hull. At r=(p+q)/2 the negative value is exactly
 -q(p-q)^2(q+1)/[(q-1)(pq-1)(pq+q^2+2q+2)(pq+p+q^2+q+2)].
All denominators are strictly positive. A sufficiently small decrease of s from q retains negativity, so the failure includes strictly bounded ratios, not only a boundary ambiguity.

The formula for Z can also be obtained by inverting the3x3 matrix whose columns are(a_i(p,q),b_i(p,q),1). Its determinant is -(p-1)(q-1)(pq-1)/(DE), so the endpoint triangle is nondegenerate. Neither simultaneous diagonalization of convex combinations nor arbitrary independent eigenbasis choices enter this separation argument.

For the exact finite-height caps
 p=7024915/1000000, q=6832329/1000000,
take r=3464311/500000=(p+q)/2 and s=854041/125000=q-1/1000000. These are strictly inside the allowed rectangle. Their exact Z_11 is
 -385883813335505539449977458937500000000/652944173864974176371573892665219138651459903<0.
This is a formal SPD metric-pair control, not an actual-polyhedron construction.

## 3. A family of sharp supporting LMIs
Fix q>1 and a parameter t>1. Define
 P0=qt+q+1, Q0=qt+t+1,
 beta(t)=q Q0^2/P0^2,
 c(t)=tq/P0+beta(t)/Q0
      =1-(q^2+q+1)/P0^2.
Suppose beta(t)>4,0<c(t)<1,1<t<=p, and
 q/D+beta(t)p/E-c(t)>0.                         (C)
Then EVERY pair in R_pq satisfies
 A+beta(t)B>=c(t)I.                            (LMI)
It is sharp: equality in the smallest eigenvalue is attained at spectrum(r,s)=(t,q). Equality for a fixed unit vector e in e^T(A+beta B-cI)e=0 is possible ONLY at this spectrum, with e the largest-eigenvalue eigenvector of A. If both adjacent ratios are strictly bounded, the matrix inequality is strict.

### Proof, including all three eigenvalue branches
Put P=rs+s+1,Q=rs+r+1. The eigenvalues of A+beta B are
 f1=rs/P+beta/Q,
 f2=s/P+beta r/Q,
 f3=1/P+beta rs/Q.
Since2P-Q=r(s-1)+2s+1>0, Q/P<2. Hence
 partial_s f1=r/P^2-beta r/Q^2<0
whenever beta>4. Its minimum at each r therefore occurs at s=q. Exact algebra there gives
 f1(r,q)-c(t)=q(q+1)(r-t)^2(q^2+q+1)/[(qr+q+1)(qr+r+1)(qt+q+1)^2].
This is nonnegative and vanishes exactly at r=t.

For f2, rP-Q=r^2s-1>=0, so Q/P<=r. Thus
 partial_s f2=1/P^2-beta r^2/Q^2<0
because beta>1. Again reduce to s=q. The derivative in r has sign
 beta(q+1)-q^2(Q/P)^2,
and Q/P=(r(q+1)+1)/(rq+q+1) increases strictly with r, with derivative(q^2+q+1)/P^2. Consequently this derivative can change sign only from positive to negative. The minimum of f2(r,q) on[1,p] occurs at an endpoint, not at an interior critical point. At r=1, f2=f1>c because t>1. At r=p, strict positivity is condition(C). Thus the entire second eigenvalue branch is strictly greater than c.

Finally rs/Q is the largest eigenvalue of trace-one B, hence at least1/3. Therefore f3>=beta/3>4/3>c. The third branch is strictly above c. Combining the three branches proves the LMI and its equality classification. The proof is for actual reciprocal matrices; validity then extends linearly to their convex hull.

## 4. Whole parameter interval for the actual finite-height bounds
For the exact p,q in section2, every t in the CLOSED interval[t0,p], t0=(p+q)/2, satisfies the hypotheses of section3. Indeed t>q>4 gives Q0>P0, so beta>q>4; the displayed formula gives0<c<1. It remains to verify(C) on the whole interval, not at selected sample points.

After multiplication by positive DE P0^2, its numerator is the explicit quadratic polynomial
 N(t)=q E P0^2+p q D Q0^2-DE q(qt^2+2qt+2t+1).
Its three degree-two Bernstein coefficients on[t0,p] are
 16805508089422767838059705000453336360939393/50000000000000000000000000000000000000000,
 99178484020817288686938895105803121433281899/8000000000000000000000000000000000000000,
 99178484020817288686938895105803121433281899/4000000000000000000000000000000000000000.
All are strictly positive. With u=(t-t0)/(p-t0), N=n0(1-u)^2+2n1u(1-u)+n2u^2, giving strict positivity on the ENTIRE interval. Companion code reconstructs these coefficients directly from the displayed quadratic and verifies the identity.

At t=t0,
 beta=5217283587296089576103014320651369/760958541886838074432481761000000,
 c=747330279745777824432481761/760958541886838074432481761,
approximately6.856199516940241 and0.9820906640889158. The exact rational values, not these decimals, are inputs.

This is strictly stronger than merely retaining the old equal cap k=281/40. Its endpoint reciprocal pair a(k,k),b(k,k) violates the new LMI at its middle eigenvector by exactly
 -35255636973151081717682054594990311/1746418877593840551774406453539025000.
Mix that pair with(I/3,I/3) in weight1/10000000: all three old equal-cap LMIs are then STRICT, but the new LMI is still violated. The mixed control is a formal old-hull point, not claimed reciprocal or an actual body. The pure endpoint is reciprocal but violates the unequal ratio caps, exactly as it should.

## 5. No finite collection of fixed spectral orbits can describe this closed hull
For each t in[t0,p], the functional e^T(A+beta(t)B)e has the sharp minimum c(t), and section3 shows that any genuine reciprocal pair attaining it has the unique spectral ratios(t,q). Suppose the whole hull were generated by finitely many simultaneous orthogonal orbits of admissible reciprocal pairs. Choose t unequal to every first ratio in that finite list. Every generator then has strictly larger value of this functional; compactness of that finite union of orthogonal orbits gives a positive minimum gap. Convex combinations also have that gap and cannot contain a(t,q),b(t,q). Contradiction.

Thus, for these actual unequal caps, the exact hull requires a genuine continuum of spectral types, not a repaired finite corner list. This does NOT prove that no finite semidefinite lifted description exists. It also does NOT prove that the intersection of the LMIs in section3 is the entire joint hull; more general functionals tr(AH)+tr(BG) may give further restrictions.

The same non-finite-orbit conclusion holds for ANY p>q>=4: at t=p condition(C) equals q(p-1)(p-q)/D^2>0, beta>q>=4 and c<1. Continuity gives a nontrivial interval of t just below p. Exchange A,B for the analogous p<q case when the smaller cap is at least4. Section2's single-corner failure requires no such lower bound and holds for EVERY unequal p,q>1.

## 6. Physical specialization and remaining question
For the actual uniform volume covariance Sigma and one physical metric M with N=M^-1, put tau=tr(Sigma M), upsilon=tr(Sigma^-1 N), A=Sigma^(1/2)M Sigma^(1/2)/tau, B=Sigma^(-1/2)N Sigma^(-1/2)/upsilon. The accepted finite-height theorem supplies the above strict caps atV10/F9, including any candidate proper110. Therefore all new LMIs are STRICT. Their square-root-free congruence form is
 Sigma M Sigma/tau+beta N/upsilon>c Sigma.
The two normalizing traces cannot be dropped or identified. In independently trace-normalized metric variables this is linear; true primal and dual arrow signs are homogeneous and remain usable. The added constraints do not identify independent metrics as inverses or replace actual centroid/facet moments.

Next concrete research: develop an exact tractable unequal-cap joint hull or certified optimization over its curved exposed boundary, and integrate these constraints into actual-COM/covariance complementary-arrow problems that remain open. The continuum theorem prevents another finite-endpoint shortcut. It is not a global lower bound improvement.

## 7. Complete recovery and evidence level
Companion part2 contains the FULL4583-byte standard-library unequal_reciprocal.py, SHA256 d7922332fa9bd5b44e9946c44e3ab264b14e1c0fcf3a2121d6a391d91fea9fad. Save that Python fence exactly with final LF. Python>=3.10, assertions enabled, no external data/seeds/libraries.
Commands:
 python -B -S unequal_reciprocal.py build
 python -B -S unequal_reciprocal.py check
Output file unequal_reciprocal.json1018bytes SHA25629dd4d9efcd9d77c0ff1d8dd00028a6d17da681b09f961891ab928279c0e3b18.
Expected stdout from each:
 UNEQUAL_RECIPROCAL_CURVED_BOUNDARY_PASS 1018 29dd4d9efcd9d77c0ff1d8dd00028a6d17da681b09f961891ab928279c0e3b18
The coordinator executed build and check successfully before preservation. The exact controls and quadratic Bernstein positivity are executable; the all-ratio/all-orbit arguments above are analytic proofs, not inferred from samples. No independent second-authored replay or proof-assistant formalization is claimed.
