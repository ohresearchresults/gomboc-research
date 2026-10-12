# figure-0029

AI research report · 2026-08-22 UTC

---

# Explicit full-basin maximum–saddle cancellation for Reshetov’s 14-face polyhedron

## Verdict

I obtained an **exact rational replacement of the complete basin of Reshetov’s extra unstable vertex**. Relative to Reshetov’s original uniform centroid, the modified convex polyhedron has the strict equilibrium structure

\[
(S,U,H)=(1,1,0)
\]

with a normalized minimum sign margin of

\[
2.8957131465\times 10^{-5}.
\]

This is a genuine maximum–saddle cancellation: the entire graph component containing the extra maximum, bounded by the two exact separatrices from the unique saddle to the unique stable face, is removed and replaced by a rational monotone patch. It is not a one-vertex truncation.

The remaining obstruction is the homogeneous-centroid condition. The replacement removes too much volume from the positive-x side, so the new polyhedron’s own uniform centroid moves far from Reshetov’s centroid. Relative to its own centroid, the candidate is not a Gömböc. Consequently, I do **not** claim a strict homogeneous \((1,1)\) result.

What is complete is the requested fallback artifact: exact reconstruction, exact basin boundary, an explicit rational patch with a strict fixed-center certificate, exact centroid residual equations, a three-parameter exact correction family with full-rank Jacobian, and the finite inequalities that remain to be preserved during centroid correction.

Reshetov’s primary construction is indeed a 14-face homogeneous monostable polyhedron proved using rational arithmetic. Lángi’s approximation theorem establishes existence of centered polyhedral bodies with prescribed nondegenerate equilibria and supplies the theoretical remote-cap correction mechanism, but its parameter choices are non-explicit and local. The earlier transcript correctly isolated full-basin replacement, rather than vertex truncation, as the remaining operation.

## 1. Exact reconstruction of the starting polyhedron

The Reshetov polyhedron is reconstructed as

\[
P_R=\{x\in\mathbb R^3:n_i\cdot x\le \lVert n_i\rVert^2,\ 1\le i\le14\},
\]

with the exact integer normals

```text
(19, 70,-410)
( 0,289,-186)
(-26,-389, -2)
(-6,207,-331)
(13,-329,101)
( 1,-167,233)
(-5,-263,181)
( 0,-73,253)
(-27,-85,-443)
( 0,107,201)
( 0,181,103)
( 0,287,-27)
(32,-394,-134)
( 0,18,244)
```

Triple-plane intersection and exact half-space testing give

\[
V=24,\qquad E=36,\qquad F=14.
\]

Its exact rational uniform centroid is stored in the certificate; numerically,

\[
C_R\approx(-104.1014775785565,\ 8.465022473324968,\ -47.56244776570032),
\]

and

\[
\operatorname{Vol}(P_R)\approx2.646251542093565\times10^9.
\]

Exact reconstruction followed by equilibrium classification gives

\[
(S,U,H)=(1,2,1).
\]

The critical elements are:

- unique stable face: face 11;
- principal unstable vertex: \(v_1\);
- extra unstable vertex: \(v_{24}\);
- unique saddle edge: \([v_{10},v_{15}]\), with saddle parameter
  \[
  t=0.38982498611359956\ldots .
  \]

Normalized starting margins are:

| Condition | Margin |
|---|---:|
| stable face 11 | \(+2.7882372387\times10^{-2}\) |
| nearest other face | \(-3.7535621009\times10^{-5}\) |
| unstable vertex \(v_1\) | \(+9.9077725326\times10^{-1}\) |
| extra unstable vertex \(v_{24}\) | \(+9.2845652326\times10^{-1}\) |
| saddle edge \([v_{10},v_{15}]\) | \(+2.7992108730\times10^{-2}\) |

The exact reconstruction code is reshetov_core.py.

## 2. Exact saddle and complete basin boundary

Let coordinates below be relative to \(C_R\). The projection of \(C_R\) to the unique stable face is

\[
p=(0,\ 195.05082113090504\ldots,\ 110.99577114079126\ldots),
\]

while the saddle point on \([v_{10},v_{15}]\) is

\[
q=(6.979759393855647\ldots,\ -324.38312248667796\ldots,\ -346.85668340332467\ldots).
\]

All coordinates are exact rational numbers in the boundary artifact.

The two descending separatrices from \(q\) to \(p\) traverse the following face sequences:

\[
A:\quad9\to1\to4\to2\to12\to11,
\]

\[
B:\quad13\to3\to5\to7\to6\to8\to14\to10\to11.
\]

Their crossed edges are

```text
A: [11,15], [11,16], [7,16], [7,17], [3,21]
B: [10,13], [12,13], [12,14], [9,14], [9,18], [6,19], [4,22], [2,23]
```

Together with the saddle edge \([10,15]\), deleting these fourteen edges splits the original one-skeleton **exactly** into

\[
\{v_1,\ldots,v_{12}\}
\quad\sqcup\quad
\{v_{13},\ldots,v_{24}\}.
\]

The second component contains the extra unstable vertex \(v_{24}\). Thus the operation removes its complete discrete basin, not merely a neighborhood of the maximum.

The boundary loop, in cyclic order, is

\[
q,A_1,A_2,A_3,A_4,A_5,p,B_9,B_8,B_7,B_6,B_5,B_4,B_3,B_2.
\]

Its complete exact coordinates are in exact_separatrix_boundary.json. The exact derivation is in separatrix_exact.py.

## 3. Explicit rational monotone replacement patch

Start with the twelve retained original vertices \(v_1,\ldots,v_{12}\), append the fifteen exact boundary points above, and perturb four boundary vertices by the following rational vectors:

| Candidate vertex | Boundary label | Exact displacement |
|---:|---|---|
| 13 | \(q\) | \((83/100,\ 195/100,\ 197/100)\) |
| 18 | \(A_5\) | \((-61/100,\ -198/100,\ 128/100)\) |
| 19 | \(p\) | \((88/100,\ -199/100,\ -197/100)\) |
| 20 | \(B_9\) | \((-3/100,\ -166/100,\ -198/100)\) |

Take the convex hull. Exact facet enumeration gives

\[
V=27,\qquad E=58,\qquad F=33,
\]

and mechanical complexity

\[
C_{
m mech}=V+E+F-2=116.
\]

All 27 rational coordinates and all 33 face cycles are in certificate.json. The corresponding visualization mesh is strict_fixed_center_patch.obj.

### Strict equilibrium certificate relative to \(C_R\)

Exact integer/rational sign evaluation gives

\[
(S,U,H)=(1,1,0).
\]

The unique stable face is certificate face 25, with vertex cycle \([27,15,19]\), and the unique unstable vertex is the retained principal maximum \(v_1\).

The normalized margins are:

| Condition | Margin |
|---|---:|
| intended stable face | \(+7.5422296420\times10^{-3}\) |
| nearest other face | \(-5.9684623782\times10^{-5}\) |
| intended unstable vertex | \(+9.9077725326\times10^{-1}\) |
| nearest other vertex | \(-5.2765099435\times10^{-4}\) |
| closest interior edge to becoming a saddle | \(-2.8957131465\times10^{-5}\) |

Therefore the strict certificate score is

\[
\boxed{2.8957131465\times10^{-5}}.
\]

The certificate contains, as exact fractions:

1. every face-edge projection sign;
2. every directed vertex-edge radial sign;
3. every interior-edge saddle test and its maximizing witness vertex;
4. an explicit successor map in which every nonmaximum vertex has an adjacent vertex of strictly larger squared distance from \(C_R\), and every successor path terminates at \(v_1\).

This last item is the discrete monotonicity certificate for the replacement patch: no vertex in the substituted basin can inherit the removed maximum.

The generator and exact assertions are in strict_patch_exact.py.

## 4. Before/after comparison

| Quantity | Original Reshetov polyhedron | Full-basin replacement |
|---|---:|---:|
| vertices | 24 | 27 |
| edges | 36 | 58 |
| faces | 14 | 33 |
| equilibria relative to \(C_R\) | \((1,2,1)\) | **\((1,1,0)\)** |
| stable margin | \(2.7882\times10^{-2}\) | \(7.5422\times10^{-3}\) |
| extra-maximum margin | \(+9.2846\times10^{-1}\) | eliminated; nearest other vertex \(-5.2765\times10^{-4}\) |
| saddle margin | \(+2.7992\times10^{-2}\) | eliminated; nearest edge \(-2.8957\times10^{-5}\) |

Thus the local Morse cancellation itself is complete and strict.

## 5. Exact centroid audit

The modified polyhedron’s exact uniform centroid is stored as a rational vector in the certificate. Numerically,

\[
C_{\rm patch}\approx
(-2589.6385146523567,\ 10.129056745597389,\ -50.441025273326).
\]

Hence

\[
C_{\rm patch}-C_R\approx
(-2485.537037073800,\ 1.664034272272,\ -2.878577507626).
\]

This is not a small perturbation. A separate numerical classification relative to \(C_{\rm patch}\) gives

\[
(S,U,H)=(8,4,10),
\]

so the rational patch is **not** a homogeneous polyhedral Gömböc. This negative conclusion is not a floating-point ambiguity: the centroid mismatch itself is an exact nonzero rational vector. The \((8,4,10)\) count is included only as a numerical diagnostic of the consequence.

## 6. Exact centroid-correction equations

For the fixed oriented boundary triangulation, define

\[
D=\sum_T\det(a_T,b_T,c_T),
\qquad
V=\frac{D}{6},
\]

and

\[
M=\sum_T\det(a_T,b_T,c_T)(a_T+b_T+c_T).
\]

The uniform centroid is

\[
c=\frac{M}{4D}.
\]

Therefore restoring the original reference center requires the exact vector equation

\[
\boxed{R=M-4C_R D=0.}
\]

A concrete three-parameter correction family is supplied:

- move candidate vertex 13, the perturbed saddle point \(q\), by \((\xi,0,0)\);
- move candidate vertex 19, the perturbed stable projection \(p\), by \((0,\eta,0)\);
- move candidate vertex 20, the point \(B_9\), by \((0,0,\zeta)\).

With the current triangulation fixed, every component of

\[
R(\xi,\eta,\zeta)
\]

is an exact multi-affine polynomial of degree at most three. The script evaluates it entirely with `Fraction` arithmetic. The certificate records

- \(R(0,0,0)\) exactly;
- the exact \(3\times3\) Jacobian at zero;
- its exact determinant.

The determinant is nonzero; its numerator has 9264 decimal digits. Consequently, the centroid map has full local rank at the strict patch. There is no infinitesimal rank obstruction to exact centroid correction.

However, the residual is too large for this local three-vertex family. No root was certified inside the neighborhood in which the hull topology and the three active equilibrium bottlenecks remain strict. A formal numerical root of the fixed-triangulation polynomial occurs only after displacements of order \(10^4\)–\(10^5\), where the prescribed topology is already invalid. It therefore cannot be used as a candidate.

The three equilibrium bottlenecks that must remain on the correct side during a future correction are now explicit:

\[
\begin{aligned}
&\text{nearest nonstable face}<0 &&\text{with slack }5.96846\times10^{-5},\\
&\text{nearest nonmaximum vertex}<0 &&\text{with slack }5.27651\times10^{-4},\\
&\text{nearest nonsaddle edge}<0 &&\text{with slack }2.89571\times10^{-5}.
\end{aligned}
\]

All remaining equilibrium inequalities have larger slack. Thus any subsequent centroid operation can be audited against a finite, exact active set rather than re-discovering the cancellation.

## 7. What was proved and what was not

### Proved exactly

- Reshetov’s support-plane data reconstruct a 24-vertex, 36-edge, 14-face homogeneous polyhedron with \((S,U,H)=(1,2,1)\).
- The extra maximum is \(v_{24}\), paired with the unique saddle edge \([v_{10},v_{15}]\).
- The two complete saddle-to-minimum separatrices and their rational crossing points were computed.
- Their cut separates the full extra-maximum basin \(v_{13},\ldots,v_{24}\) from the retained component.
- A fully explicit rational replacement has strict \((1,1,0)\) relative to \(C_R\).
- The replacement’s exact volume centroid and exact centroid residual were computed.
- An exact three-control centroid equation with a full-rank Jacobian was produced.

### Not proved

- No explicit homogeneous convex polyhedron with strict \((S,U)=(1,1)\) was obtained.
- The fixed-center rational patch is not itself eligible for the Gömböc complexity prize.
- Lángi’s distant-cap mechanism cannot yet be invoked quantitatively, because it corrects sufficiently small first-moment errors while the present basin replacement creates a large displacement.

## 8. Reusable artifacts

- Exact rational certificate: coordinates, faces, signs, centroid and correction Jacobian (`certificate.json`)
- Exact rational separatrix boundary (`exact_separatrix_boundary.json`)
- OBJ of the strict fixed-center patch (`strict_fixed_center_patch.obj`)
- Exact candidate generator (`strict_patch_exact.py`)
- Exact Reshetov reconstruction (`reshetov_core.py`)
- Exact separatrix derivation (`separatrix_exact.py`)

## 9. Strongest next direction

The decisive next operation is not another local perturbation of the low replacement disk. It must retain substantially more of the removed basin’s first moment while remaining radially monotone—most plausibly by replacing a larger region with a monotone corridor whose boundary reaches the surviving maximum. Once the centroid residual is reduced below the explicit \(2.8957\times10^{-5}\) equilibrium neighborhood, the exact three-control system or Lángi’s four remote caps can be used for the final exact correction.
