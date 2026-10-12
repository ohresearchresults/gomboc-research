# figure-0216

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Quartz 58 — exact continuation through `E18F` and the central-`Y` spine

## Literal verdict

**EXACT MATERIALIZED NONWINNER.** No strict own-centred `(S,U,H)=(1,1,0)` polyhedron was found. The accepted parent `E18P` is exact `(18,48,32)`, `(2,2,2)`; its `{W,X}` chamber theorem motivated the edge-flipped `E18F` cell and then the central-`Y` spine. :contentReference[oaicite:0]{index=0}

This continuation does not return to the excluded `E18P` chamber. It searches unrestricted coordinates in `E18F`, exactifies a target-preserving `E18FQ` cell, realizes the previously combinatorial 19-vertex central-`Y` four-triangle spine, proves a new chamber-wide obstruction there, and materializes the first adjacent incidence cell outside that obstruction.

## Immutable bundle

- [Portable archive](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_nonwinner.zip), SHA-256 `c8440bca21167cb3fd65663789eb9667b0f725acd239dc3d3105d58660d83f08`; [hash file](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_nonwinner.zip.sha256).
- [Full determination](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/RESULT.md), [README](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/README.md), [one-command verifier](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/[internal-source-reference].sh), [110-entry manifest](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/SHA256SUMS), [verification record](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/VERIFICATION_RECORD.json).

A clean replay terminates with `ALL VIVID QUARTZ 58 E18F/CENTRAL-Y VERIFIERS PASS`; the archive passes `unzip -t`.

## 1. Full-dimensional `E18F` search

The exact `E18F` anchor removes `(W,X)`, adds `(F,8)`, and has `(18,48,32)`, class `(8,8,14)`. Seven determinant-one affine searches made 31,032 declared evaluations. A separate 54-coordinate fixed-incidence continuation moved every vertex coordinate modulo translation and scale. No winner occurred. Its closest target-preserving checkpoint was `(4,2,4)` but collapsed toward nonincidence `7.770779962626151e-7` and normalized volume `6.218264392557234e-6`, so it was retained only as a boundary receipt.

A robust target-preserving state was dyadically exactified as `E18FQ` at denominator `2^60`. It has actual `(18,48,32)`, strict `(3,3,4)`, stable faces `[2,W,A]`, `[8,A,B]`, `[10,X,L]`, unstable vertices `8,A,B`, and saddles `(8,A),(8,B),(A,B),(B,F)`. Its exact volume is `103613753914471123714083206775979340275809550157549/140304157183766680147553743940763169886969524125696`; its exact centroid is `['-895439584690105466195153178256916486352189515282877/233317431759835212015655939067418700601757604433700901364697137152', '-207171015995904858631900194025143580440700281623305/477834100244142514208063363210073498832399573880219445994899736887296', '-41334481383868413515962015861116535086344704212605/14932315632629453569001980100314796838512486683756857687340616777728']`. Minimum absolute normalized mechanics margin is `1.1400368117867816e-07` and normalized nonincidence is `5.889940806756207e-06`. All 54 coordinates vary independently by `2^-28` while preserving incidence and class. [Exact V/H/audit/mesh package](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/searched_E18F/E18FQ/E18FQ_exact_report.json), [independent report](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/searched_E18F/E18FQ/E18FQ_independent_verification.json).

This is a rigorous open cell, not a CAD exclusion of the complete `E18F` realization space.

## 2. Exact positive-volume central-`Y` replacement

Replace the `E18P` two-triangle disk `[W,F,X] [W,X,8]`, boundary `W-F-X-8-W`, by

```text
[W,F,Y] [F,X,Y] [X,8,Y] [8,W,Y].
```

The source and target disks have f-vectors `(4,5,2)` and `(5,8,4)`, both Euler one; globally `(18,48,32)->(19,51,34)`. Edge `(W,X)` disappears. New true edges are `(W,Y),(F,Y),(X,Y),(8,Y)`. Exact tetrahedra `[Y,W,F,X]` and `[Y,W,X,8]` share internal triangle `[Y,W,X]` and have total positive volume `539241831007722276782289699215/1947111321950560360698936123457536`. Thus the replacement has genuine three-dimensional thickness. [Incidence certificate](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E18P_to_E19Y_patch_complex.json), [volume-cell certificate](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_positive_volume_cell_certificate.json).

## 3. Strongest endpoint `E19Y`

Use denominator `D=2^44=17592186044416`. The uncentred integer V-data are

```text
1: (241025679360,-22100107640832,-481267011584)
2: (1093667475456,-12676033568768,-2671114633216)
8: (-1537421557760,-45032566702080,5331134828544)
10: (-2219033518080,-27974195515392,7721652113408)
11: (-1925450895360,-38532255612928,6251548962816)
A: (2154294980608,11913465425920,-4840262807552)
B: (553649299456,5087022596096,258517745664)
C: (663706189824,30940090339328,-3807137562624)
F: (1981420961792,23701741023232,-4647889330176)
L: (-1982386507776,3917057921024,2693256916992)
M: (1963360948224,22813460115456,-5234935611392)
N: (1812810760192,20275320754176,-5277246066688)
P: (-2271431024640,-33192869089280,6541107032064)
R: (-168761556992,-22532766949376,146890002432)
S: (-39406206976,-28781600768,-2713733984256)
T: (-2403795947520,-26178107609088,5890767671296)
W: (-499693584384,54656377098240,-6961515839488)
X: (-1095673638912,55060009103360,-5431823773696)
Y: (-656689751493,57109220104151,-6803261146253)
```

The physical body is `conv{Q_i/D-C}`. Exact uniform volume, moments and centroid are

```text
V  = 191268223730333862185861361004943/1947111321950560360698936123457536
Mx = -81639688873267300822592387658547027679678297/45671926166590716193865151022383844364247891968
My = 3538430860611621906308585436494854911557453849/137015778499772148581595453067151533092743675904
Mz = -507414354716562023727557735616147192484321219/137015778499772148581595453067151533092743675904
Cx = -244919066619801902467777162975641083039034891/13459304704996066283514193823437289543174193152
Cy = 3538430860611621906308585436494854911557453849/13459304704996066283514193823437289543174193152
Cz = -507414354716562023727557735616147192484321219/13459304704996066283514193823437289543174193152
```

The Fraction verifier proves `M_j=V*C_j` exactly; translated first moments are `(0,0,0)`.

All 34 actual maximal faces are

```text
[1,2,8] [1,S,2] [1,8,R] [1,R,S] [2,A,8] [2,W,A]
[2,S,W] [8,10,11] [8,B,10] [8,11,P] [8,A,B] [8,P,T]
[8,S,R] [8,W,S] [8,T,X] [8,Y,W] [8,X,Y] [10,P,11]
[10,B,X] [10,L,T] [10,X,L] [10,T,P] [A,F,B] [A,M,F]
[A,N,M] [A,W,N] [B,F,C] [B,C,X] [C,F,X] [F,M,W]
[F,W,Y] [F,Y,X] [L,X,T] [M,N,W]
```

All 51 true edges are

```text
(1,2) (1,8) (1,R) (1,S) (2,8) (2,A) (2,S) (2,W)
(8,10) (8,11) (8,A) (8,B) (8,P) (8,R) (8,S) (8,T)
(8,W) (8,X) (8,Y) (10,11) (10,B) (10,L) (10,P) (10,T)
(10,X) (11,P) (A,B) (A,F) (A,M) (A,N) (A,W) (B,C)
(B,F) (B,X) (C,F) (C,X) (F,M) (F,W) (F,X) (F,Y)
(L,T) (L,X) (M,N) (M,W) (N,W) (P,T) (R,S) (S,W)
(T,X) (W,Y) (X,Y)
```

Euler is `19-51+34=2`. Every face is triangular. For each oriented face `(i,j,k)`, the deterministic H row is `n=primitive((Q_j-Q_i)x(Q_k-Q_i))`, `h=n·Q_i`, and `n·x<=h/D-n·C`. All primitive normals, supports, centred rational right sides and every nonincident exact slack are in [the H representation](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_H_representation.json).

Exhaustive own-centroid mechanics gives

```text
stable faces: [['8', 'A', 'B'], ['8', 'W', 'S']]
unstable vertices: ['8', 'Y']
saddle true edges: [['2', 'A'], ['L', 'X']]
(S,U,H)=(2, 2, 2)
```

Thus intended `[8,A,B]` and `8` survive, but the packet remains as `[8,W,S]`, `Y`, `(2,A)`, `(L,X)`. Minimum absolute normalized mechanical separation is `0.0014167079228808311`. Minimum integer support slack is `850317960682668990577057256`; normalized nonincidence is `0.00013192475653360562`. [Exact report](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_exact_report.json) and [exhaustive face/vertex/four-component-edge audit](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_audit.md) contain every sign and margin.

Exact interval arithmetic varies all 57 uncentred coordinates independently by `2^-22`, recomputes volume, moments and dependent own centroid, and preserves `(19,51,34)` and `(2,2,2)`. A separately coded Qhull/interior-tetrahedron/full-unit-normal-cone verifier reconstructs the same object and reads both meshes as watertight, winding-consistent and Euler two. [Perturbation certificate](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_perturbation_certificate.json), [independent report](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_independent_verification.json), [OBJ](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_centered.obj), [STL](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_centered.stl).

## 4. New exact chamber obstruction

On the larger all-coordinate box `2^-18`, `(X,Y)` remains a positive-length true edge. Its squared-length lower bound is `6271777037919680913716691/309485009821345068724781056`. Every directed instability component from `X` or `Y` toward a neighbor outside `{X,Y}` is positive; the minimum lower bound is `97694009399219445806071504393043250416408386454844532501399/100433627766186892221372630771322662657637687111424552206336`. Every directed component at protected `8` is positive; the minimum lower bound is `59123092946082258388811180679313779961959488404899245989/24519928653854221733733552434404946937899825954937634816`.

For centered positions, a nonpositive arrow `-x_i·(p_j-p_i)<=0` implies `||x_j||^2-||x_i||^2>=||p_j-p_i||^2>0`. If neither `X` nor `Y` were unstable, each would have to point nonpositively to the other, forcing strict squared-radius increase in both directions. Contradiction. Hence one of `X,Y` is unstable at every point of the complete box, including internal mechanics walls; `8` is independently unstable. Therefore `U>=2` throughout this certified 57-dimensional chamber. [Exact component theorem](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/E19Y_component_certificate.json), [stdlib-only independent replay](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/verify_E19Y_component_independent.py).

## 5. First exact adjacent cell outside the theorem: `E19Z`

The circuit flip on `{F,X,8,Y}` removes `[F,X,Y]`, `[X,8,Y]`, and edge `(X,Y)`; it adds `[F,X,8]`, `[F,8,Y]`, and edge `(F,8)`. Therefore the new `{X,Y}` theorem no longer applies. [Exact flip certificate](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/adjacent_E19Z/E19Y_to_E19Z_flip_certificate.json).

The realized dyadic anchor `E19Z` has `(19,51,34)`, strict `(8,8,14)`, exact volume `42906617158637589283374683/58028439341502200385896448`, exact centroid `['1443890753572035508343213453714805459199/1509642383182568569965562593274815840256', '1624895420172005785584968876584496898801/3019284766365137139931125186549631680512', '-698057033138330228217210872170163252163/3019284766365137139931125186549631680512']`, minimum mechanical separation `0.0046856575129984165`, normalized nonincidence `0.009899764348758338`, and a simultaneous all-coordinate box `2^-17`. Its stacking tetrahedron `[Y,F,W,8]` has exact positive volume `52972942692152643061339/58028439341502200385896448`. [Exact V/H/audit](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/adjacent_E19Z/E19Z_exact_report.json), [independent replay](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/adjacent_E19Z/E19Z_independent_verification.json), [OBJ](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/adjacent_E19Z/E19Z_centered.obj), [STL](sandbox:/mnt/data/vivid_quartz_58_e18f_component_breaking_result/adjacent_E19Z/E19Z_centered.stl).

Four determinant-one affine searches on `E19Z` made 72,240 declared evaluations. Target-preserving states reached `(3,3,4)` but no winner. This is empirical evidence, not a full-space exclusion.

## 6. Scope and continuation

**Proved:** exact parent reconstruction; exact target-preserving `E18FQ`; exact central-`Y` incidence and positive shared volume; complete `E19Y` V/H/E, own centroid, exhaustive full-cone mechanics, `2^-22` class box, independent verifier and meshes; exact `2^-18` theorem forcing `U>=2`; exact adjacent `E19Z` incidence, `2^-17` box, independent replay and meshes.

**Not proved:** no CAD or quantifier-elimination exclusion of the complete `E18F`, `E19Y`, or `E19Z` realization spaces is claimed. Numerical near-wall failures are discovery receipts only. Patch certificates compare exact endpoint spheres and cells; they do not assert an unstated coordinate homotopy.

The smallest still-open realization space is the 18-vertex `E18F` graph outside the exact anchor and `E18FQ` boxes. The first distinct exact incidence cell outside the new obstruction is `E19Z`; its full realization space is the strongest topology-changing continuation, so no additional vertex is yet forced. Continue from target-preserving low-count `E19Z` cells with `(F,8)` retained and `(X,Y)` absent, moving all old planes to kill the extra stable and saddle routes before a radial maximum transfers to `A,B,F,M,W`, or `X`. If every such chamber transfers the packet, the next compact topology is a two-support shared volumetric `2<->3/3<->2` complex across quadrilateral `F-X-8-Y`, not another serial stacked apex.

## Reusable conclusion

`E18FQ` proves that the edge-flipped graph contains target-preserving low-count chambers beyond its poor anchor, but no winner was found. The central-`Y` replacement produces the strongest exact endpoint `E19Y`, robust own-centred `(19,51,34)` and strict `(2,2,2)`. It removes `(W,X)` but transports the extra unstable equilibrium onto true edge component `(X,Y)`, which rigorously forces `U>=2` on a `2^-18` all-coordinate chamber. Exact `E19Z` removes `(X,Y)` and is the smallest materialized cell outside that theorem; its full realization space remains open. **Explicit disposition: exact materialized NONWINNER.**
