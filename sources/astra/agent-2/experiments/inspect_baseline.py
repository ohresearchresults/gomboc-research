from pathlib import Path
import json,numpy as np
from fractions import Fraction
from collections import Counter
from geometry import hull_from_supports,mass,summary
root=Path(__file__).resolve().parents[1]
H=json.loads((root/'artifacts/baseline/H_exact.json').read_text())['H']
Y=np.array([[float(Fraction(a,r[3])) for a in r[:3]] for r in H])
X,Y,faces,tri,E,active=hull_from_supports(Y)
print('Numerical',summary(X,Y,tri),'E',E,'sizes',dict(Counter(map(len,faces))),flush=True)
vol,c=mass(X,tri);X-=c;Y/= (1-Y@c)[:,None]
np.savez(root/'artifacts/baseline/numerical.npz',X=X,Y=Y,tri=tri,faces=np.array(faces,dtype=object),active=active,raw_centroid=c)
res=[]
for i in range(len(Y)):
    Z,Q,ff,tt,e,aa=hull_from_supports(np.delete(Y,i,axis=0))
    s=summary(Z,Q,tt);s.update(removed=i,E=e,C=2*e);res.append(s)
(root/'artifacts/baseline/single_support_deletions.json').write_text(json.dumps(res,indent=2)+'\n')
print('Removal classes',Counter((r['S'],r['U'],r['E']) for r in res))
print('Best',sorted(res,key=lambda r:(r['S']+r['U'],r['E'],r['S']))[:8])
