# C634 — recovered and locally replayed

Homogeneous convex polyhedron: **182 vertices, 317 edges, 137 maximal facets**;
mechanical complexity C=2E=634. Exact equilibrium counts (S,U,H)=(1,1,0)
relative to the body's own volume centroid; weak counts (0,0,0).

## Local verification, 10 September 2026

The original 18,954,073-byte archive and 101,865-byte Markdown were downloaded
from the original Steady Comet71 chat. Their SHA-256 values matched those in
the original night-time answer. The full 66,825-character base85/LZMA capsule
decoded into 55 source files and a 244,108-byte source map with the expected hash.

A fresh source-only replay of **C634_SOC** completed locally. Both supplied exact
auditors agreed and all six frozen output hashes matched. The local transcript is
[SOURCE_REPLAY.log](source-only/C634_SOC/SOURCE_REPLAY.log).

The two checkers are the author's two implementations, executed locally—not two
new independent reviews. Other constructions, symbolic interval proofs, full
moment/rotation suites and non-winning candidates are preserved but were not
all rerun in this recovery. Global minimality and manufacturing robustness are not proved.

## Files

- [Original full archive](STEADY_COMET71_C634_FULL.zip), including non-winning candidates and methods.
- [Complete author report and recovery capsule](RESULT_MARKDOWN.md).
- [Exact generator](source-only/C634_SOC/GENERATOR.json).
- [Local summary](source-only/C634_SOC/SUMMARY.json).
- `source-only/`: independently decoded 55-file source capsule, plus the local C634 replay outputs.
- `archive-content/`: preserved original archive contents; historical `input/research-journal.md` is not the live journal.

Source-map SHA-256: `3f2b6d1d75d20d80a1a9991b3ec8a69fa3b934b0d4e82f9751b333490ee3fbd3`.
Generator SHA-256: `09b77674fbf9877abcf35f5932d4d96fad25c855da1fefbcf1d71e7bd6d297c6`.
Matching A/B output SHA-256: `0f0c4e0d4213910d3214f8f367185909f0b6e744c9cb983e2c42c1fb60925925`.

Replay only the main C634 construction from `source-only/`:

```sh
python3 -u -c 'import CORE_REPLAY_ALL as replay; replay.one("C634_SOC")'
```

Keep the full archive private until reviewed for publication: it includes the
historical research journal and work logs, not just the publishable figure.
