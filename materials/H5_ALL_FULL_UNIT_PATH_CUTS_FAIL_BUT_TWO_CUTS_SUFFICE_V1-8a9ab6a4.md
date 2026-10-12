# material-8a9ab6a4da92

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_ALL_FULL_UNIT_PATH_CUTS_FAIL_BUT_TWO_CUTS_SUFFICE_V1

## Result and scope
For the actual uniformly filled H5 body and literal complete T56 tree, there is an explicit genuine five-dimensional parameter box on which NONE of the nine complete single-source UNIT-path energy cones contains a nonzero positive-semidefinite matrix. This includes every choice of eta,v,mu and the FULL PSD energy remainder, not only the earlier Schur sufficient floor. Nevertheless a sum of two such cuts is positive definite throughout a larger prism. Thus the minimum number of these source cuts needed for a positive-definite stress for T56 on the small box is exactly two. This is an auxiliary method-complexity statement, not the polyhedron's C=2E minimum.

The new two-cut stress excludes439 complete extensions on the prism, all within the previously proved664 three-arrow extensions there. No additional tree coverage is claimed from439. No all-root H5/whole-E17 exclusion, actual complete weak-arrow survivor, equilibrium census or new attaining construction is supplied. The accepted global interval remains34 <= C_min <=622, and attaining that lower bound remains separate.

The restriction to the RATIONAL UNIT-path identity matters. The result does not refute all possible non-unit weighted path identities, coupled cuts, global centroid-flow stresses or the full original-arrow cone. In particular it does not extend the single-cone obstruction to a common physical metric satisfying all original arrows: different source cuts below have different dual metrics.

## Exact antecedents and recovery dependency
The preceding coordinator proof [internal-source-reference], H5_OPTIMIZED_SINGLE_PATH_SCHUR_BARRIER_AND_THREE_ARROW_PRISM_V1.md,15955B, SHA e1cebcdbe2360ccf1187668f3417e016d54cbd9f33dce755546a162eb5e8c978, gives the exact LP characterization of optimized Schur tests, their radius1/256 H5 failure box, and the664-tree three-arrow prism. Its computational input is the complete source [internal-source-reference], h5_path_schur_barrier.py.txt,12878B, SHA f9d94c90a9b70bc248e93424433d3776978acc9af6655d170b38b78c5b48ca42.
The rational unit-path identity itself is [internal-source-reference], SHA6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866. The unchanged actual H5 geometry and original author comparison are in the fully read minimum-0247, SHA f31e0f04d48f1b80f427df0b3ac4342cd2b61e84f1edaaf280330521e356cce1. No independent replay of that worker's computation is claimed.

Recovery capsule part1/2, common actual geometry and exact polynomial core: [internal-source-reference] as above, saved as h5_path_schur_barrier.py.
Recovery capsule part2/2, complete new dual/coupling verifier: [internal-source-reference], h5_full_single_path_barrier.py.txt,8578B, SHA0ce38a6275073c72067df1952545d2430890ba42bacf45a7ac897bf8355773b0, saved as h5_full_single_path_barrier.py in the same directory.
Both exact units are needed. The second verifies the first's full source SHA before importing its helpers; neither a generated checkpoint nor an old sandbox is an input.

## 1. The entire single-unit-path stress cone has a finite ray description
Fix a tree directed toward a root. For a selected edge a->b let D_a be the source component and define H_ij=sym(u_i,u_j-u_i), with all u_i=z_i-g at the ONE actual reference point. For each i in D_a minus{a}, let

 R_ai=-sum_{e in path(i,a)}H_e,
 R_a0=-H_ab.

The FULL rational unit-path cut is

 C_a=-eta H_ab-sum_{i in D_a}(v_i+mu_i)sum_path(i,a)H_e,
 eta,v_i>=0, mu_i>=0, sum mu_i=1.

Its attainable cone is EXACTLY

 K_a=cone{R_a0,R_ai:i in D_a minus{a}}.                 (1)

One inclusion follows by setting alpha_i=v_i+mu_i. For the other choose mu_a=1 and all other mu_i=0, take eta to be the desired exit-ray coefficient, and v_i equal the desired path-ray coefficients for i!=a. The source path is empty, so its unit probability contributes nothing to C_a. Thus (1) already includes every fit and every PSD remainder of the full rational identity. It is not merely a lower bound obtained by throwing away squares.

If a positive-definite matrix M_a satisfies

 tr(M_a H_ab)>0 and tr(M_a sum_path(i,a)H_e)>0
 for every i in D_a minus{a},                         (2)

then tr(M_a C)<0 for every nontrivial nonnegative ray combination C in K_a. Therefore K_a contains no nonzero PSD matrix. This is a dual obstruction to one cone, not a solution of all original weak-arrow inequalities. There are finitely many rays, so rational strict witnesses can be checked directly and extended to an explicit parameter domain without any optimizer claim.

## 2. The unchanged H5 body and the two domains
Set s=1-lambda and use

 B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
 B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16),
 z_i=(s B_i,0), i=0,...,6,
 z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The maximal facets, eight-tetrahedron oriented fan, all17 true edges and exact actual volume/first-moment polynomials are fully literal in recovery part1. The new code regenerates their four FULL five-variable fan identities. In particular g=J/V is never frozen or replaced by a basal centroid;7/192<=V<=1/6 on the physical parameter domain. Strict0<x,r<1,p,q>0,p+q<1,0<lambda<1 gives the original genuine10/17/9 lattice.

The same complete tree is

 T56=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3)),

rooted at2. Let P0=(31/32,3/8,3/8,3/8,1/32), and set

 Omega2=product_{k=1}^5[P0_k-1/2048,P0_k+1/2048].

This is a genuine positive-width box, smaller than the earlier radius1/256 Schur-failure box. It has p+q>1/2, lambda>1/64 and both p,q<9/16. It lies strictly inside the positive theorem's larger prism

 R=[15/16,1]x[1/4,1/2]x[5/16,7/16]x[5/16,7/16]x[0,1/16].

Only the original genuine interior bodies have a true E17 incidence. The closed prism also includes indexed positive-volume limits, whose polynomial inequalities are valid but which are not renamed genuine10/17/9 bodies.

## 3. Nine exact positive-definite dual metrics on Omega2
Each M_a is constant in physical coordinates and has entry denominator10^6. Its six upper-triangle numerators are listed in the order00,01,02,11,12,22:

 a=0: (388629,-480023,-54147,599940,68524,11431)
 a=1: (531828,-494838,-59369,461155,55240,7016)
 a=3: (478306,408762,280337,356112,238960,165582)
 a=4: (479085,298864,-357016,202306,-218627,318609)
 a=5: (72460,163193,139487,539916,438721,387623)
 a=6: (41736,-121836,-111543,476927,457984,481337)
 a=7: (49465,-199365,-24047,926335,109643,24200)
 a=8: (875956,-12831,289409,15924,6946,108120)
 a=9: (139748,283470,160780,657967,361955,202285).

All27 exact leading principal minors are positive. Rounded traces need not equal1 exactly; no trace normalization is used in the proof. For each selected exit and each nonempty descendant path, the code forms its actual-centroid numerator

 H^V_ij=sym(Vz_i-J,z_j-z_i)=V H_ij.

There are19 rays across the nine cuts. The code proves, for every corresponding positive path/exit sum A,

 tr(M_a V A)>1/65536 throughout Omega2.                (3)

Indeed all24320 coefficients of the19 shifted scalar polynomials tr(M_a V A)-1/65536 are strictly positive in rectangular Bernstein degrees(3,3,3,3,4), with1280 coefficients per polynomial. The minimum shifted coefficient is exactly

 31798461952126594229873549169/15845632502852867518708790067200000.

Together with M_a>0 and V>0, (3) proves (2) uniformly. For a nontrivial ray combination of coefficient sum W_a,

 tr(M_a C_a)<-W_a/(65536 V)<0.

Consequently every K_a has no nonzero PSD member on Omega2. This includes the full energy terms of all nine single-source rational unit-path cuts. These nine dual metrics are not combined into one alleged weak-arrow metric. The stronger original three-arrow theorem already proves that such a common complete-tree metric does not exist here.

## 4. Two cuts suffice on the larger prism
Consider the explicit matrix

 C_pair=-2H01-2H12-5H56-2H70.                           (4)

It is exactly a sum of TWO full unit-path cuts:

 cut at1->2: eta=2, v7=2, mu1=1, all other v and mu=0,
 cut at5->6: eta=5, mu5=1, all v and other mu=0.

The first has the path7->0->1 and equals-2H12-2H70-2H01; the second is-5H56. All coefficients are legal even though the respective individual Schur matrices are singular or indefinite. Neither full cut can be PSD on Omega2 by the preceding dual certificates, but their sum is PD.

The new exact checker proves

 V C_pair>I/2048 throughout R.                        (5)

All720 coefficient matrices of V C_pair-I/2048, in rectangular degrees(3,2,3,2,4), have2160 positive exact leading minors. These are ORIGINAL moment polynomials, not global quadratic lowerings. With total original-arrow weight11 and V<=1/6,

 (2D01+2D12+5D56+2D70)/11 < -tr(M)/(22528 V)
                            <=-3 tr(M)/11264

for every nonzero PSD common metric M. Thus at least one selected actual arrow is strictly negative.

The four-arrow support has439 exact complete extensions, root counts

 (0,0,176,90,46,0,23,0,56,48).

Their complete nine-arrow lists are regenerated in the report. They are a subset of the preceding664 extensions of the three-arrow support(12,56,70) on the SAME R, so439 does not enlarge that earlier coverage. The mathematical gain is a demonstrated need for coupling: on Omega2, one of the nine full single-unit-path cones never suffices for T56, whereas the displayed two-cut sum always does.

At P0 the coupled matrix has denominator10304113082368 and upper-triangle numerator

 (822978287824,504748484239,-2285457122304,
  1776416379456,-2944624234496,15172701782016).

Its leading numerator minors are822978287824,1207181078085639937134623,8695252820659119176999436287832227840. The source records the actual point's volume, first moment, centroid, positive fan volumes and56 strict nonincidences as well. The uniform proof is (5), not this one-point control.

## 5. Interpretation and unresolved direction
The previous scalar norm-order obstruction could be bypassed by path energy. The previous optimized Schur obstruction could potentially be bypassed by its discarded PSD remainder. This result identifies another genuine boundary: even keeping that complete remainder and optimizing every single-source UNIT-path cut cannot succeed on Omega2. Coupling two source cuts repairs this specific obstruction exactly.

No inference is made about sharp/non-unit path constants, the global actual-centroid flow cone, or a general full-tree negative-arrow stress. Since individual negative arrows can themselves be written as single-cut exit rays, allowing arbitrary sums of cuts recovers the original arrow cone rather than strengthening it. The value of the coupling description is a structured certificate, not a stronger relaxation. The next substantial research question is whether such small coupled supports or genuine global centroid-flow relations give broad complete-tree coverage in the unresolved p+q>1/2 region, not another search for an impossible isolated unit-path certificate at P0.

## 6. Reproduction and evidence level
Save the two exact recovery parts under the filenames specified above, in the same directory. Run

 python -B -S h5_full_single_path_barrier.py output

Only Python>=3.11, standard library and assertions are required. Observed CPython3.13.5. A normal run and a separate cold directory containing only these two exact source inputs reproduced all three JSONs and stdout byte-identically. Optional rediscovery also passed:

 OPENBLAS_NUM_THREADS=1 python -B h5_full_single_path_barrier.py located --locate

with NumPy2.3.5/SciPy1.17.0. The complete bounded LP/eigenvector dual locator and rounding rules are in part2; its proposals are not proof. The literal rational matrices, full polynomial checks and positive minors are acceptance. No earlier worker atlas was independently replayed.

Output pins:

 h5_full_unit_path_dual_guards.json:1584220B
 SHA09a1454402bea764d7de431a3ebbd66742e54796a33738ff295c9e73db2acb02
 h5_two_unit_path_cut_matrices.json:98581B
 SHA347f6b381c278df210dfe536898c409a1a8fea41a1cb3231ea2f20a17913d81c
 h5_full_single_path_barrier_report.json:31808B
 SHA2d15c160ab5a04fb79c6c3e99513efa59154798f2a154e57390e8a2b07677b5b
 normal stdout:688B
 SHAba5097e4ca81014034833f5e08cd301a5fc71871ed151d4cb6d5b5166df5cd85
 optional-discovery stdout:743B
 SHA8f790c39011ac19da11fae179490146afcb34b55a6f63a9a3100f6e349ad63d0

Expected normal terminal markers:

 H5_FULL_UNIT_PATH_ACTUAL_FAN_IDENTITIES_PASS 4
 H5_ALL_NINE_FULL_UNIT_PATH_CONES_FAIL_PASS 9 27 19 24320
 H5_TWO_UNIT_PATH_CUTS_SUFFICE_PASS 720 2160 439
 H5_ALL_FULL_UNIT_PATH_CUTS_FAIL_BUT_TWO_CUTS_SUFFICE_PASS

The proofs and computations are exact but not proof-assistant formalization. Bounds34..622, whole-E17 coverage and the separately preserved C622 attainer remain unchanged.
