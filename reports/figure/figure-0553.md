# figure-0553

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Exact nearest reference110 distances and an all-root retained-material mass obstruction

## Outcome

**No own110 was obtained. The fixed-geometry proximity question is now resolved sharply for both literal bodies.** I found simpler, substantially closer reference110 points, certified nonzero neighborhoods around them, and proved their limiting Euclidean distance from the actual homogeneous centroid **over all stable and unstable carrier choices**. I also proved an all-root obstruction to realizing any fixed-body reference110 centre by inner convex mass removal while retaining its corresponding old unstable vertex.

Four new rational, uniformly filled projective/grid controls were reconstructed and fully audited. They are non-targets and remain recoverable, including the simpler grids and their actual incidence changes.

All four current attachments were read completely. The required literal h90 parent and its previously unread tail in the prior journal were also read through EOF; the 35-unit parent recovery matched its declared 203263-byte dictionary hash `729ec23615fe3b87fc09dd359ef85b67e862abc66a431c83f9f76b79c1c86dd5`. There is no necessary source gap for this result. The current journal's 306703 bytes match `d255e5066fea8aafe868300ce038eefde4becdf4f22ac3ba2ef3e681bba8aa47`.

The authority is **figure-0549**, SHA256 `f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605`. Throughout, primary means its `R62J_JOINT75_G7_TRUE75`, and bridge means its `REFERENCE_BRIDGE79_G8`, with the literal material-row numbering. The earlier simple reference points and their limited discovery scope are exactly those in the supplied reference-chambers source.

## 1. Sharp global reference-distance result

For either unchanged body K, let g be its actual uniform-volume centroid, and define

`R(K)={q in int(K): strict reference(S,U,H)=110 and additionalweak=000}`.

I proved

`inf_{q in R(K)} ||q-g||_2 = sqrt(Delta_K)`.

Every admissible point has distance **strictly greater** than this infimum. The boundary points below are limits, not accepted weak-free witnesses.

| Literal body | Actual V/E/F; C | Exact infimum distance, enclosed between consecutive multiples of 10^-12 | Infimum / own circumradius |
|---|---|---|---|
| Primary | 75/219/146; 438 | (0.687937922325, 0.687937922326) | (0.489141872471, 0.489141872472) |
| Bridge | 79/231/154; 462 | (0.593436002578, 0.593436002579) | (0.448612137372, 0.448612137373) |

Distances use the fixed literal input coordinates. The last column supplies a scale-invariant comparison. The original own bodies remain respectively **222** and **15/32/45**; moving a reference point has not changed their density or centroid.

### Exact limit-point definitions

For an outward triangle f=(i,j,k), put `n_f=(X_j-X_i) cross (X_k-X_i)`. Define the affine facet-side and vertex-cone forms

`S_{f,l}(q) = [n_f cross (X_{f[l+1]}-X_{f[l]})] dot (q-X_{f[l]})`,

`U_{i,j}(q) = (X_j-X_i) dot (q-X_i)`.

Indices within a triangle are cyclic and zero-based.

The primary limit is the orthogonal projection of its exact own centroid onto the intersection of

`S_[4,59,6],1(q)=0` and `S_[6,72,71],1(q)=0`.

It is approximately

`q*_primary=(0.47699783182073524, 0.03915973584478336, -0.26139877183632276)`.

The bridge limit is the unique intersection of

`U_0,4(q)=0`, `S_[44,54,76],1(q)=0`, and `S_[65,67,69],0(q)=0`.

It is approximately

`q*_bridge=(0.3774695095982171,-0.12368127278345029,-0.3020328185525119)`.

These are **exact rational definitions**, not rounded input coordinates. `canonical_targets.py` reconstructs them from the complete literal material input, solves the rational Gram system, checks positive projection multipliers, and stores every coordinate and `Delta_K=||q*-g||^2` as a fraction.

The full boundary census is important:

| Limit | Strict reference S/U/H | Additional weak S/U/H | Full closed-weak S/U/H | Positive P/Q |
|---|---|---|---|---|
| Primary q* | 1/1/0 | 2/0/2 | 3/1/2 | 0/0 |
| Bridge q* | 1/1/0 | 2/1/3 | 3/2/3 | 0/0 |

Thus even **P0/Q0 plus strict110 is insufficient** here: both exact limiting objects have forbidden weak equilibria.

### Why the lower bound covers the union of chambers

The proof does not use a fixed witness-tree LP or an optimizer's bound. It starts with K intersected with a cube about g that contains the entire proposed Euclidean ball. Every actual vertex U-cone and every maximal facet S-prism is permitted. Each is an intersection of exact affine halfspaces in `q-g`.

A proof node has one of three forms. A covering leaf exhibits two distinct closed S regions or two distinct closed U regions containing the entire cell. A split selects two regions of the same kind and covers the complement of their intersection by all their closed outside halfspaces. A distance leaf supplies an integer vector n with

`m=min_{cell vertices v} n dot v > 0`,

`m^2 >= Delta_K (n dot n)`.

The last two exact inequalities put the whole cell outside the open Euclidean ball by Cauchy–Schwarz. The accepted generator obtains its distance certificates by integer/rational nearest-point calculations on actual polygonal faces, edges and vertices; **it uses no floating distance hint**.

All branches were exhausted and every recorded split and leaf was replayed separately. Lower-dimensional children cannot conceal an admissible strict/no-extra-weak centre: that mechanical condition has an open neighborhood. The same observation excludes an admissible point on the limiting sphere, since its neighborhood would meet the already excluded open ball. This argument does not assume that every inactive primitive is nonzero.

| Exact distance proof | Total nodes | Two-critical-region leaves | Distance leaves | Flat children discarded | Pending |
|---|---:|---:|---:|---:|---:|
| Primary | 15425 | 4678 | 3964 | 56719 | 0 |
| Bridge | 61385 | 16257 | 20146 | 170449 | 0 |

Both maximum depths are16. The independent replay checks the complete tree, not the search heuristic. The homogeneous clipping/nearest-point implementation was additionally cross-checked against the supplied Fraction clipping and a separate Fraction nearest-point implementation on101 exact clipped cells.

### Why the bound is attained as an infimum

Let a be the corresponding simple near reference in the next section. Every complete mechanical guard is strictly positive at a and nonnegative at q*. This includes an explicit negative witness for **every true edge's closed saddle conditions**, not just S/U counts or Euler.

Consequently the entire rational family

`q(t)=(1-t)q*+t a, 0<t<=1`,

is reference110 with no additional weak equilibria. If the certified cube radius at a is r, the closed cube of radius `t r` about q(t) is also valid. This proves approach to the lower bound through robust reference chambers. It is a certified reference-space path for unchanged K, **not a physical own-centroid deformation path**.

## 2. Useful rational chambers and robustness controls

All terminating decimal coordinates in the following table are exact rationals. Every listed **closed** axis-aligned cube has strict reference110 and no additional weak equilibria throughout it. Every central point additionally has primitivezero000 and exact P0/Q0.

| Body / use | Exact reference point | Certified cube halfwidth | Distance to actual own centroid |
|---|---|---:|---:|
| Primary, simple near | (0.48,0.03,-0.27) | 3/4000 | 0.6899583152874338 |
| Primary, near-limit grid | (0.4770008,0.0391506,-0.2614074) | 1/2000000 | 0.6879398030263126 |
| Bridge, simple near | (0.38,-0.12,-0.31) | 3/2000 | 0.5994361880918826 |
| Bridge, near-limit grid | (0.3774720,-0.1236776,-0.3020408) | 1/1000000 | 0.5934419291235007 |

The primary chamber's stable triangle is **[51,66,65]**; the bridge chamber's is **[65,66,67]**. Their unique U is input6, and both stable triangles avoid it. The global distance proof nevertheless allowed all roots and all stable carriers.

Compared with the source's simple points, whose distances are respectively0.8322080095870213 and0.7070926477791387, the new simple references are **17.0930%** and **15.2252% closer**. The simple primary reference is only0.2937% above the global infimum; the simple bridge reference is1.0111% above it. The near-limit grids are obtained deterministically by rounding the proved `t=1/1000` approach point to denominator10^7 and retaining a smaller certified cube—not by a new tolerance-based acceptance test.

Two wider non-record controls are retained: primary `(0.49,0.03,-0.27)` and bridge `(0.5,-0.05,-0.36)`, each with cube halfwidth3/800. Their distances are0.6994816571969599 and0.7444839802406801. The latter is intentionally preserved for width despite being farther away than the source's simple bridge point. No globally optimal robustness radius is claimed; these are exact sufficient neighborhoods.

Coarse arithmetic near the boundary can change the class. The bridge point `(0.38,-0.12,-0.30)` is exactly reference121 with a positive P bar of depth approximately`3.036817581148099e-7`, singleton component and7-edge cut. The point `(0.378,-0.124,-0.302)` is exactly reference222, with P depth`3.6956778121478355e-8` and Q depth`5.790922063829354e-6`. Its P component/cut sizes are1/7 and Q sizes1/3. Both have additionalweak000. These bars are retained in full; none is removed as numerical noise.

## 3. A nonlocal physical mass obstruction, with all old roots considered

For any full-dimensional convex body W retaining a point u, coning from u gives

`centroid(W) in (u+3W)/4`.

Indeed, each integration tetrahedron has centroid `(u+a+b+c)/4`; averaging by its positive volume gives the inclusion. This concerns actual uniform volume, not vertex averaging or ballast.

For each actual vertex u of K, I exactly intersected `(u+3K)/4` with the closed reference-U cone of u, then ran the full S/U quota cover with **no nominated stable carrier**. Every root was covered:

| Body | Roots considered | Total exact nodes | Covering leaves | Pending / unresolved |
|---|---:|---:|---:|---:|
| Primary | all75 | 4734 | 2822 | 0 |
| Bridge | all79 | 7338 | 4676 | 0 |

All154 root-domain proofs were independently replayed. In particular:

**If q is any strict/no-extra-weak reference110 centre of fixed K, and u is its unique K-unstable vertex, no positive-volume convex W subset K retaining u can have actual centroid q.**

This is not restricted to input6, either old stable face, a single reference ray, a fixed escape tree, or an edge budget. It is a genuine whole-inner-material obstruction under the stated retained-point condition.

It is **not** an exclusion of own110 in an arbitrary changed inner body. Such a body's critical regions change; its own centroid need not be a reference110 point of K. Nor does the theorem exclude removal of u, moving it, outward additions, or a changed metric.

### Quantitative freedom required at the new robust references

There is a simple additional support certificate. Both literal bodies have actual facet[51,66,65] with

```text
n=(10359771888090000000,7126676443360000000,-2653593450520000000),
h=6746716165054310991,
u=X6=(-8712882,-8006246,8846843)/10000000.
```

Suppose W retains this literal u and its own centroid lies in the closed cube of halfwidth r about the relevant simple near reference a. The coning inequality forces

`h_W(n)-h_K(n) >= N/3`,

`N=4 n dot a - n dot u -3h -4r ||n||_1`.

Here N is exactly`20391007446225688057` for primary and`12335247651710978057` for bridge. Therefore

`d_H,2(W,K) >= N/(3||n||_2)`,

approximately **0.5288960429169935** and **0.3199480794951432**, respectively. These are necessary finite raw Hausdorff changes even when other material is free and W is not required to be a subbody. The source also computes exact infinity-norm lower bounds, respectively

```text
34593671462430628271/101919297072630000000,
1282446543779951989/6026336200132500000.
```

The limits apply to the entire certified reference cubes, not only their central points. Retaining input6 while attempting a tiny mass correction is therefore not the relevant remaining freedom. Moving/removing that material point or making a substantial support change escapes this stated obstruction; success after doing so is not implied.

## 4. Four finite actual-mass projective controls

I tested the direct centering response at the two new simple references. Float64 damped Newton used the actual image volume and covariance, with a positive-chart guard, at most80 steps,80 backtracks, Armijo parameter10^-4 and residual stopping test2e-14. This numerical stage supplied only parameters.

For exact recovery, take `L=K-a` and freeze

```text
b_primary=(-451528211,-247529526,114986391)/100000000,
b_bridge =(-151841890,-53012791,42250566)/100000000.
```

All exact vertex denominators `1+b dot x` are positive, so they are positive on the whole original body. Form `Y=T_b(L)`, then **separately** round each image coordinate to the nearest ties-even multiple of10^-6 or10^-8. Rebuild the actual convex hull and integrate its own centroid. The grid operation is a material change, not an assertion that rationalization preserved all faces.

| Exact finite body | V/E/F; C | Strict = full closed-weak own S/U/H | Positive P/Q | Largest P / Q depths |
|---|---|---|---|---|
| NEAR_PRIMARY_PROJECTIVE_GRID6 | 75/219/146;438 | 3/9/10 | 8/2 | 0.6093655845798481 / 0.7137628645002091 |
| NEAR_PRIMARY_PROJECTIVE_GRID8 | 75/219/146;438 | 3/9/10 | 8/2 | 0.6093656193822020 / 0.7137633907964165 |
| NEAR_BRIDGE_PROJECTIVE_GRID6 | 79/231/154;462 | 13/15/26 | 14/12 | 0.4131423908128365 / 0.3806154107373277 |
| NEAR_BRIDGE_PROJECTIVE_GRID8 | 79/231/154;462 | 13/15/26 | 14/12 | 0.4131418972835166 / 0.3806159533851081 |

All four have exact positive volume, additionalweak000 and primitivezero000. Their volumes are approximately0.09004489037211087,0.09004484576133771,0.47273719843082074 and0.47273710855671436 in table order. Their exact centroids are **not zero**. For example, the two GRID8 centroids are approximately

```text
primary: (-1.1582407800857397e-10,-7.15575720264186e-10,-1.8943685126099336e-9),
bridge:  (3.261761923571683e-10,-1.5975425132040852e-9,-1.2361566886755542e-10).
```

Every reported equilibrium and every bar uses those bodies' separately integrated exact own centroids, not the nominee or zero.

Primary GRID6 replaces8 old true edges by8 new ones; GRID8 replaces3 by3. Their stable carriers also differ: GRID6 has[6,13,54], while GRID8 has[0,59,4], alongside their other two stable faces. Both bridge grids preserve the original maximal face sets and true edges. All replacements and complete current complexes are stored. These arithmetic/non-record controls are not silently collapsed into one projective image.

The unchanged literal parent's `exact_poly.py` independently reconstructed all four grids and agreed on the maximal complexes, physical volume and first moment, centroid, S/U/H carriers, strict/closed-weak census, and every physical P/Q birth and death. Its documented homogeneous bar scaling was explicitly undone before comparison. All72 positive bars across the four controls carry complete components, cuts, attaining edges and paths in the main audits.

These are four exact failed finite controls, **not an interval exclusion of the exactly centred algebraic map, a whole projective orbit, or inverse-coupled affine metrics**. No algebraic-centering certificate is claimed for these new nominees. The existing source's different nominated bridge centering failure has its own interval proof and is not being relabelled as this computation.

## 5. Discovery, verification and recovery

Numerical disjunctive search treated all S/U carrier choices, followed by a rationally checked projection and a witness-cell margin search. Those finite MILP/optimization runs are discovery only. Their complete code, actual frozen pins, grid choices, non-default parameters and commands are retained in `STUDY_PINS.json`. Time-limited optimizer outcomes are not used as exclusion certificates.

Observed numerical environment: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0**, float64, OPENBLAS/OMP threads1, no RNG. Every accepted reference, physical grid, distance proof and retained-root proof reconstructs using **only CPython and the standard library**.

The inline recovery capsule contains30 complete source/input/manifest units, including the full literal75+6 input, both exact audit modules, all new exact and numerical producing methods, the actual numerical pins and the27 expected exact-output receipts. No originating sandbox, prior journal or external archive is needed to reconstruct the accepted findings.

Save the complete source below as `RECOVER_NEAR110.py`, then run:

```sh
python -B -S RECOVER_NEAR110.py NEAR110_SOURCE
cd NEAR110_SOURCE
python -B -S REPLAY_NEAR110.py
```

For separated distance reconstruction:

```sh
python -B -S canonical_targets.py both
python -B -S ball_exact.py primary 7/10 --projection canonical_primary.json --limit 1000000
python -B -S ball_exact.py bridge 3/5 --projection canonical_bridge.json --limit 1000000
```

**The fractions7/10 and3/5 are enclosing cube halfwidths, not the asserted Euclidean radii.** The exact squared radii come from the regenerated canonical files. The proof JSON fields distinguish these explicitly.

The complete actual complexes, volumes, first moments, centroids, full strict/closed-weak mechanics, every positive P/Q bar, current carriers and root stars regenerate in `full_references_*.json`, `CUBE_*.json` and the four `NEAR_*_AUDIT.json` outputs. All27 byte counts and hashes are embedded in `EXPECTED_OUTPUTS.json`; none is a substitute for recovery code.

Selected observed receipts:

```text
RECOVER_NEAR110.py
46469 bytes
5fe75cafabd5c4ecef1a5045763110ecd8a5d19889edfbf27d6f32d6b8f04315

Decoded source dictionary:30 units,126675 bytes
0298cc13b925fa5bb1f94934fb05ee9607cc5ceeec857a86a5d7a2b76f295bae

ball_exact_primary_7_10.json:386960 bytes
d07b0584ab4afc49dc427f66225584549c540f0c5dd743f4948479b8f90f5534
ball_exact_bridge_3_5.json:1614347 bytes
a2d2ad0ecca43b68e0ea55c6669f042003cc2c3a44d8779f14548e48782a3cca

retained_primary_all.json:72669 bytes
099f73c08d8f8a2e1aa7dc9754e4eed2b6ad015f3ef378585800af0ce7eac07d
retained_bridge_all.json:110649 bytes
00c27a235f53b2d39b087e7e60a3e516ac1e59019aa3b4e21d0d8da761ccaed8
```

Observed completion conditions include:

```text
NEAR110_SOURCE_RECOVERY_PASS 30 126675 0298cc13b925fa5bb1f94934fb05ee9607cc5ceeec857a86a5d7a2b76f295bae
EXACT_ROOT_FREE_BALL_PROOF_REPLAY_PASS 15425 4678 3964
EXACT_ROOT_FREE_BALL_PROOF_REPLAY_PASS 61385 16257 20146
EXACT_ALL_RETAINED_ROOTS_CENTROID_EXCLUSION_PASS primary 75 4734 2822
EXACT_ALL_RETAINED_ROOTS_CENTROID_EXCLUSION_PASS bridge 79 7338 4676
ALL_FOUR_PARENT_AUDITOR_CROSSCHECKS_PASS 579 39b71c705db309229079f1276eca4813e27a01d1d20180254369851b2c97aea9
```

A fresh directory decoded the inline capsule and completed the entire standard-library replay, regenerating all27 expected outputs byte-for-byte. The observed aggregate marker was:

```text
NEAR110_COMPLETE_EXACT_REPLAY_PASS 27 GLOBAL_DISTANCE_2 ALL_ROOT_CENTROID_154 OWN_CONTROLS_4 NO_OWN110
```

The optional numerical discovery was not rerun during this cold check; it is unnecessary for exact reconstruction.

The standalone decoder (`RECOVER_NEAR110.py`) and complete source/proof/audit bundle (`NEAR110_HANDOFF.zip`) are convenience copies. The full inline source below remains the recovery authority for this handoff.

## 6. Scientific continuation

The remaining fixed-body chamber-distance gap is not a search failure: its exact infimum is established, and it is about0.49 and0.45 of the respective own circumradii. Further reference-only optimization cannot turn either literal body into a near-centroid110 entrance.

A useful next physical continuation is therefore **root/material replacement or substantial outer support reconstruction**, using one of the certified cubes as a guard region while recomputing the changed body's actual centroid and critical regions. The all-root inner-retention theorem identifies precisely what a construction must stop preserving; it does not close the changed-geometry problem. The new projective/grid controls show that closeness of the nominated reference alone does not preserve the P and Q landscapes during mass repair. No own110/no-extra-weak/C<500 successor is claimed.

## Complete runnable recovery capsule

```python
"""Self-contained exact nearest-reference / material-centroid study recovery.
Python standard library only; does not launch numerical optimization.
"""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA=r"""
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
AgAAAAAEWVo=
"""
RAW_BYTES=126675
RAW_SHA256='0298cc13b925fa5bb1f94934fb05ee9607cc5ceeec857a86a5d7a2b76f295bae'
def main():
 raw=lzma.decompress(base64.b64decode(''.join(DATA.split()),validate=True))
 assert len(raw)==RAW_BYTES and hashlib.sha256(raw).hexdigest()==RAW_SHA256
 files=json.loads(raw);manifest=json.loads(files['SOURCE_PACK_MANIFEST.json'])
 root=Path(sys.argv[1] if len(sys.argv)>1 else 'NEAR110_SOURCE');root.mkdir(parents=True,exist_ok=True)
 for name,text in sorted(files.items()):
  assert Path(name).name==name and name not in ('.','..')
  b=text.encode('utf-8')
  if name in manifest:
   r=manifest[name];assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
  (root/name).write_bytes(b)
 print('NEAR110_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
