# material-17577b959d91

AI research material

---

# J87 continuation — exact findings and complete numerical methods

**Status:** local, not yet persisted through Pro Research. Access was rejected with
`Research run ... has no active coordinator capability`. This file is supplementary
recovery data, not evidence of a successful shared-memory or material mutation.
The target remains own strict110 / additionalweak000 / C<500; it has not been met.
Neither own121 body here is promoted to the canonical best or best own121 entrance.

## Exact results

`J87_EXACT_SUPPLEMENT.py.txt` is self-contained and uses only Python's standard
library. Run it directly to reconstruct the new rational G14 endpoint and the
exact tangent-span certificate. Expected terminal lines:

    TANGENT_SPAN 131 [41, 82, 123, 131] 1000000007 855823644
    ROTATED_G14 45 129 86 258 [1, 2, 1] [0, 0, 0]
    P_DEPTHS [0.5196998488002684] Q_DEPTHS []

The integer tangent matrix is the first variation of volume and the three volume
first moments. Four directions e1,e2,e3,(1,1,1) span the full 131-dimensional kernel
at the literal 45-point input. All kernel identities are checked over integers;
a nonzero modular minor supplies a rational rank certificate. Local controllability
follows for compositions of the finite common-direction charts. It is not a proof
of global reachability, an exact inverse for arbitrary rational targets, or a
family exclusion. The finite chart fixes volume and centroid, not merely a point
chosen as a reference.

The new G14 endpoint has S triangle [0,30,40], U vertices 0 and 40, H edge [21,30].
All face, vertex and edge tests use rational arithmetic after recomputing its own
homogeneous centroid. A diagonal flip removes triangles [0,5,19],[5,7,19] and adds
[0,5,7],[0,7,19]. Its last numerical guards are small (roughly 1e-12), but exact
endpoint tests are strict and find no weak equilibria. The whole rotated sequence
is NOT an exactly certified own121 path: intermediates approached support walls
closer than floating-point precision can safely settle, and Qhull changed the fan.
The exact endpoint and the older entirely certified one-direction path are distinct.

`J87_EXACT_REPLAY.py.txt` separately reconstructs the earlier finite certified
path: same V45/E129/F86/C258 own121 weak000 throughout; volume
1648544600316925211/1000000000000000000 and centroid exactly zero; one P bar
0.5678697406886946 -> 0.5306664908300557, no Q bars. This local script's current
SHA is given below. It differs from a previously advertised remote-material script
hash, although the literal input, parameter, and exact-output hashes match those
recorded for the path. Do not silently identify different script byte strings.

## Numerical methods and negative evidence

`parallel.py`, `witness.py`, `guarded.py` contain complete common-direction chart,
analytic derivative, persistence, and root/exclusion-guard methods. The remaining
trial programs preserve the exact non-default parameters actually used here.
They nominate candidates only; their persistence function has a numerical cutoff,
whereas the exact audits retain all positive bars and all exact zero cases.

To repeat the new trials, in one writable directory run:

    python J87_EXACT_REPLAY.py.txt
    OPENBLAS_NUM_THREADS=1 python tangent.py
    OPENBLAS_NUM_THREADS=1 python compose_trial.py
    OPENBLAS_NUM_THREADS=1 python round_candidate.py
    OPENBLAS_NUM_THREADS=1 python root_trial.py

The exact embedded checkpoint is authoritative for endpoint recovery; numerical
optimization need not be bitwise reproducible on different library/BLAS versions.
`span_certificate.py` offers a standalone file-input version of the exact span
calculation. All complete code units and required literal input data are below.

The seven directional LP probes refute treating the first z-chart stall as an
all-direction obstruction: a feasible direction [-1,1,1] lowered the numerical
P depth to 0.5306001927438758. The subsequent rotated sequence led to the exact
G14 endpoint above. Optimizing only the target U40 forward-score margin is not an
equivalent objective: one z-direction trial improved that score from roughly
-0.01125060 to -0.00780752 while worsening P depth from 0.51969985 to 0.55033110.
This is an observed tradeoff at one input, not a universal impossibility theorem.

The strongest continuation is to use this locally complete finite chart mechanism
on the shallower J85 own121 / low-stable-carrier input once its exact materials are
accessible. On the present input, track the actual P basin and new-facet Q guards
across explicit fan changes. Do not interpret fixed-topology root guards—which
can deliberately preserve class121—as evidence that the final cancellation is
impossible.

## Extraction

Each `## File:` section is a complete UTF-8 file in a fenced code block. Preserve
its trailing newline. No file is encoded, abbreviated, or omitted. The adjacent
byte count and SHA identify the exact stored text; they do not replace it.

Observed environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0.

## File: J87_EXACT_SUPPLEMENT.py.txt

Bytes: 15758

SHA-256: `e3a4af0cad9c96428a2f4205eaa3a24a767d2d9dc81194b2ae4d8f3a611df975`

```python
"""J87 exact supplement: full tangent span and a distinct own121 G14 endpoint.
This is a self-contained recovery unit; Python 3.11+ standard library only.
Run: python J87_EXACT_SUPPLEMENT.py.txt
No input files, external libraries, random choices or network access are required.
Exact numerical checkpoint denominators and all 90 coordinate rows are embedded.

Expected: TANGENT_SPAN 131 [41,82,123,131] modulo 1000000007, minor 855823644;
ROTATED_G14 V45 E129 F86 C258 strict121 weak000; one P depth about
0.5196998488002684, no Q bars, stable triangle [0,30,40], U0/U40, H[21,30].
This endpoint is NOT own110 and is NOT a canonical record. It is independently
recentered by its exact homogeneous-volume centroid in the audit; its raw volume
need not equal the earlier exactly mass-preserving path volume after G14 rounding.
The actual endpoint hull is enumerated over every triple of literal integer points.
The earlier rational path, this rounded endpoint, and numeric candidates are distinct.

The tangent matrix L contains the gradients of 6V and 24M at the literal integer
base body. Uniform coordinate scaling and centering do not change the kernel
condition dV=dM=0. For each d in (e1,e2,e3,(1,1,1)), the 4xN matrix A_d is L
contracted with d. Division-free exact kernel bases embed as delta p_i=s_i*d.
Every L times basis column is checked exactly over Z. The full constraint rank is
4; the span rank is at most 3N-4=131. A concrete 131x131 minor is nonzero modulo
1000000007, giving the matching rational lower bound. This is a deterministic
integer certificate, not a randomized heuristic. The successive ranks are
41,82,123,131. Four finite common-direction charts, with their constraints
recomputed at each intermediate body, therefore have a composition whose
Jacobian surjects onto the fixed-volume/fixed-centroid manifold at the base input.
The inverse function theorem gives real local controllability. Rational chart
parameters produce rational bodies; this does NOT assert that an arbitrary
prescribed rational body has rational inverse parameters, or global own110 reachability.

The rounded endpoint differs from the base in the actual diagonal flip:
remove [0,5,19],[5,7,19]; add [0,5,7],[0,7,19]. No exact all-along-path
certificate is claimed for the numerical rotated-chart sequence crossing that wall.
All positive endpoint P/Q bars and all weak-feature conditions use exact fractions.

Preservation status at creation: local recovery supplement, not yet written to
Pro Research because the tool rejected the coordinator capability. Original
inputs and nominal aliases are not silently merged with historical source objects.
"""
"""Exact rational hull and own-equilibrium checks. All predicates use Fraction."""
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def load():
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text())
    ip=[tuple(p) for p in data['points']]; faces=[]
    for a,b,c in combinations(range(len(ip)),3):
        n=cross(sub(ip[b],ip[a]),sub(ip[c],ip[a])); h=dot(n,ip[a])
        if n==(0,0,0): continue
        signs=[dot(n,p)-h for p in ip]
        if min(signs)<0<max(signs):continue
        if sum(t==0 for t in signs)!=3:raise ValueError('non-simplicial input')
        faces.append([a,b,c] if max(signs)==0 else [a,c,b])
    return [tuple(R(v,data['denominator']) for v in p) for p in ip],faces

def topology(p,faces):
    edges={};planes=[];verts=set()
    for i,f in enumerate(faces):
        verts.update(f);n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]])
        assert n!=(0,0,0)
        vals=[dot(n,x)-h for x in p]
        assert max(vals)==0,('invalid support',i,max(vals))
        assert {j for j,v in enumerate(vals) if v==0}==set(f),('coplanarity',i)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert verts==set(range(len(p)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
    assert len(p)-len(edges)+len(faces)==2
    return edges,planes

def mass(p,faces):
    W=R(0);K=(R(0),)*3
    for f in faces:
        a=p[f[0]]
        for i in range(1,len(f)-1):
            b,c=p[f[i]],p[f[i+1]];z=det(a,b,c)
            W+=z;K=add(K,mul(add(a,add(b,c)),z))
    assert W>0
    return W/6,mul(K,1/(4*W))

def bars(p,edges):
    rad=[dot(v,v) for v in p];parent=list(range(len(p)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(p[b],p[a]);t=max(R(0),min(R(1),-dot(p[a],d)/dot(d,d)))
        q=add(p[a],mul(d,t));events.append((dot(q,q),a,b))
    out=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        if rad[j]>level:out.append({'root':j,'birth2':str(rad[j]),'death2':str(level),'depth':str(1-level/rad[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(p))})==1
    return sorted(out,key=lambda b:R(b['depth']),reverse=True)

def audit(p,faces):
    edges,planes=topology(p,faces);V,g=mass(p,faces);xx=[sub(x,g) for x in p];yy=[]
    for n,h in planes:
        z=h-dot(n,g);assert z>0;yy.append(mul(n,1/z))
    def roots(x):
        strict=[];weak=[]
        for i,a in enumerate(x):
            m=max(dot(a,sub(b,a)) for j,b in enumerate(x) if i!=j)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(xx);S,WS=roots(yy);H=[];WH=[]
    for (a,b),ef in edges.items():
        d=sub(xx[b],xx[a]);t=-dot(xx[a],d)/dot(d,d);r=add(xx[a],mul(d,t))
        n,m=planes[ef[0][0]][0],planes[ef[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(e[0][0],e[1][0]) for e in edges.values()]
    return dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=str(V),centroid=list(map(str,g)),strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],S=S,U=U,H=H,P=bars(xx,list(edges)),Q=bars(yy,dual))


import itertools
def matrix_det(a):
    if not a:return 1
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*matrix_det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))
def transpose(a):return [list(x) for x in zip(*a)]

def face_list(p):
    faces=[]
    for i,j,k in itertools.combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]));h=dot(n,p[i]);z=[dot(n,x)-h for x in p]
        if n==(0,0,0) or min(z)<0<max(z):continue
        assert sum(x==0 for x in z)==3,'input not simplicial'
        faces.append([i,j,k] if max(z)==0 else [i,k,j])
    return faces

def first_variation(p,faces):
    L=[[0]*(3*len(p)) for _ in range(4)]
    for f in faces:
        a,b,c=[p[i] for i in f];D=dot(a,cross(b,c));t=[a[k]+b[k]+c[k] for k in range(3)]
        for v,n in zip(f,[cross(b,c),cross(c,a),cross(a,b)]):
            for j in range(3):
                L[0][3*v+j]+=n[j]
                for k in range(3):L[k+1][3*v+j]+=t[k]*n[j]+D*int(j==k)
    return L

def modular_rref(A,prime):
    A=[[int(x)%prime for x in row] for row in A];m=len(A);n=len(A[0]);piv=[];r=0
    for j in range(n):
        k=next((k for k in range(r,m) if A[k][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r];z=pow(A[r][j],-1,prime);A[r]=[(x*z)%prime for x in A[r]]
        for k in range(m):
            if k==r or not A[k][j]:continue
            z=A[k][j];A[k]=[(x-z*y)%prime for x,y in zip(A[k],A[r])]
        piv.append(j);r+=1
        if r==m:break
    return piv,A

def kernel_columns(A,prime):
    piv,_=modular_rref(A,prime);assert len(piv)==4
    T=[[row[j] for j in piv] for row in A];den=matrix_det(T);assert den!=0
    # adj(T)_{i,j}=cofactor(T)_{j,i}
    adj=[[(-1)**(i+j)*matrix_det([row[:i]+row[i+1:] for k,row in enumerate(T) if k!=j]) for j in range(4)] for i in range(4)]
    free=[j for j in range(len(A[0])) if j not in piv];out=[]
    for j in free:
        x=[0]*len(A[0]);x[j]=den
        for i,v in enumerate(piv):x[v]=-sum(adj[i][k]*A[k][j] for k in range(4))
        assert all(dot(row,x)==0 for row in A)
        out.append(x)
    return out,piv,den,free

def run(data):
    p=data['points'];f=face_list(p);L=first_variation(p,f);prime=1000000007
    rp,_=modular_rref(L,prime);assert len(rp)==4
    directions=[[1,0,0],[0,1,0],[0,0,1],[1,1,1]]
    columns=[];labels=[];stages=[]
    for d in directions:
        A=[[sum(row[3*i+k]*d[k] for k in range(3)) for i in range(len(p))] for row in L]
        cols,piv,den,free=kernel_columns(A,prime)
        for s,j in zip(cols,free):
            v=[s[i]*d[k] for i in range(len(p)) for k in range(3)]
            assert all(dot(row,v)==0 for row in L)
            columns.append(v);labels.append({'direction':d,'free_vertex':j})
        cols_piv,_=modular_rref(transpose(columns),prime)
        stages.append({'direction':d,'axis_constraint_pivots':piv,'axis_minor_det':str(den),'cumulative_rank':len(cols_piv)})
    cp,_=modular_rref(transpose(columns),prime);rank=len(cp)
    selected=[columns[j] for j in cp]
    rows,_=modular_rref(selected,prime)
    # Determinant of selected rank x rank minor, elimination over the finite field.
    square=[[selected[j][i]%prime for j in range(rank)] for i in rows]
    determinant=1
    for j in range(rank):
        k=next(k for k in range(j,rank) if square[k][j])
        if k!=j:square[j],square[k]=square[k],square[j];determinant=-determinant
        z=square[j][j];determinant=determinant*z%prime;inv=pow(z,-1,prime)
        for k in range(j+1,rank):
            fac=square[k][j]*inv%prime
            for h in range(j+1,rank):square[k][h]=(square[k][h]-fac*square[j][h])%prime
    assert determinant%prime!=0
    assert rank==3*len(p)-4
    return {'prime':prime,'N':len(p),'F':len(f),'constraint_rank':4,'span_rank':rank,'stages':stages,
            'minor_rows':rows,'minor_columns':cp,'minor_det_mod_prime':determinant%prime,
            'column_labels':[labels[j] for j in cp],
            'claim':'Four common-direction chart families span the whole fixed-volume, fixed-first-moment tangent space at this exact input. This is local controllability, not global own110 reachability.'}


BASE_DATA={'denominator': 1000000, 'name': 'J82_S1_ROBUST_G6', 'points': [[-1772498, -1222476, 446600], [-1039299, -313302, -700462], [-1003288, -275901, 132016], [-809479, -13170, 17208], [-790129, 68868, -233475], [-774789, -231542, -897502], [-797981, 62277, -350742], [-635384, -210168, -961663], [-609466, 221337, -171601], [-525729, 253449, -484224], [-489649, -200686, -996078], [-374946, -195685, -1011378], [-366813, 246691, 105757], [-316429, 451849, -418573], [-295644, 503340, -233141], [-275629, -186981, -1011480], [-229896, 416128, -495865], [-194308, 509959, -88421], [-195520, -211846, -1005706], [-187899, -558943, -768752], [-134126, 305378, -589651], [-126147, -264851, -992981], [-49174, 491813, 93901], [-35621, 178251, -677618], [-10288, 436303, 144281], [28080, 186153, 253802], [64850, 412231, 179729], [185379, 412442, 205366], [400273, 357835, 238447], [436566, 275260, 247302], [489402, -473343, -873790], [533167, 226150, 240322], [619725, 163301, 221898], [662701, 219162, -3537], [666794, 75353, 193396], [728134, -96722, -608110], [740107, 2105, 147220], [797950, 1378, -368423], [797491, -77809, 85715], [835835, -160959, 8618], [877002, -392469, -517165], [833841, -381745, -334567], [864938, -239770, -88025], [882247, -308985, -203874], [889527, -317124, -393548]]}
G14_DATA={'denominator': 100000000000000, 'points': [[-150430868514453, -95781442890126, 64514429415202], [-78851597515554, -4948798641958, -50074759060063], [-75899593633794, -2000580080701, 33253709238550], [-55562306923536, 24867540964854, 22323975163447], [-53009255792866, 33055502542937, -5148518982785], [-52831372486661, 3083867210373, -69427540698519], [-53140668258445, 32394132904258, -13721189236769], [-38272540463039, 5007927944480, -75837816778717], [-33684580170289, 48266245347145, 4873591440950], [-24578604545149, 51399666314966, -23533933142127], [-23955314854049, 5797188209026, -80064391782409], [-12828940518923, 6311545567924, -81770306922882], [-10925728240404, 50788600245705, 32790997122241], [-2275926915675, 71236637982966, -14998949852394], [349536913831, 76404975702374, 2065285347024], [-3388426426000, 7198344493555, -82082250165251], [6454274829813, 67673086603260, -22785585999449], [7471016826354, 77063749089767, 12982229664598], [3989008323260, 4539400664908, -81870223906939], [10787530724914, -30242215028100, -51591163514860], [16022445693170, 56663754482383, -32919487973053], [10000136378357, -469021934831, -81100049775399], [21770653414101, 75244466610114, 32778780242995], [25967066109888, 43804079466750, -42353163479957], [25341603897137, 69710942234130, 37763637075607], [29096598171031, 44840290074027, 48713235260899], [32780495117645, 67319790183837, 41425657271583], [44782527718703, 67367302292861, 44202279374720], [66209984462563, 62200475763654, 47872598218093], [69833708857414, 55254219329529, 48805798142148], [72698487243797, -21849746931336, -61928465468570], [79472303605396, 48281763317753, 48274203475276], [88106547760078, 42126181142558, 46591476279356], [93027136390158, 48142770011802, 22195835515534], [92794106239409, 33388850662431, 43853792963235], [102327696356615, 15649128889740, -35583071368939], [100045993391863, 26144557398687, 39476717876197], [106895757056771, 26190782558719, -12651122297444], [106048524092348, 17888185652841, 33242821634854], [109741741564381, 9689773668996, 25872642619542], [113837076533234, -12965274214366, -20171514369025], [109535230637180, -12347984631643, -5592282106696], [112630834192759, 1821872374496, 16564900951490], [114352920601572, -5095335458090, 5616585628874], [115083975408600, -5983784216972, -10073586760056]]}

if __name__=='__main__':
    span_result=run(BASE_DATA)
    f=face_list(G14_DATA['points'])
    p=[tuple(R(x,G14_DATA['denominator']) for x in row) for row in G14_DATA['points']]
    result=audit(p,f)
    assert result['strict']==[1,2,1] and result['weak']==[0,0,0]
    assert (result['V'],result['E'],result['F'])==(45,129,86)
    assert result['U']==[0,40] and result['H']==[[21,30]]
    assert {tuple(sorted(f[i])) for i in result['S']}=={(0,30,40)}
    assert len(result['P'])==1 and not result['Q']
    old={tuple(sorted(t)) for t in face_list(BASE_DATA['points'])}
    new={tuple(sorted(t)) for t in f}
    assert old-new=={(0,5,19),(5,7,19)}
    assert new-old=={(0,5,7),(0,7,19)}
    out={'span':span_result,'g14':G14_DATA,'faces':f,'audit':result,
         'removed_faces':sorted(old-new),'added_faces':sorted(new-old)}
    (ROOT/'J87_SUPPLEMENT_OUTPUT.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('TANGENT_SPAN',span_result['span_rank'],[s['cumulative_rank'] for s in span_result['stages']],
          span_result['prime'],span_result['minor_det_mod_prime'])
    print('ROTATED_G14',result['V'],result['E'],result['F'],result['C'],result['strict'],result['weak'])
    print('P_DEPTHS',[float(R(b['depth'])) for b in result['P']],'Q_DEPTHS',[float(R(b['depth'])) for b in result['Q']])
```

## File: J87_EXACT_REPLAY.py.txt

Bytes: 14923

SHA-256: `9b7c1c98e300cf00094bb20c93bc352792d059a1cd06225b60abd370ac1e818c`

```python
"""J87 exact common-direction finite mass chart; recovery capsule part 1/2.
This part ALONE reconstructs and certifies the rational own121 endpoint and path.
Part 2 preserves the numerical nomination methods, not needed for exact replay.
Run: python J87_EXACT_REPLAY.py.txt in a writable directory; Python 3.11+ stdlib.
Expected terminal markers: J87_EXACT_PARALLEL_PATH_PASS 45 129 86 [1, 2, 1] [0, 0, 0];
J87_EXACT_VOLUME_AND_CENTROID 1648544600316925211/1000000000000000000 ['0','0','0'];
J87_PATH_GUARD_DEGREES [3, 4] ADJACENT_MOVING_EDGES 103;
J87_P_DEPTHS [0.5678697406886946] [0.5306664908300557]; J87_Q_DEPTHS [].
The exact values in output, not the printed float approximations, are authoritative.

The literal input name J82_S1_ROBUST_G6 is retained without identifying it with
other historical objects carrying that alias. This capsule defines its own exact
1153-byte input, SHA 753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab.
Earlier transient source summaries gave different hashes/volume/depths. They are
not authoritative for this literal input. No coordinate row is inferred from them.
Parameters: 587 bytes, SHA 099904a8741c98d3011bfa64717dd741a5d3866a468c06ed1707f04128dfd990.
Output J87_EXACT_ENDPOINT_AND_PATH.json: 128877 bytes,
SHA 9a78d9de7f6969817e043dabc3d9cff6be07b1f0ae4dbabee42994f51e7beb26.

For centered rational p_i and common d, put v_i=p_i+s_i*d. Every face determinant
is affine in s, so V=V0+A*s. First moment is M=B*s+d*Q(s), where Q is quadratic.
Impose A*s=0 and the two transverse components of B*s=0; fix s_0=0 as a gauge.
Then p'_i=p_i+(s_i-c(s))*d, with c=(d.B*s)/(d.d*V0)+Q/V0, preserves V and M=0
exactly. No independent-star assumption is needed. Supporting tetrahedron
determinants are affine in s because any term with two parallel d factors vanishes.
Thus endpoint strict supports certify the fixed triangular hull on the whole ray.
For the segment s(lambda)=lambda*s, common recentering is quadratic. Primal
forward scores p_i.(p_j-p_i) have degree <=3. Facet normals are affine and supports
quadratic; the positive-denominator-cleared polar score has degree <=4. The
Bernstein covers certify all selected root/exclusion inequalities for 0<=lambda<=1.
Strict roots exclude weak vertex/facet equilibria. A weak edge equilibrium would
force a weak adjacent vertex or facet, hence none occurs; the exactly initial
single saddle remains single along the path. The endpoint is directly audited
on every actual face, vertex and edge as a separate exact computation.

This is a finite own121 path, NOT an own110 construction or a family exclusion.
All input/output fractions and every positive P/Q bar are retained; exact audits
have no floating-point tolerance or persistence floor. The endpoint remains
V45/E129/F86/C258 with S facet [0,30,40], U vertices 0 and 40, H edge [21,30].
"""

"""Exact rational hull and own-equilibrium checks. All predicates use Fraction."""
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def load():
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text())
    ip=[tuple(p) for p in data['points']]; faces=[]
    for a,b,c in combinations(range(len(ip)),3):
        n=cross(sub(ip[b],ip[a]),sub(ip[c],ip[a])); h=dot(n,ip[a])
        if n==(0,0,0): continue
        signs=[dot(n,p)-h for p in ip]
        if min(signs)<0<max(signs):continue
        if sum(t==0 for t in signs)!=3:raise ValueError('non-simplicial input')
        faces.append([a,b,c] if max(signs)==0 else [a,c,b])
    return [tuple(R(v,data['denominator']) for v in p) for p in ip],faces

def topology(p,faces):
    edges={};planes=[];verts=set()
    for i,f in enumerate(faces):
        verts.update(f);n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]])
        assert n!=(0,0,0)
        vals=[dot(n,x)-h for x in p]
        assert max(vals)==0,('invalid support',i,max(vals))
        assert {j for j,v in enumerate(vals) if v==0}==set(f),('coplanarity',i)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert verts==set(range(len(p)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
    assert len(p)-len(edges)+len(faces)==2
    return edges,planes

def mass(p,faces):
    W=R(0);K=(R(0),)*3
    for f in faces:
        a=p[f[0]]
        for i in range(1,len(f)-1):
            b,c=p[f[i]],p[f[i+1]];z=det(a,b,c)
            W+=z;K=add(K,mul(add(a,add(b,c)),z))
    assert W>0
    return W/6,mul(K,1/(4*W))

def bars(p,edges):
    rad=[dot(v,v) for v in p];parent=list(range(len(p)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(p[b],p[a]);t=max(R(0),min(R(1),-dot(p[a],d)/dot(d,d)))
        q=add(p[a],mul(d,t));events.append((dot(q,q),a,b))
    out=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        if rad[j]>level:out.append({'root':j,'birth2':str(rad[j]),'death2':str(level),'depth':str(1-level/rad[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(p))})==1
    return sorted(out,key=lambda b:R(b['depth']),reverse=True)

def audit(p,faces):
    edges,planes=topology(p,faces);V,g=mass(p,faces);xx=[sub(x,g) for x in p];yy=[]
    for n,h in planes:
        z=h-dot(n,g);assert z>0;yy.append(mul(n,1/z))
    def roots(x):
        strict=[];weak=[]
        for i,a in enumerate(x):
            m=max(dot(a,sub(b,a)) for j,b in enumerate(x) if i!=j)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(xx);S,WS=roots(yy);H=[];WH=[]
    for (a,b),ef in edges.items():
        d=sub(xx[b],xx[a]);t=-dot(xx[a],d)/dot(d,d);r=add(xx[a],mul(d,t))
        n,m=planes[ef[0][0]][0],planes[ef[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(e[0][0],e[1][0]) for e in edges.values()]
    return dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=str(V),centroid=list(map(str,g)),strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],S=S,U=U,H=H,P=bars(xx,list(edges)),Q=bars(yy,dual))


"""Rational common-direction chart; preserve volume and own centroid exactly."""
import json
from math import comb
from fractions import Fraction as R

def coefficients(p,faces,d):
    N=len(p);A=[R(0)]*N;B=[[R(0)]*N for _ in range(3)];rows=[]
    for f in faces:
        assert len(f)==3
        a,b,c=[p[i] for i in f];D=det(a,b,c);tot=add(a,add(b,c))
        ts=[det(d,b,c),det(a,d,c),det(a,b,d)];rows.append((f,ts))
        for j,t in zip(f,ts):
            A[j]+=t/6
            for k in range(3):B[k][j]+=(t*tot[k]+D*d[k])/24
    return A,B,rows

def solve(M,b):
    q=[list(row)+[v] for row,v in zip(M,b)];n=len(q)
    for j in range(n):
        k=next(k for k in range(j,n) if q[k][j])
        q[j],q[k]=q[k],q[j];z=q[j][j];q[j]=[v/z for v in q[j]]
        for k in range(n):
            if k==j:continue
            z=q[k][j];q[k]=[a-z*b for a,b in zip(q[k],q[j])]
    return [q[i][-1] for i in range(n)]

def chart(p,faces,d,params):
    V,g=mass(p,faces);p=[sub(v,g) for v in p];A,B,rows=coefficients(p,faces,d)
    e=(R(1),R(0),R(0)) if d[0]==0 and d[1]==0 else (d[1],-d[0],R(0))
    r=cross(d,e)
    C=[A,[sum(e[k]*B[k][j] for k in range(3)) for j in range(len(p))],
       [sum(r[k]*B[k][j] for k in range(3)) for j in range(len(p))],
       [R(int(j==0)) for j in range(len(p))]]
    piv=params['pivots'];s=[R(v,params['denominator']) for v in params['free_numerators']]
    assert len(s)==len(p) and len(piv)==4 and len(set(piv))==4
    for j in piv:s[j]=R(0)
    rhs=[-dot(row,s) for row in C]
    out=solve([[row[j] for j in piv] for row in C],rhs)
    for j,v in zip(piv,out):s[j]=v
    assert all(dot(row,s)==0 for row in C)
    linear=tuple(dot(row,s) for row in B)
    assert cross(linear,d)==(0,0,0)
    Q=sum(dot(ts,[s[j] for j in f])*sum(s[j] for j in f) for f,ts in rows)/24
    c1=dot(d,linear)/(dot(d,d)*V);c2=Q/V
    endpoint=[add(v,mul(d,si-c1-c2)) for v,si in zip(p,s)]
    V1,g1=mass(endpoint,faces)
    assert V1==V and g1==(0,0,0)
    return p,endpoint,s,c1,c2,C

def pa(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def ps(a,b):return pa(a,[-v for v in b])
def pm(a,b):
    c=[R(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def pdot(a,b):
    z=[R(0)]
    for x,y in zip(a,b):z=pa(z,pm(x,y))
    return z

def bernstein(poly,lo=R(0),hi=R(1)):
    n=len(poly)-1;power=[R(0)]*(n+1)
    for j,a in enumerate(poly):
        for k in range(j+1):power[k]+=a*comb(j,k)*lo**(j-k)*(hi-lo)**k
    return [sum(power[j]*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]

def covers(polys,lo=R(0),hi=R(1),depth=0):
    """At least one polynomial strictly positive on each rational subinterval."""
    for i,p in enumerate(polys):
        b=bernstein(p,lo,hi)
        if min(b)>0:return [(str(lo),str(hi),i,str(min(b)))]
    assert depth<30,('could not certify',str(lo),str(hi))
    m=(lo+hi)/2
    return covers(polys,lo,m,depth+1)+covers(polys,m,hi,depth+1)

def certify_path(p,faces,d,s,c1,c2,base):
    X=[[[v[k],(si-c1)*d[k],-c2*d[k]] for k in range(3)] for v,si in zip(p,s)]
    ed,_=topology(p,faces)
    proof={'vertex_roots':{},'vertex_exclusions':{},'facet_roots':{},'facet_exclusions':{}}
    degP=0;degQ=0
    for i in range(len(p)):
        candidates=[];ids=[]
        for j in range(len(p)):
            if i==j:continue
            # Difference cancels the quadratic common recentering exactly.
            delta=[ps(X[j][k],X[i][k])[:2] for k in range(3)]
            f=pdot(X[i],delta);degP=max(degP,len(f)-1)
            if i in base['U']:
                proof['vertex_roots'][f'{i},{j}']=covers([[-a for a in f]])
            else:candidates.append(f);ids.append(j)
        if i not in base['U']:proof['vertex_exclusions'][str(i)]={'candidates':ids,'cover':covers(candidates)}
    N=[];H=[]
    for f in faces:
        a,b,c=[p[j] for j in f];ia,ib,ic=f
        n0=cross(sub(b,a),sub(c,a))
        nd=add(mul(cross(d,sub(c,a)),s[ib]-s[ia]),mul(cross(sub(b,a),d),s[ic]-s[ia]))
        N.append([[n0[k],nd[k]] for k in range(3)])
        h=[dot(n0,a),dot(nd,a)+dot(n0,d)*(s[ia]-c1),-dot(n0,d)*c2]
        H.append(h);assert min(bernstein(h))>0
    for i in range(len(faces)):
        candidates=[];ids=[]
        for j in range(len(faces)):
            if i==j:continue
            # Denominators h_i^2 h_j are positive throughout the interval.
            pol=ps(pm(pdot(N[i],N[j]),H[i]),pm(pdot(N[i],N[i]),H[j]));degQ=max(degQ,len(pol)-1)
            if i in base['S']:proof['facet_roots'][f'{i},{j}']=covers([[-a for a in pol]])
            else:candidates.append(pol);ids.append(j)
        if i not in base['S']:proof['facet_exclusions'][str(i)]={'candidates':ids,'cover':covers(candidates)}
    proof['degrees']=[degP,degQ]
    return proof


INPUT_TEXT='{"denominator":1000000,"name":"J82_S1_ROBUST_G6","points":[[-1772498,-1222476,446600],[-1039299,-313302,-700462],[-1003288,-275901,132016],[-809479,-13170,17208],[-790129,68868,-233475],[-774789,-231542,-897502],[-797981,62277,-350742],[-635384,-210168,-961663],[-609466,221337,-171601],[-525729,253449,-484224],[-489649,-200686,-996078],[-374946,-195685,-1011378],[-366813,246691,105757],[-316429,451849,-418573],[-295644,503340,-233141],[-275629,-186981,-1011480],[-229896,416128,-495865],[-194308,509959,-88421],[-195520,-211846,-1005706],[-187899,-558943,-768752],[-134126,305378,-589651],[-126147,-264851,-992981],[-49174,491813,93901],[-35621,178251,-677618],[-10288,436303,144281],[28080,186153,253802],[64850,412231,179729],[185379,412442,205366],[400273,357835,238447],[436566,275260,247302],[489402,-473343,-873790],[533167,226150,240322],[619725,163301,221898],[662701,219162,-3537],[666794,75353,193396],[728134,-96722,-608110],[740107,2105,147220],[797950,1378,-368423],[797491,-77809,85715],[835835,-160959,8618],[877002,-392469,-517165],[833841,-381745,-334567],[864938,-239770,-88025],[882247,-308985,-203874],[889527,-317124,-393548]]}\n'
PARAMETER_TEXT='{"denominator":1000000000000,"direction":[0,0,1],"free_numerators":[0,6783627115,11508243772,11671165989,-15586231945,10548888903,12729267095,9286746648,15922249410,40807562793,2900915229,2813393925,24892894342,53139497800,35293254939,2233717546,0,14714879497,1727188992,0,45398204539,1313252530,31170605187,38475541930,32256804507,32886745275,33725484250,35920366636,39540585540,40038427503,67197887255,41650939062,43157428069,22612123658,44129165089,0,45825011245,35791871458,47686756140,49892944890,115426970895,78166643692,53344606406,59676585834,92621820878],"pivots":[0,19,35,16]}\n'

if __name__=='__main__':
    (ROOT/'J87_LITERAL_G6_INPUT.json').write_text(INPUT_TEXT)
    (ROOT/'J87_ENDPOINT_PARAMETERS.json').write_text(PARAMETER_TEXT)

    p,f=load();data=json.loads((ROOT/'J87_ENDPOINT_PARAMETERS.json').read_text());d=tuple(map(R,data['direction']))
    p0,p1,s,c1,c2,C=chart(p,f,d,data);base=audit(p0,f);end=audit(p1,f)
    assert base['strict']==[1,2,1] and end['strict']==[1,2,1]
    assert base['weak']==end['weak']==[0,0,0]
    proof=certify_path(p0,f,d,s,c1,c2,base)
    out={'parameters':data,'direction':list(map(str,d)),'scalar_field':list(map(str,s)),
         'common_correction':[str(c1),str(c2)],'initial':base,'endpoint':end,
         'endpoint_points':[[str(v) for v in q] for q in p1],'faces':f,
         'adjacent_moving_edges':sum(s[a]!=0 and s[b]!=0 for a,b in topology(p0,f)[0]),
         'path_certificate':proof}
    (ROOT/'J87_EXACT_ENDPOINT_AND_PATH.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('J87_EXACT_PARALLEL_PATH_PASS',end['V'],end['E'],end['F'],end['strict'],end['weak'],flush=True)
    print('J87_EXACT_VOLUME_AND_CENTROID',end['volume'],end['centroid'],flush=True)
    print('J87_PATH_GUARD_DEGREES',proof['degrees'],'ADJACENT_MOVING_EDGES',out['adjacent_moving_edges'],flush=True)
    print('J87_P_DEPTHS', [float(R(x['depth'])) for x in base['P']], [float(R(x['depth'])) for x in end['P']],flush=True)
    print('J87_Q_DEPTHS',[float(R(x['depth'])) for x in end['Q']],flush=True)
```

## File: core.py

Bytes: 4427

SHA-256: `75a276a5e9ec574a2b80cc8bc42dd40d630199641b771952e49258ae382e2e59`

```python
"""Exact rational hull and own-equilibrium checks. All predicates use Fraction."""
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))

def load():
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text())
    ip=[tuple(p) for p in data['points']]; faces=[]
    for a,b,c in combinations(range(len(ip)),3):
        n=cross(sub(ip[b],ip[a]),sub(ip[c],ip[a])); h=dot(n,ip[a])
        if n==(0,0,0): continue
        signs=[dot(n,p)-h for p in ip]
        if min(signs)<0<max(signs):continue
        if sum(t==0 for t in signs)!=3:raise ValueError('non-simplicial input')
        faces.append([a,b,c] if max(signs)==0 else [a,c,b])
    return [tuple(R(v,data['denominator']) for v in p) for p in ip],faces

def topology(p,faces):
    edges={};planes=[];verts=set()
    for i,f in enumerate(faces):
        verts.update(f);n=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));h=dot(n,p[f[0]])
        assert n!=(0,0,0)
        vals=[dot(n,x)-h for x in p]
        assert max(vals)==0,('invalid support',i,max(vals))
        assert {j for j,v in enumerate(vals) if v==0}==set(f),('coplanarity',i)
        planes.append((n,h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((i,a,b))
    assert verts==set(range(len(p)))
    assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values())
    assert len(p)-len(edges)+len(faces)==2
    return edges,planes

def mass(p,faces):
    W=R(0);K=(R(0),)*3
    for f in faces:
        a=p[f[0]]
        for i in range(1,len(f)-1):
            b,c=p[f[i]],p[f[i+1]];z=det(a,b,c)
            W+=z;K=add(K,mul(add(a,add(b,c)),z))
    assert W>0
    return W/6,mul(K,1/(4*W))

def bars(p,edges):
    rad=[dot(v,v) for v in p];parent=list(range(len(p)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(p[b],p[a]);t=max(R(0),min(R(1),-dot(p[a],d)/dot(d,d)))
        q=add(p[a],mul(d,t));events.append((dot(q,q),a,b))
    out=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        if rad[j]>level:out.append({'root':j,'birth2':str(rad[j]),'death2':str(level),'depth':str(1-level/rad[j]),'edge':[a,b]})
        parent[j]=i
    assert len({find(i) for i in range(len(p))})==1
    return sorted(out,key=lambda b:R(b['depth']),reverse=True)

def audit(p,faces):
    edges,planes=topology(p,faces);V,g=mass(p,faces);xx=[sub(x,g) for x in p];yy=[]
    for n,h in planes:
        z=h-dot(n,g);assert z>0;yy.append(mul(n,1/z))
    def roots(x):
        strict=[];weak=[]
        for i,a in enumerate(x):
            m=max(dot(a,sub(b,a)) for j,b in enumerate(x) if i!=j)
            if m<0:strict.append(i)
            elif m==0:weak.append(i)
        return strict,weak
    U,WU=roots(xx);S,WS=roots(yy);H=[];WH=[]
    for (a,b),ef in edges.items():
        d=sub(xx[b],xx[a]);t=-dot(xx[a],d)/dot(d,d);r=add(xx[a],mul(d,t))
        n,m=planes[ef[0][0]][0],planes[ef[1][0]][0]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm;assert D>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/D;y=(dot(r,m)*nn-dot(r,n)*nm)/D
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    dual=[(e[0][0],e[1][0]) for e in edges.values()]
    return dict(V=len(p),E=len(edges),F=len(faces),C=2*len(edges),volume=str(V),centroid=list(map(str,g)),strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],S=S,U=U,H=H,P=bars(xx,list(edges)),Q=bars(yy,dual))

if __name__=='__main__':
    p,f=load();r=audit(p,f)
    (ROOT/'BASE_AUDIT.json').write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    (ROOT/'base_faces.json').write_text(json.dumps(f)+'\n')
    print({k:r[k] for k in ['V','E','F','volume','centroid','strict','weak','S','U','H']})
    print('P',[(b['root'],float(R(b['depth'])),b['edge']) for b in r['P']])
    print('Q',[(b['root'],float(R(b['depth'])),b['edge']) for b in r['Q']])
```

## File: exact_chart.py

Bytes: 6251

SHA-256: `c0b987fdef9814dae39da8957cee39a9da90a4ea5aed5042bece9748c5c329a0`

```python
"""Rational common-direction chart; preserve volume and own centroid exactly."""
import json
from math import comb
from fractions import Fraction as R
from core import load,mass,audit,topology,add,sub,mul,dot,cross,det,ROOT

def coefficients(p,faces,d):
    N=len(p);A=[R(0)]*N;B=[[R(0)]*N for _ in range(3)];rows=[]
    for f in faces:
        assert len(f)==3
        a,b,c=[p[i] for i in f];D=det(a,b,c);tot=add(a,add(b,c))
        ts=[det(d,b,c),det(a,d,c),det(a,b,d)];rows.append((f,ts))
        for j,t in zip(f,ts):
            A[j]+=t/6
            for k in range(3):B[k][j]+=(t*tot[k]+D*d[k])/24
    return A,B,rows

def solve(M,b):
    q=[list(row)+[v] for row,v in zip(M,b)];n=len(q)
    for j in range(n):
        k=next(k for k in range(j,n) if q[k][j])
        q[j],q[k]=q[k],q[j];z=q[j][j];q[j]=[v/z for v in q[j]]
        for k in range(n):
            if k==j:continue
            z=q[k][j];q[k]=[a-z*b for a,b in zip(q[k],q[j])]
    return [q[i][-1] for i in range(n)]

def chart(p,faces,d,params):
    V,g=mass(p,faces);p=[sub(v,g) for v in p];A,B,rows=coefficients(p,faces,d)
    e=(R(1),R(0),R(0)) if d[0]==0 and d[1]==0 else (d[1],-d[0],R(0))
    r=cross(d,e)
    C=[A,[sum(e[k]*B[k][j] for k in range(3)) for j in range(len(p))],
       [sum(r[k]*B[k][j] for k in range(3)) for j in range(len(p))],
       [R(int(j==0)) for j in range(len(p))]]
    piv=params['pivots'];s=[R(v,params['denominator']) for v in params['free_numerators']]
    assert len(s)==len(p) and len(piv)==4 and len(set(piv))==4
    for j in piv:s[j]=R(0)
    rhs=[-dot(row,s) for row in C]
    out=solve([[row[j] for j in piv] for row in C],rhs)
    for j,v in zip(piv,out):s[j]=v
    assert all(dot(row,s)==0 for row in C)
    linear=tuple(dot(row,s) for row in B)
    assert cross(linear,d)==(0,0,0)
    Q=sum(dot(ts,[s[j] for j in f])*sum(s[j] for j in f) for f,ts in rows)/24
    c1=dot(d,linear)/(dot(d,d)*V);c2=Q/V
    endpoint=[add(v,mul(d,si-c1-c2)) for v,si in zip(p,s)]
    V1,g1=mass(endpoint,faces)
    assert V1==V and g1==(0,0,0)
    return p,endpoint,s,c1,c2,C

def pa(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def ps(a,b):return pa(a,[-v for v in b])
def pm(a,b):
    c=[R(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def pdot(a,b):
    z=[R(0)]
    for x,y in zip(a,b):z=pa(z,pm(x,y))
    return z

def bernstein(poly,lo=R(0),hi=R(1)):
    n=len(poly)-1;power=[R(0)]*(n+1)
    for j,a in enumerate(poly):
        for k in range(j+1):power[k]+=a*comb(j,k)*lo**(j-k)*(hi-lo)**k
    return [sum(power[j]*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]

def covers(polys,lo=R(0),hi=R(1),depth=0):
    """At least one polynomial strictly positive on each rational subinterval."""
    for i,p in enumerate(polys):
        b=bernstein(p,lo,hi)
        if min(b)>0:return [(str(lo),str(hi),i,str(min(b)))]
    assert depth<30,('could not certify',str(lo),str(hi))
    m=(lo+hi)/2
    return covers(polys,lo,m,depth+1)+covers(polys,m,hi,depth+1)

def certify_path(p,faces,d,s,c1,c2,base):
    X=[[[v[k],(si-c1)*d[k],-c2*d[k]] for k in range(3)] for v,si in zip(p,s)]
    ed,_=topology(p,faces)
    proof={'vertex_roots':{},'vertex_exclusions':{},'facet_roots':{},'facet_exclusions':{}}
    degP=0;degQ=0
    for i in range(len(p)):
        candidates=[];ids=[]
        for j in range(len(p)):
            if i==j:continue
            # Difference cancels the quadratic common recentering exactly.
            delta=[ps(X[j][k],X[i][k])[:2] for k in range(3)]
            f=pdot(X[i],delta);degP=max(degP,len(f)-1)
            if i in base['U']:
                proof['vertex_roots'][f'{i},{j}']=covers([[-a for a in f]])
            else:candidates.append(f);ids.append(j)
        if i not in base['U']:proof['vertex_exclusions'][str(i)]={'candidates':ids,'cover':covers(candidates)}
    N=[];H=[]
    for f in faces:
        a,b,c=[p[j] for j in f];ia,ib,ic=f
        n0=cross(sub(b,a),sub(c,a))
        nd=add(mul(cross(d,sub(c,a)),s[ib]-s[ia]),mul(cross(sub(b,a),d),s[ic]-s[ia]))
        N.append([[n0[k],nd[k]] for k in range(3)])
        h=[dot(n0,a),dot(nd,a)+dot(n0,d)*(s[ia]-c1),-dot(n0,d)*c2]
        H.append(h);assert min(bernstein(h))>0
    for i in range(len(faces)):
        candidates=[];ids=[]
        for j in range(len(faces)):
            if i==j:continue
            # Denominators h_i^2 h_j are positive throughout the interval.
            pol=ps(pm(pdot(N[i],N[j]),H[i]),pm(pdot(N[i],N[i]),H[j]));degQ=max(degQ,len(pol)-1)
            if i in base['S']:proof['facet_roots'][f'{i},{j}']=covers([[-a for a in pol]])
            else:candidates.append(pol);ids.append(j)
        if i not in base['S']:proof['facet_exclusions'][str(i)]={'candidates':ids,'cover':covers(candidates)}
    proof['degrees']=[degP,degQ]
    return proof

if __name__=='__main__':
    p,f=load();data=json.loads((ROOT/'J87_ENDPOINT_PARAMETERS.json').read_text());d=tuple(map(R,data['direction']))
    p0,p1,s,c1,c2,C=chart(p,f,d,data);base=audit(p0,f);end=audit(p1,f)
    assert base['strict']==[1,2,1] and end['strict']==[1,2,1]
    assert base['weak']==end['weak']==[0,0,0]
    proof=certify_path(p0,f,d,s,c1,c2,base)
    out={'parameters':data,'direction':list(map(str,d)),'scalar_field':list(map(str,s)),
         'common_correction':[str(c1),str(c2)],'initial':base,'endpoint':end,
         'endpoint_points':[[str(v) for v in q] for q in p1],'faces':f,
         'adjacent_moving_edges':sum(s[a]!=0 and s[b]!=0 for a,b in topology(p0,f)[0]),
         'path_certificate':proof}
    (ROOT/'J87_EXACT_ENDPOINT_AND_PATH.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('J87_EXACT_PARALLEL_PATH_PASS',end['V'],end['E'],end['F'],end['strict'],end['weak'],flush=True)
    print('J87_EXACT_VOLUME_AND_CENTROID',end['volume'],end['centroid'],flush=True)
    print('J87_PATH_GUARD_DEGREES',proof['degrees'],'ADJACENT_MOVING_EDGES',out['adjacent_moving_edges'],flush=True)
    print('J87_P_DEPTHS', [float(R(x['depth'])) for x in base['P']], [float(R(x['depth'])) for x in end['P']],flush=True)
    print('J87_Q_DEPTHS',[float(R(x['depth'])) for x in end['Q']],flush=True)
```

## File: parallel.py

Bytes: 7146

SHA-256: `16fd7f6c76dea98e28e8fc59df14a622c16954e01521c7e56b4114862fe78b45`

```python
"""Common-direction exact-polynomial chart; floats only nominate later exact tests."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize, LinearConstraint, linprog
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent

def hull(p):
    h=ConvexHull(p)
    f=h.simplices.copy()
    wrong=np.einsum('ij,ij->i',np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]),h.equations[:,:3])<0
    f[wrong]=f[wrong][:,[0,2,1]]
    # Canonical indexing, independent of Qhull ordering for ordinary comparisons.
    f=np.array([np.roll(t,-np.argmin(t)) for t in f]);f=f[np.lexsort(f[:,::-1].T)]
    return f

def mass(p,f):
    tr=p[f];D=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));return D.sum()/6,(D[:,None]*tr.sum(axis=1)).sum(axis=0)/(4*D.sum())

def edges(f):
    ed={}
    for i,tri in enumerate(f):
        for a,b in zip(tri,np.roll(tri,-1)):ed.setdefault(tuple(sorted([int(a),int(b)])),[]).append(i)
    assert all(len(v)==2 for v in ed.values())
    return np.array(list(ed),dtype=int),np.array(list(ed.values()),dtype=int)

def bars(p,e,grad=False):
    rad=np.einsum('ij,ij->i',p,p);dv=p[e[:,1]]-p[e[:,0]];dd=np.einsum('ij,ij->i',dv,dv)
    t=np.clip(-np.einsum('ij,ij->i',p[e[:,0]],dv)/dd,0,1)
    foot=p[e[:,0]]+t[:,None]*dv;levels=np.einsum('ij,ij->i',foot,foot)
    par=np.arange(len(p));out=[];gg=[]
    def root(i):
        while i!=par[i]:par[i]=par[par[i]];i=par[i]
        return i
    for k in np.argsort(-levels,kind='stable'):
        a,b=e[k];i,j=root(a),root(b)
        if i==j:continue
        if (rad[i],-i)<(rad[j],-j):i,j=j,i
        depth=1-levels[k]/rad[j]
        if depth>1e-14:
            out.append((float(depth),int(j),[int(a),int(b)]))
            if grad:
                g=np.zeros_like(p);g[j]+=2*levels[k]/rad[j]**2*p[j]
                g[a]-=2*(1-t[k])*foot[k]/rad[j];g[b]-=2*t[k]*foot[k]/rad[j]
                gg.append(g)
        par[j]=i
    return out,gg

def report(p,f=None):
    if f is None:f=hull(p)
    V,q=mass(p,f);p=p-q;ed,dual=edges(f)
    n=np.cross(p[f[:,1]]-p[f[:,0]],p[f[:,2]]-p[f[:,0]]);h=np.einsum('ij,ij->i',n,p[f[:,0]]);pp=n/h[:,None]
    P,_=bars(p,ed);Q,_=bars(pp,dual)
    return dict(V=len(np.unique(f)),E=len(ed),F=len(f),volume=float(V),centroid=q.tolist(),P=P,Q=Q)

class Chart:
    def __init__(self,p,d,f=None,anchor=0):
        self.f=hull(p) if f is None else np.array(f)
        self.V,q=mass(p,self.f);self.p=np.array(p)-q;self.q0=q
        self.d=np.array(d,dtype=float);self.d/=np.linalg.norm(self.d)
        self.N=len(p);self.ed,self.dual=edges(self.f)
        a,b,c=self.p[self.f].transpose(1,0,2)
        D=np.einsum('ij,ij->i',a,np.cross(b,c));self.T=np.zeros((len(self.f),self.N));self.R=self.T.copy()
        for k,col in enumerate([np.cross(b,c)@self.d,np.cross(c,a)@self.d,np.cross(a,b)@self.d]):
            self.T[np.arange(len(self.f)),self.f[:,k]]=col
            self.R[np.arange(len(self.f)),self.f[:,k]]=1
        self.A=self.T.sum(axis=0)/6
        self.B=((a+b+c).T@self.T+np.outer(self.d,D@self.R))/24
        perp=null_space(self.d[None,:]);C=np.vstack([self.A,perp.T@self.B])
        C=C/np.linalg.norm(C,axis=1)[:,None]
        if anchor is not None:
            C=np.vstack([C,np.eye(self.N)[anchor]])
        self.C=C;self.Z=null_space(C);self.linear_c=self.d@self.B/self.V
        self.H=(self.T.T@self.R+self.R.T@self.T)/(48*self.V)
        self.n0=np.cross(b-a,c-a);self.h0=np.einsum('ij,ij->i',self.n0,a)
        self.dn=np.zeros((len(self.f),3,self.N));self.hlin=np.zeros((len(self.f),self.N))
        for i,(ia,ib,ic) in enumerate(self.f):
            nb=np.cross(self.d,c[i]-a[i]);nc=np.cross(b[i]-a[i],self.d)
            self.dn[i,:,ib]+=nb;self.dn[i,:,ic]+=nc;self.dn[i,:,ia]-=nb+nc
            self.hlin[i]=a[i]@self.dn[i];self.hlin[i,ia]+=self.n0[i]@self.d
        self.nd=self.n0@self.d
        # Signed supporting tetrahedron conditions, affine even for adjacent moving vertices.
        K=[];rhs=[];walls=[]
        for i,(ia,ib,ic) in enumerate(self.f):
            u=self.p[ib]-self.p[ia];v=self.p[ic]-self.p[ia]
            for j in range(self.N):
                if j in (ia,ib,ic):continue
                w=self.p[j]-self.p[ia];beta=np.cross(u,v)@w
                l1=np.cross(v,w)@self.d;l2=np.cross(w,u)@self.d;l3=np.cross(u,v)@self.d
                row=np.zeros(self.N);row[ib]+=l1;row[ic]+=l2;row[j]+=l3;row[ia]-=l1+l2+l3
                fac=np.linalg.norm(row)
                if fac<1e-16:
                    assert beta<=1e-10;continue
                K.append(row/fac);rhs.append(-beta/fac);walls.append((int(i),int(j)))
        self.K=np.array(K);self.rhs=np.array(rhs);self.walls=walls
        self.KZ=self.K@self.Z
        assert self.rhs.min()>-1e-10
    def points(self,s):
        shift=self.linear_c@s+s@self.H@s
        return self.p+(s-shift)[:,None]*self.d
    def loss(self,z,wq=1.,power=1.):
        s=self.Z@z;cg=self.linear_c+2*self.H@s;p=self.points(s)
        n=self.n0+np.einsum('ikj,j->ik',self.dn,s)
        h=self.h0+self.hlin@s-self.nd*(self.linear_c@s+s@self.H@s)
        q=n/h[:,None]
        P,PG=bars(p,self.ed,True);Q,QG=bars(q,self.dual,True)
        v=0;g=np.zeros(self.N)
        for (dep,_,_),gp in zip(P,PG):
            v+=dep**power;gs=gp@self.d;g+=power*dep**(power-1)*(gs-gs.sum()*cg)
        for (dep,_,_),gq in zip(Q,QG):
            v+=wq*dep**power
            a=np.einsum('ik,ikj->j',gq/h[:,None],self.dn)
            b=np.einsum('ij,ij->i',gq,n)/h**2
            gs=a-b@self.hlin+(b@self.nd)*cg
            g+=wq*power*dep**(power-1)*gs
        return v,self.Z.T@g
    def optimize(self,limit=.3,weight=2.,maxiter=250):
        # Keep original chamber strictly inside numerical tolerances, rational endpoint later audited exactly.
        eps=np.minimum(1e-10,self.rhs*.001)
        con=[LinearConstraint(self.KZ,-np.inf,self.rhs-eps),LinearConstraint(self.Z,-limit,limit)]
        z=np.zeros(self.Z.shape[1]);initial=self.loss(z,weight)
        out=minimize(lambda zz:self.loss(zz,weight),z,jac=True,method='SLSQP',constraints=con,
                     options=dict(maxiter=maxiter,ftol=2e-12,disp=False))
        s=self.Z@out.x;p=self.points(s)
        return p,dict(success=bool(out.success),message=out.message,iterations=int(out.nit),fun=float(out.fun),initial=float(initial[0]),maxs=float(abs(s).max()),chamber_slack=float((self.rhs-self.K@s).min()),linear_residual=float(abs(self.C@s).max()),reported=report(p,self.f),s=s.tolist(),d=self.d.tolist())

if __name__=='__main__':
    from scipy.optimize._numdiff import approx_derivative
    dat=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text());p=np.array(dat['points'])/dat['denominator']
    print('BASE',report(p),flush=True)
    chart=Chart(p,[1,2,3]);z=np.zeros(chart.Z.shape[1]);v,g=chart.loss(z)
    gn=approx_derivative(lambda zz:chart.loss(zz)[0],z,method='3-point').ravel()
    print('gradient_error',abs(g-gn).max(),'dof',chart.Z.shape[1],flush=True)
    s=chart.Z@np.random.default_rng(8701).normal(0,1e-5,chart.Z.shape[1]);pp=chart.points(s)
    print('chart_mass_check',mass(pp,chart.f),flush=True)
```

## File: witness.py

Bytes: 3296

SHA-256: `39a5230e2ed16be12077ef500816eea6fd4aa76580295744c0a3a341c00e7dd3`

```python
"""Finite parallel-chart optimization with all nonstable-facet guards."""
import numpy as np
from scipy.optimize import minimize,LinearConstraint,NonlinearConstraint
from parallel import Chart,report,mass,ROOT
import json

def scores(x):
    rad=np.einsum('ij,ij->i',x,x);val=x@x.T/rad[:,None]-1
    np.fill_diagonal(val,-np.inf);j=val.argmax(axis=1)
    f=val[np.arange(len(x)),j];G=np.zeros((len(x),len(x),3))
    for i,k in enumerate(j):
        G[i,i]+=x[k]/rad[i]-2*np.dot(x[i],x[k])/rad[i]**2*x[i]
        G[i,k]+=x[i]/rad[i]
    return f,G,j

def witnesses(c,z):
    s=c.Z@z;cg=c.linear_c+2*c.H@s;p=c.points(s)
    n=c.n0+np.einsum('ikj,j->ik',c.dn,s)
    h=c.h0+c.hlin@s-c.nd*(c.linear_c@s+s@c.H@s)
    q=n/h[:,None]
    fp,Gp,jp=scores(p);fq,Gq,jq=scores(q)
    gp=Gp@c.d;gp-=gp.sum(axis=1)[:,None]*cg
    dh=c.hlin-c.nd[:,None]*cg
    dq=c.dn/h[:,None,None]-n[:,:,None]*dh[:,None,:]/h[:,None,None]**2
    gq=np.einsum('afk,fkj->aj',Gq,dq)
    return fp,fq,gp@c.Z,gq@c.Z,jp,jq

def optimize(c,limit=.6,maxiter=500,qweight=1.,eps=1e-7,guards=True,start=None):
    z=np.zeros(c.Z.shape[1]) if start is None else start
    fp,fq,*_=witnesses(c,z);rootp=int(np.argmin(fp));rootq=int(np.argmin(fq))
    ip=np.arange(c.N)!=rootp;iq=np.arange(len(c.f))!=rootq
    def fun(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        loss=np.minimum(fp[ip]-eps,0);lq=np.minimum(fq[iq]-eps,0)
        rootlp=max(fp[rootp]+eps,0);rootlq=max(fq[rootq]+eps,0)
        v=loss@loss+qweight*(lq@lq)+rootlp**2+qweight*rootlq**2
        gg=2*loss@gp[ip]+2*qweight*lq@gq[iq]+2*rootlp*gp[rootp]+2*qweight*rootlq*gq[rootq]
        return v,gg
    def qguards(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        return np.r_[fq[iq]-eps,-fq[rootq]-eps,-fp[rootp]-eps]
    def qguardsjac(zz):
        fp,fq,gp,gq,*_=witnesses(c,zz)
        return np.vstack([gq[iq],-gq[rootq],-gp[rootp]])
    con=[LinearConstraint(c.KZ,-np.inf,c.rhs-np.minimum(1e-9,c.rhs*.001)),LinearConstraint(c.Z,-limit,limit)]
    if guards:con.append(NonlinearConstraint(qguards,0,np.inf,jac=qguardsjac))
    out=minimize(fun,z,jac=True,method='SLSQP',constraints=con,
                 options=dict(maxiter=maxiter,ftol=1e-15,disp=False))
    s=c.Z@out.x;pp=c.points(s);fp,fq,*_=witnesses(c,out.x)
    res=dict(success=bool(out.success),message=out.message,iterations=int(out.nit),fun=float(out.fun),
             pviolations=int((fp[ip]<eps).sum()),qviolations=int((fq[iq]<eps).sum()),
             rootp=rootp,rootq=rootq,minp=float(fp[ip].min()),minq=float(fq[iq].min()),
             slack=float((c.rhs-c.K@s).min()),maxs=float(abs(s).max()),s=s.tolist(),d=c.d.tolist(),reported=report(pp,c.f))
    return pp,res

if __name__=='__main__':
    dat=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text());p=np.array(dat['points'])/dat['denominator']
    for i,d in enumerate([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,0,1],[-1,1,1]]):
        c=Chart(p,d);pp,r=optimize(c,limit=.7,maxiter=250,eps=1e-7)
        print(i,d,{k:r[k] for k in r if k not in ['s','d','reported']},'P',[(round(x[0],10),x[1]) for x in r['reported']['P']], 'Q', [(round(x[0],10),x[1]) for x in r['reported']['Q']],flush=True)
        np.savez(ROOT/f'witness_{i}.npz',points=pp,s=r['s'],d=d)
        (ROOT/f'witness_{i}.json').write_text(json.dumps(r,indent=2)+'\n')
```

## File: guarded.py

Bytes: 2485

SHA-256: `cefa60c9da46e9c4b9f0439cd90edf68e03278fd991736cbb5808056c506866c`

```python
"""P-depth descent with strict own121 root/exclusion guards and exact-polynomial mass."""
import numpy as np,json,time
from scipy.optimize import minimize,LinearConstraint,NonlinearConstraint
from witness import witnesses
from parallel import Chart,ROOT,report

def optimize(c,limit=.7,maxiter=300,eps=1e-8):
    z0=np.zeros(c.Z.shape[1]);fp,fq,*_=witnesses(c,z0)
    rootsP=np.where(fp<0)[0];rootsQ=np.where(fq<0)[0]
    assert len(rootsP)==2 and len(rootsQ)==1
    ip=np.ones(c.N,dtype=bool);ip[rootsP]=False
    iq=np.ones(len(c.f),dtype=bool);iq[rootsQ]=False
    eps=min(eps,float(fp[ip].min()/10),float(fq[iq].min()/10),float((-fp[rootsP]).min()/10),float((-fq[rootsQ]).min()/10))
    assert eps>0
    def gv(z):
        fp,fq,*_=witnesses(c,z)
        return np.r_[fp[ip]-eps,fq[iq]-eps,-fp[rootsP]-eps,-fq[rootsQ]-eps]
    def gj(z):
        fp,fq,gp,gq,*_=witnesses(c,z)
        return np.vstack([gp[ip],gq[iq],-gp[rootsP],-gq[rootsQ]])
    best=[float(c.loss(z0)[0]),z0.copy(),0]
    def cb(z):
        s=c.Z@z;feasible=gv(z).min()>-1e-12 and (c.rhs-c.K@s).min()>0 and abs(s).max()<limit+1e-12
        if feasible:
            val=c.loss(z)[0]
            if val<best[0]:best[:]=[val,z.copy(),best[2]+1]
    con=[LinearConstraint(c.KZ,-np.inf,c.rhs-np.minimum(1e-8,c.rhs*.001)),LinearConstraint(c.Z,-limit,limit),NonlinearConstraint(gv,0,np.inf,jac=gj)]
    out=minimize(lambda z:c.loss(z,wq=0),z0,jac=True,method='SLSQP',constraints=con,callback=cb,
                 options=dict(maxiter=maxiter,ftol=1e-13,disp=False))
    cb(out.x);z=best[1];s=c.Z@z;p=c.points(s)
    r=dict(success=bool(out.success),message=out.message,iterations=int(out.nit),best_loss=float(best[0]),updates=best[2],
           guard_margin=float(gv(z).min()),eps=eps,slack=float((c.rhs-c.K@s).min()),maxs=float(abs(s).max()),
           s=s.tolist(),d=c.d.tolist(),reported=report(p,c.f))
    return p,r

if __name__=='__main__':
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text());p=np.array(data['points'])/data['denominator']
    for i,d in enumerate([[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,0,1],[-1,1,1]]):
        st=time.monotonic();c=Chart(p,d);pp,r=optimize(c,maxiter=180)
        print(i,d,'seconds',round(time.monotonic()-st,2),{k:r[k] for k in r if k not in ['s','d','reported']},'P',r['reported']['P'],'Q',r['reported']['Q'],flush=True)
        (ROOT/f'guarded_{i}.json').write_text(json.dumps(r,indent=2)+'\n');np.savez(ROOT/f'guarded_{i}.npz',points=pp,s=r['s'],d=d)
```

## File: tangent.py

Bytes: 2630

SHA-256: `ba6648e2127acbeaf78d180ebad94a61a24704b0241c36001f6ff22efabfde46`

```python
"""Directional LP diagnostic and feasible finite step on the exact J87 endpoint.
Numerical nominations only. The endpoint census is evaluated on the actual hull.
"""
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from parallel import Chart,report
from witness import witnesses
ROOT=Path(__file__).resolve().parent

def load_endpoint():
    data=json.loads((ROOT/'J87_EXACT_ENDPOINT_AND_PATH.json').read_text())
    return np.array([[float(Fraction(v)) for v in x] for x in data['endpoint_points']])

def feasible(c,z,rootsP,rootsQ):
    fp,fq,*_=witnesses(c,z)
    ip=np.ones(c.N,dtype=bool);ip[rootsP]=False
    iq=np.ones(len(c.f),dtype=bool);iq[rootsQ]=False
    return (fp[ip].min()>1e-12 and fq[iq].min()>1e-12 and fp[rootsP].max()<-1e-12
            and fq[rootsQ].max()<-1e-12 and (c.rhs-c.KZ@z).min()>1e-13)

def step(p,d,trust=.01):
    c=Chart(p,d);zero=np.zeros(c.Z.shape[1]);value,grad=c.loss(zero,wq=0)
    fp,fq,gp,gq,*_=witnesses(c,zero)
    rp=np.where(fp<0)[0];rq=np.where(fq<0)[0]
    ip=np.ones(c.N,dtype=bool);ip[rp]=False
    iq=np.ones(len(c.f),dtype=bool);iq[rq]=False
    gf=np.r_[fp[ip],fq[iq],-fp[rp],-fq[rq]]
    gj=np.vstack([gp[ip],gq[iq],-gp[rp],-gq[rq]])
    # Linearized inequalities retain a tenth of each existing positive witness.
    A=np.vstack([c.KZ,c.Z,-c.Z,-gj]);b=np.r_[c.rhs*.9,np.full(c.N,trust),np.full(c.N,trust),.9*gf]
    opt=linprog(grad,A_ub=A,b_ub=b,bounds=[(None,None)]*len(zero),method='highs',
                options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    result={'direction':list(d),'trust':trust,'initial':value,'lp_success':bool(opt.success),
            'message':opt.message}
    if not opt.success:return p,result
    result['predicted']=float(opt.fun)
    alpha=1.
    for k in range(40):
        zz=alpha*opt.x
        new=c.loss(zz,wq=0)[0]
        if feasible(c,zz,rp,rq) and new<value-1e-12:
            pp=c.points(c.Z@zz)
            result.update(alpha=alpha,loss=float(new),drop=float(value-new),s=(c.Z@zz).tolist(),
                          direction_normalized=c.d.tolist(),actual_hull=report(pp))
            return pp,result
        alpha*=.5
    result.update(alpha=0.,loss=value,drop=0.)
    return p,result

if __name__=='__main__':
    p=load_endpoint();ans=[]
    for d in [[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,0,1],[-1,1,1]]:
        pp,r=step(p,d);ans.append(r)
        print({k:v for k,v in r.items() if k not in ['s','actual_hull']},flush=True)
    (ROOT/'J87_TANGENT_DIAGNOSTIC.json').write_text(json.dumps(ans,indent=2)+'\n')
```

## File: compose_trial.py

Bytes: 781

SHA-256: `8693a6f95c9a569ced6a36c0dc9ab54531c512b3899fe1004cfc6e3f47d0e08e`

```python
"""Rotated-chart guarded continuation; all outputs are numerical candidates."""
import json,time
import numpy as np
from tangent import load_endpoint
from parallel import Chart,ROOT
from guarded import optimize
if __name__=='__main__':
    p=load_endpoint();history=[]
    for i,d in enumerate([[-1,1,1],[2,0,1],[1,1,1],[0,0,1],[1,0,0],[0,1,0],[-1,1,1]]):
        st=time.monotonic();c=Chart(p,d);pp,r=optimize(c,limit=.5,maxiter=150,eps=1e-9)
        history.append(r);p=pp
        print('STEP',i,d,'SECONDS',time.monotonic()-st,{k:r[k] for k in r if k not in ['s','d','reported']},
              'P',r['reported']['P'],'Q',r['reported']['Q'],flush=True)
        (ROOT/'J87_ROTATED_CONTINUATION.json').write_text(json.dumps({'history':history,'points':p.tolist()},indent=2)+'\n')
```

## File: round_candidate.py

Bytes: 1108

SHA-256: `7971365c425570ff2883545901d2514ec9ef7555246a5c56b3a43eceba96d23c`

```python
"""Exact endpoint audit after deterministic ties-to-even grid rounding.
The source is a numerical candidate; no same-volume claim is made after rounding.
"""
import json
from fractions import Fraction as R
import numpy as np
from parallel import hull,ROOT
from core import audit

if __name__=='__main__':
    raw=json.loads((ROOT/'J87_ROTATED_CONTINUATION.json').read_text());p=np.array(raw['points'])
    scale=10**14
    # Fraction.from_float makes the rounding rule unambiguous for this checkpoint.
    ints=[[round(R(float(x))*scale) for x in row] for row in p]
    f=hull(np.array(ints,dtype=float)/scale).tolist()
    q=[tuple(R(x,scale) for x in row) for row in ints]
    result=audit(q,f)
    out={'denominator':scale,'points':ints,'faces':f,'audit':result}
    (ROOT/'J87_ROTATED_G14_EXACT.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print({k:result[k] for k in ['V','E','F','C','strict','weak','S','U','H']},flush=True)
    print('P',[(x['root'],float(R(x['depth']))) for x in result['P']],'Q',[(x['root'],float(R(x['depth']))) for x in result['Q']],flush=True)
```

## File: root_trial.py

Bytes: 2556

SHA-256: `3bc3ada808886176a80e5b45e54cf3437204c1c1b19660b41d0c9cb3efd0f3ab`

```python
"""Target-U forward-score optimization under all other root/exclusion guards.
Numerical candidates are scored on the actual hull, never inherited topology alone.
"""
import json,time
import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint
from parallel import Chart,ROOT,report
from witness import witnesses


def optimize(c,target=40,limit=.3,maxiter=200,margin=1e-11):
    z0=np.zeros(c.Z.shape[1]);fp,fq,*_=witnesses(c,z0)
    rootsP=np.where(fp<0)[0];rootsQ=np.where(fq<0)[0]
    assert target in rootsP and len(rootsP)==2 and len(rootsQ)==1
    keepP=np.array([v for v in rootsP if v!=target]);ip=np.ones(c.N,dtype=bool);ip[rootsP]=False
    iq=np.ones(len(c.f),dtype=bool);iq[rootsQ]=False
    margins=np.minimum(margin,np.r_[fp[ip],fq[iq],-fp[keepP],-fq[rootsQ]]*.1)
    def gv(z):
        fp,fq,*_=witnesses(c,z)
        return np.r_[fp[ip],fq[iq],-fp[keepP],-fq[rootsQ]]-margins
    def gj(z):
        _,_,gp,gq,*_=witnesses(c,z)
        return np.vstack([gp[ip],gq[iq],-gp[keepP],-gq[rootsQ]])
    def fun(z):
        fp,_,gp,*_=witnesses(c,z)
        return -fp[target],-gp[target]
    best=[fun(z0)[0],z0.copy()]
    def cb(z):
        v=fun(z)[0];slack=(c.rhs-c.KZ@z).min()
        if gv(z).min()>-1e-14 and slack>1e-11 and abs(c.Z@z).max()<limit+1e-10 and v<best[0]:
            best[:]=[v,z.copy()]
    con=[LinearConstraint(c.KZ,-np.inf,c.rhs-np.minimum(c.rhs*.001,1e-10)),
         LinearConstraint(c.Z,-limit,limit),NonlinearConstraint(gv,0,np.inf,jac=gj)]
    out=minimize(fun,z0,jac=True,method='SLSQP',constraints=con,callback=cb,
                 options={'maxiter':maxiter,'ftol':1e-13,'disp':False})
    cb(out.x);z=best[1];p=c.points(c.Z@z);fp,fq,*_=witnesses(c,z)
    result={'success':bool(out.success),'message':out.message,'iterations':out.nit,
            'target_score':float(fp[target]),'s':(c.Z@z).tolist(),'d':c.d.tolist(),
            'guard_slack':float(gv(z).min()),'hull_slack':float((c.rhs-c.KZ@z).min()),
            'actual':report(p)}
    return p,result

if __name__=='__main__':
    raw=json.loads((ROOT/'J87_ROTATED_G14_EXACT.json').read_text());p=np.array(raw['points'],dtype=float)/raw['denominator']
    ans=[]
    for d in [[1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,2,3],[2,0,1],[-1,1,1]]:
        st=time.monotonic();pp,r=optimize(Chart(p,d));ans.append({'result':r,'points':pp.tolist()})
        print(d,'seconds',time.monotonic()-st,{k:v for k,v in r.items() if k not in ['s','d']},flush=True)
        (ROOT/'J87_ROOT_TRIAL.json').write_text(json.dumps(ans,indent=2)+'\n')
```

## File: span_certificate.py

Bytes: 5049

SHA-256: `1f3cf7ef45e1ba2504042d89534912bafc2cafc0f14cd7210d884e7e72ee27f0`

```python
"""Exact rational tangent-span certificate for parallel-motion charts.
Integer first variation matrix plus division-free kernel bases. A nonzero minor
modulo a stated prime proves the rational rank lower bound, not a probabilistic
claim: all kernel identities are checked over Z and the rank upper bound is 3N-4.
"""
import json,itertools,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def det(a):
    if not a:return 1
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))
def transpose(a):return [list(x) for x in zip(*a)]

def face_list(p):
    faces=[]
    for i,j,k in itertools.combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]));h=dot(n,p[i]);z=[dot(n,x)-h for x in p]
        if n==[0,0,0] or min(z)<0<max(z):continue
        assert sum(x==0 for x in z)==3,'input not simplicial'
        faces.append([i,j,k] if max(z)==0 else [i,k,j])
    return faces

def first_variation(p,faces):
    L=[[0]*(3*len(p)) for _ in range(4)]
    for f in faces:
        a,b,c=[p[i] for i in f];D=dot(a,cross(b,c));t=[a[k]+b[k]+c[k] for k in range(3)]
        for v,n in zip(f,[cross(b,c),cross(c,a),cross(a,b)]):
            for j in range(3):
                L[0][3*v+j]+=n[j]
                for k in range(3):L[k+1][3*v+j]+=t[k]*n[j]+D*int(j==k)
    return L

def modular_rref(A,prime):
    A=[[int(x)%prime for x in row] for row in A];m=len(A);n=len(A[0]);piv=[];r=0
    for j in range(n):
        k=next((k for k in range(r,m) if A[k][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r];z=pow(A[r][j],-1,prime);A[r]=[(x*z)%prime for x in A[r]]
        for k in range(m):
            if k==r or not A[k][j]:continue
            z=A[k][j];A[k]=[(x-z*y)%prime for x,y in zip(A[k],A[r])]
        piv.append(j);r+=1
        if r==m:break
    return piv,A

def kernel_columns(A,prime):
    piv,_=modular_rref(A,prime);assert len(piv)==4
    T=[[row[j] for j in piv] for row in A];den=det(T);assert den!=0
    # adj(T)_{i,j}=cofactor(T)_{j,i}
    adj=[[(-1)**(i+j)*det([row[:i]+row[i+1:] for k,row in enumerate(T) if k!=j]) for j in range(4)] for i in range(4)]
    free=[j for j in range(len(A[0])) if j not in piv];out=[]
    for j in free:
        x=[0]*len(A[0]);x[j]=den
        for i,v in enumerate(piv):x[v]=-sum(adj[i][k]*A[k][j] for k in range(4))
        assert all(dot(row,x)==0 for row in A)
        out.append(x)
    return out,piv,den,free

def run(data):
    p=data['points'];f=face_list(p);L=first_variation(p,f);prime=1000000007
    rp,_=modular_rref(L,prime);assert len(rp)==4
    directions=[[1,0,0],[0,1,0],[0,0,1],[1,1,1]]
    columns=[];labels=[];stages=[]
    for d in directions:
        A=[[sum(row[3*i+k]*d[k] for k in range(3)) for i in range(len(p))] for row in L]
        cols,piv,den,free=kernel_columns(A,prime)
        for s,j in zip(cols,free):
            v=[s[i]*d[k] for i in range(len(p)) for k in range(3)]
            assert all(dot(row,v)==0 for row in L)
            columns.append(v);labels.append({'direction':d,'free_vertex':j})
        cols_piv,_=modular_rref(transpose(columns),prime)
        stages.append({'direction':d,'axis_constraint_pivots':piv,'axis_minor_det':str(den),'cumulative_rank':len(cols_piv)})
    cp,_=modular_rref(transpose(columns),prime);rank=len(cp)
    selected=[columns[j] for j in cp]
    rows,_=modular_rref(selected,prime)
    # Determinant of selected rank x rank minor, elimination over the finite field.
    square=[[selected[j][i]%prime for j in range(rank)] for i in rows]
    determinant=1
    for j in range(rank):
        k=next(k for k in range(j,rank) if square[k][j])
        if k!=j:square[j],square[k]=square[k],square[j];determinant=-determinant
        z=square[j][j];determinant=determinant*z%prime;inv=pow(z,-1,prime)
        for k in range(j+1,rank):
            fac=square[k][j]*inv%prime
            for h in range(j+1,rank):square[k][h]=(square[k][h]-fac*square[j][h])%prime
    assert determinant%prime!=0
    assert rank==3*len(p)-4
    return {'prime':prime,'N':len(p),'F':len(f),'constraint_rank':4,'span_rank':rank,'stages':stages,
            'minor_rows':rows,'minor_columns':cp,'minor_det_mod_prime':determinant%prime,
            'column_labels':[labels[j] for j in cp],
            'claim':'Four common-direction chart families span the whole fixed-volume, fixed-first-moment tangent space at this exact input. This is local controllability, not global own110 reachability.'}

if __name__=='__main__':
    data=json.loads((ROOT/'J87_LITERAL_G6_INPUT.json').read_text())
    result=run(data)
    (ROOT/'J87_SPAN_CERTIFICATE.json').write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print('J87_EXACT_TANGENT_SPAN_PASS',result['span_rank'],[s['cumulative_rank'] for s in result['stages']],result['minor_det_mod_prime'])
```

## File: J87_LITERAL_G6_INPUT.json

Bytes: 1153

SHA-256: `753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab`

```json
{"denominator":1000000,"name":"J82_S1_ROBUST_G6","points":[[-1772498,-1222476,446600],[-1039299,-313302,-700462],[-1003288,-275901,132016],[-809479,-13170,17208],[-790129,68868,-233475],[-774789,-231542,-897502],[-797981,62277,-350742],[-635384,-210168,-961663],[-609466,221337,-171601],[-525729,253449,-484224],[-489649,-200686,-996078],[-374946,-195685,-1011378],[-366813,246691,105757],[-316429,451849,-418573],[-295644,503340,-233141],[-275629,-186981,-1011480],[-229896,416128,-495865],[-194308,509959,-88421],[-195520,-211846,-1005706],[-187899,-558943,-768752],[-134126,305378,-589651],[-126147,-264851,-992981],[-49174,491813,93901],[-35621,178251,-677618],[-10288,436303,144281],[28080,186153,253802],[64850,412231,179729],[185379,412442,205366],[400273,357835,238447],[436566,275260,247302],[489402,-473343,-873790],[533167,226150,240322],[619725,163301,221898],[662701,219162,-3537],[666794,75353,193396],[728134,-96722,-608110],[740107,2105,147220],[797950,1378,-368423],[797491,-77809,85715],[835835,-160959,8618],[877002,-392469,-517165],[833841,-381745,-334567],[864938,-239770,-88025],[882247,-308985,-203874],[889527,-317124,-393548]]}
```

## File: J87_ENDPOINT_PARAMETERS.json

Bytes: 587

SHA-256: `099904a8741c98d3011bfa64717dd741a5d3866a468c06ed1707f04128dfd990`

```json
{"denominator":1000000000000,"direction":[0,0,1],"free_numerators":[0,6783627115,11508243772,11671165989,-15586231945,10548888903,12729267095,9286746648,15922249410,40807562793,2900915229,2813393925,24892894342,53139497800,35293254939,2233717546,0,14714879497,1727188992,0,45398204539,1313252530,31170605187,38475541930,32256804507,32886745275,33725484250,35920366636,39540585540,40038427503,67197887255,41650939062,43157428069,22612123658,44129165089,0,45825011245,35791871458,47686756140,49892944890,115426970895,78166643692,53344606406,59676585834,92621820878],"pivots":[0,19,35,16]}
```

## File: J87_ROTATED_G14_EXACT.json

Bytes: 4484

SHA-256: `e00728213a3eedca4f704211ea8817e19411678295291f33a22b9ab2552e9013`

```json
{"audit":{"C":258,"E":129,"F":86,"H":[[21,30]],"P":[{"birth2":"5296461761085297852482450198042048450190516467887621928155528196062102970536764579149658377932323606468014547687771/3913486990897106788753401527067925835017897012405598049028317025092443240234825037799840000000000000000000000000000","death2":"6049078936101849445551949045416561080877646880578307804703057999300253155079327438304291487833074558309866656143477021566191742730390505438223/9305818584069993963423947826935902710318688307111331571985695111625401999583501881740676775920585634057080895890720000000000000000000000000000","depth":"2181764465838305757334018112124119812555864493282943258611418063143474848585055653223823407880650484047930901559027716751636353783711244581040/4198124111205588905851334460596306839515080120142379193512437396243559233611498132658587237158342003484553120273520057273700268027174746393781","edge":[21,30],"root":40}],"Q":[],"S":[16],"U":[0,40],"V":45,"centroid":["1980796796307642755044578436879088706341997/1978253520380314346315118025179813734793822800000000000000","545815891182607055843973330282347349370847/1978253520380314346315118025179813734793822800000000000000","-3026131240603224768671631192623272266253261/1978253520380314346315118025179813734793822800000000000000"],"strict":[1,2,1],"volume":"4945633800950785865787795062949534336984557/3000000000000000000000000000000000000000000","weak":[0,0,0]},"denominator":100000000000000,"faces":[[0,1,5],[0,2,3],[0,3,4],[0,4,6],[0,5,7],[0,6,1],[0,7,19],[0,12,2],[0,19,30],[0,22,12],[0,24,22],[0,25,27],[0,26,24],[0,27,26],[0,28,25],[0,29,28],[0,30,40],[0,31,29],[0,32,31],[0,34,32],[0,36,34],[0,38,36],[0,39,38],[0,40,41],[0,41,43],[0,42,39],[0,43,42],[1,6,9],[1,9,5],[2,12,3],[3,8,4],[3,12,22],[3,14,8],[3,17,14],[3,22,17],[4,8,14],[4,14,6],[5,9,13],[5,13,7],[6,13,9],[6,14,13],[7,10,19],[7,13,16],[7,16,10],[10,11,21],[10,16,11],[10,21,19],[11,15,18],[11,16,15],[11,18,21],[13,14,16],[14,17,16],[15,16,20],[15,20,23],[15,23,18],[16,17,33],[16,33,37],[16,35,20],[16,37,35],[17,22,28],[17,28,33],[18,23,35],[18,30,21],[18,35,30],[19,21,30],[20,35,23],[22,24,26],[22,26,27],[22,27,28],[25,28,27],[28,29,31],[28,31,32],[28,32,33],[30,35,40],[32,34,36],[32,36,33],[33,36,38],[33,38,37],[35,37,40],[37,38,39],[37,39,42],[37,42,44],[37,44,40],[40,43,41],[40,44,43],[42,43,44]],"points":[[-150430868514453,-95781442890126,64514429415202],[-78851597515554,-4948798641958,-50074759060063],[-75899593633794,-2000580080701,33253709238550],[-55562306923536,24867540964854,22323975163447],[-53009255792866,33055502542937,-5148518982785],[-52831372486661,3083867210373,-69427540698519],[-53140668258445,32394132904258,-13721189236769],[-38272540463039,5007927944480,-75837816778717],[-33684580170289,48266245347145,4873591440950],[-24578604545149,51399666314966,-23533933142127],[-23955314854049,5797188209026,-80064391782409],[-12828940518923,6311545567924,-81770306922882],[-10925728240404,50788600245705,32790997122241],[-2275926915675,71236637982966,-14998949852394],[349536913831,76404975702374,2065285347024],[-3388426426000,7198344493555,-82082250165251],[6454274829813,67673086603260,-22785585999449],[7471016826354,77063749089767,12982229664598],[3989008323260,4539400664908,-81870223906939],[10787530724914,-30242215028100,-51591163514860],[16022445693170,56663754482383,-32919487973053],[10000136378357,-469021934831,-81100049775399],[21770653414101,75244466610114,32778780242995],[25967066109888,43804079466750,-42353163479957],[25341603897137,69710942234130,37763637075607],[29096598171031,44840290074027,48713235260899],[32780495117645,67319790183837,41425657271583],[44782527718703,67367302292861,44202279374720],[66209984462563,62200475763654,47872598218093],[69833708857414,55254219329529,48805798142148],[72698487243797,-21849746931336,-61928465468570],[79472303605396,48281763317753,48274203475276],[88106547760078,42126181142558,46591476279356],[93027136390158,48142770011802,22195835515534],[92794106239409,33388850662431,43853792963235],[102327696356615,15649128889740,-35583071368939],[100045993391863,26144557398687,39476717876197],[106895757056771,26190782558719,-12651122297444],[106048524092348,17888185652841,33242821634854],[109741741564381,9689773668996,25872642619542],[113837076533234,-12965274214366,-20171514369025],[109535230637180,-12347984631643,-5592282106696],[112630834192759,1821872374496,16564900951490],[114352920601572,-5095335458090,5616585628874],[115083975408600,-5983784216972,-10073586760056]]}
```

## File: J87_ROTATED_CONTINUATION.json

Bytes: 17527

SHA-256: `38915abfe2bcda6825e9e6df2832bd10403b58cdd48d137e0817b7e82a3f115a`

```json
{
  "history": [
    {
      "success": false,
      "message": "Positive directional derivative for linesearch",
      "iterations": 42,
      "best_loss": 0.5306664908300558,
      "updates": 0,
      "guard_margin": 8.999209777371674e-09,
      "eps": 9.999121974857417e-10,
      "slack": 1.0060147428687429e-08,
      "maxs": 0.0,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        -0.5773502691896258,
        0.5773502691896258,
        0.5773502691896258
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169246,
        "centroid": [
          2.1571652505299497e-17,
          -2.4251667260149966e-18,
          -7.946874017450271e-18
        ],
        "P": [
          [
            0.5306664908300558,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 7,
      "best_loss": 0.5211299089563619,
      "updates": 1,
      "guard_margin": -1.5987211555015844e-15,
      "eps": 9.999121974857417e-10,
      "slack": 1.3785975473971358e-11,
      "maxs": 0.04454478403362286,
      "s": [
        3.8159642437911844e-18,
        -0.018945546997460094,
        -0.025103435814113024,
        -0.014016203460049574,
        -0.006982403001765386,
        -0.020532352111123,
        0.0003614240600121892,
        -0.014995881486919386,
        0.007430814362596953,
        0.015927513382031595,
        -0.017966808339826668,
        -0.02174117409568152,
        -0.009178811127917916,
        0.031773932513734365,
        0.03762879641221062,
        -0.027173527053947176,
        0.03293509046628109,
        0.004002574879166974,
        -0.0342140414331987,
        0.03273972958525744,
        0.028882907607700264,
        -0.04454478403362286,
        0.0017783534811537862,
        0.03291522292072314,
        -0.0017936165826414646,
        -0.0028725501044372624,
        -0.0025789687011744077,
        -0.003020702962897482,
        -0.003501067310503844,
        -0.0035554493211284125,
        -0.03179808334690596,
        -0.0036849705277789786,
        -0.003783947533617209,
        0.0023859538957872726,
        -0.0038126140844580414,
        0.034653085921400775,
        -0.0038788708167310816,
        0.007500139584001634,
        -0.00391901613446623,
        -0.003930637175438858,
        -0.004216897062413842,
        -0.003917619959528434,
        -0.0040013657406730825,
        -0.004038474193695838,
        -0.0041404422802314295
      ],
      "d": [
        0.8944271909999159,
        0.0,
        0.4472135954999579
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.648544600316925,
        "centroid": [
          -6.874868115510082e-17,
          3.8328595476578254e-17,
          7.300162890512938e-18
        ],
        "P": [
          [
            0.5211299089563618,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 10,
      "best_loss": 0.5209652977253179,
      "updates": 2,
      "guard_margin": -2.3314683517128287e-15,
      "eps": 9.999101546753764e-11,
      "slack": 6.81435182764641e-15,
      "maxs": 0.003398523379039826,
      "s": [
        9.067838630139305e-21,
        0.0020770031847774013,
        0.00021745606693030682,
        0.00024908417978252464,
        0.00021369335835213653,
        -2.9088691071201803e-05,
        0.00013566087486006434,
        3.6510036942681764e-05,
        0.00028732182269406716,
        -7.149061714594938e-05,
        3.570370380313745e-07,
        -4.038400938919155e-05,
        0.000343684649375482,
        -0.00021570813195294952,
        0.0003654892628013167,
        -9.351364598787335e-05,
        -0.00037800532739236007,
        0.0003836134836682333,
        -0.0001247079859421216,
        0.0004954163650353998,
        0.003398523379039826,
        -0.00013414423691561052,
        0.00041327668730417296,
        7.335057328604028e-06,
        0.000411695811822161,
        0.000389633851575471,
        0.00041870616260185264,
        0.00043456599609345304,
        0.00045796026029012494,
        0.00045480996261021797,
        0.0007086920056793855,
        0.00046369554403566046,
        0.0004701666318493567,
        0.00044937480574381205,
        0.0004688457923421339,
        0.0002713482487532123,
        0.00047245472159647964,
        0.0002869782652920505,
        0.0004719873208355895,
        0.0002925356679155587,
        0.0002733200691503025,
        0.00044277395919330165,
        0.0002897127846273258,
        0.00028583095398381273,
        0.0002809757391395161
      ],
      "d": [
        0.5773502691896258,
        0.5773502691896258,
        0.5773502691896258
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.648544600316925,
        "centroid": [
          -5.331530375293533e-17,
          2.1516846477592938e-17,
          2.0881096556196917e-18
        ],
        "P": [
          [
            0.5209652977253179,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 10,
      "best_loss": 0.5209652977253179,
      "updates": 0,
      "guard_margin": 8.999001543941176e-11,
      "eps": 9.998890604379085e-12,
      "slack": 9.255459049896953e-15,
      "maxs": 0.0,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        0.0,
        0.0,
        1.0
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.648544600316925,
        "centroid": [
          1.525799811350452e-17,
          -1.5400493785541559e-18,
          1.2994509169223856e-17
        ],
        "P": [
          [
            0.5209652977253179,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": false,
      "message": "Positive directional derivative for linesearch",
      "iterations": 17,
      "best_loss": 0.5209652977253179,
      "updates": 0,
      "guard_margin": 8.999001543941176e-11,
      "eps": 9.998890604379085e-12,
      "slack": 3.365052947447538e-14,
      "maxs": 0.0,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        1.0,
        0.0,
        0.0
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.648544600316925,
        "centroid": [
          1.4556480958860632e-17,
          -1.5400493785541559e-18,
          1.3054795799701065e-17
        ],
        "P": [
          [
            0.5209652977253179,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 12,
      "best_loss": 0.5207679630229957,
      "updates": 1,
      "guard_margin": -2.886579864025407e-15,
      "eps": 9.998890604379085e-12,
      "slack": 1.168203549689624e-17,
      "maxs": 0.01580262175974726,
      "s": [
        8.808966026027694e-19,
        -0.0037067518421071742,
        -0.010461524157046312,
        -0.004900689688268086,
        -0.005128919186138878,
        -0.005596655966469717,
        -0.005092154688068199,
        -0.0065744451441996895,
        -0.005883327266178809,
        -0.006523719055835502,
        -0.008027562760675804,
        -0.007901306751375304,
        -0.006287240497006438,
        -0.00683416619047752,
        -0.007080009116369951,
        -0.007728983548865495,
        -0.006830829119516192,
        -0.007177197295057517,
        -0.009454826722170961,
        -0.010411090896529529,
        -0.0069988188936184375,
        -0.006544779039472548,
        -0.00740650423413981,
        -0.007218170360584983,
        -0.007211550575355344,
        -0.005595627000887189,
        -0.007105813439705504,
        -0.0069735805622750694,
        -0.004251640851116769,
        0.008857317155574128,
        -0.012799739502945013,
        -0.011866708378978694,
        -0.010708033027383377,
        -0.005667777305597239,
        -0.01029958771871335,
        -0.01580262175974726,
        -0.010233554241235893,
        -0.00835319253696236,
        -0.010205517923158205,
        -0.010233855946016083,
        -0.005209758202254234,
        -0.010081671412084655,
        -0.010247421470448739,
        -0.010254962546851173,
        -0.010873092716972104
      ],
      "d": [
        0.0,
        1.0,
        0.0
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.648544600316925,
        "centroid": [
          -4.665089078381841e-17,
          -1.9445178630285214e-17,
          6.631529352492984e-18
        ],
        "P": [
          [
            0.5207679630229957,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 5,
      "best_loss": 0.5196998488002631,
      "updates": 1,
      "guard_margin": -2.0872192862952135e-15,
      "eps": 9.995115846095358e-13,
      "slack": 6.888238927109907e-05,
      "maxs": 0.008036343821561332,
      "s": [
        -3.08518475345839e-19,
        0.0028752666527430974,
        0.00271863375889501,
        0.003361424638375318,
        0.003517791031178891,
        0.005772148231205292,
        0.0034928342410316562,
        0.0037049855603330404,
        0.004124574689392327,
        0.004245405890695042,
        0.0035050951298756677,
        0.0035740990533689085,
        0.004541862315517077,
        0.004874881366905074,
        0.0050527034848482175,
        0.003612793871724333,
        0.005179465032726537,
        0.005148759608447389,
        0.0036464215470490085,
        0.0034369789900095355,
        0.002831304180861549,
        0.0036744363290941574,
        0.005435164747193714,
        0.004056738442881169,
        0.00540176266742546,
        0.005125140822199723,
        0.005489568867952579,
        0.005702146119967428,
        0.006054251805015703,
        0.006063425572744909,
        0.004459226414175531,
        0.0062441396548785656,
        0.0064706344174898164,
        0.00521773318655601,
        0.006759908513339922,
        0.007270589099815421,
        0.008036343821561332,
        0.00702478246419542,
        0.0033988056311986987,
        0.005646703854823802,
        0.005554069540600078,
        0.005940273202273373,
        0.005901631200873821,
        0.005992917079335897,
        0.005777182774287012
      ],
      "d": [
        -0.5773502691896258,
        0.5773502691896258,
        0.5773502691896258
      ],
      "reported": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169255,
        "centroid": [
          8.383129997994434e-17,
          -8.269133460364803e-17,
          -1.790512925173105e-17
        ],
        "P": [
          [
            0.5196998488002631,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    }
  ],
  "points": [
    [
      -1.5043086851445278,
      -0.957814428901264,
      0.6451442941520232
    ],
    [
      -0.7885159751555371,
      -0.04948798641957904,
      -0.5007475906006323
    ],
    [
      -0.7589959363379383,
      -0.020005800807005127,
      0.33253709238549645
    ],
    [
      -0.5556230692353614,
      0.24867540964854287,
      0.2232397516344704
    ],
    [
      -0.5300925579286614,
      0.33055502542936976,
      -0.05148518982785341
    ],
    [
      -0.5283137248666097,
      0.03083867210373476,
      -0.6942754069851947
    ],
    [
      -0.5314066825844466,
      0.32394132904258116,
      -0.13721189236768527
    ],
    [
      -0.3827254046303856,
      0.050079279444795254,
      -0.7583781677871743
    ],
    [
      -0.3368458017028852,
      0.4826624534714471,
      0.048735914409502715
    ],
    [
      -0.24578604545148935,
      0.5139966631496589,
      -0.2353393314212665
    ],
    [
      -0.23955314854049167,
      0.057971882090259184,
      -0.8006439178240904
    ],
    [
      -0.12828940518923299,
      0.06311545567924183,
      -0.817703069228816
    ],
    [
      -0.1092572824040428,
      0.507886002457049,
      0.3279099712224113
    ],
    [
      -0.02275926915674692,
      0.7123663798296593,
      -0.14998949852393592
    ],
    [
      0.0034953691383053528,
      0.7640497570237429,
      0.020652853470240512
    ],
    [
      -0.03388426426000054,
      0.07198344493555317,
      -0.8208225016525053
    ],
    [
      0.06454274829812821,
      0.6767308660325977,
      -0.22785585999448815
    ],
    [
      0.07471016826354332,
      0.770637490897669,
      0.12982229664598366
    ],
    [
      0.039890083232600286,
      0.04539400664907887,
      -0.8187022390693882
    ],
    [
      0.10787530724914401,
      -0.3024221502809982,
      -0.5159116351485954
    ],
    [
      0.1602244569316955,
      0.5666375448238317,
      -0.32919487973053013
    ],
    [
      0.10000136378356503,
      -0.004690219348307345,
      -0.8110004977539933
    ],
    [
      0.2177065341410082,
      0.7524446661011435,
      0.3277878024299469
    ],
    [
      0.2596706610988846,
      0.43804079466750356,
      -0.42353163479956507
    ],
    [
      0.2534160389713726,
      0.697109422341297,
      0.37763637075606804
    ],
    [
      0.29096598171031474,
      0.4484029007402731,
      0.48713235260898824
    ],
    [
      0.3278049511764463,
      0.6731979018383676,
      0.41425657271582605
    ],
    [
      0.44782527718702625,
      0.6736730229286079,
      0.44202279374719544
    ],
    [
      0.6620998446256259,
      0.6220047576365435,
      0.47872598218092965
    ],
    [
      0.6983370885741405,
      0.552542193295289,
      0.48805798142148205
    ],
    [
      0.7269848724379679,
      -0.21849746931335573,
      -0.6192846546857007
    ],
    [
      0.7947230360539629,
      0.4828176331775301,
      0.4827420347527565
    ],
    [
      0.8810654776007849,
      0.4212618114255803,
      0.4659147627935586
    ],
    [
      0.9302713639015822,
      0.4814277001180198,
      0.22195835515533632
    ],
    [
      0.9279410623940869,
      0.33388850662431385,
      0.4385379296323501
    ],
    [
      1.0232769635661456,
      0.15649128889739614,
      -0.35583071368938535
    ],
    [
      1.0004599339186266,
      0.2614455739868726,
      0.3947671787619655
    ],
    [
      1.0689575705677146,
      0.2619078255871934,
      -0.12651122297444417
    ],
    [
      1.0604852409234808,
      0.17888185652841213,
      0.3324282163485405
    ],
    [
      1.0974174156438068,
      0.09689773668995517,
      0.2587264261954246
    ],
    [
      1.1383707653323372,
      -0.129652742143656,
      -0.20171514369024987
    ],
    [
      1.095352306371804,
      -0.12347984631642578,
      -0.05592282106695709
    ],
    [
      1.1263083419275888,
      0.018218723744961928,
      0.16564900951490108
    ],
    [
      1.143529206015719,
      -0.0509533545809042,
      0.05616585628873762
    ],
    [
      1.1508397540860031,
      -0.05983784216971587,
      -0.10073586760055896
    ]
  ]
}
```

## File: J87_TANGENT_DIAGNOSTIC.json

Bytes: 15287

SHA-256: `a34278c260343baa1e43daf9b8ce46ec77d81724f6349f4c7b4aa4cac460a6b0`

```json
[
  {
    "direction": [
      1,
      0,
      0
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.0024140287686502944,
    "alpha": 0.00390625,
    "loss": 0.5306570609344476,
    "drop": 9.429895608148442e-06,
    "s": [
      3.4367473046030185e-21,
      1.0882731307471506e-05,
      7.338337471151337e-06,
      8.883476825876858e-06,
      1.5907519936839336e-05,
      5.80232278384628e-06,
      3.906249999999994e-05,
      1.6206791258278476e-05,
      2.2293816234016068e-05,
      3.9062500000000014e-05,
      1.727032630928473e-05,
      -3.906249999999999e-05,
      7.484462863814923e-06,
      3.9062500000000014e-05,
      3.9062500000000014e-05,
      2.3155249831257594e-05,
      8.03706437806411e-06,
      7.944587836452033e-06,
      1.9082286120354973e-05,
      3.90625e-05,
      2.1247598482760466e-05,
      1.7921273524467883e-05,
      6.747748736897676e-06,
      1.2883513137949551e-05,
      3.3168973083691098e-06,
      -3.90625e-05,
      -1.9873051330384882e-06,
      -1.37962706992468e-05,
      2.019641212718385e-06,
      2.416657724013755e-05,
      2.8579854820259562e-05,
      2.400961163173589e-05,
      2.4174517591881904e-05,
      1.726247080000831e-05,
      2.407797934146527e-05,
      3.906249999999998e-05,
      2.4332501158077226e-05,
      3.466519656556879e-05,
      3.233658399110119e-06,
      5.0679777388132185e-06,
      5.180748531007991e-06,
      4.354177691977778e-06,
      5.1544695121368635e-06,
      5.314952147742327e-06,
      5.29296513333166e-06
    ],
    "direction_normalized": [
      1.0,
      0.0,
      0.0
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.6485446003169253,
      "centroid": [
        8.768964433048572e-18,
        -3.3346727558052526e-17,
        -7.239876260035727e-17
      ],
      "P": [
        [
          0.5306570609344479,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      0,
      1,
      0
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.00042261820318133334,
    "alpha": 0.0078125,
    "loss": 0.5306631894824487,
    "drop": 3.3013476070653525e-06,
    "s": [
      4.324906092218886e-21,
      -7.812500000000064e-05,
      1.4655736694603574e-05,
      1.8144179319114927e-05,
      2.1002817562106678e-05,
      -6.576834814727726e-06,
      -7.812500000000006e-05,
      6.942298435920684e-05,
      2.2590856963961184e-05,
      -2.0778657951902176e-05,
      6.256129679525517e-05,
      3.5324826350608853e-05,
      2.4995944427435925e-05,
      3.559720866075387e-05,
      2.78704226963537e-05,
      2.8457352537854126e-06,
      4.166671005424815e-05,
      7.8125e-05,
      -1.3857773943992276e-05,
      -1.8060491147053667e-05,
      3.501629423474508e-05,
      1.6714495159543203e-05,
      3.0205584098510918e-05,
      2.92854149884547e-05,
      3.0635823096569574e-05,
      3.414466698492558e-05,
      3.201065166287477e-05,
      3.4883499431788085e-05,
      5.082318662804563e-05,
      7.812499999999996e-05,
      -1.5855290902417497e-05,
      2.019248758210559e-05,
      2.5052437594088393e-05,
      5.5262171031093145e-05,
      2.643053328677131e-05,
      9.606590518565783e-06,
      2.7436469850343158e-05,
      -7.812499999999997e-05,
      2.8064330309939344e-05,
      2.843645562495051e-05,
      5.189805775742001e-05,
      7.812499999999999e-05,
      3.162723915637817e-05,
      7.30102799886386e-05,
      -7.8125e-05
    ],
    "direction_normalized": [
      0.0,
      1.0,
      0.0
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.6485446003169253,
      "centroid": [
        6.261040605196681e-17,
        2.975419244188794e-17,
        -9.618457862500153e-18
      ],
      "P": [
        [
          0.530663189482449,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      0,
      0,
      1
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -1.3402907120987868e-07,
    "alpha": 0.0078125,
    "loss": 0.530666490089325,
    "drop": 7.407308100226828e-10,
    "s": [
      1.563253559530233e-21,
      3.6761635336192084e-06,
      2.7849047823095477e-08,
      -1.6207502879067606e-08,
      -2.802893962532174e-07,
      2.9770949585512117e-06,
      2.5277692648587877e-06,
      2.7548705870033947e-06,
      3.307449123578372e-07,
      -1.9740009704032064e-07,
      2.6441277136701715e-06,
      2.6038866536221016e-06,
      2.0268293896501336e-07,
      -1.317373119703413e-06,
      9.467088649009016e-07,
      2.6020521315263773e-06,
      -1.1030694574329665e-06,
      -5.797493540952617e-08,
      2.6159074780868637e-06,
      -2.327750169653023e-07,
      -4.5835736010910074e-07,
      2.64939232115044e-06,
      2.801261571896708e-07,
      1.356799534638303e-07,
      3.075766173389161e-07,
      3.3547147093907934e-07,
      3.3348483780017277e-07,
      3.6269529283377276e-07,
      4.0235254652346236e-07,
      4.032329284808484e-07,
      -1.3213925251141246e-05,
      4.1089794276701317e-07,
      4.1169037587314765e-07,
      -7.812500000000006e-05,
      3.998117768377092e-07,
      1.492360142345704e-06,
      3.8443719308412054e-07,
      7.261081040561765e-05,
      3.5422510206085226e-07,
      3.0100833023657164e-07,
      7.782627740865636e-07,
      -5.046544235290271e-07,
      2.0559123725067584e-07,
      1.5178351577507068e-08,
      7.812499999999999e-05
    ],
    "direction_normalized": [
      0.0,
      0.0,
      1.0
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.648544600316925,
      "centroid": [
        -8.663736859851992e-17,
        4.357627262948076e-17,
        -1.3361709554857764e-17
      ],
      "P": [
        [
          0.530666490089325,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      1,
      1,
      1
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.0021152066020993544,
    "alpha": 0.03125,
    "loss": 0.5306003896766054,
    "drop": 6.610115345040413e-05,
    "s": [
      6.542330339659233e-21,
      -0.00020931555667487998,
      -6.859868284410218e-05,
      -8.258324066577833e-05,
      -9.409699335184748e-05,
      -0.00020087121806475756,
      -0.0001305712170085396,
      -0.00019094499100127588,
      -0.00018310658272473044,
      -0.00016252037122538662,
      -0.00019359945115553063,
      -0.00019669221497369325,
      -0.0001388390149806113,
      -0.00014747658916222078,
      -0.0003125,
      -0.00020094146958363017,
      -0.00014743165060764903,
      -0.00013693214924536887,
      -0.00020379977719314857,
      -0.00019935819469213656,
      -0.00013941853650860456,
      -0.00020527808582040448,
      -0.00017147176617262559,
      -0.00018611599676784783,
      -0.00017460491585495833,
      -0.00016977845640058514,
      -0.0001800327506922268,
      -0.0001885307017298996,
      -0.0001995767033207382,
      -0.00019743526314946973,
      -0.00026572435326437945,
      -0.00019945800401060097,
      -0.00019889989363611448,
      -0.0003125,
      -0.00019278411755329627,
      -0.00031249999999999995,
      -0.00018485367867877064,
      -0.00015471202523835223,
      -0.00023257789016029398,
      -0.0002533340408265409,
      -0.0003125,
      -0.00026544210481199324,
      -0.00026338522520423567,
      -0.0002746870875443986,
      -0.0002900111769687371
    ],
    "direction_normalized": [
      0.5773502691896258,
      0.5773502691896258,
      0.5773502691896258
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.648544600316925,
      "centroid": [
        2.718378974245058e-17,
        -1.2221744178561451e-18,
        -7.004758401174615e-17
      ],
      "P": [
        [
          0.5306003896766056,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      1,
      2,
      3
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.0019856649110074824,
    "alpha": 0.03125,
    "loss": 0.5306044568634065,
    "drop": 6.203396664927752e-05,
    "s": [
      -6.72849693755077e-20,
      -0.00019571310616848788,
      -6.835904736194935e-05,
      -8.449530546717033e-05,
      -0.0001983395697497177,
      -0.000191527110906792,
      -0.00031249999999999995,
      -0.00019094496800230298,
      -0.00020119899982295496,
      -0.00010042619989285732,
      -0.00019213531257177753,
      -0.0001944945374908465,
      -0.00011859551562663359,
      -6.894088207822631e-05,
      -0.00031249999999999984,
      -0.00019830181640171344,
      -7.520154142056841e-05,
      -0.00012837130938592658,
      -0.00019989953818128032,
      -9.160029720051428e-05,
      -9.690199703618117e-05,
      -0.00019991008729364847,
      -0.00014279602534841265,
      -0.0001169182593816752,
      -0.00014288983316352298,
      -0.00013564317165730454,
      -0.00014565750797815188,
      -0.0001513277853620257,
      -0.0001591406064952955,
      -0.00015754491920705422,
      -8.425190902440497e-05,
      -0.00015976324758318163,
      -0.00016061304669074642,
      -0.0003125,
      -0.00015800957597663005,
      -1.4503395792864555e-05,
      -0.00015572084272165326,
      0.00016601586646652954,
      -0.00014927321828959685,
      -0.00017352350934085787,
      -0.00031249999999999995,
      -0.0001905850922342721,
      -0.00018667456894845344,
      -0.00020408329128929187,
      -0.0002388097655731208
    ],
    "direction_normalized": [
      0.2672612419124244,
      0.5345224838248488,
      0.8017837257372732
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.648544600316926,
      "centroid": [
        -9.242488512433193e-17,
        9.47596219046311e-18,
        3.712560316841938e-17
      ],
      "P": [
        [
          0.5306044568634063,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      2,
      0,
      1
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.0032554480963079995,
    "alpha": 0.015625,
    "loss": 0.5306156213008557,
    "drop": 5.086952920008159e-05,
    "s": [
      -1.2375655423821079e-20,
      -9.184849859275445e-05,
      -0.00015625000000000014,
      -0.00015624999999999984,
      -0.00015625,
      -8.0552093275457e-05,
      -3.5133876819004295e-05,
      -8.782021568206213e-05,
      -0.00014498316104546248,
      3.114645475681064e-06,
      -9.378501905351941e-05,
      -0.00010154424855576294,
      -0.00015296917077980282,
      4.2907604353071664e-05,
      5.917462454169416e-05,
      -0.00011319125598778416,
      4.7492083980463255e-05,
      -1.61694662427241e-05,
      -0.0001293400342296,
      -9.693551707101711e-05,
      4.207623264583826e-05,
      -0.00015625,
      -4.0583562033125864e-05,
      6.298636022600424e-05,
      -7.008138267187129e-05,
      -7.554790968710593e-05,
      -7.725694639366559e-05,
      -8.285072996842741e-05,
      -8.977030827632266e-05,
      -8.979430105148947e-05,
      -0.00015625,
      -9.208818923909768e-05,
      -9.387526848498192e-05,
      1.0887091809524656e-05,
      -9.413666487679438e-05,
      0.00015624999999999998,
      -9.551768712023425e-05,
      -2.5513353419284966e-06,
      -9.758330269474108e-05,
      -0.00010424514073826089,
      -0.00011244672967382847,
      -0.00010681318268120349,
      -0.00010558763557834792,
      -0.00010686923294871499,
      -0.00010983858802197279
    ],
    "direction_normalized": [
      0.8944271909999159,
      0.0,
      0.4472135954999579
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.6485446003169253,
      "centroid": [
        3.0866754804330974e-17,
        6.650437432051744e-17,
        4.9654261102137545e-17
      ],
      "P": [
        [
          0.5306156213008558,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  },
  {
    "direction": [
      -1,
      1,
      1
    ],
    "trust": 0.01,
    "initial": 0.5306664908300558,
    "lp_success": true,
    "message": "Optimization terminated successfully. (HiGHS Status 7: Optimal)",
    "predicted": -0.004243259762942888,
    "alpha": 0.015625,
    "loss": 0.5306001927438758,
    "drop": 6.629808617997224e-05,
    "s": [
      -1.7049003637240767e-23,
      -0.00015625000000000008,
      -1.884419986798878e-05,
      -2.3358626479565618e-05,
      -6.297527757441541e-05,
      -7.352835229383739e-05,
      -0.00015625000000000017,
      -8.456296304529306e-05,
      -8.54725905972881e-05,
      -0.00015624999999999992,
      -7.335534177402579e-05,
      -6.805253309554573e-05,
      -3.0404226385927995e-05,
      -0.00012747666072384197,
      -0.00015624999999999992,
      -6.50495377579601e-05,
      4.248277734984401e-05,
      0.00015625000000000003,
      -6.247836196768553e-05,
      -0.00012269445082599244,
      -9.611863828199516e-05,
      -6.023878048824992e-05,
      -3.5790535227151846e-05,
      -3.717811502410461e-05,
      -3.4815779506567867e-05,
      -2.848725248617358e-05,
      -3.4299081232716623e-05,
      -3.3950550293947175e-05,
      -3.0017025819969285e-05,
      -2.5252252940821664e-05,
      -0.00015624999999999995,
      -1.8210086446950072e-05,
      -4.565658438766179e-06,
      0.00015624999999999995,
      2.6887226860506894e-05,
      0.00013983227397064543,
      0.0001562500000000001,
      -0.00015625000000000003,
      0.00015624999999999995,
      0.00010847907994146426,
      2.4645697522139937e-05,
      0.00015624999999999816,
      6.984758362535357e-05,
      4.673888807995704e-05,
      3.4045494910698154e-05
    ],
    "direction_normalized": [
      -0.5773502691896258,
      0.5773502691896258,
      0.5773502691896258
    ],
    "actual_hull": {
      "V": 45,
      "E": 129,
      "F": 86,
      "volume": 1.648544600316925,
      "centroid": [
        -2.034399748467269e-17,
        4.419284044117949e-17,
        -6.209522939152522e-18
      ],
      "P": [
        [
          0.5306001927438758,
          40,
          [
            21,
            30
          ]
        ]
      ],
      "Q": []
    }
  }
]
```

## File: J87_ROOT_TRIAL.json

Bytes: 45132

SHA-256: `7ff2979abf04f8ea7ed4344352a554627bc8a4339d0b8de540e5dd2b81487289`

```json
[
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 46,
      "target_score": -0.01125059722665911,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        1.0,
        0.0,
        0.0
      ],
      "guard_slack": 8.892886427247504e-13,
      "hull_slack": 9.872571691716261e-05,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169288,
        "centroid": [
          -3.1217513381652854e-17,
          4.4760082827942214e-17,
          5.989750768049228e-17
        ],
        "P": [
          [
            0.5196998488002682,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.504308685144531,
        -0.9578144289012602,
        0.6451442941520216
      ],
      [
        -0.788515975155541,
        -0.04948798641958025,
        -0.5007475906006285
      ],
      [
        -0.758995936337941,
        -0.020005800807010247,
        0.33253709238550155
      ],
      [
        -0.555623069235361,
        0.24867540964853976,
        0.22323975163447154
      ],
      [
        -0.530092557928661,
        0.33055502542936976,
        -0.051485189827848436
      ],
      [
        -0.528313724866611,
        0.030838672103729755,
        -0.6942754069851884
      ],
      [
        -0.531406682584451,
        0.3239413290425798,
        -0.13721189236768844
      ],
      [
        -0.382725404630391,
        0.05007927944479975,
        -0.7583781677871685
      ],
      [
        -0.336845801702891,
        0.48266245347144976,
        0.04873591440950156
      ],
      [
        -0.24578604545149102,
        0.5139966631496597,
        -0.23533933142126845
      ],
      [
        -0.23955314854049103,
        0.05797188209025975,
        -0.8006439178240884
      ],
      [
        -0.12828940518923101,
        0.06311545567923975,
        -0.8177030692288184
      ],
      [
        -0.109257282404041,
        0.5078860024570497,
        0.32790997122241156
      ],
      [
        -0.022759269156751017,
        0.7123663798296598,
        -0.14998949852393845
      ],
      [
        0.003495369138308982,
        0.7640497570237398,
        0.020652853470241563
      ],
      [
        -0.03388426426000102,
        0.07198344493554976,
        -0.8208225016525085
      ],
      [
        0.06454274829812899,
        0.6767308660325998,
        -0.22785585999448846
      ],
      [
        0.07471016826353899,
        0.7706374908976698,
        0.12982229664598155
      ],
      [
        0.03989008323259898,
        0.04539400664907975,
        -0.8187022390693884
      ],
      [
        0.10787530724913899,
        -0.3024221502810002,
        -0.5159116351485984
      ],
      [
        0.16022445693169898,
        0.5666375448238298,
        -0.32919487973052847
      ],
      [
        0.10000136378356898,
        -0.004690219348310247,
        -0.8110004977539884
      ],
      [
        0.21770653414100896,
        0.7524446661011398,
        0.32778780242995154
      ],
      [
        0.259670661098879,
        0.4380407946674998,
        -0.42353163479956846
      ],
      [
        0.253416038971369,
        0.6971094223412998,
        0.37763637075607154
      ],
      [
        0.290965981710309,
        0.4484029007402698,
        0.48713235260899157
      ],
      [
        0.327804951176449,
        0.6731979018383698,
        0.41425657271583155
      ],
      [
        0.447825277187029,
        0.6736730229286098,
        0.44202279374720155
      ],
      [
        0.662099844625629,
        0.6220047576365397,
        0.47872598218093154
      ],
      [
        0.698337088574139,
        0.5525421932952898,
        0.48805798142148155
      ],
      [
        0.726984872437969,
        -0.21849746931336025,
        -0.6192846546856985
      ],
      [
        0.794723036053959,
        0.4828176331775298,
        0.48274203475276156
      ],
      [
        0.881065477600779,
        0.4212618114255798,
        0.46591476279356153
      ],
      [
        0.930271363901579,
        0.4814277001180198,
        0.22195835515534154
      ],
      [
        0.927941062394089,
        0.3338885066243098,
        0.43853792963235155
      ],
      [
        1.023276963566149,
        0.15649128889739974,
        -0.35583071368938846
      ],
      [
        1.0004599339186289,
        0.2614455739868698,
        0.39476717876197154
      ],
      [
        1.0689575705677088,
        0.2619078255871898,
        -0.12651122297443845
      ],
      [
        1.0604852409234788,
        0.17888185652840974,
        0.3324282163485415
      ],
      [
        1.0974174156438088,
        0.09689773668995975,
        0.2587264261954216
      ],
      [
        1.138370765332339,
        -0.12965274214366024,
        -0.20171514369024846
      ],
      [
        1.095352306371799,
        -0.12347984631643025,
        -0.055922821066958436
      ],
      [
        1.126308341927589,
        0.018218723744959753,
        0.16564900951490155
      ],
      [
        1.143529206015719,
        -0.05095335458090025,
        0.05616585628874156
      ],
      [
        1.150839754085999,
        -0.05983784216972025,
        -0.10073586760055843
      ]
    ]
  },
  {
    "result": {
      "success": false,
      "message": "Inequality constraints incompatible",
      "iterations": 25,
      "target_score": -0.01125059722665911,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        0.0,
        1.0,
        0.0
      ],
      "guard_slack": 8.892886427247504e-13,
      "hull_slack": 0.0001168284862109719,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169288,
        "centroid": [
          -3.1217513381652854e-17,
          4.4760082827942214e-17,
          5.989750768049228e-17
        ],
        "P": [
          [
            0.5196998488002682,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.504308685144531,
        -0.9578144289012602,
        0.6451442941520216
      ],
      [
        -0.788515975155541,
        -0.04948798641958025,
        -0.5007475906006285
      ],
      [
        -0.758995936337941,
        -0.020005800807010247,
        0.33253709238550155
      ],
      [
        -0.555623069235361,
        0.24867540964853976,
        0.22323975163447154
      ],
      [
        -0.530092557928661,
        0.33055502542936976,
        -0.051485189827848436
      ],
      [
        -0.528313724866611,
        0.030838672103729755,
        -0.6942754069851884
      ],
      [
        -0.531406682584451,
        0.3239413290425798,
        -0.13721189236768844
      ],
      [
        -0.382725404630391,
        0.05007927944479975,
        -0.7583781677871685
      ],
      [
        -0.336845801702891,
        0.48266245347144976,
        0.04873591440950156
      ],
      [
        -0.24578604545149102,
        0.5139966631496597,
        -0.23533933142126845
      ],
      [
        -0.23955314854049103,
        0.05797188209025975,
        -0.8006439178240884
      ],
      [
        -0.12828940518923101,
        0.06311545567923975,
        -0.8177030692288184
      ],
      [
        -0.109257282404041,
        0.5078860024570497,
        0.32790997122241156
      ],
      [
        -0.022759269156751017,
        0.7123663798296598,
        -0.14998949852393845
      ],
      [
        0.003495369138308982,
        0.7640497570237398,
        0.020652853470241563
      ],
      [
        -0.03388426426000102,
        0.07198344493554976,
        -0.8208225016525085
      ],
      [
        0.06454274829812899,
        0.6767308660325998,
        -0.22785585999448846
      ],
      [
        0.07471016826353899,
        0.7706374908976698,
        0.12982229664598155
      ],
      [
        0.03989008323259898,
        0.04539400664907975,
        -0.8187022390693884
      ],
      [
        0.10787530724913899,
        -0.3024221502810002,
        -0.5159116351485984
      ],
      [
        0.16022445693169898,
        0.5666375448238298,
        -0.32919487973052847
      ],
      [
        0.10000136378356898,
        -0.004690219348310247,
        -0.8110004977539884
      ],
      [
        0.21770653414100896,
        0.7524446661011398,
        0.32778780242995154
      ],
      [
        0.259670661098879,
        0.4380407946674998,
        -0.42353163479956846
      ],
      [
        0.253416038971369,
        0.6971094223412998,
        0.37763637075607154
      ],
      [
        0.290965981710309,
        0.4484029007402698,
        0.48713235260899157
      ],
      [
        0.327804951176449,
        0.6731979018383698,
        0.41425657271583155
      ],
      [
        0.447825277187029,
        0.6736730229286098,
        0.44202279374720155
      ],
      [
        0.662099844625629,
        0.6220047576365397,
        0.47872598218093154
      ],
      [
        0.698337088574139,
        0.5525421932952898,
        0.48805798142148155
      ],
      [
        0.726984872437969,
        -0.21849746931336025,
        -0.6192846546856985
      ],
      [
        0.794723036053959,
        0.4828176331775298,
        0.48274203475276156
      ],
      [
        0.881065477600779,
        0.4212618114255798,
        0.46591476279356153
      ],
      [
        0.930271363901579,
        0.4814277001180198,
        0.22195835515534154
      ],
      [
        0.927941062394089,
        0.3338885066243098,
        0.43853792963235155
      ],
      [
        1.023276963566149,
        0.15649128889739974,
        -0.35583071368938846
      ],
      [
        1.0004599339186289,
        0.2614455739868698,
        0.39476717876197154
      ],
      [
        1.0689575705677088,
        0.2619078255871898,
        -0.12651122297443845
      ],
      [
        1.0604852409234788,
        0.17888185652840974,
        0.3324282163485415
      ],
      [
        1.0974174156438088,
        0.09689773668995975,
        0.2587264261954216
      ],
      [
        1.138370765332339,
        -0.12965274214366024,
        -0.20171514369024846
      ],
      [
        1.095352306371799,
        -0.12347984631643025,
        -0.055922821066958436
      ],
      [
        1.126308341927589,
        0.018218723744959753,
        0.16564900951490155
      ],
      [
        1.143529206015719,
        -0.05095335458090025,
        0.05616585628874156
      ],
      [
        1.150839754085999,
        -0.05983784216972025,
        -0.10073586760055843
      ]
    ]
  },
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 76,
      "target_score": -0.007807520793679301,
      "s": [
        -3.9702238028240593e-19,
        -0.0006827490848878869,
        -0.0015414051974639601,
        -0.002437870007533101,
        0.0009970994000058774,
        0.0033954405322866844,
        0.006734659754796835,
        0.0032191146638761103,
        -0.006804537456044605,
        -0.00474986488237495,
        0.01852551602831244,
        0.026529960337311156,
        -0.0013322116043363516,
        -0.017644692362541556,
        -0.006007296636045883,
        0.03467576552104083,
        -0.015425704230110537,
        -0.003678945582400676,
        0.034766913889595005,
        -0.016455217286603367,
        -0.007402202508397123,
        0.03510478100926795,
        -0.0012926317008506052,
        -0.010265724580023828,
        -0.0010868317848127442,
        -0.0007070628536639938,
        -0.0009550792880775174,
        -0.0008709188819440606,
        -0.0007749933517672432,
        -0.0007472919074548237,
        -0.024410929827076773,
        -0.0007675299238167256,
        -0.0008223234316912525,
        -0.047033222576957044,
        -0.0009101021820386796,
        0.016837944516490035,
        -0.0010690504793911316,
        -0.029561475143440704,
        -0.0019405110533572707,
        -0.002603278423722888,
        -0.008210861978778778,
        -0.013883355815667048,
        -0.003926098087198268,
        -0.0072973222882553755,
        -0.03457949691085858
      ],
      "d": [
        0.0,
        0.0,
        1.0
      ],
      "guard_slack": -3.3306690738754696e-16,
      "hull_slack": 9.99999649059502e-11,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169286,
        "centroid": [
          1.0171998742336324e-17,
          3.3694745833989075e-17,
          2.5081978579904197e-17
        ],
        "P": [
          [
            0.5503310973157591,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.504308685144531,
        -0.9578144289012602,
        0.6441220689103295
      ],
      [
        -0.788515975155541,
        -0.04948798641958025,
        -0.5024525649272084
      ],
      [
        -0.758995936337941,
        -0.020005800807010247,
        0.3299734619463456
      ],
      [
        -0.555623069235361,
        0.24867540964853976,
        0.21977965638524646
      ],
      [
        -0.530092557928661,
        0.33055502542936976,
        -0.051510315669534554
      ],
      [
        -0.528313724866611,
        0.030838672103729755,
        -0.6919021916945938
      ],
      [
        -0.531406682584451,
        0.3239413290425798,
        -0.13149945785458358
      ],
      [
        -0.382725404630391,
        0.05007927944479975,
        -0.7561812783649844
      ],
      [
        -0.336845801702891,
        0.48266245347144976,
        0.040909151711764964
      ],
      [
        -0.24578604545149102,
        0.5139966631496597,
        -0.24111142154533538
      ],
      [
        -0.23955314854049103,
        0.05797188209025975,
        -0.7831406270374679
      ],
      [
        -0.12828940518923101,
        0.06311545567923975,
        -0.7921953341331992
      ],
      [
        -0.109257282404041,
        0.5078860024570497,
        0.32555553437638324
      ],
      [
        -0.022759269156751017,
        0.7123663798296598,
        -0.168656416128172
      ],
      [
        0.003495369138308982,
        0.7640497570237398,
        0.013623331592503687
      ],
      [
        -0.03388426426000102,
        0.07198344493554976,
        -0.7871689613731596
      ],
      [
        0.06454274829812899,
        0.6767308660325998,
        -0.244303789466291
      ],
      [
        0.07471016826353899,
        0.7706374908976698,
        0.1251211258218889
      ],
      [
        0.03989008323259898,
        0.04539400664907975,
        -0.7849575504214854
      ],
      [
        0.10787530724913899,
        -0.3024221502810002,
        -0.5333890776768937
      ],
      [
        0.16022445693169898,
        0.5666375448238298,
        -0.3376193074806176
      ],
      [
        0.10000136378356898,
        -0.004690219348310247,
        -0.7769179419864125
      ],
      [
        0.21770653414100896,
        0.7524446661011398,
        0.32547294548740896
      ],
      [
        0.259670661098879,
        0.4380407946674998,
        -0.4348195846212843
      ],
      [
        0.253416038971369,
        0.6971094223412998,
        0.3755273137295668
      ],
      [
        0.290965981710309,
        0.4484029007402698,
        0.4854030645136356
      ],
      [
        0.327804951176449,
        0.6731979018383698,
        0.41227926818606203
      ],
      [
        0.447825277187029,
        0.6736730229286098,
        0.4401296496235655
      ],
      [
        0.662099844625629,
        0.6220047576365397,
        0.4769287635874723
      ],
      [
        0.698337088574139,
        0.5525421932952898,
        0.48628846427233474
      ],
      [
        0.726984872437969,
        -0.21849746931336025,
        -0.6447178097544672
      ],
      [
        0.794723036053959,
        0.4828176331775298,
        0.48095227958725284
      ],
      [
        0.881065477600779,
        0.4212618114255798,
        0.4640702141201783
      ],
      [
        0.930271363901579,
        0.4814277001180198,
        0.1739029073366925
      ],
      [
        0.927941062394089,
        0.3338885066243098,
        0.4366056022086209
      ],
      [
        1.023276963566149,
        0.15649128889739974,
        -0.34001499441459043
      ],
      [
        1.0004599339186289,
        0.2614455739868698,
        0.3926759030408884
      ],
      [
        1.0689575705677088,
        0.2619078255871898,
        -0.15709492335957115
      ],
      [
        1.0604852409234788,
        0.17888185652840974,
        0.32946548005349224
      ],
      [
        1.0974174156438088,
        0.09689773668995975,
        0.2551009225300067
      ],
      [
        1.138370765332339,
        -0.12965274214366024,
        -0.21094823091071924
      ],
      [
        1.095352306371799,
        -0.12347984631643025,
        -0.07082840212431747
      ],
      [
        1.126308341927589,
        0.018218723744959753,
        0.1607006861860113
      ],
      [
        1.143529206015719,
        -0.05095335458090025,
        0.04784630875879419
      ],
      [
        1.150839754085999,
        -0.05983784216972025,
        -0.136337589753109
      ]
    ]
  },
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 42,
      "target_score": -0.01125059722665911,
      "s": [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "d": [
        0.5773502691896258,
        0.5773502691896258,
        0.5773502691896258
      ],
      "guard_slack": 8.892886427247504e-13,
      "hull_slack": 0.00035442726255401324,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169288,
        "centroid": [
          -3.1217513381652854e-17,
          4.4760082827942214e-17,
          5.989750768049228e-17
        ],
        "P": [
          [
            0.5196998488002682,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.504308685144531,
        -0.9578144289012602,
        0.6451442941520216
      ],
      [
        -0.788515975155541,
        -0.04948798641958025,
        -0.5007475906006285
      ],
      [
        -0.758995936337941,
        -0.020005800807010247,
        0.33253709238550155
      ],
      [
        -0.555623069235361,
        0.24867540964853976,
        0.22323975163447154
      ],
      [
        -0.530092557928661,
        0.33055502542936976,
        -0.051485189827848436
      ],
      [
        -0.528313724866611,
        0.030838672103729755,
        -0.6942754069851884
      ],
      [
        -0.531406682584451,
        0.3239413290425798,
        -0.13721189236768844
      ],
      [
        -0.382725404630391,
        0.05007927944479975,
        -0.7583781677871685
      ],
      [
        -0.336845801702891,
        0.48266245347144976,
        0.04873591440950156
      ],
      [
        -0.24578604545149102,
        0.5139966631496597,
        -0.23533933142126845
      ],
      [
        -0.23955314854049103,
        0.05797188209025975,
        -0.8006439178240884
      ],
      [
        -0.12828940518923101,
        0.06311545567923975,
        -0.8177030692288184
      ],
      [
        -0.109257282404041,
        0.5078860024570497,
        0.32790997122241156
      ],
      [
        -0.022759269156751017,
        0.7123663798296598,
        -0.14998949852393845
      ],
      [
        0.003495369138308982,
        0.7640497570237398,
        0.020652853470241563
      ],
      [
        -0.03388426426000102,
        0.07198344493554976,
        -0.8208225016525085
      ],
      [
        0.06454274829812899,
        0.6767308660325998,
        -0.22785585999448846
      ],
      [
        0.07471016826353899,
        0.7706374908976698,
        0.12982229664598155
      ],
      [
        0.03989008323259898,
        0.04539400664907975,
        -0.8187022390693884
      ],
      [
        0.10787530724913899,
        -0.3024221502810002,
        -0.5159116351485984
      ],
      [
        0.16022445693169898,
        0.5666375448238298,
        -0.32919487973052847
      ],
      [
        0.10000136378356898,
        -0.004690219348310247,
        -0.8110004977539884
      ],
      [
        0.21770653414100896,
        0.7524446661011398,
        0.32778780242995154
      ],
      [
        0.259670661098879,
        0.4380407946674998,
        -0.42353163479956846
      ],
      [
        0.253416038971369,
        0.6971094223412998,
        0.37763637075607154
      ],
      [
        0.290965981710309,
        0.4484029007402698,
        0.48713235260899157
      ],
      [
        0.327804951176449,
        0.6731979018383698,
        0.41425657271583155
      ],
      [
        0.447825277187029,
        0.6736730229286098,
        0.44202279374720155
      ],
      [
        0.662099844625629,
        0.6220047576365397,
        0.47872598218093154
      ],
      [
        0.698337088574139,
        0.5525421932952898,
        0.48805798142148155
      ],
      [
        0.726984872437969,
        -0.21849746931336025,
        -0.6192846546856985
      ],
      [
        0.794723036053959,
        0.4828176331775298,
        0.48274203475276156
      ],
      [
        0.881065477600779,
        0.4212618114255798,
        0.46591476279356153
      ],
      [
        0.930271363901579,
        0.4814277001180198,
        0.22195835515534154
      ],
      [
        0.927941062394089,
        0.3338885066243098,
        0.43853792963235155
      ],
      [
        1.023276963566149,
        0.15649128889739974,
        -0.35583071368938846
      ],
      [
        1.0004599339186289,
        0.2614455739868698,
        0.39476717876197154
      ],
      [
        1.0689575705677088,
        0.2619078255871898,
        -0.12651122297443845
      ],
      [
        1.0604852409234788,
        0.17888185652840974,
        0.3324282163485415
      ],
      [
        1.0974174156438088,
        0.09689773668995975,
        0.2587264261954216
      ],
      [
        1.138370765332339,
        -0.12965274214366024,
        -0.20171514369024846
      ],
      [
        1.095352306371799,
        -0.12347984631643025,
        -0.055922821066958436
      ],
      [
        1.126308341927589,
        0.018218723744959753,
        0.16564900951490155
      ],
      [
        1.143529206015719,
        -0.05095335458090025,
        0.05616585628874156
      ],
      [
        1.150839754085999,
        -0.05983784216972025,
        -0.10073586760055843
      ]
    ]
  },
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 13,
      "target_score": -0.008920347927808714,
      "s": [
        9.491301153599134e-19,
        0.011410032265829949,
        0.0029233902514153704,
        0.0036185498541819873,
        0.0037457190212985447,
        0.010111331679021278,
        0.0036795212938628896,
        0.002641638927076967,
        0.004419120915880617,
        0.004171757598492227,
        0.016026977317073643,
        0.0297811219431563,
        0.004879021395846252,
        0.005114173381459098,
        0.005418864218769931,
        0.030999010789391268,
        0.005037582421204636,
        0.005529869368714337,
        0.031326434220504525,
        -0.003594607306843298,
        0.010883417472576741,
        0.031285710388899955,
        0.005834166073657224,
        0.014894154814436109,
        0.005792156729927919,
        0.005459031742498342,
        0.005877587199259634,
        0.006091704842143787,
        0.0064199804757234715,
        0.006397349354051288,
        -0.0012123020784612795,
        0.006508461480706071,
        0.0066218175356355735,
        -0.0033488257394357723,
        0.006637765403564609,
        -0.06797673811958667,
        0.006745248443483837,
        0.021889855725623842,
        0.006850983969807081,
        0.007215972374881759,
        0.04200283518298168,
        0.009365095912638498,
        0.007936051575797668,
        0.021909528871540653,
        0.028546744302226933
      ],
      "d": [
        0.2672612419124244,
        0.5345224838248488,
        0.8017837257372732
      ],
      "guard_slack": -3.4194869158454897e-15,
      "hull_slack": 9.999868644185346e-11,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169288,
        "centroid": [
          -1.7362549577436136e-17,
          2.0111071866919793e-17,
          2.9354108439630034e-17
        ],
        "P": [
          [
            0.540491307170031,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.5054602033916795,
        -0.960117465395557,
        0.6416897394105765
      ],
      [
        -0.7866180340090628,
        -0.0456921041266239,
        -0.4950537671611939
      ],
      [
        -0.7593661456759014,
        -0.0207462194829311,
        0.33142646437162027
      ],
      [
        -0.5558074893545587,
        0.24830656941014442,
        0.22268649127687853
      ],
      [
        -0.530242990658322,
        0.3302541599700475,
        -0.05193648801683184
      ],
      [
        -0.5267628760518357,
        0.033940369733280344,
        -0.6896228605408625
      ],
      [
        -0.5315748074009584,
        0.32360507940956507,
        -0.13771626681721053
      ],
      [
        -0.3831709151772046,
        0.0491882583511726,
        -0.7597146994276093
      ],
      [
        -0.3368162602059,
        0.48272153646543187,
        0.048824538900474716
      ],
      [
        -0.24582261458190877,
        0.5139235248888242,
        -0.2354490388125217
      ],
      [
        -0.23642127692577605,
        0.06423562531968972,
        -0.7912483029799434
      ],
      [
        -0.12148158380030608,
        0.07673109845708961,
        -0.7972796050620437
      ],
      [
        -0.10910482733361822,
        0.5081909125978953,
        0.32836733643367993
      ],
      [
        -0.02254396707461517,
        0.7127969839939314,
        -0.1493435922775309
      ],
      [
        0.00379210327202386,
        0.7646432252911696,
        0.021543055871386198
      ],
      [
        -0.026750948385520036,
        0.08625007668451172,
        -0.7994225540290655
      ],
      [
        0.06473758058510796,
        0.6771205306065577,
        -0.22727136313355153
      ],
      [
        0.07503656977148669,
        0.7712902939135652,
        0.13080150116982464
      ],
      [
        0.04711090669991052,
        0.059835653583702825,
        -0.7970397686674539
      ],
      [
        0.10576308978897621,
        -0.3066465852013258,
        -0.5222482875290868
      ],
      [
        0.16198165435452286,
        0.5701519396694775,
        -0.3239232874620569
      ],
      [
        0.10721130334907045,
        0.009729659782692687,
        -0.789370679057484
      ],
      [
        0.21811426236422954,
        0.753260122547581,
        0.3290109870996133
      ],
      [
        0.2624997731646727,
        0.44369901879908724,
        -0.4150442986021872
      ],
      [
        0.25381253972521256,
        0.6979024238489869,
        0.37882587301760223
      ],
      [
        0.2912734510663001,
        0.44901783945225193,
        0.4880547606769648
      ],
      [
        0.3282242841836233,
        0.6740365678527185,
        0.4155145717373545
      ],
      [
        0.44830183554135594,
        0.6746261396372636,
        0.44345246881018224
      ],
      [
        0.662664138333476,
        0.6231333450522337,
        0.48041886330447253
      ],
      [
        0.698895333860302,
        0.5536586838676157,
        0.4897327172799706
      ],
      [
        0.7255093528317581,
        -0.22144850852578216,
        -0.6237112135043313
      ],
      [
        0.7953109773050833,
        0.4839935156797784,
        0.4845058585061345
      ],
      [
        0.8816837145319221,
        0.4224982852878659,
        0.4677694735869907
      ],
      [
        0.9282248343283608,
        0.47733464097158324,
        0.21581876643568673
      ],
      [
        0.9285635615722206,
        0.33513350498057304,
        0.44040542716674647
      ],
      [
        1.0039578978680042,
        0.11785315750111025,
        -0.4137879107838227
      ],
      [
        1.001111159147494,
        0.2627480244445997,
        0.3967208544485664
      ],
      [
        1.0736563623470745,
        0.27130540914592105,
        -0.1124148476363415
      ],
      [
        1.0611647251604233,
        0.1802408250022985,
        0.33446666905937467
      ],
      [
        1.098194447135177,
        0.0984517996726963,
        0.2610575206695264
      ],
      [
        1.1484449769800371,
        -0.10950431884826387,
        -0.1714925087471539
      ],
      [
        1.0967037152888912,
        -0.12077702848224553,
        -0.05186859431568135
      ],
      [
        1.1272778226804694,
        0.02015768525072048,
        0.16855745177354264
      ],
      [
        1.1482332556644947,
        -0.04154525528334885,
        0.07027800523506866
      ],
      [
        1.1573176741736202,
        -0.0468820019944778,
        -0.08130210733769476
      ]
    ]
  },
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 48,
      "target_score": -0.010661866578870471,
      "s": [
        6.903661442354717e-18,
        0.031217489153978477,
        0.016379496667274347,
        0.029343188614626984,
        0.027039602484919087,
        0.03231020031050107,
        0.027096142990350888,
        0.023465121810717665,
        0.02299591393894617,
        0.021349750958864874,
        0.023758290084207993,
        0.028092676299248883,
        0.02365592647559126,
        0.01792787388674333,
        0.016758966685667353,
        0.029680370226518468,
        0.01772142028577162,
        0.017206141980944716,
        0.031644137793507075,
        0.016377384559292836,
        0.008820544675740826,
        0.034285857101333195,
        0.01813469706211374,
        0.005480633054086181,
        0.02414327586499076,
        0.026173592120274796,
        0.02671272401009152,
        0.02868281566417472,
        0.03112538324654897,
        0.03120813638437213,
        -0.08093204881068652,
        0.03190763515131311,
        0.03253780571725473,
        -0.0093606121518903,
        0.03263295196517289,
        -0.05956242435709482,
        0.03311009971785199,
        0.04131067822474634,
        0.03345268032686369,
        0.03371184145557233,
        0.052918938011604064,
        0.018586943667395814,
        0.0338753689761423,
        0.021578600644209328,
        0.051303112528460704
      ],
      "d": [
        0.8944271909999159,
        0.0,
        0.4472135954999579
      ],
      "guard_slack": -1.820765760385267e-15,
      "hull_slack": 9.999976454538873e-11,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169286,
        "centroid": [
          -4.2091029278633066e-18,
          2.3410394734854313e-17,
          6.302693186253649e-19
        ],
        "P": [
          [
            0.537478737101786,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.5241875725843492,
        -0.9578144289012602,
        0.6352048504321125
      ],
      [
        -0.7804730914612957,
        -0.04948798641958025,
        -0.49672614875350585
      ],
      [
        -0.7642245565836564,
        -0.020005800807010247,
        0.3299227822626439
      ],
      [
        -0.5492566109076175,
        0.24867540964853976,
        0.22642298079834328
      ],
      [
        -0.5257864896721385,
        0.33055502542936976,
        -0.049332155699587196
      ],
      [
        -0.519293490602063,
        0.030838672103729755,
        -0.6897652898529144
      ],
      [
        -0.5270500429624775,
        0.3239413290425798,
        -0.13503357255670165
      ],
      [
        -0.38161644908257797,
        0.05007927944479975,
        -0.757823690013262
      ],
      [
        -0.3361565184338216,
        0.48266245347144976,
        0.04908055604403626
      ],
      [
        -0.2465691351126238,
        0.5139966631496597,
        -0.23573087625183484
      ],
      [
        -0.23818197531732976,
        0.05797188209025975,
        -0.7999583312125077
      ],
      [
        -0.12304143907904197,
        0.06311545567923975,
        -0.8150790861737239
      ],
      [
        -0.10797766597579542,
        0.5078860024570497,
        0.32854977943653435
      ],
      [
        -0.026602978715448478,
        0.7123663798296598,
        -0.15191135330328717
      ],
      [
        -0.001393842804786436,
        0.7640497570237398,
        0.018208247498693854
      ],
      [
        -0.027216221530276606,
        0.07198344493554976,
        -0.8174884802876463
      ],
      [
        0.060514381025042585,
        0.6767308660325998,
        -0.22987004363103167
      ],
      [
        0.07022092206368306,
        0.7706374908976698,
        0.1275776735460536
      ],
      [
        0.048314573071041755,
        0.04539400664907975,
        -0.8144899941501671
      ],
      [
        0.10264479787661464,
        -0.3024221502810002,
        -0.5185268898348606
      ],
      [
        0.14823490448929308,
        0.5666375448238298,
        -0.33518965595173145
      ],
      [
        0.11078867920192091,
        -0.004690219348310247,
        -0.8056068400448124
      ],
      [
        0.21404781285409175,
        0.7524446661011398,
        0.3259584417864929
      ],
      [
        0.24469380088652853,
        0.4380407946674998,
        -0.4310200649057437
      ],
      [
        0.2551315539450107,
        0.6971094223412998,
        0.3784941282428924
      ],
      [
        0.2944974667490059,
        0.4484029007402698,
        0.48889809512834
      ],
      [
        0.3318186504369331,
        0.6731979018383698,
        0.4162634223460736
      ],
      [
        0.45360107999168714,
        0.6736730229286098,
        0.44491069514953063
      ],
      [
        0.6700603462918175,
        0.6220047576365397,
        0.4827062330140258
      ],
      [
        0.7063716068969372,
        0.5525421932952898,
        0.49207524058288066
      ],
      [
        0.6347181599185405,
        -0.21849746931336025,
        -0.6654180109454128
      ],
      [
        0.8033832050939801,
        0.4828176331775298,
        0.4870721192727721
      ],
      [
        0.8902892883299461,
        0.4212618114255798,
        0.4705266681581451
      ],
      [
        0.9020200904287061,
        0.4814277001180198,
        0.20783271841890508
      ],
      [
        0.9372499745145157,
        0.3338885066243098,
        0.4431923856925649
      ],
      [
        0.9501238242194696,
        0.15649128889739974,
        -0.3924072833627281
      ],
      [
        1.0101956199631763,
        0.2614455739868698,
        0.39963502178424526
      ],
      [
        1.086028077010752,
        0.2619078255871898,
        -0.11797596975291684
      ],
      [
        1.0705273403798357,
        0.17888185652840974,
        0.33744926607671993
      ],
      [
        1.1076913158605328,
        0.09689773668995975,
        0.2638633763037836
      ],
      [
        1.1658240149689385,
        -0.12965274214366024,
        -0.18798851887194862
      ],
      [
        1.0920980867456833,
        -0.12347984631643025,
        -0.0575499308800162
      ],
      [
        1.1367285056051877,
        0.018218723744959753,
        0.17085909135370086
      ],
      [
        1.14295080573581,
        -0.05095335458090025,
        0.055876656148787104
      ],
      [
        1.1768477654745646,
        -0.05983784216972025,
        -0.0877318619062756
      ]
    ]
  },
  {
    "result": {
      "success": true,
      "message": "Optimization terminated successfully",
      "iterations": 25,
      "target_score": -0.010453446735917638,
      "s": [
        1.2277269704941434e-17,
        -0.02136936520440043,
        -0.021072825236553162,
        -0.02604949440593924,
        -0.027139520045223228,
        -0.02234227362048724,
        -0.026878598067369208,
        -0.023630786746754718,
        -0.031900820550225036,
        -0.032543682062165555,
        -0.02558182874390956,
        -0.02648295031549185,
        -0.03518326375986449,
        -0.03751958240015309,
        -0.03907370628024922,
        -0.02698645496908072,
        -0.03768436547725389,
        -0.039842910292895835,
        -0.027422833411648258,
        -0.02712873541829658,
        -0.028047030433483514,
        -0.027783925860554486,
        -0.042085932761685534,
        -0.05663932832066131,
        -0.041803524373131645,
        -0.03951784984507941,
        -0.04244894366546092,
        -0.04403935634267401,
        -0.046565804894836006,
        -0.046504432414413426,
        -0.03520579174252615,
        -0.04756773653551354,
        -0.04879987123373687,
        -0.08881995466990204,
        -0.04988195277922485,
        -0.046036601011230985,
        -0.05523012917682399,
        -0.04745586693819284,
        -0.031843499051476,
        -0.0315509897108636,
        -0.05693783599550775,
        -0.03627996194480447,
        -0.0314041201360947,
        -0.03360637297150793,
        -0.06034794223802368
      ],
      "d": [
        -0.5773502691896258,
        0.5773502691896258,
        0.5773502691896258
      ],
      "guard_slack": -7.105427357601103e-16,
      "hull_slack": 1.0000003601606019e-10,
      "actual": {
        "V": 45,
        "E": 129,
        "F": 86,
        "volume": 1.6485446003169286,
        "centroid": [
          4.928158011373288e-17,
          3.268631492418849e-17,
          1.0473431894722367e-17
        ],
        "P": [
          [
            0.5366080249329884,
            40,
            [
              21,
              30
            ]
          ]
        ],
        "Q": []
      }
    },
    "points": [
      [
        -1.5222107717984148,
        -0.9399123422473764,
        0.6630463808059054
      ],
      [
        -0.7940804530562527,
        -0.04392350851886848,
        -0.4951831126999167
      ],
      [
        -0.764731621668915,
        -0.01427011547603638,
        0.3382727777164754
      ],
      [
        -0.558485473281722,
        0.25153781369490086,
        0.22610215568083264
      ],
      [
        -0.5323256353787579,
        0.33278810287946664,
        -0.04925211237775154
      ],
      [
        -0.5333164938313982,
        0.035841441068516944,
        -0.6892726380204012
      ],
      [
        -0.5337904034086994,
        0.3263250498668282,
        -0.13482817154344004
      ],
      [
        -0.3869842501948733,
        0.05433812500928205,
        -0.7541193222226862
      ],
      [
        -0.3363299410247324,
        0.48214659279329114,
        0.048220053731342964
      ],
      [
        -0.24489902850636192,
        0.5131096462045307,
        -0.23622634836639755
      ],
      [
        -0.24268555948271572,
        0.061104293032484436,
        -0.7975115068818637
      ],
      [
        -0.13090155334953008,
        0.06572760383953882,
        -0.8150909210685193
      ],
      [
        -0.10684630225519741,
        0.5054750223082062,
        0.32549899107356794
      ],
      [
        -0.018999414812024062,
        0.7086065254849329,
        -0.1537493528686654
      ],
      [
        0.008152497323563466,
        0.7593926288384854,
        0.015995725284987078
      ],
      [
        -0.03620571387301233,
        0.07430489454856107,
        -0.8185010520394972
      ],
      [
        0.068397740196778,
        0.6728758741339508,
        -0.23171085189313745
      ],
      [
        0.07981139659255673,
        0.765536262568652,
        0.1247210683169638
      ],
      [
        0.037820576830872595,
        0.047463513050806136,
        -0.816632732667662
      ],
      [
        0.10563600329178288,
        -0.3001828463236441,
        -0.5136723311912422
      ],
      [
        0.15851533084855654,
        0.5683466709069722,
        -0.327485753647386
      ],
      [
        0.09814033420442095,
        -0.0028291897691622094,
        -0.8091394681748404
      ],
      [
        0.22410277209618082,
        0.746048428145968,
        0.3213915644747797
      ],
      [
        0.2744693058976486,
        0.42324214986873016,
        -0.4383302795983381
      ],
      [
        0.25964922836738785,
        0.6908762329452809,
        0.3714031813600527
      ],
      [
        0.29587953630227704,
        0.44348934614830177,
        0.48221879801702355
      ],
      [
        0.33441077357463433,
        0.6665920794401845,
        0.4076507503176462
      ],
      [
        0.45534932477252593,
        0.6661489753431128,
        0.43449874616170464
      ],
      [
        0.6710825379628104,
        0.6130220642993583,
        0.46974328884375016
      ],
      [
        0.7072843484932276,
        0.5435949333762011,
        0.479110721502393
      ],
      [
        0.7294088591236667,
        -0.22092145599905785,
        -0.6217086413713961
      ],
      [
        0.8042841948935952,
        0.47325647433789364,
        0.4731808759131254
      ],
      [
        0.8913380097401123,
        0.4109892792862465,
        0.45564223065422826
      ],
      [
        0.9636495019857736,
        0.44804956203382523,
        0.18858021707114703
      ],
      [
        0.9388383346049949,
        0.3229912344134039,
        0.42764065742144564
      ],
      [
        1.0319541208986749,
        0.1478141315648739,
        -0.3645078710219143
      ],
      [
        1.0144449772123623,
        0.24746053069313642,
        0.3807821354682382
      ],
      [
        1.0784541414652178,
        0.25241125468968084,
        -0.1360077938719474
      ],
      [
        1.0609680070189043,
        0.17839909043298424,
        0.33194545025311606
      ],
      [
        1.0977313013926913,
        0.09658385094107731,
        0.25841254044653916
      ],
      [
        1.1533417536175363,
        -0.14462373042885762,
        -0.21668613197544584
      ],
      [
        1.0983964655129375,
        -0.1265240054575687,
        -0.0589669802080969
      ],
      [
        1.126537432487943,
        0.017989633184605905,
        0.16541991895454772
      ],
      [
        1.1450297678434223,
        -0.05245391640860354,
        0.054665294461038266
      ],
      [
        1.167779568128278,
        -0.07677765621199943,
        -0.11767568164283762
      ]
    ]
  }
]
```
