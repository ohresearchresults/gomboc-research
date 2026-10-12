# figure-0037

AI research report · 2026-08-22 UTC

---

# Result

I do not claim an exact-certified strict rational `S=1,U=1,H=0` witness. The completed result is a corrected full-orbit reduction, three independent global numerical searches, an exact face/vertex/edge verifier, the strongest rigorously certified near-solution, and a machine-checkable exclusion neighborhood around the near-solution.

## 1. Full projective orbit: the missing three parameters

For a bounded projective image

\[
\Phi(y)=\frac{Ny+a}{1+d^Ty},\qquad 1+d^Ty>0\text{ on }P,
\]

write `A=N-a d^T`. Nonsingularity of the homogeneous projective matrix implies that `A` is nonsingular, and

\[
\Phi(y)=A\frac{y}{1+d^Ty}+a.
\]

Let `mu(d)` be the uniform-volume centroid of `Z_d(P)`, where

\[
Z_d(y)=\frac{y}{1+d^Ty}.
\]

Affine equivariance of the centroid gives

\[
\Phi(P)-\operatorname{centroid}(\Phi(P))
=A\bigl(Z_d(P)-\mu(d)\bigr). \tag{1}
\]

Consequently, the three denominator coordinates `d` remain free. Requiring a preselected source point to map to the transformed centroid imposes three additional equations and searches only a special slice; it is not a normal form for the full problem.

After QR decomposition of `A`, output rotation can be discarded, and output scale can be fixed by `det(A)=1`. A positive-diagonal upper-triangular `A` then has five parameters. Equation (1) therefore gives an exact **eight-dimensional** normal form for the full bounded projective orbit modulo recentering, rotations, and scale: three projective-denominator parameters plus five metric parameters.

The complete proof and rational homogeneous-matrix formula are in FULL_ORBIT_NORMAL_FORM.md.

## 2. Exact mechanical audit

For final centroided rational vertices `w_i`, the independent verifier uses only exact rational arithmetic:

- Vertex `i` is strictly unstable iff `w_i^T(w_i-w_j)>0` for every adjacent `j`.
- For a face with outward normal `n`, plane value `h`, and perpendicular foot `q=h n/(n^Tn)`, every oriented boundary-edge test `((w_{k+1}-w_k) x (q-w_k))·n` must be positive.
- On edge `[i,j]`, it computes the exact foot parameter `t`, solves `q=lambda n_1+mu n_2`, checks the residual exactly, and declares a saddle only when `0<t<1`, `lambda>0`, and `mu>0`.
- It checks the complete face lattice and `S+U-H=2`.

Verifier: verify_full_orbit_result.py.

## 3. Global search performed

Three independent searches were implemented over the complete effective eight-dimensional positive-denominator chamber:

1. A direct rational upper-triangular affine parameterization, with scrambled Sobol exploration, differential-evolution restarts, nonsmooth polishing, exact rationalization, and full edge audit.
2. A primal/dual search using the fact that stable faces of `P` are unstable vertices of the polar; this directly optimizes the adjacent transfer inequalities on both primal and dual graphs.
3. A symmetric log-metric search with `Q=exp(H)` and `Q^{-1}=exp(-H)`, where `H` is trace-free symmetric. This removes triangular-coordinate bias and covers the entire SPD metric cone modulo scale.

The searches recompute the transformed polyhedron's own exact tetrahedral volume centroid for every projective denominator. They do not retain the original auxiliary center as a mechanical reference.

Search implementations and machine logs are included in the bundle:

- full_projective_metric_search.py
- full_orbit_dual_search.py
- full_orbit_Q_search.py

These are global multistart searches, not a single local five-parameter optimization. A nonpositive best maximin value, however, is not promoted to a proof of infeasibility.

## 4. Strongest rigorous certified fallback

The existing interval certificate rigorously encloses the unique projective-centroid root in the earlier reference-point-preserving slice. At that root, the transformed body has centroid exactly zero. Applying the exact determinant-one rational affine map

\[
A=\begin{pmatrix}
167563125811/40000000000 & -264973961753/200000000000 & -2899591335529/1000000000000\\
0 & 37462476781/31250000000 & 1872844404873/1000000000000\\
0 & 0 & 1250000000000000000000/6277329710046369294391
\end{pmatrix},
\qquad \det A=1,
\]

produces the rigorously certified equilibrium count

\[
(S,U,H)=(3,3,4),\qquad S+U-H=2.
\]

The complete transformed-coordinate enclosures, exact source coordinates, complete face lattice, all face/vertex/edge sign intervals, root uniqueness proof, and determinant audit are in rational_affine_interval_certificate.json. Its construction script is rational_affine_interval.py.

## 5. Precise active transfer walls

The certified near-solution is pinned by two explicit adjacent transfer pairs:

- Faces `7` and `22`, sharing primal edge `[11,16]`.
- Vertices `14` and `26`, sharing edge `[14,26]`.

Both mutual face-transfer signs are strictly positive, approximately `3.8635e-10` and `3.8645e-10`; their sum is approximately `7.7280e-10`. The two vertex-transfer signs are approximately `7983.8969` and `6888.7762`; their sum is approximately `14872.6731`.

The exact identities explaining the obstruction are

\[
g_{ij}(Q)+g_{ji}(Q)=(w_i-w_j)^TQ(w_i-w_j)>0
\]

for adjacent vertices, and

\[
g_{fg}(R)+g_{gf}(R)=\lVert p_f-p_g\rVert_R^2>0
\]

for adjacent polar vertices/faces. Thus the two equilibria cannot both disappear through their common edge: crossing the common wall transfers the equilibrium from one endpoint or face to the other. This identifies the active chamber wall rather than merely reporting a stalled objective value.

## 6. Certified metric-neighborhood exclusion

The bundle includes an exact certificate generator that takes the selected rational candidate and constructs a full five-dimensional trace-gauge box

\[
M(t)=I+t_1\operatorname{diag}(1,0,-1)+t_2\operatorname{diag}(0,1,-1)
+t_3(E_{12}+E_{21})+t_4(E_{13}+E_{31})+t_5(E_{23}+E_{32}).
\]

It chooses an exact rational `epsilon` such that `|t_k|<=epsilon` implies:

1. `M(t)` is positive definite throughout the entire box by the exact bound `max_i sum_j |(M-I)_{ij}| <= 4 epsilon < 1`.
2. Two strict primal unstable vertices, or two strict polar unstable vertices corresponding to stable primal faces, persist throughout the box.

Hence either `U>=2` or `S>=2` everywhere in that complete five-dimensional metric subfamily, globally excluding `S=1,U=1,H=0` there. The exact epsilon and every affine lower bound are stored in the generated certificate and checked independently by `verify_metric_box.py`.

## 7. Reusable artifacts

- Complete result report (`SLOT5_RESULT.md`)
- Complete reproducibility bundle (`slot5_full_orbit_bundle.zip`)
- Bundle manifest with SHA-256 hashes (`slot5_manifest.json`)
- Bundle SHA-256 (`slot5_bundle_sha256.txt`)
- Exact semialgebraic source system (`projective_metric_semialgebraic_system.json`)
- Exact 27-vertex cancellation patch (`reshetov_cancellation_patch.json`)
- Original independent exact verifier (`verify_exact%281%29.py`)

## 8. Conclusion

The decisive correction is that the full mechanically relevant orbit is the eight-dimensional family in equation (1); the earlier unique-centroid-root reduction removed the three projective denominator degrees that the assignment explicitly required. The supplied global searches now cover those degrees and recompute the body's own centroid. They did not yield a strict witness that is asserted here. The rigorous endpoint is therefore the exact `(3,3,4)` interval-certified near-solution, its precise transfer walls, and an exact full-dimensional metric-neighborhood exclusion—not a claimed global exclusion of the entire eight-dimensional orbit.
