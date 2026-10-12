"""MP9 deterministic combinatorics and certified projection screens.
CPython 3.13.5; standard library; assertions enabled.
The canonical identities are rooted-dart/both-orientation rotation codes.
"""
from collections import Counter,deque
from itertools import combinations,permutations,product
from fractions import Fraction as F
from math import factorial
import hashlib,json
assert __debug__
N=9
CAP=(0,0,1000,2000,2800,3375,3920,4320,4640)
def encoded(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def cycle(f):
    return min(f[i:]+f[:i] for i in range(len(f)))

def normalize(fs):
    return tuple(sorted(cycle(tuple(f)) for f in fs))

def incidence(fs):
    e={}
    rot=[{} for _ in range(N)]
    for k,f in enumerate(fs):
        assert len(f)>=3 and len(f)==len(set(f))
        for j,a in enumerate(f):
            b=f[(j+1)%len(f)]; c=f[j-1]
            assert (a,b) not in e
            e[a,b]=k
            assert c not in rot[a]
            rot[a][c]=b
    assert all((b,a) in e for a,b in e)
    for r in rot:
        assert len(r)>=3 and set(r)==set(r.values())
        v=next(iter(r)); s=v; seen=set()
        while v not in seen: seen.add(v);v=r[v]
        assert v==s and len(seen)==len(r)
    assert N-len(e)//2+len(fs)==2
    return e,rot

def canonical(fs):
    """Try every directed root edge and both sphere orientations.
    An oriented map is determined by its rotation system; rooted BFS is canonical.
    """
    e,rot=incidence(fs)
    best=None; bestfs=None
    for sign in (1,-1):
        rr=rot if sign==1 else [{b:a for a,b in r.items()} for r in rot]
        for a,b in e:
            labels={a:0}; queue=[a]; anchor={a:b}; rows=[]
            for x in queue:
                v=anchor[x]; row=[]
                for _ in range(len(rr[x])):
                    if v not in labels:
                        labels[v]=len(labels);queue.append(v);anchor[v]=x
                    row.append(labels[v]);v=rr[x][v]
                rows.append(tuple(row))
            assert len(labels)==N
            key=tuple(rows)
            if best is None or key<best:
                best=key
                ffs=(fs if sign==1 else tuple(tuple(reversed(f)) for f in fs))
                bestfs=normalize(tuple(labels[x] for x in f) for f in ffs)
    return best,bestfs

def three_connected(es):
    nei=[0]*N
    for a,b in es: nei[a]|=1<<b
    if any(x.bit_count()<3 for x in nei):return False
    full=(1<<N)-1
    for a,b in combinations(range(N),2):
        allowed=full^(1<<a)^(1<<b); todo=allowed&-allowed; seen=0
        while todo:
            v=todo&-todo; todo^=v; seen|=v
            todo|=nei[v.bit_length()-1]&allowed&~seen
        if seen!=allowed:return False
    return True

def triangles():
    fs=[(0,1,2),(0,3,1),(1,3,2),(2,3,0)]
    for k in range(4,N):
        a,b,c=fs.pop(0)
        fs.extend(((a,b,k),(b,c,k),(c,a,k)))
    key,fs=canonical(normalize(fs)); known={key:fs};queue=deque([fs])
    while queue:
        fs=queue.popleft();es,_=incidence(fs)
        for a,b in sorted(es):
            if a>b:continue
            f=fs[es[a,b]];g=fs[es[b,a]]
            c=next(x for x in f if x not in (a,b))
            d=next(x for x in g if x not in (a,b))
            if (c,d) in es:continue
            child=normalize([t for j,t in enumerate(fs) if j not in (es[a,b],es[b,a])]+[(c,d,b),(d,c,a)])
            kk,ff=canonical(child)
            if kk not in known:known[kk]=ff;queue.append(ff)
    return known

def auto_maps(fs):
    es,rot=incidence(fs); a,b=min(es); out=[]
    for sign in (1,-1):
        rr=rot if sign==1 else [{v:u for u,v in r.items()} for r in rot]
        for u,v in es:
            mp={a:u,b:v};todo=[(a,b)];done=set();ok=True
            while todo and ok:
                x,y=todo.pop()
                if x in done:continue
                done.add(x);xx=mp[x];yy=mp[y]
                if len(rot[x])!=len(rr[xx]):ok=False;break
                for _ in rot[x]:
                    if y in mp:
                        if mp[y]!=yy:ok=False;break
                    else:
                        if yy in mp.values():ok=False;break
                        mp[y]=yy
                    todo.append((y,x));y=rot[x][y];yy=rr[xx][yy]
            if ok and len(mp)==N:out.append(tuple(mp[i] for i in range(N)))
    out=sorted(set(out));assert tuple(range(N)) in out
    return out

def elementary():
    global N
    N=4;k,f=canonical(((0,1,2),(0,3,1),(1,3,2),(2,3,0)))
    old={k:f};counts={4:1}
    for n in range(5,10):
        N=n;new={};v=n-1
        for fs in old.values():
            for j,(a,b,c) in enumerate(fs):
                child=fs[:j]+fs[j+1:]+((a,b,v),(b,c,v),(c,a,v))
                k,f=canonical(normalize(child));new[k]=f
            es={(a,t[(i+1)%3]):j for j,t in enumerate(fs)for i,a in enumerate(t)}
            for a,b in sorted(es):
                if a>b:continue
                j,l=es[a,b],es[b,a]
                c=next(x for x in fs[j]if x not in(a,b))
                d=next(x for x in fs[l]if x not in(a,b))
                child=tuple(f for i,f in enumerate(fs)if i not in(j,l))
                child+=((b,c,v),(c,a,v),(a,d,v),(d,b,v))
                k,f=canonical(normalize(child));new[k]=f
        old=new;counts[n]=len(old)
    assert counts=={4:1,5:1,6:2,7:5,8:14,9:50}
    return old

def det(a):
    a=[r[:]for r in a];d=1
    for k in range(len(a)):
        q=a[k][k];assert q>0
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                u=q*a[i][j]-a[i][k]*a[k][j];assert u%d==0;a[i][j]=u//d
        d=q
    return d

def aut_independent(es):
    es=set(map(tuple,es));deg=[sum(i in e for e in es)for i in range(9)]
    bs=[[i for i in range(9)if deg[i]==d]for d in sorted(set(deg))];out=[]
    for choices in product(*(permutations(b)for b in bs)):
        a=list(range(9))
        for b,c in zip(bs,choices):
            for i,j in zip(b,c):a[i]=j
        if {tuple(sorted((a[i],a[j])))for i,j in es}==es:out.append(a)
    return sorted(out)

def catalogue(check=False):
    global N
    N=9;old=triangles()
    if check:assert set(old)==set(elementary())
    out=[]
    for gi,k in enumerate(sorted(old)):
        fs=old[k];ee,_=incidence(fs);es=sorted((a,b)for a,b in ee if a<b)
        au=[list(a)for a in auto_maps(fs)]
        if check:
            assert au==aut_independent(es) and three_connected(set(ee))
        roots=sorted({min(a[i]for a in au)for i in range(9)})
        L=[[sum(i in e for e in es)if i==j else -int(tuple(sorted((i,j)))in es)for j in range(8)]for i in range(8)]
        out.append(dict(id=gi,facets=fs,edges=es,aut=au,roots=roots,trees=det(L)))
    raw=encoded(out)
    assert pin(raw)==[18578,'eb4e51ef3f2593e43ec72fd80cb7ff267fcc0d17a803925c49cfa28b018e7323']
    return json.loads(raw)

def images(p,aa):
    z=[]
    for a in aa:
        q=[0]*9
        for i in range(9):q[a[i]]=a[p[i]]
        z.append(tuple(q))
    return min(z)

def edge_trees(g,r):
    aa=[a for a in g['aut']if a[r]==r];out=set();count=0
    for ee in combinations(g['edges'],8):
        adj=[[]for _ in range(9)]
        for a,b in ee:adj[a].append(b);adj[b].append(a)
        p=[-1]*9;p[r]=r;todo=[r]
        for a in todo:
            for b in adj[a]:
                if p[b]<0:p[b]=a;todo.append(b)
        if len(todo)==9:count+=1;out.add(images(p,aa))
    assert count==g['trees']
    return sorted(out)

def parent_trees(g,r):
    aa=[a for a in g['aut']if a[r]==r];adj=[[]for _ in range(9)]
    for a,b in g['edges']:adj[a].append(b);adj[b].append(a)
    p=[-1]*9;p[r]=r;vs=[i for i in range(9)if i!=r];out=set();count=0
    def dfs(at):
        nonlocal count
        if at==8:count+=1;out.add(images(p,aa));return
        i=vs[at]
        for j in adj[i]:
            p[i]=j;v=i;seen=set()
            while v!=-1 and v!=r and v not in seen:seen.add(v);v=p[v]
            if v not in seen:dfs(at+1)
        p[i]=-1
    dfs(0);assert count==g['trees']
    return sorted(out)

def code(p,r=0):
    ch=[[]for _ in p]
    for i,j in enumerate(p):
        if i!=j:ch[j].append(i)
    def f(i):return '('+''.join(sorted(f(j)for j in ch[i]))+')'
    return f(r)

def decode(s):
    p=[];stack=[]
    for x in s:
        if x=='(':v=len(p);p.append(stack[-1]if stack else 0);stack.append(v)
        else:stack.pop()
    assert not stack
    return tuple(p)

def shapes():
    ss=sorted({code((0,)+p)for p in product(*(range(i)for i in range(1,9)))})
    assert len(ss)==286
    return [decode(s)for s in ss]

def depths(p,r):
    out=[]
    for i in range(9):
        d=0
        while i!=r:d+=1;assert d<9;i=p[i]
        out.append(d)
    return out

def safe(p,r,faces):
    d=depths(p,r)
    return all(sum(CAP[d[i]]for i in f)<8000 for f in faces if r not in f)

def generic_safe(p):
    d=depths(p,0)
    return max(sum(CAP[d[i]]for i in f)for f in combinations(range(1,9),3))<8000

def verify_caps():
    assert 16*(F(1,5)-F(1,375))-4*F(1,239)>F(157,50)
    assert F(CAP[2],8000)==F(1,8)
    assert F(CAP[3],8000)==F(1,4)
    assert F(CAP[5],8000)==F(27,64)
    for d in(4,6,7,8):
        x=F(157,50*(d+1));u=1-x*x/2+x**4/24
        assert 0<x<1 and u**(d+1)<F(CAP[d],8000)

def norm_orders(p):
    def rec(order,left):
        if not left:yield order;return
        for i in sorted(left):
            if not any(j!=i and p[j]==i for j in left):
                yield from rec(order+[i],left-{i})
    return list(rec([],set(range(9))))

def comparisons(p,order):
    def ancestor(a,b):
        while p[a]!=a:
            a=p[a]
            if a==b:return True
        return False
    return [[a,b]for a,b in zip(order,order[1:])if not ancestor(a,b)]
