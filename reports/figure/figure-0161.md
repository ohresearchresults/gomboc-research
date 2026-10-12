# figure-0161

AI research report · 2026-08-29 UTC

---

# Exact M42 edge-sharing two-nonsimplicial-cell continuation

## Literal verdict

**NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedron was obtained. The first genuinely new topology beyond the graded M42 sheet was materialized exactly as two coupled triangular-bipyramidal centroid-fan 3-cells sharing a quadrilateral interface and its interior radial edge. It jointly absorbs every assignment-named terminal, stable, direct-gate, and return-gate row, but the endpoint is an open strict `(2,2,2)` body.

The exact negative conclusion applies to this endpoint, its positive coordinate box, and its first four outgoing A/B chambers. It is not a global obstruction to all larger M42 surgeries.

## Deterministic exact endpoint

The construction starts from the exact 129-row irredundant actual V-set of the 218-input graded sheet. On common denominator `S=10^36`, set

```text
{102,120,127,128,129,147,148,149,173,174,177,178,179,200}
    -> c*=(-22638817877,9862693840,-7081176048)/10^12,
218 -> A=(4082287210679,-5018521860168,-761517076674)/10^12,
219 -> B=(579546247292,-8008610548198,-2026401781145)/10^12.
```

`generate_exact_endpoint.py` performs only these rational operations, regenerates the exact centred coordinates and exact mass, byte-compares the regenerated tables, and invokes the independent exact verifier. The complete 129-row predecessor table and all 131 expanded inputs are included.

Actual hull:

```text
input rows       131
active vertices   90
true edges        250
maximal faces     162
complexity        500
Euler              2
class         (2,2,2)
```

Active rows:

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 54 69 72 73 86 88 132 133 134 135 136 137 138 139 140 141 142 144 145 146 150 151 152 164 165 166 167 168 169 170 171 172 175 176 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219
```

Inactive rows:

```text
102 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 143 147 148 149 153 154 155 156 157 158 159 160 161 162 163 173 174 177 178 179 200
```

The complete 162 maximal-face cycles and all 250 true edges with their two incident faces are written inline in the self-contained handoff and machine-readably in `face_cycles.json` and `true_edges.csv`. `halfspaces_centered.csv` is the complete exact H representation; `coordinates_active_centered.csv` is the complete exact centred V representation.

## Exact ordinary volume and three moments

Exact volume:

```text
13235024326339533185627782769472954077257971665414232759817068873117871384123748548218138081522962261635304347/600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Exact unshifted ordinary centroid:

```text
501120288155053824674001844180836355092693400990340655265156797276766027372937054388418511253965827301383980141261754849776824417568420149172001/3308756081584883296406945692368238519314492916353558189954267218279467846030937137054534520380740565408826086750000000000000000000000000000000000
-1196948094561665552411436162526537711075503143518339258844223365865309367366053691222534704079397971626175685386976795662038870917854315729618827/2647004865267906637125556553894590815451594333082846551963413774623574276824749709643627616304592452327060869400000000000000000000000000000000000
-1250376418863427832890387681394557573410853985618409918018286841134494860253996808482396366175473586812493399068117787211320235691551719631717781/10588019461071626548502226215578363261806377332331386207853655098494297107298998838574510465218369809308243477600000000000000000000000000000000000
```

The independent verifier recomputes the exact unshifted first moments and proves `Mk=V*Ck` in all three components. Translation by `tau=-C` is the hard three-component dependent moment solution, giving centred first moments exactly `(0/1,0/1,0/1)` before mechanics.

## Exhaustive full-feature audit

Stable maximal faces:

```text
[199,218,219]                                      margin 0.6507042048981592
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]     margin 0.21049851053197202
```

Unstable actual vertices:

```text
8    margin 0.3683879666270198
219  margin 0.362581365940398
```

Saddle true edges, with all four components `(t,1-t,beta1,beta2)>0`:

```text
(134,218)  decision margin 0.3926759589342512
(180,219)  decision margin 0.12916338112336925
```

Global normalized endpoint minima:

```text
stable positive        0.21049851053197202
nonstable exclusion    0.10623961052835133
unstable positive      0.362581365940398
nonunstable exclusion  0.1163755742894826
saddle positive        0.12916338112336925
nonsaddle exclusion    0.1317874509625695
topology distance      4.6811600016307245e-05
inactive separation    0.00022592636823935244
```

Every face component, every adjacent-edge vertex support, and all four components of every true-edge normal cone are exact in the audit ledgers and independently regenerated.

## Joint absorption and genuine two-cell incidence

All fourteen old packet rows are inactive. The old edge `(147,148)` and older transferred channels `(95,96)`, `(82,96)`, `(96,104)`, `(104,111)` are absent.

Let `O` be the exact own centroid and `M=(A+B)/2`. The true boundary edge `(A,B)=(218,219)` has incident triangles `[199,A,B]` and `[144,B,A]`. The centroid-fan replacement is

```text
Cell A = T(O,144,A,M) union T(O,199,A,M),
Cell B = T(O,144,M,B) union T(O,199,M,B).
```

Each union is a nonsimplicial triangular bipyramid. The cells share the quadrilateral interface `O-144-M-199`, triangulated by `[O,144,M]` and `[O,M,199]`; these interface triangles share the interior edge `(O,M)`. All four tetrahedral determinants are exact and nonzero. The full closure star has 52 boundary triangles, and its 52 centroid-fan tetrahedra form one connected nondegenerate complex touching the terminal, right, north, and left sectors. The directed box lower bounds are `0.7521619340549729` for the two-cell determinants and `0.04036350227123123` for the closure-fan determinants.

The old separated defects are therefore genuinely altered together. The residual connected A/B packet is

```text
extra stable face       [199,218,219]
extra unstable vertex   219
direct saddle           (134,218)
return saddle           (180,219)
transferred channel     (146,219)
closure edge            (218,219)
```

## Exact transferred obstruction

True edge `(146,219)` has every nonmutual endpoint support positive. Its mutual supports are

```text
sigma(146->219) = -23363778218700379533042993490677204283310170972889624955833954070475318339217447619294492969435796107706771394484222674692247354513666711692655393522600729352842712929998057171204399/13235024326339533185627782769472954077257971665414232759817068873117871384123748548218138081522962261635304347000000000000000000000000000000000000000000000000000000000000000000000000

sigma(219->146) = 71239688627742786010732974981396706682336583641070774821163663307940536704330679179037857085111104736155725719908148388425762756179399588135830831048591072811259755116009740588422871/13235024326339533185627782769472954077257971665414232759817068873117871384123748548218138081522962261635304347000000000000000000000000000000000000000000000000000000000000000000000000
```

and exactly

```text
sigma(146->219)+sigma(219->146)
 = ||x219-x146||^2
 = 452170593235732741617532481857109512086346789564919217005178412944184047/125000000000000000000000000000000000000000000000000000000000000000000000 > 0.
```

Thus both mutual supports cannot be nonpositive. At least one endpoint remains unstable throughout the certified incidence/external-sign cell; vertex `8` is independently unstable, so `U>=2`. The minimum external support is `0.2776800332106869`.

## Global radial-order obstruction

For adjacent distinct vertices, `sigma(i->j)<=0` implies `||xj||>||xi||`. Hence a unique unstable vertex must be the unique global farthest vertex. Exact squared-radius order puts protected vertex `8` only seventh among the 90 actual vertices. The six farther vertices are

```text
219 146 150 145 151 144
```

with induced true edges

```text
(144,145) (144,219) (145,146) (145,219) (146,150)
(146,219) (150,151) (150,219) (151,219)
```

With fixed geometry, making target `8` at least as far as vertex `219` requires a centre displacement strictly greater than `0.32179830706812235`. Therefore deleting `(146,219)` alone cannot suffice; the entire six-vertex superlevel terminal packet must be deactivated or radially/centroid-reordered.

## Complete first outgoing chamber atlas

Use

```text
A(sA)=c*+(1+sA)(A0-c*),
B(sB)=c*+(1+sB)(B0-c*).
```

The exact atlas reconstructs full H/V/E incidence, mass, and every normal cone in four cells:

```text
C00 (0,0)       (V,E,F)=(90,250,162)  class (2,2,2)
C10 (1/8,0)     (V,E,F)=(85,235,152)  class (2,3,3)
C01 (0,9/100)   (V,E,F)=(83,229,148)  class (3,2,3)
C11 (1/8,9/100) (V,E,F)=(79,217,140)  class (3,3,4)
```

The direct simultaneous `U-H` birth at vertex `218` / edge `(146,218)` is isolated in

```text
[503714125209/5000000000000,
 1007428250419/10000000000000]
```

of exact width `10^-13`. The return simultaneous `S-H` birth at face `[180,181,219]` / edge `(181,219)` is isolated in

```text
[186180469237/2500000000000,
 744721876949/10000000000000]
```

also of width `10^-13`. Exact controlling signs are negative below and positive above each wall. Independent opening of the two cells therefore creates paired births rather than a cancellation.

## Positive perturbation box

Rows `0..16` and all inactive rows are fixed. Every coordinate of every other active row—219 independent coordinates—may vary by `±10^-10`. Exact outward `Fraction` intervals preserve the full `(90,250,162)` incidence, strict `(2,2,2)`, inactive rows, packet absorption, old-channel deletion, two-cell/closure determinants, and obstruction.

Rigorous lower bounds:

```text
facet determinant           2.2103901212207943e-05
inactive facet determinant  0.00015649244595617755
stable component            0.003933453962422128
nonstable witness           0.009592456865886686
unstable support            0.27076032624289914
nonunstable witness         0.17547801719075545
saddle component            0.06278748839531187
nonsaddle witness           0.006434548385763544
obstruction/target support  0.27076032624289914
two-cell determinant        0.7521619340549729
closure-fan determinant     0.04036350227123123
```

Volume enclosure is `[22.058373744910437,22.058374009554672]`; the complete exact centroid enclosure is in `interval_certificate.json`.

## Search performed and scope

The search tested joint packet deletion with two-apex placements, coupled bridge-apex global/local motion, determinant-one metric motion, local and graded radial fields around all four packets, random coupled bridge configurations, and macroscopic return-lobe perturbations. No open `(1,1,0)` sample was found. These searches are empirical guidance; the endpoint, box, atlas, walls, edge obstruction, and radial theorem are exact.

## Independent verification and meshes

The aggregate transcript ends with `ALL VERIFIERS PASS` and includes:

- deterministic exact coordinate regeneration and byte comparison;
- standard-library clean-room exhaustive V-to-H and H-to-V reconstruction;
- exact volume, centroid, and three zero centred moments;
- exhaustive 162-face, 90-vertex, 250-edge four-component audit;
- exact packet/channel/two-cell/obstruction checks;
- exact `±10^-10` interval verifier;
- independent four-cell/wall atlas verifier;
- exact radial-order verifier;
- OBJ/STL watertightness and mass consistency.

The matching meshes have 90 vertices, 176 triangles, 264 triangulated edges and Euler number 2. Fourteen mesh-only edges triangulate the protected 17-gon. Recomputed volume is `22.058373877232558`; COM norm is `7.852358949702815e-16`.

## Sharpest genuinely new successor

Another point cap, scalar A/B opening, serial rail, fixed-topology metric polish, or surface refinement is subsumed. The smallest topology not represented is a **third nonsimplicial bridging cell**, equivalently an octahedral or triangular-prismatic `2<->3 / 3<->2` replacement carrying one shared interior-edge circuit through both paired-birth gates.

It must jointly absorb the connected residual core `{134,146,180,181,199,218,219}` and the radial-superlevel terminal set `{144,145,146,150,151,219}`; delete or replace `(218,219)` and `(146,219)` in the same event; couple direct gate `(146,218)` to return gate `[180,181,219]/(181,219)` through one common interior-edge flip; provide at least two macroscopic return-lobe actuators capable of overcoming the exact `>0.3217983` ordering bound; preserve the stable 17-gon and vertex `8`; and solve the three ordinary moments as hard dependent equations before every complete hull/full-cone rebuild.

## Integrity and artifacts

```text
archive SHA-256   3ed70a76341897abfade8aa68f241d68e71395d1b643e5e7e97e29c9f8f7773b
handoff SHA-256   e3c26d1c5a710335237b4cde699e08ad76ddf6d35701fb78577bdc06dcd91b69
manifest SHA-256  aacd7067528cd8a7cf5d67ad7225f3ddba503ffd4dcbc98cb3d4f22f60a18d03
certificate       023fb92e897e38c2cacadffff80c4ace75eb2a84196cb4f97030c283bfd71e75
exact verifier    432915e0fbc01c389c0d1b6c4eaf2f0bc2545d0612cf5c5cb7ea11648ebc050b
OBJ               0f795707e5dc03dd36a9fcd52d77ff84462bdeefd1d58ccd4a8210e922c74f71
STL               8e10a6a79182080ae040ade6645fced82ec948b861740c6eb8005cebf17bf324
transcript        75fb1a95bba49dc1f5b3e42d1865aa6dd1cfd71ab9916f3b7c86dc07c0417fcd
```

Complete self-contained handoff, including all 162 face cycles and 250 true edges (`research_handoff.md`)

Deterministic exact archive (`m42_two_cell_exact_handoff.zip`) · archive digest (`m42_two_cell_exact_handoff.zip.sha256`) · complete per-file manifest (`SHA256SUMS.txt`)

Generator (`generate_exact_endpoint.py`) · master certificate (`certificate.json`) · exact verifier (`verify_exact_cleanroom.py`) · interval verifier (`verify_interval.py`) · first chamber atlas (`first_chamber_atlas.json`) · radial certificate (`radial_order_certificate.json`) · two-cell certificate (`two_cell_complex.json`) · verification transcript (`RUN_ALL_VERIFIERS.txt`) · OBJ (`body.obj`) · STL (`body.stl`)
