"""Exact graph/energy exclusion of an entire movable ten-vertex disk.
This is conditional on the stated retained adjacency, anchors, three apex
supports and actual own centroid/physical metric region. It does not forbid
other contact graphs, moved anchors, centres or metrics.
"""
import sys,json,math
from fractions import Fraction as Q
from pathlib import Path
import BUILD as B
sys.set_int_max_str_digits(0)
DISK=[106,109,112,114,117,120,124,146,148,149]
LOW=[69,99,115,118,123]
START=111;END=150;APEX=95

def run(base):
 P,keep,faces,labels,_=B.setup(base,'PAIR99');c=tuple(map(Q,base['raw_centroid']))
 X=[B.sub(p,c) for p in P];J=set(DISK);E=sorted({tuple(sorted((i,j))) for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])})
 adj={i:[] for i in keep}
 for i,j in E:adj[i].append(j);adj[j].append(i)
 boundary=sorted({j for i in J for j in adj[i] if j not in J})
 assert boundary==[69,99,111,115,118,123,150]
 assert sorted(adj[START])==[69,107,114]
 corridor=J|{START,END};paths=[]
 def dfs(p):
  if p[-1]==END:paths.append(p);return
  for j in sorted(adj[p[-1]]):
   if j in corridor and j not in p:dfs(p+[j])
 dfs([START]);longest=max(paths,key=lambda p:(len(p),p));n=max(len(p)-1 for p in paths)
 assert n==10
 d=B.sub(P[END],P[START]);distance2=B.dot(d,d);delta=B.dot(X[END],X[END])-B.dot(X[START],X[START]);assert delta>0
 ratio=distance2/delta;assert 11<ratio<12
 energy=distance2-n*delta;assert energy>0
 l1=lambda v:sum(map(abs,v))
 radii=[energy/(4*n*l1(d))]
 anchors=[]
 for j in LOW:
  gap=B.dot(X[START],X[START])-B.dot(X[j],X[j]);assert gap>0
  r=gap/(4*l1(B.sub(P[START],P[j])));radii.append(r);anchors.append(dict(vertex=j,squared_radius_gap=str(gap),centre_radius=str(r)))
 exits=[]
 for j in [69,107]:
  e=B.sub(P[j],P[START]);v=B.dot(X[START],e);assert v<0;r=-v/(2*l1(e));radii.append(r);exits.append(dict(neighbor=j,arrow=str(v),centre_radius=str(r)))
 normals=[]
 for label in [0,2,35]:
  cy=faces[labels.index(label)];a,b,cc=[P[i] for i in cy[:3]];normal=B.cross(B.sub(b,a),B.sub(cc,a));h=B.dot(normal,a);normals.append(B.mul(1/h,normal))
 N=list(map(list,zip(*normals)));inverse=B.inverse(N);lam=[B.dot(row,X[APEX]) for row in inverse]
 assert all(v>0 for v in lam)
 for v,row in zip(lam,inverse):radii.append(v/(2*l1(row)))
 rho=min(radii);assert Q(615129628,10**12)<rho<Q(615129629,10**12)
 # The unchanged graph admits only10 links, but ANY replacement with at most
 # ten interior vertices admits at most11 links. Both are shorter than required.
 rho11=(distance2-11*delta)/(44*l1(d));assert rho11>0
 rho11=min([rho11]+radii[1:])
 joint_regions=[]
 for link_bound,rc,gamma in [(10,Q(1,100000),Q(1,1000)),(11,Q(1,1000000),Q(1,10000))]:
  assert 3*gamma<1
  joint=[]
  for j in [69,107]:
   e=B.sub(P[j],P[START]);v=B.dot(X[START],e)
   err=(rc+gamma*(l1(X[START])+3*rc))*l1(e)
   assert -v>err;joint.append(dict(kind='first_exit',index=j,reserve=str(-v-err)))
  for j in LOW:
   dd=B.sub(P[START],P[j]);ss=B.add(X[START],X[j]);v=B.dot(dd,ss)
   err=l1(dd)*(2*rc+gamma*(l1(ss)+6*rc));assert v>err
   joint.append(dict(kind='low_anchor_radius',index=j,reserve=str(v-err)))
  ss=B.sub(d,B.mul(link_bound,B.add(X[END],X[START])))
  deficit=distance2-link_bound*delta
  err=l1(d)*(2*link_bound*rc+gamma*(l1(ss)+6*link_bound*rc));assert deficit>err
  joint.append(dict(kind='energy',index=link_bound,reserve=str(deficit-err)))
  for k,(row,v) in enumerate(zip(inverse,lam)):
   err=l1(row)*(rc+gamma*(l1(X[APEX])+3*rc));assert v>err
   joint.append(dict(kind='apex_cone',index=k,reserve=str(v-err)))
  joint_regions.append(dict(max_links=link_bound,entrywise_symmetric_gram_radius=str(gamma),centre_infinity_radius=str(rc),positive_reserves=joint))
 return dict(status='TEN_MOVABLE_VERTICES_EXACT_GRAPH_ENERGY_OBSTRUCTION_PASS',
  source='literal S8, remove support99, then remove K99 vertices129 and145',
  movable_disk=DISK,fixed_entry=START,fixed_exit=END,lower_radius_boundary=LOW,
  boundary=boundary,induced_edges=[list(e) for e in E if e[0] in corridor and e[1] in corridor],
  all_simple_entry_exit_paths=paths,max_path_edges=n,longest_path=longest,
  squared_chord=str(distance2),squared_radius_gain=str(delta),link_lower_ratio=str(ratio),
  minimum_strict_links_at_c0=12,energy_deficit=str(energy),
  Euclidean_centre_radius=str(rho),fixed_anchor_certificates=anchors,fixed_exit_certificates=exits,
  apex=APEX,apex_support_labels=[0,2,35],apex_cone_coefficients=list(map(str,lam)),
  metric_regions=joint_regions,arbitrary_rewiring_max_interior_vertices=10,arbitrary_rewiring_centre_radius=str(rho11),
  arbitrary_rewiring_energy_deficit=str(distance2-11*delta),
  conclusion='At least one additional weak-or-strict unstable vertex in disk union {111}; apex95 stays strict U. Thus strict110/weak000 is impossible under these hypotheses.',
  scope='All ten disk points may move arbitrarily; exterior cap points may move provided boundary anchors, stated adjacency, and the three supporting apex planes persist. The larger radius requires the same graph. The smaller radius permits arbitrary internal rewiring with at most ten interior vertices, the same external anchors/interface, and no new external escape. Actual own centre/metric bounds are required. No global nonexistence claim.')
if __name__=='__main__':
 a=json.loads(Path(sys.argv[1]).read_text());r=run(a);Path(sys.argv[2]).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
 print(r['status'],len(r['all_simple_entry_exit_paths']),r['max_path_edges'],r['minimum_strict_links_at_c0'])
