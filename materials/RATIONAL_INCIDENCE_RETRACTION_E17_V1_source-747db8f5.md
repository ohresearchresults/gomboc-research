# material-747db8f521e4

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""RATIONAL_INCIDENCE_RETRACTION_E17_V1.
Exact Fraction arithmetic; Python >=3.10; no third-party dependencies.
python -B rational_incidence.py build
python -B rational_incidence.py check
This is a chart/retraction control, not an S1U1 or proper110 construction.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib, json, sys

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,s): return tuple(x*s for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a):
    n=len(a)
    if not n:return Q(1)
    if n==1:return a[0][0]
    return sum(((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n)),Q(0))
def solve(a,b):
    n=len(a); den=det(a);assert den
    return tuple(det([r[:j]+[b[i]]+r[j+1:] for i,r in enumerate(a)])/den for j in range(n))

def hull_faces(x):
    facets=set()
    for ia,ib,ic in combinations(range(len(x)),3):
        normal=cross(sub(x[ib],x[ia]),sub(x[ic],x[ia]))
        if not any(normal):continue
        h=dot(normal,x[ia]); ds=[dot(normal,p)-h for p in x]
        if max(ds)<=0 or min(ds)>=0:
            facets.add(tuple(i for i,v in enumerate(ds) if not v))
    assert set().union(*map(set,facets))==set(range(len(x)))
    return tuple(sorted(facets))

def graph_and_cycles(x,faces):
    edges=tuple((i,j) for i,j in combinations(range(len(x)),2) if sum(i in f and j in f for f in faces)==2)
    cycles=[]
    for f in faces:
        neigh={i:sorted(j for j in f if j!=i and tuple(sorted((i,j))) in edges) for i in f}
        assert all(len(q)==2 for q in neigh.values())
        cyc=[min(f),neigh[min(f)][0]]
        while True:
            nxt=next(j for j in neigh[cyc[-1]] if j!=cyc[-2])
            if nxt==cyc[0]:break
            assert nxt not in cyc;cyc.append(nxt)
        assert set(cyc)==set(f)
        n=cross(sub(x[cyc[1]],x[cyc[0]]),sub(x[cyc[2]],x[cyc[0]]));h=dot(n,x[cyc[0]])
        ext=next(i for i in range(len(x)) if i not in f)
        if dot(n,x[ext])>h:cyc=[cyc[0]]+list(reversed(cyc[1:]))
        cycles.append(tuple(cyc))
    return edges,tuple(cycles)

def moments(x,cycles):
    D=Q(0); J=(Q(0),)*3
    for f in cycles:
        for j in range(1,len(f)-1):
            a,b,c=(x[i] for i in (f[0],f[j],f[j+1]))
            d=dot(a,cross(b,c));D+=d;J=add(J,scale(add(add(a,b),c),d))
    assert D>0
    return D/6,scale(J,Q(1)/(4*D))

def truncate(x):
    faces=hull_faces(x);edges,_=graph_and_cycles(x,faces)
    v=next(i for i in range(len(x)) if sum(i in e for e in edges)==3)
    ns=sorted(j if i==v else i for i,j in edges if v in (i,j))
    new=[p for i,p in enumerate(x) if i!=v]
    new.extend(add(x[v],scale(sub(x[j],x[v]),Q(1,16))) for j in ns)
    fnew=hull_faces(new);enew,_=graph_and_cycles(new,fnew)
    assert (len(new),len(enew),len(fnew))==(len(x)+2,len(edges)+3,len(faces)+1)
    return tuple(new),v

def initial_body():
    x=tuple(tuple(map(Q,p)) for p in ((0,0,0),(4,0,0),(0,4,0),(Q(1,5),Q(1,7),4),(4,0,4),(0,4,4)))
    f=hull_faces(x);e,_=graph_and_cycles(x,f)
    assert (len(x),len(e),len(f))==(6,11,7)
    x,v1=truncate(x);x,v2=truncate(x)
    f=hull_faces(x);e,cyc=graph_and_cycles(x,f);vol,g=moments(x,cyc)
    x=tuple(sub(p,g) for p in x)
    assert moments(x,cyc)==(vol,(Q(0),)*3)
    assert (len(x),len(e),len(f))==(10,17,9)
    poles=[]
    for face in cyc:
        a,b,c=(x[i] for i in face[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a);assert h>0
        poles.append(scale(n,Q(1)/h))
    return x,f,e,cyc,tuple(poles),(v1,v2)

def incidence_chart(x,faces,poles):
    nv=len(x);nf=len(faces);values=x+poles
    neigh={i:set() for i in range(nv+nf)}
    for f,ids in enumerate(faces):
        for i in ids:neigh[i].add(nv+f);neigh[nv+f].add(i)
    left=set(neigh);peel=[]
    while left:
        i=min(left,key=lambda v:(len(neigh[v]&left),v)); old=tuple(sorted(neigh[i]&left))
        assert len(old)<=3;peel.append((i,old));left.remove(i)
    specs=[];free=[]
    for i,old in reversed(peel):
        d=len(old)
        piv=next(cols for cols in combinations(range(3),d) if det([[values[j][c] for c in cols] for j in old]))
        blank=tuple(c for c in range(3) if c not in piv)
        specs.append((i,old,piv,blank))
        free.extend(values[i][c] for c in blank)
    assert len(free)==3*(nv+nf)-sum(map(len,faces))==23
    return tuple(specs),tuple(free)

def reconstruct(specs,free):
    values={};k=0
    for i,old,piv,blank in specs:
        vals=[Q(0)]*3
        for c in blank:vals[c]=free[k];k+=1
        a=[[values[j][c] for c in piv] for j in old]
        b=[Q(1)-sum((values[j][c]*vals[c] for c in blank),Q(0)) for j in old]
        for c,t in zip(piv,solve(a,b)):vals[c]=t
        values[i]=tuple(vals)
    assert k==len(free)
    return tuple(values[i] for i in range(len(values)))

def extract(specs,values):return tuple(values[i][c] for i,old,piv,blank in specs for c in blank)

def audit(x,faces,edges,cycles,poles):
    nv=len(x)
    margins=[]
    for f,ids in enumerate(faces):
        for i in range(nv):
            s=Q(1)-dot(poles[f],x[i])
            if i in ids:assert s==0
            else:assert s>0;margins.append(s)
    assert hull_faces(x)==faces
    ee,cc=graph_and_cycles(x,faces);assert ee==edges
    vol,g=moments(x,cc)
    actual_x=tuple(sub(p,g) for p in x)
    actual_q=tuple(scale(p,Q(1)/(1-dot(p,g))) for p in poles)
    assert all(1-dot(p,g)>0 for p in poles)
    for f,ids in enumerate(faces):assert all(dot(actual_q[f],actual_x[i])==1 for i in ids)
    pp={(i,j):dot(actual_x[i],sub(actual_x[j],actual_x[i])) for e in edges for i,j in (e,e[::-1])}
    fe=tuple((f,h) for f,h in combinations(range(len(faces)),2) if len(set(faces[f])&set(faces[h]))==2)
    qq={(f,h):dot(actual_q[f],sub(actual_q[h],actual_q[f])) for e in fe for f,h in (e,e[::-1])}
    U=[i for i in range(nv) if max(v for (a,b),v in pp.items() if a==i)<0]
    S=[f for f in range(len(faces)) if max(v for (a,b),v in qq.items() if a==f)<0]
    H=[]
    for i,j in edges:
        f,h=[a for a,ff in enumerate(faces) if i in ff and j in ff]
        if max(pp[i,j],pp[j,i],qq[f,h],qq[h,f])<0:H.append((i,j))
    assert len(S)+len(U)-len(H)==2
    return dict(volume=vol,actual_centroid=g,strict_counts=[len(S),len(U),len(H)],min_nonincidence=min(margins),vertices=x,poles=poles)

def bounds_and_jet_controls():
    d=12;n=23;N=(2*d+6)*(2*d+5)**(n-1);Np=5*(n*(2*d+4)+2)*N
    B=4*d*N*N*Np*Np;K=d*B
    assert K.bit_length()==480 and 2**479<=K<2**480
    # Formal germ controls only; not additional bodies.
    # C=y-x^2, J=(t,t^2) has exact incidence and positive y first at order2.
    # At a right VF: u1=A t^2+B t^3,u2=-t,c=2t => P1=(A-2)t^2+B t^3.
    controls=[]
    for A,Bb,expected in [(1,0,'FAIL'),(2,0,'FLAT'),(2,1,'ORDER3'),(3,0,'ORDER2')]:
        coeff=(Q(A-2),Q(Bb))
        status='FAIL' if coeff[0]<0 else 'ORDER2' if coeff[0]>0 else 'ORDER3' if coeff[1]>0 else 'FLAT'
        assert status==expected
        controls.append([A,Bb,list(coeff),status])
    return dict(n=n,d=d,N=N,Nprime=Np,curve_degree=B,jet_order=K,jet_order_bitlength=K.bit_length(),shared_denominator_degree=(4**19-1)//3,formal_right_jet_controls=controls)

def clean(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [clean(v) for v in x]
    return x

def main():
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    assert __debug__ and len(sys.argv)==2 and sys.argv[1] in ('build','check')
    x,f,e,cyc,p,trunc=initial_body();spec,free=incidence_chart(x,f,p)
    assert reconstruct(spec,free)==x+p
    out=dict(status='genuine E17 chart/retraction control, NOT S1U1',faces=f,edges=e,cycles=cyc,truncate_vertices=trunc,specs=spec,free_parameters=free,base=audit(x,f,e,cyc,p),bounds=bounds_and_jet_controls(),deformations=[])
    for m in (1,2,3):
        delta=Q(m,10**9)
        changed=tuple(a+delta*(((i*7)%13)-6) for i,a in enumerate(free))
        val=reconstruct(spec,changed)
        assert extract(spec,val)==changed
        assert reconstruct(spec,extract(spec,val))==val
        out['deformations'].append(audit(val[:10],f,e,cyc,val[10:]))
    raw=(json.dumps(clean(out),indent=2,sort_keys=True)+'\n').encode()
    target=Path(__file__).with_name('rational_incidence_report.json')
    if sys.argv[1]=='build':target.write_bytes(raw)
    else:assert target.read_bytes()==raw
    print('RATIONAL_INCIDENCE_RETRACTION_E17_PASS')
    print('FREE_PARAMETERS',len(free),'V_E_F',10,17,9,'DEFORMATIONS',len(out['deformations']))
    print('COUNTS',out['base']['strict_counts'],*[v['strict_counts'] for v in out['deformations']])
    for pth in (Path(__file__),target):
        b=pth.read_bytes();print(pth.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
