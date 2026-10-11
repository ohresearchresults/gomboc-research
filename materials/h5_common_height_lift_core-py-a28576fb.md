# material-a28576fb1844

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""Exact fixed-shear common-inverse lift for genuine H5 geometry.
Geometry formulas: preserved source [internal-source-reference].
This is a new independent executable unit, not a byte alias of that source.
Python >=3.10, SymPy for exact matrix arithmetic. No external input data.
"""
from itertools import combinations
from fractions import Fraction
import sympy as S
R=S.Rational
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
PAIRS=((0,0),(0,1),(1,1))
ELL=R(21600000000000,1085712665457541)
ELLI=R(21600000000000,1089641419857541)

def sym(a,b):return (a*b.T+b*a.T)/2

def pd(A):
    return all(A[:i,:i].det()>0 for i in range(1,A.rows+1))

def geometry(theta):
    x,r,p,q,lam=map(R,theta);s=1-lam
    b=((R(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,R(1,4)),(R(1,16),R(1,16)))
    z=tuple(S.Matrix((s*u,s*w,0)) for u,w in b)+(S.Matrix((0,0,1)),S.Matrix((lam,0,1)),S.Matrix((0,lam,1)))
    area=(31-24*x*p-24*r*q)/64
    bx=R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    D=lam+2*area*s*s
    mom=S.Matrix((3*s**3*bx/2+s*s*lam*(1-3*x*p/4)/4+lam*lam/4,
                  3*s**3*by/2+s*s*lam*(1-3*r*q/4)/4+lam*lam/4,
                  area*s*s/2+lam/2+lam*lam/4))
    dd=S.S(0);kk=S.zeros(3,1);second=S.zeros(3,3)
    ef={};poles=[];rawplanes=[]
    for f,face in enumerate(FACES):
        a,b1,c=(z[j] for j in face[:3]);n=(b1-a).cross(c-a);h=n.dot(a)
        sl=[h-n.dot(v) for v in z]
        assert all(sl[i]==0 if i in face else sl[i]>0 for i in range(10))
        rawplanes.append((n,h))
        for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
        for j in range(1,len(face)-1):
            b1,c=z[face[j]],z[face[j+1]];d=a.dot(b1.cross(c));sm=a+b1+c
            dd+=d;kk+=d*sm/4
            second+=d*(sm*sm.T+a*a.T+b1*b1.T+c*c.T)/20
    assert dd==D and kk==mom and D>0
    g=mom/D;sig=(second/D-g*g.T).applyfunc(S.factor);assert pd(sig)
    vv=tuple(v-g for v in z)
    for n,h in rawplanes:
        assert h-n.dot(g)>0
        poles.append(n/(h-n.dot(g)))
    recovered=set()
    for i,j,k in combinations(range(10),3):
        n=(z[j]-z[i]).cross(z[k]-z[i])
        if n==S.zeros(3,1):continue
        vals=[n.dot(v-z[i]) for v in z]
        if max(vals)<=0 or min(vals)>=0:recovered.add(tuple(t for t,x in enumerate(vals) if x==0))
    assert recovered=={tuple(sorted(f)) for f in FACES}
    edges=tuple(sorted(ef));dual=tuple(sorted(tuple(sorted(fs)) for fs in ef.values()))
    assert len(edges)==len(dual)==17 and all(len(fs)==2 for fs in ef.values())
    primal=tuple((i,j) for e in edges for i,j in (e,e[::-1]));polar=tuple((i,j) for e in dual for i,j in (e,e[::-1]))
    return dict(theta=tuple(map(R,theta)),raw=z,v=vv,poles=tuple(poles),g=g,Sigma=sig,volume=D/6,
                edges=edges,dual=dual,ef=ef,primal=primal,polar=polar)

def metric(K,v):
    v=S.Matrix(v);kv=K*v
    M=K.row_join(kv).col_join(kv.T.row_join(S.Matrix([[1+(v.T*K*v)[0]]])))
    N=(K.inv()+v*v.T).row_join(-v).col_join((-v.T).row_join(S.ones(1,1)))
    assert M*N==S.eye(3) and pd(K)
    return M,N

def tensor_row(A,tail=0,constant=0):
    # a,b,c,d,one coordinates, K=[[a,b],[b,c]]
    return tuple(map(S.factor,(A[0,0],2*A[0,1],A[1,1],tail,constant)))

def compile_rows(B,v):
    v=S.Matrix(v)
    yy=[a[:2,0]+a[2]*v for a in B['v']]
    qq=[q[:2,0] for q in B['poles']]
    ll=[q[2]-v.dot(q[:2,0]) for q in B['poles']]
    dp={};dq={}
    for i,j in B['primal']:
        A=sym(yy[i],yy[j]-yy[i]);c=B['v'][i][2]*(B['v'][j][2]-B['v'][i][2])
        dp[i,j]=tensor_row(A,constant=c)
    for i,j in B['polar']:
        A=sym(qq[i],qq[j]-qq[i]);adj=S.Matrix(((A[1,1],-A[0,1]),(-A[1,0],A[0,0])))
        dq[i,j]=tensor_row(adj,tail=ll[i]*(ll[j]-ll[i]))
    return dp,dq

def floor_matrices(B,v,ell=ELL,elli=ELLI):
    a,b,c,d=S.symbols('a b c d');v=S.Matrix(v);K=S.Matrix(((a,b),(b,c)))
    M=K.row_join(K*v).col_join((v.T*K).row_join(S.Matrix([[1+(v.T*K*v)[0]]])))
    J=S.Matrix(((c,-b),(-b,a)))
    W=(J+d*v*v.T).row_join(-d*v).col_join((-d*v.T).row_join(S.Matrix([[d]])))
    sig=B['Sigma'];si=sig.inv()
    # W=d*N on the determinant graph; no independent polar metric.
    F=(M-ell*S.trace(sig*M)*si).applyfunc(S.expand)
    FI=(W-elli*S.trace(si*W)*sig).applyfunc(S.expand)
    return (a,b,c,d),F,FI

def evaluate(row,x):return sum(a*b for a,b in zip(row,tuple(x)+(S.S(1),)))

def audit(B,v,K):
    M,N=metric(K,v);d=K.det();x=(K[0,0],K[0,1],K[1,1],d)
    dp,dq=compile_rows(B,v)
    for (i,j),r in dp.items():assert evaluate(r,x)==(B['v'][i].T*M*(B['v'][j]-B['v'][i]))[0]
    for (i,j),r in dq.items():assert evaluate(r,x)==d*(B['poles'][i].T*N*(B['poles'][j]-B['poles'][i]))[0]
    u=[i for i in range(10) if all(evaluate(r,x)<0 for (k,j),r in dp.items() if k==i)]
    s=[i for i in range(9) if all(evaluate(r,x)<0 for (k,j),r in dq.items() if k==i)]
    saddles=[];weak=[]
    for i,j in B['edges']:
        f,g=B['ef'][i,j];rr=[evaluate(dp[i,j],x),evaluate(dp[j,i],x),evaluate(dq[f,g],x),evaluate(dq[g,f],x)]
        if all(t<0 for t in rr):saddles.append((i,j))
        elif all(t<=0 for t in rr):weak.append((i,j))
    assert len(u)+len(s)-len(saddles)==2 or weak
    return dict(M=M,N=N,K=K,v=S.Matrix(v),determinant=d,U=u,S=s,H=saddles,weak=weak,
                counts=(len(s),len(u),len(saddles)),zero_primitives=sum(evaluate(r,x)==0 for r in (*dp.values(),*dq.values())))

def encode(x):
    if isinstance(x,S.MatrixBase):return [[encode(a) for a in row] for row in x.tolist()]
    if isinstance(x,S.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(a) for a in x]
    return x
