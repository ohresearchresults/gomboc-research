# Numerical method recovery and evidence limits

The exact source capsule is independent of NumPy/SciPy and independent of these optimizer runs. This numerical capsule preserves all complete materially used methods, exact input coordinates, seeds, nondefault controls, and observed floating-point checkpoints. The finite failures are not exclusions. Numerical flags are not exact equilibrium certificates; only the three independently audited rational grids in the exact capsule are exact bodies.

The accepted benchmark remains VQ20_C622_ROUTE88_118_G12, C622 own110/weak000. New exact COORD_PYRAMID_C64_BASE16_G100000_OWN211 has C64 but TWO stable equilibria and one saddle; it is not a Gömböc. Grids1000 and10000 are distinct C64 own266 and own244 bodies, not aliases.

Run with Python3.13.5, the NumPy/SciPy versions in each checkpoint, and BLAS/OMP one thread set by each script. Commands, run in the recovered numerical directory:

    python -B pyramid_search.py --ears 1 --witness 0 --seed 160926 --iterations 180 --polish 1400 --out EAR1_W0_REPLAY.json
    python -B pyramid_coarsen.py --n 12 --seed 160926 --tries 3 --max-nfev 120 --out COARSEN12_REPLAY.json
    python -B pyramid_coarsen.py --n 19 --seed 160926 --tries 3 --max-nfev 160 --out COARSEN19_REPLAY.json
    python -B pyramid_coarsen.py --n 17 --seed 160926 --tries 3 --max-nfev 180 --out COARSEN17_REPLAY.json
    python -B greedy_coarsen.py --input COARSEN17.json --out GREEDY16_REPLAY.json --max-nfev 220 --attempts 5

EAR1_W0 completed without numerical own110. Its terminal marker is CHANGED_BASE_PYRAMID_FINITE_SCREEN_COMPLETE. Each COARSEN run ends with CHANGED_BASE_COARSENING_FINITE_SCREEN_COMPLETE in the JSON. COARSEN19 and COARSEN17 each obtained a first-try numerical own211; other attempts did not. GREEDY16 deleted parent cyclic index4 and obtained numerical own211; terminal FINITE_DELETION_REPAIR_HAS_NUMERICAL_OWN211. Exact rational coordinates were defined by applying Python round(D*v), ties to even, to every saved GREEDY16 raw_points binary64 coordinate for D1000,10000,100000. The literal resulting integer rows are preserved in the exact capsule; replaying the floating optimizer is unnecessary to reconstruct them.

C64_EXACT_CHECKPOINT.json is a numerical continuation view of the exact grid100000 raw integer points divided by100000, before a new base deletion and true-centroid recalculation. It explicitly points to the exact source definition. Its minimum h=.04 is the numeric family choice; the exact apex height is4000 in grid coordinates. No further descendant was computed before persistence of this capsule.

ConvexHull in pyramid_search.py is only a numerical oracle for the changed base. The exact auditors independently reconstruct all supports/vertices/true edges/volume moments/equilibria. A candidate with fewer than8 base vertices (C<32) is rejected before the numerical census. The own211 coarsener is an auxiliary architecture search, not an accidental relaxation of the required final own110 target. It does not assert any lower bound.

Numerical optimizer replay can differ across library/CPU environments, especially at max/convex-hull switching surfaces. The complete observed parameter vectors and raw geometric checkpoints are therefore preserved as literal data. The exact bodies and standard-library proofs/certificates do not depend on repeatability of floating optimization.
