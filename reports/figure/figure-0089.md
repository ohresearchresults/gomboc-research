# figure-0089

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Determination

**No finite homogeneous polyhedral Gömböc was obtained.** The acceptance target remains a uniform-density finite body evaluated at its own exact volume centroid with strict `(S,U,H)=(1,1,0)`, complete H/V and face-lattice data, exhaustive face/vertex/true-edge audits, independent verification, and matching meshes; auxiliary-centre, wall, near-solution, or unexpanded objects do not count.

The branch does, however, materially advance the exact Santaló frontier recorded in the supplied journal. The predecessor had already produced a gate-valid hard-centred double-Y endpoint of class `(2,1,1)` and identified a non-stellar connected two-cell/five-row crossing as the next operation. I constructed such a crossing exactly and continued through old-row deactivation, but the complete residual stable–saddle pair **transfers again rather than cancels**.

The strongest returned object is therefore a **fallback**, not a winner:

```text
Q_post: (V,E,F) = (20,54,36)
P_post = Q_post^∘: (V,E,F) = (36,54,20)
complexity C = 108
exact own-centroid class on P_post = (2,1,1)
```

It is fully finite, exact-dyadic at input, exactly hard-centred, irredundant, independently rebuilt, and safely above the `10^-5` inactive-separation gate on both sides.

## 1. Exact connected five-row/two-cell event

The materialized event uses original Q-row labels

```text
(4,18,25,15,24)
```

in that cyclic order. The five rows are projected exactly onto one common supporting plane. At the wall:

- every selected plane residual is exactly zero;
- every other Q row lies strictly behind the plane;
- the minimum other-row support gap is `0.01900546298666171`;
- the boundary orientation has one strict sign around the full pentagon;
- the augmented affine matrix has rank `3` and nullity `2`.

Thus this is a **codimension-two supporting pentagon containing two simultaneous four-row circuits**. It is a genuinely coupled five-row event, but not a single minimal affine circuit; the exact affine-nullspace basis is stored in the circuit certificate.

The strict pre-wall side is

```text
triangles       (4,18,24), (18,25,24), (25,15,24)
internal edges  (18,24), (24,25)
height pattern  (-1,-1,-1,-1,+4)/5120
```

and the strict post-wall side is

```text
triangles       (4,18,25), (4,25,15), (4,15,24)
internal edges  (4,25), (4,15)
height pattern  (+4,-1,-1,-1,-1)/5120.
```

Hence one topological event simultaneously deletes Q edges

```text
(18,24), (24,25)
```

and inserts

```text
(4,25), (4,15).
```

All three supporting triangles on each side have exact positive support gaps; all five signed four-point determinants on both sides are included in the exact coupled-five-row map (`coupled_five_row_circuit_map.json`). The standalone builder is build_coupled_five_row_map.py.

### Scope limitation

Before this exact wall was reached, the predecessor’s originally labelled outgoing saddle routes `(23,25)` and `(23,27)` had already relayed into the adjacent row-24 basin. Consequently, this is an exact non-stellar two-cell replacement, but **not a direct simultaneous cancellation of those original labelled routes**.

On the post-wall side, stable row `25` and the saddle route on Q edge `(4,24)` remain. Exact deactivation of old row `4` then transfers them to original stable row `18` and original Q edge `(18,24)`. The final active original rows are

```text
0,1,2,3,5,6,7,10,11,12,13,14,15,16,17,18,23,24,25,26
```

and the deleted or inactive original rows are

```text
4,8,9,19,20,21,22,27.
```

## 2. Exact hard centring and isolated Santaló root

The final generator starts from 20 hexadecimal binary64 triples interpreted as **exact dyadic rationals**. Let the pre-gauge polar centroid be `c`. The exact projective control is

```text
T_u(q) = q/(1-q·u),
(T_u Q)^∘ = Q^∘ - u.
```

Therefore the three first-moment equations are not penalized or numerically projected:

```text
F(u) = centroid((T_u Q)^∘) = c-u,
DF = -I_3,
u = c.
```

For the returned endpoint:

```text
c ≈ (0.012844395846209508,
     0.00020586939425850647,
     0.00016242406668913204)
projective denominator interval ≈ [0.9408554679159457,
                                    1.0527897678270568]
post-gauge first moment = (0,0,0) exactly
post-gauge centroid     = (0,0,0) exactly
Santaló/control root    = (0,0,0) exactly
control Jacobian        = -I_3 exactly.
```

The root enclosure is

```text
[-2^-80,2^-80]^3.
```

Because the moment map in the control coordinates is exactly `-u`, zero is the unique root throughout the admissible projective domain, not merely a small-residual point.

### Strict interior and bounded polarity over the whole root box

Compressed Q rows `(0,1,12,14)`, corresponding to original labels `(0,1,15,17)`, contain the origin with positive barycentric weights approximately

```text
(0.14893568943750804,
 0.23216151121364606,
 0.3775454253249582,
 0.24135737402388768).
```

The exact weighted sum is zero. The minimum origin-to-Q-face distance is approximately `0.5414358396130395`, so the origin is strictly interior and the polar is globally bounded.

Over the full root box:

```text
max P-support displacement upper bound = 1.848039258549812e-24 < 1
max Q-control dot-product upper bound   = 3.201412630319599e-22 < 1.
```

Thus both polar boundedness and every projective denominator remain strict throughout the enclosure. The complete rational inequalities are in the root-box certificate (`root_box_boundedness_certificate.json`).

## 3. Strongest exact post-circuit endpoint

The full exact object is post_five_circuit_gate_exact.json, SHA-256

```text
5052877ceab54b250090af0dc9e96d4f10b703c1f902dcac11fedacacb932977
```

Its exact polar volume is stored as a rational number; numerically

```text
Vol(P_post) ≈ 0.020215911358377397.
```

Every one of the 20 Q rows is extreme, every one of the 36 P vertices is actual, and the rebuilt Euler checks are exact.

### Complete equilibrium set at P’s own uniform centroid

#### Stable maximal faces

| Compressed row | Original row | P maximal-face cycle | Normalized margin | Limiting original row |
|---:|---:|---|---:|---:|
| `14` | `17` | `(2,5,6,20,34,18,16,12,14,28,30,33,27,25,23,21,9,3)` | `0.9431636389821872` | `23` |
| `15` | `18` | `(1,4,11,35,8)` | `0.004268900119881707` | `25` |

Original row `17` is the retained robust target. Original row `18` is the transferred unwanted stable feature.

#### Unstable vertices

There is exactly one:

```text
P vertex                       6
compressed Q incidence         (1,7,14)
original Q incidence           (1,10,17)
normalized directional margin  0.6752549327549126
full normal-cone coefficients ≈
  (0.9180127843262514,
   1.2070781835592304,
   1.286099741307843).
```

All full-cone coefficients are strictly positive. This is not a facetwise or simple-vertex surrogate.

#### Saddle edges

There is exactly one:

```text
P true edge                  (11,35)
compressed dual Q edge       (15,17)
original dual Q edge         (18,24)
normalized margin            0.019823424021624528
signs of (t,1-t,alpha,beta)  (+,+,+,+).
```

The edge is checked both for strict interior projection onto the segment and strict membership in the complete two-normal cone.

### Closest excluded features

The independently rebuilt signed exclusion margins are:

```text
nearest nonstable face:
  compressed row 18 / original row 25   -0.0042597426483666325

nearest nonunstable vertex:
  P vertex 34, original Q incidence (17,25,26)
                                            -0.0016540067466267164

nearest nonsaddle edge:
  P edge (20,34), original dual Q edge (17,25)
                                            -0.0016540067466267161.
```

The returned `(2,1,1)` class is therefore open and not a hidden wall state.

### Inactive incidence separation

```text
P minimum normalized inactive separation = 3.983506966992064e-5
Q minimum normalized inactive separation = 0.007975039242218398.
```

Both comparisons with `10^-5` are proved exactly by rational squared inequalities. The compact decisive record is certificate_summary.json.

## 4. What the continuation actually ruled out

The exact local wall and final endpoint are rigorous. The broader statements below are finite-family computational evidence, not a global impossibility theorem.

### Complete post-fan deletion scan

A complete scan of 512 valid row-deletion/deactivation subsets produced zero `(1,1,0)` state. Removing the exchange row relays the stable and saddle witnesses to adjacent rows and edges. The script and transcript are packaged in `exploratory/postfan_deletions.py` and `exploratory/postfan_deletions.out`.

### Global sequential support search

The strongest common-defect reduction reached approximately

```text
3.893057793176257e-4
```

but the actual rebuilt class was `(3,5,6)`, with P inactive separation only `6.365201385387368e-6`. Suppressing the local residual activates a source/saddle star around protected row `17`; the apparent improvement is not gate-valid.

### Unstable-incidence migration

Explicitly allowing the target unstable incidence to migrate did not create a one-source chamber. The strongest stored migration state was `(2,11,11)` with P inactive separation `6.1710739469761e-7`: nine to eleven new unstable/saddle features formed around the row-17 star.

### Long two-rail and great-circle strips

The residual original row `18` and protected original row `17` have norms approximately

```text
r_start = 262.2575957278703
r_end   = 387.0270388033747
```

and angular separation

```text
179.82522354469205 degrees.
```

For a monotone radial witness chain, the necessary dominance inequality

```text
r_end cos(theta/m)^m > r_start
```

first holds at `m=13`. Finite two-rail scans with `12,13,14,16,18` links yielded `(2,2,2)` or larger Euler-neutral blocks, never a winner. A separately optimized 13-link strip reached `(2,2,2)` but had P inactive separation `3.7092193110109727e-6`, below the gate.

### Direct residual quadrilateral flip

A direct flip of the local residual quadrilateral either deactivates the local row or creates multiple row-17-star pairs. It never opens a strict `(1,1,0)` cell.

The exact/empirical distinction, checkpoints, and source files are consolidated in search_obstruction_summary.json.

## 5. Structural obstruction and next topology

The five-row event proves that two adjacent cells can be exchanged in one connected non-stellar operation while exact centring and incidence gates remain under control. What it cannot do is supply enough geometric witness length to remove the Euler-neutral pair.

The residual stable and saddle witnesses occupy opposite ends of an almost antipodal radial chain. A local two-cell exchange chooses **which** neighboring row and edge carry the pair, but suppressing one route exposes another before both equilibrium signs become negative. When the local residual is forced smaller, the complete one-ring around row `17` births several unstable–saddle pairs; when the exchange row is deactivated, the original stable–saddle pair simply migrates to `(18,(18,24))`.

The next materially different architecture is therefore:

- one connected **nonlocal annular or bifurcated two-dimensional strip** rather than another local pentagon;
- at least 13 radial-ascent edges in the measured row-18-to-row-17 geometry;
- a second return branch whose first moment cancels the ascent branch inside the same connected complex;
- simultaneous crossing of two separated circuit blocks, not serial local flips;
- simultaneous permission for the observed relay candidates—at least rows `1,4,18,20,23,24,25,27`—to become non-extreme;
- migration of the retained unstable incidence if needed;
- the analytic projective gauge `u=c` and exact `-I_3` moment Jacobian on every accepted branch;
- P and Q inactive separation constrained above `10^-5` throughout.

Local pentagon exchange alone, a single quadrilateral flip, stellar subdivision, serial one-dimensional rails, metric-only polishing, and penalty-only centring are exhausted within this branch.

## 6. Independent verification and meshes

verify_post_five_independent.py uses only the Python standard library and does not import the generator or trust the stored topology. Starting solely from the hexadecimal input rows, it independently:

- enumerates every polar triple;
- reconstructs the complete P and Q face lattices;
- recomputes exact volume and first moments;
- reapplies the exact projective gauge;
- audits every maximal face;
- audits every vertex, including complete nonsimple normal cones;
- audits every true edge with segment and full two-normal-cone tests;
- checks every incidence and nonincidence;
- proves both inactive separations exceed `10^-5` exactly;
- proves strict origin interior and root-box boundedness.

The stored report is `PASS`: independent verification report (`independent_verification_post_five_circuit_gate_exact.json`), SHA-256

```text
60ef82c819a6fccb2534089afd70e3dbca5e7f7ba32eb52d60912f6bafb6997a
```

The integrity audit (`verification_integrity_check.json`) also reports `PASS` and confirms:

| Mesh | Vertices | Maximal OBJ faces | STL triangles | Certified cycles match |
|---|---:|---:|---:|:---:|
| P | `36` | `20` | `68` | yes |
| Q | `20` | `36` | `36` | yes |

Finite reconstruction files:

- P coordinates (`post_five_circuit_gate_P.csv`)
- Q coordinates (`post_five_circuit_gate_Q.csv`)
- P OBJ (`post_five_circuit_gate_P.obj`)
- P STL (`post_five_circuit_gate_P.stl`)
- Q OBJ (`post_five_circuit_gate_Q.obj`)
- Q STL (`post_five_circuit_gate_Q.stl`)

No coordinate-ball perturbation radius is claimed because the returned body is not a winner. Its exact strict signs and inactive gaps do prove an open `(2,1,1)` chamber.

## 7. Reproducible package

The complete distributable archive is santalo_five_circuit_result.zip.

```text
archive SHA-256
b0f34fc10ecd1f57e0ca9ca646def3704eefcdf6547c581da7ac506766a3b1a1
```

The checksum sidecar is santalo_five_circuit_result.zip.sha256.

Principal files:

- README (`README.md`)
- deterministic generator (`generate_post_five_exact.py`)
- exact geometry core (`exact_core.py`)
- complete pipeline driver (`rebuild_all.py`)
- exact endpoint certificate (`post_five_circuit_gate_exact.json`)
- exact coupled-five-row map (`coupled_five_row_circuit_map.json`)
- root-box certificate (`root_box_boundedness_certificate.json`)
- compact certificate summary (`certificate_summary.json`)
- search obstruction summary (`search_obstruction_summary.json`)
- independent verifier (`verify_post_five_independent.py`)
- verification report (`independent_verification_post_five_circuit_gate_exact.json`)
- integrity report (`verification_integrity_check.json`)
- manifest (`MANIFEST.json`)
- SHA256SUMS

Manifest SHA-256:

```text
e64195a9159f152b2a64511c073f7badc6c294644c6282c5fcac3a51946576f0
```

Reproduction after unpacking:

```bash
cd santalo_five_circuit
python rebuild_all.py
```

A fresh complete pipeline run finished with `ALL PASS`; the independent exact rebuild, root-box proof, mesh audit, and package checksums all agree.

## Final conclusion

The requested Gömböc was **not** reached. The branch nevertheless supplies the strongest possible honest handoff from this continuation: a fully exact gate-valid post-five-row-circuit `(2,1,1)` object, an exact connected codimension-two pentagon/two-cell transition, exact row deactivation and pair-transfer map, exact hard centring on every accepted endpoint, complete mechanics and incidence, independent verification, and finite meshes.

The decisive new delimitation is that a local five-row exchange is still too short: the next architecture must be a nonlocal 13-plus-link annular/bifurcated strip that crosses separated circuit blocks and cancels its own first moment within one connected topology change.
