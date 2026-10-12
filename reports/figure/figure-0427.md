# figure-0427

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Raven 11 — finite WIDTH49 event certificates; numerical endpoint recovery remains incomplete

Branch: `[internal-source-reference]`.

**No new rational endpoint is promoted by this handoff.** I do not have readable, verified copies of the new frozen height tables and their matching execution receipts. In particular, the names `FREE720_G10`, `HEIGHT_ONLY_B`, and `U1_STRONG_G5` appearing in the unfinished work are not sufficient definitions of solids. Their provisional counts, barrier values, and claimed cancellation must not be incorporated into the accepted result catalog without the literal inputs and successful exact replay.

There is, however, a complete mathematical result to preserve: **finite linear height paths in WIDTH49 admit low-degree, exact whole-path equilibrium certificates at their true filled centroids**. In one fixed maximal-complex chamber, the relevant primitive degrees are at most **3 and4 with a fixed metric**, or **5 and8 with a linearly varying physical affine map**. This yields explicit finite bounds on the number of possible mechanical event parameters and a particularly economical certificate for a genuine U/H cancellation without other births. The result accounts for changing horizontal moments and the full quadratic vertical moment; it is not a first-order mass approximation.

This does not constitute the requested new constructed endpoint. The accepted own110 incumbent remains C622.

## 1. Exact source authority and missing continuation data

The supplied literal parents are:

`figure-0421`, SHA-256 `0249d8929405ba8d63199d59a43e6f4dbcc762401666816530147fd8239cf19e`, and

`figure-0425`, SHA-256 `a28e8850f23f45ebc3e11460da8808c6d8997ef07546314940316bb482923907`.

The first contains the complete source/input closure for the original C306 and the signed-family work. The second contains the literal WIDTH49 definition and `WIDTH49_EXACT.py`. The supplied journal and parent material were read in the preceding work in this continuation; their unchanged contents remain the authority.

The exact original input is `farthest_merged_G10000.json`,2051bytes, SHA-256 `89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e`. It defines53 points on grid10000 and102 outward triangles, with actual complex V53/E153/F102, own strict121, additional weak000, and volume

`1690203202641/1000000000000`.

Its own centroid is

`(409355912737/135216256211280000,855529297349/67608128105640000,5154137003/270432512422560)`.

The missing data are specifically the newly frozen height arrays, their rational metric coefficients, and the matching new audit/proof outputs. The original geometric input is not missing. A source program that once wrote those arrays, an optimizer-output filename, or a provisional summary does not replace the arrays themselves. No new output hash or successful cold-replay marker is asserted here.

## 2. Whole-path convexity is especially simple for physical height motion

Fix the53 projected positions and let

`P_i(t)=(x_i,y_i,a_i+t b_i), 0≤t≤1`.

For any four input indices, the oriented supporting determinant is affine in t. The reason is structural: only the third coordinate varies, and every determinant term uses that coordinate from at most one row after taking differences. It is not merely a numerical observation about a chosen path.

Consequently, suppose the two endpoints have the same nominated oriented maximal complex, with all nonincident supporting inequalities strict. Every nonincident supporting inequality is then strict throughout the closed segment. Coplanarity equations for a common nonsimplicial face also persist when they hold at both endpoints, because the corresponding determinant is affine.

Thus an endpoint-to-endpoint height chord within a common chamber can have its **entire convexity and incidence verified using exact endpoint signs**. For the strict original WIDTH49 chamber, this means checking the5100 global support inequalities at the two endpoints. The actual complex remains53/153/102 throughout; this conclusion must not be used after a supporting determinant changes sign.

If contact changes are allowed, the contact parameters themselves are rational: each nonidentically-zero four-point determinant has degree at most1. Split the path at those rational contact values and rebuild the actual maximal complex in each interval. The mechanical analysis below then applies separately in each chamber.

The fixed projection still supplies a useful global complexity bound: a convex hull formed from these53 input points has at most53 exposed vertices and therefore E≤153, regardless of which input points disappear or which faces merge. This is not a statement that the original102 triangles remain maximal.

## 3. Exact finite filled mass along a height chord

Choose an oriented triangulation of the fixed chamber’s actual boundary. Integration diagonals are allowed for this calculation, but they are not counted as true edges.

For an oriented triangle f=(i,j,k), define

`d_f(t)=det(P_i(t),P_j(t),P_k(t))`.

Each d_f is affine. Put

`D(t)=Σ_f d_f(t)`

and

`N(t)=Σ_f d_f(t)(P_i(t)+P_j(t)+P_k(t))`.

Then

`V(t)=D(t)/6`,

`c(t)=N(t)/(4D(t))`.

The two horizontal components of N are affine, while its vertical component has degree at most2. These are the actual ordinary volume and first moments of the filled convex solid. No horizontal-moment constraint is needed.

If the path stays in the normalized WIDTH49 volume hyperplane, D is the positive constant D0. Otherwise, D is affine and must be recomputed from the current actual chamber. Positive endpoint volumes imply D>0 throughout a fixed valid chamber.

This distinction matters at a contact release. The old chamber’s linear equation `D_old(h)=D0` is not automatically a physical volume constraint after the hull changes. The new triangulation supplies new D and N. A numerical continuation may retain old basis coordinates for convenience, but it must not continue to call the old nominal volume the solid’s true volume.

## 4. Cubic physical primitives and quartic polar primitives

First hold the physical affine map L fixed and nonsingular. With row-vector convention, the centered physical points are

`X_i(t)=(P_i(t)-c(t))L`.

Let `G=LLᵀ`, which is positive definite. Define the polynomial vector

`C_i(t)=4D(t)P_i(t)-N(t)`.

It has degree at most2. For a directed true edge i→j, define

`A_ij(t)=C_i(t)ᵀG(P_j(t)-P_i(t))`.

Because4D>0, the sign of A_ij is exactly the sign of the physical escaping dot

`X_i·(X_j-X_i)`.

Therefore **A_ij has degree at most3**. A vertex is strictly unstable precisely when all its outgoing true-edge primitives are negative. An outgoing positive primitive excludes both a strict and an additional weak unstable equilibrium at that vertex.

For each maximal face f, choose three noncollinear vertices in its oriented cycle and let

`n_f(t)=(P_j-P_i)×(P_k-P_i)`,

`h_f(t)=n_f(t)·P_i(t)`.

Both n_f and h_f are affine under height-only motion. Define its centered-height numerator

`H_f(t)=4D(t)h_f(t)-n_f(t)·N(t)`.

The degree is at most2, not3: the horizontal components of n_f multiply the affine horizontal moments, while its vertical component is constant. Since the own centroid is strictly inside the full-dimensional solid, H_f>0 throughout a valid chamber.

Let `J=adj(G)`. For adjacent maximal faces f,g, define

`B_fg(t)=(n_fᵀJ n_g)H_f-(n_fᵀJ n_f)H_g`.

All omitted denominator factors are positive. Thus B_fg has exactly the sign of the escaping dot from the corresponding same-center polar vertex f toward g. Consequently **B_fg has degree at most4**.

A physical face is strictly stable exactly when its corresponding polar vertex has all outgoing B primitives negative. An outgoing positive B primitive excludes strict and additional weak stability on that face.

These tests use the actual own centroid throughout the finite path. Replacing c(t) by its initial value, or retaining only its derivative at t=0, would change the polynomials and invalidate the certificate.

## 5. The complete edge test uses these same four primitives

Suppose true physical edge i–j is incident to maximal faces f and g. Its strict saddle condition is exactly

`A_ij<0, A_ji<0, B_fg<0, B_gf<0`.

The first two inequalities put the orthogonal radial foot strictly inside the physical edge. The latter two put that foot strictly inside the cone generated by the two outward face normals.

For example, writing the centered polar endpoints as q_f,q_g, the coefficients of the physical edge-line foot in their span have signs determined by

`|q_g|²-q_f·q_g` and `|q_f|²-q_f·q_g`.

These are the negatives of the two directed polar escaping dots. This gives the normal-cone part of the four-primitive test directly.

The closed conditions, with at least one equality, classify the additional weak edge cases. Likewise, a weak vertex or face is classified by all its outgoing primitives being nonpositive with at least one equality. Thus the same polynomial system covers strict counts and additional weak counts; there is no need to infer H from an index formula alone.

## 6. Explicit finite bounds on mechanical events

A chamber with E true edges has2E directed physical primitives and2E directed polar primitives. Ignoring identically-zero polynomials, the number of distinct real mechanical-event parameters is at most the sum of their degrees.

For fixed L this gives

`2E·3+2E·4=14E`.

Hence a height chord in the original C306 chamber has at most **2142 distinct mechanical-event parameters**, and at most2143 open sign cells. For a chamber with E102, the corresponding bound is1428 events.

These are upper bounds, not observed counts for a particular chord. Several primitive roots can coincide, and many roots may not change the equilibrium census. Identically-zero primitives must be recorded as permanent equalities rather than counted as isolated roots; the remaining nonzero primitives still determine the finite changes of the strict/weak signature.

### The affine metric need not be frozen for a finite certificate

A similar result applies when the entries of the physical map are interpolated linearly:

`L(t)=(1-t)L0+t L1`.

Assume L(t) stays nonsingular. For lower-triangular endpoint maps with positive diagonal entries, this is automatic along their linear interpolation. The determinant need not remain1; the actual physical volume is

`det(L(t))D(t)/6`,

and the centroid transforms exactly by L(t).

Now G(t)=L(t)L(t)ᵀ has degree at most2. The physical A primitives have degree at most5. The entries of adj(G(t)) have degree at most4, so the polar B primitives have degree at most8. Therefore the corresponding bound is

`2E·5+2E·8=26E`.

For E153 this is **3978 possible mechanical-event parameters** per fixed complex chamber. This provides an exact finite-path framework for joint height/metric moves rather than only metric-frozen polishing. It does not assert that any such segment contains own110.

## 7. A small whole-path certificate for a genuine U/H cancellation

Enumerating every root of every primitive is unnecessary when the intended event is one isolated cancellation.

Consider a fixed-complex height path and an edge i–j. Suppose the only intended sign change is A_ij crossing from negative to positive. The following exact conditions are sufficient for a no-other-birth U/H cancellation:

1. A_ij has exactly one root in(0,1), crossing from negative to positive. All other outgoing physical primitives at i remain negative. The other three saddle primitives on edge i–j remain negative.
2. Every persistent unstable vertex has all its outgoing physical primitives negative throughout the interval. Every other non-event vertex has a specified outgoing positive physical witness throughout the interval.
3. Every persistent stable face has all its outgoing polar primitives negative throughout the interval. Every other face has a specified outgoing positive polar witness throughout the interval.
4. Every persistent saddle has its four primitives negative throughout the interval. Every other non-event edge has at least one specified positive primitive throughout the interval.

Together with whole-path convexity and D>0, these conditions certify the full census: i and edge i–j disappear as a U/H pair, no other strict equilibrium is born, and no other additional weak feature appears. At the event parameter the endpoint vertex and edge have the corresponding additional weak classifications. They must not be silently dropped from the wall census.

All these are exact polynomial sign statements. In the power basis `p(t)=Σ a_k t^k`, the degree-d Bernstein coefficients on[0,1] are

`beta_r=Σ_(k≤r) a_k binom(r,k)/binom(d,k)`.

Strictly positive Bernstein coefficients prove positivity over the entire closed interval; strictly negative coefficients prove negativity. Subdivision gives sharper certificates when one global coefficient test is inconclusive. A positive derivative certificate, together with opposite endpoint signs, proves the event root unique. Rational bisection then supplies a literal isolating interval without converting a floating root into a certificate.

This construction is stronger than checking only the two endpoint censuses. It is also distinct from deleting the two original C306 pole labels: every other physical vertex, polar face and mixed edge is included in the no-birth conditions.

## 8. Status of the unfinished numerical work

The unfinished attempt pursued two different mechanisms: whole-body persistence descent with temporary changes in equilibrium counts, and guarded finite steps with updated own-centroid physical/polar witnesses. It also attempted to freeze a height-only cancellation with a constant rational metric.

I cannot presently bind those attempted computations to readable literal new inputs and successful exact outputs. Accordingly:

- No claimed completed iteration count is used as finite-search evidence here.
- No provisional own211 or own121 endpoint is accepted or described as independently verified.
- No numerical search failure is converted into an exclusion of WIDTH49, a released-height chamber, or its affine orbit.
- The proposed height-only cancellation remains an unverified application of the certificate in Section7, not an established geometric event.

The exact missing dependency for that application is the pair of complete rational endpoint height tables and the common rational metric, together with their actual shared maximal complex. Those values must be recovered literally or recomputed; they must not be guessed from provisional names or from a reported event parameter.

## 9. Continuation

The useful exact continuation is now specific. A promising finite height/metric step can first be explored with the true filled centroid and both complete elder landscapes. Once its endpoint tables are frozen, use the affine supporting determinants to certify or partition the whole geometric path. In each chamber, build the cubic/quartic primitives—or quintic/octic primitives for a linearly varying physical map—and certify the full strict/weak signature, preferably using the sparse no-birth witness conditions above.

This permits a genuine finite cancellation certificate without imposing fixed horizontal moments, without assuming the initial102 triangles remain maximal after contact changes, and without mistaking a small persistence value for zero. It leaves the constructive question open: the present handoff does not supply the required new verified own110 endpoint or a complete recoverable new numerical successor.
