"""Exact nonhomothetic section body with one explicitly released physical vertex."""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from exact_section_audit import audit as audit_base
from detach_stable import audit_points

def audit(source,out):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);d=np.load(source);index=int(d['released_vertex']);offset=[mpq(float(v)) for v in d['released_offset']];audit_base(source,out/'base');X=[tuple(mpq(v) for v in row) for row in json.loads((out/'base/coordinates.json').read_text())['points']];X[index]=tuple(a+b for a,b in zip(X[index],offset));mean=tuple(sum(p[j] for p in X)/len(X) for j in range(3));X=[tuple(v-mean[j] for j,v in enumerate(row)) for row in X];meta=dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),physical_base_coordinates='base/coordinates.json',released_vertex=index,exact_physical_offset=list(map(str,offset)),translation_after_perturbation=list(map(str,mean)),density=1)
 rep=audit_points(X,out/'physical',meta);summary=json.loads((out/'physical/summary.json').read_text());summary.update(C_2E=2*rep['E'],VplusEplusF=rep['V']+rep['E']+rep['F'],goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500 and rep['V']+rep['E']+rep['F']<500);(out/'summary.json').write_text(json.dumps(summary,indent=2));print('EXACT_HYBRID',out,{k:summary[k] for k in ['V','E','F','C_2E','VplusEplusF','counts','weak','goal_met']},flush=True)
 if summary['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(summary,indent=2))
 return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');a=p.parse_args();audit(a.input,a.out)
