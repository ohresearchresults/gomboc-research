# figure-0305

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# AX moving geometry: exact global moment barriers and a target-turnover atlas

## 1. Determination

**NONWINNER; new exact nonlinear feasibility obstructions.** No own-centred strict `(1,1,0)` polyhedron is promoted. The main result is not another fixed-source ballast bound or a derivative-rank calculation. It permits every old AX10 vertex to move radially by an arbitrary positive factor or disappear, both AX12 apices to move arbitrarily in three dimensions, arbitrary old-to-old hull changes, and, in the principal finite atlas, any stable/unstable feature identities.

Three conclusions materially change the AX continuation:

1. **Keeping `C` as the unique unstable vertex cannot work even with two completely free apices and no incidence restriction.** The moving family below satisfies `||g-m|| > 43 R/1000`, where `R=||C-m||`. Every old supporting plane may change. A full-dimensional version allows the old directions to move through explicit angular cones, still with completely free apices, and proves `||g-m|| > R/100`.
2. **Turning over the unstable target is insufficient when the two apices acquire at most two additional old-vertex contacts.** All `1+14+91=106` allowed-contact families are globally excluded, with `||g-m|| > R/10000` whenever there is a unique unstable vertex. At exactly three additional contacts, 356 of 364 families are excluded; the eight surviving outer bounds and their still-unexcluded unstable targets are listed explicitly below.
3. **An arbitrary return apex does not fix a radially rearranged AX12 either.** All twelve literal directions, with arbitrary positive radii, deletions and topology, plus one completely unrestricted new direction, still force `||g-m|| > R/400` under unique instability. Separately, arbitrary numbers of vertices in explicit cones around the AX12 directions are excluded without any incidence assumption.

Every theorem tests mechanics at the same selected point `m` that defines its direction constraints. Equivalently, setting `m=g`, it excludes the stated centroidal direction/contact configurations for a homogeneous mono-unstable body. A fixed shape evaluated at a different centre may leave those hypotheses.

These are uniform-volume moment inequalities, not point-mass statements. They give a definite positive residual throughout the entire specified nonlinear families, not just near the source. They do not exclude unrestricted angular deformation of the AX realization space or all possible movements of the mechanical reference relative to a fixed body.

## 2. Literal source and independent reconstruction

The authoritative parent is `figure-0302`, SHA-256 `7bee5c7c2ae1d9f02028c3b1568cf6d081bb8f8014bb9044bd6a37ffaeb16aaf`. Its literal AX12 endpoint is origin-relative `(1,1,0)` and own-centroid `(6,9,13)`. Its fixed-old-vertex two-apex cell has the inherited positive-moment obstruction. No conflict was found in its coordinates, incidence, mass or endpoint mechanical class. I independently reconstructed those endpoint facts; I did not re-certify the parent's continuous cancellation chronology.

Let `D=1073741824`. The following integer table defines `v_i=N_i/D`. The label `0` denotes a vertex, **not** the mechanical origin.

```text
label         Nx          Ny          Nz
0     -444979431   132716346   345410525
C     -358547791  1943731258   345410525
H      628762393   132716346   345410525
AS     732217676   666787415   195057784
AT     474380773   -45871008   -42488313
AU     -81367832   235950210  -437472690
AV     313340949   439524973  -216915086
AW    -955357250   405612760   136467183
AX    -345374236  -103553253  -218759588
AY    -352238969  -200951160   190060607
BP    -566452371   -64944888     6045068
BM    -357321279  -165773795   -89441010
```

The first ten rows are AX10. All twelve are the literal AX12 endpoint, not a new deformation or a relabelled seed.

### Complete actual incidence

The twenty outward AX12 maximal face cycles are:

```text
[0,H,C] [0,C,AW] [0,AY,H] [0,AW,AY]
[C,H,AS] [C,AS,AV] [C,AV,AU] [C,AU,AW]
[H,AT,AS] [H,AY,AT] [AS,AT,AV] [AT,AU,AV]
[AT,AX,AU] [AT,BM,AX] [AT,AY,BM] [AU,AX,AW]
[AW,AX,BP] [AW,BP,AY] [AX,BM,BP] [AY,BP,BM]
```

The thirty true edges are:

```text
0-C 0-H 0-AW 0-AY
C-H C-AS C-AU C-AV C-AW
H-AS H-AT H-AY AS-AT AS-AV
AT-AU AT-AV AT-AX AT-AY AT-BM
AU-AV AU-AW AU-AX
AW-AX AW-AY AW-BP
AX-BP AX-BM AY-BP AY-BM BP-BM
```

For AX10, remove the six AX12 triangles containing `BP` or `BM` and insert `[AW,AX,AY]` and `[AT,AY,AX]`. This gives its complete sixteen-face lattice; its 24 true edges are exactly the unordered pairs in those cycles. These incidences agree with the literal parent.

An exact H representation is reconstructed from each face `(a,b,c)` by `n=(b-a)×(c-a)`, `h=n·a`, `n·x<=h`, followed by clearing denominators and integer-gcd reduction. The new audit enumerates **all** input triples, accepts precisely the globally supporting planes, groups by primitive integer plane, and recovers the stated triangles and edges without a numerical hull oracle.

### Exact ordinary masses

```text
V10 = 4314676606919473104543174179
      /7427640235712281649394745344

g10.x = -1473813210086390509534743809321315697
         /18531394919535384289564522118836649984
g10.y =  9136681163149509051862738422235609781
         /18531394919535384289564522118836649984
g10.z =   825639602344978981352215841493392229
         /9265697459767692144782261059418324992

V12 = 4357994727165421785691963003
      /7427640235712281649394745344

g12.x = -387850870720730836674941978142820359
         /4679361207328982337898225456981737472
g12.y =  570676723834719916411078553549181967
         /1169840301832245584474556364245434368
g12.z = 1652705611035370547567172720577370379
         /18717444829315929351592901827926949888
```

Thus `g10≈(-0.07953061,0.49303796,0.08910712)` and `g12≈(-0.0828854311,0.4878244688,0.0882976083)`. Exact first moments are `M10=V10*g10`, `M12=V12*g12`; the latter reproduce the parent's printed fractions. Translation by the respective exact centroid gives exactly zero ordinary first moments, but not the desired mechanics. The AX12 values agree with the parent.

I integrated each body twice: first using the origin and outward boundary triangles, then using tetrahedra with common vertex `C` and the opposite boundary. Both rational computations give identical volumes and all three first moments. Explicitly, the origin-based sums are `V=sum det(a,b,c)/6` and `M=sum det(a,b,c)*(a+b+c)/24`.

### Exhaustive endpoint mechanics

```text
AX10 at inherited origin: (1,1,0)
 S: [AT,AY,AX]
 U: C
 H: none

AX10 at its exact own centroid: (6,8,12)
 S: [C,AU,AW], [AW,AX,AY], [0,H,C],
    [AT,AY,AX], [AT,AX,AU], [C,AV,AU]
 U: C,H,AS,AT,AU,AW,AX,AY
 H: C-AS,C-AU,C-AW,H-AS,H-AT,AT-AU,
    AT-AX,AT-AY,AU-AX,AW-AX,AW-AY,AX-AY

AX12 at inherited origin: (1,1,0)
 S: [AT,AY,BM]
 U: C
 H: none

AX12 at its exact own centroid: (6,9,13)
 S: [C,AU,AW], [AY,BP,BM], [0,H,C],
    [AT,AY,BM], [AT,AX,AU], [C,AV,AU]
 U: C,H,AS,AT,AU,AW,AY,BP,BM
 H: C-AS,C-AU,C-AW,H-AS,H-AT,AT-AU,AT-AY,
    AT-BM,AU-AX,AW-BP,AY-BP,AY-BM,BP-BM
```

The AX12 classifications reproduce the immutable endpoint. The AX10 own-centroid classification above is an additional exact audit in this continuation.

For reproducibility, the complete sign-test recipe is as follows. Center every vertex at the point being tested. On oriented triangle `(a,b,c)`, set `n=(b-a)×(c-a)` and, cyclically, evaluate `-a·(n×(b-a))/||n||²`; the three values sum to one, and the face is stable exactly when all three are positive. At vertex `a`, evaluate `a·(a-b)/||a-b||²` for every true neighbour `b`; all must be positive for instability. On true edge `a,b`, put `d=b-a`, `t=-a·d/||d||²`, `p=a+td`; using both incident outward normals, solve the exact 2×2 Gram system `p=beta1*n1+beta2*n2`. The edge is a saddle exactly when `t,1-t,beta1,beta2` are all positive. No edge is dropped because a face or endpoint is noncritical.

All those individual primitives are nonzero. With normals normalized to support constant one, the audit proves absolute primitive clearance greater than `1/256` for each source at the inherited origin, greater than `1/128` for AX10 at its own centroid, and greater than `1/64` for AX12 at its own centroid. These are audit-specific normalized component bounds, not the parent's differently normalized selected-witness margins.

## 3. The global mass mechanism: increasing-radius paths and a vertex-star centroid identity

Everything in the remaining mathematical sections is derived and checked in this continuation.

Translate a candidate mechanical reference `m` to zero. Write each actual vertex as `x_i=r_i u_i`, with `r_i>0` and `||u_i||=1`. Suppose `T` is the unique unstable vertex and put `R=r_T`.

Every other vertex has a true-neighbour escape with

`x_i·(x_i-x_j)<=0`.

Therefore

`r_i <= (u_i·u_j) r_j`, with `u_i·u_j>0` and `r_j>r_i`.

The strict increase follows even at equality, since distinct endpoints satisfy `||x_j||²=||x_i||²+||x_j-x_i||²` when the arrow numerator is zero. Following escapes terminates at `T`. Along any such path,

`r_i/R <= product of the positive consecutive direction cosines`.

This is a necessary consequence of actual polyhedral mechanics, not an imposed tree/cotree matching.

Now triangulate the facets not incident to `T` and cone them to `T`. These positive-volume tetrahedra partition the convex body. Each tetrahedral centroid is `(T+a+b+c)/4`. Consequently, for any unit vector `n`, if the other vertices obey

`n·x_i >= -k_i R`,

then

`n·(g-m)/R >= (n·u_T - sum of the three largest k_i)/4`. **(VS)**

There are three **distinct** non-root vertices in each tetrahedron. Using three copies of the largest `k_i` is safe but substantially weaker. The weights in this identity are the actual tetrahedral volumes; no equal-vertex-mass substitution is involved.

A positive right-hand side in (VS) is therefore an exact ordinary-first-moment obstruction:

`n·integral_P(x-m) dx >= volume(P)*R*positive_constant`.

Increasing total volume, thinning old regions, deleting vertices, or finding a full-rank local actuator cannot cancel this positive quantity while the hypotheses hold.

## 4. Unrestricted two-apex moving geometry: `C` must turn over

Define the genuinely moving family

`K(r,p,b)=conv({r_i u_i : i=0,...,9} union {p,b})`,

where `u_i=N_i/||N_i||`, each old radius is arbitrary positive, either free point `p=BP`, `b=BM` is arbitrary in R³, and any old row may be omitted or become interior. Require a full-dimensional bounded convex hull and an interior mechanical reference. There is **no containment of the original AX10**, no fixed support plane, no fixed old-edge graph, and no constraint on the stable face.

**Theorem 1.** If `C` is the unique unstable vertex at the selected mechanical reference, then

`||g-m|| > 43 R/1000`.

A short exact certificate uses

`n=(-604,3850,1260)/sqrt(16774916)`.

The finite path calculation in Section 7 proves:

```text
n·u_C > 989/1000;
negative-projection allowance for each old vertex < 167/1000;
negative-projection allowance for BP < 325/1000;
negative-projection allowance for BM < 325/1000.
```

The old negative allowances are confined to `AT,AX,AY`; their upper bounds from the rational replay are approximately `0.166719812774`, `0.166715294331`, and `0.112435007628`. Every other old ray has nonnegative `n` projection. The two free-point bounds are approximately `0.324425272370` each. These bounds apply to **all** positions of the free points consistent with unique instability, not just their literal source positions.

At most two free points can occur among the three non-root tetrahedral vertices. Thus (VS) gives

`n·(g-m)/R > (989-325-325-167)/4000 = 43/1000`.

The less rounded rational certificate gives a lower bound approximately `0.04358771107085`. The inherited unique-unstable identity `C` cannot be retained by arbitrary radial redistribution and two arbitrarily relocated apices, even after unrestricted incidence turnover.

### Full-dimensional angular version, including arbitrary additional cone vertices

Let each old direction independently satisfy

`u_i(actual)·u_i(source) >= 16383/16385`,

the cone half-angle `2 atan(1/128)`, approximately `0.895°`. Keep both apices completely free and keep the unique unstable target in the `C` cone. Then

`||g-m|| > R/100`.

The calculated lower bound is approximately `0.0170469613103`. The proof uses `||u_i(actual)-u_i(source)||<2/128`, so old-old cosine errors are less than `4/128` and separator-dot errors less than `2/128`, followed by the same global path calculation.

In fact, arbitrary numbers of additional vertices in these ten old cones are permitted, provided at most two vertices have unrestricted directions. The exact bounds are `n·u_T>974/1000`, an allowance below `184/1000` for every cone-constrained vertex, and below `362/1000` for each unrestricted vertex. Any tetrahedron has at most two unrestricted non-root vertices, so its three negative allowances sum to less than `(362+362+184)/1000`, independently of the number of cone-constrained vertices. This proves the stronger clean bound

`||g-m|| > 33 R/2000 > R/100`.

Repeated cone labels on a path are harmless because upper-weight loops can be removed. This is an unbounded-in-radius, full-dimensional moving-geometry family with unrestricted vertex count inside its cones, not an infinitesimal first jet.

## 5. Allowing unstable-target turnover: exact additional-contact atlas

Here both apices remain completely free and every old radius may move or disappear, but record which old vertices can be their true neighbours. The literal AX12 contact sets are

```text
P = neighbours_old(BP) = {AW,AX,AY}
M = neighbours_old(BM) = {AT,AX,AY}.
```

The true edge `BP-BM` is allowed. All old-old edges are allowed in the bounding calculation, whether or not they occur in the actual hull. Deleting any original contact is also allowed.

There are fourteen possible **additional** apex-old contacts:

```text
BP to 0,C,H,AS,AT,AU,AV
BM to 0,C,H,AS,AU,AV,AW.
```

These are allowed-adjacency supergraphs, not claims that every pattern is geometrically realizable or constitutes one connected hull chamber. Each certificate covers every actual hull consistent with its supergraph.

**Theorem 2.** With at most two additional contacts, no member has its ordinary centroid at the mechanical reference and a unique unstable vertex. All possible unstable targets among the twelve labels are checked, giving the uniform bound `||g-m||>R/10000`.

| Additional contacts | Patterns | Excluded | Minimum certified centroid/R floor |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0.04561931607455... |
| 1 | 14 | 14 | 0.00738297956749... |
| 2 | 91 | 91 | 0.00016054337954... |
| 3 | 364 | 356 | 0.00004824819347... over the excluded patterns |

All 356 positive three-contact cases clear the simpler exact bound `R/25000`. The eight three-contact patterns not excluded by this test are:

```text
1  {BP-H,  BP-AU, BM-AU}       remaining target: BM
2  {BP-H,  BM-AU, BM-AV}       remaining target: BP
3  {BP-AU, BP-AV, BM-H}        remaining target: BM
4  {BP-AU, BP-AV, BM-AU}       remaining targets: H,AX,BM
5  {BP-AU, BM-0,  BM-H}        remaining target: BM
6  {BP-AU, BM-0,  BM-AU}       remaining target: BM
7  {BP-AU, BM-H,  BM-AU}       remaining target: BM
8  {BP-AU, BM-AU, BM-AV}       remaining targets: H,AX,BP
```

“Remaining” means only that this necessary moment bound has not excluded it. No body, centroid root, supporting face lattice or `(1,1,0)` chamber is asserted for these eight patterns. All other target identities in each listed pattern are excluded. None offers a way to retain `C`.

This consequence concerns endpoint incidence, not event codimension: within the radial-old/two-free-apex family, a winner must have at least three additional true contacts, and with exactly three it must lie in one of the eight listed outer families. It does not establish that three independent differential controls are necessary or sufficient.

## 6. Radial return apices and angular cone unions

For fixed old directions, take the complete positive-cosine graph and let `W_ij` be its maximum path product. Unique instability at `T` implies `r_i<=W_iT R`. Put

`kappa=max_(i,T) W_iT * max(0,-u_i·u_T)`.

The simpler form of (VS) gives `||g-m|| >= R*(1-3*kappa)/4`.

For an arbitrary extra direction `w`, the exact identity

`max_(||w||=1) (a·w)_+ (w·b)_+ = (1+a·b)/2`

bounds every path using that direction. The unique unstable target is allowed to be the new vertex. The replay establishes:

| Allowed directions, with arbitrary radii/deletions | Strict kappa bound | Forced centroid distance |
|---|---:|---:|
| AX10 rays | 1/5 | > R/10 |
| AX12 rays | 1/4 | > R/16 |
| AX10 rays plus one entirely free direction | 38/125 | > 11 R/500 |
| AX12 rays plus one entirely free direction | 33/100 | > R/400 |
| Arbitrarily many vertices in AX10 cones, half-angle `2 atan(1/36)` | 31/100 | > 7 R/400 |
| Arbitrarily many vertices in AX12 cones, half-angle `2 atan(1/50)` | 8/25 | > R/100 |

The last cone angles are approximately `3.182°` and `2.292°`; their exact cosine thresholds are `1295/1297` and `2499/2501`. The cone-union statements allow arbitrary numbers of vertices, any stable and unstable identities, any hull incidence, and unbounded positive radial motion. A path may revisit cone labels, but all inter-cone upper weights are at most one; removing an abstract loop cannot decrease its upper product. The finite maximum-path calculation therefore bounds paths of arbitrary length.

In particular, literal AX12 with all twelve radial scales released plus a completely free `BR` return apex remains impossible to centre in a unique-unstable chamber. This is a larger moving-material class than the old fixed-source AX13 suggestion. It is separate from the inherited six-support-plane capacity result, which assumes containment of the original AX10 and the inherited origin.

## 7. Complete finite certificate recipe

The proof uses finite maxima, products, integer square-root enclosures and isolated roots of a monotone cubic. The following formulas and integer instructions specify the calculation independently of the supplementary files.

Write `c_ij=u_i·u_j`, `s1(c)=(1+c)/2`, and

`s2(c)=cos(arccos(c)/3)^3`.

The latter is algebraic: if `z` is the unique root in `[1/2,1]` of `4z^3-3z-c=0`, then `s2(c)=z^3`. It is the sharp upper bound for a three-link positive-cosine product with two free intermediate directions. The three link angles have sum at least the endpoint angle, and concavity of `log(cos)` bounds their product by three equal-angle links. The two-link version gives `s1`.

Use max-times matrix multiplication, `(A*B)_ij=max_k A_ik B_kj`, and pointwise maximum. Let `W` be the positive-cosine maximum-path closure, with diagonal one. For old port sets `P,M`, define `D_P,D_M` by placing `s1(c_ab)` on the corresponding within-port pairs and zero elsewhere; define `E_PM,E_MP` by placing `s2(c_ab)` on the corresponding cross-port pairs.

Every path between old endpoints uses neither free point, one free point, two separated free points, or two consecutive free points. An upper matrix is therefore

```text
T = max(W, W*D_P*W, W*D_M*W,
        W*D_P*W*D_M*W, W*D_M*W*D_P*W,
        W*E_PM*W, W*E_MP*W).
```

For a free endpoint `p` with old ports `P`, and the other free point having ports `M`, define

```text
A^p_(a,t) = 0 if a is not in P;
A^p_(a,t) = max(W_(a,t),
                 max_(b,d in M) W_(a,b)*s1(c_bd)*W_(d,t)) otherwise.
B^p_(b,t) = W_(b,t) if b is in M, and 0 otherwise.
```

For an old target `t` and unit separator `n`, the per-vertex allowances in (VS) are

```text
old vertex i:
 k_i = T_it * max(0,-n·u_i)

free vertex p:
 k_p = max(max_a A^p_(a,t)*s1(-n·u_a),
           max_b B^p_(b,t)*s2(-n·u_b)).
```

For target `p` itself free, use `n=u_p`. The old-vertex allowances are

```text
k_i = max(max_a A^p_(a,i)*s1(-c_ai),
          max_b B^p_(b,i)*s2(-c_bi)),
```

and the other free vertex has allowance

`max_(a in P,b in M) W_ab*s2(-c_ab)`.

These cover all positions of both free directions. Reversing an undirected path preserves its cosine product. Each free vertex occurs at most once on a radius-increasing path. Allowing repeated old labels in the matrix upper bound only enlarges the feasible envelope.

For each old target, the atlas tries its own ray and the following additional exact integer directions, normalized to length one:

```text
AS: (3,4,-1)          AX: (-3,-1,-4)
AV: (1,3,-1)          AY: (-3,-1,1)
AT: (4047,562,-282)   AW: (-3513,1845,1016).
```

It retains the strongest certified lower bound, rather than replacing a successful radial separator with a worse tilted one. This nonradial step and the three-distinct-vertices refinement are essential; the cruder radial maximum test leaves several false unresolved cases.

### Exact outward-integer reconstruction, with no transcendental oracle

The supplementary standalone program is convenient, but the entire finite reconstruction is specified here:

1. Set `Q=2^40`. For integer vectors `a,b`, let `d=a·b`, `G=(a·a)(b·b)`, and `k=isqrt((d² Q²)//G)`. If `d>=0`, the cosine interval has integer endpoints `(k,k+epsilon)`; otherwise use `(-k-epsilon,-k)`, where `epsilon=0` exactly when `k² G=d² Q²`, and `epsilon=1` otherwise. Divide endpoints by `Q` to obtain the rational interval. This also normalizes every listed integer separator by exact enclosure.
2. Store nonnegative weights as integers over `Q`. Every multiplication is `mul(A,B)=ceil(A B/Q)`. Initialize `W0` to the max-times identity and perform `n-1` Bellman updates `Wnext=max(W,B*W)`, using the upper positive-cosine matrix `B`. Matrix multiplication uses `mul` and maximum. Thus every possible old-direction path is bounded; cycles cannot improve a product of weights at most one.
3. Given an upper cosine integer `c`, compute the upper `s1` integer as `ceil((Q+c)/2)`. For `s2`, find by integer bisection the smallest integer `z` in `[Q/2,Q]` with `4z³-3z Q² >= c Q²`; return `ceil(z³/Q²)`. The cubic is monotone on that interval. For a negative cosine argument, negate the lower cosine endpoint before these operations.
4. Form `D,E,T,A,B` by the formulas above, evaluating displayed products left-to-right with outward multiplication throughout. For each old target, try its own ray and its listed optional separator, form all twelve negative-projection caps, set the target cap to zero, and subtract the three largest cap integers from the lower separator-target dot integer. For each free target use the displayed free-target formulas and numerator `Q` minus the three largest caps. Division by `4Q` gives a certified lower bound on `||g-m||/R`. Retain the largest bound over permitted separators for each target, then the smallest over target identities.
5. Enumerate the fourteen additional contacts in the printed order and all subsets of sizes `0,1,2,3`. All 106 cases through size two have numerator `e` satisfying `10000 e>4Q`. Exactly 356 size-three cases satisfy `25000 e>4Q`; the eight others and their nonpositive target bounds are precisely the table above. No root, incidence input, optimization trajectory or external file is needed to regenerate this determination.
6. For the unrestricted-two-apex `C` theorem, set both port sets to all ten labels and use integer separator `(-604,3850,1260)`. The exact checks are `1000*d_lower>989Q`, `1000*max(old_caps)<167Q`, and `1000*max(free_caps)<325Q`. For the full-dimensional old-cone version at `q=128`, increase each old-old cosine upper endpoint by `ceil(4Q/q)`, clamped to `Q`, and decrease each separator-old cosine lower endpoint by `ceil(2Q/q)`, clamped to `-Q`; rebuild every path and cap. The resulting numerator satisfies `100e>4Q`. It also verifies `1000*d_lower>974Q`, every old-cone allowance below `184Q/1000`, and each unrestricted allowance below `362Q/1000`. Thus at most two unrestricted vertices and arbitrarily many old-cone vertices still give the stronger bound `33R/2000`.
7. For the radial/cone-union table, use the simpler allowance `kappa=max W_it*(-c_it)_+`. For one completely free direction replace `W` for old endpoints by `max(W,W*s1(c)*W)`, and also include `max_(i,a) W_ia*s1(-c_ia)`, which bounds either free endpoint/target. The resulting exact upper integers, in table order, are `212865054998`, `255489502280`, `333941869741`, `362748632763`, `340621074385`, and `350235863445`, all over `Q`. They satisfy the stated clean rational thresholds.
8. For cone-union pair bounds with half-angle `delta=2 atan(1/q)`, put `Cnum=q^4-6q²+1`, `Snum=4q(q²-1)`, `den=(q²+1)²`. These are exact `cos(2delta),sin(2delta)` numerators. If the central cosine interval is `[l,h]/Q`, enclose its sine above by the same integer-square-root procedure applied to `(G-d²)/G`, obtaining `sh/Q`. The broadened upper endpoint is `Q` when `h*den>=Cnum*Q`, and otherwise `min(Q,ceil((Cnum*h+Snum*sh)/den))`. The lower endpoint is `-Q` when `l*den<=-Cnum*Q`, and otherwise `max(-Q,floor((Cnum*l-Snum*sh)/den))`. Use these in step 7. The cases `q=36,50` have positive `Cnum,Snum`, so every stated rounding direction is valid.

This integer reconstruction uses bounded Bellman closure and outward rounding after each product. The separate rational replay uses exact Fraction products and Floyd closure, independently checked by a Bellman recurrence. Both reproduce the threshold conclusions and finite pattern counts. Their agreement is arithmetic/algorithmic replay within this work, not external mathematical peer review.

## 8. What was attempted, and what is not a result

I first reconstructed the literal AX10 and AX12 using exact supporting-triple and independent mass calculations. I then tested unrestricted-coordinate centroid descent inside the inherited mechanical sign cell, topology-changing direct hull optimization, and hard-centering searches with ten old radial variables and two free apices. None produced a verified winner. Some numerical optimizer scores were misleading near collapsed features; a separate whole-hull check retained extra equilibria. Those points were rejected and are not promoted, exactified or used to prove infeasibility.

The productive change of method was to bound the **entire possible negative first moment** from the necessary radius-increasing paths. The first radial separator bound left apparent gaps. Tilted separator directions removed several of them; recognizing that a vertex-star tetrahedron has three distinct non-root vertices closed every zero-, one- and two-additional-contact family. The remaining three-contact enumeration is an exact necessary-condition atlas, not a sampling result.

The source endpoint checks and all finite threshold assertions passed a rational implementation and the separately written outward-integer implementation. No scheduler, journal update or claimed unseen parent artifact is involved.

## 9. Precise remaining freedom and useful continuation

A convenient exact continuation chart is

```text
x_i = lambda_i * N_i/D,  i=0,...,9;
x_BP = (p1,p2,p3);
x_BM = (b1,b2,b3).
```

It has sixteen scalar variables before constraints. In each actual triangulated hull cell, ordinary volume is a cubic polynomial and the three first moments are quartic polynomials with rational coefficients. Impose the three moment equations and one scale condition, such as `||x_T||²=1`; this leaves twelve formal shape degrees of freedom wherever those four constraints are independent. The excluded families are empty for the desired centred mechanics despite that dimension count. Omitting old rows is allowed and reduces the dimension; giving an old vertex independent direction motion adds two angular variables.

The most useful surviving low-complexity search is not another AX13 local ballast solve. It is **a joint target-turnover and contact-changing solve**, starting with one of the eight unexcluded three-contact supergraphs or allowing a fourth additional contact. For example, permitting `BP-H`, `BM-AU`, and `BM-AV` leaves only `BP` as a possible unique unstable target under this certificate. Solve the actual quartic moments with that target, allow the stable face to be selected by the rebuilt hull, and impose full feature tests only on the actual incidence. No realization of that example is supplied here; it is a delimited unexcluded family, not a candidate.

Alternatively, retain `C` only by leaving the old-direction restriction: a two-free-apex approach must move at least one retained old direction outside the explicit `cos(delta)=16383/16385` neighbourhood, or supply more unrestricted directions. Merely changing which old support planes survive does not evade Theorem 1. Conversely, keeping `BP` and `BM` on their literal rays and adding just one unrestricted `BR` is ruled out by the AX12-plus-one-free-direction theorem. That is not the same family as three simultaneously unrestricted apices.

Moving the mechanical reference is another genuine escape only when it changes the old directions relative to that reference enough to leave these hypotheses. A simultaneous translation of the body and reference changes none of the inequalities or centroid discrepancies. The unrestricted moving-centre/fully angular AX problem remains open in this handoff, as do the eight surviving contact patterns and the unrestricted two-free-apex family with a different unstable target.

**Bottom line:** the parent successfully turned over a stable feature while retaining `C`. This continuation proves that much more aggressive volume redistribution—arbitrary old radial motion and two completely free apices—still cannot centre that protected-`C` architecture. With unstable-target turnover admitted, all contact patterns through two additional edges are also impossible. This is a global centring-capacity determination for moving material, not another locally full-rank but globally inadequate actuator.

## 10. Supplementary replay package

Exact scripts, complete rational ledgers, source audits and replay transcript (`AX_moving_geometry_exact_KQ73.zip`)

Standalone integer obstruction verifier (`AX_moving_geometry_standalone.py`)

Complete handoff, including inline executable verifier, as Markdown (`AX_moving_geometry_HANDOFF.md`)

Machine-readable handoff (`AX_moving_geometry_result.json`)

Clean-extraction replay transcript (`AX_moving_geometry_clean_replay.txt`)

Run `bash RUN_ALL.sh` from a clean extraction. The replay joins all isolated component processes and ends with:


[Encoded source block omitted; the code in this passage is incomplete.]


The finite source, all continuation-critical formulas, eight remaining patterns, exact thresholds and complete outward-integer reconstruction recipe are included above; none depends solely on a sandbox attachment. No new OBJ/STL is claimed because no successor polyhedron is promoted.

A clean extraction was replayed successfully. All 21 frozen package hashes matched before replay and after regenerated certificates, and the complete replay reached its terminal success marker. Archive SHA-256: `bbc86858325e8d5b931fc3aa7ef47927f27c927020bf852f294836c47f42d526`.
