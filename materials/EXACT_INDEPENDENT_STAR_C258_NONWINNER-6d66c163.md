# material-6d66c163f4ee

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Exact independent-star finite moment-preserving deformation

Coordinator-executed theorem and rational nonwinner. This does NOT solve own110. Parent: literal J82_S1_ROBUST_G6, 45 vertices/E129/F86/C258, own121 weak000, from [internal-source-reference] returned as J84_EXACT_CENTRE_TRAP_AND_FINITE_CAPS.md. Keep this 45-point input distinct from different near-spherical 42/46-point objects mentioned under related J82/J84 labels.

## Theorem
For an independent set I of vertices of an oriented triangular boundary, move i by w_i. Each face contains at most one moving vertex. Over incident cyclic triangles (i,j,k), define A_i=sum(v_j cross v_k)/6 and B_i=sum[(v_i+v_j+v_k)(v_j cross v_k)^T+det(v_i,v_j,v_k)Identity]/24. Exact determinant expansion gives Delta V=sum A_i dot w_i and Delta M=sum[B_i w_i+(A_i dot w_i)w_i/4]. M is the unnormalized uniform first moment. Thus A_i dot w_i=0 separately and sum B_i w_i=0 are linear constraints preserving volume, first moments and own centroid for finite steps retaining the boundary complex. Independence removes mixed-vertex terms. Convexity is a separate condition: each support/probe determinant is quadratic along the line and is checked positive on the entire unit interval.

Here 15 independent vertices give a 27-dimensional chart. Freeze 0.8 of a guarded numerical step, round free tangent coordinates to denominator 10^12, and solve three dependent coordinates exactly. No optimizer is required to reproduce this rational example.

## Exact result
EXACT_INDEPENDENT_STAR_C258_NONWINNER: V45/E129/F86/C258, own121, additional weak000. Volume and all three first moments exactly equal the parent; volume=1648544600316925211/1000000000000000000. All 3612 nonincident facet/probe inequalities are strictly positive over the ENTIRE straight path. Full endpoint primal/polar/edge census is exact. Sole positive primal radial bar born at vertex40 and dying on edge21--30 decreases from 0.5678697406886946 to 0.565782267552033. Largest coordinate numerator/denominator bit length is 758. Modest bar reduction, NOT cancellation or a complexity record. Canonical own110 remains C622.

The originating guarded floating step improved root40-to44 witness from -0.03155147994390033 to -0.02689561638890964, limited by the nonstable dual witness of physical triangle [41,0,40] next to stable triangle [40,0,30], not by support convexity. The local stable-face obstacle therefore survives removal of centroid drift. This is not a general exclusion. Adjacent-vertex motion and normal-fan changes remain open.

## Recovery
Save the following three fenced files verbatim with final LF. Python3.13.5 standard library only. Run python exact_moment_chart.py.
Expected markers:
EXACT_MOMENT_CHART_PASS 15 27 3612
EXACT_CLASS [1, 2, 1] [0, 0, 0] C 258
PRIMAL_BAR 0.5678697406886946 0.565782267552033

Manifest:
J82_S1_ROBUST_G6_INPUT.json 1153 bytes SHA256 753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab
MOMENT_CHART_PARAMETERS.json 1016 bytes SHA256 30b3fbcc8053331f15eccdf4c73b9298f04e6e97f07e9f3b42d7895ae5b9f662
exact_moment_chart.py 7251 bytes SHA256 a826ae937f4194167bfec8fee16fe61e4a6f218a6029240b6a97fbb625156634
Reproduced EXACT_MOMENT_CHART_OUTPUT.json 6846 bytes SHA256 4f8b6ef04ce845693e076334fecbd3c4e7a24c8c432fdee801ede1e6af5b68a5

## J82_S1_ROBUST_G6_INPUT.json
```json
{"denominator":1000000,"name":"J82_S1_ROBUST_G6","points":[[-1772498,-1222476,446600],[-1039299,-313302,-700462],[-1003288,-275901,132016],[-809479,-13170,17208],[-790129,68868,-233475],[-774789,-231542,-897502],[-797981,62277,-350742],[-635384,-210168,-961663],[-609466,221337,-171601],[-525729,253449,-484224],[-489649,-200686,-996078],[-374946,-195685,-1011378],[-366813,246691,105757],[-316429,451849,-418573],[-295644,503340,-233141],[-275629,-186981,-1011480],[-229896,416128,-495865],[-194308,509959,-88421],[-195520,-211846,-1005706],[-187899,-558943,-768752],[-134126,305378,-589651],[-126147,-264851,-992981],[-49174,491813,93901],[-35621,178251,-677618],[-10288,436303,144281],[28080,186153,253802],[64850,412231,179729],[185379,412442,205366],[400273,357835,238447],[436566,275260,247302],[489402,-473343,-873790],[533167,226150,240322],[619725,163301,221898],[662701,219162,-3537],[666794,75353,193396],[728134,-96722,-608110],[740107,2105,147220],[797950,1378,-368423],[797491,-77809,85715],[835835,-160959,8618],[877002,-392469,-517165],[833841,-381745,-334567],[864938,-239770,-88025],[882247,-308985,-203874],[889527,-317124,-393548]]}
```

## MOMENT_CHART_PARAMETERS.json
```json
{"dependent_columns":[0,26,27],"independent_vertices":[40,42,2,8,24,25,29,17,38,32,20,18,10,1,13],"origin":"0.8 of root40-to44 guarded floating endpoint; dependent parameters recomputed exactly","tangent_parameters":["-2090606978/1000000000000","4102465395/1000000000000","1799410066/1000000000000","-3083604333/1000000000000","159636516/1000000000000","237482899/1000000000000","84541440/1000000000000","-49528340/1000000000000","91765351/1000000000000","152562665/1000000000000","122687613/1000000000000","207046634/1000000000000","153812440/1000000000000","237852360/1000000000000","2934207921/1000000000000","-907245058/1000000000000","831929892/1000000000000","-1273989227/1000000000000","4416493817/1000000000000","316679535/1000000000000","1203696092/1000000000000","794004292/1000000000000","-177929453/1000000000000","-56064176/1000000000000","2682484738/1000000000000","1542781286/1000000000000","950764907/1000000000000","-5033800147/1000000000000","-258706279/1000000000000","1095218070/1000000000000"]}
```

## exact_moment_chart.py
```python
"""Exact independent-star finite-deformation theorem and rational example.
Python standard library only. Run in a directory with the two JSON inputs.
All Fraction operations are exact; no floating tolerances enter acceptance.
"""
import json
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def matvec(B,v):return tuple(dot(r,v) for r in B)
def zero():return (R(0),R(0),R(0))

def load():
    o=json.loads((ROOT/'J82_S1_ROBUST_G6_INPUT.json').read_text());Z=o['points']
    P=[tuple(R(t,o['denominator']) for t in p) for p in Z];F=[]
    for a,b,c in combinations(range(len(Z)),3):
        n=cross(sub(Z[b],Z[a]),sub(Z[c],Z[a]));h=dot(n,Z[a])
        if n==(0,0,0):continue
        signs=[dot(n,p)-h for p in Z]
        if min(signs)<0<max(signs):continue
        assert sum(s==0 for s in signs)==3
        F.append([a,b,c] if max(signs)==0 else [a,c,b])
    return P,F

def mass(P,F):
    total=R(0);moment=zero()
    for f in F:
        a,b,c=(P[i] for i in f);d=det(a,b,c)
        total+=d/6;moment=add(moment,mul(add(a,add(b,c)),d/24))
    assert total>0
    return total,moment,mul(moment,1/total)

def coefficients(P,F,I):
    assert all(sum(i in I for i in f)<=1 for f in F)
    AA=[];BB=[];locals_=[];columns=[]
    for i in I:
        A=zero();B=[[R(0) for _ in range(3)] for _ in range(3)]
        for f in F:
            if i not in f:continue
            j=f.index(i);f=f[j:]+f[:j];a,b,c=(P[k] for k in f)
            x=cross(b,c);d=dot(a,x);s=add(a,add(b,c));A=add(A,mul(x,R(1,6)))
            for r in range(3):
                for k in range(3):B[r][k]+=(s[r]*x[k]+(d if r==k else 0))/24
        pivot=max(range(3),key=lambda j:abs(A[j]));assert A[pivot]
        local=[]
        for j in range(3):
            if j==pivot:continue
            v=[R(0)]*3;v[j]=R(1);v[pivot]=-A[j]/A[pivot]
            assert dot(A,v)==0
            local.append(tuple(v));columns.append(matvec(B,v))
        AA.append(A);BB.append(B);locals_.append(local)
    return AA,BB,locals_,columns

def solve3(cols,b):
    A=[[cols[j][i] for j in range(3)]+[b[i]] for i in range(3)]
    for j in range(3):
        r=next(r for r in range(j,3) if A[r][j]);A[j],A[r]=A[r],A[j]
        s=A[j][j];A[j]=[x/s for x in A[j]]
        for r in range(3):
            if r!=j:
                s=A[r][j];A[r]=[x-s*y for x,y in zip(A[r],A[j])]
    return tuple(A[r][3] for r in range(3))

def construct(P,F,parameters):
    I=parameters['independent_vertices'];A,B,E,C=coefficients(P,F,I)
    J=parameters['dependent_columns'];u=[R(x) for x in parameters['tangent_parameters']]
    assert len(u)==2*len(I) and len(set(J))==3
    b=zero()
    for j,x in enumerate(u):
        if j not in J:b=sub(b,mul(C[j],x))
    dep=solve3([C[j] for j in J],b)
    for j,x in zip(J,dep):u[j]=x
    W=[zero() for _ in P]
    for k,i in enumerate(I):W[i]=add(mul(E[k][0],u[2*k]),mul(E[k][1],u[2*k+1]))
    assert all(dot(a,W[i])==0 for a,i in zip(A,I))
    total=zero()
    for i,b in zip(I,B):total=add(total,matvec(b,W[i]))
    assert total==zero()
    return [add(p,w) for p,w in zip(P,W)],W

def positive_quadratic_on_unit_interval(c,b,a):
    if c<=0 or a+b+c<=0:return False
    if a>0 and 0<-b<2*a:return 4*a*c-b*b>0
    return True

def hull_path_certificate(P,Q,F):
    # A support determinant is at most quadratic: one moving face vertex,
    # and at most one independently moving probe vertex.
    checks=0;H=[mul(add(p,q),R(1,2)) for p,q in zip(P,Q)]
    for f in F:
        for j in range(len(P)):
            if j in f:continue
            vals=[]
            for Z in (P,H,Q):
                a,b,c=(Z[i] for i in f)
                vals.append(-det(sub(b,a),sub(c,a),sub(Z[j],a)))
            c,m,e=vals;qa=2*(e+c-2*m);qb=e-c-qa
            assert positive_quadratic_on_unit_interval(c,qb,qa),(f,j)
            checks+=1
    return checks

def census(P,F):
    V,M,g=mass(P,F);X=[sub(p,g) for p in P]
    planes=[];D=[];edges={}
    for i,f in enumerate(F):
        a,b,c=(P[j] for j in f);n=cross(sub(b,a),sub(c,a));h=dot(n,sub(a,g))
        assert h>0;planes.append(n);D.append(mul(n,1/h))
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(i)
    def roots(Z):
        st=[];wk=[]
        for i,p in enumerate(Z):
            mx=max(dot(p,sub(q,p)) for j,q in enumerate(Z) if i!=j)
            if mx<0:st.append(i)
            elif mx==0:wk.append(i)
        return st,wk
    U,WU=roots(X);S,WS=roots(D);H=[];WH=[]
    for (a,b),(i,j) in edges.items():
        d=sub(X[b],X[a]);t=-dot(X[a],d)/dot(d,d);r=add(X[a],mul(d,t))
        n,m=planes[i],planes[j];nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);den=nn*mm-nm*nm
        assert den>0
        x=(dot(r,n)*mm-dot(r,m)*nm)/den;y=(dot(r,m)*nn-dot(r,n)*nm)/den
        if 0<t<1 and x>0 and y>0:H.append([a,b])
        elif 0<=t<=1 and x>=0 and y>=0:WH.append([a,b])
    return {'V':len(P),'E':len(edges),'F':len(F),'C':2*len(edges),
        'strict':[len(S),len(U),len(H)],'weak':[len(WS),len(WU),len(WH)],'S':S,'U':U,'H':H,
        'volume':str(V),'first_moment':[str(x) for x in M],'centroid':[str(x) for x in g]}

def primal_bar(P,F,g):
    X=[sub(p,g) for p in P];rr=[dot(p,p) for p in X];edges=set()
    for f in F:
        for a,b in zip(f,f[1:]+f[:1]):edges.add(tuple(sorted((a,b))))
    parent=list(range(len(P)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    events=[]
    for a,b in edges:
        d=sub(X[b],X[a]);t=max(R(0),min(R(1),-dot(X[a],d)/dot(d,d)))
        q=add(X[a],mul(d,t));events.append((dot(q,q),a,b))
    bars=[]
    for level,a,b in sorted(events,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (rr[i],-i)<(rr[j],-j):i,j=j,i
        if rr[j]>level:bars.append((1-level/rr[j],j,a,b))
        parent[j]=i
    return sorted(bars,reverse=True)

if __name__=='__main__':
    P,F=load();par=json.loads((ROOT/'MOMENT_CHART_PARAMETERS.json').read_text());Q,W=construct(P,F,par)
    assert mass(P,F)==mass(Q,F)
    checks=hull_path_certificate(P,Q,F)
    old=census(P,F);new=census(Q,F)
    assert old['strict']==new['strict']==[1,2,1]
    assert old['weak']==new['weak']==[0,0,0]
    v,m,g=mass(P,F);a=primal_bar(P,F,g);b=primal_bar(Q,F,g)
    assert len(a)==len(b)==1 and b[0][0]<a[0][0]
    out={'name':'EXACT_INDEPENDENT_STAR_C258_NONWINNER','census':new,
      'identical_volume_and_first_moment':True,'strict_hull_entire_path_checks':checks,
      'before_bar':[str(x) for x in a[0]],'after_bar':[str(x) for x in b[0]],
      'points':[[str(x) for x in p] for p in Q]}
    (ROOT/'EXACT_MOMENT_CHART_OUTPUT.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('EXACT_MOMENT_CHART_PASS',len(par['independent_vertices']),27,checks)
    print('EXACT_CLASS',new['strict'],new['weak'],'C',new['C'])
    print('PRIMAL_BAR',float(a[0][0]),float(b[0][0]))
```
