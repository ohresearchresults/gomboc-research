# figure-0085

AI research report · 2026-08-26 UTC

---

# Branched-annular P2 continuation — complete handoff

## Determination

I did **not** obtain an accepted homogeneous convex polyhedral Gömböc. The gate remains an explicit finite uniform-density body, evaluated at its own exact volume centroid, with exhaustive strict `(S,U,H)=(1,1,0)` classification and complete H/V, face, edge, verification, and mesh data; auxiliary-origin mechanics and transfer-wall points do not qualify.

The inherited B210 endpoint was the correct starting frontier: a materialized own-centroid `(2,1,1)` body whose residual dual maximum and saddle were wholly inside the previously inserted connected basin, and whose next nonredundant operation was a moment-balanced annular replacement of that entire new sub-basin.

This continuation performs that replacement at substantially larger scale. It removes/deactivates every requested B210 row `{30,31,33,34,37,38,39,41,43}`, retains 27 non-basin input rows, inserts a connected 48-support, 24-level, two-branch annulus, crosses genuine Q incidence circuits, recomputes the full hull and uniform centroid after every accepted transition, and then searches determinant-one centroid-preserving metrics. The best open own-centroid endpoint is **MA300**, with strict class `(2,3,3)`, not `(1,1,0)`.

## Reproducible finite artifact

The complete archive is p2_annular_ascent_bundle.zip, SHA-256

`43c78e8885b4ddd6b3a4927ec94d5524a21af907fe8fd86134eeffbd918eb4af`.

Its manifest (`MANIFEST.sha256`) has 178 entries; `sha256sum -c MANIFEST.sha256` passes for every entry. The bundle includes every saved H/V state, complete maximal-face cycles and true edges, all feature-cone records, raw and centered supports, moment-Jacobian experiments, circuit transitions, deterministic reconstruction, two independent verifiers, OBJ/STL, and search logs.

Primary MA300 files:

- centered V coordinates (`MA300_robust_metric_annular_P.csv`), SHA-256 `c4d68b0a01854a15f3f92fa0f7fa2eacc8b69c92a02e972779973139d711828d`;
- all centered H rows (`MA300_robust_metric_annular_H_all.csv`) and 52-row irredundant H set (`MA300_robust_metric_annular_H_active.csv`), the latter SHA-256 `521c51737a455c11640334a94820ad8ed14e60f12d38c530107469e7063b62e4`;
- complete P audit (`MA300_robust_metric_annular_P.audit.json`), SHA-256 `2d12d989bbbb884957dde4ba58ac97744fdb9a046ab191de28357cd8ca3bd850`;
- complete centered-Q/Santaló audit (`MA300_robust_metric_annular_Q_at_Santalo.audit.json`);
- maximal-face cycles and all 150 true edges (`MA300_robust_metric_annular_P.combinatorics.txt`);
- support provenance, annular graph, radial-ascent checks, active/redundant rows, and metric (`MA300_robust_metric_annular_support_metadata.json`);
- deterministic finite generator (`MA300_generator.py`), independent V verifier (`independent_verify.py`), and independent polar/H–V verifier (`verify_MA300_polar_pair.py`);
- OBJ (`MA300_robust_metric_annular_P.obj`), SHA-256 `fcd22f8fcedb9959da43932a8a6092d861a09e44674eb40ee8b8ce9e1e982ed5`, and STL (`MA300_robust_metric_annular_P.stl`), SHA-256 `98f907cacaa601d0297e8818ee2dffc21a73af8b298e06ed349e9f0c6d4449d1`;
- topology narrative (`TOPOLOGY_PATH.md`), machine-readable path (`topology_path.json`), quantified moment obstruction (`moment_closure_obstruction.json`), and geometric obstruction (`GEOMETRIC_OBSTRUCTION.md`).

MA300 is a deterministic finite decimal object, independently reconstructed to sub-`5e-16` Hausdorff error. Because it is a nonwinner, I did not promote it to a rational/interval theorem or claim an exact target perturbation box.

## Architecture actually tested

### Whole-sub-basin deletion

In B210 row numbering, the requested residual trunk/one-ring rows

`[30,31,33,34,37,38,39,41,43]`

are absent from the new input set. The retained B210 rows are

`[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,21,22,23,32,35,36,40,42]`.

The construction then adds rows `27..74`: 24 levels with one dominant A support and one subordinate B support per level. In the final centered Q:

- all 48 inserted rows are genuine extreme vertices;
- they form one connected component;
- the inserted complex has 95 internal true edges and 53 true edges to the retained boundary;
- each branch has twelve consecutive positive radial-ascent steps in MA300;
- at the auxiliary-origin target RT294, the dominant branch realizes all 24 intended ascent steps.

Thus this is a connected two-dimensional basin replacement, not a serial cap rail or a collection of mechanically independent moment actuators.

### Hard centering and accepted circuit states

For every accepted candidate, the complete polar was integrated and the own-centering projective gauge was applied before mechanical scoring. If raw supports are `Q_i` and the polar centroid is `c`, the centered H rows are

`B_i = Q_i / (1 - Q_i·c)`.

Every accepted topology was then rebuilt from these rows; no old triangulation labels were carried across a circuit. Two true Q incidence transitions were materialized:

1. `OA300_pretransfer -> SLP300_transfer`: four true edges and eight maximal triangles change;
2. `SLP300_transfer -> AS300_postannular`: edge `[11,31]` is replaced by `[29,33]`, with the corresponding two-face circuit rebuilt.

The later `AS300 -> MA300 -> MT300` continuation is different: it uses determinant-one SPD metrics, so the centroid and complete face lattice remain fixed while only mechanical signs cross.

## Complete topology/mechanics path

| State | Q rows/active | Q class at reference/Santaló point | P `(V,E,F,C)` | P class at own centroid | Minimum inactive P slack | Raw centroid norm before projective centering | Minimum absolute feature margin |
|---|---:|---:|---:|---:|---:|---:|---:|
| B210 inherited | 44/39 | `(1,2,1)` | `(68,105,39,210)` | `(2,1,1)` | `9.2528040e-8` | `1.6418064e-5` | `6.1882575e-8` |
| RT294 origin target | 75/51 | `(1,1,0)` | `(98,147,51,294)` | `(2,8,8)` | `6.4962625e-8` | `9.1215472e-3` | `6.1688051e-5` |
| MC05 early break | 75/46 | `(1,3,2)` | `(88,132,46,264)` | `(2,10,10)` | `5.9676113e-8` | `8.6856341e-3` | `7.1584642e-5` |
| MC20 deactivated | 75/38 | `(1,2,1)` | `(72,108,38,216)` | `(2,13,13)` | `2.3749314e-6` | `7.5726945e-3` | `7.7509033e-5` |
| OA300 pretransfer | 75/52 | `(1,2,1)` | `(100,150,52,300)` | `(2,3,3)` | `6.3122053e-7` | `8.3532136e-2` | `5.5030352e-4` |
| SLP300 transfer | 75/52 | `(1,1,0)` | `(100,150,52,300)` | `(2,4,4)` | `2.5244254e-7` | `1.0732732e-1` | `1.5322148e-4` |
| AS300 post-annular | 75/52 | `(1,2,1)` | `(100,150,52,300)` | `(2,4,4)` | `2.5174582e-7` | `1.0755556e-1` | `1.5237870e-4` |
| MS726 multi-sheet | 123/123 | `(1,2,1)` | `(242,363,123,726)` | `(2,3,3)` | `3.9991279e-8` | `7.5035175e-2` | `2.4835745e-4` |
| **MA300 robust metric** | 75/52 | `(3,2,3)` | `(100,150,52,300)` | **`(2,3,3)`** | `3.1363357e-7` | `0` | `2.6405626e-5` |
| MT300 metric transfer | 75/52 | `(3,3,4)` | `(100,150,52,300)` | `(3,3,4)` | `3.1239098e-7` | `0` | `1.6939947e-5` |

Every row in this table has a coordinate/support file and a complete audit under `states/` in the archive.

## Strongest open post-annular body: MA300

### Realized hull, mass, and incidence

- `(V,E,F,C) = (100,150,52,300)`;
- triangle-fan volume `3.9856652056826556e-5`;
- independent maximal-face-fan volume `3.985665205682656e-5`;
- triangle-fan centroid `(-4.1512970479812366e-17,-7.098479282301374e-18,-2.5529718030944786e-18)`;
- maximal-face-fan centroid `(-4.8496654802500455e-17,-1.4372718079038896e-17,-1.4372069519945036e-18)`;
- centroid disagreement `1.0145507774077692e-17`;
- centered first-moment norm `1.6816639469766502e-21`;
- minimum inactive P-plane slack `3.1363356684660504e-7`;
- maximum incident-plane residual `2.914335439641036e-16`;
- inactive/residual ratio `1.076175249357143e9`;
- minimum absolute complete-feature margin `2.640562572732426e-5`;
- closest excluded face, edge, and vertex margins respectively `-2.640562572732426e-5`, `-4.622176256070093e-5`, and `-0.0029137738309218163`.

The same `(100,150,52)` face lattice and `(2,3,3)` class are reconstructed at plane tolerances `1e-13`, `1e-12`, `1e-11`, `1e-10`, and `1e-9`. This is an open non-target cell, not an incidence merge or numerical wall.

### Exhaustive own-centroid equilibrium witnesses

Stable maximal faces:

1. vertices `[0,6,36,61,62,98,99]`, outward cycle `[0,98,99,61,62,36,6]`, margin `0.005907081203510886`;
2. vertices `[6,35,36,47,49]`, outward cycle `[36,35,49,47,6]`, margin `0.003263411104727501`.

Unstable vertices:

- vertex `6`, margin `0.9225500642884975`;
- vertex `19`, margin `0.002418450500233049`;
- vertex `23`, margin `0.0031805024307969983`.

Saddle true edges:

- `[0,11]`: endpoint/mechanical margin `0.003267330893738772`, projection parameter `t=0.06690153409477849`, normal-cone coefficients `[0.028096325342640078,0.026923597191382227]`, cone residual `4.13e-18`;
- `[19,23]`: margin `0.0002623449425281951`, `t=0.43194640126332123`, coefficients `[0.0061010743205493975,0.10832845849747014]`, cone residual `2.15e-17`;
- `[35,58]`: margin `0.0032624357663983187`, `t=0.18766775891832646`, coefficients `[0.021106920195474613,0.01822572407594141]`, cone residual `4.10e-17`.

All other 50 maximal faces, 97 vertices, and 147 true edges are strictly non-equilibria. Their complete projection/cone records are in the P audit.

The intended old P2 target pair was allowed to migrate, as permitted by the assignment. MA300 is therefore not claimed to preserve the original 17-gon/north labels; its actual equilibrium features are exactly those listed above.

### Irredundant final H set and obsolete rows

There are 75 supplied centered rows. The 52 irredundant rows are

`[3,11,16,22,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74]`.

The 23 explicitly redundant/obsolete rows are

`[0,1,2,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,21,23,24,25,26]`.

Thus every inserted row `27..74` survives as an extreme support, while only four retained B210 rows—`3,11,16,22`—remain active. The active H CSV is already stripped to the true 52-row representation.

### Centered dual Q

The irredundant centered support polytope has `(V,E,F,C)=(52,150,100,300)` and Santaló-origin class `(S,U,H)=(3,2,3)`.

- minimum Q nonincidence separation `5.294536553890339e-5`;
- maximum incident residual `1.4210854715202004e-14`;
- minimum absolute Q feature margin `0.004653328728582078`;
- critical rows `[3,16,28,30,50,52,54,71,73]`;
- full critical one-ring `[3,11,16,22,27,28,30,32,34,36,38,40,42,44,46,47,48,49,50,51,52,53,54,56,58,60,62,64,66,68,69,70,71,72,73,74]`.

The polar verifier confirms origin interior H-margin `4.872995496103554`, all 48 inserted supports extreme, inserted-complex connectivity, and exact dual count consistency.

### Centroid-preserving metric

MA300 applies the determinant-one SPD matrix

`M = [[0.9005083983225537,0.15101226263854972,0.04348973499218826],[0.15101226263854975,0.666854464370636,-0.18517714936532798],[0.04348973499218827,-0.18517714936532798,1.7908369786269598]]`.

Its determinant is `0.9999999999999999`, eigenvalues are `[0.5646210537558617,0.9726181695476216,1.820960618016666]`, and condition number is `3.225102227243618`. The parameter vector is

`[-0.12410650361050478,0.20294668991365458,0.04746524056866212,-0.4475384237044731,-0.169386738311746]`.

The saved robust endpoint uses `0.995` of the final near-wall metric displacement. The closer endpoint had feature margins around `1e-11` and was deliberately rejected.

## Independent reconstruction

From the extracted archive, the decisive checks are:

    python independent_verify.py MA300_robust_metric_annular_P.csv --plane-tol 1e-12 --expect-class 2,3,3 --expect-counts 100,150,52,300 --json check_P.json
    python verify_MA300_polar_pair.py --json check_polar.json
    python MA300_generator.py --prefix regenerated
    sha256sum -c MANIFEST.sha256

The independent polar verifier reports:

- generated/reference V-set Hausdorff error `3.7789906771029953e-16`;
- separate H/V consistency Hausdorff error `4.911718730997779e-16`;
- maximum active-H violation `2.4424906541753444e-15`;
- 52 active H rows = 52 reconstructed maximal P faces;
- all inserted rows extreme `true`;
- connected inserted complex `true`;
- dual count check `true`.

## New obstruction: why the annulus does not close

### The auxiliary-origin cancellation is real but not homogeneous

`RT294_origin_target` is a strict auxiliary-origin `(1,1,0)` Q construction. Its raw polar centroid is

`c=(0.009093126047198507,-5.32886994276878e-5,-0.0007175245686532681)`,

with norm `0.00912154715507998`. After mandatory own-centering, the primal is `(2,8,8)`. Therefore witness length and a connected annulus can produce the desired origin-relative flow, but not the homogeneous flow.

### Moment rank exists; the mechanically safe moment cone is too small

The `3×48` Jacobian of the polar centroid with respect to individual annular log radii has singular values

`[0.00627988,0.00368129,0.00084590]`.

So there is no first-order rank obstruction. However, the minimum-`L∞` linearized exact moment correction requires

- `||z||∞ = 0.5927665254367562`;
- `||z||2 = 4.0229193099121465`;
- support-radius multipliers spanning `[0.5527958435632397,1.8089861051670522]`.

At only 5% of this correction:

- raw reference mechanics has already changed `(1,1,0) -> (1,3,2)`;
- active supports fall from 51 to 46;
- the own-centroid primal becomes `(2,10,10)`;
- only about 4.8% of the centroid norm is removed.

At 20%, only 38 of 75 supports remain extreme and the own-centroid class is `(2,13,13)`. An 18-mode smooth correction lowers the raw centroid norm to approximately `7.34e-4`, but collapses the support hull to ten active Q rows and still gives own-centroid `(2,3,3)`.

This quantitatively separates **linear controllability** from **controllability inside the required incidence/mechanical chamber**. The first-moment null directions are too oblique to the two-branch annulus's radial-ascent chamber.

### More parallel rails reproduce the same seam

Connected `K=3,5,7` multi-rail sheets, including a state with 151 inserted active supports, were also rebuilt and audited. They remain `(2,3,3)` or worse. Added transverse moment leverage creates a new stable/saddle seam, so the Euler-neutral defect is relayed across the wider sheet instead of annihilated.

### The centroid-preserving metric path also transfers the block

The determinant-one metric removes one unstable-saddle pair while algebraically preserving the centered centroid and entire 52-face lattice, improving AS300 from `(2,4,4)` to MA300 `(2,3,3)`. Continuing in that same lattice reaches a genuine mechanical wall: the existing 25-gon

`[0,1,6,7,11,12,13,14,15,16,17,18,19,20,21,23,24,37,38,42,43,47,48,51,52]`

becomes stable while true edge `[6,47]` becomes a saddle, entering MT300 `(3,3,4)`. No incidence ambiguity is involved; inactive P slack remains about `3.12e-7`. This is a fixed-lattice Morse transfer.

## Why this failure is not another serial-rail failure

The earlier P2 failures could be explained by one-sided or bilateral serial caps moving a single pair to adjacent faces and edges. Here:

- the complete requested B210 sub-basin is absent;
- all 48 replacement supports are simultaneously extreme;
- the replacement is a connected two-dimensional annulus with 148 internal/boundary true edges;
- at least twelve radial-ascent steps survive on both branches;
- true Q circuits were crossed and the full hull was rebuilt;
- the complete integrated own-centroid gauge was recomputed before all accepted mechanical audits;
- the failure persists under wider three-, five-, and seven-rail sheets and under a centroid-preserving metric orbit.

The new obstruction is therefore more specific: a two-branch annulus can realize the radial witness ordering or supply a full-rank moment Jacobian, but in the tested geometry it cannot do both within one open incidence chamber. Moving far enough in the moment-closing directions destroys extreme supports and births multiple equilibria; staying in the open chamber leaves a connected Euler-neutral residual block that transfers at the next mechanical wall.

## Smallest genuinely unsearched whole-basin continuation

The next operation should not append to MA300. Delete/deactivate the entire 36-row centered-Q critical one-ring

`[3,11,16,22,27,28,30,32,34,36,38,40,42,44,46,47,48,49,50,51,52,53,54,56,58,60,62,64,66,68,69,70,71,72,73,74]`

in one circuit-scale move.

Replace it by a **three-lobed communicating annulus** with approximately 34–38 active supports:

- three 12-edge ascent branches share one root and one terminal boundary;
- two transverse cross-lobes couple the branches so positive and negative first moments cancel inside the same connected two-dimensional complex;
- three independent branch-depth variables are eliminated by the exact Santaló equations **before** mechanical scoring or branch acceptance;
- every old one-ring row may become redundant simultaneously;
- every surviving new row must be extreme;
- require raw Q and P inactive separation above `1e-5` throughout;
- rebuild all maximal faces, true edges, and full normal cones after each circuit crossing.

This is the smallest untested architecture that changes the radial witness assignment and all three first moments in the same connected cell. A third branch is essential: the two-branch Jacobian has rank three but requires order-one radial deformation, while independent extra parallel rails merely create another transfer seam.

## Limits

No strict own-centroid `(1,1,0)` body was found, so there is no target all-feature margin, target perturbation radius, or exact rational/interval certificate to report. MA300 is instead a strongly separated, completely materialized numerical nonwinner: its incidence reserve is more than `10^9` times its incident residual, its closest complete-feature wall is `2.64e-5` away, its H/V reconstructions agree below `5e-16`, and its full data are sufficient for independent reconstruction and continuation.
