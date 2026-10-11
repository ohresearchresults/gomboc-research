# C96 planar 24-gonal pyramid: own211 nonwinner

Canonical identity: `COORD_C96_PLANAR24_PYRAMID_OWN211`, journal event1421, 2026-09-15T21:42:01.239Z. The claimed V25/E48/F25 body has strict own(2,1,1), weak000; it is not a Gömböc. Accepted own110 record remains C622.

The complete original generator is preserved byte-for-byte with its published SHA256. It projects the 24 non-apex points of the exact C138 parent to one plane, keeps the apex, scales to integers, translates, constructs the exact hull, and recomputes the actual uniformly filled centroid. Twenty-one fewer edges arise from real maximal-facet coalescence, not recounting triangulation diagonals.

Dependencies are previously preserved, pinned local sources, not sandbox links: `../figure-c138-integer-own211-20260915/POINTS25.json`, `../figure-c282-integer-own211-20260915/c182_chain/exact_points.py`, and `../figure-finch3-c182-c592-nonwinners-20260915/source/core/{check_A.py,check_B.py,centred_mass.py}`. The canonical entry contains published output hashes. Run from this directory with a fresh output directory:

```sh
PYTHONPATH=../figure-c282-integer-own211-20260915/c182_chain python3 -B -S planar25.py ../figure-c138-integer-own211-20260915/POINTS25.json ../figure-finch3-c182-c592-nonwinners-20260915/source/core NEW_PROOF
```

See `local-proof/RECEIPT.json` for the separately recorded operator verification. No claim about impossibility for all pyramids or all affine/non-affine deformations is made.
