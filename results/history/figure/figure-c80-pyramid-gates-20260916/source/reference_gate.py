"""Exact C80 reference-centre census and uniform centroid slab obstruction.
The slab theorem concerns any convex uniformly filled 3-polytope with the same
specified extrema; it excludes this one reference centre, not its entire chamber.
"""
import argparse,hashlib,json,sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
EXPECTED='f17bb48815e8ff86697936d33af34e8e28170808674e9149dbae23c5228a19f7'
REF=[7695683,168054,-75622586]
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sign(x):return (x>0)-(x<0)
def census(A,centre):
 P=[tuple(map(F,p)) for p in A['raw_vertices']];X=[sub(p,centre) for p in P]
 N=[tuple(map(F,n)) for n in A['normals']];faces=A['faces'];owners=defaultdict(list)
 assert all(dot(n,centre)<F(h) for n,h in zip(N,A['offsets']))
 stable=[];sw=[];unstable=[];uw=[];saddles=[];hw=[];fs=[];vs=[];es=[]
 for f,cy in enumerate(faces):
  ss=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   owners[tuple(sorted((i,j)))].append(f);ss.append(sign(dot(N[f],cross(X[i],sub(P[j],P[i])))))
  fs.append(ss)
  if min(ss)>0:stable.append(f)
  elif min(ss)==0:sw.append(f)
 for i,x in enumerate(X):
  s=sign(max(dot(x,sub(p,P[i])) for j,p in enumerate(P) if j!=i));vs.append(s)
  if s<0:unstable.append(i)
  elif s==0:uw.append(i)
 assert sorted(owners)==[tuple(e) for e in A['edges']]
 for (i,j),ff in sorted(owners.items()):
  assert len(ff)==2;e=sub(P[j],P[i]);ee=dot(e,e);xe=dot(X[i],e)
  q=tuple(x-ei*xe/ee for x,ei in zip(X[i],e));n,m=[N[f] for f in ff]
  nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);assert nn*mm-nm*nm>0
  ss=list(map(sign,[-xe,ee+xe,dot(q,tuple(mm*a-nm*b for a,b in zip(n,m))),dot(q,tuple(nn*b-nm*a for a,b in zip(n,m)))]));es.append([i,j,*ss])
  if min(ss)>0:saddles.append([i,j])
  elif min(ss)==0:hw.append([i,j])
 return {'counts':[len(stable),len(unstable),len(saddles)],'weak':[len(sw),len(uw),len(hw)],'stable':stable,'unstable':unstable,'saddles':saddles,'weak_faces':sw,'weak_vertices':uw,'weak_edges':hw,'face_signs':fs,'vertex_signs':vs,'edge_signs':es}
def main():
 p=argparse.ArgumentParser();p.add_argument('audit');p.add_argument('out');args=p.parse_args();b=Path(args.audit).read_bytes();assert hashlib.sha256(b).hexdigest()==EXPECTED
 A=json.loads(b);g=list(map(F,A['raw_centroid']));own=census(A,g);ref=census(A,list(map(F,REF)))
 assert own['counts']==A['counts']==[2,1,1] and own['weak']==A['weak']==[0,0,0]
 assert own['face_signs']==A['face_signs'] and own['vertex_signs']==[row[1] for row in A['vertex_max_escape_signs']] and own['edge_signs']==A['edge_signs']
 assert ref['counts']==[1,1,0] and ref['weak']==[0,0,0]
 V=F(A['ordinary_volume']);M=list(map(F,A['raw_first_moments']));residual=[m-V*r for m,r in zip(M,REF)];assert any(residual)
 P=[tuple(map(F,p)) for p in A['raw_vertices']];lo=min(v[2] for v in P);hi=max(v[2] for v in P);lower=(3*lo+hi)/4;upper=(lo+3*hi)/4
 assert lower<=g[2]<=upper and F(REF[2])<lower
 # General proof: cone a triangulated convex boundary from a vertex at maximum
 # height. Every positive tetrahedron has mean height >=(maximum+3*minimum)/4.
 # Its positive volume-weighted average gives the lower bound. Cone from a
 # minimum vertex for the upper bound. This holds independently of this census.
 base=F(227941);apex=F(-4558809);depth=base-apex
 assert base-g[1]==depth/4 and base-F(REF[1])==59887
 result={'status':'EXACT_C80_REFERENCE110_AND_FILLED_CENTROID_SLAB_OBSTRUCTION_PASS','source_audit_sha256':EXPECTED,'reference_centre':REF,'reference_census':ref,'own_census':own,'filled_first_moments_about_reference':list(map(str,residual)),'z_extrema':list(map(str,[lo,hi])),'allowed_uniform_centroid_z':list(map(str,[lower,upper])),'reference_z_below_allowed_lower_by':str(lower-REF[2]),'reference_fractional_depth':str((base-REF[1])/depth),'own_fractional_depth':'1/4','scope':'This specified reference110 point cannot be the uniform filled centroid of ANY convex polytope retaining these z extrema; no whole-chamber exclusion.'}
 out=Path(args.out);out.mkdir(parents=True,exist_ok=False);f=out/'REFERENCE_GATE.json';f.write_bytes(enc(result));print(result['status']);print('own',own['counts'],own['weak'],'reference',ref['counts'],ref['weak']);print('reference roots',ref['stable'],ref['unstable']);print('z bounds',lower,upper,'target',REF[2]);print(f.name,f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest())
if __name__=='__main__':main()
