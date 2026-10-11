# NH72 finite two-cap compensation: exact nonwinners and conditional obstructions

Immutable worker result `asg_YU5aQXYA4IST22PaStBZEp3-`, received 2026-09-14T09:31:50.878Z. The complete 23-file standalone reconstruction/proof/search package is under `source/`. Original result JSON, Markdown, decoder, all source hashes and literal inputs are preserved.

- PAIR99: V173/E309/F138, C618, strict equilibria 9/2/9, weak000.
- TRIPLE117: V172/E308/F138, C616, strict equilibria 10/3/11, weak000.

Each has a separately defined rational proxy and an isolated-root algebraic version. The author reports exact finite restoration of the original deletion-body centroid for the algebraic endpoints, not just a nonsingular infinitesimal Jacobian. The rational proxies instead have their own exactly computed centroids very close to that target. Neither construction is a Gömböc. The accepted record remains C624.

The author also supplies frozen-support-cone certificates: under the specified unchanged supporting cones and actual centroid boxes, compatible cap changes retain at least two or three unstable equilibria. Nine separate conditional compensated-slide covers are included. These are scoped obstructions, not a global minimum or exclusion of changed critical cones/metrics/incidence. A continuous successful compensation path is not certified.

Rational proxy common centred denominators have 54,492 and 54,179 bits. These fraction-size figures must not be assigned to the algebraic coordinates; their minimal coordinate polynomials were not computed.

Exact replay uses Python's standard library with assertions enabled, from this package directory and with a new output directory:

```sh
python3 -B -S source/REPLAY.py --out replay-output
```

The original `source/README.md` documents the staged replay and optional numerical searches. Expected cold marker: `NH72_TWO_FINITE_CAP_COMPENSATORS_ROOTS_AND_RATIONAL_AUDITS_COLD_PASS`.

The monitor verified transport/source hashes, all 22 manifest entries, JSON/Python syntax and archive readback. **It did not repeat the mathematical computations.** Author-reported independent A/B hull/mechanics enumeration applies to the rational proxies; the algebraic endpoints have a separate interval proof, not two independently enumerated algebraic hulls.

Parent provenance clarification: the reported parent digest mismatch is explained by serialization boundaries. Locally verified `c00d…` hashes the 73,144-byte immutable version-2 JSON, while `0e08…` hashes its exact 72,505-byte `result_markdown` value. Both match the existing parent package byte-for-byte. The worker's original warning and `PROVENANCE.json` are retained unchanged.
