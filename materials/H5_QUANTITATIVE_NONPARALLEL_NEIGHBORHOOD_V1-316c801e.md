# material-316c801e4525

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_QUANTITATIVE_NONPARALLEL_NEIGHBORHOOD_V1

## Theorem
Let z_i be any literal H5 prototype from H5_FULL_BASAL_LAMBDA_GE_2_3_V1, with full basal parameters and 2/3<=lambda<=1. Let z'_i be the corresponding vertices of a genuine convex polyhedron with the SAME listed true cyclic facets, and suppose ||z'_i-z_i||_2<=epsilon=2^-39 for every label. Recompute its actual uniform volume centroid g'. Then every nonzero PSD weak rooted true-edge cone of this new body is excluded. In particular it has at least two strict unstable vertices under every SPD metric, even allowing weak contacts.

This is a quantitative extension off the parallel-end parameter slice. No parallelism, fixed basal cuts, or prescribed centroid is assumed for the perturbed body. Its true facet lattice must be retained; proximity alone does not establish that lattice. The theorem does not exclude all H5 realizations, all E17, or establish attainment. Global34<=C_min<=622 is unchanged.

The source theorem is completely recoverable from all three materials: geometry [internal-source-reference]; atlas [internal-source-reference]; proof/verifier [internal-source-reference]. This result uses the already proved uniform gap, not a fresh atlas replay.

## Prototype bounds
Write s=1-lambda, D=6V, K=6J. The basal labels lie in s times the horizontal standard triangle; the top labels are the vertices of lambda times that triangle at height1. Their Euclidean norms and all pairwise distances are at most sqrt(2)<3/2: cross-layer horizontal squared distance is at most s^2+lambda^2<=1, and the height difference is1. Convexity gives the same diameter bound for distances to the actual prototype centroid.

There are exactly16 oriented boundary fan triangles, since sum_F(|F|-2)=16. The explicit source identity D=1-s+2As^2, 7/64<=A<=31/64, gives 2/3<=D<=1. Thus ||D z_i-K||=D||z_i-g||<=3/2.

## Lipschitz transfer of the actual moments
Set eta=1/100 and suppose epsilon<=eta. For any one boundary triangle with reference vertex norms at most R=3/2 and perturbations at most epsilon, determinant multilinearity and the scalar triple-product bound give
|det(a',b',c')-det(a,b,c)| <= (3R^2+3R eta+eta^2)epsilon <= 7epsilon.
Summing16 triangles yields |D'-D|<=112epsilon. In particular D'>0 at the specified epsilon.

The vector first-moment formula is K=(1/4)sum det(a,b,c)(a+b+c), including signs when the origin is outside. Using sum|det(a,b,c)|<=16 R^3 and ||a+b+c||<=3R gives
||K'-K|| <= [112(3R+3eta)+3*16 R^3]epsilon/4 <=168epsilon.
This is the actual uniform moment, not an assigned vertex mass or the image of the old centroid.

For A_i=D z_i-K, the previous bounds and D<=1 give
||A'_i-A_i|| <= (112R+1+112eta+168)epsilon <=340epsilon.
The true edge displacement changes by at most2epsilon. Therefore, for B_ij=sym(A_i(z_i-z_j)^T), the operator norm satisfies
||B'_ij-B_ij|| <= [340R+2R+680eta]epsilon <=520epsilon.
The norm inequality ||sym(ab^T)||<=||a||||b|| justifies this estimate; all cross terms are included.

## Transfer of the complete tree cover
Each of the461 canonical prototype certificates uses positive integer weights with total at most128. Consequently ||P'-P||<=66560epsilon. The exact prototype proof gives
P >= delta I, delta=113814715213/284103505285742592.
At epsilon=2^-39,
delta/2-66560epsilon=45020793133/568207010571485184>0.
Thus every perturbed certificate satisfies P'>delta I/2. Its literal original-arrow support remains contained in exactly the same rooted trees, and the same exhaustive covering applies. A common nonzero PSD metric with all tree arrows weakly increasing would give trace(H P')<=0, contradicting P'>0. The genuine-body conclusion U>=2 follows by the squared-norm increasing-tree argument already proved in the source theorem.

The exact volume lower bound used here is D'>=68719476715/103079215104>0. No lower bound on the smallest eigenvalue of the tested physical metric is required.

## Explicit nonparallel continuation
For any genuine prototype, set z'_i=z_i/(1+t z_{i,1}) with |t|<=2^-42. All denominators are positive. A projective map restricted to this positive affine chart maps each segment to a segment with positive reweighted endpoints, preserves convexity and the true face lattice, and changes the supporting plane n.x=h into (n+h t e_1).y=h. The basal plane remains y_3=0; the top becomes y_3+t y_1=1, nonparallel when t!=0.
The vertex displacement is at most (3/2)|t|/(1-|t|)<2^-39. Hence this entire explicit nonparallel family remains excluded with its recomputed actual homogeneous centroid. This is not the erroneous assumption that a projective map transports a uniform centroid linearly.

## Exact arithmetic check and recovery
Extract the complete block as verify_h5_robustness.py,1633 bytes,SHA256 b8072de069cb85a0c6dc505002dbe6c960fe35963e41676e1d6b3915588cad09. It requires only the complete h5_collar_weighted.py from the geometry material. Python3.13.5; its imported geometry module requires NumPy2.3.5. Run python verify_h5_robustness.py. Expected PASS. Output h5_robustness_report.json:865 bytes,SHA256 d8923718b57e822a56addd020e441bcb79dbd1d52c258bd6288d95451626f199. Coordinator exact rational execution passed; the inequalities above constitute the geometric proof.

```python
"""Exact constants for H5 perturbation transfer, not a replay of its atlas."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from h5_collar_weighted import FACETS
eta=F(1,100);eps=F(1,2**39);R=F(3,2)
delta=F(113814715213,284103505285742592)
triangles=sum(len(f)-2 for f in FACETS);assert triangles==16
assert triangles*(3*R**2+3*R*eta+eta**2)<=112
assert (112*(3*R+3*eta)+triangles*R**3*3)/4<=168
assert 112*R+1+112*eta+168<=340
assert 340*R+R*2+340*2*eta<=520
assert 128*520==66560
assert 0<eps<=eta
reserve=delta/2-66560*eps;assert reserve>0
volume_floor=F(2,3)-112*eps;assert volume_floor>0
tmax=F(1,2**42);assert R*tmax/(1-tmax)<eps
report={'identity':'H5_QUANTITATIVE_NONPARALLEL_NEIGHBORHOOD_V1','verdict':'PASS',
 'prototype_lambda_min':'2/3','vertex_displacement_bound':str(eps),
 'oriented_boundary_triangles':triangles,'D_lipschitz_bound':112,'K_lipschitz_bound':168,
 'cleared_centered_vertex_lipschitz_bound':340,'arrow_matrix_lipschitz_bound':520,
 'certificate_lipschitz_bound':66560,'prototype_stress_gap':str(delta),
 'reserve_above_half_gap':str(reserve),'D_perturbed_lower_bound':str(volume_floor),
 'projective_t_bound':str(tmax),
 'scope':'Same true H5 facets and corresponding vertices within the stated Euclidean bound of a prototype. Actual uniform centroid recomputed. All nonzero PSD weak rooted cones excluded; genuine bodies U>=2 for all SPD metrics. Not whole H5 or E17.'}
raw=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();Path('h5_robustness_report.json').write_bytes(raw)
print(raw.decode());print('BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
```
