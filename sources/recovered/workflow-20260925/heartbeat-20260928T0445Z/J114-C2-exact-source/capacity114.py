"""Exact carrier-retaining shape/centroid gate, beyond a fixed affine orbit.
Uses complete literal J113 G4 input and exact geometry in symmetry114.py.
"""
from symmetry114 import geometry,F,dot,sub,mul,N,D
from certificate114 import outer,weighted,det,encode,interval
from pathlib import Path
import json,hashlib

def main():
    v,faces,active,edges,V,g=geometry();c=F(3,50);u=v[50];phys=[0,24];pol=[12,40]
    assert all(v[i][2]>u[2] for i in phys)
    P=[];Q=[];aa=[];bb=[]
    for i in phys:
        a=(u[2]-c)**2-(v[i][2]-c)**2;assert a>0;aa.append(a)
        P.append([[z/a for z in row] for row in outer(v[i][:2])])
    for j in pol:
        n=mul(F(1,D),N[j]);b=(1-n[2])*(1+n[2]-2*n[2]*c);assert b>0;bb.append(b)
        Q.append([[z*(1-c)**2/b for z in row] for row in outer(n[:2])])
    A=weighted(P[0],P[1],F(4,5));C=weighted(Q[0],Q[1],F(1,2));tr=sum(A[i][j]*C[j][i] for i in range(2) for j in range(2));dp=det(A)*det(C)
    target=F(1);gap=4*dp-(target-tr)**2
    assert det(A)>0 and det(C)>0 and tr<1 and gap>0
    assert g[2]<F(31,1000)<F(3,50)
    # P(c) decreases in Loewner order with c whenever denominators positive.
    # Q_j(c) has factor f(c)=(1-c)^2/[(1-nz)(1+nz-2nz*c)],
    # with f'(c)=-2(1-c)(1-nz*c)/[(1-nz)(1+nz-2nz*c)^2]<0
    # throughout the feasible range c<1, 1-nz*c>0.
    # If any normalized denominator <=0, its nonzero transverse vector already
    # contradicts the global-root radius bound. Thus the gate holds for every
    # c<=3/50 at which the selected original support planes contain the centre.
    report=dict(identity='J114_RETAINED_CARRIERS_REQUIRE_AXIAL_CENTROID_GT_3_OVER_50',parent='C2POLAR_M0_D14_G4',centroid_ceiling_test=str(c),original_centroid=list(map(str,g)),necessary_upward_shift_lower_bound='29/1000',selected_raw_vertices={str(i):list(map(str,v[i])) for i in [0,24,50]},selected_input_normals={str(i):N[i] for i in [0,12,40]},D=D,A=encode(A),C=encode(C),trace=str(tr),gap=str(gap),gap_interval=interval(gap),trace_interval=interval(tr),
       scope='Every C2-invariant convex homogeneous body retaining raw points v0 and v24 as material points, raw u=v50 as its proposed unique unstable carrier, and original input plane0 as its proposed unique stable carrier, while contained in original input halfspaces0,12,40. After any C2-preserving affine map, own110 requires its pre-map centroid z>3/50. Other boundary geometry is unrestricted. No conclusion if equilibrium roots or one of the retained material/support conditions change.',
       proof='The same weighted two-by-two trace inequality as certificate114.py, evaluated at c=3/50, is >1. Both normalized PSD matrices are Loewner-decreasing as c rises throughout the feasible radius domain; therefore every c<=3/50 is excluded. Original exact homogeneous centroid z<31/1000 proves a required upward shift >29/1000 when these carrier conditions are retained.')
    data=(json.dumps(report,indent=2)+'\n').encode();Path('J114_CARRIER_CENTROID_GATE_EXACT.json').write_bytes(data)
    print(json.dumps(dict(gap_interval=report['gap_interval'],trace_interval=report['trace_interval'],bytes=len(data),sha256=hashlib.sha256(data).hexdigest()),indent=2));print('J114_RETAINED_CARRIER_CENTROID_GATE_EXACT_PASS')
if __name__=='__main__':main()
