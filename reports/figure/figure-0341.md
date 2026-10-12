# figure-0341

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Sharp Quartz 24 — whole-support replacement, two exact monostable endpoints, and finite ordinary-moment capacity

## 1. Verdict

**No strict homogeneous own-centred (1,1,0) body was obtained.** This continuation produced two completely defined, independently audited, cold-replayed **strict (1,2,1)** bodies. Both satisfy the edge budget, but both retain a second unstable vertex and a saddle.

| Body | Actual (V,E,F) | Own-centroid (S,U,H) | Weak face/vertex/edge equilibria |
|---|---:|---:|---:|
| Immutable parent SQ24_MN41 | (41,117,78) | (2,1,1) | (0,0,0) |
| **SQ24_P72** | **(72,108,38)** | **(1,2,1)** | **(0,0,0)** |
| **SQ24_P208** | **(208,312,106)** | **(1,2,1)** | **(0,0,0)** |

P72 is the smaller new supporting architecture: it has fewer true edges than MN41 and exactly one stable maximal face. P208 spends additional edges and has a smaller remaining unstable/saddle distance-ratio barrier. Neither is an overall small-body record relative to earlier GU22/NP37 results, and neither is a Gömböc.

The principal construction changes are substantial. Both new filled solids strictly contain the **unchanged literal MN41 plus the closed Euclidean ball of radius 75**. Every old MN41 boundary feature is interior. Their actual added ordinary volumes are positive, and their added first-moment vectors are exactly zero. Thus this is not another motion inside the invariant MN41 s-cell. It is an endpoint-changing replacement of the entire old supporting geometry, with a new mechanical packet rather than a claimed 110 cancellation.

P72 also supplies a genuinely resized, rank-three **ordinary-solid moment actuator**. Three whole maximal facets move in an exactly checked supporting cube. Its actual first-moment map is quartic and is proved to cover the infinity-norm moment ball of radius **1,000,000**. The proof includes finite nonlinear bounds and actual mass reintegration, not only Jacobian rank. This capacity belongs to P72's specified cube; it is not unlimited, not automatically available on P208, and not itself a centring solution for a large unspecified surgery.

A separate new exact theorem excludes **all first-generation original-vertex-witness additions** to either P72 or P208 at zero: both current unstable roots survive the entire convexified old diameter-ball envelope. New witness generations, moved source geometry, or a changed root remain outside that theorem.

## 2. Immutable source and lineage

The defining parent remains **figure-0337**, SHA-256 **9ec0ba835fa2e90eceb2c74729178ca0d1bf6e351e1890f061195520697a4c2f**. Its canonical v2 payload was reconstructed and hashed here: **38,886 bytes**, with exactly that digest. No parent-identity, incidence, or class conflict was found. The journal's integrated parent is explicitly MN41/211, not 110, and its small actuator is not unlimited compensation. 

The original seven-file parent recovery and its complete replay were executed again. The parent definitions and their independent audits reproduced their pinned hashes. The final recovery below contains that entire parent source, so inclusion and mass differences do not depend on an inaccessible archive. The unverified floating 0.9102 checkpoint was **not** used as a defining parent.

Discovery used directions from the literal MN41 polar, then changed radii, directions and active supporting geometry in rooted constructions. The decisive hard constraint was the actual uniform-volume centroid of the **filled polar body**, not the centroid of the normal-point cloud. New generations and whole-coordinate changes supplied the larger normal array. The frozen integer normal tables, not an optimizer trajectory or a claimed unchanged-polar relationship, define the two accepted new endpoints.

There is no certified continuous death-before-birth path from MN41 to either new body. Endpoint inclusion and the disappearance of the old packet are exact; the replacement U/H packet is also exact and is not hidden by the lineage description.

## 3. Complete deterministic exact definitions and ordinary mass

The inline recovery capsule in Section 10 contains **both complete literal normal tables**:

```
RAW38.json:     38 integer triples, D=10^14, scale=256
SHA-256 f041f7de79a5c6dd59a522cbc8ea9a363488e2a316888b0f02545eae13b4a847

RAW_DENSE.json: 106 integer triples, D=10^13, scale=256
SHA-256 8700e553c66f3f4d1e26e0f23488bd156605bebedca86f77701fddfc49f812e5
```

Here is the full mathematical recovery rule for either table. Let its rows be the integer vectors I_i and put K=conv{I_i/D}. Enumerate every maximal supporting facet of K. If its primitive outward integer plane is n_f dot I <= b_f, then b_f>0 and

`x_f = D*n_f/b_f`.

These are precisely the vertices of the bounded filled polar

`P0 = {x : I_i dot x <= D for every i}`.

The code reconstructs each maximal P0 facet as the exact convex polygon of its contact vertices. It does **not** round the resulting vertices independently or delete nearly coplanar diagonals by tolerance. Canonical labels are fixed by the complete source's exact hull ordering.

For the deterministic oriented polygon fans T in the source, define the following exact rationals:

```
V0 = (1/6)  sum_(a,b,c in T) det(x_a,x_b,x_c)
M0 = (1/24) sum_(a,b,c in T) det(x_a,x_b,x_c)*(x_a+x_b+x_c)
c0 = M0/V0
P  = 256*(P0-c0).
```

This is the complete endpoint definition. In particular, the raw uncentred polar's small moment is **not assumed to vanish** after rationalizing the normals. Its physical centroid c0 is computed exactly. The final translation is to that actual centroid.

The exact ordinary volume and all first moments are therefore

```
V(P) = 2^24 * V0
M(P) = 2^32 * (M0 - V0*c0) = (0,0,0)
g(P) = (0,0,0).
```

Together with the two literal normal tables and the deterministic facet enumeration, these finite rational sums specify the exact volumes without a decimal approximation. Both auditors emit the complete reduced fractions, raw moments and raw centroid, and independently agree on them. The resulting volume fractions are large; the capsule regenerates them in full rather than truncating their digits.

| Quantity | P72 | P208 |
|---|---:|---:|
| Ordinary volume, approximately | 384068259.2060535 | 287664912.3787803 |
| Actual added volume over MN41, approximately | 383536077.3366963 | 287132730.50942314 |
| All three final first moments | exactly 0 | exactly 0 |
| All three added-region first moments | exactly 0 | exactly 0 |

The inclusion certificate is especially simple and global. Every exact MN41 vertex has norm strictly less than 125. Every final new supporting plane N dot x <= h satisfies h>0 and

`h^2 > 200^2 * (N dot N)`.

Hence each new body contains the closed ball of radius 200 strictly, and contains MN41+B_75 strictly. The old MN41 coordinates are not moved during this test. Subtracting its exactly zero moments from the new body's exactly zero moments certifies the moment of the **actual filled added region**. No point weights, altered density, or disconnected nominal cap volume is substituted for this material.

## 4. Actual maximal facets, true edges and exhaustive mechanics

P72 has **38 maximal polygonal facets**, including one decagon, one dodecagon and one 13-gon. Its actual E is **108**, not the 210 edges of a simplicial display triangulation. Here is the complete maximal-facet array:

```python
F72 = [[26,61,62,49,54,46],[43,50,57,44],[28,44,57,55],[6,29,60,61,26],[9,40,38,67,69],[9,69,68,60,29],[49,62,70],[20,50,43,22],[8,20,22,21],[7,8,21,31,12],[11,28,55,59,63],[1,5,24,42,4],[41,46,54,58,52,47],[49,70,71,58,54],[1,33,39,35,5],[1,4,2,27,32,33],[16,66,67,38],[59,64,68,69,67,66,63],[12,31,30,36,18],[19,25,23,36,30],[3,42,24,19,30,31,21,22,43,44,28,11],[5,35,10,25,19,24],[2,4,42,3,16,38,40],[0,34,27,2,40,9,29,6,14],[10,23,25],[0,17,37,34],[45,56,48],[13,32,27,34,37,15],[3,11,63,66,16],[7,13,15,64,59,55,57,50,20,8],[10,35,39,18,36,23],[7,12,18,39,33,32,13],[6,26,46,41,14],[52,58,71,65,53],[47,52,53,51],[0,14,41,47,51,56,45,17],[48,56,51,53,65],[15,37,17,45,48,65,71,70,62,61,60,68,64]]
E72 = sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
              for f in F72 for k in range(len(f))})
assert len(F72)==38 and len(E72)==108
```

P208 has 106 maximal facets and 312 true edges. Its facet-size histogram is `{3:8,4:25,5:20,6:27,7:10,8:6,9:3,10:3,12:1,14:1,16:1,21:1}`. The full 106-cycle array and all 312 edges are deterministically reconstructed from the complete literal RAW_DENSE table by **both** implementations and emitted in their complete ledgers. This exact reconstruction, included in the inline capsule, is the defining incidence recipe; no unprinted retention mask or guessed polygon merge is required.

The exhaustive own-centroid census is:

```
P72:
  sole stable facet 0: [26,61,62,49,54,46]
  unstable vertices: [9,68]
  saddle true edge:  [0,14]
  weak faces, vertices, edges: [],[],[]

P208:
  sole stable facet 0: [167,191,189,194,176,197,205,179]
  unstable vertices: [3,207]
  saddle true edge:  [0,14]
  weak faces, vertices, edges: [],[],[]
```

Every true edge is tested using all four quantities `(t,1-t,alpha,beta)`: both perpendicular-foot coordinates and both incident-normal-cone coefficients. All **432** P72 edge primitives and all **1248** P208 edge primitives are nonzero. P72 has 37 strictly excluded faces, 70 strictly excluded vertices and 107 strictly excluded edges; P208 has 105,206,311 respectively. These are direct exhaustive classifications, not saddle counts inferred from Euler's identity.

### Exact witness structure and the new closure regions

The following is P72's complete strict primal parent array, with its **two** roots marked -1:

```
[17,2,0,9,2,4,9,59,59,-1,5,9,59,37,9,17,9,45,59,16,59,40,9,7,40,3,9,0,9,9,38,40,34,27,0,4,50,17,9,59,9,9,9,9,9,56,9,29,65,61,64,56,29,65,61,68,65,68,61,68,68,60,61,68,68,61,68,68,-1,68,61,61]
```

Its maximum depth is 11. The centred polar has the following **one-root** strict parent array, maximum depth 19:

```
[-1,2,10,0,5,3,0,1,7,8,28,21,0,0,30,14,4,1,9,18,19,24,11,22,19,15,27,31,16,31,24,14,0,12,33,34,33,29]
```

Every retained nonroot arrow is positive exactly; the polar relative reserve is greater than `1/134217728`. Thus the one-root certificate proves **monostability of P72**, not monounstability. P208 likewise has a one-root polar forest, depth57 and reserve greater than `1/131072`, but a two-root primal forest of depth23. Its complete arrays and exact witness values are regenerated by the source and stored in SUMMARY.json and the audits.

For P72, U9 has incident facets `[4,5,23]`; U68 has `[5,17,37]`. Saddle `[0,14]` has incident facets **23 and35**. The short true-edge route `9-69-68` exists, but is **not** a certified radial-ascent escape. U9 has radius about1312.266 and U68 about929.668. For P208, U3 has incident facets `[35,51,72]`, U207 has `[4,27,40]`, and the saddle has incident facets18/25. A shortest true-edge connection is `3-29-77-177-186-196-192-207`, again not a monotone witness certificate.

Define the remaining unstable/saddle barrier as

`B_U = 1 - r_H^2/min(r_U1^2,r_U2^2)`.

It is approximately **0.7773900909209894** for P72 and **0.529383711438173** for P208. This diagnostic concerns the **new unstable** packet, not MN41's old stable-packet barrier. Neither number establishes proximity to cancellation.

## 5. An executed whole-facet ordinary-moment actuator on P72

The compensator facets are **16,29,36**:

```
16: [16,66,67,38]                         quadrilateral
29: [7,13,15,64,59,55,57,50,20,8]        decagon
36: [48,56,51,53,65]                     pentagon
```

Their vertex sets are pairwise disjoint. Let N_i=I_i and h_i=256*(D-N_i dot c0) be the canonical P72 supports. Put g_i=max_j |N_ij|. For the three selected facets replace

`N_i dot x <= h_i`

by

`N_i dot x <= h_i + g_i*t_k`,

with `|t_k|<=1/4`, keeping the other 35 support planes fixed. Each vertex is the intersection of exactly three planes, so its displacement is an exact affine function of the controls, obtained by a rational 3-by-3 solve. These are actual filled convex solids of density1. Negative controls can remove material from P72, but **every body in the entire cube still contains unchanged MN41+B_75 strictly**. This is not a positive-cap-only actuator claim.

The final checker proves all **2520** off-facet vertex/support inequalities over the full cube. It includes both the moving vertex and the moving support offset. Specifically each lower bound is the constant slack minus one quarter of the sum of the absolute values of **all actual affine slack coefficients**. The corrected exact support ledger has SHA-256 **fb2934f697e69a04ca88cb8a87afbc2d2d788670f9da541d4c8a4d57aa427e96**.

### Exact physical mass polynomial

With the coefficient vectors regenerated by the included actuator.py,

```
V(t) = V_P72 + sum_i sum_(k=1..3) v_ik*t_i^k
M(t) =          sum_i sum_(k=1..4) m_ik*t_i^k.
```

All mixed coefficients vanish. The geometric reason is that variation of volume or first moment under movement of one support plane is the boundary flux through its own facet; that facet's vertices depend only on its control because the three moving facets have disjoint vertex sets. This is not an assumed sum of independent overlapping caps.

For a triangulated moving facet with affine vertices a(z),b(z),c(z), its exact derivative contribution is

```
V'_i(z) += g_i * [N_i dot ((b-a) cross (c-a))] / (2*|N_i|^2)
M'_i(z) += g_i * [N_i dot ((b-a) cross (c-a))] * (a+b+c) / (6*|N_i|^2).
```

Integrating these polynomials gives every literal rational coefficient. The source contains the complete implementation, all inputs and all helpers. It independently checks the resulting mass at **21 actual parameter states**, including all eight corners, using **two different complete tetrahedral mass integrations at each state**. The guaranteed volume bounds throughout the cube are approximately

`383999336.789681 < V(t) < 384137181.622426`.

Let J be the three-column matrix of linear moment coefficients. Exactly, det(J) is nonzero; numerically it is about `3.6324533131151946e22`. The rigorous rational bounds are

```
||J^-1||_infinity < 1/10^7
L = max_row sum_i sum_(k=2..4) k*|(J^-1 m_ik)_row|*(1/4)^(k-1) < 1/40.
```

The actual values are approximately `9.622830958503351e-8` and `0.02035804385805635`.

For every desired first-moment vector y with `||y||_infinity<=1000000`, the map

`T_y(t)=J^-1*y - J^-1*(M(t)-J*t)`

is a contraction of the cube into itself: its norm bound is less than `1/10+1/160=17/160<1/4`, and its Lipschitz constant is below1/40. Therefore that actual solid family realizes **every** such ordinary first-moment vector, at a unique control inside the cube. The polynomial and all bounds are exact, not numerical rank or an extrapolated linear response.

Only y=0 gives t=0 in this cube. A nonzero auxiliary control has actual centroid **M(t)/V(t)**; it is not asserted to be a zero-centred accepted equilibrium state. A primary surgery must cancel that real moment and preserve or rebuild the support/mass cell. The guarantee is finite: capacity divided by V_P72 is only about0.002603704, and divided by `V_P72*max|vertex|` it is about`1.98413e-6`. This is useful new physical leverage, not proof that it can compensate the required whole-basin replacement.

## 6. Exact exclusion of the complete first-generation witness envelopes

For either new centred body P, let

`D_old = conv(union_(w an original vertex of P) closed_ball(w/2,|w|/2))`.

**Theorem.** Every finite convex polyhedron Q satisfying `P subset Q subset D_old` retains both named unstable vertices of P as strict unstable vertices at reference centre zero. In particular, no uniform-density such extension with actual centroid zero can be110.

This includes any finite number of points having a strict witness among P's original vertices, and their entire global convexification. It is stronger than a finite unsuccessful ball-sampling run. It is not an exclusion of new witness generations, a changed root outside this envelope, moved old geometry, or other actual reference centres.

For a root u the code proves, for every other original vertex w,

`h_(ball(w/2,|w|/2))(u) < (1-epsilon)*|u|^2`,

with epsilon=`1/2000` for P72 and `1/100` for P208. Its own diameter ball has support |u|^2 in direction u and touches that plane only at u. Hence the whole convexified envelope meets the supporting plane `u dot x=|u|^2` only at u. Every other vertex of Q has a strictly negative radial escape from u, so u stays strictly unstable.

The certificate avoids square roots. Write the unscaled raw polar vertices as A_j/b_j, and c0=m/d with integer vectors A_j,m. Put `U_j=d*A_j-b_j*m`; the final vertices are `(256/d)*U_j/b_j`. For epsilon=a/b, root i and j different from i, verify

```
uu = U_i dot U_i
uw = U_i dot U_j
ww = U_j dot U_j
z  = 2*(b-a)*uu*b_j - b*uw*b_i > 0
Delta = z^2 - b^2*uu*ww*b_i^2 > 0.
```

A separately evaluated cross-product identity must equal the same positive Delta:

```
4*(b-a)*uu*b_j*((b-a)*uu*b_j-b*uw*b_i)
 - b^2*b_i^2*|U_i cross U_j|^2.
```

All **142** P72 and **414** P208 nonself-ball comparisons were executed exactly. The positive-integer ledger hashes are

```
P72:  6bfeb96235f67f0181777ee610d518297e25588ee8c7d7caae2371d862d65665
P208: b3337193309055bc849775d1f2972ddc232991f14416cefd2484ed7b258492c6
```

Their complete reconstruction and byte encoding are in envelope.py. The two discriminant expressions are an algebraic cross-check within this certificate, not a claim of two separate independent theorem implementations. Both underlying solid geometries have the two independent full audits described next.

## 7. What was executed, what failed, and verification boundaries

The exploration included whole-coordinate motion in rooted normal charts, actual-polar-centroid closure, targeted source-facet loss, new geodesic witness generations, direct filled-hull additions, support-offset optimization, general metric screening, and whole-basin radial merge-tree objectives. Several numerically small local losses simply moved a carrier or approached a nearly coalesced feature. Temporary many-root states occurred. None was treated as an accepted cancellation.

The two exact endpoints are frozen rational-normal checkpoints. Their construction does not require rerunning numerical discovery. The research supplement preserves discovery programs and numerical states, all explicitly unpromoted except the two tables used by the exact constructor. Finite sampled failures are not global exclusions. The exact envelope theorem above has its stated, narrower hypotheses.

Two finalization errors were caught and corrected before the final capsule was frozen. The first support-cube implementation omitted the moving support's own offset in some nonincident slack bounds; the corrected checker includes it and passes the entire same cube. The envelope wrapper also needed to serialize its output before hash comparison. An intermediate replay using those older sources was superseded, not counted as the final corrected capacity certificate. The completed final source-only replay uses the corrected ledger and writer.

### Two complete independent mechanical audits

Auditor A reconstructs the normal hull from all supporting triples, derives every polar vertex from its exact plane, reconstructs projected convex polygonal facets, and integrates raw volume/moments with origin-based first-vertex fans. It checks every other vertex for instability and solves the exact two-normal Gram system on every true edge.

Auditor B imports no geometry helper from A. It uses the separate original all-triples hull implementation, independently recomputes each polar vertex by Cramer's rule from contact triples, constructs maximal polygons using three-dimensional supporting lines, and integrates with a different interior reference and last-vertex fans. It classifies vertices using incident tangent generators and uses cross products for the full edge cones.

Both check all support incidences and strict nonincidences, coherent opposite edge orientations, connectedness, the actual maximal lattice, positive volume, all raw first moments, the true centroid, and every strict and weak face/vertex/full-edge equilibrium. Exact translation/scaling identities then give the final zero moments. The faster integer-cleared implementations were additionally byte-compared against separately executed slower P72 audits. No triangulation diagonal is classified as a true edge.

The final replay also executes regular tetrahedron, cube, octahedron and exact weak-tetrahedron fixtures with both implementations. The weak fixture gives strict `(3,2,3)` and weak `(0,2,2)`; four invalid denominator/duplicate inputs are rejected. The complete original MN41 source replay is rerun as part of every full construction replay.

These are independently executed software implementations within this research, not external peer review or proof-assistant formalization.

## 8. Most useful continuation

The natural P72 target is to keep U9 as the remaining large root while replacing the U68 star, its closure through facet5, and saddle facets23/35 in one globally checked solid. The exact first-generation-envelope theorem means more original-P72-witness ball points cannot do this. A second-generation or changed-root escape must be designed with the new physical closure region, not appended as a score-only repair.

The moment actuator is now substantial and finite, but it is not independent of arbitrary surgery: facet29 meets the U68 closure boundary at vertices15/64/59. Either preserve its full supporting geometry while making the primary replacement elsewhere, or rebuild that compensator and its capacity certificate. Moving only its existing controls cannot be advertised as cancelling the packet. P208 offers a lower-barrier alternative with additional ancestry, but no P72 actuator proof is automatically inherited there.

The simple-body edge arithmetic leaves room: if that combinatorial stratum remains simple, P72 could gain130 maximal facets before E reaches498, and P208 could gain62. This is only budget arithmetic; actual convex realization and a fresh maximal-facet census are essential. The decisive acceptance test remains the full own-centroid strict110 census with no new roots or weak equilibria, not local loss, forest rank, or a vanished old label.

## 9. Frozen reproduction evidence

A fresh directory containing only the 18 decoded source files was used for the **completed corrected cold replay**. Both independent full audits of both new endpoints, the complete parent replay, all 21 two-fan mass tests, both envelope certificates and all eight output hashes passed. The observed terminal markers were

```text
SQ24_P72_P208_121_FULL_PHYSICAL_POLAR_AUDITS_AND_MILLION_MOMENT_CELL_PASS
ENVELOPE P72 142
ENVELOPE P208 414
SQ24_P72_P208_COMPLETE_COLD_REPLAY_BYTE_HASHES_PASS
```

The final pinned output hashes are:

```text
ACTUATOR.json
  425f8995f1913f11e4deaba4840fd8050a9ffe02c791b299f9f5b541749b40f4
ENVELOPE.json
  467f29f3a6e081933e46c9cc9f6a6ed68d3cf1e755902313e87ae642aba2b654
FIXTURES.json
  548f715050ddcdec8189a4666a31299527041eda8230f2121e631153dc63e8c4
P208_A.json
  f5bbf0b26973c49d1b8b903a2960987793a454bb4ccf9627f25af7af760788e8
P208_B.json
  6c510fcf516c1c100356e94564343a017c8b8a2b1d1e523510b20b942043e3d5
P72_A.json
  df4857533a141900ff0b0783642f9911d8f7cc7423d81c55291f8f2596861c8d
P72_B.json
  c99fe70ec5c16723f887b8b71356169039c5f53492a7baf81e257d9f227b6329
SUMMARY.json
  51bf9204f2e50c57cfb966ac90d11d5818ca6a5d1a2982cf8e798a54f2b6a849
```

[Exact source, both full audit pairs, complete incidence/mass ledgers, cells, envelope certificates and corrected cold-replay receipt](sandbox:/mnt/data/SQ24_POLAR121_EXACT.zip): **62,416,995 bytes**, SHA-256 `b10fa89528ed28144e14c32456cecb55f73e7c931889b584b86f62dcfc9b0065`. All **39** manifest payloads were checked; the archive has 40 files including its manifest.

[Discovery source, logs and explicitly unpromoted numerical checkpoints](sandbox:/mnt/data/SQ24_POLAR121_RESEARCH.zip): **461,479 bytes**, SHA-256 `5fb03728bfafef7fdbd6e91c3a89e73353519019898e933e03c2424a2635080e`. All **220** manifest payloads were checked; the archive has 221 files including its manifest.

The corrected final replay receipt has SHA-256 `ef08357ba78ca8ca24f64efc944b4bb660aa82d18870f4f8e2e919fde18c8b3e`. These archives supplement the complete inline exact source below; they are not its only defining data.

## 10. Complete standalone exact recovery

Save the complete program below as `recover_polar121.py`, then run:

```sh
python -S recover_polar121.py
cd sq24_polar_replay
python -S REPLAY.py
```

Exact recovery and verification use only the Python standard library, executed here with Python **3.13.5**. Do not use `-O`. Discovery used NumPy2.3.5, SciPy1.17.0 and Torch2.10.0+cpu, none needed for this recovery. Large exact fractions require the source's `sys.set_int_max_str_digits(0)` calls.

The decoded canonical JSON contains **18 complete files**, **74,280 bytes**, SHA-256 **1875334fc1f714b67734a5e48981356b71a8564f57233fb565ac94b5b4e5d30c**. It includes both full literal normal tables, both full polar auditors and both independent underlying hull auditors, the complete mass actuator and envelope checker, the original seven-file MN41 parent source, the constructor, replay driver and eight pinned outputs. There are no omitted geometry helpers, numerical solver inputs, active masks or missing rational parameters.

```python
from pathlib import Path
import json,lzma,base64,hashlib
B85=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;UXtd(_H{Ph=iqrocag;lg9zQDdLTm8Uv={r_qBICC-iR0bQ*$=21xxhCjM(`3XSa<U1Zx
CikSq=`#BOgoql#+Jb7g+uMXU2=SS!NWHa~b7HnAipjBkM*LUwGVO!XeKeu~mJ5`8Tm%K1i4*$dxG2q&Bv=Zdue|1x<s0&ko1u+2
eY8P6VJ0jyTNQ4t7U*5<P&`iI>jMwM1`Tuq-uSx?sAk)Ok1<qyPUr53tC(nz-BY!!)ZM-TfP&Nji7xT8?58i353vu!(kV65HgOLV
TwyDYd}`E*J{==3muTmOb?)b#Hz5!=g~XKE82OzbEEH6%gWNMPs6g`LM!E0aGb3zS(7oKj&j9Apjst$uU*t&AO;T0M#ua-
z@9&Lj0_1NA>(!*y{!HI<$1x^h1A`T!D|3rS?AFH?RPS69Pk9q_XxtB|!JIWr%ztM;DC^~N^#jo0XitXUNnV5g8c9<BOgsMwv;H2
0=hk1yGQlS6h466!jEUdF)?cA5-
Q>9@0&}+(IYn@xiIX{T%iuTyAI%2(=r%qwAerb&7F(j@IN2j>$$r**_5sR;+xE8Fj0?ui3eUkTTJaYqs7`SXy7`>;tV>8J?c=tdN
exus<~UqPX{P#PXWTg{jY>DOhlP;|Pt7HQ?tvg#8izuLtY!Q$3srZ;4<C^=vDu7ZEG)k(u!5-
AZD>76*kFY*%VROfBE$Q+<<s!xvplK5l1D{viaJM-
>uwJ12G68gg_CMkVnf*j5WUJNt`4Wo^LGv8v2Trsstw<M=Tu$eV+eHm+OGOqmy4aPmkpEzTdwnMm5Sp_OQn~kiV35qYUCk(-
!ohu7oW@jdV`u8CtLY2x?gaeG1`TbRt8zQDaPLEL91}?-
3XOCAei<Rz~Jhi@t6UWw#sts(K&VfrfhyGu7}2BU0d$8k~bvW$p<wk<ix4l$qX2W?-
n}|DvalMyWvX)$&`ajP{X*$f5sDf?%~h9AcJ24lT=qKC%$5%wF2f47hl|ie^X~a5C=^tnE(QS+Yg$`l;MWOT&mmH{v_TyjTx(n)y
90cO)DvEB|XWKO+LA2WY!;tJV4Im>TNoHwek180oa9p@iQvMgK<AuzUORX-Qcb;%vt0Ujkg_H1o3zStmvH*jDha_1*s{yrhqDtWM
?@a|3!GJN9z=k&Ppw2Rvj9P)rd@AN`ons;r8Nck#XFTUfqfgMJ;(axHix2G=?kB`%Pb1Z0|^LyhXMf-C`7%AR`>=-
XDMM8kz)x{S3!*T~wVeBWF}$pJfnE1^j!%oVzDweuHuf>L-
T>m&HC3)@t@)Lk2@q<bso$OU8h}b$G2BGMXo74}v}007q&744_TNmlNf&_#rnnL-
n~{Y|aVcP^Dc~s5k+EDHi{!v@AipFkMEc34c}Gky%elEq30}?voQH5^80#D0h~a+20Df&7Rt2(m*m5CRwJ!T^EqRU@NHk(o|wAL&
3@~Tqmb(_$nHw|H!|>AE_5FPb@g8ktzmWS!XhPbAbZu6#7Cp;6%ZJHkL={Xi#T?^^b|IZ8=68>rp5yjekCHaipSyb}aR-
`kAdIh6`LmOxDZAUxl$D>y$dQKD9TFkLV1jB=u{%Rz6=aMu%DtEI3%%Y`5M+@E=ZHNlB)rnoi9<ZThK~wU&T=HjeJ_?sCae5C$eR
hOJ;aaua`4NowJzQ<z-)1ud(pFeRdvF0wOKZN=BGuWODe$uBZ0{5|TUh3rpk4Ft*VU49uy@c>NZFlNo-
(0#Ea)_N<wl~q|2KUG|+>=~zcbA!-
Fv<hi{0cvVT)&(8EOU^lA;VNLkM}Q^`Z=>}smO8^1IxrlaGIz6GmGcCbeUsZqg5U(#AvQ3b=i8;CJ9L;CAkRbsZkOIavP$9|NA=V
|et`p}lZyfQ7|W(O1u0+Mu(vW$sqXL7I{c5t=2raK9w0dH=XNw@c7O7O-
^@7_Pc|v|4X(_LA|+&fs)QeTAI$*&Fhpr?Fbr&!<6TqgQxnLC97a4Lx|tC-
>pIoCcAGORy<+;y15;3Mj~&_UTQZwTcy<umeHcM)(YjOT1J`zYb2M7-
m?K7_%b>#l|MlllJtSV7e=m8%(wT1A9Atluk>)YFT;p@IzD^T$U^Tp>t{!@NSc}N!NI@LUQ>HdI^=&ixv2XsLt969C${kt{H1ars
Trgu2y{c`2{LuU-D2FQ`T?MPPUpE;J=RHJm4@y*6L{rwpnG%$X-
hT0#q3RLC{rsoLy>;z0@D##8L%iAHjl^qx<&e^xcD3A8UL~xPZFYy`o0mL=%2z#vFQ>0T;FqUzVjcUHSs?({m#UBtI!pi;7UhzxO
hjaXfVPDceebvF!cKA=Gii@qPZEPxd>k==lp67}?}bql=gm1HFM!k}d2nVm(pgz~00QYlgnOFmc7N{htJU2Hy?o%m`-
jlVj$v<w*oj(STaDmfMB~^{888a3mviESY;3Q&eamSxgHTKU^=Fp&`a`Rmw??95m%RKtgW9c^-
>?jxF1bUlgLB56i5=mX3)=3xNv=DV!BRRvWo7I|2%;q}izlF&$6D8aklzw&=q`&SSpNjSe}iUoaSb~#vJ-
8+Nm~5EX#QvJYcRJ3w;3?490UhZ)2ozY`37X;s{GTV%oYK6t9Ch4_hr<rZU=Kf_{0l~Q^Iabr$`5tqdUcW(h9`F|4iD-
r4L{1mFD>{Ud@Y&_w2pZTm|vOh1lE)Z2cL2o2gmg3W#%0RI(R_H~N9+F;14XUK#Nh!!H%Atf(Skd!LRHUd07o5Jv&G`68|a_*4C)
IB^Fr8*<=VXKsNHylsXxV{kF_dxj+ztqn)Efp50BYoF2>LnzP4285*{uO9}<Z>%?vQdH*s;~*Ozp=EL=J%NuG)~Z6y30>cwVf*H=
0%RSTpiKebAA=KO4Z}<lCK9fZa0JtVyZWoSP$fs)a7g<6$3ySaAU*g64z+nIFs-
|*{k*$Rhd#;O0T))8;U&Wr*V%E0q&%<#wYvtokvRwF6+Ep|BG65UG85m{n6-!HLRFCgbC1x-
rd(@x2WaQRPo5`DaaUp5%OrI<h}Ty{<r+vrWYPak4GtjfE*@269~l^V;F+yoQwBC(3ZwH(vjgb}mC8?@PRT2+xP}LWgSwLJ`^Oa4
WrHSg0WJ=v05^1NTB4B*hHHa#mRSG#z#)&$75pEFHR6Thwr#LiLyr?P${&tG=pM~cwHKm|u$O_YS4HT#+jPKoW!G!)W@ai)X?PsP
9pcTYvS|{SytPTv6I>QiFu}zl((i{RJravx!OtyR7|?L}W}XXo#L}4oubXORq{?IM+8&>vwMp5jF+(mwz$YfhTA3p@bl0<l9)RsP
fK9w3LO1%pIzu0R9K3}dec$4ON;%AK%<YBRRx5pxPp+}ryrF?!OsiI?a9nDerDa4qn`6+OONX52?V^Qxnw{4F<)>?y?NBU}y3!Dp
uFg{q9)Vj7hjpK1`Wq+uRNZ~9CRg-Md5rfS;VR@d-
e_MMRJaVtAg?Aub&<?+Y}2(&b|(7(jw*FFwYzg(2!niY3rz;QTax6ULk^AIAWi$R33qDRx5=7)s;1m;960`ME01fiOQUxr>#@*c(
aUt}d;a-=YrQLf#q_@!H~N*}Ok^p%((qWrH2`1U)EM&GyhdyWGdIcTz-
5`aQpUtN4bJk9kS2~c(`EX<LTP)Ku@$vN3c`vdYAk(gE=q3IH)DL#Cquh@MK|7qgm?SYE_H=-
y0q*bG7xx9H+V%UYkegdUxmILNC^oO3DVRo=d$5Q7IV$YW>1OD<JItx>gverV=Ul{A`HN=-m1xBa-Eg1@j`8oL7ma#Eu!l-
sX6%)CD8=D`kEt0V}tSgVbd07A3HIaM=B4)zx8nYS4hf9lJLvP6_gDfciZqVd8c5G$r>EqeFsJAgl|{{>WGN2$_#rQlZZ8~?a>nA
lKT72CV~q+&y&Ez?Xr-
m=n?7$H;5LjKD;={Gk0}S6gb^U{*B&t#fp{227hw3hkloC_4x^FiNx9osMjHXa5J<Sv~rtof?2u#ePP(28y_r*`MU^kpehU>x>@k
*c+-qk3|jpMO&l*SJn4u^6-
MP<v{_%H)=90RR=zFgJaub^auc%*!})f<m&>!;dN&ksc>bSuc<*d@2x<pu;!+M($}dYh&8MXkmmgY7idAc0JMW^=Mkxm?>k*!1Wv
1-
Q2fR<r4I$q`f_6LQtiFjh5I4yJN9|A#$e?fr_glhXy4c4~8Y$uVb}3e)dB@sRq&bJDK2ci+(~N1#+Qmg?lzOTZD=#k&rT4V@m?zW
B<(F(9*oF-oWY&%nUnw@gfas?!aCW0VNIely(L$Ie5kewgBeDc)re=Epq;7eyBiJYG@r%xkSMXe65%!erCY?~k2$JB3e)QJ0bF9s
e?$Xpj<K&V0Y0oaEkp#)ohSZa3Ob*D_-SsU535J^@UZ>@YIFQkuq2627BrR9HOMoD%a|e}lEHE2fzyq-
W#gzB_)b`ck7w>Kev`$^`8d8E!x*hB*RjygA!S<i?bU`y{CZrZfL1Yg6z*d*47flF(YUe7F9GD0-i-d>pxm-SEhKQxs*wPr+%XJD
xsR-8dg4%5yC_hd7;8Dx%2{F2sC3QfB>=sBQP#bOe5&U7~`0IO`Muh#SRljqMH>HCPvGSBNTtFW8Rne=#OR#+TYL&vKC-qJqZ!rZ
$1-bDc)Tv8+yiK{MONpGHg#!d4Y#P*U9|g&3=mNeEPzWfldD<tPp$Ez3<LKLp@k|-
}55i8co1#3UoUTIe1JKODa6?+li{H>XD2YSQ7dM)vlNO~#UpQ__VVl&U-
D6IRgLk0%$4ap?+S_G|N!0G+dP00)yD{D_NT)8n_lcG?d(EaE=-afajnBt!r=>Z)lf;@6Porw0crI>5L?{h3kI_8R0NV-
%^qa6tWk+!(afhmSyNzo|N0!8w;+ckA+Qs~HjR=yecco8~zJRl9(1hD&@X1|RA8p)ra`qZm8kGIt*@_`2iQQ|QqyfkGS%<1t(o1!
0kCvs2+8d(#w0PTYyhGF`on7BHM+e1Ko0rFHQkqh(A|>VbYLFQ8VvX&YKviO+8*Q^i*&(K0BDXJo&wJ+(OXaQG7^}|M%}uSa*CxE
$Su8O6bC_nB0zmPTXe2EglG1V2(N~U=ak<G=!$z*%8eu^?{}qv7%sJS*i;bUcom|mVlEcDT{LO3@FWBjoEBx2yl2W$;xzj+wtUuc
lf|mh~*SLcrUsu1G|KoYDoC99spfA-
|wBC;%<XKDBjF1GZ7jyqrXRKVki|*kW4AXX}!3K@LT}R$IdZ*lG8o%4PM+seRzK?&uk(AB8W5GgH5=6k6rC1B-
ygR7<GjBrsv5Ao}m<u<=Uu>G9rg#Rg?oy5@uOZ%g+9$wU!T(qqgWmCjv;M$o+u?bx5mSi~<i5n-
thHpZ$D+{<vq2}A3JijfNn(W^4OxGjUft8>z<aY^v|xp$jpYdL`r+T2-
OezeZl?2X%G|(X{&|R&2t@wd)vP#chJ&?GS7(r0fK#fZK>=x|ROWoZm}+gXy<|<oXz^!XgW3a59#OE{753qQUalWmWNKbDAN-
`*ry<S`;y+*$YjbRfJ}wO6HuK6jM(o=7#g2=@Vyz3<#N+KY?X_$xQ1I!7bUS=~@nh5p^5VzJZqQ^1&_$K=n2VMmiSoS>3egKf8Zh
=fazyQ?EitdA0H!ElD5hu{;Vz1DhSIWQrex~YQQ;N;t0otFQ$?F${T&muV$v7t7oQTy4FlG|_}bf4V*sE#LV<gpfAVp@6a8#YUdX
sTU#J!MR;)2HDtaRI^_v)6xU+!fvOy}%kcVm@tZthM`3v2sPhu=l0qF79qHhs=-N$F|hB-uoA18+_xpT$(=GYKvEOzRSztY=2U#3
d;P?W@o8fq%%2j#4AN~35eTsjf5>H%D2t1|dUco(uv$B<VGrbq2JS7prDuV=k+h2x5l$?MqjE4Jm^gL)^U$s_0#Vu(q=5)@V8P;j
eGaf83WHgZz_)alcVV{TdJMWHO5l9UKos!pX}WW8i1YCL!KF@XYa^Qzd#Ut~cV%pg_3r6Vlt%CuQ&pyCA)K>PS!Kr4r)Wgr$cC-
x-cM^2#VWN4;z5=gdCEa#)EcE6yn*WSNQ=sT7BJ$8QR7v_#kAkkxfXE%F&&s#Oc>FF}gBWfN|6yx|4-
WWwiNujvg{DE6>&Ol_RB(fq_yV-Z&XM#8-
S;a>Cvy1a)Rq{EDjZj}}N8^nbH;}#*{E?F~RA_S+PL+Pb9Io*P@(+K~xk6B7v4E*NF{_3Xrx6oaS!Lc6=Ev6eHWWW*Q2F2jbcpMx
Tr7N!<<7FUymzsVE0U14g=pGmFVreJGqwFTKyT!Hmu4IqihjLYDiI(qniGq*PD$|I;?P;h15(ORYRyUkmvF;jn=wkl58%jN&5dKX
3WuSF)0mq$_}}*UQsc+hXFM{AvMz}VPC@JBoszrwVL@=mJ?N@$uHqHq4}BEJ0889DX<=G=d>n{dLFxv)#Gg0`U#6Inhm+PY!q16D
@%p%=B);(uXtX<j8!``u+M3E76E*+2-
iX^CcL2S``O}?fTO{)X^g<2a);?A)d}KInz^rpfbgzhpxvjrfmL!6XdAL)3n}wGT!BX703#QgyjJa=fqe;Qcx@0f~p32}|k+D85$
w$13`l55^EAPXj4?wr_SI5HW;<MnNSx;bhx?=ax4ft~OyI$PSw|YY6p3DOBZT4}&SEMHl_n1f^Bt>&INnvOxPUvgj43kO)*MnkkL
;jKS2I)fgp2~~fR$sU4br$%ueQZ(^X#D~sk|KLzClog~3e5Pqt&E5)KdL3cTm}}rk-
D70NJ@4;K!uQ7V<|Ia=~Q8R1`r`*!b4)Xlb-u`(A|roTl+4UYoUE>qZ+U6h-<IyDwcBbQKL=kqWT~${uO=M_}iK-
@1vn=J1_*9F%XHFZLi>N6hSSse^jHTSfIl-EAr`^;Z}>B16_Y3kshRWxVHsGnkIOXB)Tw8p^=pXkt?Ckb*M4{*`4NPEl&j744b&l
d%Y5klO=f+;v4YN{Ub*`4cqo9`)Dw|FdyQdfpMBLV(E90dM|vguK-
3$&XYS{0%5Hu{&)gQ#)A8vU<jn>Udvu$X9e|yOaOtX9?`GKaW+M3a9q!bZ!i(>+@x=l+dtdqh_+*#KztZ6U@FP=gQ|e@&R)yMwED
=X%RBfNZ-Dn|dfRd)Ripw%7<Q7)_*wO(j&teI*WQD$%sG>=6mK7INKmuZgP!_3vhMD&2{o(oAAp%?ly!FZcPoB-LkKVLC<hby9^u
{_#Npy{Xz%3SHk-a`uv1iI47>1~7Ui<>X4d^RK;&l(+=3w=vFdc4j^Y=(@r<SKbOe_mmxC1aPW#G>mDpk|!*3f(cX_zn2^n3-
#ROqS)eYRwgnYZFVPJix;>w0XeS_>C<_qODX^89MO-
<r%IPwyU#trNHGd1tF&mFtO0{@?1BFbV~IZz5Z^K?dWIwQg@kYzOvPQ@R22raE;ow@=-4f^7e0Y!+-
V<}2UAG4oi)X3%rL%1+mhK63Ksh6>c*NAF&fM)bVW3KG=JBF!=Y{_XkY@B|DB6$nr$BBkPp*x?rCY{R(tTuAUxK)yu2fAE-
C?r@jXC^(wc;h<PZie73-
*giMXXH~&waDI+4^ZW9ivkPAz;hUiXAk5|Jn*VW#ux?TeoDZi<xtOq5@Lt{Tn#v@O|jVW;mT&832EvIcu|4^tDwA}L#@%QnS^S-
1k7FZ7}Tw7%pk~s9u__A>FW8?g!k-3NH`M_c-
(qz0K>716HE12>k{kq`i5`vzH$^ageUd6=4fSfQ07O@S89yVx?##hmNMXOK5u6pj*KRXT3ON_3G;uDrrL=#hE~V93?O~YS;^dxiR
sWd^(GUs=`D3)^W(DqCFNp3cqGBvNr)guVR=gcx$$q++-1g#0{Q>{sN{~S(E+h`I1Q&H;X3-0x#?iT9}lD2Lzntq-Fy37xrJ&ZP?
D=N^lnODuN9$REp1vlPE@TRjee&0aeKOve8~N2OiH?K0jMI6Q6N<ft$ry^TFj(=HnyD{XCV5-
NiG4no6JJP9}WO&+0n#q3WUQk88>uu@(LReIO!I}SiKA{^&^|0-a-#KO*s9YicM1-
QrJRf#Oc4a3uwP@II_sNbF}>V3#*AGFDJfI02tsb@d>c-
u`9+oyN6rz0PzsLTQMac9MKxE9?#6sM<@?yO#p$JPrz%+<t;&_Y$I;z{2%JuII2^55Q)u1iU_3>^Dhs03?&cB$N50d@z%2)w(`i+
dhncgpNDcm1zy{b$Ms_nHfz3`&jA%o1e3OI6TY1H9AR9GqB$icDr8yfXVt`-XP;(9k#ikd1U30pef~HNDB+rn-
;ejJysK*;XV$!OKBSU{@<Ll|(aHhdGUY)h00Q{QOD@u}-
MnmpQoxuH#E8D2N&tfA%OAutNoh17#B`^G{qXbtXTtnd`oF%pTJ)~`4ghNRb6eeHeElhwvvoUyTWmY7_D7T{Xj-`|8gfcHA-esV?
U8~tza5M*Id55@*t;O)$My?Dxm{X9t1ghcb7AWU8BMy^y&rb3jgkX;hLKuvsNj7{ibnw04sUtmr~2M1Ur{Ab7__4LAsNUlWQLM+a
3={jgcP;SS^5WZYPC=f=mcVqrbmUQRoUzcmC7Hg1lI9DO1v>zx<uC@@1LwNSI_#iO8y~eo}0=qZJKf%kh9y<3sii=2^{H%L1;^dF
1E@09(ucfLb{qNVpo094z&=&(f^sIQ@WP5b326DeE&Nuvj4D-
BB4MN72p!BH@wR|Y(vcC#4R)tzX4Y@FV`?N+C9?)g>76T6D5kixtKMWtrqeQc?MzlI78bHk@~v*J|^lU6QLAtBeF<Wgj{n@2JD2<
SpG|nbFAYB)g<lA_bXlRznDK1=1LOH=O4!~yHvA6h$;GWz`WKe#6eF`#3R?@YF-*Xr;qU~vyZ=qf4^1%%^N;E)9%21-
qNla4jToGj5&>MGLrQt@d`}J+Uew38!cin)Qwsh6I}F+!tS<QBLC$9sdyk1XyD2?>IVo@&Ky8*GYjC%YpGj%4?Fd%jb5P*saX#l-
U3{|R_%gpfo*<bN+FSXIcAcZIy2~dVa5%MN9#>&SFs#EJlJ>!S6QU7H|?#>74{W*LxN{I_D|Ix8Y~H?dGNw83TK(r_iCCjCruXr{
1-
Ubi)(MifoSM@zdd^kY7N}B33?1ow6x>tH8B>lkZQrh)jabWNr={bg=zr4?6}!7sAv+u7$AAj{;uZMj?|^qU4+`WvQrp>K`O>rH`x
X2?*6gb>c#RVGOR7eAxrX1erj_PJoh<fErY33!~d>!IP0ac#ChIwFhF_M*kIX~Uj(<q8x<y`vUT4O4RZFr<!0>ryti(JV?)H=T9H
p3T_qivX<li<GQr7ZrMZ7b{DU4H@{kV@D2(zF^&7gnulDOas44Wp*LSE0rbl=ECgTA#R=mm)lW9?xsB`;mY)?*nmxsG$jsmWw`J7
Rm8`bN!3G2~Yk0%l})9|D6P>#G!i3ceuf(KV_O0Mvm`>2y><o7Wk8kwl7^7TSBGR%t+q5J!mA(A|Z{EEeFEtu!<ohIVV(U)Tc1&-
*!d)~>EVUSHN15Q-gwp99>iS)1-
y%ZXXa8!(NKq78EJD)5M>VfpaTg%tSlQEMv7w++wW8l#`+5#YXCL%2kcr~SLdTCJ8^y)D4DJ1&Yti|H9ca8W70cp-IuqMnG`6MAN
MA~RQ0Zj<>3_nYFQ`=R1s_r!$eERT(O(9Y7=}4v>yG6LqHfaQFM?*nGR!zOpQ6K|FqWZtcHq<;4N>qz0UaCpo6uHOl#N?Z%JZH~<
LL2&l#8NnSP8bK*I*W8g7(KXb*h2mj6o<U1R*DyT6=qtbQd<g$dH)&lH-
wv4WB5lAtSF<fw%{v*Th+8CH>Y=L)~tv^*EZbX;8d_{(@YXC&U?89`@NXpN-Jb4q4<&MVdN^lz+%)`+sUEKK<-
3!ODD%QF91~y*im?NM+)d%ZJ?N?3a#hL|Mjpga#k<DudXa+ZL+N*_rtD@|1}M<+=Bb+cR>1j3-
n&z5RxQE@Hz@|6Vbje?E|7mfPN%a&X%5aqvr=Y^Mx!)|Bj3-{5!VkbR(+gfrg+w%B1Y71}O0oEz-Akn0VVyP1*OeETH`bnL10>x^
%k^a7{m|V?WPCrfzaj32Nw^Nz1Eja1m;4`}A0g0l0I+#*p%P<T9FU-(P)fsWoR6IEZLR?`|nx=Qbg}b>=x3i!OWkh!2c-
!e#Ff;q=mQD^H-3c#ho3^kJvwoWVTsf8L=bjb%Q~rH3WNin(G_tgg#?8POV1&NejlXlk;ayjFMzUPs+-`&~PW)GV(Fm0&j{*O-
VK%4f|Fm$EQ9CIvXY98Nm^5L{$Sub?oBir@Vtg3h;|N#>4e8KI<|0-pnNx7iT#3y4`bs@!}zt8F#>d*Juzb`dh$oOtf4&HLi^9D-
~Y7xwwj4Z|p~^1a+!WZA9Zi%E9VE~ySyRrO&cIoxnkn5$xFg$fh0Lg8pmKf)##Y++fRlX#d+mlnf=y8)7_lFDCU=$ZC;uNg)g&VT
)3{K(h$S**l{O}th?GA&=|j9ww{$?DQ~bU4%MWX4~GX-@{vl{-*`7S8Rh$}kHSo3<VsgnE-kJkj=9;OJo{?NgQ)L(1Ob(b7Xa-CA
P59w~DE>F0Yxazocc^>3{Q>+o-
4hw#`gpjp9G4HZZ_Q_~V<bH(w7n~Sr?GOhAP;IxPQs^$ki<zesAtUn=h|BwaN)q@L}H1w|v1B`4Xge+=XDH<5wmb4|m2w)Shykp}
yhgd|`$8he)GtVZXHdMH5+=0b1qmF1p)yj3+c~_+oc$(2btYjPUJ3H}W6cza{opA>xY@AoNw-
pcIxE)sOH+Rl3|2s<ucVvVL$%Zb5jE?Vc-tN~$I}3HTSZ|D|8Hu?;T;2fhnidsaBxfi}hphF*b*yazvHB|5X9|wML=GLXxypsNRs
lE2E2tnw4#(S9-}^1QxGCcf59!mc{ADAmUjdx35KPpYTEG`%jlx`UEX~8`vm@;dqgz+g{Hv|3WUj;4CBP@THz^-!S|}D1-
}L3%WC5|6?EKAygxF-
g=E5UH4PG;1JL3pox#B%&O`ZV5*W+<=(gWOi5T3ypKZCWTD))%zyRhU6WZ<8sm~r^5Z<8t7kbG_PGh<U<`ctHT5wbbp-
}mBYcdwljz|2yK4Vkd#r{=Vwmc;5F4g98%_|L@ZR(efB8<$%h!|)C8yJTL_hu-{)Cg5Mt-2>5Fa4G`%%4}um-CtU4W(-
r#Iz;1PU*Vv<6edQ5U*)|leW66J`f^`dL=CPC^x(SUX?EA+i};eHn9Qs6wK>Qo;+<5W8^=*rptKEMUfVS-
a}QNj7;G2RJ?;uL33E5!SmX@)&66aWQVb*0TIZt<{SNqPA?ns1dA`8<3|d^?p45f2J09te;|#1(GE~a6*xfr$;VY98fiT5mKm+1Z
a*H7~$@0j0Cn$P`?Wzzmm6JGKD-Vj}wEO{!X8sUz=<&RC)hDY}|DVZ>gT9*ORiCz6oBm$%T$6an0HR{*0l|NC-
h}?F^sM(27pHj+^Em6wDlmOm!!``9kPvP;#nE3r8$E;LW0ntoH9jeQ9!c5$0eoqZavE|N0$g-Jnj@qwQd3z_y-wI5;qmcMw6j6B`
N()Iwyyg`Pd@$oEnbRH(S%YJozpG~p=^VI<2RqkxJP%w9J{^;CY^cu5khmuTz=&po*6&@PWiPd0vdb2IbuC2wCbyb-Oa5ijgRY%T
te!R{1e2)9?GE{!q-ORpqBHIBvG;Jk!4&2+&43J_0u80Uxo<B{oB?K%2LeYx+tqx<J0h#U$wOj;B63-
uzT_yFZ~xUMp>BkQAh4XfK9&_7S?cWhE@z+#Q8nwGCUP(sBNM5WoOblJ{wS%B8x!81JR2qg2ey5i<#FRJT{0E#Sd{8>04*U%6^nA
IYT`ckLi~eTq&hAP~UK}82Avy#F1IxQw|P%NW!4SC)ua9rNKL_qYzakSWIT?q3vCo>^4LE4}~6G$0dRQ6yC|O?BecM_~{0qb85yr
7f%V7Tn|CHMHDh#rQuBkF>6!)xTOF7^eO>E?o7Eb*iFY#iz0-
*%UBdLst_HZJ77)>lz?GUYkT|@_na>+7H1v%8?1bc!ZUbQ1DLq5R$IOf92Qdo+<)sM9pS6|cc+CAS+z9L&h@n^OfGpJ?|QKIhRL)
pPU&3;1ZFy|maYh*I%*YUHp_OI_UqL*x+IM;NzouUY?Wz~Yj0Z#+Bq^DRp?Z!di}&U9mmCCyM_XfH}@;E@5?>zEKSkYEXT2Bc>b@
xS?w0MwHpB`{|jjiAD1j6{kVzI@*wD0!C7i3^F;D_0yMDWNKnZ23TRiNu)f*f#=#sdpRYIX#+EoPySgKFd+set5x<1V9Y#r$gEZf
log0%K01l=4{j!P4GV=7t;B5=fa{gE2m7zIye}Jl#gJc)}^l#FxGk~r7pVMhc@vroe#61~M`b-
W&Awd+*75rOt)evaIWCwafI4Oi2H4mhQh@Nx<UyT?u!=()?T}+K@&mKLCDD2<OusG&vVXtPks#G@5*#<&rFKBFRC}%QHNdJLkib1
tg!2Nlgxx-G$z6XKGX$OMUc3n15fhm25X0-w7mn>f~ib!fbMU)P%Q*U^I{}LJaU*9@|9V*p0$P}^_6jj6ua-
x!1<8!v^0#7plxu?wj)^xVmXIwbc8>dm8V7(nafjSyL#bcXx=49%H9jT7Xl!vYO5-MbZpJn9+>-
^Ki(7X$(|8li@mI^tg9Z8d+L({>0Z59e+?!d_YBsVjCX9{SpsYVg=ODNposY1BdTYe}?Lb09fW^FWjx|_;bM@VyIr>X&xmjUV3X$
}U!OBW?_RQrR8@?Eku;5HcY-
D9^f(u!oU`0U^z@|0S^Ph|!G+*+`eOv}rc?*#q#mzsGC%mXE5G*bQN<}KF;sH~7y>UXj(Ed(wJy?GK^25wKDg(Ip3am{adh~~>*W
VYfE`#B<Ekk`aW_^<Hjyv&V)eP~K%Ak1QOkNlh|7~2N}ibsmnaz`@hmm5M5S9RrENQGHsmGOVt=s~jf+fRAwfg~k5gJa^z^P5|8R
;K?;O3g3V5ge>hs9HD?BK@HMAqjD-E_pp6fb42B7}qLhu3cO7b)Ici+|!b{-
>D)?8HimtvL3hMN33jbuo+rGoj@Lydsv^bB)%XJsrp%Qg@C8aP6i_LE&%gPkL8+C5-
yG?*`{(sO(JxY+wht4>|kM5th=As@NL)hba!FF2}~H}yLOVME{}bgcLc~_;;HgNn}>P4{1J4&Mo0_&^w%B{A_6D(%Q?024_I5%`q
qcn;eciyq&AAlu&diH@?xwdWX~6Tz?j^Wf+(V7jyNiN9XIOXzc$-
~xn5FVJ%Pqrr85tNG|`x2=jL;XQC<UGs`q#7)rA|1*Wwg{{m1m4{qt@>D__gcaG0P}RYpb@&Nm}=fuFd#z7RzW_G9ii9+;XgRbE~
>pKwjMVWbOBPoo1<qD&~pkyjSdx~OpuNTb~O6uvw=TX`lUi3AtRNMD#CCcWey51Y<zN<m?J05vo(c?A@FficT|^YAbVa@~qcj(#;
4jrjuhZX9#%BjcZ|S>@LC8dO<Q8d8wc@!Ub$R68BIX3k}o@AzLAmRd4FmociUT#>EloO01!=vtfbi*e_k4S5hW#$PE3454%8#tIu
QAS=RYmMt9_=K$n%fHgcL=$`Ee4_)c$87y%QkyX}K$i*cs#V$1*7r&Jt=5;lCdB{wKV>PQk?Pq&C4x{fC_$N{k-
rtl9kh4P8suvIz2nGd-ovWGa416VP;5)6s;B&0<yap9%E}-
B36P)n;lr0vEB+I{&)LVOuC4)yxtWQQ9PlN7fT69O3NYhY}Jyeh?bB(M*Oi2%&NFv021<9=J1+E77`P<hX=$r!vW7aw}6@ipB=`o
LZXP||V)?}5y6%&kXbuYngThyt0n@ll-;^5nc&8Q9!sZw#ip&aL4l5IK-Lmn_^S18mMgE^rR9@YvXys;14pJLNs*Lg~J|F2+|J-
ugBp3gSW9qIQDj-
f%r|5UM3^~x!Zz=!IM^sbr3T8(>GC)rf0c8q3l=y~fi`F}^NR)YDPtLOVNv^1iPdSL*SHE_uNbrz3#4`(zY439^1;x-
C1P;$nWDB!p{^^Jg8Wfqf`K#+4^+kF2~km?+Q^>yVxmoPDg?$c8<7s1lXh^Vd0?vbHy7C-
Re$KN|E%){3R!Yjizrh<Zi$9kMJ;Oo*rK9j7_YE&zO8y|!hHO2aGqdG=B$kw({VJHNg20i~y7RQ7mXdpFaU&#njUL~qNGpiV)VN~
BJn5RC4Qcbi32o0Leb}9x{ps|3QW<r%n>aF)_0TZS+N((xy`;Q%v_cCodS*V5_x*d<#I1&D@rAeoZ{%i4%IbWyV7n@oVWQp$UQ_<
FY{%|=n8)^MsB3sJTb5luQopd1UEyx~{4tEXAfwmIIL#;vrrDdu1r<j^#oJO29*8Ef&JL2bG%8kbtaU4|)7`1Hg{cLqz&XG#|9Az
KXuY;XGBu{)f9yW4+swhG=i|G;X_-
^CtW70!#g+tHGBfGkU3q5Y{u!v;8%_Y~?3E*MZCQ@ZD8oE)a0FIcZVeWNHxF!oy?Mn@@xNB#sr5w|FK?C@y7o)S<*j9iy%VIx*sy
t5nDWc5uvUu3oQXQfzpg9z2RbBXQhWd6omV;;|UeF5%2GEwWHdjSexW$Vk;ja3l6OPznkX)hU%qpT&1zgRZa2>+0nH)BGjPQH7sZ
!KdE61dYoL0NTH@wqGpx?d&KBtcL%jQ>AJF<Q?BQyPW9Xm;v-
J6GhM0|@AeYtL#j||N;*}x*4AC?CLmVi_0c%|H>!E^AWTxX@9Goh1yr8`;49knb(wNn6?(4fLLJ3|x5iltIQT`@jqtnoU(cGbMiU
HXXjo%}YR8rKtx8>8_^*8^5(`mLIJO$(4jH6}yODJ>TD^8rRdds{s};}2+dIj+W@LS>~*$kP6x9CNKySsP1q@{19ym<FT0^XxIdP
m%RMaIDIltHsUhAS1kR{DE#Uu*BM};ZWQQzE;(tn4c|u4~B@C8{<03<@!tR+RZINJZkd-vezET%P)MIoi0#0Mq_5g6i$Gq2&DZ2%
sg9i$V`x26y6F3`U<HcUe)UGy`}ejCK7u;hdDN`MXRUM?{w``S4M<Jb7ufnL%s0XW2?X?(JumBD!}@eSBZ-
m2r67hJo4%wllB|k3BK90`{d$R%zJ{qF`p!oeRSv;<{RYOYw#hy2T}mnf*p=|AUQUJ+8ki#RAN^}|9*=clO0>diglQE3Vk5dEcBF
ch_&tiI0!$#qF-oAux$t#WH#!idf1AD;}yS|gI|r#4WbZ`GLyt!@{Awl78yB+rJm|SC}g-7rkxF=lv-
4iO`P+fRhsVTp{0Wc|B!v^5>VstwMQ7FPWLkfq5S4SXV@k5BEpv^?q=dDR%_!CpBMZYv%l#Wo=z@>G)e4>CkP!SwAG@Vr5qw9)&0
3MTh}pgLt->qTc^tDz2I+T#Of%|qD2GumGjfn%7KZ4fGX$%TZP~#79y)dN3wdL>aIFGB0g!yLe}-
X8}%zP=+)g3;~QsHYP_9{yMeYAHfQx*XM^%^C;Cr(>H?DKm6JNsiLG5{O6f^aC1H<5oAu(>cib)0xyIZNh@kRr{#Q4qG8?Wn4m6R
b@VJmnd~Tjf!`?bSn%km60Wh=Td;mvWiY>~xfv1hNkm-|hVOBbJ7b44a+$$zlnuPw3*nniNv)CDK@V>ku*3nJ}9H-
nMl6PxTPz=nh;ut>umMI0Y%q?UZM)OYUFB5@W+o(KEB1aFnT)3X3)LNQERfFY);IGjlM3wp3@=l5)1qVcMa0FT=H9`BnzZ{i6Y56
>fy`GN^`p{_4>-Q6q4fO>vKKU&$_b0dbFac7)seFUKC&~V|i0*GYe{G3WioIst5yQh9_>_mk$BRBd!y9NJ&>6nE8-
;T{#J3^>Lg*=+skrv+9xe!G<$emPh!#4{r7(1mP^p?B$wGX>8HDMUzMj)?aqm$!YpRM4z*XZlBx9I1-
!D$2q^QUC_W~hABI1&!wLSc$7m{;*!7P{yUdbSA_vdboVk_E+<y+-!w4QmV3*9Ro^5_&K0}aY1U-
5WUDC~8|OslAC{#;w?19W!OxYw;T77LdO2Gt%uCZfq_=(D5Rx)cp(Vg@-
Axpdq4HJ~FS@*_rQkq4;nSc|*!0&PSVvxIC8PNdurI1;pqkQM|$><^^2KQ|WO(b`KE?e2`oGff!mj<LE15yyV7BjFi_>w?b;`<(`
Wo`H&x_s%}o3@X~+!6@Wk9)x9VwL|Vn3-PHv2*BbxEtdBfIb#DGnkU%3jSbxwFv-
X(#6}?ss#fyh^cd!GEALtufuFUsfF%QWp3(erPS=wpyCjT!s$&a`6)E>g*y66J&gW5P1N8sJfWHdZnBU1APuMWoP^liCbKP<OcH$
9m9FdQHn-
}E8d};89ny?>x{vC{jlhOmaJmz_>XHzV5W?zN@1M>51Jgh;FDQ2>#o&hOxWxL!ADtneRG<JbnzVm{r>!yey!>8xyqP399*dP<lbR
EQ)Qmvl(La+;z<wLbytMu>zMHr&r_{5+Gbue?*)8&ayk`!%URwg9H%#g*`&3hKFl=un~M}r#WOO{aVDG2aUtZC;33D}9-
YyT(J>9eanB<qbB(IQl@WjbRRJ$mZ*p8wfh-$(jKj-gwRR5kBOnQr{X=@V-
++B6F<wnF#w4pu+BjJVD}TyQHG6>xUzTVbu!+{d=x);81d3;Q6^|25uug=d$Jubm3CA6>F=RBu^-
M;jO!eRR#%DV)lGk+LYd2(EE%3te@tzz<0}O=71Jd3LN%0^x@s248*^`CofTv*XbKhjz#l<c-
rq;=kg0Ze&}<+N5eS0IUv((p=BhgOUlgZO3DnxVb5h{CsB#29~T$xi!SCBp)`)lQwkL_Bmm!0Bbb+V9==BP?s=le6a-
X+AJ|#i)sZ&`wR;G*KaI)*ielpM+BH@Q@VkZ3e3n-
k_r4MkXpK7k$k9Oa1EL(m5$9uomw6QGS3c9GaH>?mauqN$yB2;>w{h6PiW$3E-
HIkIt>O}m<qG3i;U^yyPvceU`541c?OE;Rr*)Cl?HFk$3cl7YC7i`<RX_hzq}p2AMNIyK3*t4$uaewtGJa0$F}8$Kw@-
dBqyas$dE7Q>FuzuJIQERw<#cQS(rRbrbx2#HwC1327bOhW(d%n!^d{hJZe53JfPfMH|v^vVuf^UuwLC#uD9R9;3?M10lLV7H#n<
T2XccZQ%0EBOH0rM1!x$Zc?^der_+~S!ZLaTfXW+V{c6!+iFD~9O(*lYQzLIGI{wD83`S^x&XTuji#IKw8@}a_?gO6kv-
16iq5G>;bqL~5?sy2GmEPc^Y^56OluObXARx@o)=AyKcy+X<y2u!1%iWD$C>%~QxGMm0Bu1|>6X8On%>(H|OxL?_GkHV0RNyCAM6
#vuq4_<g6BNxgJ%brH0C@p8Yj_MNCE}qpR|cfp?5-
?Np{~ElVhC$wAbewDGgIlaE*lKXg45)d(&O!INaS2(RI>s2RZLd??P?}+R(uUcTNdGu5$S5-3oTcZHF^PM7A+s|-
n*vOPE$hc{tJ{apKEvCM(COxyhmq)ts<HD+B5bu>gPejXK7ATL?tZ&DU2m(H~=6-
GApxOEz%yZ1ZE9p=At<bwXXh<r06(n!H3vMSgqjadkgPi?$>?a!W<Dc)VoV*1=MB5vZ&;Y998w0*JZmnH6g5<_aO{C-
!wH21Bat<hq4nZW9^WXWXs{VlncLAQCE~>D>gPdXwUKvNe3bhe5Mnd>O#6o3#ogwy)^i>G;hkV$;^ZYD=&eJvw_qrtk$vKKZ{a`a
$?Nigg0ydh-XMA`kEaqZ8KJ3fjl%}LkZq6)pPA)*q?#jgdQ_<yw8D3pGB!40|Bgxe}9D#7d8^v;9QpFGz>>i1jcnPuErtVT&PA4d
{j#Vz#b9}zm%#Hrl+dU@rKrg2Dvc1S14PA1SmGFtOW*VjqMNi^tZ7Tk~xm(mqR_ZKYjGqXQp;xos4NH9I|`fdx=IjzunJ9(1Ontx
QA&<_3|(*tMZ;R_l+Qo40@oq=rK$k)H;{KfX#kmp?dD_ucIM^&0KyRC2_OdO-DKMI~E<Dy$|;G<3E_+7WcSelA@kv?|qrlZEl`yE
6FgM7dAjnlU`S6Ft>jeI`=enbFk1PXx^8V2F&@T$n#No#$nvFc-{~5k6<C^C)DA*e6n}1F#kE^l4$m-
b6Lo4th!?#3of;CSbZuqhyJbT5pG&kIQPe?$*L}!IwYPkU9)nwy{uYu<1j7?0l|4g&&%P~v_5T;H4WQ2Fos4Nasw1@waIsY!!Qe{
hz3gX3D@xFzSZSf$!?kAHZ8ZUxpi=@!)dYsS<MELA9}R~4GC+n`hhnMQ;C<nDn+KpeyW0ks4STJE9laQ<S`<Uiiw}wqRL0%nO`aH
ZgoW_x`+-
QsDrs~ry6C#yLgCXPjU#hKtDxAbaiNP07OUJd#wD8BPF>RWt^vW$89Q(5!nMAp@`#hWMo#ZpNlrLJA|cWF+9)b=zcLz7}>7^MN_Q
3@WN#OW#mf|$0${os_NH8>zBYq9lcPu9(g;+qT?o+Z(^~g=t7ZCJcH9upadfQ$%*kmL_Qn1z}oTkz#wX28Y^IERA=F+h+jyY=Ez%
m%d2F1B$7@UfAO}*->xf-F6o=mq_Se;Ij%88BbJ`+L{gwrZ9@uu=+w-
@IuhAm8T?t)baM$k8ntEZsvu8*a1oT4YS)Ob9H<X*Smg>9_?uFuT?E1#$yE>y?P)H`O+6jKndf1Cj{Z1=zlJqBee=eO?24}Yp;F%
(oucW}gJKxdL}6c4Jq?wRfwNWiKL5e`YvseHS_x?RJg)rRbEKAM_^BWxNG7Veg(WB9HA{B-HOz5oHoqCv*IX;Uq_-
;BN|dB0^gbqNsVWhHq~<M;X>5?TV%TTrk2>R?7Ue(e$rI_r#5;evmm`#>U+R8O#_QXTL)5c$NB3qpl>-
WqY=p?@YgXFi4D@gj?Sooa;Qu4yFG@30a*!Cami{dQuoE-f_1?TSvEddz4MNu_IwK{n<}_`3Jx_AF4m*yAcz0}o2cRv!i`JaQiX*
>)vj3Td>$sR;$+yK3r3obJU#*#a<)?XUzTT*4+L&5~0D-tDmKq;}GI1?v2g}y+w**xW-
O7C0e8CIVoe8I7^kk$ayru(>ywU=<nZ;I9<9?DsIevQm60~E2SEc1N*aWeIji=`2B_|`Yd+a$vY2F-
8c|a7%ny6fF8HX|(r!f6VEO59<Op-dt{)JF$aF~Gt?2ps^L05sm4SMJDbMZZ(pK^qJu7f!fM1!(54v8hz`5J2lR^X!Z#vU=PhJk%
CNoyH2b@4@YZ^ulSW3N4ytq52|8YMxrDjAqrNQ#haUe4JM0v`FU=4I<$$e6nJY@o%jn79w?_HkYcF4BC~`b{Z&{0GauZkz%7IYu|
umBY!vr4UB8z!3~MiaQL%t%`t%N<Hu_6i6rrvfHk0Q!*2Yc^qOf#OTQf=682y6NtdpF!L5x*=ck#-
@m`q^`4PBP9Dw}D{omfnWzjO#_oBvhA2lNk8F`#&dOu}?(xW&;0}q>jzT@+&VI94)HtS$$!OsVR*hHZkUIqslD9{%%>XIG|8i#RV
^MpOYs2Q^rQYm@&O?Rt)g1%H-NRtM%+E=$)XEuIbk(Uo+LO_z*oH*OgB=yY%gg=_K}VGZZz<ATR~kI_eGn?;-
{Q$S?_g4JJ5ud*bE!!Pn{L#*sALp|*AMHyopLO)cFm8I%OKz4m5X;AxEj=wLF%zK;L-
Ek(9Q*~m%fc?hGdY8UkS2pv5F>S>xNNrrmUx2#G#LkJ&cK3jYodv_xw*!&6{DKDZkuGQi}Ja7F8<4f;TEtJ&0M^_{<L<OTMq={fR
VrV=AQsLHN!Fhv?3BNV8zF1!x)8da~E)k(hnoj7vs{Q;JGbDUkXKE+We$o&zyy_Ui+DNAZSRp|oY;Q<UgXK*g1sRCQ)qf$Pd+VWh
}Ugoh?5;HA8jA3%Y<(wn_Ipg>(mYs>IzGC*X-!~KwP*Mf%#d)?k3NE~l@hTi2D*=@iBwA=9GV2`{CF-uWafB}5k?V>_<;FH6jW%^
p;G%he_Jz>$z!{hm_KOaX2vD#LvPQae<1tAlVv4NQMomyLdtAAtCe@Q7c4rXpH;RX2)zH4;-
t3GrgI8U!t;p?l~oBk?NsKYgmV5H2GOnX6J7IDv2$t`HHGV-
}9kJTzIY}&3ZL4%<Cy4NK<NrrBU+e$Bd5lEq}Rqj*yxyPM3(Jv`_D;u+I|KIkouHYWp=CV8{0;1^bm}g+=S2*c2RXQ*di@x}WWuf
3AFdufp4-1?_>Qu?5I&K+dm>;P98dC0K@-
xNX`B7RV3oO2_DMYT~T?W;^lzJJEv^JdpO_<9)3ad(m7W#d;6arYWsLfIP9ZYqxZg+GrapN|je^LsIt#PJxZEC8>8ud@kl}+7{OA
vPG-prreD~!3E)Ebg`_|zXeAZKJWii{MUigAK3X4A^HL`Y@Rd2$*q=QTMVCQHGAV!9p%h&gbaF)rYmKs&f0wx=C!T?hHtN5U+6&1
U?22LXxnD5f7jQ1fef<|YAcc%{4`{y1X5eF4w)s7P7uJ67m5d5G|aIfBF|4*#b&yTgwXJjFQ}fjFjs^EfJgWYtknBFC2-
>Vt}31n-Z3yqzQy6}zPG$Jc5ClJ8xppw-
`QsIzm_Dd~B3RXYOtRZk=;Enav(=Okj$3}z50eqS?rcZ@Xq<?pK5Fb+de!13enPS()Lm887J2>qTBs>;dpo>jI7jK@dHzh)?mDa<
#LMd#yPD+0*kHGETY<s!-
g7VfMFEI!K_MtDbE8+;iNTn?zRBC$6|d0*RlHoA{xo)S@+maK+1Tpov=Ob#=Nv~QmCYKcb6@%Z^ae6K<a+U>7Cg!cWm#yE`U0vsD
?fnDJ_p>HKjH@tzDfpQa91S*ua*ld2AE$5M|<9@I+E#ck?CN+`K5gj=MrXb8wSu(<0HaavEP=pHhe-
50H0{T4Cbpztn^up18kP%<41PPYxREGw1&9!eT<X!*T))_4c^^LUA>*FJ2)<~oX7p=1Zeu0I(i*~6X#?_ph_V}tnKKV$5)R}LNWa
6+Xer<k1KRoy?R|Pq+Y5dANANl5)S-
GXIdcK3Sp4_1QrvX`3GK<q1(F*N<yz(3$jNGUm%04eKmP!*$cOZF(_kB$uhQ4ckKVsNhpJlC9+S4M2hnHsaD6;JI!Mig<4#b7@6l
zU?-
^yJc!!$&O|1u?>4*1OI{{#xEK}oZP2Pp3E2VDkT>mxudC?<)j>bs}?L4GY4_<&Z#B#L8MuAKI4XlJi@L`nYQT_V(l3?O|m>Bup*e
jM+cJ9%~rIZa8jn=gucesSE>6hir867MN?_qX&y#Q<|m1e2S{Sq#ygCcM80LR$&+WkWO9vW*-&-
5#mvE!@nOmKrPbbAX$X21=&=RYv-E8j+KLrf%|)><Df-JA~VY3~9I=#gGLzc(GA&Gpd53Tg=Upc;0G|ct|gXx)N<SIg`&nNb-
B7IR5aUovPzNVYQR5r0Z#Su}E6_DG%xbIurrUh;o=-
Ji<Ob>U=*6qN&Po_#q<U?NqDCm(iSip9!9uh}{k43XFY!F9WNw!0M|p*pX5PTtQM9ZO+R1TwnH!iLd!}6F%z@sFnc7aN*W)jJRoa
>viW7B|*UJdGsUFB)|N#nY)h!@yc{<nTvt!y?eVMp4M8TtPajRP@AKLC=J31^nQj8YOB(i=hcr_WiIg}q&T~dQZc<1nm#TaGb?*B
W}5%PMT%_5`2n8j)FRXY?kmF1(udOvN}O6jt_-
`#s|Ar1CRopqunhMJGiaUb{v5Ceo0PA&J)PLc(K0%Js@`B?nDy3$O2hlVKTehsJgzpTH+E6qnaWYCkSF!UL14+sV@4gyLQgc~EsJ
VaY_fils;c<5cg`hOJ^qz*B@EiEKtpw0osa$bKPE4D&=GDu2_tsTd^(tB^%;z`p91q+`xlqBS8<12jK7%SP%{o49^$b1sXz_2hH-
6iZKIxDCo$u5&Ba>9FHC^mj1?ZA`0YJmln5TI4|pl^ldjSY&YqPNOgDz66&^z(fYbhTw{k!L2I~3W)gfQ5`ng!NpOANiX-
%AEdyq6NqkA1QEhkEsKb<#e3`b}n^k@y@qi_QDB}VR!!;seMlwfVmgRL7LdUy0AQ=$$jm+6+Q=%&8vu}Qs0US9$-
a^w!CNfRJ7gp=0-6|#K_rjS8wR5}kez-`FLvqC!%_>nrHF3R6mq4K)6Tu<9!&s?GPzeHzkI-
m#!+(cDsElNeJ6J~EP_??~@3aR4bZsc-$;<s$R=Z4>PQe`7y-K-?CG4ppsUECIM!{YqEn`=>Lc`aV&f5SP1P+j~$CM-PI%+P-
1@6t!sJlr01I+CcvO6AP#Pc{+ZGy=RRtz0cnI``B>L3j0@j}-
`@7k?vrwu7j<U18Wq&*OuiBm3A|1q}!}on7t`g;t{%(NJ_lFKCbrFurSM&w+=8{PJ2~{(Mce|GYoXfOJa`#U>9+RudsaL7@(Y7MA
*uRu_hdGmv&+O|(5h*>D#xLw?*d#>tUBd>OAr=?a^T{xMb6P08s78@rkiZs3?XWSDn3jU^mG$*AhzHNqtKr*~=*`e_K?PdK~Y4tO
E-U#fxGe^}}q`CQLv`sN{nu4Pw&p9F^P_{@eMk3n!(nO~-
aMVN+Z6v5)=R0`{|l~GS<w>$O9(SWrcLs54A>psjjAVi)5kHsO42q$o>hi?zivkF6=fMcqoWp;+vj7vjBr?MM+SVk-Jxscy@37EW
7PN^}5eTPBsb0Vq`I^+lQ2V$Y}|D&wWx@=_Fe2`;zPMV!UBV#XgvqVdoQ9OX8B^Bm1bpJ~QV@QIhT7YpHdWy=4+xYqc0jXRT0F$W
t=zcL9a(McGZfl}VGC~N|SbVtf`dkM3B~&91I`}+0{%E7egT`o``bP>(#BaIW8a|;>c9DDv8HO6RM7%Daj)qDAKCs`%9T4R9cc{t
U+M0dllAf1EEX2RtLZ1p>wMC?K>3e=)m)b3ibl~UG{F{2}$eQ$ro(#W9Cw8p7E%8MnqyU%ROx29dyeswmgu$!}wB-
G<50lwTTQiC*;)#Rd#+KnMZ3Me02tdg;t`)weJHKx2HfcIy+-ZJwmzSPX|85u8zo+z^uAwavVmJhL#;BWRhks9{={M-
BqKmE;<$L_cGXLuGkI>7`eCV|g8J~+68t2Lmap{W4RDHRp)E1er!gIopN@SojkrX1!^-
{#ds&COEN057EqseoczHOLla8Z<ehR7`1x1BB2<Iv1Yg<F|-)~uj(o@are-lZI5J+?jF8)VyOp<#|eFo>jwAR|OZG#R5|#%ka{s<
43PU)Be6&Xibhq+58X_IY1rza90y!tYCeEB;1~2So<}_DV^cE3y6mtqzi2p_fp&IiJc+lxLLBXa=iZ8jyt!*26m*5R!#ueUsI~5k
blnTF?IxM7#>;>5%VGQw5;yr3(*usKj@K;K#W`G8|rRiT0D%MEWX{&W{#iBlsAytWMtxKyV#!mFg_pskI#f`)gl?cL3Zk*ZXSYtp
L>Q7zf-y%^!;DQq_Pwu-
w;Ukavk7R6pKBC?ln(?VNIF%n+oDq^gM;1D{@eR(P3it~r=otU1^LV8PFLbMRCB5UPp~6uD&Fd5TU7QXY_USv?simhTVH&8^Ba0}
DXVxIGQ>)hu-XSN|z{!Qba#_9=ywLV8Z10$~*(C2D$aH|G`AuS_YsYF|K8fc>=TIC2A|Zz}OLZ(2ah-
{N+VXAgq@E_41ED+mVJ+?f@B=pO}MeB-
1a!Qn#A!W!o%yD~tGSmd|X07OYT`C>$^G&4dS@(egwQu%9NVjMUP2U6iuAuO(Rmf>B0_!52KVLBbN;g(Z!^hLTFLn?4wqR)GtM|u
4D$L!$^a|Kk*MWM;{*?9;CEK=UFrT-
1M^|;PwnaY_XdL#ZwHFF=+olGYY`{`gx%BH~<y>a)OTRq{r={%RC5H#{VE`|b46CHS_CLeT-BJ?}@yq{v!JbdaRs)S8f5if>Ah=P
i*Gi2z7K!-
_lewfb&Ucms~Xs&{#vvtekAYp$|wG8LT4m0Kr*$m`nF=Mt^Hh0K@L?%vSMspLP;jic|&8*c@>w|K!E!Ch3CRyzsuDo)gj{6wt8;~
g~&4e#^OD^~`S>u&LBt@h9VASfJ%d6PJ>}ov4Vr^)GSA<yZIQrUp8)Kvw_BGRZRv(>y?EY`Km@}|(VT@ybwR6&l*B%ch3p`u@)eV
M7D*BpQvnS0yAh1s{<x(RPYwTgaOKJ%cj4QWhOX-
?<tydwj5hWNBcffe4{=#nyTi$pn8&OG?oiQTif>W6&tXZu%S@KxZUMTlx&0aV5%V7Z>NScO)c%=~RLkN}LEClZZ4cPd7Kxqb<rmx
KB=olE*B5k$GgQ$oASVEuKVgYLIua!5M6dJp)$py<SR{#opr6vj0zM$3>UQI-2Qj-=xS$eHbda($dL^Pd!LQP4mzB-
Oq*In4Z^{GLjSumF~hnMJNAcENB(8hCqYmk(mE_81CgX;t1Hs6Cx3dZaPuCXzZU^xv$umfnpOYw18H7fz1HBK-Qcp4v2O{WSbN8|
~_ABUHqSRER}0bWFSIv`Bp{*t(>4%s}<7_Gq+>^&hZm{5R0bY<_8Rgjj=2#XIM8i2D?NAhD0X!&s>4+>s;tg(Y}+j`U>vBd1i&|H
%lj#N8FKNcRs4SvolazR^;=S|L;CKdcDmS0;zBu8(Fxd|sw(eR_x^;Eg8A84njceqWYop+<b1|d3wcxL2xU1_=&JFQhn+p;Gi+70
d3(r7hiU4nH8t0!~z4U#4vscV{9@$CkOh!y>&e@vPg=NN_;taLxwUOJCP>fdi5Iq(3RE#l@k%9=opB)1(}zsy$?dR&pT<%R!QWA*
{gQ3R00<HaEQp-w^21AKMVJ55ERfY@aX+=+(12t0yWd~SfIYG%$Je$QX3e``rp<ECAA5d1o-
IC<>WX@9KX`yTu?xj+S*%sZfD%P`z*!zV9IGv?O{jmP&4Cx2EHM4BCcj;n|?Da=N{8)=O9h(A6EbaU(;1z;x{Xz5c})c(SHo&FkE
=6=v+=d_J0ca_S?d${p*4OVaa&q^+FMYpLjnEiG}+NP$dn63|uNbZyU7$aL>XVUg$#(0tRvW8E~4e*>UJ@3!icj5^~I?4YiCRR;t
q@j!H?w}CV#}DEedujv^j9cl5p6-
giUbFHk^nPxNBE=Fq@R(`^QJ+V@Jg3Fndt9x4i?>*S{QmuiWa|byi|K1lK+nlAyh1SJ3L(8CTr_uH2%EP0L0y3(pg=A2h``yGejY
m%QwI@pLPO@MG;iJgGh(Mr`)1iVAGP{>9B8Gb(eg^2xBhyI!uo$bD-GF&Epaq2+|-
UY`Roq{AC<U!n)b#rv&_W^c;QSH^*k42zVaiP{@bgpe!<g;FVU)#9WP&&kBo9-
%O>b4rs%u|YG6Je&;9o)p`j$$WJ`P368t`sIMmIqAq~)5U!I#&h{~GU$9^bXd@4(JWAYw&Jihg1YO+aSdFnpW6_I@{VkF4Jt{i28
PC=miNc<6HSM@6ShMQ3tN7IVbBeCc|l+<QFvK6?nwrKqY=mc+k_#8N}Nc#F|ZvPVHj#k5=;HW1V06?jS-usRAESC_e9p#Yf3sbB4
IfsSS7tOkZQWrOWZf54<w750f<A}z93FQw$%9#$KRd>s_?nl!}>Jt)d^w{*6Pn{p-
GLQm;Y|V31YUd`7QW(T%G%p~N#=xmX)X5^d3<F9a@Cu^ho}8h*^T8izb+u9GM6G+eSlX%KR)4d!pt@h>Kw-mxLYZ#!IN~SUg+b*h
t?|~UbU@dWYR{F})y?1W7gijL6m@fxjI42l!3&PMK;bCAPu7PQC1u9jVG1w{W{_gbqAyZj-
4H%Y#hNV$sK_N}hGp{_FlFZ!s@rH&(*ezZNM1b?DVsfVBtU(IXtEH%btsOqHBJ@742FCh@wedF+|OGG<y3xBLKMHOeR)I#NdXz!A
K5oID_p`3OK4{huuShZ@S&9uL?0q2z}H`C5faEESR11$(hu1ArRqNFbXl-BSh7MI^EDin?po1Uydm1_I}s}hVI3slx5*rB|M4{BW
1*~_y68->-2fm8KNlZAP6L0RP%Y=GxvTd+fUq1wJA2VtHdliBFUV{SAc26l$jm&b;Q-
_|4q4fc>+No+=@NfD3AV5MP<ZF5C!z@~f#%06`T32s9i!YqY|FQa{fY?|z)YPvUZ0ki8Bl%(xwM4|t&#Y8B1o}}@2mXF)3eH(4wT
-uncibT%LOwZg$dh;tgki%+4*Dz48lrbl^jgHksALfKK=`q5vowQ>v@hFv+gKAQMwdGZ$K%8*w=Ffno95MX7>2Wz=^c-
`ZUG@>sRM0_kB6a%rJ8#Qa!kd@@Hd+?VQ}Dva#h`u4_-qwe&Z}$tjlOVC#;z@nKp1>hCYN;M-
~GxIr(7M``v6z`FvSY!?~id2WlYWRg2mIZW6L=u49}09ZFGLsH1a$~n+@j9PK|lOAm%l`)Q5OrwI2t>KIMY?q_!mB_wH=m{j*G&c
0iO_s*-KA0B1+@R%-Faqvy8G-
Jo@hF?;7`+ncaDZi6E{;KVoL(?&<LRL%7YkcNZtTgvSvk7FJjr)?dy?|+x2a8K$VtTj6bV*u0i3^w7H`;?7r6c=DWv>Xf$cP@r41
URtM@OgKpr408>7$U|C?20ybDM)+6|76v|9;=5GY7QY5^koE-r6?-~AvNVxtW<FTLleFJq^s&-Z$Y(h<R%NvOm)e)6_d>T4z4H#-
TYQ;DY*CO#ba|CtNc?qMzb{aqk3Xc80BiF%I1TvR|~h2u+VAYhcWY&jo7j80=YUY3s$P(|k<Q<}7<eKF_4PSFMMni9pKB#n~pY~*
1dU8{QqLJsr?5R*c(kars2DFC61aR%1&1UQxcC{S^|gHRQPV%)ur_|;*Xy7J&M<6~KT`-
t<)*DFyMifC)~NkW*(%6LQsIMIQrFcf}W?uKah9Z^uvcJI;3>Zatjy~dIEiPYcl3K|5N<}NxQpvcd_Z!wC`7l#c9iC#sZaL#+p+Z
cSFnb@oHp40#U^^U$EYF*EB00Hl#0jR_TA|>q9vBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(B85.split())))
assert len(raw)==74280
assert hashlib.sha256(raw).hexdigest()=='1875334fc1f714b67734a5e48981356b71a8564f57233fb565ac94b5b4e5d30c'
files=json.loads(raw);assert len(files)==18
root=Path('sq24_polar_replay');root.mkdir(exist_ok=True)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
 q=root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
print('SQ24_P72_P208_COMPLETE_EXACT_SOURCE_RECOVERED')
```
