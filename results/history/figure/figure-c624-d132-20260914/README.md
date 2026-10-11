# S8 D132: exact alternative at the existing C624 record

The canonical Figure journal at2026-09-14T07:52:56.776Z identifies and author-audits a previously unspecified numerical deletion as `COORD_S8_D132_C624`. Remove **raw-lex vertex132**, not support132, from exact S8 and take the convex hull. The new cut passes through original vertices127,133,136.

Author-reported maximal counts: V176/E312/F138, C624, own-volume-centred strict110/weak000, all mechanical primitive-zero counts0. This has one fewer vertex and one more face than S8, but the same edge complexity: not a record below624. Stable support110 refers to the NEW sorted138-support representation; unstable vertex95. Do not reuse original support labels.

Arithmetic trade-off: common centred denominator44370bits versus44770 for S8, about0.89% smaller; raw coordinates at most440bits, centred coordinates44320bits. The new cut raises support size from216 to485bits. These are exact fraction lengths, not decimal-place or manufacturing tolerance requirements.

The original complete3284-byte `REPLAY_D132.py` is preserved verbatim with SHA256 `f3489d7fc26bc80a6404b43ac0e9d5dee56c152acdc964bab5c8b2f2591df0a7`. It depends on the already preserved30-file S8 capsule at `../figure-c624-s8-20260914/source`; those files were checked byte-for-byte against the pinned decoded capsule, without duplicating them. `journal-entry.md` contains the exact source description and all expected output sizes/hashes.

Exact replay, with the output directory initially absent:

```sh
python3 -B -S REPLAY_D132.py ../figure-c624-s8-20260914/source D132_COLD
```

The author reports two full independent rational auditors, third centred-mass integration and successful source-only cold replay (`COORD_S8_D132_C624_FULL_EXACT_PASS`). The monitor has NOT repeated those mathematical computations; it verified source identity, dependency byte equality, Python syntax and archive readback. See `integrity-receipt.json`. The independently replayed global index is deliberately not changed merely on source integrity or author assertions.
