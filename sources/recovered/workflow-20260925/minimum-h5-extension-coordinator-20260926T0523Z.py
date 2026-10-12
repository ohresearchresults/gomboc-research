#!/usr/bin/env python3
"""Original-centroid H5 polynomial search and exact certificate primitives.
CPython >=3.11; NumPy for exact object and numerical arrays;
SciPy only for exploratory nonnegative stress proposals.
The inherited body and moments are literal H5_MACRO_R_HALF_TRIANGLE_ALLROOT_V1.
No globally lowered polynomial is used.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, factorial, lcm
from pathlib import Path
import numpy as np
import json, hashlib, time, sys
ZERO=(0,)*5
class P:
    def __init__(self,x=0):
        if isinstance(x,P):self.d=x.d.copy()
        elif isinstance(x,dict):self.d={k:F(v)for k,v in x.items()if v}
        else:self.d={}if not x else{ZERO:F(x)}
    def __add__(self,b):
        d=self.d.copy()
        for k,v in P(b).d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for j,w in P(b).d.items():
                z=tuple(a+c for a,c in zip(k,j));d[z]=d.get(z,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b):return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,b):return self.d==P(b).d

def var(i):
    k=[0]*5;k[i]=1;return P({tuple(k):1})
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),(0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b)))for f in FACES for a,b in zip(f,f[1:]+f[:1])}))
ARROWS=tuple(sorted([e for a,b in EDGES for e in((a,b),(b,a))]))
PAIRS=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
BOX=((F(15,16),F(1)),(F(1,4),F(1,2)),(F(0),F(1,64)))
TRI=tuple((i,j)for i in range(4)for j in range(4-i))
INDICES=tuple(product(range(4),range(4),TRI,range(5)))
FULL=((F(0),F(0)),(F(1),F(0)),(F(0),F(1)))
HALF=((F(0),F(0)),(F(1,2),F(0)),(F(0),F(1,2)))
UPPER=(((F(1,2),F(0)),(F(1),F(0)),(F(1,2),F(1,2))),
       ((F(0),F(1,2)),(F(1,2),F(1,2)),(F(0),F(1))),
       ((F(1,2),F(0)),(F(1,2),F(1,2)),(F(0),F(1,2))))

def geometry():
    x,r,p,q,l=(var(i)for i in range(5));s=1-l
    B=((P(F(1,4)),P(0)),(1-3*x/4,P(0)),(1-p,p),(q,1-q),(P(0),1-3*r/4),(P(0),P(F(1,4))),(P(F(1,16)),P(F(1,16))))
    Z=[(s*a,s*b,P(0))for a,b in B]+[(P(0),P(0),P(1)),(l,P(0),P(1)),(P(0),l,P(1))]
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=area*s*s/3+l/6
    J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
       s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,area*s*s/12+l/12+l*l/24)
    vf=P();jf=[P()for _ in range(3)]
    for ids in FAN:
        a,b,c,d=(Z[i]for i in ids);vv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6;vf+=vv
        for k in range(3):jf[k]+=vv*sum(Z[i][k]for i in ids)/4
    assert vf==V and all(jf[k]==J[k]for k in range(3))
    G=[]
    for i,j in ARROWS:
        u=tuple(V*Z[i][k]-J[k]for k in range(3));d=sub(Z[j],Z[i])
        G.append([-(u[a]*d[b]+u[b]*d[a])/2 for a,b in PAIRS])
    assert len(EDGES)==17 and len(G)==34
    assert all(k[0]<=3 and k[1]<=3 and k[2]+k[3]<=3 and k[4]<=4 for row in G for pol in row for k in pol.d)
    return G

def univ(a,b,n,i,k):
    return sum((F(comb(k,h)*comb(i,h),comb(n,h))*a**(k-h)*(b-a)**h for h in range(min(k,i)+1)),F(0))
def transform(keys,box):
    U=[{(i,k):univ(a,b,n,i,k)for i in range(n+1)for k in range(n+1)}for(a,b),n in zip(box,(3,3,4))]
    T={(i,j,a,b):F(comb(i,a)*comb(j,b),comb(3,a+b)*comb(a+b,a))if a<=i and b<=j else F(0)for i,j in TRI for a in range(4)for b in range(4-a)}
    return np.array([[U[0][ix,k[0]]*U[1][ir,k[1]]*T[ip,iq,k[2],k[3]]*U[2][il,k[4]]for k in keys]for ix,ir,(ip,iq),il in INDICES],object)
def padd(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return{k:v for k,v in c.items()if v}
def pmul(a,b):
    c={}
    for(i,j),v in a.items():
        for(k,l),w in b.items():c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*w
    return{k:v for k,v in c.items()if v}
def ppow(a,n):
    z={(0,0):F(1)}
    for _ in range(n):z=pmul(z,a)
    return z
def transition(vertices):
    (a,b),(c,d),(e,f)=vertices
    p={(0,0):a,(1,0):c-a,(0,1):e-a};q={(0,0):b,(1,0):d-b,(0,1):f-b}
    rest=padd({(0,0):F(1)},{k:-v for k,v in padd(p,q).items()})
    S=np.empty((10,10),object)
    for col,(i,j)in enumerate(TRI):
        poly=pmul(pmul(ppow(p,i),ppow(q,j)),ppow(rest,3-i-j));fac=F(factorial(3),factorial(i)*factorial(j)*factorial(3-i-j))
        for row,(u,v)in enumerate(TRI):
            S[row,col]=fac*sum((w*F(comb(u,k)*comb(v,l),comb(3,k+l)*comb(k+l,k))for(k,l),w in poly.items()if k<=u and l<=v),F(0))
    assert all(x>=0 for x in S.flat)and all(sum(row)==1 for row in S)
    return S

def raw_coeff(G):
    keys=sorted({k for row in G for pol in row for k in pol.d})
    C=np.array([[pol.d.get(k,F(0))for row in G for pol in row]for k in keys],object)
    return keys,C

def tensor_from_coeff(keys,C,box=BOX,triangle=FULL,exact=False):
    T=transform(keys,box);S=transition(triangle)
    if exact:
        dc=lcm(*(v.denominator for v in C.flat));dt=lcm(*(v.denominator for v in T.flat));ds=lcm(*(v.denominator for v in S.flat))
        ci=np.array([int(v*dc)for v in C.flat],object).reshape(C.shape)
        ti=np.array([int(v*dt)for v in T.flat],object).reshape(T.shape)
        si=np.array([int(v*ds)for v in S.flat],object).reshape(S.shape)
        K=(ti@ci).reshape(4,4,10,5,34,6)
        K=(si@K.transpose(2,0,1,3,4,5).reshape(10,-1)).reshape(10,4,4,5,34,6).transpose(1,2,0,3,4,5).reshape(800,34,6)
        return K,dc*dt*ds
    K=(np.array(T,float)@np.array(C,float)).reshape(4,4,10,5,34,6)
    K=np.einsum('uv,abvcej->abucej',np.array(S,float),K).reshape(800,34,6)
    M=np.zeros((800,34,3,3))
    for k,(a,b)in enumerate(PAIRS):M[:,:,a,b]=K[:,:,k];M[:,:,b,a]=K[:,:,k]
    return M

def trees():
    arr=[];masks=[];roots=[];geom=[];aid={e:i for i,e in enumerate(ARROWS)}
    for chosen in combinations(EDGES,9):
        adj=[[]for _ in range(10)]
        for a,b in chosen:adj[a].append(b);adj[b].append(a)
        seen={0};queue=[0]
        for a in queue:
            for b in adj[a]:
                if b not in seen:seen.add(b);queue.append(b)
        if len(seen)!=10:continue
        for root in range(10):
            out={};queue=[root]
            for a in queue:
                for b in adj[a]:
                    if b!=root and b not in out:out[b]=a;queue.append(b)
            ids=sorted(aid[e]for e in out.items());assert len(ids)==9
            arr.append(ids);masks.append(sum(1<<i for i in ids));roots.append(root)
            geom.append(root>=7 or(len(adj[root])==1 and adj[root][0]>=7))
    assert len(arr)==48790 and len(set(masks))==48790 and sum(geom)==19554
    return np.array(arr,np.int16),np.array(masks,np.uint64),np.array(roots,np.int8),np.array(geom,bool)

def find(B,maxiter=35):
    from scipy.optimize import linprog
    edges=B.shape[1];rows=[]
    for v in np.eye(3):rows.extend(np.einsum('i,neij,j->ne',v,B,v).tolist())
    rows=np.unique(np.round(rows,15),axis=0).tolist();scale=1000.
    for step in range(maxiter):
        C=np.array(rows)*scale
        lp=linprog(np.r_[np.zeros(edges),-1.],A_ub=np.column_stack([-C,np.ones(len(rows))]),b_ub=np.zeros(len(rows)),A_eq=[np.r_[np.ones(edges),0]],b_eq=[1],bounds=[(0,None)]*edges+[(None,None)],method='highs')
        if not lp.success:return None,{'error':lp.message}
        w=lp.x[:edges];M=np.einsum('neij,e->nij',B,w);ev,evec=np.linalg.eigh(M);low=float(ev[:,0].min());bound=float(lp.x[-1])/scale
        if low>2e-9:return w,{'low':low,'bound':bound,'steps':step+1}
        if bound<1e-10:return None,{'low':low,'bound':bound,'steps':step+1}
        bad=np.where(ev[:,0]<bound-max(1e-11,abs(bound)*1e-4))[0]
        if not len(bad):return None,{'low':low,'bound':bound,'steps':step+1}
        new=[np.einsum('i,eij,j->e',evec[n,:,0],B[n],evec[n,:,0])for n in bad]
        rows.extend(np.unique(np.round(new,14),axis=0).tolist())
    return None,{'low':low,'bound':bound,'steps':maxiter}

def check_rows(K,L,records,bits=40):
    mins=[None]*3
    for pairs in records:
        W=sum(w for i,w in pairs);C=sum(w*K[:,i,:]for i,w in pairs)
        for row in C:
            a,b,c,d,e,f=(int(v)*(1<<bits)for v in row);a-=W*L;d-=W*L;f-=W*L
            values=(a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
            assert min(values)>0
            for j,v in enumerate(values):mins[j]=v if mins[j]is None else min(mins[j],v)
    return mins

def write_json(path,obj):path.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':
    G=geometry();keys,C=raw_coeff(G);print('POLYNOMIALS',len(G),len(keys),flush=True)
    Ts,masks,roots,geom=trees();print('TREES',len(Ts),'GEOMETRIC',sum(geom),flush=True)
    target=int(sys.argv[1])if len(sys.argv)>1 else 0
    B=tensor_from_coeff(keys,C,triangle=UPPER[target]);np.save('/mnt/data/upper_tensor_'+str(target)+'.npy',B)
    np.savez('/mnt/data/tree_cache.npz',Ts=Ts,masks=masks,roots=roots,geom=geom)
    print('TENSOR',B.shape,flush=True)
