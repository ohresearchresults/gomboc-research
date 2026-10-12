"""Exact maximal-complex maps, independent centred mass, changes and full basins."""
import json,sys,math
from fractions import Fraction as Q
from pathlib import Path
import BUILD as B,NEW_BUILD,CRITICAL
sys.set_int_max_str_digits(0)
def bits(v):
 v=list(v);return [max(abs(x.numerator).bit_length() for x in v),max(x.denominator.bit_length() for x in v)]
def reach(graph,root):
 s={root}
 while True:
  t=s|{i for i,g in enumerate(graph) if set(g)&s}
  if t==s:return s
  s=t
def canon(c):
 k=c.index(min(c));return c[k:]+c[:k]
def run(base,gen,param,oldparam,a):
 P,keep,faces,labels,d=NEW_BUILD.coordinates(base,gen,param);X=[tuple(map(Q,r)) for r in a['raw_vertices']];lookup={p:i for i,p in enumerate(X)};mp={i:lookup[P[i]] for i in keep};inv={v:k for k,v in mp.items()}
 assert len(mp)==len(X)==173
 for fi,c in enumerate(faces):assert canon([mp[i] for i in c])==a['faces'][fi]
 E={tuple(sorted((i,j))) for c in faces for i,j in zip(c,c[1:]+c[:1])};EE={tuple(sorted((inv[i],inv[j]))) for i,j in a['edges']};assert E==EE
 assert (a['V'],a['E'],a['F'],a['counts'],a['weak'])==(173,309,138,[7,18,23],[0,0,0])
 assert a['active_input_indices']==list(range(138));assert a['face_primitive_zero_count']==a['vertex_max_zero_count']==a['edge_primitive_zero_count']==0
 V=Q(a['ordinary_volume']);M=tuple(map(Q,a['raw_first_moments']));g=tuple(map(Q,a['raw_centroid']));g0=tuple(map(Q,base['raw_centroid']));assert M==B.mul(V,g)
 D=math.lcm(*(v.denominator for x in X for v in x),*(v.denominator for v in g));Z=[tuple(int((x[k]-g[k])*D) for k in range(3)) for x in X];vol6=0;first24=(0,0,0);nt=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for k in range(1,len(cy)-1):
   x,y,z=(Z[i] for i in [cy[0],cy[k],cy[k+1]]);w=B.det(x,y,z);assert w>0;vol6+=w;first24=B.add(first24,B.mul(w,B.add(B.add(x,y),z)));nt+=1
 assert first24==(0,0,0) and Q(vol6,6*D**3)==V
 graph=[[] for x in X];ef={}
 for i,j in a['edges']:
  e=B.sub(Z[j],Z[i])
  if B.dot(Z[i],e)>0:graph[i].append(j)
  if B.dot(Z[j],e)<0:graph[j].append(i)
 for fi,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(fi)
 root=max(range(len(X)),key=lambda i:B.dot(Z[i],Z[i]));R=reach(graph,root);bad=set(range(len(X)))-R;assert all(set(graph[i])<=bad for i in bad)
 C=math.lcm(*(x.denominator for x in g));CG=tuple(int(C*x) for x in g);N=a['normals'];H=[h*C-B.dot(n,CG) for n,h in zip(N,a['offsets'])];assert min(H)>0;polar=[[] for n in N];de=[]
 for i,j in ef.values():
  de.append((i,j));nm=B.dot(N[i],N[j])
  if H[i]*nm>H[j]*B.dot(N[i],N[i]):polar[i].append(j)
  if H[j]*nm>H[i]*B.dot(N[j],N[j]):polar[j].append(i)
 pr=max(range(len(N)),key=lambda i:Q(B.dot(N[i],N[i]),H[i]**2));RR=reach(polar,pr);bb=set(range(len(N)))-RR
 oldP,_,_,_=CRITICAL.points(base,oldparam);oldraw,_=CRITICAL.build(base,oldparam);newraw,_,_=NEW_BUILD.run(base,gen,param)
 changed=[i for i in keep if P[i]!=oldP[i]];changedH=[labels[i] for i,(u,v) in enumerate(zip(oldraw['H'],newraw['H'])) if u!=v]
 u=B.sub(P[111],g);z=B.sub(P[150],g);delta=B.dot(z,z)-B.dot(u,u);d2=B.dot(B.sub(z,u),B.sub(z,u));assert 9*delta<d2<10*delta
 err=max(abs(x-y) for x,y in zip(g,g0));assert err<Q(1,10**11)
 r=dict(status='NEW_INTERFACE_FULL_COMPLEX_OWN_MECHANICS_AND_THIRD_MASS_PASS',identity=param['identity'],VEF=[a['V'],a['E'],a['F']],strict=a['counts'],weak=a['weak'],old_to_new=mp,new_to_old=inv,support_labels=labels,changed_K99_vertices=changed,changed_parent_supports=changedH,stable_supports=[labels[i] for i in a['stable_face_ids']],unstable_K99_vertices=sorted(inv[i] for i in a['unstable_vertices']),saddle_K99_edges=sorted(sorted(inv[i] for i in e) for e in a['saddle_edges']),ordinary_volume=str(V),raw_first_moments=list(map(str,M)),raw_centroid=list(map(str,g)),K99_centroid=list(map(str,g0)),centroid_error_infinity=str(err),filled_centred_first_moments=[0,0,0],positive_tetrahedra=nt,primal_root=inv[root],primal_bad=sorted(inv[i] for i in bad),primal_boundary=[sorted((inv[i],inv[j])) for i,j in a['edges'] if (i in bad)!=(j in bad)],polar_root=labels[pr],polar_bad=[labels[i] for i in sorted(bb)],polar_boundary=[[labels[i],labels[j]] for i,j in de if (i in bb)!=(j in bb)],new_inlet=list(map(str,P[111])),new_outlet=list(map(str,P[150])),endpoint_gap_squared=str(d2),endpoint_radius_squared_increment=str(delta),energy10=str(10*delta-d2),energy9=str(9*delta-d2),arithmetic=dict(H=max(abs(v).bit_length() for row in newraw['H'] for v in row),raw_vertices=bits(v for x in X for v in x),volume=bits([V]),moments=bits(M),centroid=bits(g),centred_vertices=bits(x[k]-g[k] for x in X for k in range(3)),common_denominator=D.bit_length()))
 return r
if __name__=='__main__':
 base,gen,param,oldparam,a,out=map(Path,sys.argv[1:]);r=run(*[json.loads(p.read_text()) for p in [base,gen,param,oldparam,a]]);out.write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
 print(r['status'],r['strict']);print(r['arithmetic']);print('changed',r['changed_K99_vertices']);print('S',r['stable_supports'],'U',r['unstable_K99_vertices'],'H',r['saddle_K99_edges']);print('basins',len(r['primal_bad']),len(r['primal_boundary']),len(r['polar_bad']),len(r['polar_boundary']));print('volume',float(Q(r['ordinary_volume'])),'center',list(map(lambda s:float(Q(s)),r['raw_centroid'])),'error',float(Q(r['centroid_error_infinity'])))
