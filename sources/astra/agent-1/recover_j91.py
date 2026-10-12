import numpy as np,json,pathlib,math
from scipy.spatial import ConvexHull
from audit_exact import R,cross,dot,sub,mul,encode
p=pathlib.Path('sources/j91');lines=(p/'J90_DETACHED_C390_G8.txt').read_text().splitlines();n,D=map(int,lines[0].split());N=[tuple(map(int,r.split())) for r in lines[1:]];assert len(N)==n
oracle=ConvexHull(np.array(N,dtype=float)/D);points=set()
for ss in oracle.simplices:
 a,b,c=[N[i] for i in ss];u=cross(b,c);v=cross(c,a);w=cross(a,b);det=dot(a,u);num=tuple(D*(u[k]+v[k]+w[k]) for k in range(3))
 if det<0:num=tuple(-a for a in num);det=-det
 gg=math.gcd(*num,det);pp=tuple(a//gg for a in num)+(det//gg,);assert all(dot(z,pp[:3])<=D*pp[3] for z in N);points.add(pp)
X=[tuple(R(v,a[3]) for v in a[:3]) for a in sorted(points)]
assert len(X)==130
inp=json.loads((p/'J91_REBALANCED_C434_G18_INPUT.json').read_text());X+= [tuple(R(x) for x in r) for r in inp['apexes']]
H=[]
for cy in inp['faces']:
 a,b,c=[X[i] for i in cy[:3]];normal=cross(sub(b,a),sub(c,a));offset=dot(normal,a)
 if offset<0:normal=mul(-1,normal);offset=-offset
 assert offset>0
 assert all(dot(normal,v)<=offset for v in X)
 assert {i for i,v in enumerate(X) if dot(normal,v)==offset}==set(cy)
 den=math.lcm(*(int(v.denominator) for v in (*normal,offset)));row=[int(v*den) for v in (*normal,offset)];gg=math.gcd(*row);H.append([v//gg for v in row])
out=pathlib.Path('artifacts/j91-c434');out.mkdir(exist_ok=True)
(out/'H_exact.json').write_text(json.dumps({'H':H}));(out/'V_exact.json').write_text(json.dumps(encode(X)))
Q=np.array([[float(R(x,r[3])) for x in r[:3]] for r in H]);np.savez(out/'seed.npz',Q=Q)
from geometry import halfspace_mesh,census
m=halfspace_mesh(Q);print(json.dumps(census(m),indent=2));(out/'float-census.json').write_text(json.dumps(census(m),indent=2))
