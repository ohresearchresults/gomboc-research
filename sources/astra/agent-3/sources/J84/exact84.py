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
