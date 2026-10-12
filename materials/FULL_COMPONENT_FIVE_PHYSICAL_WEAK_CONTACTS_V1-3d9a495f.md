# material-3d9a495f5485

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FULL_COMPONENT_FIVE_PHYSICAL_WEAK_CONTACTS_V1

## Status and dependency
New coordinator analytic theorem. It strengthens the finite-five-zero-arrow alternative in the completely read immutable result minimum-0218, SHA256 d2708a7da6c6867a9f47f2960251aa8600f88769bc3d919060ca8719add3a723 (HEX6_FULL_RANK_NORMAL_PORT_AND_FIVE_CONTACT_ALTERNATIVE_V8). No computation, new body, all-shape exclusion, independent replay, or changed global bound is claimed. The proof below is complete and does not require the earlier sandbox. It applies to ANY fixed full-dimensional convex 3-polytope with its specified reference strictly inside; in the research application this reference MUST be its actual uniform volume centroid.

The improvement is to take an exposed vertex of the convex hull of an ENTIRE weak-U1 component, rather than a vertex of one preselected tree polytope. This forces at least FIVE GENUINE weak-unstable source vertices, not merely five vanishing edge primitives. A zero arrow at a source which has another positive escape is not such a contact.

## 1. Definitions and exact physical meaning
Let P=conv(X_0,...,X_{n-1}), with all X_i true vertices, 0 strictly inside P, and the actual true-edge graph fixed. Put A_ij=sym[X_i(X_j-X_i)^T] for each true directed edge i->j, with sym(B)=(B+B^T)/2. Let D_ij(M)=A_ij:M=X_i^T M(X_j-X_i), for symmetric M. Normalize physical SPD matrices by tr(M)=1. The physical affine image has vertex vectors M^(1/2) X_i; uniform centring is preserved by this linear transformation when the original reference is the true volume centroid.

At SPD M, vertex i is strictly unstable exactly when ALL outgoing D_ij(M)<0. It is genuinely weak unstable (and not strict) exactly when ALL outgoing D_ij(M)<=0 and at least one equals zero. The local inequalities on all true incident edges imply the corresponding global supporting-plane inequality, because these incident edge directions generate the tangent cone of a convex polytope at its vertex. Thus this weak predicate is a genuine equilibrium contact; it is not the weaker statement that one selected primitive vanishes.

For every distinct adjacent pair,

  X_j^T M X_j-X_i^T M X_i = 2D_ij(M)+(X_j-X_i)^T M(X_j-X_i).

Consequently every weak escape D_ij>=0 strictly increases the M-radius when M is SPD. Any selection of one weak escape at every nonroot vertex, with no arrow at root r, is automatically a true arborescence to r. Conversely such a weak tree makes r the unique strict unstable vertex: r is the unique greatest-radius vertex, hence all its outgoing primitives are strictly negative; every other vertex has a nonnegative escape. Other weak equilibria are allowed in this auxiliary weak-U1 set.

For each true rooted arborescence T toward r, define

  K_T={M PSD: tr(M)=1, D_e(M)>=0 for every e in T}.

Let W_r be the finite union of all K_T. It is compact. Its SPD points are precisely the metrics with sole STRICT unstable vertex r, possibly accompanied by nonroot weak unstable vertices. Its singular points are defined by actual weak rooted trees, not by singular strict-U counts.

## 2. Singular separation and the polyhedral component lemma
No K_T contains a rank-one matrix. Indeed, for M=vv^T with v nonzero, interiority of 0 supplies both positive and negative values t_i=v.X_i. On the positive maximum exposed face, all outgoing weak arrows stay in that face; on the negative minimum exposed face the same holds. These two disjoint closed sets cannot both reach one root. Rank zero is excluded by trace one. Hence every singular member of W_r has rank two.

Let C be a connected component of W_r containing an SPD point and containing NO singular point. Then C is a compact finite union of polytopes wholly inside SPD.

Proof: W_r is a finite union of compact convex sets. Any K_T meeting C lies wholly in C by connectedness. It has an SPD point and no singular point. Define the affine polyhedron

  P_T={M symmetric: tr(M)=1, D_e(M)>=0 for e in T}.

If P_T contained a non-SPD point, the segment from its SPD point to that point would first meet a singular PSD trace-one point, lying in K_T and hence C, a contradiction. Thus P_T=K_T and is compact, so it is a polytope. Every point of C belongs to one of the finitely many K_T meeting C. Therefore C and conv(C) are compact polytopal sets inside SPD. Every vertex of conv(C) belongs to C: conv(C) is the convex hull of the finite union of the vertex sets of those K_T.

This component statement is stronger in scope than fixing one tree. If some OTHER component of W_r meets rank two, it does not invalidate the conclusion for C.

## 3. Five PHYSICAL weak contacts theorem
THEOREM. At every vertex M_* of conv(C), where C is as in Section 2, there are at least five distinct nonroot vertices i satisfying

  D_ij(M_*)<=0 for EVERY true neighbor j,
  D_ij(M_*)=0 for at least one true neighbor j.

Moreover, choose ANY one zero outgoing edge at each such weak source. The chosen arrow matrices span a five-dimensional subspace of Sym(3), all annihilating M_*. Thus five of them are independent and determine the SPD ray M_* uniquely. The five independent sources are genuinely physical weak unstable vertices, unlike a generic vertex of an arbitrary tree polytope.

Proof: Let B be the set of nonroot vertices with no strictly positive escape at M_*. Because M_* belongs to W_r and is SPD, each source in B has a zero escape and all its other escapes are nonpositive. All sources outside B have a strictly positive escape. Choose one zero escape for each i in B and one positive escape for each other nonroot source. By strict radius increase, this is a true arborescence T toward r, and K_T lies in C.

Suppose the chosen zero-arrow matrices had rank at most four. There would be a nonzero symmetric Delta with tr(Delta)=0 annihilated by all these matrices. (The trace functional is independent of these zero rows: they annihilate M_*, whose trace is one.) For sufficiently small epsilon>0 both M_*+epsilon Delta and M_*-epsilon Delta are SPD, preserve all selected zero arrows exactly, and preserve all selected positive arrows. Both lie in K_T subset C. Their midpoint is M_*, contradicting that M_* is a vertex of conv(C).

Therefore these rows have rank at least five. They all annihilate the nonzero M_*, so their rank is exactly five. There must be at least five sources in B, and five independent rows selected from them have distinct sources. No special choice of zero escape was used, proving the ANY-selection assertion. QED.

Corollary: A full-rank weak-U1 component avoiding rank two supplies a five-arrow cofactor candidate which passes BOTH full weak rooted reachability and the physical test that at least five nonroots have no positive escape. Rejecting all such physically critical candidates excludes every singular-disconnected component. It does NOT exclude components reaching unexamined rank-two systems.

The physical condition can be imposed immediately for the five selected sources before complete root reachability is tested. More than five physical weak contacts are possible and must not be discarded. Vanishing cofactor vectors do not exclude a geometry. One must enumerate other independent contact choices or retain the singular alternative.

## 4. Exactly five physical weak sources automatically yield a strict-U1 germ
At M_* as above, suppose B has EXACTLY five members. Choose one zero arrow e_i from each. Their five matrices are independent, so the six equations

  tr(Delta)=0,
  A_ei:Delta=1 for i=1,...,5

have a unique symmetric solution. Then for every sufficiently small epsilon>0,

  M_epsilon=M_*+epsilon Delta

is SPD and has a STRICT positive escape at every nonroot: the selected five zero arrows become epsilon, and the selected positive arrows at other sources remain positive. Thus the same actual body has robust sole-U1 with no weak unstable vertices.

An explicit safe range follows from any rigorous l>0 with M_*>=l I and B0>=||Delta||_op: take epsilon<l/(2B0), and for each previously positive chosen row a=A_e:M_*>0 with b=A_e:Delta<0 also impose epsilon<a/(2|b|). Rows with b>=0 need no bound. These expressions are exact once the body and candidate are exact. At rational actual data the cofactor matrix, Delta, row margins and rational safe epsilon can all be determined by exact arithmetic.

This produces U1, NOT proper110: the SAME reciprocal metric may have multiple stable equilibria and saddles. Generic sufficiently small perturbations within the resulting strict-U1 open set can avoid all finitely many genuine physical weak-contact hypersurfaces. To justify that statement, every true primal arrow polynomial is nonzero as a function on Sym(3); every polar arrow has form q_f^T adj(M)(q_g-q_f), also a nonzero polynomial because inversion maps the SPD cone onto itself and the distinct true poles give a nonzero linear functional in N=M^-1. Avoiding all four true-edge primitives is sufficient, though stronger than necessary, for absence of weak contacts. This genericity statement does not preserve S=1 and is not a census.

## 5. More than five weak sources: exact local strictification alternative
For k=|B|>5, choose one zero edge from each physical weak source. A local strict-U1 perturbation for these choices exists exactly when there is a symmetric Delta with all A_e:Delta>0. Trace zero can be imposed without loss: replace Delta by Delta-tr(Delta) M_*, since every selected A_e annihilates M_*.

If this strict linear system is impossible, the elementary finite-dimensional alternative gives nonnegative coefficients lambda_e, not all zero, with sum lambda_e A_e=0. One can take at most SIX selected zero arrows: the matrices lie in the five-dimensional linear hyperplane {A:A:M_*=0}; a minimal positive dependence there has support at most six. This is an exact local obstruction for those edge choices, not for all choices. Strictification of the full weak system requires a successful choice at every weak source; failure requires coverage of every such choice. There is no positive-semidefinite-kernel side condition here because the base metric M_* is already SPD.

## 6. Application to the literal E17 graph
The V8 graph has edges 01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89. Root0 has 36288 five-source/one-neighbor candidates before cycle rejection, all roots together 106596, as proved in the immutable parent. The six cofactor coordinates of the 5x6 true-arrow row matrix still supply the metric ray. This theorem adds a mechanically meaningful necessary filter: for EACH selected source, EVERY outgoing primitive must be nonpositive at the SPD candidate, not merely the selected arrow zero. Afterwards verify complete graph reachability and count the total weak-unstable source set B.

If exactly five physical weak sources remain, solve the explicit Delta system and obtain a true strict-U1 metric on that SAME actual body; then separately evaluate S,H and all physical weak contacts using its own inverse. If no physically critical candidates survive, conclude only that all U1 components must reach rank-two rooted metrics. A separate complete rank-two theorem is still required for an all-metric body exclusion.

All inequalities must use the actual homogeneous centroid. Replacing the actual star-centred algebraic model by a translated rational source body is a different geometry and must be identified as such, even when the labelled incidence is unchanged.

## 7. Global research disposition
This is an analytic refinement of the full-rank interior search and its physical interpretation. It gives no new excluded E17 realization, no all-type theorem, no actual U1 construction, and no new upper bound. The accepted bracket remains 34<=C_min<=622. Exact attainment and the lower exclusion remain separate unresolved obligations.
