# COORD_S8_CAP_SLIDE — exact exclusions and a physical moment controller

This is NOT a new Gömböc. The accepted C624 S8 and distinct INHERITED_G9 are unchanged. The three base bodies are exact S8 with original support 99, 117 or 84 deleted. S8 is reconstructed by BASE_GENERATOR.json and RECONSTRUCT.py; filtering is performed after reconstruction, not by an ignored active_ids field. The exact source is the recovered S8 geometry, not the older COORD_TRIPLE_C624_OWN121_G14.

## Source and evidence identity
The S8 source also appears in fully read immutable result asg_cvIXkmYXCeuUD0baP2XcB1rn, SHA256 c00d707b68ac1ed80be88960dad668969b21b25ef57afbd02f4bef9d22299ffb. DEL84 is explicitly generated here from the same S8; it is not an alleged output from that worker's four-case audit. The parent raw point ordering is exact Cartesian lexicographic order reconstructed by both independent auditors. Support labels in parent reports are filtered row indices.

Run `python -B -S REPLAY.py --out /an/absent/output/directory` using Python 3.13.5 or a compatible standard-library Python with assertions enabled. The exact reconstruction needs no NumPy or SciPy. All source-file hashes are checked before and after. Expected terminal marker: `COORD_S8_NINE_SLIDES_TWO_CAPS_SOURCE_ONLY_COLD_PASS`. Exact output filenames, byte counts and SHA256 are in EXPECTED.json; the source manifest is MANIFEST.json. No stored centroid, hull, report or certificate output is accepted as geometry input.

## Nine open-interval families, not just a grid search
At a simple vertex u with neighbours a,b,w, move only u to u(s)=(1-s)u+s w, 0<s<1. The incident facet not containing w has at least four corners in each case. Delete u from that facet cycle and add the triangle [a,b,u(s)] oriented toward the discarded u. The other facet planes remain unchanged. A new edge ab is created, so true counts on the open interval are V'=V, E'=E+1, F'=F+1.

DEL99: u145, neighbours112,129,146, permanent pole95; base175/309/136; slides175/310/137,C620. DEL117: u81, neighbours77,78,84, pole93; same counts. DEL84: u175, neighbours169,173,174, pole95; base176/310/136; slides176/311/137,C622. TILES.json gives every dyadic cell and its second weak-unstable witness, with no abbreviated rows. The fixed pole is checked throughout [0,1] separately. The certificate uses at most9 cells per family and maximum dyadic depth8; there are no uncovered cells.

Let T=abs(det(a-u,b-u,w-u))/6. The removed part is exactly the tetrahedron [u,a,b,u(s)]. For the ordinary filled-volume first moment:
V(s)=V0-sT,
M(s)=M0-sT*(2u+a+b+s(w-u))/4,
c(s)=M(s)/V(s).
V(s)>0 is certified, not assumed from an assigned reference centre. A vertex's radial normal-cone primitive for each true neighbour j is
p_ij(s)=[V(s)X_i(s)-M(s)] dot [X_j(s)-X_i(s)].
It is a rational polynomial of degree at most3. After multiplying by a positive common denominator, integer Bernstein signs on a dyadic interval certify p_ij<=0 there. Two distinct true vertices with all these signs nonpositive exclude strict own110 with weak000. They are weak normal-cone equilibrium candidates; strict instability throughout each parameter cell is not asserted.

Producer edge_slide_exclusion.py builds those exact polynomials and a complete dyadic cover. Independent edge_slide_verify.py does NOT import the producer. It checks the entire interval's supporting planes, strict nonincident slacks, convex old facet cycles, incident-normal rank3 at every vertex, oriented edge pairing, connectedness and true V/E/F; derives all moments by full boundary integration at four rational parameters; obtains primitive polynomials by Lagrange interpolation; and checks the frozen cover by exact de Casteljau subdivision. This is not a tolerance-based numerical verification or an edge count from triangulations. Bernstein weak inequalities are sufficient for the stated exclusion, including parameter values with weak candidates.

## The endpoint s=1 is a separate finite body
All three slides of a given u meet at conv(P minus {u}), regardless of the chosen w. The open-interval proof does not silently include it. edge_endpoint.py constructs the exact cut plane through all three neighbours and independently runs both complete hull/moment/all-feature auditors:
DEL99 endpoint174/309/137,C618,strict(25,36,59),weak000.
DEL117 endpoint174/309/137,C618,strict(37,48,83),weak000.
DEL84 endpoint175/310/137,C620,strict(2,3,3),weak000.
All are nonwinners. Their raw coordinate rows are the corresponding parent's rows with u removed, so no numerical rationalisation is involved. Their exact supports and own centroids are generated, not borrowed. Complexity cannot be inferred from E+1 of the open interval at s=1.

## Exact two-cap local physical centroid controller
For a separating four-cycle with affinely independent boundary points q0..q3, B has their homogeneous columns. Applying B diag(lambda0,lambda1,lambda2,lambda3) B^-1 to one component, leaving the other component untouched, fixes the four boundary points. Provided no face contains interior vertices from both components, all intended facet planarity is preserved. At identity, exact strict parent support margins yield an open convexity/incidence neighbourhood. All homogeneous denominators must remain positive. No finite radius is claimed here.

Equivalently, beta=B^-1*(p,1) and lambda_j=1+eta_j give p(eta)=(p+sum eta_j beta_j q_j)/(1+sum eta_j beta_j). This rational form is the exact physical deformation; it is not a global projectivity and does not add edges. A separating triangular boundary similarly permits I+k*l^T, fixing its boundary plane; the deterministic graph inventory is SEPARATORS.py.

DEL99 and DEL84 small cap[0,2], boundary[1,3,10,95]; large cap[83,85,87,91,93,96,98,102,105,110,113], boundary[79,90,95,116]. DEL117 small cap[0,2], boundary[1,3,10,93]; large cap[82,83,85,89,91,94,96,100,103,108,111], boundary[79,88,93,114]. The two caps are disjoint and neither moves any boundary point of the other.

Select lambda2 of the small cap, lambda0 and lambda1 of the large cap, fixing other lambdas at1. At identity velocity v(p)=beta_j(p)*(q_j-p). Differentiate every affected boundary tetrahedron, then the filled centroid c=M/V, giving dc=(dM-c*dV)/V. cap_moment_jacobian.py computes all entries and a NONZERO exact rational3x3 determinant for each of the three bases. Approximate determinants are3.1683603032226916e-10 (DEL99),3.1683591201959816e-10 (DEL117),3.168358681741384e-10 (DEL84). The determinants' rational numerator/denominator max bit lengths are91994,92010,92223; their bytes are reproducible output, not small coordinate inputs. The first controller has approximate singular values .00941835,.000375196,.0000896606. These floats illustrate conditioning, not the proof of rank.

The inverse function theorem therefore gives genuine LOCAL three-dimensional physical centroid control at unchanged incidence. A sufficiently small disjoint surgery can locally be compensated in all three true first moments by these cap parameters. This is not a global mechanical cancellation theorem, a finite-radius guarantee, or permission to prescribe an arbitrary centre without changing actual material. It does not overturn the nine exclusions, which concern the explicitly specified uncompensated families only.

## Finite failed numerical searches retained
cap_family_search.py explores three disjoint/nested-compatible tetrahedral caps (9 shape controls), global projectivity(3), and a determinant-one upper-triangular affine metric(5):17 real parameters. Five DEL117 starts, max150 function evaluations per least-squares call, seed140926, produced no strict110. Its lower residual endpoint has many extra equilibria (67,38,103), so residual reduction is NOT a mechanical improvement. cap_guard.py with180 iterations and factor.1 for each of DEL99/117 retained baseline own121; both SLSQP runs stopped with positive directional derivative, not an infeasibility proof. Frozen complete endpoints, finite histories, configurations and five-start records are included. NumPy2.3.5 and SciPy1.17.0 were used. Numerical extreme-s slide screens in edge_slide.py are search diagnostics only; the exact interval result does not depend on their tolerance counts. The exact replay does not rerun stochastic optimizers or require floating output byte identity.

Continuations worth pursuing: actual cap moment compensation coupled to a genuinely multi-vertex/whole-basin geometry change; exact finite centroid-preserving controlled paths beyond the uncompensated slides; exploitation of selected cap controls in the wider realization space. Do not recycle the same baseline nine one-vertex slides expecting an untested interior winner. No global projective-orbit exclusion, no minimum C, and no new C<624 own110 are established.
