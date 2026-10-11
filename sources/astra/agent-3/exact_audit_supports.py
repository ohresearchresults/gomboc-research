"""Freeze literal physical supports on a rational grid and run complete exact audit."""
from pathlib import Path
import argparse,json,time,hashlib
import numpy as np
from exact_audit_vertices import check_B

def audit(path,out,D):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);Q=np.load(path);H=[[int(round(float(v)*D)) for v in p]+[D] for p in Q];raw={'H':H};B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode();(out/'raw.json').write_bytes(B(raw));(out/'construction.json').write_bytes(B(dict(source=str(path),grid=D,inequalities='sum(H[i][j]*x[j],j=0..2)<=H[i][3]',density=1,rounding='ties-to-even after binary64 multiplication by grid')));start=time.time();rep=check_B.run(raw);(out/'audit.json').write_bytes(B(rep));r={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};r.update(C=2*rep['E'],seconds=time.time()-start,goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500);r['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(r,indent=2));print('EXACT_SUPPORT',out,r,flush=True)
 if r['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(r,indent=2))
 return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--grid',type=int,default=10**10);a=p.parse_args();audit(a.input,a.out,a.grid)
