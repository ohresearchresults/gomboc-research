# material-32ffcd2feafe

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ARBITRARY_CONCAVE_PROFILE_TANGENTIAL_DEFECT_MONOTONICITY_THEOREM_V1

## The new continuum theorem

Let h be continuous, nonnegative and concave on a finite interval J, and positive in its interior. Let I be any nonempty affine subinterval of positive length, with h=L=A+Bz there. Define all unmarked integrals over J:

V=int h^2, M=int z h^2, mu=M/V, N4=int h^4,
P3=int_I h^3, D0=L(mu), H=N4-D0 P3.

Then H>=0. Equality is possible exactly when I=J and h is constant, apart from changes on endpoints of measure zero. Thus every proper whole sloping side interval has H>0, for ANY number of pieces or curved concave tails. No three-piece localization is assumed.

There is a stronger monotonicity statement for the volume-cleared defect

F[h]=V H=(int h^2)(int h^4)-P3 int L h^2.

Replacing either tail outside I by its affine endpoint chord can only decrease F, strictly if that tail was not affine. The interval, marked line and endpoint values are retained. The actual uniform-volume centroid is recomputed throughout: D0 V=int L h^2 is an identity for that moving centroid. This is not a fixed-centre completion theorem and does not contradict the earlier curved fixed-centre mixed-defect countercontrol [internal-source-reference].

The proof below is elementary and independent of the previously accepted three-piece Bernstein package. That package remains needed for the complete mixed matrix inequality, which is NOT proved here.

## A weighted concavity lemma

Let g>=0 be continuous and concave on[0,1], with g(0)=0. Put k=1-t and u=k+r t for r>=0. Then

int g u^3 >= (3/10) int g u,
int g^2 u^2 >= (1/10) int g^2.

These constants also work for the endpoint-zero bulges needed below. To prove them, v(t)=g(t)/t is nonnegative and nonincreasing. For any positive reference density w and any nonincreasing nonnegative functions v,phi,

(int w v phi)(int w) >= (int w v)(int w phi).

This follows by expanding the nonnegative double integral of w(s)w(t)(v(s)-v(t))(phi(s)-phi(t). Approximation handles an infinite initial slope; every integral in the claimed inequalities is finite.

Apply this fact first with w=t(1-t), phi=(1-t)^2, and then with w=t^2 and the same phi. The exact reference ratios are

[int t(1-t)^3]/[int t(1-t)]=3/10,
[int t^2(1-t)^2]/[int t^2]=1/10.

Consequently int g k^3 >=3 int g k/10 and int t g k^2 >=int t g/10. Expanding

u^3-(3/10)u = k^3-(3/10)k
 +3r t[k^2-1/10]+3r^2 t^2 k+r^3 t^3

proves the first lemma (the symbol u, not a new profile, is intended on the left). For the second, use u>=k, and use the same monotone-ratio comparison with reference w=t^2 and density v^2. This gives int g^2 k^2 >=int g^2/10. The source checks the displayed polynomial identity with the variable u explicitly.

## Normalization and affine-tail baseline

Consider one tail, reflecting the height coordinate if necessary. Normalize the marked interval to[-1,0], its height at the tail contact to1, and its other height to q>=0. The marked line is L(z)=1+(1-q)z. Normalize the tail coordinate z=b t, with b>0. Its endpoint chord is u(t)=1-t+r t, r>=0. Set

Vm=(1+q+q^2)/3,
Nm=(1+q+q^2+q^3+q^4)/5,
P=(1+q+q^2+q^3)/4,
vr=(1+r+r^2)/3,
nr=(1+r+r^2+r^3+r^4)/5,
mr=(1+2r+3r^2)/12.

These are respectively the marked second/fourth/third moments and the normalized affine-tail second/fourth/height-weighted second moments. Let

Jq=Nm-P+(3/5)Vm.

If f(t)=q+(1-q)t on[0,1], then

Jq=int f^2(f^2-f+3/5)
   = (7/20)Vm + int f^2(f-1/2)^2 >=(7/20)Vm>0.

Also

P(1-q)=(1-q^4)/4 <=1/4,
nr-(3/5)vr=(r^3+r^4)/5 >=0,
(3/4)vr-mr=(2+r)/12 >=0,
nr>=1/5, vr>=1/3.

For just the marked interval plus this one affine tail, direct expansion gives

F=Vm Nm-P^2
 +b[Vm nr+vr(Nm-P)]
 +b^2[vr nr-P(1-q)mr].

The constant is nonnegative by Cauchy–Schwarz. The coefficient of b is at least vr Jq>0. The coefficient of b^2 is at least

vr nr-mr/4 >= vr(1/5-3/16)=vr/80>0.

No relation between q and r is needed for these inequalities. With two affine tails, the only additional cross term is Vleft Nright+Vright Nleft, which is nonnegative. The single-tail argument applies to the other side after reflection and positive scaling. Hence every affine-chord completion has F>=0, strictly if a tail has positive length. If both tails are absent, equality in Cauchy–Schwarz occurs exactly when the marked affine profile is constant.

A marked endpoint of zero height cannot have a positive-length tail beyond it under the assumed positivity in the interior of J. Thus normalization by its height is never needed on a nonempty zero-contact tail. Remaining endpoint cases also follow by continuity.

## Adding an arbitrary concave bulge

Now keep the other tail arbitrary and fixed. On the selected tail write the actual profile as u+g, where u is its endpoint chord and g>=0 is concave with g(0)=g(1)=0. Consider u+lambda g for lambda>=0. The proof does not need every lambda to be a globally concave profile: it proves a coefficient inequality. In particular it applies at lambda=1.

Let V0,N0 be the full second and fourth moments of the body with the chosen tail replaced by u. Define normalized tail integrals

a=int u g, b2=int g^2, c=int u^3 g, d=int u^2 g^2,
e=int u g^3, f4=int g^4.

The marked P remains fixed. The six nonconstant coefficients of F[u+lambda g], in ascending order, are

c1=2b a N0+4b c V0-2b P int [1+b(1-q)t]u g;
c2=b b2 N0+8b^2 a c+6b d V0-b P int [1+b(1-q)t]g^2;
c3=4b e V0+12b^2 a d+4b^2 b2 c;
c4=b f4 V0+8b^2 a e+6b^2 b2 d;
c5=2b^2 a f4+4b^2 b2 e;
c6=b^2 b2 f4.

The last four are visibly nonnegative. For the first two, discard the nonnegative contributions of the fixed opposite tail to V0 and N0, so V0>=Vm+b vr and N0>=Nm+b nr. The weighted lemma says c>=3a/10 and d>=b2/10. In addition int t u g<=a, int t g^2<=b2 and P(1-q)<=1/4. Therefore

c1 >= 2b a[Jq+b(nr+3vr/5-1/4)]
   >= 2b a[(7/20)Vm+3b/20] >=0,

c2 >= b b2[Jq+b(nr+3vr/5-1/4)] +8b^2 a c
   >= b b2[(7/20)Vm+3b/20]+8b^2 a c >=0.

The first is strictly positive when the continuous bulge is nonzero. Thus adding either arbitrary concave bulge increases F. Flatten the first and then the second tail. The affine-chord baseline already proved F>=0; the universal claim and equality case follow.

This is a continuum argument. It does not infer arbitrary-profile positivity from a finite number of knots, a numerical optimizer, or tensor Bernstein coefficients of a fixed-dimensional chart.

## Geometric meaning and remaining mixed problem

Let D be any actual centred planar convex body and P={(h(z)x,z):x in D,z in J}, uniformly filled. Its actual covariance is

Sigma_P=diag((N4/V)Sigma_D,S/V), S=int(z-mu)^2 h^2.

For a true planar base edge e, let beta=|e|dist(0,aff e)/Area(D), ce=average_e x and Te=average_e xx^T. The WHOLE lateral facet over the maximal affine interval I has, in horizontal directions,

(alpha_F T_F)_horizontal = (beta D0 P3/V) Te.

The accepted planar inequality beta Te<=3Sigma_D/2 and the new D0P3<=N4 give the sharp3/2 bound on every transverse quadratic direction for EVERY concave homothetic profile. No triangulation of the facet is used. A common nonsingular affine map transports the quadratic statement by congruence; this does not preserve a Euclidean equilibrium census.

For mixed horizontal/axial directions, the sufficient profile gate still requires

R=9S/4-D0 Pz2>=0,
H R-D0^2 Pz1^2>=0,
Pz1=int_I h^2(z-mu), Pz2=int_I h(z-mu)^2.

Only H>=0 is universally closed here. The full gate remains open on arbitrary sloping intervals, while all at-most-three-piece profiles, arbitrary maximum-plateau facets, and arbitrary endcaps retain their earlier full3/2 proofs. The new tangential proof does not replace the actual mixed-centre term or prove universal3D3/2, U>=2, an E17 incidence exclusion, C>=36, or an attaining110 body. The accepted bracket stays34<=C_min<=622.

## Exact negative control for a tempting stronger bound

There is NO universal positive constant c with H>=c D0^2 Vout for all such sloping intervals. This is refuted by genuine concave two-piece profiles

h(z)=1 on[0,1],
h(z)=(1+epsilon-z)/epsilon on[1,1+epsilon], epsilon>0,

marking the second, sloping interval. They are actual homothetic bodies, and for polygonal D are genuine convex polytopes. Their complete recovery is in the source, not a relaxed moment tuple. One obtains

mu=(epsilon^2+4epsilon+6)/(4(epsilon+3)),
D0=3(epsilon^2+4epsilon+2)/(4epsilon(epsilon+3)),
H=(epsilon^2+68epsilon+210)/(80(epsilon+3)),
Vout=1,
H/(D0^2 Vout)=epsilon^2(epsilon+3)(epsilon^2+68epsilon+210)/[45(epsilon^2+4epsilon+2)^2].

The last ratio is asymptotic to(7/2)epsilon^2 and tends to0. H,R and the mixed determinant all have strictly positive polynomial numerators and positive denominators for epsilon>0, checked symbolically in the source. This refutes only the proposed uniform tail-mass estimate, not3/2. It explains why the plateau Cauchy bound cannot simply be reused with D0^2 Vout for a steep short facet.

## Exact actual controls and reproducibility

The complete standalone source is recovery part2 [internal-source-reference]. Save its exact UTF-8 text as profile_tangential.py. It has no auxiliary code/data input or random seed. All formulas, profiles, base vertices and parameters are literal. Assertions must remain enabled.

The base is the pentagon with raw vertices(0,0),(3,0),(4,1),(2,3),(-1,2), translated by its actual area centroid. The source derives the actual polygon area, covariance and each whole-edge mean/second moment. It reconstructs every whole lateral-facet tensor, pole and actual facet centroid and checks T_F q_F=c_F. It checks all principal minors of the complete3/2 matrix on the controls; those finite checks are not the universal mixed theorem.

An actual curved profile on[-1,2] has left h=1+z/3-z^2/4 on[-1,0], marked h=1+z/3 on[0,1], right h=1+z/3-(z-1)^2/2 on[1,2]. Endpoint heights are positive and slopes match concavely. The source computes the actual centroids and defects before straightening, after straightening only the right tail and after both. The three volume-cleared defects strictly decrease and stay positive. Curved profiles are not assigned a finite polytope census.

It also reconstructs all25 genuine whole side-facet moment tensors of the existing five-piece pentagon-base polytope: knots0,1/5,2/5,3/5,4/5,1; heights1,7/5,17/10,9/5,8/5,1. Its unchanged full hull and physical census are already in the endcap capsule [internal-source-reference] plus [internal-source-reference]:30/55/27, strict244, weak0, not class110. The present source regenerates the actual side moments, not a new mechanical census. A whole prism control has H=0 as required.

Normal and fresh SOURCE-ONLY executions were observed with byte-identical report and stdout. Environment CPython3.13.5,SymPy1.14.0. Command:

    python -B -u profile_tangential.py > profile_tangential.log

Exact input:
profile_tangential.py 9120 bytes
SHA256 49738e9e414f89e55bf0327a0f71e69f6634675ee9388b8fb688b93f174d0ed4

Reproduced outputs:
profile_tangential_report.json 105520 bytes
SHA256 1c6054fce91004a74152f34447bb5c48f64064dce1c406d7cc87b940dd769696
profile_tangential.log 322 bytes
SHA256 c4a82db26af74b2d324b876b2015b6bb2cdae869f78f7b71e968b9332326f94c

Observed terminal markers:
MONOTONE_RATIO_BETA_INTEGRALS_AND_ALL_VARIATION_COEFFICIENTS_PASS
ARBITRARY_CONCAVE_TAIL_STRAIGHTENING_TANGENTIAL_DEFECT_PASS
ACTUAL_CURVED_TAIL_AND_25_FIVE_PIECE_WHOLE_SIDE_TENSORS_PASS
REPORT 105520 1c6054fce91004a74152f34447bb5c48f64064dce1c406d7cc87b940dd769696
PROFILE_TANGENTIAL_DEFECT_COMPLETE_SOURCE_RECOVERY_PASS

The source/report before the exact tail-mass counterfamily was added had7980-byte source SHA d63d66012ac3eba4cbaf26a6b5f3fe2bed161487c914b2c00db91c7b2a171d5b and104511-byte report SHA b45a2a32efe76189dfc72fc998458ea0ac77636cbc8626209ca40b54446c42f1. The complete9120-byte source above supersedes that local draft and preserves its entire proof/control content plus the exact negative family. No old sandbox is needed.
