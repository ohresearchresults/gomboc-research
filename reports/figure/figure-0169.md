# figure-0169

AI research report · 2026-08-30 UTC

---

# Sharp Harbor 48 continuation — exact acute-component-merging M42 fifth cell

## Literal verdict

**NONWINNER, but a strict one-pair advance.** I did not obtain a homogeneous convex polyhedral Gömböc with strict own-centroid `(S,U,H)=(1,1,0)`. I did obtain and independently certify a new exact rational, uniformly dense, own-centred convex polyhedron with

```text
(S,U,H)=(2,1,1).
```

This is the first endpoint in the exact M42 lineage that reduces the fourth-stage `(extra S, extra U, two H)` residual block to one Euler-neutral `(extra S, one H)` pair. The construction replaces the fourth endpoint’s separated cancellation sectors by a connected, finite-thickness, two-rail volumetric complex. It deletes the old extra unstable equilibrium, both old saddle edges, and the external-positive edge obstruction; it also merges the formerly disjoint acute true-edge components. The result is exact for the materialized endpoint and its certified coordinate box. It is not a global nonexistence theorem.

## Reproducible artifact

- Complete exact bundle (`M42_acute_bridge_fifth_cell_complete.zip`), SHA-256 `1648d8f7ae35097d1d9a60196353dfa14f120ed617bd1e9e902264a6dd50d820`; ZIP checksum (`M42_acute_bridge_fifth_cell_complete.zip.sha256`).
- Self-contained research handoff (`RESEARCH_HANDOFF.md`), SHA-256 `6825dcbc57747eb7458e3273ec714ffea8f16e7917451c76b0021998681d2c2a`.
- Final combined verification transcript (`FINAL_VERIFICATION_SUMMARY.txt`), SHA-256 `7257eccdea27951b63f8e64f8d2effe78854d0b081c117cfa558a879e5887822`; it ends with `ALL FINAL COMBINED VERIFIERS PASS`.
- 127-file SHA-256 manifest (`SHA256SUMS.txt`), integrity verifier (`verify_integrity.py`), and integrity result (`INTEGRITY_VERIFICATION.txt`). I unpacked the final ZIP separately and reran the integrity verifier successfully.

## Exact three-stage lineage

| stage | input rows | actual `(V,E,F)` | strict class | decisive residual |
|---|---:|---:|---:|---|
| M42 three-cell parent | 134 | `(92,256,166)` | `(2,2,2)` | external-positive `(153,154)`; exact shortest acute route to target 8 has 56 edges |
| cross-gap fourth cell | 140 | `(83,229,148)` | `(2,2,2)` | external-positive `(226,227)`; positive-dot graph splits `45+38` |
| acute-bridge fifth cell | 119 | `(61,163,104)` | **`(2,1,1)`** | stable `[198,224,258]`; sole saddle `(229,247)` |

The package contains all three complete exact stages. The parent clean-room verifier independently enumerates all supporting triples, reconstructs 166 maximal faces and 256 true edges, recomputes exact volume/centroid/zero translated moments, and exhaustively obtains stable faces `[0..16]`, `[201,220,221]`, unstable vertices `8,153`, and saddles `(130,222),(176,182)`. Exact multiplicative Dijkstra proves the 56-edge route deficit at `(153,154)`.

The parent-to-fourth verifier reconstructs the exact projective/linear/common-lattice lineage, the four linked nonsimplicial cells, rank-five moment/topology control system, and the fourth endpoint’s complete `(83,229,148)` lattice. The fourth endpoint deletes the parent packet but transfers it to stable `[195,224,223]`, unstable `227`, saddles `(135,224),(183,223)`, and edge `(226,227)`. Its exact positive-dot graph has components of sizes 45 and 38, with all 1,710 cross-component vertex pairs strictly negative.

The new fourth-to-fifth verifier (`verify_fourth_to_fifth_lineage.py`) proves that the fifth generator is exactly the 83 actual fourth-stage vertices, unchanged as rational points, plus rows `229..264`; it independently reconstructs the transition from `(2,2,2)` to `(2,1,1)` and the acute-graph merger. The corresponding exact certificate is here (`fourth_to_fifth_lineage_certificate.json`).

## Authoritative fifth-stage H/V/E data

The authoritative finite generator is input_rows_common_lattice.csv, SHA-256 `3619a51daacb422b3908fa2f0a4a4343fe03fd99ea12e362bf8fb53535ee385d`. Every row is

```text
q_i=(x_int,y_int,z_int)/S,
S=66545713204251021392211086000000000000.
```

It has 119 rows: the 83 exact active fourth-stage vertices and 36 new bridge rows.

Active rows:

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
54 69 72 73 88 198 224 228
229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246
247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264
```

Inactive rows:

```text
86 114 115 116 117 118 119 121 122 123 124 125 126
131 132 133 135 136 137 138 139 140 141 142
159 160 161 162 163 164 165 166 167 168 169 170 171 172 175
183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
223 225 226 227
```

Complete machine-readable data are materialized as all exact coordinates (`coordinates_all_exact.csv`), 61 centred vertices (`coordinates_active_centered.csv`), 104 irredundant halfspaces (`halfspaces_centered.csv`), all maximal-face cycles (`face_cycles.json`), all 163 true edges (`true_edges.csv`), all face mechanics (`faces_mechanics.json`), all vertex cones (`vertices_mechanics.csv`), and all four-component edge cones (`edges_four_component_audit.csv`).

## Exact volume, moments, and own centroid

Exact volume:

```text
34980705315936112950597397877275192308504202695136552026913831549/
33272856602125510696105543000000000000000000000000000000000000
```

Decimal `1051.32858696904`.

Exact unshifted centroid:

```text
Cx=-150300507102663524167538610416232307159919486469428298461058355276598660214157/
    167907385516493342162867509810920923080820172936655449729186391435200000000000

Cy=1995601915580677811515128773908322575378398359110643742476476989747812354187329/
   839536927582466710814337549054604615404100864683277248645931957176000000000000

Cz=-4302643372999357052165197955427950881004198712929763820230922537671898969190922052651854947009813907649/
    27933791803640444262551240155536974552768263548574941197309387646366035984119639551052226568000000000000
```

Direct signed-tetrahedron summation proves `M_k-V C_k=0` in all three coordinates. The dependent translation `tau=-C` therefore gives first moments exactly `(0/1,0/1,0/1)`. Its moment Jacobian is `V I_3`, with exact determinant `V^3>0` and rank 3. The complete exact mass record is in certificate.json, SHA-256 `a27d8db90a4190e200e6e4afbf1e4224f90edd5e45ea5aa3acc3016dbc281689`.

## Exhaustive equilibrium classification

Stable maximal faces:

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  margin 0.8846185087647226
[198,224,258]                                      margin 0.6819299931297264
```

Unstable actual vertices:

```text
8  margin 0.17161774899559706
```

Saddle true edges:

```text
(229,247)  four-component margin 0.49588368820124096
```

Global normalized minima:

```text
stable positive          0.6819299931297264
nonstable exclusion      0.5969553981139437
unstable positive        0.17161774899559706
nonunstable exclusion    0.012941543497126081
saddle positive          0.49588368820124096
nonsaddle exclusion      0.07486075810588302
active topology distance 3.869169282446602e-6
inactive distance        0.0024540435840961394
```

Thus the extra unstable branch is exactly gone: `U=1`. Euler’s relation is carried only by one extra stable face and one saddle.

## Two exact 19-edge acute bridges

The short/east rail is

```text
228-229-230-231-232-233-234-235-236-237-238-239-240-241-242-243-244-245-246-8.
```

The long/west rail is

```text
228-247-248-249-250-251-252-253-254-255-256-257-258-259-260-261-262-263-264-8.
```

Every listed pair is an actual true edge. For each directed step `a→b`, exact arithmetic proves both

```text
x_a·x_b>0,
x_a·(x_b-x_a)>0.
```

Consequently every nonterminal rail vertex has a strict outward witness toward protected unstable vertex 8. Minimum directed supports are `2.343592223102722` and `2.330631239732005`; maximum step angles are below 13 degrees. The exact fifth positive-dot true-edge graph is connected, with 134 positive-dot and 29 nonpositive-dot edges. The prior `45+38` component obstruction is therefore destroyed rather than merely regraded. Full exact graph data are in acute_bridge_graph.json, SHA-256 `8abe92c898864c637ccb04024cf5d7a8cb6ba3b20f021772c7156a041d0dfe40`.

## Shared-interior-edge volumetric replacement

The fifth-cell atlas (`fifth_cell_complex.json`), SHA-256 `536780178a08eab3ace137c7799967ae63395fda0835d243249b43f7822c7e9b`, contains 64 strict triangular-bipyramidal centroid-fan edge-star cells; 58 touch new rows. In every cell the two apex determinants have opposite nonzero signs, the apex segment meets the relative interior of the equatorial triangle, and all five segment/barycentric components are positive.

Two principal shared-interior-edge cells span the bridge:

```text
start cell:
  equator/interior edge star (O,229,247)
  apices 224,228
  minimum barycentric 0.12964301306695047

terminal cell:
  equator/interior edge star (O,246,263)
  apices 198,264
  minimum barycentric 0.0025858317729770437
```

All 95 boundary faces incident to new rows are triangular and cone to nondegenerate tetrahedra at the own centroid. Their shared-edge adjacency graph is connected. The minimum exact closure determinant is positive, decimal `1.9952773473691054`. This is a finite-thickness volumetric replacement, not another serial rail on the old graph.

## Exact packet transition

Rows `135,183,195,223,225,226,227` are now strictly inactive. The fourth-stage stable face `[195,223,224]`, saddles `(135,224),(183,223)`, and external-positive edge `(226,227)` are absent from the rebuilt lattice.

The residual packet is now exactly

```text
extra stable face [198,224,258]
sole saddle edge  (229,247)
extra unstable vertices: none.
```

The features are one incidence-star step apart: face `[224,229,247]` is incident to the saddle, while the stable face is limited by edge `(198,224)`; vertex 224 links the two stars. They are not yet incident to a single common cancelling true edge. The exact incidence packet is recorded in residual_packet_graph.json.

## Positive box and independent antibirth controls

Rows `0..16` and every inactive row are fixed. Every coordinate of the other 44 active rows—132 independent coordinates—may vary by exactly `±10^-12`. Directed rational/interval arithmetic preserves the entire `(61,163,104)` lattice, strict `(2,1,1)`, both rails, the connected positive-dot graph, all 64 cells, the connected 95-face closure, and all predecessor deletions.

Certified lower bounds include

```text
facet determinant             0.000133764629354541
inactive-facet determinant    0.0011149365236659242
nonunstable witness           2.3306312128008098
saddle component              0.49588368785363446
nonsaddle witness             0.006113447636252679
rail directed support         2.3306312128008098
positive-dot spanning graph   2.4554355280122913
cell tetra determinant        0.3593394902594666
cell barycentric              7.660526872790403e-6
closure-fan determinant       1.9952772649452366
```

See the interval certificate (`interval_certificate.json`), SHA-256 `50489534999e007bb0ef5799043cba913bdd51ed55ba886a9516b030d5675784`.

Two exact, disjoint one-sided antibirth controls remain inside this box:

```text
short rail: move row 232 along the centred row-231 direction;
            witness 231→232; support derivative 1071.7923953527013;
long rail:  move row 248 along the centred row-247 direction;
            witness 247→248; support derivative 1001.7367668354448.
```

For each control `0≤s≤10^-14`; maximum coordinate displacements are `2.504×10^-13` and `3.105×10^-13`. Their row supports are disjoint. Together with the three dependent translations, the exact combined control rank is 5. The control certificate (`control_certificate.json`), SHA-256 `9f272816cbe5881eb9b19cc4194ac877173b920652d00406c5e011bb44d7bd2d`, and independent control verifier (`verify_controls.py`) recompute these claims from the generator.

## Independent reconstruction and mesh parity

The clean-room exact verifier (`verify_exact_cleanroom.py`) uses standard-library `Fraction` arithmetic and does not trust stored H/E incidence. It enumerates every unique supporting triple among all 119 rows, independently reconstructs 104 maximal planes, 163 true edges, the connected Euler-2 boundary, exact volume/centroid/zero moments, every face/vertex/edge equilibrium cone, both rail inequalities, the connected positive-dot graph, all 64 strict bipyramids, the 95-face closure, predecessor deletion, and the residual S–H pair.

The matching OBJ (`body.obj`), SHA-256 `353267b2978ca69253a98752d23852ff3d075ba2a2eabf920de71b3fb5e1296e`, and STL (`body.stl`), SHA-256 `a78c9e4bc4e1f40f523477562ae255d16daeec63cd2ca0f6447b46d0333e0bcf`, are watertight and mutually consistent:

```text
vertices 61
triangles 118
triangulated mesh edges 177
Euler 2
volume 1051.3285869690405
centre-of-mass norm 1.1642871794121369e-16.
```

## What was tried and falsified

Beyond the exact construction, I recorded at least 4,973 explicit numerical evaluations around the fifth endpoint:

```text
317  double-rail parameter samples
1000 one-point stable-face cap/deletion scans
1200 two-point correlated stable/saddle cap scans
1200 structured stable-face-vertex replacements
1000 saddle support-plane completion scans
256  local deletion subsets.
```

No strict `(1,1,0)` state appeared. A mixed-integer affine-primitive center test reported the exact fifth incidence numerically infeasible even at zero margin; this HiGHS result is retained only as numerical evidence, not an exact obstruction theorem. Across the finite campaigns, local caps and replacements either preserve the sole S–H pair or transfer/multiply equilibria. The complete scope and files are in search_obstruction_summary.json.

## First topology not yet classified

The exact remaining local star is

```text
{198,224,258,229,247,228}.
```

The first nonduplicative topology is a **coupled two-cell bistellar S–H replacement**—a `2↔3 / 3↔2` pair, triangular prism, or octahedral complex—that replaces stable limiting edge `(198,224)` and saddle edge `(229,247)` inside one shared three-dimensional cell, or creates a new shared interior edge incident to both stars. Its two independent incidence coordinates must make the stable-foot death and saddle-beta death sheets overlap before any compensating U–H birth. It should preserve the base 17-gon, unstable vertex 8, both exact 19-edge rails, both antibirth directions, and the three dependent moment translations. The full exact local H/V/E/cone atlas is next_topology_atlas.json.
