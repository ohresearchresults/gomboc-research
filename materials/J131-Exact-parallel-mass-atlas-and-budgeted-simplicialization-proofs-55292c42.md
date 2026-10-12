# material-55292c42d13a

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J131 — exact parallel mass charts, local completeness, and an equilibrium-preserving release

These are coordinator-derived mathematical methods, coupled to the explicitly executed J131 DETACHED47 experiments. They do NOT establish an own110 body or finite global cancellation. Canonical own110 remains C622; the E<=249 target remains unmet.

Computational evidence: complete ordered recovery parts1/3 [internal-source-reference],2/3 [internal-source-reference],3/3 [internal-source-reference]. Parts1+2 contain the exact parent, all frozen heights, the complete exact audit/retraction/rank code and all expected outputs; part3 contains the numerical producers, explicit parameters and finite-failure limits. The one stated source-transcription correction in part1 is applied by part2's complete UNPACK131.py. One Fraction audit engine is used, not independent dual verification.

Conceptual source for the final application: the complete immutable KF27J result figure-0610, SHA16bc720d901ab221cc1dcd7b76dbb8a1a6d7abac1e5e961a27da30a8f3714453,80141 bytes, read0 through EOF with unchanged hash. Its FF2_MIN42_G5 and AF2_MIN43_G5 are author-executed exact own121 bodies. Their complete producing archive has not been independently replayed by the coordinator merely to use their findings. The applications below are proved nearby-existence statements, not newly computed coordinates or audited perturbed endpoints.

## 1. Polynomial mass identities with adjacent vertices allowed

Let an oriented, strictly triangular convex polyhedron have rational labelled vertices p_i, i=1,...,N, and outward oriented face set T. Fix a nonzero rational direction v. Allow EVERY vertex to move by its own scalar t_i in that same direction:

p_i(t)=p_i+t_i v.

No independent-star assumption is made: adjacent vertices and all three vertices of one triangle may move. The formula is used only while the nominated strict triangular lattice remains convex.

For f=(a,b,c), write

d_f=det(p_a,p_b,p_c),
p_f=p_a+p_b+p_c,
s_f=e_a+e_b+e_c,
b_f=det(v,p_b,p_c)e_a+det(p_a,v,p_c)e_b+det(p_a,p_b,v)e_c.

Terms with v in two determinant slots vanish. Therefore

d_f(t)=d_f+b_f·t,
p_f(t)=p_f+v(s_f·t).

Define the volume gradient a, the three-by-N linear moment matrix L and symmetric N-by-N matrix B by

a=(1/6) sum_f b_f,
L=(1/24) sum_f [p_f b_f^T+d_f v s_f^T],
B=(1/48) sum_f [b_f s_f^T+s_f b_f^T].

The oriented filled-volume tetrahedral formulas give EXACTLY

V(t)=V0+a·t,
M(t)=M0+L t+v(t^T B t).

These are finite identities, not first-order approximations. The tetrahedra may be signed if the coordinate origin is outside the body; their closed oriented boundary sum still gives the actual filled volume and first moment.

A face normal is affine in t. Its supporting comparison with a fourth vertex is also affine: write the comparison as a determinant of three edge differences; every higher-order term repeats direction v. Thus the strict fixed-lattice hull region for this parallel family is an intersection of affine open halfspaces. This does NOT imply that the actual-centred equilibrium region is convex.

## 2. Three linear equations and an explicit quadratic mass correction

Choose k with v_k nonzero. Impose the three linear equations

a·t=0,
(L_j-(v_j/v_k)L_k)·t=0 for j≠k.

They fix the volume and the two transverse first-moment components. Put ell=L_k/v_k and

q(t)=ell·t+t^T B t.

On this linear slice, M(t)=M0+v q(t). Translate the ENTIRE changed body by -(q(t)/V0)v. The resulting vertices

R_v(t)_i=p_i+[t_i-q(t)/V0]v

have exactly V0, M0 and g0=M0/V0. This is an explicit degree-two polynomial parametrization. The common translation does not undo the independent relative displacements and does not create a free reference centre: all equilibrium signs must be recomputed relative to the actual centroid of the translated body. Translation leaves relative convex-hull comparisons unchanged.

There is one redundant height direction. Let 1 be the all-ones vector. Since t+h1 is a translation by hv of the body at t, the exact identities are

a·1=0,
L1=V0 v,
B1=a/2.

For example, comparing M(t+h1) with M(t)+hv V(t) proves the latter two. Hence on the three-equation slice,

q(t+h1)=q(t)+hV0,
R_v(t+h1)=R_v(t).

One may fix any convenient linear translation gauge, such as sum t_i=0, without removing a physical shape direction.

An equivalent local formulation uses the four-by-N full linearized mass matrix G_v=[a;L]. For d in ker G_v,

p_i -> p_i+[d_i-(d^T B d)/V0]v

is the exact mass-preserving chart. At d=0 its derivative is simply the labelled parallel displacement d_i v. The quadratic translation corrects the remaining finite moment term.

## 3. Entire paths and the actual degree of the equilibrium guards

For a fixed admissible t, use s t,0<=s<=1. Set q1=(ell·t)/V0 and q2=(t^T B t)/V0. The vertices are

p_i(s)=p_i+[s t_i-s q1-s²q2]v.

All V,M,g values are identically those of the parent. Hull gaps remain affine because the quadratic term is a common translation and all relative motions are parallel. Positive strict endpoint hull gaps therefore prove the same strict triangular lattice on the full segment.

Let x_i(s)=p_i(s)-g0. A physical directed-chord numerator x_i·(x_j-x_i) has degree at most three. For an oriented triangular face, the foot-position edge numerator n_f(s)·[x_a(s) cross x_b(s)] also has degree at most three. These guards are generally NOT affine or concave. Exact mass alone therefore supplies no safe equilibrium homotopy.

A positive outgoing physical chord excludes a vertex from even weak U; a negative oriented facet-foot edge guard excludes its facet from even weak S. Strict root predicates are checked separately. A finite dyadic subdivision with positive Bernstein coefficients can certify these cubic inequalities. Different witnesses may cover different subintervals; demanding one globally fixed witness is unnecessarily restrictive.

If strict S/U roots and exclusions persist, weak saddle events are excluded too: an equilibrium at an edge endpoint would be a weak U, and one on the boundary of its two-face normal cone would be a weak S on an incident facet. With no weak equilibria, the usual polyhedral equilibrium index identity S+U-H=2 determines H. This does not prohibit primitive incidence zeros away from actual equilibria, and the J131 full-path certificates make no such stronger assertion.

Executed on DETACHED47, both J131_PARALLEL_100 and J131_PARALLEL_010 have full-path own211/additionalweak000 certificates:3960 exact affine hull comparisons and146 cubic root/exclusion families, with complete positive-witness unions, maximum Bernstein subdivision depth2. Their endpoint primitive diagnostics are000. The third endpoint J131_PARALLEL_001 is also own211/weak000/primitive000, but its exact s=1/2 point is222, U=[4,6],one P about4.3280723978e-8. All have identical mass and lattice. Thus the negative path result is substantive rather than a verifier's inability to find a single witness.

## 4. Exact local completeness of four charts at DETACHED47

This statement concerns labelled vertex coordinates within the same strictly triangular lattice and the same V,M. It is not a quotient by rotations or a claim about all convex-body deformations.

The full mass derivative has four rows. At the exact47-vertex parent, each coordinate-direction matrix G_x,G_y,G_z has rank4. Each corresponding exact parallel chart has43 physical tangent directions. The three coordinate-axis tangent spaces lie in different coordinate blocks and are independent, so their sum has dimension129. The full141-dimensional coordinate space has a regular mass fibre of dimension141-4=137. Three coordinate charts therefore miss eight tangent directions.

The exact47-by12 matrix [G_x^T G_y^T G_z^T] has rank12. For the diagonal direction v=(1,1,1), its mass derivative is G_d=G_x+G_y+G_z and has rank4. Choose a rational43-column basis K of ker G_d. Exact elimination verifies that [G_x;G_y]K has rank8. Since G_zK=-G_xK-G_yK, these eight residual directions supply precisely the missing quotient modulo the coordinate-axis kernels.

The complete atlas131.py records nonzero rational minors, not floating singular-value cutoffs. Its selected eight diagonal free-height coordinates are4,5,6,7,8,9,10,11 after pivot coordinates0,1,2,3. The global combined tangent rank is129+8=137. The observed output is J131_ATLAS_RANK.json2724B/SHA2a7a3903ab58d7ad90333f9fea8ec43bb39d096afd6d2a33deb5fdd019b5a8f4, terminal J131_FOUR_CHART_LOCAL_RANK_137_PASS.

Compose the four exact parallel charts, retaining all43 parameters on each axis and the selected eight on the diagonal. At each successive body rebuild the coefficient matrices using a locally unchanged nonsingular pivot choice. This gives a137-parameter smooth map into the regular V,M fibre; at the parent its derivative is an isomorphism. The inverse function theorem therefore makes its image a neighbourhood in that fibre. Strict convexity persists on a sufficiently small neighbourhood.

This eliminates the independent-star parametrization restriction LOCALLY at this parent. It does not prove that a finite desired support crossing is reachable without leaving the equilibrium class, nor that a particular sign cell has a mass-compatible cancellation. The exact Z midpoint demonstrates why that distinction matters. No rank137 statement is automatically transferred to a different polyhedron; it must be proved or computed there.

## 5. Equilibrium-preserving simplicialization of a simple polyhedron

### Conditional statement
Let K be a rational simple convex3-polyhedron, at its own uniform-volume centroid, with prescribed strict S/U/H and no additional weak equilibria. Suppose the perpendicular centroid foot of every stable facet lies strictly inside SOME triangle whose three vertices are existing vertices of that facet. Then arbitrarily close rational perturbations of the SAME labelled vertices exist whose hull is simplicial, retains every vertex, and has the same own strict S/U/H and no additional weak equilibria.

The triangle hypothesis is automatic for a triangular stable facet and for a strictly convex polygonal stable facet with at least five vertices. It is NOT asserted automatically for every quadrilateral: the intersection of the two diagonals need not lie strictly in any three-vertex triangle. No perturbation coordinates, epsilon or exact audit for the KF applications below have yet been computed.

### A polygon lemma
Take an interior point x of a strictly convex polygon with at least five true vertices. A vertex triangle contains x in the closed sense. If x is in its interior, done. Otherwise x lies on an internal diagonal a b; choose vertices c and d on opposite sides of that diagonal, possible because x is interior to the polygon. These four true polygon vertices form a convex quadrilateral with x on diagonal a b. If x lies on neither side-interior triangle from the other diagonal c d, it must also be on c d. Translate x to0; then b is a negative multiple of a and d a negative multiple of c. A fifth polygon vertex e lies on neither diagonal line: a line through an interior point meets a strictly convex polygon at just two boundary points. Whichever open cone between consecutive directions ±a,±c contains e, e together with the two oppositely directed vertices expresses0 as a strictly positive combination. Thus a strict containing triangle exists.

### Simultaneous rational face lifts
For every stable facet choose one such containing triangle, and extend it to a noncrossing triangulation of that facet polygon. Choose any triangulation on every other facet. Every such polygon triangulation has a rational strictly concave piecewise-linear height function: for its internal diagonals D, choose rational affine line functions ell_D vanishing on D and positive rational weights w_D, and take

f_F(x)=-sum_D w_D |ell_D(x)|.

Within the facet polygon, each diagonal line intersects it in exactly that diagonal. Noncrossing diagonals partition the polygon into the desired triangles. The function is affine on each triangle and has a strict concave crease across every internal diagonal. Consequently those triangles are the upper lifted facets. For an original triangular facet the sum can be zero.

Write each original facet as n_F·x=h_F with rational outward n_F. At each original vertex p_i, prescribe

n_F·d_i=f_F(p_i)

for its three incident facets. Simplicity gives exactly three linearly independent incident normals, so these equations have a unique rational vector d_i. Thus the separately chosen scalar lifts on all faces are simultaneously realizable by one rational displacement of every physical vertex. This is the key reason the statement assumes simplicity.

Set p_i(epsilon)=p_i+epsilon d_i. The first-order determinants among vertices of one old face realize its prescribed upper triangulation: tangential motions contribute no first-order coplanarity determinant, while the specified normal heights give the strict crease signs. Every supporting comparison involving a vertex not in that old face was already strict and stays strict for sufficiently small epsilon. All original vertices remain exposed, because a strict exposing functional from the interior of each old vertex's normal cone has a positive finite gap to the other vertices. Hence for all sufficiently small positive rational epsilon, the hull has the same vertices and precisely the chosen triangular refinement of every old face.

### The OWN equilibrium census, not a frozen reference census
The volume and first moment, hence the actual centroid, vary continuously in epsilon and remain rational for rational epsilon. At each stable old face, its chosen triangle contains the limiting foot strictly, so that triangle has one stable equilibrium for small epsilon. Every other triangle of that face has its limiting foot strictly outside and hence at least one strictly bad foot guard. For an old nonstable face, absence of weak equilibria says its limiting perpendicular foot is outside the whole closed facet, so it is strictly outside each of its triangles. Thus no extra stable or weak stable equilibrium appears.

At an old strict unstable vertex, every chord to another vertex has strictly negative numerator. At each old nonunstable vertex, absence of weak U supplies a strictly positive outgoing chord. These finite global inequalities persist as both the vertices and the OWN centroid move. Thus the same strict U set and no weak U persist. A weak edge equilibrium would force weak U at an endpoint or weak S on a cone boundary, already excluded. Therefore all additional weak equilibria are absent, and S+U-H=2 gives the same strict H count.

This establishes the conditional theorem. It is constructive in the algorithmic sense: choose the rational lifts, solve the3x3 systems, then test epsilon=2^-k until the finite exact hull and own-centred predicates all hold. The proof guarantees a finite k. It is NOT a statement that a particular untested floating perturbation will work, that all epsilon along an arbitrary path work, or that V/M remain fixed.

## 6. Budgeted bridge from KF27J ownS1 to free-vertex coordinates

The fully read KF27J result supplies two simple exact own121/weak000 bodies:
- FF2_MIN42_G5: V80/E120/F42, sole stable hexagon.
- AF2_MIN43_G5: V82/E123/F43, sole stable nine-gon.

Their stable facets satisfy the polygon lemma. The theorem therefore produces arbitrarily close rational simplicial own121/weak000 variants with, respectively,

V80/E234/F156 and V82/E240/F160.

These are ANALYTICALLY PROVED NEARBY-EXISTENCE ENTRANCES, not executed exact input files. No chosen lifts/epsilon/point output/census hash has been produced. Their E counts follow from simplicial3-polyhedron Euler identities E=3V-6,F=2V-4; the source bodies' exact simplicity and stable-face sizes are trusted author premises. Both variants fit E<=249 and leave5 or3 generic additional point slots before V85. They no longer retain the earlier43/42 ordinary-H reserve: the triangular refinement consumes that facet budget. Neither guarantees detachment of the stable facet from U, lower P, simpler arithmetic or the local rank137 property proved only at DETACHED47.

This bridge is useful because the original low-F simple bodies permit inexpensive normal edits but constrain vertex coordinates by coplanarity. A carefully chosen triangular release permits general vertex motion without initially losing the already completed Q=[] landscape. It can then be combined with actual-mass vertex charts, provided their local ranks and finite guard feasibility are established on the chosen body. No global completion claim follows.

The new QW49G clean H45 body has86 vertices. An unrestricted simplicial refinement would have E252, ABOVE the target budget. It therefore needs at least one genuine vertex retirement, preserved nonsimplicity or only a partial release; do not apply the V80/V82 budget conclusion to it. KL's116-vertex body and canonicalC622 similarly do not admit this generic within-budget release at fixed vertex count.

## Scientific next step
Use complete actual mass charts or a consciously chosen carrier/refinement change to leave the retained-neighbour hypotheses of J130, not another independent-star direction inside the same gate. The rank theorem provides locally complete coordinates, the X/Y paths provide real finite safe motion, and the Z path supplies a sharp limitation. On the opposite already-S1 frontier, the simplicialization theorem provides a budgeted way to change representation before attacking the entire P component. None substitutes for full own equilibrium and true-edge certification of a new110 body.
