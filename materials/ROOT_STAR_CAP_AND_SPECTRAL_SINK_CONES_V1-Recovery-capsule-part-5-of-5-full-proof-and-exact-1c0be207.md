# material-1c0be207ab96

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ROOT_STAR_CAP_AND_SPECTRAL_SINK_CONES_V1
## Recovery capsule part 5 of 5: complete mathematical proof, actual controls, and reconstruction manifest

This completes the four immutable source units previously preserved under the same object identity. All four were read completely, recovered byte-for-byte, and executed in a clean source-only directory. The result is a new reusable geometric exclusion method and an actual continuous E17 family, NOT a 110 construction, NOT a universal exclusion of E17, and NOT a change to 34<=C_min<=622. No published-result novelty claim is made.

## 1. Common physical setting

Let P be a full-dimensional convex polytope, with an interior reference origin. Write its true maximal facets as q_i.x<=1. The polar vertices q_i have the true facet-adjacency graph of P. One physical positive definite metric pair is M and N=M^-1. A true facet i is strictly stable exactly when q_i^T N(q_j-q_i)<0 at all its true neighboring facets j. This is equivalent to the foot Nq_i/(q_i^TNq_i) lying in the relative interior of the true facet. The analogous true-vertex condition x_i^TM(x_j-x_i)<0 detects strict unstable equilibria. Auxiliary triangulation diagonals are never mechanical edges.

For any nonzero difference y-x and any positive definite H,
2 x^T H(y-x)=||y||_H^2-||x||_H^2-||y-x||_H^2.
Consequently a weak exit (left side nonnegative) strictly increases the norm even when its bilinear product is zero. In a finite closed set, a maximum-norm node has all internal exits strictly negative, including ties in norm. This elementary identity is the entire strictness mechanism below. None of the general lemmas falsely replaces the actual volume centroid by the centroid of a polar body.

## 2. Root-star parabolic cap

Let B be a strictly stable facet with pole q. For a point a of P define
Delta_B(a)=(2-q.a)^2-(q^TNq)(a^TMa).
For each true neighboring facet F of B it is sufficient to have one point a_F in F outside B with Delta_B(a_F)>0. The points may be selected actual vertices; a different good point may be used for every neighbor. Then P has at least two strict stable equilibria.

Proof. A weak dual exit from F, with pole u, to B would mean
u^TN(q-u)>=0,
or ||u-q/2||_N^2<=||q||_N^2/4.
The incidence u.a_F=1 gives
(u-q/2).a_F=1-q.a_F/2.
Since a_F is outside the supporting facet B but belongs to P, q.a_F<1, so this right side is positive. Cauchy-Schwarz in the mutually inverse metrics gives
(1-q.a_F/2)^2 <= ||u-q/2||_N^2 ||a_F||_M^2 <= ||q||_N^2||a_F||_M^2/4.
This contradicts Delta_B(a_F)>0. Thus every possible exit into B from a true neighbor is strictly prohibited. All facets except B form a nonempty closed set in the actual weak-exit graph. Choose a maximum N-norm pole in this set: its internal exits are strictly negative by the identity in Section1, and any exit to B is also strictly negative. It is another strict stable facet.

Non-strict version. Replacing all >0 by >=0 prohibits strictly positive exits into B. The same complement maximum is either strictly stable or has its sole possible zero exit into B. In the latter case the foot of its facet lies in the relative interior of its true edge shared with B: every other facet inequality is strict because every other dual neighbor lies in the complement and has a strictly negative exit. This is a genuine edge-facet weak contact, not merely an unselected determinant zero. Thus the non-strict root-star hypothesis gives either another strict S or an additional physical weak EF point. In particular it still excludes strict110weak000. The strict version needs no weak000 hypothesis.

This strengthens the sufficient all-outside-vertices cap condition: one does NOT need Delta>=0 for every vertex outside B. It is enough that the good points hit all true neighbors of B. A control below has a strictly bad outside vertex but satisfies every root-star incidence.

## 3. Exact metric-cone test for one directed exit

Fix a reference SPD matrix B0 and kappa>=1. Consider every SPD N with
cond(B0^(-1/2) N B0^(-1/2))<=kappa.
No eigenframe is fixed. Overall scaling of N does not affect any sign. For nonzero vectors u,v put
D=u^TB0v, R2=(u^TB0u)(v^TB0v), R=sqrt(R2).
Then a weak exit u^TNv>=0 is possible for at least one N in this closed cone if and only if
D>=0 OR (kappa+1)^2 D^2 <= (kappa-1)^2 R2.
All equalities must be retained as possible weak exits.

Proof. Let a=B0^(1/2)u and b=B0^(1/2)v. After positive scaling, the possible matrices A=B0^(-1/2)NB0^(-1/2) may be restricted to I<=A<=kappa I. The symmetric matrix K=(ab^T+ba^T)/2 has nonzero eigenvalues (D+R)/2 and (D-R)/2. The maximum of tr(AK) over this order interval is
[(kappa+1)D+(kappa-1)R]/2.
It is achieved by taking eigenvalue kappa on the positive eigenspace and 1 on the negative eigenspace. Parallel limiting cases are included; the maximum remains the stated expression. The maximum is nonnegative automatically when D>=0. For D<0, squaring its equivalent nonnegative-radical inequality gives precisely the second condition. This is an exact sharp test for a single arrow, not a sufficient numerical relaxation.

## 4. Closed collective sets and sink strongly connected components

For a fixed real geometry and metric cone, make a directed graph on the true polar vertices. Include a true directed edge whenever Section3 permits its weak exit. Each actual weak-exit graph for any one N is a subgraph of this possible-exit graph. If A_1,...,A_r are disjoint nonempty vertex sets with no possible outgoing edges, then every N in the cone gives at least r strict stable facets. Choose a maximum N-norm pole separately in each A_l and use Section1. Thus the number of sink strongly connected components of the possible-exit graph is a valid uniform lower bound for S. It is NOT asserted to be the optimal bound: different permitted edges can require mutually incompatible metrics, and taking their union forgets that additional information.

The theorem applies verbatim to the primal vertex graph, with M replacing N, and bounds U. The S and U applications must continue to use one mutually inverse pair; independent choices of their metrics do not describe one physical polytope. The collective theorem also explains why a family can force S>=2 without any single facet being uniformly stable: a sink component can contain several facets, with its maximizing pole changing as the common metric varies.

## 5. Exact non-affine actual family TWO_SINK_PRISMATOID_V1

For 0<t<1/2 set H=5/2 and take the convex hull of the following ten vertices, with these exact labels:
0=(-2,-2,0),1=(2,-2,0),2=(2,2,0),3=(-2,2,0),
4=(3,3,H),5=(-1,3,H),6=(-2,1,H),7=(-2+t,0,H),8=(-1,-1,H),9=(3,-1,H).
The true maximal oriented facet cycles are
F0=(0,3,2,1),F1=(0,1,9,8),F2=(0,6,3),F3=(0,7,6),F4=(0,8,7),
F5=(1,2,4,9),F6=(2,3,5,4),F7=(3,6,5),F8=(4,5,6,7,8,9).
They give V10/E17/F9. This is neither the earlier bevel object nor the two-apex roof8 object. The four lower and six upper vertices lie on two parallel planes.

The body is uniformly volume-filled. Its actual volume and centroid are
Vol=5(105-2t)/12,
g_x=(-2t^2+15t+133)/(4(105-2t)),
g_y=(2t+105)/(2(105-2t)),
g_z=5(215-6t)/(8(105-2t)).
The code proves this by a positive tetrahedral decomposition about the average of all ten vertices; that auxiliary decomposition point is NOT substituted for the actual centroid. It separately verifies all true support incidences, strict nonincidences, every oriented facet turn, all positive volume tetrahedra, and every actual centered pole denominator throughout the full open interval. Endpoint factors t and 1/2-t may be removed only from geometric conditions where a change of f-vector at an endpoint is explicitly allowed. No endpoint is included as a physical 10/17/9 body.

Let
B0=((23,-13,-10),(-13,22,9),(-10,9,12)).
It is exactly SPD by its three positive leading principal minors.
The following entire metric sectors are excluded from S1:
(a) reference I, kappa<=7: F0 and F8 are both uniformly strictly stable;
(b) reference B0, kappa<=4: the two disjoint sets {F0,F5} and {F6,F7,F8} have no possible outgoing arrows and hence force at least two strict S.
These are closed condition-number sectors, including arbitrary eigenframes. Both claims hold for every 0<t<1/2 at the actual volume centroid.

There are 23 outgoing cut arcs in total: ten for the two fixed singletons and thirteen for the moving components. For each arc the code certifies both -D>0 and (kappa+1)^2D^2-(kappa-1)^2R2>0. Together with all geometric guards this gives 162 exact rational positivity records and 894 strictly positive Bernstein coefficients. Every coefficient vector is complete, including the positive denominators. Coefficient positivity, not sampled t values, proves the continuous inequalities.

At t=1/4, the possible-exit graph for (B0,4) has exactly the sink components {0,5} and {6,7,8}, while EVERY one of the nine facets has at least one strictly possible outgoing arrow. Thus no facet can be singled out as uniformly stable in this cone, yet at least two stable facets are forced collectively. The exact possible arrows are
(0,5),(1,0),(1,5),(2,3),(2,7),(3,2),(3,8),(4,1),(4,3),(4,8),(5,0),(6,7),(6,8),(7,6),(7,8),(8,7).
All possible-arrow tests have a strict feasibility margin; none is admitted solely by equality.

## 6. Actual own-centroid non-record controls

At t=1/4,
Vol=1045/24,
g=(1093/3344,211/418,2135/1672).
With N=I and M=I the body has S=9,U=9,H=16. With N=B0 and M=B0^-1 it has S=6,U=7,H=11. All 68 true directed edge/dual-edge primitives are nonzero in both controls, so there are no additional weak VE/EF/VF packets. Complete equilibrium identities and lists are stored in the regenerated exact report. These controls are not 110 and do not improve the accepted attaining complexity.

For the identity control F0 is stable. The root cap values of all six vertices outside F0 are
Delta(4)=-962751/2604700,
Delta(5)=10695899/3646580,
Delta(6)=79502503/18232900,
Delta(7)=91706431/18232900,
Delta(8)=97780807/18232900,
Delta(9)=7512411/3646580.
The good vertices {5,6,7,8,9} hit every true facet neighbor of F0, despite vertex4 being strictly bad. Therefore the root-star version really applies beyond the all-vertex hypothesis, on an actual own-centroid E17 body.

## 7. Exact checker and proof scope

The builder uses SymPy only to expand and cancel exact rational polynomials. The verifier uses Python standard-library Fraction arithmetic and independently reconstructs the geometry and every relevant bilinear expression. It verifies the full Bernstein coefficient vectors and identifies each claimed polynomial identity by 65 exact distinct rational evaluations. This latter step is NOT a positivity sampling argument: coordinate degree<=1, plane degree<=1 for the literal family, volume degree<=3, first-moment degree<=4, pole numerator/denominator degrees<=4/5, cone-square degrees<=26/30, and reported polynomial degrees<=30 imply a cross-multiplied identity degree<=60; the conservative bound64 is used. Sixty-five roots prove that cross-multiplied polynomial is identically zero. The checker tests 162*65=10530 identities and proves each positive sign by the complete positive Bernstein representation over the whole interval.

The actual control hull is also independently discovered from all vertex triples with Fraction arithmetic, rather than accepting only the supplied facet list. The true maximal faces, true edges, volume integral, centered poles, equilibrium signs, root-star incidence hits, and closed components are all checked.

This does not claim that the two metric cones cover all SPD metrics, that the displayed graph describes every realization of its facet lattice, or that no prismatoid can be mono-monostatic. Those are distinct unresolved questions. The union-of-possible-arrows method can be strengthened by preserving simultaneous common-metric compatibility; no such stronger conclusion is assumed here.

## 8. Complete source recovery and immutable inputs

Read each source material in full and save its exact UTF-8 bytes under the following filename. All four have LF newlines and a final newline. No hidden inputs, local checkpoints, omitted tables, encoded archive, or network dependency is required.

Part1: cap_geometry.py, material [internal-source-reference], 4942bytes, SHA256192e14a57e44b4f31d4b8af0039616fa4cf004af91322f214eef1472bfb71fb5.
Part2: spectral_family.py, material [internal-source-reference], 7653bytes, SHA256b40afd68d9d17d73e78add8692a5b3b87828a7cda9b2579479b41b67c0119bfd.
Part3: verify_spectral.py, material [internal-source-reference], 6828bytes, SHA256cc1dc26521092a8a21771db30c58cff6903fa99c63fe4a949495ca8ae0bfc180.
Part4: cut_probe.py, material [internal-source-reference], 1356bytes, SHA25677caae5413c6a86e30ea4c66487c7cdebcd646fef0d3f4110d0961028e429cad.
Part5: this complete proof and recovery manifest; its immutable material receipt identifies its own exact bytes and hash. Part4 is the complete exploratory method, but is not needed to reconstruct or certify the accepted object because the exact B0 is already inline in parts2/3.

Pinned execution: CPython3.13.5, SymPy1.14.0. No NumPy/SciPy needed for this certificate. Assertions must be enabled; do not use -O. The builder needs normal site import for SymPy. The verifier and exploratory probe can run with -S.

Reconstruction:
python spectral_family.py build > build.stdout
Verification:
python -S verify_spectral.py > verify.stdout
Optional redundant symbolic reconstruction comparison:
python spectral_family.py check
Optional exact recovery of discovery search:
python -S cut_probe.py > probe.stdout

The complete exploratory method has seed918731, at most5000 trials, first15 diagonal references, then B0=I+XX^T with every X entry a uniformly chosen integer from[-4,4], and kappa scanned in exact order3/2,2,3,4. It deterministically finds the accepted reference at sample31 and kappa4. Failure of such a probe would not be a geometric exclusion; here the accepted continuous certificate is independent of repeating that search.

Expected regenerated outputs:
two_sink_report.json:110930bytes,SHA2568113c490bdeeaa62cbd041b0f65503e273609fe5b0e93d609f55509f2f36fb43.
build.stdout:393bytes,SHA2564ec4c5ed832238400b6378710a6678d71107821c681bd36be64ebbcea6f76ca0.
verify.stdout:321bytes,SHA256386dfb651b8f2a61e00cfeb256204e6d22833ea9758ab535e935edc6408d18b1.
probe.stdout:337bytes,SHA2566545c85e585257b61ff7cb06528e87c0924b41406bac1e90559f733f82483199.

Expected terminal markers:
TWO_SINK_PRISMATOID_V1_OK
certificates 162 positive_coefficients 894 outgoing_cut_arcs 23
GEOMETRIC_RATIONAL_IDENTITIES_DEGREE_64_PASS 10530
COMPLETE_POSITIVE_BERNSTEIN_VECTORS_PASS 162 894
ACTUAL_OWN_COM_10_17_9_AND_MOVING_SINK_MECHANICS_PASS
ROOT_STAR_CAP_PASSES_ALL_VERTEX_CAP_FAILS_PASS
TWO_SINK_PRISMATOID_V1_STDLIB_VERIFICATION_PASS 110930 8113c490bdeeaa62cbd041b0f65503e273609fe5b0e93d609f55509f2f36fb43

Source-only cold recovery was actually executed after deleting dependency on all generated data: only the complete source files were copied into a new empty directory; both exact generation and stdlib verification succeeded; the report, build stdout, and verification stdout were byte-identical. This execution supports the finite certificate; the continuous mathematical implication is Sections1–7, not the existence of download links or hashes.
