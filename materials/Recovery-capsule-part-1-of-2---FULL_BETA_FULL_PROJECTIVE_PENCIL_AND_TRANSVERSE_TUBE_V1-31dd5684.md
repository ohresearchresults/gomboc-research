# material-31dd56843fc2

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL_CUT_STACK_FULL_BETA_FULL_PROJECTIVE_PENCIL_V1

## 1. New theorem and scope

The whole base parameter is now free. Fix

    p=(1/5,2/5,3/5), q=(1/4,1/3,1/2),
    u=(1/5,2/5,2/5), s=4/5.

For EVERY beta in(0,1), EVERY a in(-5/4,3), and EVERY physical positive definite metric, the actual uniformly filled cut-stack body defined below has at least two strict unstable vertices. No weak-free assumption and no spectral conditioning bound is imposed. In fact every complete true rooted weak-arrow tree is impossible for every nonzero positive semidefinite matrix. The latter is an algebraic separation statement, not an interpretation of degenerate metrics as ordinary physical equilibria.

This is an entire two-parameter open rectangle containing every regular ghost section a=0,1 and the two valid outer sectors. It is not a sample, a fixed-beta pencil or a small beta neighborhood. The actual normalized centroid is recalculated from uniform volume for every parameter.

There is also an explicit eleven-dimensional tube: let

    theta=(p0,p1,p2,q0,q1,q2,u0,u1,s), u2=1-u0-u1,
    ||theta-theta0||_infinity <= 2^(-83).

For every such theta, every beta in(0,1), and every t in(0,1), set

    a_theta(t)=-(1-t)/s+t(1+1/q2).

The corresponding actual body has U>=2 for every SPD metric. Thus BOTH entire beta and each parameter's ENTIRE maximal projective pencil are retained, with nine independent small transverse parameters. This is still not the whole eleven-parameter incidence or a whole E17 exclusion. No incidence is subtracted, no new own110 attainer is supplied, and34<=C_min<=622 is unchanged.

The earlier fixed-beta theorem remains useful separately: at beta=2/5 its normalized margin is2^-26 and its transverse radius2^-68 is much larger. The present complete rectangle has the more conservative common margin2^-40. Do not silently replace the old local quantitative statement with the new weaker margin or claim either tube is the full chart.

## 2. Complete exact dependencies and evidence level

The new TWO-PART capsule consists of this proof/manifest and the exact source

    [internal-source-reference]
    Recovery capsule part 2 of 2 - beta_certificate.py.txt
    9954bytes
    SHA256 ffe60695e60c78dd2a0bc5109f0e76a6b4168f26ea39a79e546f39644c10b832.

Its explicit source dependency is the previously executed pencil_certificate.py, recovered from BOTH earlier materials:

    [internal-source-reference]
    Recovery capsule part 1 of 2 - FULL_CUT_STACK_COMPLETE_PENCIL_AND_ELEVEN_PARAMETER_TUBE_V1.md
    19098bytes
    SHA256 96c76b074bac68e86741d85c4d463c59216650bb00ae0737c9eb8bb3973d0950

    [internal-source-reference]
    Recovery capsule part 2 of 2 - pencil_certificate.py.txt
    16434bytes
    SHA256 b36cdea35fb1834d680e4459c3c8163c69a9ca27d96ae422cfe14b18ec7eed1b.

The earlier Part1 supplies a COMPLETE exact recovery program correcting one transported variable name in the earlier Part2. It produces

    pencil_certificate.py,16437bytes
    SHA256 b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1.

This exact corrected source hash is enforced by the new source. The unpatched16434-byte input is not executable authority. All FOUR materials, not just the new two, are required for a descendant computation. No full76 Figure package, older numeric table or sandbox checkpoint is involved.

The coordinator executed a source-only build in a directory initially containing only the corrected parent source and the new source, then a separate exact verify invocation. Both passed. The earlier exploratory cached tensor run is not the reproducibility basis; its full stress choices were reproduced by the source-only build. The proof combines exact integer/rational finite checks with the analytical geometry and perturbation estimates below. This is not a proof-assistant formalization.

The underlying full eleven-parameter realization theorem is [internal-source-reference], fully read, with complete sources [internal-source-reference] and [internal-source-reference]. The present four-material recovery capsule repeats every actual vertex, edge and moment input used by its executable; it has no code/checkpoint dependency on those older sources. The realization theorem, not a parameter count, is the justification that the stated open parameter domain has the literal true facets.

## 3. Actual geometry and positive-cell centroid

Use labels0..9=B0,B1,B2,L0,L1,L2,R0,R1,R2,S. Put

    B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1),
    d_i=1+a p_i, e_i=1+(1-a)q_i, d_s=1+a s,
    L_i=(-p_i,B_i,y,B_i,z)/d_i,
    R_i=(q_i,B_i,y,B_i,z)/e_i,
    S=(-s,u1-beta(1-u2),u2)/d_s.

Here B_i,y and B_i,z mean the y and z coordinates of B_i; L_i and R_i each have three coordinates. The convex hull has exactly the following true maximal cycles on the open domain:

    (0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
    (1,4,5,2), (1,2,8,7),
    (3,9,4), (3,5,9), (4,9,5), (6,7,8).

The17 true edges, in the exact source order, are

    (0,2),(0,3),(0,6),(1,2),(1,4),(1,7),(2,5),(2,8),
    (3,4),(3,5),(3,9),(4,5),(4,9),(5,9),(6,7),(6,8),(7,8).

Each has two arrows, forward then reverse. No integration diagonal is included.

Seven positive actual tetrahedra partition the uniformly filled body:

    (0,1,2,5),(0,1,4,5),(0,3,4,5),(3,4,5,9),
    (0,1,2,8),(0,1,7,8),(0,6,7,8).

Their positive six-volumes are

    w=(p2/d2, p1/(d1 d2), p0/prod(d),
       (s-u.p)/(d_s prod(d)), q2/e2, q1/(e1 e2), q0/prod(e)).

These are actual geometric volumes, independent of beta. The actual centroid is

    g_raw=[sum_k w_k sum_{i in tet_k} V_i]/[4 sum_k w_k].

The maximum left coefficient is s=4/5, the maximum right coefficient is q2=1/2, and s-u.p=9/25. Thus the full positive-denominator interval is exactly -5/4<a<3 for every beta. The normalized endpoints below are limits, not finite physical members of that open interval.

## 4. Why freeing beta remains low degree: a genuine shear mechanism

There is a useful geometric identity valid throughout the full chart. For fixed a,p,q,u,s, replacing beta by beta+delta maps the raw body by

    Phi_delta(x,y,z)=(x, y+delta[-1+z-a x+max(x,0)], z).

Each of its restrictions to x<=0 and x>=0 is affine with determinant1. It preserves those halfspaces, and each of the seven actual tetrahedra lies in one of them. The map therefore transports the actual uniform volume exactly, not just the listed vertices. This proves directly that volume is beta-independent and the actual centroid is affine in beta:

    g_delta=(g_x, g_y+delta[-1+g_z-a g_x+E_P max(x,0)], g_z).

The positive-part expectation is an actual volume expectation, not an assigned vertex mass. Convexity of the image is guaranteed on the permitted beta interval by the true realization chart. This lemma by itself does not imply any equilibrium invariance: the map is not globally affine.

For the numerical certificate use the affine normalization

    q=q2, y_s=u1-beta(1-u2), K=s+q u2,
    T_a,beta(x,y,z)=(d_s(qz-x)/K, e2(sz+u2 x)/K,
                    y-y_s(qz-x)/K).

It has positive determinant d_s e2/K and fixes S=(1,0,0), R2=(0,1,0). Let Z_i(a) and g(a) be its actual vertices and centroid at beta0=2/5. For the fixed data K=1. The entire beta dependence is

    Z_i(a,beta)=Z_i(a)+(beta-2/5) lambda_i(a) e3,
    g(a,beta)=g(a)+(beta-2/5) ell(a) e3,

where

    lambda=(-1,-1,3/10,
            -22/(5a+25),-19/(10a+25),33/(30a+50),
            23/(5a-25),18/(5a-20),0,0),
    ell=[sum_k w_k sum_{i in tet_k} lambda_i]/[4 sum_k w_k].

The common affine-normalization determinant cancels in the volume-weighted centroid. This is the exact uniform-cell formula used by the source; no vertex-average surrogate appears.

Every normalized vertex has a common nonvanishing linear denominator in a and is affine in beta. It therefore lies in the convex hull of its four endpoint values at a=-5/4,3 and beta=0,1. Exact corner norms have maximum

    16097/625 < 36,

attained at a=3,beta=1,label R0. Thus every normalized vertex has norm<6 on the complete closed rectangle. The old fixed-beta radius5 is NOT valid here:16097/625>25. An early source guard incorrectly carried that smaller radius into the enlarged domain, failed before any accepted output, and was corrected. The current source, proof, refill radius and pins all use radius6.

The normalized six-volume remains beta-independent:

    N(a)=12a^5-7a^4-80a^3+1975a^2+22400a+40500,
    D(a)=N(a)/[5(a-5)(a-4)(a+5)(2a+5)(3a+5)] > 1/16.

The exact degree17 Bernstein lower bound N>=2008125/128 and positive denominator upper bound202125 are inherited algebraic identities recomputed by the source. Actual volume therefore remains nonzero through the closed normalized rectangle, even though boundary labels can become redundant.

## 5. Tensor Bernstein certificate on the complete rectangle

Write U_i=Z_i-g, E_ij=Z_j-Z_i and

    H_ij(a,beta)=sym[(Z_i(a,beta)-g(a,beta))
                    (Z_j(a,beta)-Z_i(a,beta))^T].

Use the strictly positive scalar

    Q(a)=20000(a-5)^2(a-4)^2(a+5)^2(2a+5)^2(3a+5)^2 N(a).

Set R=Q H at beta0. With du=lambda_i-ell and dv=lambda_j-lambda_i, the coefficients of b=beta-2/5 are

    R1=Q[du sym(e3 E_ij^T)+dv sym(U_i e3^T)],
    R2=Q du dv e3 e3^T,
    Q H(a,beta)=R+b R1+b^2 R2.

All entries of R,R1,R2 are rational-coefficient polynomials in a of degree at most17. The degree2 Bernstein coefficients on beta in[0,1] are exactly

    R-(2/5)R1+(4/25)R2,
    R+(1/10)R1-(6/25)R2,
    R+(3/5)R1+(9/25)R2.

After a=-5/4+(17/4)t, the degree(17,2) tensor Bernstein coefficients have common integer scale537407782912. There are54 coefficient matrices for each arrow. The source recomputes every one from the literal actual-cell formulas, not from a fit to sampled bodies.

The graph has4641 undirected spanning trees and46410 distinct rooted trees. The complete certificate has31 rectangular nodes,16 terminal rectangles, maximum subdivision depth5, and27442 positive-integer stresses with supports of size3..9. Subdivision alternates beta first, then t. Exact de Casteljau subdivision contributes a factor2^2 or2^17 to the integer scale, which the verifier tracks explicitly. Every leaf has zero remaining rooted systems.

For EACH tree and EACH parameter, some retained stress supported on arrows of that tree satisfies

    -sum w_ij H_ij/(sum w_ij) >= Gamma I,
    Gamma=2^-40.

The finite proof checks all1481868 exact symmetric3x3 tensor coefficient matrices after subtracting

    Gamma (sum w_ij) scale * [506018631541267125/14] I.

The bracket is the exact maximum degree17 Bernstein coefficient of Q, hence an upper bound for Q on the rectangle. All three leading Sylvester minors are strictly positive by integer/rational arithmetic. Bernstein convexity then proves the matrix inequality on each whole cell. Coverage is checked by exact arrow bit masks and a full recursive partition, not by testing grid points.

The coefficient-discovery LP and its eigenvector cuts are only locators for integer weights. Their success flag is not used as mathematical acceptance. There were27457 discovery requests; the15 requests that caused further subdivision were not physical feasible packets. The successful source-only run reproduced the whole rectangle, not merely the exploratory subset. Different floating libraries could choose different valid stresses; every output still must pass the exact checker.

Pair the positive stress with any nonzero PSD matrix M. Simultaneously weak forward inequalities tr(MH_ij)>=0 would contradict the positive matrix trace. For SPD, a weak forward arrow strictly increases the squared own-centred norm, so a unique strict unstable vertex would induce a spanning in-arborescence toward it. The complete rooted-tree exclusion therefore gives U>=2. All nonsingular affine images with uniform refilling are included through the arbitrary SPD metric, without choosing an independent polar metric.

## 6. Explicit same-incidence refill collar

Put eta=2^-68. Consider any normalized convex body with the SAME literal cycles and seven positive actual tetrahedra as a triangulation, with every labelled vertex displaced by at most eta from a member of the closed normalized reference rectangle. Its centroid must be recomputed from actual uniform volume.

Old radius R=6 bounds all edge vectors by12. Determinant multilinearity bounds one tetrahedron's six-volume change by

    24 R^2 eta+24 R eta^2+8 eta^3.

Summing all seven and using eta<=1 bounds the total by7112 eta. Since old D>1/16, new D>1/32. Each tetrahedral centroid moves by at most eta, and its old distance from the old body centroid is at most12. Thus

    ||Delta g|| <= [1+12*7112*32] eta
                =2731009 eta <2^22 eta.

The centred-vertex displacement is less than2^23 eta and edge displacement at most2 eta. Consequently

    ||Delta H_ij|| <[12*2^23+24+2^24 eta] eta
                  <2^27 eta=Gamma/2.

Any nonnegative normalized stress retains at least Gamma/2=2^-41. The collar therefore proves the same all-nonzero-PSD rooted-system exclusion and all-SPD U2. This is a quantitative actual-refill result; suppressing Delta g would not establish it.

## 7. Nine transverse parameters, full beta and full moving pencils

Let delta=2^-83 and theta be as in Section1. Compare at the SAME beta and SAME t in the respective moving full pencils. For transparency, all following estimates hold on the much larger guard box delta<=1/100.

Then s in[.79,.81],q2 in[.49,.51],u2 in[.38,.42],u0 in[.19,.21],u1 in[.39,.41]. All parameters and weights stay positive. The stack excess is positive even by the coarse bound s-max p>=.79-.61>0. The maximum left coefficient remains s and the maximum right coefficient remains q2. Thus each whole interval a_theta(t) is admissible, and the exact true cycles persist for every open beta and t.

Uniformly for beta in[0,1],

    9/10<K<11/10, |y_s|<1/2,
    |a|<4, |1-a|<3, d_s<7/2, e2<11/5.

The normalized S and R2 are identically fixed, including by cancellation at the endpoints. For every other raw numerator (x0,y0,z0), its uncancelled denominator h is one of1,d0,d1,d2,e0,e1. It satisfies1/5<h<4. Indeed the extremal lower bounds are1-.61/.79 and1-(1/3+.01)/.49, both greater than1/5. Hence Kh>1/8.

Exact reciprocal comparison at the same t gives

    |Delta a|<5delta, |Delta d_s|<8delta, |Delta e2|<8delta,
    |Delta K|<3delta, |Delta y_s|<=3delta, |Delta h|<7delta.

For these noncancelled vertices set

    A=q2 z0-x0, B=s z0+u2 x0,
    Z=(d_s A,e2 B,K y0-y_s A)/(K h).

Here |A|,|B|<2, |Delta A|<=2delta, |Delta B|<4delta, and |y0|<=1. The three numerator changes are less than24delta,25delta,11delta respectively. The third bound is still valid for the ENTIRE beta interval: it is at most3delta+6delta+delta, because |y_s|<1/2. The numerator norm is less than16, its change norm less than60delta, and the denominator change less than20delta. Both old and new denominators exceed1/8. Therefore

    ||Delta Z|| <[60*8+16*20*64]delta
                 =20960delta<2^15delta=eta.

Apply the actual-refill collar of Section6. This proves the full-beta, full-moving-pencil, nine-transverse-parameter theorem without reducing to fixed a endpoints, fixing the centroid artificially, or confusing the closed normalized limits with genuine open-domain E17 bodies.

## 8. Reconstruction commands, observed files and terminal markers

Environment used for the observed source-only build and separate exact verify:

    CPython3.13.5, SymPy1.14.0, NumPy2.3.5, SciPy1.17.0,
    OPENBLAS_NUM_THREADS=1, assertions enabled.

The scripts force the thread variable before NumPy import. There is no randomness, input checkpoint or symbolic cache dependency. Obtain the exact two parent materials, run the literal recover_pencil.py program in their Part1, and save the exact new Part2 as beta_certificate.py. The directory then needs only

    pencil_certificate.py,16437bytes,
    SHA b1e887ff04f59652ee400a9988d813ea63a5cc71859755d38086c0f6ca74f7b1;
    beta_certificate.py,9954bytes,
    SHA ffe60695e60c78dd2a0bc5109f0e76a6b4168f26ea39a79e546f39644c10b832.

Run

    OPENBLAS_NUM_THREADS=1 python -B beta_certificate.py build
    OPENBLAS_NUM_THREADS=1 python -B beta_certificate.py verify
    sha256sum pencil_certificate.py beta_certificate.py beta_stresses.json beta_verification.json

The source-only build derives all tensor coefficients and all tree masks before numerical discovery; verify rederives them but does NOT call a numerical optimizer. The final acceptance operations are exact.

Observed reconstructed outputs:

    beta_stresses.json,2076189bytes,
    SHA256 57df0ea7b43dd95475993667a927369038295538a548e7a588a7ed908e43eb5e;
    beta_verification.json,681bytes,
    SHA256 00d250988c0dbf9ab8bc6b60eb4dc039a4e9e1131af7a55c2e11d449813cc7c1.

Expected terminal marker from BOTH modes:

    FULL_BETA_FULL_PROJECTIVE_PENCIL_GAMMA_TUBE_EXACT_PASS

Expected report values include rooted_trees46410,nodes31,leaves16,integer_stresses27442,coefficient_matrix_checks1481868,degrees[17,2],scale537407782912,gamma1/1099511627776. Every terminal rectangle has zero uncovered trees. A failed assertion, uncovered leaf or mere LP result is not a completed proof.

The2MB stress JSON is reproducibly generated from the two small complete sources and their literal inputs. It is not claimed to be separately stored as a native material, and its hash does not replace its generator. The exact four-material dependency package suffices without the originating sandbox.

## 9. Scientific interpretation and next frontier

The decisive extension is not another thin local box: all beta values and all a values of the fixed projective class are now covered, with an explicit uniform physical margin. The true piecewise-affine shear explains why actual volume remains independent of beta and why the moment/arrow tensor stays quadratic in it. The revised radius6 and recomputed actual-centroid perturbation are essential to the transverse tube.

This does not exhaust the nine remaining shape parameters. In particular, freely varying the stack barycentric weights can reach genuine facet-merging boundaries where a vertex need not disappear; those cannot automatically invoke a nine-vertex refinement theorem. A broad stack-weight domain or a structural constraint across such boundaries would address a harder missing part of full-incidence coverage. No U1 survivor, new census, whole-type subtraction, Figure improvement or minimum equality follows from the current result. The canonical C622 construction and lower prohibition34 remain separate unchanged records.
