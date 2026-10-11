# figure-0279

Historical AI scientific report · saved 2026-09-03 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Calm Quartz 90 — exact nonsimplicial eight-vertex carrier escape

## Disposition

**EXACT DELIMITED NONWINNER.** No materialized homogeneous convex polyhedral Gömböc was obtained in the topology closed here.

The acceptance gate is an explicit finite uniform-density convex polyhedron at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, actual H/V/incidence, an exhaustive positive-margin face/vertex/true-edge audit, independent verification, and matching OBJ/STL. Wall points, auxiliary centres, near-solutions, and unexpanded theorem objects do not qualify. :contentReference[oaicite:0]{index=0}

The immutable parent `figure-0274`, payload SHA-256 `febe7249e478426e95d60296cd8698dc3aa35dcf84c0a10ab1afd09212733ed1`, is the recurrent simplicial eight-vertex `(8,18,12)`, strict `(2,2,2)` cage with sole nonprotected carrier `[0,AT]`. The journal identifies a nonsimplicial eight-vertex circuit or minimally enlarged basin as the first unrepresented continuation. :contentReference[oaicite:1]{index=1} Exact prior work proves that any strict homogeneous polyhedral Gömböc has at least eight vertices, while the eight-vertex case remains open. :contentReference[oaicite:2]{index=2}

I realized the first literal nonsimplicial successor by imposing

```text
AW=(7/8)·0-(1/4)·H+(3/8)·AT.
```

This removes physical edge `[0,AT]` and replaces its two-triangle star by the genuine quadrilateral maximal face `[0,AW,AT,H]`. The exact target has 58 supplied rows, eight active vertices, one quadrilateral and ten triangular maximal faces,

```text
(V,E,F,C)=(8,17,11,34),  (S,U,H)=(2,2,2).
```

It is therefore genuinely outside the recurrent simplicial cage, but it remains a nonwinner because `[AT,AW]` becomes the unique nonprotected all-external-positive carrier. Stable `[0,H,C]` remains a maximal face but becomes nonstable; saddle `[0,AW]` is replaced by `[0,C]`; unstable `AT` and saddle `[AT,AV]` persist.

## Immutable source and exact finite generator

```text
parent archive SHA-256   19c28a0acc5bcd75e88ddc3e63f77ff91ed8b3dcdc8652e98b1344c4d4ff21de
parent generator SHA-256 e76432da2b8d0b13c11337231c6a7bb2649ee74ed8140b68b2fa873807d33db9
common denominator       D=2^27=134217728
```

Supplied order:

```text
0,1258,1371,1975,2152,2369,2515,2732,3290,3296,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU,AV,AW.
```

For zero-based position `i`, every non-overridden source or target row is

```text
(8(i+1),-16(i+1),24(i+1))/D,
```

except `B=(0,0,0)`. The immutable source active overrides are

```text
0  =(  19057904, -50471568,  369374232)/D
C  =(-157248112,-100564064, -673203608)/D
H  =( -13428904,  95484952, -203825632)/D
AS =(  13481528, 106209064, -370999584)/D
AT =( 215035232, 155090168,  624881392)/D
AU =(  62805192,  67862424, -143066648)/D
AV =(  46873424, 109782944, -360206208)/D
AW =(-111527632,-152460864, -489579416)/D.
```

It reconstructs exactly as `(8,18,12)`, `(2,2,2)`, with stable `[0,H,C]`,`[AT,AW,AU]`; unstable `C,AT`; saddles `[0,AW]`,`[AT,AV]`; volume

```text
27255408762082521813787/7083549724304467820544
```

and centroid

```text
(120627955237556819149704640653/1829079519879004313178465107968,
 15210364627095431066434324625/114317469992437769573654069248,
-5343885881081102728270507232313/7316318079516017252713860431872).
```

The target has the same seven fixed active overrides and

```text
AW=(100671104,-9875047,608489383)/D.
```

Thus the exact target active set is `{0,C,H,AS,AT,AU,AV,AW}`. The other 50 supplied rows are strictly interior; their minimum exact oriented slack is

```text
1573634937389395890335/2361183241434822606848>0.
```

Target volume and own ordinary centroid are

```text
Vol=330307380801536071009997/113336795588871485128704

c=(4440188281072225939291773194163/22166553096406495180504231313408,
   53354088297711082912010704837381/177332424771251961444033850507264,
  -39560943284920700579508277754997/177332424771251961444033850507264).
```

After translating every active vertex by `-c`, exact tetrahedral summation gives `Mx=My=Mz=0`. For each oriented maximal face `(i,j,k)`, the primitive exact H-row is reconstructed deterministically by

```text
n=(p_j-p_i)×(p_k-p_i),  b=n·p_i,  n·x≤b,
```

followed by common-denominator clearing and four-entry gcd reduction. Coordinates, centroid, and the cycles below are therefore a complete exact H/V generator.

## Actual maximal faces and true edges

Maximal faces:

```text
[C,0,H]                    nonstable
[C,AW,0]                   nonstable
[C,H,AS]                   nonstable
[C,AS,AV]                  nonstable
[C,AV,AU]                  nonstable
[C,AU,AW]                  STABLE
[H,AT,AS]                  nonstable
[AS,AT,AV]                 nonstable
[AU,AV,AT]                 nonstable
[AW,AU,AT]                 nonstable
[0,AW,AT,H]                STABLE QUADRILATERAL.
```

Physical true edges:

```text
[0,C] SADDLE; [0,H]; [0,AW]; [C,H]; [C,AS]; [C,AU]; [C,AV]; [C,AW];
[H,AS]; [H,AT]; [AS,AT]; [AS,AV]; [AT,AU]; [AT,AV] SADDLE;
[AT,AW]; [AU,AV]; [AU,AW].
```

Every edge has exactly two incident maximal faces and `8-17+11=2`. The mesh uses one diagonal only to display the quadrilateral; that diagonal is excluded from true-edge mechanics. Minimum active nonincidence distance is `0.04751883053135229`.

## Exhaustive own-centroid mechanics

The verifier evaluates perpendicular-foot barycentrics on every maximal polygon, every directed support `sigma(v→w)=-v·(w-v)`, and all four true-edge cone components `(t,1-t,beta1,beta2)`.

Exactly two faces are stable:

```text
[C,AU,AW]      minimum normalized coordinate 0.29231868680453177
[0,AW,AT,H]   minimum normalized coordinate 0.06604758059726598.
```

Closest excluded face `[C,0,H]` has exact decision

```text
-104887065669036967481832679701656761461253013584710371/
209357174766440768583871757609089545448473829820071936.
```

Exactly `C,AT` are unstable; minimum normalized outgoing supports are `0.9159642927966116` and `0.36776984438924765`. Closest excluded vertex `AW` has normalized witness `-0.08174481993462063`.

Exactly `[0,C]` and `[AT,AV]` are saddles. The full normalized cone tuple for `[0,C]` is

```text
(0.36623395197432906,0.6337660480256709,
 1.6534769613662357,1.7126970769399827),
```

and the minimum component for `[AT,AV]` is `0.3186008772615743`. Every other true edge has an exact negative component; closest excluded edge `[0,H]` is `-0.18769494229065306`. The finite ledgers cover all 11 faces, all 34 directed vertex primitives, and all 68 edge-cone components.

## Connected positive-volume topology event

Removing common face `[0,C,H]` leaves source and target dual-connected disks with the same boundary triangle `0-H-C-0`:

```text
source patch (V,E,F)=(8,18,11), chi=1
target patch (V,E,F)=(8,17,10), chi=1.
```

No bridge face is required. Coning each patch to its own exact centroid gives positive-volume 3-balls; minimum source/target cone volumes are

```text
1761109457112849415982497395612061378099450957/
12356162766237134333638527340038852204866568192

5032988414651279229264529213879209875201452857/
49914640132532302995651187326691042291754205184.
```

Exact edge changes:

```text
removed [0,AT], [AV,AW]
inserted [C,AU]
star-changed [0,H],[0,AW],[C,AV],[C,AW],[H,AT],[AT,AW],[AU,AV],[AU,AW].
```

Hence `[0,AT]` is physically absent. The parent packet is only partly cancelled: `[AT,AW,AU]` loses stability and `[0,AW]` dies as a saddle, but `AT` and `[AT,AV]` remain and `[AT,AW]` becomes adverse.

## Complete arrow census and exact obstruction

All 17 target edges and every inserted/star-changed edge were audited. The only all-external-positive target edges are protected `[C,AS]` and nonprotected `[AT,AW]`. Every other changed nonprotected edge has a strict negative external witness. The adverse graph is one edge, with no two-edge component, directed cycle, or positive cycle rank.

For `[AT,AW]`, the exact minimum external arrow is

```text
103478946284399184719738312170175054548747/
11900577576764178990280911285088310788096.
```

The mutual arrows are

```text
sigma(AT→AW)=33806516443255831968120319815981664737009/
             11900577576764178990280911285088310788096
sigma(AW→AT)=-7011074099132246775688538742817984453149/
             11900577576764178990280911285088310788096
```

and their exact sum is

```text
||AW-AT||²=20280686946126345/9007199254740992>0.
```

If neither endpoint were unstable, both mutual arrows would be nonpositive while all external arrows stayed positive, a contradiction. One endpoint is therefore unstable in addition to `C`; here it is `AT`. This proves `U≥2` throughout the certified relative chamber.

## Exact chronology

Only `AW` moves on the canonical chord. The actual hull and ordinary centroid are recomputed in each side cell. Twelve exact Sturm-isolated simple events occur:

```text
0.409608651842179  first C/AV/AU/AW circuit
0.410795977796558  AW instability and saddle [C,AW] birth
0.417477414613841  source saddle [0,AW] death
0.467715492006151  stable [C,AW,0] and saddle [0,C] birth
0.542302336451725  bridge [C,AW] stable/saddle death
0.563170488412547  stable [C,AU,AW] and saddle [AU,AW] birth
0.572770481614881  source stable [AT,AU,AW] death
0.631023115663213  bridge stable [0,H,AT] and saddle [0,H] birth
0.781557035536616  replacement carrier [AT,AW] becomes all-positive
0.784681777316388  source carrier [0,AT] loses external positivity
0.923218665771416  protected stable [0,H,C] and saddle [0,H] death
1 exactly          quadrilateral forms and physical [0,AT] disappears.
```

Thus each replacement channel is born before its source channel dies; `AT` and `[AT,AV]` remain strict throughout. No `(1,1,0)` interval occurs on this chord.

## Exact finite atlases

The complete denominator-eight grid

```text
AW=(1-b-c)0+bH+cAT, b=i/8, c=j/8, -16≤i,j≤24
```

contains 1,681 exact parameter pairs. Exactly 248 have one quadrilateral `{0,H,AT,AW}` and no edge `[0,AT]`:

```text
218 × (2,2,2); 22 × (3,2,3); 6 × (2,3,3); 2 × (3,3,4); 0 winners.
```

Every accepted point has `U≥2` and at least one nonprotected adverse edge. Nine preserve `[0,H,C]` as stable; seven are `(3,2,3)` and two `(3,3,4)`.

A deterministic compatible second-circuit collar projects each local vertex of every two-triangle edge star onto the plane of the other three. Eleven exact cells survive: eight `(2,2,2)`, three `(3,2,3)`, zero winners; all retain adverse `[AT,AW]`. These are exact finite atlases, not a continuous global nonsimplicial exclusion.

## Positive relative-stratum box

The promoted exact radius is

```text
epsilon=2^-24=1/16777216.
```

There are 23 independent controls: all 21 coordinates of `0,C,H,AS,AT,AU,AV` plus `b_H,c_AT`; `AW=(1-b_H-c_AT)0+b_HH+c_ATAT` is dependent. The other 50 supplied rows are fixed. Volume, first moments, and the own centroid are recomputed throughout.

This is an open box in the codimension-one nonsimplicial stratum, not an ambient 24-dimensional ball. It preserves `(8,17,11)`, `(2,2,2)`, all inactivity and incidence signs, the quadrilateral turns, every mechanical decision, all anti-carrier witnesses, and the forcing theorem. Exact volume interval:

```text
[461802525504739606083702265275/158456325028528675187087900672,
 461803853512217416238233492213/158456325028528675187087900672].
```

Certified lower clearances are approximately

```text
topology 0.1671550475524405; inactive 0.49892286709096745;
quad turn 6.958429544645234; face 0.26341278037150256;
vertex 0.5891060043418314; edge 0.03787351769337713;
forcing 8.695252562160512; anti-carrier 0.14704556243210745.
```

## Scope and next topology

Closed exactly: the immutable source reconstruction; this nonsimplicial endpoint; its connected positive-volume patch; complete H/V/E and mechanics; arrow census and `[AT,AW]` theorem; the twelve-event chord; the 1,681-point/248-cell grid; the eleven-cell second-circuit collar; and the 23-dimensional `2^-24` relative box.

Not closed: the continuous whole circuit stratum, all transverse chambers, coupled two-plane nonsimplicial cells, nine-plus-vertex basin insertions, or global existence.

The first genuinely new successor is either a coupled two-plane eight-vertex circuit complex deleting both `[0,AT]` and `[AT,AW]` while deactivating `AT` and restoring a unique stable face, or a nine-vertex carrier-splitting basin insertion replacing `[AT,AW]` by two edges that each have a preassigned negative external arrow before exact centroid closure. Another simplicial cage or serial one-plane transfer is exhausted.

## Verification and artifacts

Independent exact generation, parent reconstruction, Fraction H/V/E verification, standard-library clean-room reconstruction, directed interval proof, full grid/second-circuit replay, symbolic Sturm chronology replay, and exact-to-OBJ/STL verification all pass. The mesh has eight vertices, twelve display triangles, eighteen display edges of multiplicity two, eleven physical maximal faces, and seventeen physical true edges.

```text
archive SHA-256 526ded4259e00c11e595f96503449396bc10b7b24ea4c444de3eca5ceeb3d795
archive bytes   3013505
manifest files  53
manifest SHA-256 c29b922c09e7d3171876ace365a256ed4b2ca61a036c66fbd2e840cb5c78e606
clean extraction PASS
```

- [Complete exact archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER.zip)
- [Full self-contained handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_COMPLETE_HANDOFF.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_COMPLETE_RESULT.json)
- [Clean verification receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_clean_verification.json)
- [Clean replay](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_clean_replay.txt)
- [Exact generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/generator_exact.json)
- [Exact H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/sixteenth_ns8_exact_H_irredundant.csv)
- [Exact centred V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Face ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/sixteenth_ns8_exact_faces.csv)
- [Vertex ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/sixteenth_ns8_exact_vertex_primitives.csv)
- [True-edge cone ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/data/sixteenth_ns8_exact_true_edges_full_cones.csv)
- [Grid atlas](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/certificates/carrier_escape_grid_atlas.json)
- [Second-circuit atlas](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/certificates/carrier_escape_second_circuit_atlas.json)
- [Chronology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [Relative-box certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/certificates/own_centroid_relative_stratum_perturbation_certificate.json)
- [Independent verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/scripts/verify_independent.py)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_sixteenth_nonsimplicial_circuit_exact_NONWINNER/mesh/body.stl)

**Final statement:** `NONWINNER`, rigorously delimited. The first genuine nonsimplicial eight-vertex carrier escape removes `[0,AT]`, but transfers the one-edge forcing obstruction to `[AT,AW]`; the exact finite one-plane and compatible second-circuit collars contain no winner.
