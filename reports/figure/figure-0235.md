# figure-0235

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Quartz 58 — exact carrier-breaking handoff

## Disposition

**EXACT MATERIALIZED NONWINNER.** No finite homogeneous convex polyhedral Gömböc was obtained. The run requires a uniform-density body evaluated at its own exact ordinary-volume centroid, strict `(S,U,H)=(1,1,0)`, irredundant H/V data, every maximal face and true edge, exhaustive full-cone margins, independent replay, and OBJ/STL; an auxiliary-centre or wall-only object is insufficient. :contentReference[oaicite:0]{index=0}

The inherited frontier was `E19ZC -> E21S -> E17K`: `E21S` is locally forced by carrier `{F,M}`, while compact `E17K` transfers the obstruction to `{A,B}`. The requested next move had to give a carrier endpoint a certified nonpositive external arrow or replace the carrier in one nonsimplicial event. :contentReference[oaicite:1]{index=1}

That carrier is now genuinely broken. The exact shared-cell surgery removes `Z0,Z1`, inserts `G,H,K,J`, and contains central nonsimplicial quadrilateral `[H,G,J,K]`. On the promoted strict side `E19G`, `A->K<0` and `B->8<0` throughout the certified all-coordinate box, so the old `{A,B}` increasing-radius theorem is inapplicable; old stable `[Z0,A,B]`, unstable `A,B`, and saddles `(8,A),(8,B),(A,B)` are absent or strictly inactive. The replacement packet is already strict: stable `[H,B,10]`, unstable `K`, saddles `(B,K),(Y,G)`. Thus `E19G` is `(2,2,2)`, not a winner.

## Artifacts

- [Exact archive](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_nonwinner.zip), [SHA-256 file](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_nonwinner.zip.sha256), hash `8a7ef17a20e5076428800f6adc230b273006f1fe102f9572b910762d85cbcec1`.
- [Full determination](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/RESULT.md), [README](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/README.md), [one-command verifier](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/[internal-source-reference].sh), [verification record](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/VERIFICATION_RECORD.json), [190-entry manifest](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/SHA256SUMS).
- `E19G`: [exact report](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_exact_report.json), [H rows](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_H_representation.json), [audit](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_audit.md), [box](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_perturbation_certificate.json), [independent report](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_independent_verification.json), [OBJ](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_centered.obj), [STL](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_centered.stl).
- Cell and obstruction: [patch/volume certificate](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E17K_to_E19Q_shared_cell.json), [lineage](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E17K_E19_carrier_lineage.json), [carrier certificate](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_carrier_breaking_certificate.json), [independent carrier replay](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_carrier_independent_verification.json).
- Wall/family: [wall report](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19Q_wall_exact_report.json), [wall sequence](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_E19Q_E19H_exact_wall_sequence.json), [opposite side](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19H_exact_report.json), [three-control family](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_three_control_family.json), [exact deletion census](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/E19G_small_deletion_exact_census.json), [search ledger](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/search_ledger.json), [next topology](sandbox:/mnt/data/vivid_quartz_58_carrier_breaking_result/next_open_topology.json).

Clean replay ends with `VIVID_QUARTZ_58_CARRIER_BREAKING_BUNDLE_CONSISTENCY_PASS` and `ALL VIVID QUARTZ 58 CARRIER-BREAKING VERIFIERS PASS`; the ZIP passes `unzip -t`.

## Exact shared nonsimplicial cell

Common boundary: `A-8-Y-W-F-C-X-10-B-A`.

Source disk:

```text
[Z0,X,10] [Z0,10,B] [Z0,B,A] [Z0,A,8]
[Z1,8,Y] [Z1,Y,W] [Z1,W,F] [Z1,F,C] [Z1,C,X]
[X,Z0,Z1] [Z0,8,Z1]
```

Target wall disk:

```text
[G,A,8] [G,8,Y] [G,Y,W] [G,W,F] [G,F,H]
[H,F,C] [H,C,X] [H,X,10] [H,10,B] [H,B,K]
[K,B,A] [K,A,J] [J,A,G] [H,G,J,K]
```

Disk f-vectors are `(11,21,11)` and `(13,26,14)`; both have Euler characteristic one and identical boundary-edge sets. Wall `E19Q` has global `(19,50,33)`. Strict resolutions are `E19G` with diagonal `(G,K)` and faces `[G,K,H],[G,J,K]`, and `E19H` with diagonal `(H,J)` and faces `[H,G,J],[H,J,K]`; both have `(19,51,34)`. Coning the wall disk to its exact own centroid gives positive tetrahedral volume in either triangulation, with identical total

```text
26414377255144324379017392788988700419095145939536331654765723699064283979961966824290864698749131604429433088474343
/
1078107390159597390620267881397646569617909907361043402226955911594797710729178686054103117184230008070914923376410624 > 0.
```

This is an exact positive-volume incidence replacement, not an unstated coordinate homotopy from the supplied `E17K` coordinates.

## Exact endpoint `E19G`

Use `D=2^40`. Before centring, the integer numerators for labels `[8,10,11,A,B,C,F,L,P,T,W,X,Y,U,V,G,H,K,J]` are

```text
(0,0,0)
(2942686317053,-2343955186696,349374481493)
(962368445656,-778292828630,118429110735)
(5590923130967,-5005341507742,811117214317)
(2463298597996,-921192852918,-79976860895)
(3752392290996,-3280860043537,545487274934)
(3655335382919,-3289498132802,562872093310)
(2707731989040,-2264162595531,359212275144)
(1289511412813,-1059620123902,164604064271)
(2167053742069,-1821535567763,290923072575)
(3609636218212,-3273299756834,561899617513)
(2925870652137,-2519979727111,413723892763)
(2420405374988,-2208782774056,381301401670)
(1620056487829,-1442939212905,245282661574)
(2066768125772,-1867395246031,320905978138)
(5095695902752,-4647866132499,795875224851)
(4489520145850,-3837501484960,620740732983)
(5662996579748,-5001393606691,823525329882)
(5563532264491,-4985061702757,821852459985)
```

The physical body is `conv{Q_i/D-C}`. All 19 supplied vertices are active. Exact volume:

```text
168156769037783216217044956577266681/3987683987354747618711421180841033728.
```

Exact uncentred moments:

```text
1503065094397195575881651496170759057124705258267/11692013098647223345629478661730264157247460343808
-226302157354152442451010499610024338096370623753/2192252455996354377305527249074424529483898814464
526349556146015064677000307777049414571547015445/35076039295941670036888435985190792471742381031424.
```

Exact centroid:

```text
4509195283191586727644954488512277171374115774801/1479122582770287210475325288982733807545271451648
-226302157354152442451010499610024338096370623753/92445161423142950654707830561420862971579465728
526349556146015064677000307777049414571547015445/1479122582770287210475325288982733807545271451648.
```

The verifier proves `M_j=VC_j` exactly, hence centred moments `(0,0,0)`.

Actual maximal faces:

```text
[8,11,10] [8,10,B] [8,P,11] [8,B,A] [8,A,G]
[8,T,P] [8,X,T] [8,U,X] [8,Y,V] [8,G,Y] [8,V,U]
[10,11,P] [10,H,B] [10,T,L] [10,L,X] [10,P,T] [10,X,H]
[A,B,K] [A,J,G] [A,K,J] [B,H,K]
[C,X,F] [C,F,H] [C,H,X]
[F,Y,W] [F,W,G] [F,X,U] [F,V,Y] [F,U,V] [F,G,H]
[L,T,X] [W,Y,G] [G,K,H] [G,J,K]
```

True edges:

```text
(8,10) (8,11) (8,A) (8,B) (8,P) (8,T) (8,X) (8,Y) (8,U) (8,V) (8,G)
(10,11) (10,B) (10,L) (10,P) (10,T) (10,X) (10,H) (11,P)
(A,B) (A,G) (A,K) (A,J) (B,H) (B,K)
(C,F) (C,X) (C,H)
(F,W) (F,X) (F,Y) (F,U) (F,V) (F,G) (F,H)
(L,T) (L,X) (P,T) (T,X) (W,Y) (W,G)
(X,U) (X,H) (Y,V) (Y,G) (U,V)
(G,H) (G,K) (G,J) (H,K) (K,J)
```

Thus `19-51+34=2`. For each oriented face, `n=primitive((Q_j-Q_i)×(Q_k-Q_i))`, `h=n·Q_i`, and the centred row is `n·x<=h/D-n·C`. The H file contains every primitive normal, RHS and nonincident slack. Minimum integer slack is `702135580462868647953827442595`; normalized nonincidence is `5.823968135140232e-06`.

## Exhaustive own-centroid mechanics

```text
stable   [8,B,A], [10,H,B]
unstable 8, K
saddles  (B,K), (Y,G)
class    (2,2,2)
```

Every face projection component, every directed vertex-neighbour component, and all four true-edge components `(t,1-t,alpha,beta)` are exact in the report and normalized in the audit. The minimum absolute signed normalized separation over all active and inactive features is `0.003498268541906174`.

Exact interval arithmetic permits independent perturbation of all 57 coordinate entries by `2^-28`, recomputes the volume, moments and dependent centroid, and preserves the complete incidence and class. A clean-room Qhull/tetrahedral/full-unit-normal implementation agrees; OBJ/STL are watertight, winding-consistent and Euler two.

## Carrier theorem and remaining obstruction

Throughout the `2^-28` box,

```text
A->K in [-105911615914194770646326787816169692456616477323767003977049,
         -105894751798205307946194504437418198699872474331596811556185]
        /803469022129495137770981046170581301261101496891396417650688 < 0,

B->8 in [-5088345652310981943344044103901773573588148611938716064204505,
         -5087486897719448751181079411139691411156844855421591626745561]
        /1606938044258990275541962092341162602522202993782792835301376 < 0.
```

Therefore both old forcing endpoints have a certified negative external arrow and remain non-unstable; old saddle edges remain strictly inactive. Conversely, every arrow from `K` to actual neighbours `A,B,G,H,J` is positive, and every arrow at `8` is positive. Hence `K` and `8` are strict unstable vertices throughout the chamber and `U>=2`. This is a local open-chamber theorem, not a global graph theorem.

## Wall sequence and moment-eliminated family

Keep all `E19G` coordinates except `J.z`; the primitive plane normal through `G,H,K` is `(-39508186936130758201947,-82593092456480633494566,-245420628908511754439660)`. Solving `n·(J-G)=0` gives `E19Q`; the exact displacement is `(0,0,598261818248086831336188714619551/53968567036201480261116032274399232)`. Along `J(t)=J_G+t(J_Q-J_G)`, `0<=t<=129/128`, 75 ambient rational circuit roots are enumerated, but exact support ledgers prove one actual hull change only: `(G,K)` for `t<1`, quad `[H,G,J,K]` at `t=1`, and `(H,J)` for `t>1`. `E19G`, `E19Q`, and `E19H` all remain `(2,2,2)`.

A genuine three-parameter family uses `Q_G.x+=512a`, `Q_H.y+=512b`, `Q_J.z+=512c`, `(a,b,c)∈[-1,1]^3`. The shape directions have rank three modulo translation/scale. Exact volume has multidegree `(1,1,1)` and moment numerators `(2,1,1),(1,2,1),(1,1,2)`. With `C_j=N_j/(4DV6)`, all moment equations hold identically; `d(M-VC)/dC=-VI` gives a unique dependent centroid. All 125 clean-room grid samples remain `(2,2,2)`.

## Search, exact finite exclusion, and open frontier

Positive-stress/affine searches produced 31,615 valid `G-K` realizations and 36,213 valid `H-J` realizations; no winner occurred. A 53-variable continuation reached hard score `-0.0002725169733982471` but collapsed to support `1.8376698987366212e-08` at circuit `{8,10,B,11}`; its far side remained `(2,2,2)`. Twelve coupled adjacent graph variants contributed 40,528 valid realizations and no winner. These are empirical, not continuum exclusions.

Exact integer arithmetic additionally audits all 697 subhulls obtained by deleting zero through three nonprotected `E19G` vertices while retaining `8,A,B`. Every retained set is full-dimensional and all 697 have class `(2,2,2)`.

The full `E19G` and `E19H` realization spaces remain open. The smallest materialized unclassified topology is the 19-vertex `E19H` graph outside its exact `2^-28` box. The first genuinely nonrepeating graph-changing cell must couple `H-B<->10-K`, `B-K<->A-H`, `Y-G<->8-W`, and the central `{G,H,J,K}` circuit, while giving `K` an outward relay. The smallest explicit sign architecture adds `R` with true edges `K-R,R-8` and nonpositive arrows `K->R,R->8`, preserving target `[8,A,B]`; if one support cannot realize the signs, use a connected pair `R,S` in one finite-thickness cell. With all old vertices retained, the candidate simplicial sizes are `(20,54,36)` or `(21,57,38)`. This is evidence-supported, not a proved minimum.

## Reusable conclusion

The old `{A,B}` carrier and its full unwanted packet have been deleted literally and exactly. `E19G` is bounded, irredundant, exactly own-centred, robust, independently reconstructed, and watertight-meshed. The shared nonsimplicial positive-volume cell nevertheless transfers the packet to stable `[H,B,10]`, unstable `K`, and saddles `(B,K),(Y,G)`. **Explicit disposition: exact materialized NONWINNER.**
