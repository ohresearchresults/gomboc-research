# material-c9ef4681d976

AI research material

---

"""Exact rational hull, own-centroid mechanics, and complete elder forests.
Input is {grid: positive integer, points: complete integer coordinate rows}.
Only Python's standard library is required. No floating hull nomination is used.
"""
import json,math,itertools,sys,hashlib
from fractions import Fraction as F
from collections import defaultdict,deque
from pathlib import Path

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def norm2(a):return dot(a,a)
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def write_json(path,obj):
    data=(json.dumps(encode(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(path).write_bytes(data)
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def polygon(ids,p,n):
    drop=max(range(3),key=lambda k:abs(n[k]));ab=[k for k in range(3) if k!=drop]
    ix=sorted(ids,key=lambda i:(p[i][ab[0]],p[i][ab[1]]))
    def turn(i,j,k):
        a,b,c=(tuple(p[h][z] for z in ab) for h in (i,j,k))
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def half(seq):
        out=[]
        for i in seq:
            while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
            out.append(i)
        return out
    cyc=half(ix)[:-1]+half(ix[::-1])[:-1]
    if dot(cross(sub(p[cyc[1]],p[cyc[0]]),sub(p[cyc[2]],p[cyc[0]])),n)<0:cyc.reverse()
    j=cyc.index(min(cyc));return cyc[j:]+cyc[:j]

def geometry(data):
    p=[tuple(map(int,z)) for z in data['points']];g=int(data['grid'])
    assert g>0 and len(set(p))==len(p)
    planes={}
    for i,j,k in itertools.combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]));h=dot(n,p[i])
        if n==(0,0,0):continue
        s=[dot(n,z)-h for z in p]
        if max(s)>0 and min(s)<0:continue
        if max(s)==min(s)==0:continue
        if max(s)>0:n=mul(-1,n);h=-h;s=[-v for v in s]
        d=math.gcd(*n,h);key=tuple(v//d for v in n)+(h//d,)
        planes[key]=[i for i,v in enumerate(s) if v==0]
    normals=sorted(planes);assert len(normals)>=4
    faces=[polygon(planes[n],p,n[:3]) for n in normals]
    used=sorted(set(i for f in faces for i in f))
    # This auditor accepts only exposed input nominations, not silently omitted points.
    assert used==list(range(len(p)))
    edgefaces=defaultdict(list);directed={}
    for f,cy in enumerate(faces):
        n=normals[f][:3];h=normals[f][3]
        assert all(dot(n,z)<=h for z in p)
        for i,j in zip(cy,cy[1:]+cy[:1]):
            assert (i,j) not in directed;directed[i,j]=f
            edgefaces[tuple(sorted((i,j)))].append(f)
    assert all((j,i) in directed for i,j in directed)
    assert all(len(fs)==2 for fs in edgefaces.values())
    edges=sorted(edgefaces);assert len(p)-len(edges)+len(faces)==2
    adj={i:set() for i in used}
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen={0};todo=[0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in seen:seen.add(j);todo.append(j)
    assert seen==set(used)
    for v in used:
        link=defaultdict(set)
        for cy in faces:
            if v in cy:
                j=cy.index(v);a,b=cy[j-1],cy[(j+1)%len(cy)];link[a].add(b);link[b].add(a)
        assert set(link)==adj[v] and all(len(z)==2 for z in link.values())
        seen={next(iter(link))};todo=list(seen)
        while todo:
            for j in link[todo.pop()]:
                if j not in seen:seen.add(j);todo.append(j)
        assert seen==set(link)
    tri=[(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)]
    ds=[det(p[i],p[j],p[k]) for i,j,k in tri];D=sum(ds);assert D>0
    V=F(D,6*g**3);M=[F(sum(d*(p[i][a]+p[j][a]+p[k][a]) for d,(i,j,k) in zip(ds,tri)),24*g**4) for a in range(3)]
    c=tuple(m/V for m in M);x=[sub(tuple(F(t,g) for t in z),c) for z in p]
    assert all(det(x[i],x[j],x[k])>0 for i,j,k in tri)
    assert sum((F(det(x[i],x[j],x[k]),6) for i,j,k in tri),F(0))==V
    assert all(sum((F(det(x[i],x[j],x[k]),24)*(x[i][a]+x[j][a]+x[k][a]) for i,j,k in tri),F(0))==0 for a in range(3))
    # Independent boundary-divergence formulas, three volumes and nine moments.
    volumes=[];moments=[]
    for axis in range(3):
        vv=F(0);mm=[F(0)]*3
        for i,j,k in tri:
            a,b,cc=p[i],p[j],p[k];nn=cross(sub(b,a),sub(cc,a));ss=add(add(a,b),cc)
            vv+=F(nn[axis]*ss[axis],6*g**3)
            for z in range(3):mm[z]+=F(nn[axis]*(ss[z]*ss[axis]+a[z]*a[axis]+b[z]*b[axis]+cc[z]*cc[axis]),24*g**4*(1+(z==axis)))
        assert vv==V and mm==M;volumes.append(vv);moments.append(mm)
    return p,g,normals,faces,edges,edgefaces,x,V,c,volumes,moments

def mechanics(x,normals,faces,edges,edgefaces,g,c):
    ns=[n[:3] for n in normals];hs=[F(n[3],g)-dot(n[:3],c) for n in normals];assert min(hs)>0
    strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0];allpred=[[],[],[]]
    def record(kind,identity,primitives):
        allpred[kind].append([identity,primitives]);zeros[kind]+=sum(t==0 for t in primitives)
        if min(primitives)>0:strict[kind].append(identity)
        elif min(primitives)>=0:weak[kind].append(identity)
    for f,cy in enumerate(faces):
        n=ns[f];foot=mul(hs[f]/norm2(n),n)
        record(0,f,[dot(cross(sub(x[j],x[i]),sub(foot,x[i])),n) for i,j in zip(cy,cy[1:]+cy[:1])])
    adj=defaultdict(list)
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    for i in range(len(x)):
        vals=[-dot(x[i],sub(x[j],x[i])) for j in sorted(adj[i])]
        allv=[-dot(x[i],sub(x[j],x[i])) for j in range(len(x)) if j!=i]
        assert (min(vals)>0)==(min(allv)>0) and (min(vals)>=0)==(min(allv)>=0)
        record(1,i,vals)
    for i,j in edges:
        e=sub(x[j],x[i]);a=-dot(x[i],e);b=dot(x[j],e);z=add(x[i],mul(a/norm2(e),e))
        f,k=edgefaces[i,j];n,m=ns[f],ns[k];nn,mm,nm=norm2(n),norm2(m),dot(n,m)
        assert nn*mm-nm*nm>0
        aa=dot(z,n)*mm-dot(z,m)*nm;bb=dot(z,m)*nn-dot(z,n)*nm
        record(2,[i,j],[a,b,aa,bb])
    if all(not z for z in weak):assert len(strict[0])+len(strict[1])-len(strict[2])==2
    q=[mul(1/h,n) for n,h in zip(ns,hs)]
    return dict(strict=strict,weak=weak,primitive_zero_counts=zeros,predicates=allpred),q

def landscape(p,edges):
    r=[norm2(z) for z in p];n=len(p);levels=[]
    for i,j in edges:
        e=sub(p[j],p[i]);t=max(F(0),min(F(1),-dot(p[i],e)/norm2(e)))
        levels.append(norm2(add(p[i],mul(t,e))))
    par=list(range(n));birth=list(range(n));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    adj=defaultdict(list)
    for ei,(i,j) in enumerate(edges):adj[i].append((j,ei));adj[j].append((i,ei))
    for ei in sorted(range(len(edges)),key=lambda k:(-levels[k],k)):
        i,j=edges[ei];u,z=root(i),root(j)
        if u==z:continue
        if (r[birth[u]],-birth[u])<(r[birth[z]],-birth[z]):u,z=z,u
        a,b=birth[z],birth[u];lev=levels[ei];delta=r[a]-lev
        assert delta>=0
        if delta>0:
            comp={a};todo=[a]
            while todo:
                for k,ee in adj[todo.pop()]:
                    if levels[ee]>lev and k not in comp:comp.add(k);todo.append(k)
            assert b not in comp
            cut=[[i,j] if i in comp else [j,i] for i,j in edges if (i in comp)!=(j in comp)]
            assert all(levels[k]<=lev for k,(i,j) in enumerate(edges) if (i in comp)!=(j in comp))
            prev={a:None};todo=deque([a])
            while todo and b not in prev:
                for k,ee in adj[todo.popleft()]:
                    if levels[ee]>=lev and k not in prev:prev[k]=None;prev[k]=(next_i:=edges[ee][0] if edges[ee][1]==k else edges[ee][1]);todo.append(k)
            assert b in prev
            path=[b]
            while path[-1]!=a:path.append(prev[path[-1]])
            path.reverse();lookup={tuple(sorted(e)):levels[k] for k,e in enumerate(edges)}
            assert min(lookup[tuple(sorted((i,j)))] for i,j in zip(path,path[1:]))==lev
            out.append(dict(peak=a,older=b,death_edge=list(edges[ei]),birth=r[a],death=lev,delta=delta,component=sorted(comp),boundary=cut,path=path))
        par[z]=u
    roots=[];arrows=[];cos2=[]
    for i in range(n):
        cand=[j for j,ei in adj[i] if dot(p[i],sub(p[j],p[i]))>0]
        if not cand:roots.append(i);continue
        def merit(j):return dot(p[i],sub(p[j],p[i]))**2/(r[i]*norm2(sub(p[j],p[i])))
        j=max(cand,key=merit);arrows.append([i,j]);cos2.append(merit(j));assert r[j]>r[i]
    return dict(bars=out,radius2=max(r),delta_sum=sum((z['delta'] for z in out),F(0)),roots=roots,arrows=arrows,min_arrow_cos2=min(cos2) if cos2 else None,points=p,edges=edges,edge_levels=levels)

def floor_root(n,k):
    lo=0;hi=1<<((n.bit_length()+k-1)//k)
    while hi-lo>1:
        m=(lo+hi)//2
        if m**k<=n:lo=m
        else:hi=m
    return hi if hi**k<=n else lo

def interval_power(a,k,scale=10**12):
    a=F(a);b=a*scale**k;z=floor_root(b.numerator//b.denominator,k)
    assert F(z**k)<=b<F((z+1)**k)
    return [z,z+1,scale]

def audit(data):
    p,g,ns,faces,edges,ef,x,V,c,bV,bM=geometry(data)
    mech,q=mechanics(x,ns,faces,edges,ef,g,c)
    P=landscape(x,edges);Q=landscape(q,sorted(tuple(sorted(ef[e])) for e in edges))
    assert set(P['roots'])==set(mech['strict'][1])|set(mech['weak'][1])
    assert len(Q['roots'])==len(mech['strict'][0])+len(mech['weak'][0])
    den=math.lcm(*(z.denominator for row in x for z in row))
    out=dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=V,centroid=c,centered_denominator_bits=den.bit_length(),faces=faces,normals=ns,mechanics=mech,physical=P,polar=Q,boundary_volumes=bV,boundary_moments=bM,
             TP=interval_power(P['delta_sum']**3/V**2,3),TQ=interval_power(Q['delta_sum']**3*V**2,3),
             min_edge_over_R=interval_power(min(norm2(sub(x[j],x[i])) for i,j in edges)/P['radius2'],2),
             inradius_over_R=interval_power(1/(Q['radius2']*P['radius2']),2),volume_over_R3=interval_power(V**2/P['radius2']**3,2))
    if P['min_arrow_cos2'] is not None:out['min_physical_arrow_cos']=interval_power(P['min_arrow_cos2'],2)
    return out

def controls():
    tetra={'grid':1,'points':[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]}
    prism={'grid':1,'points':[[x,y,z] for x,y in [(0,0),(1,0),(-1,3)] for z in [-1,1]]}
    a=audit(tetra);b=audit(prism)
    assert list(map(len,a['mechanics']['strict']))==[4,4,6] and list(map(len,a['mechanics']['weak']))==[0,0,0]
    assert list(map(len,b['mechanics']['strict']))==[4,4,6] and list(map(len,b['mechanics']['weak']))==[1,2,3]
    print('TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS',flush=True)
if __name__=='__main__':
    controls()
    for fn in sys.argv[1:]:
        out=audit(json.loads(Path(fn).read_text()));name=Path(fn).stem+'_EXACT.json';r=write_json(name,out)
        print(name,out['V'],out['E'],out['F'],list(map(len,out['mechanics']['strict'])),list(map(len,out['mechanics']['weak'])),out['TQ'],r,flush=True)
