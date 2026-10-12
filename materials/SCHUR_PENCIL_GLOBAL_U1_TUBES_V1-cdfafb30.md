# material-cdfafb30c578

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# SCHUR_PENCIL_GLOBAL_U1_TUBES_V1

## Exact object and evidence
The body is precisely Bright Willow18's moderate-cut rational body in fully read immutable parent minimum-0197, SHA a7b006ad09534e46e35a14bb5255b09a5f091f2f1672ad26878cb0d4d6dbfc94. It is NOT coordinator [internal-source-reference]'s different one-corner family. The full literal raw vertices, supports, facets, actual centroid calculation and all four metric parameters occur in the autonomous source below. No parent source file is required to execute it.

## General reciprocal Schur-pencil theorem
Normalize the distinguished primal vertex A=e3 and its full true polar face to q_i=(p_i,1), using a single invertible linear coordinate transformation about the actual volume centroid. Every SPD dual metric has uniquely the form

N(H,f,delta)=[[H,-Hf],[-f^T H,delta+f^T Hf]], H SPD, delta>0,
M=N^-1=[[H^-1+ff^T/delta,f/delta],[f^T/delta,1/delta]].

For any primal vertex x_v=(y_v,z_v), put tau_v=z_v+f.y_v. For any true directed primal edge v->w,

delta D^P_vw=delta y_v^T H^-1(y_w-y_v)+tau_v(tau_w-tau_v).

For any actual polar vertex q_k=(u_k,w_k), put v_k=u_k-w_k f. For any true directed polar edge k->l,

D^Q_kl=v_k^T H(v_l-v_k)+delta w_k(w_l-w_k).

Thus all physical primitive signs are affine in delta after multiplying primal primitives by the same positive delta. There are at most 4E positive breakpoints (fewer after coincidences). Their open intervals and the breakpoints themselves give a COMPLETE exact census along delta>0, with no condition-number bound and no sampling inference. A nonapical vertex's strict-U set is an open interval, possibly empty or unbounded, because it is an intersection of strict affine half-lines.

For poles on the distinguished face, w_i=1, so every selected polar arrow is independent of delta. The apex has delta D^P_Aw=tau_w-1, also independent of delta. Equivalently the apex is strict U when f lies in the interior of its actual planar pole polygon. Varying the normal Schur complement therefore tests genuinely global compatibility without changing any local face-arrow signs or apical instability.

Generic strict census is obtained from negative outgoing primal signs at vertices, negative outgoing dual signs at facets, and four negative coupled primitive signs at edges. At breakpoints the code records all zeros and weak-contact candidates; the U>=2 theorem uses strict vertices there too, so no weak-point bookkeeping assumption is needed for the exclusion.

## Complete four pencils of the literal actual E17 control
For the four H,f choices in the parent (omitting respectively 0->1,1->2,2->3,3->4), ALL delta>0 have the apex0 strict U and at least one further strict U. The complete 68-primitive positive-breakpoint counts are 20,22,21,20. This includes every finite primitive wall, delta->0 and delta->infinity approaches; singular endpoint matrices are not physical members.

Short exact traps, stronger than a long census list:

* Omit0: vertex2 is strict U for 0<delta<=1/40; vertex9 is strict U for delta>=1/40.
* Omit1: vertex3 is strict U for ALL delta>0.
* Omit2: vertex1 is strict U for 0<delta<=1/10; vertex5 is strict U for delta>=1/10.
* Omit3: vertex9 is strict U for ALL delta>0.

All three retained local arrows stay strictly positive; the omitted arrow is strictly negative. For the FIXED central body and each of the four FIXED H,f, every 0<delta<=1/20000 has strict222, weak000, all68 primitives nonzero. Hence U2 is attained along unbounded-condition-number sequences; this does not give U1 or110.

## Four genuine multidimensional unbounded tubes
There is a certified radius rho=1/10000. In the normalized actual chart, keep X0=e3 and all five pole last coordinates exactly1. Independently allow every other primal vertex coordinate, every planar coordinate of the five actual poles, every entry of symmetric H, and every coordinate of f to differ from the corresponding central value by at most rho. Restrict to actual uniformly filled own-centred realizations of the SAME literal incidence; independent boxes are only conservative enclosures, not claims that arbitrary box entries satisfy incidence/centroid equations.

For each of the four metric tubes and every delta>0, the corresponding trap above remains strictly unstable, the apex remains strictly unstable, the three retained polar arrows remain strictly positive, f stays strictly inside the true convex pentagon, and its four-arrow system remains minimally infeasible for common SPD. The latter follows from positive displacement-circuit weights r013/2+r023 and a positive definite tangent stress Q. Proper subsystems are supplied by the four transported metric tubes on the same actual body.

Proof of uniformity needs no compact interval for delta. For a low-delta trap, each outgoing affine numerator has negative intercept and negative value at the stated cut. For a high-delta trap, it has negative slope and negative value at the cut. For a permanent trap both coefficients are negative. These finitely many strict tests include both sides of the cut. Exact closed rational interval arithmetic verifies all shape/metric boxes at once. There are 49,43,51,43 strictly positive lower-bound guards, 186 total. Shared variables are conservatively interval-enclosed, never numerically sampled.

Scope: these are four explicit open metric/geometry neighborhoods with an unrestricted positive Schur complement, NOT all physical metrics of the body, NOT all fixed-pole completions, NOT a whole-incidence exclusion. Global bounds remain34<=Cmin<=622. To obtain U1 one must leave these particular tangent/footpoint neighborhoods or their controlled geometry, rather than merely changing delta.

## Reconstruction and actual execution
Save the complete Python fence as schur_pencil.py with final LF. CPython3.13.5, standard library, assertions enabled.

python -B -S schur_pencil.py build > build.stdout
python -B -S schur_pencil.py check > check.stdout
cmp build.stdout check.stdout

Coordinator executed build/check and repeated both from a fresh directory containing only the source; report bytes and stdout matched. This is an exact self-contained generation, not an independently written verifier or proof-assistant formalization.

Pins:
schur_pencil.py:12232 bytes SHA256 2f4fcfd1c2cd73fd47c7f95565cc373c5435ba88ab562f674773a824e3cab37c
schur_pencil.json:301990 bytes SHA256 e9b76379a35c176f33d573d7b9a194630e3293e669f920eee894a0eb09bf16ed
build.stdout=check.stdout:933 bytes SHA256 ba9eb9b6f9e070e0203f8bf161e5f6272d1977557f4f39a33932c77f0439d514

Terminal markers include:
EXACT_OWN_CENTROID_AND_68_RECIPROCAL_PRIMITIVES_PASS
COMPLETE_POSITIVE_SCHUR_PENCILS_ALL_OPEN_CELLS_AND_WALLS_PASS
FOUR_UNBOUNDED_SCHUR_TUBES_RADIUS_1E_MINUS4_STRICT_U_AT_LEAST2_PASS
TUBE_GUARDS [49, 43, 51, 43]
ALL_FOUR_PENCILS_STRICT_222_WEAK000_FOR_0_LT_DELTA_LE_1_OVER_20000_PASS

## Complete source
```python
#!/usr/bin/env python3
"""Exact reciprocal-metric census along four Schur-complement pencils.
CPython 3.13.5, standard library. Build/check: python -B -S schur_pencil.py build|check
The literal rational E17 body is Bright Willow18's moderate-cut control,
not the coordinator's different one-corner truncation family.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib, json, sys
from pathlib import Path


def vec(*a): return tuple(F(x) for x in a)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det3(x,y,z): return dot(x,cross(y,z))
def mv(A,x): return tuple(dot(r,x) for r in A)
def inv2(H):
    d=H[0][0]*H[1][1]-H[0][1]*H[1][0]
    assert H[0][0]>0 and d>0
    return ((H[1][1]/d,-H[0][1]/d),(-H[1][0]/d,H[0][0]/d))
def jdata(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):jdata(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [jdata(v) for v in x]
    return x

def body():
    Y=[vec(0,0,1),vec('16/25',0,'-7/25'),vec('-48/113','24/113','-103/113'),
       vec('-48/89','-48/89',1),vec(0,'-9/23',1),vec('-12/89','-1077/2047',1),
       vec('192/2225','-870/2047','19/25'),vec('36/283','144/283','-365/283'),
       vec('2032/7075','144/283','-11389/7075'),vec('672/31979','17970/31979','-56527/31979')]
    normals=[vec(0,0,1),vec(2,0,1),vec(2,4,1),vec(-2,5,1),vec(-3,3,1),
             vec('1/4','-23/3',-3),vec('46/41','-46/41','23/41'),
             vec('566/1579','3679/1579','283/1579'),vec('167/88','-46/77','59/77')]
    faces=[(0,3,5,4),(0,4,1),(0,1,8,7),(0,7,9,2),(0,2,3),(1,6,5,3,2,9,8),
           (4,5,6),(7,8,9),(1,4,6)]
    edges={}
    vol=F(0); moment=vec(0,0,0)
    for k,face in enumerate(faces):
        assert all((dot(normals[k],Y[i])==1) == (i in face) for i in range(10))
        assert all(dot(normals[k],x)<=1 for x in Y)
        for i,j in zip(face,face[1:]+face[:1]): edges.setdefault(tuple(sorted((i,j))),[]).append(k)
        for j in range(1,len(face)-1):
            a,b,c=(Y[face[i]] for i in (0,j,j+1))
            dv=abs(det3(a,b,c))/6
            vol+=dv; moment=add(moment,scale(dv/4,add(add(a,b),c)))
    assert len(edges)==17 and all(len(v)==2 for v in edges.values())
    g=scale(1/vol,moment)
    assert vol==F(123666516,327305065)
    assert g==vec('-1680051656893/1222121891838875','-105667341927/59176428446935','191281237573/27463413299750')
    h0=1-g[2]; t=scale(1/h0,g[:2])
    X=[]
    for y in Y:
        x=sub(y,g)
        X.append(((x[0]+t[0]*x[2])/h0,(x[1]+t[1]*x[2])/h0,x[2]/h0))
    Q=[]
    for n in normals:
        q=scale(1/(1-dot(n,g)),n)
        Q.append((h0*q[0],h0*q[1],h0*(q[2]-t[0]*q[0]-t[1]*q[1])))
    assert X[0]==vec(0,0,1)
    assert all(q[2]==1 for q in Q[:5])
    for k,face in enumerate(faces):
        assert all((dot(Q[k],X[i])==1) == (i in face) for i in range(10))
    return Y,normals,faces,edges,vol,g,X,Q


def census(coeff,edges,d):
    signs={k:(a*d+b>0)-(a*d+b<0) for k,(a,b) in coeff.items()}
    prim={i:[] for i in range(10)}; dual={i:[] for i in range(9)}
    for (kind,i,j),s in signs.items(): (prim if kind=='P' else dual)[i].append(s)
    U=[i for i,ss in prim.items() if all(s<0 for s in ss)]
    S=[i for i,ss in dual.items() if all(s<0 for s in ss)]
    Uw=[i for i,ss in prim.items() if max(ss)==0]
    Sw=[i for i,ss in dual.items() if max(ss)==0]
    H=[]; Hw=[]
    for (i,j),(k,l) in edges.items():
        ss=[signs['P',i,j],signs['P',j,i],signs['Q',k,l],signs['Q',l,k]]
        if max(ss)<0: H.append((i,j))
        elif max(ss)==0: Hw.append((i,j))
    if not(Uw or Sw or Hw): assert len(S)+len(U)-len(H)==2
    return dict(S=S,U=U,H=H,Sweak=Sw,Uweak=Uw,Hweak=Hw,
                zero_primitives=[k for k,s in signs.items() if s==0])


def pencil(H,f,edges,X,Q):
    G=inv2(H); coeff={}
    tau=[x[2]+dot(f,x[:2]) for x in X]
    v=[sub(q[:2],scale(q[2],f)) for q in Q]
    for (i,j),(k,l) in edges.items():
        for a,b in ((i,j),(j,i)):
            coeff['P',a,b]=(dot(X[a][:2],mv(G,sub(X[b][:2],X[a][:2]))),tau[a]*(tau[b]-tau[a]))
        for a,b in ((k,l),(l,k)):
            coeff['Q',a,b]=(Q[a][2]*(Q[b][2]-Q[a][2]),dot(v[a],mv(H,sub(v[b],v[a]))))
    assert len(coeff)==68 and all(a or b for a,b in coeff.values())
    # The four selected pole arrows must not depend on the Schur complement.
    assert all(coeff['Q',i,i+1][0]==0 for i in range(4))
    # Strict apical instability is independent of the positive Schur complement.
    for kind,i,j in coeff:
        if kind=='P' and i==0: assert coeff[kind,i,j][0]==0 and coeff[kind,i,j][1]<0
    roots=sorted({-b/a for a,b in coeff.values() if a and -b/a>0})
    cuts=[F(0)]+roots
    cells=[]
    for i,lo in enumerate(cuts):
        hi=roots[i] if i<len(roots) else None
        d=(lo+hi)/2 if hi is not None else lo+1
        c=census(coeff,edges,d)
        assert not c['zero_primitives']
        cells.append(dict(lo=lo,hi=hi,sample=d,census=c))
    walls=[dict(delta=d,census=census(coeff,edges,d)) for d in roots]
    # Exact unstable interval for each non-apex vertex; intersection of strict half-lines.
    intervals={}
    for i in range(1,10):
        lo=F(0);hi=None;empty=False
        for (kind,a,j),(u,w) in coeff.items():
            if kind!='P' or a!=i: continue
            if u==0:
                if w>=0: empty=True
            elif u>0:
                r=-w/u; hi=r if hi is None else min(hi,r)
            else: lo=max(lo,-w/u)
        if hi is not None and hi<=lo:empty=True
        if not empty: intervals[i]=[lo,hi]
    allcases=cells+walls
    minimum=min(len(c['census']['U']) for c in allcases)
    covers=[]
    verts=list(intervals)
    for n in range(1,len(verts)+1):
        covers=[sub for sub in combinations(verts,n) if all(any(v in c['census']['U'] for v in sub) for c in allcases)]
        if covers: break
    return dict(H=H,f=f,coefficients={str(k):v for k,v in coeff.items()},
                positive_roots=roots,cells=cells,walls=walls,unstable_intervals=intervals,
                minimal_strict_U=minimum,minimal_nonapical_covers=covers,
                distinct_open_censuses=sorted({(len(c['census']['S']),len(c['census']['U']),len(c['census']['H'])) for c in cells}),
                at_one=census(coeff,edges,F(1)))



class I:
    """Closed exact rational interval; no outward rounding is required."""
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=self.lo if hi is None else F(hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        if not isinstance(o,I):o=I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-as_i(o)
    def __rsub__(self,o):return as_i(o)+-self
    def __mul__(self,o):
        o=as_i(o); v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o);assert not o.lo<=0<=o.hi
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return as_i(o)/self

def as_i(x):return x if isinstance(x,I) else I(x)
def cross2(x,y):return x[0]*y[1]-x[1]*y[0]

def tube(omit,H,f,edges,X,Q,rho=F(1,10000)):
    B=lambda x:I(x-rho,x+rho)
    Z=[tuple(I(x) for x in X[0])]+[tuple(B(x) for x in row) for row in X[1:]]
    p=[tuple(B(x) for x in q[:2]) for q in Q[:5]]
    h=((B(H[0][0]),B(H[0][1])),(B(H[0][1]),B(H[1][1])))
    ff=tuple(B(x) for x in f)
    guards=[]
    def pos(name,x):
        x=as_i(x);assert x.lo>0,(omit,name,x.lo,x.hi)
        guards.append((name,x.lo,x.hi))
    det=h[0][0]*h[1][1]-h[0][1]*h[1][0]
    pos('H00',h[0][0]);pos('detH',det)
    g=((h[1][1]/det,-h[0][1]/det),(-h[1][0]/det,h[0][0]/det))
    tau=[x[2]+dot(ff,x[:2]) for x in Z]
    coeff={}
    for i,j in edges:
        for a,b in ((i,j),(j,i)):
            coeff[a,b]=(dot(Z[a][:2],mv(g,sub(Z[b][:2],Z[a][:2]))),tau[a]*(tau[b]-tau[a]))
    for (i,j),(a,b) in coeff.items():
        if i==0:pos('apex_'+str(j),-b)
    choices={0:('split',2,9,F(1,40)),1:('all',3),2:('split',1,5,F(1,10)),3:('all',9)}
    choice=choices[omit]
    if choice[0]=='all':
        v=choice[1]
        for (i,j),(a,b) in coeff.items():
            if i==v:
                pos('permanent_slope_'+str((i,j)),-a)
                pos('permanent_intercept_'+str((i,j)),-b)
    else:
        _,lo,hi,c=choice
        for (i,j),(a,b) in coeff.items():
            if i==lo:
                pos('low_intercept_'+str((i,j)),-b)
                pos('low_at_cut_'+str((i,j)),-(a*c+b))
            if i==hi:
                pos('high_slope_'+str((i,j)),-a)
                pos('high_at_cut_'+str((i,j)),-(a*c+b))
    for i in range(5):
        e=sub(p[(i+1)%5],p[i])
        pos('f_interior_'+str(i),cross2(e,sub(ff,p[i])))
        for j in range(5):
            if j not in (i,(i+1)%5):pos('pentagon_'+str((i,j)),cross2(e,sub(p[j],p[i])))
    ee=[sub(p[i+1],p[i]) for i in range(4)]
    for i,e in enumerate(ee):
        d=dot(sub(p[i],ff),mv(h,e))
        pos(('omitted_negative_' if i==omit else 'retained_positive_')+str(i),-d if i==omit else d)
    r1=(cross2(ee[1],ee[3]),cross2(ee[3],ee[0]),I(0),cross2(ee[0],ee[1]))
    r2=(cross2(ee[2],ee[3]),I(0),cross2(ee[3],ee[0]),cross2(ee[0],ee[2]))
    lam=[a/2+b for a,b in zip(r1,r2)]
    for i,a in enumerate(lam):pos('stress_weight_'+str(i),a)
    stress=tuple(tuple(-sum((lam[i]*(p[i][j]*ee[i][k]+p[i][k]*ee[i][j])/2 for i in range(4)),I(0)) for k in range(2)) for j in range(2))
    pos('stress_Q00',stress[0][0]);pos('stress_detQ',stress[0][0]*stress[1][1]-stress[0][1]*stress[1][0])
    return dict(radius=rho,strict_trap=choice,guards=guards,guard_count=len(guards),
                minimum_lower_bound=min(x[1] for x in guards))


def run():
    Y,normals,faces,edges,vol,g,X,Q=body()
    data=[((vec(1,'1/100'),vec('1/100','1/10')),vec('35/18','1/600')),
          ((vec(1,'-1/2'),vec('-1/2','17/64')),vec('31/25','149/60')),
          ((vec(1,'1/4'),vec('1/4','5/64')),vec(-1,'8/3')),
          ((vec(1,'1/4'),vec('1/4','65/16')),vec('-1/20','2/25'))]
    ps=[]
    for omit,(H,f) in enumerate(data):
        p=pencil(H,f,edges,X,Q)
        p['uniform_tube']=tube(omit,H,f,edges,X,Q)
        for i in range(4):
            b=p['coefficients'][str(('Q',i,i+1))][1]
            if i!=omit: assert b>0
        assert min(p['positive_roots'])>F(1,20000)
        cc=p['cells'][0]['census']
        assert (len(cc['S']),len(cc['U']),len(cc['H']))==(2,2,2)
        p['sharp_222_sector']=['0 < delta <=',F(1,20000)]
        ps.append(p)
    assert [(len(p['at_one']['S']),len(p['at_one']['U']),len(p['at_one']['H'])) for p in ps]==[(2,5,5),(2,4,4),(3,3,4),(2,3,3)]
    report=dict(identity='BRIGHT_WILLOW18_MODERATE_CUT_E17_FOUR_SCHUR_PENCILS_V1',
        parent_assignment='minimum-0197',parent_sha256='a7b006ad09534e46e35a14bb5255b09a5f091f2f1672ad26878cb0d4d6dbfc94',
        volume=vol,centroid=g,chart_vertices=X,chart_poles=Q,faces=faces,
        pencils=ps)
    out=(json.dumps(jdata(report),sort_keys=True,indent=2)+'\n').encode()
    target=Path('schur_pencil.json')
    if sys.argv[1]=='build':target.write_bytes(out)
    else:assert target.read_bytes()==out
    print('EXACT_OWN_CENTROID_AND_68_RECIPROCAL_PRIMITIVES_PASS')
    print('COMPLETE_POSITIVE_SCHUR_PENCILS_ALL_OPEN_CELLS_AND_WALLS_PASS')
    for i,p in enumerate(ps):
        print('OMIT',i,'ROOTS',len(p['positive_roots']),'MIN_STRICT_U',p['minimal_strict_U'],
              'COVERS',p['minimal_nonapical_covers'],'CENSUSES',p['distinct_open_censuses'])
    print('FOUR_UNBOUNDED_SCHUR_TUBES_RADIUS_1E_MINUS4_STRICT_U_AT_LEAST2_PASS')
    print('TUBE_GUARDS', [p['uniform_tube']['guard_count'] for p in ps])
    print('ALL_FOUR_PENCILS_STRICT_222_WEAK000_FOR_0_LT_DELTA_LE_1_OVER_20000_PASS')
    print(target.name,len(out),hashlib.sha256(out).hexdigest())

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Usage: python -B -S schur_pencil.py build|check')
    run()
```
