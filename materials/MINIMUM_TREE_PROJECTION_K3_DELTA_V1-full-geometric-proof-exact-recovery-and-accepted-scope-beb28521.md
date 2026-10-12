# material-beb28521d2d1

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# MINIMUM_TREE_PROJECTION_K3_DELTA_V1

## Accepted conclusion and evidence boundary
A new finite application of a uniform-volume projection theorem excludes2706 previously open K3 positions in2142 complete genuine rooted primal facet/tree classes. Its path part has2006 positions/1646 classes; its Y part has700 positions/496 classes. The accepted K3 remainder is now6659 positions in4817 classes, in1776 open incidence domains. Of the2307 original domains,531 are wholly excluded, an increase of173 over the previous358. These are exact local K3 domain labels, not173 asserted distinct unmarked combinatorial polyhedron types.

The prior accepted K3 state was9365 positions/6959 classes, from [internal-source-reference]. The new removal layer is disjoint from all its exclusions. Its exact output contains all2706 root positions, all2142 class IDs, all173 newly closed domain IDs, and the literal positive triangulation of every nonincident genuine maximal facet in every new exclusion. No output list is abbreviated in the recovery data.

The universal accepted bounds remain V>=10,F>=9,C=2E>=34. The(10,17,9) slice remains open. No C>=36, attaining construction or exact minimum follows. The separate global TREE410 ledger remains17383/24847 excluded,7464 open; its ordinal system is not the K3 ordinal system. K2 remains278/550 accepted, with its prospective550 capsule not verified to completion. The632-type/52585-joint-root register is not updated here. Figure650 remains unverified.

## 1. General geometric theorem, not restricted to a path
Let P be a full-dimensional convex polyhedron with ten genuine vertices v_0,...,v_9, constant solid density, and its own volume centroid at0. Let M be any positive-definite real matrix. Let T be any rooted tree on these ten vertices, root u=v_r, with weak inequalities

<v_i,v_parent(i)>_M >= ||v_i||_M^2

on every parent edge. For the geometric lemma the tree edges need not themselves be polyhedron edges. In the K3 application they are checked to be genuine edges and are the exact marked tree of that domain. No assumption about S=1, absence of additional arrows, or generic strictness is used by this lemma.

For each triple A of distinct vertices other than u, suppose the tree inequalities prove

<u,sum_(v in A) v>_M >= -b(A)||u||_M^2.

Call A good when b(A)<1. If every genuine maximal facet not containing u can be triangulated into good triples using its existing vertices, such P is impossible.

Proof: cone each chosen facet triangle to u. These tetrahedra have positive volumes and disjoint interiors and partition P. A genuine facet not incident with u lies in a plane strictly separated from u; genuine convex face polygons have no redundant collinear vertices. The tetrahedron with vertices u and A has centroid(u+sum_A v)/4. Its projection on u is at least(1-b(A))||u||_M^2/4>0. The actual uniform volume centroid of P is a positive volume-weighted average of these tetrahedral centroids, so its projection on u is positive. But that centroid is0. The root u cannot be0 because the volume centroid of a full-dimensional convex body lies in its interior whereas u is a vertex. Contradiction.

All tetrahedral masses in this proof belong to the same actual body. There is no replacement by an arithmetic vertex average, independently chosen masses, a polar body's centroid, or a simplex-volume sign guess. An artificial diagonal is used only to decompose a genuine face polygon and is never counted as a true edge.

## 2. Depth projection bounds with exact rational constants
The full chain proof in [internal-source-reference] gives, along a weak parent chain x_0=u,...,x_d,

<u,x_d>_M >= -A_d ||u||_M^2,
A_d=cos(pi/(d+1))^(d+1).

This is valid for all d>=1, including zero intermediate vectors. An invertible square root of M reduces to Euclidean angles. Radius ratios are bounded by consecutive cosines; log-cosine concavity and the spherical triangle inequality reduce the minimum to cos(theta/d)^d cos(theta), whose minimum is -A_d. Thus the result applies without change to every root-to-vertex path in an arbitrary rooted tree.

The exact rational upper bounds used at depths1,...,9 are

0,1/8,1/4,7/20,27/64,49/100,17/32,23/40,61/100.

Depths1,...,5 and their exact comparisons are in the cited central-root proof. Here are full justifications for the four new depths.

Depth6: put c=cos(pi/7), t=2c. Since cos(4pi/7)=-cos(3pi/7), factoring their sum gives(c+1)(8c^3-4c^2-4c+1)=0, hence f(t)=t^3-t^2-2t+1=0. Also t>sqrt(3)>5/3. The polynomial f is strictly increasing on[5/3,infinity), and f(901/500)=32201/125000000>0. Thus c<901/1000 and A_6<(901/1000)^7<49/100. The final positive difference is7970589720967983699/10^21.

Depth7: A_7=(17+12sqrt(2))/64. Since(99/70)^2>2,
17/32-(17+12*(99/70))/64=1/2240>0.

Depth8: put c=cos(pi/9)>sqrt(3)/2. The triple-angle formula gives g(c)=8c^3-6c-1=0. The function g is strictly increasing for c>=sqrt(3)/2. Since(47/50)^2>3/4 and g(47/50)=73/15625>0, c<47/50. Then A_8<(47/50)^9<23/40; the final difference is3916401897233/1953125000000000.

Depth9: A_9=((5+sqrt(5))/8)^5. Since(161/72)^2>5,
A_9<((5+161/72)/8)^5=(521/576)^5<61/100.
The final difference is7216740056959/1585084524134400.

All rational comparisons in these arguments are checked using Fraction arithmetic by the complete source. The trigonometric identities and monotonicity arguments above supply the analytic connection; numerical cosine evaluation is not used as proof.

## 3. Eight new exact chain certificates
For a chain x_0=u,x_1,...,x_m put g_i=||x_i||_M^2-<x_i,x_(i-1)>_M<=0. A certificate for a set of chain depths D has the form

Q=B||u||_M^2+<u,sum_(j in D) x_j>_M+sum_(i=1)^m lambda_i g_i.

The scalar symmetric matrix has entry00=B, adds1/2 at0j andj0 for j in D, adds lambda_i atii, and subtracts lambda_i/2 at(i,i-1) and its transpose. Entries referring to the same position are added. If this matrix is positive semidefinite and each lambda_i>=0, then

<u,sum_(j in D) x_j>_M >= -B||u||_M^2.

Indeed Q>=0 and subtracting sum lambda_i g_i cannot decrease it. The exact source verifies positive definiteness, a stronger property, by rational LDL elimination in the order x_1,...,x_m,u and checks reconstruction of every matrix entry. This is a sum-of-squares identity for arbitrary real vectors and arbitrary common M, not a claim based on a floating eigenvalue.

The three new triple certificates are:
D346,B19/20,lambda numerator vector(1562474,2587775,4285883,4063368,2302766,2416557);
D356,B999/1000,numerators(1582616,2508946,3977473,3665265,4170128,2271006);
D256,B3/4,numerators(1529122,3127519,3513362,4004822,4565028,2489135).

The five new pair certificates are:
D16,B1337/10000,numerators(1255453,2498480,2767698,3065921,3396281,3762235);
D17,B1451/10000,numerators(1229548,2406327,2597122,2803044,3025295,3265166,3524060);
D26,B4111/10000,numerators(1008777,2476319,2184816,2361272,2551980,2758092);
D27,B4227/10000,numerators(1009109,2410061,2137219,2259278,2388312,2524709,2668901);
D67,B4991/5000,numerators(1206849,1459259,1764460,2133493,2579708,3119249,1767822).

Every numerator vector has denominator1000000; there are no omitted coefficients. The first three give21 positive LDL pivots; the next five give38, for59 in total. Their exact rational pivots are reconstructed in path_projection.json and path_projection_extra.json. For simplicity the application uses B, not the slightly stronger B minus the last Schur pivot.

The three old pair certificates at D34,D35,D45 are inherited from the fully stored central-root proof, and are rechecked exactly on every current run. Their respective usable bounds are6127/10752,46/75,3/4-13127/5250000.

## 4. Good-triangle test and complete polygon recursion
For a root and its actual tree, first obtain all ten root-to-vertex paths and depths. The basic triangle bound is the sum of its three depth bounds. A chain certificate may replace two or three of those summands only when all selected vertices occur at exactly its specified depths on ONE root-to-vertex path. This condition is essential for a Y tree and is explicitly checked; equal depths on unrelated branches are not substituted for a chain.

Any proved bound below1 suffices. The program tests old pairs, then new triples, then the five extra pairs, and stops after finding a sufficient bound. It does not require the best attainable bound. This permits a small exact certificate set even though a broader floating locator considered other directions.

For a face cycle f_0,...,f_(n-1), define D(i,j) to be an available good triangulation of the subpolygon from i to j. An edge has the empty triangulation. For every i<k<j test the triangle(f_i,f_k,f_j), D(i,k) and D(k,j). If all are available, their union is D(i,j); if no k works, this sufficient test fails for that face. Every triangulation contains a triangle incident with its closing edge, so the recursion covers all triangulations of the polygon with the available good-triangle predicate. Failure is not physical feasibility, nor a general impossibility result.

The returned triangles are independently checked to number n-2, to use exactly the original polygon boundary once, each interior diagonal twice, and to have no interleaving/crossing diagonals. They are then used in the geometric volume-centroid theorem of section1. The smallest gap among all24657 triangles used in the final new exclusions is1/1000. Therefore every tetrahedral centroid in those proofs has projection at least ||u||_M^2/4000.

## 5. Literal census application and exact count layers
The input is the complete pinned K3 register, not a sample. For all2307 rows the application verifies10 vertices,17 true edges,9 maximal facet cycles, exact vertex/facet incidence, edge-two-face incidence, connected cyclic vertex links, facet intersections, Euler characteristic and three-vertex connectivity. It checks that all nine marked tree edges are true edges, that the rooted parent paths reach all vertices exactly, and that the parent paths use precisely this tree.

The raw open register has11743 positions in8739 classes. The prior central-root and inherited-theorem deltas leave9365 positions/6959 classes. Every one of these9365 positions is processed at three nested levels:

Level0, rational depths plus old three pairs:817 positions/686 classes newly excluded, consisting of595 path and222 Y positions.
Level1, add the three new triple certificates:1731 positions/1344 classes, consisting of1355 path and376 Y positions.
Level2, add the five new pair certificates:2706 positions/2142 classes, consisting of2006 path and700 Y positions.

These are nested totals, not disjoint increments. For every remaining class, the old literal transport is checked on true edges, marked tree edges, all incidences and oriented true facet cycles. In addition the entire root-to-vertex path map is shown to commute with the vertex map. Each newly excluded class is wholly covered; a class representative is not silently substituted for unverified members.

New exclusions by tree index are585:1355,677:447,710:204,608:147,690:144,645:104,681:99,523:61,627:53,678:25,676:22,685:21,696:12,651:11,703:1. There is no new TREE410 or718 position in this delta. The central residual remains17 positions/15 classes; the quadrivalent endpoint residual remains265 positions/185 classes.

Remaining class counts by tree are410:15,585:729,608:103,627:38,645:30,651:43,676:33,677:1392,678:62,681:155,685:182,690:116,696:68,703:51,710:1615,718:185. Thus TREE523 is now absent from THIS K3 remainder, not universally excluded as a ten-vertex weak tree.

Remaining class kinds are881 Y,1069 simple/quadrivalent-leaf paths,2867 two-simple-leaf paths. Of the173 newly closed K3 domains, four are path domains279,374,398,401; the other169 are Y domains. All173 exact IDs are in the deterministic output. Counts of domains, root positions and rooted isomorphism classes are deliberately distinct.

## 6. Complete recovery graph and actually observed verification
The exact prior dependency graph is in [internal-source-reference] and its predecessor [internal-source-reference]. In particular it recovers these files without the originating sandbox:

k3_census.py,13141 bytes,SHA2569d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a, from ordered compressed halves [internal-source-reference] and [internal-source-reference] with decoder [internal-source-reference];
k3_reduction.py,5178 bytes,SHA256d3138f67a9a65d5f240fab64d68093d3833a9ae7c0c6655bc0e1403732e4a18b, literal [internal-source-reference];
central_root.py,6759 bytes,SHA256c0fa7d4662c6863efb88ac356e3518a82cbac40bea2fda838be416797868ccaf, concatenate [internal-source-reference] and [internal-source-reference] with no separator;
central_k3_delta.py,8054 bytes,SHA25632548fcc62506a2eb7d5ad6e73d7660a318eb2e9fcb29f1030ad7a836562c556, literal [internal-source-reference];
central_k3_inherited_delta.py,9259 bytes,SHA256b1163fa23106f7fffd3a6739cb5b84c2f0da8ed6db62422e89efb4d8a31e5944, literal [internal-source-reference].

Run those four generators in the order k3_census.py build, k3_reduction.py build, central_k3_delta.py build, central_k3_inherited_delta.py build. Required outputs, also pinned in the current source:
k3_domains.json,2724409 bytes,SHA256f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6;
k3_classes.json,2332920 bytes,SHA256e339f0a91bc369b599f7066ffa93075a2321978c3647e738db63195eaa4bc25c;
central_k3_delta.json,38699 bytes,SHA256e619a9380936f7b499accb7ce6de3aeb5c6dc5e721035d4ca1963d6ec257de95;
central_k3_inherited_delta.json,30360 bytes,SHA2568741265f2f347c16b0a3ef7b6c0cdc21ed80aa8b4e8e854d70fe9590b1d54630.

The exact NEW source units are:
[internal-source-reference] -> path_projection.py,6201 bytes,SHA25642f6a03f6756de1f8266c4923c59e2991b9486e01c7884720a1dfab17d54c289;
[internal-source-reference] -> path_projection_extra.py,4786 bytes,SHA2568fc3aab988f76dbe157b37b16e248ce910e6ca539883d11ed9533b4912939915;
[internal-source-reference] -> tree_projection_k3.py,9440 bytes,SHA2562d33534bf7288a79cd0e99468a20795db6148b554ebb904154296ac85983a476.

For each stem path_projection,path_projection_extra,tree_projection_k3 run:
python -S STEM.py build > STEM_build.log
python -S STEM.py check > STEM_check.log

All six commands actually completed successfully in this continuation, with assertions enabled, Python3.13.5 and only standard-library dependencies. Build/check stdout for each stem is byte-identical. No RNG, optimizer, tolerance, floating eigenvalue, condition-number assumption or unstated parameter is used in these exact reconstruction/verification commands.

Reproduced outputs:
path_projection.json,4387 bytes,SHA256851ab45dfc9d4a1852dfd4ca03ebff3b54baa8305d72cc1fff8e1154fbf73293;
path_projection_extra.json,10385 bytes,SHA256f557a51ec050499e641386858dfba64611dd5380336d04f6a468bc5ed66c423b;
tree_projection_k3.json,349646 bytes,SHA256cf1cf3fa9b318102451b594f8f5cddbbb4d16bde1d7e1832cde3fd49ca15ba60.

Stdout pins for both build/check at each stem:
path_projection:211 bytes,SHA2562eb15122107c4261b21a9114b0d952340ae7a7cf7dbe1e5b159a2b9d0a89d6ec;
path_projection_extra:171 bytes,SHA2561202441e3766d3eb260a7471e94c70d8b1ef059f3b97f4b93e5b0edcd0865476;
tree_projection_k3:141 bytes,SHA25651f03b9ab77bd8ad8c0e0328bb17505b1d96f981e2de664f527caad90c710f6c.

Expected terminal markers include PATH_PROJECTION_EXACT_THREE_TRIPLE_CERTIFICATES_PASS3 21; PATH_PROJECTION_TEN_ROOT_TRIANGLE_SCREENS_PASS10 840; PATH_PROJECTION_FIVE_EXTRA_PAIR_CERTIFICATES_PASS5 38; PATH_PROJECTION_LEVEL_SCREENS_PASS3 10 2520. The complete final line is:
TREE_PROJECTION_K3_EXACT_DELTA_PASS 2706 2142 6659 4817 1776 531 173 349646 cf1cf3fa9b318102451b594f8f5cddbbb4d16bde1d7e1832cde3fd49ca15ba60

Source files contain all coefficient numerators, denominators, branch depths, recursion rules, input pins and output serialization rules. The349646-byte output is completely regenerated, not replaced by its hash. The original sandbox is supplementary only.

## 7. Search provenance, negative results and useful next frontier
The complete floating coefficient locator is separately preserved as [internal-source-reference],2881 bytes,SHA2568f80a31e11a5847496de41be03400984cb2248027636ccccfd5ff4451a11e4c1. Its input plan is the seven initial targets followed by every pair/triple of depths1,...,9,127 solves total; initial vector(10,1,...,1), no randomness, SLSQP ftol1e-12,maxiter1000,analytic eigenvalue Jacobian and nonnegative bounds are literal. It ran with Python3.13.5,NumPy2.3.5,SciPy1.17.0,OpenBLAS0.3.30,all three thread environment variables1 and PYTHONHASHSEED0. These numerical dependencies are NOT dependencies of the exact proof.

The initial floating bounds at D56,D46,D36,D346,D356,D256,D456 were approximately.8859070369610843,.7704892076417293,.6163379937126158,.9434063264582888,.9982957104765393,.747624678714494,1.1814249073325869. Such search outputs, even when the solver reports success, are not lower bounds or infeasibility certificates. In particular D56 plus a separate depth2 estimate still exceeds1; D46 plus depth3 exceeds1; D456 was not a useful subunit certificate. No impossibility assertion is drawn from those failures. The exact accepted rational coefficient checkpoints are the eight literal vectors in section3 and the source units, not the floating output bytes. Floating regeneration can vary in final bits with numerical libraries/hardware; it is excluded from normative byte-identical recovery and from all census/bound claims.

An initially rounded triple matrix failed exact LDL. Increasing every multiplier numerator by1 at denominator10^6 produced the accepted positive certificates; the failed rounded coefficients were not accepted. Early screen-count expectations were corrected before source acceptance when the redundant D25 numerical cut was removed: the final full-root unc ertified counts are41,21,11,4,1,1,4,11,21,41, not40,20,11,4,1,1,4,11,20,40. This did not change the actual2706-position exclusion set. All accepted source pins above refer to the corrected files.

Useful next directions are the remaining6659 literal positions, especially their genuinely blocked facets under this projection test. For path root3 the four uncertified triples are{0,7,9},{0,8,9},{1,8,9},{7,8,9}; root6 is their reflection. Thus every hypothetical remaining such realization must have a nonincident maximal facet with no triangulation avoiding these triples. This is a structural constraint on genuine vertex facets, not on pole labels. The central17 positions still force the previously established exceptional maximal facet. Exploiting these smaller actual-facet configurations with shared centroid/volume data is more informative than repeating unchanged projection searches. The endpoint and other full nine-pole directions, K2, and the universal minimum remain open.
