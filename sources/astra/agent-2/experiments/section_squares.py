import sys,json,numpy as np
from section_search import *
m=int(sys.argv[1]);L=int(sys.argv[2]);seed=int(sys.argv[3]) if len(sys.argv)>3 else 0
q=initial(m,L,.02,seed);out=ROOT/'artifacts/section_squares'/f'm{m}_L{L}_seed{seed}';out.mkdir(parents=True,exist_ok=True);(out/'construction.json').write_text(json.dumps(dict(m=m,L=L,seed=seed,beta=.02),indent=2)+'\n');np.save(out/'initial_theta.npy',q)
for k,tau in enumerate([-1.,-1.,.001,.0001]):
 ob=Search(q,m,L,out/f'stage{k}',tau);q=ob.run(3000)
 if ob.target:break
