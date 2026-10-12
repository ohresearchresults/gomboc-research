# material-adfad4ef7fcb

AI research material

---

"""Complete 33-variable actual C34 chart and rational control; standard library only."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys

ALPHA=1082881
NODES=[]
class E:
    def __init__(self,op,args,value,degree,mass):
        self.op,self.args,self.value,self.degree,self.mass=op,args,value,degree,mass
        self.id=len(NODES);NODES.append(self)
    def __add__(self,o):
        o=expr(o)
        if self.mass==0:return o
        if o.mass==0:return self
        if self.op==o.op=='c':return expr(self.value+o.value)
        return E('+',(self,o),None,max(self.degree,o.degree),self.mass+o.mass)
    __radd__=__add__
    def __neg__(self):return self*(-1)
    def __sub__(self,o):return self+-expr(o)
    def __rsub__(self,o):return expr(o)+-self
    def __mul__(self,o):
        o=expr(o)
        if not self.mass or not o.mass:return expr(0)
        if self.op==o.op=='c':return expr(self.value*o.value)
        return E('*',(self,o),None,self.degree+o.degree,self.mass*o.mass)
    __rmul__=__mul__
def expr(x):
    if isinstance(x,E):return x
    assert isinstance(x,int)
    return E('c',(),x,0,abs(x))
def var(i):return E('v',(),i,1,1)
def values(point):
    out=[]
    for p in NODES:
        if p.op=='c':z=F(p.value)
        elif p.op=='v':z=point[p.value]
        elif p.op=='+':z=out[p.args[0].id]+out[p.args[1].id]
        else:z=out[p.args[0].id]*out[p.args[1].id]
        out.append(z)
    return out
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def matvec(A,x):return tuple(dot(row,x) for row in A)
def adj(A):
    return [[A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]-A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3] for j in range(3)] for i in range(3)]
def principal(A,ids):
    if len(ids)==1:return A[ids[0]][ids[0]]
    if len(ids)==2:
        i,j=ids;return A[i][i]*A[j][j]-A[i][j]*A[j][i]
    return det(*A)
def psd(A):return all(principal(A,ids)>=0 for n in (1,2,3) for ids in combinations(range(3),n))

def hull(X):
    planes={}
    for ids in combinations(range(len(X)),3):
        a,b,c=(X[i] for i in ids);n=cross(sub(b,a),sub(c,a))
        if not any(n):continue
        h=dot(n,a);sl=[h-dot(n,x) for x in X]
        if min(sl)<0 and max(sl)>0:continue
        if max(sl)<=0:n=scale(n,-1);h=-h;sl=[-s for s in sl]
        fac=tuple(i for i,s in enumerate(sl) if not s)
        t=abs(next(v for v in n if v));key=tuple(v/t for v in n)+(h/t,)
        planes[key]=fac
    entries=sorted(planes.items());faces=[v for k,v in entries]
    edges=[p for p in combinations(range(len(X)),2) if sum(set(p)<=set(f) for f in faces)==2]
    cycles=[]
    for (key,f) in entries:
        a=min(f);near=sorted(j for j in f if tuple(sorted((a,j))) in edges)
        path=[a,near[0]]
        while True:
            nxt=[j for j in f if tuple(sorted((path[-1],j))) in edges and j!=path[-2]]
            assert len(nxt)==1
            if nxt[0]==a:break
            path.append(nxt[0])
        assert len(path)==len(f)
        if dot(cross(sub(X[path[1]],X[a]),sub(X[path[2]],X[a])),key[:3])<0:path=[a]+path[:0:-1]
        cycles.append(tuple(path))
    return cycles,edges

def chart(cycles,pv,pq):
    assert len(cycles)==9 and sum(map(len,cycles))==34
    assert all(len(c)>=3 and len(set(c))==len(c) for c in cycles)
    assert set(i for c in cycles for i in c)==set(range(10))
    arcs={}
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):arcs[a,b]=arcs.get((a,b),0)+1
    assert len(arcs)==34 and all(v==1 and arcs.get((b,a))==1 for (a,b),v in arcs.items())
    def connected(edges,verts):
        seen={min(verts)}
        while True:
            old=len(seen)
            for a,b in edges:
                if a in seen or b in seen:seen.update((a,b))
            if old==len(seen):return seen==verts
    assert connected(arcs,set(range(10)))
    for v in range(10):
        links=[]
        for c in cycles:
            if v in c:
                i=c.index(v);links.append((c[i-1],c[(i+1)%len(c)]))
        verts=set(x for e in links for x in e)
        assert len(verts)>=3 and connected(links,verts)
        assert all(sum(x in e for e in links)==2 for x in verts)
    for parents,n in ((pv,10),(pq,9)):
        assert len(parents)==n and set(parents)<=set(range(n))
        roots=[i for i,p in enumerate(parents) if i==p];assert len(roots)==1
        for start in range(n):
            seen=set();u=start
            while u!=roots[0]:
                assert u not in seen;seen.add(u);u=parents[u]
    names=['v%d_%d'%(i,h) for i in range(4,10) for h in range(3)]+['m00','m01','m02','m11','m12','m22']+['r%d'%a for a in range(9)]
    vv=[var(i) for i in range(33)]
    X=[tuple(map(expr,p)) for p in ((0,0,0),(1,0,0),(0,1,0),(0,0,1))]+[tuple(vv[3*(i-4):3*(i-3)]) for i in range(4,10)]
    m00,m01,m02,m11,m12,m22=vv[18:24]
    M=[[m00,m01,m02],[m01,m11,m12],[m02,m12,m22]];A=adj(M);r=vv[24:]
    normals=[cross(sub(X[c[1]],X[c[0]]),sub(X[c[2]],X[c[0]])) for c in cycles]
    tri=[];colors=[]
    for a,c in enumerate(cycles):
        for i in range(1,len(c)-1):tri.append((c[0],c[i],c[i+1]));colors.append(a)
    assert len(tri)==16
    dn=[cross(sub(X[j],X[i]),sub(X[k],X[i])) for i,j,k in tri]
    dt=[det(X[i],X[j],X[k]) for i,j,k in tri]
    ss=[tuple(X[i][h]+X[j][h]+X[k][h] for h in range(3)) for i,j,k in tri]
    T=sum(dt);U=tuple(sum(d*s[h] for d,s in zip(dt,ss)) for h in range(3))
    b=[4*T*dot(n,X[c[0]])-dot(n,U) for n,c in zip(normals,cycles)]
    cons=[]
    def put(kind,name,p):cons.append((kind,name,expr(p)))
    for ids in combinations(range(10),4):
        a,j,k,l=ids;v=det(sub(X[j],X[a]),sub(X[k],X[a]),sub(X[l],X[a]));put('ge','tetra_'+str(ids),1-v*v)
    for i in range(4,10):
        for h in range(3):put('ge','coordinate_%d_%d'%(i,h),1-X[i][h]*X[i][h])
    for a,c in enumerate(cycles):
        n=normals[a]
        for i in range(10):put('ge','support_%d_%d'%(a,i),dot(n,sub(X[c[0]],X[i])))
        for i in c[3:]:put('eq','plane_%d_%d'%(a,i),dot(n,sub(X[i],X[c[0]])))
        put('eq','inverse_%d'%a,b[a]*r[a]-1);put('ge','positive_inverse_%d'%a,r[a])
    for t,n,a in zip(tri,dn,colors):put('ge','orientation_'+str(t),dot(n,normals[a]))
    put('ge','volume_lower',T-1);put('ge','volume_upper',16-T)
    low=[[ALPHA*M[i][j]-(i==j) for j in range(3)] for i in range(3)]
    for size in (1,2,3):
        for ids in combinations(range(3),size):put('ge','metric_'+str(ids),principal(low,ids))
    put('eq','metric_trace',sum(M[i][i] for i in range(3))-1)
    for i,j in enumerate(pv):
        if i!=j:put('ge','vertex_arrow_%d'%i,dot(sub(scale(X[i],4*T),U),matvec(M,sub(X[j],X[i]))))
    for i,j in enumerate(pq):
        if i!=j:put('ge','pole_arrow_%d'%i,b[i]*dot(normals[i],matvec(A,normals[j]))-b[j]*dot(normals[i],matvec(A,normals[i])))
    assert len(cons)==386 and sum(k=='eq' for k,_,_ in cons)==17
    Dc=[4*T*d-dot(U,n) for d,n in zip(dt,dn)]
    K=[sum(d for d,a in zip(Dc,colors) if a==b) for b in range(9)]
    W=[tuple(sum(d*s[h] for d,s,a in zip(Dc,ss,colors) if a==b) for h in range(3)) for b in range(9)]
    LL=[[r[a]*dot(normals[a],sub(scale(X[cycles[a][0]],3*K[b]),W[b])) for b in range(9)] for a in range(9)]
    Q=[scale(n,4*T*ra) for n,ra in zip(normals,r)]
    denominators=b
    obj=[]
    def target(name,p):obj.append((name,expr(p)))
    for i,j in combinations(range(10),2):target('vertex_distance_%d_%d'%(i,j),dot(sub(X[i],X[j]),sub(X[i],X[j])))
    for a in range(9):
        target('support_denominator_%d'%a,b[a]);target('mass_numerator_%d'%a,3*K[a])
        for i in range(10):
            if i not in cycles[a]:target('nonincidence_%d_%d'%(a,i),4*T*r[a]*dot(normals[a],sub(X[cycles[a][0]],X[i])))
    for a,b in combinations(range(9),2):
        target('pole_distance_%d_%d'%(a,b),dot(sub(Q[a],Q[b]),sub(Q[a],Q[b])))
        target('pair_sum_%d_%d'%(a,b),2*T-LL[a][b]-LL[b][a])
        target('pair_old_%d_%d'%(a,b),(6*T-5*LL[a][b])*(6*T-5*LL[b][a])-T*T)
        if set(cycles[a])&set(cycles[b]):target('pair_incident_%d_%d'%(a,b),(9*T-8*LL[a][b])*(9*T-8*LL[b][a])-T*T)
    for t,n,a in zip(tri,dn,colors):target('triangle_orientation_'+str(t),dot(n,normals[a]))
    return names,cons,obj,(X,M,T,U,normals,denominators,r,K,LL,Q,tri,colors)

RAW=[(-3,-1,0),(-1,-2,0),(1,-2,0),(3,-1,0),(3,1,0),(1,2,0),(-1,2,0),(-3,1,0),(-1,0,2),(1,0,2)]
raw=[tuple(map(F,v)) for v in RAW]
volumes=[(abs(det(sub(raw[j],raw[i]),sub(raw[k],raw[i]),sub(raw[l],raw[i]))),(i,j,k,l)) for i,j,k,l in combinations(range(10),4)]
maximum=max(v for v,t in volumes);frame=list(min(t for v,t in volumes if v==maximum))
if det(*(sub(raw[i],raw[frame[0]]) for i in frame[1:]))<0:frame[1],frame[2]=frame[2],frame[1]
order=frame+[i for i in range(10) if i not in frame]
origin=raw[frame[0]];columns=[sub(raw[i],origin) for i in frame[1:]]
B=list(map(list,zip(*columns)));BI=[[v/maximum for v in row] for row in adj(B)]
X=[matvec(BI,sub(raw[i],origin)) for i in order]
assert X[:4]==[(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
cycles,edges=hull(X);assert (len(X),len(edges),len(cycles))==(10,17,9)
names,cons,obj,data=chart(cycles,[0]*10,[0]*9)
_,_,Tp,Up,np,bp,rp,Kp,Lp,Qp,tri,colors=data
delta=[det(*(X[i] for i in t)) for t in tri];T=sum(delta)
U=tuple(sum(d*sum(X[i][h] for i in t) for d,t in zip(delta,tri)) for h in range(3))
c=scale(U,1/(4*T));center_expected=matvec(BI,sub((F(0),F(0),F(7,12)),origin));assert c==center_expected
Y=[sub(v,c) for v in X]
cov=[[sum(det(*(Y[i] for i in t))*(sum(Y[i][h] for i in t)*sum(Y[i][k] for i in t)+sum(Y[i][h]*Y[i][k] for i in t)) for t in tri)/(20*T) for k in range(3)] for h in range(3)]
assert psd([[cov[i][j]-F(i==j,3840) for j in range(3)] for i in range(3)])
assert psd([[3*(i==j)-cov[i][j] for j in range(3)] for i in range(3)])
normals=[cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]])) for f in cycles]
bb=[4*T*dot(n,sub(X[f[0]],c)) for n,f in zip(normals,cycles)];rr=[1/t for t in bb]
M=[[dot(columns[i],columns[j]) for j in range(3)] for i in range(3)];tr=sum(M[i][i] for i in range(3));M=[[v/tr for v in row] for row in M]
point=[v for x in X[4:] for v in x]+[M[0][0],M[0][1],M[0][2],M[1][1],M[1][2],M[2][2]]+rr
ev=values(point)
def take(p):return ev[p.id]
assert take(Tp)==T and tuple(map(take,Up))==U and list(map(take,bp))==bb
geometric_count=0;mechanics=[]
for k,name,p in cons:
    z=take(p)
    if 'arrow_' in name:mechanics.append((name,str(z)));continue
    assert z==0 if k=='eq' else z>=0,(name,z)
    geometric_count+=1
Q=[tuple(map(take,q)) for q in Qp];L=[[take(p)/T for p in row] for row in Lp]
d=[3*take(p)/(4*T*T) for p in Kp]
assert sum(d)==3 and min(d)>0 and all(sum(row)==3 for row in L)
assert all(sum(L[a][b]*Q[b][h] for b in range(9))==-Q[a][h] for a in range(9) for h in range(3))
assert all(sum(L[a][k]*L[k][b] for k in range(9))+L[a][b]==4*d[b] for a in range(9) for b in range(9))
AM=adj(M)
for i in range(1,10):
    z=dict(mechanics)['vertex_arrow_%d'%i]
    assert F(z)==4*T*dot(Y[i],matvec(M,sub(Y[0],Y[i])))
for i in range(1,9):
    z=F(dict(mechanics)['pole_arrow_%d'%i])
    assert z==bb[i]**2*bb[0]/(4*T)**2*dot(Q[i],matvec(AM,sub(Q[0],Q[i])))
assert all(take(p)>0 for name,p in obj)
metadata=dict(variables=len(names),constraints=len(cons),equalities=sum(k=='eq' for k,_,_ in cons),degree=max(p.degree for _,_,p in cons),height_l1_bound=max(p.mass for _,_,p in cons),objectives=len(obj),objective_degree=max(p.degree for _,p in obj),objective_height_l1_bound=max(p.mass for _,p in obj),expression_nodes=len(NODES))
assert metadata['degree']<=12 and metadata['objective_degree']<=20
assert max(metadata['height_l1_bound'],metadata['objective_height_l1_bound'])<2**80
# Uniform term counts, before cancellations, for every 16-triangle chart.
assert 6*(ALPHA+1)**3<2**80
normal_component=8;t_mass=96;u_mass=288
dt_mass=4*t_mass*6+3*u_mass*normal_component
k_mass=16*dt_mass;w_mass=16*dt_mass*3
lambda_mass=3*normal_component*(3*k_mass+w_mass)
assert (9*t_mass+8*lambda_mass)**2+t_mass**2<2**80
assert 20**33<2**143 and 33<2**6 and 4+80+143<2**8
assert 227*(33*2**33*20**33)<2**190
assert 2**190+32<2**192 and 4*16**2==1024
assert F(5,3)*F(1,3840)==F(1,48**2)
assert 47*3*3840==541440 and 2*541440+1==ALPHA
def convert(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [convert(v) for v in x]
    if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
    return x
report=dict(identity='C34_MAXSIMPLEX_CHART_V3',epsilon='2^(-2^192)',raw_vertices=RAW,frame_order=order,max_six_volume=maximum,vertices=X,cycles=cycles,edges=edges,triangles=tri,colors=colors,center=c,covariance=cov,six_volume=T,cone_d=d,lambda_matrix=L,metadata=metadata,geometric_constraints_passed=geometric_count,formal_star_arrows=mechanics,status='Actual (10,17,9) control; formal stars fail and this is NOT a K34 witness',JPT=dict(n=33,m=1000,d=20,H=2**80))
out=(json.dumps(convert(report),sort_keys=True,separators=(',',':'))+'\n').encode();Path('c34_maxsimplex_chart_v3.json').write_bytes(out)
print('METADATA',metadata)
print('REPORT',len(out),hashlib.sha256(out).hexdigest())
src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
print('C34_MAXSIMPLEX_33_VARIABLES_386_CONSTRAINTS_EXACT_CONTROL_PASS')
