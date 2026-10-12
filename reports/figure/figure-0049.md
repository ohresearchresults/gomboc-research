# figure-0049

AI research report · 2026-08-23 UTC

---

# Result of the Conway/polar support-patch direction

## Acceptance status

This direction did **not** produce the required homogeneous polyhedral Gömböc. There is no final object in this result that may be represented as satisfying the research prompt.

The work did, however, produce two reusable materialized branches and a more precise diagnosis of the missing combinatorial operation.

## 1. Strongest low-complexity own-centroid branch

The materialized candidate `VACTIVE_S3_FAST.npz` is a simplicial convex polyhedron with

\[
V=21,\qquad F=38,\qquad E=57,\qquad C=114.
\]

Its actual uniform-volume centroid is

\[
c=(-0.00443580,\;0.00295915,\;0.35954839).
\]

Relative to this actual centroid, its exhaustive classification is

\[
(S,U,H)=(2,2,2).
\]

The intended equilibria are robust:

- intended stable face \(\{6,7,15\}\): margin \(0.0101118291\);
- intended unstable vertex \(0\): margin \(0.9202658652\).

The extra equilibria are a coupled wall configuration:

- extra stable face \(\{9,10,13\}\): margin \(+1.499529\times10^{-9}\);
- adjacent face \(\{2,9,10\}\): margin \(-1.151381\times10^{-9}\);
- extra unstable vertex \(20\): margin \(+1.725460\times10^{-7}\);
- neighboring vertex \(17\): margin \(-1.682427\times10^{-7}\);
- saddle edge \((1,8)\): margin \(0.1845175766\);
- saddle edge \((6,14)\): margin \(0.0150264915\).

Thus the tiny face and vertex signs are transfer walls, whereas the two saddles are genuine, open critical points. Flipping only the nearly coplanar circuits transfers equilibria to adjacent cells and does not remove the saddles.

## 2. Explicit Morse-connection map

A face-gradient and vertex-gradient trace was implemented for the 21-vertex candidate. It identifies the complete cancellation corridors.

For saddle edge \((1,8)\):

- the first descending branch reaches the extra stable face through
  \[
  8\to2\to4\to9;
  \]
- the second descending branch reaches the intended stable face through
  \[
  25\to26\to27\to31\to34;
  \]
- endpoint \(1\) ascends to intended maximum \(0\);
- endpoint \(8\) has ascending routes to both maxima, with the greedy route
  \[
  8\to12\to20.
  \]

For saddle edge \((6,14)\):

- the first descending branch reaches the extra stable face through
  \[
  20\to16\to12\to10\to9;
  \]
- the other reaches the intended stable face directly through
  \[
  37\to34;
  \]
- endpoint \(14\) ascends to the extra maximum through vertex \(17\);
- endpoint \(6\) has routes to both maxima.

This demonstrates that the required operation is not a diagonal flip at either transfer wall. It must replace an entire separatrix-spanning corridor so that one saddle is cancelled with the extra minimum and the other with the extra maximum.

## 3. Asymmetric multi-face support patch

A second branch retained the mechanically correct Conway-derived reference point and changed the local support combinatorics instead of repeatedly crossing the same fixed-topology wall.

The starting materialized H-polytope for this stage, `IBATCH7K30_SPARSE.npz`, had

\[
V=156,\qquad F=80,\qquad E=234,\qquad C=468,
\]

and strict equilibrium count

\[
(S,U,H)=(1,1,0)
\]

relative to the origin. Its uniform centroid was

\[
c=(0.00734754,\;0.00037133,\;0.12595215),
\]

with mechanical margin approximately

\[
2.90768\times10^{-5}.
\]

A new asymmetric outward patch was then constructed simultaneously across six near-critical lower support faces. This is materially different from the earlier balancing polygon or one-face transfer-wall sweeps: six independently shifted cap vertices alter the local face lattice at once.

After genericizing the resulting non-simple cap while preserving strict origin-relative mechanics, the materialized candidate `MCAP8_GEN.npz` has

\[
V=264,\qquad F=134,\qquad E=396,\qquad C=792.
\]

It remains strictly

\[
(S,U,H)=(1,1,0)
\]

relative to the origin, with margin

\[
4.332178\times10^{-5},
\]

and its uniform centroid is

\[
c=(0.00537814,\;-0.00089285,\;0.11681757).
\]

The asymmetric cap therefore reduced the centroid displacement while increasing, rather than consuming, the mechanical robustness margin. This refutes the narrower hypothesis that every continuation from the Conway reference must terminate immediately at the observed transfer walls. It does **not** finish the task because the remaining centroid displacement is still substantial.

## 4. Reproducible artifacts

- `VACTIVE_S3_FAST.npz`: low-complexity own-centroid \((2,2,2)\) candidate.
- `morse_trace.py`: traces the two descending and ascending separatrix systems.
- `vertex_suh_active.py`: fixed-topology solver including explicit edge-saddle components \(t,1-t,\lambda_1,\lambda_2\).
- `face_cap_search.py`: single asymmetric outward-cap search.
- `multi_face_cap_search.py`: simultaneous six-face cap-combinatorics search.
- `genericize_hpoly.py`: converts a non-simple cap result to a strict simple H-polytope while preserving the origin-relative equilibrium class.
- `hpoly_scp_sparse.py`: sparse active-set continuation of support distances and the volume centroid.
- `MCAP8_GEN.npz`: strongest materialized asymmetric-support candidate from this direction.

## 5. Missing parts of the requested deliverable

The remaining displacement

\[
\lVert c\rVert\approx0.1169447
\]

means `MCAP8_GEN.npz` is not a homogeneous Gömböc. Therefore this direction has no valid final rational coordinates, exact own-centroid equilibrium certificate, OBJ, STL, or reproducible final archive. Producing those files for the present candidate would only certify the wrong reference point.
