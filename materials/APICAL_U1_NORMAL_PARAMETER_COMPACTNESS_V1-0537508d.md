# material-0537508d170a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# APICAL_U1_NORMAL_PARAMETER_COMPACTNESS_V1

Coordinator analytical theorem. This is a general global consequence of the reciprocal Schur parametrization, not a claim specific to either the degree-five or degree-six examples. It proves that, with the tangential metric and normal footpoint fixed, a prescribed strict unstable vertex can be the only unstable vertex without extra weak contacts only inside an explicitly bounded OPEN interval of the normal parameter. Both singular ends are rigorously excluded, including arbitrary projection ties. The proof requires only that the reference point lie strictly inside a full-dimensional convex polyhedron; in the research problem that point is the actual volume centroid. No density relaxation or coordinate replacement is used.

This material is a complete analytical recovery capsule. No numerical computation, omitted coefficient list, script, new computed object or external theorem beyond elementary convexity and positive-definite quadratic forms is required. It does not increase the global lower bound or construct a proper110 body. Bounds remain34<=Cmin<=622.

## 1. Exact physical coordinates and primitives
Let P have distinct true vertices x_i and interior reference0. Apply one invertible linear coordinate change, transforming the physical metric reciprocally, so the prescribed vertex is A=x_0=e3. Every actual pole incident to A has the form q_j=(p_j,1). Let C=conv{p_j}, the ENTIRE strictly convex polygonal pole face. For any fixed H positive definite in Sym2 and f in R2, every positive normal Schur parameter delta gives

N=[[H,-Hf],[-f^T H,delta+f^T Hf]],
M=N^-1=[[H^-1+ff^T/delta,f/delta],[f^T/delta,1/delta]].

N and M are one mutually inverse physical pair, not independently selected metrics. Put G=H^-1 and, for x_i=(y_i,z_i), define

r_i=y_i^T G y_i,
tau_i=z_i+f.y_i,
a_ij=y_i^T G(y_j-y_i),
b_ij=tau_i(tau_j-tau_i).

For every TRUE directed primal edge i->j,

delta D_ij=delta x_i^T M(x_j-x_i)=a_ij delta+b_ij.                 (1)

The squared metric radius is

delta ||x_i||_M^2=delta r_i+tau_i^2,                             (2)

while delta||A||_M^2=1. A is STRICT unstable iff f lies strictly inside C. Indeed M A=(f,1)/delta, and the interior normal cone at A is exactly the cone over int C. This condition, and every polar arrow within this same face, is independent of delta. In particular f in int C implies tau_i<1 for every nonapical vertex, not just for the neighbors of A.

For an actual pole q_k=(u_k,w_k), put v_k=u_k-w_k f. Its true dual edge primitive is

D^Q_kl=v_k^T H(v_l-v_k)+delta w_k(w_l-w_k).                       (3)

Thus all4E physical primitives are affine functions of delta after multiplying primal ones by the SAME positive delta. Identically zero or harmless zero primitives must not be deleted by declaring the physical body inadmissible; only actual equilibrium conditions matter.

## 2. A negative-support vertex forces a second unstable vertex at the small-normal end
Because0 is interior and the nonzero linear functional tau has tau(A)=1,

tau_* = min_i tau_i < 0.

Among vertices attaining tau_*, choose w with largest r_w. In particular w is not A. For every neighbor j:

* If tau_j>tau_w, then b_wj<0.
* If tau_j=tau_w, then r_j<=r_w, and
  2a_wj=r_j-r_w-||y_j-y_w||_G^2<0.
  The strictness is valid even on a flat support face: y_j=y_w together with equal tau would imply x_j=x_w, contrary to distinct true vertices.

Consequently every neighbor satisfies b_wj<=0, and whenever b_wj=0 it satisfies a_wj<0. Define

L = min_{j neighbor w, a_wj>0} (-b_wj/a_wj),                    (4)

with L=+infinity if that set is empty. Every listed ratio is strictly positive. It follows directly from (1) that w is STRICT unstable for every0<delta<L. If L is finite, all outgoing primitives at w are still nonpositive at delta=L, so w is at least a WEAK additional unstable contact there. If L=+infinity, w is strict unstable for all delta>0.

If A is strict unstable, therefore, the entire interval0<delta<L contains at least two STRICT unstable vertices. A body with A as its unique unstable vertex and no extra weak equilibria must have delta>L. This includes the endpoint exclusion, not just an asymptotic or generic argument. The selection rule resolves ties in the negative support face and needs no conditioning cap.

## 3. Unique instability forces strict global radial dominance
A vertex of globally largest M-radius is strictly unstable: for any different vertex x_j with ||x_j||_M<=||x_i||_M, strict Cauchy-Schwarz with distinct vectors gives

x_i^T M(x_j-x_i)<0.

For equal-radius vectors this is also immediate from -||x_j-x_i||_M^2/2<0. Therefore, if A is the ONLY unstable vertex, it must have strictly larger radius than EVERY other vertex. Otherwise a globally maximizing nonapical vertex is another strict unstable vertex.

Using (2), the necessary inequalities are

delta r_i+tau_i^2<1 for every i!=0.                            (5)

In particular |tau_i|<1 for every nonapical vertex, including those with y_i=0. If any tau_i^2>=1, then for every delta>0 at least one nonapical vertex has radius>=||A||_M. With A strict unstable, there are then at least two strict unstable vertices for ALL delta, so the entire pencil is excluded.

If every |tau_i|<1, define

R = min_{i!=0, r_i>0} (1-tau_i^2)/r_i.                         (6)

Full dimension ensures at least one r_i>0. Thus0<R<infinity, and (5) is equivalent to0<delta<R. For every delta>=R a nonapical vertex has radius>=||A||_M, so some nonapical global maximizer is STRICT unstable; A remains strict unstable because f in int C. The large-normal end is therefore excluded INCLUDING its finite endpoint, with no generic-projection or nonzero-coefficient hypothesis.

Combining (4) and (6), any proper apical-U1 member of the fixed H,f pencil must satisfy

                         L < delta < R.                       (7)

If L=+infinity, or L>=R, the ENTIRE positive pencil is excluded. If L<R, the interval is only necessary; other unstable vertices, weak equilibria, stable-facet requirements and saddles can still exclude all of it. The lower and upper obstructing vertices need not be the same.

There is NO claim that L and R remain uniformly separated from0 andinfinity when H becomes singular, f approaches the boundary, or the actual geometry degenerates. This is exact elimination of the unbounded NORMAL parameter for each fixed physical tangential/footpoint configuration, not a compactness theorem for the full SPD cone.

## 4. An exact convex footpoint filter, and a limitation of radial dominance
The existence of any apical-U1 metric first requires the nonempty open polygon

F_A = {f in int C: z_i+f.y_i>-1 for every i!=0}.                 (8)

The upper inequalities tau_i<1 are already implied by f in int C. Thus F_A is an intersection of the true polar-face interior with explicit open HALFPLANES, independent of H. Empty F_A excludes A as the unique unstable vertex for every SPD metric, though not necessarily other possible roots.

Conversely, for ANY f in F_A and ANY H positive definite, all sufficiently small delta<R make A the unique globally farthest vertex by (5). Yet the negative-support proof produces another STRICT unstable vertex whenever delta<L. Hence every such configuration has an entire nonempty interval

0<delta<min(L,R)

on which A is strict unstable and uniquely globally farthest, but U>=2. This proves that replacing fullU1 by apical instability plus global radial dominance still loses genuine mechanical information, even before centroid or incidence simplifications. It is a general countercontrol mechanism, not a new110 construction.

For rational vertices, rational H and rational f, all the displayed bounds are exact rational numbers or+infinity; no square roots or algebraic root isolation are needed.

## 5. Complete elimination of delta for a specified proper110 root pair
Fix the ACTUAL body, A, H,f and a proposed stable facet S. If f is not in int C, or any |tau_i|>=1, or L>=R, no proper110 metric in the pencil exists. Otherwise restrict to the bounded open interval(L,R).

For each primitive (1) or (3), write its positively scaled value as a delta+b. The strict root-facet conditions are all outgoing dual primitives<0; their intersection is an open interval J, possibly empty, intersected with(L,R). The prescribed A conditions already hold independently of delta.

For every nonroot vertex i define the BAD closed relative interval in delta>0 on which ALL its outgoing primal primitives are<=0. For every nonroot facet define the analogous BAD interval from its outgoing dual primitives. For every true edge ij between facets k,l define its BAD interval by the four inequalities

D^P_ij<=0, D^P_ji<=0, D^Q_kl<=0, D^Q_lk<=0.

Each set is an interval, possibly empty, because it is an intersection of affine half-lines. The edge condition is precisely the closed edge-foot/normal-cone contact condition; its boundary includes endpoint or face degeneracies. Thus it must be excluded for the requested no-extra-weak problem. The same weak point may occur in more than one bad interval, which does not affect their union.

The EXACT admissible normal-parameter set is

J minus the union of all these bad closed intervals.           (9)

This is a finite union of open intervals. Every surviving component yields proper110 with the specified roots under the SAME mutually inverse metric pair; there are no isolated admissible delta values because all required equilibrium/escape conditions are strict. Conversely every proper110 metric in this pencil lies in (9).

All endpoints are obtained by solving individual affine inequalities. Sorting and merging O(V+F+E) intervals eliminates the final parameter; one rational sample per surviving open component suffices when the inputs are rational. Harmless primitive zeros are allowed wherever another required escape primitive is strictly positive. In particular demanding that every primitive be nonzero is not part of the necessary-and-sufficient physical criterion.

This is an analytical specification of an exact finite procedure, not a report that it has already been implemented on a new data set. The earlier full-census Schur source in [internal-source-reference] provides the primitive formulas and concrete four degree-five U1-empty tubes. Those body-specific tubes and traps are NOT transferred to the degree-six hexagon in [internal-source-reference]; only the universal formulas and theorem here transfer.

## 6. Research consequence and remaining task
For the active degree-five and degree-six global branches, the unbounded scalar delta need not be explored by blind sampling or a condition-number cutoff. Each actual body/H/f choice has an explicit rational candidate interval, and the exact proper110 test reduces to a finite interval union. The genuinely unresolved freedoms are the actual completion geometry, H and f, together with the global compatibility of all vertex/facet/edge signs. Neither this normal-parameter reduction nor the sharp five-arrow local theorem solves that full problem.
