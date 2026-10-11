# material-419e3c92231c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# PRISMATOID_ALL_SPD_U2_V1
## Recovery capsule part 4 of 4: full proof and exact recovery

### Accepted statement and scope

For every 0<t<1/2, the uniformly volume-filled genuine polytope TWO_SINK_PRISMATOID_V1, evaluated at its actual volume centroid, has at least TWO STRICT unstable vertex equilibria for EVERY positive definite metric M. Its dual metric is necessarily N=M^-1. The result includes every affine image of the actual family. No assumption S=1, H=0, or absence of weak contacts is used. In particular no member of this entire shape-parameter times full-SPD family can be an attaining proper110weak000 example.

This is NOT the whole realization space of its graph and NOT every prismatoid. It is not the earlier bevel or roof8 graph, not a newly constructed110, and not a universal E17 exclusion. The accepted global bracket remains34<=C_min<=622. The native graph enumeration below does not change any FULL/LOCAL or abstract rooted-tree registry count without an explicit incidence correspondence and overlap calculation.

The prior ROOT_STAR_CAP_AND_SPECTRAL_SINK_CONES_V1 certificate remains useful: it forces S>=2 on two complete condition-number sectors of this same family, including a sector where no individual facet is uniformly stable. The present primal result removes the metric-sector restriction for the110 exclusion. It does not by itself show S>=2 at all metrics.

### 1. Exact actual geometry

Let H=5/2. The exact ordered vertices are
v0=(-2,-2,0),v1=(2,-2,0),v2=(2,2,0),v3=(-2,2,0),
v4=(3,3,H),v5=(-1,3,H),v6=(-2,1,H),v7=(-2+t,0,H),v8=(-1,-1,H),v9=(3,-1,H).
The true maximal oriented facet cycles are
F0=(0,3,2,1),F1=(0,1,9,8),F2=(0,6,3),F3=(0,7,6),F4=(0,8,7),
F5=(1,2,4,9),F6=(2,3,5,4),F7=(3,6,5),F8=(4,5,6,7,8,9).
They have precisely10vertices,17trueedges,9maximalfacets. The two horizontal faces have4and6vertices. Facet triangulation diagonals are NOT mechanical edges.

Put D(t)=105-2t>0. The actual volume and own centroid are
V(t)=5D/12,
g_x=(-2t^2+15t+133)/(4D),
g_y=(2t+105)/(2D),
g_z=5(215-6t)/(8D).
Equivalently the three first volume moments are
J_x=(665+75t-10t^2)/48,
J_y=(525+10t)/24,
J_z=(5375-150t)/96.
These are genuine integrals, not adjustable vertex masses or the centroid of a polar body.

The exact verifier constructs a tetrahedral fan about c=(v0+...+v9)/10. The fan center c is an auxiliary integration point, not the centroid g. For every oriented boundary triangle(a,b,d), its positive volume is det(va-c,vb-c,vd-c)/6 and first moment is that volume times(c+va+vb+vd)/4. Summing gives the displayed V,J,g.

The verifier establishes150 continuous geometric positivity conditions:56strict support inequalities at nonincident vertices,68strict oriented in-facet edge-side inequalities,9cleared centroid-inside denominators,16positive tetrahedron volumes, and the positive total volume. Each degree-at-most-three polynomial is expressed in its complete cubic Bernstein basis on[0,1/2]. All600coefficients are nonnegative,594are positive and6are zero endpoint coefficients. Every one of the150vectors has a positive coefficient, hence every condition is STRICT on the open physical interval. Zero coefficients do not assert physical inclusion of t=0 or t=1/2: those endpoints are only algebraic limits where the facet lattice changes.

All declared incidences hold identically. The oriented in-facet edge-side inequalities say that each listed polygon is its actual strictly convex supporting polygon, not a self-intersecting cycle. Every listed edge occurs exactly twice with opposite orientations. These supporting polygons form the complete boundary: around every listed polygon edge the two incident supporting facets are already present; the connected facet-adjacency graph of the convex hull therefore cannot contain another facet adjacent to this nonempty closed collection. Every listed point is a strict corner of at least one supporting polygon and hence a true hull vertex. This proves completeness of the lattice, not merely consistency with a proposed subset of facets. Three rational controls also rediscover the entire hull independently from all vertex triples.

The degree argument behind interpolation is explicit. Vertices and c have degree<=1. A facet normal is the cross product of two edges. At most one of the three defining vertices varies, so its quadratic term cancels and each normal has degree<=1. Plane constants and all support polynomials have degree<=2. Edge-side expressions have degree<=3. Cleared centroid denominators8D*h-n.(8Dg) have degree<=3. Tetrahedron determinants have degree<=3 and first moments degree<=4. Five exact parameter values identify every degree<=4 polynomial; four identify the cubic exit matrices below. Exact interpolation is used to establish polynomial identities, NOT to infer positivity from samples. Positivity follows from the displayed complete Bernstein coefficient vectors.

### 2. Weak exit trees are necessary for U<=1

For actual centered vertices x_i=v_i-g and M>0 define a true weak exit i->j by
D_ij=x_i^T M(x_j-x_i)>=0,
where {i,j} is a TRUE polytope edge. A vertex is strictly unstable exactly when all of its true outgoing edge products are negative. This follows because its incident edge rays generate the tangent cone; negativity along all of them is equivalent to the supporting radial normal lying inside the vertex normal cone.

For every distinct pair,
2D_ij=||x_j||_M^2-||x_i||_M^2-||x_j-x_i||_M^2.
Thus even a ZERO weak exit strictly increases the M-norm. A global maximum-norm vertex is strictly unstable. If there were at most one strict U, there would consequently be exactly one, say root r. Every other vertex has at least one weak exit along a true edge. Choose one. No directed cycle is possible because the norm strictly increases on every chosen arrow; every path ends at r. The chosen9arrows form a rooted spanning tree of the actual17-edge graph. This implication remains valid on all weak VE/EF/VF walls and does not use dual stability or saddles.

### 3. A whole-SPD obstruction from a positive matrix combination

Set
W_i(t)=8D(t)(v_i(t)-g(t)),
A_ij(t)=-[W_i(t)(v_j-v_i)^T+(v_j-v_i)W_i(t)^T].
Every A_ij is a symmetric3x3 polynomial of degree<=3, because W_i has degree<=2 and the actual edge vector has degree<=1. For one common M,
tr(M A_ij)=-16D(t) D_ij.
In particular each weak exit requires tr(MA_ij)<=0.

A certificate row is a finite set of distinct-source true arrows with positive integer weights lambda_ij. It forms
K(t)=sum lambda_ij A_ij(t).
If K(t)>0, simultaneous weak exits for all arrows in that row are impossible: they would imply tr(MK)<=0, whereas M>0,K>0 imply tr(MK)>0. Crucially the SAME M multiplies every term. This retains precisely the common-metric compatibility that is lost when possible arrows are individually unioned over a metric cone.

Write K(t)=sum_{d=0}^3 K_d t^d. Its four cubic Bernstein coefficient matrices on0<=t<=1/2 are
C_k=sum_{d=0}^k [binom(k,d)/binom(3,d)] (1/2)^d K_d, k=0,1,2,3.
Then K(t)=sum_k binom(3,k)(2t)^k(1-2t)^(3-k) C_k. Positive definiteness of all four C_k proves K(t)>0 on the entire CLOSED algebraic interval, not just at the interpolation values.

### 4. Complete literal finite certificate

Part1 contains the complete171-row table inline. An item i:w means weight w on directed arrow i. The arrow order is the lexicographic ordering of the34ordered true edges generated by the exact facet cycles above. Each row has distinct arrow sources, all weights are positive integers1,2or3, and the entire table contains648weighted terms. Row-size distribution is89rows of3arrows,42of4,28of5,11of6,and1of7.

For each of171rows, every one of its4Bernstein matrices is exactly symmetric and positive definite by Sylvester's criterion. All684matrices and all2052positive leading principal minors are fully regenerated in the report. The smallest minor is3888; no floating-point tolerance participates in this check.

The graph enumeration takes every9-edge subset of the17trueedges: there are binom(17,9)=24310such subsets. A connected9-edge graph on10vertices is a tree. Exactly5299subsets are connected, and orienting each toward each of10roots gives52990distinct rooted trees. The exact verifier checks every such tree and finds at least one complete certificate row among its9arrows. It emits a full52990-line coverage file, recording the root, every parent and the first covering row. All171rows occur as first witnesses at least once. This is complete finite coverage, not a sample of rootings, an abstract-tree assertion, or a hash standing in place of the table.

Assume U<=1 for one t and one M. Section2 produces one of these52990rooted true trees. Section4 selects a contained certificate row; its K(t)>0 by Section3. All its chosen weak exits then contradict tr(MK)>0. Hence U_nd>=2 for every t and every SPD M. This completes the proof.

### 5. Genuine non-record controls preserved in the recovery

At t=1/4,V=1045/24,g=(1093/3344,211/418,2135/1672).
N=I,M=I gives S/U/H=9/9/16.
N=B0,M=B0^-1 with B0=((23,-13,-10),(-13,22,9),(-10,9,12)) gives6/7/11.
At t=1/128 these two metrics give8/10/16 and6/7/11.
At t=63/128 they give8/9/15 and6/7/11.
Every one of the six controls has all68true directed vertex/edge and facet/edge primitives nonzero, therefore no extra weak packets. The report retains each exact volume, centroid, mutually inverse metrics, equilibrium lists and zero list. These controls illustrate actual mechanics and endpoint behavior; they do not prove the continuous theorem and are not110examples. No claim that the lower U=2 is attained inside this metric subcollection is made.

### 6. Exact source-only recovery and dependencies

All source files are exact UTF-8 with LF newlines and a final newline. The accepted theorem and its complete full report/coverage require only TWO source units:

A. Existing immutable dependency cap_geometry.py, material [internal-source-reference],4942bytes,SHA256192e14a57e44b4f31d4b8af0039616fa4cf004af91322f214eef1472bfb71fb5. This file is complete standard-library rational hull, integration and mechanics code; it was read in full, not referred to as an inaccessible sandbox path.

B. This capsule part1, material [internal-source-reference], save as prismatoid_all_spd.py,12597bytes,SHA2563939c857ea7c43b42f0c8081989a7a2c38196a6300238ca89f6e4e23e6cba09a. All ten vertices, all nine facet cycles, the full171-row exact input checkpoint, geometry formulas, polynomial interpolation, positive-definiteness verification, complete graph enumeration, and actual controls are inline. There are no omitted helpers beyond complete dependencyA, no seed needed, no archive, no network access, and no generated-data input.

Pinned exact execution environment: CPython3.13.5 standard library only. Assertions must remain enabled; do not use -O. Reconstruction and verification commands are
python -S prismatoid_all_spd.py build > prismatoid_all_spd.stdout
python -S prismatoid_all_spd.py check > check.stdout

Expected generated files:
prismatoid_all_spd_report.json,412639bytes,SHA256dc1972da5fce0a201ce93ac464f5ded84641e37682e904424b4801ea8f14a80b.
prismatoid_all_spd_coverage.tsv,1336445bytes,SHA256fb7262df9d374cac79a8ebae0fefdfd2a75924608adea6d64954b195a28fa27b.
prismatoid_all_spd.stdout and check.stdout,each490bytes,SHA256de4dbce2b0b8817f1934f0d00c882b6934479270a77276d836f5bf06f1cb1f37.

Expected terminal markers:
ACTUAL_CONTINUOUS_10_17_9_GEOMETRY_AND_VOLUME_CENTROID_PASS 150 594 6
EXACT_ALL_52990_ROOTED_TREES_COVERED_BY_171_ROWS_PASS
ALL_684_BERNSTEIN_BLOCKS_2052_POSITIVE_MINORS_PASS 3888
ALL_SPD_M_PRISMATOID_U_AT_LEAST_TWO_FOR_ALL_T_PASS
PRISMATOID_ALL_SPD_U2_V1_SOURCE_ONLY_RECOVERY_PASS

A fresh empty directory was actually populated with only A and B; build and check succeeded with -S, and the complete report, complete coverage and stdout were byte-identical to the original. This is a source-only reproducibility statement, not a replacement for the proof in Sections1–4.

The original compact JSON spelling of the same final table can be regenerated directly from TABLE with json.dumps(TABLE,separators=(',',':'))+'\n'. It has4665bytes,SHA256bb30dbbc11f20bdd84554cd95f2dc214cb15528356d3d1c09e39e231155191ef. The inline table in part1, not that hash, is the exact recovery input.

### 7. Complete material discovery method and limits

Part2, material [internal-source-reference], save as joint_metric_probe.py,5348bytes,SHA2567b5b129920f772b1ff76de7e3bcefbfc6bcc27217b97e49a4de252eec4dcf0e4, is the complete exchange-LP discovery source. Part3, material [internal-source-reference], save as prune_joint.py,1753bytes,SHA256ac29b60083a266717c53e2b57bc497fc88a16d39826d38cec81ff07a5c5bb8aa, is the complete exact simplification/coverage-greedy source. They are preserved because they materially produced the finding, not because the accepted proof needs to rerun a floating solver.

Discovery also uses existing full spectral_family.py, material [internal-source-reference],7653bytes,SHA256b40afd68d9d17d73e78add8692a5b3b87828a7cda9b2579479b41b67c0119bfd, plus cap_geometry.py. Pinned versions: Python3.13.5,NumPy2.3.5,SciPy1.17.0,SymPy1.14.0. OPENBLAS_NUM_THREADS=1; no random seed is used. The precise substantive command was
OPENBLAS_NUM_THREADS=1 python joint_metric_probe.py --seconds 40 --limit 100000 --output joint_metric_complete.json
followed by
OPENBLAS_NUM_THREADS=1 python prune_joint.py > prune_joint.stdout.

The probe normalizes nonnegative row weights to sum1 and maximizes the common lower eigenvalue bound of all four Bernstein matrices. It starts from coordinate and pairwise signed directions and adds exact locations proposed by numerical minimum eigenvectors. Every proposed row must then pass Fraction rational reconstruction and exact positive leading minors. The run found540exact rows,0failed rooted cases,0unprocessedtrees; the exchange needed at most2iterations. The exact simplifier rounds relative weights on successively finer integer grids1..128, retains only exact-PD rows, deduplicates439candidates, then greedily covers all52990trees, producing the accepted171rows/648terms/maxweight3.

The earlier pilot limited to300solvercalls left8205unprocessed trees and was not a complete exclusion. Neither a failed LP nor failure of a particular Bernstein coefficient cone would prove geometric feasibility or infeasibility. A numeric discovery file contains measured wall-clock elapsed time and is therefore not asserted to reproduce byte-identically; it is not an accepted exact recovery input. The definitive input is the complete final table already inline in part1. The recovered mathematical object and proof do not depend on reproducing numerical solver choices, intermediate redundant540-row formatting, elapsed time or a local checkpoint.

Part4 is this full proof and manifest; its own immutable receipt identifies its exact bytes and SHA. All four capsule parts and both referenced immutable source dependencies are now preserved. For a worker studying only the accepted all-SPD theorem, attach A,part1,andpart4 explicitly; parts2/3 and spectral_family.py are necessary only when the worker is asked to use the discovery method or its exact exploratory implementation. The earlier ROOT_STAR full proof [internal-source-reference] may be attached as an independent mathematical dependency when its S-sector or root-cap conclusions are used.
