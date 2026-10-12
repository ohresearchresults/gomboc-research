"""Exact physical cap on the main stable carrier, after actual vertex retirement.
A documented rational reference point approximates the parent centroid only to
choose a compact rational foot. The NEW body's real homogeneous centroid and
all equilibrium/weak contacts are then independently integrated and audited.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd,lcm
import sys,json,hashlib,time
from gmpy2 import mpq
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
check_B.Q=mpq
from exact_bars_gmp import bars

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(row):
 den=lcm(*(int(v.denominator) for v in row));n=[int(v*den) for v in row];d=gcd(*n);return [v//d for v in n]
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def construct(source,out,mix=mpq(1,4),epsilon=mpq(1,10**7)):
 start=time.time();r=json.loads(source.read_text());X=[tuple(mpq(v) for v in p) for p in r['raw_vertices']];cent=tuple(mpq(v) for v in r['raw_centroid']);Y=[tuple(mpq(v)/(mpq(h)-dot(n,cent)) for v in n) for n,h in zip(r['normals'],r['offsets'])];eo=defaultdict(list)
 for f,ids in enumerate(r['faces']):
  for i,j in zip(ids,ids[1:]+ids[:1]):eo[tuple(sorted((i,j)))].append(f)
 Q=bars(Y,list(eo.values()));assert Q;f=Q[0]['root'];u=r['unstable_vertices'][0];assert r['counts'][1]==1 and u in r['faces'][f];assert len(r['faces'][f])==3,'this edge budget uses a triangular carrier'
 reference=tuple(mpq(int(round(float(v)*10**12)),10**12) for v in cent);n=tuple(mpq(v) for v in r['normals'][f]);h=mpq(r['offsets'][f]);foot=tuple(reference[k]+n[k]*(h-dot(n,reference))/dot(n,n) for k in range(3));p=tuple((1-mix)*foot[k]+mix*X[u][k]+epsilon*(foot[k]-reference[k]) for k in range(3));rows=[]
 for i,(ni,hi) in enumerate(zip(r['normals'],r['offsets'])):
  if i==f:assert dot(ni,p)>hi;continue
  assert dot(ni,p)<hi,'cap sees an additional old facet';rows.append([*ni,hi])
 ids=r['faces'][f]
 for i,j in zip(ids,ids[1:]+ids[:1]):
  nn=cross(sub(X[i],p),sub(X[j],p));hh=dot(nn,p)
  if hh<0:nn=tuple(-v for v in nn);hh=-hh
  assert hh>0 and all(dot(nn,x)<=hh for x in X);rows.append(primitive((*nn,hh)))
 H={'H':rows};out.mkdir(parents=True,exist_ok=False);(out/'H.json').write_bytes(blob(H));con=dict(parent_report=str(source),parent_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),mix=str(mix),epsilon=str(epsilon),reference_point=[str(v) for v in reference],old_volume_centroid=[str(v) for v in cent],reference_foot=[str(v) for v in foot],added_point=[str(v) for v in p],parent_main_stable_facet=f,parent_U=u,parent_main_Q=Q[0]['relative_depth_float']);(out/'construction.json').write_bytes(blob(con));rr=check_B.run(H);outX=[tuple(mpq(v) for v in x) for x in rr['raw_vertices']];assert set(outX)==set(X)|{p};assert (rr['V'],rr['E'],rr['F'])==(r['V']+1,r['E']+3,r['F']+2);(out/'audit.json').write_bytes(blob(rr));oldU=outX.index(X[u]);newS=[i for i in rr['stable_face_ids'] if rr['active_input_indices'][i]>=r['F']-1]
 summary={k:rr[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C_2E=2*rr['E'],V_plus_E_plus_F=rr['V']+rr['E']+rr['F'],old_U_index=oldU,new_child_stable_facets=newS,children_contain_old_U=[oldU in rr['faces'][i] for i in newS],seconds=time.time()-start);summary['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()};(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_DETACHED_CAP',summary,flush=True)
 return rr
if __name__=='__main__':
 source=ROOT/'artifacts/retire_current/exact_concave_checkpoint1/exact_E245/audit.json';out=ROOT/'artifacts/detached_main_cap/t025_e7';construct(source,out)
