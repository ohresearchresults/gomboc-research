"""Exact-rational proposal from the literal DOUBLE38_69 numerical checkpoint.
No unexecuted edge contraction is inferred from its positive epsilon.
"""
import sys,json,base64,struct,hashlib
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent'))
from blowup_edge import Model
from numeric import snapped,recover,mechanics
from atlas_opt import Atlas

def main(out):
 cp=json.loads((R/'parent/experiments/FINITE_FAILURES.json').read_text())['DOUBLE38_69'];b=base64.b85decode(cp['u_ieee754_big_endian_base85']);assert hashlib.sha256(b).hexdigest()==cp['u_byte_sha256'];u=np.array(struct.unpack('>'+'d'*(len(b)//8),b))
 d=json.loads((R/'parent/BASIN69_96/GENERATOR.json').read_text());fs=json.loads((R/'parent/BASIN69_96/faces.json').read_text());m=Model(d,fs,cp['a_node'],cp['b_node']);s=m.state(u,False);print('BEFORE',mechanics(s['q'],fs,P=s['P'],tol=1e-13),flush=True);print('GAPS',s['gaps'][19,50],s['gaps'][26,113],flush=True)
 d['controls']=np.rint(s['X']*d['grid']).astype(np.int64).tolist();dd,ff=snapped(d,fs,26,19,113);X=recover(d);p=np.linalg.solve(X[[50,51,52]],np.ones(3));q=X[113]+((1-X[113]@p)/(p@p))*p;dd['controls'][113]=np.rint(q*dd['grid']).astype(np.int64).tolist()
 out=Path(out);out.mkdir(parents=True,exist_ok=False)
 for n,x in [('GENERATOR.json',dd),('faces.json',ff),('DOUBLE_ROUNDED.json',d)]: (out/n).write_text(json.dumps(x,sort_keys=True,separators=(',',':')))
 nm=Atlas(dd,ff);ss=nm.state(nm.u0,False);rep=mechanics(ss['q'],ff,P=ss['P'],tol=1e-13);(out/'NUMERICAL.json').write_text(json.dumps(rep));print('AFTER',rep,flush=True)
if __name__=='__main__':main(sys.argv[1])
