# material-dadeea482757

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1

## Claim and scope
This coordinator construction connects the fixed-volume adjacent-triangle trace deformation problem to actual own-centroid, guard-preserving geometric coarsening. It is NOT an own110 example and does NOT change 34<=Cmin<=622. It proves a complete three-dimensional moment-neutral transverse chamber for one exact previously accepted control, and a complete two-dimensional own-centroid section whose entire closed family has strict(S,U,H)=(4,4,6), no physical weak equilibria, under the single reciprocal pair M=N=I. Its true f-vectors range from10/21/13 to10/19/11 in that section. No all-metric impossibility is claimed.

The literal original body is from accepted minimum-0123,37520bytes,SHA256 cfcf3fdd7e401178bd9b9626830ba970f0460a54e11105158977d888331d4f9d, fully read by coordinator before use. The conceptual single-vertex deformation parent minimum-0128,41987bytes,SHA256 9b8fa9986220926caf778450ec66563e7e5fe300aa1c9fb53433306b415efa34, was also fully read. Its newer deletion countercontrol is a DIFFERENT body; it has not been substituted for the literal jb58 body below. The exact computational capsule here is self-contained and requires no parent file extraction.

## General transverse-shadow lemma
Let P=conv(v_i) contain a fixed full-dimensional tetrahedron, and let ell and n be fixed affine functionals. Select u!=0 annihilating both linear parts. Move any chosen noncanonical vertices by v_i(s)=v_i+s_i u. Every oriented four-point determinant and every boundary three-point determinant is affine jointly in s: every term with at least two varying columns contains parallel copies of u and is zero. Thus actual facet coplanarity equations, actual support inequalities and boundary-fan orientation inequalities are linear. For a facet parallel to u the containing plane is fixed and planar cyclic convexity is expressed by affine signed-area inequalities. A facet transverse to u has a fixed nondegenerate projection; its cyclic order and convexity follow from that projection together with coplanarity. This describes an actual closed face-coarsening cell, not a restriction by signs of arbitrary interior tetrahedra.

On such a cell ell(v_i(s)) and n(v_i(s)) are constant. The oriented boundary formulas give affine functions V(s)=volume(P_s), B(s)=integral ell, N(s)=integral n. Consequently, on any fixed-V affine section, T=N/(6VB) is linear-fractional with positive denominator. Along each nonzero feasible direction it is monotone or constant, so one can choose a nondecreasing endpoint. The fixed-volume cell is bounded: if a moving vertex escaped to infinity while the fixed tetrahedron remained, volume(conv(tetrahedron,v)) would diverge. An endpoint is an actual geometric wall: facet merger, loss of a vertex, or loss of a marked maximal triangle into a larger coordinate-plane patch. The last event is a real boundary, not a license to apply a triangle-only theorem beyond it. Nor does this lemma prove that every residual vertex has a feasible collective direction: coupled coplanarity constraints can remain rigid.

The full first moment J(s) is in general quadratic; preserving V,B,N does not in general preserve the entire centroid. The particular symmetric control below has an additional exact cancellation on its full moment-neutral space.

## Exact original body and integrals
Labels0,1,2,3 are A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0). Put b=1/8,c=d=67/1000,eta=1/20000,delta=1/1000. For (s,w)=(13/16,0),(1,0),(107/100,delta), define z=(1-(1-c)s-w)/(1-b) and append the left/right pair (eta,s-eta,z),(s-eta,eta,z), receiving labels4,5;6,7;8,9. Define ell=1-933(x+y)/1000-7z/8 and n=149(x+y)/125. The body has true outward maximal facets, in the code's sorted order,
(0,1,2),(0,2,3),(0,3,1),(1,3,5),(1,4,2),(1,5,4),(2,4,6),(2,6,8),(2,8,9,3),(3,7,5),(3,9,7),(4,5,7,6),(6,7,9,8).
Thus Vcount/E/F=10/21/13, ABC and ABD are true maximal triangles, and the ell=0 root is(4,5,7,6), of constant oriented xy-area54369/320000. The root area is not being normalized after each deformation.

V=4263470123/21000000000;
B=4553794654013/84000000000000;
N=184904985954453/1400000000000000;
T=38830047050435130000000/19414967453661547553599, strictly2<T<51/25.
J=(1240973060097/22400000000000,1240973060097/22400000000000,10384698911451/200000000000000).
g=J/V=(3722919180291/13643104393600,3722919180291/13643104393600,218078677140471/852694024600000).
These are actual uniform-volume integrals, not transported or selected centers. Exact outward positive fans from(1/4,1/4,1/4), with two distinct boundary triangulations, agree throughout all listed actual boundary strata.

## Individual rigidity versus collective motion
Take u=(1,-1,0). Either auxiliary vertex8 or9 separately lies on two fixed incident quadrilateral planes with independent normals, hence is restricted to its u-line when the other vertices are fixed. Their exact volume derivatives are respectively -67/75000,+67/75000, so neither has a nonzero individual fixed-volume displacement. Moving BOTH by the same t u preserves V,B,N exactly, not just to first order. The complete old-face chamber along that line is -1/1340000<=t<=1/1340000. Both endpoints have actual10/20/12, retain ABC,ABD and the root, and have the same T. At the positive endpoint facets(3,7,5),(3,9,7) merge; at the negative endpoint facets(2,4,6),(2,6,8) merge. This defeats individual rigidity as a general obstruction to collective coarsening, not the possibility of collective rigidity. The full centroid changes, which motivates the section below.

## Complete moment-neutral chamber
Allow all six vertices4..9 to move independently along u. Their V,B,N derivative rows are
(-1447/84000,1447/84000,-6901/2100000,6901/2100000,-67/75000,67/75000),
(-84233/112000000,84233/112000000,-464243/8400000000,464243/8400000000,-1541/100000000,1541/100000000),
(-317817/22400000,317817/22400000,-1596870697/420000000000,1596870697/420000000000,-688827/625000000,688827/625000000).
Their exact rank is3. Their kernel consists EXACTLY of paired-center shifts (s4,s5,s6,s7,s8,s9)=(alpha,alpha,beta,beta,gamma,gamma). This is the full VBN-neutral transverse subspace of the literal old-face chart, not an arbitrary subfamily.

Write p=(alpha,beta,gamma). The complete closed actual face-coarsening chamber is the parallelepiped |L1|<=1,|L2|<=1,|L3|<=1 with
L1=20000alpha,
L2=(-10720000alpha+12460000beta)/87,
L3=(-1500800alpha+5460800beta)/3-1340000gamma.
The code derives38 distinct normalized nonconstant affine support/cycle/fan/coordinate inequalities 1+a.p>=0. All six slab rows occur among them. Conversely, every one of the38 rows is nonnegative at all eight slab corners, hence on the whole parallelepiped. This proves the exact equality of the domains. Affine nonnegative constraints have a constant zero pattern on the relative interior of each parameter face; therefore the27 exact face representatives L_i in{-1,0,1} classify the entire27 strata, not just27 sampled bodies. True facets are recomputed as maximal supporting polygons with collinear nonvertices discarded.

On a parameter face of dimension k, the true f-vector is(10,18+k,10+k). The two marked triangles ABC,ABD are both true maximal faces exactly when |L1|<1. Thus the entire chamber has minimumE18, attained at its eight corners, but every such corner loses at least one marked maximal triangle into a larger coordinate patch. Under the genuine two-triangle requirement the minimum isE19. In this precisely scoped chamber there is noE17. This is NOT a prohibition beyond the old-face cell, beyond fixed projections along u, or under other changes of VBN.

## Exact own-centroid section
The signed first moment has degree at most2 in p. Computing all its linear and quadratic coefficients exactly gives
J(p)=J(0)+u(rho.p),
rho=(7998131/672000000,19136473/6000000000,924533/1000000000).
The code kills each pure quadratic and mixed quadratic coefficient by exact coefficient evaluations, not approximate fitting. Thus the actual own centroid is unchanged exactly on rho.p=0. Intersecting with the parallelepiped yields a parallelogram: L2,L3 independently range over[-1,1], and |L1|<1 everywhere, as follows already from its four corners and linearity. Its four vertices are the negatives and positives of
(-19766916267/9582583461410000,698633054787/134156168459740000,1152460328863/134156168459740000)
and
(-18907238567/9582583461410000,708987824387/134156168459740000,64440599616871/8988463286802580000).
Every corner has actual10/19/11 and retains both marked triangles. Its interior, edges and corners have respectivelyE21,E20,E19. All retain V,B,N,J,g and the root area. The source includes full literal coordinates, actual maximal facets, true edges, ownCOM and full mechanics for all nine strata representatives and for the full27-stratum chamber.

## Continuous mechanical certificate on the entire closed own-centroid section
Use one actual Euclidean metric M=N=I throughout. Let L2=-1+2r,L3=-1+2s,r,s in[0,1],rho.p=0. Vertices and centered vectors z_i=v_i-g are affine in(r,s). Old facet outward normals n_f and support heights h_f=n_f.z_i are affine, and all16 degree-(3,3) Bernstein coefficients of each h_f are strictly positive. Hence every old support plane is genuine and q_f=n_f/h_f is its actual centered polar point.

For each of the21 original edges ij with old incident facets f,k use the four physical sign primitives. The primal pair z_i.(z_j-z_i),z_j.(z_i-z_j) are polynomials of degree<=2. A numerator of the first polar primitive is n_f.(h_f n_k-h_k n_f), with strictly positive denominator h_f^2 h_k; the reverse row is analogous. Thus all84 sign tests are exact polynomials of degree<=3. Expand each with its center sign into bidegree-(3,3) Bernstein form on the square. The complete1344 rational coefficients are generated and stored in the deterministic report. Every signed coefficient is nonnegative. For all42 primal rows and all but8 polar rows they are STRICTLY positive. Each of the8 exceptions has exactly one full boundary row or column of four zero coefficients, all others strictly positive, so its only zeros lie on that particular parameter boundary side.

The exceptional rows are exactly the two polar primitives on each old edge(2,4),(2,6),(3,5),(3,7). Each edge has a uniformly strictly positive primal escape primitive. Its polar rows vanish only at the parameter wall where its two facets merge; there the segment is no longer a true edge. Such a formal zero is not a physical weak equilibrium. No other old edge disappears on this section, and no new edge or vertex appears; the27-cell geometric certificate supplies the exact coarsened true incidence at every boundary.

The unstable labels remain0,1,8,9: all incident primal tests there are strictly negative. Each other label has a positive escape on a surviving edge, namely2->8,3->9,4->6,5->7,6->8,7->9. The stable old facets remain0=(0,1,2),1=(0,2,3),2=(0,3,1),5=(1,5,4), with all relevant dual tests strictly negative; none merges in this section. Every other facet has a polar escape chain:4->0,3->2,6->4,7->6,9->3,10->9,8->1,11->5,12->11. On a merger wall the zero arrows only identify coincident polar points; the chain continues to a strictly positive surviving escape. Hence no merged nonroot facet becomes stable. The six saddle edges are(0,1),(0,2),(0,3),(1,4),(1,5),(8,9), with all four primitives strictly negative, and persist on the entire closed section. Every remaining true edge has a strictly positive primitive, so no other strict saddle or physical weak point appears.

Consequently every body of the entire closed section, including its coarsened boundary, has strict(S,U,H)=(4,4,6), no physical weak equilibrium, and no zero primitive on its TRUE edge set. This is a continuous exact guard-preserving geometric coarsening proof, not an inference from endpoint census. The zero rows on removed triangulation-like seams are explicitly excluded from true complexity and mechanical counts.

## Reconstruction, verification and durable identities
Part1 is immutable material [internal-source-reference]. Save its ENTIRE text verbatim as transverse_shadow.py. It contains every input coordinate/formula and every helper; no external source file, hidden solver state, random seed, encoded archive or optional package is required. Tested Python3.13.5, standard library only, exact fractions throughout. No precision or floating tolerance is used.

Input transverse_shadow.py:17269bytes,SHA256 4330357c9b5b7a8a3415109135b464dbb6a9fd4c135096605b70e4fab050b036.
Reconstruction: python -S transverse_shadow.py build
Verification: python -S transverse_shadow.py check
Both were executed by coordinator in the development directory AND in a fresh directory containing ONLY the complete source. Output transverse_shadow_report.json:653362bytes,SHA256 53f1ad2cf51826daa2e4cbe081644978968ebaaa1cc3af27793c1d40fe66e73d.
Expected terminal lines in BOTH commands:
TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1 PASS
FULL_MOMENT_NEUTRAL_CHAMBER 3D 38_ROWS 6_SLABS 27_STRATA MIN_E18
TRUE_TRIANGLE_PAIR_AND_OWN_CENTROID_SECTION 2D 9_STRATA MIN_E19
CONTINUOUS_446_WEAK000 84_POLYNOMIALS 1344_BERNSTEIN_COEFFICIENTS PASS
transverse_shadow_report.json 653362 53f1ad2cf51826daa2e4cbe081644978968ebaaa1cc3af27793c1d40fe66e73d

The source deterministically generates the full report, including every rational coefficient, so the653362 output bytes need not themselves be archived as an input. The proof above supplies the continuous interpretation of the exact calculations. Part1 plus this part2 form the complete recovery capsule. The input hash identifies actual preserved bytes; it is not a mathematical substitute for the proof. Useful next questions concern width/projection changes and genuine coupled motion of a nonsimple patch, not repeating single-vertex freezing or mistaking the class446 controls for class110.
