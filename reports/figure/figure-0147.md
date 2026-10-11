# figure-0147

Historical AI scientific report · saved 2026-08-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Rapid Quartz 69 — AQ32-A2 exact adaptive refinement

## Verdict

No homogeneous polyhedral Gömböc was obtained. The strongest result is the completely expanded exact-dyadic endpoint **AQ32-A2**. Its exact polar generator `Q` and own-centred polar `P=(Q-s(Q))^circ` have

```text
(V,E,F)_Q = (22541,67616,45077)
(V,E,F)_P = (45077,67616,22541)
(S,U,H)_P = (2871,903,3772).
```

The predecessor had certified the 5,952-row collar and localized the first false U-H pair to sectors `6/14` near `gamma≈0.0401–0.0418`. :contentReference[oaicite:0]{index=0} AQ32-A2 freezes all required predecessor rows byte-for-byte, crosses an exact 1,208-event `16→32` adaptive incidence atlas, destroys that first pair and its next transferred relay, and certifies every target/collar/transition/cross-seam feature over the final Santaló root box. The weakest local exclusion is `2.1501357991621703e-6`, above the required `1.915868198716011e-6`.

The branch fails later: the first surviving exact U-H pair is in old sectors `4/12` near `gamma≈0.4417–0.4437`; the first surviving stable band begins near `gamma≈1.3197243`. Half-turn symmetry cancels transverse degree-one response but its axial response adds.

## Artifacts

- [Full research handoff](sandbox:/mnt/data/RQ69_AQ32A2_complete_handoff.md) — SHA-256 `4d8c499aedf7a11382ea673a73e3380b8a9ac09b17759e11f845c7edd13b023c`.
- [Complete exact endpoint archive](sandbox:/mnt/data/RQ69_AQ32A2_exact_endpoint.zip) — SHA-256 `ac6124a8dc723bf5520e6a7d04d8699fb74114924cd85754cc699f55b3b8783d`; `unzip -tq` passes.
- [README](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/README.md).
- [Deterministic generator](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/generate_AQ32A2_exact.py) — SHA-256 `5e1df2de910f1fb299b625997c9c85853bcac37be11441c3f9c90f088a3afd50`.
- [Independent verifier](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/verify_AQ32A2_exact.py) — SHA-256 `347ed764cebcd1ce5c5dee03efb58ba9567fddbdd39d78f8b92c903acf386d5a`.
- [Consolidated certificate](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_certificate.json).
- [Exact H/V and incidence arrays](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_exact_data.npz).
- [Expanded exact Q rows](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_Q_vertices_exact.csv), [maximal faces](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_Q_maximal_faces_exact.jsonl), and [true edges](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_Q_true_edges.csv).
- [Expanded P halfspaces](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_H_rows_root_box.csv), [vertices](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_vertices_root_midpoint.csv), [maximal faces](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_maximal_faces.jsonl), and [true edges](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_true_edges.csv).
- [Chamber atlas](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_chamber_atlas_summary.json), [root-box audit](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_exact_rootbox_audit.json), [first remaining exact features](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_first_remaining_exact_features.json), [perturbation proof](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_perturbation_proof.json), and [SHA-256 manifest](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/SHA256SUMS.txt).
- Watertight [Q OBJ](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_Q.obj), [Q STL](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_Q.stl), [P OBJ](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_at_santalo_midpoint.obj), and [P STL](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_P_at_santalo_midpoint.stl).

## Exact generator and frozen data

All coordinates have common denominator

```text
D=2^118=332306998946228968225951765070086144.
```

Exactly `5,973` rows are frozen: collar rows `0..5951`, seam rows `5952..5967`, square rows `21696..21699`, and apex row `21700`. Their predecessor/endpoint canonical SHA-256 is identical:

```text
6d96a9a48bf154c7bba6de06a97ce583b2fa49858d38ad6ea9a7b66065a6b3e3.
```

The stable square is

```text
(330241653278860971071379575221098836,
 ±649037107316853453566312041152512,
 ±649037107316853453566312041152512)/D,
```

and the apex is

```text
(-334416990645408040140947785717004757,0,0)/D.
```

The endpoint contains `1,260` modified old-sector rows and `840` inserted half-sector rows. Central sectors `6/14` run through ring `220`; sectors `7/15` through ring `410`. Added gaps `5.5/13.5` run through ring `80`; gaps `6.5/7.5/14.5/15.5` through ring `170`. Along each adaptive ray the generator selects maximal `s<=1` with

```text
p=sq,
p·(p_prev-p)>=1.1*m0*|p_prev-p|,
m0=1.915868198716011e-6.
```

Minimum scales are `0.9995701919857043` centrally and `0.9999841069808292` on gap rays. All new rows are inside the smooth source before the final dyadic shrink.

## Exact incidence and chamber atlas

All `22,541` rows are irredundant. An independent exact integer-predicate repair performs `533` 2–2 flips from the floating hull seed. There is one exact coplanar triangulation diagonal, `(21697,21698)`, inside the square; it is removed from the true-edge list. Euler is `2`.

The minimum nonzero adjacent orientation is attained at edge `(166,181)` with exact integer determinant

```text
127147975046385277374519693584517482939106762318038021311082705465281036499853312,
```

or physical magnitude `3.464902217509549e-27`. The exact global minimum normalized Q vertex-to-nonincident-maximal-face distance is `2.939343779797856e-18`, attained by vertex `165` against face `44257=[166,182,181]`; see [the exact proof](sandbox:/mnt/data/RQ69_AQ16_A2safe_exact_endpoint/AQ32A2_nonincident_separation.json).

The exact incidence path is

```text
C0→C1:  74 isolated exact 2–2 circuit roots
C1→C2: 320 exact row-insertion events
C2→C3: 294 isolated exact 2–2 circuit roots
C3→C4: 520 exact row-insertion events
Total: 1,208 events.
```

Every central wall has a rational root interval of width at most `2^-100`; every insertion records its exact visible patch and horizon. `C0` and `C4` have directed Santaló enclosures. `C1–C3` roots are numerical stage diagnostics inside exact incidence cells, not interval roots for all microcells.

Stage classes are

```text
C0 Q/P: (889,3473,4360)/(3473,889,4360)
C1 Q/P: (889,3239,4126)/(3239,889,4126)
C2 Q/P: (889,3239,4126)/(3239,889,4126)
C3 Q/P: (903,2871,3772)/(2871,903,3772)
C4 Q/P: (903,2871,3772)/(2871,903,3772).
```

## Directed Santaló root

The final root is isolated in a coordinate box of radius `1e-50` around

```text
( 0.00008555194046519056104526374002717924147701043526658991959,
 -0.00000000000000001333447181033046307737509461294791629997778410849592206,
 -6.722375920452726635833922042629035446152639120909238831e-18 ).
```

At the midpoint:

```text
V = 4.242965672057352294498441778719971750500852700544820664
||M||/V = 5.804224001428604e-61
||F|| = 9.8508492763971710e-60
strong-monotonicity lower = 16.2263207848728263.
```

The conservative root-ball radius is `6.0709075131688129e-61`; the independent verifier recomputes the larger admissible value `1.6009299556334315e-60`. Projective denominators remain in `[0.9764226996657525,1.0064349470451293]`. The positive-definite Jacobian gives global uniqueness.

## Complete mechanics

The full directed class is

```text
Q relative to s(Q): (903,2871,3772)
own-centred P:       (2871,903,3772).
```

The certified local set contains `8,073` rows and all of its `17,831` maximal faces, `8,073` vertex/full cones, and `25,902` true-edge/full cones. Over the entire root box it has zero extra stable faces, unstable vertices, or saddle edges. Directed minima are

```text
face exclusion   9.560367125081844e-6
vertex exclusion 2.1501357991621703e-6
edge exclusion   2.1501357991621703e-6.
```

The stable square margin is `0.0019531249999999868`; the apex margin is `0.0005020992467418405`.

The first surviving U is row `10932`, sector `4`, `gamma=0.4437242886757828`, with margin `0.0004305922768369719`; row `10940` is its half-turn twin. The first H is edge `[10916,10932]`, mean `gamma=0.4417242886757828`, with the same limiting primitive; `[10924,10940]` is its twin. The first S is face `1781`, spanning sectors `2/3` at `gamma=1.3197242886757834..1.3237242886757834`, margin `5.3147447941837964e-5`. Exact rational primitives are in the first-feature ledger.

## Dominant obstruction

The global L1 support-error upper bound is `0.35945035363776096`, against budget `3.1342152657311286e-7`, a factor `1,146,859.1757813126`. The actual Santaló displacement is `8.555194046519055e-5`, or `44.654397689009244` required-margin units.

Half-turn pairing cancels transverse response but not axial response:

```text
C0 root x = 7.229882669645962e-5
C4 root x = 8.555194046519055e-5
increase  = 1.325311376873093e-5.
```

A third exact-topology near-side recurrence in sectors `4/12` overshoots to numerical root `x=-3.245021762200317e-5`, deactivates eight rows, worsens Q to `(897,4267,5162)`, and reopens tiny U-H pairs near `gamma≈0.065`. Local-patch, scalar far-side return-belt, and Y-taper probes likewise transfer the pair to patch exits or create new control-boundary features. Their roots were not fully directed and they are not claimed endpoints; see the archived probe ledgers.

## Perturbation and independent verification

The coordinatewise open box is

```text
|delta q_ij|<=2^-256=8.636168555094445e-78.
```

After propagating topology, feature witnesses, denominators, and root motion, the smallest proof ratio is `6.623811943211415e40>1`. The root remains inside the `1e-50` box. Both generator and verifier return `PASS`. Q has `45,078` mesh triangles and P `90,150`; every mesh edge has incidence exactly two.

## Smallest nonrepeating continuation

Another one-ray recurrence or independent scalar return belt is ruled out by the materialized probes. The next finite object must be a genuinely two-dimensional, half-turn-coupled **four-branch return cell**:

1. Freeze the square, apex, 5,952 collar rows, seam ring, and all certified AQ32-A2 adaptive rows.
2. Replace the complete stars around sectors `4/5` and `12/13` over approximately `gamma=0.4397243..0.5237243`, not only rows `10916/10932`.
3. Include both adjacent half-sector rails, transverse cross-links, and a shared terminal cell that absorbs/deactivates temporary gap rails before they meet the coarse grid; this removes the observed patch-exit relay.
4. Add an independent axial support control. Together with two transverse controls, solve all three normalized Santaló equations as dependent variables in every rebuilt incidence cell.
5. Enumerate exact circuit order before using any formal control root, and retain all changed face/vertex/edge exclusions above `1.915868198716011e-6` throughout the root box.
6. If the root path reaches the first stable wall, couple the sectors `2/3` and `10/11` stable strip near `gamma=1.3157243..1.3237243` into the same event rather than correcting it sequentially.

## Disposition

**Used as a rigorous finite nonwinner and as closure of the first adaptive angular frontier.** AQ32-A2 proves that a literal half-turn `16→32` refinement can remove the assignment-named U-H pair without damaging any target, collar, transition, or cross-seam feature. It also isolates the remaining obstruction: independent axial moment leverage and a two-dimensional patch-exit topology are required. The acceptance gate remains unmet.
