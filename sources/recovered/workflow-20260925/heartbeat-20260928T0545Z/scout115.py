"""Finite one-step polar cut availability scout on literal J114B_G5."""
import numpy as np,json
from geometry115 import *
from pathlib import Path
m=geometry(read_h(Path(__file__).with_name('J114B_G5.txt')))
p=m['p']; c=census(m); r=m['q'][15]; oldq=m['q']; U=c['U']; junior=c['P'][0][1];level=c['P'][0][4]
ed=m['edges'];a=p[ed[:,0]];d=p[ed[:,1]]-a;t=np.clip(-np.sum(a*d,axis=1)/np.sum(d*d,axis=1),0,1);lev=np.sum((a+t[:,None]*d)**2,axis=1)
nei={i:[] for i in range(len(p))}
for (i,j),h in zip(ed,lev):
    if h>level+1e-12:nei[i].append(j);nei[j].append(i)
comp={junior};todo=[junior]
while todo:
    i=todo.pop()
    for j in nei[i]:
        if j not in comp:comp.add(j);todo.append(j)
qs=r[None,:]/2+np.linalg.norm(r)/2*p/np.linalg.norm(p,axis=1)[:,None]
qs*=.999
support=np.einsum('ij,ij->i',qs,p)
print('junior component',len(comp),'vertices',sorted(comp));print('root length',np.linalg.norm(r),'S height',1/np.linalg.norm(r),'deathradius',level**.5)
print('component max allowed cut supports',[(i,float(support[i]),float(np.linalg.norm(p[i]))) for i in sorted(comp)])
valid=np.where(support>1+1e-8)[0];print('valid',len(valid),'comp invalid',comp-set(valid))
allm=geometry(np.r_[oldq,qs[valid]])
print('max-discrete',json.dumps({k:v for k,v in census(allm).items() if not k.endswith('scores')}))
Path(__file__).with_name('SCOUT115.json').write_text(json.dumps(dict(comp=sorted(map(int,comp)),valid=valid.tolist(),candidate_q=qs[valid].tolist(),parent_centroid=m['g'].tolist(),core_census={k:v for k,v in census(allm).items() if not k.endswith('scores')}),indent=2)+'\n')
