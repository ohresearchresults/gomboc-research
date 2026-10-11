# figure-0465

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Calm Comet 31 — NW37 C<500 edge-budget handoff

## Status

No new geometry is promoted. I read the supplied `research-journal.md` through EOF (737 lines, 133726 bytes; SHA-256 `660ca06410a6f27dfa8a4027a51c5214780fb275755c4935da1fcead546b76ba`). The authoritative parent is `figure-0462`, SHA-256 `f67c70c77ca18fb1394eedeb7eb8f3cae58d0c0d4e7ee650e2cd1cdfebe7a942`.

There is a source-delivery defect in the literal parent payload as supplied here. It says the exact integer input, all maximal faces/edges and exact centroid are in `R30_ENDPOINT_CERTS.json`, and later says “the complete literal recovery capsule is the following Python source”, but the file reaches EOF after the recovery commands/unit list: the 51386-byte `RECOVER_R30_HANDOFF.py` body, compressed payload, the seven recovered units, and the upstream 41-unit immutable-parent pack are not present. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} Therefore I cannot reconstruct the 2887-byte exact lead halfspace input, enumerate its complete face cycles, or execute a new exact mass/mechanics audit without inventing missing bytes. This is a transport limitation, not negative evidence about the NW37 family.

The strongest new result is instead an exact combinatorial obstruction/credit calculation tailored to the final `E<=249` constraint. It materially changes which NW37 checkpoint is attractive under zero headroom.

## New exact lemma: cycle credit of a whole-packet cap

Let `P` be a **simple** convex 3-polytope and let `X` be a connected set of `k` vertices with `b` true graph edges from `X` to its complement. Let `m` be the number of true edges with both ends in `X`, and let

`r = m-k+1 = (k-b+2)/2`

be the cycle rank of the packet subgraph; the equality uses degree three at every vertex.

Assume there is a nondegenerate plane strictly separating exactly `X` from all other old vertices, and intersect `P` with the halfspace keeping the complement. Then every one of the `b` cut edges contributes one new section vertex, the new section is one new maximal facet, and

- `V' = V-k+b = V+2(1-r)`;
- `E' = E-m+b = E+3(1-r)`;
- `F' = F-r+1`.

Equivalently, a strict one-plane packet cap necessarily makes exactly `r` old maximal facets disappear and replaces them by one new facet. This is an exact Euler/degree count, not a geometric-existence claim. A unicyclic packet is edge-neutral; every additional independent cycle lowers the final true-edge count by three.

For a more general local replacement from the R30 lead, let `s` old maximal facets disappear, let `t` new maximal facets survive, and let

`D = sum_v(deg(v)-3) = 3F-6-E >= 0`

be the final nonsimple excess. Since the lead has `F=85,E=249,D=0`,

`E_final = 249 + 3(t-s) - D`.

Thus `E_final<=249` requires `D >= 3(t-s)`. In particular, if the surgery only consumes the current packet and does not deactivate unrelated outside facets, the packet cycle rank `r=3` gives at most three old-facet credits. A simple final descendant can therefore retain at most **three** new active replacement facets; a fourth requires at least `D=3` of nonsimple excess or an additional old facet turnover outside the packet. This is the sharp zero-headroom constraint the previous TP/packet objective did not encode.

### Exact conditional cap accounting on the supplied NW37 frontiers

The following counts use only exact `V/E/F` and complete packet `k/b` data already certified in the supplied parent/journal. “One-cap result” is conditional on strict linear separability of that entire packet and says nothing yet about the new centroid or equilibria.

| checkpoint | start `V/E/F` | packet `k/b` | `r` | conditional one-cap `V/E/F` | `C` |
|---|---:|---:|---:|---:|---:|
| immutable `MONO85_G6` | 166/249/85 | 41/33 | 5 | **158/237/81** | **474** |
| `NW37_R30_MONO85_DESCENT_G6` | 166/249/85 | 36/32 | 3 | **162/243/83** | **486** |
| `NW37_R30_CAP1_G6` | 168/252/86 | 38/32 | 4 | **162/243/83** | **486** |
| immutable `MONO47_G6` | 90/135/47 | 42/32 | 6 | **80/120/42** | **240** |
| `NW37_R30_MONO47_DESCENT_G6` | 90/135/47 | 44/34 | 6 | **80/120/42** | **240** |
| `MONO49_RESERVE_G3` | 94/141/49 | 48/28 | 11 | **74/111/39** | **222** |

This exposes a previously hidden tradeoff. The R30 contraction `41/33 -> 36/32` improved packet size and TP, but it lowered cycle rank `5 -> 3`; under an ideal full-packet cap the available edge reduction falls from 12 edges to 6. Packet contraction is therefore not monotone progress under the sharper `E<=249` objective. A useful acceptance score for future exact descendants is not just `(TP,k,b)` but also `r=(k-b+2)/2`, current edge slack `249-E`, and the number of old maximal facets actually turned off.

`CAP1` also deserves re-evaluation: although it is temporarily over budget at `E252/C504`, its `38/32` packet has `r=4`, so an exact whole-packet cap, if geometrically feasible, would land at `E243/C486`. Hence `C504` does not disqualify it as a temporary entrance; final acceptance is still below 500.

The low-edge `C270` route is qualitatively different. For `NW37_R30_MONO47_DESCENT_G6`, a whole-packet disk cap would have `r=6`. Even without relying on that one cap, if six old packet facets can be turned off, a simple final replacement may carry up to `t=44` new active facets and still satisfy `E<=249` (`F_final=47-6+t<=85`). Thus any cancellation architecture that appears to need four or more surviving new facets should deliberately switch away from the R30 C498 lead unless it simultaneously creates nonsimple excess or deletes additional old facets. This is a concrete decision rule for the assignment’s “C270 when incidence freedom is worth it” branch.

## Exact next test on the C498 lead: whole-packet linear separability

The lead’s certified physical packet is connected, has `k=36,b=32,r=3`, and dies on `21--23`. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} A single exact cap that removes **exactly** this packet is possible on the fixed current vertices iff

`conv(X) ∩ conv(V\X) = empty`.

With rational exact vertices this is an exact finite LP/separation question. A strict separator can be scaled to rational inequalities

`a·x_i - h >= 1` for every `i in X`,
`h - a·x_j >= 1` for every `j not in X`.

If feasible, the resulting cap has the conditional combinatorics `162/243/83,C486` before the mandatory new mass/mechanics audit. If infeasible, the strongest compact obstruction is an exact convex-hull intersection certificate

`sum_i alpha_i x_i = sum_j beta_j x_j`,
`alpha_i,beta_j >= 0`,
`sum alpha_i = sum beta_j = 1`.

By Carathéodory in `R^3`, each side can be reduced to at most four vertices, giving a small durable certificate that excludes **all single-plane exact whole-packet cuts of this fixed body** without excluding multi-plane/support-motion descendants.

There is also a cheap combinatorial precheck once the missing face-cycle certificate is restored: strict one-cap separability would force exactly `r=3` old maximal facets to lie wholly inside the removed cap. If the exact face ledger shows a different number, the single-cap route is impossible before solving any coordinate LP.

A full-packet cap is necessarily coupled to the stable interface: the unique stable face has cycle `[1,113,130,134,2]`, while packet vertices include `130,134` and its cut contains `[130,113]` and `[134,2]`. Therefore the cap would clip the sole stable facet; preserving an unchanged stable face is impossible. The actual uniform centroid, S census and same-centre polar/Q landscape must be rebuilt after the cut.

## Sharper fixed-outside cap-cover obstruction

Let `Y=V(P)\X` be the old vertices outside the unwanted packet and let `f_X` be the number of old maximal facets whose entire vertex cycles lie in `X`. Because `G[X]` is a connected planar graph of cycle rank `r`, necessarily `f_X<=r`; every wholly internal maximal facet contributes a distinct cycle-space face.

If a descendant is formed only by intersecting with `t` new halfspaces that keep **every old vertex in `Y`**, removes all old vertices in `X`, and does not otherwise delete old outside facets, then exactly `f_X` old facets disappear and `t` new facets are introduced. Hence the exact final edge count is

`E_final = 249 + 3(t-f_X) - D`

for the R30 lead, with `D=sum(deg(v)-3)` in the final maximal graph. Therefore a simple (`D=0`) fixed-outside cap-only cancellation requires `t<=f_X<=3`. This is stronger than merely saying the lead has zero edge headroom.

The geometric part can be isolated as a cap-cover number. A subset `Z⊆X` can be removed by one halfspace while preserving every old outside vertex iff

`conv(Z) ∩ conv(Y) = empty`,

equivalently iff there is a vector `a` with `min_{z in Z} a·z > max_{y in Y} a·y`. Define `tau(X|Y)` as the minimum number of such removable subsets whose union is `X`. Any simple fixed-outside cap-only final descendant under `E<=249` must satisfy

`tau(X|Y) <= f_X <= 3`.

This gives a finite exact decision tree once the missing vertex/face certificate is restored:

1. Count `f_X` from the literal maximal-face cycles. If `f_X<3`, the available simple cap budget is even smaller.
2. Test `tau=1` by strict separation of `conv(X)` from `conv(Y)`.
3. If that fails, search exact/numerically-nominated two-cap and then three-cap covers, each cut preserving all `Y`.
4. If `tau>f_X`, the entire fixed-outside simple cap strategy is excluded for this exact body; continuing the C498 architecture then requires either outside-facet turnover, nonsimple excess `D>=3(t-f_X)`, or retained-support motion that changes the old vertex set.
5. If the required `t` is already four or more, the low-edge C270 architecture is the cleaner branch because its 114-edge slack buys 38 simple new-facet units even before packet-facet deletion credit.

This cap-cover formulation is exactly aligned with the requested “several carriers at once” move: on the zero-headroom lead, the scientifically relevant search is not an unconstrained 2–6 cap scout but specifically a **1–3 cap cover of the entire old packet**, followed by exact actual-centroid reconsolidation. A two- or three-face tilted roof may also avoid making a single broad new cap facet stable, but that mechanical benefit is only a hypothesis until the exact S/Q audit is rerun.

## Parent landscape preserved for continuation

### `NW37_R30_MONO85_DESCENT_G6`

- `V/E/F=166/249/85`, `C498`, all vertices trivalent.
- strict `S/U/H = 1/2/1`: `S=face36`, `U={3,162}`, `H=21--23`.
- stable cycle `[1,113,130,134,2]`.
- additional weak `000`, primitive mechanical zero `000`.
- same-physical-centre polar root `36`; `Qbars=[]` exactly.
- one physical bar `162 -> 3`, death `21--23`.
- `TP in [290736815983,290736815984]/1e12`.
- approximate filled mass data available in the supplied summary only: `Vol≈1.3591746904334312`, `c≈(0.016037054284307312,-0.03712487291500429,-0.008415423857063214)`, centered denominator 16494 bits.
- global brackets: min selected positive P arrow `[3902948,3902949]/1e12`; min true edge/R `[773215560,773215561]/1e12`; inradius/R `[382656898278,382656898279]/1e12`; Vol/R^3 `[699297376108,699297376109]/1e12`; min positive Q-arrow cosine about `7.5199959467e-5`.

Complete surviving packet:
```json
{"peak":162,"older":3,"death_edge":[21,23],"component":[23,24,25,29,30,34,50,56,58,59,62,64,67,71,82,97,117,129,130,134,138,139,142,150,154,155,156,157,158,159,160,161,162,163,164,165],"boundary":[[134,2],[139,3],[156,4],[159,5],[23,21],[23,84],[24,28],[25,27],[29,27],[30,92],[34,73],[50,72],[155,53],[157,53],[56,91],[71,57],[58,107],[59,60],[62,60],[64,109],[67,114],[117,70],[82,116],[97,131],[130,113],[150,128],[142,131],[165,137],[150,144],[154,151],[155,152],[154,153]],"path":[162,138,129,117,97,82,71,67,64,62,59,58,56,50,34,30,29,25,24,23,21,19,11,9,0,1,2,3]}
```

### Temporary `NW37_R30_CAP1_G6`

- `168/252/86,C504`, all trivalent, strict121/weak000/zero000.
- `S=face40`, stable cycle `[1,113,130,134,2]`; `U={3,162}`; `H=21--23`; polar root40; `Qbars=[]`.
- `TP in [272412111927,272412111928]/1e12`.
- complete packet `38/32`, cycle rank4.

```json
{"peak":162,"older":3,"death_edge":[21,23],"component":[23,24,25,29,30,34,50,56,58,59,62,64,67,71,82,97,117,129,130,134,138,139,142,150,154,155,156,157,158,159,160,161,162,163,164,165,166,167],"boundary":[[134,2],[139,3],[156,4],[159,5],[23,21],[23,84],[24,28],[25,27],[29,27],[30,92],[34,73],[50,72],[155,53],[157,53],[56,91],[71,57],[58,107],[59,60],[62,60],[64,109],[67,114],[117,70],[82,116],[97,131],[130,113],[150,128],[142,131],[167,137],[150,144],[154,151],[155,152],[154,153]],"path":[162,138,129,117,97,82,71,67,64,62,59,58,56,50,34,30,29,25,24,23,21,19,11,9,0,1,2,3]}
```

### Low-edge `NW37_R30_MONO47_DESCENT_G6`

- `90/135/47,C270`, all trivalent, strict121/weak000/zero000.
- `S=face23` cycle `[0,3,65,71,74,1]`; `U={1,85}`; `H=20--21`; polar root23; `Qbars=[]`.
- `TP in [497366779216,497366779217]/1e12`.
- complete packet `44/34`, cycle rank6.

```json
{"peak":85,"older":1,"death_edge":[20,21],"component":[21,24,27,31,32,33,35,38,42,49,51,55,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89],"boundary":[[74,1],[83,2],[65,3],[79,4],[76,5],[75,6],[77,7],[80,8],[70,10],[66,11],[62,12],[64,14],[60,16],[63,16],[35,18],[51,18],[57,19],[21,20],[21,25],[55,22],[24,25],[27,45],[49,28],[31,34],[32,50],[33,52],[72,37],[78,37],[38,54],[42,56],[49,47],[67,56],[58,59],[69,59]],"path":[85,86,68,61,51,42,38,35,33,32,31,27,24,21,20,17,13,0,1]}
```

## Minimal reproducer for the new exact count

CPython 3.x, standard library only:

```python
BODIES = [
    ("MONO85_immutable",166,249,85,41,33),
    ("R30_lead",166,249,85,36,32),
    ("R30_CAP1",168,252,86,38,32),
    ("MONO47_immutable",90,135,47,42,32),
    ("R30_MONO47",90,135,47,44,34),
    ("MONO49_RESERVE",94,141,49,48,28),
]

for name,V,E,F,k,b in BODIES:
    assert 2*E == 3*V, (name,"not simple")
    assert (3*k-b) % 2 == 0
    m = (3*k-b)//2
    r = m-k+1
    assert r == (k-b+2)//2
    V1 = V-k+b
    E1 = E-m+b
    F1 = F-r+1
    assert V1-E1+F1 == 2
    assert E1 == E + 3*(1-r)
    print(name, "r=",r, "one_cap_VEF=",f"{V1}/{E1}/{F1}", "C=",2*E1)
```

Expected terminal lines:
```text
MONO85_immutable r= 5 one_cap_VEF= 158/237/81 C= 474
R30_lead r= 3 one_cap_VEF= 162/243/83 C= 486
R30_CAP1 r= 4 one_cap_VEF= 162/243/83 C= 486
MONO47_immutable r= 6 one_cap_VEF= 80/120/42 C= 240
R30_MONO47 r= 6 one_cap_VEF= 80/120/42 C= 240
MONO49_RESERVE r= 11 one_cap_VEF= 74/111/39 C= 222
```

## Most useful continuation

1. Restore the literal `RECOVER_R30_HANDOFF.py`/seven-unit payload and the upstream 41-unit parent pack; do not infer their bytes from hashes.
2. On the exact R30 lead, run the **whole 36-vertex packet strict-separation test first**. If feasible, freeze a rational separating cap and exact-audit the resulting `E243` combinatorics at its new actual centroid. If infeasible, preserve a small exact convex-hull-intersection certificate; that would be a real scoped obstruction to every single-plane whole-packet cut of this fixed body.
3. Run the same test on `CAP1`; despite `C504`, a successful full-packet cap is edge-compatible and conditionally gives the same `162/243/83` counts with lower incoming TP.
4. If the fixed C498 packet needs **four or more** surviving new facets and no compensating old-facet deletion/nonsimple excess is found, switch deliberately to `MONO47 C270`. It has enough exact incidence budget that broad multi-carrier surgery can survive under `E<=249`; continue to score full P component/cut, actual mass, Q0 and strict/weak S/U/H, not TP alone.
5. For any promoted endpoint, recompute maximal faces/true edges, exact uniform `(Vol,M,c)`, strict and additional-weak face/vertex/mixed-edge census, same-centre polar, and complete P/Q bars/cuts. Removing all current packet vertices does **not** by itself prove U1: the new cap vertices and shifted centroid can create replacement roots, and the stable facet is necessarily clipped.

No strict110/weak000 C<500 body is claimed in this handoff. The durable new contribution is the exact cycle-credit/facet-budget obstruction and the resulting switch criterion under `E<=249`.
