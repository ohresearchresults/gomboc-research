# figure-0405

Historical AI scientific report · saved 2026-09-18 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Harbor03 — global reference-center geometry

Assignment: `figure-0405`.

## 1. Result and remaining question

**Neither an exact reference110 center for either assigned nonwinner nor a global exclusion certificate was obtained.** The final global solver checks returned `unknown`, with reason `timeout`. They establish no infeasibility.

The substantive result is a complete, boundary-aware reduction of the free-reference problem to **three real variables and rational affine predicates**. It includes all stable faces, unstable vertices, saddle edges and weak-only features, without fixing either root or any escape witness. A stronger simplification emerged: **the saddle predicates introduce no additional equilibrium hyperplanes**. The entire feature census uses the physical directed-edge and facet-side hyperplanes: exactly `4E` distinct equilibrium hyperplanes for each of the three reconstructed bodies.

The reduction was implemented and checked against the exact parent reports. It also passed a known-feasible CONDITION25 control, including an exact rational reference110 center, a certified reference-center box, a solver SAT check, and explicit interior weak-boundary controls. This is a reusable global formulation, not a completed global coverage computation and not a new homogeneous Gömböc.

## 2. Exact bodies and source authority

The CONDITION25 control is the distinct `COORD_C622_CONDITION25_G12` body, V176/E311/F137, own110/weak000. It is not a renaming of the canonical C622 body. Its complete reconstruction requires all three CONDITION25 source parts. :contentReference[oaicite:0]{index=0}

The first target is exactly `COORD_C620_ALLWITNESS174_G12_OWN132`, V175/E310/F137. At its filled centroid, S is support3, U is raw-lex94/173/174, and H consists of 172–174 and 173–174; weak-only counts are000. :contentReference[oaicite:1]{index=1}

The second target is exactly `COORD_C616_COLLAPSE132_OWN132`, V174/E308/F136. Support84 is redundant. At its filled centroid, S is support3, U is raw-lex94/166/173, and H consists of166–168 and172–173; weak-only counts are000. This is not either old delete99/117 C616own121 body. :contentReference[oaicite:2]{index=2}

The exact report identities used and reproduced are:

| Body | Report bytes | SHA-256 |
|---|---:|---|
| CONDITION25 | 313272 | `41b440d3a557a88f0abfc4b2e1bde8b99c8793b173d433c7dfad162fefd4878d` |
| C620 ALLWITNESS174 own132 | 314808 | `f30fc15a826c78fb05d994a506d97e953e6793472657749f2abc99fce006660a` |
| C616 COLLAPSE132 own132 | 312051 | `ba4bd93b8fade753cea37dc5a7b36f030fc2d55127fb7c043e01893f4ff94eb9` |

Actual replay status in this turn: both independent A/B reports completed and agreed for C620 and C616. CONDITION25 B completed with its expected report hash. A separate fresh-source B reconstruction also reproduced all three report hashes. That fresh reconstruction was interrupted during the third body and its final B invocation was resumed separately. The third centered-mass integrations in the original full audit wrappers did not complete in this turn; their terminal whole-wrapper markers are not claimed here. The parent capsules report their earlier completed A/B/third-mass checks. The newly executed free-reference checks use the exact geometry and centroid in the hash-identified reports.

The prior100-start center search remains only a finite negative observation, with frozen beta−0.03646264655608652 and displacement0.01574467954494654. It is not a global exclusion. :contentReference[oaicite:3]{index=3} The exact own-centered bottleneck certificates likewise do not exclude another reference center; the physical barriers near−0.055759458 and−0.055759573 concern the specified centered bodies. :contentReference[oaicite:4]{index=4}

Historical library reading was selective, not an exhaustive audit. I read the complete material `[internal-source-reference]`, SHA-256 `9e864723da43fed083af74156fcb2df539db72a6588a1e48a9933949be8b8f33`, through EOF. It concerns the different `COORD_C620_VIRTUAL99_REFERENCE110_OWN60_78_136` body. Its reported exact nearest point belongs to one selected witness cell, with active physical130→144 and polar37→66/133→27 and distance between173199/10^9 and173201/10^9. That result is not an all-cell exclusion and cannot be transferred to either assigned target. No complete historical all-root exclusion for these two targets was recovered in this pass; this is not a claim that no such source exists elsewhere in the history.

## 3. Complete affine feature reduction

Let P have exact vertices x_i, actual maximal facet inequalities n_f·x≤h_f, outward-oriented facet boundary cycles, and true edges. Let c be the reference center. Interior is exactly

`I_f(c) = h_f − n_f·c > 0` for every active facet.

For each directed true edge i→j, define

`R_ij(c) = (c − x_i)·(x_j − x_i)`.

These signs are the negatives of physical escape signs. A vertex i is strictly unstable precisely when every incident R_ij is positive. It is weak-only precisely when all are nonnegative and at least one is zero. Otherwise at least one R_ij is negative. True incident edges suffice because their directions generate the tangent cone; this is not an assumption about triangulation edges.

For each directed boundary edge i→j of an outward-oriented maximal facet f, define

`T_f,ij(c) = n_f·((x_i − c) × (x_j − x_i))`.

Projection of c onto the supporting plane changes x_i−c only by a multiple of n_f, which disappears from this scalar triple product. Thus a face is strictly stable precisely when all its boundary T predicates are positive; it is weak-only precisely when their minimum is zero; it is absent as an equilibrium when their minimum is negative.

### Saddles reuse the same hyperplanes

For a true edge {i,j}, put d=x_j−x_i, D=d·d, z=x_i−c and a=z·d. The line foot has segment parameter −a/D. Its radial vector multiplied by D is

`p_num = D z − a d`.

Let n,m be the two adjacent outward facet normals. The standard four saddle tests are positivity of

`−a`,
`D+a`,
`p_num·((m·m)n − (n·m)m)`,
`p_num·((n·n)m − (n·m)n)`.

The first two are R_ij and R_ji. For the adjacent facet cycles, the last two are positive multiples of their T predicates. One way to see the signs is to orient d along the first face boundary: convexity gives d=λ(n×m), λ>0, and hence

`d×n = λ((n·n)m − (n·m)n)`.

The other face uses −d. Also each normal-cone vector is perpendicular to d, so replacing z by p_num merely multiplies its dot product by D>0.

The implementation independently constructs all four line-foot/normal-cone affine forms, clears denominators with a positive multiplier, divides by the positive integer gcd, and asserts exact equality with the shared R/T forms on **every true edge** of all three bodies. Consequently, strict H means all four shared forms are positive; weak-only H means all are nonnegative with a zero; absence of both strict and weak H means at least one is negative.

This establishes the complete boundary predicates directly. It does not infer H=0 from S/U or from an Euler count.

### Global Boolean formula

Introduce one Boolean s_f per maximal facet and one Boolean u_i per vertex. Require exactly one s_f and exactly one u_i. For each face impose:

`if s_f then all T_f>0 else at least one T_f<0`.

For each vertex impose:

`if u_i then all R_i>0 else at least one R_i<0`.

For every true edge require at least one of its four saddle predicates to be negative. Add all interior inequalities I_f>0.

**This formula is equivalent to reference strict110/weak000 on the entire interior of the fixed body.** Neither roots nor witnesses are fixed. There is no0.2 displacement box, artificial positive margin, frozen normalization, assumed contact lattice, or sampled arrangement in the formulation. Zero primitive signs are permitted when another strictly negative predicate keeps the feature away from equilibrium; actual weak equilibria are excluded explicitly.

Positive escape cycles need no additional constraints: along an escape arrow A_ij=−R_ij>0,

`|x_j−c|² = |x_i−c|² + 2A_ij + |x_j−x_i|² > |x_i−c|²`.

Thus any outgoing choices for nonroot physical vertices cannot cycle. The analogous polar argument recovers the witness-tree interpretation without enumerating trees.

The actual generated sizes are:

| Body | Raw predicates including edge tests and interior | Distinct equilibrium hyperplanes | Affine forms including interior |
|---|---:|---:|---:|
| CONDITION25 | 2625 | 1244=4E | 1381 |
| C620 own132 | 2617 | 1240=4E | 1377 |
| C616 collapse own132 | 2600 | 1232=4E | 1368 |

These are counts of the generated formulation, **not counts of covered arrangement cells**.

## 4. Exact controls and literal outcomes

At the exact own centroids, the new facet signs and all four signs on every true edge matched the parent reports entry-for-entry. The strict/weak feature lists also matched, including the vertex classification obtained independently from true incident edges.

For CONDITION25, the following small-denominator reference center was additionally checked exactly:

`c0 = (−1692341437/125000000000, 5663754857/1000000000000, −9369935897/1000000000000)`.

It is obtained by rounding each exact filled-centroid coordinate to the nearest multiple of10^−12, ties to even. The exact census is strict110/weak000, S=face3, U=raw-lex94, H empty. Interior was checked with exact arithmetic. Its displacement from the own centroid satisfies `||c0−g||∞≤1/(2·10^12)`.

A deterministic selection of823 strict affine inequalities certifies that **every center with `||c−c0||∞≤1/10000000` remains interior and reference110/weak000**. For each absent face/vertex/edge the code selects the first negative predicate and reverses its sign; roots retain all their positive predicates, and all interior predicates are retained. For each selected row a0+a·c, the exact radius test is `(a0+a·c0)/sum|a_k|`. The returned1/10000000 is strictly smaller than every applicable ratio. The source contains the entire selection and verification recipe; no823-row external witness file is missing.

This is a control chamber on the existing CONDITION25 body, not a chamber for either target and not a new body. A fixed-c0 instance of the same global Boolean formulation returned SAT with libz3 version4.13.3.0.

Weak-boundary controls use the explicit tetrahedron with vertices `(0,0,0),(1,0,0),(0,1,0),(2,2,1)`. Full oriented faces and normals are literal in the source. All four centers below are strictly interior:

| Reference center | Strict S/U/H | Weak-only S/U/H |
|---|---|---|
| `(3/10,3/10,1/10)` | 3/2/3 | 0/2/2 |
| `(301/1000,3/10,1/10)` | 3/4/5 | 0/0/0 |
| `(299/1000,3/10,1/10)` | 3/2/3 | 0/0/0 |
| `(7/15,7/15,1/10)` | 3/4/5 | 1/0/1 |

Thus vertex/edge and face/edge weak transitions are exercised explicitly, rather than only testing generic strict centers.

Final recorded solver observations used the complete global formulas, with timeout10000 milliseconds per check:

`CONDITION25 fixed c0: sat`.

`C620 global: unknown; detail (:reason-unknown "timeout")`.

`C616 global: unknown; detail (:reason-unknown "timeout")`.

The exact control marker `EXACT_REFERENCE_FEATURE_LRA_CONTROL_PASS` was observed for all three bodies. It means the feature formulation and controls passed, not that the target existence question was solved. No target model, complete arrangement coverage, or independently checkable UNSAT certificate was produced. An earlier control attempt with the enormous-denominator exact centroid failed to return SAT in that attempt; its backend status was not retained and has no negative evidentiary value. The final small-denominator control supersedes it as the explicit feasibility test.

## 5. Durable recovery and reproducibility

### Exact inherited inputs

Use all three CONDITION25 immutable materials as `parents/part1.md`, `parents/part2.md`, `parents/part3.md`:

`[internal-source-reference]`, `[internal-source-reference]`, `[internal-source-reference]`.

Their joined normalized base64 has36568 characters and SHA-256 `6311ad9802f5a98c2600fa2d856a64af0f7a19d055c2d9849e0080c141f00c50`; decoded24-file dictionary93169 bytes, SHA-256 `631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3`.

Use `[internal-source-reference]` as `parents/own132.md`. Its normalized base64 has10536 characters, SHA-256 `7e00bccdeb2da1228fa060f2c5f8997f5cca71c2954f733beea58b703df0f85a`; decoded dictionary19545 bytes, SHA-256 `8c876916dba1c272adcf8ec3ee4e16df120ad479b4386060e09e2b7b18a65c15`.

The embedded new source contains the complete C616 contact-collapse operation, including dependency ordering, so recovery needs no missing patch helper. It appends support105 to group31/pointcontrol168, replaces the support105 dependency by point168 solving axis0, and topologically reorders the DAG starting from fixed137. It asserts the exact resulting generator SHA-256 `4eb48034bf6d6d429c593977bee2b934759ba2c3a22865788880d4e18741720a`, agreeing with `[internal-source-reference]`. The C620 parent generator SHA-256 is `38ebffa8f00ba3b67e105463bf162f8ac766ce2d738bf3e7a8271539d8d05cd6`.

The recovery path uses the complete inherited exact RECONSTRUCT and check_B source, not the numerical discovery producer. No originating sandbox, old process, NumPy or SciPy installation is required.

### New source and frozen records

The following inline capsule contains all bytes of five files: the complete178-line `REFERENCE_LRA.py`, the three complete frozen RESULT.json records, and their manifest. It does not omit any helper used by the new method. Its decoded UTF-8 JSON dictionary is15639 bytes, SHA-256 `d4c049fa4939b3d216ebe9df8f983420985882e089aaa27b9ca02c5a281ecb0e`. Its whitespace-stripped base64 has7800 characters, SHA-256 `45c7ea3fd8c259404c8ef2bded96b98266dce6ef514288acf89bba7684c6819e`.

Save the base64 block as `CH03_LRA_SOURCE_CAPSULE.b64` and run this complete standard-library decoder:

```python
from pathlib import Path
import base64,hashlib,json,lzma
H=lambda b:hashlib.sha256(b).hexdigest()
s=''.join(Path('CH03_LRA_SOURCE_CAPSULE.b64').read_text().split())
assert len(s)==7800
assert H(s.encode())=='45c7ea3fd8c259404c8ef2bded96b98266dce6ef514288acf89bba7684c6819e'
b=lzma.decompress(base64.b64decode(s,validate=True))
assert len(b)==15639
assert H(b)=='d4c049fa4939b3d216ebe9df8f983420985882e089aaa27b9ca02c5a281ecb0e'
d=json.loads(b)
assert len(d)==5
out=Path('reference_lra_capsule')
out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
    q=Path(name)
    assert not q.is_absolute() and '..' not in q.parts
    p=out/q
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
m=json.loads((out/'LRA_MANIFEST.json').read_text())
for name,v in m.items():
    raw=(out/name).read_bytes()
    assert len(raw)==v['bytes'] and H(raw)==v['sha256']
print('CH03_REFERENCE_LRA_SOURCE_RECOVERED5')
```

```base64
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
```

### Commands, versions and expected outputs

Run with assertions enabled; do not use `-O`. The tested interpreter was CPython3.13.5, version string `3.13.5 (main, Jul 15 2026, 20:25:40) [GCC 14.2.0]`. Exact reconstruction and feature checks use only the standard library. Optional solver calls use the locally available shared library `libz3.so.4`, reporting version4.13.3.0, through ctypes; no Python z3 package is required.

From the directory containing the recovered script and the four parent material texts:

```sh
python -B -S REFERENCE_LRA.py --recover parents/part1.md parents/part2.md parents/part3.md parents/own132.md WORK
python -B -S REFERENCE_LRA.py WORK/REPORT622.json RUN622 --solve-ms 10000 --fixed-control
python -B -S REFERENCE_LRA.py WORK/REPORT620.json RUN620 --solve-ms 10000
python -B -S REFERENCE_LRA.py WORK/REPORT616.json RUN616 --solve-ms 10000
```

All destination directories must be new. Recovery's expected final marker is `EXACT_REFERENCE_LRA_THREE_INPUTS_RECOVERED`; in this turn its three report outputs were verified after the interrupted third call was separately resumed. Each completed feature run emits `EXACT_REFERENCE_FEATURE_LRA_CONTROL_PASS`.

Without the shared solver library, omit `--solve-ms` to execute all own-center and boundary controls and generate a global formula. The timeout header then differs, so its SMT file hash will differ from the10000ms files below. The extra small-denominator control and its box are executed by the `--fixed-control --solve-ms 10000` command.

The source file is11491 bytes, SHA-256 `88cbab1d3e300fd463076a2cea3398d0667b4fa9b69cb316509525705028940a`.

| File | Bytes | SHA-256 |
|---|---:|---|
| RUN622/GLOBAL.smt2 | 582334 | `3d1dd49c5d8b3342fd0905c73b999f899048b95833d7575afa00f839bbc153b6` |
| RUN620/GLOBAL.smt2 | 585967 | `7bed7841b72090a228c3388abf80392bbbcd79b82f9568ee260f232d0507c433` |
| RUN616/GLOBAL.smt2 | 579206 | `353085c85defc5eefc2a484583f497c4806797576feeb77e31f44b9e11aa5168` |
| Frozen622 RESULT.json | 1070 | `544732e04d94ac09b91105ca12bd9520e1081373867738ff84bcfe60e92820fc` |
| Frozen620 RESULT.json | 952 | `11947ba06c727dfd054db4aa508a9dfcde5eed570977f7c7690c2acedb6d2142` |
| Frozen616 RESULT.json | 950 | `2b58f2f64722476b193cc5cefe086fd6546f107e55850ff757d70fde6b372740` |

The complete frozen records are inside the inline capsule. Formula generation is deterministic for these exact inputs and timeout setting. RESULT identities also contain the interpreter version and observed solver outcomes, so those identities need not survive a different environment or a differently completed time-limited solve. A future target SAT result printed by this script is a candidate until its rational model is independently passed through the full interior and feature census; a future UNSAT result is not the independently replayable exclusion certificate requested here unless its proof or complete coverage certificate is also preserved.

For convenience, the [supplementary executable bundle](sandbox:/mnt/data/CH03_GLOBAL_REFERENCE_LRA_v1.zip) contains the source, parent material texts, all three exact reports, formulas and frozen records. It is1124004 bytes, SHA-256 `c914cb2258c8c389eb33f1b0c1ddea75e90b8cd78f23e603d6100169a368e290`. The inline source capsule and the named immutable parent reconstruction above remain the durable recovery route; the bundle is not the sole source.

## 6. Mass closure and the most useful continuation

Changing c in this calculation does not change the body's filled centroid g. Consequently, even a target reference110 solution would be an enabling configuration, not an own110 construction.

For a genuinely changed homogeneous body P′, exact mass closure at a proposed center c requires

`V(P)(g−c) + ∫[P′\P](x−c) dx − ∫[P\P′](x−c) dx = 0`.

For pure addition of volume v with centroid a, this specializes to `v(a−c)=V(P)(c−g)`; for pure removal, `v(a−c)=V(P)(g−c)`. These are mass identities, not existence proofs for a convex exposed modification. Convexity, actual incidence, and the new body's complete equilibrium census must still be checked after the change. Because no target chamber was found here, no specific exposed mass correction is claimed to close either target.

The most useful continuation is to work from the generated **full-feature global formulas**, rather than restart a center-policy loop. A positive branch should supply a rational c, exact S/U/H and weak lists, and a selected strict-cell box as in the control. A negative branch should produce a complete rational sign-branch certificate over P's interior. Branching a predicate into `<0`, `=0`, `>0` covers weak strata explicitly. An empty leaf can carry a rational mixed-strict linear infeasibility certificate: nonnegative multipliers cancel all center coefficients and give a negative combined right-hand side, or give zero with positive weight on at least one strict inequality. Nonempty terminal leaves must fail the target feature formula. Every branch and every leaf must be accounted for before calling the result an exclusion.

Current conclusion: the global reference110 question for both assigned targets remains undecided; the complete affine formulation, exact saddle-hyperplane reduction, verified control chamber, weak-boundary tests and reconstructible inputs are ready for that next decision step.
