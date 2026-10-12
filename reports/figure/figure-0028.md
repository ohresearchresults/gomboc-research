# figure-0028

AI research report · 2026-08-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Result: exact exclusion of the adjacent fixed-normal Reshetov programme

## Verdict

I did **not** find an explicit homogeneous polyhedral Gömböc. I did obtain the fallback artifact requested by the assignment: a complete exact exclusion of a meaningful adjacent family, substantially stronger than exclusion of the original support cell.

The supplied transcript had already isolated the exact Reshetov seed as a 14-face, 24-vertex near-miss with 
\[
(S,U,H)=(1,2,1),
\]
and placed the extra maximum next to the sole saddle; it later identified replacement of the full maximum basin through that saddle as the remaining local operation.

The new exact result is:

> **Every strict simple polytopal realization using exactly Reshetov's original 14 normal rays has at least two unstable vertices relative to every interior reference point, including its uniform-volume centroid.**

Consequently, no change of supports, no one-ridge flip, and no sequence of fixed-ray ridge flips or fixed-ray full-basin replacements can produce a homogeneous polyhedral Gömböc. A sufficiently local truncation of either forced maximum also fails: the maximum transfers to a new cut vertex.

The complete machine-checkable package is here:

- Exact exclusion package, including all certificates and verifiers (`gomboc_adjacent_exact_exclusion.zip`)
- Technical note (`README.md`)
- Run every verifier (`[internal-source-reference].sh`)

ZIP SHA-256: `95fc20fe0c02e2c7f91a9ff5eff9224e4329ea2922851df6b8b9b8789a51c9ef`.

## 1. Exact seed audit

Reshetov's Appendix A supplies the 14 integer normals, the face cycles, the 24 incident-normal triples, and the exact rational reconstruction of the vertices; the paper's own Mathematica check uses rational arithmetic.

The normals are

```text
 1  ( 19,   70, -410)       8  (  0,  -73,  253)
 2  (  0,  289, -186)       9  (-27,  -85, -443)
 3  (-26, -389,   -2)      10  (  0,  107,  201)
 4  ( -6,  207, -331)      11  (  0,  181,  103)
 5  ( 13, -329,  101)      12  (  0,  287,  -27)
 6  (  1, -167,  233)      13  ( 32, -394, -134)
 7  ( -5, -263,  181)      14  (  0,   18,  244)
```

with supports \(h_i=\lVert n_i\rVert^2\):

```text
(173361,118117,152001,152446,118611,82179,101955,
 69338,204203,51850,43370,83098,174216,59860).
```

My independent exact audit reconstructs every rational vertex and proves

\[
(V,E,F)=(24,36,14),\qquad(S,U,H)=(1,2,1).
\]

The unique stable face is face 11. The two unstable normal cones are

\[
(1,11,13),\qquad(3,9,11),
\]

and the sole saddle has common normal pair \((9,13)\). The full exact volume, uniform centroid, face cycles, edge list, coordinates, and signs are in the seed audit (`exact_seed_geometry_audit.json`), SHA-256 `f4ac84d13ec6700bdff470247021da78ba6a315d7d5788b605ccaf27f764162a`.

## 2. Support-coordinate and universal-unstable lemma

Translate an arbitrary interior point \(p\) to the origin and write centered supports

\[
d_i=h_i-n_i\cdot p>0.
\]

For a simple vertex with incident-normal triple \(I\), let \(A_I\) be the matrix whose rows are the three normals. Then

\[
v_I=A_I^{-1}d_I.
\]

Writing the vertex direction as a normal-cone combination, \(v_I=A_I^T\lambda\), gives the exact identity

\[
\boxed{\lambda=(A_IA_I^T)^{-1}d_I.}
\]

Therefore, if \((A_IA_I^T)^{-1}\) is entrywise positive, that cone is a strict unstable vertex for **every** positive \(d_I\), hence for every interior point of every realization containing it.

For the two Reshetov cones the exact inverse-Gram matrices are

\[
(A_{1,11,13}A_{1,11,13}^T)^{-1}
=\frac{1}{4250571605792}
\begin{pmatrix}
155507232&1384650336&651528400\\
1384650336&14710025476&6964530398\\
651528400&6964530398&3322436485
\end{pmatrix},
\]

\[
(A_{3,9,11}A_{3,9,11}^T)^{-1}
=\frac{1}{8579995880569}
\begin{pmatrix}
5133575914&2805603000&12305476703\\
2805603000&1605805145&6827167419\\
12305476703&6827167419&29838229794
\end{pmatrix}.
\]

Every numerator is a positive integer. Thus the two maxima are forced by the normal cones, not by the particular supports or centroid.

## 3. Complete exact one-ridge enumeration

All 36 primal edges were processed. The exact classification is

\[
\boxed{13\text{ strict realizable},\quad4\text{ Farkas-infeasible},\quad4\text{ singular},\quad15\text{ nonflippable}.}
\]

The exact manifest is here (`flip_manifest.json`), SHA-256 `dd2a3a50e100ce15e77d5109825b2632cbf6040d7a537945b4f2585bf49c6a75`.

The directly relevant local moves are decisive:

- The saddle-edge flip 17–18 is strict and replaces \((1,9,13),(3,9,13)\) by \((1,3,9),(1,3,13)\), but both forced cones \((1,11,13)\) and \((3,9,11)\) remain.
- Flip 10–16 removes the extra forced cone \((1,11,13)\) but creates forced cone \((11,12,13)\).
- Flip 15–16 removes it but creates forced cone \((1,10,13)\).
- Edge 16–17 is nonflippable because the opposite dual edge \((9,11)\) already exists.

So every one-ridge attempt transfers the extra maximum rather than annihilating it.

For each of the 13 strict fans and each of its 24 possible target vertices, I imposed the exact fan inequalities, target-instability inequalities, and the disjunction that every other vertex must have a negative normal-cone coefficient. A DPLL search reduced every leaf to a homogeneous rational system \(Gd>0\); every leaf carries positive integer Gordan weights \(y\ne0\) with

\[
y^TG=0.
\]

The complete proof has 312 target exclusions and 936 exact Gordan leaves, with no survivor. The certificate is here (`exact_oneflip_exclusion_complete.json`), SHA-256 `6eec536ead6e800a57bc97af91525e2d1de72b95b5b3443f2cc0e2d4358e6eda`; the verifier (`verify_oneflip.py`) reproduces the counts and hashes.

## 4. Global fixed-normal theorem

Let \(\mathcal A\) be the support vectors for which the origin is interior and all 14 inequalities are active facets. Facet \(i\) is active precisely when there is a witness \(x_i\) satisfying

\[
n_i\cdot x_i=d_i,\qquad n_j\cdot x_i<d_j\quad(j\ne i).
\]

Interpolating two support vectors and their witnesses shows that \(\mathcal A\) is convex. A generic path inside \(\mathcal A\) cannot delete a facet and crosses only four-plane concurrence walls; in dimension three these are 2↔2 ridge flips.

I enumerated all \(\binom{14}{3}=364\) triples and all rank-three four-ray circuits exactly:

```text
triples: 364 total; 20 singular; 110 universal-unstable
circuits: 306 type 3+1; 87 type 1+3; 159 type 4+0; 274 type 2+2
```

For every 2+2 circuit, the two local triangulations contain the same number of universal-unstable cones:

```text
187 circuits: 1 -> 1
 87 circuits: 0 -> 0
  0 failures
```

The original fan has two, so every strict simple fan with all 14 rays active has two. Hence

\[
\boxed{U(P,p)\ge2}
\]

for every such polytope and every interior point \(p\). The exact invariant certificate is here (`global_fixed_normal_invariant.json`), SHA-256 `2766f6cc72b53a7d32a5febf1effdec76d91b27dfeb68bc122d563abeb024a9a`; the exact verifier (`verify_global_invariant.py`) recomputes all 364 triples, all 274 relevant circuits, both matrices, and the original strict fan inequalities.

This exhausts not only the original support chamber but the entire strict fixed-normal programme.

## 5. Targeted truncation theorem

Let \(v\) be a strict unstable vertex relative to an interior point \(p\), and truncate it sufficiently close by one plane. Let \(x_j\) be the cut vertices. Along every old edge away from \(v\), the derivative of \(f(x)=\lVert x-p\rVert^2\) remains negative for a close cut. Choose a cut vertex \(x_j\) maximizing \(f\) over the cut face. For every neighboring cut vertex \(x_k\),

\[
2(x_j-p)\cdot(x_k-x_j)
=f(x_k)-f(x_j)-\lVert x_k-x_j\rVert^2<0.
\]

Thus every incident direction at \(x_j\) decreases \(f\), so \(x_j\) is a new strict unstable vertex. For the uniform centroid of the truncated body the argument persists for sufficiently small cuts because the removed cap has vanishing volume and first moment.

Applied to either universal Reshetov maximum, one maximum is inherited by the cut patch while the other universal maximum remains untouched. Therefore every sufficiently local one-plane truncation still has \(U\ge2\). Any stacking or surgery disjoint from both forced cones also leaves both intact.

This does not exclude a genuinely nonlocal full-basin replacement using new normal rays and reaching the saddle; that is the remaining viable family.

## 6. Full exact geometry and centroid audit of every strict adjacent fan

For each of the 13 strict adjacent fans, I supplied an integer support vector and reconstructed all rational vertices. The exact audit verifies face cycles, all incidences, strict convexity, 36 edges, Euler topology, exact positive volume, exact uniform-volume centroid, every face/vertex/edge equilibrium sign, absence of zero predicates, and \(S+U-H=2\).

The centroid classifications of the displayed strict witnesses are:

```text
flip 4–5:   (S,U,H)=(4,2,4)    flip 12–13: (5,2,5)
flip 5–23:  (5,2,5)            flip 15–16: (4,2,4)
flip 6–22:  (3,2,3)            flip 17–18: (8,2,8)
flip 8–9:   (8,2,8)            flip 18–19: (4,2,4)
flip 9–11:  (5,3,6)            flip 20–21: (8,2,8)
flip 10–16: (8,2,8)            flip 21–22: (7,2,7)
flip 11–12: (6,2,6)
```

The complete coordinates and fractions are in the adjacent geometry audit (`exact_adjacent_geometry_audit.json`), SHA-256 `862f5dc78c0a3e6f922fc8d2ff1e3151d217c21ee36d3572738a68d75c7de1c6`; the verifier (`verify_exact_adjacent_audit.py`) recomputes every entry from the source supports.

## Consequence and remaining frontier

There is no surviving semialgebraic support cell to send to a centroid solver in the original 14-ray configuration: the support-independent lower bound \(U\ge2\) kills every cell first. The smallest honest next attack is therefore a one-new-ray stellar subdivision or full basin replacement that modifies the forced cone \((1,11,13)\) and includes the saddle pair \((9,13)\). Such candidates should be filtered in this order:

1. exact universal-cone test;
2. exact circuit/topology realizability;
3. unique-unstable DPLL/Gordan filter;
4. only for survivors, uniform-volume centroid equations and all strict stable/unstable/edge conditions.

No winning polyhedron is claimed. The completed contribution is the exact global exclusion above and the executable certificate package.
