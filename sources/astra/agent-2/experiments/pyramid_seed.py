"""Exact transcription of Regos (2025), Tables1 and3, pages213-215.
https://doi.org/10.1556/096.2025.00142
The source PDF and visual table renders are preserved in sources/regos2025/.
"""
from pathlib import Path
import sys,json,math
from fractions import Fraction as F
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
P2=[[365130,-1003186,0],[732587,-873063,0],[1053703,-608356,0],[1279190,-225556,0],[1365623,240796,0],[1282053,740193,0],[1015871,1210667,0],[577057,1585450,0],[0,1801203,0],[-577057,1585450,0],[-1015871,1210667,0],[-1282053,740193,0],[-1365623,240796,0],[-1279190,-225556,0],[-1053703,-608356,0],[-732587,-873063,0],[-365130,-1003186,0],[10000,-983976,79182]]
PB=[[443228,-17159512,0],[865274,-14530623,0],[1179765,-9597962,0],[1331959,-3309437,0],[1310209,3255391,0],[1134551,9230112,0],[837732,14068092,0],[451364,17474518,0],[0,19280994,0],[-451364,17474518,0],[-837732,14068092,0],[-1134551,9230112,0],[-1310209,3255391,0],[-1331959,-3309437,0],[-1179765,-9597962,0],[-865274,-14530623,0],[-443228,-17159512,0],[0,79798943,5677353]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def physical_halfspaces(points):
    X=[tuple(F(v) for v in row) for row in points];B=X[:-1];A=X[-1];n=len(B)
    twice=[B[i][0]*B[(i+1)%n][1]-B[(i+1)%n][0]*B[i][1] for i in range(n)];area=sum(twice)/2
    assert area>0 and A[2]>0 and all(x[2]==0 for x in B)
    bc=tuple(sum(twice[i]*(B[i][k]+B[(i+1)%n][k]) for i in range(n))/(6*area) for k in range(3))
    c=tuple((3*bc[k]+A[k])/4 for k in range(3));Z=[sub(x,c) for x in X]
    rows=[(F(0),F(0),F(-1),c[2])]
    for i in range(n):
        a,b,v=Z[i],Z[(i+1)%n],Z[-1];normal=cross(sub(b,a),sub(v,a));h=dot(normal,a)
        assert h>0 and all(dot(normal,x)<=h for x in Z)
        rows.append((*normal,h))
    H=[]
    for row in rows:
        den=math.lcm(*(v.denominator for v in row));r=[int(v*den) for v in row];g=math.gcd(*r);H.append([v//g for v in r])
    return {'H':H},c,area*A[2]/3
if __name__=='__main__':
    sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'));import check_B
    out=ROOT/'artifacts/pyramids';out.mkdir(exist_ok=True)
    for name,pts in [('P2',P2),('PB',PB)]:
        raw,c,v=physical_halfspaces(pts);rep=check_B.run(raw);assert rep['raw_centroid']==['0','0','0'];assert F(rep['ordinary_volume'])==v
        (out/(name+'_points.json')).write_text(json.dumps(pts)+'\n');(out/(name+'_H.json')).write_text(json.dumps(raw)+'\n');(out/(name+'_audit.json')).write_text(json.dumps(rep,sort_keys=True,separators=(',',':')))
        np.save(out/(name+'_points.npy'),np.array(pts,dtype=float)/1e6)
        print('EXACT_PYRAMID',name,*[rep[k] for k in ['V','E','F','counts','weak']],flush=True)
