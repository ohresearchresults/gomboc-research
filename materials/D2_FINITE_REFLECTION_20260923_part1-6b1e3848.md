# material-6b1e3848c40b

AI research material

---

# D2_FINITE_REFLECTION_20260923 — Recovery capsule part 1/3

Four new rational reflection-exact finite DLV-inspired nonwinners and one rooted-chord descent negative control. These are NOT the eleven lost D2 objects mentioned in older coordinator prose. Part 2 contains all literal rational inputs and output hashes. Part 3 contains the numerical methods and literal numerical checkpoint. No 110 construction is claimed.

Write the code block as d2_exact.py with LF and one terminal newline. Expected source: 7931 bytes, SHA256 141ad514d226afe665910f93da6569e463b54621494d556f79aa2c9df42e221c. Python 3.13.5 standard library only. Reconstruction/verification after part 2: `python -B -S d2_exact.py NAME.json`. The program writes NAME_audit.json and prints D2_EXACT_H_AUDIT_PASS, V/E/F, strict/weak counts, output byte count and SHA256. Part 2 gives expected values.

The H inequalities are N.x<=denominator. Every representative produces four sign reflections of its first two coordinates. The final positive cap representative and negative axial bottom guarantee boundedness; positive RHS makes the origin strictly feasible. Exhaustive triple intersections, all support tests, exact maximal facets, true two-owner edges, exact polygon orientation, Euler/connectivity, two-origin filled-volume mass, polar/direct-feet S crosscheck and every true vertex/edge strict/weak test are included. Boundary face feet are not double-counted: their lower-dimensional carriers are tested directly.

```python
"""Source-complete exact audit of D2 H polyhedra with common positive RHS.
Standard library only. Input: JSON {name, denominator, representatives:[[a,b,c],...],bottom}.
Every representative expands to the four (signed a,signed b,c) normals; bottom=(0,0,-bottom).
All inequalities have RHS denominator. Exhaustive integer triple intersections; exact mass
and complete strict/weak vertex, edge and facet equilibrium tests. No numerical hull is used.
"""
from itertools import combinations
from math import gcd,lcm,atan2
from functools import reduce,cmp_to_key
from fractions import Fraction as F
import json,sys,hashlib

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def det(a,b,c):return dot(a,cross(b,c))
def sign(x):return (x>0)-(x<0)
def textfrac(a,b=1):return str(F(a,b))

def audit(data):
    rhs=int(data['denominator']);assert rhs>0
    reps=[tuple(map(int,r)) for r in data['representatives']]
    bottom=int(data['bottom']);assert bottom>0
    assert reps[-1][0]>0 and reps[-1][1]>0 and reps[-1][2]>0
    # The bottom and final four cap inequalities alone bound x,y,z; 0 is strictly feasible.
    norms=[]
    for a,b,c in reps:
        for sx,sy in [(1,1),(-1,1),(-1,-1),(1,-1)]:
            n=(sx*a,sy*b,c)
            if n not in norms:norms.append(n)
    if (0,0,-bottom) not in norms:norms.append((0,0,-bottom))
    assert all(any(x for x in n) for n in norms)
    vertices=set()
    for i,j,k in combinations(range(len(norms)),3):
        a,b,c=norms[i],norms[j],norms[k]
        bc=cross(b,c);den=dot(a,bc)
        if not den:continue
        s=mul(rhs,add(add(bc,cross(c,a)),cross(a,b)))
        if den<0:den=-den;s=mul(-1,s)
        if any(dot(n,s)>rhs*den for n in norms):continue
        g=reduce(gcd,(*map(abs,s),den));vertices.add((*[x//g for x in s],den//g))
    # Exact lexicographic point order (not floating or homogeneous tuple order).
    def cmp(p,q):
        for i in range(3):
            z=p[i]*q[3]-q[i]*p[3]
            if z:return sign(z)
        return 0
    verts=sorted(vertices,key=cmp_to_key(cmp));assert len(verts)>=4
    L=lcm(*(v[3] for v in verts));P=[tuple(x*(L//v[3]) for x in v[:3]) for v in verts]
    incidence=[set(i for i,n in enumerate(norms) if dot(n,p)==rhs*L) for p in P]
    facemap={}
    for i in range(len(norms)):
        ids=tuple(v for v,g in enumerate(incidence) if i in g)
        if len(ids)<3:continue
        if ids in facemap:continue
        # Every supporting plane with >=3 hull vertices is a maximal facet unless collinear.
        if not any(any(cross(sub(P[b],P[ids[0]]),sub(P[c],P[ids[0]]))) for b,c in combinations(ids[1:],2)):continue
        facemap[ids]=i
    fs=[];N=[];input_rows=[]
    for ids,i in sorted(facemap.items(),key=lambda kv:kv[1]):
        n=norms[i]
        # Use a rational 2D projection and exact orientation comparator around the vertex mean.
        drop=max(range(3),key=lambda j:abs(n[j]));axes=[j for j in range(3) if j!=drop]
        ctr=tuple(sum(P[v][j] for v in ids) for j in axes);m=len(ids)
        xy={v:(m*P[v][axes[0]]-ctr[0],m*P[v][axes[1]]-ctr[1]) for v in ids}
        def half(v):x,y=xy[v];return 0 if y>0 or (y==0 and x>=0) else 1
        def cmpangle(v,w):
            hv,hw=half(v),half(w)
            if hv!=hw:return hv-hw
            a,b=xy[v],xy[w];d=a[0]*b[1]-a[1]*b[0]
            if d:return -sign(d)
            return sign(dot(a,a)-dot(b,b))
        order=sorted(ids,key=cmp_to_key(cmpangle))
        orient=dot(n,cross(sub(P[order[1]],P[order[0]]),sub(P[order[2]],P[order[0]])))
        assert orient!=0
        if orient<0:order.reverse()
        # Global exact polygon support and orientation check for every boundary edge.
        for u,v in zip(order,order[1:]+order[:1]):
            d=sub(P[v],P[u]);assert any(d)
            assert all(dot(n,cross(d,sub(P[w],P[u])))>=0 for w in ids)
        fs.append(order);N.append(n);input_rows.append(i)
    edges={}
    triangles=[]
    for i,f in enumerate(fs):
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(i)
        triangles += [(f[0],f[j],f[j+1]) for j in range(1,len(f)-1)]
    assert all(len(o)==2 for o in edges.values())
    el=sorted(edges);assert len(P)-len(el)+len(fs)==2
    # Connected maximal complex.
    seen={0}
    while True:
        old=len(seen)
        for a,b in el:
            if a in seen or b in seen:seen.update((a,b))
        if len(seen)==old:break
    assert len(seen)==len(P)
    def mass(origin):
        tets=[det(sub(P[a],origin),sub(P[b],origin),sub(P[c],origin)) for a,b,c in triangles]
        den=4*sum(tets)
        num=tuple(sum(t*(P[a][j]+P[b][j]+P[c][j]+origin[j]) for t,(a,b,c) in zip(tets,triangles)) for j in range(3))
        return den,num
    D,C=mass((0,0,0));assert D>0
    D2,C2=mass(P[0]);assert D2==D and C2==C
    assert C[0]==C[1]==0
    X=[sub(mul(D,p),C) for p in P]
    H=[D*L*rhs-dot(n,C) for n in N];assert min(H)>0
    un=[[] for p in P];sn=[[] for f in fs]
    for a,b in el:
        d=sub(X[b],X[a]);un[a].append(dot(X[a],d));un[b].append(-dot(X[b],d))
        i,j=edges[(a,b)]
        nij=dot(N[i],N[j]);ni=dot(N[i],N[i]);nj=dot(N[j],N[j])
        sn[i].append(nij*H[i]-ni*H[j]);sn[j].append(nij*H[j]-nj*H[i])
    U=[i for i,s in enumerate(un) if max(s)<0]
    WV=[i for i,s in enumerate(un) if max(s)==0]
    S=[i for i,s in enumerate(sn) if max(s)<0]
    # Direct feet: strict face foot lies in no other support plane.
    footS=[];boundaryfeet=[]
    for i,n in enumerate(N):
        norm=dot(n,n);ss=[H[i]*dot(n,m)-H[j]*norm for j,m in enumerate(N) if j!=i]
        if max(ss)<0:footS.append(i)
        elif max(ss)==0:boundaryfeet.append(i)
    assert S==footS
    Saddles=[];WE=[];edge_rows=[]
    for eid,(a,b) in enumerate(el):
        d=sub(X[b],X[a]);dd=dot(d,d);xd=dot(X[a],d);tn=-xd
        if 0<tn<dd:
            p=add(mul(dd,X[a]),mul(tn,d));i,j=edges[(a,b)]
            aa=dot(N[i],N[i]);ab=dot(N[i],N[j]);bb=dot(N[j],N[j]);assert aa*bb-ab*ab>0
            u=dot(p,N[i])*bb-dot(p,N[j])*ab
            v=dot(p,N[j])*aa-dot(p,N[i])*ab
            if u>0 and v>0:Saddles.append(eid)
            elif u>=0 and v>=0:WE.append(eid)
        edge_rows.append([a,b,*edges[(a,b)]])
    if not WV and not WE:assert len(S)+len(U)-len(Saddles)==2
    result=dict(name=data['name'],V=len(P),E=len(el),F=len(fs),C=2*len(el),strict=[len(S),len(U),len(Saddles)],additional_weak=[0,len(WV),len(WE)],
      stable_faces=S,unstable_vertices=U,saddle_edges=Saddles,weak_vertices=WV,weak_edges=WE,boundary_face_feet=boundaryfeet,
      volume=textfrac(D,24*L**3),centroid=[textfrac(c,D*L) for c in C],
      centred_scale_bits=(D*L).bit_length(),vertex_denominator_lcm_bits=L.bit_length(),
      primitive_zero_U_arrows=sum(s==0 for a in un for s in a),primitive_zero_Q_arrows=sum(s==0 for a in sn for s in a),
      input_rows=len(norms),active_input_rows=input_rows,vertices=[list(v) for v in verts],facets=fs,edges=edge_rows,
      checks=['positive-origin-full-dimensional','cap-plus-base-boundedness','exhaustive-integer-H-triples','maximal-exact-facets','exact-polygon-convexity','true-two-owner-edges','Euler-connected','two-origin-exact-mass','reflection-centroid-axis','all-centred-supports-positive','direct-feet-polar-S-crosscheck','all-vertex-and-mixed-edge-strict-weak'])
    return result

def main():
    path=sys.argv[1];data=json.load(open(path));out=audit(data)
    dest=(sys.argv[2] if len(sys.argv)>2 else path[:-5]+'_audit.json')
    raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();open(dest,'wb').write(raw)
    print('D2_EXACT_H_AUDIT_PASS',out['name'],out['V'],out['E'],out['F'],out['strict'],out['additional_weak'],len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
