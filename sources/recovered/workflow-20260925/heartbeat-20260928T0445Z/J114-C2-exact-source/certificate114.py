"""Exact all-C2-preserving-affine exclusion for literal C2POLAR_M0_D14_G4.
Depends only on complete symmetry114.py, which embeds the exact parent H data.
The report is a new necessary-condition theorem, NOT a full affine exclusion.
"""
from symmetry114 import geometry,F,dot,sub,mul,N,D
from pathlib import Path
import json,hashlib,sys
sys.set_int_max_str_digits(0)
def outer(x):return [[a*b for b in x] for a in x]
def weighted(A,B,t):return [[t*A[i][j]+(1-t)*B[i][j] for j in range(2)] for i in range(2)]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def interval(x,D=10**12):
    a=x.numerator*D//x.denominator
    return [a,a+1,D]
def encode(A):return [[str(x) for x in row] for row in A]
def main():
    v,faces,active,edges,V,g=geometry();p=[sub(x,g) for x in v];q={i:mul(1/(D-dot(N[i],g)),N[i]) for i in active}
    assert [i for i,x in enumerate(p) if x[:2]==(0,0)]==[50]
    assert [i for i in active if N[i][:2]==(0,0)]==[0]
    u=p[50];s=q[0];phys=[0,24];pol=[12,40]
    aa=[u[2]**2-p[i][2]**2 for i in phys];bb=[s[2]**2-q[j][2]**2 for j in pol]
    assert min(aa)>0 and min(bb)>0
    P=[outer(mul(1,a)) for a in [p[i][:2] for i in phys]]
    Q=[outer(mul(1,a)) for a in [q[i][:2] for i in pol]]
    P=[[[x/a for x in row] for row in z] for z,a in zip(P,aa)]
    Q=[[[x/b for x in row] for row in z] for z,b in zip(Q,bb)]
    A=weighted(P[0],P[1],F(4,5));C=weighted(Q[0],Q[1],F(1,2))
    dA,dC=det(A),det(C);assert A[0][0]>0 and C[0][0]>0 and dA>0 and dC>0
    tr=sum(A[i][j]*C[j][i] for i in range(2) for j in range(2))
    target=F(31,25)
    assert tr<target
    gap=4*dA*dC-(target-tr)**2
    assert gap>0
    # Thus (tr sqrt(A^(1/2) C A^(1/2)))^2 = tr(A C)+2 sqrt(det A det C)>31/25.
    # For every B>0, tr(B A)*tr(B^-1 C) is >= this expression.
    # If axial U and axial S were both global farthest roots, both traces <=1.
    report=dict(identity='J114_C2_ENTIRE_SYMMETRY_PRESERVING_AFFINE_ORBIT_NO_110',parent='C2POLAR_M0_D14_G4',VEF=[len(v),len(edges),len(faces)],centroid=list(map(str,g)),volume=str(V),fixed_vertex=50,fixed_facet=0,
      physical_vertices=phys,physical_incident_supports=[[i for i,n in enumerate(N) if dot(n,v[k])==D] for k in phys],polar_input_faces=pol,
      physical_weights=['4/5','1/5'],polar_weights=['1/2','1/2'],physical_bounds=list(map(str,aa)),polar_bounds=list(map(str,bb)),
      A=encode(A),C=encode(C),trace_AC=str(tr),det_A=str(dA),det_C=str(dC),squared_trace_root_lower_bound=str(target),rational_positive_gap=str(gap),gap_interval=interval(gap),trace_interval=interval(tr),
      proof='For every SPD 2x2 B, tr(B A) tr(B^-1 C) >= tr(A C)+2 sqrt(det A det C)>31/25>1. Axial unique U and axial unique S force both traces<=1. C2 symmetry forces those two fixed carriers. G=diag(B,1) represents all C2-preserving affine metrics after positive scale normalization.',
      exclusions_not_claimed=['General symmetry-breaking affine metrics','Changed support geometry','All C2-symmetric homogeneous bodies'])
    data=(json.dumps(report,indent=2)+'\n').encode();Path('J114_C2_AFFINE_EXACT.json').write_bytes(data)
    print(json.dumps(dict(physical_incident_supports=report['physical_incident_supports'],gap_interval=report['gap_interval'],trace_interval=report['trace_interval'],bytes=len(data),sha256=hashlib.sha256(data).hexdigest()),indent=2))
    print('J114_ALL_C2_PRESERVING_AFFINE_METRICS_EXCLUDED_EXACT_PASS_NOT_110')
if __name__=='__main__':main()
