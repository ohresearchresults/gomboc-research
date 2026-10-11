# material-5b7063bbc081

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CENTROID_FLOW_TREE_COVARIANCE_CUT_V1

## Scope
This is an analytic common-metric obstruction for a selected rooted vertex tree. It retains every selected edge's quadratic energy and the actual centroid. It is not an exclusion of all H5 trees, a new C34 census, an attaining example, or a complexity-bound improvement. The accepted interval remains 34 <= C_min <= 622. The completed H5 norm-only obstruction is minimum-0246, SHA256 af162492fd1bf1598c3c52ebc979b310c73e8a8d04ae4b557455be4e4cae8ce1, read completely. The preceding path-energy residual theorem [internal-source-reference], SHA256 6dc7106cabaa16510d7f067ac60cff45a53c08dd55482a97025aa011b8ad4866, was also read completely. The present proof does not depend on computational outputs from either source.

## 1. Exact global centroid-flow identity
Let z_i be a finite configuration, g its actual reference point, u_i=z_i-g, and let a directed tree point toward root r. For each nonroot i put p(i) its parent, d_i=u_p(i)-u_i, and H_i=sym(u_i,d_i), where sym(a,b)=(ab^T+ba^T)/2. A weak arrow is tr(M H_i)>=0 for one common PSD matrix M.

Choose any nonnegative centroid representation

  sum_i lambda_i=1,  sum_i lambda_i u_i=0.

It need not be the unique barycentric representation or a vertex-mass model of the body. For a uniformly filled convex polyhedron it represents the TRUE volume centroid, not a replacement reference point. Define child-subtree masses

  m_i=sum_{j in subtree(i)} lambda_j,
  K=sum_i lambda_i u_i u_i^T,
  E=sum_{i != r} m_i d_i d_i^T.

Then the following matrix identity is exact:

  C := -sum_{i != r} m_i H_i = (K+E-u_r u_r^T)/2.       (CF)

Proof. Along the path from j to r, the norm telescope in matrix form is

  -2 sum_{i on path(j,r)} H_i
     = u_j u_j^T-u_r u_r^T + sum_{i on path(j,r)} d_i d_i^T.

Average over lambda_j. Each edge receives exactly its child-subtree mass m_i. This proves (CF). The identity itself needs sum lambda=1 but not centering; centering is used below and in the interpretation of K.

THEOREM. If K+E-u_r u_r^T is positive definite, no nonzero PSD common metric satisfies the complete tree. Indeed C is a nonnegative combination of negative-arrow matrices, so weak arrows imply tr(M C)<=0, while C positive definite implies tr(M C)>0 for every nonzero PSD M. This includes singular metrics and all ties without a genericity assumption.

If C >= epsilon I with epsilon>0, and W=sum_{i != r} m_i, at least one selected actual arrow obeys

  tr(M H_i) <= -epsilon tr(M)/W.

Here W is the lambda-average tree depth. When C is only PSD, the residual metric kernel must be retained; semidefiniteness alone is not an all-nonzero-PSD exclusion.

## 2. Coordinate-free sufficient criterion
Assume every m_i>0. Let B be the matrix whose row j is the indicator of the edge path from j to r; its root row is zero. Write lambda as a column and m=B^T lambda. Put

  Q=B^T diag(lambda) B,
  L=(Q+diag(m))/2.

Since L is positive definite, its inverse is well defined. Centering gives u_r=sum_i m_i d_i. If D is the matrix with edge vectors d_i as columns, then

  K=D(Q-mm^T)D^T,
  C=D(L-mm^T)D^T.                                    (CF2)

These identities follow by substituting u_j=u_r-D B_j^T and averaging, or directly from (CF). Therefore

  m^T L^{-1} m < 1                                   (CF3)

is a sufficient coordinate-free condition: the rank-one Schur complement makes L-mm^T positive definite. For an affinely full-dimensional physical configuration the tree-edge matrix D has full row rank, so C is positive definite in physical space. Equality or failure of CF3 does NOT refute the sharper physical-space test C>0. The latter can succeed because D has only three rows.

Entries of Q have a simple exact description: Q_ii=m_i; if one child subtree is nested in another, Q_ij equals the smaller/deeper subtree mass; for disjoint subtrees Q_ij=0. All matrices are rational when lambda is rational. CF3 can therefore be checked by exact linear algebra rather than a floating-point eigenvalue.

## 3. Actual uniform-centroid representations
For a genuine convex three-dimensional polyhedron, fix the selected root vertex r. Triangulate each facet not containing r and cone the facet triangles to r, omitting zero-volume tetrahedra. These tetrahedra partition the body up to measure-zero boundaries. For each tetrahedron tau with actual positive volume V_tau, add V_tau/(4V) to each of its four vertex weights. Then

  lambda_r=1/4, sum_i lambda_i z_i=g,

with g the actual uniformly filled volume centroid. Different actual triangulations can yield different valid representations; no frozen centroid is permitted when the shape moves. Nonnegative weights are sufficient for (CF); positive subtree masses are an additional hypothesis only for (CF3).

More generally one may optimize (CF) over all lambda>=0 satisfying sum lambda=1 and sum lambda z_i=g, optionally lambda_r=1/4. Every feasible lambda is a valid centroid representation and gives a nonnegative arrow stress. C is affine in lambda, so positive-definite feasibility is a small semidefinite separation problem. A numerical solution is discovery only: actual rational g, exact lambda satisfying its linear equations, and exact positive principal minors are required to promote a rational certificate. For a continuous parameter domain, those identities and inequalities need an independent uniform proof, for example original-polynomial Bernstein matrices without discarding terms.

## 4. Limits and relation to the H5 residual
The H5 result cited above proves that 3,185 pure basal-route trees survive even the impossible oracle granting all reflected-hull scalar norm inequalities. CF uses original arrow energy and so is not subject to that scalar-order ceiling. It remains INSIDE the original negative-arrow stress cone; it does not strengthen a complete original-arrow SDP by adding redundant constraints.

A single centroid representation can fail although another representation or a general original-arrow stress succeeds. Failure of every searched centroid-flow certificate is not an actual common-metric survivor. In particular, restricting lambda_r=1/4 or to one facet triangulation restricts the available flow stresses; this is a method choice, not an additional geometric requirement on a hypothetical class110 body.

The next concrete question is whether exact centroid-flow stresses or residual-energy stresses close macroscopic pieces of the genuine H5 p+q>1/2 domain, especially the 3,185 pure basal-route alternatives. No numerical tree count or domain extension is promoted by this analytic material.
