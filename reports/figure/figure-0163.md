# figure-0163

AI research report · 2026-08-30 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact M42 third shared-interior-edge volumetric continuation

## Literal verdict

**NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedron was obtained. The strongest materialized successor is an exact rational, uniformly dense, own-centred polyhedron with strict class **`(2,2,2)`**.

The durable journal’s incoming endpoint was the exact two-nonsimplicial-cell `(90,250,162)` body, whose six-vertex radial-superlevel packet forced the present third-cell assignment. This turn genuinely crosses that frontier: it jointly removes the old residual core, the whole six-vertex superlevel terminal packet, both old paired-birth gates, and edges `(218,219)` and `(146,219)`. The former radial-order obstruction is solved—protected vertex `8` becomes the unique exact global farthest vertex—but the Euler-neutral block transfers to a new exact true-edge obstruction.

## Exact finite endpoint

- Input rows: `134` on the common lattice `10^-36`.
- Actual irredundant hull: `(V,E,F)=(92,256,166)`, complexity `512`, Euler number `2`.
- Active rows:

```text
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 54 69 72 73
130 131 132 133 135 136 137 138 139 140 141 142
153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172
175 176 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198
201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217
220 221 222
```

- Inactive rows:

```text
86 88 102 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129
134 143 144 145 146 147 148 149 150 151 152 173 174 177 178 179 180 181 199 200 218 219
```

The exact construction starts from `predecessor_two_cell_coordinates.csv`, puts

```text
{134,143,144,145,146,147,148,149,150,151,152,180,181,199,218,219}
```

at the exact interior control point

```text
CSTAR=(-22638817877·10^24, 9862693840·10^24, -7081176048·10^24)/10^36,
```

and adds

```text
220=(2498667797393,-2884051905141,-865392654376)/10^12
221=(2866953149070,-6660906984580,-1535167851984)/10^12
222=(3712882082663,-5945040770195,-825500569466)/10^12.
```

`generate_exact_endpoint.py` is deterministic and integer-only. The complete 134-row input table, exact centred V table, all 166 maximal-face cycles, all 256 true edges with their two incident faces, and the complete irredundant centred H table are embedded in the self-contained handoff.

## Exact ordinary volume and moments

Exact volume:

```text
25619060633297224562018099255810744391923529755526800477165256999348971135522076375722605295169185604186448291
/
1200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Decimal volume: `21.349217194414354`.

Exact unshifted ordinary-volume centroid:

```text
Cx=32580193428255847578437002483483908449362305914010747652825643035989397497437708314265897399582255979500065868664451805981754244678045121649819893
   /102476242533188898248072397023242977567694119022107201908661027997395884542088305502890421180676742416745793164000000000000000000000000000000000000

Cy=-38258428824677666559739285132922681800610461250501607799070870152168281275637238819657920858106580616019266148174773534657506573630984952111439067
   /102476242533188898248072397023242977567694119022107201908661027997395884542088305502890421180676742416745793164000000000000000000000000000000000000

Cz=-7483862806218346824722104071119111562593660332616042592331672062413717281452797819240743581251202487196298760067027905871275447915068469842224489
   /102476242533188898248072397023242977567694119022107201908661027997395884542088305502890421180676742416745793164000000000000000000000000000000000000.
```

The independent verifier recomputes the three unshifted moments and proves `M_k=V C_k` exactly. Translation by `-C` therefore gives centred first moments `(0/1,0/1,0/1)` before any equilibrium audit.

## Exhaustive mechanics

Stable maximal faces:

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  margin 0.3614496955836064
[201,220,221]                                  margin 0.17216379548226857
```

Unstable actual vertices:

```text
8    margin 0.353023401890133
153  margin 0.18951865513097374
```

Saddle true edges, each with all four components `(t,1-t,beta1,beta2)>0`:

```text
(130,222)  margin 0.1780534721230713
(176,182)  margin 0.11041166554780123
```

Global normalized minima:

```text
stable positive        0.17216379548226857
nonstable exclusion    0.08250515827686435
unstable positive      0.18951865513097374
nonunstable exclusion  0.00167160290094896
saddle positive        0.11041166554780123
nonsaddle exclusion    0.008736076948572197
topology distance      1.2008491288721667e-05
inactive distance      0.003247279353808712
```

Every face component, every adjacent-edge vertex support, and all four components of every true-edge cone are stored exactly and regenerated independently.

## Genuine third-cell topology

The new boundary triangle is `[220,222,221]`. Let `O` be the exact own centroid and `M=(x220+x221+x222)/3`. The actual centroid-fan complex contains

```text
C1=T(O,M,220,221) ∪ T(O,201,220,221)
C2=T(O,M,220,222) ∪ T(O,130,220,222)
C3=T(O,M,221,222) ∪ T(O,153,221,222).
```

Each union is a convex nonsimplicial triangular bipyramid. Exact positive barycentric coefficients prove that the `M`-to-boundary-apex segment crosses the relative interior of the corresponding equatorial triangle. All three cells share the interior radial edge `O-M`, so this is a literal `2↔3` shared-interior-edge replacement rather than a surface refinement.

All 25 closure-incident boundary triangles cone to nondegenerate tetrahedra; their shared-edge adjacency graph is connected. Over the positive coordinate box, the three-cell determinant lower bound is `1.8203979747241013` and the full closure-fan determinant lower bound is `0.15908564055285743`.

All assignment-named rows `{102,120,127,128,147,148,173,178,200}` and the obsolete terminal neighbors are non-extreme. Old edges `(218,219)`, `(146,219)`, `(147,148)`, `(95,96)`, `(82,96)`, `(96,104)`, and `(104,111)` are absent. The former direct gate `(146,218)` and return gate `[180,181,219]/(181,219)` are removed as incidence, not separately relayed.

## Radial order and transferred obstruction

Protected vertex `8` is the **unique exact global farthest vertex**. The predecessor’s six-vertex superlevel packet is gone; the directed perturbation box preserves a minimum squared-radius gap of `0.5048524906889521` over every other actual vertex.

The remaining exact obstruction is true edge `(153,154)`. Every nonmutual endpoint support is positive, with minimum external raw support `1.0804303894043819`. The mutual supports are

```text
sigma(153→154)=
2482691612609091878712080924059342753610531592158474005442419981340546327939079442163791718348658777615047938405407548408373646977395001756087265769436633176576823195787447081465311
/
2561906063329722456201809925581074439192352975552680047716525699934897113552207637572260529516918560418644829100000000000000000000000000000000000000000000000000000000000000000000000

sigma(154→153)=
-2413186313155801377271877879964590003849568941464193326402148982683167866588486758340487669440839739782419416570991364600685062453908592021344671583599130785169061287556124136826187
/
2561906063329722456201809925581074439192352975552680047716525699934897113552207637572260529516918560418644829100000000000000000000000000000000000000000000000000000000000000000000000,
```

and exactly

```text
sigma(153→154)+sigma(154→153)=||x154-x153||²
=678257689149559479691554820928956538122161924126237715452509374058391
 /25000000000000000000000000000000000000000000000000000000000000000000000 > 0.
```

Thus both mutual supports cannot be nonpositive. One endpoint remains unstable throughout the certified incidence/external-sign cell; vertex `8` is independently unstable, so `U≥2` throughout that cell.

## Exact witness-route obstruction on the current graph

For any nonpositive-support step `i→j`, `r_j cos(theta_ij)≥r_i`. Exact multiplicative Dijkstra over all 209 acute edges of the 256-edge graph proves that the cheapest current-direction route from `153` to `8` uses 56 true edges:

```text
153-154-155-156-157-158-159-160-161-162-163-164-165-166-167-168-169-170-171-172-175-176-182-183-184-185-186-187-188-189-190-191-192-193-194-195-196-197-198-201-202-203-204-205-206-207-208-209-210-211-212-213-214-215-216-217-8.
```

Its necessary radius ratio is in `(2.009856231268,2.009856231269)`, whereas the exact endpoint supplies only `(1.006567220148,1.006567220149)`; the squared deficit factor is in `(3.986983323807,3.986983323808)`. The dominant angular gap is edge `(176,182)`. Therefore arbitrary regrading of intermediate radii cannot drain `153` to `8` while keeping the exact current ray directions, true-edge graph, and endpoint radii. This theorem is intentionally local to that fixed graph; a new topology or macroscopic endpoint/centroid motion remains possible.

## Complete first outgoing chamber atlas

With

```text
q222(a)=CSTAR+(1+a)(q222-CSTAR),
q182(b)=CSTAR+(1+b)(q182-CSTAR),
```

the four rebuilt exact chambers are:

| chamber | `(a,b)` | `(V,E,F)` | class | new event |
|---|---:|---:|---:|---|
| `C00` | `(0,0)` | `(92,256,166)` | `(2,2,2)` | endpoint |
| `C10` | `(1/20,0)` | `(92,256,166)` | `(2,3,3)` | unstable `222` and saddle `(221,222)` birth |
| `C01` | `(0,3/50)` | `(88,244,158)` | `(3,2,3)` | stable `[172,175,182]` and saddle `(172,182)` birth |
| `C11` | `(1/20,3/50)` | `(88,244,158)` | `(3,3,4)` | both paired births |

The direct `U-H` wall is isolated in

```text
[354351841591/10^13, 354351841592/10^13],
```

and the return `S-H` wall in

```text
[578682293826/10^13, 578682293827/10^13].
```

Both brackets have exact width `10^-13`, and the controlling primitive signs are exact and opposite at their endpoints. Every chamber has complete actual incidence, exact mass/centroid, exhaustive mechanics, and the external-positive `(153,154)` obstruction. No chamber is `(1,1,0)`.

## Positive perturbation certificate

Rows `0..16` and all inactive inputs are fixed. Every coordinate of the other active rows—225 independent coordinates—may vary by `±10^-12`. Exact outward rational intervals preserve the complete `(92,256,166)` hull, inactive ledger, strict `(2,2,2)`, all old-channel absences, unique-farthest target `8`, all three nonsimplicial cells, and the `(153,154)` obstruction.

Directed lower bounds:

```text
facet determinant           4.5880401292077855e-07
inactive facet determinant  0.0007547939576999394
stable component            0.005198279960482136
nonstable witness           0.0014478476224235287
unstable support            0.2576890642983786
nonunstable witness         0.015406932746481307
saddle component            0.0466551119204749
nonsaddle witness           0.005142508207608251
obstruction/target support  0.2576890642983786
target radial gap           0.5048524906889521
three-cell determinant      1.8203979747241013
closure-fan determinant     0.15908564055285743
```

Volume remains in `[21.34921719319722,21.34921719563149]`.

## Attempts and scope

Two random three-apex searches rebuilt 3,500 valid complete hulls; no `(1,1,0)` state appeared. The selected three-cell topology was then subjected to coordinated residual-row motion, determinant-one metric search, differentiable metric plus graded radial fields, five-row filling of the `(176,182)` gap, independent and joint exact cell openings, macroscopic return-lobe scaling, and fixed-geometry mechanical-centre MILPs. The best numerical moves transferred or multiplied the block, often entering `(4,2,4)` or paired-birth chambers. These searches guide the endpoint and next topology but are not global nonexistence proofs.

## Independent verification and mesh

The aggregate transcript ends with `ALL VERIFIERS PASS`:

- deterministic exact coordinate regeneration and byte comparison;
- exhaustive standard-library supporting-triple V→H reconstruction: all 166 maximal faces;
- exact connected closed Euler-2 boundary and complete H/V agreement;
- exact volume, centroid, and all three moment identities;
- every face, actual vertex, and four-component true edge;
- exact absorption, radial order, three-cell decomposition, and obstruction;
- exact `±10^-12` interval certificate;
- exhaustive verification of all four outgoing chambers and both walls;
- exact multiplicative-Dijkstra route certificate;
- watertight OBJ/STL correspondence.

The OBJ/STL have 92 vertices, 180 triangles, 270 triangulated edges, Euler number `2`, recomputed volume `21.349217194414354`, and centre-of-mass norm `5.65×10^-16`. Fourteen mesh-only edges are triangulation diagonals of the protected 17-gon.

## Sharp next volumetric frontier

The smallest topology not represented is a **cross-gap fourth nonsimplicial witness cell**—an edge-sharing triangular-prismatic or octahedral `2↔3 / 3↔2` replacement whose common interior-edge circuit simultaneously spans:

```text
terminal obstruction       {153,154,221,222}
extra stable foot          [201,220,221]
direct saddle gate         (130,222)
return angular gap/saddle  (176,182).
```

It must delete or break `(153,154)` while replacing the extra stable face and both saddle stars in the same rebuilt event; add genuine short-angle cross-gap edges through the `176–182` gap; retain vertex `8` as unique farthest; and include at least two macroscopic return-lobe actuators in case endpoint/centroid radial reordering is still required. Three selected coordinates should remain hard dependent ordinary-moment variables. Another local cap, serial rail, scalar cell opening, fixed-topology metric polish, or intermediate-radius regrading is now subsumed.

## Integrity and artifacts

```text
archive SHA-256    03f6186cd231dd0710ec748046f4f3f5c28099f8569d67c1995f9b9510468b0a
handoff SHA-256    a8aafa6c5fb26e47e8bd2c8ec8aa2e9f4e03fb705f462f568e874b52082e5f23
certificate        2d0294b997b42d9dbbc549853bdfc08db65181a41af01d7083fd3bbcc2ba5d80
exact verifier     6693625c61e2430f01eb96a33f9deaa2e1572579ecc1f9fbbcb5512d17dbc01d
interval verifier  f18b91b6467466f095890c7cf1df98ab47beda85a0a8bc4ba1bf60f8f19c8a1
chamber atlas      4993fab9b3ec347f19659b8ba1b053af187bc208b3c1ba7b0765deb607ffd956
route certificate  36dde30563cbfd8214a15f8eaab3416b8fdcb0aafd2d31a9fa0118bd7569bb8c
OBJ                 6b47c2fad9de26c7eb809159c9a06512a416b3159ef61150d3f4accf1982a90b
STL                 e44c664d997f75f9195e9347b16fb05a064b06857c1821a0ab9d855a19b0e5eb
transcript          276151387a4d0599e7048e35c6012ffcf985cdcc571c4fbcc2996bc5adeb432f
```

Complete self-contained handoff with all 134 rows, 166 face cycles, 256 true edges, exact V and H tables (`research_handoff.md`)

Deterministic exact archive (`m42_three_cell_exact_handoff.zip`) · archive digest (`m42_three_cell_exact_handoff.zip.sha256`) · per-file manifest (`SHA256SUMS.txt`)

Generator (`generate_exact_endpoint.py`) · master certificate (`certificate.json`) · exact verifier (`verify_exact_cleanroom.py`) · interval verifier (`verify_interval.py`) · three-cell certificate (`three_cell_complex.json`) · first chamber atlas (`first_chamber_atlas.json`) · atlas verifier (`verify_first_chamber_atlas.py`) · route certificate (`route_bound_certificate.json`) · route verifier (`verify_route_bound.py`) · transcript (`RUN_ALL_VERIFIERS.txt`) · OBJ (`body.obj`) · STL (`body.stl`)
