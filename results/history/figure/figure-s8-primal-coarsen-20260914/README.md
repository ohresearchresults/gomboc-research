# S8 primal coarsening: complete methods and five nonwinner definitions

All six canonical journal parts (08:18:02–08:26:33 UTC, 14 September 2026) are preserved byte-for-byte. The complete 22-file source package is under `source/`; its original `README.md` contains exact reconstruction, proof verification and numerical-search commands. The literal five finite rational inputs are in `source/CHECKPOINTS.json`.

Three bodies have author-reported complete independent A/B geometry/mechanics audits and third centred-mass verification. Each has V176/E311/F137, C622, weak000:

- `elastic2_D176`: equilibria 65/64/127.
- `elastic3_D147`: equilibria 1/2/1.
- `elastic3_D176`: equilibria 1/2/1.

None is a Gömböc. Two further exact rational definitions, `elastic2_D147` and `elastic2_D84`, have only numerical equilibrium classifications; do not promote those to exact counts. Best accepted construction remains C624.

The sources preserve the numerical deletion-catalog proposer, independent full-case verifier, 315-control primal chart, actual filled moments, fixed-forest/reverse-widest-tree optimizer versions, all configurations and three exact expected audit-output manifests. Legacy overflow-producing source/configurations are included for failure provenance, but corrupted saved outputs are explicitly excluded as continuation inputs. Improving an aggregate residual did not reliably improve equilibrium counts.

Dependencies were verified in place, without duplicate archives:

- `../figure-c624-s8-20260914/source`: complete 30-file S8 source package.
- `../figure-s8-fixed-d12-exclusion-20260914/source/REPLAY_INPUT.py`: exact S8 raw input reconstruction for the discovery/full-case verification route.

Follow `source/README.md`, setting its SOURCE to the first path and METHOD to this package's `source` directory; all output directories must be new. Exact replay uses Python's standard library with assertions enabled. Numerical discovery additionally used NumPy/SciPy with versions and configuration pinned in the original README; time-limited optimization is not claimed bitwise reproducible.

The monitor checked all six part pins, full encoded/decoded hashes, all 21 new per-file manifest entries, all 29 parent manifest entries, the additional input-replay source hash, JSON/Python syntax, and exact archive readback. **It has not executed the scientific scripts or repeated the mathematical checks.** The author reports source-only reconstruction, all five auxiliary-H identities, and byte-identical full audit outputs for the three exactly classified bodies.
