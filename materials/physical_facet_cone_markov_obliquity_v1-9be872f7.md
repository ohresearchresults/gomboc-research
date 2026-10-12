# material-9be872f760b4

AI research material

---

# PHYSICAL_FACET_CONE_MARKOV_OBLIQUITY_V1

## Scope
Self-contained coordinator derivation. This is NOT an exclusion of any complexity layer and NOT a class110 construction. It rules out automatically treating the canonical operator below as diagonally self-adjoint or as negative semidefinite on its mean-zero space. It does not rule out every possible geometric Gram bridge. The literal control has (V,E,F)=(5,8,5), actual (S,U,H)=(5,5,8), and no weak cells. No complexity bound is changed.

## Intrinsic physical operator
Let P be full dimensional in R^d, volume v, true homogeneous centroid 0. Actual maximal facets F_i have area A_i, outward unit normal n_i, support h_i>0, and area centroid c_i. Let q_i=n_i/h_i, w_i=A_i h_i/(d v), D=diag(w). Matrices Q,C have rows q_i^T,c_i^T. Write J=1 w^T.
Divergence gives sum A_i n_i=0 and sum A_i c_i n_i^T=v I_d. The actual facet pyramid has centroid d c_i/(d+1), giving sum A_i h_i c_i=(d+1)v g(P)=0. Consequently
1^T w=1, Q^T w=C^T w=0, Q^T D C=C^T D Q=I_d/d.
Define the intrinsic matrix
M_ij=Vol_d(conv(c_i,F_j))/v=w_j(1-c_i dot q_j),
M=J-C Q^T D.
Its entries are unaffected by translating the origin, since A_j(h_j-n_j dot c_i)/(d v) is invariant. It is also affine invariant. Relative-interior facet centroids give diagonal zero and strictly positive off-diagonal entries. M1=1 and w^T M=w^T. With A=C Q^T D, A^2=A/d and AJ=JA=0, hence
M^2+M/d=((d+1)/d)J.
Its eigenvalues are 1 once, -1/d exactly d times, and 0 in the other F-d-1 dimensions; it is diagonalizable.
For any other interior coordinate origin o, the same intrinsic M results, but the corresponding origin-based cone weights are stationary iff o=g(P). Explicitly, if g is the centroid measured from o, its unique stationary probabilities are pi_i=w_i(1-q_i dot g)=A_i(h_i-n_i dot g)/(d v). Thus the stationary probability is exactly the true centroid-based cone-volume measure, without any assumption about the polar solid's centroid.

## Reversibility theorem
The following are equivalent:
1. M admits ANY positive diagonal symmetrizer S.
2. DM=M^T D.
3. C Q^T=Q C^T.
4. c_i=G q_i for every i for a single symmetric positive definite G.
5. One centered ellipsoid touches every actual facet exactly at its area centroid.
Necessarily G=(d Q^T D Q)^(-1).
Proof: SM=M^T S and M1=1 imply that the diagonal vector of S is stationary. Irreducibility implies it is proportional to w, proving 1<->2. Divide detailed balance by w_i w_j to obtain 2<->3. Both Q and C have rank d by their mixed moment identity. Symmetry of C Q^T implies col C=col Q; write C=QG. A left inverse of Q applied on both sides of C Q^T=Q C^T gives G=G^T. The mixed moment identity forces (Q^T D Q)G=I_d/d, hence the displayed positive definite G. Conversely this formula makes C Q^T symmetric. Finally q_i dot c_i=1, so q_i^T G q_i=1. The ellipsoid {x:x^T G^(-1)x<=1} has support one against each q_i and contact Gq_i=c_i, proving 4<->5.
This is a substantial additional geometric condition, not a consequence of homogeneous centering. Non-diagonal self-adjoint inner products are not ruled out, but changing the node-coordinate inner product does not preserve the local killer inequalities automatically.

## Quantitative oblique residual
Put B=Q^T D Q, G=(dB)^(-1), Z=C-QG. Then Q^T D Z=0 and Z^T w=0. Let
P_Q=Q B^(-1)Q^T D,
R=d C Q^T D=P_Q+K,
K=d Z Q^T D.
In the stationary inner product x^T D y, P_Q is the orthogonal projection onto col Q. K maps col Q into its orthogonal complement within the mean-zero space. Direct multiplication gives P_Q K=0, K P_Q=K, K^2=0, R^2=R. Rank K=rank Z<=min(d,F-d-1).
In adapted orthonormal coordinates, R=[[I,0],[L,0]]. For each nonzero singular value sigma of L, the self-adjoint part of M=-R/d on the mean-zero space has the two eigenvalues
(-1+sqrt(1+sigma^2))/(2d)>0,
(-1-sqrt(1+sigma^2))/(2d)<0.
Indeed the restriction to its singular-vector two-plane is -(1/(2d))*[[2,sigma],[sigma,0]]. Therefore any Z!=0 creates a positive mean-zero quadratic direction, even though M itself has only -1/d and 0 as nontrivial eigenvalues.

## Complete literal rational 3D countercontrol
Vertices before centering:
(0,0,0),(3,0,0),(2,2,0),(0,1,0),(1,1,3).
Oriented actual maximal facet cycles:
(0,3,2,1),(0,1,4),(1,2,4),(2,3,4),(3,0,4).
This is a convex quadrilateral pyramid. Volume=4; solid centroid=(21/16,13/16,3/4).
Facet poles relative to that centroid, in face order:
(0,0,-4/3),(0,-16/9,16/27),(32/29,16/29,16/29),(-16/23,32/23,16/69),(-16/17,0,16/51).
Actual area centroids relative to that centroid:
(5/48,-1/16,-3/4),(1/48,-23/48,1/4),(11/16,3/16,1/4),(-5/16,25/48,1/4),(-47/48,-7/48,1/4).
Cone-volume weights:
(1/4,27/128,29/128,23/128,17/128).
The exact M has rows:
[0,9/32,29/96,23/96,17/96]
[1/3,0,1/4,7/24,1/8]
[1/3,1/4,0,5/24,5/24]
[1/3,3/8,5/24,0,1/12]
[1/3,1/8,11/24,1/12,0].
Opposite oriented 0-1-2 cycle products are 3/128=27/1152 and 29/1152. Their difference is -1/576. Any diagonal symmetrizer forces equality of these products by multiplying three detailed-balance equations and canceling diagonal entries. Hence no positive diagonal symmetrizer exists.
G has rows
[4159/5888,293/17664,-5/64],
[293/17664,1839/5888,3/64],
[-5/64,3/64,9/16].
Z has rows
(0,0,0),(20/207,10/207,0),(-4/69,-2/69,0),(4/23,2/23,0),(-20/69,-10/69,0).
Rank Z=1 and sigma^2=tr(D^(-1)K^T D K)=184/1479.
The characteristic polynomial of H=(M+D^(-1)M^T D)/2 is
(t-1)(3t+1)^2(13311t^2+4437t-46)/119799.
Its positive mean-zero eigenvalue is (sqrt(1+184/1479)-1)/6, approximately .01006354077797. The exact M still has spectrum {1,-1/3,-1/3,-1/3,0}.
All five facets and vertices are respectively strict stable and unstable, and the eight actual edges (0,1),(0,3),(0,4),(1,2),(1,4),(2,3),(2,4),(3,4) are strict saddles; weak equilibrium cells are absent. This is a universal-bridge countercontrol, not a target-class example.

## Evidence and next question
The analytic claims and literal object are self-contained. Full hull and mechanical checks were performed locally by exact SymPy 1.14.0 arithmetic. Their complete runnable source must also be preserved before claiming computational recovery is complete: physical_slack_obliquity_v1.py, 7809 bytes, SHA256 e543dc7cf55208bba16982e2ccad4bcb190eee8825b5e9903c4a1da21da4d6f0. It writes physical_slack_obliquity_v1.json, 3551 bytes, SHA256 16faa5f3c99196d64dad7ad7d9a5319e524dd479c6e72fbe1e71404cf122edb8. Hashes do not replace that source.
A concrete next bridge should retain Z and control it using actual equilibrium/incidence hypotheses, rather than silently set Z=0. A class110-specific theorem might do this; no such theorem or complexity exclusion is claimed here.
