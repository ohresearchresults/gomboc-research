#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import csv,json,math,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from numeric_hull_proposer import evaluate
sys.set_int_max_str_digits(0)

def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def qs(x):return f'{x.numerator}/{x.denominator}'
def dec(x):return format(float(x),'.18g')
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def logabsq(x):
 x=Q(x);assert x!=0
 return math.log(abs(x.numerator))-math.log(x.denominator)
def ratio_sqrt(num,den):
 num=Q(num);den=Q(den);assert den>0
 if num==0:return 0.0
 return (1.0 if num>0 else -1.0)*math.exp(logabsq(num)-.5*logabsq(den))
def mul_sqrt_ratio(num,a,b):
 num=Q(num);a=Q(a);b=Q(b);assert a>0 and b>0
 if num==0:return 0.0
 return (1.0 if num>0 else -1.0)*math.exp(logabsq(num)+.5*(logabsq(a)-logabsq(b)))

def read_rows():
 rows={};line={};S=None
 with open(ROOT/'input_rows_common_lattice.csv') as f:
  for r in csv.DictReader(f):
   s=int(r['denominator']);S=s if S is None else S;assert s==S
   i=int(r['source_id']);rows[i]=(int(r['x_int']),int(r['y_int']),int(r['z_int']));line[i]=r['lineage']
 return rows,line,S

def exact_faces(rows,S):
 P={i:np.array([z/S for z in p],float) for i,p in rows.items()}
 rr=evaluate(P,plane_tol=1e-9,strict_tol=1e-12);assert rr.valid,rr.error
 out=[];seen=set()
 for ff in rr.faces:
  c=list(ff['cycle']);a=rows[c[0]];nn=None
  for j in range(1,len(c)-1):
   for k in range(j+1,len(c)):
    z=cross(sub(rows[c[j]],a),sub(rows[c[k]],a))
    if z!=(0,0,0):nn=z;break
   if nn is not None:break
  assert nn is not None,c
  h=dot(nn,a);vals={i:dot(nn,p)-h for i,p in rows.items()}
  pos=any(v>0 for v in vals.values());neg=any(v<0 for v in vals.values());assert not(pos and neg),(c,min(vals.values()),max(vals.values()))
  if pos:nn=tuple(-z for z in nn);h=-h;vals={i:-v for i,v in vals.items()}
  cop=sorted(i for i,v in vals.items() if v==0);assert set(cop)==set(c),(c,cop)
  area=(0,0,0)
  for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
  if dot(area,nn)<0:c=[c[0]]+list(reversed(c[1:]))
  g=gcdall((*nn,h));nn=tuple(z//g for z in nn);h//=g
  key=(*nn,h);assert key not in seen;seen.add(key)
  out.append({'cycle':c,'n':nn,'h':h})
 out.sort(key=lambda f:(0 if set(f['cycle'])==set(range(17)) else 1,min(f['cycle']),len(f['cycle']),tuple(f['cycle'])))
 return out

def exact_mass(rows,faces,S):
 D6=0;M24=[0,0,0];tris=[]
 for f in faces:
  c=f['cycle']
  for j in range(1,len(c)-1):
   a,b,z=rows[c[0]],rows[c[j]],rows[c[j+1]];d=det(a,b,z);D6+=d
   for k in range(3):M24[k]+=d*(a[k]+b[k]+z[k])
   tris.append((c[0],c[j],c[j+1]))
 assert D6>0
 V=Q(D6,6*S**3);M=tuple(Q(z,24*S**4) for z in M24);C=tuple(Q(z,4*D6*S) for z in M24)
 assert tuple(M[k]-V*C[k] for k in range(3))==(Q(0),Q(0),Q(0))
 return D6,M,V,C,tris

def mechanics(rows,faces,EF,active,C,S):
 X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in rows}
 N=defaultdict(set)
 for a,b in EF:N[a].add(b);N[b].add(a)
 face_a=[];stable=[]
 for fi,f in enumerate(faces):
  n=tuple(Q(z) for z in f['n']);hc=Q(f['h'],S)-dot(n,C);assert hc>0
  foot=mul(n,hc/n2(n));c=f['cycle'];raw=[];norm=[]
  for a,b in zip(c,c[1:]+c[:1]):
   e=sub(X[b],X[a]);z=dot(cross(e,sub(foot,X[a])),n);assert z!=0,(fi,a,b)
   raw.append(z);norm.append(ratio_sqrt(z,n2(e)*n2(n)))
  iss=min(raw)>0
  if iss:stable.append(fi)
  face_a.append({'face':fi,'cycle':c,'plane_lattice':[f['n'][0],f['n'][1],f['n'][2],f['h']], 'h_centered_exact':qs(hc),'foot_exact':[qs(z) for z in foot], 'components_exact':[qs(z) for z in raw],'components_normalized':norm,'stable':iss,'decision_normalized':min(norm)})
 support={};vert_a=[];unst=[]
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};assert vals and all(v!=0 for v in vals.values())
  support[i]=vals;norm={j:ratio_sqrt(v,n2(X[i])*n2(sub(X[j],X[i]))) for j,v in vals.items()};isu=min(vals.values())>0
  if isu:unst.append(i)
  vert_a.append({'vertex':i,'unstable':isu,'supports_exact':{str(j):qs(v) for j,v in vals.items()},'supports_normalized':{str(j):v for j,v in norm.items()},'decision_normalized':min(norm.values())})
 edge_a=[];sadd=[]
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(z) for z in faces[inc[0]]['n']);n2v=tuple(Q(z) for z in faces[inc[1]]['n']);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);iss=min(vals)>0
  if iss:sadd.append(e)
  norm=[float(t),float(1-t),mul_sqrt_ratio(b1,aa,n2(p)),mul_sqrt_ratio(b2,cc,n2(p))]
  edge_a.append({'edge':list(e),'incident_faces':inc,'saddle':iss,'components_exact':{'t':qs(t),'one_minus_t':qs(Q(1)-t),'beta1':qs(b1),'beta2':qs(b2)},'components_normalized':{'t':norm[0],'one_minus_t':norm[1],'beta1':norm[2],'beta2':norm[3]},'decision_normalized':min(norm)})
 return X,N,support,face_a,vert_a,edge_a,stable,unst,sadd

def intersection_bary(ap,am,u,v):
 dp=det(ap,u,v);dm=det(am,u,v);assert dp*dm<0
 t=dp/(dp-dm);p=add(ap,mul(sub(am,ap),t));aa=n2(u);bb=dot(u,v);cc=n2(v);ru=dot(p,u);rv=dot(p,v);den=aa*cc-bb*bb;lu=(ru*cc-rv*bb)/den;lv=(rv*aa-ru*bb)/den;l0=Q(1)-lu-lv
 assert sub(p,add(mul(u,lu),mul(v,lv)))==(Q(0),Q(0),Q(0));assert min(t,Q(1)-t,lu,lv,l0)>0,(t,lu,lv,l0)
 return {'segment_parameter_exact':qs(t),'equator_barycentric_exact':[qs(l0),qs(lu),qs(lv)],'intersection_exact':[qs(z) for z in p]}
def make_cell(X,u,v,ap,am,name,aplabel,amlabel):
 dp=det(ap,X[u],X[v]);dm=det(am,X[u],X[v]);assert dp*dm<0
 z={'name':name,'equator':['own_centroid',u,v],'positive_apex':aplabel,'negative_apex':amlabel,'positive_tetra_determinant_exact':qs(dp),'negative_tetra_determinant_exact':qs(dm)};z.update(intersection_bary(ap,am,X[u],X[v]));return z

def build():
 rows,line,S=read_rows();faces=exact_faces(rows,S);cycles=[f['cycle'] for f in faces]
 EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for a,b in zip(c,c[1:]+c[:1]):EF[tuple(sorted((a,b)))].append(fi)
 assert all(len(v)==2 for v in EF.values())
 active=sorted({i for c in cycles for i in c});inactive=sorted(set(rows)-set(active));assert len(active)-len(EF)+len(faces)==2
 D6,M,V,C,tris=exact_mass(rows,faces,S);X,N,SUP,face_a,vert_a,edge_a,stable,unst,sadd=mechanics(rows,faces,EF,active,C,S)
 topo=[];ing=[];allgap=[]
 for f in faces:
  nn=Q(sum(z*z for z in f['n']));cs=set(f['cycle'])
  for i,p in rows.items():
   if i not in cs:
    g=ratio_sqrt(Q(f['h']-dot(f['n'],p),S),nn);assert g>0;allgap.append(g);(ing if i in inactive else topo).append(g)
 channels=[]
 for e in sorted(EF):
  u,v=e;ext=[z for j,z in SUP[u].items() if j!=v]+[z for j,z in SUP[v].items() if j!=u]
  if ext and min(ext)>0:
   A=SUP[u][v];B=SUP[v][u];rhs=n2(sub(X[v],X[u]));assert A+B==rhs and rhs>0;channels.append({'edge':list(e),'mutual_A_exact':qs(A),'mutual_B_exact':qs(B),'sum_squared_edge_exact':qs(rhs),'minimum_external_raw':float(min(ext))})
 obstruction=next(z for z in channels if z['edge']==[226,227]);assert all(SUP[8][j]>0 for j in SUP[8])
 rad={i:n2(X[i]) for i in active};order=sorted(active,key=lambda i:rad[i],reverse=True);assert order[0]==8;tg=min(rad[8]-rad[i] for i in active if i!=8);assert tg>0
 absorbed=[130,153,154,176,182,201,220,221,222];assert all(i in inactive for i in absorbed);assert (153,154) not in EF and (130,222) not in EF and (176,182) not in EF and not any(set(c)=={201,220,221} for c in cycles)
 # exact four-cell complex
 fcentral=next(fi for fi,c in enumerate(cycles) if set(c)=={224,226,227});fnear=next(fi for fi,c in enumerate(cycles) if set(c)=={223,224,226});M0=mul(add(add(X[224],X[226]),X[227]),Q(1,3));N0=mul(add(add(X[223],X[224]),X[226]),Q(1,3))
 c1=make_cell(X,224,226,M0,N0,'central-to-crossgap bipyramid','M0','N0');c2=make_cell(X,224,227,M0,X[225],'central-to-direct boundary bipyramid','M0',225);c3=make_cell(X,226,227,M0,X[228],'central-to-return boundary bipyramid','M0',228)
 other=next(fi for fi in EF[(223,224)] if fi!=fnear);w=next(z for z in cycles[other] if z not in (223,224));assert w==195,(w,cycles[other]);c4=make_cell(X,223,224,N0,X[195],'cross-gap fourth bipyramid','N0',195);cells=[c1,c2,c3,c4]
 new=set(range(223,229));closure=[fi for fi,c in enumerate(cycles) if set(c)&new];ced=defaultdict(list);cd=[]
 for fi in closure:
  c=cycles[fi];assert len(c)==3;d=det(X[c[0]],X[c[1]],X[c[2]]);assert d!=0;cd.append(abs(d))
  for a,b in zip(c,c[1:]+c[:1]):ced[tuple(sorted((a,b)))].append(fi)
 adj=defaultdict(set)
 for fs in ced.values():
  for a in fs:
   for b in fs:
    if a!=b:adj[a].add(b)
 seen={closure[0]};q=[closure[0]]
 while q:
  a=q.pop()
  for b in adj[a]:
   if b not in seen:seen.add(b);q.append(b)
 assert len(seen)==len(closure)
 def angle(i,j):z=ratio_sqrt(dot(X[i],X[j]),rad[i]*rad[j]);return math.acos(max(-1,min(1,z)))
 bpath=[135,224,223,183];assert all(tuple(sorted(e)) in EF for e in zip(bpath,bpath[1:]));bang=[angle(a,b) for a,b in zip(bpath,bpath[1:])]
 complex_rec={'version':2,'type':'macroscopic six-vertex triangular-prismatic replacement with four linked nonsimplicial triangular-bipyramidal centroid-fan cells','new_rows':sorted(new),'new_true_edges':[list(e) for e in sorted(EF) if e[0] in new and e[1] in new],'M0_exact':[qs(z) for z in M0],'N0_exact':[qs(z) for z in N0],'cells':cells,'shared_interior_edges':[['own_centroid','M0'],['own_centroid','N0']],'closure_face_ids':closure,'closure_faces':len(closure),'closure_connected':True,'minimum_closure_tetra_determinant_exact':qs(min(cd)),'minimum_closure_tetra_determinant_decimal':float(min(cd)),'cross_gap_true_edge_path':bpath,'cross_gap_edge_angles_degrees':[z*180/math.pi for z in bang],'maximum_cross_gap_step_degrees':max(bang)*180/math.pi,'sector_contacts':{'terminal':sorted(new|({69,152,154,155,221,222}&set(active))),'direct':sorted({4,5,86,88,132,133,135,136,137,138,139,140,141,142,224,225,227}&set(active)),'return_gap':sorted({172,175,176,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,223,226,228}&set(active)),'target_north':sorted({7,8,9,194,195,196,197,198,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,223,224}&set(active))}}
 sf=[face_a[i]['decision_normalized'] for i in stable];nf=[-z['decision_normalized'] for z in face_a if not z['stable']];uv=[z['decision_normalized'] for z in vert_a if z['unstable']];nv=[-z['decision_normalized'] for z in vert_a if not z['unstable']];sh=[z['decision_normalized'] for z in edge_a if z['saddle']];nh=[-z['decision_normalized'] for z in edge_a if not z['saddle']]
 assert len(stable)==2 and any(set(cycles[i])==set(range(17)) for i in stable) and any(set(cycles[i])=={195,223,224} for i in stable);assert unst==[8,227];assert sadd==[(135,224),(183,223)]
 cert={'version':2,'verdict':'NONWINNER — exact M42 cross-gap fourth-cell triangular-prismatic endpoint is strict own-centroid (2,2,2).','scale':S,'input_rows':len(rows),'active_rows':active,'inactive_rows':inactive,'f_vector':[len(active),len(EF),len(faces)],'complexity':len(active)+len(EF)+len(faces)-2,'euler':len(active)-len(EF)+len(faces),'volume_exact':qs(V),'volume_decimal':float(V),'first_moments_unshifted_exact':[qs(z) for z in M],'centroid_unshifted_exact':[qs(z) for z in C],'centroid_unshifted_decimal':[float(z) for z in C],'dependent_translation_exact':[qs(-z) for z in C],'centered_first_moments_exact':['0/1']*3,'class':[2,2,2],'stable_faces':[{'face':i,'cycle':cycles[i],'decision_normalized':face_a[i]['decision_normalized']} for i in stable],'unstable_vertices':[{'vertex':i,'decision_normalized':next(z['decision_normalized'] for z in vert_a if z['vertex']==i)} for i in unst],'saddle_edges':[{'edge':list(e),'decision_normalized':next(z['decision_normalized'] for z in edge_a if z['edge']==list(e))} for e in sadd],'margins':{'stable_positive_min':min(sf),'nonstable_exclusion_min':min(nf),'unstable_positive_min':min(uv),'nonunstable_exclusion_min':min(nv),'saddle_positive_min':min(sh),'nonsaddle_exclusion_min':min(nh),'active_topology_distance_min':min(topo),'inactive_distance_min':min(ing),'all_input_incidence_min':min(allgap)},'absorbed_parent_rows':absorbed,'absent_parent_features':{'edge_153_154':(153,154) not in EF,'stable_201_220_221':not any(set(c)=={201,220,221} for c in cycles),'saddle_130_222':(130,222) not in EF,'saddle_176_182':(176,182) not in EF},'old_channel_absences':{f'{a}_{b}':tuple(sorted((a,b))) not in EF for a,b in [(218,219),(146,219),(147,148),(95,96),(82,96),(96,104),(104,111)]},'obstruction':obstruction,'independent_unstable_target':8,'radial_order':{'target_vertex':8,'target_unique_farthest':True,'minimum_squared_gap_exact':qs(tg),'minimum_squared_gap_decimal':float(tg),'order':order},'fourth_cell_complex':complex_rec,'positive_channel_edges':channels}
 # output ledgers
 with open(ROOT/'coordinates_all_exact.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_int','y_int','z_int','denominator','x_exact','y_exact','z_exact','active','lineage'])
  for i in sorted(rows):w.writerow([i,*rows[i],S,*[qs(Q(z,S)) for z in rows[i]],int(i in active),line[i]])
 with open(ROOT/'coordinates_active_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_exact','y_exact','z_exact','x_decimal','y_decimal','z_decimal','radius_squared_exact','radius_squared_decimal'])
  for i in active:w.writerow([i,*[qs(z) for z in X[i]],*[dec(z) for z in X[i]],qs(rad[i]),dec(rad[i])])
 with open(ROOT/'halfspaces_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['face','nx','ny','nz','h_lattice','h_centered_exact','cycle'])
  for fi,z in enumerate(faces):w.writerow([fi,*z['n'],z['h'],face_a[fi]['h_centered_exact'],' '.join(map(str,z['cycle']))])
 json.dump(cycles,open(ROOT/'face_cycles.json','w'),indent=2);json.dump(face_a,open(ROOT/'faces_mechanics.json','w'),indent=2)
 with open(ROOT/'true_edges.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_faces'])
  for a,b in sorted(EF):w.writerow([a,b,' '.join(map(str,EF[(a,b)]))])
 with open(ROOT/'vertices_mechanics.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['vertex','unstable','decision_normalized','supports_exact_json','supports_normalized_json'])
  for z in vert_a:w.writerow([z['vertex'],int(z['unstable']),repr(z['decision_normalized']),json.dumps(z['supports_exact'],separators=(',',':')),json.dumps(z['supports_normalized'],separators=(',',':'))])
 with open(ROOT/'edges_four_component_audit.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_faces','saddle','t_exact','one_minus_t_exact','beta1_exact','beta2_exact','t_normalized','one_minus_t_normalized','beta1_normalized','beta2_normalized','decision_normalized'])
  for z in edge_a:
   ce=z['components_exact'];cn=z['components_normalized'];w.writerow([*z['edge'],' '.join(map(str,z['incident_faces'])),int(z['saddle']),ce['t'],ce['one_minus_t'],ce['beta1'],ce['beta2'],repr(cn['t']),repr(cn['one_minus_t']),repr(cn['beta1']),repr(cn['beta2']),repr(z['decision_normalized'])])
 json.dump(complex_rec,open(ROOT/'fourth_cell_complex.json','w'),indent=2);json.dump({'version':2,'target_vertex':8,'unique_farthest':True,'minimum_squared_gap_exact':qs(tg),'minimum_squared_gap_decimal':float(tg),'order':[{'rank':k+1,'vertex':i,'radius_squared_exact':qs(rad[i]),'radius_squared_decimal':float(rad[i])} for k,i in enumerate(order)]},open(ROOT/'radial_order_certificate.json','w'),indent=2);json.dump(cert,open(ROOT/'certificate.json','w'),indent=2)
 print('PASS exact endpoint build');print('input active E F C',len(rows),len(active),len(EF),len(faces),cert['complexity']);print('class',cert['class']);print('stable',cert['stable_faces']);print('unstable',cert['unstable_vertices']);print('saddles',cert['saddle_edges']);print('volume',qs(V));print('centroid',*[qs(z) for z in C]);print('margins',cert['margins']);print('obstruction',obstruction);print('target gap',float(tg));print('new edges',complex_rec['new_true_edges']);print('crossgap degrees',complex_rec['cross_gap_edge_angles_degrees'])
if __name__=='__main__':build()
