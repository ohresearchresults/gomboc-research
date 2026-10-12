# material-756fc0a948a4

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ARBITRARY_CONCAVE_HOMOTHETIC_ENDCAPS_SHARP_5_4_AND_FULL_3_2_V1

## New theorem and exact scope

Let D be any full-dimensional planar compact convex body, translated to its actual area centroid. Let h be continuous, nonnegative and concave on [a,b], positive in its interior. Uniformly fill the actual convex body P={(h(z)u,z):u in D,a<=z<=b}. The result includes arbitrarily many linear pieces and curved concave profiles; no finite-piece approximation is a premise.

Write V=integral h^2, M=integral z h^2, mu=M/V, S=integral (z-mu)^2 h^2, and N4=integral h^4. These are integrals over the whole interval. The actual covariance is Sigma_P=diag((N4/V)Sigma_D,S/V), and the actual centroid is (0,0,mu). For a true endpoint cap e in {a,b} with h_e=h(e)>0, let d=|e-mu|. In the conventions alpha_F=Area(F)dist(g,aff F)/Vol(P), T_F=average_F[(x-g)(x-g)^T], one has

alpha_e=d h_e^2/V,
T_e=diag(h_e^2 Sigma_D,d^2).

The NEW sharp tangential inequality is

    d h_e^4/N4 <= 5/4.

Equality holds exactly when h is affine from h_e at the marked endpoint to zero at the other endpoint: the body is a genuine pyramid. The accepted universal NORMAL inequality alpha_F <= (3/2) q_F^T Sigma_P q_F, where q_F.(x-g)=1 on the whole facet, is preserved in [internal-source-reference], SHA 2da1625674f6ba02f6d21c09a0d24c00228bd8f97fea7cdf541c8224f7f5b447. On this cap it gives d^3 h_e^2/S <=3/2. The mixed block vanishes at the actual centroid, not an assigned centre. Consequently EVERY whole endpoint cap of EVERY such concave homothetic profile satisfies

    alpha_e T_e <= (3/2) Sigma_P

in Loewner order. The full 3/2 is sharp, as shown by every prism in the normal direction. All conclusions transport under a common nonsingular affine map by covariance congruence; this is not an assertion of Euclidean equilibrium-census invariance under affine maps.

If an endpoint height is zero, there is no two-dimensional cap there; no fictitious facet is added. This theorem is about genuine whole caps, not integration triangles. Together with the earlier arbitrary maximum-height plateau theorem, it leaves genuinely sloping lateral facets as the open arbitrary-profile case. It does not prove the universal whole-facet 3/2 theorem, the complete E17 exclusion, C>=36, an attaining110 body, or the minimum. The accepted bracket remains 34<=C_min<=622.

## Elementary integral proof of the new sharp 5/4

By reflection and positive affine rescaling of height and the interval, take the marked cap at t=0, h(0)=1, interval [0,1]. Put k(t)=1-t and g=h-k. Concavity and h(1)>=0 give g>=0. Moreover v(t)=g(t)/t is nonnegative and nonincreasing on (0,1], because (h(t)-1)/t is a nonincreasing chord slope. The proof below in fact needs only this one-sided condition, not full concavity.

It suffices to prove

    F[h]=5 (integral h^2)(integral h^4)-4 integral t h^2 >=0.

All integrals in this proof are over [0,1]. Introduce

A=integral k g, B=integral g^2, C=integral k^3 g,
D2=integral k^2 g^2, E3=integral k g^3, G4=integral g^4,
F1=integral t k g, F2=integral t g^2.

The coefficients of F[k+lambda g] in ascending powers lambda^0,...,lambda^6 are exactly

0;
2A+(20/3)C-8F1;
B+10D2+40AC-4F2;
(20/3)E3+60A D2+20BC;
(5/3)G4+40A E3+30B D2;
10A G4+20B E3;
5B G4.

The final four are nonnegative. For the first two nonconstant coefficients set

w1(t)=2(1-t)[(10/3)(1-t)^2+1-4t],
w2(t)=11-24t+10t^2.

They are integral w1 g and integral w2 g^2+40AC, respectively. It is not valid to assume w1,w2 pointwise nonnegative. Their ordered integral kernels supply the missing positivity.

First suppose v is bounded. A nonnegative finite Stieltjes measure nu on (0,1], including the terminal constant as an atom at1, represents v(t)=integral 1_{t<=s} dnu(s) almost everywhere. Therefore

integral w1(t)g(t)dt = integral L(s)dnu(s),
L(s)=integral_0^s t w1(t)dt=s^2(1-s)^2(13-4s)/3 >=0.

For the quadratic term put

A0(s)=s^2/2-s^3/3,
C0(s)=s^2/2-s^3+3s^4/4-s^5/5,
W(s)=11s^3/3-6s^4+2s^5.

Then integral w2 g^2+40AC is the double integral of the symmetric kernel

K(s,t)=W(min(s,t))+20[A0(s)C0(t)+A0(t)C0(s)].

A0 and C0 are nonnegative and nondecreasing on [0,1], since their derivatives are s(1-s) and s(1-s)^3. For s<=t, K(s,t)>=K(s,s), and the exact diagonal identity is

K(s,s)=s^3(1-s)P(s)/3,
P(s)=11+23s-51s^2+34s^3-8s^4.

The degree-four Bernstein controls of P on [0,1] are

    11, 67/4, 14, 45/4, 9.

Every one is positive; hence K>=0. Thus every coefficient of F[k+lambda g] is nonnegative, proving F[h]>=0 at lambda=1.

For unbounded v, replace it by min(v,N). This remains nonnegative and nonincreasing; g_N=t min(v,N) is bounded by g and tends to g. The same coefficient argument applies, and dominated convergence passes every displayed integral and coefficient to the limit. No assertion that g_N itself is a concave perturbation is needed. This includes, for example, g(t)=sqrt(t).

If continuous g is not identically zero, E3=integral (1-t)g^3 is strictly positive. The cubic coefficient is then strictly positive, so F[h]>0. Equality therefore holds only at g=0, that is, h=1-t.

Undoing the normalization gives the exact inequality

4 h(a)^4 integral_a^b (z-a)h(z)^2 dz
 <=5 (integral_a^b h^2)(integral_a^b h^4).

Since mu-a=integral(z-a)h^2/V, this is precisely d h(a)^4/N4<=5/4. Reflection treats the other endpoint. This is a continuum analytical proof, not an inference from sampled or finitely many profiles.

## Exact actual controls and physical boundary

The source uses the raw planar pentagon (0,0),(3,0),(4,1),(2,3),(-1,2), centred at its actual polygon area centroid; its covariance is integrated exactly. The triangular integrations are moment calculations only.

It reconstructs a pyramid h=1-z and a prism h=1, on [0,1], attaining tangential5/4 and normal3/2 respectively. It also treats the genuine curved body h=sqrt(1+2z-z^2), not a polytope. For that body V=5/3, M=11/12, mu=11/20 and S=31/240. Both positive whole caps satisfy all matrix gap minors. No finite feature count or polytope census is assigned to the curved body.

A strict five-piece concave profile has knots (0,1/5,2/5,3/5,4/5,1) and heights (1,7/5,17/10,9/5,8/5,1). Its slopes are (2,3/2,1/2,-1,-3). The actual uniform polytope has 30 vertices,55 true edges,27 whole facets. All support planes and genuine edge incidences are checked, and the boundary fan independently reproduces the profile volume, centroid and covariance. Its native Euclidean census is strict(S,U,H)=(2,4,4), physical weak count0; it is not class110. Its numerical complexity2E=110 must not be confused with the class label110.

The complete physical closed-edge packet uses u=b-a, L=u.u, A=-a.u, R=L a+A u and B_i=R.(c_i-a), for one nonedge vertex c_i of each true incident facet. It is (A,L-A,-B_1,-B_2). All entries nonnegative mean an actual closed equilibrium; all strictly positive give a strict saddle; zero-containing admissible packets are deduplicated by their actual point R/L. The true vertices and facets give the strict U and S tests. No fan diagonal is used.

A nonorthogonal affine image uses matrix [[1,1/5,1/7],[0,1,1/6],[0,0,1]] and translation(2,-3,1). The source gives its complete transformed vertices, actual centroid/covariance, cap poles and moment tensors and all cap gap minors. It does not reuse the native Euclidean census for that image.

Further exact positive integral controls are h=1-z+z(1-z), h=1-z+sqrt(z), h=1-z+z(2-z), and the curved profile above. Their role is to illustrate the formula, not to establish the universal quantifier.

## Complete recovery and observed evidence

Recovery capsule part2 is [internal-source-reference]. It is the entire readable standalone source. Save its exact UTF-8 text as concave_profile_endcaps.py. It has no random seed, data inputs, external helpers, saved output dependency, or hidden parameters. All inputs are literal in that source. The analytical normal predecessor is needed for the general full3/2 corollary; the new tangential proof above is self-contained. The source checks the predecessor's conclusion only on the explicit controls and does not independently replay its universal proof.

Observed environment: CPython3.13.5, SymPy1.14.0, Linux. Assertions must remain enabled. Reconstruction and verification command, in a directory containing only the source:

    python -B -u concave_profile_endcaps.py > concave_profile_endcaps.log

The source checks all kernel polynomial identities, all five Bernstein controls, every perturbation coefficient, actual control moments, whole cap minors and the complete five-piece physical census, then emits the deterministic full report. A normal run and a source-only recovery run were observed. The exact archived11484-byte source was itself executed in a fresh source-only directory, and both report and stdout were byte-identical to the earlier normal/source-only runs. Its extra redundant Rational wrapper around Rational(45,4) is harmless; no recovery patch is needed or intended.

Exact recovery input:
concave_profile_endcaps.py 11484 bytes
SHA256 370224784bcb3064495168dd9b63e99383a2154a18499bfc49c94e3f3453cf4b

Exact reproduced outputs:
concave_profile_endcaps_report.json 39350 bytes
SHA256 2d51d69b7781397fb25a877426c24b46f1de48c6f11aa3bce52434309a19a88b
concave_profile_endcaps.log 297 bytes
SHA256 afe38f63cbb16e4a49f4f1e35bb97cb9b50f42f63412c1b10ab1b2053f4ec432

Observed final markers:
ONE_SIDED_CONCAVITY_LINEAR_AND_QUADRATIC_KERNELS_EXACT_PASS
ALL_ARBITRARY_CONCAVE_PROFILE_ENDCAPS_SHARP_TANGENT_5_4_PASS
ACTUAL_FIVE_PIECE (30, 55, 27) 2 4 4 weak 0
REPORT 39350 2d51d69b7781397fb25a877426c24b46f1de48c6f11aa3bce52434309a19a88b
ARBITRARY_CONCAVE_PROFILE_ENDCAPS_EXACT_RECOVERY_PASS

The first local draft used structural SymPy equality on differently factored but equal expressions; that assertion was replaced by exact subtraction/simplification before any accepted output. It was not a mathematical counterexample. The earlier11481-byte source SHA fcf355072e12bd8bcb3c23d7666b554cd31887587158bc872c6567aa882bc727 differs only by the redundant Rational wrapper and is not needed for recovery.

## Relation to the unresolved profile gate

For a genuine affine side interval I with h=A+Bz, retain D0=A+Bmu, P3=integral_I h^3, Pz1=integral_I h^2(z-mu), Pz2=integral_I h(z-mu)^2 and H=N4-D0 P3. The all-profile sufficient gate still asks H>=0 and

H[(9/4)S-D0 Pz2]-D0^2 Pz1^2>=0.

All at-most-three-piece profiles are already covered by [internal-source-reference] and its complete source [internal-source-reference]; arbitrary plateau facets are covered by [internal-source-reference] and [internal-source-reference]. The present theorem adds arbitrary endpoint caps, not this mixed sloping gate. The actual curved-completion negative control [internal-source-reference] still refutes naive same-centre affine-tail replacement. Its positive facet defect does not refute3/2. A potential continuation is an ordered curvature-kernel analysis retaining the moving actual centre; no such mixed-kernel theorem is asserted here.
