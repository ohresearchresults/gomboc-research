# J84 exact centre trap and finite-cap controls — complete recovery capsule

These are coordinator-executed results on the literal J82_S1_ROBUST_G6 body from material att_c4e5a2307816bde60574_01, not RA40_LATTICE220 itself, not B7, and not C622. The complete input is repeated below because this capsule is self-contained. No old sandbox, optimizer, or FULL76 is required. No new own110 was found; canonical C622 is unchanged.

## Exact findings and limits
The unchanged parent is V45/E129/F86,C258, own121, additionalweak000, P=.5678697406886946. In its given material-row ordering (not lexicographic canonical ordering), vertex0 is strict U. Let B={28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44}. Its27 outward edges have strictly negative radial scores for every reference centre with infinity distance <=3883/10000 from the own centroid. A maximum-radius vertex in B is therefore also strict U: for an internal neighbor w, the score is at most -|w-v|^2/2; outward scores are strictly negative by the certificate. Thus U>=2 throughout that cube, independent of S and independent of root turnover within B.
The exact limiting negative-cut threshold is 116515824167231702315178289397/300023165309328090694220250000, approximately .38835609259405773. The same fixed cut works for every strictly smaller radius. Vertex0's own sufficient radius is 2269091939834332130335499284871/2299254003592521137972892500000, approximately .9868818043978345. Consequently any interior reference point with U=1 on the UNCHANGED hull must have infinity displacement at least the former threshold. The threshold is optimal for the particular potential-edge minimax certificate, not asserted to be the true distance to the nearest U1 centre. Potential edges at different centres need not be simultaneously realizable. For altered geometry the proof requires explicitly retained negative crossing geometry; it is not a theorem against arbitrary physical surgery.
A purely mass-geometric consequence: removing relative volume m from the parent shifts its centroid by at most m/(1-m)*Dinf, where Dinf=max|p-g|inf. Therefore leaving the above open cube by cut-only mass change requires m >= 932126593337853618521426315176/4553756999997000623653443348919, approximately .20469396881266777. This is a centre-displacement bound, NOT a lower bound on material required for own110 after changing the boundary. Boundary changes can invalidate the retained-cut hypothesis before that displacement.

Two exactly frozen physical halfspace cuts demonstrate numerical-objective limitations. Keep n.x<=h using the literal integers in caps_exact84.py (a common scaling of n,h is irrelevant).
* J84_SMALL_WITNESS_CAP_G8: V51/E136/F87,C272, own121, weak000, P=.5678702165067933. Its numerical nonroot witness loss was about2e-14, yet the finite basin did not disappear and is slightly deeper than the parent's.
* J84_BAR_CAP_G8: V52/E137/F87,C274, own(1,6,5), weak000. All five exact positive P depths are approximately .5408823863525646,1.1241497995019025e-6,2.6869891759253795e-8,1.0000803257038518e-12,8.979055805714126e-13. No Q bars. A floating1e-12 bar floor hid positive bars; exact full census and fractions are authoritative. These are useful nonwinners, not progress to110 by merely reducing the largest bar.

## Reconstruction and manifests
Save each fenced source verbatim with a final LF. Run with CPython3.13.5 standard library:
python exact84.py
python cubetrap84.py
python caps_exact84.py

Expected markers:
J84_EXACT_BASE [1, 2, 1] [0, 0, 0]
J84_REFERENCE_CUBE_U_GE_2_EXACT_PASS 3883/10000 17 27
J84_EXACT_FINITE_CAP_CONTROLS_PASS_NO_110

Input/source bytes and SHA-256:
J82_S1_ROBUST_G6_INPUT.json 1153 753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab
exact84.py 6333 144a8b82a1e62ad42368a02597a79958a38bab3e320e3caa499a941588105835
cubetrap84.py 2105 c963f4fcb4e6d0baed73220c9a26f6e5be4c286291fa1133edd617314ec93b23
caps_exact84.py 958 aee19ae28f1a0dd8627defa49b32fdb57d33c46d86b9f239d33f7a0b6ccf01df

Reproduced outputs:
J84_BASE_EXACT.json 4190 c47ed668404071349edaf5176503597091f726cc361a01c6303775e221f2b777
J84_CUBE_TRAP.json 12844 5feb07233374d15878eec7da5e2e41f8921b1dfd83ed61a5e4df8cead20ecc64
J84_SMALL_WITNESS_CAP_G8.json 9882 4e75d2a42523cbacd11a39ddd311344b55498d6ab325c2812b85cd6aa4bc3b55
J84_BAR_CAP_G8.json 23938 de521692f09b7bf56fbde205567a5e075ef2e1632001156e58ae9ade7bee329d

## J82_S1_ROBUST_G6_INPUT.json
```json
{"denominator":1000000,"name":"J82_S1_ROBUST_G6","points":[[-1772498,-1222476,446600],[-1039299,-313302,-700462],[-1003288,-275901,132016],[-809479,-13170,17208],[-790129,68868,-233475],[-774789,-231542,-897502],[-797981,62277,-350742],[-635384,-210168,-961663],[-609466,221337,-171601],[-525729,253449,-484224],[-489649,-200686,-996078],[-374946,-195685,-1011378],[-366813,246691,105757],[-316429,451849,-418573],[-295644,503340,-233141],[-275629,-186981,-1011480],[-229896,416128,-495865],[-194308,509959,-88421],[-195520,-211846,-1005706],[-187899,-558943,-768752],[-134126,305378,-589651],[-126147,-264851,-992981],[-49174,491813,93901],[-35621,178251,-677618],[-10288,436303,144281],[28080,186153,253802],[64850,412231,179729],[185379,412442,205366],[400273,357835,238447],[436566,275260,247302],[489402,-473343,-873790],[533167,226150,240322],[619725,163301,221898],[662701,219162,-3537],[666794,75353,193396],[728134,-96722,-608110],[740107,2105,147220],[797950,1378,-368423],[797491,-77809,85715],[835835,-160959,8618],[877002,-392469,-517165],[833841,-381745,-334567],[864938,-239770,-88025],[882247,-308985,-203874],[889527,-317124,-393548]]}
```

## exact84.py
```python
"""Standard-library exact hull, mass, equilibrium, and radial-bar calculations."""
from fractions import Fraction as R
from itertools import combinations
from math import gcd
from functools import reduce
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def load():
    data=json.loads((ROOT/'J82_S1_ROBUST_G6_INPUT.json').read_text())
    pts=[tuple(R(v,data['denominator']) for v in row) for row in data['points']]
    # Integer supports for the generic simplicial parent; all triples are tested.
    pp=[tuple(row) for row in data['points']];faces=[]
    for a,b,c in combinations(range(len(pp)),3):
        nn=cross(sub(pp[b],pp[a]),sub(pp[c],pp[a])); hh=dot(nn,pp[a])
        if nn==(0,0,0):continue
        sg=[dot(nn,p)-hh for p in pp]
        if min(sg)<0<max(sg):continue
        if sum(t==0 for t in sg)!=3:raise ValueError('Parent is not simplicial')
        faces.append([a,b,c] if max(sg)==0 else [a,c,b])
    assert len(faces)==86
    return pts,faces

def topology(pts,faces):
    edge={};planes=[]; vv=set()
    for i,f in enumerate(faces):
        vv.update(f);n=cross(sub(pts[f[1]],pts[f[0]]),sub(pts[f[2]],pts[f[0]]));h=dot(n,pts[f[0]])
        assert n!=(0,0,0)
        assert all(dot(n,p)<=h for p in pts)
        assert {j for j,p in enumerate(pts) if dot(n,p)==h}==set(f)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edge.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert vv==set(range(len(pts)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edge.values())
    assert len(pts)-len(edge)+len(faces)==2
    seen={0};stack=[0];adj=[[] for _ in faces]
    for v in edge.values():i,j=v[0][0],v[1][0];adj[i].append(j);adj[j].append(i)
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    assert len(seen)==len(faces)
    return edge,planes

def mass(pts,faces):
    r=tuple(sum(p[k] for p in pts)/len(pts) for k in range(3))
    ts=[]
    for f in faces:
        for k in range(1,len(f)-1):
            a,b,c=[pts[t] for t in (f[0],f[k],f[k+1])]
            d=det(sub(a,r),sub(b,r),sub(c,r));assert d>0
            ts.append((d,add(r,add(a,add(b,c)))))
    ds=sum(d for d,x in ts)
    g=tuple(sum(d*x[k] for d,x in ts)/(4*ds) for k in range(3))
    return ds/6,g

def radial_bars(pts,edges):
    radii=[dot(p,p) for p in pts];parent=list(range(len(pts)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(pts[b],pts[a]);t=max(R(0),min(R(1),-dot(pts[a],d)/dot(d,d)))
        q=add(pts[a],scale(d,t));events.append((dot(q,q),a,b))
    bars=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (radii[i],-i)<(radii[j],-j):i,j=j,i
        if radii[j]>level:bars.append({'root':j,'birth2':str(radii[j]),'death2':str(level),'depth':str(1-level/radii[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(pts))})==1
    return sorted(bars,key=lambda b:R(b['depth']),reverse=True)

def audit(pts,faces,centre=None):
    edges,planes=topology(pts,faces);vol,own=mass(pts,faces);g=own if centre is None else centre
    p=[sub(x,g) for x in pts];q=[]
    for n,h in planes:
        a=h-dot(n,g);assert a>0;q.append(scale(n,1/a))
    def roots(xx):
        strict=[];weak=[]
        for i,x in enumerate(xx):
            scores=[dot(x,sub(y,x)) for j,y in enumerate(xx) if i!=j]
            m=max(scores)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(p);S,WS=roots(q);H=[];WH=[]
    for (a,b),ee in edges.items():
        d=sub(p[b],p[a]);t=-dot(p[a],d)/dot(d,d);r=add(p[a],scale(d,t))
        n,m=planes[ee[0][0]][0],planes[ee[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(ee[0][0],ee[1][0]) for ee in edges.values()]
    return {'V':len(pts),'E':len(edges),'F':len(faces),'C':2*len(edges),'volume':str(vol),
            'own_centroid':[str(x) for x in own],'reference_centroid':[str(x) for x in g],
            'is_own':g==own,'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],
            'S':S,'U':U,'H':H,'weak_S':WS,'weak_U':WU,'weak_H':WH,
            'P':radial_bars(p,list(edges)),'Q':radial_bars(q,dual),
            'faces':faces,'points':[[str(t) for t in x] for x in pts]}

def clip(pts,faces,n,h):
    edges,_=topology(pts,faces);dd=[dot(n,p)-h for p in pts]
    assert min(dd)<0<max(dd) and all(d!=0 for d in dd)
    kept=[i for i,d in enumerate(dd) if d<0];Q=[pts[i] for i in kept];old={v:i for i,v in enumerate(kept)};new={}
    for a,b in sorted(edges):
        if dd[a]*dd[b]<0:
            new[(a,b)]=len(Q);Q.append(scale(sub(scale(pts[b],dd[a]),scale(pts[a],dd[b])),1/(dd[a]-dd[b])))
    ff=[];cut_segments=[]
    for f in faces:
        row=[]
        for a,b in zip(f,f[1:]+f[:1]):
            if dd[a]<0:row.append(old[a])
            if dd[a]*dd[b]<0:row.append(new[tuple(sorted((a,b)))])
        if len(row)>=3:
            ff.append(row)
            for a,b in zip(row,row[1:]+row[:1]):
                if a>=len(kept) and b>=len(kept):cut_segments.append((b,a))
    nxt=dict(cut_segments);start=min(nxt);cap=[start]
    while nxt[cap[-1]]!=start:
        cap.append(nxt[cap[-1]]);assert len(cap)<=len(nxt)
    assert len(cap)==len(nxt);ff.append(cap)
    return Q,ff

if __name__=='__main__':
    P,F=load();rep=audit(P,F)
    assert rep['strict']==[1,2,1] and rep['weak']==[0,0,0]
    assert rep['volume']=='1648544600316925211/1000000000000000000'
    (ROOT/'J84_BASE_EXACT.json').write_text(json.dumps(rep,sort_keys=True,separators=(',',':'))+'\n')
    print('J84_EXACT_BASE',rep['strict'],rep['weak'],[float(R(b['depth'])) for b in rep['P']])
```

## cubetrap84.py
```python
"""Exact robust U trap for an unchanged J82_G6 surface, arbitrary centre drift."""
import json
from fractions import Fraction as R
from exact84 import load,topology,mass,dot,sub,ROOT
P,F=load();ed,_=topology(P,F);V,g=mass(P,F)
threshold={}
for a,b in ed:
    for i,j in [(a,b),(b,a)]:
        d=sub(P[j],P[i]);f=dot(sub(P[i],g),d)
        threshold[i,j]=max(R(0),-f/sum(abs(x) for x in d))
# Least possible maximum threshold on a directed route to 0.
dist=[None]*len(P);dist[0]=R(0)
for _ in range(len(P)):
    changed=False
    for (i,j),t in threshold.items():
        if dist[j] is not None:
            d=max(t,dist[j])
            if dist[i] is None or d<dist[i]:dist[i]=d;changed=True
    if not changed:break
assert all(d is not None for d in dist)
root0=min(t for (i,j),t in threshold.items() if i==0)
critical=max(dist);eps=min(root0,critical)
print('root0_limit',float(root0),'trap_limit',float(critical),'combined',float(eps))
for rho in [R(1,1000),R(1,100),R(1,40),R(1,20),eps*R(99,100)]:
    B=[i for i,d in enumerate(dist) if d>rho]
    valid=B and rho<root0
    print('rho',float(rho),'Bsize',len(B),'valid',bool(valid))
# Use a simple exact radius below the maximal threshold.
rho=R(int(float(eps)*10000),10000)
assert rho>0 and rho<eps
B=[i for i,d in enumerate(dist) if d>rho]
cut=[(i,j) for i,j in threshold if i in B and j not in B]
proof=[]
for i,j in cut+[(i,j) for i,j in threshold if i==0]:
    d=sub(P[j],P[i]);f=dot(sub(P[i],g),d);L=sum(abs(x) for x in d);upper=f+rho*L
    assert upper<0
    proof.append({'edge':[i,j],'f_own':str(f),'L1':str(L),'upper':str(upper)})
out={'rho':str(rho),'own_centroid':[str(x) for x in g],'B':B,'cut':[list(e) for e in cut],
     'proof':proof,'root0_limit':str(root0),'minimax_limit':str(critical),'distances':[str(x) for x in dist],
     'scope':'Unchanged hull and every arbitrary reference centre in closed infinity cube. No inference for changed cut/interface geometry.'}
(ROOT/'J84_CUBE_TRAP.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
print('J84_REFERENCE_CUBE_U_GE_2_EXACT_PASS',str(rho),len(B),len(cut))
```

## caps_exact84.py
```python
"""Freeze and audit specified finite caps; no optimizer required for replay."""
import json,hashlib
from fractions import Fraction as R
from exact84 import load,clip,audit,ROOT
P,F=load()
# Literal D=1e8 nominations. Both the normal and height share that denominator.
CASES={
 'J84_SMALL_WITNESS_CAP_G8':([49641352,-84919108,18013364],67547761),
 'J84_BAR_CAP_G8':([94301537,-19495777,-26965437],95968983),
}
for name,(n,h) in CASES.items():
    Q,ff=clip(P,F,tuple(map(R,n)),R(h));s=audit(Q,ff);s['name']=name;s['cut_normal_integers']=n;s['cut_height_integer']=h
    raw=(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/(name+'.json')).write_bytes(raw)
    print(name,s['V'],s['E'],s['F'],s['strict'],s['weak'],len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    print('P',[float(R(x['depth'])) for x in s['P']],'Q',[float(R(x['depth'])) for x in s['Q']],flush=True)
print('J84_EXACT_FINITE_CAP_CONTROLS_PASS_NO_110',flush=True)
```
