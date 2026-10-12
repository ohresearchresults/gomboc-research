# material-92fc2f3fff3b

AI research material

---

# Projective own-centroid correction with exact incidence preservation and linear equilibrium witness cells

## Evidence status
Coordinator analytic derivation; no record-body experiment was performed and no new C<622 endpoint is claimed. This direction avoids the nonsimple-incidence rank loss found in the facet-pivot method, by coupling ALL facet normal changes projectively. The general existence/uniqueness of fitting an interior point to a convex body's centroid is not claimed as new mathematics: Ivan Izmestiev, Fitting centroids by a projective transformation, arXiv:1409.6176 (2014), explicitly identifies the point-versus-convex-body case with existence and uniqueness of the Santalo point. The source abstract was read through web search in this turn; no other theorem from that paper is being used unread. The formulas and polyhedral proof below are self-contained. This is a reusable method, not proof that centering preserves a strict110 chamber.

## Exact family
Translate the desired interior reference point q to0. Write the full-dimensional bounded polyhedron as n_i dot x<=h_i with h_i>0, true vertices v, and its exact face lattice. For a parameter b in

    D={b:1+b dot v>0 for every vertex v},

put s_v=1+b dot v and T_b(x)=x/(1+b dot x). This is an invertible projective map on P, inverse T_{-b} on its image. Since the denominator is positive on all of P, convexity, every true face, and every incidence are preserved. In particular Vcount,E,F,C do not change, even at nonsimple vertices. Transformed vertices and support planes are exactly

    v'=v/s_v,
    (n_i+h_i b) dot x'<=h_i.

Rational input and rational b give rational output. This is a genuine geometry change; the output solid is assigned uniform density, not the pushforward of the old uniform mass.

## Uniform volume and centroid
The Jacobian determinant is (1+b dot x)^(-4) in dimension3. Therefore

    W(b)=Vol(T_b(P))=integral_P (1+b dot x)^(-4) dx,
    M(b)=integral_P x(1+b dot x)^(-5) dx,
    g(b)=M(b)/W(b),
    grad W=-4M,
    Hess W=20 integral_P xx^T(1+b dot x)^(-6) dx.

Hess W is positive definite on D because P is full dimensional. D is a bounded open convex polyhedron when0 is strictly inside P. W tends to infinity at its boundary: at a vertex v with 1+b dot v tending to0, choose a fixed nondegenerate tetrahedral cone contained in P with apex v; integrating a lower bound proportional to (epsilon+c*t)^(-4) against t^2 dt diverges as epsilon tends to0. Constants may be chosen uniformly along a sequence approaching a boundary point, since b remains bounded. Thus W has exactly one minimizer b_* in D, and g(b_*)=0. This is a polyhedral existence/uniqueness proof of the centroid fit for this normalized projective family.

Let the original body have centroid g, second volume moment Q=average(xx^T), and covariance Sigma=Q-g*g^T. At b=0,

    D_b g = -5 Q +4 g*g^T = -5 Sigma -g*g^T,

which is negative definite. At a centered body the derivative is -5Sigma. This gives full three-dimensional physical centroid control without relaxing any nonsimple incidence. It does NOT make arbitrary equilibrium constraints compatible with b_*.

W(b), M(b) and their derivatives may alternatively be evaluated by exact tetrahedral integration over the transformed rational boundary. No numerical quadrature or nonuniform density replacement is required. At a generally irrational b_*, a rational approximation followed by exact own-centroid recentering is permissible only after certifying strict equilibrium margins; exact equality g=0 need not be imposed on the rational pre-recentered coordinates.

## Vertex equilibrium tests become affine in b
For a true adjacent pair v,w, the sign of v' dot(v'-w') is the sign of

    L_vw(b)=|v|^2-v dot w
             + b dot (|v|^2*w-(v dot w)*v),

since the denominator is s_v^2*s_w>0. Thus a specified vertex is strictly unstable exactly when every adjacent L_vw is positive. A strictly negative selected L_vw excludes instability at a different vertex. Fixing one such negative witness for each unwanted vertex defines a convex open polyhedral witness cell in b-space. A zero chosen witness is not by itself proof of a weak equilibrium if another witness still excludes that feature; full weak tests remain necessary at candidate boundaries.

## Face equilibrium tests also become affine in b
Let m_i=n_i+h_i b. The perpendicular foot of0 to face i's plane is p_i=h_i*m_i/|m_i|^2. For any other facet j, its interior slack has the sign of

    A_ij(b)=h_j*|m_i|^2-h_i*(m_j dot m_i)
           = h_j*|n_i|^2-h_i*(n_i dot n_j)
             + h_i*b dot(h_j*n_i-h_i*n_j).

The b^2 terms cancel exactly. Face i is strictly stable if A_ij>0 for every j!=i; one strictly negative A_ij excludes stability. All other facets may be used; using the true adjacent defining halfplanes is an equivalent shorter formulation for a nonredundant polygonal face.

For chosen unique stable face and unstable vertex, fixing negative witnesses on all other faces/vertices gives an open polyhedral cell cut out by the above affine inequalities and D. This cell certifies the selected strict extrema. Complete edge and weak-equilibrium verification is still required for acceptance; do not silently substitute extrema tests or an Euler count for the requested complete certificate.

## Consequence for search
For a fixed P and fixed reference point q, the centered projective parameter b_* is unique, independent of the chosen equilibrium witnesses. A rigorous convex minimization/certification of W over a witness cell can decide whether b_* lies inside that cell. If the minimizer is outside one witness cell, only that cell is excluded; other witness choices can still describe the same strict110 component. If the unique b_* itself fails the requested equilibrium class, that fixed-reference normalized projective family has no target, not all other shapes or reference points.

An invertible linear map A after projective centering preserves actual centroid0 and the exact face lattice. It changes equilibrium tests through the positive-definite metric G=A^T A, so optimizing b/reference geometry jointly with an affine metric is an additional direction. Existing conditional affine obstructions for a different exact body or a fixed witness set must not be transferred without their hypotheses.

## Complete small exact input for method development
No historical record geometry is implicit in this note. A centered tetrahedron is given by vertices

    v0=(-1,-1,-1), v1=(1,0,0), v2=(0,1,0), v3=(0,0,1).

Its outward faces are (0,2,1), (0,1,3), (0,3,2), (1,2,3). Let e=(1/10,1/20,-1/30), and define P by replacing each v by v/(1+e dot v), keeping these faces. Every denominator is positive. Since T_b composed with T_e equals T_{b+e}, the unique normalized projective centering parameter for this exact input is b_*=-e. This gives a fully specified rational sanity example for future source code. It is not a proposed low-complexity monomonostatic body. No numerical test of this example was used to establish the identities above.

## Next research question
Build a rigorous implementation of the linear witness-cell plus physical volume minimization formulation. Then apply it to a complete durable low-C reference110 object only after obtaining its actual exact vertices/facets and literal parent. Determine whether b_* stays inside the required strict cell, and if not whether shape/reference-point/affine-metric variation can cross that obstruction while preserving C. Final acceptance always needs own uniform mass, strict110, weak000, true C<622 and a complete stored recovery capsule.
