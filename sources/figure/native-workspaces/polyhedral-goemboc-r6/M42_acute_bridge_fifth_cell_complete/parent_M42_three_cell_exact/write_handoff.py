#!/usr/bin/env python3
from pathlib import Path
import csv,json,hashlib
R=Path(__file__).resolve().parent
D=json.load(open(R/'certificate.json'));I=json.load(open(R/'interval_certificate.json'));T=json.load(open(R/'three_cell_complex.json'));A=json.load(open(R/'first_chamber_atlas.json'));RB=json.load(open(R/'route_bound_certificate.json'));S=json.load(open(R/'search_summary.json'))

def fmt_ids(xs,w=100):
 s=' '.join(map(str,xs));out=[]
 while len(s)>w:
  k=s.rfind(' ',0,w+1)
  if k<0:k=w
  out.append(s[:k]);s=s[k+1:]
 out.append(s);return '\n'.join(out)
def link(name):return f'[**{name}**](sandbox:/mnt/data/m42_three_cell_exact/{name})'
def qblock(x):return '```text\n'+str(x)+'\n```\n'
newrows='\n'.join(f"{i} ({', '.join(v)})" for i,v in D['new_rows'].items())
cellrows=[]
for c in A['cells']:
 cellrows.append('| `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |'.format(c['name'],c['parameters'],tuple(c['f_vector']),tuple(c['class']),[x['cycle'] for x in c['stable_faces']],[x['vertex'] for x in c['unstable_vertices']]))
wallrows=[]
for w in A['wall_brackets']:
 wallrows.append(f"- `{w['name']}`: `{w['interval_exact'][0]}` to `{w['interval_exact'][1]}`, exact width `{w['width_exact']}`; class changes `{w['states'][0]['class']} -> {w['states'][1]['class']}` with both named primitive signs changing together.")
faces=json.load(open(R/'face_cycles.json'))
face_text='\n'.join(f'{i}: '+','.join(map(str,c)) for i,c in enumerate(faces))
edge_lines=[]
with open(R/'true_edges.csv') as f:
 for r in csv.DictReader(f):edge_lines.append(f"({r['u']},{r['v']}):{r['incident_face_1']},{r['incident_face_2']}")
edge_text='\n'.join(edge_lines)
input_csv=(R/'coordinates_all_exact.csv').read_text()
active_v_csv=(R/'coordinates_active_centered.csv').read_text()
h_csv=(R/'halfspaces_centered.csv').read_text()
obs=D['obstruction']
route=' -> '.join(map(str,RB['shortest_path']))
md=f'''# Exact M42 third shared-interior-edge volumetric continuation

## Literal determination

**NONWINNER.** The materialized body is a finite, uniformly dense convex rational polyhedron at its own exact ordinary-volume centroid, but its strict equilibrium class is **`(S,U,H)=(2,2,2)`**, not `(1,1,0)`.

This continuation does perform the topology requested by the assignment. It replaces the prior two-cell terminal structure by **three triangular-bipyramidal nonsimplicial centroid-fan cells sharing one interior radial edge**. The former residual core, former six-vertex radial-superlevel terminal packet, both old paired-birth gates, and true edges `(218,219)` and `(146,219)` are jointly removed. The protected 17-gon and protected unstable vertex `8` survive, and vertex `8` becomes the unique exact global farthest vertex. The Euler-neutral mechanical block nevertheless transfers to a new connected packet.

The exact negative conclusion is limited to this endpoint, its positive coordinate box, and the first four exact outgoing chambers. Empirical searches do not establish a global impossibility theorem.

## What changed from the exact two-cell predecessor

The previous exact endpoint had `(V,E,F)=(90,250,162)` and an obstruction supported by the residual A/B packet. This continuation:

- collapses the complete assignment-named set `{sorted(D['absorbed_rows'])}` to the exact interior control point;
- retains the earlier collapsed rows `{sorted(D['old_absorbed_rows_from_predecessor'])}`;
- adds three exact external rows `220,221,222` whose boundary triangle supplies the central `2<->3` circuit;
- deletes every old channel in `{D['absent_old_edges']}`;
- rebuilds the actual hull as `(V,E,F)=({D['f_vector'][0]},{D['f_vector'][1]},{D['f_vector'][2]})`, complexity `{D['complexity']}`;
- makes target `8` the unique exact farthest actual vertex, eliminating the predecessor's six-vertex radial-order obstruction;
- transfers the residual maximum to the exact external-positive true edge `(153,154)`.

The former direct gate `(146,218)` and return gate `[180,181,219]/(181,219)` are absent because all of their gate rows are interior in the new body. They are not opened separately or relabelled on the boundary.

## Complete deterministic rational construction

All coordinates use the common denominator

```text
S = 10^36,  K = 10^24.
```

Start with the 131 exact input rows in `predecessor_two_cell_coordinates.csv`. Put every row in

```text
ABSORB = {{134,143,144,145,146,147,148,149,150,151,152,180,181,199,218,219}}
```

at

```text
CSTAR = (-22638817877*K, 9862693840*K, -7081176048*K)/S.
```

Add

```text
{newrows}
```

where each displayed coordinate is exact. `generate_exact_endpoint.py` performs exactly these operations, computes the ordinary volume and all three first moments from the certified oriented boundary, applies the dependent translation `tau=-M/V`, byte-compares regenerated coordinate tables, and invokes the independent verifier.

There are `{D['input_rows']}` input rows. The actual active rows are

```text
{fmt_ids(D['active_rows'])}
```

The inactive rows are

```text
{fmt_ids(D['inactive_rows'])}
```

Every inactive input has positive exact/directed separation from the complete boundary; the minimum normalized inactive distance is `{D['margins']['inactive_distance_min']}`.

## Exact ordinary volume and first moments

Exact volume:

```text
{D['volume_exact']}
```

Decimal: `{D['volume_decimal']}`.

Exact unshifted ordinary first moments:

```text
Mx = {D['first_moments_unshifted_exact'][0]}
My = {D['first_moments_unshifted_exact'][1]}
Mz = {D['first_moments_unshifted_exact'][2]}
```

Exact unshifted volume centroid:

```text
Cx = {D['centroid_unshifted_exact'][0]}
Cy = {D['centroid_unshifted_exact'][1]}
Cz = {D['centroid_unshifted_exact'][2]}
```

The clean-room verifier independently proves `Mk=V*Ck` for `k=x,y,z`; after translation by `-C`, the three centred first moments are exactly `(0/1,0/1,0/1)`.

## Complete strict equilibrium audit

Stable maximal faces:

- protected 17-gon `{D['stable_faces'][0]['cycle']}`, normalized full-polygon margin `{D['stable_faces'][0]['decision_normalized']}`;
- extra triangle `{D['stable_faces'][1]['cycle']}`, normalized margin `{D['stable_faces'][1]['decision_normalized']}`.

Unstable actual vertices:

- protected target `8`, normalized adjacent-edge support margin `{D['unstable_vertices'][0]['decision_normalized']}`;
- extra vertex `153`, margin `{D['unstable_vertices'][1]['decision_normalized']}`.

Saddle true edges:

- `(130,222)`, full four-component decision margin `{D['saddle_edges'][0]['decision_normalized']}`;
- `(176,182)`, margin `{D['saddle_edges'][1]['decision_normalized']}`.

Global endpoint minima:

```text
stable positive        {D['margins']['stable_positive_min']}
nonstable exclusion    {D['margins']['nonstable_exclusion_min']}
unstable positive      {D['margins']['unstable_positive_min']}
nonunstable exclusion  {D['margins']['nonunstable_exclusion_min']}
saddle positive        {D['margins']['saddle_positive_min']}
nonsaddle exclusion    {D['margins']['nonsaddle_exclusion_min']}
topology distance      {D['margins']['topology_distance_min']}
inactive distance      {D['margins']['inactive_distance_min']}
```

The machine ledgers contain every individual primitive:

- {link('faces_mechanics.json')} — every polygon-edge component of every maximal face;
- {link('vertices_mechanics.csv')} — every true-neighbour support at every actual vertex;
- {link('edges_four_component_audit.csv')} — exact `(t,1-t,beta1,beta2)` for every true edge.

## Exact three-cell volumetric topology

The central boundary face is `{T['central_boundary_face']}`. Let `O=(0,0,0)` be the exact own centroid and

```text
M=(x220+x221+x222)/3.
```

The three cells are

```text
C1 = T(O,M,220,221) union T(O,201,220,221)
C2 = T(O,M,220,222) union T(O,130,220,222)
C3 = T(O,M,221,222) union T(O,153,221,222)
```

Each union is a convex nonsimplicial triangular bipyramid. For every cell the exact segment from `M` to its boundary apex intersects the relative interior of the shared equatorial triangle `O-u-v`; all exact barycentric coefficients are strictly positive. The three cells share the interior radial edge `O-M` and meet through the central `2<->3` subdivision.

All `{T['closure_incident_faces']}` boundary faces incident to `220,221,222` cone to nondegenerate centroid-fan tetrahedra. Their shared-edge adjacency graph is connected. Exact determinants and barycentric certificates are in {link('three_cell_complex.json')}. Directed lower bounds over the perturbation box are `{I['strict_lower_bounds']['three_cell_tetra_determinant']}` for the three-cell tetrahedra and `{I['strict_lower_bounds']['closure_fan_determinant']}` for the full closure fan.

The closure contacts the terminal, direct, return, and stable-foot sectors through the exact active row sets recorded in `three_cell_complex.json`. This is genuine communicating volume incidence, not a surface subdivision or longer serial rail.

## Fate of radial order

The predecessor's six-vertex superlevel packet is removed. At the exact own centroid, protected vertex `8` is the unique global farthest actual vertex. Its exact squared-radius gap over the next vertex is positive, and the directed box lower bound is `{I['strict_lower_bounds']['target_unique_farthest_squared_gap']}`.

Thus the prior radial-order obstruction has been solved. The residual extra unstable vertex `153` lies strictly closer to the centroid than target `8`; the remaining failure is a witness-routing/incidence obstruction, not the absence of a farther intended target.

## Exact transferred true-edge obstruction

True edge `(153,154)` has every nonmutual endpoint support strictly positive. Its exact mutual supports are

```text
sigma(153->154) = {obs['mutual_A']}
sigma(154->153) = {obs['mutual_B']}
```

and

```text
sigma(153->154)+sigma(154->153)
 = ||x154-x153||^2
 = {obs['sum_squared_edge']} > 0.
```

The minimum external raw support is `{obs['minimum_external_raw']}`. Therefore the two mutual supports cannot both be nonpositive: throughout the certified incidence/external-sign cell, at least one endpoint remains unstable. Vertex `8` is independently strictly unstable, so the entire cell has `U>=2`.

## Exact fixed-direction witness-route bound

For a directed true-edge step `i->j`, `sigma(i->j)<=0` implies

```text
r_j cos(theta_ij) >= r_i.
```

Multiplying along a path gives the necessary condition

```text
(r_end/r_start)^2 >= product sec(theta_ij)^2.
```

An exact multiplicative Dijkstra search over all `{RB['acute_edges']}` acute edges of the `{RB['true_edges']}`-edge actual graph proves that the globally least expensive route from `153` to target `8` is the `{RB['edge_count']}`-edge path

```text
{route}
```

The exact minimum product is stored in `route_bound_certificate.json` and authenticated by SHA-256 `{RB['shortest_required_radius_ratio_squared_sha256']}`. Directed decimal brackets are

```text
required radius ratio: {RB['shortest_required_radius_ratio_bracket']}
actual endpoint ratio: {RB['actual_endpoint_radius_ratio_bracket']}
squared deficit factor: {RB['squared_gap_factor_bracket']}
```

The dominant existing angular gap is true edge `(176,182)`. Consequently, even allowing arbitrary regrading of all intermediate radial heights, the current exact directions, graph, and endpoint radii cannot route the extra maximum to `8`. New cross-gap directions/incidence or macroscopic endpoint/centroid reordering is necessary. This theorem is deliberately scoped to the current fixed ray-direction graph; it is not a global obstruction after a new topology.

## Complete first outgoing chamber atlas

Use

```text
q222(a)=CSTAR+(1+a)(q222-CSTAR),
q182(b)=CSTAR+(1+b)(q182-CSTAR).
```

Every representative below is rebuilt from all exact input rows, with complete supporting-plane enumeration, exact mass and own centroid, complete actual faces/true edges, and every normal cone:

| chamber | parameters | actual `(V,E,F)` | class | stable faces | unstable vertices |
|---|---|---:|---:|---|---|
{chr(10).join(cellrows)}

The saddle sets are, respectively:

```text
C00: (130,222), (176,182)
C10: (131,222), (176,182), (221,222)
C01: (130,222), (172,182), (175,182)
C11: (131,222), (172,182), (175,182), (221,222)
```

Exact isolated walls:

{chr(10).join(wallrows)}

Hence opening the direct cell creates a paired `U-H` birth at vertex `222` / edge `(221,222)`, while opening the return cell creates a paired `S-H` birth at face `[172,175,182]` / edge `(172,182)`. Opening both gives `(3,3,4)`. No first outgoing chamber is `(1,1,0)`, and the obstruction edge `(153,154)` remains externally positive in every representative.

The complete atlas is {link('first_chamber_atlas.json')}; its independent exhaustive verifier is {link('verify_first_chamber_atlas.py')}.

## Positive coordinate box

Rows `0..16` and every inactive input are fixed. Every coordinate of each other active row—`{I['variable_coordinates']}` independent coordinates—may vary by

```text
+/- {I['radius_exact']}.
```

Exact outward `Fraction` intervals preserve the complete `(92,256,166)` hull, strict `(2,2,2)` class, all inactive rows, every old-channel deletion, target `8` as unique farthest, all three nonsimplicial cells, and the external-positive `(153,154)` obstruction.

Volume enclosure:

```text
{I['volume_box'][0]}
<= V <=
{I['volume_box'][1]}
```

Directed lower bounds:

```text
facet determinant           {I['strict_lower_bounds']['facet_determinant']}
inactive facet determinant  {I['strict_lower_bounds']['inactive_facet_determinant']}
stable component            {I['strict_lower_bounds']['stable_face_component']}
nonstable witness           {I['strict_lower_bounds']['nonstable_witness']}
unstable support            {I['strict_lower_bounds']['unstable_vertex_support']}
nonunstable witness         {I['strict_lower_bounds']['nonunstable_witness']}
saddle component            {I['strict_lower_bounds']['saddle_edge_component']}
nonsaddle witness           {I['strict_lower_bounds']['nonsaddle_witness']}
obstruction/target support  {I['strict_lower_bounds']['obstruction_and_target_support']}
target radial gap           {I['strict_lower_bounds']['target_unique_farthest_squared_gap']}
three-cell determinant      {I['strict_lower_bounds']['three_cell_tetra_determinant']}
closure-fan determinant     {I['strict_lower_bounds']['closure_fan_determinant']}
```

## Search scope and attempted falsification

Two random three-apex searches evaluated `{S['random_three_apex_searches'][0]['valid_samples'] + S['random_three_apex_searches'][1]['valid_samples']}` valid complete hulls; none was `(1,1,0)`. The selected endpoint was then polished for strict topology/inactive margins and exact unique-farthest radial order. Further work included:

- coordinated motion of residual rows `130,153,154,176,182,198,201,220,221,222`;
- determinant-one metric search;
- differentiable metric plus graded direct/return radial fields;
- five-row filling/regrading of the return gap near `(176,182)`;
- independent and joint exact opening of `222` and `182`;
- common macroscopic return-lobe scaling;
- fixed-geometry mechanical-centre MILPs on predecessor and packet-deletion hulls.

The best unconstrained local hard score improved numerically but entered larger classes such as `(4,2,4)`; metric and field searches transferred the block to neighboring faces/vertices/edges. These are empirical observations only. The exact claims are the endpoint, its coordinate box, first chamber atlas and wall signs, obstruction identity, radial order, fixed-direction route bound, and mesh verification.

## Sharpest genuinely new continuation

The present assignment's third cell is now represented exactly and the former six-vertex radial-order packet is gone. A fourth local cap, scalar cell opening, serial rail, metric polish, or intermediate-radius regrading is subsumed.

The smallest unrepresented topology is a **cross-gap fourth nonsimplicial witness cell**, equivalently an edge-sharing triangular-prismatic/octahedral `2<->3 / 3<->2` replacement whose common interior-edge circuit simultaneously spans:

```text
terminal obstruction       {{153,154,221,222}}
extra stable foot          [201,220,221]
direct saddle gate         (130,222)
return angular gap/saddle  (176,182)
```

It must delete or break the external-positive edge `(153,154)` while replacing both saddle stars and the extra stable face in the same rebuilt incidence event; add actual short-angle cross-gap edges bridging the `176--182` gap into the terminal-to-target route; retain target `8` as unique farthest; and provide at least two macroscopic return-lobe actuators so endpoint/centroid radii can change if the new graph still fails the exact route inequality. Three selected coordinates must remain hard dependent variables solving the ordinary first moments before each full hull and full-cone audit.

This is genuinely different from extending either existing rail: it changes the witness graph and couples all four residual Morse features through one shared interior-edge circuit.

## Independent verification and mesh

The aggregate transcript {link('RUN_ALL_VERIFIERS.txt')} ends with `ALL VERIFIERS PASS` and contains:

1. deterministic exact coordinate regeneration and byte comparison;
2. exhaustive standard-library V-to-H reconstruction from every unique input triple;
3. closed connected Euler-2 boundary and exact H/V agreement;
4. exact volume, centroid, and three zero centred moments;
5. exhaustive audit of all 166 maximal faces, 92 actual vertices, and all four components of all 256 true edges;
6. exact old-packet absorption, unique-farthest target, three-cell complex, and `(153,154)` obstruction;
7. exact `+/-10^-12` interval box;
8. exhaustive exact verification of all four outgoing chambers and both width-`10^-13` walls;
9. exact multiplicative-Dijkstra route theorem;
10. watertight OBJ/STL correspondence.

The matching meshes have 92 vertices, 180 triangles, 270 triangulated edges, Euler number 2, recomputed volume `21.349217194414354`, and centre-of-mass norm `5.645351923447842e-16`. The 14 mesh-only edges are diagonals used solely to triangulate the protected 17-gon.

Key artifacts:

- {link('generate_exact_endpoint.py')}
- {link('certificate.json')}
- {link('verify_exact_cleanroom.py')}
- {link('verify_interval.py')}
- {link('first_chamber_atlas.json')}
- {link('verify_first_chamber_atlas.py')}
- {link('route_bound_certificate.json')}
- {link('verify_route_bound.py')}
- {link('three_cell_complex.json')}
- {link('radial_order_certificate.json')}
- {link('body.obj')}
- {link('body.stl')}

## Complete actual maximal-face cycles

```text
{face_text}
```

## Every true edge and its two incident maximal faces

```text
{edge_text}
```

## Complete exact input-row table

```csv
{input_csv}```

## Complete exact own-centred active V table

```csv
{active_v_csv}```

## Complete exact irredundant centred H table

```csv
{h_csv}```
'''
(R/'research_handoff.md').write_text(md)
print('wrote handoff',len(md),'chars')
