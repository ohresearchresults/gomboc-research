# figure-0383

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Atlas 56 — exact coupled-star bodies, a filled-mass path obstruction, and a one-edge relay restoration

## 1. Result

**No own110/weak000 body with E≤310 was obtained. Five finite rational nonwinners were constructed, completely audited, and recovered from sources alone.** The strongest structural result is a completed exact obstruction for an entire coupled-star parameter box, followed by a genuine incidence change that escapes its path-length hypothesis.

The useful finite comparison is **PAIR → RELAY7**: V/E/F changes **175/308/135 → 176/309/135**. One additional physical vertex and one true edge restore a cap route from six to seven links, without adding a maximal facet. **173 common physical points are exactly unchanged.** This is not yet a positive mechanical chamber: RELAY7 has strict(61,61,120), and its three relay vertices are all strict unstable vertices at the actual filled centroid.

| Replay case | Actual V/E/F | C | Full strict(S,U,H) | Weak-only |
|---|---|---:|---|---|
| PAIR |175/308/135|616|(3,2,3)|(0,0,0)|
| COMP111 |176/310/136|620|(4,2,4)|(0,0,0)|
| COMP7 |176/310/136|620|(6,1,5)|(0,0,0)|
| RELEASED_CAP_PROPOSAL |177/311/136|622|(61,62,121)|(0,0,0)|
| **RELAY7** |**176/309/135**|**618**|**(61,61,120)**|**(0,0,0)**|

The first four definitions are the formerly unexecuted proposals in the assigned joint-star parent. Their status is now **observed exact nonwinner**, not merely an invocation. The legacy filename RELEASED_CAP_PROPOSAL is retained as a replay identifier; it does not mean its present census is still numerical. RELAY7 is the new coupled cap/star construction.

The accepted benchmark remains the distinct **VQ20_C622_ROUTE88_118_G12**,176/311/137,own110/weak000. None of the five nonwinners replaces it. The coordinate parent here is **literal S8=COORD_CAP_RL_C624_STRONG_G8**, not S8_D2, C622_ROUTED, or a C626 body. The journal records this distinction and the earlier unexecuted status of the proposals. 

## 2. Parent authority and exact definition

The two assignment identities are preserved:

```text
figure-0376
4fa37ad9657e096f7b83446ab9eed072bf3322c9cf997340b813ffad34bb1d6d
figure-0368
e0df11674e3a73f23bd5f91802800b15773bf62057b91d4a653033c411d41b92
```

These are the supplied immutable-result tags, not hashes invented for a different rendered wrapper. The actual extracted source bytes were checked. The unchanged COUPLED_STAR_METHOD.py has18103 bytes/SHA `810f50e1b94e3a9400c7383996ee332114fae635caedb9cf9f293248681a7e94`. The entire26-file coordinate-parent capsule and manifest matched their literal41775-character/112244-byte identities before extracting the smaller dependency closure below. No coordinate-definition or incidence conflict was found.

**PARENT_S8.json:**9599 bytes, SHA `bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2`. Its ordered rational contact solves reconstruct137 physical supports. The full literal FACES_S8.json supplies original physical labels; the loader independently reconstructs those points from support triples, checks every prescribed and off-incidence inequality, and verifies their Cartesian lexicographic order.

Every new body is the convex hull of the explicitly generated physical cloud, equivalently its independently audited bounded H intersection. Density is **constant1 throughout the entire convex volume**. With outward maximal-facet fan triangles(a,b,c), all exact mass data and centred coordinates are defined by

```text
D6 = sum det(a,b,c)
L  = sum det(a,b,c)*(a+b+c)
V  = D6/6
M  = L/24
g  = L/(4*D6)
final vertex = raw vertex - g.
```

The complete reduced fractions, raw vertices, maximal polygons, true edges, own centroid and signs are emitted by both auditors. The literal inputs plus the finite reconstruction code below define them completely; a vertex-average or independently selected centre is never substituted.

## 3. Actual coupled surgeries and moments

All labels in the construction formulas are **original S8 physical labels**, unless explicitly marked final raw lexicographic.

For an eligible degree-three vertex i with two triangular facets, let a_i,b_i be its two neighbours on its nontriangular facet and c_i its third neighbour. Define

```text
d_i=p_b_i-p_a_i,
p_i(t_i)=p_i+t_i d_i,
w_i=Vol(conv(p_c_i,p_a_i,p_i,p_b_i)),
K_i=(w_i/4)d_i.
```

The code derives the exact isolated interval by all fixed-plane and rotating-triangle inequalities. For nonadjacent selected physical vertices, the full boundary determinant expansion has no mixed terms. Actual simultaneous convexity is checked separately, and the audited filled moments are then bound to the polynomial.

**PAIR:** put original7 at its upper interval endpoint and original111 at its lower endpoint. Thus d7=p5-p11 and d111=p114-p107. Original5 and107 become non-extreme. Original supports4/10 and135/136 coalesce. The actual result is C616/323, with final S=[3,5,89], U=[94,106], H=[[5,94],[29,58],[106,112]]. Its two unstable input labels are original95 and moved original111. The remote saddle has original endpoints30/59, and stable output89 corresponds to unchanged original support90. The simultaneous body is not classified by simply adding isolated equilibrium counts.

**COMP111:** use the same original111 lower endpoint and solve exactly

```text
[K0 K16 K74]s = -K111*t111.
```

The four moving vertices are nonadjacent. The actual convex body has C620/424; final S=[3,24,31,64], U=[95,107], H=[[1,95],[16,95],[68,95],[107,113]]. Final unstable107 is moved original111, **not deleted original107**.

**COMP7:** use original7 at its upper endpoint and solve

```text
[K0 K21 K87]s = -K7*t7.
```

The actual body has C620/615; final S=[3,5,18,19,30,31], U=[94], H=[[1,94],[5,94],[16,94],[22,94],[86,94]]. Final unstable94 is original95.

For all three, the actual audited volume equals S8 exactly. For COMP111 and COMP7, **all three actual first moments also equal S8 exactly**, hence so does the own centroid. This is completed finite rational compensation, but it creates additional mechanical defects rather than producing110. No density weights or external masses are used.

Display orientation only:

```text
S8 volume = 0.48895509175448054
S8 centroid ≈ (-0.01253368153516639,
                 0.006279838457084985,
                -0.008889105819019614).
```

## 4. Completed exact obstruction, including the actual centroid and all exterior ports

The literal25 eligible vertices are

```text
0,2,5,7,8,16,21,36,51,61,74,83,87,91,93,96,98,102,103,
105,107,111,113,122,139.
```

The entire joint polynomial was computed exactly: **13 volume monomials and62 monomials in each first-moment component**. The nonzero interacting pairs are precisely

```text
(0,2),(5,7),(8,16),(51,61),(87,91),(91,93),
(93,96),(96,98),(98,102),(102,105),(103,107),(107,111).
```

There is no original triangle with three selected vertices. Thus the volume is quadratic and first moments cubic; the adjacent-star terms were retained. The source reconstructs every coefficient, rather than assuming isolated additivity for adjacent stars.

Over the **full product of the25 individually derived intervals**, exact coefficient bounds give V>611/1250 and the following coordinate bounds for the actual own-centroid displacement whenever the moved boundary or its coarsening is the actual convex hull:

```text
|g_x-g0_x| < 87039635/10^12
|g_y-g0_y| < 55645202/10^12
|g_z-g0_z| < 34613471/10^12.
```

Consequently rho=9/100000 is a valid enclosing infinity radius. This is an over-approximation of the admissible simultaneous geometry: **isolated intervals alone are not claimed to prove simultaneous convexity**. The centroid bound comes from M(t)-g0 V(t), divided by a positive lower bound for V(t).

### First interface

Take entry100, exit117 and original internal vertices103,107,111,114. The complete exterior port set, checked against the original true-edge graph, is **{69,97,117}**. Throughout the certified centroid cube, ports69 and97 have strictly smaller squared radius than entry100, with rational lower reserves respectively23911826855/10^12 and894710065/10^12.

For any strict ascent path of n links from a to b,

```text
n*(|b-g|²-|a-g|²) > |b-a|².
```

This follows by summing the exact radial-increase identity and applying Cauchy–Schwarz to its edge vectors. For a=100,b=117,n=4, exact arithmetic gives

```text
|b-a|²-4*(|b-g0|²-|a-g0|²)-8*rho*|b-a|_1
    > 4435181230/10^12 > 0.
```

Therefore four ascent links are impossible. Merely changing the centroid while keeping these two endpoints fixed would require an infinity displacement **greater than2896037844/10^12≈0.002896037844**, whereas the entire coupled-star box is confined below0.00009.

The apex old95 remains strictly unstable throughout this box:201 extreme-position tests cover every other moving or fixed physical point, all centroid corners being bounded analytically. The minimum negative escape reserve exceeds38264421960/10^12.

It follows that a valid coarsening with **at most three internal vertices**, the same fixed entry/exit and the same complete exterior ports cannot be own110/weak000. If every vertex except the apex had a positive outgoing true edge, entry100 would have a simple positive path leaving this region. It cannot leave through either lower-radius port, and reaching117 would use at most four links, a contradiction. This argument allows arbitrary internal reconnection; it does not freeze the identity of the extra unstable vertex.

The actual PAIR and COMP111 hulls were independently checked to have exactly this coarsened region and these ports. The obstruction therefore applies to their allowed fixed-interface continuation, not merely to an imagined graph.

### Extended interface

Extending the region through117 and120 gives fixed exit124 and complete exterior ports **{69,97,106,124}**. With at most five internal vertices, six links are insufficient: the analogous uniform energy reserve exceeds5802784784/10^12. All three alternative ports remain lower-radius; the reserve for106 exceeds158712983124/10^12. A centroid-only escape from this six-link gate requires displacement greater than1806704783/10^12≈0.001806704783.

This gives a conditional obstruction even to releasing117/120 internally while retaining the outer interface, the apex and the certified own-centroid region. For a geometry outside the original star family, the actual-centroid hypothesis must be proved separately. **The seven-parameter three-relay cap has six internal vertices and is not excluded by this extended gate.** Neither gate excludes new exterior ports, more relay vertices, moved outer endpoints, a changed metric, or leaving the certified centroid region. This is a separate S8 result, not a transfer of the journal's K99 obstruction.

Observed certificate:2372 bytes, SHA `351234028e5135c836d9c17f8539ae6f9dfdf070fe8c7fe036891684366a0146`; terminal `ATLAS59_EXACT_JOINT_STAR_FIXED_INTERFACE_GATE_PASS`.

## 5. Actual relay geometry beyond the path-length hypothesis

The exact cap uses the parent's complete seven-control construction, evaluated here at

```text
(s,t,tx,ty,alpha,beta,gamma)=(0,0,0,0,8/15,10/21,3/250).
```

Put T=q135∩q73∩q71. At these zero interface-displacement parameters, A=p103 and B=p117. Define

```text
L=T+(8/15)(A-T),
R=T+(10/21)(B-T),
D=T+(3/250)(p69-T).
```

Support17 is replaced by the plane through L,R,D; support136 is omitted. The proposed physical cloud omits original107,111,114 and inserts L,R,D. Exact support/hull verification proves the actual177/311/136 body, with full own class(61,62,121), not just a nominal truncation f-vector.

**RELAY7** additionally executes the separated original7 upper-endpoint surgery, with the same exact t7 and local tetrahedron as before. Original5 loses extremality and supports4/10 coalesce. Both full independent audits bind this body to precisely the proposed cloud minus original5. Its actual volume equals the three-relay cap's volume, and

```text
M_RELAY7-M_CAP = K7*t7
```

holds exactly for the independently integrated filled moments. This is not an assumed addition of separate receipts. Both cap bodies have V≈0.4889599289649484, **not** the original S8 volume. RELAY7's actual g≈(-0.012533348680854562,0.006284653634975234,-0.008892951651192962).

The independently checked finite route comparison is

```text
PAIR:   100→103→111→114→117→120→124       (6 true edges)
RELAY7: 100→103→L→D→R→117→120→124         (7 true edges).
```

The exact own-centred escape-sign sequences are respectively

```text
PAIR:   +,+,-,+,+,+
RELAY7: +,+,-,-,-,+,+.
```

Thus the extra path vertex is geometrically real and costs only one true edge, but the chosen relay shape has three failed ascent links. This is a usable incidence-surgery mechanism, **not** evidence that the endpoint is near110. The173 common physical coordinates agree exactly and delta(V,E,F)=(1,1,0). The complete additional route checker is supplied below; its executed terminal is `ATLAS59_ONE_EDGE_RELAY_RESTORATION_EXACT_GRAPH_PASS`.

## 6. Exhaustive audits, arithmetic cost, and cold recovery

Every retained endpoint completed **two genuinely independently implemented full exact auditors**, one enumerating feasible support triples and the other clipping all support-pair lines. They separately reconstruct the bounded hull, maximal facets, true edges, filled moments and own-centred equilibria. Entire normalized A/B records agree. Each audit includes every complete vertex cone, every facet foot against all true polygon sides, and four primitives on every true edge. Weak-only lists and all face/vertex-maximum/edge primitive-zero counters are empty or zero.

An additional proof binds H to the physical cloud in both directions: every exact audited vertex belongs to that cloud, and every cloud point satisfies every H inequality. For the star bodies the audited mass is also checked against the complete joint polynomial; for RELAY7 the cap-plus-star first-moment identity is checked separately. Third centred-integer integrations use346 tetrahedra for PAIR,348 for COMP111/COMP7/RELAY7, and350 for the cap; all determinants are positive and all three centred first moments are exactly zero. Triangulation diagonals are not counted as true edges.

| Case | Primitive H maximum bits | Raw-coordinate bits | Own-centroid bits | Centred-coordinate bits | Common centred denominator bits |
|---|---:|---:|---:|---:|---:|
| PAIR |382|440|44872|44876|44926|
| COMP111 |1544|1473|44715|45645|46149|
| COMP7 |1382|1314|44715|45594|46084|
| Cap |458|440|44420|44424|44477|
| RELAY7 |458|440|44483|44487|44540|

These are final reduced fractions, not input-grid sizes. Exact compensation preserves the centroid but substantially increases local H/raw arithmetic. The full numerator/denominator, volume and first-moment costs are in the reproduced receipts.

Full-record identities:

```text
PAIR          A=B249243 bytes 682581d3c213a4ee3d3462a04938cc73c2e4af86efd6f61ff3ff1568e56ba80f
COMP111       A=B265460 bytes fe0e6dc307a33c9c2efda2aa18b65e599f382e9011f96dd1ca6ae8b91fadbf9c
COMP7         A=B263444 bytes 4a0717d71f9dc9e67ece71483e2bbc5e87fa81b9c2ad1e5f16da59a5fdd7859e
Cap           A=B249655 bytes b1a88ef6c92aea2a5b441634c96c1c168c8602f9d31a842e7647c8bc7a85e460
RELAY7        A=B250075 bytes 6145b0fdf68968322c6e60f928be159b4d3c14eba111bb284a334796cda83ba8
```

All five were executed again from a **fresh directory containing only the decoded final sources**, with no precomputed halfspaces, vertices or audit outputs. The final comparison found all43 expected output files present and byte-identical. Nonvacuous controls—tetrahedron446/weak000 and prism446/weak123—passed both auditors and were rejected as winners. Source-manifest checks completed before and after the executions.

Actually observed final aggregate marker:

```text
ATLAS59_FIVE_NONWINNERS_AND_SCOPED_CAP_GATES_COLD_SOURCE_ONLY_PASS 43
```

No new floating optimization, completed search of the whole released-interface family, or positive body is claimed. Earlier interrupted speculative searches are not being counted as results. The next useful geometric seed is the actual RELAY7 stratum with E309 and one remaining edge of headroom, but its relay and remote mechanical defects must be solved together at its actual filled centroid. Repeating centroid compensation inside the excluded short-route star family cannot do so. No global exclusion, minimality, continuous no-birth path, C<32 search, or resolution of the pending nine/nine original-proof gate is asserted.

## 7. Entire self-contained recovery

The **14-file core capsule** contains the complete unchanged joint-star method, literal S8 generator and face complex, both auditors, third mass, new cap certificate, RELAY7 generator/binder, replay drivers, all43 expected output identities, provenance and source manifests. Only the five actually required unchanged coordinate-parent files are retained; their subset manifest is explicitly regenerated. The original26-file parent was verified before extraction. No omitted parent helper or optimizer is needed.

Normalized base85: **27630 ASCII characters**, SHA `3ab1c64e8064561e0ed59616a526ec0b2927fe84b6171e0e3bc72a71ce8b635b`.
Decoded UTF-8 JSON source map: **71668 bytes**, SHA `69c30bcd04ff3212d907c670cbbf997a2f432121fa6cd0f7d3d1070b553344cf`.

Save the complete text payload below as CAPSULE.b85 and the following decoder as RESTORE59.py:

```python
import base64,hashlib,json,lzma,sys
from pathlib import Path
s=''.join(Path(sys.argv[1]).read_text(encoding='ascii').split())
assert len(s)==27630
assert hashlib.sha256(s.encode()).hexdigest()=='3ab1c64e8064561e0ed59616a526ec0b2927fe84b6171e0e3bc72a71ce8b635b'
b=lzma.decompress(base64.b85decode(s))
assert len(b)==71668
assert hashlib.sha256(b).hexdigest()=='69c30bcd04ff3212d907c670cbbf997a2f432121fa6cd0f7d3d1070b553344cf'
f=json.loads(b);assert len(f)==14
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
 r=Path(name);assert not r.is_absolute() and '..' not in r.parts
 p=out/r;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
for name,w in json.loads((out/'SOURCE_MANIFEST.json').read_bytes()).items():
 data=(out/name).read_bytes()
 assert len(data)==w['bytes'] and hashlib.sha256(data).hexdigest()==w['sha256']
print('ATLAS59_FOURTEEN_LITERAL_SOURCES_RESTORED')
```

Exact commands, tested with **CPython3.13.5, standard library only**, assertions enabled. Do not use-O. The source and proof directories must initially be absent:

```sh
python -B -S RESTORE59.py CAPSULE.b85 source59
python -B -S source59/REPLAY59.py --out proof59 --stage BUILD
for case in PAIR COMP111 COMP7 RELEASED_CAP_PROPOSAL; do
  for stage in A B MASS FINISH; do
    python -B -S source59/REPLAY59.py --out proof59 --case "$case" --stage "$stage"
  done
done
python -B -S source59/REPLAY59.py --out proof59 --stage CERT
python -B -S source59/REPLAY59.py --out proof59 --stage FIXTURES
python -B -S source59/RELAY7.py --source source59 --base-proof proof59 --out proof59/RELAY7
python -B -S source59/CHECK_ALL59.py proof59
```

The case outputs include full A.json/B.json, exact physical clouds and defining parameters, BINDING.json, MASS.json and RECEIPT.json. EXPECTED.json supplies every required filename, byte length and hash, including large exact moments. The formal polynomial and interval data are rebuilt, not loaded from an unavailable scratch file.

### Complete additional route checker

Save as ROUTE_BIND59.py and execute `python -B -S ROUTE_BIND59.py proof59` after the commands above. Its2020 bytes have SHA `c42f83e44c7ee0ec1abafd38047b554b1164221a6e66130853d91c3072fb109e`. The observed561-byte output has SHA `aa88c427b994ece4d5847e33eb563cc84d0c45881439772630861f39cc667dbf`.

```python
"""Exact finite graph/coordinate comparison: restore one cap relay at one-edge cost."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
sys.set_int_max_str_digits(0)
root=Path(sys.argv[1]);records={};maps={}
for name,sha,key in [
 ('PAIR','682581d3c213a4ee3d3462a04938cc73c2e4af86efd6f61ff3ff1568e56ba80f','input_label_to_final_raw_lex'),
 ('RELAY7','6145b0fdf68968322c6e60f928be159b4d3c14eba111bb284a334796cda83ba8','old_and_new_label_to_final_raw_lex')]:
 p=root/name;ab=(p/'A.json').read_bytes()
 assert ab==(p/'B.json').read_bytes() and hashlib.sha256(ab).hexdigest()==sha
 records[name]=json.loads(ab);maps[name]=json.loads((p/'BINDING.json').read_bytes())[key]
common=[k for k in maps['PAIR'] if maps['PAIR'][k] is not None and maps['RELAY7'].get(k) is not None]
assert len(common)==173
for k in common:
 assert records['PAIR']['raw_vertices'][maps['PAIR'][k]]==records['RELAY7']['raw_vertices'][maps['RELAY7'][k]]
result={}
for name,labels in [('PAIR',[100,103,111,114,117,120,124]),('RELAY7',[100,103,'L','D','R',117,120,124])]:
 a=records[name];mp=maps[name];path=[mp[str(i)] for i in labels];edges=set(map(tuple,a['edges']))
 assert all(tuple(sorted((i,j))) in edges for i,j in zip(path,path[1:]))
 P=[list(map(F,p)) for p in a['raw_vertices']];g=list(map(F,a['raw_centroid']));signs=[]
 for i,j in zip(path,path[1:]):
  v=sum((x-c)*(y-x) for x,y,c in zip(P[i],P[j],g));signs.append((v>0)-(v<0))
 result[name]={'original_or_relay_labels':labels,'raw_lex_route':path,'true_edge_count':len(path)-1,'actual_own_centred_escape_signs':signs}
a,b=records['PAIR'],records['RELAY7']
assert [b[k]-a[k] for k in ['V','E','F']]==[1,1,0]
assert all(maps['RELAY7'][k] in b['unstable_vertices'] for k in ['L','D','R'])
result.update({'unchanged_common_physical_points':173,'delta_V_E_F':[1,1,0],
 'relay_vertices_all_strict_unstable_at_this_endpoint':True,
 'terminal':'ATLAS59_ONE_EDGE_RELAY_RESTORATION_EXACT_GRAPH_PASS'})
print(json.dumps(result,sort_keys=True,separators=(',',':')))
```

Convenience copies, not substitutes for the literal recovery below: source-only archive (`ATLAS59_SOURCE_ONLY.zip`),54377 bytes/SHA `f9a0f45d34c7ae6c7f4fd145da851775deb673718e5d3655e5863dadc3cc4c00`; full completed proofs and logs (`ATLAS59_VERIFIED_FULL.zip`),1657709 bytes/SHA `5a7ada69804b76e6dccfcca9dd11b5e310371c5565b479b0a916b8596134998c`. Both archives were read back byte-for-byte. The source archive contains the14 core files plus the decoder, payload and additional route checker.

Additional copies: complete Markdown handoff (`ATLAS59_RESULT.md`) and v2 JSON handoff (`ATLAS59_RESULT_v2.json`).

### Literal core payload


[Encoded source block omitted; the code in this passage is incomplete.]
