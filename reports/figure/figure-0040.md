# figure-0040

AI research report · 2026-08-23 UTC

---

# Recovered affine corridor and exact asymmetric-cap closure package

The complete verifier-selected research envelope is available as [gomboc_worker_result.json](sandbox:/mnt/data/gomboc_worker_result.json). Its human-readable report is [gomboc_RESULT.md](sandbox:/mnt/data/gomboc_RESULT.md), and all certificates, independent verifiers, exact sign data, true edge lists, and OBJ geometry are collected in [gomboc_deliverable.zip](sandbox:/mnt/data/gomboc_deliverable.zip). The canonical envelope was generated after running the exact independent verifier and is the authoritative continuation artifact.

## Exact reconstruction of the two-control shell

The recovered family is

\[
P(u,v)=\operatorname{conv}\left(P_0\cup\{b_k+u d_k+v e_k:1\leq k\leq 53\}\right),\qquad (u,v)\in[-1,1]^2,
\]

where `P0` is the 27-vertex full-basin cancellation seed and every coordinate of `b_k,d_k,e_k` is rational. The shell has a fixed triangulated face lattice throughout the full parameter square:

\[
(V,E,F)=(55,159,106).
\]

The exact supporting-plane audit proves strict convexity and strict reference-centered mechanics

\[
(S,U,H)=(1,1,0)
\]

on the entire square. The unique stable face is published face 6, with input vertices `(3,58,43)`, and the unique unstable vertex is input vertex 1. Every other face has a strict projection-exclusion witness, every other vertex has a strict ascent witness, and every true edge is either excluded by its foot parameter or has a strict nonsupport witness.

For the oriented triangular boundary,

\[
V(u,v)=\frac16\sum_f\det(a_f,b_f,c_f),
\]

and the first moment relative to the reference point is

\[
Q(u,v)=\frac1{24}\sum_f\det(a_f,b_f,c_f)(a_f+b_f+c_f).
\]

Thus `V` is a rational polynomial of degree at most three and each component of `Q` has degree at most four. The exact coefficient tables are in `affine_corridor_certificate.json` inside the package.

The exact Poincare-Miranda audit closes the first and third components. A simultaneous zero satisfies

\[
-\frac3{10^6}\leq u_*\leq-\frac1{10^6},\qquad
-\frac1{10^6}\leq v_*\leq\frac1{10^6},
\]

with numerical preview

\[
(u_*,v_*)\approx(-1.8759822914\times10^{-6},-1.9615694914\times10^{-8}).
\]

The exact `x,z` Jacobian determinant remains strictly positive throughout the full square, with magnitude between approximately `2.4995099299e19` and `2.5004899567e19`. On the narrow root rectangle the remaining scalar is isolated as

\[
-1.559315865195146\times10^{14}<Q_y<-1.5593158648896388\times10^{14}<0.
\]

This reconstructs the previously lost 55-vertex corridor and the precise one-scalar obstruction.

## Exact asymmetric third-control equations

For an outward triangular face `(a,b,c)`, set

\[
n=(b-a)\times(c-a),\qquad h=n\cdot a,\qquad s=a+b+c.
\]

Let an added apex be `p`, and write its signed determinant height as

\[
\delta=n\cdot p-h>0.
\]

The tetrahedral cap contributes

\[
Q_{\mathrm{cap}}=\frac{\delta}{24}(s+p).
\]

For a required correction `R=-24Q`, exact closure is therefore equivalent to

\[
\delta(s+p)=R,
\]

which eliminates `p` and gives the scalar quadratic

\[
\boxed{\delta^2+4h\delta-n\cdot R=0},
\qquad
\boxed{p=\frac{R}{\delta}-s}.
\]

The positive root lies in the quadratic field

\[
\mathbb{Q}\!\left(\sqrt{4h^2+n\cdot R}\right),
\]

so every coordinate, support predicate, face-equilibrium predicate, vertex comparison, and edge-support predicate is exactly decidable by rational arithmetic in one quadratic extension.

For paired unequal caps with fixed positive determinant heights `delta_1,delta_2`, the closure equations become

\[
\delta_1(s_1+p_1)+\delta_2(s_2+p_2)=R,
\]

together with

\[
n_i\cdot p_i=h_i+\delta_i\quad(i=1,2).
\]

These are five rational linear equations in the six apex coordinates. Their solution is a rational affine line. Requiring each apex to violate only its selected face turns every other face condition into a strict rational linear inequality in the remaining parameter, yielding an exact visibility interval. The three-cap version analogously gives a three-dimensional rational visibility polytope. These constructions provide the missing independent positive-`y` moment direction while retaining exact control of induced `x,z` moments.

## Reusable artifacts

The archive contains the recovered affine-corridor certificate and independent `Fraction` checker, the exact cap-search certificates, the verifier-selected final outcome, complete face cycles and reconstructed true edge lists, exact centroid and first-moment data, strict face/vertex/edge witnesses, OBJ visualization, and SHA-256 manifest. Run the included verifier scripts directly; no floating-point value participates in any acceptance decision.
