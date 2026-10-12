"""Certified full mechanics of the unique admissible algebraic mass root.
Independent boundary integration checks all mass polynomial coefficients.
Usage: python -B -S algebraic_census.py MASS_JSON QUARTIC_PROOF C592_PROOF RATIONAL_OPPOSITE OUT
"""
import json,sys
from pathlib import Path
from fractions import Fraction as Q
import mass_chamber as mc
from quartic_isolate import I
assert __debug__
sys.set_int_max_str_digits(0)
GRID=10**24

def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(x*t for x in a)
def inner(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def cover(x):
 x=Q(x);return I(Q((x*GRID).__floor__(),GRID),Q((x*GRID).__ceil__(),GRID))
def classify(vals):
 signs=[x.sign() for x in vals]
 if all(x==1 for x in signs):return 1
 if -1 in signs:return -1
 raise AssertionError('Unresolved interval sign in a complete equilibrium test')

def run(mp,rp,base,rat,out):
 data=json.loads(mp.read_bytes());proof=json.loads(rp.read_bytes())
 assert proof['input_sha256']==mc.SHA(mp.read_bytes())
 roots=[x for x in proof['roots'] if x['in_selected_visibility_chamber']]
 assert len(roots)==1 and roots[0]['actual_centroid_equals_target_exactly']
 R=json.loads((rat/'A.json').read_bytes());assert mc.SHA((rat/'A.json').read_bytes())=='8ee12742068e4246b3b7daf688703b3ce6f1c9803202a7d05f96e3ad8806ac21'
 source=json.loads((base/'A.json').read_bytes());assert mc.SHA((base/'A.json').read_bytes())==data['C592_A_sha256']
 cfg=json.loads((rat/'SELECTORS.json').read_bytes())
 assert cfg['visible_facets']==data['visible_facets']
 raw=[tuple(map(Q,row)) for row in R['raw_vertices']]
 old=[tuple(map(Q,row)) for row in source['raw_vertices']]
 c0=tuple(map(Q,data['target_centroid']))
 new=117;assert new==R['V']-1 and raw[new] not in old
 assert all(x in old for i,x in enumerate(raw) if i!=new)
 box=[I(*v) for v in roots[0]['point_box']]
 assert box[0].a>max(x[0] for x in old)
 # Independent integration over the ACTUAL NEW boundary, with different fans.
 v0=Q(0);vk=(Q(0),)*3;m0=(Q(0),)*3;T=[[Q(0)]*3 for _ in range(3)]
 for cy in R['faces']:
  cy=cy[1:]+cy[:1]
  for j in range(1,len(cy)-1):
   tri=[cy[0],cy[j],cy[j+1]]
   if new not in tri:
    u,v,w=[raw[i] for i in tri];z=mc.dot(u,mc.cross(v,w))/6
    assert z>0;v0+=z;m0=mc.add(m0,mc.mul(z/4,mc.add(mc.add(u,v),w)))
   else:
    while tri[0]!=new:tri=tri[1:]+tri[:1]
    b,c=[raw[i] for i in tri[1:]];h=mc.mul(Q(1,6),mc.cross(b,c));vk=mc.add(vk,h)
    for i in range(3):
     for j2 in range(3):T[i][j2]+=(b[i]+c[i])*h[j2]/4
 assert v0==Q(data['body_volume'])+Q(data['chamber_k0'])
 assert vk==tuple(map(Q,data['chamber_k']))
 assert m0==mc.add(tuple(map(Q,data['body_first_moments'])),tuple(map(Q,data['chamber_b0'])))
 BB=[list(map(Q,row)) for row in data['chamber_B']]
 assert T==[[BB[i][j]+(Q(data['chamber_k0'])/4 if i==j else 0) for j in range(3)] for i in range(3)]
 print('INDEPENDENT_NEW_BOUNDARY_ALL_MASS_COEFFICIENTS_MATCH',flush=True)
 X=[tuple(cover(x-c) for x,c in zip(p,c0)) for p in raw]
 X[new]=tuple(box[i]-I(c0[i]) for i in range(3))
 # Round the already certified new-point-centred interval outward to short fractions.
 X[new]=tuple(I(Q((x.a*GRID).__floor__(),GRID),Q((x.b*GRID).__ceil__(),GRID)) for x in X[new])
 normals=[]
 for fi,cy in enumerate(R['faces']):
  if new in cy:
   assert len(cy)==3
   n=cross(minus(X[cy[1]],X[cy[0]]),minus(X[cy[2]],X[cy[0]]))
  else:
   # This maximal facet is unchanged. Scaling the integer normal is harmless.
   nr=R['normals'][fi];div=max(map(abs,nr));n=tuple(cover(Q(v,div)) for v in nr)
  assert inner(n,X[cy[0]]).a>0
  normals.append(n)
 S=[];Fsigns=[];edgefaces={tuple(e):[] for e in R['edges']}
 for fi,cy in enumerate(R['faces']):
  vals=[inner(normals[fi],cross(X[i],minus(X[j],X[i]))) for i,j in zip(cy,cy[1:]+cy[:1])]
  cl=classify(vals);Fsigns.append([v.sign() for v in vals])
  if cl==1:S.append(fi)
  for i,j in zip(cy,cy[1:]+cy[:1]):edgefaces[tuple(sorted((i,j)))].append(fi)
 adjacency=[set() for _ in X]
 for i,j in R['edges']:adjacency[i].add(j);adjacency[j].add(i)
 U=[];witnesses=[]
 for i in range(len(X)):
  local=[inner(X[i],minus(X[j],X[i])) for j in adjacency[i]]
  isU=all(v.b<0 for v in local);isNotU=any(v.a>0 for v in local);assert isU!=isNotU
  alltests={j:inner(X[i],minus(X[j],X[i])) for j in range(len(X)) if j!=i}
  if isU:
   assert all(v.b<0 for v in alltests.values());U.append(i);witnesses.append(-1)
  else:
   good=[j for j,v in alltests.items() if v.a>0];assert good;witnesses.append(min(good))
 H=[];Esigns=[]
 for i,j in R['edges']:
  ff=edgefaces[(i,j)];assert len(ff)==2;n,m=[normals[f] for f in ff]
  e=minus(X[j],X[i]);ee=inner(e,e);assert ee.a>0;ze=inner(X[i],e)
  p=minus(scale(X[i],ee),scale(e,ze));nn=inner(n,n);mm=inner(m,m);nm=inner(n,m)
  determinant=nn*mm-nm*nm;assert determinant.a>0
  gram=[-ze,ee+ze,mm*inner(p,n)-nm*inner(p,m),nn*inner(p,m)-nm*inner(p,n)]
  axis=cross(n,m)
  cramer=[-ze,ee+ze,inner(cross(p,m),axis),inner(cross(n,p),axis)]
  cl=classify(gram);assert cl==classify(cramer)
  Esigns.append([i,j,*[x.sign() for x in gram]])
  if cl==1:H.append([i,j])
 assert [len(S),len(U),len(H)]==[7,2,7]
 assert S==R['stable_face_ids'] and U==R['unstable_vertices'] and H==R['saddle_edges']
 result=dict(identity='COORD_C592_OPPOSITE_ALGEBRAIC_MASS_C486',V_E_F=[118,243,127],C=486,counts=[len(S),len(U),len(H)],weak=[0,0,0],stable_faces=S,unstable_vertices=U,saddles=H,own_centroid='exactly the C602 parent centroid',maximum_original_coordinate_enclosure_grid=GRID,new_point_box_source_sha256=mc.SHA(rp.read_bytes()),mass_polynomial_input_sha256=mc.SHA(mp.read_bytes()),independent_boundary_mass_coefficients_agree=True,full_combinatorics_inherited_from_strict_visibility_chamber=True,face_interval_signs=Fsigns,vertex_exit_witnesses=witnesses,edge_interval_signs=Esigns,interval_sign_zero_means_unresolved_component_not_equilibrium=True,all_edge_Gram_and_Cramer_classifications_agree=True,not_a_winner=True)
 out.write_bytes(mc.B(result));print('EXACT_ALGEBRAIC_OPPOSITE_C486_OWN727_COMPLETE_CENSUS_PASS',len(mc.B(result)),mc.SHA(mc.B(result)),flush=True)
if __name__=='__main__':run(*map(Path,sys.argv[1:]))
