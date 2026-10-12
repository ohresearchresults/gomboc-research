# material-a720b725ff36

AI research material

---

"""Exact edgewise S-lemma test for a whole-root-facet stress cone.
A finite certificate, not an independent choice of primal and polar metrics.
"""
from itertools import combinations
import sympy as S
R=S.Rational

def sym(a,b):return (a*b.T+b*a.T)/2

def pd(A):
    return all(A[:i,:i].det()>0 for i in range(1,A.rows+1))

def encode(x):
    if isinstance(x,S.MatrixBase):return [[encode(a) for a in row] for row in x.tolist()]
    if isinstance(x,S.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(a) for a in x]
    return x

def nsd(A):
    return all((-A).extract(idx,idx).det()>=0 for r in range(1,A.rows+1) for idx in combinations(range(A.rows),r))

def edge_multiplier(A,p,r):
    # x=p.w, y=r.w, z=(p cross r).w. Distinct vertices on q.p=q.r=1 are independent.
    T=S.Matrix.vstack(p.T,r.T,p.cross(r).T).inv()
    U=(T.T*A*T).applyfunc(S.factor);zz=U[2,2]
    assert zz<=0,('positive edge-kernel restriction',zz)
    if zz==0:
        assert U[0,2]==U[1,2]==0
        B=U[:2,:2]
    else:B=(U[:2,:2]-U[:2,2]*U[2,:2]/zz).applyfunc(S.factor)
    lam=2*max(B[0,1],S.S(0))
    assert nsd(B-S.Matrix(((0,lam/2),(lam/2,0)))),('opposite-sign wedge violation',B)
    L=(lam*sym(p,r)-A).applyfunc(S.factor)
    assert nsd(-L)
    return lam,L

def certify(A,q,vertices):
    assert q.dot(A*q)<=0
    assert all(q.dot(p)==1 for p in vertices)
    out=[]
    for p,r in zip(vertices,vertices[1:]+vertices[:1]):
        lam,L=edge_multiplier(A,p,r)
        out.append(dict(multiplier=lam,psd=L,principal_minors=[L.extract(idx,idx).det() for k in (1,2,3) for idx in combinations(range(3),k)]))
    return out

def bevel(t=R(1,4)):
    t=R(t)
    z=tuple(map(S.Matrix,((-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,1),(1,1,-1),(1,2,3),
             (-1,-1,-1+t),(-1,-1+t,-1),(1,-1,-1+t),(1,-1+t,-1))))
    faces=((7,6,0,2,1),(2,0,5),(5,0,3),(8,3,0,6),(5,1,2),(4,1,5),(7,1,4,9),(5,3,8,9,4),(9,8,6,7))
    g=S.Matrix((1,3+t*t-t**3/3,5+t*t-t**3/3))/(12-t*t)
    # Recover the actual volume and centroid from genuine oriented facets.
    sixvol=S.S(0);sixmoment=S.zeros(3,1);edges=set()
    for face in faces:
        a,b,c=(z[i] for i in face[:3]);n=(b-a).cross(c-a);h=n.dot(a)
        assert all(h-n.dot(z[i])==0 if i in face else h-n.dot(z[i])>0 for i in range(10))
        for i,j in zip(face,face[1:]+face[:1]):edges.add(tuple(sorted((i,j))))
        for j in range(1,len(face)-1):
            b,c=z[face[j]],z[face[j+1]];d=a.dot(b.cross(c))
            sixvol+=d;sixmoment+=d*(a+b+c)/4
    assert sixvol==6*(12-t*t) and sixmoment==sixvol*g and len(edges)==17
    recovered=set()
    for i,j,k in combinations(range(10),3):
        n=(z[j]-z[i]).cross(z[k]-z[i])
        if n==S.zeros(3,1):continue
        signs=[n.dot(a-z[i]) for a in z]
        if min(signs)>=0 or max(signs)<=0:
            recovered.add(tuple(a for a,v in enumerate(signs) if v==0))
    assert recovered=={tuple(sorted(f)) for f in faces}
    q=S.Matrix((0,-1,-1))/(2-t+g[1]+g[2]);vv=tuple(p-g for p in z)
    A=17*sym(vv[0],z[3]-z[0])+25*sym(vv[1],z[5]-z[1])+18*sym(vv[2],z[5]-z[2])
    M=S.Matrix(((105,-203,-124),(-203,626,185),(-124,185,197)))/100
    assert pd(M)
    ds=[(vv[i].T*M*(z[j]-z[i]))[0] for i,j in ((0,3),(1,5),(2,5))]
    assert min(ds)>0
    cs=certify(A+5*S.eye(3),q,tuple(vv[i] for i in faces[8]))
    return dict(t=t,g=g,A=A,M=M,positive_arrows=ds,root_pole=q,certificates=cs)

def hull_gap():
    # Actual homogeneous cube [-1,1]^3, top facet z=1, actual centroid zero.
    # Both metrics have strictly interior top feet, but their average does not.
    q=S.Matrix((0,0,1))
    def root_metric(G,u):
        b=-G*u
        return G.row_join(b).col_join(b.T.row_join(S.Matrix([[1+(u.T*G*u)[0]]])))
    G1=S.Matrix(((R(9,4),R(-149,100)),(R(-149,100),1)))
    G2=S.Matrix(((1,R(-149,100)),(R(-149,100),R(9,4))))
    M1=root_metric(G1,S.Matrix((R(1,2),0)))
    M2=root_metric(G2,S.Matrix((0,R(1,2))))
    M=(M1+M2)/2
    assert all(pd(A) for A in (M1,M2,M))
    def foot(A):
        a=A.inv()*q
        return a/q.dot(a)
    assert foot(M1)==S.Matrix((R(1,2),0,1))
    assert foot(M2)==S.Matrix((0,R(1,2),1))
    assert foot(M)==S.Matrix((R(38,27),R(38,27),1))
    # General construction for any target off the line of two given feet.
    u1=S.Matrix((R(1,2),0));u2=S.Matrix((0,R(1,2)));target=S.Matrix((10,-7))
    v1=target-u1;v2=target-u2
    f=S.Matrix.hstack(v1,v2).T.inv()*S.Matrix((1,-1))
    H1=f*f.T+S.eye(2)-v1*v1.T/v1.dot(v1)
    H2=f*f.T+S.eye(2)-v2*v2.T/v2.dot(v2)
    assert pd(H1) and pd(H2) and H1*v1==f and H2*v2==-f
    N1=root_metric(H1,u1);N2=root_metric(H2,u2)
    assert foot((N1+N2)/2)==target.col_join(S.ones(1,1))
    return dict(cube_metrics=(M1,M2),cube_feet=(foot(M1),foot(M2)),
                average_metric=M,average_foot=foot(M),
                general_target=target,general_metrics=(N1,N2),
                general_average_foot=foot((N1+N2)/2))

if __name__=='__main__':
    import json
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    print(json.dumps(encode({'bevel':bevel(),'root_hull_gap':hull_gap()}),sort_keys=True,indent=2))
    print('ROOT_FACET_EDGE_LMI_AND_HULL_GAP_V1_PASS')
