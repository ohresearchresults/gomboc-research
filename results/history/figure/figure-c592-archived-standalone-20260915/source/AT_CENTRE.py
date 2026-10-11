"""Exact all-feature census at a specified interior reference centre.

Geometry is a previously independently certified maximal complex.  These results
are explicitly reference-centre classifications, not claims about density or mass.
Two algebraically distinct edge-cone formulations are compared at every edge.
"""
import json,math,sys
from fractions import Fraction as F
from pathlib import Path
from BUILD import dot,cross,add,sub,mul,homogeneous,canon,encode
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def census(z,centre):
 X=[tuple(map(F,p)) for p in z['raw_vertices']];g=tuple(map(F,centre));N=[tuple(n) for n in z['normals']];offset=z['offsets'];faces=z['faces']
 C=math.lcm(*(x.denominator for x in g));M=tuple(int(x*C) for x in g);HP=[homogeneous(p) for p in X];bs=[p[3] for p in HP];aa=[p[:3] for p in HP];zz=[sub(mul(C,a),mul(b,M)) for a,b in zip(aa,bs)]
 def edge(i,j):return sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]))
 def sign(x):return (x>0)-(x<0)
 E={};adj=[set() for p in X]
 for fi,cy in enumerate(faces):
  assert offset[fi]*C>dot(N[fi],M)
  for i,j in zip(cy,cy[1:]+cy[:1]):E.setdefault(tuple(sorted((i,j))),[]).append(fi);adj[i].add(j);adj[j].add(i)
 assert [list(e) for e in sorted(E)]==z['edges'] and all(len(v)==2 for v in E.values())
 sf=[];sw=[];uv=[];uw=[];hs=[];hw=[];fs=[];vs=[];es=[]
 for fi,cy in enumerate(faces):
  sg=[sign(dot(N[fi],cross(zz[i],edge(i,j)))) for i,j in zip(cy,cy[1:]+cy[:1])];fs.append(sg)
  if min(sg)>0:sf.append(fi)
  elif min(sg)==0:sw.append(fi)
 for i in range(len(X)):
  signs=[[j,sign(dot(zz[i],edge(i,j)))] for j in sorted(adj[i])];vs.append(signs);m=max(s for j,s in signs)
  if m<0:uv.append(i)
  elif m==0:uw.append(i)
 for (i,j),pair in sorted(E.items()):
  e=edge(i,j);ee=dot(e,e);ze=dot(zz[i],e);p=sub(mul(ee,zz[i]),mul(ze,e));n,m=[N[k] for k in pair];d=cross(n,m)
  vals=[-ze*bs[j],C*ee+ze*bs[j],dot(cross(p,m),d),dot(cross(n,p),d)]
  other=[dot(p,sub(mul(dot(m,m),n),mul(dot(n,m),m))),dot(p,sub(mul(dot(n,n),m),mul(dot(n,m),n)))]
  assert vals[2:]==other
  sg=[sign(v) for v in vals];es.append([i,j,*sg])
  if min(sg)>0:hs.append([i,j])
  elif min(sg)==0:hw.append([i,j])
 assert len(sf)+len(uv)-len(hs)==2 or sw or uw or hw
 return encode(dict(reference_centre=g,counts=[len(sf),len(uv),len(hs)],weak=[len(sw),len(uw),len(hw)],S=sf,U=uv,H=hs,weak_faces=sw,weak_vertices=uw,weak_edges=hw,face_signs=fs,vertex_neighbor_signs=vs,edge_signs=es,scope='Fixed maximal complex at explicitly supplied reference centre; not a uniform-volume-centroid claim.'))

def main():
 z=json.loads((ROOT/'A.json').read_text());b=json.loads((ROOT/'BUILD_REPORT.json').read_text());c=b['old_centroid'];out=census(z,c)
 own=census(z,z['raw_centroid']);assert own['counts']==z['counts'] and own['weak']==z['weak'];assert own['S']==z['stable_face_ids'] and own['U']==z['unstable_vertices'] and own['H']==z['saddle_edges'];assert own['face_signs']==z['face_signs'] and own['edge_signs']==z['edge_signs']
 (ROOT/'REFERENCE_CENSUS.json').write_bytes(canon(out))
 print('COORD_C592_REFERENCE_FULL_CENSUS',out['counts'],out['weak'],flush=True)
 pp=json.loads((ROOT/'HULL_COMPLEX.json').read_text())['vertices'];index={tuple(map(F,p)):i for i,p in enumerate(pp)};ids=[index[tuple(map(F,p))] for p in z['raw_vertices']]
 print('OWN_U_INPUT_IDS',[ids[i] for i in own['U']]);print('REFERENCE_U_INPUT_IDS',[ids[i] for i in out['U']])
 print('REFERENCE_S',out['S'],'REFERENCE_H_INPUT_IDS',[[ids[i],ids[j]] for i,j in out['H']])

if __name__=='__main__':main()
