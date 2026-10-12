# figure-0420

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Maple 10 — finite geometric deformation handoff

## Outcome and exact continuation point

**No own110/weak000 polyhedron was obtained.** This handoff preserves nine genuinely changed, exactly recoverable rational bodies, not another analysis of the unchanged C366 graph. The recommended continuation is **COARSE20_G4**, a uniformly filled, 45-facet body with

`V=86, E=129, F=45, C=258; strict (S,U,H)=(1,2,1); weak=(0,0,0)`.

Its volume-normalized secondary squared-radial persistence is approximately **0.450019249**, versus **1.756874280** for the exact C366 parent: a **74.39% reduction**, with better roundness and much smaller coordinates. Nevertheless, its secondary basin remains substantial; this is neither an own110 solution nor an accepted-record improvement.

The last 20-step volume-normalized stage accepted all 20 steps. I did not establish a terminal plateau. Continuing that geometric search from the exact coarse endpoint is better supported by this run than declaring the direction exhausted.

Source authority is immutable parent `figure-0416`, supplied SHA-256 `8bb0d3cd368fedab4fc75fc6733ebdd740451ca872d7fe3eab61fdd54b6b2054`. Its eight-file literal capsule was decoded, checked, and replayed. The decoded dictionary has 25,695 bytes and SHA-256 `77c7d697f8dd274c5e98d1e9a382b2c97eb700457f21ef1f805eba6703ccfc3d`. No authority conflict was found. C366 was treated as the intersection of its 63 physical halfspaces, not as the hull of their normal rows.

## What changed geometrically

I parameterized physical halfspaces as `q_i·x <= 1`. Free changes in all three components of each row change both normal direction and plane distance. Initially all 63 rows were free, including the stable-side interface; this was not an isolated edit to one escape arrow. Each numerical trial rebuilt the polar hull, solved for physical vertices, rebuilt physical face cycles and true edges, integrated the actual uniformly filled volume, and recentered at that volume centroid. Root and witness choices were refreshed rather than frozen.

The primary geometric objective was the secondary **true-edge radial basin**, not a local vertex deficit. For a centered edge `e=x_j-x_i`, its superlevel connection height is

`lambda_ij = min_{0<=t<=1} ||x_i+t e||^2`,

with the exact segment minimizer clamped to `[0,1]`. A maximum spanning tree of these edge heights gives the merge levels of radial maxima. A secondary bar is `Delta = birth_radius_squared - merge_radius_squared`. The later search minimized the sum of such bars divided by `Volume^(2/3)`, rather than rewarding an increase of the farthest radius through a `Delta/R^2` denominator alone.

A first stable-only restoration method reduced this objective but fragmented the physical basin into 18 unstable equilibria. I therefore added simultaneous physical and polar positive-escape restoration. Each nonstable polar vertex and each physical vertex except the two currently permitted maxima needed a positive nominated escape. Linearized steps used the derivative of the actual volume centroid, followed by nonlinear restoration, live topology rebuilding, and finite backtracking. The two maxima were not required to remain: a one-maximum endpoint would have been accepted. No material-root exchange has been certified merely from changed index labels.

The numerical stage was not accepted as a certificate. Both physical reconstruction algorithms used for the final claims are exact and independent of the search chart; their complete runnable sources are in the recovery capsule.

The retained sequence includes 34 accepted coupled steps from C366, a 24-step continuation after exact active-support removal, 24 volume-normalized steps, 24 angular-bending steps, margin conditioning and coarse quantization, then another 20 volume-normalized steps. The original first coupled call requested 50 steps but stopped after 34 completed steps; no completed 50-step run is claimed. The executable recipe specifies that completed prefix.

Topology changed materially: 63 actual facets became 45. The final unique stable face is a pentagon, not the parent's triangle. The numerical path itself has not been certified continuously; the exact claims below apply to the independently reconstructed rational endpoints.

## Retained exact bodies

Every row below has **weak census 000**, zero face/vertex/edge primitive-boundary counts, a fully rebuilt maximal complex, byte-identical independent A/B audits, and a third exact centered filled-volume integration. Labels are local to each reconstructed body. No count is obtained by retaining a triangulation from an earlier body.

| Exact input name | V / E / F | C | Strict S,U,H | Largest Delta / R^2 | Largest Delta / Volume^(2/3) | r / R |
|---|---:|---:|---|---:|---:|---:|
| OUT — unchanged C366 control | 122 / 183 / 63 | 366 | 1,2,1 | 0.849887675 | 1.756874280 | 0.245366359 |
| HG34_G8 | 92 / 138 / 48 | 276 | 1,2,1 | 0.300913805 | 0.612815431 | 0.276734538 |
| HGA24_G8 | 88 / 132 / 46 | 264 | 1,2,1 | 0.302130128 | 0.476211331 | 0.327134881 |
| HA24_G8 | 86 / 129 / 45 | 258 | 1,2,1 | 0.351202639 | 0.493859905 | 0.348036710 |
| COND2_G1000 | 86 / 129 / 45 | 258 | 1,2,1 | 0.358186940 | 0.546919009 | 0.328137530 |
| **COARSE20_G4** | **86 / 129 / 45** | **258** | **1,2,1** | **0.282431498** | **0.450019249** | **0.325313296** |
| HR100_G8 — fragmented basin | 90 / 135 / 47 | 270 | 1,18,17 | 0.230095676 | 0.487769576 | 0.273081556 |
| HCAP_G9 — oblique cap plus restoration | 88 / 132 / 46 | 264 | 1,2,1 | 0.346791819 | 0.487659900 | 0.348035641 |
| HDEEP_G8 — deep-cap failure | 84 / 126 / 44 | 252 | 25,19,42 | 0.208151119 | 0.282264584 | 0.376685880 |
| COND2_G500 — coarse-rounding failure | 86 / 129 / 45 | 258 | 6,3,7 | 0.357999241 | 0.546507126 | 0.328190960 |

Displayed decimals are approximations to reconstructed exact quantities. For multiple-secondary-maximum bodies, the table reports the largest bar, not their sum. The exact sums `sum Delta/R^2` are approximately 0.250300158 for HR100_G8, 0.311987372 for HDEEP_G8, and 0.358001458 for COND2_G500. The recovery generates every positive bar and its exact interval.

The nonwinners matter. HR100_G8 demonstrates that lowering total radial persistence with only S=1 protected can create many U/H pairs. HDEEP_G8 shows that a deep oblique cut can sharply reduce the principal physical barrier while destroying the stable-side organization. COND2_G500 is an exactly classified failed rounding, not an arithmetic simplification claimed to preserve the object. COND2_G1000 is a useful alternative seed with at most 12-bit plane integers. HA24_G8 retains better roundness than the recommended endpoint.

The cap family was fully specified and finite: the three owner normals of the secondary maximum in the supplied HA24 floating checkpoint, input indices `[2,5,23]`, were combined with all integer weights `(a,b,8-a-b)/8` and multipliers `[1.005,1.02,1.05,1.1,1.2,1.35,1.6,2,2.5,3.5,5]`. All 495 trials were numerically valid. These owner indices refer to that literal floating checkpoint, not blindly to sorted RAW support indices. HCAP_G9 comes from weights `[0,3,5]`, multiplier 1.005, and one coupled restoration iteration. HDEEP_G8 comes from `[0,1,7]`, multiplier 1.6; its attempted restoration failed within the stated finite settings. None of those failures is an exclusion of other caps or coupled architectures.

## Exact main endpoint and its remaining basin

Here is the complete literal main input. Each row means `n_x*x+n_y*y+n_z*z <= h`. Offsets vary after primitive gcd reduction; do not replace them all by 10000.

```json
{"H":[[-23190,-6905,7908,10000],[-23088,97,6721,10000],[-21661,5105,5356,10000],[-17597,11697,2180,10000],[-16506,-12372,7875,10000],[-15397,13821,443,10000],[-13071,15339,-1234,10000],[-10613,16339,-2844,10000],[-10253,-15023,6915,10000],[-9872,4347,2001,5000],[-8199,16851,-4303,10000],[-6376,-16759,4976,10000],[-5833,16950,-5611,10000],[-3665,16729,-6919,10000],[-2678,-17455,2777,10000],[-167,1623,-810,1000],[297,15435,-9155,10000],[1155,-15101,3297,10000],[2197,-10814,-6880,10000],[2201,14349,-10087,10000],[2405,622,276,2500],[3006,1081,6706,10000],[3264,4489,-6993,5000],[3833,13183,-10670,10000],[3962,-12705,3497,10000],[4347,2304,6079,10000],[5291,968,-435,5000],[5412,11703,-11335,10000],[5706,613,-3769,5000],[5736,-9516,4393,10000],[5828,11380,-5775,10000],[6814,10496,-10529,10000],[7703,5260,-15433,10000],[7842,-4197,-15197,10000],[8079,9158,-9659,10000],[8156,2782,3261,10000],[8256,790,-15971,10000],[9073,7863,-8907,10000],[9942,6471,-7945,10000],[10587,-1650,-4026,10000],[10595,5108,-7165,10000],[11131,3547,-6374,10000],[11185,-1885,-8502,10000],[11301,1137,-2946,10000],[11329,2340,-4572,10000]]}
```

Its canonical RAW serialization is **1,122 bytes**, SHA-256 `80981f4c9fcf91d6b402e0b85d82d40d5a260eecf23888bdf2d3041d5dfa9011`. A and B are each **35,462 bytes**, both SHA-256 `f2524f0ece775e220e09acbb3e8a168428db90bc288374295e43b9190448ccde`. MASS is **221 bytes**, SHA-256 `9883865e5db976c346b9f6b65de8c80811df909c464ffc3b99807a098a58a077`.

Using closed-lower/open-upper intervals with denominator `10^12`, the actual raw filled centroid lies in

`[227954240944,227954240945) x [78294894277,78294894278) x [298536096349,298536096350)`,

and the volume lies in `[2137890010255,2137890010256)/10^12`. These are display intervals, not the centroid used by the audit: its full exact rational coordinates are reconstructed. The third integration uses 168 positive tetrahedra and verifies exact zero centered first moments and the same volume. Its common centered denominator has 5,481 bits.

The exact unique stable face is face 0, cycle `[2,9,11,24,22]`. The unstable vertices are `[0,25]`; the only saddle edge is `[82,85]`. The global radial root is vertex 0. For the secondary maximum 25:

| Quantity | Exact interval numerators over 10^12 |
|---|---|
| Birth radius squared | [1483787208691, 1483787208692) |
| Merge radius squared, edge 82–85 | [736957941797, 736957941798) |
| Segment minimizer t on 82→85 | [545571369203, 545571369204) |
| Delta | [746829266894, 746829266895) |
| Delta/R^2 | [282431497734, 282431497735) |
| Delta/birth radius squared | [503326395132, 503326395133) |
| Minimum true-edge length | [4054332067, 4054332068) |

Thus the barrier is still about half of that secondary peak's squared radius. This is not an almost-cancelled pair.

The independently checked directed true-edge cosine bottleneck satisfies the strict interval

`-445959388/10^9 < beta < -445959387/10^9`,

with unique critical outward arc `69 -> 83`. The complete negative-exit cut is

`[21,22,23,24,25,26,27,29,30,33,34,35,36,37,38,41,44,45,48,49,57,69]`.

Its 20 outward arcs are

`[[21,1],[22,2],[30,4],[27,5],[33,6],[38,8],[23,10],[26,10],[24,11],[41,14],[44,17],[45,17],[29,19],[35,19],[36,31],[36,53],[37,73],[41,40],[49,68],[69,83]]`.

The stable pentagon meets this cut at vertices 22 and 24. A full rooted tree and the complete cut are regenerated and independently checked with integer comparisons. This proves a real negative basin for this endpoint; opening one named arrow alone is not a cancellation certificate.

Conditioning improved substantially. Plane integers need at most 15 bits; raw vertex numerators and denominators need at most 41 and 42 bits. The exact selected positive-exclusion forests have minimum cosine intervals `[463790106,463790107)/10^12` on the polar/stable side and `[707874179,707874180)/10^12` on the physical non-U side. These are certified margins of the nominated witnesses, not claims that all true edges have those margins or that the nomination maximizes a margin. The inradius/circumradius ratio is about 0.325313296, compared with 0.245366359 for C366; `Volume/R^3` improves from about 0.336458318 to 0.497190771.

## A strictly local, topology-free obstruction

The new body also admits a useful finite-neighborhood statement. Let K be COARSE20_G4 translated to its exact filled centroid. Direct rational checks give

`r(K)>0.529`, `R(K)<1.627`, `secondary peak radius>1.218`, and `merge radius<0.859`.

The certified radial-amplitude gap is therefore greater than 0.359. True-edge radial connectivity represents whole-boundary superlevel connectivity: on each convex face, a radius sublevel is its intersection with a disk, and the components outside that disk are represented by the surviving boundary arcs. The exact maximum-spanning tree and cut consequently certify the secondary-to-root merge on the boundary, not just on an artificial triangulation.

A radial sup-norm perturbation of at most eta cannot merge these two high components when `2 eta < 0.359`. For centered bodies with Hausdorff distance s from K, support-function inclusions give a radial error at most `1.627*s/0.529`. It follows that **every convex polyhedron whose own-centered body is within Hausdorff distance 0.058 of K still has at least two strict unstable equilibria**, regardless of facet count or topology.

There is also a weaker bound without prescribing the new centroid. For uncentered Hausdorff distance `epsilon=0.0029`, put `t=epsilon/0.529`, `a=1-t`, `b=1+t`. The inclusions `aK subset L subset bK` and uniform filled-volume integration give

`||c_L|| <= d = b*1.627*(b^3-a^3)/a^3`.

Then the centered Hausdorff distance is at most `tau=epsilon+d`, and twice the radial-error bound is about **0.3543375690433 < 0.359**. Hence that closed uncentered neighborhood also excludes U=1. The enclosed proof states the geometric argument and `NEIGHBORHOOD.py` checks every rational scalar inequality against the exact reconstructed body. This is only a neighborhood obstruction, not an impossibility result for the branch or for larger finite deformations.

## Verification closure and continuation

Auditor A enumerates exact triple-plane intersections and rebuilds maximal face polygons. Auditor B independently clips support-pair lines and reconstructs the same complex. They agree byte for byte, including exact volume, first moments, centroid, all strict/weak classifications, and boundary signs. The third integration is based at the exact filled centroid and uses integer tetrahedra. The exact graph checks independently verify the cosine tree/cut and the radial maximum-spanning-tree cycle property.

Both rejection controls were run: the regular tetrahedron gives strict446/weak000; the supplied weak prism gives strict446/weak123. Both are rejected by the own110 target predicate. A cold execution from the inline capsule below regenerated and hash-checked all ten bodies, and separate re-freezes from all nine retained numerical terminal checkpoints matched their RAW/A/B/MASS bytes.

The capsule contains the complete eight parent source files, complete numerical search modules and all non-default recipes, all ten literal integer-halfspace inputs, the three literal pre-quantization inputs needed between material search stages, exact auditors, metrics, independent graph checks, neighborhood proof/checker, per-file manifests, and expected output hashes. No journal alias, historical lookup, numerical optimizer rerun, or sandbox file is needed to recover any retained rational endpoint. Numerical trajectories are version-bound; exact endpoint closure is from literal integer inputs. The supplemental archive also retains the terminal floating checkpoints, which are not needed to reconstruct their literal rational successors.

Numerical production used CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu, float64, and one BLAS/OpenMP/PyTorch thread. No random generator was used. Exact replay needs only the Python standard library and must not use `-O`.

The most useful continuation is to start from `data/COARSE20_G4.json`, restore positive physical/polar guard floors of 0.001 if needed, and continue the volume-normalized coupled search with trust 0.05 and both current U roots permitted but not required. The last stage had not plateaued. Rebuild the actual complex and re-audit each retained endpoint. If that continuation stalls, the 22-vertex cut and stable pentagon identify the region for a genuinely finite coupled interface change; the 45-facet seed leaves room for up to 60 additional supporting planes while keeping at most 105 active facets, which implies E<=309 and C<=618. The tested deep single-cap family is a warning about loss of S=1, not evidence against broader rearchitecture.

## Self-contained recovery capsule

Save the complete following program as `RECOVER_KM10.py` and run:

```sh
python -B -S RECOVER_KM10.py KM10_RECOVERED
```

It extracts 44 files and immediately performs exact closure. The compressed payload is 38,068 bytes, SHA-256 `3ba22ed7077d21789be9ea7fc4db22d219b49738d17ef6360a4bbc316c369012`. Its uncompressed deterministic stream is 115,875 bytes, SHA-256 `5fd5fbf8147812bc35c6bd3ebe1cdebbf7ec9b8c12b435f0480d776193c57e05`. Extracted file bytes total 131,841; individual byte counts and hashes are checked by `MANIFEST.json`. Integer halfspace rows are losslessly delta-coded; the three floating input arrays are losslessly encoded binary64. All other files are literal UTF-8 source/data.

Expected final markers:

```text
KM10_SOURCE_CAPSULE_RECOVERY_PASS 44
KM10_EXACT_CLOSURE_ALL_PASS 10 bodies
TARGET_OWN110_C_LT_622_FOUND false
```

To inspect or rerun a recorded finite search after recovery:

```sh
cd KM10_RECOVERED
python REPLAY_SEARCH.py --list
python REPLAY_SEARCH.py coarse_radial_20 NEW_SEARCH_DIRECTORY
```


[Encoded source block omitted; the code in this passage is incomplete.]


Supplemental artifact: [Full sources, terminal floating checkpoints, and exact audit outputs](sandbox:/mnt/data/KM10_FULL_RECOVERY.zip). The ZIP is 799,987 bytes, SHA-256 `ed78e1061db126e82195035455600b0aecf4fd9dde364af27c8e4a636ec49e00`; it is supplementary, not a dependency of the inline recovery.
