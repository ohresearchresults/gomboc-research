"""Read back two literal numerical regular-chart checkpoints, not new exact solids."""
import json,sys,argparse,hashlib,base64,struct
from pathlib import Path
R=Path(__file__).resolve().parent
C=lambda v:json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def recover(name,out):
 import numpy as np
 from blowup_edge import Model
 from numeric import mechanics
 cases=json.loads((R/'experiments/FINITE_FAILURES.json').read_text());x=cases[name]
 out.mkdir(parents=True,exist_ok=False)
 raw=base64.b85decode(x['u_ieee754_big_endian_base85']);assert hashlib.sha256(raw).hexdigest()==x['u_byte_sha256'];assert len(raw)%8==0
 u=np.array(struct.unpack('>'+'d'*(len(raw)//8),raw))
 d=json.loads((R/x['source']/'GENERATOR.json').read_text());fs=json.loads((R/x['source']/'faces.json').read_text());m=Model(d,fs,x['a_node'],x['b_node']);assert len(u)==m.np;s=m.state(u,False)
 (out/'CHECKPOINT.json').write_bytes(C(x));np.savez(out/'END.npz',u=u);rep=mechanics(s['q'],fs,P=s['P'],tol=1e-13);rep['epsilon']=float(m.epsilon(u));(out/'NUMERICAL.json').write_bytes(C(rep));print(name,'REGULAR_NUMERICAL_NOT_FINITE_CONTACT',rep['epsilon'],rep['counts']);return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('name',choices=['FULLBLOW','DOUBLE38_69']);p.add_argument('--out',type=Path,required=True);a=p.parse_args();recover(a.name,a.out)
