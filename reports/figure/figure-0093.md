# figure-0093

Historical AI scientific report · saved 2026-08-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Verdict

**No finite homogeneous convex polyhedral Gömböc was found.** The strongest requirement-complete exact endpoint is a fully certified fallback of strict own-centroid class `(S,U,H)=(2,2,2)`, not the required `(1,1,0)`. The journal's acceptance gate is a finite uniform-density body evaluated at its own exact volume centroid, with one stable face, one unstable vertex, no saddle, complete incidence, independent verification, and matching meshes. :contentReference[oaicite:0]{index=0} The supplied frontier required a connected nonlocal annulus with at least 13 ascent edges, an independent return branch, simultaneous separated circuit crossings, exact projective centring, and both inactive gaps above `10^-5`. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

## Exact connected annulus

Starting from the 20-row exact `Q_post`, the final body retains old rows `2,10,14,17,24`, deactivates active old rows `0,1,3,5,6,7,11,12,13,15,16,18,23,25,26`, and inserts two connected branches

```text
A0--A1--...--A12--old17
B0--B1--...--B12--old17.
```

Every displayed segment is a true Q edge. Both ascent and return therefore contain exactly 13 actual extreme-row edges; all 31 Q rows are extreme. Full exact rational rows, centred Q, polar P, cycles, edges, and incidences are in [the exact endpoint](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_coupled_gate_exact.json). [This exact recurrence](sandbox:/mnt/data/santalo_nonlocal_annulus_result/regenerate_coupled_from_ruled.py) regenerates its raw Q rows from the ruled parent.

## Simultaneous separated circuit crossing

The ruled parent contains two separated supporting quadrilateral circuits:

```text
C0=(A0,B0,B1,A1)      rows (5,18,19,6)
C1=(A10,B10,B11,A11)  rows (15,28,29,16).
```

One exact scalar makes both augmented determinants vanish at the same wall `t=0`. Their minimum normalized support gaps to all other Q rows are approximately `3.7823999` and `12.2407339`; their centroids are separated by about `292.374` and `131.596922°`. Across the wall, both diagonals change together:

```text
negative side: (B0,A1),(B10,A11) = (18,6),(28,16)
positive side: (A0,B1),(A10,B11) = (5,19),(15,29).
```

The exact endpoint uses `t=-2549/2048` and global Q scale `515/512`. Both negative-side diagonals are true, both positive-side diagonals absent, and no row is lost. The wall has Q/P f-vectors `(31,75,46)/(46,75,31)`; either strict side has `(31,77,48)/(48,77,31)`. Exact determinants, supports, side topologies, and endpoint signs are in [the circuit map](sandbox:/mnt/data/santalo_nonlocal_annulus_result/simultaneous_separated_circuit_map.json).

## Exact centring and bounded polarity

Every accepted endpoint uses

```text
T_u(q)=q/(1-q·u),
(T_u Q)^polar=Q^polar-u,
F(u)=centroid((T_u Q)^polar)=c-u,
DF=-I_3,
u=c.
```

Thus all three volume moments are equations, not penalties. For the strongest endpoint, the pre-gauge polar centroid is approximately `(0.5153654266332737,-2.8512996798005927,-0.005669350369481013)`, the projective denominator interval is `[0.5139783895862224,152.86220637702496]`, and the post-gauge first moment and centroid are exactly zero. The isolated control/Santaló root is exactly `(0,0,0)` in `[-2^-80,2^-80]^3`.

Q rows `(0,1,3,4)` contain the origin with positive exact barycentric weights approximately `(0.1503220004,0.3301655804,0.3483472791,0.1711651401)`. The maximum support displacement on the whole root box is `1.3884889171728745e-23<1`, so the origin stays strictly interior and polarity stays bounded. Exact inequalities are in [the root-box certificate](sandbox:/mnt/data/santalo_nonlocal_annulus_result/root_box_boundedness_all.json).

## Strongest exact endpoint

```text
Q: (V,E,F)=(31,77,48)
P: (V,E,F)=(48,77,31)
complexity=154
class at P's exact uniform centroid=(2,2,2)
P inactive separation=1.0234559950639188e-5
Q inactive separation=1.0229288486664402e-5.
```

Both gate comparisons are proved exactly by rational squared inequalities.

Stable faces:

```text
row 0 = old2   margin 0.35261867104650846
row 3 = old17  margin 2.7544603037186524.
```

Unstable vertices, with complete positive normal-cone coefficients:

```text
P vertex 2, incidence (0,2,3)=(old2,old14,old17)
margin 6.288975493432364
coefficients ≈ (82.9736843520,24.2928480247,64.8082939560)

P vertex 7, incidence (1,4,25)=(old10,old24,B7)
margin 7.735484509438685
coefficients ≈ (0.3374166510,68.8157726318,62.7333294534).
```

Saddles, each with exact positive `(t,1-t,alpha,beta)`:

```text
P edge (0,3), dual Q edge (0,4)=(old2,old24)
margin 0.0812104814012886

P edge (9,46), dual Q edge (18,24)=(B0,B6)
margin 0.05788110498123615.
```

Closest excluded face, vertex, and edge margins are respectively `-0.018596391703338447`, `-0.0471896913423373`, and `-0.018598117646176453`. Every maximal face, every vertex including nonsimple full cones, and all 77 true edges are audited exactly. See [the complete normal-cone audit](sandbox:/mnt/data/santalo_nonlocal_annulus_result/full_normal_cone_audit.json) and [the compact certificate](sandbox:/mnt/data/santalo_nonlocal_annulus_result/certificate_summary.json).

## Independent return-branch moment control

A separate closed 13+13 annulus tests internal pre-gauge cancellation. Three return-complex controls—relative branch separation, return-only radial bulge, and south-junction scale—solve the raw centroid to about `3e-14`. The centroid Jacobian has rank three, determinant `-2.1963479936224e-9`, singular values `(0.00470006999,0.00130005354,0.00035944760)`, and condition number `13.0758`. Thus moment rank is not the obstruction.

After dyadic exactification and exact `u=c`, that body has Q/P f-vectors `(26,72,48)/(48,72,26)`, class `(5,2,5)`, and P/Q inactive gaps about `0.00107124`. Internal cancellation therefore multiplies the Morse block in this two-sheet topology. See [the moment cone](sandbox:/mnt/data/santalo_nonlocal_annulus_result/return_branch_moment_cone.json) and [the exact moment-balanced endpoint](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_moment_balanced_exact.json). No single returned endpoint simultaneously has the coupled endpoint's best mechanics and exactly zero pre-gauge moment; both are exactly own-centred after the required analytic gauge.

## Transferred equilibrium block

The original unwanted stable old row `18` and saddle Q edge `(18,24)` disappear, but their Euler-neutral content transfers into two closure relays:

```text
root relay:   stable old2 + saddle Q(old2,old24)
return relay: extra U at (old10,old24,B7) + saddle Q(B0,B6).
```

Old17 remains the target stable feature, and the robust unstable lineage `(old2,old14,old17)` survives, but it is no longer unique. The exact simultaneous crossing changes both selected annular diagonals without changing `(2,2,2)`.

## Attempts to break the conclusion

This is a finite-family delimitation, not a global impossibility theorem. The package records:

- `1,486` critical-row deletion/deactivation subsets, `685` valid, no `(1,1,0)`;
- exact radial-scale scans;
- four three-rail differential-evolution runs, `19,712` total classifications, all with three 13-edge chains, no winner; best P gaps were only `3.4e-7` to `1.75e-6`;
- `4,000` random three-sheet trials (`3,974` valid), no winner; closest low-complexity state `(2,3,3)` with P gap `3.14e-7`;
- `4,000` low-residual three-sheet trials (`3,975` valid); the stored `(2,2,2)` state had P gap `8.43e-8`;
- local SQP/SLP refinements, all transferring or multiplying the closure block.

Raw scope and checkpoints are in [search_obstruction_summary.json](sandbox:/mnt/data/santalo_nonlocal_annulus_result/search_obstruction_summary.json).

## Structural obstruction and next topology

A two-sheet annulus can realize 13+13 actual edges, a full-rank return moment cone, exact hard centring, simultaneous separated circuit crossings, complete old-basin deletion, and both `10^-5` gates. It lacks enough independent transverse two-dimensional closure cells to destroy both the root and return relays. Adding a third one-dimensional rail lowers residuals only after primal inactive separation collapses.

The smallest architecture not subsumed is a **finite-thickness three-sheet communicating annulus with two genuine transverse two-cell closure bands**. One band must replace the complete old2-old24 root star; the second must replace the B0-B6/B7 return star. Those bands and the two interior circuits must cross in one four-block event, allowing old2, old24, B0, B6/B7 and exposed relays to become non-extreme together. A fourth noncritical actuator, or analytic elimination of a return mode, should maintain a uniformly conditioned three-dimensional moment cone while `u=c` remains exact.

## Independent verification and finite meshes

[The independent verifier](sandbox:/mnt/data/santalo_nonlocal_annulus_result/verify_nonlocal_annulus_independent.py) uses only the Python standard library, enumerates every polar triple, rebuilds P/Q topology, recomputes exact volume moments and gauge, and audits every face, vertex full cone, true edge, incidence, and nonincidence. A fresh coupled run completed in `28.67 s`, returned `PASS`, and matched exact-record SHA-256

```text
6b0973875b7c3532333d24f602fda2451a4d9dc5e805362c3a13faec3d609ea6.
```

Reports: [independent verification](sandbox:/mnt/data/santalo_nonlocal_annulus_result/verification/independent_verification_nonlocal_annulus_coupled_gate_exact.json), [fresh transcript](sandbox:/mnt/data/santalo_nonlocal_annulus_result/verification/verify_coupled_fresh_transcript.txt), and [mesh audit](sandbox:/mnt/data/santalo_nonlocal_annulus_result/mesh_integrity_report.json).

The strongest P mesh has `48` vertices, `31` maximal faces, `77` true edges, `92` STL triangles; Q has `31`, `48`, `77`, `58`. OBJ cycles match the certified cycles up to reversal.

- [P OBJ](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_coupled_gate_P.obj)
- [P STL](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_coupled_gate_P.stl)
- [Q OBJ](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_coupled_gate_Q.obj)
- [Q STL](sandbox:/mnt/data/santalo_nonlocal_annulus_result/nonlocal_annulus_coupled_gate_Q.stl)

No coordinate-ball perturbation radius is claimed because there is no winner; exact strict signs and gaps prove open nonwinner chambers.

## Reproducible package

[Complete archive](sandbox:/mnt/data/santalo_nonlocal_annulus_result.zip)

```text
SHA-256 19df5705efccf875ddf2bf45937fcd13747d0815ad85dd5c38604c6750000eee
```

- [README](sandbox:/mnt/data/santalo_nonlocal_annulus_result/README.md)
- [manifest](sandbox:/mnt/data/santalo_nonlocal_annulus_result/MANIFEST.json)
- [SHA256SUMS](sandbox:/mnt/data/santalo_nonlocal_annulus_result/SHA256SUMS)
- [replay driver](sandbox:/mnt/data/santalo_nonlocal_annulus_result/rebuild_all.py)
- [coordinate/mesh rebuilder](sandbox:/mnt/data/santalo_nonlocal_annulus_result/rebuild_from_certificates.py)

Reproduction after unpacking:

```bash
python rebuild_all.py
```

**Final determination:** the requested Gömböc was not reached. The branch supplies a finite exact 13+13 connected annulus, an exact simultaneous separated two-circuit crossing, a separately materialized rank-three internally moment-balanced return branch, exact hard centring, complete incidence and full-cone mechanics, strict P/Q gaps above `10^-5`, independent verification, and matching meshes. The next nonredundant move is the four-block, two-closure-band communicating three-sheet annulus described above.
