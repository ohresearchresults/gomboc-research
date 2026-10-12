# C598: a unique one-facet mass correction, and a scoped exclusion

## Exact scope and evidence status

Let P be the journaled `COORD_C602_TO91_CHAIN6_G1E12`, with 137 primitive integer support rows, sorted as in its canonical `raw.json` (28,264 bytes; SHA-256 `1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599`). Let m be the exact filled-volume centroid of `BQ13_C602_TRIANGLE9_SADDLE_CHAIN_OWN121`, not the centroid of C598. Delete only support input 114 and keep every other support fixed. Denote this bounded polyhedron by Q.

**Proved here:** exactly one active halfspace cut of Q has filled-volume centroid m. That cut has at least two strict stable equilibria at m. Consequently, no replacement of support 114 alone can both restore this prescribed centre and produce a homogeneous mono-monostatic body.

This is global over the orientation and offset of that one cut, not merely over a sampled parameter chart. It is nevertheless a narrow exclusion: other target centres, simultaneous changes to any other support, moved chain vertices, joint mass/basin surgery, and the unrestricted C<624 search remain open. The accepted S8/C624 record is unchanged.

The exact-centre cut is specified by a uniquely isolated root, NOT identified with the rational nearby checkpoint below. No full incidence or equilibrium census at that root is asserted; two stable witnesses suffice for the exclusion. All new results in this package await canonical journal integration because coordinator access failed during the turn.

## Two distinct rational nonwinners

Both use the same canonical C598 supports, replacing input row 114, and no other row:

- `COORD_C598_F114_LAMBDA005_G14_C612`: replacement `[3263087649467,95414960102344,30595189901246,31686665292562]`; V171/E306/F137, own strict (18,33,49), weak-only (0,0,0).
- `COORD_C598_F114_TARGET_G14_C664`: replacement `[-195174862984739,88750730014496,123423398976022,82718382259850]`; V201/E332/F133, own strict (5,6,9), weak-only (0,0,0).

A row `[nx,ny,nz,d]` means nx*x+ny*y+nz*z <= d. Independent full A and B reconstructions agree byte-for-byte, including maximal faces, true edges, exact mass and all strict/weak face/vertex/edge tests. Third centered-integer integrations used 338 and 398 positive tetrahedra and returned zero first moments. The rational C664 centre is close to m but is not m: the exact first-moment residual has L1 norm below 9.813e-14 and, in the certificate, strictly below 1e-12. Do not transfer its full (5,6,9) census or E332 to the isolated exact-centre root.

Arithmetic comparison (maximum numerator/denominator bit length): C598 versus C612 versus C664 has primitive support maximum 477/477/477, raw-vertex fractions 910/910/910, own centroid 80115/79291/94686, volume 40171/39755/47455, and common centered denominator 80232/79409/94807. This controller does not simplify arithmetic at the full-centre endpoint.

## General uniqueness argument

Write y=x-m. Any positive-volume halfspace cut whose centroid is m contains m strictly, so its active plane can be normalized as a.y <= 1. Set K(a)=Q intersect {a.y <= 1}, and M(a)=integral over K(a) of y dy. For a,b, the integrand in

(a-b).(M(a)-M(b)) = integral_Q ((a-b).y) (1_{a.y<=1}-1_{b.y<=1}) dy

is nonpositive everywhere and strictly negative on the symmetric difference of the two cut bodies, up to null sets. Thus two distinct cut bodies cannot both have M=0. For a full-dimensional convex Q, distinct active cutting planes give distinct cut bodies. Inactive planes may describe the same uncut Q; the certified active solution here excludes that alternative.

For a convenient existence and localization proof define the globally convex finite function

F(a)=integral_Q max(1-a.y,0) dy.

At a nonzero a, gradient F(a)=-M(a), and

Hessian F(a) = integral_{Q intersect {a.y=1}} y y^T / ||a|| dA.

The derivative follows by differentiating the halfspace indicator in the coarea formula; the plane meets the interior throughout the certified ball below. Piecewise face changes do not invalidate the section integral or the integrated strong-convexity inequality. The Hessian is positive definite whenever the section contains a nondegenerate triangle off the origin.

## Rational certificate for existence and localization

Let (N,d) be the rational C664 checkpoint row. Define the exact

a0 = N/(d-N.m),  r=1/10^6.

The verification source uses 128-bit outward-rounded dyadic interval arithmetic, implemented with Python integers. No floating sign controls acceptance. It checks hashes of both independent exact audits and every geometry input. Six explicit nonnegative normal-cone decompositions of signed coordinate axes, using only unchanged supports, establish boundedness of Q; m satisfies all these supports strictly.

The active input-114 facet of the rational checkpoint has 46 vertices. Let mu be their arithmetic mean. Take its raw-lex vertices 11,140,24, and replace each v by (v+mu)/2. Subtract m to form a triangle T in the a0.y=1 section. The code proves:

1. Each coordinate of every point of T has absolute value <1; 2<|a0_x|<3.
2. For every unchanged support n_j.x<=1, the slack at each triangle vertex exceeds 1/5, and |n_j,x|<3.
3. Its projection onto the yz plane has area A in (0,1). For G0=integral over that projected triangle of y y^T dy dz, all leading principal minors are positive and det(G0)/trace(G0)^2 > 1/40000. For a positive definite 3x3 matrix this is a valid lower bound on its smallest eigenvalue.

For a=a0+delta in the Euclidean radius-r ball, move a point y in T parallel to the x axis by

tau(y)=(1-a.y)/a_x = -delta.y/a_x.

Then |tau(y)| <= t := 3r/(2-r). The new triangle lies in the new cutting plane and remains strictly inside all unchanged supports, since 3t<1/5. Its yz projection is unchanged. Each entry of y' y'^T-y y^T has absolute value at most 2t+t^2, so its integrated matrix perturbation has operator norm <=3(2t+t^2), using A<1. Also |a_x|<3+r. It follows throughout the ball that

Hessian F(a) >= lambda I,

lambda = (1/40000 - 3(2t+t^2))/(3+r) > 0.

Numerical display only: lambda is about 5.3333278055543985e-6. Exact arithmetic proves ||M(a0)||_2 <= ||M(a0)||_1 < 1e-12 < lambda*r (about 5.3333278055543985e-12).

On the ball boundary, writing delta=a-a0,

gradient F(a).delta >= lambda*r^2 - ||M(a0)||_2*r >0.

A minimizer of continuous F on the closed ball cannot lie on its boundary: the inward radial derivative would be negative. It is therefore interior, has gradient zero, and defines an exact positive-volume mass-centred cut. Strong convexity gives local uniqueness. Global convexity, or the signed-indicator argument above, gives global uniqueness among all halfspace cuts of Q.

## Two stable witnesses throughout the isolating ball

For each unchanged input support j=9,104, normalize n_j.x<=1 and form the fixed perpendicular foot

q_j=m + ((1-n_j.m)/(n_j.n_j))*n_j.

The certificate proves positive distance, strict slack >1/100000 against every other unchanged support, moving-cut slack 1-a0.(q_j-m)>1/1000, and ||q_j-m||_1<2. Consequently for every a in the ball the moving-cut slack stays above 1/1000-2r>0. Both feet lie strictly in the relative interiors of their respective, distinct facets. Each is a strict stable equilibrium at m. The unique centred cut therefore has S>=2.

## Discovery and reproducibility

A deterministic 21-step continuation moved only support 114, solving for its three plane parameters to place its volume centroid at (1-lambda)*g_C598+lambda*m for lambda=0,.05,...,1. Code, every returned parameter, tolerance, bound and outcome are retained. Numerical discovery used Python3.13.5, NumPy2.3.5 and SciPy1.17.0. The exact replay and certificate need Python3.13.5 standard library only, assertions enabled.

The floating face-graph routine overcounts true edges even at the unchanged starting body (303 instead of299) because rounding can introduce spurious corners on collinear boundaries. Its numerical E/C fields are not valid true-edge evidence; exact endpoint audits supersede them: C612, not its preliminary620, and C664, not672. The numerical S/U diagnostics are not a complete independent census either. The moment continuation supplied candidates only; the rational audits and section-patch certificate supply the claims above.

Canonical recovery dependencies are the complete `FOUR_FRONTIERS_EXACT_CORE_20260915` capsule parts at 2026-09-15T14:47:44.818Z,14:54:38.487Z,14:56:12.493Z, and the complete C598 capsule at15:33:50.633Z. This package is a complete new source patch to those already literal, durable inputs, not an assertion that a local filename or hash replaces their data.

Run `python -B -S REPLAY.py --core CORE_DIRECTORY --c598-raw CANONICAL_C598_RAW_JSON --out NEW_PROOF_DIRECTORY`. The optional `--third-mass` adds the third centered integration. `--resume` skips an existing output only after comparing its expected byte count and hash. Expected marker: `C598_ONE_FACET_SOURCE_ONLY_REPLAY_PASS`; the internal certificate marker is `C598_ONE_FACET_CENTROID_UNIQUE_AND_NOT_MONOSTABLE_PASS`.
