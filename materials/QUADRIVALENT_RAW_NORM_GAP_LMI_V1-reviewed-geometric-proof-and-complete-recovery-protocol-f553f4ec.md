# material-f553f4ec1f8d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# QUADRIVALENT_RAW_NORM_GAP_LMI_V1

## Status and exact dependencies

This is the reviewed, explicitly persisted mathematical result recovered from coordinator archive [internal-source-reference] (SHA256 7044cfd031b2942f86e7f0d6f151e5daeeb8f1095a7defddb8148257d2bdd10e). The archive itself was unreviewed historical evidence; its claims were not promoted merely because that archive existed. The proof below was checked algebraically against the completely read geometric parent and against the literal TREE253 hypotheses. The complete exact audit source was recovered and build/check were observed in this continuation.

Mathematical parents, all completely read from cursor 0 to eof:true in this continuation:

* [internal-source-reference], SHA256 844ae3e67f523827df904cb541c79b63f82185d61a54608339397abdd8f84b65: the incident-pole angular budget, the exact local four-pole converse, and the six literal TREE253 quadrivalent leaf blocks.
* minimum-0078, SHA256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd: FULL TREE253 forces the complementary genuine primal greedy tree; a simple leaf cannot be even weakly unstable; zero tangential poles are forbidden by the full outdegree condition. Its literal result, not its superseded intermediate counters, is authoritative.
* minimum-0069, SHA256 d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff: actual homogeneous-volume Lambda identities, n1/n0>1/2, n7/n0<3/4, and Lambda05+Lambda06>51/25. Its numerical certificate generator was not reexecuted here.

The result supplies necessary local constraints for a real body and an exact converse only for an isolated local normal cone with prescribed raw squared pole norms. It does NOT supply a bounded own-centroid polyhedron. No additional entire labelled incidence/root domain or combinatorial type has been excluded. The accepted internal endpoint remains V>=10, F>=9, C>=34; K2 remains 278/550 excluded, and K3 remains 11743 open labelled roots or 8739 rooted primal facet/tree classes. C=34 existence, exclusion of every E=17 body, the exact minimum, a verified Figure C=650 upper bound, and priority/contest claims remain unresolved.

## 1. One metric, one vertex, genuine incident poles

Let x be a genuine vertex of a full-dimensional convex three-polyhedron with an interior reference at 0. Its four incident maximal-facet inequalities are q_i^T z<=1, in cyclic order A,B,C,D. Let M be the physical positive definite metric and N=M^{-1}. Define

r^2=x^T M x, sigma=1/r^2, n_i=q_i^T N q_i,
x_tilde=M^{1/2}x, q_tilde_i=M^{-1/2}q_i,
y_i=q_tilde_i-x_tilde/r^2.

Since q_i^T x=1, all y_i lie in one plane perpendicular to x_tilde, and

||y_i||^2=n_i-sigma,
q_i^T N(q_j-q_i)=y_i dot(y_j-y_i).

The y_i are the vertices of a genuine convex quadrilateral. Strict instability means 0 is strictly inside it. We also allow weak instability, meaning 0 belongs to its boundary, PROVIDED every y_i is nonzero. Under FULL TREE253 this proviso follows: y_i=0 would give three nonnegative distinct outgoing pole arrows from i, whereas the full graph allows at most one. It does not follow merely from choosing an arbitrary spanning tree of a larger shadow graph.

Assume three consecutive boundary edges form a weak-arrow path directed toward one of its four vertices. Up to reversal there are two cases:

A->B->C->D, or A->B<-C<-D.

Each arrow i->j strictly increases squared norm, because

n_j-n_i=2 y_i dot(y_j-y_i)+||y_j-y_i||^2>0.

All strict norm orderings below therefore remain valid on zero-derivative arrow walls.

## 2. Exact elimination of the unknown common shift

For an arrow e with tail t and head h, define

eta_e(s)=(n_t-s)/(n_h-s),
F(s)=sum_e eta_e(s)+2 sqrt(product_e eta_e(s)),
m=min_i n_i.

We have 0<sigma<m. The angular parent proves F(sigma)<1 at a strictly unstable corner. Its weak extension under the stated nonzero condition is F(sigma)<=1: the origin can lie only on the unselected closing edge, because on a selected edge the two nonzero opposite radii would make either arrow strictly negative. Thus the selected central angles sum to pi on that wall; otherwise their sum exceeds pi. Every selected angle is at most arccos sqrt(eta_e), strictly less than pi/2. The equivalence to F<=1 follows from

a^2+b^2+c^2+2abc-1=(c+cos(A+B))(c+cos(A-B)),

where a=cos A, b=cos B, c=cos C and A,B,C are in (0,pi/2). The second factor is positive; the first has the sign of pi-(A+B+C).

For s<m every eta_e is strictly decreasing:

eta_e'(s)=(n_t-n_h)/(n_h-s)^2<0.

A minimum norm can occur only at a path tail, never at a head, so denominators stay positive at s=m. Therefore F is continuous there and

F(m)<F(sigma)<=1.

Conversely, if the prescribed positive raw norms have the required arrow orderings and F(m)<1, choose a positive sigma<m sufficiently close to m that F(sigma)<1. The exact local converse in [internal-source-reference] constructs a convex quadrilateral of squared radii n_i-sigma containing 0 strictly, with exactly the prescribed three nonnegative distinct arrows. Lifting by

q_i=(y_i,sqrt(sigma)), x=(0,0,1/sqrt(sigma)), M=N=I

gives a genuine local three-dimensional support cone and exactly the prescribed raw norms n_i.

THEOREM: F(m)<1 is necessary for every actual corner described above and is necessary and sufficient for the existence of SOME strictly unstable local normal cone with those four raw squared pole norms and that complete local rooted-path graph. The converse does not hold for a separately fixed actual sigma without checking F(sigma)<1, and does not assert a global body or its own volume centroid.

## 3. Directed chain: a two-by-two affine matrix

Write a<b<c<d for the four raw squared norms and

Delta1=b-a, Delta2=c-b, Delta3=d-c.

The minimum is a, so

F(a)=(b-a)/(c-a)+(c-a)/(d-a).

Clearing positive denominators gives the exact equivalences

F(a)<1
iff (c-b)(d-a)>(c-a)^2
iff Delta2 Delta3>Delta1(Delta1+Delta2)
iff L_chain=[[c-b,b-a],[b-a,d-c-b+a]] is positive definite.

The last equivalence uses Delta2>0 and the determinant identity

det L_chain=Delta2(Delta3-Delta1)-Delta1^2.

For any fixed real tau this implies the valid linear cut

Delta3>(1+2 tau)Delta1-tau^2 Delta2,

because

Delta2[Delta3-(1+2 tau)Delta1+tau^2 Delta2]-det L_chain
=(tau Delta2-Delta1)^2.

A finite set of rational cuts is only a relaxation, not the full open cone.

A useful sharp consequence is

d-a>4(b-a).

Indeed d-a>2 Delta1+Delta2+Delta1^2/Delta2>=4 Delta1. Equal successive increments h>0 are impossible, since the determinant then equals -h^2. These are exclusions of continuous local norm classes, not entire polyhedral combinatorial types.

## 4. Inward path: a lifted affine matrix

For A->B<-C<-D, write n_A=a,n_B=b,n_C=c,n_D=d. Thus b>a and b>c>d. Set

p=d-a, q=c-d>0, h=b-c>0.

If p<=0, the minimum is d and F(d)=(q-p)/(q+h), so the exact condition is h+p>0. If p>=0, the minimum is a and

F(a)=p/(p+q)+(p+q)/(p+q+h)<1
iff qh>p(p+q).

Both cases agree at p=0. Equivalently,

h>|p|+max(p,0)^2/q.

This is exactly the existence of z>=0, z>=p such that

L_inward=[[q,z],[z,h+p-2z]] is positive definite.

Its determinant condition is h+p>2z+z^2/q. The right side is increasing for z>=0, so its least permissible value is attained at z=max(0,p), giving exactly the two cases above. All entries are affine in the raw squared norms and the one auxiliary variable z.

Valid necessary linear cuts are h>-p and, for each fixed tau>=0,

h>(1+2tau)p-tau^2 q.

For p>=0 the latter follows from the same completed-square identity as in the chain case. For p<0 its right side is nonpositive whereas h>0.

## 5. Literal TREE253 applications

Do not change the labels

p_tree=(0,0,1,2,3,4,5,0,7),
Z=(6,5,4,3,2,1,0,7,8).

When a quadrivalent leaf of the forced complementary primal tree is the candidate unstable root, its incident facets are one consecutive four-vertex block of Z. The four chain possibilities require, respectively,

3456: [[n4-n5,n5-n6],[n5-n6,n3-n4-n5+n6]] positive definite;
2345: [[n3-n4,n4-n5],[n4-n5,n2-n3-n4+n5]] positive definite;
1234: [[n2-n3,n3-n4],[n3-n4,n1-n2-n3+n4]] positive definite;
0123: [[n1-n2,n2-n3],[n2-n3,n0-n1-n2+n3]] positive definite.

For 0127 there must exist z>=0,z>=n2-n7 with

[[n1-n2,z],[z,n0-n1+n2-n7-2z]] positive definite.

For 0178 there must exist z>=0,z>=n8-n1 with

[[n7-n8,z],[z,n0-n7+n8-n1-2z]] positive definite.

Only the block belonging to the ACTUAL incident-facet set and the ACTUAL unstable root may be imposed. The six matrices are not six simultaneous requirements. A primal facet/tree quotient that forgets pole labels does not automatically transport these labelled formulas. For an impossibility certificate one may safely relax positive definiteness to positive semidefiniteness. One may not arbitrarily posit a uniform positive margin. Affineness in G=QNQ^T does not imply affineness in a different parametrization in which G itself is polynomial.

## 6. Exact controls, information loss, and sharpness

The following complete rational family separates a permitted weak corner from a strict corner. For t>=0 take

y0=(1,0), y1=(1,1), y2=(-1,3), y3=(-10-3t,-t),
q_i=(y_i,1), x=(0,0,1), M=N=I.

Its complete nonnegative distinct graph is precisely the chain 0->1->2->3, with the three derivatives zero. Origin-edge oriented areas are (1,4,30+10t,t), and polygon turns are (2,24+8t,33+11t,11+3t). For t>0 the positive weights (40+12t,t,t,4) have weighted y sum zero. At t=0 the raw norms are (2,3,11,101), det L_chain=711, and F(sigma)=1. At t=1 the raw norms are (2,3,11,171) and det L_chain=1271. This proves that the projected strict determinant remains necessary even on the allowed weak wall.

For an entirely rational sharp family, let epsilon>0 and set

y0=(epsilon,0),
y1=(epsilon,1),
y2=(-1-epsilon,1+epsilon+2epsilon^2),
y3=(-2-4epsilon-4epsilon^2-4epsilon^3,-2epsilon),
q_i=(y_i,1), x=(0,0,1), M=N=I.

Put f=2+epsilon+2epsilon^2. Positive zero-combination weights are

(2epsilon+f(2+4epsilon+4epsilon^2+4epsilon^3),
 2epsilon^2,2epsilon^2,epsilon f).

The complete recovered symbolic source proves coefficientwise that all four areas, all four turns, and all four weights are positive for every epsilon>0; all nonparent shadows are negative and the three selected shadows are zero. It verifies the zero-combination identities exactly. The raw norm differences satisfy

b-a=1,
d-a=4+16epsilon+35epsilon^2+48epsilon^3+48epsilon^4+32epsilon^5+16epsilon^6.

Thus 4 is the exact unattained infimum. At epsilon=0 the first tangential vector becomes zero and the full local path graph is lost.

The raw quadruple (1,2,4,8) has det L_chain=5>0, but its fixed-sigma angular criterion fails at sigma=1/10 and holds at sigma=99/100. These are two possible local shift choices, not two centers of one body. The projected condition deliberately loses actual sigma information.

The inherited inward control is kept literally: in cyclic global-label order (7,0,1,2), take q7=(1,0,3),q0=(1,3,3),q1=(-1,1,3),q2=(-1/10,-1/100,3), with x=(0,0,1/3), M=N=I, sigma=9. Weights (40,1,1,400) annihilate the tangential vectors positively. Its full local graph is 7->0,1->0,2->1. The raw norms are (10,19,11,90101/10000); hence n1/n0=11/19>1/2 and n7/n0=10/19<3/4, and the new inward matrix also passes. Therefore these two inherited raw-norm inequalities together with the exact projected corner condition are NOT sufficient to exclude even the isolated local cone. No remaining five poles, actual Lambda, volume centroid, or global 110 count is asserted for this control.

## 7. Longer directed paths

Let a strictly unstable vertex, or an allowed weak vertex with all tangential poles nonzero, have degree n+1 with n>=3. Suppose n consecutive polar boundary edges are weak arrows in one direction and the prescribed raw squared norms satisfy a0<a1<...<an. Then

(an-a0)/(a1-a0)>sec(pi/(2(n-1)))^(2(n-1)).

Proof: the sum of the actual selected central angles is at least pi. The first selected angle is strictly less than pi/2. On increasing the common shift from its actual sigma toward a0, every remaining bound increases to

alpha_j=arccos sqrt((a_{j-1}-a0)/(a_j-a0)), j=2,...,n.

Consequently sum_{j=2}^n alpha_j>pi/2. Their secants telescope:

product_{j=2}^n sec(alpha_j)^2=(an-a0)/(a1-a0).

Strict convexity of log sec on (0,pi/2), followed by its monotonicity, proves the inequality.

Sharpness is analytic. Choose 0<delta<pi/8, epsilon=sin(delta), theta=(pi/2+2delta)/(n-1), and in the complex plane set

y0=epsilon,
y1=exp(i(pi/2-delta)),
y_j=y1(1+i tan(theta))^(j-1), j=1,...,n.

Lift q_j=(y_j,1),x=(0,0,1). Each selected arrow is zero; all radii strictly increase. The sum of selected angles is pi+delta and the closing gap is pi-delta. Consecutive edges are positive multiples of the positive quarter-turns of their initial radii. All internal turns are positive. The last closing turn is controlled by ||y_{n-1}||^2-y_{n-1} dot y0>0, and the first by ||y0||^2-y0 dot y_n>0; the latter dot product is negative. The radial gaps are below pi, so the polygon is simple, strictly convex, and contains 0 strictly. For a nonparent pair the angle difference lies below 3pi/2. Its cosine is either nonpositive, or its angle is below pi/2 and repeated cosine addition makes it strictly less than the product of the constituent cosines. Hence every nonparent shadow is strictly negative. The ratio of raw differences is

[sec(theta)^(2(n-1))-sin(delta)^2]/[1-sin(delta)^2],

which tends to the claimed constant. For n=3 this is 4; for n=4 it is 64/27. This general-n proof is not inferred from a finite audit. No converse for arbitrary prescribed raw norms when n>3 is claimed.

## 8. Complete recovery, exact input pins, and observed output

The entire executable recovery source is stored in

[internal-source-reference],
QUADRIVALENT_RAW_NORM_GAP_LMI_V1 complete recovery source JSON-escaped.txt,
7331 bytes, SHA256 8e03b4199db0fb0654c23db14e482f095d8248f9c01241faa3a8d56c912da8ce.

It is the exact JSON-string content (without enclosing quotation marks) of the complete recover_raw_gap.py source. It was extracted losslessly from archive [internal-source-reference], UTF-16 interval [13647,20978). Save the material bytes exactly as raw_gap_source_json_escaped.txt, without adding a final newline. To decode, verify the input pin and execute the following complete standard-library unit as decode_raw_gap.py:

```python
from pathlib import Path
import hashlib
import json
raw = Path('raw_gap_source_json_escaped.txt').read_bytes()
assert (len(raw), hashlib.sha256(raw).hexdigest()) == (7331, '8e03b4199db0fb0654c23db14e482f095d8248f9c01241faa3a8d56c912da8ce')
source = json.loads('"' + raw.decode('utf-8') + '"').encode('utf-8')
assert (len(source), hashlib.sha256(source).hexdigest()) == (7224, '25e2f98172b8a5f272c54bd87fd2e3d64da4dba1c720fe5aa3749ecc74059c29')
target = Path('recover_raw_gap.py')
assert not target.exists() or target.read_bytes() == source
target.write_bytes(source)
print('RAW_GAP_JSON_SOURCE_DECODE_PASS')
```

Reconstruction and verification commands, assertions enabled:

python -S decode_raw_gap.py
python -S recover_raw_gap.py build
python -S recover_raw_gap.py check

The recovered source checks its own packed input (4560 bytes, SHA256 5f107e8cf333fc178167bbaa92ed070f9048d2bc4a6dff90d98866860e20cf61) and writes the complete raw_gap_recovered/raw_gap_audit.py (13854 bytes, SHA256 45c1107bd6eedfd8bbb898e80d427d2ffd1def07493e0710f0148ef03eb23372). That source includes every Fraction/polynomial helper and every literal input, and needs no sandbox checkpoint, external geometry, random seed, or numerical optimizer. Only the standard library is used; the observed interpreter is CPython 3.13.5.

The reproduced output raw_gap_recovered/raw_gap_audit.json has 34000 bytes and SHA256 7a21c0bb2bde521f125c7b03353571f453336ed209f1767474b42fff63f82aee. Its exact formula census covers all ordered integer raw norms 1..10: 210 chain quadruples, 52 passing; 870 inward quadruples, 382 passing. These are local formula tests, not global polyhedral enumeration.

Both build and check were observed in this continuation after recovering the complete source; source re-encoding reproduced the exact 7331-byte stored escaped-source pin. Terminal markers were

QUADRIVALENT_RAW_NORM_GAP_LMI_AUDITS_PASS 34000 7a21c0bb2bde521f125c7b03353571f453336ed209f1767474b42fff63f82aee
RAW_GAP_COMPLETE_SOURCE_RECOVERY_PASS build 13854 45c1107bd6eedfd8bbb898e80d427d2ffd1def07493e0710f0148ef03eb23372

and the corresponding check marker with the same two pins. These exact audits support the polynomial and rational controls; the universal geometric statements are proved above. The construction is now explicitly persisted and no longer merely an ephemeral sandbox object.
