# material-65f6b996766c

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact nonattaining control and nonredundancy test. Requires hybrid_exact_region.py."""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,sys
from pathlib import Path
import hybrid_exact_region as h

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(t,a):return [t*x for x in a]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def mv(M,v):return [dot(row,v) for row in M]
def det(M):return dot(M[0],cross(M[1],M[2]))
def inv(M):
    d=det(M);assert d
    # adjugate column i is cross of the other cyclic rows.
    cols=[cross(M[1],M[2]),cross(M[2],M[0]),cross(M[0],M[1])]
    return [[cols[j][i]/d for j in range(3)] for i in range(3)]
def quad(v,M):return dot(v,mv(M,v))
def const(p):
    assert set(p.d)<={h.Z}
    return p.d.get(h.Z,F(0))
def conv(v):return [const(x) for x in v]
def strings(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,dict):return {str(k):strings(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)):return [strings(v) for v in a]
    return a
THETA=[F(3,20),F(3,20),F(3,20),F(9,20),F(87,1000)]
M=[[F(x) for x in row] for row in [[5,1,2],[1,3,-1],[2,-1,4]]]

def main():
    pp,zz,dd,kk,planar,nn,hh,HH,VV=h.build([(x,x) for x in THETA])
    z=[conv(v) for v in zz];D=const(dd);K=conv(kk);g=mul(1/D,K);v=[sub(a,g) for a in z]
    n=[conv(a) for a in nn];support=[const(x) for x in hh];H=[const(x) for x in HH]
    poles=[mul(D/H[i],n[i]) for i in range(9)]
    N=inv(M)
    assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]**2>0 and det(M)>0
    assert [[dot(M[i],[N[k][j] for k in range(3)]) for j in range(3)] for i in range(3)]==[[int(i==j) for j in range(3)] for i in range(3)]
    # Recover every maximal support directly from all 120 triples.
    recovered=set()
    for i,j,k in combinations(range(10),3):
        no=cross(sub(z[j],z[i]),sub(z[k],z[i]))
        if not any(no):continue
        off=dot(no,z[i]);sl=[off-dot(no,a) for a in z]
        if min(sl)<0<max(sl):continue
        recovered.add(tuple(t for t,s in enumerate(sl) if s==0))
    assert recovered=={tuple(sorted(f)) for f in h.FACES}
    edges={}
    for f,face in enumerate(h.FACES):
        for i in range(len(face)):
            a,b=sorted((face[i],face[(i+1)%len(face)]));edges.setdefault((a,b),[]).append(f)
    assert len(edges)==17 and all(len(fs)==2 for fs in edges.values())
    rows=[];us=[True]*10;ss=[True]*9;hs=[];weak=[]
    for (i,j),(f,k) in sorted(edges.items()):
        a=dot(v[i],mv(M,sub(v[j],v[i])));b=dot(v[j],mv(M,sub(v[i],v[j])))
        c=dot(poles[f],mv(N,sub(poles[k],poles[f])));d=dot(poles[k],mv(N,sub(poles[f],poles[k])))
        us[i]&=a<0;us[j]&=b<0;ss[f]&=c<0;ss[k]&=d<0
        rr=[a,b,c,d]
        if max(rr)<0:hs.append([i,j])
        if max(rr)<=0 and any(x==0 for x in rr):weak.append([i,j])
        rows.append({'edge':[i,j],'facets':[f,k],'primitives':rr})
    U=[i for i,t in enumerate(us) if t];S=[i for i,t in enumerate(ss) if t]
    assert len(S)+len(U)-len(hs)==2 and not weak
    assert all(x for rr in rows for x in rr['primitives'])
    # Independent positive apex-7 tetrahedron volume and moment integral.
    apex=z[7];Dd=F(0);Kd=[F(0)]*3
    for face in h.FACES:
        if 7 in face:continue
        a=z[face[0]]
        for t in range(1,len(face)-1):
            b,c=z[face[t]],z[face[t+1]]
            d=dot(sub(a,apex),cross(sub(b,apex),sub(c,apex)))
            assert d>0
            Dd+=d;Kd=add(Kd,mul(d/4,add(add(apex,a),add(b,c))))
    assert Dd==D and Kd==K
    # Exact largest alpha satisfying every physical R inequality.
    gamma=g[2];bounds=[]
    for n0,h0,t0,f in planar:
        nh=conv(n0);h0=const(h0)
        for i in range(7):
            for j in range(7,10):
                intercept=(1-gamma)*h0-dot(nh,g[:2])+gamma*dot(nh,z[j][:2])
                slope=-dot(nh,g[:2])+(1-gamma)*dot(nh,z[i][:2])+gamma*dot(nh,z[j][:2])
                assert intercept+h.ALPHA*slope>0
                if slope<0:bounds.append((-intercept/slope,[f,i,j],intercept,slope))
    limit,tag,intercept,slope=min(bounds)
    assert h.ALPHA<limit<F(503,1000)
    assert gamma>F(278,1000) and limit*limit<gamma
    # Any reference with the unchanged universal condition48 has minimum ceiling2401/192.
    # Even the largest R-allowed alpha gives a smaller necessary product than this.
    old_threshold=gamma/(gamma-limit*limit)
    old_floor=F(2401,192)
    assert old_threshold<old_floor
    C=[[F(x) for x in r] for r in h.C];Ci=inv(C)
    rv=[quad(a,Ci) for a in v];lq=[quad(q,C) for q in poles]
    Gamma=max(rv)*max(lq)
    chis=[quad(v[i],Ci)*quad(poles[0],C)/dot(v[i],poles[0])**2-1 for i in range(7,10)]
    assert Gamma<h.GAMMA_C_UP and max(chis)<h.CHI_UP
    out={'object':'H5_HYBRID_REFERENCE_CONTROL_L087','theta':THETA,'volume':D/6,'centroid':g,
         'vertices':z,'facet_cycles':h.FACES,'edges':list(sorted(edges)),'poles':poles,'M':M,'N':N,
         'S':S,'U':U,'H':hs,'weak_edges':weak,'rows':rows,'reference':C,'Gamma':Gamma,'chi_top':chis,
         'R_max_alpha':limit,'R_max_alpha_witness':tag,'R_intercept':intercept,'R_slope':slope,
         'original_alpha_square_gap':gamma-limit*limit,
         'universal48_min_product_ceiling':old_floor,'R_maximum_required_product':old_threshold,
         'old_ceiling_minus_max_required':old_floor-old_threshold}
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'HYBRID_EXACT_CONTROL.json')
    data=(json.dumps(strings(out),sort_keys=True,indent=2)+'\n').encode();path.write_bytes(data)
    print('V E F',10,len(edges),len(h.FACES),'S U H',len(S),len(U),len(hs),'weak',len(weak),'primitives',len(rows)*4)
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('H5_HYBRID_ACTUAL_CENTROID_NONDUPLICATE_CONTROL_PASS')
if __name__=='__main__':main()
