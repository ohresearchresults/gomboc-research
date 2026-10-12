# figure-0075

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Simultaneous full-dual-basin P2 replacement — complete handoff

## Verdict

I did **not** find a certified homogeneous convex polyhedral Gömböc. The acceptance gate remains an explicit finite uniform-density body evaluated at its own volume centroid with strict `(S,U,H)=(1,1,0)`, complete H/V incidence, an independent verifier, and matching mesh; an auxiliary center, wall point, or near-solution does not qualify.

The requested nonredundant operation was nevertheless carried out: starting from the inherited robust R160 endpoint, I removed the complete recorded dual basin and replaced it by a **single connected two-dimensional polar support complex**, rather than appending another serial cap. The journal identified R160 as `(45,80,37,C=160)`, strict own-centroid `(2,1,1)`, and specified simultaneous deactivation of the two dual paths as the next move.

The strongest resulting open body is **B210**, an explicit 68-vertex uniform convex polyhedron with strict own-centroid class `(2,1,1)`. It preserves the 17-gonal stable base and unique unstable vertex 8 but still has one stable–saddle pair. It is therefore a reusable post-basin endpoint, **not** a Gömböc.

## Reproducible artifact

The complete archive is p2_full_basin_replacement_bundle.zip, SHA-256

`3944c3780f606b4c8012bd4eacddaf3dd6f70ebcc2f720456e832ccb34f58375`.

It contains 147 files: every saved H/V state, complete maximal-face and true-edge audits, raw and centered polar supports, deterministic reconstruction, independent verifiers, topology path, selected search programs/logs, and OBJ/STL. The checksum inventory is MANIFEST.sha256.

Primary files:

- B210 centered V-coordinates (`B210_full_basin_centered_P.csv`) — SHA-256 `adc8ce2390dc276ed0f91fd3a13d54a36240fee6982e150ff5be8f504e8b3773`
- B210 raw Q supports (`B210_full_basin_raw_Q.csv`) — SHA-256 `81b36d7a8738bdb4c0b254e298f21e6517b02acc836f4b1843fb06ffab0d7741`
- all centered H rows (`B210_full_basin_centered_H_all.csv`) and 39 irredundant H rows (`B210_full_basin_centered_H_active.csv`)
- complete P audit (`B210_full_basin_centered_P.audit.json`), complete Q audit (`B210_full_basin_centered_Q.audit.json`), and human-readable combinatorics (`B210_full_basin_centered_P.combinatorics.txt`)
- support provenance and connected-complex incidence (`B210_support_metadata.json`)
- deterministic generator (`B210_generator.py`), independent V-verifier (`independent_verify.py`), and independent polar/H–V verifier (`verify_polar_pair.py`)
- OBJ (`B210_full_basin_centered_P.obj`) and STL (`B210_full_basin_centered_P.stl`)
- topology path (`TOPOLOGY_PATH.md`) and machine-readable path (`topology_path.json`)
- bundle README (`README.md`)

## What changed relative to R160

The two recorded D198-order paths

`14–13–16–23–19–17` and `14–13–16–23–20–37`

map to the R160 deletion set

`[14,34,33,36,28,32,30]`.

All seven exact old rows are absent from every post-basin state. B210 retains 30 non-basin inputs and introduces rows `30..43` as fourteen replacement supports. After own-centroid projective recentering:

- all fourteen inserted rows are genuine vertices of the centered Q hull;
- their induced graph is one connected component containing all rows `30..43`;
- the complex has 24 internal true edges and 40 true edges to the old boundary;
- Q has 39 active rows and five redundant retained rows `[24,25,26,28,29]`;
- the inserted-complex assertion is therefore combinatorial fact, not a visual or triangulation inference.

The centering transformation is recorded explicitly. If `c` is the true uniform centroid of the raw polar `P=Q°`, then the own-centered body has H rows

`B_i = Q_i / (1-Q_i·c)`, so `P-c = {x : B_i·x ≤ 1}`.

For B210,

`c = (3.254038969129454e-6, 1.608343860405996e-5, 5.357720446095020e-7)`,

and the denominators range from `0.9998081458003125` to `1.0001087133075006`. The generated P point set agrees with the bundled reference at Hausdorff distance `0.0` in the recorded double-precision reconstruction, and the largest H-inequality violation is `1.11e-15`.

## B210: complete mechanical determination

### Hull, mass, and incidence

- realized `(V,E,F,C) = (68,105,39,210)`;
- volume `0.022042716810596604`;
- triangle-fan centroid `(-3.74896294034823e-17, 5.993393243094224e-17, 6.790375847387171e-20)`;
- independent maximal-face-fan centroid `(-7.820351463900388e-17, 1.813748979036169e-17, -5.043528675815619e-19)`;
- centroid disagreement `5.835143996530528e-17`;
- centered first-moment norm `1.5582740317092444e-18`;
- minimum inactive P-plane slack `9.252804033643008e-8`;
- maximum incident-plane residual `4.440892098500626e-16`;
- centered-Q minimum nonincident geometric slack `1.361338314087579e-5` versus incident residual `1.4210854715202004e-14`.

Thus the saved incidence is not comparable to numerical residual: the P inactive reserve is over `2×10^8` times the maximum incident residual. The closest complete feature sign wall is about `6.19e-8`, still over `10^8` times that residual. B210 is a genuine open non-target cell, not a D198-style merged wall.

### Equilibria of P at its own centroid

The exhaustive class is

`(S,U,H) = (2,1,1)`.

Retained targets:

- stable 17-gon `[0,1,...,16]`, margin `+0.9784559770798658`;
- unique unstable vertex `8`, margin `+0.38759050137601264`.

Residual pair:

- stable ten-gon `[18,19,20,22,23,34,43,62,64,65]`, margin `+1.1690217999502671e-5`;
- saddle edge `[50,55]`, coefficient/mechanical margin `+6.88081829592773e-5`, projection parameter `t=0.8764346851281922`, cone coefficients `[6.88081829592773e-5, 1.011524899008996]`, cone residual `2.50e-16`.

Opposite walls and nearest excluded features:

- face `[50,55,61]`: `-6.188257538050145e-8`;
- face `[64,65,66,67]`: `-1.0530504673405187e-5`;
- edge `[55,61]`: `-1.034491296455645e-7`;
- closest non-target vertex `55`: `-1.802537085470837e-6`.

### Dual centered-Q mechanics

The centered support polytope has the polarity-swapped class `(1,2,1)`:

- sole stable face `[3,11,13]`, margin `+0.22669720634202997`;
- target maximum row `3`, margin `+0.999995928676701`;
- residual maximum row `30`, margin `+0.00270290874286185`;
- sole saddle edge `[38,43]`, margin `+5.613488472400084e-5`, `t=0.9999625464283294`.

This locates the surviving Morse pair entirely inside the connected replacement complex while the target dual features remain far from their walls.

## Rebuilt topology path

Every row below has its own raw Q file, centered H/V files, complete maximal-face cycles, true edges, all face/vertex/edge records, integrated centroid, and raw incidence data in `states/` inside the archive.

| state | `(V,E,F,C)` | P class | largest nonbase face | largest nontarget vertex | largest edge | inactive slack |
|---|---:|---:|---:|---:|---:|---:|
| inherited R160 | `(45,80,37,160)` | `(2,1,1)` | `1.92487e-7` | negative | `2.69025e-7` | `9.87302e-9` |
| S114 whole-basin deletion | `(28,57,31,114)` | `(2,1,1)` | `1.32549e-3` | `-3.70348e-4` | `2.52991e-3` | `8.01581e-14` |
| R208 connected ribbon | `(65,104,41,208)` | `(2,1,1)` | `3.50473e-6` | `-3.65846e-4` | `9.71631e-4` | `2.04288e-8` |
| B210 initial open cell | `(68,105,39,210)` | `(2,1,1)` | `2.35351e-5` | `-3.57096e-4` | `8.63391e-5` | `9.25561e-8` |
| **B210 primary** | `(68,105,39,210)` | `(2,1,1)` | `1.16902e-5` | `-1.80254e-6` | `6.88082e-5` | `9.25280e-8` |
| X208 split cell | `(67,104,39,208)` | `(3,2,3)` | `2.30572e-5` | `3.31551e-5` | `3.86654e-5` | `9.26775e-8` |
| X216 double-pair cell | `(71,108,39,216)` | `(3,1,2)` | `2.67824e-5` | `-2.10534e-4` | `4.47762e-5` | `1.10779e-7` |
| T216 post-crossing relay | `(71,108,39,216)` | `(2,1,1)` | `1.27258e-6` | `-6.57333e-4` | `6.17629e-3` | `1.12465e-7` |
| A154 radial-ascent diagnostic | `(50,77,29,154)` | `(3,9,10)` | `6.37892e-3` | `2.19679e-1` | `2.82233e-1` | `1.61171e-9` |
| D198 serial-wall comparator | `(58,99,43,198)` | `(2,1,1)` | `1.34439e-9` | negative | `1.19466e-7` | `1.95399e-14` |

The deletion-only S114 and D198 states are rejected as certificates because inactive separation is comparable to incidence residual. The R208/B210/X208/X216/T216 states are actual open cells under the strict `1e-12` reconstruction.

## Why the simultaneous basin replacement still transfers the pair

The failure has two independently materialized sides.

### 1. Moment-small connected sheets relay an Euler-neutral block

B210 keeps the raw polar centroid displacement near `1.64e-5`, so the target base and vertex survive recentering. But the residual basin is then a local Euler-neutral complex. In the X216 cell, centered Q has residual maxima at rows `30` and `43` and saddle edges `[38,43]` and `[41,43]`. A computed rank-four local solve drove all four labeled margins through zero simultaneously. After rebuilding the **entire** hull—not preserving stale labels—the T216 state returned to `(2,1,1)`:

- residual maximum moved from row `30/43` to row `31`;
- residual saddle moved from `[38,43]` and `[41,43]` to `[38,41]`;
- on P the surviving saddle became `[54,68]` with much larger margin `0.006176290332687803`.

So the signs did cross; the failure was not an optimizer stopping before the wall. The global circuit changed and the pair reappeared on the adjacent cell.

### 2. A genuine cancellation at the reference origin has a macroscopic centroid cost

For a Q vertex `q_i=r_i u_i` not to be a local radial maximum, at least one incident successor must satisfy

`q_i·(q_{i+1}-q_i)>0`, equivalently `r_{i+1} cos(theta_i)>r_i`.

Along an `m`-edge ascent,

`r_end/r_start > ∏ sec(theta_i)`.

Here the residual south radius is approximately `231.2159516`, target row 3 has radius `358.0892315`, their ratio is `1.5487220`, and direct angular separation is `3.1374467` radians. Equal-angle chains need at least twelve edges: eleven require a factor about `1.574026`, while twelve require about `1.514232`.

The saved A154 construction realizes a twelve-link active ascent. Before own-centroid correction its raw Q is genuinely `(1,1,0)` relative to the reference origin, with no saddle and every new chain row extreme. But its polar centroid is

`(0.0068488977, 0.5504090132, 0.0008581601)`, norm `0.5504522919`.

After the mandatory projective/Santaló correction, the centered Q becomes `(9,3,10)` and its own-centroid polar P becomes `(3,9,10)`. The high-radius chain removes the pair mechanically only by placing close polar planes across a macroscopic angular sector, which shifts too much volume to preserve the target own-centroid chamber.

This distinguishes the present failure from the previously exhausted serial rails. Here the complete old basin was removed, all fourteen replacements were simultaneously active and connected, and real multi-feature circuits were crossed. The obstruction observed is the tension between **radial ascent needed for unique dual maximum** and **small first moment needed for own-centroid mechanics**; within moment-small sheets, the pair is relayed rather than annihilated.

## Independent verification

From the extracted archive:

```bash
python independent_verify.py B210_full_basin_centered_P.csv --plane-tol 1e-12 --json check_P.json
python verify_polar_pair.py --json check_polar.json
python B210_generator.py --prefix regenerated
```

`verify_polar_pair.py` independently checks origin interiority of Q, reconstructs `Q°`, integrates its centroid, applies the exact projective centering gauge, verifies all fourteen inserted rows are extreme, compares generated and reference V sets, audits P and centered Q, and checks the dual equilibrium counts. Its recorded checks include:

- generated/reference Hausdorff error `0.0`;
- 39 active H rows = 39 maximal P faces;
- maximum H violation `1.11e-15`;
- dual count check `true`;
- all inserted rows `30..43` extreme `true`.

## Limits and uncertainty

This is strong numerical/combinatorial evidence against the tested simultaneous-ribbon and radial-ascent architectures, **not** a proof that every P2 basin replacement is impossible. B210 is specified by finite decimal coordinates and independently audited with large residual-to-tolerance ratios, but I did not produce an exact rational or interval certificate because it is a nonwinner. Consequently there is no target `(1,1,0)` common margin or target perturbation radius to report. The D198 wall remains rejected rather than being promoted by tolerance choice.

## Most useful continuation

The next nonredundant P2 experiment should replace B210’s **new** residual sub-basin—not append to it. Simultaneously delete the residual trunk/one-ring containing rows approximately `{30,31,33,34,37,38,39,41,43}` and construct a branched annular ascent complex with at least twelve radial-ascent steps, but with its positive and negative first moments cancelling **inside the same connected complex**. The three Santaló/centroid equations should be imposed as hard constraints at every circuit branch; obsolete rows may deactivate and then must be removed from the final H set. The gate should require, throughout:

- the 17-gonal P base and north vertex 8 remain the target features;
- every surviving inserted support is extreme;
- P inactive slack above `1e-7` and centered-Q nonincidence above `1e-5`;
- no residual Q maximum or saddle after full hull rebuild;
- no reliance on a separate antipodal counter-bridge, which was observed to deactivate the target face or create a new transfer block.

That architecture directly addresses both quantified failures above: it supplies the necessary radial witness length while internalizing moment closure instead of repairing it after the mechanical cancellation.
