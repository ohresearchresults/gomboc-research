# minimum-0130

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FACET_FIXED_UNIFORM_CENTROID_BASAL_A_REGULARIZATION_V1

## 1. Main advance and its boundary

**The entire octagonal-base E17 sector in which all four weak A edges are basal is regularizable.** More generally, let P be any full-dimensional convex three-polytope of uniform density, at its actual volume centroid g0. Suppose its only physical weak equilibria are simple A=VE points, and both endpoints of every weak edge belong to one true facet B. Then arbitrary-small, full-lattice-preserving regularization is possible under either of these sufficient hypotheses:

**Two-outside-vertex hypothesis:** at most two actual vertices lie outside B. No restriction is imposed on the geometry of B, the relative apex heights, symmetry, covariance, contact-tensor rank, or the number of basal A contacts.

**Source-star hypothesis:** at each weak source x, every nontriangular maximal facet incident to x contains its outgoing weak edge. There may be any number of vertices outside B.

Both statements produce genuine rational or analytic realization curves, preserve the true uniform centroid exactly, retain all original strict feature-labelled S/U/H equilibria, and create no new strict or weak equilibrium. Their positive escape derivatives occur at the **original body**. They are not conclusions from a formal dimension count.

For V10/E17/F9 with an octagonal facet, the first hypothesis is automatic. Thus the theorem covers **every realization of every octagonal-base two-apex type when all four physical weak edges are edges of that octagon**. It does not require the source-star hypothesis in that case.

A second advance is a complete local rational coordinate construction for the actual vertex/facet realization space of any convex three-polytope. It gives the correct constrained contact stress equations and a second-order criterion that retains the curvature of maximal-facet coplanarity. On E17 the labelled realization space has dimension23, its own-centroid slice has dimension20, and the omitted coplanarity reactions form a seven-dimensional space. These are accompanied by actual local realization curves, not just a count of variables and equations.

**Not closed:** four-A configurations whose endpoints do not lie in one suitable facet; general E17 geometries without an octagonal facet; and the remaining mixed A/B and VF sectors. No full E17 regularization theorem, E17 exclusion, weak110 seed, or new110 attainer is claimed. The accepted bracket34≤C_min≤622 is unchanged.

## 2. Input authority and verification status

The retained attempt read the complete1633-line `research-journal(20260920-140602).md`, including the entire literal required parent and its executable recovery. The journal has299924 UTF-8 bytes and SHA-256 `3ad062362f64dd6c3f8829cf1b037d9c5daea2b3febf8e991bac77d23b9fe293`.

The authoritative parent is `minimum-0124`, SHA-256 `d15731e30bb7caaca85ce42b9f642ed39c686418a6fd534e617f266fa0d5fde8`, literal title `NO_FREE_FOUR_A_MATCHING_LOW_RANK_AND_FOUR_TYPE_RESIDUAL_V1`. The journal’s shorter title is an alias, not a different construction. Its authenticated compact JSON envelope has45932 bytes. Its simplicial scope is essential: the parent does not license independent motions of vertices incident to nontriangular maximal facets.  

The proofs below are self-contained beyond the physical simple-A convention. The exact static probes retained from the unfinished attempt found the three pure-four-A controls and eight mixed negative controls described below. **The final consolidation run’s terminal output was not recoverable in this resumed executor.** Accordingly, I do not claim an observed new source-only cold replay, invent terminal byte counts or SHA values, or claim an observed certificate on the fixed interval1/65536. The complete standalone verifier below instead defines an analytically guaranteed positive rational interval, emits its exact certificate and hashes, and can be continued without any predecessor code or workspace file. The mathematical regularization theorems do not depend on that execution receipt.

## 3. A facet-fixing affine correction of the actual centroid

Let ell be an affine function vanishing on B and positive inside P. For a nearby actual body K with centroid g, define

    F_K(x)=x+ell(x)(g0−g)/ell(g).                         (1)

This is an affine map. It fixes **every point of B pointwise**, not merely the contact sources, and

    F_K(g)=g0,
    det D F_K=ell(g0)/ell(g)>0.                          (2)

To verify the determinant, write ell(x)=n·x+b and use the rank-one determinant identity. The numerator is ell(g)+n·(g0−g)=ell(g0). Both quantities are positive near the original body because g0 is strictly inside P.

An affine image of a uniformly filled body is again uniformly filled, up to one constant density factor. Its volume centroid is the affine image of the original volume centroid. Thus(1) corrects the **true** centroid exactly. It does not transport a projective density, choose free cell masses, or replace the primal centroid by a polar centroid.

This observation separates the two tasks. First construct a genuine nearby realization with the desired basal escape and the base plane fixed. Then apply(1). The correction changes none of the basal endpoints, so it changes none of their escape values relative to the fixed g0. As K approaches P, F_K approaches the identity.

The condition ell(g0)≠0 is substantive. An arbitrary plane through the centroid does not support this correction: the displayed determinant would vanish. A true facet automatically avoids that problem.

## 4. Proof under the two-outside-vertex hypothesis

Let o be the orthogonal projection of g0 onto aff B. For every base vertex b, put p=b−o and prescribe

    b(s)=o+p/(1−s|p|²).                                 (3)

For sufficiently small s this is a strictly convex polygon in the same plane with the same cyclic vertex labels. No uniform radial symmetry or location of o inside B is needed for this local assertion.

For a weak basal edge x→y, write u=y−x, r=|x−o|² and q=|y−o|². Since u is parallel to B,

    (x−g0)·u=(x−o)·u=0,
    q−r=|u|²>0.

Moreover r>0. A source equal to o would have radial supporting plane B, exposing the entire facet rather than a simple VE edge. Direct substitution into(3) gives the exact escape

    (x(s)−g0)·(y(s)−x(s))
       =s r(q−r)/[(1−sr)²(1−sq)]>0.                    (4)

It remains to extend the polygon deformation to the **actual full lattice**.

Every maximal facet other than B contains at most two vertices of B, because two distinct facets intersect in at most an edge. With at most two vertices outside B, such a side facet is a triangle or a quadrilateral. A quadrilateral must contain both outside vertices a,b and one true base edge. Its two outside vertices are adjacent on its boundary, so [a,b] is a true edge. Consequently there are at most two such quadrilaterals.

With one outside vertex, hold it fixed. With two outside vertices and no quadrilateral, hold both fixed. Every changed side facet is then a triangle.

If there are one or two quadrilaterals, hold a fixed. For each quadrilateral form the plane through a and its two newly prescribed base endpoints. At the original body, the two planes, when both occur, are distinct and have independent normals. Choose enough fixed auxiliary planes through the old b so that these side-plane equations and the auxiliary equations form a nonsingular3×3 system. With two quadrilaterals one auxiliary plane suffices; its normal can be chosen to have nonzero scalar product with b−a. Solve this system for b(s).

This is an explicit rational/analytic construction through the original b. It retains every quadrilateral coplanarity identically. All other side facets remain triangles. The original strict nonincidence inequalities and polygonal face inequalities persist for sufficiently small s, so the designated faces remain the actual maximal facets of the convex hull, with precisely the original full lattice.

Finally apply(1) to this genuine lifted body. Its base is fixed pointwise by the correction; hence all the exact positive escapes(4) survive. This proves the first theorem, including unequal apex heights and every two-apex incidence type.

## 5. Proof under the source-star hypothesis

This supplies another genuine class without limiting the number of outside vertices.

The simple A contact graph is a rooted forest: a source has one outgoing weak edge, and squared distance from g0 strictly increases along every arrow. For each root set its velocity to zero. Process the other vertices in target-before-source order. For edge i, x_i→y_i with u_i=y_i−x_i, choose

    a_i=[1+|(x_i−g0)·h_(y_i)|]/|u_i|²,
    h_(x_i)=a_i u_i.                                    (5)

Vertices which are not weak sources have velocity zero. Then the derivative of the fixed-g0 escape on edge i is

    a_i|u_i|²+(x_i−g0)·h_(y_i)≥1.                      (6)

Every moving source stays in B. By hypothesis it also stays in every incident nontriangular facet plane: its direction is its weak-edge direction, and that edge is contained in each such facet. Therefore **all nontriangular maximal facet planes remain fixed exactly** under the straight raw vertex motion. Triangular faces need no additional coplanarity constraint. Strict support and convexity guards again retain the full lattice for small s.

Apply the facet-fixing correction(1). Both endpoints of every weak edge remain unchanged by it, so(6) is the true own-centroid escape derivative. This proves the second theorem.

The hypothesis concerns true maximal facets. An integration triangulation of a polygon does not satisfy it by converting that polygon into independent triangular faces.

## 6. The complete local realization space, with nonlinear recovery

Normalize the original actual centroid to0 and write the true facet inequalities as q_f·x≤1. Use actual vertices x_v and actual poles q_f as variables. Their incidence equations are

    q_f·x_v=1  for each literal vertex–facet incidence.  (7)

There are2E equations and3(V+F) variables. The incidence graph, with vertex nodes and facet nodes, is a simple planar bipartite graph. Every nonempty subgraph therefore has a node of degree at most three.

At a facet node, any at most three neighboring vertex vectors are linearly independent. They are distinct extreme points of a convex polygon in an affine plane not containing0. The corresponding statement at a vertex node follows from its actual polar facet. This is a geometric independence statement, not generic-position sampling.

A complete local rational chart follows by repeated degree-at-most-three removal. At each removed node record its remaining neighbors. If there are d neighbors, select d coordinate columns giving a nonsingular d×d minor of their vectors; the other3−d coordinates are free parameters. Reinsert nodes in reverse order, solving their d dot-product equations for the selected coordinates. The original minors remain nonzero in a neighborhood, and every incidence equation is satisfied exactly. The inverse chart reads the designated free coordinates. Strict support and polygon guards make every nearby chart point a genuine convex realization of the same full lattice.

The same removal argument proves that the differential C of(7) has full row rank. A nonzero row dependence would have a support graph in which every participating node had at least four incident nonzero coefficients, contradicting planar bipartite3-degeneracy. Thus

    rank C=2E,
    dim realization space=3(V+F)−2E=E+6.                 (8)

Translations show that the actual centroid derivative on this space is onto R³. For translation velocity a, take h_v=a and k_f=−(q_f·a)q_f; these satisfy the incidence differential, and Dg=a. The own-centroid level set is consequently a smooth local space of dimension E+3.

For V10/E17/F9 these dimensions are23 and20. Fixing a labelled affine four-vertex frame leaves11 local parameters. The point is not the count alone: the reverse linear solves above integrate the tangent data into genuine rational realization curves.

## 7. Correct full stresses and second jets on nonsimplicial bodies

Choose an outward triangulation of each maximal facet for **integration only**. Let A_v be the derivative of the resulting boundary-moment polynomial extension. Individual A_v off the realization space may depend on that triangulation; they must not be called independently available vertex actuators.

For h_v=δx_v and k_f=δq_f, the incidence derivative is

    (C(h,k))_(v,f)=q_f·h_v+x_v·k_f.                      (9)

At actual g0=0 the contact derivative is

    (Q(h,k))_i=(u_i−x_i)·h_(x_i)+x_i·h_(y_i)
                             −u_i·Σ_v A_v h_v.          (10)

The actual tangent space is ker C. A first-order regularization exists exactly when there is no nonzero alpha≥0 and signed incidence multiplier lambda satisfying

    Q^T alpha=C^T lambda.                               (11)

Equivalently, with c_alpha=Σalpha_i u_i and the literal endpoint forces F_v(alpha), every vertex and facet equation must hold:

    F_v(alpha)−A_v^T c_alpha=Σ_(f contains v)lambda_vf q_f,
    Σ_(v in f)lambda_vf x_v=0  for every maximal facet f. (12)

The second line also implies Σ_(v in f)lambda_vf=0. Thus these are genuine affine dependencies in the facets. Their total dimension is

    Σ_f(|f|−3)=2E−3F=7  on E17.                         (13)

The map from these multipliers to vertex loads is injective, by full row rank of C. These seven **coplanarity reaction modes** are not independent physical masses or the seven false-completion directions from older moment relaxations. Ignoring them would substitute the simplicial full-stress equations for a different deformation problem.

All global affine and genuinely refilled projective motions remain admissible, so(11) still implies the corresponding tensor and projective identities. Those necessary identities do not replace(12).

### Contact-zero affine rank lifting

Let T_i=sym(x_i u_i^T), W=span T_i. A metric M=I+epsilon H with H∈W^perp is realized by an actual affine image and preserves all contact equalities exactly. In a fixed original realization chart, replace each dot product in(10) by the M-bilinear form to obtain Q_M.

If the four tensors have rank three and unique positive relation alpha, a sufficient test is

    alpha^T Q_H is nonzero on ker C
    for some H∈W^perp.                                 (14)

At a body already carrying the constrained stress alpha, any sufficiently small nonzero affine parameter then destroys it: no other tensor-relation line can become a full constrained stress. The local rational chart supplies a positive actual shape velocity and its nonlinear realization.

For lower tensor rank, take a basis L of all tensor relations and a basis K of ker C. The exact matrix family

    D(M)=K^T Q_M^T L                                    (15)

handles every possible future signed stress. A nonidentically-zero maximal minor gives a contact-preserving affine image arbitrarily close to the original one at which D is injective. This is a finite polynomial test using the **same actual body and actual centroid derivative**. Failure of the test is not an exclusion theorem or an all-orders obstruction.

### The curvature term that must not be dropped

Write an actual realization curve as z(s)=z0+s z1+s² z2+O(s³), with z1=(h,k). From(7),

    C z1=0,
    C z2=−d,
    d_(v,f)=h_v·k_f.                                   (16)

Suppose also Qz1=0. Compute the complete straight-vertex moment coefficients from the outward integration triangles. If d0,d1,d2 are the determinant coefficients of orders0,1,2, and z0,z1 are the corresponding sums of positions and velocities, then

    V1=Σd1/6,
    J1=Σ(d1 z0+d0 z1)/24,
    J2=Σ(d2 z0+d1 z1)/24,
    g1=J1/V,
    g2=J2/V−V1 J1/V²,
    b_i=(h_(x_i)−g1)·(h_(y_i)−h_(x_i))−u_i·g2.          (17)

All shared-triangle mixed determinants occur in d2. For every constrained stress pair in(11), the intrinsic second-order pairing is

    alpha·b−lambda·d.                                  (18)

If(18) is positive for every nonzero alpha in the entire nonnegative constrained cone, strict separation supplies z2 satisfying(16) and b+Qz2>0. The rational chart realizes these compatible first and second jets by an actual nonlinear curve. Exact centroid subtraction completes the physical regularization. The expression is invariant under changing the integration triangulation; the off-manifold pieces and the coplanarity correction cannot be separated.

This is a sufficient second-order theorem, not a claim that every remaining E17 stress passes it.

## 8. Actual E17 controls and a precise one-vertex method boundary

Use the base vertices in z=0

    b0=(1,0,0),       b1=(1,h0,0),
    b2=(0,1,0),       b3=(−h1,1,0),
    b4=(−1,0,0),      b5=(−1,−h2,0),
    b6=(0,−1,0),      b7=(h3,−1,0),

and outside vertices (0,a,H),(0,−a,H). Integrate this true body, obtaining g. The affine shear

    S=[[1,0,−g_x/g_z],[0,1,−g_y/g_z],[0,0,1]]             (19)

fixes the base pointwise and puts its actual centroid on the z-axis. Subtract Sg. This is a complete rational construction, not a prescribed centroid in place of integration.

All controls below have true maximal facet sets

    01234567, 0189, 079, 128, 238, 348, 4589, 569, 679.

Their outward cycles are

    (0,7,6,5,4,3,2,1), (0,1,8,9), (0,9,7),
    (1,2,8), (2,3,8), (3,4,8), (4,5,9,8),
    (5,6,9), (6,7,9).

The seven integration diagonals are not true edges. There are17 true edges,34 incidences and68 mechanical primitives.

### Three pure-four-A bodies

Take a=1/2,H=2 and respectively

    (h0,h1,h2,h3)=(1/4,1/3,1/5,2/5),
                  (1/3,1/4,1/3,1/5),
                  (1/3,1/2,1/4,1/5).

Their volumes are431/180,427/180,437/180. After(19), their raw centroids are respectively

    (0,0,551/862), (0,0,547/854), (0,0,557/874).

Each has strict8/6/12 and exactly four physical weak points, all simple A on0→1,2→3,4→5,6→7. All64 other primitives are nonzero. Both outside vertices are free, of true degree five.

The source points have one common squared distance from the actual centroid. With alpha_i=1/h_i, the four tensors have rank three and

    Σalpha_i T_i=0,  Σalpha_i u_i=0.

Thus the whole global affine/projective first-jet matrix has rank three and a positive stress. No affine metric can make all four designated escape values positive. Nevertheless the genuine constrained shape matrix has rank four: the explicit curve below has a positive derivative in every row, while any signed dependence would have to be the displayed positive tensor relation.

These are actual nonsimplicial controls of the distinction between global first-order stress and genuine realization motion. They are not constrained full-shape-stress obstructions or110 bodies.

### A complete rational own-centroid arc for the first body

Put gamma=551/862. After(19), its outside vertices are

    a8=(−194/8265, 5593/11020,2),
    a9=(−194/8265,−5427/11020,2).

Initially subtract (0,0,gamma) from every listed vertex. Move the four raw sources to

    b0(s)=(1,s,0), b2(s)=(−s,1,0),
    b4(s)=(−1,−s,0), b6(s)=(s,−1,0),                    (20)

leaving the four targets fixed. Translate **both** raw outside vertices by

    w_x(s)=−3s(2553−551s)/[551(551−169s)],
    w_y(s)=−4s(551s−196)/[551(551−169s)],
    w_z(s)=−40560s/[431(551−169s)].                      (21)

Then subtract the same fixed (0,0,gamma). These formulas specify every vertex of the final body, with no implicit root or missing checkpoint.

Before the correction(21), direct uniform integration gives

    V_raw(s)=(431−169s)/180,
    J_x(s)=s(2553−551s)/132240,
    J_y(s)=s(551s−196)/99180,
    J_z(s)=(551−169s)/360.                              (22)

For example, the base is the square with four corner triangles removed, of area(311−169s)/120; its true slices against the outside segment also derive(22). The correction is exactly(1): its linear part is

    [[1,0,−J_x/J_z],
     [0,1,−J_y/J_z],
     [0,0,gamma V_raw/J_z]].                            (23)

Both outside vertices have raw height2, so(23) gives their common translation(21). The final actual centroid is therefore **exactly0 for the whole curve**, and its volume is

    V_actual(s)=551(431−169s)²/[77580(551−169s)].          (24)

Each weak escape is exactly

    phi_i(s)=s(h_i−s).                                  (25)

All base and quadrilateral coplanarities are retained identically. The verifier below constructs a positive rational epsilon≤1/65536 and certifies every support, every face polygon, all64 old primitive signs and the four positive quotients on the entire interval0<s≤epsilon. Original strict8/6/12 labels persist and weak000 holds there. This is an analytically guaranteed interval construction, not a sampled sign check or an assertion that the unread final run certified the fixed endpoint1/65536.

### Why an independent free-vertex actuator is genuinely unavailable here

Hold every vertex except a8 fixed. Its two incident quadrilateral planes are fixed by their other three vertices. Therefore a8 must stay on their exact intersection line, namely the line through a8,a9. Its admissible local configuration is one-dimensional, not three-dimensional. Its centroid image cannot contain a three-dimensional neighborhood, even to arbitrary order. The same is true of a9 alone.

With the base fixed, the two outside vertices together instead have four genuine local degrees of freedom and a rank-three centroid derivative. The three-dimensional family of affine maps fixing the base pointwise already supplies those centroid directions. This is an actual method boundary for independent-vertex rescue, not an obstruction to complete regularization.

The old radial prescription also fails maximal-facet coplanarity at first order. For the centred base, moving each vertex by |v|²v gives

    d/ds det(v1(s)−v0(s),v2(s)−v0(s),v3(s)−v0(s)) at0
      =−gamma h0 h1(h0+h1)=−3857/124128≠0.               (26)

Thus it leaves the nonsimplicial realization stratum immediately.

### Eight retained negative controls: not four-only

With h0=h1=h2=h3=1/3, use

    (a,H)=(1/2,2),(1,2),(2,2),(1/2,1),(1,1),
          (3/2,3/2),(2/3,4/3).

Also retain h=(1/4,1/3,1/4,1/3),a=1/2,H=2. All eight are true10/17/9 bodies, but each has **four A plus two additional simple EF points** on edges2–8 and6–9. Their strict counts are respectively7/6/11,5/6/9,5/6/9,5/6/9,5/6/9,5/6/9,7/6/11,7/6/11. Each has six zero primitives, not four. The complete same generators, actual centroid correction and mechanical audits are retained below. These symmetric controls must not be relabelled as pure-four-A examples.

## 9. Exact recovery and continuous certificate

Save the following complete source as `basal_e17_recover.py`. It imports no parent source. Target environment is CPython3.13.5, SymPy1.14.0 and its mpmath1.3.0 dependency, with assertions and PYTHONHASHSEED=0. No random input, numerical optimizer, external file or network is used.

    export PYTHONHASHSEED=0
    python basal_e17_recover.py build
    python basal_e17_recover.py check

The expected terminal marker is `BASAL_E17_RECOVERY_PASS`. The program emits source/report byte counts and SHA-256 values. Those are reconstruction outputs; no unobserved literal digest or cold-parity claim is supplied here.

The interval rule is itself a proof. For every positively oriented numerator and denominator polynomial p(s)=p0+Σ_(j≥1)p_j s^j, set

    epsilon=min(1/65536,
                all p0/[2(1+Σ_(j≥1)|p_j|)]).             (27)

Every p0 is strictly positive at the original body, including the four divided weak escapes. Thus epsilon is an explicitly reconstructible positive rational. For0≤s≤epsilon, the nonconstant terms have absolute sum less than p0/2. The same bound proves every Bernstein coefficient positive, since its binomial ratios are at most1. The code returns all218 rational guards and their436 cleared polynomials and Bernstein vectors, not abbreviated arrays. It also independently re-hulls and re-integrates the endpoint and checks the complete incidence first and second jets.

```python
'''BASAL_E17_FACET_FIXER_RECOVERY_V1.
Exact static controls, full realization derivatives and a whole rational arc.
python basal_e17_recover.py build|check
Target: CPython3.13.5, SymPy1.14.0, mpmath1.3.0; assertions, no RNG.
'''
from pathlib import Path
from itertools import combinations
from math import comb
import hashlib,json,sys
import sympy as s
assert __debug__ and s.__version__=='1.14.0'
R=s.Rational; Z=s.zeros(3,1); I=s.eye(3); t=s.Symbol('t')
PARENT='minimum-0124'
PARENT_SHA='d15731e30bb7caaca85ce42b9f642ed39c686418a6fd534e617f266fa0d5fde8'
CAP=R(1,65536)
CONTACTS=[(0,1),(2,3),(4,5),(6,7)]
CY=[(0,7,6,5,4,3,2,1),(0,1,8,9),(0,9,7),(1,2,8),
    (2,3,8),(3,4,8),(4,5,9,8),(5,6,9),(6,7,9)]
FS=[tuple(sorted(f)) for f in CY]
TRI=[(f[0],f[j],f[j+1]) for f in CY for j in range(1,len(f)-1)]
EDGES={}
for fi,f in enumerate(CY):
    for j in range(len(f)):
        e=tuple(sorted((f[j],f[(j+1)%len(f)])))
        EDGES.setdefault(e,[]).append(fi)
EDGES=dict(sorted(EDGES.items()))
assert len(EDGES)==17 and all(len(v)==2 for v in EDGES.values())
BASIS=[]
for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
    H=s.zeros(3); H[i,j]=H[j,i]=1; BASIS.append(H)
LENGTHS=[(R(1,4),R(1,3),R(1,5),R(2,5)),
         (R(1,3),R(1,4),R(1,3),R(1,5)),
         (R(1,3),R(1,2),R(1,4),R(1,5))]
NEG=[((R(1,3),)*4,a,H) for a,H in
     [(R(1,2),2),(1,2),(2,2),(R(1,2),1),(1,1),
      (R(3,2),R(3,2)),(R(2,3),R(4,3))]]
NEG.append(((R(1,4),R(1,3),R(1,4),R(1,3)),R(1,2),2))
def clean(x):
    return x.applyfunc(s.cancel) if isinstance(x,s.MatrixBase) else s.cancel(x)
def det(a,b,c): return a.dot(b.cross(c))
def enc(x):
    if isinstance(x,s.MatrixBase): return [[enc(v) for v in r] for r in x.tolist()]
    if isinstance(x,s.Basic): return str(x)
    if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [enc(v) for v in x]
    return x

def lattice(X):
    found=set()
    for i,j,k in combinations(range(len(X)),3):
        n=(X[j]-X[i]).cross(X[k]-X[i])
        if n==Z: continue
        vals=[n.dot(x-X[i]) for x in X]
        if min(vals)<0<max(vals): continue
        found.add(tuple(a for a,v in enumerate(vals) if v==0))
    assert sorted(found)==sorted(FS)
    normals=[]
    for f,cy in zip(FS,CY):
        i,j,k=cy[:3]; n=(X[j]-X[i]).cross(X[k]-X[i]); normals.append(n)
        assert n!=Z
        for v in range(len(X)):
            z=n.dot(X[v]-X[i])
            assert z==0 if v in f else z<0
    pair_edges=set()
    for a,b in combinations(FS,2):
        v=tuple(sorted(set(a)&set(b)))
        if len(v)==2: pair_edges.add(v)
        else: assert len(v)<=1
    assert pair_edges==set(EDGES)
    for v in range(len(X)):
        assert s.Matrix.hstack(*(normals[f] for f,cy in enumerate(CY) if v in cy)).rank()==3
    assert len(X)-len(EDGES)+len(CY)==2

def mass(X,apex=None,second=True):
    if apex is None: apex=Z
    V=s.S(0); J=Z.copy(); Q=s.zeros(3); weights=[]
    for f in TRI:
        p=[apex]+[X[v] for v in f]
        d=det(p[1]-apex,p[2]-apex,p[3]-apex); z=sum(p,Z)
        weights.append(clean(d)); V+=d/6; J+=d*z/24
        if second:
            Q+=d*(z*z.T+sum((x*x.T for x in p),s.zeros(3)))/120
    return clean(V),clean(J),clean(Q),weights

def poles(X):
    out=[]
    for f in CY:
        i,j,k=f[:3]; n=(X[j]-X[i]).cross(X[k]-X[i])
        out.append(clean(n/n.dot(X[i])))
    return out

def mechanics(X):
    qp=poles(X); pv=[[] for x in X]; pf=[[] for f in CY]
    rows=[]; weak=[]; zeros=0
    for (a,b),(f,h) in EDGES.items():
        vals=list(map(clean,[X[a].dot(X[b]-X[a]),X[b].dot(X[a]-X[b]),
             qp[f].dot(qp[h]-qp[f]),qp[h].dot(qp[f]-qp[h])]))
        signs=[int(s.sign(v)) for v in vals]; zeros+=signs.count(0)
        pv[a].append(signs[0]); pv[b].append(signs[1])
        pf[f].append(signs[2]); pf[h].append(signs[3])
        rows.append([a,b,f,h,vals])
        if max(signs)==0: weak.append([a,b,signs])
    return {'poles':qp,'rows':rows,'weak':weak,'zeros':zeros,
       'S':[i for i,v in enumerate(pf) if max(v)<0],
       'U':[i for i,v in enumerate(pv) if max(v)<0],
       'H':[(a,b) for a,b,f,h,v in rows if all(z<0 for z in v)]}

def control(lengths,a=R(1,2),height=2,pure=True):
    h0,h1,h2,h3=lengths
    raw=list(map(s.Matrix,[(1,0,0),(1,h0,0),(0,1,0),(-h1,1,0),
       (-1,0,0),(-1,-h2,0),(0,-1,0),(h3,-1,0),(0,a,height),(0,-a,height)]))
    lattice(raw)
    V,J,Q,d0=mass(raw,raw[0]); V2,J2,Q2,d8=mass(raw,raw[8])
    assert V==V2 and J==J2 and Q==Q2 and all(d>=0 for d in d0+d8)
    g=J/V; S=I.copy(); S[0,2]=-g[0]/g[2]; S[1,2]=-g[1]/g[2]
    raw=[S*x for x in raw]; g=S*g; X=[x-g for x in raw]
    lattice(X)
    v,j,q,d0=mass(X,X[0]); v2,j2,q2,d8=mass(X,X[8])
    assert v==v2==V and j==j2==Z and q==q2 and all(d>=0 for d in d0+d8)
    mm=mechanics(X); expected=[[a,b,[0,-1,-1,-1]] for a,b in CONTACTS]
    if pure:
        assert mm['weak']==expected and mm['zeros']==4
        assert [len(mm[k]) for k in ('S','U','H')]==[8,6,12]
    else:
        assert mm['zeros']==6 and len(mm['weak'])==6
        assert all(w in mm['weak'] for w in expected)
        extra=[w for w in mm['weak'] if w not in expected]
        assert extra==[[2,8,[-1,-1,-1,0]],[6,9,[-1,-1,-1,0]]]
    cov=q/V; alpha=s.Matrix([1/h for h in lengths])
    T=s.Matrix([[(X[a].T*H*(X[b]-X[a]))[0] for H in BASIS] for a,b in CONTACTS])
    P=s.Matrix.vstack(*((5*cov*(X[b]-X[a])-X[a].dot(X[a])*(X[b]-X[a])).T for a,b in CONTACTS))
    assert T.rank()==3 and T.T*alpha==s.zeros(6,1)
    assert T.row_join(P).rank()==3 and P.T*alpha==Z
    assert sum((w*(X[b]-X[a]) for w,(a,b) in zip(alpha,CONTACTS)),Z)==Z
    return {'lengths':lengths,'a':a,'height':height,'shear':S,'raw':raw,
       'centroid_raw':g,'X':X,'V':V,'covariance':cov,'positive_fans':[d0,d8],
       'mechanics':mm,'tensor_rows':T,'projective_rows':P,'global_stress':alpha,
       'scope':'PURE_FOUR_A' if pure else 'FOUR_A_PLUS_TWO_EF'}

def realization_data(rec):
    X=rec['X']; qp=rec['mechanics']['poles']; vals=X+qp
    labels=[(v,f) for f,cy in enumerate(CY) for v in cy]
    C=s.zeros(34,57)
    for r,(v,f) in enumerate(labels):
        C[r,3*v:3*v+3]=qp[f].T
        C[r,3*(10+f):3*(10+f)+3]=X[v].T
    assert C.rank()==34
    K=s.Matrix.hstack(*C.nullspace()); assert K.cols==23
    A=[]
    for w in range(10):
        B=s.zeros(3)
        for i,j,k in TRI:
            if w in (i,j,k):
                n=(X[j]-X[i]).cross(X[k]-X[i])
                B+=(X[i]+X[j]+X[k]+X[w])*n.T
        A.append(clean(B/(24*rec['V'])))
    assert sum(A,s.zeros(3))==I
    G=s.Matrix.hstack(*A,s.zeros(3,27)); Q=s.zeros(4,57)
    for row,(a,b) in enumerate(CONTACTS):
        x=X[a]; u=X[b]-x
        Q[row,:]=-u.T*G
        Q[row,3*a:3*a+3]+=(u-x).T
        Q[row,3*b:3*b+3]+=x.T
    assert (G*K).rank()==3 and (Q*K).rank()==4
    assert s.Matrix.vstack(C,G).rank()==37
    assert s.Matrix.vstack(C,G,Q).rank()==41
    fixed=s.zeros(24,57)
    for j in range(24): fixed[j,j]=1
    N=s.Matrix.hstack(*s.Matrix.vstack(C,fixed).nullspace())
    assert N.cols==4 and N[:30,:].rank()==4 and (G*N).rank()==3
    singles=[]
    for w in (8,9):
        E=s.zeros(27,57); row=0
        for v in range(10):
            if v==w: continue
            for k in range(3): E[row,3*v+k]=1; row+=1
        N1=s.Matrix.hstack(*s.Matrix.vstack(C,E).nullspace())
        assert N1.cols==1; singles.append(N1)
    # Complete rational local chart, with its actual inverse checked at the input.
    adj={i:set() for i in range(19)}
    for v,f in labels: adj[v].add(10+f); adj[10+f].add(v)
    remaining=set(adj); steps=[]; free=[]
    while remaining:
        w=min(v for v in remaining if len(adj[v])<=3)
        nb=sorted(adj[w]); d=len(nb)
        M=s.Matrix.vstack(*(vals[j].T for j in nb)) if d else s.zeros(0,3)
        pc=next(c for c in combinations(range(3),d)
                if not d or M.extract(range(d),c).det()!=0)
        fc=[j for j in range(3) if j not in pc]
        steps.append((w,nb,list(pc),fc)); free.extend((w,j) for j in fc)
        for j in nb: adj[j].remove(w)
        remaining.remove(w)
    assert len(free)==23
    recovered={}
    for w,nb,pc,fc in reversed(steps):
        x=Z.copy()
        for j in fc: x[j]=vals[w][j]
        if nb:
            M=s.Matrix.vstack(*(recovered[j].T for j in nb))
            y=M.extract(range(len(nb)),pc).inv()*(s.ones(len(nb),1)-M*x)
            for j,z in zip(pc,y): x[j]=clean(z)
        recovered[w]=x
    assert [recovered[j] for j in range(19)]==vals
    radial=[x+t*x.dot(x)*x for x in X]
    bad=s.factor(det(radial[1]-radial[0],radial[2]-radial[0],radial[3]-radial[0]))
    assert s.diff(bad,t).subs(t,0)==-R(3857,124128)
    return {'C':C,'incidences':labels,'tangent_basis':K,'moment_extension_G':G,
       'contact_extension_Q':Q,'ranks':[34,37,41],'chart_steps':steps,'chart_free':free,
       'base_fixed_tangent':N,'single_apex_tangents':singles,'illegal_radial_determinant':bad}

def verified_arc(rec,geo):
    raw=rec['raw']; gamma=R(551,862); shift=s.Matrix([0,0,gamma])
    moving=raw.copy()
    directions=[s.Matrix([0,1,0]),s.Matrix([-1,0,0]),s.Matrix([0,-1,0]),s.Matrix([1,0,0])]
    for (a,b),h in zip(CONTACTS,directions): moving[a]=raw[a]+t*h
    V,J,_,_=mass(moving,second=False)
    assert clean(V-(431-169*t)/180)==0
    expected=s.Matrix([t*(2553-551*t)/132240,t*(551*t-196)/99180,(551-169*t)/360])
    assert clean(J-expected)==Z
    L=s.Matrix([[1,0,-J[0]/J[2]],[0,1,-J[1]/J[2]],[0,0,gamma*V/J[2]]]).applyfunc(s.cancel)
    Y=[clean(L*x-shift) for x in moving]
    Vy,Jy,_,_=mass(Y,second=False)
    assert Jy==Z and clean(Vy-551*(431-169*t)**2/(77580*(551-169*t)))==0
    for (a,b),h in zip(CONTACTS,rec['lengths']):
        assert clean(Y[a].dot(Y[b]-Y[a])-t*(h-t))==0
    guards=[]
    def add(label,z):
        p,q=s.fraction(clean(z))
        if q.subs(t,0)<0: p,q=-p,-q
        p=s.Poly(p,t); q=s.Poly(q,t)
        assert p.nth(0)>0 and q.nth(0)>0
        guards.append({'label':label,'p':p.as_expr(),'q':q.as_expr()})
    add('raw_volume',V); add('raw_vertical_first_moment',J[2]); add('affine_determinant',L.det())
    qp=[]
    for fi,cy in enumerate(CY):
        i,j,k=cy[:3]; n=clean((Y[j]-Y[i]).cross(Y[k]-Y[i])); H=clean(n.dot(Y[i]))
        add(['centroid_inside',fi],H); qp.append(clean(n/H))
        for v in range(10):
            z=clean(n.dot(Y[i]-Y[v]))
            if v in cy: assert z==0
            else: add(['nonincidence',fi,v],z)
        for j in range(len(cy)):
            a,b=cy[j],cy[(j+1)%len(cy)]
            for v in cy:
                if v not in (a,b): add(['facet_polygon',fi,a,b,v],det(Y[b]-Y[a],Y[v]-Y[a],n))
    for a,b,f,h,old in rec['mechanics']['rows']:
        vals=[Y[a].dot(Y[b]-Y[a]),Y[b].dot(Y[a]-Y[b]),
              qp[f].dot(qp[h]-qp[f]),qp[h].dot(qp[f]-qp[h])]
        for j,(v,z) in enumerate(zip(old,vals)):
            if v==0:
                assert j==0 and (a,b) in CONTACTS
                add(['weak_quotient',a,b],z/t)
            else: add(['primitive',a,b,f,h,j],s.sign(v)*z)
    assert len(guards)==218
    eps=CAP
    for g in guards:
        for key in ('p','q'):
            P=s.Poly(g[key],t)
            tail=sum(abs(P.nth(j)) for j in range(1,P.degree()+1))
            eps=min(eps,P.nth(0)/(2*(1+tail)))
    assert 0<eps<=CAP
    for g in guards:
        vectors=[]
        for key in ('p','q'):
            P=s.Poly(g[key],t); n=P.degree()
            b=[sum(P.nth(j)*eps**j*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
            assert all(x>0 for x in b); vectors.append(b)
        g['bernstein']=vectors
    # Complete actual incidence curvature, not a frozen-star Hessian.
    curve=s.Matrix.vstack(*(Y+qp))
    h=clean(s.diff(curve,t).subs(t,0)); eta=clean(s.diff(curve,t,2).subs(t,0)/2)
    d=s.Matrix([h[3*v:3*v+3,0].dot(h[3*(10+f):3*(10+f)+3,0]) for v,f in geo['incidences']])
    assert geo['C']*h==s.zeros(34,1) and clean(geo['C']*eta+d)==s.zeros(34,1)
    assert geo['moment_extension_G']*h==Z
    assert geo['contact_extension_Q']*h==s.Matrix(rec['lengths'])
    end=[clean(x.subs(t,eps)) for x in Y]; lattice(end)
    ve,je,qe,de0=mass(end,end[0]); ve2,je2,qe2,de8=mass(end,end[8])
    assert ve==ve2 and je==je2==Z and qe==qe2 and all(x>=0 for x in de0+de8)
    mm=mechanics(end); assert mm['weak']==[] and mm['zeros']==0
    for key in ('S','U','H'): assert mm[key]==rec['mechanics'][key]
    return {'epsilon':eps,'raw_vertices':moving,'raw_V':V,'raw_J':J,'fixer':L,
       'vertices':Y,'actual_V':Vy,'actual_J':Jy,'poles':qp,'guards':guards,
       'first_jet':h,'second_coefficient':eta,'incidence_curvature':d,
       'endpoint':{'X':end,'V':ve,'covariance':clean(qe/ve),
                   'positive_fans':[de0,de8],'mechanics':mm}}

def build():
    pure=[control(h) for h in LENGTHS]
    negative=[control(h,a,H,False) for h,a,H in NEG]
    assert [r['V'] for r in pure]==[R(431,180),R(427,180),R(437,180)]
    assert pure[0]['centroid_raw']==s.Matrix([0,0,R(551,862)])
    assert [len(r['mechanics']['S']) for r in negative]==[7,5,5,5,5,5,7,7]
    geo=realization_data(pure[0]); arc=verified_arc(pure[0],geo)
    return {'identity':'BASAL_E17_FACET_FIXER_RECOVERY_V1','parent':[PARENT,PARENT_SHA],
       'scope':'Basal pure A theorem; negative controls are four A plus two EF. No110 claim.',
       'facets':FS,'cycles':CY,'integration_triangles':TRI,'true_edges':list(EDGES.items()),
       'pure_controls':pure,'mixed_negative_controls':negative,'realization':geo,'arc':arc}

if __name__=='__main__':
    assert sys.argv[1:] in (['build'],['check'])
    obj=build(); data=(json.dumps(enc(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path('basal_e17_recovery.json')
    if sys.argv[1]=='build': path.write_bytes(data)
    else: assert path.read_bytes()==data
    print('BASAL_E17_THREE_PURE_AND_EIGHT_MIXED_CONTROLS_PASS')
    print('INCIDENCE_RANKS_34_37_41_AND_NONLINEAR_JETS_PASS')
    print('EXACT_RATIONAL_INTERVAL_ORIGINAL_STRICT_8_6_12_WEAK000_PASS')
    print('GUARDS',len(obj['arc']['guards']),'CLEARED_POLYNOMIALS',2*len(obj['arc']['guards']))
    print('EPSILON',obj['arc']['epsilon'])
    for p in (Path(__file__),path):
        b=p.read_bytes(); print(p.name,len(b),hashlib.sha256(b).hexdigest())
    print('BASAL_E17_RECOVERY_PASS')
```

## 10. Most useful continuation

The remaining consequential E17 question is now a configuration with weak edges not all contained in a suitable facet, or one failing the source-star lifting condition. Its correct obstruction is the constrained system(11)–(12), including the seven coplanarity reaction modes, not the old independent-vertex equations. The local rational chart makes first- and second-order feasibility genuinely realizable; the unresolved step is proving that the whole nonnegative constrained cone can always be escaped in those remaining geometries. A failed affine rank-lifting test or a failed quadratic test would delimit that method, not establish impossibility of arbitrary-small regularization.
