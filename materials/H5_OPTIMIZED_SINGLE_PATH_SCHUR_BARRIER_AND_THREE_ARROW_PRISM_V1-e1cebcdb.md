# material-e1cebcdbe236

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_OPTIMIZED_SINGLE_PATH_SCHUR_BARRIER_AND_THREE_ARROW_PRISM_V1

## Scope and source authority
This work gives (i) an exact linear-programming characterization of the fully optimized single-cut ellipsoidal sufficient test, (ii) a genuine five-dimensional H5 box on which ALL NINE such tests for the literal T56 tree fail, and (iii) a three-arrow negative stress excluding664 complete trees on a larger residual prism containing that box. Failure here concerns every choice of eta,v,mu in each SINGLE Schur test, not merely one numerical fit. It does not concern every full path stress, a sum of cuts, or the full original-arrow stress cone. No actual complete weak-arrow survivor is supplied.
The proper homogeneous class110 minimum remains open, with accepted34 <= C_min <=622. No all-root H5 result, whole-E17 exclusion, new equilibrium census or attaining construction is asserted. Old exclusions on other domains cannot be added numerically to the664 extensions without a literal overlap calculation.

Fully read scientific antecedents are:
* minimum-0247, SHA256 f31e0f04d48f1b80f427df0b3ac4342cd2b61e84f1edaaf280330521e356cce1, H5_PATH_ENERGY_FIVE_ARROW_CAP_AND_CLOSED_REFLECTION_SEPARATION_V1. The literal H5 geometry, T56 labels and actual moments below are unchanged. Its author-executed proof is accepted without coordinator replay.
* [internal-source-reference], TREE_PATH_ENERGY_ELLIPSOIDAL_RESIDUAL_CUT_V1.md,9224 bytes, SHA256 6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866. This actual retrieved hash corrects the older branch's erroneous777d3b2e307553b77a92f077911d7040e94b73f764ad8b68b6c96baaf66e3633e identity.
* minimum-0246, SHA256 af162492fd1bf1598c3c52ebc979b310c73e8a8d04ae4b557455be4e4cae8ce1, the coupled-reflection norm-order ceiling and actual SPD norm-blind control. Its scalar ceiling is distinct from the stronger single-Schur barrier proved here.
* [internal-source-reference], CENTROID_FLOW_TREE_COVARIANCE_CUT_V1.md, SHA256 5b7063bbc081f028980859fd54f353d4688e02467dd5e48fc3c29250e83410d4. It motivates retaining complete energy stresses; no computational output from it is needed.

The complete new standalone executable is [internal-source-reference], h5_path_schur_barrier.py.txt,12878 bytes, SHA256 f9d94c90a9b70bc248e93424433d3776978acc9af6655d170b38b78c5b48ca42. Together with this proof it is a self-contained recovery capsule. No earlier sandbox, code extraction or external input checkpoint is needed.

## 1. Optimizing the ellipsoid is exactly a signed-convex-hull LP
Let u_i, i in D, span R^d. The source a belongs to D. Let w_k be any finite list of columns and put

 r=u_a+sum_k c_k w_k, c_k>=0,
 G=sum_i mu_i u_i u_i^T, mu_i>=0, sum_i mu_i=1.

The following conditions are equivalent:

(A) Some c,mu satisfy G-r r^T positive definite.
(B) Some c>=0 and signed t_i satisfy r=sum_i t_i u_i and tau=sum_i |t_i|<1.
(C) The polyhedron u_a+cone{w_k} meets the interior of absconv{u_i}, the convex hull of all positive and negative u_i.

Thus the strictly feasible test can be decided by the LP minimizing sum(t_i^++t_i^-) under

 u_a+sum c_k w_k=sum(t_i^+-t_i^-)u_i,
 c_k,t_i^+,t_i^->=0.

The value being strictly below1 is the criterion. This is elementary finite-dimensional convex geometry, related to the classical signed-hull formulation of c-optimal design; no novelty is claimed for that general duality. The useful specialization here is its exact path-depth failure alternative and its actual H5 realization.

Proof of A=>B. Positive definiteness implies G>0 and r^T G^-1 r<1. Define t_i=mu_i u_i^T G^-1 r. Then sum t_i u_i=r, and Cauchy-Schwarz gives sum |t_i| <= sqrt(sum mu_i)*sqrt(sum mu_i(u_i^T G^-1 r)^2)=sqrt(r^T G^-1 r)<1.

Proof of B=>A, with a quantitative floor. Let delta=1-tau>0 and n=|D|. Choose mu_i=|t_i|+delta/n. These are positive probabilities. For every vector y,

 (y.r)^2 <= [sum t_i^2/mu_i] [sum mu_i(y.u_i)^2]
            <= tau y^T G y.

Therefore

 G-r r^T >= delta G >= (delta^2/n) sum_i u_i u_i^T >0.       (1)

This formula gives exact rational positive-definite certificates from rational strict LP witnesses; it does not silently discard a nonzero residual. B<=>C is the definition of the interior of a full-dimensional centrally symmetric convex hull.

## 2. The exact single-path failure alternative
For a directed tree edge a->b, let D be the source component, depth_i the distance from i to a, and sigma_i=(depth_i-1)/(depth_i+1), including sigma_a=-1. Use columns

 w_0=u_b-u_a,  w_i=u_i+sigma_i u_a.

When D spans R^d, the optimized single-cut test G-r r^T>0 FAILS if and only if there is a vector n satisfying

 n.u_a=1,
 n.(u_b-u_a)>=0,
 -sigma_i <= n.u_i <=1  for all i in D.                     (2)

Proof. If the polyhedron u_a+cone W misses the open absolute convex hull, finite-dimensional separation supplies nonzero n with n.W>=0 and n.u_a>=max_i|n.u_i|. Since u_a is itself among the u_i, equality holds. Spanning ensures the common value is positive, so normalize it to1. The column inequalities give n.u_i>=-sigma_i; the absolute-convex-hull bound gives n.u_i<=1. Conversely, (2) gives n.r>=1 for every nonnegative eta,v and n^T G n<=1 for every probability mu. Hence

 n^T(G-r r^T)n<=0,                                         (3)

which rules out positive definiteness for every fit. If D does not span the ambient space, G-r r^T cannot be positive definite either: in any vector annihilating D its quadratic form is nonpositive. With rational input coordinates the feasible linear systems in the primal or normalized dual have rational witnesses. No floating-point optimizer success or failure is required for either exact implication.

The original rational path identity gives the FULL negative-arrow matrix

 C_path=-eta H_ab-sum_i(v_i+mu_i)sum_{e in path(i,a)}H_e
       =(G-r r^T)/2+(u_a-r)(u_a-r)^T/2
         +sum_i v_i S_i+(1/2)sum_i mu_i sum_path Delta_e Delta_e^T,

where H_ij=sym(u_i,u_j-u_i) and S_i>=0 are the exact path-square remainders. A strict signed LP witness therefore gives C_path >= delta^2 sum u_i u_i^T/(2|D|). But (2) only refutes the first Schur term, not positivity of the full C_path. It certainly does not refute an arbitrary nonnegative combination of original negative-arrow matrices. The following actual example makes that distinction uniform in all five physical parameters.

## 3. Literal H5 geometry, actual moments and domains
Write s=1-lambda and

 B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
 B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

Let z_i=(s B_i,0), i=0,...,6, and z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1). The maximal-face cycles are

 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
 (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

The eight oriented fan tetrahedra are

 (0,1,2,8), (0,9,8,2), (0,9,2,3), (0,9,3,4),
 (0,4,5,7), (0,4,7,9), (0,6,7,5), (0,7,8,9).

For strict original shape conditions 0<x,r<1, p,q>0, p+q<1 and0<lambda<1 this is the same genuine10/17/9 family as the parent. The new verifier checks the actual fan identities as FULL five-variable polynomial identities, not at a frozen centroid:

 A=(31-24xp-24rq)/64,
 bx=509/3072-3xp/8+3x^2 p/32+xp^2/8-rq^2/8,
 by=509/3072-3rq/8+3r^2 q/32+rq^2/8-xp^2/8,
 V=A s^2/3+lambda/6,
 Jx=s^3 bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
 Jy=s^3 by/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
 Jz=A s^2/12+lambda/12+lambda^2/24.

Throughout g=J/V and u_i=z_i-g. Since7/64<=A<=31/64 on the full physical triangle with x,r in[0,1], the displayed quadratic volume gives7/192<=V<=1/6 for lambda in[0,1]. Collapsed indexed boundary bodies are positive-volume limits, not genuine E17 bodies. Full support fidelity is directly checked at the rational central body; the genuine open-family incidence statement is the unchanged geometric one from the parent, not a claim that this new code recomputes every support guard on every boundary stratum.

Define the closed prism R, in the order(x,r,p,q,lambda), by

 R=[15/16,1] x[1/4,1/2] x[5/16,7/16] x[5/16,7/16] x[0,1/16].

Define its interior comparison box

 Omega=[247/256,249/256] x[95/256,97/256] x[95/256,97/256]
       x[95/256,97/256] x[7/256,9/256].

Its centre is P0=(31/32,3/8,3/8,3/8,1/32). Every point of Omega is a genuine body, is in R, has p+q>1/2 and lambda>1/64, and has both p,q<9/16. Thus it lies outside both of the EEl parent's five-arrow caps and outside the earlier half-triangle all-root domain. No claimed novelty count relative to every historical certificate follows solely from these parameter comparisons.

## 4. Three arrows exclude664 complete trees on R
Use the literal complete T56 tree rooted at2:

 T=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3)).

The remarkably small stress is

 C3=-2H12-5H56-2H70.                                      (4)

Its unnormalized matrix polynomial is

 P=V C3=-2 sym(Vz1-J,z2-z1)-5 sym(Vz5-J,z6-z5)
         -2 sym(Vz7-J,z0-z7).

The complete executable expands P-I/2048 on R into the rectangular Bernstein basis of degrees(3,2,3,2,4). ALL720 coefficient matrices are positive definite, proved by2160 exact positive leading principal minors after clearing common denominators. No global quadratic lowering, term deletion, parameter sampling or inferred continuity radius enters. Therefore

 V C3>I/2048 throughout R.                               (5)

For every nonzero PSD metric M, at least one of the three selected weak arrows fails, quantitatively

 (2D12+5D56+2D70)/9 < -tr(M)/(18432 V) <= -tr(M)/3072.

The exact true-edge extension enumerator emits every full nine-arrow rooted tree containing those three arrows. There are664, with root counts in label order

 (150,0,176,90,46,0,98,0,56,48).

The result does not claim that all664 are new after all preceding reflection or stress atlases. It is not all48790 rooted trees and does not exclude the whole H5 family. The complete extension list is regenerated and stored in the report.

At P0, actual V=614173/6291456 and

 g=(257649251/1437515776,82330207/314456576,647965/2456692).

The matrix C3 has denominator20608226164736 and upper-triangle integer entries, ordered00,01,02,11,12,22,

 (1704871490399,886989620462,-4694328250368,
  3552832758912,-5889248468992,30345403564032).

Its leading numerator minors are1704871490399,5270372694017369680592444,71551880024728861842861697003555913728, all positive. These central values are a readable control, while (5) rests on the full uniform coefficient proof.

## 5. Every optimized single-cut Schur test for T56 fails on Omega
Only three source components can have full centred span: those of0->1,1->2 and3->2. The other six have fewer than three vectors, so their G has rank<3 for every probability mu and their Schur test cannot be PD, regardless of eta,v.

For the three nontrivial components set U_i=Vz_i-J. Define n_a=N_a/L_a by

 N0=(0,-V,0),                         L0=Jy;
 h=(p,p-3x/4,0), N1=Vh,              L1=h.U1;
 N3=V(z4 cross z9)-z4 cross J-J cross z9,
 L3=N3.(z3-z4).

The source components and depths are

 a0: {0:0,5:2,6:1,7:1};
 a1: {0:1,1:0,5:3,6:2,7:2};
 a3: {3:0,4:1,9:1}.

The formula N3=V(u4 cross u9) makes n3.u4=n3.u9=0. The source normalization n_a.u_a=1 holds identically for all three. The other obligations in (2) are checked with the exact cleared polynomials

 L_a>0,
 N_a.(z_parent(a)-z_a)>=0,
 V L_a-N_a.U_i>=0,
 N_a.U_i+sigma_i V L_a>=0.

Fourteen of the selected expressions, including the separate source-normalization identities, vanish identically. The remaining19 guard polynomials have ALL34048 coefficients strictly positive in the common rectangular Bernstein degrees(3,3,3,3,6) on Omega. Their minimum is exactly

 4409171931642709780871909/950737950171172051122527404032 >0.

The executable distinguishes the identities from strict guards and emits every coefficient and label. Hence (2)-(3) hold everywhere on Omega for all three nontrivial cuts. The six small components are a4:{4},a5:{5},a6:{5,6},a7:{7},a8:{8},a9:{9}. Together these facts prove that ALL NINE optimized single-cut Schur tests fail on every body of Omega.

At P0 the explicit normalized dual vectors are

 n0=(0,-314456576/82330207,0),
 n1=(10062610432/3331872273,-3144565760/1110624091,0),
 n3=(127115571200/38191576819,263832833024/114574730457,
     58486379977/38191576819).

The report stores all their exact descendant and parent values. In particular n3.u2=4614036239/3695959047>1. These are duals for the optimized Schur relaxation, not a single physical metric satisfying the original arrows. Different n_a are allowed because the nine separate sufficient tests are being refuted; no common primal metric is inferred.

## 6. Interpretation and the next nonredundant question
The EEl parent retained a control where ONE fixed fit fails but its full stress remains PD. The present box strengthens the negative statement to EVERY fit for EVERY selected single cut, while an explicit original three-arrow stress remains PD uniformly. Optimizing mu or making nonnegative least-squares fitting more accurate cannot repair this particular sufficient condition on Omega.

The theorem does not say that every full path C_path is non-PD, that sums of cuts fail, or that more general centroid-flow certificates fail. Those mechanisms retain PSD energy terms that the Schur floor discards. The new three-arrow prism also gives useful positive exclusion outside the earlier p>=9/16 and q>=9/16 caps. The strongest next question is complete-support coverage by full stresses or a structural characterization retaining the full remainder, not numerical refinement of a now-proved impossible individual Schur fit.

## 7. Complete recovery and observed executions
The standalone source is [internal-source-reference], h5_path_schur_barrier.py.txt,12878 bytes, SHA256 f9d94c90a9b70bc248e93424433d3776978acc9af6655d170b38b78c5b48ca42. Save its bytes as h5_path_schur_barrier.py and run

 python -B -S h5_path_schur_barrier.py output

It needs Python>=3.11 and the standard library, with assertions enabled. The observed interpreter was CPython3.13.5. The source reconstructs all physical inputs, moment identities, stress matrices, normalized-dual guards, complete extensions and the rational central control. No input files other than this complete source are required.

Normal exact execution and a separate source-only cold directory reproduced all three JSON files and the stdout receipt byte-identically. Optional numerical rediscovery was also executed with

 OPENBLAS_NUM_THREADS=1 python -B h5_path_schur_barrier.py located --locate

under NumPy2.3.5/SciPy1.17.0. It recovers the three active arrows using an explicitly bounded eigenvector/LP cut loop; the small integer weights(2,5,2) remain literal exact inputs and are accepted only by the exact checker. Numerical discovery is not the proof. This new computation is coordinator-executed work, not an independent replay of the parent's larger certificate.

Output pins:

 h5_three_arrow_matrices.json:98495 bytes
 SHA256 2c75bab5cdc3675d3e883a163f9054845cacdfed3ec82fbdecc592a5b92f7e48
 h5_schur_barrier_guards.json:1804238 bytes
 SHA256 5c7933d2392a414f29ae5084d54ad7266445e4568067e0d913e0a26cfa2587ce
 h5_path_schur_barrier_report.json:43451 bytes
 SHA256 21397c00da77f25d9383961f7b83cfed3b92b93361b6c504911539e326c4d6fb
 normal stdout:689 bytes
 SHA256 0e42a046922cd8925f06b1960fd1e1495deea9e69d4e0d4676310da7dd163e2c
 optional-discovery stdout:742 bytes
 SHA256 0ecb58f41e5b7cc5faadfe724109d37769fcfc4c1244980682d05b459aa7db64

Expected normal markers:

 H5_PATH_SCHUR_ACTUAL_FAN_IDENTITIES_PASS 4
 H5_THREE_ARROW_RESIDUAL_PRISM_PASS 720 2160 664
 H5_ALL_NINE_OPTIMIZED_SINGLE_PATH_SCHUR_TESTS_FAIL_PASS 3 6 19 34048 14
 H5_OPTIMIZED_SINGLE_PATH_SCHUR_BARRIER_AND_THREE_ARROW_PRISM_PASS

These are exact rational/integer computations plus the analytic arguments above, not proof-assistant formalization. The canonical global bound and its separately preserved attaining construction remain unchanged.
