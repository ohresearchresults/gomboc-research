# material-83638e66cfb7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""H5 macro-r half-triangle all-root certificate.
Default verification uses exact polynomial, integer-matrix and graph arithmetic.
The optional find() helper proposes stresses numerically; it is not proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import json, hashlib, time, sys
import numpy as np
DIM=5; ZERO=(0,)*DIM
class P:
    def __init__(self,x=0):
        if isinstance(x,P): self.d=x.d.copy()
        elif isinstance(x,dict): self.d={k:F(v) for k,v in x.items() if v}
        else: self.d={} if not x else {ZERO:F(x)}
    def __add__(self,b):
        d=self.d.copy()
        for k,v in P(b).d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b): return self+-P(b)
    def __rsub__(self,b): return P(b)+-self
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for l,w in P(b).d.items():
                kl=tuple(a+c for a,c in zip(k,l)); d[kl]=d.get(kl,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b): return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n): z=z*self
        return z
    def __eq__(self,b): return self.d==P(b).d
    def value(self,pt): return sum((v*prod(a**b for a,b in zip(pt,k)) for k,v in self.d.items()),F(0))
def prod(xs):
    z=1
    for x in xs:z*=x
    return z
def variable(i):
    k=[0]*DIM;k[i]=1;return P({tuple(k):1})
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),(0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b))) for face in FACES for a,b in zip(face,face[1:]+face[:1])}))
ARROWS=tuple(sorted([e for a,b in EDGES for e in [(a,b),(b,a)]]))
PAIRS=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
BOX=((F(15,16),F(1)),(F(1,4),F(1,2)),(F(0),F(1,64)))
DEG=(3,3,4)
TRI=tuple((i,j) for i in range(4)for j in range(4-i))
INDICES=tuple(product(range(4),range(4),TRI,range(5)))
def geometry():
    x,r,p,q,l=(variable(i)for i in range(5));s=1-l
    B=((P(F(1,4)),P(0)),(1-3*x/4,P(0)),(1-p,p),(q,1-q),(P(0),1-3*r/4),(P(0),P(F(1,4))),(P(F(1,16)),P(F(1,16))))
    z=[(s*a,s*b,P(0))for a,b in B]+[(P(0),P(0),P(1)),(l,P(0),P(1)),(P(0),l,P(1))]
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=area*s*s/3+l/6
    J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,area*s*s/12+l/12+l*l/24)
    vf=P(0); jf=[P(0)for _ in range(3)]
    for ids in FAN:
        a,b,c,d=(z[i]for i in ids)
        vol=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6;vf+=vol
        for k in range(3):jf[k]+=vol*sum(z[i][k]for i in ids)/4
    assert vf==V and all(jf[k]==J[k]for k in range(3))
    G=[]
    for i,j in ARROWS:
        u=tuple(V*z[i][k]-J[k]for k in range(3));d=sub(z[j],z[i])
        G.append([-(u[a]*d[b]+u[b]*d[a])/2 for a,b in PAIRS])
    assert len(EDGES)==17 and len(ARROWS)==34
    for row in G:
        for poly in row:
            assert all(k[0]<=3 and k[1]<=3 and k[2]+k[3]<=3 and k[4]<=4 for k in poly.d)
    perm=(5,4,3,2,1,0,6,7,9,8)
    def reflected(poly):
        return P({(k[1],k[0],k[3],k[2],k[4]):v for k,v in poly.d.items()})
    assert all(reflected(z[perm[i]][k])==z[i][(1,0,2)[k]] for i in range(10) for k in range(3))
    assert reflected(V)==V and all(reflected(J[k])==J[(1,0,2)[k]] for k in range(3))
    assert {tuple(sorted((perm[a],perm[b])))for a,b in EDGES}==set(EDGES)
    return G

def univ(a,b,n,i,k):
    return sum((F(comb(k,h)*comb(i,h),comb(n,h))*a**(k-h)*(b-a)**h for h in range(min(k,i)+1)),F(0))
def transform(keys,box=BOX,exact=False):
    U=[{(i,k):univ(a,b,n,i,k) for i in range(n+1)for k in range(n+1)} for (a,b),n in zip(box,DEG)]
    tb={(i,j,a,b):F(comb(i,a)*comb(j,b),comb(3,a+b)*comb(a+b,a)) if a<=i and b<=j else F(0) for i,j in TRI for a in range(4)for b in range(4-a)}
    return np.array([[U[0][ix,k[0]]*U[1][ir,k[1]]*tb[ip,iq,k[2],k[3]]*U[2][il,k[4]] for k in keys] for ix,ir,(ip,iq),il in INDICES],dtype=object if exact else float)
def tensor(G,box=BOX):
    keys=sorted({k for row in G for p in row for k in p.d})
    coeff=np.array([[[p.d.get(k,F(0)) for p in row]for row in G] for k in keys],float)
    vals=(transform(keys,box)@coeff.reshape(len(keys),-1)).reshape(len(INDICES),34,6)
    mats=np.zeros((len(INDICES),34,3,3))
    for e,(i,j) in enumerate(PAIRS):mats[:,:,i,j]=vals[:,:,e];mats[:,:,j,i]=vals[:,:,e]
    return mats

def trees():
    arr=[];masks=[]; roots=[]
    aid={e:i for i,e in enumerate(ARROWS)}
    for es in combinations(EDGES,9):
        adj=[[]for _ in range(10)]
        for a,b in es:adj[a].append(b);adj[b].append(a)
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
            ids=sorted(aid[e]for e in out.items())
            assert len(ids)==9
            arr.append(ids);masks.append(sum(1<<i for i in ids));roots.append(root)
    assert len(arr)==48790 and len(set(masks))==48790
    return np.array(arr,np.int16),np.array(masks,np.uint64),np.array(roots,np.int8)

def find(B,maxiter=35):
    from scipy.optimize import linprog
    # Common PD combination of all original coefficient matrices. Locator only.
    edges=B.shape[1]; rows=[]
    for v in np.eye(3): rows.extend(np.einsum('i,neij,j->ne',v,B,v).tolist())
    rows=np.unique(np.round(rows,15),axis=0).tolist()
    scale=1000.0
    for step in range(maxiter):
        C=np.array(rows)*scale
        cons=np.column_stack([-C,np.ones(len(rows))])
        lp=linprog(np.r_[np.zeros(edges),-1.],A_ub=cons,b_ub=np.zeros(len(rows)),A_eq=[np.r_[np.ones(edges),0]],b_eq=[1],bounds=[(0,None)]*edges+[(None,None)],method='highs')
        if not lp.success:return None,{'error':lp.message}
        w=lp.x[:edges];m=np.einsum('neij,e->nij',B,w);ev,evec=np.linalg.eigh(m); low=float(ev[:,0].min());bound=float(lp.x[-1])/scale
        if low>2e-9:return w,{'low':low,'bound':bound,'steps':step+1}
        if bound<1e-10:return None,{'low':low,'bound':bound,'steps':step+1}
        bad=np.where(ev[:,0]<bound-max(1e-11,abs(bound)*1e-4))[0]
        if not len(bad):return None,{'low':low,'bound':bound,'steps':step+1}
        # Coincident coefficient eigenvectors give duplicate linear constraints.
        new=[]
        for n in bad:
            v=evec[n,:,0];new.append(np.einsum('i,eij,j->e',v,B[n],v))
        rows.extend(np.unique(np.round(new,14),axis=0).tolist())
    return None,{'low':low,'bound':bound,'steps':maxiter}

def save(path,obj): path.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')

from math import factorial, lcm
def padd(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items()if v}
def pmul(a,b):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in c.items()if v}
def ppow(a,n):
    z={(0,0):F(1)}
    for _ in range(n):z=pmul(z,a)
    return z
def transition(vertices):
    (a,b),(c,d),(e,f)=vertices
    p={(0,0):a,(1,0):c-a,(0,1):e-a};q={(0,0):b,(1,0):d-b,(0,1):f-b}
    rest=padd({(0,0):F(1)},{k:-v for k,v in padd(p,q).items()})
    S=np.empty((10,10),dtype=object)
    for col,(i,j)in enumerate(TRI):
        poly=pmul(pmul(ppow(p,i),ppow(q,j)),ppow(rest,3-i-j));fac=F(factorial(3),factorial(i)*factorial(j)*factorial(3-i-j))
        for row,(u,v)in enumerate(TRI):
            S[row,col]=fac*sum((w*F(comb(u,k)*comb(v,l),comb(3,k+l)*comb(k+l,k))for (k,l),w in poly.items()if k<=u and l<=v),F(0))
    assert all(x>=0 for x in S.flat)and all(sum(row)==1 for row in S)
    return S

def local_tensor(B,vertices):
    S=np.array(transition(vertices),float)
    BB=B.reshape(4,4,10,5,34,3,3)
    return np.einsum('uv,abvceij->abuceij',S,BB).reshape(800,34,3,3)


def build_integer_tensor():
    G=geometry();keys=sorted({k for row in G for p in row for k in p.d})
    C=[[p.d.get(k,F(0)) for row in G for p in row] for k in keys]
    dc=lcm(*(v.denominator for row in C for v in row))
    ci=np.array([[int(v*dc)for v in row]for row in C],dtype=object)
    T=transform(keys,exact=True)
    dt=lcm(*(v.denominator for v in T.flat))
    ti=np.array([[int(v*dt)for v in row]for row in T],dtype=object)
    K=(ti@ci).reshape(len(INDICES),34,6)
    return K,dc*dt


TRIANGLE=((F(0),F(0)),(F(1,2),F(0)),(F(0),F(1,2)))
GAP_BITS=34
def read_weights(path):
    records=[]
    for line in path.read_text().splitlines():
        if not line.strip():continue
        pairs=[tuple(map(int,t.split(':')))for t in line.split()]
        assert pairs and len({i for i,w in pairs})==len(pairs)
        assert all(0<=i<34 and w>0 for i,w in pairs)
        records.append(pairs)
    return records

def verify(path,out):
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    records=read_weights(path);K,L=build_integer_tensor()
    S=transition(TRIANGLE);ds=lcm(*(v.denominator for v in S.flat))
    si=np.array([[int(v*ds)for v in row]for row in S],dtype=object)
    K=(si@K.reshape(4,4,10,5,34,6).transpose(2,0,1,3,4,5).reshape(10,-1)).reshape(10,4,4,5,34,6).transpose(1,2,0,3,4,5).reshape(800,34,6);L*=ds
    Ts,masks,roots=trees();covered=np.zeros(len(Ts),bool);step=1<<GAP_BITS;mins=[None]*3
    for pairs in records:
        W=sum(w for i,w in pairs);C=sum(w*K[:,i,:]for i,w in pairs)
        for row in C:
            a,b,c,d,e,f=(int(v)*step for v in row);a-=W*L;d-=W*L;f-=W*L
            vals=(a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
            assert min(vals)>0
            for j,v in enumerate(vals):
                if mins[j]is None or v<mins[j]:mins[j]=v
        mask=np.uint64(sum(1<<i for i,w in pairs));covered|=(masks&mask)==mask
    assert len(records)==303 and covered.all()
    raw=path.read_bytes()
    report={'title':'H5_MACRO_R_HALF_TRIANGLE_ALLROOT_V1',
        'box_x_r_lambda':[[str(a),str(b)]for a,b in BOX],
        'physical_triangle':[[str(a),str(b)]for a,b in TRIANGLE],
        'facets':FACES,'edges':EDGES,'arrows':ARROWS,
        'actual_moments':'Four original five-variable fan identities and34 reflection identities hold exactly.',
        'tensor_degrees_x_r_pq_lambda':[3,3,3,4],
        'stress_count':len(records),'coefficient_matrices':800*len(records),
        'positive_shifted_leading_minors':2400*len(records),
        'coefficient_denominator':str(L),'gap_per_total_weight':f'1/{step}',
        'minimum_integer_shifted_minors':list(map(str,mins)),
        'complete_rooted_trees':len(Ts),'covered_rooted_trees':int(covered.sum()),
        'covered_by_root':{str(r):int(covered[roots==r].sum())for r in range(10)},
        'weighted_mean_arrow_bound':f'< -3 trace(M)/{1<<(GAP_BITS-1)} for every nonzero PSD M',
        'weights_bytes':len(raw),'weights_sha256':hashlib.sha256(raw).hexdigest(),
        'boundary_semantics':'Collapsed indexed limits are algebraic; a proper10/17/9 claim requires the strict physical parameter conditions.',
        'scope':'This half-triangle prism and its physically reflected prism only; not the whole H5 class, not allE17, not a new global complexity bound.'}
    b=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();out.write_bytes(b)
    print('H5_MACRO_R_HALF_TRIANGLE_ALLROOT_PASS',len(records),800*len(records),2400*len(records),len(Ts))
    print('REPORT_BYTES_SHA256',len(b),hashlib.sha256(b).hexdigest())

def main():
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('weights',type=Path);ap.add_argument('--out',type=Path,default=Path('h5_half_triangle_report.json'))
    args=ap.parse_args();verify(args.weights,args.out)
if __name__=='__main__':main()
