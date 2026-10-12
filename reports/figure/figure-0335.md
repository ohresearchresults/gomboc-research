# figure-0335

AI research report · 2026-09-07 UTC

---

# Sharp Quartz 24 — compact exact121 architecture and a rigorous small-gap negative control

## 1. Result and acceptance status

**I did not attain a homogeneous strict(1,1,0) polyhedron with E<500.** The strongest completed constructive endpoint is **SQ24_H52_R12**, an explicit homogeneous convex solid with **(V,E,F)=(100,150,52)** and strict own-centroid **(S,U,H)=(1,2,1)**. Its maximum-radius/inradius ratio is **strictly below7/2**, and its entire equilibrium class persists throughout the closed reference-centre cube of radius **1/512** about its exact volume centroid.

I also constructed **SQ24_H53_MICRO40**, a fully specified shallow truncation of H52. It has **(102,153,53)** and remains strict121, with the same certified reference-centre cube and a substantial surviving squared-radial bar **greater than1/2**. Nevertheless, its extra unstable vertex has a raw all-point relative instability gap below **10^-12**. This gives an exact, physically centred negative control against interpreting tiny raw escape deficits as near-cancellation.

**Both objects passed two actually executed, independent, complete exact geometry/mass/equilibrium audits.** Neither is a Gömböc, and neither changes the assignment's accepted strict110 record C1374. E150 is below the edge budget; the extra unstable vertex and saddle are not optional.

## 2. Source identity and constructive provenance

The source was the journal's September7 00:46 **COORD_H20_S1U2_R14**, the literal20-row121 table with SHA256 `98faec0af3cd15394caffefa6b97d45a42e64e1bf5b6eb80279ce41a8eb74e41`. I kept it distinct from the earlier H20B/H20C211 tables. I reconstructed the source and the explicit Fibonacci/noncritical-refinement recipe; I did not substitute coordinates for the journal's unprinted73-facet numerical refinement. The journal itself marks that refinement unpromoted. 

The construction moved support directions and heights together, rebuilt the actual solid and its ordinary-volume moments at every evaluated shape, spent additional facets, and allowed changing incidence. The final conditioning stage is reproducible from the complete binary64 checkpoint embedded in Section10. That checkpoint is explicitly my own52-row intermediate, not the journal's missing numerical endpoint. The exact H52 solid is defined independently by the following integer table; recovering it requires no optimizer and no earlier file.

## 3. Complete literal H52 definition

Each row is ONE inequality `nx*x+ny*y+nz*z <= h`. There is no symmetry expansion, normalization, or resampling. Let K be their bounded intersection, filled at constant density1. The final physical body is **P=K-g**, where g is the exact ordinary-volume centroid computed in Section5.

The canonical table uses one ASCII space between integers and one LF after every row, including the last. It has **2810bytes**, SHA256 **`da2708ecf0e184e87293f6fe7cb954520ba788d807a6e640ce2cf5f1eb3ed113`**.

```text
-37097271211 -151784927093 638841110308 1000000000000
-496594655170 -178665095919 -208022022372 1000000000000
-103802543572 -465138402103 421687364976 1000000000000
150447498816 -550944167218 -278169295112 1000000000000
244169587637 154136571145 -441031591147 1000000000000
-101792574063 -309408160912 569683976591 1000000000000
-205888683902 -164284505986 -437989255687 1000000000000
-77737977540 49520625527 -473027668905 1000000000000
344016537922 -212601649913 -408841575165 1000000000000
-490895229526 -198591615445 14059414113 1000000000000
-97712218075 -571335034132 234942274193 1000000000000
425175634768 -245613723134 169861807110 1000000000000
-151880865892 605220373852 293400228182 1000000000000
31951280555 535630247991 695657550695 1000000000000
-464636247909 -458621036679 82998871682 1000000000000
-155237963819 -618975913171 153069306260 1000000000000
-365571521437 -569290423224 108856345983 1000000000000
-531128014508 -129902600750 123162720618 1000000000000
-145710430128 552621971993 48916032860 1000000000000
-221363281301 120448605874 56384251771 1000000000000
165053488459 -189842485180 -17633632711 1000000000000
66539841047 293339075356 224265511555 1000000000000
-1069887455 -355979284845 -504400840483 1000000000000
345882312106 -440246607009 -161282659920 1000000000000
-158444942701 -437856900483 -132019956338 1000000000000
-168064168426 -28819340488 -2578026058 1000000000000
123304064721 25266749006 -382687088001 1000000000000
7874785980 -136346229734 287805015629 1000000000000
311654811936 454652463661 -114686228036 1000000000000
-192464695835 410076900352 164652537111 1000000000000
-239995531943 -369715269240 82469431691 1000000000000
-66054187882 560954717243 3946652359 1000000000000
-168064168430 467458806846 -2578026058 1000000000000
-172895259869 576542870986 189233627180 1000000000000
465325976158 185480030722 -10134580809 1000000000000
554799020193 -338925490345 -151552592422 1000000000000
31751638843 245604929513 7548455989 1000000000000
-77640044442 -389728525692 -389821254423 1000000000000
69220720704 138873466942 -353945846280 1000000000000
443068649163 264109616321 -158700881790 1000000000000
-22232712753 -44745880685 -294219028998 1000000000000
648219508596 -46837229311 -117995076673 1000000000000
-85003625054 1677151701 -332687088001 1000000000000
-17322854379 -72681184207 -434925835372 1000000000000
-82400955599 -218799557230 617980488473 1000000000000
-243068649163 -44745880685 -282687088001 1000000000000
256931350837 -44745880685 -332687088001 1000000000000
478790473398 43387532178 194219028998 1000000000000
311654811936 -339728525692 -343660986617 1000000000000
28251638846 -438591245277 -363186264372 1000000000000
42741197440 -220211411373 -74366098617 1000000000000
-93238992504 -374902600750 417980488473 1000000000000
```

### Exact reconstruction and actual maximal incidence

Enumerate every input-plane triple i<j<k. Set `d=det(ni,nj,nk)` and `p=hi*(nj cross nk)+hj*(nk cross ni)+hk*(ni cross nj)`. Discard d=0; change both signs if d<0. Retain p/d exactly when every input row satisfies `nl.p <= hl*d`. Deduplicate exact rational Cartesian triples and sort them lexicographically. These are vertices0..99.

On every support take its COMPLETE equality set, construct the exact outward planar convex hull, remove collinear interior points, and rotate its cycle to the least vertex index. All52 input supports are active. The complete maximal cycles, in input-row order, are:

```text
[3,6,97,98]
[23,26,29,65,75,25]
[9,13,92,93,10]
[38,50,53,43,39]
[32,35,42,45,40]
[7,8,94,96]
[31,34,55,56,44]
[44,56,63,62]
[36,47,51,50,38]
[25,75,81,84]
[13,15,90,91,92]
[70,74,78,82,80,71]
[16,95,89,21,20]
[2,3,98,99,95,16,4]
[18,19,23,25,84,87]
[15,17,88,90]
[17,18,87,88]
[0,1,9,10,8,7,6,3,2]
[37,85,77,49]
[0,2,4,5]
[66,67,72,76,80,82,91,90,88,87,84,81]
[64,77,85,89,95,99,86,83,79]
[34,41,57,59,55]
[58,68,76,72,60]
[11,12,30,33,36,38,39,26,23,19]
[0,5,14,24,27,22,12,11,1]
[28,32,40,33,30]
[78,86,99,98,97,96,94,93,92,91,82]
[46,73,54]
[4,16,20,14,5]
[1,11,19,18,17,15,13,9]
[49,77,64,61]
[14,20,21,37,49,61,24]
[21,89,85,37]
[52,54,73,79,83,69]
[50,51,70,71,68,58,53]
[24,61,64,79,73,46,42,35,27]
[26,39,43,41,34,31,29]
[22,27,35,32,28]
[42,46,54,52,48,45]
[12,22,28,30]
[47,48,52,69,74,70,51]
[62,63,66,81,75,65]
[55,59,67,66,63,56]
[6,7,96,97]
[29,31,44,62,65]
[33,40,45,48,47,36]
[69,83,86,78,74]
[57,60,72,67,59]
[41,43,53,58,60,57]
[68,71,80,76]
[8,10,93,94]
```

Consecutive pairs, with duplicates identified, are exactly150 true edges. The face-size distribution is **{3:1,4:14,5:15,6:9,7:5,8:1,9:4,10:1,11:1,12:1}**. The196 outward integration triangles are not196 maximal facets, and their internal diagonals are not additional physical edges.

## 4. Exhaustive exact mechanical census and conditioning

H52 has stable support **13**, with cycle `[2,3,98,99,95,16,4]`; unstable vertices **[2,98]**; and the sole saddle edge **[46,73]**, incident to supports28 and36. Vertex98 is the farthest vertex; vertex2 is the surviving minor maximum. Vertex2 has incident supports13,17,19. The two unstable vertices lie on the rim of the unique stable heptagon.

There are **no degenerate equilibria** and **zero zero-valued ordinary mechanical primitives**. AuditA evaluates all2652 distinct face-foot/support comparisons, all300 directed true-edge vertex comparisons, and all600 mixed-normal edge primitives:3552 ordinary mechanical primitives in total. Structural equalities defining the incidence are, of course, not claimed nonzero.

For a reference centre c, the facet foot is `c+(h-n.c)*n/(n.n)`. AuditA tests it against every other actual support. At every centred vertex a it tests every true adjacent direction w-a: strict instability requires all `a.(w-a)<0`.

For every centred true edge a,b with its two outward normals n,m, set:

```text
e=b-a; L=e.e; T=-a.e; z=L*a+T*e;
v1=(m.m)*n-(n.m)*m;
v2=(n.n)*m-(n.m)*n.
```

The four strict saddle primitives are **T,L-T,z.v1,z.v2**. AuditA checks all four signs, their weak-boundary cases, and the positive two-normal Gram determinant. It does not replace the cone test by the edge-line interval alone.

All ordinary affine sign primitives, together with the interior-support guards, preserve their signs on the **closed infinity-norm reference-centre cube of radius1/512** about g. The minimum checked sign-to-gradient-l1 ratio is approximately0.0024988506579796807, strictly above1/512. The certificate uses exact rational inequalities `abs(value(g)) > (1/512)*sum(abs(gradient))`, not sampling. This is a reference-centre certificate for fixed geometry, **not a vertex-coordinate, manufacturing, or printing-tolerance certificate**.

Define `R=max_vertex|v-g| / min_face distance(g,face plane)`. Exactly:

```text
12185427729229/10^12 < R^2 < 12185427729230/10^12 < 49/4.
```

Thus R is approximately **3.490763201540469**. In the literal table's units, the inradius is approximately1.1382387607534814 and the maximum radius3.9733219806052786. I do not conflate the normalized ratio with the unnormalized radius.

For the unique finite radial pair define `beta=1-r_saddle^2/r_minor_U^2`. Its exact interval is:

```text
525210507350/10^12 < beta < 525210507351/10^12.
```

The numerical value is **0.5252105073509101**. This is a compact, conditioned one-pair solid, **not a nearly completed110 object**. It is not uniformly superior to every other journal frontier on every metric.

## 5. Exact volume and complete mass data

The following finite rational expressions are the exact volume and moment definition, rather than decimal approximations or a polar centroid. They are completely determined by the literal rows and maximal cycles above.

For each outward facet fan triangle with exact raw vertices a,b,c, let `d=det(a,b,c)` and `s=a+b+c`. Sum over every fan triangle:

```text
W = sum d;
M = sum d*s;
J = sum d*(s*s^T+a*a^T+b*b^T+c*c^T).

Volume(K) = W/6;
integral_K x dx = M/24;
g = M/(4*W);
integral_K x*x^T dx = J/120.
```

These specify all three first moments and all six independent second moments exactly. For P=K-g, the first moments are exactly `(0,0,0)` and the second-moment matrix is `J/120-Volume(K)*g*g^T`. Both implementations independently reintegrate the translated solid, rather than merely asserting that a symbolic translation ought to centre it.

Observed exact enclosures for H52 are:

```text
23962499641603/10^12 < Volume(K) < 23962499641604/10^12;
-705232/10^18 < gx < -705231/10^18;
 112539/10^18 < gy <  112540/10^18;
  49213/10^18 < gz <   49214/10^18.
```

The volume is approximately23.96249964160365. The raw centroid is approximately `(-7.05231013299653e-13,1.1253977426911784e-13,4.921341043648739e-14)`. **Those small decimals are not substituted for g.** The exact programs retain rational arithmetic throughout and emit the full rational moment values. The reduced volume fraction alone occupies6496characters; the finite sums above avoid making that long integer printout a necessary external dependency.

## 6. Independent observed verification

**AuditA** constructs the whole H intersection by exhaustive support triples. It checks every global support, every full contact set, strict polygon sides, outward face-area vectors, opposite two-face true-edge incidence, boundary connectedness, Euler, rank-three vertex cones, and a connected single-cycle link at every vertex. Positive outward area vectors summing to zero, together with spanning normals, also certify boundedness. It integrates origin-apex outward tetrahedra, directly reintegrates the centred integer realization, and performs the complete mechanics/cube checks described above.

**AuditB imports neither AuditA nor its constructor.** It clips the rational cube[-64,64]^3 successively by the literal halfspaces, using exact segment-plane intersections and independently ordered caps. All artificial cube faces disappear and every final vertex is strictly inside the cube. Since0 is feasible, any hypothetical feasible point outside the cube would force a feasible cube-boundary point along its segment to0; the exact clipping excludes this. AuditB checks contacts, polygons, links, ranks, closed incidence and Euler independently, and reconstructs true edges as two-vertex intersections of maximal-facet contact sets.

Its mass decomposition uses an interior vertex mean as common apex and each face's vertex mean as a different face-fan point. It recomputes volume and every first/second moment independently, then directly reintegrates the exactly centred body. Its mechanics uses polygon-side tests for face feet, **all other vertices** for instability cones, and the global supporting-plane test through each edge foot for saddle/degeneracy classification. The latter requires an interior edge foot, all vertices on the supporting side, and contact set exactly the two endpoints.

The implementations agree exactly on every rational vertex, every maximal cycle, every true edge, volume, all first/second moments, centroid, and complete S/U/H/degeneracy census. Both actually reject a reversed facet and an open boundary. Fresh executed observations include:

```text
TWO_INDEPENDENT_EXACT_AUDITS_PASS H52.txt (100,150,52)
S[13] U[2,98] H[[46,73]] degeneracies[] cube1/512

TWO_INDEPENDENT_EXACT_AUDITS_PASS H53_micro40.txt (102,153,53)
S[13] U[2,100] H[[48,75]] degeneracies[] cube1/512

SQ24_FRESH_DUAL_EXACT_REPLAY_PASS_NONWINNERS_121_NO_110
```

One combined invocation exceeded the tool execution window after completing H52. I then executed the two per-object invocations separately; both completed and compared all exact data. No timeout or partial run is counted as a completed audit. The embedded source capsule was subsequently decoded, all Python sources parsed, and all recovered source bytes compared with those actually executed.

## 7. Exact shallow-truncation negative control

This is an additional exact solid, not an110 claim and not a universal lower bound.

Take H52's raw vertex2 and supports13,17,19. Define:

```text
n = N13+2*N17+3*N19
  = (-1694394592366,637170864113,1111135747244);
h0 = h13+2*h17+3*h19 = 6000000000000;
epsilon = 2^-40.
```

Append precisely ONE row, interpreted literally as an integer halfspace:

```text
(2^40*n).x <= (2^40-1)*h0.
```

Keep the preceding52 rows unchanged. Recompute the full intersection and its **new exact uniform-volume centroid**, then translate by that centroid. This is the entire deterministic definition of **SQ24_H53_MICRO40**. Its canonical53-row text has2914bytes, SHA256 **`beffb8d88b6a15c3766ce37be2e9d46a77fa8b57596545f2b6258e5677d2f3be`**.

The independently reconstructed exact census is **V102/E153/F53**, S[13], U[2,100], H[[48,75]], no degeneracies and no zero ordinary mechanical primitives. It also passes the closed1/512 reference-centre cube certificate. Its beta is approximately **0.5252105073504467**, still strictly greater than1/2.

For its genuine minor unstable vertex u, define the raw all-point relative instability gap at its actual centroid:

```text
gamma = min_{w != u} [u.(u-w)/(u.u)].
```

The exact executed comparison gives:

```text
448407486820/10^24 < gamma < 448407486821/10^24 < 10^-12.
```

Thus gamma is approximately **4.4840748682008164e-13**. The corresponding H52 gap was approximately0.0010047712950665502. The gap has fallen by more than nine orders of magnitude while the exact class, a macroscopic bar greater than1/2, and the certified reference-centre cube persist. A rule requiring gamma>10^-10 to count this unstable vertex would omit a genuine, robustly classified equilibrium even with the correct exact incidence available.

### Why this is a mass-correct geometric counterexample

Let v be the old raw minor vertex and w1,w2,w3 its true neighbours. Set:

```text
a_j = h0*(w_j-v)/(n.(v-w_j)).
```

The new cap vertices are `v+epsilon*a_j`. The removed tetrahedron has exactly:

```text
DeltaV = epsilon^3*abs(det(a1,a2,a3))/6;
g_removed = v+epsilon*(a1+a2+a3)/4;
g_new = [V*g_old-DeltaV*g_removed]/[V-DeltaV].
```

Hence the genuine centroid change is cubic in epsilon whereas the new vertex separations are linear in epsilon. Small raw dot gaps can therefore be produced by collapsing distances between competing vertices without cancelling the maximum. The finite epsilon=2^-40 instance was fully verified; I am not asserting that every integer k or every truncation direction has been checked.

This is a sharply scoped obstruction to the **stopping criterion**, not to constructing110, not to adding facets, and not to using normalized/root-connected escape conditions.

## 8. What was actually tried, and what the numerical code does

The initial new-normal screen used the journal's N80 Fibonacci directions and `q_new=w*max_i(q_i.w)/1.005`. The strict origin-relative polar witness survives by construction, but that does not conserve physical moments. I used the actual intersected volume, not an appointed origin, to evaluate and close or incorporate the centroid in subsequent stages.

The main constructive path combined a mass/S1 phase, additional edge-midpoint normal cuts, actual-centroid constrained radial-persistence descent, and joint primal/polar persistence descent. All support vectors were physical variables and the hull was rebuilt; no fixed fan or permanent all-old-feature preservation theorem was imposed. The smaller facet count was not used as a surrogate for110.

The final useful operation was a **three-stage reserve-conditioning solve allowing exactly two unstable roots**. For centred poles `b_i=q_i/(1-q_i.g)` and centred primal vertices x_i, it maximizes a common positive reserve in the all-point escape inequalities for every nonroot pole and every primal vertex other than the global maximum and the surviving minor-basin root. It deliberately exempts that second U. Consequently it is a121 conditioner, not an110 success criterion disguised as one.

The complete final-stage input `dual_e.npy` is1376bytes, SHA256 **`0e62babed17ab0ad1d1517251e58eb8441df5ee4cf443ac434d19c64ee82b0c1`**. Its bytes and all required helpers are in the embedded capsule. Three SLSQP stages,100 iterations each, coordinate bounds plus/minus0.02 per stage, t in[-1,0.001], objective `-t+0.001*||q-q_start||^2`, and ftol1e-13 reproduce the final table after actual-centroid translation and rounding the52 support vectors once at10^12. An observed fresh conditioning replay reproduced the literal H52 SHA exactly.

Environment used for that optional numerical replay: **Python3.13.5, NumPy2.3.5, SciPy1.17.0, torch2.10.0+cpu**, with one OpenBLAS/OMP/torch thread and torch float64. Floating optimizer trajectories are not an exact acceptance dependency; the integer table and standard-library audits are.

Other executed finite searches included direct110 reserve optimization, metric/projective physical variations, further basin cuts, and root-connected escape objectives. They produced no accepted110 endpoint. One raw-score110 search approached a zero reserve while a saddle and the large basin remained; a tolerance-based S/U display was not accepted. The exact microtruncation above supplies a durable reason to reject that mode of apparent progress. These finite failures do not exclude other normal architectures, support replacements, moment controls or intermediate equilibrium topologies.

## 9. Concrete continuation

H52 is a small, explicit and conditioned starting point with116 additional-facet slots before F168. For any bounded3D polyhedron, `E<=3F-6`, so keeping F<=168 suffices for E<=498. Actual incidence must still be reconstructed after every operation.

The surviving geometry is not confined to one tiny edge. A numerical descending squared-radius edge-capacity filtration identifies the minor component, just before merging at saddle[46,73], as:

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,27,35,42,46]
```

These are H52's canonical indices. This component list is numerical surgery guidance, not an additional exact certificate. It is recoverable using the included `geo.bars` construction and the exact body. The critical support groups are minor-U{13,17,19}, saddle{28,36}, global-U{0,13,27}; support13 is shared with the unique stable face.

For the minor ray, the old-parent one-wave noncritical-cut calculation selects support13 and gives retained fraction approximately0.5663284944428044, retained radius1.6318604778130001, below the current saddle radius1.985478371564609. Thus this particular ray bound does not block deeper noncritical replacement. It does **not** show that one cut repairs the whole basin, preserves S1 at the new volume centroid, or avoids new U/H pairs.

The useful continuation is coupled replacement of the whole listed region with genuine mass compensation and changing normal coverage. Normalize escape tests by geometric displacement, retain a root-connected/topological certificate, and measure the surviving radial bar as well as the equilibrium count. Do not optimize the raw gamma toward zero and call the remaining pair cancelled. No impossibility for E<500 is claimed here.

## 10. Complete executable recovery capsule

The following is a complete standalone unpacker. It contains the literal table, both independent exact programs, the replay runner, every helper required by the final conditioning code, and the complete binary checkpoint. It does not fetch files or require the journal.

The decompressed filename-to-text JSON is **29750bytes**, SHA256 **`f2c4df10c63115de09f85720829b4bdd2b6a0b079700790a03b738de51fcc046`**. Its15372 non-whitespace base85 characters decode using Python's `base64.b85decode`, followed by zlib decompression. The eight recovered entries are `H52.txt`, `audit_a.py`, `audit_b.py`, `replay_all.py`, `geo.py`, `margin52.py`, `condition.py`, and `dual_e.npy.b85`; the unpacker also restores `dual_e.npy`.

Save this full block as `unpack.py`:

```python
from pathlib import Path
import base64, hashlib, json, zlib
B85 = r'''c-qZ<347YevgltSlQ>AYAzBct+wmSd@xH`y2qppqh(&+|80<K|{Z)0hHn1~u?wotSH*>~Ft?ugT+PkZy^YquDp=BoX$zP?v@<vfp
i$)=<Cp1Gb)S{Zt7u0MbUoeWQQY;jVoRLtK$Ui@vY%ZHC8b(o9i-~luP|W7@IVGnR^9fZ|bA@cSm@O8I%cIhHRVxBCMOPDPJ*OE3
-OvmTI_7d(R#UQCK{ZxKshW{176C6+*Ar<&$?MQVg`qIFUQ`NsMbGMruB{BzvU$CbQ<Quj9;Ve|Ue%Snky8p;0HdpVA*&V@Enip}
SWr|2x&v4k1~}(cwOCNH#Y8@@6|+iK*LCfM>3{+{Ad28~FpZwoG%Z)m0gPO(sKaysH~#`DRjpv;b9ulqmoMsuo;P69d?KAM<NyU#
Q}XI6Q4GM!06qbm66vh28LF1e8HECj1M=sKTCo6xTjd;ZDhot0vTVAn3M|yLqFzjBs-oozxq=2{TOOrpDoBND=s1^A%&LZ_!_2va
Q82QAFg(nz;HaxP_}4&yKt~vpGxA0@tEfN`J)hGRHLK+T*X40Vr3g&Us|6rku8;?8vx){!5?Kvo6UYVh&#g{YRP?+CQ1t|$2{UK)
oNi<jAg4LF$irQBWe^az2x}>zVCAxgQq*!eWL-j6ihzQW&lYp~@+d%C2kOFf3d#}iK+hL}DER~kJwgLHRaX$yj4UwIfSy1@qgVu_
kl3)stdi67`C=ZPDl2>jNE)Dm>jE6}hEmXQO6UnB0fa$!Rb@qjf!0b6*pvm-68S7}OVeQHLLs3S02-?A3o@kx3GyJapo(gu0ICJ5
3VNm|vIRAdpo%LKX+Q)`DFES63}I431sru)7)U(`HY`}f6|9Ua6pHym9@YTQaw<p`Dl&{nq%~L`h)fn{Tp?l_G#Vy><pV0|oLbCg
3x)!-;W!Y;B50jbShZIwkQbJ%fmk5VK)+N4D52wgK;Z)DEQobpU)AYc!B9c<b9n`%7Jfj{KyX3VV4wkJ2xM9*7^}trx@s^bNPJF1
jRaH;Bd;Rbx&{K0g(;0yx}-HE0+37rd4V<Ma`_ynsG=J%FbjGCG}E)iRq@h+pqdIsAP4+P>tI9B+7wl8YQY$T5@rF;@;I0P<fs4~
fC<#Rt^jg59qbs82?POV%;l8)3&u`Y3tB+|_QDK$7Ni-R1=u+~0W^Y@=FxGiN|=sT9!#r()4@tqFnk3SI0`NRd;utxR>-b$59~JD
D3Hknk{jUTdeA!SDzlRL+^U`$*&?_wqX6QPKxI&}ARI-MOpsU*(mWuUTb&G4vVelGWKnfgTnL(-TtY(?E^7Ilv1;qUSOKsCKvxky
P#is{lFc$#1CI=V2>*LwX&|*=r$8-%!LT?KQWO`om<kXT4N`H{27yGNGet9(VAi|{+y=1%Zf8M<l{`wrsywUUa&?#i6s&-lfie})
1E7W0!GWk?+|X^kU>m?==7EBGRzb2CbKoxWI>-llgaY7E%xU2NR%Zma4U8=+j9(fWX(bD*)R=@JHed*VJ*zY33kotFJZK)Z8#Gh_
(`TSV%_^Ykh!H5r3TZ$T6)@igaHc5x;68G?4u%FaA<NhVXct}}X%=(_%vllW1GWXE9%34xq{b|b0Y1NgW^lz@0rOxnU={M{L(s^A
loS-^_CfdnZ7^E;OU70~cbEqU09*#2SA?+%^aEfrAvh_lID;%O526sj5Qq*E25~|jCPQ}(rU<maFtq$C1Bxh5;88&cQ93}j!SX5~
(`Zp31ON#D7qNmNcpNaWAYowdfd0iI(p-Z8k;ecK9AcQEtkPcxj}I{gNQ`g^U;|M+P~*Yofx83ETh;P37?1+$H4C7?RzlEWpnFCx
f=7bTssNI^>Vgb(S@68TFatBF>kycN>fmZ23Id0YUTSqdkOK&QvqjWc5J`~!B8CZxyar}14+KWrwlwN5@|QVn+LM}@87&}sZn?uj
qUD;6i9K|@ggqDy-AUp=G$c$faqz=oo$QI_PKLvN(5W#T)NRLP14W;KIqCS1+l?maHwNNKYw9#&qg|^xZCF1XaqBHS()ET8>6l)p
Z`Z}J5defcf6zJH{&1jg#<M0h+nLk`=Dg-j+*;Fa+Y?Vx<R4DcY9*S(iDZ(xTym|+)O8ZxbRf-Bi$rVaCgx<3u${!CJz`zN2ya@C
jhIYFeM_3B|1`#IHeVXE{--g6X<zCQb7@R3HRoe+gekf<+@a^iCXmdET20j}S~YFLAGlJhL|iG@rtqgkT&dWm@~1v!EJhj92!L{0
@yW1Vbes$)W?!0lOPC@hXO&)+p*ur#p$og|;f-rLZA;R9AaL8$qd-h&At4H>2_H1UK~YJ9&LkM#STtbD(ZnNm(<6>t`T^*=!x06x
Oa4@(XDw*o9Mqd;qFXZSp5#=zRaq{Zb6V-LS-Mfw5_T)meM1pW72pA6>Va@sO$jH70JBRtb;Yh$%sCLSO2Rv}T16Zaj8L#H$tGRW
WB4T)bt&)5hIIK)4`)mGoU99=z#x7hr=*4e&D(H}H18K{6a8Xi0djvxE7fwxhQDx!tG02~uqKApL&xr0iN57X{h_?60wbCn^Zu}s
28qER5GGsRph~Gf%#4O33Bdx~j5!)v4v<HV0(PyL<$9cI^3oI?J2pkfW>er#Fh$1>r-19|6b%Z<l%VT6jKE*y64z-irKqb&(FW3k
@GGPO2_I;&2QtXchEi%|1k!BUE^TCN5VN^7upJ5HzASjtsB}x!^+u)CtqL&&xtzGu#zb<54}7u1>4bs}k^+(-|5s$0iyTsf4U|E$
BO-!rC{HE5O4xNba@}Ls<)%eLjm4or2xm9}!7Bk)6Wf_u*gB$IT`Oo_e7FEAqSYjL)Qvo9fGLVR>O~$gqgC}MZCXG;z$V?a%AkKR
Agz*-|CFgU@W*8f7|EM1z)3YNMjMxj3!_{VXCPq)Ehx7u2hxNzt%y+=F$Du2`q~No<#NkxSRQ?P4#>`cTh4S~x#q+Q8N~G3SAQ~!
_X4Q0FH%0rlp@Ymu^{9b3ic+|OKeUcD2<yVHV|<XVuS6h>ko&EP1_m{tckl|NRcD5#~(BFOwR*%n%LV^n3~{pM=)8I-Epf~VH3nD
SoP(NE$FBuz?l7hjQksPFNLdFB0r4X2ilcQ*D|T35cpRvBTK;B1F<T+e~p3mjYx|$@Sb6wff!)mNu0jms<{NWB2wEz`6&yma8V7U
V6a5g7!XBD`6H$Zyf1%3>60z^y2P=gfL{*d)n2Oe%!bc=$>&0Q1RCE3-N#?4yROP>d@3*k%btKg015Z;WsYzLra~}9r~$UnfLx4r
%<;noF=uQMT*%Bg$_-AZgiqj#S@q3aOD@;x5`txmqWL<i)De3V&_Y)voG#Y@u99+jAHyGzFmu|UNYIN^s<IDSY7r4_Bod*IZg5l*
9_1wDOS1@{aVBPz15$XDDoAiPm`$6o`ks~WHkD9#87X|i2ysDdW*&~(52Pg`4iE`Ysxj)$JTT1_wN#}PE>(6}DG77$)LmL(_Vopk
1a#O0CFsS73f!p6WxT8NJB*+}q%4O%DbHmO$ls$d8#Hns#ac=}=N=Fmj%Ll=EmhMvyo7%k#0Qy!@yYxkhjieQZ8<`&K~zJPPUFwM
ypBIy`(gco@oITXA|pgacnJ>Pw+5lEam8e62^OK;@6o4jDWq1{UyogV_SYzS3yGxMq_wK$&<WbWe1cNhMJK&1oc&&e(r^<cbRuGf
7?T-~1KI2MGBdM3wLlbrh>R(YHJ?bhp^*ALS@t>9x4j7`WEf3^oC;Y5)BmTO3e5~m&m1>Q9GdQZ0_5_|_P|6t60y~{R4JbX2H-Oo
N(ip?P%!<#(wEPO!Soj%$XdkysDu+YtqMbdPQFQxc+5hgmJC=?t(G5xP@owo>cgf|_Iwk_9)UpIuG0s=7^!i>eES3OA{HSQs0+h@
?fqE$XAB1VRREQeFfd4YcxU33iC1;Js^e7?ubOZb(TQ7TC<J+L$qD)FlNSOoyS0#TXU8UY%?FD6I^F^in%S(?7Zapf8D*YUxD6bb
BMEkV1onQTz74W2b7}WD)(@Gc)fhG*wByhFwu2x7XXFc~3&JV9EVwGL^eZkh@Z)qT?kn$6*w9KTX$EsS!vThQs9L@|hJm5fL-<lY
@^J^erCDlEjy{f!tCpDv($_+UAA*Q9CY<Fq<=bcpH``J+bxTqwFz+^n%MTyg<sIQaW^fbEeIl1H=yqzad=54i8~{qlHkrv}CxRfe
wzmy((jcE3eA;t=TA#-a3Sd%t>Xy;-q!D!nod&JI94rh;hp~y6A`EDJU>JjUAX-4Nxx$^y4gNXAKTWHRKaZ9>1WjyDO&3Eu7}@U!
H)1d5V&E;!NZU1=T(p5x6!)ySFO2RvS&ztu?11$EBESG1Ygi8Vd8b3i^1*|Mxy=}SXXx~Y4YQv>^hEGD1MgYF`*o_aDQFBY(F<tc
u~;4_C<Tl0?UozG&i&hHEE<cI9Y^?iM=pa2V$=c@IGsW}#K3R^fO}#}Td@E=F`$ucN!b|)paTF(J7}F!j+2Iq7F-O<ZI^8eE{HEv
&H(0T_Q%0NGRMVV-%Li7g4KqUm3;!CNZ<$%iqcgibP{v|AHqgP1j?MO5S9V6`cZJm9gry>VkL=mNRn1n^!2P#oE7Y}fvX1JZ{V2@
f+8>@6PDQq4;kZAhnvHt(D0ly?GLOG5g+&B!btM~@f^<+Ok@E+xUv2bS=ol|0y>A(g+(!Pz`pJ#+<*U%sq2GVp)MHwi8W6W``^%a
^H21}(-)c8P9s9OAp8t=-1Hm|WRQF!)UG2Lj~N*)B;z$r2PA!D-V>>I480inu913WkYvjD$`f?cK{&>Y3ZNiI^&}E``1+W_ivc{_
bOxX`Obk@&tBn6JP#nAg25Ye%4tpH*aAaT0ugP)xnqZelGE-&$N@Jl3GkLb<;8u?-swIbVQC+WyYk#I=bP4{H7T#FC&*j^KnHqp*
5**cG!OeD@odE`N^#vV23}goQS^ZzobF0|~J!ioGmo(ia9e)(_;Na1gW;l>K<RbNwN8;xR43uZKEQ;&kW94#d+V2OAfvbQmB2|J-
%>hJ|S}N6p9XEC@^|<$$4f|kr=z(-ga^R0sI&ArY1@6#p(#ipF3u1*>XmV054<HI*a)QsbEDp=Ydw9TW2LP}hs-|EUBhm#{FHRqZ
EN1`Ac6CE{06<ZmMkE>moma~?kUny(i=o=NEXR*y*?6>vW!D`JC#*a3VbN}_(g8mUdEsmV2~4=dN@<`qmm1JTKm}mcR4|ZD5E&fa
GXVS+fxxorrb|VTAWn{Mf?Y1&9m1W;tk9J5olkg*dV@pkHx#Fr%OINc5X?$BV(QP?f>+HHvt~<{iuH{cE5uAqb9y|IN0}U_j#GTS
Q>FuN6Q4xHnHWqb?9?*R=va-Ohr9a(>_w*_ZHt68w;EG0s~I8Zb+gG#z*8#484&L1c#J5Q*lsR3B<35=m0lq4&*TZhj#r}_q)+P&
T^aez?K)syS`C`(BFeJn4Qn(>Y%>!KYug9Dxup@9<Us#j(}ox?-a|?T#4sBO!D=QWyTzt0b_6UuBBP;=x)N?1I7QId1ZS7~G7);n
e@LK${sr-MPW%#~Vf=?&(JOL8Z^$7%gb1~5IV_NX4Pl#LpjjKa_Q0OlGnf+ZNn={KYG`ez9t{iwVI~Cskiek$7X)<SQX?oa@E@4F
hnm+hH6uqwMlQo|K|delOvjoxZCD>}!*F8<Osdr!b70kKlqPGnfoVInT9WPWsMzsg+Rk*_vx*AxjOXW1z0!<tNC~$YQJ(jhaYY$R
B9)UQ$?2SwpUZ5!7y-AQ%xq^cdzh3n4=w<yO;B90CDWV^MjoCW6LDZhVM|AlEj2J29=&#_+<XHCVV9QNzS%pvu5H)Ox38{}Y=`bv
{HZ~=L<3`P<esq{?~^bH?yr(nlDuJ;H+Xr-E)Vf?k6ng5#5QD^$J&>ei4T#L>{*1T*!~ql*8b4MomG-c6+@t%Bo*F1m&2SQ4i}P^
tis?+EixKza3t_O(uj9e#tQ!?>hZ#@5sa969ZtuPj0fAh`<xU$X(GAj`ajJ*U;ba^p8svSc_rCwf+bGX;ZG!C7Eg_WC!cyRq>piA
`i~<={Z|LB|8bxP`&8&hCQBnHFK3_s+o@-u3+}MdD9rqWi6H3~W|!xFcA23w`*U&`;YCx+ER)R>UjA7zcPjB5b0o!VjwG($BEKBT
IN>=Ve+Itvk9p^w$UFB~-Wm29mEJ1a%&dipXP7916G;&`^AarItde=9j*uE1u%lj>(e<n`Gl}SHFuTc)%ef=;qFYE7R6%FHZw&LY
-bCJ1#fjgP%)k_~#4P@()$))^GnhO*#auv28UYS)UB@i+EV#yYzYhlls~SS|UUx0CC$bEaFt>|0BJ}0iLcS)y4W?#mU}<0e2n1$b
T=}WrcqXaI5*QL!Aj|<1JTZm1M>J@nL0--I`WasTFtX9N0gq;wHr%0?QZ9>GF&E4;kY1XT1w>AvKuYNy{}gMnbpIIMSA$GtnMb`r
%F>*#9KSNww)tR{_{YI5nhvuDX|?S5$)Gli87T!w%nB<nD16yJ;io9zl~E`bVr2*eI61FU>a|llRXi%<ks*w6{A|wa=~b5g<MA=3
{Fpy~E<=zQ5yMwcs}iGOe<3>lIeC^?&69a1MF}wFbf@gq*>xSR17Y+`tS`VBd?7PKNtNI!-@tkGO+`-N>49f%`b`^(KW_p81@i+u
OM7*>JfgzraudoW4bKn2mcrA>Tq7BY5EprY7VbwQ&jeONyt%FEFJzW-26Fnm!$#tBMvkPXS;}-e2?zA}0B8%D+2hRQJfP4kJfde!
Y~6S^-rA%}Bva&{Ixkzp*Ag5N`3kd$2p28p@=kXoZ|ua5zhzN}^E4{GlK;g{&*c_$X_YF_wKA$krmRNAO`sc-I{A6&05z1y)iRJ4
*PCb+NG!)6B>34*=?~fccvc^&!4mb6G(9Vm*jvg$L=ybWF8T?2SUOLWzp7l%WzTL}HNN%mP0w_&l%xGWO6doAZy@I1<@H5YzmwYY
v-&Jp04x8WC-ejH!w4ppycga><oE;XFx3_}@r=IxvQe77kh|w5LFCeL#~yMbnyruL^KCK%d}HZ*))dco`pJ9HH7b0cMf~|5#C+kh
u^Z3cv(XG9cNFj>n!oqgza$>GO|UJNR*S45$Ye$&LG%m`JH$QsUP}FIHB9QiO&o#R;4<N1f5EaTBEcq38WL=-L>(RL1f90n8VuR_
vORzvLaMM}#KY4F9I;dsB<cfV5g*@^YvSCUMrtzN2iNtOn9o2xwTQW8S?y9VT_wgz;8~TjcsV35YDUmq=2_>EprJA{#~*Zzr;PEm
c|{}JJRjp9EQ@1heyH4J=gz5=_IE`THtELZE%8(XOQCmpF-4c(v6{T8!&2u6EmXE6l)8tZ8!xWF23~<h@iGhrF>3L5^&DO--Nc(9
TpJ8$7G@&YXmR?>v3t+^$Wa-dh=I#R7a{3iF20D{jU$mK01s1XMXjVS9nrH1n>(Fyq(I}3^%=I)qffI)g~seZsL<#|D>N`@Z&Z4s
LZcU}(12MgQ_iv(pA?J{yPf`%Dh=qrT&KYh77UJ*Y(P($AK))B926_g@t}lgh1rRqUSk$#w7@$Z)Pby4Zs7c(OAh$#du22oZSGuR
P8rP);BTXa7+G^BFZdMCZx`%v1S|v-sG$qndne6$ffWNGfmOClhZ&q*Rs_IhhNOhkc`YmgN@9|o1&t%J8+Glt-{KFLs{>%WA3g|C
EdSR^PGVEU&ITI6gbg`xdA-+MUL=3EBzV>G40L8lSlt;bQW4>Ciwxy(pJw8nA2$yp?g}edgu9=4LG23j$tNP*o{@)tRlb7t>Zuvt
;rRjv%Bcz5g#qb|m&bgkyQ#hMOBF1aEPL`DvnQl-DNR_?<a;EfJ*o0`EsMRfOHbG%%#wT$vLrm^6RFU|49P1MGA~rY%$KTQ*rsy1
jE0?p{x|DkqPyjw8fNn6YM9B3)i4u3<urM*8YcAWFUHt_)mPFcE!*`b{z3UmYG1x!IPQ^`YIc}mYI6+@5tBwB9_coo<fJZMI(v#^
ikN7mt#Mp5fs7Wx=A2wC)y;g>DE-Pv-iE6RQ}QY|M+`{N_F5^-zlh_pGKANKbQ+Ycx0A*OpaU$|$FS1?rEFn}jVqvoiA=we<Zr`c
KNvn=3E4$5D_XCx6wu<NLhG5iaU5Be|E?nBKP>V1V@U?B;2C1L!56y>9#TfTi^N^G8m*^TDyE26NBmuBL?kQ|VPzP@yja8#Vu|^|
FgwUf7$PqVC>!*8gC55m@FO>|{*mypEU0dgYb+-~GCT@0i~=%<WNmE4z=|kb5iijvaR5ptal*|Q;U++eX8}gpxZXJC1=nIM>=sG)
dAS}SNZI`%r~m(5ZgR<d{U0PI|4BMBlq)|i`8CW)wu4k;%)b6@B2xYzqyb||x1Imnq}$)-&*H@yvHV#q=k*u)3rS-mUwCHg2mAMI
ge|aVWx{V`k)Ugh++lOd6I`&Xopd0uw6V{jp(O$+w$sMS=e7j_=l&eGyNq}Mf(>jAEuM*UEUTF~oes_yByrWS@dvzHqeJjqbJDTB
1WX5RXaI0HPC?RZ2$DARGL|#5-Jw%So}KTX?i_Dl)lP3tYS)LC``dd!PnuMdOZ`sHU+VID`b^ve?{$iMpvh=~IX-6;B=B5_x`7OS
mTu~ZCv9sOB>pUn;eR+IUNc;)wO|KQtI3&>>B6HQ&X_u*46v^$jXorsQ?p;QGR|m$YVum}IHoX_G$se&IV^&Ei!tT%NMpER;THgH
po};*R$MMg(7<F@RZ=NcOO54>=}i_R3m-sxE-Mqb!t6Q=v&J&vJxLRL(V!RlHY|ZoCNo_Scqy3>7Z~Ybsv4%3<@Mx`A5Jn_P$Qx<
TqTH3jh&@%;jx<dWt?~_9Fz7x9Is=(kj)3)^1|s@TK|XRZ@gd-O*Ty}uN16COR>~K)+*rl3|hICm2cFGM%K`jx|uH&ngu0q=B!*+
X;@mLWwcbQu3Jr2)sqC^1Tb;IRG==9jRdT~U2YbRkFNJGw~uSMz}>S`un|XRr$?usYM1-x$J=+clkMx>Lk4+8Aw$k*>IDN-vVZ+$
yMMl}q?G#ojGo_~EY>&8hwjIX-O;9^?GATuQ@8iuACJs;Z_6LQr$*mY_Vi@@xIMh>Y(4er`IMsHcD~t*-FtKGaQk}Nc;2q}zmB#q
U8(bL{~Qm}H`eo))YilIpYEI1_3m;0^ymBh#`D9OF@OGDJpO(2dzjz8(ahG4*Sh$6*wNmcAEX|iw!PHeo5qv1v3a@3x*Jyy(%|ac
dwRa=EbQFAb=S?^dDLnd9oqf0*8QEYy)AsPcAu2bdvyQ6TP#u&J%9dvHowrW?u^0Rmh$HI%g4*j(b2fR{p+MH8(;cAwdW`I;`8p8
uTpDW-uii=?YP<J%Qri{$u)gm+g<CHzyG>Sy}dg7_{;cyf9{kIjvJp^*K775r~P{F4G*@S#_!Bco%YY&e!E|L-`IFQD&%^zkJ|lZ
c5vy)_dU8L?Hr`2q}9H{4twkK&@kRVyxH{D>S=3zar(u1JF+((He26*-x`;n8|wFi!6!G}dDpmEKN;K)zcugZk@}|h&1#!hdxiT?
hhL5jP5Qki-(BpR=k@EfIXIf1)_#|-jH|P8%^Cf?Uq2Z3H{}{l?{C=swePaCSuPlQp}COGuFjON>HdA=bG<$K`BZP%wzl~$*R?;k
Y(;)J`P|fYx30~DgT0@ZM&bL-e)jTtbM5N7FUfD84j+bxyAKy1yJN2~wzl#qz~=hr+P=Aavbea=9zT8D>)bfyyYEJSb8=nYdw+WW
J#TE<hmAR{)ptJ?>E7)5csL!u?WBLr3Y&$`n@8tcZ@TXJ$<VrgXKhP`wQnbP7v7h1U0R!dSw9@rZU@u;LF&!@{lnXo`}^YicWLo-
H7egs_p`O9;`89*_fhTe?(yftv9`9UnA6dHiazPrA7xuVyF4r0JZs;d9(GQOpES4gIJmg~(kWi8yEEgr;T{(3)24pXp+DWH<FQTe
-H-a+RgGHG_;XRSbKia!7QehTt)<Vm+wZ>LUwvD<{+Qbt{#NBLZ)T@OrMva6rtECaypz_&%p3jsa?!f$pUdmCO&8y%yTkAIkNtP^
#@qeQ+9+k%Y1-9)9Y6o-=Ra-UkKc`tzBylxJ{9iYJsjLM`giI<p{uWdljhIqw`<aQ@#_8FdHrE@YQAx^`>j@5aewdRzBRUT*Ykt!
S*?8YzBlXI^xHz;${U?@x$%^e-z)OoNn`3>{oL5RFp63Cqj9&DeYo$uAEuR!!-Jc}VCU+#cGrFQd2w+1?c!VE)N{Vs2elpf=lgW7
pxN4UdjC0JmVR1ae)rctrtN$yUH@{j_B`Fy4~~Dj%ItJpK1kcWo$iHka+&^gcfNbRel~Yzx8KaUUM!#L@1)NKXKntiyT3Tx|JeC<
`X#HapAKiHwFMr3t=%28m92r=e{;5fH+niM_AaIRsMtEp4!<;M^Qf_AZ{JOnE6Kgn)|}JY#@qG!V*YgRY#yv{J<ZGX=I-ol^7d%!
>y0&?K2LMko$;Ntx%p7AyV>`fuD82=voX2dAKbgSkG;i7K0lVqyT!|&HRB;|X_Ee&`hAdJ|MGDDeBRnTG7Y!&`7qVG>Z#gEPr5m}
o&0X}-%oZ<uln7^nRnUw^xRmxJHEc1=7#I%U-I;GZKBt`_0#^%K^lz0;q97{x_p=ae60;H@5XdGGCr<57wgJn`g%NnY`@!5Mthf^
9xwK?7rWX_Kg_Rf9={vx)3wgd-TQp2+`YPd(=nUi(@u7s&ZV+Df8Xif-PGUz`dz=<w&(9=_uBCN@!{I+-S+s~SbLZLn%g<OpG@};
z8!zDZVTR8@BP;IlYO)ID|NP4?tHzhZ#?`|U1R<xt-RYiz1PlKmv7%6e4~q_i%-M-!J~P$abTRO>s#L9=DdBKyKK#GH{W%C9~qmq
BhCDzn99f9gOiKm{7C<HemZ@+w?B0b*H6x;+J^glum0RA&mKp2)B5+HpVuD-_Pze@=l%0x?)Xxve^I{|^|#Wj<4iA}jdAbSRQfsY
G`3D}zW47R9k*S#$GL;acjnC?0OEn=tHG1ku))=N5P{hcOp0#1LuY2q4<QEekCy6FyWfOh1S6jg4WF|>2e&hwj5VI}oJplb(rPt>
yF7W5rd2DgDq>gi70(#Oj%4c8hf@IF#F*2uOgA00u)WE|wP`2g0ZM(Fozf;oEJVYox1I5Z{TW!23iPUCz%;~DDi$$8i%fK)LWBgE
l=yLo#m1VhYc8aUWD^V%x?*!`6UT|~H9Hx{vfG{d(DkBkMzV!=H~FU98b=`VsEj9`)Fz^UyKVgGR^?dQWW=|d4IIp>_iBB+2MdwQ
4QGOlbsM6pDV}t>cE&Yl7Wf9-Ps7sMlMdxEA;Q4fo6QXDH(Cu6?TitoHL^@Bmez?mw>_$0cDnHa;j?_$bRfZWKqH_K*5V<FCN>R6
S|g(QL(46jT4NtP+cnOxt7SWQESj{t#O|gy?Ih03Ul1NuCUyl$Uro0fl@@-_g14wai%iDsXG39gR{&_0@?YX7{`lt(;t<&PGy-6}
PW@$U%n%<|*YzP+{)%O^8SIDez)5i96Cfp->-BZ$#hxni2PvESy1Ydm(=qAL4pN)Ke`G{Q1SAWH1=3)R36OAN6ChX1Cdf{t@mJU)
w`p7UHHq!BKrf}SL%2Q(rDG59eK9JO&5_F!+N>mDrew8@Uuu93EAkIw#@Ztauqyr_Z@gDb<am0hhRGB~K$%z$Z1tsy&uy9bB2i-k
-nXD#(n-@Epiq5?jfzMYpbd+M-Lfi2Wh`JQJa5@a#!6fvTn4NS?*)HnR5DYs#YdRR*rj6PV>XL0cJ?Q}-ZH+r05;=+(Q?_lpA5`;
eWj(b(jp)(x62<i6lL4Na~BhFNVzV5D1W$3x8wbzqD4leO~kms;F_){%|W`Dh&WW5r{=+8@jTBOWv<H>#e%;ymj0EGsbr<Bpbs-9
c<?TzS!rPS=)*BlfG;Q(mNlXHaD5Wc%PKd_5tZ;!3jg?{(EhTmGJoAV%z(}@Cj%1Fqx?DScSj3gL%kk(y>d95NOtsVFT5{U$v4z4
1vdgjC1|LYZ5rG}-fOh|V^51&W;DcYRuh>9>`4y<n<inyUGG~-@l_AfrMNRjOn|Bt+X`x;Y)ZSaqewjctl)|efemrltyW721k4LR
?-i}VfLRsiM!=is^0X8>Ky1dsym~z-)R-~nV_UGX_Xm8yZv3!XEVf&vb|@j@^sQcxmX1D_(vKCb8W<K<A}xUt0(;1OF8}J0Z%yR#
9F55+Sxv)F8!Sqljz36hdc4K&13fL{Q7W``lGO|zG^6(|*F9RVzyn<GCtCNm>K@3S=h07@rfs(IxJn8jq(7DM48!jCYr#X$Bg{*-
<gz!Qo|nNhcM!(tcm{jEH3!Jk=|6@%od%Gn13I0)0vVKMhRd>m1TX<sNQ}|gSmVI>MDOv%d8S^om-XwKF6&kKksb$X#I))<)GAbB
&|)X$1l<P%Dh*PD;NBVF^YH!=`aeecKMwGI5K&0Wio_t-px0^||4NSlW{`fw_XNS<9j6?;m!W-tFW$n_SbJ5@T%)99rlTfCKUWm^
T=52*AW2nngHt?oEU;Wt)+ASyDme^WElUtQc!>NR5ah*xSOaQV1SJao1G7~p^9G&c>mnW%Hcs$Fj+(^447#?}5^<+Vg@^~W-%rV}
`v=KV1<jDjWSgJyngXJK15?9Yl_alj4#VzOksddZ>qFKz0Xk7KnPy~QVQBMYlDuRuWG74fpf?Ohu_Ow|&KuzKSlpz_JOWOwcB(J;
;qOp*fZ7Z+I!rQ}72Xc=sA^R#`4IJk{vjhLOQ7KppH$4a;#PfH30*hiy3Te9{sC%is}Miujh3RleB?`#YEmx0He%`Umvw&WNSB8p
5J(Ly624x+Hz~srG~17sA25N`vHR7-UO&cSVn#T%2ooN{1nN)6&U-H(5SMuXg70$xy0u9M&mBGHXoCl0xixlDEAe(FD7h>ww$V2|
FLA<XT@rq=22qtgsnsOU>bJ<4u!<4N&XYxTKD1}X3LX1il{K)J7?<Q~9EcRmz@&=zg+JJ}Y4xoMJ7hLP*9{v95&#taVdz(?rTF7?
mNz<7;TIE%tjXXXe}abD=ve5NP@s5I-SQ?h&5bf|;R|Db#nP?$$izB+T=+sRjj33wztC~TN54uJtkxd_QLkeHWz#Cr0~;_F@ET^n
5kM18Ifh^CEhNku`lhpnJJ-InAhGV@TRA~1LLECCQGxyfl`a+pLs;(uKpT*);cLtMY`M&XydxS9|G_7Z((TX_x1+%_`q`~Ix++Kb
LL@nO+z*Zu_(L_iR7PK(oM<+wR1bR9E9{M{Qgtb6)no_}&B3U~EVz}{ve?0$@QI{P>2M}+7~zfRlxp&<q;Tk_*Rz_aH+>=e*20%F
k-gx}^&vP40uhSB?H|Z2FFx{N4N?L?Tvp%EP*~Sr>_H<v7zO=s!UYlrG{o5A(+BsT5pf>$n*ZlSgqfsIpVDrWitcMv6v4}@RGj}q
Dwd}%tI%+rz!b1(oV#1F1QQTuz@3?0aB9B)E#uU5m9BH7{M7Zs<$AruI^v(yE4}OZ_7;DEi?0jf9O%9-{l*_z<om@!8sJGQEMSOk
WdmcB7El4fuIcY%&FKX5lg$kN!OvfT@x;s8a5@=HCmxNH4myCTv$;lkwYoV0brz}#X!@i8#so$uur~g9AT>w4fmOgOWCVKz8q;W`
7wlt|xcRD80AZ5$Pp23l{^2-oRK-_bfToQGi=pJrz<icOv7>KI{T>+pdbkJQ`;g>*8y~YwB^f(%RFIuD&A`eLo)qIv#KjXfDPqLa
+^)kWg(N3Q!m$^ilf<8vh(HX;5PxkmZe!^p=BHRQ1;Y5o+GRS<%ynR^<7O6&_(JAY!Pu?)$8M_MtrfHUbH#Til?Xfefkqh|;lvak
B|TRndrHo^^^BsZ7_{NL@2oRnfBCsutpbm=6mL(fnV|NLXM#ZssK^FWzW<73gv%|5a`(@B%H;*+Fvpda6T^}ynQED#L*WUoRdAmj
ka~OzjvtE<>&Pe?;g^8ECd=y;aFQ8<OOg3oC?560B?%w`sR$|)a*+(INoNTA<*VbXi*sN(tF1R#G00OA4NkI@v>n(Mkz{M?K<o<`
kt7Ufm)&O~km5gN$f_4`EFK2I(vu~yQ7{&wXt;!(sZNqj+Z!cIIQ_HCsN^T#SH(Ii@-6Z3srM{IJ}3p*J3HM644L&#B6%UE1`r8f
k^xn`_XRm7$B|g#50xk(lCe@0<T-nxMKsEreyMo8X27o&K-79X+3Z@QKExkpzaK6CxSBv@VY<yU#HOz4;zty)k|Xlg1FPe~kK{f;
$Q!;Ifp0F1FwEm;0a$f>Idu{b_M{`Kq1j6jmV@Ua%~E2t0LFvdUnOFQge4!ZN6G*E^WV|etNV=sL7%r=+`+%#&EkFWKzwT)0hvpU
b!@Ev?d#RA7J6U}!3!k>;?r?KsR64MG9R$my`U;V^WS{b;J;DvASy@x-RJ9mIR0y&tcX+9tCenbT}$!1JiF7yT@mkAzjqC^5apma
T91v^W25zIKp!mm#22T){^W{Ty_hwMnx4y%9R8o>D1}@WR!CI*M>p_`|Jkfea?wxC^THW{yOv62mDD6Gr*a_h<E`M0Qyl`m2X@09
QlP~8A8TObpj;)!Vm2C?TvW5KF`4&SVsqVUwd%meLOo}yMnli%at%w**DcK|HnTZ1pKqCkx{)`EIpBIrtK<LglV#-c`KH#=>sHdQ
!O?3BepZQ9-*9o{GY8)V#`8<R_~`X-3eHyQ&g2*CnEmfN`1Nw(;JK)pPqgW4-yw{{=e_5&VrKCBGp`K-tJ~(c<E6Q);@xugogz_(
7yE>d$^7vg(`s|}+FE%==as1#7krD4eddUDoe_=;dj~+&;y%RFd~^Sk?o*lggJyC-ZjhJ$(3?V>KPP)W*&#rlX9R?y3#<F^VIHL{
?<M5uK<dHBjrqm_zWD%`F>EV6!dh7j0Tvic9A%##K_BBuC>@vk=VzDK{wGQzrA`d<)gIOy0s|~CWv}hwi*2}YbY}!MtX5-UH3|O|
Kt&1+Ad%2NtA;`hO(qg*JE>@-Silz$vN@91t5tl}5T31wD~{D*tWFF)G8O=`!3B~x#NcWvc%wP)E&2D}5l7hHg^o4;)=y%ani>E7
h7Z_zsRnerwtIGRe!PDTK>%CtQka@Z?9lojA?*Au1o53>Mm}G1iKr$eqRN!`C7~qL4+y7uVJuwnYS<(zJ;j<+EH;hRm-?@fhf=g%
fk~^B?yz4XG34-sA|`8Wd$GM-{kpwW{kk1izk(6-Wg-q}n^(kcb1mHFm9X3KDp(vmjt$#>;TtsgIw>-Dd+8fAo9xp<hN{WSAlUa}
Hra=VWPd1rWd<}TTO?WEESZCWNzoi`$04u>?EM=qX-F!t)yq;_igw??*?5hm0QS;1hPGe)#!zMH8$<l9JO-hXWYB>K>^IWRUm3$K
zUx8gB1EGad3gi=0U2eCUQcFN_$M^{Uwo$sr*|yM64_t(4+7?sD=IjCLj}(dso;8~P<u%L*w>>x`V!aKH>3~?X_@bS)i}>3<NL;;
jol85seNt)rR70?h>F4yGv2QdaWLEQYU@kwm6=eaf>}W3Ug^f9G3dwm_)<^yfOXR#nh{^Wg5lw}umTs!&3pwpTc!NdZ=BgnhWuqN
^U=g+(LU8);j*x5*SBZ2qtm_p^L_YpdR^Q9w!I5>5^dd;D41V%4E{HxwpYFxCGs9DdY5?eLy%F9e*ns-8WzMe`4{c%X6f+Yzqf3$
<f{uUTRXVizdEe#-E1F=C5xh8TypL7?DY2N^mPC7s-|ix+}2c8NfMD@<r6Jo`PcLR0|wR?=K
'''
raw = zlib.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw) == 29750
assert hashlib.sha256(raw).hexdigest() == 'f2c4df10c63115de09f85720829b4bdd2b6a0b079700790a03b738de51fcc046'
files = json.loads(raw)
out = Path('sq24_capsule')
out.mkdir(exist_ok=True)
for name, text in files.items():
    assert Path(name).name == name
    (out / name).write_text(text, encoding='utf-8')
checkpoint = base64.b85decode((out / 'dual_e.npy.b85').read_text().strip())
assert hashlib.sha256(checkpoint).hexdigest() == '0e62babed17ab0ad1d1517251e58eb8441df5ee4cf443ac434d19c64ee82b0c1'
(out / 'dual_e.npy').write_bytes(checkpoint)
```

Exact reconstruction and verification commands, with assertions enabled:

```sh
python -S unpack.py
cd sq24_capsule
python -S replay_all.py H52.txt
python -S replay_all.py H53_micro40.txt
```

The micro40 invocation generates the exact microtruncation table itself. Both verification invocations write exact rational volume/moment/incidence reports and compare the two full independent audits. Neither needs NumPy, SciPy or torch.

Optional final-stage numerical construction replay in the specified environment:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python condition.py
```

This writes `H52_reconditioned.txt` and asserts its exact byte hash matches the literal H52 definition. The actually observed marker was `LITERAL_H52_CONDITIONING_REPLAY_MATCH da2708ecf0e184e87293f6fe7cb954520ba788d807a6e640ce2cf5f1eb3ed113`.

For supplemental logs, full rational report printouts and optional unpromoted search checkpoints, see the exact nonwinner handoff archive (`SQ24_H52_AND_MICRO40_EXACT_NONWINNERS.zip`),658915bytes, SHA256 `26441ee1a4d8f4bf92de228e2daf0b7255052e3ae92038f65dd819a2e4ecc359`. That archive is supplementary: both exact bodies and the executable continuation capsule are fully defined above.
