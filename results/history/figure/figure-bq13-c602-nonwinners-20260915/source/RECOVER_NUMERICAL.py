"""Read back a stored positive-epsilon numerical chart, never promote it as a contraction."""
import json,sys,argparse
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R))
from leaf_noinflate import Leaf
from root_absorb_noinflate import Absorb
from numeric import mechanics

def main(a):
 e=json.loads((R/'EXPECTED.json').read_text())['TRI9_TRIANGLE9_STEP8'];base=R/e['path'];d=json.loads((base/'GENERATOR.json').read_text());fs=json.loads((base/'faces.json').read_text())
 folder='C600_noinflate'if a.object=='C600_APPROACH'else'root602_noinflate'
 cp=json.loads((R/folder/'CHECKPOINT.json').read_text());u=np.array([float.fromhex(v)for v in cp['u_hex']]);m=Leaf(d,fs,13,28,115,True)if a.object=='C600_APPROACH'else Absorb(d,fs,141)
 floors=json.loads((R/folder/'fixed_floors.json').read_text());assert np.array_equal(m.floor,np.array(floors));s=m.state(u,False);rr=mechanics(s['q'],fs,P=s['P'],tol=1e-13)
 report=dict(status='BQ13_POSITIVE_EPSILON_NUMERICAL_CHECKPOINT_READBACK',object=a.object,epsilon=float(m.epsilon(u)),numerical_census=rr,not_an_exact_contraction=True,not_a_winner=True)
 assert report['epsilon']>0
 a.out.mkdir(parents=True,exist_ok=False);(a.out/'READBACK.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':')));print(report,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--object',choices=['C600_APPROACH','ROOT_ABSORPTION'],required=True);p.add_argument('--out',type=Path,required=True);main(p.parse_args())
