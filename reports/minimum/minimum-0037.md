# minimum-0037

AI research report · 2026-09-10 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_CAP9_NEW_281_RESTORED_V1

## 1. Determination and authority

**The 281-of-286 universal nine-pole capped-row escape-tree theorem has been re-established by a new complete executable proof.** The exact uncovered ordinals are **253, 266, 272, 278, 285**, with the five literal parent arrays below. This turn generated and independently verified **51,912 integer symmetric 9-by-9 matrices and 467,208 positive leading principal minors**. The 25-frame consequence has also been replayed, with its previously conditional five-form premise now discharged by the new certificates.

The theorem includes **weak escape equalities, all real positive-definite reciprocal metrics, and arbitrarily small positive actual cone volumes**. Application uses rows of one actual original-body Lambda at its ordinary uniform-volume centroid. Convex decomposition weights are not fitted physical masses; the polar is not assumed uniformly centred.

Specification parent: `minimum-0035`, SHA-256 `8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36`. I used its literal specification and discrete plans, not its unavailable predecessor coefficients as evidence. The current journal explicitly records the malformed original publication and the conditional status of the previous graph replay. No tree/C32-label conflict was found in the specification used here.

**These are new source and coefficient bytes.** The old four source units remain unavailable. The old decoder's claimed `11977 / 5b568871fbf047909ed0c738c8f4df4fc61985d99492bfb14e5f7358d18e8c14` identity is not recovered, and no new output is represented as matching the old historical matrix-stream pins.

**No additional survivor exclusion using the matrix-square or triangle-chain volume constraints is certified here.** The five remaining forms are unexcluded, not declared physically realizable. The accepted research register remains `32<=C_min<=1374`, with the same 17 whole C32 types `{33,34,72,139,149,152,159,163,164,178,192,217,284,288,293,294,295}` excluded. The unpersisted coordinator 7954 package is not promoted. No new `F>=10`, `V>=10`, `C>=34`, named whole-type exclusion, or attainer is claimed.

## 2. Exact tree coverage and complete complement

These are **rooted-tree ordinals, not canonical C32 map IDs**. They index lexicographically sorted canonical preorder parent arrays; `p[0]=0`, and each selected arrow is `i -> p[i]`.

```text
253 (0,0,1,2,3,4,5,0,7)
266 (0,0,1,2,3,4,5,4,0)
272 (0,0,1,2,3,4,5,5,0)
278 (0,0,1,2,3,4,5,6,0)
285 (0,0,1,2,3,4,5,6,7)
```

The entire discrete plan, repeated literally in producer and checker, is:

```python
rows01=[246,247,248,249,250,251,260,261,262,263,264,265,
        267,268,269,270,271,273,274,275,276,279,280,281]
rows02=[277,282,283,284]
remaining=[253,266,272,278,285]
```

Every excluded ordinal outside `rows01` and `rows02` uses coefficient row 0 alone. Thus the proof has 253 single-row records, 24 records using rows 0 and 1, and four records using rows 0 and 2: **281 tree records, 309 row instances, and 168 extremes per row**. These row indices are not alternative physical centres or cone apices. No vertex or excursion is deleted or contracted.

The producer canonicalizes all `8!=40320` increasing parent arrays. The independent checker separately enumerates multisets of smaller rooted subtrees and compares the resulting complete set with its own increasing-array enumeration. Both counts are

`[1,1,2,4,9,20,48,115,286]`

for sizes one through nine. The checker also verifies all five literal ordinal/array bindings. Every rooted tree admits a parent-before-child labelling, so this finite enumeration covers every labelled tree up to the certificate's permutation-equivariance.

## 3. Proof and actual physical scope

### One actual body and one actual Lambda

Let the original full-dimensional homogeneous polytope have its actual volume centroid at 0, volume V, actual facet poles `q_i` with `q_i.x<=1`, facet areas `A_i`, distances `h_i`, and uniform-area centroids `c_i`. Define

```text
omega_i=A_i h_i/(3V),
Lambda_ai=3 omega_i(1-q_a.c_i).
```

Coning an actual facet to the actual centroid gives volume `omega_i V` and centroid `3c_i/4`. Ordinary centring and divergence give

```text
sum omega_i=1,
sum omega_i c_i=0,
sum omega_i q_i=0,
3 sum omega_i c_i q_i^T=I_3.
```

Consequently the **same** physical Lambda has zero diagonal, positive off-diagonal entries, row sums three, and `Lambda Q=-Q`. The accepted physical trace theorem supplies the simultaneous bound `Lambda_ai<=c3<10/9`, where

`c3=max_(r>=0) 3(1+2r+3r^2)/[(1+r+r^2)(3+2r+r^2)]`.

This turn proves the finite capped-row implication, not that earlier trace theorem. The algebraic proof includes the closed cap 10/9 and zero coefficients, while its physical application uses the actual areas, centroids and cone volumes just defined. Arbitrary capped rows are not asserted to be physical.

For any primal physical metric `M>0`, use its single reciprocal metric `N=M^-1`, and put `H=Q N Q^T`. H is nonzero PSD, and has rank three for the actual body. The certificate argument does not need a rank bound, a condition-number bound, a coordinate box, or a positive lower bound on any cone volume.

### Every extreme coefficient row

The eight off-diagonal coefficients of each row belong to

`K={s: 0<=s_i<=10/9, sum s_i=3}`.

At a vertex of K at most one coordinate is strictly between its bounds: otherwise two such coordinates can be perturbed oppositely. The sum condition then forces exactly two entries 10/9, one 7/9, and five zeros. Hence there are exactly `C(8,2)*6=168` vertices.

For row a and distinct non-a indices i,j,k, with i<j, use the integer vector

`w=9e_a+10e_i+10e_j+7e_k`.

The actual row has some convex decomposition `rho_a,w>=0`, of total one, satisfying

`Q^T sum_w rho_a,w w=0`.

The rho are an algebraic decomposition of an actual row; they are not fitted tetrahedral masses. Every extreme vector, including all closed-boundary zeros, is covered.

### Exact integer matrices and the averaging contradiction

For each chosen arrow i->p[i], define

`L_i=2e_i e_i^T-e_i e_p[i]^T-e_p[i] e_i^T`.

A weak escape is `A_i,p=q_i^T N(q_p-q_i)>=0`; therefore `trace(L_i H)=-2A_i,p<=0`.

Each record provides integer vectors `gamma_a`, nonnegative integers `mu_a,w,i`, and constant symmetric offsets `O_a` of total zero. A single-row record has zero offset. A two-row record uses K and -K; its 45 upper-triangular coefficients contribute twice their value on a diagonal and their value at each off-diagonal position.

The exact matrices are

`B_a,w=gamma_a w^T+w gamma_a^T+9 sum_i mu_a,w,i L_i+9 O_a`.

**All 51,912 matrices satisfy `B_a,w-I_9>0`.** The independent checker expands the scalar quadratic polynomial, reconstructs its symmetric matrix, checks all positive leading determinants by integer Bareiss elimination, and separately computes a Fraction LDL factorization whose nine positive pivot products agree exactly with the Bareiss determinants.

Average the matrices using each selected row's actual rho and sum over the rows. The gamma terms vanish by the actual row equations. The offsets cancel because each convex decomposition has total one. Every escape term is nonpositive. The pairing of this sum with H is therefore nonpositive.

But every matrix is strictly above I, each selected row has convex weights of total one, and H is nonzero PSD. The same pairing is strictly positive. This contradiction excludes the whole continuous weak-escape domain of that tree. Solver normalizations constrain only the separating coefficients, never the physical body.

### Why an S1 body supplies a true-edge tree

A strictly stable facet corresponds at the same origin to a strictly unstable pole in N. Every other pole has a nonnegative escape along an actual dual edge. Along any selected arrow between distinct poles,

`||q_p||_N^2-||q_i||_N^2=2A_i,p+||q_p-q_i||_N^2>0`.

Thus even weak escape ties cannot create a cycle. With the unique strictly stable facet at root 0, the arrows form a tree. The exhaustive exclusions leave precisely the five arrays above. Every weak escape tree has one of those forms. In particular there is a true-dual-edge ascent path of at least six edges; this is not a shortest-path or diameter assertion for the full dual graph.

## 4. The 25 maximal frames: the premise is now proved

The full literal `FRAMES` table is in `frames.py` below; every listed inner set is added to its base tree's eight arrows. No continuation-critical frame is omitted.

For a fixed surviving tree, an additional nonnegative arrow to a descendant would create a strict-norm-increase cycle. Any other additional arrow, substituted for its source's parent, must produce another one of the five surviving shapes. This leaves respectively 7, 6, 7, 8, and 4 individually possible additional arrows.

The exact checker exhausts all 592 subsets of those possibilities. It tests acyclicity, every parent choice, canonical rooted shapes, and an independent directed Laplacian cofactor count. The observed results are:

```text
TREE ordinal   possible extra arrows   retained subsets   maximal frames
253            7                       12                 5
266            6                       20                 4
272            7                       26                 6
278            8                       19                 6
285            4                        5                 4
```

The 82 retained graphs are **base-tree-labelled graphs**, not 82 isomorphism classes or physical bodies. Their 25 inclusion-maximal frames form an exhaustive outer cover. Consequently an actual nine-pole S1 body has **at most 11 nonnegative unequal directed pole-shadow pairs, at least 61 strictly negative pairs, and at most eight weak rooted escape arborescences**. Any actual graph is a subgraph of one of these frames containing its chosen base tree; pairs outside that frame are strictly negative.

The graph argument also tests nonadjacent pairs. True incidence is needed when selecting mechanical dual-edge trees or complementary cotrees, not for the stronger all-pair sign restriction.

For the inherited joint C32 application, the two possible primal candidates remain

```text
T     =(0,0,1,2,3,4,5,6,0)
T_alt =(0,0,8,2,3,4,5,6,0).
```

The second requires the actual edge 28 and its proper sign. Necessary matching selects **some** sign-compatible complementary pair, not a freely prescribed pair. Terminal triangle 567 is a nonroot cotree leaf exiting across edge 57. Its allowed template labels and cotree depths are

```text
253: label6/depth6, label8/depth2
266: label6/depth6, label7/depth5, label8/depth1
272: label6/depth6, label7/depth6, label8/depth1
278: label7/depth7, label8/depth1
285: label8/depth8.
```

Thus cotree depths three and four remain excluded, now with a recoverable five-form certificate premise. This does not count any new catalogue cases or whole types; no true-incidence catalogue sweep was performed here.

## 5. What was implemented and actually executed

### New numerical producer

`engine.py` is a new structured log-barrier implementation, not a reconstruction of unavailable old source. For m extreme-row blocks, it uses global free gamma/offset variables, eight local nonnegative escape multipliers per block, and a common margin t. Writing the numerical block with w/9 instead of w, the barrier objective is

`-t-(tau/m)[sum_blocks logdet(B_numeric-t I)+sum_all_multipliers log(mu)]`

with the coefficient normalization `sum_all_multipliers mu=m`. The integer certificate formula above is the corresponding expression multiplied by nine after rationalization.

All numerical choices are explicit: initial t=-1, zero free coefficients, every multiplier 1/8; `tau=0.05*0.18**outer`; at most 12 outer rounds and 70 Newton steps per round; decrement tolerance `min(1e-7,tau*0.001)`; positivity step factor 0.99; Armijo factor 0.05; at most 60 halvings; symmetric linear solve with `rcond=1e-14` least-squares fallback; acceptance candidate margin `t>1e-8`; max-absolute-coefficient normalization and `np.rint` at scale `10**8`. Newton's local multiplier blocks are eliminated before the global solve.

These are locator settings, not mathematical bounds on geometry or physical metrics. The producer accepts a record only after exact integer elimination proves every `B-I` positive definite. Ordinal 0 instead uses the small exact seed below; the other 280 records are numerically generated and then exact-checked.

### Independent proof checker

`verify.py` imports neither engine nor builder. Its independent cap-vertex enumeration filters all eight-tuples in `{0,7,10}^8`; its matrix reconstruction expands scalar monomials rather than using the producer's matrix assembly. Every one of the 51,912 shifted matrices is checked by both full integer Bareiss elimination and a separate `Fraction` LDL factorization, with all nine pivot products compared.

The output contains 4041 free coefficient integers and 415296 nonnegative multiplier integers. These are separating-certificate coefficients, not values of the physical Lambda.

### Environment and observed boundaries

Final observed environment:

```text
CPython 3.13.5, GCC 14.2.0, Linux x86_64
NumPy 2.3.5
SciPy 1.17.0
threadpoolctl 3.6.0
NumPy OpenBLAS 0.3.30 / Haswell / one thread
SciPy OpenBLAS 0.3.30 / Haswell / one thread
One producer process; no randomness.
```

This is **Haswell, not the old claimed SkylakeX environment**. Explicit runtime `threadpool_limits(1)` is included because the environment can preload numerical libraries before source-level environment settings.

Two clean reconstructions of the final source produced identical coefficient, independent-check and frame bytes. The second ran through the complete `replay.py` driver with **observed exit status 0**. A separate frozen `replay.py check` also completed with **observed exit status 0**. These are new executions, not the old recorded logs. The independent exact check is implementation-independent of the numerical producer, not external peer review or proof-assistant formalization.

An earlier long invocation timed out and was not counted as a complete replay. Preliminary coefficients produced before controlling a preloaded BLAS threadpool are not this checkpoint. The pinned final sources and final outputs below supersede those development attempts.

### Physical strengthening: no further exclusion promoted

After obtaining recoverable integer certificates, I explored adding reciprocal-volume coupling between actual coefficient rows. No additional tree-form exclusion from that exploration is certified here. Numerical non-success is not evidence of feasibility or impossibility, and experimental arrays are not promoted as successor checkpoints.

A precise analytic continuation is available. For `x=Lambda_ab`, `y=Lambda_ba`, and the actual pair-hull volume fraction r, the inherited physical inequality is `xy<=r^2`, with `0<=x,y<=10/9`. It comes from the same actual facet traces, not independently fitted masses.

The exact identity

`100+81r^2-90(x+y)=(10-9x)(10-9y)+81(r^2-xy)`

therefore gives `x+y<=10/9+9r^2/10`. An actual triangular-chain hull upper bound R also bounds each contained pair hull, yielding `k=10/9+9R^2/10`. A common PSD certificate multiplier Z can then enter the two row blocks as `(s_ab-k/2)Z` and `(s_ba-k/2)Z`; actual averaging contributes `(x+y-k)Z`, whose pairing with the same H is nonpositive. At R=1, k=181/90. This specifies a coupled certificate extension, **not a newly closed tree or incidence class**.

The actual identity `Lambda^2+Lambda=12*1*omega^T` and the inherited triangular-chain minor theorem remain additional physical constraints. They are not used in the restored 281-tree proof and have not closed any of its five forms in this turn.

## 6. Self-contained recovery capsule, checkpoint and pins

Save all five complete source units in §7 together, UTF-8/LF with a final LF, in an empty directory. No old sandbox, journal, coefficient checkpoint, catalogue or network-fetched mathematical input is required for full generation.

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python -S replay.py > full.log
python -S replay.py check > frozen.log
python -S replay.py seed
```

Use CPython 3.13.5 and the numerical backend above for the pinned byte-identical reconstruction. The frozen checker and seed mode use only the standard library. On a different numerical backend, changed coefficients must pass the independent checker and receive their own pins; they must not be described as this byte-identical checkpoint.

The full driver verifies every source pin, reconstructs all coefficients, runs the independent exact checker, exhausts the frame graphs, and checks all coefficient/report/log pins. `check` skips numerical generation but requires the exact frozen coefficient file. `seed` checks only the small exact record and explicitly does **not** claim a 281-tree replay.

### Small exact continuation checkpoint

The following complete formula reconstructs record 0 of the full checkpoint:

```text
ordinal=0
parent=(0,0,0,0,0,0,0,0,0)
selected_rows=[0]
gamma=(900,9,9,9,9,9,9,9,9)
offset=0
for every row-0 extreme w:
    mu_i=100*w_i+9, for i=1,...,8.
```

The complete extreme-vector generator is in the sources. This formula gives all 168 matrices without any numerical dependency; root/leaf cross entries cancel exactly. `replay.py seed` reconstructs `seed0.json` and checks its 168 matrices by both exact methods. The seed is a genuine record of the full theorem, not an unrelated smoke test. The full 281-record checkpoint remains deterministically reconstructible from all five sources.

### Byte and SHA-256 pins

| File | Bytes | SHA-256 |
|---|---:|---|
| `engine.py` | 3924 | `382527ea22bb7a02d448ac2eb1f9c1b5785f15384df6c9248f1639714b87ab00` |
| `build.py` | 2924 | `7ee0832cf805272cc47e587dff7a8710250eef481b7a5ca55af9e36633dcec78` |
| `verify.py` | 5792 | `c572e6bb3ff4ef19db498b436972f4304229ab3f26562a74a179765519bea8f9` |
| `frames.py` | 4681 | `c4389bb0b7e05e0c0294f1214fe29eb8b913c6fadd94d902681c9c52795e4158` |
| `replay.py` | 3114 | `93968859a1d831acf122fb7291639787061f32044c6e718aefa8a67f6b5dddc3` |
| `cap9_new.json` | 3829595 | `b0cfc1a3d46eec19e3e5d0f1603de276edb45da7cc06b069e7299b4c1ae7654c` |
| `cap9_checked.json` | 817 | `3e23d591677593fa852949daf2642c45f556b73d1da0b755d42818f1572167ac` |
| `frames_new.json` | 1616 | `d21bf29911fc161ad993af4267e8b57dc3f8a9f9b85908283a0141c67360a988` |
| `seed0.json` | 4455 | `2e45acd9ffdd7a7eab8251713114d36599b83d03259d1b146080a73ebe231455` |
| `build.log` | 440 | `57a4d7214ccc6c95a481cb295f0a67e53e629c0a061ffb53484ce3282719d3bb` |
| `verify.log` | 720 | `1c2f9948ca653242b9080d82af7bb218e598cc1ba9ec070b156f62d17b9f85fd` |
| `frames.log` | 305 | `abf49bcced761cc9f3055a0ece58a2342b34b93498a89a9654ac343bd97f0999` |
| `full.log` | 1664 | `a1be74e95118a3be422f8d7581326a37d9d3ac88fc1df8a6cec6389adb0d02d6` |
| `frozen.log` | 1224 | `a5ae27199c669eb01549b98963c86c1dd618632e32b48ccfac7cc60c8e858678` |

All checkpoint and report JSON uses `json.dumps(...,sort_keys=True,separators=(',',':'))`, UTF-8, and a final LF. The canonical tree array and the independent stream pins are:

| Exact stream | SHA-256 |
|---|---|
| 286 canonical parent arrays | `da3053088269e80f5369da69d69dc96e0c74ce7247db66a7eb9cbecd03cb66cb` |
| leading_minors | `405084e707751e4a0e238af3659a2317aaf92183e54a5809799111d2c7f3ebc8` |
| shifted_matrices | `ddf0d4409dd59b279240e23e3b5537a334244695741201c36e9565a976141693` |
| weights | `3b50a97469f5ffc9d24a8152babbbf67799289ba74668bf12f6201c5b96fb458` |

The independent stream order is increasing excluded tree ordinal, then selected-row order, then the two 10-indices in lexicographic order, then the 7-index in ascending order. The checker appends canonical JSON/LF records respectively of the forms

```text
[ordinal,row,extreme_index,w]
[ordinal,row,extreme_index,B_minus_I]
[ordinal,row,extreme_index,nine_leading_principal_minors].
```

The frame JSON matches the prior conditional graph object's bytes because the graph consequence itself is unchanged. Its matrix-proof premise is now supplied by the new exact certificate; this is not a claim to have recovered the old graph source.

### Observed complete source-only replay transcript

```text
EXACT_LITERAL_STAR_CHECKPOINT_PASS 0 168
NEW_CAP9_GENERATED 0 168
NEW_CAP9_GENERATED 25 168
NEW_CAP9_GENERATED 50 168
NEW_CAP9_GENERATED 75 168
NEW_CAP9_GENERATED 100 168
NEW_CAP9_GENERATED 125 168
NEW_CAP9_GENERATED 150 168
NEW_CAP9_GENERATED 175 168
NEW_CAP9_GENERATED 200 168
NEW_CAP9_GENERATED 225 168
NEW_CAP9_GENERATED 250 336
NEW_CAP9_GENERATED 275 336
NEW_CAP9_INTEGER_GENERATION_PASS 281 51912
DATA 3829595 b0cfc1a3d46eec19e3e5d0f1603de276edb45da7cc06b069e7299b4c1ae7654c
TWO_INDEPENDENT_TREE_ENUMERATIONS_PASS [1, 1, 2, 4, 9, 20, 48, 115, 286] 40320
EXACT_CAP9_TREE_PASS 0 168
EXACT_CAP9_TREE_PASS 25 168
EXACT_CAP9_TREE_PASS 50 168
EXACT_CAP9_TREE_PASS 75 168
EXACT_CAP9_TREE_PASS 100 168
EXACT_CAP9_TREE_PASS 125 168
EXACT_CAP9_TREE_PASS 150 168
EXACT_CAP9_TREE_PASS 175 168
EXACT_CAP9_TREE_PASS 200 168
EXACT_CAP9_TREE_PASS 225 168
EXACT_CAP9_TREE_PASS 250 336
EXACT_CAP9_TREE_PASS 275 336
ALL_CAP_EXTREME_ROWS_EXACTLY_COVERED_PASS 309 51912
INDEPENDENT_SCALAR_BAREISS_FRACTION_LDL_PASS 51912 467208
NEW_281_OF_286_UNIVERSAL_CAP9_THEOREM_PASS [253, 266, 272, 278, 285]
REPORT 817 3e23d591677593fa852949daf2642c45f556b73d1da0b755d42818f1572167ac
NO_F10_V10_C34_OR_WHOLE_C32_TYPE_ASSERTION
FRAMES_RECHECK 253 7 12 5
FRAMES_RECHECK 266 6 20 4
FRAMES_RECHECK 272 7 26 6
FRAMES_RECHECK 278 8 19 6
FRAMES_RECHECK 285 4 5 4
FIVE_FORM_GRAPH_THEOREM_RECHECK_PASS 592 82 25 11 8
REPORT 1616 d21bf29911fc161ad993af4267e8b57dc3f8a9f9b85908283a0141c67360a988
NEW_281_MATRIX_PROOF_AND_25_FRAMES_REPLAY_PASS
ALL_NEW_CAP9_SOURCE_COEFFICIENT_REPORT_STREAM_FRAME_PINS_PASS
NOVA24_CAP9_NEW_281_RESTORED_COMPLETE_RECOVERY_PASS
REMAINING_TREE_ORDINALS 253 266 272 278 285
```

The separate frozen replay reproduced the independent matrix and graph checks and the final recovery marker, with exit 0. The full and frozen transcripts are pinned above.

Supplementary new complete proof and frozen checkpoint (`NOVA24_CAP9_NEW_281_RESTORED_V1.zip`): 1,200,135 bytes, SHA-256 `aae5596a83abc3a163473b5e2dbdf41f1638c67d2cb697c06601cbc71df77f0e`. This archive is optional; the complete reconstruction material follows.

## 7. Complete literal new source units

### 7.1 `engine.py`

```python
"""NEW cap9 barrier locator. Numerical output is not an exclusion certificate."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
from threadpoolctl import threadpool_limits
threadpool_limits(limits=1)
from itertools import product,combinations

def canonical(p):
 children=[[] for _ in p]
 for i in range(1,len(p)):children[p[i]].append(i)
 def code(i):return '('+''.join(sorted(code(j) for j in children[i]))+')'
 out=[];stack=[]
 for c in code(0):
  if c=='(':out.append(stack[-1] if stack else 0);stack.append(len(out)-1)
  else:stack.pop()
 return tuple(out)
def trees(n=9):return sorted({canonical((0,)+p) for p in product(*(range(i) for i in range(1,n)))})
def weights(a):
 out=[];ids=[i for i in range(9) if i!=a]
 for i,j in combinations(ids,2):
  for k in ids:
   if k in (i,j):continue
   w=[0]*9;w[a]=9;w[i]=w[j]=10;w[k]=7;out.append(w)
 assert len(out)==168
 return out
def locate(p,rows,verbose=False):
 m=168*len(rows);nf=9*len(rows)+(45 if len(rows)>1 else 0);d=nf+1
 I=np.eye(9);L=np.zeros((8,9,9))
 for u in range(1,9):L[u-1,u,u]=2;L[u-1,u,p[u]]=L[u-1,p[u],u]=-1
 J=np.zeros((m,d,9,9));off=[]
 if len(rows)>1:
  assert len(rows)==2
  for i in range(9):
   for j in range(i,9):
    b=np.zeros((9,9));b[i,j]+=1;b[j,i]+=1;off.append(b)
 for r,a in enumerate(rows):
  for t,ww in enumerate(weights(a)):
   t+=168*r;w=np.array(ww)/9
   for i in range(9):J[t,9*r+i]=np.outer(I[i],w)+np.outer(w,I[i])
   if len(rows)>1:J[t,18:63]=np.array(off)*(1 if r==0 else -1)
 J[:,-1]=-I
 y=np.zeros(d);y[-1]=-1;u=np.full((m,8),1/8.)
 def matrix(yy,uu):return np.einsum('mdij,d->mij',J,yy,optimize=True)+np.einsum('mk,kij->mij',uu,L,optimize=True)
 B=matrix(y,u)
 for outer in range(12):
  tau=.05*.18**outer;fac=tau/m
  for inner in range(70):
   chol=np.linalg.cholesky(B);R=np.linalg.inv(B)
   C=R[:,None]@J;D=R[:,None]@L
   gy=-np.trace(C,axis1=2,axis2=3).sum(axis=0);gy[-1]-=1/fac
   gu=-np.trace(D,axis1=2,axis2=3)-1/u
   Hyy=np.einsum('mdij,meji->de',C,C,optimize=True)
   Huy=np.einsum('mkij,mdji->mkd',D,C,optimize=True)
   Huu=np.einsum('mkij,mlji->mkl',D,D,optimize=True)
   Huu[:,np.arange(8),np.arange(8)]+=1/u**2
   rhs=np.concatenate((Huy,np.ones((m,8,1)),gu[:,:,None]),axis=2)
   sol=np.linalg.solve(Huu,rhs);T=sol[:,:,:d];e=sol[:,:,d];v=sol[:,:,d+1]
   S=np.zeros((d+1,d+1));b=np.zeros(d+1)
   S[:d,:d]=Hyy-np.einsum('mkd,mke->de',Huy,T,optimize=True)
   S[:d,d]=-np.einsum('mkd,mk->d',Huy,e,optimize=True);S[d,:d]=S[:d,d];S[d,d]=-e.sum()
   b[:d]=-gy+np.einsum('mkd,mk->d',Huy,v,optimize=True);b[d]=v.sum()
   S=(S+S.T)/2
   try:step=solve(S,b,assume_a='sym',check_finite=False)
   except Exception:step=np.linalg.lstsq(S,b,rcond=1e-14)[0]
   dy=step[:d];du=-v-np.einsum('mkd,d->mk',T,dy,optimize=True)-e*step[d]
   descent=fac*(gy@dy+(gu*du).sum());decrement=-descent
   if decrement < min(1e-7,tau*.001):break
   alpha=min(1.,.99*float(np.min(-u[du<0]/du[du<0]))) if np.any(du<0) else 1.
   old=-y[-1]-fac*(2*np.log(np.diagonal(chol,axis1=1,axis2=2)).sum()+np.log(u).sum())
   deltaB=matrix(dy,du)
   for back in range(60):
    yy=y+alpha*dy;uu=u+alpha*du;BB=B+alpha*deltaB
    try:
     ch=np.linalg.cholesky(BB)
     val=-yy[-1]-fac*(2*np.log(np.diagonal(ch,axis1=1,axis2=2)).sum()+np.log(uu).sum())
     if np.isfinite(val) and val<=old+.05*alpha*descent:break
    except np.linalg.LinAlgError:pass
    alpha*=.5
   else:return None
   y,u,B=yy,uu,BB
  if verbose:print('ITER',outer,inner,'margin',y[-1],'eq',u.sum()/m,'dec',decrement,flush=True)
  if y[-1]>1e-8:return y[:-1],u,y[-1]
 return None
if __name__=='__main__':
 import sys,time
 idx=int(sys.argv[1]);rows=[int(v) for v in sys.argv[2:]] or [0]
 t=time.time();z=locate(trees()[idx],rows,True)
 print('RESULT',idx,rows, None if z is None else z[2], 'time',time.time()-t)
 if z is not None:np.savez('test%d.npz'%idx,g=z[0],mu=z[1],margin=z[2])
```

### 7.2 `build.py`

```python
"""NEW deterministic producer: no unavailable cap9 file is an input.
CPython3.13.5, NumPy2.3.5, SciPy1.17.0, threadpoolctl3.6.0, one BLAS thread, no randomness.
python build.py produces cap9_new.json; python -S verify.py is independent.
"""
from pathlib import Path
import hashlib,json
import engine
import numpy as np
assert __debug__
ROWS01=[246,247,248,249,250,251,260,261,262,263,264,265,267,268,269,270,271,273,274,275,276,279,280,281]
ROWS02=[277,282,283,284]
REMAINING=[253,266,272,278,285]

def positive(a):
 # Fraction-free elimination, using a symmetric trailing update.
 a=[r[:] for r in a];old=1
 for k in range(9):
  pivot=a[k][k]
  if pivot<=0:return False
  for i in range(k+1,9):
   for j in range(i,9):
    z=a[i][j]*pivot-a[i][k]*a[k][j]
    assert z%old==0
    a[i][j]=a[j][i]=z//old
  old=pivot
 return True

def matrices(p,rows,g,u):
 off=[[0]*9 for _ in range(9)]
 if len(rows)==2:
  t=18
  for i in range(9):
   for j in range(i,9):off[i][j]+=g[t];off[j][i]+=g[t];t+=1
 for r,a in enumerate(rows):
  gamma=g[9*r:9*r+9]
  for t,w in enumerate(engine.weights(a)):
   b=[[gamma[i]*w[j]+w[i]*gamma[j]+(9*off[i][j]*(1 if r==0 else -1)) for j in range(9)] for i in range(9)]
   for i,mu in enumerate(u[168*r+t],1):
    b[i][i]+=18*mu;b[i][p[i]]-=9*mu;b[p[i]][i]-=9*mu
   yield b

if __name__=='__main__':
 records=[];tt=engine.trees();nm=0
 for ordinal,p in enumerate(tt):
  if ordinal in REMAINING:continue
  rows=[0,1] if ordinal in ROWS01 else [0,2] if ordinal in ROWS02 else [0]
  if ordinal==0:
   # Small exact continuation checkpoint; no numerical locator for this tree.
   gi=[900]+[9]*8
   ui=[[100*w[i]+9 for i in range(1,9)] for w in engine.weights(0)]
  else:
   result=engine.locate(p,rows)
   assert result is not None,('LOCATOR_UNKNOWN',ordinal,rows)
   g,u,margin=result;scale=max(np.max(np.abs(g)),np.max(np.abs(u)))
   gi=np.rint(g/scale*10**8).astype(np.int64).tolist()
   ui=np.rint(u/scale*10**8).astype(np.int64).tolist()
  assert all(v>=0 for r in ui for v in r)
  for b in matrices(p,rows,gi,ui):
   for i in range(9):b[i][i]-=1
   assert positive(b),('EXACT_REJECTION',ordinal)
   nm+=1
  record=dict(ordinal=ordinal,parent=p,rows=rows,g=gi,mu=ui)
  records.append(record)
  Path('partial').mkdir(exist_ok=True)
  Path('partial/%03d.json'%ordinal).write_text(json.dumps(record,sort_keys=True,separators=(',',':'))+'\n')
  if ordinal%25==0:print('NEW_CAP9_GENERATED',ordinal,len(ui),flush=True)
 assert len(records)==281 and nm==51912
 obj=dict(tag='NOVA24_CAP9_NEW_281_V1',specification_parent='minimum-0035',specification_sha256='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36',remaining=REMAINING,records=records)
 data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
 Path('cap9_new.json').write_bytes(data)
 print('NEW_CAP9_INTEGER_GENERATION_PASS',len(records),nm)
 print('DATA',len(data),hashlib.sha256(data).hexdigest())
```

### 7.3 `verify.py`

```python
"""Independent exact CAP9 verifier; CPython 3.13.5, standard library only.
Imports neither engine nor builder. No floating-point operations.
Run: python -S verify.py [cap9_new.json]
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,sys
assert __debug__
R01={246,247,248,249,250,251,260,261,262,263,264,265,267,268,269,270,271,273,274,275,276,279,280,281}
R02={277,282,283,284}
REST={253:(0,0,1,2,3,4,5,0,7),266:(0,0,1,2,3,4,5,4,0),272:(0,0,1,2,3,4,5,5,0),278:(0,0,1,2,3,4,5,6,0),285:(0,0,1,2,3,4,5,6,7)}
def serial(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
def parse(s):
 p=[];stack=[]
 for c in s:
  if c=='(':p.append(stack[-1] if stack else 0);stack.append(len(p)-1)
  else:assert stack;stack.pop()
 assert not stack
 return tuple(p)
def multisets():
 levels={1:['()']}
 for n in range(2,10):
  pool=sorted((s,k) for k in range(1,n) for s in levels[k]);out=[]
  def walk(left,start,parts):
   if left==0:out.append('('+''.join(parts)+')');return
   for i in range(start,len(pool)):
    s,k=pool[i]
    if k<=left:walk(left-k,i,parts+[s])
  walk(n-1,0,[]);assert len(out)==len(set(out));levels[n]=sorted(out)
 return levels
def array_code(p):
 def descend(i):return '('+''.join(sorted(descend(j) for j in range(i+1,len(p)) if p[j]==i))+')'
 return descend(0)
def weights(a):
 ids=[i for i in range(9) if i!=a];out=[]
 for t in product((0,7,10),repeat=8):
  if sum(t)!=27 or t.count(10)!=2 or t.count(7)!=1:continue
  w=[0]*9;w[a]=9
  for i,v in zip(ids,t):w[i]=v
  out.append(w)
 out.sort(key=lambda w:(tuple(i for i,v in enumerate(w) if v==10),w.index(7)))
 assert len(out)==168 and len(set(map(tuple,out)))==168
 return out
W=[weights(a) for a in range(9)]
def scalar_matrix(p,g,mu,w,offset,sign):
 # Expand 2(g.x)(w.x)+18 sum mu_i(x_i^2-x_i*x_parent)
 # +18 sign sum_{i<=j} offset_ij*x_i*x_j - sum x_i^2.
 coeff={}
 def add(i,j,v):
  key=(min(i,j),max(i,j));coeff[key]=coeff.get(key,0)+v
 for i in range(9):
  for j in range(9):add(i,j,2*g[i]*w[j])
 for i,v in enumerate(mu,1):add(i,i,18*v);add(i,p[i],-18*v)
 k=0
 for i in range(9):
  add(i,i,-1)
  for j in range(i,9):add(i,j,18*sign*offset[k]);k+=1
 out=[[0]*9 for _ in range(9)]
 for (i,j),v in coeff.items():
  if i==j:out[i][i]=v
  else:assert v%2==0;out[i][j]=out[j][i]=v//2
 return out

def bareiss(a):
 b=[r[:] for r in a];previous=1;minors=[]
 for k in range(9):
  pivot=b[k][k];assert pivot>0;minors.append(pivot)
  for i in range(k+1,9):
   for j in range(k+1,9):
    z=pivot*b[i][j]-b[i][k]*b[k][j]
    assert z%previous==0;b[i][j]=z//previous
  previous=pivot
 return minors

def fraction_ldl(a,minors):
 lower=[[F(int(i==j)) for j in range(9)] for i in range(9)];diag=[];prod=F(1)
 for k in range(9):
  pivot=F(a[k][k])-sum(lower[k][j]**2*diag[j] for j in range(k))
  assert pivot>0;diag.append(pivot);prod*=pivot;assert prod==minors[k]
  for i in range(k+1,9):
   lower[i][k]=(F(a[i][k])-sum(lower[i][j]*lower[k][j]*diag[j] for j in range(k)))/pivot
 return diag

if __name__=='__main__':
 levels=multisets();counts=[len(levels[n]) for n in range(1,10)]
 assert counts==[1,1,2,4,9,20,48,115,286]
 arrays={(0,)+p for p in product(*(range(i) for i in range(1,9)))}
 assert len(arrays)==40320
 codes={array_code(p) for p in arrays};assert codes==set(levels[9])
 tt=sorted(parse(s) for s in codes);assert {i:tt[i] for i in REST}==REST
 print('TWO_INDEPENDENT_TREE_ENUMERATIONS_PASS',counts,40320,flush=True)
 raw=Path(sys.argv[1] if len(sys.argv)>1 else 'cap9_new.json').read_bytes();data=json.loads(raw)
 assert raw==serial(data) and data['tag']=='NOVA24_CAP9_NEW_281_V1'
 assert data['specification_parent']=='minimum-0035'
 assert data['specification_sha256']=='8c1f1ed216fa9ce12e3141e4b177040958865e3dbbc42c88b8a7f4fcf68faf36'
 assert data['remaining']==sorted(REST)
 rec=data['records'];assert [r['ordinal'] for r in rec]==[i for i in range(286) if i not in REST]
 streams=[hashlib.sha256() for _ in range(3)];nm=0;nr=0;freeints=0;multints=0
 for r in rec:
  o=r['ordinal'];p=tt[o];assert r['parent']==list(p)
  rows=[0,1] if o in R01 else [0,2] if o in R02 else [0];assert r['rows']==rows
  g=r['g'];mus=r['mu'];assert len(g)==(63 if len(rows)==2 else 9) and len(mus)==168*len(rows)
  assert all(type(v) is int for v in g)
  assert all(len(u)==8 and all(type(v) is int and v>=0 for v in u) for u in mus)
  freeints+=len(g);multints+=sum(map(len,mus));offset=g[18:] if len(rows)==2 else [0]*45
  for ri,a in enumerate(rows):
   for wi,w in enumerate(W[a]):
    mat=scalar_matrix(p,g[9*ri:9*ri+9],mus[168*ri+wi],w,offset,1 if ri==0 else -1)
    minors=bareiss(mat);fraction_ldl(mat,minors)
    for h,obj in zip(streams,([o,a,wi,w],[o,a,wi,mat],[o,a,wi,minors])):h.update(serial(obj))
    nm+=1
  nr+=len(rows)
  if o%25==0:print('EXACT_CAP9_TREE_PASS',o,len(mus),flush=True)
 assert nm==51912 and nr==309 and freeints==4041 and multints==415296
 report=dict(tag='NOVA24_CAP9_NEW_EXACT_VERIFICATION_V1',trees=286,excluded=281,remaining=sorted(REST),remaining_parents=[REST[i] for i in sorted(REST)],row_count=nr,extremes_per_row=168,matrices=nm,leading_minors=9*nm,free_integers=freeints,multiplier_integers=multints,coefficient_bytes=len(raw),coefficient_sha256=hashlib.sha256(raw).hexdigest(),tree_sha256=hashlib.sha256(serial(tt)).hexdigest(),streams=dict(zip(('weights','shifted_matrices','leading_minors'),(h.hexdigest() for h in streams))))
 b=serial(report);Path('cap9_checked.json').write_bytes(b)
 print('ALL_CAP_EXTREME_ROWS_EXACTLY_COVERED_PASS',nr,nm)
 print('INDEPENDENT_SCALAR_BAREISS_FRACTION_LDL_PASS',nm,9*nm)
 print('NEW_281_OF_286_UNIVERSAL_CAP9_THEOREM_PASS',sorted(REST))
 print('REPORT',len(b),hashlib.sha256(b).hexdigest())
 print('NO_F10_V10_C34_OR_WHOLE_C32_TYPE_ASSERTION')
```

### 7.4 `frames.py`

```python
"""Frame consequence, using the newly verified 281-tree complement.
Adapted from the literal parent recheck_frames.py, not old dual_frames.py.
CPython3.13.5, standard library only. Run: python -S frames.py.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
assert __debug__
certificate=json.loads(Path('cap9_checked.json').read_text())
assert certificate['tag']=='NOVA24_CAP9_NEW_EXACT_VERIFICATION_V1'
assert certificate['excluded']==281 and certificate['matrices']==51912
assert certificate['remaining']==[253,266,272,278,285]
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
print('FIVE_FORM_GRAPH_THEOREM_RECHECK_PASS',592,82,25,11,8)
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('NEW_281_MATRIX_PROOF_AND_25_FRAMES_REPLAY_PASS')
```

### 7.5 `replay.py`

```python
"""NEW complete source-only CAP9 recovery; never decodes the malformed parent.
CPython3.13.5; all/check/seed modes. Save all five source units together.
Full: python -S replay.py. Frozen: python -S replay.py check.
Tiny exact checkpoint only: python -S replay.py seed.
Numerical: numpy2.3.5,scipy1.17.0,threadpoolctl3.6.0,OpenBLAS0.3.30/Haswell.
"""
from pathlib import Path
import hashlib,json,os,subprocess,sys
assert __debug__
S={'engine.py': [3924, '382527ea22bb7a02d448ac2eb1f9c1b5785f15384df6c9248f1639714b87ab00'], 'build.py': [2924, '7ee0832cf805272cc47e587dff7a8710250eef481b7a5ca55af9e36633dcec78'], 'verify.py': [5792, 'c572e6bb3ff4ef19db498b436972f4304229ab3f26562a74a179765519bea8f9'], 'frames.py': [4681, 'c4389bb0b7e05e0c0294f1214fe29eb8b913c6fadd94d902681c9c52795e4158']}
O={'cap9_new.json': [3829595, 'b0cfc1a3d46eec19e3e5d0f1603de276edb45da7cc06b069e7299b4c1ae7654c'], 'cap9_checked.json': [817, '3e23d591677593fa852949daf2642c45f556b73d1da0b755d42818f1572167ac'], 'frames_new.json': [1616, 'd21bf29911fc161ad993af4267e8b57dc3f8a9f9b85908283a0141c67360a988'], 'build.log': [440, '57a4d7214ccc6c95a481cb295f0a67e53e629c0a061ffb53484ce3282719d3bb'], 'verify.log': [720, '1c2f9948ca653242b9080d82af7bb218e598cc1ba9ec070b156f62d17b9f85fd'], 'frames.log': [305, 'abf49bcced761cc9f3055a0ece58a2342b34b93498a89a9654ac343bd97f0999'], 'seed0.json': [4455, '2e45acd9ffdd7a7eab8251713114d36599b83d03259d1b146080a73ebe231455']}
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
for n,want in S.items():assert pin(Path(n).read_bytes())==want,('SOURCE_PIN',n)
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
assert mode in ('all','check','seed')
# This exact record belongs to the full checkpoint, not an unrelated smoke test.
import verify as v
W=v.weights(0);g=[900]+[9]*8;mu=[[100*w[i]+9 for i in range(1,9)] for w in W]
r=dict(ordinal=0,parent=[0]*9,rows=[0],g=g,mu=mu)
for w,u in zip(W,mu):
 a=v.scalar_matrix([0]*9,g,u,w,[0]*45,1);v.fraction_ldl(a,v.bareiss(a))
b=v.serial(r);assert pin(b)==O['seed0.json'];Path('seed0.json').write_bytes(b)
print('EXACT_LITERAL_STAR_CHECKPOINT_PASS',0,168,flush=True)
if mode=='seed':
 print('SEED',*pin(b));print('SEED_ONLY_NOT_281_TREE_REPLAY');raise SystemExit(0)
def run(args,log):
 env=os.environ.copy()
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[k]='1'
 env['PYTHONHASHSEED']='0'
 p=subprocess.run([sys.executable]+args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
 Path(log).write_bytes(p.stdout);sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
 assert p.returncode==0,('CHILD_EXIT',args,p.returncode)
if mode=='all':run(['build.py'],'build.log')
assert pin(Path('cap9_new.json').read_bytes())==O['cap9_new.json']
run(['-S','verify.py'],'verify.log');run(['-S','frames.py'],'frames.log')
for n,want in O.items():
 if n=='build.log' and mode=='check':continue
 assert pin(Path(n).read_bytes())==want,('OUTPUT_PIN',n)
print('ALL_NEW_CAP9_SOURCE_COEFFICIENT_REPORT_STREAM_FRAME_PINS_PASS')
print('NOVA24_CAP9_NEW_281_RESTORED_COMPLETE_RECOVERY_PASS')
print('REMAINING_TREE_ORDINALS 253 266 272 278 285')
```

## 8. Exact remaining domain and most useful continuation

The durable successor is the **new 281-tree certificate checkpoint**, its independent exact checker, and the restored 25-frame theorem. It does not rehabilitate the malformed old source or retroactively turn old recorded output into current execution.

The unexcluded physical domain consists of genuine bodies whose actual pole escape tree has one of the five literal arrays, whose full nonnegative pole-shadow graph fits one of the 25 literal maximal frames, and which satisfy all true incidences, actual ordinary-volume centring, actual facet-volume/area-centroid identities, the same full Lambda including its matrix-square identity, and one reciprocal physical metric. A frame or independent capped-row solution is not a physical witness. In the joint setting, both available actual complementary choices must remain eligible.

The next useful step is no longer another generic 286-tree search. Transport the proved five-form/frame restrictions through the lead's surviving true-incidence placements, identify actual triangular facet chains and their common volume upper bounds, and impose those constraints together with the same Lambda's matrix-square/Schur identities. The explicit two-row PSD coupling above provides one concrete certificate extension; it still needs a successful exact certificate and exhaustive coverage before any additional tree form, labelled incidence class, root, or whole C32 type is declared closed.

**Final boundary:** 281 of 286 tree shapes excluded with fully recoverable new integer certificates; exactly five shapes remain unexcluded; 25 maximal frames and their 11-pair/eight-tree bounds freshly verified; no new physically coupled survivor exclusion, whole-type exclusion, or global lower-bound increase.
