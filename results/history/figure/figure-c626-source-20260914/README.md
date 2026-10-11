# C626 source preservation — 2026-09-14

The Figure coordinator accepted two C626 constructions, G8 and G14, in canonical journal event 1137 (01:00:36 UTC). It reported V=178, E=313, F=137, strict equilibria (1,1,0), no weak-only equilibria, two full exact audits and a third centred mass integration.

Local preservation verified the literal capsule hash and decoded JSON hash, every source-manifest entry, all three search-method source hashes, Python syntax, and byte-identical file readback. This is **source integrity verification, not an independent local mathematical replay or a global minimum proof**. The previously independently replayed `latest-reproducible-gomboc/CURRENT.json` has therefore not been changed.

- `exact/`: both exact generators, the complete reconstruction, A/B auditors, third mass integration, expected results and replay driver; no external parent dependency for these finite exact constructions.
- `method/`: all three literal search-method extensions, including rejected/coarser candidate reconstruction. They require the unchanged BQ13 parent sources embedded in `BQ13-parent-result.json`.
- `BQ13-parent-result.json`: immutable result `asg_zSkJefQuEkGHd3_fzUFMGE19`, preserved with its original SHA-256. It contains the full parent recovery capsule; parent numerical replay has not been rerun here.
- `source-journal-entries.md`: both complete journal entries, including the capsule, instructions, failed candidates and scope limitations.
- `integrity-receipt.json`: source byte counts, hashes and provenance.

Exact replay requires standard-library Python, assertions enabled, and a fresh output directory. Read and review the supplied source before executing it. For example, from this directory:

```sh
python3 exact/REPLAY.py --object G8 --out local-G8 --stage ALL --coordinates
```

This command is documentation only; the monitor has not executed the mathematical replay. G8's claimed centred denominator is 43,316 bits, so these are not small-coordinate fractions. G14 is retained separately; coarse G6/G7 failures are claims about those rounded candidates, not impossibility results for their grids.
