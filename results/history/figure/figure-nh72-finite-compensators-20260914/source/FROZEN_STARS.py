"""Global restrictions from genuine unchanged supporting cones, not solver failure."""
import sys,json,itertools
from pathlib import Path
from fractions import Fraction as Q
import BUILD
sys.set_int_max_str_digits(0)
ROOTS={'PAIR99':[95,124],'TRIPLE117':[75,76,93]}
def certify(P,faces,raw,g,moving,roots):
 q=[tuple(Q(v,h[3]) for v in h[:3]) for h in raw['H']];result=[];bounds=[]
 for v in roots:
  inc=[f for f,cy in enumerate(faces) if v in cy and not set(cy)&moving];z=BUILD.sub(P[v],g);cert=None
  for fs in itertools.combinations(inc,3):
   mat=[[q[f][j] for f in fs] for j in range(3)]
   try:inv=BUILD.inverse(mat)
   except StopIteration:continue
   lam=[BUILD.dot(row,z) for row in inv]
   if min(lam)>0:
    assert all(sum(lam[k]*q[fs[k]][j] for k in range(3))==z[j] for j in range(3))
    eps=min(lam[k]/(2*sum(abs(x) for x in inv[k])) for k in range(3));bounds.append(eps)
    cert=dict(vertex=v,unchanged_face_ids=list(fs),positive_weights=list(map(str,lam)),weight_floors_1e12=[int(x*10**12) for x in lam],centre_box_radius=str(eps));break
  assert cert is not None,v
  result.append(cert)
 return result,min(bounds)
def run(base,case):
 P,keep,faces,labels,beta=BUILD.setup(base,case);raw,_=BUILD.raw(base,case,[Q(0)]*3);g=tuple(map(Q,base['raw_centroid']));moving={i for cap in BUILD.CASES[case]['caps'] for i in cap['vertices']};cert,eps=certify(P,faces,raw,g,moving,ROOTS[case]);floor=int(eps*10**12)
 out=dict(status='FINITE_MULTIVERTEX_SURGERY_ARBITRARY_CAP_COMPENSATION_EXCLUDED',case=case,strict_unstable_lower_bound=len(cert),certificates=cert,centre_box_radius=str(eps),radius_floor_1e12=floor,scope='Any convex finite realization retaining the listed fixed vertices and unchanged supporting halfspaces, with actual ordinary-volume centroid within the certified open infinity-norm box around c0. In particular arbitrary boundary-fixing deformations of both caps with perfect centroid restoration. No restriction on cap parameter magnitude is imposed. Different core geometry or centres outside the box are not excluded.')
 print(out['status'],case,len(cert),float(eps),flush=True);return out
if __name__=='__main__':
 base,case,out=sys.argv[1:];r=run(json.loads(Path(base).read_text()),case);Path(out).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
