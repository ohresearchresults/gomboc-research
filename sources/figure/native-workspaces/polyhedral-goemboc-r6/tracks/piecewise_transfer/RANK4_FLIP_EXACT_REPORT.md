# Exact directed audit of the clean row-54 compensating flip cell

## Verdict

In the fixed actual cell materialized by `row54_multiwall_flip.csv`, no one of
the 144 component choices can remove all four residual equilibria before some
protected/witness/support guard reaches zero in the directed analytic first
jet with

\[
\|D c\|_\infty\le 0.1,\qquad \|c\|_\infty\le 20.
\]

All 144 fixed-\(\delta=1\) branches now have separate literal rational Farkas
certificates.  For every branch, its supported analytic rows and decimalized
nonnegative locator weights were rebuilt over exact Fractions; the complete
175-column stationarity residual was then cancelled exactly with allowed
coefficient-box rows.  Every repaired right-hand side is strictly negative.
The closest one to zero is branch 55:

\[
b^T y = -2.7275656563049473\ldots\times 10^{-12}<0,
\qquad A^T y=0
\]

with every multiplier nonnegative.  This is not an inference from floating
ranking: the exact coverage ledger contains a negative rational RHS and exact
stationarity/nonnegativity checks for each named branch 0 through 143.  Thus
the apparent razor-thin subunit branches in the old finite-difference atlas
were solver/derivative artifacts, not directed first-order escape witnesses.

This is a fixed-cell, first-order theorem.  It is not a nonlinear path or
fresh-hull theorem outside the stated trust region.

## Cell and branch ledger

The audited source has f-vector `(61,162,103)`, mechanics class `(2,2,2)`, and
all 37 forced rails.  Its unwanted packet is:

- stable face `S[198,243,244]`, with three face-foot edge components;
- unstable vertex `U2`, with neighbours `1,3,88`;
- saddle edge `H[4,5]`, with components `t, 1-t, beta1, beta2`;
- saddle edge `H[12,13]`, with the same four component choices.

Therefore the directed component atlas has exactly
\(3\times3\times4\times4=144\) branches.  The exact 44-coordinate structural
ledger proves that every branch has death-gradient rank four and rank five
after adding the shared ultrathin quad-support primitive.  The two apparent
support slacks on faces `[3,88,2]` and `[88,3,242]` are exactly the same
oriented tetrahedral volume of `{2,3,88,242}`.

## Frozen 175-column analytic chart

The decisive audit uses exactly the 175 cached displacement modes of the full
guarded LP:

- 48 Dirichlet-Laplacian graph modes;
- complete defect-star, base-tangent, and remote row-coordinate controls;
- nine linear controls and three projective controls.

Every cached binary64 displacement is interpreted as its exact dyadic
rational.  The finite-decimal source coordinates and supplied 103 maximal-face
cycles are also exact.  Normalized primitives are differentiated through
their rational logarithmic derivatives; for example,

\[
d\log\frac{P}{\sqrt{RS}}=\frac{dP}{P}-\frac12\frac{dR}{R}-\frac12\frac{dS}{S}.
\]

This removes every square root while retaining the exact first derivative of
the normalized mechanics/support component.  The common ledger contains 6301
selected protected, non-feature-witness, and support rows.

## Complete exact analytic coverage

For each branch the fixed-\(\delta=1\) system is

\[
\begin{aligned}
  \text{guard loss}_k(c)&\le1 &&(6301\text{ rows}),\\
  d\log f_i(c)&\le-1 &&(4\text{ chosen deaths}),\\
  |Dc|&\le0.1 &&(183\text{ physical coordinate rows}),\\
  |c_j|&\le20 &&(175\text{ coefficient rows}).
\end{aligned}
\]

Every inequality is scaled by its infinity row norm only for active-set
location.  The numerical IPM/revised-simplex solves have no theorem role:
their positive supports are merely proposals.  On each proposed support, the
batch exactifier performs the following rational calculation:

1. interprets every cached binary64 mode coefficient as its exact dyadic;
2. rebuilds every supported normalized-dlog guard/death row exactly;
3. converts every positive locator multiplier to an exact finite-decimal
   rational;
4. cancels each component of the resulting stationarity residual with an
   available `+e_j` or `-e_j` coefficient-box row;
5. tests the repaired rational value of \(b^T y\) for strict negativity.

The complete exact result is:

- 144 branches enumerated;
- 144 exact nonnegative multiplier ledgers;
- 144 exact zero stationarity vectors in all 175 columns;
- 144 strictly negative exact Farkas right-hand sides;
- no failed branches;
- closest-to-zero exact certificate: branch 55.

Branch 55 selects

1. `S[198,243,244]` via edge `(243,244)`;
2. `U2` via neighbour `1`;
3. `H[4,5]` via `one_minus_t`;
4. `H[12,13]` via `beta2`.

Branch 55 uses a revised-simplex locator with 214 positive supported rows.
Its unrepaired exact RHS is `-3.593923514590313e-12`.  The exact stationarity
repair mass is `4.331789291426827e-14`; multiplying that mass by the box RHS
20 gives the complete repair cost.  The repaired exact RHS remains strictly
negative at `-2.7275656563049473e-12`.

The three other solver-scale supports (branches 9, 13, and 54) also use
revised-simplex locators and retain exact repaired RHS values
`-4.053865372522443e-12`, `-4.218620712814449e-12`, and
`-3.2425694863912957e-12`.  Every other branch's IPM support survives the same
exact reconstruction and repair; no numerical ordering assumption is used.

For comparison, the former finite-difference leader branch 102 also has an
independent exact analytic certificate with repaired RHS
`-1.875419937433946e-08`.  The easier branch-4 trust pilot has the exact dual
lower bound `delta >= 6.8482681832897`.

## Artifacts

- `rank4_flip_exact_ledger.py/json`: exact primitive/Jacobian and 144-branch
  rank ledger in the explicit 44-coordinate local chart.
- `rank4_flip_175_analytic_guard_rows.npz`: one rebuilt 6301-by-175 analytic
  guard matrix used by every branch.
- `rank4_flip_analytic_dual_atlas.py/json`: complete 144-branch row-scaled
  analytic active-set locator and branch-to-component mapping; its floating
  signs are not used as proof.
- `rank4_flip_analytic_dual_atlas_ipm_weights.json`: retained IPM multiplier
  proposals for all branches.
- `rank4_flip_analytic_dual_search.py`: individual analytic active-set and
  crossover locator.
- `rank4_flip_exact_coverage.py/json`: literal per-branch rational rebuild,
  exact stationarity repair, and strict 144-of-144 Farkas coverage theorem.
- `rank4_flip_exact_analytic_farkas_branch13.json`: independent exact
  branch-13 certificate from the earlier numerical ranking.
- `rank4_flip_exact_analytic_farkas_branch102.json`: decisive exact certificate
  for the former finite-difference leader.
- `rank4_flip_exact_trust_farkas.json`: exact branch-4 trust pilot.
- `verify_rank4_flip.py`: materialized-ledger and certificate verifier.
