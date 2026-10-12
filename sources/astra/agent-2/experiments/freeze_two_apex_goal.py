"""Exact freeze of one consistent two-contact-group physical support body.
Free binary64 controls are converted to their exact dyadic rationals. The
second group's dependent normal component is derived rationally from h.v=1.
Only the resulting single homogeneous filled intersection is audited. Native
B audits every strict/weak sign; native A independently verifies a qualifier.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from freeze_triangle_cap_goal import primitive,encode,check_B,check_A

def run(source,out,m,n):
    source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=source.read_bytes();(out/'controls.npy').write_bytes(raw);controls=np.load(out/'controls.npy')
    if not np.isfinite(controls).all():raise ValueError('nonfinite physical controls')
    q=list(map(lambda x:mpq(float(x)),controls));point=q[-3:]
    if not point[2]:raise ValueError('second contact plane parameterization is singular')
    H=[]
    for i in range(m):H.append([q[2*i],q[2*i+1],mpq(1)])
    for i in range(n):
        a,b=q[2*m+2*i:2*m+2*i+2];H.append([a,b,(1-a*point[0]-b*point[1])/point[2]])
    remaining=q[2*(m+n):-3]
    if len(remaining)%3:raise ValueError('physical support controls have invalid length')
    H.extend(remaining[i:i+3] for i in range(0,len(remaining),3));body={'H':sorted(set(primitive([*h,1]) for h in H))}
    (out/'controls_exact.json').write_text(json.dumps(dict(m=m,n=n,q=list(map(str,q)),prescribed_intersections=[['0','0','1'],list(map(str,point))]),indent=2)+'\n');(out/'H.json').write_bytes(encode(body))
    construction=dict(source=str(source),sha256=hashlib.sha256(raw).hexdigest(),m=m,n=n,definition=__doc__,mass='uniform Lebesgue volume on this exact intersection',prescribed_intersections_need_not_be_hull_vertices=True)
    (out/'construction.json').write_text(json.dumps(construction,indent=2)+'\n');B=check_B.run(body);(out/'audit_B.json').write_bytes(encode(B));qualified=B['counts']==[1,1,0] and B['weak']==[0,0,0] and 34<=2*B['E']<500
    result={k:B[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};result.update(C2E=2*B['E'],VplusEplusF=B['V']+B['E']+B['F'],B_qualified=qualified,independent_A_qualified=False,audit_B_sha256=hashlib.sha256(encode(B)).hexdigest())
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    if qualified:
        A=check_A.run(body);(out/'audit_A.json').write_bytes(encode(A));different=[k for k in set(A)|set(B) if A.get(k)!=B.get(k)];(out/'independent_comparison.json').write_text(json.dumps(dict(differing_fields=different),indent=2)+'\n')
        if different:raise ValueError('independent exact auditors disagree on the proposed Figure')
        result.update(independent_A_qualified=True,audit_A_sha256=hashlib.sha256(encode(A)).hexdigest());(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EXACT_TWO_APEX_GOAL_AUDIT',result,flush=True);return result

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
