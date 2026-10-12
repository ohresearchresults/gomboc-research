# figure-0440

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Sharp Lynx 47 — whole-polar-basin deformation with exact nonwinners

Branch: `[internal-source-reference]`.

## Result and acceptance boundary

**No own110 endpoint was obtained.** I constructed and cold-replayed four distinct rational descendants of the physical 21-point architecture. The principal small-arithmetic descendant, **SL47_WHOLE_Q19_G4**, has **V21/E57/F38, C114, strict own312, additional weak000, primitive-zero000, and a 58-bit common centered denominator**. Its physical landscape has one unstable vertex and no positive physical elder bar. Its same-physical-center polar has two positive bars, not zero.

This is actual whole-basin progress with a cost: relative to CANCEL21_G4, the sum of **all** positive polar elder depths, normalized as `TQ = Vol(P)^(2/3) * sum(delta_Q)`, falls by more than **9.4284%**. The dominant relative polar bar decreases from approximately .927755770277 to .870110388233, but an additional small S/H pair is present. Physical escape reserve decreases. This is neither a cancellation certificate nor an improvement of the accepted own110 incumbent C622.

The geometry genuinely changes its maximal complex: six input-labelled edges disappear and six different ones appear. Its degree histogram changes. Therefore this endpoint is not merely a translation, affine image, or positive-denominator projective image of the parent.

## Reading, source authority, and inherited comparisons

I read the complete supplied 1,133-line journal, including its branch memory and literal selected parent, and all 21 decoded source units. The selected parent is `figure-0438`, supplied payload SHA-256 `16684588638a09e8929f3ce23437b244db8ef4f46a3cfe29b4deea8a906b0547`. Its extracted 26,407-byte recovery program matched SHA-256 `1e8f5a53e3ec40bb620d02fb4dbbf740cd721a71ed539a834db079830520f24b`; its decoded source dictionary matched the supplied 61,794-byte identity. No necessary source dependency is missing. No research connector or external archive was used.

The two comparison bodies are the parent's **physical point hulls**, not the old CONTACT2 halfspace body: CANCEL21_G4 is own211 and FREE21_G4 is own312. Their tradeoff, physical centroid requirement, and distinct definitions are source-authoritative. :contentReference[oaicite:0]{index=0}

I freshly reconstructed both G4 parents during the present exact comparison and again in the source-only cold replay. Their FULL and BASIN output hashes matched the parent's four published identities. This is an executed comparison, not a fresh claim to have rerun all nine historical parent bodies. The inherited verifier remains one complete mechanical implementation with separate mass evidence, not two independent whole-mechanics auditors. :contentReference[oaicite:1]{index=1}

## Complete principal exact input

Interpret this entire JSON as `conv(points / grid)` with uniform positive volume density:

```json
{"grid":10000,"points":[[-13508,10052,-8978],[7531,917,-5390],[9257,2551,-2775],[9893,3119,-235],[10437,1509,1565],[10552,-521,2680],[10271,-2759,3297],[9501,-4873,3885],[8295,-6606,4631],[6779,-7624,5885],[4983,-8211,7197],[2843,-8737,8080],[555,-8888,8727],[-1864,-8749,9028],[-4317,-8320,8951],[-6800,-7570,8466],[-9197,-6488,7533],[-11439,-5033,6085],[-13381,-3009,4166],[-14824,-268,1625],[-15526,3469,-2132]]}
```

Defining input: **415 bytes**, SHA-256 `49fac345eda50215e805c7a9a3033a96eb152f1bb3437566ff131a4421625f2c`.

Its exact volume is `211260115097/240000000000`. Its actual filled centroid is

```text
(-24709550052279/42252023019400000,
 1669965686738819/211260115097000000,
 18470066435097/42252023019400000).
```

Numerically, volume is .8802504795708334 and centroid is approximately `(-.0005848134192517508, .007904784516339277, .000437140404534393)`. All mechanical calculations use these exact fractions. The volume is between 1.031296274262 and 1.031296274263 times the parent's volume; this is not a uniform-shrinking objective artifact.

All 21 points are exposed. All 38 maximal facets are genuine triangles, and all 57 counted edges are true edges. In the exact reconstructed ordering, stable faces are `[1,6,10]`, the unique unstable vertex is `[2]`, and saddles are `[[2,13],[2,15]]`. The degree histogram is `{3:3,4:5,5:7,6:2,7:2,11:1,13:1}`. The three stable cycles in original input labels are `[20,19,4]`, `[2,1,0]`, and `[18,1,17]`.

The exact input-labelled edge changes relative to CANCEL are:

```text
removed = [[1,14],[4,17],[11,13],[11,14],[14,16],[14,17]]
added   = [[1,12],[1,16],[12,14],[12,15],[12,16],[16,18]]
```

The full eight removed/eight added triangular-face lists are regenerated in `SL47_COMPARISON.json`; the complete underlying maximal complexes are regenerated in the FULL reports.

## Complete physical and polar basin evidence

Here `X=v-c`, and `Q_f=n_f/(h_f-n_f.c)`. The polar is **not** filled and recentered independently.

The complete positive physical true-edge forest is the following 20-arrow tree, terminating at exact vertex2, which is original input0:

```text
[[0,2],[1,0],[3,1],[4,3],[5,4],[6,5],[7,6],[8,7],[9,8],[10,9],
 [11,10],[12,11],[13,15],[14,12],[15,17],[16,14],[17,19],[18,16],
 [19,20],[20,18]]
```

Every arrow has strictly positive `X_i.(X_j-X_i)`. The selected minimum cosine lies in `[453977934,453977935)/10^12`. Every outgoing primitive at root2 is strictly negative. The physical positive elder list is exactly empty; the full feature enumeration within the same audit implementation also gives U1.

The polar has roots `[1,6,10]`, global root1. Its complete positive forest is:

```text
[[0,4],[2,0],[3,1],[4,10],[5,1],[7,8],[8,3],[9,11],[11,5],
 [12,10],[13,15],[14,11],[15,12],[16,13],[17,14],[18,16],[19,17],
 [20,21],[21,19],[22,15],[23,20],[24,26],[25,23],[26,22],[27,28],
 [28,29],[29,25],[30,26],[31,27],[32,30],[33,34],[34,32],[35,37],
 [36,33],[37,36]]
```

The selected minimum positive polar-forest cosine lies in `[186630418010,186630418011)/10^12`. This large forest margin does **not** remove the three roots.

**Dominant polar bar:** peak10 merges with older peak1 on true dual edge `[2,6]`; its relative depth lies in `[870110388233,870110388234)/10^12`. An attaining path is `[10,4,0,2,6,7,8,3,1]`. The complete strict-upper component is

```text
[0,2,4,10,12,13,15,16,18,22,24,26,30,32]
```

and its entire outward boundary is

```text
[[0,1],[2,3],[2,6],[4,5],[10,9],[12,9],[13,14],[16,17],
 [18,19],[18,20],[22,23],[24,25],[24,27],[30,31],[32,31],[32,34]]
```

Thus the current dominant component has 14 vertices and 16 boundary edges, not the parent's 13 and15. Old facet indices must not be reused as immutable physical owners.

**Additional polar bar:** peak6 merges with older peak1 on `[6,7]`; its relative depth lies in `[18242135,18242136)/10^12`. The attaining path is `[6,7,8,3,1]`; the entire strict-upper component is `[6]`, with boundary `[[6,2],[6,7],[6,33]]`.

For both bars, the exact certificate checks that every cut-edge minimum squared radius is at most the merge level, that the stated path attains that level, and that the older peak lies outside the strict-upper component. Complete rational births, merge heights, differences, normalized depths, and both layer circumradii are regenerated in `SL47_WHOLE_Q19_G4_BASIN.json`. No positive bar is omitted by a floating threshold in these certificates.

## Quantitative comparison and arithmetic companions

For the principal G4 body, exact cube comparisons give

```text
TQ(parent CANCEL) in [33906510555318,33906510555319)/10^12
TQ(new G4)       in [30709639238853,30709639238854)/10^12
TQ(new)/TQ(old)  in [905715118892,905715118893)/10^12.
```

These bounds use `TQ^3=(sum(delta_Q))^3*Vol(P)^2`, with rational arithmetic and integer cube isolation. Both bodies have exactly TP=0. The sum improves despite the additional positive polar bar; the equilibrium count nevertheless worsens from211 to312.

All four new rounded bodies have V21/E57/F38, weak000 and primitive-zero000. Each grid is frozen independently from the **same complete binary64 terminal checkpoint** using `round(Fraction(x)*10**k)`, ties to even. No grid inherits another grid's class.

| New exact body | Own S/U/H | Common centered denominator bits | Positive P-bar count | Positive Q relative bars, lower endpoints with width10^-12 |
|---|---|---:|---:|---|
| SL47_WHOLE_Q19_G6 | 3/1/2 | 85 | 0 | .870073426891; .000018092324 |
| SL47_WHOLE_Q19_G5 | 3/1/2 | 71 | 0 | .870071247198; .000018106132 |
| SL47_WHOLE_Q19_G4 | 3/1/2 | 58 | 0 | .870110388233; .000018242135 |
| SL47_WHOLE_Q19_G3 | 3/4/5 | 45 | 3 | .870636930552; .000015728817 |

G3's three physical relative bars lie respectively in `[1221220,1221221)`, `[278719,278720)`, and `[119883,119884)`, divided by10^12. They are real positive bars with complete paths/cuts, not numerical zeros. G3 is a preserved rounding countercontrol, not an own312 companion.

Principal G4 conditioning is certified by

```text
min_true_edge/RP in [116355709980,116355709981)/10^12
r^2/RP^2        in [7180099086,7180099087)/10^12
Vol(P)^2/RP^6   in [16272904678,16272904679)/10^12.
```

The body has not achieved its smaller objective by collapsing a true edge. However, its selected physical cosine reserve is less than half CANCEL's reserve and much smaller than FREE's. **The exact G4 margin is below the numerical run's .0005 floor.** G5 and G6 are also slightly below that floor after independent rounding: their minima lie respectively in `[484084109,484084110)` and `[499785056,499785057)`, divided by10^12. Exact U1 survives, but exact preservation of the original numerical floor is not claimed.

## What was executed, including the failed continuation

### Whole-Q descent with finite physical validation

`WHOLE_Q.py` varies all 63 physical coordinates. It rebuilds the convex hull and actual filled centroid for finite trials, forms the same-physical-center polar, and minimizes the sum of **all** positive polar elder depths times `Vol(P)^(2/3)`. It does not exempt the largest bar. Its loss includes every merger's positive part; the separate floating event display has a10^-12 threshold and is not used as exact acceptance evidence.

The local quadratic subproblem uses the current physical true-edge escape choices, live centroid derivatives, coordinate trust .04, and a fixed cosine floor .0005. Finite acceptance rebuilds geometry and requires numerical U1, true-edge escape floor .0005, minimum true-edge length/R at least .04, r/R at least .04, and Armijo decrease of the full polar objective. There is no post-acceptance volume normalization. Hull triangulation and signs remain floating during scouting; final maximal-complex claims come only from rational reconstruction.

Executed command:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python WHOLE_Q.py --input CANCEL.json --out CANCEL_WHOLE40 --steps 40
```

Actual boundary: **20 attempted outer iterations, 19 accepted finite steps, 265 finite backtracking trials, 40 total inner QP iterations**, with every QP reporting success. Outer iteration19 found no accepted trial among exponents0 through21. The requested40 steps were not completed. The fixed floor was never adaptively reduced.

The first accepted step already had floating S3/U1. The final accepted checkpoint had TQ approximately30.709537571733915, physical margin .0005000003243349815, and minimum edge/R .11638191789688809. The complete 21-point binary64 checkpoint and the entire accepted-run history are embedded. No continuous no-birth path is asserted, and the exact frozen endpoint has the additional pair described above.

### Direct nonlinear constrained whole-Q continuation

I then ran `NONLINEAR_Q.py` from that exact binary64 checkpoint, with actual hull and mass recomputation inside objective and constraints, all-point physical escape maxima, fixed root input0, margin .0005, coordinate bounds ±.5 about the start, minimum all-pair distance/R .04, r/R .04, and volume/R^3 .06. SLSQP used maximum100 iterations and ftol10^-10.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python NONLINEAR_Q.py --input CANCEL_WHOLE40.json --out CANCEL_NL100 --steps 100
```

Observed termination: **84 reported optimizer iterations, 290 function/model evaluations, 80 Jacobian evaluations, 80 callback records, status8**, message `Positive directional derivative for linesearch`. **No callback produced a lower-objective accepted feasible replacement of the starting checkpoint.** The stored best point array equals the starting point array exactly.

The terminal trial has floating V13/E33/F22, S8/U7, TQ approximately4.682713128655403 and minimum constraint approximately−.2859878711347833. It is infeasible. Its smaller objective is not accepted basin progress. Its complete 21-input terminal float array, starting array, terminal diagnostics, settings and complete producing source are embedded as a nonaccepted numerical checkpoint. It has no exact H/weak audit and is not promoted to an exact descendant. The redundant full callback trace is supplementary, not a dependency of any exact result here.

Environment for both executed scouts: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, one BLAS/OMP/Torch thread, no RNG. These finite stops establish neither stationarity of the geometry problem nor exclusion of a nonlinear family.

## Verification, receipts, and continuation

Exact reconstruction exhausts all supporting triples, merges exact coplanar supports, constructs maximal polygon cycles, and checks all-point supporting inequalities, orientation, opposite edge incidences, connectedness, vertex links, Euler, filled mass and every strict/weak S/U/mixed-edge H predicate. The unstable census is also compared with the all-point characterization. All six replayed point hulls have38 positive interior-anchor tetrahedra; their volumes and first moments agree exactly with separately coded projected-polygon divergence integration.

Fresh controls passed tetrahedron446/weak000, prism446/weak123, and reversed-orientation rejection. This is still **one complete mechanics implementation**, not the two-full-auditor winner-level gate. No winner claim is made.

Principal observed output receipts:

| File | Bytes | SHA-256 |
|---|---:|---|
| SL47_WHOLE_Q19_G4.json | 415 | 49fac345eda50215e805c7a9a3033a96eb152f1bb3437566ff131a4421625f2c |
| SL47_WHOLE_Q19_G4_FULL.json | 8749 | bc9394377994c95a1b11ffe4fd6be132c0626002ad80037bf5bf0ea75d3817a6 |
| SL47_WHOLE_Q19_G4_BASIN.json | 2924 | 1f7f005c414ed7124c024cce6906022ce55c6cad4113d9e1253ae4585fe5d3b2 |

All four new inputs, six FULL reports, six SUMMARY reports, six complete BASIN reports, and the exact comparison report are covered by the embedded23-output expected manifest. A freshly decoded directory actually produced:

```text
SL47_INLINE_SOURCE_RECOVERY_PASS 16
SL47_SOURCE_HASHES_PASS
SL47_TETRA446_PRISM446_WEAK123_REVERSED_PASS
SL47_EXACT_SIX_BODIES_FULL_BASINS_AND_OUTPUT_HASH_PASS 23
SL47_OWN110_FOUND False
```

The useful continuation is a **feasibility-preserving finite whole-interface step**, not another objective evaluation at an infeasible endpoint and not removal of the minor polar pair alone. The changed G4/G6 geometries supply a smaller dominant basin and an explicitly changed true complex; FREE supplies substantially more physical reserve. A second-order restoration or an added/replaced physical vertex should be evaluated against the entire current14-vertex polar component and16-edge boundary, with both nonglobal polar roots tracked and actual mass recomputed. This is a proposed next mechanism, not an executed success. There is no evidence here that dropping the physical guard, freezing the current root, or retaining21 vertices is necessary. The sufficient105-input-vertex budget still leaves84 additions.

## Self-contained recovery capsule

The complete executable below contains16 source/input/manifest units, including all four exact helper modules used, both new numerical producers, both literal G4 parents, the full accepted-run checkpoint/history, the failed nonlinear terminal checkpoint, independent-grid freezing, exact comparison and full-basin verification. It requires no old journal, parent sandbox, external file, or optimizer execution for exact reconstruction.

Save it as `RECOVER_SL47.py` and run:

```bash
python -B -S RECOVER_SL47.py SL47_COLD
```

Exact replay uses only the CPython3.13.5 standard library. To repeat either numerical experiment, use the commands above in a disposable copy of the decoded directory; do not overwrite the pinned defining checkpoint. The original numerical experiments were executed as reported; the source-only cold replay reruns exact mathematics, not those optimizers.

Capsule identities: decoded JSON74,135bytes/SHA256 `4141a611e546b7e1b87c5206b595332536616a4ee2ba957afe2a930e828056f2`; XZ19,596bytes/SHA256 `5083409283d1b2ec29ae40999887a8706286802574b780e90b96f2e07238c61e`; normalized base6426,128characters/SHA256 `b742e67d0eeba808aaf57a85762916a163ab07c1962b97f8dfbbc1ecfad313ce`. Recovery program27,162bytes/SHA256 `b62e6524a588a565a487148ca7338d21f4c043eeb3b55bb093be1d922c9146f0`.

Supplementary conveniences: [recovery program](sandbox:/mnt/data/RECOVER_SL47.py), [complete source/output archive](sandbox:/mnt/data/SL47_RESEARCH_HANDOFF.zip), and [observed cold-replay log](sandbox:/mnt/data/SL47_COLD_REPLAY.log). None is required instead of the inline capsule.

```python
"""SL47 exact source-only recovery, CPython 3.13.5 standard library."""
import base64,hashlib,json,lzma,pathlib,subprocess,sys
DATA="""
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4SGWTEpdAD2IhCUiPHTGSFNl0NIOpxVu8CUXDVWPLRzezD3291LvP9Oil7avkTjOp+mz
SK+kzwdWZoXzwVAiL9IbmdM7jsOPsdK0p/NNmmRvuluQ/MI79YzC5P28V3NzESaNtA/aS9V8qnMLghAO7ktvDzybEHttcQ5G1Y0+
KYvEby9PAK/szQkdHBKrWGPHoXsAXeDcRKuOzSkc09w008SapOa03c4OjvHOR3Zd/1QsQbBX1dz/moKps+uNNsYACbPEfPPHiIb4
ne//0B13dvPy8jOT2exBQLlUeJws/SUP6CdSfay0Fn9KqrzDyG+JnvMEchpXKWYLTLSpIhBgY9z88UuUafXfWN9kofV8Aj7OzqcD
8qzomnxthU9SWTsUaX4d+YtM5kupvboBVuNAl8K+qV7+3e2gA/UdO8lMpWjKWRdXr19F6L4Ar6Wis6faNpfkOIgwpNBj3V/LaIM1
VPU2OX80FotvUyh+DVH4XXZvRN102AneT2NlOcT4F+tuRYKQbQJbE5jCAf/wqHYn3cBBV3fPjqDlwGS4pw7KaFEDnlO2zJKRwDfH
RtoNqSvP90Q4T7SNo+496jR0YiFu+eWKojh5btWmI818e6yzw1IEJ6ZesIZKE4ArAVuqlPHwKRgl3qmI8c9bMum9XqaoarMEq8ib
Vy9m2gHGhuKF5mxfN1PEwcYe0IUDgvyW7quLq6gs5fmuHVdl2iZrVrOybOpL5KHtsO+nhGSWD8Nxa6UE17x2aRxJbdXpGY94MtMg
1Zja00ucsc4rnj9A3vCvA0ZDNWuLG8AMimAJruiO9RyYJeroQg2A79HqtC7rJ/wV1oRrQgt1ZjZX5xe0Ffdq12sUj7PJHupvHdZi
N6BaAEgNnM46y2qQ+keHMvmy8eKzBLh9Bfes6+RAmve1gXh7nIOYff+j4vuhKjI87t6HCT1WvCSHpl60Fv2kqkCKuiGDM7cvGIpx
2Zfysu10KuA22ZlCfXjAwboE89VEnZS7mqoiEyV7MMl0JkYs+kT/ojE1iM6DUSjOxMw1/b+CJPhqrDY+Hsb/en3z374z09UKqg5u
BwPWOUKG7YFfpoVnrJyYzK1AnMlvbcP/2P6D3U44F8O4n1DKmNVBvvU1Xb2MuDfOcudHLNZfyZz1itKqs0VUvveOfX1dhT49T+RP
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
mAGXwwQXyWRFscRn+wIAAAAABFla
"""
raw=lzma.decompress(base64.b64decode("".join(DATA.split()),validate=True))
assert len(raw)==74135 and hashlib.sha256(raw).hexdigest()=='4141a611e546b7e1b87c5206b595332536616a4ee2ba957afe2a930e828056f2'
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'SL47_COLD').resolve()
out.mkdir(parents=True,exist_ok=True)
sources=json.loads(raw)
for name,text in sources.items():
 assert pathlib.Path(name).name==name and name not in ('.','..')
 (out/name).write_bytes(text.encode())
print('SL47_INLINE_SOURCE_RECOVERY_PASS',len(sources),flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY_SL47.py')],cwd=out,check=True)
```
