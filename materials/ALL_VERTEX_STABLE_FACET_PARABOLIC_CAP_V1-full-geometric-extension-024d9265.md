# material-024d92650bd9

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ALL_VERTEX_STABLE_FACET_PARABOLIC_CAP_V1

## Source and scope

This is a coordinator's direct generalization of the actual two-apex polar-ball argument in the complete literal result minimum-0092, read from cursor0 throughEOF with SHA25633edfe049eef1952a3ac3a5789eb77f540643321f9e44f7c8671928cf1039d1e and title TWO_APEX_BISECTOR_REFLECTION_AND_BASE_ROOT_CAP_V1. It is proved in full below; neither the source transport nor an earlier summary is a mathematical verification. No novelty or priority claim is made.

The extension applies to every full-dimensional convex3polytope, with any specified reference point in its interior. No bound on the number of vertices or facets, no two-apex hypothesis, no chosen complementary tree, and no volume-centroid identity is needed. It therefore applies in particular to the actual uniform-volume centroid without replacing that point by a free reference. It is a sufficient exclusion of strict monostability with no extra weak contacts, not a proof of the global minimum of class110. No new polyhedral construction or computational data is asserted. The minimum bracket remains34<=C_min<=622.

## 1. Notation and theorem

Translate the specified interior reference point to0. Let M be one positive-definite physical metric on primal coordinates and N=M^-1 its one reciprocal polar metric. Write the true maximal facet inequalities of P as q_F.x<=1. For a facet B set q=q_B, k=sqrt(q^T N q)>0. For each actual vertex a outside B put

p_a=q.a<1,
Delta_B(a)=(2-p_a)^2-k^2(a^T M a).

THEOREM. Suppose B is strictly stable, meaning that its physical perpendicular foot f_B=Nq/k^2 lies in the relative interior of the true facet B. Suppose Delta_B(a)>=0 for EVERY vertex a outside B. Then P has either a second strictly stable facet or an additional genuine weak edge-facet equilibrium point distinct from f_B. If all the displayed inequalities are strict, there is a second strictly stable facet.

Consequently, a polytope with a unique strictly stable facet B and no additional weak equilibria must have at least one actual vertex a outside B satisfying Delta_B(a)<0. This is only a necessary condition for that mechanical class: a violating vertex need not be adjacent to the stable facet, and no sufficiency or minimality follows.

## 2. Why every side facet is constrained

Every true maximal facet F other than B contains at least one actual vertex a outside B. Otherwise all its vertices, and hence its entire two-dimensional facet, would lie in the supporting plane aff(B). That supporting plane cuts out the one maximal facet B, so F would equal B. This observation is the sole place where the original two-apex argument used the list of exterior vertices. It remains valid for any number of exterior vertices.

Use the dual-metric diametral ball

D_B={r:(r-q/2)^T N(r-q/2)<=k^2/4}.

Its support function evaluated on a primal vector a is

max_(r in D_B) a.r = [q.a+k sqrt(a^T M a)]/2.

This follows by the reciprocal-metric Cauchy inequality, and fixes the primal/dual pairing without introducing an independent polar metric. Since p_a<1 implies2-p_a>0, Delta_B(a)>=0 is exactly the statement that this maximum is<=1. A nonzero functional a.r is strictly smaller than its maximum at every point of the interior of D_B.

Let r=q_F be the pole of any F!=B, and choose an exterior vertex a in F. Its actual incidence gives a.r=1. Hence r cannot lie inside D_B. Therefore

r^T Nq <= r^T Nr                                      (1)

for EVERY pole r other than q. If all Delta_B(a)>0, the support maximum is<1 for the chosen exterior vertex, so r is outside even the closed ball and every inequality(1) is strict. No completion moments, artificial incidence or numerical tolerances enter this argument.

## 3. Selecting a genuine second stable facet or a genuine weak point

Choose a pole r!=q having largest N-norm among all poles other than q. For any other pole s distinct from r,q,

r^T Ns <= |r|_N |s|_N <= |r|_N^2,

and equality throughout would require s=r. The poles represent distinct true maximal facets, so

r^T Ns < r^T Nr for every s!=r,q.                     (2)

If inequality(1) for this r is strict, the point f=Nr/(r^T Nr) satisfies r.f=1 and s.f<1 for every other facet pole s, including q. It lies in the relative interior of F and is its physical perpendicular foot, so F is strictly stable. Because F!=B, this is a second strict stable equilibrium.

If inequality(1) is an equality, define the same f. Then

r.f=q.f=1,
s.f<1 for every s distinct from r,q.

Thus f lies on exactly the two true maximal facets F and B and no other facet. In a full-dimensional3polytope this is precisely the relative interior of the genuine common edge e=F intersect B. In particular F and B are actually adjacent; adjacency was not assumed merely from the equality of two formal rows. The point f is a nonzero positive multiple, after applying M, of the outward normal r of F. Hence it is a weak edge-facet resting contact on the boundary of the edge normal cone, not a harmless zero whose edge is mechanically inactive.

For a complete primitive check, write the two distinct endpoints of e as u,v and f=u+t(v-u),0<t<1. Because r.(v-u)=0 and Mf=r/(r^T Nr), f^T M(v-u)=0. Therefore

u^T M(v-u)=-t (v-u)^T M(v-u)<0,
v^T M(u-v)=-(1-t)(v-u)^T M(v-u)<0.

The two polar primitives are

r^T N(q-r)=0,
q^T N(r-q)=r^T Nr-q^T Nq<0.

The final strict inequality follows from r^T Nq=r^T Nr and reciprocal-metric Cauchy: |q|_N>=|r|_N, and equality would force q=r, impossible for distinct facets. Thus the four actual edge primitives have signs(-,-,0,-), up to swapping the two facet positions. This is a genuine simple edge-facet packet in the relative interior of the true edge. It is distinct from the original strict equilibrium f_B in the relative interior of B. This proves the theorem, including its exact weak boundary.

The boundary does NOT exclude a count of strict equilibria S_nd=1,U_nd=1,H_nd=0 accompanied by extra weak resting points. Its exclusion is for the requested strict class with no extra weak equilibria. Replacing this conclusion by an exclusion of every weak complementary tree would be incorrect.

## 4. Geometric form: a paraboloid based at the stable facet

Apply a single physical whitening to make M=I, and use orthonormal coordinates with the reference point0, aff(B) at height-h, h=1/k>0, and q=(0,0,-1/h). Write an exterior vertex as a=(u,H-h), where H>0 is its true height above B and u is its horizontal displacement from the perpendicular projection of0 onto aff(B). Then p_a=1-H/h, and direct expansion gives

Delta_B(a)=4H/h-|u|^2/h^2.

Thus the closed hypothesis is exactly

|u|^2<=4hH for every vertex outside B.                (3)

A strict no-extra-weak monostable polytope must have an exterior vertex outside this closed paraboloid, |u|^2>4hH. This need not put its projection outside the polygon B itself: condition(3) and ordinary projection-overhang are different geometric tests. No equivalence between them is asserted.

The theorem is unchanged by expressing the same physical body in another affine chart with the corresponding single M and N=M^-1. It does not say that arbitrary active affine changes preserve stability or the cap inequalities; those physical quantities must be recomputed after an actual deformation and, for an own-centred body, after recomputing the true centroid.

## 5. A quantitative strict guard

There is also an explicit uniform polar margin when every Delta_B(a)>0. Define, over the finite set of vertices a outside B,

eta=min_a [2-p_a-k|a|_M]/[2|a|_M] >0.

For any true side pole r and any incident exterior vertex a, a.r=1 exceeds the support of D_B by [2-p_a-k|a|_M]/2. The dual-metric distance from r to D_B is therefore at least this gap divided by |a|_M, hence at least eta. Since D_B is a ball,

|r-q/2|_N >= k/2+eta.

It follows that every actual side-to-B primitive has the strict upper bound

r^T N(q-r) <= -(k eta+eta^2)<0.                      (4)

Thus the open cap class has a true finite margin, not merely an infinitesimal or generic argument. Formula(4) may be used as a sufficient actual-geometry filter in a future search. It is not a lower bound on the number of vertices and does not identify any root class in an old census without a literal correspondence.

## 6. Limits, exact dependencies and continuation

The entire mathematical proof is this material; there is no missing code or computed-object recovery. The full preceding two-apex source minimum-0092 contains seven separately recoverable actual10/17/9 controls and the full two-apex reflection/bisector theorem. Their coordinates, mechanics and code remain literal in that immutable result and are not copied or relabeled here. This generalization does not turn any of its S/U/H=2/2/2 controls into a110-body.

The useful new global conclusion is: every unique strict stable facet without extra weak points needs a genuinely far transverse vertex in the precise parabolic sense(3). The theorem does not prove that this requirement is incompatible with the actual volume centroid, a unique unstable point, or the f-vector10/17/9. Those simultaneous constraints remain the next geometric question. The accepted lower prohibitionC>=34 and the separate exactC622 attaining construction remain nonmatching endpoints of the minimum problem.
