"""Finite projection to the exact collapsed chart from the literal blow-up checkpoint."""
import sys,json,argparse
from pathlib import Path
import numpy as np
from blowup_edge import Model
from atlas_opt import Atlas
from numeric import mechanics
R=Path(__file__).resolve().parent

def construct(t=0.):
 d=json.loads((R/'C628_WINNER/GENERATOR.json').read_text());fs=json.loads((R/'C628_WINNER/faces.json').read_text())
 cp=json.loads((R/'experiments/BLOWUP_CHECKPOINT.json').read_text());m=Model(d,fs,cp['a_node'],cp['b_node']);u=np.array([float.fromhex(x) for x in cp['u_hex']]);X=m.chart(u,False);p=(1-t)*X[m.aa]+t*X[m.bb]
 for j,(i,k) in enumerate(m.free):
  if i==m.aa:u[j]=p[k]/m.scale[j]
 u[m.epindex]=0.
 dd,ff=m.endpoint(u)
 return dd,ff
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--t',type=float,default=0.);p.add_argument('--out',type=Path,required=True);a=p.parse_args();dd,ff=construct(a.t);a.out.mkdir(exist_ok=True,parents=True);(a.out/'GENERATOR.json').write_text(json.dumps(dd,sort_keys=True,separators=(',',':')));(a.out/'faces.json').write_text(json.dumps(ff,separators=(',',':')))
 m=Atlas(dd,ff);s=m.state(m.u0,False);print(mechanics(s['q'],ff,P=s['P'],tol=1e-13));print('bad',np.flatnonzero(s['vals']<0).tolist())
