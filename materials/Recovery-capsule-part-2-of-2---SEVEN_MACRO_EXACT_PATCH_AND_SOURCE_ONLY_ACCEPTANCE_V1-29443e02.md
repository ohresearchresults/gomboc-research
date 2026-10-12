# material-29443e02c382

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Required exact recovery patch and source-only acceptance

Object: PARALLEL_CORNER_SEVEN_MACROSCOPIC_DOMAIN_V1.
Recovery capsule part1of2 is [internal-source-reference], SHA f39d8b9eda38cf17fbd9a05374b92eae59d66c7fda300a04617bbc1078c4078a. This material is part2of2. BOTH materials are required for exact computational recovery. Part1 contains the full theorem, geometry, complete two-source units and commands, but its transported core source has one excess closing square bracket in choose_split. Its unpatched core must NOT be described as the executed source.

Save the core block as parallel_corner_seven.py and the wrapper block as dominant_cap.py, with LF newlines and one final newline. Run the following complete exact patch BEFORE any geometry/build/check command:

```python
from pathlib import Path
import hashlib
p=Path('parallel_corner_seven.py')
b=p.read_bytes()
bad=b'pairs.append((k,MI[tuple(beta)]]))'
good=b'pairs.append((k,MI[tuple(beta)]))'
assert len(b)==13650
assert hashlib.sha256(b).hexdigest()=='daffeeb08c527474b3b308ad1e84aa4070360a26c1ae69a2d75ea2886e0feedd'
assert b.count(bad)==1
b=b.replace(bad,good)
assert len(b)==13649
assert hashlib.sha256(b).hexdigest()=='1af55b4dfef26eb8df231859b98cfedb027b62c53419caf3b3ccbc92280ec404'
p.write_bytes(b)
q=Path('dominant_cap.py').read_bytes()
assert len(q)==2149
assert hashlib.sha256(q).hexdigest()=='0b0e85f3574b6481117e65db3ad6be2bdde798ece1b31b3601255076bd2fddb9'
print('SEVEN_MACRO_TESTED_SOURCE_RECOVERED')
```

The patch was tested on the one-character-corrupted source and its output compared byte-for-byte with the actually executed source, PASS. These complete input hashes prevent any other undetected difference from being treated as the tested source. No code helper or parameter is omitted.

The fresh directory containing ONLY the two tested source files has now completed the full build and final exact replay. Its certificate and report are byte-identical to the normal build and separate check:

    dominant_narrow.json 320915 bytes
    SHA256 8a03e8622798623f939fbc7b7e5800148ffecfd775415504e2f2b480ec772c0f
    dominant_narrow.report.json 1175 bytes
    SHA256 13a07f1c5da43891c2d8f4ac148621b1c8d28f230ac96545e33d55a82e8459ad

The source-only run terminal marker is DOMINANT_CAP_NARROW_ALLROOT_EXACT_PASS. It independently reconstructs3390 integer stresses,23 nodes,12 leaves,11729 stress-cell uses,45039360 exact positive matrices,52780 roots and no unresolved nodes, retaining gap2^-24. This resolves the pending cold-execution statement in part1. It is exact integer/rational computational acceptance, not proof-assistant certification.

Use the exact reconstruction/check commands and dependency versions in part1. No earlier code, certificate or sandbox path is needed. The complete proof domain remains lambda2>=lambda0+lambda1, all strict simplex coordinates, |q| in[1/2,1), all a,b in(0,1), c in(0,1/2], with its genuine actual centroid. The whole seven-chart and full E17 incidence remain open.

Editorial correction to part1's negative-method paragraph: remove the stray fragment 'Its614? count is not needed as evidence'. The actual first full-domain partial run had3932 stresses,41 nodes,12 completed leaves,16106 uses and61847040 exact PD matrices; unresolved nodes32through40. It was explicitly PARTIAL_EXACT_CHECK_ONLY, not a whole-domain theorem or a physical survivor. These partial counts do not enter the new complete regional proof.
