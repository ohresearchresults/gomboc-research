# figure-0476

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Comet 83 — exact affine corridor closure and carrier-wall handoff

## Outcome

No homogeneous own-centred strict110/additionalweak000 body was found. I do **not** have a global impossibility theorem for the entire five-dimensional SPD Gram cone of `SC83_BF35_CAP2_TURNOVER_G4`. The strongest exact fixed-incidence result is instead a source-complete **rational affine corridor exclusion** containing and extending both earlier numerical S2/U2 checkpoints, together with two exact rational C198 affine checkpoints. The strongest geometry continuation is an exact one-carrier checkpoint that crosses the nearest algebraic wall of the original one-cap separation certificate, but the obstruction immediately hands off to a new packet/complement intersection and the body becomes strict222 with one P and one Q bar rather than reopening C186.

The current literal parent is `figure-0471`, SHA-256 `2a5d92a204aefcc79842889962716db2628c9dcaed484f121f9007f439e05391`; it supplies the exact simple V66/E99/F35/C198 two-cap body, its strict18/10/26 mechanics and the exact original one-cap obstruction. The literal payload gives the complete active35-row input and full P/Q audit.

I read the entire continuation journal through EOF and re-used the exact parent source `BF35_PACKET24_RECOVER.py`, 15772 bytes, SHA-256 `590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359`. No alias/source conflict was found.

## 1. Exact rational fixed-incidence affine checkpoints

Write `K` for the exact raw `SC83_BF35_CAP2_TURNOVER_G4`, with its actual filled-volume centroid `c`. For either matrix below, the physical body is exactly

`K_i = A_i (K-c)`.

Because `A_i` is rational and invertible, this is a genuine uniformly filled rational polyhedron, incidence is unchanged, and its actual homogeneous centroid is exactly 0.

```text
A1 = [[837/500, -7/100,  69/1000],
      [0,        13/25,  -3/50],
      [0,        0,      23/20]]

A2 = [[581/500,  3/250, 29/250],
      [0,        281/500,34/125],
      [0,        0,      153/100]]
```

Both are exact `V66/E99/F35/C198`, weak000, primitivezero000, and strict222.

### `SC83_CAP2_AFFINE_G1_D1000`

- Strict census: `S=[0,9]`, `U=[0,65]`, `H=[[31,55],[48,50]]`.
- Common own-centred denominator: 3844 bits.
- `TP in [2010349824909,2010349824910)/1e12`.
- `TQ in [11157495409754,11157495409755)/1e12`.
- Exact input receipt: 154711 bytes, SHA-256 `3044218126088558b24d860631a429e5cf29b4e0cb8c1a6ffd8d08a6eedb3c6c`.
- Full exact audit: 571332 bytes, SHA-256 `40150a38d96bf20f2666b2e5342e265b723cda14ebcaf2f3b0ed3d6b51ef996f`.

Complete P landscape:
```text
roots [0,65]
peak0 -> elder65; death edge48--50
path [0,2,13,19,45,48,50,51,54,60,61,62,63,64,65]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,31,33,35,36,39,43,45,48]
cut [[6,37],[7,27],[9,40],[9,49],[11,52],[15,25],[15,28],[17,56],[18,57],[20,27],[21,29],[21,59],[22,32],[23,44],[24,26],[31,55],[35,53],[36,50],[39,42],[43,53],[43,60],[45,47],[48,50]]
```

Complete Q landscape:
```text
roots [0,9]
peak0 -> elder9; death edge8--10
path [0,33,25,10,8,7,9]
component [0,1,3,4,5,10,13,16,17,25,32,33]
cut [[0,6],[1,7],[1,9],[3,6],[4,6],[5,6],[5,18],[5,19],[5,20],[10,7],[10,8],[10,23],[13,6],[13,9],[16,6],[17,6],[25,7],[32,20],[33,2],[33,11],[33,15],[33,20],[33,22],[33,23],[33,26],[33,27],[33,34]]
```

### `SC83_CAP2_AFFINE_G2_D1000`

- Strict census: `S=[0,9]`, `U=[18,65]`, `H=[[12,32],[51,54]]`.
- Common own-centred denominator: 3846 bits.
- `TP in [1620772396646,1620772396647)/1e12`.
- `TQ in [11210348902781,11210348902782)/1e12`.
- Exact input receipt: 155004 bytes, SHA-256 `31b223ab06e41c82262dec059868c046ca1f31a65ce53413023172a42cc7c193`.
- Full exact audit: 571812 bytes, SHA-256 `dc8ed73cdad13b4582bfab71836b01418dd33e937fe9c7b5c134b98fd251558f`.

Complete P landscape:
```text
roots [18,65]
peak18 -> elder65; death edge12--32
path [18,11,1,0,3,5,8,9,12,32,55,56,57,58,63,65]
component [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,31,34,35,36,38,41,45,47,48,50,51]
cut [[2,24],[6,28],[7,23],[7,42],[10,43],[10,49],[12,32],[12,53],[14,23],[14,24],[15,32],[16,26],[16,29],[17,56],[19,21],[19,57],[20,28],[22,44],[34,52],[38,40],[38,60],[41,52],[41,59],[48,46],[51,54]]
```

Complete Q landscape:
```text
roots [0,9]
peak0 -> elder9; death edge5--6
path [0,33,32,5,6,9]
component [0,1,3,4,5,10,13,16,17,25,32,33]
cut [[0,6],[1,7],[1,9],[3,6],[4,6],[5,6],[5,18],[5,19],[5,20],[10,7],[10,8],[10,23],[13,6],[13,9],[16,6],[17,6],[25,7],[32,20],[33,2],[33,11],[33,15],[33,20],[33,22],[33,23],[33,26],[33,27],[33,34]]
```

These are exact rational freezes of the earlier numerical S2/U2 region, not new class110 candidates.

## 2. Exact affine-corridor exclusion containing both checkpoints

Define the rational affine family

`A(t)=A1+t(A2-A1)`.

For every real `t in [-1/2,2]`, exact Bernstein-sign evaluation proves `det A(t)>0` and proves that centered-polar vertices/faces 0 and 9 are both strict roots. Hence **every body in this entire fixed-incidence affine family has S>=2** and therefore cannot be strict110.

The determinant factors exactly as

`det A(t)=-(21t+260)(38t+115)(256t-837)/25000000`,

which is positive on the whole interval. For each true polar edge leaving roots 0 and 9, the score after applying `A(t)` is a rational polynomial divided by `det(A(t))^2`; all Bernstein coefficients of the cleared numerator are strictly negative on `[-1/2,2]`. The exact verifier emitted:

`SC83_CAP2_AFFINE_PATH_S0_S9_PERSIST_PASS -1/2 2`.

This is a **scoped one-parameter affine theorem**, not an exclusion of the full five-dimensional SPD orbit. In particular, a disconnected S1/U1 Gram cell elsewhere remains logically open. The parent itself explicitly left the fixed-incidence Gram-cell question open.

## 3. Exact carrier-wall analysis for reopening the C186 one-cap route

The original one-cap obstruction is the exact intersection of packet triangle `[9,37,47]` with retained segment `[22,40]`. I varied one supporting-plane **height** at a time, holding its normal and the five obstruction owner triples fixed. Each obstruction barycentric weight is then a Möbius rational function of the height increment `delta`, so the interval on which all five weights remain positive is exact.

Across all 15 incident support-height axes, the nearest algebraic wall of this specific certificate is:

```text
packet vertex 9, support row17
row17 = [-10698,5673,17646,10000]
delta* = -291064344773518473533590672859696358000 /
          6794114895348614923597437680516360249
       ~= -42.84065684152425
```

The next-nearest wall is retained vertex22/support23 on the positive side:

```text
row23 = [-9944,17443,4550,10000]
delta = 3742255861373808945431880079624667460 /
        84842981947203236205341392192889153
      ~= 44.10801901921092
```

Thus, **within the fixed owner-triple chart and while the five points retain their packet/complement roles**, no single incident fixed-normal height move with `|delta|<42.8406568415...` can destroy the original convex-intersection certificate. This is deliberately not promoted to a theorem about arbitrary normal motion or topology-changing support replacement.

## 4. Exact first carrier checkpoint beyond that wall

I crossed the nearest wall by changing only parent packet24 support row17:

```text
[-10698,5673,17646,10000]
          ->
[-10698,5673,17646, 9950]
```

All other `SC83_BF35_REPLACE5_PACKET24_G4` rows are unchanged. The exact child is `SC83_BF35_CARRIER17_M50_G4`:

- `V66/E99/F35/C198`.
- Strict `(S,U,H)=(2,2,2)` with `S=[1,17]`, `U=[4,65]`, `H=[[19,53],[47,65]]`.
- additional weak000, primitivezero000.
- common centered denominator 4376 bits.
- `TP in [823946382668,823946382669)/1e12`.
- `TQ in [7261356273,7261356274)/1e12`.
- Input 920 bytes, SHA-256 `ef321a3dc765f5442b7791b838551483ee7e31f55b22de0012e5ec290fdd13dc`.
- Full exact report 157540 bytes, SHA-256 `b09ae79e92c316880ddf8c83dc6a8cab7bf4eb9c22fdffc58b4d1121e024f16e`.

Complete P landscape:
```text
roots [4,65]
peak4 -> elder65; death edge47--65
path [4,2,1,0,20,25,34,37,39,46,47,65]
component [0,1,2,3,4,5,6,7,8,9,10,11,16,20,21,23,24,25,34,37,38,39,46,47]
cut [[2,57],[4,59],[5,14],[6,64],[7,17],[8,18],[8,19],[9,31],[9,56],[10,12],[11,63],[16,62],[21,61],[23,45],[24,40],[38,48],[39,28],[46,51],[47,43],[47,65]]
```

Complete Q landscape:
```text
roots [1,17]
peak17 -> elder1; death edge10--17
path [17,10,12,27,2,15,1]
component [17]
cut [[17,9],[17,10],[17,24],[17,25],[17,31]]
```

So crossing the nearest original certificate wall does **not** reopen the one-cap C186 route. The complete 24/20 physical packet remains nonseparable. A new exact sparse convex-hull intersection is:

```text
lambda2*v2 + lambda9*v9 + lambda47*v47
  = mu22*v22 + mu40*v40
```

with all coefficients strictly positive:

```text
lambda2  = 170716324837112895522357109665911217056654703533 /
           625020142627436843593742652438814187952335057000
lambda9  = 2150608643387240722279108210526070863793706167 /
           24039236254901417061297794324569776459705194500
lambda47 = 3187103944498045514337029834393801027496351945 /
           5000161141019494748749941219510513503618680456
mu22     = 1223466423557794441188966943392998260757618717 /
           1875060427882310530781227957316442563857005171
mu40     = 651594004324516089592261013923444303099386454 /
           1875060427882310530781227957316442563857005171
```

The three packet weights sum to 1 and the two retained weights sum to 1 exactly. This is a new exact obstruction, not a floating LP failure. It shows a concrete **obstruction handoff**: the first certificate is crossed, but the packet remains convexly interlocked with the complement.

## 5. What did not become a theorem

I also attacked the full fixed-incidence U1 sign-cell problem with exact negative-definite arrow-combination blockers and finite SPD searches. Every tested putative rooted escape pattern encountered blockers, and broad numerical searches continued to bottom out at at least two U and two S, but the blocker cover was not completed. I therefore make **no global claim** that the entire SPD orbit has U>=2 or S>=2. Transient blocker-state files are not promoted as durable proof objects.

Similarly, finite fixed-topology screens of a second single support-height motion from the row17 child did not find a separator; this is finite evidence only, not an exclusion of two-carrier normal/support replacement.

## 6. Durable recovery capsule

Exact dependencies:
```text
figure-0467
SHA c2b59f1bc19ca564bc7e3ed9432e0d24ff61b02d7274838f277e0ef3b9d99837
BF35_PACKET24_RECOVER.py
15772 bytes
SHA 590eb1e51405f5441ea1ed2e75406138a9be723aace312aeb0ab25eecff38359

figure-0471
SHA 2a5d92a204aefcc79842889962716db2628c9dcaed484f121f9007f439e05391
```

The consolidated exact source `SC83_SCOPE_AND_CARRIER.py` is 9100 bytes, SHA-256 `d0fcd709a911a42193fcb449e2edc5bdbfdf3fb1f58a6b16afad79eaa534592a`. It embeds the complete two-cap H input, both rational affine matrices, exact affine-path Bernstein proof, the single-height certificate-wall calculation, the row17 carrier child, and the new exact convex-intersection certificate. It requires CPython 3.13.5, the exact parent source above, and SymPy 1.14.0 for the polynomial/Bernstein family proof.

Compressed payload: 4036 bytes, SHA-256 `5a0acd9c8e67af62f1f7e16ddef674f482534d021f14597258b9ba603985ee78`.

Save the following decoder as `RECOVER_SC83_SCOPE.py` beside the exact parent source and run it; then run `python -B SC83_SCOPE_AND_CARRIER.py`.

```python
import base64,hashlib,lzma,pathlib
B64='''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'''
x=base64.b64decode(B64)
assert len(x)==4036 and hashlib.sha256(x).hexdigest()=='5a0acd9c8e67af62f1f7e16ddef674f482534d021f14597258b9ba603985ee78'
b=lzma.decompress(x)
assert len(b)==9100 and hashlib.sha256(b).hexdigest()=='d0fcd709a911a42193fcb449e2edc5bdbfdf3fb1f58a6b16afad79eaa534592a'
pathlib.Path('SC83_SCOPE_AND_CARRIER.py').write_bytes(b)
print('SC83_SCOPE_SOURCE_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
```

Expected exact terminal markers from the consolidated source are:
```text
SC83_CAP2_EXACT_AFFINE_222_ENDPOINTS_PASS ...
SC83_CAP2_AFFINE_PATH_S0_S9_PERSIST_PASS -1/2 2
SC83_ORIGINAL_INTERSECTION_NEAREST_SINGLE_HEIGHT_WALL_PASS 9 17 lo <exact fraction>
SC83_CARRIER17_NEW_ONECAP_OBSTRUCTION_PASS ...
SC83_SCOPE_AND_CARRIER_PASS
```

Execution-status precision: the two endpoint full audits, the affine-path theorem, the row17 child full audit and the new intersection certificate were each executed successfully in component runs, producing the receipts above. The newly consolidated all-in-one packaging source itself did **not** reach its final marker within the shell-limited cold run before this handoff; that is a packaging replay limitation, not an unverified geometry claim. No second independent mechanics implementation is claimed for the new checkpoints.

## 7. Most useful continuation

The fixed-incidence route should now split cleanly:

1. **Gram-cell branch:** search outside the exact `A(t), t in [-1/2,2]` S>=2 corridor. If pursuing an impossibility theorem, finish an exact finite blocker cover rather than treating numerical S2/U2 failure as proof. Any candidate must still be rationally frozen and audited for mixed H and weak000.
2. **C186 geometry branch:** the original one-carrier height certificate hands off rather than separates. Continue from the exact row17 child and attack the new obstruction `{packet 2,9,47; retained 22,40}` with a genuinely coordinated second carrier **normal/support replacement**, not just another local scalar height tweak. Re-run exact packet/complement separation after each topology change. The first success should then add one whole-packet cap and perform the full rebuilt mass/S/U/H/Q audit; conditional complexity remains attractive only if the final maximal complex really reaches E93/C186.

Final acceptance remains exact strict110, additionalweak000, true E<=249. No such body is claimed here.
