# figure-0421

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Raven 11 — measured signed-capacity families, a uniform two-U obstruction, and two exact C454 nonwinners

Branch: `[internal-source-reference]`.

**No own110/weak000 successor was obtained.** The substantive new results are an executed **13-dimensional signed stress-capacity family with true E≤306**, a different executed **13-dimensional family with E≤304**, a **continuous two-U exclusion over the entire first capacity polytope and explicit metric regions**, and two exact **V89/E227/F140, own(5,16,19)/weak000** contact-stratum bodies. The latter genuinely reduce the original physical radial persistence, but fragment it into additional peaks and substantially worsen the polar landscape. They are not near-winner claims based on angular residuals.

All new exact claims below were reconstructed in a fresh source-only directory. The final replay matched **31 exact output hashes**. The inherited canonical own110 remains C622, V176/E311/F137.

## 1. Source authority and execution boundary

The literal parents are `figure-0414`, SHA-256 `6837898e4ebf09d5d8228ac8e1de77cc6eff6a2921842bd07360200d99148e00`, and `figure-0419`, SHA-256 `51279e4c288187ef00ba5a828f7d83998e750a9a800e1c6351ad36404b02e0aa`. The latter’s previously expected midpoint markers are now replaced by actual execution results, not retrospectively treated as previously observed results.

The unchanged geometric input is the complete 53-point/grid10000 C306 table with its 102 oriented triangles: `farthest_merged_G10000.json`, 2051 bytes, SHA-256 `89599e0825f7075c151639b70d9db5959fcdc058c0be555d1a96d8598ccdea3e`. Its literal rows, rather than any C318 alias, define the starting solid. :contentReference[oaicite:0]{index=0}

The updated 1546-line journal and the required literal parent payloads were available in full. No additional research archive or connector was used. The old continuation’s unavailable optimizer receipts remain unavailable; the finite campaigns reported here are fresh, separately preserved executions.

## 2. Evaluated architecture costs: the requested 13D extension fits

For an original interior cap edge e, let `c_e=1+2d_e`, where d_e is its number of proper crossings with original interior edges of the opposite cap. These are topological costs, not curvature coefficients.

The measured costs on the complete SIGNED13 support are:

| Cap | Edge: exact cost |
|---|---|
| Upper | 1–14:7; 2–14:9; 28–47:5; 47–52:3 |
| Lower | 0–3:1; 0–5:1; 1–4:3; 1–5:1; 3–6:1; 3–12:9; 3–28:9; 3–36:17; 3–48:27; 4–5:9; 5–48:31; 36–48:15; 47–48:1; 48–50:3; 48–52:1 |

Thus the formerly unevaluated quantities are exactly `u=9, v=1, w=3`. The old formulas give **E17=288 and E18=305**. The extra edge1–5 costs1, so **E19=306≤310**. This extension was constructed and used, not merely proposed.

The actual open maximal complexes and exact identity-metric interior censuses are:

| Family | Shape dimension | Actual V/E/F | Strict midpoint S/U/H | Weak-only | Common centered physical denominator bits |
|---|---:|---:|---:|---:|---:|
| LOWER17_DIM11 | 11 | 115/288/175 | 14/2/14 | 000 | 1389 |
| LOWER18_DIM12 | 12 | 123/305/184 | 14/3/15 | 000 | 1531 |
| SIGNED13 | 13 | 123/306/185 | 12/3/13 | 000 | 1534 |
| SWAP13 | 13 | 122/304/184 | 7/3/8 | 000 | 1570 |

The first three midpoint parameters are respectively five bridge coordinates1/2 followed by lower coordinates1/7,1/8,1/9. SWAP13 uses four bridge coordinates1/2 followed by nine coordinates1/10. Their positive centered integration tetrahedron counts are226,242,242,240; these are not their maximal-face counts.

### Complete SIGNED13 parameter order

The following order is used by every literal parameter vector in this handoff:

    0 upper: [(1,14)]
    1 upper: [(2,14)]
    2 upper: [(28,47)]
    3 upper: [(47,52)]
    4 lower: [(1,4)]
    5 lower: [(0,3),(3,6),(3,12)]
    6 lower: [(36,48),(47,48),(48,50)]
    7 lower: [(0,3),(3,6),(3,28)]
    8 lower: [(36,48),(47,48),(48,52)]
    9 lower: [(0,3),(3,6),(3,48),(47,48),(48,50)]
    10 lower: [(0,5),(4,5),(5,48),(47,48),(48,50)]
    11 lower: [(0,3),(3,6),(3,36)]
    12 lower: [(1,5),(4,5),(5,48),(47,48),(48,50)]

Each field is reconstructed by the exact parent nullspace, positive orientation, and maximum-fraction normalization. The complete admissible domain is **0≤Rt≤1 with signed t**, where the regenerated19×13 rational R has full column rank. It is not a13-cube, and it is not restricted to the safe positive simplex.

There are exactly six independent stress equations, two at each lower interior node3,5,48. The13 fields span the full19−6-dimensional supported stress kernel. By the parent completeness theorem, the capacity inequalities are sufficient as well as necessary for convex fixed-z, fixed-width chord translation on this support. Contact boundaries can remove creases and crossing vertices but cannot create features outside it. Consequently **the entire closed capacity polytope has true E≤306**, including every saturated stratum and every nonsingular affine image.

All these bodies have constant physical volume

`1690203202641/1000000000000`.

Before final translation to0, their actual uniform-volume centroid is

`(409355912737/135216256211280000, 855529297349/67608128105640000, 5154137003/270432512422560)`.

This is enforced by subtracting the exact fibre-volume-weighted mean of the chord displacement. The volume and full first-moment polynomial, including cross terms, are checked. Only the two longitudinal affine shear coefficients per mode are rounded to denominator2^20; vertices are not independently rounded.

**Gauge warning:** the regression gauge depends on the constructed open complex. Independently built families therefore have different gauges. Corresponding support strata can have the same affine orbits without using the same numerical metric coordinates. The next theorem is pinned to the serialized SIGNED13 gauge.

## 3. New continuum obstruction: the entire signed13 capacity retains two U over explicit metric regions

Let `p_i(t)` be the centered SIGNED13 points in its fixed2^20 shear gauge, and apply a row-vector affine map `p→pL`. Write `G=LLᵀ`.

**Theorem.** Throughout the entire closed signed capacity `0≤Rt≤1`, original C306 vertices0 and14 remain two distinct strict unstable vertices at the actual uniformly filled centroid for every positive-definite G with

`condition_number(G) ≤ 1173/827`.

Equivalently, all affine maps with

`condition_number(L) ≤ sqrt(1173/827) ≈ 1.1909574659`

are excluded as own110 in this fixed gauged family. The statement includes every metric orientation and arbitrary overall scale.

A second certified region is the aligned box

`G33=1`,

`|G11−1|, |G22−1|, |G12|, |G13|, |G23| ≤11/100`.

This entire box is positive definite by strict diagonal dominance. For both nominated vertices and every other generated point, the escaping-dot primitive is **<−1/1000** throughout the box and full shape capacity. The largest exact upper bound is approximately−0.0010303717812715793. The box and spectral region should be retained with their separate scopes.

This is not a finite-search failure, a small parameter box around one shape, or a claim about all affine metrics. It excludes a continuous13-dimensional physical capacity times a metric region, including all its exact contact strata.

### Proof and exact certificate

The original poles are generated point labels7 and36, checked against the literal original input0 and14. Their horizontal coordinates are fixed, while every height is affine in t.

For each pole i, bound its height and all122 differences `z_j−z_i` over the **full** capacity. Eight literal nonsingular13-row bases of R provide exact bounds. For a linear functional `a·t`, choose one such basis B and solve

`η=(R_Bᵀ)⁻¹a`.

Then

`a·t=Σ η_e λ_e ≤Σ max(η_e,0)`

because each selected fraction lies in[0,1]. Take the minimum of these eight valid bounds; apply the same construction to−a for the lower bound. The inverse identities and exact stationarity are checked rationally. The eight bases need not enumerate capacity vertices or solve every linear program optimally.

There are492 linear functionals and3936 exact basis-bound checks. For each of244 ordered pole/other-point pairs, the resulting rectangle for `z=z_i` and `d_z=z_j−z_i` bounds

`F0=x_i d_x+y_i d_y+z d_z`.

Its five metric-perturbation coefficients are

`x_i d_x`, `y_i d_y`, `x_i d_y+y_i d_x`, `x_i d_z+z d_x`, `y_i d_z+z d_y`.

The metric-box expression is multi-affine in z,d_z and the five metric entries. Checking its four rectangle corners with the exact coefficient absolute-value bound proves every escaping dot is<−1/1000. All976 corner tests pass.

For the spectral result, the same rectangles give an upper bound F0<0 and an upper bound B for `|p_i|²|p_j−p_i|²`. Every pair satisfies the exact integer inequality

`1000² F0² >173² B`.

Hence its Euclidean escaping cosine is uniformly<−173/1000. For `p=p_i`, `d=p_j−p_i`, the symmetric matrix `(pdᵀ+dpᵀ)/2` has eigenvalues `(p·d±|p||d|)/2` and0. If G has eigenvalues in[m,κm],

`pᵀGd ≤ (m/2)[(κ+1)p·d+(κ−1)|p||d|]`.

Forκ=1173/827, `(κ−1)/(κ+1)=173/1000`, so this is strictly negative. Both poles therefore remain exposed strict U against every other generating point, even when other points or faces coalesce. The centroid used here is the actual filled centroid fixed by the exact mass identity.

The primary checker is `trap_basis.py`,5746bytes,SHA-256 `efd121ef8e43d2df7453a9a1e1dd8b6cae15ae7eb4c1e20e00046b30da632051`. Its483461-byte exact proof output has SHA-256 `f7f6655bce0f58debb15d03ef7c7d346993ae27cfd9460e4b7cd7ca3c47a17ab`. Optional discovery actually solved492 numerical linear programs and nominated the eight bases; pure exact replay needs neither SciPy nor that discovery output because all bases are literal in the checker.

**Scope boundary:** the theorem does not exclude larger-condition affine maps, SWAP13’s differently gauged/new support, other64D stress supports, another projection, changed fibre widths, or arbitrary physical surgery. It must not be transferred to another family merely because some of its rays have the same names.

## 4. Two exact saturated signed bodies: C454, own(5,16,19)/weak000

The retained bodies are **SAT_SIGNED_SIMPLE** and **SAT_SIGNED_NEAR**. Both have

**V89/E227/F140,C454; strict(S,U,H)=(5,16,19); additional weak000; exact actual centroid0; volume1690203202641/10^12.**

Their maximal facets are110 triangles,26 quadrilaterals and4 pentagons. There are174 positive centered integration tetrahedra. Their common centered physical denominators have1023 and1038bits respectively.

### Complete literal definitions

Use the SIGNED13 mode order above and its exact2^20 gauged constructor. Set

`r=3487819549104654454/7458006485348347165`,

`t=[1,1,1,a,0,1,−r*b,0,b,1,0,1,0]`.

For SIMPLE, `a=3/5`, `b=1/64`. For NEAR, `a=594141/10^6`, `b=15939/10^6`.

After subtracting the exact actual centroid, multiply row vectors by

    A=1046495/10^6
    B=1885792/10^6
    L=[[A,0,0],
       [87169/10^6,B,0],
       [353907/10^6,-544575/10^6,1/(A*B)]]

The determinant is exactly1. These rational constants define the bodies without any optimizer replay, exponential evaluation, or coordinate rounding.

The negative sixth-index coefficient is essential. It makes `λ_(36,48)=0` exactly while other capacities reach0 or1. These are genuine signed contact strata outside the nonnegative ray cone. The maximal complex was rebuilt exactly at the saturated parameters; the open123/306/185 complex was not reused as a boundary census.

Both bodies have the following strict labels in their generated ordering:

    S=[2,10,26,133,134]
    U=[7,10,11,12,26,28,38,39,40,56,59,61,63,68,72,84]
    H=[[5,7],[7,40],[9,10],[10,28],[11,12],[11,84],
       [13,72],[26,28],[26,68],[38,39],[38,63],[39,40],
       [48,52],[56,59],[59,61],[61,63],[67,72],[72,78],[84,85]]

All weak-only lists are empty. Original poles0 and14 map to new points5 and27 and are no longer unstable: in SIMPLE they have positive escapes to points10 and12, approximately0.0214252 and0.0410281. This is removal of the old carriers **with replacement peaks**, not net cancellation. The physical global root is28 and the polar global root is2.

### Full physical and polar basin evidence

The new diagnostic uses true-edge squared-radius superlevel persistence with the elder rule: a component’s peak dies when it first joins a component with an older/higher peak. Every positive bar has an exact attaining path and a separating strict-superlevel cut. This avoids repeatedly charging a shared deep rootward barrier to several younger peaks. The inherited auditor’s root-reaching diagnostics are also retained, explicitly as a different statistic.

Decimals below are displays of regenerated exact rational quantities at the same physical volume:

| Quantity | Original C306 | SIMPLE | NEAR |
|---|---:|---:|---:|
| Number of positive physical bars |1|15|15|
| Largest physical squared-radius bar |1.5563144368785482|0.1076384598453290|0.1076382011864727|
| Sum of physical bars |1.5563144368785482|0.3089536240323436|0.3089536247550934|
| Number of positive polar bars |0|4|4|
| Sum of same-center polar bars |0|7.944992096779238|7.944995022463345|

Exact comparisons prove SIMPLE’s largest physical bar is less than7/100 of the original and its total physical persistence is less than21/100 of the original. Thus the principal physical barrier falls by more than93% and the sum by more than79%; the actual ratio of sums is approximately0.1985162. This is substantial physical basin change, unlike the earlier C328 angular-only improvement. It nevertheless creates15 secondary physical peaks and four secondary polar peaks, so it does not solve either complete landscape.

With R the global physical circumradius, the largest normalized bar lies in `(50360510239,50360510240)/10^12` for SIMPLE, versus `(760514941676,760514941677)/10^12` for C306. These use **global-radius normalization**, not the earlier C328 birth-radius normalization.

SIMPLE’s exact true-edge cosine bottlenecks lie in

`(−259670015,−259670014)/10^9` physically, and

`(−862544008,−862544007)/10^9` on the same-center polar.

Both remain negative. Its largest physical bar is born at peak7 and merges across edge5–7. The full paths, cuts and all remaining bars on both sides are regenerated in the capsule.

The change is not uniform shrinking: volume is exactly fixed and detL=1. SIMPLE has `r_in²/R²≈0.03950108` and `V²/R^6≈0.29258077`, compared with approximately0.09235570 and0.33335660 for C306.

Both C454 bodies passed the full integer maximal-complex/own-centroid/strict-and-weak audit and a separate Fraction feature census. Independently coded projected divergence integrations on all three coordinate axes agree with the tetrahedral volume and zero first moments. No primitive-zero000 assertion or new winner’s independent acceptance is added.

## 5. A different support redesign was also constructed and searched

**SWAP13** removes upper bridge2–14, cost9, and adds the positive lower seven-edge ray

`[(0,3),(3,5),(3,6),(4,5),(5,48),(47,48),(48,50)]`.

Only original edge3–5 is new, costing7. It joins the existing lower3–48–5 network. The complete supported stress dimension remains13, while the true open complex becomes **122/304/184**. The closed signed capacity has E≤304. The exact positive-ray reconstruction, full-rank capacity, actual mass and midpoint own(7,3,8)/weak000 all passed.

Its mode order is SIGNED13 with mode1 removed and the new seven-edge ray appended. This is a genuinely changed support family, not a subdivision diagonal or a relabeling. Sixteen joint shape/metric endpoints were computed on it; none nominated SU11. The SIGNED13 metric obstruction is not silently transferred to this new family.

## 6. Observed finite searches and their limitations

The complete numerical method and all nondefaults are included in the source capsule. Exact bodies above are defined by literal rationals, not numerical trajectories.

The main method optimizes the sum of physical elder-rule true-edge bars divided by `V^(2/3)`, plus a weighted sum of same-center polar bars multiplied by `V^(2/3)`. Analytic derivatives include the actual affine vertex, normal, height and metric changes. Since the chart fixes actual filled mass exactly, no arbitrary center is substituted. An SVD coordinate whitening changes only the linear coordinates of the full signed capacity.

For SIGNED13, **72 complete18-variable SLSQP endpoints** were obtained:

| Polar weight | Completed starts | Total function evaluations | Total iterations |
|---:|---:|---:|---:|
|0|16|1723|1471|
|1|16|1700|1454|
|10|16|1981|1398|
|100|16|2135|1690|
|1000|8|1449|811|

All72 endpoints satisfy capacity constraints to1e−9;71 report optimizer success. None nominates numerical SU11. Seed190926113, capacity margin10^−6, ftol10^−11, metric log bounds[−2,2] for two diagonals and[−3,3] for three off-diagonals were used. Iteration limits were800 for the first four weights and600 for weight1000. Initialization mixes repeated near-zero/midpoint controls and80-step signed-capacity hit-and-run controls; these are not72 independent random initial points.

Physical-only descent produced major persistence reduction but many small peaks. The exact C454 controls preserve that meaningful outcome without claiming class improvement. Higher polar weights retained fewer polar defects but did not obtain complete cancellation.

A separate positive-polar-escape guarded campaign requested eight starts but completed **only two**, numerical S1/U5 and S1/U3, with guard violations about−2.64e−15 and−1.70e−14. The third start raised `ValueError: Origin not interior` on an infeasible SLSQP trial. It is not an eight-start negative result. Both completed metric conditions were inside the newly proved spectral region, which explains their persistent second U within that region—not all possible monostable affine components.

A contact-oriented numerical screen evaluated **475136 combinations**:232 nominal lower-capacity vertices ×32 bridge corners ×64 metrics. It found no numerical U1, minimum U2, and two numerical S1/U2 cases. The232 vertices were nominated numerically, not proved to be a complete exact vertex list. Polar planes were grouped at ten decimal places and the nominal physical graph could retain subdivisions at contacts. Consequently this is finite scout evidence only, not an exact boundary census or capacity exclusion. The64 metrics were identity plus63 Gaussian controls, not a bounded continuous metric cover.

For SWAP13, eight starts each at weights0 and1000, seed190926213, maxiter600, all completed and were capacity-valid to1e−9. There was no SU11 nomination. The complete endpoint histograms, source hashes, seeds, options and interruption record are in the10573-byte `FINITE_RECEIPTS.json`, SHA-256 `4e7b9249ae60ecaeda311bd63ea0aa305a20bbdfc73a594c7193db9ac5ca213b`.

These finite campaigns exclude no additional continuous family. In particular, repeated small numerical losses, solver success flags and approximate contact counts are not acceptance evidence.

## 7. Useful continuation after these results

The near-conformal region of the complete SIGNED13 capacity is now genuinely excluded, rather than merely unsuccessfully sampled. A continuation in this fixed gauge must leave the certified metric regions while finding a compatible monostable polar chamber, or change the support/projection enough to invalidate the two-pole bounds. Saturated signed contacts are usable: the exact C454 bodies demonstrate both old pole carriers can be removed, but the replacement physical and polar peaks must be handled together.

The3–5 support swap is already constructed and finitely searched; it should not be described as an unperformed next step. The eight-basis interval method supplies an inexpensive exact architecture test for further supports: determine whether the full admissible field can change the complete pole escape intervals before investing in another local optimizer. Width-changing surgery remains outside this theorem and distinct from the coordinator’s parallel work.

## 8. Self-contained recovery, actual markers and identities

The decoder below restores **all16 complete source/input/manifest units**. It embeds the literal C306 coordinates and facets, both parent-dependent constructors, the new signed and swapped constructors, all numerical producers and nondefaults, the eight exact proof bases, both exact C454 definitions, independent mass checks, controls and31 expected output hashes. No parent download, sandbox coordinate file or optimizer replay is needed for exact reconstruction.

Executed exact environment: **CPython3.13.5, standard library, assertions enabled**. Numerical environment: NumPy2.3.5, SciPy1.17.0, `OPENBLAS_NUM_THREADS=1`.

Save as `RECOVER_SIGNED_QR11.py`, then run:

    python -B -S RECOVER_SIGNED_QR11.py
    python -B -S QR11_SIGNED_SOURCE/REPLAY_SIGNED_QR11.py

The fresh decoded-directory replay actually ended with:

    QR11_SIGNED_COMPLETE_SOURCE_RECOVERY_PASS 16
    QR11_LOWER_FACE_SOURCE_AND_FULL_MIDPOINT_CENSUSES_PASS
    SIGNED13_EXACT_MIDPOINT_PASS 123 306 185 [12, 3, 13] [0, 0, 0]
    SWAP13_EXACT_FULL_CENSUS_PASS 122 304 184 [7, 3, 8] [0, 0, 0]
    SIGNED13_EIGHT_BASES_FULL_CAPACITY_TWO_U_PROOF_PASS 492 244
    SATURATED_SIGNED_EXACT_NONWINNER_PASS SAT_SIGNED_SIMPLE 89 227 140 [5, 16, 19] [0, 0, 0]
    SATURATED_SIGNED_EXACT_NONWINNER_PASS SAT_SIGNED_NEAR 89 227 140 [5, 16, 19] [0, 0, 0]
    SIGNED_EXACT_EQUAL_VOLUME_PERSISTENCE_COMPARISON_PASS
    SIGNED_QR11_EXACT_TETRA_PRISM_AND_REVERSE_CONTROLS_PASS
    QR11_SIGNED_EXACT_SOURCE_ONLY_COLD_PASS 31

The proof marker additionally prints its numerical bound displays and `G_condition<=1173/827`; the complete log is preserved. Controls include tetrahedron strict446/weak000, prism strict446/weak123, and reversed-orientation rejection.

Optional numerical replay:

    OPENBLAS_NUM_THREADS=1 python QR11_SIGNED_SOURCE/REPLAY_SIGNED_QR11.py --numerical

The numerical campaigns were actually executed, but numerical cold bitwise reproducibility is not claimed across platforms. The driver preserves the guard run’s possible nonzero return code instead of concealing its interruption.

Principal exact output identities:

| Output | Bytes | SHA-256 |
|---|---:|---|
| SIGNED13_FAMILY.json |292620|`e2c8783794431f39a5fcbf25c370eb6d21307880d23dea3f533d324af70d6dc8`|
| SWAP13_FAMILY.json |325205|`0d5af7b7683a8d3a191b65bd5fda910ff856ff36ab448006d0882776d26ed07c`|
| SIGNED13_UNIFORM_TWO_U_PROOF.json |483461|`f7f6655bce0f58debb15d03ef7c7d346993ae27cfd9460e4b7cd7ca3c47a17ab`|
| SAT_SIGNED_SIMPLE_EXACT.json |157999|`2f858c864c8d5031c7b6fa8ed7e8e65529257e79ef19c9d13738089f664eb93e`|
| SAT_SIGNED_SIMPLE_AUDIT.json |4315|`cee87471ecabc6a5a755647d7a88a5610731e1f154436412d74c5ae47f491f57`|
| SAT_SIGNED_NEAR_EXACT.json |159203|`e0a19e15ec99db36605440634719a7849b7f5f394a86ddcc42f7b3ce2a9cb72a`|
| SAT_SIGNED_NEAR_AUDIT.json |4315|`b8d677ba48045d874bf500379fb3b0416299e6c65095cc7f550a9fad115ef7ba`|
| SIGNED_EXACT_COMPARISON.json |72060|`2b3a8645719be2fa192e327c43d2ead7e41d10055dc3da580e79f91f6f1268b2`|

The normalized base64 below has33852 characters, SHA-256 `f630ee7ecfd8cf62a3e10d88f1e1446c335332ed009def1c28e267a8e5fb658e`; its XZ has25388bytes, SHA-256 `52b6ebadca2404ab5bf62f5a98c87ccc934391f299553e4953ac182ffb97a722`; decoded JSON has91383bytes, SHA-256 `8023d29ace62bd789be58fe5920376b18f8e52185f3cb6f38c232884799d2e3f`. Each restored file is separately checked.

Supplemental [executed source, exact outputs and finite-search receipts](sandbox:/mnt/data/QR11_SIGNED_CONSTRUCTION_AND_TWO_U_PROOF.zip):1314374bytes, SHA-256 `7caa754e2bb8874cd09f922ca7a054a161f1d528424b2a7d977a650023ee8b73`. The archive is optional; the complete recovery closure follows.

```python
# Complete self-contained source/input recovery for QR11 signed continuation.
import base64,hashlib,json,lzma,pathlib,sys
DATA="""
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4WT2YuldAD2IiMbUDKr8M96sXyRJUTg4MkQRjovqWRNBvF+MXY1/BKIvR/BBEBoN8Jue
u5ZUCVe8T+o6OMZkYnsLwpLoVMFoBTTx1+BACknN1ztnzcD11u5txvp4KvXBcEnXYvyPDvpp/HDiMT8ROXXCkZ/nDlumCYRolAsd
8q/vqFCiSgxPPc1pkCNaGi2aRSoPWtafz5yxfGJEL1R2UEe9fyZIj29HQEzwBhEhrgZ2IofBILGfHZ6TTuw4A01klPVUJRMXaR4Z
yFByvgMD7S4jug23vmhuVf7GLym6Nm/4rOJsrivCBG1Fhy+ed2gBNwD07mDQr6r6/7Nwxc03VvML6BLTLDJInHxC2D30MN9uPcTY
0FyD0Z683QrhWo/6J5ZTIdZRy3Qbh9qLsnxSOlApokW7JPvmE3R0LQCwssPBSdQ9uQNJgOje2Mqd7Q6eyuS+gf2sUg6UsGk6ZoA0
hakUV5C95Qd/+E+d/ut6B+vi94bXWo/k3cgC2BBGwKPLJvcSGCecY7vG1peGd0nwENAmdexOBdieW/erqu8BN3GyeVArEotF/rFV
JvAKfzbd0KhzJKoGW6lM/oNsRKIniiKU9R65eVsn66FIuKUnI5c8MP2bIThThH4u2D0WjEk5+tW66nNjfS9TxD10CBg6DjOAN/oA
1/mQu8oa3Y+hKecC0fckqWQqbLgvNtcliHfNJvirR+AS1v07FaK4f63lzmAkCBju7yMmGCo6JEL3k6o6nHW6lrQZ7on8EN9hDcGw
IeEO90qQk7WmAxVltT8+GBscI2DC/sjFLpb/aY9qEtrfDMs4y+cZNbsr5evAHDWyOK8/FPc9wlbL2Jl6AOWybh1C6x5JApMH1pQm
03yR4qgr5zWO+PAa9ahkL9GdCFw8egwmrG4FCJZJaJZBRwNYkKC9fE3wODk3Of2b+3HqE3BTG/LRofGGq6eT/31PxgY5EZfiI03r
htpniqLotoYT7RxrD4gWdANFrnCNHUhw+XSzKKn4+IbfAFnMkahQ0GaAYWZ0oL5lBTKJLxeubcHBs+7txM9PSscJIiAAjI0TlWHc
7OJroBpdIatxVWSc8BvhhyDo98Qbgqn+Qtt6qXrSkqAcIU8F4SGTZKMROChzTvXttYap8BKu1xDxb8P8eakkkHCw+q0aWcQu8pdk
tv691ARtO94PRN8NfFg5jil7tNTwWXt5N3QZ8s0TGm31gjw4/pi8o1EBt3lUj87N8wvAoG74g2Bm9aiqOjRrA5380xDeMzJI5Br7
Yp/WA++gL89fmQaXYK0pHkSLyFHYo5l3n3W6yk6naXqfvWxyn7jcqpNdSmHmo53cgJCWTmZ66B0pXMbmWxijgz0KszQkIHq3dKqS
vDOsV3UrKU8r388VAzCMAUBsZEpyi+rOzc5YWIdIAVTkHDBb1zBDbGzD6suzL2gwj7qwTga79g4esQmme4p2EtAl3AH3XMm6jylD
gWqgRrM/JFtRDrE6eXdosJBh5FUJHRAk22wYmb1T1cNRIrcB9hTSCPWculsWv7qxIm/2Zjg3wdMX4ogG0nlKF0XhjzTsZFPCXSYU
rtfUIIxgFbdwQqyDm6ilaK+jtdE3xUWT5G8Du3AaJ6wKmxoc+fRhHQh50r5TFLpNMjVs4Ki7uvH/4kONWqUoscl46Joekz8kxfYv
+wNWfyzh6PbH2Yjsq8PugmhQSqrsjjgIr5Ogiv+2VUyJ8I+6oxknIVtNbDKlMV2ROr6lb1mOyHUDN6XNJcfx+rTs1Unga7vnuTuq
SaoS4vIB76EctnmsbS6RZXwWJGd+rF1S44Ne33W3TZTbMhgaM3OIOMy+dhZdhZQcwv86zSgcmQnnGD79h37UvGgB+rt4tK+3jD/4
o2g5fMq3MY1eNeQ4JWlb9heB94ovDZK7E40Cvjej/tw3n/H3nBI6PfWnr7hJlcLTGefdAa2M7M3rpynyYfXSfhr9M1ryJcpFjt0R
tZEWjBuKcclkMqAaLrve9dsFSyX1SBW+OH2LJKmtUfS5Dn7KqDWPqfjp2mGdyPCHo7vCaEUtJtsYHoiebn2ORl+Y0FMA9eDUCiXf
wL9rW6cdo6pY/a/Gt77yGTJbM4+jgnt+8dAz74yb2Hx+/cry1KKIeEKAtK2AfXt7I3ZBVXkMpjAO7yaNGJXYk8+lk3Vq7Qpsmx0+
IK1Q8v5MClwLsSgpdXSbRAI834bHCf17XUKuoui3+LB20S8PYBMaNM3iMZDqYa8RVznhRrKv24lYMHn9mfEVzPlMMwXXbPeubuOl
gR/mCr8U07jlC8+fiKMPjXG0btXnrcPMrZO4rDsjnBywTjqJ1tN4ikofSwMU3rkij2Y562t3HFLKG36TJg8ULhWRpCprAB8wldJ+
khGqs8oBexBHh6yIJP5oHT8xE8xVfKJbLghXWskh8VbXZ75C5BborNNl4HJnz/f5KprxCjFt017xO7IZjkJnPC4kjHTkZQjBE+U1
cN+nmYIFIa6DJ6uOZXpRa3e0T92ko0t/34QuR2f2jG8RDOjud9PuZlJnK2AnaBxcblh1ZzaiVUdJxoxnhYR8JxyPi198Z5j2Ti6m
MBxCZqRZSvWH53SyJ5ExCJApiSoxuy1DFmbVkddENpe/VGS+eU3LBCBMLbq3Wyzgispx2EbDk5ij8i/Ydel2eyWr/bjdKK//x46w
qNdaPT9nO7tr3hGDKqG7Xk3KlgcwVXbh8cQUe2tAAVWpdVUCV8D/CsWCY0sZBnhFgldEtoOrPNyo7b6LR1WkJWeY1gUwKa/be04H
6Lm43p6Q46uhsDjm6QBZ3AK//U+o6MA3lrxGbtuMbfUo4oeog9f82flibNSTnOBEfL4QTh8tRESYdzNry+KiJnqT8Fj7pBmBehS4
8RDwl7TWZFVsG1vZ7A7n+Ns80ecSd8WUcFWDjiilOWxc9NUHTrsjT8MRqwxM/xK81RbTU5rG4kfHr2FFDtyceMg+EOnKGzTWBaPt
O2yASjBiCXOhcJW54aGXBL4G1zPZJF6E3amMisQzcY+mRCRVYr0cbctvZY05ZKrbDxPTqZdxFsv92h/e+KbhW2uwXkJ9AnFAZXLa
swLQCqRsCu/i8xA3ELZudr+lDiDHeOTIlMutpDgiRF3dww0d6iMQB/OYZcVnKgIab4J5rrsKSTUFqIK5Pw+DiLCPmTxWRmpyz9g+
E9Tthqb1vNtBuuArx1aX1zdEuRqs1s3W1hjiC2f8EW9vADCLwhBNLzsVPo45jgqkPrmN/4mWSZkuBIyGJee/u/023IAHq+RTFkob
4NFWWmJGjk9/BFFCnqMMXKeM7k7cKuBaumFRc4DhpQa1TKLnS8V2U2WoXorv37s20uQU0jeGcnjK4jgZQSd1+31e9lmT2GFjq+Zx
P5PxcMLVtETu4RSUSwRLrWcM1Q/zCpgDjTqTzdKfBOI5dv3MnDIlWaCGHIPGhkS21zs6/KAYFbmCOCAE97qYNvV+/C1ynf5UXby3
3coe6VbUICQwAIffyM/LtLHJ7d3bfH6edxPR1Cebrrl3RAtoWV1ETHrcf2yS9yjK309u+YCQTcp6+wR3FMnCa0tIEGws2NRCrzIc
89gSh8/SDuzrmNivzXJVHayvh9E2KXUrREl4yeH11LJT6CP7SsG9DwHOs6zc3mkE8CJbMwvis7iLDDShqZaL8/5Es6euCvYuTWad
t80L1+ApwCdwFcnhtXkZr31XRqdUzu7xxKXha66dnZ5EI5xfANtJt9TBlrlPAKvhiRhLTdSXTByDPRl1EtLTXyOVbBAoTWlZk46b
UB9AH1V8sH8XGf+UzfO1hrqi2NIEKDYMPO3ephlqXPC13pB9FvLcZki+47K3cNqTLEuZ7pRFPYImjL56rf6vzRusuC6O9sRtWocz
/a1fa2T3ey5wDeRLqXXnK+NzJW/Yt18LO36zALMQQxVc5SFoCRB44uPd6HnbAnomJ/9lsA+kni6YH44C472el5+RQwHLUPr+QTdv
EQk7DAj48nKq1VhJdj5ECub6Zw5e4nxagUU5RxocKDqSHmkJzfaTq+PewonKRurefJXKSPhBPaPWM9v7w8p+LjqNrtUgp0dJF8iq
C1klrDGF7jx9M+wgJ4lpnjgVV7qSFRU7n1NkOd0UWgQ5rqfF/Psgy/iiVDrn5eH2TcKSxd4YN3OnQsGHMyCTeuEs1FINJjgB251P
Rt8Az8YQ445dWA6TDdTeDFpVhfvYZFRIG1kpbi/lvnhhY1TgXdBZ/deBRFY9IGRyF/UJtjfIziGXtT5wKiAtLIZ1+LhCnYi/9iQu
aEfHSZuyHenbPTLiolWgEgNNEP8NevN2pugnTlqwG4d5I/fhG3J42bkg83g8OUupiVs5Rsh4fcNwfh4WvFr+JgTN/+H0x4c8Eysy
8m+JBpyeL82w/QSlqagedaoKiUWlMhlI5EyR6xou1ALGYgtd4ZTo5SpM1NEurG1gM8DU4A3Oiv2p2NJt8O7e0oUPG11e2cBOZfcx
lcyho1kZiSptlKlUtyCKfMKi/NZvZrUmX6nHlwhWabTmFm8eZjYNpQHowaQkmCB6hlhnPoydfhsfok7nYMEefr1vqy7dQKAPpr5i
GQbSROQpaxeogWkGSZ4Mz3W1GTfXw7Djmn86TdOlurQeCTPaUbKqD+wgNYaFeoa+01NtWJZfTd3V703aqIgvqn6lLurrYIkHUV3u
KZMcfKtIiKNiMrFbfpORAjHZ5jnMWSaF9X8FOSynoyoGodYYoXzdtuS050BwvBRIVU5RuyOtOI91l2QkH7c6EAclEmopbQpKFymG
iGoSnNY7WpKxvnxriJaBzUpZdg/VJtgKNG+r6WcCsCjTQFiZ9xPVQnD85RjsupeD8cV/JcaTG8HAHasDUWiM4ld4KEr85NylUUxs
DRlrJ3nBazvSM2mO7MVyr6BFZNLhseZRydjB+Y0yHCrjtp17NQwTTXWjCTTa/a9oJOGFDkH/qFpX4j5yCH7QV3A+Xfww7aC59BHZ
0W4972C2Y+GtWV++xcDsZokfULHHL5q7zfgIBVs+0R5aGwcQYNjgVFyMB3tPajBgqltqizAejfJZAeK9u/6dTA6NkrKGCi8bD027
Wqa19rT7AlYNtoSKiqxyCYJ9Rk60M0f0PxuCgXIBjyIRMO1m+TIgB86NKS7dDnUxbfw93D3aygd5J3njGBxjG7azRt605KGN3i+z
A3dWsU50QPdMr1YOLV0oLkEACUtvXxkeYQWlIFgcDgRyvFQT2R0tIABgg9yDYINb9V0/ZZaLd+Oek5JYzxrnq2jXe7jJvxeV1Fzb
Iiwwh/Hwwjch37oTpBXtqFPKS82zBC5F+a4Vu2OrfHld1dtMTHcuNhXU+XK6kZnrOhaaQAZcoK+VtFkwmR3IQUCoNMZuQMn2E/Hd
NYbOcW6jE3dJKbWY0ZE9MTcGEIGA0VbPz/TnB+S6MfAuNI4YU0QFoe/Dx4WRPJxZSoD8rttlpc88rn0Uwh8be03Ks6JqUC0WU0iF
6YIZxL6jX4lInkhlFHuWvtMkDqfiDwCUiHdi+vkaitq4NVJ7cKIieFZjQRspzNblMQjhkHFiy+mRbXUKiEqwqXSEZ3sTFdA1tc+M
rdLxFIJjmY4odp7otEBPiGv7mwjxwG5J2J+h8RDs8DNA1xMGDHdRps7wOnugXLSarB1sPxtf74i2rE9GRp2OOTAFevkdz0qAKQxC
Cma/UAdSvJW6/k4TMtw8SjJYeI2/vE3xGIJl64L7AEiyrDok421BRu4RDjTsWECe0eGfDvH83qn3/VVyJrdJviZrlxZ35HRbWvSB
2x0kvSutXdRPlkAJ9WNpdNP3MZse39l5+vS+UVxeujLnqLFoTDHQ8PI1kA7U5Rvp377pbsK38RUbGZkShDP8jJ6tOEmdyKCd+cG/
D/Tfia7i1fOx+iYAynGyOCUy9iY0QTsQIZuH4ugBee46Um/bJZUCBUH2lb9cWpRVUAyKGRIC1gh/uTKv/15D7KVCOPF/ndFFAiVJ
Y1+IRQqr62GjJvcMSgraes+yQlMXuJFNtrlH1HtEmkBX5CQ3qFXQ9JMswNTMtzbts0O7bA1eQnV7esBwp1xBnnbNsL4ASvV9r3Ox
4Cd7pXbwxWRYnsWxk2RCNB9/vqvfJGXnlZ1CfKpL7XNPtqJdf14T8zmMUnF1VxrzOQ8uymWsPXF+hJU7BtUukgBYKbIOZpO23XXW
jQOkf35pTUN7MJlKEDaYScr6kYBlAh3CfjQfLUEFmfPlCdv0V1aKMOgTIeY0+ZKmNleGWv1+KV/7C1/kGmRosyT7Hxt4SmWoH0vl
3zBCozbChd6/geYsDHhFLjpkR85LsKkYpkKpmNs3ePisFUFTlWNqRT2jkhScLdWkTNvlharGGrUuiwnOqRyv94jBZ+OeG3oAHJV7
nq7ISUfd0m5zgzRDd43FgK7A8WZIlFyCtK91Nau6RpeaG/g68BNLBIuGivqUBTsvLqpL27FXmQ4RjiYIJicM40cYhQUx9llD92Ij
pC4rjgiDo61lxIqGWXDL+K54zr+53vfQJufOeBL9ZiNpxmeJWgfL5dSNvW7eL98aQdGVvB/+qttK3O2CXrA9VB6U96C1b7FM9UDd
p98SLOVK/ThMMveKgrFJ3CWVrqC0PznHmCogOT9flzuW+3yiqIo0pNC1a4aN5iqBqlEAfjqdDP+eCOif0e+1hqGYJCqx4AMXGVci
tbbdd6RHCwfY0FwBJLBulBgf3WmVazdXkDcsUiDQq6lzy9Me3vZYl6arH2tMvpKK1Pnou4E1h9n1r6MApuf3FBkDibSY5ZY09C6d
ZzsO/oLsboQedORdpUlnpQE6lx2J3K/VYrreaacNuuLv9a0CRuNHCnzvH375V1jg3pGwaXPXHBrZfQkxVuRJZyUoSvhiIDgXWVdu
uiSQ6RNCWwXk6MwLX9VtCUo2TqlIE/zjVaWJ7Q+a90UDdv4irl8fXYnPjsGqydWApJxKYnfkN2EKC+ndRrthPXXVthejb1bjr76l
JUCrM6EcDSS5z7SOckPKudCLN2/SPl8dkGHlQYEi3wfdFhyT6AKtuBWyvu+ZIBqcxDEechXfg+Yd00XO1NtCsb3va5f/bM3E6+XZ
xv2+64fg9oi7xYn8HTvGOguRxxgrBfzBOYJrP7LYrceesUEirJ+EXob8CqgeOawsdoT3vit4UOzuo/2RGWifvaKWw+QA2lHxnJUh
Q5a1pdpREmb6P9BLA96dPa7fvUOJpwGRTtur20dXjQxCEWI+4ifmswbYbmKMBo5XQf4nI3I17+4AObn2ZCdyvQ5GeHgh83UGwjQA
URYJRm/fTSRXeyk2O0ov/tnaPpnllgWJGJppJkzeBw4kgorwL/iuaSA8Z/yCFWXFx2aDXJ8gD9IMUaBhQ9OTvsIXh7CyJEC84rz0
tlvH7FMsUpW2XM7RRHDGLcHnU9slveXMv+DvIhbWFSfxXKcFplesm3P8wM0aB7Shw2cJdISfQjjgY5RzW6U3z2tALRMVPraCHy8m
JsuXOpnHAkS0yGFu+Oo5fKDu/axNtEsc4cjY0n4zP8OqJDXmwAz1SmWR8En4yj37jvQ6zaL82oLG2meqlabL7YwsCn4fQ7dpkaOV
SDTl2Fl5HzCT8/rpMPT6zmVqRjAG7r0FXxKxPeKfW+z3a6DaPG4Iyr+KZ0mWlR3k/bBpst3YUFLKrj2nX5RAME6HAod7rDuCSyrq
2sTmz4LzNgtXTWAgsq4IagJl1OfQtbWR3BoiuoOLuXJwrZqyKpvBUdSmcLz1Dj0ZCZEF5rczflwQw/U+nE+uR1aSKiXIyp8wIdal
LWw4m0lJ1NrIwm0u5mjOJ3lsKmjruxqjNEzgblFAf3HBHW80SsT8T+f2tNrSo9TgdTYsFMJsEPPrhK9hhidshQdPnybQVPZ5DImT
rBhF+CxND2mKi9RidPS9mTByo5PeOmieOgyh5bqk25Opw30g71LB1yJ3Ziy7oJIrCusmpj2wSAVBw0+uaThameIhVkaLmGCnsW1s
B9ETamK0uZicoHQTyRb0nyoIKd4ja1tEbrJ/n9vIqYvp2JKQibTrpguaYNBpMSMlQhElWvHkgkRcTmfhyqAKJI+btai6Ma6ob9R+
b8WrtyFxtkFDTkXC8XObQTaOAlTwKzm5EZ/imnq60fvGipaep9/HhnPVoNvui4w26Zxm6qgOc3v3icxJ3P345rd3Y7p8BMhMjUaX
vCQmMlxtE/LA2p1cini2mIi0gxrMHrZNt8FjkVwRHhPrr0zBBt/9Zx78FJRBtqca63kVcERFWwzEZXtq+Il6CIzXTZMkb8aDn+HC
dE5/Pb9qNVba5nXklX4luQPBd4i+52pXtxEdrOSrJRoYk7hMKxJxNi4pUBJM3m1Zv4Oz6Uk0qeZSABXQx3u3fRsXpeyJwlKlkqfX
QJ3rLZUQk2JuGhVYjI54+k64huqv8eTxd0jNsBFpDIa0YCxF4Qbwps+uht5g0ecGK4ptgmh3VI2XnsGR+OMFddKi+knRkBuN2nup
wri3bHnDpEF1l/GJLR0NiyQxGlIfk6YLfLXXF6lIozSsOqUPLQraC18glwN9V15UwxXhH6MFHFOZtAoEb6brrSDWxuCIBac4M0oE
e7aCyRuvBwqldO+Nwwserd7RwaqiewZf5EiwxaO8xZD6kkweu/yoWw7z3KJ3xFZtMSH0p/aWYZiauV7y71Q3p6VKjZES3BOOTCd7
2RHxeIngbT7lOZpo55GOoLpGW6UlPCUfTcMCx0CIL/bg66VSCzCP+NGO7oFgDwdhb8SSMiETFEtWSBaAARY+Qsr0NtpbhQdbx7j4
zL4K+OBxONvo5OfZ+xChNdM+mvU4Z8e75iGPh3uvTk75D0Hf9FNtbq5Nih0yPXcJv0/VqNLtRSiMuMBjnoHHVXT2Wmm/jdziHLtC
ZCbdupQlHx675WubSefmL5aKMlQf0PnTvUDpS0j+EYE0nLI+Ak+59ZMovdxzeO4iUBn8P2Z/VUifKhe8rY2xvL15ijmkfp5r5S9k
uXeWyvFr+7j6xN5ScNNYaIHXklhKRk8xpYJxAzA+cNtYH3WhXPJD36mkRBRIzFGItOmZxuj0KJYosI4iCT5drPypKuk/mmqgRUYF
LMIGdcoBvGT1IwaNurmHeFyX8sVkGLUOLypce2mh6agU0ZXHQW9VrAPKk+5frC72zF+sr2N8l2X/6FzbVhkX/aUeSPAmPHwYR+cR
VOty55Dp/l47UwiGYN0OCq2p7sAd2TxDYD6GcPhUOwBr9/jQdZRBxXC+zgC/hi4C/zTsfdfQICGV5dQGirN9mOszUWOn+LsH1Hrd
VL26pVfNwUP1UqXVyKcRPjkDhdFNbyB68JbuO6eXJTXCRd5PPDO5t29XNe0QTeXpwGEBbYjBxaiutHWJsMXnTh5pLK5SSWCZy5Y/
dIreeYRc6i40cGyNinhcaHgP8G6W8D4LUcoWKQ8v6CYB3wsoJXgCkuVGE5cdZLrgFL7kOzO4OkuUckDJcT09spYi5KjkAnyiIqGu
zp1WXch2jwzi2zCIbpCRhtGIJnPXnKISPL8mH5rjohdDC1Kgp1k1LRO6U/rfoIjOTngiJWlRADmAbSqMak3nU9LGepMiPzgb+d6s
7tV1KRhBf7JeXmysfRxtRmLp750DRiTP1fr5BofTQq7vlZAsAmGBK4Kwoo81h5QQIVfMXDJf/8mIAjkI5qJBgIYOz4pXtHwRl5rg
qTpyJ+T59sP4xNTfegCQqfZjdrxMTgfJeJG6aINbVGTdUewL4WX49Y4ks84Y2v7DCN2GIaMZveOeQNkUXNhtKFZKJMy8xB8u9dWh
DuqPOPjX8SQWfBjlpND2J2+VRbV5FufRol1vMy2ZOoOPCXTbFsg73xmaVb4JAHspkG0eWF3wSAluxfkBeMDVLA/Gi2YgcsEnlKYU
0TOyS/lQZGugaKjwSoanyfaK+MxJm9mrCwpQIlOGu64XXVbrlIlIbKd7lJAmgsy8wArvqmX5gYRgJbS7CfQlaKig2+5y+oy2Pnyh
czyMnfUkQjMpgCAPoj9v9RaiPkjtfZBZhuR9MSouBpga56U9pfbnDh6U06PhHMRVsIISW14IIRIIbM7JII+X0fXMtd9O+BCVqfX2
wbr4QkRBqjeqIN1zgBCySKpyVL2rgrgHku6cBJRu8JSUEZ3DM2LtAPTe3gk9TsgOsJlXqpWCvj0FImwBafczMVP3Qwkcc4MQ2G8r
91wfEcavu8eaT5t3ga9b6cvhX+jiuoxkZpxvykv2aT2BwarZBX8E7Movlxx7WZeWzHtv8YRMcvs7grjXCMabN1Z6naIx8aZkwz9x
ujEEtqgT7Ma75ARUtEXRoC02h6+XgZzWc751spgjuix+fR3gpx49Itk4NcTNOYna0/rgEBRNX46B6/aeSZdCGOzN5o6ykKVpawLx
nHb/erPIPHQTnFy9xQMuVPXQwnCKl0XNDFHCENjS98rmJ0p+N71dgZ/0iXrbXdbuzgNSA3c5dIRB66hP+sJzikuq2pIx7pVZLxZo
NaJ/+jo4dv6qYvOTCr1K+FT810a9M1IjnLvOBYEmSZi1TDFrF3b7E8bQOl5xhhFUKdEbgwFTJEPWTtSgnAvxMg70jw7vJYsQfgwo
gzQV2gMtmg6phn/nlSFPiqTCR4i+78QIMyQZiDCg9JwjrCfYtYr1VdnL0WovI+EdWuMVJsTgBK6ID8wZborWHnzB3wnVib98PL8p
qZWLa8y578zfLE53E37knA6hbWw9y9pSzxfTbeF4smV53nVPW8WqCLn5TaDa27JCTtszHDKL1jcxkN4OAMYmLZPRUbbXbgYrY9cO
h9cLl5hTKXQRQF8lPrV+okUyGJP2Qj7gCMLUDcMjxC+nUjLi1Ca22cFdBI1aMoMcV8e/uWmQZVqEQVK+CjuQXhjHNykzfLTFzeHb
jcBkIVT/BmkCwzRBWOJA79pFAe69SkbugORDJ2YMpHZ9XoOwAaeBF9jzgdFsIia0tNRqx86Yr6lObxJYx9XNl8pvRBABeAIJ1tje
rTNVO8wR5IPwSnGJUK9i61QotDCRl5Oup69px052w2uss+RcGtmc23TzxeE+1xDXnY+qmq8Ge59+IX0so8GLNVxHR4k2mRQ+YdfF
BwD12YJRiug2OqQF/MZ9ALB6mqlnayTXbmEvVOTkMFkb4ZGR0296zLNx6HgA12Gl6nAcVTXpolHyQfSWO+17e2ApMH0qgul/EuTd
uM4vmOopxb+wjt+Yd4yAkrccIGK2Ua1UG27wBzeKUwQ4tHBib23o1NQmICraf6JXTHrHP5MB8X/6D1cda3gx+wfCcXKU4kqP7yoM
Mh1FzHVKf+RdZKzwKLn8jd1ZHBU1kmpEs584xLdRt+AwrNKUO09Ug32iTU/KsuBFT9MweZnktffEvE9jq3Fw2cxNR5AtAYPz/wOm
A1GqScv+PHqBw1Y/+jjFzURr+gOxRGjOy9Azs+TdvFUBmc5cqSadpW1W+uGqDAgGoAJIlf6UntMGSJbh+0A4mdBHKvO6vD9GwpE0
bxwTWdY0jw3c+T9ykyIciPTN+YtyQiHf2NgPNgUlKXlxt/l2O+x/0php3w0VMbKaVFXVfu6uFpLvKJeeTdRsYHiIW9tsfent4w2C
d39SM2tUTr0rYL4ylu+uzeVaNW30sjfs7XKO5c/n0i+yf5CbdypPMkDp7c/LeLnOGgT1eNzefcvnaqSSlryRd4gXpf/oQaILVzYv
iNsXbY/2CtjdZfX2Hwb3itV696+VMPI0/lTuu89qzU7ruf1MStV4TynGgh4k4ZrLuPLlZj6te49JlbFRR9eZIiZKR/7C6PQ5QwU4
E+pbcQ9YMCJZWHVdzQ/pdQ/fGs73Qaw8nuAAVGACsy5DgEp46mUYodNVyAt/l0op/VhUfNkuuoanrUIToWbAMaEKBwy5zKyj7Nrz
Fpq/kW6M8d2tCynr7E2/NL+AqNQ3r0LhEUH88Dls4uGPNjG3Zq52QiSPXtPnEPBwzwGHhL8y2k9RoQ9yWMCLq4k+HAKkTpqEaBbi
uutpATLGVJmZnYxjEpCr6RdMIzgLpph/hhaZnucd169gubF7Y3PHT+RGfmn+6Tw8EXSvbWsv08dhHPT1EJ65p+hM1N+hAPWK+k0N
ptid2Wh/aU+RcKI8vuwteUK+x93QZz3iHdPDAmrk2B5G5CdoNVgCxMfhFEtrOXY3g5K1JatLa4aM5TXb97wW2SE4c0mk5fspmqxY
G1f3HRMU2THVAgLv5nEVhyLSVL2CcnhMGClgNxXwSuQJRAOZDzegxyqxdJRUzUbjfkDbE3uBJRy23Yx5EVhg9AnJIa2wDuP71DXA
Xt+1fl5mwNBLAJTWv/abEN/efKoD00PLzQQ9B56H5+NlhD0puZ/16Y9ySuNQ4iMMP9gBhVI/oqqghXzbV7Gavg8ayrcYRwiDs4UY
J9tHV4iuyA6khdwPP82nWTIa6MlsJRwzpwW6GS8/ooBM6NwShdFpjByTM4URrKgzD+tdvZBeNa4WUNp4DDOIqAb8WGoafZml68Gz
JYU/k3wCDSJbJDG8FEbbfqpnLZbfcQJ0f3FV1pa65cNCvds7LoYnQDG2zUAJ5g9weodn0c0alwiLnnDAzZd0tKIIYIJmPuBmp2Jb
GoYACKKb43lP6Mi6IR5Ty2n5TiOjivotEPjGpOt13um415FGzTJMZ9arPqajZrWbYzgV3NOlpl+eS1csfOzmpsxwvyBpp4g7V6XH
Mipnh3G0sg3X8zNWlnG6ds/dBOutiueJlNLJXcNBlpUJ+dXyvTrhHh+PJxG2BxpE5FK1WmsfLbfG7Ih97YJCBR79SlbCoWF5Xd7n
NtzIzuoDve2bNoc8u8zB4nmBqNkmJPcg5I/fLgy/liT7sTjqbmJElfAZ/xxrssWCWI82Ga63GWSl0Qeh61SBjJV28PtewuLIDQ5+
wFfs7QKTlXfwEjdX2CwcHIzVXdObPRODbpJBjO+L35hDIZd/aYyhfgFuvP4TrBNFSwYmKL3p2DFBvXcVyc4A7v5gfPGl2MQnuzGR
cIDeZHE8C22rEfWPy7wKBAdOMCPFDrIKxDglzXYS4chRbqVBGSrTvrn8leYE1jG+rSiNQRJIo5CKhT6W3csYb+DUT1bMXJAJ2gsD
4voKauTY6iJue+xX440fC/erJUfIimo69Obae9SYgePjnv9146FFcLxcOcGjLVp2Z6Lk07eKbChRJJHlrTxF40vUYKzvXQau2ImO
1UdiFxqwNw7suVJ+fALPX+c2u3Y9y5FFdrU7x88/b8pzTrgiXVmfDr9OtADjIooI87t3AWCs6ZJnJ5MOJUeaBS6I4+Rb3SHHZlSr
nRzNScbWPvIhCn72IQYYzmq1zlWwZnO6AMA4kC7kX2I2lZQlJ2OtrS+j682NFxuX2TUmZZHsCLL/tDMRtbH9i2aoDn220mJ9mtda
q08G+72gOjCX2/gMi9uwqq7SHfbflDJVh8pylyZx62Dc5huucV6w1z2htsROsZv/IPW7yuztRwAoLDdk6WcFYOfDTyj9/Slu8Cci
nmYK0JSxYUF7Xh1H6FXgJbNH9uXUhtUv0R1bM8RE+Ap0NVn8xGsptRSm1+ZPqDDijHnTSY7VjWVYfiIhhEuKqZaif2t3gvJTe3sA
uPf1Cs40gRkrni4rB2NFk4gFCVyUtGSYl4Cqj9C1LEh1OTYR9zmxo9uNqK93OMvPvXF8dMikjr/GebMBN7D5rYY2TsXxP62MhLqW
auAKiGxtajrCD9FqQfi27yXJFAe/vPwEg5RKr80Yg1YuuoC1EtlE39o+gxf3d5OTK+YB+e59Ld/4LVX77BKrPe5oS+LGG4jAEh7e
9wWT9aBYDwDJ666NJe6kWrBUECO93mmAGRV/V2UBN7jITHigqRrDknBJzUKB8Y1aVxDxRmwgZb7VbgPG9uG/BJkUAEQ31hOX615T
zIPR18M5RL2LIGennPdpSFLv7xlZy49BEdhJoyY7phrBngIXOVVEPwpD7hHgQdc5ARk9pKTjwOI2nK7jJPLHattsNe/53L8Bl9XK
+vuWPqafc2hFFMTMzyCzP50n49jgJKeMraKbdd6c8qQb9uRcgV0DzybZB7exWFICa+4t/HdI/XOUOE80ooB1bDtHp7RT+XcdScdt
3GC2V0QnF4eECAySD5KShElETbZOttjq0TtswdzEQRqxsXdBHIYMhPgmdcPj5tiTyX9AQBQFvkJalIVU1NW8tHBwG32nY9JUgmux
EpS2EeLGkNstdCRAvCtA1WDT86BL3jb+dS4ZfFYLbOogvJCxqrnkyiiZBcirzcikUS/9bPRPJi5DuM8IUsy6h5I2y8Ye/kULhLR7
V0oz7jJNj+Bi2rMYfTw9WFSPaw8QHdGHdSIxifkPK6TVIMfR9J8fXjMYmRWrBK+j9hLW30RA23p+h6Bv+oyHZ673SlzvcrKNzrtp
YXvjf7jk8SAQ2uEjw+3hewit4Vfl0pIolXb2a67+7OM0GePWPQceyEcimitBqHs0MVlpatrrOB1iBhHgkJz+V+MRiJDKtqsEHH2U
sLmQbFlgCfJ4E2q8N0klQgUzUZzE/MxWoozZ3n7SD+g6dUCWkZxsq82LZDTR9FHwxrsyuSICDO7JLaW/ewf/b8QAega7oCmdUTtv
q9bxwpsb+h9R7Jj2suchQTgQfJAsVNX99yysyGFxZDcIp1nKGqHEYqnSJmz8XmKQe/Ccazbb0HkLRsy9oaiAdTqLUe9iLuY5DALz
9z3+0tf8GAz/22JckuabOZG6DRQ97hjpU12j01RJ5IJ3RXCF7/DUvOW1extYrNEOgNfJVaYCX2c+kb4R2+WdIaIu1kfv30nHmBet
j69JH+P+R6ygonvRPWHVImuQEL5zeBSr11Id88YUwjHUrqydTRlxujL9B6smChJRT5bIlq+nGdEOJlSgMibAXq9EKQebO897bII2
XrVy+5XB7KtnzmgbMgXaMRa/c3+/HQu/0WZBCe7tgYUlT1XF0t0Odl79JnSPPeset/d+PBOdfyGoSgzysNcTeW6kpIxq/09vOLPN
0SX6LbFkZF7Ly2aUw0NGjaD582SaQLaEozMjFjx9uchIPD6XssR7dnSqTADjXHwlg7Qi20iJYqJx7w1NLx3RlcTt8P16ivTWqvo7
Zgl8ZDypH65gT4Es+sCPxT066qWoSLyzisCuA2QYT9dgIhOwgP0IB4s19E8FhfgtKfzaoJAXIB4Bm3Ju5QYEPkI3bvpwRNYRvIeO
F6iT4snZd9jPvCCDNjmhbTK/9smqzM7zU1KD5sefKdoM6s7qa+FZkRTPoqxARDJDYetQugZ4isNX4kgByeFnZc9lv83w6iqh+ruH
HALU+DpTvj4MWBxUSi4telKfVO3T/oZoPpZ7NvjFjAsgqC+TAloxy9LHdRDTsOUufFxeN1TiXFqz9g3Uc4iTp/MXLcoB5uefBig+
VKszpIBqpA2dKgaTsm7viwcn/0AXaMuq4hK5jbgffa1IhGX4XPC3BjIe+/NJhUvKV9bkBJ2+q4oSUUGIBk6USJRWBWfxEV75+3+O
d2K77eCCt37yYUeJS/QynUH1Zs2oKAFtuoXJajrOjESCV1hqgx+3tv2juh4VRg6m1MNhF6U8U4pdjGBmo9WGQLn1Lzjv7MZzV2V8
XEBKpH7ffM1aFc8vzXjkBMB0XY7MR9l5YwA9EjH+Vr01kLi98NFx9TFqPBtLd69LGqk/vqAxwL2mD6JTPPI6Bf7EusIJJMN6/aVz
ekvxS0r5/sn/8PjpW+QTyaZrOGEwUdb1cDuZAFufH7eDaslyqB7A+nSgwuuU+C5PNpFwVfDe7M2Xw7s989nzREqZclGGYVGKZ+3/
hDC08oBAtSt8uRm9azQ8Yi0gGmI6xDUIDJ6WGsPSASS0O2Z5iJN5St767MXF9oX1Yyu1jBRpD8E5NZsZ0nc35leQlzscHsL2o4d8
DDtAcF1yN+ot8ZnCbL1a39CFotYjqMHxmVCm1jio6m4cYpDynZpz3DWsD2Z8ZzckPwBJ0XXHfuUr3Z4fByPkD2BApSyK4vBvMeCi
BBBNgn7yQoNKHR/b7+6hV1ofi/UmHDNDJibcuvEfALLutPTXod5F41f/wYyEhgWewSm+bsrCq1V5CUTlT6FA54BEBMbzIeOzjV1L
yKA5rXDtLp/YsYg1tK6UqFSfeHLfdU3JgzTacIcFZu1MSx4j/P9MJC39KADIaiOdlEnlrk9ioMgNvQLuekpn8HtdELME8unjhRVW
YVoTYMsuHLeJVbiqK7nQBSb37EXyllSfc4faXJ2kdiGcYnnsDnj7dgSA/ui5BL9FiddGViRTePg10tygV/Cid7RE3j9it1YMk0aw
wzcsFZ3dTNbYZzMN2Rpwf0+Z8tnKbtqANh3CvRjHG/rCrhG9RNbucW66P5U2i4Xl9i1CkNJmQh7DFimglb5YdL5V6+Wypi+3y2J/
5dH3DjIIVspHc9/wRj7JvpHMS8+N4Sg/gfY2MOVR/lNWEPRJebbJb5IcQcbkl5vJHvYiagSAL4gWSD6uxbcN352annNZDXPMiC+B
GyKLtiark3ZWDEEz+5H1qh9f5we7ETrDOEesYc8D7WTI/GpkpA+Xepao58KyDYQbYwZfEBVGsf67gX5l+/CslcSu7V5NB8OqXtRG
vPqpf51yEhW9skgbgI2wZji1q/6nJhJVfFPmpx7grPaX9ThycQjsXe4jEJHxXUclxRXqUtToaU7EziGSGPokGBbQH7hr/DxN+AT4
4XQsvOMw83QH1HMfRaQcQ6JVJ0I4Vt0Vz15n/uKT6V5wcl+3ugXnngVJzDmuc7bcCMbXDDC2qIjGS8aUREin1774KENb8O7JMoMY
zpG2mSurvt0m4HE341vhK0P4pn11qfnx/qsWUH81CfvM2L1pMIcyyio4LeWHQneqOAk8+5uQBEQaysHqHtsmSo9PdbUjioPTJU3w
HDIW9ZkU3bs6Ig8CYSG0/7ArGpMVp2yoAj4vTRdfPI31/Cld0A7Bk5Ygt5Eo8ytNzbrh5/m0u9wK6a3aeLDpXFag0HG0j0MHeokX
xgmBYybAqNSo1ZbAD6yjUcyi+2uFKd4+i5pxS9OnEwENobzkr19g8+cPDDslI3Ga0iKPUkGs7b45cfhcXWI6mfY+jTDliGjyuGN3
7n7L4xgf/KTBOGedVaKIm97yWNmQ0mAH6k7ofGMNzc5SXPljTfkrgiIjFvXs6FjA4t5vzdnSNyVr2eS2++1cxQ6uY7Oq0FhWhKk2
wlWLIfiH2Ax8AytbS+QbSMWaeGFIMzQGqaj1oEu+nrqBxeKNJT0/l1HCp/XCwj+at5x4wIwksWm77u9I86b8GqbxqbwFORGhGelf
qG+q5ihzagSO915n+LWmmPFkMi83eIphi4A6j/TtYcF8G9L6oTprrwSTVOvVOb/dlgtNwG/t0ll40qXkq3r/vxe6dsA/iQFq29Pz
bGuHADfDsceGvjwg+mvY7aWLyDS/dofwSr9mRnG7VFG1fq2jvcj67Cacb8zFQ1nt+1pR+Y0FLL0ZVc5WIehyP1iERtinEriE1GBc
yQ5yN7Vimm3IzHVBxOJngfuL3eBhXo3ZsGNd5wk6gKIfZ3j/Bl5NQP4EpM+oGUwKvvCt6nPFZlf0ajUVCD0n0x15e0v3sNgMNwiM
IShshu0qzslP10TXBpfF/dmNk7XyFLaO23nnKkkywakG9e4MddYzFJ/kE/QDAc71uNG8eR/IUKHnizDHddfRP8nVhZyjKbUdJ9gI
5z0w5lA5VKNTg3saDndUV3qVxCdpTOH2yl5hQsW/J+IJ8JAZoktAKsCWCjEDv9zlvHukCv3uu1Qq1HArF6TkhvBr1uYN1jq6Jpg0
vnAfSPJkCdtOr9XnSq6DrCkMLhk4u8CqgDCI3wxByb9GNhmkZv/zeXX39QmKmXgB8P/NOhijxz3wNkYDePGdAmwilnCLTzPQTx2F
IZCSVwk86ecGZu5NPVA5cQBn38JISrV4v1NoUUkfY3OvudF6QAO8SPrRPh6f0zY1BgibFtYnZ1jFrp0HbsuuwMaOBcK2RPzmo23a
/A+rcmXzq0KQoOY8YeWBB40q8d686cZ5G72p4NSbZCPieW65IDTYvJwbxoJiQdfKM9Qgmi+kib8TlcNc7uOjFhBuSrJfM1aBOHlr
LZvcfE8RCMyrgFBzAVod9na3eQAI+GF2v/hKvySoAFFxpl6myuFTjzANt5eVS0G82sUl+cme2IckK28N7RD87nECz4R2PyarDB38
7VnZrwNP+7rLNRjelSazt5bSyTotMLtWlJi/w1n8nkgAb5zQKSQDZXxAusJKH7rsOErlNr+Dzk2MCWsjA5DsfLDcY0yjvGyDAqbU
gZaOw2lmT6dehE1E1SuSTS09b0Hl/LbxWVUSLfed3CM2ikk7DGmOttOaHJYLavdLHFz/XsQ8407LySzwpXXWQaR+bJvEdrpDijxI
fGUA8UamCN0YgvcGoGYEXaiwt0cRESKRmx7iwwNAl1bZ5yefHuYdX0O49Y5cDsUx4j5aRLYy+jJd17PISJyYZSqoWfbDMH8ayKO2
gYZUuJ1GIQsy7npThZ+keOi2MsH2yq/MKAY0SdelutYV9yJW9SbfhKXPUr8NNs/c8E5GPojb3ce3CniA6ra0/I8D3vRcbQ6TwXhR
jH2PMZFlDd+lLq7CsHx5qbvWPIAfVu19Sr3UR4ReGmBtQsuTRRh5dtjMyGZ1QD9LMrSicsWhogMTOgPTfTn8JDuEzX/8M9zrB5rk
0fZhXYp+QC5hFaai9iV+2qk9L1liA09EIPf2Kne/4u740KRWfnk+cXhrOBctMmTKqQMNYqh8OR83fwm8dzzVAjjTw8YiKjZqB6JZ
CZwMR5YkMWtN101EN93ue28P4F5qcqWABxSFcMOolnZMx1LWT9RT4+KsItD2ISE8iS2ksecX4Gv9nkiya1tawPEbHJ848mKgmsr1
zDZli5RiPsK9YxkrCCH4xIf8aUj65fN7MUc9AsSknXQ8Jh5/5NE1MzyFUHnl7M93Te7tmwYnC3+USABvgGiQ+Ep1fsNdLVNLP1gq
h1MXMygpJehjfYnS9wJ43RuUxlAS+z9YDGIzvoGXnf/dkGIdrFIEmnKa+2OCDKKux1LUTxTwI7295iCrKQcTucn/+0MhT1pIwGC6
fPi9dXpxmTooiWFUEnHLZ/ICb0gUDL7AcyHPnQwZcVYnIyDAui9c9qvdBnkjVfeeuosKtrnUS5dOicPV1vOayF7g379/L0hXJgJP
afwErzosmwq2K+sy1uNRXuei77MfGhkNjPAMGWwDIHSFj00rEIiKt8PjK8snRqgpndQCV2Mjf63YssMNqXiM8ALOedFgzeNf64Ik
MzSgzGGhZFygIAVamhwBnL6gpQlNeo8hsnWTvqie46Im3usVzYIqBBZyI2aVpuJ2I8oa8t+hSiu4qb7lF8nUKfpsVv31e63aKQna
lVP/5DNViBcRC6vDOzxuKLPU6iGogfM+94I4iMdYfr2QPCbJAtmXzzQOuqhCn3N1HhM6pavThW9wHEbhuFNlRybOc9zZv9Q8NWsE
HfFUBqufIEJzS9/Z92jr1572/qkYva/diCJhxnKDmEjXnqtlmjV0CIANJU0sTSILwaywi9JsAbb733Lrc4TxuQTX2XCihbKb8NdZ
+E+GmayI7tEsRzW9QLvGEb6eNPp34YpOMz36FKqeO06xXwzCZIGl0ZucZRbw6To/aK2tCiSnLZf5YFmUO8SkUB+TR9WEnxBnflFy
gAvRRBqSGz6DBG8uZxDKt30S9wQc7AixBe2WdZvx9X2kJWlseU2fRcyX4dodqE1aROHJWXmMv2wS5ArDSK4ruLnpwnKX4H2LEpIC
kIF+EyH/RuklgEEeM6UTsPFLze2pRS8sgjug2iNe7N9R9tYC2u13JfqvbsagMsTMxMfr7JEYWNyUrwmeaKNt/G7FjI/5j5QbJ+r1
eFcNZkkr1mjWC+aEhD4uZhSbQSUVfzDEHr9NtZZl+Wg3jnqp/rPazmJ1FPtpWEJ8sbafRMxTH4Zrx4hj/WckRZNh+K7hCzEhAPhy
DjP61EsjK9JDebwVogbcjBLWqFHR77ArdHawBizyhwXh5k7rMNgX1KuZpG7AOAKGySVaNYnoSTT5QRfzbLTNebBzoI4jCLb+F5DN
OWORcy16Edc/37WfFjcuQWy93KiPDVE2cJvEL7YSlKNw/IuXtKe8peHSNzGQi9ItWHVjmE5v/XOP+DcXS55nv2dOOFCL6/9jg5oB
T9kMuncD+IvxRk8fVgwYDQMsCgznV3HwuJahgtDxLNyC94FDt6BHDCuhow7OzAHVq5PLj8JxwTg8rsHfPZERGtd6EzD6VOQ61LkH
N7l2lg93SUHvpNhSkd3idmS+Tgi7ec9uhsiF78NuExB/zyU07YF7fd0cyFgM66/Ouxktk3Yn3I6KrEBXNXGUSPOg2lYA8+sbDp4l
Fp++KgHUZaIdcC5KA8MtYmNyb3vAbcgzBG+M9XBU11PTHc53uRLyB2+2Wch65FTr1yNjOPkfOd6UQ44xUBJ62iij4nupG+40Hl8/
yD2eyJ6cXPLU2lUAZafpZJq7TizYrrm8aFIAX7m0Vd3sh6P6z1mSaqBQlhcwgvnzEAMTgB5IVQRQNHJm0U4vyJbOg9ZLJwiNFWV7
BAw1cbCqvWcy50LaWX3QnkQcTwaCaN1s1JuGNKHOJXm07rcJeYWRTiSgtZrj9oegrDmBIKDe/VET/fHJJNum9UeGi4dVGT/b1e2L
ayfpVH5mTfiQR5KXfAbFkOHuPvePVExwhsVw13Pk2R4K7+BbUdiCX5PV/nv2k+nlv9WQELn/yLvCzfbcX/Jd8AmVATUqBkclCiUY
5JTvxz/QScgZjrZ6onkh7ud0YDSsYxSI4n6zcZ4KF0vnwd4jLeHCf7UUq0eU/+M31wetLsJ+P15/jGx5PurP47Rb+kjdAJVeiMid
UB9UYwkefQS2+rti8hHRhKGU/FC4LoSTnpmaYp6YrctJ/KKk0TThXfxFAnhLatUCDcze64gDkX8g0sjTr3R9njnOvpbdXTrZZ1uz
/kL83R64SMl5B9IMqgYs9tIqwJJd+k0+dcm3fpI+EaLsKtFeK0fkuUpjS7PCSIahi8+/06SiwEJxZrMYrs+qnBCQ8LQa3rXrSfFh
CeBLztaFUSWBOdRt6RLraIrD9ESgr6hkwwrrlYqYH8bg0ggpjRYEiuoehbO5Usy1RZni6mrReCfH1IZxauLL18zqJKthK6hDQwcV
vlNDwgRfQxL5EwD5YO8xwc+d7SAABGgtMOYrAcHSZeWgl6sP8kYGgDGcB28sGKnWjq0xx4bp30qoGeekPcOOqkTMqizAT6MKjKjS
pDz2X/eCZMG+uGOkM861sar74B/7ARnZPaytEPn6ZAj/tsx1EdNC1vs4Kqoy14E7s9uSvmo0hEw3OrSs8cC9M4ttJqI7AsqD4ZQM
Z6EMZfZyVJ+D1XZNog+nGA8StAg2NkAV1gIB1bi24kT9mK7qOSFtpClyLBBr42mXzVTM6izsTcf8631XWF8wCDFSj2D8psQGELsv
bWw+EWgkgXMTamdoVmMYs49VvSuI5a9ZgagcjdyCkdnhSrVlp9FUlXBT6Wwz/PBaHIXXiSUCImVhJkBogaWlv8HN+ZmXl7oJH5g3
1oRhbchxxx3IlCOLIkxMWF43M0I3ZQBFwqBvn3qrSaO3bS7GCim9L1d2NVeuW14ssX9Vqsr9KCSWxbT9Qo5kc/8jULO5JzNEMnnb
AQi5Ufo5R6MQLU5UY7s7W/S13TndesHRpPLn/sGSJzvUflkHHnTV0pMTqWVq7t/wsOs2YOLNBE8P9GsQOoAYd/iwIuxsYj0xIYpk
usAlJauabXLKGwzq4dj4Nt/KqMfKL4vAUDb2diScLqm6yhHBUdb/X2zq84qxleWNEVu2TpiHYCx9raF43m8zKAMlNobqB41NWi8O
MOZBELc2s87N/ct6bpBRkZogUSrkdFhCeRFqvfABeygyUrnp2c0TjBwOYLUZymIZ5LWmsmmT6zfSx7QgsfiVrMbc06R04HQhSy61
lzsF3PsmdWB2WVpSzve6WFul+mYiAr5IfSmOopnrftQ/iNo7YB+8DCwrCNop0lL/IiQ6O/MiqbEl+AOGqdwmXt1JzIr94L9XaNjx
wXNOBbJ5CHuezRzXOkdrcWoHoCN5TlUrfVR9YXVtmQFk18WrInrlsuYzk+Onuxifxt9OczbKrrLYnXvpN4XaR6DfwLGPV3Lp/SAZ
ku8wYdxjmNDpt+xQdWm/JN77yn4TyQnCHG8Fc+PbmYz3Oi9BAOafuhLO3NKK+4RRDpmsR2A6m54+cuejMquZIZFofNVCRNEstK8L
cAhyYwsCQtQrpcmGv08FP91Ip+SZB3qLkRTlymGwjoya+gdog0ZHIzF+X1Q45DyyUubynkIImep9BWUGFUyXe8slYH3fWEYErJdn
S3BxxuIEWu+av4WneLSlVHaCX13wsMTB2h7Br9mkdcZyRvrbw89xku3IsiHiQBPm1BM75keibPVBj9AKZTquCVWuOJJsJfUcjyNW
lNOa58j7Vmd24yDfAo0yIwhGy23WwX81PsKOxg5VEQgqQ+w0Uj6lCFeGQZA/IWo3bUcuYlUO7toOsZp70SScG7+vTN8brEEhCKSj
jwsP35HFHCP4QHnYLZeikonrDx66Ot1Y9QOE7gupQ9wKOuKjXYd0ou4Gin2OYVEwM9xJFU0mEjG/LbEKTo2WUKAjzlNAiurgnh3D
VaaiuQe4rjqDPnZc9lr06tgMhoNE4Euz9v3SALHOLNnCARzfXgWhXrKuj+tfmuZkSFoh9SVtOt+90qnyJ35DYi0eNf5dpwUP6TOD
OdvAHiCKyK2/ScB4ysqlTeFsVS4/4xZF59iX2uNAiiaBO9/d3e5xVdvr2kn7iUxEMqkBowQy8s4mn1JmA1miFsUmsf8nZxElhwi1
0SfrT0Fq+zYiggFIhhMkDFxkLovHW6LMxeWadi3h5SEKHecCqyfjhPcV2nawJjntwjxhKjLPheesrBrYR3wr/qiTzt8egQuFNLmv
CpXoAr2Tpv20V9qjYqV529EVzoXCMWo2CnjPxJ+C0I/ajfcLSvvgeWUe0n65/k6givBdPZOr0vSBGdhPm2yyRS+a98H7EtAIXECY
ooeEjUBrhqX3pU5Ve4Aiy5WG4BSngE5z7g4zmM2uvCthI3F5UyUnnW5QJexkRusWeI8FmtFjGRNmaTfbiHLEYMmewdVtAR9WuDG/
DGo7SMphne6Bg5BeuNB9BfgB1yjFwIOIyJ/sE73YbMtSvamZhcIV9iaiJ5E/RJdlJAYZRR5Ff6BpMU0mrFEXQh/PX8OaYmdy01dS
NdtjZoGAKIdv4nL2QMg4TbRR+DD6rNad5+0FGm60cOjxGjhsU1imPnG8ZRcyVMBnyqoeDrzlJu4vHYtGkN/Vt5U+iLhtGIPzH8Ho
SOlZHsGhnVBq8jUX9rQLYa2P3+FzZDnmcByIbspIDHFblTyKW6rJfGt49uc1kE1FQITzxddFrAyY/xGJ8ZavyGfL40yRr72RnFvj
nRvRWIjnCh3A7x+2ItIQSsZhXMwSW03QXsok+trHaaPbn0QRiiaot4HV1CTokPqkzE/Od9NE4Tvg6XIhywBblCtD8VSpOt2UkzAl
hKh0cThmBqdGn0ZLlOcV2Lc9XOOO2uk9f4UV/h0EihLIYzFSNMS3GyQxWLbUjC3xHf3xCQJFRu7jv5LiZ9MEpzXayORyiikuM7IF
HsIPVnNPLMFbzA0oyNj7lMiNO1GGor5MTRUEneqDsWMfD8ASyBo0jpiZ1noemcA6bc+qXhtEjeBrB31td8jVVPskRf30+HxHfK5u
foFfNF4XXiSR3vQU9FePDc6wNqoGO8DvoHaT0r9PDvpvr/QKgVTbknmmoouvwCCzw3MpuZTdt3MiIWPIe+RoZB98bGz9yNKMgYYo
EapH0SebKVpySqtaXLIfU9vfvcMUrRahr2/rKQVYLw8v52C4lTFmXYckVbZOTXlov6PMxMaUVroSeaWMJ7TFNwcM+vrZ2XtQXyL/
e1W6x7A7XaIplKoyuYXab4n8qefIUnAXlbCElNj41Az/GF75Xa3NFIya7MMcwdIEQ9Bp/pQj/HWf+WKFtQODJo588RP+NH/StoOV
kAM3vxS2KRQbXwPDZwz9bAaDIqQBlSgSTBEFqamwAOVDtvQtCT47TLKVMt0jh0d7PjilDkJI3zT37/40OoXoHnmKYyTasJCZnyS7
4GqThPg9IhbKX1c1CskQKBM5QdUg0ZhaWljjd+qYMNxEzYgoOQr5fBxDo8f7Z4PF8zmxRyhIO+oEC17PfWR6WbvSgilLDScS21q5
ZpktwGmBxQfGi70K2df7x7sfJrPCIXV6nAdPwejJN89T+SxZsJcBcw2TUf413kmgG7KyKkoCXlbBvlh76N6roJ68aGH49761f3Tc
IQBVzgY3dfgIUFXqTCv7Yquanb84iIT56jqhTjN+2ISXnYkM5iJGnYyujDMPC7+k+OXg0nuahmpvtFoxQixP7Scq7gbMU/viksSr
85pRhoCZ6J253YV08r+CaL0ej0GkT3fpCjsGc+6zdluwgJU9ZBBUBcZTk3sX/ay3px4H6E9bwucjCgIFD7yCUEtwVy3+xXCnap5P
UUdQBQihsxOWJImiCrawrgrhgJHi87u2YMGs8kB3FjyK8JpHQe9L7CTmvkXP1wJQM+3KRd0vSVp1NTTx07/tXp/Sy/np9I7WfqCu
HTC8OG9m7Ul85hbp8ZfsX43w8ehLcaemHQaVOEEuIWu9we5SD17oGpMUWLL2YRcI7lHpW86BPtSuDOO7Dr8q1Kcz36w+utYBlwza
0JQYNQsFFmW7X6rGIlHpEubITafMLIgjdar/Z0SSphmlXaqEiVhnDcOStjJfEgRMVT7ItPqbb0WAz4wSQ4K+UY3zXr9y5G2IP7Ov
Q/3z8K55dtY8W0guZi8o+LE7XBtdDqGP9fkf6CkSo7cBwaGK3eUQD8uNDMWtDnPSdD3me5ropJGumwnXuHQtDxVjjMSn7AVGwrLi
/Cahby3Gzp+zOoGb+T1vwkfR6emPaQA/qdaSXVs+Lrf/Qmk2NM3EEbl4y/wPXi6kgXOQPGVqhTLNS5+sbvynOKU/i9dJl6O6FIPa
xeT87+L7S8K2dvQFzNImu53/l+p0WXrIQ1S28g73BOcNGcj5A76N4Dr0aH02NYvNIIcthNMcJFjKRRYcawAHKhwflliaWiJNmu8y
QtcdF/TXkwpKUwIvix8NEy8to5g5dNH3U0TgX75PiN7evg3ndkISJM+xhZ70bs99T6vPYhMpV+rPzxcZNm0AurfZXmW0lOxGg8yL
i0/rxZGHHNuFTXr35f3dLsKS7xY0VQ9a1upiLKiYbMEJi3vS8HpIoCABqRr1SLEqfzKZZjEyyir+isdm9ddUVCStW4SfOL1XhLQb
UinOZRM2foHCw43XYAndqhVBIwqxnlQV511e4mU2wJPwGsSN/mu7lo0B54ixYumHMGau6rXMlBMLtVBYBIxn8T1G2PP7jQafY1uH
3xAdmuNdPLYH27Q0O1/mYz2HcKZWA6s7EAhiSoPX/31t56J3L51R6O+UEsIM7kYP6dRex8LVR0VmbXOWL7ckI52JE5ekEn0ML+/Y
NdMC4qYQAG2yvi9HvEKm1RinULu8H12NrEIcKcdRMaNfboQMu4m+Sb8jOln4T7To+ibxGCBg5DROXTdFbpr1klEtpCJkFtFe2aVM
o78z11VbropvRaLKA+tDwYgLeeVpvuWVmQi7QmhF7k3U6SnIrnXTHnuR3P9XgLVyEkZsHoNMs9NUSd1cCjDjAXof2WB27SwE24pe
kxS14K8qan+ysNgPnI/euJtQr4RbvvrH7ju73c+BPr/NQSbFDvS8f6ES5iUr2Roxjx/SV/xIgBC7dANq6P6H+9XT61RJIUQp890+
UH2GGOXE0mixDF+eQ0s6vRQLBXjS0EnCWzOhU7squg6TQtA8UgyUjWAhPCf/VgubsFnqAg7d0yVqDknegg1RT1SO5CvGqjxvID8X
/QCycEAtofnpWvb2FIF7n53q1kbL1p3EvxQixDcIxoBJF4BY1LwJd6dJBys+vbVJzSBM3usDqfzBye2W/5pJSMYsAoBTxzQ2zee6
XrubqO+4houKmM5e6Mpdg5hAwbaqu72CCTPbV7RWdqa4JGNaJWxU2K3cCL5K+Y7Ot3slMx0C/DC5QpvB9r05jQ/PHcClkhN2Z2LK
DWDutJC1Q+Aj4TWuQxlSE478bQ6nPROyLeiFPHFkFOoENIRMi7V0Z1YsfKcb7coccnB3yYyLrbLUMLwBlC+nM/dAFMVwu13IPbNr
ReBib4rMl6F7Eg3Wm4DlmP8hUE0oj4JHqljJByNjKIGNRqC8BaCFZYCvUYzGgiEwR+7xx41fLDPBpzS2HxinGJ+BOXQDx4UvcmJS
GkQLYLq1Bo2gPGnz59/g/ibiMFuKLjUrMihkd1j9VPq4xEzExDH71G29lCRg7CWO3CDOcKekGnzSRL5poRAboGixz0KGwMDMVk9o
j9ZvxlaRfsOnRsAo2ibYZRxSzqkkiVl2QREw4UCzbN1+PCbGANyssfZHHQGEHiRjDaGDY5pKrAlCIxWagGOOeNi0GaO1jCSIoKPC
6GYs6Upxb7mRVxcS1wKeQselT5mHRgMJKuEyWj4CNneA2G3dPCnUcOUqGjzvLMlaScodMIMvapdDTQKhaRAoKiMwDfDhZ1R4HqO+
BxtKT73L4necpT780VINeg4CFFhd84esYDey9WxkUBF05eiAF6+Q1aXo5X7EV4Wt6u/mYb1YOFQJQo3MNAALbVZSUzlcWicOQ9Xq
CJE27MIsT6az4XHFiyPO0N2JFlLkCqGz/nGOwbR9NftvD/cyHIp6gllJqKTsVwZXonR4THg+qbea8taaJghHQQ2Y/cneFpUuN3jX
wbUx9vqXm/bP6Mpw605wsVy/fOuIA5tisUhNOAZerRv7mYGvGNnpCEOq7l3Z5IS7XyaWyF4SwOZCM+fe1h7ai3KI8U8hbTUnL+wg
JQSEPaxuYjroReEsgqeuz0KuVcPVbd0WcSZddDTXTtxvuuauJoI5B3UbjexWXvgyjdO2jzoEhwgTCqTtMdk+KHdveGYJU0L22pKT
rJZktCn1VILBPWVHkm3H8sA+LAwOgyqIbPLCEeJCS+FTD8WjIeKfzzgrLoeb/dKSh5D7gywWlS8QIEHyGHwspN9YtkbAUzbaSqtK
nsT3WdLIdhhdzOOW+ET+0lkFIdiwoCgFr+OPywo9ZoBVRY0MHTyzXysBcdbkmaHOLy6gjgIIvPwp7qVb/9ojCH1CaHBm6Dr4TpW4
Fh7Y+V2c0RtRFMDdxMfgA8zAaDovIPzJbsg01+27X7T6s0PCLys1uJK1JW7G5Kd4FPh5AGr2H7nGpCXXTxeGZtJlYkR4JdaVKgKV
T3+QeC0QbOFnvG9tTlSB3iYaMiPLq7Qv0ZfZ5dyMDTd5RLzpMJ6wxQKeT44dpL/FrNMl1oijX9xF5HBd7vT6itAK0qhoyfovZtXz
5MAwWwl9ay6k+g0Pj+iaiLKbbTRP++9th488OG6u5xv345hi3+uS4W4iluaEjlYyJHRT+yBRSQ3HUvTAUKctZm+UfthxY1BwEKXi
wR5e2SHfsCLYI+PJNIKeOMpAC0MPbXqN7geW3jO1f6cO28pnes30SIlSOJ+yt+LNcn8S9cRyTs/8I22I6kYYOMJd3ai7gFLSmtd2
15fNgDNxDYn1sQmUlNEUbEez4jebY38GMt6jAhN8nNHYqMWbmKz0vK/YTExLIR5+u0fnLxuGluT4MUcl9QoRiZGRwXRzXdqJiW/V
DmJeufYxqOiAZU480WJhAK7HiU37KStY1gms8q1z0gIYVQ0ntPDrfW08TsJ/AoXn5vexSpyohXfenhRO0zbgGcSzCGny1sVf8LjL
bh1kI9Wm3ZNLhR24nVLiJtd5gSGSSkMYu7PG4M8YbpMScpgUa9Gw5JgvU1oZ3UKP3yOLDBwdWBPSHbzCIHG8C4R2P+oJfovQvEZk
hhcTUAdP6x4UlMg7H8QROgPIp37AZpem0qPu6xKpSlPFcMdOsWzUSBE9nbPYzIaJ6uwAjNis6ojvjrYQ4aggBkMsE3vcq+byMoE5
wuX+G0zgapRsE5QQYcTCi9cZefoDIJwPLsVutKKhnKa/c9tiScAM37b2dbFM5PdhSdiQ5FIQdWvpsk9CR4SeeCWd/68QzD1T1jop
vxI7K6S55edlGCT8UOmS8A51PGs0L69+XDXkb2RkdRarPyWMP6QjeFe+y8M2CU/eHy7qZKyQ01UGZ6C5wZl/QwDhR614AVUUh0aC
9dM1tm2+b7vf7rYV25mvGiThlllxsOqFqv937FiW+xcdj2M5H2ebB6j2AiyLKHOqDd8cof5iw5nsDb4HA2mLWzv2benO1LWm51+p
ECTjWm+HT+Jtcz8ib/x6qq3bSh5pI4i+vUSJ1PbsdPUEo9hmoRnhdDcbOwmH1hZsm5Dq1M5qlWUfPAPuj+ryMFzyOoMfv/+j91Po
3cQifb2N65Fh0CNllfTL5d9ecp5fHASxph1t9PhOetKJibdPq4i5yhwK6dlECrTYW5+JZTZ/R/hY+7sBxjCYf6M8neHKONjFcJ7q
Ie8/UUnx5fHoE3lDq4qdZv9wPO8c4gBuD6VAf8fu2BgEJJU8euioC/Uqutpeb40mDuvZYE7pIoYteTyEr2luxZ5F6EuCun2MIhMe
z1uuBpHQArNoYmeiND00lGv+qs6t6dzDAJQWvXQcZzfg5eVPC/ahRysTS5CCP5HDEok/mcL2wk4TKYhm28hRiYTlH5MAC0sMMZBy
gh8K/ydiFAgY0iZ4Q521DGRA6zgDFtbJc22koAArdNhKgI0PKwvrDzbu7jw5WbndWAv0jxrqaCaum6lKG9SdjJcksEDGshbVErCx
wNAk4PIxh5UEd/Xe1hzubQBBXXDl4KkIfnm8blvAgQ9Om8nx5lrGLFvMdGsL0o2yOEqTjWaE7D+nsyTavQJmebAvPRdkVE01V01O
5giEoaZC400YmMcPmnObooeKPQsW6uJ6ecsl/FaigL9vexAPa1saBRDAvFel9nWm7Xt7ze4IAEhaqueWnkQ8kf9SAIbl3/HqczSs
f5/GZtVK6S0pjxngkmfQ5WRASE1b2GXcVAkZ0MLcq5wQHIsgVDvOpQEvsh4is3/068HPdgoz6KviXJQuThtgr/UQRgVUpdxUPlyo
AMlB4wvULqNVmGjHlR/wUfWY++rqfRkB7NV+lchZh3jPUeRtXqp0lK0wubR/JyDd5uZO+72FlyQ907IjwhzuEKeVc/g+V4fPOzIx
Q6uaxZZtQbHAOueHui3UWrJkq43SXVkCxQaxvESgMBERnhOMsaIa5oaGAuDXwlaZNuyI8ssWmBlSEExPC8syKEjbeeLnA2IF8DCx
0rr5W6l8+e85GZKLOy38A1NaRiN6YLS3v1SdKLXuA0xN20eQog9Gbhrgzma4XQCppm2JJU/Me80/emn1c8KRTq8YA3NQOMbAFzVB
QKzSNoPHrixhu/zRNVlbwEbYbIHQNzAMvhsIrTCnrM/obaGPdviIkY6JoXIuW7wwBxVbnlLIHJlxTfRYoPlp8AlX9EQemjHeSTlh
gsozPRCUUBrCHP2VCFCK7Nee8t85tV5oc4xU/JMIwLe+0kStDEM+ML4wbLukgAm763Ija4aizSIg34IaNrSAhqjJLtd/X6erCcD7
RbHFq3w8caQkrdeuyMNsUXVPC4szPTiz9KS+cCwwN1LyoLzXRAOPHmowEKt5yXyLflAIIGXEKfLyIRNUnnow2pdSnGYB57QuUe5A
YrQXczfXZhkVnzBktMlXNMdvboEtB1H0W3w059bi4merz/S6AI1DfTZV9zIIX45QSJ5mPbVC7tPJR84I14fwUgTbFBwWXJylIz+F
C/qDCTXXlLgn58Dnkt6WxsT7M12O/ihNGCDlRscpwqM+4qYKjdt7qHxB+IGnERYJoZY+a60qZ6zi8wvpgvdqxP5iMQaLXrrMQcSK
qxzgcx3lpOPdFTnCPAY9R23HoYtbIh1TxKGdtC0PSqt8RHakKy8jfUiWPcMgAMG5bUXLXQZHa8YSuA2IOwtu3G1vXBiFDYO71U1S
C9MFEZy5Xw3S15/9rKNghfecl+xnIE7X+vzm3GMMVm3ISDFWenTEPjCXMaqH+qltF6udrdv8H2kz1Vn/6F0vB/xvNhwdDcLUyZX8
GQJZ83DDA4kBhk48TzhistNN/8pRdQAZqT8Mj8TyT7wKkVcicsMLLOWq2ASSQKZ4W4xi49Hu0CVskLNVvXImvkGHYfZgDiVOwBSb
9X3F3XgMGifKGeCDiZU8ihYHubhjacbEubidNBdQIrchq528SJkCnWko61uyRPF9Q4ME3dXNoNt7Hu5xXzH7hCfwQlwJgVilDdre
y4qjnxSSL5do9i/S1DVx8e4gLR1sHLw1Rptrn/i4LP16yjux3iUqKfQyPLJ3reDPTI/RxRXEJ7Apo++sf++qxYicfX9ah0PkLD9L
3MuL4dTRjlBHUjacc7aFXC0Im0DXjGoOB2UREcZ5NWOxkEVwlss9dBYDqDw5odY+g6oW6GhHztS7QP4yKENmH/jQ34srqP7auCSn
HqBqYkV9EJt0jr0KTbDRA42JSfCDWSW0GLkmLerkeOFrqrRb222H+wdLXyrljOywbGnjaYzgEY705Meval2UU78gA5U2nClWhp3A
foVGOF7rGnanelgZA8ujZFOszK3r34rfJcdOMY/JqfC8q3PJiwVIo778vDnPfvofx5UlTa2Ny3AWur/eqPxDyOUwYmjCieZe5gsp
PLQk+YVulFrjWvmJvpmqrxHwZGnq+XFzkKhV6iDYHHpS4m09VEoYVitQneE+m2PRIEki0To1wWWpnwlymonySrEp/GzSJxi23Won
ROeFgrHwAlazz1F+M93XAbsPglpuzx6ylz3SwDGwJWwYHbO8DVBE8MRf2C00c/Z63cLwjvz4WbIqaYe59ugzg/kbdSWmhz/UgXta
Ie5bk+TyMMUahOtHfzXpj8TpkjVWBOsfmFV/KhgKmhRZyGib4jTJbrkPVMaLSN9RijdV5BLiwLd4BqS5lCZXdc4+jbCY7LZ5SqaM
Aq35CRM0BUibC1cGR2e5DRcCw6m5ol5mKkfGtbOIWaTnC/7M/pWnL5RpxOCKqBA1F0kagcknfs/HkVFmTd8UKpa8Uqg2ySIJYffT
3BDJcE9JvoGZHowB5YxK9Nm9h+RbuvEJRIUUH8ZuuF6Ol9cJB+6RWJ2G0c8laGcxDle1jxkx4P+8yzab4kjAF6ZkH2BrQSktxZCD
ZyqFxIn3YHWP3b+v/OtPuKKADNdvNZP7+uN/CYD1WDu4jSVpgcGEbTTRDAmCsu85q1soHvGc1U2uT5N7161rs1+/oZkoU4QsPN0O
qcx3+Y0s9i+juu4L4zFRks23c25hh7CJ3B+5bLWKdwJMtF3DiOP0zWS+lYE0ACQjA/m9pgzfupPswZCHjbf120Exd8dzzSru3/Y+
fmrzauwK1eMxPnM8XNM/beD2qNOuL1KlV7lQm5J8eAT2UQC/xTefNHsYLU9OpTxrNQOR7fHlQUC2qQ1gtSoXZ4BxXPltNE0eC0IV
ZEGJJCyefgofvoNlNLtUIPtKS3jLcng1W1NGtr2zir+e7wGcHZH/6v6otSw6kpQLd3rbYHgkg50l5LfiuRdXMBjs1w0gDBWljtyw
vDlzfmCC7Jeh9erE4gfxHoMigbbxdVRM6Ajj+VVD/8phjaxHBHYlRxoLIUkyY0GCQOtcfVlO0Hg5t56PVzRx92XyxHpEnQiOaL07
dd8f51w0LER7r3TQ7QAXOfpi5zJ4AIpEIIxFp/pgncycXsRfopmJTcZqap1K9FqR0YlmRD5T1BrrDcka4mejiv0mhgBV+DNLQLQa
kAXdkYRB3efiHFcfh7qg+C+lGFfabA+aXZx9/l6o9Wpj9LVFGl6RsLMRrSTjYXcf7x9haD/lX/dgADeEXvxGaSSGu8HvW91g5DEb
wCrGo+d4PehG8aIvZV8txsFLsbTHnMsqiu+MOWopqXtmJ/9mW2wo+sFfU5UHNPPC8y15wrYbVxne2TRv5rjMnN8ORyvZVGDCNboR
sB2jxgRw1/wOT/cYnonuaMNHv7JAW2vks6v4UA7l8o31sj4WRV3UEzuqeb7Gn30eUB5gOPXs15zw5xoFNXRTsN/FzEu/GQs4mz2v
SeCRkTZoeWnlbCOpCPmBFPhpJLcJ0PlWTjKIdoSyIYRBj4hrFeABRoXDhkrS2I3kEfy9r9N9l6S+QYASmYJxXaTuTdw3Ez82PIyy
7tTIsspOkULby1DaQKTUeGi4oXW4tFXPG1nhS/1zX2yAU89GpxX5BUYQYGAsF+o9fs9KdtUtFzQ5INgX8S5hOBdtYpF05vCscFxc
foZVPX9wIQHYc2mfHf5tkqz4EuJ0U0rkfbGP2+0Jt367DxM+Da7iN/Bzzl6OMNRN9WgJjCr65UVYIqKTOmleum3prlEwdFRMPAWP
8f0hbL0ST5qnUIv7yLBo1B4KhCCXKDX2br/fZxoSswSVTkfwIAMqW4OpIok24vKfFnkWzYwB2Owkm4Qjet75WiK4sO5WQMMvBXNb
lzWD/Vx4Wt1QRnTV52wh0EQ4VqDhSOXmmO9ROKwPUm6J2e7fk9tGjQ4bfXjNVcCD7yq+0RFnKXMirxMy+egoathhtWFJunJF+5xa
tWUIPBytJVjViKm9/n3nrqXN6aNE4RcYgH7Aul6Cz+76DNu3tobfizCxSWy81nyxTxY6XaSCSGYZ6LCO7/NII0zy13R6cjHcEnqd
rpSGiARXmZqQ5o67m45DIj3w3E6fsUzOgSF424pfRQmhG5ZnQE7OhZOlrnz2AOyTE4NBEhr8Gh6/jqeA4dxRW9ZV/OaD/XQ7m4R9
5XHi3yOYfdWmCqMzOyIAx7p49uLGQC6qGhC+oUmr/DNBwR6S5tcxZ79b0RHUDnoOogwnUaOJhqQW41V30tw6ILZAGhrCZApyT2q+
i6pfVrpMjrBilLrUvvB6dopLWti0VS2tRDEDHudcvBclKMzOi06E/8qIoVQACcbyYK1VRCUIiVK9CKGT3f6qMO1AqCpl26fabtLj
hTmXCYkRNQIda74VEeZNaB0XDPkIyJBcbfJrOQr+R8FvS0Y/b39MQbW/djMfLxK9s2gAk6wnaOoigkbQ/ELaTy94o/TIQXDw0ezf
2an7MwT0DBbyy6KAwvYGlu5mzzK8WJPS7O9eF9Apbmp5ivnP7/JqY+ZxjdeJBqpaUeLKz6wyP5uLltVfn1c8HdDN+NIjvjKYV2BZ
HteR4WZfdMr2Gl1dfhUEuLi5WmNaS38p4gVRiPI1rEHuY++GWHvVLaq9SuqvRQW3M3Z+fYHvefArJLux9imYNBVYj1UhaC5YnqX8
Mecl5WCDTiR8P6IaHtpmmCbzbaEj58ctl+9MZixkYrAEmXaVDJa5Yz2gxcfUmEYGdlHqkaypybeCkcOBVw+dbb2tdN8L7jpmRSO0
ovgTrw8v4p5BvqVTsOY+AmrAAxoITpiIrA3TDvYze4+H2L5antE7ueDezbHHbJ2eiUbkmkcKP6j/Mo3vFxJAOE7MqhlBaE1kt/3O
KRFQh20EEeNUzph8B5qBjDtgG6PQ/AWGhjva5YyqjC6K2UZrjI3s0ZV8JOXKdotDZtbBzlo/G948dsdZM8j/C2FhS+oP1PeOa36h
paqsYQBXlJQaVViPKDrhzScxOZc/qkNhmamStiLPqwFj1PxKsQvg98b37zTa+X1D46gBfSKIOWBT3ONOdTiS1b0MosKEDjhl75ht
ILoAAAAANAwuT4ZvIsQAAYXGAffJBXXWGImxxGf7AgAAAAAEWVo=
"""
s=''.join(DATA.split())
assert len(s)==33852 and hashlib.sha256(s.encode()).hexdigest()=='f630ee7ecfd8cf62a3e10d88f1e1446c335332ed009def1c28e267a8e5fb658e'
x=base64.b64decode(s,validate=True)
assert len(x)==25388 and hashlib.sha256(x).hexdigest()=='52b6ebadca2404ab5bf62f5a98c87ccc934391f299553e4953ac182ffb97a722'
x=lzma.decompress(x)
assert len(x)==91383 and hashlib.sha256(x).hexdigest()=='8023d29ace62bd789be58fe5920376b18f8e52185f3cb6f38c232884799d2e3f'
j=json.loads(x);assert j['version']==1 and len(j['files'])==16
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'QR11_SIGNED_SOURCE')
out.mkdir(parents=True,exist_ok=True)
for name,s in j['files'].items():
 assert pathlib.Path(name).name==name and name not in['','.','..']
 b=s.encode();r=j['manifest'][name]
 assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 (out/name).write_bytes(b);assert (out/name).read_bytes()==b
print('QR11_SIGNED_COMPLETE_SOURCE_RECOVERY_PASS',len(j['files']))
```

**Acceptance boundary:** measured and audited signed families, a continuous two-U theorem over specified joint shape/metric regions, two exact C454 nonwinners, and complete observed finite receipts are established. No own110 endpoint, no arbitrary-metric exclusion, and no global exclusion of fractional chord constructions is claimed.
