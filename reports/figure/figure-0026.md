# figure-0026

AI research report · 2026-08-22 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Result

## Bottom line

I completed the exact-certification direction and implemented it as an executable package. I did **not** obtain a homogeneous 21-face polyhedral Gömböc: no rational halfspace list in this run passes the exact test at its own uniform-volume centroid with `(S,U,H)=(1,1,0)`. The strongest search state is instead an exact rational 21-face polytope that is `(1,1,0)` relative to a supplied auxiliary point, while its exact volume centroid gives `(18,25,41)`. It is therefore a rigorous continuation seed, not the requested final figure.

This distinction follows the standard polyhedral definition: equilibrium is relative to the uniform-volume centroid; stable, saddle, and unstable equilibria lie in relative interiors of faces, edges, and vertices, respectively. The Conway–Domokos–Kovács 21-vertex/21-face construction that supplied the starting normals is explicitly a **0-skeleton with equal point masses**, not a homogeneous 3-skeleton. The v1 construction data also give the top-vertex correction `h = sin²(alpha_1) tan²(pi/k)` and the `P_(4,5)` angle row used in the reconstruction.

The earlier transcript had already isolated the right finite objects—exact tetrahedral centroid sums and exact face/vertex tests—and the fixed-normal polar support family. This result makes that route complete, adds the missing edge test, adds a complete face-lattice proof, and supplies working rational and interval verifiers.

## Exact certificate

Input is a finite list of rational halfspaces

`P = {x in R^3 : q_i·x <= h_i, i=0,...,m-1}`,

with the intended family having `m=21`.

### 1. Exact vertices, incidences, convexity, and completeness

For every triple `I=(i,j,k)`, form the 3×3 matrix with rows `q_i,q_j,q_k` and solve

`v_I = A_I^{-1}(h_i,h_j,h_k)^T`

by exact Cramer's rule. For `m=21`, all `C(21,3)=1330` triples are examined. A nonsingular intersection is retained exactly when every slack

`s_(I,l) = h_l - q_l·v_I`

is nonnegative. Equal rational points are deduplicated, and incidence is recomputed from the zero slacks.

For the generic Conway-polar certificate the verifier requires:

- every retained vertex has exactly three incident facets;
- every nonincidence slack is strictly positive;
- all 21 halfspaces are active;
- two vertices are adjacent exactly when their incidence sets share two facets;
- every vertex has degree three;
- every face graph is one polygonal cycle;
- `V-E+F=2`;
- boundedness is certified by strictly positive rational weights with `sum lambda_i q_i=0`.

This exhausts all possible triple intersections and proves that no unlisted vertex, edge, or facet exists.

### 2. Exact volume and centroid

Orient every exact face cycle by its outward normal and fan-triangulate it. For all oriented boundary triangles `(a,b,c)`, define

`D = sum det(a,b,c)`

and

`N = sum det(a,b,c)(a+b+c)`.

Then exactly

`Vol(P) = D/6`

and

`centroid(P) = N/(4D)`.

The proof is the signed-tetrahedron decomposition: tetrahedron `(0,a,b,c)` has signed volume `det(a,b,c)/6` and centroid `(a+b+c)/4`. The checker requires `D>0`.

After translation to the exact centroid `c`, write

`y_v = v-c`, and `H_i = h_i-q_i·c`.

All translated supports must be strictly positive.

### 3. Stable faces

The orthogonal projection of the origin to translated face `i` is

`p_i = H_i q_i/(q_i·q_i)`.

After clearing its positive denominator, face `i` is a strict stable equilibrium exactly when

`F_(i,j) = (q_i·q_i)H_j - H_i(q_i·q_j) > 0`

for every `j != i`.

A nonstable face is certified by one explicit witness `j` with `F_(i,j)<0`. Any zero is rejected as a degeneracy.

### 4. Unstable vertices

A vertex `v` is a strict unstable equilibrium exactly when its radial plane supports the polytope only at `v`, equivalently

`U_(v,w) = y_v·(y_v-y_w) > 0`

for every other vertex `w`.

Every nonunstable vertex carries one exact witness `w` with `U_(v,w)<0`; zeros are rejected.

### 5. Edge equilibria and their exclusion

For translated edge endpoints `a,b`, put

`d=b-a`, `L=d·d`, and `tau=-a·d`.

The perpendicular foot on the edge line is

`x = a + (tau/L)d`.

It lies in the relative interior exactly when `0<tau<L`. Set the denominator-cleared foot

`X = L a + tau d = Lx`.

For every nonendpoint vertex `w`, define

`E_(e,w) = X·(Lw-X) = L^2 x·(w-x)`.

The edge is a strict saddle equilibrium exactly when

`0<tau<L` and `E_(e,w)<0` for every nonendpoint vertex `w`.

Every non-equilibrium edge therefore has a finite exact witness of one of three types:

1. `tau<0`;
2. `tau>L`;
3. some vertex has `E_(e,w)>0`, so the perpendicular plane is not supporting.

Thus the certificate explicitly rules out every edge; it never infers `H=0` merely from the face and vertex counts.

## Rationalization and precision guarantee

Vertices must **not** be rounded independently. Round `(q_i,h_i)` to rational or dyadic values, then solve every vertex again exactly. This preserves coplanarity by construction.

For a quick a priori topology budget, let

`kappa_I = ||A_I^{-1}||_infinity` and `R_I = ||v_I||_infinity`.

If every normal coordinate changes by at most `eps_q`, every support by at most `eps_h`, and

`3 kappa_I eps_q < 1`,

then

`||v'_I-v_I||_infinity <= B_I`

with

`B_I = kappa_I (eps_h + 3 eps_q R_I)/(1-3 kappa_I eps_q)`.

A nonincidence slack changes by at most

`Delta s_(I,j) <= eps_h + 3 eps_q R_I + (||q_j||_1+3 eps_q)B_I`.

Consequently `s_(I,j)>Delta s_(I,j)` preserves that incidence sign.

The stronger executable test surrounds every coefficient by an outward-rounded box

`|delta q_(i,k)| <= rho`, `|delta h_i| <= rho`,

re-solves all intended vertices by interval Cramer's rule, encloses the exact volume centroid, and reevaluates every face, vertex, and edge witness. The intended dual triangles are also checked to form a closed Euler sphere; because every listed triangle remains a strict supporting facet, that sphere is the complete dual hull boundary. A passing interval report therefore proves that **every** point in the coefficient box has the same face lattice and equilibrium classification.

If the report returns `rho=2^(-k)`, nearest dyadic rounding with denominator `2^b` is safe for `b>=k`, because its error is at most `2^(-b-1)<rho`. Decimal rounding is safe when `0.5·10^(-p)<rho`. Any pre-existing floating-to-rational residual must be added before comparison.

## Search result in the 21-face family

The supplied fixed-normal continuation searches supports `h_i` while imposing mechanics relative to

`r_t = t·centroid(P(h))`.

`t=0` is the mechanically correct polar reference and `t=1` is the required homogeneous problem.

The best saved fixed-topology run reached

`t = 0.3702368768`

with numerical normalized maximin margin

`1.5187194866886776e-4`

and retained `F=21`, `V=38`, `E=57`.

After dyadic rationalization and complete exact recomputation:

- topology is exactly `(F,V,E)=(21,38,57)`;
- relative to the supplied rational auxiliary point, the exact mechanics are `(S,U,H)=(1,1,0)`;
- relative to the exact uniform-volume centroid, the exact mechanics are `(S,U,H)=(18,25,41)`;
- the Poincaré–Hopf check gives `18+25-41=2`;
- there are no degeneracies in either audit.

The auxiliary `(1,1,0)` certificate survives independent perturbations of every normal coordinate, every support, and every auxiliary-reference coordinate throughout the outward-rounded box

`rho = 2^(-21) = 1/2097152`.

The next larger dyadic box `2^(-20)` fails an edge nonsupport enclosure. Thus 21 dyadic fraction bits, or 7 decimal places under the strict total-error rule, preserve this exact auxiliary certificate.

For the same rational body classified at its own centroid, the entire nonwinning `(18,25,41)` classification survives the box `rho=2^(-26)`.

This is stronger than the shared-context `t≈0.31` state, but it is not a homogeneous Gömböc. The fixed-topology path encounters a bifurcation wall before `t=1`; direct fixed-chamber searches in this run did not find a positive-margin endpoint.

## Executable artifact

- Complete package: exact checker, rationalizer, interval verifier, search code, fixtures, and SHA-256 manifest (`conway_exact_certificate.zip`)
- README and mathematical specification (`README.md`)
- Exact verifier (`verify_exact.py`)
- Complete rational 21-halfspace auxiliary fixture (`conway21_aux_t0370_dyadic22.json`)
- Full exact report (`conway21_aux_t0370_dyadic22.report.json`)
- Auxiliary `(1,1,0)` interval-radius report (`conway21_aux_t0370_dyadic22.aux_interval_fast.max.json`)
- Fixed-topology continuation state (`homotopy_t03702368768.npz`)
- One-command regression audit (`run_all.sh`)

Package SHA-256:

`64094c45bbe1223304332dce803f118ad878389ea4050f7601795efd61229b8b`

## Acceptance procedure for any later numerical `t=1` candidate

1. Save its floating normals and supports as `Q,H`.
2. Round only `Q,H` with `rationalize_halfspaces.py`.
3. Run `verify_exact.py --require-gomboc`.
4. Accept only if it reports exactly one stable face, one unstable vertex, zero edge equilibria, no degeneracy, and no expected-count mismatch.
5. Run `interval_fast.py --find-dyadic` to obtain a coefficientwise rationalization radius.
6. Publish the rational halfspace JSON, exact report, interval report, and package hash together.

The checker is already sufficient to turn a genuine numerical endpoint into a finite publication-grade certificate. What remains unsolved in this direction is the endpoint search itself, not the certification mathematics.
