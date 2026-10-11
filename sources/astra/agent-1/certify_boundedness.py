"""Exact nonnegative conic decompositions of +/- coordinate axes in H normals."""
import sys,json,itertools,pathlib,hashlib
from audit_exact import cross,dot,R,encode
p=pathlib.Path(sys.argv[1]);h=json.loads(p.read_text())['H'];n=[tuple(map(int,r[:3])) for r in h];assert all(int(r[3])>0 for r in h);cert={}
for ids in itertools.combinations(range(len(n)),3):
 a,b,c=[n[i] for i in ids];u,v,w=cross(b,c),cross(c,a),cross(a,b);d=dot(a,u)
 if not d:continue
 for axis in range(3):
  for sign in [-1,1]:
   key=f'{axis}:{sign}'
   if key in cert:continue
   coeff=[R(sign*z[axis],d) for z in [u,v,w]]
   if min(coeff)<0:continue
   assert all(sum(coeff[j]*n[ids[j]][k] for j in range(3))==(sign if k==axis else 0) for k in range(3))
   cert[key]={'normal_indices':list(ids),'coefficients':coeff}
 if len(cert)==6:break
assert len(cert)==6
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'strict_interior_point':[0,0,0],'certificates':cert,'recession_cone_is_zero':True}
pathlib.Path(sys.argv[2]).write_text(json.dumps(encode(out),indent=2));print('EXACT_BOUNDEDNESS_CERTIFIED')
