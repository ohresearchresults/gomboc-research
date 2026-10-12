# figure-0404

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Comet 83 — whole-basin reconstruction, exposed material, and two complementary low-complexity frontiers

Assignment: `figure-0404`.

## Result and recovery status

**No own110 body is claimed.** The principal constructive findings are two different, completely audited exact nonwinning architectures:

1. **C320, V94/E160/F68, own121/weak000:** whole-support coarsening and actual mass correction leave only one unwanted U/H pair, with **150 true edges of headroom**. A low-coordinate version, `COMPACT_COARSENED_G5M2`, has maximum reduced raw-coordinate numerator/denominator lengths 67/67 bits and a 9,448-bit common centered denominator.
2. **C510, V87/E255/F170, own716/weak000:** a complete physical escape route plus **opposite-side exposed material**, not merely a center adjustment, removes every unwanted unstable basin. The remaining problem is entirely on the stable side. The common-grid version `SC83_C510_OUTSIDE_MASS_G8` has maximum reduced raw-coordinate lengths 27/27 bits and a common centered denominator of only **113 bits**. It retains 55 true edges of headroom.

These are complementary continuation points, not successively better approximations to an own110 body. C320 is monostable but has a substantial physical closed-cut barrier. C510 is monounstable but has a substantial centered-polar closed-cut barrier.

**Recovery limitation of this response:** the complete runnable **59-unit standalone capsule** was constructed, decoded into a fresh directory, and successfully cold-replayed. Its complete literal source is in the attached `RECOVER_SC83.py`, but it is **not embedded in this `result_markdown`**. Consequently this response does not fulfill the requested inline-only recovery contract. Under the assignment's explicit durability rule, the newly computed objects below remain **artifact-backed but ephemeral**, and are **not promoted here as durable successors** to the last reconstructible immutable parent. The hashes and links below locate and authenticate the complete recovery artifact; they are not presented as substitutes for the missing inline capsule.

The strongest exact mathematical findings are also stated below with their proofs and precise scope. No finite unsuccessful search is converted into an exclusion theorem.

## 1. Source authority: the assigned aliases conflict with the literal parent

The immutable parent is `figure-0402`, SHA-256 `8ce4f86a32d0921555ac4cb4b466718d1fcae9b7817f1ff669dceb055043a37b`. Its complete literal payload and its complete standalone source capsule were read and hash-checked.

The assignment and navigation summary identify C544 as V128/E272/F146 and C506 as V121/E253/F134. **Those are not the bodies in the literal immutable parent.** The actual parent recipes reconstruct:

| Literal exact parent | V/E/F | Own strict S/U/H | Weak-only |
|---|---:|---:|---:|
| `CR70_C544_COARSEN8_G14` | 154/272/120 | 1/3/2 | 000 |
| `CR70_C506_COARSEN15_G14` | 142/253/113 | 1/4/3 | 000 |

The conflict is visible between the navigation summary and the literal table. I followed the literal recipes rather than inventing a conversion between the conflicting aliases.

For the literal C544, the retained apex is raw-lex87, degree44; the unstable vertices are `[82,87,139]`, and saddle edges are `[[83,129],[141,145]]`. For literal C506, the apex is raw-lex74, and the unstable vertices are `[30,69,74,133]`. The sole stable carrier in these parent monostable bodies is original input support3.

Likewise, the literal parent's fixed-body center-ball obstruction has radius **2/25**, not 1/2000. It concerns fixed geometry, not an affine or shape exclusion.

The literal `C572_DUAL` is the physical body obtained by adding a polar relay inequality and correcting physical mass. I did not reinterpret it as the independently centered geometric polar of another named body.

The original standalone parent replay completed with:

`CR70_COLD_SOURCE_ONLY_ALL_EXACT_NONWINNERS_AB_MASS_GATES_PASS 3215 0aaf86cf4c3d06347c9ed801c257fb39b663b7cf0d6fa9f490326ff7810e584d`

### Independently retrieved library evidence

The following exact source units were read completely, not merely through search excerpts:

- `material:[internal-source-reference]`, `COORD_SINGLE_CAP_MASS_EXISTENCE_V1.md`, SHA-256 `bca38da0cd0c495593041dff24233610ffcc30351b0878e7f6744fdeb1bd333f`. Its cap potential gives global mass-closing existence under its stated bounded-cap hypotheses. It does not preserve a mechanical class, protected incidences, or an edge budget.
- `material:[internal-source-reference]`, `TWO_C616_DELETIONS_EXACT_FREE_TWO_THREE_LINK_EXCLUSION.md`, SHA-256 `8da989165096fffc58344c78b432009b4bf23f4b2c6a701a5a8919361a3f40f5`. I used its free-path criterion, not its body-specific C616 exclusions, which do not transfer to the present bodies.

## 2. Main monostable construction: C320 own121

### Geometry and actual topology

`SC83_C320_WHOLECOARSEN_H41_G10_OWN121` is a uniformly filled rational body with:

- **V94/E160/F68**, strict **1/2/1**, weak-only **000**, primitive equilibrium zero counts **000**.
- **184 positive centered tetrahedra**, independently integrated volume, and exactly zero centered first moments.
- Sole stable support **input2**; unstable vertices **raw-lex0 and48**; sole saddle **[0,74]**.
- One degree41 vertex, raw-lex28; all other vertices have degree3.

The high-degree geometric vertex is

`(-93986657/2000000000, -8245791/625000000, 2092920449/2000000000)`.

It is **not an unstable equilibrium**. The physical root has changed: the desired root for the current routing certificates is raw-lex0, on the opposite side of the old apex architecture. Both actual unstable vertices have degree3. This is genuine root and interface turnover, not preservation of the old apex under a new name.

The unwanted unstable vertex48 has neighbors `[18,31,83]` and owner supports `[1,2,25]`. Root0 has neighbors `[1,5,74]` and owners `[2,7,52]`. Both unstable vertices lie on the sole stable facet, support2.

The construction originated from the literal C506 branch, moved the apical/support geometry, and then repeatedly removed physical supports while solving the filled-mass controller. The first beam used depth30/width5 and visited 14,886 attempted states. The second used depth35/width5 and visited 11,885. The selected checkpoint was at depth21 of the second beam, not its last layer.

**A numerical topology correction matters here:** the scout reported V90/E154/F66 and S1/U3. The rounded rational checkpoint and complete exact hull instead have **V94/E160/F68 and own121**. The latter is the construction being reported.

### Exact global barrier, not a local residual

A complete true-edge tree/cut certificate at the actual filled centroid proves

`-601/1000 < beta_physical < -149/250`.

The attaining physical cut is `[28,31,48]`, with **43 outward boundary arcs**. The physical rooted tree has93 arrows. The centered-polar rooted tree has67 arrows, each with angular escape greater than `1/10000000000`.

Thus this is a much smaller monostable body, but its remaining physical basin is **not nearly removed**. Its numerical physical bottleneck is about -0.59839. The very low edge count should be used to replace that basin's exposed interface and mass distribution, not to interpret a small local hinge as success.

### Fraction reduction and the G5M2 repair

The same architecture was independently reconstructed and audited at several rational grids:

| Version | V/E/F | Own strict | Max raw-coordinate numerator/denominator bits | Minimal common centered denominator bits |
|---|---:|---:|---:|---:|
| Original G10 | 94/160/68 | 1/2/1 | 134/134 | 20694 |
| `COMPACT_COARSENED_G8` | 94/160/68 | 1/2/1 | 109/109 | 16094 |
| `COMPACT_COARSENED_G6` | 94/160/68 | 1/2/1 | 83/83 | 11556 |
| **`COMPACT_COARSENED_G5M2`** | **94/160/68** | **1/2/1** | **67/67** | **9448** |
| Uncorrected G5 | 94/160/68 | 2/2/2 | 67/67 | 9446 |
| G4 | 94/160/68 | 20/2/20 | 58/57 | 7234 |
| G3 | 94/160/68 | 27/2/27 | 43/43 | 5017 |

All rows have weak-only000 and completed independent A/B/centered-mass checks.

The G5M2 repair is an exact finite change: round the normalized polar data to grid10^5, increase the **x numerator of input support38 by2**, then complete the common apical-incidence equation. This restores monostability lost by the unmodified G5 rounding. The exact full input and reconstruction code are in the standalone capsule; the instruction alone is not a replacement for that input.

For G5M2, the degree41 point is

`(-4699/100000, -1319/100000, 52323/50000)`.

Its maximum H-integer length is35 bits; raw centroid lengths are9420/9442; centered coordinate lengths9446/9446; volume lengths4730/4730. The actual roots and saddle remain `[0,48]` and `[0,74]`.

G6 has the larger numerical polar margin, approximately1.6453e-5, while G5M2 has the cheaper arithmetic and a numerical polar margin approximately9.324e-7. Both received fresh exact true-edge physical/polar gate checks. These numerical margins are scouting summaries; the exact gates, not their decimal approximations, are the certificates.

### Exact minimum31 free links

At the actual centroids of both the original G10 and G5M2 C320 bodies:

**No strictly positive free escape path of30 or fewer links leads from bad vertex48 to any existing vertex. A31-link path to root0 exists, with rational intermediate points.**

Only six existing vertices have larger radius than48: `[0,1,2,3,4,6]`. The other88 targets are excluded for every path length by strict radial increase. Exact angle/radius bounds exclude up to30 links for the six remaining targets. A literal rational31-link witness is stored, with30 intermediate points on denominator10^12 and every angular arrow greater than1e-6.

This is a **fixed-endpoint, fixed-own-center free-path result**. Intermediate points are free in space. It is not a convex-hull realization, not a fixed-incidence theorem, not an affine exclusion, and not an edge-complexity lower bound.

The exposed-interface issue is explicit: **all30 intermediate points of this particular minimum-length witness violate old stable support2**, and its16th intermediate point has normalized support ratio greater than4. This excludes retaining that support while adding this witness. It does **not** exclude every possible31-link path subject to that halfspace.

The complete exact report markers were observed for both inputs:

`SC83_C320_EXACT_MINIMUM_31_FREE_LINKS_ALL_EXISTING_ENDPOINTS_PASS`

G10 report:1343bytes, SHA-256 `e6fa512c83e77eee6ea4f335d9e6278a25b5840567e395f0241f8c430b04bdf0`.

G5M2 report:1354bytes, SHA-256 `f73f651584fc93282d7ddd49bd99b0640f62a3960d26a0c7a112143a06d86787`.

### Why the free-path criterion is exact

For nonzero centered endpoints u,z, let R=|z|/|u| and phi=angle(u,z). A positive arrow x→y means x·(y−x)>0. Writing successive radii r_i and angles theta_i, this is

`r_(i+1) cos(theta_i) > r_i`.

Consequently all theta_i<pi/2 and

`R product_i cos(theta_i) > 1`.

The spherical triangle inequality gives sum theta_i≥phi, and concavity of log cos gives

`product_i cos(theta_i) <= cos(phi/n)^n`.

Thus a free n-link path exists exactly when

`phi/n < pi/2` and `R cos(phi/n)^n > 1`.

Sufficiency follows by equally spaced directions along a shortest great-circle arc and a common radial ratio R^(1/n). Strict inequalities allow rational approximation of the intermediate points when the endpoints are rational. The body-specific minimum31 statements additionally require the exact endpoint data and interval certificates in the recovery capsule.

## 3. Main monounstable construction: C510 with extremely small coordinate complexity

### Opposite-side material changes the physical problem

Starting from the exact C320 G5M2 body, I took its actual centered vertices and the complete30-point free-chain witness. I then added **opposite-side physical points**, recomputing the ordinary filled hull centroid at every accepted step.

For an existing point y, proposed points used

`p = y/2 + (1-epsilon)|y|n/2`, with |n|=1.

Since p is strictly inside the ball with center y/2 and radius |y|/2, it satisfies p·(y−p)>0. This gives an explicit reference-center escape to y. The reference escape is only a proposal mechanism; the final actual-centroid audits are separate.

The material search used seed83190, a1500-point proposal pool, at most150 rounds, and true-edge ceiling310. It accepted47 new points. The complete input list then had171 points, with87 exposed vertices. The finite numerical run ended at iteration47 with `NO_DESCENT`, actual centroid norm approximately1.0264210796e-6, and both reference and own numerical S/U counts7/1. This small residual was not called an exact centroid lock.

I rounded the87 exposed vertices to common grids10^8 and10^10, reconstructed the complete exact hull, recomputed its exact own centroid, and independently audited every equilibrium feature.

### Exact outcome

Both rational versions are **V87/E255/F170, own7/1/6, weak000, primitive zeros000**, with170 positive centered tetrahedra and exactly zero centered first moments.

For **`SC83_C510_OUTSIDE_MASS_G8`**:

- The sole unstable vertex is raw-lex18, degree4, at
  `(-9776637/12500000, -1039321/10000000, -54859299/50000000)`.
- Stable input supports are `[3,114,129,161,165,167,168]`.
- Saddles are `[[43,45],[50,63],[63,75],[75,86],[81,82],[81,86]]`.
- All170 maximal faces are triangles.
- Maximum raw-coordinate lengths are27/27 bits; raw centroid88/110; centered coordinates110/110; volume75/74.
- **Minimal common centered denominator:113 bits.**

The distinct G10 body has the same V/E/F and mechanical class, but different rational coordinates. Its common centered denominator is139 bits. The input-support numbering differs after exact hull sorting; matching counts do not identify the two bodies.

The exact hull proof includes both containments: every input point satisfies all reconstructed halfspaces, and every vertex of the independently reconstructed halfspace hull is an input point. Thus the claimed hull is not merely a list of numerical triangles.

### Both sides have complete true-edge certificates

For both G8 and G10:

- A physical rooted tree with86 arrows has every angular escape greater than **1/10000000**.
- A169-arrow centered-polar tree and a60-vertex polar cut with42 outward boundary arcs certify
  **`-113/250 < beta_polar < -451/1000`**.

The physical basin is genuinely repaired at the actual uniformly filled centroid. The polar basin is still substantial, approximately -0.451. This is a useful opposite mechanical frontier, not an own110 claim.

Observed marker:

`SC83_OUTSIDE_MASS_EXACT_OWN_U1_TREE_AND_DUAL_TRAP_PASS 487 cb4e3be9de2e8b5164260f33f48a17d4865e0e277582e7e475dbeaa1f79cb984`

### Finite all-vertex polar continuation

A reusable continuation works directly with all87 physical vertices, not a fixed support/controller chart. At every trial it computes the filled centroid from the current oriented hull, centers the physical points, reconstructs the polar vertices, and evaluates both true-edge bottlenecks. Automatic differentiation includes the ordinary mass calculation. The optional contact-crossing mode discards old nonowner-slack constraints and rebuilds the hull after contact changes.

With87 physical vertices, any resulting convex hull has at most3·87−6=255 edges. This gives a topology-independent edge ceiling for that vertex-description search, even when the triangulation changes.

Two finite runs completed without an own110 endpoint:

| Mode | Maximum steps / initial trust / physical margin | Observed stopping point |
|---|---|---|
| Fixed chamber | 300 /0.01 /1e-9 | Iteration103, trust floor; S/U7/1; physical beta≈9.953e-10; polar beta≈-0.40202646 |
| Contact crossing | 700 /0.02 /1e-9 | Iteration242, trust floor; S/U7/1; physical beta≈5.00086e-10; polar beta≈-0.39335267 |

The second run approached nonowner slack approximately7.37e-14. Neither numerical endpoint was promoted as a new exact body. The complete method and its settings are preserved in the artifact capsule; the exact continuation parent remains the audited G8 body.

## 4. Whole-chain envelopes: a uniform-filled mass obstruction that changes the next move

I also built complete multi-step physical routes directly on the literal C544/C506 parents, rather than repeating their old single-relay grids.

The fixed reference center for these experiments is

`c0 = (-1352037528797, 572276679414, -940951259941)/100000000000000`.

The C544 routes use9 and6 links from the two unwanted unstable vertices to the retained apex, adding13 points. The C506 routes use9,9 and6 links, adding21 points. Let H be the convex hull of all old and added points. Let K be the convex hull of the protected route endpoints, the retained root, and the added route points.

The full H bodies, the protected K bodies, and the clipped pieces used in the proof were exactly reconstructed. Their ordinary filled moments were evaluated independently; this is not a discrete point-mass argument.

| Envelope | Actual V/E/F | Own strict | Weak | Centered tetrahedra |
|---|---:|---:|---:|---:|
| `SC83_CHAIN_544` | 155/316/163 | 19/25/42 | 000 | 306 |
| `SC83_CHAIN_506` | 131/289/160 | 12/27/37 | 000 | 258 |

The C544 envelope exceeds E310 and is deliberately retained as a material nonwinner. The old apex no longer has degree44: its actual degree is35 in CHAIN544 and13 in CHAIN506. The chains have a certified reference-center U1 routing structure, but neither filled body is own-U1.

### General envelope theorem

For a fixed vector a, define

`L = integral_(K intersect {a·(x-c0)>=0}) a·(x-c0) dx + integral_(H intersect {a·(x-c0)<=0}) a·(x-c0) dx`.

For **every measurable uniformly filled set P with K subset P subset H**,

`a·integral_P (x-c0) dx >= L`.

Proof: on the positive side, P must contain the positive part of K, while all additional material has nonnegative contribution. On the negative side, P is a subset of H, so its negative contribution is no smaller than that of all of H's negative part. Add the two inequalities.

Since volume(P)≤volume(H), when L>0,

`|g(P)-c0| >= L/(|a| volume(H))`.

This includes **all convex cuts, any number of moving corrective planes, and every other uniformly filled subset between K and H**. It is stronger than failure of a particular mass-controller solver.

For the exact envelopes, the verified instances are:

| Envelope | a | Exact excluded own-centroid ball |
|---|---|---|
| CHAIN544 | (2,9,4) | radius1/25 about c0 |
| CHAIN506 | (-3,7,6) | radius1/8 about c0 |

Approximate achieved lower bounds are0.0485053 and0.131253, respectively. The exact proof files, not these decimals, determine the inequalities.

This is **not** an exclusion of moving K, moving the desired center outside the stated ball, changing metric, or adding material outside H. Its constructive consequence is that preserving these route skeletons while merely cutting the existing envelope cannot restore the intended small-center configuration.

### An exact lower bound on required external material

Suppose a convex body P contains K, has centroid c0, and has the same fixed unique unstable root z=(0,0,1). Its farthest vertex must be z, so P lies in the radius R=|z−c0| ball about c0. Material outside H can contribute at most |a|R times its volume in the compensating direction. The previous inequality therefore gives

`volume(P outside H) >= L/(|a|R)`.

The exact instances imply external volume greater than **7/200** for CHAIN544 and **29/250** for CHAIN506.

Allowing the centroid to move within1/10000 of c0, while retaining K and the same fixed unique unstable root, still gives external-volume lower bounds **17/500** and **23/200**, respectively. The verification uses a radius bound1.01 and the containing-cube bound8R^3 to control the allowed centroid moment.

This explains why the successful physical-basin repair above adds exposed opposite-side material rather than searching another cap inside the old envelope.

### Independent clipped-moment verification

All four clipped integrals used by the two envelope certificates were independently reconstructed as rational halfspace bodies, fully audited by A/B, and separately integrated after centering. The volumes and all three first moments agreed with the envelope calculation.

Observed marker:

`SC83_ALL_FOUR_CLIPPED_MOMENTS_INDEPENDENT_AB_MASS_PASS 2379 97a3ace20c6cf400c45fe96f1c9f5ca6148d4a4d3d01f5e127843b38bde89929`

External-material bound marker:

`SC83_EXACT_NEW_MATERIAL_VOLUME_LOWER_BOUNDS_PASS`

Report:1636bytes, SHA-256 `1fda4581977d8deffa99a6ebd477cfbba858fe6cb4a1ee5e83aac250bdc18a5a`.

## 5. Other exact constructions retained, including nonwinning interface improvements

The search also released complete apical polygons, added whole support blocks, allowed root turnover, and reversed the low-order polar architecture. These outcomes are retained rather than discarded for not improving the main mechanical class.

| Exact construction | V/E/F | Own strict S/U/H | Common centered denominator bits |
|---|---:|---:|---:|
| `SC83_C560_APEXFACE6_OWN1_42_41` | 173/280/109 | 1/42/41 | 44928 |
| `COMPACT_ADVANCED_G6` | 173/280/109 | 1/42/41 | 20184 |
| `SC83_C578_FREE44_G10` | 179/289/112 | 1/61/60 | 36778 |
| `SC83_C576_FREE45_G10` | 178/288/112 | 1/61/60 | 36718 |
| `SC83_C290_APICAL8_TWO_POLAR_CHAINS_OWN2_11_11` | 94/145/53 | 2/11/11 | 21717 |
| Compact C290-family G6 | 102/153/53 | 2/11/11 | 10636 |
| Compact C290-family G7 | 102/153/53 | 2/11/11 | 12947 |
| Compact C290-family G8 | 102/153/53 | 2/11/11 | 14947 |
| `SC83_C138_REVERSED_POLAR_G10` | 46/69/25 | 2/4/4 | 8896 |
| `SC83_C144_REVERSED_POLAR_G10` | 48/72/26 | 2/3/3 | 9269 |

Every table entry has weak-only000 and completed exact A/B/independent-centered-mass checks. Together with the seven C320 variants, two C510 variants, and two chain envelopes, these are **21 retained exact nonwinning bodies**.

For C560, all44 apical polygon contacts moved through a common planar map,75 other supports moved independently, and six caps were added. Its exact physical bottleneck lies between -0.071 and -0.070, with a104-vertex cut and70 outward arcs; the polar tree is positive. `COMPACT_ADVANCED_G6` preserves that topology and mechanical class with raw-coordinate lengths81/82 bits.

For C578, all44 apical polygon points moved independently in their two-dimensional contact chart, rather than only through one common map. Its exact physical bottleneck is between -0.035 and -0.034. C576 promotes former free support33 to a45th apical contact and then releases the entire45-gon. Its exact physical bottleneck is between -0.034 and -0.033; its physical cut contains176 vertices and46 outward boundary arcs.

For comparison, exact parent certificates put both literal C544 and C506 physical bottlenecks between -0.437 and -0.436. The C576 interface therefore reduces the magnitude of the certified global physical barrier by a factor greater than218/17. However, it creates61 unstable equilibria. **Barrier improvement alone is not mechanical simplification.**

Two additional topology corrections must survive continuation:

- In the C290 architecture, the old point(0,0,1) is cut off by input supports77 and78. It is not an8-valent or44-valent retained apex.
- A floating compact-G8 scout reported V97/E148; the exact compact C290-family G8 hull is **V102/E153/F53**.

The C560 centered-mass checker uses a nonminimal integer embedding with44,957-bit denominator. The reduced common centered-coordinate denominator is44,928 bits. These are different arithmetic representations of the same body, not conflicting geometries.

## 6. Complete verification methods and what the finite searches do not establish

### Independent exact audits

Auditor A enumerates rational support triples, certifies boundedness, reconstructs maximal polygon faces and true edges, checks oriented incidence and connectivity, integrates ordinary filled volume and first moments, and checks every face, every vertex against all other vertices, and every true edge for strict and weak equilibrium conditions.

Auditor B independently clips support-pair lines, reconstructs vertices and cycles using different predicates, integrates with a different rational interior-base triangulation, and uses independent feature formulas. Its canonical reports agree byte-for-byte with A.

A third integration shifts the body by the exact filled centroid, uses positive integer tetrahedra, matches the independently computed volume, and verifies exactly zero centered first moments. The fixture suite checks the tetrahedron and prism strict/weak cases and rejects three invalid inputs.

For the new grid-V C510 bodies and chain envelopes, additional checks establish both containments between the proposed point hull and the independently audited halfspace hull. All reported E values are edges of the actual maximal complex, not triangulation diagonals.

### Exact angular tree/cut arithmetic

For x=N/s and y=M/t with positive denominators, set

`alpha=N·N`, `beta=M·M`, `gamma=N·M`,

`D=s*gamma-t*alpha`,

`R=s*s*beta-2*s*t*gamma+t*t*alpha`.

Then

`W(x,y)=D/sqrt(alpha*R)`.

A negative bound W<−p/q is equivalent to the integer conditions D<0 and q²D²>p²alphaR. Positive bounds are handled analogously. No floating square root enters the exact gate verification.

For a chosen root, a rooted tree with all arrows exceeding a proves beta>a. A root-excluding cut whose every outward arrow is below b proves beta<b. The tree and cut use **true hull edges**, including the centered-polar true complex. Their literal arrays are in the source capsule.

### Finite numerical campaigns

The capsule preserves the complete geometry model, ordinary-mass derivatives, Newton/Armijo controller, whole-support beam, full-apical-polygon continuation, whole-chain proposal mechanism, rational rounding/repair, opposite-material search, and the all-vertex polar continuation. Numerical dependencies were NumPy2.3.5 and SciPy1.17.0; the all-vertex automatic-differentiation continuation additionally used Torch2.10.0+cpu. Exact reconstruction and verification require only CPython3.13.5's standard library. Numerical runs used one OpenBLAS/OMP thread.

Two low-C full-support continuations each completed3500 accepted steps. One ended at numerical S1/U3 with physical beta about -0.48478; the other at S1/U2 with physical true-edge beta about -0.55737. Its all-point escape diagnostic was about -0.51326 and must not be substituted for the true-edge bottleneck. Neither numerical endpoint was promoted.

Two later coarsening beams from exact G6, each depth30/width6 with8947 attempted states, did not produce S/U1/1. Their final numerical38/74/38, S2/U2 outputs were not promoted as exact successors.

These are finite observations. They exclude neither the continuous support families nor their affine orbits. An unsuccessful mass-controller run is not evidence against the general cap-mass existence theorem.

## 7. Recovery artifacts, exact identities, and observed final replay

### Complete standalone artifact

Standalone complete decoder: RECOVER_SC83.py

Decoder: **84671bytes**, SHA-256

`c0db93b8cd233c405fece8510bd3a9f70cdc85150486df2e5cad69978385a7b6`.

It contains59 source/data units:58 manifest-listed units plus the manifest. It includes the needed parent reconstruction sources, exact new inputs, exact generators, independent auditors, mass checker, literal routing/cut and free-path certificates, numerical methods, and pinned campaign settings. No numerical optimizer or library fetch is needed to recover the retained exact bodies.

Internal capsule identities:

| Layer | Size | SHA-256 |
|---|---:|---|
| UTF-8 source dictionary | 217558bytes | `8646632341388208c7c35dabe595fb9fdc9abc0aa73546f8fbf08f52a455a65b` |
| XZ | 61784bytes | `e939d9163f3499b7ded6c6113e09d5309b0c3499de8d157feb75c6a171874a53` |
| Whitespace-normalized base64 | 82380characters | `68b99c7230013eac5ecbf46a336b652d6da98818ca9dc3ddd1e0fae66a0b4dde` |

The decoder checks all these identities and every manifest-listed source identity. Its output directory must be fresh:

```sh
python -B -S RECOVER_SC83.py SC83_source
```

Observed recovery marker:

`SC83_STANDALONE_SOURCE_RECOVERED 59`

The full source-only replay completed first from the assembled source and then independently from the freshly decoded source. Both reached:

`SC83_COLD_SOURCE_ONLY_ALL_RETAINED_AB_MASS_BOTTLENECK_AND_ENVELOPE_PASS 3745 df9dea55877a897967e549bea53caefc6f310ce350d25955cb29b48a4c142aa1`

The terminal receipt pins58 source identities and29 regenerated output receipts/certificates; each body receipt additionally pins its generated raw geometry, A/B reports, centered-mass report, and arithmetic-cost report. The final decoded replay was observed through its terminal marker, not inferred from intermediate output.

Expanded prepared handoff (`HANDOFF_PREFIX.md`) and capsule identity sheet (`HANDOFF_IDENTITIES.md`) accompany the source.

Complete research archive, including standalone source and working records (`SC83_RESEARCH_HANDOFF.zip`)

The archive's observed size is18,868,999bytes. The decoder hash above is the pinned recovery identity; no unverified archive hash is asserted.

### Selected exact checkpoint identities

These names and hashes identify the generated artifacts inside the recovery, not standalone recovery recipes:

**C320 original G10**

- `COARSENED_INPUT.json`:5742bytes, SHA `27fdf13aadc1dadb47417980020b1925f4bfa81aaeeb5e1fdcb83d86416d6921`.
- Raw H:5014bytes, SHA `8b3e660a1efb54db9fa1e8e452c0a7ae7d4414b36e97d5e188d62122d46180ad`.
- A=B:114027bytes, SHA `cf8ba91e13f69d070dd896e3b4506fd08e9097012f6d797ce534aa457544e1f6`.
- Receipt:815bytes, SHA `ef6c7b10ea84dc70e329ab84310f5d968b257d25b70505f83da11d2a2b4c6f90`.
- Marker: `SC83_C320_WHOLECOARSEN_H41_OWN121_EXACT_AB_MASS_ROOT_TURNOVER_PASS`.

**C320 G5M2**

- `grid5_checkpoint.py`:1699bytes, SHA `28e967e351b054d170ee8ac6536771ad7ba4863e79c8b7e7fb31034b2327b551`.
- Raw H:2780bytes, SHA `4a2f1a1c6cdc85b9e6a40b73fbd5aca6f9d2bb3ca772fc1c85e97e3a57650a1e`.
- A=B:57664bytes, SHA `81bea8769ec4eaacf6eca0d1c26f3f3e1b90da814644a6737378e1267beff085`.
- Receipt:645bytes, SHA `db88eeeef3c0f0e0ebaab9918c18b2f39c7a1c99829dca56ff4914d0a21d43c5`.
- Marker: `SC83_C320_G5M2_OWN121_EXACT_AB_MASS_PASS`.

**C510 common-grid G8**

- `OUTSIDE_HULL_G8_INPUT.json`:4625bytes, SHA `36e8529128572f8330ac0b60e69c64ec6aa996e380cf727d399d514f8a4b3d6f`.
- `outside_checkpoint.py`:1696bytes, SHA `91e166e34a05ffde4d56c40bcfb211d5c5e8e1d6c0b5f313085deb1b7cb64572`.
- Raw H:16329bytes, SHA `8e944447b325009477470cb935c2ddb7fb34bfa26b82149f3f8dbe1ee7820be9`.
- A=B:33700bytes, SHA `1adc0bf2cb499787ff5e06834a76265318ef29e825caaddd5e7a565d3cc6a961`.
- Receipt:753bytes, SHA `5efe2194ebf97137b369bfa86f2f2838866592c03fe3fed7c4f864c88df3eec4`.
- Marker: `SC83_C510_OUTSIDE_MASS_G8_EXACT_HULL_AB_MASS_PASS`.

**C510 common-grid G10**

- `OUTSIDE_HULL_G10_INPUT.json`:5150bytes, SHA `f3e6fb31165dfc17179463a1e52e272a2b527707a5297cfa7b5b33ccb269ffcb`.
- A=B:38919bytes, SHA `95b503d8d712d0c46f74d3902f2ef840ca89776e0334908c2547982d4bfda270`.
- Receipt:754bytes, SHA `e74e7ad2b6d74bb67d035d191d2142f757c820775bd0a5722a7fe7f1a748efb5`.

**Envelope proof inputs and outputs**

- `ENVELOPE_INPUTS.json`:9613bytes, SHA `6e7ea8703733d96f1676b0ab1b2107cb14778d83ce8edd3e9daa9979a5d8542c`.
- CHAIN544 proof:130384bytes, SHA `326580a510d1af07f7390d01276c963d1e9fba8bb25e4ed29f72b1fd4d3f198d`.
- CHAIN506 proof:132067bytes, SHA `c6466f18af2555aad704ab1b7d838c2a3fee5db345fe350ff4b49ec10f7eab86`.

## 8. Consequential continuation

The next constructive choice is between two qualitatively different architectures.

**For a monostable starting point, use C320 G6 or G5M2.** Keep G6 when the larger polar margin is useful and G5M2 when arithmetic cost matters. Release the old stable support2 and the entire physical closed-cut interface rather than trying to append the certified31-link chain behind a support that cuts every one of its intermediate points. The degree41 point is geometric structure, not the actual unstable root; do not root-lock it accidentally.

The68-support representation gives an additional rigorous budget advantage: any bounded full-dimensional deformation using at most68 halfspaces has F≤68 and hence E≤3F−6≤198, even if all old high-degree contacts split. Thus retaining the present degree41 incidence is unnecessary merely to stay below E310. Adding at most37 further supporting planes still gives the unconditional bound E≤309. This is a combinatorial resource for whole-interface redesign, not a promise of mechanical feasibility.

**For a monounstable starting point, use C510 G8.** Its113-bit centered arithmetic and87-vertex description make repeated exact audits unusually inexpensive. Its physical positive tree is already exact at the actual centroid. Replace the entire60-vertex centered-polar trapping region, permitting contact turnover and genuine material changes, rather than driving one stable-face residual to zero. The87-vertex search chart has E≤255 automatically, leaving room to add physical vertices as well.

The whole-chain envelope certificates explain a concrete failure mode: keeping the route skeleton and trying to repair mass only by cutting inside the old envelope is impossible in the stated centroid balls. The C510 construction demonstrates a way past that obstruction by adding exposed opposite-side material. The remaining stable-side repair must again be checked at the newly recomputed ordinary-volume centroid.

**Unfinished:** no construction here has own110/weak000; the numerical polar continuations stopped with seven stable equilibria; and the complete source capsule, although built and twice successfully cold-replayed, has not been reproduced literally inside this immutable Markdown value. Until that last recovery condition is satisfied, the exact new geometries are reported as verified artifact-backed nonwinners, not durable replacements for the literal parent.
