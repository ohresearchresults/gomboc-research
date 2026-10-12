# material-c97bda903918

AI research material

---

# BH81 finite multicut: complete primary recovery capsule

Self-contained. Save the three literal blocks as BH81_CORE.py, CUT_INPUTS.json and exact_new.py. Python sources end with one newline; compact JSON has no final newline. Run `python exact_new.py` with Python3.13.5, standard library only. No external checkpoint or originating sandbox is required. The code reconstructs actual maximal convex facets, verifies the closed true-edge complex, integrates the uniform filled body at two interior anchors, and tests every own-centroid stable/unstable/edge predicate and weak boundary case.

Five NONWINNERS, not an own110 incumbent: CUT121 V50/E75/F27,C150,own121; LOW121 V44/E66/F24,C132,own121; MASS132 V50/E75/F27,C150,own132; MICRO V42/E63/F23,C126,own132; RADIAL V62/E95/F35,C190,own(4,16,18). All have weak000 and primitive-zero counts000. Each cut means (integer_row/grid) dot x<=1, applied to the hull of the46 embedded G6 points divided by10^6. CUT121/MASS132/RADIAL each have21 cuts; LOW121/MICRO have27. The `source` fields are provenance labels, not dependencies. MICRO's additional U/H pair is genuinely strict, not removable by a floating tolerance.

The lead observed the original54-source cold replay `BH81_FINITE_MULTICUT_EXACT_COLD_REPLAY_PASS 54 independent=True` and a reduced full replay `BH81_MINIMAL_RECOVERY_PASS`, including a second integer-hull/full-feature auditor and projected-polygon mass integration. Those optional methods are not needed for the reconstruction in this primary capsule. The core contains complete inverse3 for an optional separate root method, but does not call it here.

Expected terminal: five `EXACT_MULTICUT_BODY_PASS` lines with counts above. Output filename / bytes / SHA256:
CUT121_EXACT.json /31411/ c745dee9dc5732fcb4ab8c2eed9380921683d07c99cc52b5850db03b54e0d68d
LOW121_EXACT.json /29855/ d77653ab141e4978e434ae7ba1c58041a8e8277a80537eb99720754b796a2396
MASS132_EXACT.json /31960/ caca567bee0c7ab81bbcc5e5a3727e7d65e3ba7f77335a76fe746e0c4d55ba91
MICRO_EXACT.json /39163/ 70efa26463d1b1bcd54a456bec977705c5a43e68d3781651bb24d55485d8ec17
RADIAL_EXACT.json /27878/ cecb4fa2f222a44b3bfd3341d7cf4f03bc508aa810642b4f66790f8a5c42d357
Own-centered common-denominator bits respectively9217,8901,9429,11891,7391. Each NAME_V_INPUT.json is exact integer/common-grid data, not a rounding instruction. EXACT_RECEIPTS.json records output identities.
Source receipts: BH81_CORE.py8408bytes SHA25612132578b6ae9379baab76276b077b0a9548332bd8202b8a9c432b63519b58f1; CUT_INPUTS.json5275bytes SHA2563d24c6af88b91e0eed55087e1c94231c2aa6938d4643a43b58725aa5164fba1a; exact_new.py1973bytes SHA25628effc70b91a2fdf4713522b9c04c30e2ff194a57aedd0b26bdc0520c16234cc.

## BH81_CORE.py
```python
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict, Counter
from pathlib import Path
import argparse, hashlib, json, math, sys

sys.set_int_max_str_digits(0)
Z = F(0)
P6 = [
[-662782,-214465,-845973],[-414228,-151742,533649],
[-161896,254607,812156],[365352,256078,682778],
[-4963,148822,-521027],[472559,520988,212704],
[79060,562904,-173068],[201613,126680,-443592],
[329321,453145,628173],[223093,597478,579771],
[-19072,614025,655946],[-249702,561436,698505],
[-441568,542642,645050],[81579,740260,404654],
[-621409,499632,558154],[-759574,464284,346398],
[-876227,418544,281729],[-762901,475717,422075],
[-969023,321126,89302],[-933907,249672,-106357],
[-931297,367490,186346],[-990566,281683,-2502],
[-1004114,233262,-93695],[-1009407,175066,-181963],
[-1003594,111429,-275498],[-985825,56733,-362387],
[-963561,3357,-431336],[-926489,-29260,-514430],
[-874803,-74796,-604952],[-797712,-129095,-709746],
[212288,-80824,-582533],[-530449,-300001,-896862],
[-453991,-363552,-909506],[-263404,-613951,20338],
[-477834,-372599,114345],[-600760,-232410,-880486],
[-364153,-430343,-913823],[217011,-462047,-780335],
[486981,106570,612006],[157779,-569803,63306],
[-149044,-601434,-828255],[-98079,-133974,751134],
[19869,-745421,-660667],[119026,-858571,-341744],
[285028,-657317,-632695],[168908,-413062,260503]]
G6 = dict(grid=1000000, points=P6)
G6_SHA = '63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5'

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def encode(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),
                      default=str).encode()
def rational_points(raw):
    return [tuple(F(x,raw['grid']) for x in row] for row in raw['points']]
def raw_points(points):
    points=sorted(set(points))
    g=math.lcm(*(x.denominator for row in points for x in row))
    return dict(grid=g,points=[[int(x*g) for x in row] for row in points])

def cycle(points,n):
    points=sorted(set(points))
    if len(points)<3: return ()
    drop=max(range(3),key=lambda i:abs(n[i]))
    axes=[i for i in range(3) if i!=drop]
    def xy(p): return (p[axes[0]],p[axes[1]])
    def turn(a,b,c):
        a,b,c=xy(a),xy(b),xy(c)
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    ordered=sorted(points,key=xy)
    lo=[]
    for p in ordered:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(ordered):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    out=lo[:-1]+hi[:-1]
    if len(out)<3: return ()
    if dot(cross(sub(out[1],out[0]),sub(out[2],out[0])),n)<0:
        out.reverse()
    k=out.index(min(out))
    return tuple(out[k:]+out[:k])

# A face is (outward normal, positive support, cyclic rational vertices).
def hull(points):
    points=sorted(set(points)); raw=raw_points(points)
    ip=[tuple(v) for v in raw['points']]; g=raw['grid']; planes={}
    for i,j,k in combinations(range(len(ip)),3):
        n=cross(sub(ip[j],ip[i]),sub(ip[k],ip[i]))
        if n==(0,0,0): continue
        d=dot(n,ip[i]); vals=[dot(n,p)-d for p in ip]
        if max(vals)<=0 and min(vals)<0: pass
        elif min(vals)>=0 and max(vals)>0:
            n=mul(-1,n); d=-d
        else: continue
        h=math.gcd(*(abs(x) for x in (*n,d)))
        key=tuple(x//h for x in (*n,d))
        planes[key]=None
    faces=[]
    for key in sorted(planes):
        n=tuple(F(x) for x in key[:3]); d=F(key[3],g)
        assert d>0
        poly=cycle([p for p in points if dot(n,p)==d],n)
        assert len(poly)>=3
        faces.append((n,d,poly))
    assert len(faces)>=4
    return faces

def vertices(faces):
    return sorted({p for n,d,poly in faces for p in poly})

def clip(faces,n,d=F(1)):
    n=tuple(map(F,n)); d=F(d); allp=vertices(faces)
    if all(dot(n,p)<=d for p in allp): return faces
    assert any(dot(n,p)<d for p in allp)
    result=[]; cap=set()
    for nn,dd,poly in faces:
        out=[]
        for a,b in zip(poly,poly[1:]+poly[:1]):
            sa=dot(n,a)-d; sb=dot(n,b)-d
            if sa<=0: out.append(a)
            if sa==0: cap.add(a)
            if (sa<0<sb) or (sb<0<sa):
                p=add(a,mul(-sa/(sb-sa),sub(b,a)))
                out.append(p); cap.add(p)
        out=cycle(out,nn)
        if len(out)>=3: result.append((nn,dd,out))
    cap=cycle(cap,n)
    assert len(cap)>=3
    result.append((n,d,cap))
    return result

def integrate(faces,anchor=(Z,Z,Z)):
    V=Z; M=[Z,Z,Z]; count=0
    for n,d,poly in faces:
        for j in range(1,len(poly)-1):
            a,b,c=poly[0],poly[j],poly[j+1]
            w=F(det(sub(a,anchor),sub(b,anchor),sub(c,anchor)),6)
            assert w>0
            V+=w; count+=1
            for k in range(3): M[k]+=w*(anchor[k]+a[k]+b[k]+c[k])/4
    assert V>0
    return V,tuple(M),count

def complex_data(faces):
    p=vertices(faces); lookup={x:i for i,x in enumerate(p)}
    f=[[lookup[x] for x in poly] for n,d,poly in faces]
    edges=defaultdict(list); nbr=defaultdict(set)
    for k,((n,d,poly),row) in enumerate(zip(faces,f)):
        assert all(dot(n,x)<=d for x in p)
        assert set(row)=={i for i,x in enumerate(p) if dot(n,x)==d}
        for i,j in zip(row,row[1:]+row[:1]):
            edges[tuple(sorted((i,j)))].append((k,i,j))
            nbr[i].add(j); nbr[j].add(i)
    for pair,inc in edges.items():
        assert len(inc)==2
        assert inc[0][1:]==tuple(reversed(inc[1][1:]))
    assert len(p)-len(edges)+len(f)==2
    reached={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in nbr[i]-reached: reached.add(j); stack.append(j)
    assert len(reached)==len(p)
    return p,f,edges,nbr

def census(faces,c):
    p,f,edges,nbr=complex_data(faces); x=[sub(a,c) for a in p]
    strict=[[],[],[]]; weak=[[],[],[]]; zeros=[0,0,0]
    def take(k,label,values):
        zeros[k]+=sum(v==0 for v in values)
        if min(values)>0: strict[k].append(label)
        elif min(values)>=0: weak[k].append(label)
    for k,((n,d,poly),row) in enumerate(zip(faces,f)):
        take(0,k,[-dot(n,cross(sub(x[j],x[i]),x[i]))
                  for i,j in zip(row,row[1:]+row[:1])])
    for i in range(len(p)):
        take(1,i,[-dot(x[i],sub(x[j],x[i])) for j in sorted(nbr[i])])
    for (i,j),inc in sorted(edges.items()):
        e=sub(x[j],x[i]); ee=dot(e,e); t=-dot(x[i],e)
        z=add(mul(ee,x[i]),mul(t,e))
        n,m=faces[inc[0][0]][0],faces[inc[1][0]][0]
        aa,bb,ab=dot(n,n),dot(m,m),dot(n,m)
        zn,zm=dot(z,n),dot(z,m)
        take(2,[i,j],[t,ee-t,zn*bb-zm*ab,zm*aa-zn*ab])
    counts=list(map(len,strict))
    if not any(weak): assert counts[0]+counts[1]-counts[2]==2
    # Independent all-halfspace characterization of strict stable faces.
    stable2=[]
    for i,(n,d,poly) in enumerate(faces):
        foot=add(c,mul((d-dot(n,c))/dot(n,n),n))
        if all(dot(m,foot)<h for j,(m,h,pp) in enumerate(faces) if i!=j):
            stable2.append(i)
    assert stable2==strict[0]
    # Independent all-vertex characterization of strict unstable vertices.
    unstable2=[i for i in range(len(p))
        if all(dot(x[i],sub(x[j],x[i]))<0 for j in range(len(p)) if i!=j)]
    assert unstable2==strict[1]
    return dict(strict=counts,weak=list(map(len,weak)),primitive_zeros=zeros,
                strict_features=strict,weak_features=weak)

def audit(faces):
    p,f,edges,nbr=complex_data(faces)
    V,M,nt=integrate(faces)
    anchor=tuple(sum(x[k] for x in p)/len(p) for k in range(3))
    V2,M2,nt2=integrate(faces,anchor)
    assert (V,M)==(V2,M2)
    c=tuple(x/V for x in M)
    own=census(faces,c)
    return dict(V=len(p),E=len(edges),F=len(f),C=2*len(edges),
        volume=V,centroid=c,own=own,faces=f,points=p,
        face_histogram=dict(Counter(map(len,f))),positive_tetrahedra=nt,
        second_mass_decomposition_equal=True)

def inverse3(h):
    d=det(*h)
    if not d: raise ArithmeticError('singular active-cap mass derivative')
    cols=[cross(h[1],h[2]),cross(h[2],h[0]),cross(h[0],h[1])]
    return [[cols[j][i]/d for j in range(3)] for i in range(3)]
```

## CUT_INPUTS.json
```json
{"CUT121":{"cuts":[[52233891965,12412875478,-22244204333],[54662479864,11885326716,-16836720975],[57195138088,16964442315,-5028909179],[55672528052,25470656880,6347138510],[57410150468,19561271574,14822013010],[58592064916,7940628156,25580653046],[58521893737,-5464050387,29902563801],[55335728627,-22260202147,33069177922],[48191144829,-37390641520,34839675756],[37394927280,-41532143791,45328791435],[25808950199,-47949197637,49007535805],[10134399766,-52312244148,52993638708],[-6641429790,-54720782088,53824457747],[-25678479404,-56193832244,49978124433],[-42979236748,-53314341179,44326954942],[-57511032776,-48145310965,36454340123],[-69629441171,-40876449169,26936449483],[-80299074947,-30791008462,14661196162],[-89398108891,-15383791673,-2815383514],[-92994106101,10580367366,-30507900681],[-77491258235,46152810567,-65427225915]],"grid":10000000000,"source":"KILL_SMALL_CLASS.json"},"LOW121":{"cuts":[[-2706654797,13036183744,5164315568],[-403735797,14666667062,14009143827],[-4452986858,14356020699,2116544154],[762706789,12948560589,15567869178],[3097409269,-4380789239,-6951735769],[3882387114,-8523372434,-2946144554],[170280863754,65015881995,-78959999486],[187789023553,67487091997,-39173045099],[204071193517,38701890676,-10720579155],[211492066010,7136624203,16546439917],[210651395610,-26125330332,41665059252],[203837169357,-62555068704,53285233452],[190226285152,-97123187337,64779526591],[166854409942,-125398316472,91026592246],[136603982675,-149240443717,113637271538],[99632806859,-168644186584,132602221190],[58542238194,-182092230441,146377207512],[13745109210,-189556317469,155012104108],[-33332646693,-190549619854,157975767167],[-81961224595,-184545548057,154961242530],[-131947676196,-170905109730,144771463996],[-179433324722,-149007845880,127346822083],[-224753383839,-117070372086,100865685867],[-263458273684,-74225588292,64357172421],[-293046858428,-14375324760,12270579805],[-300018414203,66425846786,-59493518833],[-257688765296,171776886110,-155346342516]],"grid":10000000000,"source":"ROBUST27B_FINAL.json"},"MASS132":{"cuts":[[52531384799,10737883442,-21217160290],[54123575057,11496872519,-16904591266],[56856734982,16546065812,-4721821617],[54768224213,26874421403,6314686259],[57303906071,19684625798,14927069554],[58571294571,7785080043,25756438300],[58428045377,-5437723731,30080720901],[55193693383,-22443762028,33290292514],[48019532350,-37907577983,34760655767],[37179227237,-41525389205,45791907667],[25767274210,-48122444255,49076207998],[9916721657,-52464806963,53141607269],[-6790777702,-54665165863,54088117528],[-25906763081,-56501566991,49833211674],[-43159660190,-53661667498,44085149005],[-57669682960,-48236324946,36485132489],[-69739986298,-40913349629,27089895526],[-80414826394,-30722555320,15002343257],[-89533894382,-15413015457,-2511570164],[-93204096541,10444045533,-30394992480],[-77874474882,46009801980,-65185051732]],"grid":10000000000,"source":"S1_CENTERED.json"},"MICRO":{"cuts":[[-27066547973579,130361837440902,51643155679280],[-4040396004165,146718979255798,140147842071397],[-44529868584264,143560206994459,21165441540718],[7624443915812,129523259655042,155724764019231],[30974092689311,-43807892390824,-69517357686228],[38823871144587,-85233724341652,-29461445539888],[1702891166686436,650206413409726,-789650762581581],[1878022064269373,674946216350769,-391790025012700],[2040872312983405,387053628591290,-107257485914378],[2115075465960413,71368601652374,165428792949851],[2106651473502377,-261266011938133,416664199441519],[2038496880007765,-625570026328744,532872557642987],[1902378098395453,-971257483885177,647779641186845],[1668623120504442,-1254024934689635,910301383366049],[1366097772894965,-1492444722744053,1136404169049418],[996357101528487,-1686481122003230,1326053885916235],[585438085691969,-1820954162715099,1463786941953240],[137455277288840,-1895582535584725,1550122700396973],[-333322781482862,-1905504088422531,1579739599240450],[-819597222145778,-1845437277901781,1549593771226600],[-1319456889839784,-1709027418473705,1447670500892202],[-1794283168879679,-1490041663870955,1273430454423131],[-2247460648449158,-1170659408541975,1008617717342543],[-2634466735424675,-742221688172232,643545401324649],[-2930319274587725,-143730940119279,122691778272635],[-2999999999334761,664254100405695,-594925157896348],[-2576676029286304,1717683415100938,-1553473479958573]],"grid":100000000000000,"source":"SMALL27_FINAL.json"},"RADIAL":{"cuts":[[-23636290623,-136533493730,74116004912],[9866338945,-2497217630,8161774770],[10910578914,-6495909642,-1832671101],[16613327195,-1743213256,-2787181725],[14287465335,-2214979877,-3273142796],[15073892940,438653953,-6749217669],[-444354733,-7648755279,-5024540951],[4467555550,-4761030823,-2405229191],[12010074830,9688866656,-8469587747],[10361433695,13950316202,-7542981681],[6655930821,15464301527,-7407144195],[2722287362,16510497799,-7130004310],[-1805366544,12618661060,-9091772021],[-4491939437,7923360209,-9051189454],[-10125530128,15301838964,-6085062554],[-10781097448,9374143101,-6507985485],[4820934554,5913784575,9675498596],[151717086,13297178437,-6857383074],[11018032775,18726277394,-7462979896],[-2562446199,80980179276,-33354195155],[-866888466,111308036476,-66981795829]],"grid":10000000000,"source":"RADIAL21_ENERGY.json"}}
```

## exact_new.py
```python
"""Freeze literal cut planes, reconstruct actual maximal hull, exact own and reference census."""
import json,math,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
import BH81_CORE as ex

def freeze(sources,grid=10**10):
 controls={}
 for name,file in sources.items():
  z=json.loads(Path(file).read_text())
  rows=[[round(F(x)*grid) for x in row] for row in z['cuts']]
  controls[name]=dict(grid=grid,cuts=rows,source=file)
 Path('CUT_INPUTS.json').write_bytes(ex.encode(controls))
 return controls

def reconstruct(spec):
 faces=ex.hull(ex.rational_points(ex.G6))
 for row in spec['cuts']:faces=ex.clip(faces,[F(x,spec['grid']) for x in row])
 return faces

def replay(controls):
 receipts={}
 for name,spec in controls.items():
  faces=reconstruct(spec);result=ex.audit(faces);result['reference_zero']=ex.census(faces,(F(0),)*3)
  c=result['centroid'];points=result['points'];den=math.lcm(*(x.denominator for p in points for x in p))
  cd=math.lcm(*((x-c[j]).denominator for p in points for j,x in enumerate(p)))
  result['common_raw_denominator_bits']=den.bit_length();result['common_centered_denominator_bits']=cd.bit_length()
  result['cut_input']=spec
  data=ex.encode(result);Path(name+'_EXACT.json').write_bytes(data)
  raw=ex.raw_points(points);Path(name+'_V_INPUT.json').write_bytes(ex.encode(raw))
  receipts[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),VEF=[result[k] for k in ('V','E','F')],
   strict=result['own']['strict'],weak=result['own']['weak'],zero=result['own']['primitive_zeros'],center_bits=cd.bit_length())
  print('EXACT_MULTICUT_BODY_PASS',name,receipts[name],flush=True)
 Path('EXACT_RECEIPTS.json').write_bytes(ex.encode(receipts));return receipts

if __name__=='__main__':
 if '--freeze' in sys.argv:
  controls=freeze(dict(MASS132='S1_CENTERED.json',CUT121='KILL_SMALL_CLASS.json',RADIAL='RADIAL21_ENERGY.json'))
 else:controls=json.loads(Path('CUT_INPUTS.json').read_text())
 replay(controls)
```
