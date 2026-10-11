"""Exact C2-symmetric affine compatibility test on literal J113 M0 D14 G4.
New necessary-condition computation; not a replay of the author's full census.
Run with CPython standard library and assertions enabled.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import math,json,hashlib,sys
sys.set_int_max_str_digits(0)
A0=[[631,-19,9661],[1323,-79,9564],[2131,-184,9377],[3091,-335,9043],[4203,-526,8478],[5422,-735,7586],[6635,-923,6275],[7661,-1039,4499],[8272,-1036,2304],[8244,-895,-141],[7440,-643,-2550],[5874,-353,-4579],[3741,-115,-5929],[1367,0,-6433]]
B0=[[-618,149,9657],[-1305,273,9559],[-2116,381,9370],[-3085,481,9033],[-4210,581,8466],[-5440,690,7571],[-6658,819,6257],[-7674,973,4481],[-8258,1139,2287],[-8190,1277,-154],[-7343,1322,-2558],[-5754,1203,-4583],[-3634,879,-5930],[-1318,365,-6433]]
D=10000
N=[(0,0,D)]
for block in (A0,B0):
    N+=list(map(tuple,block))+[(-x,-y,z) for x,y,z in block]
raw=str(len(N))+' '+str(D)+'\n'+'\n'.join(' '.join(map(str,a)) for a in N)+'\n'
assert len(raw.encode())==874 and hashlib.sha256(raw.encode()).hexdigest()=='53d2d66e568161904ed2b66a44190459d70409f96b552a76c1f6316fc210e4b4'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def geometry():
    vs=set();cs={(i,j):cross(N[i],N[j]) for i,j in combinations(range(len(N)),2)}
    for i,j,k in combinations(range(len(N)),3):
        w=dot(N[i],cs[j,k])
        if not w:continue
        a=tuple(D*(cs[j,k][t]-cs[i,k][t]+cs[i,j][t]) for t in range(3))
        if w<0:w=-w;a=mul(-1,a)
        if all(dot(n,a)<=D*w for n in N):vs.add(tuple(F(x,w) for x in a))
    v=sorted(vs);faces=[];active=[];ed={};areas=[];V=F(0);M=(F(0),)*3
    for j,n in enumerate(N):
        ids=[i for i,x in enumerate(v) if dot(n,x)==D]
        if len(ids)<3:continue
        c=mul(F(1,len(ids)),tuple(sum(v[i][k] for i in ids) for k in range(3)))
        axis=min(range(3),key=lambda k:abs(n[k]));e=cross(n,tuple(int(k==axis) for k in range(3)));f=cross(n,e)
        ids.sort(key=lambda i:math.atan2(float(dot(sub(v[i],c),f)),float(dot(sub(v[i],c),e))))
        area=(F(0),)*3
        for a,b in zip(ids,ids[1:]+ids[:1]):
            assert all(dot(cross(sub(v[b],v[a]),sub(v[k],v[a])),n)>0 for k in ids if k not in(a,b))
            area=add(area,mul(F(1,2),cross(v[a],v[b])))
            ed.setdefault(tuple(sorted((a,b))),[]).append((a,b))
        assert cross(area,n)==(0,0,0) and dot(area,n)>0
        areas.append(area)
        for b,cidx in zip(ids[1:-1],ids[2:]):
            a=ids[0];w=dot(v[a],cross(v[b],v[cidx]));assert w>0
            V+=w/6;M=add(M,mul(w/24,add(add(v[a],v[b]),v[cidx])))
        faces.append(ids);active.append(j)
    assert all(len(z)==2 and z[0]==z[1][::-1] for z in ed.values())
    assert len(v)-len(ed)+len(faces)==2
    assert tuple(sum(a[k] for a in areas) for k in range(3))==(0,0,0)
    assert any(dot(N[i],cross(N[j],N[k])) for i,j,k in combinations(active,3))
    # Exact positive area weights of spanning outward normals prove boundedness.
    g=mul(1/V,M)
    assert V>0 and all(dot(n,g)<D for n in N)
    assert g[:2]==(0,0)
    assert {(-x,-y,z) for x,y,z in v}==set(v)
    assert {(-x,-y,z) for x,y,z in N}==set(N)
    return v,faces,active,sorted(ed),V,g

def main():
    v,faces,active,edges,V,g=geometry()
    p=[sub(x,g) for x in v];q={i:mul(1/(D-dot(n,g)),n) for i,n in enumerate(N) if i in active}
    fixedv=[i for i,x in enumerate(p) if x[0]==x[1]==0]
    fixedf=[i for i in active if N[i][0]==N[i][1]==0]
    assert fixedv==[50] and fixedf==[0]
    u=p[fixedv[0]];s=q[fixedf[0]]
    # Every unique radial maximum must be fixed by the isometric half-turn.
    # G normalized to diag(B,1), inverse diag(B^-1,1).
    candidates=[]
    for i,x in enumerate(p):
        aa=u[2]**2-x[2]**2
        for j,y in q.items():
            bb=s[2]**2-y[2]**2
            lhs=dot(x[:2],y[:2])**2;rhs=aa*bb
            candidates.append((float(lhs-rhs),i,j,lhs,rhs,aa,bb))
    candidates.sort(reverse=True);gap,i,j,lhs,rhs,aa,bb=candidates[0]
    out=dict(identity='J114_C2_AFFINE_NECESSARY_NORM_TEST',parent='C2POLAR_M0_D14_G4',VEF=[len(v),len(edges),len(faces)],volume=str(V),centroid=list(map(str,g)),centroid_float=list(map(float,g)),fixed_vertex=fixedv,fixed_facet=fixedf,best_pair=[i,j],point=list(map(str,p[i])),polar=list(map(str,q[j])),axial_U=list(map(str,u)),axial_S=list(map(str,s)),lhs=str(lhs),rhs=str(rhs),gap=str(lhs-rhs),gap_float=gap,upper_physical=str(aa),upper_polar=str(bb),violation=lhs>rhs,top_pairs=[[i,j,g] for g,i,j,*_ in candidates[:20]])
    Path('C2POLAR_M0_D14_G4.txt').write_text(raw)
    Path('J114_SYMMETRY_REPORT.json').write_text(json.dumps(out,indent=2)+'\n')
    Path('J114_GEOMETRY.json').write_text(json.dumps(dict(N=N,D=D,vertices=[list(map(str,x)) for x in v],centroid=list(map(str,g)),volume=str(V),active=active,faces=faces,edges=edges),indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['VEF','centroid_float','fixed_vertex','fixed_facet','best_pair','gap_float','violation','top_pairs']},indent=2))
    print('J114_C2_METRIC_NORM_TEST_FINISHED_NOT_110')
if __name__=='__main__':main()
