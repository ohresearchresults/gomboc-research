"""Exact own-mass incidence labels, whole radial/polar basins and arithmetic costs."""
import json,sys,math
from fractions import Fraction as F
from pathlib import Path
from endpoint import dot,cross,det,inverse,mv,dump
sys.set_int_max_str_digits(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def bits(seq):
 seq=list(map(F,seq));return [max(abs(v.numerator).bit_length() for v in seq),max(v.denominator.bit_length() for v in seq)]
def bracket(x,D=10**12):
 x=F(x);n=x.numerator*D//x.denominator
 return {'lower_numerator':n,'upper_numerator':n+1,'denominator':D,'strict':F(n,D)<x<F(n+1,D)}
def reach(graph,root):
 reverse=[[] for _ in graph]
 for i,row in enumerate(graph):
  for j in row:reverse[j].append(i)
 seen={root};queue=[root]
 while queue:
  i=queue.pop()
  for j in reverse[i]:
   if j not in seen:seen.add(j);queue.append(j)
 return seen

def run(out):
 a=json.loads((out/'A.json').read_text());assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
 par=json.loads((out/'INPUT.json').read_text());D=par['D'];t=tuple(F(v,D) for v in par['t']);A=[[F(v,D) for v in row] for row in par['A']];inv=inverse(A)
 labels=json.loads((out/'LABELS.json').read_text());X=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));volume=F(a['ordinary_volume']);moment=tuple(map(F,a['raw_first_moments']));assert moment==mul(volume,g)
 b=mv(inv,g);delta=1-dot(t,b);assert delta>0;c=mul(1/delta,b)
 back=[]
 for x in X:
  y=mv(inv,x);d=1-dot(t,y);assert d>0;back.append(mul(1/d,y))
 order=sorted(range(len(back)),key=lambda i:back[i]);parent_of={j:i for i,j in enumerate(order)}
 apex=95 if par['delete']==99 else 93
 assert back[order[apex]]==(0,0,1)
 C=math.lcm(*(v.denominator for v in g));M=tuple(int(C*v) for v in g);bs=[math.lcm(*(v.denominator for v in x)) for x in X]
 aa=[tuple(int(v*d) for v in x) for x,d in zip(X,bs)];Z=[sub(mul(C,x),mul(d,M)) for x,d in zip(aa,bs)]
 def e(i,j):return sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]))
 graph=[[] for _ in X]
 for i,j in a['edges']:
  ed=e(i,j)
  if dot(Z[i],ed)>0:graph[i].append(j)
  if dot(Z[j],ed)<0:graph[j].append(i)
 norms=[dot(x,x) for x in Z];root=0
 for i in range(1,len(X)):
  if norms[i]*bs[root]**2>norms[root]*bs[i]**2:root=i
 assert root in a['unstable_vertices'];good=reach(graph,root);bad=set(range(len(X)))-good;assert all(set(graph[i])<=bad for i in bad)
 edgefaces={}
 for fi,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces.setdefault(tuple(sorted((i,j))),[]).append(fi)
 N=[tuple(n) for n in a['normals']];h=a['offsets'];hh=[v*C-dot(n,M) for n,v in zip(N,h)];assert min(hh)>0
 pgraph=[[] for _ in N]
 for fs in edgefaces.values():
  assert len(fs)==2;i,j=fs
  if hh[i]*dot(N[i],N[j])-hh[j]*dot(N[i],N[i])>0:pgraph[i].append(j)
  if hh[j]*dot(N[j],N[i])-hh[i]*dot(N[j],N[j])>0:pgraph[j].append(i)
 proot=0
 for i in range(1,len(N)):
  if dot(N[i],N[i])*hh[proot]**2>dot(N[proot],N[proot])*hh[i]**2:proot=i
 assert proot in a['stable_face_ids'];pgood=reach(pgraph,proot);pbad=set(range(len(N)))-pgood;assert all(set(pgraph[i])<=pbad for i in pbad)
 centred=[sub(x,g) for x in X];barriers=[]
 for i,j in a['saddle_edges']:
  ed=sub(X[j],X[i]);p=centred[i];h2=dot(p,p)-dot(p,ed)**2/dot(ed,ed)
  assert h2>0
  rec={'base_edge':sorted([parent_of[i],parent_of[j]]),'original_owner_facets':[labels[k] for k in edgefaces[tuple(sorted((i,j)))]],'squared_radius':str(h2)}
  if (i in bad)!=(j in bad):
   roots=[k for k in a['unstable_vertices'] if k in bad];assert roots
   rec['unwanted_primal_barriers']={str(parent_of[k]):bracket(1-h2/dot(centred[k],centred[k])) for k in roots}
  fi,fj=edgefaces[tuple(sorted((i,j)))]
  if (fi in pbad)!=(fj in pbad):
   roots=[k for k in a['stable_face_ids'] if k in pbad];assert roots
   rec['unwanted_polar_barriers']={str(labels[k]):bracket(1-F(hh[k]**2,C*C*dot(N[k],N[k]))/h2) for k in roots}
  barriers.append(rec)
 admiss=json.loads((out/'ADMISSIBILITY.json').read_text());lower=F(admiss['minimum_denominator']);assert min(1+dot(t,x) for x in back)==lower
 # Pullback of the new physical centroid really is strictly inside the original deleted body.
 from RECONSTRUCT import recover
 source=Path(__file__).resolve().parent;rows=recover(json.loads((source/'BASE_GENERATOR.json').read_text()))['H'];ids=[i for i in range(137) if i!=par['delete']]
 slacks=[F(rows[i][3])-dot(rows[i][:3],c) for i in ids];assert min(slacks)>0
 result=dict(base_vertex_of_new=[parent_of[i] for i in range(len(X))],new_vertex_of_base=order,
  stable_original_facets=[labels[k] for k in a['stable_face_ids']],unstable_base_vertices=[parent_of[i] for i in a['unstable_vertices']],saddles_base_vertices=[sorted([parent_of[i],parent_of[j]]) for i,j in a['saddle_edges']],
  global_primal_root_base=parent_of[root],global_polar_root_original=labels[proot],
  primal_root_reaching_base=sorted(parent_of[i] for i in good),primal_closed_unwanted_base=sorted(parent_of[i] for i in bad),
  primal_boundary_base=[sorted([parent_of[i],parent_of[j]]) for i,j in a['edges'] if (i in bad)!=(j in bad)],
  polar_root_reaching_original=sorted(labels[i] for i in pgood),polar_closed_unwanted_original=sorted(labels[i] for i in pbad),
  polar_boundary_original=[sorted([labels[i],labels[j]]) for i,j in edgefaces.values() if (i in pbad)!=(j in pbad)],
  projective_centroid=list(map(str,b)),centroid_pullback=list(map(str,c)),inverse_centroid_denominator=str(delta),
  projective_volume=str(volume/det(A)),centroid_pullback_in_source_interior=True,denominator_minimum=str(lower),denominator_minimum_bracket=bracket(lower),
  barriers=barriers,arithmetic=dict(H_integer_max_bits=max(abs(v).bit_length() for n in json.loads((out/'raw.json').read_text())['H'] for v in n),raw_vertices=bits(v for x in X for v in x),volume=bits([volume]),raw_first_moments=bits(moment),centroid=bits(g),centred_vertices=bits(v for x in centred for v in x)))
 dump(out/'DETAILS.json',result);print('EXACT_ALL_BASINS_LABELS_AND_PULLBACK_PASS',par['delete'],len(bad),len(pbad),flush=True)
 return result
if __name__=='__main__':run(Path(sys.argv[1]))
