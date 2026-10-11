# minimum-0128

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# AUXILIARY_VERTEX_FIXED_VOLUME_SLIDES_AND_BINARY_ROOT_OBSTRUCTION_V1

## Determination

The unrestricted maximum and the full unequal-endpoint root-only maximum remain undetermined. No body with T>=51/25 is claimed. This continuation supplies a general **actual-body, fixed-volume reduction for positive-density auxiliary vertices**, together with a stronger obstruction to simple root projection.

The reduction applies to every finite canonical triangular-pair polytope, with arbitrary nonnegative opposite endpoint data, including zero endpoints and b=1. Whenever an auxiliary vertex has a nonzero motion preserving both its incident polygonal facet planes and the actual volume, its position can be moved to a genuine face-degeneration event without decreasing the ORIGINAL ratio. Repeating this operation terminates at a root-only body, a coordinate-patch boundary, or a precisely defined residual in which every remaining positive-density auxiliary vertex is individually fixed by its polygonal planes plus the volume constraint. In particular, such a residual vertex must meet at least two nontriangular maximal facets. This is a reduction, not an exclusion of that residual.

The negative result is stronger than the parent's unchanged-root deletion example. A complete rational interval of genuine bodies has T>2, yet **all eight nonidentity combinations of retaining, deleting, or vertically projecting its two auxiliary vertices to the root give smaller T**. This includes projection that is allowed to enlarge the root. Nevertheless, an oblique fixed-volume motion converts a member into a genuine root-only body with strictly larger T. Thus the new method addresses a real obstruction rather than assuming that one of the elementary root operations must work.

All new computational certificates, controls, the generic rational single-vertex routine, the numerical discovery source, and its complete checkpoint are embedded in the recovery below. The original and fresh source-only build/verify runs were observed successfully.

## 1. Input authority and evidence status

Read the entire current journal, including the literal parent and its complete executable source, through EOF. Current journal research-journal(20260920-140556).md: 312753 bytes, SHA-256 a618320f58fc3cf14c7406c3729d248a963f18487f4facf61bb91211fc366c8e. Unchanged earlier materials remain the earlier supplied evidence; no inaccessible archive was assumed.

Required parent: **minimum-0123**, supplied immutable SHA-256 **cfcf3fdd7e401178bd9b9626830ba970f0460a54e11105158977d888331d4f9d**. No scientific, incidence, or alias conflict was found. Its 38/37 and 18/17 figures count true vertices and are not trace bounds. Its actual-moment coupling and its fixed-root deletion obstruction are retained. :contentReference[oaicite:0]{index=0}

There is now an observed replay of the parent's formerly unreceipted audit. Its unchanged extracted root_trace_audit_v1.py is 10751 bytes, SHA-256 **aa1391a86e83f6d427567562ad55cf816ba4249f6946f5e320bacc6d4c627b6d**. Both build and verify printed ROOT_FIXED_ROOT_DELETION_EXACT_PASS for the 70968-byte report, SHA-256 **36a384c42671eba668c8c7d2cf1ca123ccba9ae3f497ca7395b9f1f54577b5f5**. This closes an execution-receipt gap, not a mathematical gap or a new trace exclusion.

The new reduction is proved directly from the original uniform tetrahedron integrals. No external localization or shadow-system theorem is a premise. Exact checks below are rational computational algebra and genuine hull audits, not proof-assistant formalization.

## 2. General single-vertex theorem

Let P contain the canonical tetrahedron

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),

and have the entire maximal coordinate facets ABC and ABD. Fix

    ell=1+(d-1)x+(c-1)y+(b-1)z >= 0 on P,
    n=(1+b+c)x+(1+b+d)y,
    0<=b<=1, c,d>=0.

Assume F=P∩{ell=0} is a genuine two-dimensional facet. Write

    V=Vol(P), J=∫P x, Bell=∫P ell, N=∫P n,
    T=N/(6 V Bell).

An auxiliary vertex is a true vertex v other than A,B,C,D with ell(v)>0. All such vertices have positive x,y.

For each nontriangular maximal facet G containing v, its other vertices include three noncollinear fixed points. Holding all vertices except v fixed therefore fixes G's plane. Let its normal be n_G, with arbitrary nonzero scaling, and define

    E_v = {h : n_G·h=0 for every such G},
    a_v·h = D_v V(h) for h in E_v,
    H_v = E_v ∩ ker(a_v).

These are geometric plane and ORIGINAL-volume constraints, not constraints on an independently chosen mass. The row a_v is taken from one fixed boundary-triangulation volume polynomial. On E_v it is the actual volume derivative. Outside E_v it is only a polynomial extension: moving a vertex out of an incident polygon plane can change the hull cell, and that unrestricted hull derivative is NOT being substituted. Two triangulations give extensions differing by a vector in the span of the polygon normals, so H_v and the augmented-rank test are independent of this choice.

**Single-vertex reduction.** If H_v is nonzero, there is a nonconstant segment of positions for v, starting at the given body, with exactly constant V and nondecreasing T. Before its first wall the full original face lattice, coordinate triangles, root facet and root plane are retained. At the wall the actual hull has fewer true edges. The endpoint either still has the exact coordinate triangles, or is a coordinate-patch limit. The original root remains contained in the zero set, so its area cannot disappear. If the moving vertex reaches ell=0, the root can enlarge; its area is not asserted constant at that event.

The complete closed fixed-volume position domain in the current face chamber is a compact polytope of dimension at most two. The trace is linear-fractional there, with a strictly positive denominator. Its maximum is attained at a vertex of that position polytope. Rational input admits a deterministic rational step and rational endpoint.

For a simplicial auxiliary star, there is additionally a nonzero line preserving **both V and T exactly**, all the way to its two chamber endpoints. This is an exact level line, not merely a vanishing first variation.

### 2.1. Exact original moment identity

Triangulate the actual oriented boundary, using integration diagonals only. Keep this triangulation fixed while v moves by h in its allowed plane space. The signed boundary formulas are

    V=(1/6) Σ_sigma det(x_i,x_j,x_k),
    J=(1/24) Σ_sigma det(x_i,x_j,x_k)(x_i+x_j+x_k).

Each determinant is affine in the single moving vertex. Consequently, for a fixed vector-valued linear map C_v,

    V(h)=V0+a_v·h,
    J(h)=J0+C_v h+(a_v·h)h/4.                 (1)

The quadratic term follows by multiplying each incident determinant's linear coefficient by the extra vertex sum h; the sum of those determinant coefficients is 6a_v·h. Thus it is the SAME volume derivative appearing in both formulas.

On H_v, (1) becomes

    V(h)=V0,
    Bell(h)=Bell0+ell_lin·C_v h,
    N(h)=N0+n_lin·C_v h.                     (2)

Both integrals belong to the actual deformed uniform body. In particular, along h=t u,

    T'(t)=[N1 Bell0-N0 Bell1]/[6 V0(Bell0+t Bell1)^2].   (3)

The numerator in (3) is constant. Either orientation of u is feasible locally; choose the orientation giving a nonnegative numerator. No inclusion monotonicity, separate moment optimization, or uniformly refilled balanced image is used.

If the star is simplicial, E_v=R3. The two homogeneous equations

    a_v·u=0,
    Bell0 n_lin·C_v u-N0 ell_lin·C_v u=0

have a nonzero common solution. Equations (2) then give exact preservation of T throughout its feasible line, including all finite endpoint values.

### 2.2. The complete feasible position domain is linear

Use o=(1/4,1/4,1/4), which stays strictly inside because T0 stays inside. Impose the fixed polygon-plane equations, together with the following finite inequalities for the oriented boundary triangulation:

    det(x_j-x_i,x_k-x_i,x_l-x_i) <= 0

for every oriented integration triangle and every vertex, and

    det(x_i-o,x_j-o,x_k-o) >= 0.

For an incident nontriangular face also impose its cyclic planar edge inequalities using its fixed normal. They keep its polygon convex and its cyclic order correct; a fan orientation alone need not certify planar polygon convexity. Include x(v)>=0, y(v)>=0 and ell(v)>=0 explicitly.

Every determinant above is affine in the one moving point: terms with two occurrences of its displacement cancel. The planar edge inequalities are affine for the same reason. The open versions of the nonidentically-zero rows describe the original face chamber. Its closure is exactly their nonstrict polyhedron: interpolation toward the original point makes every previously strict row strict. Thus no disconnected or fictitious realization cell is introduced.

The chosen volume-polynomial derivative is nonzero. Indeed, if the incident boundary triangles have outward unit normals u_sigma and areas A_sigma, the triangular boundary variation gives

    a_v=(1/3) Σ_(sigma incident v) A_sigma u_sigma.

Each u_sigma·(v-o)>0, so a_v·(v-o)>0. This last computation uses the polynomial extension only to show that its row is nonzero; physical deformations are still restricted to E_v. Intersecting the position domain with a_v·h=0 therefore leaves at most two dimensions.

### 2.3. Compactness and positive denominators

Every feasible body contains T0 and has volume V0. For the canonical barycentric coordinates of the moving point,

    lambda=(1-x-y-z,z,y,x),

each tetrahedron obtained by replacing one vertex of T0 by v is contained in the actual body and has volume |lambda_i|/6. Hence |lambda_i|<=6V0. The position domain is bounded. It is closed, so it is compact.

Furthermore

    V0>=1/6,
    Bell(h)>=∫T0 ell=(1+b+c+d)/24>0.

These statements remain valid at a face merger, root collision, or coordinate-patch endpoint. No root area, endpoint tilt, or image Jacobian is divided out.

If a position is a convex combination of feasible positions h_i with coefficients theta_i, equations (2) give

    N(h)/Bell(h)
      = Σ_i [theta_i Bell(h_i)/Σ_j theta_j Bell(h_j)] * N(h_i)/Bell(h_i).

This proves the linear-fractional maximum assertion while retaining the common body's volume.

### 2.4. Deterministic rational implementation

The embedded generic_step implements a wall step, not a numerical optimizer. Compute a_v by the signed original boundary formula. Stack a_v and the incident polygon normals, compute rational reduced row-echelon form, and take the null vector for the first free column. Orient it using the exact numerator in (3). Along that vector all chamber constraints have the form c_i+t d_i<=0. The first forward wall is exactly

    t_end=min_{d_i>0}(-c_i/d_i).

It is finite and strictly positive by boundedness and relative-interior feasibility. The routine reconstructs the endpoint's true maximal facets, true vertices and true edges, and verifies its own volume and ratio. It returns FIXED_VOLUME_RIGID rather than fabricating a direction when the augmented row rank is three.

The generic routine was actually executed on the symmetric two-step example, its unequal-endpoint companion, and both individually rigid auxiliary vertices of the literal parent's body. The fixed-direction certificates additionally verify the entire stated motion intervals.

## 3. Finite reduction and exact uncovered complement

A proper endpoint of a fixed face chamber is a coarsening of its labelled face structure. Vertex limits cannot create new vertices. Facet normals normalized at o remain bounded because a fixed ball about o lies in T0; limits of the old supporting halfspaces therefore represent the limiting full-dimensional body with no more facets. If both vertex and facet counts stayed unchanged, all old vertices and facets would survive, all old incidences would persist, and Euler's identity would leave no room for a new incidence or lost edge. The previously strict wall could then not be reached. Thus at least one of the vertex or facet counts drops, and the true edge count drops as well.

Apply the single-vertex step whenever H_v is nonzero and recompute the actual hull at every wall. Stop immediately on reaching a coordinate patch. Otherwise the true edge count strictly decreases at each step, so after finitely many steps the result is either root-only or satisfies

    rank({a_v} ∪ {n_G : G incident to v, G nontriangular})=3

for EVERY remaining positive-density auxiliary vertex. In particular, every such vertex meets at least two nontriangular maximal facets. The entire path keeps V and the endpoint data fixed and never decreases T. This theorem includes arbitrary unequal c,d and the original zero-endpoint and b=1 strata; it does not use the singular affine-density coordinates at b=1.

The residual is **not empty and is not excluded**. For the literal parent's body at delta=1/1000, the two auxiliary vertices 8,9 each meet two independent quadrilateral planes. Their allowed individual motion line is span(1,-1,0), and exact original-volume differentiation gives

    D_8 V(1,-1,0)=-67/75000,
    D_9 V(1,-1,0)=+67/75000.

Thus both are individually fixed once volume is fixed. This is an actual 10/21/13 triangular-pair body, not a formal rank example. Its original data are

    V=4263470123/21000000000,
    Bell=4553794654013/84000000000000,
    N=184904985954453/1400000000000000,
    T=38830047050435130000000/19414967453661547553599.

Its value is between 2 and 2.001. Complete coordinates reconstruct from the parent's literal parameters, which are also embedded in the new independent generator. This obstruction is only to an individual fixed-volume move; it is not an obstruction to joint vertex/facet motions.

If a step reaches a coordinate patch, the quotient from the unchanged n and ell is explicitly a marked-patch functional, not a trace of two falsely relabelled triangles. The original positive-area root has not disappeared. For a strict value above 51/25, the accepted root-preserving patch resolution transfers it to nearby genuine triangular-pair bodies. An endpoint value exactly 51/25 still requires an equality argument. The reduction does not settle that boundary. :contentReference[oaicite:1]{index=1}

Once a genuine root-only endpoint with 0<b<1,c,d>0 is reached, the parent's finite-vertex reduction remains available. It does not become a trace bound merely by composition with this new reduction. The unresolved alternatives are the individually rigid auxiliary strata, joint deformations across those strata, the root-only maximum itself, and the global threshold-equality boundary. No uniform bound on the terminal number of vertices or facets is proved. This is a finite-polytope reduction, not a bounded-complexity reduction for arbitrary nonpolyhedral maximizers in the compact closure.

## 4. Complete failure of the retain/delete/project rule

Fix endpoints

    (a,b,c,d)=(1,3/20,1/25,1/25),
    ell=1-(24/25)(x+y)-(17/20)z,
    n=(119/100)(x+y).

For **every** delta in [1/50,13/500], take P_delta as the hull of the following ten literal points, in this order:

    0=(0,0,0), 1=(0,0,1), 2=(0,1,0), 3=(1,0,0),
    4=(1/5,3/5,116/425), 5=(3/5,1/5,116/425),
    6=(1/8,11/12,0), 7=(11/12,1/8,0),
    8=(1/2000,3997/6000,(20/17)(9/25-delta)),
    9=(3997/6000,1/2000,(20/17)(9/25-delta)).

Vertices 4–7 are the genuine quadrilateral root. Its xy area is 4147/28800 and its physical area is that number times sqrt(25657)/85. Vertices 8,9 have ell=delta>0. Every noncanonical point has strictly positive x,y, so ABC and ABD are the entire maximal coordinate facets.

For an auxiliary vertex define D as deleting it, Z as replacing it by its vertical projection onto ell=0 with x,y unchanged, and K as retaining it. Recompute the true convex hull and original uniform moments after the operation. The theorem is

    T(P_delta)>T(P_delta acted on by (action8,action9))

for all eight choices in {K,D,Z}² other than (K,K), throughout the whole interval. Reflection identifies them with five comparators: D1, Z1, D2, Z2 and M, where M deletes one auxiliary vertex and projects the other. All comparators are genuine triangular-pair bodies with genuine roots; Z is allowed to change and enlarge the root. Hence the result also rules out choosing the better first single-vertex deletion/projection, and rules out every simultaneous root-only assignment of these two elementary operations.

### 4.1. Complete geometric and polynomial coverage

The interval splits at delta*=1/40. P_delta is true 10/20/12 on the left open interval, true 10/21/13 on the right open interval, and true 10/19/11 at delta*. At that wall a pentagonal facet is genuine. Its peak facet cycles are

    012, 031, 02673, 182, 139, 19548,
    286, 379, 4576, 468, 597.

No pentagon diagonal is counted as an edge. In particular, this body is not 10/17/9.

For each of the six bodies P,D1,Z1,D2,Z2,M and each of the two closed intervals, the certificate constructs the actual supporting facets at an interior rational point, forms their determinant polynomials, and checks their entire closed interval. It uses 1777 nonpositive supporting coefficients: 1169 negative and 608 zero. Endpoint mergers are re-hulled as actual mergers.

The original moments are polynomials of degree at most two. Let D_P=6V_P Bell_P. Each comparison is certified by

    N_P D_other-N_other D_P > 0.

All five comparisons, P>2, a coarse upper bound, and the signed derivative of T use 68 strictly positive exact Bernstein coefficients over the two CLOSED cells. There is no infeasible-cell pruning. The derivative is strictly positive on the left and strictly negative on the right. Thus the height-interval maximum is exactly at delta*, with

    max T(P_delta)=27271148057790/13615985794057
                 ≈2.0028772407865687 < 2003/1000.

This is a complete negative variational result, not a maximum over unrestricted shapes and not a threshold counterexample.

### 4.2. Exact peak controls and original volumes

|Body at delta*=1/40|True V/E/F|Original volume|Exact T|
|---|---|---|---|
|P|10/19/11|883423/4590000|27271148057790/13615985794057|
|D1|9/17/10|3491221/18360000|214954012517160/107386211879867|
|Z1|9/18/11|56179/286875|4088500400775/2042050695716|
|D2|8/15/9|2759/14688|52934710143/26462548445|
|Z2|8/15/9|182621/918000|14140593240375/7066803388034|
|M|8/15/9|3541021/18360000|273069660516450/136388234630461|

Every entry is audited at its OWN uniform-volume centroid with the identity metric. The peak controls have strict S/U/H=4/4/6, with all true-edge primitives nonzero and no weak edge packets. These are nonwinning controls, not 110 bodies. Full facet cycles, all three first moments, Bell, N, root areas, poles and primitive packets are regenerated, not inferred from f-vectors.

For P itself,

    V0=883423/4590000,
    Bell0=15412759/293760000,
    N0=3145461137/25920000000,
    J0=(449351591/8812800000,
        449351591/8812800000,
        1545976397/31212000000).

The root-only mixed comparator is included because comparing only D2 and Z2 would not exhaust the binary choices.

## 5. The oblique coupled motion succeeds where every binary choice fails

Start from the peak P=P_(1/40). For 0<=tau<=1 move only vertices 8,9 by

    v8(tau)=v8+tau*(3825,10795,-13287)/109650,
    v9(tau)=v9+tau*(10795,3825,-13287)/109650.

The entire open path consists of genuine 10/19/11 bodies with the same coordinate triangles and root plane. It preserves reflection symmetry and the ORIGINAL volume exactly. Its exact moments are

    V(tau)=883423/4590000,
    N(tau)=3145461137/25920000000
             +(4532507/23220000000)*tau,
    Bell(tau)=15412759/293760000
             -(212837/7017600000)*tau,
    Jx(tau)=Jy(tau)=449351591/8812800000
             +(647501/7894800000)*tau,
    Jz(tau)=1545976397/31212000000
             -(66917353/447372000000)*tau.

Thus T is strictly increasing on the WHOLE interval. The actual centroid is J(tau)/V0; it is neither fixed nor transported. At tau=1 the two auxiliary vertices reach the root and old vertices 4,5 cease to be extreme. The genuine root-only successor, in its new vertex order, is

    A,B,C,D,
    (1/8,11/12,0), (11/12,1/8,0),
    (3043/86000,65757/86000,116/425),
    (65757/86000,3043/86000,116/425).

It has true 8/15/9 and

    V=883423/4590000,
    Bell=827956913/15789600000,
    N=135472389227/1114560000000,
    T=419480576642175/208981765700914
     ≈2.0072592230009105.

Its root xy area is 1422421/7740000. Root area is 4147/28800 before the collision and enlarges at the endpoint; it must not be described as continuously preserved facet area. The physical-area factor stays sqrt(25657)/85. The successor's root deficit is nonconstant: its near deficit is 3043/43000 and its far deficit is 1/4. It is not silently placed in the old constant-deficit family. It remains in the previously closed low-endpoint chamber and is not a new trace record.

The generic single-vertex procedure also reaches the same successor in two individually certified steps. First move vertex 8 along (3825,10795,-13287) for t from 0 to 1/109650. Its entire chamber interval is [-1/7650000,1/109650]. At the root endpoint the actual body is 9/17/10, with

    T=690354406200900/344304803855003 ≈2.0050675984515998.

Re-hull, then move the remaining auxiliary vertex along (-10795,-3825,13287) from 0 to -1/109650. The other endpoint of each position interval is a genuine coordinate-patch limit, not a triangular-pair control. The complete audit retains their coordinates and their own moments. The chosen root endpoints retain exact coordinate triangles.

### Unequal-endpoint companion

The method is not restricted to c=d. Keep the preceding xy coordinates, b=3/20,c=1/25, set d=1/20, and set each noncanonical height by

    z=[1+(d-1)x+(c-1)y-w]/(1-b),

with w=0 at vertices 4–7 and w=1/40 at 8,9. The true initial body is 10/21/13. Move vertex 8 in direction (3825,10795,-13242), for 0<=t<=1/109650. The entire motion retains the original volume

    V=14283443/73440000.

Its exact initial and root-endpoint traces are

    T_initial=17791691749429200/8899143228802769 < 2,
    T_end=765650132831151600/382553717212838591 > 2.

The endpoint is genuine 9/19/12, with the same root plane and exact ABC/ABD. Its original Bell and N are

    Bell_end=26783018437/505267200000,
    N_end=37531869256429/303160320000000.

The static initial and root-endpoint own-centroid mechanical censuses are respectively 4/4/6 and 5/4/7, all primitives nonzero. No whole-interval mechanical census is inferred from those endpoint audits; the whole-interval claims concern geometry, volume and trace.

## 6. Original weighted verification and retained discovery evidence

Every reported actual control is reconstructed by exact supporting-triple enumeration, actual polygonal facet cycles, true edges, Euler's identity, and an independent intersection of supporting-plane triples. Two positive interior tetrahedral fans give identical ORIGINAL volume and first moment.

For each control with b>0 the actual balanced projective image is also reconstructed. With S0=1+b+c+d and Jp=b*S0^2, exact tetrahedral integration on TWO image fans checks

    I4=Jp*V, Iell=Jp*Bell, In=Jp*N,
    T=Jp*In/(6*I4*Iell).

These are the transformed original weights. The image's uniformly refilled centroid is not substituted. Mechanical audits always use the original body's own volume centroid.

The numerical locator was used only to discover the binary obstruction. Its complete source and frozen checkpoint are in the recovery. Actual environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, one BLAS thread. It used differential evolution with seed918633, maxiter600, population multiplier20, tol1e-10, polishing enabled, one worker and immediate updating. Its nine complete bounds and all inputs are literal in the source. The terminal checkpoint had nfev108400 and success=false: the iteration limit is not a maximum or an exclusion. The portable source differs from the executed locator only in its output-file destination; no numerical method or parameter was changed.

The intermediate rationalized control is also preserved rather than discarded. In the generator's parameter order (b,q,r,R,eta_r,eta_R,s,w,eta_aux), it is

    (31/200,81/2000,1591/2000,5211/5000,
     849/2000,2373/10000,1323/2000,13/500,1/10000).

The pair generator is (eta/2,s-eta/2,z) and its reflection, with z=[1-(1-q)s-w]/(1-b). This control is genuine 10/21/13, V=196117663691/1014000000000 and

    T=12938005989739227465900000/6460922231918985617368489.

Its deleted and projected root-only controls, their exact own volumes/moments and full mechanics are independently retained in the report. The simpler construction above is the principal recovery object, not a claim of numerical optimality.

## 7. Most useful continuation

The new reduction replaces arbitrary mobile auxiliary vertices by actual face-degeneration strata while preserving the original ratio in the correct direction. The remaining individual-volume rigidity is a real geometric phenomenon, demonstrated by the literal parent's body. The next consequential step is a coupled motion of vertices or facet planes that removes that rigidity without losing the common volume/density relation. Alternatively, bounding the root-only endpoint class would settle one of the terminal alternatives. Repeating elementary deletion or vertical root projection is now ruled out even with the better choice and even when root enlargement is allowed.

No global minimum bound, E17 incidence count, or attaining 110 construction changes. The compact weighted maximum and the exact-threshold patch boundary remain unresolved.

## 8. Complete recovery and observed receipts

Save the complete source block below as recover_auxiliary_trace_v1.py, UTF-8/LF with a final LF. Run

    python -S recover_auxiliary_trace_v1.py sources work
    python -S recover_auxiliary_trace_v1.py build work
    python -S recover_auxiliary_trace_v1.py verify work

The exact child needs only the Python standard library, with assertions enabled. No optimizer, parent file, journal, coefficient download, or sandbox dependency is needed. The optional locator is not called by these commands. Its portable optional command is

    python work/root_binary_locator_portable.py de locator-output.json

Original build/verify and a fresh source-only extraction/build/verify all completed with byte-identical reports. The final observed pins are:

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_auxiliary_trace_v1.py|13487|c1d321d8627f0baa11c569d13d6836c50241c698b692cc98a9cf4fbb31167791|
|Decoded three-file payload|26690|04fd02384cb4d1edaedf480508cdef319995952b7495561564f5d2cb5dd3507a|
|auxiliary_trace_v1.py|23387|cdb5ff4c334e3af06d2880dffa5423379e679743087d179f917faf8e82c87c03|
|auxiliary_trace_v1.json|376806|97796311d20fe0b269469a273f75f0623ce49699365c3728fdbbe467782bbe69|
|root_binary_locator_portable.py|2178|5690e0635d0f7bdf02a1f3f213ba6a542d3db91e34c47f9f50fc51539cc4508e|
|root_binary_result.json|479|b4ddb1c06525efaae92cfc60832bb1897e7431599f296bfb2ae818a09ef53785|

Observed terminal markers include AUXILIARY_TRACE_EXACT_PASS, FIXED_VOLUME_TWO_GENUINE_ROOT_COLLISIONS_PASS, and AUXILIARY_TRACE_SELF_CONTAINED_RECOVERY_PASS. The source regenerates every exact polynomial, supporting row, coefficient, actual body, and moment in the report; report hashes are not substitutes for missing recovery data.

Convenience copies: [complete recovery](sandbox:/mnt/data/recover_auxiliary_trace_v1.py), [plain generic routine and verifier](sandbox:/mnt/data/auxiliary_trace_v1.py), and [complete sources and reports](sandbox:/mnt/data/auxiliary_trace_v1_complete.zip). The embedded recovery, not these links, is the durable handoff.

### Autonomous recovery source

```python
# AUXILIARY_VERTEX_FIXED_VOLUME_SLIDES_AND_BINARY_ROOT_OBSTRUCTION_V1
# Parent minimum-0123,
# cfcf3fdd7e401178bd9b9626830ba970f0460a54e11105158977d888331d4f9d.
# Exact proof child: CPython 3.13.5 standard library, assertions enabled.
# Optional locator only: NumPy 2.3.5, SciPy 1.17.0, one BLAS thread.
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
PAYLOAD_PIN=(26690, '04fd02384cb4d1edaedf480508cdef319995952b7495561564f5d2cb5dd3507a')
SOURCE_PINS={'auxiliary_trace_v1.py': (23387, 'cdb5ff4c334e3af06d2880dffa5423379e679743087d179f917faf8e82c87c03'), 'root_binary_locator_portable.py': (2178, '5690e0635d0f7bdf02a1f3f213ba6a542d3db91e34c47f9f50fc51539cc4508e'), 'root_binary_result.json': (479, 'b4ddb1c06525efaae92cfc60832bb1897e7431599f296bfb2ae818a09ef53785')}
REPORT_PIN=(376806, '97796311d20fe0b269469a273f75f0623ce49699365c3728fdbbe467782bbe69')
BLOB='''
c-q~4YjfMUvf%gq6}oe(R-
_Hfq}~rBRe3nq$z~Fdop>`*R4PiOEZP#ukd!PtHUE9P8vqHCk|%TP+^wxWGh>lJqX9I4eiP^CZ_Z}tuY4zdoTjle_oiFB5k3Ak{O
w=0mtVfV`|$4N)t}Rw^Q+J2U#D;1eLa6Oz4`Rv%kSsY>kseVoL^60eta{1_3k4=U48oWdHU(q_2;WEuRp*0^l^G)e-
HjuyL4hNNNY}VJH4BA`X3kfH{P4qU(YY++qB>L;}2{72Enc`UN$@3+I%rzv=*-0^V*he_xdw;FdKB6-G0lOIfI_Hu-aYA>9jrDwy
loc=?{86x8Lu#TDIF>3|vI@`tmVdhC!{>uv?7|t0k!uxK8ZWR{ku8nKBqm;>D>S21(5eoY~5A8{dOP9Ik5%AcCmy*HIX!wYRbW+S
J}kAU}oHVYteG=HYtg2M#rqFp-lkp+5z239sJ+`Lc8ptYddc7_j6Knur0_rc>9OZEmO2@4@%L^%gZZObv(4%wg=Mn>eT?o3&x=jv
i}^Fs|*`W6ck0Pkux&CVOjGrYRaGn^~b@x`|evu{+t{QnXobR>qt;r8e`UooItC90@v)!z3wmU^ruYax@z^Cnpa4fhT*y<dcPEmZ
)X&$;L8U)JmkTN0Vjq45^sD=nTu%Ks_fgF4=?U-!9XHe+&c99DWaK@IO^Herwp~<Y?sqpjq=5s-
os6HH5EutHe`<qG@5)Na%;7XnZ%J$v?125lpsWm!^42P~zPrxI2W3o#56pTG>*BtF6~E;_xA1@iI{(o%5BSqz0lq!aCC&xg1GwG&
co=+!StMcm{$18a77)&w--
msmri%4wPh~rc_9v*!8Jvs-3mmtX56KcL6*MV>cTXl<)*LspnGVz4yph&U)rLHGgOb(6K)utl0}-_f0uy#Ek<re0Im~6;_%KE-hC
$o&;f^kYEzl%wg4Jv%O;;8FRH~%o8KqKUA(@@)69Jjvp9__d_2*xJmhVlD}jBKK2iA8W?S(rN8oOxO<?H`NFON2NBbP_wfmAWBR3
upK)slZ;dF746}#^i=8O)0w88}c2HYbS}|y#x;Y*K>f`KvJj8cVs;?hx?O|c7i0#ff{wA>cmx`u~a1*%v=U?g#CXOV>$?Lq!5L;K
EF<DEeUckjUM9y*v=Yn0r(wj`Y-
pf~Ql5pmN5cq!ZXaweP9tNo&Y`nZ4Hanc|K(rerD`$Ss$D$}QPh1)#9lFa&0qGhS7NN~E>ul}p<jbBO5IC!UVGRS09PY$s0UoszS
9N-#F*qvHIt&9Y7{Zg-t}I0;FW9WT*hxK!9J@+6x3uZIaTsyzUU38cC_N3GSz-im2;kH^I}iBPQ+^y&3&i^L9~?1hBZ}hi&YQ#e<
YOZmV`JF*6DA++$;8}Gy7}XL<#BQBLF{B`ic5wIpszEvLaa<ZLuYE$MM1MvX##!EtRWRNVsGokiKicoJBy1tA2#yN!1bheAcYvCK
y_yg;Rw*<@Xjh6TiDAD*xqmqoXsjVB*zv^OQK@3RJ^i)x!F+wEeGgLSYY20vFIR31XN*8MxJ{MaO%j&1NPG=c*KD?u^HjZc?rJ$#
W|k7!eKJ=qqp#xp)i=m?L^25OjGphz+qQs<BaQv!>qu{G5SJe<+z0$R9HB7<uI{Nv&0qIof3C6Q2aBtVLj+!2)t-
W<T<zs$kAcWY&<a)16=q;v4&GZ+H7GcP3m<^<0ZUXXSMMX!!-A>w-
fv!F!LB61<e476ktJ$J5FeEG(nB@z)YXvc>+_3@1bml?SfT8*5zvr*owS~#5W0ZU<P|Q(w6JWK#sIoLRvhN`QmT0#jor@b6A*o!*
N|8ZGn76%5Whd)S-
Zq@np0P*PyH?nV7_`Vvsf{q=nXHGO2xmhUFjIW<K!3b_X_~(eQ?&YC3w4YMBLUS!*=+R;#2SjVn7H`ZdoE&9=B-
EA=IDUQ*3$rdHcLvCR^!Qi7-+^&I-
WQ@_Ws`A0&P8KdYrv>UP|4_Bns356WzM9g!RKhEjVJndE+OPT<V7gn|Q=9oiGwLIf!N{|fS1EVA0BLn)v7YF~$@Xs9nn5XS38d@T
CdPx}s1iFNmn<WFeVS)#|hm$|T9hKEUr;N~*4z$DoROVbg+meVk>^;xx3yPBK&r>4`ecY*+OfYo%%LLPwOi1tuDw|5KPeo%-
teU5BeE~aRd#E|x!jTDMF1I$z*$>m1#tpw=3qMZMsTehX&u*peusglUHH`Nrqtk|eGHrbAfwC9)^TfDN`|*-rjO${O^~vZK-
)`Yy%g4BBB6hn+&PU-2XNhW#eQLNT;vn6UNUj_dKuBY+PgHAAWjs3kqc42?Io^26fEr!v@6-
#ZY`|iuyUFOmbMEo?$ph7aTRHC_IRMg*Elnj*pj)C|eZu79R1TxWbvf~YEu1krCR;p%TT(KasJK%VK33deMQQmEjz&9P2w3s51a(
Q4N@Q7i4zy4}%ZaJ)`Y+Jk|Ku<}*p+A2=nHf#UTu86hIZn$DPEWIwFR#g)f6gFRg#p<&l(EP{lMHJQ^ca<9X<?^@`u{dY8-
PkQg<Ma@-
2v%Msl^Y#@bRb1Tgm<Ib3i0%aSyPqA6??rEcts>c$sRH+B;Rd3_M_T0vG1pKN=<C5af$cS@T^?N%%SZPs7=slWB6IO*vebhwn${F
#E2zjWltL$h|$rS8CCtNEJU&RyjR+6420lPC7v&D>Kb76!I9BDG~BVa!L8Xu0_qDdQ1sp$IL;VWeA%1*bzKJq9SdBlaVA#9&|J8m
RjqZ-
7+(nLsU^7?yc#{3z7?$ZE>c8TXNB%LJfl)|C4t@NRKJg%Rndks4hxcW|tln?{UpcQn_471juu5lu!;Sm^+A9LHiDAcu9^)G6+eNM
{Ws%-
O66fy5g7$9Ev+oTFKhwm7<24aWo362_A%j8CMR<bBU+^uppEKJllc^mtxC_oSRvvA@;nMKth_qJmDK>l+bhMK!1p^H<}+wXQnquy
n^B&1bxIQQ5^OQ3(WMF>?u#H><kt@-
Aty9OS1n<fn|Vh_X8@L*{Gh7J>nDYXaA3G7J7%%r>)r%C1Xse6SlPa2}i=Gmt_o$5inPO5{<+GdS~NAT(QrZ0V~N4!EHHi9MQUn=
d%lH{9LdZa7V!0u|64&Pk(kj*xK}=)5{wg-1um-
3dGyOaEjQnny?X2ONuYpyttAgWBFB*QKWbxp!Gry@$@s@(6J7nd%UG&T3lp2HksJRIz;iU-S1UXU~&z_B<VQ_T-
+Py>1>**2gPCv0~e@d&X1)+fIJbIddnSGk3Xj=C118MYMMn=L}N5v58#lJNK}Tji=mE^Hg%w$Z0E5uACY0Zl%H^K67+IZX2UyZwN
@BC8$y2xjy0Ip<-
w&QtvY#b3ITSPf<KwXi^X64}v(?Qzgjw8GGsPx;$u_O_U6QsesA(S@n6tC5u3l@&@e5iiQ8V;&|R;t&Lo+F&EujMP_)zgrsxXTNq
ZipakwWv8Wk7$d<(BTt<8u|HB%zx!}O#Uy~3w+h$4E%Izp5`z!Vbh^Q88S`xkk#V<cxUcBV?$*a--
;`Z^Y<3GL!moKkg{(k=X{OXz;&<0@Jtb<LO9qa=i#JkPpTT8szmPKKs*XJKTKwAULI<m92CD<`NVMz<BEHmdm3x5Y=1|oT@)Zwa$
B>s&3U@^O5Ud+5J2G$wR2dRvlv6$=HiHx@_GBuH9fIP9JTtUe~@`c`QDmOJBMFN`P1M@u5E~ZErbPKRo^7#s$6Gp>iUcou>#0~od
{{3MdCCSOdgLw)sGi|Xi8{RGzI<n`THW@(C?-Qbw&$6Jjl9!51TL%wLD#*kFXYJ)?UV((>=v!7G!+DCiLL<)Wm-
S(eyjb<d&g;g*{^a;_JQz;OP~XZ><8R~s<N)xSW)Zl8EU*7ouKT^(&p?@)vEze&dV^lR^EeJ;gGi#N<t!G$@I^)druSn;EQ?**To
wxYu>8#~QD1H?(#-ITpEz=RIYN6xg#$HHx#!pqRY=`r%!fuYby8qJX{Lcl+(Mn4LxrY1mJD-
5;sFoNbw%24e}JM80lz$sD5OOv8nnmeL~&Y-#-pDQ7}0w+<F9~+{lQ%RM|QdZDbIL|#<1Qa7j}Vtnppvc3JV2I;6x`G!2-
ggwYHCE$MZsSEOAQ&4s<?u!*D>zB!E@YbGDot*GKB%9DdLo^oXs?e~|067@3tpPiGY^9pH1b(fy9&5PppAAL&5?KsS*R+|kfJHgM
iYL|5a7c*IB{qLIX<`D$(McLMzWkzfVD1=rQ8(G7ZEZt9cKSN13ShA+COr#{gZ<VFtRtL*<z+4;9oz@e+J*w3G%ln19q_vq$`XjT
x{Sn@(x`KbLMW5h`^%^PH*ds&ZW{46-
%HGQBU@<^)c!Wg7+NgT^)2gPVnN%Z(nXXhtF6%pPaS<r`uYl*QaKbc@aOq@4(BhHL$Ty_zMVVZjc{stiuz`&S=as<vF=Q5Oqc-WX
u5~GupA3hBWXh~PPKTT2`7MY{6hf4XC2x}i*f$oBP=1O?`#k(~r$3<WS4F0322>xPF#57NvMb!&BP@dbw5*zr~9o;!|K08V*_*c3
QqJqc0JbK+0;gS}|0sbAyjuyIqIEpf-
4)lSPIbAS%vhis~2jO&~4)Z&qT}C;!cd#F%*ArAq+V0tF9%KJd=4ke5VilO$v0<Oi#35{I4ZWz`(xsNzkOZ-OQ-
@JxSYW`j7?lt%Wuz4j*a?c1LJy(}H<Y4V!j(<N5Mn3=08$S&CZGq26-
8B@5tMWC_29w$zyKJmgeVSORDLoF;>lelX4z|>xksQ=Y;(kSMF0n#^ru)g5*|jdF^dqw(}<=gZdxMc=}HQ)mD-
#zDu&MXvRhyHB~@b}HMRdm1Zo-
7<`O(da}~<DD>(A%XD>Fq7_jk=ZW#VWE=LbRu`w2D2ymkUpVUj>i0ZGf%{Z5N6c@_$dWD>ry7<Tg_L-*)*~E1BI2A`8{)mz-rhy>
`B{q_?y}TkXE4wE%pFP*T_e>3Lis81~*jXi98?TDHqpR{ghuJcJ?VvYPL^GnO+>5Brf)ItHdB8}+O|3MiqATR`l2>)B(b{*pu?mj
??zB15MW3eoTrvQItqvOdWzmw-#LZ*`wAM_-Jd%@}a3hd9q#p31ic{PNLb1A`PPvr6G6^TwyLMEqhgSF@*?hZkVz(IAOygfN6w|n
rGIU=FtY4O6h*7c<mSrSjeU8Z@5$aP<5j>frS;B?KDp|>eDzO8}O`M%EOVIhxK$~SS0Dzw*C15edjP>h)8sxufZ~dL;ieRvhryke
17J|mP^lEb_2w@{TE98Q)v-I3J1dSH6IA9~x!q|sj@*UMgW{0zCXvs3tdIb9t{?Xa4XsFS|VWFhNEPI;6Q-
OmLZA4Q^9`gmaDj{RB86+I;2*q~GsBSVWxqd|z#4577YT!dUWwf2nR2qp;r}pVm6AB5w=kJLL<t(Wh<#4?qTqBQx1MV`pRmD$c6V
ZCXJg2dT(Fh}Vza*PgDPm7E!NHJ8Khz_(F3#g;upSbVkV>%2f;ES-
%u0oKQ__PF25VB^!1!cnWim7(85)NSEkFjQo>J?m7sn5{=xPj2CZjp5LY_*aMyZe<Kv+6bA#BfBVGY)$NPEOH_ciuDu789jq9)_I
M%}vZ)0Wi;DcTeP&C>D8&Z;C#VWXm`XGX9Vb$H~&q+$Lq>c=o#4((>;v;}}CRx$?4zJO`t9P;4{+iK6y*h$l@#yZvi0M}X5vQKTx
5*QETd20Y5`hQG8maK0;KN<eR>B|Z4n=5ci7ZxvDA`v^ud)rI@e4%oZ=nc!OrS+HGk}`&t!_w!<D<urew+1Mr8RHeS5#wXYty$s1
2WDBPkvJsA6aO{<HQ7jRnM72WygZ<aFB3mehZ)5#_Q&MG6h936@E5>_Q&d2(!;;}Gac0>A;TEJ2^VxEbhXTx(V<SCUVk$Eb<eqcC
5FIS0EFX|?W|nuFtb7+cyNAwTKKmRKCF5C=Q1?;`4SHXGTv2}*6%-
c9t<s^K?>)^Itn*yIKn0_cGIj%Mfe6ChkWMPJiM`2am|fS*Z7`*j0CV?(eM$=|49o?cX73IUOl+s^<UsCVEH(Eew+S@aaK$TXyg=
zpE>S+(^Lh*@GBB`tMOCZlGONGWWwyE|1FB4>%gpoV2p_YR7Fm5rNSwqL^CY-
cF+{Y?gL<-wP^i@zC@m|KZS`!)g7aWlYM5*1!0P}|(E1VsRKf?5QQ3<MzA|zbGUeeC4N6`!QCRYviNd1ytTZMxCF)F!#EY^4ti-y
FmS78%#5EoZu@H!AScrg$UCAXeBg!%vuCyLc$iOFi`)?Y)u!hw6!Is2~C@zK_09OL8M=i3Yg=VxCI-69h9-
dieOTVaY8**+;$_~UR{PBT{Y=4)(N#0W;M)jEH%CHU(JQtf}N)w5Jz=@J&h^j}D#s;uP;fXA;4|#&cNm6rDgF0>EH2<oMVM`o@^B
d(DqOfDuUpaj>b>dqu<yyZu;Sqk1kaJ1_v?uEZO;K;h@0shzB6*V&0*>tWVHvKxDVU#YpzyRJSAJas&BU2x1)z#bX;#ojSx(gK$)
t}VG~b$(O3uAEz4ZdX29~4~Cx^m97`fpH@b8Za{X$3xdw(t-
^xqN=3Rgho>22(|Xtdy_P$Q7`*@+N?o0TxOqHy(y>JAuY`BDvQ(eg1NYb^{`k2MK*8wMxQ$_cy^u-
jnEZvEgER0NS0{BM`gIEMl^E9es%S(h>y@~r_X*<B?wsb&6}wAZ4vMX^6BNc=OE4o=(%#;BOy4Q6ml_IN|=QL2TOxi2LPn`Smx<O
hN0P9yrFF|)vM=W>0=8g=`$4@OM4he|kT;dQ%pYIpG$|D!^y_+<5jzAnqO%8c%pyn3KU7hDBbj<8@nY)<s$)V;WdZLub3`z?uYzV
znzML|RnZKKZyg**^|37(7Kqf)8D3nXi@2>y#!HNTtGoFtP=m@XpnOpbzrpMv()zH>4HZN!UF^AA$Wtj1b~t<}UefJ*n62tf^m0z
lS)_-
+!01TRuW?u%Vvn@4YrZjbdk7$eudr6Jm7GXI_t$^hfbS=S}?u6YI|`&^%#q0wc@sQaE2ODA^Lh$JD7$Y!DY$S)Y2k^5=7j6LM_v~
J=j+nTPQ%;B8Gk5f#LiNn=%+p}e#HffXf>4COeXOKO2nznt~5zqbhKovJzy;i<sTg_J1wuR8Yyk{eoEGgf{y@{5CCoLf&#^s*f&E
7OsDMpp`ns2J6*lA>HK;``N%t=9uL$+db(CS-OXV4$?T7zb@*Y0)(I4z5H+g%Gvnk{=^_Xqt>*Y35t{dRxwJk}RN&uJ<%Z;Xx(QI
(Z^Qzg%!dhRqow}%SGWwv8Bf%jtrLZG}~NFOR^oQPiw-
M=b3p^#fvu@{R<tp9?y%U@X1nv0y(zT&}Trx)SSfZ=&~4+MQ7#yihqyh>2Z_TkFSc8^f;ROZ1W<`5_|w$BPjqt$PA;Ar*+9d-
g+yiJZ4kt8$dVp5EbD)1gu7j~gSE*=cw(4q<R&U+};510-
AHus=Wo3qy&*xiBMYY*DZ0h~Y9?+*rcyVY#=`&P5pEp0{WLbmO7J1_;9RljB19lHySak`yW&+avCDD49e*x&V8^GsnP{?#I<5lw<
XNEs%G8#&H4;A^*AtOtLsoYmoOxgaS6?Z85M0G&LOR(rxPi0!8}9HW*8Mwcy~S}IPh?|R_GGKeBryI2qw#{MnfTygA>R-
NM(SWp=bAaiUyuHn$c{(LI-Mm0ePM30>-
F=|WXicER;^n3VCcas~gjXM|qTJ*O$$v;KJ2n;W(I#S>111Q=j1LiiFvI`<GE*HEI;2~XBOMcPhEJ4$nWG;mRjt&X=KI1<woaM4R
LjsY<PCg%U+2x?D(Ds1SP8&0JoQ)P=fM{6={eVHIQh-uZx8oFHFhQB<Q?%nUWaGM3=B`>DNX31;7td+wu;`5{P5R94u)*^U<T-
8IgLdEQ^t#=4)9!VE?Siba;q>+_3yymEBvq}>f7_AD49*1iFziFQ?wtOzy+$K0*<K?t&ltq$+`ShE-ip41R0r)P9}A-
+d=SeB56TTdpFx7Eh;@@u<ZscF;_F`;9Wp!a;gIiA(9y~{n?7ZlzBEY&y+p4LX1r5oQbBgztHh)|smCudRUX@N{KN2d<Z%1}WF!3
L<K3x~M<}sqaxjfl4yYt4aSZ>#{XL&4I$Vx>L}M85PMqr1Alb-
F{UdUJtF+fUbL1a$TT&7<%){x<lt+!+!ry9{fKZ0bl;0UiB`TNs=bp<kf?)nLdFC~fLuAxwnfLzI9HO(DpU~t~yS*vRupQXaRNpp
f`(>Xgx6HO6sfNhtQ!gURa*q@HIWNTJWK^`E3xoSRGnzQtJ!nLkWAZ@$TBh3^8>K87<&BFd6<>ujr4v(svoqcqgz*}45ynAqIAod
Ia=9UwTXBa?vL!E^>M_<%j%Am53hOdEN;;QGQYYOcyk59o=<3~nzI#(=neR*W$H~%?ZjPy%RI#UhIS7;&5qgV-KSwkP>;~;X{nx_
`2SW`?&^~2?_DPQ@(2~fo!fby~L5pY2!`R~@%v}yK1fc26^bmuJF+i!A-
w9N@dIV;G9R=7sBlIdkq+HHRRLd5VYR|0UQr)VtL<i2VHCF-
<A+m^mmZCA*pGWXatRwx~U`HuAqON5!P}G6wmuDwv=?Q>5%tIcbX;wZ2*c(JCcbJ7Z3=!kdgDUBBQI*2Y5#)iP&0aaX)vy8iV9t1
JkKl^bwI;@vnYjmBp#JBVK~%HcR>~u^M{JczgJAScClCieQ(DRGOdsY3>MJiI$))%bNqmZ=N>-
}GEK;i&IV$&B4jmng97W!LTjZ!bCJ{Qi7t{C3>Tywb7f~IGt%;-Y7%`ALVlNirAb=Z=RUYj*1b!%LG|A9#jNc$SJs_kcj25-
#V<W?_LO*$+=TQIqV?CI&h_@e|6{Wn^+w)PDt7?p8wB7P6nb7@}{rM;R_6^?;<aG1xR^@bml|uQ?Kcz_ihH2e~$d;#SktPoSqB*J
LBG-Gn#iU1bgpP?Iz_q{xaJmd_mS0|_ZhY9v;1Wep5y=ZQU<)u;x`}~t!HZHsRiRg+_V-UW=l@u`?u|d~xs@UhIjNYFk_Gfv#gnu
JWYTcI%7aLI5c@&2N%Ks|!fY`DRj4fxhkc&TyakQ`odBPw&LZ_<PGsHFk8&hTaqOUCiA_VFZOJ^at6amY=#<{hSw|}}!z3rdUBwG
3XXa2~eRGs}z@FVQ0JPDF(J$@}SuIwR>{Y^{m&hgF*G!+E-nd*|Orldzl6wEdRE?bY|3-YI>TEVgB4WeGMU5Z115}ew5q@m-
W0s;IRfZH5XuL;b)m$pnwfX;*Q&swmdC7q4@AH02*wT*qCr(J6bBR+#f0;Zn;)ls47C%glQ2x^Klv&X$ytinV-
E#;uO8fxt2AzAxj=jzA*i2&p+Yg0f$pFa-g*VR;=B>(|B28-7@KbLMT;Q+$hzv9gh40zSQ??421fC)n-
{oI@7qUQA;6LG&JW<7kXoHE|PvJFF*`Dg_&R}i+(`?Vwf+cPCnmyYlKF}M0s@3Y+ok73T8?>P$|3XC$Ko7R0MHYi0lC#tj5weyZA
<LXy3QO+ms+eK_C9l`7<fE1+60F5M&PvlL&Gb3XA(+B>FhY|G&juyXty~C7DE;RlWS319*|5u4P9z3_Ek|=w#v@$gGO*Fq7BHaG{
7*Q4u_?s{O4Lzl{SxGFeWu8S#mAJ&>mxie&2f8J(xHI3z^#@45jw-;N`)ZlKypv2!IvJ8V(-
u~ikDjYNQ<G6D#J>hTVDS+T%lawqoIfd1YUpcPUSk&!hrc_*R0AZl6{w6DR!YAMCc^pNI(WV&6E)o`pYWOXTB#M%?jxgyp&AAO7T
cuiBGapgoallHmt0K@v2rv5&^jJbc&xGPp2Tpr&G)*o=)r4%T$v`u+HLJyrZy1tFH<uiv+pFY~!z7;1DoZfALsX2YYtM6$2i*PU>
(2FMDpdn{|{Jg3SXA%n3lI_ugZ|@qR53ZMbT%BZ1O@l+}lz;2hV#e-G+r!wcr2o9PJB+`)^bvtj0;C3Mi_Lxo9-
aSlbR#zPF^X*zpMfh0IQWhsKjp!l4G1mnq-fOuylz{*%mxQXYU=zcm~_$#2LS%6j%E7)g-b`m~cy?hOO|I?SN*XMQe!3$I-
lh<N5lBLt^bX9R<>Fr$q)=SbXpY8z8^RF*of1X~xyuKEAX<}upRCpL?;edYr-
=C)cdH(UsyN~DMXukgR;lsOYIGES68)7N5JG33)9H<aJp!|*fMjx2rRV#1^R^c31b&5Lz?;BTlte@|qRY(i|NI6`M+Q-
fM^0C%z(9Px7b01#phTUsejqLjHF!>&Y32cY0ABVxX{^|1k<EsxZucsfs{677BadrOk%{6c|(56dpzhCYHky!J~$YlX2p3x&-
dmcpcN~~n=M~{spa#Bo0lVGpIVC(HJz`SO)KhVmi5Bdu&!YK9E{*$Mgxc*|{;jsraQx84LXjOg>uFuck@PXa$wp!nVSD(Iod~?mm
M#E~`tT6z686GWo?1@K^Vh!<RXHQf=7!0Z}AfhrDC~r2bBFsep&;~!-
%k}LGp3f1}<wAbhpi3~(PsBlghf_GdXe2PZ73vyzNna2(=oXo%vBI5k+dy|;dJ^XMJW64)ZQ!SvFcu@FC&Fo)$Dw(&9S<oUH92jY
d7WjR$~IYAn($k1>61qO7C5?BOttiOY3$_bmJAr<7X2c}RFTCy#*|YzVe~trUz`1aU(BuiG0{^iefHopPkg%)L#@oKv{X{1g$xLX
Bkx&fc)6mct9eH}@%N-uj>nWy>7U@wgAaYnXZc?G<PoVH$Ic^#V6=M^DCZ-
)a_olPa&1*d>T+>3Y>vod^8<cw(e$}RD^Prye=C@&yjLm&Hn&v>)A&&j9&oh)n2%T3DwW%jeu7!~SHn+|%?$5nx@ai<G_wIn9kcZ
B^{zZ|3mztO$hEGeVa=JRARYlLh|yb$!q!x-L+z<i=y^NtO<qt=>z1xe-
;TSJL;YpfnF%st_CBLll&vj_vkiwb%hX|HGs?`$i<NZQ&AlkC89A3=`3)fKn-
_;~{4H2XVL&AnlE?)nxuh)yi@97LwX!(UW`o7%N&5HF9@C<@CMz@fNfo>vgV+z(b^Xio;1<ufsA$OhkEc*-AOkZ;GgvTC_37-
E1IneW*Cyr0RKB>#_VpOBHa0MWFkaK;X!`vnf<sP#|7avY&7&~?QYabf&v1aSID1_4V(0+Fwv9BT;3ZzA4XE%Vca)GmLm0MLZIUJ
FET(=nIYMZP4uWQ@zshOqdOAJvHq`whLHgd9m?>ySVCW-_aWCTk2?t02K@>&_2p8V87z~-
)9#}f)!}R3<*+UrLqZVv4`aIl+<*WOkI=VhO{|mt}6i@tT9XqNIsi*o3?*mWjLpg@}u0F)8ZFf0+>Oe2?Nw=t4YyxbSF6%>D6#@s
aVBu{A1U|8PvYErlPY??9TP&9)`p1+Nnu<ZfdW4atpyCzM(tV%ltS@A4b6wX&#HV8oL<s8T1E`gx3s!q5sisN`t*AB{LQrXbe*X>
U{Qb9KZ45Hj0+p-P?1Hs8=v!cY)|w=L+h8XS2CaU-
1>&ZLO_0XaXl#+ZuUR1Rp$=aydhMxKzyji4zS#PUgamPZsDMU5;IK`^n^lFSG2t5Fh-
|ChhFu0F*)n7CiAA%syWM`f*|i3}e#hz~6z&}a5PA%ih*ibH1qx>@+tFmLhTUm{5pDPEZhO#aff0>ku-aC;17>x<)gHh<P)P(Bbh
;fhw+F2rSnMq<Yqp_Xuh$*4JN@Qh(51potJMW+_rW-~+W<j;&0f!L+dZq->-
YLFB`k#cuH9^b^$!E+cL>me$+YcutJi6E1_M~C9+d)hIvuF#b=$CV?PjNgu9M&X`XB!X(ThVe
'''
def checked(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin

def main():
    assert len(sys.argv)==3
    mode=sys.argv[1];assert mode in ('sources','build','verify')
    out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())))
    checked(raw,PAYLOAD_PIN);files=json.loads(raw);assert set(files)==set(SOURCE_PINS)
    for name,text in files.items():
        data=text.encode();checked(data,SOURCE_PINS[name]);p=out/name
        if p.exists():assert p.read_bytes()==data
        else:p.write_bytes(data)
    if mode!='sources':
        report=out/'auxiliary_trace_v1.json'
        subprocess.run([sys.executable,'-S',str(out/'auxiliary_trace_v1.py'),mode,str(report)],check=True)
        checked(report.read_bytes(),REPORT_PIN)
    print('AUXILIARY_TRACE_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
