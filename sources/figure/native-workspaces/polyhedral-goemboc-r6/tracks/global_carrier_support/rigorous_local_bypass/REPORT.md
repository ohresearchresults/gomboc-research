# Exact directed carrier bypass and topology walls

## Verdict

`RUN_ALL.sh` finishes with both literal verdicts

```text
EXACT_DIRECTED_LOCAL_BYPASS_AND_FIRST_HARD_WALL_PASS
EXACT_DIRECTED_STAGE6_TETRAHEDRAL_FLIP_PASS
```

The proof layer reads every saved finite decimal as an exact `Fraction`.  It
repairs the nominal base to the exact rational plane through rows `0,54,1`,
rationalizes the saved 22 chart columns, and reprojects every base column to
that plane.  Qhull only locates face ledgers during certificate construction;
the clean-process verifiers accept them only after exhaustive exact support,
topology, centroid, and mechanics reconstruction.

This is a theorem about the explicitly frozen nearby rational chart and the
two saved rays.  It is **not** a global continuation/existence theorem and not
a theorem about Qhull's binary64 coplanarity tolerance.

## Linked birth wall and continuous bypass

For the common edge `(8,245)`, let `n1` be the normal of `[7,8,245]`, `n2` the
normal of `[8,245,246]`, and `X245=4D(p245-centroid)`.  The active components
of `S(8,245,246)` and `H(8,245)` share the exact numerator

```text
N = (X245.n1) ||n2||^2 - (X245.n2) (n1.n2).
```

The verifier proves the polynomial identity connecting the directed face-foot
component to `N`, proves the Gram, normal, reference-orientation, and cross
factors have strict signs, and proves every other component of the two
features is strictly positive.  Thus the two numerical roots are one exact
root in this chart.

The isolated local `x` root is

```text
midpoint = -3.1858654575556146e-16
width    =  5.551115123125783e-25
```

It maps to original continuation coordinate about
`alpha=0.06992415224174803`.  The roughly `1e-13` displacement from the
binary64 locator is the explicitly recorded base-plane/chart rationalization,
not an asserted enclosure of the unmodified floating model.

An independent antibirth tangent is reconstructed by exact cofactors in the
five controls

```text
row7_u, row9_u, row54_v, row10_v, row10_u.
```

All four keep-gradient pairings are the literal zero polynomial.  The pairing
with `N` is strictly negative throughout the isolated root interval; equivalently
the augmented `5x5` determinant is nonzero there.

All four radius-`1e-5` quadrant points have exact fresh supporting hulls with
`(V,E,F)=(61,162,103)`, Euler `2`, the base, and all 37 forced rails.  The two
lower cells have class `(3,2,3)` and the two upper cells class `(2,2,2)`, with
the linked signs exactly as predicted.

The L path

```text
(-1e-5,0) -> (-1e-5,+1e-5) -> (+1e-5,+1e-5)
```

is certified continuously, not by its old 81 samples.  Each segment has 6,968
exact constant-sign Bernstein certificates: all supporting slacks, face
orientation and edge-denominator factors, protected base/U8 components, and
an exhaustive negative witness for every forbidden S/U/H feature.  Hence the
entire closed L path stays fresh-hull valid, class `(2,2,2)`, avoids both linked
births, and retains all rails.  Segment digests are

```text
f5e1127d9e73138c7c2e7cfbec1197e9b66a3ea090ceb99a66e208dce23d7245
ac03cdfe213885b9da2fc5d763f2f70f9a054543728552e5b73d4408775b4381
```

## First hard active-row wall

On the saved post-bypass adaptive ray, the first hard wall is exactly

```text
det(8,9,10,263) = 0
t midpoint = 0.0006713057191167713
root width = 5.082197683525802e-25.
```

The determinant is quadratic and strictly decreasing on the isolation
interval.  Exactly two prewall support slacks are `-det`; the other 5,957
support polynomials stay strict through the entire root interval.  This proves
the ordering, rather than merely identifying a flip after it happened.

Before the root the exact hull has `(61,162,103)` and row `9` is active.  After
it the exact hull has `(60,160,102)`, row `9` is strictly in the relative
interior of the new base face, and the class remains `(2,2,2)`.  The flip is

```text
faces removed: base-with-9, [8,9,263], [9,10,263]
faces added:   base-without-9, [8,10,263]
edges removed: (8,9), (9,10), (9,263)
edge added:    (8,10)
```

## Stage-6 common support/topology event

The later event is exactly the tetrahedral circuit

```text
det(7,8,245,246) = 0
t midpoint = 0.007530223475369099
root width = 6.776263578034403e-25.
```

The exact rational-chart root is `5.4366637494e-10` past the saved binary64
estimate; that shift is recorded explicitly and comes from the exact base/chart
rationalization.  Exactly two pre-flip support slacks equal the circuit
determinant.  All other 5,957 remain strict through the isolated interval.

At the root, the exact face ledger has `(61,161,102)`, Euler `2`, and the merged
strict supporting quadrilateral `[7,8,245,246]`.  Its exhaustive 1,003-polynomial
mechanics certificate gives class `(2,2,2)` with stable faces base and the
quadrilateral, unstable vertices `8,54`, and saddles `(6,7),(9,10)`.

Across the root:

```text
faces: [7,8,245] + [8,245,246]  ->  [7,8,246] + [7,245,246]
edge:  (8,245)                  ->  (7,246)
```

`S(7,8,246)` is the new stable face; `[7,245,246]` is nonstable, and the new
diagonal `(7,246)` is nonsaddle by a strict negative `beta1`.  Active labels,
base, all 37 rails, unstable vertices, saddle edges, and total class remain
unchanged.  Therefore this wall transfers the stable local face; it does not
create an additional U or H.

## Reproduction and hashes

Run from this directory:

```bash
./RUN_ALL.sh
```

Primary source hashes:

```text
row54_far_rebuilt.csv              611e8e57e2d8986f410894f67f20ffd1c07dc378a49218f5576cf350676ab004
row54_far_rebuilt_audit.json       78af366cfff29d52564a4fae07b22f0f19684cdcbc82a89ff5de14f3b30ad3a2
local_birth_atlas.json             0efed84d5e00cae6ee0e4ffdabfbd57adbde372ac3314db6ed91f28f25417442
pair_wall_continuation.json        b3913111ddf7ded65b1fcd360cde4123479904de06bb00f57b7d825474976b2d
adaptive_birth_bypass.json         ce1600a3187a696e7fca030c1543a9347efbdb98929e76311d89d7c993e32872
adaptive_five_circuit_stage6.json  3bab2c521e71cb0fdf1d9501d8840c8a00de7b3d8cea3efae3d37004b313a393
stage6_topology_wall_audit.json    73678a58fa9bcf7a14c794445d6e9a99e5f35aca0666566c7a9fd927f98c84d4
```

Face-ledger hashes:

```text
local star       16c74e44430e5c6aee076c598bd3aa45f023253352784cabf2fde3b8e29b879e
first-wall post  7ae6924ccd2e905e3f3e9bb92c65b542eb2f0fa48eddf7ad65225273732a82e6
stage6 pre       3e0e8051a3b39279fd0e8b8dc41e7ab470ad0bb9f25b6c86511d75fd363707ad
stage6 wall      e484c8f05907f3ed248ab37a263bbda7527193420b55426f7ae4f1aaf5e64994
stage6 post      fe33c599ab3f8eabd05c61d206f48beadbdefd111be4fb65bc4a32140a795251
```

`certificate.json` and `stage6_certificate.json` contain every exact
coefficient, rational root bracket, source/face hash, transition, and digest.

