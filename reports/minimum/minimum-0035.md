# minimum-0035

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# NOVA24_RECOVERY_BOUNDARY_AND_TRIANGULAR_CHAIN_MINOR_V1

## 1. Determination

**The recovery boundary is now attributable: the authenticated immutable publication itself contains the malformed recovery block. It is not merely an error in the lead's manual extraction.** I reconstructed the exact 32,940-byte version-2 parent envelope and obtained its required SHA-256 `e415baee38fcd56612393d45cd7c966dad05dffa836c3659ace5ca13a2b1490b`. Its literal Python block is **12,086 bytes**, not 11,977; its whitespace-free base85 payload is **9,073 bytes**, not 8,965. All three original modes fail before extracting any source.

**The requested recovery of all four original source units was not completed.** No bytes matching their four pins were recovered. I have not substituted newly written code for those originals. What is preserved completely below is the publication's actual malformed decoder, both correctly pinned historical transcript byte streams, a new independent conditional graph replay, and a new physical-volume theorem with a complete exact verifier. This is not a repaired successor of the missing 51,912-matrix checkpoint.

After resolving that boundary, I proved a stronger, scoped physical restriction: for three actual triangular facets forming a two-edge chain, a three-by-three principal minor of `I+Lambda` has a positive, explicit **common hull-volume lower bound**. Combined with the same actual matrix-square identity, this gives an exact rank-three Schur reduction and a conditional rational denominator bound. It closes **none of the five whole tree forms** and **no named C32 type or root**. It excludes the explicitly specified sign/volume chambers below, not an entire combinatorial incidence type.

The five-tree certificate theorem remains inherited research evidence; its 281 numerical certificates have not been replayed here. The graph consequence has been independently replayed conditional on those five forms. The parent states the intended certificate and graph scope explicitly.

## 2. Exact source attribution and observed failure

The two supplied files were present at the initial filesystem inspection; no old cap9 ZIP, original decoder, or decoded source files were mounted there. Searches of the supplied text located the source names only in the literal parent. Tool discovery exposed no Library search/read action. **Library availability is unresolved**, rather than established absent.

Input snapshots:

| Input | Bytes | SHA-256 |
|---|---:|---|
| `research-journal.md` | 3194061 | `e6c0eae5fa315532c6ce66b9b3a1c8f98db845c12f05d49f5a2fd7e9cb0d1915` |
| `source-research-journal(4).md` | 1737149 | `1e54e3291077a0f4f0fe4588bb6793b823c7f904caab1c1ac8712bde2c014722` |

The exact authentication recipe is important. Extract the Markdown beginning with `# NOVA24_F9_FIVE_TREES_25_ESCAPE_FRAMES_V1\n` through the attachment's EOF. This extracted text ends in the closing fence without a final LF. Append **one Markdown LF**, then serialize:

```python
json.dumps({'version':2,'result_markdown':markdown+'\n'},
           ensure_ascii=False,separators=(',',':')).encode('utf-8')
```

The result is exactly the required **32940 / e415baee...** envelope. Extracting §8's Python fence without editing produces:

| Actual published item | Observed bytes | Observed SHA-256 |
|---|---:|---|
| Python decoder | 12086 | `7eb8d073300a5a93e7d2b4b108616e74baf1e988e2fdaa9ec00b78f552ae1882` |
| Whitespace-free base85 | 9073 | `72d3256c5086ca308d60875c797785684917ae4214cc122cdff30b039ecb9614` |

The Python decoder's own assertion expects a different length and hash. Direct decoding of the complete observed base85 raises `ValueError: base85 overflow in hunk starting at byte 890`. Separately, its first 15 characters, `c-rlN3yjVc(BZqz`, already yield an invalid deflate header: `invalid code lengths set`. Thus changing line wrapping or blindly trimming the length excess is not an authenticated repair.

Actual executions of the published decoder with `extract`, `check`, and `all` each returned **exit 1 at the payload assertion**. None reached coefficient generation or either independent verifier. This resolves the journal's earlier provisional attribution, which had deliberately not blamed the immutable source. The conflicting claim is specifically that its literal §8 is the pinned complete 11,977-byte source-only recovery. It is not a demonstrated falsification of the mathematical theorem or of a separate, now-unavailable historical execution.

Two historical outputs **were recovered byte-for-byte**. The §7 transcript is the pinned 1,906-byte `full_recovery.log`; deleting its first 14 complete lines gives the pinned 1,448-byte `frozen_recovery.log`. This is recovery of recorded output bytes, **not a new execution of the claimed matrix proof**.

### Every original source/output pin retained

The following are the parent's declared pins. Only the two historical logs are recovered to these pins here; the original decoder and the four decoded units are not.

| Original item | Declared bytes | Declared SHA-256 |
|---|---:|---|
| `recover_cap9.py` | 11977 | `5b568871fbf047909ed0c738c8f4df4fc61985d99492bfb14e5f7358d18e8c14` |
| `cap_engine.py` | 4681 | `74bd7575284f8729c038c8e9aaa3946e7c4f562448a760bd9a8010031840bbfe` |
| `build_cap9.py` | 1839 | `fa9f62d0e506330bb71751d8b42c9115f39944a6ce862a2674fbe34485289340` |
| `verify_cap9.py` | 6162 | `108b099264c362fa80a69362528266ec223e7a4407ed9011b7f951367957b5da` |
| `dual_frames.py` | 4595 | `e885a097ca6c2e69979b9a57900a52ee136fb95cc9821891350cc328f3095a6c` |
| `cap9_exact.json` | 3737691 | `6ece23fec81293b1f67e0b7474c8bd7f91908e5c8fec879738dbc6f443b75bc7` |
| `cap9_verification.json` | 3701 | `471103e6b93d245a0320b5b0a747cc4ddee2025f7be368bf16ed23921319c9ed` |
| `dual_frames.json` | 7688 | `b174fe2cf9a941ef168acb553ef9bf5d95595a637e6844e5185b688f6bd84680` |
| `full_recovery.log` | 1906 | `a7875bf243088527f497dab1e9e2b6a4acabd7187f0dfa6576dc099574437516` |
| `frozen_recovery.log` | 1448 | `0ad986b4f93604487de999070088d234cdaca4259177e372637f6ed472b4e61d` |
| Intended base85 payload | 8965 | `a287bccf2c4b9c4a6182627461847c3831c81c3c0167027f2a305f82f40580df` |
| Intended decoded source/input JSON | 17810 | `11612fd5a7fa40547f4993b3bf27dbb0ad02affb8fd565c83e82b8773138c53f` |

The declared independent stream hashes, in weight / scalar-matrix / leading-minor order, remain:

```text
bdbf7468726e5a46bb20673ceca19a6ff02e9ce1a6e1cd3d1a900297a78562b5
adf162e147077136fc064e3a438885af2a5228366f457f1947e1f1f157618fc2
3c26b93641ba6ddc53ed3aab4fbe4220fe9130573e4693a59b7ac21305d5fae7
```

The parent's antecedents are retained without reauthentication here: physical trace parent `minimum-0024`, SHA-256 `b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95`, declared 57,975-byte pretty version-2 envelope; and `minimum-0032`, SHA-256 `3c4347c3beb52ca549da23ff0b0eb42a85251a52c2a920bbf1deb68b4b73fe4d`, declared 17,651-byte compact envelope without adding a Markdown LF. The later coordinator universal285/quad-ten proof remains a distinct dependency, not retroactive replay of that second parent.

## 3. Five-form theorem: exact preserved scope and averaging argument

The five remaining **TREE ordinals**, not C32 map IDs, are:

```text
253 (0,0,1,2,3,4,5,0,7)
266 (0,0,1,2,3,4,5,4,0)
272 (0,0,1,2,3,4,5,5,0)
278 (0,0,1,2,3,4,5,6,0)
285 (0,0,1,2,3,4,5,6,7)
```

The ordering is lexicographic on canonical preorder parent arrays; `p[0]=0`, and each required arrow is `i -> p[i]`. The preserved discrete certificate plan is:

```python
rows01=[246,247,248,249,250,251,260,261,262,263,264,265,
        267,268,269,270,271,273,274,275,276,279,280,281]
rows02=[277,282,283,284]
remaining=[253,266,272,278,285]
```

Every other excluded ordinal uses row 0 alone: 253 single-row cases, 24 cases using rows 0 and 1, and four cases using rows 0 and 2. These are coefficient-row indices, not geometric apices or new centroids. There are 168 extreme vectors per row, hence `168*(253+2*28)=51912` matrices and `9*51912=467208` leading minors. The numerical coefficients themselves remain unrecovered.

For one actual own-centred body, let `omega_i=A_i h_i/(3V)`, let `c_i` be its actual facet area centroid, and set

`Lambda_ai=3 omega_i(1-q_a·c_i)`.

Cone integration and divergence give `sum omega_i=1`, `sum omega_i c_i=sum omega_i q_i=0`, `3 sum omega_i c_i q_i^T=I`, and consequently `Lambda Q=-Q`, zero diagonal, positive off-diagonal entries and row sums three. The imported trace cap is simultaneous: `Lambda_ai<=c3<10/9`, where

`c3=max_(r>=0) 3(1+2r+3r^2)/[(1+r+r^2)(3+2r+r^2)]`.

For row `a`, the closed capped simplex has exactly 168 vertices: two entries `10/9`, one `7/9`, five zeros. Put `w=9e_a+10e_i+10e_j+7e_k`. An actual row has a convex decomposition `rho_a,w` with total one and `Q^T sum_w rho_a,w w=0`. These convex coefficients are **not fitted physical masses**.

For the one reciprocal metric `N=M^-1`, put `H=Q N Q^T`. A weak tree arrow gives `A_i,p=H_i,p-H_i,i>=0`; for `L_i=2e_i e_i^T-e_i e_p^T-e_p e_i^T`, its pairing is `trace(L_i H)=-2A_i,p<=0`. The parent describes integer certificates

`B_a,w=gamma_a w^T+w gamma_a^T+9 sum_i mu_a,w,i L_i+9 O_a`,

with `mu>=0`, `sum_a O_a=0`, and every `B_a,w-I` positive definite. For two rows, the offsets are `K,-K`; the 45 upper-triangular coefficients contribute twice their value on the diagonal and their value off-diagonal.

Averaging **the rows of the same actual Lambda**, the gamma terms vanish, the offsets cancel because each decomposition totals one, and the escape terms are nonpositive. But a weighted sum of matrices strictly above `I` has positive pairing with nonzero PSD `H`. This is the contradiction. It includes weak escape equalities and has no rank, metric-condition, or positive-volume cutoff. Correctness of this argument is distinct from having the missing integer coefficients to verify its premises.

The reported numerical environment was CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30/SkylakeX, Linux x86_64, one process, one BLAS thread, no randomness. All declared non-default locator settings are preserved: starting margin −1; zero free coefficients; escape multipliers totalling one; `tau=0.05*0.18**outer`; at most 12 outer rounds and 70 Newton steps; decrement tolerance `min(1e-7,tau*0.001)`; positivity factor 0.99; Armijo factor 0.05; at most 60 halvings; symmetric solve with `rcond=1e-14` least-squares fallback; margin threshold `1e-8`; max-absolute-coefficient normalization and rounding at `10**8`; acceptance only by exact `B-I>0`. These settings do not reconstruct the missing implementation bytes by themselves.

### Maximal frames and joint complement preserved

The complete literal 25-frame table is embedded in `recheck_frames.py` below and checked against independent enumeration. The new replay obtains, in ordinal order:

```text
ordinal   optional pairs   retained subsets   maximal frames
253       7                12                 5
266       6                20                 4
272       7                26                 6
278       8                19                 6
285       4                 5                 4
```

All 592 optional subsets are exhausted. The 82 retained base-labelled graphs have 25 inclusion-maximal frames, at most 11 nonnegative unequal pairs, at least 61 negative pairs, and at most eight rooted escape trees. The checker separately verifies DAG status, every parent choice, directed Laplacian cofactors, the 286 canonical rooted trees, and the literal frame table. This is a **new conditional graph replay**, not recovery of the original `dual_frames.py` or its JSON serialization.

For the joint application, the two inherited primal candidates are `T=(0,0,1,2,3,4,5,6,0)` and `T_alt=(0,0,8,2,3,4,5,6,0)`, with the second requiring actual edge 28 and its proper sign. Matching selects some compatible complementary pair, not an arbitrarily prescribed pair. Terminal triangle 567 is a nonroot cotree leaf exiting across edge 57. Its allowed template labels/depths remain: 253: `6/6,8/2`; 266: `6/6,7/5,8/1`; 272: `6/6,7/6,8/1`; 278: `7/7,8/1`; 285: `8/8`. Thus depths three and four are forbidden. These are cotree depths, not full-dual shortest distances.

## 4. New physical theorem: a positive triangle-chain principal minor

### Statement

Let `A,B,C` be three **actual maximal triangular facets** of a convex three-polytope `P`, with `A-B` and `B-C` sharing two distinct true edges. Use the body's actual volume centroid, its actual area centroids and cone weights, and its same physical `Lambda`. Set

`r=Vol(conv(A union B union C))/Vol(P)` and `K=I+Lambda`.

Then the whole continuous realization domain satisfies

**`det K_[A,B,C] >= (1-r)^2(1+2r)`.**

When the three-facet hull is a proper subbody, `r<1`, so the principal minor is strictly positive. This includes every such chain in a C32 body: its union has at most five of the nine actual vertices. Equality in the displayed bound is possible when all three pairs share true edges; therefore the quantitative bound is not merely a loose sign test.

This is deliberately **not** a P0 assertion for arbitrary facets. The exact physical negative-minor example with two quadrilaterals remains valid and is retained in the verifier. The journal's general P0 warning is not contradicted.

### Complete volume proof

Write `d_i=3 omega_i` and form only the diagonally similar matrix `B=diag(d) Lambda diag(d)^-1`. Its entries are not new variables:

`B_ij=A_i dist(c_j,aff F_i)/V=3 Vol(conv(F_i,c_j))/V`.

For edge-adjacent triangular facets, `B_ij=B_ji` equals their actual two-facet-hull volume fraction, because the triangular area centroid is one-third of the way from the shared edge to the remaining vertex.

If all three pairs share edges, their union is a tetrahedron and all six off-diagonal entries are `r`. Direct expansion gives `det K_T=(1-r)^2(1+2r)`.

Otherwise write the successive triangles as `A=oab`, `B=obc`, `C=oce`. This translation to `o` is solely for determinant volumes; it does not change the mechanical reference. The four rays have the cyclic order `a,b,c,e` in a strictly positive section of the tangent cone. After choosing orientation, define the four positive normalized tetrahedral volumes

```text
x=det(a-o,b-o,c-o)/(6V)
y=det(a-o,b-o,e-o)/(6V)
z=det(a-o,c-o,e-o)/(6V)
w=det(b-o,c-o,e-o)/(6V).
```

The two possible roof triangulations give

`r=max(x+z,y+w)`, `t=abs(x+z-y-w)`.

Indeed the two fans lie inside the five-vertex hull, and its exposed roof is the farther fan, or their common coplanar quadrilateral. There are no other roof vertices. Actual triangular centroid integration gives exactly

```text
B_T = [[0,x,x+y],
       [x,0,w],
       [z+w,w,0]].
```

Consequently

`D=det K_T=1-x^2-w^2-(x+y)(z+w)+xw(x+y+z+w)`.

If `r=x+z`, substitute `z=r-x`, `y=r-t-w`. The exact polynomial identity is

```text
D = (1-r)^2(1+2r)
    +2(1-r)(r^2-xw)
    +t[z+w-xw].
```

If `r=y+w`, the final bracket is instead `x+y-xw`; the first two terms are unchanged. Since `0<x,w<=r<=1`, `r^2-xw>=0`. The final brackets are respectively `z+w(1-x)>0` and `y+x(1-w)>0`. Every remainder is nonnegative. This proves the theorem, including the flat auxiliary tetrahedron `t=0`. The code below checks both identities as formal integer-coefficient polynomials, not at sample parameter points.

### Coupling to the actual matrix-square identity

At the true centroid,

`Lambda^2+Lambda=12·1 omega^T`, hence `K^2-K=12·1 omega^T`.

The polynomial `Lambda(Lambda+I)(Lambda-3I)=0` has distinct roots. The 3-eigenspace is one-dimensional; zero diagonal forces the −1 multiplicity to be three. For nine facets the spectrum of `K` is `4,1,1,1,1,1,0,0,0`. Thus `rank K=6`, and the sum of its 84 principal three-by-three minors is exactly `10+4*10=50`.

For an actual triangular chain `T` and its six-facet complement `R`, the new theorem makes `K_TT` invertible with a physical-volume lower bound on its determinant. The following constraints then hold **simultaneously**:

```text
K_TT^2-K_TT = 12·1_T omega_T^T-K_TR K_RT,
S_R = K_RR-K_RT K_TT^-1 K_TR,
rank(S_R)=3,
Q_T = -K_TT^-1 K_TR Q_R,
S_R Q_R=0,  rank(Q_R)=3.
```

All four-by-four minors of the six-by-six Schur matrix vanish. Its three-dimensional right kernel is the actual remaining pole coordinate space. With the same reciprocal metric `N`, every tree inequality must be evaluated in `H=Q N Q^T`; no independent Gram block or independently centred polar is introduced. This is a usable exact elimination of three pole rows, not just another independent coefficient cap.

### Conditional rational lower bound from a genuine volume deficit

Suppose the chain hull is contained in an actual ancestor-closed subhull `Q` for which the already journaled bound `400000*(V-Vol(Q))^2>Vol(Q)^2` has been established. The journal records that bound and its proper ancestor-closure scope. I have not reverified its antecedent certificate here.

It implies `r<2000/(2000+sqrt(10))<2000/2003`. Since `(1-r)^2(1+2r)` decreases on `[0,1]`, the new determinant satisfies the exact rational bound

**`det K_T > 54027/8036054027 > 1/150000`.**

This implication is conditional on the actual subhull certificate, not permission to fit a scalar volume or infer an ancestor closure from a tree label alone.

## 5. Physical rational verification and exact unexcluded complement

The new verifier uses the journal's actual nine-vertex countercontrol, not arbitrary masses. It rebuilds its complete hull from all triples, checks the nine maximal facets and 16 true edges, integrates the ordinary volume and centroid, recentres exactly, reconstructs every actual facet centroid, `d`, and `Lambda`, verifies all 81 matrix-square entries and all 36 reciprocal hull-volume inequalities, and preserves the known negative nontriangular minor. Its raw volume and centroid are

```text
V=65791/196608,
g=(28475383/101054976,28475383/101054976,-259/197373).
```

These are inherited fixture data, independently recomputed in this execution.

To make the metric coupling explicit, the source uses the rational physical image

```text
A=[[1,1/3,0],[0,1,1/5],[0,0,1]], det(A)=1,
M=A^T A=[[1,1/3,0],[1/3,10/9,1/5],[0,1/5,26/25]],
N=M^-1=[[251/225,-26/75,1/15],[-26/75,26/25,-1/5],[1/15,-1/5,1]].
```

It reconstructs the image body as well, verifying its centroid `Ag`, its transformed poles and the **identical physical Lambda**. At its own centroid this metric fixture has strict `(S,U,H)=(5,5,8)`, not S1. Its stable facet indices are `[0,1,2,3,6]`; unstable vertex indices are `[0,1,2,3,7]`; saddles are `(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(3,7),(4,7)`.

There are three actual triangular chains. For `0-1-4` and `0-1-7`, the common volume fraction is `49408/65791`, the minor is `17690354146653/25888493428061`, and the lower bound is `44180961428223/284773427708671`. For `4-1-7`, the fraction is `256/65791`, and the minor equals its lower bound, `284760526226175/284773427708671`. Every corresponding Schur matrix has exact rank three. The nontriangular `[3,6,0]` minor remains `-2626495209961/103553973712244`.

**Exact remaining domain:** retain all five literal tree forms, all 25 frame possibilities and all their genuine label transports. Both available actual primal complements must still be considered. For each surviving physical incidence, impose the new inequality on every triple that really is a triangular two-edge chain, and the rational strengthening only when its actual ancestor-volume premise is certified. Instances with no such chain receive no restriction from this theorem. The excluded continuous chambers are exactly those violating one of these necessary inequalities or the coupled Schur identities; no exhaustive catalogue incidence sweep was performed, and no count of newly excluded labelled cases is asserted.

The accepted whole-type set remains `{33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}`. The coordinator's unpersisted 7954 package is not promoted. The research register remains `32<=C_min<=1374`, with no new `F>=10`, `V>=10`, `C>=34`, or C32 attainer statement.

## 6. New recovery commands, observed replays and pins

All three new units below use **CPython 3.13.5 and the standard library only**, assertions enabled, no randomness, no numerical optimizer, no external geometry input. Save them exactly as UTF-8/LF with a final LF. In a clean directory:

```sh
python -S boundary_replay.py > boundary_without_attachment.log
python -S recheck_frames.py > frames.log
python -S chain_minor.py > chain.log
```

The first command preserves the actual published decoder and both historical logs without the old sandbox. To repeat the additional full-parent authentication against this turn's supplied journal:

```sh
python -S boundary_replay.py /path/to/research-journal.md > boundary.log
```

Two separate clean directories completed these three commands with exit 0 and matching output bytes. Here exit 0 for `boundary_replay.py` means that the **negative recovery diagnosis was reproduced**; its three child executions of the old published decoder each exit 1. It is not the old recovery PASS.

| New file/output | Bytes | SHA-256 |
|---|---:|---|
| `boundary_replay.py` | 17149 | `d7f73de766f86156216d6c32da432dd57d15c69f4aab327cc2ba8cbc663d79cc` |
| `recheck_frames.py` | 4457 | `ff8234bdfc705be6c3186edc216ba187a896cf97e0d00fdd5b3aebd3ac8f2129` |
| `chain_minor.py` | 9929 | `1b3bd959fb05e9de55b084fb4551fb7317b931206576bb13c0296690d6bc8aa1` |
| `boundary.log`, with attachment authentication | 660 | `6ce818056e92c8af8e5469e006ff22d494d042e2f90c99e3a201afe4e142a3d9` |
| `frames_new.json` | 1616 | `d21bf29911fc161ad993af4267e8b57dc3f8a9f9b85908283a0141c67360a988` |
| `frames.log` | 316 | `1505c44fae5f9ba59372f5dfbca50cc8c6fbf307989942899367818542b6c3ab` |
| `chain_minor.json` | 3720 | `32b3f4b4843e662f619811fc855a50f4cfe11fca809f47777d054f05cb59e906` |
| `chain.log` | 361 | `a91ecf112162c6e2c9d89db6bdc600e416ee9951f84e72844e83c6e9a68660c4` |

Expected decisive markers are:

```text
IMMUTABLE_PUBLICATION_SOURCE_MISMATCH_REPRODUCED
ORIGINAL_FOUR_SOURCE_UNITS_NOT_RECOVERED_NO_MATRIX_REPLAY_CLAIM
CONDITIONAL_FIVE_FORM_GRAPH_THEOREM_RECHECK_PASS 592 82 25 11 8
ORIGINAL_281_MATRIX_CERTIFICATES_NOT_REPLAYED
TWO_FAN_POLYNOMIAL_IDENTITIES_EXACT_PASS
ACTUAL_C32_CENTROID_RECIPROCAL_METRIC_MATRIX_SQUARE_PASS
TRIANGULAR_CHAIN_MINORS_AND_RANK_THREE_SCHUR_PASS 3
PHYSICAL_FIXTURE_S_U_H 5 5 8
NO_WHOLE_TREE_OR_C32_TYPE_CLOSED
```

Supplementary complete evidence and new-source bundle (`NOVA24_RECOVERY_BOUNDARY_AND_TRIANGULAR_CHAIN_MINOR_V1.zip`). The inline sources, not this archive, reconstruct every new claimed object. The unavailable original four source units remain explicitly unavailable.

## 7. Complete new source units

### 7.1 Evidence-preserving negative recovery — `boundary_replay.py`


[Encoded source block omitted; the code in this passage is incomplete.]


### 7.2 New independent frame replay — `recheck_frames.py`

```python
"""NEW standard-library replay of the parent's conditional graph theorem.
Not the unavailable original dual_frames.py. CPython 3.13.5; no random input.
Run: python -S recheck_frames.py. Tree ordinals are NOT C32 catalogue IDs.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
assert __debug__
EXPECTED={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
FRAMES = {
 253: [
  [(1,8)],
  [(2,8)],
  [(3,8)],
  [(7,6)],
  [(8,4),(8,5),(8,6)]
 ],
 266: [
  [(2,8),(5,7),(6,7)],
  [(2,8),(6,7),(7,5)],
  [(2,8),(7,5),(7,6)],
  [(7,5),(7,6),(7,8)]
 ],
 272: [
  [(2,8),(6,4),(6,7)],
  [(6,4),(6,7),(6,8)],
  [(2,8),(6,7),(7,4)],
  [(2,8),(6,4),(7,6)],
  [(2,8),(7,4),(7,6)],
  [(7,4),(7,6),(7,8)]
 ],
 278: [
  [(1,8)],
  [(3,8)],
  [(2,8),(6,4),(7,5)],
  [(2,8),(7,4),(7,5)],
  [(7,4),(7,5),(7,8)],
  [(8,7)]
 ],
 285: [
  [(2,0)],
  [(3,0)],
  [(7,0)],
  [(8,0)]
 ]
}
def rooted(p):
 for i in range(1,len(p)):
  seen=set()
  while i:
   if i in seen:return False
   seen.add(i);i=p[i]
 return p[0]==0
def canonical(p):
 assert rooted(p)
 children=[[] for _ in p]
 for i in range(1,len(p)):children[p[i]].append(i)
 def code(i):return '('+''.join(sorted(code(j) for j in children[i]))+')'
 text=code(0);parents=[];stack=[]
 for c in text:
  if c=='(':
   parents.append(stack[-1] if stack else 0);stack.append(len(parents)-1)
  else:stack.pop()
 return tuple(parents)
def trees(n):return sorted({canonical((0,)+t) for t in product(*(range(i) for i in range(1,n)))})
def determinant(a):
 a=[list(map(F,r)) for r in a];d=F(1)
 for i in range(len(a)):
  j=next((j for j in range(i,len(a)) if a[j][i]),None)
  if j is None:return F(0)
  if j!=i:a[j],a[i]=a[i],a[j];d=-d
  t=a[i][i];d*=t
  for j in range(i+1,len(a)):
   u=a[j][i]/t
   for k in range(i,len(a)):a[j][k]-=u*a[i][k]
 return d
def dag(edges):
 incoming=[0]*9;out=[[] for _ in range(9)]
 for i,j in edges:incoming[j]+=1;out[i].append(j)
 stack=[i for i in range(9) if incoming[i]==0];n=0
 while stack:
  i=stack.pop();n+=1
  for j in out[i]:
   incoming[j]-=1
   if incoming[j]==0:stack.append(j)
 return n==9
counts=[len(trees(n)) for n in range(1,10)]
assert counts==[1,1,2,4,9,20,48,115,286]
alltrees=trees(9);assert {i:alltrees[i] for i in EXPECTED}==EXPECTED
allowed=set(EXPECTED.values());records=[];subset_count=0;kept=0;maximum_arcs=0;maximum_trees=0
for ordinal,p in EXPECTED.items():
 base={(i,p[i]) for i in range(1,9)};extra=[]
 for i in range(1,9):
  for j in range(9):
   if j in (i,p[i]):continue
   q=list(p);q[i]=j
   if rooted(q) and canonical(q) in allowed:extra.append((i,j))
 valid=[]
 for mask in range(1<<len(extra)):
  subset_count+=1;s={e for k,e in enumerate(extra) if mask>>k&1};edges=base|s
  out=[sorted(j for a,j in edges if a==i) for i in range(1,9)]
  if not dag(edges):continue
  choices=[(0,)+q for q in product(*out)]
  if not all(rooted(q) and canonical(q) in allowed for q in choices):continue
  lap=[[0]*9 for _ in range(9)]
  for i,j in edges:lap[i][i]+=1;lap[i][j]-=1
  assert determinant([r[1:] for r in lap[1:]])==len(choices)
  valid.append((s,len(choices)));maximum_arcs=max(maximum_arcs,len(edges));maximum_trees=max(maximum_trees,len(choices))
 maximal=[(s,n) for s,n in valid if not any(s<t for t,_ in valid)]
 maximal.sort(key=lambda r:sorted(r[0]));kept+=len(valid)
 assert {tuple(sorted(t)) for t,_ in maximal}=={tuple(sorted(t)) for t in FRAMES[ordinal]}
 frames=[dict(extra=sorted(s),trees=n) for s,n in maximal]
 records.append(dict(ordinal=ordinal,parent=p,optional=extra,retained=len(valid),frames=frames))
 print('FRAMES_RECHECK',ordinal,len(extra),len(valid),len(maximal))
assert subset_count==592 and kept==82 and sum(len(r['frames']) for r in records)==25
assert [len(r['optional']) for r in records]==[7,6,7,8,4]
assert [r['retained'] for r in records]==[12,20,26,19,5]
assert [len(r['frames']) for r in records]==[5,4,6,6,4]
assert maximum_arcs==11 and maximum_trees==8
b=(json.dumps(dict(tag='NOVA24_FRAMES_NEW_RECHECK_V1',counts=counts,subsets=subset_count,retained=kept,max_arcs=maximum_arcs,max_trees=maximum_trees,records=records),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('frames_new.json').write_bytes(b)
print('CONDITIONAL_FIVE_FORM_GRAPH_THEOREM_RECHECK_PASS',592,82,25,11,8)
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('ORIGINAL_281_MATRIX_CERTIFICATES_NOT_REPLAYED')
```

### 7.3 New physical theorem and exact rational verifier — `chain_minor.py`

```python
"""NOVA24_TRIANGULAR_CHAIN_MINOR_V1; CPython 3.13.5, stdlib only.
Analytical input: the actual-body Lambda in parent minimum-0034,
e415baee38fcd56612393d45cd7c966dad05dffa836c3659ace5ca13a2b1490b.
This is NEW source, not any of the four unavailable original cap9 units.
Run: python -S chain_minor.py. No numerical search or external input.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
assert __debug__
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def elim(a):
 a=[list(map(F,r)) for r in a];r=0;d=F(1)
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  if k!=r:a[k],a[r]=a[r],a[k];d=-d
  z=a[r][j];d*=z;a[r]=[v/z for v in a[r]]
  for i in range(len(a)):
   if i!=r:
    z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r,d,a
def det(a):
 r,d,_=elim(a);return d if r==len(a) else F(0)
def inv(a):
 n=len(a);r,_,b=elim([list(a[i])+eye(n)[i] for i in range(n)])
 assert r==n and [x[:n] for x in b]==eye(n)
 return [x[n:] for x in b]
def hull(p):
 faces=set();n=len(p)
 for i,j,k in combinations(range(n),3):
  normal=cross(sub(p[j],p[i]),sub(p[k],p[i]))
  if not any(normal):continue
  s=[dot(normal,sub(x,p[i])) for x in p]
  if max(s)>0 and min(s)<0:continue
  if not any(s):continue
  faces.add(tuple(a for a in range(n) if s[a]==0))
 faces=sorted(faces);edges=set()
 for f,g in combinations(faces,2):
  t=set(f)&set(g)
  if len(t)==2:edges.add(tuple(sorted(t)))
  else:assert len(t)<=1
 center=tuple(sum(x[k] for x in p)/n for k in range(3));cycles=[]
 for f in faces:
  adj={i:sorted(j for j in f if tuple(sorted((i,j))) in edges) for i in f}
  assert all(len(v)==2 for v in adj.values())
  q=[min(f),adj[min(f)][0]]
  while True:
   j=next(j for j in adj[q[-1]] if j!=q[-2])
   if j==q[0]:break
   assert j not in q;q.append(j)
  assert set(q)==set(f)
  normal=cross(sub(p[q[1]],p[q[0]]),sub(p[q[2]],p[q[0]]))
  if dot(normal,sub(center,p[q[0]]))>0:q=[q[0]]+q[:0:-1]
  cycles.append(q)
 assert n-len(edges)+len(cycles)==2
 assert set().union(*(set(f) for f in cycles))==set(range(n))
 return cycles,sorted(edges)
def integrate(p,faces):
 d=F(0);m=[F(0)]*3
 for f in faces:
  for j in range(1,len(f)-1):
   a,b,c=(p[i] for i in (f[0],f[j],f[j+1]));z=det3(a,b,c);d+=z
   for k in range(3):m[k]+=z*(a[k]+b[k]+c[k])
 assert d>0
 return d/6,tuple(x/(4*d) for x in m)
def geometry(p,faces):
 found,edges=hull(p)
 assert {frozenset(f) for f in found}=={frozenset(f) for f in faces}
 v,g=integrate(p,faces);x=[sub(a,g) for a in p]
 v1,g1=integrate(x,faces);assert v1==v and g1==(0,0,0)
 q=[];d=[];c=[]
 for f in faces:
  a,b,z=(x[i] for i in f[:3]);normal=cross(sub(b,a),sub(z,a));h=dot(normal,a)
  assert h>0;qi=tuple(t/h for t in normal)
  assert all(dot(qi,x[i])==1 if i in f else dot(qi,x[i])<1 for i in range(len(x)))
  total=F(0);s=[F(0)]*3
  for j in range(1,len(f)-1):
   a,b,z=(x[i] for i in (f[0],f[j],f[j+1]));w=det3(a,b,z);assert w>0;total+=w
   for k in range(3):s[k]+=w*(a[k]+b[k]+z[k])
  q.append(qi);d.append(total/(2*v));c.append(tuple(t/(3*total) for t in s))
 assert sum(d)==3
 assert all(sum(d[i]*q[i][k] for i in range(len(q)))==sum(d[i]*c[i][k] for i in range(len(q)))==0 for k in range(3))
 assert [[sum(d[i]*c[i][j]*q[i][k] for i in range(len(q))) for k in range(3)] for j in range(3)]==eye(3)
 L=[[d[j]*(1-dot(q[i],c[j])) for j in range(len(q))] for i in range(len(q))]
 assert all(L[i][i]==0 and sum(L[i])==3 for i in range(len(q)))
 assert all(0<L[i][j]<F(10,9) for i in range(len(q)) for j in range(len(q)) if i!=j)
 assert mm(L,q)==[[-z for z in r] for r in q]
 L2=mm(L,L);assert all(L2[i][j]+L[i][j]==4*d[j] for i in range(len(q)) for j in range(len(q)))
 assert elim(L)[0]==4
 return v,g,x,q,d,c,L,edges
# Exact formal polynomial arithmetic in (x,w,v,t), not point sampling.
def pa(a,b):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def ps(a,b):return pa(a,pn(b))
def pm(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   k=tuple(u+v for u,v in zip(i,j));c[k]=c.get(k,0)+x*y
 return {k:v for k,v in c.items() if v}
def pc(c):return {(0,0,0,0):c} if c else {}
X,W,V,T=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
for side in (0,1):
 Y=ps(ps(V,T),W) if side==0 else ps(V,W)
 Z=ps(V,X) if side==0 else ps(ps(V,T),X)
 CD=pm(pa(X,Y),pa(Z,W));XW=pm(X,W)
 D=pa(ps(ps(ps(pc(1),pm(X,X)),pm(W,W)),CD),pm(XW,pa(pa(X,Y),pa(Z,W))))
 base=pm(pm(ps(pc(1),V),ps(pc(1),V)),pa(pc(1),pm(pc(2),V)))
 extra=pa(pm(pm(pc(2),ps(pc(1),V)),ps(pm(V,V),XW)),pm(T,ps(pa(Z,W) if side==0 else pa(X,Y),XW)))
 assert ps(D,pa(base,extra))=={}
print('TWO_FAN_POLYNOMIAL_IDENTITIES_EXACT_PASS')
P=[tuple(F(t,192) for t in r) for r in [(192,0,0),(0,192,0),(0,0,192),(48,48,-192),(3,0,0),(0,3,0),(0,0,12),(3,3,-12),(80,80,-67)]]
FAC=[[0,1,2],[0,8,1],[0,2,6,4],[0,4,7,3],[0,3,8],[1,5,6,2],[1,3,7,5],[1,8,3],[4,6,5,7]]
v,g,p,q,d,c,L,edges=geometry(P,FAC)
assert v==F(65791,196608) and g==(F(28475383,101054976),F(28475383,101054976),-F(259,197373))
A=[[F(1),F(1,3),F(0)],[F(0),F(1),F(1,5)],[F(0),F(0),F(1)]]
M=mm(tr(A),A);N=inv(M);assert det(A)==1 and mm(M,N)==eye(3)
PA=mm(P,tr(A));va,ga,xa,qa,da,ca,La,ea=geometry(PA,FAC)
assert va==v and ga==tuple(dot(r,g) for r in A) and La==L and da==d
assert qa==[tuple(r) for r in mm(q,inv(A))]
K=[[F(i==j)+L[i][j] for j in range(9)] for i in range(9)];assert elim(K)[0]==6
minor_sum=sum(det([[K[i][j] for j in ids] for i in ids]) for ids in combinations(range(9),3))
assert minor_sum==50
bad=[3,6,0];bad_minor=det([[K[i][j] for j in bad] for i in bad]);assert bad_minor==-F(2626495209961,103553973712244)
tri=[i for i,f in enumerate(FAC) if len(f)==3];chains=[]
for ids in combinations(tri,3):
 mids=[b for b in ids if all(len(set(FAC[a])&set(FAC[b]))==2 for a in ids if a!=b)]
 if not mids:continue
 b=min(mids);a,cid=sorted(set(ids)-{b});verts=sorted(set(FAC[a]+FAC[b]+FAC[cid]));pp=[P[i] for i in verts]
 ff,_=hull(pp);vol,_=integrate(pp,ff);r=vol/v
 minor=det([[K[i][j] for j in ids] for i in ids]);bound=(1-r)**2*(1+2*r)
 assert 0<r<1 and minor>=bound>0
 if len(set(FAC[a])&set(FAC[cid]))==1:
  o,=set(FAC[a])&set(FAC[cid]);bv,=set(FAC[a])&set(FAC[b])-{o};cv,=set(FAC[b])&set(FAC[cid])-{o}
  av,=set(FAC[a])-{o,bv};ev,=set(FAC[cid])-{o,cv}
  aa,bb,cc,ee=[sub(P[i],P[o]) for i in (av,bv,cv,ev)]
  dx,dy,dz,dw=[abs(t)/(6*v) for t in (det3(aa,bb,cc),det3(aa,bb,ee),det3(aa,cc,ee),det3(bb,cc,ee))]
  assert min(dx,dy,dz,dw)>0 and r==max(dx+dz,dy+dw)
  BB=lambda i,j:d[i]*L[i][j]/d[j]
  assert BB(a,b)==BB(b,a)==dx and BB(b,cid)==BB(cid,b)==dw
  assert BB(a,cid)==dx+dy and BB(cid,a)==dz+dw
 else:
  assert all(d[i]*L[i][j]/d[j]==r for i in ids for j in ids if i!=j)
 u=[i for i in range(9) if i not in ids];kt=[[K[i][j] for j in ids] for i in ids]
 left=mm([[K[i][j] for j in ids] for i in u],inv(kt));removed=mm(left,[[K[i][j] for j in u] for i in ids])
 schur=[[K[i][j]-removed[ii][jj] for jj,j in enumerate(u)] for ii,i in enumerate(u)]
 assert elim(schur)[0]==3
 k2=mm(kt,kt);outside=mm([[K[i][j] for j in u] for i in ids],[[K[i][j] for j in ids] for i in u])
 assert all(k2[ii][jj]-kt[ii][jj]==4*d[j]-outside[ii][jj] for ii,i in enumerate(ids) for jj,j in enumerate(ids))
 chains.append(dict(chain=[a,b,cid],vertices=verts,volume_fraction=r,minor=minor,lower_bound=bound,schur_rank=3))
assert len(chains)>0
# Full original-body mechanics in the single metric M, equivalent to Euclidean PA.
G=mm(mm(q,N),tr(q));stable=[];unstable=[];saddles=[]
for i in range(9):
 tests=[G[i][i]-G[j][i] for j in range(9) if j!=i]
 assert all(t!=0 for t in tests)
 if min(tests)>0:stable.append(i)
for i in range(9):
 tests=[dot(p[i],tuple(dot(r,sub(p[j],p[i])) for r in M)) for j in range(9) if j!=i]
 assert all(t!=0 for t in tests)
 if max(tests)<0:unstable.append(i)
for i,j in edges:
 a=p[i];e=sub(p[j],a);me=tuple(dot(r,e) for r in M);t=-dot(a,me)/dot(e,me)
 f,h=[k for k in range(9) if i in FAC[k] and j in FAC[k]]
 z=G[f][f]*G[h][h]-G[f][h]**2;assert z>0
 b1=(G[h][h]-G[f][h])/z;b2=(G[f][f]-G[f][h])/z
 assert all(w!=0 for w in (t,1-t,b1,b2))
 if min(t,1-t,b1,b2)>0:saddles.append([i,j])
assert len(stable)+len(unstable)-len(saddles)==2
# Every reciprocal hull-volume constraint for this same physical Lambda.
for i,j in combinations(range(9),2):
 pts=[P[k] for k in sorted(set(FAC[i]+FAC[j]))];faces,_=hull(pts);w,_=integrate(pts,faces)
 assert L[i][j]*L[j][i] <= (w/v)**2 <= 1
r=F(2000,2003);guard=(1-r)**2*(1+2*r);assert guard==F(54027,8036054027)>F(1,150000)
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
report=dict(tag='NOVA24_TRIANGULAR_CHAIN_MINOR_V1',vertices=P,facets=FAC,volume=v,centroid=g,linear_image=A,metric=M,reciprocal_metric=N,d=d,Lambda=L,chains=chains,principal_three_minor_sum=minor_sum,nontriangular_negative_minor=bad_minor,mechanics=dict(S=stable,U=unstable,H=saddles),conditional_guard=guard,whole_five_forms_closed=0)
b=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode();Path('chain_minor.json').write_bytes(b)
print('ACTUAL_C32_CENTROID_RECIPROCAL_METRIC_MATRIX_SQUARE_PASS')
print('NONTRIANGULAR_P0_COUNTERCONTROL_RETAINED',bad_minor)
print('TRIANGULAR_CHAIN_MINORS_AND_RANK_THREE_SCHUR_PASS',len(chains))
print('PHYSICAL_FIXTURE_S_U_H',len(stable),len(unstable),len(saddles))
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('NO_WHOLE_TREE_OR_C32_TYPE_CLOSED')
```

## 8. Continuation priority and final boundary

The most valuable recovery input is an actual copy of the four original files, the original 11,977-byte decoder, or the intended 17,810-byte decoded JSON that matches its pin. Without such bytes, recreating a numerical locator would be a new implementation, not faithful recovery of the old executable. The malformed immutable text and its historical logs are now recoverable from this handoff; the original matrix checkpoint is not.

The independent mathematical continuation is to locate genuine triangular two-edge facet chains in the lead's surviving labelled incidences, retain the actual common hull volumes and ancestor certificates, and use the proved positive principal block to eliminate three pole rows of the same physical Lambda. Enforce its rank-three Schur kernel, the single reciprocal metric, both available complementary choices, and the literal five-form/frame inequalities together. No conclusion should be drawn from failure of a locator or from a freely chosen incidence-supported mass matrix.

In summary: the publication-level source mismatch is authenticated; two historical log streams and the conditional graph consequence are recovered; the new triangular-chain minor/Schur theorem is proved and exactly checked; the four original source units and the original 281-certificate replay remain unrecovered; and no whole-tree, whole-type, or global lower-bound endpoint has advanced.
