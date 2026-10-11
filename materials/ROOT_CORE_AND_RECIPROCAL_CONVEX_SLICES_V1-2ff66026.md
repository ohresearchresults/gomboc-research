# material-2ff66026d671

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ROOT_CORE_AND_RECIPROCAL_CONVEX_SLICES_V1

Coordinator original mathematical synthesis. Two self-contained reductions follow, together with an exact actual-centroid countercontrol. Neither proves a new global edge bound or a proper110 construction. Accepted34<=Cmin<=622 remains unchanged. Symbols U and weak vertex equilibria are distinguished from full stable-face/saddle-edge mechanical counts.

## I. ROOT_SYMMETRIC_HULL_CENTROID_CORE_V1

### I.1 Metric-free eligibility for the unique global radius maximum
Let P=conv(Y_0,...,Y_(n-1)) be full-dimensional, with actual volume centroid g in its interior. Set X_i=Y_i-g and fix a vertex a. The following are equivalent:
(1) There exists SPD M for which X_a^T M X_a is the UNIQUE largest squared vertex radius.
(2) X_a is outside conv{+X_i,-X_i:i!=a}.
(3) There exists a linear functional ell such that ell(X_a)>|ell(X_i)| for every i!=a.
Proof: if X_a belongs to that symmetric hull, norm convexity prohibits a strictly larger M-norm. Conversely strict separation from a compact symmetric convex hull gives(3), with ell(X_a)>0. Set M=ell ell^T+epsilon I. All squared-radius gaps at epsilon0 are strictly positive, so sufficiently small positive epsilon preserves them and makes M SPD. Rational geometry and a rational strict separator permit a rational epsilon.

For any globally farthest vertex i and true neighbour j,
D_ij=X_i^T M(X_j-X_i)=(||X_j||_M²-||X_i||_M²-||X_j-X_i||_M²)/2<0.
EVERY globally farthest vertex is therefore strict U. A body with exactly one strict U has that vertex uniquely globally farthest and must satisfy the eligibility criterion, even if additional weak equilibria are temporarily allowed. The converse is false.

### I.2 The centroid exclusion core is a convex polyhedron
For fixed raw P define the inward tangent cone T_a=cone(P-Y_a) and outward normal cone N_a={ell:ell(Y_a-Y_i)>=0 for all i}. The set of reference centres for which a is ineligible is
C_a=(Y_a+P)/2-T_a.
Equivalently,
g in C_a iff 2ell(g)>=ell(Y_a)+min_i ell(Y_i) for all ell in N_a.

Proof: an eligible separator must strictly expose Y_a and satisfy ell(Y_a+Y_i-2g)>0 for every i!=a. Conversely these inequalities give the strict separator of I.1. If a nonzero boundary direction of N_a has positive midpoint slack, a sufficiently small perturbation toward an interior normal preserves the midpoint slack while making exposure strict. Thus failure of eligibility is exactly the displayed intersection of closed halfspaces, with normal-cone boundary directions included. The lower support of (Y_a+P)/2-T_a is[ell(Y_a)+min_P ell]/2 when ell in N_a, and minus infinity otherwise. This Minkowski sum is a closed polyhedron, and separation identifies the two sets.

Finite exact formula: for every vertex b refine by K_ab=N_a intersect(-N_b). Its extreme rays h impose h dot(Y_a+Y_b-2g)<=0. These finitely many inequalities characterize C_a because the minimum of ell on P is ell(Y_b) in K_ab. Every K_ab is pointed. In dimension3 its rays are obtained from cross products of pairs of independent active constraint normals, testing both signs; lower-dimensional intersections are included. Thus fixed rational raw geometry gives finitely many rational LINEAR inequalities in the actual centroid. Positive midpoint slack on any one ray gives an eligible strict separator after rational interior-normal perturbation.

### I.3 Three-generator gauge and quantitative all-metric exclusion
Define rho_a=min{sum|c_i|:X_a=sum_(i!=a)c_i X_i}. The other centred vertices span R3, since g is interior. The optimal normalized point belongs to a boundary face of the symmetric hull of dimension<=2, hence at most3 signed generators suffice. They are linearly independent when the supporting face is a triangle; lower-dimensional supports extend to a nonsingular triple using zero coefficients. Enumerating all nonsingular triples with Cramer's rule gives rho exactly.
Eligibility iff rho_a>1. For every SPD,
||X_a||_M <= rho_a max_(i!=a)||X_i||_M.
If rho_a<1 this is a uniform norm-ratio gap. It prohibits a as a unique globally farthest root, NOT a as an additional local U.

### I.4 Fully preserved exact actual E17 countercontrol
Exact source: [internal-source-reference], root_core.py.txt,8937bytes,SHA2561bd673985599721cc481d7e7cdcc4695d06bbe80d12a7ec3d1d269f9af3b30fd. Save unchanged as root_core.py. Source contains every raw coordinate, true face and parameter; no other computational dependency is required.
Input is EXACT central(r,s,eta)=(1/4,1/4,1/4) in Bright Willow18 immutable minimum-0199 SHA818ef0f09b76ed0128685b8ca263e1898784ba9fdb4a78881206817ae46020d0, in that parent's raw affine frame. It is NOT the distinct CORNERCUT apex4 body. The parent's all-SPD family U2 theorem is accepted separately; this is not an independent replay of that theorem.
The standalone source checks every maximal supporting facet by exhaustive support triples, strict full-polygon convexity, edge incidence and Euler, then computes the actual homogeneous centroid by exact signed tetrahedra. No independent masses or assumed COM.
Actual volume3435181/9997824; actual raw COM=(1111571226551/3577534900640,2785510668367/8943837251600,69222241/274814480).
Exactly roots4 and7 are ineligible:
rho4=5031664986545/6551054443758<1,
rho7=71600206872421/76582295774325<1.
All eight other roots0,1,2,3,5,6,8,9 are eligible. At each, the source constructs an exact rational SPD making it uniquely globally farthest and evaluates all true directed primal edges. In that root order, strict unstable sets are respectively{0,9},{1,9},{2,4},{3,7},{5,7},{6,9},{3,8},{4,9}. Each control has exactly2strict U and no weak VERTEX equilibria. Full stable-facet and saddle-edge censuses are not asserted. Roots4 and7 can be the second local U although ineligible as a sole U.
With the accepted parent family theorem, these examples attain sharp U=2 at EVERY eligible globally-farthest root on this exact body. They do not produce U1 or exclude a canonical type.
Reconstruction AND exact verification: python root_core.py --output root_core.json . Do not use -O. Executed with Python3.13.5, requires standard library only and syntax>=3.10. No randomness, precision settings or hidden input.
Expected marker END_ROOT_CORE_EXACT_OK. Deterministic root_core.json29617bytes,SHA2563659d04c68412d9d31bd687761978aa46236bc684e8bfd275446bec9d7656ab4. Complete exact gauges, core inequalities, metrics and gaps reconstruct from source. Coordinator-executed exact computation, not worker replay.

## II. FIXED_FOOTPOINT_RECIPROCAL_CONVEX_SLICES_V1

This is a general fixed-body physical-metric reduction, not tied to the E17 example. The underlying Schur normal-variable method is preserved in [internal-source-reference] (fully read). The proof below is self-contained and needs no missing code.

### II.1 One physical metric, normalized at a proposed unstable root
Use an invertible linear chart, AFTER translating to the actual COM, with proposed root A=e3. Scale the physical SPD metric so A^T M A=1. Every such metric has a unique form
M=[[K+ff^T,f],[f^T,1]], K in S2 positive definite, f in R2.
This is exactly the Schur complement criterion. In the earlier inverse-metric notation N=[[H,-Hf],[-f^T H,delta+f^T H f]], the normalized physical parameter is K=delta H^-1; no independent primal and polar metrics are introduced.
For X_i=(y_i,z_i) and tau_i=z_i+f dot y_i,
D^p_ij=y_i^T K(y_j-y_i)+tau_i(tau_j-tau_i).
For FIXED f this is affine in the three entries of K. Root A is strict U exactly when tau_j<1 at all its true neighbours.
Let J=adj(K). In dimension2 J is LINEAR in K, det M=det K, and
adj(M)=[[J,-Jf],[-f^T J,det K+f^T J f]].
For a polar vertex q_i=(u_i,w_i), put v_i=u_i-w_i f. The exact reciprocal polar arrow, multiplied by positive det M, is
v_i^T J(v_j-v_i)+(det K) w_i(w_j-w_i).
Along the root's full polar face, w_i=w_j=1, so this simplifies to
(p_i-f)^T J(p_j-p_i),
again affine in the same three K variables. More generally the determinant term vanishes on any equal-w polar edge, but a general edge outside that plane retains it.

CONSEQUENCE: for fixed f, any prescribed collection of true primal arrows and true polar arrows inside the root's full polar face is one convex feasibility problem in S2, using exactly M and M^-1. Weak or strict scalar arrows are respectively closed or open affine halfspaces, intersected with the open SPD cone. It is NOT generally convex after including arbitrary polar edges outside equal-w planes: det K is quadratic there. This is the central remaining boundary, not a suppressed detail.

### II.2 Exact root domain and bounded metric closure for a FIXED body
A uniquely globally farthest root A must satisfy
r_i(K)+tau_i²<1 for every i!=A, where r_i(K)=y_i^T K y_i.
For a prescribed f, some K>0 satisfies these inequalities iff
f in F0={f:-1<z_i+f dot y_i<1 for every i!=A}.
Necessity follows from r_i>=0; sufficiency follows by taking K=epsilon I small enough. Thus F0 is the exact two-dimensional footpoint domain for eligible globally-farthest roots. It is an open bounded convex polygon (possibly empty): the transverse y_i span R2 and the displayed finitely many slabs bound f in both independent directions. Nonemptiness is equivalent to I.1.
Let Sigma=sum_(i!=A)y_i y_i^T>0. Summing the radial caps gives
tr(K Sigma)<n-1, hence tr K<(n-1)/lambda_min(Sigma).
Together with bounded F0 this gives a compact closure of the normalized uniquely-farthest metric region for EACH fixed body. The closure includes K singular and slab/radial equality walls. No uniform eigenvalue lower bound, no compactness across arbitrary varying shapes, and no admission of degenerate metrics as physical examples are claimed.

### II.3 A weak escape tree already imposes strict radial ordering
Suppose a true-edge arborescence points toward A and each selected D^p_ij>=0. On every tree edge,
||X_j||_M²-||X_i||_M²=2D^p_ij+||X_j-X_i||_M²>0.
Hence A is uniquely globally farthest and strict U, and every nonroot has a nonnegative true escape. Such a weak tree rules out other STRICT U, but may permit weak vertex equilibria. Proper110 still requires their removal and the true full-facet/edge contact census. An infeasibility theorem for this weak relaxation remains a valid strong exclusion.
Therefore any feasible weak rooted escape-tree slice automatically lies inside F0 and the radial caps; these do not have to be separately assumed. Conversely if every other vertex is not strict U, choosing a nonnegative true escape gives an acyclic functional graph by strict norm growth and thus a tree to the unique strict U.

### II.4 Small mixed primal/root-face infeasibility certificates
For fixed f, form any finite family of scalar affine inequalities in K from primal arrows, root-face reciprocal polar arrows, or radial caps, with any specified strict/weak choices, and intersect them with S2++. Finite Helly in ambient dimension3 implies: if the system is infeasible, some at most4 convex sets are already infeasible. Thus either at most4 scalar affine constraints are inconsistent without using SPD, OR at most3 scalar constraints together with SPD are infeasible.
This is POINTWISE in f. The certificate's support may change with f; it is NOT one universal four-arrow obstruction valid for every footpoint or every shape. It does not contradict the already sharp minimal4/minimal5 face circuits where f also varies. When using ONLY homogeneous root-face arrow constraints at fixed f, trace-normalizing K reduces the dimension further to2, but this cannot be used in an inhomogeneous mixed primal system.

### II.5 Complete sparse dual alternative for WEAK slices
Write every weak scalar constraint as B_r:K+b_r>=0. Then no K>0 satisfies them iff nonnegative multipliers mu_r exist such that
Q=-sum mu_r B_r is positive semidefinite,
q=sum mu_r b_r,
and either (Q!=0 and q<=0) or (Q=0 and q<0).
Sufficiency: summing the weak inequalities gives -Q:K+q>=0, impossible because Q:K>0 for Q nonzero PSD and K>0, or because q<0 when Q=0.
Necessity: let P_aff be the polyhedron defined by the weak affine constraints. If P_aff is empty, ordinary finite-dimensional affine Farkas gives Q=0,q<0. If P_aff is nonempty but disjoint from the OPEN positive definite cone, convex separation gives a nonzero Q>=0 with sup_(K in P_aff)Q:K<=0=inf_(K>0)Q:K. The corresponding bounded feasible linear program on the polyhedron has an attained dual solution, producing mu>=0 with -sum mu B=Q and sum mu b<=0. Helly permits support at most4 overall, and at most3 in the nonempty-polyhedron/PSD-separation case.
The stated dual alternative is for ALL-WEAK scalar inequalities. Helly still applies to mixed strict systems, but their strict dual alternatives need the corresponding additional cases and are NOT claimed by this formula.
For primal-only arrows, B_r depends only on fixed geometry, while b_r(f)=tau_i(tau_j-tau_i) is quadratic in f. Therefore a fixed multiplier vector with Q>=0 supplies a quadratic exclusion region q(f)<=0 (or q(f)<0 when Q=0) in the two-dimensional footpoint domain. This is a promising exact finite-cover target. It is NOT yet a proved finite list covering F0; the possible stress cone is generally nonpolyhedral, and an unproved finite extreme-ray enumeration must not be assumed. Root-face polar B_r additionally depends affinely on f.

## III. Scientific significance and evidence boundary
I supplies a metric-free exact root filter, a convex actual-centroid core, and countercontrols showing why uniquely farthest is not enough. II puts primal escape and the physically reciprocal local polar obstruction in a common convex slice with small exact infeasibility support. The untouched global obstruction is gluing those slices over f and shape, and the determinant coupling on general polar edges. These are research frontiers, not a minimum proof. Actual centroid is indispensable throughout; arbitrary positive barycentric masses cannot replace it.
The convex separation, finite Helly and linear-program duality used are standard mathematical facts; all specialized reductions and claimed implications are proved explicitly here. No claim of historical priority. No code materially produced II, so its complete proof is its preservation unit. The exact source materially producing I.4 is independently preserved in [internal-source-reference] and must be explicitly supplied to a computational successor along with this proof.
