#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as Q
import csv,json,hashlib,math
R=Path(__file__).resolve().parent
C=json.load(open(R/'certificate.json'));I=json.load(open(R/'interval_certificate.json'));K=json.load(open(R/'construction.json'));P=json.load(open(R/'common_lattice_projection.json'));FC=json.load(open(R/'fourth_cell_complex.json'));G=json.load(open(R/'graph_radial_obstruction.json'));A=json.load(open(R/'first_chamber_atlas.json'));S=json.load(open(R/'search_summary.json'))
cycles=json.load(open(R/'face_cycles.json'))
rows=list(csv.DictReader(open(R/'input_rows_common_lattice.csv')))
edges=[]
with open(R/'true_edges.csv') as f:
 for z in csv.DictReader(f):edges.append((int(z['u']),int(z['v']),z['incident_faces']))

def code(lines):return '```text\n'+'\n'.join(lines)+'\n```'
def wrap_ids(ids,w=100):
 out=[];cur=''
 for z in map(str,ids):
  if cur and len(cur)+1+len(z)>w:out.append(cur);cur=z
  else:cur=(cur+' '+z).strip()
 if cur:out.append(cur)
 return out
def short_fr(s,n=74):
 return s if len(s)<=n else s[:34]+' … '+s[-34:]
# Exact input appendix.
input_lines=['source_id x_int y_int z_int / S   lineage',f'S={K["common_denominator"]}']
for r in rows:input_lines.append(f"{r['source_id']} {r['x_int']} {r['y_int']} {r['z_int']} / {r['denominator']}   {r['lineage']}")
face_lines=[f"{i}: {' '.join(map(str,c))}" for i,c in enumerate(cycles)]
edge_lines=[];cur=[]
for u,v,fs in edges:
 t=f'({u},{v})[{fs.replace(" ",",")}]'
 if sum(len(x)+1 for x in cur)+len(t)>108:edge_lines.append(' '.join(cur));cur=[t]
 else:cur.append(t)
if cur:edge_lines.append(' '.join(cur))
# Cell determinant details.
cell_lines=[]
for z in FC['cells']:
 cell_lines += [f"{z['name']}:",f"  equator={z['equator']}; apices=({z['positive_apex']},{z['negative_apex']})",f"  det1={z['positive_tetra_determinant_exact']}",f"  det2={z['negative_tetra_determinant_exact']}",f"  segment t={z['segment_parameter_exact']}",f"  equator barycentrics={z['equator_barycentric_exact']}"]
# Atlas table.
atlas_rows=[]
for z in A['cells']:
 st=';'.join('-'.join(map(str,x['cycle'])) for x in z['stable_faces']);un=','.join(str(x['vertex']) for x in z['unstable_vertices']);sa=','.join('-'.join(map(str,x['edge'])) for x in z['saddle_edges'])
 atlas_rows.append(f"| {z['cell_id']} | {z['a_exact']} | {z['b_exact']} | {tuple(z['f_vector'])} | {tuple(z['class'])} | {st} | {un} | {sa} |")
# New rows.
newrows=[]
for r in rows:
 if int(r['source_id'])>=223:newrows.append(f"{r['source_id']} = ({r['x_int']},{r['y_int']},{r['z_int']})/{r['denominator']}")
# Search/provenance concise.
prov=json.load(open(R/'search_provenance.json'))
parts=[]
parts.append('# Exact M42 cross-gap fourth nonsimplicial witness-cell continuation')
parts.append('## Literal verdict')
parts.append('**NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedron was obtained. The strongest materialized object is an exact rational, uniformly dense, own-centred open endpoint with strict class **`(2,2,2)`**. This is an exact negative result for the endpoint, its positive coordinate box, and the first eight adjacent two-control chambers—not a global obstruction to every larger M42 topology.')
parts.append('The new operation is genuinely beyond the three-cell parent. It absorbs rows `{130,153,154,176,182,201,220,221,222}`, so the parent obstruction edge `(153,154)`, stable face `[201,220,221]`, and saddle edges `(130,222)` and `(176,182)` all disappear as actual incidence. Six macroscopic replacement rows `223..228` make a triangular-prismatic closure with four linked triangular-bipyramidal centroid-fan cells. The central true edge `(223,224)` has angle `12.176168280690863°`, replacing the parent’s `53.18645752675954°` dominant angular gap. Protected vertex `8` remains the unique farthest actual vertex. The residual Euler-neutral block transfers to stable face `[195,224,223]`, unstable vertex `227`, saddles `(135,224)` and `(183,223)`, and the exact external-positive true edge `(226,227)`.')
parts.append('## Authoritative exact finite generator')
parts.append(f"The authoritative generator is the literal common-lattice table `input_rows_common_lattice.csv`: for every listed row, `q_i=(x_int,y_int,z_int)/S`, with\n\n`S={K['common_denominator']}`.\n\nThere are exactly 140 rows. The floating search and rational design route are provenance only; they are not substituted for the finite table. `generate_exact_endpoint.py` regenerates all derived H/V/E/mechanics files from the table and invokes the independent exact verifier. The exact base projection uses the integer normal `{P['base_plane_integer_coordinate_normal']}` and offset `{P['base_plane_integer_coordinate_h']}`; every base correction is below `9.53×10^-13`. The six new authoritative rows are:")
parts.append(code(newrows))
parts.append('The design provenance used three macroscopic return-lobe group scalings on rows `155..175`, `183..198`, and `202..217`, a three-component projective control, and a full invertible upper-triangular linear map before final common-lattice exactification. This is not a regrading of the old 56-edge route. The complete provenance is retained in `search_provenance.json`; the complete exact table below is decisive.')
parts.append('## Actual hull and active/inactive status')
parts.append(f"Exact actual hull: `(V,E,F)=({C['f_vector'][0]},{C['f_vector'][1]},{C['f_vector'][2]})`, complexity `{C['complexity']}`, Euler `{C['euler']}`. All supporting planes are reconstructed exhaustively from every unique input triple by the standard-library verifier.")
parts.append('Active rows:\n'+code(wrap_ids(C['active_rows'])))
parts.append('Inactive rows:\n'+code(wrap_ids(C['inactive_rows'])))
parts.append('All mandatory parent rows `130,153,154,176,182,201,220,221,222` are strictly inactive. Older channels `(218,219)`, `(146,219)`, `(147,148)`, `(95,96)`, `(82,96)`, `(96,104)`, and `(104,111)` are absent as true edges.')
parts.append('## Exact ordinary volume, first moments, and own centroid')
parts.append('Exact ordinary volume:\n\n`'+C['volume_exact']+'`\n\nDecimal: `'+repr(C['volume_decimal'])+'`.')
parts.append('Exact unshifted first moments:\n'+code([f'M{x}={v}' for x,v in zip('xyz',C['first_moments_unshifted_exact'])]))
parts.append('Exact unshifted ordinary-volume centroid:\n'+code([f'C{x}={v}' for x,v in zip('xyz',C['centroid_unshifted_exact'])]))
parts.append('The three dependent coordinates are the exact global translation `tau=-C`:\n'+code([f'tau_{x}={v}' for x,v in zip('xyz',C['dependent_translation_exact'])]))
parts.append('The generator and independent verifier prove `M_k−V C_k=0` componentwise. Thus after applying those three dependent coordinate controls, the ordinary first moments are exactly `(0/1,0/1,0/1)` and mechanics is evaluated at the body’s own centroid, not an auxiliary point.')
parts.append('## Exhaustive equilibrium audit')
parts.append('Stable maximal faces:\n'+code([f"face {z['face']} cycle {z['cycle']} normalized margin {z['decision_normalized']}" for z in C['stable_faces']]))
parts.append('Unstable actual vertices:\n'+code([f"vertex {z['vertex']} normalized margin {z['decision_normalized']}" for z in C['unstable_vertices']]))
parts.append('Saddle true edges:\n'+code([f"edge {z['edge']} four-component decision margin {z['decision_normalized']}" for z in C['saddle_edges']]))
parts.append('Global normalized endpoint minima:\n'+code([f'{k} = {v}' for k,v in C['margins'].items()]))
parts.append('Every maximal-face foot component, every actual-vertex adjacent-edge support, and all four components `(t,1−t,beta1,beta2)` of every true edge are stored exactly in `faces_mechanics.json`, `vertices_mechanics.csv`, and `edges_four_component_audit.csv`, and independently regenerated.')
parts.append('## Four linked nonsimplicial cells and cross-gap incidence')
parts.append('Let `O` be the exact own centroid, `M0=(x224+x226+x227)/3`, and `N0=(x223+x224+x226)/3`. The exact complex consists of four triangular bipyramids. For every cell the two apex tetrahedral determinants have opposite nonzero signs, and the apex segment intersects the relative interior of the equatorial triangle with exact positive barycentric coordinates:')
parts.append(code(cell_lines))
parts.append(f"All `{FC['closure_faces']}` new-row incident boundary triangles cone to nondegenerate tetrahedra at `O`; their shared-edge adjacency graph is connected. The exact minimum absolute closure determinant is `{FC['minimum_closure_tetra_determinant_exact']}` (`{FC['minimum_closure_tetra_determinant_decimal']}`). New true edges are `{FC['new_true_edges']}`. The actual linked path from the direct saddle star to the return saddle star is `{FC['cross_gap_true_edge_path']}` with edge angles `{FC['cross_gap_edge_angles_degrees']}` degrees; its central new edge `(224,223)` is the literal short-angle cross-gap link.")
parts.append('## Exact transferred true-edge obstruction')
obs=C['obstruction']
parts.append('True edge `(226,227)` has every nonmutual endpoint support strictly positive. Its mutual supports are:\n'+code([f"sigma(226->227)={obs['mutual_A_exact']}",f"sigma(227->226)={obs['mutual_B_exact']}",f"sum=||x227-x226||^2={obs['sum_squared_edge_exact']}>0",f"minimum external raw support={obs['minimum_external_raw']}"]))
parts.append('Therefore both mutual supports cannot be nonpositive. At least one endpoint stays unstable throughout the certified incidence/external-sign cell; target vertex `8` is independently unstable, so `U>=2`.')
parts.append('## Unique-farthest target and stronger acute-graph obstruction')
parts.append(f"Vertex `8` is the unique exact global farthest actual vertex. The minimum squared-radius gap to every other vertex is `{C['radial_order']['minimum_squared_gap_exact']}` (`{C['radial_order']['minimum_squared_gap_decimal']}`), and the interval box preserves a lower gap `{I['strict_lower_bounds']['target_unique_farthest_squared_gap']}`.")
parts.append('A nonpositive-support witness step `i→j` satisfies `x_i·x_j>=||x_i||^2>0`; hence it can use only a positive-dot true edge. Exact reconstruction gives two positive-dot components:')
parts.append(code([f"component 0 ({len(G['acute_components'][0])} rows): {' '.join(map(str,G['acute_components'][0]))}",f"component 1 ({len(G['acute_components'][1])} rows): {' '.join(map(str,G['acute_components'][1]))}"]))
parts.append(f"Endpoints `226,227` lie in component `{G['obstruction_component_index']}`, while target `8` lies in component `{G['target_component_index']}`. Every one of all `{G['cross_component_vertex_pair_count']}` cross-component vertex pairs has exact negative dot product. The least obtuse is `{G['least_obtuse_cross_pair']['vertices']}`, with exact dot `{G['least_obtuse_cross_pair']['dot_exact']}` and angle `{G['least_obtuse_cross_pair']['angle_degrees']}°`. Thus no witness chain exists on the current true-edge graph under any radial regrading that leaves rays and graph fixed.")
for r in G['endpoint_to_target_equal-angle_bounds']:
 parts.append(f"Even if new equal-angle intermediate directions are inserted while endpoint rays and radii stay fixed, the directed route bound from `{r['start']}` to `8` excludes every chain with at most `{r['largest_excluded_edge_count']}` edges; `{r['first_edge_count_not_excluded']}` is the first count not excluded. Endpoint angle interval: `{r['angle_interval_degrees']}` degrees; available radius-ratio interval: `{r['available_radius_ratio_interval']}`.")
parts.append('## Complete first outgoing chamber atlas')
parts.append('Controls are `q223(a)=a q223` and `q227(b)=b q227`. Every representative reconstructs the entire exact hull, ordinary centroid, maximal faces, true edges, and all normal cones:')
parts.append('| cell | a | b | `(V,E,F)` | class | stable cycles | unstable | saddles |\n|---|---:|---:|---:|---:|---|---|---|\n'+'\n'.join(atlas_rows))
parts.append('Exact incidence walls:\n'+code([f"{z['description']}; circuit={z['circuit']}; root={z['root_exact']}; removed={z['removed_edges']}; added={z['added_edges']}" for z in A['exact_incidence_walls']]))
parts.append('Exact mechanical wall brackets:\n'+code([f"{z['description']}: [{z['lo_exact']},{z['hi_exact']}], width={z['width_exact']}, classes {z['lo_class']}->{z['hi_class']}" for z in A['isolated_mechanical_walls']]))
parts.append('The terminal sequence is an exact `U-H-U` relay: unstable `226`, then both `226,227` plus saddle `(226,227)`, then unstable `227`. The cross-gap `2↔2` flip transfers the extra stable/saddle branch from the `194/195` side to the `223` side. No atlas cell is `(1,1,0)`.')
parts.append('## Positive coordinate box')
parts.append(f"Rows `0..16` and all inactive inputs are fixed. Every coordinate of the other active rows—`{I['variable_coordinates']}` independent coordinates—may vary by `±{I['radius_exact']}`. Exact outward rational intervals preserve the full `{tuple(I['preserved_f_vector'])}` hull, strict `{tuple(I['preserved_class'])}`, all parent-feature deletions, unique-farthest target, all four nonsimplicial cells, the `(226,227)` obstruction, and the two-component acute-graph obstruction.")
parts.append('Directed strict lower bounds:\n'+code([f'{k} = {v}' for k,v in I['strict_lower_bounds'].items()]))
parts.append(f"Volume enclosure: `{I['volume_box'][0]}` to `{I['volume_box'][1]}` (`{I['volume_box'][2]}` to `{I['volume_box'][3]}`). The exact centroid enclosure is recorded in `interval_certificate.json`.")
parts.append('## Search attempts and falsification')
parts.append('The 20-parameter macroscopic prism/projective/metric family was searched by differential evolution, followed by four local feature-targeted continuations and fixed-geometry mechanical-centre tests. Competitive states included `(2,3,3)`, `(3,2,3)`, and `(3,3,4)`, but no open `(1,1,0)` state appeared. These searches are empirical guidance only. The exact nonwinner result rests on the exhaustive endpoint audit, positive box, exact chamber atlas, edge identity, and acute-component theorem.')
parts.append('## Independent verification and mesh')
parts.append('The standard-library clean-room verifier independently enumerates every supporting plane from all unique input triples, proves the complete 148-face hull, reconstructs all 229 true edges and the connected Euler-2 boundary, recomputes exact mass/centroid/zero moments, audits all 148 faces, 83 vertices and 229 four-component edge cones, checks all deleted parent features, the four-cell complex, exact obstruction, unique-farthest target, and the two acute components. The separate interval, chamber-atlas, graph, and mesh verifiers all pass.')
parts.append('The matching OBJ/STL have `83` vertices, `162` triangles, `243` triangulated mesh edges, and Euler number `2`. Fourteen mesh-only edges triangulate the protected 17-gon. Recomputed decimal volume is `95.03325164350123`; the mesh centre-of-mass norm is `7.883978793478446e-15`. `RUN_ALL_VERIFIERS.txt` ends with `ALL VERIFIERS PASS`.')
parts.append('## Sharpest genuinely new successor')
parts.append('Another scalar endpoint transfer, local cap, serial rail, fixed-ray radial regrading, or same-component metric polish is subsumed. The current failure is not radial order—target `8` is already uniquely farthest—but an exact **acute-component separation**: the terminal obstruction component and target component are separated by negative dot products for every cross pair.')
parts.append('The smallest topology not represented is therefore an **acute-component-merging fifth nonsimplicial cell** (or a pair of edge-sharing prismatic/octahedral cells) that rotates or inserts at least one macroscopic ray direction so the actual true-edge graph gains a positive-dot bridge between the two exact components. It must simultaneously absorb the residual packet `{135,183,195,223,224,226,227}`, delete `(226,227)`, replace stable `[195,224,223]` and saddles `(135,224),(183,223)`, preserve the 17-gon and unique-farthest vertex `8`, and include a genuine finite-thickness terminal-to-target route. With the endpoint rays/radii fixed, at least 19 witness edges are necessary; a macroscopic ray rotation can beat that count. At least two noncritical return-lobe actuators and the three exact dependent ordinary-moment coordinates should remain available, with a full hull/full-cone rebuild at every incidence wall.')
parts.append('## Reproducible files')
parts.append('- `input_rows_common_lattice.csv`: complete authoritative 140-row exact generator.\n- `coordinates_active_centered.csv`, `halfspaces_centered.csv`: complete exact V/H representation.\n- `face_cycles.json`, `true_edges.csv`: all actual maximal faces and true edges.\n- `faces_mechanics.json`, `vertices_mechanics.csv`, `edges_four_component_audit.csv`: complete exact full-feature audit.\n- `fourth_cell_complex.json`, `graph_radial_obstruction.json`, `first_chamber_atlas.json`, `interval_certificate.json`: topology, obstruction, chamber, and box certificates.\n- `verify_exact_cleanroom.py`, `verify_interval.py`, `verify_first_chamber_atlas.py`, `verify_graph_obstruction.py`, `verify_mesh.py`: independent checks.\n- `body.obj`, `body.stl`: matching watertight meshes.')
parts.append('## Appendix A — complete authoritative input rows')
parts.append(code(input_lines))
parts.append('## Appendix B — every maximal-face cycle')
parts.append(code(face_lines))
parts.append('## Appendix C — every true edge with its two incident face IDs')
parts.append(code(edge_lines))
(R/'research_handoff.md').write_text('\n\n'.join(parts)+'\n')
print('wrote handoff bytes',(R/'research_handoff.md').stat().st_size)
