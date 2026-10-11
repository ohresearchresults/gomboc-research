from pathlib import Path
import sys,numpy as np
from log_persistence import LogPersistenceSearch
from support_persistence import ROOT
k=int(sys.argv[1]);Y=np.load(ROOT/'artifacts/blend_families'/f't{k:03d}.npy');rng=np.random.default_rng(34000+k)
out=ROOT/'artifacts/blend_anneal'/f't{k:03d}'
for stage,tau in enumerate([.03,.01,.003,.001,.0003]):
 obj=LogPersistenceSearch(Y,out/f'stage{stage}',penalty_scale=tau)
 obj.run(rounds=6,iters=500,rng=rng)
 if obj.target:break
 Y=np.load(obj.out/'lowest_loss.npy')
 print('ANNEAL',k,stage,tau,'best',obj.best,'lowest',obj.bestcost,flush=True)
