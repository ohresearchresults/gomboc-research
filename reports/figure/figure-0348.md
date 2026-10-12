# figure-0348

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Steady Lynx 57 — C698 certified; length-free escape derivatives and exact sparse nonwinners

## 1. Result and acceptance boundary

**The smallest new promoted body is `LYNX2_C698_AREA_D1E9`: 218 vertices, 349 true edges, 133 maximal facets, C=698, strict own-centroid (S,U,H)=(1,1,0), weak (0,0,0).** Two independently implemented exhaustive exact auditors completed and produced identical complete reports. A fresh directory decoded from the literal capsule below completed the entire source-only replay, including all-feature negative controls and two independently triangulated translated-volume integrations. A separate source-only execution reconstructed the same exact body by rounding its frozen winning float.hex checkpoint and reproduced all eight output files byte-for-byte.

**C<500 was not reached.** This is 27 fewer true edges than the distinct lead C752, a 7.180851% reduction, and 62 fewer than LYNX139. It remains 100 true edges above E=249. The improvement over the lead is modest; the additional constructive contribution is a better-conditioned, actual-centroid differential and a new latent-plane realization with exact nonwinners at C592 and C534. Neither nonwinner is promoted as a Gömböc.

| Capsule case | Exact body | Actual V/E/F | C | Strict own S/U/H | Weak |
|---|---|---:|---:|---:|---:|
| `winner` | LYNX2_C698_AREA_D1E9 | 218/349/133 | 698 | 1/1/0 | 0/0/0 |
| `before` | LYNX2_C808_BLOCK_BEFORE_D1E10 | 267/404/139 | 808 | 1/1/0 | 0/0/0 |
| `latent_parent` | LYNX2_C702_AREA_D1E9 | 219/351/134 | 702 | 1/1/0 | 0/0/0 |
| `cut` | LYNX2_CUT_EXACT_NONWINNER | 243/368/127 | 736 | 40/48/86 | 0/0/0 |
| `latent80` | LYNX2_LATENT80_EXACT_NONWINNER | 159/296/139 | 592 | 8/2/8 | 0/0/0 |
| `latent100` | LYNX2_LATENT100_EXACT_NONWINNER | 176/267/93 | 534 | 9/6/13 | 0/0/0 |

Every row has a complete exact defining generator, two completed exhaustive exact audits, and an observed source-only replay in this handoff's capsule. The three negative rows remain negative even after exact translation to their own volume centres.

## 2. Parent authority and actual lineages

I read the attached journal and both literal parent payloads. The assignment metadata identifies `figure-0344` by SHA-256 `ad404dda4981131e5fe60474cc5ddcae4b8ac886e92812f584dbb987ff3e0a05`, and `figure-0345` by `122a1859f8d9d0f582b8ea5f563d7c54b9dfeb8f708a3ee98a53923a171b35fc`. Those are the supplied parent commitments; the independently checked byte commitments are their decoded source capsules. LYNX139 is the distinct simple C990-derived 274/411/139 body, not C752 or the contact-chart C792. The journal explicitly preserves these distinctions.

The LYNX139 exact capsule decoded to 62645 bytes, SHA-256 `75ca8f054440016f02d26c509c3a362483f8c22fc7a4a5339faf2a400ea3035e`; its recovered sources agreed with the attached C822 archive. The QR29 capsule decoded to 48909 bytes, SHA-256 `23f037949be6b1bcb90d920606a2a72722ff56e86a29494d33c0268911ca9139`. I actually executed the QR29 original replay: its A/B reports reproduced the prescribed SHA `1bf1b155dba32adda76005922408b6b5bb13a94b710d980e147845285d430371` and terminal pass. Its transferable-coordinate-ownership mechanism is used as source evidence, not as instructions or as C698's geometry.

I separately recovered the lead C752 literal RAW.json, SHA-256 `1353da92125392ca69c92fb1c695187a9e98bd8791c8dd3c2eb7c056dbfdeccf`. Its stable normal is (360260,2906302,846940), D=1000000. Fresh A/B replays of C752 and LYNX139 agreed, and their exact escape graphs were rebuilt. No semantic conflict in the two named parent payloads was found. No apex ID, cycle, or row number was borrowed across bodies.

There are two actual constructive branches: the LYNX139 global-block branch gives `before` and its literal twelve-support `cut`; the C752 whole-body area/rank branch gives C702 and C698. The two latent nonwinners use the separately preserved C702 checkpoint. Each new exact body below is independently reconstructible without either parent archive or journal.

## 3. Complete exact definition of C698

`proof/GENERATOR.json` contains all **134 integer control triples**, grid D=1000000000, the following 44 root rows, and three coplanarity records. Its 5034 source bytes have SHA-256 `7fef3c0c801b3f6fff60a5093c970489a8e8ce86bf54e8aeae55bb3cd7110e26`. The complete table is inside the inline capsule, not just at a file link.

First divide controls by D. Set q_i,z=1 for these exact row indices:

```text
0,1,2,4,5,7,9,10,11,21,22,23,24,25,26,28,29,30,31,32,33,34,
35,36,39,40,41,42,43,60,61,62,65,66,69,70,96,97,98,99,130,131,132,133
```

Evaluate the following records in sorted-ready topological order, with exact rational arithmetic:

```text
dep=46, anchors=[27,48,78], axis=0
dep=40, anchors=[27,39,79], axis=1
dep=133, anchors=[11,79,80], axis=1
```

For record `(i,[a,b,c],k)`, let n=(q_b-q_a)×(q_c-q_a), then replace

`q_i[k] = (n·q_a - sum(n[j]*q_i[j] for j!=k))/n[k]`.

The included recoverer verifies a nonzero denominator and evaluates the acyclic dependencies deterministically. Convert each q_i to primitive integer `(N_i,h_i)` with q_i=N_i/h_i and h_i>0. Define

**P0={x:N_i·x<=h_i for all 134 inputs}, filled uniformly with density one; P=P0-g(P0).**

The resulting exact RAW.json is SHA-256 `181fac70d9bdffc779a205a0f91bbb4c206238de9edd1ecf854cf5c89072c163`. Input row **57 is redundant**. The remaining **133 maximal physical facets** and **349 true edges** are recovered from the complete inequalities, not imposed from a floating triangulation.

### Exact mass specification

Both auditors enumerate the exact raw vertices X and every outward maximal polygon. Fan each polygon from its first vertex, producing the explicitly reconstructible finite triangle list T. Set

`W = sum(det(X[a],X[b],X[c]) for (a,b,c) in T)`

`L = sum(det(X[a],X[b],X[c])*(X[a]+X[b]+X[c]) for (a,b,c) in T)`.

Then the exact rational quantities are **V0=W/6, M0=L/24, g0=L/(4W)**. These formulas, the complete literal input and the two complete finite evaluators are an exact arithmetic-circuit definition of every mass datum. The reports emit the expanded reduced numerators and denominators as `ordinary_volume`, `raw_first_moments`, and `raw_centroid`; none is an unspecified fitting constant. Expanded volume alone has thousands of digits, so the reconstruction circuit is materially shorter than printing that fraction.

Readable decimal displays of these exact rationals are:

```text
V0 = 0.4753425251114912
M0 = (-0.002241757217452622,
       0.011753406604223516,
      -0.0003890325114754747)
g0 = (-0.004716088081803368,
       0.024726183716608913,
      -0.0008184256424022392)
```

For P, **V=V0, Mx=My=Mz=0 exactly, g=(0,0,0) exactly**. The raw centre is appreciably nonzero and was never rounded away. Mechanical classification uses this genuine rational volume centre. Two separately chosen translated fans additionally reintegrate the zero first moments, rather than relying only on writing M-Vg=0.

### Maximal incidence and exhaustive critical features

The degree histogram is **214 degree-three vertices, three degree-four vertices, one degree-44 vertex**. Degree excess is 44. The maximal facet-size histogram is

`[(3,43),(4,30),(5,22),(6,13),(7,6),(8,6),(9,3),(10,1),(11,4),(12,1),(14,2),(25,2)]`.

The **432 integration triangles are not additional mechanical faces**. Their diagonals do not reduce or increase the true E=349 used here.

The sole stable facet is input **3**, outward normal **(263881428,2921745097,854233966)**, raw offset **1000000000**. Its centred offset is exactly h-N·g0. In the auditors' common lexicographically sorted exact vertex ordering, its complete 25-cycle is

```text
[64,115,192,194,197,200,203,205,206,209,202,201,189,188,187,
156,148,143,136,135,130,119,98,86,85]
```

The sole unstable vertex is **105**, raw coordinate **(0,0,1)**, centred coordinate **(-g0x,-g0y,1-g0z)**. Its complete 44-row contact set is exactly the root list above. All other vertices, including the three nonsimple degree-four vertices, are tested with their full incident cones. There are **no saddle edges, no weak faces, no weak vertices, and no weak edges**. Every one of the **1396=4E edge primitives is nonzero**; face-side primitive zero count and vertex maximum-escape zero count are also zero. All remaining coordinates, cycles, contacts and signs are exhaustively reconstructed in A.json and independently in B.json.

## 4. Independent exact proof and observed replay

Auditor A enumerates every independent input support triple with integer Cramer determinants and all-halfspace feasibility. Six nonnegative normal-cone representations of the signed coordinate axes certify boundedness; positive offsets put the origin strictly inside. It reconstructs maximal polygons with exact projected convex hulls, verifies the closed oriented complex, integrates origin-based first-vertex fans, and tests every physical vertex against every other vertex.

Auditor B independently clips every support-pair intersection line against all inequalities, recovers its endpoints and true edges, and independently orders maximal polygons by supporting lines. It integrates different fans from a different strictly interior point. Adjacency-based full-cone classification is checked against all-vertex escape classification. B does not import A.

For each centred true edge a--b, write e=b-a, t=-a·e/(e·e), p=a+t e. For its two outward normals n,m, write p=alpha*n+beta*m. A strict saddle requires **t>0, 1-t>0, alpha>0, beta>0 simultaneously**. A forms the Gram coefficients; B independently forms the cross-product coefficients. Both evaluate all four predicates on every actual edge and also test every all-nonnegative weak case. Absence of saddles is not inferred from Euler or an escape merit.

Both programs explicitly recover maximal exposure, finite positive ordinary volume, every face-side condition, complete vertex cones, and all strict/weak edge cases. They agree on every complete report field. Identical A/B hashes reflect the common canonical output schema, not a shared geometric implementation.

The replay additionally runs regular tetrahedron, cube, octahedron, weak-equilibrium tetrahedron, and translated-box controls through both auditors. The box has exact V=18, M=(9,-9,0), g=(1/2,-1/2,0). Six malformed/duplicate/zero-height/unbounded input tests are rejected. Two translated fan integrations check covariance and reject four malformed fans in total.

Actual C698 source-only output bindings:

| File | Bytes | SHA-256 |
|---|---:|---|
| A.json | 199148 | `2e63b0f7bfa599c278495c01a68d4b141aa4787aeffb7d34019f3055b7fd0f1d` |
| B.json | 199148 | `2e63b0f7bfa599c278495c01a68d4b141aa4787aeffb7d34019f3055b7fd0f1d` |
| EXTRA.json | 213177 | `a16c38bc6706c26ccc0d91bd3caa57884ef79bcffb30b12e7607f4e467c65204` |
| CONTROLS.json | 896 | `6c32a17aea063bfb45de36cc03d427e9c27e3b00473c40c3f2a66e9289f594be` |
| TRANSLATED_MASS.json | 21749 | `20ebf455ff307b770b1b3f436f39c3a08721ab7167b6c6006b0ebeef1da26d68` |
| PATHS.json | 13169 | `13da408279aedad58a20a86a8db40c85f8b8ac6f39974e4e4e888401d4c16bc5` |
| SUMMARY.json | 1695 | `25b26025dc1c79bc1c822073c8a65298e408d344326158f572759c42a1e873c3` |

Observed terminal marker:

`LYNX2_C698_AREA_D1E9_TWO_EXACT_AUDITS_TRANSLATED_MASS_AND_ALL_FEATURE_CONTROLS_PASS`.

The final capsule was actually decoded into an empty directory, and all 60 recovered source/data files were compared with the committed source mapping. All six case replays completed from source-only case directories. The winning frozen float.hex checkpoint was separately rounded by exact Fraction/ties-to-even arithmetic, rebuilt and audited from another fresh directory; its RAW, A, B, EXTRA, CONTROLS, TRANSLATED_MASS, PATHS and SUMMARY were byte-identical to the earlier completed C698 cold run. The final baseline replays likewise completed. These are executed software-independent checks within this research, not independent human peer review, proof-assistant formalization, manufacturing tolerances, or minimality evidence.

## 5. New constructive differential: remove short-edge division, not actual mass

The parent normalized escape is `(p_i·(p_j-p_i))/(||p_i|| ||p_j-p_i||)`. It improved earlier search conditioning but differentiating through a near-collapsing endpoint difference still introduces a badly scaled representation.

For an actual physical edge with incident outward support vectors q_a,q_b, use its oriented unit direction

`t_ij = sigma*(q_a×q_b)/||q_a×q_b||`,

where sigma points from X_i to X_j. Then use

`a_ij = (X_i-g)·t_ij/||X_i-g||`.

This is exactly the same value as the normalized chord escape, but its first derivative avoids division by the shrinking edge length. It does not eliminate the separate problems of nearly parallel face normals, singular latent triples, or contact changes; those still require actual re-hulling and rank checks.

The second improvement is an actual filled-volume centroid derivative that does not differentiate a fragile vertex-triangulation graph. For physical facet F_i in plane q_i·x=1, define

`m_i=integral_Fi x dA`, `T_i=integral_Fi x*x^T dA`.

Normal boundary velocity under delta q_i is `-(delta q_i·x)/||q_i||`. Consequently, wherever the first shape variation is defined,

**`D_{q_i} g = -(T_i-g*m_i^T)/(V*||q_i||)`**.

For a facet integration triangle with vertices a,b,c, area A and S=a+b+c, the exact polynomial moment formulas are

`m_triangle=A*S/3`,

`T_triangle=A*(S*S^T+a*a^T+b*b^T+c*c^T)/12`.

The code uses these boundary moments for the derivative at the current body. An affine expression `g_base+Jg*(q-q_base)` is used only as a local automatic-differentiation device. **Every objective value and every line-search trial rebuilds the actual hull and integrates its actual volume and first moments.** The polar points are q_i/(1-q_i·g) using that same physical centroid, not the polar's unrelated mass centre.

The complete executable differential test ran on the frozen winning checkpoint from the decoded final source. Unit-normal-cross and endpoint-unit directions agreed to 1.0020334140225328e-13 in the escape value. Translation covariance errors were at most 8.881784197001252e-16; scaling covariance error was 1.4842727741326556e-16. For the fully specified seed-260909 finite-difference direction at step 1e-6, centroid derivative maximum error was 1.3334305014323089e-11 and escape derivative maximum error was 5.381253060932067e-7. The coarser 1e-4 probe changed combinatorics on one side and is not represented as a fixed-cell differential check. These numerical tests support the displayed analytic derivation; they do not replace the exact endpoint audits.

### Whole-body area concentration and genuine rank loss

I coupled this differential to the physical maximal-facet-area objective

`sum_i (A_i/sum_j A_j + epsilon)^p`.

The successful family used p=1/2, then a p=1/4 stage with epsilon=1e-6. Facet areas are grouped by actual exposed support, not counted triangle-by-triangle. All available normal coordinates and moving coplanarity charts can move, with both physical and polar escape constraints. The direction-normalized reserve used in the final stage was 2e-5; actual trial acceptance rebuilt the body. Small-area sets were tested as whole support-loss blocks. Intrinsic coplanarity closures were subsequently restored by exact rational records, then the actual maximal complex was audited afresh.

Relative to C752, C698 has eight fewer maximal facets and three additional units of exposed degree excess. The exact accounting is

`E = 3F-6-sum_v(deg(v)-3)`;

`376-349 = 3*(141-133)+(44-41) = 27`.

The degree-44 root is not a new 44-edge saving: C752 already had its corresponding root excess. The additional distributed contacts contribute only the extra three units. This is a real facet/rank reduction, not removal of integration diagonals.

### What happened to both escape graphs

All graph predicates were recomputed with exact integer signs at each body's own exact centroid. An arc i→j requires p_i·(p_j-p_i)>0. Chord graphs permit every vertex pair; true-edge graphs permit only actual mechanical neighbours. Every graph in this table has one sink and every node reaches it.

| Body | Maximum shortest chord hops: physical / polar | Maximum shortest true-edge hops: physical / polar |
|---|---:|---:|
| C752 | 84 / 76 | 107 / 77 |
| LYNX139 | 91 / 72 | 111 / 73 |
| New C808 | 92 / 72 | 114 / 72 |
| **New C698** | **98 / 74** | **119 / 75** |

**The winning C752→C698 branch shortened the polar graph but lengthened the physical graph. It did not achieve simultaneous global escape shortening.** This is the principal limitation of the successful area objective. For C698, chord arc counts are 652 physical and 203 polar; true-edge arc counts are 225 and 140. The exact selected-forest relative dot/radius-squared reserve floors are 76446/10^12 physical and 789859/10^12 polar. Those reserves use a different normalization from the direction cosine optimized above and are not coordinate perturbation tolerances.

## 6. A literal twelve-support block and its remaining obstruction

The LYNX139 branch produced exact positive C808 with 139 active inputs. Its complete generator and ordinary-moment evaluator are included as `before`. Its degree excess is seven, unique stable input is 3, unique unstable raw coordinate is (0,0,1), and all 1616 edge primitives are nonzero. This new raw apex must not be substituted for the original LYNX139 apex.

The exact `cut` body deletes precisely these zero-based input rows from C808:

**[11,26,54,58,60,86,88,92,123,125,132,136]**.

`CHECK_DELETION.py` verifies literal equality of every retained primitive halfspace. Therefore the raw before body is contained in the raw cut body; both are then independently evaluated at their own actual volume centres. Exact deletion gives 243/368/127, but the full class is **40/48/86**, weak000, not 110. All 1472 edge primitives are nonzero.

The continuous search uses

`q_deleted(lambda)=(1-lambda)*base + lambda*sum_j w_j*q_anchor_j`,

with nonnegative weights summing to one, retained anchor rows, freely moving anchor geometry and freely moving barycentric weights. At lambda=1 the deleted row is exactly redundant. The successful intermediate's numerical precursor was at lambda≈0.987670444140995; its rounded/reconstructed exact C808 is defined by its literal table, not by asserting that the old floating lambda equation holds exactly.

Second-order correction subsequently reached a numerical checkpoint at **lambda=0.9909885574281585**, still 267/404/139 and numerical own110, with normalized minimum about 1.4454e-5. All 139 supports remained active. Its complete q_hex, contact chart, deletion plan, barycentric weights and lambda are in `numerical/BLOCK_FRONTIER_FLOAT.json`. It is explicitly **unpromoted numerical continuation data**. Lambda near one does not mean that twelve mechanical facets have already disappeared. The exact before/cut pair shows how little added volume can still create a large critical packet; no feasibility conclusion about every possible moving-weight block follows.

## 7. A different sparse architecture: latent moving planes

To permit many exact contacts without assigning one dependent normal-coordinate owner per relation, I constructed the outer normals from intersections of a second, latent support system. The complete exact C702 parent is retained as `latent_parent`; it is 219/351/134, own110, with 135 defining rows and redundant input127.

For latent vectors q_i and a literal selected triple (a,b,c), define

`X_abc = (q_b×q_c+q_c×q_a+q_a×q_b)/(q_a·(q_b×q_c))`.

Let c be a separate literal polarization vector and set h_abc=X_abc-c. The actual candidate is

**P0={y:h_abc·y<=1 for every selected triple}, density1; P=P0-g(P0).**

Both latent nonwinner generators contain the complete integer latent controls, contact records, cap rows, polarization coordinates and ordered selected triples on grid1e9. `RECONSTRUCT_LATENT.py` evaluates all rational intersections exactly. A shared latent plane q_i·X=1 imposes exact coplanarity among the outer normals. If the contact is exposed, it yields a genuine high-order physical vertex; exposure is determined by the exhaustive outer-body audit, never by the number of equations imposed.

The polarization c is a **physical shape parameter**, not an accepted freely chosen mechanical centre. Every outer candidate's ordinary volume centroid is recomputed. The guarded version also checks latent halfspace exposure; the unguarded version permits the selected intersections to leave the latent hull while still rebuilding the actual outer body.

Deleting 80 outer rows from the 219-row starting polar and moving the whole latent geometry produced **exact C592:159/296/139, degree excess115, own8/2/8**. A floating tolerance reconstruction had suggested 152/289/139; exact reconstruction exposed seven additional microscopic true edges. The apparent low numerical merit did not mean own110. Deleting 100 outer rows produced **exact C534:176/267/93, own9/6/13**. It has119 supplied rows but only93 maximal facets; 26 redundant rows are retained in the complete definition. This is close to the numerical complexity target only, not close to the required equilibrium census in any certified sense.

These are usable exact sparse architectures, not positive endpoints. Their complete all-four-edge ledgers have respectively1184 and1068 nonzero primitives, with every weak class zero. Their generators, both auditors, negative-case acceptance wrappers and observed cold outputs are supplied. Nothing depends on reproducing an optimizer.

### Exact mass recovery for every preserved case

For all six cases, the finite W/L formula in Section3 and the embedded full evaluators define every exact rational mass and centroid. The following are only decimal displays, provided to detect wrong-body substitutions. After each defining own-centroid translation, all three first moments are exactly zero, including for the nonwinners.

| Case | Raw ordinary volume | Raw first moments (Mx,My,Mz) | Raw centroid (gx,gy,gz) |
|---|---:|---|---|
| before | .6082881075588479 | (.004434144272699621,-.01604506895832235,-.006546376673286051) | (.007289546216010226,-.026377416817687984,-.010761967219049621) |
| latent_parent | .4807546105895486 | (.0013225845849320736,.01264368196330028,.00025492688873897276) | (.0027510595963087907,.026299658255581476,.0005302640538930169) |
| cut | .6083318354959121 | (.004447621971142936,-.01605097361587174,-.006544276848616693) | (.007311177406188573,-.02638522707394885,-.010757741855284952) |
| latent80 | 26.77860865235662 | (-2.030009457416181,-2.057248283609407,2.0387300645759723) | (-.07580712962984851,-.07682431564376148,.07613278535278031) |
| latent100 | 27.033994643462204 | (-1.2821916604164778,4.472571688300095,1.8577681111078812) | (-.04742886418846568,.16544250109118538,.06871970404703608) |

Additional exact report bindings; each A and B is separately generated and byte-identical:

```text
before A=B 290494 bytes
62ac88dce95e1d16e2d9d6a420d82ee73f3c50b1efa290aea396c7153bf21cf9
latent_parent A=B 202662 bytes
3b68bdf222c8211fcba594b5a6edc66300c217622387a41cbce13f07740e47e9
cut A=B 265455 bytes
ec214e5bfdc97d41ebc4cbf591de0d5a39b78a0bf643763bfd494ddf3268567c
latent80 A=B 215125 bytes
41b87ce5fb87c32ab657d3b0b518d985830f55a0eea155764043b55ab213aeb2
latent100 A=B 342026 bytes
c80c86304747c20201dd4f791d2606516ddf15283ea12da13512b8c655aeffa1
```

## 8. What remains and the useful continuation

The successful facet-area concentration made the physical escape chain longer. The twelve-row homotopy reached a positive near-wall body but not a positive completed block. The latent construction attained substantially smaller exact complexes, but lost the one-stable/one-unstable census. These are the consequential observed obstacles, not a theorem that lower complexity is impossible. Additional bounded choices of deletion blocks, metric/projective controls and repair objectives did not produce another promoted endpoint; none is a global exclusion.

A simple geometric diagnostic explains why radial and angular redistribution must be coupled. For a strict positive escape chain with successive angular separations theta_j and radii r_j, `r_(j+1)*cos(theta_j)>r_j`. If n steps join directions separated by Theta with endpoint radial ratio R, convexity of -log(cos) gives the necessary inequality

`log(R) > sum_j -log(cos(theta_j)) >= -n*log(cos(Theta/n))`.

This is a fixed-endpoint chain condition, not a universal polyhedron bound: the endpoints, radii, directions, incidence and centre are all allowed to move in a new body.

The useful next direction is to use the length-free differential and boundary centroid Jacobian while explicitly rewarding shorter physical **and** polar routes, and simultaneously changing exposed latent contacts or removing whole support blocks. C698 is the positive exact restart; C592 is the high-contact sparse restart with explicitly wrong class. Preserve the complete census while testing transitions, rather than using the small area merit or nominal rank as a stopping condition. At C698's current degree excess44, F99 would give E247; that is only an accounting target, not proof that this deformation exists.

## 9. Fully self-contained recovery and executable continuation

The four `LYNX2_CAPSULE` parts below concatenate, after whitespace removal, to **64085 base85 characters**, with lengths **16000,16000,16000,16085**. Base85-decode and lzma-decompress them to **205902 bytes**, SHA-256

**`fe93ee265e57560b286199004863bc431800181913b07c83b41c6ae0e1742143`**.

The decoded JSON is `{"version":1,"files":{relative_path:utf8_source}}`, containing **60 files**. It includes every defining integer, selected latent triple, exact contact record, frozen winning float.hex input, full numerical block frontier and complete required helper. No external parent, omitted helper, numerical optimizer rerun, or sandbox path is needed for exact recovery.

Save the concatenated stream as `capsule.txt`. This is the complete decoder:

```python
import base64, hashlib, json, lzma, sys
from pathlib import Path, PurePosixPath
s = ''.join(Path(sys.argv[1]).read_text().split())
b = lzma.decompress(base64.b85decode(s))
assert len(s) == 64085 and len(b) == 205902
assert hashlib.sha256(b).hexdigest() == 'fe93ee265e57560b286199004863bc431800181913b07c83b41c6ae0e1742143'
d = json.loads(b)
assert d['version'] == 1 and len(d['files']) == 60
out = Path(sys.argv[2])
out.mkdir(exist_ok=False)
for name, source in d['files'].items():
    p = PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts
    dst = out.joinpath(*p.parts)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(source, encoding='utf-8')
```

With that decoder saved as `decode.py`, exact verification commands are:

```sh
python -S decode.py capsule.txt recovery
python -S recovery/RUN_CASE.py winner
python -S recovery/RUN_CASE.py before
python -S recovery/RUN_CASE.py latent_parent
python -S recovery/RUN_CASE.py cut
python -S recovery/RUN_CASE.py latent80
python -S recovery/RUN_CASE.py latent100
python -S recovery/CHECK_DELETION.py
python -S recovery/RUN_BASELINES.py
python -S recovery/numerical/EXACTIFY.py recovery/numerical/WINNER_FLOAT.json rounded_winner --grid 1000000000 --tag LYNX2_C698_AREA_D1E9
```

Case directories must be fresh; `RUN_CASE.py --output NEW_DIRECTORY` selects another fresh location. Never use `-O`. Exact execution needs only the Python standard library and was tested with **Python3.13.5**. Expanded rational reports require the included `sys.set_int_max_str_digits(0)` calls; this is serialization handling, not a relaxed arithmetic test.

Numerical discovery used **NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu**, float64, one Torch/BLAS thread, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. The complete remaining modules retain the actually used algorithms; unused functions were removed from the inline source, and the retained import closure was checked and executed. The unpruned research source is also in the supplemental archive.

Executable continuations with exact input checkpoints:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
# Re-execute the final global power-area search stage; not guaranteed bit-identical.
python recovery/numerical/area_power.py recovery/numerical/POWER_INPUT.json next_power --cycles 14 --steps 140 --power .25 --eps .000001 --cut .006
# Restart global motion from the actual exact C698 generator.
python -S recovery/numerical/FROM_EXACT.py recovery/proof/GENERATOR.json start698.json 3
python recovery/numerical/area_cycles.py start698.json next_area --cycles 12 --steps 115
# Reproduce the differential/covariance tests.
python recovery/numerical/CHECK_DIFFERENTIAL.py recovery/numerical/WINNER_FLOAT.json differential.json
# Resume the complete moving-weight twelve-support frontier.
python recovery/numerical/soc_batch.py recovery/numerical/BLOCK_FRONTIER_FLOAT.json next_block.json --resume --steps 220
# Restart from the exact C592 nonwinner, preserving all latent defining data.
python -S recovery/numerical/FROM_LATENT_EXACT.py recovery/cases/latent80/GENERATOR.json start592.json 72
python recovery/numerical/RESUME_LATENT.py start592.json next_latent.json --guard --steps 220
```

For `latent100`, use its own generator and stable-target input63 rather than72. Those are numerical target choices, not a claim of a unique stable face on either nonwinner. `EXACTIFY.py NEW_CHECKPOINT NEW_DIRECTORY --grid D --tag NEW_TAG` supports either ordinary contact or latent checkpoints; it rounds exact float.hex rationals with ties-to-even, restores declared rational contacts, derives actual V/E/F from a fresh exact audit, then requires the complete positive own110 replay. It must fail rather than promote a nonwinner. Numerical optimization is not asserted bit-reproducible; the frozen literals define all claimed exact endpoints independently.

The decoded-source differential test, an actual global-flow step, and an actual guarded latent resume were executed successfully. The guarded latent step rejected its numerical proposal normally; no numerical improvement is claimed from that smoke test. All endpoint claims above depend on exact reconstruction and complete replays, not on those smoke tests.

## 10. Supplemental files and integrity

Complete source, exact reports, cold receipts and unpruned numerical work (`Steady_Lynx57_C698_RESEARCH.zip`): **5879875 bytes**, SHA-256 **`babc4210edc94b5d7277b3af9fd44fd096235144ace94c782d67ec69ab515d15`**. All **677 manifest entries** were checked against the completed ZIP bytes. It contains expanded rational moments, complete maximal incidence and sign ledgers for the six cases, the actual replay transcripts, and the source/rounding comparison receipts.

The full self-contained Markdown handoff (`Steady_Lynx57_C698_HANDOFF.md`) includes these same literal capsule parts. The links supplement rather than replace the inline definition. No research journal was modified.

### LYNX2_CAPSULE_1

[Encoded source block omitted; the code in this passage is incomplete.]


### LYNX2_CAPSULE_2

[Encoded source block omitted; the code in this passage is incomplete.]


### LYNX2_CAPSULE_3

[Encoded source block omitted; the code in this passage is incomplete.]


### LYNX2_CAPSULE_4

[Encoded source block omitted; the code in this passage is incomplete.]
