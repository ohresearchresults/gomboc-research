# material-844ae3e67f52

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# QUADRIVALENT_POLE_PATH_ANGULAR_CRITERION_V1

## Result and scope

This material proves a sharp LOCAL normal-cone obstruction at a strictly unstable vertex whose incident genuine facet poles are joined by a boundary path of weak pole arrows. For four incident facets it gives an explicit necessary and sufficient condition on the four tangential pole radii for realizing the entire local rooted-path shadow graph. A directed three-edge chain requires tangential radius growth strictly greater than 8; the constant 8 is the exact unattained infimum. A more general sharp directed-path bound is also proved analytically.

These statements apply to the genuine features and ONE reciprocal metric of any full-dimensional convex three-polyhedron with an interior reference. They do not require a volume-centroid assumption. Consequently they are valid necessary conditions for the homogeneous own-volume-centroid problem, but they do NOT prove that a local cone extends to a closed own-centered body, and they do NOT replace the global volume, incidence, moment or equilibrium conditions.

No additional whole labelled incidence/root position, whole combinatorial type, or global integer lower bound is excluded in this material. The accepted internal global bound remains C>=34. The canonical K2 register remains 278/550 excluded; the K3 register remains 11743 open labelled root positions, or 8739 rooted genuine facet/tree classes. In particular no C34 attainer, C>=36 theorem or exact minimum is asserted.

### Literal antecedents

The following mathematical sources were completely read in this coordinator turn:

* minimum-0078, SHA256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd. It proves that FULL literal TREE253 and joint strict S=U=1 force the complementary genuine primal greedy tree, and proves the stronger mixed-radial-sign obstruction at its SIMPLE leaves. The new argument below does not reinterpret any of its labelled incidences and does not claim its weak-unstable extension from a merely strict-unstable angular proof.
* [internal-source-reference], SHA256 0a41828439b53441a8f97ccfded65fc45b492e836580dfca02a7faa58420cc69. Its mathematical text establishes the K3 run-count classification and supplies a local quadrivalent strictly unstable countercontrol to an automatic nonsimple-leaf ban. Its embedded one-block encoded recovery DATA is known corrupted and is EXCLUDED; none of the present proofs or computations uses that encoded block. The corrected K3 capsule remains [internal-source-reference], [internal-source-reference] and [internal-source-reference].

The new exact symbolic/rational audit source is [internal-source-reference], described completely in the recovery section below. The universal claims are proved here analytically; the code checks the displayed polynomial family identities and literal rational controls, not a sample-based universal geometric assertion.

## 1. Genuine local normal section and reciprocal metric

Let P be a full-dimensional convex three-polyhedron with reference 0 in its interior. Use genuine maximal facets, genuine vertices and genuine edges. Write its facet inequalities as q_i^T z<=1. Let M be the positive definite physical metric and N=M^{-1}. A true vertex x is strictly unstable precisely when

x^T M e<0

for every nonzero extreme-ray direction e of its true tangent cone, equivalently Mx is in the interior of the outward normal cone at x.

Let q_0,...,q_{d-1} be the d incident facet poles, in their cyclic order. The number d is also the number of genuine edges incident to x. Put

r^2=x^T M x, sigma=1/r^2,
x_tilde=M^{1/2}x, q_tilde_i=M^{-1/2}q_i,
p=x_tilde/r^2, y_i=q_tilde_i-p.

This is one simultaneous physical change of coordinates, with the inverse transformation on the poles. Because q_i^T x=1, the vectors y_i lie in the plane perpendicular to x_tilde. The q_tilde_i are exactly the vertices of a genuine two-dimensional polar face, so the y_i are the vertices of a convex polygon in this plane.

Strict instability says that x_tilde is interior to the positive hull of q_tilde_i. Intersect that cone with the plane q^T x_tilde=1: p lies in the relative interior of conv(q_tilde_i). Hence 0 is strictly inside conv(y_i). In particular every y_i is nonzero. Define

u_i=||y_i||^2=q_i^T N q_i-sigma>0,
rho_i=sqrt(u_i).

Thus these are tangential squared radii and radii, NOT the raw squared pole norms and pole norms.

The pole-arrow identity is exact:

q_i^T N(q_j-q_i)=y_i dot (y_j-y_i).

A weak arrow i->j means this expression is nonnegative. For distinct incident poles such an arrow implies

u_j-u_i=2 y_i dot(y_j-y_i)+||y_j-y_i||^2>0.

All norm inequalities used below are therefore strict even when the arrow derivative itself is zero.

## 2. Necessary angular budget for a boundary path

Assume that d-1 consecutive boundary edges of the incident polar polygon are selected weak pole arrows, in either direction, so that they form a boundary path and leave one boundary edge unselected. For an arrow e:i->j put

eta_e=u_i/u_j in (0,1).

Since 0 lies strictly inside the polygon, the positive central angles between consecutive rays are all in (0,pi), and their sum is 2pi. On a selected edge its central angle beta_e satisfies

rho_i rho_j cos(beta_e)>=rho_i^2,

so

0<beta_e<=arccos(sqrt(eta_e))<pi/2.

The omitted edge has a central gap less than pi. Therefore the sum of the selected actual angles is greater than pi, and necessarily

SUM_e arccos(sqrt(eta_e))>pi.                    (A)

This proof uses actual cyclic adjacency and strict instability. It does not apply to an arbitrary set of nonincident poles, and it does not silently replace strict instability by a weak contact condition.

For d=3, there are only two selected angles, each strictly less than pi/2. Thus (A) is impossible. This recovers a strict-unstable simple-leaf ban without a full global shadow-graph hypothesis or a centroid condition. The earlier pZ theorem is stronger on weak local boundaries and remains the authority for that stronger statement.

## 3. Four incident poles: exact algebraic criterion

For d=4 let eta_1,eta_2,eta_3 be the three selected arrow ratios. Then (A) is equivalent to

eta_1+eta_2+eta_3+2 sqrt(eta_1 eta_2 eta_3)<1.    (Q)

Proof: put A=arccos(sqrt(eta_1)), B=arccos(sqrt(eta_2)), C=arccos(sqrt(eta_3)), and a=cos A, b=cos B, c=cos C. All three angles are in (0,pi/2). Direct expansion gives

a^2+b^2+c^2+2abc-1
 =(c+cos(A+B))(c+cos(A-B)).

The second factor is positive. The first is negative exactly when A+B+C>pi: when A+B<=pi/2 it cannot be negative; otherwise cos is strictly decreasing and arccos(-cos(A+B))=pi-A-B. This proves the equivalence, including the strict boundary.

### Polynomial guards without square roots

For the three directed edges define, with multiplicities retained,

D=PRODUCT_e u_head(e)>0,
P0=PRODUCT_e u_tail(e)>0,
B0=D-SUM_e [u_tail(e) PRODUCT_{f!=e}u_head(f)].

Then (Q) is equivalent to the TWO polynomial inequalities

B0>0,
B0^2-4 P0 D>0.                                  (P)

Indeed (Q) is B0>2 sqrt(P0 D); the first sign guard is essential when squaring. Repeated heads in an inward-oriented path are repeated factors, not distinct-set products.

For an actual joint primal/polar realization one may use

a_i=(x^T M x)(q_i^T N q_i)-1=r^2 u_i>0

instead of u_i. Every ratio and both homogeneous sign guards are unchanged. This embeds the condition in a single physical primal/polar Gram formulation without introducing an independent metric, a new center, or freely chosen masses.

## 4. Necessity and sufficiency for the LOCAL four-pole rooted path

Fix four positive squared radii u_0,u_1,u_2,u_3 and the boundary path 0-1-2-3, oriented toward one of its four vertices. Suppose every arrow strictly increases u. Then the following are equivalent:

(i) There is a convex quadrilateral y_0,y_1,y_2,y_3, in that cyclic order, containing 0 strictly, with ||y_i||^2=u_i, and whose COMPLETE nonnegative distinct-pole shadow graph consists of exactly the prescribed three arrows.

(ii) The ratios of those three arrows satisfy (Q), or equivalently (P).

Necessity follows from Sections 1-3. For sufficiency set alpha_i=arccos(sqrt(u_tail/u_head)) for the boundary edge i-(i+1). Place y_i with radius sqrt(u_i) at the successive angles

0, alpha_0, alpha_0+alpha_1, S=alpha_0+alpha_1+alpha_2.

Condition (Q) gives pi<S<3pi/2. Thus the closing angular gap is in (pi/2,pi). Every selected arrow is exactly zero; every reverse arrow is strictly negative. It remains to prove that this angular placement is genuinely convex and has no unwanted nonnegative arrows.

Let R denote positive rotation by pi/2. Up to reversal of the path there are only two orientations.

### Directed chain 0->1->2->3

The consecutive edge vectors e_0=y_1-y_0, e_1=y_2-y_1, e_2=y_3-y_2 are positive multiples of R y_0, R y_1, R y_2, respectively. The two internal turns are positive because their arguments differ by alpha_0 and alpha_1, both in (0,pi/2). For the closing edge e_3=y_0-y_3,

cross(e_2,e_3) is a positive multiple of u_2-y_2 dot y_0>0,

where Cauchy-Schwarz and u_2>u_0 give the strict inequality. Also

cross(e_3,e_0) is a positive multiple of u_0-y_0 dot y_3>0,

because cos S<0. The four radial arguments are in their cyclic order, with every consecutive gap less than pi, so the polygon is simple. The positive turns make it a strictly convex quadrilateral. Every origin-edge cross product is positive; consequently 0 is strictly inside it.

For the nonconsecutive pair 0,2,

cos(alpha_0+alpha_1)<cos(alpha_0)cos(alpha_1)

implies y_0 dot y_2<u_0, by telescoping the two radius ratios. Similarly y_1 dot y_3<u_1. The pair 0,3 has negative dot product. These are below both relevant squared radii, so all nonparent arrows are strictly negative.

### Inward path 0->1<-2<-3

Now e_0,e_1,e_2 are positive multiples of R y_0, R y_2, R y_3, respectively. The first internal turn has argument alpha_0+alpha_1 in (0,pi); the next has argument alpha_2 in (0,pi/2), so both are positive. The two closing turns are positive multiples of u_3-y_3 dot y_0 and u_0-y_0 dot y_3. They are positive because cos S<0. As above, the cyclic angular order, all positive turns and all positive origin-edge areas give a convex quadrilateral containing 0 strictly.

For pair 0,2, the same cosine identity gives

y_0 dot y_2<u_0 u_2/u_1<min(u_0,u_2),

since u_1 is larger than both adjacent squared radii. Pair 1,3 telescopes along 3->2->1 and has dot product less than u_3. Pair 0,3 has negative dot product. Hence these nonparent arrows are all strictly negative.

This proves the full local shadow-graph assertion. Each other root position is one of these two cases after reversing the path.

To turn the two-dimensional construction into a local three-dimensional normal cone, choose any sigma>0 and use

x=(0,0,1/sqrt(sigma)), q_i=(y_i,sqrt(sigma)), M=N=I.

Then q_i dot x=1, and x is in the interior of the cone generated by q_i. Thus it is a strictly unstable vertex of this LOCAL support cone. This step does not create a bounded polyhedron with its own volume centroid at 0. Such a global completion is a separate problem.

One can also decrease the three chosen angles slightly while keeping their sum greater than pi. Then all selected arrows become strictly positive. Convexity and all nonparent negative signs persist by openness. Therefore the sufficiency statement is not an artifact of admitting zero selected arrows.

## 5. Sharp directed-chain radius growth

For a three-edge directed chain, eta_1 eta_2 eta_3=u_0/u_3. Put z=rho_0/rho_3. Arithmetic-geometric mean and (Q) give

3 z^(2/3)+2z<1.

The left side is strictly increasing for z>0 and equals 1 at z=1/8. Therefore

rho_3/rho_0>8, or u_3>64 u_0.                   (8)

This is a necessary condition, not by itself a sufficient one; (Q) is the complete local criterion. It concerns tangential radii after subtracting the common radial projection. Replacing it by a claim about raw pole norms would be wrong.

### Exact family showing sharpness

For any k>0 with k^2>3 set s=k^2 and

y_0=(1,0),
y_1=(1,k),
y_2=(1-k^2,2k),
y_3=(1-3k^2,3k-k^3).

The squared radii are u_i=(1+s)^i. The complete off-diagonal shadow matrix, with zero diagonal also displayed, is

[[0,0,-s,-3s],
 [-s,0,0,-s-s^2],
 [-3s-s^2,-s-s^2,0,0],
 [-6s-3s^2-s^3,-3s-4s^2-s^3,-s-2s^2-s^3,0]].

Thus its only nonnegative distinct arrows are 0->1,1->2,2->3, all exactly zero. The origin-edge oriented areas in cyclic order are

k, k(1+s), k(1+s)^2, k(s-3),

and the consecutive polygon turns are

k^3, k^3(1+s), k^3(s+3), 3k^3.

They are all positive. There is the fully explicit positive zero combination

w=((s+1)(s+3),s-3,s-3,3),
SUM_i w_i y_i=0, SUM_i w_i=s(s+6)>0.

These data prove the strict local instability for q_i=(y_i,1), x=(0,0,1). Moreover

rho_3/rho_0=(1+k^2)^(3/2) -> 8 as k decreases to sqrt(3).

At equality the closing origin-edge area is zero, so strict local instability is lost. Hence 8 is the exact unattained infimum. Rational k can approach sqrt(3) from above, so the family has arbitrarily close rational support data; no hidden numerical optimization is involved.

The polynomial guards for this family factor exactly as

D=(1+s)^6, P0=(1+s)^3,
B0=(s-2)(1+s)^5,
B0^2-4P0D=s^2(s-3)(1+s)^9.

The stored source verifies these identities coefficient-by-coefficient over rational polynomials, in addition to the full area, turn, weight, norm and shadow identities.

At k=7/4 the literal rational control is

y=((1,0),(1,7/4),(-33/16,7/2),(-131/16,-7/64)),
integer weights=(6305,16,16,768), sum=7105,
u=(1,65/16,4225/256,274625/4096).

In particular u_3/u_0=274625/4096>64. Its full exact matrices and polynomial guards are deterministically generated in quad_corner_audit.json.

### General directed boundary path

More generally, let n=d-1>=3 and let all selected arrows form a directed chain along the boundary path. If beta_1,...,beta_n are its actual central angles, then

rho_n/rho_0 >= PRODUCT_j sec(beta_j).

The function log sec t has second derivative sec^2 t>0 on (0,pi/2). Since SUM beta_j>pi, convexity gives the sharp necessary inequality

rho_n/rho_0 > sec(pi/n)^n.                       (G)

For n=2 no such local strictly unstable vertex exists, as already proved. Sharpness for every n>=3 is analytic: choose

pi/n < theta < min(3pi/(2n),pi/2),
y_j=(1+i tan(theta))^j, j=0,...,n,

interpreting complex numbers as vectors in the plane. Each selected arrow is zero; consecutive radii multiply by sec(theta), and their angular gaps are theta. The closing gap is in (pi/2,pi). Consecutive edge vectors are positive multiples of R y_j, so internal turns are positive; the last turn is controlled by ||y_{n-1}||^2-y_{n-1} dot y_0>0, and the first by ||y_0||^2-y_n dot y_0>0. The polygon is therefore convex and contains 0 strictly. For a nonparent pair separated by h>=2 steps, either cos(h theta)<=0 or 0<h theta<pi/2. In the latter case repeated cosine addition gives cos(h theta)<cos(theta)^h. Hence every nonparent arrow is negative. The ratio sec(theta)^n tends to the right side of (G) as theta decreases to pi/n. The general-n statement is proved here, not inferred from the n=3 code audit.

## 6. A rational inward-path barrier to using only two TREE253 norm bounds

The following exact local cone has an inward path and satisfies BOTH inherited raw-norm restrictions n_1/n_0>1/2 and n_7/n_0<3/4. It demonstrates why those restrictions plus local quadrivalent instability alone cannot give an exclusion.

Use M=N=I, x=(0,0,1/3), sigma=9 and list the incident facet labels in the cyclic order (7,0,1,2):

q_7=(1,0,3),
q_0=(1,3,3),
q_1=(-1,1,3),
q_2=(-1/10,-1/100,3).

The corresponding y vectors are (1,0),(1,3),(-1,1),(-1/10,-1/100). Positive weights (40,1,1,400), summing to 442, have weighted y sum zero. The origin-edge areas are 3,4,11/100,1/100; consecutive polygon turns are 6,191/50,28/25,33/10. Thus this is a genuine convex local normal section with a strictly unstable vertex.

Its full shadow matrix in that displayed local order is

[[0,0,-2,-11/10],
 [-9,0,-8,-1013/100],
 [-3,0,0,-191/100],
 [-1101/10000,-1401/10000,799/10000,0]].

Its only nonnegative distinct arrows are 7->0,1->0,2->1. The raw squared pole norms in the same order are

(10,19,11,90101/10000).

Therefore n_1/n_0=11/19>1/2 and n_7/n_0=10/19<3/4. Tangential squared radii are (1,10,2,101/10000), and the exact criterion has

D=200, P0=101/5000, B0=13899/100,
B0^2-4P0D=193020601/10000>0.

This control has no asserted remaining five poles, actual Lambda matrix, volume centroid, E17 realization or global equilibrium count. In particular it is NOT a nine-facet TREE253 witness and NOT a homogeneous Gomboc construction.

## 7. Application to the genuine TREE253 quadrivalent leaf

Keep the literal global parent array and dual Hamilton path

p=(0,0,1,2,3,4,5,0,7),
Z=(6,5,4,3,2,1,0,7,8).

Under the accepted complementary-tree theorem, a quadrivalent primal tree leaf has exactly three selected dual edges on its cyclic polar face. They form one run, so its four incident facet labels are one of the six consecutive four-vertex blocks of Z:

3456, 2345, 1234, 0123, 0127, 0178.

The first four are directed chains, and (8) implies respectively

a_3>64a_6, a_2>64a_5, a_1>64a_4, a_0>64a_3,

where a_i=(x^T M x)(q_i^T N q_i)-1>0 for that actual candidate unstable vertex. The full criterion (Q) is stronger than these corollaries.

For block 0127 the three ratios are a_2/a_1, a_1/a_0, a_7/a_0. Thus

a_2/a_1+a_1/a_0+a_7/a_0+2sqrt(a_2 a_7)/a_0<1.

Equivalently, with L=a_0 a_1-a_2 a_0-a_1^2-a_1 a_7,

L>0 and L^2>4 a_2 a_7 a_1^2.

For block 0178 the ratios are a_1/a_0, a_7/a_0, a_8/a_7. Thus

a_1/a_0+a_7/a_0+a_8/a_7+2sqrt(a_1 a_8)/a_0<1.

Equivalently, with L=a_0 a_7-a_1 a_7-a_7^2-a_0 a_8,

L>0 and L^2>4 a_1 a_8 a_7^2.

These are literal facet-label statements. A primal rooted facet/tree quotient that forgets the full pole labeling cannot transport the particular labelled expressions without checking the corresponding facet map and pole-arrow hypotheses.

The accepted K3 census contains 266 full facet-labelled domains whose complementary tree is a path with one simple and one quadrivalent leaf. The present theorem supplies a new necessary condition when the quadrivalent leaf is the unstable root. The number 266 is inherited from the accepted census, not freshly enumerated here. No complete one of those root domains has yet been shown to violate the new condition for all genuine own-centered realizations. Therefore the integer registers are not reduced.

## 8. Complete exact reconstruction and observed verification

The complete runnable input is immutable material

[internal-source-reference]
QUADRIVALENT_POLE_PATH_ANGULAR_CRITERION_V1 complete exact audit source.py.txt.

Save its exact UTF-8/LF text as quad_corner_audit.py. It is 8538 bytes with SHA256

c623d983fdc6c3325088281611cf8b0b494a97bc865bf6f04f963f77fee6814e.

It contains every helper, polynomial coefficient operation, exact literal rational input, graph orientation, weight, sigma and default output name. No numerical optimizer, random seed, external mathematical package, original sandbox checkpoint or omitted data is needed. It uses only the Python standard library, chiefly fractions.Fraction, json, hashlib and pathlib. The observed interpreter was CPython 3.13.5 on Linux x86_64; no floating-point calculation contributes to the checks or generated bytes.

Reconstruction command:

python -S quad_corner_audit.py build

Verification command:

python -S quad_corner_audit.py check

The generated output is quad_corner_audit.json, 6939 bytes, SHA256

6553723a372c0973894816b768bf480b491b8f688793ed9729515d3cd5b84c4b.

Both commands print exactly the terminal marker and output pin

QUADRIVALENT_POLE_PATH_SYMBOLIC_AND_RATIONAL_AUDITS_PASS 6939 6553723a372c0973894816b768bf480b491b8f688793ed9729515d3cd5b84c4b

Build refuses to replace an existing different output. Check deterministically reconstructs the exact expected bytes and compares them to the saved output. The source hash should be checked against the input pin before executing. The output is supplementary: the complete stored source with its literal inputs suffices to reconstruct it if the sandbox disappears.

Observed in this turn: build and check passed in the originating directory; the source was then copied alone into a new directory, and both build and check passed again with the same byte count and SHA256. These are exact symbolic/rational audits and deterministic cold reconstruction, not a second independent proof of the universal geometric theorem and not a numerical feasibility result.

The output records the full polynomial norm, weight, guard and shadow identities, both complete rational controls, their exact origin-edge areas, polygon turns, all nonnegative distinct arrows and scope statements. It explicitly records zero new whole-incidence exclusions and the unchanged accepted C>=34 endpoint.
