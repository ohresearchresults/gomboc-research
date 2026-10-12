import json,re,pathlib,math,numpy as np
from audit_exact import R,sub,cross,dot,mul
s=pathlib.Path('sources/COORD_D717_DROP29_C162_OWN121_EXACT_INPUT_AND_RECEIPTS.md').read_text();data=json.loads(re.search(r'```json\n(.*?)\n```',s,re.S)[1]);X=[tuple(R(v) for v in row) for row in data['points']];H=[]
for cy in data['triangles']:
 a,b,c=[X[i] for i in cy];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
 if h<0:n=mul(-1,n);h=-h
 assert h>0 and all(dot(n,x)<=h for x in X)
 den=math.lcm(*(int(v.denominator) for v in (*n,h)));row=[int(v*den) for v in (*n,h)];gg=math.gcd(*row);H.append([v//gg for v in row])
p=pathlib.Path('artifacts/c162');p.mkdir(exist_ok=True);(p/'input.json').write_text(json.dumps(data,separators=(',',':')));(p/'H_exact.json').write_text(json.dumps({'H':H},separators=(',',':')))
Q=np.array([[float(R(v,row[3])) for v in row[:3]] for row in H]);np.savez(p/'seed.npz',Q=Q)
from geometry import halfspace_mesh,census
print(census(halfspace_mesh(Q)))
