"""Run two independently implemented exact maximal-complex/mechanical audits.
No numerical results or claimed f-vector enter geometry reconstruction.
"""
import sys,json,hashlib,argparse,time
from pathlib import Path
if not __debug__:raise RuntimeError('Assertions required')
sys.set_int_max_str_digits(0);R=Path(__file__).resolve().parent
sys.path[:0]=[str(R/'parent/parent'),str(R/'parent')]
import RECONSTRUCT,check_A,check_B,centred_mass,measure626

def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def run(a):
 a.out.mkdir(parents=True,exist_ok=False);data=a.generator.read_bytes();raw=RECONSTRUCT.recover(json.loads(data));rb=canon(raw);(a.out/'GENERATOR.json').write_bytes(data);(a.out/'raw.json').write_bytes(rb)
 recs=[];receipts=[]
 for label,module in [('A',check_A),('B',check_B)]:
  t=time.perf_counter();z=module.run(raw);bz=canon(z);(a.out/(label+'.json')).write_bytes(bz);recs.append(z);receipts.append(dict(engine=label,seconds=time.perf_counter()-t,bytes=len(bz),sha256=sha(bz)));print('FULL_EXACT',label,z['V'],z['E'],z['F'],z['counts'],z['weak'],flush=True)
 assert recs[0]==recs[1];z=recs[0];st=measure626.run(z,raw);(a.out/'STATS.json').write_bytes(canon(st));print('STATS', {k:v for k,v in st.items() if k not in ['primal_forest','dual_forest']},flush=True)
 cm=centred_mass.run(z);(a.out/'CENTRED_MASS.json').write_bytes(canon(cm))
 fixtures=[]
 for name,H,c,w in [('tetra',[[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),('weak_prism',[[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
  x=check_A.run({'H':H});y=check_B.run({'H':H});assert x==y and x['counts']==c and x['weak']==w;fixtures.append(dict(name=name,counts=c,weak=w))
 rec=dict(status='BQ13_NEW_TWO_FULL_EXACT_AND_CENTRED_MASS_PASS',generator_sha256=sha(data),generator_bytes=len(data),raw_sha256=sha(rb),raw_bytes=len(rb),engines=receipts,VEF=[z[k] for k in ['V','E','F']],counts=z['counts'],weak=z['weak'],S=z['stable_face_ids'],U=z['unstable_vertices'],H=z['saddle_edges'],centred_mass=cm,fixtures=fixtures,python=sys.version)
 (a.out/'RECEIPT.json').write_bytes(canon(rec));print(rec['status'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--generator',type=Path,required=True);p.add_argument('--out',type=Path,required=True);run(p.parse_args())
