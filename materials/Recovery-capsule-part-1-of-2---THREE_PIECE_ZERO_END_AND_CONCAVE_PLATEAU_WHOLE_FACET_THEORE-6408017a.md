# material-6408017af3a7

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1 of 2: whole-facet theorems for three-piece zero-end profiles and arbitrary concave plateaux

Object identity: THREE_PIECE_ZERO_END_ALL_FACETS_AND_ARBITRARY_CONCAVE_PLATEAUX_V1.
Part 2 contains the complete standalone executable homothetic_three_piece_and_plateau.py. Both parts constitute the proof/recovery capsule. The source has no external computational helper or input. No sandbox, filename or hash substitutes for that literal source.

## 1. The two new theorems and their limits
Let D be ANY compact full-dimensional convex planar body, and let h be a continuous nonnegative concave function on a compact interval, positive in its interior. Fill P={(h(z)u,z):u in D} uniformly. Use its ACTUAL volume centroid g, volume covariance Sigma, and for a genuine WHOLE flat facet F the uniform second moment T_F about the SAME g. Let alpha_F=distance(g,aff F) Area(F)/Volume(P).

THEOREM A. If h has at most THREE affine pieces and vanishes at BOTH endpoints, every genuine whole flat facet satisfies alpha_F T_F <= (3/2) Sigma. For three genuine pieces the full gap is positive definite. The constant 3/2 is the sharp supremum for this class. The statement includes arbitrary asymmetric bases and all nonsingular affine images. At coincident slopes, merge the coplanar pieces and use the accepted all-two-piece theorem for the actual whole facet; do not sum fragment estimates.

THEOREM B. For an ARBITRARY concave h, suppose its maximum is attained on a nondegenerate interval I. Every whole lateral facet over that maximal constant-height interval satisfies the same full 3/2 inequality. If any positive-length tail remains outside I, its full gap is positive definite. The tails may be curved, may have arbitrarily many slope changes and need not be symmetric; the actual centroid need not lie over I. This theorem concerns these plateau facets, NOT every other affine piece of an arbitrary profile. When there are no tails the body is a prism, already covered by the accepted prism theorem.

Neither statement proves the arbitrary-concave-profile theorem, the universal 3D whole-facet theorem, a mechanical U2/S2 exclusion, an E17 whole-incidence exclusion, or a new own110 construction. The separate accepted bounds C>=34 and C<=622 remain unchanged. The general nonlinear completion obstruction in [internal-source-reference] remains valid: fixed-centre/fixed-facet/fixed-interval affine-tail minimization is false.

Analytical inputs read completely for this research: arbitrary uniform-planar whole-edge 3/2 and alpha_D<=2/3 in [internal-source-reference], SHA240b58ed6bde2703c5788573c8c20ca2a4278a3abc1cfc66fb8f607645eb646d,13829B; the mixed-profile reduction and all-two-piece theorem in [internal-source-reference], SHA9db28182e955108523e5d157a00e1660c4e415c68ed4aec4e12d92922ba4cd4a,18894B. Exact integration/control routines were adapted from the fully read [internal-source-reference], SHAfd43cd9771d265d3942b4839175ed54dedef7ab3180f0dc8443ebacc089f6c26,12673B; the required routines are ALL included in the new standalone source, so that old helper is not a computational dependency.

## 2. The actual mixed-matrix reduction
Translate the ACTUAL area centroid of D to 0. Put

    V=int h^2, M=int z h^2, mu=M/V,
    E=int z^2 h^2, S=E-M^2/V, N4=int h^4.

Then Volume(P)=Area(D)V, g=(0,0,mu), and Sigma=diag((N4/V) Sigma_D,S/V). On a genuine maximal affine piece I write h_I(z)=A+Bz, D0=A+Bmu>0, and

    P3=int_I h^3,
    Pz1=int_I h^2(z-mu),
    Pz2=int_I h(z-mu)^2.

For a whole base edge e, its actual centred moments are T_e and c_e, and

    alpha_F T_F=(alpha_D D0/V) [[P3 T_e,Pz1 c_e],[Pz1 c_e^T,Pz2]].

Set H=N4-D0P3, C=D0Pz1, R=(9/4)S-D0Pz2. The accepted planar bounds alpha_D T_e<=(3/2)Sigma_D and alpha_D<=2/3 show

    V[(3/2)Sigma-alpha_F T_F]
      >= alpha_D [[H T_e,-C c_e],[-C c_e^T,R]].

Because T_e>=c_e c_e^T, the scalar conditions H>=0,R>=0,HR-C^2>=0 suffice. For an actual whole edge T_e is positive definite: its line does not pass through the interior area centroid. Therefore H>0 and HR-C^2>0 give a positive-definite full 3D gap by the Schur complement. The generally nonzero mixed block is retained throughout.

## 3. Complete three-piece normalization and two sufficient charts
For three genuine pieces with both end heights zero, affine changes of z and height normalize the middle piece to endpoints (0,1) and (1,q). Write

    h(z)=(z+a)/a,                 -a<=z<=0;
    h(z)=1+(q-1)z,                 0<=z<=1;
    h(z)=q[1-(z-1)/b],             1<=z<=1+b.

Here a,b>0, q>0, and concavity is EXACTLY

    b/(b+1) <= q <= (a+1)/a.

Equality at the upper bound merges left/middle facets; equality at the lower bound merges middle/right facets. Those equalities are genuine changes of the maximal-facet lattice, not three separate coplanar faces.

The complete outer-left chart is

    q=[ab+x(a+b+1)]/[a(b+1)],  a,b>0, 0<=x<=1.

It covers the entire concavity interval. Reflection z->1-z and height rescaling by 1/q send parameters to (b,a,1/q), so the same outer-left proof covers the right outer piece.

For the middle piece reflection permits q<=1. Its complete falling-middle chart is

    q=(b+x)/(b+1),  a,b>0, 0<=x<=1.

The rising-middle case is its reflected/rescaled counterpart. No restriction to equal tail lengths, balanced heights, a symmetric base or a prescribed centre is imposed.

The actual bulk moments are

    V=(a+bq^2+q^2+q+1)/3,
    M=(-a^2+b^2q^2+4bq^2+3q^2+2q+1)/12,
    E=(a^3+b^3q^2+5b^2q^2+10bq^2+6q^2+3q+1)/30,
    N4=(a+bq^4+q^4+q^3+q^2+q+1)/5.

For either selected piece let Pij=int_I z^j h^i, and Dn=A V+B M=V D0. The exact expressions checked by the source are

    Hn=V N4-Dn P30=V H,
    Cn=Dn(V P21-M P20)=V^2 C,
    Rn=(9/4)V^2(VE-M^2)-Dn(V^2 P12-2VM P11+M^2 P10)=V^3 R,
    Detn=Hn Rn-Cn^2=V^4(HR-C^2).

The source constructs all Pij by exact polynomial integration. Every cleared original denominator is a polynomial with strictly positive coefficients in positive a,b,q. In each chart it then clears the positive q-denominator to its full q-degree and expands in nonnegative powers a^i b^j and the Bernstein basis in x on [0,1]. Every coefficient is nonnegative. This is a finite GLOBAL sign proof, not a grid, floating optimization or independent-moment relaxation.

The six certificates have these exact control counts (zeros in parentheses):

    outer H:422(189); outer R:1386(540); outer determinant:5663(2415);
    middle H:97(2); middle R:405(0); middle determinant:1414(2).

Total 9387 controls:3148 zero,6239 strictly positive,NONE negative. Strict endpoint witnesses are also recorded for each polynomial: at least one positive x=0 Bernstein control and one positive x=1 control multiply positive a,b monomials. Nonnegative controls imply strict positivity for every interior x as well. Consequently H,R and HR-C^2 are strictly positive over the entire selected-piece chart. The proof of whole genuine facets now follows from Section2 and reflection. At a slope equality use the earlier WHOLE merged two-piece theorem; the strict three-piece conclusion is not silently transported through that merger.

A sharp family has square base [-1,1]^2, a=b=1/n, q=1, n>0. Its genuine middle facet x=1 and test (1,0,0) have exact quotient

    alpha_F v^T T_F v/(v^T Sigma v)=15n/(10n+4) -> 3/2.

Each finite member has two actual apices and two square rings, hence true V/E/F=10/20/12. The limiting prism is not counted as the same incidence.

## 4. An elementary moment-quotient theorem for arbitrary concave tails
Normalize the maximum height to 1 and let I be the entire maximum plateau. For 0<t<1 let L(t) be the length of {z:h(z)>=t} minus |I|. Concavity of h makes its superlevel sets intervals, and their Minkowski interpolation inclusion shows L(t) is concave. Also L>=0 and L(1)=0. Therefore w(t)=L(t)/(1-t) is nondecreasing: for t1<t2<1, concavity against the endpoint 1 gives L(t2)>=(1-t2)L(t1)/(1-t1).

For any exponent p>0 the tail moment is

    Mp=int_{outside I} h^p = p int_0^1 t^(p-1)(1-t)w(t)dt.

For q>p, use the probability density p(p+1)t^(p-1)(1-t) and the monotonicity of BOTH w and t^(q-p). Chebyshev's covariance identity gives

    Mq >= [(p+1)/(q+1)] Mp.                  (TAIL)

For completeness, the difference is q/[p(p+1)] times Cov(w,t^(q-p)); the covariance equals one half of the double integral of [w(t)-w(s)][t^(q-p)-s^(q-p)], which is nonnegative. This also handles limiting endpoint slopes by integrability. No differentiability, finite-piece assumption or localization theorem is used. In particular

    int_out h^2 <= (5/3) int_out h^4.

Linear tails from height1 to zero attain this quotient; unequal tail lengths are allowed. The plateau itself must be removed before using this equality description. With no tails both sides are zero.

## 5. The plateau mixed inequality, including actual recentering
Let Z=z-mu, normalize plateau height1 and put

    Sin=int_I Z^2, Sout=int_out Z^2 h^2,
    Vout=int_out h^2, H=int_out h^4,
    C=int_I Z=-int_out Z h^2.

The last identity is the ACTUAL centre relation int Z h^2=0. If any tail is present, H>0 and Sin>0. Weighted Cauchy and (TAIL) give

    C^2 <= Vout Sout <= (5/3) H Sout.

Thus an even stronger scalar gate than the general sufficient 9/4 gate holds:

    H[(5/3)(Sin+Sout)-Sin]-C^2 >= (2/3)H Sin >0.

For the original R=(9/4)(Sin+Sout)-Sin the explicit lower bound is

    HR-C^2 >= H[(5/4)Sin+(7/12)Sout] >0.

Here D0=1 and P3=|I|, so H=N4-|I| is exactly the scalar H in Section2, not an independently chosen tail moment. The full actual plateau-facet gap is positive definite. This proves Theorem B for ALL concave tails. It does not control a different sloping affine piece of the same profile.

## 6. Actual controls, boundary mergers, and evidence level
The standalone source checks five true rational polytopes by independent oriented-boundary volume integration, all maximal support facets, all true edges, the actual volume centroid/covariance, all whole-facet full 3/2 gaps by every principal minor, pole identities and the own Euclidean physical edge packets:

    square flat top (a,b,q)=(2,3,1):10/20/12, own S8 U10 H16, weak000;
    asymmetric pentagon falling middle (2,1,3/4):12/25/15, own S12 U8 H18, weak000;
    asymmetric triangle rising middle (1,2,3/2):8/15/9, own S6 U5 H9, weak000;
    square left merge (2,1,3/2):6/12/8, own S8 U6 H12, weak000;
    square right merge (1,2,2/3):6/12/8, own S8 U6 H12, weak000.

The raw bases are square(-1,-1),(1,-1),(1,1),(-1,1); pentagon(0,0),(3,0),(4,1),(2,3),(-1,2); triangle(0,0),(3,0),(1,2). Each is translated by its ACTUAL area centroid. The two merger controls delete their redundant rings before constructing maximal faces. Integration fan diagonals are never added to physical edges. The census is only for these native Euclidean controls, not transferred through general affine images.

A separate actual curved-body control uses the same centred asymmetric pentagon and

    h(z)=1-z^2/4 on[-2,0], h=1 on[0,1],
    h(z)=sqrt(1-(z-1)^2/9) on[1,4].

It is globally concave, with derivative0 at both plateau joins, strictly concave tails and zero endpoint heights. Its only 2D flat boundary pieces are the five WHOLE plateau rectangles. It is NOT a polytope, so no finite V/E/F or equilibrium census is assigned. Exact profile moments are V=61/15,M=49/12,E=773/70,N4=215/63 and actual axial centroid mu=245/244, strictly OUTSIDE the plateau. Consequently the mixed moment C=-123/244 is nonzero. All five full actual facet gaps are positive definite. The tail quotient is483/380<5/3; S=711497/102480, H=152/63, Sin=60271/178608, Sout=1720493/260470. The original determinant gate is14422530359/393830640 and its proved lower bound is290143661/28130760, both positive. Every full matrix and facet vertex is emitted exactly.

Normal and fresh source-only executions BOTH completed with byte-identical reports and logs. An initial source transcription missed one closing parenthesis and failed before execution; the final literal source in part2 fixes that syntax error. No mathematical assertion failed. These are analytical proofs plus exact rational global polynomial certificates, not proof-assistant formalization or independent re-verification of the accepted uniform-planar theorem.

## 7. Complete recovery identities
Part2 contains the complete source, with LF and one final newline:

    homothetic_three_piece_and_plateau.py,14574B,
    SHA256 11e7ec2681f37702b5829eee2e492e9d476d2f982d08485211a9f78170747293.

CPython3.13.5, SymPy1.14.0, assertions enabled. No external input, helper, seed or precision parameter. Reconstruction and verification command:

    python -B homothetic_three_piece_and_plateau.py > three_plateau.log

Outputs:

    homothetic_three_piece_and_plateau_report.json,1232934B,
    SHA256 c0ac4ee26585930711ba638cbb7452ecb694d0022a899bd6a8416af863957df8;
    three_plateau.log,589B,
    SHA256 505ee0822ba9fd5c2a16488a9257fbceef5cd23e800304e115ed862e511e62dc.

First marker: EXACT_THREE_PIECE_ZERO_END_ALL_FACETS_PASS 6 9387 3148.
Curved marker: ACTUAL_ASYMMETRIC_CURVED_PLATEAU_FIVE_WHOLE_FACETS_PD_PASS 245/244.
Final marker: THREE_PIECE_AND_ARBITRARY_CONCAVE_PLATEAU_EXACT_RECOVERY_PASS.
The report contains every polynomial monomial, rational Bernstein control, strictness witness, exact actual coordinate, moment matrix, true incidence and physical control primitive. The deterministic literal generator is the smallest exact representation, not an omitted coefficient table.
