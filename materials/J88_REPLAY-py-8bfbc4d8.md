# material-8bfbc4d8f8e1

AI research material

---

"""J88 exact recovery: two rational own121 endpoints and a coarse222 control.
Self-contained CPython 3.11+ standard library; no external inputs or optimizer.
Run python J88_REPLAY.py. Exact supporting triples, volume, own centroid,
strict/weak census and every positive primal/polar bar use Fraction.
The fixed-volume chart is valid where its chosen vertex-coordinate coefficient
is nonzero and the resulting oriented support complex remains valid.
Endpoint accuracy does not certify every point of the numerical producing path.
Expected marker: J88_EXACT_RECONSTRUCTION_PASS_OWN121_NOT_110.
"""
"""Exact rational hull and own-equilibrium checks. All predicates use Fraction."""
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def load():
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text())
    ip=[tuple(p) for p in data['points']]; faces=[]
    for a,b,c in combinations(range(len(ip)),3):
        n=cross(sub(ip[b],ip[a]),sub(ip[c],ip[a])); h=dot(n,ip[a])
        if n==(0,0,0): continue
        signs=[dot(n,p)-h for p in ip]
        if min(signs)<0<max(signs):continue
        if sum(t==0 for t in signs)!=3:raise ValueError('non-simplicial input')
        faces.append([a,b,c] if max(signs)==0 else [a,c,b])
    return [tuple(R(v,data['denominator']) for v in p) for p in ip],faces

def topology(p,faces):
    edges={};planes=[];verts=set()
    for i,f in enumerate(faces):
        verts.update(f);n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]])
        assert n!=(0,0,0)
        vals=[dot(n,x)-h for x in p]
        assert max(vals)==0,('invalid support',i,max(vals))
        assert {j for j,v in enumerate(vals) if v==0}==set(f),('coplanarity',i)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert verts==set(range(len(p)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
    assert len(p)-len(edges)+len(faces)==2
    return edges,planes

def mass(p,faces):
    W=R(0);K=(R(0),)*3
    for f in faces:
        a=p[f[0]]
        for i in range(1,len(f)-1):
            b,c=p[f[i]],p[f[i+1]];z=det(a,b,c)
            W+=z;K=add(K,mul(add(a,add(b,c)),z))
    assert W>0
    return W/6,mul(K,1/(4*W))

def bars(p,edges):
    rad=[dot(v,v) for v in p];parent=list(range(len(p)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(p[b],p[a]);t=max(R(0),min(R(1),-dot(p[a],d)/dot(d,d)))
        q=add(p[a],mul(d,t));events.append((dot(q,q),a,b))
    out=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        if rad[j]>level:out.append({'root':j,'birth2':str(rad[j]),'death2':str(level),'depth':str(1-level/rad[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(p))})==1
    return sorted(out,key=lambda b:R(b['depth']),reverse=True)

def audit(p,faces):
    edges,planes=topology(p,faces);V,g=mass(p,faces);xx=[sub(x,g) for x in p];yy=[]
    for n,h in planes:
        z=h-dot(n,g);assert z>0;yy.append(mul(n,1/z))
    def roots(x):
        strict=[];weak=[]
        for i,a in enumerate(x):
            m=max(dot(a,sub(b,a)) for j,b in enumerate(x) if i!=j)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(xx);S,WS=roots(yy);H=[];WH=[]
    for (a,b),ef in edges.items():
        d=sub(xx[b],xx[a]);t=-dot(xx[a],d)/dot(d,d);r=add(xx[a],mul(d,t))
        n,m=planes[ef[0][0]][0],planes[ef[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(e[0][0],e[1][0]) for e in edges.values()]
    return dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=str(V),centroid=list(map(str,g)),strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],S=S,U=U,H=H,P=bars(xx,list(edges)),Q=bars(yy,dual))


from math import lcm
import hashlib

def dump(name,obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/name).write_bytes(raw)
    return dict(name=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def exact_hull(p):
    D=lcm(*(x.denominator for v in p for x in v));rows=[tuple(int(x*D) for x in v) for v in p];fs=[]
    for a,b,c in combinations(range(len(rows)),3):
        n=cross(sub(rows[b],rows[a]),sub(rows[c],rows[a]));h=dot(n,rows[a])
        if n==(0,0,0):continue
        vals=[dot(n,v)-h for v in rows]
        if min(vals)<0<max(vals):continue
        assert sum(v==0 for v in vals)==3,'nonsimplicial endpoint'
        fs.append([a,b,c] if max(vals)==0 else [a,c,b])
    assert set(range(len(rows)))=={i for f in fs for i in f},'some row is not a true vertex'
    return fs

def correct(p,fs,V0,pivot=(16,1)):
    """A rational chart wherever the selected volume coefficient is nonzero."""
    a,k=pivot;A=R(0)
    for f in fs:
        if a not in f:continue
        pos=f.index(a);j,l=f[(pos+1)%3],f[(pos+2)%3]
        A+=cross(p[j],p[l])[k]/6
    assert A!=0
    V,g=mass(p,fs);alpha=(V0-V)/A
    q=[list(v) for v in p];q[a][k]+=alpha;q=list(map(tuple,q))
    V1,g1=mass(q,fs);assert V1==V0
    q=[sub(v,g1) for v in q];assert mass(q,fs)==(V0,(0,0,0))
    topology(q,fs)
    return q,dict(pivot=list(pivot),coefficient=str(A),correction=str(alpha),translation=list(map(str,g1)))

def cube(p,fs):
    """S1 sufficient open centre cube, using best all-facet and adjacent witnesses.
Maximum rho returned is a strict boundary: certificate uses rho/2 on closed cube.
"""
    ed,planes=topology(p,fs);V,g=mass(p,fs)
    ns=[a for a,b in planes];hs=[b-dot(a,g) for a,b in planes]
    adj=[set() for f in fs]
    for ef in ed.values():a,b=ef[0][0],ef[1][0];adj[a].add(b);adj[b].add(a)
    inside=min(h/sum(map(abs,n)) for h,n in zip(hs,ns));bounds={};roots=[]
    for i,n in enumerate(ns):
        values=[];nn=dot(n,n)
        for j,m in enumerate(ns):
            if i==j:continue
            nm=dot(n,m);W=nm*hs[i]-nn*hs[j];a=sub(mul(m,nn),mul(n,nm));den=sum(map(abs,a))
            values.append((j,W,None if den==0 else abs(W)/den))
        if all(w<0 for _,w,_ in values):roots.append(i)
        bounds[i]=values
    assert len(roots)==1,roots
    sf=roots[0];out={}
    for mode in ['all','adjacent']:
        cert=[];lim=inside
        for i in range(len(fs)):
            vals=bounds[i]
            if i==sf:
                for j,w,r in vals:
                    assert w<0
                    if r is not None:lim=min(lim,r)
            else:
                cand=[(r,j) for j,w,r in vals if w>0 and r is not None and (mode=='all' or j in adj[i])]
                assert cand,('no positive eligible witness',mode,i)
                r,j=max(cand);lim=min(lim,r);cert.append([i,j,str(r)])
        out[mode]=dict(open_rho=str(lim),open_rho_float=float(lim),closed_rho=str(lim/2),witnesses=cert)
    return dict(stable_facet=fs[sf],centre=list(map(str,g)),policies=out)


G8={"denominator":100000000,"name":"J88_FULL_B_G8","points":[[-150695683,-96552263,67428419],[-85207768,-10614819,-53620143],[-66982613,10330368,33912478],[-58297708,26422981,24244823],[-56106479,34280462,-2248037],[-54555978,1255060,-75551804],[-55539569,34390016,-12938269],[-37711497,4308265,-83041110],[-38675044,49452236,5530704],[-30483925,52917484,-24083944],[-21774146,4218067,-87031303],[-11126320,4143579,-88374206],[-15420140,51319826,35842101],[-7843052,75127303,-15400387],[-7616792,78193605,-565010],[-1058703,4443644,-88478715],[3521667,70872697,-25605975],[3535415,79400021,15805845],[8934756,1954284,-87510345],[6774529,-35993037,-43654638],[12384339,59655944,-35866034],[18315136,530160,-85509416],[18371409,78032232,35579212],[18793874,50382251,-43158698],[24028997,73414157,40932017],[28561541,45452704,52964479],[33574403,71398793,45084620],[44382426,69596759,48321040],[67482575,63568615,52272793],[76323055,57190184,52880763],[77665836,-21869956,-65744115],[82999327,48806290,52368885],[89348450,40024794,50497050],[90873614,49886620,27767471],[95428612,30869357,47082077],[99404320,13965747,-43810474],[100835576,21707227,42147207],[105543740,25683974,-16267245],[105651809,12471743,35383949],[109402571,3888791,27211946],[112454652,-20287473,-25181272],[113806455,-16789911,-8017337],[112172110,-4133648,17227140],[113735887,-11220719,5351438],[114726502,-10126070,-13373282],[83574577,-28783095,-27600354]]}
G6={"denominator":1000000,"name":"J88_FULL_B_G6","points":[[-1506957,-965523,674284],[-852078,-106148,-536201],[-669826,103304,339125],[-582977,264230,242448],[-561065,342805,-22480],[-545560,12551,-755518],[-555396,343900,-129383],[-377115,43083,-830411],[-386750,494522,55307],[-304839,529175,-240839],[-217741,42181,-870313],[-111263,41436,-883742],[-154201,513198,358421],[-78431,751273,-154004],[-76168,781936,-5650],[-10587,44436,-884787],[35217,708727,-256060],[35354,794000,158058],[89348,19543,-875103],[67745,-359930,-436546],[123843,596559,-358660],[183151,5302,-855094],[183714,780322,355792],[187939,503823,-431587],[240290,734142,409320],[285615,454527,529645],[335744,713988,450846],[443824,695968,483210],[674826,635686,522728],[763231,571902,528808],[776658,-218700,-657441],[829993,488063,523689],[893485,400248,504971],[908736,498866,277675],[954286,308694,470821],[994043,139657,-438105],[1008356,217072,421472],[1055437,256840,-162672],[1056518,124717,353839],[1094026,38888,272119],[1124547,-202875,-251813],[1138065,-167899,-80173],[1121721,-41336,172271],[1137359,-112207,53514],[1147265,-101261,-133733],[835746,-287831,-276004]]}
EXPECTED=[{'bytes': 1153, 'name': 'J88_FULL_B_G6_INPUT.json', 'sha256': '0f29a44b357e490cadb4ac900c11bd811e56fc39be84d399c6925b15fd9237f2'}, {'bytes': 1233, 'name': 'J88_FULL_B_G6_EXACT.json', 'sha256': 'b7460766da6ccb663de198ea9bfcf0925ed9e9b9a4ae76953ef2d60e2953cbb8'}, {'bytes': 1431, 'name': 'J88_FULL_B_G8_INPUT.json', 'sha256': '9ce7afd63030c533c48f553a626c7b2ade91bb34bd2d55d8d81d4e12c8f75ffd'}, {'bytes': 23308, 'name': 'J88_FULL_B_G8_EXACT.json', 'sha256': '6af7ea15abdcd11c60d935796af6c5780c9e6a91896063f7fe2fbb7eb60bf987'}, {'bytes': 59957, 'name': 'J88_FULL_B_G8_MASS_EXACT.json', 'sha256': '24e7515e993fe04ecd8e263733d1272832172154931e58b1653fbef7f9b89574'}]

V0=R(3791834665223904409031391864938220273,2000000000000000000000000000000000000)

def main():
    got=[]
    for data in [G6,G8]:
        name=data['name'];got.append(dump(name+'_INPUT.json',data))
        p=[tuple(R(x,data['denominator']) for x in row) for row in data['points']]
        f=exact_hull(p);r=audit(p,f);r['name']=name
        assert (r['V'],r['E'],r['F'])==(46,132,88) and r['weak']==[0,0,0]
        if data is G6:
            assert r['strict']==[2,2,2] and len(r['P'])==len(r['Q'])==1
        else:
            assert r['strict']==[1,2,1] and len(r['P'])==1 and not r['Q']
            r['S1_cube']=cube(p,f)
        got.append(dump(name+'_EXACT.json',r))
        print(name,r['strict'],r['weak'],[float(R(x['depth'])) for x in r['P']],
              [float(R(x['depth'])) for x in r['Q']])
        if data is G8:
            q,cor=correct(p,f,V0);name='J88_FULL_B_G8_MASS';rr=audit(q,f)
            rr.update(name=name,correction=cor,points=[[str(x) for x in v] for v in q],faces=f,S1_cube=cube(q,f))
            assert rr['strict']==[1,2,1] and rr['weak']==[0,0,0]
            assert R(rr['volume'])==V0 and rr['centroid']==['0','0','0']
            assert len(rr['P'])==1 and not rr['Q']
            got.append(dump(name+'_EXACT.json',rr))
            print(name,rr['V'],rr['E'],rr['F'],rr['strict'],rr['weak'],
                  float(R(rr['P'][0]['depth'])),rr['S1_cube']['policies']['all']['open_rho_float'])
    assert got==EXPECTED,(got,EXPECTED)
    dump('J88_REPLAY_MANIFEST.json',got)
    print('J88_EXACT_RECONSTRUCTION_PASS_OWN121_NOT_110')

if __name__=='__main__':main()
