# material-5a2db83302ee

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# D2_SYMMETRY_QUOTIENT_AND_SECTIONS_20260923
Complete internal analytic source. No new class110 construction is claimed. These statements concern finite Euclidean convex polyhedra at their actual uniform filled-volume centroid. They do not exclude general two-vertical-reflection geometry. No numerical computation or missing external source is needed for the proofs below; originality relative to the literature is not asserted.

## 1. Exact orbit-exterior escape reduction
Let a finite orthogonal group G preserve a full-dimensional convex polyhedron P. Its actual uniform centroid c is fixed by G: apply each g to the volume integral and use change of variables. Translate c to0. Two distinct points x,y in the same G orbit have equal squared norm, hence
  x dot (y-x) = (|y|^2-|x|^2-|y-x|^2)/2 = -|y-x|^2/2 < 0.
In particular a true edge inside a symmetry orbit can NEVER be a positive outgoing radial escape, irrespective of how short it is. For every vertex v the condition that some true incident edge v--w satisfies v dot(w-v)>0 is therefore unchanged if all same-orbit edges are removed from the candidate list.

This is an equivalence of strict escape feasibility, not an approximation. Edge incidence is still the actual maximal-polyhedron incidence. The orbit-reduced graph must not add chords. For a singleton proposed root r, if every other vertex has a positive outgoing orbit-exterior true edge, then following these edges strictly increases squared radius, cannot cycle, and ends at r. If r itself is a strict unstable vertex, it is the only unstable vertex. By equivariance it is sufficient to check one representative per orbit, but multiplicities must be restored in all equilibrium counts. A proposed root orbit of size greater than1 cannot represent a unique equilibrium.

Apply the same identity to the polar Q=(P-c)^*. This is the polar about the SAME physical volume centroid, never the polar recentered at its own volume centroid. Q inherits G. Strict stability of a P facet corresponds to strict instability of its Q vertex: the perpendicular foot q_i/|q_i|^2 lies in the relative interior of the primal facet exactly when q_j dot q_i < |q_i|^2 for all other Q vertices; it is sufficient to test the true Q neighbours because the linear functional reaches a strict maximum there exactly when it reaches its strict global maximum at q_i. Thus orbit-exterior physical and polar escape constraints preserve the desired root-feasibility problem. A final accepted body still receives the full exact strict/weak facet, vertex and mixed-edge audit; this reduction is not a replacement for that certificate.

### Why this changes a numerical objective
Consider the popular vertex penalty max(0,margin-max_w v dot(w-v)/(|v| |w-v|))^2 over true neighbours. For same-orbit w, the normalized score is exactly -|w-v|/(2|v|). A short reflected edge can therefore be the least negative choice even when every orbit-exterior escape is strongly negative. Minimizing this penalty can shrink the reflected edge toward coincidence rather than route the entire critical orbit to another radius level. Deleting same-orbit candidates removes this spurious optimization option without deleting any feasible strict escape. This explains a possible failure mechanism; it does not prove that the quotient loss converges, improves equilibrium counts, or solves the finite construction problem.

For the two vertical reflections (x,y,z)->(-x,y,z),(x,y,z)->(x,-y,z), a numerical orbit signature is (abs(x),abs(y),z) after actual centering. In an exact implementation use exact equalities, or derive orbit labels from the exact group action and incidence. Approximate orbit merging can misclassify nearby distinct orbits and is NOT an exact certificate. In an H input with a four-element sign orbit per representative and a singleton bottom plane, the input orbit index is directly known, after discarding inactive planes.

## 2. Rectangular-section obstruction at the actual mass centre
### Statement
Let l<R, and let a,b:[l,R]->[0,infinity) be continuous concave piecewise-affine functions, positive on [l,R), with a(R)=b(R)=0 and a(l),b(l)>0. Define
  K={(x,y,z): l<=z<=R, |x|<=a(z), |y|<=b(z)}.
K is a full-dimensional convex polyhedron with a rectangular bottom facet and a unique axial top vertex. At its actual homogeneous centroid it either has an additional weak equilibrium or has at least THREE strict stable facets. In particular it cannot be an own strict110 body without additional weak equilibria, for any number of segments or edges.

### Proof
Reflection symmetry makes the centroid axial. Translate its height to0 and write the height interval [-L,T], with L,T>0. The bottom facet contains (0,0,-L) in its relative interior, so it is a strict stable facet. Suppose that there is neither an additional weak equilibrium nor any strict stable lateral facet.

On the meridian x=a(z), y=0 define A(z)=a(z)^2+z^2. On an interval where a(z)=alpha+s z is affine,
  A'(z)/2 = a(z)s+z,
whose derivative is 1+s^2>0. At a genuine slope break, concavity gives s_right<=s_left and a(z)>0, so A'/2 has a downward jump, never an upward one.

An interior zero a(z)s+z=0 is the perpendicular foot from the centroid onto the supporting plane x-s z=alpha. Since y=0 and b(z)>0, and the height is interior to the affine segment, this foot lies in the relative interior of the actual maximal lateral facet. It is therefore a strict stable facet. A zero at an endpoint of such a segment (other than the top) places the supporting-plane foot on its facet boundary, yielding an additional weak equilibrium. This includes a zero at the bottom edge. The same assertion holds when a segment endpoint arises only from a subdivision: collinear segments are merged first. A break of b alone does not split the maximal x-side facet or affect this argument.

Near the top, a(T)=0 and A'(T-)/2=T>0. Since A'/2 increases strictly within each affine segment, jumps only downward at the finitely many breaks, and has no zeros allowed by the preceding paragraph, it must be positive everywhere on [-L,T]. Otherwise a negative value could reach the final positive interval only by a zero on some affine segment or at its boundary; a downward jump cannot do that. Thus A is strictly increasing. Repeating the argument for B(z)=b(z)^2+z^2 shows that B is strictly increasing too.

Comparing endpoints yields T^2 > L^2+a(-L)^2 > L^2, hence T>L. For 0<h<L, comparison at h and -h cancels h^2 and gives a(h)>a(-h) and b(h)>b(-h). The section area W(z)=4a(z)b(z) therefore satisfies W(h)>W(-h). It follows that the first volume moment is
  integral[-L,T] z W(z) dz
  = integral[0,L] z(W(z)-W(-z)) dz + integral[L,T] z W(z) dz > 0,
contradicting that the actual centroid has height0. There is consequently a strict stable lateral facet or an additional weak equilibrium. Reflection in x=0 or y=0 pairs any such lateral stable facet with a distinct stable facet. Together with the bottom facet this gives S>=3 when weak equilibria are absent. QED.

The obstruction uses actual volume mass in its decisive last step. It is not valid for an arbitrarily chosen reference point. It assumes centred rectangular parallel sections and an axial point top. It does not cover oblique/drifting section centres, mixed horizontal facet-normal directions producing nonrectangular sections, a general D2 body, or all two-apex bodies. A finite chart that uses only vertical-plane normals of the forms (nx,0,nz) and (0,ny,nz), with these endpoint conditions, lies in the excluded class. Adding more such levels cannot repair it.

## 3. Fixed homothetic centrally symmetric sections
Let B be a fixed full-dimensional centrally symmetric convex polygon in the horizontal plane, centred at0. Let a:[l,R]->[0,infinity) be continuous concave piecewise affine, positive on [l,R), with a(R)=0 and a(l)>0. The body
  K={(u,z): l<=z<=R, u in a(z) B}
has the same conclusion: absent additional weak equilibria, S>=3 at its actual uniform centroid.

Proof. Write B={u:n_j dot u<=h_j}, with distinct unit outward normals and positive h_j. Choose h=min_j h_j and an attaining normal n. The point h n is in the relative interior of that facet: for every other distinct normal n_k,
  n_k dot(h n) < h <= h_k.
It remains the relative-interior foot on that section side at every positive scale a(z). The paired normal -n supplies the opposite side. The actual centroid is axial by central symmetry. After its height is set to0, the function h^2 a(z)^2+z^2 has precisely the derivative and downward-jump properties used in Section2. No lateral stable or additional weak foot would force it to increase strictly to the axial top. Thus T>L, a(h0)>a(-h0) for every 0<h0<L, and the area W(z)=area(B)*a(z)^2 has strictly positive first moment, a contradiction. Any strict lateral stable facet is paired by u->-u. QED.

This excludes fixed centred homothetic polygonal stacks, including varying-width regular-polygon stacks. It does not exclude a changing nonhomothetic angular shape, changing section centres, or the general reflection-symmetric construction problem. Sections2 and3 are complementary: rectangles may vary their two widths independently, while Section3 allows an arbitrary fixed centrally symmetric polygon.

## 4. Consequences for the constructive frontier
The numerical D2 chart with genuinely mixed horizontal supporting normals is NOT excluded. It should retain changing angular shape and route the full physical and polar critical ORBITS through true exterior edges while recomputing volume mass. Orbit contraction, adding more rectangular/homothetic levels, and replacing the actual centroid by a convenient reference are not solutions. Independently localized finite top/bottom carriers remain a separate open constructive direction. This source establishes a reusable exact reduction and two scoped family obstructions, not a C<500 class110 endpoint.
