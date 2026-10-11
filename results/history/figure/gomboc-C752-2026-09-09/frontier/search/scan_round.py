import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,hashlib,numpy as np
from pathlib import Path
from coarsen2 import load,data,geom,ERR
q,labels=load(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(exist_ok=True,parents=True)
# Defining RAW convention: keep original stable support at input row 3.
s=labels.index(3);order=list(range(len(q)));order[3],order[s]=order[s],order[3];q=q[order];labels=[labels[j] for j in order]
(out/'INPUT_ORDER.json').write_text(json.dumps(labels))
for k in range(4,10):
 D=10**k;I=np.rint(q*D).astype(np.int64);I[q[:,2]==1,2]=D;z=I/D
 try:
  G=geom(z);cc=[len(G[x]) for x in ('S','U','H')];vef=[G[x] for x in ('V','E','F')];f=float(data(G,3,False)[0].min())
  raw=json.dumps(dict(D=D,I=I.tolist(),scale=1),sort_keys=True,separators=(',',':')).encode()
  print(k,vef,cc,f,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
  if cc==[1,1,0] and f>0 and len(G['active'])==len(z):(out/f'RAW_D{D}.json').write_bytes(raw)
 except ERR as e:print(k,'INVALID',str(e)[:200],flush=True)
