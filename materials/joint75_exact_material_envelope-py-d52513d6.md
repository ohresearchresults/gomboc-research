# material-d52513d68657

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""Exact homogeneous material-envelope obstruction, standard library only.
Integer geometry uses common coordinate denominator 10**8. Every supporting
plane is enumerated, equal planes merged, polygon boundaries reconstructed.
No floating result, tolerance, optional package, or nominated topology is trusted.
"""
from itertools import combinations
from math import gcd
from functools import reduce
from fractions import Fraction as F
import json,hashlib,argparse
from pathlib import Path

I75 = [
[-11310213,-3802031,232661],[-11269293,-2834032,-2182730],
[-10855182,-2246500,-3911998],[-10128821,-1814868,-5467871],
[-9452382,-6834502,6456555],[-9308206,-1555414,-6662777],
[-8712882,-8006246,8846843],[-8693078,-1373304,-7380329],
[-7797905,-1286403,-8181129],[-6681453,-1307873,-8916622],
[-6352338,2020313,-1146993],[-5892536,2295258,-71116],
[-5592263,2241235,541206],[-5425338,-1474781,-9487378],
[-5280741,2171200,1073969],[-4959361,3312877,-1863739],
[-4453446,1994305,2115702],[-4311479,345947,4048866],
[-4305575,1694912,2608464],[-4237167,1203950,3206121],
[-3820955,4252385,-2139686],[-3661038,4074852,-884602],
[-3623465,-1644023,-10021566],[-3190033,811977,3827673],
[-3155609,4102561,85230],[-3074935,4483432,-2851622],
[-2953571,-1851896,-10161171],[-2718323,668005,3934224],
[-2651732,122199,4295157],[-2302445,4621821,-3324860],
[-2248430,-2037367,-10247983],[-2145336,4388373,461753],
[-1938256,3964861,1093487],[-1561887,3760992,1454978],
[-1502148,-2223378,-10275715],[-1278721,4758931,-3663608],
[-1049751,3727821,1606020],[-740759,-2457388,-10231458],
[-298044,4806779,-3669461],[-159770,3872224,1576892],
[-121991,838112,3483867],[39249,-2666243,-10115526],
[91753,589879,3521150],[725989,729286,3291554],
[822613,-2865673,-9923443],[847151,1601384,2948252],
[1257541,4150503,1429262],[1400720,4852019,-3212547],
[1599055,-3043575,-9655675],[2331916,-2317243,-9420429],
[2351892,-3267823,-9302290],[2947803,5018418,-438633],
[3091632,-3449326,-8871363],[3252567,4572542,973174],
[3518927,-4445832,-8207140],[3801752,-3598386,-8365506],
[3886092,3932529,1241770],[4317265,3420766,1352627],
[4466143,-3720508,-7791824],[4524082,-5334292,-6695320],
[4622668,3053371,1323427],[4905967,2678528,1274548],
[5061533,-3853293,-7158199],[5166891,2298083,1206990],
[5506198,-4926808,-5369878],[5525767,-801605,-6004784],
[5644371,1606910,926729],[6018142,937609,612094],
[6137534,-4326615,-4182924],[6330239,239389,230320],
[6547165,-3582767,-3087182],[6574260,-489010,-228500],
[6738672,-1246564,-776981],[6751376,-2814918,-2197016],
[6805726,-2026966,-1429050]]
A6 = [[54523165,-66300276,-55391279],
[49842012,-91287749,-32456638],[35949856,-110325885,-5024889],
[13236236,-120608734,24070669],[-16841661,-119820327,51618679],
[-51605841,-106402263,74185541]]
J19=[22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70]
D=10**8
R=[tuple(10*x for x in p) for p in I75]+[tuple(p) for p in A6]
assert len(R)==81 and len(set(R))==81 and len(J19)==19

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
    g=reduce(gcd,(abs(x) for x in a),0)
    return tuple(x//g for x in a)

def polygon(ids,n):
    drop=max(range(3),key=lambda k:abs(n[k]));u,v=[k for k in range(3) if k!=drop]
    ids=sorted(ids,key=lambda i:(R[i][u],R[i][v]))
    def turn(i,j,k):return (R[j][u]-R[i][u])*(R[k][v]-R[i][v])-(R[j][v]-R[i][v])*(R[k][u]-R[i][u])
    def half(seq):
        a=[]
        for i in seq:
            while len(a)>1 and turn(a[-2],a[-1],i)<=0:a.pop()
            a.append(i)
        return a
    f=half(ids)[:-1]+half(reversed(ids))[:-1]
    assert len(f)>=3
    if dot(cross(sub(R[f[1]],R[f[0]]),sub(R[f[2]],R[f[0]])),n)<0:f.reverse()
    k=f.index(min(f));return f[k:]+f[:k]

def hull(ids):
    ids=sorted(ids); planes=set()
    for i,j,k in combinations(ids,3):
        n=cross(sub(R[j],R[i]),sub(R[k],R[i]))
        if n==(0,0,0):continue
        h=dot(n,R[i]);pos=neg=False
        for l in ids:
            s=dot(n,R[l])-h;pos=pos or s>0;neg=neg or s<0
            if pos and neg:break
        if pos and neg:continue
        if not (pos or neg):raise ValueError('Not full dimensional')
        if pos:n=tuple(-x for x in n);h=-h
        planes.add(primitive(n+(h,)))
    planes=sorted(planes);faces=[]
    for a in planes:
        zeros=[i for i in ids if dot(a[:3],R[i])==a[3]]
        assert all(dot(a[:3],R[i])<=a[3] for i in ids)
        faces.append(polygon(zeros,a[:3]))
    keep=sorted({i for f in faces for i in f});owners={};tri=[]
    for fi,f in enumerate(faces):
        for i,j in zip(f,f[1:]+f[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(fi)
        tri.extend((f[0],f[k],f[k+1]) for k in range(1,len(f)-1))
    assert all(len(v)==2 for v in owners.values())
    assert len(keep)-len(owners)+len(faces)==2
    assert sum(map(len,faces))==2*len(owners)
    V6=0;Mnum=[0]*3;area=[0]*3
    for i,j,k in tri:
        t=det(R[i],R[j],R[k]);V6+=t
        for a in range(3):Mnum[a]+=t*(R[i][a]+R[j][a]+R[k][a])
        n=cross(sub(R[j],R[i]),sub(R[k],R[i]));area=[x+y for x,y in zip(area,n)]
    assert V6>0 and area==[0,0,0]
    # Independent integration reference, using integers throughout.
    N=len(keep);S=tuple(sum(R[i][k] for i in keep) for k in range(3));VV=0;MM=[0]*3
    for i,j,k in tri:
        vv=[tuple(N*R[t][a]-S[a] for a in range(3)) for t in (i,j,k)]
        t=det(*vv);assert t>0;VV+=t
        for a in range(3):MM[a]+=t*(S[a]+N*(R[i][a]+R[j][a]+R[k][a]))
    assert VV==N**3*V6 and MM==[N**4*x for x in Mnum]
    return dict(ids=keep,faces=faces,planes=planes,edges=sorted(owners),V=len(keep),E=len(owners),F=len(faces),V6=V6,Mnum=Mnum,
                volume=F(V6,6*D**3),centroid=[F(x,4*D*V6) for x in Mnum])

def reduced_core(O):
    ids=[0,2,6,13,31,47,63,65,75,76,77,78,79,80]
    W=hull(ids);dv=O['V6']-W['V6'];protected=[];bounds=[]
    for vi in O['ids']:
        if vi not in W['ids']:continue
        candidates=[]
        for wi in O['ids']:
            if wi==vi:continue
            d=sub(R[wi],R[vi]);vd=dot(R[vi],d)
            b=4*W['V6']*vd-dot(W['Mnum'],d)+4*dv*max(0,vd-min(dot(R[i],d) for i in O['ids']))
            candidates.append((b,wi))
        b,w=max(candidates)
        bounds.append(dict(vertex=vi,max_upper_numerator=b,attaining_outer_vertex=w))
        if b<0:protected.append(vi)
    assert protected==[6,65] and (W['V'],W['E'],W['F'])==(14,36,24)
    return dict(W=W,protected_U=protected,all_U_bounds=bounds,
                conclusion='Every homogeneous convex L between this14-anchor core and O has at least the two strict unstable vertices P6 and P65 at its actual centroid. No own110.')

def report():
    K=hull(range(75));O=hull(range(81));ids=[i for i in range(81) if i not in J19];W=hull(ids)
    assert (K['V'],K['E'],K['F'])==(75,219,146)
    assert (O['V'],O['E'],O['F'])==(79,231,154)
    assert (W['V'],W['E'],W['F'])==(62,180,120)
    c=K['centroid'];dv=O['V6']-W['V6'];assert dv>0
    protectedU=[];allU=[]
    for vi in O['ids']:
        if vi not in W['ids']:continue
        upper=[]
        for wi in O['ids']:
            if wi==vi:continue
            d=sub(R[wi],R[vi]);vd=dot(R[vi],d)
            bound=4*W['V6']*vd-dot(W['Mnum'],d)+4*dv*max(0,vd-min(dot(R[i],d) for i in O['ids']))
            upper.append((bound,wi))
        b,w=max(upper)
        allU.append(dict(vertex=vi,max_upper_numerator=b,attaining_outer_vertex=w))
        if b<0:protectedU.append(vi)
    protectedS=[];allS=[]
    for fi,f in enumerate(O['faces']):
        if not all(i in W['ids'] for i in f):continue
        lower=[];n=O['planes'][fi][:3]
        for i,j in zip(f,f[1:]+f[:1]):
            a=cross(n,sub(R[j],R[i]));av=dot(a,R[i])
            bound=dot(a,W['Mnum'])-4*W['V6']*av+4*dv*min(0,min(dot(a,R[v])-av for v in O['ids']))
            lower.append((bound,[i,j]))
        b,e=min(lower)
        allS.append(dict(facet=f,min_lower_numerator=b,attaining_edge=e))
        if b>0:protectedS.append(f)
    massbounds=[]
    for k in range(3):
        Vw=W['volume'];Mw=F(W['Mnum'][k],24*D**4);delta=F(dv,6*D**3)
        lo=Mw-c[k]*Vw+delta*min(F(0),min(F(R[i][k],D)-c[k] for i in O['ids']))
        hi=Mw-c[k]*Vw+delta*max(F(0),max(F(R[i][k],D)-c[k] for i in O['ids']))
        massbounds.append(dict(axis=k,relative_moment_lower=lo,relative_moment_upper=hi,
                               lower_centroid_gap=lo/O['volume'] if lo>0 else None,
                               upper_centroid_gap=hi/O['volume'] if hi<0 else None))
    assert protectedU==[0,1,2,3,6,7,8,51,65,73,74,75,76,77]
    assert len(protectedS)==4 and {tuple(sorted(f)) for f in protectedS}=={(6,63,80),(6,14,18),(47,51,65),(51,65,66)}
    assert massbounds[1]['relative_moment_upper']<0<massbounds[2]['relative_moment_lower']
    return dict(identity='JOINT75_J19_SIX_BRIDGE_MATERIAL_ENVELOPE',denominator=D,scope='Every homogeneous convex L with conv(P[not J19],A6) subset L subset conv(P75,A6)',
                parent_source='figure-0552',parent_sha256='ad8dc7c434c78f9d6a7bbd334969fdbfdab83f3a56202484b2698ad9bf1c95d4',
                K=K,O=O,W=W,reduced_core=reduced_core(O),protected_U=protectedU,protected_S=protectedS,all_U_bounds=allU,all_S_bounds=allS,massbounds=massbounds,
                conclusion='S>=4 and U>=14 at the actual homogeneous centroid for every body in this material envelope; hence no own110, at any edge budget.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='exact_envelope.json');args=ap.parse_args()
    r=report();raw=(json.dumps(r,sort_keys=True,separators=(',',':'),default=str)+'\n').encode();Path(args.out).write_bytes(raw)
    print('JOINT75_MATERIAL_ENVELOPE_EXACT_PASS',len(r['protected_S']),len(r['protected_U']))
    print('JOINT75_FOURTEEN_ANCHOR_CORE_EXACT_PASS',r['reduced_core']['protected_U'])
    for b in r['massbounds']:print('AXIS',b['axis'],'MOMENT_BOUNDS',float(b['relative_moment_lower']),float(b['relative_moment_upper']),'CENTRE_GAPS',None if b['lower_centroid_gap'] is None else float(b['lower_centroid_gap']),None if b['upper_centroid_gap'] is None else float(b['upper_centroid_gap']))
    print('REPORT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
