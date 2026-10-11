# Exact small-physical actual-cell escape from the supporting shell

## Result

The exact supporting-shell seed `(61,150,91)`, mechanics class `(3,4,5)`, has a
literal actual-cell escape using only the normalized row-255 physical actuator

\[
q_{255}(t)=q_{255}(0)+t(-1/2,-1,-1/4),\qquad t\le 0.
\]

The largest moved coordinate is exactly `|t|`.  Before total displacement
`3/40 = 0.075`, the path crosses three exact convex-hull circuit walls and one
isolated algebraic mechanics wall.  Every rational open cell and every topology
wall was rebuilt from the 119 rows with exact supporting planes, exact ordinary
volume/centroid and exact mechanics.

At the far point `t=-3/40`:

- the hull is still `(61,150,91)`;
- all 61 source rows are active;
- the protected base is stable;
- `U8` is unstable;
- all 37 forced rail edges survive;
- the mechanics class is `(2,4,4)`.

The crossing therefore removes both `S[228,254,255]` and `H(228,255)` without
using the macroscopic formal affine root.

## Ordered circuit passage

| Event | Exact parameter | Decimal | Flip |
|---|---:|---:|---|
| C1 `{54,69,255,256}` | `-3615267103928901398240936256322781 / 611921550720128478247065031250000000` | -0.00590805651423 | remove `(69,256)`, add `(54,255)` |
| C2 `{54,255,256,257}` | `-6438261608048694302098584291151381 / 197629520245071295791538014000000000` | -0.0325774287164 | remove `(54,256)`, add `(255,257)` |
| C3 `{69,253,254,255}` | `-56405681997229737189821421650935963 / 1384604901927999443875664360000000000` | -0.0407377454165 | remove `(69,254)`, add `(253,255)` |
| M, shared mechanics | unique cubic root in `[-71/1000,-7/100]` | -0.0701777438694 | kill `S[228,254,255]` and `H(228,255)` |
| C4 `{54,255,257,258}` | `-4970733002820949473430874776013092097 / 54545695939900301628073599750000000000` | -0.0911297017513 | remove `(54,257)`, add `(255,258)` |

For each open topology cell the producer checks all 10,529 strict face-support
inequalities.  Their exact intersection has the adjacent circuit roots as its
literal endpoints, which proves order and excludes an unlisted topology exit.
At each circuit wall the rebuilt f-vector is `(61,149,90)` and all protected
objects survive.

The first event after the `(2,4,4)` far cell is C4.  The exact point `t=-1/10`
lies beyond it and rebuilds again as `(61,150,91)`, class `(2,4,4)`, with
base/U8/all 37 rails intact.  The following exact topology endpoint is C5 at
approximately `-0.131705008518`.

## Shared mechanics wall

In the complete C3--C4 support chamber, the numerator for the directed face
component of `S[228,254,255]` along `255->228` and the numerator for
`H(228,255):beta2` have the same primitive cubic factor.  With coefficients in
ascending powers it is

```text
-3325940631378510271964993690692151947521897104756381965637909593220061559601804046309614703120692980778359328304426744622456579530192292614575984111447
-47391859904211122771873159953552264604882376821548747997960133113360748990639530142295658093186441277361801209974301920431299238799714941369875000000000 * t
+17637520410351383300672083782754106277245109120629054769741256416163431950008934112856544900295235502001278757181405407123431531250000000000000000000 * t^2
+109299642899737286045299392077155412208240828857123468274538725627373643134458491647316466637340405173078832146484375000000000000000000000000000000 * t^3
```

Its signs differ at the rational endpoints `-71/1000` and `-7/100`.  The exact
Sturm sequence has degrees `3,2,1,0` and counts exactly one root in that
interval.  Symbolic rational-function ledgers also prove that all 16 base face
components and all 14 supports of `U8` have zero roots throughout the entire
C3--C4 chamber.  Rails and all-active status are fixed by the exact support
chamber.

## Far-cell residual cone

The remaining original five death gradients have exact rank 5.  Adding the
three other live saddle walls produces a complete eight-wall residual block
of exact rank 6 in the six normalized physical controls.

A numerical locator finds strict residual-death directions in sparse 2D/3D
charts, but they immediately point toward rebirth of the killed pair.  The
authoritative result is an exact homogeneous Gordan circuit.  Seven positively
scaled primitive integer gradient rows—six residual deaths and the no-rebirth
guard for `S[228,254,255]`—have strictly positive integer multipliers and sum
to zero in every one of the six control columns.  Hence no direction can make
all eight residual death derivatives strictly negative while keeping both
killed-wall derivatives nonpositive.  This is a local far-cell cone theorem,
not a claim that no further sequential topology passage exists.

## Artifacts

- `rank5_circuit_escape.py` — exact producer and symbolic derivation.
- `rank5_circuit_escape.json` — circuit/chamber ledgers, cubic, far rank and
  literal Gordan multipliers.
- `rank5_escape_cells/` — source, pre/wall/far rational cells and the labelled
  algebraic-wall locator.
- `verify_rank5_circuit_escape.py` — clean regeneration plus independent exact
  checks of circuit determinants/brackets, chambers, Sturm count, far flags,
  Gordan stationarity and every recorded SHA-256.
- `rank5_circuit_escape_artifacts.sha256` — hashes for the delivered package.

Run:

```bash
python tracks/piecewise_transfer/verify_rank5_circuit_escape.py
```

Expected final marker:

```text
VERIFIED_EXACT_RANK5_ACTUAL_CELL_ESCAPE
```
