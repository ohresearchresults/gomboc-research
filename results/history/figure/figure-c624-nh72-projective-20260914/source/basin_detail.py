"""Exact whole-basin turnover, using each body's actual own volume centroid."""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
from exact_orbit import dot,sub,add,mul,cross,det,matvec,data,dump
sys.set_int_max_str_digits(0)

def graph_at(X,g,edges):
 C=math.lcm(*(v.denominator for v in g));M=tuple(int(C*v) for v in g);bs=[math.lcm(*(v.denominator for v in x)) for x in X];aa=[tuple(int(b*v) for v in x) for x,b in zip(X,bs)];zz=[sub(mul(C,a),mul(b,M)) for a,b in zip(aa,bs)];graph=[[] for _ in X]
 for i,j in edges:
  e=sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]))
  if dot(zz[i],e)>0:graph[i].append(j)
  if dot(zz[j],e)<0:graph[j].append(i)
 roots=[i for i,z in enumerate(graph) if not z];rr=[dot(z,z) for z in zz];root=roots[0]
 for i in roots[1:]:
  if rr[i]*bs[root]**2>rr[root]*bs[i]**2:root=i
 return graph,roots,root

def reaching(graph,root):
 seen={root}
 while True:
  new=seen|{i for i,g in enumerate(graph) if set(g)&seen}
  if new==seen:return seen
  seen=new

def path(graph,start,end):
 prev={start:None};queue=[start]
 for i in queue:
  if i==end:break
  for j in sorted(graph[i]):
   if j not in prev:prev[j]=i;queue.append(j)
 if end not in prev:return None
 ans=[];v=end
 while v is not None:ans.append(v);v=prev[v]
 return ans[::-1]

def interval(v,D=10**12):
 k=v.numerator*D//v.denominator
 assert F(k,D)<v<F(k+1,D)
 return [k,k+1,D]

def run(source,which,out):
 raw,par,t,A,inv,alpha,lower=data(source,which);a=json.loads((out/'A.json').read_text());extra=json.loads((out/'EXTRA.json').read_text());X=[tuple(map(F,r)) for r in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));E=a['edges'];faces=a['faces'];new_of=extra['new_index_of_parent'];parent_of=extra['parent_index_of_new'];Y=[matvec(inv,x) for x in X];back=[mul(1/(1-dot(t,y)),y) for y in Y]
 # Reintegrate the inverse physical solid, using the inherited maximal faces.
 V0=F(0);M0=(F(0),)*3
 for cy in faces:
  for j in range(1,len(cy)-1):
   p,q,r=(back[k] for k in (cy[0],cy[j],cy[j+1]));v=det([p,q,r])/6;assert v>0;V0+=v;M0=add(M0,mul(v/4,add(add(p,q),r)))
 g0=mul(1/V0,M0);parentX=[back[i] for i in new_of];parentE=[sorted([parent_of[i],parent_of[j]]) for i,j in E];basegraph,baseroots,baseroot=graph_at(parentX,g0,parentE);basegood=reaching(basegraph,baseroot);basebad=set(range(177))-basegood
 assert baseroots==[96,163] and baseroot==96 and len(basegood)==18 and len(basebad)==159
 known=[166,167,169,171,174,176,175,173,172,170,168,165,164,161,158,156,102,96]
 assert basegood==set(known) and all(j in basegraph[i] for i,j in zip(known,known[1:]))
 newgraph,newroots,newroot=graph_at(X,g,E);newgood=reaching(newgraph,newroot);newbad=set(range(177))-newgood;goodlabels={parent_of[i] for i in newgood};badlabels={parent_of[i] for i in newbad}
 if which=='FAR':
  assert badlabels=={156,158,161,164,165,166,167,168,169,170,171,172,173,174,175,176}
  assert basebad<=goodlabels and goodlabels==basebad|{96,102}
 # Polar graph uses the SAME physical centroid, never polar-volume centring.
 N=[tuple(row) for row in a['normals']];h=a['offsets'];C=math.lcm(*(v.denominator for v in g));M=tuple(int(C*v) for v in g);ds=[hh*C-dot(n,M) for n,hh in zip(N,h)];assert min(ds)>0
 owners={}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
 dg=[[] for _ in N]
 for e,(i,j) in sorted(owners.items()):
  c=dot(N[i],N[j])
  if ds[i]*c-ds[j]*dot(N[i],N[i])>0:dg[i].append(j)
  if ds[j]*c-ds[i]*dot(N[j],N[j])>0:dg[j].append(i)
 dr=[i for i,v in enumerate(dg) if not v];assert dr==a['stable_face_ids'];droot=dr[0]
 for i in dr[1:]:
  if dot(N[i],N[i])*ds[droot]**2>dot(N[droot],N[droot])*ds[i]**2:droot=i
 dgood=reaching(dg,droot);dbad=set(range(137))-dgood
 assert all(set(dg[i])<=dbad for i in dbad)
 # Every reported saddle below lies across the indicated actual-edge basin cut.
 u=next(i for i in newroots if i!=newroot);uu=dot(sub(X[u],g),sub(X[u],g));barriers=[]
 dother=next(i for i in dr if i!=droot);fd=F(ds[dother],C)**2/dot(N[dother],N[dother]);polarbarriers=[]
 for i,j in a['saddle_edges']:
  p=sub(X[i],g);e=sub(X[j],X[i]);foot=sub(p,mul(dot(p,e)/dot(e,e),e));hh=dot(foot,foot)
  if (i in newbad)!=(j in newbad):
   b=1-hh/uu;assert b>0;barriers.append(dict(edge_parent_labels=[parent_of[i],parent_of[j]],relative_squared_barrier=b,strict_interval=interval(b)))
  f,k=owners[tuple(sorted((i,j)))]
  if (f in dbad)!=(k in dbad):
   b=1-fd/hh;assert b>0;polarbarriers.append(dict(supports=[f,k],relative_squared_barrier=b,strict_interval=interval(b)))
 q=[tuple(F(v,r[3]) for v in r[:3]) for r in raw['H']];maxl=max(sum(map(abs,n)) for n in q);assert maxl<5
 output=dict(parent_volume=V0,parent_centroid=g0,parent_root_reaching=sorted(basegood),
  old_unwanted_reaching_new_global_root=sorted(basebad&goodlabels),old_unwanted_not_reaching_new_global_root=sorted(basebad-goodlabels),
  new_unwanted_formerly_parent_good=sorted(badlabels&basegood),new_global_root_parent_label=parent_of[newroot],
  exact_positive_path_from_parent163_to_new_root=[parent_of[i] for i in path(newgraph,new_of[163],newroot)] if path(newgraph,new_of[163],newroot) else None,
  polar_roots=dr,polar_global_root=droot,polar_root_reaching=sorted(dgood),polar_closed_unwanted=sorted(dbad),
  polar_boundary_support_pairs=sorted([list(pair) for pair in owners.values() if (pair[0] in dbad)!=(pair[1] in dbad)]),
  primal_barriers=barriers,polar_barriers=polarbarriers,
  max_parent_normal_L1=maxl,cube_halfside=F(1,5),universal_projective_cube_halfside=F(1,10))
 dump(out/'DETAIL.json',output)
 print('EXACT_PRIMAL_POLAR_WHOLE_BASIN_TURNOVER_PASS',which,len(basebad&goodlabels),len(newbad),len(dbad),flush=True)
if __name__=='__main__':run(Path(sys.argv[1]).resolve(),sys.argv[2],Path(sys.argv[3]).resolve())
