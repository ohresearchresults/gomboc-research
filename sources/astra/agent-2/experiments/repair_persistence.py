from pathlib import Path
import sys,numpy as np,json
from support_search import SupportSearch,ROOT
from support_persistence import PersistenceSearch,complex_for,points,edge_graphs,barcode
seed=int(sys.argv[1]) if len(sys.argv)>1 else 1
Y=np.load(sys.argv[2] if len(sys.argv)>2 else ROOT/'artifacts/support_persistence/kf27d_maxnorm_seed1/lowest_loss.npy')
out=ROOT/'artifacts/persistence_repair'/f'seed{seed}';rng=np.random.default_rng(seed)
if seed>1:Y+=rng.normal(size=Y.shape)*(.0001*seed)
obj=SupportSearch(Y,out,margin=1e-5);obj.run(rounds=35,iters=600,rng=rng)
for filename in ['best.npy','lowest_loss.npy']:
 P=np.load(out/filename);ds,xm,tr,tm,ym=complex_for(P);Z,Q=points(P,ds,tr,tm);eu,es=edge_graphs(ds,xm);bu,wu,p=barcode(Z,xm,eu);bs,ws,q=barcode(Q,ym,es)
 print('END_BARS',filename,sorted(p,reverse=True)[:4],sorted(q,reverse=True)[:4],flush=True)
