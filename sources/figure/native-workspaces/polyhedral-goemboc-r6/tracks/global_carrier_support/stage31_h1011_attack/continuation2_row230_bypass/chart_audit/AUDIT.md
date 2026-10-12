# Exact row-230-loss wall chart audit

Verdict: **FEASIBLE, non-integrated** (`EXACT_ROW230_WALL_CHART_AUDIT_FEASIBLE_NONINTEGRATED`).

The exact wall is

`Delta = det(p230-p198, p231-p198, p229-p198) = 0`,

with current-cell signed slack `sigma=-Delta>0`.  The complete current support
family has three identical rows, not two:

- `support:f83:w229` for `[198,230,231]`;
- `support:f97:w231` for `[198,229,230]`;
- `support:f102:w198` for `[229,231,230]`.

The fourth orientation is replacement face `[198,229,231]` with witness 230
and the opposite inequality `Delta>=0`.  On the isolated parent-ray wall,
row 230 is strictly inside that triangle with barycentric weights approximately
`(198,229,231)=(0.00166327494214, 0.220173809175, 0.778162915883)`.

The exact physical chart has dimension 165.  The wall row has
rank 1 and tangent nullity 164.
The four target rows have rank 4; wall plus targets have
rank 5; all eight audited target/guard rows
have rank 8.

Each of the three collapsing spokes `(198,230)`, `(229,230)`, `(230,231)` has
`gram = Delta^2 * positive_cofactor` and `beta1,beta2 = Delta * nonzero_cofactor`.
All other incident face, directed-vertex, `t`, `one_minus_t`, and edge-length
primitives stay nonzero on the root interval.  Crossing removes row 230 and
the two forced rails `(229,230)` and `(230,231)`.

Both required first-order witnesses exist:

- an exact rational direction strictly decreases `S,U54,H56,H1011`, increases
  `sigma`, does not worsen base/U8, and pushes `H910` farther negative;
- an exact algebraic wall-tangent direction annihilates `dDelta` and has the
  same strict target/guard signs on the entire isolated root interval.

Therefore no Gordan/Farkas infeasibility certificate is applicable: exact
primal witnesses certify feasibility.  A separate local interval of
`epsilon=1/100000000000000000000` checks all
7904 support and
own-uniform-volume-centroid mechanics primitives, all 61 rows, base/U8, all 37
rails, and `H910<0`.  No continuation endpoint file, final integration, winner
claim, OBJ, or STL is produced.
