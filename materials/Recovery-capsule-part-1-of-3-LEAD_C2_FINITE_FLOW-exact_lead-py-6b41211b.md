# material-6b41211b97dd

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Complete rational convex-polyhedron audit for the lead's new C2 candidates.
Derived explicitly from exact_c2.py ([internal-source-reference]), not an
independent auditor. Python3.13.5 standard library. Exhaustive integer hull,
maximal polygons, two-origin mass, direct mixed mechanics, tied-level P/Q.
Input: JSON {identity,scale,rows}. Output records all exact data and both forests.
Usage: python -B -S exact_lead.py input.json output.audit.json
       python -B -S exact_lead.py --controls
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict,deque

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x

def polygon(P,ids,n):
    drop=max(range(3),key=lambda j:abs(n[j]));ax=[j for j in range(3) if j!=drop]
    rows=sorted((P[i][ax[0]],P[i][ax[1]],i) for i in ids)
    def area(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in rows:
        while len(lo)>=2 and area(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(rows):
        while len(hi)>=2 and area(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    cyc=[r[2] for r in lo[:-1]+hi[:-1]];assert len(cyc)>=3
    if dot(cross(sub(P[cyc[1]],P[cyc[0]]),sub(P[cyc[2]],P[cyc[0]])),n)<0:cyc.reverse()
    k=cyc.index(min(cyc));return cyc[k:]+cyc[:k]

def hull(source):
    assert len(source)==len(set(source));planes={}
    for ia,ib,ic in combinations(range(len(source)),3):
        a,b,c=source[ia],source[ib],source[ic];n=cross(sub(b,a),sub(c,a))
        if n==(0,0,0):continue
        h=dot(n,a);side=0;bad=False;zeros=[]
        for j,p in enumerate(source):
            v=dot(n,p)-h
            if v:
                s=1 if v>0 else -1
                if side and side!=s:bad=True;break
                side=s
            else:zeros.append(j)
        if bad:continue
        assert side,'input not full-dimensional'
        if side>0:n=mul(-1,n);h=-h
        g=math.gcd(*n);n=tuple(v//g for v in n);h//=g;planes[(*n,h)]=zeros
    assert len(planes)>=4
    raw=sorted(((polygon(source,ids,key[:3]),key) for key,ids in planes.items()),key=lambda x:tuple(x[0]))
    used=sorted(set(i for cyc,key in raw for i in cyc));mp={x:i for i,x in enumerate(used)}
    P=[source[i] for i in used];faces=[[mp[i] for i in cyc] for cyc,key in raw];eq=[key for cyc,key in raw]
    owners=defaultdict(list)
    for f,cyc in enumerate(faces):
        n=eq[f][:3];h=eq[f][3];assert all(dot(n,p)<=h for p in source)
        assert all(dot(n,P[i])==h for i in cyc)
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):owners[tuple(sorted((a,b)))].append((f,a,b))
    E=sorted(owners);adj=[[] for _ in P];fa=[[] for _ in faces]
    for a,b in E:
        o=owners[(a,b)];assert len(o)==2 and o[0][1:]==o[1][:0:-1]
        adj[a].append(b);adj[b].append(a);fa[o[0][0]].append(o[1][0]);fa[o[1][0]].append(o[0][0])
    assert len(P)-len(E)+len(faces)==2
    seen={0};stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    assert len(seen)==len(P)
    return P,used,faces,eq,E,owners,adj,fa

def mass(P,faces,origin=(0,0,0)):
    v6=0;m=(0,0,0)
    for cyc in faces:
        a=sub(P[cyc[0]],origin)
        for j in range(1,len(cyc)-1):
            b=sub(P[cyc[j]],origin);c=sub(P[cyc[j+1]],origin);d=det(a,b,c)
            v6+=d;m=add(m,mul(d,add(add(a,b),c)))
    assert v6>0
    return F(v6,6),add(origin,tuple(F(v,4*v6) for v in m))

def landscape(X,E):
    birth=[dot(x,x) for x in X];levels={};adj=[[] for _ in X];weights=[]
    for k,(i,j) in enumerate(E):
        a=birth[i];c=birth[j];b=dot(X[i],X[j]);w=a if b>=a else c if b>=c else F(a*c-b*b,a+c-2*b)
        weights.append(w);levels.setdefault(w,[]).append(k);adj[i].append((j,k));adj[j].append((i,k))
    par=list(range(len(X)));peak=list(range(len(X)));members=[{i} for i in range(len(X))];bars=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for w in sorted(levels,reverse=True):
        local=defaultdict(set)
        for k in levels[w]:
            i,j=E[k];a,b=find(i),find(j)
            if a!=b:local[a].add(b);local[b].add(a)
        remaining=set(local)
        while remaining:
            first=min(remaining);group={first};stack=[first];remaining.remove(first)
            while stack:
                for j in local[stack.pop()]:
                    if j not in group:group.add(j);stack.append(j);remaining.remove(j)
            elder=max(group,key=lambda r:(birth[peak[r]],-peak[r]));ep=peak[elder]
            for r in sorted(group):
                p=peak[r]
                if r==elder or birth[p]<=w:continue
                comp=sorted(i for i in members[r] if birth[i]>w);cs=set(comp)
                cut=[list(e) for e in E if (e[0] in cs)!=(e[1] in cs)]
                prev={p:None};queue=deque([p])
                while queue and ep not in prev:
                    i=queue.popleft()
                    for j,k in sorted(adj[i]):
                        if weights[k]>=w and j not in prev:prev[j]=i;queue.append(j)
                assert ep in prev;path=[ep]
                while path[-1]!=p:path.append(prev[path[-1]])
                path.reverse();lookup={e:weights[k] for k,e in enumerate(E)}
                death_edges=[sorted((a,b)) for a,b in zip(path,path[1:]) if lookup[tuple(sorted((a,b)))]==w];assert death_edges
                bars.append(dict(peak=p,elder=ep,birth=birth[p],death=w,death_relative=(birth[p]-w)/w,birth_relative=(birth[p]-w)/birth[p],component=comp,cut=cut,path=path,death_edges=death_edges))
            united=set().union(*(members[r] for r in group))
            for r in group:par[r]=elder
            members[elder]=united
    assert len({find(i) for i in range(len(X))})==1
    return dict(nodes=X,edges=E,births=birth,edge_minima=weights,bars=bars)

def audit(data):
    scale=int(data['scale']);source=[tuple(map(int,p)) for p in data['rows']]
    P,used,faces,eq,E,owners,adj,fa=hull(source)
    V,c=mass(P,faces);origin=tuple(F(sum(p[j] for p in P),len(P)) for j in range(3));V2,c2=mass(P,faces,origin);assert V==V2 and c==c2
    L=math.lcm(*(x.denominator for x in c));C=tuple(int(x*L) for x in c);X=[sub(mul(L,p),C) for p in P]
    normals=[q[:3] for q in eq];supports=[L*h-dot(n,C) for *n,h in eq];assert min(supports)>0
    Q=[tuple(F(v,h) for v in nn) for nn,h in zip(normals,supports)]
    strict={'S':[],'U':[],'H':[]};weak={'S':[],'U':[],'H':[]};zeros={'S':0,'U':0,'H':0};esc=[]
    for i,x in enumerate(X):
        vals=[dot(x,sub(X[j],x)) for j in adj[i]];zeros['U']+=sum(v==0 for v in vals)
        if max(vals)<0:strict['U'].append(i)
        elif max(vals)==0:weak['U'].append(i)
        else:
            j=max(adj[i],key=lambda j:(dot(x,sub(X[j],x)),-j));a=dot(x,sub(X[j],x));assert a>0
            esc.append(dict(source=i,target=j,dot=a,cosine_squared=F(a*a,dot(x,x)*dot(sub(X[j],x),sub(X[j],x)))))
    for f,nn in enumerate(normals):
        vals=[dot(nn,normals[g])*supports[f]-dot(nn,nn)*supports[g] for g in fa[f]];zeros['S']+=sum(v==0 for v in vals)
        if max(vals)<0:strict['S'].append(f)
        elif max(vals)==0:weak['S'].append(f)
        foot=[];cyc=faces[f];norm2=dot(nn,nn)
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):foot.append(dot(cross(sub(X[b],X[a]),sub(mul(supports[f],nn),mul(norm2,X[a]))),nn))
        assert (min(foot)>0)==(f in strict['S']);assert (min(foot)==0)==(f in weak['S'])
    for a,b in E:
        d=sub(X[b],X[a]);dd=dot(d,d);ad=dot(X[a],d);rnum=sub(mul(dd,X[a]),mul(ad,d))
        f,g=[v[0] for v in owners[(a,b)]];nf,ng=normals[f],normals[g];aa=dot(nf,nf);bb=dot(ng,ng);ab=dot(nf,ng);D=aa*bb-ab*ab;assert D>0
        A=dot(rnum,nf)*bb-dot(rnum,ng)*ab;B=dot(rnum,ng)*aa-dot(rnum,nf)*ab
        assert mul(D,rnum)==add(mul(A,nf),mul(B,ng));vals=[-ad,dd+ad,A,B];zeros['H']+=sum(v==0 for v in vals)
        if min(vals)>0:strict['H'].append([a,b])
        elif min(vals)==0:weak['H'].append([a,b])
    QE=sorted({tuple(sorted(v[0] for v in owners[e])) for e in E});PS=landscape(X,E);QS=landscape(Q,QE)
    if not any(weak.values()):
        assert len(strict['S'])+len(strict['U'])-len(strict['H'])==2
        assert len(PS['bars'])==len(strict['U'])-1 and len(QS['bars'])==len(strict['S'])-1
    if len(strict['U'])==1 and not weak['U']:
        root=strict['U'][0];nxt={e['source']:e['target'] for e in esc}
        for i in range(len(P)):
            seen=set()
            while i!=root:
                assert i not in seen;seen.add(i);i=nxt[i]
    radius2=max(dot(x,x) for x in X);inradius2=min(F(h*h,dot(nn,nn)) for h,nn in zip(supports,normals))
    return enc(dict(identity=data['identity'],scale=scale,source_rows=source,extreme_source_indices=used,V=len(P),E=len(E),F=len(faces),C=2*len(E),facets=faces,raw_support_planes=eq,edges=E,actual_volume=V/scale**3,actual_centroid=tuple(v/scale for v in c),centred_integer_multiplier=L,centred_integer_offset=C,physical_coordinate_multiplier=L*scale,strict=strict,additional_weak=weak,primitive_zero_counts=zeros,physical_landscape=PS,polar_landscape=QS,positive_true_edge_forest=esc,inradius_circumradius_squared=inradius2/radius2,markers=['EXHAUSTIVE_MAXIMAL_HULL_PASS','EXACT_TWO_ORIGIN_MASS_PASS','STRICT_WEAK_FULL_S_U_H_PASS','SIMULTANEOUS_LEVEL_P_Q_PASS','POSITIVE_PHYSICAL_TRUE_EDGE_FOREST_PASS']))

def controls():
    cases=[('cube',list(product((-1,1),repeat=3)),[6,8,12],[0,0,0]),('tetra',[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],[4,4,6],[0,0,0]),('weak_prism',[(x,y,z) for x,y in [(0,0),(1,0),(-1,1)] for z in (-1,1)],[4,4,6],[1,2,3])]
    for name,rows,sc,wc in cases:
        d=audit(dict(identity=name,scale=1,rows=rows));assert [len(d['strict'][k]) for k in ('S','U','H')]==sc;assert [len(d['additional_weak'][k]) for k in ('S','U','H')]==wc
    print('LEAD_C2_CUBE_TETRA_WEAK_PRISM_CONTROLS_PASS')
def main():
    if sys.argv[1:] == ['--controls']:controls();return
    p=Path(sys.argv[1]);out=Path(sys.argv[2]) if len(sys.argv)>2 else p.with_suffix('.audit.json');d=audit(json.loads(p.read_text()));raw=(json.dumps(d,sort_keys=True,indent=2)+'\n').encode();out.write_bytes(raw)
    print(d['identity'],[d[k] for k in ['V','E','F','C']],{k:len(v) for k,v in d['strict'].items()},{k:len(v) for k,v in d['additional_weak'].items()},'P',len(d['physical_landscape']['bars']),'Q',len(d['polar_landscape']['bars']),flush=True)
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest(),flush=True);print('LEAD_C2_EXACT_BODY_AUDIT_PASS',flush=True)
if __name__=='__main__':main()
