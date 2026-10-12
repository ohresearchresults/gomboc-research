# material-fb374f81916b

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact rational linear forms for the H5 paired-arrow reciprocal cone.
Requires h5_reference_core.py; standard library only. Python>=3.11.
An exact witness is a list of row labels; its positive dual is reconstructed
by solving a rational linear system, not by importing numerical weights.
"""
from h5_reference_core import *

THETA=(Q(3,20),Q(3,20),Q(3,20),Q(9,20),Q(13,100))
B0=body(THETA)
W9=((Q(223142,10**6),Q(-130077,10**6)),(Q(-130077,10**6),Q(219126,10**6)))
C=aligned_reference(B0,9,W9);CI=inv(C)
K=Q(4);LOW=Q(1,21);UP=Q(16,21);SUM=Q(17,21)
BASIS=(((1,0,0),(0,0,0),(0,0,0)),((0,0,0),(0,1,0),(0,0,0)),((0,0,0),(0,0,0),(0,0,1)),
       ((0,1,0),(1,0,0),(0,0,0)),((0,0,1),(0,0,0),(1,0,0)),((0,0,0),(0,0,1),(0,1,0)))
Z=(Q(0),)*6

def matlin(a,b):return tuple(dot(a,mv(e,b)) for e in BASIS)
def traceprod(A,B):return sum((A[i][j]*B[j][i] for i in range(3) for j in range(3)),Q(0))
E=(tuple(traceprod(C,e) for e in BASIS)+Z,Z+tuple(traceprod(CI,e) for e in BASIS))

def row(label,spoke,polar,B=B0,top=9):
    """Return exact A,b for the labelled necessary inequality A.x<=b."""
    typ=label[0]
    if typ=='psd':
        j=label[1];v=tuple(map(Q,label[2]));xx=matlin(v,v);yy=xx
        if j==0:return scale(-1,xx)+Z,-LOW*quad(v,CI)
        if j==1:return xx+Z,UP*quad(v,CI)
        if j==2:return Z+scale(-1,yy),-LOW*quad(v,C)
        if j==3:return Z+yy,UP*quad(v,C)
        if j==4:return matlin(mv(C,v),mv(C,v))+yy,SUM*quad(v,C)
        raise ValueError('unknown PSD block')
    V=B['v'];P=B['poles']
    if typ=='primal':return scale(-1,matlin(V[top],sub(V[spoke],V[top])))+Z,Q(0)
    if typ=='polar':return Z+scale(-1,matlin(P[0],sub(P[polar],P[0]))),Q(0)
    if typ=='order':
        j=label[1];return sub(matlin(V[j],V[j]),matlin(V[top],V[top]))+Z,Q(0)
    raise ValueError('unknown scalar row')

def exact_solve(A,b):
    """Full-column-rank consistent rectangular system, exact Gaussian elimination."""
    R=[list(map(Q,a))+[Q(v)] for a,v in zip(A,b)];n=len(A[0]);lead=0;pivots=[]
    for k in range(n):
        candidates=[i for i in range(lead,len(R)) if R[i][k]]
        if not candidates:raise ArithmeticError('dual support is not uniquely normalized')
        j=candidates[0];R[lead],R[j]=R[j],R[lead];d=R[lead][k];R[lead]=[x/d for x in R[lead]]
        for i in range(len(R)):
            if i!=lead and R[i][k]:
                d=R[i][k];R[i]=[x-d*y for x,y in zip(R[i],R[lead])]
        pivots.append((k,lead));lead+=1
    assert all(not any(r[:-1]) and not r[-1] for r in R[lead:])
    return tuple(R[i][-1] for k,i in pivots)

def exact_dual(labels,spoke,polar,B=B0,top=9):
    rows=[row(a,spoke,polar,B,top) for a in labels];n=len(labels)
    A=[tuple(r[0][k] for r in rows)+(E[0][k],E[1][k]) for k in range(12)]
    A.append((Q(1),)*n+(Q(0),Q(0)))
    sol=exact_solve(A,(Q(0),)*12+(Q(1),));y=sol[:n];z=sol[n:]
    assert all(t>0 for t in y)
    assert all(sum(y[i]*rows[i][0][k] for i in range(n))+z[0]*E[0][k]+z[1]*E[1][k]==0 for k in range(12))
    margin=sum(y[i]*rows[i][1] for i in range(n))+sum(z)
    assert margin<0
    return y,z,margin
