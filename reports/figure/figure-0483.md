# figure-0483

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# SC83 — complete C180 affine exclusion, exact Q-packet removal, and a C176 material chart

## Outcome

**The full-SPD uncertainty for the literal `SC83_BF35_ONECAP_C180_AFFINE222` shape is resolved negatively.** No positive-definite Gram matrix gives that exact uniformly filled geometry one strict unstable vertex and zero additional weak unstable vertices. Consequently, its entire nonsingular affine orbit contains no own-centred strict110/additionalweak000 body. This is a new exact certificate on the C180 parent, not a transfer of any C198 corridor exclusion.

No new strict110 body is claimed. I also established that the complete remaining **10-vertex/16-cut polar packet is one-cap separable**, and implemented its removal as an actual physical vertex insertion. The resulting durable, nonsimple material nonwinner is `SC83_C176_QPACKET10_INSERT_P14_1_M4_D10`: **V52/E88/F38, C176, strict(11,2,11), additionalweak000, primitivezero000.**

Its new vertex is 16-valent. It has a certified three-dimensional point-position box and complete exact finite-volume/first-moment polynomials on the visibility cell. Its mechanically fragmented polar landscape is preserved in full; it is not called stable-basin cancellation or an improved equilibrium-class endpoint.

## 1. Source authority and checks actually executed

I read the complete supplied journal, including its literal parent payload and decoder, and decoded/read the entire standalone source before research. The mounted journal is 177154 bytes, 1007 physical text lines, SHA-256 `a388ed17d3064a7b61255c2f2e64a0ae94fa7cf6a5158618b2b87122a382cae5`.

The required parent is `figure-0481`, advertised immutable SHA-256 `7b61883c3932f89c25f224d4d392259488c1cf0673b4bc72c39941bdbd9d3b9d`. The parent supplies the exact affine frame, strict222 census and complete P29/25 and Q10/16 interfaces.

There is a **transport-hash limitation, not a geometry substitution**: the Markdown span extracted from its heading through mounted EOF has 21522 bytes and SHA-256 `3396598c6c442eab51bdf36b5f1b021342ce967906ece14373cb00ed6e25954c`, which does not reproduce the advertised outer-result hash. I do not infer the unavailable original serialization. The embedded source independently decodes to exactly **17276 bytes**, SHA-256 `033968bb2c49df312a8d92cc89d3a2e015404b329529761fe824f77ec34aabe7`; fresh execution reproduces **all six parent input/audit receipts byte-for-byte**, including the C180 affine input and full audit. Those source and receipt identities are explicitly provided by the literal payload. No coordinate, incidence, centroid or index conflict was found. No missing additional source is needed for the findings below.

I then performed a second fresh replay from the new **source-only capsule**, in a new directory. It reconstructed all parent objects, checked the new global exclusion, rebuilt the new C176 body's actual mass/mechanics/landscapes, and matched all ten expected output hashes.

## 2. Exact theorem: every SPD metric on this C180 shape is excluded from weak-free U1

### Statement and scope

Let K be the literal affine C180 body, c its exact uniform-volume centroid, and G any real symmetric positive-definite 3 by 3 matrix. On K-c, measured using the quadratic metric G, it is impossible to have exactly one strict unstable vertex and no additional weak unstable vertices.

This excludes **all five projective metric degrees of freedom**, all condition numbers, off-diagonal directions and disconnected metric cells. It is not a diagonal-family result, a connected-component statement, or a bounded numerical search. No explicit distance from the singular PSD boundary is needed.

The theorem fixes the exact raw geometry and its actual uniform mass. It does **not** exclude different realizations of the same combinatorial graph, support/vertex changes, projective material changes, or the new C176 geometry below.

### Reduction to positive escape choices

For a true directed edge i to j, write a_i=x_i-c and

`D_ij(G) = a_i^T G (x_j-x_i)`.

At a nonroot vertex in a strict-U1/weak-U0 configuration, at least one outgoing true-edge score is strictly positive. Choose one such edge at every nonroot. Positivity implies

`|a_j|_G^2 - |a_i|_G^2 = 2 D_ij(G) + |x_j-x_i|_G^2 > 0`.

Thus the selected graph has no directed cycle and terminates at the unique root. Conversely, an actual weak-free U1 realization supplies exactly such a root-labelled positive-parent selection. The C180 graph is trivalent, so the finite necessary systems have 60 root choices and three possible parents at each of the other 59 vertices. The proof covers these systems implicitly; it does not claim to have explicitly enumerated `60*3^59` assignments or counted the graph's spanning trees.

### Exact integer arrow matrices

The parent reconstructor supplies homogeneous raw vertices `(p_i,d_i)`, with positive d_i, and the actual centroid `c=C/D`. Define

`Y_i = D*p_i - d_i*C`,

`E_ij = d_i*p_j - d_j*p_i`,

`T_ij = Y_i E_ij^T + E_ij Y_i^T`.

Then

`D_ij(G) = tr(G T_ij)/(2 D d_i^2 d_j)`.

Every denominator is positive. Let b_e be the maximum absolute-entry bit length of T_e, and let `B=max b_e=4122`. The certificate uses integer matrices

`Z_e = 2^(B-b_e) T_e`.

This is a positive row scaling, not a rounded centroid or approximate metric predicate.

For each blocker, the supplied positive integer weights w_e satisfy

`sum_e w_e Z_e` **negative definite**.

All three signed leading-principal-minor conditions are checked with exact integers: first minor negative, second positive, determinant negative. If every selected escape in that blocker were positive for SPD G, the weighted trace would be positive; negative definiteness makes it strictly negative. This is an exact contradiction.

### Complete finite cover and independent discrete replay

The final reduced bank contains **677 negative-definite blockers: 649 triples, 24 quadruples and four quintuples**. Every blocker is unconditional; the final proof needs no auxiliary farthest-root inequalities or numerical dual feasibility assumptions.

The bank also contains **139 explicitly checked simple directed cycles**. The checker adds the **90 automatic reverse-edge pair clauses**. Each nonroot has exactly one selected parent; a root has none.

A complete standard-library integer/bitset domain search rejects every root. Observed deterministic totals are:

`60 roots; 813749 recursive nodes; 406945 conflicts; 3788147 forced-choice removals.`

These are **search-tree/domain-check counts**, not counts of distinct physical metric cells or spanning trees. The code performs exhaustive branching on every surviving parent option, exact unit propagation of the forbidden selections, and memoization only of already proved impossible domains. Removing all metric blockers leaves a satisfiable root-0 combinatorial control, which is checked during replay.

The final exact checker uses **neither an SDP solver nor Z3 nor SciPy**. Numerical linear-programming/eigenvector cuts were used only to nominate positive integer blocker weights; a finite weighted-triple bank and symbolic clause learning supplied candidates. SciPy's optimization interface was the numerical front end, not the proof authority. The capsule includes complete reusable cone and finite-grid nominators, with their settings and observed dependency versions. It does not rely on reproducing discarded SAT models or their trial order.

**Scientific consequence:** changing only the affine metric on this C180 parent cannot finish the assignment. Geometry really must change. Rational affine reparameterization cannot reopen this closed orbit.

## 3. The complete Q10/16 packet is exactly one-cap removable

All indices here are the parent's affine-frame indices. Its unwanted polar packet is

`X=[1,2,3,4,5,15,16,17,18,30]`.

Construct its polar about the actual physical centroid, without independently filling or recentering that polar:

`q_f = n_f/(h_f-n_f.c)`.

The small integer separator is

`n=(2,0,-1), n.q <= 2`.

The retained-complement maximum is attained at polar vertex14 and lies in

`[1339673617424,1339673617425)/10^12`.

The packet minimum is attained at polar vertex1 and lies in

`[2299618816330,2299618816331)/10^12`.

Thus the offset2 strictly retains all 22 complementary polar vertices and rejects all ten packet vertices. The verifier computes the complete underlying rational numbers, rather than trusting these decimal brackets.

Under same-centre polarity this particular cut is the physical insertion `p*=c+(1,0,-1/2)`. To avoid importing the parent's large centroid denominator into the added point, I instead froze the nearby **raw affine-frame** point

`p0=(7/5,1/10,-2/5)`.

This is a different point, not an alias for p*. Exact evaluation against every old maximal plane proves that it sees **exactly the same ten faces X**. The constructed uniformly filled body is

`K_new = conv(K, p0)`.

All subsequent mass and both landscapes are rebuilt for K_new. Its final polar uses the **new actual physical centroid**, not the old separator centre.

### Actual complexity and contact turnover

The visible polar packet has 18 internal edges and 16 boundary edges. The one-cap transformation gives `E'=90-18+16=88`. Direct exhaustive hull reconstruction confirms the dual physical counts **52/88/38, C176**.

Exactly these nine old physical vertices disappear:

`[22,39,42,43,44,47,48,52,53]`.

The new point is lexicographic vertex43. The degree histogram is **44 trivalent vertices, seven 4-valent vertices and one 16-valent vertex**. Thus its nonsimple excess is20, and the independent count identity is `3*38-6-20=88`. The face-size histogram is `18x3, 7x4, 6x5, 5x6, 1x13, 1x21`. It leaves **161 final-edge units** under E<=249; this is combinatorial headroom, not an existence promise.

## 4. Exact material audit and complete surviving interfaces

The new body's full audit gives:

`strict(S,U,H)=(11,2,11); additionalweak=(0,0,0); primitivezero=(0,0,0)`.

`S=[0,1,3,6,9,14,22,23,26,27,31]`, `U=[2,51]`.

`H=[[2,49],[6,50],[10,48],[17,43],[17,46],[18,43],[19,43],[34,43],[36,47],[37,40],[39,41]]`.

The two unstable vertices are the **unchanged geometric old roots2 and59**, now indexed2 and51. Removing the entire old polar packet did not remove the physical packet.

Actual uniform volume is approximately `0.9089055210288105`; the actual raw centroid is approximately `(0.5249315236754802,0.11092949171328152,0.06377545890591174)`. The common centred-coordinate denominator has3441 bits. The complete exact volume, first moment, centroid, vertices and all maximal planes are generated by the capsule; none is replaced by the displayed approximations.

Using the parent's exact TP/TQ definitions:

`TP in [2345695445726,2345695445727)/10^12`,

`TQ in [3276348490237,3276348490238)/10^12`.

There is **one P bar, with a36/26 packet, and ten Q bars**. This is real geometry/contact turnover with a smaller C, but the stable landscape fragments rather than disappears. The following topology data are complete, in the new body's lexicographic vertex/active-face indexing. Exact birth/death levels, depths and all other audit fields are regenerated by `full(rows)` in the capsule.

```json
{"P":{"roots":[2,51],"bars":[{"peak":2,"elder":51,"death_edge":[37,40],"component":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,36,37],"boundary":[[0,45],[1,29],[2,49],[6,50],[8,38],[10,48],[13,39],[13,41],[14,29],[14,42],[17,43],[17,46],[18,43],[19,43],[20,43],[21,43],[28,43],[30,43],[32,35],[32,43],[33,38],[34,35],[34,43],[36,47],[37,40],[37,43]],"path":[2,0,1,3,4,5,7,9,11,15,19,20,37,40,51]}]},"Q":{"roots":[0,1,3,6,9,14,22,23,26,27,31],"bars":[{"peak":6,"elder":14,"death_edge":[6,14],"component":[6],"boundary":[[6,0],[6,3],[6,14],[6,21],[6,37]],"path":[6,14]},{"peak":0,"elder":14,"death_edge":[0,6],"component":[0],"boundary":[[0,6],[0,9],[0,21],[0,36]],"path":[0,6,14]},{"peak":9,"elder":23,"death_edge":[9,23],"component":[9],"boundary":[[9,0],[9,21],[9,23],[9,35]],"path":[9,23]},{"peak":23,"elder":14,"death_edge":[0,9],"component":[9,23],"boundary":[[9,0],[9,21],[9,35],[23,22],[23,35]],"path":[23,9,0,6,14]},{"peak":27,"elder":26,"death_edge":[25,26],"component":[25,27],"boundary":[[25,7],[25,26],[27,13],[27,33]],"path":[27,25,26]},{"peak":26,"elder":31,"death_edge":[26,32],"component":[25,26,27],"boundary":[[25,7],[26,21],[26,32],[27,13],[27,33]],"path":[26,32,31]},{"peak":1,"elder":14,"death_edge":[1,18],"component":[1],"boundary":[[1,2],[1,3],[1,4],[1,5],[1,8],[1,10],[1,11],[1,13],[1,14],[1,17],[1,18],[1,19],[1,20]],"path":[1,18,8,2,4,14]},{"peak":22,"elder":31,"death_edge":[22,24],"component":[22],"boundary":[[22,21],[22,23],[22,24]],"path":[22,24,21,31]},{"peak":31,"elder":14,"death_edge":[22,23],"component":[21,22,24,25,26,27,28,29,30,31,32,33],"boundary":[[21,0],[21,4],[21,5],[21,6],[21,7],[21,8],[21,9],[21,11],[21,12],[21,14],[21,15],[21,16],[21,19],[22,23],[25,7],[27,13],[33,3],[33,34]],"path":[31,21,24,22,23,9,0,6,14]},{"peak":3,"elder":14,"death_edge":[1,3],"component":[3],"boundary":[[3,1],[3,6],[3,13],[3,14],[3,33],[3,34]],"path":[3,1,14]}]}}
```

## 5. Exact finite mass chart and concrete remaining direction

There is a useful three-dimensional **material**, not merely affine, continuation chart. Around p0, the closed infinity-norm box of radius **1/25** lies strictly inside the same visibility cell. The exact minimum distance to any old plane in this norm is

`39757926508261/842035542072490 > 1/25`,

attained at old face1. All eight corners are checked exactly. The box therefore retains the same visible faces, horizon and C176 contact architecture. This is a geometry claim; no uniform equilibrium class on that box is asserted.

For an outward-oriented triangle `(a,b,c)` in a visible old facet, put `w=(b-a)x(c-a)`, `h=det(a,b,c)` and `s=a+b+c`. Its added pyramid has

`Delta V(q)=(w.q-h)/6`,

`Delta M(q)=Delta V(q)*(q+s)/4`.

Summing over the fixed visible triangulation gives complete rational coefficients

`V(q)=V0+V1.q`,

`M(q)=M0+ML*q+q*(V1.q)/4`.

The generator emits every coefficient in `SC83_C176_POINT_CHART.json`. At p0 these finite-addition formulas agree exactly with the independently rebuilt new H-hull's volume and first moment. They supplement the auditor's positive-tetrahedral, coordinate-divergence and own-centred-fan identities. They do not treat mass or centroid as free variables.

The most useful continuation is now **p-position plus full-SPD motion on this new material chart**, with actual centroid `M(q)/V(q)`, or a coupled retained-support turnover if that fixed outside geometry is too restrictive. Two explicit retained carriers couple the inherited death interfaces:

- Parent physical death edge38--45 has owners **faces1/8**; face1 is replaced while face8 is retained. Face8 is original raw input row11, `[1875,17326,141,10000]` before the parent's stated affine map.
- Parent polar death edge2--14 corresponds to physical edge17--54; face2 is replaced while face14 is retained. Face14 is original raw input row18, `[9928,-21771,4765,10000]` before that affine map.

The retained21-gon cap, parent face31/input35, is another natural joint carrier; its raw row is `[-737,-4,-1000,300]`. These are concrete interfaces on the C180-to-C176 line, not a return to the superseded C198 two-cap architecture.

Moving either retained plane changes the outside body: then rebuild the hull and the finite mass-chart coefficients, rather than incorrectly reusing the fixed-outside coefficients above. Permit temporary S/U/H births and evaluate complete P/Q components and cuts, not only named-root escape scores.

**Unresolved:** the complete affine orbit of the new C176 shape, the joint three-dimensional point-position/five-dimensional metric chart, and further coupled retained-support changes have not been excluded or solved here. The C180 global certificate is not transferred to them. No strict110 endpoint or minimality claim is made.

## 6. Recovery capsule, verification tier and receipts

The capsule below is self-contained: it includes the literal parent source and all its rows/affine map, the complete677-blocker/139-cycle bank, the exact Boolean-domain cover checker, the finite insertion and full mechanics/landscape auditor, complete finite-mass coefficient generator, optional numerical nominators, and ten expected output receipts.

Exact replay uses **CPython3.13.5 standard library only**. Optional numerical nomination uses the observed **NumPy2.3.5/SciPy1.17.0**, with `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`; these packages are not imported by exact replay. The cone tool uses trace normalization, nine initial PSD-direction cuts, eigenvector refinement, HiGHS primal/dual tolerances1e-9, and exact integer checking after rounding candidate weights on grids10^5,10^7,10^9,10^11. The optional triple-grid tool explicitly records its finite weight grid; un-nominated triples are not called feasible or excluded.

Evidence tier: one exhaustive rational H-hull/full face-vertex-mixed-edge mechanics implementation with three mass identities; an additional explicit finite-pyramid mass check for the new body; and a separate exact integer matrix/finite-domain proof. This is not a claim of two independent full mechanics auditors. The inherited tetra446, weak-prism and unbounded-H controls pass. Fresh source-only recovery and all ten byte receipts pass.

Save the decoder below as `RECOVER_SC83_C180_SPD_C176.py`, then run:

```sh
python -B -S RECOVER_SC83_C180_SPD_C176.py SC83_HANDOFF
cd SC83_HANDOFF
python -B -S REPLAY_SC83_RESULT.py
```

Optional reusable nomination commands:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NOMINATE_SC83_CONE.py --record 0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NOMINATE_SC83_TRIPLE_GRID.py
```

The exact ten-file source dictionary is **98699 bytes**, SHA-256 `7564f26c7f6ec470fa825e097f06ab7332d4fba7a067a7e70bc988468c2cd6be`. Its XZ encoding is **19436 bytes**, SHA-256 `f0b8df842b9222225ef2cb492b99fb63362f6b4a64afd99fc4ccd2d4d3c317c4`, with25916 nonwhitespace base64 characters.

Principal exact receipts:

| Object | Bytes | SHA-256 |
|---|---:|---|
| Complete blocker/cycle bank | 49575 | `e6468a314fa59323038a1bbed42250a537d1cf39d8981799e3908bc4354be4e0` |
| C180 global-exclusion report | 12472 | `c7afe8734b5a06b5e9fd03b1ba9348958aee96b9aa2b75259c1e313a1873cfa7` |
| C176 exact H input | 2626 | `1485cac2e4d8ab7c08f3332806b4a982b9cbc943ce6b86b91a3567df29d4c126` |
| C176 full mass/mechanics/PQ audit | 612222 | `30a1748601799c9aacf8144417097a36a05252263c04d4e78720e9469ae757d2` |
| Exact point box and finite mass coefficients | 20647 | `2ee140d79dcc9b7dc6d75ea946451910322e60e154f17cb13541a663b70643fc` |

Expected decisive terminal markers:

```text
SC83_C180_INTEGER_ND_BLOCKERS_PASS 677 649 24 4
SC83_C180_DIRECTED_CYCLES_PASS 139
SC83_C180_ALL_SPD_U1_WEAKU0_EXCLUDED_PASS 60 813749
SC83_Q10_ONECAP_SEPARATION_AND_POINTBOX_PASS 14 1 1/25
SC83_C176_QCAP_FULL_AUDIT_PASS 52 88 38 176 11 2 11 0 0 0
SC83_RESULT_TEN_OUTPUT_HASHES_PASS10
SC83_C180_GLOBAL_AFFINE_EXCLUSION_AND_C176_MATERIAL_HANDOFF_PASS
```

Convenience copies, not dependencies of the inline recovery: source-and-audit bundle (`SC83_C180_SPD_C176_HANDOFF.zip`) and decoder (`RECOVER_SC83_C180_SPD_C176.py`).

### Complete inline decoder and source payload

```python
import base64,hashlib,json,lzma,pathlib,sys
B64='''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'''
x=base64.b64decode(B64)
assert len(x)==19436 and hashlib.sha256(x).hexdigest()=='f0b8df842b9222225ef2cb492b99fb63362f6b4a64afd99fc4ccd2d4d3c317c4'
b=lzma.decompress(x)
assert len(b)==98699 and hashlib.sha256(b).hexdigest()=='7564f26c7f6ec470fa825e097f06ab7332d4fba7a067a7e70bc988468c2cd6be'
files=json.loads(b);assert len(files)==10
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'SC83_HANDOFF')
out.mkdir(parents=True,exist_ok=True)
for name,text in sorted(files.items()):
 assert pathlib.Path(name).name==name
 raw=text.encode('utf-8');(out/name).write_bytes(raw)
 print('SC83_SOURCE',name,len(raw),hashlib.sha256(raw).hexdigest())
print('SC83_SOURCE_ONLY_RECOVERY_PASS',len(files),len(b),hashlib.sha256(b).hexdigest())
```
