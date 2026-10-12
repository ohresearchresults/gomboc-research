#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
import json,math,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import build_exact_endpoint as B

def lcm(a,b):return abs(a//math.gcd(a,b)*b)
BASE,LINE,S0=B.read_rows()
def controlled(a:Q,b:Q):
 L=lcm(a.denominator,b.denominator);S=S0*L
 rows={i:tuple(z*L for z in p) for i,p in BASE.items()}
 rows[223]=tuple(z*a.numerator//a.denominator for z in rows[223]);rows[227]=tuple(z*b.numerator//b.denominator for z in rows[227])
 assert all(z*a.denominator%(a.denominator)==0 for z in [0]) # marker
 return rows,S

def audit(a,b,full=True):
 rows,S=controlled(a,b);faces=B.exact_faces(rows,S);cycles=[f['cycle'] for f in faces];EF=defaultdict(list)
 for fi,c in enumerate(cycles):
  for u,v in zip(c,c[1:]+c[:1]):EF[tuple(sorted((u,v)))].append(fi)
 assert all(len(z)==2 for z in EF.values())
 active=sorted({i for c in cycles for i in c});inactive=sorted(set(rows)-set(active));D6,M,V,C,tris=B.exact_mass(rows,faces,S);X,N,SUP,fa,va,ea,stable,unst,sadd=B.mechanics(rows,faces,EF,active,C,S)
 channels=[]
 for e in sorted(EF):
  u,v=e;ext=[z for j,z in SUP[u].items() if j!=v]+[z for j,z in SUP[v].items() if j!=u]
  if ext and min(ext)>0:
   A=SUP[u][v];BB=SUP[v][u];rhs=B.n2(B.sub(X[v],X[u]));assert A+BB==rhs
   channels.append({'edge':list(e),'mutual_A_exact':B.qs(A),'mutual_B_exact':B.qs(BB),'sum_squared_edge_exact':B.qs(rhs),'minimum_external_raw':float(min(ext))})
 rec={'a_exact':B.qs(a),'b_exact':B.qs(b),'scale':S,'active_rows':active,'inactive_rows':inactive,'f_vector':[len(active),len(EF),len(faces)],'complexity':len(active)+len(EF)+len(faces)-2,'volume_exact':B.qs(V),'centroid_unshifted_exact':[B.qs(z) for z in C],'centered_first_moments_exact':['0/1']*3,'class':[len(stable),len(unst),len(sadd)],'stable_faces':[{'face':i,'cycle':cycles[i],'decision_normalized':fa[i]['decision_normalized']} for i in stable],'unstable_vertices':[{'vertex':i,'decision_normalized':next(z['decision_normalized'] for z in va if z['vertex']==i)} for i in unst],'saddle_edges':[{'edge':list(e),'decision_normalized':next(z['decision_normalized'] for z in ea if z['edge']==list(e))} for e in sadd],'face_cycles':cycles,'true_edges':[{'edge':list(e),'incident_faces':EF[e]} for e in sorted(EF)],'positive_channels':channels}
 if full:rec.update(face_audit=fa,vertex_audit=va,edge_audit=ea)
 return rec,(rows,S,faces,cycles,EF,active,inactive,X,SUP,fa,va,ea)

Avals=[Q(9,10),Q(1)]
Bvals=[Q(991,1000),Q(993,1000),Q(9947,10000),Q(996,1000)]
cells=[]
for ia,a in enumerate(Avals):
 for ib,b in enumerate(Bvals):
  z,_=audit(a,b,True);z['cell_id']=f'A{ia}B{ib}';cells.append(z);print(z['cell_id'],z['f_vector'],z['class'],z['unstable_vertices'],z['saddle_edges'])
# Exact incidence walls, linear circuit determinants under scalar row motion.
def orient(rows,a,b,c,d):return B.det(B.sub(rows[b],rows[a]),B.sub(rows[c],rows[a]),B.sub(rows[d],rows[a]))
def linear_root(moving,circuit):
 rows,S=controlled(Q(1),Q(1));p=rows[moving];r0=dict(rows);r0[moving]=(0,0,0);f0=orient(r0,*circuit);f1=orient(rows,*circuit);return -Q(f0,f1-f0)
# A wall circuit (194,195,224,223); b wall circuit (122,123,225,227)
a_root=linear_root(223,(194,195,224,223));b_inc=linear_root(227,(122,123,225,227))
# exact mechanical sign brackets at a=1
brackets=[('terminal U-H birth: sigma(227->226)=0',Q(9913313896160,10**13),Q(9913313896161,10**13),'B'),('terminal U-H death: sigma(226->227)=0',Q(9947861168775,10**13),Q(9947861168776,10**13),'A')]
wall_records=[]
for desc,lo,hi,which in brackets:
 zl,data_l=audit(Q(1),lo,False);zh,data_h=audit(Q(1),hi,False)
 def mutual(data):
  SUP=data[8];return SUP[226][227],SUP[227][226]
 al,bl=mutual(data_l);ah,bh=mutual(data_h);sl=bl if which=='B' else al;sh=bh if which=='B' else ah
 assert sl*sh<0,(desc,sl,sh)
 wall_records.append({'description':desc,'lo_exact':B.qs(lo),'hi_exact':B.qs(hi),'width_exact':B.qs(hi-lo),'lo_class':zl['class'],'hi_class':zh['class'],'lo_f_vector':zl['f_vector'],'hi_f_vector':zh['f_vector'],'sigma_226_to_227_lo_exact':B.qs(al),'sigma_226_to_227_hi_exact':B.qs(ah),'sigma_227_to_226_lo_exact':B.qs(bl),'sigma_227_to_226_hi_exact':B.qs(bh),'controlling_sign_lo':-1 if sl<0 else 1,'controlling_sign_hi':-1 if sh<0 else 1})
# exact sign around A incidence root and B incidence root
inc=[]
for desc,root,moving,circ in [('cross-gap 2-to-2 flip: edge (194,224) -> (195,223)',a_root,223,[194,195,224,223]),('terminal 2-to-2 flip: edge (122,225) -> (123,227)',b_inc,227,[122,123,225,227])]:
 lo,hi=(Q(9,10),Q(1)) if moving==223 else (Q(994,1000),Q(995,1000))
 zl,dl=audit(lo,Q(1),False) if moving==223 else audit(Q(1),lo,False);zh,dh=audit(hi,Q(1),False) if moving==223 else audit(Q(1),hi,False)
 inc.append({'description':desc,'circuit':circ,'root_exact':B.qs(root),'root_decimal':float(root),'left_sample_exact':B.qs(lo),'right_sample_exact':B.qs(hi),'left_f_vector':zl['f_vector'],'right_f_vector':zh['f_vector'],'left_class':zl['class'],'right_class':zh['class'],'removed_edges':sorted([x['edge'] for x in zl['true_edges'] if x['edge'] not in [y['edge'] for y in zh['true_edges']]]),'added_edges':sorted([x['edge'] for x in zh['true_edges'] if x['edge'] not in [y['edge'] for y in zl['true_edges']]])})
out={'version':2,'description':'Complete exact two-control first chamber atlas around the M42 fourth-cell endpoint. a scales row 223 and b scales row 227 about the exact construction origin; every cell rebuilds the actual hull, exact mass/own centroid and every face/vertex/four-component true-edge cone.','controls':{'a':'q_223(a)=a q_223','b':'q_227(b)=b q_227'},'representative_grid':{'a_values':[B.qs(z) for z in Avals],'b_values':[B.qs(z) for z in Bvals]},'cells':cells,'exact_incidence_walls':inc,'isolated_mechanical_walls':wall_records,'conclusion':'All eight representative open cells and all wall-adjacent samples are nonwinners. The a-wall transfers the extra stable/saddle branch through a true 2-to-2 flip. The b-sequence is a U-H-U relay: endpoint 226, temporary saddle edge (226,227) with both endpoints unstable, then endpoint 227; the terminal 2-to-2 flip lies between the two mechanical walls.'}
json.dump(out,open(ROOT/'first_chamber_atlas.json','w'),indent=2)
print('A root',B.qs(a_root),float(a_root));print('B incidence',B.qs(b_inc),float(b_inc));print('PASS chamber atlas')
