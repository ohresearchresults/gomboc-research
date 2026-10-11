# material-6cc82ec50840

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# DEPTH_INCIDENCE_AND_DEG6_CAP300_V1

## Result, scope, and relation to the newer structural obstruction

This capsule preserves three exact analytic improvements and one meaningful negative application result. They concern one actual uniformly dense convex three-dimensional polyhedron at its own volume centroid, one positive definite vertex metric M, and the inverse pole metric N=M^{-1}. No polar-centroid transfer, free first-moment completion, or independently chosen Gram matrix is allowed.

A. If the weak primal and dual rooted trees have heights Hp,Hq, the condition number in the actual covariance gauge obeys

kappa <= 81 f(Hp+1) f(Hq+1),   f(n)=cos^(2n)(pi/(2n)).

B. On (V,E,F)=(10,17,9), kappa<48. Any vertex/pole product Gamma=(v^T Mv)(q^T Nq) is <432. For an incident pair v.q=1 it is <8000067/19600<40817/100<409. The tree-height version gives Gamma<301 whenever Hp<=3, or Hp<=4 and Hq<=6, on this layer.

C. For an actual two-apex base B and outside U-root x of degree6, an AVAILABLE genuine cyclic chain B->q0->q1->q2->q3->q4->q5 whose missing closing edge is xz, together with the genuine weak arrow z->x, forces Gamma(x,q5)>301. The body assumptions and the rank-order input are specified below. This is a continuous conditional lemma, not a whole E17 exclusion.

D. The exact native ROOF8_3_5 census contains24 selected full xz chains with U9 of degree6. Their selected primal heights are7,8,9, so the shallow-depth consequence of A--C excludes NONE of these24 when only those selected heights are used. That failure does not prove feasible geometry. Subsequently TWO_APEX_ROOT_LEAF_OBSTRUCTION_V1 excluded ALL24 by a stronger rank-child argument, without a depth hypothesis. Thus none of these24 remains an open selected xz case. The analytic available-chain lemma C remains a wider and different assertion, because arbitrary available chains need not extend to a complementary pair.

The exact minimum is not proved here. Accepted bounds remain34<=C_min<=622. No new uniform110 construction is promoted. The preserved local six-pole cone is explicitly NOT a bounded body.

## Exact sources

Both literal parents were fully read cursor0 through EOF before use:

* minimum-0086, SHA8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10, TWO_APEX_FACET_CLOSING_512_V1. It contains the actual covariance/finite-depth geometric argument and its distinct degree4/6 ROOF8_3_5 source.
* minimum-0087, SHAb77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5, H0_GLOBAL_NERVE129_AND_WEAK_PACKETS_V1. It supplies the true-feature reciprocal-metric conventions and positive/weak complementary-tree distinction.

The fully read material [internal-source-reference], SHAaf169f4ded154478fff382b79d1beaa91071ef51b625dec2db222b0e470c48ab, contains the actual two-apex rank theorem and its rational K/200 certificate. The mandatory covariance correction [internal-source-reference], SHA0ef4abceed94299c2ffd0501d0b1c5c39607955f59bcfb6f9747caf66ab69572, is incorporated, not merely listed.

The sole external analytic input is Berwald's inequality in the primary author paper: Dylan Langharst and Eli Putterman, Weighted Berwald's Inequality, arXiv:2210.04438v7,27February2024, equation(1), https://arxiv.org/html/2210.04438v7 . The current primary HTML was read in this coordinator segment. For a nonnegative concave f on a three-dimensional convex body, t_f(p)=(binom(3+p,p) E f^p)^(1/p) is decreasing. The p=1,q=2 specialization used here is16(Ef)^2>=10E(f^2). We do not claim this classical inequality as a new discovery or pretend the finite script formalizes it.

## 1. Actual isotropic geometry, with the corrected averaging step

Let Sigma be the actual uniform-volume covariance, positive definite for a full-dimensional body. The affine map Sigma^{-1/2} makes it I and preserves the genuine centroid0. In this gauge

sqrt(5/3) B_2 subset P subset sqrt(15) B_2.       (1.1)

For the outer bound choose an actual vertex and a unit axis e through it, with projection b>0. Decompose P into actual tetrahedra with that vertex as apex. If the other projections are z1,z2,z3 and s=z1+z2+z3, actual centroid0 gives E_cells s=-b with the true normalized tetrahedral volumes. Exact simplex integration yields

20 E_P(e.X)^2 = E_cells[b^2+sum z_i^2+(b+s)^2]
 >= E_cells[2b^2+2bs+(4/3)s^2]
 = (4/3)E_cells s^2 >=(4/3)b^2.

The cancellation2b^2+2b E_cells s=0 occurs AFTER averaging. The corresponding summand can be negative in one tetrahedron and must not be discarded pointwise. Since the variance is1, b^2<=15. Every vertex satisfies this, hence the whole convex body does.

For an arbitrary unit e let h=max_P e.X and set f=h-e.X>=0. Then Ef=h and Ef^2=h^2+1. Berwald gives16h^2>=10(h^2+1), hence h^2>=5/3. This is the inner bound. Polarity at the SAME origin gives radii1/sqrt(15) andsqrt(3/5) for P*. Both bodies therefore have outer/inner radius ratio at most3. Uniformity of the polar is neither assumed nor needed.

In original coordinates the relevant SPD operator is A=Sigma^{1/2} M Sigma^{1/2}; the corresponding pole operator is exactly A^{-1}. The product Gamma itself is invariant under this change.

## 2. Height rather than vertex count in the crossing lemma

Let r B_2 subset conv(X) subset R B_2 and let A>0 have eigenvalues lambda1>=lambda2>=lambda3. Suppose a selected weak A-arrow tree on the actual points has one root and height H, where height is the maximum number of arrows to the root. Weak means y^T A(z-y)>=0. Then

lambda1/lambda2 <= (R/r)^2 f(H+1).              (2.1)

Choose a leading unit eigenvector e with sign making the root's e-projection nonnegative. Since the r-ball is in conv(X), some starting vertex has e-projection<=-r. Follow its tree path until the first arrow y->z crossing from a negative to a nonnegative e-projection. Let L be the number of arrows from the start through this crossing, so1<=L<=H. In transformed coordinates A^{1/2}y let phi be the angle to -e. It lies in(0,pi/2); phi=0 would make the crossing inequality impossible.

For any weak arrow the preceding norm is no greater than the next norm times the cosine of their mutual angle; distinct-point norm increases strictly, and all these mutual angles lie in[0,pi/2). The starting projection supplies sqrt(lambda1)r no greater than its norm times the cosine of its starting angle to -e. The spherical triangle inequality says that this starting angle and the L-1 preceding arrow angles sum to at least phi. By concavity and monotonicity of log cos,

sqrt(lambda1)r <= |A^{1/2}y| cos^L(phi/L).       (2.2)

On the crossing, the leading-axis contribution to y^T Az is nonpositive. The transverse transformed component of z has length<=sqrt(lambda2)R. Thus the weak arrow inequality gives

|A^{1/2}y| <=sqrt(lambda2)R sin(phi).            (2.3)

Combining gives a factor sin(phi)cos^L(phi/L). Its derivative in logarithmic form is cot(phi)-tan(phi/L); the unique maximum is at phi=L*pi/(2(L+1)), with value cos^(L+1)(pi/(2(L+1))). Therefore lambda1/lambda2<=(R/r)^2 f(L+1). The function f(n) increases for real n>=1: writing t=pi/(2n), the derivative of log f is2(log cos t+t tan t)>0, since this bracket has derivative t sec^2 t>0 and limit0 at t=0. This proves(2.1).

Zero primitive derivatives were not discarded. No complementarity between different trees is required for this analytic lemma. Any available rooted trees provide bounds using their own heights; replacing selected trees by other available ones is permitted only after those arrows are justified in the same geometry.

## 3. Joint metric bound and exact rational evaluation on E17

For unique U and S the true vertex graph and true pole graph have weak trees to their unique roots, since a nonroot has a weak outgoing edge and norms strictly increase. Apply(2.1) to P,A and P*,A^{-1}, using(1.1). If the heights are Hp,Hq,

lambda1(A)/lambda2(A)<=9 f(Hp+1),
lambda2(A)/lambda3(A)<=9 f(Hq+1),
kappa<=81 f(Hp+1)f(Hq+1).                     (3.1)

For E17 with V10,F9, Hp<=9,Hq<=8. The exact trigonometric upper value for9kappa is729 f(10)f(9), approximately431.96875137; the approximate decimal is not the rational proof. The source instead proves kappa<48 using a rational upper cosine polynomial and a rational lower bound on pi.

The rational pi bound is reconstructed from Machin's identity. Let alpha=atan(1/5), beta=atan(1/239). Exact angle addition gives tan(4alpha)=120/119 and tan(4alpha-beta)=1; the angles lie in the principal interval, so pi=16alpha-4beta. The alternating four-term lower sum for alpha and the one-term upper beta bound give

pi >16 sum_{j=0}^3 (-1)^j/((2j+1)5^(2j+1))-4/239 >333/106.

For n>=2, t=(333/106)/(2n), the exact fourth-order upper Taylor polynomial c_n=1-t^2/2+t^4/24 is positive and below1, and cos(pi/(2n))<c_n. Taylor's sixth-order remainder has the required negative sign on this interval. Therefore f(n)<c_n^(2n). The source checks with Fractions that81 c_10^20 c_9^18<48. For any vertex and pole, ||v||^2||q||^2<=9 in the covariance gauge, so Gamma<=9kappa<432. This strengthens the older convenient bound29160/59 without changing the existence problem by itself.

## 4. Incident-pair inequality

For any SPD A of condition kappa and nonzero u,w, write r=||u||||w|| and c=u.w. Then

sqrt((u^T Au)(w^T A^{-1}w))
 <= [(kappa+1)r+(kappa-1)sqrt(r^2-c^2)]/(2sqrt(kappa)).     (4.1)

To prove this, rescale A by a positive scalar, which leaves the product unchanged, so its spectrum is in[m,M]=[1/sqrt(kappa),sqrt(kappa)]. The scalar inequality t^{-1}<=m+M-t holds for t in[m,M], hence A^{-1}<=(m+M)I-A. For unit a=u/||u||, b=w/||w||, arithmetic-geometric mean gives

sqrt((a^T Aa)(b^T A^{-1}b))
 <=(a^T Aa+b^T A^{-1}b)/2
 <=[m+M+tr(A(aa^T-bb^T))]/2.

The nonzero eigenvalues of aa^T-bb^T are plus/minus sin(theta), where cos(theta)=c/r. Its positive and negative eigendirections give trace at most(M-m)sin(theta). Multiplying by r proves(4.1), including parallel vectors.

For a true incident pair, u=Sigma^{-1/2}v,w=Sigma^{1/2}q have c=1 and1<=r<=3. The right side increases in r and in kappa>=1. Thus

Gamma <=Psi(kappa)=[3(kappa+1)+sqrt(8)(kappa-1)]^2/(4kappa).

Since kappa<48 and sqrt(8)<99/35, exact rational arithmetic gives

Gamma < [147+(99/35)47]^2/192
 =8000067/19600 <40817/100<409.                 (4.2)

The complete source evaluates the corresponding rational upper bound for all72pairs Hp=1..9,Hq=1..8, retaining a directed-upward integer rounding to millionths and the exact Boolean test for301. It verifies that Gamma<301 when Hp<=3, and also when Hp<=4,Hq<=6. It does not assert this is the only possible set of heights giving a useful bound, nor that the constants are sharp.

## 5. Genuine two-apex rank-cap hypotheses

Assume one true maximal base facet B contains all vertices except the unique U-root x and z. Normalize physically x=e3. A positive true-volume fan gives B.(x+z)=-2-delta,delta>0, and the actual rank theorem gives a maximum base vertex b with b->x and b^2>|z|^2. Assume also a genuine weak arrow z->x, q0.x=q0.z=B.b=1, q0.b<=1, and B->q0. These assumptions make b,z belong to the closed ball with diameter[0,x]. They are real support and metric inequalities, not arbitrary five-vector data substituted for a body.

Set u=q0^2-1. The previously accepted exact positive definite K/200 Gram identity gives

u>1251/100+24|z|^2+(1459/100)delta.             (5.1)

The source reproduces the full five-by-five K, equality and inequality multipliers, all leading principal minors8692,11573255,16503151100,8831025280,5962527728, and the exact identity. The constant1351/100 is for q0^2-24z^2, while1251/100 is for u-24z^2. This is not a new proof claim about a changed parent object.

## 6. Six true incident poles and the five-arrow closing-line envelope

Let q_i=(t_i,1),i=0..5, be the six true poles incident at the strict U-root x, in cyclic order. Their tangent polygon contains0 strictly inside. Assume genuine weak arrows q0->q1->...->q5, and that the closing true edge between q0 and q5 has endpoints x,z. Let u=|t0|^2,a=|t5|^2 and h be the squared distance from0 to the line t0t5. The five positive successive radial angles alpha_i lie in(0,pi/2), and their sum T exceeds pi because the one remaining cyclic angle is smaller than pi. Log-cos concavity gives

u/a <= cos^10(T/5).                            (6.1)

We prove a>300 by contradiction. Suppose a<=300. By(5.1), u/a>1251/30000>1/32. If T>=3pi/2, then T/5>=3pi/10>pi/4, and(6.1) would give u/a<1/32. Hence pi<T<3pi/2 and t0.t5<0. Set w=(u/a)^(1/5); then1/2<w<cos^2(pi/5)=(3+sqrt5)/8<131/200 and T<=5 arccos sqrt(w). In particular the substituted upper angle is less than5pi/4<3pi/2, so both the actual and substituted angles lie in the monotonicity interval used next.

For s=sqrt(u/a)=w^(5/2), the distance to the closing line satisfies

h/a=s^2(1-cos^2 T)/(1+s^2-2s cos T).

The right side is strictly increasing in cos T when -1<cos T<0: its derivative has the sign of s cos^2 T-(1+s^2)cos T+s, which is positive there. Since cos is increasing on(pi,3pi/2), substitution of the upper T from(6.1) gives

h/a <= F5(w)=N(w)/D(w),
N(w)=w^5(16w^2-12w+1)^2,
D(w)=31w^4-9w^3+w^2+w+1.                      (6.2)

The source verifies the multiple-angle algebra exactly using cos(5theta)=cos(theta)(16cos^4(theta)-20cos^2(theta)+5). The denominator is positive: D=1+w+w^2(31w^2-9w+1), and124(31w^2-9w+1)=(62w-9)^2+43.

The actual line xz, with x=e3 and q0.z=q5.z=1, gives

|z|^2>=1/(1+h).                                (6.3)

For example, if t=x.z and sigma^2=|z|^2, h=(1-t)^2/(sigma^2-t^2) and
sigma^2-1/(1+h)=((1+h)t-1)^2/[h(1+h)]>=0.
The denominator is positive for a genuine distinct closing endpoint. This identity alone does not imply z->x; that weak arrow was assumed separately in section5.

By(5.1),(6.2),(6.3) and a<=300,

a w^5 >1251/100+24/(1+h)
 >=1251/100+24/(1+300F5(w)),
a w^5 <=300w^5.

This is impossible if

P(w)=(1251-30000w^5)(D+300N)+2400D>0.           (6.4)

The exact degree14 polynomial, in descending powers, is

-2304000000w^14+3456000000w^13-1584000000w^12+216000000w^11
-9000000w^10+95146800w^9-143845200w^8+66022800w^7
-9037200w^6+345300w^5+113181w^4-32859w^3+3651w^2+3651w+3651.

The source supplies a full positive Bernstein certificate on the four CLOSED rational intervals
[0,131/400], [131/400,393/800], [393/800,917/1600], [917/1600,131/200].
All15 coefficients on every interval are exact positive fractions, generated and checked from the full polynomial without omitted input; they are retained literally in the reproducible JSON. The intervals cover the whole required range, including all their boundaries. Positivity is not inferred from numerical samples. This proves a>300, hence q5^2=a+1>301.

## 7. Exact local cone control, not a polyhedron110

The rational recurrence t0=(1,0), t_{i+1}=(a-4b/3,4a/3+b) for t_i=(a,b),i=0..4, gives the full tangent list

(1,0), (1,4/3), (-7/9,8/3), (-13/3,44/27), (-527/81,-112/27), (-79/81,-3116/243).

The source verifies strictly convex cyclic order,0strictly inside, and all five arrow primitives equal0. It has u=1,a=9765625/59049,h=606841/621241,w=9/25, and equality h/a=F5(w). Thus the multiple-angle closing formula has a nontrivial exact common planar control. This is only a local six-pole tangent cone. It does not satisfy the physical rank-cap input u>12.51, does not supply a base/centroid, and is NOT a bounded uniform body or a110 counterexample.

## 8. Exact negative depth census and later supersession

The source fixes the literal ROOF8_3_5 maximal facet cycles

F0=(0,1,2,3,4,5,6,7),F1=(0,1,8),F2=(1,2,8),
F3=(3,4,9),F4=(4,5,9),F5=(5,6,9),F6=(6,7,9),
F7=(2,3,9,8),F8=(7,0,8,9).

It enumerates all17lexicographic true-edge choices of9primal edges. There are4053primal spanning trees, with complementary dual trees. For U9degree6, all stable roots0..8 and either full cycle order(7,3,4,5,6,8) or(8,6,5,4,3,7), the condition B0->first and all five successive dual arrows selects24pairs. The complete mask, both parent arrays, stable/unstable roots and chain are in the JSON. Their selected(Hp,Hq) histogram is
(7,7):6,(7,8):4,(8,6):2,(8,7):4,(8,8):2,(9,6):2,(9,7):2,(9,8):2.

None meets Hp<=3 or Hp<=4,Hq<=6, and the exact full table also fails the301 test for these heights. This is a real limit of applying the new product bound using THESE selected trees; it does not forbid shorter available alternative trees. More importantly, the subsequent root-leaf theorem proves that every such selected xz-chain is impossible outright: x has only the second apex as its selected child, contrary to the actual maximum-base rank order. All24are included in the now-durable root-leaf census, not an open frontier.

The stronger root-leaf capsule is [internal-source-reference] + [internal-source-reference] + mandatory correction [internal-source-reference]. That distinct source proves its own geometry and native counts. The old available-arrow degree6 conditional cap and the general metric/incidence lemmas are retained because selection is a stronger assumption, and because they may apply elsewhere.

## 9. Complete reconstruction and verification

Save part1 of this capsule as the literal UTF-8 file depth_incidence_cap300.py. It is the complete standalone standard-library source,10556bytes,SHA2564331e803cca0a2fe5f8d0f7a6adb76103afc0d8b6245a6f28a428773c7d7b8a0. Part2 is this proof. CPython3.13.5 was used, without external packages, with assertions enabled, no seed and no input file. All matrices, intervals, cone coordinates and facet cycles are in the source.

Reconstruction: `python -S depth_incidence_cap300.py build`.
Verification: `python -S depth_incidence_cap300.py check > depth_incidence_cap300_check.txt`.
The script refuses to overwrite an altered existing report. To reconstruct in a clean directory only the exact source is needed. Both commands were actually run successfully in this coordinator segment.

Expected JSON: depth_incidence_cap300.json,25417bytes,SHA25621008e4341a09609790da026e3de3284141b36349fa940798071da4c6603c9e3.
Expected check stdout: depth_incidence_cap300_check.txt,318bytes,SHA25669ddb1dac427d305e2e2991717397c0acb94d7de3eac1fcf9b9da9775aec09e1.
Terminal lines:
CENTROID_TREE_DEPTH_CONDITION_48_AND_INCIDENT_PRODUCT_409_PASS
DEG6_XZ_FIVE_ARROW_CHORD_AND_CAP300_EXACT_PASS
ROOF8_DEG6_24_SELECTED_CHAINS_SHALLOW_DEPTH_COVERAGE_ZERO_PASS
depth_incidence_cap300.json 25417 21008e4341a09609790da026e3de3284141b36349fa940798071da4c6603c9e3
DEPTH_INCIDENCE_AND_DEG6_CAP300_RECOVERY_PASS

A successful byte replay is not the continuous proof. Sections1--6 provide that proof, including the external Berwald input, the actual centroid hypotheses, incidence, metric reciprocity and every domain restriction. The source certifies the finite exact algebra and censuses. No new lower-endpoint or upper-endpoint claim follows from transport success alone.
