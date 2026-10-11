"""Exact one-plane intersection of a retained rational physical source body."""
import argparse,json,hashlib,time
from pathlib import Path
from math import gcd,lcm
from gmpy2 import mpq
from exact_audit_vertices import check_B,dot

def audit(source,nomination,definition,out,grid):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);source=Path(source);parent=json.loads((source/'audit.json').read_text());raw=json.loads((source/'raw.json').read_text());nom=json.loads(Path(nomination).read_text());definition=json.loads(Path(definition).read_text());n=tuple(mpq(int(round(float(v)*grid)),grid) for v in nom['normal']);h=mpq(int(round(float(nom['offset'])*grid)),grid);scale=mpq(float(definition['scale']));cent=tuple(mpq(v) for v in parent['raw_centroid']);rhs=h*scale+dot(n,cent);row=n+(rhs,);den=lcm(*(int(x.denominator) for x in row));row=[int(v*den) for v in row];gg=gcd(*row);row=[v//gg for v in row];assert row[3]>0;raw={'H':raw['H']+[row]};t=time.time();B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),default=str).encode();(out/'raw.json').write_bytes(B(raw));(out/'construction.json').write_bytes(B(dict(source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),source_raw_sha256=hashlib.sha256((source/'raw.json').read_bytes()).hexdigest(),normal=n,normalized_offset=h,scale=scale,source_exact_centroid=cent,physical_cut=row,grid=grid,definition='original exact body intersect physical_cut; uniform density1')));a=check_B.run(raw);(out/'audit.json').write_bytes(B(a));su={k:a[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};su.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],seconds=time.time()-t,goal_met=a['counts']==[1,1,0] and a['weak']==[0,0,0] and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500);su['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(su,indent=2));print('EXACT_CLIP',out,{k:su[k] for k in ['V','E','F','counts','weak','C_2E','VplusEplusF','goal_met']},flush=True)
 if su['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(su,indent=2))
 return a

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('nomination');p.add_argument('definition');p.add_argument('out');p.add_argument('--grid',type=int,default=10**12);a=p.parse_args();audit(a.source,a.nomination,a.definition,a.out,a.grid)
