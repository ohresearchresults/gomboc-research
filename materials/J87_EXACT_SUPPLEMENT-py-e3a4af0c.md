# material-e3a4af0cad9c

AI research material

---

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
