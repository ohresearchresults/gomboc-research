# figure-0481

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Steady Comet 83 — two-carrier separation, exact one-cap C180, and affine reconsolidation

## Outcome

No exact homogeneous own-centred strict110/additionalweak000 body was found, so I do **not** claim completion. The strongest new exact geometry result is substantially better than the requested conditional C186 route: from literal `SC83_BF35_CARRIER17_M50_G4`, one coordinated second-carrier **normal/support replacement** makes the complete unwanted physical packet strictly one-cap separable while simultaneously dropping the pre-cap maximal complex from C198 to C192. Adding the proved separator then realizes an exact simple **V60/E90/F32, C180** one-cap descendant. A rational affine reconsolidation of that same C180 incidence is exact strict222/weak000 with exactly **one physical P bar and one same-centre polar Q bar**.

Thus the old C186 conditional target is superseded on this branch: the topology-changing second-carrier move earns six complexity units before the cap, and the whole-packet cap earns twelve more, giving C180. Final acceptance still requires strict110/weak000 with E<=249; no such endpoint is claimed.

The authoritative incoming result is `figure-0476`, SHA-256 `896976dda03b904508bcc928b7ce54fd26da87458381587b26dfc7c45bc64b86`. It supplies `SC83_BF35_CARRIER17_M50_G4`, V66/E99/F35/C198 strict222/weak000, and the transferred exact convex interlock on packet vertices `{2,9,47}` versus retained `{22,40}`. :contentReference[oaicite:0]{index=0} The literal parent records the exact child mechanics and positive barycentric obstruction. :contentReference[oaicite:1]{index=1}

I read the supplied 967-line continuation journal through EOF. Mounted receipt: 162468 bytes, SHA-256 `05fbc56d6e6944292dba0d4a9d6f460c805fa33a21f1e86b3af3e2b22f525d5d`. The active target is C<500, hence E<=249. :contentReference[oaicite:2]{index=2}

## 1. Coordinated second-carrier replacement

Start from the exact 35-row packet24 H representation used by the parent. Retain the first carrier move

```text
row17: [-10698, 5673, 17646, 10000]
    -> [-10698, 5673, 17646,  9950]
```

and make the second, topology-changing normal/support replacement

```text
row2:  [-3565,-11566, 19679,10000]
    -> [ 3160, 16386,-11425,10000].
```

All other rows remain exactly the literal packet24 rows. Old input row8 becomes inactive after rebuilding the exact hull. The resulting exact body is `SC83_BF35_TWO_CARRIER_SEP_C192`.

### Exact maximal geometry and mechanics

- `V=64, E=96, F=34, C=192`; simple, `2E=3V`.
- Strict census `(S,U,H)=(4,2,4)`; `S=[1,2,16,26]`, `U=[2,63]`, `H=[[2,57],[18,52],[29,41],[44,46]]`.
- Additional weak census `000`; primitive-zero census `000`.
- Actual uniform volume approximately `1.0409452723445014`; actual filled-volume centroid approximately `(0.02121898605020252,0.00032499378866481193,0.024272873776338532)`.
- Common centred-coordinate denominator: 4204 bits.
- Maximal-face histogram: `3×3, 8×4, 8×5, 8×6, 2×7, 2×8, 2×10, 1×13`.
- Exact input: 919 bytes, SHA-256 `0b2844a7974f5e9c61d71520888c8663e7ad03ae5450ac5f0d48a5a51d34f9d5`.
- Full exact audit: 281696 bytes, SHA-256 `ac756331836fae90dd726d12f0be07a0a959583dc7f2bdc70e36be6aa76a768e`.

### Complete physical P landscape

P roots `[2,63]`; exactly one positive bar; `TP in [930603238180,930603238181)/10^12`.

```text
peak 2 -> elder 63
death edge [44,46]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,19,20,22,23,24,25,26,37,39,44]
cut [[2,57],[4,13],[5,62],[6,16],[7,17],[7,18],[8,32],[8,55],[10,61],[11,28],[12,21],[14,33],[15,60],[20,59],[22,43],[26,29],[37,51],[39,45],[39,49],[44,45],[44,46]]
path [2,1,0,19,25,44,46,48,63]
```

The dying packet is exactly **25 vertices / 21 cut edges**, hence cycle rank `r=(25-21+2)/2=3`.

### Complete same-centre Q landscape

Q roots `[1,2,16,26]`; exactly three positive bars; `TQ in [659078520317,659078520318)/10^12`.

```text
peak26 -> elder1
death [14,26]
component [26]
cut [[26,0],[26,8],[26,10],[26,11],[26,14],[26,24]]
path [26,14,1]

peak16 -> elder1
death [9,16]
component [16]
cut [[16,8],[16,9],[16,23],[16,24],[16,30]]
path [16,9,11,26,14,1]

peak2 -> elder1
death [2,25]
component [2]
cut [[2,3],[2,7],[2,10],[2,12],[2,15],[2,20],[2,21],[2,25]]
path [2,25,8,23,24,26,14,1]
```

This is a genuine topology change and not merely destruction of the old sparse certificate: the rebuilt current packet itself is strictly separable.

## 2. Exact packet/complement separation

For the rebuilt C192 body's raw exact vertices, take `n=(-737,-4,-1000)`. The exact packet minimum is

```text
min_packet n·x = 50411676845000/149696146691
               ≈ 336.7600166025572,
```

attained at packet vertex44. The exact retained-complement maximum is

```text
max_retained n·x = 123739158596/452630003
                 ≈ 273.3781626844564,
```

attained at retained vertex43. Hence the convex hulls are strictly separated. Choose the rational cap

```text
-737*x - 4*y - 1000*z <= 300.
```

Its exact margins are

```text
packet rejection = 5502832837700/149696146691 > 0,
retained inclusion = 12049842304/452630003 > 0.
```

Thus the entire 25-vertex packet is removed and every retained vertex remains strictly inside; no floating LP inference is involved.

## 3. Exact realized one-cap body: C180

Append cap row `[-737,-4,-1000,300]` and rebuild everything exactly. `SC83_BF35_ONECAP_C180_RAW` has:

- `V=60, E=90, F=32, C=180`; simple.
- Strict `(S,U,H)=(11,5,14)`; additional weak `000`; primitive-zero `000`.
- Actual uniform volume approximately `0.6961881689027343`; actual centroid approximately `(0.21824182522612687,0.10125722200174972,0.17138896901065798)`.
- Common centred denominator 3937 bits.
- Face histogram `3×3, 11×4, 7×5, 8×6, 1×10, 1×13, 1×21`.
- Exact input 939 bytes, SHA-256 `204ef79f1bdc1386108c0102f1be56af857456b3e12d69bded58ec92c06d9af8`.
- Full audit 743038 bytes, SHA-256 `35b1262cd41c7c8673d9c951974dabed6f67d4663ae2030fd46e20c423153de9`.

The cycle-credit transition is actually realized: `V 64->60`, `E 96->90`, `F 34->32`, `C 192->180`. The raw cap is mechanically poor and is preserved as an exact intermediate, not the preferred continuation endpoint.

## 4. Rational affine reconsolidation of the C180 incidence

Apply exact nonsingular rational `y=A x` with

```text
A = (1/100000) *
[[138868,  24270, 28466],
 [     0, 114247, -7309],
 [     0,      0, 63031]].
```

The verifier transforms halfspace normals exactly by `A^{-T}` and re-runs the exhaustive H hull, maximal geometry, three mass identities, strict/weak face/vertex/mixed-edge mechanics and same-centre polar landscape. Incidence is preserved and the filled centroid transforms exactly; no free reference centre is substituted.

The promoted endpoint `SC83_BF35_ONECAP_C180_AFFINE222` has:

- `V=60, E=90, F=32, C=180`.
- Strict `(S,U,H)=(2,2,2)`; `S=[4,9]`, `U=[2,59]`, `H=[[17,54],[38,45]]`.
- Additional weak `000`; primitive-zero `000`.
- Actual volume approximately `0.6961900651607675`; actual centroid approximately `(0.3764307695534164,0.10315651867535,0.10802818105710782)` in transformed raw coordinates.
- Common centred denominator 3953 bits.
- Face histogram `3×3, 11×4, 7×5, 8×6, 1×10, 1×13, 1×21`.
- Exact transformed H input 2484 bytes, SHA-256 `0ba58fe2613d6f69cc62cc11f15921d4ae89af7819b4063b98f5f52288e8cf8b`.
- Full exact audit 146355 bytes, SHA-256 `2fb468018e02d6b9b77de59443e8c475d820d3e3742a1b8121d2185a2dc68287`.

### Complete P landscape of promoted C180

P roots `[2,59]`; exactly one positive bar; `TP in [2235872168752,2235872168753)/10^12`.

```text
peak 2 -> elder 59
death edge [38,45]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,27,29,32,37,38]
cut [[0,51],[1,30],[2,57],[6,58],[8,23],[8,40],[9,24],[10,56],[12,23],[12,24],[13,41],[13,46],[14,30],[14,49],[16,26],[17,54],[18,53],[19,35],[22,47],[22,52],[27,26],[29,31],[29,47],[37,55],[38,45]]
path [2,0,1,3,4,5,7,9,11,15,19,20,38,45,59]
```

P packet = **29 vertices / 25 cut edges**.

### Complete Q landscape of promoted C180

Q roots `[4,9]`; exactly one positive bar; `TQ in [3567774643467,3567774643468)/10^12`.

```text
peak 4 -> elder 9
death edge [2,14]
component [1,2,3,4,5,15,16,17,18,30]
cut [[1,8],[1,12],[1,22],[1,31],[2,14],[2,31],[4,31],[5,0],[5,8],[5,11],[5,14],[15,31],[16,31],[17,31],[18,31],[30,31]]
path [4,3,15,2,14,0,11,23,9]
```

Q packet = **10 vertices / 16 cut edges**.

The affine step therefore reconsolidates the mechanically exploded cap to an exact weak-free 222 body with one residual packet on each side. This is the strongest continuation object from this branch, but it is not 110.

## 5. Scope of negative evidence

No exact obstruction for the full five-dimensional SPD orbit of the new C180 incidence was proved. Finite affine/SPD failures are not exclusions and are not promoted as such. The earlier exact S>=2 corridor belongs to the old C198 two-cap incidence and does not transfer automatically to C180.

The durable advance is exact geometry: the transferred packet/complement interlock is genuinely removed by a second carrier replacement, strict one-cap separability is proved with rational margins, the one-cap construction realizes C180, and a rational affine map reconsolidates both landscapes to one bar each.

## 6. Source-complete recovery capsule

Standalone `SC83_C180_VERIFY.py` contains the complete parent H rows, exact two-carrier modifications, exhaustive rational H hull, maximal faces/true edges, three exact mass identities, strict/additional-weak S/U/mixed-H audit, exact P/Q landscapes, separation proof, cap construction, rational affine transformation and all asserted receipts. It needs only CPython 3.13.5 standard library; no parent file or numerical library is required.

```text
SC83_C180_VERIFY.py
17276 bytes
SHA-256 033968bb2c49df312a8d92cc89d3a2e015404b329529761fe824f77ec34aabe7

LZMA payload 6520 bytes
SHA-256 b35a5156043c417cb5fb5a2b2c22e78e01e1c1864c86e997a82ae8cc2596ff6d
base64 characters 8696
```

Save the following decoder as `RECOVER_SC83_C180.py`, run it, then run `python -B -S SC83_C180_VERIFY.py`.

```python
import base64,hashlib,lzma,pathlib
B64='''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'''
x=base64.b64decode(B64)
assert len(x)==6520 and hashlib.sha256(x).hexdigest()=='b35a5156043c417cb5fb5a2b2c22e78e01e1c1864c86e997a82ae8cc2596ff6d'
b=lzma.decompress(x)
assert len(b)==17276 and hashlib.sha256(b).hexdigest()=='033968bb2c49df312a8d92cc89d3a2e015404b329529761fe824f77ec34aabe7'
pathlib.Path('SC83_C180_VERIFY.py').write_bytes(b)
print('SC83_C180_SOURCE_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
```

Observed fresh cold-replay markers:

```text
SC83_C180_SOURCE_RECOVERY_PASS 17276 033968bb2c49df312a8d92cc89d3a2e015404b329529761fe824f77ec34aabe7
NW00_EXACT_H_TETRA446_PRISM446_WEAK123_UNBOUNDED_CONTROLS_PASS
SC83_TWO_CARRIER_ONECAP_C180_EXACT_PASS 50411676845000/149696146691 123739158596/452630003
SC83_RECEIPT SC83_BF35_TWO_CARRIER_SEP_C192 919 0b2844a7974f5e9c61d71520888c8663e7ad03ae5450ac5f0d48a5a51d34f9d5 281696 ac756331836fae90dd726d12f0be07a0a959583dc7f2bdc70e36be6aa76a768e
SC83_RECEIPT SC83_BF35_ONECAP_C180_RAW 939 204ef79f1bdc1386108c0102f1be56af857456b3e12d69bded58ec92c06d9af8 743038 35b1262cd41c7c8673d9c951974dabed6f67d4663ae2030fd46e20c423153de9
SC83_RECEIPT SC83_BF35_ONECAP_C180_AFFINE222 2484 0ba58fe2613d6f69cc62cc11f15921d4ae89af7819b4063b98f5f52288e8cf8b 146355 2fb468018e02d6b9b77de59443e8c475d820d3e3742a1b8121d2185a2dc68287
```

Evidence tier is one exhaustive exact H-poly mechanics implementation with three exact mass identities plus successful source-only cold replay. The inherited tetra446, weak-prism and unbounded-H controls pass. No second independent full mechanics implementation is claimed.

## 7. Most useful continuation

Continue from `SC83_BF35_ONECAP_C180_AFFINE222`, not from the row17 C198 child and not from the mechanically exploded raw cap. It has E90, leaving **159 final-edge slots** under E<=249.

1. Attack the 10-vertex/16-cut Q packet around death edge `[2,14]`, allowing support turnover and root exchange while preserving or later recovering one physical root.
2. Then attack the 29-vertex/25-cut P packet dying on `[38,45]`.
3. Do not freeze present root identities; temporary S/U/H/Q births are acceptable, but every promoted body must rebuild maximal hull, actual uniform centroid, strict/weak mixed mechanics and both complete landscapes.
4. The fixed-incidence SPD cone of C180 remains logically open; a rational 110 cell would be immediately promotable, but finite metric failure must not be upgraded to exclusion.

No strict110/additionalweak000 C<500 construction is claimed. The durable advance is an exact **C180 strict222/weak000 one-cap architecture with one P and one Q residual packet**, reached by proved two-carrier separation and exact rational affine reconsolidation.
