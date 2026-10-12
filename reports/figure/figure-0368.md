# figure-0368

AI research report · 2026-09-15 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Atlas 56 — S8 depth-two charts, three exact C624 arithmetic successors, and preserved C622/C620 nonwinners

## 1. Result and acceptance boundary

**No own110 body with C<624 was obtained. Three new uniformly filled rational C624 own110/weak000 bodies were obtained, completely audited, and cold-replayed.** The most useful new chart has arithmetic solve depth **two**, not merely the requested transfer of depth three.

The preferred geometry/continuation endpoint is **ATLAS57_S8_D2_C624_OWN110**, replay case `S8_D2`. Its primitive H coefficients cost102 bits, raw coordinates196 bits, and common centred denominator22745 bits. **ATLAS57_S8_CORE4_C624_OWN110**, case `S8_CORE4`, has the smallest common centred denominator22509 bits, versus44770 for S8: a49.723% reduction. **ATLAS57_S8_D3_C624_OWN110**, case `S8_D3`, preserves the direct transfer of the earlier method and is retained separately.

All three have the **actual maximal V177/E312/F137 complex**, C624, all137 supports active, strict(S,U,H)=(1,1,0), additional weak-only(0,0,0). The unique stable facet is support3; the unique unstable raw lexicographic vertex is95=(0,0,1); there are no saddle true edges. These are not renamed C626 objects.

The literal coordinate parent is **COORD_CAP_RL_C624_STRONG_G8=S8**, GENERATOR9599 bytes, SHA256 `bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2`. Its six journal capsule blocks were concatenated and decoded programmatically, with59100-character and170010-byte checksums matching the assignment. The method parent remains **figure-0364**, tagged SHA256 `ce3bc71c79e645777301fa6ac1adcb9a3e29cb148af68147797add570f1aa60d`; its30810-character source capsule was separately decoded and checked. The tagged wrapper digest is not being substituted for the checksums of the actual decoded sources. No mathematical source-definition conflict was found. S8 and the earlier C626 bodies have different node counts and contact groups. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

There are also **five fully exact C622 own121 variants and two fully exact C620 nonwinners** below. Every one completed both independent full audits, third filled-mass integration and final source-only replay. None is promoted as a Gömböc.

## 2. Arithmetic measured on final geometry

Each entry is the maximum reduced numerator/denominator bit length; H means primitive integer normal coefficients. The common denominator is for all final centred coordinates, not the initial control grid.

| Replay case | C / strict class | H | Raw vertex | Own centroid | Centred vertex | Common centred denominator |
|---|---|---:|---:|---:|---:|---:|
| Literal S8 |624 /110|216|440|44715|44720|44770|
| S8_D3 |624 /110|131|230|25674|25675|25747|
| S8_CORE4 |624 /110|155|239|22503|22506|22509|
| **S8_D2** |**624 /110**|**102**|**196**|**22720**|**22720**|**22745**|
| C622_SEED |622 /121|623|831|47954|47958|48009|
| C622_IMPROVED |622 /121|317|479|58580|58585|58588|
| C622_D2_G9 |622 /121|190|410|46326|46326|46370|
| C622_D2_G10 |622 /121|214|472|52033|52036|52100|
| C622_D2_ADAPT |622 /121|213|407|46090|46090|46155|
| STAR7 |620 /211|275|440|44779|44783|44833|
| STAR111 |620 /121|382|440|44808|44812|44863|

S8_D2 improves the common centred denominator49.196%, while S8_CORE4 saves another236 denominator bits but has larger H/raw fractions and a deeper chart. Neither input-denominator size nor solve depth alone is treated as the final arithmetic objective. The source parent's centroid-bit comparison used its exact finite filled-mass formulas; its already accepted full mechanical audit was not rerun merely out of distrust.

For **all three positive endpoints**, exact integer comparisons certify every selected true-adjacent primal and polar ascent cosine **strictly greater than3/5000000=6e-7**, and every off-incidence support gap **1-q_i·p_v>1/1250**. The176 positive primal arcs reach95 with maximum depth94; the136 positive polar arcs reach3 with depth75. These are endpoint bounds, **not a perturbation box, fabrication tolerance or continuous-path certificate**.

## 3. The new depth-two contact mechanism

The exact pre-approximation rechart preserves the full S8 geometry. S8 has179 mixed nodes,42 auxiliary contact groups and315 free coordinates. One auxiliary node represents an ordinary degree-three physical vertex and is redundant: removing that auxiliary variable and its three defining equations does **not** delete a physical vertex, support or true edge. Keeping exactly the41 nonsimple physical vertices as auxiliaries gives178 mixed nodes and still315 free coordinates.

In this reordered auxiliary numbering, the supports with more than three auxiliary neighbours are exactly

```text
26,54,76,78,79,90.
```

The earlier transferred chart used eight auxiliary dependences and depth3. A second exact chart chooses only four dependent auxiliary nodes **[145,158,161,173]**, allowing a point to depend on several core normals. The finite incidence-cover condition is that each core support loses exactly degree-minus-three auxiliary predecessors. This produces S8_CORE4's smaller common centred denominator.

The stronger reorientation is simpler:

```text
1. Make all six core support vectors free.
2. Solve each auxiliary point using its incident core supports.
3. Solve each remaining support using all its prescribed auxiliary points.
```

The fixed apex is not incident to a core support. Every other auxiliary point has at most three core neighbours, and every remaining support has at most three auxiliary neighbours. All selected minors are nonzero, verified rationally; dependent axes maximize the exact absolute minor, with lexicographic tie order. Thus the contact graph is solved in two layers, with every prescribed incidence equation appearing exactly once. The local triangular-solve argument gives a rational chart wherever these same minors remain nonzero. This does not assert global convexity or equilibrium preservation for arbitrary controls.

**All retained mixed points and all physical support vectors were checked exactly equal before any physical change.** The315-dimensional freedom is unchanged. The depth-two construction also applies to the moved C622 endpoint with179 nodes,42 groups and314 free coordinates, again with exact unchanged-geometry equality.

Only afterwards were independent coordinates approximated and their denominators compressed. Each positive proposal starts with per-node rational approximation tolerance1e-9 and then three denominator-first rounds, maximum tested denominator2000000, coordinate trust1e-5, requested cosine floor6e-7. The identity floors are fixed for the phase as max(requested,min(0.1*initial_exit,1e-5)); they do not decay when a witness changes. Every accepted change recomputes the contact geometry, actual filled volume and centroid, nonlinear exit values, root reserves, support gaps and tetrahedral determinants. The Jacobian includes dg=(dM-g*dV)/V.

Accepted row changes by round were155/49/22 for S8_D3,154/44/19 for S8_CORE4, and159/51/25 for S8_D2. The exact frozen endpoints, not the numerical search decisions, are authoritative.

### Compact exact recovery

For every independent coordinate of all three positive endpoints, the final integer numerator equals **round(D_i X_i,k)** from the corresponding **initial exact S8 rechart**, using ties-to-even rational rounding. The same identity holds for C622_D2_ADAPT relative to its exact depth-two preimage. This was checked coordinate by coordinate and then by complete reconstructed point equality.

Consequently the capsule need only store each complete per-node denominator vector, the literal parent and exact rechart code. No unlisted numerator correction is needed. This is a verified property of these finite endpoints, not a general rounding theorem. `factory57.py` reconstructs the positive GENERATOR files byte-for-byte without running optimization.

## 4. A genuinely reconstructed C622 contact stratum

`C622_SEED` starts from literal S8, not the coordinator's ephemeral numerical endpoint. Let

```text
p = intersection of supports101,102,121,
q120_new = q120 + ((1-q120·p)/(p·p))*p.
```

Only this support changes at the initial projection. Add the exact auxiliary owner **[101,102,120,121]** and identify old physical raw vertices162 and164 in every maximal cycle. Then rechart the new auxiliary as a free physical point and solve its incident supports downstream. The seed rechart is checked exactly equal to this projected geometry. Its actual maximal complex is **176/311/137**, not an assumed diagram count.

All pre-existing nonsimple groups remain, including

```text
[16,18,71,94]
[71,94,109,116,119,126]
[3,17,49,57,73,88,134,135,136].
```

The last is S8's degree-nine cap contact and must not be silently replaced by a C626 group's data.

The quotient inherits its outgoing route from **old larger-radius164**, whose old successor is166. The positive incoming161→162 is retained; incoming vertices are not wholesale reassigned. In the initial quotient construction labels the outgoing edge is162→165. After the controlled motion and final raw lexicographic reordering, the same owner-defined incoming/outgoing edges are **160→163** and **163→164**. Their owners are respectively

```text
[47,120,121] → [101,102,120,121] → [3,101,102].
```

For C622_SEED the exact census is S=[3], U=[95,162], H=[[162,165]]. For C622_IMPROVED, C622_D2_G9, C622_D2_G10 and C622_D2_ADAPT it is S=[3], U=[95,163], H=[[163,164]]. All five have weak-only000 and all137 supports active.

### Controlled finite improvement, still not cancellation

A full physical predictor/corrector reduced the unique bad outgoing cosine from about-0.04112030519 to-0.01540652852 while retaining the entire rooted quotient graph. Exact endpoint inequalities give

```text
seed:     -41120306/10^9 < cosine < -41120304/10^9
improved: -15406530/10^9 < cosine < -15406527/10^9.
```

These certify **more than5/8 reduction of this deficit**. The remaining deficit is substantial; this is not an almost-certified110 body. All other selected adjacent polar/primal exits are exactly positive, bounded below by2e-8 for C622_SEED, C622_IMPROVED, G10 and ADAPT; G9 uses1.8e-8. The inactive gap bound1/1250 survives. The directed quotient graph reaches the intended root combinatorially but has one negative arc, so it is not a positive ascent forest through the bad vertex.

The corrector does not merely backtrack along one linear prediction. It chooses an intermediate defect target and repeatedly repairs all nonlinear healthy constraints using updated full own-centroid derivatives. The physical displacement metric comes from the SVD of stacked Dq/2 and DP. The fixed inherited floors and geometry guards are retained. The first seven and subsequent six accepted steps came from longer runs interrupted externally; only those saved prefixes are claimed. Completed continuations had four more steps and, after another exactly equal core-first rechart, four final steps. No continuous no-birth path is asserted.

The improved full-grid generator's irrelevant dependent-coordinate slots were removed in the compact canonical representation. All reconstructed mixed points and the complete RAW/A/B record remain exactly identical. `C622_IMPROVED` now has canonical GENERATOR9064 bytes/SHA `d19f597ed2702e120f7261d90a7e001101d17a54f3d087af3420d08c10c486e2`; this is an encoding change, not another geometric result. The historical full-generator hashes remain in CONTROL_DATA/CHECKPOINT_HASHES.

The depth-two variants G9/G10 are exact ties-to-even freezes of this rechart at10^9 and10^10. ADAPT uses the complete per-node denominator vector. Their exact class remains121. The corresponding10^8 freeze was only numerically screened and gave(8,12,18); this is not a grid exclusion. The unfinished tolerance1e-10/1e-11 denominator scan produced no endpoint and is not counted as a failed exact body.

## 5. Two exact volume-neutral primal star coarsenings

These preserve a different, genuinely primal source of lower true C. A degree-three physical vertex v has two triangular facets and one nontriangular facet. Let a,b be its neighbours on that nontriangular facet and c its third neighbour. Move

```text
p_v(t)=p_v+t(p_b-p_a).
```

Every supporting inequality affected by this motion is linear in t. The full finite allowed interval is computed exactly from all fixed supports and both rotating triangular supports against every physical point, including positive support-height guards. The two bodies below use its specified endpoint, not a numerical contact-time estimate.

`STAR7`: move **old raw7** to the positive endpoint; old raw5 becomes non-extreme and old supports4/10 coalesce. Actual **V176/E310/F136, C620, own211/weak000**; output S=[3,5], U=[94], H=[[5,94]].

`STAR111`: move **old raw111** to the negative endpoint; old raw107 becomes non-extreme and old supports135/136 coalesce. Actual **176/310/136, C620, own121/weak000**; output S=[3], U=[95,107], H=[[107,113]]. The output vertex107 is not the deleted old physical107. This contact changes the degree-nine cap to degree eight; the changed stratum is explicit, not falsely claimed preserved.

For w=Vol(conv(p_c,p_a,p_v,p_b)), exact filled-mass identities are

```text
V_new=V_S8,
M_new-M_S8=(w/4)*t*(p_b-p_a).
```

An additional completed exact check matched **every audited vertex** to the proposed moved physical cloud minus exactly the declared lost vertex, tested every cloud point in every H halfspace, and matched the audited volume and first moments to these identities. Thus the bodies are the actual primal convex hulls, not just unrelated H systems of a convenient size. The complete checker appears after the main capsule.

## 6. Exhaustive checks, actual mass and reproduction status

All ten listed exact endpoints completed independent **A** and **B** reconstruction. A enumerates all feasible support triples; B independently clips every support-pair line. They use separately implemented maximal-facet/true-edge construction, filled-mass integration and equilibrium predicates, and neither imports the other's geometry or mechanics. Their entire normalized records agree, not just the equilibrium counts.

For each positive C624 endpoint this includes419220 triples or9316 lines,624 facet-side tests,31152 ordered vertex comparisons, and1248 primitives on312 actual edges. The true maximal facet histogram is

```text
{3:52,4:30,5:26,6:12,7:9,8:3,9:2,10:1,12:1,19:1}.
```

The vertex-degree histogram is

```text
{3:136,4:34,5:3,6:2,9:1,44:1}.
```

Every oriented maximal cycle matches the literal S8 owner-set correspondence. Weak-only faces, vertices and edges are all empty; face-side, maximum-vertex and edge primitive-zero counters are zero. H=0 is not inferred from Euler. The350 integration triangles have525 mesh edges, of which213 are drawing diagonals, not true edges.

The C622 cases each check1244 edge primitives and348 positive centred tetrahedra; the C620 stars each check1240 edge primitives and348 tetrahedra. Complete maximal cycles, owners, true edges and strict/weak sign arrays are in the deterministic A/B outputs. A third centred-integer tetrahedral integration separately proves all three first moments zero and the same volume. Tetrahedron strict446/weak000 and triangular prism strict446/weak123 are nonvacuous fixtures, both rejected as winners.

For every object, with outward raw fan triangles(a,b,c), all exact coordinates and filled moments are defined by the finite rational formulas

```text
D6 = sum det(a,b,c)
L  = sum det(a,b,c)*(a+b+c)
V  = D6/6
M  = L/24
g  = L/(4*D6)
final vertex = raw vertex - g.
```

The density is constant throughout the whole convex volume. The centre is never independently prescribed or estimated by averaging vertices. The full reduced fractions are emitted by both auditors; the literal input plus these executed finite formulas is their complete definition.

Display approximations:

```text
S8_D2:
 V=0.48895508965166073
 g=(-0.012533675515608649,0.006279834764387915,-0.008889116736363752)
S8_CORE4:
 V=0.48895505053659477
 g=(-0.012533612029362175,0.006279827901586373,-0.008889057860078934)
C622_IMPROVED:
 V=0.48860505794750514
 g=(-0.012623890453496826,0.006195839401176979,-0.008935122484425998)
```

### Executed source-only checks

The final26-source capsule was decoded into a previously absent directory. **All ten** case receipts completed from it, with terminal marker

```text
ATLAS57_SOURCE_ONLY_TWO_FULL_EXACT_AND_THIRD_MASS_PASS CASE DISPOSITION
```

DISPOSITION is WINNER only for S8_D3/S8_CORE4/S8_D2; the other seven are PRESERVED_NONWINNER. G9's combined call was interrupted after A/B/MASS and then FINISH actually completed separately. An over-broad case selector in the first packaging driver was rejected by the RAW hash gate before an incorrect ADAPT audit; the corrected final capsule was decoded fresh and all final receipts completed. These are completed executions, not replay-ready assertions.

The three positive numerical proposals were separately reproduced byte-for-byte from decoded source. FINAL4 reproduced the controlled C622 geometry exactly from its frozen prechart input, and ADAPT622 reproduced its generator exactly. A full cold PREFIX7→CORRECT4→CORRECT6 numerical trajectory was not rerun; the original saved-prefix evidence and complete restart code are retained without upgrading it to a witnessed full cold numerical run.

Selected canonical identities:

```text
S8_D2:
 GEN7437 d57c968a2bb594c8c9d8090cac30d3ca1c74698e0e95188df811d207fdfba086
 RAW6712 e5f262e920f555ea4bfaa165dddd31008db978071644b67fc112053c095eb1c0
 A=B135226 98be7f24dea6675f7c02c2121a44952d63a10ebe7668549d0704f6489f17254d
 RECEIPT1408 6cd84074ca1ac75c8bdd6bbb3dbacc33fb913e4acc419646013f58a32ff49b0f
S8_CORE4:
 GEN7483 76588079696c01489d15e7c84b725fe8302852a7acba7b4aa5efa506a2c9d517
 RAW6633 6c3c0623e145b2c351910ac82db9548a8917e9b7035fce948dc970f6f25b30c7
 A=B133847 c6c2d418dfa10c37bcc63233c7ac5cd7ea7b38f73483eb3ab3bf7a8c626a0964
 RECEIPT1411 ac47c13e15cc794d4c25d9b707753c9560bf8f720e5fca23c431186ad56b0da0
S8_D3:
 GEN7530 8a52fafc3eb06c096c8072458ff6fbe2c233551725b65b33d7088661fe686ad8
 RAW7213 1dd218d3fbb9e881f9b650af594546a059bf485b24abc1967ddaf5d1558dfa65
 A=B149586 40739c935674f4e08840f15edf18b72577758e7526ec599dc1d776cb147bc080
 RECEIPT1408 82e2de05a0e990858eb31e387f6674afb63afa1b1927d2143181a3de4d7983f0
C622_D2_ADAPT:
 GEN9568 e2800658dbb0d4e4cb87b1b3f040f3605572bff7aa24029a248353b2645a986a
 RAW12293 59b2ec18db02907fe6e95da468a8697517165d3c8aaeb5181a1d2212f619a19d
 A=B255248 3c31527bf827fe47d27523cf283da6ffd4b3455af39f294d17e7626ead4677bd
 RECEIPT1480 388a87a6183034e16c7bb7f40a17658d3d2c829bd96d766b6ac6576352973b26
```

EXPECTED.json contains the full byte counts, hashes, mass and fraction-cost receipts for all ten cases. MANIFEST.json binds the25 other source files before and after each replay.

## 7. Continuation and limits

For an own110 starting body use **S8_D2**. For the unresolved specific lower-C stratum, **C622_D2_ADAPT** supplies a fully exact own121 body, depth-two chart, preserved incoming edge and a single quantified bad outgoing edge. The useful new freedom is to construct the six core normals first, not merely lower the old control grid. A further proposed contact must be followed by an actual maximal-complex rebuild; dropping a redundant auxiliary variable does not reduce true C.

The C622 residual remains about0.0154 while healthy floors are around10^-8. Keeping one bad pair is not evidence of a small remaining geometric change. A different finite cavity or incidence transition may be needed; these local methods do not exclude one. No unrestricted-geometry impossibility, denominator optimum, global C minimum or continuous no-birth path is asserted. C<32 was not searched. Nine/nine original-proof verification remains pending, not an assumption proved here.

## 8. Complete literal recovery

The capsule contains the literal S8 parent, all contact groups/orders/axes, full per-node denominator vectors, complete frozen314-coordinate inputs, both independent auditors, third mass, exact geometry-equality code, fixed-forest predictor/corrector and positive reproposal methods. No prior ZIP, external helper, scheduler or hidden checkpoint is needed.

**41775** whitespace-free base85 characters, SHA256

```text
9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d
```

Decode to **112244 bytes**,26-source JSON map, SHA256

```text
75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360
```

Save the capsule as CAPSULE.txt and the following as RESTORE.py:

```python
import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text(encoding='ascii').split())
assert len(s)==41775
assert hashlib.sha256(s.encode()).hexdigest()=='9372158b106c03f1804a225bf3636814fe72535cdf690bfdd24ba1cf2d61eb9d'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==112244
assert hashlib.sha256(b).hexdigest()=='75670b87e53f119fa26c5127589e0dfb63d5a4ac986cdb755de7e67d5b5d9360'
files=json.loads(b);assert len(files)==26
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in files.items():
    rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
    p=out/rel;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
for name,w in json.loads((out/'MANIFEST.json').read_bytes()).items():
    data=(out/name).read_bytes()
    assert len(data)==w['bytes'] and hashlib.sha256(data).hexdigest()==w['sha256']
print('ATLAS57_26_EXACT_SOURCES_RESTORED')
```

Exact verification uses only the standard library, tested **CPython3.13.5/Linux**. Assertions must remain enabled; do not use-O. Source and per-case output directories must initially be absent:

```sh
python -B -S RESTORE.py CAPSULE.txt exact-source
for case in S8_D2 S8_CORE4 S8_D3 C622_SEED C622_IMPROVED C622_D2_G9 C622_D2_G10 C622_D2_ADAPT STAR7 STAR111; do
  python -B -S exact-source/verify57.py --object "$case" --out "proofs/final_$case"
done
```

The stages A,B,MASS,FINISH can instead be run separately in that order on the same case directory, with--stage. The complete output includes RAW, full A/B, exact moment fractions, actual centroid, maximal cycles/edges, detailed signs, third mass, equality proofs and final receipt.

Numerical discovery/reproposal uses **NumPy2.3.5/SciPy1.17.0**, one BLAS thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B exact-source/REPROPOSE57.py --stage S8_D2 --out proposals
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B exact-source/REPROPOSE57.py --stage S8_CORE4 --out proposals
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B exact-source/REPROPOSE57.py --stage S8_D3 --out proposals
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B exact-source/REPROPOSE57.py --stage FINAL4 --out proposals
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B exact-source/REPROPOSE57.py --stage ADAPT622 --out proposals
```

These named stages actually completed in the final decoded environment. Optional PREFIX7,CORRECT4,CORRECT6 reproduce the earlier saved prefixes in order; ROUND622 reconstructs the three stated scalar freezes. Platform-dependent numerical deviation is rejected rather than treated as a new certificate. None of these numerical programs is needed to define the frozen exact endpoints.

Convenience artifacts supplement, rather than replace, the inline source: [source-only ZIP](sandbox:/mnt/data/ATLAS57_S8_CONTACT_SOURCE_ONLY.zip),47884 bytes/SHA `ecd543bfbbd4e69301812746435c1462fb42d18febeeaa9cc7ed0b4dbf175ab8`; [full proofs and research archive](sandbox:/mnt/data/ATLAS57_S8_CONTACT_VERIFIED_FULL.zip),6008352 bytes/SHA `f7bb0f92d9cd846445e42bbaf09b84ebd0cfd1140c9598f4d3174dde53d2d013`. The research subtree contains explicitly nonpromoted numerical screens and interrupted histories. Both ZIPs were read back and checked. The complete [Markdown handoff](sandbox:/mnt/data/ATLAS57_S8_CONTACT_RESULT.md) and [v2 JSON handoff](sandbox:/mnt/data/ATLAS57_S8_CONTACT_RESULT_v2.json) are additional copies of the literal result.

### Main26-source capsule

```text
{Wp48S^xk9=GL@E0stWa761SMbT8$j;kI*vOI-jxh=gNdqHg-_y_<nFIgE5tg437+$E;aw9Z)AFYu~#0-T-SIfzMgGAK7Lr0AV_t3ct)FANdsA`=-mzD16k{
>qu=!>AmHa9K<;?Bb}#NSSo2!xi%l-g@_Trlf}^v_dS$iLV!zpDHiIwmwD+QvO~@u`^zkY9C^Uqoo47UbjLzvP#x-0Vag!DuLDCG4QX(oXiXeJI;s7~1e*|L
XwTMtAVw7F5RuhY@00`|FvDuU-49G@x^Yl<Y1Du&gbdrdqt@L?soTsme`DIhFTMel!uU1PC>5lZiixkq6X+K5QC;9OYi!apg&ua@xAV-wIF=)8%ZB;FF)sLd
G+or}*5;6`iPBDL8`qRghj2sBM}NMXuc3ib{9!>`3jgJ$kd)lH;+~tYdk^t_hbp>(eq-I*B6ks=Fe9Squmv@bRH~NVEL-z!f*1IW8kXJ#UvZLEQ(%zd+2D+t
vk8&ohyR@&<!7HE+?ot(lN#f6hI1s+UsSB>+99)DcneJY-Aqf1cJa@Vbqt=<|FPvd$><{@0e!2#iR!`#_v5zH226W~AgnJUU9V${h9)qEV7d<RJyfh0k;~+b
w4rBDB=#riu0eKa#Ne^8ZRu{leRTvvhl}Blu(b|^MIoZTAhYdg|At9mrrUpuXu^>;90pB2<FP>h7!;v)+xheKsNU2GZMGATZF=aC8>4OIF23TF96m8MnGmKe
KYfP{T)O{x`Nx!m>X$Ty)O-KTCRY5_@2l@am8$0;WH`r06sab-XHrE}adi;%MI$b=iviGbu5hF>oPL*gAZwlKNZ0M+A5=dbvRrTdh^s*5TP&GH>|vipJCq7N
B>z^V1F%X?#*`$!OC5%~Zgj%1NH$va!g2zT_#Y0|D+^l4ve%G&FgK>LDX_>siOZiX^+;ae?$xSMOzg1&d5xWo*7$}Aub*31+{8I0C64d2#|*?cT$4k_+>*5A
?&;lfFSYLZ6Xez7T5{t<k>NfG3hULHx$k4QaWbP0_v13dKWjl4KCqg({e20jFd5w2FvE`SUSx7X_{~4t@d$eNs_20GFQBx7ZRi!pwiN-iqCzw7>?AriEH*q7
^~^&+aQn0#U7;%_x@g#mfceJ2di`OG9Hny={N`xF-$S^i63AC8HKT(_w-%>K!!Hr@6&`=Fp#-Gc(VF&7S=~~l$RfC_8_5zjt9nJ&p-A{dqOnng_GNAPo>>f8
K9vP!8+TE`O_m?a15GE`y#ztz+K^KiZ6$g*FC>SgWcYfGWRBC>tz(>*aIG|ha42Q%Z=gYGfXw(lGhd8lH%C=QtsUrjFDp|}A2ZZRldX=LRMMq?ZQJp;IdvN5
OCX9x8i?p{w2Y858)*YGg|}AuD6dO~8ew`WPw+;9O04yY27WoLr#)2^ssDtn$}#T8H5}jfP@TMg9V)fmq{tpR^@X^YP<H3oQ|;j#R@N0QRC|hvm;Ski49Nd8
nB}yRLWFpEwF-u=fv4T4Qv?At&O@y<eXoQ2cRL~K6X^Vr6CR%C)vD4tr@T?lP=;lxSM`eh&D=`6&*T#yfaau1czpVvx>xR%tnA*ZRkBOE2$-t1C!n)XeXT4+
2#~-gWxClcz;^fDqLrH}6$mqgv$mcGtN(A}2c*mUdx*7;P~8^d=*roY54YK*gr(Sm*~QoMoLD3hM21Y!8?}$!JBHc;uATKl@Df>8_2iU856M8Do?2JlbA(Dw
Ub>irtbCF4ETc#IxXSNCa`{XihlI+OZL97q&pBlqchZB`#Ec-14y-IQ5KKQCR#AXt-@^0-pHpn^Pc6jT^M;Kqtxqe;o3|3P3|kewAjbCCW)ePqwdQSLy@u@X
;fi$>S#O;4>Pru~Ywfn=ZVi+ffw;t7hA*0DGVCg61TqDn&uId4LbDLRNW66aOrv6HuRla%W-Cf}tkaxFg!2c(p6j}}EOXZhwj!UFeU~{AIhIE5ENW8#?g2>a
e8f&WSP^=%UuYC9Z{DXje{4Xwkzc6ea6r>y-DWBlrrU2~G~gb%Ow3V3OS$@%lTHl0UZv=3%>f|=5Y#qVoE#0Y){<SpUeSwU^?gITYUV-y_0gP~v2Vv<I@)PV
hAfq6VG65AtEeT#XK_mm(7b~eCa~`IDhLar#Q`Fasg8h#>ALa~THFX2wQBH|<a<PGN(M-YV5nqP`XGW_;J%a(Fp?Pf1u5J!WLHKIf;&#--W5{mpoR4^8;tv2
kW!r&ijeY4sCejG8qT4opz-fBaSY^-k;g|Z5*W`WMRrx#kMj93dCdk3Iv(lygFe@X-r1gRt_`C*`8V&!q5q3g*93nnGAvYkkf>`;dhiv6j{&qZMs1lE116hj
&E73si`T~{^Ys)vC)B>;S5Ozto#O{Y392S#&8)ng7*V{r!y*q|@ycf$8mgAY<nXo0U;1iuF2J|@5p!Of23B@Fb;r6RP@kD`TfoLaFzVRnSs|)w#P4MDX?qS9
H9!mtC3vaBDWqQ3>p^D&kd7GvWu9wuE551xziL3j5>c_r^Is~#m_Fh|QZoA~+fwEsSn3vm2+3kCiLYGBVw_651tF>2tv;8ac?w!mo}q(YyU*=J4&u&>Dy8tf
$Scune!_9wiuy+;vmqY&hkO)qexWerM`)N8>Ly>~#{)`qF0X`bbNz8%h_--JiJ?~d3=E7q$ICKXVx)qu;aBNY!vcfNYIY$9(1%aYAsVX!>v#+_w_a?ZGR6Y?
JKONYX~5jpm}6|vOh1h^y{-sRE6qXFZjEgaP|KwU$xCY<>8Spyj3$)ngU?R5VhxvwB<@zS*G0=k4R#O&=mj1$>8)c*?_mA|KO!p?9;msWMI5hm14XPpyMze*
8|6@W5-mq6n)^MT$Bj^76k6N#^qJP@W?vmkCC$)4!BT(s38JprfV7_&b+@tTrBUf$5{39Ody1gbK>sJC*e&MN=QL|@h_0fKq<$ah&@AbI>wJ&78M|SFm6V!!
|DpJj?L5qw(uw3z5JYbOXB&%y8E=I-ZppJ-dw8}~5F_kq=~Y7r7Q>1!aqaUoveg4uR94gQa%VHN%nu~Bf#4cM(hFG}K%gbv-)VdbDe7Pyo;!UJEC};iaJffN
whY7{Ne}gWQni+d(M4Uhja_+*z(Ym4ws$S<C-6L`Z}V)BY`GQ<=-a#>1!!{(q8cO!dfBQR0(ZiWSUx2crp(pefS`YKsVe8mYH^{hO6?sN7nt@&FFM$70`+Gi
3{PQ$JYey^y}0mNN~IS~eh89wRq?ifV_q)wmgoV%6l8{MMoYO=hWtlNP?a{&NdRfu-k!2Oob}A7VcJ~Uo@hbz51$VJc<IihY;`Yc!!i0m=*DH5W<PTl&NzWS
1|tSJUdF^W*P!N*Ug3E2+n_tw`&srPObho`!CPTL8b+mJnH^ug=jfa(7;)jy$Ny_&=T8dR()tvcjIvo7b_%7Ft||U#u!*&Mfezc|m1;znZOxPOBqZQ5Vy0`1
*!-bRuz>92^JHYTwEPjkJ*Zvg^pDG>D$+`Re&tjn-Fq0!repTCDU-F{dROhM3;-Nk2kOHxe!nE0sJfZMCnXAw=IHHscY;PZeg6raB^7AkiM3&$y`Hz1Yg6H^
Wp}9cVA12E#8?NEl{|l08?@GtKclF-7gF|x0@waE8Z|6}K2+RP2aY7L^RjZf=;7~*D?NUBJDAU1z6uW%a`BxN&Q|QKn8-+XB_*=VJZtZ`Od-qFZ*+KwvP?o8
+AsbEVTU`ZMXytABNpBsC6y=mgPUPqKWFF#qw+h>oTjGYYA0KK3}$*3<+T-mKOK(ASDD+B+WxjTd6QB9uBGN_VxZPH)tJ489Hv)t`IGA@n|%>_hEAW@bX^z{
cJTfd0hkVU;+Cyd9Y47{W=nc?`_YFJiOfkVPOSujYxD<`rlfd_ljFS{-*|=&;B;1*7!PEqZKd_Y%7(JA4Jb#+1e5K+#BrfrAX$c!nKAE23iaZ~+y>520Pemh
<#|mk&zh?u@nx@j77Nw$7F0}QZc$V%E$Y(y8HuhvaF-D-*Sd+bbh1>i0x@ufRd<uUyoW7ymG<_=%fC$<RM3hW1`wh@dSXaUI$tkh_4~`3aXBh7kB28w{d}BG
SXhA>XvcP1%^w+&)j4%y^h%RPlZwhwf==f|B~PZ)9b0s!`d@J6jcbI|(;8ipfnf#}c=qtyv(1^0k-R4za!1ZU@zC=0Ez{wR3kFT(yvz}O)+80XTEP&T{>v5w
;=O6$9OC`+v%tB00~K3FXD@T`rODA&<EyQ4Z%If;kQqmN$znL2iHW{aR?P&vfnp;I%Qxg<IKj`|!owhy{Jtnv{XF7_y6l;tmSmu@mxCsBzuoMpDQ055D~$Ez
szAj&=PpI>#HDlh!$f<OB}JiT|Czlo3iX~&a{F2w3gc6T2s8+*oWqd{Z!mJ_#8lGD;L}T0B~pFw3i5m??w5)z;qRlJL<i4LY3sXgYF}zWAsK{^zmfn^XCoFq
1)0aC#Ns=L?|@H4usI{^V(OI?QF2&=Cb|mKIt(F!VAwB-)N`Oj|A7j|KFDSLYvUu~-YNZ>qp`TFsnx;3+7z0`{QIQ657G2DK1d0%iyuFr<SQ3KBf@OyXe{^m
;QHqI=VjSPwroR#$_67%kx;*`>VL~u2ab8)d6XzS3OmE7NzwG@{n_`+faUf>rm9@BW_sX+l|OI&n<zv`;Lqv8`h&^F-9X{kjQmtZ@*bLo4a2)Nc%WmZVaL_U
<)l6{q%8-vxEW-4ap6d_6_^QRqWNa%)Gy8HEA`r{P9FJL`hsuh<qmH&^q0r$bmcBq5ct3_sal#FyKl%SeYd6nw9$oo@KFB9<kU6=<`h?|vuK)%1`=NeSW6+I
E5~9*h~B?P&pmCMbSZ;$aRNEw14YfUObL@aZs|{Ml{rg2VHH`^1=FAXs_e<8<Taic!yGh!o61=v(}DnCN#gK~>?IIbAON&P8U99WDbV(a1jlBlfX&E_ixx56
1DXI)@-?gALG3urWGkuT{8(I#MEv)|5E4ghD0$)yDEu@^ao%jq#EG=ZzYsyLrk9ENsgXUC{`QilB(1u+@U^|Io3PRt%RyX8Q2%Mk$KUVb7z5JTx#&=yREu74
7)g<UDW=28=~~bG#iO@^C_9))m&PVapw3kJx@aaTeHU0C=Q%zBoF!YcBGRVel*aHj<6gL>bV~1EPy9${_B{PzDI?%%FkT>($X6ETrAQm0-K_?)plwJ>u4mS+
%bMHjS(=t)zW1r#40oXbJvc2RJ%gfF{X*~&Z%LqjprV?kDpmudyk;}R>u)Hc!NnN81F!6mGZe~<+mxh^Y%`=%8}!(@vU5(Z7Gl0f!WM(}fi;GHok;LSPf+RY
=DDO33IIk??{B@p<A8Y%QLmIiK!!bRm;{K8wX@;ezxZlr3d(q@e40V~KwIRQEgZKQ0AJZxV$5JjO;iJQ1W^R=05HJsxv)|z5kk$~9N*?K1R-tEP1EF!$N+F+
I5$=mdr$iQQKY(c0Icth1lTSh&qvsI5^Zjh?_Ir`FKpNYfHSBX8XJ!_)t#h#cm`ntckPwbJnR`vnQDg?1|i{O@Y)QdyE-gq&mcLPC!4FWJ(Z?|68^FiZ+GO6
p|dzS4PUMSG@rnlI2w~X)Rb-WynWi*YF&Rb=-@;<1&L=Q3rZ507~YX9`L)R&&y3mS8|UNB%R)hAAREeWQaJ=q<?bJ0Uqko=ZxW!oB5AG_Byh!CYf?!i7Rj(8
LWAI<Zk&@9OsxyFiMR@up*xlq*^lD8;sa;d#`?p8wh%V#)2qq?mZ2iHsz3|^tGwIq-u7`<670)vdlcBX;M53g-CLfL(4ehd_i-^DF3z13i-+%H1>%Q#P5JE`
Wnd?dqn2g~0+7@#o%NS@Ctc-fR3&;75H%PD-^K2!PDbVEXVrnQnHD?MqWmTzgdH9upMC>LE{na+__Y-aql+Jfo>+y+V-?90PrenOwH-r{FUwuo_#2cI;skMf
t@RrUOP~||a1?6xH3>K<LOT617mYk=LBEz`hv3MnXotJXq!yo6$1OWbqHAyx-<~|-hA8S^pchc}72IrdA1utB9no3j*HCaNNW?a7-6zU;@pL|v729|TFRomW
xV)@-B6j|)VU9%c@02|tym}$K#KrHmnrkaoifa-UogdDjD&Jcz)?|2kY}^bzpx4ptJU7g!$;(uV4BNv(4Rb8Up~5t*yoV8ZwoZiI-=iDSaL)v5P2Pwtvz46P
Q?4z1vS-I{(7)wBrk&n{_s;No$UC0AmB0~Ff%IL)8D>dR*0rjr8uA1eLvc|@)qo*=AtKW$ILP24_v8Eu&6M<-GzOQbt#`Q91P9y+7)hi3^gGIXqMH)XA9!a+
8-7^Z3C-T>(H&t2S<d?BNmj!3=e54W2k0O~ybd6m`$Dv(7ZLn_&dI9Ilpmdlc)fQV3_b)2ix&n7Jy8#v<H{<)E2$3jSGF6DHx`kmmyOa8_bz9V^&-^do{$d`
jPVNQK>lVY;js}nXd8XV%%QZBmQ7<!Zh23D@zmX0&VS8-V%@I9atQZ5bd(Q<A%K$iE-Ydoyy74T9TtPT@u&y)EFnY%GCxv9eKKRrw463`bn;kB+=dX6mn-3X
#6Rvh%@!ehL8$BPqI8J{lQAFpFQBibTH{JU7^RX`WWb5y^g!z-RmF>w;N5w&FdE#)8w~3!^SN~$FDc#Dq7)URaNMt1rD+ro!w9+0dAZTbTUz8&o!6|!+(Cj5
c2}nR_yNE8pZYnycu-ymW2006lRoSh?vETso(*0>y+%&LV&RX#s`_h=@apNp36b*{nHllW&58;}B%u%yoT1ljXyPvlbx(Qc85A7?p&1P6l-Zy~zqXi?<-(#5
*Hn8y=~aM&1VLRxIxD_1r-Q6EZNVbq6squ}6h&*x7m2N6IO-hKf_N?=cWvp+`%8BTkXb|Rt;ABf%Jw3X&F!KAiqa^X&%=D^f=uoAV%2`Q5@z-9oiFySe^j5a
!z@HAPZDsIp=QC|I9nyKFAjL(Jw8toSz6Pe3Di45?uIN#9eM|s54zCdH(~rwba*p!i@YSI6ee@~EE$i$n@6i3IDbGRc>7nh-Q!(NuiQBdhZ(pkwii2d-(-lo
5k5Z;s}R=MNzr!99{*1k26Wj|rqrb=q;yxSxeL#<<^|I({U&4eC}D!k`z8w&N6N|9XDf;k)qacu>a<a~g;J?%?;YN~9${$L=xZ4u)qwcdE#hyK_iX2;e|m8O
yc!nDgrGD6f_2!{I30Pgm3PvElg#UFc+cx8e-zl8HQvP?qogZT-aYq?-r;JdmIurYT}itZ0L$=Yv;)~KIA^F)VCYji0n6I{=QoATq5^-pWe7ffzd(|{V4(xp
{&51^V&OhAa!y$GNde3BL_><reN-@h`g^fj|0=eD+Ke$OQLe|f*+%wKDS6zN_pmG3!n)!WhVfr|k6|tP!Afmye3)A=`$`m@Gnt~)?AJr+Y;{btYApkI;EDG<
gSCPPYP>WnD>)#bXgB`1>j7TM`H{s?_lGysp<RDlexSh4+f?AcF$n3!=gZNB58=Jx?rRR(mAJ8%llF&8RwZP~G|wm2lGtd4VQtMyHwr^7Spb!t`mGyX_8m0f
s}7)!p&?VKFi;peIlM|kZikABxxu@#I%AKyKb^iSk~KHY(8ZLcrpt2_mE|N_5|XTE5dc{L)>YTAQf>Gs#~2!x>6{kY%awNJjo?~HtHW;8GU|P!jF`#UJ;cX!
tt;+F5d|x|ywjzHo^HqJI>bew-~ZSzic-%Hq8RtPw4EeVblZkVvC?NhKD}EDMDZSj7)x48Va%Ivt_!HPGc-VewC^NDY&5*ykS(J_!1p#>$r`*OJ163uGVmxw
02p(U%g*yK7Oc5WYid^IDkZ|cA@023@&AIA{+1;2r<}2`@!gwbzkoZh&rIWxjJI`c4COQJvmW`ey5q00?%rF-4P<1&U&dp663$rvAEPy)7!dz^hm)?9@IJQU
Mz>7M`5g#jMiIarC+O*a_|}TASPJWyLv{r1_w<c=S$@AvS#d6mLce-k=i7`%E4zr=AB_}~JcfO9W5+XZUC_C84TcT5srTN5*NW69N8{uGov?shQq`#2bffmb
-#~dNUSw0WyJLm9vgzDxMI@{eg>rh8e*W4kCPgx~lGnla10wJqCDH^G)-E_*dKRpNZ|O$rGkQ;l&T%^uq*J~EX*kVO3$_W1e}>wJ{;qA{0karC4kfiYu{L~m
AH<0poZq8xVcqzIjB=}0>8lXaRIwe5*!#BlpAEsIvQ#HOPUbD~JZ8B}T`mXrm^VD&@{c?1g@RYYrPnz4ThWG%4psD9cXnF{b1Nc}l~DWMcEY7nCYPXwjmHaD
;Vw{wf^rOU*u$ou6yJYdES@9)42ejRe>jvtEQDnn>%Gh#u|%VQ<tqC%mn<G-7KZ&p61(fhIHe!6Ti7C&b@F+3M=P_b<Az3aU*4*`NQmHZh!;8BK;BLye{_^-
WyzORjQ+{m^>#Yzyfxs%FJHHo7<NMkuz8Ie8NHv6lylZl0);;}QM-~Vk|6)#LiWuY`N)XaIiCHzbDEo`aEGMZOsf_->c{_ub7hkCziyzds9WRQHR)33v9}Gg
a!^+B!l<hqaT_S1Cj1`F;}0{LtptH0R}&0XCB-s4d5{@swl%-@M!C_LVIKx{2yZM2M7X5C*VMSap7W>_oNY(Y(Xa`dkt8yk64*8%%+sN?6j*Et8r;1&&YmN5
BXu%=tQrJ^rur`(G(L8}o^H<2kStJBOZM8vsCXkLV71MPaX83KH5UTzSOVGB<Zs(?%wBUw+GzW1%ttUPC?j)Nv<ZZ*r!_WqS{L_#XY-p01X;N%l>bIpfA>sm
Ci{=weTG4@$H+bWJKRj!+~>3MEoy*e^fUjsTpw<bN`G(KAflIsM8`%rfFhv<ygKO8W5IFqxA^&Uug}7Q<Pgp&=;!@m6KWYR?IFiTgn<e790|@kb$<8kLlBe_
8w|mN=pfTXskT_J5uX}eq-|rQAR%g+`xSHX(O~ThEVvItswc|ho7g0R_*3Qvtb?&Qvvn_1z%sCagiBv^T^uF3J;(YHfTd@XUn&(CEyJlK_Pg51{aA7^w88NS
l;o%Ui+q*kJ;I)e$x<pAdRlwf!7&RPJC-?|%~45@nYm?Iy2u?#a(=L&4BgfpZN(gK119>C*HKSEPNI;jf(YUNKUDsgCm0_w1&=3_i7C#WOkg_+WAg<3a=HRL
6Mx8H+eA&3;a%*EJ~4s!@Nx02=jEP?exSur?IK|n{ufx-Jk|XSbD;$?d|NcbGoU!xnVGzjk05I8#Z;kC!!Pf4Z{>ly6uIl<z?&FP>T>8NL7N7vgY7ObcUa-Z
dD<c6N-ah47RqYCigc{*coRKCa8lF=MZk|<7U*)J=8^~+=1=Km?hfsV<9L!zc?prSMcy6_TQZYo+2lDWdGD4l29mT;HDi&$IVg!h?Xt{?AsN5Lfke+Ww@@&j
Cl}&;0@#?t=IsmnlX$pJ6&hp{+POf`-$%F{H}{gmL6XB6#+nN|(~TV$myNz%R^_xIs(xw3mdywut^D~3{2n&Qu5AU@7(~u>(&UQ>Uu;6keGn4&m-7w0&*VXl
&pQCNZdj@fSv;ICVm}b0eN}1KH8bKQbvynIZS?=*ym6||t1-JpvWWbb5a~V!$F(W=XF*Un_XtVrl=h?r;N9Hg;m&Okb&RL*>h5~`Mu;=*I-I)I9~%z$`$<K#
@=>T?#l77m(JuO`Dmxhh@NIjotL@x@ry*gDx>8!5441U#xe+i*`jF`Kg)&e29V`^0->)X{&7Ja8ok4g=7@c|bt+H&G^o{@+gOn7}&*60&*bjyN!0)fzM8eCC
oi?ZVXBv9+r3VijS2`N5wL}>Ng`UG=vGPHUI+>B**h4S%^$sYu`_cUz=$kXy6w|AP1VOh+54j3f9?HBDco7V&yz_tpDr$sx9-9DCxBWfLn!^!gZ-hPRh51c2
n$qWn->P(cqkBOfRUwor+g!6l=OYqaTM!w>Iv6=^K841bGZY-6bUr81gfs;&S_5Jn5g<TLDwI9#wcKPqf>)V>(Bv-aZeZh&-m3g;apC?^f^W>*3Vv{G$A?Eh
u7ZQ&0Org@w6cfNDm2b4u+08_4Nb)f7Ao5`khwc8^?>@CNtyj{_`!f)dMNHptgdGpK2v$?V3ZeH*~Xh3bH|M`-O<CY>`}~^2~bH<fV0=8FCA0}HsAxNCiqEH
M`k*d4aLBycvI&f<SQvAgSLG;uCwKUVc1B-vpn^mY?={=oRA>W(;MbWpM;AqXn)cB8LY&DFW_r4*w80JRLmfQl2J?H6t&Hn0w)9w9nBilK{B=GbgI7%`TEjF
hAk>cvgh#<1wtS}vf-k~j{N04aNj_5ue1N;$xb(sc3EHGdtBXYgwG2p@=(Z2;jMJkF4-WJ+MZ*~^FYK>bAgVX_9kc~GsIb;&~ao{TyNCTD8?1-L*fCQk_$-`
4fXRTJhTZv#@sl-9ARvi7LVB=Le0u;c_f|{3I+q0DNbsK>neqsOijsY`-_^C+$0!RXmanE$oQ09kK!~L<pqlTo7fsW2pnQusO@hH(BE;C6Bcc?h>C%;X;%9a
?ld+LUzums2@%RCDQQdaWLJ_UO?Y<Th*DmYiImEB+&B-lzu0sS_XKr^LbaKjI>BW>YV)2nBS#bQxoS>n6-s_FgOJW$mjGJ_$aGMJ2gY__wX24hf1q3a+_ZjL
8RBlzkBD`(o78_}?<xCx#(sl7nQG_qNdyJyGb{h6hSOw(jJ_GjqMOM*_kY<|iRlyqD;_=K{Z}0e&sy(HkMez|))B+!YOraSP6b-*qvoA!Q&ywTI+~`nK}4VL
J_LxvPl{L)Ydc9$dVe+$Wg{nM<c6++IWw<uFYHa*lG3B0$46{<5+x<yh{=IaIRB^~<3gAGj~ZwXZdq6Khq;hiNQ=JUeHMk>BMG!+riMa#{{D5TnU*SrUD0{W
ClUyez(t<NnB~4ezNdlUL$(Il(3kcf(OR{KmWgPCuPb=siEwzbwZN)9XzKz?eYzd%=O8RqsOQnSXX%m~AUp%M!N0Y<{DDr-txlt1PZSRZH?&nsH*Ia@j>1ni
F&%B=9j0#xHXYi%C1r$X=00Eup17P&MI#Pj270X+GPHEPswL2tc~rP>1`QS5$kN?K*!Q{SvffH7yJo~D@B;Q6pE|PTR*XnXAOJeE95f<B?uIC!hn~@}Zoo^T
7eoYINH~|(K4?Tr36Jg}yNTU$_pV5#x;({sxPgd7GapU6l2~d1V0@1e!&5EHbMUb}PgEP0DV6js;$swy%h&x#9bJI=kdXo=L(;h?!Jc}6FTW7qwBrGzijAfS
RdUPgO+_!XX+&vct~3PQqsS9au<MvU&wOBo7eggJo^x1shy9a&hkGEJ$;d3ES8b2ir=ZS<S(6{&PtB>_ZwT|!BCRRy41i8g4vzyYWnB-k9g7Zf1HtRHUP_2p
oXOk&0I}S;l&!yUI18{$Y_m~+9Cv(fHN^W&mntLr?o|Ed%G5!6ePXBZUXke#^TJkZaVi{Y<qd<k`%3poOt=MNyg~wTsWgXGos2d_dHjWpEXBhNJuo|<R~PCb
8RI=kgokQFP2{ed{*-?==P@orxk4BJvQrjKpg)lSNsKkp%HGMaZy)IXc?Up;mb);^Mf~EQLFWmR7k`>X=%>P0oOzO=Qb%mxtcj>q$~RNT%$sKmLBZk6l=GL%
Lp%OpmF}L<5ji?a^`~2SAPFvGB=j;@r&!)Tx|%96Lw%SWJES;F+f6^6dLusts9>RIHy~xw;8Wk)(w0Iq&1ZtK5UJ2HKY*Y4S{*wzkoHLk8&Qzb^T%#x5}|H{
lz?tHvVKw%F^miKv-P+<1omQO$B5yvkRr6(1!22nPXCV#SW=+@{;o$YBFtgCx479izW|L=9{wXf@Q(DqnJFS{QXf{mczTzdVpyV*0sGwqS?J1QrhUK1z<V-R
db8;z^Kq2;$g)BfQj4BBaoT^+k)&%yL5%?&_vXne<NDi$>3izasLcBQ!=^4sd)gJ2zoqbEVk?XhTUq#zK|9|%clil3!l}+z(Z5)=VFSre&-vJidmhA!>#@7)
<0wDkh?G8T1iU=*?30n2PFA5}qKFMW0XzWIh$?&lVGT!R3ZA%0@Gcu`N<azIKJa#|ZFD)QkrB9Qv%#axvrvwVJbv`PVBXtkm%8Ddr=y@&WFKjBG>Tc?#YAma
2DRC-Eo*a*wk!ivjnF51KB3B8-)86fHsz2_IIV#czCzKN^tMcXjhe9SNv0|v+QQvcj83}RRe|fNE7&mqWn-7!gOWt|EoQEjSrcpS7|Lb7BVguZX!mJ7eXiy?
Lz9{*W~4Ne<R0ec<+>Zb6XCLMAQM>5Iv5Dv{ZcrA2A*Q*8xjR=aE^}HYKR-zEm(5865wGN7Tj{9;>|6Tubm9?<pp0$w&%USsCa@uM8m%7M`BqGFl-5V_I@#K
*9M>gs;f}@X{K>K0ghN>x{1*eHu@OMh>t}0FQ>GU@us(9K1;*Uv`|2;z%}y0P|yE0YzGp1w?1HAExJAU@pvixkB0Ogm<wPyqmeSA=~BvOrBZ0wfAYCEOXv`2
%fwP|2r1Ly9%cvBXEZn`z1LpNI`YK8mTmUOfPXPWOJzdX^p$?nt>g9#2K+?MIZveQN3|JSjH_3+Sj3OsW{jmGbP0cZSkCLIZ>v(yWR+xGcTB%f2cE(hCS;qr
E4FESgz--y9)Wd(5{y#3W}5hc4F!yI;*K&0Vg*3oaLTUc<lMZ{rB-s|n~8?*$3T#aL~J&t>3c}K%Ylv;0}0N_)4U=M!g=h~<sKZmZc%jX<Acse>8SP~VxRiR
!+3P0FTTd1n|k)zX*W3pu_WC<RdAzkURqjoO&e)|VS?1x;uhA+M_BsAZx0Mm9U;&ot0~hGx#}|?7DQTk2-<>x`KB)xtJ|y)1u5fvQ^05!O+a_eTiYjl`hd|p
_nKkVu+LAvzV%<}20dz4z6ox>8aZ<1Q+#kv?zm18BZjNSaN<OCgu2yBlFu(-_qmha$;dcWvWU)6w|eo=$qpl!fT3$o>HgI|B$Bk9Acqw-!dlqK1U3!W$%kpy
W$$7jW%%IJ1G7+nwSAJEYPmz$L&JVAlx9B<7M9zE!-LO=4*Xu*{bY8PS!&d;BSExE;KaNB;fDc0vEb)zRPqOu|C6mK6^;ZdB*ahGN?>yIbVCwD=c$4vvEO%8
4=~$8O?qp{d2vo*%XB$vYmuW>=C)yf{sI?P$Sf`-i1^!^m*trcmry58!kEQRV;=@VZtf!y-}B50$IS6Hzs|^z*4Z*Xuu=c-6}9Ofdf<tdICi^6ewv~Xn)XlU
S3vH=#c}vRZbV~*zE-sT#jF~zlER9^5oQf~lLlz3z->Gpi0{kDZK<IJ8T?{-6|eo6`k-&`;eJUO#OE;2VID;%y|iQg?%>ZQrutniBPoyI{`rnW59DdKYiC3i
M)rJ9<h22_WTiTTRk5Z4(kH}<ob!n08)fLjJ4*HCc^1g;A?Gwl$sH1cnsaw?ne^3<mkz8KJw@%iN|q&jOJ!5UaclX8w<&f=T<`%YxHv5d%wFcQ`{+4>-VR7+
P#U<F55EDvN2Lo%u|soKdnW<~bRZyzuI4>0)H|kLqkrcvukr<I#ZcT9{uLg0D3~yS-*&OtR$B3tG1F5foLZ=TmBmumy6<gb_tfN`_b*uP&Ai$&wePB{f%#wV
iWnDKtnG|5F)PHwhx*Im0U`Fdxg}Z=bF};Kn#gQ&FoaQt$sMls{p%W!8Ax&!DG$6xTrM*NOuJMh{Y=q=ZPRfuX5YxXu%2MRf&QN5*m0!RWv|*f`6I7~gfJVm
xqtW-4}`J#TtMwbv4KXW27&;^OT2Of4_?@+f(7jzmX*bJ_H>pyxoFg_r+$Y6(p}h}$flznkjt3{Gc>FM*(tpIRwQTP!w*w5;>C{4n?(tJF{*){+`9(zltyuD
{S{2;_9B^K{@o(m-emS;8R;VUd_LGg)?e6Y3&oWi>M}`VC$ikp+@mX(+wZ?0_6Dq+=hUO5zcqrtsecqG;G?Htpt~TcKm(DvOCvB`QxMZoSPWd=0y-fAFF=`W
gnuxlbR?!@6)vl@Ccj}QjmyBu7`bPXQ10E-C@7)ZD09y0cjt;n8TFnVsjta~`|WUIK{B8oL~aF7hilkdQEkSR){fbnWMl(KBerY}ZI7)!v2F6;lKkfkcHwhk
n4-ep@b0s7biX!>s8b>+H34GdwbuQ5Cc7yhV2FKtOTQ8bN~oXrInIkD86$@5yP)}m!fyJ#6*lvU#@x7$pa*9Lg{a?!Pg46y9Y2s+9hUz7rLE5N<X#D|0?vY4
SRb6-uc5fv`%BzS6|3ge$*uphL-W;oM8_vN39?CF(I?6H;khs5v4p|r)SP9rhD956&yEv#9{Z!X&v?fKo2kHiFfm{s;hNUUq+$f?KorHPId@Q_3`QZfHv?LN
Hf>MruWjqfl*ScCV>MUdkqBqCAJu4EO*y9bM<b<!zF6g+I5fU^CKNDxY0@b;6*G8So|WkJ_*CVBfo2U<
yZyVkRp7$YLRykf@&lP7)mh7hxe8)?Y3$+KBn_LWNJV(_XjZ@Wz;7yJq3&f(e9pC^A^lRffw##o<Vv!Gh`b36Y*lnu*cBURO?E3TcS}63n)-&U-;PjM?`_TH
Cbv1CVeXYzSRUayyhAYFXzB1J!v+~b?-i4PJ=9xjf6$H40Adg7eNFn?q*aXDn5ga_CnaQpgv-_JwHdxbF1{0QJlDW@sk-Qvk(oOryf&?+MnKPjc~X>dPUA|Q
HC`zJUkz~#y++Lxr2HWoxk7j#YRZ0!X4^u-EWMl55W(SIj70o)H@`F1ps8(q_%X6zr1+K>WbPv`g85wC+9c^+@~OYWH|}tiwQFBb`^sDfm*7b{#V8fx;@`cs
zXXotv2PNfYa-YI&Ey(aw?!LLIYCxE02(;~2hda|#5wrMIV*esAY+9*|Bdx3K<{u*F_F@3HNRCO=rp+*D9NG42<LEA!ptz>L?hjmPJKqj2J|AUTAZkGe(G^S
wR!t^+V7%jbGL|TWMmgC+oxXIP~{9OC-`D8dH9R_M=Zr%To&)D_Jd8;Jj@Ci`Z;Nn_{>K6C^8^DHHFl!&ccuLxHR@0`Y3<EeBjP6mv{v(O*E~ER6+12QwkDl
RJ+T58bR_*a$ZHna&z&enKeuV%K2MQE2w*pHLn8r))bBBXZ=yq0MYxIAKwWc2qxg~T&L4zYBil@{euFAAK@!l@V6FL6>D~SsykI$L>iu2ezC*zuj6e>^US22
QS@n>^X2vX1>Mmx`Jc_)jUHTJ)?{;`fSuti;;&kB;?fr?tz=8PB?cVLCz^6K9+=7GzyI`aSqXAG9JZZI(3KlckKFmkIHB##`TM}fQyd#rE+n%Gn0Q8^{%th7
FRw0JLczjb-LOHJGI7=iLOKL{hQEopJu9}5W{{LaPhm3i*iXeU9Ou!7V>KT0h@e*FLhK|}@esz83t9N;?U<JsmuZHhlJD)35&U=O6>e;4kBObW8Kc|}bc%Ss
!D7m8P3{`TK8dYbwv7A(;e+4X1y-nXhF>IgD=C5w7`A|M$v?@hwRO3J4jgI&VCCnu`LIsF$BYe!#5cW%LqC0Cl%~}q6r`8{&0-Ry2qkaj7m?Bz4`|b%cQk1}
6MeOK)l3ozIf!(G#ReDDXX3zI$ZkT@b`?H3dEeRru@L$Pil%^PHdR1CjJN%LKWnR&?6wfe$68ccQJtR;OvVmK=VojJl6rXp@}7BFVzA%``qls}qf@lcE$y;T
8_ZNPL$I&?5`#yX({@gy?tnH-OKdr%B{7fef${r07Oj*cS_Mp+G?{D<VlV241hW@$Qup`oB!s`s{>`{apB|Kv1}cfCl6)odQ3F{`3^_Fq-|%&DL4lrF(rDEC
Si335S2`L21q+zyvzZM;`P4D*YpqYH;5n7v9@2Z>PzR-HGM5F)nCTidFPkR~0Z2YZ8F{*Rpb}eP(NynDli68Ayd9!R2pIz3v*n>->p(fwtx+W6HdtM)m{fY^
<SttK-H*PvW;<>=I%Nx(agABXOczd<n!Dd`y-aOj$kmf&FkRENS`^ql=oMA@osE~gQ?nb@$*69o<XbYt;s0L1*VLIontAd~GSu;|zAmYkcn3+~muL+I!Fm1&
RL<5pKGr=eD8N)3o909ArlCa&22v)tWmIk-YGBVv(UDo{vE7k#gGdE*KUG$*E(8$Cpz}#9kg_TM47P<hhd{4cN2zqteWHrNSM`6wZ5xEf$ic)r{is~o=g44~
=RdX+!FA0vf%kFqWyjFI9w`!<ohWJ;GJ?EO?n13T&AZIboXF#rZff5U;o8QoU>sD9ZFgT86510juAh&OP)I{)`aKw<PAL#3`qsCaCyVIO3Iv^SgV9Ve{Po-V
=6gJg(x=h(`G}kKKrA#g<n0elV87M5S!#7MWS)y*3r9yKEb9#2cUry1$T^gPUYREmmmVguF~U8AOPvs^Xg5k&d+GwqM4zFl2KsWV)YRZWMY+gA%l#gW8B7ka
IevH$_8vR(wef0ByoEqWsSWu>s{mYpoHs6=b<CB|_Fxzrg-3y4+P(EJ5iWA`z|){FnScloj&JRZ3*4Vg<=$@(n~uSV@y|WnCpV*^2DBN_1L5?76#kiHuB|Y)
Y$=h0DobEGl3bSx-k#tA$B66Jb5U>orr)E%Osit%^tt0pqv^z~*N_^=V+{juUG511Q9n>C25*GVZ~deLsA{N=dO%16RM!M!$&F?W4At4g^h!mk5(<>Dh>SUC
h(^p4tt`1aiMgO=uGBNdsww)zLAg@9yRed>A5>#%z3CVgD)}CMWc+DNk%oBKaumMl>qSd(PFeF(+i)c$BW+uEcFdkR)_ELfQHt18ctM<~g?hAJ`jx{&KWtd6
7Ja$SD`@d=!_uoQmb-rRQ#jJ%ZE{gwJeZn7#Q~cXxNl3t@2-xGgu;Bz9v>`T7$w+D!|n1;aM)#6h-uBp3H!^aaXv;3ugcs$W<qYcbQyt)gurK)<cwh-2Vxcl
9}0Ao23~C(6w<E#f~48XOI2$s=<cQ0<FA%rG6d`cRzbuXF|GM=wQ>?<8Y*K}X(0>%zt=nlBGlsIaqt&bLc<6;p7b3dnQ$kCUxRd<(BUzE+DN|PV7Y5vv?wyt
r!G)-NQ10)fz^v3W+)SGC;%s7GkcgT%CfO$Jh>s3A{eWSVs1>48VQM;d0N&3<UrvZZqZ5FGe+M&VUwX_NCQ%?#IzLKG0RtFPVbAcVyFhuwj0e$?7~Isq9Nz&
8a;|vX4lwjoo$xy{hgf@=4Jp36!q;Uh~fN$x)DAU?KQ#BO;8C)5w!?-gF_ifqz*`BJhx2A*v{gTX~gBo@Yr1e(Y@!j9St=`QZQ!BDO9oFcvc>CVRjmWN1n5}
YP;gD!&1aoiRI6az>t(hN9IaO>~EO052uy6ndc*g{zQJR8+ykJxtPH@nZz!$#7%L&2m!C~t9ys=dX+991c4_3kFl{ggUEoL)USjX32}&xuW4KqM4B8ac$rgj
h}WoqkBtUjU4j)?a9~yTE~MN8)?ofEKskxHs^s)B7jG-;IiqA`xv7MMx|5(Vm~CB66USkYiKtIr=hcfSOD0t%42pv!KXNfK{N8QCaSBOScBhD7aBJ$3(uC2d
0#c(!2*c>^cq3QAuZ=E2+~}cSe)=tj2_MgM@|T~va*X_?*(tt-zg%<5yH<VOdUpACs*20DG71zP_521Yi}(K(4cKi1fvu(cXvGI!#UA&r)M!jO);C`Vr1@kf
5kSTw70^EdG3jw=dJ}-AE^|;Nw>B24UX6QWeCxC7PB4z<h+X+9A?OufMx)lY0yDor6q<kIFkS5e`?Ry%e0rm}KtY02o-T^a<Qy-ORX!9ihPS%9Lun*YwYgm7
^U2nk3u{rXOyp1g2HOBXn4NMyMIaP4F&jN^`pOXe@NFZn7;=%??>As*z4;$oMIfV#spl@r05hq?j-9LFb)V<Sa3RK*Ida!pDn^UPMSG+};zq`hN@16Aa}w){
<O1Nj@f+~o8lM_FXjfn6*6!|xF1I?c0_|}L@en~qb~w?(>9g1<k)HgaYyEkBly9f*$d)<anS=&zA~O_4QV+ty#70Mk<Z?5;-i7e$GX%63ZnaMmarhg5ok$ZM
gdPcqUS35hu)+t%VjpH5<wmuJj)Uu{uDgrBh8JJm!-hWqr(ZltcTi)*PwWfi=WHJ_wGR!?-GjeO{DOwcSN=d^>#ni+uh;3V{R!FvD92K$JYa`quIT&5BPeZ&
gW}fs8kVOLBLTHZki?bVcOWs%xT*TbvpC%E_WgoRc0j-;v+^hC6>f#(_oIHt9K5TwK}TSQ?1t!%PR?&Wkb-<?*X6-}6`F}q$OVtX*7D4?w}(#Ap9Mp=n3LVt
urPgU@i5cJC9o@<Xx0;w+i$@xX7c4wM2gCadPxW*N*4j}h=oxlzJwADT>`}d{FsY87ah~Al9}+Kt(;&Lu4}%^Cv9`?!_yRIhD+O~UvQcSP&mt@Llqa@S&B8X
XUSc1vwm0$K!6k}&N5p>BNjNwe^5#}U>b<}M)^j%VJ$IE?KqDlLoP5=SToDuvj1;b4|$g65s&WIlAW@&KZAW;yl0<u7_T0~B^QnZ`1dBGVTjJCHxLGf4R=GL
M~~$mtD-#i+DmhxY?Cg)JyXvx=GNj$!DLHBDyK`uKKT0R^<f5c4n=h;`R#c~)!7MMXLg9X@_`qAoT9Oe_;)Co=3<tTQ-=@BsHm@tf-lZHJ?iDXucJ1wIIe;z
$4s1X^%d7XmXeCCV{3ONM0h#~Hs5LY=F{H_bLxxuedSRz@K@4|(q`yv8rt|N$q<9se}M<oqxZVnnb9}Z^+-NQO)Ldw6>kL)bEyvI0HUU-VbT-ycc8XzKN{~F
xo_d-wP-Nv3#Uqe+!IUFyYG6AU1um><g$bsV?%k8VTY99I86G+!&$r2<~fV;w<|8khtlJ_R+WMZArtdMqb)b3AJ*4Ucb|KuI15HqDF<ETitZV^!mS>OE~&iu
mwUAftSbUDNsbCS|2Q2qV!rlac5M2w{NtaRv#9F4fshNaf`E&y-jznfrLc)BmaXIGMZeVh2Hyf*^hk||A*+Ri&}9VMiis!IyLiI`+bj*ftOpZ{ohGg&7Wkjm
Fo4nZvU@?2_KowVHq&G-P*qFR%$jCL?%4kYV_*qSUA8+`d=`1idu!}N`>dqS`5$!wf-fk;!JyrWQ0IXwkaI9LU2AaBhGjmDpR8X#L+O0Kh6=IW&q|$6)-$&Y
q8^WnVI89Gqf0MGGg84|U_<D5=<Zx1AB4*gYwcxPLcO`}%4Jm-qKT=jK3Np2OfcN`TQfZ{Q^qnu%XVrs|Jn;#=pF#Wl4vszhsUtDw>dsNBOZ|25VIlu>$t$~
**f&*YgVf-v6AA#$0wK<(|i9X05QN7c;m<Ng>35i&Zz}CeMSBvSPx?Zm``7ZtL69ePr><MMnMNWZ(~_;x(z%*<q79$ku_KSZRtFUf{6%v74yRA{JnxmVbM~-
%|E|qCOQo9?1kkBGND|E`KJuIO+K;~VjsMAv>Fu=X-8SwVO4?Le!|v#IDg}5-Z$J~;(T=)PappJazewJG$XI<ASQsFffrSzpTnAwHOc?#t29WtquO*}EdlnP
l9a7Y@l$>hc?JZuvi!T4{wcqvyIDIOQv4{zj+K@H*MW`mOUSu}mVftG@h-!%Sv?&kxk~P`r4nEYBYfy(S*f00eEZ$gfF&``l<&~E1utQ~0p6wkHj20ABBbQW
c@uFinWY7lkvS)LB_#J@5@N^ff*h^gq-fe5W`}_5c<^6oZeS%Ucugh~@oaj|oTD0<s~LXdJQ?(>R&QiHnWU^cEnhvG29+VY&&4?XzGzW*JFpITfzQ&Z#c_jl
wtnIWNbfXSJ!>mLC?aQc<^5I4tvs)W%rHpPxO3j_ws*S@fwV#9`!731qH%aiz_8xPJJ5ECAsoA(l9-3EduCtfj#Sx?jLk4J*o-BfXm3!1$nyex5zE62$FkR{
sbxfbHMgF3Jc_bUMmTVRCjj;0$XEv9Q0%wgV?rA`rT?mY{m&hXStvPUFwXl|p$edZ55W?dGnqfgt#mR>Oy9JTjsv!4?u9{f>pyH(pA_z4Fc_(~TOfk;dkLua
e(6tm6DJ0l;$S72@mn}ly_+n{nuP`>^)VT47#Vk<^hhuleI81yiS!Dqjr^%1e6W}bc#WghlMvPsO9U2FF%8Qnk+qu&Ym3gY;I!(?j{|uR4~t2sF#F&J9wj7J
U)^r-HeFQ_9O&WN3gW5V1;=IN!!Dfjw(Ykmyx}ROD`2V~vlhimt8QLihrkxuGoPqxXstF5f(O~ho(|+qqQpQ@WG&E1Y-57UAV@HJUXqDIn%=ASMmEMS%X0@+
)w5AC1Y<PozaHpEa5?k{v1?<DOAyl%DlIv|(DR#a?vkTm9~^6{#W5hv)iaULxL&kM-xW+G0ln}DFWf>4*8r=y4&=DAi3I&jlO}L=+!~(atN3KBw~EP|)lVQz
6QvMl1LIihLyl{&EP3MaZ?nU9AQpVNXJaw((k~~g`_>`bLdDOKm9&V|RsNLLE~iIBr9IU3{>W@>&ap1Si285?D9W;zF_+*5z9sz!DN(yzptI59<PCXSy2=C%
UDg>?uWe7(k!{je_%s3Vl>IBrnP}q_*aRje(~6M4%>&?6GMPWn=$~e5DW$$cIkcgX3p%0k4Ie)h%@;UWAfLD|Nxs}E>~B?1)~YgYi2&QkOR-b%%OUk~eO)QA
z3D5qaMjrbZe90+>JZ`?*&Ch;9mn?-9C|7c<&L3qQosF)%A0wfNqUKI00HdebZYvr0Lpm_#Pq`P#8jRG>x4~5;(Il;#&C1;?@R6``(^^Ar79Vs4H5(Z<`1EP
pHfIt50;xQXK>5%e+<W$wG#z7^{5B06}F5|1#li|dasB_<nkQN7dSveHq^ZQ$Na>OVO<X%rq_IFGD>VNNx`XN1f}bNk)ae%Pz4ej3^Tc~S_aiQbrhmw6d2pY
AfJP(WOY#}07;AU46FRzved;<7p<ZGuHCI5i+CG|)`7q2s24oT{QjXMSsn8rtwd;1*#4zRXqu(-i!k%D36u!TkxB;CqL=3(Xi<8MvyDD|RsR7b`8&F%%N6ji
Lrs@Jm|Uc)@;|9gy3Lh?5<At4rhA0J;FFlKhCNDrY0`}1;>1D!Juhm8eA1$>wpPMj;GNl8nR!WlG!iOUKIad{r`BZyh4+X|TN@9gR&qcA^=@Y4dD2bsyXoig
Q!~IK(~jCRYD~ww1cC%a96=F5f1Zs4a`n=x+O(tQL48526TM?871Ml@6!7b7^sLeusk@=X3AJVM^x_wP%1)I6tuNAZsGjf+p*e0XSpV0Zx?iHWc9(X*c%9~_
#10z9-wUeXsLPQaGWX}{9tM6@b&2mEHbxiOu)d8JM27Zs7_@Vu%0-rC+iToZmw118h(%ec5a2=002nnQS3tM&zf}gHrbBQwoQ3K0C32%`|0CN6DpiTDuvN;u
oIBs-w`x#gL;FucrSfhA{!D+NH7)@K0OnL^h-{ji(;qNgmIhQ#&I|J(HEr6}`83RC^irj?`;U)j#~3-bh2Dn=gN6I18h3#%4?z%y_u|Q^{P3{dPCnYR9w>9N
PW3I?U9uh*p!ijm<;$`;lnscpe7F`Nu{@iUNqDSZ@5@FeZ+dcuthcr8PkFUZTSjy6M)BaznhF_xPO56BeLF|T87_%Tt$$%!G=#Hg>F^JimJ?-zZ!+nZyVpiM
3kb?o`I<{vlS-@&_;#2Y@;z!?<udRutx2ten3Z6!Bo>Q-1k<6zd0<0-vo=90E##G*v%3V!-GinyOURTXTR&B5DwD<5u%G0vO1qmViY*W8w-%t<dwggg6v|;L
z;_ne%;IiEj}oL+u@Mzikjl0>9gS=B1mZnVlg;;s@D$!+qdMFX9tv{ImqC6=Mq?K(CX}r|Fb;VZQ)9}KFxocOBaY{9t>~WNjS|-wocszi5^WSUiwo8z-^E7#
T0J>1^nQ;2+u+u*IxB-v@^=^6uPyfu?qD9AP`T&XXGypB2Sk{j#4aw0R`!nk8tf=PUej_=^Zf4QY)<yDpU+{e^<@hoBCrX;vLVW4l~ua8%IcIvZj7BP?U2CT
H!xCDt(gDOAIO>1n3>-0E33WgH9jFr6s--^IiG3?19|Bp^go1D!$WOMJ7z|10iJa`V3qRl;+cB)Nd_V9Hw=^&SAo4B1jbKxExE0}2r2?H1SqBq@jcF05s2x{
liLky<Ddp7!JGz^Q6*}Klaie<ZuN<lnF^7`sFh~hWqU9$=EJ<9&`Qcz8T9nVMeMr(Wh|~PPls^J3ob2L4%VF@Yv})$RVoBLTxt{fyGiX9BY+;Y6lxeb>cvR6
H}`sGIn_68dRc9)uKDSoM7l@8QaBOlITvnfE7d6_7ILO;JfAM?!fZ`Ak+>kClsq#RzI|<OqvIIiSZBXO!-D~@-QAmZ2RBSSH#Rv{qC1j4Hvjwi-cn>(bh1*F
uqCXs(osJ4xg%ko;$$o>li!)Wkrd<WAj5Law>tyUh0pgjNr<Ey5Q-&=cm~AXGz20)jfwDFhr?Fk5@@>#uK5A~SB0L&l0pvt;d9g!mr-kawXVvO#i7G`8(ZG7
OSD#`;#{h}Cd%I}JQHldy9e_Qhiu@GPcMhePIsKi3qC&wsHdQPDB)7Kak(O48bu$lA<Gc;Tc3qE#jG@lebtR^soENrn0#<6zJa!r(?D$80U3I&3!V9+-zt87
<MKRPeJ_*{&_}_3O}LPk@J`aZ0JNekdW?l}$vfR*UA&CH6+|nYK~K&a<<+2GO(^JQPnd-C1Xgyd7NbbBu}}o6vc)_09D}IF>Y1#cg?=Cw5V}NMMZ3)!<IR&V
3I^Ty9zCn;qqk3EYuhvpj2&#C6DM>SR$ZR#Rnj!L)sodX?hsE0gGsE`EBz2sPE)0{n`{on=mv<DLOWFHfdNpv4-**Y#Y~X4+{Ww4T)9WCcdWY+Dr#4Jy@kcf
wED*Ci_EKt97TB3Ko#)%`qU3(9y>rn1@v;*3<i55OIV=4Wl5-Zc`@QC<hssl9`0m--6w>ufg<Dl)TO`or}L4mO|6KdZUX*J8eLjz3?&p!+`t5CggnUF<nDwF
YEYFwnwL!?;6Tu6?|x6MP;=EZh|IgDsz799)&^|SPFQGV46YRS<Nr-KmWEtIUL!Mgr4q%)kep5K=z*#K%Zl%K_=7d>l0d5MV24<Hp*`g|P;(-EvRe+jMg9$8
Zh`}#kSgpx-u;fZyTZ<(?+pWbt@^TVcZWLhB|U#$74yIR$gA<wldP67+TvT7pvBo-Vov6(8YN>yWj)ePqLjt=kV87OZ}ch(Qq0b%p#A?+w6#8BGeF738(bFP
EzXW%k-+2r)T`T6AO|v`F$NVD;Wp^eM@Xt=1$?VZ#jOI1QH}8L#E@{OAu&SZx2GqC8Q)YGic|FU6yJ@*@-gyU?OA^22B}03U~JpsQ^i7pMCx``1FLKvdcsLG
ya;G;W6w1xT`#)SM!MnlmNrW7h^$DGo;-3qM*5!3g@H{iHGL887E$})I|r`WFm`^BewfMO#ym9KM~)DRr$WnhRh-7aDx@T<bItOZsf^d5egwJCSsh^7+tkkW
=C6kLBWbZ{Mlyvu-V^XP8hIJ5%LJ&^hn78Dn+@U`AY$ZO+~~Dd$PSc277npRO1i4EVVi-krKM$Y%pY&Cewo-GHeQC2Ku9E=-uVm;AvV$mGxo3;sDTaR+^bM?
cZ!J+qn*0`ee=AN6r$<TjPE!`Xv7{bYUGocLA|)Hf$Uja5V-y#W#{vfVNoA|OfE@25QKCNXAOIacTIC}JpQw$(M`PjMpce`q=RYu;RBQLC1<!s<nK(KKAIsV
e4AuO%!x+d7U@xbjs5rD{puB%Ct}>#=&aKpmu^<I@<Z9hwSzSw<IC|{SxP`|DgFe8@^6+p`*XahQ4;3w6ROIvT1|3XH^d7?=;fTK14PKD-${Xk?2IP{XSnR<
0s~%p9?k76Bww}|V5Nw?4S<mc7OC(Qp)u6I%K}rS^yCl6+Z4X_GBteZ@4h9K&C~lqJ|HWAUa^tc)GhkD7@-<Z0khdGUoAM9&wq_4{hcmgFO|oIkZ>L9$e|J=
Y{!gL2m#KT-_^ffJ^tK9M_(`9DJLXFd#134h5d-s4tv*|e*fS&gRT^)`niNV^1!psrng9zgO=!TN=lRj(DfcSPrP8RIRX@2fteaT%!N3s6)vS=Vu6k(6^`Wv
)U5FhsnHpcsQ+yD_=k#`p@^~2%W@fr$QL&#ZD@a(X=-XgHB8i7$SNLL_ka~laqdv0e|cjP!X_lL&v3M)7M-@`6AADfO8;Bf)Sn&>6f@%avdPE%&~mn=@a^o*
LN?|f)_nzfTp0G@tr{RlCYrhau-hzwfz!LhZvCLBk_?2lwwSUAxiK#V)41a}!RWuD36$5oLKUp=FuKK)^g+OohkjJU1IOTk&&D5ENa!gt!Gd+DCxd@XDqh;T
OYZCrG~aUqTo{TrX@@2siZHfHIA@p~n<hd(@X<fzc*tiKB3rMTro@!(pXF0Eeze%|Dr9xVLJXbiUFwUB2`S;XK@(0xrUM1c4!{z$gkSt2v4`VD!S^h#&6#-A
>Zdba)=PKa50|l<sYIq)POo1H-)cpz=$Ws1)1F?z7;PZA62JGz@JrU24T3Bs0V$g=8CgD)qwzO|FgAsP1D%8g1Sq2Y7sA1zX@!s%Je&`aqP@>9e2tHLGdzN5
HE#4O^{>P(ghzOgnWUx20&zsP@!@OFLWmhOWE!OP{3HUx$DN0$P%oLiOst*mJ;6MYUFMReXbdy>9h9xN9%ul1I7SJv>MFuXEugMftl~16h66`Jqa@-?S$B=F
iv)~Ztp{AGb-yQb3~=AKXV7!hLIrm^(WceRrc$I#U4HX5<V|EpLv`Zt<)Qu~#Ab}5X&o8BX2-8$2f$pJ9NVSrfdNWn<`kR#`SpTkvg|Sz`3p}I1R_x_n}*Q2
Wf^3z;Hc)+WlnV@*8azM=x#1J!y;#9D7qqC<czigZtM1u>m@RkMj#+}YIk8jMi}M}{h}<95R;BwmGy>YAZ$D7r@6W~DuUYgs&~kGiLp}{xf+1L1CQD1`x%s8
S?O~~DRGvPPaenWlOv3Gc?~e>$zDY533d@kNUtz1IIRPlM(z{Eb^q#}Fs+WvKhI+<nMj_uZ3pxqWFg^Jk~|O;r@fwZ;|8rZij&qo+?1FhPPyiNZ;(AU3b}F$
OIYh!`pLgaK=a;^^T$?|)0u!iw)b^(ysMYSbByy2jyiyY^_`C#zD#0^nE=4(m@7(!+uQym!KTZbkW>KaDSi&o^jvsH>hw`Ff(&3O5q7_6Uiv78$LRCwmR|AJ
(<DPV*G>E)(r=|{^HE_W(A>=GUXr&@m~tYo(zU*MU=+P4w=pV_=c3TS1^({~!*`NjkdUSaw#K;o(HB+b3A&S=3ZZ~#Lk`aek1Sg2nifPK2?6K>Q_;tu{;JlE
MlO3>kT)zuK=evD<QF*PJN?ubCrK)QsmOU|-zPpFh!L&gwqXzHi>UP&lN<tbgup&p_fMKDFA`zOdzK-}m9)h*J5<F5hf-BW%dq8`An$d{aw{xVP*AVYrG<Ny
ZQpl9Kk?@VH~t!YXA>e>oZ5zn+f-bOl{EWmfsLzVuEA_pq;Oh*NTO-s1Ltfx2@;Uw<@USQ=1?S<8+bYrajRE5Fqz`rtKeFT*VmZnr(>1e&()~+VBRDxop{VT
CnCSQhs|nt$wGm>4Ykar4%MYY;k@-d5f?r*>yFj{wz47HD&}U%l1Kr|oRrT`ajj9-?k*pl?77VOOps9xY4E)dLEPrhU%7uqO|rBST~MalmS5`74*GIbfa%@*
JhHj?Co~iocz)mqciv_3QDDn!8i=n;M`bMd55Y!d>qO$lkP-p#bi_E)TEibYvvVYZ&_x*~eG}YVzf5P3h6#4c=NhpIbdV_9a4LH?n}xHQ<r^D<;sP5sX?kQW
*PHJa)tg2#<@F+AA2Y*y_*8lKs3skaI#@f%3B}`1XN3M(q<SBxMS<Z#S0ARX!`LLEp&B^8qtDr%)=+p<kUm~!IDQtfB2Vrmyhz`NE@F`4;CYH8MXlbyuc?-Z
!i|MmLhRNLV0f|DS1wLp0pE1uN<><Zl)KVswdTv*(L?C8J<QXqHbj5f7H}Akx6V$TSQYu9HTD%U6g#NV)hEohV}ot!<$TBshA4z!OeSsgww#MRzxe(eL;d|2
)6OWTta1X~`<6a0H=4ia3lTK9s4us}m#v_FG&Q6sgOUvd7eYRNX)O<!o=ETWm<!{ulJT;zG!bjUschp>Qc<~Q@`Y!udQ6hy6KM$9k1H;|o@I-#bSuO!vvALB
R6o>qU#xqr8BZCs!v3YxNWex+Q5{g^H9p81Z)>J46|P!^_zTvA;@=dRMgNd)#|XSGa1*7FQ%cD}ue?%0ClJso1q(vj>$ud_ii|Zun$!ZrOg8aXp*P0M_jMdC
Y8M8R;R+F3K8{e$`uea`gd}V@FinA#IK^fd(V{6&%vd-|*Q&#Y%xOn&A`PJ&kxApHNjZf`DX_lEB2MpT$mLY?>n(GbE*u!Vt|#W((-mX#k%eanfB<${1yYKu
3)iYON=imIW-sYu49S^`K*g=d&vSK|>pAb)H!$&5RBo}vbQWj3%-d1?mWyLh^(zh(2{p|r6w%C>Y4}cLjfRKhMBop`lF2AlOrHwySFK#VjaxTEhIJJ3*4l$S
fcTV*TqW~*DlA(zUO5m)eEvi_(xnxqxGKCCY=W+_wokQ_rm({9dilj)bMapW<OudZSp1JcsbLw7W?kNyh*GP%u&NaiN|1%z3Xqni$FhnaEa?q>4CvN^Y!QKV
4d|H&nSvn!v+&NXB|KJoh3XF`fdI*{;gV<b{Zf)01B9Wk=7KKL#m!{S{i$LrU**KVpamD7sioYZF0<P2^;Nv_C2;a0cgyn8*)(5T5+A}Tj5!(5<;0kGFG4%_
<}#MZy;9MtSQr6Px$8$}acSi9{ghpfgO{8`6>@`rT&CaoXi0obv{z6}f)-OIX$QPLo?I!unv%+cJyv9>6e>Jsoj^o(7KG0C=0{^-n$#gj2h(_}8mMOG8T=#a
QSEYf>lZ}7`m&0h#6rZ0f(bx&PpMkfoHC%lLxWUg>^k00h{IW1?oVVo6l-6;_p%T*eUMtfWRkH=Ij8?+!E7a?bvQro&ee&bYYy_u$4z7&C<uLkhUyL4PfNb`
Q%oeb5kMM@w)I*lZm!c(Yk`NKu}|bEY_bp7zwhJDo!q50GaQ&81(;-D*uL?PM1X0ANmS=aj_{C^CVXFP?P;VH$+L_@e$}{Ap)Mug(D+_X=Oa;G@^2FCk^0*}
s(Vw-qiu5if%xcsd*8Q0Tu_NoHnCg@67KoUQhF<qeDB+0@DT8xb|VnrF@dec%mdzvg_C{S50p34-faCfdg|_Fv_%N!0zr1iD*zOqrqf^|PhdNa<aGFL2)I>i
Ldr{OSjRC*F+8N}{KVU$?U}4NON|YRheR>`^|ISh+mp9K(y-(}Nm(fWCp%=p6+F6pwjF*B`wR%fE1@-D$Z(1Kkz+GU)b+eN)d3|^(1MA#TgtxzkwK~PK`13F
gG6YZ4p^ZH+h0{(-N1Kdu5q%ZR6C9J1H&urcy0Wi=;BFxrdhv&CRjPhe=+&%Hl0l}hoT3%NO^~Sn+=UI$I&p@#l=bG6r;te7*K-;YT(y%x(7X$9dZgIENJzM
@UMpbpod+SiT;9|Q4)(Fe~2c-QnGKz=0j$PE(IThAH^ms#4<U$K7fIc{(d3-)Tgu5VFXIu?k;6<<>Jhfalp|+CD0Qgx-v>5IcnBk2kL1kv2BFpL%c2A>)`YL
7)cC-$QYr_V|&;6H5-mc9bp?g)HTiXu21wwd4Q(`Hw;r7uoSj<N`7#I0r|o9%sovnEWL{klQxhB>b+4d@r;E3Q*DF%X~g^?CDZA&v@4qk-f=d2dh^zH);qlN
wnO5TNGlAaW2-to&(Sk;9%K4$#s%oHTusO+L}o0j=cn>QFxg1;*TiJyRV+cXWYe3Ci4<5R0G}}@&|PKzfCA;H8gr4({iaSDeXT|{?Ym}fLrJ>M-*g4Fk}=!A
6M&IKYpE!g*Du7(UAFe2plR3&F>rKWP1_d}Y?mTC@Z^dn*kq>zd#rMIgYigXx5dBSm>uZ;okI-6M-ZmNP-vXXf2#~p*g$&?f2=<3m7-x>H8GJIzq68~7l03p
F^U_1to1b8gYst9qdsFs=Udu(zIfJy1+^S2TRY)DJI|H(VQrt-^(~K*_kwF?7vbSdwvY^03fjbxGDrYGcgVJV=z|7wNJ){(K<yOq%&(N)^&%5|6-TL-_a!Rk
HPVJ)9uM`WKQ~$CReKU4xj1j<i<md4M)Ud-q?i)>bgbaI=62j}UYj)yry_HCQS+lDLjKd$`{%Yzo!oGo=yK7I&n(3=vmuR{+#?=7@f>Q|2~?MIFAYF+K6e53
_ood@dTfBhPxW*Ed?L58SnzeplC|r)4k5HUOLy>-khJsd%}%7DZpv>jAgx_cZD{m=tBD$-XPpGn(Engh2u18*Y0i$J62(JX+f&G>fw*%)oVUE&Fk`g5RoBs~
%ec>LjemnpVNz8}QgO-&eb!7qPIl>FR2;fJQ+Z}zyla7^^Of>z^(3XI7o=?xh#eH`qwdov?&$KW@B+Nrzr4iDAwR$N_7Zu0kw@4HOf3sJcRLM-N8hsOetA^Q
zqKSz$dxNELO?kw){)l-BLH$d|H%&GhYgj$pEk@=&Nx!vf%_N74Jw#UO<}qT7b`ExRjGpY`Da&cjh7qA9;n`ZUiiW=)+M&p`+02iq+Ak^a2nkqUt7c@79{A2
&oED2+esF`_Pnk1_sCcFfn<Bk&|MzfbMI+WUT<<M4H(Ycn&DQ6MKrkbJc{}rNK68>i{4>%yrV~au@z;arxwHf&m6F!+EX++$UXtLM;W5M1uqm1DR6$G5V<Q<
hjt75X2rJtGSyYxrgvq~IdkpH9I<h~RnnH;wo)rD^qtG=9(Nzl`$9jaLC9wFc@@uckdpu~JsPcU%y!mY
75*m1NJQqGxP9@3)%Q|FA+kp+pZxUK1Q>49i2nT@Ho~&q9aJ;|UE0;)y{MAuRCkLN02Gvllb{IUCrMPgokC>Meeff$%%NlJB!GfRXfp0GYj~yv*x{Ol%AN}7
E6+eKU-cxRjJv$OwCeN$vp|))td)Q?$T<Q4{EsGw$cpnoGz-I$i@+dH^Tqmvv~+R46iVb$T;edcHLPKUJ;10z3C4sC+4TA4-7x0_dna7)kbZMmDS19E!aHZS
?T<t(ww)QzKX7rAjf5MYq&DmsASbT51SyJP%G}uaJV?JTkReLIWGg*d%z<qiYBk9GiBaiz8#4SHryLP`kNT2K#4PiPYF#2or0{e@6#HdludCG<Kf^ec6xip}
waiTM`(SxO=;UAS`D*HiI=8~MY=tQicSDp#Ni%9>J7Uw<`<30x&R(==J%um>HepS3*^RmM_+Tp<!(s~hX`d^%N}Ceb+oNC21<L7Xy?YU&D7?Mv;l#k(?ahTX
jZ?{oR3DAc#IvcIvZ_PPs9<@SMtYLFhAg!}?Djh2+~%Qo)?3f*(dRw8&v1UIqKUYzAa<5t=UfEweE2xg9(T8Hv1S1F^uYwZ{OR;Chxip%3HDode+{e6?rd3c
8YZg}=Lw@+c@i`EZG#I+yqvVWiZmkOe`UI@db&e^gO09>=4OtE78K|&pbG{-Im%aTn+$Rn(mFSG>LveSyF)Sew0Xz-WEg;dX`#%Pix@u@6lq%^ophtTbX8~5
0cX)bicv-*DGG)-MpmX>(iB>|JNE(A*rSsz*QTvl?7al^YUp0M@>)R+Cl3sU(%C<J6s@fvua{Zoc2)xVBQ?07JAzqg=y9m`!#19@U4B;64TMEA&Y`m$vi2Wj
s5@jF1eIqtY&zjmYpi1}p!p;eG7+sjZ^xxV&qUa5D+`N4bKkev&1|oa42L8Erm*pIearGfa#`dRQ<?|k3yI(A!|93^m&7?>W!1Y8oBF<uJd*)XI3TQLy|Xi|
yJ2vHc1WIS*k%-1z7C*uU%g$MO?LI9N>E*bz9!0IiWro37?Ox@q{;vqc+l_?6F>*5^skn_r(uN^T`uIC&~+jW&suHWQA5hoi6Uj3FK(?JO^;<s{TBv=Rd#rV
t{hr81d`_XJ)9@Q_!vPgkDSxUJNTSYSJzTd4ZAP4%?-|1Ou~p6vmM}?iCUtxk@1+lW%NxX{Z<v`%*6Te(&9q_OX5&aBYQi|nE*#|oT7LCUuH6=EEwsSGw}N3
%N=1J0+}tO@kb7bc@WVP<EViw=8(Wj#&e-5(6!C?cR^|T-N;6T@Rs!ZS9$qE04SZ&u6;@%&^^ywERQOwZjHNvUx8`Ew7d}z$2yV_QJou*!qQ4+3sH`NvkuOl
1<2i2qzsFVWYJGtASwZ^OyZ^Z@~k?c30$X=Q49vN?l;cs73X`^KgKVnZ38~Ijt?Z3VM=H%#p@Cg`eS>46mc{M$9<pKsA@rWa{~gd$=MjG6CQC|SG&!AcJ;xG
`qnx*YOH}=+WQfkHHV?o-+&YoSP1(E&Yp5Lcx8J$Hb)Ddp%&Y_F-i07y?<6UHL#v7PKOebQ?h~a59$xpIUc!r=jPFWscJttQaA-B6|rksdrJT7K#2y7N@X~_
iA*}MCl*7r&U*OZhf-N&HI_+AkExk&-FeS>`2`!mTUHd-TgP={ktj~iA1~-lohMj#FFS3U=85|K+4D|HNw}nv{$bR9EWa#X`4-~Ecs(lY+i>RZ0?7WvFayF|
>dWjL*~@<NFHesN{W#XsYYdS7qEM>Xo%J}din}Da9W?5KQ3r*u5YKOeV^&fKH@k}V=#eK~-7;LD`|trlAFpF0>AUl$)}i53G!{IH_g8X46e2N%+*^On&E0)E
*pjO|L336LOUmC1OOhT{;CRX1%Z5!-G;Y9&s?xgf+usqq5@v}tzunK|==0jO&vrItan24Z86y^l%iKah)4Xw<C)0fLc9z{fiLxZ4xFHd(`72z3&d=4wKS5{c
NDKt#N-5W~-wTkXv#TRmTG7`xE2y!HI)DcVlWY;#iQ=8Fv+!EZXvnZ0z4mS2Mq7hq`40~{p2`Ct$p1j!ZOXxY+~!<@nO(Pz{Q~5=BT$AA$R5m(yh>&^ITGz?
=2J|*Es=d~Dc3ZNBn){Eg)Jnfis}hAE;NorS~P7QReCp0+T#R;U*FT(Q%Sh~pV8=zs7@foM7htg$seY|3=vPfzOq#Qh|dbQe6@0`A;?-_t>B@O{N<eccukj8
{J7`<&L|;YBx#u~MNF8J#XPRt!)l|(>u&%#w6rwDqB~WHdzf>*A*?SOn(yOjL3LHoxqw`~uooBf7Rf!8w;(_tz~V^wI;q2hZA@@C_XMR}^dtI~*mM67TO)ca
N*1=vn<$=Owb-ZKuy0ytTODtVBuD&HXDVnNHM;82v!V%30O}8{V9e}*Odi;R4JjFL2Jc!OG4*#vy+z179-xCpE~s~8e&EL9Nw^cCi?et^s#1+0Bewzhr)Rbr
8|KwwSe?w0u9t(=;O_I3e1F{>qKz_J)KGp`jXYURhNZv6sJ*(@?ZGK^pQlpCQhb5pj5@A|Vg)>hnwRlwgK$|yeSjrF#d_n2IJ`yWEDM@qR!hndvzRTespaJ`
Ca2s*-9!aKYLj63VNwW<5nzs9pXL%!e%v4@$Ft2<g*S2=33C=a*MU<3dd&*r7o>Kc#<qx9q!Gkb{o=Xy`;ZgzgZ7l2{0fR*_V!~b^iwX~P_Zez$ZWzvMWo&a
IQVsi-81EXHi~;q!6qKl?$jV`L0t>Z!0DFC;8~6GIM9Lt>SpjFFOD~cZJ)rmU+S0>cg5?qDzrEHTRY$y2iY=p8WDZ&AFEnATw`AH7CubA!2a;Y!!1e7s5eZ_
Ex<8h0OUBr(8=3QcP08Q9Pi+CuTN&GiYXLMx3ib~tG~QB?P$+!@nj7@j?+Z^`4CkybXv}n&B`e*-^u%cXJdC3h{A>o+#KIB$<gReEqDMyytdw7gfnK#GaRCj
3GLDbrHijJmTfe4!%lvDy?z>aG0iq<2#P^fFkak2G})=J;nnvdgFPG4@w!~wVnwZy+X@M~ovo|ya-?`Xwkrzc!%=%K?`W#~9c_E1CTRFJR><`2Do)H`jg42;
y9|7H&yjqo%#BVQbiKb>0w$o#WsX2Qs>pEkc@pMexz#ZPM6EBNxD0p7u&?&p(#5Mt9o&gmOT}fGq9mpRAPwi|X&)F_%Jq}E4ZOu!L??2AG{(55P2_q?T*4&w
-5N%oeRg*O#zff9@N+@LjJq6ND5d#)<&owXoT8c<?i2tvd;Focdw#|R^v*c4$$2_mNT2j?;gejHgQRhkAS|AaC=&v^`bo!bgITZWD2CPd_RPM7&xbDn6CZ?A
v#6>*Ubz73ye2M~<Cl`8_t@bbvi>M!=(y{KN~G`62x1nKbE&It3pjlC5MD%fC0(%S@R*Yr+vq0l?w!*-sEbvVLGJ;xQ9?YXzQSb;a{tn-Nq%`<WZ!|bv?NN1
2fawmdUv9&r?K7xWp;(pm8qdQt){oF1^O_4$w{HF7w?!pm@d#}oJ^9h7C%5Pmw5U#f{|NY7k((Q(^?Is{x;^WHp%gQz4#F_gF3I&==yYC@3`@?-&UFTiY6d0
Ntzxy4YPoxU`UoTnpu{Ir4Yl}41X#%cFl@_LWC8YrlxJ<>wmQ9F=^;&j{9{pb;dV<z0Z#0NeMsH)cr`>Q*KYfLP+z0G{+WjH3-A{L@T|;I;JZF{|EX^{m9QQ
#AA(`1r#GKT`iv9=k<<d6;h<^B;0*0jSVw;yTG7uxqHEmc<^ey5pFoBnam7vEsJlA|G@7q>eI~P9W*0?@n}Cf&GP$9UaP=+n}`JB+)8b~Y!D<o&dLxoIaW+_
PCv&|O2xLs4N)R1mAbL|H+b-ApbPha_U{#}1Ta<N%IoSk-7lz-eB23~x#Osx3N`W+DuA83Czm?_#)??^iC(B6H`0)o01*hh4#G#aSt{<&&XK|d5O>+QSCAGc
4N(dcEFfU$6wxJBR(*th(35y`a&=*C3uJLyiLe`?50pm9CPw-BEOFSk2c%v?DMkOdYHcKzE8Zxz<CfBGNHU@zGqtQPj$)Fg@13~$8WquS$TM<XcjG`sz_SEK
nv>1K>h?tRw<ksRVffj`<(BGBnT2%k`-r|pw`V69za)g@+;--(F(ep?ex}LM+ziG@_B{R6y%6vLtFYE6oZg!6bB*%bA-GG=m;|>l1-B;77H4?Q!_zreV$F=8
BMM+sVh(1PrRI*crmMs;ZoG-zuWT6x+#1;(iC0<>tE`Xpn-_m4G%AAlm#SFiG?+%W$nR$)MSPzAe!l1E+GM>|@)Xo?J%P<-@@bH8o)Q%SHRs7;&OD;a#zka<
L%*#=cp;lPqKU!d@-${zCrd5inTltPnG7)yWWWAc#_Eax_rv*-6tMw8o25o(6iR&1&*Jky$EU3S#p?vV0LSqrLStsQa80K>r_B8+N+fFf|3TI5@l)yD&7-34
6^GYoRE{QFY9**xz;%@m?+6Yu?3Fxz>cUuS70w3IS5V_T>`YdB=cq-+Y+}{L)9%S#S2+{^h7>2x91<kr8sXx6s=l&-X0PYk)AfoK1yRdVEPfGpRk-=9Xi$pM
czV-`?B$u`<06pFI-CbWd(wxLuwNEYAAO^^hV-GicarbIo1BL-9K@T<XL&?36ao=YF*n7HwIhXd%Z9x3_GGy(5_v-b)s<?Dj)EeC{zm0pJ5+|1u8kGhK(xoN
aWT#?^tg`Fd?7W*)wd~DCYFReOEqukLQmGPeQHQXe;Xwsip3M0jl902eGf!<LxKjD;B{GQ8g`A3fKGkRXSE1_cFNfUyzUe%wJUT*Djtt`)C<FPs3{nd<m8?L
Bmg)8<>R;#WDaQ%dgz1r53xj)BY4)thjuOD!n<S{p@KMsA}rX29moqm-JURJm0D}4zl=%AnjAJAhWZgZ9^FvOdkCNj04zX(9tpxolYK}ausc4INN7I_ai~j<
5_6~>tJ7S|xR_P1$U+F&xGi_?%@N0!IdUW^=$z;NdjbkcBgj4joMmArT_uGg1*7?m>SGR_Wr&`DUw%^fJ^+mz4JMleX98uH=Plxa!ks31bncMIO^=_@{u(HA
{8Yi51{S%mE-ZtL;{f2t7YW_NuBr!sTXn0P+wRhTt(1dSY@61*+V)}$W3=RP?PB-J`$p&6_DMQZ-d|sHT4{X=?``J)QZ=44CN-P|?2!0txkIksciYAGRGpgX
jGEe;>O~hdNQJ{|rRQ(tj_*mYW7n`*Y<_QD%^O$1W5p)F<674OT>$D#93OKj$vtOGs)JZ)S1OZ7oYXjo1F^m>RgEn2WtW08Ete0MIrlN|HhYKCZhG+egFv-@
FT~i6s=TeLl*0e(kRoeX)1BTjz8$WLWki~sSRhPg_P+cz;bjFq$cs=KgA(SGo>E>VMO`%J+q$kuk7taM$p?=Ox(L<A6cdaoaC*}0YSxkO0^zkFfld^d^S~%}
**5~~3<`>O)I>BV%QP(;6QkU_IFtVW+lJ4Di4?+`N1E!^V3C&8e5u#Ay#8}dPgU<XEbBG7^jg)dC3HL_W@u-G<_8%tPi6SjaM@pVGl{5E$dPEZJf{mA<W{Aj
<wi9_jlhiCDCaTG{M6&@Sor~jjQMsOyf>+pUDz#jirlDf*xENCqP=cli#hQD`FoF8J51UzEH`N;+8<*r+ZANxlFDEs-1uW%RTs34okEQuyW+a&T3LToQbL<-
8uGRbTo7B$6eq^s$ndvMs4khxDH>+zbHmqoNpHPxV|P#&w@n?27;J35cR+UdA09Qi1QEp8IWRYwp;i;6jovRa7Q`T_1gy0{kgw*Obzj=`9J65W?Da0U?mHsc
2crg0HaEmoA+X7iPjh;6Ld$V-6}xQt)3$yvipNlk`V60L(Heh{58VvV2J{jAtVRrpC(-dN{_^-wibyBAo7jF6J&7TLEw@_;CF4JVV`fs1Q5RdIT%yZ|jw$@|
PN$aUfC%M9Zxp*0OFpK?lR--0$EQ9g@W;>Dy5kiEsEKbrGj>Z!_4pOHB)?Vkihd-GSC+b0Iou>SuOO{;dXejsbQ$d|o9uS~Rm8F9q_mgrQk-5>QB}I61;Nbj
BMJ<HG2S*u`m(MkIku@%E;RFZ>k=~_q^W6&zvm0t=;VU90P(B&n<2Ry!InZ6y-w1U8HFF?uuv{AF?<zS3E8^gbp3Emo(tTRqY*Bpt|3Hyng>k68>b(cjmHX*
CV=nwH4r%NKH1o4!H)O$c<iF{G_#H!Pooz(=|CC)xLX6%j}57jD6<g-gV+JLdV;$X`62<7R1xKWTWC%&`Hm<KU>;dhY`iNbXo9i?K3}|=60~-+8Y(OZqpvg5
p*C7$1Uh?8WDYdjAgE%nE2-bY;geBo{g1-UK*DZi4p2`ki+qo>H)NV16qBnqv{`=I!El$4=9`5lY=eg;O#U6=<7?eBm-T-Bk=jab2<gn+*$NNrT4iq7)n*Jj
XMoBQo3#~}UVirIt>$W>Y%<B(U~Ph5V|SgU-R1r4FPFr`Oaii9vdqc_FNK$FfO=^o%;N&rNT`3=DuGP!q>&Rfs=;URLlW(856e71c}gA*v6Dj%eZ!g&)n!li
+dYu$G@Qm$)R>JoK~Qq*6_5e+7yy3@wq90GcJS%fHvoTS$8K;i1jv>{ZM&uefQ1UtWuTyMEy=EkJx5l@qnJf`NoL5R^~S}7%nUnO7xFWL;OXCQy3al2u}W~|
ibDwzZhr3eBFP15t1MzIzhb^{YMqn}z7AK4`a-AnBn%*Q3FOD}{IDVbZms{@!W{a{QPmdfyVxO8<t{v|#F{Y2@i6r8JF|@cv!o>OD~;hc-fR<iM<`5mx>VfZ
x8q;2WJD|IE8HoPoEUYc^^<P2DgH~olg2hIGX=|f4Dxk7AYH{(*AL%_$^ur{*~Rt@J|lZFkjGDBk(9Xb@O%t|5$v0C=b4ye@REU6b_eg>s=g7`nlUQA3}2L|
g>LwsTV^DB!X;R;u1N9X;S&=kepuAJY0L|LY{J#<A}*8%)?NsCQA%r43>N_{rwIkEYmCfw<l(Kfa8%v&HGX_JWw~DA>(UvDRa0_G6M6X}JJnCqQ0;EOEf;Bc
|1E+<FFuXa=tt@V6ykYWU>)+K7BG<Vv<hL6S2hez$*jqEzLC!*M06!NZfF|&>Dg1nG*Rw>BiO&id?k94kQgJ?Vlz^jPSyjI4(kD^{NYQAFp5@yod`(#*W1)6
@jJN)>*Y%ug@*IVM19%(OxawwEZ*hU7A2)@6ik2K2#3bhB*Q34Mx&gE4EUIg=JgtAgWFfMm-Gkb@bjB!!>rsK<dN4@fN{zfC8Jy5GO??E<FB5Rp@wPmRjWDK
0=W%zODXqF(&~{}6S2_g%t_iU5JcxW%ELzBgx>|{x|A3%&H1ncE^QL_uMQOiZBDr(x7@n6VZv0Fl801&bHCs%x$uT8Z^673wLQ~|M>kR#ApeIqKKdc%v&95Z
#QlEY)Zq=Ta=R@FP%1<}f{uZ%1xki=yM{>1PuFfv&Z{nf2+q(+Tze;45$U>X_?XB6cqMQ>zGdh~Z6vZ?B1m_8KOobNBkYe0Q;lVVl?dp*FmJE&X?x)H5sTB_
WeEyeeja4jS7lgYE2<-!(bq@v@FU{!3-68Uu83h*wX2WF03WKWU_Iq1!Y|)d<1#8CvC<Uq66Jslvih?$0(`bysm~LFpNnK8eaV$#T0Ca!7^q+9;`K!dbm;Vi
l4NKI4+>r$I+Z5HfW#~jtuBSm9b?9Bl?!z1I+n!`M|15$s0RF2_1aDu;YqJ%-zu>{islPILQzv)yIYfI^9PCdl~o`qAmRu{;rDG&#5?wQ2$TIdY6BZ3(&DWn
qfiR;)f8&&)%!Vm?mX8MTKtaRwYENNb{})#J|Q|npFD8WDe%@ikd)`&rVn)h8yE^<@KZZLOojB2WD{TLt*kWZ)Wjt>HCsCoX1NS(JC12F+;fp3g+514YoG~!
V{Vw;TZ;@I+F5Nllw}1HYcVaS0h9?C2K9PhxAOMOSoOKaLO;QHDkIyUrE0M#opvt|$=Y8*%gs%vA3tIFJjoUS+%%uTbO=|07Bg|U<;>K`iB_Le^KQl&yc}A^
5$3IeU3SieTVR4}7|Dvp;54xj)e+9DknyhMs8}=erKA?#I`P7WJP@+>qeEwgiUx8rTT61#;3}r!M?yArVjl`Fr<-s$Ia%nAdf=Cn>*&a){!`g%(#+>GOT<9$
v;_2S24Bxp78>!v3#Aa87=5hy$ScRI)Bzfgc#rAk%F#nayGa{xJk)!ox-~UF<zfAv#i}Y`YVP#R-2!wO)5?pVML<j?szME`%v2N2HG){2*J}@iLDm-b>Z(o4
u&KloN7dZ`>Zl2j)4q?dR79{wQ2b;!?$j}d06BjPT$kD+UcXjDjI(WA|Fh9(Vx!$5Qhkn)XYOm(q~2`RMG5RG3nt4j=oS0?WA#b|nz06eHz{VZ{Al!vt#-R5
lK3T|Zrk(X0}D$UPHk^fRr|FL7m;&9H^QfMnoq&|9OZF@WY(*&2v41CQzn5Yfs?k77Vj|Cmyt{tI||TTPCSp^6yOk30d=Y<8IWT%%L9>yW<$X~&_uXFQD*In
$I|*y`88pdr+27#4?#C)$>z3JK-B&n3OW6!r??v?S-DZ#MV^e%L#(RyB(?+(0H4A)emkg_CJB(sA9~AM%er<1zk_~%*>CMIDeo%bp!~9=(Fh`32>5!3q0V}y
XT>^NB`a2K<mD1(y|t{dPV(teT%_UwDoL|)0x7K%+}s?fKD)~?c|mY>(>!rC4Y(*4@}Ipr6@Yj;%SBv4csa%$d>>Q+5;k_MCSweyre@!oJ<l6y=tV8SHbuN7
P&}~v8ag8qn){~WG@jw0pYw-&gu^(CZJ9b*&q;(Jq45J4QngnP<Egkht@{1sj0vp3x{+%$>o!q=u_v9&EWfcm@mG=?f5afNJb>M*tm~SOlCGw?`&9MWk0hIU
>nbuRG1{6PMvzN3)1{|bnBs{L`3QPaM2)jhPL7E0$_u9H>8qxZT87Meh+6DD=&7kK_;)L0Xg4dQe4%2KL$j*nF`-y8s33TMA2-*w(>rS{`CAHmN%8lk_13~6
eaP%{%nUfQb>(Hv1YI0)^YIG7Y_^dV5eEAl^_;e=OteEvsT=d)P2NO4$Nf^6BWo`!38=u!b28!%i-KMJVr9u?(t#}4M6#)F30NsKWKr`_HspKU#PKPd(t}G8
+aF;1dA$L66`OlU<hJwX*fXwRtCf9R7N~$HI~@!4w_RFDtJ;?fI%#KI`SuEmG%JP-O*rtYn;t8DMT1ceKYo#0Ao_N-%kKvn7lsg-R*It}roM~-Hp_XH^KDnd
G7xS*Fze4L6(`;}v)K+#E4_HpSr<W%Hr2(Mt$l>Uxwg;bn*3*gC$?!)%?%phE<$dFr?2Q<?NB2_Va#FlmIU{(OuVR&T^Poe;KJb5&>*zOG3c#|Bg@MP;99So
Dj+VqXt*VWNrpK(xgu0aGg=#PlBv5VHwy`uei5~u^u3)90I`tgLZF+uQwT43(*Cp9sa$F>Tw7dm?NUkjVXl~dH|#ragx4Q%ByO;w81?i;oT|#yHE03(`b^s4
!D&zQ;yjdQpOhXOfS!oD3wY^QgSg5*hK~h`By{H-%~O44C+l*J5dW7vSy}`9GmsU72lS5Tnt)*MeXeI5kqe+&I)BQ-TvQ!ZxU(jCn`s${vM=fVRo`16l!#E{
9~)(9B}F5m<^$O?#qr`=C~re>vlpDGZ#zOajqoya3UJf_1`2CgwyvQ8qY0Cx9T*y{b<8{Vfy6s+jp6d*pH+Y&+h|<)V+brF=@;@dkTbkC@d+>3>Y7`#7o=Fi
85-ppf>#KZ6U2hjQ4M-B&rGbKKbTtYI%5o7v~N<EJQ^HaiVDr;k`P5Yeqlyh!{*(F^PsbhZPjC-X1aYgkU%KzSupwE0unN%@InTnAx}GU+EHGiB6=}|@{Sn+
JO(X1l`X%y4H3IARB%VS?=+6>^byh3_&()<gk0in?D$C9sRn1}s}Pb-aSa8SLVnOmR#hJOeK2f{8MrG*4Cjot6Ml^PTKR0f$I8(IUB~<Xv=7h!GL39I4alW%
6u?V-^3s@&Zk$NRA#^|mlxP$eCu$;g6ce}A_%*{Ux9QfCGzqbqa3y=k!c$``XB`_(#$aV2UI4szE>r-|-2OKnNOx-${@cenn*E4jM4n@cy~$<yMh(Txz!Zzm
A;B`UbPP66&9PQPM+PjOB6RYRg~xwLMNn?ru|G<dZ%~JUr0`s^1*kCRykmc_jx;63brvc*{w*vk73%lg=I-kkd!S4%foQ<gWJna47->#`F5U<tF^0M#VUXoS
bUGcdQ8n)?K)6=u8r&Ht7@8pg*CS2$%0mee$luYjb$*@Ks#sBZFh$Z*bY`W+qs=9UAzM<=JD5?+`ZIW6)EziR92qV&%P#5^AmLAfOS$$q3K5F64x22*UW-8t
EXGT#coQ+&$5}1+Hg=1UlfadOC`9>PqFj#TFpagd!tX^WctYuE7XlU$V2Dwko3{jb;m5vM{o&<ug+3#nz!N+C@=W)DD=fJuCNqXsOfkOAs;S>iwc#tZ<SXid
NmF;ikQboP^kWJdt>*V*Ngl?(H*+ym<Qvz@s0I*3;vNI)K?m;=5rPYQF(1nAQVkGTi}Ff`x{(_KKk;+5Z{Og>V7PeqyE63!oZm%#D2hZ%SVPa?Uk_-*XWIj}
BkDL@z>I}uhr1Kf<y97t2Ne!i#FO!H4k{&_N?Jn0R`xO)|Hx#wsB+P~iqST%sT1&SfU}3lgr!L_nrEDh?iEOc-a(_wd#Y4?F8|Xis%}fAf~0;Fkr~LFtNPGp
D^p6}$vl}@gAmFIy2J+L{shjgzJX0BG@evLFjG(7u|zk&Q`x)wMXi?*@MpKF<1oLdogo-;JsFBY91q}et-t8TX@@jzrn30VRSqjzrGBvbWTvBq*x>NrySO77
BSO;%gj<gG%~VN3BfjgTmO`##++`+yH81<6;>(2tGKMF^HeXyTue>j6wV!BMn3`IWX(KXU0|_pH5XHyqA>G!X{+f!yu+8nUB_u-)H^wj|+S8M@id|I;A7t}M
kuNU2G^xp-v|kB|!oK`T5VW8cs_&&eG^<WR>T+X<5g%Md_Ce~;L@SovJ|or7<QQv&)TEY^+P(=tqxuJRtZ;#RLp4XBxtr7`!+DU-WODe`l4{Rzxe*?p*3*01
%{3{|A@d5*e;Pce@w6RNswc%_gHH0&{(N`qnKeLGCIlN2#t24JSe@liF999{TdL}5ot|qqfCi98rDmmDe)_V$HJf6#ucAb>1KGo{(Zr_6{CnT$rL?C__DSx;
W!*lx5kT}fa`9BJ!2+?exPFN)tohna0l?hYFcJB%{>Pc@^Dm&yz=*)BK)YdPnow6th+fyMQw<q`I}n^?SR8c}6r?MX$;Mc@M`M*xO8rV-Jht}k|IX-mK^n{t
NQHyuNuUs$cjgUDa71*_bM6Nyc>Ke{C3&0vr<7F4t!gA@iZvD9Dbtl8gqWKgUxe>{ukY4N_*RpzOn(DD)^>=~2GFHBG~+3Jc-7RF)dPmqd<2Y{AI08KovHUQ
Q0C)nNpC<Ko%tdMlx-z4?U%0iKCe7oT69XE?M-fPSGR^60I8Tvny^eyJ>LB1R#R=KbTu{S3?}?=>BwcXnvRm+=?x&8LOle=D(W6FxrCtTElS75-GKa1hSZ1&
&D5KMJPX~naq=HkV`da{-LPA!0fG(C+|a*_EEUm-{kqUTwgpzIJqtUGsvl=SEga{@b*)J3y*bUc3g65;(J^KC1~ClDh7Wz6WsRo-*n#mo)5<3S0IIS>g)_Nm
t7p<#53%;Z8_HAsu>)-}SwK8)VDRo!AL;*P#U3$s3c7AFp@6Ev(ch5E1TQ2K>W(QSE^DV=ff~R$ll5I!kY{*`mKw|nVnmrrW1|d7@@NPAv77T39^4AMo&<Gf
5f!GnEHhXG&e~=Dx)W44%84l7b=<kaUyX-BkMJr9cvaEWc3Ph49I}CT(s{-_Mf|!&0G;)}3m19+HMI_mf>l!rxHk_~kGT+F6{<B*O;krc2mEHpHC7%RU$$a&
ufldoCv6rOwdh5NsH2w}_i>sB$iaNkdJ;*4y{~~aOzv^o*bwz2oTIFONU`Vun<1;=fc^E41YNV7$)_*QhA4ToZ7Ruhb)C-MPJgwQvBs%73IQFaJEje?GJ?^U
!G=}dnqK2NCu8HVffiD}dqJt5&J!4w>DEEI9T304W8+4MHq50V)i2rw{2~{@K%eVJocf-p*8f-<Djk9xU+IQ^1G0%XptsRjk&Miyp8FQwzH%YBUhmsB#a=Wl
PQm3RjMr7T5L#y#axiuyLkz-1hZAfPT<~P@n}&e7#rVdpQrC9#^fNc8b~O*R;8%r@Z*AEV+xWwDvKquODLH>iJ?WivEpsV1<Q3j8VTlW6l4p%X@R|;(XE(E;
?B2+<-ypEm#u4zu7c*ejAs}zuOePz1-)GQO{1%B~lsPt+Ds>vTkM~J^h-S}F8ZqPWVN(N18AV=#BJg9c)QUJJZf+F6qj`zabfNK@5TKxIK9xDH2Y`3SI~e_t
K!Dg|>+5PU+lU@QpD+e2->TnW?bs%x-`=iCV-@MByx%Wh`^x(biz^)dHlGVc_EZu>3iDiv#zcOeI+2+B7<%X1eB~wK2*ABKcTjdAR-shtcsgxQZN8F%&iY}8
+9CvdjHlri;1$X4G<&#5OnYr>T9A-QpZ7ec-|jKKACc*jwu*MoX{$|p5^6WS&ei^OvtZD%Lu@pp^|{!Aw)>p^qoDDvVaQYUKnmI}Eh45v6=^-z$1n8NNfz1h
kFB9FUn`wH7kNvnQgtAq17(iDg&WS+S_g|a1W<3sWfY1~x{ou%*i%VhGwN&bOVi#xR=gUEH8^$)KC^jvWy5dvW;Ge+t8n`siQ*N=Ih0N%!myRG8=x61QOKu#
g$Ef(rlQ$<uUtrO@UI?(+ki!*U8<zgie3I-%M=$3XM|Pui{E2A(U%Z9AvR>_!#vjNT9qW~36I(`+piQWZFN75Sn_wakL}YNBFilw_GXc%xgTx@?+uN=r13$O
uyvjsLI;`=FqMbX>>R~hN_8~YDDobIpqd(7^Glx>N2w5PGONXuX!U*$t#n^>z}pQ|`tDonuQmlEvuEO(^Pjw-owzn=1u<}`D1fT-n@}jFmU#Pwn28mW${NL0
%i*`mAF{fR`_ZVl+2pmTKM>|7PR1fb7dE%dn7P0p8`>2N?kJMy(p)mm<lq&)SbVcLQPy8ge<{?%DfqyuaY2zLh#FG|RjL3E7cc;eQR=CQ8HCO<RU=%-LPqd;
@VN(Dsz>}gnFpx@hr0{+6%omIH{&soCha~(Pl(lG$8{j3;(81-&geGini29>m1z-%Yg8jgs|(G4BXaZCDb$BN#+{WX{Dy?|5y1#X(VJkAY|s65Pz?<#u>nck
E?vH1kOU$0{g>5ap;yBT^y56SZWTER_0d>h`uFnc34)qmc&{--q~sHCVd1BPt4?au=Yeqz3ua^24fe=-@~Xp55^+U4i=7d_KmL;`z|6v1(-F;I=<Br(QsyM*
Iv^-28fKP7Yplv1W|TXk7g7}InvJB$L>zwqP(>cenmVR}ROrIUzVq_2gKR17y*}{^Kef=J@F9??l#!a<47bR-<SC~;dh=vs5VF^@2K^N!VTR6WYBkZiz#Q~V
Ks{%>q&+a{<w|`d+YV_~8MOaul}%L|`w*dyBoe%vXR6Z!MHTRhi^;n-JdNk%X?V_s%S@F0dveQal;Ml#{88PoZwsCw^7eki(rG1K^#rwm%?9un;W1?G-)JG?
CK8lcP9-opZI)?Xd9pI*-IhAi-Vj#ePBjXfleWU7B@x)tUlvW%W~bVw&M{PMWTY2J=2xO^ulkp3Dn~`HAie%GwLXW~?q)aiYC#670l!sQf703WZ>F+)EZ|=x
-SgBU9~0*)wie59rc^Aq^cbHhEwG9rsKb#Wq&?+_owai`P~(mC+>|gAI>cu}&PKD$cGgI<YQrr_&L17`m}Klmva(m$ykaLr?5ZYn3#o5w%GRn@Uy{>z-@t3^
gIFeZSlx$-wXGHIWLmJCL})aQ^BatVF9983oNs<P(ub)`OII}O`b_1!v%wM%*&d5NiLDXV;XMiXNnEW2JoGHXk%}97HJ;<H85J72K5>FjzJAR!DG|yDmlqc7
6iLmdMof*ulKsc+mA@gNs!hhf4m>JYbXo+NWBNtjKCrs*el?GCqfh_<VuPN@y{<6l00HNO0`%+#=i?ravBYQl0ssI200dcD
```

### Complete additional primal-star identity checker

Save this as STAR_IDENTITY.py and run `python -B -S STAR_IDENTITY.py exact-source proofs` after the two star replays. Both terminal identity checks actually completed. This supplies an additional primal-cloud/volume-identity binding; it does not replace A/B.

```python
"""Bind both exact primal-star constructions to their audited convex bodies."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
source,proof=map(Path,sys.argv[1:]);sys.path.insert(0,str(source.resolve()))
import exact57,rational56

def mass(P,faces):
 D=F(0);L=[F(0)]*3
 for cy in faces:
  for k in range(1,len(cy)-1):
   a,b,c=[P[i] for i in [cy[0],cy[k],cy[k+1]]]
   dd=exact57.dot(a,exact57.cross(b,c));assert dd>0
   D+=dd;L=[x+dd*(i+j+k) for x,i,j,k in zip(L,a,b,c)]
 return D/6,[x/24 for x in L]

d,fs=exact57.source();P=exact57.physical(rational56.points(d)[:137],fs);V,M=mass(P,fs)
for name,v,side,lost in [('STAR7',7,1,5),('STAR111',111,0,107)]:
 a=json.loads((proof/('final_'+name)/'A.json').read_bytes())
 b=json.loads((proof/('final_'+name)/'B.json').read_bytes());assert a==b
 raw,r=exact57.star(d,fs,v,side);PP=[p[:] for p in P]
 PP[v]=[x+F(r['t'])*F(y) for x,y in zip(P[v],r['direction'])]
 want={tuple(p) for i,p in enumerate(PP) if i!=lost}
 assert {tuple(map(F,p)) for p in a['raw_vertices']}==want
 for p in PP:assert all(exact57.dot(row[:3],p)<=row[3] for row in raw['H'])
 assert F(a['ordinary_volume'])==V
 assert [F(x)-y for x,y in zip(a['raw_first_moments'],M)]==list(map(F,r['first_moment_change']))
 print('EXACT_HULL_EQUALS_PRIMAL_STAR_AND_VOLUME_MOMENT_IDENTITY_PASS',name,flush=True)
```
