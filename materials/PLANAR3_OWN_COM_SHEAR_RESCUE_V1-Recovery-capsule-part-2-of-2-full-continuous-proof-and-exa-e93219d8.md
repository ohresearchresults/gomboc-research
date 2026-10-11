# material-e93219d8bbce

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# PLANAR3_OWN_COM_SHEAR_RESCUE_V1
## Recovery capsule part 2 of 2: full continuous theorem, exact body, failed controls and reconstruction

This is a new regularization theorem for an entire specified planar cyclic three-contact sector, not a minimum proof, not a class110 construction, and not an exclusion of10/17/9. The actual control below has V/E/F=8/18/12 and strict S/U/H=9/5/12. The bracket34<=C_min<=622, all root censuses and all FULL/LOCAL counts remain unchanged. Universal regularization for arbitrary three-contact positions or mixed vertex-edge/edge-facet types is not proved here.

Part1, immutable material [internal-source-reference], is the COMPLETE runnable source planar3_own_com.py. Part2 gives the geometric proof independently of a successful transport or hash. No originating sandbox, external checkpoint, numerical seed or omitted helper is a dependency of the recovery.

## 1. Geometry and statement

Let P be a full-dimensional convex3polytope of constant volume density, with its TRUE volume centroid at0. Initially use physical orthonormal Euclidean coordinates. A simple vertex-edge contact means that the radial supporting plane at a vertex z exposes exactly one genuine edge [z,z+u], with z.u=0; all other support guards at that physical point are strict. It is one physical weak point, although a feature census may label both its vertex and edge. An edge-facet contact and a vertex-facet packet are different types and are NOT silently included.

Write

z0=(1,0,0), z1=(-1/2,sqrt(3)/2,0), z2=(-1/2,-sqrt(3)/2,0),
d_i=(-z_i,2,z_i,1,0), u_i=h_i d_i, h_i>0.

Thus d_i is the same 90-degree rotation of z_i in the contact plane Pi={x3=0}. The expression for d_i means its coordinates are (-second coordinate of z_i, first coordinate of z_i,0), not a four-coordinate vector.

THEOREM. Suppose the three [z_i,z_i+u_i] are genuine exposed edges of P, and its only weak physical equilibria are these three simple vertex-edge contacts. Then arbitrarily small actual affine/projective deformations, always recentered at the actual new uniform-volume centroid, remove all three weak contacts, preserve the full face lattice, and preserve every original strict equilibrium and its type. The deformation can be chosen as an optional small affine shear fixing Pi pointwise, followed by one projective map, actual centroid subtraction, and one affine map. Orthogonal similarities and a common positive scaling of the stated sector are also allowed.

This covers EVERY actual P with those hypotheses and arbitrary other vertices/facets, not only the explicit8-vertex body below. The preliminary shear is needed in the proof only for a specified covariance exception. No assertion that an arbitrary three-contact configuration can be transformed into this equilateral sector is made.

## 2. True-centroid differentiation and the stress barrier

Let Sigma=E_P[xx^T]>0, L=5Sigma. For T_t(x)=x/(1+t p.x), choose t sufficiently small so every denominator is positive throughout P. The projective image is filled uniformly, rather than assigned the transported original density. Since the Jacobian is (1+t p.x)^(-4), its actual centroid is

g(t)=E_P[x(1+t p.x)^(-5)]/E_P[(1+t p.x)^(-4)].

It is analytic near0 and g'(0)=-5Sigma p=-Lp. Recenter by this very g(t). For an edge with z.u=0, let z(t)=T_t(z)-g(t), u(t)=T_t(z+u)-T_t(z). Put a=p.z, b=p.u and l=Lp. Then

z'(0)=l-a z,
u'(0)=-(a+b)u-bz.

With S(a,b)=(ab^T+ba^T)/2 and T_i=S(z_i,u_i), the derivative D_i of S(z_i(t),u_i(t)) is

D_i=S(l,u_i)-(p.(2z_i+u_i))T_i-(p.u_i)z_i z_i^T.

Hence trD_i=u_i.(L-|z_i|^2 I)p. For the present sector the matrices T_i/h_i=S(z_i,d_i) span exactly the two-dimensional space W of planar trace-zero symmetric matrices, and

sum_i T_i/h_i=0,
sum_i d_i=0,
sum_i |z_i|^2 d_i=0.

The positive relation alpha_i=1/h_i is unique. Every first own-centroid projective-affine contact jet has zero alpha-weighted sum. Also sum_i z_i^T M u_i/h_i=0 for EVERY symmetric M: affine-only escape cannot make all three contact functions positive. This latter identity even survives an arbitrary common translation of the reference point because sum_i u_i/h_i=0. In particular it is not repaired by pretending the centroid is a freely chosen reference.

The weighted tensor derivative D=sum_i D_i/h_i belongs to W for every p and every actual Sigma. To see this, the only possible off-plane contribution is S(l,sum_i d_i)=0, all remaining terms are planar, and their total trace is0. Therefore the earlier sufficient test that D should leave W does not apply. This is the consequential distinction from CYCLIC3_OWN_COM_SECOND_ORDER_V1, whose nonplanar diagonal stress is repaired by D outside W. The planar case is resolved below by a different second-order coefficient.

## 3. Full second-order identity, including arbitrary edge lengths

Let p1,p2 be the planar components of p and l1,l2 the planar components of Lp. Set the planar block of the first affine metric coefficient to

H_Pi=((h+2l1-2p1,-l2+p2),(-l2+p2,h)),

where h is an arbitrary real scalar. Its off-plane coefficients may be arbitrary. The scalar h in H_Pi is unrelated to the three positive edge lengths h_i. With M(t)=I+tH, direct substitution gives every first contact coefficient trD_i+H:T_i=0.

We derive the full weighted second coefficient, rather than treating numerical cancellation as a proof. Suppress the index i, put v=p.d so b=h_i v, and denote l_z=l.z, l_d=l.d. Write

g(t)=-t l+t^2 g2+O(t^3),
z(t)=z+t(l-a z)+t^2(a^2 z-g2)+O(t^3),
u(t)=u-t[(a+b)u+bz]+t^2[(a+b)^2u+(2ab+b^2)z]+O(t^3).

For phi_i(t)=z_i(t)^T(I+tH)u_i(t), its normalized second coefficient is

[t^2]phi_i/h_i = -g2.d_i + l.Hd_i + a_i l_di - v_i l_zi + a_i v_i - v_i z_i.Hz_i.        (1)

To check (1), before eliminating h_i its purely geometric terms are -(a_i+h_i v_i)l_di-v_i l_zi+3a_i v_i+h_i v_i^2, and its H-term is l.Hd_i-(2a_i+h_i v_i)z_i.Hd_i-v_i z_i.Hz_i. The first-order identity z_i.Hd_i=v_i-l_di cancels ALL h_i-dependent terms and yields (1). Thus arbitrary genuine edge lengths, not merely equal ones, are covered. The common actual g2 term disappears in the weighted sum because sum_i d_i=0; it has not been replaced by a free center.

Let J be the planar90-degree rotation. The equilateral identities sum_i z_i z_i^T=(3/2)I_Pi and d_i=Jz_i give

sum_i(a_i l_di-v_i l_zi)=3(p1 l2-p2 l1),
sum_i a_i v_i=0,
sum_i l.Hd_i=0.

Direct evaluation at the three displayed z_i gives

sum_i v_i z_i.Hz_i=(3/4)p2(H11-H22)+(3/2)p1 H12
                 =-(3/2)(p1 l2-p2 l1).

Therefore the normalized weighted second contact coefficient is exactly

beta(p):=sum_i [t^2]phi_i/h_i = (9/2)[p1(Lp)2-p2(Lp)1].                   (2)

All possible off-plane H terms cancel in this weighted sum because the weighted D is planar. Equation(2) is also independently expanded symbolically in the complete exact source for arbitrary h1,h2,h3, p1,p2,l1,l2,h.

The quadratic form Q_L(p)=p1(Lp)2-p2(Lp)1 has symmetric matrix

A_L=((L12,(L22-L11)/2,L23/2),
     ((L22-L11)/2,-L12,-L13/2),
     (L23/2,-L13/2,0)).

It has trace0. It is nonzero unless L11=L22,L12=L13=L23=0. A nonzero real symmetric trace-zero matrix has a positive eigenvalue: otherwise all its eigenvalues would be nonpositive with zero sum, hence zero, contradicting nonzero. Consequently, outside that exception some p has beta(p)>0.

The linear map R:Sym(3)->R^3, R(J)_i=J:T_i, has rank2 and image alpha-perp, alpha_i=1/h_i. Let c_i=[t^2]phi_i and A=sum_i alpha_i. Since beta=sum_i alpha_i c_i>0, choose J2 with

R(J2)_i=beta/A-c_i.

The compatibility condition is exactly that its alpha-weighted sum is zero. Thus the one common metric M(t)=I+tH+t^2J2 has

z_i(t)^T M(t)u_i(t)=(beta/A)t^2+O(t^3)>0

for all i and small positive t. M(t) stays SPD. Its positive-diagonal upper-triangular Cholesky factor B(t), B(t)^T B(t)=M(t), is an actual Euclidean affine map, applied AFTER true projective centering. A linear map preserves a uniform body's zero actual centroid. For a simple vertex-edge contact, positive z^T M u removes the local weak vertex/edge pair without producing a new strict pair: squared distance along the edge has positive first derivative at the endpoint, and all other normal-cone guards are strict. All remaining strict or inactive physical features retain their open sign guards. Hence all original strict equilibria are retained and no new weak ones appear.

## 4. Removing the axial covariance exception without moving the contacts

The exceptional case A_L=0 is exactly

Sigma=diag(sigma,sigma,tau), sigma,tau>0

in the displayed physical frame. Then the weighted first and second coefficients above vanish; this is NOT an all-orders obstruction.

Before the projective deformation, apply an arbitrarily small actual linear shear

S_epsilon=((1,0,epsilon),(0,1,0),(0,0,1)), epsilon!=0.

It fixes every point of Pi pointwise, so all six contact-edge endpoints, their orthogonality relations and stress tensors remain unchanged. Its image has the same face lattice. Since at each of the three simple contacts every other radial support inequality is strict, sufficiently small epsilon retains those inequalities. The finitely many other strict or inactive physical guards likewise remain open. Thus the new body still has exactly these same three simple weak points and all original strict equilibria. Its actual volume centroid stays0.

The actual covariance changes by the true affine law:

Sigma_epsilon=S_epsilon Sigma S_epsilon^T
=((sigma+epsilon^2 tau,0,epsilon tau),(0,sigma,0),(epsilon tau,0,tau)).

Its off-plane covariance entry epsilon tau is nonzero, so A_(5Sigma_epsilon) is nonzero and the preceding second-order construction applies. Given any neighborhood of the initial polytope, first choose epsilon sufficiently small, then choose the projective/metric parameter sufficiently small. Their composition is inside that neighborhood and has removed all contacts. This is a two-stage small-deformation proof; it does not assert that a single direct second-order jet at the original axial body has positive stress. It completes the theorem for the entire stated equilateral planar three-only sector.

## 5. A genuine exactly reconstructible own-centered control

A rational chart is convenient. Physical Euclidean coordinates are obtained by B0=diag(1,sqrt(3),1), so the initial chart metric is M0=B0^T B0=diag(1,3,1). The eight chart vertices are

v0=(1,0,0), v1=(1,1/3,0),
v2=(-1/2,1/2,0), v3=(-1,1/3,0),
v4=(-1/2,-1/2,0), v5=(0,-2/3,0),
v6=(1/5,1/10,2), v7=(-1/5,-1/10,-2).

The physical contact points B0*v0,B0*v2,B0*v4 are exactly the equilateral z_i above; their physical edge lengths are h_i=sqrt(3)/3. The equatorial hexagon has area centroid0 and the two apices are antipodal, hence its uniform bipyramid centroid is0. Exact positive tetrahedral integration independently proves chart volume2, physical volume2sqrt(3), and true COM0.

Its genuine f-vector is8/18/12. Exhaustive rational support enumeration recovers these maximal facet index sets:

(0,1,6),(0,1,7),(0,5,6),(0,5,7),(1,2,6),(1,2,7),
(2,3,6),(2,3,7),(3,4,6),(3,4,7),(4,5,6),(4,5,7).

Their orientations, exact poles and all genuine edges are deterministically reconstructed, not assumed from a picture. The true chart covariance is

Sigma_chart=((103/750,1/500,1/25),
             (1/500,409/9000,1/50),
             (1/25,1/50,2/5)).

The physical covariance is B0 Sigma_chart B0^T, in particular its12entry is sqrt(3)/500, not1/500. The chart and physical tensors are not conflated in the calculation.

The full exact initial census is:
strict stable facets [1,2,3,4,5,6,8,9,11];
strict unstable vertices [1,3,5,6,7];
strict saddle edges [0,5],[0,7],[1,2],[1,6],[1,7],[2,6],[3,4],[3,6],[3,7],[4,7],[5,6],[5,7].

Thus S/U/H=9/5/12. The only weak physical points are vertices0,2,4 on edges01,23,45. Every radial support plane there exposes exactly its two edge endpoints, proving simple vertex-edge contact rather than a vertex-facet packet. There are exactly three zero primitives among all72; there are no weak facets and no extra edge-interior weak points. Although C=36, this is NOT a110-body and NOT a10/17/9 body.

For each true edge ab with incident chart poles q,r, the four primitives are a^T M(b-a), b^T M(a-b), q^T N(r-q), r^T N(q-r), with N exactly M^-1. All four negative mean a strict saddle; all nonpositive with a zero mean a weak edge point; a positive primitive excludes an edge equilibrium. Vertex and facet checks use their complete respective incident lists. Part1 computes every primitive and its exact census; no triangulation diagonal is treated as a mechanical edge.

## 6. A literal arc and complete interval certificate

Take chart p=e1. Apply Y_i(t)=v_i/(1+t v_i,1); integrate the actual transformed uniform polytope to obtain g(t), and set X_i=Y_i-g(t). Its true chart centroid expansion satisfies

g'(0)=-5Sigma_chart e1, [t^2]g(t)=(1/8,7/48,0).

The exact true recentered poles are q_i(t)=(q_i+t e1)/(1-(q_i+t e1).g(t)); there is no independent polar recentering. Use

M(t)=M0+tH1+t^2H2,
H1=((-47/75,-3/100,0),(-3/100,0,0),(0,0,0)),
H2=((-16181/9000,4731/10000,0),(4731/10000,0,0),(0,0,0)),
N(t)=M(t)^(-1).

With H2 omitted, all first contact coefficients vanish and the three second coefficients in index order are

-1427/10000, 48899/90000, -16003/45000,

whose sum is9/200. With the displayed H2, every phi_i(t)/t^2 tends3/200>0 at0. This is consistent with the normalized physical beta=(9/2)(5sqrt(3)/500)=9sqrt(3)/200, since alpha_i=1/h_i=sqrt(3).

More than a formal jet is proved. On the ENTIRE closed interval0<=t<=1/1024 the source certifies, by exact positive rational Bernstein coefficients, every projective denominator, every leading principal minor of M(t), every true-centroid facet denominator, every originally nonzero primitive with its original sign, and all three canceled rational functions phi_i(t)/t^2. A positive rational polynomial certificate applies separately to numerator and denominator after sign normalization. Hence for EVERY0<t<=1/1024, all69 originally nonzero primitives retain their signs, the remaining three are positive, and the strict census stays9/5/12 with weak000.

For completeness, if P(t)=sum_(j=0)^m a_j t^j and e=1/1024, its Bernstein coefficients on[0,e] are

b_k=sum_(j=0)^k a_j e^j binom(k,j)/binom(m,j),0<=k<=m.

All b_k in each asserted guard are exact positive rationals. Nonnegative Bernstein basis functions sum to1, so this is a whole-interval proof, not sampled positivity. The deterministic report stores all power coefficients, degrees and smallest Bernstein coefficients. The endpoint is additionally checked by a new complete rational hull enumeration, exact centroid integration, unchanged maximal facet/edge identity, full equilibrium census and the exact Cholesky identity.

Physical Euclidean vertices throughout are B(t)X_i(t), where B(t) is the unique upper-triangular positive-diagonal Cholesky factor of M(t). This fixes all square-root choices. In particular B(0)=B0. Their true centroid is0 and actual Euclidean volume is det(B(t))*Vol_chart(t). Exact algebraic physical endpoint coordinates are in the recovered report.

## 7. Meaningful failed controls, preserved rather than silently relabeled

Two different initially proposed apex choices do not satisfy the three-only hypotheses. Both use the same six chart base vertices and M0.

(1) Apices plus/minus(0,0,2): actual chart volume2, COM0, physical covariance diag(2/15,2/15,2/5), strict S/U/H=6/5/9. It has NINE physical weak points: three vertex-edge points plus six edge-facet points. Weak facets are[0,1,6,7,10,11]. Thus it is not a three-only realization of the axial covariance exception and not a counterexample to the theorem.

(2) Apices plus/minus(1/5,0,2): actual chart volume2, COM0, strict S/U/H=8/5/11. It has FIVE physical weak points: the same three vertex-edge points and two distinct edge-facet points. Weak facets are[0,1]. Tilting only one horizontal component did not remove all extra degeneracies.

The accepted apices plus/minus(1/5,1/10,2) give a DIFFERENT body. Its full physical census establishes exactly three weak points. All three bodies, every coordinate, full maximal facet cycles, true covariance and complete primitive censuses are contained in the source/report. The failure of the first two designs is not discarded merely because their strict counts do not improve a record.

## 8. Durable recovery manifest

Part1 is material [internal-source-reference]. Save its entire text unchanged as planar3_own_com.py, UTF-8/LF with final LF. It is15022bytes, SHA2564ef1fe90e4d9b5c1f3be9c7468fc7f93d3884b147b9443826744cfe31f6447e2. This is the only computational recovery input; all exact vertices, metric coefficients, general symbolic identities, two failed controls and epsilon endpoint are in it. Part2 is the continuous proof and recovery protocol, not an additional missing data file.

Reference environment: CPython3.13.5, SymPy1.14.0, assertions enabled, no other dependencies. Never use-O. From a directory containing only this source, reconstruct with

python planar3_own_com.py build > build_stdout.txt

and verify by exact recomputation and byte comparison with

python planar3_own_com.py check > check_stdout.txt

Expected planar3_own_com.json:184239bytes, SHA256668f508a9de55a6d595fc138c0ec5749eff98409bad29667010ce1c736b81ce9.

Expected build_stdout.txt and check_stdout.txt: each479bytes, SHA256ab778a16de8b184b4fe0bcac9480b59a269255d24a7e02dc9c3a2ce2214c0d7f. Their entire text is:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

PLANAR3_OWN_COM_SHEAR_RESCUE_RECOVERY_PASS

A cold replay was performed from only the final exact source in a fresh directory; both build and check ran and every reproduced byte count/hash above matched. The report includes full initial/endpoint geometry and metrics, true centroid functions, general symbolic tensor identities, all interval certificates and both failed physical controls. Hashes identify these bytes but do not replace the complete source or the geometric proof.

## 9. Relationship to prior accepted sources and remaining frontiers

CYCLIC3_OWN_COM_SECOND_ORDER_V1 is the earlier NONPLANAR sector, with complete parts [internal-source-reference] and [internal-source-reference]. Its unique-positive-stress sufficient lemma uses trD!=0 or D outside W. The present planar result explicitly resolves a case where neither condition holds, using the actual covariance second jet and a contact-plane-fixing shear. It does not alter the earlier exact body, its strict5/4/7 census, or its symmetric-six-contact negative control.

The broader accepted two-contact result remains literal assignment minimum-0076, SHA256bb5b0d967434487f3ef8fb86e4712d48c753bc31e44a89fb37e791e96bb86a79, read0throughEOF in this coordinator context. The proof in this capsule is self-contained and does not require rerunning that parent's code. It does not promote the two-contact theorem into a universal three-contact theorem.

Unresolved: arbitrary three simple vertex-edge contacts with non-equilateral stress geometry; mixed primal/dual contacts where the common inverse metric introduces extra second-order terms; multiple independent positive stresses; vertex-facet packets with alternatives; and application to an actual weak110 candidate. No such candidate or new attaining example is claimed. The lower bound34 and upper construction622 remain separate, nonmatching sides of the original minimum problem.
