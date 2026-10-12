# figure-0346

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Willow 83 — finite closure replacement, actual opposite-side moment closure, and a global single-cut obstruction

## 1. Verdict

**No strict homogeneous own-centred (1,1,0) polyhedron with E<500 was obtained.** The main new construction has **228 vertices, 359 true edges, 133 maximal facets, strict own-centroid class (2,4,4), and no weak equilibria**. Its complete supplied-support chart satisfies the global bound **E≤499**.

This is a genuine finite replacement of the CAVITY147 supporting closure, including original B023 supports 50 and 75, jointly with an actual opposite-side material cut and a certified nonlinear ordinary-moment closure. It is not a Gömböc, and its equilibrium count does not improve on the separate B023/211 or C1370/110 benchmarks.

The strongest new conclusion is global within a precisely stated family: **the constructed zero-centred member is the unique zero-centred single-halfspace cut of its fixed ARC34 source, and the unique maximum-volume zero-centred measurable subset of that source, up to null sets.** It has two stable facets. Thus changing only that one additional cap cannot solve the fixed-ARC34, fixed-raw-centre-zero problem. Changed source supports, a moved raw centroid, smaller-volume multi-cut bodies, and other finite architectures remain outside the obstruction.

The parent material-side and finite-generation insertion certificates, previously proposed without terminal receipts, were actually executed and passed. Four complete exact A/B audit pairs, both independent nonlinear cap-domain checks, every zero-primitive check, controls, and the global dual/material certificate were rerun in a fresh source-only cold replay and matched their pinned hashes.

The current journal records the completed B023 cold replay and treats H162 as a distinct branch. I did not transfer CAVITY147 labels to H162 or modify the journal.

## 2. Source identity and exact finite definitions

The authoritative parent is `figure-0342`, SHA-256 `dbddcc47d4010d714e5d877174d1cba5261af9a11079e4c73c0536343fe5a21a`. Its literal payload and complete recovery source were read. No conflicting geometry alias was used.

The original B023 table has D=10^12 and 166 integer support rows I_i. Its corrected zero-based row 99 is

`[1319071116910,-112685548427,-1866813004671]`.

The complete table in the inline capsule has canonical compact sorted JSON length 7336 bytes and SHA-256 `c240a5e8398bd2d4daf70ee6e456dd15af3b8b77141ca2e101d09a18d88e0765`. The physical body is always the uniformly filled intersection `I_i·x≤D`, never the material convex hull of the normal points.

### CAVITY147

Delete exactly these original B023 rows:

`C=[12,27,28,29,31,32,36,44,45,72,73,74,79,83,84,119,120,163,164]`.

Keep every other row unchanged in increasing original order. Thus local row j corresponds to `keep[j]`, where `keep=[i for i in range(166) if i not in C]`. Its defining SHA-256 is `1be8e6c7905dc162bac34ed62d1eae357aad5257dfb531eb32f26ee35fd70145`; the original-row-map SHA-256 is `58aec71b1b9001e965826a379d33a5bab59c9cdf28fcbc8c879a56ae9c542f5d`.

The parent correctly distinguishes this 19-row ball-sublevel component from its complete supporting closure. The exposed reference stable supports are original B023 **3,50,75**.

### ARC34 and the rational endpoint JOIN_R12

Append the **34 literal integer root-plane rows** in `DATA.json['new35'][:34]` to CAVITY147. Each has exactly z=D. They are supplied rows 147 through 180. Their complete literal list is contained in the inline capsule, not in an optimizer state or an unavailable archive. Call the resulting filled intersection **R=ARC34**.

Append one more normal, supplied row 181:

`[2173696396495,-531355277705,-1763638292596]`.

Its normalized rational normal is

`c=(2.173696396495,-0.531355277705,-1.763638292596)`.

Define `K0=R∩{x:c·x≤1}` and **JOIN_R12=K0-g0**, where g0 is the exact ordinary-volume centroid of K0.

The arc was discovered as a finite clockwise logarithmic radial sequence in q_z=1, around the complete minor-side closure from original row 50 toward row 3. The **frozen literal integer rows**, not this transcendental description, define the endpoint. They make original row 50 inactive and original row 75 nonstable. All 34 inserted arc rows and the opposite-side cap are active in K0.

Important definition hashes:

| Definition | Bytes | SHA-256 |
|---|---:|---|
| All 35 appended rows | 1569 | `8ff9d4fde2ec17eece0927c456cbf58b85ede1386d00955938e727a0d99eb78b` |
| ARC34, all 181 supplied rows | 8030 | `309a8c4502f718f3bf3cf842c9ed1c1e4bcc30a48b48daf00d2e9afcba4a44e3` |
| ARC34, 155 active rows | 6879 | `17bbbbd4b2d273bfe20e8ae816bac29d8f69d2ff3747d2a34f127b1f44e25461` |
| JOIN, all 182 supplied rows | 8075 | `6ae81bbe3ac64a3954dc00535d5ed4518c7a22e4157eef1f0804ab4a96b60e41` |
| JOIN, 133 active rows | 5908 | `cd338552882a5cb6cbc11ea38a5793520a6dc126bcd95c47e67f70c085241c00` |
| JOIN active-to-supplied map | 467 | `db7b282ceea3bd42ced3e918d6033e8463b4ba10f2bbaefdb5fbb4f16ca38eca` |

The active maps are exact recovery data. Both auditors independently reconstruct the maximal lattice; the finite-domain certificates additionally check **all 182 supplied inequalities**, including inactive ones.

### Edge accounting

The full final chart has N=182 supplied rows and R=44 rows on q_z=1, with all other rows strictly below that plane. Hence

`E≤3N-R-3=499`.

The original 71-edge headroom is allocated to 34 root-plane insertions and one off-plane insertion. This bound allows inactive supplied rows.

At the endpoint only 133 normals are active; the actual protected apex has degree 37 and all other vertices are trivalent. The observed maximal lattice is **228/359/133**. There are 49 inactive supplied inequalities, seven of which still touch the fixed apex. These exact support contacts are not weak equilibria.

Removing the 49 genuinely redundant inequalities leaves the identical endpoint and a smaller continuation chart N=133, R=37, E≤359. It has room, in the corresponding protected-root bound, for 46 additional off-plane normals or 70 additional root-plane normals. This is useful budget arithmetic, not a cancellation claim.

## 3. Exact mass, maximal incidence, and exhaustive mechanics

For a complete outward maximal-polygon fan T, independently reconstructed by either auditor, define

`W=Σ det(X_a,X_b,X_c)`,

`V0=W/6`,

`M0=(1/24)Σ det(X_a,X_b,X_c)(X_a+X_b+X_c)`,

`g0=M0/V0`.

Together with the complete literal normals and exact all-triples reconstruction in the capsule, these finite rational sums specify the exact volume and all raw first moments. Both auditors emit the complete reduced fractions.

For K0, approximately:

`V0=0.43859981899846406`,

`M0=(4.2540969961544474e-15,6.313643745289164e-16,-2.642325548384154e-15)`,

`g0=(9.699267559819365e-15,1.4394998519849534e-15,-6.0244565408573655e-15)`.

M0 is **not exactly zero**. Translating by the actual rational g0 gives JOIN_R12 with all three first moments identically zero and unchanged exact volume V0.

In the common canonical A/B physical-vertex numbering:

- Stable maximal faces: **0 and 132**, supplied supports **3 and 181**, namely original B023 row 3 and the new cap.
- Unstable vertices: **8,149,225,226**. Vertex149 is the raw protected apex `(0,0,1)`.
- Saddle true edges: **[8,15], [159,169], [176,191], [187,210]**.
- Weak face, vertex, edge counts: **0,0,0**.

The stable polygon cycles are

`[148,149,219,221,194,176,191]`,

`[159,169,226,210,187,168,203,207,160,162,225,212,213,198,191,176,224,222,227,172]`.

The cap is a genuine maximal **20-gon**. The complete 133 maximal cycles and all 359 true edges are deterministically reconstructed and emitted by both auditors. No fan diagonal is classified as a polyhedral edge.

The exhaustive census is 2 stable/131 excluded faces, 4 unstable/224 excluded vertices, and 4 saddle/355 excluded true edges. All **1436 individual four-component true-edge primitives**, every face boundary primitive, and all **51,756 ordered distinct-vertex radial primitives** are nonzero at the rational own-centred endpoint.

The new residual closure is explicit:

| Feature | Incident source supports |
|---|---|
| U8 | old66, arc14, arc15 |
| U225 | old54, old124, cap |
| U226 | old30, old132, cap |
| H[8,15] | old66 / arc15 |
| H[159,169] | old129 / cap |
| H[176,191] | old3 / cap |
| H[187,210] | old98 / cap |

The cap collar in cyclic order is

`128–129–132–30–98–96–76–15–89–90–54–124–87–88–52–3–133–130–127–56–128`,

with these numbers in original B023 numbering. Its three saddle interfaces and the separate old66/arc14/arc15 unstable closure cannot be omitted by a successor.

CAVITY147 is now exactly confirmed as **283/428/147**, own **26/63/87**, weak0, volume approximately0.49158180268986945. ARC34 before the opposite cap is exactly **272/425/155**, own **62/90/150**, weak0, volume approximately0.4585034892054464. Its favourable reference-zero mechanics observed during discovery are not its own-centroid mechanics.

## 4. Finite nonlinear ordinary-moment capacity on the actual changed cap

Keep all 181 ARC34 inequalities fixed and vary the entire cap normal:

`K(s)=R∩{x:(c+s)·x≤1}`.

At a cap vertex X_i of K0, let v_i be the exact vector annihilated by its two fixed incident normals and satisfying `c·v_i=1`. Then

`X_i(s)=X_i-v_i(s·X_i)/(1+s·v_i)`.

All other vertices remain fixed. Both certificates cover the actual finite rational displacement, positive denominators, and every supplied support inequality throughout their cubes.

### Implementation A

`normal_cell.py` uses the rank-one vertex formula, exact base contacts, and 192-bit outward dyadic interval arithmetic. It computes the ordinary first-moment derivative from actual moving-face flux:

`D_q M=-∫_(cap)xx^T/|q| dA`.

It proves

`|s|∞≤δ_A=2^-26`, `|y|∞≤μ_A=10^-11`.

For the exact inverse C of the base moment Jacobian, the verified quantities are approximately

`||C||∞=397.75029032322743`,

`||CM0||∞=2.609252459363075e-13`,

`sup||I-C DM(s)||∞≤L_A=1.878172051823862e-5`.

The exact bounds satisfy `||C||∞μ_A+||CM0||∞+L_Aδ_A<δ_A` and `L_A<1`. Therefore `s↦s-C(M(s)-y)` is a contraction of the full cube strictly into itself. **Every ordinary first-moment vector in the stated ball is realized uniquely by an actual filled solid in this cube.**

The domain proof checks **40,771 strict nonincident support numerators** and **725 identically zero supplied-support contacts**. It certifies the complete reference-zero (2,4,4) census and every true-edge primitive throughout the cube. Nine actual parameter states, including all corners, were also integrated by two different complete tetrahedral mass fans with exactly identical volumes and moments.

### Independent implementation B

`normal_cell_B.py` imports no geometry or interval helper from A. It reconstructs moving vertices by **Cramer's rule**, uses **224-bit outward rational interval arithmetic**, and differentiates the **entire tetrahedral first-moment integral by forward automatic differentiation**, independently of A's face-flux derivative.

It treats A's rational inverse merely as an untrusted preconditioner, proving contraction directly from its own full-volume Jacobian enclosure. It separately checks all supplied supports, orthogonal face feet, complete vertex tangent generators, and cross-product edge-cone coefficients.

It proves

`|s|∞≤δ_B=2^-30`, `|y|∞≤μ_B=10^-12`,

with `L_B≤0.0003187084993901115` and the strict cube-mapping inequality. It obtains the same complete (2,4,4) census and no zero face, vertex-generator, or edge primitive.

For the zero-moment root it also proves an enclosure centred at `-CM0` with remainder below approximately `8.318560554487041e-17`. On this refined box it checks **all51,756 ordered distinct-vertex primitives**, none containing zero. Their minimum absolute lower bound is approximately `1.6693060941584598e-14`; this is not advertised as a normalized all-coordinate reserve.

Nonzero requested moments y give auxiliary bodies with actual centroid y/V, not centred endpoints. Only the y=0 member below is asserted to have centroid exactly zero at the unchanged raw origin.

## 5. Finite algebraic endpoint JOIN_ZERO and actual material closure

Let s* be the unique solution of the three exact equations

`Σ_(a,b,c∈T) det(X_a(s),X_b(s),X_c(s))(X_a(s)+X_b(s)+X_c(s))=(0,0,0)`

inside `[-2^-30,2^-30]^3`. The literal base vertices, contacts, fan T and rank-one vectors are completely reconstructed by the capsule. Multiplication by `∏_(cap vertices i)(1+s·v_i)^4` makes these rational equations polynomial; all those denominators are positive in the box.

This finite rational polynomial system and isolating box define a unique real-algebraic s*, not an optimizer prescription or an unquantified limiting construction. Define

`JOIN_ZERO=R∩{x:(c+s*)·x≤1}`.

Both independent finite-domain proofs certify its existence, uniqueness, exact maximal lattice and strict mechanics. Its ordinary centroid and all three first moments are **exactly zero**. It has **228/359/133**, strict own **(2,4,4)**, weak0.

The isolated cap normal is approximately

`(2.173696396495261,-0.5313552777049703,-1.7636382925961113)`.

The decimals are not its definition. Its exact isolating intervals are regenerated in `JOIN_NORMAL_CELL_B.json`.

Its exact volume is the finite algebraic determinant sum `V*=Σdet(X_a(s*),X_b(s*),X_c(s*))/6`. The verified strict enclosure is

`43859981899845050236614329/10^26 < V* < 43859981899845050236614330/10^26`.

Let C147 denote the filled CAVITY147 solid. The two actual disjoint removed regions satisfy

`JOIN_ZERO⊂R⊂C147`,

`M(C147\R)=M_C147-M_R`,

`M(R\JOIN_ZERO)=M_R`.

Their sum is exactly M_C147. Approximately:

| Actual removed region | Volume | Ordinary first-moment vector |
|---|---:|---|
| Complete arc/closure cut C147\R | 0.03307831348442304 | (-0.0059714921768606105,-0.0018654971345236197,0.006304957461573995) |
| Opposite cap R\JOIN_ZERO | 0.019903670206995912 | (0.006251495594319172,-0.000015151845476266756,-0.004559905175986674) |

The opposite cap's positive-x/negative-z moment counteracts the complete closure cut's negative-x/positive-z moment. Its y component is retained in the exact vector equation. These are real filled material regions, not nominal ballast or a rank-only compensation claim.

The large finite removal is certified directly from its endpoint geometry and mass. The small local μ_A capacity concerns residual actuation around that finite endpoint; it is not extrapolated to supply the macroscopic moment.

The body also retains open material beyond old B023 supports44 and83. For example, the exact point

`(89685984597927868216132210113750000,-134692835087669860969802036392500000,-32703267505908224019398941755000000)/326162317446585660580510813681103813`

is `(1-10^-5)` times canonical JOIN vertex223. All supplied JOIN inequalities hold strictly throughout the complete δ_A cube, with slack at least10^-5, while old B023 support44 is violated by more than0.00024778. Thus the construction genuinely retains new cavity material while removing a separate opposite-side region.

## 6. Global single-cut theorem and maximum retained volume

Fix the literal filled ARC34 solid R in its unchanged raw frame and define

`F(q)=∫_R max(0,1-q·x) dx`.

F is convex. Differentiating under the integral, since a cut plane has three-dimensional measure zero, gives

`∇F(q)=-M(R∩{q·x≤1})`.

At an active two-dimensional cut facet,

`∇²F(q)=∫_(cut facet)xx^T/|q| dA`.

This is positive definite: for nonzero a, vanishing of its quadratic form would force an open two-dimensional part of `q·x=1` into the distinct linear plane `a·x=0`, which is impossible.

At q*=c+s*, the first moment vanishes and the cap is an actual20-gon. Thus q* is a strict local minimum of the convex function F and therefore its **unique global minimum and unique stationary point**. Another stationary point would make the joining segment minimizing, contradicting strictness near q*.

Consequently **JOIN_ZERO is the unique positive-volume single-halfspace cut of this fixed R whose ordinary centroid is raw zero**. Every such halfspace can be normalized to q·x≤1, because zero is strictly interior to a full-dimensional convex body at its centroid.

The new cap and original row3 are independently proved stable by **362 exact global support inequalities** throughout the entire δ_A cube. The minimum lower bounds are approximately0.12792622342173732 and1.5236171061763817. Equivalently, each facet foot q_i/|q_i|² satisfies every other supplied halfspace strictly. Thus the unique centred cut is not110.

This closes all finite directions and offsets of **one extra cap at fixed R and fixed raw centre zero**, not merely a local witness forest or a sampled search.

A stronger volume statement follows. For any measurable K⊂R with M(K)=0,

`V(K)=∫_K(1-q*·x)dx≤∫_R max(0,1-q*·x)dx=F(q*)=V*`.

Equality requires the positive part to be retained and the negative part omitted, up to null sets. Hence JOIN_ZERO is the unique maximum-volume zero-centred measurable subset of R. Among closed full-dimensional convex bodies equality means the identical body. Any zero-centred Gömböc contained in this fixed R must discard **strictly more** volume; no uniform positive additional-volume gap is proved.

An entirely rational dual upper certificate is

`F(c)=V0-c·M0`.

For `r=||CM0||∞/(1-L_A)`, the actual Jacobian enclosure proves

`0≤F(c)-V*≤r||M0||_1+(r²/2)Σ_ij sup|DM_ij|`.

The bound is below approximately **3.48412329233285e-27**, yielding the strict volume interval above. `global_dual.py` regenerates the exact rational dual value, error bound, material moments and volume intervals.

**Scope:** this does not exclude a cut with a moved actual raw centroid followed by its own translation; changed ARC34 normals; a different stable or unstable root; material outside R; or smaller-volume subsets using two or more independent cuts. It is not a general E<500 impossibility theorem.

## 7. Parent certificates now completed; secondary finite construction

The parent material-side checker now has an observed complete receipt. For all19 withdrawn rows it constructs exact nonnegative λ_a,λ_b and μ>0 satisfying

`I_i=λ_a I_a+λ_b I_b-μe_y`, `λ_a+λ_b≤1`.

Thus `CAVITY147\B023⊂{y<0}`. It excludes only old-centre containing additions confined to that envelope; this continuation deliberately uses actual removals and a new region.

Both B023 finite-generation insertion certificates also passed: L10/cube1/500 and L11/cube1/2000, each with1320 exact endpoint/corner comparisons. Minimum squared-relative gaps are approximately0.0003671002862806422 and0.0005993672705589183. Their complete618523-byte receipt has SHA-256 `8f406dc3c37ef884f7c1e889130c98b93a8878fc6f71396be091b166d1c51c63`. Their retained-old-support and intended-root hypotheses are not transferred to ARC34/JOIN.

A separate finite offset attempt, **CLOSURE3**, changes only these original B023 support offsets of CAVITY147:

`t50=-46907692120/10^12`, `t1=-22470705426/10^12`, `t75=-60748323207/10^12`,

using `I_i·x≤D(1+t_i)`. It is exactly **276/414/140**, own **(4,2,4)**, weak0. It changes both50/75 closure and real opposite positive-y material through row1 but does not cancel the packet.

Its specified three-offset cube has δ=1/8192 and certified ordinary-moment capacity10^-7, with exact cubic volume and quartic moment polynomials retaining **all mixed terms**. The proof checks39,744 nonincident slacks, complete mechanical primitives and15 actual states by two complete mass integrations; its contraction bound is approximately0.002488255369816602. This secondary family has one complete polynomial implementation with two mass integrations, whereas the main JOIN family has the additional independent Cramer/full-volume-AD proof. Both full endpoint audits, its exact literal parameters and active original-row map are in the main capsule.

## 8. Search evidence and continuation

Discovery included finite complete arcs, actual opposite-cap moment solves, multi-generation polar-escape replacements, affine metrics and coupled supporting/mass repair. Every numerical body was evaluated at its actual uniformly filled volume centroid. No positive residual bar or improved reference-centre count was promoted as cancellation.

After the single-cut obstruction, a distinct two-cut search completed **70 deterministic seeded outer searches**, each with an actual-volume-centroid inner solve for the second cut and a whole physical/polar persistence objective. No numerical own110/E<500 endpoint appeared. This is finite negative evidence, not exclusion of the two-cut family. A second inline capsule below contains every source module called by that search.

The useful next construction must include the **entire new cap20-gon/collar and old66–arc14–arc15 closure together**, and leave the single-cut volume optimum: introduce genuinely independent facets and accept more removal, change the ARC34 support geometry, or permit and recompute a changed raw centroid. The redundant-row-pruned identical endpoint has substantial real edge headroom. Tuning only the existing cap while insisting on raw centroid zero is now exactly closed. C1370 is unimproved and H162 remains the lead's separate direction.

## 9. Verification and artifacts

The four full A/B audit pairs agree on every common field except the deliberately different integration triangulation. They independently reconstruct supporting hulls, contact vertices, maximal polygons, true edges, volume, moments, own centroid and all strong/weak mechanics. The two cap-family implementations additionally use different vertex reconstruction, interval arithmetic, physical differentiation and cone formulas. These are independently executed software implementations within this research, not external peer review or proof-assistant formalization.

Important pinned outputs:

| Output | SHA-256 |
|---|---|
| JOIN_A.json | `6880cd9bb3067e278700ca464c8cc9bef98fafd2e4e4ddb35483a4f9d77bacf5` |
| JOIN_B.json | `0ff39528f45c62d214eff3bd090dae249dc2bf344a2c93fe862db3dde0b92499` |
| JOIN_EXTRA.json | `f8a583c421ac7aa1a885e0f394701886bdd2974877c07c0a8655914dc388486e` |
| JOIN_NORMAL_CELL.json | `761ba1973e6f3ab860b0ca7f7994891cca024cfc47b1114d50b544ec3067f36f` |
| JOIN_NORMAL_CELL_B.json | `c389531e62b0a2a4e7f5af0bbda1470d0193433f210a1ad663b0089c0f062327` |
| JOIN_TWO_STABLES.json | `caac61331fb8b6c0ebeead0dc4fd7c4e87917ab10a49306e9fb7fc63b9e9553f` |
| GLOBAL_DUAL_AND_MATERIAL.json | `c281df7e1518a93bf69d6ce1248acd71da9a754ba258c0da7181639eeccb7bc1` |
| CLOSURE3_MOMENT_CELL.json | `7ca3eafbe72e3310a334b068ee158b68b11789d87fdaa183caa3fb8ddaa66b01` |

All remaining hashes are in the complete EXPECTED.json. Controls include regular tetrahedron, cube, octahedron and a weak tetrahedron; the latter has strict(3,2,3), weak(0,2,2). Four invalid denominator/duplicate inputs are rejected.

A genuinely fresh empty directory was populated solely by decoding the frozen15-source capsule. The entire replay actually completed, rerunning all four A/B pairs, every zero check, parent certificates, controls, both main nonlinear proofs, the secondary polynomial cell and the global material/dual certificate. Every pinned output matched byte-for-byte. The observed terminal marker was

`QW83_FINITE_ARC_OPPOSITE_CAP_FOUR_TWO_AUDIT_BODIES_TWO_INDEPENDENT_NONLINEAR_CELLS_ALL_ZEROS_CONTROLS_GLOBAL_DUAL_SOURCE_ONLY_COLD_NONWINNER_PASS`.

The completed cold transcript is5353 bytes, SHA-256 `3aacd3e34962123b7a54953137bfe9877465910745f02c4f453aec320e0b10f9`. No pending job is being substituted for this receipt.

Compact complete source package and cold receipt (`QW83_FINITE_SOURCE.zip`):120142 bytes, SHA-256 `2940d8ff23f4c32f3e2378fd8644f78bcdea0703b53b1038e429f3c4a8d15393`. Full exact audit and certificate archive (`QW83_FINITE_EXACT.zip`):379300795 bytes, SHA-256 `0adad140a7ee850fc516cc1e1ded70109db34466d0b01afe94308af8e6f80153`; all51 manifest payloads were read back and hashed. Standalone exact recovery (`RECOVER_QW83_FINITE.py`). Extended handoff (`QW83_FINITE_HANDOFF.md`). Numerical discovery source, states and logs (`QW83_FINITE_RESEARCH.zip`). These supplement, rather than replace, the inline defining source below.

## 10. Complete standalone exact source capsule

Exact verification uses only the Python standard library, executed with Python3.13.5. Do not use -O. The map contains **15 complete files,85484 bytes**, SHA-256 `5c57823adbd9cde14f89b3143d5f43249d5dc643be7a6927c91a89c3877938df`.

It contains the complete corrected166-row B023 table, withdrawal, all35 new literal normals, active maps, both full auditors and their independent hull helpers, all-zero inspector, both nonlinear cap proofs, polynomial actuator, two-stable/global-dual checkers, constructor, replay and expected hashes. No optimizer or unprinted endpoint parameter is needed.

Save the following as RECOVER_QW83_FINITE.py, run `python -S RECOVER_QW83_FINITE.py recovered`, then `cd recovered` and `python -S REPLAY.py`.

```python
from pathlib import Path
import base64,lzma,json,hashlib,sys
assert not sys.flags.optimize
B85=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;Z5si5nTX1h=fH_U%qYUpa1v=t1p6*3*4_q3&1XX)vcwPN~Fg&O1S2NF{(KQs)Ry?wb-A#
KB4#OTRmd%v5NOLJ4(EPpbet^XKtl0S;cRNG-w>9P5=WXKJ&yGHtRWV&Q(+0nl~}lgXoRVJTR$<ZNiRil}T0a$=3Q)vl5<Ma`BL0
Vb<h&SHps^s!as-TO?n*QSk>fT*PR@zj&IEi>fv>GR$FMRx3#6tfXx9$x``=0^9}bE)Fhi+ODdaRB(n{-xc^xQnYXQJ~ELZAA;8;
#yxeCqt0Iyy>3XHV>CmrgQ4KJAuWz0xGy-1L4thS`IB+VY_|i07=!WP%A@!2$iD{WfUe|ObQLNOQ-FK@iN9gVhyux^vV*MUyTxpF
_nUp9uN2Q0fd^o(2{7a<W7u;m(_`KUh7Z=wv2K8i{p_P^_3Ro9c5~P^<pN6>Xwh-Q1r`ww-QLC%6C05NCXJx8I#J?R_fGW(?9k0S
9z+qtjc5??nEXO0i4Bwb;iV=ym@$6^$GV}0Ak&2$uvfp`hNi^zX2;IHsiIO}we9~@ABDU_{_=~_vf?GsSG>`*UXugSiR;l?ItSiw
z?I#WB9rA9x;Qjx|834$s&X(H>|@c`%#LO`NZD8y@Og%UcN|Me^#q7RWQ|9=Le32iLxeky9v(W(?K_p62^9YTxxKwH@Ps$A1F8Kz
a7Qd8q(}NM!8I5|cUqMi?}go>uJ~MRRJaJis0cmrJOzNg&aZzT2tS000g2$Lh$Vn=`k`*!L074}ge{$lBBf<rdlbAq@jgW*JJ#0J
4Gv8Mq-<?Bn0choUZ+9o%Yr?9@x(MUIn|B8U3BVeG^!()H3CPOTB5U|l|nn$g_`DX96A=lbWO)!>Sp{*D?eB+u-K}EJys+I)@2-I
%mPJa(4FSk4sRfq=lKYy&a4fF2SZi#A<Lm(z+O+^WozbFaR=0pEg**O{KTBi$r0W<5LM5R@f`c&e4<4ZuiiArT42F;l_2RyFBzid
IREo9xb_B+cBDs(+dK-q-xn8X-Y~c46a86eNkk;uG-^>XMuM@<_Rnd-iR_(WV>4D9DD2BpJ|P5e-0_+zMnMve#smeu6Ioqy!>zFx
;7Q}bnk~efp4YX}9(oxoADnX}J3;92TPO=Bd&b^NKz(BlFh?wI#er}zN5<9tyydc;C7jVf&d}Ig3*Uxx)|*~o;;Rr?@6Zn!10K4t
{@!G*7F)y=H9vd$_`4!Y!W$_7%2;@W=p+mbHuO~Lx~{gZdO=0J+$!lGT2j6MJn{op;O^Qu5tN6&c54}<#i*_v1!|f71GB<pa!ZAQ
ScyW4$SgK7NwUrY>HphUFxD>k5S9OgOR1@o4AKmk1U7Of*Vb1Kqnx{=|ER9!N1ipTuR2CF7?wJ{0vKX)#AYk!vEv4|5F|Bb$5aGP
lUVgMs92;eAQQtjjJFrpHo>=O4*9vygMol04J0}ZbgD}dk4Wi?*rD!XTMzKBgBHG5s*y{`Lj-5Ad?`}EZ#1K_gk%I-VzV`xduY8j
c!w7f!^bHxgmYAko?b4QSm_UylARqo6@2lkMtIztTn?+C`{qi4Dbpy*Z5x3J)s!3<TVREDJ-Qkn&qoA5Z36X|s{@U6et&~rDR5ff
)TwYc?1P`VwKiT+5(tr%%c7~9QF?W|(N?T^mD?l9alewwH%vtm9E$$R2)>9e-r&KSiz8BeUR3@Y#)9U%e70h-ImtGotk>ud^y+g=
J8Uk4w!dc;>m$86M5ZNo#l=s$S*>s;__H94K==hy9&x@)Iw{4}_2Mw@mwKu^J(&(T{-Qbtm241vWj$jCYrJVM@b67pt4Qo$o@BB1
;~(|bhg}`-Y4~sD&~}Ee`05;NigNzC_{A_{V8LiHw1=i~>@~sI#yl8+I=r}oiWXQ|#-acs4ejdr-s$^DCMVE+>f!j=Yo;SwPYy5;
zUw{QZ0|&U1lgl_(IT2pVGSSXY_AO*YbD+$<A7fLr4kiB4GL^3oOYw(NayrW7C_)OU3EAadC{ntcx0hdqezNlN!dOCW*8Jx5@ram
RP^n3p+Qxkx0)(l1-RCMD~}haF<Pzo8<93CXPzR-(IT;fzBZbOG98XE$M)*ZD?Uk>JZRXn1FTx2CU={tU>#de;zet`XvZQG`pl2M
SXFYEsTVwRSn1uUuKnUpk|!x~>EOGHF;Q%x<!CUPLrGXF#1x|WCC?Ph@g+>hOLfBXp#v=ho!7=f4(Nn%eV}8wMF<*i8}>*cb&Kxz
SSD7Zq}(x$4b)AmxM`i*YVV*=%l#nC)d*Lu?#V}Jej;}b<P7<nPj{aWS&~v%_wM@{+$A+9<sO4AIqyuk@Fh3Q-ny5K73!^C+((U4
nh%SCM5@<R+F;^p^MZ|153D5I+NJ7#>_-#*z0ESyx}B~6SQDk|fw5d(#^%jaU#5dFozs3rF%|{CJH0-+5On)6-KT7I>UCG#IEXh0
AebKIMLVvF7%{Tm)8`$Dcb1aN))hI~h6VGFVsuW6p)Y(jwvWly8R0i;LYoj~&Ta1jg*4UNpMhyF(NPJpQSue)o|*{c!=1Y53-L#I
Dih1ieAyZD$BKLL;_W_9lBNXQF^D{w@rrF4_chW(eOImu?8VEyg#y3%KKl6oWLG{cmoJO^7z3}!dwV}Gz?+!&rO2Of2V01{96tyA
VLR%o_-U)j&WE!X+*I7SCd-|BtNIPP*d%$GXGAsfY5ni1RdT%`3nlClBp}P{)J(^KS#RZZjvhdS-;Gvt7*Ul;7&CSyeM}vpRbT?x
O10^VG{<6YH5?aP>E9%XP3!zG<||v(d9Iv4)=6$SZ>=fIWeMEE#2$LRWO@#klW?o~feo%_rs<0}wY9R=-rm4!dtO6NVY-#j;a0KI
N3lOZZ^B>gxKAXumfeGPDR#$OtFzFddlGGq<vck~AfwfpV;VKP5j<*^@Ifc3gZSA$EMw?ChE><yIE_3rip4$_sw_ZT+8`lF;kg|c
Ye&`2=m*gu?HC&@X<`6y;*Cd4gkJ(ve;@Q2Z~aJiKL7rws@uc54^l%xTn^wAGT1DyBsn2)cNds~po95Eb&Jpb;Ewd%M<-ImBOvl4
Ta!2sA8s%uixT?sww8BIC}AMCV8*?9<gPO1qvo-UR(*;>wFyd2?ORkUSD(Phh~k5mDvl9`RENw{Xi~f5KI7$9J$+XdWuP=mObXm4
8FXs3*XJhJ;=%ohT=GET<RG49evgwP)?U}+N{b&ja0ZLUiwVQ|z?AE7*SsS?v5%RE#)wf(AqYNp5!ox&Z_pDsaCMra6}yd*Ger}v
FR5Gov=m$&o&^!eBT;pDFIU=2Epx)_wWz!3#>1oOoY_rGw4b~Zr)$SGh*l@JG$wAdoJ|e9!R7+-PtWoM(J0cyrx`BM7#-T{eaIf8
D1*1687Z-2Iz^01>GQUr-QazQj51J?c6j%9BXlbS5_%lVzB+58;|qU1#$d*61n0u(h@_8V+PSX;n34xp>2gTMc|lOsOKSTTG~AOY
yj5J-S(RZ-Z3UU%N}&FA;GV7mVC8dhI85&sB2u;e-?v!FvJI1OyI>(dc$Modie`Cde(RU5tW9Nsuhjg>mqp-50?b0|%}e8#0`pQb
Yuk_B$G%WP3CD6TYfge<fV{cMj_#pMGeZQ;cak}ZKHruL!l+oy!pQ4F3Zm|oooVn%!U8jlZ;XQ}xP<4i#2nX0Jk!3VP>!i)gE)ba
eNMrzNB@G-%7O;lnTH(tAn$c5ZH8JIZsfhn$g}_Msdya9SjM^^sieaV26|O<2+d8|vqGTtHWXqLNTocpbn&UCva><)NW)D?pzQK+
@CJ(GK;qw{d`8*$^dP`sNX^{Hj@PPTG_qIOC=!-ICWAb&w_B-J4)U0Op>jEAk=<lOBS8qh*Y@=!uJi8=(FYcFtbs#S`)aRc%yObd
`PRT5o)<T~KVj5kqm4<3{FA(p{1~S^_<u(O-Sj<zdF&oEI(!o<kd4f2safeIO<p_{e2UyP&m9v6T|u_{?t(dFwHr~A;{7uU_tB$)
W6c^+GBcP^?PT~gk%}b#KQT>jk7MZ{6-5Awb-FPqHbu-N?8U!Xvu%assLXOlS`D8EuUsX?sAOdH%&)yQj4nb}MROxYfwQ(!y8wq9
KU*9bH>YsM()f){9;V9?3q&hPRELN{JJ7wV|A@UikQzW?=aHohvlXB5pz4ub-%({Kww3%_nQ~{!bO5?J0*6t_@(Oq5Wi1P9^R<5t
9zOKFVQI(eVjrBtSC4>GE!o6*V>0knvYmPnmqHMyv%TB%=pibgXI~H@z<~?8PnE(0Qa{4_HAhl1j86OHg0Y~)II(mZUA`wGFDBt8
yLsLj^P*+r9Lacb(NvaW&u3M`l|Fr$fswNWos428ckG@F;8e}q7r;<^m;4f(0)2=VI9V<awghkAYHSksEakGFJ-)uD&w6k|iJC#D
X|<^LH*`OmSlZ%p=hCzvD1mT$Fi&>a3v#qS;b4Mad9adXpR>!1gP+WzqVBBe6y|O+pu7}NNjofTiCYlF=BcN%2PYP2KWz%M3)R&G
siz31v=RyTvx2f#@2s87#Om`uNR!uT>4GO+S2Tu3GO=e|ffNYWn(~Zg`_-J2JhH`-7KAw%v)L_z>p2EVO*4<J0d!sF{S^AGJ$D|4
ohn_UFpGTHNpY~tDUE0njD$v*0RjRu$e07sO;5gTz0uw6ixhv{iPj-GY(CK)U0Uk5ZTm{y{l;~ulr84?8T|Bam?C+QUxw-amtw;`
+`%p#9kd8z`Z@Rlu4S#(|MgUli;Q*U{zI)wtiToVn4gO$Q9)>*F3HFg*^pL3pT+Tz&Cb^a@r&Rq=);hq76{R@Nha1Y@cwdK9KCdd
(+!c|*(CXHfAM!Z*gkS)D*b5G0Q62*-dI%Rm$%~B6<mY0h(;ERvuNQ@k`$M!eP?cLAS*|si1c#+QEZOwqF?LisD=q<$I)+=y~WC9
Q=+QQDW4-3iWBXX{euG0XH5_dV+gVKHrn*GfpW3eZyy|1IjWk_G{9xW+{V;KNT%MZ!Td5VHU?~&L|ZQJx9R3<vWg*U20ex~#d^0~
6uV5XDd*u<Uq2Qj9cQ6l%*ZIxx&2Z*!$_$dU{aZe8nexKA(3-m2yjZ(UHI43ngqkJu@U(4W%nnw0#j=|C#Lu}c4DF<M|>*l{q<4N
os#>lxRC@%m@J%QL!FXD#%4rqZFUW<<geKmL`rBeHUHYEz+0wZ9<9z;jS9m*W5ohvrfx0JOVAxB)p`<&CVoz3`%!^jeF|aE+1)~$
0t6KFjuQKln0A0#zLO(k(@mO~tlr^vT_sPiL5Mz!%6#P&Lw-p|xBfP1ZEQP;4Qy^vmvgG6yzDK6BqeVoTW!f)TW{{TlpT53v5S1@
|6l$nHMj=$%nSr#n!;+jL&Kyw$IzpC=T$dGq1Xsl+Ufm$7e?KC7N9<KW3Duuln_l6{hkXeCud0~Ma{1z=@#E1QRnqmuvlu?umjYq
j!6##OmbAI>Koi%HPt#W*1(|Yy<25GJA!P+W}%~QoW1TkJ0WK~O1z%sfh<RUz3@|`8x6qpV>{#Y0WN}_I~h`eI}73m*EDF$TTLJ0
=gmO4G&})qugGuOCHrAq)<PoEoagw3w8tW&xrx68b~xu=HhzzM`1GR8^el&nmt{b#jwX`Pcw97B;c0%+x5OxtMH+w1?&8ojpcQMm
nI<zVX~cIZpD2^&Ch@CY86FJ9uvvCFhux?Tp14)ZGAr5qEB`f`C)v+pyN%I`h%UC?jZL{ak4k-;(=y=(-Iq0{)af-TCalbhX-?OD
O7(5s2+`hlGt&HK<rKQla6*M7jaq!aQ%u#aY=zfB!}IZZLI<S6!BEo#|JrN<I4KmxB-7nYWHJDMfF?LoG?96NqJBY|DnK+E?yN@`
f+8=^e_8$CB5D6d7A#IXJlTpMZk*0KKr#*|DzyaBZvDk{e6>+Gj?ceXw}7S0p)ydj%R>F>2M2)m<+DoA*b27ei3*Bp4F1Es?QF#j
zJ7+e?hkIs7x)Fx=*?%EO1nLJ8((^l5b<RthBZNXoEeI5Mb)=DiY-eY2<aSQPRU^$$MDG3aVTBr#ADC$){GQy_roc;g8U~%)h7S-
R~ABp3doaes%2*v7mMypNT~cLQ;_ge`nuuDM$c(*C1mBzKY@8HvbdGxaqeK2!48|sGc7p$IP#}$Rev-N`N)&T-hPRXb;QJ0+@Z91
?8&>9Rh2!k+8PGEPjT|K@dD2ZZ)(=j<-C#$^g_6VW&?YQy#`%(f6tjOPV>8yM+;=f^px8**evGbU^KADF>5TsRkS-AHc$wh3G=CU
lXTZ>A3FCcbpYB}2@<#%)6hETnS5PwIe6cdQ_-U{EjKCn($)I*hOARtcA?$Mb{W)7+yL`He17m|tupHJ{26ThQ2UfiIp^13jfbV(
sS$8t+}@nd-_}AON%LWS`HJFx6atU;0Y(4I+NkA?2T{ygiKjfhZ^zW?9Z>=4p`P_H(6gK?i=^F%?9|0MgyFin<s8f|V(N-*Bc(}Q
Sg(qAZN<AyQ%6nk_?aJ*M9ubtdQNT7VsPxP$o1TbGZBtn{<I>}n^%ypF7)s`7}48}1SJ~ZV$H#^o~Z^X`foe>{#E5(9{=zP{Kp6b
uDN$$8hYAbs8baEq%Hib3VO-7g|tIiDT;e53j<mq`rGn>5Vxnx!mCmQ3%U=(GqmVfSFnkuVd<SYlQAt5Fy351&7>3J2w)*=mQ~0k
KXvNJd&>jv&~0-S*kBNqNX<;kvdoMphs9)35-I>UNeU8$?0P8YjUY`rY<4}R#r1$EcNEggs{*OmR0`DZkMYukzgBZ~sOrI^-}i3$
IXT~gZYy0OjbayU-Hgv6zyH)^1Qk%HFFvDC54DUt<%0hvf>8chCG5KRX-f~*6W1{FAf9t`GIgvbw&+*w>^8<gtWogi84QGsz66mh
>z~G2u+PqOP#B-1D*-jDnj)`|HQ*}4&s9ON)vDTV|8=MaAPSyGl?z398-d;PoLdRxr$(X5T^I8vDifXZh{Gyr?-Bk)3gG!EwOn~E
>6jM2oKUb*ID5to9xEt;2s*#h+FZVF?oijA6bA#$l%34$H%h&(pRy@qvRjQsSBabo7-!~<C{pg4R(B^|)XPkrZw~994Z)M_N`wx?
vLK?Jaz8VfXF<9d9s6cljpkoMETcI(U{QLQQ8(~82PpC;7NU#-3GJJwK+}DF4V|{V0nsvwB0jH6&WI}CwzVZq?&sW`z<G88Rq(Vm
&fOytnItjR^s>>}!oKyJls<qbVJnsd_mU$QHd&*i#u|Hzrgz+I$o<M1E#IL21%`2r`_B9D>OZXJYKYcrEI@Ynyt^P8NuYdVJwR+%
fn;?(;*DGM*g!&sox8MwUPB<EVOdLZlIXcmhQRfZk2I|kFF@16v0AB=Te4gppdXzV@<TZeZ~P_8(z|vqpZK!5ORWw09bvr5gZP}_
S&n1xt1-Me94A|a7Lx&{^bb$j)E62A7=@D_NFgS4h`|jP<Y#fv&YFx@9K%K}cxYt@D(GDw*&irFZ7Kc+e80!BnSt4f+4dkyUQmT~
+5w4GWKG=c3YfeU72g(qXX;6=3Ao-0*USq-xzMQF$&q>nryg&CcraPq@V)=C5oK6~xsB05!Mv!YFs~R5kDql@xwM#UMPbqWGz5;$
iDD^%@oe@Kl-d^A{>b>vm(F2pr^YkPY|ni}r)n`_;+lG}dBKb5$R#O5+BI=4l@eR{o=|sMH{UmnyDfvF8$_OL&BQDqvV;F{QZgml
e@daV;TfQrr5iE1<jVH$3nwl>d2%;LVo#WQkjvq*?T5-N@6>u@xa12R=Dm4(kxa})2~~D`gx^!}$!<XkEQc}~0J61oVb*R}XdPZ^
fvhU;f6LloC*V%ITo!<SZsUh<rjbi-vO&A7AJ(Zp-F`vkf)IvPGAtO4<d3a-?;wHSFZ&MU#`FIU<wBdas`}wm#!yQu+H%?g=57*C
!2rRdioz<}X4TNNbM8J1a>>_sRL*)Ax%2S^MsR;~-GmoXnsX+iM_7%`d6dK<Fpl9OEZd@Tad^VhMl}3R@A3Eo3&O(8>9xuUis9oX
!y9ju+3TS6P|Z_(ed%X0qoql_WH{;59Gc+8p@sYaj15QpY%pw~bNf0nXtlc*0o6enkd(+G$;yZs34VqinK#U|z&vT?3J*ED{$fwb
j3cr`vLk>geoh;q?FgSae*oxp0NE&gkBd=y?;177uu}7y8+_&WvAkfl6&g+TTG7w%rkp)&?2ci!GB15G7cz#S_mJRe7j0<VT|+J-
RwPQmH<};1N4OItS7MeUo#5A2;cjkquxVqqJ64wwt?~I9lc+RYY~oC1e}n{vx`6w#FLrp?fmyUp9O#6CE8Q|viyIruy<4v6gQ@A-
49QaBeBqo~utdK+sM^p3g%UY7B^A?0eT3F0rh(0dxEfmyY-Rq|LHxVkFW65!evMnYrN*}$ffdk&%XfxSa#0fhRZCE@VIbe*C<;7D
gsX$fL^&$MIfgGaKyAZ{xE|~Tb$nO~@xpZzUW?&dNBnYg`+<Vp(OlQ+w8K35nm_cO$~f8?F-1|Q{yyzFQ}<>k)3J8T<Zy*)slAp<
z06+cU$Ai+Nd?b9-+!lk0tX#`t=BuZ`p{oT#8$_=DYwc_n)PMJ%o@QdDORb!vTOD0Ab(Onvg{~uy9fmvJyNNPO1OQ=#jL3K{Rz<f
HX@H$CVDAjTTGX+hwBDQxS0bLl3i<e^>Z)I$h(&nhu5!znM^DwX61QqM$!O=D|qRYcl0XpR^r6WLjp`C;!5z0Zr!AkG(;*hWrD17
lqUo6J{zlf=hLTF*$8cxr++#$zD#p2{#H)*M_YCd*pT=ak^0xMqd(BC^K_sQ3nS&pOTu?%&w!8Ik5RniC!aP$Yj`UmtV(|NW?UWi
9uk!Y<eJuKEx#nV%ah$_)2za7N~}?k9z0=|PJ{uV_N{+ou8tqg@O^Y61^uLL1CdO(Z61WKk`W6pn4;`^s0MI-7j#fi&-?lJcKvCp
Vw;3vu*hxZzQw7H&9b*Oga#gW5X*AtGQ}DR_*(5;00^ms-g2++07fUi`~1PRDv*i=wy`<ArwguU9?b?jSUow8>F*|yXbYP4RzVR4
S|0ChVSJ6Vu43PQhO=vAhlD%OacfJ8RfYwEXiE<RR0Y<J@U=JlZmVu~B=H=K?43@jBG=uId6@A%?iE#|w)lJwZ!%Ls64gYI?RvBg
w|u9aD?k$<k!%Ta9*bl;lUw^sP8|=4wRWbIu7hdL{U<b?2{1k8*)E})FA@6opirC)lUMuu$j|-m(6RlLY5fR=P!qrAk;GSqRY&t+
J*E>Q;tvp<kCkG|iR@yJ*_#nXUgG%57z6uZf|5te!RVxch=z^o9!}b7105Q7{mM51S+o-s*RgqWW~UyPf(_ZrlFzGMyGsS%1PncA
ZKcUf?s0eUfQ8{ZE=}h4&(v^r{cqDWXglGz;ee|kkBB|uEd_O~adTzt{flDzz3iuQ)b-*)V+71ChenHQx`z2OP@VnXV?0<d<1ooY
Y7lD^DjA5I;Wk1j0Rb%hXYb2#Am2|kdA2ws{YRD&kkm|PcNx%{z}1ng)^vid<Qv?*cWac*mn_X|pjC&o?T;tNv|~fiv`O5b&hPQs
p*60eM_)<Va4uhJ5wmz62I?|bRUO|9Kn`gZK{EW)7Ur=Pw;Y%K&GVqgD)2v^JlfA_n}ZzW;=}$!Xq#{kiob&|t;JmM#gtciiJ=5k
RF2i_z_lrQm$h_`@;XKcd=*BlV_-Cm_59&C=iGK$y9X=y4??q@Zkb5X>tFn>g1XIdi7+9oQ{YCH0Ui;y?dNq2H#25Jv?2;X%PU%u
o{-YwH`>?Z;OI-hno4l^WZKVy8K-lO(&<sq;c=fwcT4BnOUYOQRkhA#zQq^p(r)dJBO8%xaA=#PSK!2CoaDhNz^2=%?unHBrV_eV
d{C2)p3T8wdWYK8cf7%U*@b2E^7x@|5Ph%yFZ*Pb_N76rM6xwzrKWpp32E232lk8B>NaYTb+Te{Pkab5yIiDi`rpqtXE^pwrF6R#
N&#9TmQvThg%%vJcxP{nTT6pg)7&J7y_qxANt9%u{PfZqP}2_)o!OX@k$K-@NeA<rp#uo|U!vr)@Cx^N1>6~aOA59$<qpo3qal@t
QD@lfPcqEM+np-{No1A#Fts#zHM#CaTtnO6OI4#<VsSH6HdF+<&yVSu=gV_WlG4bLTyWBbw%vEopd`qSNuRJyn)bi5)AYL{%G**?
W`JC-*jPuwDM>fD^B7lN5}7b-l0+&Z*$vT-cnHnwg0D3nPPoeh?a?u|Ndp-dfP?;dR_L#ODd*B?MVvKc7px2+jK=+>NW3vjL82i<
`HA?>oQ123vEywcn!UW5$<=Fr7aNTiypy`zKnwZzcXZ3+2L-)OjDv=F_^UJel;n$k5Xs*|F=d=5xlSicNBa&Nw=F;0kmjTDIGHk<
ZQ%zUZ#76@5$$gZFDPC<1z+usTA_|r@6}7msS$F4t@aT1{C30R@=+Em-4X2~%oJH0lhKFasIUo=cAe_MorprOi}6U#5EU2hFjv5o
Sd95bh4n)55nOC}qIz(m^f`}h6^2|DBaT$TQKU+%Y+U}$al$bvi|WZSE~hy=^R2={tRfPj6S){YQXQxj<g(3@Bn*OMVogBFHu$n8
Pl=4&e;Z$s%Tp~&hcXW1;sgnF@kFgqnjpNb&5yVjk$MG)dt-cfhUl&s%2xAio5GAiluz_MU?d6V-qb88n)YH99AVxi3ppc1NJDwW
Chr_rrBl$3mQvohfU_)uv&pMqpr+kxPWp5ejx+<+(1q;3>!rV$pnXVQ3zGY=WH=F>!FHQ5y+sbK6EUEi7ai}b_6THXddxAqIlR9P
JE1qMc@pC5xSXEUe#vW+>IVu+ePT#CZ%g_-Fv#&7WJ;)mz9OgMSfy#CWEnk`J9p><XBCov;)c!Y`bsyy-rUf6nfqIB`G#Qrd2Rt&
7LI`v%saN3o<W%TpwgUqSPJc^ZUK8?3@?*0O;H1iD1xvN<YJDQKptD9aWAMJl%gcP(B(oS)nxY;!YY;T4)ec7GwR5Mi`k6l`(zNw
a`roiu+4;%JVq)vr9^V``#~TchFc!xV?5=xgERn!&7)YYBz=DK19m*U#WZdbX{s><arj)rMLMj(7Fus;Q1c`kl)l5X>0dI+8&<g>
yHwzAmy=6qlkNH@W{N7(<7PC;<H|-ucs<oo>zad_?Taa%WtZ#0BF$*q;oTHJ)*AS}%)srL`He80=cU>zCqlc(K)CvI&ZOSRI<SFy
0_EX}xI^X;eZz4V)gcj6hcge9efDI+yEmJj_wVsEMm!Yb0Za?ZU~b2^u=`434&0fOb=gk|#b=uM7D@Ra18-TGsHZ!h3}~sO4Ifyl
u^WF{@M}qFE^@|pJxj~ZcXm^LWPW+l+7HI8)OSAuexGl_*Z%I+bxjTn_jcJQaO#S^?@taM4`c?x4OSb_*X!t%WGCai&nJNxJ@N}~
u1Z(Lbbq%j8%5C9Y12i(xW(F=A=8!Q?kuceFA?<K3E<IcVk@J40md-a$P<2s$jqufQ9=mj#4?`I^4Ncr<+ffnja&r{%+eY~sTiE&
kecl!vTpH4RKfiN<}n>l%5?7*ujI`q*hgpQ*p28lkS)6>K)`9${md@SZ)=t51%MqGIm=)n8u<<UnoA$NhuCN{_7TCH`X%@EoT^OM
@rFyILY7E$=e3ENu^=S2u6n7a22NgeH<t+KTQOg94CxsM`i0(3;8{O0oWx_X&z-&odo|uo2#a`qDml+v;>2F}n6JXDI$mt-JomYq
c;zVxuUX%S$ox5Ymq?g!%-8zFuI1Y|M+fsFsSDBnPtE?0u)i8SxnG|oYGg{Je+IM+C@4%qNU8e?W_bkdfa8}0$e{^pEfxxN&Ea30
K&tam<h^FVrYdJ*s+-V|W}bgz{q}sB`;;R@7IDJfawu}lR>2e`;&VMG*#W~2>G3LmQYW09O7m0qq1d0C%MhZXe+cL#yTU0I@5V~=
v#xxT3DDV7!So32B3q7RMq18%|G9W+XY^(BJwLB6gsMkI+-0Q`r__U>@|`P3c7XfZzq(-dnUU^~Y;YDLT-FS8bdb>mrqKa=CCvbS
iKT}O58D&5xVX6$r~gO$iSoYLU>$!d>n2rA30l8;5b+$41Iq4iQTxqDwkW!bv_--+JNfmOg-HI!?_7u=<muQjcAz?qX9Rdv!Q490
3xd;A?z5ljkXS8eFH}b!-9HD+h}Avm;YJ%n4e=BIl~XOPWDg9DSl*K9W_vq3^m5(L0N+Hv#9Qaw3Bi+-2_XbPp2cO7?*qxaX-^w4
<FobtzjPh8iri=%Zag@uNQq3gY=gHL;E`3?&ZB&GlB5=R036hJjI%%2`K#IEeDvmi!`;a!;ql-P^T;Xt*}z;r-&!b3=UN{}vfI}k
Lm$XxMrg_&V><0!^9%om7WG^^+a%&Tvfl1>Wq@YAjwl`W9SW&5O+PpLlZ8W_(d83$?nmiK2IWf0VMa^B=LPHkB6GSYmEz9cT8G$h
#UC&1Q*Z6W`!fORN0^ve)mm`4ToTtpxyrz%Aw$Bugzv9dB=wxeJgXT$*xGk?sok^1VNPXe3CVc;@_tJ?v^LB3Qr=D1;97D4m+Rpa
J|0W~@ta<(*deJm%kaDXQ<$e5n4yjlw1~*3Qf;u2N_p>3N{=98$-FXt13L;g*TGjSAG8MCIAr56EX|8xzmW7C_lC7A)P0t%y2}oa
8o$06eM2$7ZNbpG?|;x4sBzF`rXY1}^jT{$G}fv-C<HJ!c2=_zZYHO4@FX_j4e?0?uy^!<a_8JM&Xo41|9<{p{!7}5b)S}?`=(|!
)uC)!z0>?G>c>;i85!F5$Wy?LGXaKQ8#M7^AZj-8eyyz%h?X=PDflsUgqbcVTvUu05vdJX;I}u4aBk(a1913lk9##UKd!rcN5@%Y
rEAC`B@#^vs`Sl1ax$aCqGXlg#?i3D(^H$tdhzswHFB9jmMpHxZpKw?<kNAOQSS+qh`&{kOZjSQmM>fkQz^z5k9k-Tn^++~c0#s7
rq$*9dbPZQ#{{SfoW2%O-Xai&&lGZ2_EH9s>rRFYgXR?)-I4}!q;D1_I_D0OFDK#`y62jA$NXWz{NW{hzztVm^sjK_?ZOfA-We}G
?%qHjHu6mKywuzLUsMO9)oYXQdr=5XXGu0;85-!fIubRW$BPa{vg86nR=3gLl;${C5&~}gme|M^0C-RG5JguO_+oMK^Y2nMa@dk3
y0Jy>QS-*RKR4WP3ddKEN~)=^2|1fF!dO&mzYQWdh&NQ<&r@{h6v9+u3jlrICL8lCosi#Y*6%$c$`k?51$%p|2yBkUNM5}lXX)+|
1Fzb;@x8FhBSJ!J2Cd_E16cRwiKm}dP=Q1K_H@7(0CK<x>kwGsKsf`&#|f~DYL4h-*l(zTvc8G9#q>c~8^uvy?V17nCNtrx$3X$<
F|oyA!&!9$5>}N$4cf$!YeesDo~<-Vm~cfJ9WM8IJoWu}_=<!IUGjL=aSxX)=qTHVz)I(jJdf6#F~xXkXrMq`%V|IaS9otI?=xTZ
&@y2PhVH@sr#9^jTsC|1aHviL@U1J5E+_<CWR9`RJX^AIKVKEU9rR~5WLPim_#fy!A_yiEQG9=qQm2wnXW#pekiS$aCitrVtMZ<g
hnEl6(bWADRNT7<GNmaLWf5{xyeiq_;JF@!4h8VaFE8Iz(sT9}awPEJ<Ze0$@d~JxN27lI<jou!{afglXDlPHROH=#@v91HIQ+Cn
E@rEhlson2kik|-@i%+TsJ?_@w7-(ivR>*pghCPfw9@FW5H@*%Y1?rVWNv;CV$d(`g^7$p#xIND2@nG7R#VwpCk!+fuW>~#4|z@)
a^w2nCXF6p36^a}H-gO^F5o#Xe>A+Yo7WaLko1rd#8n-PYIel;?<6e|070V3tu1F9K7qtRUGuqZTQl4d4~}qEs5>kJ&CFzbK60wf
eYLO+HvJCJ3f5!mO|<uzo$L=|_{6sT9O_01+1q7k&Qe6u05U)?20h>H&O!;+&Q*DLSc+j?cBncm-ylHB;^c$JiQV5uRikm7zO6qg
RF{d};cTM-ejq_im~yR20pS#cP;UX4Y`#M;FjAv&$i1LBIHOG^t(h(Q49e)}phS?nWXbQhhB3Sqfi_fB2@AMf9Hq}36TSep-R&g|
zoDX3N5*64!^jOcgcSwR)tq(HGq+=0;}f>QgZh7M6AXD?59O5EZ)o{y-!h<t!-<LmlWc!t>1Sk!0X=Rf59fL2;1%IlmR7qzUc<xA
3aT^hT{~XCq&2h3(hv^+XGN=UYq2R)=L@+`#-)wadt40lGYiBH4X<Y@6^`V8v|;8z$G_xG=OCL6A~<9N96?9?7gs-1fSN(yts97N
ie~tKuK;J=+X&O934opUWXAqG$u>f<lruU$hQ5_%A;-gypEm)f{2U;DmV~s713F$5rDinW*O@-4EPzslUd7rBg1FvS4I(GxP$MJJ
0fnZxS=s(+)JPlm@>GMnM)cz>Vgh#v56hp<8We3d91Y!@j^9dvcvYGlaCm%>0&&NocP?ap>dXf@f|(pAl1a`Sww*L`BtOJ$m0u#q
XmD56aC713*I8|i-JQfd)1^NNK@zz!`U{y4F-c{E#v|ZBxy9VZtvLa&&arwF@&}~^@f?TV!fXnF9#IF{nQvyn#tsj8=o&;gY#A{)
`fjsKM|%T%{!sKdv+@A$<%uxr34jF`8l>g2#`qWv^9=cL&RBT-q)|pE?jPG70Z7!Efc@H}cbrXrQftJI6}S0PQ_sg8g$M=A=%Erx
HAv^L`BquByrYN!EtRnF1La7rENNCjqS6@3_=Y%4^_UL=Bgt2Q&l6ND53;j{tHqfaNq!B4P)HR{5Pak}P7)qq+mzm!LtMI-C630M
pt7vU8;KwPj;1GDl^wi}o?pSL=Wz9x`JJ~sVaIH-ww$7T6?lnIs+=t+Pb%L`E&Ijp-W;>kuL@hmCAys*!?Ij?YK_4Rz@$A(ZN&F@
M^yeG`U$)Hb?Ua$zM=y9(UulBl;II<wnrE{kvN1bD7?=D<{WD4*}n`fC#MO1{T?6z147WQ3A84y%xsit0xu{(#QP-e&dl-pumL|w
*4;m0Lvxb)V$QkSq-A<oOJQE8$oJS4S-k6l!gT_Oy3<gXrE;J<UY(Z~`oUgSixK}qS>h$`lARd|&?WYpUG7?pxo<#on)7k<v9yKF
7MZp~49wz`W0QM1=`?&gSMRB$t>Lii`g-ifIbEUOAhI%sVee4KP<=d8GRLfPhit*0Sgs$k2VX6lf<$I-5<bZON5i6)SI$WN%nVm8
t7?~%O#)M(IxdK6gGG2CSV`}pX+RUV{h)Z!^0mUllaO2jq8y%eXJ7^O2ArBSU3}gAUTFujQSCp2Z)_AVDhJ_(6nNM2J?5TLvA|Uj
M}(Lo3nWb+6O&1Ujm|mt7IICz5j=a815}$eG4KSJriW)`>1Yh5n@0i(UIFjhRXq;$?3ZC~NwEc<y=AQ4hTq6LDOe|*WopS;6RB#y
=YpfUS#tz*&#C$@?1{}2k<uw#=Gv|1(|Io2o>XG-hH4URw5PsD;NLCC03o(sNsv9w&)8+OfAn^$NF%M<Ie41T#Y8Ot34Z|Mo$p_`
LyDAH5^H<{qt;{=7M)G+pl9|sfvwEgS>#>S*z4BMIO|PPRDHBY&-kjJsT!C!B78C{sGzao<bGJb-S>!n7ilgGwQ+OjA2j@*l7+5Q
VCGh&od&50HPEn5x;aRqa1l)Jza`bqc7+A8V^)$+q^&@Jq_+F1y2|Ea3a~TCw)I`mx_Y0ZBtC>vGd8j7kYUk{Tv{51a#^{sdae|l
^{dan5;YxRDXulXzd;EYkl2fo&HLC#BUiS)_CtIbVY}Q`Imb57vq)C1jM5Zd>4y)M_GFrunh?}Nb0xR7u}eiH6B3Yw`|Mv%Q222W
4Gzo?RR9)sHx+Pua$R`%h;(Z|Ii9qcM8iM?3!<Jl=C!P0KS=Sy<B{S8C?ZCsZS)7&o+N4U6Gs8B^;BDgr{h!kiFBVv<WlF~yts*c
K+FqW-24Bk-uNBfFbI6XaXJ4Y_V;+D4lPq}d__jGV?xW58`r{X$B=zC*22{97iiCHOt-+1=DV-$r4YXdBf?U7XoD{A2nE=93#DzA
GZpq8{z3A^(2FqCy$*$4RzAZ>*^h3FPkM*1`DuCo)s&+SRmz}u3yc^)i8IsNm`05Z_r~l*skX=&gD-5(5DEu5dp7{0-2zMX{;Sr@
-P8HojagupbsrJ$>Wc1TmDIzlF%8GD_4d0MaQ#B5%2{l<mUFP$lIsEV?GkbI_=+k3Z!i~{^eY}`kBh;^IWhXZKiN@h;YQ%(E)AgY
@0FpjN{Gg&<j>0*@R60x5h>UXQj5I^3@pQ}>!_si3n5&yS6&z(zIBw)4c)?2nl4K^W{L`p9rmY8?O7!p+ML;XO}?DBJwKL{FZN_<
R-D$LHs80r^*9Epm6VYrI=2g)xeQhU%p+=bCl)ej<!c}(%Su-cp<!(3F~-gW0_c``w3tQ!nUoro&c|U#O}DVb=_h=oc?nwW4I3_t
>%V>YgqVWEd_$E*cZP_{l}_#TTPhz}D8Rt8UN)8@f_4Yq2BPEeol;u*pZv0tDt(I}P0gfIw-aMeWdF$}q?M>8zYf4aL2S0TO}Pg`
161J?H3`y;>H&;_`O=hY(vSszPV%7swO40B!KtH>u$Y_<zLQp^KwKG9B%t61<K^l0TupjEyQ33C=wO)`1r92^If||v2eb`?V+}S&
2mql&Qc!6OB>R?k=+tsb%|R1<?i8Jn$u;kkD|h~KWIp2=fzyw7_BD?NT9uKXy0`k2FIlcy-{ec(fS3;n#vIKh7d>_ZyHU4*a7ED$
h?d<Pzr3zR$tMW6WDNlFS$XVf;oR|?!ehw`7Z93H)&O-%lvN$7<4^-|e5`;%K<;vDDCN@%QfEH(ZiN`T9VZLCc$&is+duUhRMC+D
=7hl)*@Md;mTxWncr!$;{q3oUXR7RS(AG_UOy6*|281r5P7P*<Lho;rjC4WJV3Sud3s8*|vAmOpyyqOy?>@KfLbzlSH#Fm$wM!<Y
BHawmD+QzYVzLU;{IZyxfKoxzj#v~>KX{GW&3x)~H)3$r`bHOxP3ifjRaRT=0&ik|_M~OBC3HMY@Ova>rNf3m7S;1$m8Z;J%s06t
s@GZ67cS`gm3=p=dzEUIEJn%PY?jRxV?RwV8NU(=<r-_*K=lXXFy~W7&6pFS$`T4UZK|_c>qbuweMt&ti%m6X+X5qUYg1WVMku%d
d}zePeF@koKZ%%IlA&kq1vN|t^6VD+$bJpx;u)GJ!Qa!i+qAOziEm3&H_~?One=9V`;+d_GhfmDRB5K#TKqQjA%&S%{u6LPGvWOe
v*5zS<c#@SM{9Ge=kQGxfA*Bv4N5;UuROF=DBKnm?81StT^BYwPntB1QDf1g&7dmm0cww-&L6j=e^+HR{9`g0zbIy5Fn#5HoHhEa
P0&ylSX=DOAB#eP*G3{^KmCfxtg`{eXoRSB5HB}!5EVMh?P{Mt(xXy{=0zlF5~Gs@dLngbo<LRwH4;MBh%2xY*e{yM!BYnm&Q!4T
vJA(`LnpywYm#8f(%owO3q1M7YxIRu(pL1sd=BYfjO2wE$9eCS)?)m<2i#Y9J5hK>{rH1hJPD~*OJinc$e+2+TE`*|5@;J`&M#p~
A${)&``1tJO4aNbjw;i7E+l}>(4&H!2(>d&k>u+6kandu%6NBYY<AIk=rHv5HbT?k*jmhBq5Ozv^IQMJ%k8c-<lm#~72>RV-cqF~
+M7bfOG&|ujr0H7$ZX2GJkwI4tbwGh8t}98<_)A~b-YoyRZ0w?I2b4suppmoEvGvCZcXY!-m1@?vAL^KU<p9_PZ7O^4yrXwOrxH)
ejM^qIYh>RC~A=-$LGI6_Z)eL*D=xQMk55~jnq`2ijkLqKu}Y$F5mKskqJJ4jv*HzLi<w){Wj}di^lvuRO;Ma%g3VN(&N1AT$zSt
$r2K8$lJ}HowEC!6|(@J#r_-KIL^QIq0bp0AY(onQCqce^bAyl5n%H(FfLl{TyLyb%4Kk^`>N3#hbhBW@}^xTl%jU!q8?c%j~HYN
fwlB%4gOvK8k=uM1{chK#sBgVjDqU%vhYCO4&AcSQ~5EPS%4?)gaklr_@#)&@`FVKXz)`%=6I^@ijXdBiQoq?Nc_Q51$BxEe=uYW
Hr9K3i(-5dMTsA51N<M<$f+*T#0r$a7?hZm9$(xT)5;qXv6dKu8FOXJnC+Xt11QcRIG%dXhf6H?t^u7>kAKXP0SkPi94ETkrn#?0
ssJ6%`hUDJ^g%`WIMaK#x*bz%d6{bQ38yX(c5YotXLcEQ#9Gs=!iOZ$Gm(2R7;{*2<+>XJnrOY=JuXi+EHl^lt)wJXz>}s-cie_B
CV0S5v~-xfrXQ-G;^8#XK4i~qjIAnf6rd#>DwmDDz=fz0m&M=z%~^~-rbbb5{6R;wAhzMJ4v1Bv$bhyXq)HVaP0$RMZZY7ZZ<Tzy
_Ad@$gdyYB(vn#g5)LG?eA0?FH0ts#t(8ud4-B&D%b=p|HQgMvQ#AW#rXJHf+}9E_Z;H(fKWu(KOG*4DGs;@GfJpB>%zgeXTQ9LS
OtRC<d)W3LP_FCml*1;K;c?+o8<agYmTaVYY?KFpFoxnE0xeG~V&)bP`O5uwQt0mxWClsdaic$<t^isrll<>4<bh6mg=c`}gPu3s
c#ZAnI118lK$4!CzCf_VXF3cq?`ypEsiv{SfI9+gx6ELbzB0@Z-O+C&e){%R{@c2YC-0C2J=w6LjQuXm^6g8DdSOLu2mb&RTy_UW
ge@cEh(77#b9eY69+t_sd&yR`X7ZW{Wf0QOK)9M`Dj`R*zpmDe+YX|dFFZK|3|C6eMpHz1-2n%J{W~Ss(Kh^uGhDHabBQJmQy>w2
N2RW-g$%kE=f$ndLgGp;dD>@1PL1?|YV<`Rv5cH+Q3imW7!}l7RGK9F{+k+*^L`4=snfw#$M~tZY?f*}*dOa5ey8gSc^uNEWb>XA
y_-OHWR0g^wQHPFrfY4uv!yH1zlfV@!gdj0I7hSYns~sw7;zFdqz4Zo`)<q}lafW_VgR}xBN^ctyF}q;5~2lB2RSC>AVPwDT)wM_
um*Z9`R&ZZ8j8HUoVyr;Otu_L)enq#T)U4{C->==#1s6h4dI_7$Jav3TKYiETVM<N433NKjFkZAj73Se`vTw&#O@?_ccC*c9^!IA
buf>M?s$%D5u=jIf{t??uf@;1cdTB~CA@79Sl`?k;<+Jm9{5AOS?M3Uho?Z$VcSxPx>C;<=-<H;UNG~uSBb0qZhWJUul;v`i$Z0V
H+6@z&m8xL&p)&{bQ|OgPB3r6pNtr>W}U8Ag^#U(RX`|cB>xkBcn=bd+N}wZec2{omTbu0Gq8w-;%=jaK?95SMGM8}#d69nRnib>
!%JC_$>5k1VlHgPaY*nAC-MjmAXPT83Fw$=-q%Irn^b;J9{3FBI3?Oyp+T3ixnBxWf7xRpZOTz{@a9iQGq2@#qkOvlpcMv$_kYgQ
Z~AkmaJ~<flWyx677(m^%j#tlg~GGb1+v^p+Gd$T26o{9qWU(BXOT*cc%C4g_PU)4z5`_4LEW_2;GXSIMwr~86c=aaDK#G1K?c+5
mZK|K_H9&F!O}bRa$fKUL>GofGZ}@v<~h%)gBfc(GHfX83UNLZwUTn`8;O@ZwsJwvuHYkAyT)XPppHRTiwWJp;s}7Uyi<IWy~?v0
ferlS4V>!A3@LBjBcMsPlbFaCto0@d%ZP-Z>qnnky-`CWD^vRz4TKNBL%Yxm_%&hiu71bv9@7bK@dNLNFQ1U$LGoeKi``gY{@;&u
@ZLcLY#=ir%`lk24r1J;vi>l%%g(aZuc=IclSFKQA_fgP%Zsq@K9GkALw~wJG`^7Qb~)Egl9u9zRiX9-JnlVS$SLdyUicm~yF@!a
U|A8uVuYZ^u=3m+a1lR87BOsdUN+HpgS>btAeDNzPXFUg8+ESZsYo%iSu&wo!jGy(7cc?O5@po9Fl%|rRdpKE0~g0`I7+XoCf-7s
Vwj{uPS;Xv0@9v;muzs_B*bGS=RfX&dgSY_;jPh4TzjhUz54ym$A9B(fXtC<A_O8OICfTq4Rrt@xIQXYP+AGsjDRx<xQ6p<3cBo@
Rfnd`yBI;*C=-|Y320W$d<Oty&G=414>Ej(ke!7b=swEtfaYk>(6kd8>x;k@X*~;IOwRMZdD&vo##5nJJ(}G%3k6n0)Qg|)0<tm7
!<Pg4=IW55Ts|1QeQ+E@aN~&S24~2a6emKm;}#RvizxPOvWOcF2F5EntK~io%N;*Na6UYZu;#k8R|Gsyz;@wB3Zb-MKz{k)kmhh*
L@}4VX%;+VH6)RmeA(ye<fU+}9Te|@T2?nQjt5|y9|rQ@lZ$=l#4Z8eRyp_h((=|(J69fMiQnE2O)445h-BhPSgNyxInrpfVC=yy
zMdc9^;x!xyrP!?eTHGQB#tto7<#)6G$BIsq2Ove(1p}?SOJpO8lyzNFfHDT${rbw7eEY(ki2OV7hZs{$nu{F5Vpxutvk=f>S0U1
8boQTyFIEku5EUvi2m@Am_?97)S5dF2f<Wn$x=ocm(J1VH{T@SY}GGo!JD<f;PVZCasICXP3t2QEO=Vb6Ss)VHJR}Z9rLKBmk+Tz
_7ie{lmOw<voV#H!OOg@*%#kkT4yp5H3^&xBEC?qzmZ$E3Z<N0`rh{cWz>kfsi_QG^9z5NQ$gHo?xqb#O*ur#?Zz-x_FHaqV%(^m
q1cTEmP$SvqCSA{<n`S^#uxs1#urp2u|+CHB<3BOd*68KHdVfM^%a#;2f(QnY;qMToIne~4tiQ*y$L9l8Ijw|uns5WuwnC$x!kOn
Q~axIy`Gg%K6Yqb+9$nBA8xs=vzv*}79704PGp<L*MTRUk0`9Qe!^~5eF@aw?tYN6HuUFEtaX(?&2*-LJ;2}~r%X6RS?O01As!Ca
$R=V{ehmB7=J9gZ_^jlqQ<CcyS^oj2w9L|9x+s?|;}9RD01!i<&1B!;6d#j{DfXOG#D3+B%@D*q5`?>R+iOL<N!QsXV&9jIOZQQ(
6_i@~4pKx+8WjJ57%?nVSQnhg9i$AM1Y9X@#r*rzr7)aLZvd{Ky_BWHp<wi=e6*pnY&XL#-h};<bn^*VQI&vg++)Xu=;30dwkX_3
!N8tbu=sSq8$6VU3(Q*pdeG-*o{X9-Nl8MPqrZpPjYWR|LLeO)mX2oG>4IZk5Ab>B?C|GW6#uDoyVFMOS@z^Nb(u&{+*vNJs>N-d
-4)vNCY{NN0QlRUT6-e2BAHX{5smY^t^>S_HNb|ROl0QD%r?A1fLt2{ol)s4|GW;vwi8qE7ga+mNPN;V0J@T^WV-u9DKyl&N@+Zl
585+ydwe;nF}WP<WCxRYFks|2tl8=Z3kMniaFCXr76a*ln%Ji$a9NYZ=grW>Vk|lL#W(xt;TTZtIOUTG^CaG|qsSHD67w+-b|#fy
2hQPzUF*@ZYttb4;_|r1Xb%@EZPvSo50sYKW`e#NOaKC+AzrB}QGs4K{>>Qau&o_nl_&WKm?RYv8)a~g1(d&7Y^t96_xxxm`#l3n
T}ao8aJx%uL+dbcStgnc2ur?+L>9gsoZxw9KZ7~Uh;nM>O5+t_TXRg{=e=556XUd49Rcq5kzeppQTBn862-Fwf?N$A=JWJL(9@93
-qICrqO_9;G1~1x>aj>Ir?$dX)by7WuItKYh7_X$nAmHuf~Hwx&&soO6Ncy-IfBChWL6uWaxdCGVR|<-z97K0q)kg_Yl>;S|AwSt
cJoDiA)C^a9z9*~<~M=Y?YU0<MR=!Yn@KN>SCI#^N-hkjh$<eYQx~|B1AZ*Ki{WK)&#F-_MV`AXa>bD1Spfo9URw-Cu@s~aWTvyX
bv467C^R$I)@y{w=fdNUp66;Z=ILOYGTr4Z3o0BmTgL96=r3|SK{8X*x!OVcwdlYj1yHyOc$e`jl*}}}W#At&=5x5$n6gV|)9Sb$
3CN4Hy4|cp<JGLD#ptX{a9aIQTKST!5ZsaljB|7-|FfvJClX2Mb)-x+Eb0AOGeBZ<dWz7A*p4p<+9MGExs*9{j_{c3^i9Cb&f|+N
K9C4Qy4AR`MTE{vf!%!PrC`}T48rL^c(XrP)xFu~acCSGp3c&6Ul8Fe`+vCmbrsw34kvz)7yXvd{xjcaN%+az=p99he98@s_Z9Lo
Tm)Dj8OM$`$Inx1mMt(jc-AlNefSdHd(wu~)3a7)wdVD$I-02|qW;w{sg{4feTsH#1{5{V3kS!F6NB_%{o)VgOt)-sAV~0(|FMuu
hkPO#egM?SA)N&g?D)U2pWa{uP~`Ch%YGLTT-9BewB_0jr$KU9^mE&c##Im#Wha&21kOInNl%*=Ejs=&2YlnlHT3uK%B1J-eU_pO
vH=u2vct{iRsc!Doe(1)pQc$t)Q721N)a1(+oTzCXi}nNgsS9#sajEDLw@XNkyeW5ul@;r9>z%SH_YpvdX_o5(M)keQ|m!qQ|3ra
P^jU6uRYo;4Q7?%jy5+E38>;CKy{<aAlJBC0Pcty&}sq@;uj0w-ald!VVfKylm1avN`-6X!JnOK=nF`bQZyw?vsf|w%>BS8VEbE!
zvPicxfH`jda9|Xe9jgAAxGf4<97iPtNuW}d1Uo5YB{ZO#tinZ1yt)7n@z~8u+wryRJ#{vnvbmYeE;A!oJztbOjw^VKg5`1@U{?p
kl=d~2US1`X4qixwVzoU^P4f{(#MKTg0Qx^O*T-6nj{&Y?72rofcjnlQ$W8$HQ=AEav)-U#d}?wH0T@QDs&@qrpXy43jbk?FP6Q|
3(Ja?yqn1&@q!co0AG7qJe`JkrEa74J^o#MrGmHZVZ@WCY!k^1@-S)5=BBIN@gS2>n{#M%k-V6FygmDSJ&(@*+B^kGwJ#fUL`Bd;
6KX%CT<z2mdN=lTZ75%RY2-$n{~?PZ_=Wf5!UFD-d4p=tWu1j!NdtRaYJlyW?!6?4WWLLJnOdekQG)#z`U@J_trJShOd{%5!pOnr
w2RWxC~^oqF3kA@d3lg1qfYjy=0Kzfs}`-2645D(_!IkzpbQH+<!5x_-Y7uAkh<M??nB7!vH04q0B>fC3tiafc|>0CyKPL2GBTy0
@wa(EGBWxrraZdp76?Em{?hl`Cdt1AAlo>8bH9=Io%yETZRE>4{G0mb=zXu%0w*gQB#MJ5aLb(lrSFs_l7JfEKyE{hj@BqJtx+`R
hBAi0z*V>mo~~i(tE#xd@0~m<ngIqZpYet)EzzetEjJuH--B1#7pDji@T1+}f!+$=;fh^=u*o~0S;fJYfzqi<U@ZL1@7i!Wd1e$>
^$o?l<3M@I!&m6%RoaVl^LiYWD-bKwq^WD;m5Y?%dpXAI^|?l(HW7fiB1i&SVm-NdjbDMDb4@ZZV3rNzsCAPELGmsW9H5^bqq$G<
JbHw*F-~j~9*Z@{Bjfu*pWn$-Lz)>uzo5XNZqh_eXoswDARMqsd@_zH4%}53HbR(+z<{XCn~-&LoP0t_0f0~YaZuy&jY3uN%L){|
4f<xlu3L+giy0Q=$Fae>A8~Lyd4d4<X_z21MtBo$*(Z~xq1$g;JCK=!PkZJjkkc6L<={vf=Hl$Z`dSEpGGyMJ1yeZV^I{He7qaBb
Mh$WiQRuy1N&?Rkai;js&T+{PpNcyR;QSQntvc0jHchaIkEn!|9w+L0*Z1C01%-3HDe@&Dl=3pw0q%k7SX6}rMp0`(fhNXjK8`My
;ELLSoFQAHa#jS^f(RkmR325X{#X%C9drQ%j}l({*Y#AoBVy}J0jP0X$zV~Z)`}2WaS1G%=e0!|=J6ebL<@I}L1O7NOa!)N<_{vh
Jz`sH*TYFz1>3(dviBG>S!#{y^1T(j_K=_&Le7U5Hs(U%r&Zvo0JZ~D<T3_dK2kKEVh2HQ_cC-x-4ShRq2BG9&0!*wmupy+j8f~I
wqm&Sc7lcnb!oA?{0#cIrwgr~Qi2!7JH7eYfCY^OJ-7@um~NF6^|&o5N8>wJhDINw-9}Y=PK$M&<xJU5c-XwKf`D(OyyT=A01dXN
4^t;v-=Dv5X3+^3yT_oj_XMcik-LXVmc$SGQr_%xiO-SCQU;`zprCoXZe1gs@3#C4Yw893Usrp_*lm|nji)!D2mZ5WGQ!PX6c9lB
3Kp_vl!Ck|>f+iTRZL8(3n|EcH-(%|3>JQ)+N{-ke)O_DDk7mu*epJ$(AZu)8_wu(9QfJ0d7)0j6$EcR3M*zD^g?<#xH~o&HE(AG
9PPF*<ywU>hSZXQtpZTkR*)`V+qq0bowp<ATTTTfZ$Tsc>7tjO?Bd%h<n7<rb0js6z)h^|S*a7a&9L1Ie=!kBT@P0YCLWgYPpJ?L
MlwF(0$^|Ir;o9?goo4~;DhPi0HUZh^+0~~UIxf;EspPg+Gi#w+~{F48p$xrwjtpl9<o2I&;Qa~Cze`9ZVI)Sy%{vGd1A(uUgq|X
;l}s!&=q=y5BO85xD0Igin@=!;7M(5ddAgplrndjP4JPQU8+8)nYp#jYIhA}bbS_3jh|i51_~>xA?pUm6$urD6(IktlPvJ_)Q>EY
!MYEX2>m21@>}W8wcEr$ReqBiZ%IDTEzem=zOX`Y!{jEU65e2(0OY$;EsLr0B10(`P?BF`L5(>P-zSVw97tA7hgC0yC{fWUjU^5V
_BlK{uL9|GMn(~_!>yjriM8T{f}mx9g!oI%H$_*^1C;Ijp6liuY8e8#QW|ei4rA>C2(@@bPkML-0Z(70B`zn%<EviHyG;3XO@vaP
s`4;+lI*Ty57UUQ_K@IXUgS?|5$xGQ6h`f_U4xg{2ZOdyfNy;8!-Y=!lB)GQTDGr}V)JTFP%49J(j$UtE7Jp<|M{|F-eN6R+Hhcw
AJA4VL-lQwuD5*7u)x&xz8ohLVk(?~+RNPg$Rg~XbDr!XZRpsofv=}asz!*f$`axQ87WAGz#OQJR1kLP-c<P?r9;0f1u%x7aO?^*
?pOL3BUl+ZcJ>5#=lC#X+MT6?rm*peQl9M<`BBT=uc{Y%TunZ)^{V>_EcT|HJ)WOs_0EB*cZd`9F0}L?-%xf|r%0}f1PD^A+JT<X
b&+)wqLd6{s!hb#_Om)dIi-E0>+{rtU=Ww^l?^nlRz44^vR3Cu?Nm2s8I|L$=Gbw!^Mug%KMuV>Q4Yn?Lx;W~4fb4lGvPl*%Wx|O
A-6Qu6Dh?L2Uv-DFwY4H{j$9<?N~bh+yeN*niQVJTI{!$kP?!|)cM!QSI;~mLzDW<3ml)he5(oab1B>?Pl;6WkLUhXR_>{4WxD3!
7cj1}CjYw*c!Q%T3hF0F%mk+JSr9Bacr;>HSK2-F=&<G6#$-&fYlaOmD|w*xT_Z<iIbj7j5euXQIf{gxvkocK#vIQtq&a1&`m54k
vitEobtCD7U^;-C3~_&-BT^~GB~b)-+}zZuZ_@btZnB-hap{Y1gnE*MAnP)-W#m<r4!pO`3wzWc4S-ClDbc4_=o6D6P#*}Op~&CC
a^I9A4Z#i*63KMo?)vj(Z$={gKO5ksm|QnVXz{zifCm7iW4^5lEzHWTNbB3}7RS`O!3l+lM(5IboPA?i2;*Ty3pNQve2Uyrn`+wv
Y7?v*Goe7v*=Lu11u<GIW+s~_)D)2@V+2&3q+PH6748UJL(5D5+~~i&Oy37lC~C87UV2g9mev3X1AA1#DbJpsZcNlhGK5EPhR=z*
lrPik+M7h7UrLhm)xejsF6oV<hHu9VG{?ERVFP1_^|Q8$0R)!3DbN|~mK4(beL=8$R-4o~m~$5+J{}MQh1W&kNq7W~=U^Fkf(>bP
L)$$hM@rY2*TEbUt%ZMnY^)B`LM?K{iT3si<NBHDc~pyA7@mm8eFx@KDPU@c_q|>~TB7Ri351d4CF;`jaxmVa@4y76SQ=TFRg6xC
>7|<8jNTzyI)Pe6JnZp9vN}`JFxvi_=a^3Ku6*-h5YEVq_i(L*)U(U})CXi25>pSdLkMI7Xwm(U%EY??--p~SUD2=th!Ih3lGj-u
dMhoW;7CopEq+#hu1F>2B_UppFD5#kC9wj-T$%);&7FN$$FvMe&IS#=t#YUClwwxrp`y|#5LCJAc)Bkyr9j$0z~wcd_Io3w6+f@J
4K~2^ursq!;tu1mnt}wdEa9Zkhqpv!+7S(~&0#Q{=4TWdRjQEjdQPQa%Gt^*y<mIA5Dz-JNw3J!jaJ6yN_!#ZalLy_TmY}`ykonD
Y-!pzCW<{sFKu+e#4W54^6utX3|F{ohdQaBbfp`A3o<3}yh?wXg>7%2tC~YeF4DaGni)M3wnE_3;SW5C#D2{syOfw!pP9W2;T}!m
{PAm0o1FOUTJEMeE-d>c7|UKx95Ovi$lBl%&QFn`G_R^+0O|0<E+`K1Unlh)$PSkGB_GL1mJkEDnkz=}&9;SD3>Ro-KZ(75x)|dD
f&UI=^-|Rll}Tn)zl)XQKhyxSB+G?cirpG~x{B938&Fw5>?b(Ve@)WVtko+39R69o!QSIt(ZAc}VEpCIWP9E<09a{)Lil$q8=2!P
)7|JT0eI&a018&>Ai$|M<-H4Vm%^r+s#HO%+iON}KB9n#lir2~Rq0nG9!bGq1WH7La=Aq-fY#yRLkm<=|6PjcP1``%)}o;vNh0i;
?@xetQtRg%%moK8=a^zx7VgwctMv}kj~=Ocsrt*~)i9xq=PMf({$lAdyfI~00H8FVoMN;HXnVj2#qJrC(Qw9=T!Hd%3Q2V_Q2+Q+
WZg50q5;t6R5j9{t1>~ipK)rQgOQ9*RnL^;9=f{rntb)`g6&m5*iHr>T@!@MH6+d7KbdKc6LcdDK7<GnMjw>w<U`5Q*PtzwkM80O
Fl32ip6-8~8EdH<qg;P;YSwujaSM}`o2EOntKZI2tyLe@^J&~GW!O_o1_z^H4gfj4-x-*K`9pbcjU|3PNnem^8*dt@3UOzT$$7Lc
7Gwcqu3tNfe-CMa%x3%xy<oT6=;%+ZU@83)oqTOUwnscrTzu`7;6r2IQieylASK(bY;;K}KX`IYRy=iOK;wZ+?I;P>5=-~eAJu7~
sGSbRN$3~f3^1l0E8j<(fVnCAyCpDE)#UUIn4}YgsouCG{;WVH6xo*&_B$V<)v9<Ofmm?u<TlQ5CW<nlFeEYhLbA`>3+V285Zo2j
BC@`AN7!d0n6uTJT1l5+L;iwm^64f*7u=>UeTGM5+=tW}<jcgC=)$=m1?X$(jubz4Nqt)kjgSd$JmX5mTE>lu{q(I!pG_MVKu-m9
Nzceo94GAPE0xs5_|X!Iy?cUe$l@aHTc~kNe8fTkeS7g0sL63dP8K`B@!{2PbBfT4ObuHLi+$~GZWClxlZnSbY;QG|DU#X66=wHv
LRk{$jF;Dz?u%5i5Mttv;F2-Y`5Qh6jG7OWUW>EbA%Z(l5<%YdfbilrL{ROcsyGqTh;AlxeGdv(I}Ihm+=Yr(x(mKS!Pp7*ufesl
<*a<%+gG;9M(+(|Rd_^Ti4Yum*b>2TP<WzD<%lz2YTR^7O0FucGp@@<R$s4h2r<92;{xUz^CT<j@}cg3r*0g;TflXbhdI(ArROT&
%W9h3E5*s$yws)=r-4lUMb)Q)O(~sJzUx8DKWN_YTr{-OaW*C^hBNnZS%G{*Y3M|)H(M#zW+KM#I=_JMx{thiE=G&TSq57rNTLTe
4*lKx8{Zt_#a&%@``oQ7=~Y^tdtu!|$|f~bkJR<-V|e-x!>)uL03_*J6)#EE8<WH)P_E;L_H^LFTI?*QcCm07AUEmW9TEs4b)xmT
e4C|-8p<czE;`<zfCh?5^1(1@2qK2a$X-q)0XFggWG=_97{Jp4M*$T06PmKq(g^tN>}F1Wr*de%&@UFs)L<|&JGol5DB#W9ojB8N
(}4FA>cuJ~Ec!;_J3T$|g<nUr?{0M!#hK4%oqP~1jFtDjp?S*Dws@?$&<*fIjZ19UndFIKNO<p~)JChb)OLkYen7xX_P_`hF6VhL
$;CRN57wT22M#4P_J%?)_HQ6NY<{FIW;d^Ov(f+%TY-d5OX|}jJm}S^3XhZ#`QF?wklZ<SVaLJw&_u_uU1{*%h~uU_r&)qs1AFCB
jo5J2`lcURB?JOI1~@?*jlxd{!D}Ry9Xm~!w3CIzU=6bnmeSQsOfXQZNFLE8(hp0`{pwc)9B6<)rOc=nRt`2#-YFG?J)F4SUMEAH
)KVNn30wA|_N632^g;Ox!TK{fVca-qyb7hnTwd-?r|I+Wkjlb>05}a}t4CM$J^Zps(FHWII*0}i%b!CP#cjqLFseLZEpI(g0-NBh
&eB*$YzTJ<@juGq;y40Riu-=4QOfowzhv4q2_Spme}!xLpytHE%A)Blzq~*~EeAa^6=}G;NTjk@6aq7DF|RToDaSmr1S3s^Y?d@b
0~)al05C5m`Q7V9DMMv6ovRG7Zlfrv`x|dNkv3se#i2ui{!C-0HaP4MnmrTv&G(mwZ=);z_T)&N7xjbq2#Xwi*rCXGGWr39P?Sr~
NEb=|Q3tm&DLgmik!*2MG8NKn<k^pu!HLrc;sqGk1jxR}Vwi|98$Cd{W%#RRtK8IHP!iBLQi^pPCNyug$O5<jc)DR{Lbg3{8G+pq
Vii-oPl2JFJ|r->xnO_Uav=7G-?aoq6VLgsotd+OX?|R96*HS$Opk8H$q}vI`wiBA&84K_GvhLE>KfoCPvj#o18n_dUPFT10)mfb
s%Y%KPs`0zde`im;yFI2TB%cn^ozGl?2|$oVboQu)}q-By~wR_33|IqIH3m!>VrCoSV5KuL!x{AowIN*LVv8Ul^ilz5&@c*9uEB1
$gh@g_N8<&THW3yV7C8D!=fm};$HMGN4Q0Z9+V<CMXE(NUV6+erkDt=M63>N-#-UD=vWvqq@y64mAl)Vsw^kmjUvX&An}KgOLnxJ
iDxxo+mF7~yG<h&@gM?tSzQqRnyZP}a3%1mr0LoXrP6+4<lHohs%g*{YMEy5k7Kby)#6^{{m39Qs^|G54(tAZz6`Tx`Yt-=$X;iU
kkx~-k$AOD;%<Ik(D0_+T7w8hkZW;sRh&*Km15CC&hZ}Ta_&Vr-VS}Oh43~$qE)jQH3RZivNL@eY*r_tB%84nMaLn;C{fkr^|KW5
Tt&uDdfSOS`j6oE#!{?*5w;BNvrCEfLw<|iY{rqp7G${t>kl7|#6k<LnY1xQt?d{_CC;Q2%c9IrKEcsmNtGZ>v32dy4&!rL^p0@)
j^F$jj?C6qxPZTvFX!?WsS<sDzc?NL8O|!pLIzC0jH*<FZaJ!64`6P+x>VM3RK<a6-yisyj}e%@G|{>Gz`u|?4C#>j|0){Y0*A$c
7TqQi|8M@P92u_{_8#>}eMlZ8DF-4uc6C;JQ^oY4NWNW=$;59X%Q8d#Zd!s)A!huO8|SS?*7e_Br9ZRY(D&&@6<+=tP2}-UPjjB3
LsLPELRGAG?fzD3eS%ua#KMY#((aY)@(2EYEF98OIeY(f6>-c8_mV!S2x=n3)iXN4&CHcMb;Yl&RLD{>#oUPmVtzU2@mfx0_~Ks;
uVE3Ztv>HYax-4!zTUZBXyV)&@n7)dCU~*7?wu5;@uxR=g)31#9z^d7F`i@*Eb?fbJ&SR+l|pktFQq2XS6#k^i>@GJQoc1xw102!
J|USI3#UIv6px#D_#Ja{bg?u-Mbq7f;@7PI{-6F6`1JY<CB2juZ{Ot}q|YhgUaTqdL_>M?6yl+CN#M1gufzG8tY&r}f8BKY2KV$3
8^nnN1$vrkhqmIbn{^7UVj<&XZRw31C$pwvn8g7(ZfT@o2(r1;#J6Px--ef3#To$9O6OHXRbJpCC~hV+9vykKT-69cHW}(d>j^59
0WGR6M1E-3?Y=A<tsZax;ZC`j&E^q7+w?ruZ}Xq$OMRAv{exFwA}&{1Q9FBVdXnNIybP;TNFp%yQyp@a1>kRpxQEr?wT!8~y$W>D
Po_~=Ce!_+R&Wptc?n99g)mt;7B>294Klk}YQb5(PBL=N@7RUdijc5l>mgX63x)3$?TnSOVnb3f09k;73t3Up17f4eOh;_DP;I;X
+JiXbxYJ2^*}4>{BT}imncw{cED)_BVP-F<yLv4$)49GV$3Dkuvg(a+Aj9$Ij@r@M+OI^0klDa+D;#l^u3tptrK<M~oq2^2x%S~O
5&O|>sT=@RWqIm*kF_q0mKA7dQoi88d7;$NS2QsNA(bXUrT3BqXgFw$LQ_hTX_d~0#j_)S@F-sL=oVjNwNj{F2uFyt<+M>v2%{?P
$qKL`L2E45hw8RhDDJ)T)6ko|`D1WzBK^NQ62_Ppx=rYZLa%tq_F)HS-8vD$CS?SNyRpI-Qh$2)7a3W9p~Ns>y9X#JppY)3S<zN5
wG7A*{HH^NHZQo9Nqx$^8%Iw_Q&JupfGfgc73pA*Gt8&L--ajt1pAz{$Yg@39SNvk7tlfAg0{oXR(6|~C#{e)W*kKF2QVmJ6bxGb
h$x5HKTBnB85BLUD)_FnRmhKNoDbwaF`hB6cMvCK|C8NmPHs&8oDW<FB5ix(c4tJK$;_O#Ni=nke7rVe8VD~<C#KW79g{O$h&G}E
1sGoWC3hP~W^sP{WeoCW9ZL}qRf~TvXH{tU%uBJDm16F^p{*v>mh+xqdRgZ6iwNv-xS|AgEpC@`gl9gaRLM5EIjJ4bidO^=Kg-Gu
;tr=zYph$@P$WULP4JpLLiv}%b=&Wig7WslV}eAR7zZ!*Ksz@T(|o{lQ__&o*WFG7Z1i;0u)d%OSLQZO1^$Z_7X%&Q-3RIdck{Ek
_A?Tck9|stz1T4?4zY9J4_#a=X<}gO6C`*0rx6pe5|M}}&lv*TASCag(uJ=K;>GYxPXAWfF}e^wuPX%Ik}GD+vxL7lSUdbR><yme
{K(ln3e>j}<Bu!)nd8AEsA2G>mVI@7252rK+80-f25|&I9muA0c<-wLfn_bf2(Q5c#h<ALL1p+O`FVOee@A9sz4!a+cP&>UgS2f^
N7tet@1?Z6NBzb2S`4*1CN{N-gU@3Y0up8sV1J;mUvjdcM33zlsDFS67VS+}JRWO-X0CFVlUVQ`HO~=!KY?bTsHxE`@9xGiL`XPM
%0b*1r=Za3<ydRy{0me3DteBIT}o16eSd>f``n(=oCNCY&|T`TiNQg)-2m**53>cP>x8>mn76}d5l4qW+{~dm>{zSE1er$tXKQvF
%r5{E-(T~X;*`vJtuHb`2zRgG7EzJG(kIC+ufoHa@eyNVI10}ar;FknWV4e64IBxPLv)$m(&*r3lO-yLx2A^;EvtPU%kU`u;@Q6)
i!GoqcBsVr4>)Iq;+lVJc%o*9y70IN+L9duxjpV&M>@T?eO4>ogt(o)=n#2?dX<*K{ii3JFlqT1i7ojFtY|-TPY{d>XmACTWaOHm
ux7{2ku25ZKe>d=E+c{jp7^onUJZCJ?YiRuE%FPPDNNjTK4*xjKK*LA4RQ%fjlZoBd>GW*MdaGmr`O#tbBPsW=_&%!RzDf(VovGV
k}!cNthpuwCwC8?xc>{znV9>bF}hO*Pv?;@g?<q~c^5pdj?MT6T0^J4L{me;KX*s-^egTF*w$2fH5G>WB+hhD`OM6xY(wj)0}+e{
q{CXt7Z7tkH!aCw83Y;h^HiX;&XW7^c?Joomsac$pmsO`)eW?)Ri5LLDOORaCV_~U+BX=n<`*fre)^NCoh`N7pp6>o$(7p&2W}FT
IF4Gr-R0X!jNxDZ;6Un}HK^52xjd_N_b<cZ4T1#5r#O5sednfkVA!MaM^JIr7D>&D^#VniyZpx#^8k16J%%M1kxdS{@^$3#jx9ja
7PCATX6Y^q8Xv?z$O6pvoVW_aeKX*W=T(>OEOeEszQrVq%<~JW8f^p|n6r-vsjgIf&34OIp_U{-aQ2u7vs&ltwLLA60HWM-z@SK*
iuqkEB~tj2F9_uKB}!Koi*mKXgf~|n+K~C^rR0V}o>N`p!x7jrB<cLIWySlt_%U^E83y>SbBU<SBd-&E`((88sS?#$;3!JA-r&J_
sTLHy0hs4@1SFH3Q}%X=W%0;9`)u~fS%8PNDPtZa6JJyQ8je;YO@){Zr6=1ggq9R>EB-y02+p3WBpV+o4h0kqhAZUwY6&5ZsqE_-
7twStNeu~79i`v`ycPDLaJShLVt7z`K_J^!Ud?MED=eCdD=z_I=@<_95e9KZ;*sEb&54J<(g2hbfPW3RzcK^NaR?wvH#PyV)thLJ
k3P3Sw=$&7Qm2vK7DJ2%*XVs(&yQZrd-)c!%CVt#ID9tdC|oE!`ugH~OEBBX1#%koEd+g#N^(JlhhG1hesRuP|39sJq!(Ls{v5!L
pbg#FmH!s^f#7XP*V%*@yQ;WdI}#$0e#>ShllZ{+37R4x*LsX78l6W$^Xj>fC}P%z<1s@fy-TGgjF09e@jq$CQtu?nQG?oRA%_uZ
0q;y<SP@kK8_-yOG!o47jM%aU{W-G4SV+VP>2Jo2wbVSRIbveP&9JlhGuAsYjmTqHwZp_~_`}|AZti`LQ{W!RIN<{zt>^>^r#QFc
iXh42>GkW?WW%A6R)52ujAHGo4f=UcA{cYOYX+dRMTP`~xk>zCdQVI0Gt;GjYp)T`;8(r2cbkW{ube3Ua=L1#=gS8?e@uLquzO2K
8j_DIgdVDGuwv~oj|X3XJT_?MMR#b)okpohn(O@d(tT!L`NR#Dq>|WS2Rn*wOu|)DVd+x?eYz=3&0|e~JJvnBR-4e~7*Em8Gxs%<
)EB{qHR?PsQlqq|+*z4rlsoG1b@M`d2Y{tJCA1}a?5=)-Mxq-Eh$RZyfGr{NY<XK9&QV*MqWpb^*|w7*=dSuK9^Fh3s1%^?vxsYN
MtNOUoI<Dm*A|D?B1ij_Up!nvf$N~1iY|`Ma5GwAdpn(SxX;?wKE@!Xb`QNzDkkV4m`ft57^Q9__Ab9z#H%@)BoP~OBs;!JV-O~c
Hef`sy3fqT55?xSa0+T@crwUR3af?vT>v3T;Mo6|p_oU&65S7-R7glv+Payul0qjl0H%Ga{Rl`x$i3a!w}+G)BZ>+ceR3Wgiy)45
92e8%=i~zv(c1mHh&l1?VYN&1>|7ZwD%^#|rc7y%vE)M&%fs|K+i}O9flD>6DD9g0rzWyjMN0|@@?v7dZbQttXzwAlCY#W?@6tJT
fiX%!4hz?<lpH>pW{eL-yKFWhVrCq5EAC3d!|ze<=a=hMo%nFjy>n7vdCYN?O;8YA@Q<TWvDfR7T`SooR-3mE1CBD}#uvhnN067R
!3qlQ?{+?$2Hr8uRU&uZt8SG^hb0jZ*r#C?FP@jCY1S&8GjF928a26<T9GV`NF@|4#dHb)CJ2|FD59tnZ}Mw3g96Qc?C`ACuCW4g
RzxM2orn};&T@mlyWNJ1y&`~!gR195k^Gzt)p^`t{PL_GE*LTo?^bdecY7js6QK7~hSaQbj@ymXzA|sDnyD76apL>dz@&&#c6<k#
!@vpiy7=!xA<)1@<Oz=d***F?!jwRx8}N-i-R{qO?+!G&O!M%y;MZp$JDE&j@e+yP;@7CFAaP`qTe3>I>OJ&=oHikv{u)VZ70{e!
ITyn92K<Wx4%-UmUHY@f3#3&i<g_mg%euTchSXw%vxBbgx^dGRF3G3TrQdcC`Vp&eWeBV29U*wC@Mh{~4p?&GJ;sIKv8n+yHcrfx
^VxW5N&&c~8JT|g!+d3AKOw`AMzy|4Tx^KJ?P_AUD5VKZ4U6&*vP|3X_93BSw}KR!&6$}Qi8S|O<(!9T?(43EP16;_hZ;!pKmaFJ
00000=(7p9Ms@vU00FJc0qmOv$U3R8vBYQl0ssI200dcD
"""
bs=lzma.decompress(base64.b85decode("".join(B85.split())))
assert len(bs)==85484
assert hashlib.sha256(bs).hexdigest()=="5c57823adbd9cde14f89b3143d5f43249d5dc643be7a6927c91a89c3877938df"
files=json.loads(bs);assert len(files)==15
root=Path(sys.argv[1] if len(sys.argv)>1 else "qw83_finite_replay")
root.mkdir(exist_ok=False)
for name,text in files.items():
 p=Path(name);assert not p.is_absolute() and ".." not in p.parts
 out=root/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(text.encode())
print("QW83_COMPLETE_15_SOURCE_CAPSULE_RECOVERED",root)
```

The historical parent source contains an unused seven-row prefix, overwritten by the complete authoritative table before computation. The canonical hash assertion guards the actual corrected input; that prefix is not an alternative geometry.

## 11. Complete minimal source for the finite two-cut search

The second capsule contains all four modules called by the70-start numerical search. Its geometric input is the first capsule's exact ARC34.json, SHA-256 `17bbbbd4b2d273bfe20e8ae816bac29d8f69d2ff3747d2a34f127b1f44e25461`. Seed8309,70starts, at most120outer iterations per start. The minimal extraction removes only unused joint.py functions and persistence.py's demonstration main; all called functions are unchanged.

Dependencies used were Python3.13.5, NumPy2.3.5, SciPy1.17.0. Run this decoder inside the recovered exact directory, then `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python two_cut.py`. These are numerical nonwinner experiments, not exact certificates.

```python
from pathlib import Path
import base64,lzma,json,hashlib
B85=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;341-23-I>h>1rt){-yCB~*alI%aX+MQy!|mmKU7DrTSbcd?bKsSZxjYLVGZqHO%&x5jBg
rLwW%dl-Z^9b{IkjoBH@?sC@0+in#@6C*Q1t{v#PTn|NP7gJl@Zcv#n4(fc9H-nJg-sBS%SHt&l7jq-GF~Vo8_nX)N3Ql9`ik%`v
-{r-gwRXuPf!*&Eycq?p-U*@)mzw&PG<dBdyrv`t4PtX-wKJO`64D+*JfnTG;~=^8dbx=UFpsvqTH4cx_FxSo5<5N}_q+BD8=sbo
9~X=$cp<1Fy~G+;4JsJ(`AARD%X5YB>@JYCpa>Rh`{>{NmhP@T^T$wih`TRv&z|0WKBCJ~on@PNcHK*-HPLnT6>GcAFj}F7F_&5N
&2tz@rygLqJz1vXt`O?=!0TY=)47i!xwN3_@cyqzFuMc;c4Svq6|Oxw@o3{(tEg?W$o%p+D(~ezasAWc{8pqWRshzLdifWn(wO()
joqcnPOZP^*)+1XbsWi)$!22h-C7SMyhvbS*fnNq&-3^gtR~o{(ZhiGvj*hcI0mF@NfP4Jo`j^3Pxak$opV~T76cG8Wk_oYJ=PlG
-_#84p@zpW!V3vjb)3$$!M`9Anh(e3u`sm!<<}2x>KWWZEC;BobEgfEzw)u1xi%vO-Xgza$>2p7J?_B&RX~kt?_ZhSQqzpsM*W6y
eUU)wC=^V2N;Zs?XS?ij9|_`wwOCX*xXeg!)76ERng8!@v6s(fSe>vOaK6Qa8%3yXT>aP}%NT%{J+JLI<Y8FAx(#)K#XE$)#Zhl~
V+l>}(}p2Z+#jxs%{o{}A*Vo_l!ihY7MTYB-<93xv^<iR!z)WEd_fbnFyJLaF0Z;5GC^Jq0wq;T=C7E^xz;8`2`S~p>BJ=}$#b`9
Bx-(4U}DVaKY-}ql<1HBzw+U^Rxif;le`{M-WS>jXBls#lG=Y2vlk{6p!f!6@zlL%Y7&ot_atj|T&_%kJzdAa+CGnK={EE0kTPWd
wuqcDVD+>1>;{k(bia_AF6*>9lx%6T{l%7|ok@;^Dbs?lm7Al7JE8nS8raAIP}q69Q1YTsugsQ9#t{K2^5UeT(r10z`Ij^b^AM3@
8Apg*Ob#F)tMvu!273fiBcz7XN?|9*$DEvVXtk`{dcK;fgSiuN6}rUI5^i1z%0Gaay)p5-+N?F6%-d#}E3|Q6dDo=5I-JD?I}A6R
vF~0PRO;*)65ny%f+j6PE+Y9WtUMxef6F7ilpCb8c&DH{5rWwkW98)2{aEDeDUnPjZh|M4VMpFhhL)2AdIt`859r$)9y8CybmZH6
xj8lB@T%|;mr||rMX8Vuf_EUPB_|j2`QEJVq#z)e?k{CR<n6UD_06Zn*_d2b_4%UzN~(;~t}xUf*7~fflc!_G<D_<tF*<G?F%#t8
;7}xg8N0=KG(G;k6<W>TBUnO@>B(s?f4|M3?~ct+@)9DT6XFa@1n+5&McZc_%+?zrR!%dUqwa<3%xL)7ypn7bT+FpH_uKHIZ6s{2
zPhN^JxrNFDL3Hyp(mY!z$ld*I6-|}L*j_PbKFU<Gk&AE%@pcs*vdvD?{sj4Q}~>lc};rvdAkumqFngXZIzk}2z&|2oy0Tfy>}i)
mf^PtNcuefeT8haFr7u65FV{r!iHDH#kO=myF?VCOG>ANFH-rC#Y6c=42Q9?K(DP3!AoE$-|5pe6Q<X|3Q?<)wp#HmV;=0V4FL4_
yEXM)v+kpf!ZA+paeqEdIS%91;5o08o)1hk{@v*2`VfkKmZ0M&@d;|oe?L$`wDD=+L(F3Ii^XV1D!e|G3?_JWwpSG}erW4aqB(9I
(g?!iw*!jeR#K(2DtC><ZdTj+dXnobk*H144m|$)Pm2+4eq0-glDbmLlW(^g73?Dheuv*<g>M6ldnrldV?$e9A@^;X>^F-LNs3sw
AiohF@@D)I%Db(~sCy>RoDU$FFa^p&fH~O#O?JWXtHmj5cw{##7L2pWuHF2ac|leqwnmV7*BQn<2V~Osr?}KV_|GC&zw6iM@{ELV
XV`M?IVLYlZ$mvC8xcaNFjzbwWS-}p+Z6NzWB#k^$Al;pO;=|l!vrb%Qn8grCeM@((Ese{@(r?oYF0D274l?|w9{f@TxK`6&LJeV
bV5zYz$VP-KRR@VA=PY3OtB7SIg9K3H65^yPS5LY!?2nN20)5<bKArFYATKEgH(zJLOyAR7mCl&G>vlmPaix0bJ0bqcU?_EK`Va7
l@@keKYanAnB{$7`e<ZDYrQDaj1S_mZ!Mfaj!DdCjK4sj1LxQC?>1%8T%c_;2Z46#!P#IVFh;<Hl6}F%sy*9Q-C&-h5;f|*w`HHu
$qTVLxOb&3{GN_L%y<qo?B|vPBp#+5^DxSfF;lD4<$$ex%@6~2nkJzBSR)i|{mc0-&0@}4V+HIt?hTxJ8i*+^!>*F+h6r9!@a$o}
>L%gKC+W*wPw3K_pa@WwrEtVcYH6c-(t6d5bv<{uZDR8y-y(bW=~lhO-YrEcit~!hs0=%m)nYx2&D77*hI1}lug>Ml4&%lYTdV((
&km6xca3t9ApvZ)uPva7^>QR3BAr@CY}XEWIpG=60db>UbAVAh(}m{9l~9O9TmttXGE(yJEHxBSG=q(Vpuf+l5Ky{=&M>i8kh-{8
J4G)GPPX=<^et+}jr^hm2yO+3F9E^B1Y8tXO#g<mvzE+YQn$Ed#NQ9VNoJ^nRswUiB|+;#4?1ej7P^rNcjtmfqDbUl$quP1`>K!B
q)mQ$dJcYFLl%octpjlYTD~0`Yp~_5e^kk<z49UsqMTEMuTo|LDbyYRCRMn$Ix=#a9ntaz?gW;CJ{&Y~{KIbOK4c9x8u-467^k{h
3M)_aDVd@^+SDm)-*a3b%5ms8o4VOaSi&(<DGcnA9g|S{nnGlZ{@b@6*2tjXW^sVG3);ypNTTtb38%`oc&u7aS6I&-W4%c}uFO7q
bX@P`A<L8@o0jaVYlbV7`e{T?adkibsxl~iEwcx{2ABMF-iRZj&kiW`&P*9jP+;Z}CndLZs8*^>Auu4q4qkq>A|p_2Ko1j>?xCW)
&Bi2B&xyIaU~3^MlQemCyqW1<h3ufUgNWwWSOnxWJ&D7==dAWPpItt_F(>|i^4-ORsy42>d-8F(FU)Ggdcm&4a=DLr-8qF(#+~ay
3QbB3I1mqF8G6)fY7j>NElfeBH4l`8IqV?li!Y%MCfHzDMP_;qe{J|?B?lYI)s);M5#TCrW>yT>Bs=_VQeqKyCYQ%NQT9ljT`^dj
925mzB{s`8LY&_ca}^JY3CaxZ9v?ZxhnS_kdsA+^`P_dJ$N7Sei%H(AAle~1;~>a6oems19CKh`g-Zxd0-&Q`qQrEe&kI>g?eLnn
7umAK7-_U)k$2{Ze-e^`?G+`{$9%?Waud9T%KIWVLc5&3>tIbH;WK8**6SZ|01q($kV|I%ACJfTxx08z*3(!GT?mN%ee9a3<^E8K
Fo%=gFO~@5hN9D|@i?Bq>Utl%$j>*D#q55#-qRg}qAC@&jflxTFW&fG&QP4ld-aZ#ccb(l&v#>BEWK&r?1ZUc<Bn<RWVzMf9$XX+
iBKtV^LacFkmAkh<a`3clSijdn3`R~D}6;Sv7q;;es(2vGeXcJ0?vrV4_!5KINpVaIbpv^N=jc7(nk*fUrl4f7NWa3FDE<O6fu%G
PRSaFcEqKv4A5^y!kG~Q-zE_&e{F5`);ZTGXFJLkAJmuVq-Rwhyj=ZHQUbMobbBmAyqZja_pWv>$wS09z`#ivPY{%GIqRBxRf=0~
tAxNNG6e}C1jHiF6;MM$pG;i^b25=r=OH{aH@y3NwSV}H`^+8O^v;miZ%2is$I^pOTztUcgdA>**98GB;N1%y15}Ne#qB@oZ}!6~
1t1l7AtUsbKU^wL)@RbG2mOTD!@nk#O5BX7V0gHe%}?ox1QH|%y7x83%p;jT^;ct3xX&-kNi?5pAd7h=+HTWTe(r;w1HK_$%8S<w
Gfmu8ZDKW`S}42wpP5F!4fxrcxGu>-$k~t!(fXR$(|nLd4w;!Q>AG{d9rz4)aW27Ll!62d$3EH<IqobVlXGp6RLZW>9@)m(hrz{O
`)$)iS%h8*K=7qOE@l@Vz0L}nHjhyMk6c~#HM+fUu^E$SZEO_}PAM>FkS=OG<4W17nICOSREpqKIT_(Ed-+%{1(LL-n@AHyv|FH>
%mVCJsF`})wE+g{mzQF4*LtY~)%BBD1a$J^G%H|%3u{{7A5)<VMxV)71Ou^7jS<nVyib;2SmDNIgeeazDnFG53n$AWT9#>C+Es<s
JJ<dqv<MrXERtjXwo9Q?gDlcN2iTzS#2LtmnGHxkv9qYVwT<=YVot{osR`A)V5oNfMM{92eb+haF{@%Im3ba>T4u*5qoW$^71lS1
j~;Z~;P;&Ps<v}<Y^g&(YcrV74OBu!oSnx1fH#5Ee+-CP;B6GVUnbe%OATx)lHmP3Au4vIkku%DUJ+V)P!!Jq^`rE2TXoFy;m3J>
<zVMzpt0^sWz!@f^OpSDjdU5#ZRiAQ2&3nnHp;LartE?mN$%|JXKdT<s_s5Zd-7@ll2wShHk1B4&2KmS|FGeO+jX5P+E)QkqZ?no
UNfaD;1Q6-ijzigd`S=3lku`^x2iLFoG@I@wt&UBcf!F@G1M&#W|Zp@mcto&>(iJJS3$xJ@yVqFnMUmg-`5#J(LhEE@&T_<=7v2h
xV;KU3K14_^c4B3ys{h^fE+I72p`K>^GoJ^qTTgl%<;xpP6w8&4Wp(_4sfM0<aSusJe1Loi8y<4kQ=ZwFT7bXNYTn+8ZCAZQJG?$
5ieA}9sRoZxZ+OPVjrc)7B<^3;2QT4Fi9rJQd!PFxJf<W?BPrt5^Gx!fnhY3QyD6tU^^;+En_2~-HpR5Ew_60zu;*hH0yC9aZ;mR
+n{Z}rC+*T1fAD;soR;NE`th6Fh8ds<MEhFWR>e1fiKc_X#fBKEU;NseC?=F00E*N;X?obA6QOQvBYQl0ssI200dcD
"""
bs=lzma.decompress(base64.b85decode("".join(B85.split())))
assert len(bs)==8673
assert hashlib.sha256(bs).hexdigest()=="919b94bf5af70e06f6014aed79cdbbaa095487091c5b527444c5ab4b97f50a39"
for name,text in json.loads(bs).items():
 p=Path(name);assert p.name==name and not p.is_absolute()
 p.write_text(text)
```

**Final status:** the complete finite supporting-closure/opposite-region moment construction is established and exactly nonwinning. The fixed-ARC34, fixed-zero-centre, single-cut problem is globally closed; genuinely changed multi-cut or moved-support constructions remain open. No strict own110/E<500 is claimed.
