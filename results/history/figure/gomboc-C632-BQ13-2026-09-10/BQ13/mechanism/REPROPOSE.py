"""Optional deterministic-in-this-environment replay of the successful cap proposal.
Exact acceptance depends only on the frozen rational object and ../REPLAY.py.
A different numerical-library proposal is never substituted for that object.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys,json,hashlib
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R),str(R/'parent_sources')]
from numeric import recover,vertices,topology,mechanics
from contact_chart import make_chart
from spiral_cap import construct
import mass_close

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 g=json.loads((R/'qp622a/LATEST.json').read_text())
 fs=json.loads((R/'C622_chart/faces.json').read_text())
 q=recover(g)[:135];P=vertices(q,topology(fs)[0]);c=np.array(mechanics(q,fs,P=P)['centroid'])
 (own,reference,qn,pn,fn),details=construct(q,P,fs,c,1/3,2/3,(0.,0.))
 owners,_=topology(fn);ids=[98]+[i for i,o in enumerate(owners) if len(o)>3 and i!=98]
 seed,_=make_chart(qn,pn[ids],[owners[i] for i in ids],10**14,'supports')
 original=json.loads((R/'cap632_seed/GENERATOR.json').read_text())
 assert canonical(seed)==canonical(original),'Numerical proposal changed; the frozen exact winner is unchanged.'
 assert fn==json.loads((R/'cap632_seed/faces.json').read_text())
 assert list(c)==json.loads((R/'cap632_seed/reference.json').read_text())
 print('CAP_SEED_REPROPOSED_IDENTICALLY',details,own['counts'],reference['counts'],flush=True)
 out=R/'reproposed'
 if out.exists():raise FileExistsError(str(out))
 mass_close.run(str(out),seconds=24,fraction=1.,reserve=.2)
 got=canonical(json.loads((out/'END.json').read_text()))
 target=(R.parent/'objects/C632_WINNER/GENERATOR.json').read_bytes()
 assert got==target,'Reproposed controls differ; audit them separately, never promote by analogy.'
 print('BQ13_COMPLETE_CAP_AND_MASS_REPROPOSAL_BYTE_IDENTICAL',hashlib.sha256(got).hexdigest(),flush=True)
if __name__=='__main__':main()
