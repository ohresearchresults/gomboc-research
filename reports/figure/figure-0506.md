# figure-0506

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quiet Quartz 41 — closeout with no new polyhedron

## Result and execution boundary

**No new strict110/additionalweak000 body was obtained. No changed exact endpoint, completed geometry-optimization campaign, or new geometric exclusion is claimed.** This execution did not achieve the requested substantive finite-geometric advance. The scientific continuation remains open.

The preceding assistant turn ended with `Thinking failed`. At closeout, the active `/mnt/data` directory contained only the supplied journal, with no post-parent body, numerical checkpoint, trial ledger, or proof artifact. Consequently, the elapsed time before `finish` cannot be counted as completed research or unsuccessful trials. I did not recover evidence permitting any such claim.

During closeout I read the supplied journal and literal parent, decoded and read all seventeen supplied source/input units, checked source integrity and the correspondence of the printed C120/C222 inputs, and computed a small exact **current-carrier map** for C120. That map is a continuation aid, not a changed construction, fresh mass/mechanics audit, or exclusion theorem. Its complete runnable recovery is below.

## Source authority and integrity

The construction authority remains **figure-0496**, advertised SHA-256 `cb70d6ffe26a61c3c58741ee3b706dcffc73f31be5b9ec4f19e7f29513befc8d`. The supplied literal payload contains the seventeen-unit recovery capsule and exact rational inputs; no additional archive dependency was needed to read them.

Observed local transport identities:

- Uploaded journal: **344980 bytes**, SHA-256 `a5b3bb981eb79d118ddc222d90e4514c7ab35ac963f221d215fe0f2ee3e807b0`.
- Decoded canonical source dictionary: **43708 bytes**, **17 entries**, SHA-256 `29f8e68ec2e1d70fc4a63de644c48f492b87d45f96c66ef8b3fc686555435af0`, matching the literal capsule assertion.
- Supplied numerical checkpoint: **1313 bytes**, SHA-256 `06c32e0b8ecefd7ef81e01c89078ed0ceec83b71982ef917271ca648beb485d4`.
- The printed 22 C120 halfspaces exactly match decoded `S1_C120_G1000_rows.json`; the printed 40 C222 integer points exactly match decoded `S1_VGRID_D10000_input.json`.

**Outer-digest limitation:** the local UTF-8 substring beginning at `# QH83 — exact whole-packet access, a smaller S1 companion, and a complete cap-chart obstruction` and continuing through the journal's EOF is 38600 bytes, SHA-256 `5dc7b8db44a36dbb6358012142cce047c43b36f2c4af9ac007da9d9c9eeece6e`, not the advertised immutable-result digest. Adding one or two terminal newlines does not produce the advertised digest. The pack does not establish the serialization responsible for that difference. I therefore do not claim an outer-payload hash match, invent a replacement parent identity, or infer a geometric contradiction. The inner seventeen-source dictionary does match exactly.

The parent's fifteen expected output receipts were **not** mechanically replayed during this closeout. Copying their manifest is not another verification of those outputs.

## Preserved scientific starting points

These are **inherited results**, not newly computed bodies:

| Exact entrance | V/E/F; C | Strict S/U/H | Complete residual landscape | Final edge headroom |
|---|---:|---:|---|---:|
| S1_C120_G1000 | 40/60/22; 120 | 1/2/1 | One P component/cut 18/16; Q empty | 189 |
| S1_VGRID_D10000 | 39/111/74; 222 | 1/2/1 | One P component/cut 17/35; Q empty | 138 |
| QH83_CAPBOOST5 | 72/108/38; 216 | 8/7/13 | Six positive P bars and seven positive Q bars | 141 |

All three have inherited additionalweak000 and primitivezero000. C222's 56-bit common centred denominator remains a distinct arithmetic advantage; CAPBOOST5 remains a thicker, lower-P-energy but multi-basin alternative. These merits do not establish proximity to cancellation.

The supplied cap obstruction remains precisely bounded: unchanged original C144 supports, cap normal `(-22,-24,-6)`, the complete specified offset interval, and the entrywise Gram box of radius `1/16`. It does **not** exclude joint support/normal/material changes in C120, C222, or CAPBOOST5. The parent's cap already demonstrates why deleting every old packet vertex is insufficient: its surviving physical component contains both new cap vertices and formerly retained vertices.

## Exact current-carrier diagnostic

I derived the following directly from the parent's **complete C120 maximal face cycles**, without borrowing C144 labels. Those literal cycles and the complete 16-edge cut are the input authority.

For **S1_C120_G1000**, with face numbers equal to the displayed 22-row support order:

- Physical death edge **3–18** has owners **0 and 1**.
- Younger unstable vertex **4** has owners **2, 7, 19**.
- Elder unstable vertex **39** has owners **11, 14, 19**.
- The sole stable facet is **14**, cycle `[1,33,36,39,5,2]`. It intersects the dying packet at vertices `[1,2,5]` and its complement at `[33,36,39]`.
- The packet has **18 vertices, 19 internal edges, 16 boundary edges**, and internal cycle rank **2**. The only wholly internal facets are **2 and 7**. The wholly external facets are **6, 9, 11, 12**; all other sixteen facets cross the packet boundary.

This identifies a real coupling: facet14 crosses the full packet boundary and contains elder39, while facet19 is incident to both unstable vertices. The original C144 pairs `8/14` and `5/23` are not a substitute for this map.

A possible initial block for a future **joint** deformation is `{0,1,2,7,11,14,19}`, spanning the current death interface, both root stars and the sole stable carrier. This is only a proposed experimental choice: it is neither a sufficient cancellation mechanism nor a restriction on which supports may move. Acceptance must still follow the entire evolving P/Q landscape at the actual filled-volume centroid, including root transfers outside this initial block.

### Complete runnable recovery of the diagnostic

Save the following exactly as `QQ41_C120_INTERFACE.py` and run:

```sh
python -B -S QQ41_C120_INTERFACE.py
```

Executed environment: **CPython 3.13.5**, standard library only, assertions enabled. The source is **3064 bytes**, SHA-256 `a422120e977877075b2c2172eb139602e50d780cfa2e3359001797e01d418195`.

```python
"""Exact combinatorial handoff aid; NOT a hull, mass, or mechanics audit.
Input: literal C120 maximal cycles in figure-0496.
Python standard library only; run with assertions enabled.
"""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

CYCLES = [[3,8,9,10,16,19,18],[0,3,18,20,23,21,12],[0,1,2,4,6,7,8,3],[16,22,24,19],[14,27,32],[10,11,13,15,17,25,22,16],[21,23,36,33,32,27],[2,5,4],[12,21,27,14],[18,19,24,26,20],[0,12,14,32,33,1],[20,26,37,38,39,36,23],[22,25,28,29,30,31,34,35,37,26,24],[17,28,25],[1,33,36,39,5,2],[15,29,28,17],[13,30,29,15],[11,31,30,13],[9,34,31,11,10],[4,5,39,38,6],[7,35,34,9,8],[6,38,37,35,7]]
CUT = [[1,33],[3,18],[5,39],[6,38],[7,35],[9,34],[11,31],[12,21],[13,30],[14,27],[14,32],[15,29],[16,19],[16,22],[17,25],[17,28]]

def main():
    owners = defaultdict(list)
    for f, cy in enumerate(CYCLES):
        for i, j in zip(cy, cy[1:] + cy[:1]):
            owners[tuple(sorted((i, j)))].append(f)
    vertices = set().union(*map(set, CYCLES))
    assert vertices == set(range(40))
    assert len(owners) == 60 and len(CYCLES) == 22
    assert all(len(v) == 2 for v in owners.values())
    assert all(sum(i in edge for edge in owners) == 3 for i in vertices)
    X = set(range(18))
    cut = sorted([list(e) for e in owners if (e[0] in X) != (e[1] in X)])
    assert cut == CUT
    internal = sorted([list(e) for e in owners if set(e) <= X])
    seen, todo = {0}, [0]
    while todo:
        u = todo.pop()
        for i, j in internal:
            if u in (i, j):
                v = j if u == i else i
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
    assert seen == X
    rank = len(internal) - len(X) + 1
    assert rank == 2
    incident = lambda i: [f for f, cy in enumerate(CYCLES) if i in cy]
    report = dict(
        body='S1_C120_G1000',
        parent='figure-0496',
        declared_parent_sha256='cb70d6ffe26a61c3c58741ee3b706dcffc73f31be5b9ec4f19e7f29513befc8d',
        verified_parent_dictionary_sha256='29f8e68ec2e1d70fc4a63de644c48f492b87d45f96c66ef8b3fc686555435af0',
        V_E_F=[40,60,22], packet=sorted(X), internal_edges=internal,
        cycle_rank=rank,
        cut_edge_owners=[[i,j,owners[(i,j)]] for i,j in cut],
        death_edge_owners=owners[(3,18)],
        younger_U4_owners=incident(4), elder_U39_owners=incident(39),
        stable_face14_cycle=CYCLES[14],
        inside_facets=[f for f,cy in enumerate(CYCLES) if set(cy)<=X],
        outside_facets=[f for f,cy in enumerate(CYCLES) if not set(cy)&X],
        interface_facets=[f for f,cy in enumerate(CYCLES) if set(cy)&X and set(cy)-X],
        status='Combinatorial derivation from supplied parent; no changed body or fresh mass/mechanics certificate.')
    data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
    Path('QQ41_C120_INTERFACE.json').write_bytes(data)
    print('QQ41_C120_LITERAL_INTERFACE_MAP_PASS',len(data),hashlib.sha256(data).hexdigest())

if __name__ == '__main__':
    main()
```

Observed terminal marker:

```text
QQ41_C120_LITERAL_INTERFACE_MAP_PASS 2842 939d7cc8b541d493f366cd01d7ded2a8321beb5a003f1f765e8c082c30b7e65a
```

The resulting **2842-byte** JSON includes every cut edge with both owners, every internal packet edge, all facet partitions and the root-carrier data. It is not a partial interface selected by a numerical threshold.

## Continuation and evidence still required

The most useful continuation remains genuine finite material redistribution from the exact C120 or C222 entrance, or whole-landscape reconsolidation from CAPBOOST5—not another unchanged recovery or fixed-C144 cap-offset scan. The current-carrier map removes an indexing ambiguity but does not solve the mass-coupled cancellation problem.

There is no new endpoint here for which to provide a new volume/centroid certificate, maximal hull, strict/additional-weak/mixed-edge census, or complete post-deformation P/Q barcode. Those acceptance requirements remain outstanding. No unsuccessful finite search, stationarity conclusion, or exclusion of a larger family follows from this interrupted execution.

For a fresh executor, retain the complete literal MFW parent as the construction dependency. The diagnostic above is independently reconstructible, but intentionally does not replace the parent's geometry generator and full auditor.

Supplementary convenience copy: the seventeen unchanged supplied source/input units and the new interface diagnostic (`QQ41_closeout_sources.zip`). The archive contains no claimed new polyhedron or newly replayed fifteen-report audit set.
