# C752: independently replayed exact construction

`COORD_H141_C752_D1000000` is the current best locally verified construction in this research.
It is not a proof of the global minimum, an external peer review, or a manufacturing certificate.

| Property | Exact result |
| --- | ---: |
| Vertices | 237 |
| True edges | 376 |
| Maximal facets | 141 |
| Complexity V + E + F - 2 | 752 |
| Strict stable / unstable / saddle equilibria | 1 / 1 / 0 |
| Weak equilibria | 0 / 0 / 0 |
| Zero edge primitives | 0 of 1,504 |

## Definition and reproduction

`source/RAW.json` contains all 141 integer normals and D = 1,000,000. The body is the
uniformly filled intersection I[i] dot x <= D, centred at its exact ordinary-volume
centroid. The centroid is computed, not chosen as an independent parameter.

Definition SHA-256:
`1353da92125392ca69c92fb1c695187a9e98bd8791c8dd3c2eb7c056dbfdeccf`.

Run with Python 3.11 or newer, standard library only, without `-O`:

```sh
python3 verify.py my-fresh-replay
```

The destination must not already exist. The driver authenticates the seven source
files, executes both exact auditors plus additional checks in that fresh directory,
checks all expected output hashes, and writes an explicit acceptance receipt.

Two local fresh-directory replays completed on 2026-09-09 using Python 3.13.14:
67.05 seconds and 67.40 seconds. Both passed; all five output files matched the
author's published hashes and therefore each other byte-for-byte. The auditors use
distinct hull/polygon, mass-integration and equilibrium calculations. This establishes
reproducibility of their exact checks, not an independent formal proof of their code.

## Files

- `source/`: complete exact input and both auditors; no originating ChatGPT sandbox required.
- `source-manifest.json`: exact source hashes and sizes.
- `replay-1/`, `replay-2/`: full evidence, logs and local receipts.
- `geometry-exact.json`: rational raw vertices, maximal faces, true edges and true centroid.
- `model-viewing.obj`: rounded decimal viewing derivative, not an exact certificate.
- `coordinate-complexity.json`: raw and centred rational representation sizes.
- `frontier/`: all 23 decoded continuation files, including separate C760 and numerical
  checkpoints. Preservation does not independently verify these other constructions.
- `COORDINATOR_HANDOFF.md`: original complete report, retained as provenance.

Raw vertex fractions have at most 19-digit denominators; translating to the exact
centroid produces denominators up to 7,079 digits. These are representation metrics,
not physical fabrication tolerances. The compact support definition remains D = 10^6.

Non-record constructions and unsuccessful candidates are separately retained in
`../research-results-2026-09-09/`; they are not discarded when the best construction changes.
