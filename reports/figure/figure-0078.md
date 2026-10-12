# figure-0078

AI research report · 2026-08-26 UTC

---

# Verdict

**No strict homogeneous convex polyhedral Gömböc was found.** The required finite own-centroid class is `(S,U,H)=(1,1,0)`; the strongest exact connected double-Y endpoint is instead a gate-valid `(2,1,1)` body. Two additional exact endpoints expose the attempted cancellation as a sequential Morse-pair transfer and fail the primal inactive-separation gate.

The journal requires an actual uniform-density finite body at its own volume centroid, with complete incidence and strict one-stable/one-unstable/no-saddle mechanics. It identified row `18`, its eleven-row one-ring, and Q edge `(20,23)` as the coupled continuation from the predecessor gate.

## What was constructed

A connected upper/lower bifurcation inserts rows `25,26,27` into the predecessor’s 25-row Q.

- Junction `25` cones the exact cavity boundary `(5,6,7,17,9,10,18,19,20,23,15,16)` and replaces ten supporting Q triangles.
- Upper branch `26` replaces triangle `(9,17,25)`.
- Lower branch `27` replaces `(18,19,25)`, `(19,20,25)`, `(20,23,25)`.

Thus the branch spans both the residual stable-star side and the old saddle basin. It is not an unchanged rail, rotational copy, single deletion, or metric-only deformation. The exact endpoints do not deactivate the whole old eleven-row star: forcing larger portions out transfers the stable equilibrium to row `1`. That is part of the negative result.

After every materialized shape branch the exact projective controls are

```text
T_u(q)=q/(1-q·u),  (T_u Q)^polar=Q^polar-u,
F(u)=centroid((T_u Q)^polar)=c-u,  DF=-I_3.
```

Setting `u=c` solves all three first moments identically. Every exact endpoint has first moment `(0,0,0)`, Santaló root `s=0`, positive projective denominators, and a positive tetrahedron containing the origin. For the box `[-2^-80,2^-80]^3`, the exact bounds `max_p 2^-80||p||_1` are `1.84519e-24`, `1.84769e-24`, and `1.84773e-24`, all below `1`; hence the full root box lies in `int(Q)` and polarity is bounded throughout. See the exact root-box certificate (`root_box_boundedness_certificate.json`).

## Exact endpoint 1: strongest gate-valid body

Full exact certificate (`double_y_gate_safe_exact.json`)

- Q/P f-vectors: Q `(28,78,52)`, P `(52,78,28)`; all 28 Q rows are extreme.
- Exact own-centroid class: `(2,1,1)`.
- P inactive separation: `1.0101984183194323e-5`, exact `>10^-5`.
- Q inactive separation: `4.763684572076683e-4`, exact `>10^-5`.
- Pre-gauge centroid: approximately `(0.009777418801057253, 0.006256927872991613, 0.00011112126273770819)`.
- Stable row `17`, protected target: margin `0.9680997156329716`.
- Transferred stable row `1`: margin `0.003210210784380884`.
- Unique unstable P vertex `7`, incidence `(1,10,17)`: margin `0.6406156131873693`; full cone coefficients approximately `(1.018022862,1.044859515,1.279590411)`, all positive.
- Unique saddle P edge `(50,51)`, dual Q edge `(23,27)`: margin `0.012842354532530485`, with all four segment/cone conditions positive.

The old saddle `(20,23)` is gone, but it has transferred to `(23,27)`; stable row `18` has transferred to row `1`. This is an open strict nonwinner.

Meshes: P OBJ (`double_y_gate_safe_P.obj`), P STL (`double_y_gate_safe_P.stl`), Q OBJ (`double_y_gate_safe_Q.obj`), Q STL (`double_y_gate_safe_Q.stl`).

## Exact endpoint 2: three-node transfer cell

Full exact certificate (`double_y_near_transition_exact.json`)

- Q/P f-vectors: Q `(28,78,52)`, P `(52,78,28)`.
- Exact class `(2,2,2)`.
- Protected stable row `17`: `0.9683410998908135`.
- Residual stable row `18`: `4.6592238639497205e-5`.
- Protected unstable incidence `(1,10,17)`: `0.6436935298872603`.
- Extra unstable incidence `(23,25,27)`: `1.0029901532388335e-4`.
- Saddles `(23,25)` and `(23,27)`: approximately `1.00299e-4` and `1.00314e-4`.
- P inactive separation `8.61110438689328e-7`, so it fails the gate; Q inactive is `1.611853633223976e-4`.

This exact body exposes one extra unstable vertex joining two genuine saddle edges.

## Exact endpoint 3: five-node frontier

Full exact certificate (`double_y_five_node_frontier_exact.json`)

Two further lower-branch rows `28,29` were inserted and optimized jointly. The exact result has Q `(30,84,56)`, P `(56,84,30)`, class `(2,2,2)`, protected margins `0.9682446922303948` and `0.6436812659477315`, residual stable margin `2.1299111893263773e-5`, extra unstable margin `1.6535417387840118e-5`, and saddles `(23,27)` and `(23,29)`.

Its Q inactive separation remains above the gate at `1.7223330503825016e-5`, but P inactive collapses to `1.2359845040276754e-7`. The residual/inactive trend is:

```text
3 nodes: residual 1.00314e-4, P inactive 8.61110e-7
4 nodes: residual about 5.084e-5, P inactive about 3e-7  [floating checkpoint]
5 nodes: residual 2.12991e-5, P inactive 1.23598e-7
```

Repeated stellar subdivision therefore approaches an incidence wall faster than it opens a cancellation chamber.

## Circuit and Morse map

Complete exact circuit map (`branch_circuit_map.json`)

The scalar insertion path crosses fourteen exact rational four-row circuits, with row sets and approximate thresholds:

```text
(6,7,18,25)       .8034281705258048
(7,9,18,25)       .8085142493652829
(5,6,18,25)       .8101754393273476
(5,18,20,25)      .8118499032061602
(5,16,20,25)      .8312733753763480
(9,10,18,25)      .8514216019708240
(16,20,23,25)     .8573423714544662
(15,16,23,25)     .8674101277439935
(18,19,20,25)     .9205329957967561
(7,9,17,25)       .9743731440386643
(9,17,25,26)      .9848521435630814
(20,23,25,27)     .9922304716157560
(19,20,25,27)     .9955851037529643
(18,19,25,27)     .9972577616469774
```

The JSON stores the exact rational thresholds, removed/added facets, and before/after f-vectors. No simultaneous five-row circuit occurs on this recorded scalar path; broader five-row searches produced no certified open winner.

Six Morse transitions were localized numerically to adjacent binary64 values. They are not claimed as algebraic root isolations; endpoint mechanics is exact. Their net sequence is

```text
stable 18 -> temporary stable 1+18 -> stable 1
saddle 20-23 -> saddle 23-25 -> saddle 23-27,
```

with short intermediate `(3,1,2)` and `(2,2,2)` pair-birth cells.

## Structural obstruction

Local witness Jacobian (`local_transfer_jacobian.json`) shows that the gradients of saddles `(23,25)` and `(23,27)` are nearly exact negatives. Local LP and direct searches found no direction making the residual stable witness, both saddle witnesses, and the extra unstable witness simultaneously negative while preserving the row-17 and vertex-7 barriers. Suppressing either outgoing saddle strengthens the other.

Deletion/deactivation scans transfer the stable feature to row `1`; larger lower deletions transfer the saddle to another neighboring edge. Great-circle and bifurcated radial-ascent rails with 12–32 segments can witness against row `1`, but create multiple additional unstable-saddle pairs near protected row `17`. Three-, four-, and five-node stellar continuations improve residual magnitudes while destroying primal incidence separation.

These computations delimit the tested stellar-junction, deletion, face-subdivision, and radial-ascent families; they are not a theorem excluding every double-Y geometry.

The next materially different architecture is a **non-stellar connected two-cell replacement** crossing a coupled five-row circuit. It must remove row `1` and both outgoing saddle edges in one event, permit old ring and lower-fork rows to become non-extreme simultaneously, preserve row `17` and incidence `(1,10,17)` only by explicit margin barriers, and retain the analytic gauge `u=c`.

## Independent verification

Current exact-record hashes match stored PASS reports:

```text
79782305a558041ade02c59387d94f5b9544fb93a77436640e6dc86e772e8476  gate-safe
222774e14189aba6a85378ced5d2c768db0b3d925f0d20598f4099d0b301d249  near-transition
d255e4e91a9835bea440e0a1b3d2595b84e470f77a438ce5c14b6a66fc58604f  five-node
```

- Full-triple exact verifier (`verify_double_y_independent.py`) independently enumerates every polar triple for the 28-row objects.
- Exact-support verifier (`verify_double_y_support_independent.py`) uses an independent facet proposal followed by exact support/nonincidence, closed-sphere, Euler, connectivity, centroid, gauge, lattice, and complete mechanics checks.
- Integrity and mesh audit (`verification_integrity_check.json`).
- PASS reports: gate-safe (`independent_verification_double_y_gate_safe_exact.json`), near-transition (`independent_verification_double_y_near_transition_exact.json`), five-node (`independent_verification_double_y_five_node_frontier_exact.json`).

Every maximal face, true edge, vertex, incidence/nonincidence, stable projection, vertex full normal cone, and edge segment/two-normal cone is stored and audited. No perturbation radius is claimed because no winner exists; the gate-safe nonwinner nevertheless lies in an exact open `(2,1,1)` chamber.

## Reproducible archive

- README (`README.md`)
- Certificate summary (`certificate_summary.json`)
- Manifest (`MANIFEST.json`)
- SHA256SUMS
- Complete archive (`santalo_double_y_result.zip`)

Archive SHA-256:

```text
95aa8c0541ded4778a88c58fd2c984f5d2ab709f7b7937015aa5e585ee841a93
```

Reproduction after unpacking:

```bash
python rebuild_from_certificate.py
python write_root_box_certificate.py
python verify_double_y_independent.py double_y_gate_safe_exact.json
python verify_double_y_independent.py double_y_near_transition_exact.json
python verify_double_y_support_independent.py double_y_five_node_frontier_exact.json
```

**Final determination:** the branch replaces the predecessor’s single lower-fork picture with an exact, hard-centered, multi-circuit upper/lower topology, but it transfers the complete residual pair rather than cancelling it. The strongest exact object remains `(2,1,1)`; the unresolved route is a non-stellar coupled five-row/two-cell replacement.
