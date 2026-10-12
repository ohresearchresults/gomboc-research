# C746: locally replayed exact construction

COORD_FLOW_H140_C746_D100000000 is a locally verified construction with complexity C=746.
It improves the previously locally verified C752; neither global minimality nor manufacturing robustness is established.

| Property | Exact result |
| --- | ---: |
| Vertices | 235 |
| True edges | 373 |
| Maximal facets | 140 |
| Complexity V + E + F - 2 | 746 |
| Strict stable / unstable / saddle equilibria | 1 / 1 / 0 |
| Weak equilibria | 0 / 0 / 0 |
| Zero edge primitives | 0 of 1,492 |

## Definition and reproduction

source/RAW.json contains all 140 integer normals, D=100,000,000 and scale=1.
The body is the uniformly filled intersection I[i] dot x <= D, translated to its exact ordinary-volume centroid. The centre is computed from the filled solid, not chosen separately.

Definition SHA-256: f5d1d6a9c23cbd89b0d7185971c1d1ac6c384190a50949c4681cbaba2ecf7016.

Run with Python 3.11 or newer, standard library only, without -O:

```sh
python3 verify.py my-fresh-replay
```

The destination must not already exist. The driver authenticates all seven source files, executes both exact auditors and additional controls in a fresh directory, and requires the recorded output hashes and terminal marker. No numerical search, original sandbox or network access is needed.

## Completed local verification

Two separate fresh-directory runs completed on 9 September 2026 with Python 3.13.14 and assertions enabled: 79.26 seconds and 80.31 seconds. They ran in parallel; these times are receipts, not a performance benchmark.

In EACH run both distinct exact implementations reconstructed the maximal geometry, actual volume and centroid, and every strict/weak equilibrium test. Additional full-boundary sublevel and positive-forest checks passed, together with known-body, weak-boundary and invalid-input controls. All five output files matched the author's hashes and the other local run byte-for-byte. Sources were unchanged.

This is reproducibility of two different implementations on this machine, not a third verifier, a formal proof-assistant certificate, or external peer review.

## Package contents

- source/: seven unchanged source/input files.
- verify.py and source-manifest.json: standalone replay driver and input pins.
- geometry-exact.json: rational raw vertices, maximal faces, true edges and true centroid.
- model-viewing.obj: rounded decimal viewing derivative ONLY, not an exact certificate or print-ready guarantee.
- coordinate-complexity.json: raw and centred rational representation metrics.
- replay-1/ and replay-2/: full exact outputs, logs and local acceptance receipts.
- COORDINATOR_HANDOFF.md, capsule-original.json and source-map.json: preserved source provenance.
- GOMBOC_C746_SOURCE_AND_MODEL.zip: portable source, model and reproduction instructions.
- GOMBOC_C746_FULL_VERIFICATION.zip: the two complete local verification records.

The source/model archive contains no search-run journal. The verification archive contains the computational verification logs, not the research conversation history. Both archives have per-file manifests and are read back and SHA-256 verified after creation.

## Coordinate arithmetic and scope

There are 705 scalar raw coordinates; 702 are nonintegers. Reduced raw numerators and denominators have at most 25 digits. After exact centroid translation, all 705 are nonintegers and maximum numerator/denominator length is 9,790 digits. These are representation sizes, not fabrication tolerances.

The full C752 package and all earlier results remain preserved. This C746 package reconstructs and verifies the resulting figure; it is not the complete numerical discovery engine.
