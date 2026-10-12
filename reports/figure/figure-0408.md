# figure-0408

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Sharp Raven 82 — finite shape–mass gates, genuine moment transport, and seven exact nonwinners

Branch: `[internal-source-reference]`.

## 1. Outcome and authoritative starting point

**No new own-centroid110/weak000 body was found.** Seven genuinely changed rational bodies with E<311 were retained and independently exact-audited. Three retain reference110/weak000 at specified rational points, but their ordinary uniformly filled centroids do not reach those points. Nothing in this handoff improves the supplied own110 incumbent.

The strongest new results are a finite-shape ordinary-mass obstruction for three small partial witness systems, a real E308 fixed-reference mass correction that reduces every ordinary first-moment error component by more than 10.4%, and a separate actual-hull continuation to E177 nonwinners, including a 61-vertex body with a 129-bit common centred denominator.

The complete five-text input pack was read, including the entire journal, its literal parent payload and the four coordinate source materials. The source closure was sufficient; no fifth C616 patch or external archive was needed. I used the literal parent `figure-0406`, envelope SHA-256 `8f63bbe8ff6c44a2ffa9e6030c14db1962f3e21e22ece583de1ea1db0cc68246`. Source-authoritative C616 is V174/E308/F136, own132; C620 is V175/E310/F137, own132, not HA39/V174/F138 or an own121 alias. The inherited rational reference centres and their different stable roots are used as supplied.

I did not rerun the solved global fixed-shape centre search or closest-centre optimization. Their inherited conclusions are kept separate from the new physical bodies. The capsule below embeds the complete required parent generator, exact recovery code, new inputs and all necessary auditors. It needs no supplied material file, journal, sandbox or numerical rediscovery to recover these seven exact endpoints.

## 2. New finite-shape ordinary-centroid obstruction

### 2.1 Precisely quantified statement

Write the source support representatives as `N_i = H_i[:3]/H_i[3]`, using original input support IDs. Consider any full-dimensional uniformly volume-filled convex polyhedron K, with 0 strictly inside it, and valid inequalities

`N_i · x <= h_i`, with `h_i > 0`.

All heights, all other boundary pieces, all other supporting planes and the entire remaining face lattice may change. Let `u` be a point of K at which the six stated support inequalities are equalities. The theorem does not prescribe u's coordinates, require u to be an unstable equilibrium, or prescribe a stable root.

Define `r_ij = (N_i·N_j)/(N_i·N_i)` and `e_ij = r_ij h_i - h_j`. A positive e_ij means the perpendicular foot of 0 on plane i lies beyond inequality j, and hence excludes stability on i. In the source cells, the listed pairs are actual adjacent-facet, first-negative-side witnesses, not merely an all-pair surrogate.

For each packet below, **the six contacts and the closed inequalities e_ij >= 0 on every listed arrow are incompatible with g(K)=0**. This is a finite ordinary-mass obstruction, not a first derivative calculation, fixed-shape centre exclusion or solver infeasibility report.

| Packet | Two directed chains | Two internal contact arrows | Required contacts at u | Certified componentwise normal box |
|---|---|---|---|---|
| near | 22→62; 96→61→78 | 29→30; 33→34 | 22,29,30,33,34,96 | 1/10000 |
| simple | 1→6→111; 19→54→53→89→110→124→125→126 | 24→23; 68→67 | 1,19,23,24,67,68 | 1/1000 |
| discovered | 1→6; 2→52→51→87→108→128 | 41→42; 98→64 | 1,2,41,42,64,98 | 1/10000 |

The packets have respectively 5/11/8 arrows and 9/15/12 normals. Only 34 different literal source normal rows are needed for all three.

Each normal-box statement permits independent real perturbations of every component of every listed N_i by at most the displayed amount, in this explicitly specified representative gauge. Heights remain arbitrary positive reals. The contact and arrow hypotheses must still hold. The boxes are conservative certified boxes, not maximal radii, rotationally invariant distances or Hausdorff bounds.

**Scope is essential:** these are three specified partial witness regions, not the full union of reference110 geometries. Releasing a required contact, choosing different surviving witnesses, or changing normals outside the certified region leaves the theorem's hypotheses. The physical construction in Section 3 actually does leave the near packet; the theorem must not be reused to forbid that construction.

### 2.2 Elementary mass identity and strictness on the closed witness boundary

For any u∈K, triangulate the boundary and cone it to u, omitting zero-volume tetrahedra. A positive tetrahedron with apex u and base-triangle centroid b has centroid `(u+3b)/4`. Averaging by its actual positive volume gives

`(4g-u)/3 ∈ K`.

Consequently, every valid support inequality supplies

`K_i := N_i·u + 3h_i - 4N_i·g >= 0`.

For two linearly independent terminal normals, a positively weighted sum of their K_i is strictly positive. Otherwise both K_i would vanish. Every positive cone tetrahedron's base centroid would then lie on both support planes; since all base vertices satisfy both inequalities, all three base vertices would lie in the planes' intersection line. A positive-volume tetrahedron cannot have a collinear base. This proves the strictness needed below, including when some e_ij=0.

For a chain `i_0→...→i_m` with all r positive, put `p=product(r)` and use the exact telescoping identity

`p h_(i_0) - h_(i_m) = sum_l [product_(k>l)(r_k)] e_l`.

When its initial support contacts u, its associated vector is `W_chain = N_(i_m) + 3p N_(i_0)`. For an internal arrow whose two supports contact u, use `W_internal = r_ij N_i - N_j`.

In the order `[first chain, first internal arrow, second internal arrow, second chain]`, each packet has four W vectors with a strictly positive exact dependence

`a_0 W_0 + a_1 W_1 + a_2 W_2 + a_3 W_3 = 0`, all `a_k > 0`.

The verifier clears positive denominators and computes the four signed 3×3 cofactors. Their common sign is checked, their integer weights are reduced, and every coordinate of the weighted sum is verified to be exactly zero.

Let `t_0,t_1` be the two chain terminal supports and define

`L = (a_0 N_(t_0) + a_3 N_(t_1))/(a_0+a_3)`.

Combining the dependence, contact equalities and the cone mass inequalities yields

`-4 L·g = positive weighted kernel slack + sum_(i,j) beta_ij e_ij`,

where all beta_ij are positive and the kernel-slack term is strictly positive. Therefore `-4 L·g > sum beta_ij e_ij >= 0`, contradicting g=0. The exact verifier independently expands and cancels the complete symbolic identity in all h_i and the three components of u. Rational interval arithmetic proves positive chain ratios, the common strict cofactor signs and independence of the terminal normals throughout each stated normal box. Thus the proof applies to finite changes of shape and actual mass, including arbitrary additional valid inequalities, under its explicit hypotheses.

For orientation only, the separators L in the source axes are approximately:

```text
near        (-0.5958555909112105, -1.5074138517314355, -0.7916483742119449)
simple      (-0.9960312617236038, -0.041023169913438094, -1.1868795207289666)
discovered  (-0.8977705706733613,  0.36994239249531546, -1.1892382768143300)
```

The complete rational values, positive circuit weights, all escape coefficients and normal-box certificates are regenerated, not inferred from these decimals.

### 2.3 Exact execution and source binding

`THREE_GATES_INPUT.json` contains all 34 complete integer normal rows, all three literal reference centres, every chain and internal arrow, and both parent report hashes. It is 4539 bytes, SHA-256 `60e161361baad07f94817dbaf427f3a3dd7259d22cd75053c6e302980862ce0c`.

`three_gates.py` and `bind_gates.py` were executed with rational arithmetic. Binding checks every supplied normal against both independently reconstructed parent H-descriptions and verifies every listed arrow against the actual canonical outward facet cycles and true-edge adjacency. Each is the first negative facet-side choice in the corresponding supplied reference cell.

```text
THREE_GATES_CLOSED/CERTIFICATE.json
40280 bytes; SHA256 3c1c4b4f6d2201f8f0d877f1f1610d3284e5e59bb0b41c7f1720e27a93e822e7

GATE_BINDING.json
3505 bytes; SHA256 5601032cd6f91091c1825e3b1f03e14b3d3317b8a236a39197841cc4d1e396f7
```

This closes the three stated finite-height/contact/witness architectures. It does not close arbitrary height charts with unrestricted witness turnover, any entire normal orbit, or the physical realization question.

## 3. An actual E308 fixed-reference mass correction

### 3.1 Exact endpoint and ordinary moment progress

`MASS_NEAR_EXACT` is a different homogeneous rational polyhedron with V174/E308/F136. The same literal point

`c = (-290787037/1000000000, -270371541/1000000000, -68565859/250000000)`

is reference110/weak000 on it. Its unique reference stable facet is original support90; its unique reference unstable point remains exactly `(0,0,1)`, now raw-lex vertex96. Independent direct projection/normal-cone and affine-form audits agree on the entire feature census. A closed L-infinity box of radius 1/100000000 around c stays within a certified strict witness polyhedron.

Its own-centroid class is **(35,25,58), weak000**. It is not a Gömböc or an own-centroid successor to the incumbent.

Approximate values, with exact quantities reconstructed by the capsule:

```text
Parent C616:
  V = 0.4887907847041145
  g = (-0.0135664289668713, 0.0055828257331528445, -0.009444569284946271)

MASS_NEAR_EXACT:
  V = 0.4740993790166344
  g = (-0.03476521466387458, -0.015583941329854724, -0.029704236901838175)
```

Let `d_0=g_parent-c`, `d_1=g_new-c`, and let `M_c(P)=V(P)(g(P)-c)` be the actual ordinary first moment about the fixed reference. Exact rational comparisons prove, separately in every coordinate,

`0.923 < d_1[k]/d_0[k] < 0.924`,

`0.895 < M_c(P_new)[k]/M_c(P_parent)[k] < 0.896`.

Thus **every ordinary first-moment error component is reduced by more than 10.4%**, with no density change or reference-point substitution. The three moment ratios are approximately 0.895772756233, 0.895544959049 and 0.895738946842. The actual volume ratio lies in `[0.969943366063,0.969943366064)`.

The Euclidean centroid-gap ratio is strictly between 0.923439887 and 0.923439888, a reduction of about 7.6560%. The new exact L-infinity gap lies in `[0.256021822336, 0.256021822337)`.

That is below the inherited fixed-C616 infimum 0.27721934672215..., because the geometry has actually changed. It is not a new fixed-body optimum and proves no Hausdorff-distance statement. The parent explicitly restricts its old bound to the unchanged body.

### 3.2 Genuine witness turnover, not frozen old choices

At the parent near reference, facet22 has valid escaping adjacent facets62 and33; the canonical first-negative selector uses62. At the new endpoint:

```text
                     parent      MASS_NEAR_EXACT
e_(22,62)               >0               <0
e_(22,33)               >0               >0
e_(96,61)               >0               >0
e_(61,78)               >0               >0
e_(29,30)               >0               >0
e_(33,34)               >0               >0
```

Both 22–62 and 22–33 are genuine adjacent facet pairs. All six near-packet contacts at the inherited apex remain exact. The fourth natural cofactor has changed sign; its new/source ratio lies between -0.041115861881 and -0.041115861880. The other three cofactor ratios remain positive.

Accordingly, the endpoint is outside both the old selected-arrow packet and its original positive-circuit normal component. **Do not spend the next continuation trying to cross the old 22→62 or fourth-cofactor gate: the retained endpoint has already left them.** The 22→33 alternative was already available at the parent; it was not an invented new edge. Exact endpoint comparisons establish these statements; no exact chronology of the intervening crossings is claimed.

### 3.3 What was constructed and checked

The producer used all 312 free coordinates of the rational contact DAG, analytic derivatives of the ordinary filled-volume centroid, and maximum-witness turnover on both the physical body and its same-reference polar. It did not fix the old own-stable support3 or every inherited escape choice. All 100 numerical steps in the first mass run were accepted with positive nominal exposure and reference gates. The final frozen endpoint, rather than a nominal mesh or sampled path, was reconstructed and audited exactly.

Independent exhaustive-triple A and support-pair B agree byte-for-byte. The third centred integer-tetrahedron integration has 344 positive tetrahedra, exactly zero filled first moments about the actual centroid, and common centred denominator 56228 bits. All strict and additional weak feature lists were recomputed on maximal faces and true edges. All primitive-zero counts are zero.

`PHYSICAL_PROGRESS.json`, 1787 bytes, SHA-256 `ceea6cadd3d6ba20de762f6a7cb2f1b986023a265bb91aeb0cb2c526ffd9900a`, contains exact enclosing fractions for every progress ratio and the witness/cofactor comparisons.

## 4. Seven retained exact geometries

Every row below is an executed exact A/B/third-mass result. All seven have additional weak000 and primitive-zero000. The denominator column is the bit length of a common denominator after subtracting the actual filled centroid, not the number of decimal places in a producer grid.

| Recovered directory | V/E/F | Own strict S/U/H | Common centred denominator bits | Additional exact reference result |
|---|---:|---:|---:|---|
| MASS_NEAR_EXACT | 174/308/136 | 35/25/58 | 56228 | 110 at fixed near centre; S90; radius 10^-8 |
| SIMPLE_EXACT | 174/308/136 | 34/18/50 | 56381 | 110; S126; radius 10^-7 |
| NEAR_EXACT | 174/308/136 | 33/19/50 | 56440 | 110; S90; radius 10^-7 |
| ACTUAL_NEAR_EXACT | 142/238/98 | 11/7/16 | 57631 | Not claimed |
| FREEH98_EXACT_OK | 150/225/77 | 6/3/7 | 26634 | Not claimed |
| FREEH_RAW3_EXACT | 118/177/61 | 4/3/5 | 20941 | Not claimed |
| FREEV61_EXACT | 61/177/118 | 3/4/5 | 129 | Not claimed |

The earlier two homotopy references, in their raw coordinate systems, are exactly:

```text
SIMPLE_EXACT:
(-216881456713/1000000000000,
 1712790276/1000000000000,
 -431459171039/1000000000000)

NEAR_EXACT:
(-281003561193/1000000000000,
 -260444410597/1000000000000,
 -265439007157/1000000000000)
```

Both have reference unstable point `(0,0,1)`, raw-lex99. These are changed finite bodies, but their reference-to-own interpolation did not close mass. Their retained numerical interpolation parameters were respectively 0.13919360586437501 and 0.036720706250000006; those decimals do not define the exact bodies. The complete frozen integer free-coordinate tables do.

### 4.1 Actual exposed-hull rearchitecture

The separate ACTUAL_NEAR route starts with a physical projective scout, using `x -> (1+a_z)x/(1+a·x)`, then changes the complete contact controls while rebuilding the actual exposed hull and reintegrating its filled volume after topology changes. It is not a push-forward nonuniform density and does not integrate an obsolete boundary. The exact endpoint has only98 maximal supports and238 true edges. Its convexity, maximal complex and own class11/7/16 were reconstructed independently.

Next I deliberately released the contact chart and used the98 active support rows as independent normal variables. The completed cosine-normalized run was frozen and exactified as FREEH98_EXACT_OK. **Its exact 150/225/77 census supersedes the numerical nomination 152/228/78.** A second numerical max-objective intermediate is preserved as a complete rational input for the following raw-objective producer, not promoted as another exact endpoint.

The raw-objective continuation gives FREEH_RAW3_EXACT:98 supplied halfspaces,61 active,118 vertices and177 edges. The very small raw escape residual did not represent an own110 near-hit: the full exact class remains435. Lowering that surrogate did not achieve the requested cancellation and does not establish proximity to a valid cancellation. This is finite diagnostic evidence, not an exclusion of its realization family.

### 4.2 Preserve all98 rows; distinguish a deliberate61-row future family

FREEH_RAW3_EXACT/RAW.json retains **all98 supplied rows**. `physical_results.py` separately generates H61_ACTIVE.json from its exact active support IDs. Independent exact audits prove the present polyhedra identical: their complete reports agree after removing only the input-index map. The output directory H61_ACTIVE_EXACT is a second representation of the same current body, not an eighth changed body.

These are different continuation families. Keeping all98 input inequalities permits only7 further inputs under the unconditional105-input cap. Deliberately dropping the37 redundant inputs gives a61-input family with44 further support slots under that cap. Since E<=3F-6 for a3-polytope, at most105 supporting inequalities guarantee E<=309. A count of61 currently active facets is not permission to add44 while silently keeping potentially reactivating old rows.

### 4.3 A lower-arithmetic physical vertex descendant

FREEV61_EXACT starts from a numerical, grid-10^8 version of the own-centred polar of FREEH_RAW3_EXACT, then changes the actual physical vertices and freezes grid10^9. It is **not the exact polar**, and no preservation of the polar's own centroid is asserted.

Its complete61-point integer input is2030 bytes, SHA-256 `45c7bcbe1364fbc41ed6b551b57222bc1a19c86c34d0907e847335a7b7594465`. `audit_points.py` applies an exact rational mean translation, enumerates supporting triples, reconstructs the true maximal H-complex, runs both independent auditors, and integrates the actual mass. All61 points are exposed. There are118 positive centred tetrahedra and a129-bit common centred denominator. The whole own census is345/weak000.

This provides a different low-arithmetic construction platform, with44 additional physical point slots while retaining V<=105 and hence E<=309. It has more unwanted critical points than a one-pair seed and is not claimed to dominate such seeds.

### 4.4 Complete report identities

For each line, A.json and B.json are identical:

```text
MASS_NEAR_EXACT    309669  a6b1d7c7e83105113c4a385b9a8730bce560c56e17e649647fc2c1595d485cbf
SIMPLE_EXACT       310259  1ec0d3e4cdbe610b653854ae22b4140e3dcba2ff71611cb3053bd93f887017a4
NEAR_EXACT         310659  a996eafcfc891ebbd0c7a72055ce7b39b96a88a42018aa6696b50b7ee298b827
ACTUAL_NEAR_EXACT  309063  def2ba3bb7ec599e02768e257759b27f5ac8b326bac9fe08e3233744c45eae46
FREEH98_EXACT_OK   146740  a10d3593051eec2fbaa39992b0af6133a01b0242c1ff7b8b4f84cc7c293c34b4
FREEH_RAW3_EXACT   115290  aff0cf3c73f042d027e9e30abfcfbf152fb95d0c456c9668dd6bf9063ef0bb92
FREEV61_EXACT       26577  8dc4d401e74624f8cd32c9e4ffc72c9727fb6af9af1a30eb06c406d054512b86
```

Every raw input, mass output, reference audit and relevant certificate also has its exact byte count and SHA-256 in the embedded EXPECTED.json. The full feature lists are regenerated by the complete source, not left behind in a sandbox.

## 5. Methods, limitations and useful continuation

The new theorem changes the height-only question: preserving just six apex contacts and one of these small closed escape packets already prevents ordinary centring, regardless of the rest of the boundary. A useful physical continuation must actually leave its hypotheses, not merely supply a full-rank mass Jacobian. The E308 endpoint demonstrates one such departure while retaining reference110.

The main fixed-reference producer used an equality `Dg dz=-alpha(g-c)` to request radial centroid progress. A later1000-step invocation completed only142 attempts before the tool execution limit; it must not be described as1000 completed steps. It reached a numerical gap about0.4361520867, with a near-zero reference escape and severe backtracking. The complete nonradial alternative `mass_steer.py` removes that artificial ray restriction, minimizes a normalized centroid-gradient objective and contracts the trust region after severe backtracking. Its400 attempts completed, reaching a numerical gap0.4350105366, but the minimum reference escape was about1.30e-9 and the minimum nominated six-volume about1.73e-11. These later probes were not exact-audited and are not promoted durable successors to MASS_NEAR_EXACT. Their methods, exact starting body and all parameters are retained; their small progress or stopping behavior proves no geometric impossibility.

For direct continuation from the retained exact mass endpoint, the complete `mass_continue.py` loads the frozen generator's free coordinates, rather than requiring an unavailable Z checkpoint:

```sh
python -B mass_continue.py --center near --generator frozen/MASS_NEAR_EXACT/GENERATOR.json --steps 100 --out NEXT_MASS_NEAR
```

Its zero-step starting-state test was executed. The complete `mass_steer.py` is the nonradial alternative with the same generator argument. Neither is a certified future success. Preserve the live22→33 escape, allow other witnesses and the stable root to change when the actual geometry permits, and recompute the complete own-centroid census at every exact endpoint. The retained E308 chart has only two extra true edges available; significant contact release may require compensating coarsening.

The other useful branch point is the deliberately reduced H61 family or the distinct low-arithmetic V61 family. They have real44-element input budgets, not just a drawing simplification. New whole-basin additions/removals or normal changes can therefore be tested without keeping the record parent's44-valent apex or every old contact. Complete cosine-normalized continuation commands are in NUMERICAL.md. They are proposed next experiments, not experiments claimed completed here.

All numerical producers used CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and one BLAS/OpenMP thread. Their full code and consequential options are embedded. The fixed-reference and actual-contact runs use no RNG; the free-H/free-V jitter seeds and exact starting inputs are retained. Frozen rational inputs, rather than platform-dependent floating iteration identity, define the exact bodies. The executed free-V source and its subsequent single-line cache-mutation repair are both preserved; the exact frozen endpoint and independent audit do not depend on that repair. No full rational continuum certificate for the discovery paths, global geometry exclusion or own110 promotion is claimed.

## 6. Standalone recovery capsule and observed cold replay

### 6.1 What is embedded

The44-file capsule includes the full C620 parent generator and complete C616 collapse/reordering operation; both exact hull auditors and independent centred-mass integrator; every new exact input; the three gate inputs and verifiers; independent direct and affine reference-feature checks including weak controls; all materially used producer units and options; continuation methods; and source/output manifests.

For the four contact bodies, FROZEN_FREE_CONTROLS.json retains all312 independent coordinate indices and every integer value. PREPARE.py fills these into the exact C616 topology. Stored dependent values are inherited instead of retaining redundant rounded producer values, and RECONSTRUCT recomputes them from the exact contact equations. The canonical generators have **exactly the same RAW.json bytes** as the original full producer generators. GENERATOR_PROVENANCE.json records both identities. This changes the recovery representation, not the rational geometry.

For example, the canonical MASS_NEAR_EXACT/GENERATOR.json is11937 bytes, SHA-256 `58aead40db093587b9e503ee640f1f706c5eda00c139c54007e1a86298bd410b`; its RAW.json is15668 bytes, SHA-256 `f7455d3494e127dd2efd58fc27e99a2443b97783bb4a15f1e9afd7d759633962`. No omitted dependent control is a required external input.

### 6.2 Reconstruction and verification

Save the decoder below as RECOVER_PHYSICAL.py and the entire final base64 block as CAPSULE.b64. Run with assertions enabled:

```sh
python -B -S RECOVER_PHYSICAL.py CAPSULE.b64 R82_PHYSICAL_SOURCE
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py
```

The destination must be new. Exact replay uses only the Python standard library; it does not import NumPy, SciPy or a solver. It reconstructs both source-authoritative parent reports, the three finite-shape certificates, all seven new bodies, three full reference audits, the moment-progress identities, and the identical active-only H61 representation. Four explicit weak-boundary tetrahedron controls also pass the independent direct implementation.

For a runtime with short per-call limits, the identical replay is available in complete consecutive stages:

```sh
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py prepare
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py gates
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py MASS_NEAR_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py SIMPLE_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py NEAR_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py ACTUAL_NEAR_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py FREEH98_EXACT_OK
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py FREEH_RAW3_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py FREEV61_EXACT
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py references
python -B -S R82_PHYSICAL_SOURCE/REPLAY.py finish
```

These were executed from a freshly decoded copy of the final capsule. One long multi-body invocation was interrupted during the last point-body audit; that incomplete output directory was separated and the whole point-body audit rerun successfully before the reference and final stages. No partial output was accepted as a pass.

Observed final markers:


[Encoded source block omitted; the code in this passage is incomplete.]


The last marker checks all50 frozen output byte counts and hashes. COLD_RECEIPT.json is348 bytes, SHA-256 `a3eba4566d0d427e6e298291ed5a2462837d10cb243d77dd824fe3b6fcc72b42`. EXPECTED.json is5897 bytes, SHA-256 `5bf5a4125daaa4fa782adecc08116ba59b1819cea50c4723ff708813a779897c`.

Capsule identities:

```text
Normalized base64: 72364 characters
SHA256 1a443c8775608800a4ab12a288f8c88ae6888f0291611126c503eab9d39dff74
XZ: 54272 bytes
SHA256 39b6e511f77109f860dc79f5c7cea95c712f63b8004884dd4f65c5f5280a7888
Decoded UTF-8 JSON dictionary: 206113 bytes, 44 complete source files
SHA256 1b19dac3308a9bdb41921797bbfe8cfbce67a377525e8efdc82dc37613355414
```

Supplementary source, original inputs, numerical observations and complete cold outputs (`R82_FINITE_PHYSICAL_MASS_GATES.zip`):3102191 bytes, SHA-256 `65261d594323b5cd92d544e4fea7ecae3da3f61a279e8576eafcf4e21984c508`. The following inline capsule, not that ZIP, is the durable recovery source.

### 6.3 Complete decoder

```python
from pathlib import Path
import base64,hashlib,json,lzma,sys
assert __debug__ and len(sys.argv)==3,'Give CAPSULE.b64 NEW_DIRECTORY'
H=lambda b:hashlib.sha256(b).hexdigest()
s=''.join(Path(sys.argv[1]).read_text(encoding='utf-8').split())
assert len(s)==72364 and H(s.encode())=='1a443c8775608800a4ab12a288f8c88ae6888f0291611126c503eab9d39dff74'
z=base64.b64decode(s,validate=True)
assert len(z)==54272 and H(z)=='39b6e511f77109f860dc79f5c7cea95c712f63b8004884dd4f65c5f5280a7888'
b=lzma.decompress(z)
assert len(b)==206113 and H(b)=='1b19dac3308a9bdb41921797bbfe8cfbce67a377525e8efdc82dc37613355414'
d=json.loads(b);assert len(d)==44
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 q=Path(name);assert not q.is_absolute() and '..' not in q.parts
 p=out/q;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
for name,v in json.loads((out/'SOURCE_MANIFEST.json').read_text()).items():
 bb=(out/name).read_bytes();assert len(bb)==v['bytes'] and H(bb)==v['sha256']
print('R82_FINITE_PHYSICAL_SOURCE_CAPSULE_RECOVERED44')
```

### 6.4 Complete source/input capsule

```base64
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
WVo=
```
