# figure-0339

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Rapid Raven 11 — physical support motion and a sparse homogeneous monostable endpoint

## 1. Result and acceptance boundary

**I did not obtain the requested homogeneous own-centred strict (1,1,0) polyhedron with E<500.** No reference-centre certificate below is promoted to that class. The strongest new homogeneous endpoint from this direction by total equilibrium count is **RR11_P35_R9_121**, actual **(V,E,F)=(66,99,35)**, with **(S,U,H)=(1,2,1)** at its exact ordinary-volume centroid. It is monostable, not mono-monostatic, and is not a Gömböc complexity record.

The physical chamber experiments also produced three fully recoverable, twice-audited reference110 bodies. Their actual own-centroid counts remain substantially worse:

| Canonical endpoint | Actual V/E/F | Reference-origin S/U/H | Actual-centroid S/U/H |
|---|---:|---:|---:|
| RR11_P35_R9_121 | 66/99/35 | 1/2/1 | **1/2/1** |
| RR11_C2H139_R12_REFERENCE110 | 261/398/139 | **1/1/0** | 9/25/32 |
| RR11_C2H165_R12_REFERENCE110 | 317/478/163 | **1/1/0** | 55/79/132 |
| RR11_C2V157_R12_REFERENCE110 | 155/456/303 | **1/1/0** | 91/59/148 |

All are actual bounded, filled, uniform-density solids. All true edges, maximal faces, ordinary first moments and equilibria were reconstructed exactly. Both independently implemented audits completed for every row. A separate fresh decode and full cold replay reproduced every canonical output hash. There were no weak equilibria at either tested centre of any row. These are independent software implementations within this investigation, not external peer review or proof-assistant formalization.

The journal's preserved C1370, E685 strict110 remains above the target and is not superseded here. I did not create an immutable parent identity for a late preserved source. 

## 2. Source-authority correction discovered on actual replay

I recovered the complete late RR11 10-file/30959-byte source capsule, SHA-256 `95656eb0ecb60c48f702ee413925431868e02ac097319776b4a8e5a7fc10cce7`, and executed its complete replay, including both exact auditors. Its observed receipt was `RAPID_RAVEN11_COLD_EXACT_REPLAY_ALL_PASS`.

**The old handoff's prose volume/moment/hash tables conflict with its literal executable capsule.** For example, the prose gives G32 volume floor 851669459055772 at scale 10^15; the literal source, its own expected.json, and both executed audits instead give **851631977020541**. The capsule is authoritative; these are not interchangeable definitions of G32. The conflicting prose is visible in the journal. 

Correct capsule-derived values are strict intervals `(L,L+1)/10^15`:

| Body | L for V | L for Mx,My,Mz |
|---|---:|---|
| G32 | 851631977020541 | -8647518142367, -1633294742330, -74159384167868 |
| T32 | 865405805885937 | -67722787475, 31293585269108, -58443627155644 |

G32's canonical defining-body SHA-256 is `5c9a1c3ac58037785d81be9802b84c5f99b671a6208f9d820fb630654b7aec63`; its identical A/B report SHA-256 is `0f402b0b2712b4e936528684344ce48eeedb4b16b6850c06612aa5dcbaf9e871`. T32's corresponding hashes are `9f3c16b828814cf1b2ba2ed3105c85075ef617df697d00c0637933d8f792ce24` and `a9c095675189cfd4e4c10e3c5eaa05ddf503063e0a6c46f0b49acfb054c6a2af`. Their equilibrium counts still agree with the assignment: G32 reference110/own13,24,35; T32 reference110/own14,24,36.

I also recovered the complete SQ24 source capsule, SHA-256 `6d9c0d51af19b83810077f3276db5445892e3277c62442fa581c6cd6cc182416`, and used its literal R83/AFF83 geometry. No unavailable WB24 table or defective illustrative GU22 face list was substituted. The exact checkpoint tables and cold-replayed hashes in this handoff, not scratch decimal summaries or exploratory serializations, identify the four new endpoints.

## 3. Strongest new homogeneous endpoint: complete P35 definition

Let D=10^9 and let I be the following complete ordered 35-row integer table. Define the physical solid

`K = {x in R^3 : I[f]·x <= D for every f=0,...,34}`.

Its density is one. Compute its exact ordinary centroid g by the finite determinant sums below and define **P=K-g**. No rounded centroid or point-mass adjustment occurs in this definition.

```python
D=1000000000
I=[[2230877646,17192027236,-19817197483],[1264771841,18603166963,-18384681721],[100457689,20127124780,-16395850948],[-1121531015,21506191188,-14002078712],[-2343195682,22626775000,-11269263232],[-3519515004,23407011684,-8264311275],[-4611556634,23784306359,-5061629691],[-5585336642,23712820902,-1742859179],[-6412092164,23163445205,1605240510],[-7068926025,22124355782,4893636742],[-7539447586,20601454595,8034161824],[-7814236857,18618369036,10942674299],[-7891045809,16215870688,13542038865],[-7774701522,13450674338,15764763490],[-7476711597,10393646887,17555177121],[-3613544786,1123559440,17490359428],[3903927012,-12137249553,6047863738],[4952366564,-15527258498,2897095658],[4208439955,13078948078,-21880688194],[5254742120,10345971581,-22713812390],[6229397967,7321839906,-23252414040],[7087714949,4090951168,-23432506833],[7794030340,741097231,-23208728400],[8320285044,-2636224654,-22552069183],[8646022069,-5947896050,-21449551636],[8758721970,-9102118562,-19904329961],[8654084786,-12011618603,-17935639634],[8336087636,-14596780124,-15578347600],[7816743736,-16788471906,-12882003183],[7115544198,-18530401903,-9909376982],[6258600904,-19780890624,-6734529829],[5277532813,-20514012565,-3440485203],[3717237860,-20342616720,120332706],[-452169826,-14823563997,3538482907],[-6254567396,-2372270227,12629561396]]
```

For reconstruction independent of any historical parent, enumerate every support triple `(a,b,c)` of rows of I with nonzero determinant d. Its possible intersection is

`x = D*(a×b + b×c + c×a)/d`.

Retain it exactly when every input inequality holds. Remove duplicate points and sort the resulting rational triples lexicographically. These are vertices 0,...,65. For each support take its full contact set and its outward convex polygon. This is the exact construction implemented by H.py, not a floating halfspace approximation.

All 35 supports are active. The complete maximal-face cycles, in support order, are:

```python
C=[[5,44,47,49,51,54,56,59,62,63,19,17,14,12,9,6],[3,44,5],[2,47,44,3],[0,1,49,47,2],[1,4,51,49],[4,8,54,51],[8,11,56,54],[11,15,59,56],[15,18,60,62,59],[18,21,57,60],[21,23,52,57],[23,24,46,52],[24,26,42,46],[26,28,39,42],[28,30,39],[30,31,32,33,65,63,62,60,57,52,46,42,39],[33,34,45,48,50,53,55,58,61,64,65],[34,35,36,37,38,40,41,43,45],[19,63,65,64],[17,19,64,61],[14,17,61,58],[12,14,58,55],[9,12,55,53],[6,9,53,50,7],[7,50,48,10],[10,48,45,43,13],[13,43,41,16],[16,41,40,20],[20,40,38,22],[22,38,37,25],[25,37,36,29,27],[29,36,35],[27,29,35,34,33,32],[0,2,3,5,6,7,10,13,16,20,22,25,27,32,31],[0,31,30,28,26,24,23,21,18,15,11,8,4,1]]
```

The 99 true edges are precisely the distinct unordered consecutive pairs of these cycles. Face-size multiplicities are `{3:3,4:20,5:5,6:1,9:1,11:1,13:1,14:1,15:1,16:1}`. In particular, the stable face is a genuine maximal 16-gon. Display triangulation diagonals are not true edges.

### Exact ordinary volume and all first moments

For each outward cycle `(c0,...,cm-1)`, use fan triangles `(c0,ck,ck+1)`, k=1,...,m-2. With the exactly reconstructed rational vertices a,b,c, put d=det(a,b,c). The following are exact finite rational expressions with every input specified above:

`V = sum(d)/6`,

`M_raw = sum(d*(a+b+c))/24`,

`g = M_raw/V`,

`Vol(P)=V`, and **`M_P=(0,0,0)`**.

These sums are also a compact exact recovery definition of the volume and all first moments; they require no numerical root or unknown scalar. Both audits emit the full rational V, all three raw first moments and all three centroid coordinates. They independently reintegrate the translated filled solid and obtain its three exact zero first moments. The unreduced decimal approximations are not used for centring:

`V ≈ 0.0037924151018589726`,

`M_raw ≈ (0.000022493904244706964,0.000006288419062864104,0.000010557387216392131)`,

`g ≈ (0.005931287488461077,0.0016581568456948807,0.002783816363144713)`.

The complete 3591-character rational volume is reproduced in both audit outputs and in the supplemental Markdown handoff. The inline recovery capsule below regenerates it, all raw moment fractions and the exact centring translation without that supplement.

### Exhaustive own-centroid mechanics

The exact stable-support list is **[0]**, the unstable-vertex list is **[0,65]**, and the saddle-edge list is **[[32,33]]**. Stable support0 has cycle

`[5,44,47,49,51,54,56,59,62,63,19,17,14,12,9,6]`.

The saddle's incident maximal supports are **15 and 32**. All 34 other maximal faces are strictly nonstable; all 64 other vertices are strictly nonunstable. No weak face, vertex or edge equilibrium exists. None of the 396 four-component true-edge primitives vanishes.

Partitioning nonsaddles by the first negative component in the order `(foot lower bound, foot upper bound, first adjacent-normal coefficient, second adjacent-normal coefficient)` gives **[32,32,32,2]**: 98 excluded edges, plus the one actual saddle. The same partition and equilibrium counts hold at the uncentred construction origin. The full per-edge integer primitive values and sign vectors are regenerated by the capsule, not inferred from Euler's identity.

The remaining packet is not a tiny numerical gate. At the own centroid the two unstable squared radii are approximately 0.283810137302668 and 0.328277444942526; the saddle squared radius is approximately 0.005875536508001 and its segment parameter approximately 0.719920783792039. The diagnostic `1-r_H^2/min(r_U0^2,r_U65^2)` is approximately **0.9792976510147173**. This is not an impossibility proof or a centre-ball obstruction; it warns against treating this endpoint as already close to cancelling its last unstable/saddle pair.

### Physical ancestry

The support proposal came from literal AFF83 followed by actual support deletion and full physical-centroid recomputation. In the canonical AFF83 83-row numbering the retained proposal rows were

`[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,21,34,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,65,76]`.

They were rounded once to the printed 10^-9 support grid. This selector explains ancestry but is not needed for reconstruction: the literal I table is authoritative. Taking the polar and deleting inequalities changes actual supporting material. Its physical mass and own-centroid mechanics were recomputed, not imported by formally exchanging S and U of AFF83. No claim that this polar replacement contains unchanged GU22 is made.

## 4. Moved reference110 chambers and actual physical mass

I left the fixed 144-support G32/T32 intersection rather than attempting another blind projective centring of that fixed body. The executed replacement uses paired opposite-hemisphere support arcs informed by R83's new-root ancestry, followed by full support motion. It has different supporting material, physical volume and mass controls.

The arc proposal normalized the R83 axial apex to (0,0,2), joined an apical stable pole a to b=1.4*b0, where b0 is the opposite axial stable pole, inserted 24 interior poles and their half-turn partners, and removed redundant proposal supports. With e=a/|a|, unit great-circle tangent f toward b, endpoint angle theta and t=j/25, its proposal formula was

`need=-25*log(cos(theta/25))`,

`extra=log(|b|/|a|)-need`,

`r(t)=|a|*exp(need*t+extra*t)`,

`q(t)=r(t)*(cos(theta*t)*e+sin(theta*t)*f)`.

This describes numerical discovery, not a transcendental exact definition. The complete rational C2H139 support table in the capsule freezes the finite endpoint, including its axial reflection. Its reference110 status follows from reconstructing every actual vertex, maximal face and true edge.

The continuations allowed paired-coordinate motion, live witness changes, global hull turnover and new-witness pair insertion. Retained chart constraints were C2 symmetry, an axial scale gauge, one common bottom polygon and strict reference escape conditions for every actual nonroot vertex and nonroot support. Original G32 supporting planes and a fixed original-GU22-witness envelope were **not** retained. No unchanged-GU22 inclusion requirement is asserted for these replacements.

C2H139 and C2H165 are actual halfspace bodies `K(q)={x:q_i·x<=1}` with complete literal 10^-12-grid support arrays. C2V157 is instead the convex hull of 157 complete literal 10^-12-grid generators, of which 155 are extreme. For each body the two transverse first moments are exactly zero; the axial moment is not:

| Body | Ordinary volume, approximately | Raw centroid, approximately | Raw axial first moment, approximately |
|---|---:|---|---:|
| C2H139 | 5.842466229891778 | (0,0,-0.2652998698659189) | -1.550005530486315 |
| C2H165 | 2.792140209265972 | (0,0,-0.05118511537028368) | -0.1429160187412868 |
| C2V157 | 10.703208089645873 | (0,0,0.04222078420506437) | 0.4518978390548377 |

Exact V and all raw moments of each halfspace body are the same fully specified all-triples/Cramer/contact-cycle determinant sums as P35, applied to its complete table in the capsule. Both auditors emit the full rational values. Translating by the exact centroid gives zero ordinary first moments, but leaves the own-centred classes in the first table, not110.

For C2V157 the exact integer moment representation is compact. With D=10^12 and the reconstructed outward integer-grid hull:

```text
W = 64219248537875239511479146058817150250
J = (0,0,10845548137316105679216732296610940383392171015018)
Vol = W/(6*D^3)
M_raw = J/(24*D^4)
g = J/(4*W*D)
```

C2H165 has 165 input supports but 163 maximal active facets. C2V157 has 157 generators but 155 actual vertices. All reported incidences are after exact rational reconstruction. No pre-rounding mesh count is substituted; shallow incidences can split on rounding.

### Full-edge and degeneracy census

First-negative-component partitions use the four-component order specified for P35:

| Body | Reference-origin excluded-edge bins | Own-centroid excluded-edge bins | Own saddles | Edge primitive components |
|---|---|---|---:|---:|
| P35 | [32,32,32,2] | [32,32,32,2] | 1 | 396 |
| C2H139 | [142,142,28,86] | [126,126,74,40] | 32 | 1592 |
| C2H165 | [178,178,39,83] | [138,138,32,38] | 132 | 1912 |
| C2V157 | [97,85,137,137] | [74,56,89,89] | 148 | 1824 |

Every listed edge primitive is nonzero. Each own-centroid row's excluded-edge bins plus actual saddles sum to true E. Reference110 roots are C2H139: S[0], U[130]; C2H165: S[0], U[158]; C2V157: S[151], U[0]. Their reference saddle lists are empty. The capsule regenerates complete own stable/unstable/saddle lists, all maximal cycles, active-input selectors, every true edge and every sign ledger. Coplanarity defining a maximal polygon is not counted as a mechanical equilibrium degeneracy.

## 5. Executed physical shape derivative and continuation

The useful actuator is the derivative of the actual filled halfspace intersection, not the volume centroid of conv(q). For a face `q_i·x=1`,

`dV/dq_i = -(1/|q_i|) integral_face x dA`,

`dM/dq_i = -(1/|q_i|) integral_face x*x^T dA`.

For an outward triangle a,b,c on that face, set

`Aover=q_i·((b-a)×(c-a))/(2*q_i·q_i)` and `s=a+b+c`.

Its contributions are

`dV_i=-Aover*s/3`,

`dM_i=-Aover*(a*a^T+b*b^T+c*c^T+s*s^T)/12`.

Then `dg=(dM-g*dV)/V`. These integrate exposed connected solid material; they do not sum overlapping nominal caps or alter density.

The included CONTINUE.py combines this physical moment gradient with sequential linear programming and minimum-norm nonlinear feasibility corrections, rebuilding live hulls and escape witnesses. Its polar_mass.py constructs physical faces from primal-polar contacts. An earlier double-hull normal-matching implementation failed on nearly coplanar slivers of a rational restart; the included implementation replaces that failure rather than concealing it.

At C2H139 the included physical integrator agreed with the exact-audit volume to about 1.4e-13 and centroid to about 8e-15; at C2H165 the displayed double-precision volume agreed. Four central-difference checks with step 10^-7 had maximum absolute derivative discrepancies below 1.2e-8. A two-step smoke continuation from literal C2H139 actually completed, changing numerical axial centroid to approximately -0.252879464 and then -0.249200191. Those smoke outputs are **not** new exact promoted bodies.

The capsule freezes the four audited checkpoints. The optimization driver continues those literal inputs; it does not assert a uniquely reproducible optimizer trajectory or eventual mass closure.

## 6. What was tried and useful continuation

Free G32 vertex/support motion, coupled physical-moment/escape objectives and newly witnessed material additions produced no own110. The replacement C2 support continuation reduced its actual axial centroid error substantially while retaining reference110 after exact rounding, but consumed mechanical reserve and increased the number of own-centroid equilibria. That is partial physical correction, not acceptance based on a small residual or reference certificate.

For P35, support deletion reached the printed 35-support solid. Further deletion/fusion trials, full-support own-centroid optimization, bounded affine-metric sampling and single-lobe cuts produced no accepted110. These are finite unsuccessful computations, not exclusions of their continuous families. Tiny penalty values and nearly vanishing individual unstable predicates were not promoted.

**P35 supplies a genuinely homogeneous S1 chamber at E99**, with the exact remaining U0/U65/H[32,33] interface and incident support pair15/32. It leaves room for nonlocal replacement of the second unstable basin while retaining or rebuilding the single stable basin and recomputing all physical moments. **C2H139 supplies a less depleted, fully finite reference110 starting chamber** for the exposed-face physical derivative. C2H165 is a later complete boundary checkpoint, not a recommendation to keep pushing its nearly exhausted linearized chamber blindly. Whole support/witness replacement, including temporarily moving away from the smallest centroid residual, is a more meaningful next experiment than another unconditioned post-hoc projectivity.

No global no-go theorem for C2, all projectivities, all sparse chambers or E<500 was proved here. The requested own110 remains a constructive objective, not something excluded by these trials.

## 7. Independent audits, exact hashes and cold replay

Audit A for halfspace checkpoints enumerates all exact support triples, tests every input inequality, reconstructs complete maximal contacts and outward polygons, checks opposite true-edge orientations, Euler incidence, cyclic vertex links and rank, and integrates origin-fan tetrahedra. Faces are tested against all other supports, vertices against all other vertices, and every true edge against all four endpoint/Gram-cone inequalities. POINT_A.py independently constructs the grid-point checkpoint from exhaustive integer supporting triples and integer moment sums.

Audit B imports no geometry helper from either A. It constructs an incremental exact homogeneous-coordinate hull, independently groups planes and Jarvis-walks maximal polygons, and compares the complete maximal cycles against the defining body/support data. It integrates positive tetrahedra from an interior apex and separately reintegrates the centred solid. Its stable test uses polygon-side feet, its unstable test uses incident-edge tangent cones, and its edge test uses the radial perpendicular-foot plane against every other actual vertex, together with the endpoint interval. Thus this is not the same Gram implementation called twice.

Both audits completed and agreed on exact V, every raw moment, exact centroid, zero centred moments, full maximal incidence, all true edges, every equilibrium list and zero/weak ledgers. Controls were a regular tetrahedron (4,4,6), cube (6,8,12), and a rationally translated/properly rotated P35 with the physical moment transformation checked explicitly. After freezing hashes, a separate fresh source decode with no copied audit outputs completed the full replay and reproduced all expected hashes. Its final receipt was:

`RR11_SPARSE_PHYSICAL_NONWINNERS_TWO_AUDITS_COLD_REPLAY_PASS_NOT_A_GOMBOC`.

Exact dependencies: **Python 3.13.5 standard library only**, assertions enabled; do not use `-O`. Numerical continuation: **NumPy 2.3.5 and SciPy 1.17.0**, one OpenBLAS/OMP thread. There are no required external optimizer checkpoints.

Canonical input hashes:

```text
P35.json     1343 bytes e1d481bc4f300ebea454234bfd00dbc2ca1323ecd426bcb5e92b4522e8790b9b
C2H139.json  5903 bytes 819c810ed8876078333a8f64d9729a4f0d8f5c91c4ac7e32afecdd20438dd002
C2H165.json  7049 bytes 1cc1b1f8836494b9a63331bed31b7dc9e9e231dee4be8182dd90cff13125d5fb
C2V157.json  6845 bytes 80b540612102e5c06eff744fbf11c6b90d5cb124d621f5e8dc46f4eb91c087c0
```

Canonical complete audit hashes, also frozen in expected.json:

```text
P35.A.json    def4db009735232a2d4151cc9c43e7e94ef8a7202a859ea8c78704ec62d0051b
P35.B.json    fcc6863b3f3745f1dda994ad605526ba23dc7ba11289c394dd5a224a87ae3633
C2H139.A.json e850020277a12f7558a9fb30290b5959ca199ddb6f2d58774e8ba435bb0b8877
C2H139.B.json 928e257a67df8cab5da2df7dcd746c40a4a2adc33b777669da491b41546e9981
C2H165.A.json 5bc7208c7e53051940038a1fd00dbc1fe07112e3fb3c8b4e409837332d433aef
C2H165.B.json a33fc8e91bc86b0e85e09a74beaf01d47d6b7337acdcef1ba96eee0ff92c8f88
C2V157.A.json 16632d70f043e936a13fe38c4837a232d43844e70454d4e97dfd104106a41c8a
C2V157.B.json 2b31e31a494fd65c25f037607a70ea4b340229a22517abb2ea6be2342d67ea09
```

## 8. Entire literal recovery capsule

This is the complete source/data unit: H.py, core.py, B.py, POINT_A.py, all four complete literal input tables, expected.json, REPLAY.py, dynamic.py, chart.py, polar_mass.py and CONTINUE.py. No historical coordinate file, helper, parameter table or secret optimizer input is omitted.

Decoded canonical JSON: **56647 bytes, 14 files**, SHA-256 **`94ad48eec5561a26094d4be7e93db5e6ada384c8afad51a6c2924b1128a6b7d4`**.

Save the entire following Python block as RR11_RECOVER.py, then run:

```sh
python RR11_RECOVER.py
cd RR11_SPARSE_REPLAY
python -S -u REPLAY.py
```

A complete numerical continuation command is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python CONTINUE.py C2H139.json --polar --steps 200 --trust .006 --eps 1e-6 --out resume139
```

C2H165.json may instead be supplied with `--trust .004 --eps 1e-7`; its small remaining reserve can make the local linear program infeasible. C2V157.json uses the same driver **without** `--polar`. Any numerical successor must be rationalized and passed through H.py or POINT_A.py and B.py. A promoted successor requires actual E<500, exact own counts [1,1,0], empty weak lists and a completed nonzero four-component edge ledger. An optimizer flag or reference count is insufficient.

```python
import base64,hashlib,json,lzma,pathlib
B85=r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;N3<>fL#DRh=fApyCOKA=>&TxYSfeU&VmmXm56a~%EH?RHSgwW&n9%dLpb<Ne(?GggEH1w
W3c~GRpDO>y}pjpZ>ShHg}YKgg)?Tv4jyTQn--$)LQvsC9^tSVDxY?kKlmlk0-uhhO5HYqI!fn3^6-yR9?J<8-A|ij^iKmk(S>&_
oXK&*MtABs)lj{vt2_;2-sLf<F!yTRcYsG!2UpD)aQ)&rWJmtY(%4P$Fi+H9;$Pjb@k1`Q*o7LpB;?;Wa~je2JVq6{kS(c}qkhcC
30^WKLYq;bb)(Lpa|%f*vA}zj*IoEr7!N73Ye=w?inrsh>CN9C9#?2p8*!*~6!~T23s*`tV$wh8_`*uo8_PawUx5*5qfSWG2Br7U
_P$7nO6}1@JAyVSV~v_Vovy<>=x@l6l%z)VF$17}lv%^w5hL-#OE1E#k_}u#rzw>yWts7ZOUjM7f&~)hnRuVlpH)iXhM_=Fy-Xwp
cZ}W#%@naP*(e#nMZQDUJlqi=<6VQxr^c=mc7rqfoVi+YX&IZbPS$<{^45Alv5);1k+$lckLjQeHjrL@IG~bHBt85vO3+B@DcO4&
rq%Rpcs+3iem^oM?MCej0{>K|OdLW`yOaMI{YH9yS-=(N_!?dKXTINU=C2E>H1o!Y4>M_CdGneT-UTP`zdX$DDvsChdA8@aeR;BR
0`SuOcLh~Fi-7R*welcg<_I3nPr}@_Nq&*Z6ep~_WZbDq>IGO-q__AMPcLH=MnTT9+)>F1CdFA-L2g~z^Oyk8vqoLzoSXJ9DZ6ZH
(Z9>;DRhr(tCbRlMdGQT*c-}M4~F24)7mPGV<^=GhM83>S@c(RJ4aWg#FFSLL9+p%@UfK7W+BhSTk(JU`twD5-1k^L^<ogS_Xaln
T|ncQUS(7(#^@jnOccyQgCrd?Bi771_fa^i*;Sz7?m%S!Rffi1`S3J$K$;4DZ=@N?RKFC|1!7C;Sw*}YjC_OgmxyQZ#->0aqCv7N
QIMDi7jDwk{SC(7mVuA1IbNI5v65;gj8fJUH${Y(#z65a!MtkuP1!3w4gBDj6%T$%_|T8Z{3%=`F+)+&z;)l;JsevD2W@Je_;yuy
w(T#OO8pb1wB*s4hg41jEfiJrMY+?L7^C+@5kO9-XYF2v7H*V19&Q{g??pm)>Cegc=$TsTCr!NrpLE@7QQJ(J{fR$|&`EpRKi-<F
u{Q)U53;RZ++LH63na_qOwHD$+r%bF&2rnxET%N!X=!;!+iqp2El~KF%wYFn!*P_b*iQ-o^^IIFWpq11VgoXq_^;vZ<w0A5=hfJ6
srGfh=uNkYmxG*i3Op1Zz+G#3wxJ5R`Vfa$03sNl2y5w%EZr&;mLl<Mb^M}CQ|zoJH-pQza&&c!93Mo0LQbGU3!7r)k*mB9Yf>L3
>Y_?66tu^ZV3HutsQ@DLS!m4_1o1UE5QJc5<jpBNE8APMK=Er+8pH)j@<OsIcn3#=m-G!N<)WR^t^9>EB<s1~fR}X8a<*b+|FfRx
93?YSEM7CQkrLu)g9?0Qckg<kDOwVg$Pu+Uz=`2Q2}Vg%SWt>RTW7Q1dlq4G`T}>Q>!a{R#s563`{iVyc<qR5Q*=f;8pAlRRpmH(
Xfao9%!AP9N=i6}FxuLo?0<?)YJz_l8e0<2dmQh>f3SeKR#Fn5fPk{LT=nvgrei*-Zh+m@*8cKVu9aXBOO%DC0ZodZi~Wf+Tofw_
QXz7fc(K>k-_mvji#JF-ZO4WOysAuPsp-=iFy)9`;wmbC#e<lpXqDf!e5oP#ixOY=#Y??-|N9bUq=SDI+F3{9@*Ueahrgkdyb7xs
>lht#Y#v8P6u$C*w;7Uy(amRTkLX3mAaTN_E`7u0o3Qy=5HfLJO&+fUug(K<Q(;<%eU7)4oC86pPq#%RaP3*RjM#&NlGRwQ!~VV4
1O78gq#Hi^)=uDQRGMd9*pUJyB!Ko0Swm3T_0g>#8Wy<iVazNM1I*x@K5ZC`?l_Do!7{D%tL0uz3*L`D#+59n-8Cy>deyEWpq6#$
xOP#<TLG7zwiakLosmLc)ubz~;4C#EkH5g%EYe4XakVl?PffnBV=e840#;W6bHt1S;eXZ{HuExxcytw6@hig!jNqAktX#*}xgJhu
?jT9sSrNAPAJ(Vl$#$CTxFRnK(18}5n^<%q!k*QFM@)b23dwv{zZvaGyz_mXJxHwq+!v((cS-eJI#Zg3u#{Y6BCfLGM5llvlOFt-
#1~{uIz5rE=8E{Nw!@i=IE+pp>&(K1uulnqT*jjIf|ZTOePOnYd_=2QyFZ84_x717_&_~`r{JT&)`Qx*wZs*2_JXVGCe&!EZo5-0
+Q(x>VCXAIr5fIX*Lv?0aC9+D$Z9sXAAMh`_aeJscv=H>cZZ8jXy6cAJNR9)9FYSj6r9Oh6V1Ik%*2(A*;_~q6?%)Lhv7FFn;k!s
(ULJ%eq(9OWW2`K9nA}n+$ACR0U&ZB>yj^hox%MeDaDZw-KIF0YWz<~rDbCuInRbUZ(SUNF-czOafRaXNws+|>tKjIn_~yR2*icT
rW$G*PX5u?*aY|LB68Ih=7%(^>Ty808;;7MrO-6EeVZy<a>!eMh5l@f$tI|mgP}H3i~a5H>Pw-Yq{Hxv<>Ky{_cD*2T53mW0WOzk
h%ZRCKC5hb%5Tlf4GxQX*ie{DM0wQbk<y2qU6)XE0v`&@x8CqU(@G@lSXCkVp8o<g1^6iE)W46+tv(PZPayH`cTohS;fU!T(U>Y5
+E8Lmb}pVT#3C2-K!Rv7`au{>H*gVM>d6Y1NgU$M_4w|EJ9BWw+jO%lp9IoY-s{OMERIY;WGRn1McGj<M`_xE$Tq6Ng{0FZyT|1P
R+!e<EqnGf)55BUhxyFVvBUGWB4eSI^vO&8f!kj()byv7<T%(e;cx>w7a|~po~g@)roGn=x3@0lwk{}`!q?w`P^MMFTtCM314==O
6vq3+I`tJ25<kjA-#&pOOT$+AlZ;yyC%*U0Pt~N<4+S`nRd%8cytR0PlcMiu8-q9UmeV%0w*rRg|Nr0Ikt_4!-a=gUA~IiKQeVb_
3$h8<hnOaKkja-f$kvLuwM%_5b7naL!3`qwG}$+mC`-ca^pZutClXa8>7;w^i6#D;%tnE<wDO|<cSyISrv^!IVGYCJ(4DrJ_#!9#
x#mJG<)>HINsk*<-6;V!_n_}m5(FOG$Tg&2o@3;fKgsrpKFI8%#<V6X5B9&ZRE%Er-%Stia>n_02x7rsFV5SW+Ph{4%R%X5ANI3M
5Knny5R%(ps~zzN5Z3gGBk+5C6;G4SqLsPQd?F5ZpoH+A_~zkLWm&S`+NeE8;R$!cziW!7;3y7NH%V4!RJ!uz1T2~O+|sFi(A7&*
-a{r;<{XG}2{YoHZ_1e-AhAqxo4^pVw~fQh!%GZ0Z#aD2DFQuSy7O-@GY}~heSZ*jONAl{&^6lBeWRG<?ZqAg34v<*GO;KiJmiuW
qjPp~n~P0r+UyBdv3K)0GR+j_%fG&Lv*i*UP1bAeslNdX@o7%4QNtGAJb1r6$#aOU4`;g8r$W7;{68hnrKf)(QlN8t;GPSV_SXty
U`*4)vM6gQbSZZ{>mFLX9p-WGTfe`Wz-Lm3bH7$U8)Bo866y$Um7Q&!xu4inuJ~8%JR9hT!)tw)=nE}sYhR}%ilqlb`aCFkSB5*-
4bTConiK<7V0NSmkY2&{WxSU-+=S5d)4iZem71i~e0&9+He*JjVz)|$^{ObQW_Ge<q7A#Vr*PQ%U>CsB^sg8U^o>dDag4N6OS@uM
nF4~V39ky{t>H_X6`9VR!!3b~cd%zKPU+|bty?C=euxCQUCWM35Gd&#j+ndxw8$yLe2-oBf(&k)gpjvU`}mH|KM46|<}w<Ukpaxl
6?6RwJ0OxFmi#<Qa2xzle4#fVY0+Iv+m)F#D{`BxEyj>4<*#)dkLgHyzapDqfkeO9pZ|g<!v%G`P~QcUw6pdMcz~xRgz%0c9%|=$
_^-FKi5V`*LWYzFc9@>bKs@3S&O|k<0Q>)sX@g@S3vh0`=?WW{glQs*3<5B!EOLZ8WynChvUy@s0n6#?)TS5TW*5;e8BU53JhkST
pk}V*@5Z?Qln)DqD>8LzT~`nt&o=iYJBafp+!gjVf1$E4yWR`$u>_-H#quj69#?Ly5X_F#zePrhGhSgjqN@`wyR~80xtfpv(J|x4
lv|73r0wG?vIAHqD)dR!&JAqdNBbX)u<vupC{h7<HgizUtSq1h)*W0|?%w;9U?uH#40}Fi%Z?Yx_FP*6AtF8J&ttl1dnO7U%QD9_
hfJi+wdG!~Wg8XM2+QC!j(c1&xeZ*H4$*-_&4IrbAVnI4VG2|&%30aC1LH&G+;OSEw=l~MC4<;rEri(iPozZmGbESg6jckT<)nj>
^c?EVxrxY9N@=4^Yu3k<Wj8Wy1QTu><DG~<o)9<4#|ZrGTL*;miVSdchJ+w!%PSJe438TC#n6eGR90!@YSL+^0TZsm4VW5Ty>GU_
O>ZciAY#$^^NU?r5qt$<-x1PK!*eU1dU&z2hQBvR5{)}AH9uaH-#|YCc>K35>@F61<_)Tc-2sR@oj`1<D%y+{%qpi5iO~4|ds2p(
^4H6lyV>y}Fg7*fZ#E*^?t}pUuh~Nx+IbFtCvxj7-)^v@FGioYg)%e~cKx0ZpXpAHUKJq^7nmWV5|RR{s}zd<uJc6Xxy;A^XD>}i
nzh*mhjhK5Bg*mgvxV0)s)y!*;xDDL^YUG#n}YG;Y&g6JJgld>4y=r3m9#gl3b>gi7q#>-6xx<I3Bp?}2*`9NZJhj3T=4YR1#k<J
?=)iJc^mdSJ(P6>qq3+TA$CNO^Q~@IXwlIiBQHlcJ?q>!fN`_xSyRSyqZjga%q4(%7UmAG2zzcZg%=ZjDpsyx^KH8{^(RunHke4=
fJW_Vve^YA%tn(&mws#<!_cL%*U;8&^*R7JaP<>Cd>u3FS_D2C)-61~j~gZ|wjggEkl#q!|Jd!>k{JgjEI&LhG1q+VC|04vVe*3|
;+LRpNe`9!b}X~Zar9|-NY23F$(OZDw&yrM{nbCPm4tT6uYpr5o3-!veqpQPsGj=nnjj>=`(_Rr3_TDHcy)1;0*V?aF1-0L3rb~L
TC7Q}H(7LC{>~V;8;G>W1|#3Rs6h2K7{~;6pBv^EFRleGRP2jYUZ?lpwd4%>KGTx8f_Cn$RQ;qBCK>NfP8?q#=DrLV{x4w0BSMko
W4)|BZ;!%Ugj#KOBK|p2C^Z81ss~Lhl0P>EAO!bd_uEf(i`LX)qirVTB2Z}2j%QJ9R!I-$8_g&gS`OfO*}<AKD7FA@5}NF@;ZuLz
->Ih=NHxK@Mt1Gy|FbhLSEsz+GeH$Y?z+|7E|=()mA8lGt7}1w{S%oLT&NsgwtQ!o**sFiN;HsR<+z;z!WDV@L{}f%5YUqP($59P
z1Ti#0b2%9BfUS#(m1b_XajjghB-02C>&0xGu1g3e$iH2?r1MOE8``?hCnLiK>h&FOX@798&qiboJ;)IT#rL82a%I^3QGdrEC2q5
cK)nN;dab?h(Svxi<<HuH>9Bx5VwN~Ra?>Y1j!Awc9fyGxK;wjOBqS|k9|}u4#jS1-sJaM?45YQK;sOw7mBv;I@<NVN9hhM;_&=i
L}z~9>8^Nt4}B=l7w<}46b#A3+&bXNMK|O}714_38XE7yv%z!hs|{*{hrv{}X?I|3#zi8Vy9LQi;p3tgDjn+kJ+v6>=xzYv1e1#}
V4i(v)Tw+oMfaUHU}xh0xFV6(kM`*<o(&h=Y3DBuJs7;JqJlAqkv*fDs$Fe2YdHtPzgE%bD*oWw*x!)`h5tdMQ<nnyFki1@_*xG4
=O+yh_k>0I=cA`^TVHJ4wZdfwyiPce4#_xdsw39G34X=wQID;TV6p*kZC#bN<(E@2Nux&Hchczvx>h?MH6)anVj1$GE=R5xiz(p(
#ls3D{S_n&X7;q5uj}A@s0M49*VD%lrpdNy&@XoZzr%g0e}Srll5R;Ul-ro=b+%?L;M@xK63asyi%-#KuHu=lEp2n?611cBf~Qom
_&}V7+rXJo9!~aTpaR3s)}3tQDrmSuo&@T*OU>QzTXr5NePc_JQhF!d4XAyCzmkt&gqg;oiNk0l_?}$yJn*wtJ`9c2sT+4e`_yr$
ESbz!|E*=XvKQGCk*63*74!vzCxd2xzjzV_I2e7`XIHR^9W=99gb2nU4!4mi8`EOx`>>HIVK>v0<U|IZ&GbOL4C&h2w$zDo@v?f1
rxMMGB)#(62D3{s?*xSCwiCAtpSLv^T>zU}Ay?GTj~<V%n9eKJ?UKoO!#QjrQn9poztVe7hUE{*;`~?P2IQ#^%<~k1(JIkC$D$&&
i~=3ah${Ns`9Ps<RvpVT4bWlr)t7<8D;{#o#03uNy+eNZR|m%p$i1=QgSnZfi~1+uM9_8285R~Ab190OL%&|QzUSg1X;M@3hIKeq
Ctsq92-6$+s8CX`HyDR~SULS2cBk7!UFC|3YHbv_VLNZ=B@Qk9lA_1$$9WOoD^Z*Szdxus<_4NYIuJzIVny8os~QM#bK3Ekb!EtA
=V(G<)Pqb5z2)}Y0uxSDekDyf^00}M%*n#hDo&u(@P~+rpD9e_LZ%`e5%^wa-fvkOGjK+K0_qr)zT9DQkDv-Uu8qI9LR}4w7`DcW
9VlZ8e0Dkv_!dts3Ag49d57_$a-H<E%$q>IqLR0rmKh^pp!&~FZQOtaas{j@e<<;vcX-dXJXcT^oq|ary%c~2)xg7cIS6!a(>KlG
Uuhog+oc^(@7!Y8^^!!f{eU&n7S$Rj+L-)_l3qkTsa~}am!?0OH4$NckrSTwzff+9HyX)A@vZ66w1Y?vvM6-*huJ)J1bcB-Z7CbI
@vR?8WLH9=Kk-F)pVS>J)UX$QM7pRcluBEoHq=}<9^v#+W6i!OtP@buP<br5JYFtN67$Yr9}2YL!A3|Q{jCixS=|aJ)D3;6g&)fW
v^iW)nvGMmFGR}7^=!UaaeW2lKNG$0QrDtQQkG6mKx-r5YCA#MYKE6_<yG;y^3Yp%jbA8p7o+MjCVO+;2_52e%<~{j(}^?CO7e?j
pl)Hx5<p(4CdR-k1-y6YhV(3~nmzeKL*?tX_Eu`D;59o-X8qwO4#Ixe;CetUz{_s7k{#Ov=~<QIvwt0Eiuw#Vu+Q7rXp9J{1tM(>
>S6Tg#r~r{3|;-2orRZ&B6LHr5My|ay^r(0W(O~*q0nzXIv8^td*7YfUd1&>je>P?+rZox)hvRne6uE@lwcbK8sy!q!db>kv|BIW
eX|-@!~Gw6KM_OokDXo!m}k4_zZ*j%Goq(p29KF`l6dLM93a^022U{pf+zNmn&^bin*H#@5Afc;A{_do$C$sjPVFs&aL{eaVzx;w
wO#un5lkQJxd+kd&&40kE>-HjGij?1OXMmPJLiq0B+(g+G`UI-%NspYq~US;L;q=~`l}SYpR#QCV#nOh|6X&Hd}Dl6*{EvekA6s!
Zs78lrpZfP$eh0*8BiO3rIakn%XEh3KpY$Jw*m^?_tCWy-V*k;-L{XvI6pIV2apbB?GgV6Vaw3lv|S_Wyi&hX@+u6w02C#P*Qci?
g$$<mW1)8#yUOv7wRWF7+ak|0>apfYNwJI69Zf#xF4zf5+y*h$!L-GzaK&3#juCs41(l&Ls&BWuz)zb&H|&a+y+v%Gq?`l0EG!I!
Kx=Td9xc#{I!_t9-59(tMwV9OA#2b6@pA8HF|`37LWY;6Hq@i25F?I7qNNrv#v`B+R{qnv&huXR6nGl2N*RpQ0Xmp_yI%5-ypK&4
cY_35S;g=2CP_=f69;y#I7VjG@VcX^I!eg0PQSLP+8Oauzd+Y=<P6^^g<wqeCTE4&3z^OaA)o|jhWac+jXJ3O`q%I6I@dyl<*;pb
iLB(wCF3iAYz+Fw_BESVJV9fGYDDLqv+Rw@UTaM~0njxDBGp;nirh{%+u<0cb(w(4i!RU3m_pHbbxoSt{en?GFIYH(;2Sk$;+P%q
E6>cdxJKipM}_2eqpgNAjd|1;tAME_{|2C|{d;oN*t7E;3?{*;tkqHAGk7RhEaL4B^^cYluxmV^4T~4rY)0(<tnQ-|P;$}s)(o-R
nzit#|LoOE>nkiIpeG`Ky~AZP{KjqdPQ1)YR*OQg`_8pd)8QT>!ZRkXkf97|JF{4&vlpw;2}1}RUf0o~Fid!;l$e|yNC36vv2}4c
3duvsoQ?uZky%VOIwvkP;lUl*)NdnU8#=kzIeWNq>>dgQfH%kj27P}R?)(a1t1Hp_Lj?qBU@=FF>uFz8A0^SFz|hzDm%+(4?hclM
1oII)XKqh_ww2$546Ph3q%<cN{JeM1*`u8QCh>(8l2!=+m=9!x?3un6>Vjl&e~@oCLz+sT0Q}#BF@9UE5G)-oA}|A{W`sdia~p=%
K{=*jWG3Scw?dCR;R4EP0D`*dx6r21bA0g8w$xT1d7v@|2XZOOdj>)vjR3wiXOt$3@W=WL0*<TQtt-^>1vQ=i*&47w;Wcv8!BKaP
aGuFNgwj8<HT)Jxjphe#l}*Ayq$8*HSs&=&SkMi}Cj&lh^pC(DDya7vsO88W5R3k%RDt?O66_)H3DE`zeN9B6d1aJ7DZ6`cNnZQD
oH^!wl3!D3y>f2Qbx#ks#Zt(9<u{xw*5D)8nH8QhV6m_h+>pon|4u}2++4hk3v+1kjpiTowZ&+qrsny+yq^h2Z)l>PbSoG!YYQm!
wz{>RQBlPfs^{Fn>T8uNb@9hovY2c+%M<dQ+4UwdtU$EAoii_g%12v^4w66eKuT}M;%phT<i*H-M8Ji+ZmiRs`$!k}CP-|wyeae9
#tf&jizC?FySFk-DO<@|*$e<Q+Nfsn)CS*RF5-<9?4lx<N}0AATx>zbDka&D6DR6VIC@>p^E%oqfN-|I9dAZs{dg^{Y^_fQsfCj>
wbBu{82ZN`&QXYzmDSVOJUzvV$D?q}7ww4;GZ5$)D5_DBG`y_hhM|#M@zxqC7xN2O0sU99*2j*95E`EG$lEKLSVp_Rpque~P)E07
obu?0FTxyoA+W_kabp8J_v-giZ55Pk)b|gkU-^*&!rmn0vitXjRa4trUOPM;WkQYuT<uh~PK_kRdL|=MO483OJ35ckYY_^k&6us6
*KI9)Jn5|UVv13)$lbxDUh7zYp@#d*MTKVUq+7P@CiJGi>gcX0{XJ%A5ake-nm1|N%GYPCK-N7efD*DHZA`sf#UxnUc?HT<!Aj^2
_ux$R(xnfd*0Gq>lvn8Wvl|HfcM7KaYQu)GBq@wBlYMu(rwmMDo(e9^B*7FpIjpI<NARfhZLHNd<~dpi;e2<)BZC>Z#BPjy5MA3%
_iLj*po<|;cA}pZZ+{bGoFk<at-8A(%i@__%BzLCNmx_7)edKL(=~zDeBy4^<Q*Qb6i;r97*a@FWw#Yw{Rao#gqZI@{Rna$hR&Zj
7YQPjyHRr@Hkod>GZ9XQv~KkU<rinQ-P<7id5&#q4AGddHK?fE2GqIy@HaoWng7Um4CTV^s6Jm}<bu|1G|QIO`sS=KV<CTjYDD06
*B)$DU$<rKIOI`wiLP_W#GkhcuyFH{0u?Vg_ZRKWO%!PpzhwzJNkyETmcrc=H)vatcZCL0jPaY5-7(j)fW@zcPp%W^Lc(iq8p?`r
%s5UY>54XA@a%E9k10-<qb6rfOzWXUIw3hQD1@d`MnQgvbtiF}2*Z!bx4WG#7-uYPw^84pIJg~Mt+O<s4&7#%;a-Og-K^FGi6gp(
s@C0GDhz80DdiFkmYD)fj?aE>0XF6z3G4L;B9yE{x!wp}(RAoD8~&1D>`a+{K#GW%m@!(eZ-4k;*1Z~D4l?55JB4|?v@BiBn$4cf
`3rpuOEj{P5uium-^%t71ify8NSlo>Gd^9sotYm^#x5BGBew>Q*qEql@dq;ikgcvGmAhN{^-}cNCMF98A*-_OBKYByCXU*sNQdd7
c6r4Im^+5zHT|*ek$MT|bjpFoVK+=M4=|;tYr`b|1_N-D)~<XsMnWIv7K1BaFq&2#VB^H5#~&k(%Iv!9VRzP;$YoGJBb;`oSa>NU
rq>Nw>w-lK#6yeBv-B_!l!y-+Z=)%wC9`yR<3t*x*;AVMN?DSxRAzj{lU4MfqX%x}!Fq<_w88?A)&rgeMzR#bY*ynTHo)Ik)sic!
c!`mkrCRj{$V_y{3rjl$0{Wm%haJ9rzaNv}SA?0->Ptw|c*BPW{^x@ueAx=ZJyi8h#Cst>r4;JhrO4_MVa_S>Hc^w!euR0_>r*B`
4v7xoF4trh3uy)T?pY{f$gDW#tyzgi@|wVIlB>kEWKlo{q;I6YlOvIkY<p+L%W>68a_SBw=01BAUJ8}AJUwj0YIhQPzBAF9WC7~i
G=WVdJIedpuWjxzCe-1owkI|zQH0L6)9hKYZ(DJI?<F5$ZLo|oO7Djvv!+i}K-Ty~V&3-tHIYh1$fq_uk&CD?ard#TH0WF<YAk`1
f}h0p=B#D6cJGpJ;niNicPa4M(&{AcKXb;o+uX^10(VDduDR{LDmHgLmj`~4p>-|v)p{Ro?L625PkaVTgr(1L^8gf%ciwasC+YU$
?;7{wtSkmCF~If(^L-t75Lo#kxE=FF-p_^ThAR4T80VK5<?IS1x>Ie>DoIO^+wB&Yg&<d12}SK6!fhDts_ht}h9FD9gMT7)cjyrW
v0Rm52DgD5?zBQrqpi_LT8|QR%c`7(tb?R4p+7T=T@9QCx^(2~1X&7B_eXwimxM$~)^wb?qI@3HlgCmEJ){ooH8$N@mehDr>R)F3
9T5m-7--6-_8mZIk7`aAhUW?&w(cgf1Uj~i8tNYb6J-<E2Up4cbH0>%Ui*dUI)!&{u&3%&fz5|_K-iq$g>pC+ABNqHEN}dzy;mkt
=;<k_1*v!bw#tV&>)ZO491nc^dI>4p@7axKj%X;)eWm0w@;6<kC$eNM^ld@uWLo<v=>TL^ao?JMT|6s8bN1c1PPDb%BqBG(**$or
b{M3kvog^>`5lV3DyN(pL9KpN^?O0`#Yr|!kg~FZMRNslFD<|i`NA8-?#o-s0npP3t8T7~2k{_y*++(v0}d@0%}>kIbjH9x<wYz~
ms2=Db{#KV1D?)Cwla}h3UPru-JIwXV+v>HpTD|1pMz<*HBS~Fd?IXf%ysoC<_GI>B=TCtFss!SRL$He$U#IR;fi}*M39C`)*#4&
*&C5sBK%d{B@R(YRcNGGhwfYpnBOR}7ChdnJU;m|m~|D>h{-)Aj!l<*2mY7bxB;@|&kx-yxo2`ax(=mk*qI@(##E%pIBrl$o_cn^
c*8pUDX8npnE?XEvHn*$kzNHg#`{jbjagxHh!-ya|81;-wh^Gt;nx?(2QRRXMES2dYp`<E7?&OJfBI+r%**RKw58h3@vf0L|7L`H
Dx#gti_C!#;Qmx}RdUiX>U5}%8r^<c=a?aHrW(~N@7DYa9vtc{`s*~KL_wN^fX^;q@q9L>c!_>29HY})gO04uaxk{Uac=wXvS$Ml
b<1RvvTgLO)ciGwCH%cnEP_o2jQR(Y)_4WjmU@)FU>(nX3$Pn#!F^a>up|9+Mcmcec><<E$<ilA*1TM+c>yfL_fU-krUyKnch(=c
kXQNy*Bw3Sje{7xM(zkRFN)J*7?P<;eA0or0vJFn@}h;6C?cH!hJUZm^%fmj(%=WRRZo8b^leHn$aa#AeX#Rn4}_P4DCml&e#X(7
xeGe?gyx82_h5;eTMGTquY|oouyRW`AXjiAcf4cA@pyXMxlCjEd^{RTv8Oi5-bqtuaS--GrpCLu!m3Xie7dX)utZHap)9#Z)8Y)0
WikJ{Z4aSvo~dA#vZz)E+;qFK-UKPg(71$Z29aGYSR(!39U|tB5{H^`x=I2K6}IQ-IG38B&R$5RntPbtKZ<fiE-p%d6#LRc5S2bJ
fwqQSj@|+E(96>#1^K7D0fsHJkd(1f_XZ1p1bw5$7Sd%Z9^UOPHG9R_G+`y^HPd%~2_f0asJJWKdA0=ePs$#V{itheJB9sG{Arrd
6SLRxeRe4{wv}!i3<4D!xdzzwz#D6p<(G-*r@b`$>|o5-l)(zXg6H?<LnBG7x&2Z?Nj05x*q*;FQZF@XRkkYyZ#>5AE7n@N_*RD<
jl}2-H*-GLqWh$&mnYGtGLFt;=0e=Q^Kr>FA410UT5k8|`BHrf2}kei=x2?qoABDn0>=OO$y#i~2p=*@9-|dHnO*{o<cIY6@XHu9
(YaHN_igIkf_MBmgO-dLbJCoF3P`OBN@^ykA>iCTDbrxP@^cUuQQ(1w#ladQA&13P9Qr&8?J^tYlO$9~$idT5VK=OxmN=yrADCk^
*fgIZv7Xcs1b`w5l-s-KNUEDoc$Z%#;EGI@$u08;rMu6rd{`>cs`?=R-T8Y!Hff}om1Ll4KkihYB8%+3bydF|5f}n2e3>`si+ux&
tC!8<7m?QzhwUBHEIOA=IjDAa;Dy)Fp&BdY9T!1>TCf7$o@ybAa)L7blaYVsY~(EG0+LBBao}G!%#q@yCWE-?g`tRn5{+}5Y{=<=
UWat)dc-H(Ti>^){<y@Y&>3@GuXxyHsItc^%sXZ03qKuMVl^nyPY$9Be6O;P_B%)9HoO8g=aK1S049F=XJykWLrYGT3_VVI;qfl+
>T$d>vmj?^lj=fSDE#^T3>jDcdt|tp`(64gP-qr`_SGczJeqZ@j3wwv7`^j8A^_F74ID}Sc>fsoeJ(94(Gs2zh~@majv&bKs(~i>
36N@v*+}?%Z&0(z3a&YUViz5HE$7N;!Yeba-h|CfepMm3-ItHZaL-o98tGB{PKh>flI%(o5tYJJmFkIPyBi1>ziV_>$M;~A|AhAW
Cmg@qvwadzsDC$5%XOfAy(2Jvi4>)**Whj%?MKz+x1VDXJ~t7wx8CE}C&xeH_;nqT96b|N@De<GWGvstf0Xfo{}CcHn1E$?=|`44
ms-EnDvLY1pbho$JY(&WAP`!-h>Ah`Q0U<sA^m9?isIl4tUuAZQj{}~;??8Yh_NUq$Mb*rPh#J2-%x8>(p^T^{D+1N5N^c=NWTlU
yBu)THDU}zuKqt#vUth=9I<*$w{F&*Y1SHJEz2K8=k!8S)eG=2WNAZCF^%r0OW3rB4zXZS9b?MQ%%6eFS6Qh^80G0gmn(yJQ%^R{
)?uyAxNp7UTOyItX@t&(z11!KTM@U`SW95Wb|(xLZQW|%ftff}B6-;sC1|CXeEp9n2^JTzN^a-mO-47x*N&&x9F-XI5QqLpnu^bJ
ZY!8bdV(ycP}hb%!lS!6?2UW5(hA;@f8?p)2!YIytR5=5;f6c|JI+P>w%LtH3!&&2rZ6*A{nMR~SZfr93V?o;hIHmQnFDv~smoRk
gPhz)@WERX-_N*p0H`Yt7W}eVc%zY1&hM>lR&kW|qa3Zs?*F}gwyH7AH^BtPjPsL$eC(#xbRE||H0qyuHd4L}R;im*q9DZL>lw(j
Y}NAEv0%5_JfU{9jlzzTekXY7j@ia*(4mJaQL1s(k{BYgIjwB-L2;=7bO_LzTBvO&414fwqrP_tab7Khi86As!;+c24fps0$~>E9
v}R0}@40l8$y>Nv(LjSsKf)NZa5lkfwUqr2Jt^Ve_NMFvZ7VSk4d)3^?)YWBcfi7U;dbkW-OFE-B#$kZT?(pnW;|{UZF+<X#3LPt
T)M4hzpMA~;RQk|%pt0yxx1WA*Looo%`(oJq}s{6&VCxH_JqB9V+L<OC+NUZMjoaO)BVt_g{3_;wejHq>|B+ouRl?|MD)yg;7L?A
iUCaaNlq}-zqp-hO&js5I$>b9g$*|*%8py5T8ic?WY>*!yC1b%Hjn~g3Re#Fur;)RoJwcuoB(=?vK+-@%|^!Bw!9-bRa~=Mv_{8~
Y`%4KD}8UIBx#MW0qL91L*JMmB<+oNhz-W9Eun4mLb5!stVkNrr8b3)_5_W1K2}0~a!TrLn0$--+<Ld2zSMwOhVA!}`@>z6fPR~e
@+CpFOl-AxJL2CBskqKXRps5r0DP7Ut;Q&TC!eQ*!d$7aeP*B*Y|{jp@e?<FL`>@`wwJuXp@}-ZcYRK;xRV9C)(J>r;k}t3>ug}m
kRgV6V$cr3ZnJWTe;on9u(}X!jtK}P1cISREe(T9wEu_YSQivEs4=)~c;i{)v!`?wC3X@3CqOFEkD^%r@OyVos3}7w@BA4~K0N!i
O9?7{YLB{m-;|r!M=dacW?FYw+gudvO6fTGn5P#nqhTHC_vqxwwGOXxzocPC0Cc7%;X|jw8@-NtGYQZ2Ph&`FA&l}$zjwBEQd0>m
SL`CqUid&-n?fg2HBSp<kI4Y-T*Hcis?;6x>XOYlhO{pff^Ks=4G~S~o_cZ8?K)jVlIp#Y1oii@V(|Tsbq7Yc30l~F!d~LH)Gk!V
YyxYYLg}R~KR>=>k9zm}pJl|@YdP54BR7Shle!p*5zN2ce)joM8|kfVV$xOu@k6<KP90QxD7+({J9rmegyV3k=y`?%b=I`4C6gtn
q1p0Fvlxh2#Ymx{*0Dcoc&UzV?JUVoA2j9dnR<6irAD+Pwc!$r)rM;Cvi;Y{epe4q@NMkB_6gx%Qc|>43<JAFE=HQ9HkiTNUpXM6
tK-!vl8c$^$$$Zjgrd}ApT^vhllo5bH87X@E@aNds?Th|UIc<4tU4eZ_bK;&v5_wHLcs+<1US#AFec5lJeUK&OE7Hfo`;1e7=1~{
Ip|=%u2VGywg*;fT+D8}wzl=To)mu|&Dg_OWDt}`oXARe%t$}INmTdbO+F^=7W3IS;THWDPnpTT=Wk=|pI1kd2>FUH!Tr_Wrmg6e
z+o-^c`Br1_BF*t_j^?Xf3)b-Q;JJB3&mo4!#<OgMr8_sPz}}pr{&JuQ3y-eWdA98np(^X1OBg}EuW2`JfwQqBtQ<x++k<3x5SWa
DU|SR^r2*DI&V0x;lnuoKob(*V$D16h&}*lsb;7T6DnIhWrmFYZ073=Ky&xcl=UKNMR%0W-x}5<Yuy50|NE#_XOO!iRPmDsuk_+v
k;VF-);4P;bGjFJ-p%)B`@n#9nkh*f(p}4`I#kJ0iSIDwHKj$h`RPs5HHU4Wq0jdP(DN7c@ECYW8{W_Ah~e!3hg0--@|T41RoDgo
Ju*tDvfnKXD%k124D8u@L&kk$f7KXjzV>N10=5*z0x&oY6=i%W$G4;kW?j1frZx0RHrZ0iS2Y>L45}!i&iyiM8T^~j$~;E+KK>><
cjNue4&`C%Mh&xT)Es__xGC^3C<kHOg^78Xs2b-o({^jb-x<1pvZ97bvyaV59<~WANonoiUw-5F?L>0`Cb&R%hNc$e>;}tzboG-J
hFUlS#fZLh_h`WT@@`vsNhfd|pvgS|KP#E**QxZpeBs8%o2914v7_Hx9Q{64O$k#vZz;D^&2~W82#uF%&R%R}X<emZL0Tw-PHtdn
=#(JpY)nv>4xE%B)I|FFXB!FFYpL2<T6)r{<o*TS=nuH8x(UGYbtTs3+ox9~fD1Gk<Zs{2)M2((U1&m;YW4cGkEBYStUNT(`K{g#
m<wmvCO9)`N6!5n+Dn}N6M!nBdAVJPcA)N^#D@)90v+6nem{Zx1j2>yctHIa#1-X9+E$ZmqmQqE>+<5pBGa*UQ&%;s{8BKqoscS1
7rn=Oa_STGr!<I1B<bA({^ipzfJcrWQjxC@^HknNfRm^Vr))BD!3=8=Ax>SOIlwZtlITl)adeL#Gg8kpMmO$)>8qWROQxWqFoH>y
$8e^F_?+PMB(ZnaJp{CP`yP3W@+6X51dh5vTYz6hQQo;8iUlt29<5c7uD-KG#H#CBXJ{E6#++_=@juvCI4^PNpTd#Md@(Phb=R@d
PbO-FR8Ko$+<_dR$PHgzID-AV_>Iv@_+b|r6A$zq-PzE!cLzUsNfoi-?<+RqFdQNPRz*&6Nf#By@o9G4+d@>;>vm#0ZsS}ZyJyAn
g5&jyx#6w~--JPeBC|vKu~ZP_iO6p2XQ49${_!#9mS_hO6w`)kU&GKNHlv*~JpJW^hR0PEHSaYw0g;dV=tW69!kV&qk#tP>5BC3k
I>S>tigS)$Ot(8d5k+PU{_ScQwkA_V=>67*L@+No3Jy`{XZ+2QOt4+JUS~DLytc77p&Z0~W+>c0w2yM-V`>WO%a-p5aHdGp-=141
B;!nP#AnmsK*aAPTp4JL@ET}|53r!Dd}~ENlx8RIxM&DoC12Lei(S<~>}#E56tm6ZYN6!pE<+yy<j4lZB+msWsJTp%tKo}y>}QEI
B<IJWD5S+7BFlY!C4CAizOMidhk$ZFh8x$fjof@CB%+!*ifXT398Ks+k`j6(6K~5ODV=v?C%5Om1z*;(Z7$M{snAAuG1LnW^gKKw
R1K(x*yk3{zRNKk9`tr{aR-F*cg242TTii-EoQi)-pq~dM=k<O5H@mQtwS0jtGZW8Kvw_IjEzP)^d{O%wNEN1rXYvc7<Kb47?FtK
Fzp7B6*g;NM+124l65L+X%Q&EzY#|*@|$mPOuZ*;@8oIx7NI~=MxAv&BZ@B?bJ1U$1M14ULMem83`x1`K?i!z={~YGaa6rEXIX_?
(qGc3J;|5|G$J;w8P_LVhvLFMDh2uDm$p5Edfl$`B8z(!XCx4%k_zbdI)}`o_bEEE15XD(Ov=nfLo_PU><w-4JOx=MMvE|in+)j=
ke+1O;t2O|CdP*J$j|QRIG@<Ao{&-havm4IW4yJr9XqKz{qr){%We_M{v|%sn>b+Q0%#7oYTJv{GZu8$w`Az1E^SWNEf+%1{}ZJ#
XSZL|n;oVbtq#Djb9srPX@MQ>@&(zO9Tg{!b_2Gsntylh#3b4En|@Bus83i=_^{d|SDTPI2kgft)cV-?eI6T4k1d?rKJfF$jsvvk
+G;G^lY4vAO%qKOl-#J+f)Bz}qx9k?HS!4S671=+1rbth;odyjg=zwUv!N7p)q7dsG;DlyN^AtRaaxIVV79@4L#q$%DD)dnLp8T8
fC%IKYV`AtYL0!Mm5*iJZa7@bjdw<kb!09{$)j#LDjeG^zqUDD7W9@Tlq_w?y-#BfSIE!GIBsg)f>++X?maOe;XVyKc9%{$d>FO`
I<$cC6PUjTis@>pDG?rn5#g@Xp|l;=KmAO+N{;g*{G1nlwRjo?u1k93*oyS@2@V>A$3wnNM||MV&KcZ7A@La)=`YzIAchP3&G7?y
J1y5Dn-1yB2g(u6_Y8Cr-vDO=211KTw55uzpc0P}e@8GGM-LaF3x$<?c~4s?g5Y^0TiQIGeLM4m%U!_x@uwR6&nn8qiyU=R)2v|^
lPK0DvrTG+GLpRK)HzJfsMjV2a+yQ|)LpdWJ6WaZx$`?@TUTc!+SRLBCk|>l!QB$x_^3#Bs_j>a47s)rFt=tnshRz<WiG2k?YVA%
K3Q2aM&@VqhS@e<P|kHZLE=_6ZrT&u>S!t;p2%ac-ty>I`41rQ(6`+muf!jF4Z;){g@M27eUt>dr9O0P3VR>3_ve_gHnAtx?K}vJ
<Bit_A5(~f;cwzRFN|Gna@*-Qd#P|-UCrzWww9nE8LorkQ;9%&nNA)pIUaKQ$tF!tDdZJQUPHocsRM2mDmSA=ZQ|SyS0!y@ZU<1L
T;@zOgey8yqNxAwa5cAg!b`D_Lk`vy6IyQ;J*V4X=0PZ_Ewlpmu%1O1Vp-O?=_(pvUPri6E^V0m#ncF04s+4Nlj6zKTSwh;%ztsK
NO9a0%uo#|;V9c)%LwWI1E#24R)?u|EC{8`GpMSn0)NMnl7|i)h8=5mKS6vP@iN^+0bG6?0pHd42Fc&)-Gq2*;;$>|AiYvdLq{Y)
(H%76_$$3>q8imrQSj+w!$uuxsZs#Z-Cp;^_#F>&#2T5Om*_sk==x6`Ef*>Aj%RZPv?3b<4|mc?zb8c(ngLfSEGr;FP5xYe0i~zc
Q&jW{RC~2MA0PbJnGvbyIxl-tbEOEeVubt-wS_Trv`1_80}c_L&rT$)Lk3pC(_S5CK97Q&<Xm<!RqE)qSAben;2>6qI$IyKEauN9
TQD_&9Z7RstdegC+ogQ3kma?pNEri7Vjgg3G%;2aV)RXse>5GxTBR$ufkEWc-;7^Nko*GRz+@><rknXuI4CKe{t9UfYfaiHCLD>2
&E8M;&V!j996B{1-;*Wncbl0*shJ+#-Yl7)U+=7bh$-CQ!Rcd=IwRlNhlW2Fo6`bPw5C&DnGo+#P2S1~;|b3w`5|DF06#1^21<l4
Dg1_eO0wEG;8Rro*RCn>?=6cfNe`RH+M6oQUwqxfMj$Oh(BFo$=%o>~H_5J9hh_3V^GYWqCx1w;I^{2@u-E}N@<ncq0I=EK)57@|
3newLuVL>})4COCpk`1n{|KqwsC3POJB?58t*Ki)bzzeep2mJJqZ5FP$(xYxdq7Bv2c)xQR<I8cuR13G;A2WRophH-0!P;lKn#Em
4E!(3aCIk69k!3eDGP4(S|+Aj$9ZdT4RBLiJttn$OtK`RUJhUv66IN8QcqsK2%$9}asJcbl}<SI=U>p&bxM##(wFh_SD%0XVvI-U
L!HZAjo29GFWi{fC|YF?3#78lCUfoP{8@F>T8ScG;DXAbfrv)cjqTjW$x$Z(yJ|4kQDWLN-&Xoi_{!Ae=v1AqVX$s+RlO9rB@=j5
qmA+jBQqOIp9o-e&8mD2<bE+xrLsE_s>eob#K7J8)(A~^)D|6HLwuP<6ZGt*dB>5=95v5wLvb*1yuM;d4lvCqP3-RP$%krg%EQ+7
*ZDH!TA5KcV9Jq9TZIW{^2fJ%-@6SiHCW(7s511FLSac{cvbjmFmUw1J!mW~Y>j)3cT_c=g0_IBIq1F%CT6}-AYVIz8@AKhs>h4}
HjD64=?wF4pI0q69tPplfs(=fyjBHEygKjU$hxuTY*h<^j@s+AJv@pdPECO9@zyYxdu<x?@$MxRWzT}41)otV&LdzDlMDtAU7D;+
3*7G6KYipZkdx07EnA1s-@hj9yXh__HZkESN|i3qR%c5#c!%PCYmbk;pxa0kQ}n`0m5QknJEn|k0VKX#a9!+ibT(pOl@9ZejtD75
#$eEt_7K0~Da0Ck$?LAZ7&=v|TX343Bo*2SSUz`(tEA#FeWuQ)(zCf%?n0lxW)zX%9oHZmHP3*i9GGL+>Zzh{oGv}i$l@UO`jpih
3He>U8G$twm}R0F13wlFvc$JJEq%+!qm73q1=iB+%b>v(2_X6j?Q$cCyoU4w7Qu!4&cOi2F1S)zmOK{$rG4;!AN{#M?nIcd!~u(e
LxLfd@(H(Z^#$X!c6`*ut!nD8GivJezdb!CxwOpjB%X^vG0?x!(fq4(;BnvoA7ouOHe$ozmA%ZU+cI2*ODiJo@7P1@2N`BUPv%z;
cTka{;{WtP&oHTXd4?yj8?VRwMb8LPUiLrtF29RtX;Wz})F}Z)*lIskw<NHO0=sPtQN@9&hxxG}i5$h4ORBGTws0fO(MG@e%`*Ah
g0IOO$M8E1Pek`X97LU8sr09>qSHQse-8Tz2T-i)squm#Iq9s4pv+3~Kn*054mFpKati>VXT^Dp2{YeTxnlqP^_dP=(<-+M{M5lf
0l5idS2^uz$M?qB9$Cb2c&{2ldI0a?Lp_%!)2XUFOhL<#jDC2$tq-P|&vsrZ970E>wK?WMifXS5P=WYpb%ti9HbIu?uxbisvYy-K
x6FYL(W88NLLD-2gV3q5kdNm4(`y$%eTrIPwbQ=A4O8r1tFzO>wDs@0Fh%0kJXRtPYnOcg5<AWCy1?@RhzAo^O=wK3r*Agzr)d|?
f3u<T@U4s}&(`Im8@+^9$LsfJ!q(rwr3!yPz19F!ild}xECB9A9d#U<TGVFBU3dY;)U7mzwmG$h4Zj#lJ@>1VaQN2wAPlgyofA6m
9s2h5g($ag9`Id<HCYl9W}kyV#F{SOy56Tg)O7C8AwH6c+v$%rC!Y|gF1D3PH`ZzIKBlXnzZ?DB3+tu)RjXjXQXV!p&^p<TwA}Zd
F73hQCR0q7TZA#V3-l4irs^kb5&KwX&qe)Uh+|}SI>rTMhh6+powj2#7<g~gM_?VOBUPpNErIG#kAZilNKy}WItcGRK4n><^jgB7
imv$$_eQ)c4CnL{X4r+E3==WTRMHA3uWCY?zXV$(ciEEKEwvwpd_SOZo=M$bIft(g`jX4MG2)?Hj$kcSQWt%`E4g>V{<oq~^fA>_
dukTFG~gB|g+yhN5`v)&RueCjBPRSe{s!Hy`NKVJo<w^UWb%L<UJ#N+wPpBOoDaEN29aG+U&OKAQ>2;cdnD4)pUk6VQU^@OJM%3+
G$;!JyF82_!L;4pSg1BQ?6Clhdx6)I@Y(&~dC1jdKn=4och^}Z)JiC+-rLPp1zay{@p<Ck$_!*MX{G5KGLPXt3z`kmY;jH|A3R;U
Qri=kg)9xoo!Z(=r;31*g{ZBi`NpyDJd2=XCs$Qhh*8Szd)P-Hx#zmWs2(Y3?)~SdkFi@tv>fY#JXY8ADj$BnvGrSqCVQ-av^^mU
$eGL$8tFa1t-qNezy+tbX>Wb>vx39pEZ?@x7r9`+TE&ICEu>4&<>Cq-K}2D1=6B?LBG!KDzqfjkj7Yk64!7{gL9?kxVNuB5d)bfk
;4sSnpS+7x2v6swqZ(kNz~MtZqMH8b#&zBm6LQU-Nj$#}<E?f8Qo)%7<Z3&+vIZZ0guxCbP65vqb0fuC0`+r5mgn*|il5acn8{en
V^g?P$r>B)MXfs~!iZ=A%CXOJ4Ni|dcjKTB9nLpy_HH9FnSmI<5goqTm=@_4=L!*{j2H1z=5{zxoggk3+k@@_dGPvP)@kOJh-QVz
g_Fnlz_4>a;c<*Tjin;!{Y+o)-$mn}V6Ky`(gEQhf4^uAO$CBmc}&w1$;n)L0YT-S4)1xA2PM#oS)#%mrv$(C{r8gVl@i#_&dP?1
+%~^KCPGe;>39bF%~8yzJ#>uiuU<&Sp_89O2Aw)AZ(8F<y|j7oY&_&$9Dr6SuQJ=QrZZ<slEPQF!Q+(ORGm)a9H9<ENj<x0^2>0?
(TDT6ACnn6`Tg43y#~_sIWiMx!2-8a<Gw<s0Z3>zU@MGK*c>+PYvSTGvsP&JpF|+s9B@%bPTMr8ii_G6?Cbt0d$6OgbDpWSQQEod
9v|}w){mI6r;`^2!0g|6tc}z|VB*KJLWea1t|}o_Yd|HKzT?LIeV(g$%=R?;OG?LsS3<3yDec^7y0?is!rIokkmJjI7n2zdrqB3b
Aw+cu^}|-|fi*Xo=GxndLFi__+lobb-w<3n1iY4*D3yn~`<drQ)Ot522dI4>3Bh^X*YGA%&4$Zym*`k*LAX&4ljS$3=nXn3sCk;h
zD$B|`HSNtFK0;x^<2*9by)x4t)l))OvI9iPn6;fl1v6Nzy@S=5H}QLX#AcO;I%&J#9R>Sd(v)2qPq5xQjVx(NzX0jH7z~0-|DCs
4^7<jP&d8!zi^2;&VL%!$ouP<uxdHduOfZ#_dL09LC`}!l0(+ZQzbzG)iXwH!H^WFrWuA4`Rl?MnftQ5=uS+PGKYXy!J#R2UCS}w
D_GNub8&%vjDOx;?UNTYK?jFVdq62L;S4(nW*0~ufOimMjs%TYjtN&p31V7XiOxB2>v|y9Wz`*euzBRkC#vpQ^4z)W+R9lZ%BX7`
zO>)nJJ+3uq`UxfA1ucs&G>i2!BZJosoNeYAHZzuwr4V7mPYF5%Bp`_aJTQ1EOuYR_9GnHiJyM5l*<J)#~MVll6_I@FiJXFV95Td
UHS-xetb}?6>&FC-#HaJc)^q&JUZ`npLL!RZfczyix5z`aLr8Q^06EJ<T)blj#aE;Pq6U1!|vMEAA}bl!DP*I%^l7F8HUjkV89q*
lM_(Eb{hp-`oy@zRtU*T&O>qz)X3E8=YDU?KE`DM@>$WTpS_;t&c=Uc3Z%2mb2cArm`&=3ds-tUHb3!_WiDd$PfEiY;<PUys1zYL
tdr89OZ(4KzV^&Z_i#8qnr2{v9aj6=Z`iRuga)=0WJK3QWc<v=P!T0UYupkJRRAL2`J!vb7i#!O#G1e*u4<&0P0x#A3gKDrJS_~s
j8C7lxKUSKCO>{^tDV*CZg>J_Qis8`<`2SLj2zBEfr+!naZ96}8u`@w1@q+uB&#NHo-GQL^e;l47^^P8xgfe7UMW_o<LvjvJdhgv
?Ys6QQetL?)sU(QS=y4<mL!2nMx$}h=^r{&P##hi$>lJBC3OyAx?<VJdM}v2*fasqTY)hqs1AzmM$057evA##&4u!n1{P_|&R;cM
6%Ec95QJU<a)88;XQI#v5=k-rTMQu$4*k5`B}V>_WYo{wUG6t_L~Suy#mOv;TPw*lBRTf_z#diFjy6MV7OloAAa^3I#)r4F_4)O{
9LZnAgsvd@K>ah;ODt!`vCiWG@rlmJMqR>KjDZeWU0&pMUu$4Y#Y@G_6<WK0#%xtQxvdA;?+jhGeHo72NsCOZAT8->b6&n2`Pv5X
Zc(vXdQTDY_!IcXsB_<pjoKH2QIh_+vZvbiuew-2c)8K$$1I3bW^b(y{r*dlgwZ@d>)YqMaJpFC7cl9OfB{uf*5hnb5lpw{ASP&7
-~MPrRA~WqTXtY@3{(bk9rLg*Q(@}Tb+<_nGO;+zZE00D?!0F)xQu!BGF0wl0bAaCOuh$1>p#DGMNY2m;twVGMAbbFiinPyhJ#Q_
wI!rAX=_8C7ou@cb6U3y>Y|y?wz|e0t7Y^i4GY=s;*qPZB7R7D&@tzD5SwH1@%RRlmw<~UQ0jF2-4!}&665PT)XZXADc3>~W>h-a
3cpG`W|^9bWfqX#Fi1{y#Sx;$x*_eUout+>6$ef9i$cmUoP{V9+o%zr%}57E+#kyr&PvG7f|EwIF$4^70U8vbE;y<RRfTr{8cJ8=
*no=(*kqyyMrjtoK)nq@VI_E-qQ&BC#GYiztPmpxx)Pg~SHJ>JnX}a0KHXjy%MP9EvHrP+!>(CU`?TK}n4GLS;G?2Xr??fp#_(OT
E*rwE$ep^Z>1vpaUYvz=<)sBYM1<6H!@1c;CEvQ*(%oL|gYC?m7%YZPf(~F`Cp>%)&G07=tb_HWXjB6mC2iy)1U^85*D0H$rFRN^
=6@>+7|s;+@QVc%?PfhePAd{B&tHcagZS2iucfCI^FgaHY<%>Nd#%IFt)k>Go{l}S83gku!a3d2??{GauO-Sb!BG~u<BQM%`_DJN
adLtC>n~i?ka7+OfYQqQ%xN{^6RSbTbqN%jWMH}jpg43?pO3KW3NHM(JHP?t+cd`Y1ea_xE^0|94Xu?0s($vFuhjI_Z)<7q5l{dC
-kN_<-~N|B00Eqh0mr%n?uPhFvBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw)==56647
assert hashlib.sha256(raw).hexdigest()=='94ad48eec5561a26094d4be7e93db5e6ada384c8afad51a6c2924b1128a6b7d4'
files=json.loads(raw);assert len(files)==14
root=pathlib.Path('RR11_SPARSE_REPLAY');root.mkdir(exist_ok=True)
for name,text in files.items():
    p=pathlib.Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    (root/p).write_bytes(text.encode('utf-8'))
print('RR11_COMPLETE_SOURCE_RECOVERED',root)
```

## 9. Supplemental artifacts

[Complete exact replay, audit outputs, and discovery supplement](sandbox:/mnt/data/RR11_sparse_physical_handoff.zip). [Standalone source recovery program](sandbox:/mnt/data/RR11_RECOVER.py). [Expanded Markdown handoff including the full rational P35 volume](sandbox:/mnt/data/RR11_result_markdown.md).

These files supplement the full inline capsule. No supplemental link is the sole source of a claimed exact checkpoint, moment, audit procedure or continuation-critical generator.
