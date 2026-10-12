# material-9e76632309f3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact source-subtree reflection cuts for the literal H5 family.
Python >=3.11; standard library, assertions enabled. No external inputs.
Actual geometry/moments: minimum-0245, immutable result
SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be.
This is a new local-cut certificate, not a replay of that parent's computation.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, lcm
from pathlib import Path
import argparse, hashlib, json

ZERO = (0,) * 5
FACES = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
         (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN = ((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
       (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES = tuple(sorted({tuple(sorted((a,b))) for f in FACES
                    for a,b in zip(f, f[1:]+f[:1])}))
TOP = (7,8,8,9,9,7,7)
PARENT_SUPPORT = {(0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0)}

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
            for j,w in P(b).d.items():
                z=tuple(a+c for a,c in zip(k,j))
                d[z]=d.get(z,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b): return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n): z=z*self
        return z
    def __eq__(self,b): return self.d==P(b).d

def var(i):
    k=[0]*5; k[i]=1
    return P({tuple(k):1})
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def geometry(pt):
    x,r,p,q,z=pt; s=1-z
    B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
       (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
    X=tuple((s*a,s*b,0) for a,b in B)+((0,0,1),(z,0,1),(0,z,1))
    A=(31-24*x*p-24*r*q)/64
    Bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    By=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=A*s*s/3+z/6
    J=(s**3*Bx/4+s*s*z*(1-3*x*p/4)/24+z*z/24,
       s**3*By/4+s*s*z*(1-3*r*q/4)/24+z*z/24,
       A*s*s/12+z/12+z*z/24)
    return B,X,V,J

def guard_polynomials():
    pt=tuple(var(i) for i in range(5)); lam=pt[4]; s=1-lam
    B,X,V,J=geometry(pt)
    v=P(); j=[P(),P(),P()]
    for ids in FAN:
        a,b,c,d=(X[i] for i in ids)
        dv=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
        v+=dv
        for k in range(3): j[k]+=dv*sum(X[i][k] for i in ids)/4
    assert v==V and all(j[k]==J[k] for k in range(3))
    labels=[]; guards=[]
    for target,i,j in product(range(7),repeat=3):
        if i==j: continue
        n=(B[j][1]-B[i][1],B[i][0]-B[j][0])
        h=dot(n,B[i]); a=X[TOP[target]][:2]
        R=V*s*h-2*dot(n,J[:2])+2*J[2]*dot(n,a)
        R+=(V-2*J[2])*s*dot(n,B[target])
        labels.append((target,i,j)); guards.append(R)
    return labels,guards

def interval_factor(i,n,a,lo,hi):
    return sum(F(comb(a,k)*comb(i,k),comb(n,k))*lo**(a-k)*(hi-lo)**k
               for k in range(min(i,a)+1))

def coefficients(polys,box):
    keys=sorted({k for p in polys for k in p.d})
    nx=max(k[0] for k in keys); nr=max(k[1] for k in keys)
    nt=max(k[2]+k[3] for k in keys); nl=max(k[4] for k in keys)
    tri=tuple((i,j) for i in range(nt+1) for j in range(nt+1-i))
    indices=tuple(product(range(nx+1),range(nr+1),tri,range(nl+1)))
    C=[[p.d.get(k,F(0)) for p in polys] for k in keys]
    T=[]
    for i,j,(u,v),w in indices:
        row=[]
        for a,b,c,d,e in keys:
            if c>u or d>v or e>w: row.append(F(0)); continue
            z=interval_factor(i,nx,a,*box[0])*interval_factor(j,nr,b,*box[1])
            z*=F(comb(u,c)*comb(v,d),comb(nt,c+d)*comb(c+d,c))
            z*=F(comb(w,e),comb(nl,e))*box[2][1]**e
            row.append(z)
        T.append(row)
    dc=lcm(*(v.denominator for row in C for v in row))
    dt=lcm(*(v.denominator for row in T for v in row))
    CI=[[int(v*dc) for v in row] for row in C]
    ans=[]
    for row in T:
        nz=[(k,int(v*dt)) for k,v in enumerate(row) if v]
        ans.append([sum(t*CI[k][j] for k,t in nz) for j in range(len(polys))])
    return ans,dc*dt,indices,(nx,nr,nt,nl)

def strict_faces(box,degrees):
    nx,nr,nt,nl=degrees
    opts=[]
    for interval,n in zip(box[:2],(nx,nr)):
        o=[None]
        if interval[0]>0: o.append(0)
        if interval[1]<1: o.append(n)
        opts.append(o)
    # lambda=0 is not a genuine H5 body. Upper endpoint is included.
    return tuple(product(opts[0],opts[1],(None,nl)))

def strict_guard(col,indices,faces):
    if min(col)<0: return False
    for i,j,w in faces:
        if not any(c>0 for c,(a,b,_,d) in zip(col,indices)
                   if (i is None or a==i) and (j is None or b==j)
                   and (w is None or d==w)):
            return False
    return True

def all_trees(good):
    # good[(b,S)] supplies strict containment w(b,TOP[b]) in conv(B[S]).
    rooted_counts=[0]*10; old_counts=[0]*10; new_counts=[0]*10
    union_counts=[0]*10; all_union=[0]*10; cut_uses={}; examples=[]
    n=0; tree_rows=[]
    for edges in combinations(EDGES,9):
        adj=[[] for _ in range(10)]
        for a,b in edges: adj[a].append(b);adj[b].append(a)
        seen={0}; todo=[0]
        for a in todo:
            for b in adj[a]:
                if b not in seen: seen.add(b);todo.append(b)
        if len(seen)<10: continue
        n+=1
        cuts=[]
        for b,a in enumerate(TOP):
            if b not in adj[a]: continue
            comp={a}; todo=[a]
            for u in todo:
                for v in adj[u]:
                    if (u==a and v==b) or v in comp: continue
                    comp.add(v);todo.append(v)
            S=tuple(sorted({b}|{v for v in comp if v<7}))
            if (b,S) in good: cuts.append((b,S,comp))
        for root in range(10):
            parent={};seen={root};todo=[root]
            for a in todo:
                for b in adj[a]:
                    if b not in seen:seen.add(b);todo.append(b);parent[b]=a
            rooted_counts[root]+=1
            old=root>=7 or (root<7 and len(adj[root])==1 and adj[root][0]>=7)
            old_counts[root]+=old
            hits=[(b,S) for b,S,comp in cuts if root not in comp]
            new=bool(hits);new_counts[root]+=new
            union_counts[root]+=bool(old or new)
            old20=PARENT_SUPPORT.issubset(parent.items())
            all_union[root]+=bool(old or new or old20)
            if new and not old:
                for h in hits:cut_uses[h]=cut_uses.get(h,0)+1
                if len(examples)<5:examples.append({'root':root,'arrows':sorted(parent.items()),'cut':hits[0]})
            tree_rows.append([root,sorted(parent.items()),int(old),int(new),int(old20)])
    assert n==4879 and rooted_counts==[4879]*10
    assert sum(old_counts)==19554
    return {'unrooted':n,'rooted':sum(rooted_counts),'old_by_root':old_counts,
            'local_by_root':new_counts,'union_by_root':union_counts,
            'union_with_parent20_by_root':all_union,'local_only_new':sum(union_counts)-19554,
            'union':sum(union_counts),'union_with20':sum(all_union),
            'remaining_with20':48790-sum(all_union),'examples':examples,
            'cut_uses':[[list(k),v] for k,v in sorted(cut_uses.items())],
            'tree_stream_sha256':hashlib.sha256(json.dumps(tree_rows,separators=(',',':')).encode()).hexdigest()}

def clean(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    return x

def save(path,obj):
    raw=(json.dumps(clean(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    path.write_bytes(raw)
    return {'filename':path.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def main(out,mode,lambda_max):
    if not __debug__:raise RuntimeError('Assertions must be enabled; do not use -O.')
    assert F(0)<lambda_max<=F(1,16)
    box=((F(0),F(1)),(F(0),F(1)),(F(0),lambda_max)) if mode=='full' else \
        ((F(15,16),F(1)),(F(1,4),F(1,2)),(F(0),lambda_max))
    labels,polys=guard_polynomials(); nums,den,indices,degrees=coefficients(polys,box)
    assert degrees==(2,2,2,3) and len(labels)==294 and len(indices)==216
    assert F(7,32)*(1-lambda_max)**2>lambda_max**2
    faces=strict_faces(box,degrees)
    accepted={label for i,label in enumerate(labels)
              if strict_guard([row[i] for row in nums],indices,faces)}
    good={}; all_subsets=[]
    for size in range(3,8):
        for S in combinations(range(7),size):
            for b in S:
                guards=[(b,i,j) for i,j in zip(S,S[1:]+S[:1])]
                if all(g in accepted for g in guards):
                    good[(b,S)]=guards;all_subsets.append([b,S])
    report={'scope':'Genuine H5 bodies only: strict physical x,r,p,q and lambda>0, plus closed stated macro bounds.',
            'mode':mode,'parameter_box_x_r_lambda':box,
            'parent20_union_scope':'Counts involving parent20 are valid only on the intersection with its x/r prism and lambda<=1/64.','triangle':'p>0,q>0,p+q<1',
            'degrees':degrees,'guards':len(labels),'indices':len(indices),
            'accepted_chord_guards':len(accepted),'certified_target_subsets':all_subsets,
            'strict_parameter_faces':faces,'census':all_trees(good)}
    if lambda_max in (F(1,64),F(1,16)):
        expected=(64,14,22941,3387) if mode=='full' else (86,43,26409,6855)
        assert (len(accepted),len(good),report['census']['union'],
                report['census']['local_only_new'])==expected
    out.mkdir(parents=True,exist_ok=True)
    pin=save(out/'local_reflection_coefficients.json',{'guard_order':labels,'indices':indices,
             'common_denominator':den,'coefficients':nums,'accepted':sorted(accepted)})
    report['coefficients']=pin
    reportpin=save(out/'local_reflection_report.json',report)
    print(json.dumps(clean(report['census']),sort_keys=True))
    print('H5_LOCAL_SUBTREE_REFLECTION_PASS',mode,len(labels),len(indices),len(accepted),len(good),report['census']['union'])
    print(json.dumps({'report':reportpin,'coefficients':pin},sort_keys=True))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=('full','prism'),default='full')
    ap.add_argument('--out',type=Path,default=Path('h5-local-output'))
    ap.add_argument('--lambda-max',type=F,default=F(1,16))
    args=ap.parse_args();main(args.out,args.mode,args.lambda_max)
