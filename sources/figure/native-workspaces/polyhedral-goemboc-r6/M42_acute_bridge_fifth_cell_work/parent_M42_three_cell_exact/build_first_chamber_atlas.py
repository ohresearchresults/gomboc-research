#!/usr/bin/env python3
"""Build the exact first two-control chamber atlas beyond the M42 three-cell endpoint."""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
import csv,json,math,sys
import numpy as np
R=Path(__file__).resolve().parent;BASES=10**36
sys.path.insert(0,str(R));from numeric_hull_proposer import evaluate
def qstr(x):return f'{x.numerator}/{x.denominator}'
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def sub(a,b):return tuple(a[k]-b[k] for k in range(3))
def add(a,b):return tuple(a[k]+b[k] for k in range(3))
def mul(a,t):return tuple(a[k]*t for k in range(3))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def n2(a):return dot(a,a)
def lcm(a,b):return abs(a*b)//math.gcd(a,b)
def gcdall(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(int(x)))
 return g
def primitive(n,h):
 g=gcdall((*n,h));return (*tuple(int(z)//g for z in n),int(h)//g)
base={}
with open(R/'coordinates_all_exact.csv') as f:
 for r in csv.DictReader(f):base[int(r['source_id'])]=tuple(Q(int(r[k]),int(r['denominator'])) for k in ('x_num','y_num','z_num'))
Cstar=base[102];Q222=base[222];Q182=base[182]
def construct(a:Q,b:Q):
 P=dict(base);P[222]=add(Cstar,mul(sub(Q222,Cstar),1+a));P[182]=add(Cstar,mul(sub(Q182,Cstar),1+b));return P

def audit(a:Q,b:Q,full=True):
 Pq=construct(a,b);L=BASES
 for z in (a.denominator,b.denominator):L=lcm(L,BASES*z)
 rows={i:tuple(int(z*L) for z in p) for i,p in Pq.items()};assert all(Q(rows[i][k],L)==Pq[i][k] for i in rows for k in range(3))
 rr=evaluate({i:np.array([float(z) for z in p]) for i,p in Pq.items()},plane_tol=2e-8,strict_tol=1e-12);assert rr.valid,rr.error;cycles=[list(f['cycle']) for f in rr.faces];planes=[]
 for fi,c in enumerate(cycles):
  n=cross(sub(rows[c[1]],rows[c[0]]),sub(rows[c[2]],rows[c[0]]));h=dot(n,rows[c[0]]);vals={i:dot(n,p)-h for i,p in rows.items()};pos=any(z>0 for z in vals.values());neg=any(z<0 for z in vals.values());assert not(pos and neg)
  if pos:n=tuple(-z for z in n);h=-h
  cop={i for i,p in rows.items() if dot(n,p)==h};assert cop==set(c)
  assert all(dot(n,p)<h for i,p in rows.items() if i not in cop)
  area=(0,0,0)
  for u,v in zip(c,c[1:]+c[:1]):area=add(area,cross(rows[u],rows[v]))
  if dot(area,n)<0:c=[c[0]]+list(reversed(c[1:]));cycles[fi]=c
  n0,n1,nz,h=primitive(n,h);planes.append(((n0,n1,nz),h))
 EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for u,v in zip(c,c[1:]+c[:1]):EF[tuple(sorted((u,v)))].append(fi)
 assert all(len(v)==2 for v in EF.values());active=sorted(set().union(*(set(c) for c in cycles)));inactive=sorted(set(rows)-set(active));assert len(active)-len(EF)+len(cycles)==2
 D6=0;M=[0,0,0]
 for c in cycles:
  for j in range(1,len(c)-1):
   x,y,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(x,y,z);D6+=d
   for k in range(3):M[k]+=d*(x[k]+y[k]+z[k])
 assert D6>0;V=Q(D6,6*L**3);C=tuple(Q(M[k],4*D6*L) for k in range(3));Mom=tuple(Q(M[k],24*L**4) for k in range(3));assert all(Mom[k]==V*C[k] for k in range(3));X={i:tuple(Q(rows[i][k],L)-C[k] for k in range(3)) for i in active}
 stable=[];fraw=[];fdec=[]
 for fi,c in enumerate(cycles):
  n=tuple(Q(z) for z in planes[fi][0]);h=dot(n,X[c[0]]);foot=mul(n,h/n2(n));ref=tuple(sum((X[i][k] for i in c),Q(0))/len(c) for k in range(3));vals=[];norm=[]
  for u,v in zip(c,c[1:]+c[:1]):
   e=sub(X[v],X[u]);z=dot(cross(e,sub(foot,X[u])),n)
   if dot(cross(e,sub(ref,X[u])),n)<0:z=-z
   vals.append(z);norm.append(float(z)/math.sqrt(float(n2(n)*n2(e))))
  fraw.append(vals);fdec.append(min(norm));
  if min(vals)>0:stable.append(fi)
 N=defaultdict(set)
 for u,v in EF:N[u].add(v);N[v].add(u)
 SUP={};unst=[];vdec={}
 for i in active:
  vals={j:-dot(X[i],sub(X[j],X[i])) for j in sorted(N[i])};SUP[i]=vals;vdec[i]=min(float(z)/math.sqrt(float(n2(X[i])*n2(sub(X[j],X[i])))) for j,z in vals.items())
  if min(vals.values())>0:unst.append(i)
 sadd=[];eraw={};edec={}
 for e,inc in sorted(EF.items()):
  i,j=e;d=sub(X[j],X[i]);t=-dot(X[i],d)/n2(d);p=add(X[i],mul(d,t));n1=tuple(Q(z) for z in planes[inc[0]][0]);n2v=tuple(Q(z) for z in planes[inc[1]][0]);aa=n2(n1);bb=dot(n1,n2v);cc=n2(n2v);r1=dot(p,n1);r2=dot(p,n2v);den=aa*cc-bb*bb;assert den>0;b1=(r1*cc-r2*bb)/den;b2=(r2*aa-r1*bb)/den;vals=(t,Q(1)-t,b1,b2);eraw[e]=vals;pn=math.sqrt(float(n2(p)));edec[e]=min(float(t),float(1-t),float(b1)*math.sqrt(float(aa))/pn,float(b2)*math.sqrt(float(cc))/pn)
  if min(vals)>0:sadd.append(e)
 channels=[]
 for e in sorted(EF):
  u,v=e;ex=[z for j,z in SUP[u].items() if j!=v]+[z for j,z in SUP[v].items() if j!=u]
  if ex and min(ex)>0:channels.append({'edge':[u,v],'mutual':[qstr(SUP[u][v]),qstr(SUP[v][u])],'sum_squared_edge':qstr(n2(sub(X[v],X[u]))),'minimum_external_raw':float(min(ex))})
 rad={i:n2(X[i]) for i in active};order=sorted(active,key=lambda i:rad[i],reverse=True)
 rec={'parameters':{'a_222':qstr(a),'b_182':qstr(b)},'scale':L,'f_vector':[len(active),len(EF),len(cycles)],'complexity':len(active)+len(EF)+len(cycles)-2,'active_rows':active,'inactive_rows':inactive,'volume_exact':qstr(V),'centroid_exact':[qstr(z) for z in C],'centered_moments_exact':['0/1']*3,'class':[len(stable),len(unst),len(sadd)],'stable_faces':[{'face':i,'cycle':cycles[i],'decision_normalized':fdec[i]} for i in stable],'unstable_vertices':[{'vertex':i,'decision_normalized':vdec[i]} for i in unst],'saddle_edges':[{'edge':list(e),'decision_normalized':edec[e]} for e in sadd],'positive_channel_edges':channels,'target_face_present':any(set(cycles[i])==set(range(17)) for i in stable),'target_vertex_present':8 in unst,'target_unique_farthest':order[0]==8,'radial_top':[{'vertex':i,'radius_squared_exact':qstr(rad[i])} for i in order[:8]]}
 if full:
  rec['faces']=[{'face':i,'cycle':c,'plane_integer':[*(planes[i][0]),planes[i][1]]} for i,c in enumerate(cycles)];rec['true_edges']=[{'edge':list(e),'incident_faces':fs} for e,fs in sorted(EF.items())]
 return rec,{'cycles':cycles,'EF':EF,'fraw':fraw,'SUP':SUP,'eraw':eraw}

cells={'C00_base':(Q(0),Q(0)),'C10_direct_UH_birth':(Q(1,20),Q(0)),'C01_return_SH_birth':(Q(0),Q(3,50)),'C11_both_births':(Q(1,20),Q(3,50))}
out=[]
for name,(a,b) in cells.items():
 rec,_=audit(a,b,True);rec['name']=name;out.append(rec);print(name,rec['f_vector'],rec['class'],rec['stable_faces'],rec['unstable_vertices'],rec['saddle_edges'])
br=[]
for name,axis,lo,hi in [('direct_UH_wall_222_221222','A',Q(354351841591,10**13),Q(354351841592,10**13)),('return_SH_wall_172175182_172182','B',Q(578682293826,10**13),Q(578682293827,10**13))]:
 states=[]
 for side,t in [('lo',lo),('hi',hi)]:
  a,b=(t,Q(0)) if axis=='A' else (Q(0),t);rec,raw=audit(a,b,False)
  if axis=='A':
   vm=min(raw['SUP'][222].items(),key=lambda x:x[1]);e=raw['eraw'][(221,222)];em=min(enumerate(e),key=lambda x:x[1]);sig={'vertex_222_min_neighbor':vm[0],'vertex_222_min_support_exact':qstr(vm[1]),'edge_221_222_min_component_index':em[0],'edge_221_222_min_component_exact':qstr(em[1])}
  else:
   fi=next(i for i,c in enumerate(raw['cycles']) if set(c)=={172,175,182});fv=min(raw['fraw'][fi]);e=raw['eraw'][(172,182)];em=min(enumerate(e),key=lambda x:x[1]);sig={'face_172_175_182_min_component_exact':qstr(fv),'edge_172_182_min_component_index':em[0],'edge_172_182_min_component_exact':qstr(em[1])}
  states.append({'side':side,'parameter':qstr(t),'f_vector':rec['f_vector'],'class':rec['class'],'signatures':sig})
 br.append({'name':name,'axis':axis,'interval_exact':[qstr(lo),qstr(hi)],'width_exact':qstr(hi-lo),'states':states})
atlas={'version':1,'description':'Exact first outgoing two-control chamber atlas for independent radial opening of third-cell apex 222 and return-gate row 182 about the common interior control point c*. Every representative rebuilds the full hull and all normal cones.','parameterization':'q222(a)=c*+(1+a)(q222-c*); q182(b)=c*+(1+b)(q182-c*); all other inputs fixed.','cells':out,'wall_brackets':br,'verdict':'No chamber is (1,1,0). Opening 222 creates a simultaneous unstable-saddle pair at vertex 222 / edge (221,222). Opening 182 creates a simultaneous stable-saddle pair at face [172,175,182] / edge (172,182). Opening both gives (3,3,4); the remaining block transfers rather than cancels.'}
json.dump(atlas,open(R/'first_chamber_atlas.json','w'),indent=2);print('WROTE',R/'first_chamber_atlas.json')
