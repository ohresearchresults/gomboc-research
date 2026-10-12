# figure-0042

AI research report · 2026-08-23 UTC

---

# Exact result: full-orbit chamber coverage, global sign-architecture partition, and certified active-wall exclusion

## Verdict

I did **not** obtain a strict homogeneous polyhedral Gömböc, and I did **not** obtain a global infeasibility proof for the complete eight-dimensional orbit. I therefore do not claim the requested figure or a full exclusion.

The completed exact result is nevertheless substantially stronger than the preceding numerical search. It supplies:

1. an exact, gap-free reconstruction of the entire bounded positive-denominator chamber;
2. an exact bounded normalization of all five metric degrees of freedom;
3. a global proof reducing every possible unique-equilibrium witness architecture to a primal/dual pair of rooted spanning arborescences and excluding every cyclic architecture;
4. an explicit rational full-orbit point with all 27 exact rational vertices and exact own uniform-volume centroid;
5. a complete outward-rounded face/vertex/edge audit showing that point has `(S,U,H)=(3,3,4)`;
6. a nonzero closed **eight-dimensional** rational parameter box around that point on which interval arithmetic proves `U>=2` everywhere.

The original transcript had correctly isolated full-basin replacement followed by exact centroid control as the remaining construction problem. This assignment instead exhausts the global projective denominator geometry and the finite witness-sign logic of the exact 27-vertex cancellation seed.

## 1. Exact coverage of the three projective variables

Put `y_i=x_i-C_R`, where `C_R` is the original exact reference point. The complete bounded chart is

\[
D=\{d\in\mathbb R^3:1+d^T y_i>0,\ i=0,\ldots,26\}.
\]

The closure is exactly the negative polar of the translated source polyhedron. Its exact dual face lattice is

\[
(V,E,F)=(33,58,27).
\]

The verifier checks all `33 x 27 = 891` vertex/inequality relations with rational arithmetic: 116 are exact incidences and 775 are strict positive nonincidences. The smallest positive nonincidence slack is approximately `0.0010316649733123366`.

Every one of the 27 chamber facets is ordered as a cycle and triangulated. Coning those boundary triangles to the strict interior point `d=0` gives an exact face-to-face partition into **62 rational tetrahedra**. Their exact volumes sum to a chamber volume of approximately `1.1139184496193782e-6`. Thus no positive-denominator component or boundary case is omitted.

If one denominator becomes zero, a source vertex maps to infinity. If one becomes negative, continuity along the segment from `C_R` to that vertex forces a pole inside the body. Such parameters do not represent a bounded convex image.

Artifacts: exact chamber (`full_positive_denominator_chamber.json`) and exact chamber verifier report (`full_positive_denominator_chamber.verify.json`).

## 2. Exact coverage of the five metric variables

Modulo positive scale, every SPD metric has a unique trace-one representative:

\[
Q\succ0,\qquad \operatorname{tr}Q=1.
\]

The compact closure is the trace-one PSD spectrahedron. Taking `q11,q22,q12,q13,q23` as independent and `q33=1-q11-q22`, the whole closure lies in the explicit rational box

\[
q_{11},q_{22}\in[0,1],\qquad
q_{12},q_{13},q_{23}\in[-1/2,1/2],
\]

with the principal-minor and determinant inequalities stored in the chamber file. Consequently the full effective domain is an explicitly bounded eight-dimensional semialgebraic set after compactification.

A further exact simplification is important: throughout the strict denominator chamber, projectivity and the invertible affine numerator preserve the complete source face lattice. Hence every valid interior point has exactly `V=27,E=58,F=33`. Interior topology changes are impossible; apparent flips can only arise from numerical hull rebuilding or from crossing an invalid/singular boundary.

## 3. Global transfer theorem and exhaustive sign-architecture partition

For centered transformed primal vertices define

\[
g_{i\to j}=w_i^T(w_i-w_j).
\]

A vertex is strict unstable exactly when all its outgoing values are positive. To certify that another vertex is not unstable, select one adjacent witness with `g_{i->j}<0`. Then

\[
\|w_j\|^2-\|w_i\|^2
=\|w_j-w_i\|^2-2g_{i\to j}>0.
\]

Thus every selected negative witness strictly increases squared radius. A directed witness cycle is therefore impossible.

For faces, let `r_f` be the corresponding transformed polar vertex and define

\[
\gamma_{f\to g}=r_f^T(r_f-r_g).
\]

A primal face is stable exactly when its polar vertex is unstable, and the identical radius identity excludes every directed dual witness cycle.

This gives a complete dichotomy for every one-witness sign selection:

- a primal or dual directed cycle: **globally infeasible** for every `d` and every SPD `Q`;
- no directed cycle: necessarily a primal spanning arborescence directed to the selected unstable root, paired with a dual spanning arborescence directed to the selected stable root.

Conversely every strict `S=1,U=1` point induces at least one such tree pair. Therefore no sign architecture is unclassified at this logical level.

Fraction-free Bareiss evaluation of every Matrix-Tree cofactor gives

\[
\tau(G)=\tau(G^*)=10{,}503{,}279{,}880{,}522.
\]

With 27 possible unstable roots and 33 possible stable roots, the exact compressed unresolved class contains

\[
27\cdot33\cdot\tau(G)\tau(G^*)
=98{,}294{,}129{,}429{,}483{,}210{,}588{,}138{,}303{,}244
\]

rooted tree-pair architectures.

Artifacts: theorem (`SIGN_ARCHITECTURE_THEOREM.md`), machine-readable partition (`sign_architecture_partition.json`), and exact verifier (`verify_sign_architecture_partition.py`).

## 4. Explicit rational point in the full eight-parameter orbit

The exact denominator is

\[
d=\left(
-\frac{1156627810363187}{10^{17}},
-\frac{2539601704896849}{10^{19}},
\frac{7975943191573983}{5\cdot10^{18}}
\right).
\]

The exact determinant-one affine numerator is

\[
A=\begin{pmatrix}
\frac{63352455633912147}{10^{18}} & \frac{6714317}{25000000} & \frac{174622453}{50000000}\\
0 & \frac{23790906276075049}{5\cdot10^{17}} & \frac{241599921}{50000000}\\
0 & 0 & \frac{5\cdot10^{35}}{1507212334345606594937804044720203}
\end{pmatrix},
\qquad\det A=1.
\]

For `z_i=y_i/(1+d^T y_i)`, the exact uniform-volume centroid `mu(d)` is recomputed from all 50 oriented source triangles, and the final vertices are `w_i=A(z_i-mu(d))`. The package expands all 81 coordinate fractions. The final own uniform-volume centroid is exactly

\[
(0,0,0).
\]

The minimum projective denominator is rigorously larger than `0.2034014564378200107`, so this is an interior point, not a denominator-boundary artifact.

Artifacts: rational transformation (`active_wall_rational_transform.json`), all exact coordinates and centroid (`active_wall_exact_coordinates.json`), and exact coordinate identity audit (`active_wall_exact_coordinates.verify.json`).

## 5. Complete own-centroid audit of the rational near-solution

A separate 100-digit outward-rounded implementation rebuilds the body directly from the exact source and rational transformation. It audits every maximal face, all 27 vertices, and all 58 true edges. It certifies

\[
\boxed{(S,U,H)=(3,3,4)}
\]

with:

- stable faces `0,3,19`;
- unstable vertices `14,20,21`;
- saddle edge indices `17,32,35,47`;
- Morse identity `3+3-4=2`;
- zero unresolved interval predicates.

Strict positive lower bounds include approximately `2.16479308984e-5` for the limiting face predicate, `3.84263936384e-5` for the limiting normalized vertex direction, and `4.16964316044e-9` for the limiting positive edge-support predicate.

Artifacts: interval certificate (`active_wall_interval_certificate.json`), independent interval verifier (`verify_active_wall_interval.py`), and OBJ (`active_wall.obj`).

## 6. Exact active walls

The extra equilibria form adjacent pairs:

- vertices `20/21`;
- faces `0/3`.

At the exact rational point both mutual directed signs are positive. The certified raw values are approximately

\[
g_{20\to21}>194.5984473,
\qquad g_{21\to20}>187.2184501,
\]

and

\[
\gamma_{0\to3}>9.8336935\times10^{-9},
\qquad
\gamma_{3\to0}>9.9837828\times10^{-9}.
\]

The exact transfer identities

\[
g_{i\to j}+g_{j\to i}=\|w_i-w_j\|^2>0,
\qquad
\gamma_{f\to g}+\gamma_{g\to f}=\|r_f-r_g\|^2>0
\]

show why crossing a common wall transfers an equilibrium rather than annihilating both pair members. A successful branch must reroute both extras through external edges in the primal and dual rooted trees.

## 7. Certified full-dimensional eight-parameter exclusion box

Use the exact determinant-one gauge

\[
A=\begin{pmatrix}a&b&c\\0&e&f\\0&0&(ae)^{-1}\end{pmatrix}
\]

and vary all eight parameters independently around the rational point with exact halfwidths

\[
|\Delta d_i|\le10^{-13},\qquad
|\Delta a|,|\Delta e|\le10^{-11},\qquad
|\Delta b|,|\Delta c|,|\Delta f|\le10^{-10}.
\]

Outward-rounded interval evaluation over the **entire closed box** proves:

- all 27 projective denominators stay positive;
- `a` and `e` stay positive, hence the affine numerator remains invertible with determinant one;
- vertices `20` and `21` remain strict unstable equilibria at the body's recomputed own centroid.

The minimum raw directed predicate over those two vertices and the entire box is bounded below by `30.4591693789`. Therefore

\[
U\ge2
\]

throughout this nonzero full-dimensional box, exactly excluding `S=1,U=1,H=0` there.

Artifacts: exact box (`full8_exclusion_box.json`), interval report (`full8_exclusion_box.verify.json`), and box verifier (`verify_full8_exclusion_box.py`).

## 8. Remaining problem and scope

The result gives exact coverage of the projective chamber, exact global elimination of every cyclic witness architecture, a complete compressed representation of all surviving tree-pair branches, and one rigorously excluded full-dimensional eight-variable box. It does **not** interval-exclude all surviving arborescence regions.

The exact unresolved system is recorded in remaining_semialgebraic_problem.json. The appropriate continuation is a DPLL/interval solver over the 62 exact denominator tetrahedra, with:

1. parent-edge branching only;
2. immediate cycle rejection by the exact radius theorem;
3. semidefinite Gordan/Stiemke certificates for fixed primal branches;
4. `adj(Q)` polynomial constraints for dual branches;
5. exact face/vertex/edge reconstruction only for boxes surviving the relaxation.

## Reproducibility bundle

- Complete self-contained bundle (`assignment2_full_orbit_exact_bundle.zip`)
- Bundle SHA-256 (`assignment2_full_orbit_exact_bundle.zip.sha256`)
- Full technical report (`RESULT.md`)
- Manifest (`MANIFEST.sha256`)
- Captured successful verification run (`VERIFICATION.log`)

Run `./run_all.sh` inside the extracted bundle to regenerate the exact coordinates and repeat every exact and interval audit.
