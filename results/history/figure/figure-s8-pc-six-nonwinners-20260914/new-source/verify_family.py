"""Exact audit of support-deletion endpoints, using the persisted independent S8 auditors.
Stages are separate to support bounded executions. Every stage checks source hashes.
All floating optimization is excluded. INPUT contains the frozen GENERATOR.json.
"""
import argparse,json,sys,hashlib
from pathlib import Path
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'source'))
import REPLAY,RECONSTRUCT,check_A,check_B,centred_mass,measure

def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def put(p,x):p.write_bytes(canon(x))
def meta(p):b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def valid(r):
 assert r['weak']==[0,0,0]
 assert r['centred_centroid']==r['centred_first_moments']==[0,0,0]
 assert all(r[k]==0 for k in ('face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'))
 assert r['V']-r['E']+r['F']==2
 assert len(r['edges'])==r['E'] and r['edge_primitive_count']==4*r['E']
 assert r['active_input_indices']==list(range(r['F']))

def main(a):
 REPLAY.sources();out=a.out
 if a.stage=='A':
  out.mkdir(parents=True,exist_ok=False);d=json.loads((a.input/'GENERATOR.json').read_text());ids=d.get('active_ids',list(range(d['n_supports'])))
  raw=RECONSTRUCT.recover(d);raw={'H':[raw['H'][i] for i in ids]};put(out/'GENERATOR.json',d);put(out/'ACTIVE_IDS.json',ids);put(out/'raw.json',raw)
  r=check_A.run(raw);valid(r);put(out/'A.json',r)
 elif a.stage=='B':
  r=check_B.run(json.loads((out/'raw.json').read_text()));valid(r);put(out/'B.json',r);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
 elif a.stage=='MASS':
  r=json.loads((out/'A.json').read_text());valid(r);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes();put(out/'CENTRED_MASS.json',centred_mass.run(r));put(out/'STATS.json',measure.run(r,json.loads((out/'raw.json').read_text())))
 elif a.stage=='FINISH':
  r=json.loads((out/'A.json').read_text());valid(r);assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
  receipt=dict(status='EXACT_DELETION_FAMILY_TWO_AUDITS_THIRD_MASS_PASS',VEF=[r[k] for k in ('V','E','F')],C=2*r['E'],counts=r['counts'],weak=r['weak'],accepted_gomboc=r['counts']==[1,1,0],stable=r['stable_face_ids'],unstable=r['unstable_vertices'],saddle=r['saddle_edges'],files={n:meta(out/n) for n in ('GENERATOR.json','ACTIVE_IDS.json','raw.json','A.json','B.json','CENTRED_MASS.json','STATS.json')})
  put(out/'RECEIPT.json',receipt)
 else:raise ValueError(a.stage)
 REPLAY.sources();print('EXACT_DELETION_FAMILY',a.stage,[r[k] for k in ('V','E','F')],r['counts'],r['weak'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['A','B','MASS','FINISH'],required=True);main(p.parse_args())
