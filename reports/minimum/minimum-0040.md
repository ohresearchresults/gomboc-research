# minimum-0040

Historical AI scientific report · saved 2026-09-10 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# NOVA24_F9_11_SHADOW_FRAMES_V1

## 1. Determination

**A new whole-continuous-domain restriction has been proved for the five remaining nine-pole forms.** For an actual homogeneous convex three-polytope with nine facets and a unique strictly stable facet, at its own uniform-volume centroid and with one reciprocal positive-definite metric, the complete nonnegative unequal-pair pole-shadow graph has:

**at most 10 arrows, at least 62 strictly negative unequal pairs, and at most four weak escape arborescences.**

Its exhaustive outer cover now consists of **11 maximal base-tree-labelled frames**, rather than the parent's 25. Of the parent's 82 admitted base-tree-labelled graphs, **57 are excluded and 25 remain unexcluded**. All weak escape equalities are included, with no restriction on the reciprocal metric's condition number or on positive physical cone volumes.

The new certificates exclude **12 nine-arrow configurations**, each consisting of one of the five base trees and one additional nonnegative shadow. Exact label transport yields the 21 forbidden single-extra-arrow placements listed below. These are continuous sign-domain exclusions, not exclusions inferred from failed numerical searches.

**The five whole tree forms themselves remain unexcluded:** TREE ordinals **253, 266, 272, 278, 285**. No canonical C32 root or whole type is declared closed.

There is an important limitation to the mechanism. The successful two-row certificates contain genuine physical reciprocal-pair counterterms, justified by the same body's pair-hull volumes. However, a subsequent exact deletion test proves that all the certificates remain valid without those counterterms. Thus the demonstrated advance comes from imposing the **ninth shadow inequality simultaneously with the tree**, beyond the old tree-shape closure. It does **not** establish that matrix-square or volume coupling is essential, or that those stronger physical constraints close a whole surviving form.

### Source authority

The literal parents used are:

```text
minimum-0037
SHA-256 ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596
NOVA24_CAP9_NEW_281_RESTORED_V1

minimum-0038
SHA-256 de9cd99e6171b5909689e636d347b20d427f837b702d67eb007279b34f4fbaeb
C32_FOUR_TRIANGLE_FAN_PHYSICAL_BOUNDARY_V1
```

The first supplies the accepted 281-tree exclusion and the five-form/25-frame premise. Its 51,912 matrices were **not rerun** in this continuation. The second supplies the actual four-row singularity warning. No conflicting tree, facet, or canonical-map alias was used. The parent explicitly distinguishes these TREE ordinals from C32 map IDs. :contentReference[oaicite:0]{index=0}

The second parent's proper common-apex four-triangle fan can have a negative or zero determinant despite positive proper minors and strict actual mechanics. **No four-row physical block is inverted in this proof.** The positive matrices below are auxiliary separating certificates, not principal blocks of the actual `I+Lambda`. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## 2. Exact newly excluded domains and complete remaining cover

For the actual facet-pole rows Q and reciprocal metric N, write

`A_ij=q_i^T N(q_j-q_i)`.

For each array p below, its eight required shadows are `A_i,p[i]>=0`, i=1,...,8. Root 0 labels the unique strictly stable facet. These are canonical rooted-tree labels, not primal vertex labels or original catalogue facet labels:

```text
253 (0,0,1,2,3,4,5,0,7)
266 (0,0,1,2,3,4,5,4,0)
272 (0,0,1,2,3,4,5,5,0)
278 (0,0,1,2,3,4,5,6,0)
285 (0,0,1,2,3,4,5,6,7)
```

### The 12 certified representatives

Each line excludes the entire continuous domain satisfying the base tree and the displayed additional **weak** inequality. No sign is imposed on the other pairs by that certificate.

```text
case  TREE  additional arrow  selected actual coefficient rows
 0    253   1 -> 8            (0,)
 1    253   2 -> 8            (0,)
 2    253   3 -> 8            (0,)
 3    253   7 -> 6            (0,)
 4    253   8 -> 4            (0,)
 5    253   8 -> 5            (0,)
 6    253   8 -> 6            (0,1)
 7    266   2 -> 8            (0,1)
 8    272   2 -> 8            (0,1)
 9    278   1 -> 8            (0,1)
10    278   2 -> 8            (0,1)
11    285   8 -> 0            (0,1)
```

The certificate's row indices refer to rows of **one actual Lambda**. They are not alternative physical centroids or cone apices.

These configurations were admitted by the parent's graph closure because replacing one tree parent still left an allowed tree shape. The new proof instead retains all eight original arrows and imposes the ninth simultaneously.

Exact root-preserving graph isomorphisms give the following complete set of newly forbidden single extras within the old cover:

```text
253: (1,8),(2,8),(3,8),(7,6),(8,4),(8,5),(8,6)
266: (2,8),(7,8)
272: (2,8),(6,8),(7,8)
278: (1,8),(2,8),(3,8),(7,8),(8,7)
285: (2,0),(3,0),(7,0),(8,0)
```

For example, case 9 transports to TREE285 with extra `(2,0)` under the exact old-to-new vertex permutation

`pi=(0,2,3,4,5,6,7,8,1)`.

Its coefficient rows `(0,1)` become actual rows `(0,2)`. The reciprocal inequality after transport concerns those actual facets; it is not a statement about primal edge 28 or canonical type 285. The source reconstructs and verifies every transport permutation used in the 57 exclusions.

### The 11 remaining maximal frames

Add each inner extra-arrow list to the eight arrows of its corresponding base tree:

```python
NEW = {
 253: [[]],
 266: [
  [(5,7),(6,7)],
  [(6,7),(7,5)],
  [(7,5),(7,6)]
 ],
 272: [
  [(6,4),(6,7)],
  [(6,4),(7,6)],
  [(6,7),(7,4)],
  [(7,4),(7,6)]
 ],
 278: [
  [(6,4),(7,5)],
  [(7,4),(7,5)]
 ],
 285: [[]]
}
```

Extras in a frame may be absent. The actual graph is a subgraph containing its chosen base tree; every pair outside its frame is strictly negative. A frame is an upper cover, not a claim that its complete graph is physically realizable.

The exact exhaustive counts are:

| TREE ordinal | Old admitted graphs | Newly excluded | Remaining graphs | New maximal frames |
|---|---:|---:|---:|---:|
| 253 | 12 | 11 | 1 | 1 |
| 266 | 20 | 12 | 8 | 3 |
| 272 | 26 | 17 | 9 | 4 |
| 278 | 19 | 13 | 6 | 2 |
| 285 | 5 | 4 | 1 | 1 |
| Total | 82 | 57 | 25 | 11 |

These are base-tree-labelled graph counts, **not canonical roots, map types, or graph-isomorphism-class counts**. The complete 25-graph remainder and all 57 exclusion witnesses are reconstructed by `cover.py`; the literal 11-frame table is its compact complete description.

Every remaining frame has at most ten arrows and at most four rooted escape arborescences. For forms **253 and 285**, the actual complete nonnegative shadow graph must equal the base tree itself, so the weak escape arborescence is unique.

## 3. Physical averaging proof

### One actual centroid, one actual Lambda, one reciprocal metric

Let P be the actual full-dimensional homogeneous body, translated by its ordinary volume centroid. For actual facet i, let `A_i,h_i,c_i` denote its area, centroid-to-plane distance, and uniform-area centroid, and let `V=Vol(P)`. Define

```text
omega_i=A_i h_i/(3V),
d_i=3 omega_i,
Lambda_ai=3 omega_i(1-q_a.c_i).
```

Actual cone integration and divergence give

```text
sum omega_i=1,
sum omega_i c_i=sum omega_i q_i=0,
3 sum omega_i c_i q_i^T=I_3,
Lambda Q=-Q,
Lambda 1=3*1,
Lambda_aa=0.
```

The accepted trace theorem supplies `0<Lambda_ai<10/9` off the diagonal. These are actual facet areas, centroids and cone volumes; no polar volume centroid is substituted. These physical identities and the cap are inherited from the first parent. :contentReference[oaicite:3]{index=3}

For an arbitrary physical primal metric `M>0`, use its one reciprocal `N=M^-1`, and set `H=Q N Q^T`. H is nonzero PSD, with actual geometric rank three. The separating proof is stronger in that it does not need to impose rank three, a metric condition bound, or any lower volume cutoff.

Each actual coefficient row lies in the closed capped simplex

`{s:0<=s_i<=10/9, sum s_i=3}`.

Its 168 vertices have two entries 10/9, one 7/9 and five zeros. At an extreme point at most one coordinate can be strictly between its bounds; the sum condition determines these values. For selected row a the corresponding integer vectors are

`w=9e_a+10e_i+10e_j+7e_k`, with distinct i,j,k different from a and i<j.

The actual row admits nonnegative convex weights `rho_a,w`, of total one, with

`Q^T sum_w rho_a,w w=0`.

These rho are an algebraic convex decomposition of an actual row, **not fitted physical masses**. Every extreme row is checked, including the closed boundary.

### Genuine reciprocal pair-hull coupling

For actual distinct facets a,b, put

`R_ab=conv(F_a union F_b)`, `r_ab=Vol(R_ab)/V<=1`.

Both selected facets are preserved in this actual subhull. The diagonally similar physical matrix

`B=diag(d) Lambda diag(d)^(-1)`

has entries `B_ij=A_i dist(c_j,aff F_i)/V`; the selected traces scale by the actual volume ratio when passing between R_ab and P. The inherited reciprocal trace inequality therefore gives

`x y<=r_ab^2`, where `x=Lambda_ab`, `y=Lambda_ba`.

This is the physical pair-hull inequality, not a constraint assigned to independently chosen rows. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

Together with the cap,

```text
100+81r_ab^2-90(x+y)
 =(10-9x)(10-9y)+81(r_ab^2-xy) >=0.
```

Thus, on the entire physical domain,

`x+y<=10/9+9r_ab^2/10<=181/90`.

Only the unconditional actual inclusion `R_ab subset P` is used for the final constant. No unproved small-volume threshold is imposed. The argument applies whether or not the transported facets share a true edge.

### Integer certificate formula

For each of the nine required arrows `i->j`, define

`L_ij=2e_i e_i^T-e_i e_j^T-e_j e_i^T`.

Then a weak nonnegative shadow gives

`trace(L_ij H)=-2A_ij<=0`.

A one-row record contains an integer vector gamma and nonnegative integer arrow multipliers for every extreme w. A two-row record contains two gamma vectors, a symmetric integer offset O, and a symmetric integer counterterm Z. Its offsets are O and -O. For both O and Z, the stored 45 upper-triangular parameters produce twice their parameter on a diagonal and their parameter at each off-diagonal position.

The exact verifier proves **Z positive definite** in every two-row record. For a selected row a, with other selected row b and offset sign `epsilon_a=+1` or `-1`, define

```text
C_a,w = 20(gamma_a w^T+w gamma_a^T)
        +180 sum_e mu_a,w,e L_e
        +180 epsilon_a O
        +(20w_b-181)Z.
```

For one-row records the last two terms are absent. Every multiplier is nonnegative, and **every `C_a,w-I_9` is positive definite**.

Average with each row's actual rho and sum over selected rows. The gamma terms vanish through the actual row equations. The offsets cancel because both decompositions total one. The arrow terms pair nonpositively with the same H. In a two-row case the counterterm averages to

`180(Lambda_ab+Lambda_ba-181/90)Z`,

which also pairs nonpositively with H by the actual pair-hull inequality and `Z>=0`.

The resulting pairing is therefore nonpositive. But every certificate matrix is strictly above I, each row's convex weights total one, and H is nonzero PSD. Its pairing is strictly positive. This contradiction excludes the complete nine-arrow domain.

There is no strictness assumption on the nine escape inequalities: a chosen shadow may equal zero. Distinct actual poles still obey

`||q_j||_N^2-||q_i||_N^2=2A_ij+||q_j-q_i||_N^2>0`,

so their nonnegative graph is acyclic even on weak escape boundaries.

### Exact combinatorial coverage

`cover.py` enumerates all 592 optional subsets of the parent's literal 25-frame input. It checks every parent choice for rootedness and the five permitted shapes, verifies directed matrix-tree cofactor counts, and recovers exactly the old 82 graphs and 25 maximal frames.

For each old graph, it exhausts its nine-edge subsets and tests root-preserving isomorphism against the 12 certified configurations. Degree classes only prune permutations: every permutation within the corresponding classes is enumerated. Each reported witness includes the exact nine-edge subgraph and a checked complete nine-label permutation.

Exactly 57 graphs contain a forbidden configuration. The remaining 25 have exactly the 11 maximal frames displayed above, proving the new numerical bounds. No geometric sample or failed locator is used in this coverage argument.

## 4. What the physical coupling did—and did not—establish

The main verification checks **3024 shifted certificate matrices and six positive-definite Z matrices**, giving **27,270 positive leading principal minors**. It expands each scalar quadratic independently of the producer, applies full integer Bareiss elimination, and separately performs Fraction LDL factorization with all nine pivot products compared to the Bareiss determinants.

After obtaining these certificates, I deleted the reciprocal counterterm exactly. Of the 3024 blocks:

```text
1008 single-row blocks are unchanged;
1512 coupled blocks remain PD by addition of a nonnegative multiple of Z;
504 remaining blocks were directly rechecked by Bareiss and Fraction LDL.
```

All pass. The direct deletion checks add 4536 leading-minor verifications. The complete deletion audit is included as `ablation.py`.

**Therefore the new exclusions hold even in the independent capped-row outer relaxation.** The delivered physical coupling is valid and its Z matrices are nonzero, but it is not essential for these particular certificates. This is a useful distinction: the old frontier missed simultaneous shadow coexistence, not just an unavailable volume constraint.

I also investigated stronger row/pair restrictions on the remaining tail-arrow configurations, but obtained no further certified exclusion. Numerical non-success is not a feasibility certificate or a barrier theorem. No matrix-only feasible family is presented as a physical realization.

The same actual matrix-square identity `Lambda^2+Lambda=12*1*omega^T`, genuine three-triangle-chain volume identities, and rank-three pole geometry remain available for the unresolved domain. Their decisive use is still an outstanding obligation. No claim of four-row nonsingularity is made, including on the singular physical stratum established by the second parent.

## 5. C32 interpretation and exact remaining complement

The new theorem is universal for nine-facet S1 bodies; it does not depend on a particular C32 incidence. Consequently it applies to every genuine C32 placement exhibiting one of the forbidden labelled shadow configurations, without inventing a catalogue correspondence.

For the inherited strict nondegenerate joint matching application, preserve both possible primal choices:

```text
T     =(0,0,1,2,3,4,5,6,0)
T_alt =(0,0,8,2,3,4,5,6,0).
```

The second is available only when actual edge 28 and its required sign are present. Matching selects some sign-compatible complementary pair; it does not license fixing one arbitrarily. :contentReference[oaicite:6]{index=6}

A new corollary is that, when an actual dual escape tree has shape 253 or 285, its complete nonnegative graph is that unique tree. Hence **at most one of the two distinct primal choices can be sign-compatible as its complementary matching tree**, even when both primal escape trees are mechanically available. This does not identify which choice works, and does not exclude a root or type. Both must still be considered before actual facet-label transport and complement checking.

The exact unexcluded domain is: all genuine realizations admitting one of the five literal base trees, with the complete nonnegative shadow graph contained in one of the 11 literal new frames, together with all actual support/incidence conditions, ordinary volume-centroid equations, actual facet area and volume identities, the same physical Lambda including its matrix-square identity, and one reciprocal SPD metric. The outer cover asserts no physical attainability.

No canonical C32 incidence sweep was performed. The 17 accepted whole types remain

`{33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}`.

The shared register stays `32<=C_min<=1374`. The unpersisted coordinator 7954 package is not promoted. No new `F>=10`, `V>=10`, `C>=34`, whole-type count, or attainer is claimed. :contentReference[oaicite:7]{index=7}

## 6. Complete recovery, observed execution and pins

### Commands and environment

Save all six complete source units in §7 together, UTF-8/LF with a final LF. Full reconstruction uses no old coefficient file, sandbox archive, catalogue or journal input:

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python -S replay.py > full.log
python -S replay.py check > frozen.log
```

Observed numerical environment:

```text
CPython 3.13.5, GCC 14.2.0, Linux x86_64
NumPy 2.3.5
SciPy 1.17.0
threadpoolctl 3.6.0
NumPy OpenBLAS 0.3.30 / SkylakeX / one thread
SciPy OpenBLAS 0.3.30 / SkylakeX / one thread
One producer process, no randomness.
```

This is **SkylakeX**, unlike the first parent's Haswell reconstruction environment. These are new coefficients and new source identities. Frozen verification is standard-library exact arithmetic. Byte-identical numerical reconstruction is tied to the stated environment; a different backend's coefficients must be independently checked and assigned new pins rather than called this checkpoint.

The new locator uses nine nonnegative multipliers per extreme block, initially 1/9, with their total normalized to the number of blocks m. Gamma and offset coefficients start at zero, the margin starts at -1, and the coupled Z starts at `0.001 I`. Its barrier is

`-margin-(tau/m)[sum logdet(block-margin I)+sum log(mu)+logdet(Z)]`,

omitting `logdet(Z)` for single-row cases. It uses `tau=0.05*0.18**outer`, at most eight outer rounds and 70 Newton steps, decrement tolerance `min(1e-7,tau*0.001)`, positivity step factor 0.99, Armijo factor 0.05, at most 60 halvings, symmetric solve with `rcond=1e-14` least-squares fallback, candidate margin threshold `1e-8`, max-absolute-coefficient normalization, and `np.rint` at `10**8`. Acceptance is exclusively by exact positive-definiteness checks. None of these parameters restricts physical coordinates, metrics or volumes.

A producer execution and a separate clean six-source driver execution produced identical coefficient and output bytes. The complete clean `replay.py` returned **observed exit status 0**. A separate frozen `replay.py check` also returned **observed exit status 0**, including the counterterm-deletion audit. The old 281 matrices were not regenerated or reverified.

### Source, coefficient and output pins

| File | Bytes | SHA-256 |
|---|---:|---|
| inputs.py | 1569 | f268a0f9923c2c74b6b8b1c14a542e0b6b2e6b59fe80883ae983a02f382e841e |
| make.py | 5786 | 3e11bedf8f61ba71c028b374bd08f97d0b41b302f5bc1af7ea879a4a128cdc84 |
| check.py | 3973 | 3b8c45780c9441d26bb806a77a533cb6e47cb5f425cfc8ea02bcd46caaa2b9eb |
| cover.py | 5016 | 1308a7db5d3059b3489e754476666db6328ee8d1155bd2f00754086877d900c8 |
| ablation.py | 1384 | ef05b97ab9ffc5952ab4034fe11634c9f1a2a91002489e19546918df47b7122d |
| replay.py | 2753 | f32a0a27d8be69b539632d01c0b52ba4e589f7ed4eb83efc311b975d264889c0 |
| shadow_exact.json | 251836 | 1cf29f366fc666b1e41fd8f8a9a7df3739123a3ba0701c93f3fb13d2c31efd99 |
| shadow_verified.json | 820 | 97f5dc06484139d4a383ca1b42aec9e1f033102ebaac6aa3fa1db1914708ee81 |
| shadow_cover.json | 10036 | 5bad625f9a57c514229749b6d6b4b2e2f2d4a1bed1d2f4a6c39ade6c120fff0b |
| omission.json | 142 | f0a6682f19624cc32757457a1503fefef3512f33c8f4df443cb707ad6b5f4049 |
| make.log | 662 | aa8722776a5620610e99d793308c3bd28fe5aaa1d8f27e588fce3adbe367e87a |
| check.log | 655 | 49907278c7085d6844d61c44e612f0b32e552f544fd940b44c1a19f267d0f834 |
| cover.log | 315 | c899dddb6b3503d5596ff656f6da6e4d77a55d9f6dc531552a978ce0e14822ad |
| ablation.log | 209 | de2029939a4224bd30756cef862f8bb02df5530c88bcf3d6044c6d55fd506ad5 |
| full.log | 1994 | 28387e7acc325794f9f9e32c5573b325f7a510c7b626b234168377613ea5d0a5 |
| frozen.log | 1332 | 33dbf77962b9197741f69359674e9cb714caa060ed6292ccaf5923783fda5066 |

The coefficient file contains 702 free integers and 27,216 nonnegative multiplier integers. Every JSON object uses `json.dumps(...,sort_keys=True,separators=(',',':'))`, UTF-8 and one final LF.

Independent exact stream hashes:

```text
weights:
6b433f2148b0e5add769916b1efa366a37bdfb23bd5d4bbcc83631ffd6e93b1b
matrices:
1777298335771d2b689bede2d17d97ebc951128d433fa9fb008923736d954938
minors:
5248c6b54103600874163ca61b0cca5c9bd4d5af7d86b15951ab9754ab84a972
couplings:
30d170ce7aca458b5903014617fc9b97f09178af5aea16349543b7f0a6abe56a
```

Order: case index 0 through 11, selected rows in their literal order, then w in lexicographically sorted nine-tuple order. Canonical JSON/LF stream records are `[case,row,extreme_index,w]`, `[case,row,extreme_index,C-I]`, and `[case,row,extreme_index,nine_leading_minors]`. Each coupled case additionally appends `[case,Z,nine_leading_minors_of_Z]` to the coupling stream.

Observed decisive terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Supplementary [new complete proof checkpoint](sandbox:/mnt/data/NOVA24_F9_11_SHADOW_FRAMES_V1.zip): **131155 bytes**, SHA-256 `fd0c6cda92dba1b474cd43376b0a91f1e93280e580151b98264169d7e7ab7848`. The archive is optional; all inputs, generator, independent checker, coverage reconstruction and deletion audit are included literally below.

## 7. Complete executable source

### inputs.py

```python
"""Exact inputs; tree ordinals are not C32 map IDs. UTF-8/LF/final LF."""
PARENTS=[('minimum-0037','ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596'),('minimum-0038','de9cd99e6171b5909689e636d347b20d427f837b702d67eb007279b34f4fbaeb')]
TREES={253: (0, 0, 1, 2, 3, 4, 5, 0, 7),
 266: (0, 0, 1, 2, 3, 4, 5, 4, 0),
 272: (0, 0, 1, 2, 3, 4, 5, 5, 0),
 278: (0, 0, 1, 2, 3, 4, 5, 6, 0),
 285: (0, 0, 1, 2, 3, 4, 5, 6, 7)}
OLD={253: [[(1, 8)], [(2, 8)], [(3, 8)], [(7, 6)], [(8, 4), (8, 5), (8, 6)]],
 266: [[(2, 8), (5, 7), (6, 7)],
       [(2, 8), (6, 7), (7, 5)],
       [(2, 8), (7, 5), (7, 6)],
       [(7, 5), (7, 6), (7, 8)]],
 272: [[(2, 8), (6, 4), (6, 7)],
       [(6, 4), (6, 7), (6, 8)],
       [(2, 8), (6, 7), (7, 4)],
       [(2, 8), (6, 4), (7, 6)],
       [(2, 8), (7, 4), (7, 6)],
       [(7, 4), (7, 6), (7, 8)]],
 278: [[(1, 8)],
       [(3, 8)],
       [(2, 8), (6, 4), (7, 5)],
       [(2, 8), (7, 4), (7, 5)],
       [(7, 4), (7, 5), (7, 8)],
       [(8, 7)]],
 285: [[(2, 0)], [(3, 0)], [(7, 0)], [(8, 0)]]}
PLAN=[(253, (1, 8), (0,)),
 (253, (2, 8), (0,)),
 (253, (3, 8), (0,)),
 (253, (7, 6), (0,)),
 (253, (8, 4), (0,)),
 (253, (8, 5), (0,)),
 (253, (8, 6), (0, 1)),
 (266, (2, 8), (0, 1)),
 (272, (2, 8), (0, 1)),
 (278, (1, 8), (0, 1)),
 (278, (2, 8), (0, 1)),
 (285, (8, 0), (0, 1))]
NEW={253: [[]],
 266: [[(5, 7), (6, 7)], [(6, 7), (7, 5)], [(7, 5), (7, 6)]],
 272: [[(6, 4), (6, 7)], [(6, 4), (7, 6)], [(6, 7), (7, 4)], [(7, 4), (7, 6)]],
 278: [[(6, 4), (7, 5)], [(7, 4), (7, 5)]],
 285: [[]]}
```

### make.py

```python
"""New graph certificates, not a replay of the old 281 trees.
CPython3.13.5/numpy2.3.5/scipy1.17.0/threadpoolctl3.6.0.
One OpenBLAS thread, one process, no random inputs. Run: python make.py.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import warnings,json,hashlib
from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.linalg import solve,LinAlgWarning
from threadpoolctl import threadpool_limits
threadpool_limits(1)
warnings.simplefilter('ignore',LinAlgWarning)
from inputs import PARENTS,TREES,PLAN
assert __debug__
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for i,j in combinations(ids,2):
  for k in ids:
   if k in (i,j):continue
   w=[0]*9;w[a]=9;w[i]=w[j]=10;w[k]=7;out.append(w)
 return sorted(out)
def locate(p,extra,rows):
 nr=len(rows);coupled=nr==2;m=168*nr;nf=108 if coupled else 9;d=nf+1
 I=np.eye(9);edges=[(i,p[i]) for i in range(1,9)]+[extra]
 L=np.zeros((9,9,9));basis=[]
 for k,(i,j) in enumerate(edges):L[k,i,i]=2;L[k,i,j]=L[k,j,i]=-1
 for i in range(9):
  for j in range(i,9):
   b=np.zeros((9,9));b[i,j]+=1;b[j,i]+=1;basis.append(b)
 basis=np.array(basis);J=np.zeros((m,d,9,9))
 for r,a in enumerate(rows):
  for wi,ww in enumerate(weights(a)):
   t=168*r+wi;w=np.array(ww)/9
   for i in range(9):J[t,9*r+i]=np.outer(I[i],w)+np.outer(w,I[i])
   if coupled:
    J[t,18:63]=basis*(1 if r==0 else -1)
    J[t,63:108]=basis*(w[rows[1-r]]-181/180)
 J[:,-1]=-I;y=np.zeros(d);y[-1]=-1;u=np.full((m,9),1/9.)
 if coupled:
  k=63
  for i in range(9):
   for j in range(i,9):
    if i==j:y[k]=.0005
    k+=1
 def zmatrix(yy):return np.einsum('k,kij->ij',yy[63:108],basis)
 def matrix(yy,uu):return np.einsum('mdij,d->mij',J,yy,optimize=True)+np.einsum('mk,kij->mij',uu,L,optimize=True)
 B=matrix(y,u)
 for outer in range(8):
  tau=.05*.18**outer;fac=tau/m
  for inner in range(70):
   ch=np.linalg.cholesky(B);R=np.linalg.inv(B);C=R[:,None]@J;D=R[:,None]@L
   gy=-np.trace(C,axis1=2,axis2=3).sum(axis=0);gy[-1]-=1/fac
   gu=-np.trace(D,axis1=2,axis2=3)-1/u
   Hyy=np.einsum('mdij,meji->de',C,C,optimize=True)
   logz=0.
   if coupled:
    Z=zmatrix(y);zc=np.linalg.cholesky(Z);E=np.linalg.inv(Z)@basis
    gy[63:108]-=np.trace(E,axis1=1,axis2=2)
    Hyy[63:108,63:108]+=np.einsum('kij,lji->kl',E,E,optimize=True)
    logz=2*np.log(np.diag(zc)).sum()
   Huy=np.einsum('mkij,mdji->mkd',D,C,optimize=True)
   Huu=np.einsum('mkij,mlji->mkl',D,D,optimize=True)
   Huu[:,np.arange(9),np.arange(9)]+=1/u**2
   sol=np.linalg.solve(Huu,np.concatenate((Huy,np.ones((m,9,1)),gu[:,:,None]),axis=2))
   T=sol[:,:,:d];e=sol[:,:,d];v=sol[:,:,d+1]
   S=np.zeros((d+1,d+1));b=np.zeros(d+1)
   S[:d,:d]=Hyy-np.einsum('mkd,mke->de',Huy,T,optimize=True)
   S[:d,d]=-np.einsum('mkd,mk->d',Huy,e,optimize=True);S[d,:d]=S[:d,d];S[d,d]=-e.sum()
   b[:d]=-gy+np.einsum('mkd,mk->d',Huy,v,optimize=True);b[d]=v.sum();S=(S+S.T)/2
   try:step=solve(S,b,assume_a='sym',check_finite=False)
   except Exception:step=np.linalg.lstsq(S,b,rcond=1e-14)[0]
   dy=step[:d];du=-v-np.einsum('mkd,d->mk',T,dy,optimize=True)-e*step[d]
   descent=fac*(gy@dy+(gu*du).sum())
   if -descent<min(1e-7,tau*.001):break
   alpha=min(1.,.99*float(np.min(-u[du<0]/du[du<0]))) if np.any(du<0) else 1.
   old=-y[-1]-fac*(2*np.log(np.diagonal(ch,axis1=1,axis2=2)).sum()+np.log(u).sum()+logz)
   delta=matrix(dy,du)
   for back in range(60):
    yy=y+alpha*dy;uu=u+alpha*du;BB=B+alpha*delta
    try:
     chnew=np.linalg.cholesky(BB);lognew=0.
     if coupled:lognew=2*np.log(np.diag(np.linalg.cholesky(zmatrix(yy)))).sum()
     val=-yy[-1]-fac*(2*np.log(np.diagonal(chnew,axis1=1,axis2=2)).sum()+np.log(uu).sum()+lognew)
     if np.isfinite(val) and val<=old+.05*alpha*descent:break
    except np.linalg.LinAlgError:pass
    alpha*=.5
   else:raise ArithmeticError('LOCATOR_UNKNOWN')
   y,u,B=yy,uu,BB
  if y[-1]>1e-8:return y[:-1],u
 raise ArithmeticError('LOCATOR_UNKNOWN')
def symmetric(v):
 b=[[0]*9 for _ in range(9)];k=0
 for i in range(9):
  for j in range(i,9):b[i][j]+=v[k];b[j][i]+=v[k];k+=1
 return b
def positive(a):
 a=[r[:] for r in a];last=1
 for k in range(9):
  q=a[k][k]
  if q<=0:return False
  for i in range(k+1,9):
   for j in range(i,9):
    z=q*a[i][j]-a[i][k]*a[k][j];assert z%last==0;a[i][j]=a[j][i]=z//last
  last=q
 return True
def exact_matrices(p,extra,rows,g,u):
 O=symmetric(g[18:63]) if len(rows)==2 else [[0]*9 for _ in range(9)]
 Z=symmetric(g[63:108]) if len(rows)==2 else [[0]*9 for _ in range(9)]
 if len(rows)==2:assert positive(Z)
 edges=[(i,p[i]) for i in range(1,9)]+[extra]
 for r,a in enumerate(rows):
  h=g[9*r:9*r+9]
  for t,w in enumerate(weights(a)):
   v=20*w[rows[1-r]]-181 if len(rows)==2 else 0
   B=[[20*(h[i]*w[j]+w[i]*h[j])+180*(1 if r==0 else -1)*O[i][j]+v*Z[i][j] for j in range(9)] for i in range(9)]
   for (i,j),mu in zip(edges,u[168*r+t]):B[i][i]+=360*mu;B[i][j]-=180*mu;B[j][i]-=180*mu
   for i in range(9):B[i][i]-=1
   yield B
if __name__=='__main__':
 records=[];nm=0
 for k,(o,ex,rows) in enumerate(PLAN):
  g,u=locate(TREES[o],ex,rows);scale=max(np.max(np.abs(g)),np.max(np.abs(u)))
  g=np.rint(g/scale*10**8).astype(np.int64).tolist();u=np.rint(u/scale*10**8).astype(np.int64).tolist()
  assert all(x>=0 for r in u for x in r)
  for b in exact_matrices(TREES[o],ex,rows,g,u):assert positive(b);nm+=1
  records.append(dict(index=k,ordinal=o,extra=ex,rows=rows,g=g,mu=u))
  print('NEW_SHADOW_CERTIFICATE',k,o,list(ex),list(rows),len(u),flush=True)
 obj=dict(tag='NOVA24_F9_11_SHADOW_FRAMES_V1',parents=PARENTS,records=records)
 b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();Path('shadow_exact.json').write_bytes(b)
 assert nm==3024
 print('NEW_SHADOW_GENERATION_PASS',12,nm,6)
 print('DATA',len(b),hashlib.sha256(b).hexdigest())
```

### check.py

```python
"""Independent exact verifier; CPython3.13.5, standard library only.
No numerical producer imports. Scalar expansion, Bareiss, and Fraction LDL.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
from inputs import PARENTS,TREES,PLAN
assert __debug__
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for t in product((0,7,10),repeat=8):
  if sum(t)!=27 or t.count(10)!=2 or t.count(7)!=1:continue
  w=[0]*9;w[a]=9
  for i,v in zip(ids,t):w[i]=v
  out.append(w)
 assert len(out)==168 and len(set(map(tuple,out)))==168
 return sorted(out)
def expand(h,w,mu,edges,off,z,factor,sign):
 c={}
 def add(i,j,v):
  key=(min(i,j),max(i,j));c[key]=c.get(key,0)+v
 for i in range(9):
  for j in range(9):add(i,j,40*h[i]*w[j])
 for (i,j),v in zip(edges,mu):add(i,i,360*v);add(i,j,-360*v)
 k=0
 for i in range(9):
  add(i,i,-1)
  for j in range(i,9):add(i,j,360*sign*off[k]+2*factor*z[k]);k+=1
 a=[[0]*9 for _ in range(9)]
 for (i,j),v in c.items():
  if i==j:a[i][i]=v
  else:assert v%2==0;a[i][j]=a[j][i]=v//2
 return a
def bareiss(a):
 a=[r[:] for r in a];previous=1;out=[]
 for k in range(9):
  pivot=a[k][k];assert pivot>0;out.append(pivot)
  for i in range(k+1,9):
   for j in range(k+1,9):
    z=pivot*a[i][j]-a[i][k]*a[k][j];assert z%previous==0;a[i][j]=z//previous
  previous=pivot
 return out
def ldl(a,minors):
 L=[[F(i==j) for j in range(9)] for i in range(9)];D=[];prod=F(1)
 for k in range(9):
  pivot=F(a[k][k])-sum(L[k][j]**2*D[j] for j in range(k));assert pivot>0
  D.append(pivot);prod*=pivot;assert prod==minors[k]
  for i in range(k+1,9):L[i][k]=(F(a[i][k])-sum(L[i][j]*L[k][j]*D[j] for j in range(k)))/pivot
if __name__=='__main__':
 raw=Path('shadow_exact.json').read_bytes();obj=json.loads(raw)
 assert raw==serial(obj) and obj['tag']=='NOVA24_F9_11_SHADOW_FRAMES_V1'
 assert obj['parents']==[list(p) for p in PARENTS] and len(obj['records'])==len(PLAN)==12
 streams={k:hashlib.sha256() for k in ('weights','matrices','minors','couplings')};nm=0;nz=0;nfree=0;nmu=0
 for ix,(o,ex,rows) in enumerate(PLAN):
  r=obj['records'][ix];assert (r['index'],r['ordinal'],r['extra'],r['rows'])==(ix,o,list(ex),list(rows))
  g=r['g'];mu=r['mu'];assert len(g)==(108 if len(rows)==2 else 9) and all(type(v) is int for v in g)
  assert len(mu)==168*len(rows) and all(len(u)==9 and all(type(v) is int and v>=0 for v in u) for u in mu)
  off=g[18:63] if len(rows)==2 else [0]*45;z=g[63:108] if len(rows)==2 else [0]*45
  edges=[(i,TREES[o][i]) for i in range(1,9)]+[ex]
  assert len(set(edges))==9
  if len(rows)==2:
   Z=[[0]*9 for _ in range(9)];k=0
   for i in range(9):
    for j in range(i,9):Z[i][j]=Z[j][i]=(2 if i==j else 1)*z[k];k+=1
   minors=bareiss(Z);ldl(Z,minors);nz+=1;streams['couplings'].update(serial([ix,Z,minors]))
  for ri,a in enumerate(rows):
   for wi,w in enumerate(weights(a)):
    factor=20*w[rows[1-ri]]-181 if len(rows)==2 else 0
    A=expand(g[9*ri:9*ri+9],w,mu[168*ri+wi],edges,off,z,factor,1 if ri==0 else -1)
    minors=bareiss(A);ldl(A,minors)
    for key,val in [('weights',w),('matrices',A),('minors',minors)]:streams[key].update(serial([ix,a,wi,val]))
    nm+=1
  nfree+=len(g);nmu+=sum(map(len,mu));print('EXACT_NEW_SHADOW_PASS',ix,o,list(ex),len(mu),flush=True)
 assert (nm,nz,nfree,nmu)==(3024,6,702,27216)
 report=dict(tag='NOVA24_F9_11_SHADOW_VERIFIED_V1',parents=PARENTS,cases=len(PLAN),matrices=nm,coupling_matrices=nz,positive_leading_minors=9*(nm+nz),free_integers=nfree,multiplier_integers=nmu,coefficient_bytes=len(raw),coefficient_sha256=hashlib.sha256(raw).hexdigest(),streams={k:v.hexdigest() for k,v in streams.items()})
 b=serial(report);Path('shadow_verified.json').write_bytes(b)
 print('INDEPENDENT_SCALAR_BAREISS_FRACTION_LDL_PASS',nm,nz,9*(nm+nz))
 print('ONE_PHYSICAL_LAMBDA_RECIPROCAL_PAIR_AVERAGING_PASS')
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
```

### cover.py

```python
"""Exact old-cover intersection with newly certified nine-arrow subgraphs.
No geometry samples. Standard library only. Run after check.py.
"""
from itertools import permutations,combinations,product
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from inputs import TREES,OLD,NEW,PLAN
assert __debug__
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def tree_code(p):
 ch=[[] for _ in p]
 for i in range(1,9):ch[p[i]].append(i)
 def walk(i):return '('+''.join(sorted(walk(j) for j in ch[i]))+')'
 return walk(0)
def rooted(p):
 for i in range(1,9):
  seen=set()
  while i:
   if i in seen:return False
   seen.add(i);i=p[i]
 return p[0]==0
def determinant(a):
 a=[list(map(F,r)) for r in a];out=F(1)
 for k in range(len(a)):
  j=next((j for j in range(k,len(a)) if a[j][k]),None)
  if j is None:return F(0)
  if j!=k:a[j],a[k]=a[k],a[j];out=-out
  p=a[k][k];out*=p
  for i in range(k+1,len(a)):
   t=a[i][k]/p
   for j in range(k,len(a)):a[i][j]-=t*a[k][j]
 return out
@lru_cache(None)
def canonical(edges):
 # Complete root-preserving isomorphism test; degree classes only prune.
 groups=defaultdict(list)
 for i in range(1,9):groups[(sum(b==i for a,b in edges),sum(a==i for a,b in edges))].append(i)
 parts=[groups[k] for k in sorted(groups)];starts=[];n=1
 for c in parts:starts.append(n);n+=len(c)
 best=None;bestpi=None
 for ps in product(*(permutations(c) for c in parts)):
  pi=[0]*9
  for st,pp in zip(starts,ps):
   for k,i in enumerate(pp):pi[i]=st+k
  code=tuple(sorted((pi[i],pi[j]) for i,j in edges))
  if best is None or code<best:best=code;bestpi=pi
 return best,bestpi
if __name__=='__main__':
 v=json.loads(Path('shadow_verified.json').read_text());raw=Path('shadow_exact.json').read_bytes()
 assert v['tag']=='NOVA24_F9_11_SHADOW_VERIFIED_V1' and v['cases']==12 and v['matrices']==3024 and v['coupling_matrices']==6
 assert v['coefficient_sha256']==hashlib.sha256(raw).hexdigest()
 bad={}
 for k,(o,ex,rows) in enumerate(PLAN):
  es=tuple(sorted([(i,TREES[o][i]) for i in range(1,9)]+[ex]));code,pi=canonical(es)
  assert code not in bad;bad[code]=(k,pi,es)
 allowed={tree_code(p) for p in TREES.values()};reports=[];oldtotal=0;newtotal=0;maxarcs=0;maxtrees=0;subsets=0;single=[]
 for o,p in TREES.items():
  base={(i,p[i]) for i in range(1,9)};optional=sorted(set(tuple(e) for fr in OLD[o] for e in fr));oldgraphs=[]
  for mask in range(1<<len(optional)):
   subsets+=1;extra=tuple(e for j,e in enumerate(optional) if mask>>j&1);edges=tuple(sorted(base|set(extra)))
   choices=[(0,)+q for q in product(*(sorted(j for a,j in edges if a==i) for i in range(1,9)))]
   if not all(rooted(q) and tree_code(q) in allowed for q in choices):continue
   L=[[0]*9 for _ in range(9)]
   for i,j in edges:L[i][i]+=1;L[i][j]-=1
   assert determinant([r[1:] for r in L[1:]])==len(choices)
   oldgraphs.append((extra,edges,len(choices)))
  maximal=[x for x,e,n in oldgraphs if not any(set(x)<set(y) for y,_,_ in oldgraphs)]
  assert {tuple(sorted(x)) for x in maximal}=={tuple(sorted(fr)) for fr in OLD[o]}
  kept=[];covered=[]
  for extra,edges,count in oldgraphs:
   witness=None
   for es in combinations(edges,9):
    if {a for a,b in es}!={1,2,3,4,5,6,7,8}:continue
    code,pi=canonical(es)
    if code not in bad:continue
    k,srcpi,srces=bad[code];inverse=[pi.index(i) for i in range(9)];transport=[inverse[srcpi[i]] for i in range(9)]
    assert sorted(transport)==list(range(9)) and transport[0]==0
    assert tuple(sorted((transport[i],transport[j]) for i,j in srces))==es
    witness=dict(certificate=k,permutation=transport,subgraph=es);break
   if witness is None:
    kept.append((extra,count));maxarcs=max(maxarcs,len(edges));maxtrees=max(maxtrees,count)
   else:
    covered.append(dict(extra=extra,**witness))
    if len(extra)==1:single.append([o,extra[0]])
  newmax=[(x,n) for x,n in kept if not any(set(x)<set(y) for y,_ in kept)]
  assert {tuple(sorted(fr)) for fr,n in newmax}=={tuple(sorted(fr)) for fr in NEW[o]}
  oldtotal+=len(oldgraphs);newtotal+=len(kept)
  reports.append(dict(ordinal=o,parent=p,old_count=len(oldgraphs),remaining=[dict(extra=x,trees=n) for x,n in kept],maximal=[dict(extra=x,trees=n) for x,n in newmax],excluded=covered))
  print('NEW_FRAME_COVER',o,len(oldgraphs),len(kept),len(newmax),flush=True)
 assert (subsets,oldtotal,newtotal,maxarcs,maxtrees,len(single))==(592,82,25,10,4,21)
 assert sum(len(r['maximal']) for r in reports)==11
 obj=dict(tag='NOVA24_F9_11_FRAME_COVER_V1',old_subsets=subsets,old_graphs=oldtotal,excluded_graphs=oldtotal-newtotal,remaining_graphs=newtotal,maximal_frames=11,maximum_arcs=maxarcs,maximum_trees=maxtrees,forbidden_single_extras=single,records=reports)
 b=serial(obj);Path('shadow_cover.json').write_bytes(b)
 print('EXHAUSTIVE_NEW_COVER_PASS',592,82,57,25,11,10,4)
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
 print('FIVE_FORMS_REMAIN_NO_NEW_C32_WHOLE_TYPE_OR_GLOBAL_BOUND')
```

### ablation.py

```python
"""Exact counterterm-omission audit. Does not assert physical feasibility.
Run after check.py; imports its exact arithmetic, never the numerical code.
"""
import json,hashlib
from pathlib import Path
from inputs import TREES,PLAN
from check import weights,expand,bareiss,ldl,serial
assert __debug__
raw=Path('shadow_exact.json').read_bytes();obj=json.loads(raw)
v=json.loads(Path('shadow_verified.json').read_text())
assert v['coefficient_sha256']==hashlib.sha256(raw).hexdigest()
direct=0;monotone=0;unchanged=0
for r,(o,ex,rows) in zip(obj['records'],PLAN):
 if len(rows)==1:unchanged+=168;continue
 g=r['g'];edges=[(i,TREES[o][i]) for i in range(1,9)]+[ex]
 for ri,a in enumerate(rows):
  for wi,w in enumerate(weights(a)):
   if 20*w[rows[1-ri]]-181<=0:monotone+=1;continue
   A=expand(g[9*ri:9*ri+9],w,r['mu'][168*ri+wi],edges,g[18:63],[0]*45,0,1 if ri==0 else -1)
   ldl(A,bareiss(A));direct+=1
assert (direct,monotone,unchanged)==(504,1512,1008)
report=dict(tag='NOVA24_SHADOW_COUPLING_OMISSION_V1',direct=direct,PSD_monotonicity=monotone,unchanged=unchanged,all_matrices_without_counterterm_PD=True)
b=serial(report);Path('omission.json').write_bytes(b)
print('EXACT_COUPLING_OMISSION_PASS',3024,'DIRECT',direct,'PSD_MONOTONICITY',monotone,'UNCHANGED',unchanged)
print('NO_COUPLING_ESSENTIALITY_OR_PHYSICAL_WITNESS_CLAIM')
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
```

### replay.py

```python
"""Source-only or frozen replay of NEW nine-pole shadow-graph exclusions.
Save all six source units together, UTF-8/LF/final LF.
Full: python -S replay.py. Frozen: python -S replay.py check.
The 281 parent matrices are NOT a reconstruction input and are NOT replayed.
"""
from pathlib import Path
import hashlib,os,subprocess,sys
assert __debug__
S={'inputs.py': [1569, 'f268a0f9923c2c74b6b8b1c14a542e0b6b2e6b59fe80883ae983a02f382e841e'], 'make.py': [5786, '3e11bedf8f61ba71c028b374bd08f97d0b41b302f5bc1af7ea879a4a128cdc84'], 'check.py': [3973, '3b8c45780c9441d26bb806a77a533cb6e47cb5f425cfc8ea02bcd46caaa2b9eb'], 'cover.py': [5016, '1308a7db5d3059b3489e754476666db6328ee8d1155bd2f00754086877d900c8'], 'ablation.py': [1384, 'ef05b97ab9ffc5952ab4034fe11634c9f1a2a91002489e19546918df47b7122d']}
O={'shadow_exact.json': [251836, '1cf29f366fc666b1e41fd8f8a9a7df3739123a3ba0701c93f3fb13d2c31efd99'], 'shadow_verified.json': [820, '97f5dc06484139d4a383ca1b42aec9e1f033102ebaac6aa3fa1db1914708ee81'], 'shadow_cover.json': [10036, '5bad625f9a57c514229749b6d6b4b2e2f2d4a1bed1d2f4a6c39ade6c120fff0b'], 'omission.json': [142, 'f0a6682f19624cc32757457a1503fefef3512f33c8f4df443cb707ad6b5f4049'], 'make.log': [662, 'aa8722776a5620610e99d793308c3bd28fe5aaa1d8f27e588fce3adbe367e87a'], 'check.log': [655, '49907278c7085d6844d61c44e612f0b32e552f544fd940b44c1a19f267d0f834'], 'cover.log': [315, 'c899dddb6b3503d5596ff656f6da6e4d77a55d9f6dc531552a978ce0e14822ad'], 'ablation.log': [209, 'de2029939a4224bd30756cef862f8bb02df5530c88bcf3d6044c6d55fd506ad5']}
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
for n,w in S.items():assert pin(Path(n).read_bytes())==w,('SOURCE_PIN',n)
mode=sys.argv[1] if len(sys.argv)>1 else 'all';assert mode in ('all','check')
def run(args,log):
 env=os.environ.copy()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
 env['PYTHONHASHSEED']='0'
 p=subprocess.run([sys.executable]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
 Path(log).write_bytes(p.stdout);sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
 assert p.returncode==0,('CHILD_EXIT',args,p.returncode)
if mode=='all':run(['make.py'],'make.log')
assert pin(Path('shadow_exact.json').read_bytes())==O['shadow_exact.json']
run(['-S','check.py'],'check.log');run(['-S','cover.py'],'cover.log');run(['-S','ablation.py'],'ablation.log')
for n,w in O.items():
 if n=='make.log' and mode=='check':continue
 assert pin(Path(n).read_bytes())==w,('OUTPUT_PIN',n)
for n,w in S.items():assert pin(Path(n).read_bytes())==w,('SOURCE_CHANGED',n)
print('ALL_NEW_SOURCE_COEFFICIENT_STREAM_COVER_PINS_PASS')
print('NOVA24_F9_11_SHADOW_FRAMES_COMPLETE_REPLAY_PASS')
print('FIVE_FORMS_UNCLOSED_NO_F10_C34_OR_WHOLE_TYPE_PROMOTION')
```

## 8. Continuation

The durable new checkpoint is the 12-configuration integer proof and its exact 57-exclusion/25-remainder cover. It is smaller than another universal tree reconstruction and directly supplies stronger all-pair constraints to genuine incidence work.

The remaining optional shadows are confined to the tail configurations in the 11-frame table. A useful next certificate should impose those surviving simultaneous arrows together with the actual matrix-square equations and genuine triangular-chain area/volume data. The three-chain positive pivot remains legitimate; any four-row reduction must explicitly retain its positive, negative and singular strata. Both actual primal complementary choices must be retained until their transported dual constraints are checked.

**Final boundary:** 57 old base-labelled shadow graphs excluded; 11 maximal frames remain, with at most ten nonnegative pairs and four escape trees. Forms 253 and 285 have unique complete nonnegative trees. All five whole forms remain unexcluded. The exact deletion audit shows that the present improvement does not yet require the stronger physical pair-volume coupling, and no matrix-square-driven whole-form or canonical-type exclusion is claimed.
