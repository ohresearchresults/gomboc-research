# figure-0036

AI research report · 2026-08-22 UTC

---

# Complete resolution of the seven-vertex remainder

## Result

All **869 rooted automorphism orbits** left by the previous seven-vertex classification are now exactly excluded. They represent all **1,714 labeled survivor systems**. The new layer contains **5,341 exact branch certificates**; none remains unresolved. Combined with the prior 137,922 exact certificates, this closes all

\[
137{,}922+1{,}714=139{,}636
\]

seven-vertex shadow-tree/tetrahedron systems.

**Certificate-verified theorem:** every full-dimensional homogeneous convex polyhedron in \(\mathbb R^3\) with a unique nondegenerate unstable equilibrium has at least **eight vertices**. Therefore every strict homogeneous polyhedral Gömböc has at least eight vertices.

The current published framework supplies the rooted shadow-tree reduction and the root-cone tetrahedral decomposition, and explicitly reports that its original quadratic certificate leaves roughly one percent of the seven-vertex systems unresolved. :contentReference[oaicite:0]{index=0} The present result closes exactly that finite remainder.

**Complete reusable artifact:** [v7_complete_exclusion_artifact.zip](sandbox:/mnt/data/v7_complete_exclusion_artifact.zip)  
ZIP SHA-256: `3a1a9121c74b3bc27b2d1aff773567fc1f4cfbf3ab02d0e64642ab06bef776c6`

Principal files:

- [Theorem and proof](sandbox:/mnt/data/v7_complete_exclusion/THEOREM_AND_PROOF.md)
- [Machine-readable theorem summary](sandbox:/mnt/data/v7_complete_exclusion/v7_exclusion_summary.json)
- [All 869 orbit certificates](sandbox:/mnt/data/v7_complete_exclusion/v7_moment_exclusion_certificate.json)
- [Explicit mapping of all 1,714 labeled survivors](sandbox:/mnt/data/v7_complete_exclusion/v7_survivor_orbit_mapping.json)
- [Independent exact Fraction verifier](sandbox:/mnt/data/v7_complete_exclusion/verify_v7_moment_exclusion_independent.py)
- [Saved independent verification](sandbox:/mnt/data/v7_complete_exclusion/v7_moment_independent_verification.json)
- [Expanded sample branch certificate](sandbox:/mnt/data/v7_complete_exclusion/v7_moment_sample_branch.json)
- [Manifest](sandbox:/mnt/data/v7_complete_exclusion/MANIFEST.json)
- [Checksums](sandbox:/mnt/data/v7_complete_exclusion/SHA256SUMS.txt)

## The decisive exact centroid consequence

Normalize a hypothetical seven-vertex example by translating its true uniform-volume centroid to zero and rotating/scaling its unique unstable root to

\[
r=(1,0,0).
\]

For a simplicial realization, cone \(r\) to every triangular face not incident with it. These tetrahedra form a partition \(\mathcal D\), with strictly positive determinant volumes \(\Delta_T/6\). The **full degree-four centroid equation** is

\[
\boxed{\sum_{T\in\mathcal D}\Delta_T\sum_{v\in T}r_v
      =4\operatorname{Vol}(P)c(P)=0.}
\]

The earlier relaxation used only its first coordinate, equivalently its dot product with the normalized root. The new step retains the same identity in every vertex direction. For each vertex \(j\),

\[
0=\sum_{T\in\mathcal D}\Delta_T
\left(r_j\cdot\sum_{v\in T}r_v\right),
\qquad \Delta_T>0,
\]

so at least one tetrahedron obeys

\[
\boxed{r_j\cdot\sum_{v\in T}r_v\le0.}
\]

This is a finite disjunction of quadratic inequalities and is an exact consequence of the true degree-four centroid equation—there is no numerical centroid penalty or approximation.

## Exact certificate for each branch

Every survivor orbit already specifies:

1. a maximal planar seven-vertex graph;
2. a representative unstable root;
3. a rooted shadow tree with six inequalities
   \[
   (r_i-r_{p(i)})\cdot r_i\le0;
   \]
4. a selected root-moment tetrahedron \(T_0\) satisfying
   \[
   r\cdot\sum_{v\in T_0}r_v\le0.
   \]

For each orbit, the new certificate chooses one nonroot **killing vertex** \(j\). It branches over every root-cone tetrahedron \(T\), because one must satisfy the new vertex-moment inequality. With the root eliminated, the 18 remaining coordinates and the homogenizing constant form \(z=(1,x)\in\mathbb R^{19}\). The six shadow forms, root-moment form, and vertex-moment form are

\[
f_k(x)=z^{\mathsf T}H_kz\le0,\qquad k=1,\ldots,8.
\]

For every branch, the bundle stores positive integer weights \(w_k\) for which

\[
A=\sum_{k=1}^{8}w_k(2H_k)
\]

is an exact positive-definite integer matrix. Hence

\[
2\sum_{k=1}^{8}w_k f_k(x)=z^{\mathsf T}Az>0
\]

for every \(x\), contradicting simultaneous nonpositivity of the eight necessary inequalities. All tetrahedral branches are excluded for the chosen \(j\), so the orbit is excluded.

## Orbit-complete accounting

| graph | graph6 | survivor systems | rooted orbits | new branch certificates | unresolved |
|---:|---|---:|---:|---:|---:|
| 0 | `F~nR_` | 194 | 91 | 594 | 0 |
| 1 | `Fv|Xo` | 360 | 152 | 959 | 0 |
| 2 | `Fek~w` | 444 | 420 | 2,568 | 0 |
| 3 | `FJn^W` | 456 | 156 | 930 | 0 |
| 4 | `Fhf~o` | 260 | 50 | 290 | 0 |
| **total** | all types | **1,714** | **869** | **5,341** | **0** |

`v7_survivor_orbit_mapping.json` gives every original survivor key, its representative orbit ID, and an explicit root-fixing graph automorphism carrying the representative to that labeled system. Internal SHA-256: `817ac2e44341bc802c2cc930cb2786c5d55d505cb1d8fa051522be7f8bfa293b`.

The complete moment bundle has internal SHA-256 `9c98db2436796ac22b99804e829db55a58d9aab6c8a54f00bd2ecc8f75251fb3`; the prior partition bundle has internal SHA-256 `d13260088b7a769ffb0d48f4e62b514d3cbb3cd91c8a1e026bf774499e4eb39a`.

## Independent exact verification

Two exact arithmetic paths verify all 5,341 matrices:

- `verify_v7_moment_exclusion.py` uses fraction-free Bareiss/Sylvester elimination; the smallest positive pivot is `42`.
- `verify_v7_moment_exclusion_independent.py` reconstructs every 19-by-19 matrix independently and performs exact \(LDL^{\mathsf T}\) over `fractions.Fraction`. Its smallest diagonal value is
  \[
  \frac{72430057077062129}{81521192437027616}>0.
  \]

The independent run also rechecks both bundle self-hashes, every graph6 identifier, every rooted tree, every root tetrahedron, every branch set, all 869 orbit IDs, all multiplicities, and the exact total of 1,714 covered systems.

## Why full realization, stable-face, and no-saddle chambers cannot reopen a case

The certified system is a relaxation containing every actual convex realization. A genuine realization supplies positive tetrahedral volumes and therefore satisfies every centroid-moment disjunction. A Gömböc must first satisfy the necessary condition \(U=1\). Since even that relaxed necessary system is empty for every seven-vertex type, adding strict convexity determinants, one stable-face chamber, and no-saddle edge disjunctions only shrinks an already empty set.

For completeness, the artifact retains the independent rational polyhedron verifier and the complete face, vertex, and edge predicates. The transcript correctly required exact tetrahedral centroid sums, strict orientation tests, unstable-vertex dot products, convexity determinants, and positive margins rather than floating-point classification. :contentReference[oaicite:1]{index=1}

After centering:

- a face is stable iff every exact oriented projection sign \(\Phi(F,i)>0\);
- a vertex is unstable iff \(-v\cdot(w-v)>0\) for every adjacent \(w\);
- an edge is a saddle iff its projection parameter is strictly interior and both adjacent-normal cone coefficients are positive.

Those predicates are unnecessary for the exclusion proof because contradiction already occurs at the prerequisite \(U=1\), but `exact_polyhedron_verifier.py` remains available for any future eight-vertex candidate.

## Reproduction

From the extracted artifact directory, run:

`./verify_remainder.sh`

It performs the independent exact Fraction audit, the separate Bareiss audit, and reconstructs the complete 1,714-to-869 orbit mapping. The archived successful audit reports 869 orbits, 1,714 systems, 5,341 branch certificates, and zero remainder.

## Conclusion

There is no seven-vertex strict homogeneous polyhedral Gömböc. More strongly, there is no seven-vertex homogeneous convex polyhedron with a unique nondegenerate unstable equilibrium. The requested figure, if it exists, must have at least eight vertices.
