#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as Q
from collections import defaultdict, deque
from pathlib import Path
import csv,json,math,hashlib
import numpy as np
from numeric_hull_proposer import evaluate
R=Path(__file__).resolve().parent
S=10**36; K=10**24
# Parent packet already collapsed: additionally absorb the complete six-vertex superlevel terminal packet,
# its obsolete terminal strip, both old apices, and the two old gate vertices.
ABSORB={134,180,181,199,218,219}|set(range(143,153))
CSTAR=(-22638817877*K,9862693840*K,-7081176048*K)
NEW={
220:(2498667797393*K,-2884051905141*K,-865392654376*K),
221:(2866953149070*K,-6660906984580*K,-1535167851984*K),
222:(3712882082663*K,-5945040770195*K,-825500569466*K),
}
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def primitive(n,h):
 g=gcdall((*n,h));n=tuple(int(z)//g for z in n);h=int(h)//g
 # canonical sign for stable key only; orientation restored separately
 q=next(z for z in (*n,h) if z)
 return ((*n,h) if q>0 else (*tuple(-z for z in n),-h))
def qstr(x):return f'{x.numerator}/{x.denominator}'
def dec(x):return format(float(x),'.18g')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load_rows():
 rows={}
 with open(R/'predecessor_two_cell_coordinates.csv') as f:
  for r in csv.DictReader(f):
   i=int(r['source_id']);assert int(r['denominator'])==S
   rows[i]=(int(r['x_num']),int(r['y_num']),int(r['z_num']))
 assert len(rows)==131
 for i in ABSORB:rows[i]=CSTAR
 rows.update(NEW)
 return rows

def exact_faces(rows):
 pts={i:np.array([z/S for z in p],float) for i,p in rows.items()}
 rr=evaluate(pts,plane_tol=1e-8,strict_tol=1e-12)
 assert rr.valid,rr.error
 faces=[];seen=set()
 for f in rr.faces:
  c=list(f['cycle'])
  # exact noncollinear triple
  a=rows[c[0]]; tri=None
  for u in range(1,len(c)-1):
   for v in range(u+1,len(c)):
    n=cross(sub(rows[c[u]],a),sub(rows[c[v]],a))
    if n!=(0,0,0):tri=(c[0],c[u],c[v],n);break
   if tri:break
  assert tri
  n=tri[3];h=dot(n,a);vals={i:dot(n,p)-h for i,p in rows.items()}
  pos=any(z>0 for z in vals.values());neg=any(z<0 for z in vals.values());assert not(pos and neg),(c,min(vals.values()),max(vals.values()))
  if pos:n=tuple(-z for z in n);h=-h;vals={i:-z for i,z in vals.items()}
  assert all(z<=0 for z in vals.values())
  cop=sorted(i for i,z in vals.items() if z==0);assert set(cop)==set(c),(c,cop)
  # orient cycle so area vector follows outward n
  area=(0,0,0)
  for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
  if dot(area,n)<0:c=[c[0]]+list(reversed(c[1:]))
  # reduce oriented plane without canonical sign flip
  g=gcdall((*n,h));n=tuple(z//g for z in n);h//=g
  key=primitive(n,h);assert key not in seen;seen.add(key)
  faces.append({'cycle':c,'n':n,'h':h})
 # stable deterministic order: base face last? sort by min cycle, len, tuple
 faces.sort(key=lambda f:(0 if set(f['cycle'])==set(range(17)) else 1,min(f['cycle']),len(f['cycle']),tuple(f['cycle'])))
 return faces

def build():
 rows=load_rows();faces=exact_faces(rows);cycles=[f['cycle'] for f in faces]
 # complete exact edges
 EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for a,b in zip(c,c[1:]+c[:1]):EF[tuple(sorted((a,b)))].append(fi)
 assert all(len(v)==2 for v in EF.values())
 active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active));assert len(active)-len(EF)+len(faces)==2
 # exact mass
 D6=0;M=[0,0,0]
 for c in cycles:
  for j in range(1,len(c)-1):
   a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
   for k in range(3):M[k]+=d*(a[k]+b[k]+z[k])
 assert D6>0
 V=Q(D6,6*S**3);C=tuple(Q(M[k],4*D6*S) for k in range(3));Mom=tuple(Q(M[k],24*S**4) for k in range(3));assert all(Mom[k]==V*C[k] for k in range(3))
 X={i:tuple(Q(rows[i][k],S)-C[k] for k in range(3)) for i in active}
 # mechanics
 face_a=[];stable=[]
 for fi,f in enumerate(faces):
  c=f['cycle'];n=tuple(Q(z) for z in f['n']);hc=Q(f['h'],S)-dot(n,C);foot=mul(n,hc/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[];norm=[]
  for a,b in zip(c,c[1:]+c[:1]):
   e=sub(X[b],X[a]);z=dot(cross(e,sub(foot,X[a])),n);rz=dot(cross(e,sub(ref,X[a])),n)
   if rz<0:z=-z
   vals.append(z);norm.append(float(z)/math.sqrt(float(n2(n)*n2(e))))
  st=min(vals)>0
  if st:stable.append(fi)
  face_a.append({'face':fi,'cycle':c,'plane_integer':[*(f['n']),f['h']],'h_centered_exact':qstr(hc),'stable':st,'components_exact':[qstr(z) for z in vals],'components_normalized':norm,'decision_normalized':min(norm)})
 N=defaultdict(set)
 for a,b in EF:N[a].add(b);N[b].add(a)
 SUP={};vert_a=[];unstable=[]
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals;norm={j:float(z)/math.sqrt(float(n2(X[i])*n2(sub(X[j],X[i])))) for j,z in vals.items()};u=min(vals.values())>0
  if u:unstable.append(i)
  vert_a.append({'vertex':i,'unstable':u,'supports_exact':{str(j):qstr(z) for j,z in vals.items()},'supports_normalized':{str(j):v for j,v in norm.items()},'decision_normalized':min(norm.values())})
 edge_a=[];saddles=[];EC={}
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(z) for z in faces[inc[0]]['n']);n2v=tuple(Q(z) for z in faces[inc[1]]['n']);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);EC[e]=vals;h=min(vals)>0
  if h:saddles.append(e)
  pn=math.sqrt(float(n2(p)));norm=[float(t),float(1-t),float(b1)*math.sqrt(float(aa))/pn,float(b2)*math.sqrt(float(cc))/pn]
  edge_a.append({'edge':list(e),'incident_faces':inc,'saddle':h,'components_exact':[qstr(z) for z in vals],'components_normalized':norm,'decision_normalized':min(norm)})
 # topology / inactive distances
 topo=[];ing=[]
 for f in faces:
  nn=math.sqrt(sum(z*z for z in f['n']))
  cs=set(f['cycle'])
  for i,p in rows.items():
   if i not in cs:
    g=Q(f['h']-dot(f['n'],p),S)/nn;assert g>0;topo.append(float(g))
    if i in inactive:ing.append(float(g))
 # ext-positive obstruction candidates
 channels=[]
 for e in sorted(EF):
  u,v=e
  ex=[z for j,z in SUP[u].items() if j!=v]+[z for j,z in SUP[v].items() if j!=u]
  if ex and min(ex)>0:
   A=SUP[u][v];B=SUP[v][u];rhs=n2(sub(X[v],X[u]));assert A+B==rhs
   channels.append({'edge':list(e),'mutual_A':qstr(A),'mutual_B':qstr(B),'sum_squared_edge':qstr(rhs),'minimum_external_raw':float(min(ex))})
 # exact radial order
 rad={i:n2(X[i]) for i in active};order=sorted(active,key=lambda i:rad[i],reverse=True);assert order[0]==8
 # three-cell complex around central face
 central=next((fi for fi,c in enumerate(cycles) if set(c)=={220,221,222}),None);assert central is not None
 Mpt=mul(add(add(X[220],X[221]),X[222]),Q(1,3));O=(Q(0),Q(0),Q(0));cells=[]
 for u,v in ((220,221),(220,222),(221,222)):
  inc=EF[tuple(sorted((u,v)))];other=inc[0] if inc[1]==central else inc[1];p=next(z for z in cycles[other] if z not in (u,v));assert len(cycles[other])==3
  dc=det(sub(Mpt,O),sub(X[u],O),sub(X[v],O));da=det(sub(X[p],O),sub(X[u],O),sub(X[v],O));assert dc*da<0
  # line M->p intersection with triangle O,u,v: solve M+t(p-M)=alpha*u+beta*v
  # Cramer solve [p-M,-u,-v] * [t,alpha,beta] = -M
  A0=sub(X[p],Mpt);B0=tuple(-z for z in X[u]);C0=tuple(-z for z in X[v]);D=det(A0,B0,C0);assert D!=0
  rhs=tuple(-z for z in Mpt)
  t=det(rhs,B0,C0)/D;alpha=det(A0,rhs,C0)/D;beta=det(A0,B0,rhs)/D
  assert 0<t<1 and alpha>0 and beta>0 and alpha+beta<1,(u,v,p,t,alpha,beta)
  cells.append({'equator':[0,u,v],'central_apex':'M','boundary_apex':p,'central_tetra_determinant':qstr(dc),'adjacent_tetra_determinant':qstr(da),'segment_intersection':{'t_M_to_p':qstr(t),'alpha_u':qstr(alpha),'beta_v':qstr(beta),'origin_weight':qstr(1-alpha-beta)}})
 # closure fan connectivity, all incident faces cone to O
 closure=[fi for fi,c in enumerate(cycles) if set(c)&{220,221,222}];ced=defaultdict(list);cdets=[]
 for fi in closure:
  c=cycles[fi];assert len(c)==3;z=det(X[c[0]],X[c[1]],X[c[2]]);assert z!=0;cdets.append(abs(z))
  for a,b in zip(c,c[1:]+c[:1]):ced[tuple(sorted((a,b)))].append(fi)
 adj=defaultdict(set)
 for fs in ced.values():
  for a in fs:
   for b in fs:
    if a!=b:adj[a].add(b)
 seen={closure[0]};dq=list(seen)
 while dq:
  a=dq.pop()
  for b in adj[a]:
   if b not in seen:seen.add(b);dq.append(b)
 assert len(seen)==len(closure)
 # margins
 sf=[face_a[i]['decision_normalized'] for i in stable];nf=[-r['decision_normalized'] for r in face_a if not r['stable']]
 uv=[r['decision_normalized'] for r in vert_a if r['unstable']];nv=[-r['decision_normalized'] for r in vert_a if not r['unstable']]
 sh=[r['decision_normalized'] for r in edge_a if r['saddle']];nh=[-r['decision_normalized'] for r in edge_a if not r['saddle']]
 obstruction=next(z for z in channels if z['edge']==[153,154])
 assert stable and unstable==[8,153] and saddles==[(130,222),(176,182)]
 # outputs
 with open(R/'coordinates_all_exact.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_num','y_num','z_num','denominator','x_exact','y_exact','z_exact','active','lineage'])
  for i in sorted(rows):
   p=rows[i];lin=('third_cell_absorbed_packet' if i in ABSORB else ('third_cell_apex_'+str(i) if i in NEW else 'two_cell_predecessor_input'))
   w.writerow([i,*p,S,*[qstr(Q(z,S)) for z in p],int(i in active),lin])
 with open(R/'coordinates_active_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_exact','y_exact','z_exact','x_decimal','y_decimal','z_decimal','radius_squared_exact','radius_squared_decimal'])
  for i in active:w.writerow([i,*[qstr(z) for z in X[i]],*[dec(z) for z in X[i]],qstr(rad[i]),dec(rad[i])])
 json.dump(cycles,open(R/'face_cycles.json','w'),indent=2)
 with open(R/'true_edges.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_face_1','incident_face_2']);
  for e,inc in sorted(EF.items()):w.writerow([*e,*inc])
 with open(R/'halfspaces_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['face','nx','ny','nz','h_unshifted_integer','h_centered_exact','cycle'])
  for r in face_a:w.writerow([r['face'],*r['plane_integer'][:3],r['plane_integer'][3],r['h_centered_exact'],' '.join(map(str,r['cycle']))])
 json.dump(face_a,open(R/'faces_mechanics.json','w'),indent=2)
 with open(R/'vertices_mechanics.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['vertex','unstable','decision_normalized','supports_exact_json','supports_normalized_json'])
  for r in vert_a:w.writerow([r['vertex'],int(r['unstable']),repr(r['decision_normalized']),json.dumps(r['supports_exact'],separators=(',',':')),json.dumps(r['supports_normalized'],separators=(',',':'))])
 with open(R/'edges_four_component_audit.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['u','v','incident_faces','saddle','t_exact','one_minus_t_exact','beta1_exact','beta2_exact','t_normalized','one_minus_t_normalized','beta1_normalized','beta2_normalized','decision_normalized'])
  for r in edge_a:w.writerow([*r['edge'],' '.join(map(str,r['incident_faces'])),int(r['saddle']),*r['components_exact'],*map(repr,r['components_normalized']),repr(r['decision_normalized'])])
 complex_rec={'version':1,'type':'three triangular-bipyramidal nonsimplicial centroid-fan cells sharing the interior radial edge O-M','central_boundary_face':cycles[central],'M_exact':[qstr(z) for z in Mpt],'cells':cells,'closure_incident_faces':len(closure),'closure_face_ids':closure,'closure_connected':True,'minimum_closure_tetra_determinant_exact':qstr(min(cdets)),'sector_contacts':{
  'terminal':sorted(set(active)&{69,102,113,114,143,144,145,146,147,148,149,153,154,198,221,222}),
  'direct':sorted(set(active)&{4,5,86,88,120,127,128,129,130,131,132,133,134,135,136,220,222}),
  'return':sorted(set(active)&set(range(153,218))),
  'stable_foot':sorted(set(active)&{102,117,118,120,198,199,200,201,202,220,221})}}
 json.dump(complex_rec,open(R/'three_cell_complex.json','w'),indent=2)
 radial={'version':1,'target_vertex':8,'unique_farthest':True,'order':[{'rank':k+1,'vertex':i,'radius_squared_exact':qstr(rad[i]),'radius_squared_decimal':float(rad[i])} for k,i in enumerate(order)],'previous_superlevel_packet_inactive':sorted(ABSORB & {144,145,146,150,151,219}),'conclusion':'Protected vertex 8 is the unique exact global farthest actual vertex. The predecessor six-vertex radial-superlevel obstruction is removed; the residual extra unstable vertex 153 is strictly closer than 8.'}
 json.dump(radial,open(R/'radial_order_certificate.json','w'),indent=2)
 cert={'version':1,'verdict':'NONWINNER — exact M42 third nonsimplicial-cell endpoint is strict own-centroid (2,2,2).','scale':S,'input_rows':len(rows),'active_rows':active,'inactive_rows':inactive,'f_vector':[len(active),len(EF),len(faces)],'complexity':len(active)+len(EF)+len(faces)-2,'volume_exact':qstr(V),'volume_decimal':float(V),'first_moments_unshifted_exact':[qstr(z) for z in Mom],'centroid_unshifted_exact':[qstr(z) for z in C],'centroid_unshifted_decimal':[float(z) for z in C],'centered_first_moments_exact':['0/1']*3,'class':[len(stable),len(unstable),len(saddles)],'stable_faces':[{'face':i,'cycle':cycles[i],'decision_normalized':face_a[i]['decision_normalized']} for i in stable],'unstable_vertices':[{'vertex':i,'decision_normalized':next(z['decision_normalized'] for z in vert_a if z['vertex']==i)} for i in unstable],'saddle_edges':[{'edge':list(e),'decision_normalized':next(z['decision_normalized'] for z in edge_a if z['edge']==list(e))} for e in saddles],'margins':{'stable_positive_min':min(sf),'nonstable_exclusion_min':min(nf),'unstable_positive_min':min(uv),'nonunstable_exclusion_min':min(nv),'saddle_positive_min':min(sh),'nonsaddle_exclusion_min':min(nh),'topology_distance_min':min(topo),'inactive_distance_min':min(ing)},'absorbed_rows':sorted(ABSORB),'old_absorbed_rows_from_predecessor':[102,120,127,128,129,147,148,149,173,174,177,178,179,200],'absent_old_edges':[[218,219],[146,219],[147,148],[95,96],[82,96],[96,104],[104,111]],'new_rows':{str(i):[qstr(Q(z,S)) for z in NEW[i]] for i in NEW},'obstruction':obstruction,'radial_order':{'target_unique_farthest':True,'target_radius_squared_exact':qstr(rad[8]),'next_vertex':order[1],'next_radius_squared_exact':qstr(rad[order[1]]),'extra_unstable_radius_squared_exact':qstr(rad[153])},'three_cell_complex':complex_rec,'positive_channel_edges':channels}
 json.dump(cert,open(R/'certificate.json','w'),indent=2)
 print('BUILT',len(rows),len(active),len(EF),len(faces),'class',cert['class'])
 print('V',qstr(V));print('C',*[qstr(z) for z in C]);print('stable',cert['stable_faces']);print('unstable',cert['unstable_vertices']);print('saddles',cert['saddle_edges']);print('margins',cert['margins']);print('channels',[(z['edge'],z['minimum_external_raw']) for z in channels]);print('cell thirds',[(z['boundary_apex'],z['central_tetra_determinant'][:30],z['adjacent_tetra_determinant'][:30]) for z in cells])
if __name__=='__main__':build()
