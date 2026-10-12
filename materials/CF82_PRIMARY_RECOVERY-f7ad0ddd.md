# material-f7ad0ddd5b48

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# CF82 three primary exact-body recovery capsule

Source: fully read immutable worker result figure-0446, SHA e33ef3c141a5dee5658263bb371547437a7d1740f14fd649c3c5d9410a59c4e4. Its result omitted the full decoder. The lead recovered the actual Library RECOVER_CF82.py (79664 bytes, SHA 6a4f99b24ef48b360acf9a136d536d10d42a6cc98f3e2a9cceb1157ad5afb391) and authenticated its complete 39-unit dictionary (209355 bytes, SHA 778d9a6a51765315295fa67b8f9bf6abc0c2b9a1f061ab2e3e5f8edc79f50d42). This smaller capsule durably preserves the three preferred exact bodies, not the entire numerical campaign or its remaining twelve grids. Those other full source units still require separate preservation. No old sandbox or Library file is required for the three bodies below.

All three are strict211/additionalweak000/primitivezero000 NONWINNERS. RESERVE42_G5 has V42/E120/F80,C240; RESERVE83_G6 and MAIN83_G7 have V82/E240/F160,C480 with supplied row81 inactive. The latter two are distinct rational bodies. The accepted own110 record remains C622. Coordinates are numerator rows divided by the literal grid. Uniform mass is integrated anew; no point is an imposed centroid. The worker reported two independent hull/mechanics implementations; this minimal capsule supplies one complete exact maximal-hull/mechanics auditor with two different mass formulas. The lead's replay below is source recovery, not a third independent mathematical audit.

Save the reconstruction driver below as RECOVER_CF82_PRIMARY.py and this entire material as CF82_PRIMARY_RECOVERY.md. Run:
python -B -S RECOVER_CF82_PRIMARY.py CF82_PRIMARY_RECOVERY.md CF82_PRIMARY

The driver checks all four source files, rebuilds each maximal complex and exact own mass, and reproduces the three original compact audit byte counts/hashes. It was executed with CPython3.13.5. Expected final marker: CF82_THREE_PRIMARY_INPUT_AND_AUDIT_HASHES_PASS. Individual markers name every body. Controls require strict446 tetrahedron and strict446/additionalweak123 prism. All input and audit filenames, byte counts and SHA256 values are literal in the driver. Driver:2070bytes SHA42128b6d397523bf5f0d9aa2d5c69b11b371b56f37a4ad0493926773238b506c.

## Reconstruction driver
```python
"""Extract three literal CF82 bodies and one full exact auditor from this material."""
import hashlib, json, pathlib, re, sys
if len(sys.argv)!=3: raise SystemExit('Usage: python -B -S RECOVER_CF82_PRIMARY.py MATERIAL.md OUT')
source=pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); out=pathlib.Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
inputs={
 'exact_addition.py':(6947,'130800bb8fd045a0399a04663cb193d728fbc7ed4379a6d5328ea5d4972cc079'),
 'CF82_RESERVE42_G5.json':(932,'b3cb940d430aa31dae1444de1ec07fa72a6092d2b9326cb5bfc99b61f7a395e6'),
 'CF82_RESERVE83_G6.json':(2065,'77a30726cc19c133f2bd8997b4a9454495e6dd80333c985c12a4aa5ae319485a'),
 'CF82_MAIN83_G7.json':(2315,'1d63a06ee4e9c0d39d258f1016dbc6ded1b141b5394af12e33f9ef959265b95a')}
expected={
 'CF82_RESERVE42_G5':(7511,'570a79b8cf5106fea03d398e410c25f281382ac95e841d55e0641eb02ffd23af'),
 'CF82_RESERVE83_G6':(15840,'3461b0931e788f69bfc59da9ee288b4268f55c29115fba6aa974033476bad356'),
 'CF82_MAIN83_G7':(17335,'742dd910d55e146aa00e82853846472e4f055d3f7dc19a4381295592fe7778b8')}
found={}
for name,text in re.findall(r'^### FILE ([^\n]+)\n```[^\n]*\n(.*?)^```',source,re.M|re.S):
 if name not in inputs:continue
 assert name not in found
 raw=(text.rstrip('\n') if name.endswith('.json') else text).encode('utf-8')
 assert (len(raw),hashlib.sha256(raw).hexdigest())==inputs[name],name
 found[name]=raw;(out/name).write_bytes(raw)
assert set(found)==set(inputs)
sys.path.insert(0,str(out));from exact_addition import audit,encode,controls
controls()
for name,receipt in expected.items():
 d=json.loads(found[name+'.json']);A=audit(d['points'],d['grid'])
 assert A['strict']==[2,1,1] and A['weak']==A['primitive_zeros']==[0,0,0]
 raw=(json.dumps(encode(A),sort_keys=True,separators=(',',':'))+'\n').encode()
 assert (len(raw),hashlib.sha256(raw).hexdigest())==receipt,name
 (out/(name+'_AUDIT.json')).write_bytes(raw)
 print('CF82_PRIMARY_EXACT_RECOVERY_MATCH_PASS',name,A['V'],A['E'],A['F'],A['strict'],flush=True)
print('CF82_THREE_PRIMARY_INPUT_AND_AUDIT_HASHES_PASS',flush=True)
```

### FILE CF82_RESERVE42_G5.json
```json
{"grid":100000,"points":[[-134781,124232,-57411],[55390,-26663,-58815],[93012,21290,-31323],[99464,38177,7683],[79885,38238,47046],[104939,-1363,30326],[102412,-27512,29686],[93912,-47154,37844],[82099,-60980,49734],[67854,-69183,64124],[50357,-75551,76847],[29936,-79891,87081],[6987,-82245,93885],[-17741,-83290,95712],[-43057,-83066,91851],[-68223,-79469,83743],[-92634,-71399,71625],[-115514,-55556,57491],[-134491,-33317,38892],[-146576,-2105,17406],[-149566,40418,-13182],[12570,-34730,-48726],[81034,1537,-48884],[96656,33821,-14778],[102963,26256,16025],[104344,13817,26565],[104640,-15183,28880],[98719,-38412,32500],[88329,-54750,43504],[75293,-65696,56723],[59468,-72732,70633],[40519,-77889,82402],[18772,-81127,91146],[-5229,-82974,95430],[-30407,-83201,94651],[-55766,-81813,88221],[-80514,-76008,78285],[-104430,-64929,64288],[-125663,-45526,48463],[-141709,-18580,28649],[-150053,18572,1715],[-141535,84112,-51489]]}
```

### FILE CF82_RESERVE83_G6.json
```json
{"grid":1000000,"points":[[-1386569,1203129,-552845],[542791,-287488,-647806],[936748,202320,-304446],[967120,408381,192919],[773682,366041,565249],[1047004,-14984,317074],[1023002,-275426,292729],[936836,-470120,378382],[819536,-604181,500174],[677952,-683380,644572],[503477,-744686,773102],[300314,-784260,878029],[69604,-813508,940587],[-177030,-831541,951099],[-428269,-834905,906213],[-678530,-791741,830142],[-919704,-698729,718474],[-1142631,-548972,569546],[-1330992,-326632,385284],[-1458036,-24615,166686],[-1505410,388885,-150409],[43940,-470958,-550743],[824521,19234,-498195],[973405,322945,-119814],[1038298,259286,153939],[1043319,145237,279803],[1047263,-151671,280020],[985415,-384734,321114],[881070,-545134,435513],[752153,-649662,570328],[594862,-715503,712182],[405838,-766332,829514],[187806,-799804,915688],[-52527,-824191,952585],[-300715,-842634,929000],[-555019,-814937,876216],[-799231,-747750,784565],[-1034348,-631206,649018],[-1242947,-446970,480931],[-1404920,-183142,278249],[-1491042,193864,25666],[-1410454,849080,-487291],[700451,-125359,-593972],[961121,266890,-212272],[1022882,327145,104374],[950704,287628,412192],[1049386,-84150,297966],[1005428,-330967,307359],[909880,-508733,406868],[786448,-629016,534291],[637472,-699585,679386],[455296,-757064,801384],[244775,-792227,898446],[8887,-819178,948314],[-239748,-833579,945448],[-492391,-829598,888815],[-740576,-773361,805365],[-978034,-667495,683084],[-1194714,-499784,525979],[-1370397,-257092,331910],[-1483255,78687,87182],[-1516785,841508,-274125],[301835,-411650,-637051],[891521,120415,-401891],[999450,363931,-21668],[1043799,203120,216289],[1049000,63950,294405],[1036424,-214785,287595],[962144,-428256,350355],[851044,-576334,467176],[716252,-666506,608355],[550361,-729486,744438],[353005,-779705,851589],[129220,-806952,929787],[-114610,-828270,953587],[-364447,-841516,917312],[-617298,-806283,852636],[-860369,-726011,751406],[-1089668,-592435,610176],[-1288828,-389298,432438],[-1434637,-106233,223650],[-1493758,299479,-50557],[-1408934,1023224,-543125]]}
```

### FILE CF82_MAIN83_G7.json
```json
{"grid":10000000,"points":[[-13865717,12031429,-5528461],[5427835,-2874792,-6477865],[9367420,2023157,-3044410],[9671125,4083641,1929171],[7736704,3660347,5652374],[10469995,-149832,3170683],[10229961,-2754243,2927305],[9368350,-4701186,3783830],[8195428,-6041844,5001777],[6779482,-6833798,6445669],[5034946,-7447022,7731220],[3003229,-7842745,8780432],[696058,-8135141,9405933],[-1770294,-8315392,9510967],[-4282659,-8348928,9062030],[-6785181,-7917223,8301217],[-9196786,-6987047,7184480],[-11426333,-5489742,5695471],[-13309959,-3266346,3852836],[-14580375,-246151,1666869],[-15054290,3888682,-1504340],[439201,-4709798,-5507704],[8245127,192341,-4981853],[9734032,3229400,-1198112],[10382907,2592851,1539398],[10433284,1452390,2798044],[10472470,-1516693,2800202],[9854078,-3847290,3211173],[8810799,-5451376,4355175],[7521544,-6496618,5703292],[5948753,-7155147,7121931],[4058496,-7663482,8295296],[1878105,-7998141,9156981],[-525264,-8241930,9525868],[-3007131,-8426298,9289917],[-5550127,-8149180,8762038],[-7992157,-7476961,7845735],[-10343515,-6312056,6490233],[-12429499,-4469722,4809321],[-14049232,-1831455,2782465],[-14910442,1938643,256663],[-14104671,8490695,-4873109],[7004438,-1253570,-5939621],[9611128,2668858,-2122676],[10228834,3271450,1043741],[9506955,2876265,4121840],[10493775,-841492,2979638],[10054265,-3309663,3073600],[9098813,-5087328,4068691],[7864526,-6290181,5342934],[6374844,-6995949,6793955],[4553103,-7570817,8014012],[2447811,-7922398,8984586],[88877,-8191824,9483180],[-2397482,-8335728,9454456],[-4923860,-8295878,8887988],[-7405618,-7733418,8053414],[-9780350,-6674978,6830825],[-11947165,-4997860,5259793],[-13704002,-2570956,3319085],[-14832655,786750,871688],[-15168109,8415495,-2740563],[3018288,-4116391,-6370593],[8915126,1204123,-4018840],[9994452,3639229,-216653],[10437967,2031190,2162889],[10490022,639506,2944049],[10364234,-2147851,2875956],[9621420,-4282546,3503552],[8510506,-5763338,4671820],[7162504,-6665054,6083544],[5503723,-7294981,7444490],[3530166,-7797194,8516067],[1292227,-8069605,9297959],[-1146102,-8282696,9535869],[-3644447,-8415084,9173018],[-6172884,-8062679,8526171],[-8603476,-7259890,7513807],[-10896703,-5924363,6101769],[-12888299,-3893019,4324354],[-14346426,-1062391,2236441],[-14937577,2994793,-505569],[-14089393,10232217,-5431397]]}
```

### FILE exact_addition.py
```python
"""Standalone exact maximal-hull / own-volume / S,U,H audit for rational point inputs.
Uses Python 3.13 standard library. Every decisive geometry comparison is exact.
One complete mechanical implementation plus distinct coordinate-boundary mass.
All indexed outputs use retained input labels, and lexicographically sorted planes.
"""
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations,product
from math import gcd,lcm
import json,sys,hashlib
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def audit(points,grid=1):
    P=list(map(tuple,points));assert len(set(P))==len(P)
    planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
        if n==(0,0,0):continue
        ss=[dot(n,p)-h for p in P]
        if min(ss)>=0:n=mul(n,-1);h=-h;ss=[-x for x in ss]
        if max(ss)>0:continue
        div=gcd(gcd(gcd(abs(n[0]),abs(n[1])),abs(n[2])),abs(h))
        key=tuple(x//div for x in n)+(h//div,)
        planes[key]=[v for v,s in enumerate(ss) if s==0]
    faces=[]
    for key,ids in sorted(planes.items()):
        n=key[:3];base=P[ids[0]];v=sub(P[ids[1]],base);w=cross(n,v)
        # Sort in exact oriented plane coordinates around point average.
        N=len(ids);s=tuple(sum(P[i][j] for i in ids) for j in range(3))
        uv={i:(dot(sub(mul(P[i],N),s),v),dot(sub(mul(P[i],N),s),w)) for i in ids}
        def cmp(i,j):
            a,b=uv[i],uv[j];ha=(a[1]<0 or (a[1]==0 and a[0]<0));hb=(b[1]<0 or(b[1]==0 and b[0]<0))
            if ha!=hb:return 1 if ha else -1
            c=a[0]*b[1]-a[1]*b[0]
            return -1 if c>0 else 1 if c<0 else 0
        cyc=sorted(ids,key=cmp_to_key(cmp))
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):
            vals=[dot(cross(sub(P[j],P[i]),sub(P[k],P[i])),n) for k in ids if k not in(i,j)]
            assert min(vals)>0,('non-extreme coplanar nomination',key)
        faces.append(dict(n=n,h=key[3],cycle=cyc))
    owners={};tri=[]
    for f,face in enumerate(faces):
        cyc=face['cycle']
        for i,j in zip(cyc,cyc[1:]+cyc[:1]):owners.setdefault(tuple(sorted((i,j))),[]).append(f)
        tri += [(cyc[0],cyc[k],cyc[k+1]) for k in range(1,len(cyc)-1)]
    verts=sorted(set(sum([x['cycle'] for x in faces],[])))
    assert len(verts)-len(owners)+len(faces)==2
    assert all(len(x)==2 for x in owners.values())
    # Connected vertex links and graph, true maximal complex, not just Euler.
    adj={i:set() for i in verts}
    for a,b in owners:adj[a].add(b);adj[b].add(a)
    seen={verts[0]};todo=list(seen)
    while todo:
        for j in adj[todo.pop()]-seen:seen.add(j);todo.append(j)
    assert len(seen)==len(verts)
    for i in verts:
        link={j:set() for j in adj[i]}
        for face in faces:
            c=face['cycle']
            if i in c:
                k=c.index(i);a,b=c[k-1],c[(k+1)%len(c)];link[a].add(b);link[b].add(a)
        assert all(len(x)==2 for x in link.values())
        reached={next(iter(link))};todo=list(reached)
        while todo:
            for j in link[todo.pop()]-reached:reached.add(j);todo.append(j)
        assert len(reached)==len(link)
    D=sum(det(P[a],P[b],P[c]) for a,b,c in tri);assert D>0
    N=tuple(sum(det(P[a],P[b],P[c])*(P[a][k]+P[b][k]+P[c][k]) for a,b,c in tri) for k in range(3))
    volume=F(D,6*grid**3);centroid=tuple(F(x,4*D*grid) for x in N)
    # Separate divergence integration: V=int_boundary x_k n_k, M_j=int_boundary x_j^2 n_j/2.
    vm=[];mm=[]
    for k in range(3):
        vtot=F(0);mtot=F(0)
        for a,b,c in tri:
            A=cross(sub(P[b],P[a]),sub(P[c],P[a]))[k]
            vals=[P[a][k],P[b][k],P[c][k]]
            vtot+=F(A*sum(vals),6)
            mtot+=F(A*(sum(vals)**2+sum(x*x for x in vals)),48)
        vm.append(vtot/grid**3);mm.append(mtot/grid**4)
    assert vm==[volume]*3 and all(mm[k]==volume*centroid[k] for k in range(3))
    X=[sub(mul(p,4*D),N) for p in P];nf=[f['n'] for f in faces];hf=[dot(f['n'],X[f['cycle'][0]]) for f in faces]
    assert min(hf)>0
    stable=[];weak_s=[];unst=[];weak_u=[];sad=[];weak_h=[];zeros=[0,0,0]
    for i,(n,h) in enumerate(zip(nf,hf)):
        vals=[hh*dot(n,n)-h*dot(nn,n) for j,(nn,hh) in enumerate(zip(nf,hf)) if j!=i]
        zeros[0]+=sum(v==0 for v in vals)
        if min(vals)>0:stable.append(i)
        elif min(vals)>=0:weak_s.append(i)
    for i in verts:
        vals=[dot(X[i],sub(X[j],X[i])) for j in adj[i]];zeros[1]+=sum(v==0 for v in vals)
        assert (max(vals)<0)==all(dot(X[i],sub(X[j],X[i]))<0 for j in verts if j!=i)
        if max(vals)<0:unst.append(i)
        elif max(vals)<=0:weak_u.append(i)
    for (a,b),(f,g) in sorted(owners.items()):
        e=sub(X[b],X[a]);dd=dot(e,e);t=-dot(X[a],e);w=add(mul(X[a],dd),mul(e,t));n,m=nf[f],nf[g]
        aa,bb,ab=dot(n,n),dot(m,m),dot(n,m);assert aa*bb-ab*ab>0
        ca=dot(w,n)*bb-dot(w,m)*ab;cb=dot(w,m)*aa-dot(w,n)*ab
        vals=[t,dd-t,ca,cb];zeros[2]+=sum(v==0 for v in vals)
        if min(vals)>0:sad.append([a,b])
        elif min(vals)>=0:weak_h.append([a,b])
    assert len(stable)+len(unst)-len(sad)==2 if not(weak_s or weak_u or weak_h) else True
    return dict(V=len(verts),E=len(owners),F=len(faces),C=2*len(owners),strict=[len(stable),len(unst),len(sad)],weak=[len(weak_s),len(weak_u),len(weak_h)],primitive_zeros=zeros,
      volume=volume,centroid=centroid,S=stable,U=unst,H=sad,weak_S=weak_s,weak_U=weak_u,weak_H=weak_h,faces=faces,edges=sorted(owners),active_inputs=verts,
      mass_method='oriented origin tetrahedra vs coordinate boundary divergence',common_centered_denominator_bits=lcm(*(F(x,4*D*grid).denominator for p in X for x in p)).bit_length())

def controls():
    tetra=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    a=audit(tetra);assert a['strict']==[4,4,6] and a['weak']==[0,0,0]
    prism=[(x,y,z) for x,y in [(1,0),(1,1),(-2,-1)] for z in (-1,1)]
    a=audit(prism);assert a['strict']==[4,4,6] and a['weak']==[1,2,3],encode(a)
    print('ADDITION_TETRA446_PRISM446_WEAK123_CONTROLS_PASS')
if __name__=='__main__':
    controls()
    if len(sys.argv)>1:
        d=json.loads(Path(sys.argv[1]).read_text());a=audit(d['points'],d['grid']);raw=(json.dumps(encode(a),sort_keys=True,indent=2)+'\n').encode()
        out=Path(sys.argv[2] if len(sys.argv)>2 else 'AUDIT.json');out.write_bytes(raw)
        print('C114_EXACT_ADDITION_AUDIT_PASS',a['V'],a['E'],a['F'],a['strict'],a['weak'],len(raw),hashlib.sha256(raw).hexdigest())
```
