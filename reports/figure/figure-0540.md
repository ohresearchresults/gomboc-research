# figure-0540

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# R62 — physical H24/G3 hybrids and finite material continuation

## Outcome

**No own strict110 body was obtained.** I retained eleven new rational bodies and certified their complete maximal complexes, filled-volume centroids, strict and closed-weak equilibria, and every positive P/Q bar. The most useful results are a genuine physical hull hybrid with a replaced defective stable carrier, a substantially improved finite material-repair descendant, and a four-decimal lattice version with an exactly located facet flip.

The required physical inputs were used literally: H24 is `R3_HBRIDGE_S1_G3`, not a polar alias; G3 is `W51_ROBUST_G3`, including all 32 supplied material rows and its interior row 3. Their actual complexes were independently recovered as 44/66/24 and 31/87/58.

Here Δ denotes the dimensionless bar depth `(birth − death)/birth`, with birth and death measured as squared radial values. Counts below are `(S,U,H)`. Every listed exact endpoint has additional weak `(0,0,0)` and primitive-zero counts `(0,0,0)`.

| Body | V/E/F | C=2E | Strict S/U/H | Positive P/Q bars | Principal remaining depth |
|---|---:|---:|---:|---:|---:|
| Literal H24 | 44/66/24 | 132 | 1/2/1 | 1/0 | P 0.9668955428814634 |
| Literal G3 | 31/87/58 | 174 | 2/1/1 | 0/1 | Q 0.7827432115794241 |
| **R62_HYBRID_G5** | **40/111/73** | **222** | **2/1/1** | **0/1** | **Q 0.717015522969343** |
| R62_MULTIBASIN_G6 | 44/121/79 | 242 | 9/1/8 | 0/8 | Q 0.7034129684946863 |
| R62_INTERSECTION_ONE_G5 | 46/69/25 | 138 | 1/2/1 | 1/0 | P 0.9633837314044774 |
| R62_INTERSECTION_G5 | 48/72/26 | 144 | 1/2/1 | 1/0 | P 0.9637506775643248 |
| R62_INTERSECTION_CONT_G5 | 50/75/27 | 150 | 1/2/1 | 1/0 | P 0.954688801596139 |
| **R62_REPAIR_G5** | **34/96/64** | **192** | **2/1/1** | **0/1** | **Q 0.5797391045261** |
| R62_REPAIR_G6 | 34/96/64 | 192 | 2/1/1 | 0/1 | Q 0.5797353533243755 |
| **R62_LATTICE_G4** | **34/96/64** | **192** | **2/1/1** | **0/1** | **Q 0.57979804559242** |

The repaired bodies are finite positional material-repair descendants, **not unmodified unions or intersections**. This distinction is encoded in the reconstruction and lineage records.

## Physical family and exact poses

Write A for the literal H24 H-body and B for the convex hull of the literal G3 input rows divided by 1000. For rational u, define

`R(u) = ((1-u·u)I + 2uuᵀ + 2[u]×)/(1+u·u)`.

For positive rational a,b and three rational shear entries v, define

`L = [[a,0,0],[v0,b,0],[v1,v2,1/(ab)]]`.

The physical global map is **y=Lᵀx**, equivalently row-vector `x@L`; det L=1. The union family is `Lᵀ conv((sRA+t) ∪ B)`. The intersection family is `Lᵀ(A ∩ (sRB+t))`. All poses below use the parents’ literal raw frames. Divide u,s,t,a,b,v by D.

| Endpoint | D | u | s | t | a,b | v |
|---|---:|---|---:|---|---|---|
| HYBRID_G5 | 100000 | [-178562,-61181,88138] | 8482 | [16373,-74111,-10445] | [99376,99957] | [-1083,-965,1997] |
| MULTIBASIN_G6 | 1000000 | [-1792321,-587026,570198] | 99849 | [233972,-714825,-136101] | [996605,998885] | [-14762,-9480,18504] |
| INTERSECTION_ONE_G5 | 100000 | [-26176,-3086,6917] | 250000 | [70112,16451,-210175] | [100000,100000] | [0,0,0] |
| INTERSECTION_G5 | 100000 | [-26176,-3086,6917] | 250000 | [-15104,-20263,-97745] | [100000,100000] | [0,0,0] |
| INTERSECTION_CONT_G5 | 100000 | [-42191,7892,22685] | 324278 | [34299,-27499,-208654] | [98663,100781] | [-3015,2871,1189] |

The complexity guarantees hold throughout the corresponding full-dimensional physical families: the hull union has at most 75 extreme vertices and therefore E≤219, C≤438; the intersection has at most 82 maximal facets and therefore E≤240, C≤480. These follow from the three-dimensional polytope inequalities and do not imply any equilibrium inheritance.

## What the genuine hull hybrid actually replaces

For `R62_HYBRID_G5`, all 31 extreme B vertices survive, while the surviving H24 vertices are original canonical A indices `[0,2,3,15,16,17,18,21,23]`. The new maximal complex has one A-only hexagonal facet, 51 B-only facets, and 21 mixed triangular facets.

The only surviving original A facet is canonical facet 2, **not H24’s stable facet 3**. Thus this construction does not transfer H24’s S1 property. The B facets removed by visibility are canonical parent facets `[8,12,14,16,18,29,32]`.

The original junior stable B triangle with literal rows `[10,29,30]` is physically hidden. Its replacement is the mixed stable triangle **A23 + B20 + B26**. The elder stable triangle remains B[4,30,31], the unique unstable vertex remains B0, and the saddle remains the physical B[2,5] edge. This is genuine defective-carrier replacement, but not cancellation.

Fresh filled integration gives

`volume ≈ 7.530032144065614`

`centroid ≈ [-0.048650938299054446,-0.19876145517824526,0.3442318969464569]`.

For comparison, the two transformed input volumes sum to only 7.245532494467039. The convexly filled bridge contributes material beyond that sum; additive-component mass would be wrong even before addressing overlap.

In the hybrid’s canonical complex, the sole Q bar has peak 41, elder 15, and attaining dual edge [12,13]. Its exact component is

`[0,6,7,9,10,11,13,14,16,18,19,21,22,23,24,32,33,34,35,36,37,38,39,40,41,47,56,66]`.

Its cut is

`[[0,1],[0,2],[7,8],[12,13],[14,15],[16,17],[19,20],[24,26],[13,28],[39,46],[28,47],[47,52],[55,56],[58,66],[66,68]]`.

An attaining path is

`[41,38,39,35,24,23,19,16,18,21,22,11,6,13,12,2,3,4,5,1,8,15]`.

The certificate reconstructs exact birth and death, proves that the maximum cut gate equals death, and independently checks that the minimum gate on this path equals death.

## Why the nonwinning multi-basin endpoint matters

The U1-only guarded continuation produced `R62_MULTIBASIN_G6`, a genuine physical union with strict 9/1/8. Its eight positive Q depths are

`[0.7034129684946863,0.00019275982877075582,0.00007230295836449759,0.00006260874465814106,0.00001866469687191316,0.000007453945361333336,0.000005744013633852695,0.00000031800025109380263]`.

All eight are retained and certified, rather than suppressing the seven small bars. The whole-landscape log loss is strictly lower than the main hybrid’s loss despite having more stable equilibria. This comparison is proved **exactly**, without comparing rounded logarithms: the verifier compares the rational products of all birth/death ratios. Those products are approximately 3.4032396405772034 for MULTIBASIN and 3.533762738529086 for HYBRID. Thus even the complete aggregate loss is not class-monotone. This is a concrete reason to retain the S-count guard, not evidence against the physical family.

## Intersection continuation

The one-plane and two-plane intersections preserve H24’s sole stable facet and its elder unstable vertex, while introducing genuinely mixed vertices at the other tip. The one-plane endpoint has six mixed vertices; the two-plane endpoint has eight. The continued intersection has thirteen mixed vertices and three active B facets, originating from B row triples `[8,15,20]`, `[10,29,30]`, and `[10,20,26]`.

For the continued intersection, fresh integration gives

`volume ≈ 3.380115858066232`

`centroid ≈ [-0.26667329307938425,-0.20798806042532178,-0.0426559406052284]`.

Its exact own census is 1/2/1. The sole P bar has peak 49, elder 0, physical birth ≈1.5216286235527996 and death ≈0.06894681889285334. Its component is

`[18,19,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]`,

its cut is `[[15,18],[23,24],[25,29],[26,28],[27,31]]`, and an attaining path is

`[49,45,44,39,42,32,36,37,28,26,12,11,10,9,7,5,4,0]`.

Here [25,29] is the attaining primal edge. The remaining P defect is still large; the finite intersection exploration did not approach cancellation.

## Finite material repair and arithmetic endpoint

Starting from the exact 40-vertex union, I allowed finite physical point displacements with fresh mass integration and live contact reconstruction. Six points became interior and were removed before the next positional stage. The retained floating checkpoints are complete, and the exact final bodies do not depend on replaying an optimizer.

The raw 34 repair rows descend from original material indices

`[45,44,46,75,74,73,72,49,51,21,18,23,50,52,48,71,54,53,58,55,56,70,57,60,59,69,61,68,62,64,63,67,65,66]`,

where material 0…43 are canonical A vertices and material 44+j is literal B row j. The generated contact certificate gives every exact displacement from the original union. The junior stable patch changes again to descendants of **B30, A21, A23**; the saddle remains descendants of B2/B5.

`R62_LATTICE_G4` is a useful simpler-arithmetic endpoint. It differs from ordinary four-decimal rounding by at most **one 10⁻⁴ grid unit per coordinate**. Ordinary rounding is strict 2/4/4, with three genuinely positive P depths

`[5.407680747584978e-9,4.0559133818172466e-10,3.322553335450446e-11]`.

The lattice repair removes all three without hiding weak contacts. Its sole Q bar increases slightly, to 0.57979804559242. The MILP supplied a feasible incumbent, not an optimality proof.

For the lattice endpoint, lexicographically sorted canonical vertex numerators, with common denominator 10000, are

```python
V=[[-25000,-11458,12173],[-24698,-2139,1591],[-21166,-5339,-1069],[-14852,-13335,19284],[-8516,-12964,21953],[-3050,-11658,23124],[167,2005,-12378],[1010,5276,-11609],[1729,-8724,-3166],[1737,-9715,23234],[1747,8323,-10137],[1946,11380,-6815],[2305,-8869,-525],[2580,13598,-3086],[3599,-8343,-2425],[5283,-6276,-9668],[5755,-7387,22526],[6536,8538,-8899],[7969,11593,-4602],[8175,-483,-10474],[8964,-4889,21226],[9642,4249,-9182],[10525,8109,-6656],[10847,11915,2876],[11448,-2306,19475],[12248,9151,-3559],[13423,-37,17243],[14050,8641,-682],[14885,2022,14627],[15101,2888,-2244],[15355,7778,2383],[15814,3845,11738],[16043,6743,5528],[16199,5426,8674]]
F=[[0,1,2],[0,13,1],[0,2,15],[0,8,3],[0,3,13],[0,15,8],[1,6,2],[1,7,6],[1,10,7],[1,11,10],[1,13,11],[2,6,15],[3,8,4],[3,4,13],[4,5,9],[4,12,5],[4,8,12],[4,9,13],[5,14,9],[5,12,14],[6,7,19],[6,19,15],[7,10,17],[7,17,21],[7,21,19],[8,14,12],[8,15,14],[9,16,13],[9,14,16],[10,11,17],[11,13,18],[11,18,17],[13,16,23],[13,23,18],[14,15,20],[14,20,16],[15,19,29],[15,24,20],[15,29,24],[16,20,23],[17,18,22],[17,22,21],[18,25,22],[18,23,25],[19,21,29],[20,24,23],[21,22,29],[22,25,29],[23,24,26],[23,27,25],[23,26,28],[23,30,27],[23,28,31],[23,32,30],[23,31,33],[23,33,32],[24,29,26],[25,27,29],[26,29,28],[27,30,29],[28,29,31],[29,30,32],[29,33,31],[29,32,33]]
E=sorted({tuple(sorted((f[k],f[(k+1)%3]))) for f in F for k in range(3)})
assert len(V)==34 and len(E)==96 and len(F)==64
```

Its exact volume is `3829714090727/400000000000`. Its exact first moment is

`[-564250479098450641/480000000000000000, -19290709384199323/16000000000000000, 5808597660411386339/2000000000000000000]`.

Its exact centroid is

`[-564250479098450641/4595656908872400000, -19290709384199323/153188563629080000, 5808597660411386339/19148570453635000000]`.

Canonical equilibrium carriers are S=[13,16], U=[0], H=[[2,6]]. The sole Q bar has peak 16, elder 13, and exact depth

`2660897311095690832091710471623021487313/4589345081085088553319244057451463189651`.

Its component is `[2,3,5,11,12,15,16,18,19,25,26,28,34,35,37,38,56,58,60]`; its cut is `[[0,2],[3,4],[6,11],[12,13],[14,15],[14,18],[11,21],[27,28],[32,35],[38,39],[37,45],[48,56],[50,58],[52,60],[60,62]]`; an attaining path is `[16,12,3,5,2,11,6,7,8,9,10,1,4,13]`.

The ordinary rounding gallery is also retained: G2 is strict 7/12/17 with 11 P and 6 Q bars; G3 is strict 5/14/17 with 13 P and 4 Q bars; G4 is strict 2/4/4 with 3 P and 1 Q bar. All their positive bars, however small, are regenerated in full.

## Exact changed-contact event

The linear material interpolation from REPAIR_G5 to LATTICE_G4 has a certified facet flip on raw repair indices `[14,15,21,23]`. Its old diagonal [14,21] is replaced by [15,23]. The unique coplanarity parameter in [0,1] is the root of

`-4298817763 + 10128396868 θ - 25407 θ² + 2 θ³ = 0`,

isolated exactly in

`[466668635707/1099511627776, 116667158927/274877906944]`.

Thus θ≈0.424432651659572. The certificate proves strict monotonicity of the cubic, strict supporting-plane separation of every other material point throughout this isolating interval, and strict convexity of the coplanar quadrilateral. This is a proved contact transition, **not** a claim that the entire interpolation has constant equilibrium class.

## Search scope and continuation

The numerical exploration included a completed 2646-pose targeted union grid, broad free-pose scouts, U1-only and S≤2/U1 guarded union continuations, free material continuation, guarded S1/U≤2 intersection continuation, and finite lattice repair. Complete sources, nondefault parameters, seeds and retained checkpoints are in the capsule’s README and scripts. Interrupted runs are identified there: in particular the three free material stages retained iterations 72,79,93, and the second intersection continuation retained iteration 257 rather than completing its requested 700 steps.

Numerical screening used floating contact reconstruction and complete-chord landscapes; it is not an exclusion proof. The frozen rational endpoints use maximal facets, true edges and actual dual adjacency, with exact filled mass and both edge-normal coefficients. Independent V/H reconstruction checks passed for REPAIR_G5 and LATTICE_G4; independent Fraction/integer mechanics checks passed for the main union and continued intersection. No equilibrium class was inherited from a parent.

The most useful continuation is the Q-side material family seeded by `F62L_pin.json`, preserving U1 and all nonprincipal Q escape guards while changing the **retained B2/B5 saddle region together with the mixed junior stable patch**. The original complementary-region splice removed the parent junior stable face but left this saddle mechanism intact. A single outgoing-chord objective is not a substitute for the full current bar and cut landscape.

## Recovery and provenance

I read the complete supplied journal and all 82 decoded W51 source files. The native journal’s 318894-byte SHA-256 matched `2125c93ed57efe0a9329da6791e24c1d90f611e3f89323bcfe07a865edd3bd7d`; W51’s decoded raw source packet matched `ce7c3f1ad9ce6d5696792ac9fd6ad791c37c39dbb5442783e9413477c1eea559`. The supplied parent authority is assignment `figure-0537`, payload digest `05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21`. No missing physical-input dependency remains.

The exact input hashes are H24 `2db11dc460899bc3d49af4fc7af40230e3e6d1ac657b73350b677405d88cd6d91` and G3 `0fa93190d2a33864b219b2b73b6a433236f1e1338dea7ec49075c3ca2ac033fc`.

Save the following complete source capsule as `RECOVER62.py`, then run:

```sh
python -B -S RECOVER62.py R62_SOURCE
cd R62_SOURCE
python -B -S verify_r62.py
```

Cold exact recovery was tested with CPython 3.13.5 and **requires only the standard library**. Optional numerical discovery uses NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu, float64, and one CPU thread. Every necessary numerical helper and checkpoint is included; exact recovery does not depend on numerical replay.

Expected terminal markers are:

```text
R62_SOURCE_RECOVERY_PASS 50 115294 e3266d4a5ee58802d9ac6cc80fa35f2bddaafa681209aa9d51121ccd55ede8b2
R62_EXACT_FACET_FLIP_PASS ['466668635707/1099511627776', '116667158927/274877906944'] 0.424432651659572
R62_COLD_RECOVERY_AND_EXACT_AUDIT_PASS 13 NO_OWN110_CLAIM
```

`EXPECTED62.json` contains byte counts and SHA-256 values for every complete output certificate. Important receipts include HYBRID audit: 30776 bytes, `5d32243ea227fb9be802462cb6e1ad5148c5b7a5308b6bae1111dac0353ce599`; REPAIR_G5 audit: 3534 bytes, `3ab5b4ff0c7c1df98e7ee216ed4a5ddaa8d1cd47f7d99df81ef9d2818e0393b1`; LATTICE_G4 audit: 3459 bytes, `5604cf4f3b9e7357ba597473179d4bc3aeccfce343e927a7086dbda2126f149a`; flip certificate: 6453 bytes, `be693d2c151a6bcf208d539fe0f1126ecf3bf30898fdc4c5786eadd2e2b2c5ed`.

One unit correction is explicit in the verifier: the original V-auditor stores radial endpoints in centroid-numerator units. New audits convert P endpoints by `1/T²` and Q endpoints by `T²`, where `T=24*volume*D⁴`, before physical cut/path checks. Bar depths are unchanged.

Convenience copies: complete source and regenerated certificates (`R62_HANDOFF.zip`), 225025 bytes, SHA-256 `f5ae4a37b34e83bb129f86d1d13af64bc9f27b54be723bb2cee8695661d866a0`; recovery script (`RECOVER62.py`), 44848 bytes, SHA-256 `f4a95eaafa12cc18fa7226ebb2a5c3a41053015afb43ea4d8dee56e9e664308e`. Neither download is required by the inline capsule.

```python
# R62: complete source/input/checkpoint recovery, CPython standard library.
import base64,hashlib,json,lzma,sys
from pathlib import Path,PurePosixPath
DATA="""
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
"""
RAW_BYTES=115294
RAW_SHA256="e3266d4a5ee58802d9ac6cc80fa35f2bddaafa681209aa9d51121ccd55ede8b2"
def main():
    raw=lzma.decompress(base64.b64decode("".join(DATA.split()),validate=True))
    assert len(raw)==RAW_BYTES and hashlib.sha256(raw).hexdigest()==RAW_SHA256
    files=json.loads(raw);manifest=json.loads(files["SOURCE62_MANIFEST.json"])
    root=Path(sys.argv[1] if len(sys.argv)>1 else "R62_SOURCE")
    root.mkdir(parents=True,exist_ok=True)
    for name,text in sorted(files.items()):
        rel=PurePosixPath(name)
        assert not rel.is_absolute() and ".." not in rel.parts
        b=text.encode("utf-8")
        if name in manifest:
            rec=manifest[name]
            assert len(b)==rec["bytes"] and hashlib.sha256(b).hexdigest()==rec["sha256"]
        p=root.joinpath(*rel.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    print("R62_SOURCE_RECOVERY_PASS",len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=="__main__":main()
```
