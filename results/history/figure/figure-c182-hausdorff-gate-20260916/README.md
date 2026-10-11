# C182 own-centred Hausdorff exclusion — not a new Gömböc

Preserved from the completed Figure coordinator handoff, canonically archived in five exact parts at 2026-09-16T00:09:51.868Z. All parts reconstruct the original 27,428-byte envelope with SHA256 6e4555f87ef5cb817332fb4f3174be8a53ae9dfbd12cbeb40a7851069713a124. Both literal method files match their declared byte lengths and SHA256 pins.

The body is the already known Finch C182_TWO_PLANE222, V54/E91/F39, own222/weak000. The new certificate concerns an own-centred Hausdorff neighbourhood of radius 9/1000 in the original coordinate frame and units: bodies inside it retain at least two strict stable and two strict unstable equilibria. This is not a global edge-count lower bound, not a coordinatewise tolerance, and not a claim that leaving the neighbourhood suffices for own110. The previous affine-only certificates remain separate evidence.

Operator verification rebuilt the exact input from the intact original Finch source, ran both complete independent auditors and the third mass integration, then executed every new rational containment predicate. The 778-byte certificate matches the author's SHA256 f55bd545683ae78f08848743645012bdd3628db77ed79f5240f04cf8d7022096 exactly. See local-proof/verification-receipt.json and operator-replay.txt. The geometric proof is retained verbatim in handoff.md; computational reproduction is not a formal proof-assistant verification.

The complete finite affine/projective numerical method is preserved too. The author reports 26,941 and 52,320 evaluations respectively, without own110; those finite searches were not rerun by the operator and do not exclude entire transformation families. Seed, bounds, iteration counts, environment and all required input identities are in the source and handoff.

Reproduce from this directory with a fresh output directory:

```sh
python3 -B -S ../figure-finch3-c182-c592-nonwinners-20260915/source/replay_fin.py --case C182_TWO_PLANE222 --out NEW_EXACT
python3 -B -S C182_DOUBLE_GEOMETRIC_GATE.py --raw NEW_EXACT/raw.json --audit NEW_EXACT/A.json --out NEW_EXACT/CERTIFICATE.json
```

The original 44-file parent is retained at the path above; no original or journal was overwritten. The handoff's separate 15-file ZIP and floating endpoint JSON downloads have not been retrieved. Their sandbox links are not counted as saved files; exact scientific inputs and the full methods needed for reconstruction are preserved locally.
