# figure-0414

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Raven 11 — complete fractional-transfer cone, exact complexity law, and a C328 basin-turnover control

Branch: `[internal-source-reference]`. No new own110 body is claimed. The inherited canonical C622 remains unchanged.

The substantive outputs are: a complete description of **all convex fixed-z chord translations** of this literal C306, modulo affine chord gauge; an **exact true-complex counting law** throughout that 64-dimensional fractional parameter space; a complete small-support stress-ray classification; a new nine-parameter, exactly mass-centered construction with **open maximal V117/E290/F175**; and an exact **V58/E164/F108 own121/weak000** nonwinner that exchanges the global radial root while retaining a deep secondary basin. The last object supplies a useful warning: improving even the true-edge angular bottleneck need not substantially reduce radial persistence.

## 1. Input authority and execution boundary

I read the entire 906-line attached journal, both five-hinge capsules, and the complete JSON coordinator payload, including its literal source units. The required IDs were `[internal-source-reference]`, `[internal-source-reference]`, and `[internal-source-reference]`. No additional archive, parent coordinate file, research connector, or journal mutation was used. There is no missing dependency for the results below.

The supplied five-hinge construction is a convex, actual-mass chart, not an equilibrium certificate; its stated open complex is V64/E180/F118. The supplied finite joint searches do not exclude that chart or more general fractional transfers. My new construction does not reinterpret those finite failures as a theorem. The old all-direction uniform-mixing exclusion is also left intact. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

The sole geometric input needed by the new capsule is the original `farthest_merged_G10000.json`, 2051 bytes, SHA-256 `89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e`. Its 53 integer points, grid10000, and 102 oriented triangles are included in full inside the recovery capsule. No C318 labels or C318 obstruction are transferred to it.

## 2. A complete fixed-projection parameterization, not another seven-block ansatz

Let the original body be `g(x,y) ≤ z ≤ f(x,y)` over its projection D. Here f is concave and g is convex. Consider any chord translation β for which both `f+β` is concave and `g+β` is convex. The new body has exactly the same fibre width `w=f−g`.

**Completeness theorem for this fixed z projection.** Every such β is a sum `β=u+l`, where u is continuous piecewise affine on the original upper triangulation and l is continuous piecewise affine on the original lower triangulation. Upper u transfers a fraction λ of the original upper curvature, and lower l transfers a fraction λ of the original lower curvature, with every fraction in [0,1]. The only ambiguity in the decomposition is an affine function moved between u and l.

The proof does not assume β is polyhedral. On an open overlap cell, f and g are affine. The two convexity requirements therefore make β both concave and convex there, hence affine. At a proper crossing of one upper and one lower edge, continuity says the two possible gradient jumps are multiples of their two independent edge normals. Going around the four cells shows that each jump coefficient is unchanged across the crossing. Thus jumps propagate along each entire original edge. Around an original upper interior vertex the lower function is locally affine, so the upper jumps close; the same holds with the roles reversed. Integrating these jumps gives u and l. The jump inequalities on either side give exactly `0≤λ≤1`.

The genericity needed here is checked exactly, not presumed: all 23,426 triples of the 53 projected input points are noncollinear. In particular, opposite-cap edges do not pass through a cap interior node or overlap an original crease. The original strict hull audit supplies the two embedded cap triangulations.

There is an especially useful **positive-stress formulation**. For an original interior cap edge e=ij, let w_e>0 be the magnitude of its original gradient-jump coefficient relative to a perpendicular to `p_j−p_i`. At each interior projected vertex i,

`Σ_(j:ij is a cap edge) w_ij λ_ij (p_j−p_i) = 0.`

These are two rational linear equations per interior vertex. Write them as `A λ=0`. Their complete exact data are reconstructed by `sparse_structure.py`.

| Cap | Nodes | Interior nodes | Interior edges | rank(A) | Fractional dimension |
|---|---:|---:|---:|---:|---:|
| Upper | 34 | 17 | 65 | 34 | 31 |
| Lower | 36 | 19 | 71 | 38 | 33 |

The checked ranks also prove sufficiency: the nodal-height-to-jump map has kernel consisting of the three affine functions, and its image has the same dimension as ker(A). Thus the feasible fraction sets are exactly `ker(A) ∩ [0,1]^E`, not merely necessary relaxations. The all-half vector is a relative-interior feasible point. After removing the constant chord translation and the two longitudinal affine shears, the complete space has **31+33=64 dimensions**.

Actual mass is not an extra nonlinear unknown in this chart. Volume and both horizontal first moments are unchanged, while

`ΔM_z = ∫_D w β`.

Subtracting `m(β)=(∫_D wβ)/V` from β fixes the original filled centroid. This follows directly from expanding `((f+β)^2−(g+β)^2)/2`; the β² terms cancel. The implementation separately verifies the full boundary-moment polynomial, including all cross terms.

**Scope:** this classifies all convex translations of the fixed original fibres in this projection. It does not classify arbitrary physical surgery, another projection, a changed width, or projective changes. Within this fixed-width problem, inserting an arbitrary new crease inside an old overlap cell is impossible: that cell must remain affine. Changing width or projection genuinely escapes this restriction.

## 3. Exact true V/E/F throughout the full fractional space

Let I be the number of original interior cap edges whose fractions are strictly between 0 and 1. Let J be the number of original cap interior nodes at which the incident fractions are neither all0 nor all1. For each of the 201 proper upper/lower edge crossings, with upper fraction a and lower fraction b, count

`1[a<1 and b>0] + 1[a>0 and b<1]`.

Let X be the sum of these counts. Then the **actual maximal complex**, including endpoint strata, satisfies

`V = 53 + J + X`,

`E = 153 + I + 2X`,

`F = 102 + I − J + X`.

To prove the edge formula, each original interior crease appears on one cap at an endpoint fraction and on both caps at a strictly fractional value. The 17 silhouette edges persist. A surviving proper crossing splits two edges on its cap, adding two edges. For vertices, a cap interior node has one surviving lift when all its fractions are0 or all1, and two lifts otherwise. A nonzero convex stress cannot have an interior node of degree one or two under the verified noncollinearity condition. Thus no counted branch is a disguised straight subdivision. Each surviving crossing contributes one additional vertex. Euler gives the face formula.

Consequently the exact edge-budget condition on **all** feasible fixed-z fractional fields is

`E≤310  ⇔  I+2X≤157`.

This is stronger and more broadly applicable than the old seven-block crossing filter, while remaining explicitly projection-specific. It is invariant under subsequent nonsingular affine maps. At all fractions1/2, the formula gives **V491/E1093/F604**: 136 fractional edges, 36 mixed interior nodes and 402 crossing vertices. The two caps have precisely twice the 302 original overlay cells.

These formulas turn sparse architecture selection into an exact stress-feasibility/crease-status problem. Tiny nonzero curvature still pays its full topological cost; setting a fraction exactly0 or1 can remove true features.

## 4. Complete small-support classification reveals two missed upper alternatives

The stress cone is pointed after affine gauge removal. A non-bridge extreme ray has a connected interior support and at least three boundary anchors. Every interior support node has degree at least three. With m support edges and n interior support nodes, extremality requires `m≤2n+1`; otherwise the equilibrium matrix leaves at least two independent supported directions and the positive ray splits.

For m≤6 this leaves only three possibilities: a three-spoke Y; two interior Y nodes joined by an edge, with five edges total; or an interior triangle with one boundary spoke at each node, with six edges total. A four-edge extreme ray is impossible. These observations make the following finite exact screen exhaustive, rather than a random sample.

| Cap | Y3 tested/positive | Double-Y5 tested/positive | Triangle6 tested/positive |
|---|---:|---:|---:|
| Upper | 6 / 0 | 49 / 2 | 81 / 0 |
| Lower | 17 / 5 | 132 / 6 | 132 / 0 |

All **417** cases were checked with rational nullspaces, and every nominated nullspace had dimension at most one. There are therefore 13 non-bridge rays with support≤6, plus the five previously known bridge rays. All their complete rational fractions are generated in `SPARSE_STRUCTURE.json`.

In particular, an upper deformation involving its interior nodes needs at least **five**, not seven, original upper edges. The two minimal upper supports are

`[(14,27),(27,30),(27,47),(28,30),(30,47)]`,

`[(17,27),(27,30),(27,47),(28,30),(30,47)]`.

Their single-ray open complexes are respectively **77/202/127** and **79/206/129**. This is a constructive result: the exact screen overturned a preliminary guess based on sampled, larger upper rays. The separately retained seven-edge upper ray is not called minimal.

For the lower Y at vertex3, the support and normalized fractions are

`(0,3): 98181228995894268/247735201406058937`,

`(3,6): 16194711118692/975411707059753`,

`(3,12): 1`.

This nonuniform field acts on only three edges of the old large lower block, leaving its other edges at0. It is therefore genuinely outside the old seven-block cube, without contradicting that cube's previously stated scope.

## 5. New nine-parameter exact physical construction below the edge budget

Use the following nine normalized stress-ray fields, in this order. Each field is uniquely reconstructed by zero jumps off its listed support, three fixed cap gauge values, a one-dimensional rational nullspace, positive orientation, and normalization of its maximum fraction to1.

| Parameter | Cap | Complete active support |
|---|---|---|
| t0 | Upper | (1,14) |
| t1 | Upper | (2,14) |
| t2 | Upper | (28,47) |
| t3 | Upper | (47,52) |
| t4 | Lower | (1,4) |
| t5 | Lower | (0,3), (3,6), (3,12) |
| t6 | Lower | (36,48), (47,48), (48,50) |
| t7 | Upper | (14,27), (27,30), (27,47), (28,30), (30,47) |
| t8 | Upper | (17,27), (27,30), (27,47), (28,30), (30,47) |

The domain is `[0,1]^7 × {(t7,t8):t7≥0,t8≥0,t7+t8≤1}`. The last two fields overlap, so treating all nine controls as an unrestricted cube would be wrong. Their simplex constraint protects the shared curvature capacity.

The generator clips the original caps on their complete rational overlay, merges cells with identical affine-in-parameter plane coefficients, removes straight subdivisions, and reconstructs oriented maximal face cycles. It verifies all support inequalities over the entire product domain. For an affine slack with coefficients c0 through c9, its domain minimum is

`c0 + Σ_(k=0..6) min(0,c_(k+1)) + min(0,c8,c9)`.

Every nonincident slack is strictly positive at the interior sample having its first seven parameters1/2 and its last two parameters1/3. The full polynomial filled volume and centroid are verified before and after mean compensation and shear gauge.

The actual open complex is **V117/E290/F175, C580**. It has 17 fractional edges, four mixed interior nodes and 60 crossing vertices. Every closed-domain boundary body has no more than290 true edges. The separate eight-dimensional faces t8=0 and t7=0 have open counts **102/259/159** and **104/263/161**, respectively. They are family strata, not asserted equilibrium classes.

The physical volume throughout is

`1690203202641 / 10^12`.

The physical centroid throughout is the original C306 centroid

`(409355912737/135216256211280000, 855529297349/67608128105640000, 5154137003/270432512422560)`.

The chosen gauge rounds only two **affine shear coefficients per mode** to denominator2^20. It does not round vertices independently. This preserves the exact solid's volume, centroid, incidence and full affine orbit. The dyadic-gauge interior midpoint has full exact census **strict(13,3,14), weak000**, not110, and a1369-bit common centered physical denominator. Its distinct full-regression-gauge counterpart has the same census and3691 bits. Both are preserved by deterministic reconstruction; the latter is not silently identified with the former.

## 6. A small exact own121 nonwinner and a rigorous whole-basin comparison

The most useful individual body is **C328_Y3_ROOT_TURNOVER**. It uses only the lower Y3 field, its independently reconstructed denominator2^20 shear gauge, and

`t = 113170867807 / 250000000000`.

After evaluating this mean-compensated body, subtract its actual centroid and multiply row vectors by the following exact determinant-one matrix. With `d=10^12`, `a=999952695120`, `b=1002932507713`,

`L = [[a/d, 0, 0], [492893306/d, b/d, 0], [-2787871571/d, 11303394998/d, d^2/(a*b)]]`.

No exponential or optimizer output is part of this exact definition. Those rational constants, the literal original input and the supplied generator reconstruct every coordinate.

The complete audit gives:

**V58/E164/F108, C328; strict(S,U,H)=(1,2,1); weak-only000; exact physical centroid0; volume1690203202641/10^12; common centered physical denominator351 bits.** There are104 triangular maximal faces and four quadrilaterals. The112 positive centered integration tetrahedra are not112 maximal faces.

In its own generated ordering, the stable face is0, the unstable vertices are3 and19, and the saddle edge is30–32. Original C306 vertex0 maps to3; original vertex14 maps to19. The global radial root changes from original0 to original14, but both remain unstable. This is root turnover, not cancellation.

Both physical and same-center polar landscapes were audited. For a strict nonroot radial peak of squared radius B, let h be its exact maximin true-edge merge level, using the minimum squared distance along every complete edge. The reported radial depth is `(B−h)/B`. Edge paths capture the surface superlevel components because, on each convex planar face, the complement of a centered-distance disk connects the corresponding outside boundary arcs. The implementation supplies an attaining path and a separating cut at every nonroot peak, on both sides.

| Quantity | Original C306 | Exact C328 control |
|---|---:|---:|
| Physical true-edge cosine bottleneck, ×10^9 | between −699336298 and −699336297 | between −562723922 and −562723921 |
| Polar true-edge cosine bottleneck, ×10^9 | between449375 and449376 | between99 and100 |
| Secondary radial relative depth, ×10^9 | between761482576 and761482577 | between761330948 and761330949 |

These are rational path/cut bounds, not rounded optimizer claims. For a directed edge, the normalized score is `A/sqrt(B)` with integer A and positive integer B. Threshold comparisons use signs and cross-multiplied squares; root reachability certifies the lower endpoint, and an unreachable cut certifies the upper endpoint.

For C328, the secondary physical peak is vertex3, the global root is19, and one attaining edge path is

`[3,2,23,16,30,32,44,19]`.

The separating superlevel cut is

`[1,2,3,4,5,6,8,13,16,18,20,21,22,23,24,25,26,27,29,30,38,40,47]`.

The polar has no nonroot peak and has a completely positive exact true-edge escape tree.

Thus the magnitude of the angular bottleneck improves by more than19.5%, while the secondary **relative radial depth improves by less than0.020%** and remains above0.76133. The positive polar reserve also becomes much smaller. This is a concrete demonstration that even an improved negative **true-edge** angular objective is not, by itself, substantial radial-basin removal. It is not a theorem that angular objectives can never help.

The exact audit reconstructs supporting planes from rational coordinates, checks strict off-face support, true two-face edges, every vertex link, Euler, positive centered tetrahedra and zero centered first moments, then checks every face, vertex and mixed edge-cone predicate. C328's census was additionally reproduced by the separate Fraction implementation. The tetrahedron strict446/weak000 control and the triangular-prism strict446/weak123 control pass; reversed orientation is rejected. No claim of primitive-zero000 or of a new winner's independent three-way acceptance is made.

## 7. Finite experiments, other retained bodies, and the surviving frontier

The standalone numerical source preserves16 one-Y/five-affine SLSQP trials, seed19092682, maxiter300, ftol1e-11, positive polar floor1e-7, and all bounds and initializations. No numerical SU11 occurred. Some endpoints violate the requested constraints; their violations remain in the regenerated output. Selected trial9 has independently retested positive feasibility before rational freezing. Its initial control was `(0.9257568095147384,0,0,0,0,0)` and its numerical endpoint was `(0.4526834712282221,−4.7305999315856676e-5,0.002928216299799105,0.0004928933062023199,−0.0027878715711961715,0.011303394998479521)`. The last epigraph coordinate in the full numerical record is not a shape parameter.

The exact body does not depend on reproducing that optimization. The numerical clean replay nevertheless regenerated all7804 bytes of `ONE_Y_SEARCH.json`, SHA-256 `5f47dbdfb39d74f96b7f782a7a51e635673075aea051c308c269f5fd3132b533`.

The extended exact replay also preserves the earlier seven-field family with open78/210/134 and its midpoint strict(14,3,15)/weak000, all its named one-field boundary examples, and two direction-dependent Y14 families in the rational chart `X=x+z/10, Y=y−z`. Their supports are respectively `{1–14,4–14,14–24}` and `{1–14,14–24,14–27}`. After mapping back to physical coordinates, their half-parameter bodies have **71/190/121, strict(5,2,5)** and **66/180/116, strict(7,2,7)**; both are weak000 and retain the original actual volume and centroid. At parameter1 they have **71/189/120, strict(12,2,12)** and **66/179/115, strict(13,3,14)**, again weak000. These are meaningful nonwinning constructions, not aliases of the fixed-z bodies. Their complete source, gauges, parameters and reconstruction are included in `--extended-only`.

No exclusion of the nine-field family, the complete64-dimensional fractional family, their full affine orbits, or other projections follows from the finite searches. The useful continuation is now more specific: use the exact stress equations and `I+2X≤157` to choose low-cost supports, including the two upper five-edge alternatives; permit exact endpoint/contact changes; and assess both radial peak-to-merge persistence and the complete polar escape reserve at the actual centroid. The C328 control should prevent accepting another angular-score/root-turnover improvement as basin annihilation. To introduce genuinely new creases beyond this complete fixed-z space, change projection or release the preserved width rather than merely subdividing an affine overlay cell.

## 8. Self-contained recovery and actual verification

The following decoder contains the **complete literal input and all five runnable source units**, plus the exact expected-output manifest. Nothing inside it refers to an unavailable parent file or requires downloading an output. The compressed representation is only packaging; decoding writes the full readable generator, stress classifier, integer auditor, exact replay driver and numerical replay source.

Executed exact environment: **CPython3.13.5, standard library, assertions enabled**. Numerical replay additionally used **NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1**. All principal exact audit outputs contain integer/rational data, not floating diagnostics.

Save the decoder below as `RECOVER_QR11.py`, then run:

    python -B -S RECOVER_QR11.py
    cd QR11_SOURCE
    python -B -S REPLAY_QR11.py --verify-manifest

Actually observed from a new decoded directory:

    QR11_COMPLETE_SOURCE_RECOVERY_PASS 7
    C306_FIXED_Z_DIM64_EXACT_COST_AND_MIN_UPPER5_PASS
    QR11_TETRA446_PRISM446_WEAK123_REVERSE_REJECTION_PASS
    QR11_EXACT_DIM64_COST_MIN_UPPER5_C328_OWN121_C580_FAMILY_PASS
    QR11_EXACT_OUTPUT_HASH_REPLAY_PASS 8

Optional, also executed:

    OPENBLAS_NUM_THREADS=1 python one_y_replay.py
    python -B -S REPLAY_QR11.py --extended-only

The second command completed with `QR11_EXTENDED_EXACT_NONWINNERS_RECOVERED`. An earlier slow extended Fraction-census attempt timed out; the final integer-scaled audit completed without changing those geometries or census results.

The base64 capsule contains18952 characters, SHA-256 `d689ad70d3c0e976ceca583f55ec9cebd31ed613d86b81372e63c3f0972b1cfc`; it decodes to14212 XZ bytes, SHA-256 `cffa13591fb1c5cebe02c9cb3f939dc89c82f2777b935b732afc4791b62c06cd`, then40001 JSON bytes, SHA-256 `c8d3c3acc4b88695c0f3b1b51937733a44a5766eea4c712a0667518d16c558fb`. Each of the seven recovered files has its own checked byte count and SHA-256 inside the capsule.

```python
# Complete QR11 source/input recovery; standard library only.
import base64,hashlib,json,lzma,pathlib,sys
DATA='''
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
'''
s=''.join(DATA.split());assert len(s)==18952 and hashlib.sha256(s.encode()).hexdigest()=='d689ad70d3c0e976ceca583f55ec9cebd31ed613d86b81372e63c3f0972b1cfc'
b=base64.b64decode(s,validate=True);assert len(b)==14212 and hashlib.sha256(b).hexdigest()=='cffa13591fb1c5cebe02c9cb3f939dc89c82f2777b935b732afc4791b62c06cd'
b=lzma.decompress(b);assert len(b)==40001 and hashlib.sha256(b).hexdigest()=='c8d3c3acc4b88695c0f3b1b51937733a44a5766eea4c712a0667518d16c558fb'
z=json.loads(b);assert z['version']==1 and len(z['files'])==7
r=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'QR11_SOURCE');r.mkdir(parents=True,exist_ok=True)
for n,t in z['files'].items():
 assert pathlib.Path(n).name==n and n not in ['', '.', '..']
 b=t.encode();m=z['manifest'][n];assert len(b)==m['bytes'] and hashlib.sha256(b).hexdigest()==m['sha256']
 p=r/n;p.write_bytes(b);assert p.read_bytes()==b
print('QR11_COMPLETE_SOURCE_RECOVERY_PASS',len(z['files']))
```

### Exact principal output identities

| File | UTF-8 bytes | SHA-256 |
|---|---:|---|
| `SPARSE_STRUCTURE.json` | 5488 | `d1cb23a2400d868bc6451fa593d67fa4d1a03f4871cf73984c2135438dbac207` |
| `Y3_D20_FAMILY.json` | 10540 | `acd48c56ae15166101355948fefc0f2cdc3a9e9d14fbaf6748913bc92ab54a5b` |
| `C328_Y3_ROOT_TURNOVER_EXACT.json` | 29656 | `bc736d79a3a3625839e5bb97ce36298262a00768380d28d61e941a6bad3682b8` |
| `C328_Y3_ROOT_TURNOVER_AUDIT.json` | 1451 | `47056a1f284ec4de3b2e11c558b4da33a1571f63400dad8c743e3efad33d70fd` |
| `C306_BASELINE_BASIN_AUDIT.json` | 1422 | `849b17151b3082fdb86997ec94957e836b9a9efab96a3d54fbccf1bd2e1dae3d` |
| `Y9_D20_FAMILY.json` | 192269 | `0ca9ec96f90fb7fd6ec99aa9d1d92f82ec521d884bd0748537b1b70f2d8de08b` |
| `Y9_D20_MID_EXACT.json` | 99938 | `d9121b14fe02e809009e871044443153dae5066df41fd1fe2070421736fb38a3` |
| `Y9_D20_MID_AUDIT.json` | 4423 | `8c31c5cb1415fd6567848c3483a3a3279ed95bec2ba7225732c9523983cd6ba7` |

Supplemental copies of the readable sources, all principal and extended exact objects, manifests and executed replay logs are in the [proof/source archive](sandbox:/mnt/data/QR11_FRACTIONAL_HANDOFF.zip) (1149011 bytes; SHA-256 `2119e1fdf1b09a8c00073f13ece90916377a13998249140303849992758f2cb9`). This archive is optional: the complete reconstruction input and source are embedded above.

**Acceptance boundary:** a new 64-dimensional exact parameterization, exact complexity law, complete support-six screen, and a C580 family are established; C328 is an exact own121/weak000 nonwinner. No own110 successor or exclusion of the surviving constructive families is claimed.
