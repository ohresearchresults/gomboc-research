# figure-0337

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Sharp Quartz 24 — exact nonlocal descendant and mass-neutral new-witness repair

## 1. Verdict and acceptance boundary

**No homogeneous own-centred strict (1,1,0) polyhedron with E<500 was obtained.** The completed, independently audited results are two strict **(2,1,1)** bodies and a finite supporting-cell certificate for a real, rank-three ordinary-moment actuator. Neither body is a Gömböc.

| Exact body | V | True E | Maximal F | Own-centroid (S,U,H) | Weak equilibria |
|---|---:|---:|---:|---:|---:|
| SQ24_NP37 | 37 | 105 | 70 | (2,1,1) | (0,0,0) |
| SQ24_MN41 | 41 | 117 | 78 | (2,1,1) | (0,0,0) |

NP37 is a moved-geometry descendant of AFF83, not a claim that the AFF83 solid stayed unchanged during the deformation. MN41 is then a **genuine additive extension of the unchanged, exactly centred NP37**, with strictly positive added ordinary volume and exactly zero added first-moment vector. Both contain the unchanged, own-centred GU22 plus the closed unit ball strictly. They therefore do not remain in the excluded original-GU22-witness envelope.

The useful new result is an executed repair of a small radial-ascent reserve: vertex 33 acquires new witness 37, whose own witness is 32. The direct ascent value improves by a factor of approximately **33,006,251**, and the minimum relative ascent reserve of the full one-root forest improves by approximately **28,967**. This repair uses actual solid material and exact moment cancellation, not point weights, a substituted reference centre, or an unexecuted compensator proposal.

The remaining stable/saddle packet is still deep. Its distance-ratio barrier is approximately **0.9261301911636768**, and the two stable triangles and saddle edge survive unchanged. Thus the new witness repair must not be described as stable-basin cancellation or as a near-110 endpoint. These bodies are not overall small-body records relative to GU22; their value is the changed supporting geometry and the fully executed ordinary-mass interface.

## 2. Source authority and what was actually executed

I recovered the journal's ten-file, 47,195-byte R83/AFF83 source capsule with SHA-256 `6d9c0d51af19b83810077f3276db5445892e3277c62442fa581c6cd6cc182416`, and executed its complete replay. Its final marker was `SQ24_GU22_OBSTRUCTIONS_R83_AFF83_ALL_FOUR_FULL_EXACT_AUDITS_PASS`. That marker certifies the parent nonwinner classes, not 110. The literal capsule and the late journal distinguish the R83/AFF83 architecture from the excluded old envelope. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The completed new construction below needs no historical archive, optimizer state, or missing parent coordinates. Its seven-file inline capsule contains every input and helper required to reconstruct both new bodies, the finite contact cells, the moment calculations, and both exhaustive auditors.

The initial interrupted exploratory runtime lost its unpromoted working files. I did not promote any body from those missing files. The source parent was recovered again, and the exact results in this handoff were regenerated, frozen, audited, and cold-replayed in the surviving runtime.

Discovery retained this AFF83 input-index sequence before moving the remaining coordinates:

`[0,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,29,36,41,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,68,69]`.

Every deletion or coordinate proposal was screened against its recomputed numerical volume centroid and rebuilt hull. The frozen rational endpoint, not that numerical chronology, is what the exact audits certify. In particular, the final NP37 coordinates are not merely an undeformed subset of AFF83.

## 3. Complete literal definition of NP37

The following integers are the complete uncentred checkpoint. Let `P_i = (4*W*I_i - M)/(4*W*D)`, componentwise. The hull of these 37 rational points is NP37. The auditors independently reconstruct the boundary and recompute W and M from ordinary tetrahedral integration.

```python
D = 10**15
I = [
    [6010851933593284, 81691159443508352, -92640959026753936],
    [1339864332303852, 87244333729017792, -86764137546854128],
    [-4437649667204246, 94526007349204944, -76898042045214560],
    [-8335516764884204, 99613680408747840, -68182830152496424],
    [-13381370039892864, 105255966657071744, -49848359272883312],
    [-17341381851675110, 109029239495379568, -35239707417051356],
    [-21247743932927528, 110695641358139008, -19670216142630092],
    [-24612805816292804, 110354936943705696, -4514153038224925],
    [-27486201231419276, 107693567414594384, 11758219331133232],
    [-29776428300051400, 102649073438829344, 27776584345644656],
    [-31715860677422364, 95577715870899504, 42362007016716376],
    [-33116755490946232, 87698649862758992, 54308600733024752],
    [-34218857260443264, 78691127115790960, 64887042754679416],
    [-32859522345639752, 68847610931407896, 74840034211524192],
    [-31410876422305124, 55463946305318016, 84524840782946064],
    [-29164361852857656, 39585917300851152, 92479752400668640],
    [-28665682284360936, 18408251362086128, 97182438729889632],
    [26331314242675, -7812870265755152, 75094676448247760],
    [21989598917545424, -49210167682069144, 38516974414230592],
    [29011748163424436, -72661667747940112, 19020270053840500],
    [17144518632420550, 58646384319250176, -101439624666916992],
    [23363834338740660, 45359474750062976, -106118142133380160],
    [28698334635374452, 30660349764970340, -108405257071619936],
    [33059546649258444, 17383508743590088, -109593599163101856],
    [36704940756777656, 3769769030276968, -109245633812968656],
    [39596213293761896, -10245212139582086, -107258784121257392],
    [43998657911059304, -27685609210475044, -101104416542314672],
    [47052031783386536, -43753249370879008, -92440923124164400],
    [47007252541335264, -57728291931316640, -83155591344456496],
    [45218329292889224, -70025861157859880, -72759327935361792],
    [42936609226476608, -80769703293606832, -60258817525646432],
    [38333656378312688, -88913980249218528, -49199596659689440],
    [32765486601420464, -95711411168350240, -36182971240302848],
    [28491888154878864, -100006759665303840, -15755175050069058],
    [15477158899511858, -100678812334705024, 3231608252538710],
    [-19373766552968524, -54972877423471624, 27906903752514008],
    [-33026348147499256, 3969945109759798, 78896348295354976],
]
W = 3193085389494484181912229940647676745679175426430336
M = [24032451136859676368769355820152536752377307811986729340214121376800, -38575767621632429065299558280186605578064809451297416696774483694912, -11863592054799278181956718614097767516232372373859835817210779498256]
```

Here W is the signed boundary determinant sum and M is the determinant-weighted vertex-sum vector for the uncentred integer checkpoint. Consequently

`V_NP37 = W/(6*D**3)`

and the uncentred physical centroid is `M/(4*W*D)`. The displayed translation is a coordinate change to the actual physical centroid. It is not an assertion that the uncentred checkpoint already has zero first moments.

The exact ordinary volume is

```text
V_NP37 = 24945979605425657671189296411309974575618558018987/46875000000000000000000000000000000000000000
```

approximately **532180.89824908075**. For the defined centred NP37, all three ordinary first moments are exactly zero. Both auditors return stable faces `[1,35,2]` and `[17,18,21]`, unstable vertex `0`, saddle edge `[16,34]`, and no weak face, vertex, or edge equilibria.

## 4. Complete finite construction of MN41

All labels in this section refer to the centred NP37 coordinates above. Keep vertices 0 through 36 fixed. Add vertex 37 at

```text
q = (26634546314457/1000000000000,
     -19395112486393/200000000000,
     -2986014941321/200000000000).
```

Its visible old triangular facets are exactly

```text
[12,33,13], [13,33,14], [15,33,16], [14,33,15].
```

The code constructs their entire horizon, replaces the visible patch, and checks every resulting support inequality against every point. Let `B = conv(NP37 union {q})`, and let `DeltaM` be the actual first moment of `B minus NP37`. It is determined directly from the four visible tetrahedra: for each oriented visible triangle `(a,b,c)`, put

`v_f = ((b-a) cross (c-a)) dot (q-a) / 6 > 0`;

then sum `v_f` for the added volume and `v_f*(a+b+c+q)/4` for DeltaM. The program checks this against the actual complete oriented boundary, rather than presuming that disconnected proposal caps describe the hull.

Use these three unchanged, pairwise vertex-disjoint base facets for the physical compensators:

```text
B1 = [10,11,13]
B2 = [0,5,6]
B3 = [8,9,17].
```

For base k define its barycentre `b_k=(a+b+c)/3` and outward unnormalised normal `N_k=(b-a) cross (c-a)`. Solve the rational 3 by 3 system

`[b_1 b_2 b_3] * lambda = -DeltaM`.

All three resulting lambda values are strictly positive. They are **actual cap volumes**, realized geometrically, not fictitious masses. Set

`h_k = 6*lambda_k/(N_k dot N_k)`.

A tip at `b_k+h_k*N_k` has tetrahedral volume exactly lambda_k. Tangential motion of that tip preserves this volume.

For a nonzero normal N, define its deterministic ordered tangent basis as follows: choose the coordinate a maximizing `abs(N[a])`, breaking ties by the smallest index; for each remaining coordinate j in ascending order, take the vector with entry j equal to 1, entry a equal to `-N[j]/N[a]`, and the third entry zero. Let `d1,d2` be the two vectors for N1, `d3` the first vector for N2, and `d4` the first vector for N3. The matrix

`L = [lambda_1*d1, lambda_1*d2, lambda_2*d3]`

is nonsingular for the printed data. Solve

`L*gamma = -sum_k lambda_k*h_k*N_k`.

Define initial compensator tips

```text
u1 = b1 + h1*N1 + gamma1*d1 + gamma2*d2
u2 = b2 + h2*N2 + gamma3*d3
u3 = b3 + h3*N3.
```

The added first moment is now exactly

`DeltaM + sum_k lambda_k*b_k + (1/4)*sum_k lambda_k*(h_k*N_k + tangential_shift_k) = 0`.

The exact globally supporting boundary confirms that these are the actual solid cap volumes and actual moments. All old NP37 vertices remain fixed, and no recentering is performed after this addition.

### Nonzero canonical actuator endpoint

Solve `L*xi = -lambda_3*d4`, and set

```text
k1 = xi1*d1 + xi2*d2
k2 = xi3*d3
k3 = d4.
```

Divide all three vectors by the maximum absolute coordinate occurring among them. This common positive rational normalization makes their maximum absolute coordinate 1. Each vector is nonzero; `N_k dot k_k=0`, and `sum_k lambda_k*k_k=0` exactly.

**The final canonical MN41 vertices are**

```text
[P0,...,P36, q, u1+(1/8)*k1, u2+(1/8)*k2, u3+(1/8)*k3].
```

This specifies every coordinate by literal rational data and finite linear algebra. The complete runnable implementation and both auditors are in the inline capsule in Section 10.

The exact ordinary volume is

```text
V_MN41 = 8032163638404379730236505547591051390501431671500055613099860091107135113216334261184031953645143070019286203679172959421785366231661231234117859378230507477324899548359729259059663295658530919892291717/15092892300345775129778512325348326904394993354426457491966789608608583779283355583030897794409175765909286685613716572563568356382590598915713723440752000000000000000000000000000000000000000000000
```

approximately **532181.86935716518**. All three raw first moments at this final endpoint are exactly zero. The actual added volume over NP37 is `V_MN41-V_NP37`, approximately **0.971108084495 > 0**; its actual added first-moment vector is exactly `(0,0,0)`.

## 5. Actual supporting cell and ordinary-moment polynomials

Replace 1/8 in the last three coordinates by a rational parameter s. An executed exact Bernstein certificate proves that **every s in [-1/4,1/4]** has the same 41 vertices, 78 maximal triangular facets, and 117 true edges. It checks **3,512 strict Bernstein polynomials**, covering every off-facet supporting inequality, all 468 true-edge sign primitives, every nonroot vertex's retained positive witness, and all root-versus-other-vertex inequalities.

Each facet contains at most one moving tip. Therefore each supporting slack and each tested edge or witness primitive has degree at most two in s. Positivity of the three exact quadratic Bernstein coefficients certifies the entire interval, not only sampled parameter values. The ledger hash is

`762bdffc5e7257b7f86157e0c364b3fed5eb9839d812b01162f7bb08c7e72708`.

The actual ordinary-mass polynomials on this checked cell are

```text
V(s)   = V_MN41
Mx(s)  = 0
My(s)  = 0
Mz(s)  = 0.
```

The degree bounds follow from the actual triangulation. The code independently reintegrates the full solid at `s=-1/4,0,1/4`, proving these polynomial identities. The final body uses the nonzero value `s=1/8`.

This cell is rigorously strict211 throughout. Its two stable triangles and saddle edge stay fixed. **Thus no member of this particular interval is 110.** This is a statement about this specified finite family only, not an impossibility theorem for all new-witness additions, all moment-balanced panels, or the R83/AFF83 architecture.

### An actual rank-three moment actuator, not merely a zero-moment kernel

At the canonical endpoint, additionally move tip 38 by `z1*d1+z2*d2` and tip 39 by `z3*d3`, leaving all other vertices fixed. On the executed supporting cube

`abs(z1), abs(z2), abs(z3) <= 1/100`,

the full hull retains the same maximal facets. Eight exact corner hull checks and complete mass reintegrations certify this cube. The support slacks are multi-affine in these three controls, so positivity at all eight corners covers the whole cube. The physical volume is constant and the physical first-moment polynomial is exactly

`M(z) = (L/4)*z`.

The determinant of this moment matrix is nonzero, approximately **1.64199689898722e-05**. Thus it is a finite full-rank actuator in an executed contact cell. The complete exact matrix is reconstructed by the formulas above and stored in REPORT.json. A guaranteed infinity-norm moment capacity is

`(1/100) / max_row_sum_abs((L/4)^(-1))`,

approximately **1.761764674560065e-05**.

For nonzero z, this auxiliary body is **not** asserted to have its physical centroid at zero. Its centroid is exactly `M(z)/V_MN41`. The cube certifies real geometric moment leverage; only the explicitly balanced endpoint and the s-family have zero raw moments. Do not extrapolate the actuator beyond its certified supporting cube or interpret its off-centre auxiliary states as centred equilibrium certificates.

## 6. Complete maximal incidence and exhaustive mechanical census

Every MN41 maximal facet is triangular. The complete actual facet list and deterministic true-edge reconstruction are:

```python
F = [[32,37,34],[33,34,37],[7,35,36],[25,32,35],[7,36,8],[6,35,7],[20,22,35],[1,20,35],[24,25,35],[8,36,9],[4,35,5],[9,36,10],[2,35,3],[5,35,6],[14,36,16],[3,35,4],[10,36,11],[22,23,35],[23,24,35],[16,35,34],[25,29,31],[16,36,35],[11,36,12],[12,36,13],[1,35,2],[13,36,14],[25,31,32],[25,26,29],[32,34,35],[26,28,29],[0,20,1],[14,16,15],[26,27,28],[20,21,22],[29,30,31],[11,12,13],[0,1,2],[24,27,26],[24,26,25],[0,2,3],[18,34,19],[18,19,27],[0,3,4],[23,27,24],[6,21,20],[19,30,29],[0,4,5],[6,7,21],[15,16,17],[0,6,20],[13,14,17],[19,29,28],[19,28,27],[14,15,17],[16,34,17],[18,23,22],[19,34,33],[18,22,21],[9,10,17],[17,34,18],[18,27,23],[10,13,17],[17,18,21],[7,8,17],[7,17,21],[19,33,37],[31,37,32],[30,37,31],[19,37,30],[8,9,40],[9,17,40],[8,40,17],[11,13,38],[10,11,38],[10,38,13],[5,6,39],[0,5,39],[0,39,6]]
E = sorted({tuple(sorted((f[i], f[(i+1)%3]))) for f in F for i in range(3)})
assert len(F)==78 and len(E)==117
```

These are not a guessed boundary. Auditor A and auditor B independently reconstruct the same maximal facets and true edges from the coordinates. NP37's full 70-facet and 105-edge incidence is likewise reconstructed and included in both NP37 audit outputs.

For both bodies:

```text
Stable maximal facets: [1,35,2], [17,18,21]
Unstable vertices:     [0]
Saddle true edges:     [16,34]
Weak faces:           []
Weak vertices:        []
Weak true edges:      []
```

For MN41, all 76 other faces are strictly nonstable, all 40 other vertices strictly nonunstable, and all 116 other true edges excluded. Both complete audits check the two foot-coordinate inequalities and the two normal-cone coefficients on **every** true edge, including weak candidates. Euler's identity is only an incidence consistency check and is not used to infer the saddle count. All 468 primitive edge quantities are nonzero.

An early floating screen merged a nearly coplanar pair and printed **E116/F77** for the unsheared 41-point proposal. That incidence is rejected. The independently reconstructed exact incidence of the final body is **E117/F78**, with no quadrilateral or artificial diagonal removal.

The exact new primal parent array is

```text
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 34, 34, 0, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 33, 34, 16, 32, 11, 3, 10]
```

Every arrow is strictly positive and terminates at vertex 0; maximum depth is 17. The exact auditors separately check vertex 0 against every other vertex. The minimum relative arrow is approximately **9.535512491172467e-08**, versus **3.291798373221557e-12** in NP37.

In particular,

```text
old best arrow at vertex 33   ~= 3.401846083436594e-08
new arrow 33 -> 37            ~= 1.122821848643919
improvement factor           ~= 33006250.75634311
```

Vertex 37 itself has the exact strict witness 32. The fixed old solid and the added ordinary material both have centroid zero. This is why the new witness reserve is not lost to a hidden centre-of-mass shift.

## 7. Executed verification and hashes

The two full auditors are separate implementations. A uses exhaustive supporting triples, projected monotone polygon reconstruction, a boundary tetrahedral fan, all-other-point vertex tests, and an exact Gram-system edge test. B imports no geometry helper from A and uses independent supporting-line polygon reconstruction, a different interior-reference mass integration, incident tangent generators, and cross-product cone coefficients. Both reconstruct maximal incidence, check global support, connectivity and opposite edge orientation, integrate ordinary volume and all first moments, and classify all strict and weak face/vertex/full-edge equilibria.

The exact replay additionally executes a regular tetrahedron, a cube with actual quadrilateral maximal faces, and a deliberately degenerate tetrahedron with strict counts `(3,2,3)` and weak counts `(0,2,2)`. Both programs agree on these fixtures. Four invalid denominator/duplicate-point inputs are rejected. A nontrivial exact rigid motion of NP37 is independently reintegrated by both programs and has the expected physical centroid `(7,-3,5)`.

The complete seven-file source capsule was decoded into a fresh directory containing no generated outputs. A full cold replay reconstructed both final bodies, both audits of each, all moment/support cells, and all controls. **All eight pinned output hashes were byte-identical.** The observed terminal marker was

```text
SQ24_NP37_MN41_TWO_AUDIT_AND_MASS_CELL_COLD_REPLAY_PASS
```

Selected hashes:

```text
NP37 definition  02f3a52f76728ab7ce919b5de32ffe86e5f61f563f8245490636a35d4fe63302
NP37 audit A     c07c245d4386fedec7a778b3ef7a7abc9ed57c11e06955d27ba1bd9b08d7bf64
NP37 audit B     c1b3f59ca48aa8c86d9610870ca48b9ad4afa22a7bd381ca29256ff3f4f15059
MN41 definition  9840ece948f01a82732ed3c7aaa91c3a907d45ce92a2228569af4271e6befcb3
MN41 audit A     5a3f91d8d0c21671deaba8288db7e6ec305890cb1b0e4039c467f390fe7fb5c3
MN41 audit B     4ed8cad934d6b9ec691a512097b9abb84a1c1ed9eb0fbbd35985bb1652dd4bb2
REPORT.json      3110468ae890a29a2f7dc307768b21e669b5af23cca5ed5fdd459b13152dab69
```

These are independently executed software implementations within this research, not external peer review or a proof-assistant formalization.

## 8. Exploration outcomes and the remaining construction problem

I tried nonlocal deletions and all-coordinate panel motion; new-generation diameter-ball witnesses; direct additions with recomputed ordinary centroid; exact mass-neutral primary-patch plus three-compensator repairs; rotated coil unions; dual witness-tree linearization; and a radial merge-tree/persistence screening objective. None of these screening objectives was used as an acceptance certificate.

The initial diameter-ball filling and unconstrained persistence searches produced additional equilibrium pairs rather than a certified cancellation. Direct recentering after new-witness additions repeatedly consumed the small primal reserves elsewhere. The executed moment-neutral repair above avoids that particular failure by leaving the actual centroid unchanged.

A subsequent floating chain alternated this kind of neutral repair with further panel motion. It reached a screening barrier near 0.9102347658 before another rescue failed, but developed near-coplanar/sliver issues and was **not** promoted to an exact successor. Its labelled unverified checkpoint and discovery code are in the research supplement. No exact V/E/F or strict/weak equilibrium claim is made for that floating state. The accepted continuation anchor is MN41, whose literal reconstruction is above.

No broad exclusion follows from these finite failures. In particular, the GU22 original-witness theorem does not exclude this moved/new-root geometry, and the certified strict211 s-cell does not exclude leaving that cell. Conversely, a nonsingular moment map or a strong one-root forest is not a certificate that the remaining polar basin can be cancelled.

The most useful next construction should begin from MN41 and jointly move the closure region containing both `[1,35,2]`, `[17,18,21]` and the interface `[16,34]`. The current finite kernel deliberately preserves their geometry and therefore cannot perform that cancellation. Use the rank-three actuator only within its actual certified moment capacity; for a larger primary patch, rebuild the compensator weights, actual supporting hull, and contact cell. A new accepted endpoint still needs a fresh rational definition, its own actual mass, full strict/weak edge-cone checks, both independent audits, and a cold replay.

## 9. Portable artifacts

[Exact constructions, complete audits, cells, source and cold-replay receipt](sandbox:/mnt/data/SQ24_NP37_MN41_EXACT.zip): **436,226 bytes**, SHA-256 `63a9d90b6f14a9fc897cb96601c96926de6dd9d9ddca141fb089b6a0227ac33a`. The archive contains 21 files, with all listed payloads checked against its manifest.

[Discovery source, parent recovery, logs and explicitly unverified floating checkpoint](sandbox:/mnt/data/SQ24_NP37_MN41_RESEARCH.zip): **1,121,456 bytes**, SHA-256 `be5d76040aae1ca372718228f5d5b15e72196368b666e6346f0d431a68c2b103`. Its 73 files include a checked payload manifest. It supplements the exact handoff; its numerical proposals are not additional certified bodies.

The cold-replay receipt SHA-256 is `81297985e24e45662462ae6fd316668a32d62da58580aab9ddd314ce8c34b995`. The archives are optional for the exact constructions: the complete source is embedded next.

## 10. Complete standalone recovery capsule

Save the following complete program as `recover_new.py`, then execute

```sh
python -S recover_new.py
cd sq24_np37_mn41
python -S REPLAY.py
```

Use Python without `-O`. Exact recovery and verification use only the Python standard library and were executed with **Python 3.13.5**. Discovery used NumPy 2.3.5, SciPy 1.17.0 and Torch 2.10.0+cpu; none is needed for the exact replay.

The decoded canonical JSON is **29,678 bytes**, contains exactly **seven complete files**, and has SHA-256 `4cb82fbcbeb9582868c0920e4803570146a0ca5e752706839bdb8fa818faa282`. The files are `main.py`, the two independent auditors, the literal NP37 raw checkpoint, the literal GU22 checkpoint, eight pinned output hashes, and `REPLAY.py`. The main program includes every rational geometry helper, the actual visible-patch reconstruction, the physical volume/moment construction, both supporting-cell certificates, the exhaustive audit calls, fixtures, and the deterministic final definitions. There are no omitted helper modules or optimizer dependencies.

```python
from pathlib import Path
import json,lzma,base64,hashlib
B85=r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;B)OMeO&-Oh=iqrocag;lg9zQDdLTm8Uv={r_qQYhzmHO-wx$p3W4kKQX4qOL%4S!iXyI8
4{dAy^}Z(PRHXO_{J5`$$F64F1t>R6{dRNzuf;wTPm~SKjMGI2iD-J<jbsbr_A^nL4p$h{|92U$OAf%)J)<;^_h#D<S9=7VX0_UV
d`P}8^iyVAdM7odRfwyeXJ+8z#*WT3u@k#^l(}E>;B9h}e-X;1c*QqZ$8mg9%l^yz${o*2n1s_WJnBO23CSY0Ji@XAl_VTn0o>Hj
H1o&eW}F9Vc7(3MX77v^;`qosq6&p8bmrDoXm5KEkYsNh>r%tY;YaJZrZxk*Xsy9xqB;H>cap`0LpSN&BOpvNm<@lSXyhUk^nlWz
Y~bfUCu}e`(ZRjP2SLQi1m(=#Zczq@U(`sdAFvXj8tyI5>*Q1^l+ZSnUv;ViNw1Azn=mL~+d(e&_tN&~4Di=;x?5GVm`!5%K>tLV
R(nN98&z^}vY=B}kb#aaPKY#s&_dhy0QGafJt(oNe(6|e@tFVUSWxyarlB=T^4WoCclTopH=uNOdPkkG=>1KTg<4lf)Ye?MZkgGY
;d-9f0~TYal^H1qo9U_fdQFB^M*|alKdWxfMYYMs1`vEfJX?IXJi4~=(V_H>HbHVJ6sq-Q9Llxu@PJ`)J!%<y@#%UrE{_f-0zcJ-
-6b#L^b;O&Q82%uu*kAXll<?{Hmb(Z<LrW*D2P~=sgUFb_M4oV+_o6qNKCGgP5jF6$dHAnzJ_O<ix-zHXceKpnvLtc_}HZH4@y(?
6f)<X;qYX%Sh6=EDewd;A*|(kt|hl))kwwfJE?)Dl>4QLQJ3}{k$WXKu4NVqe_QTX??~YwZ9fAw<u1v1ObE@Nf}e6=PzZ8Gmv|<z
gqo2)&R}R9LW<re`ReJMwrroCzD=NRDxY@qV#m|zJVlG{?-f)gwCy}y-bX)V+3}F};KE+}xyM;K;lsZ|WpjSe-=kiIsUeihiqFO+
9*g24&IE2vqi$uKzgeAO`h`($e$Qc$7TVjj{=2oJd9DsPUd2Y73)kTGVO1m0B=%6<<u_!!tNu9NLY+0FBgE*~rM&eKqE+gHqsrQ-
DDQGXrQMO*d_40O7o|;H?m?TFY+xO>5a&Xeob=**O$nLs;4K%36<Kosezw*(8&mv@m!Ay>sO>z%1Ca)})><;c`*SPZ<D3dzFGR8f
Jo}md4{=O#Vu4^ptEE5>bY~4Dh7P!hh4Fawpp2{~2*RaX!NN%ujpx=hi-8=FqwvzC`ZeR|<l>!PIn>S~ei-S*>Uys?J3zawPmJJO
1$NPKW<&kHz249{rdz4J^M+$0($TWgP0*GD&P-5?XMYE;>dotOy*|pw2LIh5Cv1c+P6PS5T~mY(7+>GUH=Cv|K=IVM*^LY_RYnqF
gl`do_r_LO+4mhqCjeb@&66Vc{AHsO>#a1GVP)Ao1oCdzD*zGD&Z3;%Y#&w8ke9nh6_I?W0uHRBi>Rl4yA|w}6?+z;z^<Q)Y7@Dr
^Cv??mOT@Lj*Yk)_F+DJ^}kCB2h7%}Y+<}vU5cg``tdD<NYknV7VK-g9?YV!`FswRf`kCHKQai@oS$?7p0*l*W$Hb&_APMC=fs~N
1e5=*O}k~tr(jkwg3-<ViQRTjP;-9=yaS$m;Up&w{TT<3&unFhnm(AM)j*{~J>^L$;Nx|9xGS<kbf$i^bo5YzX|zbBij4NZ5%>`@
qX%6SX4w!f`8wd+yKDi6f(C$~$8J9&s5;UT8MW)8eEvK}39Q&XmQB-S_r`Q;m}Ow%64-LFS$Vd7{u?pYn~Q;23k)m@$eBg*=auVd
<hOlQP*?4S`kDfo?I<We1ozV}iZyR*R^AABQaL)p>Y?!Y18F8zwl%RK<<%6hQf*dr`g<|CH>d<1G$om2R9~zn5%|?BsH%tATDhHu
MepE@+&>ApzY_DWaCy?YYG6e|3#8NTj~A%9a10>FiZ;JG!B+WL;#Kq|hUMd37M-@Bi48bqQuZL9h7Xzgbv6<Y1&9&wHXkY9@ty#y
W>!E&Kmf~Iy_${&A){J@)GxTw>6I^d;4s>@PdlaCf{>@uy1!P19(7Xc-w_}94m`f;PO}J9cXx>g$Fe?Se=EC<GuCO%l8`3GDnZvm
dBJV*ZvF-^FmC#!uG0CRN}<Nat)9CIyUVY6H%nhDbdJy|g@wcZ62*d#F4s9|RLkEeHhg!0F4QYCj9Z0LqNTW04%<UCGKvqD=+$lg
q#@grRe)JH+i$@s^Ij2utengt@JqIQ<8w6}mLZlMOpPV#woYL0(G~Hdk${DHWeGRE12B2=yl1MJPL%Eb@wyDV)u}K|pHr7XPG1^y
8NaI_M~deb33Rs{1jJ=~@s8bqR@a!xtZq$+;qBnYcVxfnS0u8>5%wEeOIj7$lB#)m>wDQZ`@r2_8?I<=*=CeVazphwHCBJIk{5n!
*>q~24}ggK6FYuN*x2Q)hA3^s<~3Gt76m9LJ*D8UT@fhOD$M(}zb<|scxb3X2EgMhEHN5z+J8cZ?icZR{mc8?B}Wu|N&4g4o7CU>
7?3k;BAvbv+KoiFpfKO+mpxB+NM*A&73RZ-Md?mJh9`qr`ad5TR5ZLWOz~;|Bj~PxP0XYuGU-cG=SA6aRO<?g)x9I<xP)Z*u7q9I
Hi=t^MeT?`x9q4@<Y~GqMQ`=xAI+1ui8N2*9!9b`5ds6gV5~ffnbDDd<hMSZ@$|t#=+~=7+!H1^Mq*^i@t_#5Tv2x9RuZ;;FVyo9
6vaxbZbmQdVUSZr3BktoDG&|q0yMr8*1&YV*o+R##%MkT0XoCrH<Ge>9b!@2yViXzOb~qPGhwGO8V*v_3V@iU!F>FXUQmbZ5}lQ3
1rbhMqD=drU51wU4PzUq0f!B+I~`_#F#Mno6K3y;w232&zsgOa422piliCt-yeN{D9J0I%sR`2tOPAKxcwdw9%=Uo;hz)YYzJLrI
jlg$a{TzvVyU1U}LH8oIkZhZ7k1cn7Z-YLU=2HV3!WiF=>fzbJ4_%7IrFoBl6R+RUMi{OVwj7TfUEKJEIG140_mb(Q_li4t2e_bA
Mo!Y5%i{QvRq!uEmP};b4eCy@V>>w}p69y54vs0i%UU8iuKDfCWs0g4*pKBbxTdI^M@;M-JLX2`T>SOB!id+wB*K0#S|A$~dfLvK
>R6SibJ)=>_xrI?(wc1|gt6Quz>L!=z**Wf?xgK9Y!`WLyL~XCt0Uws!(5cH7w)h?W*6y_$?NLVB??%qo#zh9&j{s(5Lj~|UdU%C
6w@!8VBL)H#l@V#(e>bWuG4G<&mwHk?hD-*K*w~%FTe01kLETc?pS0;gM7>p??^K&E&}kA&hK!br;KVfA`{C4_)d@lv0e3vU}>E#
!JMGTp7ykT@&d2K)R-qn-hvQg%9HUak?0p_PMdh&zrPwCpD_WWnr9AVu|06^B>}xAgO;$!!jz!;EB^@cug|a`8A1Wz!G|Z&Fq@=m
h#r)M<THF6FlZ;OAnFU@T<<(h{ax^oCp)tvI&so-_96AzZ4~<9^KKpO6_^ji!+g*2aD|N&o5wM)t$=t5N0-^ROR~EMIyWTkasK=^
=`+AMKR}JOt9j6mAzI{#gy!gVf3wdf>o9&%Ku!Z*0V7BE3cng-a#I>lNKd6GTV{`f)#D3nCd2u9)9?i!AlRTALupqP%+Pt^3cPuX
a!-9lOP~{JJn0M_#*U1PNYSTGRXOPmN{a`HcdXQ3*#z;c_+oxf!|1R7WA<TQfw?io8+JL53C4>>0y%%$%=LEECyW706W(NDqyd#B
s%FKktl{zkNFXT0_k)fh28Y8CaV&dz8|~KME1KpF|9#Eu2O!SUgg=_p@J)+G+!8TV&&gOK$^?vcZ-p4qYAS@<MJ4gX$0vI<y2COM
FLqW)Ot~C&E6o~X8mqy9d8GMUHsmf9nE4GBiBB)@+Cm)Vy7vy&G$8!oZQ#Zfxc&I{>3guCx~k;2LC(QHNarJcACyKVmpeE8oD0fJ
=e?u-b-wk>D;2k)N}Dz0R@u%WR<M6kYDU+s9-z`gO^%{kiP=UKg=dW+PP62)lcC*`olg;=?R7WrsN$A3nN6Kh8x_}i@BU!9@uoH0
o>g+Pp2HE$h$p%K>;M&h#%}LAsWU6SnL#1W89G{Up&DwZD+_JQW;z;-!Olahki;??P~%AKmFwhF-;8g5sX{O^fX4vQilYBTS+Sb~
01dJzV@Z(-sSF5qC#ONpkqG%Kj$L=kC;~jkm6wbzS&~meFc7P^SL^eAtd>)DaH+Y|e&vD}fs6U}o93r&%KGhAlmW6%RA&bYK#i>K
6D{<RS^DTTea-i^XBrLtZSWzEnTjQ1Wo)V#S8-iWJ`#;v!msi`Sx(wX_q8LJrF{07!!cPm?s3e8*XTEZ4QJ2Sl9P9!!ri5eQ}(OT
K%$BivWXoK;$$a`_S^<)`{GpS@N!3WyFCv<)PhjaIlly`QeP@Q7SM8gnDtPHMq{@P_`%UGTRA5Rlc#Y;-8y^RpWo!N8>P&}j~LGj
`C3lA5e^Cq`XAlQe-fYn_=@9SJD$KZF|`#>60_|ONUIHm@Y54G5vBN|?023r=D9_8v71`sGCEPU)q`|-^oKp=ntKK}R<&I_8V@6F
PmdE+(>0Iw$<ddB8tkq@DAm7j#=lhWsL<G)FL)alQ0#6xul(@r432}8kLI}wgSeY{$BGq590Fk<e)3mM_N9zP%4ZY~l*hMT4vaJo
cLTl4-GT-o9THrDv6p!ofk-LeUfzHRB~-_zl8P!Z@u&4nt8=!oG!5Ga2zIAP&?u+IF6$Og*DDMpON>U-MChJ{)jpb}E?S8$bAPQD
H@dZyDC4ids^rUR?p)(%h21^$Ac6@Y)GV(VXsC>c?x2U~bYEP{{wPDBl|?wn=uL}Dl_5lYGl&7eKfN-MLm5R}K5zSXX>U1mOgjqJ
KHN*p;#V@NtO3P|+@K2PWStdUDJQ{lUOmlmxRJ2UMJOznQ5VUW)LW3&O!{R2DtPGGRk1&)AZD5-kGF?rbvz?F31m=@&7o2liZtj3
E)oANV97)13Q>?$sYwQu*E5d)yCO4|(jI(NmaeImFB6WGJlgVHiQLNlA5E3WljQ}9wH7bu)L-S=bJ=reS>A^6gNsyA_H{%l!?vKi
JK5^WNsF+fJ2g#}mUU{BYll!(<=U&@RJ`>eOH3R=sGS+|mr^kwkwz%q--@>ix!zg`FJBD<awr>818Z@owog~pu?gIEzXh|i!*V=!
p5fmS)mSc5?bHDIqt2s(fdWs$3AXTlaMd0Kl~?V?u)`tafCX5?rsoZf0o2B-Brhmh@zHMQX%!I_Ct0kz<2$;Ue?U1ZkO*2cy9oMu
2^5UM6(E!MLp5$`(E)|@a2{qH=+_?;3<8miN^zH5pm(7}zd73Nyw$c${u0MCq{gl<5bm-W$#HzgNFAS|lD`0*;+@M&g#@c^Qg|m)
U33Gii}>J(q?GLFPW#*XnR~30Ak|oL2=b3g;?sC+lQVTsU^UY{p~Ht{*S8I%tC0k#xa3LsL@Nz>ddnz{&H=;Y-3(TkrGnomj8`v`
jLuv)OD{9mqa^GF2bgKQHNB~R)_nklF!q$5iw#HQkwVqGNr&CmqFyS$HGZaw!6bg1&R;pl?(AWaYVh573`hVt=L4mO-<G2_a*1L`
O8ef0?IXGzA%FFtZ8GtrOcbE~Sau6kcn~4?Y0bBipmzjdc2Ce`I|>)Zn?x?qfBEbnbg_;{!bv#8Pi1kGU#lY48p^OeG0jL>vOh<n
S}WE#gI&U&<l;t!SeODDd+a^f2gn~XhA3PbZDDdzPZa+|V{l~K-V$}1q$Kd%%dqk;_%&xb+JN4Na52HeofXRIv_psk3PEC0L)U?K
wF;l`qvHDvL_}MaK@Hu>&ppkA-dKwJ9*(EkeMgG8#~aaM$R=6<;je8irZp^rDsuWM?u>c=U|a0O_y}-LJ^|XPrPQ;4i@3w=H34iE
H0T*O%rjm_mLqwna#-Z@sQOIhwA6{Fd#&+!PO2$()_MMf04s{Lq6|Gw30c8~JINKQb2iuULXzF&I!G43IbN|uWOm!-)p+ifVgY^I
G7gC2*ZuU*4I?_fi14Gy#({$MXXeqQo!$p!${YPLNENj%kNkG7@VmPBcE^|{rE`ugI?2UfyZB2@E<nR@8Zl5*-<Z;L9B+ajSoqC+
9qy=4+89?nONa20HF3c2*j=Js<bP65${IP+<fmmx?Mzpdu!i8XmM4lww4XyV`H@scrl!_oI|lOEe<3Z3Va|ZpbTU83Ty`WU!JnV9
PZLMe{a1YE#YavEut;MsMi*SpQ9n#d-_jRz@xwadO_%0E+PY5He2!<4mbk#|n2)5%%`D3JkoHVA;Q=rkB?OID9O&Dr+=hd`C@;lK
M<i?fj?;QG@-%*wHu$r{Igmvf@JtAeGeXY#nL^G9#5zii$bIVu!))i?4B>=$9LJXs?*&ZzLuf$hE<TXI#RjcmG2;Nnsy1T(^~F!Q
gAQk|m{^MUlFS!dBiPLMpn%@>&k3o>4iMhG?r$ZG28sD<wOQc$#P2wKUAypy4^niL>>nnuF^jD=nnQhF&Gm`QHS!QkBwM;5btrHx
%n!ZKRM*!B<(~|YmJSuyV7qzld@pJY4iu8vV4~VTwxs@1rfnv9+vRuAfJuZbK|=Ut(iy1hS}~mfS#_fnfm}4-Vus`-3zx>`hVaCm
3(?5!@M0#aV{evWqL*q0Rhy}^5e{#`Qdjd2pNmv%rdr_AU`V_?ukhMm=JX-REhfJrxTlsF0WXXV0c+0|P!q0u9B(&xclSyH$|&6c
OYeP#8fu@@m%wzgGzki1SlvoXsdVfBzZLb~c6jlQPO1r=#jF3kEsxn!y&J=VxOvh2I46<8H0Gki&LUe(oAh&}Skz+nb9}Q>hP#(?
jKWdlG=s91snccsk-@2ihds;dw$n2(LKd#RdLulZnf?Xzk9bHVvwH+_f;O0zJ^{aLBkczqDJ8(mcUj)RaM5>0)E45lyJAZZ91lu1
ZAe9WkhN3*Ydyr*>WY;X#z<487qvL^61>=6==s78vR~r*%6B*5*BPE!8i_X=EjnOvz{7jRMdw%KtD~q=CK7aehNj^z9OeI)M|e_J
!)GIewoQQ=Hle5h*NbkL)`Eg%Di3b)nd$drG!@)iN+ARQR>^?7>}BT?oJrd*N1xO<+DDQz_eyK;j3v$FG26(Eg0em#Nn@ZD5mWO3
+)GoMv%1!!$q!P)u#rDH;J!1izy}<1LW^Uq&<ir$dRzl5<J`_JfOcUoctscCtjklJ(N-o+V%E~0hOakjWx&<?V?MDEv3{*U94oxr
SAs1=JtXjD+iC2@))?z)$Yq)wCB7^1K|~<`^mqelL5K~?w5Q};&7?yqVHzkkZp_Ak!6lVQ_jXl(U=5!^U#j{`Zv&_5Z(hjrG<$LT
lE3i$nxOXXg_z|s(+pm^HNG_a^3&Nc2kRHfFl*_5`W&LS)*LR%W*8R~4Gxnj5}S3~TvU5f+51X+KjP!-&=TZ)bh9SU?VS1<a|k>^
j8wc5VfQB~sT#Vo(chdYIn}bOwk!|H#Upvk18`(|=Yj5(lqM+-sTqgHnf@wr51J|NV}E!TU<Q3eA!;iRL)Mkuj+mHMzwSyB9xm$9
u8=<A#}-E__E%yvl3|ao&}}HW@Ut}=M@#<>W6RnKO1@@0p?~O?+AiQvEeNu^2Yo82$i(HpYePp1u74PhWOZE&W5Eyzx70m&m-BX;
%ikJ2omPzg)`;%hPpjs^pq}nA>|NtAAY5GuLBg-O%EP-zbt~MLk9{)aq7t+wFrhkIap1W(6eh>-xbwkaK!9*bL8phy#U)2HQn0wh
P}uI;0*(HadiMQ>kQy>N+p|hWis((3ez8@RdHoHG=!%i`bIMyN^Tmk0R(k_7s6sRQVL~Jm-&8%$z7XS40H9xpRY-4Kn_VEs2|1~v
B$duBzYb?Gm9e$bQ-AkRqYsl_%peUXDpRL`1_>AJlB6hI=-tq8nx6yCkrKkMlU8x4t>-d8%R0^|jajH@+mb+Na$VJQESs1PL_PzY
sg@YhYRa_R_XY=~34P7#fIl%&bh^T3;!~#U9X$iLie;NOAz3*Y(o${UL8{kJG<mcj#ksiaaTy04<tUb5)V(^v1z&5)J!reh)cO$7
ca^&`(y^=kD{XEutOv2rHYSvYv@(S5Shx*$x@`hOba`>BE<fT2oPp{+IG(TT3x5x$N%Dbi#4xd>h*Wg3X}1~uMKH_s^9gb?EPX7t
X))C!%0;o}hzR^~vxh;Fj4t4zSJ(bnhLsv$*{Yc)2_2zAvUY6w<Qu}VUVFP}J5++*bV$MiVJJowSYb;Vv3t>5kRXmfJmJ<;D<>tp
tl6jw^e(RIUt1!m|0n65TgvgLTdwh%T~33tzt7EjEUCCTC@A5DzoyE%35M=a&<>RKOFU}VIL0I&*3WRCVFDVO^hz^q9?~l~j^cmw
{Vpol)E&&qm-c8u@}>rqd<M2Q2+X@9HB6~NJXsw=JY|ucM&+EbpNYeMB(TgukpHY*E<!&+6EbNw+4E^G!Zyr)nOM-1w>Q(Z(4dz2
R)4)P&(d{7@*bI3SlM5VcH%;PbRr;doVcakEqD%g1||k#^K3Xu3*3-I9;M3>H2fq|rS7mwYI$dZ{IppqPDyU$cx+6F%ySKYlqS0X
d!S(6w4+}<OPwt;uxmKyCy>OSD{wvhrqwnp@p&vF>2ZOsiJ+p^`6+|Fu63pFK94?Mvj5<MaXHJbhG`d`{VjFcL1fMYRWguby&$?{
?)}a5+hO}q&-x0wXfK@@Ka8fgi5=EUr!TbYfACOmW?lWyqeIA$yr6RTxTR@lKuQju&-lPC7oS})FM<M_pS|O?nIt*p;vq>Ci&Taf
l>=vDis(ekw{+6l^-V)M4}moxkC2*DGWR`-{CoEd(*yvtvb6IDEf>7l)+ps=pp`LgB`jv%xAdK4ULbFbb_$l6axFTr<rM`-^f7B^
wKiD&dwmw~Iap;%9$47Q{)o!7&TJ+&4jvuZK)Tu?RGA^Yr<p42{5Dl!hFp?aYl7&mGHxQM&{%F2%)wgw4pIUyL^k8}iVf$)Z@jX6
;K-?EWkx8NPpTKv`*+0$B6$ZDGSKn<5@AiZ08<+qQo;q~GD<`b<ifH&4JQ&bGs`<dsD|f8{46;ZQkT_Sa6_|JmFAxt@#v$p2YF^8
CA(foimV=23w1FVaiwi3yvw2R(Y=;`;vv8J>d^eT*9RK5nz@sYygjcPt0pJN+qNE1$>aZ8nzM1Hv|Zeh{!EU12VBNLjlE;|ekL)D
b&PlO*x)(lg~{|dUbiOOsXj?rVL@g0oWFJPbIIYx8dJVb98r=dPy44@IogQl8VJ?XxkLWkQDS|t>hNkVGX6tm9U0DjCHvrt!OK>d
XV2E)VBEPs@f^<z10GTBjX`4WE{lyQG(%Y==Q8E)v4sBMpACa`#m5JXrfzyu@Cd(}g9K&Q9U!I0yfyO3e?A;@LB!M%u6a)*+V||?
`Ns^0iD3wfQ-II7nRlMO6~PgP3Q>hNdQ+7U?WfUts5;(VDwE?HldElMZ5eNW3jj)|$=dj57$Z4MqCqt0?@P|(Q>un@%JiL2wRS*j
8e-l09qGUqFX!gkNcB2Y#RYUXMc~5L3Nx}$e*QSQ8Q#gtwb|mi>b}%;u=z&#MC_N&2s`iu^i57}NwNf6wBAyDgSD}tdpER1H0Lat
*yZ1v_Vl~4YnCuWVMGQ2%7@1W!+dB&&?clwfi|F`W@*J?jW6rO>Wv~1Mq}8XRTEx|48K#rUKZK2j@LnU7T#DhjfVSQZ=>@Xm`x68
yxC1)LIKF3k#C&7S0e+kFElO`PsZR`yiEQiKx3`tptffLFU<%GOCV>`M(d-#T7*T_BQ=odCBrE5=rPgsn66<j@}cN*yp}bU&Q<$u
m<s#j@md_73{7i2mUc?o0qNjMn@O)p*Y`bGA6Mnz8I~Z4I^LK7YK3|4V)L38y?dLeK{+U7&8le*bMME^*z7RVn)_@L$g_Dp)Re9q
d>~TU667EP2bRh)Sw1Uf&2F0&O&;Aw5Z1KFot*M5WGU?Ci8eyhCYhTnbb<766%%Uoe)(ZgR~SiEp=5VN?vn-%@<ldJos+CruGU_R
cIILF5T6?QSP-XbZN+8>o)*EUWj=6#z5IadiNI8UNnIPvEYw^-^-I=G7GPyP(X#pw^6C@*a=byy7<-`z<FI5o*V1=VMRvE4cKUf<
+^j(aGp2t09RM19+*r@+{|{2AQSbe0h~tQ`qn>0!EJFp~G;tGdB*{v)^7mt0uwD^T1FpxSr=>DWUUzdQzY+$(90!c_xWNUfIgg_1
U`k;gB$AZakRP&Rp=2$%F><#D9nxn&?#s*hvryS76MFR2NzUo;l@I76V|JA7+zxX)%{1-#f?(i}9(^4>ek$CQ<gL|PS*j}}qVKp#
up~88CcK98B6rgXKd{7>&4n@HwXF;{2+D(T8J=ov${|iRxecl|zLOk+D3P?rp_K=0A??|8<5qvZmmeYae`xJGyctgXVK@q>y~h>>
HAN6pnvrh`uf+KdJ_9s_a4GzyfW5>WbV?kb8Z~Ip{u@GPLMsk*XWyZv=)%nXE@f9HLD#<n)c6$8Bkj}Tt(v=X>pc~25kRVyg|viz
ogl{;kF3@TL2{BI_mE=0*_}NMDLK2Ny<#db<2boh2gfv<zGk`GatFr(x$j7!$9<vT`N{eOP3+bPtvOR(uf_*=oiEBLck8~Yz57M2
{7FG>sGngxjaIzNXHF#HkRN6$$2tNB2!3mWoc{Wx5KNrl>&5`mqghBN?RxakpE{5@2qN0-)^b{2H162Ufcx4#Qg3P~Ie83pPn7wz
7oC~ty5tW`E?DOxh-zz#o~<W3%@j(C=W};UmnZaI!htRmqd2tbShkh`ngnsEt`(fO-N%N>G}DsEuP+)}tnW^s;g{uT7jmo2{zCqP
I+x`U7b0&$HgJb@_$%lmaIfy0!|dj%E=W|z8`03R1Yxc^WBI}WS91TjnQySleC%Uwn7&&E9z{22r`uX}@q^6UBj#;8CjcV2&{%jZ
gaG*lIkcirK|e>!z1dAH%`z5}Z%c=VF#;}&(Xa-k7825(H?Xx3S@Zv>e-5%@4a#>RN5;(faB8PdO6%4ITJH6dpA;O`4TjzZO24ez
BMJ>#K^KEZFzO~ZZOA!Hmunu}RZFS{I^TRGG(zp9T9sRQU`+LP8Wvr2hCogpAh{22c`Qjp&@oxK&9Ordx&;t8y2sP`24YC6m8<wI
&WCx*DINxBrgwbqm5?KLrgc<HDF#h_P*aIi(@NWPRj9DFMR}N{QLfLQn%?Nb$X!xz#s@sMV@UHHwX>y@fxI7*&+mi_*-s9@Iz|@E
fa#wj5IerM-$=y^%7%VYS0$>xE_T<ElA7T^JZH$oLz+_3CE{S=nWnJdBi4%+4+_%7n*Z{c)*+ZbLhmjXLJ?jvD5bON0|e$ei&l7G
UV1Z8)7AI$k`#u){c|Ce#02s>Jn5kAgYGNAb-ODvS9gGj_)HNC#6lr&o6~i$HP>rd`7y>HYgm$&`#U>Ad#p|gOG|(1tx;qpQ+r-r
aTWk0z1Et0HA^`w+m<_#TSTg;vFbkn^vyS@EJ`#FM(t=y&NAH&$4|q3Ejs@!rZl>qJ{zBc7Cq-iPe9ZcLx<5q{ZP6MZUo@PrmKdb
Ov7H=v)oT_Rxe;=uE8FxcvIc3Dr8rH-xS4lYGfG|0!Q4hHL%GAX%T`hZ`3>9=xXRn#eEAU!%S6CHS1<vgT}D;r1?V3`u*TRA-E_#
ubOH~%n9!z!&Y>KHI#L<)TdppzW47DB@k}r{ZP3GrQg^uN+PGzx0{!#g6e_i?YgQnjjLy-ceShVsgcp4^u)=chbJ|rkWrAlTM(qE
5XrFdVr>V((WpoEm$i-WuelID%^#_XHi`v)WSi7@l6fT*ev2IJK^E=VGd+F93zZO{6#^_LnsWQzbk<c2D<afJK|=bM$aD%Ms!YLL
^8-!Z-^NqJ_l^AWo55IE!7f}OOgpKFdTd)eSmV;Vxs3?L=lvbf65qdukD*9R5PtaEso!5biw^z{V*V@Yi~p0-l$d~a1)EAyB}WN&
UMtE9phvmqS~5zYg_eDDNDw)Pw++U2fD%kSeZ<am!76o)0v9+i?h>{bRoRq4v=5jQ9#ED*;+C5F$auqo-hghWMiv310{v4*yG#Cd
I;e!7Pr`+JHLxv%ZaYiTrFw`eYQD&Vdm(?~tc+hgWKe_I@fP~}FRBxk<A33m)Rg6ahty~K*<?_;?eW;c6%cFc1_eoDR?Qz=vvrSG
{gW}=T}4)l0Qjz$8f&ve8a;BcqBu5&bxP8Mosfs6WQ|xNBKe+@T_CQW<~1AOM8z=)ZX1lBRTii9N?Wc$$ESv_S3G9tAdN8-!v9R*
*BWw_0+hEKO}e_kpS2y%e$S?;gmlz6bU=iMCqd_EP%bhqA$P@_-%hN|POzBjjW<=r*Pks8A8M3y24POA3%rj~@VSAS;e7*iUH&Ek
@s%Bd%p2hl72>=A!;guH8Inwys1~%kJ=4D=cyDvQ3G(8C-vIMuU?<a}n}`#(Qa_C&OMtNpU#605V~5~N3?=zvPUKBIfCr|WlOsQX
jzbb#otHe7YZ%hOauN%ag2yeoAC!<mQW8I{(%?Mw)$$^qNxt`#=k^PzUmm0r7IxP~vUiy!hRX5=`~GJYSG<E3;pYw)-&cg<!*09+
@^vBwqJ>|*F2Ie)J6(;3g{BkBsm8oUm`9J@RlY}PMZ8keVVV6OhGCS<lUTMmM*xwcel_nNy_g19>arnZf`b2yl+00b$mN>16N;uN
l4H%OZgeb2W2hh-<YTwciN6gAqe@zoAnyO2sF|~@>@FA}xe^s6;t*cm%ibZ(hcRdpGc`K(4fYtdk<$}3P@1`xl%Ym!+hUmO$6LA$
S0NL*Eza-6SMEL>-otXIVe57Uamo`(`(mr#`HjVJy%&OuzwjDF1aNs21){`-yy3=oXeQNhqz<}z+h}Q_)Qx^(!6DiKUm6C=db8ou
>kSHHY@k>EVaZQbBtH|FGGG%pAn)o!NJ5baHk*K`Sve(Hly40kO|KtNQ5Z!$;2cS<=}Z?QV<JJ<nk>;{`2o?O-%Jg4;bLf)*`3HS
N82mq^3C32hXpkRdM6>5g&+ph3tAdP<_XD#2`f6=dg;+#XzRP83#mnqt_~DYZ>#uTu9gyU?_KeIFSaBH7;8qg=)TR4ZN+A7R0&m_
%pTxBTzc>enMQw<pYBx^XLgFn;X9RokgR?ke*Q~RWzsJN$Rc~I1P9xgY~I^g*Xj0<jM_xAUzhNB9_bsQ8MR&}SoH*Fm-_6Mt~9--
0EQ)*J(||5D9ZLpv`es=aHrfQO4?lc9MJ7&Ch6;tBe3AmVSElWakK$a>7_Bi=JX7bp<u;Qk|+I291HAF;TFhbG2&{<Ydn>@6)+LF
98$(c+D%7|pUEcWWOMGxgncHVjrr?576%P#h&g^zQpg$`=naA`Z_{KHEZ|2XIZ^Ljm*1#+(W{3(CO?y5mRGdANj;|YDlEN#ifnFF
bR{w7h^Ut<Tp7%b*s^A4bc6e<9`fRiFHb&|yyun5WYehm!jWeJil$95C~s?lzz^fHwa)+N0|5nYt*rZkuN5fB;@MJ+3#M(K=n-jF
;L*tX%%9@jT<I%uAxpTKGcNQMZ^l!Gb<oVQG?dMFOs}Lsos7<F=P;edz&!_?Cg-LFL>IP+ERE*Y3#^f|n@;OLF0JAT9e22tSp#mm
u?7<ehvuhvKm&Xt00000=Mnze)gum900Eg(?&kpjBIlU}vBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw)==29678
assert hashlib.sha256(raw).hexdigest()=='4cb82fbcbeb9582868c0920e4803570146a0ca5e752706839bdb8fa818faa282'
files=json.loads(raw);assert len(files)==7
root=Path('sq24_np37_mn41');root.mkdir(exist_ok=True)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
 q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
print('SQ24_NP37_MN41_COMPLETE_SOURCE_RECOVERED')
```
