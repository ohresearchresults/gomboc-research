# material-fbd4969fd76d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

C40 fixed-geometry affine-metric reduction.

Labels: bottom apex 0; lower ring 1,2,3,4 cyclic; upper ring 5,6,7,8 correspondingly; top apex 9.
True edges:
0-1,0-2,0-3,0-4,
1-2,2-3,3-4,4-1,
1-5,2-6,3-7,4-8,
5-6,6-7,7-8,8-5,
5-9,6-9,7-9,8-9.

The 9 by 9 cofactor of the integer graph Laplacian has exact determinant 31500. By the matrix-tree theorem there are 31500 unrooted spanning trees and 315000 choices after marking one of ten vertices as root.

Fix any rational raw N=4,M=2 stack and its exact uniformly-filled raw centroid c. Write p_i=x_i-c. For symmetric positive-definite G define, for each directed true edge i to j,
D_ij(G)=p_i^T G (p_j-p_i).
Each D_ij is linear in the six independent entries of G. Vertex i is strict unstable exactly when all its outgoing D_ij are negative.

If the affine image has exactly one strict unstable vertex r, choose one positive D_i,parent(i) from every other vertex. Because
p_j^T G p_j - p_i^T G p_i = 2 D_ij(G) + (p_j-p_i)^T G (p_j-p_i),
every chosen positive arrow strictly increases squared radius. The arrows cannot cycle and, with one root, form a spanning tree directed to r.

Conversely, if a root-labelled spanning tree has D_i,parent(i)>0 for every nonroot and D_rj<0 for every neighbor of r for one SPD G, then every nonroot has a strict escape and r is the unique strict unstable vertex.

Thus for one fixed raw C40 geometry, affine-orbit U=1 feasibility is exactly a finite disjunction of 315000 strict sign systems: linear edge inequalities in G plus G positive definite. Any feasible open cone contains rational G. Exact infeasibility certificates can be sought as positive-definite combinations of the symmetric edge-form matrices, analogous to the accepted Minimum certificate machinery.

Scope boundary: this is not an exclusion of all C40 stacks because the raw profile and actual centroid vary. It is a reusable exact fixed-geometry test and a route to discovering parameter-uniform obstruction patterns.
