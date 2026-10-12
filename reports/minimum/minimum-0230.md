# minimum-0230

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# VF_COUPLING_RIGHT_JETS_AND_PRIVATE_FACET_STRESS_RESCUE_V1

Slot: Sharp Lynx 54. Branch: [internal-source-reference].

## 1. Results and exact scope

The full S1U1 regularization question is not settled here. The following advances concern the actual reduced contact packet, rather than an additional projective-only obstruction.

**A. A genuine VF packet has only two necessary complementary exit choices, not four.** This follows from an exact identity coupling its two primal and two reciprocal polar primitives. Consequently a first-layer packet needs at most 2^8=256 local selectors instead of65536. No independent primal/polar metric is introduced.

**B. For first-order escape, each physical VF can be compressed further to one scalar constraint, chosen according to its physical corner angle.** Thus a selector has one row per physical weak point, rather than two rows perVF. With k physical points and q VF points, k≤17−q in the S1U1 first layer. This is not a dimension-count proof of feasibility.

**C. The corresponding second-order reduction has an essential correction at a right VF corner.** I derive its sharp threshold and incorporate it into the entire-stress-cone second-jet criterion on the genuine realization manifold. Five exact uniformly filled tetrahedral curves show that omitting this term can create a new strict stable or unstable equilibrium. Equality can leave a VE contact, while the same first and second jets can be rescued at third order.

**D. A new sufficient actual-shape rescue theorem removes a packet whose positive metric dependencies all involve one contact, provided that contact has a specified private movable facet and a separate genuine centroid-corrector facet.** The proof constructs a true same-lattice deformation, keeps the moving uniform COM exactly fixed by the implicit function theorem, and defeats the entire positive-stress cone. Applied to any actual weak S1U1 body meeting these hypotheses, it gives arbitrarily close proper110 bodies of the same type. No such S1U1 input is asserted to exist.

**E. There are at most two completely plane-movable facets on any genuine10/17/9 polyhedron.** This explains why independently assigning a free whole facet to every weak contact cannot solve the general first-layer problem. It does not reduce the eleven genuine affine shape parameters to two.

No canonical count, global exclusion, attaining construction, or complexity bound changes. The accepted internal interval remains34≤C_min≤622. The new radial-index input makes strictH0 automatic for an actual weak-inclusive S1U1 body; additional weak points remain the genuine issue.

## 2. Authority and physical conventions

The exact parent is `minimum-0227`, SHA-256 `57bf2cc803fdd3e5ace5587e000d4b1b6372f42306aaff28e467e2b94f1ca8db`. Its literal payload, including the complete source, is present in the new journal and was read through EOF. The new inputs are `[internal-source-reference]` and `[internal-source-reference]`. No conflicting parent incidence or object identity was found.

I use the supplied zero-weak-index theorem and reduced-selector equivalence as mathematical inputs, not as new results or as theorems inferred from the controls below. In particular, the additional no-strict-saddle premise in my parent's final open question is now unnecessary. While all original nonzero primitive signs are protected, eliminating weakvertex and weakfacet groups eliminates every physical weak point and preserves the exact strict S,U,H labels.

The genuine realization equations are smooth. Their eleven affine shape parameters and five trace-one metric parameters give a sixteen-dimensional local manifold in the first layer. The maximum-simplex inequalities are chart restrictions, not physical restrictions on its tangent space. None of this eliminates positive mechanical dependencies.

Use actual centered vertices X_i, same-origin facet poles q_f, and ONE SPD pair M,N=M⁻¹. Write

P_ij=X_iᵀM(X_j−X_i),
Q_fh=q_fᵀN(q_h−q_f).

Only true edges and maximal facets enter. In the local arguments, every initially nonzero primitive sign is protected by taking a sufficiently small genuine same-lattice neighborhood. Harmless zero rows are not required to become positive.

## 3. Exact VF coupling and two complementary selectors

Consider any genuine vertex–facet flag v∈F, not necessarily currently an equilibrium. Let q be the pole of F, so q·v=1. Let e1,e2 be the two true boundary-edge vectors of F emanating from v. The other facet across e1 has pole r1; the other facet across e2 has pole r2. Define

s=qᵀNq>0, p=Nq/s,
E=[e1 e2], v−p=E u,
G=EᵀME=[[a,c],[c,b]],
δ1=−(r1−q)·e2>0,
δ2=−(r2−q)·e1>0.

Here p is the physical perpendicular foot on the actual plane of F. The two positive δ values are true nonincidence slacks: the opposite endpoint of either boundary edge is not on the neighboring facet across the other edge. G is positive definite.

Put P1=vᵀMe1, P2=vᵀMe2, Q1=qᵀN(r1−q), Q2=qᵀN(r2−q). Then the following identities hold **exactly throughout the genuine flag neighborhood**:

(P1,P2)ᵀ=G u,
Q1=sδ1 u2,
Q2=sδ2 u1.                                                   (3.1)

Indeed pᵀMe_i=q·e_i/s=0. Also (r1−q)·v=(r1−q)·e1=0, while (r1−q)·e2=−δ1; substituting p=v−Eu proves the polar formula. The second formula is analogous.

Consequently

P1 Q2/(sδ2)+P2 Q1/(sδ1)
=uᵀGu=(v−p)ᵀM(v−p)≥0,                                     (3.2)

with equality exactly when p=v. At an initialVF this equality holds, but its second-order contribution cannot generally be discarded.

### Theorem 3.1: two choices suffice

In a neighborhood of a physical VF with its other nonzero signs protected,

(max(P1,P2)>0 and max(Q1,Q2)>0)

is equivalent to

(P1>0 and Q2>0) OR (P2>0 and Q1>0).                         (3.3)

These are the two cross-edge choices: the polar exit is across the other boundary edge, not the edge chosen for the primal exit.

To prove necessity, use(3.1). Suppose some P_i and some u_j are positive, but no coordinate has both P_i>0 and u_i>0. In two coordinates their positive entries must be at different indices. The two products P1u1 and P2u2 are then nonpositive, contradicting uᵀGu>0. Sufficiency is immediate.

This is an exact scalar coupling of an actual flag, not an assertion about four freely assigned tensor rows. It holds for nonsimple vertices and nontriangular F. The closing relation does not add an artificial mechanical edge.

For q distinctVF points, the complete local reduced packet therefore has at most2^q selectors, each retaining the two necessary extreme groups at eachVF. In first-layer S1U1, q≤8, so256 selectors suffice. The source's4^q bound remains valid but is not sharp once the common-metric flag relation is retained.

## 4. One row per physical point at first order

The off-diagonal entry c=e1ᵀMe2 records the actual physical corner angle.

If c≥0, then u≤0 implies Gu≤0. Hence

joint VF escape ⇔ max(P1,P2)>0.                             (4.1)

If c≤0, then u1>0,u2≤0 gives P1=a u1+c u2>0, and similarly with indices reversed. If both u entries are positive, uᵀGu>0 ensures that at least one P entry is positive. Therefore

joint VF escape ⇔ max(u1,u2)>0
                ⇔ max(Q1,Q2)>0.                            (4.2)

For an initially acute corner, c>0 persists locally and(4.1) is an exact neighborhood reduction. For an initially obtuse corner, c<0 persists and(4.2) is exact. At an initially right corner, c=0 need not persist; it must not be used as a neighborhood assumption.

Nevertheless at the initialVF, u=0 and

P′=G0 u′,
(Q2/(sδ2),Q1/(sδ1))′=u′.                                   (4.3)

At a right corner G0 is diagonal and positive. Thus one positive component of u′ gives both complementary exits already at first order.

### First-order packet theorem

For every physical point select a scalar row as follows:

VE: its unique forced primal row.
EF: its unique forced polar row.
AcuteVF: either P1 or P2.
ObtuseVF: either u1 or u2, which are positive rescalings of Q2,Q1.
RightVF: either u1 or u2; equivalently the corresponding P_i/a_i at the initial first jet.

A true tangent direction making every selected scalar derivative positive removes the entire packet, with every required primal and polar VF exit positive at first order. Conversely, a simultaneous strict first-order resolution selects one such positive row at each point. The full-rank incidence theorem integrates this direction to a true same-lattice analytic arc.

There is now **one row per physical point**. If k=nVE+nEF+nVF and q=nVF, the supplied bounds give

k+q≤17, hence k≤17−q,
number of choices≤2^q≤256.                                  (4.4)

The parent's full mechanical reaction criterion applies to these rows, with their positive rescaling factors. In particular first-order failure requires a positive dependence on the full true tangent space for every such selector. Linear dependence is not excluded merely because k≤16 when q≥1.

For clarity, a normalized u-row is not a new independent variable: it is computed from the same moving vertex, facet pole, reciprocal metric and actual COM in(3.1).

## 5. The sharp right-corner second-jet threshold

Let an actual C² deformation start at a rightVF. Write

u(ε)=εα+ε²β/2+o(ε²),
G12(ε)=εδ+o(ε),
G11(0)=a>0, G22(0)=b>0.

If some α_i>0, the point is already resolved at first order. If both α_i<0, no strict first/second-order resolution occurs along that prescribed initial velocity.

Suppose α_i=0 and α_j≤0. The only potentially resolving coordinate when α_j<0 is i. Differentiating(3.1) gives

P_i″=G_ii(0)β_i+2δα_j,
normalized complementary Q_i″=β_i.

Thus the exact condition for both exits to be strictly positive at second order is

**β_i>Θ_i:=max(0,−2δα_j/G_ii(0)).**                        (5.1)

If α1=α2=0, this reduces to choosing some β_i>0. The formula also covers α_j=0 directly.

The varying corner term is genuine:

δ=e1′ᵀM0e2+e1ᵀM0e2′+e1ᵀM′e2.

It cannot be replaced by a derivative of a freely chosen angle. The mismatch derivatives α,β include the actual moving centroid and reciprocal foot.

### Entire-cone second-order criterion after compression

Let C(z)=0 be the seven genuine planarity equations in a23-variable local chart and L=ker DC(z0). Choose a true velocity v∈L. Select dominant scalar exits as in Section4 for simple and nonright contacts, requiring their first derivatives to be nonnegative. Remove from the second-order test every point already resolved at first order.

For a remaining rightVF compute α=u′(v). If both components are negative, this velocity is unsuitable for a strict second-jet resolution. Otherwise choose a zero component i with the other component nonpositive, retain the scalar f=u_i, and attach its threshold Θ_i(v) from(5.1). At the other remaining contacts attach threshold0.

Choose any acceleration a0 satisfying

DC a0=−D²C[v,v].

For every remaining selected row define

b_i=D²f_i[v,v]+df_i(a0)−Θ_i(v).

Then the selected strict first/second-order tests are achievable by one true arc **if and only if**

Σ_i λ_i b_i>0

for every nonzero λ≥0 with

Σ_i λ_i df_i|L=0.                                           (5.2)

If that cone is empty, the condition is vacuous. This tests the entire cone, not a selected stress ray. It is the finite-dimensional strict separation of b+df(L) from the nonpositive alternative: adding w∈L to a0 changes the second coefficients by df_i(w). The implicit function theorem then corrects the remaining geometric error at order3 without changing the prescribed first two jets.

The choices above include all strict first/second-jet resolutions of the local packet. They do not include arcs whose first successful exit occurs at order3 or higher. Equality in(5.1) or(5.2) is therefore not an all-orders obstruction.

### Actual moments and inverse metric remain compulsory

For the genuine oriented boundary fan,

D=Σ det(Y_a,Y_b,Y_c),
J=Σ det(Y_a,Y_b,Y_c)(Y_a+Y_b+Y_c),
g=J/(4D).

Its true derivatives are

g′=(J′−4gD′)/(4D),
g″=(J″−4gD″−8D′g′)/(4D).                                   (5.3)

At M0=I, writing M=I+εH+ε²K/2+…, one must use

N′=−H, N″=2H²−K.                                           (5.4)

In arbitrary coordinates these are −N0HN0 and2N0HN0HN0−N0KN0. Likewise q_f=p_f/(1−p_f·g) is differentiated with this same g. These are exactly the actual-COM and inverse terms retained in the parent; the new reduction removes redundant scalar tests, not these terms.

## 6. A genuine private-facet rescue class

This theorem supplies an actual realization-space sufficient class. It does not presume that any first-layer S1U1 body belongs to it.

Call a true facet completely plane-movable when all its vertices have degree3. Its normalized raw pole may then vary in all three coordinates while all other facet poles are fixed: affected vertices are the intersections of their three genuine planes. Nonsimple vertices are not incident to this moving plane. Strict nonincidence slacks preserve the true lattice for sufficiently small changes.

Choose a compressed first-order selector f1,…,fk from Section4. For a primal row its direct footprint is its two endpoint vertices. For a polar row its direct footprint is its two facet poles. Positive normalization of a row does not change its first derivative at its zero.

### Theorem 6.1: one private contact meeting every positive metric dependency

Suppose two distinct true facets R,F are completely plane-movable and one selected row f_a satisfies all of the following.

1. R avoids every direct footprint: it contains no endpoint of a selected primal row and is neither pole of any selected polar row.
2. F avoids the direct footprints of every selected row other than f_a.
3. F controls f_a in one of these genuine ways:
   * f_a is a polar row Q_FG from a weakEF, or the chosen dominant polar row of an obtuseVF;
   * f_a is a primal row P_vw at a VE and F contains its true exposed edge[v,w];
   * f_a is the chosen primal row at an acute or rightVF, and F is its bearing facet.
4. Every nonzero positive dependence among the frozen-geometry metric derivatives uses rowa with positive weight. Equivalently, if T_i is the symmetric matrix satisfying df_i(H)=T_i:H for a metric variation, then

λ≥0, Σ_i λ_i T_i=0, λ≠0 ⇒ λ_a>0.                           (6.1)

Then the full physical packet admits a true same-lattice first-order resolution. Every original strict equilibrium label is retained. If the input is actual weak-inclusive S1U1, the resulting bodies are proper110 of the same type.

Condition(6.1) concerns the entire nonnegative metric-stress cone. It is equivalent to strict metric feasibility of the rows other than a, not to checking one convenient dependency. If the complete packet was already metric-feasible, no shape actuation is needed.

### Proof with the actual uniform centroid

Work at the initial physical normalization g=0,M=N=I. For normalized raw pole velocities w_f, the moving uniform centroid obeys

g′=−Σ_f d_f T_f w_f,
d_f=Area(F_f)/(Vol(P)|p_f|), T_f=E_Ff[xxᵀ].                 (6.2)

These are genuine area moments. For a true facet, T_f is positive definite: a nonzero linear form cannot vanish on its entire affine plane, since that plane does not contain0. Thus the partial COM derivative in the three parameters of R is the invertible matrix −d_R T_R.

The implicit function theorem adjusts the pole of R to keep the **actual uniformly filled COM exactly0** while F is varied. This is not an arbitrary change of reference. Because R avoids every footprint, that correction has no direct effect on any selected row. Formula(6.2) is the parent's full moving-body derivative, here used as a genuine actuator.

For a polar row Q_FG, move p_F with velocity−p_F. With p_G fixed and COM corrected,

Q_FG′=(p_G−2p_F)·(−p_F)=|p_F|²>0,

using the active equality p_F·p_G=|p_F|².

For a primal row P_vw, choose a pole velocity h with h·v=0,h·w=−1. Such h exists because v,w are independent. The source v stays fixed. At the simple targetw, let d be the true edge direction towards its third neighbor outsideF. The two other planes atw stay fixed, giving

w′=d/(p_F·d).

Both p_F·d and v·d are strictly negative. For VE the radial support exposes precisely[v,w]; forVF it exposes F, and d leaves that facet. Hence

P_vw′=(v·d)/(p_F·d)>0.                                     (6.3)

AtVF the stipulated bearing-facet choice is essential; moving the other incident facet can leave d inside the radial supporting facet and give zero instead.

Let ψ be this genuine COM-corrected shape direction. It has df_a(ψ)>0 and df_i(ψ)=0 for i≠a. By(6.1), the remaining metric rows admit a common H with T_i:H>0. Add a sufficiently large fixed positive multiple of ψ to this metric direction to make rowa positive too. For a sufficiently small arc parameter the same metric stays SPD, its polar metric is its actual inverse, all old nonzero signs persist, and the flag results provide all missing VF exits. The input radial-index theorem then excludes new saddles and weak points.

This construction also proves directly that no full realization-space positive stress can remain: such a stress would first be a metric stress, hence have λ_a>0, but its evaluation on ψ would be λ_a df_a(ψ)>0, not zero.

### Why many independent private planes are not available in E17

Every genuine10/17/9 body has at most two completely plane-movable facets.

Indeed Σ_v(deg(v)−3)=4. The possible degree profiles of nonsimple vertices are

(7), (6,4), (5,5), (5,4,4), (4,4,4,4).

Two distinct true vertices belong to at most two common true facets. In the first four cases the union of the facets incident to nonsimple vertices consequently has size at least7,8,8,7, respectively.

For the last case, suppose those four degree4 vertices used at most six facets. Their four incidence sets, each of size4 in a six-element universe, would have pairwise intersections at most2. Their two-element complements would therefore be pairwise disjoint, requiring eight elements in a six-element universe. Contradiction. So this union also has at least seven facets.

Only the at most two remaining facets can be completely plane-movable. This is a true-incidence theorem, independent of COM or M. The small exact set-system audit in the source checks the final finite combinatorial step, but the proof above does not depend on sampling.

Therefore one distinct private plane per contact plus a separate COM controller cannot address arbitrary first-layer packets. Theorem6.1 uses only two planes and resolves the other contacts through their common metric cone. It does not claim that those two planes or the required footprints always exist.

On the parent's actual strict547 four-contact control, the only completely plane-movable facet is F8=(7,5,6). It meets the target5 of P05, so there is no footprint-avoiding COM plane. The private-facet criterion is inconclusive there, while the parent's genuine full-shape rescue remains valid. This is an explicit limit of this sufficient class, not an actual obstruction. The code retains the literal parent incidence and rows without renaming the object.

## 7. Actual right-VF controls: the missing term changes the physics

These controls start at the supplied homogeneous tetrahedron

Y0=(1,0,0), Y1=(1,1,0), Y2=(1,0,1), Y3=(−3,−1,−1).

Its actual COM is0, M=N=I, strict counts334, and there is one physicalVF at vertex0/facet012, represented on two weak edges.

For rational k,A,B and ε define

u1=Aε²+Bε³, u2=−ε,
v=(1,u1+kεu2,u2),
e1=(0,1,0), e2=(0,kε,1),
Y0=v, Y1=v+e1, Y2=v+e2,
Y3=−Y0−Y1−Y2.                                              (7.1)

All bodies are uniformly filled tetrahedra with the same true lattice. Their actual COM is identically0 and Vol=2/3: the edge determinant is identically−4. The common metric is I throughout. The pole of012 and its foot are fixed at(1,0,0), and

G=[[1,kε],[kε,1+k²ε²]],
P01=(A−k)ε²+Bε³,
P02=−ε+(kA−k²)ε³+kBε⁴,
Q02/(sδ2)=u1, Q01/(sδ1)=u2.                               (7.2)

At ε=0 the only four zero rows are P01,P02,Q01,Q02. All20 other primitives keep their original strict signs on every curve below, for the **whole interval**0<ε≤1/1000.

| Name | (k,A,B) | Strict counts on the positive interval | Physical weak points | Consequence |
|---|---|---|---|---|
| OBTUSE_PRIMAL_FALSE_RESCUE | (−2,−1,0) |435|0|P01>0, but both u entries are negative: a new strict stable facet appears.|
| ACUTE_DUAL_FALSE_RESCUE | (2,1,0) |345|0|u1>0, but both primal exits are negative: a new strict unstable vertex appears.|
| CORRECT_SECOND_JET | (2,3,0) |334|0|Both required exits are strictly positive at second order; original strict labels persist.|
| THRESHOLD_EQUALITY_ONE_VE | (2,2,0) |334|1|P01 remains identically zero; VF changes to oneVE on01.|
| THIRD_ORDER_AFTER_EQUALITY | (2,2,1) |334|0|P01=ε³; the same first and second jets as the preceding curve are rescued at third order.|

Here α=(0,−1), δ=k, a=1 and β1=2A, so the sharp threshold is β1>max(0,2k). The table tests exactly this distinction. In particular weak freedom alone is not preservation of S1U1: the first two curves remove the weak point but create a new strict extremum and a saddle.

The new curves are tetrahedral and hence affinely related. They are deliberately **not** evidence of additional non-affine E17 shape freedom or of an obstruction at an S1U1 body. They are actual homogeneous countercontrols to the erroneous right-corner second-order reductions. Nor is the last curve a body for which all possible first/second-order rescues fail; it concerns the specified jets only.

The interval proof checks129 rational positive conditions with626 strictly positive Bernstein numerator/denominator coefficients, including exact inverse power reconstruction. All poles, normalized flag multipliers, rows, orders, signs, actual endpoint COMs and complete physical censuses are regenerated from the source. No finite sampling substitutes for the interval statements.

## 8. Remaining actual obstruction

The new source removes hidden strict saddles from the target. The flag identities further remove artificial conflicts between independently selected primal and polar VF exits. At a right corner, however, a prescribed motion can couple a second-order mismatch to a first-order changing edge angle; that is a real same-metric geometric effect, not a selector artifact.

The unresolved universal step is now more specific. For each actual S1U1 packet, does some compressed selector admit a full first-order direction, or some true velocity and acceleration satisfy the threshold-adjusted all-cone test(5.2)? If not, a genuine obstruction must survive the exact flag identities, the true incidence tangent space, and the actual surface-moment COM loads. A stress seen only on the metric or projective subspace is still insufficient.

The private-facet theorem closes its stated actual geometric class, but I have not proved that every first-layer packet has its controller geometry or its stress-support property. The at-most-two theorem explains one concrete limitation of attempting to obtain universal rescue from independently free facets. Coupled changes involving nonsimple stars and genuine polygon planarity remain necessary outside that class.

No feasible weak S1U1 source, actual nonregularizable S1U1 packet, universal second-order guarantee, or proper110 density theorem is supplied. The parent's strict547 and mixed-six controls retain their own non-S1U1 meanings; they are not promoted into evidence in the target class.

## 9. Recovery and verification

Save the complete source below as `vf_packet.py`, UTF-8, LF, final newline. Dependencies: CPython3.13.5, SymPy1.14.0; assertions enabled. All proof calculations use exact rational/integer arithmetic. There are no input files, numerical optimizers, random seeds or external data dependencies.

Commands:

python -B vf_packet.py build
python -B vf_packet.py check

Expected terminal marker:

VF_PACKET_COMPRESSION_RIGHT_JET_ACTUAL_COM_PASS

Final source:9837 bytes, SHA-256 `7c7e4c5217665f6e9fd1637553eaed0c3c42a02500138359b51c4df670d9ef8d`.
Generated report:153528 bytes, SHA-256 `91d3da1ee8ab7cee7753e07807c168f446642498b453befc8ce4b0f11c746710`.

Normal build/check and a fresh source-only build/check completed with exit0, the terminal marker and identical source/report pins. The general geometric theorems are proved above, not inferred from these controls. No independent coordinator replay or proof-assistant formalization is claimed.

Convenience copies: source (`vf_packet.py`), exact report (`vf_packet_report.json`), observed replay receipts (`replay_receipts.json`). The literal source is sufficient without these links.

```python
"""VF_PACKET_COMPRESSION_AND_RIGHT_JET_CORRECTION_V1.
CPython 3.13.5 / SymPy 1.14.0, exact rational arithmetic.
Actual control parent: [internal-source-reference], uniform tetraVF.
Fullshape incidence parent: minimum-0227,
SHA256 57bf2cc803fdd3e5ace5587e000d4b1b6372f42306aaff28e467e2b94f1ca8db.
No external input file, network, random seed or numerical optimizer.
python -B vf_packet.py build ; python -B vf_packet.py check
"""
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,json,sys
import sympy as S
R=S.Rational
EPS=R(1,1000)
FACES=tuple(combinations(range(4),3))

def V(v):return S.Matrix(v)
def scalar(x):return S.factor(x)
def body(e,k,A,B):
 u1=A*e**2+B*e**3;u2=-e
 a=V((1,u1+k*e*u2,u2));edge1=V((0,1,0));edge2=V((0,k*e,1))
 x=[a,a+edge1,a+edge2];x.append(-sum(x,S.zeros(3,1)))
 return x

def geometry(x):
 assert sum(x,S.zeros(3,1))==S.zeros(3,1)
 determinant=S.Matrix.hstack(*(x[i]-x[0] for i in (1,2,3))).det()
 assert S.expand(determinant)==-4
 q=[(S.Matrix.vstack(*(x[i].T for i in f)).inv()*S.ones(3,1)).applyfunc(S.factor) for f in FACES]
 for f,p in zip(FACES,q):
  assert all(S.cancel(p.dot(x[i])-1)==0 for i in f)
  assert S.cancel(p.dot(x[next(i for i in range(4) if i not in f)])+3)==0
 rows={}
 for i in range(4):
  for j in range(4):
   if i!=j:rows[('P',i,j)]=S.factor(x[i].dot(x[j]-x[i]))
 for f in range(4):
  for h in range(4):
   if f!=h:rows[('Q',f,h)]=S.factor(q[f].dot(q[h]-q[f]))
 return q,rows

def census(x):
 q,rows=geometry(x)
 stable=[f for f in range(4) if max(rows[('Q',f,h)] for h in range(4) if h!=f)<0]
 unstable=[i for i in range(4) if max(rows[('P',i,j)] for j in range(4) if j!=i)<0]
 weakv=[i for i in range(4) if max(rows[('P',i,j)] for j in range(4) if j!=i)==0]
 weakf=[f for f in range(4) if max(rows[('Q',f,h)] for h in range(4) if h!=f)==0]
 saddles=[];weakedges=[];primitives=[]
 for i,j in combinations(range(4),2):
  f,h=[a for a,face in enumerate(FACES) if i in face and j in face]
  pp=[rows[('P',i,j)],rows[('P',j,i)],rows[('Q',f,h)],rows[('Q',h,f)]]
  primitives.append([i,j,f,h,pp])
  if max(pp)<0:saddles.append([i,j])
  elif max(pp)==0:weakedges.append([i,j])
 vf=[]
 for f in weakf:
  foot=q[f]/q[f].dot(q[f])
  for i in weakv:
   if i in FACES[f] and foot==x[i]:vf.append([i,f])
 counts=[len(stable),len(unstable),len(saddles)]
 assert counts[0]+counts[1]-counts[2]==2
 return dict(vertices=x,faces=FACES,volume=R(2,3),centroid=S.zeros(3,1),
             M=S.eye(3),N=S.eye(3),poles=q,counts=counts,stable=stable,unstable=unstable,
             saddles=saddles,weak_vertices=weakv,weak_facets=weakf,weak_edges=weakedges,
             VF=vf,physical_weak_count=len(weakv)+len(weakf)-len(vf),primitives=primitives)

def positive(e,f):
 n,d=map(lambda a:S.Poly(a,e),S.fraction(S.cancel(f)))
 if d.eval(0)<0:n,d=-n,-d
 assert n.eval(0)>0 and d.eval(0)>0
 rec=[]
 for p in (n,d):
  degree=p.degree();power=list(reversed(p.all_coeffs()))
  bb=[sum(power[j]*EPS**j*R(comb(i,j),comb(degree,j)) for j in range(i+1)) for i in range(degree+1)]
  assert min(bb)>0
  for k in range(degree+1):
   assert sum(bb[j]*comb(degree,j)*comb(degree-j,k-j)*(-1)**(k-j) for j in range(k+1))==power[k]*EPS**k
  rec.append(dict(power=power,bernstein=bb))
 return rec

def symbolic_identities():
 a,b,c,u,v=S.symbols('a b c u v')
 G=S.Matrix([[a,c],[c,b]]);w=V((u,v));p=G*w
 assert S.expand(p[0]*u+p[1]*v-(a*u*u+2*c*u*v+b*v*v))==0
 # Normalize mixed polar rows by their true positive geometric multipliers.
 # At a right VF, first u=(0,alpha2), so P1''/a=beta1+2*c'*alpha2/a.
 e,alpha2,beta1,beta2,adot,bdot,cdot=S.symbols('e alpha2 beta1 beta2 adot bdot cdot')
 gg=S.Matrix([[a+e*adot,e*cdot],[e*cdot,b+e*bdot]])
 ww=V((e*e*beta1/2,e*alpha2+e*e*beta2/2));pp=gg*ww
 assert S.expand(S.diff(pp[0],e,2).subs(e,0)-a*beta1-2*cdot*alpha2)==0
 assert S.diff(pp[0],e).subs(e,0)==0
 # Full inverse, including the mandatory quadratic inverse term.
 H=S.Matrix(3,3,lambda i,j:S.Symbol('h%d%d'%(min(i,j),max(i,j))))
 K=S.Matrix(3,3,lambda i,j:S.Symbol('k%d%d'%(min(i,j),max(i,j))))
 prod=(S.eye(3)+e*H+e*e*K/2)*(S.eye(3)-e*H+e*e*(H*H-K/2))
 assert prod.subs(e,0)==S.eye(3)
 assert prod.diff(e).subs(e,0)==S.zeros(3)
 assert prod.diff(e,2).subs(e,0)==S.zeros(3)
 return dict(energy='P1*u1+P2*u2=u^T G u',right_second='P1_second=a*beta1+2*cdot*alpha2')

def first_layer_movable_facet_bound():
 # Sum(degree(v)-3)=4. Any two distinct vertices share at most two true facets.
 profiles=((7,),(6,4),(5,5),(5,4,4),(4,4,4,4))
 assert all(sum(d-3 for d in profile)==4 for profile in profiles)
 lower=(7,8,8,7,7)
 # The sole nontrivial six-facet possibility is four four-element incidence sets.
 sets=[set(x) for x in combinations(range(6),4)]
 admissible=[ix for ix in combinations(range(len(sets)),4)
             if all(len(sets[i]&sets[j])<=2 for i,j in combinations(ix,2))]
 assert admissible==[]
 return dict(nonsimple_degree_profiles=profiles,incident_facet_union_lower=lower,
             maximum_plane_movable_facets=2,six_facet_set_systems_checked=1365)

def parent_footprint_test():
 faces=((2,6,5,0,8,1,3),(4,0,5,7),(9,0,4),(9,8,0),
        (3,1,4),(1,8,9,4),(4,2,3),(4,7,6,2),(7,5,6))
 rows=(('Q',1,2),('P',0,5),('P',1,8),('P',2,3))
 degrees=[sum(i in f for f in faces) for i in range(10)]
 simple=[f for f,ids in enumerate(faces) if all(degrees[i]==3 for i in ids)]
 free=[f for f in simple if all((f not in row[1:] if row[0]=='Q' else not(set(faces[f])&set(row[1:]))) for row in rows)]
 assert simple==[8] and free==[]
 return dict(faces=faces,selected_rows=rows,vertex_degrees=degrees,plane_movable_faces=simple,
             unused_COM_controller_faces=free,status='private-plane criterion inconclusive; parent fullshape rescue is valid')

def main():
 assert __debug__ and sys.version_info[:3]==(3,13,5) and S.__version__=='1.14.0'
 assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
 e=S.symbols('e')
 baseX=body(R(0),R(0),R(0),R(0));base=census(baseX)
 assert base['counts']==[3,3,4] and base['VF']==[[0,0]] and base['physical_weak_count']==1
 assert base['weak_edges']==[[0,1],[0,2]]
 _,base_rows=geometry(baseX)
 zeroes={row for row,val in base_rows.items() if val==0}
 assert zeroes=={('P',0,1),('P',0,2),('Q',0,1),('Q',0,2)}
 cases=[('OBTUSE_PRIMAL_FALSE_RESCUE',-2,-1,0,[4,3,5],0),
        ('ACUTE_DUAL_FALSE_RESCUE',2,1,0,[3,4,5],0),
        ('CORRECT_SECOND_JET',2,3,0,[3,3,4],0),
        ('THRESHOLD_EQUALITY_ONE_VE',2,2,0,[3,3,4],1),
        ('THIRD_ORDER_AFTER_EQUALITY',2,2,1,[3,3,4],0)]
 out=dict(parent='[internal-source-reference]',epsilon_max=EPS,base=base,
          identities=symbolic_identities(),movable_facet_bound=first_layer_movable_facet_bound(),
          private_plane_limit=parent_footprint_test(),cases={})
 total=0;coeffs=0
 for name,k,A,B,expected,weak in cases:
  k,A,B=map(R,(k,A,B));x=body(e,k,A,B);q,rows=geometry(x)
  edge1=x[1]-x[0];edge2=x[2]-x[0];G=S.Matrix([[edge1.dot(edge1),edge1.dot(edge2)],[edge2.dot(edge1),edge2.dot(edge2)]])
  u=V((A*e*e+B*e**3,-e));foot=q[0]/q[0].dot(q[0]);EE=S.Matrix.hstack(edge1,edge2)
  assert (x[0]-foot-EE*u).applyfunc(S.expand)==S.zeros(3,1)
  s=q[0].dot(q[0]);delta1=-(q[1]-q[0]).dot(edge2);delta2=-(q[2]-q[0]).dot(edge1)
  assert S.cancel(rows[('Q',0,2)]/(s*delta2)-u[0])==0
  assert S.cancel(rows[('Q',0,1)]/(s*delta1)-u[1])==0
  assert (G*u-V((rows[('P',0,1)],rows[('P',0,2)]))).applyfunc(S.cancel)==S.zeros(2,1)
  assert S.expand(rows[('P',0,1)]-(A-k)*e*e-B*e**3)==0
  guards=[['delta1',positive(e,delta1)],['delta2',positive(e,delta2)]]
  signs={};orders={}
  for row,val in rows.items():
   if val==0:signs[row]=0;orders[row]=None;continue
   n,d=map(lambda v:S.Poly(v,e),S.fraction(S.cancel(val)))
   if d.eval(0)<0:n,d=-n,-d
   order=min(ix[0] for ix,c in n.terms());sign=S.sign(n.nth(order))
   guards.append([row,positive(e,sign*val/e**order)])
   signs[row]=sign;orders[row]=order
   if row not in zeroes:assert order==0 and sign==S.sign(base_rows[row])
  endpoint=census([v.subs(e,EPS) for v in x]);assert endpoint['counts']==expected
  assert endpoint['physical_weak_count']==weak
  for row,val in geometry([v.subs(e,EPS) for v in x])[1].items():assert S.sign(val)==signs[row]
  theta=max(R(0),2*k);beta1=2*A
  out['cases'][name]=dict(parameters=[k,A,B],vertex_polynomials=x,Gram=G,mismatch=u,
                         normalized_polar=[u[0],u[1]],rows=[[key,v] for key,v in rows.items()],
                         signs=[[key,v] for key,v in signs.items()],orders=[[key,v] for key,v in orders.items()],
                         right_jet=dict(alpha=[0,-1],beta1=beta1,corner_derivative=k,threshold=theta,
                                        strict_second_pass=bool(beta1>theta)),
                         endpoint=endpoint,guards=guards)
  total+=len(guards);coeffs+=sum(len(t['bernstein']) for tag,g in guards for t in g)
 assert (total,coeffs)==(129,626)
 out['guard_count']=total;out['positive_coefficient_count']=coeffs
 text=json.dumps(clean(out),sort_keys=True,indent=2)+'\n';target=Path('vf_packet_report.json')
 if sys.argv[1]=='build':target.write_text(text,encoding='utf-8')
 else:assert target.read_text(encoding='utf-8')==text
 print('VF_PACKET_COMPRESSION_RIGHT_JET_ACTUAL_COM_PASS')
 print('GUARDS',total,'POSITIVE_COEFFICIENTS',coeffs)
 for name,d in out['cases'].items():print(name,d['endpoint']['counts'],d['endpoint']['physical_weak_count'])
 for path in (Path(__file__),target):
  data=path.read_bytes();print(path.name,len(data),hashlib.sha256(data).hexdigest())

def clean(x):
 if isinstance(x,S.MatrixBase):return [[clean(v) for v in row] for row in x.tolist()]
 if isinstance(x,S.Rational):return str(x)
 if isinstance(x,S.Basic):return str(x)
 if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [clean(v) for v in x]
 return x
if __name__=='__main__':main()
```
