# figure-0438

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vivid Lynx 12 — C114 architecture replacement with exact own211; no own110

Branch: `[internal-source-reference]`.

## Result

**A new source-complete replacement body has V21/E57/F38, C114, strict own(S,U,H)=(2,1,1), weak000, and a 58-bit common centered denominator.** Its identifier is **VL12_DUAL_CANCEL21_G4**. All physical extra-maximum basins are absent at its actual uniform-volume centroid. One substantial same-physical-center polar basin remains, corresponding to its second stable equilibrium. This is a useful exact NONWINNER, not an own110 construction or an improvement of the accepted C622 own110 incumbent.

The construction replaces the original 38-vertex/21-facet architecture by a freely deformed 21-vertex/38-facet architecture. It does not clip a fixed waist or merely rename the old roots. It also does **not** supply a certified continuous path from the original C114 to the replacement.

A companion, **VL12_DUAL_FREE21_G4**, is exact own312/weak000 at the same C114 and 58-bit denominator. Passing from that frozen companion to CANCEL21_G4 decreases the exact endpoint census S3→S2 and H2→H1 while retaining U1. The maximal face cycles agree at these endpoints. The smaller polar bar disappears, but the larger polar bar grows; retain both bodies as different tradeoffs.

## Source authority and reading

I read the entire supplied 1,198-line journal, including branch memory and the literal parent `figure-0432`, SHA-256 `a00849da3b96c21a3afce30d32ab973073fe1ec393b2909e93120ec9b33a6b0b`. I decoded and read all nine supplied parent source units. No necessary exact dependency is missing, and no research connector or external archive was used.

The parent is correctly own121/weak000 with V38/E57/F21, not own110; its centroid is not zero. Its complete physical bar is large, while its same-center polar has no positive bar. These are the literal-parent facts, not an alias inferred from older branch prose. :contentReference[oaicite:0]{index=0}

The supplied nine-source parent recovery was actually run through `BH81_CONTACT2_FOUR_RATIONAL_NONWINNERS_COLD_PASS 4`. All four inherited output hashes matched. The new capsule independently reconstructs the G6 parent again and checks its 690,015-byte full output against SHA-256 `0e857472cf4a8c50326f38eec6d18463b6256693e49f3e508266cac867938e32`.

## What changed, and what was actually executed

Two initial free-21-normal probes varied the entire H-description and recomputed actual filled mass. They did not freeze the central section. The guarded probe made 11 accepted steps before stopping; a physical-only variant made 33. Their final floating re-evaluations were S2U2 and S14U3, respectively, despite stricter intended acceptance. Unit-volume renormalization occurs after the trial acceptance test, and nearly zero floating predicates can change on re-evaluation; witness floors can also shrink. These runs are preserved as numerical validator failures, **not** class-preserving paths, exact endpoints, or exclusions of the free-normal family.

I then changed architecture. For the exact G6 parent `P={x:n_i·x≤1}`, form the new physical point hull `conv{n_i}`. This is its raw-origin polar, but it is now filled uniformly and evaluated at **its own** centroid. Merely doing that gives exact own(4,9,11), not211 or110. Thus none of the successful classification is obtained by incorrectly treating the parent's physical centroid as the new polar's centroid.

`DUAL_SEARCH.py` freely varies all 63 coordinates of these 21 physical vertices, rebuilds the actual convex hull, integrates volume and first moment, and evaluates own-centered escape predicates. L-BFGS-B terminated after **38 iterations/43 evaluations**, not the requested maximum500 iterations. Its discovery objective uses a positive all-point physical escape margin of0.003 and an explicit short-edge penalty. The frozen rational outputs are accepted only by the subsequent complete exact hull, mechanics and persistence calculations.

Starting from the exact FREE21_G4 point table, `DUAL_SMALL.py` minimizes all positive polar bars except the largest, with a physical escape penalty of weight1000 and target margin0.001. It terminated after **8 iterations/34 evaluations**. Exact freezing gives the CANCEL family. This is an actual endpoint pair-count reduction, not a claim that the entire intervening optimizer trajectory was no-birth or mechanically certified.

Numerical environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, one BLAS/OMP/Torch thread, no RNG. All source, inputs, defaults, nondefaults, frozen round-trip checkpoints and execution logs are inside the recovery capsule. The exact replay uses only the Python standard library.

## Exact endpoint inventory

Every row below has **V21/E57/F38, C114, weak000 and primitive-zero000**, with all21 supplied physical points exposed and all38 maximal facets triangular. Denominator bits refer to the common denominator of the actual centered physical vertices, not raw-grid decimal places. A displayed bar value is the lower endpoint of an exact interval of width10^-12, normalized by that layer's global squared circumradius.

| Exact identifier | Own strict S/U/H | Centered denominator bits | Positive physical bars | Positive same-center polar bars |
|---|---|---:|---|---|
| VL12_DUAL_FREE21_G6 | 3/1/2 | 84 | none | .901583917945; .000268154087 |
| VL12_DUAL_FREE21_G5 | 3/1/2 | 71 | none | .901571760930; .000268396276 |
| VL12_DUAL_FREE21_G4 | 3/1/2 | 58 | none | .901600992733; .000267612147 |
| VL12_DUAL_FREE21_G3 | 3/2/3 | 45 | .000001070929 | .901485487546; .000254302506 |
| VL12_DUAL_CANCEL21_G6 | 2/1/1 | 85 | none | .927862364226 |
| VL12_DUAL_CANCEL21_G5 | 2/1/1 | 71 | none | .927858187922 |
| VL12_DUAL_CANCEL21_G4 | 2/1/1 | 58 | none | .927755770277 |
| VL12_DUAL_CANCEL21_G3 | 3/1/2 | 43 | none | .928543173445; .000000322019 |

The ninth retained exact control, **VL12_RAW_POLAR_G6**, has own4/9/11, centered denominator98bits, eight positive physical bars and three positive polar bars. Its complete lists and geometry are regenerated. The G3 rows demonstrate why a tiny positive bar must not be discarded or why coarser rounding must not inherit a finer body's class.

Every grid is frozen independently as `round(Fraction(binary64_coordinate)*10**k)`, ties to even, from its complete pinned checkpoint. G4 is not obtained by re-rounding the G6 integer table.

## Primary literal physical body

The following is the complete 415-byte defining JSON for **VL12_DUAL_CANCEL21_G4**. Interpret it as a **convex hull of physical points divided by10000**, never as halfspaces.

```json
{"grid":10000,"points":[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]]}
```

Input SHA-256: `df0a606ee746a5546f046a4800f1eed5c833bf27e0fbe31d28da4984a482a6f2`.

Its exact uniform volume is `5121227535899/6000000000000`. Its actual centroid is

```
(242198547478883/204849101435960000,
 231436767908883/51212275358990000,
 386646611479453/204849101435960000).
```

Numerically these are volume .8535379226498333 and centroid (.0011823266286310717,.0045191658891651975,.001887470380729625). The nonzero centroid is used exactly in every mechanical test; translating it away is bookkeeping, not physical mass closure.

In the exact generator's lexicographic vertex/facet ordering, S=[1,9], U=[2], H=[2–13]. Physical root2 is original input0. Stable face1 has cycle[1,19,0]; stable face9 has cycle[3,13,4]. The sole saddle's adjacent facets are2 and6. The degree histogram is {3:4,4:4,5:7,6:1,7:3,12:2}. All57 edges are true edges. The minimum edge length divided by the physical circumradius is in[116216295554,116216295555)/10^12, so this endpoint does not obtain a small deficit by collapsing an edge.

The complete companion G4 literal is also compact:

```json
{"grid":10000,"points":[[-13506,10017,-9025],[7576,847,-5312],[9203,2681,-2774],[9859,3063,-262],[10415,1444,1501],[10534,-560,2630],[10247,-2748,3309],[9491,-4871,3884],[8293,-6614,4621],[6777,-7647,5867],[4985,-8225,7189],[2841,-8793,8031],[556,-8902,8727],[-1869,-8793,9001],[-4342,-8345,8935],[-6808,-7570,8473],[-9197,-6461,7561],[-11427,-4980,6137],[-13361,-2965,4208],[-14796,-283,1611],[-15511,3410,-2190]]}
```

Its SHA-256 is `2f6fb60bd61ff3b7e45aab24ad16ba7826137c3faa5b8ab0c9e94b93d67d873d`; volume is `1037440120339/1200000000000`, and its centroid is `(99980571051103/103744012033900000,125200901724987/29641146295400000,-130692377637581/207488024067800000)`. Thus the continuation changes actual volume and first moment; it is not a free reference-center move.

## Complete physical and same-center polar basin evidence

All labels in this section are the exact generated labels, not numerical Qhull labels. Write `X_i=v_i-c` and form polar vertices `Q_f=n_f/(h_f-n_f·c)`. **Do not integrate and recenter this polar** when reproducing these diagnostics.

For CANCEL21_G4 the following complete20-arrow true-edge physical tree terminates at root2:

```
[[0,2],[1,0],[3,1],[4,3],[5,4],[6,5],[7,6],[8,7],[9,8],[10,9],
 [11,10],[12,11],[13,15],[14,12],[15,17],[16,14],[17,19],[18,16],
 [19,20],[20,18]]
```

Every arrow has `X_i·(X_j-X_i)>0`; the exact minimum cosine lies in[947330784,947330785)/10^12. Root2 has every outgoing primitive strictly negative. The complete physical elder list is empty, and the full feature census independently checks U1. FREE21_G4 has the same tree with a larger minimum cosine in[2838422510,2838422511)/10^12.

For CANCEL21_G4, polar roots are[1,9]; the global polar root is1. The sole positive bar is9→1, merging on dual edge2–6. An exact attaining path is

`[9,4,0,2,6,7,8,3,1]`.

The complete strict-upper component at its merger level is

`[0,2,4,9,11,13,14,17,19,20,26,30,32]`.

Its complete15-edge boundary, oriented outward, is

```
[[0,1],[2,3],[2,6],[4,5],[9,10],[11,12],[14,15],[14,16],
 [17,18],[20,21],[20,23],[26,24],[30,31],[32,31],[32,34]]
```

Every boundary edge has its exact minimum squared radius at or below the merger level. The path attains that level and the strict-upper component excludes the older root. The capsule regenerates the exact rational birth, merger, difference and normalized bar, along with the entire positive polar forest. Its sole bar/R_Q² lies in[927755770277,927755770278)/10^12. The minimum positive selected polar-forest cosine lies in[132591461,132591462)/10^12.

FREE21_G4 has that dominant basin plus a second positive bar at polar peak6. The latter merges on6–7, has strict-upper component[6], boundary[[6,2],[6,7],[6,33]], and attaining path[6,7,8,3,1]. Its relative bar lies in[267612147,267612148)/10^12. In CANCEL21_G4 that extra bar is absent and the exact counts decrease. However, the dominant relative bar grows from .901600992733 to .927755770277. This is a count-versus-barrier tradeoff, not unqualified progress on both landscapes.

At the replacement's actual farthest-axis central section, CANCEL21_G4 has rho²/R_P² in[506280643733,506280643734)/10^12. The direct opposite-cap gap divided by R_P² is in[-681191970,-681191969)/10^12. Hence the old positive two-cap separation certificate does not apply to this replacement. The sufficient rational area-obstruction calculation is also nonpositive; its code clamps the displayed positive lower bound to zero, so **zero is not claimed to be the exact transcendental area residual**. The independent full exact U census, rather than merely passing these necessary gates, establishes physical U1.

Conditioning quantities are r²/R_P² in[6764702216,6764702217)/10^12 and V²/R_P^6 in[15111039822,15111039823)/10^12. These are not improvements asserted over every parent conditioning statistic.

## Verification level and recovery receipts

`EXACT_DUAL.py` enumerates every supporting triple of the rational physical points, merges exact coplanar supports and rebuilds maximal polygon cycles. The inherited exact auditor checks global support containment, orientation, opposite two-face edge pairing, boundary connectivity, vertex links, Euler, actual mass, every maximal-face foot, every unstable-vertex primitive and all four mixed-edge saddle primitives. Vertex results also agree with the all-point characterization. Additional weak cases and primitive zeros are tested explicitly, not inferred from Euler.

Actual volume and first moments agree between positive interior-anchor tetrahedra and separately coded projected-polygon divergence integration. Tetrahedron strict446/weak000, prism strict446/weak123 and reversed-orientation rejection pass. This is **one complete mechanical implementation with separate mass evidence**, not two independent whole-mechanics auditors and not proof-assistant formalization. No winner is promoted from this evidence level.

A fresh directory containing only the inline recovered sources successfully produced these observed terminal markers:

```
VL12_COMPLETE_INLINE_SOURCE_RECOVERY_PASS 21
VL12_CONTROLS_TETRA446_PRISM446_WEAK123_REVERSED_PASS
VL12_EXACT_PARENT_G6_MATCH_PASS
VL12_C114_REPLACEMENT_EXACT_NINE_NONWINNERS_PASS 9
VL12_SOURCE_ONLY_EXACT_REPLAY_AND_OUTPUT_HASH_PASS 20
```

The two G4 basin runs additionally printed `VL12_EXACT_FOREST_AND_FULL_ELDER_PATH_CUT_PASS` with their exact byte/hash receipts.

| Output | Bytes | SHA-256 |
|---|---:|---|
| VL12_DUAL_CANCEL21_G4_FULL.json | 8809 | 52f189cbb6988b44b5b8a8f5c53ce3c2a11268580e3affcbcf2514169f513ff4 |
| VL12_DUAL_CANCEL21_G4_BASIN.json | 2103 | 065763598eeb7809f1cd43ae2fb115b338db1a8bba9f1670c7eb6c9998bb2e8b |
| VL12_DUAL_FREE21_G4_FULL.json | 9172 | f8199eaa5680cf78d9822f13efa90e5ea7d70994ef13d6c627adee777c722d49 |
| VL12_DUAL_FREE21_G4_BASIN.json | 2954 | 09a5bbf30aa565724a349c8351611553cf4015d5389558d315f8c64dede19a50 |

All nine input/full-output identities and both G4 basin identities are checked by the supplied expected-output manifest.

## Most useful continuation

Continue from both literal G4 bodies. CANCEL21_G4 solves the physical multiplicity problem but leaves one deep polar basin; FREE21_G4 has more physical escape reserve and a smaller dominant polar bar, at the cost of an additional small S/H pair. Neither dominates the other.

The substantial remaining task is to redesign the entire13-vertex polar upper component and its15 boundary edges while retaining or rebuilding the physical root2 escape system at the changing actual centroid. This includes the stable face9 region and its connection to the physical root star. Moving just polar peak9 or opening only dual edge2–6 is not a certificate of cancellation.

The replacement has21 physical points, leaving84 possible additional inputs before the sufficient bound V≤105 implies E≤309. Alternatively its38 maximal supports leave67 additional support slots under F≤105. These are available complexity budgets, not a prescribed fixed-incidence restriction or a feasibility theorem. The original fixed-waist obstruction is not being extended to this variable geometry. No global family exclusion follows from either initial failed probe.

## Self-contained runnable capsule

Save the complete program below as `RECOVER_VL12_C114_REPLACEMENT.py` and run:

`python -B -S RECOVER_VL12_C114_REPLACEMENT.py VL12_REPLAY`

No external parent, optimizer execution, NumPy, SciPy or Torch is needed for exact reconstruction. The numerical producers are included for continuation; execute them in a disposable copy so they do not overwrite the frozen defining checkpoints.

The capsule contains21 units. Expanded JSON:61,794bytes, SHA-256 `f529bf432bfb07042cf6ab5e3663957cef664386bc140af84f705b94d55fe937`. XZ:18,816bytes, SHA-256 `288863166e1583fde4f058e57e3668e72666c6e5c1b96bc410c03b432a878fd5`. Normalized base64:25,088characters, SHA-256 `a25691529131966c39c7cad38bb85fdebb3c5ae8a4b1a56c4590a70ee3a952e2`. Recovery program:26,407bytes, SHA-256 `1e8f5a53e3ec40bb620d02fb4dbbf740cd721a71ed539a834db079830520f24b`.

[Recovery program](sandbox:/mnt/data/RECOVER_VL12_C114_REPLACEMENT.py) and [verified source/output archive](sandbox:/mnt/data/VL12_C114_REPLACEMENT_VERIFIED.zip) are conveniences only; all continuation-critical sources and checkpoints follow inline.

```python
"""VL12 exact C114 replacement recovery. CPython 3.13.5 standard library.
All sources, exact inputs, frozen numerical checkpoints and producers are inline.
"""
import base64,hashlib,json,lzma,pathlib,subprocess,sys
DATA="""
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4PFhSUBdAD2IhCUiPHTGSFNl0NIOpxVu8CUXDVWPLRzezD3291LvP9Oil7avkTjOp+mz
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
"""
raw=lzma.decompress(base64.b64decode(''.join(DATA.split()),validate=True))
assert len(raw)==61794 and hashlib.sha256(raw).hexdigest()=="f529bf432bfb07042cf6ab5e3663957cef664386bc140af84f705b94d55fe937"
out=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'VL12_REPLAY').resolve()
out.mkdir(parents=True,exist_ok=True)
sources=json.loads(raw)
for name,text in sources.items():
 assert pathlib.Path(name).name==name and name not in ('.','..')
 (out/name).write_bytes(text.encode('utf-8'))
for name,receipt in json.loads(sources['SOURCE_MANIFEST.json']).items():
 b=(out/name).read_bytes()
 assert len(b)==receipt['bytes'] and hashlib.sha256(b).hexdigest()==receipt['sha256'],name
print('VL12_COMPLETE_INLINE_SOURCE_RECOVERY_PASS',len(sources),flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY_NEW.py')],cwd=out,check=True)
```
