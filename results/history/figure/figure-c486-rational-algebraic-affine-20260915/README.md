# Three distinct C486 nonwinners and exact mass-closure method

Preserved from canonical Figure entries1380–1385 on2026-09-15. The accepted own110 edge record remains C622. None of these C486 bodies is a Gömböc.

| Construction | V/E/F | Own S/U/H | Evidence |
|---|---|---|---|
| Rational opposite point R12 |118/243/127|7/2/7|Author reports full exact A/B, third mass and completed cold replay|
| Isolated algebraic mass-closed point |118/243/127|7/2/7|Author reports exact quartic/Sturm/visibility, independent boundary moments and full interval census, then completed combined cold replay|
| Projective/affine image of rational R12 |118/243/127|3/3/4|Author reports exact A/B, third mass and vertex bijection; its combined cold replay was still pending in entry1385|

All report weak-only000. The algebraic point has degree at most4 and restores the exact old C602 centroid; it is not the nearby rational R12 point. Four real quartic roots were isolated, but only one lies in this fixed41-visible-facet chamber. That is not an all-chamber or unrestricted geometric exclusion. The affine body transforms the rational R12 body, not the algebraic one, and recomputes actual filled mass.

The three literal source maps are retained in `rational/` (5files), `algebraic/` (8files), and `affine/` (1file). There are13 unique file contents because one original helper is shared across the first two published capsules. Full encoded/decoded and per-file pins, syntax and22 upstream dependency files were checked. No mathematical or numerical replay was executed by the monitor; the scientific claims remain author evidence.

Dependencies already preserved once:

- `../figure-four-frontiers-core-20260915/source/` —16files.
- `../figure-c592-exposed-chain-20260915/source/` —6files.

With fresh output directories, the published replay entry points are:

```sh
python -B -S rational/REPLAY_OPPOSITE.py CORE C592_SOURCE NEW_R12_PROOF
python -B -S algebraic/REPLAY_MASS_GATE.py CORE C592_SOURCE rational NEW_MASS_PROOF
python -B -S affine/REPLAY_AFFINE334.py CORE C592_SOURCE rational NEW_AFFINE_PROOF
```

Use the two explicit dependency paths above for CORE and C592_SOURCE. `canonical-entries.md` preserves all exact roots, coefficients' reconstruction, parameters, expected output hashes and evidence boundaries.

The algebraic method produces quartic coefficients up to107,564bits and Sturm intermediates up to356,600bits; exact centering is not an arithmetic simplification. The affine variant's shared centred denominator is63,728bits. The separate18/24/20/117-case numerical screens remain pending their own complete method/data capsule and are not covered by these14 files.
