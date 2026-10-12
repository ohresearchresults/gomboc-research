# material-67e95a99930b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact two-amplitude physical feature atlas V2

## Status and purpose

Coordinator analytic theorem and exact completed computation. The general method is a finite exact decision procedure for proper110 without additional weak equilibria on each fixed relative eigenframe of a fixed actual uniformly filled centred polytope. It never separates the primal and polar metrics. A rational E17 control has been completely computed, including an exact feature-boundary reduction. No C600 atlas has yet been executed, no all-orientation exclusion has been obtained, and no bound changes: 34<=Cmin<=622, with canonical C622 unchanged.

The actual control is the literal cut-and-stack body of fully read immutable result minimum-0279, SHA-256 d29ef38046c1ca99c02309710e454af21163746b81c7c780054e30b1f102b55a. It is not the older symmetric b=1/6 small-cut family. The computational source below embeds every exact coordinate, facet cycle and centroid needed here; this computation does not need the originating sandbox or a hidden centroid-flow source.

## 1. Physical primitives

Let X_i be the actual volume-centred vertices of a full-dimensional convex three-polytope. Let Q_f be the supporting pole of each TRUE maximal facet, so Q_f dot X_i<=1, equality on that facet. Let M be the primal SPD metric and N=M^-1 the SAME physical inverse. For every true edge ij with incident facets fh, define four numbers

D_ij=X_i^T M(X_j-X_i), D_ji=X_j^T M(X_i-X_j),
D_fh=Q_f^T N(Q_h-Q_f), D_hf=Q_h^T N(Q_f-Q_h).

A vertex is strict U exactly when every outgoing primal primitive is negative. A facet is strict S exactly when every outgoing polar primitive is negative. An edge is strict H exactly when all four displayed numbers are negative. A physical weak edge packet has all four nonpositive and at least one zero; a primitive zero accompanied by a positive escape is not by itself a physical weak equilibrium. These are the run's actual true-feature conventions, not a triangulation census.

For a generic metric with no zero primitive, all equilibria are nondegenerate and S+U-H=2. Thus S=U=1 implies H=0. We still evaluate the full four-number packet at every accepted representative; Euler's identity is not a substitute for the physical inverse or true facets.

## 2. Exact two-amplitude inverse

Choose N0 SPD and M0=N0^-1, and nonzero u,v with u^T M0 v=0. Put a=u^T M0 u and b=v^T M0 v. For 0<=p,q<1, set

N(p,q)=N0+[p/((1-p)a)]uu^T+[q/((1-q)b)]vv^T,
M(p,q)=M0-[p/a]M0uu^T M0-[q/b]M0vv^T M0.

Then both matrices are SPD and N(p,q)M(p,q)=I. To see this, whiten by N0: the two normalized directions N0^-1/2 u/sqrt(a), N0^-1/2 v/sqrt(b) are orthonormal. N has relative eigenvalues 1/(1-p),1/(1-q),1 in these directions, and M has the reciprocal relative eigenvalues. This is an exact physical parameterization, not a convex relaxation of pairs.

Each primal primitive is affine in p,q. Each polar primitive, after multiplication by the positive denominator (1-p)(1-q), is

A+(B-A)p+(C-A)q+(A-B-C)pq,
A=Q_f^T N0(Q_h-Q_f),
B=(Q_f dot u)((Q_h-Q_f) dot u)/a,
C=(Q_f dot v)((Q_h-Q_f) dot v)/b.

Consequently all 4E signs are signs of rational bilinear polynomials f=a0+b0 p+c0 q+d0 pq; primal d0=0, and polar a0+b0+c0+d0=0.

Every SPD target N, up to a positive scalar, has such a representation for SOME M0-orthogonal pair u,v: whiten N relative to N0 and scale its smallest eigenvalue to one. The difference from identity is PSD of rank at most two. For any one fixed complete M0-orthogonal frame, its three pairs cover the entire positive diagonal relative-frame family up to scaling. This does NOT make three fixed pairs an all-orientation atlas. Rational frames obtained by rational Gram-Schmidt are dense, so exhaustive enumeration of rational frames gives a semidecision procedure for a robust proper110 attainer on a rational fixed body. Finite failed frames do not prove nonexistence in all orientations.

## 3. Finite exact projection with degree at most two

Write each primitive f_i(p,q)=A_i(p)+B_i(p)q, with A_i,B_i affine. Project to the p axis all real roots in [0,1] of

A_i, B_i, A_i+B_i,
and A_i B_j-A_j B_i for every pair i,j,

and include 0,1. The first three families account for the boundaries q=0, poles or vertical components, and q=1. Pair polynomials account for crossings of zero graphs. Every projected polynomial has degree at most two. Identically zero projections are ignored, but identically zero primitives themselves remain in the full packet. Coincident zero graphs and shared factors do not need artificial perturbation.

Between consecutive distinct projected roots, all finite graphs q=-A_i/B_i retain their order and their presence inside (0,1). Choose a rational p in that interval and a rational q between every two consecutive graph values, including boundaries 0 and 1. These finitely many representatives meet every two-dimensional open sign chamber. We catalogue sign vectors, not a full adjacency graph; disconnected regions can have the same sign vector, which is harmless for a census decision.

The implementation represents rational roots exactly and irreducible quadratic roots by their primitive integer minimal polynomial with positive leading coefficient and the sign of the radical. Dyadic integer-square-root enclosures are refined until all distinct roots are disjoint and ordered. No floating-point ordering, tolerance, optimizer or random sample enters the acceptance calculation. All three completed charts separated their roots at 16 bits. The finite 16384-bit guard raises an error rather than claiming completion if it were reached.

Why this open-chamber calculation decides the stated target: a proper110 metric without additional physical weak equilibria has strict margins at its two genuine equilibria and positive escape margins on every remaining potential physical contact. Therefore that property persists in a relative neighbourhood of the metric. Incidental primitive zeros do not destroy this openness. A target lying on p=0 or q=0 can be perturbed into the square; a target on any nonidentically-zero primitive curve can be perturbed away from the finite union of these curves. Identically zero primitives, when present, must be retained. Hence an isolated lower-dimensional sign stratum cannot conceal a proper110weak000 target from the full method. The calculation is NOT a complete census of all lower-dimensional weak strata and does not establish an all-weak-root U2 theorem.

## 4. Exact feature-boundary reduction

Enumerating every primitive zero wastes many curves which cannot change S or U. There is an exact reduction, not a numerical pruning rule.

For each vertex, its strict U region in the open (p,q) square is the intersection of its outgoing primal halfplanes. Clip the closed square by these rational affine inequalities. If the resulting polygon has no positive area, the vertex is never strict U in the open square. If an outgoing primitive is identically zero, it is also never strict U. Otherwise retain only constraints supporting positive-length polygon edges not already on the square boundary. A full-dimensional convex polygon is the intersection of the halfplanes of these edges and the domain edges. Redundant constraints meeting the polygon only at a vertex cannot affect its interior. Thus the retained rows determine precisely the original strict U region throughout the open domain.

For each facet, let r=p/(1-p), s=q/(1-q), then introduce

xi=r/(1+r+s)=p(1-q)/(1-pq),
eta=s/(1+r+s)=q(1-p)/(1-pq).

This bijects the open unit square onto xi>0, eta>0, xi+eta<1, with inverse p=xi/(1-eta), q=eta/(1-xi). A polar row a0+b0 p+c0 q+d0 pq with a0+b0+c0+d0=0 has the same sign as a0+b0 xi+c0 eta, because the original numerator equals (1-pq) times this expression. Each strict S region is therefore a convex polygon in this triangle. Apply the same exact boundary-support reduction, retaining the ORIGINAL corresponding bilinear rows for the common (p,q) arrangement.

The union of all retained U and S rows determines every generic (S,U) region. At a sample for this reduced arrangement, choose rational p and q away from all OMITTED primitive zero sets as well: first avoid the finitely many vertical whole-zero p values, then avoid the finitely many q roots. The program does this by an explicit infinite rational sequence with only finitely many forbidden choices. With no identically zero primitive, the chosen representative has no weak packet; full direct census is checked against (S,U,S+U-2,0). This determines whether a proper110 chamber exists without computing every irrelevant full sign chamber.

The reduced implementation deliberately requires no identically zero primitive. Use the full algorithm otherwise. Reduced sign-vector counts and full sign-vector counts are different quantities. Equality is claimed only for the attainable census TYPES, verified exactly for all three completed charts.

## 5. Complete actual control and observed results

The complete runnable source is immutable material [internal-source-reference], named feature_atlas.py.txt. Save those exact bytes as feature_atlas.py. It embeds the ten literal rational Y rows and the nine maximal facet cycles from the stated parent. It verifies all supporting triples, all strict nonfacet inequalities, all 17 true edges, positive tetrahedral fans, actual volume 47426669/140625000, and actual centroid

(305383217/94853338000,6871784228327/28456001400000,487569104171/1897066760000).

It integrates the full actual covariance Sigma exactly from those tetrahedra, takes N0=Sigma, and constructs its M0-orthogonal frame by rational Gram-Schmidt from (1,0,0),(0,1,0),(0,0,1). All inputs and frame rules are embedded; there are no non-default unreported parameters.

Pair (0,1): full projection polynomials1936, critical roots427, samples6011, full sign vectors114, minimum generic S+U=6 with S>=3,U>=3. Feature reduction retains23 of68 rows, projection polynomials262, roots156, generic samples2146, reduced sign vectors108,22 census types.

Pair (0,2): full projection polynomials1701, roots459, samples7741, full sign vectors198, minimum generic S+U=4 with S>=2,U>=2. Reduction retains24 rows, projection polynomials279, roots147, samples2021, reduced sign vectors155,28 census types.

Pair (1,2): full projection polynomials1701, roots307, samples4646, full sign vectors149, minimum generic S+U=4 with S>=2,U>=2. Reduction retains13 rows, projection polynomials84, roots30, samples297, reduced sign vectors58,16 census types.

All three are complete on their entire two-amplitude squares, and none has proper110weak000. Their union is the complete fixed-frame metric family, including its finite lower-boundary metrics by the openness argument. This is an actual-body nonwinner and a reusable exact method, not a whole TREE410 or E17 exclusion. The previous parent's selected TREE410 obstruction and complementary dual-tree detection retain their separate scopes.

The generated JSON contains all exact coefficient rows, actual covariance and rational frame, rational witnesses for every census type, feature selectors, all statistics, and the full sign-vector digests. Digests for pairs01,02,12 respectively:
4eef3b3df04151192e24813ad19dbe76fb7ddfcc16dc6ddaaba40c730b98aeb6
38cd3a37f06dff7745d1582d6c13b46b31156570a4e8a59b1ceadb0c72ac52a6
244938556e8323a32aaad9b09a6f5abd0fd3ba7694b3d5a9d8929fdc5435b846

## 6. Additional exact metric mechanisms

For a single inverse rank-one ray N(t)=N0+t ww^T, t>-1/eta, eta=w^T M0 w, the exact inverse is M0-t M0ww^T M0/(1+t eta). A primal primitive has affine numerator D0+t[eta D0-(x^T M0w)(e^T M0w)] and every polar primitive is affine in t. All event parameters are therefore rational for rational data; all open intervals on a ray can be enumerated exactly, including births followed by later cancellations. No first-event assumption is needed.

For an individual initially negative primal arrow D=x dot e<0 with Euclidean nonzero x,e, put c=-D/(||x||||e||). If 0<c<1, the smallest possible condition number of an SPD metric M making x^T M e>=0 is

kappa_crit=(1+c)/(1-c).

Indeed A=(xe^T+ex^T)/2 has eigenvalues lambda_plus=(D+||x||||e||)/2>0, lambda_minus=(D-||x||||e||)/2<0 and zero. After scaling lambda_min(M)=1, tr(MA)<=kappa(M) lambda_plus+lambda_minus. Equality is attainable by putting the largest metric eigenvalue along the positive eigendirection and the smallest along the negative one. The zero eigendirection is free. Equivalently an inverse rank-one increase along the negative eigendirection attains the same threshold. If c=1, x and e are antiparallel and the arrow remains negative for every SPD metric. This is a sharp analytic single-arrow barrier, not an executed numeric C600 star threshold. Taking the minimum over a vertex's outgoing arrows gives the first possible loss of that strict U star under a condition-number bound.

The C600 parent minimum-0278 has two unstable vertices neither incident to its sole saddle edge. The already preserved [internal-source-reference] therefore excludes a first ordinary single-contact fixed-body cancellation directly to110. The atlas and complete rank-one rays are useful precisely because they allow births and subsequent events. Changing actual shape or carrier remains a separate viable mechanism. The exact algebraic C600 centroid-completion checkpoint must not silently be replaced by its rational midpoint: a nearby rational body would be a distinct object, requiring its own actual centroid and true-feature census.

## 7. Reproduction and evidence boundary

Dependency: Python standard library only; observed CPython3.13.5 with assertions enabled. Python>=3.9 is the source's intended compatibility, not a claim of multi-version execution.

Input feature_atlas.py:12964 bytes, SHA-256 11fdb454563c9f0ec21407ef0c0be33d6f994778a4f6687608beddefc8d64aa1, exact material [internal-source-reference].
Output feature_report.json:240239 bytes, SHA-256 ea07c0c9e6abd837168d3589705f2f4b8be23d4454f28763432d253deb5273aa.

Reconstruction command:
python -B -S feature_atlas.py > feature_report.json

Verification command:
python -B -S -c "import hashlib,json,pathlib; p=pathlib.Path('feature_atlas.py').read_bytes(); r=pathlib.Path('feature_report.json').read_bytes(); assert len(p)==12964 and hashlib.sha256(p).hexdigest()=='11fdb454563c9f0ec21407ef0c0be33d6f994778a4f6687608beddefc8d64aa1'; assert len(r)==240239 and hashlib.sha256(r).hexdigest()=='ea07c0c9e6abd837168d3589705f2f4b8be23d4454f28763432d253deb5273aa'; assert json.loads(r)['marker']=='EXACT_TWO_AMPLITUDE_PHYSICAL_FEATURE_ATLAS_V2 PASS'; print('EXACT_TWO_AMPLITUDE_PHYSICAL_FEATURE_ATLAS_V2 PASS')"

Expected stderr reports completed frame pairs0 1,0 2,1 2 with sign-vector counts114,198,149 and minimum S+U6,4,4. The expected JSON marker is EXACT_TWO_AMPLITUDE_PHYSICAL_FEATURE_ATLAS_V2 PASS.

Normal and fresh source-only cold runs were observed with byte-identical reports. The final persisted source differs from the earlier12963-byte local source by one blank line only; the exact12964-byte persisted version was then executed and again gave the identical report. The source hash above identifies the persisted runnable unit, not the obsolete whitespace version. Hash equality is a recovery check; correctness rests on the analytic coverage argument and the exact checks performed by the program.
