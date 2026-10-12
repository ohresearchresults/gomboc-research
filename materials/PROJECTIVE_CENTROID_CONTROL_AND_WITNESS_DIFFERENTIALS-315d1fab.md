# material-315d1fabda09

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Projective centroid control and physical/polar witness differentials

Self-contained coordinator derivation. This is a mathematical method, not a new strict110 construction, no priority claim, and not an exclusion of a family. It complements the finite V20 experiments in [internal-source-reference]. All centroids below are homogeneous volume centroids, not vertex means. The proof is independent of numerical searches.

## 1. Exact projective family and volume derivatives
Let K be a full-dimensional bounded convex polytope in R^3 with 0 in int(K). Define D={q: q.x<1 for every x in K}=int(K polar), and T_q(x)=x/(1-q.x). It suffices to test denominator positivity at all vertices. T_q is an orientation-preserving projective bijection on K; it preserves its face lattice and physical V,E,F. Its inverse on its image is T_{-q}. Its Jacobian determinant is (1-q.x)^(-4): the derivative matrix is I/d+x q^T/d^2, with d=1-q.x, and the rank-one determinant identity gives d^(-3)(1+q.x/d)=d^(-4).

Write K_q=T_q(K), V(q)=vol(K_q), c(q)=centroid(K_q), and Sigma(q)=volume covariance of K_q. The change of variables gives
V(q)=integral_K (1-q.x)^(-4) dx,
V(q)c(q)=integral_K x(1-q.x)^(-5) dx.
Hence
  gradient log V(q)=4c(q),
  D c(q)=5 E_{K_q}[y y^T]-4 c(q)c(q)^T
        =5 Sigma(q)+c(q)c(q)^T,
  Hessian log V(q)=20 Sigma(q)+4 c(q)c(q)^T.
The second identity follows by differentiating numerator and denominator: derivative of the numerator is 5 integral_K xx^T(1-q.x)^(-6) dx, whose normalized value is 5 E_{K_q}[yy^T]. Sigma(q) is positive definite because K_q has nonempty interior. Consequently log V is strictly convex and D c is everywhere positive definite.

For arbitrary initial centroid c0=c(0), the displacement relative to the image of the old centroid obeys
  c(q)-T_q(c0)=5 Sigma(0)q+O(||q||^2).
The c0 c0^T term cancels the derivative of T_q(c0). For a centered source c0=0 this becomes c(q)=5 Sigma(0)q+O(||q||^2). This establishes local three-dimensional centroid control without a density change.

## 2. Global coordinate-centroid control
The map q -> c(q) is in fact a smooth bijection D -> R^3 with smooth inverse. Here is a polytope proof of the required properness, avoiding an unsupported local-to-global leap.

Triangulate the boundary of K and cone it to0. Each positively oriented tetrahedron has vertices0,a,b,c and volume v_t>0. Its image has exact volume
  v_t(q)=v_t / [(1-q.a)(1-q.b)(1-q.c)].
This follows by taking the determinant of the three transformed columns. Summing gives V(q). The closure of D is compact because0 lies in int(K). For any q_j approaching a boundary point q*, some vertex v of K has q*.v=1. At least one nondegenerate boundary triangle containing v contributes a positive tetrahedron. Its factor1-q_j.v tends to0, and its other positive denominator factors are uniformly bounded above on closure(D). Thus that tetrahedron's volume, and therefore V(q_j), tend to infinity. This argument applies to arbitrary approaches to the boundary, including contact with an edge or face.

For an arbitrary b in R^3, log V(q)-4b.q therefore tends to infinity at the boundary of the bounded domain D. It attains a minimum in D; strict convexity makes it unique, and its stationarity equation is c(q)=b. The everywhere nonsingular Jacobian gives a smooth inverse. Thus actual centroid coordinates can be used as unconstrained parameters for this family. This does NOT mean the boundary is fixed while its centroid moves: K_q deforms simultaneously.

A useful exact polar identity is K_q=(K polar - q) polar. Indeed, for p in K polar and y=T_q(x), (p-q).y=(p.x-q.x)/(1-q.x)<=1; reversing the projective map gives equality of the bodies. No theorem from outside this document is required for the identities above.

## 3. Any prescribed interior reference point can become the image-centroid
For any p in int(K), there is exactly one q in D such that
  c(T_q K)=T_q(p).
This is stronger than the derivative at0 but still says nothing automatic about Euclidean equilibrium counts after deformation.

Proof. Set L=K-p, which contains0 in its interior. Section2 applied to L gives a unique r in D_L such that c(T_r L)=0. Since -p belongs to int(L), a=1+r.p>0. Put q=r/a. For x in K,
  1-q.x=(1-r.(x-p))/a>0,
so q belongs to D. Direct algebra gives
  T_q(x)-T_q(p)=a(I+p r^T) T_r(x-p).
The linear map on the right is invertible since det(I+p r^T)=1+r.p=a>0. Taking centroids proves the desired equality. Conversely, for q in D, set r=q/(1-q.p); this is well-defined and lies in D_L. The same invertible affine relation shows that any solution must correspond to the unique centering r. Uniqueness follows.

Equivalently the map p(q)=T_{-q}(c(q))=c(q)/(1+q.c(q)) is a smooth bijection D -> int(K). Its denominator s=1+q.c(q) is positive because c(q) is interior to K_q. Differentiating and using Section1 gives
  Dp(q)=(5/s)(I-p(q)q^T) Sigma(q),
  det Dp(q)=125 det(Sigma(q))/s^4>0.
The determinant uses 1-q.p=1/s. This supplies an interior-reference parametrization as well as the coordinate-centroid parametrization.

## 4. Exact recovery arithmetic
For rational K and rational q in D, transformed vertices and the true centroid are rational. For any oriented tetrahedron with vertices x0,x1,x2,x3 (not necessarily x0=0),
  v_t(q)=v_t/prod_{i=0}^3(1-q.x_i),
  centroid_t(q)=(sum_{i=0}^3 T_q(x_i))/4.
The volume identity follows from the determinant of homogeneous vertex columns and the determinant-one homogeneous matrix [[I,0],[-q^T,1]]. Summing signed tetrahedral masses and first moments recovers exact V(q),c(q). For the origin-cone triangulation all masses are positive and x0=0 remains0. Rational affine maps can subsequently be applied without changing homogeneity or the face lattice. The inverse centroid parameter needed for a specified rational target need not itself be rational; exact strict equilibrium signs would instead be certified for a chosen nearby rational q. No claim of exact rational target solvability is made.

## 5. Analytic eight-parameter witness linearization at a centered source
Now assume c(0)=0 and denote Sigma=Sigma(0). Let v_i be physical source vertices and p_f the polar vertices normalized by p_f.x<=1. In the projectively transformed body recentered at its TRUE centroid,
  v_i(q)=v_i + (v_i v_i^T-5 Sigma)q + O(||q||^2).
Its centered polar vertex has the exact formula
  p_f(q)=(p_f-q)/(1-(p_f-q).c(q)),
so
  p_f(q)=p_f+(-I+5 p_f p_f^T Sigma)q+O(||q||^2).
These formulas account for the volume-centroid motion, which is essential.

For a directed physical edge v->u, define g=(u-v).v (positive gives the chosen strict escape). Its derivative under projective displacement is k(u,v).q where
  k(u,v)=u(u.v)+v(u.v-2|v|^2)-5 Sigma(u-v).
To add infinitesimal affine metric G=I+H, H symmetric, its additional first-order contribution is (u-v)^T H v. One scalar scale direction is irrelevant for sign, leaving five metric parameters plus three projective parameters.

For a directed polar edge p->r define h=(r-p).p. Set B_p=-I+5 p p^T Sigma, B_r=-I+5 r r^T Sigma. Its projective derivative is
  [(B_r-B_p)^T p + B_p^T(r-p)].q.
The affine contribution has the OPPOSITE metric sign, -(r-p)^T H p, because polar coordinates transform by A^{-T} and their metric is G^{-1}=I-H+O(H^2).

These are complete first-order formulas, not code-produced experimental findings. They suggest a continuation method that controls physical and polar witnesses jointly instead of optimizing a sum that can sacrifice one side. A fixed chosen witness tree is only one admissible escape system: a failed linearization or failure for that tree is not a global obstruction. Trust-region sign and denominator controls are required; a feasible infinitesimal step is not a finite certified body. A final candidate must have exact physical coplanar-face merging, volume centroid, strict S/U/H and all weak cases checked.

## 6. Research boundary and next question
There is no mass-control obstruction by itself within the full positive-denominator projective family: any interior reference p is projectively centerable. The unresolved coupled problem is whether the SAME deformation admits a Euclidean/affine metric and physical/polar escape configuration yielding strict110/weak000 at low E. A free-center110 witness of the original undeformed body cannot be promoted merely by invoking Section3; the projective map changes the Euclidean root cells. The V20 finite experiments demonstrate why controlling one local score or one basin energy is not enough. Use centroid/reference parametrization plus the analytic physical/polar differential to identify genuinely joint directions, not to claim an already constructed C108 winner.
