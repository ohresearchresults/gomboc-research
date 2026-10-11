"""Exact convex hull of a retained rational polyhedron and one literal point.
Both hull inclusions, true maximal faces, mass and all contact signs are checked.
"""
import argparse,json,hashlib,time
from pathlib import Path
from math import lcm,gcd
from gmpy2 import mpq
from exact_audit_vertices import check_B,dot,cross,sub

def audit(source,nomination,definition,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);source=Path(source);a=json.loads((source/'audit.json').read_text());nom=json.loads(Path(nomination).read_text());de=json.loads(Path(definition).read_text());P=[tuple(mpq(v)for v in x)for x in a['raw_vertices']];g=tuple(mpq(v)for v in a['raw_centroid']);scale=mpq(float(de['scale']));point=tuple(g[k]+scale*mpq(float(nom['point'][k]))for k in range(3));N=[tuple(mpq(v)for v in row)for row in a['normals']];h=[mpq(v)for v in a['offsets']];visible=[dot(n,point)>hh for n,hh in zip(N,h)];owners={tuple(e):[]for e in a['edges']}
 for f,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners[tuple(sorted((i,j)))].append(f)
 rows=set()
 def add(n,b):
  row=tuple(n)+(b,);den=lcm(*(int(v.denominator)for v in row));r=tuple(int(v*den)for v in row);d=gcd(*r);rows.add(tuple(v//d for v in r))
 for f,(n,b)in enumerate(zip(N,h)):
  if not visible[f]:add(n,b)
 for (i,j),adj in owners.items():
  if visible[adj[0]]==visible[adj[1]]:continue
  n=cross(sub(P[j],P[i]),sub(point,P[i]));b=dot(n,P[i]);assert b!=0
  if b<0:n=tuple(-v for v in n);b=-b
  add(n,b)
 points=P+[point];assert all(dot(r[:3],x)<=r[3]for r in rows for x in points);B=lambda o:json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode();raw=dict(H=sorted(rows));(out/'raw.json').write_bytes(B(raw));(out/'coordinates.json').write_bytes(B(dict(source_vertices=P,new_vertex=point)));(out/'construction.json').write_bytes(B(dict(source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),formula='convex hull(exact source polyhedron union new_vertex), uniform density1',scale=scale,source_centroid=g,normalized_literal_dyadic_point=[str(mpq(float(v)))for v in nom['point']],visible_source_facets=[i for i,v in enumerate(visible)if v])));t=time.time();r=check_B.run(raw);assert {tuple(mpq(v)for v in x)for x in r['raw_vertices']}<=set(points);(out/'audit.json').write_bytes(B(r));su={k:r[k]for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};su.update(C_2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],goal_met=r['counts']==[1,1,0]and r['weak']==[0,0,0]and 34<=2*r['E']<500 and r['V']+r['E']+r['F']<500,seconds=time.time()-t);su['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(su,indent=2));print('EXACT_GENERAL_CAP',out,{k:su[k]for k in ['V','E','F','counts','weak','C_2E','VplusEplusF','goal_met','seconds']},flush=True)
 if su['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(su,indent=2))
 return r

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('nomination');p.add_argument('definition');p.add_argument('out');a=p.parse_args();audit(a.source,a.nomination,a.definition,a.out)
