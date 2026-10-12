#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict, deque
from pathlib import Path
import csv,json,math,sys
import numpy as np
R=Path(__file__).resolve().parent
# Keep the bundle self-contained: the numeric proposer is shipped with the
# sibling fourth-cell endpoint.  The original worker path under /mnt/data is
# intentionally not required in the portable working copy.
sys.path.insert(0,str(R.parent/'fourth_cell_endpoint'))
from numeric_hull_proposer import evaluate
sys.set_int_max_str_digits(0)

def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def qs(x):x=Q(x);return f'{x.numerator}/{x.denominator}'
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def logabsq(x):
 x=Q(x);assert x
 return math.log(abs(x.numerator))-math.log(x.denominator)
def ratio_sqrt(num,den):
 num=Q(num);den=Q(den);assert den>0
 if num==0:return 0.
 return (1 if num>0 else -1)*math.exp(logabsq(num)-.5*logabsq(den))
def mul_sqrt_ratio(num,a,b):
 num=Q(num);a=Q(a);b=Q(b);assert a>0 and b>0
 if num==0:return 0.
 return (1 if num>0 else -1)*math.exp(logabsq(num)+.5*(logabsq(a)-logabsq(b)))

def read_rows():
 rows={};line={};S=None
 for r in csv.DictReader(open(R/'input_rows_common_lattice.csv')):
  i=int(r['source_id']);s=int(r['denominator']);S=s if S is None else S;assert s==S
  rows[i]=tuple(int(r[k]) for k in ('x_int','y_int','z_int'));line[i]=r['lineage']
 return rows,line,S

def exact_faces(rows,S):
 P={i:np.array(rows[i],float)/S for i in rows};rr=evaluate(P,plane_tol=1e-8,qhull_options='Qt Qx',strict_tol=1e-12);assert rr.valid,rr.error
 out=[];seen=set()
 for ff in rr.faces:
  c=list(ff['cycle']);a=rows[c[0]];nn=None
  for j in range(1,len(c)-1):
   for k in range(j+1,len(c)):
    z=cross(sub(rows[c[j]],a),sub(rows[c[k]],a))
    if z!=(0,0,0):nn=z;break
   if nn is not None:break
  assert nn is not None
  h=dot(nn,a);vals={i:dot(nn,p)-h for i,p in rows.items()};pos=any(v>0 for v in vals.values());neg=any(v<0 for v in vals.values());assert not(pos and neg),(c,min(vals.values()),max(vals.values()))
  if pos:nn=tuple(-z for z in nn);h=-h;vals={i:-v for i,v in vals.items()}
  cop=sorted(i for i,v in vals.items() if v==0);assert set(cop)==set(c),(c,cop)
  area=(0,0,0)
  for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
  if dot(area,nn)<0:c=[c[0]]+list(reversed(c[1:]))
  g=gcdall((*nn,h));nn=tuple(z//g for z in nn);h//=g
  key=(*nn,h);assert key not in seen;seen.add(key);out.append({'cycle':c,'n':nn,'h':h})
 out.sort(key=lambda f:(0 if set(f['cycle'])==set(range(17)) else 1,min(f['cycle']),len(f['cycle']),tuple(f['cycle'])))
 return out

def exact_mass(rows,faces,S):
 D6=0;Mint=[0,0,0];tris=[]
 for f in faces:
  c=f['cycle']
  for j in range(1,len(c)-1):
   a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
   for k in range(3):Mint[k]+=d*(a[k]+b[k]+z[k])
   tris.append((c[0],c[j],c[j+1]))
 assert D6>0
 V=Q(D6,6*S**3);M=tuple(Q(Mint[k],24*S**4) for k in range(3));C=tuple(Q(Mint[k],4*D6*S) for k in range(3));assert all(M[k]==V*C[k] for k in range(3))
 return D6,M,V,C,tris

def mechanics(rows,faces,EF,active,C,S):
 X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in rows};N=defaultdict(set)
 for a,b in EF:N[a].add(b);N[b].add(a)
 fa=[];stable=[]
 for fi,f in enumerate(faces):
  n=tuple(Q(z) for z in f['n']);h=Q(f['h'],S)-dot(n,C);assert h>0;foot=mul(n,h/n2(n));c=f['cycle'];raw=[];norm=[];ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3))
  for a,b in zip(c,c[1:]+c[:1]):
   e=sub(X[b],X[a]);z=dot(cross(e,sub(foot,X[a])),n)
   if dot(cross(e,sub(ref,X[a])),n)<0:z=-z
   assert z!=0;raw.append(z);norm.append(ratio_sqrt(z,n2(e)*n2(n)))
  yes=min(raw)>0
  if yes:stable.append(fi)
  fa.append({'face':fi,'cycle':c,'plane_lattice':[f['n'][0],f['n'][1],f['n'][2],f['h']],'h_centered_exact':qs(h),'foot_exact':[qs(z) for z in foot],'components_exact':[qs(z) for z in raw],'components_normalized':norm,'stable':yes,'decision_normalized':min(norm)})
 va=[];SUP={};unstable=[]
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};assert vals and all(v!=0 for v in vals.values());SUP[i]=vals;norm={j:ratio_sqrt(v,n2(X[i])*n2(sub(X[j],X[i]))) for j,v in vals.items()};yes=min(vals.values())>0
  if yes:unstable.append(i)
  va.append({'vertex':i,'unstable':yes,'supports_exact':{str(j):qs(v) for j,v in vals.items()},'supports_normalized':{str(j):z for j,z in norm.items()},'decision_normalized':min(norm.values())})
 ea=[];saddles=[];EC={}
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(z) for z in faces[inc[0]]['n']);n2v=tuple(Q(z) for z in faces[inc[1]]['n']);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);EC[e]=vals;yes=min(vals)>0
  if yes:saddles.append(e)
  norm=[float(t),float(1-t),mul_sqrt_ratio(b1,aa,n2(p)),mul_sqrt_ratio(b2,cc,n2(p))]
  ea.append({'edge':list(e),'incident_faces':inc,'saddle':yes,'components_exact':{'t':qs(t),'one_minus_t':qs(1-t),'beta1':qs(b1),'beta2':qs(b2)},'components_normalized':{'t':norm[0],'one_minus_t':norm[1],'beta1':norm[2],'beta2':norm[3]},'decision_normalized':min(norm)})
 return X,N,SUP,EC,fa,va,ea,stable,unstable,saddles

def cell_for_edge(e,inc,faces,X,name):
 a,b=e;c1=faces[inc[0]]['cycle'];c2=faces[inc[1]]['cycle'];assert len(c1)==len(c2)==3
 u=next(z for z in c1 if z not in e);v=next(z for z in c2 if z not in e);dp=det(X[u],X[a],X[b]);dm=det(X[v],X[a],X[b]);assert dp*dm<0
 t=dp/(dp-dm);p=add(X[u],mul(sub(X[v],X[u]),t));aa=n2(X[a]);bb=dot(X[a],X[b]);cc=n2(X[b]);ra=dot(p,X[a]);rb=dot(p,X[b]);den=aa*cc-bb*bb;la=(ra*cc-rb*bb)/den;lb=(rb*aa-ra*bb)/den;l0=Q(1)-la-lb;assert sub(p,add(mul(X[a],la),mul(X[b],lb)))==(Q(0),Q(0),Q(0))
 return {'name':name,'true_edge':[a,b],'incident_faces':inc,'equator':['own_centroid',a,b],'apices':[u,v],'apex_determinants_exact':[qs(dp),qs(dm)],'segment_parameter_exact':qs(t),'equator_barycentric_exact':[qs(l0),qs(la),qs(lb)],'strict_convex_bipyramid':min(t,1-t,l0,la,lb)>0,'minimum_barycentric_decimal':float(min(t,1-t,l0,la,lb))}

def build():
 rows,line,S=read_rows();faces=exact_faces(rows,S);cycles=[f['cycle'] for f in faces];EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for a,b in zip(c,c[1:]+c[:1]):EF[tuple(sorted((a,b)))].append(fi)
 assert all(len(v)==2 for v in EF.values());active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active));assert len(active)-len(EF)+len(faces)==2
 D6,M,V,C,tris=exact_mass(rows,faces,S);X,N,SUP,EC,fa,va,ea,stable,unstable,saddles=mechanics(rows,faces,EF,active,C,S)
 assert len(rows)==119 and (len(active),len(EF),len(faces))==(61,163,104);assert [len(stable),len(unstable),len(saddles)]==[2,1,1];assert unstable==[8] and saddles==[(229,247)]
 assert {frozenset(cycles[i]) for i in stable}=={frozenset(range(17)),frozenset({198,224,258})}
 # topology gaps
 topo=[];ing=[]
 for f in faces:
  nn=Q(sum(z*z for z in f['n']));cs=set(f['cycle'])
  for i,p in rows.items():
   if i not in cs:
    z=Q(f['h']-dot(f['n'],p),S);assert z>0;g=ratio_sqrt(z,nn);topo.append(g)
    if i in inactive:ing.append(g)
 # bridge paths and exact directed support
 short=[228]+list(range(229,247))+[8];long=[228]+list(range(247,265))+[8]
 railrecs=[]
 for name,path in [('short_east_rail',short),('long_west_rail',long)]:
  steps=[]
  for a,b in zip(path,path[1:]):
   e=tuple(sorted((a,b)));assert e in EF;d=dot(X[a],sub(X[b],X[a]));assert d>0;pd=dot(X[a],X[b]);assert pd>0
   steps.append({'from':a,'to':b,'true_edge':True,'directed_support_exact':qs(d),'positive_dot_exact':qs(pd),'directed_support_decimal':float(d),'angle_degrees':math.degrees(math.acos(max(-1,min(1,ratio_sqrt(pd,n2(X[a])*n2(X[b]))))))})
  railrecs.append({'name':name,'path':path,'edges':len(path)-1,'steps':steps,'minimum_directed_support_exact':qs(min(Q(z['directed_support_exact']) for z in steps)),'minimum_directed_support_decimal':min(z['directed_support_decimal'] for z in steps),'maximum_step_angle_degrees':max(z['angle_degrees'] for z in steps)})
 # positive-dot graph exact
 G={i:set() for i in active};pos=[];non=[]
 for a,b in EF:
  z=dot(X[a],X[b]);(pos if z>0 else non).append((a,b,z))
  if z>0:G[a].add(b);G[b].add(a)
 seen={min(active)};q=[min(active)]
 while q:
  a=q.pop()
  for b in G[a]:
   if b not in seen:seen.add(b);q.append(b)
 assert seen==set(active)
 # principal two seam bipyramids and full exact convex edge-cell atlas
 start=cell_for_edge((229,247),EF[(229,247)],faces,X,'start shared-interior-edge bipyramid');terminal=cell_for_edge((246,263),EF[(246,263)],faces,X,'terminal shared-interior-edge bipyramid');assert start['strict_convex_bipyramid'] and terminal['strict_convex_bipyramid']
 atlas=[]
 for e,inc in sorted(EF.items()):
  if len(cycles[inc[0]])!=3 or len(cycles[inc[1]])!=3:continue
  z=cell_for_edge(e,inc,faces,X,f'edge-star {e[0]}-{e[1]}')
  if z['strict_convex_bipyramid']:atlas.append(z)
 assert len(atlas)==64
 new=set(range(229,265));newatlas=[z for z in atlas if set(z['true_edge'])&new];assert len(newatlas)==58
 closure=[fi for fi,c in enumerate(cycles) if set(c)&new];ced=defaultdict(list);cd=[]
 for fi in closure:
  c=cycles[fi];assert len(c)==3;z=det(X[c[0]],X[c[1]],X[c[2]]);assert z!=0;cd.append(abs(z))
  for a,b in zip(c,c[1:]+c[:1]):ced[tuple(sorted((a,b)))].append(fi)
 adj=defaultdict(set)
 for fs in ced.values():
  for a in fs:
   for b in fs:
    if a!=b:adj[a].add(b)
 seenf={closure[0]};q=[closure[0]]
 while q:
  a=q.pop()
  for b in adj[a]:
   if b not in seenf:seenf.add(b);q.append(b)
 assert seenf==set(closure)
 complexrec={'version':1,'type':'two-rail acute-component-merging finite-thickness replacement with two principal shared-interior-edge triangular bipyramids and an exact 64-cell edge-star atlas','new_rows':sorted(new),'short_rail':railrecs[0],'long_rail':railrecs[1],'principal_cells':[start,terminal],'all_strict_convex_edge_star_bipyramids':atlas,'new_row_touching_bipyramids':len(newatlas),'closure_face_ids':closure,'closure_faces':len(closure),'closure_connected':True,'minimum_closure_tetra_determinant_exact':qs(min(cd)),'minimum_closure_tetra_determinant_decimal':float(min(cd)),'positive_dot_graph_connected':True,'positive_dot_true_edges':len(pos),'nonpositive_dot_true_edges':len(non)}
 # residual packet graph
 residual={'protected_stable_face':list(range(17)),'protected_unstable_vertex':8,'extra_stable_face':[198,224,258],'sole_saddle_edge':[229,247],'extra_unstable_vertices':[],'old_fourth_packet_rows_now_inactive':[135,183,195,223,225,226,227],'deleted_fourth_features':{'stable_face_195_223_224':not any(set(c)=={195,223,224} for c in cycles),'saddle_135_224':(135,224) not in EF,'saddle_183_223':(183,223) not in EF,'external_positive_edge_226_227':(226,227) not in EF},'incidence_bridge':{'stable_face_to_saddle_graph_distance':1,'bridge_vertex':224,'adjacent_saddle_face':[224,229,247],'limiting_stable_boundary_edge':[198,224]},'interpretation':'The fourth-cell U-H branch is closed by both monotone rails; the acute graph becomes connected and only one S-H packet remains. The extra stable face and saddle are one incidence-star step apart but not incident to the same true edge.'}
 # normalized minima
 sf=[z['decision_normalized'] for z in fa if z['stable']];nf=[-z['decision_normalized'] for z in fa if not z['stable']];uv=[z['decision_normalized'] for z in va if z['unstable']];nv=[-z['decision_normalized'] for z in va if not z['unstable']];sh=[z['decision_normalized'] for z in ea if z['saddle']];nh=[-z['decision_normalized'] for z in ea if not z['saddle']]
 cert={'version':1,'verdict':'NONWINNER — exact M42 acute-component-merging double-rail fifth-cell endpoint is strict own-centroid (2,1,1).','scale':S,'input_rows':len(rows),'active_rows':active,'inactive_rows':inactive,'f_vector':[len(active),len(EF),len(faces)],'complexity':len(active)+len(EF)+len(faces)-2,'euler':len(active)-len(EF)+len(faces),'volume_exact':qs(V),'volume_decimal':float(V),'first_moments_unshifted_exact':[qs(z) for z in M],'centroid_unshifted_exact':[qs(z) for z in C],'centroid_unshifted_decimal':[float(z) for z in C],'dependent_translation_exact':[qs(-z) for z in C],'centered_first_moments_exact':['0/1']*3,'class':[2,1,1],'stable_faces':[{'face':i,'cycle':cycles[i],'decision_normalized':fa[i]['decision_normalized']} for i in stable],'unstable_vertices':[{'vertex':i,'decision_normalized':next(z['decision_normalized'] for z in va if z['vertex']==i)} for i in unstable],'saddle_edges':[{'edge':list(e),'decision_normalized':next(z['decision_normalized'] for z in ea if z['edge']==list(e))} for e in saddles],'margins':{'stable_positive_min':min(sf),'nonstable_exclusion_min':min(nf),'unstable_positive_min':min(uv),'nonunstable_exclusion_min':min(nv),'saddle_positive_min':min(sh),'nonsaddle_exclusion_min':min(nh),'active_topology_distance_min':min(topo),'inactive_distance_min':min(ing)},'acute_bridge':{'positive_dot_graph_connected':True,'short_rail_edges':19,'long_rail_edges':19,'positive_dot_true_edges':len(pos),'nonpositive_dot_true_edges':len(non)},'predecessor_feature_deletions':residual['deleted_fourth_features'],'old_fourth_packet_rows_now_inactive':residual['old_fourth_packet_rows_now_inactive'],'residual_packet':residual}
 # outputs
 with open(R/'coordinates_all_exact.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_int','y_int','z_int','denominator','x_exact','y_exact','z_exact','active','lineage'])
  for i in sorted(rows):w.writerow([i,*rows[i],S,*[qs(Q(z,S)) for z in rows[i]],int(i in active),line[i]])
 with open(R/'coordinates_active_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_exact','y_exact','z_exact','x_decimal','y_decimal','z_decimal','radius_squared_exact','radius_squared_decimal'])
  for i in active:w.writerow([i,*[qs(z) for z in X[i]],*[float(z) for z in X[i]],qs(n2(X[i])),float(n2(X[i]))])
 with open(R/'halfspaces_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['face','nx','ny','nz','h_lattice','h_centered_exact','cycle'])
  for fi,z in enumerate(faces):w.writerow([fi,*z['n'],z['h'],fa[fi]['h_centered_exact'],' '.join(map(str,z['cycle']))])
 json.dump(cycles,open(R/'face_cycles.json','w'),indent=2);json.dump(fa,open(R/'faces_mechanics.json','w'),indent=2)
 with open(R/'true_edges.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_faces'])
  for e in sorted(EF):w.writerow([*e,' '.join(map(str,EF[e]))])
 with open(R/'vertices_mechanics.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['vertex','unstable','decision_normalized','supports_exact_json','supports_normalized_json'])
  for z in va:w.writerow([z['vertex'],int(z['unstable']),repr(z['decision_normalized']),json.dumps(z['supports_exact'],separators=(',',':')),json.dumps(z['supports_normalized'],separators=(',',':'))])
 with open(R/'edges_four_component_audit.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_faces','saddle','t_exact','one_minus_t_exact','beta1_exact','beta2_exact','t_normalized','one_minus_t_normalized','beta1_normalized','beta2_normalized','decision_normalized'])
  for z in ea:
   ce=z['components_exact'];cn=z['components_normalized'];w.writerow([*z['edge'],' '.join(map(str,z['incident_faces'])),int(z['saddle']),ce['t'],ce['one_minus_t'],ce['beta1'],ce['beta2'],cn['t'],cn['one_minus_t'],cn['beta1'],cn['beta2'],z['decision_normalized']])
 json.dump(complexrec,open(R/'fifth_cell_complex.json','w'),indent=2);json.dump({'version':1,'connected':True,'vertices':active,'positive_dot_true_edges':[{'edge':[a,b],'dot_exact':qs(z)} for a,b,z in pos],'nonpositive_dot_true_edges':[{'edge':[a,b],'dot_exact':qs(z)} for a,b,z in non],'short_rail':railrecs[0],'long_rail':railrecs[1]},open(R/'acute_bridge_graph.json','w'),indent=2);json.dump(residual,open(R/'residual_packet_graph.json','w'),indent=2);json.dump(cert,open(R/'certificate.json','w'),indent=2)
 print('PASS exact fifth endpoint',len(rows),len(active),len(EF),len(faces),'class',cert['class']);print('V',qs(V));print('C',*[qs(z) for z in C]);print('margins',cert['margins']);print('cells',len(atlas),len(newatlas),'closure',len(closure));print('rails',railrecs[0]['minimum_directed_support_decimal'],railrecs[1]['minimum_directed_support_decimal'])
if __name__=='__main__':build()
