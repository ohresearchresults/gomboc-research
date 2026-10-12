# Exact C648 constructions and numerical discovery methods
Run `python3 -S RUN_ALL.py --cold` for all three exact rational objects.
C648_REBUILT_R7 is the preferred strict110 body:189 vertices,324 true edges,137 maximal facets.
C648_REBUILT_R12 is a distinct strict110 body of the same combinatorics.
C648_DIRECT_SEED_NONWINNER is the separate strict211 seed, not a Gomboc.
All three have full exact weak000 census, all1296 nonzero true-edge primitives, no vertex-pair zero, and independently reconstructed exact filled-volume centroids.
The mathematical definition is GENERATOR.json plus RECONSTRUCT.py: normalize support inequalities q.x<=1 then translate by the exact volume centroid. All centred rational vertices are regenerated as CENTRED_VERTICES.json.
Discovery methods require NumPy/SciPy; exact acceptance uses only standard library. Numerical condition36_best is a further, unaccepted conditioning checkpoint, not either audited R7/R12 object. BASE650/A.json intentionally retains only topology and190 placeholders: it is a topology input, NOT an exact audit report. BASE650/GENERATOR.json defines the exact original incumbent.
