# figure-0467

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> The reported C=198 candidate still has two unstable equilibria and one saddle; it does not meet the gömböc condition.
<!-- historical-status:end -->

---

# Steady Comet 83 — exact BF35 whole-packet contraction under C<500

## Outcome

No exact strict110/additionalweak000 body was found, so this branch is **not complete** and I do not claim a new accepted record. The strongest exact changed body obtained is **`SC83_BF35_REPLACE5_PACKET24_G4`**, an own-centred homogeneous `V66/E99/F35/C198` strict121, weak000, primitive-zero000 descendant of BF35REC_G4. It keeps the same-centre polar landscape exactly cancelled (`Qbars=[]`) while contracting the entire physical packet from the literal BF35 parent’s corrected **29 vertices / 25 cut edges** to **24 vertices / 20 cut edges**. The authoritative parent explicitly corrects 30→29.

The live acceptance target is `C=2E<500`, hence `E<=249`; the older generic E<=310 target is obsolete. The new body has E99, leaving 150 final-edge slots.

## Source authority and reading closure

I read the attached 2066-line journal through EOF, including both literal parent payloads, and decoded/read the portable exact source pack before research. Journal snapshot: 238713 bytes, SHA-256 `fe0f29f9b06ae2353c755d6852a196ef8baccc0a5c732939a6a71f2bafb350fb`. Authoritative parents are `figure-0450`, SHA-256 `4acbb52f78b198f4db9f9fc83e18ec2b6b446d3703b82c4ab1b238b5275533f8` and `figure-0451`, SHA-256 `0bfa541ab2de1a9c2b23e2917ca7c671e99c34053e05cca39db1d0838c5bb62c`. No source conflict was found beyond the already-declared BF35 29/25 correction.

Portable-parent receipts: XZ 47316 bytes / SHA-256 `45b634630ba18cf489f4dd1487eb60d42feee425cc5cad8009b7b1aea99558b0`; decoded dictionary 156800 bytes / SHA-256 `2ab044fb2306d7ffe31d58a05e5458e2b6b06c593ccfd255d828d9831be708db`. A new all-52-body cold replay was **not** completed here; the exact BF35 computations below were freshly executed.

BF35 was chosen over BA69 because both are S1/Q0 own121 entrances but BF35 starts at E99 rather than E183, leaves 150 rather than 66 final-edge slots, and has substantially better minimum-edge reserve. BA69’s lower scalar P depth remains a complementary checkpoint, not a discarded branch.

## Exact changed body: `SC83_BF35_REPLACE5_PACKET24_G4`

- Maximal complex: `V=66, E=99, F=35, C=198`; E counts true maximal-hull edges only.
- Strict census: `S=[1]`, `U=[4,65]`, `H=[[47,65]]`, i.e. strict `(1,2,1)`.
- Additional weak census: `(0,0,0)`; primitive-zero census `(0,0,0)`.
- Common actual-centred coordinate denominator: 4376 bits.
- Actual uniform volume `≈1.0581151242791984`; actual centroid `≈(0.02248364264847009,0.008024327922806943,0.017322130146690127)`. Exact fractions are deterministically regenerated from the literal H rows.
- Face histogram: `5×3,7×4,9×5,6×6,2×7,2×8,1×9,1×10,1×11,1×14`.
- `minedge/R ∈ [3029548588,3029548589)/1e12`; `r/R ∈ [236899126947,236899126948)/1e12`; `Vol/R^3 ∈ [256810785334,256810785335)/1e12`.
- P forest depth 16; minimum selected true-edge cosine `[1550274419,1550274420)/1e12`.
- Q forest depth 20, unique root `[1]`; minimum selected true-edge cosine `[173896688,173896689)/1e12`.

Input receipt: **921 bytes**, SHA-256 `36e2f3d550c2f6da45ed54e31bdc70f2eb597d436dd6e4291a794808efb58667`. Full exact audit/report: **89405 bytes**, SHA-256 `7f08743b50f4d50d1161de8a98dc421bfd83427732b24f8ae2ee05e77d954a84`. The report contains all 35 maximal face cycles, all 99 true edges, exact mass/centroid, and all mechanics predicates.

### Complete P/Q packet

`Q roots=[1]`, `Qbars=[]` exactly, so `TQ=0`. The generic exact cube-root enclosure prints `[0,1]` for zero; it is not a positive bar.

Exactly one positive P bar remains:

```text
peak 4; elder 65; death edge 47--65
path [4,2,1,0,20,25,34,37,39,46,47,65]
component [0,1,2,3,4,5,6,7,8,9,10,11,17,20,21,23,24,25,34,37,38,39,46,47]
cut [[2,57],[4,59],[5,14],[6,64],[7,19],[8,31],[8,56],[9,16],[9,18],[10,12],[11,63],[17,62],[21,61],[23,45],[24,40],[38,48],[39,28],[46,51],[47,43],[47,65]]
```

Thus the whole packet contracts **29/25 → 24/20**. TP is `[823890801110,823890801111)/1e12`, slightly worse than BF35’s `[822447828147,822447828148)/1e12`; the improvement is therefore a real whole-interface contraction rather than a scalar-depth improvement. Global-radius-relative P depth is `[332872941068,332872941069)/1e12`.

## Exact support replacement

From the 35 active BF35REC_G4 supports, remove:

```text
[-11114,7822,16372,10000]
[-11888,11237,13335,10000]
[-11289,16268,6227,10000]
[-12287,13817,9902,10000]
[15669,-8908,-11956,10000]
```

and add:

```text
[-11908,14037,10055,10015]
[-11098,7965,16569,10098]
[-11191,16296,6148,9982]
[-118072,113520,134887,100551]
[14943,-9383,-12716,10042]
```

The recovery payload below contains the complete 35 parent-active rows, these five replacements, the final 35-row H input, exact hull/mechanics/mass code, and full P/Q reconstruction. No external parent file is required.

## Complete active single-deletion census of BF35

All 35 active one-support deletions were audited exactly. Every child is `V64/E96/F34/C192`, weak000/primitivezero000. **None is strict110 and none is strict121.** Exactly one deletion retains S1: active position 9, row `[8653,2816,-16402,10000]`; that child is strict132 with `S=[1]`, `U=[5,37,63]`, `H=[[24,37],[45,63]]`, Qbars empty and two P bars:

```text
peak37 -> elder5, death24--37
component [37]
cut [[37,24],[37,39],[37,46]]
path [37,24,20,0,1,2,5]

peak5 -> elder63, death45--63
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,20,21,23,24,25,27,37,39,44,45]
cut [[2,55],[4,35],[5,57],[6,32],[7,62],[8,38],[9,43],[10,30],[11,31],[11,53],[12,19],[12,47],[14,61],[15,16],[15,29],[18,60],[21,59],[25,58],[27,40],[27,42],[37,46],[39,26],[44,49],[45,41],[45,63]]
path [5,2,1,0,20,24,37,39,44,45,63]
```

Its TP is `[823663041587,823663041588)/1e12`. This closes only the immediate **pure-deletion** layer of the fixed active BF35 representation. Ledger receipt: 10769 bytes, SHA-256 `e9bf28a0582a040fce433e800913bc82a21a2ad73cc67fb4e2cb365c44f53a82`.

## Sharpened final-bound two-terminal gate

The parent theorem gives `D <= (V+1)(2R^2-A-B)` for an own-centred U1/no-additional-weak-U target retaining two points `u,z`. Under final `E<=249`, degree>=3 implies `V<=166`, hence necessarily

`R^2 >= (A+B+D/167)/2`.

With fixed current centroid, retained two roots, and no circumradius increase past the larger retained-root radius, a necessary condition is `D/(B-A)<=167`. Exact-rational metric data give approximately BF35 `5.0998`, new packet24 body `5.110125339...`, BA69 `4.0831`: none is excluded. MONO14 is `318.1830...>167`, so only its **retained-two-root/fixed-centre/no-radius-increase** envelope is excluded by the sharpened C<500 bound. Centroid/radius/pair changes evade this scoped result.

## What was tried; evidence limits

Finite actual-mass support replacement was evaluated by rebuilding the exhaustive H hull, maximal geometry, uniform centroid and complete P/Q landscapes after every candidate. The productive path contracted the exact BF35 packet to 24/20 while preserving S1 and exact Q0. A later finite single-replacement window and a finite pair-replacement window did not beat 24/20 or produce strict110; earlier quota-style flow fragmented roots. These are finite negatives, not exclusions.

The promoted body was freshly replayed from the self-contained standard-library capsule. Evidence tier is one exhaustive exact H-poly mechanics implementation with three exact mass identities: boundary tetrahedra, coordinate-boundary divergence, and a positive own-centred tetrahedral fan. A separate common-grid V-side audit was attempted but timed out before producing a report, so **no second independent full mechanics audit is claimed**.

## Self-contained recovery capsule

The full exact verifier/reconstructor is 15772 bytes, SHA-256 `590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359`. Below is its complete LZMA-compressed literal payload, not a hash-only reference. Compressed payload: 5788 bytes, SHA-256 `2778dc7d13c9c6ddfa2be99b718b2567801e3e80a90c2fbf2221fae630f6ac3c`.

Save this decoder as `RECOVER_SC83_PACKET24.py` and run `python -B -S RECOVER_SC83_PACKET24.py`; it writes the exact `BF35_PACKET24_RECOVER.py` and verifies both byte count and SHA-256.

```python
import base64,hashlib,lzma,pathlib
B64='''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
kbHEZ/sCAAAAAARZWg=='''
x=base64.b64decode(B64)
assert len(x)==5788 and hashlib.sha256(x).hexdigest()=='2778dc7d13c9c6ddfa2be99b718b2567801e3e80a90c2fbf2221fae630f6ac3c'
b=lzma.decompress(x)
assert len(b)==15772 and hashlib.sha256(b).hexdigest()=='590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359'
pathlib.Path('BF35_PACKET24_RECOVER.py').write_bytes(b)
print('SC83_PACKET24_SOURCE_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
```

Then execute:

```text
python -B -S BF35_PACKET24_RECOVER.py
```

Expected markers:

```text
NW00_EXACT_H_TETRA446_PRISM446_WEAK123_UNBOUNDED_CONTROLS_PASS
SC83_BF35_PACKET24_EXACT_PASS 921 36e2f3d550c2f6da45ed54e31bdc70f2eb597d436dd6e4291a794808efb58667 89405 7f08743b50f4d50d1161de8a98dc421bfd83427732b24f8ae2ee05e77d954a84
```

For the exhaustive one-deletion layer:

```text
python -B -S BF35_PACKET24_RECOVER.py --deletions
```

Additional marker:

```text
SC83_BF35_ALL35_SINGLE_DELETIONS_NO_110_OR_121_PASS [9] 10769 e9bf28a0582a040fce433e800913bc82a21a2ad73cc67fb4e2cb365c44f53a82
```

Convenience copy only: BF35_PACKET24_RECOVER.py. The inline compressed payload is the durable recovery authority.

## Most useful continuation

Continue from `SC83_BF35_REPLACE5_PACKET24_G4`, while keeping BA69 as the lower-scalar-depth alternative. Do **not** spend another turn on literal one-support pruning; that layer is now exactly closed. Instead drive a coordinated multi-exit event across several of the current 20 cut edges using two/three simultaneous support replacements or added carriers, then reconsolidate S1/Q0 at the rebuilt actual filled centroid. Temporary U/H/Q births and root exchange are allowed; final acceptance remains strict110/weak000 with E<=249.

Merit should prioritize `(Qbars=0,S=1)`, then P-bar count and complete P component/cut size, then strict U/H and conditioning, with scalar TP secondary. This endpoint is the concrete reason: packet size improves 29/25→24/20 although TP rises slightly. With E99 there is ample final complexity budget for a genuine multi-carrier annihilation rather than preserving the 35-support chart at all costs.

No exact C<500 strict110/weak000 construction is claimed; unresolved work is annihilating this final 24/20 physical packet without recreating a positive polar packet.
