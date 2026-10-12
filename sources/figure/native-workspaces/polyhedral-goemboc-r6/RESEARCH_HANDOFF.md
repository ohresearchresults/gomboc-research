# Sharp Harbor 48 continuation — exact acute-component-merging M42 fifth cell

## Literal verdict

**NONWINNER, but a strict one-pair advance.** No finite homogeneous convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)` was obtained. The strongest new exact object is a rational, uniformly dense, own-centred convex polyhedron with strict

```text
(S,U,H)=(2,1,1).
```

It advances the exact M42 line from the three-cell parent `(2,2,2)`, through the cross-gap fourth-cell endpoint `(2,2,2)`, to the first certified endpoint in this line with only one residual Euler-neutral pair. The two unstable branches and two saddle branches of the fourth endpoint are replaced by two exact monotone 19-edge rails. They close the extra unstable branch, delete the old obstruction edge, merge the previously disjoint acute components, and leave one extra stable face coupled to one saddle edge.

The negative statement is exact for this endpoint and its certified coordinate box. The broader search statements are finite empirical falsification, not a global nonexistence theorem.

## Reproducible lineage

The bundle contains all three exact stages and clean-room verification:

| stage | input rows | actual `(V,E,F)` | strict class | decisive residual |
|---|---:|---:|---:|---|
| M42 three-cell parent | 134 | `(92,256,166)` | `(2,2,2)` | external-positive edge `(153,154)`; exact shortest acute route to 8 has 56 edges |
| cross-gap fourth cell | 140 | `(83,229,148)` | `(2,2,2)` | external-positive edge `(226,227)`; acute graph components `45+38` |
| acute-bridge fifth cell | 119 | `(61,163,104)` | `(2,1,1)` | extra stable `[198,224,258]`; sole saddle `(229,247)` |

`verify_fourth_to_fifth_lineage.py` proves that the fifth generator consists exactly of all 83 actual fourth-stage vertices, with identical rational coordinates, plus new rows `229..264`. It also independently proves the class transition and acute-graph merger.

## Authoritative exact fifth generator

The complete generator is `fifth_cell_endpoint/input_rows_common_lattice.csv`. For each row,

```text
q_i=(x_int,y_int,z_int)/S,
S=66545713204251021392211086000000000000.
```

The table, not the floating design provenance, is authoritative. It has 119 rows: 83 inherited fourth-stage vertices and 36 new bridge rows.

Exact active rows:

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
54 69 72 73 88 198 224 228
229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246
247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264
```

Exact inactive rows:

```text
86 114 115 116 117 118 119 121 122 123 124 125 126
131 132 133 135 136 137 138 139 140 141 142
159 160 161 162 163 164 165 166 167 168 169 170 171 172 175
183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
223 225 226 227
```

All 104 irredundant halfspaces, 61 centred vertices, 104 actual maximal-face cycles, 163 true edges and the complete mechanics ledgers are materialized in CSV/JSON.

## Exact mass and hard moment closure

Exact volume:

```text
34980705315936112950597397877275192308504202695136552026913831549
/33272856602125510696105543000000000000000000000000000000000000
```

Decimal: `1051.32858696904`.

Exact unshifted ordinary-volume centroid:

```text
Cx=-150300507102663524167538610416232307159919486469428298461058355276598660214157
   /167907385516493342162867509810920923080820172936655449729186391435200000000000

Cy=1995601915580677811515128773908322575378398359110643742476476989747812354187329
   /839536927582466710814337549054604615404100864683277248645931957176000000000000

Cz=-4302643372999357052165197955427950881004198712929763820230922537671898969190922052651854947009813907649
   /27933791803640444262551240155536974552768263548574941197309387646366035984119639551052226568000000000000.
```

The three dependent controls are the exact translation `tau=-C`. Direct signed-tetrahedron summation proves `M_k-V C_k=0`; after translation all three first moments are identically zero. The translation-moment Jacobian is `V I_3`, with determinant `V^3>0` and rank 3.

## Exhaustive own-centroid equilibrium audit

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

Global normalized endpoint minima:

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

Every face-foot component, every adjacent-edge vertex support and all four components `(t,1-t,beta1,beta2)` of every true edge are exact and independently regenerated.

## Two exact 19-edge monotone rails

The short/east rail is

```text
228-229-230-231-232-233-234-235-236-237-238-239-240-241-242-243-244-245-246-8.
```

The long/west rail is

```text
228-247-248-249-250-251-252-253-254-255-256-257-258-259-260-261-262-263-264-8.
```

Every listed pair is a true edge. For every directed step `a -> b`, exact arithmetic proves

```text
x_a·x_b>0,
x_a·(x_b-x_a)>0.
```

Thus every nonterminal rail vertex has an outward witness toward the protected unstable vertex 8. The exact minimum directed support is `2.343592223102722` on the short rail and `2.330631239732005` on the long rail. Maximum step angles are below 13 degrees.

The fourth endpoint’s positive-dot graph had two exact components of sizes 45 and 38 and all 1,710 cross-component pairs were obtuse. The fifth endpoint’s positive-dot true-edge graph is connected, with 134 positive-dot and 29 nonpositive-dot true edges. Hence the precise fourth-stage acute-component obstruction is eliminated, not merely bypassed numerically.

## Shared-interior-edge volumetric replacement

The exact centroid-fan atlas contains 64 strict triangular-bipyramidal edge-star cells; 58 touch new rows. Each cell has opposite nonzero apex determinants, an apex segment crossing the relative interior of the equatorial triangle, and five positive segment/barycentric components.

Two principal shared-interior-edge cells span the bridge:

```text
start cell:
  true edge/equator = (O,229,247)
  apices = 224,228
  minimum barycentric = 0.12964301306695047

terminal cell:
  true edge/equator = (O,246,263)
  apices = 198,264
  minimum barycentric = 0.0025858317729770437
```

There are 95 new-row boundary faces. They are all triangular, all cone to nondegenerate tetrahedra at the own centroid, and their shared-edge adjacency graph is connected. The minimum exact closure determinant is positive; decimal `1.9952773473691054`.

This is a genuine finite-thickness replacement. It is not a serial regrading of the fourth endpoint’s old graph.

## Packet transition

The old fourth-stage rows

```text
135 183 195 223 225 226 227
```

are all strictly inactive. The following fourth-stage features are absent:

```text
stable face [195,223,224]
saddle edge (135,224)
saddle edge (183,223)
external-positive obstruction edge (226,227).
```

The fourth residual block `(extra S, extra U, two H)` therefore closes to one residual `(extra S, one H)` pair:

```text
extra stable face [198,224,258]
sole saddle edge (229,247)
no extra unstable vertex.
```

The two residual features are one incidence-star step apart. Face `[224,229,247]` is incident to the saddle edge; the stable face has limiting boundary edge `[198,224]`; vertex 224 connects their stars. They are not yet incident to one common cancelling true edge.

## Positive coordinate box and independent antibirth directions

Rows `0..16` and all inactive rows are fixed. Every coordinate of the other 44 active rows—132 independent coordinates—may vary by `±10^-12`.

Exact outward interval arithmetic preserves the full `(61,163,104)` lattice, strict `(2,1,1)`, both monotone rails, connected positive-dot graph, all 64 strict bipyramids, the 95-face connected closure and all predecessor deletions. Directed lower bounds include:

```text
facet determinant             1.337646293545410e-4
inactive-facet determinant    1.114936523665924e-3
nonunstable witness           2.3306312128008098
saddle component              0.49588368785363446
nonsaddle witness             0.006113447636252679
rail directed support         2.3306312128008098
positive-dot spanning graph   2.4554355280122913
cell tetra determinant        0.3593394902594666
cell barycentric              7.660526872790403e-6
closure-fan determinant       1.9952772649452366
```

Two disjoint exact one-sided shape controls are retained inside that box:

```text
short antibirth: move row 232 along centred row-231 direction,
                 witness 231->232, derivative 1071.7923953527013;
long antibirth:  move row 248 along centred row-247 direction,
                 witness 247->248, derivative 1001.7367668354448.
```

For each, `0<=s<=10^-14`; maximum coordinate displacements are respectively `2.504e-13` and `3.105e-13`. Their row supports are disjoint. Together with the three translations, the exact control rank is 5. `verify_controls.py` independently recomputes the volume and centroid derivatives and both support derivatives.

## Independent verification and mesh parity

`fifth_cell_endpoint/verify_exact_cleanroom.py` uses standard-library fractions and no stored H/E topology. It enumerates every unique supporting triple among all 119 rows, reconstructs exactly 104 maximal planes and 163 true edges, recomputes mass and centroid, audits every equilibrium cone, verifies both rail inequalities, reconstructs the positive-dot graph, checks all 64 bipyramids and the 95-face closure, and proves predecessor packet deletion.

The final combined rerun ends with:

```text
ALL FINAL COMBINED VERIFIERS PASS
```

Mesh parity for the fifth endpoint:

```text
61 vertices
118 triangles
177 triangulated mesh edges
Euler 2
volume 1051.3285869690405
centre-of-mass norm 1.1643e-16.
```

OBJ and STL reconstruct the same watertight oriented triangle set and agree with the exact maximal-face triangulation.

## Finite falsification after the exact endpoint

At least 4,973 explicit local numerical evaluations are materialized in `search_evidence/`: double-rail parameter samples, one-point caps, two-point caps, stable-vertex replacements, saddle support-plane completions and local deletion subsets. None produced `(1,1,0)`. A numerical mixed-integer affine-cone feasibility test also found no own-centre location giving `(1,1,0)` while the exact fifth incidence and coordinates are fixed. This MILP result is guidance only, not an exact obstruction theorem.

The repeated local behavior is pair transfer: a serial face move transfers the stable equilibrium to an adjacent rail face; a serial edge move transfers the saddle to an adjacent edge; aggressive caps produce compensating U-H births.

## First topology not yet classified

The smallest nonrepeating continuation is a **coupled two-cell bistellar S-H replacement** centered on the exact local star

```text
{198,224,258,229,247,228}.
```

It should replace the stable limiting edge `(198,224)` and saddle edge `(229,247)` inside one triangular-prismatic/octahedral volumetric complex, or create a new shared interior edge incident to both stars. The stable face-foot death wall and saddle beta death wall must overlap before any U-H birth. Preserve target face `[0..16]`, vertex 8, both 19-edge rails, two independent rail-antibirth controls and three dependent translations. At least three local topology controls are indicated: stable-foot death, saddle-beta death and a shared relay-overlap coordinate.

`fifth_cell_endpoint/next_topology_atlas.json` contains the complete exact local H/V/E and four-component mechanics data for that star.

## File map

- `parent_M42_three_cell_exact/`: independent exact reconstruction of the requested M42 parent, route obstruction, box and meshes.
- `fourth_cell_endpoint/`: complete exact cross-gap fourth-cell endpoint and acute-component theorem.
- `parent_to_fourth_lineage_control_certificate.json`, `verify_parent_to_fourth_lineage_and_controls.py`: exact parent-to-fourth lineage and rank-5 controls.
- `fifth_cell_endpoint/input_rows_common_lattice.csv`: authoritative 119-row exact fifth generator.
- `fifth_cell_endpoint/coordinates_active_centered.csv`, `halfspaces_centered.csv`: complete exact V/H data.
- `fifth_cell_endpoint/face_cycles.json`, `true_edges.csv`: every actual maximal face and true edge.
- `fifth_cell_endpoint/faces_mechanics.json`, `vertices_mechanics.csv`, `edges_four_component_audit.csv`: exhaustive full-cone mechanics.
- `fifth_cell_endpoint/fifth_cell_complex.json`: complete 64-cell convexity atlas and connected closure.
- `fifth_cell_endpoint/acute_bridge_graph.json`: both exact rails and connected positive-dot graph.
- `fifth_cell_endpoint/interval_certificate.json`: open 132-coordinate box.
- `fifth_cell_endpoint/control_certificate.json`, `verify_controls.py`: exact rank-5 moment/antibirth controls.
- `fifth_cell_endpoint/next_topology_atlas.json`: exact residual local star and first unclassified replacement.
- `fifth_cell_endpoint/body.obj`, `body.stl`: matching watertight meshes.
- `FINAL_VERIFICATION_SUMMARY.txt`: current combined clean-room rerun.
